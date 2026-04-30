#!/usr/bin/env python3
"""Shared AI API utility for Menshly Global article generators.

Smart routing with three backends (in priority order):
1. Groq via Cloudflare proxy — fastest, uses gsk_ key through edge proxy
   to bypass geo-restrictions on api.groq.com
2. Node.js bridge (z-ai-web-dev-sdk) — reliable, works from any server
3. Pollinations AI — free, no key needed, always-available fallback

The Cloudflare proxy routes requests through Cloudflare's edge network,
bypassing the 403 geo-block that Groq enforces from certain regions (HK, etc).
When AI_API_KEY starts with "gsk_", the proxy is used automatically.

Environment variables:
  AI_API_KEY   — Groq key (gsk_...), Gemini key (AIza...), or "bridge"
  AI_API_BASE  — Override API base URL (default: auto-detected from key)
  AI_MODEL     — Model name (default: llama-3.3-70b-versatile for Groq)
  GROQ_PROXY_URL — Cloudflare Pages proxy URL (default: auto-detected)
  GEMINI_API_KEY — Google Gemini API key (optional secondary fallback)
"""

import os
import json
import subprocess
import tempfile
import requests
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BRIDGE_SCRIPT = PROJECT_ROOT / "scripts" / "ai-bridge.js"

# ── Cloudflare Groq Proxy ──
# Routes through Cloudflare's edge network to bypass geo-blocks on api.groq.com
GROQ_DIRECT_BASE = "https://api.groq.com/openai/v1"
GROQ_PROXY_URL = os.environ.get(
    "GROQ_PROXY_URL",
    "https://menshly-global-enz.pages.dev/api/groq-proxy"
)
GROQ_DEFAULT_MODEL = "llama-3.3-70b-versatile"

# ── Pollinations API — free, no key ──
POLLINATIONS_OPENAI_BASE = "https://text.pollinations.ai/openai"
POLLINATIONS_MODEL = "openai"  # Only working model on Pollinations (gpt-oss-20b)

# ── Gemini API — Google's LLM ──
GEMINI_API_BASE = "https://generativelanguage.googleapis.com/v1beta/openai"
GEMINI_MODEL = "gemini-2.0-flash"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

# ── Cache for proxy availability ──
_proxy_tested = False
_proxy_available = False


def _get_api_key():
    """Get the configured API key."""
    return os.environ.get("AI_API_KEY", "")


def _get_api_base():
    """Get the configured API base URL."""
    return os.environ.get("AI_API_BASE", "")


def _get_model():
    """Get the configured model name."""
    return os.environ.get("AI_MODEL", GROQ_DEFAULT_MODEL)


def _is_groq_key(key=None):
    """Check if the API key is a Groq key (starts with gsk_)."""
    k = key or _get_api_key()
    return bool(k and k.startswith("gsk_"))


def _is_gemini_key(key=None):
    """Check if the API key is a Gemini key (starts with AIza)."""
    k = key or _get_api_key()
    return bool(k and k.startswith("AIza"))


def _is_bridge_mode():
    """Check if bridge mode is explicitly requested."""
    key = _get_api_key()
    base = _get_api_base()
    if "bridge" in key.lower() or "local-proxy" in key.lower():
        return True
    if "localhost" in base or "127.0.0.1" in base:
        return True
    return False


def _test_groq_proxy():
    """Test if the Cloudflare Groq proxy is reachable and working.

    Returns True if the proxy responds (even with 401, which means
    it's forwarding to Groq correctly).
    """
    global _proxy_tested, _proxy_available
    if _proxy_tested:
        return _proxy_available

    try:
        resp = requests.post(
            GROQ_PROXY_URL,
            headers={
                "Authorization": "Bearer test-key",
                "Content-Type": "application/json",
            },
            json={
                "model": GROQ_DEFAULT_MODEL,
                "messages": [{"role": "user", "content": "test"}],
                "max_tokens": 1,
            },
            timeout=10,
        )
        # 401 = proxy works but test key is invalid (expected)
        # 200 = proxy works and somehow test passed
        # 403 = proxy itself is blocked (shouldn't happen from Cloudflare)
        # Anything other than connection error means proxy is reachable
        _proxy_available = resp.status_code != 403
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        _proxy_available = False

    _proxy_tested = True
    if _proxy_available:
        print("  [proxy] Cloudflare Groq proxy is reachable")
    else:
        print("  [proxy] Cloudflare Groq proxy is NOT reachable")
    return _proxy_available


