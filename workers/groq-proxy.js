/**
 * Groq API Proxy Worker
 *
 * Routes requests to api.groq.com from Cloudflare's edge network,
 * bypassing geo-restrictions on the Groq API.
 *
 * Security: Only proxies to api.groq.com, rejects all other targets.
 * Auth: Validates the Groq API key from the incoming request.
 */

export default {
  async fetch(request, env) {
    // Only allow POST requests
    if (request.method !== 'POST') {
      return new Response(JSON.stringify({ error: 'Method not allowed' }), {
        status: 405,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    // Get the path from the URL (everything after /groq-proxy)
    const url = new URL(request.url);
    const targetPath = url.pathname.replace(/^\/groq-proxy/, '') || '/openai/v1/chat/completions';

    // Only allow specific Groq API paths
    const allowedPaths = [
      '/openai/v1/chat/completions',
      '/openai/v1/models',
      '/v1/chat/completions',
      '/v1/models',
    ];

    if (!allowedPaths.some(p => targetPath.startsWith(p))) {
      return new Response(JSON.stringify({ error: 'Path not allowed' }), {
        status: 403,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    // Get the API key from the request header
    const authHeader = request.headers.get('Authorization') || '';
    const apiKey = authHeader.replace('Bearer ', '').trim();

    if (!apiKey || !apiKey.startsWith('gsk_')) {
      return new Response(JSON.stringify({ error: 'Invalid or missing Groq API key' }), {
        status: 401,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    try {
      // Forward the request to Groq API
      const groqUrl = `https://api.groq.com${targetPath}`;
      const headers = new Headers(request.headers);
      headers.set('Host', 'api.groq.com');
      headers.delete('cf-connecting-ip');
      headers.delete('cf-ipcountry');
      headers.delete('cf-ray');
      headers.delete('cf-visitor');

      const body = await request.text();

      const response = await fetch(groqUrl, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'Content-Type': 'application/json',
        },
        body: body,
      });

      // Return the response from Groq
      const responseHeaders = new Headers();
      responseHeaders.set('Content-Type', response.headers.get('Content-Type') || 'application/json');
      responseHeaders.set('Access-Control-Allow-Origin', '*');
      responseHeaders.set('Access-Control-Allow-Methods', 'POST, OPTIONS');
      responseHeaders.set('Access-Control-Allow-Headers', 'Authorization, Content-Type');

      return new Response(response.body, {
        status: response.status,
        headers: responseHeaders,
      });

    } catch (error) {
      return new Response(JSON.stringify({ error: `Proxy error: ${error.message}` }), {
        status: 502,
        headers: { 'Content-Type': 'application/json' },
      });
    }
  },
};
