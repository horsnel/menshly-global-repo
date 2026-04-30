#!/usr/bin/env python3
"""Generate batch of high-quality opportunity and intelligence articles using z-ai-web-dev-sdk.

This script generates articles section-by-section to ensure quality and length,
using the Node.js bridge (ai-bridge.js) which calls z-ai-web-dev-sdk.
"""

import os
import re
import json
import time
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BRIDGE_SCRIPT = PROJECT_ROOT / "scripts" / "ai-bridge.js"

# ── Opportunity Article Topics ─────────────────────────────────────────
OPPORTUNITY_TOPICS = [
    {
        "topic": "AI Podcast Production Agency",
        "title": "How to Start an AI Podcast Production Agency in 2026 ($8K-$40K/Month)",
        "slug": "ai-podcast-production-agency",
        "angle": "AI podcast production agency that produces, edits, and distributes podcasts for businesses and creators",
        "intelligence_angle": "Build and Deploy an AI Podcast Production Pipeline with Descript and Make.com",
        "intelligence_slug": "build-ai-podcast-production-pipeline",
        "excerpt": "Every tool, every hack, every ugly truth — the complete deep dive on building an AI podcast production agency that turns raw recordings into polished shows on autopilot.",
        "affiliates": ["Make.com", "Replit", "ElevenLabs", "Canva", "ChatGPT", "Notion", "Descript"],
    },
    {
        "topic": "AI Resume & Career Service",
        "title": "How to Start an AI Resume & Career Service in 2026 ($5K-$25K/Month)",
        "slug": "ai-resume-career-service",
        "angle": "AI-powered resume writing, LinkedIn optimization, and career coaching service",
        "intelligence_angle": "Build an AI-Powered Resume and Career Optimization System",
        "intelligence_slug": "build-ai-resume-career-optimization-system",
        "excerpt": "Every framework, every hack, every ugly truth — the complete deep dive on building an AI resume and career service that lands clients their dream jobs.",
        "affiliates": ["Make.com", "ChatGPT", "Canva", "Notion", "Grammarly", "Loom", "Calendly"],
    },
    {
        "topic": "AI Affiliate Marketing Business",
        "title": "How to Build an AI Affiliate Marketing Business in 2026 ($10K-$50K/Month)",
        "slug": "ai-affiliate-marketing-business",
        "angle": "AI-powered affiliate marketing that creates content, ranks pages, and generates passive commissions",
        "intelligence_angle": "Build and Scale an AI Affiliate Marketing System with Semrush and Make.com",
        "intelligence_slug": "build-ai-affiliate-marketing-system",
        "excerpt": "Every strategy, every hack, every ugly truth — the complete deep dive on building an AI affiliate marketing business that generates passive income on autopilot.",
        "affiliates": ["Semrush", "Make.com", "Hostinger", "ChatGPT", "Canva", "Notion", "Beehiiv"],
    },
    {
        "topic": "AI Customer Support Automation Agency",
        "title": "How to Start an AI Customer Support Automation Agency in 2026 ($8K-$35K/Month)",
        "slug": "ai-customer-support-automation-agency",
        "angle": "AI customer support agency that deploys chatbots, email automation, and ticket routing for businesses",
        "intelligence_angle": "Build and Deploy AI Customer Support Automation for Businesses",
        "intelligence_slug": "build-ai-customer-support-automation",
        "excerpt": "Every workflow, every hack, every ugly truth — the complete deep dive on building an AI customer support agency that replaces expensive support teams with smart automation.",
        "affiliates": ["Make.com", "Vapi", "ChatGPT", "Klaviyo", "ActiveCampaign", "Notion", "Canva"],
    },
    {
        "topic": "AI Real Estate Marketing Agency",
        "title": "How to Start an AI Real Estate Marketing Agency in 2026 ($10K-$50K/Month)",
        "slug": "ai-real-estate-marketing-agency",
        "angle": "AI marketing agency specialized for real estate — listing descriptions, virtual tours, lead nurture, social media",
        "intelligence_angle": "Build an AI Real Estate Marketing System with Make.com and Canva",
        "intelligence_slug": "build-ai-real-estate-marketing-system",
        "excerpt": "Every tool, every hack, every ugly truth — the complete deep dive on building an AI real estate marketing agency that helps agents close more deals with less effort.",
        "affiliates": ["Make.com", "Canva", "ChatGPT", "ElevenLabs", "Klaviyo", "Buffer", "Notion"],
    },
]


