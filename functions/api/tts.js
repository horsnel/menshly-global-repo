/**
 * Cloudflare Pages Function: Professional TTS API v2.0
 * Generates natural-sounding audio from text using AI neural voices.
 *
 * Engine priority:
 *   1. OpenAI-compatible API (if TTS_API_KEY + TTS_API_URL env vars set) — premium
 *   2. Microsoft Edge TTS (free neural voices, no API key needed) — default
 *
 * Edge TTS voices are the same high-quality neural voices used by
 * Microsoft Edge's "Read Aloud" feature — professional, natural, free.
 *
 * Configure via Cloudflare Pages Environment Variables (optional):
 *   TTS_API_KEY  - API key for premium TTS service
 *   TTS_API_URL  - TTS API endpoint (e.g., https://api.openai.com/v1/audio/speech)
 *   TTS_VOICE    - Default voice name (default: en-US-AriaNeural)
 *
 * POST /api/tts
 *   action: "ping"              -> check if TTS is available
 *   action: "voices"            -> list available Edge TTS voices
 *   action: "generate"          -> generate audio from text
 *     text: "text to speak"     -> text content (max 1000 chars)
 *     voice: "voice_name"       -> optional voice selection
 *     speed: 1.0                -> optional speed (0.5 - 2.0)
 */

/* ---- Edge TTS Configuration ---- */
const EDGE_TTS_TOKEN = '6A5AA1D4EAFF4E9FB37E23D68491D6F4';
const EDGE_TTS_WSS = 'wss://speech.platform.bing.com/consumer/speech/synthesize/readaloud/edge/v1';
const DEFAULT_VOICE = 'en-US-AriaNeural';
const OUTPUT_FORMAT = 'audio-24khz-48kbitrate-mono-mp3';

/* Available Edge Neural voices */
const VOICE_LIST = {
  'en-US-AriaNeural':     'Aria (Female, US) — Default',
  'en-US-JennyNeural':    'Jenny (Female, US)',
  'en-US-MichelleNeural': 'Michelle (Female, US)',
  'en-US-JaneNeural':     'Jane (Female, US)',
  'en-US-DavisNeural':    'Davis (Male, US)',
  'en-US-JasonNeural':    'Jason (Male, US)',
  'en-US-TonyNeural':     'Tony (Male, US)',
  'en-US-GuyNeural':      'Guy (Male, US)',
  'en-US-ChristopherNeural': 'Christopher (Male, US)',
  'en-US-EricNeural':     'Eric (Male, US)',
  'en-GB-SoniaNeural':    'Sonia (Female, UK)',
  'en-GB-RyanNeural':     'Ryan (Male, UK)',
  'en-GB-LibbyNeural':    'Libby (Female, UK)',
  'en-AU-NatashaNeural':  'Natasha (Female, AU)',
  'en-AU-WilliamNeural':  'William (Male, AU)',
  'en-CA-ClaraNeural':    'Clara (Female, CA)',
  'en-IN-NeerjaNeural':   'Neerja (Female, India)',
};

/* ---- Utility Functions ---- */
function uuid() {
  return 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'.replace(/x/g, () =>
    Math.floor(Math.random() * 16).toString(16)
  );
}

function escapeXml(s) {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;');
}

function ratePercent(speed) {
  if (speed === 1) return '+0%';
  const pct = Math.round((speed - 1) * 100);
  return (pct >= 0 ? '+' : '') + pct + '%';
}

function jsonResponse(data, status) {
  if (status === undefined) status = 200;
  return new Response(JSON.stringify(data), {
    status: status,
    headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' }
  });
}

/* ================================================================
   Edge TTS via WebSocket — Free Neural Voices
   Uses the same API as Microsoft Edge's "Read Aloud" feature.
   ================================================================ */
