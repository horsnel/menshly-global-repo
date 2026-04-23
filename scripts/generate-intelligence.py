#!/usr/bin/env python3
"""
MenshlyGlobal — Intelligence Article Generator
Generates deep implementation guides — full stack, every resource, everything to get it done.
Posts to: content/intelligence/
"""

import json, os, random, re, sys, time, urllib.parse, urllib.request, urllib.error, ssl
from datetime import datetime, timezone, timedelta

def _clean(val):
    return re.sub(r'[\u200b-\u200f\u2028-\u202e\ufeff\u00ad]', '', val).strip()

API_KEY = _clean(os.environ.get("AI_API_KEY", ""))
API_BASE = _clean((os.environ.get("AI_API_BASE") or "https://api.cerebras.ai/v1")).rstrip("/")
MODEL = _clean(os.environ.get("AI_MODEL") or "llama-3.3-70b")
PEXELS_KEY = _clean(os.environ.get("PEXELS_API_KEY", ""))
PIXABAY_KEY = _clean(os.environ.get("PIXABAY_API_KEY", ""))
MANUAL_TOPIC = _clean(os.environ.get("MANUAL_TOPIC", ""))

def _err(msg):
    os.makedirs("output", exist_ok=True)
    with open("output/error.log", "w") as f: f.write(msg + "\n")
    print(f"ERROR: {msg}"); sys.exit(1)

if not API_KEY: _err("AI_API_KEY not set")

def slugify(text):
    s = text.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s); s = re.sub(r'[\s_]+', '-', s); s = re.sub(r'-+', '-', s)
    return s.strip('-')[:80]

def safe_fetch_json(url, headers=None, timeout=15):
    try:
        ctx = ssl.create_default_context()
        req = urllib.request.Request(url, headers=headers or {})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"  Fetch failed: {e}"); return None

TOPICS = [
    "Complete guide to building an AI chatbot agency from zero to first client",
    "How to build and sell AI automation workflows using Make.com",
    "Step-by-step: building a SaaS product with AI in 30 days",
    "Full-stack guide to launching an AI content business",
    "How to set up an AI-powered lead generation system for B2B clients",
    "Building a custom GPT business: from idea to revenue",
    "Complete implementation guide for AI voice agent services",
    "How to build an AI-powered e-commerce store from scratch",
    "Setting up an AI consulting practice: tools, pricing, and first clients",
    "Full implementation: AI-powered social media management system",
    "How to build and monetize AI workflow templates",
    "Complete guide to AI-powered resume and career services",
    "Building an AI data analysis freelance business step by step",
    "How to create and sell AI prompt libraries for profit",
    "Full-stack implementation of an AI email marketing automation system",
    "How to build an AI-powered course creation business",
    "Complete guide to setting up AI-powered customer service for small businesses",
    "Building profitable AI micro-SaaS products: a technical walkthrough",
    "How to launch an AI SEO agency with free tools",
    "Complete implementation: AI-powered newsletter business from zero"
]

def pick_topic():
    if MANUAL_TOPIC: return MANUAL_TOPIC
    try:
        with open("output/recent_int_topics.json", "r") as f: recent = json.load(f)
    except: recent = []
    available = [t for t in TOPICS if t not in recent]
    if not available: available = TOPICS[:]
    chosen = random.choice(available)
    recent.append(chosen); recent = recent[-20:]
    os.makedirs("output", exist_ok=True)
    with open("output/recent_int_topics.json", "w") as f: json.dump(recent, f)
    return chosen

def fetch_image(query):
    if PEXELS_KEY:
        url = f"https://api.pexels.com/v1/search?query={urllib.parse.quote(query + ' coding technology')}&per_page=3&orientation=landscape"
        data = safe_fetch_json(url, headers={"Authorization": PEXELS_KEY})
        if data and data.get("photos"):
            return data["photos"][0]["src"]["large"]
    if PIXABAY_KEY:
        url = f"https://pixabay.com/api/?key={PIXABAY_KEY}&q={urllib.parse.quote(query + ' programming computer')}&image_type=photo&orientation=horizontal&per_page=3"
        data = safe_fetch_json(url)
        if data and data.get("hits"):
            return data["hits"][0].get("largeImageURL") or data["hits"][0].get("webformatURL", "")
    return ""

def generate_article(topic):
    system_prompt = """You are a content creator for Menshly Global, an AI monetization blog with the tagline "Where AI Meets Revenue". You write for the INTELLIGENCE section — deep implementation guides.

CRITICAL RULES:
- Write a DETAILED implementation guide — the full stack, every resource, everything it takes to get it done
- Include: prerequisites, step-by-step setup, tools needed, code examples where relevant, cost breakdown, timeline, troubleshooting
- Use markdown subheadings (##, ###) for clear structure
- Include a "What You'll Need" section at the top
- Include an "Expected Revenue" section with realistic numbers
- Target length: 800-1200 words
- Be extremely practical and actionable — readers should be able to follow along
- End with a "Quick-Start Checklist" summarizing all steps
- Return ONLY valid JSON: {"title": string, "summary": string, "content": string}"""

    body = json.dumps({
        "model": MODEL, "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Write an Intelligence guide about: \"{topic}\""}
        ], "max_tokens": 4000, "temperature": 0.7
    }).encode()

    req = urllib.request.Request(API_BASE + "/chat/completions", data=body, headers={
        "Content-Type": "application/json", "Authorization": "Bearer " + API_KEY
    })
    try:
        with urllib.request.urlopen(req, timeout=90) as resp: data = json.loads(resp.read().decode())
    except Exception as e: _err(f"AI API error: {e}")

    raw = data.get("choices", [{}])[0].get("message", {}).get("content", "")
    if not raw: _err("AI returned empty response")

    article = None
    try: article = json.loads(raw)
    except: pass
    if not article:
        match = re.search(r'```(?:json)?\s*({.+})\s*```', raw, re.DOTALL)
        if match:
            try: article = json.loads(match.group(1))
            except: pass
    if not article: article = {"title": topic, "summary": raw[:200], "content": raw}
    return article

def main():
    topic = pick_topic()
    print(f"INTELLIGENCE — Topic: {topic}")
    article = generate_article(topic)
    title = article.get("title", topic).strip().replace('"', "'")
    image = fetch_image(topic)
    if not image: print("WARNING: No image found, article will have no image")

    now = datetime.now(timezone.utc) - timedelta(hours=1)
    slug = slugify(title)
    fm = [
        "---",
        f'title: "{title}"',
        f'date: "{now.strftime("%Y-%m-%dT%H:%M:%SZ")}"',
        f'slug: "{slug}"',
        f'categories: ["intelligence"]',
        f'author: "Menshlyglobal Editorials"',
        f'description: "{article.get("summary", "")[:160].replace(chr(34), "")}"',
    ]
    if image: fm.append(f'image: "{image}"')
    fm.extend(["---", ""])

    content = article.get("summary", "") + "\n\n" + article.get("content", "")
    markdown = "\n".join(fm) + content

    post_path = f"content/intelligence/{slug}.md"
    if os.path.exists(post_path):
        print(f"Article '{slug}' already exists — skipping"); return

    os.makedirs("output", exist_ok=True)
    with open("output/article.md", "w") as f: f.write(markdown)
    with open("output/target_section.txt", "w") as f: f.write("intelligence")
    with open("output/target_slug.txt", "w") as f: f.write(slug)
    print(f"Article saved: {post_path}")

if __name__ == "__main__": main()
