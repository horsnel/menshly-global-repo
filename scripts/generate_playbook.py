#!/usr/bin/env python3
"""Generate a Playbook article using AI API."""

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
    "AI freelancing playbook with step-by-step client acquisition",
    "Automation service blueprint for small businesses",
    "AI content creation playbook with templates and prompts",
    "AI consulting starter guide with pricing and positioning",
    "AI-powered e-commerce automation playbook",
]

PRICES = ["$19", "$29", "$39", "$49"]

topic = random.choice(TOPICS)
price = random.choice(PRICES)

prompt = f"""Write a detailed playbook about: {topic}

This is for an AI monetization blog called "Menshly Global" (tagline: "Where AI Meets Revenue").
Price: {price}
Target audience: entrepreneurs and freelancers who want ready-made strategies they can execute immediately.

Structure:
- Compelling title
- "What's Inside" overview section
- 4-5 detailed sections with H2 headings
- Specific tools, templates, and step-by-step instructions
- Realistic expectations for results and timeline
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
            {"role": "system", "content": "Generate a short, punchy, uppercase title for this playbook. Return ONLY the title."},
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
category: "Playbook"
price: "{price}"
readTime: "10 MIN"
excerpt: "{body[:120].replace(chr(10), ' ').replace('"', "'")}..."
---

"""
    content_dir = Path("content/playbooks")
    content_dir.mkdir(parents=True, exist_ok=True)
    filepath = content_dir / f"{slug}.md"
    filepath.write_text(front_matter + body)
    print(f"Created: {filepath}")
