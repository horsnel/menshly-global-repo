#!/usr/bin/env python3
"""Generate an Opportunity deep-dive article using AI API.

This generator produces full-length (~5,000-5,500 word) articles that follow
the exact Menshly Global deep-dive template:
  - SEO-optimized title (How to Build an AI [Service] ($X-Y/Month))
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

v3 REWRITE — Section-by-section generation:
  - Generates each major section as a SEPARATE API call
  - Works reliably even on weak models (Pollinations, small LLMs)
  - Enforces minimum word count per section
  - Quality checks with retry on short sections
  - Cross-links to intelligence and playbook articles
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

# ── Section definitions ──
SECTION_DEFS = [
    {
        "heading": "Opening Hook",
        "instructions": """Write the OPENING HOOK (2-3 paragraphs).
Grab attention with a shocking number, an uncomfortable truth, or a contrarian take.
End with a line like "I'm going to lay out everything: the exact tools, the tricks nobody shares, the ugly truths, and the realistic numbers."
Write 200-300 words.""",
        "min_words": 150,
        "include_heading": False,
    },
    {
        "heading": "Why This Works Right Now",
        "instructions": """Write the "Why This Works Right Now" section.
3 reasons this opportunity exists RIGHT NOW. Each reason gets a full paragraph with evidence.
Write 300-400 words.""",
        "min_words": 200,
    },
    {
        "heading": "The Realistic Picture (Before You Get Excited)",
        "instructions": """Write the "The Realistic Picture" section with 4 ugly truths in accent-box shortcodes:
{{% accent-box %}}
**Truth #1:** [harsh reality with specific numbers]
{{% /accent-box %}}
(Repeat for truths 2-4)
Write 300-400 words total.""",
        "min_words": 200,
    },
    {
        "heading": "The Free Stack: Starting With Zero Dollars",
        "instructions": """Write the "The Free Stack" section.
List 7 free tools, each as: **Tool Name — $0** — One-line description.
End with a paragraph explaining limitations and when to upgrade.
Include one HACK callout in an accent-box shortcode.
Write 300-400 words.""",
        "min_words": 200,
    },
    {
        "heading": "The Paid Stack: When You're Ready to Scale",
        "instructions": """Write the "The Paid Stack" section.
List 8-10 paid tools, each as: **Tool Name — $X/mo** — One-line description.
End with total monthly cost and ROI analysis.
Include one HACK callout in an accent-box shortcode.
Write 300-400 words.""",
        "min_words": 200,
    },
    {
        "heading": "The Workflow: Step-by-Step With Every Shortcut",
        "instructions": """Write the "The Workflow" section with 3-4 detailed steps.
Each step: ### Step N: Name (time estimate) — 2-3 paragraphs of detail + HACK callout in accent-box.
Include specific prompts, settings, or configurations.
Write 500-700 words total.""",
        "min_words": 350,
    },
    {
        "heading": "Pricing: What to Charge and How to Defend It",
        "instructions": """Write the "Pricing" section.
3 pricing tiers (Starter/Growth/Enterprise) with specific dollar amounts and what's included.
One Pricing Trick HACK in accent-box shortcode.
Write 250-350 words.""",
        "min_words": 150,
    },
    {
        "heading": "Getting Clients: The Real Playbook",
        "instructions": """Write the "Getting Clients" section.
