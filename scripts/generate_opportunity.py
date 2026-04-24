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
  - What Nobody Warns You About
  - Start This Weekend (exact action plan with copy-paste pitch)

NEW FEATURES (v2):
  - Uses TrendingTopicDiscovery for topic selection (no more random from hardcoded list)
  - Embeds affiliate links naturally in tool mentions
  - Appends "Recommended Tools" section with affiliate links
  - Outputs topic metadata for cross-linking with Intelligence/Playbook generators
  - Saves topic data to data/last_generated.json for other generators to pick up
"""

import os
import re
import json
import time
import requests
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

# Auto-load .env from project root
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

from image_utils import generate_article_image, generate_hero_image
from trending_topics import TrendingTopicDiscovery
from affiliate_injector import inject_affiliate_links, generate_tools_section
from ai_utils import api_call

AI_API_KEY = os.environ.get("AI_API_KEY", "")
AI_API_BASE = os.environ.get("AI_API_BASE", "https://api.groq.com/openai/v1")
AI_API_MODEL = os.environ.get("AI_MODEL", "llama-3.3-70b-versatile")
AI_MODEL = AI_API_MODEL

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LAST_GENERATED_FILE = PROJECT_ROOT / "data" / "last_generated.json"


# ── Master prompt that enforces the exact deep-dive structure ─────────
SYSTEM_PROMPT = """You are the lead writer for Menshly Global (tagline: "Where AI Meets Revenue").
You write in a casual, human, straight-talking voice — like a friend who's actually done this stuff
is giving you the real playbook over coffee. No corporate jargon. No AI-sounding filler.
Every sentence must carry weight. No fluff. No "In conclusion" or "It's important to note."

WRITING STYLE RULES:
- Write like you're talking to one person, not an audience
- Use concrete numbers, not vague claims ("$2,500/month" not "good money")
- Name real tools with real prices — be specific about which tools to use
- Include tricks and shortcuts people normally gate behind $497 courses
- Be honest about ugly truths — don't sugarcoat
- Use short punchy sentences. Then a longer one that explains the nuance.
- NEVER use phrases like "In today's rapidly evolving landscape" or "As we look to the future"
- NEVER write filler transitions. Jump straight to the next idea.
- Each section must be substantial (minimum 300 words for main sections)

AFFILIATE TOOL INTEGRATION RULES:
When mentioning tools, use these EXACT tool names (these are our affiliate partners):
- Make.com (automation platform)
- Replit (cloud IDE for AI SaaS)
- Vapi (AI voice agents)
- Fliki AI (AI text-to-video)
- Canva (design platform)
- ChatGPT (AI assistant)
- ElevenLabs (AI voice synthesis)
- Klaviyo (email marketing)
- ActiveCampaign (CRM + email)
- Semrush (SEO toolkit)
- Hostinger (web hosting)
- Shopify (e-commerce)
- Zapier (app automation)
- Apollo.io (B2B sales intelligence)
- PhantomBuster (LinkedIn automation)
- Buffer (social media scheduling)
- Loom (video messaging)
- Calendly (scheduling)
- Beehiiv (newsletter platform)
- Notion (workspace)
- Midjourney (AI image generation)
- Grammarly (AI writing assistant)

IMPORTANT: Always mention at least 5-6 of these tools NATURALLY in the article.
Do NOT add a separate "Recommended Tools" section — we add that automatically.
Just weave the tool names into the Free Stack, Paid Stack, and Workflow sections.

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


def generate_article(topic_data: dict):
    """Call the AI API to generate the full article.

    Uses a two-pass approach for Groq:
    1. First pass generates the bulk of the article
    2. If too short (< 4000 words), a second pass continues from where it left off
    """
    topic = topic_data.get("selected_title", topic_data.get("opportunity_angle", topic_data.get("topic", "")))
    context = topic_data.get("context", "")
    affiliates = topic_data.get("affiliates", [])

    user_prompt = f"""Write a complete deep-dive article about: {topic}

{'TRENDING CONTEXT: ' + context if context else ''}

Follow the exact structure and style defined in your system instructions.
This is for the Opportunities category on Menshly Global.
Target audience: entrepreneurs, freelancers, and builders who want to make money with AI.

The title must be SEO-optimized following this pattern:
"How to [VERB] [TOPIC] in 2026 ([BENEFIT/REVENUE HOOK])"

Return the article as pure Markdown (no front matter). Begin with the title as an H1."""

    payload = {
        "model": AI_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        "max_tokens": 16000,
        "temperature": 0.75,
    }
    data = api_call(payload)
    body = data["choices"][0]["message"]["content"]

    finish_reason = data["choices"][0].get("finish_reason", "")
    word_count = len(body.split())
    print(f"  First pass: {word_count} words, finish_reason={finish_reason}")

    if finish_reason == "length" or word_count < 4000:
        print("  Article too short, continuing with second pass...")
        continue_prompt = f"""The previous article was cut off. Here is what was generated so far (last 500 words):

...{body[-2000:]}

CONTINUE the article from where it left off. Do NOT repeat any content. Pick up EXACTLY where it ended.
If you were in the middle of a section, complete it. Then continue with all remaining sections.
Make sure to include: Tricks and Hacks, The Real Numbers (month-by-month table), What Nobody Warns You About, and Start This Weekend.

WORD COUNT TARGET: Write at least 2000 more words."""

        payload2 = {
            "model": AI_MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
                {"role": "assistant", "content": body},
                {"role": "user", "content": continue_prompt},
            ],
            "max_tokens": 16000,
            "temperature": 0.7,
        }
        data2 = api_call(payload2)
        continuation = data2["choices"][0]["message"]["content"]
        cont_words = len(continuation.split())
        print(f"  Second pass: {cont_words} words added")
        body = body + "\n\n" + continuation

    final_words = len(body.split())
    print(f"  Total: {final_words} words")

    # Inject affiliate links into tool mentions
    body = inject_affiliate_links(body, affiliates)

    # Append Recommended Tools section
    tools_section = generate_tools_section(affiliates)
    if tools_section:
        body = body + "\n\n" + tools_section

    return body