def call_llm(system_prompt: str, user_prompt: str, max_tokens: int = 8000, temperature: float = 0.75) -> str:
    """Call the AI via the Node.js bridge or direct API."""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    # Try direct API first (Groq if available)
    api_key = os.environ.get("AI_API_KEY", "")
    api_base = os.environ.get("AI_API_BASE", "")
    
    if api_key and api_base:
        try:
            import requests
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            }
            payload = {
                "model": os.environ.get("AI_MODEL", "llama-3.3-70b-versatile"),
                "messages": messages,
                "max_tokens": max_tokens,
                "temperature": temperature,
            }
            resp = requests.post(
                f"{api_base}/chat/completions",
                headers=headers,
                json=payload,
                timeout=300,
            )
            if resp.status_code == 200:
                data = resp.json()
                return data["choices"][0]["message"]["content"]
            else:
                print(f"  Direct API failed ({resp.status_code}), trying bridge...")
        except Exception as e:
            print(f"  Direct API error: {e}, trying bridge...")

    # Try the Node.js bridge
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump({
                "messages": messages,
                "max_tokens": max_tokens,
                "temperature": temperature,
            }, f)
            temp_path = f.name

        result = subprocess.run(
            ["node", str(BRIDGE_SCRIPT), "--input-file", temp_path],
            capture_output=True,
            text=True,
            timeout=600,
            cwd=str(PROJECT_ROOT),
        )

        try:
            os.unlink(temp_path)
        except OSError:
            pass

        if result.returncode != 0:
            raise RuntimeError(f"Bridge error: {result.stderr.strip()[:200]}")

        output = result.stdout.strip()
        json_start = output.find('{')
        if json_start >= 0:
            output = output[json_start:]
        data = json.loads(output)
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"  Bridge failed: {e}")
        return None


def slugify(title: str) -> str:
    """Create a URL-safe slug from the title."""
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    slug = slug.strip("-")
    return slug[:80]


def generate_opportunity_article(topic_data: dict) -> str:
    """Generate a complete opportunity article section by section."""
    
    system = """You are the lead writer for Menshly Global (tagline: "Where AI Meets Revenue").
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

AFFILIATE TOOL NAMES to weave in naturally (at least 5-6): Make.com, Replit, Vapi, Fliki AI, Canva, ChatGPT, ElevenLabs, Klaviyo, ActiveCampaign, Semrush, Hostinger, Shopify, Zapier, Apollo.io, PhantomBuster, Buffer, Loom, Calendly, Beehiiv, Notion, Midjourney, Grammarly

Write ONLY the article content in Markdown. No frontmatter. Start with ## headings (not #)."""

    topic = topic_data["topic"]
    title = topic_data["title"]
    angle = topic_data["angle"]
    
    # Generate article in one large prompt with strict structure
    user_prompt = f"""Write a complete deep-dive opportunity article titled: "{title}"

About: {angle}

Follow this EXACT structure and write EACH section with SUBSTANTIAL content (300+ words each):

## [Opening Hook - 2-3 paragraphs]
Start with a shocking number or uncomfortable truth. End with "I'm going to lay out everything: the exact tools, every hack, every ugly truth, and the realistic numbers."

## Why This Works Right Now
3 reasons this opportunity exists RIGHT NOW. Each reason gets a full paragraph with evidence and specific numbers.

## The Realistic Picture (Before You Get Excited)
4 ugly truths in this format:
> **Truth #1:** [harsh reality with specific numbers]
(Repeat for truths 2-4, each in blockquote format)

## The Free Stack: Starting With Zero Dollars
7 free tools, each as: **Tool Name — $0** — One-line description.
End with a paragraph explaining limitations and a HACK in blockquote format.

## The Paid Stack: When You're Ready to Scale
8-10 paid tools, each as: **Tool Name — $X/mo** — One-line description.
End with total monthly cost and ROI analysis. Include one HACK in blockquote format.

## The Workflow: Step-by-Step With Every Shortcut
3-4 detailed steps (### Step N: Name (time estimate))
Each step has 2-3 paragraphs of detail + HACK callout in blockquote format.

## Pricing: What to Charge and How to Defend It
3 pricing tiers (Starter/Growth/Enterprise) with specific dollar amounts and what's included.
One Pricing Trick HACK in blockquote format.

## Getting Clients: The Real Playbook
3 methods with names and conversion rates (### Method N: Name (Conversion: X%))
Each method gets a full paragraph with specific tactics.
End with one HACK in blockquote format.

## Tricks and Hacks They Don't Share in Courses
5 hacks, each in blockquote format:
> **HACK 1: Name.** Detailed explanation of the trick.

## The Real Numbers
A month-by-month revenue table:
| Month | Revenue | Clients | Notes |
|-------|---------|---------|-------|
8-10 rows from Month 1 ($0) through Month 12.
Then a paragraph on unit economics.

## What Nobody Warns You About
4 honest warnings, each as a bold-titled paragraph.

## Start This Weekend (Literally)
Exact weekend action plan:
**Saturday morning:** specific task
**Saturday afternoon:** specific task  
**Sunday:** specific task with copy-paste pitch template

WORD COUNT TARGET: 4,500-5,500 words. Do NOT cut sections short.
Every section must be fully developed with real substance."""

    result = call_llm(system, user_prompt, max_tokens=16000, temperature=0.75)
    if not result:
        print(f"  FAILED to generate opportunity article for {topic}")
        return None
    
    word_count = len(result.split())
    print(f"  Generated opportunity article: {word_count} words")
    
    # If too short, continue
    if word_count < 4000:
        print("  Article too short, generating continuation...")
        continue_prompt = f"""The previous article was cut off at {word_count} words. Here is the end:

...{result[-2000:]}

CONTINUE the article from where it left off. Do NOT repeat any content. Pick up EXACTLY where it ended.
Make sure to include any remaining sections, especially: Tricks and Hacks, The Real Numbers table, What Nobody Warns You About, and Start This Weekend.

Write at least 2000 more words."""
        
        continuation = call_llm(system, continue_prompt, max_tokens=16000, temperature=0.7)
        if continuation:
            result = result + "\n\n" + continuation
            word_count = len(result.split())
            print(f"  After continuation: {word_count} words")
    
    return result


