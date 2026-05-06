---
title: "The AI SEO Agency Playbook: 36 Steps to $25K/Month"
date: 2026-05-01
category: "Playbook"
price: "₦35,000"
readTime: "90 MIN"
excerpt: "The complete operating system for building an AI-powered SEO agency from zero. 10 modules, 40 procedures, exact tool configurations, client acquisition scripts, three pricing tiers, and a scaling roadmap. From empty Semrush dashboard to ₦15M/month in recurring revenue."
image: "/images/articles/playbooks/ai-seo-agency-playbook.png"
heroImage: "/images/heroes/playbooks/ai-seo-agency-playbook.png"
relatedOpportunity: "/opportunities/ai-seo-agency-2026/"
relatedGuide: "/intelligence/build-optimize-scale-ai-seo-workflows-semrush/"
---

This is not a blog post condensed into a PDF. This is an operating system for building an AI-powered SEO agency from zero to ₦15,000,000/month in recurring revenue. Every module contains exact procedures — not theories, not possibilities, not "consider doing X." You will do X, in this order, with these tools, and you will verify it worked before moving on.

**40 procedures. 10 modules. 8+ hours of reading and execution.** If you complete every procedure, you will have a functioning SEO agency with paying clients, automated content pipelines, and a scaling roadmap. If you skip procedures, you will have a folder of half-configured tools and no revenue. The choice is yours.

---

# MODULE 1: FOUNDATION — YOUR SEO AGENCY OPERATING SYSTEM

## Overview

Before you touch a single keyword research tool, you need the infrastructure that runs your agency. This module sets up your project management, documentation, client portal, financial tracking, and communication systems. These are not optional. Every successful SEO agency operator has these systems in place before their first client call. Every failed operator skipped them.

**Time to complete:** 3-4 hours
**Tools needed:** Notion (free), Google Workspace (₦3,600/mo), Paystack (free to set up)

## Procedure 1.1: Create Your Agency Command Center in Notion

Open your browser and go to notion.so. Sign in or create a free account. You should see the Notion dashboard — a clean sidebar on the left and a main area with a "New page" button.

Click **New page** in the left sidebar. Name it: `[Your Agency Name] Command Center`. This is the single source of truth for your entire business.

Inside this page, create seven sub-pages by typing `/page` and naming each one:

1. **Clients** — Every client, their status, their deliverables, their revenue
2. **SOPs** — Standard Operating Procedures for every repeatable SEO process
3. **Prompt Library** — Every AI prompt your agency uses, organized by service type
4. **Keyword Vaults** — Organized keyword research by client and industry
5. **Templates** — Client-facing documents, proposals, contracts, reports
6. **Finance** — Revenue tracking, expense tracking, margin analysis
7. **Pipeline** — Prospects, leads, and their position in your sales process

### The Clients Database

Open the **Clients** sub-page. Type `/table` and select **Table — Full page**. Name it `Client Roster`.

Add these columns (click the `+` button at the right end of the header row):

| Column Name | Type | Description |
|---|---|---|
| Client Name | Title | The business name |
| Status | Select: Active, Onboarding, Paused, Churned | Current relationship state |
| Tier | Select: Starter, Growth, Enterprise | Service tier |
| Monthly Revenue | Number | Retainer amount in Naira |
| Setup Fee | Number | One-time setup fee in Naira |
| Start Date | Date | When the engagement began |
| Next Delivery | Date | When the next deliverable is due |
| Semrush Project | URL | Link to the Semrush project |
| Ahrefs Campaign | URL | Link to the Ahrefs campaign |
| Health Score | Select: Green, Yellow, Red | Relationship health |

Add one test row: Client Name = "Test Client," Status = "Active," Tier = "Starter," Monthly Revenue = 500000, Setup Fee = 300000. Fill in all remaining fields.

## Procedure 1.2: Set Up Your Financial Infrastructure

### Paystack for Naira Payments

Go to paystack.com and create a business account. Complete the business verification — you will need your BVN, a valid ID, and a corporate bank account. Paystack processes Naira payments directly, supports recurring billing, and charges 1.5% + ₦100 per transaction (capped at ₦2,000).

Once approved, navigate to **Products** in the Paystack dashboard. Create three products:

**Product 1: Starter Setup Fee**
- Name: `Starter SEO Setup`
- Price: ₦300,000 (One time)
- Description: "One-time setup fee for Starter tier SEO engagement"

**Product 2: Starter Monthly Retainer**
- Name: `Starter Monthly SEO`
- Price: ₦500,000/month (Recurring)
- Description: "Monthly retainer for Starter tier SEO services"

**Product 3: Growth Setup Fee**
- Name: `Growth SEO Setup`
- Price: ₦750,000 (One time)

**Product 4: Growth Monthly Retainer**
- Name: `Growth Monthly SEO`
- Price: ₦1,500,000/month (Recurring)

**Product 5: Enterprise Setup Fee**
- Name: `Enterprise SEO Setup`
- Price: ₦2,000,000 (One time)

**Product 6: Enterprise Monthly Retainer**
- Name: `Enterprise Monthly SEO`
- Price: ₦3,000,000/month (Recurring)

Generate payment links for each product. Save all links in your Notion **Templates** page under "Payment Links."

### Revenue Tracking

In your Notion **Finance** page, create a table called `Revenue Tracker` with these columns:

| Column Name | Type |
|---|---|
| Month | Title (e.g., "May 2026") |
| Total MRR | Number (Monthly Recurring Revenue in ₦) |
| Setup Fees | Number |
| Total Revenue | Formula: Total MRR + Setup Fees |
| Expenses | Number |
| Net Profit | Formula: Total Revenue - Expenses |
| Active Clients | Number |
| Average Revenue Per Client | Formula: Total MRR / Active Clients |

## Procedure 1.3: Configure Your Communication Stack

### Business Email

Go to workspace.google.com and sign up for the Business Starter plan ($6/mo ≈ ₦9,600/mo). Register a domain that matches your agency name. Create your email: hello@youragency.com or yourname@youragency.com. Do not use a personal Gmail address for client communication.

### Client Booking Calendar

Go to cal.com and create a free account. Set up two meeting types:

1. **SEO Discovery Call** — 30 minutes, available Monday through Friday, 9 AM to 5 PM WAT
2. **Weekly Check-in** — 15 minutes, recurring, for active clients only

Connect your Google Calendar. Copy your booking link and save it in Notion **Templates**.

{{% accent-box %}}HACK: Set your Cal.com minimum scheduling notice to 2 hours. This prevents prospects from booking a call 5 minutes from now when you are unprepared. First impressions are everything — a frantic, unprepared discovery call kills deals before they start.{{% /accent-box %}}

## Check-In: Module 1 Complete

- [ ] Notion Command Center created with all 7 sub-pages
- [ ] Client Roster database with all 10 columns and a test row
- [ ] Paystack account with 6 products and 6 payment links
- [ ] Revenue Tracker table in Notion with current month row
- [ ] Professional email address on custom domain
- [ ] Cal.com booking page with SEO Discovery Call and Weekly Check-in

Count your checkmarks. You need all 6. Do not proceed to Module 2 with an incomplete foundation.

---

# MODULE 2: TECH STACK — YOUR SEO ARSENAL

## Overview

Your agency runs on tools. This module sets up every tool you need — Semrush, Ahrefs, ChatGPT, Make.com — connects them, and verifies each connection. Total cost: under ₦200,000/month at full capacity, but most tools are free or discounted until you have paying clients.

**Time to complete:** 4-5 hours
**Tools needed:** Semrush (₦0-30 day trial → ₦55,000/mo Guru), Ahrefs (₦0-7 day trial → ₦55,000/mo Standard), ChatGPT Plus (₦30,000/mo), Make.com (free tier)

## Procedure 2.1: Configure Semrush

Go to semrush.com and start a 30-day free trial of the **Guru plan**. You need Guru (not Pro) because it includes Content Marketing Toolkit and historical data. Pro does not.

