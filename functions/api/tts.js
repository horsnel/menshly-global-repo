/**
 * Cloudflare Pages Function: Professional TTS API
 * Generates natural-sounding audio from text using AI voices.
 *
 * Configure via Cloudflare Pages Environment Variables:
 *   TTS_API_KEY  - API key for the TTS service
 *   TTS_API_URL  - TTS API endpoint URL (e.g., https://api.openai.com/v1/audio/speech)
 *   TTS_VOICE    - Voice name (default: alloy)
 *
 * Supports OpenAI-compatible TTS APIs (OpenAI, ElevenLabs, etc.)
 *
 * POST /api/tts
 *   action: "ping"              → check if TTS is available
 *   action: "generate"          → generate audio from text
 *     text: "text to speak"     → text content (max 1000 chars)
 *     voice: "voice_name"       → optional voice selection
 *     speed: 1.0                → optional speed (0.5 - 2.0)
 */
export async function onRequestPost(context) {
  try {
    const body = await context.request.json();
    const { action, text, voice, speed } = body;

    /* ---- Ping: Check if TTS is configured ---- */
    if (action === 'ping') {
      const ttsKey = context.env.TTS_API_KEY || '';
      const ttsUrl = context.env.TTS_API_URL || '';
      return jsonResponse({
        available: !!(ttsKey && ttsUrl),
        voice: context.env.TTS_VOICE || 'alloy'
      });
    }

    /* ---- Generate: Create audio from text ---- */
    if (action === 'generate') {
      if (!text || text.trim().length === 0) {
        return jsonResponse({ error: 'Text is required' }, 400);
      }

      if (text.length > 1000) {
        return jsonResponse({ error: 'Text too long (max 1000 characters)' }, 400);
      }

      const ttsKey = (context.env.TTS_API_KEY || '').replace(/[\u200b-\u200f\u2028-\u202e\ufeff\u00ad]/g, '').trim();
      const ttsUrl = (context.env.TTS_API_URL || '').replace(/\/+$/, '');

      if (!ttsKey || !ttsUrl) {
        return jsonResponse({
          error: 'TTS not configured. Set TTS_API_KEY and TTS_API_URL in Cloudflare Pages environment variables.',
          hint: 'Go to Cloudflare Dashboard > Pages > Settings > Environment variables'
        }, 503);
      }

      const ttsVoice = voice || context.env.TTS_VOICE || 'alloy';
      const ttsSpeed = Math.max(0.5, Math.min(2.0, parseFloat(speed) || 1.0));

      /* Call the TTS API (OpenAI-compatible format) */
      const response = await fetch(ttsUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + ttsKey
        },
        body: JSON.stringify({
          model: 'tts-1',
          input: text.trim(),
          voice: ttsVoice,
          speed: ttsSpeed,
          response_format: 'mp3'
        })
      });

      if (!response.ok) {
        const errorText = await response.text();
        console.error('TTS API error:', response.status, errorText);
        return jsonResponse({
          error: 'TTS generation failed',
          status: response.status
        }, 502);
      }

      /* Stream the audio back to the client */
      const audioBuffer = await response.arrayBuffer();

      return new Response(audioBuffer, {
        status: 200,
        headers: {
          'Content-Type': 'audio/mpeg',
          'Content-Length': audioBuffer.byteLength.toString(),
          'Cache-Control': 'public, max-age=86400', /* Cache for 24h */
          'Access-Control-Allow-Origin': '*'
        }
      });
    }

    return jsonResponse({ error: 'Unknown action. Use "ping" or "generate".' }, 400);

  } catch (err) {
    console.error('TTS Function error:', err);
    return jsonResponse({ error: 'Server error: ' + (err.message || 'Unknown') }, 500);
  }
}

/* Handle CORS preflight */
export async function onRequestOptions() {
  return new Response(null, {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type'
    }
  });
}

function jsonResponse(data, status) {
  if (status === undefined) status = 200;
  return new Response(JSON.stringify(data), {
    status: status,
    headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' }
  });
}
