#!/usr/bin/env python3
"""Bulk generate 5 opportunity + 5 intelligence articles using Pollinations API.

Uses the direct Pollinations text API for clean, long-form content.
Generates images using the existing image_utils module.
Applies affiliate links using the affiliate_injector module.
"""

import os
import re
import json
import time
import requests
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

from image_utils import generate_article_image, generate_hero_image
from affiliate_injector import inject_affiliate_links, generate_tools_section

PROJECT_ROOT = Path(__file__).resolve().parent.parent
POLLINATIONS_DIRECT = "https://text.pollinations.ai/"
POLLINATIONS_OPENAI = "https://text.pollinations.ai/openai/chat/completions"

# ── Article Topics ─────────────────────────────────────────────────────

OPPORTUNITY_TOPICS = [
    {
        "topic": "AI Voice Agent Agency",
        "title": "How to Start an AI Voice Agent Agency in 2026 ($5K-30K/Month)",
        "slug": "ai-voice-agent-agency-2026",
        "excerpt": "Businesses are replacing phone trees with AI voice agents — and they'll pay you $5K+ per month to build, deploy, and manage them. Here's the full breakdown with every tool, hack, and ugly truth.",
        "intelligence_title": "Build, Deploy, and Scale AI Voice Agents with Vapi: The Complete Step-by-Step Guide",
        "intelligence_slug": "build-deploy-scale-ai-voice-agents-vapi",
        "affiliates": ["Vapi", "Make.com", "Replit", "Calendly", "ElevenLabs", "Notion"],
    },
    {
        "topic": "AI Content Repurposing Agency",
        "title": "How to Start an AI Content Repurposing Agency in 2026 ($3K-15K/Month)",
        "slug": "ai-content-repurposing-agency-2026",
        "excerpt": "Every creator has hours of long-form content sitting unused. You can turn one video into 30 pieces of content with AI — and charge $3K+ per client per month. Here's exactly how.",
        "intelligence_title": "Design, Build, and Automate an AI Content Repurposing Pipeline with Make.com: The Complete Step-by-Step Guide",
        "intelligence_slug": "design-build-automate-ai-content-repurposing-pipeline-makecom",
        "affiliates": ["Make.com", "Canva", "ChatGPT", "Fliki AI", "Buffer", "Beehiiv"],
    },
    {
        "topic": "AI SEO Agency",
        "title": "How to Start an AI SEO Agency in 2026 ($4K-25K/Month)",
        "slug": "ai-seo-agency-2026",
        "excerpt": "Traditional SEO agencies are slow and expensive. You can outrank them using AI-powered workflows that deliver results in weeks, not months. Here's the complete playbook.",
        "intelligence_title": "Build, Optimize, and Scale AI-Powered SEO Workflows with Semrush: The Complete Step-by-Step Guide",
        "intelligence_slug": "build-optimize-scale-ai-seo-workflows-semrush",
        "affiliates": ["Semrush", "Make.com", "ChatGPT", "Grammarly", "Notion", "Hostinger"],
    },
    {
        "topic": "AI SaaS Micro Products",
        "title": "How to Build AI SaaS Micro Products on Replit in 2026 ($2K-20K/Month)",
        "slug": "ai-saas-micro-products-replit-2026",
        "excerpt": "You don't need a team of engineers to build a SaaS product anymore. One person with Replit and AI can ship a micro SaaS in a weekend and scale it to $20K/month. Here's the full blueprint.",
        "intelligence_title": "Design, Build, and Launch AI SaaS Micro Products with Replit: The Complete Step-by-Step Guide",
        "intelligence_slug": "design-build-launch-ai-saas-micro-products-replit",
        "affiliates": ["Replit", "Make.com", "ChatGPT", "Hostinger", "Notion", "Calendly"],
    },
    {
        "topic": "AI Social Media Management Agency",
        "title": "How to Start an AI Social Media Agency in 2026 ($3K-20K/Month)",
        "slug": "ai-social-media-agency-2026",
        "excerpt": "Brands are drowning in content demands — 7 posts a week across 5 platforms. You can serve 10 clients at once using AI workflows that cut production time by 80%. Here's every tool and trick.",
        "intelligence_title": "Build, Automate, and Scale AI Social Media Pipelines with Buffer and Make.com: The Complete Step-by-Step Guide",
        "intelligence_slug": "build-automate-scale-ai-social-media-pipelines-buffer-makecom",
        "affiliates": ["Buffer", "Make.com", "Canva", "Fliki AI", "ChatGPT", "Beehiiv"],
    },
]


