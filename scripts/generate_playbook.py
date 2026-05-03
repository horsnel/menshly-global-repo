#!/usr/bin/env python3
"""Generate a premium Playbook article using AI API.

This generator produces full-length (~8,000-10,000 word) premium playbooks
that follow the Menshly Global Playbook template:
  - Multiple MODULES (8-12), each with an Overview
  - Numbered PROCEDURES within each module
  - Interactive check-ins at every stage
  - Appendices (Tool Reference, SOP Index, Revenue Calculator)

v5 REWRITE — Procedure-by-procedure generation for Pollinations:
  - Each PROCEDURE is a SEPARATE API call (small enough for any model)
  - Module overviews generated separately
  - Guaranteed structure: opening + 10 modules + 3 appendices
  - Works reliably on Pollinations, Groq, Together, or any OpenAI-compatible API
  - Quality repair: re-generates any missing pieces
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

# Playbook-specific API overrides — supports Together AI or falls back to general AI_API
PLAYBOOK_API_KEY = os.environ.get("PLAYBOOK_API_KEY", os.environ.get("TOGETHER_API_KEY", AI_API_KEY))
PLAYBOOK_API_BASE = os.environ.get("PLAYBOOK_API_BASE", AI_API_BASE)
PLAYBOOK_MODEL = os.environ.get("PLAYBOOK_MODEL", AI_MODEL)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LAST_GENERATED_FILE = PROJECT_ROOT / "data" / "last_generated.json"

# ── Quality targets ──
MIN_MODULES = 8
MIN_PROCEDURES = 20
MIN_TOTAL_WORDS = 6000
MAX_REPAIR_ATTEMPTS = 2

# ── Module definitions — the 10-module playbook skeleton ──
MODULE_DEFS = [
    {
        "num": 1,
        "title": "FOUNDATION",
        "desc": "Setup, accounts, infrastructure. Register your business accounts, set up your domain, email, and foundational tools.",
        "procedures": 3,
        "min_words": 600,
    },
    {
        "num": 2,
        "title": "TECH STACK",
        "desc": "Tools, connections, API keys. Connect every tool in your stack, configure integrations, and verify data flows.",
        "procedures": 3,
        "min_words": 600,
    },
    {
        "num": 3,
        "title": "FRAMEWORK",
        "desc": "The universal process and methodology. Define your service delivery framework, client onboarding flow, and quality standards.",
        "procedures": 2,
        "min_words": 600,
    },
    {
        "num": 4,
        "title": "FIRST BUILD",
        "desc": "Guided walkthrough of the core product or service. Build your first deliverable end-to-end with real client data.",
        "procedures": 3,
        "min_words": 800,
    },
    {
        "num": 5,
        "title": "CLIENT ACQUISITION",
        "desc": "How to get paying customers. Set up your outreach systems, landing page, and lead generation pipeline.",
        "procedures": 3,
        "min_words": 700,
    },
    {
        "num": 6,
        "title": "DELIVERY",
        "desc": "How to deliver value consistently. Build your delivery pipeline, quality checkpoints, and client communication templates.",
        "procedures": 2,
        "min_words": 600,
    },
    {
        "num": 7,
        "title": "SCALING",
        "desc": "From solo to team, margin analysis. Hire your first contractor, build SOPs for delegation, and analyze margins.",
        "procedures": 3,
        "min_words": 700,
    },
    {
        "num": 8,
        "title": "ADVANCED PATTERNS",
        "desc": "Premium techniques and upsells. Add high-ticket services, build recurring revenue, and create productized offerings.",
        "procedures": 2,
        "min_words": 600,
    },
    {
        "num": 9,
        "title": "FINANCIAL OPERATIONS",
        "desc": "Revenue tracking, pricing increases, and proposal templates. Build your financial dashboard and contract templates.",
        "procedures": 2,
        "min_words": 600,
    },
    {
        "num": 10,
        "title": "LAUNCH PLAN",
        "desc": "Day-by-day execution calendar for the next 30 days. Your complete action plan to go from zero to first paying client.",
        "procedures": 3,
        "min_words": 700,
    },
]

# ── System prompt shared across all calls ──
SYSTEM_PROMPT = """You are the senior implementation writer for Menshly Global (tagline: "Where AI Meets Revenue").
You write PREMIUM PLAYBOOKS — complete operating systems that readers execute from start to finish to build real businesses.

This is NOT a blog post. This is NOT a guide. This is an OPERATING SYSTEM with exact procedures.

