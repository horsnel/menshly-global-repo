#!/bin/bash
# Robust playbook image regenerator with aggressive retry and delays
BASE="/home/z/my-project/menshly-global-repo"
THUMB_DIR="$BASE/static/images/articles/playbooks"
HERO_DIR="$BASE/static/images/heroes/playbooks"
LOG="$BASE/regen_log.txt"
DELAY=60  # base delay between successful requests

log() { echo "$(date '+%H:%M:%S'): $1" >> "$LOG"; }

TPRE='Ultra-premium editorial illustration: an elite playbook blueprint for'
TSUF=', a grand dark open book floating in deep black space with luminous pages revealing modular workflow diagrams, geometric checklists and procedure flowcharts rendered in crimson and red, floating red-rimmed module cards arranged in a grid pattern, crystalline milestone markers with warm red glow, strictly using deep black (#0A0A0A) background with gold (#FF0004) accent lighting and highlights, premium minimalist dark aesthetic, bold geometric shapes with luminous red edges and warm crimson glow, abstract futuristic tech aesthetic with atmospheric depth, professional magazine cover quality, ABSOLUTELY NO TEXT NO WORDS NO LETTERS NO NUMBERS NO CHARACTERS NO WRITING NO SCRIPT NO TYPOGRAPHY NO CALLIGRAPHY NO SIGNS NO LABELS NO CAPTIONS NO CHINESE NO JAPANESE NO KOREAN NO ARABIC NO HINDI NO SYMBOLS THAT RESEMBLE WRITING completely text-free image, sharp clean vector-quality edges, 8K quality'

HPRE='Cinematic wide hero banner: a grand vaulted chamber for'
HSUF=', red light streaming from a central floating open playbook, illuminating floating holographic procedure icons and modular step markers, deep black atmospheric walls receding into dramatic perspective, illuminated red columns representing playbook modules, volumetric red light rays creating atmospheric depth, strictly using deep black (#0A0A0A) atmospheric background with brilliant red (#FF0004) light streams and accents, epic dramatic composition with volumetric red light rays, premium minimalist dark aesthetic, premium editorial magazine quality, ABSOLUTELY NO TEXT NO WORDS NO LETTERS NO NUMBERS NO CHARACTERS NO WRITING NO SCRIPT NO TYPOGRAPHY NO CALLIGRAPHY NO SIGNS NO LABELS NO CAPTIONS NO CHINESE NO JAPANESE NO KOREAN NO ARABIC NO HINDI NO SYMBOLS THAT RESEMBLE WRITING completely text-free image, ultra-clean sharp edges, atmospheric depth with layered black gradient, 8K quality'

gen() {
    local prompt="$1" output="$2" attempt=0 max=10 wait=90
    while [ $attempt -lt $max ]; do
        if z-ai-generate -p "$prompt" -o "$output" -s 1344x768 2>&1 | rg -q "completed"; then
            log "✅ $output"
            return 0
        fi
        attempt=$((attempt+1))
        log "❌ Attempt $attempt/$max: $output - waiting ${wait}s"
        sleep $wait
        wait=$((wait+30))
    done
    log "💀 FAILED: $output"
    return 1
}

# All items to process
declare -a ITEMS=(
    # Remaining thumbnails
    "T|ai-ecommerce-optimization-playbook|AI E-commerce Optimization Playbook"
    "T|ai-email-marketing-automation-playbook|AI Email Marketing Automation Playbook"
    "T|ai-hr-recruitment-automation-playbook|AI HR Recruitment Automation Playbook"
    "T|ai-lead-generation-playbook|AI Lead Generation Business Playbook"
    "T|ai-marketplace-launch-playbook|AI Marketplace Launch Playbook"
    "T|ai-seo-agency-playbook|AI SEO Agency Playbook"
    "T|ai-side-hustle-blueprint|AI Side Hustle Blueprint"
    "T|ai-video-production-agency-playbook|AI Video Production Agency Playbook"
    "T|automation-agency-starter-kit|Automation Agency Starter Kit"
    "T|build-scale-and-monetize-an-ai-translation-and-localization-service-with-chatgpt-and-makecom|AI Translation and Localization Playbook"
    "T|chatgpt-prompt-engineering-guide|ChatGPT Prompt Engineering Guide"
    "T|fetch-the-transaction-from-plaid-sandbox|Plaid Integration Playbook"
    # All heroes
    "H|24-procedures-12-modules-12-hours-of-reading-and-execution|AI Automation Agency Playbook"
    "H|ai-automation-agency-playbook|AI Automation Agency Playbook"
    "H|ai-bookkeeping-automation-playbook|AI Bookkeeping Automation Playbook"
    "H|ai-cold-email-outreach-playbook|AI Cold Email Outreach Agency Playbook"
    "H|ai-copywriting-agency-playbook|AI Copywriting Agency Playbook"
    "H|ai-customer-onboarding-agency-playbook|AI Customer Onboarding Agency Playbook"
    "H|ai-ecommerce-optimization-playbook|AI E-commerce Optimization Playbook"
    "H|ai-email-marketing-automation-playbook|AI Email Marketing Automation Playbook"
    "H|ai-hr-recruitment-automation-playbook|AI HR Recruitment Automation Playbook"
    "H|ai-lead-generation-playbook|AI Lead Generation Business Playbook"
    "H|ai-marketplace-launch-playbook|AI Marketplace Launch Playbook"
    "H|ai-seo-agency-playbook|AI SEO Agency Playbook"
    "H|ai-side-hustle-blueprint|AI Side Hustle Blueprint"
    "H|ai-video-production-agency-playbook|AI Video Production Agency Playbook"
    "H|automation-agency-starter-kit|Automation Agency Starter Kit"
    "H|build-scale-and-monetize-an-ai-translation-and-localization-service-with-chatgpt-and-makecom|AI Translation and Localization Playbook"
    "H|chatgpt-prompt-engineering-guide|ChatGPT Prompt Engineering Guide"
    "H|fetch-the-transaction-from-plaid-sandbox|Plaid Integration Playbook"
)

log "=== STARTING REGENERATION (30 images) ==="
for entry in "${ITEMS[@]}"; do
    IFS='|' read -r type slug title <<< "$entry"
    if [ "$type" = "T" ]; then
        prompt="${TPRE} ${title}${TSUF}"
        output="$THUMB_DIR/${slug}.png"
    else
        prompt="${HPRE} ${title}${HSUF}"
        output="$HERO_DIR/${slug}.png"
    fi
    gen "$prompt" "$output"
    sleep $DELAY
done

log "=== FINAL SIZES ==="
ls -lh "$THUMB_DIR"/*.png >> "$LOG"
ls -lh "$HERO_DIR"/*.png >> "$LOG"
log "=== DONE ==="
