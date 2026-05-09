#!/usr/bin/env python3
"""Auto-generate hero images and thumbnails for articles that are missing them.

Scans all content sections (opportunities, intelligence, playbooks) and:
  1. Finds articles with missing image files
  2. Finds articles with Pollination AI URLs (not local files) in front matter
  3. Generates premium AI images using z-ai-web-dev-sdk (Node.js CLI)
  4. Updates front matter to point to local files
  5. Optionally forces regeneration of ALL images (--force flag)

Usage:
  python3 scripts/auto_generate_images.py              # Generate only missing images
  python3 scripts/auto_generate_images.py --force       # Regenerate ALL images
  python3 scripts/auto_generate_images.py --low-quality  # Regenerate only low-quality images (<20KB)
  python3 scripts/auto_generate_images.py --section opportunities  # Only one section
  python3 scripts/auto_generate_images.py --slug ai-seo-agency-2026  # Only one article
  python3 scripts/auto_generate_images.py --limit 5     # Process max 5 articles per run
  python3 scripts/auto_generate_images.py --thumbnails-only  # Skip hero images
  python3 scripts/auto_generate_images.py --heroes-only       # Skip thumbnail images
"""

import os
import re
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO_ROOT / "content"
STATIC_IMAGES = REPO_ROOT / "static" / "images"
ARTICLE_IMAGES = STATIC_IMAGES / "articles"
HERO_IMAGES = STATIC_IMAGES / "heroes"

SECTIONS = ["opportunities", "intelligence", "playbooks"]

# Quality threshold: images below this size (bytes) are considered low-quality placeholders
LOW_QUALITY_THRESHOLD = 20 * 1024  # 20KB

# ── Prompt builders ────────────────────────────────────────────────────

def build_thumbnail_prompt(title: str, section: str, excerpt: str = "") -> str:
    """Build a premium AI image prompt for article thumbnails."""
    clean = re.sub(r"[^a-zA-Z0-9\s]", "", title.lower())
    clean = re.sub(r"\bhow to\b|\bin 2026\b|\bcomplete guide\b|\bblueprint\b|\bstep by step\b", "", clean)
    clean = re.sub(r"\s+", " ", clean).strip()

    section_style = {
        "opportunities": (
            f"a futuristic command center dashboard for {clean} floating in deep navy space, "
            "holographic revenue indicators and growth arrows rendered in brilliant gold, "
            "crystalline data streams connecting business metrics with glowing amber nodes, "
            "abstract geometric shapes representing market opportunities with gold wireframe edges, "
            "a subtle radial gold light emanating from the center"
        ),
        "intelligence": (
            f"an advanced AI automation blueprint for {clean}, "
            "a luminous gold circuit-board pattern on deep navy background, "
            "interconnected workflow nodes with glowing amber connections, "
            "a central AI processor chip radiating golden light pulses, "
            "flowing data pipelines rendered as golden rivers, "
            "holographic API connection points with precise geometric alignment"
        ),
        "playbooks": (
            f"an elite playbook blueprint for {clean}, "
            "a grand golden open book floating in deep navy space with luminous pages revealing modular workflow diagrams, "
            "geometric checklists and procedure flowcharts rendered in amber and gold, "
            "floating gold-rimmed module cards arranged in a grid pattern, "
            "crystalline milestone markers with warm golden glow"
        ),
    }

    style = section_style.get(section, section_style["opportunities"])

    prompt = (
        f"Ultra-premium editorial illustration: {style}, "
        f"strictly using deep navy blue (#0A1628) background with gold (#F0C040) accent lighting and highlights, "
        f"Tesla-inspired minimalist luxury aesthetic, "
        f"bold geometric shapes with luminous gold edges and warm amber glow, "
        f"abstract futuristic tech aesthetic with atmospheric depth, "
        f"professional magazine cover quality, "
        f"no text no words no letters no numbers no people no faces, "
        f"sharp clean vector-quality edges, 8K quality"
    )
    return prompt


