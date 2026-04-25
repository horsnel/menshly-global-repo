#!/usr/bin/env python3
"""Generate a premium Playbook article using AI API.

This generator produces full-length (~8,000-10,000 word) premium playbooks
that follow the Menshly Global Playbook template:
  - Multiple MODULES (8-12), each with an Overview
  - Numbered PROCEDURES within each module
  - Interactive check-ins at every stage
  - Appendices (Tool Reference, SOP Index, Revenue Calculator)

NEW FEATURES (v2):
  - Links to the most recent Opportunity AND Intelligence articles
  - Embeds affiliate links naturally in tool mentions
  - Appends affiliate tool reference section
  - Uses topic data from last_generated.json for coordinated content
  - Cross-links added to both opportunity and intelligence articles
"""

import os
import re
import json
import time
import requests
from datetime import datetime, timezone
from pathlib import Path
import random
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

# Optional: Override model for playbooks
PLAYBOOK_API_KEY = os.environ.get("PLAYBOOK_API_KEY", AI_API_KEY)
PLAYBOOK_API_BASE = os.environ.get("PLAYBOOK_API_BASE", AI_API_BASE)
PLAYBOOK_MODEL = os.environ.get("PLAYBOOK_MODEL", AI_MODEL)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LAST_GENERATED_FILE = PROJECT_ROOT / "data" / "last_generated.json"


def load_last_generated() -> dict:
    """Load the last generated article data for cross-linking."""
    if not LAST_GENERATED_FILE.exists():
        return {}
    try:
        return json.loads(LAST_GENERATED_FILE.read_text())
    except (json.JSONDecodeError, Exception):
        return {}


# ── Master prompt for Playbook generation ────────────────────────────
SYSTEM_PROMPT = """You are the senior implementation writer for Menshly Global (tagline: "Where AI Meets Revenue").
You write PREMIUM PLAYBOOKS — complete operating systems that readers execute from start to finish to build real businesses.

This is NOT a blog post. This is NOT a guide. This is an OPERATING SYSTEM with exact procedures.

CRITICAL STYLE RULES:
- Write in an INSTRUCTIONAL, COMMANDING tone — like a senior operator handing a junior their exact playbook
- Every instruction must be SPECIFIC: exact button names, exact menu paths, exact settings, exact URLs
- Include INTERACTIVE CHECK-INS throughout: "Do you see [X]? You should see [X] if you're in the right place.
  Go back and check [Y] if you don't see it." — These appear after EVERY major step.
- Show expected output at every step: UI states, JSON responses, dashboard screenshots described in text
- Include error scenarios: "If you see [ERROR], this means [CAUSE]. Fix it by [SOLUTION]."
- Name real tools with real prices and real free tier limits
- Include complete configurations — readers should be able to follow along without guessing
- Never use vague phrases like "configure it appropriately" — say EXACTLY what to configure
- Each procedure should take 10-60 minutes in real life — break large steps into sub-steps
- Use TABLES for: tool comparisons, cost breakdowns, pricing tiers, margin analysis, revenue projections
- Every module ends with a CHECK-IN checklist: "- [ ] Item 1" format with 4-7 items

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

Always mention at least 6-8 of these tools NATURALLY throughout the playbook.
Do NOT add a separate "Recommended Tools" section — we add that automatically.

PLAYBOOK STRUCTURE (follow this EXACTLY):

Opening paragraph: State what this playbook is (not a blog post — an operating system), the total number
of modules and procedures, and the outcome the reader will achieve if they complete every procedure.
Use bold for the count: "**X procedures. Y modules. Z+ hours of reading and execution.**"

---

# MODULE 1: [DESCRIPTIVE TITLE — ALL CAPS]

## Overview
What this module covers, why it matters, and what happens if you skip it.
Time to complete and tools needed.

## Procedure 1.1: [Exact Action — Imperative Verb]
Step-by-step instructions with:
- Exact URLs to visit
- Exact buttons to click
- Exact fields to fill in
- Interactive check-in: "Do you see [X]? If not, [troubleshooting]."
- Expected output or result

## Procedure 1.2: [Exact Action]
Same level of detail. Include tables where appropriate.

## Check-In: Module 1 Complete
- [ ] Item 1
- [ ] Item 2
(4-7 items)

---

Continue for 8-12 modules total. The modules should follow this logical progression:
1. FOUNDATION — Setup, accounts, infrastructure
2. TECH STACK — Tools, connections, API keys
3. FRAMEWORK — The universal process/methodology
4. FIRST BUILD — Guided walkthrough of the core product/service
5. CLIENT/USER ACQUISITION — How to get paying customers
6. DELIVERY — How to deliver value consistently
7. SCALING — From solo to team, margin analysis
8. ADVANCED PATTERNS — Premium techniques
9. PROPOSALS/CONTRACTS (if service business) or PRODUCT LAUNCH (if product)
10. FINANCIAL OPERATIONS — Revenue tracking, pricing increases
11. QUALITY ASSURANCE — Checklists, reviews
12. LAUNCH PLAN — Day-by-day execution calendar

---

# APPENDIX A: COMPLETE TOOL REFERENCE
Table with columns: Tool | Purpose | Free Tier | Paid Tier | When to Upgrade
(10-15 tools relevant to the playbook topic)

# APPENDIX B: THE COMPLETE SOP INDEX
Table with columns: SOP # | Procedure | Category | Difficulty | Est. Time

# APPENDIX C: THE REVENUE CALCULATOR
Table showing revenue projections at Month 1, Month 3, Month 6, and Month 12

WORD COUNT TARGET: 8,000-10,000 words. Every procedure must be fully detailed with exact steps.
The playbook must be so detailed that a complete beginner can follow it and end up with a working business."""


