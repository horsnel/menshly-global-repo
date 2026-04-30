// CloudFlare Pages Function: Debug LLM connectivity
// GET /api/debug-llm — tests Pollinations AI from the edge

export async function onRequestGet(context) {
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
  };

  const results = {};

  // Test 1: Simple Pollinations text request
  try {
    const t0 = Date.now();
    const resp = await fetch('https://text.pollinations.ai/openai', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        messages: [
          { role: 'system', content: 'You are a helpful assistant.' },
          { role: 'user', content: 'Say hello in one word.' }
        ],
        model: 'openai',
        max_tokens: 20,
      }),
    });
    const elapsed = Date.now() - t0;
    const text = await resp.text();

    results.pollinations = {
      status: resp.status,
      ok: resp.ok,
      elapsed_ms: elapsed,
      response_preview: text.substring(0, 300),
    };
  } catch (e) {
    results.pollinations = { error: e.message, stack: e.stack?.substring(0, 200) };
  }

  // Test 2: Article-style request (longer)
  try {
    const t0 = Date.now();
    const longSystem = 'You are a content writer. Write detailed, specific content about AI business. Use markdown. Include numbers, tool names, and prices.';
    const longUser = 'Write a short article (200 words) about starting an AI chatbot agency. Include pricing, tools, and first steps.';
    const resp = await fetch('https://text.pollinations.ai/openai', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        messages: [
          { role: 'system', content: longSystem },
          { role: 'user', content: longUser }
        ],
        model: 'openai',
        max_tokens: 1000,
      }),
    });
    const elapsed = Date.now() - t0;
    const text = await resp.text();

    results.pollinations_article = {
      status: resp.status,
      ok: resp.ok,
      elapsed_ms: elapsed,
      response_preview: text.substring(0, 300),
    };
  } catch (e) {
    results.pollinations_article = { error: e.message, stack: e.stack?.substring(0, 200) };
  }

  return new Response(JSON.stringify(results, null, 2), { status: 200, headers });
}
