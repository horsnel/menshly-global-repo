#!/usr/bin/env python3
"""Shared AI API utility for Menshly Global article generators.

Supports three modes (in priority order):
1. Direct API call (Groq, OpenAI, Cerebras, etc.) when AI_API_KEY is set and valid
2. Pollinations AI (free, no key) as automatic fallback when no key or key fails
3. Node.js bridge via z-ai-web-dev-sdk when AI_API_BASE contains 'localhost' or
   AI_API_KEY contains 'local-proxy' or 'bridge'

The Pollinations fallback ensures GitHub Actions workflows always work even
without paid API keys. It's free, OpenAI-compatible, and requires no authentication.
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

# Pollinations API — free, no key, OpenAI-compatible
POLLINATIONS_BASE = "https://text.pollinations.ai/openai"
POLLINATIONS_MODEL = "openai"  # reasoning model, supports long outputs

# Gemini API — Google's LLM, OpenAI-compatible endpoint
GEMINI_API_BASE = "https://generativelanguage.googleapis.com/v1beta/openai"
GEMINI_MODEL = "gemini-2.0-flash"
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")


def _use_bridge() -> bool:
    """Determine if we should use the Node.js bridge instead of direct API."""
    api_key = os.environ.get("AI_API_KEY", "")
    api_base = os.environ.get("AI_API_BASE", "")
    if "local-proxy" in api_key or "bridge" in api_key:
        return True
    if "localhost" in api_base or "127.0.0.1" in api_base:
        return True
    return False


def _use_direct_api() -> bool:
    """Determine if we have a real API key to make direct calls."""
    api_key = os.environ.get("AI_API_KEY", "")
    api_base = os.environ.get("AI_API_BASE", "")
    # Only use direct API if we have a non-empty key AND an explicit base URL
    if api_key and api_base:
        return True
    # Groq keys start with gsk_
    if api_key and api_key.startswith("gsk_"):
        return True
    # Gemini keys start with AIza
    if api_key and api_key.startswith("AIza"):
        return True
    return False


def api_call(payload, max_retries=5, api_key=None, api_base=None):
    """Call the AI API with automatic retry and Pollinations fallback.

    Strategy:
    1. If bridge mode → use Node.js bridge
    2. If direct API key available → try direct call first
    3. If direct call fails → fall back to Pollinations (free)
    4. If no key at all → use Pollinations directly
    """
    # Bridge mode takes priority (local dev with z-ai-web-dev-sdk)
    if _use_bridge():
        try:
            return _bridge_call(payload, max_retries)
        except RuntimeError as e:
            print(f"  Bridge failed, falling back to Pollinations: {e}")
            return _pollinations_call(payload, max_retries)

    # Try Gemini if available (fast, generous quota when active)
    if GEMINI_API_KEY and not api_key:
        try:
            print("  Trying Gemini API...")
            return _direct_call(payload, max_retries, api_key=GEMINI_API_KEY, api_base=GEMINI_API_BASE)
        except Exception as e:
            error_msg = str(e)[:200]
            print(f"  Gemini API failed: {error_msg}")
            print(f"  Falling back to Pollinations (free)...")
            return _pollinations_call(payload, max_retries)

    # Direct API mode
    if api_key or _use_direct_api():
        try:
            return _direct_call(payload, max_retries, api_key=api_key, api_base=api_base)
        except Exception as e:
            error_msg = str(e)[:200]
            print(f"  Direct API failed: {error_msg}")
            # Try Gemini as secondary fallback before Pollinations
            if GEMINI_API_KEY:
                try:
                    print(f"  Trying Gemini API as fallback...")
                    return _direct_call(payload, max_retries=2, api_key=GEMINI_API_KEY, api_base=GEMINI_API_BASE)
                except Exception as e2:
                    print(f"  Gemini fallback also failed: {str(e2)[:200]}")
            print(f"  Falling back to Pollinations (free)...")
            return _pollinations_call(payload, max_retries)

    # No API key — try Gemini, then Pollinations
    if GEMINI_API_KEY:
        try:
            print("  Trying Gemini API...")
            return _direct_call(payload, max_retries, api_key=GEMINI_API_KEY, api_base=GEMINI_API_BASE)
        except Exception as e:
            print(f"  Gemini failed: {str(e)[:200]}")

    print("  No API key configured, using Pollinations (free)...")
    return _pollinations_call(payload, max_retries)


def _direct_call(payload, max_retries=5, api_key=None, api_base=None):
    """Direct API call to Groq, OpenAI, Cerebras, etc."""
    key = api_key or os.environ.get("AI_API_KEY", "")
    base = api_base or os.environ.get("AI_API_BASE", "https://api.groq.com/openai/v1")
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }
    for attempt in range(max_retries + 1):
        try:
            resp = requests.post(
                f"{base}/chat/completions",
                headers=headers,
                json=payload,
                timeout=300,
            )
            if resp.status_code == 429:
                wait = 30 * (attempt + 1)
                if attempt < max_retries:
                    print(f"  Rate limited (429). Waiting {wait}s before retry {attempt+1}/{max_retries}...")
                    time.sleep(wait)
                    continue
                else:
                    resp.raise_for_status()
            if resp.status_code >= 500:
                if attempt < max_retries:
                    wait = 10 * (attempt + 1)
                    print(f"  Server error ({resp.status_code}). Waiting {wait}s...")
                    time.sleep(wait)
                    continue
            # Auth errors (401, 402, 403) — don't retry, raise immediately
            if resp.status_code in (401, 402, 403):
                print(f"  API auth/payment error ({resp.status_code}): {resp.text[:200]}")
                raise RuntimeError(f"API error {resp.status_code}: {resp.text[:200]}")
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.Timeout:
            if attempt < max_retries:
                wait = 15 * (attempt + 1)
                print(f"  Request timed out. Waiting {wait}s...")
                time.sleep(wait)
                continue
            raise
    resp.raise_for_status()


def _pollinations_call(payload, max_retries=5):
    """Call Pollinations AI — free, no key, OpenAI-compatible.

    The "openai" model on Pollinations is a reasoning model that may put
    content in `reasoning_content` instead of `content`. We handle both.
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
            print(f"  Pollinations API call (attempt {attempt+1}/{max_retries+1})...")
            resp = requests.post(
                f"{POLLINATIONS_BASE}/chat/completions",
                headers=headers,
                json=poll_payload,
                timeout=600,  # 10 min — reasoning models can be slow
            )

            if resp.status_code == 429:
                wait = 30 * (attempt + 1)
                if attempt < max_retries:
                    print(f"  Rate limited (429). Waiting {wait}s...")
                    time.sleep(wait)
                    continue
                else:
                    resp.raise_for_status()

            if resp.status_code >= 500:
                if attempt < max_retries:
                    wait = 15 * (attempt + 1)
                    print(f"  Server error ({resp.status_code}). Waiting {wait}s...")
                    time.sleep(wait)
                    continue

            resp.raise_for_status()
            data = resp.json()

            # Handle reasoning_content fallback
            # The Pollinations "openai" model may put content in reasoning_content
            # instead of content. We extract from either field.
            if data.get("choices"):
                choice = data["choices"][0]
                msg = choice.get("message", {})
                content = msg.get("content", "")
                reasoning = msg.get("reasoning_content", "")

                if not content or not content.strip():
                    if reasoning and reasoning.strip():
                        print(f"  Extracting content from reasoning_content field...")
                        msg["content"] = reasoning
                        # Clear reasoning to avoid confusion
                        if "reasoning_content" in msg:
                            del msg["reasoning_content"]

            return data

        except requests.exceptions.Timeout:
            if attempt < max_retries:
                wait = 30 * (attempt + 1)
                print(f"  Pollinations timed out. Waiting {wait}s...")
                time.sleep(wait)
                continue
            raise RuntimeError("Pollinations API timed out after maximum retries")

        except requests.exceptions.ConnectionError:
            if attempt < max_retries:
                wait = 20 * (attempt + 1)
                print(f"  Connection error. Waiting {wait}s...")
                time.sleep(wait)
                continue
            raise RuntimeError("Pollinations API connection failed after maximum retries")

    raise RuntimeError("Pollinations API failed after maximum retries")


def _bridge_call(payload, max_retries=3):
    """Call AI via Node.js bridge (z-ai-web-dev-sdk)."""
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
                        print(f"  Bridge error: {error_msg[:200]}. Retrying ({attempt+1}/{max_retries})...")
                        time.sleep(5)
                        continue
                    raise RuntimeError(f"AI bridge failed: {error_msg}")

                # Parse JSON from stdout
                output = result.stdout.strip()
                json_start = output.find('{')
                if json_start >= 0:
                    output = output[json_start:]

                data = json.loads(output)
                return data

            finally:
                try:
                    os.unlink(temp_path)
                except OSError:
                    pass

        except subprocess.TimeoutExpired:
            if attempt < max_retries:
                print(f"  Bridge timed out. Retrying ({attempt+1}/{max_retries})...")
                time.sleep(10)
                continue
            raise RuntimeError("AI bridge timed out after maximum retries")

        except json.JSONDecodeError as e:
            if attempt < max_retries:
                print(f"  Bridge returned invalid JSON. Retrying ({attempt+1}/{max_retries})...")
                time.sleep(5)
                continue
            raise RuntimeError(f"AI bridge returned invalid JSON: {e}")

    raise RuntimeError("AI bridge failed after maximum retries")
