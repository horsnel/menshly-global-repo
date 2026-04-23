#!/usr/bin/env python3
"""Generate an Opportunity deep-dive article using AI API.

This generator produces full-length (~5,000-5,500 word) articles that follow
the exact Menshly Global deep-dive template:
  - SEO-optimized title (How to X in 2026...)
  - Opening hook paragraph
  - Why This Works Right Now
  - The Realistic Picture (4 ugly truths in accent-box shortcodes)
  - The Free Stack (7 zero-cost tools)
  - The Paid Stack (8-10 tools with costs, total monthly)
  - The Workflow (3-4 detailed steps with HACK callouts)
  - Pricing (3 tiers + pricing trick)
  - Getting Clients (3 methods with conversion rates)
  - Tricks and Hacks (5 hacks in accent-box shortcodes)
  - The Real Numbers (month-by-month revenue table)
  - What Nobody Warns You About (4 warnings)
  - Start This Weekend (exact action plan with copy-paste pitch)
"""

import os
import re
import json
import requests
from datetime import datetime, timezone
from pathlib import Path
import random

from image_utils import generate_article_image, generate_hero_image

AI_API_KEY = os.environ.get("AI_API_KEY", "")
AI_API_BASE = os.environ.get("AI_API_BASE", "https://api.openai.com/v1")
AI_MODEL = os.environ.get("AI_MODEL", "gpt-4o")

# ── Trending AI automation opportunity topics ──────────────────────────
TOPICS = [
    "How to start an AI automation agency in 2026",
    "How to make money selling AI agents on marketplaces in 2026",
    "How to build a faceless YouTube channel with AI in 2026",
    "How to start an AI copywriting agency in 2026",
    "How to start an AI SEO agency in 2026",
    "How to build AI SaaS micro-products in 2026",
    "How to start an AI chatbot agency for e-commerce in 2026",
    "How to start a content repurposing agency with AI in 2026",
    "How to start an AI social media management agency in 2026",
    "How to build an AI lead generation system in 2026",
    "How to start a voice AI business in 2026",
    "How to start an AI data analysis service in 2026",
    "How to start an AI newsletter business in 2026",
    "How to start an AI image generation agency in 2026",
    "How to create and sell AI-powered online courses in 2026",
    "How to build a one-person business with GPT-5 in 2026",
    "How to start an AI freelance arbitrage business in 2026",
    "How to build AI-powered email marketing automation in 2026",
    "How to start an AI video editing service in 2026",
    "How to build an AI podcast production agency in 2026",
    "How to start an AI HR and recruitment automation agency in 2026",
    "How to build an AI customer onboarding automation business in 2026",
    "How to start an AI bookkeeping and accounting automation service in 2026",
    "How to build an AI proposal and grant writing agency in 2026",
    "How to start an AI real estate automation agency in 2026",
]

topic = random.choice(TOPICS)

# ── Master prompt that enforces the exact deep-dive structure ─────────
SYSTEM_PROMPT = """You are the lead writer for Menshly Global (tagline: "Where AI Meets Revenue").
You write in a casual, human, straight-talking voice — like a friend who's actually done this stuff
is giving you the real playbook over coffee. No corporate jargon. No AI-sounding filler.
Every sentence must carry weight. No fluff. No "In conclusion" or "It's important to note."

WRITING STYLE RULES:
- Write like you're talking to one person, not an audience
- Use concrete numbers, not vague claims ("$2,500/month" not "good money")
- Name real tools with real prices
- Include tricks and shortcuts people normally gate behind $497 courses
- Be honest about ugly truths — don't sugarcoat
- Use short punchy sentences. Then a longer one that explains the nuance.
- NEVER use phrases like "In today's rapidly evolving landscape" or "As we look to the future"
- NEVER write filler transitions. Jump straight to the next idea.
- Each section must be substantial (minimum 300 words for main sections)

ARTICLE STRUCTURE (follow this EXACTLY):

## Opening Hook
2-3 paragraphs that grab attention with a shocking number, an uncomfortable truth, or a
contrarian take. End with a line like "I'm going to lay out everything: the exact tools,
the tricks nobody shares, the ugly truths, and the realistic numbers."

## Why This Works Right Now
3 reasons this opportunity exists RIGHT NOW (not last year, not next year — now).
Each reason gets a full paragraph with evidence.

## The Realistic Picture (Before You Get Excited)
4 ugly truths wrapped in accent-box shortcodes:
{{% accent-box %}}
**Truth #1:** [harsh reality with specific numbers]
{{% /accent-box %}}
(Repeat for truths 2-4)

## The Free Stack: Starting With Zero Dollars
7 free tools, each as: **Tool Name — $0** — One-line description.
End with a paragraph explaining limitations and when to upgrade.
Include one HACK callout in an accent-box.

## The Paid Stack: When You're Ready to Scale
8-10 paid tools, each as: **Tool Name — $X/mo** — One-line description.
End with total monthly cost and ROI analysis.
Include one HACK callout in an accent-box.

## The Workflow: Step-by-Step With Every Shortcut
3-4 detailed steps (### Step N: Name (time estimate))
Each step has 2-3 paragraphs of detail + HACK callout in accent-box.
Include specific prompts, settings, or configurations where relevant.

## Pricing: What to Charge and How to Defend It
3 pricing tiers (Starter/Growth/Enterprise) with specific dollar amounts and what's included.
One Pricing Trick HACK in accent-box.

## Getting Clients: The Real Playbook
3 methods with names and conversion rates (### Method N: Name (Conversion Rate: X%))
Each method gets a full paragraph with specific tactics.
End with one Referral HACK in accent-box.

## Tricks and Hacks They Don't Share in Courses
5 hacks, each in accent-box:
{{% accent-box %}}
**HACK 1: Name.** Detailed explanation of the trick.
{{% /accent-box %}}

## The Real Numbers
A month-by-month revenue table:
| Month | Revenue | Clients/Users | Notes |
|-------|---------|---------------|-------|
8-10 rows from Month 1 ($0) through Month 12 ($15K-$50K+).
Then a paragraph on unit economics.

## What Nobody Warns You About
4 honest warnings, each as a bold-titled paragraph.

## Start This Weekend (Literally)
Exact weekend action plan:
**Saturday morning:** specific task
**Saturday afternoon:** specific task
**Sunday:** specific task with copy-paste pitch template

WORD COUNT TARGET: 5,000-5,500 words. Do NOT cut sections short.
Every section must be fully developed with real substance."""