async function synthesizeEdgeTTS(text, voice, speed) {
  const reqId = uuid();
  const connId = uuid();
  const wsUrl = EDGE_TTS_WSS + '?TrustedClientToken=' + EDGE_TTS_TOKEN + '&ConnectionId=' + connId;

  /* Connect via WebSocket (Cloudflare Workers supports fetch with upgrade) */
  const resp = await fetch(wsUrl, {
    headers: { Upgrade: 'websocket' }
  });

  const ws = resp.webSocket;
  if (!ws) {
    throw new Error('WebSocket upgrade failed');
  }

  ws.accept();

  return new Promise((resolve, reject) => {
    const audioParts = [];
    let resolved = false;

    const timeout = setTimeout(() => {
      if (!resolved) {
        resolved = true;
        try { ws.close(1000); } catch(e) {}
        if (audioParts.length > 0) {
          resolve(combineAudio(audioParts));
        } else {
          reject(new Error('Edge TTS timed out after 20s'));
        }
      }
    }, 20000);

    /* Send configuration message */
    const timestamp = new Date().toISOString();
    ws.send(
      'X-Timestamp:' + timestamp + '\r\n' +
      'Content-Type:application/json; charset=utf-8\r\n' +
      'Path:speech.config\r\n\r\n' +
      JSON.stringify({
        context: {
          synthesis: {
            audio: {
              metadataoptions: {
                sentenceBoundaryEnabled: 'false',
                wordBoundaryEnabled: 'true'
              },
              outputFormat: OUTPUT_FORMAT
            }
          }
        }
      })
    );

    /* Send SSML message */
    const ssml =
      "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'>" +
      "<voice name='" + voice + "'>" +
      "<prosody rate='" + ratePercent(speed) + "'>" +
      escapeXml(text) +
      "</prosody>" +
      "</voice>" +
      "</speak>";

    ws.send(
      'X-RequestId:' + reqId + '\r\n' +
      'Content-Type:application/ssml+xml\r\n' +
      'X-Timestamp:' + timestamp + 'Z\r\n' +
      'Path:ssml\r\n\r\n' +
      ssml
    );

    /* Handle incoming messages */
    ws.addEventListener('message', (event) => {
      const data = event.data;

      if (typeof data === 'string') {
        /* Text message — could contain audio data (base64) or control signals */
        if (data.indexOf('Path:turn.end') !== -1) {
          /* Synthesis complete */
          if (!resolved) {
            resolved = true;
            clearTimeout(timeout);
            try { ws.close(1000); } catch(e) {}
            if (audioParts.length > 0) {
              resolve(combineAudio(audioParts));
            } else {
              reject(new Error('Edge TTS returned no audio data'));
            }
          }
        } else if (data.indexOf('Path:audio') !== -1) {
          /* Audio chunk — extract base64 payload after double CRLF */
          const headerEnd = data.indexOf('\r\n\r\n');
          if (headerEnd !== -1) {
            const payload = data.substring(headerEnd + 4).trim();
            if (payload.length > 0) {
              try {
                const binaryStr = atob(payload);
                const bytes = new Uint8Array(binaryStr.length);
                for (let i = 0; i < binaryStr.length; i++) {
                  bytes[i] = binaryStr.charCodeAt(i);
                }
                audioParts.push(bytes);
              } catch (e) {
                /* Ignore base64 decode errors — might be partial data */
              }
            }
          }
        }
      } else if (data instanceof ArrayBuffer) {
        /* Binary message — raw audio data */
        audioParts.push(new Uint8Array(data));
      }
    });

    ws.addEventListener('error', () => {
      if (!resolved) {
        resolved = true;
        clearTimeout(timeout);
        reject(new Error('Edge TTS WebSocket connection error'));
      }
    });

    ws.addEventListener('close', (event) => {
      if (!resolved) {
        resolved = true;
        clearTimeout(timeout);
        if (audioParts.length > 0) {
          resolve(combineAudio(audioParts));
        } else {
          reject(new Error('Edge TTS WebSocket closed without audio (code: ' + event.code + ')'));
        }
      }
    });
  });
}

function combineAudio(parts) {
  const totalLen = parts.reduce((sum, p) => sum + p.length, 0);
  const result = new Uint8Array(totalLen);
  let offset = 0;
  for (const part of parts) {
    result.set(part, offset);
    offset += part.length;
  }
  return result.buffer;
}

