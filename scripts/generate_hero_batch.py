#!/usr/bin/env python3
"""Generate hero images for a specific batch of articles.

Usage: python3 generate_hero_batch.py <start_index> <count>
  python3 generate_hero_batch.py 0 5   # Articles 1-5
  python3 generate_hero_batch.py 5 5   # Articles 6-10
"""

import sys
import re
from pathlib import Path
from image_utils import generate_hero_image

ARTICLES = [
    ("opportunities", "ai-agent-marketplaces-2026", "How to Make Money Selling AI Agents on Marketplaces in 2026"),
    ("opportunities", "ai-automation-agency", "How to Start an AI Automation Agency in 2026"),
    ("opportunities", "ai-chatbot-ecommerce-agency", "How to Build an AI Chatbot Agency for E-Commerce Stores in 2026"),
    ("opportunities", "ai-copywriting-agency", "How to Start an AI Copywriting Agency in 2026"),
    ("opportunities", "ai-course-creation", "How to Create and Sell AI-Powered Online Courses in 2026"),
    ("opportunities", "ai-data-analysis-service", "How to Start an AI Data Analysis Service in 2026"),
    ("opportunities", "ai-faceless-video-factory", "How to Build a Faceless YouTube Channel With AI in 2026"),
    ("opportunities", "ai-image-generation-agency", "How to Start an AI Image Generation Agency in 2026"),
    ("opportunities", "ai-lead-generation-machine", "How to Build an AI Lead Generation System in 2026"),
    ("opportunities", "ai-newsletter-business", "How to Start an AI Newsletter Business in 2026"),
    ("opportunities", "ai-saas-micro-products", "How to Build AI SaaS Micro-Products in 2026"),
    ("opportunities", "ai-seo-agency", "How to Start an AI SEO Agency in 2026"),
    ("opportunities", "ai-social-media-agency", "How to Start an AI Social Media Agency in 2026"),
    ("opportunities", "content-repurposing-agency-deep-dive", "How to Start a Content Repurposing Agency With AI in 2026"),
    ("opportunities", "gpt5-solo-entrepreneur", "How to Build a One-Person Business With GPT-5 in 2026"),
    ("opportunities", "voice-ai-business-blueprint", "How to Start a Voice AI Business in 2026"),
    ("intelligence", "ai-content-business-guide", "Launch and Monetize an AI Content Business From Scratch"),
    ("intelligence", "build-ai-chatbot-agency", "Build and Scale an AI Chatbot Agency End-to-End"),
    ("intelligence", "build-ai-lead-generation-system", "Build and Automate an AI Lead Generation System with Make.com and OpenAI"),
    ("intelligence", "build-ai-seo-agency-workflows", "Build and Scale an AI SEO Agency with Automated Workflows"),
    ("intelligence", "build-ai-social-media-pipeline", "Build and Automate an AI Social Media Management Pipeline"),
    ("intelligence", "build-ai-voice-agent-system", "Build and Deploy an AI Voice Agent System with Vapi"),
    ("intelligence", "create-ai-saas-micro-products-replit", "Build and Monetize AI SaaS Micro-Products on Replit"),
    ("intelligence", "create-faceless-youtube-channel-ai", "Create and Scale a Faceless YouTube Channel with AI Tools"),
    ("intelligence", "deploy-ai-email-marketing-automations", "Design and Deploy AI-Powered Email Marketing Automations"),
    ("intelligence", "makecom-automation-workflows", "Design, Build, and Deploy Make.com Automation Workflows"),
    ("playbooks", "ai-automation-agency-playbook", "Build and Scale an AI Automation Agency from Zero to $30K/Month"),
    ("playbooks", "ai-side-hustle-blueprint", "Build and Monetize AI Side Hustle Income Streams"),
    ("playbooks", "automation-agency-starter-kit", "Build and Launch an Automation Agency with Zero Budget"),
    ("playbooks", "chatgpt-prompt-engineering-guide", "Master ChatGPT Prompt Engineering for Business Revenue"),
]


def add_hero_to_frontmatter(filepath: Path, hero_path: str) -> bool:
    content = filepath.read_text()
    if re.search(r"^heroImage:", content, re.MULTILINE):
        print(f"   heroImage already exists, skipping")
        return False
    content = re.sub(
        r'^(image: ".*?")$',
        rf'\1\nheroImage: "{hero_path}"',
        content,
        count=1,
        flags=re.MULTILINE,
    )
    filepath.write_text(content)
    print(f"   Added heroImage to frontmatter")
    return True


if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    batch = ARTICLES[start:start+count]

    print(f"Generating hero images for {len(batch)} articles (index {start}-{start+count-1})")

    for section, slug, title in batch:
        print(f"\n--- {section}/{slug} ---")
        hero_file = Path(f"static/images/heroes/{section}/{slug}.png")
        if hero_file.exists():
            print(f"  Hero image already exists, skipping generation")
            hero_hugo_path = f"/images/heroes/{section}/{slug}.png"
        else:
            try:
                hero_hugo_path = generate_hero_image(topic=title, slug=slug, section=section)
            except Exception as e:
                print(f"  FAILED: {e}")
                continue

        md_path = Path(f"content/{section}/{slug}.md")
        if md_path.exists():
            add_hero_to_frontmatter(md_path, hero_hugo_path)

    print("\nDone!")
