// CloudFlare Pages Function: TTS API
// POST /api/tts  →  Returns guidance to use browser speechSynthesis
// The primary TTS is now Microsoft Speech via the browser's Web Speech API
// (speechSynthesis). This endpoint exists as a fallback marker and for
// any future cloud TTS integration.

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

export async function onRequestOptions() {
  return new Response(null, { status: 204, headers: CORS_HEADERS });
}

export async function onRequestPost(context) {
  // The client now uses browser speechSynthesis (Microsoft TTS) directly.
  // This endpoint returns a message indicating the client should use browser TTS.
  return new Response(JSON.stringify({
    error: 'Cloud TTS is not the primary provider. Use browser speechSynthesis (Microsoft TTS) instead.',
    useBrowserTTS: true
  }), {
    status: 503,
    headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
  });
}
