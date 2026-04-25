#!/bin/bash
set -e

echo "=== MENSHLY GLOBAL — Build & Deploy ==="

# Clean previous build
rm -rf output

# Build Hugo
echo "Building Hugo site..."
hugo --minify --destination output

# Count pages
PAGES=$(find output -name "*.html" | wc -l)
echo "Built ${PAGES} pages"

# Deploy via Wrangler
echo "Deploying to CloudFlare Pages..."
npx wrangler pages deploy output --project-name=menshly-global

echo "=== Deploy complete ==="
