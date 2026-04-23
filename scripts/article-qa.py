#!/usr/bin/env python3
"""
MenshlyGlobal — Article QA Verification Script
Verifies articles BEFORE they can be published to the homepage.
Called by GitHub Actions workflow and the promote-to-homepage Cloudflare function.

Checks:
  A. Content Authenticity — ripped/fake/low-quality content detection
  B. Image-Article Relevance — ripped images, stock vs news source, relevance scoring
  C. Auto-Fix — repair malformed front matter, replace bad images, fill missing fields
  D. Reject — move failing articles to output/rejected/

Environment variables (same as auto-generate.py):
  AI_API_KEY   — AI API key (Cerebras / compatible)
  AI_API_BASE  — API base URL (default: https://api.cerebras.ai/v1)
  AI_MODEL     — Model name (default: auto-detect)
  PEXELS_API_KEY  — Pexels API key (image source 1)
  PIXABAY_API_KEY — Pixabay API key (image source 2)
  FREPIK_API_KEY  — Freepik API key (image source 3)

Usage:
  python scripts/article-qa.py --dir content/posts/
  python scripts/article-qa.py --dir content/posts/ --fix
  python scripts/article-qa.py --dir content/posts/ --reject
  python scripts/article-qa.py --file content/posts/some-article.md --fix
"""

import argparse
import json
import os
import re
import shutil
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

# ── Configuration ──────────────────────────────────────────
def _clean(val):
    """Strip invisible Unicode chars that break HTTP headers (e.g. copy-paste LRM/RLO)."""
    return re.sub(r'[\u200b-\u200f\u2028-\u202e\ufeff\u00ad]', '', val).strip()

API_KEY = _clean(os.environ.get("AI_API_KEY", ""))
API_BASE = _clean((os.environ.get("AI_API_BASE") or "https://api.cerebras.ai/v1")).rstrip("/")
MODEL = _clean(os.environ.get("AI_MODEL") or "")
PEXELS_KEY = _clean(os.environ.get("PEXELS_API_KEY", ""))
PIXABAY_KEY = _clean(os.environ.get("PIXABAY_API_KEY", ""))
FREPIK_KEY = _clean(os.environ.get("FREPIK_API_KEY", ""))

# ── Valid categories (must match auto-generate.py) ──────────
VALID_CATEGORIES = [
    "entertainment", "finance", "technology", "business",
    "health", "science", "world"
]

DEFAULT_AUTHOR = "Menshlyglobal Editorials"
DEFAULT_CATEGORY = "world"

# ── Ripped content indicators ─────────────────────────────
RIPPED_PATTERNS = [
    r'<div\s+class="cnn-header"',
    r'<div\s+class="[\w-]*header[\w-]*"',
    r'MENSHLY\s+GLOBAL\s*//\s*OFFICIAL\s+DISPATCH',
    r'OFFICIAL\s+DISPATCH',
    r'@Olhmescraxes1',
    r'olhmescraxes',
]

# Inline HTML image tags (legitimate Hugo markdown should not have these in body)
INLINE_IMG_PATTERN = re.compile(r'<img\s+src=', re.IGNORECASE)

# Empty iframe pattern (spam artifact)
EMPTY_IFRAME_PATTERN = re.compile(r'<iframe[^>]*src\s*=\s*["\']\s*["\']', re.IGNORECASE)

# ── Model auto-detection ──────────────────────────────────
MODEL_PREFERENCES = [
    "llama-3.3-70b",
    "llama3.1-8b",
    "deepseek-r1-distill-llama-70b",
    "qwen-3-235b-a22b-instruct-2507"
]

ACTIVE_MODEL = None

def auto_detect_model():
    """Query the API for available models and pick the best one."""
    global ACTIVE_MODEL
    try:
        req = urllib.request.Request(
            API_BASE + "/models",
            headers={
                "Authorization": "Bearer " + API_KEY,
                "User-Agent": "MenshlyGlobal/1.0 (Bot; +https://menshly-global.pages.dev)"
            }
        )
        ctx = ssl.create_default_context()
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            data = json.loads(resp.read().decode())
        available = [m["id"] for m in data.get("data", [])]
        print(f"  QA — Available models: {', '.join(sorted(available))}")

        if MODEL and MODEL in available:
            print(f"  QA — Using configured model: {MODEL}")
            ACTIVE_MODEL = MODEL
            return MODEL
        elif MODEL:
            print(f"  QA — Configured model '{MODEL}' not found, auto-detecting...")

        for pref in MODEL_PREFERENCES:
            if pref in available:
                print(f"  QA — Auto-selected: {pref}")
                ACTIVE_MODEL = pref
                return pref

        fallback = available[0] if available else "llama-3.3-70b"
        print(f"  QA — Using fallback model: {fallback}")
        ACTIVE_MODEL = fallback
        return fallback
    except Exception as e:
        print(f"  QA — Could not list models ({e}). Using: {MODEL or 'llama-3.3-70b'}")
        ACTIVE_MODEL = MODEL or "llama-3.3-70b"
        return ACTIVE_MODEL


# ── Utility functions (copied from auto-generate.py) ──────
def slugify(text):
    """Convert text to URL-safe slug."""
    s = text.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'-+', '-', s)
    s = s.strip('-')
    return s[:80] if len(s) > 80 else s

def safe_fetch_json(url, headers=None, timeout=15):
    """Fetch JSON from URL — returns None on failure instead of crashing."""
    try:
        ctx = ssl.create_default_context()
        req = urllib.request.Request(url, headers=headers or {})
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"    Fetch failed: {e}")
        return None

