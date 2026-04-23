#!/usr/bin/env python3
"""Generate an Opportunity article using AI API."""

import os
import json
import requests
from datetime import datetime, timezone
from pathlib import Path

AI_API_KEY = os.environ.get("AI_API_KEY", "")
AI_API_BASE = os.environ.get("AI_API_BASE", "https://api.openai.com/v1")
AI_MODEL = os.environ.get("AI_MODEL", "gpt-4o")
PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY", "")

TOPICS = [
    "New AI model release and monetization opportunities",
    "Emerging AI automation platform and how to profit from it",
    "AI-powered business tool that creates new revenue streams",
    "Untapped AI market niche with high profit potential",
    "AI API integration opportunity for freelancers and agencies",
]

import random
topic = random.choice(TOPICS)

prompt = f"""Write a detailed article about: {topic}

The article should be for an AI monetization blog called "Menshly Global" (tagline: "Where AI Meets Revenue").
Target audience: entrepreneurs, freelancers, and builders who want to make money with AI.

Structure:
- Catchy title
- 3-4 sections with H2 headings
- Actionable insights and specific examples
- Realistic revenue numbers
- Minimum 800 words

Return ONLY the article body in Markdown format (no front matter)."""

def generate_article():
    headers = {
        "Authorization": f"Bearer {AI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": AI_MODEL,
        "messages": [
            {"role": "system", "content": "You are an expert AI business writer for Menshly Global."},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": 2000,
        "temperature": 0.8,
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
            {"role": "system", "content": "Generate a short, punchy, uppercase title for this article. Return ONLY the title, nothing else."},
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
category: "AI Discovery"
readTime: "6 MIN"
excerpt: "{body[:120].replace(chr(10), ' ').replace('"', "'")}..."
---

"""
    content_dir = Path("content/opportunities")
    content_dir.mkdir(parents=True, exist_ok=True)
    filepath = content_dir / f"{slug}.md"
    filepath.write_text(front_matter + body)
    print(f"Created: {filepath}")
