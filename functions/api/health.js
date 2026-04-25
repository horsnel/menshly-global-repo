// CloudFlare Pages Function: API Health Check
// GET /api/health — returns which API keys are configured

export async function onRequestGet(context) {
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
  };

  const env = context.env || {};

  return new Response(JSON.stringify({
    status: 'ok',
    services: {
      cerebras: !!env.CEREBRAS_API_KEY,
      deepseek: !!env.DEEPSEEK_API_KEY,
      pexels: !!env.PEXELS_API_KEY,
      pixabay: !!env.PIXABAY_API_KEY,
      paystack: !!env.PAYSTACK_SECRET_KEY,
      email: !!env.EMAIL_API_KEY,
    },
    chat: !!env.CEREBRAS_API_KEY ? 'ready' : 'not_configured',
    articleGenerator: !!env.CEREBRAS_API_KEY ? 'ready' : 'not_configured',
    images: {
      pexels: !!env.PEXELS_API_KEY,
      pixabay: !!env.PIXABAY_API_KEY,
      pollination: true, // Free, no key needed
    },
    timestamp: new Date().toISOString(),
  }), { status: 200, headers });
}