def extract_subject_words(topic, title=None):
    """Extract the most important subject nouns from a topic/title for image search."""
    text = (title or topic).lower()
    stop_words = set([
        "the", "a", "an", "of", "in", "on", "for", "to", "and", "or", "is",
        "are", "was", "were", "be", "been", "being", "have", "has", "had",
        "how", "what", "why", "when", "where", "who", "which", "that", "this",
        "it", "its", "with", "from", "by", "at", "as", "but", "not", "no",
        "can", "could", "will", "would", "should", "may", "might", "must",
        "do", "does", "did", "about", "into", "over", "after", "before",
        "between", "under", "through", "during", "without", "within",
        "all", "each", "every", "both", "few", "more", "most", "other",
        "some", "such", "than", "too", "very", "just", "also", "now",
        "new", "your", "you", "we", "they", "our", "their", "my",
        "best", "top", "guide", "tips", "ways", "ideas", "things",
        "means", "could", "hints", "suggests", "heading", "future",
        "complete", "practical", "simple", "expert", "ultimate"
    ])
    words = [w.strip(".,!?;:'\"()-") for w in text.split()]
    subjects = [w for w in words if w not in stop_words and len(w) > 2]
    return " ".join(subjects[:4]) if subjects else topic.split()[:2]

def build_image_query(topic, category_key):
    """Build image search query using extracted subject words."""
    return extract_subject_words(topic)

IMAGE_KEYWORDS = {
    "entertainment": ["cinema", "music concert", "celebrity", "film set", "stage performance", "movie theater", "red carpet"],
    "finance": ["finance", "money savings", "investment chart", "banking", "wallet coins", "stock market", "gold coins"],
    "technology": ["technology", "computer laptop", "digital innovation", "smartphone", "coding", "circuit board", "robot"],
    "business": ["business meeting", "office corporate", "entrepreneur", "startup team", "handshake", "office desk", "corporate"],
    "health": ["health fitness", "yoga wellness", "healthy food", "medical care", "exercise", "running", "meditation"],
    "science": ["science laboratory", "space galaxy", "microscope research", "chemistry", "nature", "telescope", "DNA"],
    "world": ["world map globe", "city skyline", "diverse culture", "african landscape", "travel", "earth from space", "global"]
}

def score_image_relevance(photo_data, topic, category_key):
    """Score how relevant an image is to the topic (0-100)."""
    score = 50
    topic_lower = topic.lower()
    topic_words = set(topic_lower.split())
    tags = []
    description = ""
    if isinstance(photo_data, dict):
        if photo_data.get("tags"):
            tags = [str(t).lower() for t in photo_data["tags"]]
        if photo_data.get("description"):
            description = str(photo_data["description"]).lower()
        if photo_data.get("alt"):
            description += " " + str(photo_data["alt"]).lower()
    all_text = " ".join(tags) + " " + description
    for word in topic_words:
        if len(word) > 3 and word in all_text:
            score += 15
    cat_keywords = IMAGE_KEYWORDS.get(category_key, [])
    for kw in cat_keywords[:3]:
        if kw in all_text:
            score += 5
    if not tags and not description:
        score -= 20
    return min(score, 100)


# ── Pexels Image Source ────────────────────────────────────
def fetch_pexels_image(topic, category_key):
    """Source 1: Fetch image from Pexels."""
    if not PEXELS_KEY:
        return None
    query = build_image_query(topic, category_key)
    url = f"https://api.pexels.com/v1/search?query={urllib.parse.quote(query)}&per_page=5&orientation=landscape"
    print(f"    [Pexels] Searching: {query}")
    data = safe_fetch_json(url, headers={"Authorization": PEXELS_KEY}, timeout=15)
    if not data or not data.get("photos"):
        print("    [Pexels] No results")
        return None
    best = None
    best_score = 0
    for photo in data["photos"][:5]:
        s = score_image_relevance(photo, topic, category_key)
        if s > best_score:
            best_score = s
            best = photo
    if best:
        print(f"    [Pexels] Best match scored {best_score}/100")
        return {
            "url": best["src"]["large"],
            "thumb": best["src"]["medium"],
            "credit": best["photographer"],
            "credit_url": best["photographer_url"],
            "source": "Pexels",
            "score": best_score
        }
    return None


# ── Pixabay Image Source ───────────────────────────────────
def fetch_pixabay_image(topic, category_key):
    """Source 2: Fetch image from Pixabay."""
    if not PIXABAY_KEY:
        return None
    query = build_image_query(topic, category_key)
    url = f"https://pixabay.com/api/?key={PIXABAY_KEY}&q={urllib.parse.quote(query)}&image_type=photo&orientation=horizontal&per_page=5&safesearch=true"
    print(f"    [Pixabay] Searching: {query}")
    data = safe_fetch_json(url, timeout=15)
    if not data or not data.get("hits"):
        print("    [Pixabay] No results")
        return None
    best = None
    best_score = 0
    for hit in data["hits"][:5]:
        s = score_image_relevance(hit, topic, category_key)
        if s > best_score:
            best_score = s
            best = hit
    if best:
        print(f"    [Pixabay] Best match scored {best_score}/100")
        img_url = best.get("largeImageURL") or best.get("webformatURL", "")
        if not img_url:
            return None
        return {
            "url": img_url,
            "thumb": best.get("webformatURL", img_url),
            "credit": best.get("user", "Pixabay User"),
            "credit_url": f"https://pixabay.com/users/{best.get('user_id', '')}-{best.get('user', '')}/",
            "source": "Pixabay",
            "score": best_score
        }
    return None


# ── Freepik Image Source ───────────────────────────────────
def fetch_freepik_image(topic, category_key):
    """Source 3: Fetch image from Freepik API."""
    if not FREPIK_KEY:
        return None
    query = build_image_query(topic, category_key)
    url = f"https://api.freepik.com/v1/resources?locale=en-US&phrase={urllib.parse.quote(query)}&image_type=photo&orientation=landscape&limit=5&order=relevance"
    print(f"    [Freepik] Searching: {query}")
    data = safe_fetch_json(url, headers={
        "Accept-Language": "en-US",
        "Accept": "application/json",
        "Authorization": f"Bearer {FREPIK_KEY}"
    }, timeout=15)
    if not data or not data.get("data"):
        print("    [Freepik] No results")
        return None
    best = None
    best_score = 0
    for item in data["data"][:5]:
        s = score_image_relevance(item, topic, category_key)
        if s > best_score:
            best_score = s
            best = item
    if best:
        print(f"    [Freepik] Best match scored {best_score}/100")
        thumbs = best.get("thumbnails", [])
        img_url = ""
        for t in thumbs:
            if t.get("width", 0) >= 1280:
                img_url = t.get("url", "")
                break
        if not img_url and thumbs:
            img_url = thumbs[-1].get("url", "")
        if not img_url:
            return None
        thumb_url = thumbs[0].get("url", img_url) if thumbs else img_url
        return {
            "url": img_url,
            "thumb": thumb_url,
            "credit": best.get("creator", {}).get("name", "Freepik Contributor"),
            "credit_url": best.get("creator", {}).get("url", ""),
            "source": "Freepik",
            "score": best_score
        }
    return None


