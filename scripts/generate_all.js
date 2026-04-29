#!/usr/bin/env node
/**
 * Menshly Global — Full Article Generator
 * Generates 10 articles (5 pairs) using z-ai-web-dev-sdk
 * CRITICAL: max_tokens MUST NOT exceed 4000 per call
 */

import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { execSync } from 'child_process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const PROJECT_ROOT = path.resolve(__dirname, '..');

const MAX_TOKENS = 4000; // CRITICAL: Do NOT exceed this value

const ARTICLE_PAIRS = [
  {
    opp: {
      title: "How to Build an AI Chatbot Agency for E-Commerce in 2026 ($8K-25K/Month)",
      topic: "AI chatbot agency for e-commerce",
      slug: "ai-chatbot-ecommerce-agency-2026",
      context: "E-commerce stores are replacing human support with AI chatbots that sell, not just answer questions",
      affiliates: ["ChatGPT", "Make.com", "Shopify", "Replit", "Notion", "Zapier"],
      revenue: "$8K-25K/Month",
    },
    int: {
      title: "Build an AI Chatbot Agency for E-Commerce: The Complete Step-by-Step Guide",
      topic: "AI chatbot agency for e-commerce",
      slug: "build-ai-chatbot-ecommerce-agency",
      difficulty: "INTERMEDIATE",
      affiliates: ["ChatGPT", "Make.com", "Shopify", "Replit", "Notion", "Zapier"],
    }
  },
  {
    opp: {
      title: "How to Start an AI Lead Generation Agency in 2026 ($5K-20K/Month)",
      topic: "AI lead generation agency",
      slug: "ai-lead-generation-agency-2026",
      context: "B2B companies are desperate for qualified leads and AI can find, qualify, and nurture them automatically",
      affiliates: ["Apollo.io", "Make.com", "PhantomBuster", "Calendly", "ActiveCampaign", "Loom"],
      revenue: "$5K-20K/Month",
    },
    int: {
      title: "Build an AI Lead Generation Agency: The Complete Step-by-Step Guide",
      topic: "AI lead generation agency",
      slug: "build-ai-lead-generation-agency",
      difficulty: "INTERMEDIATE",
      affiliates: ["Apollo.io", "Make.com", "PhantomBuster", "Calendly", "ActiveCampaign", "Loom"],
    }
  },
  {
    opp: {
      title: "How to Launch an AI Social Media Agency in 2026 ($3K-15K/Month)",
      topic: "AI social media management agency",
      slug: "ai-social-media-agency-2026",
      context: "Brands need constant social content and AI can generate, schedule, and optimize it 24/7",
      affiliates: ["Canva", "Buffer", "ChatGPT", "Make.com", "Beehiiv", "Midjourney"],
      revenue: "$3K-15K/Month",
    },
    int: {
      title: "Build an AI Social Media Agency: The Complete Step-by-Step Guide",
      topic: "AI social media management agency",
      slug: "build-ai-social-media-agency",
      difficulty: "BEGINNER",
      affiliates: ["Canva", "Buffer", "ChatGPT", "Make.com", "Beehiiv", "Midjourney"],
    }
  },
  {
    opp: {
      title: "How to Build an AI Copywriting Agency in 2026 ($4K-18K/Month)",
      topic: "AI copywriting agency",
      slug: "ai-copywriting-agency-2026",
      context: "Every business needs copy — emails, ads, landing pages — and AI produces first drafts in seconds",
      affiliates: ["ChatGPT", "Grammarly", "Make.com", "Notion", "Semrush", "ActiveCampaign"],
      revenue: "$4K-18K/Month",
    },
    int: {
      title: "Build an AI Copywriting Agency: The Complete Step-by-Step Guide",
      topic: "AI copywriting agency",
      slug: "build-ai-copywriting-agency",
      difficulty: "BEGINNER",
      affiliates: ["ChatGPT", "Grammarly", "Make.com", "Notion", "Semrush", "ActiveCampaign"],
    }
  },
  {
    opp: {
      title: "How to Start a Faceless YouTube Channel Business with AI in 2026 ($2K-12K/Month)",
      topic: "AI faceless YouTube channel",
      slug: "faceless-youtube-channel-ai-2026",
      context: "Faceless YouTube channels powered by AI video generation are making creators thousands without showing their face",
      affiliates: ["Fliki AI", "ElevenLabs", "Canva", "ChatGPT", "Make.com", "Beehiiv"],
      revenue: "$2K-12K/Month",
    },
    int: {
      title: "Build a Faceless YouTube Channel Business with AI: The Complete Step-by-Step Guide",
      topic: "AI faceless YouTube channel",
      slug: "build-faceless-youtube-channel-ai",
      difficulty: "BEGINNER",
      affiliates: ["Fliki AI", "ElevenLabs", "Canva", "ChatGPT", "Make.com", "Beehiiv"],
    }
  },
];

