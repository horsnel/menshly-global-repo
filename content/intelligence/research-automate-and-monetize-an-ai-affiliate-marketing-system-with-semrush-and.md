---
title: "Research, Automate, and Monetize an AI Affiliate Marketing System with Semrush and Make.com"
date: 2026-05-01
category: "Implementation"
difficulty: "ADVANCED"
readTime: "35 MIN"
excerpt: "This is the execution guide for building the AI Affiliate Marketing business we outlined in our opportunity deep‑dive. Follow the steps below and you'll have a fully automated content research, creation, and monetization pipeline..."
image: "/images/articles/intelligence/build-and-scale-an-ai-affiliate-marketing-system-with-semrush-and-makecom.png"
heroImage: "/images/heroes/intelligence/build-and-scale-an-ai-affiliate-marketing-system-with-semrush-and-makecom.png"
relatedOpportunity: "/opportunities/ai-affiliate-marketing-business/"
relatedPlaybook: "/playbooks/24-procedures-12-modules-12-hours-of-reading-and-execution/"
---

This is the execution guide for building the **AI Affiliate Marketing** business we outlined in our opportunity deep‑dive. Follow the steps below and you will have a fully automated content research, creation, and monetization pipeline that generates affiliate revenue around the clock. This system uses Semrush for keyword intelligence, Make.com for workflow automation, and AI for content generation — all connected into a self‑reinforcing loop that compounds over time.

Ready to understand the full business opportunity? Read our [opportunity deep‑dive](/opportunities/ai-affiliate-marketing-business/).

---

## Prerequisites

