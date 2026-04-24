#!/usr/bin/env python3
"""Generate a premium Playbook article using AI API.

This generator produces full-length (~8,000-10,000 word) premium playbooks
that follow the Menshly Global Playbook template — the same format as
"The AI Automation Agency Playbook":
  - Multiple MODULES (8-12), each with an Overview
  - Numbered PROCEDURES within each module (e.g., Procedure 1.1, 1.2)
  - Interactive check-ins at every stage ("Do you see X? You should see X.")
  - Exact UI step-by-step instructions (button names, menu paths, settings)
  - Error handling and troubleshooting at every step
  - Tables for cost breakdowns, tool references, margin analysis
  - Module-level check-in checklists
  - Appendices (Tool Reference, SOP Index, Revenue Calculator)
  - Title using imperative verbs (NOT "How to")
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

AI_API_KEY = os.environ.get("AI_API_KEY", "")
AI_API_BASE = os.environ.get("AI_API_BASE", "https://api.groq.com/openai/v1")
AI_API_MODEL = os.environ.get("AI_MODEL", "llama-3.3-70b-versatile")
AI_MODEL = AI_API_MODEL

# Optional: Override model for playbooks (use a better model if available)
PLAYBOOK_API_KEY = os.environ.get("PLAYBOOK_API_KEY", AI_API_KEY)
PLAYBOOK_API_BASE = os.environ.get("PLAYBOOK_API_BASE", AI_API_BASE)
PLAYBOOK_MODEL = os.environ.get("PLAYBOOK_MODEL", AI_MODEL)


def api_call(payload, max_retries=5, api_key=None, api_base=None):
    """Call the AI API with automatic retry on rate limits (429) and server errors (5xx).
    
    For playbooks, pass api_key and api_base to use PLAYBOOK_* overrides.
    """
    key = api_key or AI_API_KEY
    base = api_base or AI_API_BASE
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }
    for attempt in range(max_retries + 1):
        try:
            resp = requests.post(
                f"{base}/chat/completions",
                headers=headers,
                json=payload,
                timeout=300,
            )
            if resp.status_code == 429:
                retry_after = resp.headers.get("Retry-After")
                wait = int(retry_after) if retry_after else 30 * (attempt + 1)
                if attempt < max_retries:
                    print(f"  Rate limited (429). Waiting {wait}s before retry {attempt+1}/{max_retries}...")
                    time.sleep(wait)
                    continue
                else:
                    print(f"  Rate limited (429). Max retries reached.")
                    resp.raise_for_status()
            if resp.status_code >= 500:
                if attempt < max_retries:
                    wait = 10 * (attempt + 1)
                    print(f"  Server error ({resp.status_code}). Waiting {wait}s before retry {attempt+1}/{max_retries}...")
                    time.sleep(wait)
                    continue
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.Timeout:
            if attempt < max_retries:
                wait = 15 * (attempt + 1)
                print(f"  Request timed out. Waiting {wait}s before retry {attempt+1}/{max_retries}...")
                time.sleep(wait)
                continue
            raise
    resp.raise_for_status()

# ── Playbook topics ──────────────────────────────────────────────────
TOPICS = [
    "Build and Scale an AI Content Agency from Zero to $30K/Month",
    "Design, Build, and Monetize AI SaaS Micro-Products on Replit",
    "Launch and Scale an AI Voice Agent Business with Vapi",
    "Build and Automate an AI SEO Agency with Make.com Workflows",
    "Create, Deploy, and Scale AI-Powered E-Commerce Chatbots",
    "Build and Monetize AI Image Generation Workflows and Agencies",
    "Design and Launch an AI Newsletter Business with Full Automation",
    "Build and Scale an AI Social Media Management Pipeline",
    "Create and Deploy AI-Powered Customer Onboarding Systems",
    "Build and Automate an AI Bookkeeping and Finance Service",
    "Configure, Deploy, and Scale AI-Powered HR and Recruitment Automation",
    "Build and Monetize a Faceless YouTube Channel Empire with AI",
    "Design, Build, and Sell AI-Powered Email Marketing Automations",
    "Build and Scale an AI Data Analysis and Reporting Service",
    "Create, Launch, and Grow an AI Course Creation Business",
    "Build and Operate an AI Copywriting Agency with Automation",
    "Design and Deploy AI Lead Generation Systems with OpenAI",
    "Set Up, Train, and Deploy Custom AI Agents with LangChain",
    "Build and Monetize AI Automation for Real Estate Agencies",
    "Create and Scale an AI-Powered Podcast Production Business",
]

PRICES = ["$29", "$39", "$47"]

topic = random.choice(TOPICS)
price = random.choice(PRICES)

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
Same level of detail. Include tables where appropriate (database columns, settings, etc.)

## Procedure 1.3: [Exact Action]
Continue with the same depth.

## Check-In: Module 1 Complete
- [ ] Item 1
- [ ] Item 2
(4-7 items, counting format: "X checkmarks. Do you have all X?")

---

# MODULE 2: [DESCRIPTIVE TITLE]
(Repeat the same structure: Overview, Procedures 2.1-2.N, Check-In)

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

Adjust the exact module titles and count to fit the topic naturally.

---

# APPENDIX A: COMPLETE TOOL REFERENCE
Table with columns: Tool | Purpose | Free Tier | Paid Tier | When to Upgrade
(10-15 tools relevant to the playbook topic)

# APPENDIX B: THE COMPLETE SOP INDEX
Table with columns: SOP # | Procedure | Category | Difficulty | Est. Time
(One row per procedure — should match the total procedure count stated in the intro)

# APPENDIX C: THE REVENUE CALCULATOR
Table showing revenue projections at Month 1, Month 3, Month 6, and Month 12
Include: Active Clients/Users, Average Revenue, Total MRR, Setup Fees, Total Annual Revenue, Expenses, Net Profit

WORD COUNT TARGET: 8,000-10,000 words. Every procedure must be fully detailed with exact steps.
Do NOT write short sections. Every procedure needs sub-steps, configurations, and check-ins.
The playbook must be so detailed that a complete beginner can follow it and end up with a working business."""

