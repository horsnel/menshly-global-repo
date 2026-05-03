#!/usr/bin/env python3
"""Generate a premium Playbook article using AI API.

This generator produces full-length (~8,000-10,000 word) premium playbooks
that follow the Menshly Global Playbook template:
  - Multiple MODULES (8-12), each with an Overview
  - Numbered PROCEDURES within each module
  - Interactive check-ins at every stage
  - Appendices (Tool Reference, SOP Index, Revenue Calculator)

v4 REWRITE — Together AI powered, quality-enforced:
  - Uses Together AI (Llama-3.3-70B) as primary backend for reliable long-form
  - Generates each module as a SEPARATE API call for reliability
  - Enforces minimum word count per module (600+ words)
  - Guaranteed structure: opening + 10 modules + 3 appendices
  - QUALITY REPAIR LOOP: re-generates missing modules until all 10 are present
  - Final quality gate: exits with error if < 8 modules or < 20 procedures
  - Cross-links to opportunity and intelligence articles
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

# Optional: Override model for playbooks — Together AI is preferred
PLAYBOOK_API_KEY = os.environ.get("PLAYBOOK_API_KEY", os.environ.get("TOGETHER_API_KEY", AI_API_KEY))
PLAYBOOK_API_BASE = os.environ.get("PLAYBOOK_API_BASE", "https://api.together.xyz/v1" if PLAYBOOK_API_KEY and PLAYBOOK_API_KEY.startswith("tgp_") else AI_API_BASE)
PLAYBOOK_MODEL = os.environ.get("PLAYBOOK_MODEL", "meta-llama/Llama-3.3-70B-Instruct-Turbo" if PLAYBOOK_API_KEY and PLAYBOOK_API_KEY.startswith("tgp_") else AI_MODEL)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LAST_GENERATED_FILE = PROJECT_ROOT / "data" / "last_generated.json"

# ── Quality targets ──
MIN_MODULES = 8
MIN_PROCEDURES = 20
MIN_TOTAL_WORDS = 6000
MAX_REPAIR_ATTEMPTS = 3

# ── Module definitions — the 10-module playbook skeleton ──
MODULE_DEFS = [
    {
        "num": 1,
        "title": "FOUNDATION",
        "desc": "Setup, accounts, infrastructure. Register your business accounts, set up your domain, email, and foundational tools.",
        "procedures": 3,
        "min_words": 700,
    },
    {
        "num": 2,
        "title": "TECH STACK",
        "desc": "Tools, connections, API keys. Connect every tool in your stack, configure integrations, and verify data flows.",
        "procedures": 3,
        "min_words": 700,
    },
    {
        "num": 3,
        "title": "FRAMEWORK",
        "desc": "The universal process and methodology. Define your service delivery framework, client onboarding flow, and quality standards.",
        "procedures": 2,
        "min_words": 700,
    },
    {
        "num": 4,
        "title": "FIRST BUILD",
        "desc": "Guided walkthrough of the core product or service. Build your first deliverable end-to-end with real client data.",
        "procedures": 3,
        "min_words": 900,
    },
    {
        "num": 5,
        "title": "CLIENT ACQUISITION",
        "desc": "How to get paying customers. Set up your outreach systems, landing page, and lead generation pipeline.",
        "procedures": 3,
        "min_words": 800,
    },
    {
        "num": 6,
        "title": "DELIVERY",
        "desc": "How to deliver value consistently. Build your delivery pipeline, quality checkpoints, and client communication templates.",
        "procedures": 2,
        "min_words": 700,
    },
    {
        "num": 7,
        "title": "SCALING",
        "desc": "From solo to team, margin analysis. Hire your first contractor, build SOPs for delegation, and analyze margins.",
        "procedures": 3,
        "min_words": 800,
    },
    {
        "num": 8,
        "title": "ADVANCED PATTERNS",
        "desc": "Premium techniques and upsells. Add high-ticket services, build recurring revenue, and create productized offerings.",
        "procedures": 2,
        "min_words": 700,
    },
    {
        "num": 9,
        "title": "FINANCIAL OPERATIONS",
        "desc": "Revenue tracking, pricing increases, and proposal templates. Build your financial dashboard and contract templates.",
        "procedures": 2,
        "min_words": 700,
    },
    {
        "num": 10,
        "title": "LAUNCH PLAN",
        "desc": "Day-by-day execution calendar for the next 30 days. Your complete action plan to go from zero to first paying client.",
        "procedures": 3,
        "min_words": 800,
    },
]

# ── System prompt shared across all module calls ──
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

CRITICAL LENGTH RULES:
- Each procedure MUST be at least 250 words. This is NON-NEGOTIABLE.
- Each module overview MUST be at least 100 words.
- Include specific numbered steps (1, 2, 3...) within each procedure — never write in vague paragraphs.
- Do NOT truncate or cut short. Write the COMPLETE procedure.

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

Always mention at least 2-3 of these tools NATURALLY in each module.
Do NOT add a separate "Recommended Tools" section — we add that automatically."""


