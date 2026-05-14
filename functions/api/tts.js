// CloudFlare Pages Function: TTS API with multiple providers
// POST /api/tts  →  audio/mpeg stream
// Body: { text, voice_id?, speed? }
// Strategy: Speechify → ElevenLabs → returns error (client uses browser TTS fallback)

const SPEECHIFY_DEFAULT_VOICE = 'david';
const ELEVENLABS_DEFAULT_VOICE = 'JBFqnCBsd6RMkjVDRZzb';
const ELEVENLABS_MODEL = 'eleven_flash_v2_5';
const MAX_TEXT_LENGTH = 5000;
const REQUEST_TIMEOUT = 60000;

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

const SPEECHIFY_VOICES = ['david', 'mrbeast', 'snoop', 'gwyneth', 'emma', 'kimberly'];

// Rate limiting
const rateLimiter = new Map();
const RATE_LIMIT_WINDOW = 60000;
const RATE_LIMIT_MAX = 10;

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
  text = text.replace(/[\u2018\u2019]/g, "'");
  text = text.replace(/[\u201C\u201D]/g, '"');
  text = text.replace(/\u2011/g, '-');
  text = text.replace(/\u2013/g, '-');
  text = text.replace(/\u2014/g, '--');
  text = text.replace(/\s+/g, ' ').trim();
  return text;
}

export async function onRequestOptions() {
  return new Response(null, { status: 204, headers: CORS_HEADERS });
}

async function trySpeechify(text, voiceId, speed, apiKey) {
  try {
    const url = 'https://api.speechify.ai/v1/audio/speech';
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), REQUEST_TIMEOUT);

    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        input: text,
        voice_id: voiceId,
        audio_format: 'mp3',
        speed: Math.max(0.5, Math.min(2.0, Number(speed) || 1.0)),
      }),
      signal: controller.signal,
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      return { ok: false, status: response.status };
    }

    const result = await response.json();
    if (!result.audio_data) {
      return { ok: false, status: 502 };
    }

    const audioBuffer = Uint8Array.from(atob(result.audio_data), c => c.charCodeAt(0));
    return { ok: true, buffer: audioBuffer, provider: 'speechify' };
  } catch (err) {
    return { ok: false, status: 500, error: err.message };
  }
}

async function tryElevenLabs(text, voiceId, apiKey) {
  try {
    const url = `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`;
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), REQUEST_TIMEOUT);

    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'xi-api-key': apiKey,
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg',
      },
      body: JSON.stringify({
        text: text,
        model_id: ELEVENLABS_MODEL,
        voice_settings: { stability: 0.5, similarity_boost: 0.75 },
      }),
      signal: controller.signal,
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      return { ok: false, status: response.status };
    }

    const audioBuffer = await response.arrayBuffer();
    return { ok: true, buffer: new Uint8Array(audioBuffer), provider: 'elevenlabs' };
  } catch (err) {
    return { ok: false, status: 500, error: err.message };
  }
}

export async function onRequestPost(context) {
  const { request, env } = context;

  const ip = request.headers.get('CF-Connecting-IP') || 'unknown';
  if (isRateLimited(ip)) {
    return new Response(JSON.stringify({ error: 'Rate limited. Please wait before requesting more audio.' }), {
      status: 429,
      headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
    });
  }

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
  const requestedVoice = body.voice_id || SPEECHIFY_DEFAULT_VOICE;
  const speed = body.speed || 1.0;

  if (!rawText || typeof rawText !== 'string') {
    return new Response(JSON.stringify({ error: 'Missing or invalid text field' }), {
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

  const speechifyKey = env.SPEECHIFY_API_KEY || 'ZYnqwIOZbL2FwA0XWaLXqzVmz7nYDW5J6IlPG9SEwWg=';
  const elevenLabsKey = env.ELEVENLABS_API_KEY || '20a953b59f011e0537c2c79f4928f3ffb4b6df90fb1b31bda18407037bccb1af';

  // Try Speechify first
  if (speechifyKey) {
    const speechifyVoice = SPEECHIFY_VOICES.includes(requestedVoice) ? requestedVoice : SPEECHIFY_DEFAULT_VOICE;
    const result = await trySpeechify(truncatedText, speechifyVoice, speed, speechifyKey);
    if (result.ok) {
      return new Response(result.buffer, {
        status: 200,
        headers: {
          ...CORS_HEADERS,
          'Content-Type': 'audio/mpeg',
          'Content-Length': result.buffer.byteLength.toString(),
          'Cache-Control': 'public, max-age=86400',
          'X-TTS-Provider': result.provider,
        },
      });
    }
    console.log('Speechify failed:', result.status);
  }

  // Fallback to ElevenLabs
  if (elevenLabsKey) {
    const result = await tryElevenLabs(truncatedText, ELEVENLABS_DEFAULT_VOICE, elevenLabsKey);
    if (result.ok) {
      return new Response(result.buffer, {
        status: 200,
        headers: {
          ...CORS_HEADERS,
          'Content-Type': 'audio/mpeg',
          'Content-Length': result.buffer.byteLength.toString(),
          'Cache-Control': 'public, max-age=86400',
          'X-TTS-Provider': result.provider,
        },
      });
    }
    console.log('ElevenLabs failed:', result.status);
  }

  // Both providers failed — return error so client uses browser TTS fallback
  return new Response(JSON.stringify({ error: 'Cloud TTS unavailable. Using browser speech.' }), {
    status: 503,
    headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
  });
}