const OPP_SYSTEM_PROMPT = `You are the lead writer for Menshly Global. Write in a casual, straight-talking voice — like a friend who's done this gives you the real playbook. No corporate jargon. No filler. Every sentence carries weight.

STYLE RULES:
- Talk to one person, not an audience
- Concrete numbers ("$2,500/month" not "good money")
- Name real tools with real prices
- Include tricks normally gated behind $497 courses
- Be honest about ugly truths
- Short punchy sentences. Then a longer one with nuance.
- NEVER "In today's rapidly evolving landscape"
- NEVER filler transitions
- Each section minimum 300 words`;

const INT_SYSTEM_PROMPT = `You are the technical implementation writer for Menshly Global. Write deep execution guides readers can follow step-by-step.

CRITICAL STYLE RULES:
- INSTRUCTIONAL, COMMANDING tone — senior operator handing a junior their playbook
- Every instruction SPECIFIC: exact button names, menu paths, settings, URLs
- INTERACTIVE CHECK-INS: "Do you see [X]? You should see [X] if you're in the right place."
- Show expected output at every step
- Include error scenarios: "If you see [ERROR], this means [CAUSE]. Fix it by [SOLUTION]."
- Name real tools with real prices and free tier limits
- Complete configurations — no guessing
- Never "configure it appropriately" — say EXACTLY what to configure
- Use TABLES for comparisons, cost breakdowns, pricing`;

async function callAI(messages) {
  const zai = await ZAI.create();
  const completion = await zai.chat.completions.create({
    messages,
    max_tokens: MAX_TOKENS,
    temperature: 0.75,
  });
  return completion.choices[0]?.message?.content || '';
}

