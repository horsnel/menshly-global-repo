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
import requests
from datetime import datetime, timezone
from pathlib import Path
import random

from image_utils import generate_article_image

AI_API_KEY = os.environ.get("AI_API_KEY", "")
AI_API_BASE = os.environ.get("AI_API_BASE", "https://api.openai.com/v1")
AI_MODEL = os.environ.get("AI_MODEL", "gpt-4o")

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
    """Call the AI API to generate the full playbook."""
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
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE,
    }
    print(f"Generating playbook about: {topic}")
    print(f"Price: {price}")
    print(f"Max tokens: {MAX_TOKENS}")
    print("Calling API (this may take 2-3 minutes for a full playbook)...")
    resp = requests.post(
        f"{AI_API_BASE}/chat/completions",
        headers=headers,
        json=payload,
        timeout=300,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]


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

    body = generate_playbook()
    title = extract_title(body)
    excerpt = build_excerpt(body)
    read_time = estimate_read_time(body)

    slug = slugify(title)
    now = datetime.now(timezone.utc)

    # Generate playbook thumbnail via Pollination AI
    image_path = generate_article_image(
        topic=topic,
        slug=slug,
        section="playbooks",
    )

    front_matter = f"""---
title: "{title}"
date: {now.strftime("%Y-%m-%d")}
category: "Playbook"
price: "{price}"
readTime: "{read_time}"
excerpt: "{excerpt}"
image: "{image_path}"
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
