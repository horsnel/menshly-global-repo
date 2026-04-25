// Cloudflare Pages Function: AI Article Generator
// Format prompts are stored server-side — NEVER exposed to the client
// Uses: Cerebras (text), Pexels + Pixabay (images)

export async function onRequestPost(context) {
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
  };

  try {
    const { category, topic, revenue, difficulty } = await context.request.json();

    if (!topic || !category) {
      return new Response(JSON.stringify({ error: 'Topic and category are required.' }), { status: 400, headers });
    }

    // Check Cerebras API key upfront for clear error messaging
    if (!context.env.CEREBRAS_API_KEY) {
      console.error('CEREBRAS_API_KEY not set in CloudFlare Pages environment');
      return new Response(JSON.stringify({ error: 'AI service not configured. CEREBRAS_API_KEY is missing. Set it in CloudFlare Pages → Settings → Environment variables.' }), { status: 503, headers });
    }

    const slug = topic.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
    const date = new Date().toISOString().split('T')[0];
    const topicTitle = topic.replace(/(?:^|\s)\S/g, t => t.toUpperCase());

    // Fetch images from Pexels + Pixabay + Pollination AI fallback in parallel
    const [pexelsImages, pixabayImages, pollinationImages] = await Promise.allSettled([
      fetchPexelsImages(topic, context.env.PEXELS_API_KEY),
      fetchPixabayImages(topic, context.env.PIXABAY_API_KEY),
      fetchPollinationImages(topic, slug)
    ]);

    const allImages = [
      ...(pexelsImages.status === 'fulfilled' ? pexelsImages.value : []),
      ...(pixabayImages.status === 'fulfilled' ? pixabayImages.value : []),
      ...(pollinationImages.status === 'fulfilled' ? pollinationImages.value : [])
    ];

    // Select hero image (landscape, high quality)
    const heroImage = allImages.find(img => img.width > img.height && img.width >= 1200) || allImages[0] || null;
    // Select thumbnail image
    const thumbnailImage = allImages.find(img => img.width >= 800) || allImages[0] || null;
    // Collect inline images (3-5 for article body)
    const inlineImages = allImages.slice(0, 5);

    // Build the system prompt based on category — FORMAT KEPT SECRET
    const systemPrompt = buildSystemPrompt(category);
    const userPrompt = buildUserPrompt(category, topicTitle, slug, date, revenue, difficulty);

    // Call Cerebras API for article generation
    const articleData = await callCerebras(
      context.env.CEREBRAS_API_KEY,
      systemPrompt,
      userPrompt,
      category
    );

    return new Response(JSON.stringify({
      success: true,
      article: articleData,
      images: {
        hero: heroImage,
        thumbnail: thumbnailImage,
        inline: inlineImages
      },
      meta: { category, topic: topicTitle, slug, date, revenue, difficulty }
    }), { status: 200, headers });

  } catch (error) {
    console.error('Article generation error:', error);
    return new Response(JSON.stringify({ error: 'Article generation failed. Please try again.' }), { status: 500, headers });
  }
}

export async function onRequestOptions() {
  return new Response(null, {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    }
  });
}

// ─── CEREBRAS API ───────────────────────────────────────────
async function callCerebras(apiKey, systemPrompt, userPrompt, category) {
  const maxTokens = category === 'playbook' ? 16000 : category === 'intelligence' ? 8000 : 6000;

  const response = await fetch('https://api.cerebras.ai/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${apiKey}`
    },
    body: JSON.stringify({
      model: 'llama-3.3-70b',
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: userPrompt }
      ],
      max_tokens: maxTokens,
      temperature: 0.8,
      top_p: 0.95
    })
  });

  if (!response.ok) {
    const err = await response.text();
    throw new Error(`Cerebras API error: ${response.status} - ${err}`);
  }

  const data = await response.json();
  const content = data.choices?.[0]?.message?.content || '';

  return parseGeneratedContent(content, category);
}

// ─── PEXELS API ─────────────────────────────────────────────
async function fetchPexelsImages(query, apiKey) {
  if (!apiKey) return [];
  try {
    const response = await fetch(`https://api.pexels.com/v1/search?query=${encodeURIComponent(query + ' AI technology business')}&per_page=8&orientation=landscape`, {
      headers: { 'Authorization': apiKey }
    });
    if (!response.ok) return [];
    const data = await response.json();
    return (data.photos || []).map(photo => ({
      url: photo.src.large2x || photo.src.large,
      thumbnail: photo.src.medium,
      width: photo.width,
      height: photo.height,
      alt: photo.alt || query,
      photographer: photo.photographer,
      source: 'pexels',
      sourceUrl: photo.url
    }));
  } catch (e) {
    return [];
  }
}

