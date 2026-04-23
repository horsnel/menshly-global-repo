#!/usr/bin/env python3
"""Shared image generation utilities for Menshly Global article generators.

Uses Pollination AI (free, no API key) to generate topic-relevant thumbnails,
then remaps every pixel to the strict brand palette (white/black/acid yellow)
and downscales for smooth edges.

Usage in generators:
    from image_utils import generate_article_image

    image_path = generate_article_image(
        topic="How to Start an AI Automation Agency",
        slug="ai-automation-agency",
        section="opportunities",  # opportunities | intelligence | playbooks
    )
    # Returns: "/images/articles/opportunities/ai-automation-agency.png"
"""

import os
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image

# ── Brand Colours ──────────────────────────────────────────────────────
WHITE = (255, 255, 255)
BLACK = (26, 26, 26)
YELLOW = (249, 255, 0)
BRAND_COLOURS = [WHITE, BLACK, YELLOW]
BRAND_SET = set(BRAND_COLOURS)

# ── Image dimensions ──────────────────────────────────────────────────
# Generate at 2x for smoother edges, then downscale
GEN_WIDTH = 1344
GEN_HEIGHT = 768
FINAL_WIDTH = 672
FINAL_HEIGHT = 384

# ── Pollination AI endpoint ───────────────────────────────────────────
POLLINATION_URL = "https://image.pollinations.ai/prompt/{prompt}?width={w}&height={h}&nologo=true&seed={seed}"

# ── Static images directory ───────────────────────────────────────────
STATIC_DIR = Path("static/images/articles")


def _build_prompt(topic: str) -> str:
    """Build a Pollination AI prompt from the article topic.

    Creates a topic-relevant flat minimalist icon description that
    forces the model to use only the brand colours.
    """
    # Extract key subject words for a more targeted icon
    clean = re.sub(r"[^a-zA-Z0-9\s]", "", topic.lower())
    clean = re.sub(r"\bhow to\b|\bin 2026\b|\bcomplete guide\b|\bblueprint\b|\bstep by step\b", "", clean)
    clean = re.sub(r"\s+", " ", clean).strip()

    prompt = (
        f"Flat minimalist icon illustration of {clean}, "
        f"strictly using ONLY white black and bright acid yellow #F9FF00 colors, "
        f"solid white background, geometric brutalist style, "
        f"clean sharp vector edges, no gradients no shading, "
        f"bold flat illustration, 3px black borders, no rounded corners, "
        f"perfectly clean and smooth edges, no text no words no letters"
    )
    return prompt


def _download_image(prompt: str, seed: int, timeout: int = 90) -> bytes:
    """Download an image from Pollination AI."""
    encoded_prompt = urllib.parse.quote(prompt)
    url = POLLINATION_URL.format(
        prompt=encoded_prompt,
        w=GEN_WIDTH,
        h=GEN_HEIGHT,
        seed=seed,
    )

    req = urllib.request.Request(url, headers={"User-Agent": "MenshlyGlobal/1.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = resp.read()
                if len(data) > 1000:  # Valid image should be bigger
                    return data
                print(f"  Image too small ({len(data)} bytes), retrying...")
        except Exception as e:
            print(f"  Download attempt {attempt+1} failed: {e}")
            if attempt < 2:
                time.sleep(3)

    raise RuntimeError(f"Failed to download image after 3 attempts")


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


def _downscale_and_remap(img: Image.Image) -> Image.Image:
    """Downscale from 2x to final size, then remap again for smooth edges."""
    img_small = img.resize((FINAL_WIDTH, FINAL_HEIGHT), Image.LANCZOS)

    # The LANCZOS downscale blends brand colours into intermediates,
    # so we remap again to ensure purity
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


def generate_article_image(
    topic: str,
    slug: str,
    section: str,
    seed: int | None = None,
) -> str:
    """Generate a brand-coloured article thumbnail using Pollination AI.

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

    print(f"\n📸 Generating image for: {slug}")
    print(f"   Topic: {topic}")
    print(f"   Section: {section}")

    # Build prompt
    prompt = _build_prompt(topic)
    print(f"   Prompt: {prompt[:120]}...")

    # Download from Pollination AI
    print("   Downloading from Pollination AI...")
    image_data = _download_image(prompt, seed)
    print(f"   Downloaded: {len(image_data):,} bytes")

    # Load into PIL
    import io
    img = Image.open(io.BytesIO(image_data))
    print(f"   Source size: {img.size}")

    # Step 1: Remap at full resolution
    print("   Remapping to brand colours (2x resolution)...")
    img = _remap_brand_colours(img)

    # Step 2: Downscale + remap for smooth edges
    print("   Downscaling for smooth edges...")
    img_final = _downscale_and_remap(img)

    # Step 3: Save
    out_dir = STATIC_DIR / section
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{slug}.png"
    img_final.save(str(out_path), "PNG")

    # Verify purity
    pixels = img_final.load()
    w, h = img_final.size
    non_brand = 0
    for y in range(h):
        for x in range(w):
            if pixels[x, y] not in BRAND_SET:
                non_brand += 1

    hugo_path = f"/images/articles/{section}/{slug}.png"
    print(f"   Saved: {out_path} ({w}x{h})")
    print(f"   Non-brand pixels: {non_brand}")
    print(f"   Hugo path: {hugo_path}")

    return hugo_path
