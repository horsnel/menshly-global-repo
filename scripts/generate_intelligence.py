#!/usr/bin/env python3
"""Generate an Intelligence deep-dive article using AI API.

This generator produces full-length (~3,500-4,500 word) implementation articles
that follow the Menshly Global Intelligence template:
  - SEO title with imperative verbs (like "Train, Serve, and Deploy...")
  - Prerequisites section with specific tools and costs
  - Numbered step-by-step sections with interactive check-ins
  - Interactive "what do you see?" validation checkpoints
  - Complete configurations and settings
  - Error handling and troubleshooting at every step
  - Pricing tables for client delivery
  - Cost breakdown table
  - Production checklist
  - "What to Do Next" section

NEW FEATURES (v2):
  - Links to the most recent Opportunity article via relatedOpportunity frontmatter
  - Links to the corresponding Playbook via relatedPlaybook frontmatter
  - Embeds affiliate links naturally in tool mentions
  - Appends "Recommended Tools" section with affiliate links
  - Uses topic data from last_generated.json for coordinated content
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


def load_last_opportunity() -> dict | None:
    """Load the last generated opportunity article data for cross-linking."""
    if not LAST_GENERATED_FILE.exists():
        return None
    try:
        data = json.loads(LAST_GENERATED_FILE.read_text())
        return data.get("last_opportunity")
    except (json.JSONDecodeError, Exception):
        return None


# ── Master prompt for Intelligence articles ──────────────────────────
SYSTEM_PROMPT = """You are the technical implementation writer for Menshly Global (tagline: "Where AI Meets Revenue").
You write deep execution guides that readers can follow step-by-step to build real systems.

CRITICAL STYLE RULES:
- Write in an INSTRUCTIONAL, CLINICAL tone — like a senior engineer walking a junior through a build
- NOT the casual/conversational Opportunities tone — Intelligence readers are here to EXECUTE
- Every step must be specific: exact button names, exact menu paths, exact settings
- Include INTERACTIVE CHECK-INS throughout: "Do you see [X]? You should see [X] if you're in the right place.
  Go back and check [Y] if you don't see it."
- Show expected output at every step: terminal output, UI screenshots described in text, JSON responses
- Include error scenarios: "If you see [ERROR], this means [CAUSE]. Fix it by [SOLUTION]."
- Name real tools with real prices
- Include complete configurations, not pseudocode — readers should be able to copy-paste
- Never use vague phrases like "configure it appropriately" — say EXACTLY what to configure
- Each numbered step should take 10-30 minutes in real life — break large steps into sub-steps

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

Always mention at least 5-6 of these tools NATURALLY in the article.
Do NOT add a separate "Recommended Tools" section — we add that automatically.

ARTICLE STRUCTURE (follow this EXACTLY):

## Prerequisites
Bullet list of accounts, tools, costs, and time required.
Total upfront cost stated clearly.

## Step 1: [Setup/Configure]
Directory structure, account setup, API keys, initial configuration.
Full terminal commands or UI steps with expected output.
Interactive check-in: "Do you see [X]? If not, [troubleshooting]."

## Step 2: [Build Core Component]
The main implementation. Complete, runnable configurations.
Explain what each part does in 1-2 sentences.
Interactive check-in after each major configuration.

## Step 3: [Test Locally]
How to verify it works. Test commands, expected responses.
Common errors and fixes.
The N-test checklist (5 specific things to verify before proceeding).

## Step 4: [Add Advanced Feature]
Enhancement that makes the system production-worthy (AI enrichment, error handling, routing, etc.)
Interactive check-in after configuration.

## Step 5: [Deploy to Production OR Price and Sell]
Either deployment steps with commands and verification,
OR pricing structure with a table (Starter/Growth/Enterprise tiers)
and the specific sales method with a copy-paste pitch template.

## Step 6: [Scale/Grow]
How to go from 1 to 10+ clients/users.
Hiring plan, automation upgrades, margin improvements.

## Cost Breakdown
Table with columns: Item | Free Tier | Paid Tier | When to Upgrade
Monthly cost analysis at different scales.

## Production Checklist
Checklist of 8-10 items to verify before going live:
- [ ] Item 1
- [ ] Item 2
etc.

## What to Do Next
4-5 specific next steps or expansion ideas.