# ── System Prompts ─────────────────────────────────────────────────────

OPPORTUNITY_SYSTEM = """You are the lead writer for Menshly Global (tagline: "Where AI Meets Revenue").
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
4 ugly truths formatted as blockquotes:
> **Truth #1:** [harsh reality with specific numbers]

(Repeat for truths 2-4)

## The Free Stack: Starting With Zero Dollars
7 free tools, each as: **Tool Name — $0** — One-line description.
End with a paragraph explaining limitations and when to upgrade.

## The Paid Stack: When You're Ready to Scale
8-10 paid tools, each as: **Tool Name — $X/mo** — One-line description.
End with total monthly cost and ROI analysis.

## The Workflow: Step-by-Step With Every Shortcut
3-4 detailed steps (### Step N: Name (time estimate))
Each step has 2-3 paragraphs of detail + shortcut callout in a blockquote.
Include specific prompts, settings, or configurations where relevant.

## Pricing: What to Charge and How to Defend It
3 pricing tiers (Starter/Growth/Enterprise) with specific dollar amounts and what's included.
One Pricing Trick in a blockquote.

## Getting Clients: The Real Playbook
3 methods with names and conversion rates (### Method N: Name (Conversion Rate: X%))
Each method gets a full paragraph with specific tactics.

## Tricks and Hacks They Don't Share in Courses
5 hacks, each in a blockquote:
> **HACK 1: Name.** Detailed explanation of the trick.

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


INTELLIGENCE_SYSTEM = """You are the technical implementation writer for Menshly Global (tagline: "Where AI Meets Revenue").
You write deep execution guides that readers can follow step-by-step to build real systems.

CRITICAL STYLE RULES:
- Write in an INSTRUCTIONAL, CLINICAL tone — like a senior engineer walking a junior through a build
- NOT the casual/conversational Opportunities tone — Intelligence readers are here to EXECUTE
- Every step must be specific: exact button names, exact menu paths, exact settings
- Include INTERACTIVE CHECK-INS throughout: "You should now have: ✓ X ✓ Y ✓ Z. If you're missing any, go back to [section]."
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
Interactive check-in.

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

