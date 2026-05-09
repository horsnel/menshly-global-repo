#!/usr/bin/env python3
"""Shared image generation utilities for Menshly Global article generators.

Uses z-ai-web-dev-sdk CLI (z-ai-generate) to generate premium, brand-aligned
thumbnails and hero/OG images with the Tesla/Braun-inspired aesthetic.

Usage in generators:
    from image_utils import generate_article_image, generate_hero_image

    image_path = generate_article_image(
        topic="How to Start an AI Automation Agency",
        slug="ai-automation-agency",
        section="opportunities",
    )
    # Returns: "/images/articles/opportunities/ai-automation-agency.png"

    hero_path = generate_hero_image(
        topic="How to Start an AI Automation Agency",
        slug="ai-automation-agency",
        section="opportunities",
    )
    # Returns: "/images/heroes/opportunities/ai-automation-agency.png"

FALLBACK: If z-ai-generate is unavailable, falls back to Pollination AI (free, no API key).
"""

import io
import os
import re
import time
import subprocess
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image

# ── Brand Colours ──────────────────────────────────────────────────────
NAVY = (10, 22, 40)       # #0A1628
GOLD = (240, 192, 64)     # #F0C040
WHITE = (255, 255, 255)
BLACK = (26, 26, 26)

# Legacy brand colours (for Pollination fallback)
LEGACY_WHITE = (255, 255, 255)
LEGACY_BLACK = (26, 26, 26)
LEGACY_YELLOW = (249, 255, 0)
LEGACY_BRAND_COLOURS = [LEGACY_WHITE, LEGACY_BLACK, LEGACY_YELLOW]
LEGACY_BRAND_SET = set(LEGACY_BRAND_COLOURS)

# ── Image dimensions ──────────────────────────────────────────────────
THUMB_SIZE = "1344x768"    # z-ai-generate size for thumbnails
HERO_SIZE = "1344x768"     # z-ai-generate size for hero images

# Pollination fallback dimensions
POLLINATION_THUMB_GEN = (1344, 768)
POLLINATION_THUMB_FINAL = (672, 384)
POLLINATION_HERO_GEN = (2400, 1260)
POLLINATION_HERO_FINAL = (1200, 630)

# ── Static images directories ─────────────────────────────────────────
STATIC_DIR = Path("static/images/articles")
HERO_DIR = Path("static/images/heroes")

# ── Pollination AI endpoint (fallback) ────────────────────────────────
POLLINATION_URL = "https://image.pollinations.ai/prompt/{prompt}?width={w}&height={h}&nologo=true&seed={seed}"


# ── Prompt builders ────────────────────────────────────────────────────

def _clean_topic(topic: str) -> str:
    """Clean a topic string for use in image prompts."""
    clean = re.sub(r"[^a-zA-Z0-9\s]", "", topic.lower())
    clean = re.sub(r"\bhow to\b|\bin 2026\b|\bcomplete guide\b|\bblueprint\b|\bstep by step\b", "", clean)
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean


def _build_premium_thumbnail_prompt(topic: str, section: str) -> str:
    """Build a premium AI image prompt for article thumbnails (Tesla/Braun aesthetic)."""
    clean = _clean_topic(topic)

    section_style = {
        "opportunities": "business opportunity visualization with revenue indicators and growth arrows",
        "intelligence": "technical implementation diagram with workflow nodes and data pipelines",
        "playbooks": "comprehensive system blueprint with modular procedures and checklists",
    }
    style = section_style.get(section, section_style["opportunities"])

    prompt = (
        f"Premium editorial illustration of {clean}, "
        f"showing {style}, "
        f"strictly using deep navy blue (#0A1628) background with gold (#F0C040) accent lighting and highlights, "
        f"clean minimalist Tesla-inspired design, "
        f"bold geometric shapes with luminous gold edges, "
        f"abstract futuristic tech aesthetic, "
        f"professional magazine cover quality, "
        f"no text no words no letters no numbers no people, "
        f"sharp clean vector-quality edges"
    )
    return prompt


def _build_premium_hero_prompt(topic: str, section: str) -> str:
    """Build a cinematic hero/OG image prompt (Tesla/Braun aesthetic)."""
    clean = _clean_topic(topic)

    section_style = {
        "opportunities": "transformative before-and-after business metamorphosis with golden light illuminating the future state",
        "intelligence": "sophisticated automation blueprint unfolding with connected nodes and flowing golden data pipelines",
        "playbooks": "grand vaulted space with golden light streaming from a central open playbook, illuminating floating icons",
    }
    style = section_style.get(section, section_style["opportunities"])

    prompt = (
        f"Cinematic wide hero banner of {clean}, "
        f"depicting {style}, "
        f"strictly using deep navy blue (#0A1628) atmospheric background with brilliant gold (#F0C040) light streams and accents, "
        f"epic dramatic composition with radial gold light, "
        f"Tesla-inspired minimalist luxury aesthetic, "
        f"premium editorial magazine quality, "
        f"no text no words no letters no numbers no people, "
        f"ultra-clean sharp edges, atmospheric depth"
    )
    return prompt


