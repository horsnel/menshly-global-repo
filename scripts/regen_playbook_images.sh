#!/bin/bash
# Regenerate ALL playbook thumbnail and hero images with stronger anti-text prompts
# Includes retry logic with exponential backoff for API rate limits

set -e

BASE="/home/z/my-project/menshly-repo"
THUMB_DIR="$BASE/static/images/articles/playbooks"
HERO_DIR="$BASE/static/images/heroes/playbooks"

THUMB_PROMPT_PREFIX='Ultra-premium editorial illustration: an elite playbook blueprint for'
THUMB_PROMPT_SUFFIX=', a grand dark open book floating in deep black space with luminous pages revealing modular workflow diagrams, geometric checklists and procedure flowcharts rendered in crimson and red, floating red-rimmed module cards arranged in a grid pattern, crystalline milestone markers with warm red glow, strictly using deep black (#0A0A0A) background with red (#FF0004) accent lighting and highlights, premium minimalist dark aesthetic, bold geometric shapes with luminous red edges and warm crimson glow, abstract futuristic tech aesthetic with atmospheric depth, professional magazine cover quality, ABSOLUTELY NO TEXT NO WORDS NO LETTERS NO NUMBERS NO CHARACTERS NO WRITING NO SCRIPT NO TYPOGRAPHY NO CALLIGRAPHY NO SIGNS NO LABELS NO CAPTIONS NO CHINESE NO JAPANESE NO KOREAN NO ARABIC NO HINDI NO SYMBOLS THAT RESEMBLE WRITING completely text-free image, sharp clean vector-quality edges, 8K quality'

HERO_PROMPT_PREFIX='Cinematic wide hero banner: a grand vaulted chamber for'
HERO_PROMPT_SUFFIX=', red light streaming from a central floating open playbook, illuminating floating holographic procedure icons and modular step markers, deep black atmospheric walls receding into dramatic perspective, illuminated red columns representing playbook modules, volumetric red light rays creating atmospheric depth, strictly using deep black (#0A0A0A) atmospheric background with brilliant red (#FF0004) light streams and accents, epic dramatic composition with volumetric red light rays, premium minimalist dark aesthetic, premium editorial magazine quality, ABSOLUTELY NO TEXT NO WORDS NO LETTERS NO NUMBERS NO CHARACTERS NO WRITING NO SCRIPT NO TYPOGRAPHY NO CALLIGRAPHY NO SIGNS NO LABELS NO CAPTIONS NO CHINESE NO JAPANESE NO KOREAN NO ARABIC NO HINDI NO SYMBOLS THAT RESEMBLE WRITING completely text-free image, ultra-clean sharp edges, atmospheric depth with layered black gradient, 8K quality'

# All playbook filenames and their readable titles
declare -a FILENAMES=(
  "ai-automation-agency-playbook"
  "ai-email-marketing-automation-playbook"
  "ai-seo-agency-playbook"
  "build-scale-and-monetize-an-ai-translation-and-localization-service-with-chatgpt-and-makecom"
  "ai-hr-recruitment-automation-playbook"
  "ai-marketplace-launch-playbook"
  "fetch-the-transaction-from-plaid-sandbox"
  "ai-bookkeeping-automation-playbook"
  "chatgpt-prompt-engineering-guide"
  "ai-copywriting-agency-playbook"
  "ai-cold-email-outreach-playbook"
  "ai-side-hustle-blueprint"
  "ai-customer-onboarding-agency-playbook"
  "ai-ecommerce-optimization-playbook"
  "24-procedures-12-modules-12-hours-of-reading-and-execution"
  "ai-lead-generation-playbook"
  "automation-agency-starter-kit"
  "ai-video-production-agency-playbook"
)

declare -a TITLES=(
  "AI Automation Agency Playbook"
  "AI Email Marketing Automation Playbook"
  "AI SEO Agency Playbook"
  "AI Translation and Localization Service"
  "AI HR Recruitment Automation Playbook"
  "AI Marketplace Launch Playbook"
  "Fetch the Transaction from Plaid Sandbox"
  "AI Bookkeeping Automation Playbook"
  "ChatGPT Prompt Engineering Guide"
  "AI Copywriting Agency Playbook"
  "AI Cold Email Outreach Playbook"
  "AI Side Hustle Blueprint"
  "AI Customer Onboarding Agency Playbook"
  "AI Ecommerce Optimization Playbook"
  "24 Procedures 12 Modules 12 Hours"
  "AI Lead Generation Playbook"
  "Automation Agency Starter Kit"
  "AI Video Production Agency Playbook"
)