def build_hero_prompt(title: str, section: str, excerpt: str = "") -> str:
    """Build a cinematic hero/OG image prompt."""
    clean = re.sub(r"[^a-zA-Z0-9\s]", "", title.lower())
    clean = re.sub(r"\bhow to\b|\bin 2026\b|\bcomplete guide\b|\bblueprint\b|\bstep by step\b", "", clean)
    clean = re.sub(r"\s+", " ", clean).strip()

    section_style = {
        "opportunities": (
            f"a grand {clean} cathedral scene, "
            "towering digital columns of revenue data rising from a deep navy abyss, "
            "brilliant gold light streaming through geometric archways revealing market analytics and growth graphs, "
            "floating holographic business cards with gold-trimmed edges, "
            "a dramatic golden sunrise at the far end of a perspective corridor"
        ),
        "intelligence": (
            f"a sophisticated {clean} command center, "
            "a vast deep navy space with towering holographic screens displaying automation workflow diagrams, "
            "golden data streams flowing between floating modules like liquid amber, "
            "a dramatic perspective corridor lined with illuminated workflow nodes, "
            "epic golden light casting long geometric shadows"
        ),
        "playbooks": (
            f"a grand vaulted chamber for {clean}, "
            "golden light streaming from a central floating open playbook, "
            "illuminating floating holographic procedure icons and modular step markers, "
            "deep navy atmospheric walls receding into dramatic perspective, "
            "illuminated golden columns representing playbook modules, "
            "volumetric gold light rays creating atmospheric depth"
        ),
    }

    style = section_style.get(section, section_style["opportunities"])

    prompt = (
        f"Cinematic wide hero banner: {style}, "
        f"strictly using deep navy blue (#0A1628) atmospheric background with brilliant gold (#F0C040) light streams and accents, "
        f"epic dramatic composition with volumetric gold light rays, "
        f"Tesla-inspired minimalist luxury aesthetic, "
        f"premium editorial magazine quality, "
        f"no text no words no letters no numbers no people no faces, "
        f"ultra-clean sharp edges, atmospheric depth with layered navy-to-black gradient, 8K quality"
    )
    return prompt


# ── Image generation via z-ai-web-dev-sdk CLI ──────────────────────────

def generate_image(prompt: str, output_path: str, size: str = "1344x768") -> bool:
    """Generate an image using the z-ai-generate CLI tool."""
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    # Try local CLI first, then npx fallback (for CI environments)
    cli_cmd = "z-ai-generate"
    if subprocess.run(["which", "z-ai-generate"], capture_output=True).returncode != 0:
        cli_cmd = "npx z-ai-generate"

    cmd = [
        *cli_cmd.split(),
        "--prompt", prompt,
        "--output", output_path,
        "--size", size,
    ]

    print(f"  Generating: {os.path.basename(output_path)}")
    print(f"  Prompt: {prompt[:120]}...")

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=180,
        )
        if result.returncode == 0 and os.path.exists(output_path):
            file_size = os.path.getsize(output_path)
            print(f"  ✅ Generated: {output_path} ({file_size:,} bytes)")
            return True
        else:
            print(f"  ❌ Failed: {result.stderr[:200] if result.stderr else 'Unknown error'}")
            # Clean up partial file
            if os.path.exists(output_path):
                os.remove(output_path)
            return False
    except subprocess.TimeoutExpired:
        print(f"  ❌ Timeout generating image")
        return False
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


# ── Front matter parsing and updating ──────────────────────────────────

def parse_front_matter(filepath: Path) -> dict:
    """Parse YAML front matter from a markdown file."""
    content = filepath.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return {}

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}

    fm_text = parts[1].strip()
    fm = {}
    for line in fm_text.split("\n"):
        line = line.strip()
        if ":" in line and not line.startswith("-"):
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            fm[key] = value

    fm["_raw"] = fm_text
    fm["_body"] = parts[2]
    return fm


def update_front_matter(filepath: Path, updates: dict) -> bool:
    """Update specific fields in the front matter without rewriting the whole file."""
    content = filepath.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return False

    parts = content.split("---", 2)
    if len(parts) < 3:
        return False

    fm_text = parts[1]

    for key, value in updates.items():
        # Check if the field already exists
        pattern = rf'^{key}:.*$'
        if re.search(pattern, fm_text, re.MULTILINE):
            # Update existing field
            fm_text = re.sub(pattern, f'{key}: "{value}"', fm_text, flags=re.MULTILINE)
        else:
            # Add new field after the last existing field
            fm_text = fm_text.rstrip() + f'\n{key}: "{value}"'

    new_content = f"---\n{fm_text.strip()}\n---{parts[2]}"
    filepath.write_text(new_content, encoding="utf-8")
    return True