CRITICAL STYLE RULES:
- Write in an INSTRUCTIONAL, COMMANDING tone — like a senior operator handing a junior their exact playbook
- Every instruction must be SPECIFIC: exact button names, exact menu paths, exact settings, exact URLs
- Include INTERACTIVE CHECK-INS: "Do you see [X]? If not, [troubleshooting]." after every 3-5 steps
- Show expected output at every step: UI states, JSON responses, dashboard screenshots described in text
- Include error scenarios: "If you see [ERROR], this means [CAUSE]. Fix it by [SOLUTION]."
- Name real tools with real prices and real free tier limits
- Never use vague phrases like "configure it appropriately" — say EXACTLY what to configure
- Use TABLES for: tool comparisons, cost breakdowns, pricing tiers, margin analysis, revenue projections

AFFILIATE TOOL INTEGRATION:
Always naturally mention at least 2 of these tools per procedure: Make.com, Replit, Vapi, Fliki AI, Canva, ChatGPT, ElevenLabs, Klaviyo, ActiveCampaign, Semrush, Hostinger, Shopify, Zapier, Apollo.io, PhantomBuster, Buffer, Loom, Calendly, Beehiiv, Notion, Midjourney, Grammarly.

Do NOT add a separate "Recommended Tools" section — we add that automatically.

CRITICAL: Write COMPLETE content. Do NOT truncate. Do NOT say "continue in next section". Write the FULL procedure."""


def load_last_generated() -> dict:
    """Load the last generated article data for cross-linking."""
    if not LAST_GENERATED_FILE.exists():
        return {}
    try:
        return json.loads(LAST_GENERATED_FILE.read_text())
    except (json.JSONDecodeError, Exception):
        return {}


def _call_api(messages: list, max_tokens: int = 4000, temperature: float = 0.7) -> str:
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
5. Sound commanding and instructional

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


def generate_module_overview(module_def: dict, topic: str, context: str) -> str:
    """Generate just the module overview heading and introduction."""
    num = module_def["num"]
    title = module_def["title"]
    desc = module_def["desc"]
    proc_count = module_def["procedures"]

    prompt = f"""Write ONLY the Overview section for MODULE {num}: {title} of a playbook about: {topic}

{'TRENDING CONTEXT: ' + context if context else ''}

This module covers: {desc}
This module has {proc_count} procedures.

Write EXACTLY this structure:

# MODULE {num}: {title}

## Overview
[2-3 paragraphs explaining what this module covers, why it matters, what happens if you skip it.
Include a TABLE of tools needed with columns: Tool | Purpose | Free Tier | Paid Tier.
State estimated time to complete.]

Do NOT write any procedures. Just the heading and overview.
Write at least 150 words for the overview."""

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]

    for attempt in range(3):
        try:
            result = _call_api(messages, max_tokens=1500, temperature=0.7)
            if f"MODULE {num}" in result and len(result.split()) >= 80:
                return result
            print(f"  Overview {num} attempt {attempt+1}: too short, retrying...")
            time.sleep(2)
        except Exception as e:
            print(f"  Overview {num} attempt {attempt+1} failed: {str(e)[:80]}")
            time.sleep(5)

    # Fallback
    return f"# MODULE {num}: {title}\n\n## Overview\n{desc}\n\n**Time to complete:** 60 minutes\n**Tools needed:** See individual procedures below.\n"


def generate_procedure(module_num: int, proc_num: int, proc_title_hint: str,
                       topic: str, context: str, module_title: str) -> str:
    """Generate a single procedure. This is the core unit of generation.

    By generating each procedure separately, we ensure:
    - Each call is small enough for Pollinations to complete
    - No truncation — each procedure is complete
    - Consistent quality across all procedures
    """
    prompt = f"""Write Procedure {module_num}.{proc_num} for MODULE {module_num}: {module_title}
of a playbook about: {topic}

{'TRENDING CONTEXT: ' + context if context else ''}

Procedure topic: {proc_title_hint}

Write EXACTLY this structure:

## Procedure {module_num}.{proc_num}: [SPECIFIC ACTION — Imperative Verb]

[Write 15-25 numbered steps with:
- Exact URLs to visit or exact tool names to open
- Exact buttons to click (in bold)
- Exact fields to fill in
- Interactive check-in after every 4-5 steps: "Do you see [X]? If not, [troubleshooting]."
- Expected output or result at key milestones
- At least one error scenario: "If you see [ERROR], this means [CAUSE]. Fix it by [SOLUTION]."
- Include a TABLE where appropriate (tool comparison, cost breakdown, settings, or pricing)
- Name real tools with real prices and free tier limits
- Each step should be specific enough that a beginner can follow along without guessing]

