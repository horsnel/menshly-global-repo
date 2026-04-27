#!/usr/bin/env python3
"""Trending Topic Discovery Module for Menshly Global.

This module discovers trending AI automation topics and business ideas using:
1. AI-powered topic generation using the configured API
2. Deduplication against existing articles
3. Persistent topic queue stored in data/trending_queue.json

The topic queue ensures generators never run out of trending topics to write about.
Each topic is enriched with context, affiliate suggestions, and related keywords.

Usage:
    from trending_topics import TrendingTopicDiscovery

    discovery = TrendingTopicDiscovery()
    topic = discovery.get_next_topic("opportunity")
    # Returns: {"topic": "How to build AI voice agents...", "context": "...", "affiliates": [...]}
"""

import json
import os
import re
import time
import random
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

# Auto-load .env from project root
load_dotenv(Path(__file__).resolve().parent.parent / ".env")

from ai_utils import api_call

AI_API_KEY = os.environ.get("AI_API_KEY", "")
AI_API_BASE = os.environ.get("AI_API_BASE", "https://api.groq.com/openai/v1")
AI_MODEL = os.environ.get("AI_MODEL", "llama-3.3-70b-versatile")

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
QUEUE_FILE = PROJECT_ROOT / "data" / "trending_queue.json"
CONTENT_DIRS = {
    "opportunities": PROJECT_ROOT / "content" / "opportunities",
    "intelligence": PROJECT_ROOT / "content" / "intelligence",
    "playbooks": PROJECT_ROOT / "content" / "playbooks",
}


def _get_existing_slugs(section: str) -> set:
    """Get all existing article slugs in a section to avoid duplicates."""
    content_dir = CONTENT_DIRS.get(section)
    if not content_dir or not content_dir.exists():
        return set()
    slugs = set()
    for f in content_dir.glob("*.md"):
        if f.name != "_index.md":
            slugs.add(f.stem)
    return slugs


def _get_existing_titles(section: str) -> set:
    """Get all existing article titles in a section for dedup."""
    content_dir = CONTENT_DIRS.get(section)
    if not content_dir or not content_dir.exists():
        return set()
    titles = set()
    for f in content_dir.glob("*.md"):
        if f.name == "_index.md":
            continue
        try:
            text = f.read_text()
            for line in text.split("\n"):
                if line.startswith("title:"):
                    title = line.split("title:", 1)[1].strip().strip('"').strip("'")
                    titles.add(title.lower())
                    break
        except Exception:
            pass
    return titles


def _load_queue() -> dict:
    """Load the trending topic queue from disk."""
    if QUEUE_FILE.exists():
        try:
            return json.loads(QUEUE_FILE.read_text())
        except (json.JSONDecodeError, Exception):
            pass
    return {
        "last_updated": None,
        "topics": [],
        "used_topics": [],
    }


def _save_queue(queue: dict):
    """Save the trending topic queue to disk."""
    QUEUE_FILE.parent.mkdir(parents=True, exist_ok=True)
    queue["last_updated"] = datetime.now(timezone.utc).isoformat()
    QUEUE_FILE.write_text(json.dumps(queue, indent=2))