def is_pollination_url(value: str) -> bool:
    """Check if a front matter value is a Pollination AI URL (not a local file path)."""
    return value.startswith("http") if value else False


# ── Article scanning ───────────────────────────────────────────────────

def scan_articles(section: str = None, slug: str = None) -> list:
    """Scan articles and return those needing image generation.

    Returns list of dicts: {section, slug, title, excerpt, needs_thumbnail, needs_hero, has_pollination_thumbnail, has_pollination_hero}
    """
    articles = []
    sections = [section] if section else SECTIONS

    for sec in sections:
        sec_dir = CONTENT_DIR / sec
        if not sec_dir.exists():
            continue

        for md_file in sorted(sec_dir.glob("*.md")):
            if md_file.stem == "_index":
                continue

            if slug and md_file.stem != slug:
                continue

            fm = parse_front_matter(md_file)
            if not fm:
                continue

            article_slug = md_file.stem
            title = fm.get("title", article_slug)
            excerpt = fm.get("excerpt", "")

            # Check thumbnail
            thumb_path = ARTICLE_IMAGES / sec / f"{article_slug}.png"
            thumb_fm = fm.get("image", "")
            needs_thumbnail = not thumb_path.exists()
            has_pollination_thumb = is_pollination_url(thumb_fm)
            low_quality_thumb = False
            if thumb_path.exists():
                low_quality_thumb = os.path.getsize(str(thumb_path)) < LOW_QUALITY_THRESHOLD

            # Check hero
            hero_path = HERO_IMAGES / sec / f"{article_slug}.png"
            hero_fm = fm.get("heroImage", "")
            needs_hero = not hero_path.exists()
            has_pollination_hero = is_pollination_url(hero_fm)
            low_quality_hero = False
            if hero_path.exists():
                low_quality_hero = os.path.getsize(str(hero_path)) < LOW_QUALITY_THRESHOLD

            articles.append({
                "section": sec,
                "slug": article_slug,
                "title": title,
                "excerpt": excerpt,
                "filepath": md_file,
                "needs_thumbnail": needs_thumbnail,
                "needs_hero": needs_hero,
                "has_pollination_thumbnail": has_pollination_thumb,
                "has_pollination_hero": has_pollination_hero,
                "low_quality_thumbnail": low_quality_thumb,
                "low_quality_hero": low_quality_hero,
                "thumbnail_path": str(thumb_path),
                "hero_path": str(hero_path),
            })

    return articles


# ── Main logic ─────────────────────────────────────────────────────────