After signing in, you should see the Semrush dashboard with a domain search bar at the top. Enter your own website domain (or a client's if you have one). Press Enter.

### Create Your First Project

Click **Projects** in the left sidebar → **Create project** → Enter your domain → Name it `[Client/Domain] SEO Project`.

Enable these tracking modules (click each one and configure):

**1. Position Tracking**
- Keywords: Add 50 target keywords relevant to the niche
- Location: Select the target country and city
- Device: Desktop + Mobile
- Frequency: Daily tracking (this matters — weekly data is too slow for SEO reporting)

**2. Site Audit**
- Crawl scope: Crawl all subdomains → No
- Crawl limit: 500 pages (Starter), 2,000 pages (Growth), 10,000 pages (Enterprise)
- Crawl frequency: Weekly
- User-agent: SemrushBot
- Exclude parameters: Add `?utm_`, `?ref=`, `?fbclid=` to prevent duplicate URL crawling

**3. On-Page SEO Checker**
- Click **Start** — Semrush will analyze your top 10 ranking keywords and generate recommendations
- This module auto-updates weekly

**4. Content Analyzer**
- Connect Google Analytics and Google Search Console when prompted
- This enables content performance tracking tied to real traffic data

Do you see all four modules active in your Project dashboard? If any show "Not configured," click them and complete setup. Every module must be green.

{{% accent-box %}}HACK: Before your Semrush trial expires, export all Position Tracking data, Site Audit reports, and Keyword Magic Tool results to Google Sheets. If you cannot afford Guru immediately, you retain your research data and can re-subscribe when you land your first client. Never lose research because of a lapsed subscription.{{% /accent-box %}}

## Procedure 2.2: Configure Ahrefs

Go to ahrefs.com and start a 7-day trial of the **Standard plan** ($99/mo ≈ ₦158,000/mo at full price, trial is $7).

After signing in, you should see the Ahrefs dashboard with a search bar. Enter your target domain.

### Set Up Site Explorer Configuration

1. Click **Site Explorer** → Enter your domain → Select mode: **Subdomains** (this captures www and non-www)
2. In the left sidebar, navigate to **Organic keywords** — this shows all keywords the domain currently ranks for
3. Click the **Export** button → Export to CSV → Save in your Google Drive under `Clients/[Name]/Discovery/`

### Set Up Ahrefs Alerts

Click **Alerts** in the top navigation. Create three alerts:

**Alert 1: New backlinks**
- Type: Backlink
- Frequency: Daily
- Send to: Your professional email

**Alert 2: Keyword ranking changes**
- Type: Keyword
- Track: Top 50 keywords
- Frequency: Weekly
- Send to: Your professional email

**Alert 3: New referring domains**
- Type: Referring domain
- Frequency: Weekly
- Send to: Your professional email

### Ahrefs Site Audit Setup

Click **Site Audit** in the left sidebar → **+ New project** → Enter domain → Configure:

- Crawl scope: Path `/` only (entire site)
- Crawl limit: 500 URLs (Starter), 5,000 (Growth+)
- JavaScript rendering: Enabled (critical for modern sites)
- Schedule: Weekly, Monday at 2:00 AM WAT

Run your first audit. Wait for completion (5-30 minutes depending on site size). Review the Health Score — this is the number you will improve for clients.

## Procedure 2.3: Set Up Your AI Content Engine

### ChatGPT Plus Configuration

Go to chatgpt.com and subscribe to ChatGPT Plus ($20/mo ≈ ₦30,000/mo). You need Plus for GPT-4o access, which produces significantly better SEO content than GPT-3.5.

Create a **Custom GPT** specifically for SEO content production:

1. Click **Explore GPTs** → **Create**
2. Name: `SEO Content Engine`
3. Description: "Produces SEO-optimized content following exact specifications"
4. Instructions (paste this exactly):

```
You are an SEO content production engine. You receive a content brief and produce a fully optimized article. Follow these rules without exception:

1. NEVER acknowledge the prompt. Start writing immediately.
2. Include the target keyword in: title, first paragraph, at least 2 H2 headings, meta description, and naturally throughout body text.
3. Write at the specified word count ±5%. Never write less than 90% of the target.
4. Use this structure: H1 title → Introduction (hook + keyword) → 4-6 H2 sections → H2 FAQ section with 5 questions → Conclusion with CTA.
5. Every H2 section must be 200-400 words.
6. Include 3-5 internal linking suggestions marked as [INTERNAL LINK: topic].
7. Include 2-3 external linking suggestions marked as [EXTERNAL LINK: authoritative source on topic].
8. Write at a Flesch-Kincaid grade level of 7-8. Short sentences. Active voice. No jargon without explanation.
9. Add schema markup suggestions at the end in JSON-LD format.
10. Output the meta title (max 60 chars) and meta description (max 155 chars) BEFORE the article body.
```

5. Save the GPT. Test it with this prompt: "Write a 1,500-word article targeting the keyword 'best SEO tools for small business'. Tone: professional but approachable. Audience: Nigerian small business owners."

Review the output. Does it include the meta title/description? Are H2 headings present? Is the keyword distributed naturally? If not, refine your Custom GPT instructions and test again.

### OpenAI API Access

Go to platform.openai.com. Navigate to **API Keys** and create a new key. Copy it immediately — you cannot view it again. Store it in a password manager (1Password, Bitwarden) — not in Notion.

Navigate to **Billing** and add $20 in credit. Set a monthly limit of $100. This prevents a buggy automation from draining your account overnight.

## Procedure 2.4: Set Up Make.com for SEO Automations

Go to make.com and sign up for the Free plan (1,000 operations/month).

Click your profile icon → **Connections** → **Add connection**. Connect these services:

1. **Google Sheets** — Authorize with your Google account
2. **Gmail** — Authorize with your professional email
3. **Slack** — Create a workspace at slack.com if needed, then authorize
4. **OpenAI** — Enter your API key
5. **Notion** — Authorize with your Notion account
6. **HTTP (Make a request)** — This is built-in, no connection needed

Verify all 5 connected services show a green "Connected" status.

## Check-In: Module 2 Complete

- [ ] Semrush Guru plan with first project configured (4 modules active)
- [ ] Ahrefs Standard plan with 3 alerts and Site Audit configured
- [ ] ChatGPT Plus with SEO Content Engine Custom GPT created and tested
- [ ] OpenAI API key with $20+ credit and $100 monthly limit
- [ ] Make.com account with 5 connected services (all green)
- [ ] All initial audit data exported and saved to Google Drive

6 checkmarks required. Do you have all 6?

---

# MODULE 3: KEYWORD RESEARCH SYSTEM — THE INTELLIGENCE ENGINE

## Overview

Keyword research is the foundation of every SEO engagement. This module gives you a repeatable system for producing keyword maps that drive content strategy, on-page optimization, and client reporting. You will use Semrush and Ahrefs in tandem — each has strengths the other lacks.

**Time to complete:** 4-6 hours (first time), 2-3 hours per client after system is built

## Procedure 3.1: The Keyword Research Workflow in Semrush

Open Semrush. Click **Keyword Magic Tool** in the left sidebar.

Enter your client's primary keyword (e.g., "digital marketing Nigeria"). Set these filters:

- **Country:** Target country (e.g., Nigeria)
- **Volume:** Minimum 10 monthly searches
- **Keyword Difficulty (KD%):** Maximum 70 (anything above 70 requires heavy link building — not suitable for new clients)
- **Include keywords:** Add niche-specific modifiers (e.g., "lagos", "small business", "affordable")
- **Exclude keywords:** Add irrelevant terms (e.g., "free", "salary", "jobs", "course", "internship")

Click **Search**. You should see a table of keywords with columns: Keyword, Volume, KD%, CPC, Competitive Density, Results, Trend.

### Build the Keyword Map

Select keywords by checking the box next to each one. Prioritize by this exact order:

1. **High volume + Low KD (under 30)** — These are your "quick win" keywords. Tag them `PRIORITY-1`.
2. **Medium volume + Medium KD (30-50)** — These require content investment but are achievable. Tag them `PRIORITY-2`.
3. **High volume + High KD (50-70)** — These need link building support. Tag them `PRIORITY-3`.

Click **Add to keyword list** → Create a new list named `[Client Name] Keyword Map`.

Export the list: Click **Export** → **CSV** → Save to `Clients/[Name]/Discovery/` in Google Drive.

## Procedure 3.2: Cross-Reference with Ahrefs Keyword Explorer

Open Ahrefs. Click **Keywords Explorer** in the top navigation.

Enter the same primary keyword. Select the same country. Click **Search**.

### Apply the Ahrefs Filter Stack

In the Keywords Explorer results, apply these filters:

- **Volume:** 10+
- **Keyword Difficulty:** 0-70
- **Traffic Potential:** 50+ (this estimates total traffic if you ranked #1 for this keyword AND all related long-tail variations)
- **SERP Features:** Select "Featured snippet available" — these are opportunities to win Position Zero

Sort by **Traffic Potential** descending. This gives you keywords where ranking #1 produces real traffic, not just vanity metrics.

### Find Keyword Gaps

In Ahrefs, click **Content Gap** in the left sidebar under **Competitive analysis**.

Enter your client's domain in the top field. Enter 3-5 competitor domains in the bottom field. Click **Show keywords**.

This shows keywords that competitors rank for but your client does not. Sort by **Volume** descending. Filter KD to 0-50. These are your easiest acquisition opportunities.

Export all results to CSV. Save alongside the Semrush data.

## Procedure 3.3: Build the Content Calendar from Keywords

Open a new Google Sheet. Name it `[Client Name] Content Calendar`. Create these columns:

| Column | Description |
|---|---|
| Keyword | Target keyword from research |
| Search Volume | Combined Semrush + Ahrefs data |
| KD Score | Use the higher of the two tools |
| Priority | PRIORITY-1, PRIORITY-2, or PRIORITY-3 |
| Content Type | How-to, Listicle, Comparison, Definition, Case Study |
| Target Word Count | 1,500 (P1), 2,000 (P2), 2,500+ (P3) |
| Search Intent | Informational, Transactional, Navigational, Commercial |
| Publish Date | When the article goes live |
| Status | Planned, In Progress, Published, Ranking |

Fill this sheet with 50 keywords minimum. Yes, 50. A proper content calendar covers 3-6 months of weekly publishing. Anything less is not a strategy — it is a wish.

{{% accent-box %}}HACK: Use Ahrefs' "Questions" report in Keywords Explorer to find question-based keywords. These produce "People Also Ask" featured snippets at a 3x higher rate than statement keywords. Featured snippets drive 8-12% of all organic clicks for pages that win them. Stack your content calendar with question-based keywords for rapid visibility gains.{{% /accent-box %}}

## Procedure 3.4: Automate Keyword Monitoring with Make.com

Create a new Make.com scenario called "Weekly Keyword Rank Tracker."

**Module 1: Schedule Trigger**
- Interval: Every Monday at 7:00 AM WAT

**Module 2: HTTP — Make a Request (Semrush API)**
- URL: `https://api.semrush.com/?type=position_tracking&key=[YOUR_API_KEY]&project=[PROJECT_ID]&display_limit=50`
- Method: GET
- Parse response: Yes

**Module 3: Google Sheets — Update Rows**
- Spreadsheet: `[Client Name] Rank Tracker`
- Map the API response fields to your sheet columns: keyword, previous position, current position, change, URL

**Module 4: OpenAI — Analyze Changes**
- Model: gpt-4o
- System prompt: "Analyze these keyword ranking changes. Identify: 1) Keywords that improved by 5+ positions (celebrate these), 2) Keywords that dropped by 5+ positions (investigate these), 3) Keywords on the cusp of page 1 (positions 11-15, push these). Output a 3-section summary."
- User message: Map the rank change data

**Module 5: Slack — Send Message**
- Channel: `#seo-reports`
- Message: Map the AI analysis output

Activate the scenario. Verify it runs on the next Monday.

## Check-In: Module 3 Complete

- [ ] Semrush Keyword Magic Tool search completed with all filters applied
- [ ] Keyword map created with PRIORITY-1, PRIORITY-2, PRIORITY-3 tags
- [ ] Ahrefs Keywords Explorer cross-reference completed
- [ ] Content Gap analysis against 3-5 competitors completed
- [ ] Content Calendar spreadsheet with 50+ keywords populated
- [ ] Weekly Keyword Rank Tracker automation built in Make.com

6 checkmarks. The Content Calendar is the most critical deliverable — it becomes the roadmap for every piece of content you produce.

---

# MODULE 4: AI CONTENT STRATEGY — THE PRODUCTION PIPELINE

## Overview

Content production is where most SEO agencies fail. They either produce thin content that never ranks or they spend ₦50,000+ per article on human writers and cannot maintain margins. This module gives you an AI-powered content pipeline that produces publish-ready articles at scale while maintaining quality. You will produce 8-12 articles per month per Growth client while spending less than ₦5,000 per article on AI costs.

**Time to complete:** 5-6 hours to build the pipeline, then 1-2 hours per article

## Procedure 4.1: Create the Content Brief Template

Before any article is written, you need a content brief. Open your SEO Content Engine Custom GPT and use this prompt to generate briefs:

```
Generate a comprehensive content brief for the keyword "[TARGET KEYWORD]".

Include:
1. Target keyword and 3-5 secondary keywords
2. Search intent classification
3. Recommended word count
4. Recommended title (under 60 characters, includes target keyword)
5. Meta description (under 155 characters, includes target keyword, has a CTA)
6. H2 outline (6-8 sections, each with a 1-sentence description of what it covers)
7. Key points to cover (based on top 10 ranking articles for this keyword)
8. Internal linking opportunities (related topics on our site)
9. External linking opportunities (authoritative sources to cite)
10. FAQ section: 5 questions with brief answers (target PAA snippets)
11. Schema markup type: Article, FAQPage, HowTo, or Review
12. Call to action: What action should the reader take?
```

Save each generated brief in your Notion **Prompt Library** under "Content Briefs → [Client Name]".

## Procedure 4.2: The AI Content Production Process

### Step 1: Generate the First Draft

Open your SEO Content Engine Custom GPT. Paste the content brief and add:

```
Write this article now. Follow the brief exactly. Do not add a conclusion until I say so. Write at least [WORD COUNT] words. Use short paragraphs (2-3 sentences max). Every H2 section must be substantial — no 50-word filler sections.
```

### Step 2: Human Edit Pass (30 minutes per article)

Read the entire draft. Fix these specific issues that AI consistently produces:

1. **Remove hedging language** — Delete phrases like "it's worth noting that," "in today's digital landscape," "at the end of the day." These are AI filler.
2. **Add specific data** — Replace vague claims ("many businesses") with specific numbers ("67% of Nigerian SMEs"). Use Statista, Google Trends, or industry reports.
3. **Inject client voice** — Add one anecdote, opinion, or perspective that only the client could provide. This is what makes content feel human.
4. **Verify facts** — AI hallucinates statistics. Every claim with a number must be verified or removed.
5. **Improve transitions** — AI articles jump between topics. Add transitional sentences between H2 sections.

### Step 3: On-Page Optimization Pass

Run the article through Semrush's **SEO Writing Assistant**:

1. Open Semrush → **Content Marketing** → **SEO Writing Assistant**
2. Click **Create new template** → Enter your target keyword → Select country and language
3. Paste your edited article
4. Review the scores: Overall, Readability, SEO, Originality, Tone of Voice

Target scores:
- **Overall:** 8+/10
- **Readability:** 8+/10 (Flesch-Kincaid grade 7-8)
- **SEO:** 9+/10 (keyword placement, related keywords, length)
- **Originality:** 7+/10 (rewrites any flagged sentences)
- **Tone of Voice:** Match the client's brand (formal, casual, technical)

If any score is below target, follow the specific recommendations in the sidebar. Recompose flagged sentences. Add recommended related keywords. Extend short sections.

{{% accent-box %}}HACK: After the SEO Writing Assistant pass, search your target keyword on Google and open the top 3 ranking articles. Identify one element each article has that yours lacks — a unique statistic, a specific example, a visual element. Add that missing element to your article. This "skyscraper" technique is what pushes your content from page 2 to page 1.{{% /accent-box %}}

### Step 4: Add Schema Markup

At the bottom of your article (in the CMS), add JSON-LD schema markup. Use this template:

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[ARTICLE TITLE]",
  "description": "[META DESCRIPTION]",
  "author": {
    "@type": "Organization",
    "name": "[CLIENT NAME]"
  },
  "publisher": {
    "@type": "Organization",
    "name": "[CLIENT NAME]",
    "logo": {
      "@type": "ImageObject",
      "url": "[LOGO URL]"
    }
  },
  "datePublished": "[PUBLISH DATE]",
  "dateModified": "[MODIFY DATE]",
  "mainEntityOfPage": "[ARTICLE URL]"
}
```

For FAQ articles, also add:

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[QUESTION 1]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[ANSWER 1]"
      }
    }
  ]
}
```

## Procedure 4.3: Build the Content Publishing Automation

Create a Make.com scenario called "Content Publishing Pipeline."

**Module 1: Google Sheets — Watch Rows**
- Spreadsheet: `[Client Name] Content Calendar`
- Sheet: "Content Calendar"
- Filter: Status = "In Progress"
- Trigger: When a row is added or updated

**Module 2: OpenAI — Generate Meta Tags**
- Model: gpt-4o
- System prompt: "Generate an SEO-optimized meta title (max 60 characters) and meta description (max 155 characters) for the following article. Output as JSON: {\"meta_title\": \"...\", \"meta_description\": \"...\"}"
- User message: Map the keyword and article title from the sheet

**Module 3: Gmail — Send Notification**
- To: The client's content manager
- Subject: "New SEO Article Ready for Review: [Article Title]"
- Body: Include the meta title, meta description, target keyword, and a link to the Google Doc

**Module 4: Google Sheets — Update Row**
- Set Status = "Ready for Review"
- Set Publish Date = today's date + 2 business days

Activate the scenario. Test with one article from your Content Calendar.

## Procedure 4.4: Content Refresh Automation

Ranking content decays. An article that ranks #3 today will drop to #8 in 6 months if untouched. You need a content refresh system.

Create a Make.com scenario called "Content Decay Monitor."

**Module 1: Schedule Trigger** — First of every month at 6:00 AM WAT

**Module 2: HTTP — Semrush API Position Tracking**
- Pull current rankings for all tracked keywords
- Filter: Keywords where position dropped by 3+ places in the last 90 days

**Module 3: OpenAI — Generate Refresh Recommendations**
- Model: gpt-4o
- System prompt: "You are an SEO content strategist. Given a list of articles whose rankings have declined, generate specific refresh recommendations for each. Include: new sections to add, outdated statistics to update, new keywords to incorporate, and internal links to add. Output as a numbered list."
- User message: Map the declining keyword data

**Module 4: Google Sheets — Add Rows**
- Spreadsheet: `[Client Name] Content Refresh Queue`
- Map: keyword, current position, previous position, AI recommendations, priority level

## Check-In: Module 4 Complete

- [ ] Content Brief template created and tested with 3 keywords
- [ ] AI Content Production Process documented as SOP (4 steps)
- [ ] SEO Writing Assistant scores hitting 8+/10 on test articles
- [ ] Schema markup templates saved in Notion Templates
- [ ] Content Publishing Pipeline automation built and tested in Make.com
- [ ] Content Decay Monitor automation built and tested

6 checkmarks. The SEO Writing Assistant scores are non-negotiable — content below 8/10 will not rank consistently. Fix it before publishing.

---

# MODULE 5: ON-PAGE OPTIMIZATION — THE PRECISION ENGINE

## Overview

On-page optimization is where SEO campaigns are won or lost. You can have perfect keyword research and excellent content, but if your title tags are 80 characters, your images have no alt text, and your internal linking is random, you will not rank. This module gives you a systematic on-page optimization process that you apply to every page on a client's site.

**Time to complete:** 3-4 hours per site (initial optimization), 1 hour per month (maintenance)

## Procedure 5.1: The On-Page Audit Checklist

For every page on the client's site, run this checklist:

| Element | Specification | Tool to Verify |
|---|---|---|
| Title Tag | 50-60 characters, includes primary keyword, compelling | Semrush Site Audit |
| Meta Description | 140-155 characters, includes keyword, has CTA | Semrush Site Audit |
| H1 Tag | Exactly 1 per page, includes primary keyword | Semrush Site Audit |
| H2-H3 Structure | Logical hierarchy, no skipped levels, keywords in H2s | Manual review |
| URL Structure | Short, keyword-rich, no stop words, hyphens not underscores | Manual review |
| Image Alt Text | Descriptive, includes keyword where natural, no keyword stuffing | Semrush Site Audit |
| Internal Links | Minimum 3 internal links per page to related content | Ahrefs Site Audit |
| External Links | 2-3 authoritative external links per article | Manual review |
| Schema Markup | Appropriate type (Article, FAQ, HowTo, Product, LocalBusiness) | Google Rich Results Test |
| Core Web Vitals | LCP < 2.5s, FID < 100ms, CLS < 0.1 | Google PageSpeed Insights |
| Mobile Usability | No mobile usability errors | Google Search Console |
| Canonical Tags | Self-referencing on canonical pages, pointing to canonical on duplicates | Semrush Site Audit |

## Procedure 5.2: Execute On-Page Optimization Using Semrush

Open your Semrush project. Click **On-Page SEO Checker**. This module analyzes your site against the top 10 ranking pages for your target keywords and generates specific recommendations.

Click **Ideas** tab. You will see a list of optimization ideas sorted by estimated traffic impact. Work through them in this order:

**Priority 1: "Implement immediately" ideas** — These are quick wins (title tag fixes, missing meta descriptions, broken internal links). Estimated time: 30 minutes per page.

**Priority 2: "Content-related" ideas** — These require content changes (adding keywords, extending word count, adding semantic keywords). Estimated time: 1-2 hours per page.

**Priority 3: "Technical" ideas** — These require developer involvement (schema markup, canonical tags, page speed). Estimated time: varies, coordinate with client's developer.

For each optimization you implement, mark it as "Implemented" in the On-Page SEO Checker. Semrush will re-crawl and verify the change within 1-2 weeks.

## Procedure 5.3: Internal Linking Strategy and Automation

Internal linking is the most underrated SEO tactic. Most sites have thousands of pages with fewer than 3 internal links pointing to each page. Google uses internal links to understand site structure, distribute page authority, and discover new content.

### Build the Internal Link Map

1. Export all published URLs from the client's sitemap (domain.com/sitemap.xml)
2. In Ahrefs, go to **Site Explorer** → **Best by links** → Sort by **URL Rating (UR)** descending
3. Identify the top 20 pages by authority — these are your "power pages"
4. For each power page, add 3-5 internal links pointing to pages that need an authority boost (pages ranking positions 11-20 for their target keywords)
5. Use descriptive anchor text that includes the target page's keyword

### Automate Internal Link Discovery

Create a Make.com scenario: "Internal Link Opportunities."

**Module 1: Schedule Trigger** — Every 2 weeks, Wednesday at 9:00 AM WAT

**Module 2: HTTP — Ahrefs API**
- Endpoint: `/api/v3/site-explorer/organic-keywords`
- Parameters: domain, limit=100, display_filter="position>10 AND position<21"
- This fetches keywords where the client ranks page 2 (positions 11-20)

**Module 3: OpenAI — Generate Link Recommendations**
- Model: gpt-4o
- System prompt: "Given a list of pages ranking positions 11-20 for their target keywords, suggest 3 internal link insertion points per page. For each, specify: 1) The source page (high authority page on the same site), 2) The anchor text to use, 3) The target page. Output as a table."
- User message: Map the position 11-20 data + top authority pages

**Module 4: Google Sheets — Add Rows**
- Spreadsheet: `[Client Name] Internal Link Opportunities`

## Check-In: Module 5 Complete

- [ ] On-Page Audit Checklist completed for all priority pages
- [ ] Semrush On-Page SEO Checker "Implement immediately" ideas all marked done
- [ ] Core Web Vitals passing on mobile and desktop for top 10 pages
- [ ] Internal Link Map created with top 20 power pages identified
- [ ] Internal Link Opportunities automation built and tested
- [ ] At least 15 internal links added across priority pages

6 checkmarks. The internal links are the easiest win on this list — most clients see a 2-5 position boost within 4 weeks of adding strategic internal links.

---

# MODULE 6: TECHNICAL SEO AUDITS — THE INFRASTRUCTURE LAYER

## Overview

Technical SEO is the plumbing of your client's website. If the plumbing is broken, nothing else matters — not content, not links, not keywords. A site with crawl errors, broken redirects, and slow page speed will never rank regardless of how good the content is. This module gives you a systematic technical audit process using Semrush and Ahrefs.

**Time to complete:** 4-6 hours per audit, 2 hours per month for monitoring

## Procedure 6.1: Run the Semrush Site Audit

Open your Semrush project → **Site Audit** → Click **Start audit** if this is your first time, or **Re-audit** if one exists.

Wait for completion (5-30 minutes). Review the **Overview** tab. You will see:

- **Errors** (red): Critical issues that must be fixed immediately
- **Warnings** (yellow): Important issues that should be fixed within 30 days
- **Notices** (blue): Informational items to review

### Fix These Errors First (Always)

1. **Broken pages (4xx errors)** — Find the source of internal links pointing to these pages and update them
2. **Duplicate content without canonical** — Add canonical tags pointing to the primary version
3. **Broken redirects (5xx errors)** — Fix server-side issues or remove redirect chains
4. **Missing meta descriptions** — Write unique meta descriptions for every page (use the AI content engine for scale)
5. **Missing H1 tags** — Add exactly one H1 per page containing the target keyword
6. **Mixed content (HTTP/HTTPS)** — Force HTTPS redirect and update all internal links

## Procedure 6.2: Run the Ahrefs Site Audit

Open Ahrefs → **Site Audit** → Your project → **View results**.

Focus on the **Performance** and **Crawlability** tabs:

### Performance Issues
- **Largest Contentful Paint (LCP)** — Target under 2.5 seconds
- **Cumulative Layout Shift (CLS)** — Target under 0.1
- **Total page size** — Flag pages over 3MB
- **Unused CSS/JS** — Recommend code splitting or deferral

### Crawlability Issues
- **Orphan pages** — Pages with zero internal links pointing to them. Add at least one internal link to each.
- **Crawl depth > 4 clicks** — Important pages should be reachable within 3 clicks from the homepage. Restructure navigation.
- **Blocked resources** — Ensure robots.txt is not blocking CSS/JS files that Googlebot needs to render the page
- **Redirect chains** — Chains of 3+ redirects waste crawl budget. Consolidate to single 301 redirects.

## Procedure 6.3: Create the Technical SEO Report Template

Build a Google Docs template called `[Client Name] Technical SEO Report — [Month]`. Structure:

**Section 1: Executive Summary (1 page)**
- Site Health Score (Semrush): Previous → Current → Change
- Ahrefs Health Score: Previous → Current → Change
- Total errors found vs. total errors fixed this month
- Top 3 priority issues remaining

**Section 2: Crawl Errors (with screenshots)**
- List each 4xx and 5xx error with: URL, error type, recommended fix, status (Fixed/Pending)

**Section 3: Index Coverage**
- Total indexed pages vs. total submitted pages
- Pages blocked by robots.txt (review for accidental blocks)
- Pages with noindex tags (review for accidental noindex)
- Canonical tag issues

**Section 4: Page Speed (Core Web Vitals)**
- LCP, FID, CLS scores for top 10 traffic pages
- Before/after comparison if fixes were implemented

**Section 5: Recommendations for Next Month**
- Prioritized list of 5-10 fixes with estimated impact

## Procedure 6.4: Automate Technical Monitoring

Create a Make.com scenario: "Technical SEO Alert System."

**Module 1: Schedule Trigger** — Daily at 6:00 AM WAT

**Module 2: HTTP — Semrush API Site Audit**
- Pull new errors detected in the last 24 hours

**Module 3: Router — Filter by Severity**
- Path 1: Critical errors → Send immediately to Slack `#seo-critical`
- Path 2: Warnings → Aggregate in Google Sheets for weekly review

**Module 4: Slack — Critical Alerts**
- Channel: `#seo-critical`
- Message: "🚨 CRITICAL SEO ERROR DETECTED: [error type] on [URL]. Fix within 24 hours."

**Module 5: Google Sheets — Log All Errors**
- Spreadsheet: `[Client Name] Error Log`
- Columns: Date, URL, Error Type, Severity, Status, Date Fixed

{{% accent-box %}}HACK: Set up Google Search Console email forwarding to your professional email. Google sends alerts for critical issues (malware, indexing drops, manual actions) directly. Forward these to your `#seo-critical` Slack channel using Make.com. A 48-hour delay in responding to a manual action penalty can cost a client months of organic traffic.{{% /accent-box %}}

## Check-In: Module 6 Complete

- [ ] Semrush Site Audit completed with all critical errors documented
- [ ] Ahrefs Site Audit completed with performance and crawlability issues documented
- [ ] Technical SEO Report template created and filled out for first client
- [ ] Top 10 critical errors fixed or documented with fix timeline
- [ ] Technical SEO Alert System automation built and tested
- [ ] Google Search Console email forwarding configured

6 checkmarks. Critical errors must be fixed before you do anything else. A site with broken redirects is a site that cannot rank, period.

---

# MODULE 7: LINK BUILDING AUTOMATION — THE AUTHORITY ACCELERATOR

## Overview

Backlinks remain the strongest ranking signal in Google's algorithm. Without them, your content competes with one hand tied behind its back. This module gives you a systematic link building process that combines AI-powered prospecting with automated outreach. You will build 10-20 quality backlinks per month per Growth client.

**Time to complete:** 5-6 hours to build the system, 3-4 hours per week to execute

## Procedure 7.1: Backlink Prospecting with Ahrefs

Open Ahrefs → **Site Explorer** → Enter a competitor domain → **Backlinks** in the left sidebar.

Filter backlinks:
- **Dofollow** only (nofollow links do not pass authority)
- **DR (Domain Rating)** 30+ (lower DR links are not worth the effort)
- **Traffic:** 100+ monthly visits to the linking page
- **Link type:** Text links (image links and redirects are less valuable)
- **Platform:** Exclude forum links and blog comments (low quality)

Export the filtered backlink list. These are websites that have linked to your client's competitors. They are your primary link targets — they have already demonstrated willingness to link to content in this niche.

## Procedure 7.2: The Skyscraper Link Building Method

### Step 1: Find Link-Worthy Content

In Ahrefs, go to **Top content** → **Best by links** for competitor domains. Identify their most-linked pages (pages with 20+ referring domains). These are content formats that naturally attract links in this niche.

Common link-worthy formats:
- Original research / data studies
- Comprehensive guides ("Ultimate Guide to...")
- Free tools and calculators
- Infographics
- Case studies with real results

### Step 2: Create Superior Content

Using your AI Content Engine, create a version of the competitor's most-linked content that is:
- 2x more comprehensive
- Updated with 2026 data
- Includes original visuals (use Canva or Midjourney)
- Features expert quotes (reach out to 5 industry experts on LinkedIn for a 1-sentence quote)

### Step 3: Automated Outreach

Create a Make.com scenario: "Link Building Outreach."

**Module 1: Google Sheets — Watch Rows**
- Spreadsheet: `[Client Name] Link Prospects`
- Filter: Status = "Not Contacted"

**Module 2: OpenAI — Personalize Outreach Email**
- Model: gpt-4o
- System prompt: "Write a brief, personalized outreach email for a link building campaign. The email should: 1) Reference something specific about the prospect's website or recent content, 2) Mention that you've created a superior resource on [TOPIC], 3) Suggest they link to it as an additional resource for their readers, 4) Keep it under 150 words, 5) Sound human, not salesy. No subject line — I'll add that separately."
- User message: Map the prospect's URL, their linked content, and your new content URL

**Module 3: Gmail — Send Email**
- To: Prospect's email
- Subject: "Resource for your [THEIR ARTICLE TITLE] article"
- Body: Map the AI-generated email
- Add a 3-day delay before follow-up

**Module 4: Google Sheets — Update Row**
- Set Status = "Contacted"
- Set Contact Date = today

{{% accent-box %}}HACK: Before reaching out to any prospect, link to their content from your client's article first. When you email them, mention the link: "I actually referenced your guide on [TOPIC] in our new article — your section on [SPECIFIC POINT] was excellent." This reciprocity increases response rates by 35-40% compared to cold outreach without a prior link.{{% /accent-box %}}

## Procedure 7.3: HARO and Digital PR Link Building

HARO (Help A Reporter Out) connects journalists with expert sources. Every quote you provide earns a backlink from a high-DR publication.

### Set Up HARO Monitoring

1. Go to connectively.us (formerly HARO) and create a free expert account
2. Select categories relevant to your client's industry
3. Check emails 3x daily (8 AM, 12 PM, 5 PM WAT) — journalists work on deadlines and the first qualified response wins

### AI-Powered Response System

When you see a relevant query, use this prompt in your SEO Content Engine:

```
A journalist is writing an article about [TOPIC]. They need an expert quote from a [CLIENT'S INDUSTRY] professional. Write a 2-3 sentence quote that: 1) Demonstrates deep expertise, 2) Includes a specific statistic or data point, 3) Offers a contrarian or unique perspective. Tone: authoritative but accessible.
```

Add the journalist to a Google Sheet called `HARO Tracker` with columns: Date, Query, Publication, DR, Response Sent, Link Earned, Link URL.

Expected conversion: 1 link per 8-10 responses. At 3 responses per day, you earn 2-3 high-DR backlinks per month with minimal effort.

## Check-In: Module 7 Complete

- [ ] Competitor backlink analysis completed in Ahrefs with prospect list exported
- [ ] Skyscraper content created for top link opportunity
- [ ] Link Building Outreach automation built and tested in Make.com
- [ ] HARO account created with relevant categories selected
- [ ] First 10 link prospect emails sent
- [ ] HARO response template created and first 3 responses submitted

6 checkmarks. Link building compounds — every link you build today makes every future piece of content rank faster. Start sending emails.

---

# MODULE 8: REPORTING & DASHBOARDS — THE VALUE PROOF

## Overview

Clients cancel SEO retainers when they cannot see the value. This module gives you a reporting system that makes progress visible, quantifiable, and undeniable. Every report you send is a retention tool. Every dashboard you build is a reason for the client to renew.

**Time to complete:** 4-5 hours to build templates, 1-2 hours per month per client

## Procedure 8.1: Build the Monthly SEO Report

Create a Google Slides template called `Monthly SEO Report — [Client Name]`. Use this structure:

**Slide 1: Executive Summary**
- Organic traffic: Previous month → Current month → % change
- Keyword rankings: Total tracked keywords in top 10, top 3, and position 1
- New backlinks acquired this month
- Domain Rating change
- Revenue attribution (if Google Analytics e-commerce is connected)

**Slide 2: Keyword Ranking Movement**
- Table: Top 10 keywords with position change arrows
- Color code: Green (improved), Yellow (no change), Red (declined)
- Highlight any keyword that reached page 1 this month

**Slide 3: Organic Traffic Trend**
- Line chart: 6-month organic traffic trend from Google Analytics
- Annotations for major changes (algorithm updates, content published, links earned)

**Slide 4: Content Performance**
- Top 5 performing articles by organic traffic
- Top 5 articles with the most ranking keyword gains
- Content published this month with initial performance metrics

**Slide 5: Backlink Profile**
- New referring domains this month
- DR distribution of new links
- Total backlink count trend

**Slide 6: Technical Health**
- Site Health Score trend (Semrush)
- Errors fixed this month vs. errors remaining
- Core Web Vitals status

**Slide 7: Next Month's Plan**
- 5-7 specific action items with expected outcomes
- Content planned for publication
- Link building targets

## Procedure 8.2: Build the Real-Time SEO Dashboard

Use Google Looker Studio (free) to create a live dashboard.

### Data Sources

Connect these data sources in Looker Studio:

1. **Google Analytics 4** — Organic traffic, sessions, bounce rate, conversions
2. **Google Search Console** — Impressions, clicks, average position, CTR
3. **Google Sheets** — Manual data entry for: keyword rankings (from Semrush), backlinks (from Ahrefs), Domain Rating

### Dashboard Layout

Create these sections on a single page:

**Section 1: KPI Cards (top row)**
- Organic Sessions (this month vs. last month)
- Organic Clicks (GSC)
- Average Position (GSC)
- Total Backlinks (Ahrefs)
- Domain Rating (Ahrefs)

**Section 2: Traffic Trend Chart**
- Line chart: Organic sessions over 12 months
- Data source: Google Analytics 4

**Section 3: Keyword Performance Table**
- Columns: Keyword, Position, Previous Position, Change, Search Volume, URL
- Data source: Google Sheets (updated by your Make.com rank tracker)

**Section 4: Top Pages by Organic Traffic**
- Bar chart: Top 10 pages by organic sessions
- Data source: Google Analytics 4

Share the dashboard with the client. Set it to "View" access so they can check progress anytime without asking you.

## Procedure 8.3: Automate Report Generation

Create a Make.com scenario: "Monthly SEO Report Generator."

**Module 1: Schedule Trigger** — 1st of every month at 7:00 AM WAT

**Module 2: Google Sheets — Get Range**
- Spreadsheet: `[Client Name] Rank Tracker`
- Range: All rows updated in the last 30 days

**Module 3: OpenAI — Generate Executive Summary**
- Model: gpt-4o
- System prompt: "You are an SEO analyst writing a monthly executive summary. Given keyword ranking changes, traffic data, and backlink data, write a concise 3-paragraph summary covering: 1) The biggest wins this month, 2) Areas of concern, 3) Recommended focus for next month. Use specific numbers. Be direct. No fluff."
- User message: Map the monthly data

**Module 4: Gmail — Send Report**
- To: Client email
- Subject: `[Client Name] SEO Performance Report — [Month Year]`
- Body: The AI-generated executive summary + link to the Looker Studio dashboard

**Module 5: Slack — Post Summary**
- Channel: `#seo-reports`
- Message: Monthly summary + link to full report

## Check-In: Module 8 Complete

- [ ] Monthly SEO Report template created in Google Slides (7 slides)
- [ ] Real-time Looker Studio dashboard connected to GA4 + GSC + Sheets
- [ ] Dashboard shared with client (View access)
- [ ] Monthly SEO Report Generator automation built and tested
- [ ] First monthly report sent to client (or test client)
- [ ] Executive summary quality verified — specific numbers, no fluff

6 checkmarks. The dashboard is your retention tool. Clients who can see their SEO data in real time are 3x less likely to cancel than clients who receive only monthly reports.

---

# MODULE 9: CLIENT ACQUISITION — THE MACHINE THAT FEEDS THE MACHINE

## Overview

You can do SEO. Now you need clients who will pay you to do it. This module gives you the exact scripts, templates, and processes for acquiring SEO clients consistently. No guessing. No hoping. Follow the procedures and clients will appear.

**Time to complete:** 5-6 hours to build assets, then 1-2 hours daily for outreach

## Procedure 9.1: Build Your SEO Demo Portfolio

Before you sell, you need proof. Your portfolio consists of:

1. **Your own agency website** — Optimized for "[city] SEO agency" and "SEO services Nigeria." This is your most powerful proof. If you cannot rank your own site, you cannot rank a client's.
2. **3 case study documents** — Even if you have not had paying clients yet, you can create case studies by:
   - Optimizing a friend's or family member's business website for free
   - Running a 90-day SEO experiment on a test domain
   - Documenting the process, data, and results in a professional format

Each case study must include:
- Client name and industry
- Starting metrics (traffic, rankings, Domain Rating)
- Strategy implemented (in 3-5 bullet points)
- Results achieved (traffic change %, new keywords ranked, revenue impact)
- Timeline
- Screenshots of Semrush/Ahrefs dashboards

## Procedure 9.2: The SEO Audit as a Sales Tool

The most effective client acquisition method for SEO agencies is the free mini-audit. You audit a prospect's website, find obvious problems, and present the findings. The prospect sees your expertise before they pay you a kobo.

### Build the Mini-Audit Template

Create a Loom video walkthrough (5-7 minutes) covering these exact points:

1. **Open Semrush** → Show their domain overview (traffic, keywords, backlinks)
2. **Show 3 keyword opportunities** — Keywords their competitors rank for but they do not
3. **Show 1 critical technical error** — Usually a crawl error, missing meta descriptions, or slow page speed
4. **Show their Domain Rating vs. competitors** — The gap is your sales hook
5. **Recommend 3 specific actions** — "If you fix X, Y, and Z, I estimate a 30-50% traffic increase within 90 days"

### Find Prospects for Mini-Audits

Use this process to build a list of 50 prospects:

1. Open Google. Search: "[industry] in [city]" (e.g., "real estate agencies in Lagos")
2. Open each result on page 1 and page 2
3. For each website, check their SEO quality by running the domain through Semrush:
   - Domain Rating under 30? → Good prospect (low authority = lots of room for improvement)
   - Fewer than 100 organic keywords? → Good prospect (low visibility = clear need)
   - Obvious technical errors on homepage? → Great prospect (you can show immediate value)

4. Add qualifying prospects to a Google Sheet: `SEO Prospect List`

| Column | Description |
|---|---|
| Business Name | From Google search results |
| Website | Domain URL |
| DR | From Semrush (under 30 = high priority) |
| Organic Keywords | From Semrush (under 100 = high priority) |
| Top Competitor | The business ranking #1 for their main keyword |
| Contact Email | From their website or LinkedIn |
| Contact Name | From LinkedIn or website team page |
| Audit Status | Not Started, Recorded, Sent, Replied, Meeting Booked |

Find 50 businesses. This takes 3-4 hours. Do it in one sitting.

## Procedure 9.3: The Outreach Scripts

### Cold Email Script 1: Mini-Audit Offer

**Subject line:** Found 3 SEO issues on [their domain]

**Body:**

> Hi [First Name],
>
> I was researching [their industry] businesses in [city] and noticed [their domain] has some SEO issues that are likely costing you traffic.
>
> Quick findings:
> - Your site has [X] pages with missing meta descriptions
> - [Competitor Name] is ranking for [Y] keywords that you're not targeting
> - Your Domain Rating is [Z], while the #1 ranking site in your niche is at [Z+20]
>
> I recorded a 5-minute walkthrough showing exactly what's happening and how to fix it: [Loom link]
>
> Worth a chat to discuss?
>
> [Your Name]

### Cold Email Script 2: Competitor Gap Approach

**Subject line:** [Competitor Name] is outranking you on [X] keywords

**Body:**

> Hi [First Name],
>
> I ran a competitive analysis between [their domain] and [Competitor Domain]. The gap is significant:
>
> - They rank for [X] keywords you don't
> - They have [Y] more referring domains
> - Their top pages get [Z] more organic visits per month
>
> I help [industry] businesses close this gap systematically — keyword research, content optimization, technical fixes, and link building.
>
> Can I send you a free mini-audit showing exactly where to start?
>
> [Your Name]

### Send Protocol

- Send 10 emails per day, maximum 15
- Space throughout the day: 3 at 9 AM, 4 at 12 PM, 3 at 4 PM WAT
- Track all sends in your Prospect List spreadsheet
- Follow up with non-responders after 4 days: "Hey [Name], just bumping this. Happy to send the mini-audit — no strings attached."
- Follow up again after 10 days: "Hey [Name], I know you're busy. Here's the thing — [Competitor Name] just published a new article targeting [keyword]. Every month you wait, they get harder to catch. Want me to send the audit?"

Expected results from 50 emails: 10-15 replies (20-30%), 5-7 meetings booked, 2-3 clients closed.

## Procedure 9.4: The Sales Call That Closes

When a prospect books a discovery call, follow this script:

**Minutes 0-5:** Introduce yourself briefly. Ask: "Before I show you anything, tell me — what does organic traffic mean for your business in terms of revenue? If you doubled your organic traffic tomorrow, what would that be worth?"

**Minutes 5-15:** Share your screen. Walk through the mini-audit Loom video live, pausing to explain implications. Show their competitor's Semrush data side by side. The visual gap between them and their competitor creates urgency.

**Minutes 15-25:** Ask: "If you could rank for those [X] keywords your competitor ranks for, what would that mean for your business?" Let them calculate the value. Then ask: "What's prevented you from investing in SEO before?" Listen for objections — budget, skepticism about SEO, bad experience with a previous agency.

**Minutes 25-30:** Present pricing. Use this framing:

"We offer three tiers. Most clients start with Growth because it includes everything you need for real results."

| Tier | Setup Fee | Monthly | What's Included |
|---|---|---|---|
| **Starter** | ₦300,000 | ₦500,000/mo | 4 articles/mo, basic on-page optimization, monthly technical audit, keyword tracking |
| **Growth** | ₦750,000 | ₦1,500,000/mo | 8 articles/mo, full on-page + technical SEO, link building (10 links/mo), weekly rank tracking, Looker Studio dashboard |
| **Enterprise** | ₦2,000,000 | ₦3,000,000/mo | 12+ articles/mo, everything in Growth + dedicated SEO strategist, daily monitoring, priority technical fixes, content strategy workshops, competitor warfare |

If they say yes, send the Paystack payment link immediately from your Notion Templates page. If they say "let me think about it," respond: "Totally understand. I'll send you a summary email with the audit link and pricing. What's the best way to follow up with you next week? And is there anyone else who needs to be part of that conversation?"

{{% accent-box %}}HACK: When presenting pricing, always show the Enterprise tier first, then Growth, then Starter. This is price anchoring. After seeing ₦3,000,000/month, ₦1,500,000/month feels reasonable. If you present Starter first, Growth feels expensive. The order of presentation determines the perception of value.{{% /accent-box %}}

## Check-In: Module 9 Complete

- [ ] Agency website live and optimized for target keywords
- [ ] 3 case study documents created (even from free/experimental work)
- [ ] Mini-audit template created and tested (Loom video walkthrough)
- [ ] 50 prospects in SEO Prospect List spreadsheet
- [ ] First batch of 10 outreach emails sent
- [ ] Sales call script memorized or printed and on your desk

6 checkmarks. The outreach emails are the hardest part. Most people overthink and under-send. Send the emails.

---

# MODULE 10: SCALING & TEAM BUILDING — FROM SOLO TO AGENCY

## Overview

Solo SEO operators hit a ceiling at ₦3,000,000-₦5,000,000/month in revenue. Breaking through requires systems and people. This module shows you exactly how and when to hire, what to delegate, and how to maintain margins as you grow from a one-person shop to a multi-client agency generating ₦15,000,000+/month.

**Time to complete:** Ongoing — implement as you hit each trigger point

## Procedure 10.1: The Hiring Roadmap

**When you have 3 clients (₦1,500,000-₦4,500,000 MRR):** Hire a Virtual Assistant (VA). Budget: ₦150,000-₦250,000/month (₦800-₦1,500/hour), 15-20 hours/week. The VA handles:

- Client communication (responding to emails, scheduling calls)
- Data entry (updating keyword trackers, logging audit results)
- Basic QC (running Semrush Site Audits, reporting errors to you)
- Social media posting for clients (scheduling content in Buffer)
- HARO monitoring and initial response drafting

**When you have 6 clients (₦4,500,000-₦9,000,000 MRR):** Hire a Junior SEO Specialist. Budget: ₦300,000-₦500,000/month, full-time. The Junior SEO handles:

- Keyword research execution (following your SOP from Module 3)
- Content brief generation (using your Custom GPT)
- On-page optimization implementation (following your checklist from Module 5)
- Content editing (first pass on AI-generated articles)
- Internal link building execution
- Monthly report generation (filling in your templates)

**When you have 10 clients (₦9,000,000-₦15,000,000 MRR):** Hire a Content Writer. Budget: ₦250,000-₦400,000/month, full-time. The Content Writer handles:

- AI content production (operating your SEO Content Engine Custom GPT)
- Human editing pass on all articles
- Client-specific voice and tone adaptation
- Content calendar management
- Content refresh execution

**When you have 12+ clients (₦15,000,000+ MRR):** Hire a Sales Representative. Budget: ₦400,000-₦600,000 base + 10% commission on first-year client revenue. The Sales Representative handles:

- Prospecting (building the 50-business list from Module 9)
- Mini-audit creation and outreach
- Discovery calls (following your script from Module 9)
- Pipeline management and follow-ups
- Proposal creation and sending

## Procedure 10.2: The SOP Library You Must Build

Every task in your agency must have a written SOP before you can delegate it. If you cannot hand a document to a Junior SEO and have them execute the task without asking you questions, you do not have an SOP — you have notes.

Build SOPs for these 15 critical processes:

| # | SOP Name | Module Reference | Estimated Build Time |
|---|---|---|---|
| 1 | Client Onboarding | Module 1 | 2 hours |
| 2 | Semrush Project Setup | Module 2 | 1.5 hours |
| 3 | Ahrefs Campaign Setup | Module 2 | 1.5 hours |
| 4 | Keyword Research (Semrush) | Module 3 | 2 hours |
| 5 | Keyword Research (Ahrefs) | Module 3 | 2 hours |
| 6 | Content Calendar Creation | Module 3 | 1 hour |
| 7 | Content Brief Generation | Module 4 | 1 hour |
| 8 | AI Content Production | Module 4 | 2 hours |
| 9 | On-Page Optimization Checklist | Module 5 | 2 hours |
| 10 | Internal Link Building | Module 5 | 1.5 hours |
| 11 | Technical SEO Audit | Module 6 | 2 hours |
| 12 | Link Building Outreach | Module 7 | 2 hours |
| 13 | HARO Response Protocol | Module 7 | 1 hour |
| 14 | Monthly Report Generation | Module 8 | 2 hours |
| 15 | Client Mini-Audit | Module 9 | 2 hours |

Total SOP build time: ~25 hours. This is your most important investment. Done correctly, these SOPs allow a Junior SEO to handle 80% of client work while you focus on sales and strategy.

{{% accent-box %}}HACK: Record yourself executing each SOP using Loom. A 15-minute video of you actually doing the work is worth more than a 5-page written document. Store Loom links inside each Notion SOP page. New hires watch the video first, then use the written SOP as a reference while they execute. This cuts training time from 2 weeks to 3 days.{{% /accent-box %}}

## Procedure 10.3: Margin Analysis at Scale

| Clients | MRR | Team Cost/mo | Tool Cost/mo | Net Profit/mo | Margin |
|---|---|---|---|---|---|
| 3 (Solo) | ₦1,500,000 | ₦0 | ₦200,000 | ₦1,300,000 | 87% |
| 6 (+ VA + Junior) | ₦4,500,000 | ₦750,000 | ₦300,000 | ₦3,450,000 | 77% |
| 10 (+ Writer) | ₦9,000,000 | ₦1,500,000 | ₦400,000 | ₦7,100,000 | 79% |
| 12 (+ Sales) | ₦12,000,000 | ₦2,100,000 | ₦500,000 | ₦9,400,000 | 78% |
| 15 (Full team) | ₦15,000,000 | ₦3,500,000 | ₦700,000 | ₦10,800,000 | 72% |

Margins compress slightly as you hire, but absolute profit increases dramatically. A 72% margin on ₦15,000,000 is ₦10,800,000/month — far more than a solo operator earning 87% on ₦1,500,000 (₦1,305,000/month).

## Procedure 10.4: The Scaling Roadmap — ₦0 to ₦15M/Month

### Phase 1: Foundation (Months 1-3)
- Complete all 10 modules of this playbook
- Land your first 2-3 clients using Module 9 outreach
- Deliver exceptional results (focus on quick wins: technical fixes, on-page optimization, easy keywords)
- Build your case studies from real client results
- Revenue target: ₦1,000,000-₦1,500,000 MRR

### Phase 2: Systematize (Months 4-6)
- Hire your VA
- Complete all 15 SOPs
- Automate reporting (Module 8)
- Increase outreach volume to 20 emails/day
- Revenue target: ₦3,000,000-₦4,500,000 MRR

### Phase 3: Scale (Months 7-12)
- Hire Junior SEO and Content Writer
- Expand to 8-10 clients
- Introduce Enterprise tier for larger clients
- Begin content marketing for your own agency (eat your own cooking)
- Revenue target: ₦7,500,000-₦12,000,000 MRR

### Phase 4: Dominate (Months 12-18)
- Hire Sales Representative
- Build referral partnerships with web development agencies and marketing consultants
- Launch a "done-with-you" SEO training product for ₦500,000/seat (additional revenue stream)
- Revenue target: ₦15,000,000+ MRR

{{% accent-box %}}HACK: The most overlooked growth lever is the "SEO for SEO agencies" strategy. Your own agency website should be your best case study. Target keywords like "SEO agency Lagos," "SEO services Nigeria," "best SEO company in [city]." When prospects search for an SEO agency and find YOU organically, the sale is 80% closed before the discovery call. A referral prospect has a 30% close rate. An inbound lead from organic search has a 60%+ close rate.{{% /accent-box %}}

## Check-In: Module 10 Complete

- [ ] Hiring roadmap saved in Notion with trigger points for each role
- [ ] VA job description drafted and ready to post on Upwork/LinkedIn
- [ ] All 15 SOP outlines created in Notion (even if not yet fully detailed)
- [ ] Margin analysis spreadsheet created with your actual numbers
- [ ] Scaling roadmap printed and posted where you see it daily
- [ ] You have identified your Phase 1 revenue target and written it down

6 checkmarks. The SOP outlines are the most critical — without them, you cannot delegate, and without delegation, you cannot scale past ₦5,000,000/month.

---

# THE PRICING TABLE — YOUR REVENUE ARCHITECTURE

This is the complete pricing structure for your AI SEO agency. Every client fits into one of these three tiers. Do not create custom pricing for individual clients — it destroys your margins and confuses your team. If a prospect needs something between tiers, upgrade them to the next tier and include the additional value.

| Feature | Starter | Growth | Enterprise |
|---|---|---|---|
| **Setup Fee** | ₦300,000 | ₦750,000 | ₦2,000,000 |
| **Monthly Retainer** | ₦500,000/mo | ₦1,500,000/mo | ₦3,000,000/mo |
| **Minimum Commitment** | 3 months | 6 months | 12 months |
| **Articles per Month** | 4 (1,500 words) | 8 (2,000 words) | 12+ (2,500 words) |
| **Keyword Tracking** | 50 keywords | 150 keywords | 500+ keywords |
| **Technical Audits** | Monthly | Bi-weekly | Weekly + real-time alerts |
| **On-Page Optimization** | Top 10 pages | Top 30 pages | All pages |
| **Link Building** | Not included | 10 links/month | 20+ links/month |
| **Reporting** | Monthly PDF | Looker Studio dashboard | Looker Studio + weekly calls |
| **Content Strategy** | Basic calendar | Full content strategy | Content strategy workshops |
| **Dedicated Specialist** | No | No | Yes |
| **Competitor Analysis** | Basic | Quarterly deep-dive | Monthly competitor warfare |
| **Response Time SLA** | 48 hours | 24 hours | 4 hours |
| **Your Cost/mo** | ~₦80,000 | ~₦250,000 | ~₦600,000 |
| **Your Margin/mo** | ~₦420,000 (84%) | ~₦1,250,000 (83%) | ~₦2,400,000 (80%) |

---

# FINAL CHECK-IN: PLAYBOOK COMPLETE

- [ ] Module 1: Foundation — All infrastructure configured and tested
- [ ] Module 2: Tech Stack — Semrush, Ahrefs, ChatGPT, Make.com connected
- [ ] Module 3: Keyword Research — 50+ keyword map built for first client
- [ ] Module 4: AI Content — Content pipeline producing 8+/10 SEO Writing Assistant scores
- [ ] Module 5: On-Page Optimization — All priority pages optimized
- [ ] Module 6: Technical SEO — All critical errors fixed, monitoring active
- [ ] Module 7: Link Building — Outreach system sending, HARO responses submitted
- [ ] Module 8: Reporting — Dashboard live, monthly report template ready
- [ ] Module 9: Client Acquisition — Outreach emails sent, calls booked
- [ ] Module 10: Scaling — SOPs outlined, hiring roadmap documented

**10 checkmarks.** If you have all 10, you have a complete AI SEO agency operating system. If you are missing any, go back and complete the module. Every module builds on the previous one. A missing module is a broken link in the chain.

This playbook is your operating system. Update it as you learn. Add procedures as you discover better methods. Remove procedures that prove ineffective. The document should evolve as your agency grows. But the framework — Foundation → Tools → Research → Content → On-Page → Technical → Links → Reporting → Acquisition → Scale — is the sequence that works. Follow it.