// ─── PIXABAY API ────────────────────────────────────────────
async function fetchPixabayImages(query, apiKey) {
  if (!apiKey) return [];
  try {
    const response = await fetch(`https://pixabay.com/api/?key=${apiKey}&q=${encodeURIComponent(query + ' AI technology')}&image_type=photo&orientation=horizontal&per_page=8&safesearch=true&min_width=800`);
    if (!response.ok) return [];
    const data = await response.json();
    return (data.hits || []).map(hit => ({
      url: hit.largeImageURL || hit.webformatURL,
      thumbnail: hit.webformatURL,
      width: hit.imageWidth,
      height: hit.imageHeight,
      alt: hit.tags || query,
      photographer: hit.user,
      source: 'pixabay',
      sourceUrl: hit.pageURL
    }));
  } catch (e) {
    return [];
  }
}

// ─── POLLINATION AI (FREE — NO API KEY NEEDED) ─────────────
async function fetchPollinationImages(query, slug) {
  try {
    const encoded = encodeURIComponent(query.toLowerCase() + ' AI technology business brutalist design');
    return [
      {
        url: `https://image.pollinations.ai/prompt/${encoded}?width=1200&height=630&nologo=true&seed=${slug}`,
        thumbnail: `https://image.pollinations.ai/prompt/${encoded}?width=672&height=384&nologo=true&seed=${slug}`,
        width: 1200,
        height: 630,
        alt: query,
        photographer: 'Pollination AI',
        source: 'pollination',
        sourceUrl: 'https://pollinations.ai'
      },
      {
        url: `https://image.pollinations.ai/prompt/${encodeURIComponent(query.toLowerCase() + ' workflow automation dashboard')}?width=1200&height=630&nologo=true&seed=${slug}-2`,
        thumbnail: `https://image.pollinations.ai/prompt/${encodeURIComponent(query.toLowerCase() + ' workflow automation dashboard')}?width=672&height=384&nologo=true&seed=${slug}-2`,
        width: 1200,
        height: 630,
        alt: query + ' workflow',
        photographer: 'Pollination AI',
        source: 'pollination',
        sourceUrl: 'https://pollinations.ai'
      }
    ];
  } catch (e) {
    return [];
  }
}

// ─── FORMAT PROMPTS (SERVER-SIDE ONLY — NEVER EXPOSED) ──────
function buildSystemPrompt(category) {
  const base = `You are a senior content strategist for Menshly Global, a platform about AI business opportunities. You write in a direct, no-nonsense voice. No fluff, no filler, no generic advice. Every sentence must deliver value. You use specific numbers, tool names, pricing, and actionable steps. You write in Markdown format. You include blockquotes for "ugly truths" and "hacks" using the > prefix.`;

  if (category === 'opportunity') {
    return base + ` You are writing an OPPORTUNITY article — a deep-dive discovery of a specific AI business model. The article must follow this exact structure:
1. Opening hook (2-3 paragraphs with revenue potential and why NOW)
2. "Why This Works Right Now" (market timing, data, trends)
3. "The Realistic Picture" (4 ugly truths as blockquotes with **Truth #1-4**)
4. "The Free Stack: Starting With Zero Dollars" (3-5 free tools with descriptions)
5. "The Paid Stack: When You're Ready to Scale" (4-6 paid tools with costs, total monthly cost line)
6. "The Workflow: Step-by-Step" (3-4 steps with substeps and time estimates)
7. "Pricing: What to Charge" (3-4 pricing tiers with what's included)
8. "Tricks and Hacks They Don't Share in Courses" (3-5 HACK blockquotes)
9. "The Real Numbers" (revenue projection table in Markdown with Month/Revenue/Clients/Notes)
10. "Start This Weekend" (Saturday morning, Saturday afternoon, Sunday actions)

Each section must be substantial — no placeholder text. Write as if you're giving away $200/hour consulting advice for free. Use specific tool names, prices, and configurations. Include HACK blockquotes with real techniques.`;
  }

  if (category === 'intelligence') {
    return base + ` You are writing an INTELLIGENCE article — a step-by-step implementation guide. The article must follow this exact structure:
1. Opening (why manual processes kill this business, set expectations)
2. "Prerequisites" (tools needed with costs, time required, total upfront cost)
3. "Step 1: [Setup/Tech Stack]" (detailed walkthrough with exact clicks and URLs, substeps, verification checkpoints)
4. "Step 1 Check-In" (3 verification items)
5. "Step 2: [Core Workflow Build]" (module-by-module walkthrough with configuration settings, error handling)
6. "Step 2 Check-In" (verification items)
7. "Step 3: [Production Pipeline]" (repeatable system, quality gates, scoring criteria)
8. "Step 3 Check-In" (verification items)
9. "Step 4: [Monitoring/Reporting/Delivery]" (automated reporting, alerts, client delivery)
10. "Step 5: [Pricing and Service Delivery]" (pricing table in Markdown with Tier/Monthly/Included/Cost/Margin columns, cost breakdown table)

Each step must include "Do you see X?" verification checkpoints. Write as if the reader has zero experience but is smart enough to follow precise instructions. No skipping steps. Every tool must be named with its cost. Every configuration must be specific.`;
  }

  if (category === 'playbook') {
    return base + ` You are writing a PLAYBOOK article — a premium procedure-based system. The article must follow this exact structure:
1. Opening (strong statement — this is not a blog post, it's an operating system, X procedures, X modules)
2. "MODULE 1: FOUNDATION" (overview + 2 procedures with exact steps + check-in)
3. "MODULE 2: TECH STACK" (overview + 2 procedures + total cost breakdown + check-in)
4. "MODULE 3: THE BUILD FRAMEWORK" (overview + 2 procedures with code/config + check-in)
5. "MODULE 4: FIRST CLIENT / FIRST REVENUE" (outreach scripts, demo call scripts, pricing presentation)
6. "MODULE 5: DELIVERY AND RETENTION" (SOPs, monthly calendar, churn prevention)
7. "MODULE 6: SCALING" (hiring roadmap, margin analysis table with Clients/Revenue/Team Cost/Tool Cost/Profit/Margin columns)

Every procedure must start with a clear action verb. Include exact URLs where possible. Use "Do you see X? If Y, do Z" verification patterns. The tone is authoritative and procedural — no theories, no possibilities, only exact actions. Each module must end with a Check-In section using checkboxes.`;
  }

  return base;
}