def api_call(payload, max_retries=5, api_key=None, api_base=None):
    """Call the AI API with smart routing and automatic fallback.

    Strategy (in priority order):
    1. Groq key (gsk_) → Cloudflare proxy → direct fallback → bridge → Pollinations
    2. Bridge mode → Node.js bridge → Pollinations
    3. Gemini key → direct call → bridge → Pollinations
    4. No key → bridge → Pollinations
    """
    key = api_key or _get_api_key()
    base = api_base or _get_api_base()

    # ── Strategy 1: Groq key via proxy ──
    if _is_groq_key(key):
        return _groq_strategy(payload, max_retries, key)

    # ── Strategy 2: Explicit bridge mode ──
    if _is_bridge_mode():
        return _bridge_strategy(payload, max_retries)

    # ── Strategy 3: Gemini key ──
    if _is_gemini_key(key):
        return _gemini_strategy(payload, max_retries, key, base)

    # ── Strategy 4: Generic key with base URL ──
    if key and base:
        return _generic_strategy(payload, max_retries, key, base)

    # ── Strategy 5: No key — try bridge then Pollinations ──
    return _no_key_strategy(payload, max_retries)


# ──────────────────────────────────────────────
# Strategy implementations
# ──────────────────────────────────────────────

def _groq_strategy(payload, max_retries, api_key):
    """Groq key: try proxy → direct → bridge → Pollinations."""
    # Step 1: Try Cloudflare proxy first (bypasses geo-blocks)
    try:
        print("  [groq] Trying Cloudflare proxy...")
        return _proxy_call(payload, max_retries, api_key)
    except Exception as e:
        print(f"  [groq] Proxy failed: {str(e)[:150]}")

    # Step 2: Try direct Groq API (works from supported regions)
    try:
        print("  [groq] Trying direct API...")
        return _direct_call(payload, max_retries=2, api_key=api_key, api_base=GROQ_DIRECT_BASE)
    except Exception as e:
        print(f"  [groq] Direct API failed: {str(e)[:150]}")

    # Step 3: Fall back to Node.js bridge
    try:
        print("  [groq] Falling back to Node.js bridge...")
        return _bridge_call(payload, max_retries=2)
    except Exception as e:
        print(f"  [groq] Bridge failed: {str(e)[:150]}")

    # Step 4: Last resort — Pollinations
    print("  [groq] All Groq routes failed, using Pollinations (free)...")
    return _pollinations_call(payload, max_retries)


def _bridge_strategy(payload, max_retries):
    """Bridge mode: try bridge → Pollinations."""
    try:
        print("  [bridge] Using Node.js bridge (z-ai-web-dev-sdk)...")
        return _bridge_call(payload, max_retries)
    except Exception as e:
        print(f"  [bridge] Failed: {str(e)[:150]}")
        print("  [bridge] Falling back to Pollinations (free)...")
        return _pollinations_call(payload, max_retries)


def _gemini_strategy(payload, max_retries, api_key, api_base):
    """Gemini key: try direct → bridge → Pollinations."""
    try:
        print("  [gemini] Trying direct Gemini API...")
        return _direct_call(payload, max_retries, api_key=api_key, api_base=api_base or GEMINI_API_BASE)
    except Exception as e:
        print(f"  [gemini] Direct failed: {str(e)[:150]}")

    try:
        print("  [gemini] Falling back to Node.js bridge...")
        return _bridge_call(payload, max_retries=2)
    except Exception as e:
        print(f"  [gemini] Bridge failed: {str(e)[:150]}")

    print("  [gemini] Using Pollinations (free)...")
    return _pollinations_call(payload, max_retries)


def _generic_strategy(payload, max_retries, api_key, api_base):
    """Generic key+base: try direct → bridge → Pollinations."""
    try:
        print(f"  [direct] Trying {api_base}...")
        return _direct_call(payload, max_retries, api_key=api_key, api_base=api_base)
    except Exception as e:
        print(f"  [direct] Failed: {str(e)[:150]}")

    try:
        print("  [direct] Falling back to Node.js bridge...")
        return _bridge_call(payload, max_retries=2)
    except Exception as e:
        print(f"  [direct] Bridge failed: {str(e)[:150]}")

    print("  [direct] Using Pollinations (free)...")
    return _pollinations_call(payload, max_retries)


def _no_key_strategy(payload, max_retries):
    """No API key: try bridge → Pollinations."""
    # Try bridge first (z-ai-web-dev-sdk is pre-installed)
    try:
        print("  [no-key] Trying Node.js bridge...")
        return _bridge_call(payload, max_retries=2)
    except Exception as e:
        print(f"  [no-key] Bridge failed: {str(e)[:150]}")

    print("  [no-key] Using Pollinations (free)...")
    return _pollinations_call(payload, max_retries)