WORD COUNT TARGET: 4,000-5,000 words. Every step must be fully detailed.
Do NOT write short sections. Every step needs sub-steps, configurations, and check-ins."""


def call_pollinations_direct(system_prompt, user_prompt, max_retries=3):
    """Call Pollinations direct text API for clean, long content."""
    payload = {
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "model": "openai",
        "seed": int(time.time()) % 10000,
    }
    headers = {"Content-Type": "application/json"}

    for attempt in range(max_retries + 1):
        try:
            print(f"  API call attempt {attempt+1}/{max_retries+1}...")
            resp = requests.post(POLLINATIONS_DIRECT, headers=headers, json=payload, timeout=600)
            if resp.status_code == 429:
                wait = 30 * (attempt + 1)
                print(f"  Rate limited. Waiting {wait}s...")
                time.sleep(wait)
                continue
            resp.raise_for_status()
            return resp.text
        except requests.exceptions.Timeout:
            if attempt < max_retries:
                print(f"  Timeout. Retrying...")
                time.sleep(15)
                continue
            raise RuntimeError("Pollinations API timed out")
        except requests.exceptions.ConnectionError:
            if attempt < max_retries:
                print(f"  Connection error. Retrying...")
                time.sleep(20)
                continue
            raise RuntimeError("Pollinations API connection failed")

    raise RuntimeError("Pollinations API failed after maximum retries")


def extract_title(body):
    """Extract H1 title from markdown."""
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
    return "Untitled"


def slugify(title):
    """Create URL-safe slug."""
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    slug = slug.strip("-")
    return slug[:80]


def build_excerpt(body):
    """Build short excerpt from article body."""
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


def strip_h1(body):
    """Remove H1 title from body."""
    lines = body.split("\n")
    filtered = []
    skipped_h1 = False
    for line in lines:
        if not skipped_h1 and line.strip().startswith("# ") and not line.strip().startswith("## "):
            skipped_h1 = True
            continue
        filtered.append(line)
    return "\n".join(filtered)


def generate_opportunity_article(topic_data):
    """Generate a single opportunity article."""
    topic = topic_data["topic"]
    suggested_title = topic_data["title"]
    slug = topic_data["slug"]
    affiliates = topic_data["affiliates"]

    print(f"\n{'='*60}")
    print(f"Generating OPPORTUNITY: {suggested_title}")
    print(f"{'='*60}")

    # Step 1: Generate images
    image_path = f"/images/articles/opportunities/{slug}.png"
    hero_path = f"/images/heroes/opportunities/{slug}.png"

    try:
        print("Generating thumbnail...")
        image_path = generate_article_image(topic=topic, slug=slug, section="opportunities")
        print(f"  Thumbnail: {image_path}")
    except Exception as e:
        print(f"  Thumbnail failed (non-fatal): {e}")

    try:
        print("Generating hero image...")
        hero_path = generate_hero_image(topic=topic, slug=slug, section="opportunities")
        print(f"  Hero: {hero_path}")
    except Exception as e:
        print(f"  Hero failed (non-fatal): {e}")

    # Step 2: Generate article content
    print("Generating article content...")
    user_prompt = f"""Write a complete deep-dive article about: {topic}

The suggested title is: {suggested_title}

Follow the exact structure and style defined in your system instructions.
This is for the Opportunities category on Menshly Global.
Target audience: entrepreneurs, freelancers, and builders who want to make money with AI.

The title must follow this pattern:
"How to [VERB] [TOPIC] in 2026 ([BENEFIT/REVENUE HOOK])"

Return the article as pure Markdown (no front matter). Begin with the title as an H1.
Make sure the article is at least 5,000 words. Every section must be fully developed."""

    body = call_pollinations_direct(OPPORTUNITY_SYSTEM, user_prompt)

    # If too short, continue
    word_count = len(body.split())
    print(f"  First pass: {word_count} words")

    if word_count < 4500:
        print("  Article too short, continuing...")
        continue_prompt = f"""The previous article was cut off or too short. Here is the last part:

...{body[-1500:]}

CONTINUE the article from where it left off. Do NOT repeat any content. Pick up EXACTLY where it ended.
If you were in the middle of a section, complete it. Then continue with all remaining sections.
Make sure to include: Tricks and Hacks, The Real Numbers (month-by-month table), What Nobody Warns You About, and Start This Weekend.

Write at least 2000 more words."""

        continuation = call_pollinations_direct(OPPORTUNITY_SYSTEM, continue_prompt)
        cont_words = len(continuation.split())
        print(f"  Second pass: {cont_words} words added")
        body = body + "\n\n" + continuation
        word_count = len(body.split())
        print(f"  Total: {word_count} words")

    # Step 3: Process the article
    title = extract_title(body)
    excerpt = build_excerpt(body)
    body_clean = strip_h1(body)

    # Inject affiliate links
    body_clean = inject_affiliate_links(body_clean, affiliates)

    # Append Recommended Tools
    tools_section = generate_tools_section(affiliates)
    if tools_section:
        body_clean = body_clean + "\n\n" + tools_section

    # Build frontmatter
    read_time = max(14, min(22, word_count // 250))
    now = datetime.now(timezone.utc)

    front_matter = f"""---