def main():
    # Parse CLI args
    force = "--force" in sys.argv
    low_quality = "--low-quality" in sys.argv
    thumbnails_only = "--thumbnails-only" in sys.argv
    heroes_only = "--heroes-only" in sys.argv
    section = None
    slug = None
    limit = 0  # 0 = no limit

    if "--section" in sys.argv:
        idx = sys.argv.index("--section")
        if idx + 1 < len(sys.argv):
            section = sys.argv[idx + 1]

    if "--slug" in sys.argv:
        idx = sys.argv.index("--slug")
        if idx + 1 < len(sys.argv):
            slug = sys.argv[idx + 1]

    if "--limit" in sys.argv:
        idx = sys.argv.index("--limit")
        if idx + 1 < len(sys.argv):
            limit = int(sys.argv[idx + 1])

    print("=" * 60)
    print("🖼️  Menshly Auto Image Generator")
    print("=" * 60)
    print(f"Force: {force}")
    print(f"Low-quality mode: {low_quality}")
    print(f"Section: {section or 'ALL'}")
    print(f"Slug: {slug or 'ALL'}")
    print(f"Limit: {limit or 'NONE'}")
    print(f"Thumbnails only: {thumbnails_only}")
    print(f"Heroes only: {heroes_only}")
    print()

    # Scan articles
    articles = scan_articles(section, slug)

    if force:
        # Force mode: regenerate ALL images
        targets = articles
        print(f"🔄 Force mode: regenerating images for ALL {len(targets)} articles")
    elif low_quality:
        # Low-quality mode: only articles with small/placeholder images
        targets = [
            a for a in articles
            if a["low_quality_thumbnail"] or a["low_quality_hero"]
            or a["needs_thumbnail"] or a["needs_hero"]
            or a["has_pollination_thumbnail"] or a["has_pollination_hero"]
        ]
        lq_count = sum(1 for a in targets if a["low_quality_thumbnail"] or a["low_quality_hero"])
        print(f"🔍 Low-quality mode: found {lq_count} articles with sub-par images (out of {len(articles)} total)")
    else:
        # Normal mode: only articles missing images or using Pollination URLs
        targets = [
            a for a in articles
            if a["needs_thumbnail"] or a["needs_hero"]
            or a["has_pollination_thumbnail"] or a["has_pollination_hero"]
        ]
        print(f"📋 Found {len(targets)} articles needing image updates (out of {len(articles)} total)")

    if not targets:
        print("✅ All articles have images! Nothing to do.")
        return

    # Apply limit
    if limit > 0 and len(targets) > limit:
        print(f"⏱️ Limiting to {limit} articles this run")
        targets = targets[:limit]

    # Process each article
    success_thumb = 0
    success_hero = 0
    failed = 0
    skipped = 0

    for i, article in enumerate(targets, 1):
        print(f"\n{'─' * 50}")
        print(f"[{i}/{len(targets)}] {article['section']}/{article['slug']}")
        print(f"  Title: {article['title']}")

        # Generate thumbnail
        if not heroes_only:
            if force or article["needs_thumbnail"] or article["has_pollination_thumbnail"] or (low_quality and article["low_quality_thumbnail"]):
                prompt = build_thumbnail_prompt(
                    article["title"],
                    article["section"],
                    article["excerpt"],
                )
                ok = generate_image(prompt, article["thumbnail_path"], "1344x768")
                if ok:
                    success_thumb += 1
                    # Update front matter
                    thumb_hugo_path = f"/images/articles/{article['section']}/{article['slug']}.png"
                    update_front_matter(article["filepath"], {"image": thumb_hugo_path})
                    print(f"  Updated front matter: image → {thumb_hugo_path}")
                else:
                    failed += 1
            else:
                print(f"  ⏭️  Thumbnail already exists, skipping")
                skipped += 1

        # Generate hero
        if not thumbnails_only:
            if force or article["needs_hero"] or article["has_pollination_hero"] or (low_quality and article["low_quality_hero"]):
                prompt = build_hero_prompt(
                    article["title"],
                    article["section"],
                    article["excerpt"],
                )
                ok = generate_image(prompt, article["hero_path"], "1344x768")
                if ok:
                    success_hero += 1
                    # Update front matter
                    hero_hugo_path = f"/images/heroes/{article['section']}/{article['slug']}.png"
                    update_front_matter(article["filepath"], {"heroImage": hero_hugo_path})
                    print(f"  Updated front matter: heroImage → {hero_hugo_path}")
                else:
                    failed += 1
            else:
                print(f"  ⏭️  Hero already exists, skipping")
                skipped += 1

    # Summary
    print(f"\n{'=' * 60}")
    print(f"📊 Summary")
    print(f"  Thumbnails generated: {success_thumb}")
    print(f"  Heroes generated: {success_hero}")
    print(f"  Skipped (already exist): {skipped}")
    print(f"  Failed: {failed}")
    print(f"  Total processed: {len(targets)}")

    # Save report
    report = {
        "timestamp": datetime.utcnow().isoformat(),
        "force_mode": force,
        "total_articles": len(articles),
        "articles_processed": len(targets),
        "thumbnails_generated": success_thumb,
        "heroes_generated": success_hero,
        "skipped": skipped,
        "failed": failed,
    }
    report_path = REPO_ROOT / "data" / "image_generation_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2))
    print(f"  Report saved: {report_path}")

    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
