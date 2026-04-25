// Cloudflare Pages Function: AI Article Generator
// Strategy 1: Pollinations "mistral" (free, not a reasoning model — clean content)
// Strategy 2: Pollinations "openai" (free, reasoning model — needs content extraction)
// Strategy 3: HuggingFace Inference API (free tier, optional API key)
// Strategy 4: Cerebras (if key available and working)
// Strategy 5: DeepSeek (if key available and working)
// Images: Pollinations AI (free) | Pexels | Pixabay

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

    const slug = topic.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
    const date = new Date().toISOString().split('T')[0];
    const topicTitle = topic.replace(/(?:^|\s)\S/g, t => t.toUpperCase());

    // Fetch images from all sources in parallel
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

    const heroImage = allImages.find(img => img.width > img.height && img.width >= 1200) || allImages[0] || null;
    const thumbnailImage = allImages.find(img => img.width >= 800) || allImages[0] || null;
    const inlineImages = allImages.slice(0, 5);

    // Build messages
    const revMap = {'1k-5k':'₦800K-₦4M','5k-10k':'₦4M-₦8M','10k-25k':'₦8M-₦20M','25k-50k':'₦20M-₦40M','50k+':'₦40M+'};
    const rev = revMap[revenue] || '₦8M-₦20M';
    const pollMessages = buildPollinationsMessages(category, topicTitle, rev, difficulty);
    const fullMessages = buildFullMessages(category, topicTitle, rev, difficulty, date);

    let content = '';
    const debugInfo = {};

    // ── Strategy 1: Pollinations "mistral" model (not a reasoning model) ──
    {
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 30000);
        const t0 = Date.now();

        const pollResp = await fetch('https://text.pollinations.ai/openai/chat/completions', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          signal: controller.signal,
          body: JSON.stringify({
            messages: pollMessages,
            model: 'mistral',
            max_tokens: 4000,
            temperature: 0.8,
            seed: Math.floor(Math.random() * 10000),
          }),
        });
        clearTimeout(timeoutId);

        if (pollResp.ok) {
          const respText = await pollResp.text();
          try {
            const data = JSON.parse(respText);
            const msgContent = data.choices?.[0]?.message?.content || '';
            const reasoningContent = data.choices?.[0]?.message?.reasoning_content || '';
            const candidate = msgContent || reasoningContent || '';

            debugInfo.pollinations_mistral = {
              elapsed: Date.now() - t0,
              msgLen: msgContent.length,
              reasonLen: reasoningContent.length,
              valid: !!(candidate && isValidArticle(candidate)),
              firstChars: candidate.substring(0, 80),
            };

            if (candidate && isValidArticle(candidate)) {
              content = candidate;
              console.log('Pollinations mistral: article generated, length:', content.length);
            }
          } catch (parseErr) {
            debugInfo.pollinations_mistral = { error: `JSON parse: ${parseErr.message}` };
          }
        } else {
          const errText = await pollResp.text().catch(() => '');
          debugInfo.pollinations_mistral = { error: `HTTP ${pollResp.status}: ${errText.substring(0, 100)}` };
        }
      } catch (e) {
        const errType = e.name === 'AbortError' ? 'timeout' : e.message;
        debugInfo.pollinations_mistral = { error: errType };
      }
    }

    // ── Strategy 2: Pollinations "openai" model (reasoning model with extraction) ──
    if (!content) {
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 30000);
        const t0 = Date.now();

        const pollResp = await fetch('https://text.pollinations.ai/openai/chat/completions', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          signal: controller.signal,
          body: JSON.stringify({
            messages: pollMessages,
            model: 'openai',
            max_tokens: 4000,
            temperature: 0.8,
            seed: Math.floor(Math.random() * 10000),
          }),
        });
        clearTimeout(timeoutId);

        if (pollResp.ok) {
          const respText = await pollResp.text();
          try {
            const data = JSON.parse(respText);
            const msgContent = data.choices?.[0]?.message?.content || '';
            const reasoningContent = data.choices?.[0]?.message?.reasoning_content || '';

            // The "openai" model is a reasoning model:
            // - content: actual article (when model has enough tokens)
            // - reasoning_content: model's thinking + sometimes the article
            let candidate = msgContent || reasoningContent || '';

            // Validate it's an actual article, not a plan/outline
            if (candidate && isValidArticle(candidate)) {
              content = candidate;
            }
            // If it looks like reasoning/plan, try extracting article from it
            else if (candidate && candidate.length > 300) {
              const extracted = extractArticleFromText(candidate);
              if (extracted) {
                content = extracted;
              }
            }

            debugInfo.pollinations_openai = {
              elapsed: Date.now() - t0,
              msgLen: msgContent.length,
              reasonLen: reasoningContent.length,
              valid: !!content,
              firstChars: (msgContent || reasoningContent || '').substring(0, 80),
            };

            if (content) {
              console.log('Pollinations openai: article generated, length:', content.length);
            }
          } catch (parseErr) {
            debugInfo.pollinations_openai = { error: `JSON parse: ${parseErr.message}` };
          }
        } else {
          const errText = await pollResp.text().catch(() => '');
          debugInfo.pollinations_openai = { error: `HTTP ${pollResp.status}: ${errText.substring(0, 100)}` };
        }
      } catch (e) {
        const errType = e.name === 'AbortError' ? 'timeout' : e.message;
        debugInfo.pollinations_openai = { error: errType };
      }
    }

    // ── Strategy 3: HuggingFace Inference API (free tier) ──
    if (!content) {
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 35000);
        const t0 = Date.now();

        // Build a simple text prompt for HF text generation
        const hfPrompt = buildHuggingFacePrompt(category, topicTitle, rev, difficulty);
        const hfApiKey = context.env.HF_API_KEY || '';

        const hfResp = await fetch('https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            ...(hfApiKey ? { 'Authorization': `Bearer ${hfApiKey}` } : {}),
          },
          signal: controller.signal,
          body: JSON.stringify({
            model: 'HuggingFaceH4/zephyr-7b-beta',
            messages: [
              { role: 'system', content: 'You are a content writer for Menshly Global. Write in a direct, no-nonsense voice with specific numbers, tool names, and prices. Write in Markdown with # headings. Start with a # heading immediately.' },
              { role: 'user', content: hfPrompt },
            ],
            max_tokens: 4000,
            temperature: 0.8,
          }),
        });
        clearTimeout(timeoutId);

        if (hfResp.ok) {
          const data = await hfResp.json();
          const candidate = data.choices?.[0]?.message?.content || '';

          debugInfo.huggingface = {
            elapsed: Date.now() - t0,
            length: candidate.length,
            valid: !!(candidate && isValidArticle(candidate)),
            firstChars: candidate.substring(0, 80),
          };

          if (candidate && isValidArticle(candidate)) {
            content = candidate;
            console.log('HuggingFace: article generated, length:', content.length);
          } else if (candidate.length > 300) {
            // Try extraction
            const extracted = extractArticleFromText(candidate);
            if (extracted) {
              content = extracted;
              console.log('HuggingFace: article extracted, length:', content.length);
            }
          }
        } else {
          const errText = await hfResp.text().catch(() => '');
          debugInfo.huggingface = { error: `HTTP ${hfResp.status}: ${errText.substring(0, 100)}` };
        }
      } catch (e) {
        const errType = e.name === 'AbortError' ? 'timeout' : e.message;
        debugInfo.huggingface = { error: errType };
      }
    }

    // ── Strategy 4: Cerebras fallback ──
    if (!content && context.env.CEREBRAS_API_KEY) {
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 20000);
        const t0 = Date.now();
        const cerebrasResp = await fetch('https://api.cerebras.ai/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${context.env.CEREBRAS_API_KEY}`,
          },
          signal: controller.signal,
          body: JSON.stringify({
            model: 'llama-3.3-70b',
            messages: fullMessages,
            max_tokens: 8000,
            temperature: 0.8,
            top_p: 0.95,
          }),
        });
        clearTimeout(timeoutId);
        if (cerebrasResp.ok) {
          const data = await cerebrasResp.json();
          const candidate = data.choices?.[0]?.message?.content || '';
          debugInfo.cerebras = { elapsed: Date.now() - t0, length: candidate.length, valid: isValidArticle(candidate) };
          if (isValidArticle(candidate)) content = candidate;
        } else {
          debugInfo.cerebras = { error: `HTTP ${cerebrasResp.status}` };
        }
      } catch (e) {
        debugInfo.cerebras = { error: e.message };
      }
    }

    // ── Strategy 5: DeepSeek fallback ──
    if (!content && context.env.DEEPSEEK_API_KEY) {
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 20000);
        const t0 = Date.now();
        const dsResp = await fetch('https://api.deepseek.com/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${context.env.DEEPSEEK_API_KEY}`,
          },
          signal: controller.signal,
          body: JSON.stringify({
            model: 'deepseek-chat',
            messages: fullMessages,
            max_tokens: 8000,
            temperature: 0.8,
          }),
        });
        clearTimeout(timeoutId);
        if (dsResp.ok) {
          const data = await dsResp.json();
          const candidate = data.choices?.[0]?.message?.content || '';
          debugInfo.deepseek = { elapsed: Date.now() - t0, length: candidate.length, valid: isValidArticle(candidate) };
          if (isValidArticle(candidate)) content = candidate;
        } else {
          debugInfo.deepseek = { error: `HTTP ${dsResp.status}` };
        }
      } catch (e) {
        debugInfo.deepseek = { error: e.message };
      }
    }

    if (!content) {
      return new Response(JSON.stringify({
        error: 'All AI services are currently unavailable. Please try again in a moment.',
        debug: debugInfo,
      }), { status: 503, headers });
    }

    const articleData = parseGeneratedContent(content, category);

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

