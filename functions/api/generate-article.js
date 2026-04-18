/**
 * Cloudflare Pages Function: AI Content Generator
 * Generates reviews, analysis, guides, and opinions using AI.
 * Fetches relevant images from Pexels automatically.
 *
 * Configure via Cloudflare Pages Environment Variables:
 *   AI_API_KEY     - AI API key (e.g., Cerebras, Groq, OpenAI)
 *   AI_API_BASE    - API base URL (default: https://api.cerebras.ai/v1)
 *   AI_MODEL       - Model name (default: auto-detect)
 *   PEXELS_API_KEY - Pexels API key for auto images
 */

export async function onRequestPost(context) {
  try {
    const { topic, category, tone, length } = await context.request.json();

    if (!topic || topic.trim().length < 3) {
      return jsonResponse({ error: 'Please provide a topic (at least 3 characters)' }, 400);
    }

    const rawKey = context.env.AI_API_KEY || '';
    const apiBase = (context.env.AI_API_BASE || 'https://api.cerebras.ai/v1').replace(/\/+$/, '');
    const configuredModel = context.env.AI_MODEL || '';
    const pexelsKey = context.env.PEXELS_API_KEY || '';

    if (!rawKey) {
      return jsonResponse({
        error: 'AI API key not configured. Set AI_API_KEY in Cloudflare Pages environment variables.',
        hint: 'Go to Cloudflare Dashboard > Pages > your site > Settings > Environment variables'
      }, 503);
    }

    /* Strip invisible Unicode chars that break auth (same as Python script) */
    const apiKey = rawKey.replace(/[\u200b-\u200f\u2028-\u202e\ufeff\u00ad]/g, '').trim();

    /* === Auto-detect model — skip if API key looks wrong === */
    let model = configuredModel;
    if (!model) {
      model = await autoDetectModel(apiKey, apiBase);
      if (!model) model = 'llama-3.3-70b';
    }

    /* === Category Map === */
    const categoryMap = {
      'film-review': 'Film & TV Review',
      'entertainment': 'Arts & Culture',
      'personal-finance': 'Personal Finance',
      'market-analysis': 'Market Analysis',
      'business-strategy': 'Business Strategy',
      'technology': 'Tech & Innovation',
      'commentary': 'Expert Commentary'
    };

    /* === Tone/Style Map === */
    const toneMap = {
      'review': 'detailed review with clear verdict, pros/cons, and rating',
      'analysis': 'in-depth analytical breakdown with data-driven insights',
      'guide': 'practical how-to guide with actionable steps',
      'opinion': 'thought-provoking opinion editorial with strong perspective',
      'listicle': 'engaging numbered list/ranking format with short punchy entries',
      'feature': 'engaging long-form feature with storytelling'
    };

    const lengthMap = {
      'short': '300-400 words',
      'medium': '600-800 words',
      'long': '1200-1500 words'
    };

    const catLabel = categoryMap[category] || 'Analysis';
    const toneLabel = toneMap[tone] || 'informative analysis style';
    const lengthLabel = lengthMap[length] || '600-800 words';

    /* === System Prompt === */
    const systemPrompt = `You are a content creator for MenshlyGlobal, a premium international media platform. You write ONLY the following types of content: reviews, analysis, opinions, guides, and commentary. You NEVER write breaking news, factual news reporting, or time-sensitive news articles.

CRITICAL RULES:
- Write in ${toneLabel} style
- Target length: ${lengthLabel}
- Category: ${catLabel}
- This is an OPINION/REVIEW piece, not a news article
- Include a compelling, SEO-friendly headline (max 15 words)
- Include a 1-2 sentence summary/standfirst
- Use subheadings for structure
- For movie reviews: include a rating out of 10, pros/cons, and final verdict
- For money ideas: include estimated startup costs, difficulty level, and income potential
- For business stats: include relevant data points, percentages, and trends
- For guides: include numbered steps, tips, and common mistakes to avoid
- Be specific — use concrete examples, numbers, and real-world references
- Never claim to report facts that need verification — this is analysis/opinion only
- End with a clear conclusion or actionable takeaway

FORMAT: Return a JSON object with these keys:
  "title" (string) — the headline
  "summary" (string) — 1-2 sentence standfirst
  "category" (string) — the category label
  "content" (string) — the article body in HTML using <h2>, <p>, <blockquote>, <ul>, <li> tags`;

    const userPrompt = `Write a ${catLabel} piece about: "${topic}"`;

    /* === Call AI API — try with JSON mode first, fallback to plain === */
    let rawContent = null;
    let usedJsonMode = false;

    // Attempt 1: With response_format: json_object
    try {
      const aiResponse = await fetch(apiBase + '/chat/completions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + apiKey
        },
        body: JSON.stringify({
          model: model,
          messages: [
            { role: 'system', content: systemPrompt },
            { role: 'user', content: userPrompt }
          ],
          max_tokens: 3000,
          temperature: 0.75,
          response_format: { type: 'json_object' }
        })
      });

      if (aiResponse.ok) {
        const aiData = await aiResponse.json();
        rawContent = aiData.choices?.[0]?.message?.content;
        if (rawContent) usedJsonMode = true;
      } else {
        // JSON mode not supported by this model — try without
        const errText = await aiResponse.text();
        console.log('JSON mode failed:', aiResponse.status, errText.substring(0, 200));
      }
    } catch (e) {
      console.log('JSON mode error:', e.message);
    }

    // Attempt 2: Without response_format (plain text mode)
    if (!rawContent) {
      try {
        const aiResponse = await fetch(apiBase + '/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + apiKey
          },
          body: JSON.stringify({
            model: model,
            messages: [
              { role: 'system', content: systemPrompt },
              { role: 'user', content: userPrompt }
            ],
            max_tokens: 3000,
            temperature: 0.75
          })
        });

        if (!aiResponse.ok) {
          const errText = await aiResponse.text();
          let errMsg = 'AI API returned status ' + aiResponse.status;
          try {
            const errJson = JSON.parse(errText);
            errMsg = errJson.error?.message || errJson.message || errMsg;
          } catch (e) {}
          // If 401, add helpful hint
          if (aiResponse.status === 401) {
            errMsg += '. Check that AI_API_KEY is correct in Cloudflare env vars.';
          }
          return jsonResponse({ error: errMsg }, 500);
        }

        const aiData = await aiResponse.json();
        rawContent = aiData.choices?.[0]?.message?.content;
      } catch (e) {
        return jsonResponse({ error: 'Failed to reach AI API: ' + e.message }, 500);
      }
    }

    if (!rawContent) {
      return jsonResponse({ error: 'AI returned empty response. Try a different topic.' }, 500);
    }

    /* === Parse response — handle multiple formats === */
    let article = parseAiResponse(rawContent, topic, catLabel);

    article.id = 'ai-' + Date.now();
    article.topic = topic;
    article.tone = tone;
    article.category = catLabel;
    article.generatedAt = new Date().toISOString();
    article.readTime = Math.max(2, Math.ceil((article.content || '').split(/\s+/).length / 200));

    /* === Fetch Image from Pexels === */
    if (pexelsKey) {
      try {
        const searchQuery = buildImageQuery(topic, category);
        const imgResponse = await fetch('https://api.pexels.com/v1/search?query=' + encodeURIComponent(searchQuery) + '&per_page=1&orientation=landscape', {
          headers: { 'Authorization': pexelsKey }
        });
        if (imgResponse.ok) {
          const imgData = await imgResponse.json();
          if (imgData.photos && imgData.photos.length > 0) {
            const photo = imgData.photos[0];
            article.image = photo.src.large;
            article.imageThumb = photo.src.medium;
            article.imageCredit = photo.photographer;
            article.imageLink = photo.photographer_url;
          }
        }
      } catch (imgErr) {
        // Image fetch failed — article is still valid
      }
    }

    return jsonResponse(article, 200);

  } catch (err) {
    return jsonResponse({ error: 'Server error: ' + (err.message || 'Unknown error') }, 500);
  }
}