function extractExcerpt(body, maxLen = 200) {
  const lines = body.split('\n');
  let paragraph = '';
  for (const line of lines) {
    const t = line.trim();
    if (t.startsWith('# ') && !t.startsWith('## ')) continue;
    if (t.startsWith('## ')) { if (paragraph) break; continue; }
    if (!t) { if (paragraph) break; continue; }
    paragraph += t.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') + ' ';
  }
  let e = paragraph.trim().substring(0, maxLen);
  if (paragraph.trim().length > maxLen) e += '...';
  return e.replace(/"/g, "'");
}

function stripH1(body) {
  let skipped = false;
  return body.split('\n').filter(line => {
    if (!skipped && line.trim().startsWith('# ') && !line.trim().startsWith('## ')) { skipped = true; return false; }
    return true;
  }).join('\n');
}

function wordCount(text) {
  return text.split(/\s+/).filter(w => w.length > 0).length;
}

async function generateOpp(pair, date) {
  const { opp, int: ip } = pair;
  console.log(`\n📝 OPP: ${opp.title}`);

  const userPrompt = `Write a complete deep-dive article: "${opp.title}"

TRENDING CONTEXT: ${opp.context}

AFFILIATE TOOLS TO MENTION NATURALLY (at least 5-6): ${opp.affiliates.join(', ')}

Follow this EXACT 12-section structure:
1. Opening hook (no heading) - 2-3 punchy paragraphs
2. ## Why This Works Right Now - 3 numbered reasons with data
3. ## The Realistic Picture (Before You Get Excited) - 4 truths as > **Truth #N:** blockquotes
4. ## The Free Stack: Starting With Zero Dollars - 6-8 tools with **Tool — $0** format
5. ## The Paid Stack: When You're Ready to Scale - 8-10 tools with **Tool — $X/mo** format
6. ## The Workflow: Step-by-Step With Every Shortcut - 3-4 steps as ### Step N: Name (time estimate)
7. ## Pricing: What to Charge and How to Defend It - 3 tiers
8. ## Getting Clients: The Real Playbook - 3 methods with conversion rates
9. ## Tricks and Hacks They Don't Share in Courses - 5 HACK blockquotes
10. ## The Real Numbers - Month-by-month revenue table
11. ## What Nobody Warns You About - 4-5 bold warnings
12. ## Start This Weekend (Literally) - Sat/Sun plan

Return pure Markdown (no front matter). Begin with 2-3 punchy opening paragraphs, then all sections.
WORD COUNT: 5,000-5,500 words minimum.`;

  // Pass 1: Opening + Why This Works + Realistic Picture + Free Stack
  console.log('  Pass 1/3: Opening + Why This Works + Realistic Picture + Free Stack');
  const pass1 = await callAI([
    { role: 'system', content: OPP_SYSTEM_PROMPT },
    { role: 'user', content: userPrompt + '\n\nWrite ONLY: the opening paragraphs (no heading), Why This Works Right Now, The Realistic Picture, and The Free Stack. Write at least 1800 words.' },
  ]);

  // Pass 2: Paid Stack + Workflow + Pricing
  console.log('  Pass 2/3: Paid Stack + Workflow + Pricing');
  const pass2 = await callAI([
    { role: 'system', content: OPP_SYSTEM_PROMPT },
    { role: 'user', content: userPrompt },
    { role: 'assistant', content: pass1 },
    { role: 'user', content: 'Continue with: The Paid Stack (8-10 tools), The Workflow (3-4 steps with time estimates), and Pricing (3 tiers). Do NOT repeat previous content. Write at least 1800 words.' },
  ]);

  // Pass 3: Getting Clients + Hacks + Real Numbers + Warnings + Weekend Plan
  console.log('  Pass 3/3: Getting Clients + Hacks + Numbers + Warnings + Weekend');
  const pass3 = await callAI([
    { role: 'system', content: OPP_SYSTEM_PROMPT },
    { role: 'user', content: userPrompt },
    { role: 'assistant', content: pass1 + '\n\n' + pass2 },
    { role: 'user', content: 'Continue with: Getting Clients (3 methods with conversion rates), Tricks and Hacks They Don\'t Share in Courses (5 HACK blockquotes), The Real Numbers (month-by-month revenue table with 12 rows), What Nobody Warns You About (4-5 bold warnings), and Start This Weekend (Sat/Sun plan). Do NOT repeat previous content. Write at least 1800 words.' },
  ]);

  let body = pass1 + '\n\n' + pass2 + '\n\n' + pass3;
  let wc = wordCount(body);
  console.log(`  After 3 passes: ${wc} words`);

  // Pass 4 if under 4000 words
  if (wc < 4500) {
    console.log('  Pass 4: Expanding...');
    const cont = await callAI([
      { role: 'system', content: OPP_SYSTEM_PROMPT },
      { role: 'user', content: userPrompt },
      { role: 'assistant', content: body },
      { role: 'user', content: `Current word count is ${wc}. You need at least 4500 words. Expand the thinnest sections with more detail, more examples, more specific numbers. Do NOT repeat. Write at least 1500 more words.` },
    ]);
    body += '\n\n' + cont;
    wc = wordCount(body);
    console.log(`  After pass 4: ${wc} words`);
  }

  const title = body.split('\n').find(l => l.startsWith('# ') && !l.startsWith('## '))?.replace(/^#+\s*/, '').trim().replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') || opp.title;
  const excerpt = extractExcerpt(body);
  const bodyClean = stripH1(body);

  const frontmatter = `---
title: "${title}"
date: ${date}
category: "AI Opportunity"
readTime: "16 MIN"
excerpt: "${excerpt}"
image: "/images/articles/opportunities/${opp.slug}.png"
heroImage: "/images/heroes/opportunities/${opp.slug}.png"
relatedGuide: "/intelligence/${ip.slug}/"
---

`;

  const dir = path.join(PROJECT_ROOT, 'content', 'opportunities');
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, `${opp.slug}.md`), frontmatter + bodyClean);

  console.log(`  ✅ Saved: ${opp.slug}.md (~${wc} words)`);
  return { slug: opp.slug, title, wordCount: wc, type: 'opportunity' };
}

