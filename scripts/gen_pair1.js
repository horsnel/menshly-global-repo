#!/usr/bin/env node
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const PROJECT_ROOT = path.resolve(__dirname, '..');
const MAX_TOKENS = 4000;

const pair = {
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
};

const OPP_SYS = `You are the lead writer for Menshly Global. Write in a casual, straight-talking voice — like a friend who's done this gives you the real playbook. No corporate jargon. No filler. Every sentence carries weight. Short punchy sentences then longer ones with nuance. Concrete numbers. Name real tools with real prices. Be honest about ugly truths.`;

const INT_SYS = `You are the technical implementation writer for Menshly Global. Write deep execution guides readers can follow step-by-step. INSTRUCTIONAL COMMANDING tone. Every instruction SPECIFIC: exact button names, menu paths, settings. INTERACTIVE CHECK-INS. Show expected output. Include error scenarios. Name real tools with real prices. Complete configurations. Use TABLES for comparisons.`;

async function callAI(messages) {
  const zai = await ZAI.create();
  const c = await zai.chat.completions.create({ messages, max_tokens: MAX_TOKENS, temperature: 0.75 });
  return c.choices[0]?.message?.content || '';
}

function extractExcerpt(body, maxLen = 200) {
  const lines = body.split('\n');
  let p = '';
  for (const line of lines) {
    const t = line.trim();
    if (t.startsWith('# ') && !t.startsWith('## ')) continue;
    if (t.startsWith('## ')) { if (p) break; continue; }
    if (!t) { if (p) break; continue; }
    p += t.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') + ' ';
  }
  let e = p.trim().substring(0, maxLen);
  if (p.trim().length > maxLen) e += '...';
  return e.replace(/"/g, "'");
}

function stripH1(body) {
  let skipped = false;
  return body.split('\n').filter(line => {
    if (!skipped && line.trim().startsWith('# ') && !line.trim().startsWith('## ')) { skipped = true; return false; }
    return true;
  }).join('\n');
}

function wc(text) { return text.split(/\s+/).filter(w => w.length > 0).length; }

async function generateOpp() {
  const { opp, int: ip } = pair;
  console.log(`\n📝 OPP: ${opp.title}`);

  const up = `Write a complete deep-dive article: "${opp.title}"

TRENDING CONTEXT: ${opp.context}
AFFILIATE TOOLS TO MENTION NATURALLY: ${opp.affiliates.join(', ')}

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

Return pure Markdown (no front matter). 5,000-5,500 words minimum.`;

  console.log('  Pass 1/3...');
  const p1 = await callAI([
    { role: 'system', content: OPP_SYS },
    { role: 'user', content: up + '\n\nWrite ONLY: opening paragraphs (no heading), Why This Works Right Now, The Realistic Picture, and The Free Stack. At least 1800 words.' },
  ]);

  console.log('  Pass 2/3...');
  const p2 = await callAI([
    { role: 'system', content: OPP_SYS },
    { role: 'user', content: up },
    { role: 'assistant', content: p1 },
    { role: 'user', content: 'Continue with: The Paid Stack (8-10 tools), The Workflow (3-4 steps), and Pricing (3 tiers). Do NOT repeat. At least 1800 words.' },
  ]);

  console.log('  Pass 3/3...');
  const p3 = await callAI([
    { role: 'system', content: OPP_SYS },
    { role: 'user', content: up },
    { role: 'assistant', content: p1 + '\n\n' + p2 },
    { role: 'user', content: 'Continue with: Getting Clients (3 methods with conversion rates), Tricks and Hacks (5 HACK blockquotes), The Real Numbers (month-by-month table, 12 rows), What Nobody Warns You About (4-5 bold warnings), and Start This Weekend (Sat/Sun plan). Do NOT repeat. At least 1800 words.' },
  ]);

  let body = p1 + '\n\n' + p2 + '\n\n' + p3;
  let w = wc(body);
  console.log(`  After 3 passes: ${w} words`);

  if (w < 4500) {
    console.log('  Pass 4: Expanding...');
    const c = await callAI([
      { role: 'system', content: OPP_SYS },
      { role: 'user', content: up },
      { role: 'assistant', content: body },
      { role: 'user', content: `Current: ${w} words. Need 4500+. Expand thinnest sections with more detail, examples, specific numbers. Do NOT repeat. At least 1500 more words.` },
    ]);
    body += '\n\n' + c;
    w = wc(body);
    console.log(`  After pass 4: ${w} words`);
  }

  const title = body.split('\n').find(l => l.startsWith('# ') && !l.startsWith('## '))?.replace(/^#+\s*/, '').trim().replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') || opp.title;
  const excerpt = extractExcerpt(body);
  const fm = `---\ntitle: "${title}"\ndate: 2026-04-27\ncategory: "AI Opportunity"\nreadTime: "16 MIN"\nexcerpt: "${excerpt}"\nimage: "/images/articles/opportunities/${opp.slug}.png"\nheroImage: "/images/heroes/opportunities/${opp.slug}.png"\nrelatedGuide: "/intelligence/${ip.slug}/"\n---\n\n`;
  const dir = path.join(PROJECT_ROOT, 'content', 'opportunities');
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, `${opp.slug}.md`), fm + stripH1(body));
  console.log(`  ✅ Saved: ${opp.slug}.md (~${w} words)`);
  return { slug: opp.slug, wordCount: w };
}