MAX_RETRIES=5
BASE_DELAY=15
SUCCESS_COUNT=0
FAIL_COUNT=0

generate_with_retry() {
  local prompt="$1"
  local output="$2"
  local attempt=1
  local delay=$BASE_DELAY

  while [ $attempt -le $MAX_RETRIES ]; do
    echo "  [Attempt $attempt/$MAX_RETRIES] Generating: $(basename "$output")"
    
    if z-ai-generate -p "$prompt" -o "$output" -s 1344x768 2>&1; then
      echo "  ✅ SUCCESS: $(basename "$output")"
      return 0
    fi
    
    echo "  ❌ Failed attempt $attempt for $(basename "$output")"
    
    if [ $attempt -lt $MAX_RETRIES ]; then
      echo "  ⏳ Waiting ${delay}s before retry..."
      sleep $delay
      delay=$((delay * 2))
      if [ $delay -gt 120 ]; then
        delay=120
      fi
    fi
    
    attempt=$((attempt + 1))
  done
  
  echo "  💀 PERMANENT FAILURE: $(basename "$output") after $MAX_RETRIES attempts"
  return 1
}

echo "======================================================"
echo "  PLAYBOOK IMAGE REGENERATION - ANTI-TEXT PROMPTS"
echo "  $(date)"
echo "======================================================"
echo ""

TOTAL=${#FILENAMES[@]}
echo "Found $TOTAL playbook files to regenerate"
echo "  Thumbnails: $THUMB_DIR"
echo "  Heroes:     $HERO_DIR"
echo ""

# Generate THUMBNAILS
echo "=========================================="
echo "  PHASE 1: THUMBNAIL IMAGES ($TOTAL)"
echo "=========================================="
for i in "${!FILENAMES[@]}"; do
  fname="${FILENAMES[$i]}"
  title="${TITLES[$i]}"
  output="$THUMB_DIR/${fname}.png"
  prompt="${THUMB_PROMPT_PREFIX} ${title}${THUMB_PROMPT_SUFFIX}"
  
  echo ""
  echo "[$((i+1))/$TOTAL] Thumbnail: $fname"
  echo "  Title: $title"
  
  if generate_with_retry "$prompt" "$output"; then
    SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
  else
    FAIL_COUNT=$((FAIL_COUNT + 1))
  fi
  
  # Delay between successful generations to avoid rate limits
  sleep 5
done

echo ""
echo "=========================================="
echo "  PHASE 2: HERO IMAGES ($TOTAL)"
echo "=========================================="
for i in "${!FILENAMES[@]}"; do
  fname="${FILENAMES[$i]}"
  title="${TITLES[$i]}"
  output="$HERO_DIR/${fname}.png"
  prompt="${HERO_PROMPT_PREFIX} ${title}${HERO_PROMPT_SUFFIX}"
  
  echo ""
  echo "[$((i+1))/$TOTAL] Hero: $fname"
  echo "  Title: $title"
  
  if generate_with_retry "$prompt" "$output"; then
    SUCCESS_COUNT=$((SUCCESS_COUNT + 1))
  else
    FAIL_COUNT=$((FAIL_COUNT + 1))
  fi
  
  # Delay between successful generations to avoid rate limits
  sleep 5
done

echo ""
echo "======================================================"
echo "  REGENERATION COMPLETE"
echo "  $(date)"
echo "======================================================"
echo "  Success: $SUCCESS_COUNT"
echo "  Failed:  $FAIL_COUNT"
echo ""

echo "=========================================="
echo "  FILE SIZE REPORT"
echo "=========================================="
echo ""
echo "--- THUMBNAILS ---"
for fname in "${FILENAMES[@]}"; do
  fpath="$THUMB_DIR/${fname}.png"
  if [ -f "$fpath" ]; then
    size=$(stat -c%s "$fpath" 2>/dev/null || stat -f%z "$fpath" 2>/dev/null || echo "N/A")
    echo "  ${fname}.png  -  ${size} bytes"
  else
    echo "  ${fname}.png  -  MISSING"
  fi
done

echo ""
echo "--- HEROES ---"
for fname in "${FILENAMES[@]}"; do
  fpath="$HERO_DIR/${fname}.png"
  if [ -f "$fpath" ]; then
    size=$(stat -c%s "$fpath" 2>/dev/null || stat -f%z "$fpath" 2>/dev/null || echo "N/A")
    echo "  ${fname}.png  -  ${size} bytes"
  else
    echo "  ${fname}.png  -  MISSING"
  fi
done