def extract_title(body: str) -> str:
    """Extract the H1 title from the markdown body."""
    for line in body.split("\n"):
        line = line.strip()
        if line.startswith("# ") and not line.startswith("## "):
            # Strip any markdown links from title
            title = line.lstrip("# ").strip()
            title = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', title)
            return title
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
    lines = body.split("\n")
    paragraph = ""
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            continue
        if line.startswith("## "):
            if paragraph:
                break
            continue
        if not line:
            if paragraph:
                break
            continue
        # Strip markdown links for clean excerpt
        clean = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', line)
        paragraph += clean + " "
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


def save_last_generated(topic_data: dict, slug: str, title: str):
    """Save the last generated article info for cross-linking by other generators."""
    data = {}
    if LAST_GENERATED_FILE.exists():
        try:
            data = json.loads(LAST_GENERATED_FILE.read_text())
        except (json.JSONDecodeError, Exception):
            pass

    data["last_opportunity"] = {
        "slug": slug,
        "title": title,
        "topic": topic_data.get("topic", ""),
        "context": topic_data.get("context", ""),
        "affiliates": topic_data.get("affiliates", []),
        "opportunity_angle": topic_data.get("opportunity_angle", ""),
        "intelligence_angle": topic_data.get("intelligence_angle", ""),
        "playbook_angle": topic_data.get("playbook_angle", ""),
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }

    LAST_GENERATED_FILE.parent.mkdir(parents=True, exist_ok=True)
    LAST_GENERATED_FILE.write_text(json.dumps(data, indent=2))


if __name__ == "__main__":
    if not AI_API_KEY:
        print("ERROR: AI_API_KEY not set")
        exit(1)

    # Step 0: Get trending topic
    print("Discovering trending topic...")
    discovery = TrendingTopicDiscovery()
    discovery.ensure_minimum_queue(5)
    topic_data = discovery.get_next_topic("opportunity")

    if not topic_data:
        print("ERROR: No trending topics available")
        exit(1)

    topic = topic_data.get("selected_title", topic_data.get("topic", ""))
    print(f"Generating article about: {topic}")
    print(f"Context: {topic_data.get('context', 'N/A')}")
    print(f"Affiliates: {', '.join(topic_data.get('affiliates', []))}")

    # Step 1: Generate images FIRST (before article content)
    prelim_slug = slugify(topic)

    print("Generating thumbnail image...")
    image_path = generate_article_image(
        topic=topic,
        slug=prelim_slug,
        section="opportunities",
    )
    print(f"Thumbnail saved: {image_path}")

    print("Generating hero image...")
    hero_path = generate_hero_image(
        topic=topic,
        slug=prelim_slug,
        section="opportunities",
    )
    print(f"Hero image saved: {hero_path}")

    # Step 2: Generate article content
    print("Generating article content...")
    body = generate_article(topic_data)
    title = extract_title(body)
    excerpt = build_excerpt(body)
    body_clean = strip_h1(body)

    slug = slugify(title)
    now = datetime.now(timezone.utc)

    # Step 3: Rename images if slug differs from preliminary slug
    if slug != prelim_slug:
        old_thumb = image_path
        old_hero = hero_path
        new_thumb = image_path.replace(prelim_slug, slug)
        new_hero = hero_path.replace(prelim_slug, slug)
        if os.path.exists(old_thumb):
            os.rename(old_thumb, new_thumb)
            image_path = new_thumb
            print(f"Renamed thumbnail: {new_thumb}")
        if os.path.exists(old_hero):
            os.rename(old_hero, new_hero)
            hero_path = new_hero
            print(f"Renamed hero: {new_hero}")

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

    # Step 4: Save topic data for cross-linking
    save_last_generated(topic_data, slug, title)
    print(f"Saved topic data for cross-linking")

    # Step 5: Mark topic as used
    discovery.mark_topic_used(topic_data)

    print(f"\n✅ Opportunity article generated successfully!")
    print(f"   Other generators can now link to: /opportunities/{slug}/")