3 methods with names and conversion rates (### Method N: Name (Conversion Rate: X%)).
Each method gets a full paragraph with specific tactics.
End with one Referral HACK in accent-box shortcode.
Write 350-450 words.""",
        "min_words": 200,
    },
    {
        "heading": "Tricks and Hacks They Don't Share in Courses",
        "instructions": """Write the "Tricks and Hacks" section with 5 hacks, each in accent-box:
{{% accent-box %}}
**HACK 1: Name.** Detailed explanation of the trick.
{{% /accent-box %}}
Write 400-500 words total.""",
        "min_words": 250,
    },
    {
        "heading": "The Real Numbers",
        "instructions": """Write the "The Real Numbers" section.
Include a month-by-month revenue TABLE:
| Month | Revenue | Clients/Users | Notes |
|-------|---------|---------------|-------|
8-10 rows from Month 1 ($0) through Month 12 ($15K-$50K+).
Then a paragraph on unit economics.
Write 250-350 words.""",
        "min_words": 150,
    },
    {
        "heading": "What Nobody Warns You About",
        "instructions": """Write the "What Nobody Warns You About" section.
4 honest warnings, each as a bold-titled paragraph with specific details.
Write 250-350 words.""",
        "min_words": 150,
    },
    {
        "heading": "Start This Weekend (Literally)",
        "instructions": """Write the "Start This Weekend" section with an exact weekend action plan:
**Saturday morning:** specific task
**Saturday afternoon:** specific task
**Sunday:** specific task with copy-paste pitch template
Write 250-350 words.""",
        "min_words": 150,
    },
]

# ── System prompt shared across all section calls ──
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
- Each section must be substantial (minimum 200 words for main sections)

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
Just weave the tool names into the Free Stack, Paid Stack, and Workflow sections."""


def _call_api(messages: list, max_tokens: int = 4000, temperature: float = 0.75) -> str:
    """Make a single API call and return the content text."""
    payload = {
        "model": AI_MODEL,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    data = api_call(payload)
    return data["choices"][0]["message"]["content"]


def generate_article(topic_data: dict):
    """Generate the full article using section-by-section approach.

    Each section is a separate API call, ensuring consistent quality
    regardless of the AI backend being used.
    """
    topic = topic_data.get("selected_title", topic_data.get("opportunity_angle", topic_data.get("topic", "")))
    context = topic_data.get("context", "")
    affiliates = topic_data.get("affiliates", [])

    print(f"Generating article about: {topic}")
    print(f"Strategy: Section-by-section generation ({len(SECTION_DEFS)} sections)")

    # Generate the title first
    title_prompt = f"""Generate an SEO-optimized title for an article about: {topic}

The title MUST follow this exact pattern:
"How to Build an AI [SERVICE] ($X-$Y/Month)"

RULES:
- Always start with "How to Build an AI"
- Drop the year — do NOT include "in 2026" or any year
- Always include a revenue range in parentheses like ($X-$Y/Month)
- Use a hyphen in the revenue range: $3K-$20K (not $3K-$20K/Month → use /Month at the end)
- Keep the service name concise — remove unnecessary words

Examples:
- "How to Build an AI SEO Agency ($5K-$30K/Month)"
- "How to Build an AI Content Repurposing Agency ($3K-$15K/Month)"
- "How to Build an AI Translation and Localization Service ($3K-$20K/Month)"

Return ONLY the title, nothing else."""

    title_messages = [
        {"role": "system", "content": "You are an SEO title generator. Return only the title."},
        {"role": "user", "content": title_prompt},
    ]

    for attempt in range(3):
        try:
            title_text = _call_api(title_messages, max_tokens=100, temperature=0.8)
            title_text = title_text.strip().strip('"').strip("'")
            if len(title_text) > 20:
                break
        except Exception as e:
            print(f"  Title generation attempt {attempt+1} failed: {str(e)[:100]}")
            time.sleep(3)
    else:
        title_text = f"How to Build an {topic} ($5K-$25K/Month)"

    print(f"  Title: {title_text}")

    # Generate each section
    sections = []
    total_sections = len(SECTION_DEFS)

    for i, section_def in enumerate(SECTION_DEFS):
        heading = section_def["heading"]
        instructions = section_def["instructions"]
        min_words = section_def["min_words"]
        include_heading = section_def.get("include_heading", True)

        print(f"\n  [{i+1}/{total_sections}] Generating: {heading}...")

        # Build context from previously generated sections
        prev_context = ""
        if sections:
            prev_summaries = []
            for s in sections:
                first_line = s.split("\n")[0][:100]
                prev_summaries.append(first_line)
            prev_context = f"Previously written sections: {', '.join(prev_summaries)}"

        section_prompt = f"""Write the following section for an article about: {topic}

TITLE: {title_text}

{'TRENDING CONTEXT: ' + context if context else ''}

SECTION TO WRITE: {heading}

{instructions}

{prev_context if prev_context else ''}

WORD COUNT TARGET: At least {min_words} words for this section.
Be specific with real numbers, real tool names, and real prices."""

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": section_prompt},
        ]

        section_result = None
        for attempt in range(2):  # Reduced from 3 to 2 retries to prevent workflow timeouts
            try:
                result = _call_api(messages, max_tokens=3000, temperature=0.75)
                word_count = len(result.split())

                if word_count >= min_words * 0.6:
                    if word_count < min_words:
                        print(f"    {heading}: {word_count} words (target {min_words}, accepted)")
                    else:
                        print(f"    {heading}: {word_count} words ✓")

                    # Add the heading if needed
                    if include_heading and not result.strip().startswith("## "):
                        result = f"## {heading}\n\n{result}"

                    sections.append(result)
                    section_result = result
                    break
                else:
                    print(f"    {heading} attempt {attempt+1}: too short ({word_count} words), retrying...")
                    section_result = result
                    time.sleep(2)  # Reduced from 3s
            except Exception as e:
                print(f"    {heading} attempt {attempt+1} failed: {str(e)[:100]}")
                time.sleep(3)  # Reduced from 5s
        else:
            # Use whatever we got — partial content is better than nothing
            if section_result:
                print(f"    {heading}: using best available after retries")
                if include_heading and not section_result.strip().startswith("## "):
                    section_result = f"## {heading}\n\n{section_result}"
                sections.append(section_result)
            else:
                # Generate a placeholder section so the article still works
                print(f"    {heading}: generating placeholder (API exhausted)")
                placeholder = f"## {heading}\n\nDetails coming soon. Check back for updates on this section."
                sections.append(placeholder)

    # Assemble the full article
    body = f"# {title_text}\n\n" + "\n\n".join(sections)

    final_words = len(body.split())
    placeholder_count = sum(1 for s in sections if "Details coming soon" in s)
    print(f"\n  Total article: {final_words} words")
    if placeholder_count:
        print(f"  WARNING: {placeholder_count} section(s) used placeholders (API issues)")

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
        print("No AI_API_KEY set — will use Pollinations (free) as fallback")

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

    # Step 1: Generate images FIRST (non-fatal — continue without if failed)
    prelim_slug = slugify(topic)

    image_path = f"/images/articles/opportunities/{prelim_slug}.png"
    hero_path = f"/images/heroes/opportunities/{prelim_slug}.png"

    try:
        print("Generating thumbnail image...")
        image_path = generate_article_image(
            topic=topic,
            slug=prelim_slug,
            section="opportunities",
        )
        print(f"Thumbnail saved: {image_path}")
    except Exception as e:
        print(f"  Thumbnail generation failed (non-fatal): {e}")

    try:
        print("Generating hero image...")
        hero_path = generate_hero_image(
            topic=topic,
            slug=prelim_slug,
            section="opportunities",
        )
        print(f"Hero image saved: {hero_path}")
    except Exception as e:
        print(f"  Hero image generation failed (non-fatal): {e}")

    # Step 2: Generate article content (section-by-section)
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

    if word_count < 3500:
        print("  WARNING: Total word count below 3500.")

    # Step 4: Save topic data for cross-linking
    save_last_generated(topic_data, slug, title)
    print(f"Saved topic data for cross-linking")

    # Step 5: Mark topic as used
    discovery.mark_topic_used(topic_data)

    print(f"\n✅ Opportunity article generated successfully!")
    print(f"   Other generators can now link to: /opportunities/{slug}/")
