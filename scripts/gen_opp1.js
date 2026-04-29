#!/usr/bin/env node
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const PROJECT_ROOT = path.resolve(__dirname, '..');

async function callAI(messages) {
  const zai = await ZAI.create();
  const c = await zai.chat.completions.create({ messages, max_tokens: 4000, temperature: 0.75 });
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

const SYS = `You are the lead writer for Menshly Global. Write in a casual, straight-talking voice — like a friend who's done this gives you the real playbook. No corporate jargon. No filler. Every sentence carries weight. Short punchy sentences then longer ones with nuance. Concrete numbers. Name real tools with real prices. Be honest about ugly truths.`;

async function main() {
  const up = `Write a complete deep-dive article: "How to Build an AI Chatbot Agency for E-Commerce in 2026 ($8K-25K/Month)"

TRENDING CONTEXT: E-commerce stores are replacing human support with AI chatbots that sell, not just answer questions
AFFILIATE TOOLS: ChatGPT, Make.com, Shopify, Replit, Notion, Zapier

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

  console.log('Pass 1...');
  const p1 = await callAI([
    { role: 'system', content: SYS },
    { role: 'user', content: up + '\n\nWrite ONLY: opening paragraphs (no heading), Why This Works Right Now, The Realistic Picture, and The Free Stack. At least 1800 words.' },
  ]);
  console.log(`Pass 1 done: ${wc(p1)} words`);

  console.log('Pass 2...');
  const p2 = await callAI([
    { role: 'system', content: SYS },
    { role: 'user', content: up },
    { role: 'assistant', content: p1 },
    { role: 'user', content: 'Continue with: The Paid Stack (8-10 tools), The Workflow (3-4 steps), and Pricing (3 tiers). Do NOT repeat. At least 1800 words.' },
  ]);
  console.log(`Pass 2 done: ${wc(p2)} words`);

  console.log('Pass 3...');
  const p3 = await callAI([
    { role: 'system', content: SYS },
    { role: 'user', content: up },
    { role: 'assistant', content: p1 + '\n\n' + p2 },
    { role: 'user', content: 'Continue with: Getting Clients (3 methods with conversion rates), Tricks and Hacks (5 HACK blockquotes), The Real Numbers (month-by-month table, 12 rows), What Nobody Warns You About (4-5 bold warnings), and Start This Weekend (Sat/Sun plan). Do NOT repeat. At least 1800 words.' },
  ]);
  console.log(`Pass 3 done: ${wc(p3)} words`);

  let body = p1 + '\n\n' + p2 + '\n\n' + p3;
  let w = wc(body);
  console.log(`After 3 passes: ${w} words`);

  if (w < 4500) {
    console.log('Pass 4...');
    const c = await callAI([
      { role: 'system', content: SYS },
      { role: 'user', content: up },
      { role: 'assistant', content: body },
      { role: 'user', content: `Current: ${w} words. Need 4500+. Expand thinnest sections. Do NOT repeat. At least 1500 more words.` },
    ]);
    body += '\n\n' + c;
    w = wc(body);
    console.log(`After pass 4: ${w} words`);
  }

  const title = body.split('\n').find(l => l.startsWith('# ') && !l.startsWith('## '))?.replace(/^#+\s*/, '').trim().replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') || 'How to Build an AI Chatbot Agency for E-Commerce in 2026 ($8K-25K/Month)';
  const excerpt = extractExcerpt(body);
  const fm = `---\ntitle: "${title}"\ndate: 2026-04-27\ncategory: "AI Opportunity"\nreadTime: "16 MIN"\nexcerpt: "${excerpt}"\nimage: "/images/articles/opportunities/ai-chatbot-ecommerce-agency-2026.png"\nheroImage: "/images/heroes/opportunities/ai-chatbot-ecommerce-agency-2026.png"\nrelatedGuide: "/intelligence/build-ai-chatbot-ecommerce-agency/"\n---\n\n`;
  const dir = path.join(PROJECT_ROOT, 'content', 'opportunities');
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, 'ai-chatbot-ecommerce-agency-2026.md'), fm + stripH1(body));
  console.log(`✅ Saved: ai-chatbot-ecommerce-agency-2026.md (~${w} words)`);
}
main().catch(e => { console.error('Fatal:', e); process.exit(1); });