def generate_playbook(topic_data: dict, opportunity_data: dict = None, intelligence_data: dict = None):
    """Call the AI API to generate the full playbook.

    Uses a multi-pass approach for Groq:
    1. First pass generates the bulk
    2. Second pass continues if too short
    3. Third pass fills appendices if still short
    """
    topic = topic_data.get("playbook_angle", topic_data.get("selected_title", topic_data.get("topic", "")))
    context = topic_data.get("context", "")
    affiliates = topic_data.get("affiliates", [])
    price = random.choice(["₦15,000", "₦25,000", "₦35,000"])

    # Build cross-linking context
    cross_link_context = ""
    if opportunity_data:
        cross_link_context += f"""

RELATED OPPORTUNITY ARTICLE: "{opportunity_data.get('title', '')}" — this playbook is the premium companion to this opportunity deep-dive.
URL: /opportunities/{opportunity_data.get('slug', '')}/"""

    if intelligence_data:
        cross_link_context += f"""

RELATED INTELLIGENCE GUIDE: "{intelligence_data.get('title', '')}" — the free implementation guide that accompanies this playbook.
URL: /intelligence/{intelligence_data.get('slug', '')}/

In the opening paragraph, mention: "This playbook extends our free implementation guide with complete procedures, SOPs, and revenue calculators."
At the end, mention: "For the free step-by-step guide, see our [implementation guide]({{< ref "/intelligence/{intelligence_data.get('slug', '')}.md" >}}).\""""

    user_prompt = f"""Write a complete premium playbook about: {topic}

{'TRENDING CONTEXT: ' + context if context else ''}
Price point: {price}
{cross_link_context}

Follow the EXACT structure and style defined in your system instructions.
This is for the Playbook category on Menshly Global — the most premium, execution-focused content we publish.

The title must use IMPERATIVE VERBS (NOT "How to"):
Pattern: "[VERB], [VERB], and [VERB] [THING] with [TOOL]"

Return the playbook as pure Markdown (no front matter). Begin with the opening paragraph (no H1 title — the title goes in front matter only)."""

    api_key = PLAYBOOK_API_KEY
    api_base = PLAYBOOK_API_BASE
    model = PLAYBOOK_MODEL

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        "max_tokens": 16000,
        "temperature": 0.7,
    }
    print(f"Generating playbook about: {topic}")
    print(f"Price: {price}")
    print(f"Model: {model}")
    print("Calling API (this may take 2-3 minutes)...")
    data = api_call(payload, api_key=api_key, api_base=api_base)
    body = data["choices"][0]["message"]["content"]

    finish_reason = data["choices"][0].get("finish_reason", "")
    word_count = len(body.split())
    print(f"  First pass: {word_count} words, finish_reason={finish_reason}")

    if finish_reason == "length" or word_count < 6000:
        print("  Playbook too short, continuing with second pass...")
        continue_prompt = f"""The previous playbook was cut off. Here is what was generated so far (last section):

...{body[-2000:]}

CONTINUE the playbook from where it left off. Do NOT repeat any content. Pick up EXACTLY where it ended.
Make sure to include all remaining modules AND the 3 appendices.

WORD COUNT TARGET: Write at least 3000 more words."""

        payload2 = {
            "model": model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
                {"role": "assistant", "content": body},
                {"role": "user", "content": continue_prompt},
            ],
            "max_tokens": 16000,
            "temperature": 0.65,
        }
        data2 = api_call(payload2, api_key=api_key, api_base=api_base)
        continuation = data2["choices"][0]["message"]["content"]
        cont_words = len(continuation.split())
        print(f"  Second pass: {cont_words} words added")
        body = body + "\n\n" + continuation

        finish_reason2 = data2["choices"][0].get("finish_reason", "")
        total_words = len(body.split())
        module_count = body.count("# MODULE")

        if finish_reason2 == "length" or total_words < 8000 or module_count < 6:
            print("  Still short, continuing with third pass for appendices...")
            appendix_prompt = f"""The playbook needs its appendices. Here is the end of what was generated:

...{body[-2000:]}

Write the MISSING APPENDICES now:
- APPENDIX A: COMPLETE TOOL REFERENCE (table with 10-15 tools)
- APPENDIX B: THE COMPLETE SOP INDEX (table with one row per procedure)
- APPENDIX C: THE REVENUE CALCULATOR (table with Month 1/3/6/12 projections)

Do NOT repeat any content already written. Only write the appendices that are missing.
WORD COUNT TARGET: At least 1500 words for the appendices."""

            payload3 = {
                "model": model,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                    {"role": "assistant", "content": body},
                    {"role": "user", "content": appendix_prompt},
                ],
                "max_tokens": 16000,
                "temperature": 0.6,
            }
            data3 = api_call(payload3, api_key=api_key, api_base=api_base)
            appendix = data3["choices"][0]["message"]["content"]
            app_words = len(appendix.split())
            print(f"  Third pass: {app_words} words added")
            body = body + "\n\n" + appendix

    final_words = len(body.split())
    print(f"  Total: {final_words} words")

    # Inject affiliate links
    body = inject_affiliate_links(body, affiliates)

    # Append Recommended Tools section
    tools_section = generate_tools_section(affiliates)
    if tools_section:
        body = body + "\n\n" + tools_section

    return body, price