# ── Unified image fetcher with fallback chain ──────────────
def fetch_best_image(topic, category_key, article_title=None):
    """Try all 3 image sources, pick the highest-scoring result."""
    search_text = article_title if article_title else topic
    print(f"  Searching images for: {search_text}")
    candidates = []
    pexels_result = fetch_pexels_image(search_text, category_key)
    if pexels_result:
        candidates.append(pexels_result)
    pixabay_result = fetch_pixabay_image(search_text, category_key)
    if pixabay_result:
        candidates.append(pixabay_result)
    freepik_result = fetch_freepik_image(search_text, category_key)
    if freepik_result:
        candidates.append(freepik_result)
    if not candidates:
        print("  No images found from any source")
        return None
    candidates.sort(key=lambda x: x.get("score", 0), reverse=True)
    winner = candidates[0]
    print(f"  Winner: {winner['source']} (score {winner.get('score', 0)}/100)")
    return winner


# ── AI API call helper ─────────────────────────────────────
def call_ai(system_prompt, user_prompt, max_tokens=800, temperature=0.3):
    """Call AI API and return the text response. Returns None on failure."""
    if not API_KEY:
        print("  QA — AI_API_KEY not set, skipping AI checks")
        return None

    global ACTIVE_MODEL
    if not ACTIVE_MODEL:
        auto_detect_model()

    body = json.dumps({
        "model": ACTIVE_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "max_tokens": max_tokens,
        "temperature": temperature
    }).encode()

    req = urllib.request.Request(
        API_BASE + "/chat/completions",
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + API_KEY,
            "User-Agent": "MenshlyGlobal/1.0 (Bot; +https://menshly-global.pages.dev)"
        }
    )

    try:
        ctx = ssl.create_default_context()
        with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
            data = json.loads(resp.read().decode())
        return data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    except urllib.error.HTTPError as e:
        error_body = e.read().decode() if e.fp else "No details"
        print(f"  QA — AI API error {e.code}: {error_body[:200]}")
        return None
    except urllib.error.URLError as e:
        print(f"  QA — AI API connection error: {e.reason}")
        return None
    except Exception as e:
        print(f"  QA — AI call failed: {e}")
        return None


# ── Parse Hugo front matter ────────────────────────────────
def parse_front_matter(content):
    """Parse Hugo markdown front matter. Returns (metadata_dict, body_text).
    Handles both valid and slightly malformed front matter."""
    metadata = {}
    body = ""
    
    if not content.startswith("---"):
        # No front matter at all
        return metadata, content
    
    # Find closing ---
    parts = content.split("---", 2)
    if len(parts) < 3:
        # Malformed — only opening --- or missing closing ---
        return metadata, content
    
    fm_text = parts[1]
    body = parts[2].strip() if len(parts) > 2 else ""
    
    # Parse YAML-like front matter (simple key: value parser)
    for line in fm_text.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        
        # Handle key: "value" or key: value
        match = re.match(r'^(\w+)\s*:\s*(.+)$', line)
        if match:
            key = match.group(1).strip()
            value = match.group(2).strip().strip('"').strip("'")
            metadata[key] = value
        # Handle key: ["value1", "value2"] (array)
        elif re.match(r'^-\s+', line):
            # This is an array item — skip for simple parsing
            pass
    
    return metadata, body


def count_body_words(body):
    """Count words in article body, stripping HTML tags first."""
    # Remove HTML tags
    clean = re.sub(r'<[^>]+>', '', body)
    # Remove markdown formatting
    clean = re.sub(r'[#*_\[\]()>]', ' ', clean)
    # Count words
    words = clean.split()
    return len(words)


def is_video_only(body):
    """Check if article body is essentially just a video embed."""
    # Strip whitespace
    clean = body.strip()
    if not clean:
        return True
    
    # Remove all iframe/embed HTML
    no_embeds = re.sub(r'<iframe[^>]*>.*?</iframe>', '', clean, flags=re.DOTALL | re.IGNORECASE)
    no_embeds = re.sub(r'<iframe[^>]*/?>', '', no_embeds, flags=re.IGNORECASE)
    no_embeds = re.sub(r'\{\{<\s*youtube[^>]*>\}\}', '', no_embeds)
    no_embeds = re.sub(r'\{\{<\s*vimeo[^>]*>\}\}', '', no_embeds)
    no_embeds = re.sub(r'\{\{<\s*dailymotion[^>]*>\}\}', '', no_embeds)
    
    # Remove remaining HTML tags
    no_embeds = re.sub(r'<[^>]+>', '', no_embeds)
    # Remove markdown
    no_embeds = re.sub(r'[#*_\[\]()>]', ' ', no_embeds)
    
    words = no_embeds.split()
    return len(words) < 30


