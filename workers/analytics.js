// CloudFlare Worker: Lightweight Analytics
// Tracks pageviews via KV, serves stats dashboard
//
// Endpoints:
//   POST /track  — record a pageview
//   GET  /stats  — return analytics data (last 30 days)
//   GET  /       — health check

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Content-Type': 'application/json',
    };

    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }

    // POST /track — record pageview
    if (request.method === 'POST' && url.pathname === '/track') {
      try {
        const data = await request.json();
        const pv = {
          url: data.url || '/',
          referrer: data.referrer || '',
          ua: data.ua || '',
          ts: new Date().toISOString(),
        };

        if (!env.ANALYTICS) {
          return json({ ok: true, note: 'no KV' }, 200, corsHeaders);
        }

        const today = new Date().toISOString().slice(0, 10);
        const key = `pv:${today}`;

        // Append to daily array
        let existing = [];
        try {
          const raw = await env.ANALYTICS.get(key);
          if (raw) existing = JSON.parse(raw);
        } catch {}
        existing.push(pv);
        // Keep last 10000 per day to prevent KV bloat
        if (existing.length > 10000) existing = existing.slice(-10000);
        await env.ANALYTICS.put(key, JSON.stringify(existing), { expirationTtl: 2592000 }); // 30 days

        // Increment path counter
        const countKey = `count:${today}:${pv.url}`;
        const currentCount = parseInt(await env.ANALYTICS.get(countKey) || '0', 10);
        await env.ANALYTICS.put(countKey, String(currentCount + 1), { expirationTtl: 2592000 });

        // Increment daily total
        const totalKey = `total:${today}`;
        const currentTotal = parseInt(await env.ANALYTICS.get(totalKey) || '0', 10);
        await env.ANALYTICS.put(totalKey, String(currentTotal + 1), { expirationTtl: 2592000 });

        return json({ ok: true }, 200, corsHeaders);
      } catch (e) {
        return json({ error: e.message }, 400, corsHeaders);
      }
    }

    // GET /stats — return analytics
    if (request.method === 'GET' && url.pathname === '/stats') {
      const days = Math.min(parseInt(url.searchParams.get('days') || '30', 10), 90);
      const password = url.searchParams.get('password') || '';

      if (env.ADMIN_PASSWORD && password !== env.ADMIN_PASSWORD) {
        return json({ error: 'unauthorized' }, 401, corsHeaders);
      }

      if (!env.ANALYTICS) {
        return json({ daily: [], pages: [] }, 200, corsHeaders);
      }

      const daily = [];
      const pageCounts = {};
      const now = new Date();

      for (let i = 0; i < days; i++) {
        const d = new Date(now);
        d.setDate(d.getDate() - i);
        const dateStr = d.toISOString().slice(0, 10);
        const totalKey = `total:${dateStr}`;
        const count = parseInt(await env.ANALYTICS.get(totalKey) || '0', 10);
        daily.push({ date: dateStr, views: count });

        // List all count keys for this day to get per-page data
        // We'll scan known paths instead (more efficient than list)
      }

      // Get top pages by scanning recent pageview data
      const recentPv = [];
      for (let i = 0; i < Math.min(days, 7); i++) {
        const d = new Date(now);
        d.setDate(d.getDate() - i);
        const dateStr = d.toISOString().slice(0, 10);
        try {
          const raw = await env.ANALYTICS.get(`pv:${dateStr}`);
          if (raw) {
            const pvs = JSON.parse(raw);
            for (const pv of pvs) {
              pageCounts[pv.url] = (pageCounts[pv.url] || 0) + 1;
              if (pv.referrer) {
                // Track referrer sources
              }
            }
          }
        } catch {}
      }

      const pages = Object.entries(pageCounts)
        .map(([url, count]) => ({ url, views: count }))
        .sort((a, b) => b.views - a.views)
        .slice(0, 50);

      const totalViews = daily.reduce((sum, d) => sum + d.views, 0);

      return json({
        totalViews,
        days,
        daily: daily.reverse(),
        pages,
      }, 200, corsHeaders);
    }

    // Health check
    return json({
      status: 'active',
      service: 'Menshly Analytics',
      version: '1.0.0',
    }, 200, corsHeaders);
  },
};

function json(data, status, headers) {
  return new Response(JSON.stringify(data), { status, headers });
}