WORD COUNT TARGET: 3,500-4,500 words. Every step must be fully detailed.
Do NOT write short sections. Every step needs sub-steps, configurations, and check-ins."""


def generate_article(topic_data: dict, opportunity_data: dict = None):
    """Call the AI API to generate the full article.

    Uses a two-pass approach for Groq:
    1. First pass generates the bulk of the article
    2. If too short (< 3000 words), a second pass continues from where it left off
    """
    topic = topic_data.get("intelligence_angle", topic_data.get("selected_title", topic_data.get("topic", "")))
    context = topic_data.get("context", "")
    affiliates = topic_data.get("affiliates", [])
    difficulty = random.choice(["INTERMEDIATE", "ADVANCED"])

    # Build context about the related opportunity article
    opportunity_context = ""
    if opportunity_data:
        opp_title = opportunity_data.get("title", "")
        opp_slug = opportunity_data.get("slug", "")
        opportunity_context = f"""

IMPORTANT CROSS-LINKING CONTEXT:
This intelligence guide is the IMPLEMENTATION companion to the opportunity article:
"{opp_title}" (URL: /opportunities/{opp_slug}/)

The guide should reference this opportunity in the opening paragraph:
"This is the execution guide for building the [TOPIC] business we outlined in our opportunity deep-dive."
And at the end, link back: "Ready to understand the full business opportunity? Read our [opportunity deep-dive]({{< ref "/opportunities/{opp_slug}.md" >}})."
"""

    user_prompt = f"""Write a complete step-by-step implementation article about: {topic}

{'TRENDING CONTEXT: ' + context if context else ''}
Difficulty level: {difficulty}
{opportunity_context}

Follow the exact structure and style defined in your system instructions.
This is for the Intelligence category on Menshly Global — deep implementation guides for builders.

The title must be SEO-optimized using IMPERATIVE VERBS (not "How to"):
Pattern: "[VERB], [VERB], and [VERB] [THING] with [TOOL]"
Example: "Train, Serve, and Deploy a Scikit-learn Model with FastAPI"
Example: "Design, Build, and Deploy Make.com Automation Workflows"

Return the article as pure Markdown (no front matter). Begin with the title as an H1."""

    payload = {
        "model": AI_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        "max_tokens": 16000,
        "temperature": 0.7,
    }
    data = api_call(payload)
    body = data["choices"][0]["message"]["content"]

    finish_reason = data["choices"][0].get("finish_reason", "")
    word_count = len(body.split())
    print(f"  First pass: {word_count} words, finish_reason={finish_reason}")

    if finish_reason == "length" or word_count < 3000:
        print("  Article too short, continuing with second pass...")
        continue_prompt = f"""The previous article was cut off. Here is what was generated so far (last 500 words):

...{body[-2000:]}

CONTINUE the article from where it left off. Do NOT repeat any content. Pick up EXACTLY where it ended.
If you were in the middle of a section, complete it. Then continue with all remaining sections.
Make sure to include: Cost Breakdown, Production Checklist, and What to Do Next.

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
            "temperature": 0.65,
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

    return body, difficulty


import random


def extract_title(body: str) -> str:
    """Extract the H1 title from the markdown body."""
    for line in body.split("\n"):
        line = line.strip()
        if line.startswith("# ") and not line.startswith("## "):
            title = line.lstrip("# ").strip()
            title = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', title)
            return title
    for line in body.split("\n"):
        line = line.strip()
        if line:
            return line.strip("# ").strip()
    return "Untitled Implementation"


def slugify(title: str) -> str:
    """Create a URL-safe slug from the title."""
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    slug = slug.strip("-")
    return slug[:80]


def build_excerpt(body: str) -> str:
    """Build a short excerpt from the article body."""
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
        clean = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', line)
        paragraph += clean + " "
    excerpt = paragraph.strip()[:200]
    if len(paragraph.strip()) > 200:
        excerpt += "..."
    return excerpt.replace('"', "'")


def strip_h1(body: str) -> str:
    """Remove the H1 title line from the body."""
    lines = body.split("\n")
    filtered = []
    skipped_h1 = False
    for line in lines:
        if not skipped_h1 and line.strip().startswith("# ") and not line.strip().startswith("## "):
            skipped_h1 = True
            continue
        filtered.append(line)
    return "\n".join(filtered)


def save_last_generated(topic_data: dict, slug: str, title: str, difficulty: str):
    """Save the last generated intelligence article info for cross-linking."""
    data = {}
    if LAST_GENERATED_FILE.exists():
        try:
            data = json.loads(LAST_GENERATED_FILE.read_text())
        except (json.JSONDecodeError, Exception):
            pass

    data["last_intelligence"] = {
        "slug": slug,
        "title": title,
        "difficulty": difficulty,
        "topic": topic_data.get("topic", ""),
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }

    LAST_GENERATED_FILE.parent.mkdir(parents=True, exist_ok=True)
    LAST_GENERATED_FILE.write_text(json.dumps(data, indent=2))