async function generateInt(pair, date) {
  const { opp, int: ip } = pair;
  console.log(`\n📝 INT: ${ip.title}`);

  const userPrompt = `Write a complete step-by-step implementation article: "${ip.title}"

This is the IMPLEMENTATION companion to the opportunity article: "${opp.title}" (URL: /opportunities/${opp.slug}/)

Reference this opportunity in the opening paragraph.

AFFILIATE TOOLS TO MENTION NATURALLY (at least 5-6): ${ip.affiliates.join(', ')}
Difficulty: ${ip.difficulty}

Follow this EXACT structure:
1. Opening paragraph (1-2 sentences)
2. ## Prerequisites - accounts, URLs, costs, time
3. ## Step 1 through Step 8 - each with interactive check-ins, UI instructions, code blocks
4. ## Cost Breakdown - table
5. ## Production Checklist - 15-25 checkbox items
6. ## What to Do Next - 4-5 next steps

Each step must have:
- Interactive check-ins ("Do you see X? You should see X")
- Exact UI steps with button names, menu paths, settings
- Code blocks where applicable
- Error scenarios ("If you see ERROR, fix by SOLUTION")
- Expected output

Return pure Markdown (no front matter). Begin with title as H1.
WORD COUNT: 8,000-11,000 words minimum.`;

  // Pass 1: Opening + Prerequisites + Steps 1-3
  console.log('  Pass 1/3: Opening + Prerequisites + Steps 1-3');
  const pass1 = await callAI([
    { role: 'system', content: INT_SYSTEM_PROMPT },
    { role: 'user', content: userPrompt + '\n\nWrite ONLY: Opening paragraph, Prerequisites, Step 1, Step 2, and Step 3. Include interactive check-ins, exact UI instructions, code blocks. Write at least 2500 words.' },
  ]);

  // Pass 2: Steps 4-6
  console.log('  Pass 2/3: Steps 4-6');
  const pass2 = await callAI([
    { role: 'system', content: INT_SYSTEM_PROMPT },
    { role: 'user', content: userPrompt },
    { role: 'assistant', content: pass1 },
    { role: 'user', content: 'Continue with Step 4, Step 5, and Step 6. Include interactive check-ins, code blocks, exact configurations, and error scenarios. Do NOT repeat previous content. Write at least 2500 words.' },
  ]);

  // Pass 3: Steps 7-8 + Cost + Checklist + What Next
  console.log('  Pass 3/3: Steps 7-8 + Cost + Checklist + What Next');
  const pass3 = await callAI([
    { role: 'system', content: INT_SYSTEM_PROMPT },
    { role: 'user', content: userPrompt },
    { role: 'assistant', content: pass1 + '\n\n' + pass2 },
    { role: 'user', content: 'Continue with Step 7 (Automate with Make.com), Step 8 (Analytics and Optimization), Cost Breakdown (table with Tool | Free Tier | Paid Tier | When to Upgrade), Production Checklist (15-25 checkbox items as - [ ] Item), and What to Do Next (4-5 specific steps). Do NOT repeat. Write at least 2500 words.' },
  ]);

  let body = pass1 + '\n\n' + pass2 + '\n\n' + pass3;
  let wc = wordCount(body);
  console.log(`  After 3 passes: ${wc} words`);

  // Pass 4 if under 6000 words
  if (wc < 6000) {
    console.log('  Pass 4: Expanding...');
    const cont = await callAI([
      { role: 'system', content: INT_SYSTEM_PROMPT },
      { role: 'user', content: userPrompt },
      { role: 'assistant', content: body },
      { role: 'user', content: `Current word count is ${wc}. You need at least 6000 words. Expand the thinnest steps with more detail, more code blocks, more error scenarios, more interactive check-ins. Do NOT repeat. Write at least 2000 more words.` },
    ]);
    body += '\n\n' + cont;
    wc = wordCount(body);
    console.log(`  After pass 4: ${wc} words`);
  }

  // Pass 5 if still under 6000
  if (wc < 6000) {
    console.log('  Pass 5: Further expanding...');
    const cont = await callAI([
      { role: 'system', content: INT_SYSTEM_PROMPT },
      { role: 'user', content: userPrompt },
      { role: 'assistant', content: body },
      { role: 'user', content: `Still only ${wc} words. Need at least 6000. Expand Step 7 and Step 8 significantly with full Make.com scenario setup, exact automation configs, detailed analytics dashboards, A/B testing procedures. Add more Production Checklist items. Write at least 2000 more words.` },
    ]);
    body += '\n\n' + cont;
    wc = wordCount(body);
    console.log(`  After pass 5: ${wc} words`);
  }

  const title = body.split('\n').find(l => l.startsWith('# ') && !l.startsWith('## '))?.replace(/^#+\s*/, '').trim().replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') || ip.title;
  const excerpt = extractExcerpt(body, 250);
  const bodyClean = stripH1(body);

  const frontmatter = `---
title: "${title}"
date: ${date}
category: "Implementation"
difficulty: "${ip.difficulty}"
readTime: "28 MIN"
excerpt: "${excerpt}"
image: "/images/articles/intelligence/${ip.slug}.png"
heroImage: "/images/heroes/intelligence/${ip.slug}.png"
relatedOpportunity: "/opportunities/${opp.slug}/"
---

`;

  const dir = path.join(PROJECT_ROOT, 'content', 'intelligence');
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, `${ip.slug}.md`), frontmatter + bodyClean);

  console.log(`  ✅ Saved: ${ip.slug}.md (~${wc} words)`);
  return { slug: ip.slug, title, wordCount: wc, difficulty: ip.difficulty, type: 'intelligence' };
}

