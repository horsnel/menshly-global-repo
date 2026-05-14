// CloudFlare Pages Function: Dual TTS API (Speechify → ElevenLabs fallback)
// POST /api/tts  →  audio/mpeg stream
// Body: { text, voice_id?, speed? }
// Strategy: Try Speechify first; on 402/quota error, fall back to ElevenLabs

const SPEECHIFY_DEFAULT_VOICE = 'david';
const ELEVENLABS_DEFAULT_VOICE = 'JBFqnCBsd6RMkjVDRZzb'; // George — warm British storyteller
const ELEVENLABS_MODEL = 'eleven_flash_v2_5';
const MAX_TEXT_LENGTH = 5000;
const REQUEST_TIMEOUT = 60000; // 60 seconds

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

// Valid Speechify voice IDs
const SPEECHIFY_VOICES = ['david', 'mrbeast', 'snoop', 'gwyneth', 'emma', 'kimberly'];

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
  // Replace smart quotes and non-breaking hyphens with ASCII equivalents
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

// ---- Speechify TTS ----
async function speechifyTTS(text, voiceId, speed, apiKey) {
  const url = 'https://api.speechify.ai/v1/audio/speech';
  const body = {
    input: text,
    voice_id: voiceId,
    audio_format: 'mp3',
    speed: Math.max(0.5, Math.min(2.0, Number(speed) || 1.0)),
  };

  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), REQUEST_TIMEOUT);

  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(body),
    signal: controller.signal,
  });

  clearTimeout(timeoutId);

  if (!response.ok) {
    const errorText = await response.text();
    let errorDetail = `Speechify API returned ${response.status}`;
    try { errorDetail = JSON.parse(errorText).error || errorDetail; } catch {}
    const retriable = response.status === 402 || response.status === 429;
    return { ok: false, status: response.status, error: errorDetail, retriable };
  }

  const result = await response.json();
  const audioDataBase64 = result.audio_data;
  if (!audioDataBase64) {
    return { ok: false, status: 502, error: 'No audio_data in Speechify response', retriable: true };
  }

  const audioBuffer = Uint8Array.from(atob(audioDataBase64), c => c.charCodeAt(0));
  return { ok: true, buffer: audioBuffer };
}

// ---- ElevenLabs TTS (fallback) ----
async function elevenLabsTTS(text, voiceId, apiKey) {
  const url = `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`;
  const body = {
    text: text,
    model_id: ELEVENLABS_MODEL,
    voice_settings: { stability: 0.5, similarity_boost: 0.75 },
  };

  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), REQUEST_TIMEOUT);

  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'xi-api-key': apiKey,
      'Content-Type': 'application/json',
      'Accept': 'audio/mpeg',
    },
    body: JSON.stringify(body),
    signal: controller.signal,
  });

  clearTimeout(timeoutId);

  if (!response.ok) {
    let errorDetail = `ElevenLabs API returned ${response.status}`;
    try { const err = await response.json(); errorDetail = err.detail?.message || err.detail || errorDetail; } catch {}
    return { ok: false, status: response.status, error: errorDetail };
  }

  const audioBuffer = await response.arrayBuffer();
  return { ok: true, buffer: new Uint8Array(audioBuffer) };
}

// ---- Main handler ----
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

  // API keys
  const speechifyKey = env.SPEECHIFY_API_KEY || 'ZYnqwIOZbL2FwA0XWaLXqzVmz7nYDW5J6IlPG9SEwWg=';
  const elevenLabsKey = env.ELEVENLABS_API_KEY || '20a953b59f011e0537c2c79f4928f3ffb4b6df90fb1b31bda18407037bccb1af';

  // --- Try Speechify first ---
  if (speechifyKey) {
    const speechifyVoice = SPEECHIFY_VOICES.includes(requestedVoice) ? requestedVoice : SPEECHIFY_DEFAULT_VOICE;
    try {
      const result = await speechifyTTS(truncatedText, speechifyVoice, speed, speechifyKey);
      if (result.ok) {
        return new Response(result.buffer, {
          status: 200,
          headers: {
            ...CORS_HEADERS,
            'Content-Type': 'audio/mpeg',
            'Content-Length': result.buffer.byteLength.toString(),
            'Cache-Control': 'public, max-age=86400',
            'X-TTS-Provider': 'speechify',
          },
        });
      }
      // If Speechify failed with retriable error (402/quota), fall back
      if (result.retriable) {
        console.log('Speechify failed (' + result.status + '), falling back to ElevenLabs');
      } else {
        // Non-retriable error — return the error
        return new Response(JSON.stringify({ error: result.error }), {
          status: result.status >= 500 ? 502 : result.status,
          headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
        });
      }
    } catch (err) {
      console.error('Speechify TTS error:', err.message || err);
      // Fall through to ElevenLabs
    }
  }

  // --- Fallback: ElevenLabs ---
  if (elevenLabsKey) {
    try {
      // Map Speechify voice names to ElevenLabs voice IDs
      const voiceMap = {
        'david': 'JBFqnCBsd6RMkjVDRZzb',
        'emma': 'JBFqnCBsd6RMkjVDRZzb',
        'gwyneth': 'JBFqnCBsd6RMkjVDRZzb',
        'kimberly': 'JBFqnCBsd6RMkjVDRZzb',
        'mrbeast': 'JBFqnCBsd6RMkjVDRZzb',
        'snoop': 'JBFqnCBsd6RMkjVDRZzb',
      };
      const elevenVoiceId = voiceMap[requestedVoice] || ELEVENLABS_DEFAULT_VOICE;
      const result = await elevenLabsTTS(truncatedText, elevenVoiceId, elevenLabsKey);

      if (result.ok) {
        return new Response(result.buffer, {
          status: 200,
          headers: {
            ...CORS_HEADERS,
            'Content-Type': 'audio/mpeg',
            'Content-Length': result.buffer.byteLength.toString(),
            'Cache-Control': 'public, max-age=86400',
            'X-TTS-Provider': 'elevenlabs',
          },
        });
      }

      return new Response(JSON.stringify({ error: result.error }), {
        status: result.status >= 500 ? 502 : result.status,
        headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
      });
    } catch (err) {
      if (err.name === 'AbortError') {
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

  return new Response(JSON.stringify({ error: 'No TTS API key configured' }), {
    status: 500,
    headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
  });
}