# ──────────────────────────────────────────────
# API call implementations
# ──────────────────────────────────────────────

def _proxy_call(payload, max_retries, api_key):
    """Call Groq API via Cloudflare Pages proxy.

    The proxy runs on Cloudflare's edge network and forwards
    requests to api.groq.com, bypassing geo-restrictions.
    """
    model = payload.get("model") or _get_model()
    proxy_payload = {
        "model": model,
        "messages": payload.get("messages", []),
        "max_tokens": payload.get("max_tokens", 8000),
        "temperature": payload.get("temperature", 0.7),
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    for attempt in range(max_retries + 1):
        try:
            print(f"  [proxy] Groq via Cloudflare (attempt {attempt+1}/{max_retries+1})...")
            resp = requests.post(
                GROQ_PROXY_URL,
                headers=headers,
                json=proxy_payload,
                timeout=300,
            )

            if resp.status_code == 429:
                wait = 30 * (attempt + 1)
                if attempt < max_retries:
                    print(f"  [proxy] Rate limited (429). Waiting {wait}s...")
                    time.sleep(wait)
                    continue
                resp.raise_for_status()

            if resp.status_code >= 500:
                if attempt < max_retries:
                    wait = 10 * (attempt + 1)
                    print(f"  [proxy] Server error ({resp.status_code}). Waiting {wait}s...")
                    time.sleep(wait)
                    continue

            # Auth errors — don't retry
            if resp.status_code in (401, 402, 403):
                raise RuntimeError(f"Proxy auth error ({resp.status_code}): {resp.text[:200]}")

            resp.raise_for_status()
            data = resp.json()

            # Tag the response so we know it came via proxy
            if "choices" in data:
                print(f"  [proxy] Success! Model: {data.get('model', 'unknown')}")
            return data

        except requests.exceptions.Timeout:
            if attempt < max_retries:
                wait = 15 * (attempt + 1)
                print(f"  [proxy] Timed out. Waiting {wait}s...")
                time.sleep(wait)
                continue
            raise RuntimeError("Groq proxy timed out after maximum retries")

        except requests.exceptions.ConnectionError:
            if attempt < max_retries:
                wait = 10 * (attempt + 1)
                print(f"  [proxy] Connection error. Waiting {wait}s...")
                time.sleep(wait)
                continue
            raise RuntimeError("Groq proxy connection failed after maximum retries")

    raise RuntimeError("Groq proxy failed after maximum retries")


def _direct_call(payload, max_retries=5, api_key=None, api_base=None):
    """Direct API call to Groq, OpenAI, Gemini, Cerebras, etc."""
    key = api_key or _get_api_key()
    base = api_base or _get_api_base() or GROQ_DIRECT_BASE
    model = payload.get("model") or _get_model()

    call_payload = {
        "model": model,
        "messages": payload.get("messages", []),
        "max_tokens": payload.get("max_tokens", 8000),
        "temperature": payload.get("temperature", 0.7),
    }

    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }

    for attempt in range(max_retries + 1):
        try:
            print(f"  [direct] {base} (attempt {attempt+1}/{max_retries+1})...")
            resp = requests.post(
                f"{base}/chat/completions",
                headers=headers,
                json=call_payload,
                timeout=300,
            )
            if resp.status_code == 429:
                wait = 30 * (attempt + 1)
                if attempt < max_retries:
                    print(f"  [direct] Rate limited (429). Waiting {wait}s...")
                    time.sleep(wait)
                    continue
                else:
                    resp.raise_for_status()
            if resp.status_code >= 500:
                if attempt < max_retries:
                    wait = 10 * (attempt + 1)
                    print(f"  [direct] Server error ({resp.status_code}). Waiting {wait}s...")
                    time.sleep(wait)
                    continue
            # Auth errors (401, 402, 403) — don't retry, raise immediately
            if resp.status_code in (401, 402, 403):
                print(f"  [direct] Auth error ({resp.status_code}): {resp.text[:200]}")
                raise RuntimeError(f"API error {resp.status_code}: {resp.text[:200]}")
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.Timeout:
            if attempt < max_retries:
                wait = 15 * (attempt + 1)
                print(f"  [direct] Timed out. Waiting {wait}s...")
                time.sleep(wait)
                continue
            raise
    resp.raise_for_status()


