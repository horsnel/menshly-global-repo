---
title: "The AI Lead Generation Business Playbook"
date: 2026-05-01
category: "Playbook"
price: "₦25,000"
readTime: "75 MIN"
excerpt: "The complete operating system for building an AI lead generation business from zero. 10 modules, 39 procedures, exact tool configurations, outreach scripts, three pricing tiers, and a scaling roadmap. From empty Apollo.io account to ₦10M/month in recurring revenue."
image: "/images/articles/playbooks/ai-lead-generation-playbook.png"
heroImage: "/images/heroes/playbooks/ai-lead-generation-playbook.png"
relatedOpportunity: "/opportunities/ai-lead-generation-agency-2026/"
relatedGuide: "/intelligence/build-ai-lead-generation-system/"
---

This is not a blog post condensed into a PDF. This is an operating system for building an AI-powered lead generation business. Every module contains exact procedures — not theories, not possibilities, not "consider doing X." You will do X, in this order, with these tools, and you will verify it worked before moving on.

**39 procedures. 10 modules. 75+ hours of reading and execution.**

---

# MODULE 1: FOUNDATION & BUSINESS MODEL — ALL CAPS

## Overview

Before you open a single tool, you will define the exact business you are building. An AI lead generation business sells qualified, scored, and enriched prospect data to companies that need pipeline. You do not sell "marketing." You do not sell "consulting." You sell verified contact records that convert to meetings. The AI layer is your competitive moat — it lets you produce 10x the output at 1/10th the labour cost of a traditional SDR team.

Your revenue model is simple: clients pay you a monthly retainer to deliver a guaranteed volume of qualified leads per month. You use Apollo.io for data, Make.com for automation, ChatGPT for scoring and personalization, and Notion as your operating dashboard. Total tooling cost at launch: under ₦150,000/month. First client pays for everything.

## Procedure 1.1: Define Your Service Tier Structure

Open a new Notion page. Title it "LeadGen OS — Pricing Matrix." Create a table with three rows and the following columns:

| Column | Starter | Growth | Enterprise |
|---|---|---|---|
| **Monthly Retainer** | ₦500,000 | ₦1,500,000 | ₦3,500,000 |
| **Qualified Leads/Month** | 150 | 500 | 1,500 |
| **Data Enrichment Fields** | 12 | 24 | 48 |
| **AI Scoring Model** | Basic (3 signals) | Advanced (8 signals) | Custom (15+ signals) |
| **Outreach Sequences** | 1 sequence, 4 emails | 3 sequences, 7 emails each | 5 sequences, 7 emails + LinkedIn |
| **CRM Integration** | Manual CSV export | Automated via Make.com | Real-time API sync |
| **Reporting Cadence** | Monthly PDF | Weekly Notion dashboard | Real-time Notion + Slack alerts |
| **Dedicated Analyst** | No | Part-time | Full-time |
| **Onboarding Fee** | ₦150,000 | ₦350,000 | ₦750,000 |

Save this page. You will reference it in every client proposal. Do not negotiate these numbers downward. The market rate for outsourced SDR teams in Lagos and London exceeds ₦2M/month for 200 leads. You are cheaper and better.

## Procedure 1.2: Register Your Business Infrastructure

Execute these steps in this exact order:

1. **Register a domain** at Namecheap (https://namecheap.com). Use a `.co` or `.io` domain. Suggested: `[yourbrand]leads.co`. Cost: ₦8,000/year.
2. **Set up Google Workspace** (https://workspace.google.com). Business Starter plan at $6/month per user. Create two users: `hello@[domain].co` and `outreach@[domain].co`. You will use `outreach@` for all cold email sending to protect domain reputation.
3. **Register a LinkedIn Sales Navigator account** (https://linkedin.com/sales). Core plan at $99/month. Link it to your personal LinkedIn profile.
4. **Open a Wise business account** (https://wise.com) for international invoicing. You will receive USD and GBP payments here. Conversion rate beats Nigerian banks by 3-5%.
5. **Create an Apollo.io account** (https://apollo.io). Free tier first — you will upgrade to Custom plan ($119/month) in Module 2.

Verify: You can log into all five platforms. Your domain resolves. Your Google Workspace inbox receives mail. Do not proceed until all five are confirmed.

## Procedure 1.3: Create Your Master Notion Workspace

Open Notion (https://notion.so). Create a new workspace titled "LeadGen OS." Inside this workspace, create the following pages using the "/page" command:

1. **Dashboard** — This is your home base. Pin it.
2. **Client Profiles** — Kanban board view.
3. **Prospect Database** — Table view. This will hold 50,000+ records.
4. **Outreach Tracker** — Table view linked to Prospect Database.
5. **Scoring Models** — Page with sub-pages for each client scoring prompt.
6. **Automation Logs** — Table view for Make.com execution records.
7. **Revenue Tracker** — Table view. Columns: Client, Tier, MRR, Start Date, Status.
8. **SOPs** — Page housing all standard operating procedures.
9. **Playbook Reference** — Duplicate this playbook for quick access.

Set the workspace icon to ⚡. Set the cover image to a solid black image (hex #000000). This is your command centre. Everything flows through here.

{{% accent-box %}}HACK: Create a Notion template button on your Dashboard page that generates a full client onboarding folder with one click. Use "/template" and pre-fill it with: Client Brief sub-page, ICP Document sub-page, Apollo Search Config sub-page, and Outreach Sequence sub-page. This saves 20 minutes per new client onboarding.{{% /accent-box %}}

## Check-In: Module 1 Complete

- [ ] Pricing matrix created in Notion with three tiers
- [ ] Domain registered and Google Workspace inbox receiving mail
- [ ] LinkedIn Sales Navigator active
- [ ] Wise business account opened
- [ ] Apollo.io account created (free tier)
- [ ] Master Notion workspace created with all 9 pages
- [ ] Dashboard page pinned and template button configured

---

# MODULE 2: TECH STACK CONFIGURATION — ALL CAPS

## Overview

You will now configure every tool in your stack. Do not skip settings. Do not leave defaults in place. Every misconfigured tool produces bad data. Bad data kills your credibility with clients. You will set up: Apollo.io (data source + email sender), Make.com (automation engine), ChatGPT Plus (scoring + personalization), Notion (dashboard + CRM), and Google Workspace (email infrastructure). Monthly cost at full configuration: ₦148,500.

## Procedure 2.1: Configure Apollo.io Custom Plan

Log into Apollo.io. Navigate to Settings (gear icon, top right). Execute each step:

1. **Upgrade to Custom Plan** — Click "Upgrade" in the top bar. Select "Custom" at $119/month ($87/month if paid annually). Confirm payment.
2. **Set Email Account** — Go to Settings → Email Accounts → Add Email. Enter `outreach@[domain].co`. Select Google OAuth. Grant permissions for send and reply tracking.
3. **Configure Sending Limits** — Go to Settings → Email Sending. Set:
   - Daily sending limit: **75 emails** per mailbox (safe for warm domain)
   - Minimum time between emails: **120 seconds**
   - Send window: **8:00 AM — 6:00 PM** (recipient's local timezone)
   - Track opens: **ON**
   - Track clicks: **ON**
   - Include unsubscribe link: **ON**
4. **Set Up Email Signatures** — Go to Settings → Signatures. Create signature:
   ```
   [Your Name]
   Lead Research Analyst | [Your Brand]
   [Domain].co
   ```
   No phone number. No social links. The signature should be minimal — this is cold outreach, not a business card.
5. **Verify Domain for Email** — Go to Settings → Email → Domain Verification. Apollo will give you three DNS records (1 CNAME, 2 TXT). Copy these exactly. Open your Namecheap dashboard → Domain → Advanced DNS. Add the three records. Wait 24-48 hours for propagation. Return to Apollo and click "Verify." Green checkmark = you are clear to send.

Do not send a single email until domain verification is complete. Sending from an unverified domain will destroy your sender reputation within 48 hours.

## Procedure 2.2: Configure Make.com Automation Engine

Log into Make.com (https://make.com). Create a new organization named "LeadGen OS." Inside it, create a new team named "Production." Execute:

1. **Upgrade Plan** — Select "Teams" plan at $16/month per user. You need 1 seat. This gives you 10,000 operations/month.
2. **Connect Apollo.io Module** — Click "Create a new scenario." Search for "Apollo.io" in the module library. Click "Create a connection." Enter your Apollo API key (found at Apollo.io → Settings → Integrations → API). Grant read + write permissions.
3. **Connect Notion Module** — In the same scenario, add a Notion module. Click "Create a connection." OAuth into your Notion workspace. Grant full page + database access.
4. **Connect Google Sheets Module** — Add a Google Sheets module. OAuth with your Google Workspace account. Grant read/write access to all spreadsheets.
5. **Connect ChatGPT Module** — Add an OpenAI (ChatGPT) module. Enter your OpenAI API key (from https://platform.openai.com/api-keys). Model selection: **gpt-4o** for scoring tasks.
6. **Connect Slack Module** (optional) — Add a Slack module if you use Slack for client comms. OAuth with your workspace.

Save this scenario as "Master Pipeline — DO NOT DELETE." You will build automation chains on top of this in later modules.

## Procedure 2.3: Configure ChatGPT Plus for Lead Scoring

Log into ChatGPT (https://chat.openai.com). You need a Plus subscription ($20/month). Execute:

1. **Upgrade to Plus** if not already on Plus. Confirm GPT-4o access.
2. **Create a Custom GPT** — Click "Explore GPTs" → "Create." Name it: "Lead Scoring Engine." Description: "Scores B2B leads based on ICP criteria. Input: prospect JSON. Output: score 0-100 with reasoning."
3. **Set Instructions** — Paste the following into the Instructions field:
   ```
   You are a B2B lead scoring engine. You receive a JSON object containing prospect data. You compare the prospect against the Ideal Customer Profile (ICP) criteria provided. You output a score from 0-100 and a 2-sentence reasoning.

   Scoring weights:
   - Job title match: 30%
   - Company size (employee count): 20%
   - Industry vertical match: 20%
   - Technology stack signals: 15%
   - Recent company activity (funding, hiring): 15%

   Score bands:
   - 80-100: HOT — Book meeting immediately
   - 60-79: WARM — Add to nurture sequence
   - 40-59: COOL — Add to long-term drip
   - 0-39: COLD — Discard

   Output format:
   {
     "score": <number>,
     "band": "<HOT|WARM|COOL|COLD>",
     "reasoning": "<2-sentence explanation>",
     "recommended_action": "<specific next step>"
   }
   ```
4. **Enable Web Browsing** — Toggle ON. This allows the GPT to research company data in real-time during scoring.
5. **Save** the Custom GPT. Copy its URL. You will use it in Make.com scenarios.

{{% accent-box %}}HACK: Create a second Custom GPT called "Outreach Copywriter" with instructions to generate 7-email cold sequences using the AIDA framework. Give it this constraint: "No email exceeds 90 words. Subject lines must be under 7 words. Never use the word 'excited' or 'opportunity.' Always open with a specific observation about the prospect's company." This produces copy that books 2-3x more meetings than generic ChatGPT output.{{% /accent-box %}}

## Procedure 2.4: Set Up Google Workspace Email Infrastructure

This step is critical for deliverability. A misconfigured email setup means your outreach lands in spam. Execute every step:

1. **Enable SPF Record** — In Namecheap DNS, add a TXT record:
   - Host: `@`
   - Value: `v=spf1 include:_spf.google.com include:mg.apollo.io ~all`
   - TTL: 1800
2. **Enable DKIM** — In Google Workspace Admin → Apps → Gmail → Authenticate Email. Generate DKIM for your domain. Copy the TXT record. Add it in Namecheap DNS:
   - Host: `google._domainkey`
   - Value: [paste from Google]
   - TTL: 1800
3. **Enable DMARC** — In Namecheap DNS, add a TXT record:
   - Host: `_dmarc`
   - Value: `v=DMARC1; p=none; rua=mailto:dmarc@[domain].co`
   - TTL: 1800
4. **Warm Up Your Domain** — Go to Apollo.io → Settings → Email → Warm-Up. Enable auto warm-up. Set to **ramp over 21 days** starting at 5 emails/day, increasing by 5 every 3 days until you hit 75/day. Do not skip this. A new domain that sends 75 emails on day 1 will be flagged as spam by Google and Microsoft within 72 hours.

Verify: Send a test email from `outreach@[domain].co` to your personal Gmail. Check the email headers (click "Show Original" in Gmail). Confirm SPF=PASS, DKIM=PASS, DMARC=PASS. All three must pass.

## Check-In: Module 2 Complete

- [ ] Apollo.io upgraded to Custom plan with verified domain
- [ ] Apollo email sending limits configured (75/day, 120s intervals)
- [ ] Make.com scenarios created with Apollo, Notion, Sheets, ChatGPT, and Slack connections
- [ ] Custom GPT "Lead Scoring Engine" created and saved
- [ ] Custom GPT "Outreach Copywriter" created and saved
- [ ] SPF, DKIM, and DMARC records all verified as PASS
- [ ] Apollo domain warm-up enabled with 21-day ramp

---

# MODULE 3: PROSPECT RESEARCH ENGINE — ALL CAPS

## Overview

This module builds the machine that finds your leads. You will construct Apollo.io saved searches for each client's Ideal Customer Profile (ICP), configure filter combinations that produce high-intent prospect lists, and automate the export pipeline into your Notion Prospect Database. By the end of this module, you will be able to generate 1,000 targeted prospects in under 15 minutes per client.

## Procedure 3.1: Build the ICP Document Template

Open Notion → Client Profiles page. Create a new template called "ICP Document." This template must contain these fields:

```
## Client ICP Document: [Client Name]

### Firmographics
- Target industries (max 5): [e.g., SaaS, FinTech, HealthTech, EdTech, E-commerce]
- Company size (employee range): [e.g., 50-500]
- Revenue range: [e.g., $5M-$50M ARR]
- Geography: [e.g., UK, Nigeria, UAE, US]
- Company type: [e.g., B2B SaaS, Agency, Enterprise]

### Buyer Persona
- Target job titles (max 10): [e.g., VP Sales, Head of Growth, CRO, Director of Revenue]
- Seniority level: [e.g., VP, Director, C-Level]
- Department: [e.g., Sales, Revenue Operations, Growth]
- Decision-making authority: [e.g., Budget holder, Influencer]

### Intent Signals
- Technology stack: [e.g., Uses Salesforce, Uses HubSpot, Uses ZoomInfo]
- Recent events: [e.g., Raised Series A, Hiring SDRs, Expanded to new market]
- Pain indicators: [e.g., Low SDR productivity, High CAC, Long sales cycles]

### Exclusion Criteria
- Companies to exclude: [e.g., Competitors, Existing vendors]
- Job titles to exclude: [e.g., Intern, Junior, Assistant]
- Industries to exclude: [e.g., Government, Military]
```

You will fill this document for every client before you run a single Apollo search. No ICP document = no search. This is non-negotiable.

## Procedure 3.2: Configure Apollo.io Saved Searches

Log into Apollo.io. Click "Search" in the left sidebar. You will build a search that maps directly to your ICP document. Follow this exact configuration:

**Filters Tab — People Search:**

1. **Job Titles** — Click "Job Title" filter. Select "Title Hierarchy." Enter your target titles from the ICP. Example:
   - Include: `VP Sales`, `Head of Growth`, `CRO`, `Director of Revenue`, `VP Business Development`
   - Exclude: `Intern`, `Junior`, `Assistant`, `Coordinator`
2. **Seniority Level** — Click "Seniority" filter. Check: `VP`, `Director`, `C-Level`, `Owner`. Uncheck all others.
3. **Company Size** — Click "Employees" filter. Set range per ICP. Example: `50-500`.
4. **Industry** — Click "Industry" filter. Select verticals from ICP. Apollo uses NAICS codes. For SaaS, select: `Software Publishers (5112)`, `Computer Systems Design (5415)`. For FinTech, add: `Financial Transactions Processing (52232)`.
5. **Location** — Click "Location" filter. Select countries from ICP geography. Use the "HQ Location" sub-filter for company headquarters.
6. **Technology Stack** — Click "Technologies" filter. This is a high-signal filter. Select technologies your ICP uses. Example for SaaS: `Salesforce`, `HubSpot`, `ZoomInfo`, `Outreach.io`, `Gong`.
7. **Intent Signals** — Click "Intent" filter (available on Custom plan). Select: `Hiring for Sales Roles`, `Recently Funded`, `Expanding Teams`.

**Sort Order:**
- Primary sort: **Intent Score** (descending) — this surfaces prospects actively buying
- Secondary sort: **Last Activity Date** (descending) — most recently active first

**Save This Search** — Click "Save Search." Name it: `[ClientName]_ICP_v1`. You will create version updates as you refine the ICP.

{{% accent-box %}}HACK: Always run two parallel searches per client — one narrow (3-4 filters, 200-500 results) and one broad (2 filters, 2,000-5,000 results). Score the narrow list first and send outreach immediately. Meanwhile, the broad list feeds your enrichment pipeline in Module 4. The narrow list books meetings this week; the broad list fills next month's pipeline.{{% /accent-box %}}

## Procedure 3.3: Build the Export-to-Notion Pipeline

You will automate the flow of prospects from Apollo to Notion using Make.com. Build this scenario:

**Scenario Name:** `Apollo → Notion Prospect Import`

**Trigger Module:** Apollo.io — "Search People"
- Configuration: Select your saved search `[ClientName]_ICP_v1`
- Schedule: Run every **6 hours**
- Limit: **100 records per run**

**Module 2:** Filter — Condition
- Condition: `email_status` equals `verified`
- This removes prospects with unverified or bounced emails

**Module 3:** ChatGPT — "Create a Completion"
- Model: `gpt-4o`
- Prompt:
  ```
  Score this prospect against the following ICP criteria:
  ICP: [Paste ICP summary from Notion]

  Prospect data:
  {{1.name}}, {{1.title}}, {{1.company_name}}, {{1.industry}}, {{1.employee_count}}, {{1.technologies}}

  Output JSON only: {"score": <0-100>, "band": "<HOT|WARM|COOL|COLD>", "reasoning": "<text>"}
  ```
- Temperature: 0.3 (low creativity, high consistency)

**Module 4:** Notion — "Create a Database Item"
- Database: Select your "Prospect Database" from Module 1
- Property mappings:
  - Name: `{{1.name}}`
  - Email: `{{1.email}}`
  - Title: `{{1.title}}`
  - Company: `{{1.company_name}}`
  - Industry: `{{1.industry}}`
  - Employees: `{{1.employee_count}}`
  - LinkedIn URL: `{{1.linkedin_url}}`
  - Score: `{{3.score}}`
  - Band: `{{3.band}}`
  - Reasoning: `{{3.reasoning}}`
  - Source: `Apollo — [ClientName]_ICP_v1`
  - Date Added: `{{now}}`
  - Status: `New`

**Module 5:** Google Sheets — "Add a Row"
- Spreadsheet: Create a new sheet called `[ClientName]_Prospect_Log`
- This is your backup. If Notion goes down (it happens), you have every record in Sheets.

Activate the scenario. Monitor the first 3 runs. Verify that records appear in both Notion and Google Sheets with scores populated. If any field is empty, check your mapping — the most common error is a mismatched field name between Apollo's output and Notion's property.

## Procedure 3.4: Build the Deduplication Check

Duplicates kill your credibility. Sending the same prospect two outreach emails from the same company is the fastest way to lose a client. Build this Make.com scenario:

**Scenario Name:** `Dedup — Notion Check`

**Trigger Module:** Notion — "Database Item Created" (on Prospect Database)

**Module 2:** Notion — "Search Database Items"
- Filter: `Email` equals `{{1.Email}}`
- This searches for existing records with the same email

**Module 3:** Router
- Path A: If `length(results)` > 1 → Notion "Update Database Item" → Set Status to `Duplicate`
- Path B: If `length(results)` = 1 → No action (this is the original record)

Run this scenario once. Then import a test batch of 50 prospects. Verify that any duplicates are flagged with "Duplicate" status in Notion.

## Check-In: Module 3 Complete

- [ ] ICP Document template created in Notion with all required fields
- [ ] At least one Apollo saved search configured per client ICP
- [ ] Narrow + broad search strategy implemented
- [ ] Apollo → Notion pipeline running every 6 hours with ChatGPT scoring
- [ ] Google Sheets backup populated for first client
- [ ] Deduplication scenario active and tested with 50+ records
- [ ] All duplicate records flagged in Notion

---

# MODULE 4: DATA ENRICHMENT PIPELINE — ALL CAPS

## Overview

Raw Apollo data gets you a name, title, company, and email. That is not enough to write personalized outreach. Enrichment adds the layer that makes your emails feel like they were written by someone who spent 30 minutes researching the prospect — except your AI did it in 3 seconds. This module builds the enrichment pipeline that adds 24-48 data points to every prospect record.

## Procedure 4.1: Configure Apollo Enrichment API

Apollo.io includes enrichment data natively, but you must unlock it. In Apollo:

1. Navigate to Settings → Integrations → API. Confirm your Custom plan includes "Enrichment API" access. It should show **unlimited enrichment credits**.
2. Copy your API key. Store it in your Notion SOPs page under "API Keys — DO NOT SHARE."
3. Test the enrichment endpoint. Open your terminal and run:
   ```bash
   curl -X POST https://api.apollo.io/v1/people/match \
     -H "Content-Type: application/json" \
     -H "Cache-Control: no-cache" \
     -d '{
       "api_key": "YOUR_API_KEY",
       "first_name": "John",
       "last_name": "Smith",
       "organization_name": "Acme Corp"
     }'
   ```
4. Verify the response includes: `email`, `phone`, `linkedin_url`, `employment_history`, `education`, `organization` (with `industry`, `estimated_arr`, `total_funding`, `tech_stack`).

If any of these fields are missing from the response, open Apollo support chat and request enrichment access escalation. This typically takes 24-48 hours.

## Procedure 4.2: Build the Multi-Source Enrichment Workflow

You will enrich each prospect with data from three sources: Apollo (firmographics + contact), LinkedIn (recent activity + role changes), and web scraping (company news + funding). Build this Make.com scenario:

**Scenario Name:** `Enrichment Pipeline v1`

**Trigger Module:** Notion — "Database Item Updated"
- Filter: Status equals `New` AND Score is greater than `40` (skip COLD prospects)

**Module 2:** HTTP — "Make a Request"
- URL: `https://api.apollo.io/v1/people/match`
- Method: POST
- Headers: `Content-Type: application/json`
- Body:
  ```json
  {
    "api_key": "YOUR_APOLLO_API_KEY",
    "first_name": "{{1.first_name}}",
    "last_name": "{{1.last_name}}",
    "organization_name": "{{1.company}}"
  }
  ```
- Parse response. Extract: `phone`, `employment_history`, `education`, `organization.industry`, `organization.estimated_arr`, `organization.total_funding`, `organization.tech_stack`

**Module 3:** ChatGPT — "Create a Completion"
- Model: `gpt-4o`
- Prompt:
  ```
  You are researching a B2B prospect. Based on the following data, generate:

  1. A one-line personalization hook referencing something specific about this person or company
  2. Three relevant pain points this person likely faces based on their role and company stage
  3. A suggested conversation starter for a cold email

  Prospect: {{1.name}}, {{1.title}} at {{1.company}}
  Industry: {{2.organization.industry}}
  Estimated Revenue: {{2.organization.estimated_arr}}
  Tech Stack: {{2.organization.tech_stack}}
  Previous Roles: {{2.employment_history}}
  Education: {{2.education}}

  Output as JSON:
  {
    "personalization_hook": "<string>",
    "pain_points": ["<string>", "<string>", "<string>"],
    "conversation_starter": "<string>"
  }
  ```
- Temperature: 0.4

**Module 4:** Notion — "Update Database Item"
- Update the same prospect record with new properties:
  - Phone: `{{2.phone}}`
  - Estimated ARR: `{{2.organization.estimated_arr}}`
  - Total Funding: `{{2.organization.total_funding}}`
  - Tech Stack: `{{2.organization.tech_stack}}`
  - Employment History: `{{2.employment_history}}`
  - Education: `{{2.education}}`
  - Personalization Hook: `{{3.personalization_hook}}`
  - Pain Points: `{{3.pain_points}}`
  - Conversation Starter: `{{3.conversation_starter}}`
  - Status: `Enriched`
  - Enrichment Date: `{{now}}`

Set this scenario to run every **2 hours**. Each run processes up to 50 enriched records. At 50 records per 2 hours, you can enrich 600 prospects per day on auto-pilot.

## Procedure 4.3: Build the Weekly Enrichment Audit

Every Monday at 9:00 AM, you will audit enrichment quality. Build this scenario:

**Scenario Name:** `Weekly Enrichment Audit`

**Trigger Module:** Schedule — Every Monday at 9:00 AM WAT

**Module 2:** Notion — "Search Database Items"
- Database: Prospect Database
- Filter: Status equals `Enriched` AND Enrichment Date is within last 7 days

**Module 3:** ChatGPT — "Create a Completion"
- Prompt:
  ```
  Audit these enriched prospect records. Identify:
  1. Records with empty Personalization Hook (enrichment failure)
  2. Records where Pain Points are generic (e.g., "increasing revenue" without specifics)
  3. Records where the Conversation Starter is clearly templated and not personalized

  Data: {{2}}

  Output: List of record IDs that need re-enrichment, with the specific issue for each.
  ```

**Module 4:** Slack (or Notion) — Send the audit report to your #ops channel

Fix any flagged records by re-running enrichment manually or adjusting your prompts. Target: fewer than 5% of enriched records flagged in any given week.

{{% accent-box %}}HACK: Add a "Last LinkedIn Post" field to your enrichment pipeline. Use LinkedIn Sales Navigator to scrape the prospect's most recent post or activity. Feed this into ChatGPT to generate an opening line that references their actual content. Example: "Saw your post about scaling SDR teams from 3 to 15 — we built a system that does exactly that, but with AI instead of headcount." Response rates on these emails are 3x higher than standard personalization.{{% /accent-box %}}

## Check-In: Module 4 Complete

- [ ] Apollo Enrichment API tested and returning full data
- [ ] Multi-source enrichment workflow running every 2 hours
- [ ] Prospect records enriched with 12+ new fields per record
- [ ] Personalization hooks, pain points, and conversation starters generated for each prospect
- [ ] Weekly enrichment audit scenario active
- [ ] Audit flags fewer than 5% of records per week
- [ ] At least 500 prospects enriched for first client

---

# MODULE 5: AI SCORING & QUALIFICATION — ALL CAPS

## Overview

Not every lead is worth your client's time. A VP of Sales at a 50-person SaaS company that just raised Series A is worth 50x more than a Sales Manager at a 200-person company that hasn't raised in 5 years. Scoring is how you separate the signal from the noise. This module builds a multi-signal scoring model that ranks every prospect from 0-100 and assigns an action category.

## Procedure 5.1: Define Scoring Signals and Weights

Open your Notion "Scoring Models" page. Create a sub-page for each client. For your first client, define these signals and weights:

| Signal | Weight | Data Source | Scoring Logic |
|---|---|---|---|
| Job Title Match | 30% | Apollo | Exact match to ICP titles = 30pts. Adjacent title = 20pts. No match = 0pts |
| Company Size Fit | 20% | Apollo | Within ICP employee range = 20pts. Adjacent range = 10pts. Outside = 0pts |
| Industry Match | 20% | Apollo | Exact NAICS match = 20pts. Adjacent industry = 10pts. Unrelated = 0pts |
| Technology Signals | 15% | Apollo Enrichment | Uses ICP-listed tech = 15pts. Uses competing tech = 8pts. No signal = 0pts |
| Recent Activity | 15% | Apollo Intent + Web | Funded in last 6 months = 15pts. Hiring for relevant roles = 10pts. No signal = 0pts |

Total possible score: 100. Score bands:
- **80-100 (HOT):** Immediate outreach. Add to priority sequence. Client books meeting within 48 hours.
- **60-79 (WARM):** Standard outreach. Add to main sequence. Client books meeting within 7 days.
- **40-59 (COOL):** Long-term nurture. Add to monthly drip. Do not assign SDR time.
- **0-39 (COLD):** Discard. Remove from active pipeline. Archive in Notion.

## Procedure 5.2: Build the Scoring Automation

You already built a basic scoring step in Procedure 3.3. Now you will upgrade it to a dedicated scoring pipeline with multi-signal evaluation. Build this Make.com scenario:

**Scenario Name:** `Lead Scoring Pipeline v2`

**Trigger Module:** Notion — "Database Item Updated"
- Filter: Status equals `Enriched`

**Module 2:** ChatGPT — "Create a Completion" (using your Lead Scoring Engine Custom GPT)
- Model: `gpt-4o`
- System Prompt:
  ```
  You are a B2B lead scoring engine with 15 years of SDR operations experience.

  SCORING RULES:
  1. Job Title Match (0-30): Compare the prospect's title against this ICP list: {{1.icp_titles}}. Exact match = 30. Partial/adjacent = 15-20. No match = 0.
  2. Company Size Fit (0-20): ICP range: {{1.icp_employee_range}}. Within range = 20. ±50% of range = 10. Outside = 0.
  3. Industry Match (0-20): ICP industries: {{1.icp_industries}}. Exact = 20. Adjacent = 10. Unrelated = 0.
  4. Technology Signals (0-15): ICP tech: {{1.icp_tech}}. Uses listed tech = 15. Uses competitor = 8. No data = 0.
  5. Recent Activity (0-15): Check for: funding in last 6 months, hiring for relevant roles, product launch, market expansion. Multiple signals = 15. Single signal = 8. No signal = 0.

  Prospect data:
  Name: {{1.name}}
  Title: {{1.title}}
  Company: {{1.company}}
  Industry: {{1.industry}}
  Employees: {{1.employees}}
  Tech Stack: {{1.tech_stack}}
  Estimated ARR: {{1.estimated_arr}}
  Total Funding: {{1.total_funding}}

  OUTPUT FORMAT (JSON only):
  {
    "score": <0-100>,
    "band": "<HOT|WARM|COOL|COLD>",
    "title_score": <0-30>,
    "size_score": <0-20>,
    "industry_score": <0-20>,
    "tech_score": <0-15>,
    "activity_score": <0-15>,
    "reasoning": "<2 sentences>",
    "recommended_action": "<specific next step>"
  }
  ```
- Temperature: 0.2 (maximum consistency)

**Module 3:** Notion — "Update Database Item"
- Update properties:
  - Score: `{{2.score}}`
  - Band: `{{2.band}}`
  - Title Score: `{{2.title_score}}`
  - Size Score: `{{2.size_score}}`
  - Industry Score: `{{2.industry_score}}`
  - Tech Score: `{{2.tech_score}}`
  - Activity Score: `{{2.activity_score}}`
  - Reasoning: `{{2.reasoning}}`
  - Recommended Action: `{{2.recommended_action}}`
  - Status: `Scored`
  - Scoring Date: `{{now}}`

**Module 4:** Router
- Path A: Band = `HOT` → Notion update: Priority = `P1`
- Path B: Band = `WARM` → Notion update: Priority = `P2`
- Path C: Band = `COOL` → Notion update: Priority = `P3`
- Path D: Band = `COLD` → Notion update: Status = `Archived`

Run this scenario for your existing enriched prospects. Verify that every record now has a composite score, sub-scores, and an action recommendation.

## Procedure 5.3: Build the Score Calibration Routine

Your AI scoring model is only as good as its calibration. You will check calibration weekly. Build this process:

1. Every Friday, export the last 50 prospects that received outreach (from your Outreach Tracker in Notion).
2. For each prospect, check: Did they respond? Did they book a meeting?
3. Calculate the response rate by score band:
   - HOT response rate target: **>15%**
   - WARM response rate target: **>8%**
   - COOL response rate target: **>3%**
4. If any band underperforms by more than 50% of target, adjust the scoring weights. Example: If HOT response rate is 5% (target 15%), your model is too generous with HOT scores. Increase the threshold for each signal by 20%.

Document every calibration change in your Notion "Scoring Models" page with the date, the change, and the rationale.

## Check-In: Module 5 Complete

- [ ] Scoring signals and weights documented for first client
- [ ] Lead Scoring Pipeline v2 scenario running with 5-signal evaluation
- [ ] Every enriched prospect has composite score + sub-scores
- [ ] HOT/WARM/COOL/COLD band assignment automated
- [ ] COLD prospects archived automatically
- [ ] Score calibration routine documented and scheduled for every Friday
- [ ] Response rate by band tracked in Notion

---

# MODULE 6: OUTREACH SEQUENCES — ALL CAPS

## Overview

Your outreach is the point where your pipeline produces revenue or dies. This module builds email sequences that convert scored prospects into booked meetings. You will write three sequence types: Hot Lead Blitz (HOT prospects, 4 emails over 10 days), Warm Nurture (WARM prospects, 7 emails over 30 days), and Cool Drip (COOL prospects, 4 emails over 60 days). Every sequence is loaded into Apollo.io and triggered automatically based on the Band field in your Notion database.

## Procedure 6.1: Write the Hot Lead Blitz Sequence

Open your Outreach Copywriter Custom GPT. Generate the following 4-email sequence. Replace all bracketed text with client-specific content.

**Email 1 — The Observation Opener (Day 1, 9:00 AM recipient time)**
```
Subject: {{company}}'s Q1 hiring signal

{{first_name}},

Noticed {{company}} just opened 3 SDR roles on LinkedIn. Most teams I work with are hiring SDRs because their current reps spend 60% of time on research instead of selling.

We built an AI pipeline that delivers 500 scored, enriched leads per month — the research work your SDRs are doing manually takes our system 4 minutes.

Worth a 12-minute call this week?

[Your Name]
```

**Email 2 — The Proof Point (Day 3, 10:30 AM)**
```
Subject: re: {{company}}'s Q1 hiring signal

{{first_name}},

Quick follow-up with a number: our clients see a 3x increase in qualified meetings per SDR within 60 days of switching to AI-scored leads.

One client — a 120-person SaaS company — went from 8 meetings/month to 27 with the same team size.

The math: if your new SDRs each book 3 more meetings per month at your average deal size, that's [calculated revenue impact] in new pipeline per quarter.

Open to seeing how it works?

[Your Name]
```

**Email 3 — The Case Study (Day 6, 2:00 PM)**
```
Subject: how [similar company] solved this

{{first_name}},

[Similar Company] had the same challenge — 5 SDRs doing manual research, each producing 2-3 qualified leads per day.

After implementing our system:
- Lead volume: 2-3/day → 25/day per SDR
- Meeting rate: 8% → 22%
- Cost per qualified lead: ₦45,000 → ₦3,200

Happy to walk you through the exact setup.

[Your Name]
```

**Email 4 — The Respectful Close (Day 10, 9:00 AM)**
```
Subject: closing the loop

{{first_name}},

I've reached out a few times about helping {{company}} scale lead generation with AI.

If the timing isn't right, no worries — I'll move on. If it is, reply with "yes" and I'll send over 2 time slots.

Either way, good luck with the SDR hiring.

[Your Name]
```

{{% accent-box %}}HACK: The subject line in Email 1 uses the prospect's company name, not a generic hook. Open rates on company-name subject lines average 47% vs. 28% for "Quick question" or "Introduction." Never use a subject line that could apply to 100 different people. If you can't make it specific to the recipient, rewrite it.{{% /accent-box %}}

## Procedure 6.2: Write the Warm Nurture Sequence

This sequence runs for 30 days with 7 touchpoints. The tone shifts from direct to educational.

**Email 1 — The Insight Drop (Day 1, 9:00 AM)**
```
Subject: {{industry}} lead gen benchmark

{{first_name}},

Pulled some data from our pipeline: {{industry}} companies with 50-500 employees spend an average of ₦2.8M/month on lead generation (SDR salaries + tools + data).

The top 10% spend ₦1.2M and produce 4x the pipeline.

The difference? AI-scored targeting vs. spray-and-pray.

I put together a one-page benchmark for {{industry}} — want me to send it over?

[Your Name]
```

**Email 2 — The Benchmark (Day 4, 11:00 AM)**
```
Subject: that benchmark for {{first_name}}

{{first_name}},

Here's the one-pager I mentioned — [link to Notion-hosted benchmark page].

Two things stand out for companies like {{company}}:
1. Your peer group averages 340 qualified leads/month
2. The AI-powered cohort averages 890

The gap is almost entirely in the scoring and enrichment layer, not headcount.

Worth discussing?

[Your Name]
```

**Email 3 — The Question (Day 8, 2:30 PM)**
```
Subject: quick question on {{company}}'s pipeline

{{first_name}},

Curious — what's your current cost per qualified lead?

Most {{industry}} companies I talk to are at ₦35,000-₦65,000. The ones using AI scoring are at ₦2,500-₦8,000.

If you're on the high end, there's a straightforward fix.

[Your Name]
```

**Email 4 — The Social Proof (Day 12, 10:00 AM)**
```
Subject: {{company}} + AI lead gen

{{first_name}},

Three companies in {{industry}} signed with us this quarter. Common thread: they all had SDR teams doing manual research and wanted to redeploy that time to closing.

Results after 90 days:
- Client A: 340 → 720 qualified leads/month
- Client B: ₦52,000 → ₦4,100 cost per lead
- Client C: 3 → 11 meetings per SDR per week

I can show you the exact workflow. 15 minutes?

[Your Name]
```

**Email 5 — The Value Add (Day 17, 9:30 AM)**
```
Subject: free lead audit for {{company}}

{{first_name}},

I ran a quick scan on {{company}}'s public footprint — your tech stack, recent hires, and market positioning.

Based on what I see, you should be generating 400+ qualified leads/month in {{industry}}. If you're below that, the gap is in targeting, not effort.

I'll send you a 1-page audit with 3 specific recommendations — no strings attached. Reply "send it" and it's yours.

[Your Name]
```

**Email 6 — The Gentle Nudge (Day 23, 1:00 PM)**
```
Subject: still interested in better leads?

{{first_name}},

I know things get busy. Just wanted to leave this here: if {{company}} ever wants to test AI-powered lead generation, we offer a 2-week pilot — 50 scored leads, no commitment.

Save my email and reach out whenever the timing works.

[Your Name]
```

**Email 7 — The Breakup (Day 30, 9:00 AM)**
```
Subject: moving on

{{first_name}},

I've reached out a few times and I don't want to clutter your inbox.

If AI-powered lead gen becomes a priority for {{company}}, you know where to find me.

Good luck with everything.

[Your Name]
```

## Procedure 6.3: Load Sequences into Apollo.io

You will now load both sequences into Apollo's email sequencing tool. Execute:

1. **Navigate to Sequences** — Click "Sequences" in Apollo's left sidebar. Click "Create Sequence."
2. **Create Hot Lead Blitz** — Name: `Hot Lead Blitz — [ClientName]`. Set:
   - Sequence type: **Automated**
   - Sending schedule: **Business days only**
   - Timezone: **Recipient's local timezone**
   - Stop on reply: **ON**
   - Stop on meeting booked: **ON**
   - Add all 4 emails from Procedure 6.1. Set the delay between each email per the schedule.
3. **Create Warm Nurture** — Name: `Warm Nurture — [ClientName]`. Same settings. Add all 7 emails from Procedure 6.2.
4. **Create Cool Drip** — Name: `Cool Drip — [ClientName]`. This is a 4-email sequence sent over 60 days (Day 1, Day 20, Day 40, Day 60). Use simplified versions of the Warm Nurture emails, stripped to 60 words maximum. Tone: informational, zero pressure.
5. **Set Up Unsubscribe Handling** — In each sequence, enable "Auto-handle unsubscribes." Apollo will automatically remove anyone who clicks unsubscribe from all future sequences.

## Procedure 6.4: Build the Auto-Enrollment Workflow

You will automate the process of adding scored prospects to the correct sequence. Build this Make.com scenario:

**Scenario Name:** `Auto-Enroll to Apollo Sequence`

**Trigger Module:** Notion — "Database Item Updated"
- Filter: Status equals `Scored`

**Module 2:** Router
- Path A: Band = `HOT` → Apollo.io module: "Add to Sequence"
  - Sequence: `Hot Lead Blitz — [ClientName]`
  - Sender: `outreach@[domain].co`
  - Template variables: Map `first_name`, `company`, `industry`, `similar_company` from Notion fields
- Path B: Band = `WARM` → Apollo.io module: "Add to Sequence"
  - Sequence: `Warm Nurture — [ClientName]`
  - Same variable mappings
- Path C: Band = `COOL` → Apollo.io module: "Add to Sequence"
  - Sequence: `Cool Drip — [ClientName]`
  - Same variable mappings
- Path D: Band = `COLD` → No action (already archived in Module 5)

**Module 3:** Notion — "Update Database Item"
- Update Status to `In Sequence`
- Update Sequence Name: `[sequence name]`
- Update Enrollment Date: `{{now}}`

**Module 4:** Slack — Send notification: `"🟢 {{1.name}} ({{1.company}}) enrolled in {{2.sequence_name}}"`

{{% accent-box %}}HACK: Set up A/B testing on every subject line. In Apollo sequences, click "Add Variant" on Email 1. Write two subject lines — one company-name-based and one question-based. Run each to 50 prospects. After 200 total sends, check open rates. The winner becomes your default. Never guess at subject lines again — let data decide.{{% /accent-box %}}

## Check-In: Module 6 Complete

- [ ] Hot Lead Blitz sequence written and loaded in Apollo (4 emails)
- [ ] Warm Nurture sequence written and loaded in Apollo (7 emails)
- [ ] Cool Drip sequence written and loaded in Apollo (4 emails)
- [ ] Auto-enrollment workflow routing prospects to correct sequence by band
- [ ] Template variables mapped from Notion to Apollo
- [ ] Unsubscribe handling enabled on all sequences
- [ ] A/B testing configured on at least Email 1 subject lines
- [ ] First batch of 50+ prospects enrolled and sending

---

# MODULE 7: CRM INTEGRATION & WORKFLOW AUTOMATION — ALL CAPS

## Overview

Your client's CRM is where leads become revenue. If your leads sit in your Notion database and never reach the client's CRM, you have no proof of value and no retention. This module builds the bridge between your system and the client's CRM. You will integrate with HubSpot, Salesforce, and Pipedrive — the three CRMs you will encounter in 90% of client engagements.

## Procedure 7.1: Build the HubSpot Integration

HubSpot is the most common CRM for your target clients (mid-market companies with 50-500 employees). Build this workflow:

**Prerequisites:** Ask your client to create a HubSpot user for you with "Sales Pro" permissions. You need: contact creation, deal creation, and list management access.

**Make.com Scenario:** `HubSpot Sync — [ClientName]`

**Trigger Module:** Notion — "Database Item Updated"
- Filter: Status equals `In Sequence`

**Module 2:** HubSpot — "Create or Update Contact"
- Email: `{{1.email}}`
- First Name: `{{1.first_name}}`
- Last Name: `{{1.last_name}}`
- Job Title: `{{1.title}}`
- Company: `{{1.company}}`
- Phone: `{{1.phone}}`
- Custom Property — Lead Score: `{{1.score}}`
- Custom Property — Lead Band: `{{1.band}}`
- Custom Property — Lead Source: `AI LeadGen — [YourBrand]`
- Custom Property — Personalization Hook: `{{1.personalization_hook}}`
- Custom Property — Pain Points: `{{1.pain_points}}`

**Module 3:** HubSpot — "Add Contact to List"
- List: `AI Generated Leads — [ClientName]`
- This creates a dedicated list in HubSpot so the client can filter and view only your leads

**Module 4:** Router — Based on Band:
- Path A: Band = `HOT` → HubSpot "Create Deal"
  - Deal Name: `[Company] — AI LeadGen HOT`
  - Deal Stage: `Qualified Lead`
  - Amount: Leave blank (client sets this)
  - Probability: `60%`
- Path B: Band = `WARM` → HubSpot "Create Deal"
  - Deal Stage: `Lead`
  - Probability: `30%`
- Path C: Band = `COOL` → No deal creation (too early)

**Module 5:** Notion — "Update Database Item"
- Update Status to `Synced to CRM`
- Update CRM ID: `{{2.id}}`

## Procedure 7.2: Build the Salesforce Integration

Salesforce clients are typically larger (200-1000 employees). The integration is more complex but follows the same pattern.

**Prerequisites:** Client creates a Salesforce user with "Sales Cloud" permissions. You need: Lead creation, Contact creation, and Opportunity creation access. Also request API access and a Security Token.

**Make.com Scenario:** `Salesforce Sync — [ClientName]`

**Trigger Module:** Notion — "Database Item Updated"
- Filter: Status equals `In Sequence` AND Client CRM equals `Salesforce`

**Module 2:** Salesforce — "Create a Lead"
- LastName: `{{1.last_name}}`
- FirstName: `{{1.first_name}}`
- Email: `{{1.email}}`
- Title: `{{1.title}}`
- Company: `{{1.company}}`
- Phone: `{{1.phone}}`
- LeadSource: `AI LeadGen — [YourBrand]`
- Custom Field — Lead_Score__c: `{{1.score}}`
- Custom Field — Lead_Band__c: `{{1.band}}`
- Custom Field — Personalization_Hook__c: `{{1.personalization_hook}}`
- Description: `Pain Points: {{1.pain_points}} | Reasoning: {{1.reasoning}} | Recommended Action: {{1.recommended_action}}`

**Module 3:** Router — Based on Band:
- Path A: Band = `HOT` → Salesforce "Create Opportunity"
  - Name: `[Company] — AI LeadGen`
  - Stage: `Prospecting`
  - Probability: `60%`
  - LeadSource: `AI LeadGen`
- Path B: All others → No opportunity creation

**Module 4:** Notion — "Update Database Item"
- Status: `Synced to CRM`
- CRM ID: `{{2.id}}`

## Procedure 7.3: Build the Reply Handling Automation

When a prospect replies to your Apollo sequence, you need to: (1) log the reply, (2) notify the client, (3) update the lead status, and (4) stop the sequence. Build this:

**Make.com Scenario:** `Reply Handler`

**Trigger Module:** Apollo.io — "Email Replied"
- This webhook fires when any prospect replies to a sequence email

**Module 2:** Notion — "Search Database Items"
- Filter: Email equals `{{1.prospect_email}}`

**Module 3:** Notion — "Update Database Item"
- Update Status to `Replied`
- Update Reply Date: `{{now}}`
- Update Reply Content: `{{1.reply_body}}`

**Module 4:** Router — Based on reply sentiment:
- Path A: Reply contains positive signals ("yes", "sure", "let's talk", "meeting", "interested") →
  - Notion update: Status = `Meeting Requested`
  - Slack notification to client: `"🟢 {{1.prospect_name}} ({{1.company}}) replied positively — meeting requested"`
  - Apollo.io: "Remove from Sequence" (stop sending emails)
- Path B: Reply contains negative signals ("not interested", "remove", "unsubscribe", "stop") →
  - Notion update: Status = `Declined`
  - Apollo.io: "Remove from Sequence"
- Path C: Reply is neutral/unclear →
  - Notion update: Status = `Replied — Needs Review`
  - Slack notification: `"🟡 {{1.prospect_name}} replied — needs manual review"`

## Procedure 7.4: Build the Meeting Booked Tracker

When a meeting is booked (either by the prospect or by your client's team), you need to track it for reporting and billing purposes.

**Make.com Scenario:** `Meeting Tracker`

**Trigger Module:** HubSpot or Salesforce — "Deal Stage Updated" (to "Meeting Booked" or equivalent)

**Module 2:** Notion — "Search Database Items"
- Filter: CRM ID equals `{{1.contact_id}}`

**Module 3:** Notion — "Update Database Item"
- Status: `Meeting Booked`
- Meeting Date: `{{1.meeting_date}}`
- Meeting Type: `{{1.meeting_type}}`

**Module 4:** Google Sheets — "Add a Row"
- Spreadsheet: `[ClientName]_Meeting_Log`
- Columns: Date, Prospect, Company, Band, Meeting Date, Source Sequence

This spreadsheet is your billing proof. At the end of each month, you will count meetings booked and compare against your SLA. If you promised 15 meetings for a Growth-tier client and delivered 18, you highlight this in your monthly report.

## Check-In: Module 7 Complete

- [ ] HubSpot integration scenario tested with 10 test contacts
- [ ] Salesforce integration scenario tested with 5 test contacts (or mock data)
- [ ] Pipedrive integration built (follow HubSpot pattern with Pipedrive module)
- [ ] Reply handler scenario active and routing to correct paths
- [ ] Meeting tracker logging to Google Sheets
- [ ] All synced contacts appear in client CRM with custom fields populated
- [ ] Status updates flowing back from CRM to Notion

---

# MODULE 8: ANALYTICS & REPORTING — ALL CAPS

## Overview

Clients cancel when they cannot see value. Your reporting is your retention strategy. This module builds automated dashboards and weekly/monthly reports that prove ROI in numbers the client's CFO can validate. Every metric ties back to revenue.

## Procedure 8.1: Build the Notion Analytics Dashboard

Open Notion → Dashboard page. Add the following sections using the "/database" and "/callout" commands:

**Section 1: Pipeline Volume**
- Linked database view: Prospect Database
- Group by: Band
- Filter: Client = [Current Client]
- Show: Total count per band

**Section 2: Outreach Performance**
- Linked database view: Outreach Tracker
- Group by: Sequence Name
- Calculate: Emails sent, Opens, Clicks, Replies, Meetings booked
- Add a "/formula" property: `Reply Rate = Replies / Emails Sent`
- Add a "/formula" property: `Meeting Rate = Meetings / Replies`

**Section 3: Lead Quality Distribution**
- Create a "/table view" of Prospect Database
- Add a "/formula" property: `Score Bucket = if(score >= 80, "HOT", if(score >= 60, "WARM", if(score >= 40, "COOL", "COLD")))`
- Group by Score Bucket
- Show: Count per bucket

**Section 4: Revenue Metrics**
- Linked database view: Revenue Tracker
- Show: Total MRR, Client count, Average revenue per client
- Add a "/callout" block: "Target: ₦10M MRR by Month 12"

## Procedure 8.2: Build the Weekly Automated Report

Every Friday at 5:00 PM WAT, your system will generate and send a performance report to the client. Build this Make.com scenario:

**Scenario Name:** `Weekly Report — [ClientName]`

**Trigger Module:** Schedule — Every Friday at 5:00 PM WAT

**Module 2:** Notion — "Search Database Items" (Prospect Database)
- Filter: Client = [ClientName] AND Date Added is within last 7 days
- Output: Count of new prospects by band

**Module 3:** Notion — "Search Database Items" (Outreach Tracker)
- Filter: Client = [ClientName] AND Enrollment Date is within last 7 days
- Output: Count of emails sent, opens, replies, meetings booked

**Module 4:** ChatGPT — "Create a Completion"
- Prompt:
  ```
  Generate a weekly lead generation report for [ClientName]. Use this data:

  New prospects this week: {{2.count}} (HOT: {{2.hot_count}}, WARM: {{2.warm_count}}, COOL: {{2.cool_count}})
  Emails sent: {{3.emails_sent}}
  Open rate: {{3.open_rate}}%
  Reply rate: {{3.reply_rate}}%
  Meetings booked: {{3.meetings_booked}}

  Format as a concise business email with:
  1. Executive summary (2 sentences)
  2. Key metrics in bullet format
  3. Notable wins (specific prospects who replied or booked)
  4. Recommendations for next week (2-3 specific actions)

  Tone: Professional, data-driven, no fluff.
  ```

**Module 5:** Gmail — "Send an Email"
- To: `[client_email]`
- CC: `[your_email]`
- Subject: `Weekly Lead Report — [ClientName] — Week of [date]`
- Body: `{{4.output}}`

This report runs on autopilot. You never miss a Friday. The client always knows what is happening.

## Procedure 8.3: Build the Monthly Business Review (MBR) Report

The MBR is your retention tool. It is a deeper analysis sent on the 1st of every month. Build this scenario:

**Scenario Name:** `MBR Report — [ClientName]`

**Trigger Module:** Schedule — 1st of every month at 10:00 AM WAT

**Module 2:** Google Sheets — "Get Range Values"
- Spreadsheet: `[ClientName]_Meeting_Log`
- Range: All rows from previous month

**Module 3:** Notion — "Search Database Items" (Prospect Database)
- Filter: Date Added is within last 30 days

**Module 4:** ChatGPT — "Create a Completion"
- Prompt:
  ```
  Generate a Monthly Business Review for [ClientName].

  Data:
  - Total new prospects: {{3.count}}
  - HOT leads: {{3.hot_count}}
  - WARM leads: {{3.warm_count}}
  - Meetings booked: {{2.meeting_count}}
  - Meetings by source sequence: {{2.by_sequence}}
  - Average lead score: {{3.avg_score}}
  - Top performing sequence: {{2.top_sequence}}
  - Worst performing sequence: {{2.bottom_sequence}}

  Monthly SLA target: [Insert from pricing tier]
  SLA met: [Yes/No based on comparison]

  Format:
  1. SLA Compliance Summary (pass/fail on each metric)
  2. Pipeline Health Score (0-100 based on lead quality distribution)
  3. Cost Per Lead Calculation (retainer / total leads delivered)
  4. Cost Per Meeting Calculation (retainer / meetings booked)
  5. Recommendations for next month (3 specific, actionable items)
  6. Scaling suggestion: Should this client upgrade to the next tier? Why or why not?

  Tone: Boardroom-ready. Numbers first, commentary second.
  ```

**Module 5:** Gmail — "Send an Email"
- To: `[client_email]` + `[client_cfo_email]`
- Subject: `Monthly Business Review — [ClientName] — [Month]`
- Body: `{{4.output}}`

{{% accent-box %}}HACK: Always include Cost Per Lead and Cost Per Meeting in your MBR. These are the two numbers the CFO cares about. When you show that your cost per qualified lead is ₦3,200 vs. their internal cost of ₦45,000, the conversation shifts from "should we keep this vendor?" to "how do we expand this?" Frame everything in cost savings, not activity metrics.{{% /accent-box %}}

## Procedure 8.4: Build the Internal Performance Dashboard

You need your own dashboard to run the business. This is separate from client-facing reports. Add to your Notion Dashboard:

**Table 1: Client Performance Summary**
- Columns: Client Name | Tier | MRR | Leads Delivered MTD | Meetings MTD | SLA Status (On Track / At Risk / Behind) | Retention Risk (Low / Medium / High)
- Update this table every Monday morning

**Table 2: System Health**
- Columns: Automation Name | Last Run | Status | Error Count | Next Action
- Pull from Make.com execution logs
- Any automation with 3+ consecutive errors = RED, needs immediate fix

**Table 3: Revenue Forecast**
- Columns: Month | Projected MRR | Actual MRR | New Clients | Churned Clients | Net New MRR
- Update on the 1st of every month
- Track against your ₦10M/month target

## Check-In: Module 8 Complete

- [ ] Notion analytics dashboard built with pipeline volume, outreach performance, lead quality, and revenue sections
- [ ] Weekly automated report scenario sending every Friday
- [ ] Monthly Business Review scenario sending on the 1st
- [ ] Internal performance dashboard with client summary, system health, and revenue forecast
- [ ] Cost Per Lead and Cost Per Meeting calculated for first client
- [ ] All reports tested with real data before going live

---

# MODULE 9: CLIENT ACQUISITION — ALL CAPS

## Overview

You now have a fully operational lead generation machine. This module turns that machine on yourself — you will use your own system to find, score, and convert clients. Your target: sign 3 clients in your first 60 days. First client at Starter tier (₦500,000/month), second at Growth tier (₦1,500,000/month), third at Growth tier (₦1,500,000/month). By Month 3, you are at ₦3.5M MRR.

## Procedure 9.1: Define Your Own ICP

Before you run Apollo searches for clients, you need to know who buys AI lead generation services. Your ICP as a business:

**Firmographics:**
- Industry: SaaS, FinTech, HealthTech, B2B Services, Technology Consulting
- Company size: 30-500 employees
- Revenue: $2M-$50M ARR
- Geography: Nigeria, UK, UAE, US, South Africa
- Business model: B2B with outbound sales motion

**Buyer Persona:**
- Titles: VP Sales, Head of Growth, CRO, Director of Sales Operations, CEO (sub-$5M revenue)
- Pain: SDR team underperforming, cost per lead too high, manual research eating selling time
- Trigger: Recently hired SDRs, raised funding, entered new market, lost a key SDR

**Exclusion:**
- B2C companies (wrong sales motion)
- Companies with <10 employees (no budget)
- Government and military (procurement cycle too long)
- Companies already using ZoomInfo + Outreach + SDR team of 20+ (they built it internally)

## Procedure 9.2: Build Your Own Apollo Search

Log into Apollo.io. Build a People Search with these filters:

1. **Job Titles:** `VP Sales`, `Head of Growth`, `CRO`, `Director of Sales Operations`, `CEO`
2. **Seniority:** C-Level, VP, Director, Owner
3. **Employees:** 30-500
4. **Industry:** Software Publishers, Computer Systems Design, Financial Technology, Management Consulting
5. **Location:** United Kingdom, Nigeria, United Arab Emirates, United States, South Africa
6. **Technologies:** Salesforce, HubSpot, Outreach.io, LinkedIn Sales Navigator (indicates they already invest in sales tools)
7. **Intent:** Hiring for Sales Roles, Recently Funded

Save as: `Own_ICP_Client_Prospecting_v1`

Export the first 200 results. Run them through your own enrichment and scoring pipeline. You are now eating your own dog food — the same system you sell to clients, you use to acquire them.

## Procedure 9.3: Write Your Client Acquisition Sequence

This is different from your client-facing sequences. This is you selling your service. Build a 5-email sequence in Apollo:

**Email 1 — The Uncomfortable Stat (Day 1)**
```
Subject: {{company}}'s SDR cost per lead

{{first_name}},

The average B2B SDR costs ₦750,000/month in salary + tools. Each one produces 2-3 qualified leads per day. That's a cost per lead of ₦12,000-₦18,000.

Our AI pipeline produces the same leads at ₦3,200 each — and delivers 500 per month, not 60.

If {{company}} has SDRs doing manual research, you're overpaying by 4-5x.

Worth 15 minutes?

[Your Name]
[Your Brand]
```

**Email 2 — The Proof (Day 3)**
```
Subject: what {{company}} would look like

{{first_name}},

Ran a quick simulation based on {{company}}'s public data:
- Estimated SDR team: [inferred from LinkedIn hiring]
- Current estimated output: [calculated]
- With AI lead gen: [3-5x calculated output]
- Monthly cost difference: [savings in ₦]

This isn't theoretical — we run this exact system for [industry] companies today.

I'll send the full breakdown if you're interested.

[Your Name]
```

**Email 3 — The Walkthrough (Day 6)**
```
Subject: 12-minute demo?

{{first_name}},

I can show you exactly how this works in 12 minutes:
1. How we find 500+ qualified leads per month using AI
2. How we score and enrich each lead with 24+ data points
3. How we write personalized outreach that books 3x more meetings
4. How it all syncs to your CRM automatically

No slides. No pitch deck. Just a live walkthrough of the system.

Pick a time: [Calendly link]

[Your Name]
```

**Email 4 — The Risk Reversal (Day 10)**
```
Subject: 50 free scored leads for {{company}}

{{first_name}},

I'll make this easy: give me your ICP and I'll deliver 50 scored, enriched leads in 48 hours. Free.

If the quality isn't what you expect, we part ways. If it is, we talk about doing this at scale.

No contract. No commitment. Just proof.

Reply with "send it" and a 2-sentence description of your ideal customer.

[Your Name]
```

**Email 5 — The Breakup (Day 14)**
```
Subject: moving on from {{company}}

{{first_name}},

I've reached out a few times and I don't want to be a nuisance.

If you ever want to explore AI-powered lead gen, save this email. The 50-lead free trial offer doesn't expire.

All the best.

[Your Name]
```

## Procedure 9.4: Execute the 50-Lead Free Trial Strategy

This is your highest-converting acquisition tactic. When a prospect accepts the free trial:

1. **Collect ICP** — Send them your ICP Document template from Notion. Ask them to fill it in. Give them 24 hours.
2. **Run Apollo Search** — Build a saved search based on their ICP. Export 100 prospects (you'll deliver 50 scored leads, but you need buffer for COLD scores).
3. **Enrich and Score** — Run through your standard pipeline (Module 4 + Module 5).
4. **Deliver in Notion** — Create a shared Notion page titled "[ClientName] — 50 Lead Free Trial." Add a table view with columns: Name, Title, Company, Email, Score, Band, Personalization Hook, Pain Points. Share the page with the prospect via Notion's "Share to web" feature.
5. **Follow Up** — 48 hours after delivery, send this email:
   ```
   Subject: your 50 leads — how do they look?

   {{first_name}},

   Delivered 50 scored leads yesterday. Quick question:

   On a scale of 1-10, how well do these match what your SDR team would manually research?

   If you're at 7+, we should talk about doing this at 10x volume.

   [Your Name]
   ```

Close rate on free trial recipients who rate 7+: **65%**.

## Procedure 9.5: Build the Proposal Template

Create a Notion page template titled "Client Proposal — [ClientName]." Structure:

```
# AI Lead Generation Proposal for [ClientName]

## Executive Summary
[2-3 sentences summarizing what you'll deliver]

## Service Tier: [Starter / Growth / Enterprise]
[Copy from pricing matrix in Module 1]

## Deliverables
- Qualified leads per month: [number]
- Data enrichment fields: [number]
- Outreach sequences: [number]
- CRM integration: [yes/no, which CRM]
- Reporting cadence: [weekly/monthly]

## SLA Guarantees
- Minimum [X] qualified leads per month (band WARM or above)
- Minimum [X] meetings booked per month
- If SLA is missed 2 consecutive months, client receives 1 month free

## Timeline
- Week 1: ICP development + Apollo search configuration
- Week 2: First batch of enriched + scored leads delivered
- Week 3: Outreach sequences launched
- Week 4: First meetings booked, first weekly report delivered

## Investment
- Onboarding fee: ₦[amount] (one-time)
- Monthly retainer: ₦[amount]
- Contract term: 3 months minimum, month-to-month after

## Next Steps
1. Sign this proposal (reply "Approved")
2. Complete the ICP Document (link)
3. Schedule kickoff call (Calendly link)

Signed,
[Your Name]
[Your Brand]
```

## Check-In: Module 9 Complete

- [ ] Own ICP defined and documented
- [ ] Apollo search for client prospects saved and running
- [ ] 5-email client acquisition sequence loaded in Apollo
- [ ] 50-lead free trial process documented and tested
- [ ] Proposal template created in Notion
- [ ] First 200 client prospects exported and scored
- [ ] Outreach to client prospects started
- [ ] First discovery call booked

---

# MODULE 10: SCALING & TEAM BUILDING — ALL CAPS

## Overview

One person can manage 3-5 clients at Growth tier before quality degrades. To reach ₦10M MRR, you need a team. This module defines the hiring roadmap, the delegation framework, and the operational systems that let you scale from solo operator to 10-person agency without breaking the machine you built.

## Procedure 10.1: Define the Scaling Milestones

Record these milestones in your Notion Revenue Tracker:

| Milestone | MRR | Clients | Team Size | Key Hire |
|---|---|---|---|---|
| Level 1: Solo Operator | ₦0 — ₦2M | 1-3 | 1 (you) | None |
| Level 2: First Hire | ₦2M — ₦5M | 4-6 | 2 | Lead Research Analyst |
| Level 3: Core Team | ₦5M — ₦10M | 7-12 | 4 | + Operations Manager + Outreach Specialist |
| Level 4: Full Agency | ₦10M — ₦25M | 13-25 | 8-10 | + Account Manager + 2 Analysts + Sales Rep |
| Level 5: Platform Business | ₦25M+ | 25+ | 15+ | + Product Manager (build SaaS) |

You are currently at Level 1. Do not hire until you hit ₦2M MRR. Premature hiring is the #1 killer of service businesses.

## Procedure 10.2: Hire the Lead Research Analyst

This is your first hire. They will own the research pipeline — Apollo searches, enrichment, and scoring — freeing you to focus on client management and sales.

**Job Description:**
```
Title: Lead Research Analyst (Remote)
Compensation: ₦350,000 — ₦500,000/month
Location: Remote (Lagos, Abuja, or anywhere with reliable internet)

Responsibilities:
- Build and maintain Apollo.io saved searches for 5+ clients
- Monitor and troubleshoot Make.com automation pipelines
- Run weekly enrichment audits and fix flagged records
- Maintain Notion Prospect Database accuracy (deduplication, status updates)
- Generate weekly and monthly client reports
- Calibrate scoring models based on response rate data

Requirements:
- 1+ year experience with Apollo.io or similar prospecting tools
- Proficiency in Notion (databases, formulas, templates)
- Basic understanding of Make.com or Zapier automations
- Strong written English
- Available 9 AM — 5 PM WAT, Monday — Friday

Nice-to-have:
- Experience with B2B sales or SDR operations
- ChatGPT / AI tool proficiency
- HubSpot or Salesforce experience
```

Post this on: LinkedIn, Twitter, and remote job boards (WeWorkRemotely, Remote.co). Interview 10 candidates. Hire the one who can build an Apollo search in under 10 minutes during the skills test.

## Procedure 10.3: Build the SOP Library

Every task in your business must be documented as a Standard Operating Procedure (SOP) before you delegate it. Create these SOPs in your Notion SOPs page:

**SOP-001: New Client Onboarding**
1. Client approves proposal → Create client folder in Notion using template button
2. Send ICP Document template to client → Set 24-hour deadline
3. Build Apollo saved search from ICP → Name: `[ClientName]_ICP_v1`
4. Create Make.com scenarios for this client (Enrichment, Scoring, CRM Sync, Reports)
5. Create client-specific sequences in Apollo (Hot, Warm, Cool)
6. Build Google Sheets backup for this client
7. Send "Onboarding Complete" email with timeline for first delivery

**SOP-002: Weekly Operations Checklist**
1. Monday: Update Internal Performance Dashboard, check system health
2. Tuesday: Review enrichment audit flags, fix errors
3. Wednesday: Review scoring calibration, adjust if needed
4. Thursday: Prepare for client calls, review pipeline
5. Friday: Verify weekly reports sent, review meeting log

**SOP-003: Client Quarterly Business Review**
1. Pull 90-day data from Notion + Google Sheets
2. Calculate: Total leads delivered, Meetings booked, Cost per lead, Cost per meeting, SLA compliance rate
3. Compare against SLA guarantees
4. Write QBR document (2 pages max)
5. Schedule 30-minute QBR call with client
6. Present data, discuss scaling opportunities
7. If client is outgrowing current tier, propose upgrade

**SOP-004: Automation Failure Recovery**
1. Check Make.com execution log → Identify failed scenario
2. Read error message → Categorize: API limit, Auth expired, Data format, Module error
3. API limit: Wait 1 hour, retry
4. Auth expired: Re-authenticate the module connection
5. Data format: Check field mappings in Notion, fix mismatch
6. Module error: Check Make.com status page, escalate to support if needed
7. Document the failure in Automation Logs (Notion)
8. If same failure occurs 3 times, rebuild the scenario

{{% accent-box %}}HACK: Record a Loom video for every SOP. A 3-minute video showing someone how to build an Apollo search is 10x more effective than a 2-page written document. Store Loom links inside each Notion SOP page. When you hire someone, their first week is watching your SOP videos and replicating each task. This cuts onboarding from 4 weeks to 1 week.{{% /accent-box %}}

## Procedure 10.4: Build the Client Expansion Playbook

Your fastest revenue growth comes from expanding existing clients, not signing new ones. Build this expansion process:

**Trigger:** Client has been active for 90+ days AND SLA compliance is ≥95%.

**Expansion Conversation Script:**
```
"[ClientName] is hitting 95%+ SLA compliance consistently. Your SDR team is
converting our leads at [X]%. If we increase lead volume by 2x, your pipeline
doubles. The next tier up gives you [specifics from pricing matrix]. The
incremental cost is ₦[difference], but the incremental pipeline value based on
your current conversion rate is ₦[calculated]. That's a [X]x return on the
upgrade. Want me to switch you over this month?"
```

**Expansion targets:**
- Starter → Growth: 50% of Starter clients should upgrade within 6 months
- Growth → Enterprise: 30% of Growth clients should upgrade within 9 months

Track expansion rate in your Revenue Tracker. If expansion rate drops below 20%, your service quality is slipping — fix the product before you fix the sales.

## Procedure 10.5: Build the ₦10M/Month Roadmap

This is your 12-month financial roadmap. Record it in Notion:

| Month | New Clients | Churned Clients | Total Clients | Avg MRR/Client | Total MRR | Cumulative Revenue |
|---|---|---|---|---|---|---|
| 1 | 1 | 0 | 1 | ₦500,000 | ₦500,000 | ₦500,000 |
| 2 | 1 | 0 | 2 | ₦750,000 | ₦1,500,000 | ₦2,000,000 |
| 3 | 2 | 0 | 4 | ₦875,000 | ₦3,500,000 | ₦5,500,000 |
| 4 | 1 | 0 | 5 | ₦900,000 | ₦4,500,000 | ₦10,000,000 |
| 5 | 2 | 0 | 7 | ₦930,000 | ₦6,500,000 | ₦16,500,000 |
| 6 | 2 | -1 | 8 | ₦1,000,000 | ₦8,000,000 | ₦24,500,000 |
| 7 | 2 | 0 | 10 | ₦1,000,000 | ₦10,000,000 | ₦34,500,000 |
| 8 | 2 | -1 | 11 | ₦1,050,000 | ₦11,550,000 | ₦46,050,000 |
| 9 | 3 | 0 | 14 | ₦1,100,000 | ₦15,400,000 | ₦61,450,000 |
| 10 | 2 | -1 | 15 | ₦1,150,000 | ₦17,250,000 | ₦78,700,000 |
| 11 | 3 | 0 | 18 | ₦1,200,000 | ₦21,600,000 | ₦100,300,000 |
| 12 | 3 | -1 | 20 | ₦1,250,000 | ₦25,000,000 | ₦125,300,000 |

**Assumptions:**
- Average client acquisition: 2 per month after Month 3
- Churn rate: 5-8% (1 client per quarter)
- Average MRR increases as you sign higher-tier clients
- Month 7: ₦10M MRR milestone
- Month 12: ₦25M MRR with 20 clients

**Expenses at Month 12 (estimated):**
- Tooling (Apollo, Make, ChatGPT, Notion, LinkedIn, Google Workspace): ₦750,000/month
- Team salaries (8 people at average ₦600,000/month): ₦4,800,000/month
- Marketing and lead generation for your own business: ₦500,000/month
- Infrastructure and miscellaneous: ₦450,000/month
- **Total expenses: ₦6,500,000/month**
- **Profit at Month 12: ₦18,500,000/month (74% margin)**

{{% accent-box %}}HACK: Once you hit ₦10M MRR, start building a self-serve SaaS version of your pipeline. Clients pay ₦200,000-₦500,000/month to access your Apollo + ChatGPT + Notion system directly via a web dashboard. This converts your service into a product, adds a revenue stream with near-zero marginal cost, and creates a moat that competitors cannot replicate. Use Next.js for the frontend and Retool for the internal dashboard.{{% /accent-box %}}

## Check-In: Module 10 Complete

- [ ] Scaling milestones documented in Revenue Tracker
- [ ] Lead Research Analyst job description posted
- [ ] 4 core SOPs written and stored in Notion
- [ ] Loom video recordings created for each SOP
- [ ] Client expansion playbook documented
- [ ] 12-month financial roadmap recorded with assumptions
- [ ] Monthly expense projections calculated
- [ ] ₦10M MRR target mapped to specific month and client count

---

# FINAL CHECK-IN: PLAYBOOK COMPLETE

You have built the complete operating system. Verify every component:

- [ ] **Module 1:** Business model defined, pricing tiers set, infrastructure registered, Notion workspace live
- [ ] **Module 2:** Apollo.io configured with verified domain, Make.com connected, ChatGPT Custom GPTs built, email infrastructure secured (SPF/DKIM/DMARC)
- [ ] **Module 3:** ICP template created, Apollo saved searches running, export-to-Notion pipeline active, deduplication enforced
- [ ] **Module 4:** Enrichment API unlocked, multi-source enrichment workflow producing 24+ fields per prospect, weekly audit running
- [ ] **Module 5:** 5-signal scoring model operational, sub-scores calculated, HOT/WARM/COOL/COLD routing automated, calibration routine scheduled
- [ ] **Module 6:** Three outreach sequences written and loaded, auto-enrollment workflow routing by band, A/B testing configured, first batch sending
- [ ] **Module 7:** HubSpot and Salesforce integrations live, reply handler routing correctly, meeting tracker logging to Sheets
- [ ] **Module 8:** Notion analytics dashboard built, weekly reports automating, MBR reports generating, internal performance dashboard updating
- [ ] **Module 9:** Own ICP defined, client acquisition sequence running, free trial process tested, proposal template ready
- [ ] **Module 10:** Scaling roadmap recorded, first hire job description posted, SOPs documented with video, expansion playbook ready

**39 procedures. 10 modules. One operating system.**

From empty Apollo.io account to ₦10M/month in recurring revenue. Every tool, every setting, every script, every workflow — documented, automated, and ready to execute.

Start now. Build Module 1 today.
