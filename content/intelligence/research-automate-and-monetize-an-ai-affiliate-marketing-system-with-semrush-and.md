---
title: "Research, Automate, and Monetize an AI Affiliate Marketing System with Semrush and Make.com"
date: 2026-05-01
category: "Implementation"
difficulty: "ADVANCED"
readTime: "25 MIN"
excerpt: "> This is the execution guide for building the **AI Affiliate Marketing** business we outlined in our opportunity deep‑dive. > Ready to understand the full business opportunity? Read our opportunity d..."
image: "/images/articles/intelligence/build-and-scale-an-ai-affiliate-marketing-system-with-semrush-and-makecom.png"
heroImage: "/images/heroes/intelligence/build-and-scale-an-ai-affiliate-marketing-system-with-semrush-and-makecom.png"
relatedOpportunity: "/opportunities/ai-affiliate-marketing-business/"
---

> This is the execution guide for building the **AI Affiliate Marketing** business we outlined in our opportunity deep‑dive.  
> Ready to understand the full business opportunity? Read our [opportunity deep‑dive](/opportunities/ai-affiliate-marketing-business.md).

---

## Prerequisites

| Tool | Account Type | Monthly Cost | Time to Setup |
|------|--------------|--------------|---------------|
| [**Semrush**](https://www.semrush.com/) | Pro Plan (SEO Toolkit) | $129.95 | 5 min |
| [**Make.com**](https://www.make.com/en/register?pc=menshly) | Unlimited Plan | $49.00 | 5 min |
| [**Replit**](https://replit.com/refer/egwuokwor) | Hacker Plan (1 GB RAM) | $9.00 | 2 min |
| **ActiveCampaign** | Lite Plan | $15.00 | 3 min |
| [**Canva**](https://www.canva.com/) | Pro Plan | $12.99 | 2 min |
| [**ElevenLabs**](https://elevenlabs.io/) | Free Tier (paid plan $20) | $0–20 | 2 min |
| [**Fliki AI**](https://fliki.ai?referral=noah-wilson-w84be4) | Starter Plan | $18.00 | 3 min |
| [**Vapi**](https://vapi.ai/) | Basic Plan | $14.00 | 3 min |
| **Midjourney** | Standard Plan | $10.00 | 3 min |
| **Hostinger** | Premium Cloud (1 GB) | $3.95 | 3 min |
| **Zapier** | Starter | $19.99 | 2 min |
| [**Notion**](https://notion.so/) | Free | $0 | 1 min |
| [**Grammarly**](https://grammarly.com/) | Premium | $12.00 | 1 min |
| **Other** | - | - | - |

**Total upfront cost per month:** ~$292.88  
*(If you skip paid tiers for a test run, you can remain under ~$100.)*  

**Estimated initial setup time:** 45 minutes.

---

## Step 1: Setup & Configure the Foundation

### 1.1 Create Core Accounts

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
| **Midjourney** | https://midjourney.com/home/ | **Join the Discord** |
| **Hostinger** | https://www.hostinger.com/ | **

| **Hostinger** | https://www.hostinger.com/ | **Get Started** |
| **Zapier** | https://zapier.com/ | **Sign up** |
| **Notion** | https://www.notion.so/ | **Create Account** |
| **Grammarly** | https://www.grammarly.com/ | **Sign Up** |

> **Tip:** Keep all login credentials in a secure password manager (e.g., Bitwarden).  

### 1.2 Capture API Keys

| Tool | Where to Find | How to Copy |
|------|---------------|-------------|
| **Semrush** | Dashboard → Settings → API | Click **Generate API Key**, copy the 32‑character string. |
| **Make.com** | My Apps → Create new app → API Key | Click **Generate**, copy the token. |
| **ActiveCampaign** | Settings → Developer → API Access | Click **Create New API Key**, copy. |
| **ElevenLabs** | Dashboard → API Keys | Click **New Key**, copy. |
| **Fliki AI** | Dashboard → API | Click **Generate**, copy. |
| **Vapi** | Dashboard → API Keys | Click **Generate**, copy. |
| **Hostinger** | Control Panel → API | Click **Generate**, copy. |
| **Zapier** | Settings → API Keys | Click **Generate**, copy. |

> **Interactive Check‑in:**  
> Do you see the API key fields for each tool? If a key is missing, double‑check you are on the correct page. Some platforms hide keys behind a **Show Key** toggle; click it.

### 1.3 Prepare Your Project Directories

We’ll host the backend on **Replit** and the static site on **Hostinger**. Create the following folder structure in Replit:

```
/affiliate-system
├─ /src
│  ├─ index.js
│  ├─ semrush.js
│  ├─ make.js
│  ├─ activecampaign.js
│  └─ helpers.js
├─ /data
│  └─ keywords.json
├─ package.json
└─ .env
```

#### 1.3.1 Create the Replit Project

1. Open Replit, click **+ New Repl**.  
2. Select **Node.js** template.  
3. Name the Repl `affiliate-system`.  
4. After the Repl initializes, click **Files** → **+ Folder** → type `src`.  
5. Inside `src`, create the files listed above.  
6. Click **+ Folder** → type `data`.  

> **Interactive Check‑in:**  
> Do you see a `package.json` at the root? If not, run `npm init -y` in the console.

#### 1.3.2 Configure Environment Variables

Open `.env` and paste:

```
SEMRUSH_API_KEY=your_semrush_key
MAKE_API_KEY=your_make_key
ACTIVE_CAMPAIGN_API_KEY=your_ac_key
ACTIVE_CAMPAIGN_URL=https://youraccount.api-us1.com
ELEVENLABS_API_KEY=your_elevenlabs_key
FLIKI_API_KEY=your_fliki_key
VAPI_KEY=your_vapi_key
HOSTINGER_API_KEY=your_hostinger_key
```

> **Interactive Check‑in:**  
> Do you see the `.env` file with the keys? If any key is missing, revisit the API key steps.

### 1.4 Install Core Dependencies

Open the Replit **Shell** and run:

```bash
npm install axios dotenv nodemon
```

- **axios** – HTTP client for API calls.  
- **dotenv** – Load `.env` variables.  
- **nodemon** – Auto‑restart during development.

> **Expected Output:**

```
added 134 packages, updated 3 packages, and audited 137 packages in 12.3s
```

Add a **start** script to `package.json`:

```json
"scripts": {
  "dev": "nodemon src/index.js",
  "start": "node src/index.js"
}
```

> **Interactive Check‑in:**  
> Run `npm run dev` and confirm the console prints `Server is running on port 3000`. If you see `nodemon: command not found`, install it globally: `npm install -g nodemon`.

---

## Step 2: Build Core Component – Keyword Discovery & Content Planning

The heart of an AI affiliate marketing system is the **keyword discovery pipeline**. We’ll fetch keyword ideas from Semrush, enrich them with traffic metrics, and push them into ActiveCampaign as prospects for content creation.

### 2.1 Semrush Keyword Extraction

Create `src/semrush.js`:

```js
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
  const rows = response.data.split('\n').slice(1); // skip header
  const keywords = rows.map(row => {
    const [phrase, volume, cost, competition, position] = row.split(';');
    return { phrase, volume, cost, competition, position };
  });

  return keywords;
}

module.exports = { fetchKeywordIdeas };
```

> **Explanation:**  
> - `export_columns` selects: Phrase, Search Volume, CPC

## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
