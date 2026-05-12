#!/bin/bash
# Menshly Hero Image Generator - Batch 1: Opportunities (first 20)
set -e

REPO="/home/z/my-project/menshly-global-repo"

gen() {
  local slug="$1"
  local section="$2"
  local prompt="$3"
  local hero="$REPO/static/images/heroes/$section/$slug.png"
  local thumb="$REPO/static/images/articles/$section/$slug.png"
  
  if [ -f "$hero" ] && [ $(stat -c%s "$hero" 2>/dev/null || echo 0) -gt 5000 ]; then
    echo "⏭️  SKIP $slug (exists)"
    return 0
  fi
  
  echo "🖼️  GEN $slug..."
  z-ai-generate -p "$prompt" -o "$hero" -s 1344x768 2>&1 | tail -1
  
  if [ -f "$hero" ] && [ $(stat -c%s "$hero" 2>/dev/null || echo 0) -gt 5000 ]; then
    cp "$hero" "$thumb"
    echo "✅ $slug done ($(du -h "$hero" | cut -f1))"
  else
    echo "❌ $slug failed"
  fi
}

# ===== OPPORTUNITIES BATCH 1 =====
echo "📁 OPPORTUNITIES BATCH 1 (20 articles)"
echo "========================================"

gen "ai-ecommerce-optimization-agency" "opportunities" \
  "Cinematic 8K overhead shot of a modern e-commerce dashboard on a large monitor, showing product analytics charts, conversion funnels, and AI-powered recommendation widgets, vibrant data visualization in orange and teal, sleek glass desk with smartphone showing Shopify app, photorealistic, dramatic lighting"

gen "how-to-build-an-ai-legal-document-automation-agency-5k-30kmonth" "opportunities" \
  "Cinematic 8K close-up of a courtroom-style wooden desk with legal documents being scanned by a robotic arm, AI holographic interface showing contract analysis, warm amber desk lamp lighting, leather briefcase, scales of justice, photorealistic dramatic lighting"

gen "how-to-build-an-ai-translation-and-localization-service-3k-20kmonth" "opportunities" \
  "Cinematic 8K dramatic shot of multiple floating holographic screens showing different languages being translated in real-time, world map with glowing connection lines, earbuds and microphone on a white marble desk, vibrant green and coral accents, photorealistic"

gen "how-to-build-an-ai-translation-and-localization-service-in-2026-3k-20kmonth" "opportunities" \
  "Cinematic 8K shot of a sleek translation booth with neural network visualization on curved monitors, headphones on stand, flags of nations as small holograms, cool silver and warm orange palette, photorealistic studio lighting"

gen "ai-api-wrapper-business" "opportunities" \
  "Cinematic 8K macro shot of server racks with glowing fiber optic cables, API endpoint visualization floating as holographic code, circuit board patterns in emerald green and deep purple, data streaming effects, photorealistic tech aesthetic"

gen "ai-grant-writing-service" "opportunities" \
  "Cinematic 8K overhead of an elegant wooden desk with grant proposal documents, fountain pen, university crest seal, AI assistant chat window on tablet showing proposal drafting, warm burgundy and cream tones, photorealistic academic setting"

gen "how-to-build-an-ai-contract-and-proposal-writing-service-in-2026-5k25kmonth" "opportunities" \
  "Cinematic 8K shot of a professional office desk with proposal documents stacked neatly, AI chat interface on a large monitor drafting contracts, silver pen, leather portfolio, charcoal and copper color scheme, photorealistic"

gen "ai-bookkeeping-automation" "opportunities" \
  "Cinematic 8K dramatic shot of a modern accounting workspace, dual monitors showing QuickBooks dashboard with AI insights, calculator, spreadsheets with green highlights, coffee cup, warm wood and steel aesthetic, photorealistic"

gen "ai-video-production-agency" "opportunities" \
  "Cinematic 8K shot of a professional video editing suite, large monitors showing timeline with AI-generated video clips, camera on tripod, studio lighting rig, boom microphone, rich red and dark teal palette, photorealistic"

gen "ai-data-annotation-and-training-service" "opportunities" \
  "Cinematic 8K macro of data labeling interface on ultra-wide monitor, bounding boxes around objects in images, AI training pipeline visualization, neural network nodes in warm amber, dark workspace, photorealistic"

gen "ai-hr-recruitment-automation-agency" "opportunities" \
  "Cinematic 8K shot of a modern HR office, multiple screens showing candidate profiles with AI matching scores, video interview window, Greenhouse logo on display, warm coral and navy palette, photorealistic"

gen "how-to-launch-an-ai-personal-finance-automation-service-in-2026-2k-10kmonth" "opportunities" \
  "Cinematic 8K dramatic shot of personal finance dashboard on a tablet and laptop, budget charts, investment portfolio with AI recommendations, bank card, coins, deep green and gold accents, photorealistic home office"

gen "ai-customer-support-automation-agency" "opportunities" \
  "Cinematic 8K shot of a modern call center with AI chatbot interface on curved monitors, customer satisfaction metrics, Zendesk-style dashboard, headset on desk, teal and warm white palette, photorealistic"

gen "ai-real-estate-marketing-agency" "opportunities" \
  "Cinematic 8K aerial view of luxury real estate with AI-generated property listing on a tablet, virtual tour interface, Zillow-style map, warm sunset golden hour, architectural photography style, photorealistic"

gen "how-to-launch-an-ai-appointment-booking-automation-business-in-2026-2k15kmonth" "opportunities" \
  "Cinematic 8K shot of a reception desk with AI booking system on a sleek monitor, calendar grid with appointments, Calendly-style interface, modern office lobby, warm wood and white palette, photorealistic"

gen "ai-course-creation-business-2026" "opportunities" \
  "Cinematic 8K shot of an online course creation studio, monitor showing course builder with AI-generated lesson plans, microphone for voiceover, ring light, notebook with curriculum outline, warm terracotta and cream, photorealistic"

gen "ai-content-repurposing-agency-2026" "opportunities" \
  "Cinematic 8K dramatic shot of content repurposing workflow, large monitor showing one blog post being split into social media posts, tweets, and video scripts by AI, vibrant magenta and dark slate palette, photorealistic"

gen "ai-resume-career-service-2026" "opportunities" \
  "Cinematic 8K overhead of a desk with resume documents, AI resume builder on laptop screen showing optimized CV, professional headshot being analyzed, LinkedIn interface, navy and warm gold, photorealistic"

gen "ai-freelance-marketplace-2026" "opportunities" \
  "Cinematic 8K shot of a freelancer workspace, Replit code editor on screen with AI freelancer matching interface, multiple project cards floating as holograms, purple and warm amber palette, photorealistic"

gen "ai-saas-micro-products-replit-2026" "opportunities" \
  "Cinematic 8K dramatic shot of Replit IDE on large monitor building a SaaS micro-product, code editor with AI pair programming, deployment pipeline visualization, electric blue and orange accents, photorealistic"

echo ""
echo "✅ Opportunities Batch 1 complete (20 articles)"