def detect_ripped_content(body):
    """Check for signs of ripped/copied content from external sources."""
    issues = []
    
    # Check ripped patterns
    for pattern in RIPPED_PATTERNS:
        if re.search(pattern, body, re.IGNORECASE):
            issues.append(f"Ripped content pattern: {pattern}")
    
    # Check for inline <img src= tags in body (not Hugo-standard)
    if INLINE_IMG_PATTERN.search(body):
        inline_count = len(INLINE_IMG_PATTERN.findall(body))
        if inline_count >= 1:
            issues.append(f"Inline <img> tags in body ({inline_count} found) — indicates ripped HTML")
    
    # Check for empty iframes (spam artifact)
    if EMPTY_IFRAME_PATTERN.search(body):
        issues.append("Empty <iframe> tags found — spam artifact")
    
    # Check for <figure> tags with inline images (ripped from other sites)
    figure_img_count = len(re.findall(r'<figure[^>]*>.*?<img\s+src=', body, re.DOTALL | re.IGNORECASE))
    if figure_img_count >= 2:
        issues.append(f"Multiple <figure><img> blocks ({figure_img_count}) — likely ripped HTML")
    
    # Check for <div> styling in body (not standard markdown)
    div_style_count = len(re.findall(r'<div\s+style=', body, re.IGNORECASE))
    if div_style_count >= 2:
        issues.append(f"Multiple styled <div> tags ({div_style_count}) — likely ripped HTML")
    
    # Check for social media handle spam
    if re.search(r'follow\s+@\w+\s+on\s+(twitter|x)', body, re.IGNORECASE):
        issues.append("Social media handle spam in body")
    
    return issues


def check_front_matter_quality(metadata):
    """Check for missing or malformed front matter fields."""
    issues = []
    
    # Missing essential fields
    if not metadata.get("categories") and not metadata.get("category"):
        issues.append("Missing 'categories' field")
    
    if not metadata.get("author"):
        issues.append("Missing 'author' field")
    
    if not metadata.get("description"):
        issues.append("Missing 'description' field")
    
    if not metadata.get("title"):
        issues.append("Missing 'title' field")
    
    if not metadata.get("date"):
        issues.append("Missing 'date' field")
    
    # Check for malformed fields — excessive whitespace
    for key, value in metadata.items():
        if isinstance(value, str):
            if value != value.strip():
                issues.append(f"Field '{key}' has leading/trailing whitespace")
            if re.search(r'\s{3,}', value):
                issues.append(f"Field '{key}' has excessive internal whitespace")
    
    # Check for encoding issues in title/description (? replacing special chars)
    for field in ["title", "description"]:
        val = metadata.get(field, "")
        if val and "?" in val and re.search(r'\?{2,}', val):
            issues.append(f"Field '{field}' has encoding errors (?)")
    
    return issues


def ai_verify_content(title, description, body_snippet):
    """Use AI to analyze content authenticity. Returns dict with verdict and reason."""
    if not API_KEY:
        return {"verdict": "SKIP", "reason": "AI_API_KEY not set, AI verification skipped"}
    
    # Truncate body to save tokens
    snippet = body_snippet[:1500] if len(body_snippet) > 1500 else body_snippet
    
    system_prompt = """You are a content quality auditor for a media platform. Analyze the article snippet and classify it as ONE of:
- LEGITIMATE: Original analysis, opinion, guide, or review piece
- RIPPED: Copied/ripped news article from another source (looks like a raw news feed dump)
- MISINFORMATION: Generated misinformation with fabricated claims or fake statistics
- LOW_QUALITY: Insufficient content, repetitive, or no substance

Respond with ONLY a JSON object: {"verdict": "LEGITIMATE|RIPPED|MISINFORMATION|LOW_QUALITY", "reason": "brief explanation"}"""

    user_prompt = f"""Title: {title}
Description: {description}

Article body (excerpt):
{snippet}"""

    response = call_ai(system_prompt, user_prompt, max_tokens=200, temperature=0.1)
    if not response:
        return {"verdict": "SKIP", "reason": "AI call failed, skipping content verification"}
    
    # Parse AI response
    try:
        # Try direct JSON parse
        result = json.loads(response)
        return result
    except json.JSONDecodeError:
        # Try extracting JSON from response
        json_match = re.search(r'\{[^}]+\}', response, re.DOTALL)
        if json_match:
            try:
                result = json.loads(json_match.group())
                return result
            except json.JSONDecodeError:
                pass
    
    # Fallback: check for keywords in response
    response_lower = response.lower()
    if "ripped" in response_lower:
        return {"verdict": "RIPPED", "reason": "AI classified as ripped content"}
    elif "misinformation" in response_lower:
        return {"verdict": "MISINFORMATION", "reason": "AI classified as misinformation"}
    elif "low_quality" in response_lower or "low quality" in response_lower:
        return {"verdict": "LOW_QUALITY", "reason": "AI classified as low quality"}
    else:
        return {"verdict": "LEGITIMATE", "reason": "AI classified as legitimate (default)"}


def ai_check_image_source(image_url):
    """Use AI to evaluate if an image URL is from a stock photo or ripped from a news site.
    Returns dict with source_type and reason."""
    if not API_KEY:
        return {"source_type": "UNKNOWN", "reason": "AI_API_KEY not set"}
    
    system_prompt = """You are an image source analyzer. Given an image URL, determine if it comes from:
- STOCK: Stock photo sites (Pexels, Pixabay, Freepik, Unsplash, Picsum)
- NEWS: News/media sites (Bloomberg, Moneycontrol, CNN, Reuters, etc.)
- SOCIAL: Social media (Instagram, Twitter/X, Facebook)
- OTHER: Other sources

Respond with ONLY JSON: {"source_type": "STOCK|NEWS|SOCIAL|OTHER", "reason": "brief explanation"}"""

    user_prompt = f"Image URL: {image_url}"

    response = call_ai(system_prompt, user_prompt, max_tokens=100, temperature=0.1)
    if not response:
        # Fallback: check URL patterns ourselves
        return check_image_source_heuristic(image_url)
    
    try:
        result = json.loads(response)
        return result
    except json.JSONDecodeError:
        json_match = re.search(r'\{[^}]+\}', response, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group())
            except json.JSONDecodeError:
                pass
    
    return check_image_source_heuristic(image_url)


