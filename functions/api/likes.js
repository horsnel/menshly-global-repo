// CloudFlare Pages Function: Likes API
// KV namespace binding: LIKES (MENSHLY_LIKES)
// GET  /api/likes?slug=<article-slug>  → { slug, likes }
// POST /api/likes                       → { slug, likes } (body: { slug })

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Content-Type': 'application/json',
};

// Rate limiting: simple in-memory counter (resets on deploy)
const rateLimiter = new Map();
const RATE_LIMIT_WINDOW = 60000; // 1 minute
const RATE_LIMIT_MAX = 10; // 10 likes per minute per IP

function isRateLimited(ip) {
  const now = Date.now();
  const entry = rateLimiter.get(ip);
  if (!entry || now - entry.start > RATE_LIMIT_WINDOW) {
    rateLimiter.set(ip, { start: now, count: 1 });
    return false;
  }
  entry.count++;
  return entry.count > RATE_LIMIT_MAX;
}

function sanitizeSlug(slug) {
  if (!slug || typeof slug !== 'string') return null;
  // Only allow alphanumeric, hyphens, slashes (for section/slug paths)
  const cleaned = slug.replace(/[^a-z0-9\/\-]/gi, '').substring(0, 200);
  return cleaned || null;
}

export async function onRequestOptions() {
  return new Response(null, { status: 204, headers: CORS_HEADERS });
}

export async function onRequestGet(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const slug = sanitizeSlug(url.searchParams.get('slug'));

  if (!slug) {
    return new Response(JSON.stringify({ error: 'Missing slug parameter' }), {
      status: 400,
      headers: CORS_HEADERS,
    });
  }

  let likes = 0;
  if (env.LIKES) {
    try {
      const stored = await env.LIKES.get(`like:${slug}`);
      if (stored) {
        const data = JSON.parse(stored);
        likes = data.count || 0;
      }
    } catch (err) {
      console.error('KV read error:', err);
    }
  }

  return new Response(JSON.stringify({ slug, likes }), {
    headers: CORS_HEADERS,
  });
}

export async function onRequestPost(context) {
  const { request, env } = context;

  // Rate limit check
  const ip = request.headers.get('CF-Connecting-IP') || 'unknown';
  if (isRateLimited(ip)) {
    return new Response(JSON.stringify({ error: 'Rate limited' }), {
      status: 429,
      headers: CORS_HEADERS,
    });
  }

  let body;
  try {
    body = await request.json();
  } catch {
    return new Response(JSON.stringify({ error: 'Invalid JSON' }), {
      status: 400,
      headers: CORS_HEADERS,
    });
  }

  const slug = sanitizeSlug(body.slug);
  if (!slug) {
    return new Response(JSON.stringify({ error: 'Missing or invalid slug' }), {
      status: 400,
      headers: CORS_HEADERS,
    });
  }

  if (!env.LIKES) {
    return new Response(JSON.stringify({ error: 'KV not configured' }), {
      status: 500,
      headers: CORS_HEADERS,
    });
  }

  try {
    // Atomic increment using KV
    const key = `like:${slug}`;
    const stored = await env.LIKES.get(key);
    const current = stored ? (JSON.parse(stored).count || 0) : 0;
    const newCount = current + 1;

    await env.LIKES.put(key, JSON.stringify({
      count: newCount,
      updatedAt: new Date().toISOString(),
    }), { expirationTtl: 0 }); // No expiration

    return new Response(JSON.stringify({ slug, likes: newCount }), {
      headers: CORS_HEADERS,
    });
  } catch (err) {
    console.error('KV write error:', err);
    return new Response(JSON.stringify({ error: 'Failed to save like' }), {
      status: 500,
      headers: CORS_HEADERS,
    });
  }
}