/* === Response Parser — handles JSON, code blocks, and plain markdown === */
function parseAiResponse(raw, topic, catLabel) {
  // Format 1: Clean JSON
  try {
    const parsed = JSON.parse(raw);
    if (parsed.title && parsed.content && parsed.content.length >= 100) {
      return parsed;
    }
  } catch (e) {}

  // Format 2: JSON wrapped in markdown code block
  const codeBlockMatch = raw.match(/```(?:json)?\s*(\{[\s\S]*?\})\s*```/);
  if (codeBlockMatch) {
    try {
      const parsed = JSON.parse(codeBlockMatch[1]);
      if (parsed.title && parsed.content && parsed.content.length >= 100) {
        return parsed;
      }
    } catch (e) {}
  }

  // Format 3: JSON with escaped content field (nested markdown)
  try {
    const parsed = JSON.parse(raw);
    const nested = parsed.content;
    if (nested) {
      const cleaned = nested.trim().replace(/^["']|["']$/g, '');
      if (cleaned.length >= 200) {
        return {
          title: parsed.title || topic,
          summary: parsed.summary || cleaned.substring(0, 200),
          category: parsed.category || catLabel,
          content: ensureHtml(cleaned)
        };
      }
    }
  } catch (e) {}

  // Format 4: Plain markdown response
  const cleaned = raw.trim().replace(/^```\w*\s*/, '').replace(/\s*```$/, '');
  if (cleaned.length >= 200) {
    const lines = cleaned.split('\n');
    const summaryLines = [];
    let bodyStart = 0;
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];
      if (line.startsWith('## ') || line.startsWith('# ')) {
        bodyStart = i;
        break;
      }
      if (line.trim()) summaryLines.push(line);
    }
    const summary = summaryLines.join(' ').substring(0, 300);
    const body = bodyStart > 0 ? lines.slice(bodyStart).join('\n') : cleaned;

    return {
      title: extractTitle(lines, topic),
      summary: summary || topic,
      category: catLabel,
      content: ensureHtml(body)
    };
  }

  // Format 5: Last resort — just wrap it
  return {
    title: topic,
    summary: raw.substring(0, 200),
    category: catLabel,
    content: '<p>' + raw.replace(/\n\n/g, '</p><p>').replace(/\n/g, '<br>') + '</p>'
  };
}

