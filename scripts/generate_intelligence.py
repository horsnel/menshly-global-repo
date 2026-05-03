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

v3 REWRITE — Section-by-section generation:
  - Generates each major section as a SEPARATE API call
  - Works reliably even on weak models (Pollinations, small LLMs)
  - Enforces minimum word count per section
  - Quality checks with retry on short sections
  - Cross-links to opportunity and playbook articles
"""

import os
import re
import json
import time
import random
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

# ── Section definitions for Intelligence articles ──
SECTION_DEFS = [
    {
        "heading": "Prerequisites",
        "instructions": """Write the Prerequisites section.
Bullet list of accounts, tools, costs, and time required.
Total upfront cost stated clearly.
Include a TABLE with: Tool | Purpose | Cost | Free Tier Limit
Write 200-300 words.""",
        "min_words": 150,
    },
    {
        "heading": "Step 1: Setup and Configuration",
        "instructions": """Write Step 1: Setup and Configuration.
Directory structure, account setup, API keys, initial configuration.
Full terminal commands or UI steps with expected output.
Interactive check-in: "Do you see [X]? If not, [troubleshooting]."
Include error scenarios: "If you see [ERROR], this means [CAUSE]. Fix it by [SOLUTION]."
Write 400-600 words.""",
        "min_words": 300,
        "heading_template": "## Step 1: {step_title}",
    },
    {
        "heading": "Step 2: Build the Core System",
        "instructions": """Write Step 2: Build the Core System.
The main implementation. Complete, runnable configurations.
Explain what each part does in 1-2 sentences.
Interactive check-in after each major configuration block.
Include a TABLE showing the key settings and their values.
Write 500-700 words.""",
        "min_words": 350,
        "heading_template": "## Step 2: {step_title}",
    },
    {
        "heading": "Step 3: Test and Validate",
        "instructions": """Write Step 3: Test and Validate.
How to verify it works. Test commands, expected responses.
Common errors and fixes.
The 5-point test checklist (5 specific things to verify before proceeding).
Write 300-400 words.""",
        "min_words": 200,
        "heading_template": "## Step 3: {step_title}",
    },
    {
        "heading": "Step 4: Add Advanced Features",
        "instructions": """Write Step 4: Add Advanced Features.
Enhancement that makes the system production-worthy (AI enrichment, error handling, routing, etc.)
Interactive check-in after configuration.
Show the exact configuration changes needed.
Write 400-500 words.""",
        "min_words": 250,
        "heading_template": "## Step 4: {step_title}",
    },
    {
        "heading": "Step 5: Deploy to Production",
        "instructions": """Write Step 5: Deploy to Production OR Price and Sell.
If deployment: deployment steps with commands and verification.
If service business: pricing structure with a TABLE (Starter/Growth/Enterprise tiers)
and the specific sales method with a copy-paste pitch template.
Write 350-450 words.""",
        "min_words": 200,
        "heading_template": "## Step 5: {step_title}",
    },
    {
        "heading": "Step 6: Scale and Grow",
        "instructions": """Write Step 6: Scale and Grow.
How to go from 1 to 10+ clients/users.
Hiring plan, automation upgrades, margin improvements.
Include a TABLE showing scale milestones.
Write 300-400 words.""",
        "min_words": 200,
        "heading_template": "## Step 6: {step_title}",
    },
    {
        "heading": "Cost Breakdown",
        "instructions": """Write the Cost Breakdown section.
TABLE with columns: Item | Free Tier | Paid Tier | When to Upgrade
Include 8-10 items.
Monthly cost analysis at different scales (solo, 5 clients, 10+ clients).
Write 200-300 words.""",
        "min_words": 150,
    },
    {
        "heading": "Production Checklist",
        "instructions": """Write the Production Checklist section.
Checklist of 8-10 items to verify before going live:
- [ ] Item 1
- [ ] Item 2
etc.
Each item should be specific and measurable.
Write 150-250 words.""",
        "min_words": 100,
    },
    {
        "heading": "What to Do Next",
        "instructions": """Write the "What to Do Next" section.
4-5 specific next steps or expansion ideas, each as a bold-titled paragraph.
Include links to related Menshly content where relevant.
Write 200-300 words.""",
        "min_words": 150,
    },
]

# ── System prompt shared across all section calls ──
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

Always mention at least 2-3 of these tools NATURALLY in each section.
Do NOT add a separate "Recommended Tools" section — we add that automatically."""