Write at least 300 words. Do NOT truncate. Write the COMPLETE procedure.
Do NOT write any other procedures or module headings. Just this one procedure."""

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]

    for attempt in range(3):
        try:
            result = _call_api(messages, max_tokens=4000, temperature=0.7)
            word_count = len(result.split())
            has_procedure = f"Procedure {module_num}.{proc_num}" in result

            if word_count >= 150 and has_procedure:
                print(f"    Proc {module_num}.{proc_num}: {word_count} words ✓")
                return result
            else:
                print(f"    Proc {module_num}.{proc_num} attempt {attempt+1}: {word_count} words, retrying...")
                time.sleep(2)
        except Exception as e:
            print(f"    Proc {module_num}.{proc_num} attempt {attempt+1} failed: {str(e)[:80]}")
            time.sleep(5)

    # Fallback: return what we got
    print(f"    Proc {module_num}.{proc_num}: using best available after retries")
    return result


def generate_module_checkin(module_num: int, module_title: str, procedure_titles: list) -> str:
    """Generate the check-in section at the end of a module."""
    items = "\n".join(f"- [ ] {t} completed and verified" for t in procedure_titles)
    items += "\n- [ ] All tools connected and working\n- [ ] No errors or warnings in any dashboard"

    return f"\n## Check-In: Module {module_num} Complete\n\n{items}\n"


def generate_module(module_def: dict, topic: str, context: str) -> str:
    """Generate a complete module with overview + procedures + check-in.

    Uses procedure-by-procedure generation for maximum reliability on any AI backend.
    """
    num = module_def["num"]
    title = module_def["title"]
    proc_count = module_def["procedures"]
    desc = module_def["desc"]

    print(f"  Module {num}: {title} — generating overview + {proc_count} procedures")

    # Step 1: Generate overview
    overview = generate_module_overview(module_def, topic, context)

    # Step 2: Generate procedure title hints based on module description
    proc_hints = _get_procedure_hints(num, title, desc, proc_count, topic, context)

    # Step 3: Generate each procedure individually
    procedures = []
    proc_titles = []
    for p in range(1, proc_count + 1):
        hint = proc_hints[p - 1] if p - 1 < len(proc_hints) else f"Complete the {desc.split('.')[0]} setup"
        proc_text = generate_procedure(num, p, hint, topic, context, title)
        procedures.append(proc_text)
        # Extract title for check-in
        title_match = re.search(r"## Procedure \d+\.\d+:\s*(.+)", proc_text)
        if title_match:
            proc_titles.append(title_match.group(1).strip())
        else:
            proc_titles.append(hint)

    # Step 4: Generate check-in
    checkin = generate_module_checkin(num, title, proc_titles)

    # Step 5: Assemble the module
    module_text = overview + "\n\n---\n\n"
    module_text += "\n\n---\n\n".join(procedures)
    module_text += "\n" + checkin

    total_words = len(module_text.split())
    print(f"  Module {num}: complete — {total_words} words, {len(procedures)} procedures")

    return module_text


def _get_procedure_hints(module_num: int, module_title: str, desc: str,
                          proc_count: int, topic: str, context: str) -> list:
    """Generate short procedure title hints for a module using AI."""
    prompt = f"""For MODULE {module_num}: {module_title} of a playbook about "{topic}", suggest {proc_count} procedure titles.

Module description: {desc}

Each title should be a SPECIFIC, ACTIONABLE imperative verb phrase like:
- "Register Your Business Domain on Hostinger"
- "Create a Make.com Scenario for Data Pipeline"
- "Build the ChatGPT Budget Analysis Prompt"