# ── z-ai-generate CLI image generation ─────────────────────────────────

def _generate_via_cli(prompt: str, output_path: str, size: str = "1344x768") -> bool:
    """Generate an image using the z-ai-generate CLI tool.
    
    Returns True on success, False on failure.
    """
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    cmd = [
        "z-ai-generate",
        "--prompt", prompt,
        "--output", output_path,
        "--size", size,
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=180,
        )
        if result.returncode == 0 and os.path.exists(output_path):
            file_size = os.path.getsize(output_path)
            print(f"  ✅ CLI generated: {output_path} ({file_size:,} bytes)")
            return True
        else:
            print(f"  ⚠️ CLI failed: {result.stderr[:200] if result.stderr else 'Unknown error'}")
            if os.path.exists(output_path):
                os.remove(output_path)
            return False
    except subprocess.TimeoutExpired:
        print(f"  ⚠️ CLI timeout")
        return False
    except FileNotFoundError:
        print(f"  ⚠️ z-ai-generate CLI not found, will fall back to Pollination")
        return False
    except Exception as e:
        print(f"  ⚠️ CLI error: {e}")
        return False


def _cli_available() -> bool:
    """Check if z-ai-generate CLI is available."""
    try:
        result = subprocess.run(
            ["z-ai-generate", "--help"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired, Exception):
        return False


# ── Pollination AI fallback ────────────────────────────────────────────

def _build_pollination_prompt(topic: str) -> str:
    """Build a Pollination AI prompt for the thumbnail (flat icon style)."""
    clean = _clean_topic(topic)
    prompt = (
        f"Flat minimalist icon illustration of {clean}, "
        f"strictly using ONLY white black and bright acid yellow #F9FF00 colors, "
        f"solid white background, geometric brutalist style, "
        f"clean sharp vector edges, no gradients no shading, "
        f"bold flat illustration, 3px black borders, no rounded corners, "
        f"perfectly clean and smooth edges, no text no words no letters"
    )
    return prompt


def _build_pollination_hero_prompt(topic: str) -> str:
    """Build a Pollination AI prompt for the hero/OG image."""
    clean = _clean_topic(topic)
    prompt = (
        f"Premium cinematic editorial hero image of {clean}, "
        f"strictly using ONLY white black and bright acid yellow #F9FF00 colors, "
        f"dramatic composition with acid yellow #F9FF00 accent lighting and shadows, "
        f"bold geometric shapes and layered depth, "
        f"Swiss brutalist editorial design, high contrast black and yellow, "
        f"abstract futuristic tech landscape, "
        f"professional magazine cover quality, "
        f"no gradients no shading only flat hard-edge colour blocks, "
        f"3px black borders on all elements, no rounded corners, "
        f"no text no words no letters no numbers, "
        f"sharp clean vector-quality edges"
    )
    return prompt


def _download_pollination_image(prompt: str, seed: int, width: int, height: int, timeout: int = 120) -> bytes:
    """Download an image from Pollination AI at the specified dimensions."""
    encoded_prompt = urllib.parse.quote(prompt)
    url = POLLINATION_URL.format(
        prompt=encoded_prompt,
        w=width,
        h=height,
        seed=seed,
    )

    req = urllib.request.Request(url, headers={"User-Agent": "MenshlyGlobal/1.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = resp.read()
                if len(data) > 1000:
                    return data
                print(f"  Image too small ({len(data)} bytes), retrying...")
        except Exception as e:
            print(f"  Download attempt {attempt+1} failed: {e}")
            if attempt < 2:
                time.sleep(3)

    raise RuntimeError("Failed to download image after 3 attempts")


def _remap_legacy_colours(img: Image.Image) -> Image.Image:
    """Remap every pixel to the nearest legacy brand colour."""
    img = img.convert("RGB")
    pixels = img.load()
    w, h = img.size

    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y]
            best = None
            best_dist = float("inf")
            for bc in LEGACY_BRAND_COLOURS:
                dist = (r - bc[0]) ** 2 + (g - bc[1]) ** 2 + (b - bc[2]) ** 2
                if dist < best_dist:
                    best_dist = dist
                    best = bc
            pixels[x, y] = best

    return img


def _downscale_and_remap(img: Image.Image, target_w: int, target_h: int) -> Image.Image:
    """Downscale from gen size to final size, then remap for smooth edges."""
    img_small = img.resize((target_w, target_h), Image.LANCZOS)
    pixels = img_small.load()
    w, h = img_small.size
    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y]
            best = None
            best_dist = float("inf")
            for bc in LEGACY_BRAND_COLOURS:
                dist = (r - bc[0]) ** 2 + (g - bc[1]) ** 2 + (b - bc[2]) ** 2
                if dist < best_dist:
                    best_dist = dist
                    best = bc
            pixels[x, y] = best
    return img_small


# ── Public API ─────────────────────────────────────────────────────────

def generate_article_image(
    topic: str,
    slug: str,
    section: str,
    seed: int | None = None,
) -> str:
    """Generate a brand-coloured article thumbnail.

    Tries z-ai-generate CLI first (premium Tesla/Braun aesthetic).
    Falls back to Pollination AI (free, no API key) if CLI unavailable.

    Args:
        topic: The article topic/title (used to build the image prompt).
        slug: The URL slug (used as the filename).
        section: Content section - "opportunities", "intelligence", or "playbooks".
        seed: Optional seed for reproducibility. Random if not set.

    Returns:
        The Hugo frontmatter image path, e.g. "/images/articles/opportunities/my-slug.png"
    """
    if seed is None:
        seed = int(time.time()) % 100000

    print(f"\n📸 Generating thumbnail for: {slug}")
    print(f"   Topic: {topic}")
    print(f"   Section: {section}")

    # Ensure output directory exists
    out_dir = STATIC_DIR / section
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = str(out_dir / f"{slug}.png")

    # Try premium CLI generation first
    prompt = _build_premium_thumbnail_prompt(topic, section)
    print(f"   Prompt: {prompt[:120]}...")

    if _generate_via_cli(prompt, out_path, THUMB_SIZE):
        hugo_path = f"/images/articles/{section}/{slug}.png"
        print(f"   Hugo path: {hugo_path}")
        return hugo_path

    # Fallback to Pollination AI
    print("   Falling back to Pollination AI...")
    pollination_prompt = _build_pollination_prompt(topic)
    image_data = _download_pollination_image(pollination_prompt, seed, *POLLINATION_THUMB_GEN)
    img = Image.open(io.BytesIO(image_data))
    img = _remap_legacy_colours(img)
    img_final = _downscale_and_remap(img, *POLLINATION_THUMB_FINAL)
    img_final.save(out_path, "PNG")

    hugo_path = f"/images/articles/{section}/{slug}.png"
    print(f"   Saved: {out_path}")
    print(f"   Hugo path: {hugo_path}")
    return hugo_path


def generate_hero_image(
    topic: str,
    slug: str,
    section: str,
    seed: int | None = None,
) -> str:
    """Generate a premium brand-coloured hero/OG image.

    Tries z-ai-generate CLI first (premium Tesla/Braun aesthetic).
    Falls back to Pollination AI (free, no API key) if CLI unavailable.

    Args:
        topic: The article topic/title (used to build the image prompt).
        slug: The URL slug (used as the filename).
        section: Content section - "opportunities", "intelligence", or "playbooks".
        seed: Optional seed for reproducibility. Random if not set.

    Returns:
        The Hugo frontmatter hero_image path, e.g. "/images/heroes/opportunities/my-slug.png"
    """
    if seed is None:
        seed = (int(time.time()) + 99999) % 100000

    print(f"\n🌟 Generating hero image for: {slug}")
    print(f"   Topic: {topic}")
    print(f"   Section: {section}")

    # Ensure output directory exists
    out_dir = HERO_DIR / section
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = str(out_dir / f"{slug}.png")

    # Try premium CLI generation first
    prompt = _build_premium_hero_prompt(topic, section)
    print(f"   Prompt: {prompt[:120]}...")

    if _generate_via_cli(prompt, out_path, HERO_SIZE):
        hugo_path = f"/images/heroes/{section}/{slug}.png"
        print(f"   Hugo path: {hugo_path}")
        return hugo_path

    # Fallback to Pollination AI
    print("   Falling back to Pollination AI...")
    pollination_prompt = _build_pollination_hero_prompt(topic)
    image_data = _download_pollination_image(pollination_prompt, seed, *POLLINATION_HERO_GEN, timeout=180)
    img = Image.open(io.BytesIO(image_data))
    img = _remap_legacy_colours(img)
    img_final = _downscale_and_remap(img, *POLLINATION_HERO_FINAL)
    img_final.save(out_path, "PNG")

    hugo_path = f"/images/heroes/{section}/{slug}.png"
    print(f"   Saved: {out_path}")
    print(f"   Hugo path: {hugo_path}")
    return hugo_path
