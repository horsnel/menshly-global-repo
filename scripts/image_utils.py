#!/usr/bin/env python3
"""Shared image generation utilities for Menshly Global article generators.

Uses Pollination AI (free, no API key) to generate topic-relevant thumbnails
and premium hero/OG images, then remaps every pixel to the strict brand
palette (white/black/acid yellow) and downscales for smooth edges.

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
"""

import io
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

# ── Thumbnail dimensions ──────────────────────────────────────────────
# Generate at 2x for smoother edges, then downscale
GEN_WIDTH = 1344
GEN_HEIGHT = 768
FINAL_WIDTH = 672
FINAL_HEIGHT = 384

# ── Hero/OG image dimensions ──────────────────────────────────────────
# Standard OG image ratio is 1200x630; generate at 2x for smooth edges
HERO_GEN_WIDTH = 2400
HERO_GEN_HEIGHT = 1260
HERO_FINAL_WIDTH = 1200
HERO_FINAL_HEIGHT = 630

# ── Pollination AI endpoint ───────────────────────────────────────────
POLLINATION_URL = "https://image.pollinations.ai/prompt/{prompt}?width={w}&height={h}&nologo=true&seed={seed}"

# ── Static images directories ─────────────────────────────────────────
STATIC_DIR = Path("static/images/articles")
HERO_DIR = Path("static/images/heroes")


def _build_prompt(topic: str) -> str:
    """Build a Pollination AI prompt for the thumbnail (flat icon style)."""
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


def _build_hero_prompt(topic: str) -> str:
    """Build a Pollination AI prompt for the premium hero/OG image.

    Hero images are cinematic, dramatic, and premium — not flat icons.
    They look like a high-end editorial feature image.
    """
    clean = re.sub(r"[^a-zA-Z0-9\s]", "", topic.lower())
    clean = re.sub(r"\bhow to\b|\bin 2026\b|\bcomplete guide\b|\bblueprint\b|\bstep by step\b", "", clean)
    clean = re.sub(r"\s+", " ", clean).strip()

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


def _download_image(prompt: str, seed: int, width: int, height: int, timeout: int = 120) -> bytes:
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


def _downscale_and_remap(img: Image.Image, target_w: int, target_h: int) -> Image.Image:
    """Downscale from 2x to final size, then remap again for smooth edges."""
    img_small = img.resize((target_w, target_h), Image.LANCZOS)

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

    print(f"\n📸 Generating thumbnail for: {slug}")
    print(f"   Topic: {topic}")
    print(f"   Section: {section}")

    # Build prompt
    prompt = _build_prompt(topic)
    print(f"   Prompt: {prompt[:120]}...")

    # Download from Pollination AI
    print("   Downloading from Pollination AI...")
    image_data = _download_image(prompt, seed, GEN_WIDTH, GEN_HEIGHT)
    print(f"   Downloaded: {len(image_data):,} bytes")

    # Load into PIL
    img = Image.open(io.BytesIO(image_data))
    print(f"   Source size: {img.size}")

    # Step 1: Remap at full resolution
    print("   Remapping to brand colours (2x resolution)...")
    img = _remap_brand_colours(img)

    # Step 2: Downscale + remap for smooth edges
    print("   Downscaling for smooth edges...")
    img_final = _downscale_and_remap(img, FINAL_WIDTH, FINAL_HEIGHT)

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


def generate_hero_image(
    topic: str,
    slug: str,
    section: str,
    seed: int | None = None,
) -> str:
    """Generate a premium brand-coloured hero/OG image using Pollination AI.

    Hero images are larger (1200x630), more cinematic and dramatic than
    thumbnails, designed for social sharing and Google search results.

    Args:
        topic: The article topic/title (used to build the image prompt).
        slug: The URL slug (used as the filename).
        section: Content section - "opportunities", "intelligence", or "playbooks".
        seed: Optional seed for reproducibility. Random if not set.

    Returns:
        The Hugo frontmatter hero_image path, e.g. "/images/heroes/opportunities/my-slug.png"
    """
    if seed is None:
        seed = (int(time.time()) + 99999) % 100000  # Different seed from thumbnail

    print(f"\n🌟 Generating hero image for: {slug}")
    print(f"   Topic: {topic}")
    print(f"   Section: {section}")

    # Build premium hero prompt
    prompt = _build_hero_prompt(topic)
    print(f"   Prompt: {prompt[:120]}...")

    # Download from Pollination AI at 2x hero resolution
    print("   Downloading from Pollination AI...")
    image_data = _download_image(prompt, seed, HERO_GEN_WIDTH, HERO_GEN_HEIGHT, timeout=180)
    print(f"   Downloaded: {len(image_data):,} bytes")

    # Load into PIL
    img = Image.open(io.BytesIO(image_data))
    print(f"   Source size: {img.size}")

    # Step 1: Remap at full resolution
    print("   Remapping to brand colours (2x resolution)...")
    img = _remap_brand_colours(img)

    # Step 2: Downscale + remap for smooth edges
    print("   Downscaling for smooth edges...")
    img_final = _downscale_and_remap(img, HERO_FINAL_WIDTH, HERO_FINAL_HEIGHT)

    # Step 3: Save
    out_dir = HERO_DIR / section
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

    hugo_path = f"/images/heroes/{section}/{slug}.png"
    print(f"   Saved: {out_path} ({w}x{h})")
    print(f"   Non-brand pixels: {non_brand}")
    print(f"   Hugo path: {hugo_path}")

    return hugo_path