| Tool | Account Type | Monthly Cost | Time to Setup |
|------|--------------|--------------|---------------|
| [**Semrush**](https://www.semrush.com/) | Pro Plan (SEO Toolkit) | $129.95 | 5 min |
| [**Make.com**](https://www.make.com/en/register?pc=menshly) | Teams Plan | $49.00 | 5 min |
| [**Replit**](https://replit.com/refer/egwuokwor) | Hacker Plan (1 GB RAM) | $9.00 | 2 min |
| **ActiveCampaign** | Lite Plan | $15.00 | 3 min |
| [**Canva**](https://www.canva.com/) | Pro Plan | $12.99 | 2 min |
| [**ElevenLabs**](https://elevenlabs.io/) | Free Tier (paid plan $20) | $0–20 | 2 min |
| [**Fliki AI**](https://fliki.ai?referral=noah-wilson-w84be4) | Starter Plan | $18.00 | 3 min |
| [**Vapi**](https://vapi.ai/) | Basic Plan | $14.00 | 3 min |
| **Hostinger** | Premium Cloud (1 GB) | $3.95 | 3 min |
| **Zapier** | Starter | $19.99 | 2 min |
| [**Notion**](https://notion.so/) | Free | $0 | 1 min |
| [**Grammarly**](https://grammarly.com/) | Premium | $12.00 | 1 min |

**Total upfront cost per month:** Approximately $304.88 (or under $100 if you skip paid tiers for an initial test run).

**Estimated initial setup time:** 60 to 90 minutes for the complete pipeline.

---

## Step 1: Set Up and Configure the Foundation

### 1.1 Create Core Accounts

Create accounts for each tool in the prerequisites table. Use a consistent email address across all platforms to simplify account management. Store all credentials in a secure password manager like Bitwarden — you will be generating API keys for each service, and losing track of them is a common source of integration failures.

| Tool | URL | Exact Button |
|------|-----|--------------|
| **Semrush** | https://app.semrush.com/ | **Start Free Trial** |
| **Make.com** | https://www.make.com/ | **Sign up** |
| **Replit** | https://replit.com/ | **Sign up** |
| **ActiveCampaign** | https://www.activecampaign.com/ | **Get Started** |
| **Canva** | https://www.canva.com/ | **Sign up** |
| **ElevenLabs** | https://elevenlabs.io/ | **Create Account** |
| **Fliki AI** | https://fliki.ai/ | **Sign Up** |
| **Vapi** | https://vapi.ai/ | **Register** |
| **Hostinger** | https://www.hostinger.com/ | **Get Started** |
| **Zapier** | https://zapier.com/ | **Sign up** |
| **Notion** | https://www.notion.so/ | **Create Account** |
| **Grammarly** | https://www.grammarly.com/ | **Sign Up** |

> **Tip:** Complete all account creations in a single session. The momentum of setting up the entire stack at once is important — spreading setup across multiple days is the number one reason operators abandon this system before it generates revenue.

### 1.2 Capture API Keys

Every tool in this pipeline exposes an API that Make.com or your Replit app will call programmatically. Generate and store these keys now:

| Tool | Where to Find the API Key | How to Copy |
|------|---------------------------|-------------|
| **Semrush** | Dashboard then Settings then API | Click **Generate API Key**, copy the 32‑character string |
| **Make.com** | My Apps then Create new app then API Key | Click **Generate**, copy the token |
| **ActiveCampaign** | Settings then Developer then API Access | Click **Create New API Key**, copy the URL and key together |
| **ElevenLabs** | Dashboard then API Keys | Click **New Key**, copy |
| **Fliki AI** | Dashboard then API | Click **Generate**, copy |
| **Vapi** | Dashboard then API Keys | Click **Generate**, copy |
| **Hostinger** | Control Panel then API | Click **Generate**, copy |
| **Zapier** | Settings then API Keys | Click **Generate**, copy |

> **Interactive Check‑in:** Do you see the API key fields for each tool? If a key is missing, double‑check you are on the correct page. Some platforms hide keys behind a **Show Key** toggle — click it to reveal the full string.

### 1.3 Prepare Your Project Directories

You will host the backend on Replit and the static affiliate site on Hostinger. Create the following folder structure in Replit:

```
/affiliate-system
├── /src
│   ├── index.js          # Main server entry point
│   ├── semrush.js        # Semrush API wrapper
│   ├── content.js        # AI content generation module
│   ├── make.js           # Make.com webhook triggers
│   ├── activecampaign.js # Email automation module
│   └── helpers.js        # Shared utilities
├── /data
│   └── keywords.json     # Cached keyword data
├── package.json
└── .env
```

#### 1.3.1 Create the Replit Project

1. Open Replit, click **+ New Repl**, and select the **Node.js** template.
2. Name the Repl `affiliate-system`.
3. After the Repl initializes, create the folder structure listed above.
4. Initialize the project: `npm init -y` in the Shell.

#### 1.3.2 Configure Environment Variables

Open the `.env` file and paste:

```
SEMRUSH_API_KEY=your_semrush_key
MAKE_API_KEY=your_make_key
ACTIVE_CAMPAIGN_API_KEY=your_ac_key
ACTIVE_CAMPAIGN_URL=https://youraccount.api-us1.com
ELEVENLABS_API_KEY=your_elevenlabs_key
FLIKI_API_KEY=your_fliki_key
VAPI_KEY=your_vapi_key
HOSTINGER_API_KEY=your_hostinger_key
OPENAI_API_KEY=your_openai_key
```

> **Check‑in:** Do you see the `.env` file with all the keys? If any key is missing, revisit the API key steps above.

### 1.4 Install Core Dependencies

Open the Replit Shell and run:

```bash
npm install axios dotenv nodemon openai
```

- **axios** — HTTP client for all API calls throughout the pipeline
- **dotenv** — Load environment variables from the `.env` file
- **nodemon** — Auto‑restart the server during development
- **openai** — Official OpenAI SDK for content generation

Add start scripts to `package.json`:

```json
"scripts": {
  "dev": "nodemon src/index.js",
  "start": "node src/index.js"
}
```

> **Check‑in:** Run `npm run dev` and confirm the console prints `Server running on port 3000`.

---

## Step 2: Build the Keyword Discovery Pipeline

The heart of an AI affiliate marketing system is the keyword discovery pipeline. This module fetches keyword ideas from Semrush, enriches them with traffic and competition metrics, and prioritizes them by affiliate potential. A well‑configured keyword pipeline is the difference between writing content that ranks and writing content that disappears into the void.

### 2.1 Semrush Keyword Extraction

Create `src/semrush.js`:

```javascript
require('dotenv').config();
const axios = require('axios');

const SEMRUSH_API_KEY = process.env.SEMRUSH_API_KEY;
const SEMRUSH_BASE = 'https://api.semrush.com';

async function fetchKeywordIdeas(baseKeyword, limit = 20) {
  const url = `${SEMRUSH_BASE}/keywords/overview`;
  const params = {
    key: SEMRUSH_API_KEY,
    display_limit: limit,
    export_columns: 'Ph,Nq,Cp,Co,Pr',
    keyword: baseKeyword,
    database: 'us',
    type: 'phrase_organic',
  };

  const response = await axios.get(url, { params });
  const rows = response.data.split('\n').slice(1); // Skip header row
  const keywords = rows.map(row => {
    const [phrase, volume, cpc, competition, position] = row.split(';');
    return {
      phrase: phrase?.trim(),
      volume: parseInt(volume) || 0,
      cpc: parseFloat(cpc) || 0,
      competition: parseFloat(competition) || 0,
      position: parseInt(position) || 0,
    };
  });

  return keywords.filter(k => k.phrase && k.volume > 0);
}

async function findAffiliateKeywords(niche, count = 50) {
  // Start with broad niche terms
  const seedKeywords = [
    niche,
    `best ${niche}`,
    `${niche} review`,
    `${niche} vs`,
    `cheap ${niche}`,
    `${niche} alternatives`,
    `top ${niche} 2026`,
  ];

  const allKeywords = [];
  for (const seed of seedKeywords) {
    const keywords = await fetchKeywordIdeas(seed, Math.ceil(count / seedKeywords.length));
    allKeywords.push(...keywords);
  }

  // Deduplicate and sort by affiliate potential score
  const seen = new Set();
  const unique = allKeywords.filter(k => {
    if (seen.has(k.phrase)) return false;
    seen.add(k.phrase);
    return true;
  });

  // Score: High volume + high CPC + low competition = best affiliate potential
  return unique
    .map(k => ({
      ...k,
      affiliateScore: (k.volume * k.cpc) / (k.competition + 0.1),
    }))
    .sort((a, b) => b.affiliateScore - a.affiliateScore)
    .slice(0, count);
}

module.exports = { fetchKeywordIdeas, findAffiliateKeywords };
```

### 2.2 Test the Keyword Pipeline

Create a test script `src/test-keywords.js`:

```javascript
const { findAffiliateKeywords } = require('./semrush');

async function test() {
  const keywords = await findAffiliateKeywords('project management software', 20);
  console.log('Top Affiliate Keywords:');
  keywords.forEach((k, i) => {
    console.log(`${i + 1}. "${k.phrase}" — Vol: ${k.volume}, CPC: $${k.cpc}, Score: ${k.affiliateScore.toFixed(0)}`);
  });
}

test().catch(console.error);
```

Run it with `node src/test-keywords.js`. You should see a ranked list of keywords with their affiliate potential scores. The highest‑scoring keywords are your content priorities — these are the terms where search volume meets commercial intent.

---

## Step 3: Build the AI Content Generation Module

### 3.1 Content Generator (src/content.js)

```javascript
require('dotenv').config();
const OpenAI = require('openai');

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

async function generateAffiliateArticle(keyword, productData, wordCount = 2500) {
  const prompt = `Write a comprehensive, SEO-optimized affiliate article targeting the keyword "${keyword.phrase}".

Requirements:
- Word count: approximately ${wordCount} words
- Include an engaging introduction that addresses the reader's pain point
- Naturally incorporate the keyword "${keyword.phrase}" 3-5 times throughout
- Include a comparison section for these products: ${productData.map(p => p.name).join(', ')}
- Add pros and cons for each product
- Include a clear recommendation with reasoning
- End with a compelling call-to-action
- Use H2 and H3 subheadings for structure
- Write in an authoritative but approachable tone
- Do NOT use generic filler language

Product details:
${productData.map(p => `- ${p.name}: ${p.description} (Price: ${p.price}, Affiliate link: ${p.link})`).join('\n')}

The article should feel like genuine expert advice, not a sales pitch. Focus on helping the reader make an informed decision.`;

  const response = await openai.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [
      { role: 'system', content: 'You are an expert product reviewer and affiliate content writer who produces honest, detailed, and helpful comparison articles.' },
      { role: 'user', content: prompt },
    ],
    max_tokens: Math.min(wordCount * 2, 4096),
    temperature: 0.7,
  });

  return response.choices[0].message.content;
}

async function generateMetaDescription(keyword, articlePreview) {
  const response = await openai.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [
      { role: 'system', content: 'Write compelling SEO meta descriptions under 160 characters.' },
      { role: 'user', content: `Write a meta description for an article targeting "${keyword.phrase}". Article preview: ${articlePreview.slice(0, 500)}` },
    ],
    max_tokens: 100,
    temperature: 0.5,
  });

  return response.choices[0].message.content;
}

module.exports = { generateAffiliateArticle, generateMetaDescription };
```

### 3.2 Define Your Affiliate Products

Create `data/products.json` with the products you are affiliating:

```json
{
  "project_management": [
    {
      "name": "Monday.com",
      "description": "Visual project management platform with automation",
      "price": "$9/user/month",
      "link": "https://your-affiliate-link.com/monday",
      "category": "team-collaboration"
    },
    {
      "name": "ClickUp",
      "description": "All-in-one productivity platform",
      "price": "$7/user/month",
      "link": "https://your-affiliate-link.com/clickup",
      "category": "all-in-one"
    },
    {
      "name": "Asana",
      "description": "Work management for teams",
      "price": "$10.99/user/month",
      "link": "https://your-affiliate-link.com/asana",
      "category": "task-tracking"
    }
  ]
}
```

Replace the affiliate links with your actual tracked links. Each product entry should include enough detail for the AI to write meaningful comparisons.

---

## Step 4: Build the Make.com Automation Scenarios

### 4.1 Scenario 1: Weekly Keyword Research Pipeline

This scenario runs every Monday at 6 AM, fetches new keyword opportunities from Semrush, and queues them for content creation.

1. **Trigger:** Scheduler (every Monday at 6:00 AM)
2. **Module 1:** HTTP request to your Replit app's `/api/keywords/fetch` endpoint
3. **Module 2:** JSON Parser to extract the top 10 keywords
4. **Module 3:** Iterator to loop through each keyword
5. **Module 4:** Notion — Create a new page in the "Content Queue" database for each keyword, including the search volume, CPC, competition score, and affiliate potential score
6. **Module 5:** Slack or Email — Send yourself a weekly summary of the top 10 opportunities

### 4.2 Scenario 2: Content Generation Pipeline

This scenario monitors the Notion "Content Queue" database and generates articles for queued keywords.

1. **Trigger:** Notion — Watch for new pages in "Content Queue" with status "Queued"
2. **Module 1:** HTTP request to your Replit app's `/api/content/generate` endpoint, passing the keyword data and product information
3. **Module 2:** Notion — Update the page with the generated article content and change status to "Draft"
4. **Module 3:** ActiveCampaign — Add the keyword to a tracking list for SEO monitoring
5. **Module 4:** Email — Send the draft article to your editorial inbox for review

### 4.3 Scenario 3: Content Publishing Pipeline

After you review and approve a draft, this scenario publishes it to your Hostinger site and distributes it across channels.

1. **Trigger:** Notion — Watch for pages with status "Approved"
2. **Module 1:** HTTP request to Hostinger to create a new blog post via the WordPress REST API (if using WordPress) or Hugo content file (if using Hugo)
3. **Module 2:** Canva — Generate a featured image using the keyword as a prompt
4. **Module 3:** Fliki AI — Convert the article into a 60‑second video summary for YouTube Shorts and social media
5. **Module 4:** ActiveCampaign — Add the published article to your newsletter queue
6. **Module 5:** Notion — Update the page status to "Published" and record the publication date and URL

---

## Step 5: Deploy the Hostinger Affiliate Site

### 5.1 Site Architecture

Your affiliate site should be built for speed and SEO. Use Hugo (the same static site generator as the Menshly platform) for maximum performance:

```
/affiliate-site
├── content/
│   ├── _index.md          # Homepage
│   ├── about.md            # About page
│   └── reviews/            # Product review articles
│       ├── best-project-management-tools.md
│       ├── monday-vs-clickup.md
│       └── ...
├── layouts/
│   ├── index.html
│   └── reviews/
│       └── single.html
├── static/
│   ├── images/
│   └── css/
└── config.toml
```

### 5.2 SEO Configuration

In `config.toml`, configure SEO essentials:

```toml
baseURL = "https://your-affiliate-site.com"
languageCode = "en-us"
title = "Your Niche Reviews"

[params]
  description = "Expert reviews and comparisons for [your niche]"
  affiliateDisclaimer = "We may earn a commission when you purchase through our links. This does not affect our recommendations."

[markup]
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true
```

### 5.3 Deploy to Hostinger

1. Build the Hugo site locally: `hugo --minify`
2. Upload the `public/` directory to your Hostinger server via SFTP or the Hostinger File Manager
3. Configure your domain's DNS to point to the Hostinger server
4. Enable SSL via Hostinger's one‑click Let's Encrypt integration
5. Submit your sitemap to Google Search Console: `https://your-affiliate-site.com/sitemap.xml`

---

## Step 6: Build the Email Nurturing Sequence

### 6.1 Welcome Sequence (ActiveCampaign)

Create a five‑email welcome sequence for subscribers who join your email list through a lead magnet (e.g., "Free Comparison Checklist: Top 10 Project Management Tools"):

| Email | Delay | Subject | Purpose |
|-------|-------|---------|---------|
| #1 | Immediate | Your [Niche] Comparison Checklist is Here | Deliver the lead magnet, introduce your brand |
| #2 | Day 2 | The #1 Mistake People Make When Choosing [Niche] Tools | Educational content that builds trust |
| #3 | Day 4 | Our Top Pick for [Niche] in 2026 | Soft recommendation with affiliate link |
| #4 | Day 7 | [Tool A] vs [Tool B]: Which One Wins? | Detailed comparison with multiple affiliate links |
| #5 | Day 10 | Ready to Decide? Here's Our Final Recommendation | Strong CTA with the highest‑commission product |

### 6.2 Ongoing Content Newsletter

After the welcome sequence, subscribers enter a weekly newsletter that delivers:

- One new product review per week
- One "vs" comparison article per week
- One industry news roundup per week
- Occasional "deal alert" emails when products offer discounts (these generate the highest per‑email revenue)

---

## Step 7: Video Content Pipeline with Fliki AI

### 7.1 Automate Video Creation

For each published article, automatically generate a 60‑second video summary using Fliki AI:

```javascript
// src/fliki.js
const axios = require('axios');

async function generateVideo(articleContent, keyword) {
  const response = await axios.post('https://api.fliki.ai/v1/generate', {
    script: articleContent.slice(0, 500), // First 500 chars as video script
    voice: 'professional_female',
    aspect_ratio: '9:16', // Vertical for Shorts/Reels
    subtitles: true,
    background_music: 'upbeat_corporate',
  }, {
    headers: { 'Authorization': `Bearer ${process.env.FLIKI_API_KEY}` },
  });

  return response.data.video_url;
}

module.exports = { generateVideo };
```

### 7.2 Distribution Workflow

1. Generate the video through Fliki AI
2. Upload to YouTube Shorts, Instagram Reels, and TikTok via Make.com social media modules
3. Include the affiliate link in the video description and pinned comment
4. Track clicks through your affiliate dashboard

---

## Step 8: Monitoring, Analytics, and Optimization

### 8.1 Track Key Metrics

Monitor these metrics weekly:

- **Organic traffic per article** (Google Analytics)
- **Keyword ranking position** (Semrush Position Tracking)
- **Click‑through rate on affiliate links** (your affiliate dashboard)
- **Conversion rate** (affiliate clicks to purchases)
- **Revenue per article** (total commissions divided by number of articles)
- **Email subscriber growth** (ActiveCampaign)
- **Video views and engagement** (YouTube Analytics)

### 8.2 Optimization Loop

Every month, run this optimization loop:

1. **Identify underperforming articles** — Articles ranking below position 20 for their target keyword need content updates. Add 500+ words of new information, update product prices and features, and add fresh internal links.
2. **Double down on winners** — Articles ranking in the top 5 should get more backlinks, social promotion, and email feature spots. Consider creating companion videos and infographics.
3. **Refresh stale content** — Update any article with outdated product information, pricing, or screenshots. Google rewards freshness, especially for review content.
4. **Test new keywords** — Run the keyword discovery pipeline monthly and add the top 5 new opportunities to your content queue.

---

## Step 9: Scaling to $10K+ Per Month

### 9.1 Expand to Multiple Niches

Once your first niche generates $3K+ per month, replicate the system in a new niche. The entire pipeline — keyword research, content generation, email nurturing, and video distribution — is niche‑agnostic. You only need to swap the product data and Semrush seed keywords.

High‑commission niches for 2026:

- **SaaS and software** (30–50% recurring commissions)
- **Financial services** (high CPA, $100–$500 per referral)
- **Health and wellness supplements** (30–40% commissions)
- **Online education and courses** (50–70% commissions)
- **Web hosting and domains** ($50–$200 per signup)

### 9.2 Build a Content Team

At $7K+ per month, hire freelance writers and editors to supplement AI‑generated content. AI handles the first draft; humans add expertise, personal experience, and editorial quality. This hybrid approach produces content that ranks better than pure AI output and converts better than generic affiliate spam.

### 9.3 Launch a Paid Acquisition Channel

Reinvest 20% of revenue into paid channels:

- **Google Ads** targeting high‑intent keywords (e.g., "buy project management software")
- **YouTube pre‑roll ads** on competitor review videos
- **Newsletter sponsorships** in your niche

---

## Troubleshooting Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| Articles not ranking | Low Domain Authority or thin content | Build backlinks via guest posts; add 1,000+ words of unique analysis |
| Low affiliate CTR | Generic CTAs or too many links | Use contextual product recommendations; limit to 3–4 affiliate links per article |
| High bounce rate | Content does not match search intent | Analyze the top‑ranking pages for your keyword; match their format and depth |
| Semrush API limits | Exceeded plan quota | Cache keyword data locally; reduce API calls by batching queries |
| Make.com scenario failures | Webhook timeout or API changes | Add error‑handling modules with retry logic; monitor scenario execution logs daily |
| Content feels "AI‑generated" | Overly formulaic prompts | Add personal anecdotes, specific use cases, and opinionated recommendations to prompts |

---

## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
- **[Semrush](https://www.semrush.com/)** — SEO and content marketing — outrank your competitors
- **[ElevenLabs](https://elevenlabs.io/)** — AI voice synthesis — human‑quality voiceovers and agents
- **[Replit](https://replit.com/refer/egwuokwor)** — Cloud IDE — build and deploy without infrastructure