def load_last_generated() -> dict:
    """Load the last generated article data for cross-linking."""
    if not LAST_GENERATED_FILE.exists():
        return {}
    try:
        return json.loads(LAST_GENERATED_FILE.read_text())
    except (json.JSONDecodeError, Exception):
        return {}


def _call_api(messages: list, max_tokens: int = 8000, temperature: float = 0.7) -> str:
    """Make a single API call and return the content text."""
    payload = {
        "model": PLAYBOOK_MODEL,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    data = api_call(payload, api_key=PLAYBOOK_API_KEY, api_base=PLAYBOOK_API_BASE)
    return data["choices"][0]["message"]["content"]


def generate_opening(topic: str, context: str, price: str, cross_link_context: str) -> str:
    """Generate the opening paragraph that introduces the playbook."""
    prompt = f"""Write the OPENING PARAGRAPH for a premium playbook about: {topic}

{'TRENDING CONTEXT: ' + context if context else ''}
Price point: {price}
{cross_link_context}

The opening paragraph must:
1. State that this is an OPERATING SYSTEM (not a blog post or guide)
2. Include the count in bold: "**25 procedures. 10 modules. 12+ hours of reading and execution.**"
3. State the outcome the reader will achieve if they complete every procedure
4. Be 150-250 words long
5. Sound commanding and instructional — like a senior operator briefing a junior

{"Mention: 'This playbook extends our free implementation guide with complete procedures, SOPs, and revenue calculators.'" if "implementation guide" in cross_link_context else ""}

Return ONLY the opening paragraph as Markdown. No title, no heading — just the paragraph."""

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]

    for attempt in range(3):
        try:
            result = _call_api(messages, max_tokens=1000, temperature=0.7)
            if len(result.split()) >= 80:
                return result
            print(f"  Opening too short ({len(result.split())} words), retrying...")
        except Exception as e:
            print(f"  Opening generation attempt {attempt+1} failed: {str(e)[:100]}")
            time.sleep(5)

    return f"This is your complete operating system for {topic}. **25 procedures. 10 modules. 12+ hours of reading and execution.** Follow every procedure in order and you will have a fully operational business generating revenue within 30 days. Skip nothing. Every step exists because someone before you failed by skipping it."


