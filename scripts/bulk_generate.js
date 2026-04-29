#!/usr/bin/env node
/**
 * Menshly Global — Content-Only Bulk Generator
 * Generates article TEXT using z-ai-web-dev-sdk
 * Images are generated separately via the existing Python scripts
 */

import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const PROJECT_ROOT = path.resolve(__dirname, '..');

const ARTICLE_PAIRS = [
  {
    opp: {
      title: "How to Build an AI Chatbot Agency for E-Commerce in 2026 ($8K-25K/Month)",
      topic: "AI chatbot agency for e-commerce",
      slug: "ai-chatbot-ecommerce-agency-2026",
      context: "E-commerce stores are replacing human support with AI chatbots that sell, not just answer questions",
      affiliates: ["ChatGPT", "Make.com", "Shopify", "Replit", "Notion", "Zapier"],
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

const OPP_SYSTEM_PROMPT = `You are the lead writer for Menshly Global (tagline: "Where AI Meets Revenue").
You write in a casual, human, straight-talking voice — like a friend who's actually done this stuff is giving you the real playbook over coffee. No corporate jargon. No AI-sounding filler. Every sentence must carry weight. No fluff.

WRITING STYLE RULES:
- Write like you're talking to one person, not an audience
- Use concrete numbers, not vague claims ("$2,500/month" not "good money")
- Name real tools with real prices
- Include tricks and shortcuts people normally gate behind $497 courses
- Be honest about ugly truths
- Short punchy sentences. Then a longer one that explains the nuance.
- NEVER "In today's rapidly evolving landscape" or "As we look to the future"
- NEVER write filler transitions
- Each section must be substantial (minimum 300 words)

ARTICLE STRUCTURE (follow EXACTLY):

Start with 2-3 punchy opening paragraphs with shocking numbers. No heading for this.

## Why This Works Right Now
3 numbered reasons with bold headers and data.

## The Realistic Picture (Before You Get Excited)
4 ugly truths as blockquotes:
> **Truth #1:** [harsh reality with numbers]

## The Free Stack: Starting With Zero Dollars
6-8 free tools: **Tool Name — $0** — Description. Include HACK blockquote.

## The Paid Stack: When You're Ready to Scale
8-10 paid tools: **Tool Name — $X/mo** — Description. Total cost. Include HACK blockquote.

## The Workflow: Step-by-Step With Every Shortcut
3-4 steps (### Step N: Name (time estimate)). Each with detail + HACK blockquote.

## Pricing: What to Charge and How to Defend It
3 tiers (Starter/Growth/Enterprise). Pricing Trick HACK blockquote.

## Getting Clients: The Real Playbook
3 methods (### Method N: Name (Conversion Rate: X%)). Specific tactics.

## Tricks and Hacks They Don't Share in Courses
5 hacks as blockquotes:
> **HACK 1: Name.** Explanation.

## The Real Numbers
Month-by-month revenue table:
| Month | Revenue | Clients/Users | Notes |
8-12 rows. Unit economics paragraph.

## What Nobody Warns You About
4-5 bold-titled warnings.

## Start This Weekend (Literally)
Sat morning / Sat afternoon / Sunday plan with copy-paste pitch.

WORD COUNT: 5,000-5,500 words. Do NOT cut sections short.`;

const INT_SYSTEM_PROMPT = `You are the technical implementation writer for Menshly Global (tagline: "Where AI Meets Revenue").
You write deep execution guides that readers can follow step-by-step to build real systems.

CRITICAL STYLE RULES:
- INSTRUCTIONAL, COMMANDING tone — senior operator handing a junior their playbook
- Every instruction SPECIFIC: exact button names, menu paths, settings, URLs
- INTERACTIVE CHECK-INS throughout: "Do you see [X]? You should see [X] if you're in the right place."
- Show expected output at every step
- Include error scenarios: "If you see [ERROR], this means [CAUSE]. Fix it by [SOLUTION]."
- Name real tools with real prices and free tier limits
- Complete configurations — readers follow along without guessing
- Never "configure it appropriately" — say EXACTLY what to configure
- Use TABLES for comparisons, cost breakdowns, pricing tiers

ARTICLE STRUCTURE (follow EXACTLY):

Opening paragraph: 1-2 direct sentences about what you'll build.

## Prerequisites
Required accounts with URLs, costs. Optional upgrades. Total cost. Time commitment.

## Step 1: [Setup/Configure]
Account setup, API keys, configuration. Interactive check-in.

## Step 2: [Build Core Component]
Main implementation. Complete configurations. Interactive check-in.

## Step 3: [Test and Validate]
Verify it works. Test commands. Common errors. Interactive check-in.

## Step 4: [Add Advanced Feature]
Production-worthy enhancement. Interactive check-in.

## Step 5: [Deploy to Production OR Price and Sell]
Deployment steps or pricing table.

## Step 6: [Scale/Grow]
1 to 10+ clients.

## Step 7: [Automate with Make.com]
Full Make.com scenario setup.

## Step 8: [Analytics and Optimization]
KPIs, A/B testing, continuous improvement.

## Cost Breakdown
Table: Tool | Free Tier | Paid Tier | When to Upgrade

## Production Checklist
15-25 items: - [ ] Item

## What to Do Next
4-5 specific next steps.

WORD COUNT: 8,000-11,000 words. Every step FULLY DETAILED.`;

async function callAI(messages, maxTokens = 8000) {
  const zai = await ZAI.create();
  const completion = await zai.chat.completions.create({
    messages,
    max_tokens: maxTokens,
    temperature: 0.75,
  });
  return completion.choices[0]?.message?.content || '';
}

function extractExcerpt(body, maxLen = 200) {
  const lines = body.split('\n');
  let paragraph = '';
  for (const line of lines) {
    const t = line.trim();
    if (t.startsWith('# ')) continue;
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

async function generateOpp(pair, date) {
  const { opp, int: ip } = pair;
  console.log(`\n📝 OPP: ${opp.title}`);

  const userPrompt = `Write a complete deep-dive article about: ${opp.title}\n\nTRENDING CONTEXT: ${opp.context}\n\nAFFILIATE TOOLS TO MENTION NATURALLY (at least 5-6): ${opp.affiliates.join(', ')}\n\nFollow the EXACT 12-section structure in your system instructions. Return pure Markdown (no front matter). Begin with 2-3 punchy opening paragraphs, then all 12 sections.\n\nWORD COUNT: 5,000-5,500 words minimum.`;

  // Pass 1: Opening + Why This Works + Realistic Picture + Free Stack
  const pass1 = await callAI([
    { role: 'system', content: OPP_SYSTEM_PROMPT },
    { role: 'user', content: userPrompt + '\n\nWrite ONLY these sections: the opening paragraphs, Why This Works Right Now, The Realistic Picture, and The Free Stack. Write at least 2000 words.' },
  ], 8000);

  // Pass 2: Paid Stack + Workflow + Pricing
  const pass2 = await callAI([
    { role: 'system', content: OPP_SYSTEM_PROMPT },
    { role: 'user', content: userPrompt },
    { role: 'assistant', content: pass1 },
    { role: 'user', content: 'Continue with: The Paid Stack, The Workflow (all steps), and Pricing sections. Do NOT repeat previous content. Write at least 2000 words.' },
  ], 8000);

  // Pass 3: Getting Clients + Hacks + Real Numbers + Warnings + Weekend Plan
  const pass3 = await callAI([
    { role: 'system', content: OPP_SYSTEM_PROMPT },
    { role: 'user', content: userPrompt },
    { role: 'assistant', content: pass1 + '\n\n' + pass2 },
    { role: 'user', content: 'Continue with: Getting Clients, Tricks and Hacks, The Real Numbers (month-by-month table), What Nobody Warns You About, and Start This Weekend. Do NOT repeat. Write at least 2000 words.' },
  ], 8000);

  let body = pass1 + '\n\n' + pass2 + '\n\n' + pass3;
  let wc = body.split(/\s+/).length;
  console.log(`  After 3 passes: ${wc} words`);

  if (wc < 4000) {
    const cont = await callAI([
      { role: 'system', content: OPP_SYSTEM_PROMPT },
      { role: 'user', content: userPrompt },
      { role: 'assistant', content: body },
      { role: 'user', content: 'Continue from where you left off. Do NOT repeat. Complete ALL remaining sections. Write at least 1500 more words.' },
    ], 8000);
    body += '\n\n' + cont;
    wc = body.split(/\s+/).length;
    console.log(`  Pass 2: ${wc} words`);
  }

  const title = body.split('\n').find(l => l.startsWith('# ') && !l.startsWith('## '))?.replace(/^#+\s*/, '').trim().replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') || opp.title;
  const excerpt = extractExcerpt(body);
  const bodyClean = stripH1(body);
  const readTime = `${16 + Math.floor(Math.random() * 8)} MIN`;

  const frontmatter = `---\ntitle: "${title}"\ndate: ${date}\ncategory: "AI Opportunity"\nreadTime: "${readTime}"\nexcerpt: "${excerpt}"\nimage: "/images/articles/opportunities/${opp.slug}.png"\nheroImage: "/images/heroes/opportunities/${opp.slug}.png"\nrelatedGuide: "/intelligence/${ip.slug}/"\n---\n\n`;

  const dir = path.join(PROJECT_ROOT, 'content', 'opportunities');
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, `${opp.slug}.md`), frontmatter + bodyClean);

  console.log(`  ✅ Saved: ${opp.slug}.md (~${wc} words)`);
  return { slug: opp.slug, title, wordCount: wc };
}

async function generateInt(pair, oppData, date) {
  const { opp, int: ip } = pair;
  console.log(`\n📝 INT: ${ip.title}`);

  const userPrompt = `Write a complete step-by-step implementation article about: ${ip.title}\n\nThis is the IMPLEMENTATION companion to the opportunity article: "${opp.title}" (URL: /opportunities/${opp.slug}/)\n\nReference this opportunity in the opening paragraph.\n\nAFFILIATE TOOLS TO MENTION NATURALLY (at least 5-6): ${ip.affiliates.join(', ')}\nDifficulty: ${ip.difficulty}\n\nFollow the EXACT structure: Prerequisites, Steps 1-8, Cost Breakdown, Production Checklist, What to Do Next. Every step with interactive check-ins, exact UI steps, code blocks, error scenarios.\n\nReturn pure Markdown (no front matter). Begin with title as H1.\n\nWORD COUNT: 8,000-11,000 words minimum.`;

  // Pass 1: Opening + Prerequisites + Steps 1-3
  const pass1 = await callAI([
    { role: 'system', content: INT_SYSTEM_PROMPT },
    { role: 'user', content: userPrompt + '\n\nWrite ONLY: Opening paragraph, Prerequisites, Step 1, Step 2, and Step 3. Include interactive check-ins. Write at least 3000 words.' },
  ], 8000);

  // Pass 2: Steps 4-6
  const pass2 = await callAI([
    { role: 'system', content: INT_SYSTEM_PROMPT },
    { role: 'user', content: userPrompt },
    { role: 'assistant', content: pass1 },
    { role: 'user', content: 'Continue with Step 4, Step 5, and Step 6. Include interactive check-ins, code blocks, and error scenarios. Do NOT repeat previous content. Write at least 2500 words.' },
  ], 8000);

  // Pass 3: Steps 7-8 + Cost Breakdown + Checklist + What Next
  const pass3 = await callAI([
    { role: 'system', content: INT_SYSTEM_PROMPT },
    { role: 'user', content: userPrompt },
    { role: 'assistant', content: pass1 + '\n\n' + pass2 },
    { role: 'user', content: 'Continue with Step 7 (Automate with Make.com), Step 8 (Analytics), Cost Breakdown table, Production Checklist (15-25 items), and What to Do Next. Do NOT repeat. Write at least 2500 words.' },
  ], 8000);

  let body = pass1 + '\n\n' + pass2 + '\n\n' + pass3;
  let wc = body.split(/\s+/).length;
  console.log(`  After 3 passes: ${wc} words`);

  if (wc < 6000) {
    const cont = await callAI([
      { role: 'system', content: INT_SYSTEM_PROMPT },
      { role: 'user', content: userPrompt },
      { role: 'assistant', content: body },
      { role: 'user', content: `Continue. Current: ${wc} words. Complete ALL remaining sections with full detail. Write at least 2000 more words.` },
    ], 8000);
    body += '\n\n' + cont;
    wc = body.split(/\s+/).length;
    console.log(`  Pass 4: ${wc} words`);
  }

  const title = body.split('\n').find(l => l.startsWith('# ') && !l.startsWith('## '))?.replace(/^#+\s*/, '').trim().replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') || ip.title;
  const excerpt = extractExcerpt(body, 250);
  const bodyClean = stripH1(body);

  const frontmatter = `---\ntitle: "${title}"\ndate: ${date}\ncategory: "Implementation"\ndifficulty: "${ip.difficulty}"\nreadTime: "28 MIN"\nexcerpt: "${excerpt}"\nimage: "/images/articles/intelligence/${ip.slug}.png"\nheroImage: "/images/heroes/intelligence/${ip.slug}.png"\nrelatedOpportunity: "/opportunities/${opp.slug}/"\n---\n\n`;

  const dir = path.join(PROJECT_ROOT, 'content', 'intelligence');
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, `${ip.slug}.md`), frontmatter + bodyClean);

  console.log(`  ✅ Saved: ${ip.slug}.md (~${wc} words)`);
  return { slug: ip.slug, title, wordCount: wc, difficulty: ip.difficulty };
}

async function main() {
  console.log('🚀 Menshly Global — Content Generator');
  const date = '2026-04-27';
  const results = { opp: [], int: [] };

  for (let i = 0; i < ARTICLE_PAIRS.length; i++) {
    const pair = ARTICLE_PAIRS[i];
    console.log(`\n${'#'.repeat(50)}\nPAIR ${i+1}/${ARTICLE_PAIRS.length}\n${'#'.repeat(50)}`);

    try {
      const oppResult = await generateOpp(pair, date);
      results.opp.push(oppResult);

      const intResult = await generateInt(pair, oppResult, date);
      results.int.push(intResult);

      console.log(`\n✅ Pair ${i+1} done! Opp: ${oppResult.wordCount}w | Int: ${intResult.wordCount}w`);
    } catch (e) {
      console.error(`❌ Pair ${i+1} failed: ${e.message}`);
    }

    if (i < ARTICLE_PAIRS.length - 1) {
      console.log('⏳ 5s cooldown...');
      await new Promise(r => setTimeout(r, 5000));
    }
  }

  // Update last_generated.json
  const dataDir = path.join(PROJECT_ROOT, 'data');
  fs.mkdirSync(dataDir, { recursive: true });
  const lgPath = path.join(dataDir, 'last_generated.json');
  let lg = {};
  try { lg = JSON.parse(fs.readFileSync(lgPath, 'utf8')); } catch {}

  if (results.opp.length > 0) {
    const lo = results.opp[results.opp.length - 1];
    const lp = ARTICLE_PAIRS[ARTICLE_PAIRS.length - 1];
    lg.last_opportunity = { slug: lo.slug, title: lo.title, topic: lp.opp.topic, context: lp.opp.context, affiliates: lp.opp.affiliates, intelligence_angle: lp.int.title, playbook_angle: `Build, Scale, and Monetize ${lp.opp.topic} with Make.com`, generated_at: new Date().toISOString() };
  }
  if (results.int.length > 0) {
    const li = results.int[results.int.length - 1];
    lg.last_intelligence = { slug: li.slug, title: li.title, difficulty: li.difficulty, topic: ARTICLE_PAIRS[ARTICLE_PAIRS.length - 1].int.topic, generated_at: new Date().toISOString() };
  }
  fs.writeFileSync(lgPath, JSON.stringify(lg, null, 2));

  console.log('\n\n📊 SUMMARY');
  console.log('Opportunity Articles:');
  for (const r of results.opp) console.log(`  ✅ ${r.slug} — ~${r.wordCount} words`);
  console.log('Intelligence Articles:');
  for (const r of results.int) console.log(`  ✅ ${r.slug} — ~${r.wordCount} words`);
}

main().catch(e => { console.error('Fatal:', e); process.exit(1); });