/* Extract title from first heading or first meaningful line */
function extractTitle(lines, fallback) {
  for (const line of lines) {
    const match = line.match(/^#{1,3}\s+(.+)/);
    if (match) return match[1].trim();
  }
  return fallback;
}

/* Ensure content has HTML tags (convert basic markdown) */
function ensureHtml(text) {
  if (!text) return '';
  // If it already has HTML tags, return as-is
  if (/<h[1-6]|<p|<div|<br/i.test(text)) return text;
  // Convert markdown to HTML
  let html = text;
  html = html.replace(/^### (.+)$/gm, '<h3>$1</h3>');
  html = html.replace(/^## (.+)$/gm, '<h2>$1</h2>');
  html = html.replace(/^# (.+)$/gm, '<h2>$1</h2>');
  html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');
  html = html.replace(/^> (.+)$/gm, '<blockquote>$1</blockquote>');
  html = html.replace(/^[-*] (.+)$/gm, '<li>$1</li>');
  html = html.replace(/\n\n/g, '</p><p>');
  html = '<p>' + html + '</p>';
  html = html.replace(/<p>\s*<\/p>/g, '');
  html = html.replace(/<p>\s*(<h[23]>)/g, '$1');
  html = html.replace(/(<\/h[23]>)\s*<\/p>/g, '$1');
  return html;
}

/* === Auto-detect best model === */
const MODEL_PREFERENCES = [
  'llama-3.3-70b',
  'llama3.1-8b',
  'deepseek-r1-distill-llama-70b',
  'qwen-3-235b-a22b-instruct-2507'
];

async function autoDetectModel(apiKey, apiBase) {
  try {
    const resp = await fetch(apiBase + '/models', {
      headers: {
        'Authorization': 'Bearer ' + apiKey,
        'User-Agent': 'MenshlyGlobal/1.0'
      }
    });
    if (!resp.ok) return null;
    const data = await resp.json();
    const available = (data.data || []).map(m => m.id);
    console.log('Available models:', available.join(', '));

    for (const pref of MODEL_PREFERENCES) {
      if (available.includes(pref)) return pref;
    }
    return available[0] || null;
  } catch (e) {
    console.log('Model detection failed:', e.message);
    return null;
  }
}

/* Build a search query for Pexels based on topic + category */
function buildImageQuery(topic, category) {
  const categoryKeywords = {
    'film-review': 'cinema movie film',
    'entertainment': 'entertainment culture music',
    'personal-finance': 'finance money business',
    'market-analysis': 'business charts data analytics',
    'business-strategy': 'business office corporate',
    'technology': 'technology digital innovation',
    'commentary': 'analysis thought leadership'
  };
  const prefix = categoryKeywords[category] || 'media';
  const topicWords = topic.split(/\s+/).slice(0, 4).join(' ');
  return prefix + ' ' + topicWords;
}

/* Handle CORS preflight */
export async function onRequestOptions() {
  return new Response(null, {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type'
    }
  });
}

/* === Helpers === */
function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' }
  });
}