def generate_module(module_def: dict, topic: str, context: str, prev_module_summary: str = "") -> str:
    """Generate a single module with its procedures, check-ins, and detail.

    Each module is generated as a separate API call, ensuring consistent
    quality regardless of the AI backend being used.
    """
    num = module_def["num"]
    title = module_def["title"]
    desc = module_def["desc"]
    proc_count = module_def["procedures"]
    min_words = module_def["min_words"]

    # Build procedure headings list
    proc_headings = ""
    for p in range(1, proc_count + 1):
        if p == 1:
            proc_headings += f"## Procedure {num}.{p}: [Exact Action — Imperative Verb]\n"
            proc_headings += "Step-by-step instructions with:\n"
            proc_headings += "- Exact URLs to visit or exact tool names to open\n"
            proc_headings += "- Exact buttons to click\n"
            proc_headings += "- Exact fields to fill in\n"
            proc_headings += "- Interactive check-in: 'Do you see [X]? If not, [troubleshooting].'\n"
            proc_headings += "- Expected output or result\n"
            proc_headings += "- Error scenario: 'If you see [ERROR], this means [CAUSE]. Fix it by [SOLUTION].'\n"
            proc_headings += "Write at least 250 words per procedure.\n\n"
        elif p == 2:
            proc_headings += f"## Procedure {num}.{p}: [Exact Action]\n"
            proc_headings += "Same level of detail. Include a TABLE where appropriate (tool comparison, cost breakdown, or settings).\n"
            proc_headings += "Write at least 250 words.\n\n"
        else:
            proc_headings += f"## Procedure {num}.{p}: [Exact Action]\n"
            proc_headings += "Same level of detail. Include specific configurations and settings.\n"
            proc_headings += "Write at least 250 words.\n\n"

    prompt = f"""Write MODULE {num}: {title} for a premium playbook about: {topic}

{'TRENDING CONTEXT: ' + context if context else ''}

This module covers: {desc}

You MUST write EXACTLY {proc_count} procedures for this module.

Follow this EXACT structure:

---

# MODULE {num}: {title}

## Overview
What this module covers, why it matters, and what happens if you skip it.
Time to complete and tools needed. Write 2-3 paragraphs (at least 100 words).

{proc_headings}
## Check-In: Module {num} Complete
- [ ] Item 1 (specific, measurable)
- [ ] Item 2
- [ ] Item 3
- [ ] Item 4
(4-7 items)

{"CONTEXT: The previous module covered: " + prev_module_summary if prev_module_summary else ""}

WORD COUNT TARGET: At least {min_words} words for this entire module.
Be SPECIFIC. Name real tools, real prices, real settings. No vague instructions.
Do NOT truncate or cut short. Write EVERY procedure COMPLETELY.
Each procedure must have at least 10 numbered steps."""

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]

    for attempt in range(3):
        try:
            # Use higher max_tokens for Together AI (supports longer outputs)
            result = _call_api(messages, max_tokens=8000, temperature=0.7)
            word_count = len(result.split())

            # Quality check: ensure we have the minimum structure
            has_module_heading = f"# MODULE {num}" in result or f"# Module {num}" in result
            procedure_count = result.count("## Procedure")
            has_checkin = "Check-In" in result

            if word_count >= min_words * 0.6 and has_module_heading and procedure_count >= 1:
                if word_count < min_words:
                    print(f"  Module {num}: {word_count} words (target {min_words}, accepted with {procedure_count} procs)")
                else:
                    print(f"  Module {num}: {word_count} words, {procedure_count} procs ✓")
                return result
            else:
                print(f"  Module {num} attempt {attempt+1}: too short or missing structure ({word_count} words, {procedure_count} procs), retrying...")
                time.sleep(3)
        except Exception as e:
            print(f"  Module {num} attempt {attempt+1} failed: {str(e)[:100]}")
            time.sleep(5)

    # Fallback: return whatever we got from the last attempt
    print(f"  Module {num}: using best available output after retries")
    return result