def _pollinations_call(payload, max_retries=5):
    """Call Pollinations AI — free, no key.

    Uses the OpenAI-compatible endpoint with the "openai" model.
    Handles reasoning_content fallback (Pollinations "openai" is a reasoning model).
    """
    poll_payload = {
        "model": POLLINATIONS_MODEL,
        "messages": payload.get("messages", []),
        "max_tokens": min(payload.get("max_tokens", 8000), 16000),
        "temperature": payload.get("temperature", 0.7),
    }

    headers = {"Content-Type": "application/json"}

    for attempt in range(max_retries + 1):
        try:
            print(f"  [pollinations] Free API (attempt {attempt+1}/{max_retries+1})...")
            resp = requests.post(
                f"{POLLINATIONS_OPENAI_BASE}/chat/completions",
                headers=headers,
                json=poll_payload,
                timeout=600,  # 10 min — reasoning models can be slow
            )

            if resp.status_code == 429:
                wait = 30 * (attempt + 1)
                if attempt < max_retries:
                    print(f"  [pollinations] Rate limited (429). Waiting {wait}s...")
                    time.sleep(wait)
                    continue
                else:
                    resp.raise_for_status()

            if resp.status_code >= 500:
                if attempt < max_retries:
                    wait = 15 * (attempt + 1)
                    print(f"  [pollinations] Server error ({resp.status_code}). Waiting {wait}s...")
                    time.sleep(wait)
                    continue

            # 404 = model not found — don't retry
            if resp.status_code == 404:
                raise RuntimeError(f"Pollinations model not found (404): {resp.text[:200]}")

            resp.raise_for_status()
            data = resp.json()

            # Handle reasoning_content fallback
            if data.get("choices"):
                choice = data["choices"][0]
                msg = choice.get("message", {})
                content = msg.get("content", "")
                reasoning = msg.get("reasoning_content", "")

                if not content or not content.strip():
                    if reasoning and reasoning.strip():
                        print("  [pollinations] Extracting from reasoning_content...")
                        msg["content"] = reasoning
                        if "reasoning_content" in msg:
                            del msg["reasoning_content"]

            return data

        except requests.exceptions.Timeout:
            if attempt < max_retries:
                wait = 30 * (attempt + 1)
                print(f"  [pollinations] Timed out. Waiting {wait}s...")
                time.sleep(wait)
                continue
            raise RuntimeError("Pollinations API timed out after maximum retries")

        except requests.exceptions.ConnectionError:
            if attempt < max_retries:
                wait = 20 * (attempt + 1)
                print(f"  [pollinations] Connection error. Waiting {wait}s...")
                time.sleep(wait)
                continue
            raise RuntimeError("Pollinations API connection failed after maximum retries")

    raise RuntimeError("Pollinations API failed after maximum retries")


def _bridge_call(payload, max_retries=3):
    """Call AI via Node.js bridge (z-ai-web-dev-sdk).

    The bridge uses the z-ai-web-dev-sdk which is pre-installed
    and works from any server location.
    """
    for attempt in range(max_retries + 1):
        try:
            # Write payload to temp file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
                json.dump({
                    "messages": payload.get("messages", []),
                    "max_tokens": payload.get("max_tokens", 4096),
                    "temperature": payload.get("temperature", 0.7),
                }, f)
                temp_path = f.name

            try:
                print(f"  [bridge] z-ai-web-dev-sdk (attempt {attempt+1}/{max_retries+1})...")
                result = subprocess.run(
                    ["node", str(BRIDGE_SCRIPT), "--input-file", temp_path],
                    capture_output=True,
                    text=True,
                    timeout=600,
                    cwd=str(PROJECT_ROOT),
                )

                if result.returncode != 0:
                    error_msg = result.stderr.strip() or "Unknown bridge error"
                    if attempt < max_retries:
                        print(f"  [bridge] Error: {error_msg[:150]}. Retrying...")
                        time.sleep(5)
                        continue
                    raise RuntimeError(f"AI bridge failed: {error_msg}")

                # Parse JSON from stdout
                output = result.stdout.strip()
                json_start = output.find('{')
                if json_start >= 0:
                    output = output[json_start:]

                data = json.loads(output)
                if "choices" in data:
                    print(f"  [bridge] Success! Model: {data.get('model', 'unknown')}")
                return data

            finally:
                try:
                    os.unlink(temp_path)
                except OSError:
                    pass

        except subprocess.TimeoutExpired:
            if attempt < max_retries:
                print(f"  [bridge] Timed out. Retrying ({attempt+1}/{max_retries})...")
                time.sleep(10)
                continue
            raise RuntimeError("AI bridge timed out after maximum retries")

        except json.JSONDecodeError as e:
            if attempt < max_retries:
                print(f"  [bridge] Invalid JSON. Retrying ({attempt+1}/{max_retries})...")
                time.sleep(5)
                continue
            raise RuntimeError(f"AI bridge returned invalid JSON: {e}")

    raise RuntimeError("AI bridge failed after maximum retries")