USER_PROMPT = f"""Write a complete deep-dive article about: {topic}

Follow the exact structure and style defined in your system instructions.
This is for the Opportunities category on Menshly Global.
Target audience: entrepreneurs, freelancers, and builders who want to make money with AI.

The title must be SEO-optimized following this pattern:
"How to [VERB] [TOPIC] in 2026 ([BENEFIT/REVENUE HOOK])"

Return the article as pure Markdown (no front matter). Begin with the title as an H1."""


def generate_article():
    """Call the AI API to generate the full article."""
    headers = {
        "Authorization": f"Bearer {AI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": AI_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT},
        ],
        "max_tokens": 8000,
        "temperature": 0.75,
    }
    resp = requests.post(
        f"{AI_API_BASE}/chat/completions",
        headers=headers,
        json=payload,
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]


def extract_title(body: str) -> str:
    """Extract the H1 title from the markdown body."""
    for line in body.split("\n"):
        line = line.strip()
        if line.startswith("# ") and not line.startswith("## "):
            return line.lstrip("# ").strip()
    # Fallback: first non-empty line
    for line in body.split("\n"):
        line = line.strip()
        if line:
            return line.strip("# ").strip()
    return "Untitled Opportunity"


def slugify(title: str) -> str:
    """Create a URL-safe slug from the title."""
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    slug = slug.strip("-")
    return slug[:80]


def build_excerpt(body: str) -> str:
    """Build a short excerpt from the article body (first meaningful paragraph)."""
    # Skip the title line and find first real paragraph
    lines = body.split("\n")
    paragraph = ""
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            continue
        if not line:
            if paragraph:
                break
            continue
        paragraph += line + " "
    excerpt = paragraph.strip()[:200]
    if len(paragraph.strip()) > 200:
        excerpt += "..."
    return excerpt.replace('"', "'")


def strip_h1(body: str) -> str:
    """Remove the H1 title line from the body (it goes into frontmatter)."""
    lines = body.split("\n")
    filtered = []
    skipped_h1 = False
    for line in lines:
        if not skipped_h1 and line.strip().startswith("# ") and not line.strip().startswith("## "):
            skipped_h1 = True
            continue
        filtered.append(line)
    return "\n".join(filtered)


if __name__ == "__main__":
    if not AI_API_KEY:
        print("ERROR: AI_API_KEY not set")
        exit(1)

    print(f"Generating article about: {topic}")
    body = generate_article()
    title = extract_title(body)
    excerpt = build_excerpt(body)
    body_clean = strip_h1(body)

    slug = slugify(title)
    now = datetime.now(timezone.utc)

    # Generate article thumbnail via Pollination AI
    image_path = generate_article_image(
        topic=topic,
        slug=slug,
        section="opportunities",
    )

    # Generate premium hero/OG image via Pollination AI
    hero_path = generate_hero_image(
        topic=topic,
        slug=slug,
        section="opportunities",
    )

    front_matter = f"""---
title: "{title}"
date: {now.strftime("%Y-%m-%d")}
category: "AI Opportunity"
readTime: "16 MIN"
excerpt: "{excerpt}"
image: "{image_path}"
heroImage: "{hero_path}"
---

"""

    content_dir = Path("content/opportunities")
    content_dir.mkdir(parents=True, exist_ok=True)
    filepath = content_dir / f"{slug}.md"
    filepath.write_text(front_matter + body_clean)

    word_count = len(body_clean.split())
    print(f"Created: {filepath}")
    print(f"Title: {title}")
    print(f"Slug: {slug}")
    print(f"Word count: ~{word_count}")