async function generateInt() {
  const { opp, int: ip } = pair;
  console.log(`\n📝 INT: ${ip.title}`);

  const up = `Write a complete step-by-step implementation article: "${ip.title}"

This is the IMPLEMENTATION companion to: "${opp.title}" (URL: /opportunities/${opp.slug}/)
Reference this opportunity in the opening paragraph.
AFFILIATE TOOLS: ${ip.affiliates.join(', ')}
Difficulty: ${ip.difficulty}

Structure:
1. Opening paragraph (1-2 sentences)
2. ## Prerequisites - accounts, URLs, costs, time
3. ## Step 1 through Step 8 - each with interactive check-ins, UI instructions, code blocks
4. ## Cost Breakdown - table
5. ## Production Checklist - 15-25 checkbox items
6. ## What to Do Next - 4-5 next steps

Each step: interactive check-ins, exact UI steps, code blocks, error scenarios, expected output.
Return pure Markdown (no front matter). 8,000-11,000 words minimum.`;

  console.log('  Pass 1/3...');
  const p1 = await callAI([
    { role: 'system', content: INT_SYS },
    { role: 'user', content: up + '\n\nWrite ONLY: Opening, Prerequisites, Step 1, Step 2, Step 3. Interactive check-ins. At least 2500 words.' },
  ]);

  console.log('  Pass 2/3...');
  const p2 = await callAI([
    { role: 'system', content: INT_SYS },
    { role: 'user', content: up },
    { role: 'assistant', content: p1 },
    { role: 'user', content: 'Continue with Step 4, Step 5, Step 6. Interactive check-ins, code blocks, error scenarios. Do NOT repeat. At least 2500 words.' },
  ]);

  console.log('  Pass 3/3...');
  const p3 = await callAI([
    { role: 'system', content: INT_SYS },
    { role: 'user', content: up },
    { role: 'assistant', content: p1 + '\n\n' + p2 },
    { role: 'user', content: 'Continue with Step 7 (Automate with Make.com), Step 8 (Analytics), Cost Breakdown table, Production Checklist (15-25 items as - [ ] Item), What to Do Next (4-5 steps). Do NOT repeat. At least 2500 words.' },
  ]);

  let body = p1 + '\n\n' + p2 + '\n\n' + p3;
  let w = wc(body);
  console.log(`  After 3 passes: ${w} words`);

  if (w < 6000) {
    console.log('  Pass 4: Expanding...');
    const c = await callAI([
      { role: 'system', content: INT_SYS },
      { role: 'user', content: up },
      { role: 'assistant', content: body },
      { role: 'user', content: `Current: ${w} words. Need 6000+. Expand thinnest steps with more detail, code blocks, error scenarios, check-ins. Do NOT repeat. At least 2000 more words.` },
    ]);
    body += '\n\n' + c;
    w = wc(body);
    console.log(`  After pass 4: ${w} words`);
  }

  if (w < 6000) {
    console.log('  Pass 5: Further expanding...');
    const c = await callAI([
      { role: 'system', content: INT_SYS },
      { role: 'user', content: up },
      { role: 'assistant', content: body },
      { role: 'user', content: `Still ${w} words. Need 6000+. Expand Steps 7-8 significantly with full Make.com setup, analytics dashboards, A/B testing. Add more checklist items. At least 2000 more words.` },
    ]);
    body += '\n\n' + c;
    w = wc(body);
    console.log(`  After pass 5: ${w} words`);
  }

  const title = body.split('\n').find(l => l.startsWith('# ') && !l.startsWith('## '))?.replace(/^#+\s*/, '').trim().replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') || ip.title;
  const excerpt = extractExcerpt(body, 250);
  const fm = `---\ntitle: "${title}"\ndate: 2026-04-27\ncategory: "Implementation"\ndifficulty: "${ip.difficulty}"\nreadTime: "28 MIN"\nexcerpt: "${excerpt}"\nimage: "/images/articles/intelligence/${ip.slug}.png"\nheroImage: "/images/heroes/intelligence/${ip.slug}.png"\nrelatedOpportunity: "/opportunities/${opp.slug}/"\n---\n\n`;
  const dir = path.join(PROJECT_ROOT, 'content', 'intelligence');
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, `${ip.slug}.md`), fm + stripH1(body));
  console.log(`  ✅ Saved: ${ip.slug}.md (~${w} words)`);
  return { slug: ip.slug, wordCount: w };
}

async function main() {
  const oppResult = await generateOpp();
  const intResult = await generateInt();
  console.log(`\n✅ Pair 1 done! Opp: ${oppResult.wordCount}w | Int: ${intResult.wordCount}w`);
}
main().catch(e => { console.error('Fatal:', e); process.exit(1); });