USER_PROMPT = f"""Write a complete premium playbook about: {topic}

Follow the EXACT structure and style defined in your system instructions.
This is for the Playbook category on Menshly Global — the most premium, execution-focused content we publish.
Price point: {price}

The title must use IMPERATIVE VERBS (NOT "How to"):
Pattern: "[VERB], [VERB], and [VERB] [THING] with [TOOL]"
Example: "Build, Scale, and Monetize an AI Content Agency with Make.com and OpenAI"

Return the playbook as pure Markdown (no front matter). Begin with the opening paragraph (no H1 title — the title goes in front matter only)."""

# Number of API calls to make (each generates a portion)
# We'll generate the full playbook in one large call for consistency
MAX_TOKENS = 16000
TEMPERATURE = 0.7


def generate_playbook():
    """Call the AI API to generate the full playbook.
    
    Uses a multi-pass approach for Groq:
    1. First pass generates the bulk (first ~6 modules)
    2. Second pass continues if too short (< 6000 words)
    3. Third pass fills remaining modules + appendices if still short
    """
    # Use PLAYBOOK_ override variables if set, otherwise fall back to AI_ vars
    api_key = PLAYBOOK_API_KEY
    api_base = PLAYBOOK_API_BASE
    model = PLAYBOOK_MODEL

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT},
        ],
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE,
    }
    print(f"Generating playbook about: {topic}")
    print(f"Price: {price}")
    print(f"Model: {model}")
    print(f"Max tokens: {MAX_TOKENS}")
    print("Calling API (this may take 2-3 minutes for a full playbook)...")
    data = api_call(payload, api_key=api_key, api_base=api_base)
    body = data["choices"][0]["message"]["content"]
    
    # Check if the playbook was cut short
    finish_reason = data["choices"][0].get("finish_reason", "")
    word_count = len(body.split())
    print(f"  First pass: {word_count} words, finish_reason={finish_reason}")
    
    # If too short, continue with second pass
    if finish_reason == "length" or word_count < 6000:
        print("  Playbook too short, continuing with second pass...")
        continue_prompt = f"""The previous playbook was cut off. Here is what was generated so far (last section):

...{body[-2000:]}

CONTINUE the playbook from where it left off. Do NOT repeat any content. Pick up EXACTLY where it ended.
If you were in the middle of a module, complete it. Then continue with all remaining modules.
Make sure to include all remaining modules AND the 3 appendices (Tool Reference, SOP Index, Revenue Calculator).

WORD COUNT TARGET: Write at least 3000 more words. Every procedure needs sub-steps, configurations, and check-ins."""
        
        payload2 = {
            "model": model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_PROMPT},
                {"role": "assistant", "content": body},
                {"role": "user", "content": continue_prompt},
            ],
            "max_tokens": MAX_TOKENS,
            "temperature": 0.65,
        }
        data2 = api_call(payload2, api_key=api_key, api_base=api_base)
        continuation = data2["choices"][0]["message"]["content"]
        cont_words = len(continuation.split())
        print(f"  Second pass: {cont_words} words added")
        body = body + "\n\n" + continuation
        
        # Check again after second pass
        finish_reason2 = data2["choices"][0].get("finish_reason", "")
        total_words = len(body.split())
        module_count = body.count("# MODULE")
        
        if (finish_reason2 == "length" or total_words < 8000 or module_count < 6):
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
                    {"role": "user", "content": USER_PROMPT},
                    {"role": "assistant", "content": body},
                    {"role": "user", "content": appendix_prompt},
                ],
                "max_tokens": MAX_TOKENS,
                "temperature": 0.6,
            }
            data3 = api_call(payload3, api_key=api_key, api_base=api_base)
            appendix = data3["choices"][0]["message"]["content"]
            app_words = len(appendix.split())
            print(f"  Third pass: {app_words} words added")
            body = body + "\n\n" + appendix
    
    final_words = len(body.split())
    print(f"  Total: {final_words} words")
    return body