title: "{title}"
date: {now.strftime("%Y-%m-%d")}
category: "AI Opportunity"
readTime: "{read_time} MIN"
excerpt: "{excerpt}"
image: "{image_path}"
heroImage: "{hero_path}"
relatedGuide: "/intelligence/{topic_data['intelligence_slug']}/"
---

"""

    # Save
    content_dir = Path("content/opportunities")
    content_dir.mkdir(parents=True, exist_ok=True)
    filepath = content_dir / f"{slug}.md"
    filepath.write_text(front_matter + body_clean)

    final_words = len(body_clean.split())
    print(f"  Saved: {filepath}")
    print(f"  Title: {title}")
    print(f"  Word count: ~{final_words}")

    return {"slug": slug, "title": title, "words": final_words}


def generate_intelligence_article(topic_data, opportunity_slug):
    """Generate a single intelligence article linked to an opportunity."""
    topic = topic_data["topic"]
    suggested_title = topic_data["intelligence_title"]
    slug = topic_data["intelligence_slug"]
    opp_slug = topic_data["slug"]
    opp_title = topic_data["title"]
    affiliates = topic_data["affiliates"]

    print(f"\n{'='*60}")
    print(f"Generating INTELLIGENCE: {suggested_title}")
    print(f"{'='*60}")

    # Step 1: Generate images
    image_path = f"/images/articles/intelligence/{slug}.png"
    hero_path = f"/images/heroes/intelligence/{slug}.png"

    try:
        print("Generating thumbnail...")
        image_path = generate_article_image(topic=topic, slug=slug, section="intelligence")
        print(f"  Thumbnail: {image_path}")
    except Exception as e:
        print(f"  Thumbnail failed (non-fatal): {e}")

    try:
        print("Generating hero image...")
        hero_path = generate_hero_image(topic=topic, slug=slug, section="intelligence")
        print(f"  Hero: {hero_path}")
    except Exception as e:
        print(f"  Hero failed (non-fatal): {e}")

    # Step 2: Generate article content
    print("Generating article content...")
    user_prompt = f"""Write a complete step-by-step implementation article about: {topic}

The suggested title is: {suggested_title}

CROSS-LINKING CONTEXT:
This intelligence guide is the IMPLEMENTATION companion to the opportunity article:
"{opp_title}" (URL: /opportunities/{opp_slug}/)

The guide should reference this opportunity in the opening paragraph:
"This is the execution guide for building the {topic} business we outlined in our opportunity deep-dive."

Follow the exact structure and style defined in your system instructions.
This is for the Intelligence category on Menshly Global — deep implementation guides for builders.

The title must use IMPERATIVE VERBS:
Pattern: "[VERB], [VERB], and [VERB] [THING] with [TOOL]: The Complete Step-by-Step Guide"

Return the article as pure Markdown (no front matter). Begin with the title as an H1.
Make sure the article is at least 4,000 words. Every step must be fully detailed with check-ins."""

    body = call_pollinations_direct(INTELLIGENCE_SYSTEM, user_prompt)

    # If too short, continue
    word_count = len(body.split())
    print(f"  First pass: {word_count} words")

    if word_count < 3500:
        print("  Article too short, continuing...")
        continue_prompt = f"""The previous article was cut off or too short. Here is the last part:

...{body[-1500:]}

CONTINUE the article from where it left off. Do NOT repeat any content. Pick up EXACTLY where it ended.
If you were in the middle of a section, complete it. Then continue with all remaining sections.
Make sure to include: Cost Breakdown, Production Checklist, and What to Do Next.

