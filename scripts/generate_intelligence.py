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
"""

import os
import re
import json
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

# ── Intelligence implementation topics ────────────────────────────────
TOPICS = [
    "Build and Deploy an AI Chatbot Agency End-to-End",
    "Design, Build, and Deploy Make.com Automation Workflows",
    "Launch and Monetize an AI Content Business From Scratch",
    "Build and Scale an AI SEO Agency with Automated Workflows",
    "Create and Deploy an AI Voice Agent System with Vapi",
    "Build and Monetize AI SaaS Micro-Products on Replit",
    "Design and Deploy AI-Powered Email Marketing Automations",
    "Build an AI Lead Generation System with Make.com and OpenAI",
    "Create and Scale a Faceless YouTube Channel with AI Tools",
    "Build and Deploy an AI Social Media Management Pipeline",
    "Set Up, Train, and Deploy a Custom AI Agent with LangChain",
    "Build and Automate an AI Copywriting Agency Workflow",
    "Design and Launch an AI Newsletter Business with Automation",
    "Build and Scale an AI Data Analysis Service End-to-End",
    "Create and Deploy AI-Powered E-Commerce Chatbots",
    "Build and Monetize AI Image Generation Workflows",
    "Design and Deploy AI-Powered Customer Onboarding Systems",
    "Build and Scale an AI Course Creation Business",
    "Configure and Deploy AI-Powered HR and Recruitment Automation",
    "Build and Automate an AI Bookkeeping Service",
]

DIFFICULTIES = ["INTERMEDIATE", "ADVANCED"]

topic = random.choice(TOPICS)
difficulty = random.choice(DIFFICULTIES)

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

USER_PROMPT = f"""Write a complete step-by-step implementation article about: {topic}

Follow the exact structure and style defined in your system instructions.
Difficulty level: {difficulty}
This is for the Intelligence category on Menshly Global — deep implementation guides for builders.

The title must be SEO-optimized using IMPERATIVE VERBS (not "How to"):
Pattern: "[VERB], [VERB], and [VERB] [THING] with [TOOL]"
Example: "Train, Serve, and Deploy a Scikit-learn Model with FastAPI"
Example: "Design, Build, and Deploy Make.com Automation Workflows"

Return the article as pure Markdown (no front matter). Begin with the title as an H1."""


def generate_article():
    """Call the AI API to generate the full article."""
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
        "max_tokens": 8000,
        "temperature": 0.7,
    }
    resp = requests.post(
        f"{AI_API_BASE}/chat/completions",
        headers=headers,
        json=payload,
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]


def extract_title(body: str) -> str:
    """Extract the H1 title from the markdown body."""
    for line in body.split("\n"):
        line = line.strip()
        if line.startswith("# ") and not line.startswith("## "):
            return line.lstrip("# ").strip()
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
        if not line:
            if paragraph:
                break
            continue
        paragraph += line + " "
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


if __name__ == "__main__":
    if not AI_API_KEY:
        print("ERROR: AI_API_KEY not set")
        exit(1)

    print(f"Generating article about: {topic}")
    print(f"Difficulty: {difficulty}")

    # Step 1: Generate images FIRST (before article content)
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
    body = generate_article()
    title = extract_title(body)
    excerpt = build_excerpt(body)
    body_clean = strip_h1(body)

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
category: "Implementation"
difficulty: "{difficulty}"
readTime: "25 MIN"
excerpt: "{excerpt}"
image: "{image_path}"
heroImage: "{hero_path}"
---

"""

    content_dir = Path("content/intelligence")
    content_dir.mkdir(parents=True, exist_ok=True)
    filepath = content_dir / f"{slug}.md"
    filepath.write_text(front_matter + body_clean)

    word_count = len(body_clean.split())
    print(f"Created: {filepath}")
    print(f"Title: {title}")
    print(f"Slug: {slug}")
    print(f"Difficulty: {difficulty}")
    print(f"Word count: ~{word_count}")