def check_image_source_heuristic(image_url):
    """Heuristic check for image source without AI."""
    url_lower = image_url.lower()
    
    stock_domains = ["pexels.com", "pixabay.com", "freepik.com", "unsplash.com", "picsum.photos"]
    news_domains = ["bloomberg.com", "moneycontrol.com", "cnn.com", "reuters.com", "bbc.co.uk",
                    "nytimes.com", "theguardian.com", "wsj.com", "ft.com", "cnbc.com",
                    "aljazeera.com", "news.yahoo.com", "apnews.com"]
    
    for domain in stock_domains:
        if domain in url_lower:
            return {"source_type": "STOCK", "reason": f"Stock photo domain: {domain}"}
    
    for domain in news_domains:
        if domain in url_lower:
            return {"source_type": "NEWS", "reason": f"News site domain: {domain} — likely ripped"}
    
    return {"source_type": "OTHER", "reason": "Unknown source"}


def ai_check_image_relevance(title, description, image_url):
    """Use AI to score image-article relevance (0-100).
    Returns relevance score."""
    if not API_KEY:
        return 50  # Neutral score when AI not available
    
    system_prompt = """You are an image relevance scorer. Given an article title, description, and image URL, score how relevant the image is to the article topic on a scale of 0-100.

Consider:
- Does the image URL suggest a photo that matches the article subject?
- Is the image from a stock photo search for this topic, or is it unrelated?

Respond with ONLY a JSON object: {"score": <0-100>, "reason": "brief explanation"}"""

    user_prompt = f"""Title: {title}
Description: {description}
Image URL: {image_url}"""

    response = call_ai(system_prompt, user_prompt, max_tokens=100, temperature=0.1)
    if not response:
        return 50
    
    try:
        result = json.loads(response)
        score = int(result.get("score", 50))
        return max(0, min(100, score))
    except (json.JSONDecodeError, ValueError, TypeError):
        json_match = re.search(r'"score"\s*:\s*(\d+)', response)
        if json_match:
            try:
                return max(0, min(100, int(json_match.group(1))))
            except ValueError:
                pass
    
    return 50


# ── Auto-fix functions ─────────────────────────────────────
def fix_front_matter(content, metadata):
    """Fix malformed front matter and return the corrected full content."""
    if not content.startswith("---"):
        # No front matter — create one
        title = metadata.get("title", "Untitled Article")
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        slug = slugify(title)
        
        fm = f"""---
title: "{title}"
date: "{date_str}"
slug: "{slug}"
categories: ["{DEFAULT_CATEGORY}"]
author: "{DEFAULT_AUTHOR}"
description: ""
---

"""
        # Find where the actual body starts (skip any non-front-matter header)
        return fm + content
    
    # Parse existing front matter and rebuild it clean
    parts = content.split("---", 2)
    if len(parts) < 3:
        return content  # Can't fix
    
    fm_text = parts[1]
    body = parts[2] if len(parts) > 2 else ""
    
    # Re-parse front matter lines and clean them
    clean_lines = []
    for line in fm_text.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        
        # Fix whitespace in key: value pairs
        match = re.match(r'^(\w+)\s*:\s*(.+)$', stripped)
        if match:
            key = match.group(1)
            value = match.group(2).strip()
            # Clean excessive whitespace in value
            value = re.sub(r'\s{2,}', ' ', value)
            clean_lines.append(f'{key}: {value}')
    
    # Add missing essential fields
    keys_present = set()
    for line in clean_lines:
        match = re.match(r'^(\w+)\s*:', line)
        if match:
            keys_present.add(match.group(1))
    
    if "title" not in keys_present:
        clean_lines.insert(0, 'title: "Untitled Article"')
    if "date" not in keys_present:
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        clean_lines.append(f'date: "{date_str}"')
    if "categories" not in keys_present and "category" not in keys_present:
        clean_lines.append(f'categories: ["{DEFAULT_CATEGORY}"]')
    if "author" not in keys_present:
        clean_lines.append(f'author: "{DEFAULT_AUTHOR}"')
    if "description" not in keys_present:
        clean_lines.append('description: ""')
    
    # Rebuild
    new_fm = "---\n" + "\n".join(clean_lines) + "\n---\n"
    return new_fm + body


def fix_missing_fields(metadata, content):
    """Fix missing author and categories in content. Returns modified content."""
    parts = content.split("---", 2)
    if len(parts) < 3:
        return content
    
    fm_text = parts[1]
    body = parts[2] if len(parts) > 2 else ""
    
    # Fix missing/invalid author
    author = metadata.get("author", "")
    valid_authors = [
        "Menshlyglobal Editorials",
        DEFAULT_AUTHOR
    ]
    if not author or author not in valid_authors:
        fm_text = re.sub(r'^author\s*:.*$', f'author: "{DEFAULT_AUTHOR}"', fm_text, flags=re.MULTILINE)
        if "author" not in fm_text:
            fm_text += f'\nauthor: "{DEFAULT_AUTHOR}"'
    
    # Fix missing categories
    categories = metadata.get("categories", "")
    if not categories:
        fm_text = re.sub(r'^categories\s*:.*$', f'categories: ["{DEFAULT_CATEGORY}"]', fm_text, flags=re.MULTILINE)
        if "categories" not in fm_text:
            fm_text += f'\ncategories: ["{DEFAULT_CATEGORY}"]'
    else:
        # Validate categories
        cat_clean = categories.strip("[]\"' ")
        if cat_clean not in VALID_CATEGORIES:
            fm_text = re.sub(r'^categories\s*:.*$', f'categories: ["{DEFAULT_CATEGORY}"]', fm_text, flags=re.MULTILINE)
    
    # Fix missing description
    desc = metadata.get("description", "")
    if not desc:
        # Extract first 160 chars of body as description
        clean_body = re.sub(r'<[^>]+>', '', body)
        clean_body = re.sub(r'[#*_\[\]()>]', ' ', clean_body).strip()
        auto_desc = clean_body[:160].replace('"', "'")
        fm_text = re.sub(r'^description\s*:.*$', f'description: "{auto_desc}"', fm_text, flags=re.MULTILINE)
        if "description" not in fm_text:
            fm_text += f'\ndescription: "{auto_desc}"'
    
    return "---" + fm_text + "---" + body


