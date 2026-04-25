// CloudFlare Pages Function: API Health Check
// GET /api/health — returns which API keys are configured

export async function onRequestGet(context) {
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
  };

  const env = context.env || {};

  // Pollinations AI is always available (free, no key needed)
  const primaryLLM = 'pollinations';
  const hasFallback1 = !!env.CEREBRAS_API_KEY;
  const hasFallback2 = !!env.DEEPSEEK_API_KEY;

  return new Response(JSON.stringify({
    status: 'ok',
    services: {
      pollinations: true,  // Primary LLM - free, no key
      cerebras: hasFallback1,  // Fallback LLM
      deepseek: hasFallback2,  // Fallback LLM
      pexels: !!env.PEXELS_API_KEY,
      pixabay: !!env.PIXABAY_API_KEY,
      paystack: !!env.PAYSTACK_SECRET_KEY,
      email: !!env.EMAIL_API_KEY,
    },
    chat: 'ready',
    articleGenerator: 'ready',
    images: {
      pexels: !!env.PEXELS_API_KEY,
      pixabay: !!env.PIXABAY_API_KEY,
      pollination: true,  // Free, no key needed
    },
    timestamp: new Date().toISOString(),
  }), { status: 200, headers });
}
