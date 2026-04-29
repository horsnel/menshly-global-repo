#!/usr/bin/env node
import ZAI from 'z-ai-web-dev-sdk';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, '..');

async function ai(messages) {
  const zai = await ZAI.create();
  const c = await zai.chat.completions.create({ messages, max_tokens: 4000, temperature: 0.75 });
  return c.choices[0]?.message?.content || '';
}

function excerpt(body, max=200) {
  let p = '';
  for (const line of body.split('\n')) {
    const t = line.trim();
    if (t.startsWith('# ') && !t.startsWith('## ')) continue;
    if (t.startsWith('## ')) { if (p) break; continue; }
    if (!t) { if (p) break; continue; }
    p += t.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') + ' ';
  }
  let e = p.trim().substring(0, max);
  if (p.trim().length > max) e += '...';
  return e.replace(/"/g, "'");
}

function stripH1(body) {
  let s = false;
  return body.split('\n').filter(l => {
    if (!s && l.trim().startsWith('# ') && !l.trim().startsWith('## ')) { s = true; return false; }
    return true;
  }).join('\n');
}

function wc(t) { return t.split(/\s+/).filter(w=>w.length>0).length; }

const OPP_SYS = `You are the lead writer for Menshly Global. Casual, straight-talking voice. Like a friend giving you the real playbook. No jargon, no filler. Concrete numbers. Name real tools with real prices. Honest about ugly truths. Short punchy sentences then longer ones with nuance.`;

const INT_SYS = `You are the technical implementation writer for Menshly Global. Deep execution guides. INSTRUCTIONAL COMMANDING tone. Every instruction SPECIFIC: exact button names, menu paths, settings. INTERACTIVE CHECK-INS. Show expected output. Error scenarios. Real tools with real prices. Complete configurations. Use TABLES.`;

const pairs = [
  { opp: { title: "How to Build an AI Chatbot Agency for E-Commerce in 2026 ($8K-25K/Month)", topic: "AI chatbot agency for e-commerce", slug: "ai-chatbot-ecommerce-agency-2026", context: "E-commerce stores are replacing human support with AI chatbots that sell, not just answer questions", affiliates: ["ChatGPT","Make.com","Shopify","Replit","Notion","Zapier"] }, int: { title: "Build an AI Chatbot Agency for E-Commerce: The Complete Step-by-Step Guide", topic: "AI chatbot agency for e-commerce", slug: "build-ai-chatbot-ecommerce-agency", difficulty: "INTERMEDIATE", affiliates: ["ChatGPT","Make.com","Shopify","Replit","Notion","Zapier"] } },
  { opp: { title: "How to Start an AI Lead Generation Agency in 2026 ($5K-20K/Month)", topic: "AI lead generation agency", slug: "ai-lead-generation-agency-2026", context: "B2B companies are desperate for qualified leads and AI can find, qualify, and nurture them automatically", affiliates: ["Apollo.io","Make.com","PhantomBuster","Calendly","ActiveCampaign","Loom"] }, int: { title: "Build an AI Lead Generation Agency: The Complete Step-by-Step Guide", topic: "AI lead generation agency", slug: "build-ai-lead-generation-agency", difficulty: "INTERMEDIATE", affiliates: ["Apollo.io","Make.com","PhantomBuster","Calendly","ActiveCampaign","Loom"] } },
  { opp: { title: "How to Launch an AI Social Media Agency in 2026 ($3K-15K/Month)", topic: "AI social media management agency", slug: "ai-social-media-agency-2026", context: "Brands need constant social content and AI can generate, schedule, and optimize it 24/7", affiliates: ["Canva","Buffer","ChatGPT","Make.com","Beehiiv","Midjourney"] }, int: { title: "Build an AI Social Media Agency: The Complete Step-by-Step Guide", topic: "AI social media management agency", slug: "build-ai-social-media-agency", difficulty: "BEGINNER", affiliates: ["Canva","Buffer","ChatGPT","Make.com","Beehiiv","Midjourney"] } },
  { opp: { title: "How to Build an AI Copywriting Agency in 2026 ($4K-18K/Month)", topic: "AI copywriting agency", slug: "ai-copywriting-agency-2026", context: "Every business needs copy — emails, ads, landing pages — and AI produces first drafts in seconds", affiliates: ["ChatGPT","Grammarly","Make.com","Notion","Semrush","ActiveCampaign"] }, int: { title: "Build an AI Copywriting Agency: The Complete Step-by-Step Guide", topic: "AI copywriting agency", slug: "build-ai-copywriting-agency", difficulty: "BEGINNER", affiliates: ["ChatGPT","Grammarly","Make.com","Notion","Semrush","ActiveCampaign"] } },
  { opp: { title: "How to Start a Faceless YouTube Channel Business with AI in 2026 ($2K-12K/Month)", topic: "AI faceless YouTube channel", slug: "faceless-youtube-channel-ai-2026", context: "Faceless YouTube channels powered by AI video generation are making creators thousands without showing their face", affiliates: ["Fliki AI","ElevenLabs","Canva","ChatGPT","Make.com","Beehiiv"] }, int: { title: "Build a Faceless YouTube Channel Business with AI: The Complete Step-by-Step Guide", topic: "AI faceless YouTube channel", slug: "build-faceless-youtube-channel-ai", difficulty: "BEGINNER", affiliates: ["Fliki AI","ElevenLabs","Canva","ChatGPT","Make.com","Beehiiv"] } },
];

async function genOpp(pair) {
  const {opp, int: ip} = pair;
  console.log(`OPP: ${opp.slug}`);
  const up = `Write a deep-dive article: "${opp.title}"\n\nContext: ${opp.context}\nTools: ${opp.affiliates.join(', ')}\n\nStructure:\n1. Opening hook (no heading) - 2-3 punchy paragraphs\n2. ## Why This Works Right Now - 3 numbered reasons\n3. ## The Realistic Picture (Before You Get Excited) - 4 truths as > **Truth #N:** blockquotes\n4. ## The Free Stack: Starting With Zero Dollars - 6-8 tools **Tool — $0**\n5. ## The Paid Stack: When You're Ready to Scale - 8-10 tools **Tool — $X/mo**\n6. ## The Workflow: Step-by-Step With Every Shortcut - 3-4 steps ### Step N: Name (time)\n7. ## Pricing: What to Charge and How to Defend It - 3 tiers\n8. ## Getting Clients: The Real Playbook - 3 methods with conversion rates\n9. ## Tricks and Hacks They Don't Share in Courses - 5 HACK blockquotes\n10. ## The Real Numbers - Month-by-month revenue table\n11. ## What Nobody Warns You About - 4-5 bold warnings\n12. ## Start This Weekend (Literally) - Sat/Sun plan\n\nPure Markdown. 5000+ words.`;

  const p1 = await ai([{role:'system',content:OPP_SYS},{role:'user',content:up+'\n\nWrite ONLY: opening (no heading), Why This Works Right Now, The Realistic Picture, The Free Stack. 1800+ words.'}]);
  console.log(`  P1: ${wc(p1)}w`);
  const p2 = await ai([{role:'system',content:OPP_SYS},{role:'user',content:up},{role:'assistant',content:p1},{role:'user',content:'Continue: Paid Stack (8-10 tools), Workflow (3-4 steps), Pricing (3 tiers). No repeat. 1800+ words.'}]);
  console.log(`  P2: ${wc(p2)}w`);
  const p3 = await ai([{role:'system',content:OPP_SYS},{role:'user',content:up},{role:'assistant',content:p1+'\n\n'+p2},{role:'user',content:'Continue: Getting Clients (3 methods w/ conversion rates), Tricks and Hacks (5 HACK blockquotes), Real Numbers (12-row table), What Nobody Warns You About (4-5 bold warnings), Start This Weekend (Sat/Sun plan). No repeat. 1800+ words.'}]);
  console.log(`  P3: ${wc(p3)}w`);

  let body = p1+'\n\n'+p2+'\n\n'+p3;
  let w = wc(body);
  if (w < 4500) {
    const p4 = await ai([{role:'system',content:OPP_SYS},{role:'user',content:up},{role:'assistant',content:body},{role:'user',content:`${w} words. Need 4500+. Expand thinnest sections. No repeat. 1500+ more words.`}]);
    body += '\n\n'+p4;
    w = wc(body);
    console.log(`  P4: ${w}w`);
  }

  const title = body.split('\n').find(l=>l.startsWith('# ')&&!l.startsWith('## '))?.replace(/^#+\s*/,'').trim().replace(/\[([^\]]+)\]\([^)]+\)/g,'$1')||opp.title;
  const fm = `---\ntitle: "${title}"\ndate: 2026-04-27\ncategory: "AI Opportunity"\nreadTime: "16 MIN"\nexcerpt: "${excerpt(body)}"\nimage: "/images/articles/opportunities/${opp.slug}.png"\nheroImage: "/images/heroes/opportunities/${opp.slug}.png"\nrelatedGuide: "/intelligence/${ip.slug}/"\n---\n\n`;
  fs.mkdirSync(path.join(ROOT,'content','opportunities'),{recursive:true});
  fs.writeFileSync(path.join(ROOT,'content','opportunities',`${opp.slug}.md`), fm+stripH1(body));
  console.log(`  ✅ ${opp.slug}: ${w}w`);
  return {slug:opp.slug, wordCount:w};
}

async function genInt(pair) {
  const {opp, int:ip} = pair;
  console.log(`INT: ${ip.slug}`);
  const up = `Write a step-by-step implementation guide: "${ip.title}"\n\nCompanion to: "${opp.title}" (/opportunities/${opp.slug}/)\nReference it in opening.\nTools: ${ip.affiliates.join(', ')}\nDifficulty: ${ip.difficulty}\n\nStructure:\n1. Opening paragraph (1-2 sentences)\n2. ## Prerequisites - accounts, URLs, costs, time\n3. ## Step 1 through Step 8 - interactive check-ins, UI instructions, code blocks\n4. ## Cost Breakdown - table\n5. ## Production Checklist - 15-25 checkbox items\n6. ## What to Do Next - 4-5 steps\n\nEach step: interactive check-ins, exact UI steps, code blocks, error scenarios, expected output.\nPure Markdown. 8000+ words.`;

  const p1 = await ai([{role:'system',content:INT_SYS},{role:'user',content:up+'\n\nWrite ONLY: Opening, Prerequisites, Step 1, Step 2, Step 3. Interactive check-ins. 2500+ words.'}]);
  console.log(`  P1: ${wc(p1)}w`);
  const p2 = await ai([{role:'system',content:INT_SYS},{role:'user',content:up},{role:'assistant',content:p1},{role:'user',content:'Continue: Step 4, Step 5, Step 6. Check-ins, code blocks, errors. No repeat. 2500+ words.'}]);
  console.log(`  P2: ${wc(p2)}w`);
  const p3 = await ai([{role:'system',content:INT_SYS},{role:'user',content:up},{role:'assistant',content:p1+'\n\n'+p2},{role:'user',content:'Continue: Step 7 (Make.com automation), Step 8 (Analytics), Cost Breakdown table, Production Checklist (15-25 items), What to Do Next (4-5 steps). No repeat. 2500+ words.'}]);
  console.log(`  P3: ${wc(p3)}w`);

  let body = p1+'\n\n'+p2+'\n\n'+p3;
  let w = wc(body);
  if (w < 6000) {
    const p4 = await ai([{role:'system',content:INT_SYS},{role:'user',content:up},{role:'assistant',content:body},{role:'user',content:`${w} words. Need 6000+. Expand thinnest steps. No repeat. 2000+ more words.`}]);
    body += '\n\n'+p4;
    w = wc(body);
    console.log(`  P4: ${w}w`);
  }
  if (w < 6000) {
    const p5 = await ai([{role:'system',content:INT_SYS},{role:'user',content:up},{role:'assistant',content:body},{role:'user',content:`${w} words still. Need 6000+. Expand Steps 7-8 with full Make.com setup, analytics, A/B testing. More checklist items. 2000+ more words.`}]);
    body += '\n\n'+p5;
    w = wc(body);
    console.log(`  P5: ${w}w`);
  }

  const title = body.split('\n').find(l=>l.startsWith('# ')&&!l.startsWith('## '))?.replace(/^#+\s*/,'').trim().replace(/\[([^\]]+)\]\([^)]+\)/g,'$1')||ip.title;
  const fm = `---\ntitle: "${title}"\ndate: 2026-04-27\ncategory: "Implementation"\ndifficulty: "${ip.difficulty}"\nreadTime: "28 MIN"\nexcerpt: "${excerpt(body,250)}"\nimage: "/images/articles/intelligence/${ip.slug}.png"\nheroImage: "/images/heroes/intelligence/${ip.slug}.png"\nrelatedOpportunity: "/opportunities/${opp.slug}/"\n---\n\n`;
  fs.mkdirSync(path.join(ROOT,'content','intelligence'),{recursive:true});
  fs.writeFileSync(path.join(ROOT,'content','intelligence',`${ip.slug}.md`), fm+stripH1(body));
  console.log(`  ✅ ${ip.slug}: ${w}w`);
  return {slug:ip.slug, wordCount:w, difficulty:ip.difficulty};
}

async function main() {
  console.log('🚀 Starting generation at', new Date().toISOString());
  const results = [];
  for (let i = 0; i < pairs.length; i++) {
    const pair = pairs[i];
    console.log(`\n=== PAIR ${i+1}/5: ${pair.opp.topic} ===`);
    try {
      results.push(await genOpp(pair));
      results.push(await genInt(pair));
    } catch(e) {
      console.error(`❌ Pair ${i+1} failed:`, e.message);
    }
    if (i < pairs.length-1) {
      console.log('Cooldown 3s...');
      await new Promise(r=>setTimeout(r,3000));
    }
  }
  console.log('\n\n📊 SUMMARY');
  for (const r of results) {
    const ok = r.wordCount >= (r.difficulty ? 6000 : 4000) ? '✅' : '⚠️';
    console.log(`${ok} ${r.slug}: ${r.wordCount} words`);
  }
  console.log(`Total: ${results.reduce((s,r)=>s+r.wordCount,0)} words across ${results.length} articles`);
}
main().catch(e=>{console.error('Fatal:',e);process.exit(1);});
