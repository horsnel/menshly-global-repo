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
# Menshly brand: dark background with neon green/purple/teal tech aesthetic
DARK_BG = (8, 8, 24)       # #080818 deep dark blue-black
NEON_GREEN = (0, 255, 128)  # #00FF80 neon green
NEON_PURPLE = (140, 80, 255) # #8C50FF neon purple
NEON_TEAL = (0, 210, 210)   # #00D2D2 neon teal
WHITE = (255, 255, 255)

# Brand colours for Pollination fallback remapping
BRAND_DARK = (8, 8, 24)           # #080818
BRAND_GREEN = (0, 255, 128)        # #00FF80
BRAND_PURPLE = (140, 80, 255)      # #8C50FF
BRAND_TEAL = (0, 210, 210)         # #00D2D2
BRAND_COLOURS = [BRAND_DARK, BRAND_GREEN, BRAND_PURPLE, BRAND_TEAL]
BRAND_SET = set(BRAND_COLOURS)

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
    """Build a premium AI image prompt for article thumbnails (Menshly neon tech aesthetic)."""
    clean = _clean_topic(topic)

    section_style = {
        "opportunities": "futuristic business dashboard with holographic revenue charts, growth metrics, and neon data visualizations",
        "intelligence": "advanced AI system blueprint with interconnected workflow nodes, glowing circuit patterns, and data pipelines",
        "playbooks": "digital playbook interface with modular procedure cards, neon progress indicators, and step-by-step workflows",
    }
    style = section_style.get(section, section_style["opportunities"])

    prompt = (
        f"Premium editorial illustration of {clean}, "
        f"showing {style}, "
        f"dark deep blue-black background with neon green (#00FF80) and purple (#8C50FF) glowing accents, "
        f"futuristic tech aesthetic with holographic elements and neon circuit patterns, "
        f"3D isometric view with clean geometric shapes and luminous edges, "
        f"teal (#00D2D2) accent highlights on floating data screens, "
        f"professional AI technology magazine cover quality, "
        f"no text no words no letters no numbers no people no Chinese characters, "
        f"sharp clean vector-quality edges, NO blue-and-gold color scheme, NO brutalist style, NO red color"
    )
    return prompt


def _build_premium_hero_prompt(topic: str, section: str) -> str:
    """Build a cinematic hero/OG image prompt (Menshly neon tech aesthetic)."""
    clean = _clean_topic(topic)

    section_style = {
        "opportunities": "holographic command center with neon green growth charts and purple data streams flowing between business modules",
        "intelligence": "vast AI automation chamber with floating holographic screens, neon green circuit paths, and purple-lit workflow nodes",
        "playbooks": "grand digital vault with floating neon playbook pages, teal progress markers, and purple modular step indicators",
    }
    style = section_style.get(section, section_style["opportunities"])

    prompt = (
        f"Cinematic wide hero banner of {clean}, "
        f"depicting {style}, "
        f"dark deep blue-black (#080818) atmospheric background with neon green (#00FF80) and purple (#8C50FF) light streams, "
        f"epic dramatic composition with teal (#00D2D2) accent highlights, "
        f"futuristic tech aesthetic with holographic elements and neon glowing edges, "
        f"premium editorial magazine quality, "
        f"no text no words no letters no numbers no people no Chinese characters, "
        f"ultra-clean sharp edges, atmospheric depth, NO blue-and-gold color scheme, NO brutalist style, NO red color"
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
    """Build a Pollination AI prompt for the thumbnail (Menshly neon tech style)."""
    clean = _clean_topic(topic)
    prompt = (
        f"Flat minimalist icon illustration of {clean}, "
        f"dark deep blue-black background with neon green (#00FF80) and purple (#8C50FF) glowing accents, "
        f"futuristic tech style with holographic elements, "
        f"clean sharp vector edges with neon-lit geometric shapes, "
        f"teal (#00D2D2) highlight accents, "
        f"no text no words no letters no Chinese characters, "
        f"NO blue-and-gold colors, NO brutalist style, NO red color"
    )
    return prompt


def _build_pollination_hero_prompt(topic: str) -> str:
    """Build a Pollination AI prompt for the hero/OG image (Menshly neon tech style)."""
    clean = _clean_topic(topic)
    prompt = (
        f"Premium cinematic editorial hero image of {clean}, "
        f"dark deep blue-black (#080818) background with neon green (#00FF80) and purple (#8C50FF) glowing light streams, "
        f"dramatic composition with teal (#00D2D2) accent highlights, "
        f"futuristic tech landscape with holographic elements, "
        f"premium neon-lit editorial design, high contrast dark and neon, "
        f"abstract futuristic tech aesthetic, "
        f"professional magazine cover quality, "
        f"no text no words no letters no numbers no Chinese characters, "
        f"sharp clean vector-quality edges, NO blue-and-gold colors, NO brutalist style, NO red color"
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


def _remap_brand_colours(img: Image.Image) -> Image.Image:
    """Remap every pixel to the nearest brand colour."""
    img = img.convert("RGB")
    pixels = img.load()
    w, h = img.size

    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y]
            best = None
            best_dist = float("inf")
            for bc in BRAND_COLOURS:
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
            for bc in BRAND_COLOURS:
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
    img = _remap_brand_colours(img)
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
    img = _remap_brand_colours(img)
    img_final = _downscale_and_remap(img, *POLLINATION_HERO_FINAL)
    img_final.save(out_path, "PNG")

    hugo_path = f"/images/heroes/{section}/{slug}.png"
    print(f"   Saved: {out_path}")
    print(f"   Hugo path: {hugo_path}")
    return hugo_path