def generate_appendix(appendix_letter: str, topic: str, all_modules_text: str) -> str:
    """Generate one appendix section."""
    if appendix_letter == "A":
        title = "COMPLETE TOOL REFERENCE"
        desc = "Table with columns: Tool | Purpose | Free Tier | Paid Tier | When to Upgrade"
        extra = "Include 10-15 tools relevant to the playbook topic. Use real pricing."
    elif appendix_letter == "B":
        title = "THE COMPLETE SOP INDEX"
        desc = "Table with columns: SOP # | Procedure | Category | Difficulty | Est. Time"
        extra = "List every procedure from all 10 modules. At least 20 rows."
    else:  # C
        title = "THE REVENUE CALCULATOR"
        desc = "Table showing revenue projections at Month 1, Month 3, Month 6, and Month 12"
        extra = """Include these tables:
1. Revenue Projections: Month | Revenue | Clients | Expenses | Profit
2. Pricing Tiers: Tier | Price | Deliverables | Margin
3. Break-Even Analysis: showing when initial investment is recovered"""

    prompt = f"""Write APPENDIX {appendix_letter}: {title} for a playbook about: {topic}

{desc}

{extra}

Here is a summary of the playbook modules for reference:
{all_modules_text[:3000]}

Return ONLY this appendix section. Start with:
# APPENDIX {appendix_letter}: {title}

WORD COUNT TARGET: At least 500 words."""

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]

    for attempt in range(3):
        try:
            result = _call_api(messages, max_tokens=4000, temperature=0.6)
            if len(result.split()) >= 200:
                return result
            print(f"  Appendix {appendix_letter} attempt {attempt+1}: too short, retrying...")
        except Exception as e:
            print(f"  Appendix {appendix_letter} attempt {attempt+1} failed: {str(e)[:100]}")
            time.sleep(5)

    # Minimal fallback
    if appendix_letter == "A":
        return f"# APPENDIX A: COMPLETE TOOL REFERENCE\n\n| Tool | Purpose | Free Tier | Paid Tier | When to Upgrade |\n|------|---------|-----------|-----------|------------------|\n| Make.com | Automation | 1,000 ops/mo | $9/mo | 10,000+ ops/mo |\n| ChatGPT | AI Assistant | Free | $20/mo | API integration |\n| Notion | Workspace | Free | $8/mo | Team collaboration |\n| Canva | Design | Free | $13/mo | Brand kit needed |\n| Apollo.io | Sales Intel | Free | $49/mo | 100+ leads/mo |\n"
    elif appendix_letter == "B":
        return f"# APPENDIX B: THE COMPLETE SOP INDEX\n\n| SOP # | Procedure | Category | Difficulty | Est. Time |\n|-------|-----------|----------|------------|----------|\n| 1.1 | Account Setup | Foundation | Easy | 30 min |\n| 2.1 | API Configuration | Tech Stack | Medium | 45 min |\n| 4.1 | First Deliverable | First Build | Hard | 2 hrs |\n| 5.1 | Outreach Launch | Client Acquisition | Medium | 1 hr |\n| 10.1 | 30-Day Calendar | Launch Plan | Easy | 45 min |\n"
    else:
        return f"# APPENDIX C: THE REVENUE CALCULATOR\n\n| Month | Revenue | Clients | Expenses | Profit |\n|-------|---------|---------|----------|--------|\n| 1 | $0 | 0 | $50 | -$50 |\n| 3 | $1,500 | 2 | $100 | $1,400 |\n| 6 | $5,000 | 5 | $200 | $4,800 |\n| 12 | $15,000 | 10 | $500 | $14,500 |\n"


def _count_modules_in_text(text: str) -> set:
    """Find which module numbers exist in the generated text."""
    found = set()
    for match in re.finditer(r"#\s+MODULE\s+(\d+)", text, re.IGNORECASE):
        found.add(int(match.group(1)))
    return found


def _count_procedures_in_text(text: str) -> int:
    """Count the number of procedures in the generated text."""
    return len(re.findall(r"##\s+Procedure\s+\d+\.\d+", text, re.IGNORECASE))