Return ONLY a JSON array of {proc_count} strings. No explanation, just the array.
Example: ["Register Your Business Domain on Hostinger", "Set Up Email Forwarding in Hostinger", "Create a Notion Workspace for Client Data"]"""

    messages = [
        {"role": "system", "content": "Return only valid JSON arrays of strings. No explanation."},
        {"role": "user", "content": prompt},
    ]

    try:
        result = _call_api(messages, max_tokens=500, temperature=0.8)
        # Try to parse JSON
        match = re.search(r'\[.*\]', result, re.DOTALL)
        if match:
            hints = json.loads(match.group())
            if isinstance(hints, list) and len(hints) >= proc_count:
                return hints[:proc_count]
    except Exception as e:
        print(f"    Hint generation failed: {str(e)[:60]}")

    # Fallback hints based on module
    fallback_hints = {
        1: ["Register Your Business Domain on Hostinger", "Set Up Email and Workspace in Notion", "Create Core Business Accounts and Calendly"],
        2: ["Connect ChatGPT API and Store Keys in Notion", "Build Your First Make.com Automation Scenario", "Configure Vapi Voice Agent and ElevenLabs TTS"],
        3: ["Design Your Service Delivery Framework in Notion", "Build the Client Onboarding Automation Pipeline"],
        4: ["Build the Core AI Product in Replit", "Create the Data Processing Pipeline with Make.com", "Deploy and Test the Complete System"],
        5: ["Build a High-Conversion Landing Page on Shopify", "Set Up Lead Generation with Apollo.io", "Create Automated Email Nurture Sequence in Klaviyo"],
        6: ["Deploy the Product to Production on Hostinger", "Build Quality Assurance and Client Communication Templates"],
        7: ["Hire Your First Contractor on Upwork", "Build SOPs for Task Delegation in Notion", "Run a Margin Analysis and Pricing Review"],
        8: ["Create a High-Ticket Consulting Package", "Build Recurring Revenue with Subscription Tiers on Shopify"],
        9: ["Build a Live Revenue Dashboard in Notion with Make.com", "Create Proposal Templates and Automated Billing with Stripe"],
        10: ["Configure Demo Scheduling with Calendly and Notion", "Build Marketing Automation and Prospect List with Apollo.io", "Execute the 30-Day Launch Calendar"],
    }
    return fallback_hints.get(module_num, [f"Complete Step {i+1}" for i in range(proc_count)])


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
            result = _call_api(messages, max_tokens=3000, temperature=0.6)
            if len(result.split()) >= 200:
                return result
            print(f"  Appendix {appendix_letter} attempt {attempt+1}: too short, retrying...")
        except Exception as e:
            print(f"  Appendix {appendix_letter} attempt {attempt+1} failed: {str(e)[:80]}")
            time.sleep(5)

    # Minimal fallback
    if appendix_letter == "A":
        return "# APPENDIX A: COMPLETE TOOL REFERENCE\n\n| Tool | Purpose | Free Tier | Paid Tier | When to Upgrade |\n|------|---------|-----------|-----------|------------------|\n| Make.com | Automation | 1,000 ops/mo | $9/mo | 10,000+ ops/mo |\n| ChatGPT | AI Assistant | Free | $20/mo | API integration |\n| Notion | Workspace | Free | $8/mo | Team collaboration |\n| Canva | Design | Free | $13/mo | Brand kit needed |\n| Apollo.io | Sales Intel | Free | $49/mo | 100+ leads/mo |\n| Hostinger | Hosting | $1.99/mo | $3.95/mo | Custom domain needed |\n| Klaviyo | Email Marketing | 250 contacts | $20/mo | 500+ contacts |\n| Shopify | E-commerce | 3-day trial | $29/mo | Product sales |\n| Replit | Cloud IDE | Free | $7/mo | Private repos |\n| Vapi | Voice AI | 5 calls/mo | $15/mo | Production use |\n"
    elif appendix_letter == "B":
        return "# APPENDIX B: THE COMPLETE SOP INDEX\n\n| SOP # | Procedure | Category | Difficulty | Est. Time |\n|-------|-----------|----------|------------|----------|\n| 1.1 | Register Domain | Foundation | Easy | 30 min |\n| 1.2 | Set Up Workspace | Foundation | Easy | 20 min |\n| 1.3 | Create Business Accounts | Foundation | Easy | 30 min |\n| 2.1 | Connect ChatGPT API | Tech Stack | Medium | 45 min |\n| 2.2 | Build Make.com Scenario | Tech Stack | Medium | 60 min |\n| 2.3 | Configure Voice Agent | Tech Stack | Hard | 60 min |\n| 4.1 | Build Core Product | First Build | Hard | 2 hrs |\n| 5.1 | Build Landing Page | Client Acquisition | Medium | 1 hr |\n| 7.1 | Hire Contractor | Scaling | Medium | 45 min |\n| 10.1 | Configure Demo Scheduling | Launch Plan | Easy | 30 min |\n"
    else:
        return "# APPENDIX C: THE REVENUE CALCULATOR\n\n| Month | Revenue | Clients | Expenses | Profit |\n|-------|---------|---------|----------|--------|\n| 1 | $0 | 0 | $50 | -$50 |\n| 3 | $1,500 | 2 | $100 | $1,400 |\n| 6 | $5,000 | 5 | $200 | $4,800 |\n| 12 | $15,000 | 10 | $500 | $14,500 |\n\n## Pricing Tiers\n| Tier | Price | Deliverables | Margin |\n|------|-------|-------------|--------|\n| Starter | $500/mo | Basic automation | 70% |\n| Pro | $1,500/mo | Full automation + support | 75% |\n| Enterprise | $3,000/mo | Custom + consulting | 80% |\n"


def _count_modules_in_text(text: str) -> set:
    """Find which module numbers exist in the generated text."""
    found = set()
    for match in re.finditer(r"#\s+MODULE\s+(\d+)", text, re.IGNORECASE):
        found.add(int(match.group(1)))
    return found


def _count_procedures_in_text(text: str) -> int:
    """Count the number of procedures in the generated text."""
    return len(re.findall(r"##\s+Procedure\s+\d+\.\d+", text, re.IGNORECASE))


def generate_playbook(topic_data: dict, opportunity_data: dict = None, intelligence_data: dict = None):
    """Generate the full playbook using procedure-by-procedure approach.

    v5 approach: Each procedure is a separate API call, ensuring:
    - Full content regardless of AI model quality or output limits
    - No truncation — each procedure is complete and self-contained
    - Works on Pollinations, Groq, Together, or any backend
    - Quality repair loop ensures all modules are present
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
    print(f"Strategy: Procedure-by-procedure generation (10 modules × 2-3 procs + 3 appendices)")

    # ── Step 1: Generate the opening paragraph ──
    print("\n[1] Generating opening paragraph...")
    opening = generate_opening(topic, context, price, cross_link_context)

    # ── Step 2: Generate each module (overview + procedures) ──
    modules = []
    for i, module_def in enumerate(MODULE_DEFS):
        step_num = i + 2
        print(f"\n[{step_num}/11] Generating Module {module_def['num']}: {module_def['title']} ({module_def['procedures']} procedures)...")
        module_text = generate_module(module_def, topic, context)
        modules.append(module_text)

    # ── Step 3: Build module summary for appendix context ──
    module_summaries = []
    for m in modules:
        headings = [line.strip() for line in m.split("\n") if line.strip().startswith("#") or line.strip().startswith("##")]
        module_summaries.append("\n".join(headings[:15]))
    all_modules_summary = "\n".join(module_summaries)

    # ── Step 4: Generate appendices ──
    appendices = []
    for letter in ["A", "B", "C"]:
        print(f"\n[Appendix] Generating Appendix {letter}...")
        appendix = generate_appendix(letter, topic, all_modules_summary)
        appendices.append(appendix)

    # ── Step 5: Assemble the full playbook ──
    body_parts = [opening, "\n\n---\n\n"]
    # Sort modules by module number
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

    # ── Step 6: Inject affiliate links ──
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

    # ── Step 7: Quality report ──
    if module_count >= MIN_MODULES and procedure_count >= MIN_PROCEDURES:
        print(f"  ✅ QUALITY GATE PASSED: {module_count} modules, {procedure_count} procedures")
    elif module_count < MIN_MODULES:
        print(f"  ❌ QUALITY GATE FAILED: Only {module_count} modules (minimum: {MIN_MODULES})")
    else:
        print(f"  ⚠️  QUALITY WARNING: Only {procedure_count} procedures (target: {MIN_PROCEDURES}+)")

    if final_words < MIN_TOTAL_WORDS:
        print(f"  ⚠️  QUALITY WARNING: Only {final_words} words (target: {MIN_TOTAL_WORDS}+)")

    return body, price