def generate_intelligence_article(topic_data: dict) -> tuple:
    """Generate a complete intelligence article section by section."""
    
    system = """You are the technical implementation writer for Menshly Global (tagline: "Where AI Meets Revenue").
You write deep execution guides that readers can follow step-by-step to build real systems.

CRITICAL STYLE RULES:
- Write in an INSTRUCTIONAL, CLINICAL tone — like a senior engineer walking a junior through a build
- Every step must be specific: exact button names, exact menu paths, exact settings
- Include INTERACTIVE CHECK-INS: "Do you see [X]? You should see [X] if you're in the right place."
- Show expected output at every step: terminal output, UI descriptions, JSON responses
- Include error scenarios: "If you see [ERROR], this means [CAUSE]. Fix it by [SOLUTION]."
- Name real tools with real prices
- Include complete configurations, not pseudocode — readers should be able to copy-paste
- Never use vague phrases like "configure it appropriately" — say EXACTLY what to configure
- Each numbered step should take 10-30 minutes in real life

AFFILIATE TOOL NAMES to weave in naturally (at least 5-6): Make.com, Replit, Vapi, Fliki AI, Canva, ChatGPT, ElevenLabs, Klaviyo, ActiveCampaign, Semrush, Hostinger, Shopify, Zapier, Apollo.io, PhantomBuster, Buffer, Loom, Calendly, Beehiiv, Notion, Midjourney, Grammarly

Write ONLY the article content in Markdown. No frontmatter. Start with ## headings (not #)."""

    topic = topic_data["topic"]
    intel_angle = topic_data["intelligence_angle"]
    opp_title = topic_data["title"]
    opp_slug = topic_data["slug"]
    
    user_prompt = f"""Write a complete step-by-step implementation article titled: "{intel_angle}"

This is the execution guide for building the {topic} business outlined in: "{opp_title}" (URL: /opportunities/{opp_slug}/)

Reference this opportunity in the opening paragraph.

Follow this EXACT structure:

## Prerequisites
Bullet list of accounts, tools, costs, and time required.
Total upfront cost stated clearly.

## Step 1: [Setup/Configure]
Directory structure, account setup, API keys, initial configuration.
Full terminal commands or UI steps with expected output.
Interactive check-in: "Do you see [X]? If not, [troubleshooting]."

## Step 2: [Build Core Component]
The main implementation. Complete, runnable configurations.
Explain what each part does.
Interactive check-in after each major configuration.

## Step 3: [Test Locally]
How to verify it works. Test commands, expected responses.
Common errors and fixes.
A 5-test checklist.

## Step 4: [Add Advanced Feature]
Enhancement that makes the system production-worthy.
Interactive check-in after configuration.

## Step 5: [Deploy to Production OR Price and Sell]
Pricing structure with a table (Starter/Growth/Enterprise tiers)
and the specific sales method with a copy-paste pitch template.

## Step 6: [Scale/Grow]
How to go from 1 to 10+ clients/users.
Hiring plan, automation upgrades, margin improvements.

## Cost Breakdown
Table with columns: Item | Free Tier | Paid Tier | When to Upgrade
Monthly cost analysis at different scales.

## Production Checklist
Checklist of 8-10 items:
- [ ] Item 1
etc.

## What to Do Next
4-5 specific next steps.

WORD COUNT TARGET: 4,500-5,500 words. Every step must be fully detailed.
Do NOT write short sections. Every step needs sub-steps, configurations, and check-ins."""

    result = call_llm(system, user_prompt, max_tokens=16000, temperature=0.7)
    if not result:
        print(f"  FAILED to generate intelligence article for {topic}")
        return None, "INTERMEDIATE"
    
    word_count = len(result.split())
    print(f"  Generated intelligence article: {word_count} words")
    
    difficulty = "ADVANCED"
    
    # If too short, continue
    if word_count < 3500:
        print("  Article too short, generating continuation...")
        continue_prompt = f"""The previous article was cut off at {word_count} words. Here is the end:

...{result[-2000:]}

CONTINUE the article from where it left off. Do NOT repeat any content. Pick up EXACTLY where it ended.
Make sure to include: Cost Breakdown table, Production Checklist, and What to Do Next.

Write at least 2000 more words."""
        
        continuation = call_llm(system, continue_prompt, max_tokens=16000, temperature=0.65)
        if continuation:
            result = result + "\n\n" + continuation
            word_count = len(result.split())
            print(f"  After continuation: {word_count} words")
    
    return result, difficulty