def replace_image_in_content(content, new_image_url):
    """Replace the image field in front matter with a new URL."""
    # Replace existing image line
    new_content = re.sub(
        r'^image\s*:.*$',
        f'image: "{new_image_url}"',
        content,
        flags=re.MULTILINE
    )
    
    # If no image field existed, add it after the date line
    if "image:" not in content:
        new_content = re.sub(
            r'^(date\s*:.*$)',
            f'\\1\nimage: "{new_image_url}"',
            new_content,
            flags=re.MULTILINE
        )
    
    return new_content


def remove_ripped_html_body(content):
    """Remove ripped HTML artifacts from article body while keeping markdown content."""
    parts = content.split("---", 2)
    if len(parts) < 3:
        return content
    
    fm_text = parts[1]
    body = parts[2] if len(parts) > 2 else ""
    
    # Remove <figure> blocks with inline images (but keep any text inside)
    body = re.sub(r'<figure[^>]*>.*?</figure>', '', body, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove empty iframes
    body = re.sub(r'<iframe[^>]*src\s*=\s*["\']\s*["\'][^>]*>.*?</iframe>', '', body, flags=re.DOTALL | re.IGNORECASE)
    body = re.sub(r'<iframe[^>]*/?>', '', body, flags=re.IGNORECASE)
    
    # Remove styled divs (but keep content)
    body = re.sub(r'<div[^>]*>', '', body, flags=re.IGNORECASE)
    body = re.sub(r'</div>', '', body, flags=re.IGNORECASE)
    
    # Remove <figcaption> blocks
    body = re.sub(r'<figcaption[^>]*>.*?</figcaption>', '', body, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove social media spam lines
    body = re.sub(r'For live updates.*?follow\s+@\w+\s+on\s+(Twitter|X)\.?', '', body, flags=re.IGNORECASE | re.DOTALL)
    body = re.sub(r'To stay up-to-date.*?follow\s+@\w+\s+on\s+(Twitter|X)[^.]*\.', '', body, flags=re.IGNORECASE | re.DOTALL)
    body = re.sub(r'Stay connected with our lead analyst on X.*?</p>', '', body, flags=re.IGNORECASE | re.DOTALL)
    body = re.sub(r'Follow\s+@\w+\s+now.*?curve\.?', '', body, flags=re.IGNORECASE | re.DOTALL)
    body = re.sub(r'<p[^>]*>\s*@?\w*olhmescraxes[^<]*</p>', '', body, flags=re.IGNORECASE | re.DOTALL)
    body = re.sub(r'<p[^>]*style="text-align:center[^"]*"[^>]*>\s*Stay connected.*?</p>', '', body, flags=re.IGNORECASE | re.DOTALL)
    
    # Remove any remaining @Olhmescraxes references
    body = re.sub(r'@Olhmescraxes\w*\s*', '', body, flags=re.IGNORECASE)
    body = re.sub(r'olhmescraxes\w*', '', body, flags=re.IGNORECASE)
    
    # Remove <hr> separators that are spam artifacts
    body = re.sub(r'\n<hr>\n', '\n', body)
    
    # Clean up excessive blank lines
    body = re.sub(r'\n{3,}', '\n\n', body)
    
    return "---" + fm_text + "---" + body


# ── Main QA verification ──────────────────────────────────
def verify_article(filepath, do_fix=False):
    """Verify a single article. Returns a result dict."""
    filename = os.path.basename(filepath)
    result = {
        "file": filepath,
        "filename": filename,
        "status": "PASS",
        "issues": [],
        "warnings": [],
        "fixes_applied": [],
        "content_modified": False,
    }
    
    # Read file
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
    except Exception as e:
        result["status"] = "FAIL"
        result["issues"].append(f"Cannot read file: {e}")
        return result
    
    if not content.strip():
        result["status"] = "FAIL"
        result["issues"].append("File is empty")
        return result
    
    # Parse front matter
    metadata, body = parse_front_matter(content)
    
    title = metadata.get("title", "")
    description = metadata.get("description", "")
    image_url = metadata.get("image", "")
    categories = metadata.get("categories", "")
    
    # ═══════════════════════════════════════════════════════
    # A. Content Authenticity Verification
    # ═══════════════════════════════════════════════════════
    
    # A1. Check for ripped content patterns
    ripped_issues = detect_ripped_content(body)
    if ripped_issues:
        print(f"  ❌ RIPPED CONTENT: {filename}")
        for issue in ripped_issues:
            print(f"     - {issue}")
        
        # Auto-fix: clean up ripped HTML from body
        if do_fix and ripped_issues:
            content = remove_ripped_html_body(content)
            result["fixes_applied"].append("Removed ripped HTML artifacts from body")
            result["content_modified"] = True
            # Re-parse after fix
            metadata, body = parse_front_matter(content)
            
            # Re-check: are ripped issues resolved?
            remaining_ripped = detect_ripped_content(body)
            if remaining_ripped:
                # Still has ripped content that couldn't be auto-cleaned
                result["issues"].extend(remaining_ripped)
                result["status"] = "FAIL"
            else:
                # All ripped issues were fixed
                result["warnings"].append("Had ripped HTML artifacts (auto-fixed)")
                if result["status"] == "FAIL":
                    result["status"] = "WARNING"
                print(f"  🔧 Ripped content cleaned successfully")
        else:
            result["issues"].extend(ripped_issues)
            result["status"] = "FAIL"
    
    # A2. Check front matter quality
    fm_issues = check_front_matter_quality(metadata)
    if fm_issues:
        for issue in fm_issues:
            if "Missing" in issue:
                result["issues"].append(issue)
                if result["status"] != "FAIL":
                    result["status"] = "WARNING"
            else:
                result["warnings"].append(issue)
        
        print(f"  ⚠️  FRONT MATTER: {filename}")
        for issue in fm_issues:
            print(f"     - {issue}")
        
        # Auto-fix: fix front matter
        if do_fix:
            content = fix_front_matter(content, metadata)
            metadata, body = parse_front_matter(content)
            content = fix_missing_fields(metadata, content)
            metadata, body = parse_front_matter(content)
            result["fixes_applied"].append("Fixed front matter")
            result["content_modified"] = True
            # Remove the front matter issues since they're fixed
            result["issues"] = [i for i in result["issues"] if "Missing" not in i]
            if not result["issues"]:
                result["status"] = "PASS"
    
    # A3. Content quality — word count
    word_count = count_body_words(body)
    if word_count < 150:
        result["issues"].append(f"Content too short ({word_count} words, minimum 150)")
        result["status"] = "FAIL"
        print(f"  ❌ TOO SHORT: {filename} ({word_count} words)")
    
    # A4. Video-only posts
    if is_video_only(body):
        result["issues"].append("Video-only post with no real article body")
        result["status"] = "FAIL"
        print(f"  ❌ VIDEO-ONLY: {filename}")
    
    # A5. AI content authenticity check (only if API key available)
    if API_KEY and word_count >= 50:
        print(f"  🤖 AI content check: {filename}")
        ai_result = ai_verify_content(title, description, body)
        ai_verdict = ai_result.get("verdict", "SKIP")
        ai_reason = ai_result.get("reason", "")
        
        if ai_verdict in ("RIPPED", "MISINFORMATION"):
            result["issues"].append(f"AI verdict: {ai_verdict} — {ai_reason}")
            result["status"] = "FAIL"
            print(f"  ❌ AI: {ai_verdict} — {ai_reason}")
        elif ai_verdict == "LOW_QUALITY":
            result["warnings"].append(f"AI verdict: LOW_QUALITY — {ai_reason}")
            if result["status"] == "PASS":
                result["status"] = "WARNING"
            print(f"  ⚠️  AI: LOW_QUALITY — {ai_reason}")
        elif ai_verdict == "LEGITIMATE":
            print(f"  ✅ AI: LEGITIMATE")
        else:
            print(f"  ⏭️  AI: {ai_verdict}")
        
        # Rate limit
        time.sleep(1)
    
    # ═══════════════════════════════════════════════════════
    # B. Image-Article Relevance Check
    # ═══════════════════════════════════════════════════════
    
    if image_url:
        # B1. Check image source
        source_check = ai_check_image_source(image_url)
        source_type = source_check.get("source_type", "UNKNOWN")
        source_reason = source_check.get("reason", "")
        
        # Also do heuristic check
        heuristic_check = check_image_source_heuristic(image_url)
        
        # If either AI or heuristic says NEWS, flag it
        if source_type == "NEWS" or heuristic_check.get("source_type") == "NEWS":
            flag_reason = source_reason or heuristic_check.get("reason", "")
            result["warnings"].append(f"Image from news/external source: {flag_reason}")
            if result["status"] == "PASS":
                result["status"] = "WARNING"
            print(f"  ⚠️  IMAGE SOURCE: {flag_reason}")
            
            # Auto-fix: try to replace with stock photo
            if do_fix:
                cat_key = DEFAULT_CATEGORY
                if categories:
                    cat_clean = categories.strip("[]\"' ")
                    if cat_clean in VALID_CATEGORIES:
                        cat_key = cat_clean
                
                new_image = fetch_best_image(title, cat_key, article_title=title)
                if new_image:
                    content = replace_image_in_content(content, new_image["url"])
                    result["fixes_applied"].append(f"Replaced ripped image with {new_image['source']} photo by {new_image['credit']}")
                    result["content_modified"] = True
                    result["warnings"] = [w for w in result["warnings"] if "Image from news" not in w]
                    print(f"  🔧 Replaced image with {new_image['source']} photo")
                else:
                    result["warnings"].append("Could not find replacement stock photo")
                    print(f"  ⚠️  Could not find replacement image")
        
        # B2. Check image-article relevance
        if API_KEY:
            print(f"  🤖 AI relevance check: {filename}")
            relevance_score = ai_check_image_relevance(title, description, image_url)
            
            if relevance_score < 40:
                result["warnings"].append(f"Image relevance score: {relevance_score}/100 (below 40 threshold)")
                if result["status"] == "PASS":
                    result["status"] = "WARNING"
                print(f"  ⚠️  IMAGE RELEVANCE: {relevance_score}/100")
                
                # Auto-fix: search for better image
                if do_fix:
                    cat_key = DEFAULT_CATEGORY
                    if categories:
                        cat_clean = categories.strip("[]\"' ")
                        if cat_clean in VALID_CATEGORIES:
                            cat_key = cat_clean
                    
                    new_image = fetch_best_image(title, cat_key, article_title=title)
                    if new_image and new_image.get("score", 0) > relevance_score:
                        content = replace_image_in_content(content, new_image["url"])
                        result["fixes_applied"].append(f"Replaced low-relevance image (score {relevance_score}) with better match from {new_image['source']} (score {new_image.get('score', 0)})")
                        result["content_modified"] = True
                        result["warnings"] = [w for w in result["warnings"] if "Image relevance score" not in w]
                        print(f"  🔧 Replaced with {new_image['source']} image (score {new_image.get('score', 0)})")
                    else:
                        result["warnings"].append(f"No better image found (current score: {relevance_score})")
                        print(f"  ⚠️  No better replacement image found")
            else:
                print(f"  ✅ IMAGE RELEVANCE: {relevance_score}/100")
            
            time.sleep(1)
    else:
        # No image — this is a warning (articles should have images)
        result["warnings"].append("No image in front matter")
        if result["status"] == "PASS":
            result["status"] = "WARNING"
        print(f"  ⚠️  NO IMAGE: {filename}")
        
        # Auto-fix: try to add an image
        if do_fix:
            cat_key = DEFAULT_CATEGORY
            if categories:
                cat_clean = categories.strip("[]\"' ")
                if cat_clean in VALID_CATEGORIES:
                    cat_key = cat_clean
            
            new_image = fetch_best_image(title, cat_key, article_title=title)
            if new_image:
                content = replace_image_in_content(content, new_image["url"])
                result["fixes_applied"].append(f"Added image from {new_image['source']} by {new_image['credit']}")
                result["content_modified"] = True
                result["warnings"] = [w for w in result["warnings"] if "No image in front matter" not in w]
                print(f"  🔧 Added image from {new_image['source']}")
    
    # ═══════════════════════════════════════════════════════
    # Write back fixed content
    # ═══════════════════════════════════════════════════════
    if do_fix and result["content_modified"]:
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  💾 Saved fixes to: {filename}")
        except Exception as e:
            result["warnings"].append(f"Could not save fixes: {e}")
            print(f"  ⚠️  Could not save: {e}")
    
    return result


def reject_article(filepath, reason):
    """Move a failing article to output/rejected/ directory."""
    rejected_dir = "output/rejected"
    os.makedirs(rejected_dir, exist_ok=True)
    
    filename = os.path.basename(filepath)
    dest = os.path.join(rejected_dir, filename)
    
    # Avoid overwriting existing rejected files
    if os.path.exists(dest):
        base, ext = os.path.splitext(filename)
        timestamp = int(time.time())
        dest = os.path.join(rejected_dir, f"{base}-{timestamp}{ext}")
    
    try:
        shutil.move(filepath, dest)
        print(f"  🗑️  REJECTED: {filename} → {dest}")
        print(f"     Reason: {reason}")
        return True
    except Exception as e:
        print(f"  ⚠️  Could not move {filename}: {e}")
        return False


def print_qa_report(results):
    """Print a formatted QA report to stdout."""
    print("\n" + "=" * 70)
    print("  MENSHLYGLOBAL — ARTICLE QA REPORT")
    print("=" * 70)
    
    pass_count = 0
    fail_count = 0
    warn_count = 0
    
    for r in results:
        status = r["status"]
        icon = {"PASS": "✅", "FAIL": "❌", "WARNING": "⚠️ "}.get(status, "❓")
        
        if status == "PASS":
            pass_count += 1
        elif status == "FAIL":
            fail_count += 1
        else:
            warn_count += 1
        
        print(f"\n{icon} {r['filename']} — {status}")
        
        for issue in r.get("issues", []):
            print(f"   ❌ {issue}")
        for warning in r.get("warnings", []):
            print(f"   ⚠️  {warning}")
        for fix in r.get("fixes_applied", []):
            print(f"   🔧 {fix}")
    
    print("\n" + "-" * 70)
    total = len(results)
    print(f"  Total: {total}  |  ✅ Pass: {pass_count}  |  ⚠️  Warning: {warn_count}  |  ❌ Fail: {fail_count}")
    print("=" * 70)
    
    return fail_count


def write_qa_report_json(results, output_dir="output"):
    """Write QA report to output/qa-report.json."""
    os.makedirs(output_dir, exist_ok=True)
    
    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "total": len(results),
            "pass": sum(1 for r in results if r["status"] == "PASS"),
            "warning": sum(1 for r in results if r["status"] == "WARNING"),
            "fail": sum(1 for r in results if r["status"] == "FAIL"),
        },
        "articles": results
    }
    
    with open(os.path.join(output_dir, "qa-report.json"), "w") as f:
        json.dump(report, f, indent=2)
    
    print(f"  QA report written to {output_dir}/qa-report.json")