def discover_trending_topics(count: int = 15) -> list[dict]:
    """Discover trending AI automation topics using AI-powered research."""
    existing_opp = _get_existing_titles("opportunities")
    existing_int = _get_existing_titles("intelligence")
    existing_pb = _get_existing_titles("playbooks")
    all_existing = existing_opp | existing_int | existing_pb

    existing_list = "\n".join(f"- {t}" for t in sorted(all_existing)[:40])

    system_prompt = """You are a trend research analyst for Menshly Global (tagline: "Where AI Meets Revenue").
Your job is to identify trending AI automation business opportunities that entrepreneurs can start RIGHT NOW.

Return topics as a JSON object with a "topics" key containing an array. Each topic must have:
- "topic": A short description like "How to start an AI [X] agency/business in 2026"
- "context": 1-2 sentences on why this is trending NOW
- "keywords": 3-5 SEO keywords
- "affiliates": List of relevant affiliate tool names (from: Make.com, Replit, Vapi, Fliki AI, Canva, ChatGPT, ElevenLabs, Notion, Klaviyo, Semrush, Hostinger, Shopify, Zapier, Apollo.io, PhantomBuster, Buffer, Loom, Calendly, Beehiiv, Grammarly, ActiveCampaign, Midjourney)
- "opportunity_angle": How to frame the opportunity article title (pattern: "How to [VERB] [TOPIC] in 2026 ([BENEFIT])")
- "intelligence_angle": How to frame the intelligence guide title (pattern: "[VERB], [VERB], and [VERB] [THING] with [TOOL]")
- "playbook_angle": How to frame the playbook title (pattern: "[VERB], [VERB], and [VERB] [THING] with [TOOL]")

IMPORTANT: Topics must be FRESH and specific emerging niches like:
- AI agent marketplaces and custom GPT stores
- AI-powered proposal and grant writing
- AI real estate automation
- AI voice agent businesses with Vapi/Bland.ai
- AI podcast production agencies
- AI HR/recruitment automation
- AI bookkeeping automation
- AI customer onboarding systems
- AI content repurposing with multi-platform distribution
- AI SaaS micro-products on Replit
- Faceless YouTube channels with AI
- AI newsletter businesses with Beehiiv
- AI email marketing with Klaviyo/ActiveCampaign
- AI data analysis services
- AI course creation businesses
- AI social media management pipelines
- AI lead generation with Apollo/PhantomBuster
- AI copywriting agencies
- AI image generation agencies
- AI SEO agencies with Semrush
- One-person businesses powered by GPT-5/Claude
- AI freelance arbitrage businesses
- AI video editing services
- AI chatbot agencies for e-commerce (Shopify)
- AI cold email outreach systems
- AI customer support automation
- AI appointment booking systems
- AI contract/proposal writing with LLMs
- AI translation and localization services
- AI supply chain optimization consulting
- AI legal document automation

Return ONLY valid JSON, no other text."""

    user_prompt = f"""Generate {count} trending AI automation business opportunity topics.

These are the EXISTING article titles already published (DO NOT duplicate these):
{existing_list}

Focus on topics that are:
1. Currently trending or about to trend
2. Have clear monetization paths ($1K-50K/month potential)
3. Can be started by solo entrepreneurs with minimal capital
4. Have real tools available NOW
5. Are different enough from existing articles to add value

Return the JSON now."""

    payload = {
        "model": AI_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "max_tokens": 8000,
        "temperature": 0.85,
    }

    data = api_call(payload)
    content = data["choices"][0]["message"]["content"]

    try:
        result = json.loads(content)
        if isinstance(result, dict) and "topics" in result:
            return result["topics"]
        elif isinstance(result, list):
            return result
    except json.JSONDecodeError:
        match = re.search(r'\{.*\}', content, re.DOTALL)
        if match:
            try:
                result = json.loads(match.group())
                if isinstance(result, dict) and "topics" in result:
                    return result["topics"]
            except json.JSONDecodeError:
                pass
        match = re.search(r'\[.*\]', content, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass

    print("  WARNING: Could not parse AI response as JSON, using fallback topics")
    return _fallback_topics()


def _fallback_topics() -> list[dict]:
    """Fallback static topics if AI discovery fails."""
    return [
        {"topic": "How to start an AI cold email outreach agency in 2026", "context": "AI-powered personalization at scale is replacing generic cold emails", "keywords": ["cold email", "AI outreach", "automation"], "affiliates": ["Apollo.io", "Make.com", "Zapier"], "opportunity_angle": "How to Start an AI Cold Email Outreach Agency in 2026 ($5K-30K/Month)", "intelligence_angle": "Build, Automate, and Scale AI Cold Email Outreach Systems with Apollo.io", "playbook_angle": "Build, Scale, and Monetize an AI Cold Email Outreach Agency with Apollo.io and Make.com"},
        {"topic": "How to build AI customer support automation in 2026", "context": "Businesses are replacing first-line support with AI chatbots and routing", "keywords": ["AI support", "chatbot automation", "customer service"], "affiliates": ["ChatGPT", "Make.com", "Zapier", "Shopify"], "opportunity_angle": "How to Build an AI Customer Support Automation Business in 2026 ($3K-20K/Month)", "intelligence_angle": "Design, Build, and Deploy AI Customer Support Automation with ChatGPT", "playbook_angle": "Design, Build, and Scale AI Customer Support Automation Systems with ChatGPT and Make.com"},
        {"topic": "How to start an AI appointment booking system in 2026", "context": "Voice AI and chatbot booking are replacing manual scheduling", "keywords": ["AI booking", "appointment automation", "voice AI"], "affiliates": ["Vapi", "Calendly", "Make.com"], "opportunity_angle": "How to Start an AI Appointment Booking Automation Business in 2026 ($2K-15K/Month)", "intelligence_angle": "Build and Deploy AI Appointment Booking Systems with Vapi and Calendly", "playbook_angle": "Build, Deploy, and Scale AI Appointment Booking Systems with Vapi and Calendly"},
        {"topic": "How to build an AI contract and proposal writing service in 2026", "context": "LLMs can now draft professional contracts and proposals in minutes", "keywords": ["AI contracts", "proposal automation", "legal AI"], "affiliates": ["ChatGPT", "Notion", "Make.com"], "opportunity_angle": "How to Build an AI Contract and Proposal Writing Service in 2026 ($5K-25K/Month)", "intelligence_angle": "Design, Build, and Deploy AI Contract and Proposal Writing Systems with ChatGPT", "playbook_angle": "Build, Automate, and Scale an AI Contract and Proposal Writing Service with ChatGPT and Make.com"},
        {"topic": "How to start an AI personal finance automation service in 2026", "context": "People want automated budgeting, expense tracking, and investment insights", "keywords": ["AI finance", "personal finance automation", "budget AI"], "affiliates": ["ChatGPT", "Make.com", "Notion"], "opportunity_angle": "How to Start an AI Personal Finance Automation Service in 2026 ($2K-10K/Month)", "intelligence_angle": "Build and Deploy AI Personal Finance Automation Systems with ChatGPT", "playbook_angle": "Build, Deploy, and Monetize AI Personal Finance Automation Systems with ChatGPT and Make.com"},
        {"topic": "How to build an AI translation and localization service in 2026", "context": "Global businesses need fast, AI-powered multilingual content", "keywords": ["AI translation", "localization", "multilingual AI"], "affiliates": ["ChatGPT", "Make.com", "ElevenLabs"], "opportunity_angle": "How to Build an AI Translation and Localization Service in 2026 ($3K-20K/Month)", "intelligence_angle": "Build, Automate, and Deploy AI Translation and Localization Services with ChatGPT", "playbook_angle": "Build, Scale, and Monetize an AI Translation and Localization Service with ChatGPT and Make.com"},
        {"topic": "How to start an AI legal document automation agency in 2026", "context": "Law firms and businesses are automating contract review and legal drafting", "keywords": ["AI legal", "document automation", "legal tech"], "affiliates": ["ChatGPT", "Make.com", "Notion"], "opportunity_angle": "How to Start an AI Legal Document Automation Agency in 2026 ($5K-30K/Month)", "intelligence_angle": "Design, Build, and Deploy AI Legal Document Automation with ChatGPT", "playbook_angle": "Design, Build, and Scale an AI Legal Document Automation Agency with ChatGPT and Make.com"},
        {"topic": "How to build an AI supply chain optimization consulting business in 2026", "context": "AI is revolutionizing logistics, demand forecasting, and inventory management", "keywords": ["AI supply chain", "logistics AI", "demand forecasting"], "affiliates": ["ChatGPT", "Make.com", "Notion"], "opportunity_angle": "How to Build an AI Supply Chain Optimization Consulting Business in 2026 ($5K-40K/Month)", "intelligence_angle": "Build and Deploy AI Supply Chain Optimization Systems with ChatGPT", "playbook_angle": "Build, Scale, and Monetize AI Supply Chain Optimization Consulting with ChatGPT and Make.com"},
    ]


class TrendingTopicDiscovery:
    """Main class for discovering and managing trending topics."""

    def __init__(self):
        self.queue = _load_queue()

    def refresh_topics(self, count: int = 15):
        """Discover new trending topics and add them to the queue."""
        print("Refreshing trending topic queue...")

        try:
            new_topics = discover_trending_topics(count)
        except Exception as e:
            print(f"  Topic discovery API failed: {e}")
            print(f"  Using fallback static topics instead")
            new_topics = _fallback_topics()

        if not new_topics:
            print("  No topics returned from API, using fallback")
            new_topics = _fallback_topics()

        used_titles = set(t.get("topic", "").lower() for t in self.queue.get("used_topics", []))

        added = 0
        for topic in new_topics:
            topic_text = topic.get("topic", "").lower()
            if topic_text in used_titles:
                continue

            queue_topics = [t.get("topic", "").lower() for t in self.queue["topics"]]
            if topic_text not in queue_topics:
                topic["discovered_at"] = datetime.now(timezone.utc).isoformat()
                self.queue["topics"].append(topic)
                added += 1

        print(f"  Added {added} new topics to queue (total: {len(self.queue['topics'])})")
        _save_queue(self.queue)
        return added

    def get_next_topic(self, section: str = "opportunity") -> dict | None:
        """Get the next topic from the queue for a given section."""
        if not self.queue["topics"]:
            self.refresh_topics()

        if not self.queue["topics"]:
            print("  WARNING: No trending topics available, using fallback")
            fallback = _fallback_topics()
            self.queue["topics"] = fallback
            _save_queue(self.queue)

        topic = self.queue["topics"].pop(0)

        if section == "opportunity":
            topic["selected_title"] = topic.get("opportunity_angle", topic.get("topic", ""))
        elif section == "intelligence":
            topic["selected_title"] = topic.get("intelligence_angle", topic.get("topic", ""))
        elif section == "playbook":
            topic["selected_title"] = topic.get("playbook_angle", topic.get("topic", ""))
        else:
            topic["selected_title"] = topic.get("topic", "")

        _save_queue(self.queue)
        return topic

    def mark_topic_used(self, topic: dict):
        """Mark a topic as used so it won't be selected again."""
        self.queue.setdefault("used_topics", []).append({
            "topic": topic.get("topic", ""),
            "used_at": datetime.now(timezone.utc).isoformat(),
        })
        _save_queue(self.queue)

    def get_queue_size(self) -> int:
        """Return the number of topics remaining in the queue."""
        return len(self.queue.get("topics", []))

    def ensure_minimum_queue(self, minimum: int = 10):
        """Ensure the queue has at least `minimum` topics."""
        if len(self.queue.get("topics", [])) < minimum:
            needed = minimum - len(self.queue.get("topics", []))
            print(f"  Queue has {len(self.queue.get('topics', []))} topics, need {needed} more")
            self.refresh_topics(count=max(needed, 15))


if __name__ == "__main__":
    """CLI: Discover trending topics and populate the queue."""
    discovery = TrendingTopicDiscovery()

    print(f"Current queue size: {discovery.get_queue_size()}")
    print("Discovering trending AI automation topics...")

    added = discovery.refresh_topics(20)
    print(f"Added {added} new topics")
    print(f"Queue size: {discovery.get_queue_size()}")

    for i, topic in enumerate(discovery.queue["topics"][:5], 1):
        print(f"\n  {i}. {topic.get('opportunity_angle', topic.get('topic', ''))}")
        print(f"     Context: {topic.get('context', 'N/A')}")
        print(f"     Affiliates: {', '.join(topic.get('affiliates', []))}")