/* ================================================================
   OpenAI-Compatible TTS — Premium Fallback
   Used when TTS_API_KEY + TTS_API_URL are configured.
   ================================================================ */
async function synthesizeOpenAI(text, voice, speed, apiKey, apiUrl) {
  const response = await fetch(apiUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + apiKey
    },
    body: JSON.stringify({
      model: 'tts-1',
      input: text.trim(),
      voice: voice,
      speed: speed,
      response_format: 'mp3'
    })
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error('OpenAI TTS API error ' + response.status + ': ' + errorText);
  }

  return await response.arrayBuffer();
}

/* ================================================================
   Main Handler
   ================================================================ */
export async function onRequestPost(context) {
  try {
    const body = await context.request.json();
    const { action, text, voice, speed } = body;

    /* ---- Ping: Check if TTS is available ---- */
    if (action === 'ping') {
      const hasOpenAI = !!(context.env.TTS_API_KEY && context.env.TTS_API_URL);
      return jsonResponse({
        available: true,  /* Always available — Edge TTS is free */
        engine: hasOpenAI ? 'openai' : 'edge-tts',
        defaultVoice: context.env.TTS_VOICE || DEFAULT_VOICE,
        openai: hasOpenAI
      });
    }

    /* ---- Voices: List available Edge TTS voices ---- */
    if (action === 'voices') {
      return jsonResponse({
        voices: VOICE_LIST,
        default: DEFAULT_VOICE
      });
    }

    /* ---- Generate: Create audio from text ---- */
    if (action === 'generate') {
      if (!text || text.trim().length === 0) {
        return jsonResponse({ error: 'Text is required' }, 400);
      }

      if (text.length > 1000) {
        return jsonResponse({ error: 'Text too long (max 1000 characters per chunk)' }, 400);
      }

      const ttsSpeed = Math.max(0.5, Math.min(2.0, parseFloat(speed) || 1.0));
      const ttsVoice = voice || context.env.TTS_VOICE || DEFAULT_VOICE;

      /* Validate voice name for Edge TTS */
      const validEdgeVoice = VOICE_LIST[ttsVoice] ? ttsVoice : DEFAULT_VOICE;

      let audioBuffer;

      /* Try OpenAI-compatible API first (if configured) */
      const apiKey = (context.env.TTS_API_KEY || '').replace(/[\u200b-\u200f\u2028-\u202e\ufeff\u00ad]/g, '').trim();
      const apiUrl = (context.env.TTS_API_URL || '').replace(/\/+$/, '');

      if (apiKey && apiUrl) {
        try {
          audioBuffer = await synthesizeOpenAI(text.trim(), ttsVoice, ttsSpeed, apiKey, apiUrl);
        } catch (e) {
          console.warn('OpenAI TTS failed, falling back to Edge TTS:', e.message);
          /* Fall through to Edge TTS */
        }
      }

      /* Use Edge TTS (free, no API key needed) */
      if (!audioBuffer) {
        try {
          audioBuffer = await synthesizeEdgeTTS(text.trim(), validEdgeVoice, ttsSpeed);
        } catch (e) {
          console.error('Edge TTS failed:', e.message);
          return jsonResponse({
            error: 'TTS generation failed: ' + e.message,
            fallback: 'browser'
          }, 502);
        }
      }

      /* Stream audio back to client */
      return new Response(audioBuffer, {
        status: 200,
        headers: {
          'Content-Type': 'audio/mpeg',
          'Content-Length': audioBuffer.byteLength.toString(),
          'Cache-Control': 'public, max-age=86400',
          'Access-Control-Allow-Origin': '*',
          'X-TTS-Engine': apiKey && apiUrl ? 'openai' : 'edge-tts',
          'X-TTS-Voice': validEdgeVoice
        }
      });
    }

    return jsonResponse({ error: 'Unknown action. Use "ping", "voices", or "generate".' }, 400);

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
