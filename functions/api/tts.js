// CloudFlare Pages Function: ElevenLabs TTS API
// POST /api/tts  →  audio/mpeg stream
// Body: { text, voice_id? }
// Uses ElevenLabs Flash v2.5 model for low-latency generation

const DEFAULT_VOICE_ID = 'zGjIP4SZlMnY9m93k97r'; // User-selected ElevenLabs voice
const MAX_TEXT_LENGTH = 5000;
const REQUEST_TIMEOUT = 60000; // 60 seconds

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

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
  // Strip HTML tags
  text = text.replace(/<[^>]*>/g, ' ');
  // Strip markdown images
  text = text.replace(/!\[[^\]]*\]\([^)]*\)/g, '');
  // Strip markdown links but keep text
  text = text.replace(/\[([^\]]*)\]\([^)]*\)/g, '$1');
  // Strip markdown headers (# symbols)
  text = text.replace(/^#{1,6}\s+/gm, '');
  // Strip markdown bold/italic markers
  text = text.replace(/(\*{1,3}|_{1,3})(.*?)\1/g, '$2');
  // Strip markdown horizontal rules
  text = text.replace(/^[-*_]{3,}\s*$/gm, '');
  // Strip code blocks
  text = text.replace(/```[\s\S]*?```/g, '');
  // Strip inline code
  text = text.replace(/`([^`]+)`/g, '$1');
  // Strip blockquote markers
  text = text.replace(/^>\s+/gm, '');
  // Normalize whitespace
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

  if (!rawText || typeof rawText !== 'string') {
    return new Response(JSON.stringify({ error: 'Missing or invalid text field' }), {
      status: 400,
      headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
    });
  }

  // Clean the text
  const text = cleanText(rawText);

  if (!text.trim()) {
    return new Response(JSON.stringify({ error: 'Text is empty after cleaning' }), {
      status: 400,
      headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
    });
  }

  // Enforce max length
  const truncatedText = text.length > MAX_TEXT_LENGTH ? text.substring(0, MAX_TEXT_LENGTH) : text;

  // Get API key from env var or fallback
  const apiKey = env.ELEVENLABS_API_KEY || '20a953b59f011e0537c2c79f4928f3ffb4b6df90fb1b31bda18407037bccb1af';

  if (!apiKey) {
    return new Response(JSON.stringify({ error: 'ElevenLabs API key not configured' }), {
      status: 500,
      headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
    });
  }

  // Validate voice_id (alphanumeric + underscores/hyphens only)
  if (!/^[a-zA-Z0-9_-]+$/.test(voiceId)) {
    return new Response(JSON.stringify({ error: 'Invalid voice_id format' }), {
      status: 400,
      headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
    });
  }

  try {
    const elevenLabsUrl = `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`;

    const requestBody = {
      text: truncatedText,
      model_id: 'eleven_flash_v2_5',
      voice_settings: {
        stability: 0.5,
        similarity_boost: 0.75,
      },
    };

    // Use AbortController for timeout
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), REQUEST_TIMEOUT);

    const response = await fetch(elevenLabsUrl, {
      method: 'POST',
      headers: {
        'xi-api-key': apiKey,
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg',
      },
      body: JSON.stringify(requestBody),
      signal: controller.signal,
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      let errorDetail = `ElevenLabs API returned ${response.status}`;
      try {
        const errorBody = await response.json();
        errorDetail = errorBody.detail?.message || errorBody.detail || errorBody.message || errorDetail;
      } catch {
        // Response wasn't JSON, use status text
        errorDetail = response.statusText || errorDetail;
      }

      console.error('ElevenLabs TTS error:', response.status, errorDetail);

      // Map common errors to user-friendly messages
      if (response.status === 401) {
        errorDetail = 'TTS service authentication failed';
      } else if (response.status === 402 || response.status === 422) {
        errorDetail = 'TTS voice not available on current plan';
      } else if (response.status === 429) {
        errorDetail = 'TTS service rate limit reached, please try again later';
      }

      return new Response(JSON.stringify({ error: errorDetail }), {
        status: response.status >= 500 ? 502 : response.status, // Proxy 5xx as 502
        headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
      });
    }

    // Stream the audio back
    const audioBuffer = await response.arrayBuffer();

    return new Response(audioBuffer, {
      status: 200,
      headers: {
        ...CORS_HEADERS,
        'Content-Type': 'audio/mpeg',
        'Content-Length': audioBuffer.byteLength.toString(),
        'Cache-Control': 'public, max-age=86400', // Cache for 24h — same text = same audio
      },
    });
  } catch (err) {
    if (err.name === 'AbortError') {
      console.error('ElevenLabs TTS request timed out');
      return new Response(JSON.stringify({ error: 'TTS generation timed out. Try shorter text.' }), {
        status: 504,
        headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
      });
    }

    console.error('ElevenLabs TTS error:', err.message || err);
    return new Response(JSON.stringify({ error: 'TTS generation failed', detail: err.message || String(err) }), {
      status: 500,
      headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
    });
  }
}
