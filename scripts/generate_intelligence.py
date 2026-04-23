#!/usr/bin/env python3
"""Generate an Intelligence article using AI API."""

import os
import json
import requests
from datetime import datetime, timezone
from pathlib import Path
import random

AI_API_KEY = os.environ.get("AI_API_KEY", "")
AI_API_BASE = os.environ.get("AI_API_BASE", "https://api.openai.com/v1")
AI_MODEL = os.environ.get("AI_MODEL", "gpt-4o")

TOPICS = [
    "How to build an AI automation agency end-to-end",
    "Deep implementation guide for AI-powered lead generation systems",
    "Building a profitable AI SaaS product from scratch",
    "Complete guide to AI workflow automation for enterprises",
    "Scaling an AI consulting practice to six figures",
]

DIFFICULTIES = ["INTERMEDIATE", "ADVANCED"]

topic = random.choice(TOPICS)
difficulty = random.choice(DIFFICULTIES)

prompt = f"""Write a deep implementation guide about: {topic}

This is for an AI monetization blog called "Menshly Global" (tagline: "Where AI Meets Revenue").
Difficulty: {difficulty}
Target audience: builders and entrepreneurs who want complete, step-by-step execution guides.

Structure:
- Descriptive title
- 5-6 detailed sections with H2 headings
- Technical details with specific tools, APIs, and configurations
- Architecture diagrams described in text
- Code examples where relevant
- Cost estimates and revenue projections
- Common pitfalls and how to avoid them
- Minimum 1200 words

Return ONLY the article body in Markdown format (no front matter)."""

def generate_article():
    headers = {
        "Authorization": f"Bearer {AI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": AI_MODEL,
        "messages": [
            {"role": "system", "content": "You are an expert AI implementation writer for Menshly Global."},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": 3000,
        "temperature": 0.7,
    }
    resp = requests.post(f"{AI_API_BASE}/chat/completions", headers=headers, json=payload, timeout=60)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]

def generate_title(body):
    headers = {
        "Authorization": f"Bearer {AI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": AI_MODEL,
        "messages": [
            {"role": "system", "content": "Generate a short, punchy, uppercase title for this implementation guide. Return ONLY the title."},
            {"role": "user", "content": body[:500]},
        ],
        "max_tokens": 50,
        "temperature": 0.5,
    }
    resp = requests.post(f"{AI_API_BASE}/chat/completions", headers=headers, json=payload, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"].strip().strip('"')

if __name__ == "__main__":
    if not AI_API_KEY:
        print("ERROR: AI_API_KEY not set")
        exit(1)

    body = generate_article()
    title = generate_title(body)

    slug = title.lower().replace(" ", "-").replace(":", "").replace("'", "")[:60]
    now = datetime.now(timezone.utc)

    front_matter = f"""---
title: "{title}"
date: {now.strftime("%Y-%m-%d")}
category: "Implementation"
difficulty: "{difficulty}"
readTime: "20 MIN"
excerpt: "{body[:120].replace(chr(10), ' ').replace('"', "'")}..."
---

"""
    content_dir = Path("content/intelligence")
    content_dir.mkdir(parents=True, exist_ok=True)
    filepath = content_dir / f"{slug}.md"
    filepath.write_text(front_matter + body)
    print(f"Created: {filepath}")