function generateImage(prompt, outputPath) {
  const dir = path.dirname(outputPath);
  fs.mkdirSync(dir, { recursive: true });
  try {
    execSync(`z-ai-generate --prompt "${prompt.replace(/"/g, '\\"')}" --output "${outputPath}" --size 1344x768`, {
      timeout: 120000,
      stdio: 'pipe',
    });
    return fs.existsSync(outputPath);
  } catch (e) {
    console.error(`  ⚠️ Image generation failed for ${outputPath}: ${e.message?.substring(0, 100)}`);
    return false;
  }
}

async function main() {
  console.log('🚀 Menshly Global — Full Article Generator');
  console.log(`   MAX_TOKENS per call: ${MAX_TOKENS}`);
  const date = '2026-04-27';
  const results = [];

  for (let i = 0; i < ARTICLE_PAIRS.length; i++) {
    const pair = ARTICLE_PAIRS[i];
    console.log(`\n${'='.repeat(60)}`);
    console.log(`PAIR ${i + 1}/${ARTICLE_PAIRS.length}: ${pair.opp.topic}`);
    console.log(`${'='.repeat(60)}`);

    try {
      // Generate Opportunity article
      const oppResult = await generateOpp(pair, date);
      results.push(oppResult);

      // Generate Intelligence article
      const intResult = await generateInt(pair, date);
      results.push(intResult);

      console.log(`\n✅ Pair ${i + 1} done! Opp: ${oppResult.wordCount}w | Int: ${intResult.wordCount}w`);
    } catch (e) {
      console.error(`❌ Pair ${i + 1} failed: ${e.message}`);
      console.error(e.stack);
    }

    // Cooldown between pairs
    if (i < ARTICLE_PAIRS.length - 1) {
      console.log('⏳ 5s cooldown...');
      await new Promise(r => setTimeout(r, 5000));
    }
  }

  // Generate images for all articles
  console.log('\n\n🎨 Generating images...');
  for (const pair of ARTICLE_PAIRS) {
    const { opp, int: ip } = pair;

    // Opp thumbnail
    const oppThumbPath = path.join(PROJECT_ROOT, 'static', 'images', 'articles', 'opportunities', `${opp.slug}.png`);
    console.log(`  📸 Opp thumbnail: ${opp.slug}.png`);
    generateImage(
      `Flat minimalist icon illustration of ${opp.topic}, strictly using ONLY white black and bright acid yellow #F9FF00 colors, solid white background, geometric brutalist style, no text`,
      oppThumbPath
    );

    // Opp hero
    const oppHeroPath = path.join(PROJECT_ROOT, 'static', 'images', 'heroes', 'opportunities', `${opp.slug}.png`);
    console.log(`  🖼️ Opp hero: ${opp.slug}.png`);
    generateImage(
      `Premium cinematic editorial hero image of ${opp.topic}, strictly using ONLY white black and bright acid yellow #F9FF00 colors, dramatic acid yellow accent lighting, Swiss brutalist editorial design, no text`,
      oppHeroPath
    );

    // Int thumbnail
    const intThumbPath = path.join(PROJECT_ROOT, 'static', 'images', 'articles', 'intelligence', `${ip.slug}.png`);
    console.log(`  📸 Int thumbnail: ${ip.slug}.png`);
    generateImage(
      `Flat minimalist icon illustration of building ${ip.topic} system, strictly using ONLY white black and bright acid yellow #F9FF00 colors, solid white background, geometric brutalist style, no text`,
      intThumbPath
    );

    // Int hero
    const intHeroPath = path.join(PROJECT_ROOT, 'static', 'images', 'heroes', 'intelligence', `${ip.slug}.png`);
    console.log(`  🖼️ Int hero: ${ip.slug}.png`);
    generateImage(
      `Premium cinematic editorial hero image of building ${ip.topic} implementation, strictly using ONLY white black and bright acid yellow #F9FF00 colors, dramatic acid yellow accent lighting, Swiss brutalist editorial design, no text`,
      intHeroPath
    );
  }

  // Final summary
  console.log('\n\n' + '='.repeat(60));
  console.log('📊 FINAL SUMMARY');
  console.log('='.repeat(60));

  const oppResults = results.filter(r => r.type === 'opportunity');
  const intResults = results.filter(r => r.type === 'intelligence');

  console.log('\nOpportunity Articles:');
  for (const r of oppResults) {
    const status = r.wordCount >= 4000 ? '✅' : '⚠️';
    console.log(`  ${status} ${r.slug} — ${r.wordCount} words`);
  }

  console.log('\nIntelligence Articles:');
  for (const r of intResults) {
    const status = r.wordCount >= 6000 ? '✅' : '⚠️';
    console.log(`  ${status} ${r.slug} — ${r.wordCount} words (${r.difficulty})`);
  }

  const totalWords = results.reduce((sum, r) => sum + r.wordCount, 0);
  console.log(`\nTotal words generated: ${totalWords}`);
  console.log(`Total articles: ${results.length}`);
}

main().catch(e => { console.error('Fatal:', e); process.exit(1); });