Write at least 2000 more words."""

        continuation = call_pollinations_direct(INTELLIGENCE_SYSTEM, continue_prompt)
        cont_words = len(continuation.split())
        print(f"  Second pass: {cont_words} words added")
        body = body + "\n\n" + continuation
        word_count = len(body.split())
        print(f"  Total: {word_count} words")

    # Step 3: Process
    title = extract_title(body)
    excerpt = build_excerpt(body)
    body_clean = strip_h1(body)

    # Inject affiliate links
    body_clean = inject_affiliate_links(body_clean, affiliates)

    # Append Recommended Tools
    tools_section = generate_tools_section(affiliates)
    if tools_section:
        body_clean = body_clean + "\n\n" + tools_section

    # Build frontmatter
    read_time = max(20, min(30, word_count // 200))
    now = datetime.now(timezone.utc)
    difficulty = "INTERMEDIATE"

    front_matter = f"""---
title: "{title}"
date: {now.strftime("%Y-%m-%d")}
category: "Implementation"
difficulty: "{difficulty}"
readTime: "{read_time} MIN"
excerpt: "{excerpt}"
image: "{image_path}"
heroImage: "{hero_path}"
relatedOpportunity: "/opportunities/{opp_slug}/"
---

"""

    # Save
    content_dir = Path("content/intelligence")
    content_dir.mkdir(parents=True, exist_ok=True)
    filepath = content_dir / f"{slug}.md"
    filepath.write_text(front_matter + body_clean)

    final_words = len(body_clean.split())
    print(f"  Saved: {filepath}")
    print(f"  Title: {title}")
    print(f"  Word count: ~{final_words}")

    # Step 4: Update opportunity article with back-link
    opp_file = Path("content/opportunities") / f"{opp_slug}.md"
    if opp_file.exists():
        try:
            opp_content = opp_file.read_text()
            if "relatedGuide:" not in opp_content:
                opp_content = opp_content.replace(
                    "---\n\n",
                    f'relatedGuide: "/intelligence/{slug}/"\n---\n\n',
                    1,
                )
                opp_file.write_text(opp_content)
                print(f"  Updated opportunity article with link to intelligence guide")
        except Exception as e:
            print(f"  Warning: Could not update opportunity article: {e}")

    return {"slug": slug, "title": title, "words": final_words}


if __name__ == "__main__":
    import random

    results = {"opportunities": [], "intelligence": []}

    # Generate 5 opportunity articles
    for i, topic_data in enumerate(OPPORTUNITY_TOPICS):
        print(f"\n\n{'#'*70}")
        print(f"# OPPORTUNITY ARTICLE {i+1}/5")
        print(f"{'#'*70}")
        try:
            result = generate_opportunity_article(topic_data)
            results["opportunities"].append(result)
        except Exception as e:
            print(f"  ERROR generating opportunity article: {e}")
            continue
        # Rate limit pause
        time.sleep(5)

    # Generate 5 intelligence articles
    for i, topic_data in enumerate(OPPORTUNITY_TOPICS):
        print(f"\n\n{'#'*70}")
        print(f"# INTELLIGENCE ARTICLE {i+1}/5")
        print(f"{'#'*70}")
        try:
            result = generate_intelligence_article(topic_data, topic_data["slug"])
            results["intelligence"].append(result)
        except Exception as e:
            print(f"  ERROR generating intelligence article: {e}")
            continue
        # Rate limit pause
        time.sleep(5)

    # Print summary
    print(f"\n\n{'='*60}")
    print("GENERATION SUMMARY")
    print(f"{'='*60}")
    print(f"\nOpportunity Articles ({len(results['opportunities'])}):")
    for r in results["opportunities"]:
        print(f"  - {r['title']}: ~{r['words']} words")

    print(f"\nIntelligence Articles ({len(results['intelligence'])}):")
    for r in results["intelligence"]:
        print(f"  - {r['title']}: ~{r['words']} words")

    total_words = sum(r['words'] for r in results['opportunities']) + sum(r['words'] for r in results['intelligence'])
    print(f"\nTotal words generated: ~{total_words}")
