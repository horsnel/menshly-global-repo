#!/usr/bin/env python3
"""
MenshlyGlobal — Opportunities Article Generator
Generates discovery/overview articles about new AI models, ideas, and automation systems.
Posts to: content/opportunities/
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
    "How GPT-5 is creating new revenue streams for solo entrepreneurs",
    "The rise of AI agent marketplaces and what it means for your business",
    "Claude's new tool-use capabilities open doors for automation startups",
    "Why AI-powered SaaS is the fastest growing business model in 2026",
    "Midjourney V7 creates new opportunities in print-on-demand businesses",
    "How small businesses are using AI to compete with enterprise companies",
    "The AI automation gold rush: which niches are still untapped",
    "New AI models make it possible to run a one-person agency",
    "Voice AI is transforming customer service — here's the business opportunity",
    "How to profit from the AI API economy as a middleware builder",
    "AI-generated content farms: are they still profitable in 2026",
    "The opportunity in AI-powered personalization for e-commerce",
    "Why every consultant needs an AI co-pilot in 2026",
    "AI code assistants are creating a new breed of solo developers",
    "The untapped market for AI in African small businesses",
    "How to build a six-figure AI automation agency from scratch",
    "The rise of AI-powered marketplaces and platform businesses",
    "Why AI workflow automation is the next big consulting opportunity",
    "New AI video tools create opportunities in content production",
    "How AI is democratizing access to professional services"
]

def pick_topic():
    if MANUAL_TOPIC: return MANUAL_TOPIC
    try:
        with open("output/recent_opp_topics.json", "r") as f: recent = json.load(f)
    except: recent = []
    available = [t for t in TOPICS if t not in recent]
    if not available: available = TOPICS[:]
    chosen = random.choice(available)
    recent.append(chosen); recent = recent[-20:]
    os.makedirs("output", exist_ok=True)
    with open("output/recent_opp_topics.json", "w") as f: json.dump(recent, f)
    return chosen

def fetch_image(query):
    if PEXELS_KEY:
        url = f"https://api.pexels.com/v1/search?query={urllib.parse.quote(query + ' AI technology')}&per_page=3&orientation=landscape"
        data = safe_fetch_json(url, headers={"Authorization": PEXELS_KEY})
        if data and data.get("photos"):
            return data["photos"][0]["src"]["large"]
    if PIXABAY_KEY:
        url = f"https://pixabay.com/api/?key={PIXABAY_KEY}&q={urllib.parse.quote(query + ' artificial intelligence')}&image_type=photo&orientation=horizontal&per_page=3"
        data = safe_fetch_json(url)
        if data and data.get("hits"):
            return data["hits"][0].get("largeImageURL") or data["hits"][0].get("webformatURL", "")
    return ""

def generate_article(topic):
    system_prompt = """You are a content creator for Menshly Global, an AI monetization blog with the tagline "Where AI Meets Revenue". You write for the OPPORTUNITIES section — discovery articles about new AI models, ideas, and automation systems.

CRITICAL RULES:
- Write an exciting discovery/overview article about the OPPORTUNITY
- Focus on: what is it, why it matters, where the money is
- Include revenue potential, market size, and monetization angles
- Use markdown subheadings (##) for structure
- Target length: 500-700 words
- Be specific with concrete examples and actionable takeaways
- End with a "The Revenue Play" section summarizing how to monetize
- Return ONLY valid JSON: {"title": string, "summary": string, "content": string}"""

    body = json.dumps({
        "model": MODEL, "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Write an Opportunities article about: \"{topic}\""}
        ], "max_tokens": 3000, "temperature": 0.8
    }).encode()

    req = urllib.request.Request(API_BASE + "/chat/completions", data=body, headers={
        "Content-Type": "application/json", "Authorization": "Bearer " + API_KEY
    })
    try:
        with urllib.request.urlopen(req, timeout=60) as resp: data = json.loads(resp.read().decode())
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
    print(f"OPPORTUNITIES — Topic: {topic}")
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
        f'categories: ["opportunities"]',
        f'author: "Menshlyglobal Editorials"',
        f'description: "{article.get("summary", "")[:160].replace(chr(34), "")}"',
    ]
    if image: fm.append(f'image: "{image}"')
    fm.extend(["---", ""])

    content = article.get("summary", "") + "\n\n" + article.get("content", "")
    markdown = "\n".join(fm) + content

    post_path = f"content/opportunities/{slug}.md"
    if os.path.exists(post_path):
        print(f"Article '{slug}' already exists — skipping"); return

    os.makedirs("output", exist_ok=True)
    with open("output/article.md", "w") as f: f.write(markdown)
    with open("output/target_section.txt", "w") as f: f.write("opportunities")
    with open("output/target_slug.txt", "w") as f: f.write(slug)
    print(f"Article saved: {post_path}")

if __name__ == "__main__": main()