def extract_title(body: str) -> str:
    """Extract or infer the title from the playbook body."""
    for line in body.split("\n")[:10]:
        line = line.strip()
        bold_match = re.match(r"^\*\*(.+?)\*\*", line)
        if bold_match:
            return bold_match.group(1).rstrip(".!")
        if line.startswith("# ") and not line.startswith("## "):
            title = line.lstrip("# ").strip()
            title = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', title)
            return title
    for line in body.split("\n"):
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("---") and len(line) > 10:
            sentence = line.split(".")[0].strip()
            if len(sentence) > 10:
                return sentence
    return "Untitled Playbook"


def slugify(title: str) -> str:
    """Create a URL-safe slug from the title."""
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    slug = slug.strip("-")
    return slug[:80]


def build_excerpt(body: str) -> str:
    """Build a short excerpt from the playbook body."""
    lines = body.split("\n")
    paragraph = ""
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            continue
        if line.startswith("---"):
            continue
        if not line:
            if paragraph:
                break
            continue
        clean = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
        clean = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', clean)
        paragraph += clean + " "
    excerpt = paragraph.strip()[:250]
    if len(paragraph.strip()) > 250:
        excerpt += "..."
    return excerpt.replace('"', "'")


def estimate_read_time(body: str) -> str:
    """Estimate read time based on word count."""
    word_count = len(body.split())
    minutes = max(15, word_count // 200)
    return f"{minutes} MIN"


def update_article_cross_links(article_path: Path, playbook_slug: str, section: str):
    """Update an existing article with a link to the new playbook."""
    if not article_path.exists():
        return
    try:
        content = article_path.read_text()
        field_name = "relatedPlaybook"
        if field_name not in content:
            # Insert before the closing ---
            content = content.replace(
                "---\n\n",
                f'{field_name}: "/playbooks/{playbook_slug}/"\n---\n\n',
                1,
            )
            article_path.write_text(content)
            print(f"  Updated {article_path.name} with playbook link")
    except Exception as e:
        print(f"  Warning: Could not update {article_path.name}: {e}")


if __name__ == "__main__":
    if not AI_API_KEY:
        print("ERROR: AI_API_KEY not set")
        exit(1)

    # Step 0: Load cross-link data
    print("Loading cross-link data...")
    last_data = load_last_generated()
    opportunity_data = last_data.get("last_opportunity")
    intelligence_data = last_data.get("last_intelligence")

    # Get topic data
    if opportunity_data:
        topic_data = {
            "topic": opportunity_data.get("topic", ""),
            "playbook_angle": opportunity_data.get("playbook_angle", ""),
            "context": opportunity_data.get("context", ""),
            "affiliates": opportunity_data.get("affiliates", []),
        }
        print(f"Writing playbook for same topic as opportunity: {opportunity_data.get('title', '')}")
    else:
        print("No recent opportunity found, discovering trending topic...")
        discovery = TrendingTopicDiscovery()
        discovery.ensure_minimum_queue(5)
        topic_data = discovery.get_next_topic("playbook")

    if not topic_data or not topic_data.get("playbook_angle"):
        print("ERROR: No topic available")
        exit(1)

    topic = topic_data.get("playbook_angle", topic_data.get("topic", ""))

    # Step 1: Generate images
    prelim_slug = slugify(topic)

    print("Generating thumbnail image...")
    image_path = generate_article_image(
        topic=topic,
        slug=prelim_slug,
        section="playbooks",
    )
    print(f"Thumbnail saved: {image_path}")

    print("Generating hero image...")
    hero_path = generate_hero_image(
        topic=topic,
        slug=prelim_slug,
        section="playbooks",
    )
    print(f"Hero image saved: {hero_path}")

    # Step 2: Generate playbook content
    print("Generating playbook content...")
    body, price = generate_playbook(topic_data, opportunity_data, intelligence_data)
    title = extract_title(body)
    excerpt = build_excerpt(body)
    read_time = estimate_read_time(body)

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
        'category: "Playbook"',
        f'price: "{price}"',
        f'readTime: "{read_time}"',
        f'excerpt: "{excerpt}"',
        f'image: "{image_path}"',
        f'heroImage: "{hero_path}"',
    ]

    # Cross-link to opportunity article
    if opportunity_data:
        opp_slug = opportunity_data.get("slug", "")
        if opp_slug:
            front_matter_lines.append(f'relatedOpportunity: "/opportunities/{opp_slug}/"')

    # Cross-link to intelligence guide
    if intelligence_data:
        int_slug = intelligence_data.get("slug", "")
        if int_slug:
            front_matter_lines.append(f'relatedGuide: "/intelligence/{int_slug}/"')

    front_matter_lines.extend([
        "---",
        "",
    ])

    front_matter = "\n".join(front_matter_lines)

    content_dir = Path("content/playbooks")
    content_dir.mkdir(parents=True, exist_ok=True)
    filepath = content_dir / f"{slug}.md"
    filepath.write_text(front_matter + body)

    word_count = len(body.split())
    print(f"Created: {filepath}")
    print(f"Title: {title}")
    print(f"Slug: {slug}")
    print(f"Price: {price}")
    print(f"Read Time: {read_time}")
    print(f"Word count: ~{word_count}")

    # Quality check
    module_count = body.count("# MODULE")
    procedure_count = body.count("## Procedure")
    checkin_count = body.count("Check-In:")
    appendix_count = body.count("# APPENDIX")

    print(f"\nQuality Check:")
    print(f"  Modules found: {module_count} (target: 8-12)")
    print(f"  Procedures found: {procedure_count} (target: 25+)")
    print(f"  Check-ins found: {checkin_count} (target: 8+)")
    print(f"  Appendices found: {appendix_count} (target: 3)")

    if module_count < 6:
        print("  WARNING: Fewer modules than expected.")
    if procedure_count < 15:
        print("  WARNING: Fewer procedures than expected.")

    # Step 4: Update existing opportunity and intelligence articles with playbook link
    if opportunity_data:
        opp_file = Path("content/opportunities") / f"{opportunity_data.get('slug', '')}.md"
        update_article_cross_links(opp_file, slug, "opportunities")

    if intelligence_data:
        int_file = Path("content/intelligence") / f"{intelligence_data.get('slug', '')}.md"
        update_article_cross_links(int_file, slug, "intelligence")

    # Step 5: Mark topic as used
    if opportunity_data:
        discovery = TrendingTopicDiscovery()
        discovery.mark_topic_used(topic_data)

    print(f"\n✅ Playbook generated successfully!")
    print(f"   Cross-linked to opportunity: {opportunity_data.get('slug', 'N/A') if opportunity_data else 'N/A'}")
    print(f"   Cross-linked to intelligence: {intelligence_data.get('slug', 'N/A') if intelligence_data else 'N/A'}")