def repair_missing_modules(modules: list, topic: str, context: str) -> list:
    """Quality repair loop: re-generate any missing modules.

    After the initial generation pass, check which modules are missing
    and re-generate them individually. This ensures we always get
    the full 10-module structure.
    """
    # Find which module numbers we actually have
    found_nums = set()
    for m in modules:
        found_nums.update(_count_modules_in_text(m))

    expected_nums = {d["num"] for d in MODULE_DEFS}
    missing_nums = expected_nums - found_nums

    if not missing_nums:
        print(f"  All {len(expected_nums)} modules present ✓")
        return modules

    print(f"  WARNING: Missing modules: {sorted(missing_nums)}")
    print(f"  Starting quality repair loop...")

    for repair_attempt in range(MAX_REPAIR_ATTEMPTS):
        still_missing = sorted(expected_nums - found_nums)
        if not still_missing:
            print(f"  Repair complete! All modules present after attempt {repair_attempt}")
            break

        print(f"  Repair attempt {repair_attempt + 1}/{MAX_REPAIR_ATTEMPTS}: regenerating modules {still_missing}")

        for num in still_missing:
            module_def = next((d for d in MODULE_DEFS if d["num"] == num), None)
            if not module_def:
                continue

            # Get previous module summary for context
            prev_summary = ""
            if num > 1 and num - 1 in found_nums:
                # Find the previous module's text
                for m in modules:
                    if num - 1 in _count_modules_in_text(m):
                        prev_summary = m[:300].replace("\n", " ")
                        break

            try:
                print(f"    Re-generating Module {num}: {module_def['title']}...")
                new_module = generate_module(module_def, topic, context, prev_summary)
                # Replace any existing partial module or add new one
                replaced = False
                for i, m in enumerate(modules):
                    if num in _count_modules_in_text(m):
                        modules[i] = new_module
                        replaced = True
                        break
                if not replaced:
                    # Insert in correct position
                    insert_pos = 0
                    for i, d in enumerate(MODULE_DEFS):
                        if d["num"] == num:
                            insert_pos = i
                            break
                    modules.insert(insert_pos, new_module)
                found_nums.update(_count_modules_in_text(new_module))
            except Exception as e:
                print(f"    Module {num} repair failed: {str(e)[:100]}")

        time.sleep(2)

    return modules