def load_last_opportunity() -> dict | None:
    """Load the last generated opportunity article data for cross-linking."""
    if not LAST_GENERATED_FILE.exists():
        return None
    try:
        data = json.loads(LAST_GENERATED_FILE.read_text())
        return data.get("last_opportunity")
    except (json.JSONDecodeError, Exception):
        return None


def _call_api(messages: list, max_tokens: int = 4000, temperature: float = 0.7) -> str:
    """Make a single API call and return the content text."""
    payload = {
        "model": AI_MODEL,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    data = api_call(payload)
    return data["choices"][0]["message"]["content"]


def generate_article(topic_data: dict, opportunity_data: dict = None):
    """Generate the full article using section-by-section approach.

    Each section is a separate API call, ensuring consistent quality
    regardless of the AI backend being used.
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
CROSS-LINKING: This guide is the IMPLEMENTATION companion to the opportunity article:
"{opp_title}" (URL: /opportunities/{opp_slug}/)
Reference this in the opening: "This is the execution guide for the [TOPIC] business we outlined in our opportunity deep-dive."
Link back at the end: "Ready to understand the full business opportunity? Read our [opportunity deep-dive]({{< ref "/opportunities/{opp_slug}.md" >}})." """

    print(f"Generating article about: {topic}")
    print(f"Difficulty: {difficulty}")
    print(f"Strategy: Section-by-section generation ({len(SECTION_DEFS)} sections)")

    # Generate the title first
    title_prompt = f"""Generate an SEO-optimized title for a technical implementation article about: {topic}

The title must use IMPERATIVE VERBS (NOT "How to"):
Pattern: "[VERB], [VERB], and [VERB] [THING] with [TOOL]"
Examples:
- "Train, Serve, and Deploy a Scikit-learn Model with FastAPI"
- "Design, Build, and Deploy Make.com Automation Workflows"

Return ONLY the title, nothing else."""

    title_messages = [
        {"role": "system", "content": "You are a technical title generator. Return only the title."},
        {"role": "user", "content": title_prompt},
    ]

    for attempt in range(3):
        try:
            title_text = _call_api(title_messages, max_tokens=100, temperature=0.8)
            title_text = title_text.strip().strip('"').strip("'")
            if len(title_text) > 15:
                break
        except Exception as e:
            print(f"  Title generation attempt {attempt+1} failed: {str(e)[:100]}")
            time.sleep(3)
    else:
        title_text = f"Build, Deploy, and Scale {topic}"

    print(f"  Title: {title_text}")

    # Generate an intro paragraph
    intro_prompt = f"""Write a 2-3 paragraph introduction for a technical implementation article about: {topic}

Title: {title_text}
Difficulty: {difficulty}

The intro should:
1. State what the reader will build and achieve
2. Mention this is an execution guide (not a blog post)
3. State the total time and cost commitment
{opportunity_context if opportunity_data else ""}

Write 150-250 words. Do NOT include a heading — just the paragraphs."""

    print(f"\n  [0/{len(SECTION_DEFS)}] Generating introduction...")
    intro_messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": intro_prompt},
    ]
    intro = ""
    for attempt in range(3):
        try:
            intro = _call_api(intro_messages, max_tokens=1000, temperature=0.7)
            if len(intro.split()) >= 80:
                break
        except Exception as e:
            print(f"    Intro attempt {attempt+1} failed: {str(e)[:100]}")
            time.sleep(3)

    # Generate each section
    sections = []
    total_sections = len(SECTION_DEFS)

    for i, section_def in enumerate(SECTION_DEFS):
        heading = section_def["heading"]
        instructions = section_def["instructions"]
        min_words = section_def["min_words"]

        print(f"\n  [{i+1}/{total_sections}] Generating: {heading}...")

        # Build context from previously generated sections
        prev_context = ""
        if sections:
            prev_summaries = []
            for s in sections[-3:]:  # Only last 3 for context
                first_line = s.split("\n")[0][:100]
                prev_summaries.append(first_line)
            prev_context = f"Previously written sections: {', '.join(prev_summaries)}"

        section_prompt = f"""Write the following section for a technical implementation article about: {topic}

TITLE: {title_text}
Difficulty: {difficulty}

{'TRENDING CONTEXT: ' + context if context else ''}

SECTION TO WRITE: {heading}

{instructions}

{prev_context if prev_context else ''}

WORD COUNT TARGET: At least {min_words} words for this section.
Be specific with exact settings, exact tool names, and exact configurations."""

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": section_prompt},
        ]

        section_text = ""
        for attempt in range(3):
            try:
                result = _call_api(messages, max_tokens=3000, temperature=0.7)
                word_count = len(result.split())

                if word_count >= min_words * 0.6:
                    if word_count < min_words:
                        print(f"    {heading}: {word_count} words (target {min_words}, accepted)")
                    else:
                        print(f"    {heading}: {word_count} words ✓")

                    # Add the heading if not already present
                    if not result.strip().startswith("## "):
                        result = f"## {heading}\n\n{result}"

                    section_text = result
                    sections.append(section_text)
                    break
                else:
                    print(f"    {heading} attempt {attempt+1}: too short ({word_count} words), retrying...")
                    time.sleep(3)
            except Exception as e:
                print(f"    {heading} attempt {attempt+1} failed: {str(e)[:100]}")
                time.sleep(5)
        else:
            # Use whatever we got
            if not section_text:
                section_text = f"## {heading}\n\n*Section content pending review.*\n"
            elif not section_text.strip().startswith("## "):
                section_text = f"## {heading}\n\n{section_text}"
            print(f"    {heading}: using best available after retries")
            sections.append(section_text)

    # Assemble the full article
    body = f"# {title_text}\n\n{intro}\n\n" + "\n\n".join(sections)

    # Add opportunity cross-link at the end
    if opportunity_data:
        opp_slug = opportunity_data.get("slug", "")
        body += f'\n\nReady to understand the full business opportunity? Read our [opportunity deep-dive]({{< ref "/opportunities/{opp_slug}.md" >}}).\n'

    final_words = len(body.split())
    print(f"\n  Total article: {final_words} words")

    # Inject affiliate links into tool mentions
    body = inject_affiliate_links(body, affiliates)

    # Append Recommended Tools section
    tools_section = generate_tools_section(affiliates)
    if tools_section:
        body = body + "\n\n" + tools_section

    return body, difficulty


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
        print("No AI_API_KEY set — will use Pollinations (free) as fallback")

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

    if not topic_data or not topic_data.get("topic"):
        print("ERROR: No topic available")
        exit(1)

    # If intelligence_angle is missing, derive it from the topic
    if not topic_data.get("intelligence_angle"):
        topic_text = topic_data.get("topic", "")
        topic_data["intelligence_angle"] = f"Build, Deploy, and Scale {topic_text}"
        print(f"  No intelligence_angle found, derived: {topic_data['intelligence_angle']}")

    topic = topic_data.get("intelligence_angle", topic_data.get("topic", ""))
    print(f"Generating article about: {topic}")

    # Step 1: Generate images FIRST (non-fatal — continue without if failed)
    prelim_slug = slugify(topic)

    image_path = f"/images/articles/intelligence/{prelim_slug}.png"
    hero_path = f"/images/heroes/intelligence/{prelim_slug}.png"

    try:
        print("Generating thumbnail image...")
        image_path = generate_article_image(
            topic=topic,
            slug=prelim_slug,
            section="intelligence",
        )
        print(f"Thumbnail saved: {image_path}")
    except Exception as e:
        print(f"  Thumbnail generation failed (non-fatal): {e}")

    try:
        print("Generating hero image...")
        hero_path = generate_hero_image(
            topic=topic,
            slug=prelim_slug,
            section="intelligence",
        )
        print(f"Hero image saved: {hero_path}")
    except Exception as e:
        print(f"  Hero image generation failed (non-fatal): {e}")

    # Step 2: Generate article content (section-by-section)
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

    if word_count < 2500:
        print("  WARNING: Total word count below 2500.")

    # Step 5: Save data for playbook cross-linking
    save_last_generated(topic_data, slug, title, difficulty)
    print(f"Saved topic data for cross-linking")

    print(f"\n✅ Intelligence article generated successfully!")
    print(f"   Cross-linked to opportunity: {opportunity_data.get('slug', 'N/A') if opportunity_data else 'N/A'}")
    print(f"   Other generators can link to: /intelligence/{slug}/")
