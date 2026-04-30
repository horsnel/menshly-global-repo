/**
 * Groq API Proxy — Cloudflare Pages Function
 *
 * Routes: /api/groq-proxy
 * Forwards requests to api.groq.com from Cloudflare's edge network,
 * bypassing geo-restrictions on the Groq API.
 *
 * The Groq API key must be passed in the Authorization header.
 */

export async function onRequestPost(context) {
  const { request } = context;

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
    // Parse the request body to get model and messages
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

// Handle CORS preflight
export async function onRequestOptions() {
  return new Response(null, {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Authorization, Content-Type',
    },
  });
}
