#!/usr/bin/env python3
"""Shared AI API utility for Menshly Global article generators.

Supports two modes:
1. Direct API call (Groq, OpenAI, etc.) when AI_API_KEY is a real API key
2. Node.js bridge via z-ai-web-dev-sdk when AI_API_BASE contains 'localhost' or
   AI_API_KEY contains 'local-proxy' or 'bridge'

The bridge mode calls: node scripts/ai-bridge.js --input-file /tmp/payload.json
This allows Python generators to use the z-ai-web-dev-sdk without needing
a separate HTTP server.
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


def _use_bridge() -> bool:
    """Determine if we should use the Node.js bridge instead of direct API."""
    api_key = os.environ.get("AI_API_KEY", "")
    api_base = os.environ.get("AI_API_BASE", "")
    # Use bridge if: local proxy key, localhost base, or if the API key doesn't look valid
    if "local-proxy" in api_key or "bridge" in api_key:
        return True
    if "localhost" in api_base or "127.0.0.1" in api_base:
        return True
    # If API key is empty or looks invalid, try bridge
    if not api_key or api_key.startswith("gsk_") is False:
        return True
    return False


def api_call(payload, max_retries=5, api_key=None, api_base=None):
    """Call the AI API with automatic retry on rate limits and server errors.

    Supports both direct API calls and Node.js bridge mode.
    """
    use_bridge = _use_bridge()

    if use_bridge:
        return _bridge_call(payload, max_retries)

    # Direct API call mode
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
                    timeout=600,  # 10 min timeout for long generations
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
                # Handle case where there might be log messages before the JSON
                json_start = output.find('{')
                if json_start >= 0:
                    output = output[json_start:]

                data = json.loads(output)
                return data

            finally:
                # Clean up temp file
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