// ═══════════════════════════════════════════════════════════════
// VALIDATION & EXTRACTION
// ═══════════════════════════════════════════════════════════════

function isValidArticle(text) {
  if (!text || text.length < 300) return false;
  
  // Check for reasoning/planning patterns
  const firstLines = text.split('\n').slice(0, 3).join(' ').trim();
  const planningPatterns = [
    /^(I need to|Need to|Let me|I should|I'll|I will|Let's craft|I must|I have to|We need to)/i,
    /^(The user wants|The instruction|The task is|Based on the|Following the|User wants)/i,
    /^(Title already|We can start|Then sections|Three blockquotes)/i,
  ];
  for (const pat of planningPatterns) {
    if (pat.test(firstLines)) return false;
  }
  
  // Must have at least one markdown heading (# )
  const hasHeadings = /^#{1,3}\s+/m.test(text);
  if (!hasHeadings) return false;
  
  // Must have substantial content after headings
  const contentLines = text.split('\n').filter(l => l.trim() && !l.trim().startsWith('#') && !l.trim().startsWith('---')).length;
  if (contentLines < 10) return false;
  
  return true;
}

// Extract article from text that may contain reasoning + article mixed together
function extractArticleFromText(text) {
  if (!text) return '';
  
  // Method 1: Code block extraction
  const codeBlockMatch = text.match(/```(?:markdown|md)?\s*\n([\s\S]*?)```/);
  if (codeBlockMatch && codeBlockMatch[1].trim().length > 200) {
    const extracted = codeBlockMatch[1].trim();
    if (/^#{1,3}\s+/.test(extracted)) return extracted;
  }
  
  // Method 2: Find the first # heading and extract everything from there
  const headingIdx = text.search(/\n#{1,3}\s+/);
  if (headingIdx !== -1) {
    let articleText = text.substring(headingIdx + 1);
    
    // Remove trailing reasoning patterns
    const trailingPatterns = [
      /\n(?:Now count|Let me count|I need to|Wait,|Actually,|Let's count|I'll count|Word count|I should|Let me check|We need to|Let's plan)[\s\S]*$/i,
      /\n\d+\s*words?\s*[\s\S]*$/i,
    ];
    for (const pat of trailingPatterns) {
      const match = articleText.match(pat);
      if (match) {
        articleText = articleText.substring(0, match.index);
      }
    }
    
    articleText = articleText.trim();
    
    if (articleText.length > 300 && isValidArticle(articleText)) {
      return articleText;
    }
    
    // Even if isValidArticle fails, check if there's enough real content
    const lines = articleText.split('\n');
    const articleLines = [];
    for (const line of lines) {
      const trimmed = line.trim();
      if (/^(We need|I need to|Need to|Let me|I should|I'll write|I'll include|Three blockquotes|Then sections)/i.test(trimmed)) {
        break;
      }
      articleLines.push(line);
    }
    const extracted = articleLines.join('\n').trim();
    if (extracted.length > 300 && /^#{1,3}\s+/.test(extracted)) {
      return extracted;
    }
  }
  
  // Method 3: Look for "Draft content:" or "Article:" markers
  const draftMarkers = ['Draft content:', 'Draft:', 'Article:', 'Here is the article:', "Here's the article:"];
  for (const marker of draftMarkers) {
    const idx = text.indexOf(marker);
    if (idx !== -1) {
      const after = text.substring(idx + marker.length).trim();
      const headingIdx2 = after.search(/^#{1,3}\s+/m);
      if (headingIdx2 !== -1) {
        let articleText = after.substring(headingIdx2);
        const reasoningStart = articleText.search(/\n(?:Now count|Let me count|I need to|Wait,|Actually,)/);
        if (reasoningStart !== -1) {
          articleText = articleText.substring(0, reasoningStart);
        }
        articleText = articleText.trim();
        if (articleText.length > 200) return articleText;
      }
    }
  }
  
  return '';
}

// ═══════════════════════════════════════════════════════════════
// PROMPT BUILDERS
// ═══════════════════════════════════════════════════════════════

function buildPollinationsMessages(category, topic, rev, difficulty) {
  // Concise prompts for Pollinations — shorter = more tokens for content
  if (category === 'opportunity') {
    return [
      { role: 'system', content: 'You are a content writer for Menshly Global. Write in a direct, no-nonsense voice. Use specific numbers, tool names, and prices. Write in Markdown with # headings, > blockquotes for truths/hacks, and tables. Start with a # heading immediately.' },
      { role: 'user', content: `Write an OPPORTUNITY article: "How to Start a ${topic} in 2026 (Build Once, Get Paid Forever)"

Revenue target: ${rev}/month | Difficulty: ${difficulty}

Include these sections:
## Why This Works Right Now (market data, trends)
## The Realistic Picture (3 ugly truths as > blockquotes)
## The Free Stack (3-4 free tools with descriptions)
## The Paid Stack (3-4 paid tools with costs, total monthly cost)
## The Workflow (3 steps with time estimates)
## Pricing Tiers (3 tiers: Starter, Growth, Premium)
## Hacks They Don't Share (2-3 > blockquotes)
## Revenue Projections (Markdown table: Month | Revenue | Clients)
## Start This Weekend (Sat AM, Sat PM, Sun actions)

Be specific with tool names and prices. No fluff. Write the COMPLETE article now.` }
    ];
  }

  if (category === 'intelligence') {
    return [
      { role: 'system', content: 'You are a content writer for Menshly Global. Write in a direct, no-nonsense voice. Use specific numbers, tool names, and prices. Write in Markdown with # headings, verification checkpoints, and tables. Start with a # heading immediately.' },
      { role: 'user', content: `Write an INTELLIGENCE guide: "Build and Scale a ${topic} with Automated Workflows"

Revenue target: ${rev}/month | Difficulty: ${difficulty}

Include these sections:
## Prerequisites (tools, costs, time needed, total upfront cost)
## Step 1: Setup (detailed walkthrough with tool names and URLs)
## Step 1 Check-In (3 verification items)
## Step 2: Core Workflow Build (configuration, error handling)
## Step 2 Check-In (verification items)
## Step 3: Production Pipeline (quality gates, scoring)
## Step 3 Check-In (verification items)
## Step 4: Monitoring & Delivery (automated reporting, alerts)
## Pricing Table (Markdown table: Tier | Monthly | Included | Cost | Margin)

Name every tool with its cost. Include verification checkpoints. Write the COMPLETE guide now.` }
    ];
  }

  if (category === 'playbook') {
    return [
      { role: 'system', content: 'You are a content writer for Menshly Global. Write in a direct, authoritative voice. Use specific numbers, tool names, and prices. Write in Markdown with # headings, procedures, and checkboxes. Start with a # heading immediately.' },
      { role: 'user', content: `Write a PLAYBOOK: "The ${topic} Playbook"

Revenue target: ${rev}/month | Difficulty: ${difficulty}

Include these modules:
## MODULE 1: Foundation (2 procedures with exact steps)
## MODULE 2: Tech Stack (tools, costs, total monthly cost)
## MODULE 3: Build Framework (2 procedures with code/config)
## MODULE 4: First Client (outreach script, demo script, pricing)
## MODULE 5: Delivery & Retention (SOPs, churn prevention)
## MODULE 6: Scaling (hiring roadmap, margin table: Clients | Revenue | Costs | Profit | Margin)

Every procedure starts with an action verb. Include exact tool configs. Write the COMPLETE playbook now.` }
    ];
  }

  return [
    { role: 'system', content: 'You are a content writer. Write in Markdown. Start with a # heading immediately.' },
    { role: 'user', content: `Write a complete article about: "${topic}". Include pricing, tools, and first steps. Be specific.` }
  ];
}

function buildFullMessages(category, topic, rev, difficulty, date) {
  const systemBase = 'You are a content strategist for Menshly Global. Write in a direct, no-nonsense voice. Use specific numbers, tool names, prices, and actionable steps. Write in Markdown. Use > blockquotes for "ugly truths" and "hacks". Be concise but thorough.';

  let userPrompt = '';
  if (category === 'opportunity') {
    userPrompt = `Write a comprehensive OPPORTUNITY article about: "${topic}"

Target revenue: ${rev}/month | Difficulty: ${difficulty} | Date: ${date}

Title: "How to Start a ${topic} in 2026 (Build Once, Get Paid Forever)"

Cover ALL sections: opening hook, why now, realistic picture (4 truths as blockquotes), free tools, paid tools with costs, workflow steps with time estimates, pricing tiers, hacks as blockquotes, revenue projection table, weekend action plan. Use specific tool names and prices. No placeholders.`;
  } else if (category === 'intelligence') {
    userPrompt = `Write a comprehensive INTELLIGENCE implementation guide about: "${topic}"

Target revenue: ${rev}/month | Difficulty: ${difficulty} | Date: ${date}

Title: "Build and Scale a ${topic} with Automated Workflows"

Cover ALL steps: prerequisites with costs, setup walkthrough, core workflow build, production pipeline, monitoring, pricing table. Include "Do you see X?" verification checkpoints. Name every tool with its cost. No placeholders.`;
  } else if (category === 'playbook') {
    userPrompt = `Write a comprehensive PLAYBOOK about: "${topic}"

Target revenue: ${rev}/month | Difficulty: ${difficulty} | Date: ${date}

Title: "The ${topic} Playbook"

Cover ALL modules: foundation with procedures, tech stack with costs, build framework, first client acquisition, delivery and retention SOPs, scaling with margin analysis. Include exact procedures and check-ins. No placeholders.`;
  } else {
    userPrompt = `Write a complete article about: "${topic}"`;
  }

  return [
    { role: 'system', content: systemBase },
    { role: 'user', content: userPrompt }
  ];
}

function buildHuggingFacePrompt(category, topic, rev, difficulty) {
  if (category === 'opportunity') {
    return `Write an OPPORTUNITY article: "How to Start a ${topic} in 2026 (Build Once, Get Paid Forever)"
Revenue target: ${rev}/month | Difficulty: ${difficulty}
Include sections: Why This Works Right Now, The Realistic Picture (3 ugly truths as blockquotes), The Free Stack, The Paid Stack with costs, The Workflow with time estimates, Pricing Tiers, Hacks as blockquotes, Revenue Projections table, Start This Weekend plan.
Be specific with tool names and prices. Write in Markdown with # headings. Start with a # heading immediately.`;
  }
  if (category === 'intelligence') {
    return `Write an INTELLIGENCE guide: "Build and Scale a ${topic} with Automated Workflows"
Revenue target: ${rev}/month | Difficulty: ${difficulty}
Include sections: Prerequisites with costs, Step-by-step setup, Core Workflow Build, Production Pipeline, Monitoring & Delivery, Pricing Table.
Name every tool with its cost. Write in Markdown with # headings. Start with a # heading immediately.`;
  }
  if (category === 'playbook') {
    return `Write a PLAYBOOK: "The ${topic} Playbook"
Revenue target: ${rev}/month | Difficulty: ${difficulty}
Include modules: Foundation with procedures, Tech Stack with costs, Build Framework, First Client acquisition, Delivery & Retention SOPs, Scaling with margin table.
Write in Markdown with # headings. Start with a # heading immediately.`;
  }
  return `Write a complete article about: "${topic}". Include pricing, tools, and first steps. Write in Markdown with # headings.`;
}

// ═══════════════════════════════════════════════════════════════
// IMAGE FETCHERS
// ═══════════════════════════════════════════════════════════════

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

// ═══════════════════════════════════════════════════════════════
// CONTENT PARSER
// ═══════════════════════════════════════════════════════════════

function parseGeneratedContent(content, category) {
  const titleMatch = content.match(/^#\s+(.+)$/m) || content.match(/^##?\s+(.+)$/m);
  const title = titleMatch ? titleMatch[1].replace(/\*\*/g, '').trim() : '';

  const lines = content.split('\n');
  let excerpt = '';
  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#') && !trimmed.startsWith('---') && !trimmed.startsWith('>') && trimmed.length > 50) {
      excerpt = trimmed.substring(0, 200).replace(/\*\*/g, '');
      break;
    }
  }

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
