#!/bin/bash
# Menshly Hero Image Generator - ALL articles
# Generates high-quality topic-specific images for opportunities, intelligence, playbooks, and PDFs

REPO="/home/z/my-project/menshly-global-repo"

gen() {
  local slug="$1"
  local section="$2"
  local prompt="$3"
  local size="${4:-1344x768}"
  local hero="$REPO/static/images/heroes/$section/$slug.png"
  local thumb="$REPO/static/images/articles/$section/$slug.png"
  
  echo -n "🖼️  $section/$slug... "
  
  z-ai-generate -p "$prompt" -o "$hero" -s "$size" 2>/dev/null
  
  if [ -f "$hero" ] && [ $(stat -c%s "$hero" 2>/dev/null || echo 0) -gt 5000 ]; then
    cp "$hero" "$thumb"
    local sz=$(du -h "$hero" | cut -f1)
    echo "✅ $sz"
    return 0
  else
    rm -f "$hero"
    echo "❌ FAILED"
    return 1
  fi
}

FAILED=0
SUCCESS=0

# ===== OPPORTUNITIES (40 articles) =====
echo ""
echo "📁 OPPORTUNITIES (40 articles)"
echo "========================================"

gen "ai-ecommerce-optimization-agency" "opportunities" \
  "Cinematic 8K overhead shot of a modern e-commerce dashboard on a large monitor, showing product analytics charts, conversion funnels, and AI-powered recommendation widgets, vibrant data visualization in orange and teal, sleek glass desk with smartphone showing Shopify app, photorealistic, dramatic lighting" && ((SUCCESS++)) || ((FAILED++))

gen "how-to-build-an-ai-legal-document-automation-agency-5k-30kmonth" "opportunities" \
  "Cinematic 8K close-up of a courtroom-style wooden desk with legal documents being scanned by a robotic arm, AI holographic interface showing contract analysis, warm amber desk lamp lighting, leather briefcase, scales of justice, photorealistic dramatic lighting" && ((SUCCESS++)) || ((FAILED++))

gen "how-to-build-an-ai-translation-and-localization-service-3k-20kmonth" "opportunities" \
  "Cinematic 8K dramatic shot of multiple floating holographic screens showing different languages being translated in real-time, world map with glowing connection lines, earbuds and microphone on a white marble desk, vibrant green and coral accents, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "how-to-build-an-ai-translation-and-localization-service-in-2026-3k-20kmonth" "opportunities" \
  "Cinematic 8K shot of a sleek translation booth with neural network visualization on curved monitors, headphones on stand, flags of nations as small holograms, cool silver and warm orange palette, photorealistic studio lighting" && ((SUCCESS++)) || ((FAILED++))

gen "ai-api-wrapper-business" "opportunities" \
  "Cinematic 8K macro shot of server racks with glowing fiber optic cables, API endpoint visualization floating as holographic code, circuit board patterns in emerald green and deep purple, data streaming effects, photorealistic tech aesthetic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-grant-writing-service" "opportunities" \
  "Cinematic 8K overhead of an elegant wooden desk with grant proposal documents, fountain pen, university crest seal, AI assistant chat window on tablet showing proposal drafting, warm burgundy and cream tones, photorealistic academic setting" && ((SUCCESS++)) || ((FAILED++))