if __name__ == "__main__":
    if not AI_API_KEY:
        print("ERROR: AI_API_KEY not set")
        exit(1)

    # Step 0: Get trending topic + cross-link data
    print("Loading cross-link data...")
    opportunity_data = load_last_opportunity()

    # If we have a recent opportunity, write the intelligence guide for the same topic
    if opportunity_data:
        topic_data = {
            "topic": opportunity_data.get("topic", ""),
            "intelligence_angle": opportunity_data.get("intelligence_angle", ""),
            "context": opportunity_data.get("context", ""),
            "affiliates": opportunity_data.get("affiliates", []),
        }
        print(f"Writing intelligence guide for same topic as opportunity: {opportunity_data.get('title', '')}")
    else:
        # No recent opportunity — get a fresh trending topic
        print("No recent opportunity found, discovering trending topic...")
        discovery = TrendingTopicDiscovery()
        discovery.ensure_minimum_queue(5)
        topic_data = discovery.get_next_topic("intelligence")

    if not topic_data or not topic_data.get("intelligence_angle") or not topic_data.get("topic"):
        print("ERROR: No topic available")
        exit(1)

    topic = topic_data.get("intelligence_angle", topic_data.get("topic", ""))
    print(f"Generating article about: {topic}")

    # Step 1: Generate images FIRST
    prelim_slug = slugify(topic)

    print("Generating thumbnail image...")
    image_path = generate_article_image(
        topic=topic,
        slug=prelim_slug,
        section="intelligence",
    )
    print(f"Thumbnail saved: {image_path}")

    print("Generating hero image...")
    hero_path = generate_hero_image(
        topic=topic,
        slug=prelim_slug,
        section="intelligence",
    )
    print(f"Hero image saved: {hero_path}")

    # Step 2: Generate article content
    print("Generating article content...")
    body, difficulty = generate_article(topic_data, opportunity_data)
    title = extract_title(body)
    excerpt = build_excerpt(body)
    body_clean = strip_h1(body)

    slug = slugify(title)
    now = datetime.now(timezone.utc)

    # Step 3: Rename images if slug differs
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

    # Build frontmatter with cross-links
    front_matter_lines = [
        "---",
        f'title: "{title}"',
        f'date: {now.strftime("%Y-%m-%d")}',
        'category: "Implementation"',
        f'difficulty: "{difficulty}"',
        'readTime: "25 MIN"',
        f'excerpt: "{excerpt}"',
        f'image: "{image_path}"',
        f'heroImage: "{hero_path}"',
    ]

    # Add cross-link to opportunity article
    if opportunity_data:
        opp_slug = opportunity_data.get("slug", "")
        if opp_slug:
            front_matter_lines.append(f'relatedOpportunity: "/opportunities/{opp_slug}/"')

    front_matter_lines.extend([
        "---",
        "",
    ])

    front_matter = "\n".join(front_matter_lines)

    content_dir = Path("content/intelligence")
    content_dir.mkdir(parents=True, exist_ok=True)
    filepath = content_dir / f"{slug}.md"
    filepath.write_text(front_matter + body_clean)

    # Step 4: Update the opportunity article with a back-link to this intelligence guide
    if opportunity_data:
        opp_slug = opportunity_data.get("slug", "")
        opp_file = Path("content/opportunities") / f"{opp_slug}.md"
        if opp_file.exists():
            try:
                opp_content = opp_file.read_text()
                # Add relatedGuide if not already present
                if "relatedGuide:" not in opp_content:
                    # Insert before the closing ---
                    opp_content = opp_content.replace(
                        "---\n\n",
                        f'relatedGuide: "/intelligence/{slug}/"\n---\n\n',
                        1,
                    )
                    opp_file.write_text(opp_content)
                    print(f"  Updated opportunity article with link to intelligence guide")
            except Exception as e:
                print(f"  Warning: Could not update opportunity article: {e}")

    word_count = len(body_clean.split())
    print(f"Created: {filepath}")
    print(f"Title: {title}")
    print(f"Slug: {slug}")
    print(f"Difficulty: {difficulty}")
    print(f"Word count: ~{word_count}")

    # Step 5: Save data for playbook cross-linking
    save_last_generated(topic_data, slug, title, difficulty)
    print(f"Saved topic data for cross-linking")

    print(f"\n✅ Intelligence article generated successfully!")
    print(f"   Cross-linked to opportunity: {opportunity_data.get('slug', 'N/A') if opportunity_data else 'N/A'}")
    print(f"   Other generators can link to: /intelligence/{slug}/")
