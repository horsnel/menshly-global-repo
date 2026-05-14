// CloudFlare Pages Function: Speechify TTS API
// POST /api/tts  →  audio/mpeg stream
// Body: { text, voice_id?, speed? }
// Uses Speechify AI for high-quality voice generation

const DEFAULT_VOICE_ID = 'david'; // Clear professional narrator
const MAX_TEXT_LENGTH = 5000;
const REQUEST_TIMEOUT = 60000; // 60 seconds

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

// Valid Speechify voice IDs
const VALID_VOICES = ['david', 'mrbeast', 'snoop', 'gwyneth', 'emma', 'kimberly'];

// Rate limiting: simple in-memory counter (resets on deploy)
const rateLimiter = new Map();
const RATE_LIMIT_WINDOW = 60000; // 1 minute
const RATE_LIMIT_MAX = 10; // 10 TTS requests per minute per IP

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

// Clean text for TTS: strip HTML, markdown artifacts, and normalize whitespace
function cleanText(raw) {
  if (!raw || typeof raw !== 'string') return '';
  let text = raw;
  text = text.replace(/<[^>]*>/g, ' ');
  text = text.replace(/!\[[^\]]*\]\([^)]*\)/g, '');
  text = text.replace(/\[([^\]]*)\]\([^)]*\)/g, '$1');
  text = text.replace(/^#{1,6}\s+/gm, '');
  text = text.replace(/(\*{1,3}|_{1,3})(.*?)\1/g, '$2');
  text = text.replace(/^[-*_]{3,}\s*$/gm, '');
  text = text.replace(/```[\s\S]*?```/g, '');
  text = text.replace(/`([^`]+)`/g, '$1');
  text = text.replace(/^>\s+/gm, '');
  text = text.replace(/\s+/g, ' ').trim();
  return text;
}

export async function onRequestOptions() {
  return new Response(null, { status: 204, headers: CORS_HEADERS });
}

export async function onRequestPost(context) {
  const { request, env } = context;

  // Rate limit check
  const ip = request.headers.get('CF-Connecting-IP') || 'unknown';
  if (isRateLimited(ip)) {
    return new Response(JSON.stringify({ error: 'Rate limited. Please wait before requesting more audio.' }), {
      status: 429,
      headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
    });
  }

  // Parse request body
  let body;
  try {
    body = await request.json();
  } catch {
    return new Response(JSON.stringify({ error: 'Invalid JSON body' }), {
      status: 400,
      headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
    });
  }

  const rawText = body.text;
  const voiceId = body.voice_id || DEFAULT_VOICE_ID;
  const speed = body.speed || 1.0;

  if (!rawText || typeof rawText !== 'string') {
    return new Response(JSON.stringify({ error: 'Missing or invalid text field' }), {
      status: 400,
      headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
    });
  }

  // Validate voice ID
  if (!VALID_VOICES.includes(voiceId)) {
    return new Response(JSON.stringify({ error: `Invalid voice_id. Valid options: ${VALID_VOICES.join(', ')}` }), {
      status: 400,
      headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
    });
  }

  const text = cleanText(rawText);

  if (!text.trim()) {
    return new Response(JSON.stringify({ error: 'Text is empty after cleaning' }), {
      status: 400,
      headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
    });
  }

  const truncatedText = text.length > MAX_TEXT_LENGTH ? text.substring(0, MAX_TEXT_LENGTH) : text;

  // Speechify API key: try CloudFlare env first, then fallback
  const apiKey = env.SPEECHIFY_API_KEY || 'ZYnqwIOZbL2FwA0XWaLXqzVmz7nYDW5J6IlPG9SEwWg=';

  if (!apiKey) {
    return new Response(JSON.stringify({ error: 'Speechify API key not configured' }), {
      status: 500,
      headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
    });
  }

  try {
    const speechifyUrl = 'https://api.speechify.ai/v1/audio/speech';

    const requestBody = {
      input: truncatedText,
      voice_id: voiceId,
      audio_format: 'mp3',
      speed: Math.max(0.5, Math.min(2.0, Number(speed) || 1.0)),
    };

    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), REQUEST_TIMEOUT);

    const response = await fetch(speechifyUrl, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestBody),
      signal: controller.signal,
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      let errorDetail = `Speechify API returned ${response.status}`;
      try {
        const errorBody = await response.json();
        errorDetail = errorBody.error || errorBody.message || errorDetail;
      } catch {
        errorDetail = response.statusText || errorDetail;
      }

      console.error('Speechify TTS error:', response.status, errorDetail);

      if (response.status === 401) {
        errorDetail = 'TTS service authentication failed';
      } else if (response.status === 402) {
        errorDetail = 'TTS service quota exceeded';
      } else if (response.status === 429) {
        errorDetail = 'TTS service rate limit reached, please try again later';
      }

      return new Response(JSON.stringify({ error: errorDetail }), {
        status: response.status >= 500 ? 502 : response.status,
        headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
      });
    }

    // Speechify returns JSON with base64-encoded audio_data
    const result = await response.json();
    const audioDataBase64 = result.audio_data;

    if (!audioDataBase64) {
      console.error('Speechify TTS: no audio_data in response');
      return new Response(JSON.stringify({ error: 'TTS generation returned no audio' }), {
        status: 502,
        headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
      });
    }

    // Decode base64 to binary
    const audioBuffer = Uint8Array.from(atob(audioDataBase64), c => c.charCodeAt(0));

    return new Response(audioBuffer, {
      status: 200,
      headers: {
        ...CORS_HEADERS,
        'Content-Type': 'audio/mpeg',
        'Content-Length': audioBuffer.byteLength.toString(),
        'Cache-Control': 'public, max-age=86400',
      },
    });
  } catch (err) {
    if (err.name === 'AbortError') {
      console.error('Speechify TTS request timed out');
      return new Response(JSON.stringify({ error: 'TTS generation timed out. Try shorter text.' }), {
        status: 504,
        headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
      });
    }

    console.error('Speechify TTS error:', err.message || err);
    return new Response(JSON.stringify({ error: 'TTS generation failed', detail: err.message || String(err) }), {
      status: 500,
      headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
    });
  }
}