# ── Main ───────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="MenshlyGlobal Article QA Verification",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/article-qa.py --dir content/posts/
  python scripts/article-qa.py --dir content/posts/ --fix
  python scripts/article-qa.py --dir content/posts/ --reject
  python scripts/article-qa.py --file content/posts/some-article.md --fix
"""
    )
    parser.add_argument("--dir", help="Directory of markdown articles to verify")
    parser.add_argument("--file", help="Single markdown file to verify")
    parser.add_argument("--fix", action="store_true", help="Auto-fix issues where possible")
    parser.add_argument("--reject", action="store_true", help="Move failing articles to output/rejected/")
    args = parser.parse_args()
    
    if not args.dir and not args.file:
        parser.error("Either --dir or --file must be specified")
    
    # Collect files to verify
    files = []
    if args.file:
        if not os.path.isfile(args.file):
            print(f"ERROR: File not found: {args.file}")
            sys.exit(1)
        files.append(args.file)
    elif args.dir:
        if not os.path.isdir(args.dir):
            print(f"ERROR: Directory not found: {args.dir}")
            sys.exit(1)
        for fname in sorted(os.listdir(args.dir)):
            if fname.endswith(".md") and fname != "_index.md":
                files.append(os.path.join(args.dir, fname))
    
    if not files:
        print("No markdown files found to verify.")
        sys.exit(0)
    
    print(f"\nMenshlyGlobal Article QA Verification")
    print(f"Files to check: {len(files)}")
    print(f"Auto-fix: {'ON' if args.fix else 'OFF'}")
    print(f"Reject: {'ON' if args.reject else 'OFF'}")
    print()
    
    # Auto-detect model if AI key is available
    if API_KEY:
        auto_detect_model()
    
    # Verify each article
    results = []
    for filepath in files:
        filename = os.path.basename(filepath)
        print(f"\n{'─' * 60}")
        print(f"  Checking: {filename}")
        print(f"{'─' * 60}")
        
        result = verify_article(filepath, do_fix=args.fix)
        results.append(result)
    
    # Handle rejections
    if args.reject:
        rejected_dir = "output/rejected"
        os.makedirs(rejected_dir, exist_ok=True)
        
        for r in results:
            if r["status"] == "FAIL":
                reasons = "; ".join(r.get("issues", []))
                if reject_article(r["file"], reasons):
                    r["rejected"] = True
                else:
                    r["rejected"] = False
    
    # Print report
    fail_count = print_qa_report(results)
    
    # Write JSON report
    write_qa_report_json(results)
    
    # Exit code
    if fail_count > 0:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
