#!/usr/bin/env python3
"""
Menshly Hero Image Generator — High-quality topic-specific images
Generates unique 8K-style hero images and PDF covers for all articles.
Uses z-ai-generate CLI with carefully crafted prompts per topic.
"""

import os
import re
import subprocess
import sys
import time
import json
from pathlib import Path

REPO = Path("/home/z/my-project/menshly-global-repo")
CONTENT = REPO / "content"
HERO_DIR = REPO / "static/images/heroes"
THUMB_DIR = REPO / "static/images/articles"
PDF_DIR = REPO / "static/images/pdfs"

# Ensure output dirs exist
for d in [HERO_DIR / "opportunities", HERO_DIR / "intelligence", HERO_DIR / "playbooks",
          THUMB_DIR / "opportunities", THUMB_DIR / "intelligence", THUMB_DIR / "playbooks",
          PDF_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# ── Image prompt mapping: unique per article ──
# Each prompt is crafted to be visually distinct, topic-relevant, 
# with realistic colors (no generic blue/gold), cinematic 8K style

OPPORTUNITIES_PROMPTS = {
    "ai-ecommerce-optimization-agency": "Cinematic 8K overhead shot of a modern e-commerce dashboard on a large monitor, showing product analytics charts, conversion funnels, and AI-powered recommendation widgets, vibrant data visualization in orange and teal, sleek glass desk with smartphone showing Shopify app, photorealistic, dramatic lighting",
    
    "how-to-build-an-ai-legal-document-automation-agency-5k-30kmonth": "Cinematic 8K close-up of a courtroom-style wooden desk with legal documents being scanned by a robotic arm, AI holographic interface showing contract analysis, warm amber desk lamp lighting, leather briefcase, scales of justice, photorealistic dramatic lighting",
    
    "how-to-build-an-ai-translation-and-localization-service-3k-20kmonth": "Cinematic 8K dramatic shot of multiple floating holographic screens showing different languages being translated in real-time, world map with glowing connection lines, earbuds and microphone on a white marble desk, vibrant green and coral accents, photorealistic",
    
    "how-to-build-an-ai-translation-and-localization-service-in-2026-3k-20kmonth": "Cinematic 8K shot of a sleek translation booth with neural network visualization on curved monitors, headphones on stand, flags of nations as small holograms, cool silver and warm orange palette, photorealistic studio lighting",
    
    "ai-api-wrapper-business": "Cinematic 8K macro shot of server racks with glowing fiber optic cables, API endpoint visualization floating as holographic code, circuit board patterns in emerald green and deep purple, data streaming effects, photorealistic tech aesthetic",
    
    "ai-grant-writing-service": "Cinematic 8K overhead of an elegant wooden desk with grant proposal documents, fountain pen, university crest seal, AI assistant chat window on tablet showing proposal drafting, warm burgundy and cream tones, photorealistic academic setting",
    
    "how-to-build-an-ai-contract-and-proposal-writing-service-in-2026-5k25kmonth": "Cinematic 8K shot of a professional office desk with proposal documents stacked neatly, AI chat interface on a large monitor drafting contracts, silver pen, leather portfolio, charcoal and copper color scheme, photorealistic",
    
    "ai-bookkeeping-automation": "Cinematic 8K dramatic shot of a modern accounting workspace, dual monitors showing QuickBooks dashboard with AI insights, calculator, spreadsheets with green highlights, coffee cup, warm wood and steel aesthetic, photorealistic",
    
    "ai-video-production-agency": "Cinematic 8K shot of a professional video editing suite, large monitors showing timeline with AI-generated video clips, camera on tripod, studio lighting rig, boom microphone, rich red and dark teal palette, photorealistic",
    
    "ai-data-annotation-and-training-service": "Cinematic 8K macro of data labeling interface on ultra-wide monitor, bounding boxes around objects in images, AI training pipeline visualization, neural network nodes in warm amber, dark workspace, photorealistic",
    
    "ai-hr-recruitment-automation-agency": "Cinematic 8K shot of a modern HR office, multiple screens showing candidate profiles with AI matching scores, video interview window, Greenhouse logo on display, warm coral and navy palette, photorealistic",
    
    "how-to-launch-an-ai-personal-finance-automation-service-in-2026-2k-10kmonth": "Cinematic 8K dramatic shot of personal finance dashboard on a tablet and laptop, budget charts, investment portfolio with AI recommendations, bank card, coins, deep green and gold accents, photorealistic home office",
    
    "ai-customer-support-automation-agency": "Cinematic 8K shot of a modern call center with AI chatbot interface on curved monitors, customer satisfaction metrics, Zendesk-style dashboard, headset on desk, teal and warm white palette, photorealistic",
    
    "ai-real-estate-marketing-agency": "Cinematic 8K aerial view of luxury real estate with AI-generated property listing on a tablet, virtual tour interface, Zillow-style map, warm sunset golden hour, architectural photography style, photorealistic",
    
    "how-to-launch-an-ai-appointment-booking-automation-business-in-2026-2k15kmonth": "Cinematic 8K shot of a reception desk with AI booking system on a sleek monitor, calendar grid with appointments, Calendly-style interface, modern office lobby, warm wood and white palette, photorealistic",
    
    "ai-course-creation-business-2026": "Cinematic 8K shot of an online course creation studio, monitor showing course builder with AI-generated lesson plans, microphone for voiceover, ring light, notebook with curriculum outline, warm terracotta and cream, photorealistic",
    
    "ai-content-repurposing-agency-2026": "Cinematic 8K dramatic shot of content repurposing workflow, large monitor showing one blog post being split into social media posts, tweets, and video scripts by AI, vibrant magenta and dark slate palette, photorealistic",
    
    "ai-resume-career-service-2026": "Cinematic 8K overhead of a desk with resume documents, AI resume builder on laptop screen showing optimized CV, professional headshot being analyzed, LinkedIn interface, navy and warm gold, photorealistic",
    
    "ai-freelance-marketplace-2026": "Cinematic 8K shot of a freelancer workspace, Replit code editor on screen with AI freelancer matching interface, multiple project cards floating as holograms, purple and warm amber palette, photorealistic",
    
    "ai-saas-micro-products-replit-2026": "Cinematic 8K dramatic shot of Replit IDE on large monitor building a SaaS micro-product, code editor with AI pair programming, deployment pipeline visualization, electric blue and orange accents, photorealistic",
    
    "ai-voice-agent-agency-2026": "Cinematic 8K shot of a voice AI studio, Vapi dashboard on monitor showing voice agent configuration, studio microphone, sound wave visualization, waveform in coral red, dark acoustic panels, photorealistic",
    
    "ai-social-media-agency-2026": "Cinematic 8K overhead of a social media command center, multiple screens showing AI-generated posts scheduling, analytics dashboards, Buffer interface, vibrant gradient from coral to deep purple, photorealistic",
    
    "ai-data-analysis-service-2026": "Cinematic 8K macro of data visualization on ultra-wide monitor, interactive charts and graphs with AI insights panel, Python code editor, Jupyter notebook, warm teal and amber color scheme, photorealistic",
    
    "ai-appointment-booking-agency-2026": "Cinematic 8K shot of a modern salon reception with AI booking tablet mounted on counter, appointment calendar with smart scheduling, warm wooden interior, soft ambient lighting, cream and forest green, photorealistic",
    
    "ai-seo-agency-2026": "Cinematic 8K dramatic shot of SEO dashboard on dual monitors, keyword ranking charts, backlink analysis, Semrush-style interface, search engine results visualization, deep emerald and warm copper, photorealistic",
    
    "ai-affiliate-marketing-business": "Cinematic 8K overhead of affiliate marketing dashboard, commission tracking charts, product comparison widgets, Semrush analytics, revenue graphs trending upward, rich burgundy and teal, photorealistic",
    
    "ai-resume-career-service": "Cinematic 8K shot of a career coaching office, AI resume optimizer on screen, professional headshot gallery, interview preparation interface, warm mahogany and cream, photorealistic",
    
    "ai-lead-generation-agency-2026": "Cinematic 8K shot of lead generation pipeline visualization on curved monitor, CRM dashboard with AI scoring, sales funnel with conversion rates, orange and charcoal palette, photorealistic",
    
    "ai-chatbot-ecommerce-agency-2026": "Cinematic 8K shot of an e-commerce store chatbot interface on tablet, AI product recommendations, shopping cart widget, customer conversation with purchase completion, warm coral and navy, photorealistic",
    
    "ai-podcast-production-agency": "Cinematic 8K dramatic shot of a podcast studio, professional microphone with pop filter, sound mixer, AI transcription on monitor, waveform visualization, rich burgundy and dark wood, photorealistic",
    
    "ai-cold-email-agency": "Cinematic 8K shot of email outreach dashboard, AI-personalized email sequences on monitor, open rate analytics, reply tracking, warm slate grey and electric green accents, photorealistic",
    
    "how-to-build-ai-powered-email-marketing-automation-in-2026-5000month-revenue-pot": "Cinematic 8K dramatic shot of Klaviyo-style email marketing dashboard, automated campaign flows, subscriber segmentation with AI, open rate charts, warm terracotta and deep navy, photorealistic",
    
    "fliki-ai-faceless-youtube-channel": "Cinematic 8K shot of a faceless YouTube channel creation setup, Fliki AI interface on monitor generating video from script, thumbnail designs, YouTube Studio analytics, vibrant red and dark charcoal, photorealistic",
    
    "ai-newsletter-business": "Cinematic 8K shot of newsletter creation workspace, Beehiiv editor on screen, subscriber growth charts, AI content suggestions, email template preview, warm cream and forest green, photorealistic",
    
    "ai-automation-agency": "Cinematic 8K dramatic shot of Make.com automation workspace, workflow builder with connected apps, automation triggers and actions, Zapier-style flowchart, electric teal and warm copper, photorealistic",
    
    "ai-lead-generation-machine": "Cinematic 8K macro of AI lead scoring interface, prospect database with engagement heatmaps, outreach sequence timeline, CRM integration, deep purple and warm amber, photorealistic",
    
    "content-repurposing-agency-deep-dive": "Cinematic 8K shot of content transformation studio, one piece of content being split into 10 formats on large monitor, blog to video to podcast to social conversion, coral and slate blue, photorealistic",
    
    "ai-copywriting-agency": "Cinematic 8K shot of a creative writing desk, AI copywriting assistant on large monitor, multiple ad copy variations, A/B test results, ChatGPT interface, warm cream and rich burgundy, photorealistic",
    
    "ai-agent-marketplaces-2026": "Cinematic 8K shot of an AI agent marketplace interface, browsing custom GPT agents, agent comparison cards, user ratings, ChatGPT store style, vibrant teal and warm orange, photorealistic",
    
    "gpt5-solo-entrepreneur": "Cinematic 8K dramatic shot of a solo entrepreneur at a minimalist desk, GPT-5 interface on laptop running multiple business tasks simultaneously, calendar, invoices, content, warm amber and dark charcoal, photorealistic",
    
    "voice-ai-business-blueprint": "Cinematic 8K shot of voice AI development workspace, Vapi configuration dashboard, voice waveform editor, telephony integration diagram, deep navy and electric coral, photorealistic",
}

INTELLIGENCE_PROMPTS = {
    "build-ai-ecommerce-optimization-agency": "Cinematic 8K technical shot of Shopify admin with Make.com automation workflows, product optimization AI modules, conversion rate dashboard, Shopify logo prominent, warm amber and cool teal, photorealistic",
    
    "build-an-ai-translation-and-localization-service-with-chatgpt-the-complete-step-": "Cinematic 8K shot of ChatGPT translation workflow, parallel text windows showing source and target languages, localization QA dashboard, world globe with language markers, warm silver and coral, photorealistic",
    
    "build-automate-and-deploy-ai-translation-and-localization-services-with-chatgpt": "Cinematic 8K shot of automated translation pipeline, ChatGPT API integration diagram, localization file management, CAT tool interface, cool mint and warm copper, photorealistic",
    
    "build-integrate-and-deploy-ai-personal-finance-automation-systems-with-chatgpt": "Cinematic 8K dramatic shot of personal finance automation, ChatGPT analyzing bank statements, budget allocation pie charts, Plaid API integration, deep forest green and warm gold, photorealistic",
    
    "fetch-the-transaction-from-plaid-sandbox": "Cinematic 8K macro shot of Plaid API console, bank transaction data in JSON format, sandbox testing environment, Plaid logo on interface, electric green and dark slate, photorealistic developer setup",
    
    "build-ai-bookkeeping-automation-system": "Cinematic 8K shot of QuickBooks with Make.com automation, invoice processing workflow, receipt OCR scanning, bank reconciliation dashboard, warm teal and copper, photorealistic",
    
    "build-ai-grant-writing-service": "Cinematic 8K shot of AI grant writing workflow in Make.com, research database integration, proposal template builder, submission tracking, warm burgundy and cream, photorealistic",
    
    "build-and-scale-an-ai-data-annotation-pipeline-with-label-studio": "Cinematic 8K shot of Label Studio annotation interface, image labeling with bounding boxes, dataset quality metrics, Make.com export pipeline, warm amber and dark charcoal, photorealistic",
    
    "build-ai-hr-recruitment-automation-system": "Cinematic 8K shot of Greenhouse ATS with Make.com workflows, candidate pipeline, AI screening scores, interview scheduling, warm navy and coral, photorealistic",
    
    "build-ai-video-production-agency": "Cinematic 8K shot of HeyGen video generation interface, AI avatar customization, script-to-video pipeline, Make.com workflow triggers, rich red and dark teal, photorealistic",
    
    "build-ai-api-wrapper-business": "Cinematic 8K shot of Vercel deployment dashboard, OpenAI API integration code, API wrapper architecture diagram, endpoint testing, electric purple and warm orange, photorealistic",
    
    "research-automate-and-monetize-an-ai-affiliate-marketing-system-with-semrush-and": "Cinematic 8K shot of Semrush keyword research with Make.com automation, affiliate link tracking, content scheduling pipeline, revenue dashboard, warm teal and burgundy, photorealistic",
    
    "build-configure-and-deploy-an-ai-appointment-booking-system-with-vapi-and-calend": "Cinematic 8K shot of Vapi voice agent connected to Calendly, voice call flow diagram, appointment confirmation interface, booking calendar, warm coral and navy, photorealistic",
    
    "build-optimize-scale-ai-seo-workflows-semrush": "Cinematic 8K dramatic shot of Semrush SEO toolkit, keyword gap analysis, backlink audit, content optimization suggestions, ranking trajectory charts, deep emerald and warm copper, photorealistic",
    
    "build-ai-resume-career-service": "Cinematic 8K shot of ChatGPT resume builder interface, ATS optimization checker, skill matching algorithm, interview prep chatbot, warm mahogany and cream, photorealistic",
    
    "launch-ai-freelance-marketplace": "Cinematic 8K shot of Replit-based freelancer platform, project bidding interface, AI skill matching, milestone payment system, vibrant teal and warm amber, photorealistic",
    
    "design-build-launch-ai-saas-micro-products-replit": "Cinematic 8K shot of Replit IDE building a SaaS product, AI code completion, one-click deployment, Stripe payment integration, electric blue and warm orange, photorealistic",
    
    "build-ai-appointment-booking-agency": "Cinematic 8K shot of Vapi voice agent for booking, phone system integration, calendar management, automated SMS confirmations, warm coral and charcoal, photorealistic",
    
    "launch-ai-data-analysis-agency": "Cinematic 8K shot of ChatGPT data analysis workspace, Python code generating insights, interactive Plotly charts, data pipeline architecture, warm teal and deep amber, photorealistic",
    
    "design-build-automate-ai-content-repurposing-pipeline-makecom": "Cinematic 8K shot of Make.com content repurposing scenario, blog input to multiple outputs, social media scheduling, format transformation flow, warm magenta and slate, photorealistic",
    
    "build-deploy-scale-ai-voice-agents-vapi": "Cinematic 8K shot of Vapi voice agent dashboard, call flow builder, voice cloning interface, telephony integration, deep navy and electric coral, photorealistic",
    
    "build-automate-scale-ai-social-media-pipelines-buffer-makecom": "Cinematic 8K shot of Buffer scheduling with Make.com triggers, content calendar, AI post generation, engagement analytics, warm coral and dark teal, photorealistic",
    
    "build-ai-course-creation-business": "Cinematic 8K shot of ChatGPT course outline generator, lesson plan builder, quiz creation interface, student progress dashboard, warm terracotta and cream, photorealistic",
    
    "launch-ai-agent-marketplace-business": "Cinematic 8K shot of ChatGPT custom GPT marketplace, agent configuration panel, usage analytics, monetization dashboard, vibrant teal and warm copper, photorealistic",
    
    "build-ai-cold-email-agency": "Cinematic 8K shot of Make.com cold email automation, personalization variables, A/B testing dashboard, reply tracking pipeline, warm slate and electric green, photorealistic",
    
    "build-ai-course-creation-system": "Cinematic 8K shot of AI course authoring tool, curriculum tree structure, video lesson editor, quiz generator, student analytics, warm cream and forest green, photorealistic",
    
    "launch-ai-data-analysis-service": "Cinematic 8K shot of ChatGPT analytics service, data visualization gallery, automated report generation, statistical analysis interface, deep amber and cool slate, photorealistic",
    
    "build-gpt5-solo-entrepreneur-system": "Cinematic 8K shot of GPT-5 business system, multi-task AI assistant managing calendar, emails, invoices, content creation simultaneously, warm amber and dark charcoal, photorealistic",
    
    "build-content-repurposing-agency": "Cinematic 8K shot of AI content repurposing studio, one article being transformed into 8 formats, social media posts, video scripts, infographics, warm coral and navy, photorealistic",
    
    "build-ai-image-generation-agency": "Cinematic 8K shot of Midjourney prompt crafting workspace, image gallery with variations, style consistency tools, client brief comparison, vibrant purple and warm gold, photorealistic",
    
    "build-ai-newsletter-business": "Cinematic 8K shot of Beehiiv newsletter platform, AI content curation, subscriber analytics, monetization with ads, email template designer, warm cream and forest green, photorealistic",
    
    "fliki-ai-faceless-youtube-channel-guide": "Cinematic 8K shot of Fliki AI video creation, text-to-video workflow, AI voiceover selection, thumbnail generator, YouTube upload queue, vibrant red and charcoal, photorealistic",
    
    "deploy-ai-email-marketing-automations": "Cinematic 8K shot of Klaviyo email automation builder, customer journey mapping, AI product recommendations, abandoned cart flows, warm terracotta and navy, photorealistic",
    
    "create-faceless-youtube-channel-ai": "Cinematic 8K shot of faceless YouTube content factory, Fliki AI batch video generation, script templates, upload scheduler, analytics dashboard, warm red and dark slate, photorealistic",
    
    "build-ai-chatbot-agency": "Cinematic 8K shot of ChatGPT chatbot builder, conversation flow designer, widget customization, analytics dashboard with satisfaction scores, warm teal and copper, photorealistic",
    
    "build-ai-voice-agent-system": "Cinematic 8K shot of Vapi voice agent builder, intent mapping, response generation, phone number provisioning, call analytics, deep navy and coral, photorealistic",
    
    "makecom-automation-workflows": "Cinematic 8K dramatic shot of Make.com scenario builder, multiple connected modules, data transformation pipeline, error handling routes, electric teal and warm amber, photorealistic",
    
    "build-ai-lead-generation-system": "Cinematic 8K shot of Make.com lead generation workflow, OpenAI enrichment, CRM integration, email sequence triggers, scoring dashboard, warm purple and copper, photorealistic",
    
    "ai-content-business-guide": "Cinematic 8K shot of ChatGPT content creation studio, blog post editor, SEO optimization, content calendar with AI suggestions, warm mahogany and cream, photorealistic",
}

PLAYBOOKS_PROMPTS = {
    "ai-ecommerce-optimization-playbook": "Cinematic 8K dramatic overhead of a comprehensive e-commerce playbook binder open on a glass desk, Shopify dashboard on monitor behind, product optimization checklists, revenue charts, warm amber and teal, photorealistic",
    
    "the-ai-legal-document-automation-playbook-25-steps-to-20kmonth": "Cinematic 8K shot of a premium legal automation playbook on a mahogany desk, contract workflow diagrams, 25-step milestone tracker, courtroom background with warm lighting, burgundy and gold, photorealistic",
    
    "build-scale-and-monetize-an-ai-translation-and-localization-service-with-chatgpt-and-makecom": "Cinematic 8K shot of a translation playbook with ChatGPT and Make.com workflow diagrams, multilingual document examples, revenue calculator, warm silver and coral, photorealistic",
    
    "fetch-the-transaction-from-plaid-sandbox": "Cinematic 8K shot of a technical payment integration playbook, Plaid API documentation, code snippets, sandbox test results, fintech dashboard, electric green and dark slate, photorealistic",
    
    "24-procedures-12-modules-12-hours-of-reading-and-execution": "Cinematic 8K dramatic shot of a massive automation agency playbook, 12 module tabs visible, procedural checklists, Make.com workflow screenshots, warm copper and charcoal, photorealistic",
    
    "ai-bookkeeping-automation-playbook": "Cinematic 8K shot of a bookkeeping playbook with QuickBooks integration guides, receipt processing workflows, monthly reconciliation checklists, warm teal and gold, photorealistic",
    
    "ai-video-production-agency-playbook": "Cinematic 8K shot of a video production playbook, HeyGen workflow guides, script templates, editing checklists, camera equipment visible, rich red and dark teal, photorealistic",
    
    "ai-lead-generation-playbook": "Cinematic 8K shot of a lead generation playbook, CRM setup guides, outreach sequence templates, conversion funnel diagrams, warm amber and deep purple, photorealistic",
    
    "ai-seo-agency-playbook": "Cinematic 8K shot of an SEO agency playbook, keyword research methodology, Semrush workflow guides, ranking milestone tracker, deep emerald and warm copper, photorealistic",
    
    "ai-cold-email-outreach-playbook": "Cinematic 8K shot of a cold email playbook, email sequence templates, personalization frameworks, deliverability checklists, warm slate and electric green, photorealistic",
    
    "ai-email-marketing-automation-playbook": "Cinematic 8K shot of an email marketing playbook, Klaviyo automation flows, campaign templates, segmentation strategies, warm terracotta and navy, photorealistic",
    
    "ai-hr-recruitment-automation-playbook": "Cinematic 8K shot of an HR recruitment playbook, Greenhouse setup guides, candidate scoring rubrics, interview automation workflows, warm navy and coral, photorealistic",
    
    "ai-copywriting-agency-playbook": "Cinematic 8K shot of a copywriting agency playbook, ChatGPT prompt libraries, A/B testing frameworks, client onboarding templates, warm cream and rich burgundy, photorealistic",
    
    "ai-marketplace-launch-playbook": "Cinematic 8K shot of a marketplace launch playbook, platform architecture diagrams, vendor onboarding flows, payment integration guides, vibrant teal and warm orange, photorealistic",
    
    "ai-customer-onboarding-agency-playbook": "Cinematic 8K shot of a customer onboarding playbook, welcome sequence templates, product tour guides, retention analytics dashboards, warm coral and charcoal, photorealistic",
    
    "ai-automation-agency-playbook": "Cinematic 8K shot of an automation agency playbook, Make.com scenario templates, client delivery frameworks, pricing calculators, electric teal and warm copper, photorealistic",
    
    "ai-side-hustle-blueprint": "Cinematic 8K shot of a side hustle blueprint, 5-step quick-start guide, revenue calculator, time management templates, warm amber and dark charcoal, photorealistic minimalist desk",
    
    "automation-agency-starter-kit": "Cinematic 8K shot of an automation agency starter kit, 26-step launch checklist, Make.com beginner workflows, pricing guide, client proposal templates, warm copper and navy, photorealistic",
    
    "chatgpt-prompt-engineering-guide": "Cinematic 8K shot of a prompt engineering guide, ChatGPT interface with advanced prompts, prompt pattern library, output comparison charts, warm mahogany and cream, photorealistic",
}

def generate_image(prompt, output_path, size="1344x768"):
    """Generate an image using z-ai-generate CLI."""
    cmd = [
        "z-ai-generate",
        "--prompt", prompt,
        "--output", str(output_path),
        "--size", size
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode == 0 and output_path.exists():
            size_bytes = output_path.stat().st_size
            if size_bytes > 5000:
                return True, f"OK ({size_bytes//1024}KB)"
            else:
                output_path.unlink(missing_ok=True)
                return False, f"Too small ({size_bytes}B)"
        return False, result.stderr[-200:] if result.stderr else "Unknown error"
    except subprocess.TimeoutExpired:
        return False, "Timeout"
    except Exception as e:
        return False, str(e)

def read_front_matter(filepath):
    """Read YAML front matter from a Hugo content file."""
    with open(filepath, 'r') as f:
        content = f.read()
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if match:
        return match.group(1)
    return ""

def get_image_field(front_matter, field):
    """Extract a field value from front matter."""
    match = re.search(rf'^{field}:\s*["\']?(.*?)["\']?\s*$', front_matter, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None

def main():
    sections = {
        "opportunities": (CONTENT / "opportunities", OPPORTUNITIES_PROMPTS),
        "intelligence": (CONTENT / "intelligence", INTELLIGENCE_PROMPTS),
        "playbooks": (CONTENT / "playbooks", PLAYBOOKS_PROMPTS),
    }
    
    results = {"success": [], "failed": [], "skipped": []}
    total = sum(len(p) for _, p in sections.values()) + len(PLAYBOOKS_PROMPTS)  # + PDFs
    
    print(f"🎨 Menshly Hero Image Generator")
    print(f"   Total images to generate: {total} heroes + {len(PLAYBOOKS_PROMPTS)} PDF covers = {total + len(PLAYBOOKS_PROMPTS)}")
    print()
    
    # Generate hero + thumbnail images for each article
    for section_name, (section_dir, prompts) in sections.items():
        print(f"\n📁 Processing {section_name.upper()} ({len(prompts)} articles)")
        print("=" * 60)
        
        for slug, prompt in prompts.items():
            # Find the actual content file
            content_file = section_dir / f"{slug}.md"
            if not content_file.exists():
                print(f"  ⚠️  {slug}: Content file not found, skipping")
                results["skipped"].append(f"{section_name}/{slug}")
                continue
            
            # Determine output paths
            hero_path = HERO_DIR / section_name / f"{slug}.png"
            thumb_path = THUMB_DIR / section_name / f"{slug}.png"
            
            # Generate hero image (1344x768 for widescreen)
            print(f"  🖼️  Generating hero: {slug}...")
            ok, msg = generate_image(prompt, hero_path, "1344x768")
            if ok:
                print(f"  ✅ Hero: {msg}")
                
                # Copy hero as thumbnail too (same image, different path)
                import shutil
                shutil.copy2(hero_path, thumb_path)
                
                results["success"].append(f"{section_name}/{slug}")
                
                # Update front matter if needed
                fm = read_front_matter(content_file)
                expected_image = f"/images/articles/{section_name}/{slug}.png"
                expected_hero = f"/images/heroes/{section_name}/{slug}.png"
                
                current_image = get_image_field(fm, "image")
                current_hero = get_image_field(fm, "heroImage")
                
                needs_update = False
                if current_image != expected_image:
                    needs_update = True
                if current_hero != expected_hero:
                    needs_update = True
                
                if needs_update:
                    with open(content_file, 'r') as f:
                        content = f.read()
                    
                    # Update image field
                    if current_image:
                        content = re.sub(r'^image:.*$', f'image: "{expected_image}"', content, flags=re.MULTILINE)
                    else:
                        # Add after title
                        content = re.sub(r'^(title:.*)$', f'\\1\nimage: "{expected_image}"', content, flags=re.MULTILINE)
                    
                    # Update heroImage field
                    if current_hero:
                        content = re.sub(r'^heroImage:.*$', f'heroImage: "{expected_hero}"', content, flags=re.MULTILINE)
                    else:
                        content = re.sub(r'^(image:.*)$', f'\\1\nheroImage: "{expected_hero}"', content, flags=re.MULTILINE)
                    
                    with open(content_file, 'w') as f:
                        f.write(content)
                    print(f"  📝 Updated front matter")
            else:
                print(f"  ❌ Hero failed: {msg}")
                results["failed"].append(f"{section_name}/{slug}")
            
            # Rate limit: small delay between generations
            time.sleep(2)
    
    # Generate PDF cover images
    print(f"\n📁 Processing PDF COVERS ({len(PLAYBOOKS_PROMPTS)} playbooks)")
    print("=" * 60)
    
    for slug, prompt in PLAYBOOKS_PROMPTS.items():
        pdf_cover_path = PDF_DIR / f"{slug}.png"
        
        # PDF cover prompt variant - more document-like
        pdf_prompt = prompt.replace("Cinematic 8K", "Cinematic 8K professional document cover design of")
        
        print(f"  📄 Generating PDF cover: {slug}...")
        ok, msg = generate_image(pdf_prompt, pdf_cover_path, "864x1152")  # Portrait for PDF
        if ok:
            print(f"  ✅ PDF cover: {msg}")
            results["success"].append(f"pdf/{slug}")
        else:
            print(f"  ❌ PDF cover failed: {msg}")
            results["failed"].append(f"pdf/{slug}")
        
        time.sleep(2)
    
    # Summary
    print(f"\n{'='*60}")
    print(f"📊 GENERATION SUMMARY")
    print(f"{'='*60}")
    print(f"  ✅ Success: {len(results['success'])}")
    print(f"  ❌ Failed:  {len(results['failed'])}")
    print(f"  ⚠️  Skipped: {len(results['skipped'])}")
    
    if results['failed']:
        print(f"\n  Failed items:")
        for item in results['failed']:
            print(f"    - {item}")
    
    # Save results
    report_path = REPO / "data/image_regeneration_report.json"
    with open(report_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n  Report saved to: {report_path}")

if __name__ == "__main__":
    main()
