import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const BASE = '/home/z/my-project/menshly-repo';
const THUMB_DIR = path.join(BASE, 'static/images/articles/playbooks');
const HERO_DIR = path.join(BASE, 'static/images/heroes/playbooks');

const THUMB_PREFIX = 'Ultra-premium editorial illustration: an elite playbook blueprint for';
const THUMB_SUFFIX = ', a grand dark open book floating in deep black space with luminous pages revealing modular workflow diagrams, geometric checklists and procedure flowcharts rendered in crimson and red, floating red-rimmed module cards arranged in a grid pattern, crystalline milestone markers with warm red glow, strictly using deep black (#0A0A0A) background with red (#FF0004) accent lighting and highlights, premium minimalist dark aesthetic, bold geometric shapes with luminous red edges and warm crimson glow, abstract futuristic tech aesthetic with atmospheric depth, professional magazine cover quality, ABSOLUTELY NO TEXT NO WORDS NO LETTERS NO NUMBERS NO CHARACTERS NO WRITING NO SCRIPT NO TYPOGRAPHY NO CALLIGRAPHY NO SIGNS NO LABELS NO CAPTIONS NO CHINESE NO JAPANESE NO KOREAN NO ARABIC NO HINDI NO SYMBOLS THAT RESEMBLE WRITING completely text-free image, sharp clean vector-quality edges, 8K quality';

const HERO_PREFIX = 'Cinematic wide hero banner: a grand vaulted chamber for';
const HERO_SUFFIX = ', red light streaming from a central floating open playbook, illuminating floating holographic procedure icons and modular step markers, deep black atmospheric walls receding into dramatic perspective, illuminated red columns representing playbook modules, volumetric red light rays creating atmospheric depth, strictly using deep black (#0A0A0A) atmospheric background with brilliant red (#FF0004) light streams and accents, epic dramatic composition with volumetric red light rays, premium minimalist dark aesthetic, premium editorial magazine quality, ABSOLUTELY NO TEXT NO WORDS NO LETTERS NO NUMBERS NO CHARACTERS NO WRITING NO SCRIPT NO TYPOGRAPHY NO CALLIGRAPHY NO SIGNS NO LABELS NO CAPTIONS NO CHINESE NO JAPANESE NO KOREAN NO ARABIC NO HINDI NO SYMBOLS THAT RESEMBLE WRITING completely text-free image, ultra-clean sharp edges, atmospheric depth with layered black gradient, 8K quality';

const playbooks = [
  { file: 'ai-automation-agency-playbook', title: 'AI Automation Agency Playbook' },
  { file: 'ai-email-marketing-automation-playbook', title: 'AI Email Marketing Automation Playbook' },
  { file: 'ai-seo-agency-playbook', title: 'AI SEO Agency Playbook' },
  { file: 'build-scale-and-monetize-an-ai-translation-and-localization-service-with-chatgpt-and-makecom', title: 'AI Translation and Localization Service' },
  { file: 'ai-hr-recruitment-automation-playbook', title: 'AI HR Recruitment Automation Playbook' },
  { file: 'ai-marketplace-launch-playbook', title: 'AI Marketplace Launch Playbook' },
  { file: 'fetch-the-transaction-from-plaid-sandbox', title: 'Fetch Transaction from Plaid Sandbox' },
  { file: 'ai-bookkeeping-automation-playbook', title: 'AI Bookkeeping Automation Playbook' },
  { file: 'chatgpt-prompt-engineering-guide', title: 'ChatGPT Prompt Engineering Guide' },
  { file: 'ai-copywriting-agency-playbook', title: 'AI Copywriting Agency Playbook' },
  { file: 'ai-cold-email-outreach-playbook', title: 'AI Cold Email Outreach Playbook' },
  { file: 'ai-side-hustle-blueprint', title: 'AI Side Hustle Blueprint' },
  { file: 'ai-customer-onboarding-agency-playbook', title: 'AI Customer Onboarding Agency Playbook' },
  { file: 'ai-ecommerce-optimization-playbook', title: 'AI Ecommerce Optimization Playbook' },
  { file: '24-procedures-12-modules-12-hours-of-reading-and-execution', title: '24 Procedures 12 Modules 12 Hours' },
  { file: 'ai-lead-generation-playbook', title: 'AI Lead Generation Playbook' },
  { file: 'automation-agency-starter-kit', title: 'Automation Agency Starter Kit' },
  { file: 'ai-video-production-agency-playbook', title: 'AI Video Production Agency Playbook' },
];

