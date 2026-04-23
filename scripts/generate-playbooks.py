#!/usr/bin/env python3
"""
MenshlyGlobal — Playbooks Generator
Generates marketplace-ready ebooks, templates, and materials for download/purchase.
Posts to: content/playbooks/
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

PLAYBOOKS = [
    {"title": "The AI Side Hustle Blueprint", "type": "Ebook", "topic": "15 proven AI side hustles you can start this weekend with zero investment", "pages": "45", "price": "Free"},
    {"title": "Automation Agency Starter Kit", "type": "Toolkit", "topic": "Everything you need to launch an AI automation agency including proposal templates and pricing sheets", "pages": "60", "price": "$19"},
    {"title": "ChatGPT Prompt Engineering Playbook", "type": "Ebook", "topic": "200+ revenue-generating prompts for business, content, and automation", "pages": "80", "price": "$9"},
    {"title": "AI Freelancing Rate Calculator Template", "type": "Template", "topic": "Spreadsheet template to calculate your ideal freelance rate based on expenses and goals", "pages": "5", "price": "Free"},
    {"title": "The No-Code AI Business Builder", "type": "Mini-Course", "topic": "Step-by-step mini-course for building AI businesses without writing code", "pages": "30", "price": "$14"},
    {"title": "AI Tool Stack Selection Guide", "type": "Ebook", "topic": "The definitive guide to choosing the right AI tools for every business type and budget", "pages": "55", "price": "$7"},
    {"title": "Client Onboarding Templates for AI Agencies", "type": "Template", "topic": "Professional onboarding documents, questionnaires, and scope templates for AI service businesses", "pages": "15", "price": "Free"},
    {"title": "The AI Revenue Playbook", "type": "Ebook", "topic": "How to turn any AI skill into a revenue stream — from beginner to $10K/month", "pages": "70", "price": "$29"},
    {"title": "Social Media AI Automation Templates", "type": "Template", "topic": "Ready-to-deploy Make.com and Zapier templates for AI-powered social media management", "pages": "20", "price": "$12"},
    {"title": "AI Business Legal Starter Pack", "type": "Toolkit", "topic": "Contracts, terms of service, and privacy policy templates for AI businesses", "pages": "25", "price": "Free"},
    {"title": "The AI Consultant's Field Guide", "type": "Ebook", "topic": "How to position, price, and deliver AI consulting services that clients pay premium for", "pages": "50", "price": "$24"},
    {"title": "Email Automation with AI Workshop Guide", "type": "Mini-Course", "topic": "Complete workshop curriculum for teaching AI email automation to small businesses", "pages": "35", "price": "$16"},
]

def pick_playbook():
    if MANUAL_TOPIC: return {"title": MANUAL_TOPIC, "type": "Ebook", "topic": MANUAL_TOPIC, "pages": "30", "price": "Free"}
    try:
        with open("output/recent_pb_topics.json", "r") as f: recent = json.load(f)
    except: recent = []
    available = [p for p in PLAYBOOKS if p["title"] not in recent]
    if not available: available = PLAYBOOKS[:]
    chosen = random.choice(available)
    recent.append(chosen["title"]); recent = recent[-15:]
    os.makedirs("output", exist_ok=True)
    with open("output/recent_pb_topics.json", "w") as f: json.dump(recent, f)
    return chosen

def fetch_image(query):
    if PEXELS_KEY:
        url = f"https://api.pexels.com/v1/search?query={urllib.parse.quote(query + ' book ebook')}&per_page=3&orientation=landscape"
        data = safe_fetch_json(url, headers={"Authorization": PEXELS_KEY})
        if data and data.get("photos"):
            return data["photos"][0]["src"]["large"]
    if PIXABAY_KEY:
        url = f"https://pixabay.com/api/?key={PIXABAY_KEY}&q={urllib.parse.quote(query + ' business book')}&image_type=photo&orientation=horizontal&per_page=3"
        data = safe_fetch_json(url)
        if data and data.get("hits"):
            return data["hits"][0].get("largeImageURL") or data["hits"][0].get("webformatURL", "")
    return ""

def generate_playbook(playbook):
    system_prompt = f"""You are a content creator for Menshly Global, an AI monetization blog with the tagline "Where AI Meets Revenue". You write for the PLAYBOOKS section — marketplace-ready materials for download/purchase.

CRITICAL RULES:
- Write a PREVIEW/SAMPLE of a {playbook["type"].lower()} titled "{playbook["title"]}"
- Include: what's inside, key takeaways, a sample chapter/section, and who it's for
- Format as a marketplace listing with enough detail to convince someone to download/buy
- Use markdown subheadings (##, ###) for structure
- Include "What's Inside" section listing all chapters/modules
- Include a "Who This Is For" section
- Include a sample excerpt from one chapter
- Target length: 400-600 words
- Return ONLY valid JSON: {{"title": string, "summary": string, "content": string}}"""

    body = json.dumps({
        "model": MODEL, "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Create a Playbook listing for: \"{playbook['topic']}\""}
        ], "max_tokens": 3000, "temperature": 0.7
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
    if not article: article = {"title": playbook["title"], "summary": raw[:200], "content": raw}
    return article

def main():
    playbook = pick_playbook()
    print(f"PLAYBOOKS — {playbook['type']}: {playbook['title']}")
    article = generate_playbook(playbook)
    title = article.get("title", playbook["title"]).strip().replace('"', "'")
    image = fetch_image(playbook["topic"])

    now = datetime.now(timezone.utc) - timedelta(hours=1)
    slug = slugify(title)
    fm = [
        "---",
        f'title: "{title}"',
        f'date: "{now.strftime("%Y-%m-%dT%H:%M:%SZ")}"',
        f'slug: "{slug}"',
        f'categories: ["playbooks"]',
        f'author: "Menshlyglobal Editorials"',
        f'description: "{article.get("summary", "")[:160].replace(chr(34, "")}"',
        f'type: "{playbook["type"]}"',
        f'pages: "{playbook["pages"]}"',
        f'price: "{playbook["price"]}"',
    ]
    if image: fm.append(f'image: "{image}"')
    fm.extend(["---", ""])

    content = article.get("summary", "") + "\n\n" + article.get("content", "")
    markdown = "\n".join(fm) + content

    post_path = f"content/playbooks/{slug}.md"
    if os.path.exists(post_path):
        print(f"Playbook '{slug}' already exists — skipping"); return

    os.makedirs("output", exist_ok=True)
    with open("output/article.md", "w") as f: f.write(markdown)
    with open("output/target_section.txt", "w") as f: f.write("playbooks")
    with open("output/target_slug.txt", "w") as f: f.write(slug)
    print(f"Playbook saved: {post_path}")

if __name__ == "__main__": main()