def build_frontmatter(title: str, date: str, category: str, read_time: str, excerpt: str, 
                      image: str, hero_image: str, extra_fields: dict = None) -> str:
    """Build Hugo frontmatter."""
    lines = ["---"]
    lines.append(f'title: "{title}"')
    lines.append(f'date: {date}')
    lines.append(f'category: "{category}"')
    if category == "Implementation":
        lines.append(f'difficulty: "{extra_fields.get("difficulty", "INTERMEDIATE")}"')
    lines.append(f'readTime: "{read_time}"')
    lines.append(f'excerpt: "{excerpt}"')
    lines.append(f'image: "{image}"')
    lines.append(f'heroImage: "{hero_image}"')
    
    if extra_fields:
        if "relatedGuide" in extra_fields:
            lines.append(f'relatedGuide: "{extra_fields["relatedGuide"]}"')
        if "relatedOpportunity" in extra_fields:
            lines.append(f'relatedOpportunity: "{extra_fields["relatedOpportunity"]}"')
        if "relatedPlaybook" in extra_fields:
            lines.append(f'relatedPlaybook: "{extra_fields["relatedPlaybook"]}"')
    
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", choices=["opportunity", "intelligence", "both"], default="both")
    parser.add_argument("--count", type=int, default=5, help="Number of articles to generate")
    args = parser.parse_args()
    
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%Y-%m-%d")
    
    topics = OPPORTUNITY_TOPICS[:args.count]
    
    if args.type in ("opportunity", "both"):
        print(f"\n{'='*60}")
        print(f"Generating {len(topics)} OPPORTUNITY articles...")
        print(f"{'='*60}")
        
        for i, topic_data in enumerate(topics):
            print(f"\n--- Opportunity Article {i+1}/{len(topics)}: {topic_data['topic']} ---")
            
            body = generate_opportunity_article(topic_data)
            if not body:
                print(f"  SKIPPING {topic_data['topic']} - generation failed")
                continue
            
            # Clean up title from body if it starts with #
            body_clean = body
            for line in body.split("\n"):
                if line.strip().startswith("# ") and not line.strip().startswith("## "):
                    body_clean = body.replace(line + "\n", "", 1)
                    break
            
            slug = topic_data["slug"]
            image = f"/images/articles/opportunities/{slug}.png"
            hero = f"/images/heroes/opportunities/{slug}.png"
            
            # Build related links
            extra = {
                "relatedGuide": f"/intelligence/{topic_data['intelligence_slug']}/",
                "relatedPlaybook": "/playbooks/ai-side-hustle-blueprint/",
            }
            
            frontmatter = build_frontmatter(
                title=topic_data["title"],
                date=date_str,
                category="AI Opportunity",
                read_time="16 MIN",
                excerpt=topic_data["excerpt"],
                image=image,
                hero_image=hero,
                extra_fields=extra,
            )
            
            content = frontmatter + body_clean
            
            filepath = PROJECT_ROOT / "content" / "opportunities" / f"{slug}.md"
            filepath.parent.mkdir(parents=True, exist_ok=True)
            filepath.write_text(content)
            
            word_count = len(body_clean.split())
            print(f"  Saved: {filepath}")
            print(f"  Word count: ~{word_count}")
            
            # Save to last_generated
            lg_file = PROJECT_ROOT / "data" / "last_generated.json"
            lg_data = {}
            if lg_file.exists():
                try:
                    lg_data = json.loads(lg_file.read_text())
                except:
                    pass
            lg_data["last_opportunity"] = {
                "slug": slug,
                "title": topic_data["title"],
                "topic": topic_data["topic"],
                "opportunity_angle": topic_data["angle"],
                "intelligence_angle": topic_data["intelligence_angle"],
                "generated_at": now.isoformat(),
            }
            lg_file.parent.mkdir(parents=True, exist_ok=True)
            lg_file.write_text(json.dumps(lg_data, indent=2))
    
    if args.type in ("intelligence", "both"):
        print(f"\n{'='*60}")
        print(f"Generating {len(topics)} INTELLIGENCE articles...")
        print(f"{'='*60}")
        
        for i, topic_data in enumerate(topics):
            print(f"\n--- Intelligence Article {i+1}/{len(topics)}: {topic_data['intelligence_angle']} ---")
            
            body, difficulty = generate_intelligence_article(topic_data)
            if not body:
                print(f"  SKIPPING {topic_data['intelligence_angle']} - generation failed")
                continue
            
            # Clean up title from body
            body_clean = body
            for line in body.split("\n"):
                if line.strip().startswith("# ") and not line.strip().startswith("## "):
                    body_clean = body.replace(line + "\n", "", 1)
                    break
            
            slug = topic_data["intelligence_slug"]
            image = f"/images/articles/intelligence/{slug}.png"
            hero = f"/images/heroes/intelligence/{slug}.png"
            
            extra = {
                "difficulty": difficulty,
                "relatedOpportunity": f"/opportunities/{topic_data['slug']}/",
                "relatedPlaybook": "/playbooks/ai-side-hustle-blueprint/",
            }
            
            # Build excerpt from body
            lines = body_clean.split("\n")
            paragraph = ""
            for line in lines:
                line = line.strip()
                if line.startswith("## "):
                    if paragraph:
                        break
                    continue
                if not line:
                    if paragraph:
                        break
                    continue
                if not line.startswith("#"):
                    clean = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', line)
                    paragraph += clean + " "
            excerpt = paragraph.strip()[:200]
            if len(paragraph.strip()) > 200:
                excerpt += "..."
            excerpt = excerpt.replace('"', "'")
            
            frontmatter = build_frontmatter(
                title=topic_data["intelligence_angle"],
                date=date_str,
                category="Implementation",
                read_time="25 MIN",
                excerpt=excerpt,
                image=image,
                hero_image=hero,
                extra_fields=extra,
            )
            
            content = frontmatter + body_clean
            
            filepath = PROJECT_ROOT / "content" / "intelligence" / f"{slug}.md"
            filepath.parent.mkdir(parents=True, exist_ok=True)
            filepath.write_text(content)
            
            word_count = len(body_clean.split())
            print(f"  Saved: {filepath}")
            print(f"  Word count: ~{word_count}")
            
            # Update the opportunity article with back-link
            opp_file = PROJECT_ROOT / "content" / "opportunities" / f"{topic_data['slug']}.md"
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
    
    print(f"\n{'='*60}")
    print("Batch generation complete!")
    print(f"{'='*60}")