gen "how-to-build-an-ai-contract-and-proposal-writing-service-in-2026-5k25kmonth" "opportunities" \
  "Cinematic 8K shot of a professional office desk with proposal documents stacked neatly, AI chat interface on a large monitor drafting contracts, silver pen, leather portfolio, charcoal and copper color scheme, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-bookkeeping-automation" "opportunities" \
  "Cinematic 8K dramatic shot of a modern accounting workspace, dual monitors showing QuickBooks dashboard with AI insights, calculator, spreadsheets with green highlights, coffee cup, warm wood and steel aesthetic, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-video-production-agency" "opportunities" \
  "Cinematic 8K shot of a professional video editing suite, large monitors showing timeline with AI-generated video clips, camera on tripod, studio lighting rig, boom microphone, rich red and dark teal palette, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-data-annotation-and-training-service" "opportunities" \
  "Cinematic 8K macro of data labeling interface on ultra-wide monitor, bounding boxes around objects in images, AI training pipeline visualization, neural network nodes in warm amber, dark workspace, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-hr-recruitment-automation-agency" "opportunities" \
  "Cinematic 8K shot of a modern HR office, multiple screens showing candidate profiles with AI matching scores, video interview window, Greenhouse logo on display, deep black and red (#FF0004) palette, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "how-to-launch-an-ai-personal-finance-automation-service-in-2026-2k-10kmonth" "opportunities" \
  "Cinematic 8K dramatic shot of personal finance dashboard on a tablet and laptop, budget charts, investment portfolio with AI recommendations, bank card, coins, deep black (#0A0A0A) and red (#FF0004) accents, photorealistic home office" && ((SUCCESS++)) || ((FAILED++))

gen "ai-customer-support-automation-agency" "opportunities" \
  "Cinematic 8K shot of a modern call center with AI chatbot interface on curved monitors, customer satisfaction metrics, Zendesk-style dashboard, headset on desk, teal and warm white palette, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-real-estate-marketing-agency" "opportunities" \
  "Cinematic 8K aerial view of luxury real estate with AI-generated property listing on a tablet, virtual tour interface, Zillow-style map, dramatic red (#FF0004) light streams, architectural photography style, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "how-to-launch-an-ai-appointment-booking-automation-business-in-2026-2k15kmonth" "opportunities" \
  "Cinematic 8K shot of a reception desk with AI booking system on a sleek monitor, calendar grid with appointments, Calendly-style interface, modern office lobby, warm wood and white palette, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-course-creation-business-2026" "opportunities" \
  "Cinematic 8K shot of an online course creation studio, monitor showing course builder with AI-generated lesson plans, microphone for voiceover, ring light, notebook with curriculum outline, warm terracotta and cream, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-content-repurposing-agency-2026" "opportunities" \
  "Cinematic 8K dramatic shot of content repurposing workflow, large monitor showing one blog post being split into social media posts, tweets, and video scripts by AI, vibrant magenta and dark slate palette, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-resume-career-service-2026" "opportunities" \
  "Cinematic 8K overhead of a desk with resume documents, AI resume builder on laptop screen showing optimized CV, professional headshot being analyzed, LinkedIn interface, black (#0A0A0A) and red (#FF0004), photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-freelance-marketplace-2026" "opportunities" \
  "Cinematic 8K shot of a freelancer workspace, Replit code editor on screen with AI freelancer matching interface, multiple project cards floating as holograms, purple and warm amber palette, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-saas-micro-products-replit-2026" "opportunities" \
  "Cinematic 8K dramatic shot of Replit IDE on large monitor building a SaaS micro-product, code editor with AI pair programming, deployment pipeline visualization, electric blue and orange accents, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-voice-agent-agency-2026" "opportunities" \
  "Cinematic 8K shot of a voice AI studio, Vapi dashboard on monitor showing voice agent configuration, studio microphone, sound wave visualization, waveform in coral red, dark acoustic panels, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-social-media-agency-2026" "opportunities" \
  "Cinematic 8K overhead of a social media command center, multiple screens showing AI-generated posts scheduling, analytics dashboards, Buffer interface, vibrant gradient from coral to deep purple, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-data-analysis-service-2026" "opportunities" \
  "Cinematic 8K macro of data visualization on ultra-wide monitor, interactive charts and graphs with AI insights panel, Python code editor, Jupyter notebook, warm teal and amber color scheme, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-appointment-booking-agency-2026" "opportunities" \
  "Cinematic 8K shot of a modern salon reception with AI booking tablet mounted on counter, appointment calendar with smart scheduling, warm wooden interior, soft ambient lighting, cream and forest green, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-seo-agency-2026" "opportunities" \
  "Cinematic 8K dramatic shot of SEO dashboard on dual monitors, keyword ranking charts, backlink analysis, Semrush-style interface, search engine results visualization, deep emerald and warm copper, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-affiliate-marketing-business" "opportunities" \
  "Cinematic 8K overhead of affiliate marketing dashboard, commission tracking charts, product comparison widgets, Semrush analytics, revenue graphs trending upward, rich burgundy and teal, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-resume-career-service" "opportunities" \
  "Cinematic 8K shot of a career coaching office, AI resume optimizer on screen, professional headshot gallery, interview preparation interface, warm mahogany and cream, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-lead-generation-agency-2026" "opportunities" \
  "Cinematic 8K shot of lead generation pipeline visualization on curved monitor, CRM dashboard with AI scoring, sales funnel with conversion rates, orange and charcoal palette, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-chatbot-ecommerce-agency-2026" "opportunities" \
  "Cinematic 8K shot of an e-commerce store chatbot interface on tablet, AI product recommendations, shopping cart widget, customer conversation with purchase completion, deep black and red (#FF0004), photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-podcast-production-agency" "opportunities" \
  "Cinematic 8K dramatic shot of a podcast studio, professional microphone with pop filter, sound mixer, AI transcription on monitor, waveform visualization, rich burgundy and dark wood, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-cold-email-agency" "opportunities" \
  "Cinematic 8K shot of email outreach dashboard, AI-personalized email sequences on monitor, open rate analytics, reply tracking, warm slate grey and electric green accents, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "how-to-build-ai-powered-email-marketing-automation-in-2026-5000month-revenue-pot" "opportunities" \
  "Cinematic 8K dramatic shot of Klaviyo-style email marketing dashboard, automated campaign flows, subscriber segmentation with AI, open rate charts, deep black (#0A0A0A) and red (#FF0004), photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "fliki-ai-faceless-youtube-channel" "opportunities" \
  "Cinematic 8K shot of a faceless YouTube channel creation setup, Fliki AI interface on monitor generating video from script, thumbnail designs, YouTube Studio analytics, vibrant red and dark charcoal, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-newsletter-business" "opportunities" \
  "Cinematic 8K shot of newsletter creation workspace, Beehiiv editor on screen, subscriber growth charts, AI content suggestions, email template preview, warm cream and forest green, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-automation-agency" "opportunities" \
  "Cinematic 8K dramatic shot of Make.com automation workspace, workflow builder with connected apps, automation triggers and actions, Zapier-style flowchart, electric teal and warm copper, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-lead-generation-machine" "opportunities" \
  "Cinematic 8K macro of AI lead scoring interface, prospect database with engagement heatmaps, outreach sequence timeline, CRM integration, deep purple and warm amber, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "content-repurposing-agency-deep-dive" "opportunities" \
  "Cinematic 8K shot of content transformation studio, one piece of content being split into 10 formats on large monitor, blog to video to podcast to social conversion, coral and slate blue, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-copywriting-agency" "opportunities" \
  "Cinematic 8K shot of a creative writing desk, AI copywriting assistant on large monitor, multiple ad copy variations, A/B test results, ChatGPT interface, warm cream and rich burgundy, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "ai-agent-marketplaces-2026" "opportunities" \
  "Cinematic 8K shot of an AI agent marketplace interface, browsing custom GPT agents, agent comparison cards, user ratings, ChatGPT store style, vibrant teal and warm orange, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "gpt5-solo-entrepreneur" "opportunities" \
  "Cinematic 8K dramatic shot of a solo entrepreneur at a minimalist desk, GPT-5 interface on laptop running multiple business tasks simultaneously, calendar, invoices, content, warm amber and dark charcoal, photorealistic" && ((SUCCESS++)) || ((FAILED++))

gen "voice-ai-business-blueprint" "opportunities" \
  "Cinematic 8K shot of voice AI development workspace, Vapi configuration dashboard, voice waveform editor, telephony integration diagram, deep black (#0A0A0A) and red (#FF0004), photorealistic" && ((SUCCESS++)) || ((FAILED++))

echo ""
echo "📊 Opportunities: ✅ $SUCCESS | ❌ $FAILED"