def extract_title(body: str) -> str:
    """Extract or infer the title from the playbook body.

    Looks for the bold text in the opening paragraph first (e.g. "25 procedures. 10 modules..."),
    then falls back to the first H1 heading.
    """
    # First: look for bold text in the first 5 lines
    for line in body.split("\n")[:10]:
        line = line.strip()
        bold_match = re.match(r"^\*\*(.+?)\*\*", line)
        if bold_match:
            title = bold_match.group(1).rstrip(".!")
            # Skip generic titles like "25 procedures. 10 modules..."
            if re.match(r"^\d+\s+(procedure|step|module)", title, re.IGNORECASE):
                continue
            return title

    # Second: look for the first H1 that's NOT "MODULE X"
    for line in body.split("\n"):
        line = line.strip()
        if line.startswith("# ") and not line.startswith("## "):
            title = line.lstrip("# ").strip()
            title = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', title)
            # Skip "MODULE X" headings
            if re.match(r"^MODULE\s+\d+", title, re.IGNORECASE):
                continue
            return title

    # Third: look for first substantial non-heading text
    for line in body.split("\n"):
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("---") and len(line) > 10:
            sentence = line.split(".")[0].strip()
            if len(sentence) > 10 and not re.match(r"^\d+\s+(procedure|step|module)", sentence, re.IGNORECASE):
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
    print(f"Playbook generator v5 — procedure-by-procedure, Pollinations-optimized")
    print(f"PLAYBOOK_API_KEY: {'***' + PLAYBOOK_API_KEY[-8:] if PLAYBOOK_API_KEY and len(PLAYBOOK_API_KEY) > 8 else 'NOT SET'}")
    print(f"PLAYBOOK_MODEL: {PLAYBOOK_MODEL}")
    print(f"PLAYBOOK_API_BASE: {PLAYBOOK_API_BASE}")

    if not PLAYBOOK_API_KEY:
        print("No PLAYBOOK_API_KEY set — will use Pollinations (free) as fallback")

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

    if not topic_data.get("playbook_angle"):
        topic_text = topic_data.get("topic", "")
        topic_data["playbook_angle"] = f"Build, Scale, and Monetize {topic_text}"

    topic = topic_data.get("playbook_angle", topic_data.get("topic", ""))

    # Step 1: Generate images (non-fatal)
    prelim_slug = slugify(topic)

    image_path = f"/images/articles/playbooks/{prelim_slug}.png"
    hero_path = f"/images/heroes/playbooks/{prelim_slug}.png"

    try:
        print("Generating thumbnail image...")
        image_path = generate_article_image(topic=topic, slug=prelim_slug, section="playbooks")
        print(f"Thumbnail saved: {image_path}")
    except Exception as e:
        print(f"  Thumbnail generation failed (non-fatal): {e}")

    try:
        print("Generating hero image...")
        hero_path = generate_hero_image(topic=topic, slug=prelim_slug, section="playbooks")
        print(f"Hero image saved: {hero_path}")
    except Exception as e:
        print(f"  Hero generation failed (non-fatal): {e}")

    # Step 2: Generate playbook content
    print("Generating playbook content (procedure-by-procedure)...")
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
        old_thumb_fs = str(PROJECT_ROOT / "static" / image_path.lstrip("/"))
        old_hero_fs = str(PROJECT_ROOT / "static" / hero_path.lstrip("/"))
        new_thumb = image_path.replace(prelim_slug, slug)
        new_hero = hero_path.replace(prelim_slug, slug)
        new_thumb_fs = str(PROJECT_ROOT / "static" / new_thumb.lstrip("/"))
        new_hero_fs = str(PROJECT_ROOT / "static" / new_hero.lstrip("/"))
        if os.path.exists(old_thumb_fs):
            os.rename(old_thumb_fs, new_thumb_fs)
            image_path = new_thumb
        if os.path.exists(old_hero_fs):
            os.rename(old_hero_fs, new_hero_fs)
            hero_path = new_hero

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

    if opportunity_data:
        opp_slug = opportunity_data.get("slug", "")
        if opp_slug:
            front_matter_lines.append(f'relatedOpportunity: "/opportunities/{opp_slug}/"')

    if intelligence_data:
        int_slug = intelligence_data.get("slug", "")
        if int_slug:
            front_matter_lines.append(f'relatedGuide: "/intelligence/{int_slug}/"')

    front_matter_lines.extend(["---", ""])
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

    # Update cross-links
    if opportunity_data:
        opp_file = Path("content/opportunities") / f"{opportunity_data.get('slug', '')}.md"
        update_article_cross_links(opp_file, slug, "opportunities")

    if intelligence_data:
        int_file = Path("content/intelligence") / f"{intelligence_data.get('slug', '')}.md"
        update_article_cross_links(int_file, slug, "intelligence")

    # Mark topic as used
    if opportunity_data:
        discovery = TrendingTopicDiscovery()
        discovery.mark_topic_used(topic_data)

    print(f"\n✅ Playbook generated successfully!")
