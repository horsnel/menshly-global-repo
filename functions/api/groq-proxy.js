/**
 * Groq API Proxy — Cloudflare Pages Function
 *
 * Routes: /api/groq-proxy
 * Forwards requests to api.groq.com from Cloudflare's edge network,
 * bypassing geo-restrictions on the Groq API.
 *
 * The Groq API key must be passed in the Authorization header.
 */

// Handle all requests — route by method
export async function onRequest(context) {
  const { request } = context;

  // CORS preflight
  if (request.method === 'OPTIONS') {
    return new Response(null, {
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS, GET',
        'Access-Control-Allow-Headers': 'Authorization, Content-Type',
      },
    });
  }

  // Health check
  if (request.method === 'GET') {
    return new Response(JSON.stringify({
      status: 'ok',
      service: 'groq-proxy',
      message: 'Send POST with Authorization: Bearer gsk_... header',
    }), {
      headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' },
    });
  }

  // Only allow POST
  if (request.method !== 'POST') {
    return new Response(JSON.stringify({ error: 'Method not allowed. Use POST.' }), {
      status: 405,
      headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' },
    });
  }

  // Get the API key from the request header
  const authHeader = request.headers.get('Authorization') || '';
  const apiKey = authHeader.replace('Bearer ', '').trim();

  if (!apiKey || !apiKey.startsWith('gsk_')) {
    return new Response(JSON.stringify({ error: 'Invalid or missing Groq API key (must start with gsk_)' }), {
      status: 401,
      headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' },
    });
  }

  try {
    // Parse the request body
    const body = await request.json();

    // Forward to Groq API
    const groqResponse = await fetch('https://api.groq.com/openai/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    });

    const responseData = await groqResponse.json();

    return new Response(JSON.stringify(responseData), {
      status: groqResponse.status,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
    });

  } catch (error) {
    return new Response(JSON.stringify({ error: `Proxy error: ${error.message}` }), {
      status: 502,
      headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' },
    });
  }
}