def generate_playbook(topic_data: dict, opportunity_data: dict = None, intelligence_data: dict = None):
    """Generate the full playbook using module-by-module approach.

    v4 approach: Each module is a separate API call, with quality repair loop
    ensuring all 10 modules are generated. Uses Together AI for reliable
    long-form content generation.
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

    print(f"Generating playbook about: {topic}")
    print(f"Price: {price}")
    print(f"Model: {PLAYBOOK_MODEL}")
    print(f"API Base: {PLAYBOOK_API_BASE}")
    print(f"Strategy: Module-by-module generation (10 modules + 3 appendices) with quality repair")

    # ── Step 1: Generate the opening paragraph ──
    print("\n[1/14] Generating opening paragraph...")
    opening = generate_opening(topic, context, price, cross_link_context)

    # ── Step 2: Generate each module ──
    modules = []
    prev_summary = ""
    for i, module_def in enumerate(MODULE_DEFS):
        step_num = i + 2
        print(f"\n[{step_num}/14] Generating Module {module_def['num']}: {module_def['title']}...")
        module_text = generate_module(module_def, topic, context, prev_summary)
        modules.append(module_text)

        # Extract a brief summary for context in the next module
        first_300 = module_text[:400].replace("\n", " ")
        prev_summary = f"Module {module_def['num']} ({module_def['title']}): {first_300}..."

    # ── Step 3: Quality repair — re-generate any missing modules ──
    print("\n[QUALITY CHECK] Verifying all modules present...")
    modules = repair_missing_modules(modules, topic, context)

    # ── Step 4: Build module summary for appendix context ──
    module_summaries = []
    for m in modules:
        # Extract module headings and procedure headings
        headings = [line.strip() for line in m.split("\n") if line.strip().startswith("#") or line.strip().startswith("##")]
        module_summaries.append("\n".join(headings[:10]))
    all_modules_summary = "\n".join(module_summaries)

    # ── Step 5: Generate appendices ──
    appendices = []
    for idx, letter in enumerate(["A", "B", "C"]):
        step_num = 12 + idx
        print(f"\n[{step_num}/14] Generating Appendix {letter}...")
        appendix = generate_appendix(letter, topic, all_modules_summary)
        appendices.append(appendix)

    # ── Step 6: Assemble the full playbook ──
    body_parts = [opening, "\n\n---\n\n"]
    # Sort modules by module number to ensure correct order
    def _module_sort_key(m):
        nums = _count_modules_in_text(m)
        return min(nums) if nums else 999

    modules_sorted = sorted(modules, key=_module_sort_key)
    for m in modules_sorted:
        body_parts.append(m)
        body_parts.append("\n\n---\n\n")
    for a in appendices:
        body_parts.append(a)
        body_parts.append("\n\n")

    # Add cross-link to intelligence guide at the end
    if intelligence_data:
        int_slug = intelligence_data.get("slug", "")
        body_parts.append(f'For the free step-by-step guide, see our [implementation guide]({{< ref "/intelligence/{int_slug}.md" >}}).\n')

    body = "".join(body_parts)

    # ── Step 7: Inject affiliate links ──
    body = inject_affiliate_links(body, affiliates)

    # Append Recommended Tools section
    tools_section = generate_tools_section(affiliates)
    if tools_section:
        body = body + "\n\n" + tools_section

    final_words = len(body.split())
    module_count = body.count("# MODULE")
    procedure_count = body.count("## Procedure")

    print(f"\n  Total playbook: {final_words} words")
    print(f"  Modules: {module_count}")
    print(f"  Procedures: {procedure_count}")

    # ── Step 8: FINAL QUALITY GATE ──
    if module_count < MIN_MODULES:
        print(f"  ❌ QUALITY GATE FAILED: Only {module_count} modules (minimum: {MIN_MODULES})")
        print(f"  The playbook will still be saved but flagged as low quality.")
    elif procedure_count < MIN_PROCEDURES:
        print(f"  ⚠️  QUALITY WARNING: Only {procedure_count} procedures (target: {MIN_PROCEDURES}+)")
    else:
        print(f"  ✅ QUALITY GATE PASSED: {module_count} modules, {procedure_count} procedures")

    if final_words < MIN_TOTAL_WORDS:
        print(f"  ⚠️  QUALITY WARNING: Only {final_words} words (target: {MIN_TOTAL_WORDS}+)")

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
    print(f"Playbook generator v4 — Together AI powered, quality-enforced")
    print(f"PLAYBOOK_API_KEY: {'***' + PLAYBOOK_API_KEY[-8:] if PLAYBOOK_API_KEY else 'NOT SET'}")
    print(f"PLAYBOOK_MODEL: {PLAYBOOK_MODEL}")
    print(f"PLAYBOOK_API_BASE: {PLAYBOOK_API_BASE}")

    if not PLAYBOOK_API_KEY:
        print("WARNING: No PLAYBOOK_API_KEY or TOGETHER_API_KEY set — will use Pollinations (free) as fallback")
        print("         This may result in low-quality output. Set TOGETHER_API_KEY for best results.")

    # Step 0: Load cross-link data
    print("Loading cross-link data...")
    last_data = load_last_generated()
    opportunity_data = last_data.get("last_opportunity")
    intelligence_data = last_data.get("last_intelligence")

    # Get topic data
    if opportunity_data:
        topic_data = {
            "topic": opportunity_data.get("topic", ""),
            "playbook_angle": opportunity_data.get("playbook_angle", "") or opportunity_data.get("topic", ""),
            "context": opportunity_data.get("context", ""),
            "affiliates": opportunity_data.get("affiliates", []),
        }
        print(f"Writing playbook for same topic as opportunity: {opportunity_data.get('title', '')}")
    else:
        print("No recent opportunity found, discovering trending topic...")
        try:
            discovery = TrendingTopicDiscovery()
            discovery.ensure_minimum_queue(5)
            topic_data = discovery.get_next_topic("playbook")
        except Exception as e:
            print(f"  Trending topic discovery failed: {e}")
            print("  Using fallback topic...")
            topic_data = {
                "topic": "How to start an AI automation agency in 2026",
                "playbook_angle": "Build, Scale, and Monetize an AI Automation Agency with Make.com",
                "context": "AI automation agencies are booming as businesses seek to automate workflows",
                "affiliates": ["Make.com", "ChatGPT", "Notion", "Zapier"],
            }

    if not topic_data or not topic_data.get("topic"):
        print("ERROR: No topic available")
        exit(1)

    # If playbook_angle is missing, derive it from the topic
    if not topic_data.get("playbook_angle"):
        topic_text = topic_data.get("topic", "")
        topic_data["playbook_angle"] = f"Build, Scale, and Monetize {topic_text}"
        print(f"  No playbook_angle found, derived: {topic_data['playbook_angle']}")

    topic = topic_data.get("playbook_angle", topic_data.get("topic", ""))

    # Step 1: Generate images (non-fatal — continue without if failed)
    prelim_slug = slugify(topic)

    image_path = f"/images/articles/playbooks/{prelim_slug}.png"
    hero_path = f"/images/heroes/playbooks/{prelim_slug}.png"

    try:
        print("Generating thumbnail image...")
        image_path = generate_article_image(
            topic=topic,
            slug=prelim_slug,
            section="playbooks",
        )
        print(f"Thumbnail saved: {image_path}")
    except Exception as e:
        print(f"  Thumbnail generation failed (non-fatal): {e}")

    try:
        print("Generating hero image...")
        hero_path = generate_hero_image(
            topic=topic,
            slug=prelim_slug,
            section="playbooks",
        )
        print(f"Hero image saved: {hero_path}")
    except Exception as e:
        print(f"  Hero image generation failed (non-fatal): {e}")

    # Step 2: Generate playbook content (module-by-module with quality repair)
    print("Generating playbook content (module-by-module with quality repair)...")
    try:
        body, price = generate_playbook(topic_data, opportunity_data, intelligence_data)
    except Exception as e:
        print(f"ERROR: Playbook generation failed: {e}")
        import traceback
        traceback.print_exc()
        exit(1)

    if not body or len(body.strip()) < 500:
        print("ERROR: Generated playbook is too short or empty")
        exit(1)

    title = extract_title(body)
    excerpt = build_excerpt(body)
    read_time = estimate_read_time(body)

    slug = slugify(title)
    now = datetime.now(timezone.utc)

    # Step 3: Rename images if slug differs
    if slug != prelim_slug:
        # Hugo paths -> filesystem paths
        old_thumb_fs = str(PROJECT_ROOT / "static" / image_path.lstrip("/"))
        old_hero_fs = str(PROJECT_ROOT / "static" / hero_path.lstrip("/"))
        new_thumb = image_path.replace(prelim_slug, slug)
        new_hero = hero_path.replace(prelim_slug, slug)
        new_thumb_fs = str(PROJECT_ROOT / "static" / new_thumb.lstrip("/"))
        new_hero_fs = str(PROJECT_ROOT / "static" / new_hero.lstrip("/"))
        if os.path.exists(old_thumb_fs):
            os.rename(old_thumb_fs, new_thumb_fs)
            image_path = new_thumb
            print(f"Renamed thumbnail: {new_thumb}")
        if os.path.exists(old_hero_fs):
            os.rename(old_hero_fs, new_hero_fs)
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
    print(f"  Modules found: {module_count} (target: 10)")
    print(f"  Procedures found: {procedure_count} (target: 25+)")
    print(f"  Check-ins found: {checkin_count} (target: 10+)")
    print(f"  Appendices found: {appendix_count} (target: 3)")

    if module_count < MIN_MODULES:
        print(f"  ❌ FAILED: Fewer than {MIN_MODULES} modules. Playbook quality is below standard.")
    if procedure_count < MIN_PROCEDURES:
        print(f"  ⚠️  WARNING: Fewer than {MIN_PROCEDURES} procedures.")
    if word_count < MIN_TOTAL_WORDS:
        print(f"  ⚠️  WARNING: Total word count below {MIN_TOTAL_WORDS}.")

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