def extract_title(body: str) -> str:
    """Extract or infer the title from the playbook body.

    The playbook body does NOT start with an H1 (per our template),
    so we look for the first bold statement or infer from content.
    """
    # Look for a bold title-like line near the top
    for line in body.split("\n")[:10]:
        line = line.strip()
        # Check for markdown bold that looks like a title
        bold_match = re.match(r"^\*\*(.+?)\*\*", line)
        if bold_match:
            return bold_match.group(1).rstrip(".!")
        # Check for H1
        if line.startswith("# ") and not line.startswith("## "):
            return line.lstrip("# ").strip()

    # Fallback: use the first meaningful line
    for line in body.split("\n"):
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("---") and len(line) > 10:
            # Take first sentence
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
        # Strip bold markers for clean excerpt
        clean = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
        paragraph += clean + " "
    excerpt = paragraph.strip()[:250]
    if len(paragraph.strip()) > 250:
        excerpt += "..."
    return excerpt.replace('"', "'")


def estimate_read_time(body: str) -> str:
    """Estimate read time based on word count."""
    word_count = len(body.split())
    # Average reading speed: 200 words/min for technical content
    minutes = max(15, word_count // 200)
    return f"{minutes} MIN"


if __name__ == "__main__":
    if not AI_API_KEY:
        print("ERROR: AI_API_KEY not set")
        exit(1)

    # Step 1: Generate images FIRST (before playbook content)
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
    body = generate_playbook()
    title = extract_title(body)
    excerpt = build_excerpt(body)
    read_time = estimate_read_time(body)

    slug = slugify(title)
    now = datetime.now(timezone.utc)

    # Step 3: Rename images if slug differs from preliminary slug
    if slug != prelim_slug:
        import shutil
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
category: "Playbook"
price: "{price}"
readTime: "{read_time}"
excerpt: "{excerpt}"
image: "{image_path}"
heroImage: "{hero_path}"
---

"""

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
        print("  WARNING: Fewer modules than expected. The playbook may be incomplete.")
    if procedure_count < 15:
        print("  WARNING: Fewer procedures than expected. The playbook may need expansion.")
    if word_count < 5000:
        print("  WARNING: Word count is low. Consider increasing MAX_TOKENS or regenerating.")