const MAX_RETRIES = 8;
const BASE_DELAY = 10000; // 10 seconds

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function generateWithRetry(client, prompt, outputPath, label) {
  for (let attempt = 1; attempt <= MAX_RETRIES; attempt++) {
    try {
      console.log(`  [Attempt ${attempt}/${MAX_RETRIES}] ${label}`);
      
      const result = await client.images.generations.create({
        model: 'gpt-image-1',
        prompt: prompt,
        n: 1,
        size: '1344x768',
      });

      if (result.data && result.data[0]) {
        const imageData = result.data[0];
        const base64Data = imageData.base64 || imageData.b64_json;
        if (base64Data) {
          fs.writeFileSync(outputPath, Buffer.from(base64Data, 'base64'));
          const stats = fs.statSync(outputPath);
          console.log(`  ✅ SUCCESS: ${path.basename(outputPath)} (${stats.size} bytes)`);
          return true;
        }
      }
      console.log(`  ⚠️ Unexpected response format, retrying...`);
    } catch (err) {
      const is429 = err.message && err.message.includes('429');
      console.log(`  ❌ Error: ${is429 ? 'Rate limited' : err.message.substring(0, 100)}`);
      
      if (attempt < MAX_RETRIES) {
        const delay = is429 ? Math.min(BASE_DELAY * Math.pow(2, attempt), 180000) : BASE_DELAY;
        console.log(`  ⏳ Waiting ${delay/1000}s before retry...`);
        await sleep(delay);
      }
    }
  }
  console.log(`  💀 PERMANENT FAILURE: ${path.basename(outputPath)}`);
  return false;
}

async function main() {
  const args = process.argv.slice(2);
  const mode = args[0] || 'all'; // all, thumbs, heroes
  const startIdx = parseInt(args[1] || '0');
  const endIdx = parseInt(args[2] || String(playbooks.length - 1));

  console.log('======================================================');
  console.log('  PLAYBOOK IMAGE REGENERATION');
  console.log(`  Mode: ${mode}, Range: ${startIdx}-${endIdx}`);
  console.log(`  ${new Date().toISOString()}`);
  console.log('======================================================');

  // Dynamically import ZAI
  let ZAI;
  try {
    const mod = await import('z-ai-web-dev-sdk');
    ZAI = mod.default;
  } catch (e) {
    console.error('Failed to import z-ai-web-dev-sdk:', e.message);
    process.exit(1);
  }

  const client = await ZAI.create();
  let success = 0, fail = 0;

  const subset = playbooks.slice(startIdx, endIdx + 1);

  if (mode === 'all' || mode === 'thumbs') {
    console.log('\n=== THUMBNAIL IMAGES ===');
    for (let i = 0; i < subset.length; i++) {
      const pb = subset[i];
      const prompt = `${THUMB_PREFIX} ${pb.title}${THUMB_SUFFIX}`;
      const outputPath = path.join(THUMB_DIR, `${pb.file}.png`);
      console.log(`\n[${i+1}/${subset.length}] ${pb.file}`);
      
      if (await generateWithRetry(client, prompt, outputPath, `Thumbnail: ${pb.title}`)) {
        success++;
      } else {
        fail++;
      }
      await sleep(3000); // 3s between requests
    }
  }

  if (mode === 'all' || mode === 'heroes') {
    console.log('\n=== HERO IMAGES ===');
    for (let i = 0; i < subset.length; i++) {
      const pb = subset[i];
      const prompt = `${HERO_PREFIX} ${pb.title}${HERO_SUFFIX}`;
      const outputPath = path.join(HERO_DIR, `${pb.file}.png`);
      console.log(`\n[${i+1}/${subset.length}] ${pb.file}`);
      
      if (await generateWithRetry(client, prompt, outputPath, `Hero: ${pb.title}`)) {
        success++;
      } else {
        fail++;
      }
      await sleep(3000); // 3s between requests
    }
  }

  console.log('\n======================================================');
  console.log('  SUMMARY');
  console.log(`  Success: ${success}, Failed: ${fail}`);
  console.log(`  ${new Date().toISOString()}`);
  console.log('======================================================');

  // Report file sizes
  console.log('\n--- FILE SIZE REPORT ---');
  for (const pb of subset) {
    const thumbPath = path.join(THUMB_DIR, `${pb.file}.png`);
    const heroPath = path.join(HERO_DIR, `${pb.file}.png`);
    const thumbSize = fs.existsSync(thumbPath) ? fs.statSync(thumbPath).size : 'MISSING';
    const heroSize = fs.existsSync(heroPath) ? fs.statSync(heroPath).size : 'MISSING';
    console.log(`  ${pb.file}.png | Thumb: ${thumbSize} | Hero: ${heroSize}`);
  }
}

main().catch(console.error);
