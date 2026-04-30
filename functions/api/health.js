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
  const hasHF = true; // HuggingFace free tier always available
  const hasFallback1 = !!env.CEREBRAS_API_KEY;
  const hasFallback2 = !!env.DEEPSEEK_API_KEY;

  // Any LLM available = system is connected
  const anyLLM = true; // Pollinations + HuggingFace are always available

  return new Response(JSON.stringify({
    status: 'ok',
    connected: anyLLM,  // Frontend should check THIS
    services: {
      pollinations: true,  // Primary LLM - free, no key
      huggingface: hasHF,  // Free tier always available
      cerebras: hasFallback1,  // Fallback LLM
      deepseek: hasFallback2,  // Fallback LLM
      pexels: !!env.PEXELS_API_KEY,
      pixabay: !!env.PIXABAY_API_KEY,
      paystack: !!env.PAYSTACK_SECRET_KEY,
      email: !!env.EMAIL_API_KEY,
    },
    chat: anyLLM ? 'ready' : 'offline',
    articleGenerator: anyLLM ? 'ready' : 'offline',
    images: {
      pexels: !!env.PEXELS_API_KEY,
      pixabay: !!env.PIXABAY_API_KEY,
      pollination: true,  // Free, no key needed
    },
    timestamp: new Date().toISOString(),
  }), { status: 200, headers });
}