function buildUserPrompt(category, topic, slug, date, revenue, difficulty) {
  const revMap = {'1k-5k':'$1K-$5K','5k-10k':'$5K-$10K','10k-25k':'$10K-$25K','25k-50k':'$25K-$50K','50k+':'$50K+'};
  const rev = revMap[revenue] || '$10K-$25K';

  if (category === 'opportunity') {
    return `Write a complete OPPORTUNITY article about: "${topic}"

Target revenue range: ${rev}/month
Difficulty level: ${difficulty}
Date: ${date}
URL slug: ${slug}

The article title should follow the pattern: "How to Start a [TOPIC] in 2026 (Build Once, Get Paid Forever)"

Write the FULL article now. Every section must be complete with real, specific content. No placeholders. No "[Description]" text. Write actual content for every section.`;
  }

  if (category === 'intelligence') {
    return `Write a complete INTELLIGENCE implementation guide about: "${topic}"

Target revenue range: ${rev}/month
Difficulty level: ${difficulty}
Date: ${date}
URL slug: ${slug}

The article title should follow the pattern: "Build and Scale a [TOPIC] with Automated Workflows"

Write the FULL article now. Every step must be complete with specific tool names, URLs, configurations, and verification checkpoints. No placeholders. No "[Description]" text.`;
  }

  if (category === 'playbook') {
    return `Write a complete PLAYBOOK about: "${topic}"

Target revenue range: ${rev}/month
Difficulty level: ${difficulty}
Date: ${date}
URL slug: ${slug}

The article title should follow the pattern: "The [TOPIC] Playbook"

Write the FULL playbook now. Every module must be complete with exact procedures, tool configurations, and verification checkpoints. No placeholders. No "[Description]" text. This is a premium product worth $47-$49.`;
  }

  return `Write a complete article about: "${topic}"`;
}

// ─── PARSE GENERATED CONTENT ────────────────────────────────
function parseGeneratedContent(content, category) {
  // Extract title from first ## or # heading
  const titleMatch = content.match(/^#\s+(.+)$/m) || content.match(/^##?\s+(.+)$/m);
  const title = titleMatch ? titleMatch[1].replace(/\*\*/g, '').trim() : '';

  // Extract excerpt from first paragraph (non-heading, non-empty)
  const lines = content.split('\n');
  let excerpt = '';
  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#') && !trimmed.startsWith('---') && !trimmed.startsWith('>') && trimmed.length > 50) {
      excerpt = trimmed.substring(0, 200).replace(/\*\*/g, '');
      break;
    }
  }

  // Calculate read time based on word count
  const wordCount = content.split(/\s+/).length;
  const readTime = Math.max(5, Math.ceil(wordCount / 250)) + ' MIN';

  return {
    title,
    excerpt,
    content,
    wordCount,
    readTime,
    category: category === 'opportunity' ? 'AI Opportunity' : category === 'intelligence' ? 'Implementation' : 'Playbook'
  };
}
