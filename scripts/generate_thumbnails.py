#!/usr/bin/env python3
"""
Pollination AI Thumbnail Generator for Menshly Global
Generates AI thumbnails for articles that don't have hero images.
Usage: python3 scripts/generate_thumbnails.py [--slug <slug>] [--all]
"""

import os
import sys
import json
import time
import hashlib
import urllib.request
import urllib.parse
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
CONTENT_DIR = REPO_ROOT / "content"
HERO_DIR = REPO_ROOT / "static" / "images" / "heroes"
ARTICLE_DIR = REPO_ROOT / "static" / "images" / "articles"

# Topic-to-prompt mapping for better thumbnails
TOPIC_PROMPTS = {
    "ai": "futuristic AI neural network with glowing nodes and data streams, dark background, technology",
    "automation": "robotic arms assembling digital widgets on a production line, blue and yellow accents",
    "agency": "modern office with multiple screens showing analytics and workflows, professional",
    "copywriting": "keyboard with AI-generated text floating above it, creative writing",
    "seo": "search engine results page with ranking indicators and analytics charts",
    "voice": "sound waves and voice visualization with AI microphone and digital processing",
    "social media": "social media apps floating with engagement metrics and content calendar",
    "email": "email inbox with AI-generated subject lines, envelope icons, deliverability",
    "newsletter": "digital newsletter layout with subscriber growth chart and content preview",
    "saas": "cloud-based SaaS dashboard interface with metrics, user growth, revenue",
    "ecommerce": "online store with AI product recommendations and shopping cart",
    "video": "video editing timeline with AI-generated clips and thumbnails",
    "data": "data visualization dashboard with AI analytics and insights",
    "lead generation": "funnel diagram with AI-powered lead scoring and CRM integration",
    "course": "online learning platform with AI course creation and student progress",
    "chatbot": "chat interface with AI bot responding to customer queries",
    "image": "AI image generation interface with creative outputs and prompts",
    "prompt": "AI prompt engineering workspace with token counting and model selection",
    "side hustle": "person working on laptop with multiple income stream indicators",
    "faceless youtube": "faceless YouTube channel setup with AI video creation tools",
    "replit": "code editor with AI-assisted development and deployment pipeline",
    "default": "AI technology business concept with digital transformation and growth indicators"
}

def get_prompt_for_topic(title, section="opportunities"):
    """Generate a Pollination AI prompt from article title and section."""
    title_lower = title.lower()

    # Find best matching topic keyword
    best_match = "default"
    best_len = 0
    for keyword, prompt in TOPIC_PROMPTS.items():
        if keyword in title_lower and len(keyword) > best_len:
            best_match = keyword
            best_len = len(keyword)

    base_prompt = TOPIC_PROMPTS[best_match]

    # Section-specific enhancement
    section_enhancements = {
        "opportunities": "business opportunity discovery, revenue potential, market analysis",
        "intelligence": "implementation guide, step-by-step workflow, technical setup",
        "playbooks": "premium playbook system, procedures, checklists, scaling framework"
    }
    enhancement = section_enhancements.get(section, "")

    # Combine into final prompt
    full_prompt = f"{base_prompt}, {enhancement}, menshly global brand colors yellow and black, brutalist design, professional"
    return full_prompt


def generate_pollination_url(prompt, width=1200, height=630, seed=""):
    """Build a Pollination AI image URL."""
    encoded = urllib.parse.quote(prompt.lower())
    return f"https://image.pollinations.ai/prompt/{encoded}?width={width}&height={height}&nologo=true&seed={seed}"


def generate_thumbnail_url(prompt, width=672, height=384, seed=""):
    """Build a Pollination AI thumbnail URL."""
    encoded = urllib.parse.quote(prompt.lower())
    return f"https://image.pollinations.ai/prompt/{encoded}?width={width}&height={height}&nologo=true&seed={seed}"


def process_article(front_matter_path, force=False):
    """Process a single article and add Pollination thumbnail if missing."""
    with open(front_matter_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse front matter
    if not content.startswith('---'):
        return False

    parts = content.split('---', 2)
    if len(parts) < 3:
        return False

    fm_text = parts[1].strip()
    body = parts[2]

    # Check if already has image
    has_image = 'image:' in fm_text or 'heroImage:' in fm_text
    if has_image and not force:
        return False

    # Extract title
    title = ""
    for line in fm_text.split('\n'):
        if line.startswith('title:'):
            title = line.split(':', 1)[1].strip().strip('"').strip("'")
            break

    if not title:
        return False

    # Determine section
    rel_path = front_matter_path.relative_to(CONTENT_DIR)
    section = rel_path.parts[0] if rel_path.parts else "opportunities"

    # Generate URLs
    slug = front_matter_path.stem
    if slug == "_index":
        return False

    prompt = get_prompt_for_topic(title, section)
    hero_url = generate_pollination_url(prompt, seed=slug)
    thumbnail_url = generate_thumbnail_url(prompt, seed=slug)

    # Add image and heroImage to front matter
    new_fm_lines = []
    for line in fm_text.split('\n'):
        new_fm_lines.append(line)

    # Add image fields
    if 'image:' not in new_fm_lines:
        new_fm_lines.append(f'image: "{thumbnail_url}"')
    if 'heroImage:' not in new_fm_lines:
        new_fm_lines.append(f'heroImage: "{hero_url}"')

    new_fm = '\n'.join(new_fm_lines)
    new_content = f'---\n{new_fm}\n---{body}'

    with open(front_matter_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  Added Pollination thumbnail: {slug}")
    return True


def process_all_articles():
    """Process all articles in the content directory."""
    count = 0
    for section in ["opportunities", "intelligence", "playbooks"]:
        section_dir = CONTENT_DIR / section
        if not section_dir.exists():
            continue
        for md_file in section_dir.glob("*.md"):
            if md_file.stem == "_index":
                continue
            print(f"Processing: {md_file.relative_to(REPO_ROOT)}")
            if process_article(md_file):
                count += 1
    return count


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate_thumbnails.py [--all] [--slug <slug>]")
        sys.exit(1)

    if "--all" in sys.argv:
        count = process_all_articles()
        print(f"\nDone! Added thumbnails to {count} articles.")
    elif "--slug" in sys.argv:
        idx = sys.argv.index("--slug")
        if idx + 1 >= len(sys.argv):
            print("Error: --slug requires a value")
            sys.exit(1)
        slug = sys.argv[idx + 1]
        # Find the article
        for section in ["opportunities", "intelligence", "playbooks"]:
            md_file = CONTENT_DIR / section / f"{slug}.md"
            if md_file.exists():
                process_article(md_file, force=True)
                print(f"Done! Processed {slug}")
                return
        print(f"Error: Article not found: {slug}")
    else:
        print("Usage: python3 generate_thumbnails.py [--all] [--slug <slug>]")


if __name__ == "__main__":
    main()
