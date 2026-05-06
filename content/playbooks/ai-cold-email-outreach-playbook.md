---
title: "The AI Cold Email Outreach Agency Playbook: 44 Steps to $15K/Month"
date: 2026-05-01
category: "Playbook"
price: "₦35,000"
readTime: "90 MIN"
excerpt: "The complete operating system for building an AI cold email outreach agency from zero. 10 modules, 44 procedures, exact tool configurations, outreach scripts, three pricing tiers, and a scaling roadmap. From empty inbox to $15K/month in recurring revenue."
image: "/images/articles/playbooks/ai-cold-email-outreach-playbook.png"
heroImage: "/images/heroes/playbooks/ai-cold-email-outreach-playbook.png"
relatedOpportunity: "/opportunities/ai-cold-email-agency/"
relatedGuide: "/intelligence/build-ai-cold-email-agency/"
---

This is not a blog post condensed into a PDF. This is an operating system for building an AI cold email outreach agency. Every module contains exact procedures — not theories, not possibilities, not "consider doing X." You will do X, in this order, with these tools, and you will verify it worked before moving on.

**44 procedures. 10 modules. 90+ hours of reading and execution.** If you complete every procedure, you will have a fully operational AI cold email outreach agency generating ₦6M–₦12M/month in recurring revenue within 180 days. If you skip procedures, you will have a half-configured Make.com scenario that burns through domains and lands in spam. The choice is yours.

---

# MODULE 1: AGENCY ARCHITECTURE — FOUNDATION

## Overview

Before you touch a single tool, you need to understand the exact business model you are building. An AI cold email outreach agency is not a "freelance email service." It is a systems business that acquires leads, warms them through AI-personalized sequences, and delivers booked meetings to clients on a performance or retainer basis. The margin comes from automation. One Make.com scenario can serve 20 clients simultaneously. That is the leverage.

This module covers your agency structure, service definition, ICP (Ideal Client Profile) for your own agency, and the legal/financial skeleton you need before spending ₦1 on tools. Time required: 8–12 hours. Tools: None (yet). A Google Doc or Notion page.

## Procedure 1.1: Define Your Agency Service Model

Open a blank document. Type the following headers. Fill them in using the exact specifications below. Do not freelance your way through this — follow the model.

**Service Model Options:**

| Model | Description | Revenue Target (Monthly) | Complexity |
|-------|-------------|--------------------------|------------|
| Performance-Based | Charge per booked meeting (₦15,000–₦45,000/meeting) | ₦1.5M–₦4.5M | Low setup, high risk |
| Retainer + Performance | ₦750K/month retainer + ₦15,000/meeting over threshold | ₦2M–₦6M | Medium complexity |
| Full-Stack Retainer | ₦1.5M–₦3M/month for complete outbound engine | ₦3M–₦12M | High complexity, highest margin |

You will choose **Retainer + Performance** as your starting model. Here is why: pure performance means you carry all the risk. Pure retainer means clients expect perfection from Day 1. The hybrid gives you cash flow stability from the retainer and upside from booked meetings.

Write this in your document:

```
Agency Name: [Your Name] Outbound
Service Model: Retainer + Performance
Retainer: ₦750,000/month
Meeting Credit: 5 meetings included
Overage: ₦15,000 per additional booked meeting
Contract Term: 3-month minimum, month-to-month after
```

## Procedure 1.2: Define Your Agency's ICP

Your agency's ICP is NOT the same as your clients' ICP. You are selling outbound infrastructure. Your buyers are:

1. **B2B SaaS companies** (ARR ₦50M–₦500M, sales teams of 3–15, currently underperforming on outbound)
2. **Professional services firms** (consulting, accounting, legal — partners who need pipeline but have no SDRs)
3. **Marketing agencies** (who want to offer outbound as a service but lack the tech stack)

Create an ICP one-pager:

```
Target: B2B companies with ₦50M+ annual revenue
Headcount: 10–200 employees
Buyer: VP Sales, Head of Growth, or Founder
Pain Signal: Hiring SDRs who underperform, spending on ads with no ROI, 
             no outbound infrastructure, LinkedIn outreach only
Excluded: B2C, e-commerce, local businesses, companies under ₦20M revenue
```

## Procedure 1.3: Register Your Business Entity

This procedure is jurisdiction-dependent but mandatory. You will not run an agency through a personal bank account.

**Nigeria (primary):** Register with CAC (Corporate Affairs Commission) at https://portal.cac.gov.ng as a Business Name or Limited Liability Company. Cost: ₦10,000–₦50,000 depending on structure.

**US-facing (optional):** If targeting US clients, register a Wyoming LLC via https://www.wyomingcompany.com or https://stripe.com/atlas. Cost: $100–$500. This gives you a US bank account via Mercury (https://mercury.com) and Stripe access for card payments.

Open a business bank account. Connect it to a payment processor:

| Processor | Use Case | Fee |
|-----------|----------|-----|
| Stripe | US/EU clients, card payments | 2.9% + ₦150 |
| Paystack | Nigerian clients, card/bank transfer | 1.5% + ₦100 |
| Wise | International wire transfers | 0.5–1% |

{{% accent-box %}}HACK: Open a Wise Business account immediately. You will need it for paying domain registrars, Google Workspace, and Apollo.io — all denominated in USD. The Wise virtual card avoids Nigerian card foreign transaction limits.{{% /accent-box %}}

## Procedure 1.4: Create Your Agency's Outbound Asset (One-Page Site)

You will NOT build a full website. You will build a single-page site that exists solely to validate credibility when prospects Google your agency.

Use Carrd (https://carrd.co) — one-page site builder. Pro plan: $19/year.

Structure:

1. **Hero:** "We Build AI-Powered Outbound Engines That Book 15+ Meetings/Month for B2B Companies"
2. **How It Works:** 3-step process (We Research → We Personalize → You Close)
3. **Results:** "Average client sees 12–20 booked meetings/month within 60 days"
4. **CTA:** "Book a 15-Minute Outbound Audit" → Calendly link

Connect a custom domain. Buy one at Namecheap (https://namecheap.com) — use `.co` or `.io` if `.com` is taken. Cost: ₦3,000–₦8,000/year.

## Check-In: Module 1 Complete

- [ ] Agency service model defined and documented (Retainer + Performance)
- [ ] ICP one-pager written with target, headcount, buyer, pain signals, exclusions
- [ ] Business entity registered (CAC or Wyoming LLC)
- [ ] Business bank account opened with payment processor connected
- [ ] Wise Business account opened with virtual card active
- [ ] One-page Carrd site live with custom domain and Calendly CTA

---

# MODULE 2: TECH STACK CONFIGURATION

## Overview

Your tech stack is the engine. Every tool here has been selected for a specific reason: cost efficiency, API accessibility, and compatibility with Make.com. Do not substitute tools unless the procedure explicitly gives you an alternative. Every substitution introduces risk.

This module covers the complete tool procurement and initial configuration. You will create accounts, connect APIs, and verify each integration before moving on. Time required: 6–8 hours. Budget: ₦150,000–₦250,000 for first-month setup.

## Procedure 2.1: Procure Your Core Tool Stack

Create accounts at each of the following URLs. Use your business email (the Google Workspace domain you will set up in Module 4). If you don't have it yet, use a dedicated Gmail — you will migrate later.

| Tool | URL | Purpose | Monthly Cost |
|------|-----|---------|--------------|
| Apollo.io | https://apollo.io | Lead database + email sequences | $49–$119/user (Starter/Pro) |
| Make.com | https://make.com | Workflow automation engine | $9–$16/month (1,000–10,000 ops) |
| Google Workspace | https://workspace.google.com | Email hosting + domains | $6/user/month (Business Starter) |
| OpenAI | https://platform.openai.com | GPT-4o API for personalization | ~$50–$200/month (usage-based) |
| Clay | https://clay.com | Enrichment + waterfall data | $149/month (Starter) |
| Instantly.ai | https://instantly.ai | Email warmup + delivery | $30–$70/month (Growth) |
| Lemlist | https://lemlist.com | Alternative sending + multichannel | $59/month (Email Starter) |
| Calendly | https://calendly.com | Meeting booking | $10/month (Standard) |
| Notion | https://notion.so | Client dashboard + SOPs | Free–$8/month |

**Total estimated monthly cost: ₦180,000–₦350,000** (depending on volume and plan tiers)

Write these down in your Notion workspace. Create a page called "Agency Tech Stack" with each tool, login email, and billing date.

## Procedure 2.2: Configure Make.com Workspace

1. Go to https://make.com and sign in.
2. Click **Create a new scenario**. You will NOT build the full scenario yet — you are verifying API connections.
3. Click the **+** icon to add a module. Search for **HTTP – Make a request**. This is your universal API connector.
4. In another tab, go to https://apollo.io → Settings → API. Copy your API key. Store it in a secure password manager (Bitwarden — https://bitwarden.com — free).
5. Back in Make.com, add an HTTP module. Set:
   - URL: `https://api.apollo.io/v1/people/search`
   - Method: POST
   - Headers: `Content-Type: application/json`, `Cache-Control: no-cache`
   - Body (JSON):
   ```json
   {
     "api_key": "YOUR_APOLLO_API_KEY",
     "page": 1,
     "per_page": 1,
     "organization_num_employees_ranges": ["51-200"]
   }
   ```
6. Click **Run once**. If you see a 200 response with a `people` array, your Apollo API is live. If you get a 401, your API key is wrong. Regenerate it at https://apollo.io/settings/integrations.

Do you see a successful API response with contact data? If not, check: (1) Apollo plan includes API access (Pro plan required), (2) API key has no trailing spaces, (3) your Make.com account is on a paid plan (free plan has limited HTTP requests).

## Procedure 2.3: Configure OpenAI API Access

1. Go to https://platform.openai.com/api-keys.
2. Click **Create new secret key**. Name it: `make-agency-prod`. Copy it immediately — OpenAI will not show it again.
3. Go to https://platform.openai.com/settings/organization/billing. Add ₦20,000 ($12) minimum credit. This funds your personalization engine. You will use GPT-4o-mini for most personalization (cheaper, fast) and GPT-4o for complex personalization tasks.
4. In Make.com, add a new module: **OpenAI (ChatGPT) – Create a Chat Completion**. Connect using your API key.
5. Set model to `gpt-4o-mini`, prompt: "Say 'API connection verified.'" Click **Run once**. You should see the response.

{{% accent-box %}}HACK: Set a monthly spending limit on your OpenAI account at https://platform.openai.com/settings/organization/limits. Set it to $100/month initially. AI personalization for 50,000 emails/month should cost $30–$60. If it crosses $100, something in your Make.com loop is running unnecessarily.{{% /accent-box %}}

## Procedure 2.4: Set Up Your Notion Command Center

Create a Notion workspace with this exact structure:

```
📁 Agency Command Center
├── 📄 Client Tracker (Database)
│   Properties: Client Name, Status, Retainer Amount, Meetings Delivered, 
│               Contract Start, Contract End, Renewal Date
├── 📄 Campaign Tracker (Database)
│   Properties: Client, Campaign Name, ICP, Total Sent, Reply Rate, 
│               Meeting Booked Rate, Status
├── 📄 Domain Inventory (Database)
│   Properties: Domain, Provider, Google Workspace Status, Warmup Status,
│               Sending Limit, Date Added
├── 📄 SOPs (Page)
│   ├── Lead Research SOP
│   ├── Email Sequence SOP
│   ├── AI Personalization SOP
│   ├── Client Onboarding SOP
│   └── Reporting SOP
└── 📄 Financials (Page)
    ├── Monthly Revenue Tracker
    ├── Expense Tracker
    └── Client Invoice Log
```

This is your operating system. Every client, campaign, domain, and dollar flows through here. Do not skip this structure. You will reference it daily.

## Check-In: Module 2 Complete

- [ ] All 9 core tool accounts created with business email
- [ ] Apollo.io API key generated and tested via Make.com HTTP module
- [ ] OpenAI API key generated, billing funded, connection verified in Make.com
- [ ] Monthly spending limit set on OpenAI ($100 cap)
- [ ] Notion Command Center created with all 4 databases and 5 SOP pages
- [ ] All credentials stored in Bitwarden (not browser, not Notion, not Google Docs)

---

# MODULE 3: LEAD RESEARCH WITH APOLLO.IO

## Overview

Lead research is where 80% of agencies fail. They buy a list of 10,000 contacts, load them into a sequence, and wonder why their reply rate is 0.3%. Quality leads are not found — they are engineered through precise search criteria, layered filters, and verification. This module gives you the exact Apollo.io search configurations, saved views, and export procedures that produce lists with 8–15% reply rates instead of 0.3%.

You will learn to search, filter, verify, and structure lead lists for any client ICP. Time required: 10–15 hours. Tools: Apollo.io, Clay (optional enrichment), Google Sheets.

## Procedure 3.1: Configure Apollo.io Organization Settings

1. Log in to https://apollo.io.
2. Navigate to **Settings → Organization**. Set your company name and domain.
3. Navigate to **Settings → Users**. Invite team members if applicable (each seat costs $49–$119/month).
4. Navigate to **Settings → Credit Usage**. Understand your credit allocation:

| Apollo Plan | Monthly Credits | Export Limit | API Access |
|-------------|----------------|--------------|------------|
| Free | 60 | 10/month | No |
| Basic ($49/user) | 900 | 200/month | No |
| Professional ($99/user) | 3,000 | 500/month | Yes |
| Organization ($119/user) | 9,000 | Unlimited | Yes |

You need the **Professional** plan at minimum for API access. Without API, you cannot automate lead research through Make.com.

5. Navigate to **Settings → Email Accounts**. Do NOT connect your sending email here yet — that happens in Module 4. This is only for Apollo's native sequences, which you will use as a backup, not primary.

## Procedure 3.2: Build Your First Saved Search (SaaS ICP)

This is the search you will run for your first SaaS client. Follow every filter exactly.

1. Go to **Search → People** in Apollo.
2. Set these filters:

```
Location: United States, United Kingdom, Canada
Employee Count: 11-50, 51-200
Industry: Computer Software, SaaS, Information Technology
Seniority: VP, Director, Head, C-Level
Department: Sales, Revenue, Growth, Business Development
Keywords (Title): "VP Sales" OR "Head of Sales" OR "Director of Sales" 
                   OR "Chief Revenue Officer" OR "VP Growth"
Technologies (Company): Salesforce OR HubSpot (indicates they have a CRM 
                        — they can receive meetings)
Funding: Series A, Series B, Series C (they have money to spend)
```

3. Click **Save Search**. Name it: `SaaS-Outbound-VP-Sales-SeriesA-C`.
4. Look at the result count. If it is below 500, broaden the employee count to include 201–500. If it is above 10,000, narrow the title keywords.

**Target list size per campaign: 500–2,000 contacts.** Below 500 means you will exhaust the list too quickly. Above 2,000 means your ICP is too broad and reply rates will suffer.

## Procedure 3.3: Build Saved Search #2 (Professional Services ICP)

```
Location: United States, United Kingdom
Employee Count: 11-50, 51-200
Industry: Management Consulting, Accounting, Legal Services
Seniority: Partner, Managing Director, C-Level
Keywords (Title): "Partner" OR "Managing Partner" OR "Principal" 
                   OR "Director of Business Development"
Technologies (Company): HubSpot OR Pardot (indicates marketing sophistication)
Company Revenue: $5M–$50M
```

Save as: `ProfServices-Partner-Consulting-MidMarket`.

## Procedure 3.4: Verify and Enrich Lead Data

Apollo data is good but not perfect. Email verification rates hover around 85–90%. You will lose 10–15% of your list to bounces if you do not verify.

**Option A (Budget):** Use Apollo's built-in email verification. In any search, click the **Email Status** column header. Sort by "Verified" first. Remove all contacts marked "Unverified" or "Guessed."

**Option B (Pro):** Export your list and run it through Clay's waterfall enrichment:

1. In Apollo, select your saved search results (select all → up to your export limit).
2. Click **Export** → **CSV**.
3. Open https://clay.com and create a new table.
4. Import the CSV.
5. Add enrichment columns:
   - **Work Email** (via Hunter.io integration in Clay)
   - **Email Verification** (via ZeroBounce integration in Clay)
   - **LinkedIn Profile** (via Clay's native enrichment)
   - **Recent Company News** (via Clay's Google News integration — this feeds your AI personalization)
6. Filter out rows where email verification = "invalid" or "catch-all."
7. Export the cleaned list as CSV.

{{% accent-box %}}HACK: The "Recent Company News" enrichment in Clay is the single highest-ROI data point in your entire stack. When your AI personalization engine references a company's recent funding round, product launch, or hire, your reply rate doubles. This is not theoretical — it is the difference between a 3% and a 7% reply rate.{{% /accent-box %}}

## Procedure 3.5: Structure Your Lead Lists for Make.com Import

Your final CSV must have these exact column headers (case-sensitive — your Make.com scenario will reference them):

```
first_name | last_name | email | title | company_name | company_domain | 
linkedin_url | company_news | icp_label | sequence_tag
```

- `icp_label`: Which saved search this contact came from (e.g., "SaaS-VP-Sales")
- `sequence_tag`: Which email sequence they will receive (e.g., "seq-pain-point," "seq-social-proof")
- `company_news`: The Clay-enriched recent news item (or "none" if unavailable)

Upload this CSV to Google Sheets. Name the sheet: `[ClientName]-LeadList-[Date]`. This Google Sheet becomes the data source for your Make.com scenario.

## Check-In: Module 3 Complete

- [ ] Apollo.io Professional plan active with API access confirmed
- [ ] First saved search (SaaS ICP) created with 500–2,000 results
- [ ] Second saved search (Professional Services ICP) created
- [ ] Lead list exported and enriched through Clay waterfall
- [ ] Invalid/catch-all emails removed (verification pass complete)
- [ ] Final CSV structured with all 10 required columns uploaded to Google Sheets

---

# MODULE 4: EMAIL INFRASTRUCTURE SETUP

## Overview

Your email infrastructure determines whether your emails land in the primary inbox or the spam folder. This is not a "set it and forget it" operation. Google and Microsoft update their spam filters constantly. Your infrastructure must be built to withstand these updates — multiple domains, proper DNS records, gradual warmup, and continuous deliverability monitoring.

This module is the most technical in the entire playbook. Execute it precisely. A single misconfigured DNS record will destroy your deliverability for weeks. Time required: 12–16 hours (spread over 14–21 days for warmup). Tools: Namecheap, Google Workspace, Instantly.ai, MXToolbox.

## Procedure 4.1: Procure Sending Domains

You will NOT send cold emails from your client's primary domain. Ever. If a domain gets blacklisted from cold outreach, it must NOT be the domain their team uses for business email.

**Rule: 1 domain per 50 emails/day planned volume.** If a client wants 200 cold emails/day, you need 4 domains minimum.

1. Go to https://namecheap.com.
2. Purchase domains following this naming convention:

```
Pattern: [keyword]-[keyword].com or [keyword]get.com or [keyword]io.com
Example: outboundscale.io, getpipeline.co, replyengine.com
```

3. Do NOT use the client's brand name in the domain. Use generic, professional-sounding names.
4. Purchase 3–5 domains per client to start.

**Domain budget per client: ₦15,000–₦40,000** (3–5 domains at ₦3,000–₦8,000 each)

## Procedure 4.2: Configure DNS Records for Each Domain

For EACH domain you purchased, you must configure these DNS records in Namecheap:

**Step 1: Connect to Google Workspace**

1. In Google Workspace admin (https://admin.google.com), click **Add domain**.
2. Select "Verify domain." Google will give you a TXT record.
3. In Namecheap → Domain List → Manage → DNS, add:
   - Type: `TXT`
   - Host: `@`
   - Value: `google-site-verification=[CODE_PROVIDED]`
   - TTL: Automatic

4. Add MX records for Google Workspace:

| Type | Host | Value | Priority | TTL |
|------|------|-------|----------|-----|
| MX | @ | ASPMX.L.GOOGLE.COM | 1 | Auto |
| MX | @ | ALT1.ASPMX.L.GOOGLE.COM | 5 | Auto |
| MX | @ | ALT2.ASPMX.L.GOOGLE.COM | 5 | Auto |
| MX | @ | ASPMX2.GOOGLEMAIL.COM | 10 | Auto |
| MX | @ | ASPMX3.GOOGLEMAIL.COM | 10 | Auto |

**Step 2: Configure SPF Record**

Add a TXT record:
- Type: `TXT`
- Host: `@`
- Value: `v=spf1 include:_spf.google.com ~all`
- TTL: Automatic

**Step 3: Configure DKIM**

1. In Google Workspace Admin → Apps → Google Workspace → Gmail → Authenticate email.
2. Select your domain. Google will generate a DKIM record.
3. Add it in Namecheap DNS:
   - Type: `TXT`
   - Host: `google._domainkey`
   - Value: `[VALUE_PROVIDED_BY_GOOGLE]`
   - TTL: Automatic

**Step 4: Configure DMARC**

Add a TXT record:
- Type: `TXT`
- Host: `_dmarc`
- Value: `v=DMARC1; p=none; rua=mailto:dmarc@youragencydomain.com`
- TTL: Automatic

Start with `p=none` (monitoring mode). After 14 days of clean sending, change to `p=quarantine`. After 30 days, change to `p=reject`.

**Step 5: Add Custom Tracking Domain**

In Instantly.ai → Settings → Tracking, add a CNAME record:
- Type: `CNAME`
- Host: `track`
- Value: `track.instantly.ai`
- TTL: Automatic

## Procedure 4.3: Create Email Accounts and Configure Signatures

For each domain, create 2–3 Google Workspace user accounts:

```
first@domain1.com (e.g., sarah@outboundscale.io)
first.last@domain1.com (e.g., sarah.okon@outboundscale.io)
```

Use realistic names. Do NOT use "outreach@domain.com" or "sales@domain.com" — spam filters flag generic role addresses.

Configure each account's signature:

```
[First Name]
[Title] | [Client Company Name]
[Phone Number — real or Calendly link]

[Client Company Tagline — 3-5 words]
```

Keep signatures minimal. No images, no logos, no social media icons. HTML-rich signatures trigger spam filters. Plain text only.

## Procedure 4.4: Warm Up Email Accounts with Instantly.ai

This is the most critical procedure in this entire playbook. Skipping warmup = guaranteed spam folder.

1. Log in to https://instantly.ai.
2. Click **Add Account** → **Connect with SMTP/IMAP**. Enter each Google Workspace account's credentials. (Enable "Less Secure Apps" or create an App Password in Google Workspace Admin → Security.)
3. For each account, configure warmup settings:

```
Warmup Enabled: YES
Starting Volume: 5 emails/day
Increase Rate: 2 emails/day (every 24 hours)
Maximum Volume: 40 emails/day (reached after ~18 days)
Warmup Ratio: 40% (40% of emails are replies to other warmup emails)
Mark as Important: YES
Move to Primary: YES (Gmail-specific — moves warmup emails out of Promotions tab)
```

4. Run warmup for **14–21 days minimum** before sending a single cold email.
5. Monitor the Warmup Analytics dashboard daily. All accounts should show:
   - Health Score: 90%+
   - Reply Rate: 30%+
   - Spam Complaints: 0

{{% accent-box %}}HACK: During warmup, log in to each Google Workspace account manually at least once every 48 hours. Open warmup emails, reply to a few, mark some as important, move some to different folders. Google tracks human-like behavior patterns. A fully automated warmup with zero manual interaction is detectable.{{% /accent-box %}}

## Procedure 4.5: Verify Deliverability with MXToolbox

1. Go to https://mxtoolbox.com/diagnostic.aspx.
2. Enter each domain. Verify all checks pass (green):
   - SPF Record: PASS
   - DKIM Record: PASS
   - DMARC Record: PASS
   - MX Record: PASS
   - Blacklist: NOT LISTED
3. Run the blacklist check at https://mxtoolbox.com/blacklists.aspx for each domain and each IP.
4. If any domain is blacklisted, submit delisting requests immediately. This can take 24–72 hours.

## Check-In: Module 4 Complete

- [ ] 3–5 sending domains procured per client (not client's primary domain)
- [ ] All DNS records configured: SPF, DKIM, DMARC, MX, CNAME for tracking
- [ ] 2–3 Google Workspace email accounts created per domain with realistic names
- [ ] All signatures configured (plain text, minimal)
- [ ] Instantly.ai warmup running for 14+ days on all accounts (Health 90%+)
- [ ] MXToolbox deliverability check: all green, no blacklists
- [ ] DMARC policy set to p=none (to be escalated after 14 days clean sending)

---

# MODULE 5: AI PERSONALIZATION ENGINE

## Overview

Generic cold emails are dead. "I came across your company and thought we could help" gets deleted in 0.3 seconds. AI personalization is your unfair advantage — but only if done correctly. Bad AI personalization (obviously AI-written, hallucinated facts, wrong company references) is worse than no personalization.

This module builds the AI personalization engine that generates first lines, email bodies, and follow-ups that feel like a human spent 15 minutes researching each prospect. You will configure OpenAI prompts, build the Make.com scenario that processes your lead list, and validate output quality before connecting it to your sending engine. Time required: 8–10 hours. Tools: Make.com, OpenAI API, Google Sheets.

## Procedure 5.1: Write Your Personalization Prompt Library

You will create three prompt templates in a Google Doc called "Personalization Prompts." Each serves a different purpose.

**Prompt 1: First Line Generator (for email opening)**

```
You are a senior SDR who writes hyper-personalized cold email first lines. 
Given the following information about a prospect, write ONE opening sentence 
that references something specific about them or their company. Rules:
- Do NOT mention AI, automation, or technology
- Do NOT use exclamation marks or emojis
- Do NOT write "I came across" or "I noticed" or "I saw"
- Reference the specific company news item if available
- If no news is available, reference their title or company growth stage
- Maximum 20 words
- Sound like a human who did 10 minutes of research
- Do not be overly complimentary

Prospect First Name: {{first_name}}
Prospect Title: {{title}}
Company: {{company_name}}
Company News: {{company_news}}

Write the first line:
```

**Prompt 2: Pain Point Email Body**

```
Write a cold email to {{first_name}} at {{company_name}}. 
They are a {{title}}.

Context: Our client [Client Company] helps [ICP description] achieve 
[outcome] through [method].

The email must:
1. Open with the first line provided below
2. Identify ONE specific pain point relevant to their role
3. Position [Client Company] as the solution without being salesy
4. End with a soft CTA: "Worth a 15-minute chat?" or "Open to seeing how this works?"
5. Be maximum 80 words total
6. Use short paragraphs (1-2 sentences each)
7. No links in the first email

First line: {{generated_first_line}}

Write the email:
```

**Prompt 3: Follow-Up Sequence Generator**

```
Write 3 follow-up emails for a cold outreach sequence to {{first_name}} 
at {{company_name}}.

Original email: {{original_email_body}}

Follow-up rules:
- Follow-up 1 (Day 4): Add one specific data point or case study result. 
  Max 40 words. "Just wanted to make sure this didn't get buried."
- Follow-up 2 (Day 8): Ask a direct question about their current process. 
  Max 35 words. "How are you currently handling [pain point]?"
- Follow-up 3 (Day 12): Breakup email. Max 25 words. 
  "Totally understand if the timing isn't right. I'll cross you off my list."

No links in follow-up 1. Calendly link OK in follow-up 2 and 3 only.
```

## Procedure 5.2: Build the AI Personalization Make.com Scenario

This scenario reads your Google Sheet lead list, sends each row to OpenAI for personalization, and writes the personalized emails back to a new sheet.

1. In Make.com, create a new scenario. Name it: `AI-Personalization-v1`.
2. Add module: **Google Sheets – Search Rows**
   - Spreadsheet: Select your lead list Google Sheet
   - Sheet: Select the sheet name
   - Filter: `sequence_tag` = `seq-pain-point` (or whatever tag you want to process)
   - Limit: 50 rows per run (do not process more than 50 at once — quality control)

3. Add module: **OpenAI (ChatGPT) – Create a Chat Completion**
   - Model: `gpt-4o-mini`
   - Temperature: 0.7 (higher = more creative, lower = more consistent)
   - Messages:
     - Role: `system`, Content: "You are a senior SDR who writes hyper-personalized cold emails."
     - Role: `user`, Content: Paste Prompt 1 from Procedure 5.1, replacing `{{variables}}` with Make.com mapping references:
       - `{{first_name}}` → mapped from Google Sheets `first_name` column
       - `{{title}}` → mapped from Google Sheets `title` column
       - `{{company_name}}` → mapped from Google Sheets `company_name` column
       - `{{company_news}}` → mapped from Google Sheets `company_news` column

4. Add module: **OpenAI (ChatGPT) – Create a Chat Completion** (second call)
   - Model: `gpt-4o-mini`
   - Temperature: 0.5
   - Messages:
     - Role: `system`, Content: "You write concise, effective cold emails."
     - Role: `user`, Content: Paste Prompt 2, mapping `{{generated_first_line}}` to the output of the previous OpenAI module.

5. Add module: **Google Sheets – Add Row**
   - Spreadsheet: Same Google Sheet, different sheet tab named "Personalized-Emails"
   - Columns to map:
     - `first_name` ← from step 2
     - `email` ← from step 2
     - `first_line` ← from step 3 output
     - `email_body` ← from step 4 output
     - `company_name` ← from step 2
     - `sequence_tag` ← from step 2

6. Set the scenario to run: **Manual trigger** (you will NOT auto-run this — you must review AI output first).

7. Click **Run once**. Process 5 contacts. Review the output in the "Personalized-Emails" tab.

## Procedure 5.3: Quality-Control AI Personalization Output

This procedure is non-negotiable. AI-generated emails WILL contain errors. You must catch them before they reach prospects.

Create a Google Doc called "AI Quality Log." For each batch of personalized emails:

1. **Hallucination check:** Does the email reference a fact about the company that is NOT in your data? If yes → rewrite manually. AI will fabricate funding rounds, product launches, and hires.
2. **Template check:** Does the email sound like a template with the name swapped? If yes → the prompt needs adjustment. Increase temperature to 0.8 or add more specific instructions.
3. **Length check:** Is the email over 80 words? If yes → truncate. Long emails do not get replies.
4. **Link check:** Does Email 1 contain any links? If yes → remove. First emails with links trigger spam filters and reduce reply rates by 40%.
5. **Name check:** Is the first name correct and properly capitalized? AI sometimes lowercases names or inserts weird characters.

Log every error in your Quality Log. Track the error rate per batch. If error rate exceeds 10%, STOP and refine your prompts before processing more leads.

{{% accent-box %}}HACK: Create a "golden example" folder with 20 manually written cold emails that produced replies. Include 3 examples directly in your OpenAI system prompt as reference. This is called few-shot prompting and reduces hallucination rates by 60%.{{% /accent-box %}}

## Check-In: Module 5 Complete

- [ ] Three personalization prompts written and saved in Google Doc
- [ ] Make.com scenario "AI-Personalization-v1" built with Google Sheets → OpenAI → Google Sheets flow
- [ ] Test run completed: 5 contacts processed, output reviewed
- [ ] AI Quality Log created with first batch errors documented
- [ ] Error rate below 10% on test batch (if not, prompts refined and retested)
- [ ] "Personalized-Emails" tab populated with first_line and email_body columns

---

# MODULE 6: CAMPAIGN BUILD IN MAKE.COM

## Overview

This is where everything connects. Your lead list, your AI-personalized emails, your sending infrastructure, and your analytics — all wired together through Make.com scenarios. This module builds the complete campaign automation that takes a lead from your Google Sheet, through personalization, through sending, through follow-up sequencing, and into your analytics dashboard.

You will build TWO Make.com scenarios: one for the primary send sequence and one for follow-ups. You will NOT use Apollo's native sequences as your primary sender — Make.com gives you far more control over timing, routing, and error handling. Time required: 10–14 hours. Tools: Make.com, Google Sheets, Instantly.ai (or SMTP direct).

## Procedure 6.1: Build the Primary Send Scenario

1. In Make.com, create a new scenario: `Primary-Send-v1`.

2. **Module 1: Google Sheets – Search Rows**
   - Spreadsheet: Your lead list
   - Sheet: "Personalized-Emails"
   - Filter: `sent_status` IS EMPTY (only unsent rows)
   - Limit: 10 (start conservative — you will scale up)
   - Sort: Row number ascending

3. **Module 2: Iterator** (to process rows one at a time)
   - Array: Output array from Module 1

4. **Module 3: Router** (split into two paths — one for Instantly, one for direct SMTP)

   **Path A: Instantly.ai (Recommended)**
   
   **Module 3A: HTTP – Make a Request**
   - URL: `https://api.instantly.ai/api/v1/campaigns/add-lead`
   - Method: POST
   - Headers:
     ```
     Content-Type: application/json
     Authorization: Bearer YOUR_INSTANTLY_API_KEY
     ```
   - Body:
     ```json
     {
       "campaign_id": "YOUR_CAMPAIGN_ID",
       "lead_email": "{{email}}",
       "lead_name": "{{first_name}} {{last_name}}",
       "personalization": "{{email_body}}",
       "company_name": "{{company_name}}"
     }
     ```
   
   **Path B: Direct SMTP (Backup)**
   
   **Module 3B: Email – Send an Email**
   - To: `{{email}}`
   - From: `{{sender_email}}`
   - Subject: Dynamically generated (see Procedure 6.2)
   - Content: `{{email_body}}`
   - SMTP: Google Workspace SMTP (`smtp.gmail.com`, port 587, TLS)

5. **Module 4: Google Sheets – Update Row**
   - Row number: from Module 2 output
   - Update column: `sent_status` → "sent"
   - Update column: `sent_date` → `{{now}}`
   - Update column: `sender_account` → the email address that sent

6. Set scenario schedule: **Every 30 minutes** during business hours (8 AM – 6 PM recipient timezone). Do not send outside business hours — reply rates drop 70%.

## Procedure 6.2: Write Subject Lines That Get Opened

Subject lines are NOT generated by AI. They are manually crafted and A/B tested. Create a subject line bank in your Notion SOPs page.

**High-performing subject line patterns for cold email:**

| Pattern | Example | Expected Open Rate |
|---------|---------|--------------------|
| Question | "still handling outbound manually?" | 45–55% |
| Specific result | "14 meetings in 12 days" | 50–60% |
| First name only | "{{first_name}}" | 40–50% |
| Pain point | "SDR hiring isn't scaling" | 45–55% |
| Curiosity gap | "your outbound stack is missing something" | 35–45% |

Rules:
- All lowercase (no capitalization — feels personal, not marketing)
- Under 5 words (short subjects get opened 26% more)
- No emojis, no links, no "Re:" prefix (fake Re: is illegal under CAN-SPAM)

For each campaign, prepare 3 subject line variants. Split your lead list into thirds. Track open rates by variant. After 200 sends per variant, kill the lowest performer and split traffic between the top two.

## Procedure 6.3: Build the Follow-Up Scenario

1. In Make.com, create a new scenario: `Follow-Up-Sequence-v1`.

2. **Module 1: Google Sheets – Search Rows**
   - Spreadsheet: Your lead list
   - Sheet: "Personalized-Emails"
   - Filter: `sent_status` = "sent" AND `reply_status` IS EMPTY AND `follow_up_stage` IS EMPTY
   - Limit: 20

3. **Module 2: Date Filter (Make.com built-in filter)**
   - Condition: `sent_date` → Date → "is more than" → 4 days ago (this creates the Day-4 follow-up timing)

4. **Module 3: OpenAI – Create a Chat Completion**
   - Model: `gpt-4o-mini`
   - Prompt: Follow-up 1 from your prompt library (Procedure 5.1, Prompt 3)
   - Map variables from the Google Sheet row

5. **Module 4: HTTP – Send via Instantly API** (same configuration as Procedure 6.1, Path A)

6. **Module 5: Google Sheets – Update Row**
   - Update `follow_up_stage` → "follow-up-1-sent"
   - Update `follow_up_1_date` → `{{now}}`

7. **Add a second branch** (click the + after the Router) for Follow-up 2:
   - Filter: `follow_up_stage` = "follow-up-1-sent" AND `reply_status` IS EMPTY AND `follow_up_1_date` is more than 4 days ago
   - Same OpenAI + Instantly + Google Sheets update flow
   - Update `follow_up_stage` → "follow-up-2-sent"

8. **Add a third branch** for Follow-up 3 (breakup):
   - Filter: `follow_up_stage` = "follow-up-2-sent" AND `reply_status` IS EMPTY AND `follow_up_2_date` is more than 4 days ago
   - Same flow
   - Update `follow_up_stage` → "breakup-sent"

9. Schedule: **Every 60 minutes** during business hours. Follow-ups should arrive at different times than the initial send.

{{% accent-box %}}HACK: Add a "reply detection" module between each follow-up stage. In Instantly, enable webhooks for reply events. In Make.com, add a Webhook module that updates `reply_status` = "replied" when a prospect responds. This prevents you from sending follow-up #2 to someone who already replied to follow-up #1 — the #1 agency embarrassment.{{% /accent-box %}}

## Procedure 6.4: Configure Sending Throttling and Domain Rotation

You must distribute sends across your domains and email accounts. Sending 200 emails from one account in a day = spam folder guaranteed.

**Daily sending limits per account:**

| Account Warmup Stage | Daily Send Limit |
|----------------------|------------------|
| Week 1 (new) | 10 cold emails/day |
| Week 2 | 20 cold emails/day |
| Week 3 | 30 cold emails/day |
| Week 4+ | 40 cold emails/day (maximum — never exceed) |

**Domain rotation strategy:**
- Assign each lead to a specific sender account in your Google Sheet
- In Make.com, add a **Set Variable** module before the send module:
  - Create a formula: If `ROW_NUMBER mod [number_of_accounts] = 0`, sender = account1; if `= 1`, sender = account2, etc.
- This distributes sends evenly across all accounts

**Time-of-day throttling:**
- 8:00 AM – 10:00 AM: 40% of daily volume (peak inbox checking time)
- 10:00 AM – 2:00 PM: 40% of daily volume
- 2:00 PM – 5:00 PM: 20% of daily volume
- After 5:00 PM: 0% (no sends)

In Make.com, use the built-in schedule with multiple time windows, or add a time-check filter module before the send module.

## Check-In: Module 6 Complete

- [ ] Primary-Send-v1 scenario built and tested with 5 contacts
- [ ] Subject line bank created with 3 variants per campaign
- [ ] Follow-Up-Sequence-v1 scenario built with 3 branches (Day 4, Day 8, Day 12)
- [ ] Reply detection webhook configured between Instantly and Make.com
- [ ] Sending throttling configured: 40 emails/day/account max, domain rotation active
- [ ] Time-of-day sending rules enforced (no after-hours sends)
- [ ] All test sends verified in recipient inbox (not spam, not promotions tab)

---

# MODULE 7: DELIVERY AND SENDING OPERATIONS

## Overview

Campaign launch is not the finish line — it is the starting line. This module covers the daily, weekly, and monthly operations that keep your agency running. Cold email is a living system: domains get blacklisted, accounts get flagged, reply rates fluctuate, and clients need reporting. Without operational discipline, a profitable campaign can become a deliverability disaster in 48 hours.

You will build the operational runbook — the exact tasks you perform every morning before your coffee gets cold. Time required: 4–6 hours to document. Ongoing: 30–60 minutes daily per client.

## Procedure 7.1: Build the Daily Operations Checklist

Create a Notion page called "Daily Operations Runbook." Copy this exactly:

```
DAILY OPERATIONS RUNBOOK — [Client Name]
Execute between 7:00 AM and 8:00 AM daily.

□ 1. Check Instantly.ai dashboard
   - All accounts: Health Score above 85%? → If NO, pause sending on that account
   - Any accounts flagged? → If YES, check MXToolbox blacklist status
   
□ 2. Check Google Workspace admin
   - Any security alerts? → If YES, investigate immediately
   - Any accounts locked? → If YES, unlock and reduce sending volume by 50%
   
□ 3. Review reply inbox (for all sender accounts)
   - Positive replies → Forward to client within 30 minutes
   - Objections → Log in "Objection Tracker" Notion database
   - Unsubscribes → Mark in Google Sheet, do NOT send again
   
□ 4. Check Make.com scenario execution log
   - Any failed operations? → If YES, fix and rerun
   - API errors from OpenAI? → If YES, check billing and rate limits
   - API errors from Instantly? → If YES, check API key and campaign status
   
□ 5. Update Campaign Tracker in Notion
   - Emails sent yesterday: [number]
   - Replies received yesterday: [number]
   - Meetings booked yesterday: [number]
   - Reply rate: [replies/sent]%
   
□ 6. Monitor domain blacklist status
   - Run MXToolbox blacklist check on all active domains
   - If blacklisted: pause all sending from that domain, submit delisting request
```

## Procedure 7.2: Handle Positive Replies

When a prospect replies positively (e.g., "Sure, let's chat," "Send me more info," "When are you free?"), you have a 15-minute window to respond before their attention shifts.

**Response protocol:**

1. Reply from the SAME sender account (not your personal email).
2. Template:

```
Hi [First Name],

Great to hear from you. Here's my calendar link — pick any time that works:

[CALENDLY_LINK]

Looking forward to connecting.

[Sender Name]
```

3. Forward the entire email thread to your client's designated contact within 30 minutes.
4. Update the Google Sheet: `reply_status` → "positive", `meeting_status` → "booking-in-progress".
5. Update Notion Campaign Tracker: increment "Meetings Booked" counter.

## Procedure 7.3: Handle Objections and Negative Replies

Not every reply is positive. Common objections and your responses:

| Objection | Response |
|-----------|----------|
| "Not interested" | "No worries at all. I'll cross you off my list. Have a great week." |
| "We already have a solution" | "Makes sense — most of our clients did too before switching. Mind if I send a 2-minute video showing the difference?" |
| "Send me more info" | Send a 1-page PDF case study. Do NOT send a 20-page deck. |
| "Wrong person" | "Appreciate the heads up. Who would be the right person to speak with?" |
| "How did you get my email?" | "I found your profile through public business directories. Happy to remove you from my list if you'd prefer." |

Log every objection in your Notion Objection Tracker. After 50 objections, analyze the pattern. If 30% say "wrong person," your ICP targeting is off. If 40% say "not interested," your value proposition is weak.

## Procedure 7.4: Manage Bounces and Deliverability Issues

1. **Hard bounces** (email does not exist): Mark `email_status` → "bounced" in Google Sheet. Remove from all future campaigns. These damage your sender reputation.
2. **Soft bounces** (mailbox full, temporary issue): Retry once after 48 hours. If still bounces, mark as "bounced."
3. **Spam complaints**: This is a red alert. If you receive more than 1 spam complaint per 1,000 emails sent, IMMEDIATELY:
   - Pause all sending from the affected account
   - Review the last 100 emails sent from that account for quality issues
   - Check if the lead list was poorly targeted (wrong ICP)
   - Reduce daily send volume by 50% when resuming

**Bounce rate threshold:** Keep below 3%. If your bounce rate exceeds 3%, your entire domain is at risk of blacklisting.

{{% accent-box %}}HACK: Set up Google Alerts for "spam report" + each of your sending domains. If anyone reports your emails as spam on social media or forums, you will know within hours. Reputation damage is easier to prevent than to repair.{{% /accent-box %}}

## Procedure 7.5: Build the Weekly Reporting Cadence

Every Friday at 4:00 PM, run this process for each active client:

1. Pull the week's data from your Analytics-RAW Google Sheet (you will build this in Module 8).
2. Calculate key metrics: emails sent, open rate, reply rate, positive reply rate, meetings booked, cost per meeting.
3. Write a 5-sentence summary in an email:
   - "This week we sent [X] emails, achieving a [Y]% reply rate."
   - "We booked [Z] meetings, bringing the monthly total to [A]."
   - "Top performing subject line: '[subject]' at [B]% open rate."
   - "One optimization we made: [change]."
   - "Next week's focus: [goal]."
4. Send the email to the client's designated contact.
5. Log the report in your Notion Campaign Tracker.

This weekly email is your retention tool. Clients who receive consistent, data-driven updates stay 3x longer than clients who are left wondering what you are doing.

## Check-In: Module 7 Complete

- [ ] Daily Operations Runbook created in Notion with all 6 daily checkpoints
- [ ] Positive reply protocol documented and tested (response within 15 minutes)
- [ ] Objection response templates created for all 5 common objections
- [ ] Objection Tracker database created in Notion
- [ ] Bounce management procedure active (hard bounces removed, soft bounces retried)
- [ ] Bounce rate below 3% on test campaign (if not, review lead quality)
- [ ] Weekly reporting cadence established (every Friday, 5-sentence summary)

---

# MODULE 8: ANALYTICS AND OPTIMIZATION

## Overview

You cannot scale what you cannot measure. This module builds the analytics infrastructure that tells you — and your clients — exactly what is working and what is not. Every number in your reports must be traceable to a specific action. "We sent some emails and got some replies" is not a report. "We sent 1,247 emails across 4 sequences, achieved a 6.2% reply rate, and booked 18 meetings at a cost of ₦12,500/meeting" is a report.

You will build a Make.com-powered analytics pipeline, create client-facing dashboards, and establish the optimization loop that improves results every single week. Time required: 6–8 hours. Tools: Make.com, Google Sheets, Notion.

## Procedure 8.1: Build the Analytics Data Pipeline

Create a new Google Sheet called "Analytics-RAW." This sheet collects every event from your campaigns. Columns:

```
date | client_name | campaign_name | sender_account | event_type | 
lead_email | sequence_position | subject_line_variant | 
icp_label | reply_type
```

Event types: `sent`, `opened`, `replied`, `meeting_booked`, `bounced`, `unsubscribed`, `spam_complaint`

In Make.com, modify your Primary-Send-v1 and Follow-Up-Sequence-v1 scenarios:

1. After every send action, add a **Google Sheets – Add Row** module pointing to Analytics-RAW.
2. Map: `event_type` → "sent", `date` → `{{now}}`, plus all other fields from the lead row.
3. For reply events (from your webhook), add a second Google Sheets – Add Row with `event_type` → "replied" (and `reply_type` → "positive", "negative", "neutral" based on AI classification — add an OpenAI module to classify the reply).

For open tracking: Instantly.ai provides open events via API. Add a scheduled Make.com scenario that pulls open data from Instantly every hour:

```
HTTP Module: GET https://api.instantly.ai/api/v1/analytics/opens
Headers: Authorization: Bearer YOUR_INSTANTLY_API_KEY
Params: campaign_id, start_date, end_date
```

Write each open event to Analytics-RAW.

## Procedure 8.2: Build the Client-Facing Dashboard

Create a Google Sheet called "Dashboard-[ClientName]" with these tabs:

**Tab 1: Weekly Summary**

| Metric | Week 1 | Week 2 | Week 3 | Week 4 |
|--------|--------|--------|--------|--------|
| Emails Sent | | | | |
| Open Rate | | | | |
| Reply Rate | | | | |
| Positive Reply Rate | | | | |
| Meetings Booked | | | | |
| Cost per Meeting | | | | |
| Bounce Rate | | | | |

Formulas (all reference Analytics-RAW via COUNTIFS):
- Open Rate: `=COUNTIFS(event_type,"opened",week,W1)/COUNTIFS(event_type,"sent",week,W1)`
- Reply Rate: `=COUNTIFS(event_type,"replied",week,W1)/COUNTIFS(event_type,"sent",week,W1)`
- Cost per Meeting: `=Monthly_Retainer/COUNTIFS(event_type,"meeting_booked",month,M1)`

**Tab 2: Sequence Performance**

| Sequence | Sent | Opened | Replied | Meeting Booked | Reply Rate | Meeting Rate |
|----------|------|--------|---------|----------------|------------|--------------|
| seq-pain-point | | | | | | |
| seq-social-proof | | | | | | |
| Follow-up 1 | | | | | | |
| Follow-up 2 | | | | | | |
| Breakup | | | | | | |

**Tab 3: Subject Line A/B Test**

| Variant | Subject Line | Sent | Opened | Open Rate |
|---------|-------------|------|--------|-----------|
| A | | | | |
| B | | | | |
| C | | | | |

Share this Google Sheet with your client (view-only access). Update it every Monday by 9 AM. This is your weekly deliverable alongside booked meetings.

## Procedure 8.3: Establish the Weekly Optimization Loop

Every Friday, run this optimization process:

**Step 1: Kill low performers.** If a subject line variant has an open rate more than 10 percentage points below the top performer after 300 sends, kill it. Reallocate volume to the winner.

**Step 2: Double down on high performers.** If an ICP segment has a 2x higher reply rate than average, build a dedicated sequence for that segment. Create a new Apollo saved search targeting that ICP more aggressively.

**Step 3: Fix the leaky bucket.** If your open rate is above 40% but reply rate is below 4%, your email body is the problem. Rewrite the body. If your open rate is below 30%, your subject line or your sender reputation is the problem. Check deliverability first (MXToolbox), then test new subject lines.

**Step 4: Optimize send times.** Look at your Analytics-RAW data. Filter for `event_type = "replied"`. What time did those emails arrive? What day? Adjust your Make.com schedule to concentrate sends during those high-conversion windows.

**Step 5: Review the objection log.** Any recurring objections? If 20%+ of objections are the same type, write a proactive response into your sequence (e.g., if "we already use [competitor]" is common, add a line in Email 1 acknowledging alternatives).

{{% accent-box %}}HACK: The single highest-leverage optimization is reply speed. When a positive reply comes in, the chance of booking a meeting drops 10x if you respond after 1 hour versus 15 minutes. Automate the initial reply (Procedure 7.2) and you will see a 40% increase in meetings booked from the same number of positive replies.{{% /accent-box %}}

## Procedure 8.4: Build the Monthly Client Report

Create a Notion template called "Monthly Outbound Report." Structure:

```
# Monthly Outbound Report — [Client Name] — [Month]

## Executive Summary
- [X] meetings booked (vs. [target])
- [X]% reply rate (vs. [previous month])
- ₦[X] cost per meeting (vs. [previous month])

## Volume Metrics
- Emails sent: [X]
- Unique contacts reached: [X]
- Sequences active: [X]

## Performance by Sequence
[Table from Tab 2 of Dashboard]

## Top Performing Subject Lines
1. "[subject line]" — [X]% open rate
2. "[subject line]" — [X]% open rate
3. "[subject line]" — [X]% open rate

## ICP Segment Analysis
[Which ICP segments performed best/worst]

## Optimization Actions Taken
1. [Action and result]
2. [Action and result]

## Recommendations for Next Month
1. [Specific recommendation]
2. [Specific recommendation]
3. [Specific recommendation]
```

Generate this report on the 1st of every month. Send it as a PDF (export from Notion). Schedule a 30-minute review call with the client within the first week of the month.

## Check-In: Module 8 Complete

- [ ] Analytics-RAW Google Sheet created with all 10 event columns
- [ ] Analytics pipeline wired into Make.com scenarios (events logged for every send/reply/open)
- [ ] Client-facing dashboard built with Weekly Summary, Sequence Performance, and A/B Test tabs
- [ ] Dashboard shared with client (view-only, updated every Monday)
- [ ] Weekly optimization loop documented and executed (kill low performers, double down on high)
- [ ] Monthly client report template created in Notion
- [ ] First monthly report generated and delivered

---

# MODULE 9: SCALING AND TEAM OPERATIONS

## Overview

You can manage 3 clients alone. At 5 clients, you will drown in operations. At 10 clients, you need a team. This module covers the exact hiring profiles, onboarding procedures, and operational systems that let you scale from ₦2M/month to ₦12M/month without breaking the machine you built in Modules 1–8.

Scaling is not "do more of the same." It is "build systems that let other people do what you did, at 80% of your quality, at 20% of your cost." That 80/20 ratio is the key insight. Perfect is the enemy of scalable. Time required: 10–15 hours to build systems. Ongoing: hire as needed.

## Procedure 9.1: Define Your Hiring Roadmap

You will hire in this exact order. Do not skip steps.

| Role | When to Hire | Monthly Salary (₦) | Key Skill |
|------|-------------|---------------------|-----------|
| Outbound Specialist | At 3 clients | ₦200,000–₦350,000 | Apollo.io + Make.com + copywriting |
| Deliverability Tech | At 5 clients | ₦250,000–₦400,000 | DNS, email infrastructure, warmup management |
| Client Success Manager | At 7 clients | ₦200,000–₦300,000 | Client communication, reporting, objection handling |
| AI Prompt Engineer | At 10 clients | ₦300,000–₦500,000 | OpenAI prompting, output quality, model selection |
| Sales/Closer | At 12 clients | ₦150,000 base + ₦100,000 commission | Selling outbound services to new clients |

**Total team cost at 12 clients: ₦1.1M–₦1.85M/month**

At 12 clients on the Retainer + Performance model (₦750K/month + ₦225K average overage), you are generating ₦11.7M/month. Team cost is ₦1.85M. Tool cost is ~₦500K. Margin: **₦9.35M/month (80% margin).**

## Procedure 9.2: Build SOPs for Each Role

Every task in your agency must be documented as a Standard Operating Procedure. No SOP = no delegation. No delegation = no scaling.

Create the following SOPs in your Notion "SOPs" page:

**SOP: Lead Research**
1. Open Apollo.io → Search → People
2. Load saved search for client ICP
3. Export CSV (max 2,000 contacts per export)
4. Import to Clay for enrichment
5. Run email verification
6. Remove invalid and catch-all emails
7. Add `company_news` enrichment column
8. Export final CSV with all 10 required columns
9. Upload to Google Sheets named `[Client]-LeadList-[Date]`
10. Notify Campaign Manager: "Lead list ready for personalization"

**SOP: AI Personalization Quality Check**
1. Run Make.com scenario "AI-Personalization-v1" on new lead list (batch of 50)
2. Open "Personalized-Emails" tab in Google Sheets
3. Check 10 random emails for: hallucinations, length (under 80 words), no links in Email 1, correct names
4. If error rate > 10%, refine prompt and rerun
5. If error rate < 10%, approve batch for sending
6. Log results in AI Quality Log

**SOP: Client Onboarding**
1. Send client onboarding form (Google Form): company name, ICP description, value proposition, 3 competitor names, target geographies, exclusions, CRM details
2. Create client folder in Notion with: ICP one-pager, campaign tracker, domain inventory
3. Procure 3–5 sending domains (Procedure 4.1)
4. Configure DNS records for all domains (Procedure 4.2)
5. Create Google Workspace accounts (Procedure 4.3)
6. Start Instantly.ai warmup (Procedure 4.4)
7. Build Apollo saved searches based on client ICP (Procedure 3.2)
8. Write personalization prompts specific to client value prop (Procedure 5.1)
9. Configure Make.com scenarios for this client (duplicate and customize templates)
10. Set up Analytics dashboard (Procedure 8.2)
11. Schedule first weekly check-in

{{% accent-box %}}HACK: Record yourself performing each SOP using Loom (https://loom.com). A 5-minute video is worth 2 pages of text. When onboarding a new Outbound Specialist, assign them 3 Loom videos on Day 1 and have them execute the SOPs on a test client. This cuts onboarding time from 2 weeks to 3 days.{{% /accent-box %}}

## Procedure 9.3: Build the Client Acquisition Engine for Your Agency

Your agency is a cold email outreach agency. You will use cold email outreach to acquire clients for your cold email outreach agency. This is not ironic — it is proof of concept.

**Your agency's ICP (from Procedure 1.2):** B2B SaaS, ₦50M+ ARR, VP Sales/Head of Growth buyer.

**Your agency's outbound sequence:**

**Email 1:**

```
subject: {{first_name}}

Hey {{first_name}},

{{personalized_first_line_based_on_company_news}}

Most {{icp_label}} companies we work with are spending ₦2M–₦5M/month on SDRs 
who book 3–5 meetings if they're lucky. We built an AI outbound engine that 
books 15–20 meetings/month for less than half that cost.

Worth a 15-minute chat?

[Sender Name]
```

**Follow-up 1 (Day 4):**

```
subject: re: {{first_name}}

Just floating this up — our clients see an average 12% reply rate on cold 
outreach. Industry average is 2%.

Open to seeing how?
```

**Follow-up 2 (Day 8):**

```
subject: re: {{first_name}}

How are you currently scaling outbound? 

If the answer involves hiring more SDRs, we should talk. Here's my calendar:
[CALENDLY_LINK]
```

**Breakup (Day 12):**

```
subject: re: {{first_name}}

Totally understand if the timing isn't right. I'll cross you off my list.

If things change, you know where to find me.

[Sender Name]
```

Send 100 emails/day across 3 sender accounts targeting your own ICP. Expected results at 5% positive reply rate: 5 conversations/day → 2 meetings/day → 10 meetings/week. Close rate at 25%: 2.5 new clients/week.

## Procedure 9.4: Systematize Client Onboarding

When a new client signs, execute this onboarding sequence in exactly this order. No deviations.

**Day 0 (Contract Signed):**
- Send welcome email with onboarding form link
- Create Notion client folder
- Procure sending domains (takes 1–2 days to propagate DNS)

**Day 1–3:**
- Configure all DNS records (SPF, DKIM, DMARC, MX, CNAME)
- Create Google Workspace accounts
- Start Instantly.ai warmup on all accounts

**Day 4–7:**
- Build Apollo saved searches based on client ICP
- Write and test personalization prompts for client's value prop
- Build first lead list (500–1,000 contacts)
- Run AI personalization on first batch

**Day 8–14:**
- Quality check AI-personalized emails
- Configure Make.com scenarios for this client
- Set up Analytics dashboard
- Continue warmup (accounts not yet at full sending capacity)

**Day 15–17:**
- Begin sending at 50% volume (half of full sending capacity)
- Monitor deliverability closely
- First weekly check-in with client

**Day 18–21:**
- Scale to full sending volume
- Activate follow-up sequence
- First weekly report delivered

**Day 28–30:**
- First monthly report
- 30-day review call
- Optimize based on data

## Check-In: Module 9 Complete

- [ ] Hiring roadmap documented with all 5 roles, triggers, and salary ranges
- [ ] All 3 SOPs written in Notion (Lead Research, AI Personalization QC, Client Onboarding)
- [ ] Loom videos recorded for each SOP
- [ ] Agency outbound sequence created and sending (100 emails/day to own ICP)
- [ ] Client onboarding system documented with Day 0–30 timeline
- [ ] At least 1 new team member hired or in hiring pipeline (at 3+ clients)

---

# MODULE 10: FINANCIAL OPERATIONS AND PRICING ARCHITECTURE

## Overview

Money in, money out. If you cannot track it, you cannot optimize it. This module covers pricing architecture, invoicing, expense management, and the financial model that takes your agency from ₦2M/month to ₦12M/month with 75–80% margins. You will build a financial tracker, set up recurring invoicing, and model three growth scenarios.

Every number in this module is denominated in Naira (₦). If you bill international clients in USD, convert at the prevailing CBN rate on the date of invoice. Time required: 4–6 hours. Tools: Notion, Stripe/Paystack, Google Sheets.

## Procedure 10.1: Establish Your Three-Tier Pricing Model

You will offer three pricing tiers. Every prospect receives a proposal with all three tiers. The middle tier is designed to be the obvious choice (anchoring effect).

| Feature | Starter | Growth | Enterprise |
|---------|---------|--------|------------|
| **Monthly Retainer** | ₦500,000 | ₦1,200,000 | ₦2,500,000 |
| **Included Meetings** | 4 | 10 | 25 |
| **Overage per Meeting** | ₦20,000 | ₦15,000 | ₦10,000 |
| **Sending Domains** | 2 | 4 | 8 |
| **Email Accounts** | 4 | 8 | 16 |
| **Lead List Volume** | 1,000 contacts/month | 3,000 contacts/month | 10,000 contacts/month |
| **AI Personalization** | Standard prompts | Custom prompts + A/B testing | Custom prompts + A/B + multivariate |
| **Follow-Up Sequences** | 2-step | 4-step | 4-step + multichannel (LinkedIn) |
| **Analytics Dashboard** | Weekly email report | Real-time Google Sheet | Real-time + monthly strategy call |
| **Dedicated Account Manager** | No | Yes | Yes + priority Slack channel |
| **Contract Minimum** | 3 months | 3 months | 6 months |
| **Setup Fee** | ₦150,000 | ₦250,000 | ₦500,000 |

**Your delivery cost per client (Growth tier):**

| Cost Item | Monthly Cost (₦) |
|-----------|-------------------|
| Domains (4 × ₦5,000) | 20,000 |
| Google Workspace (8 × ₦4,500) | 36,000 |
| Instantly.ai (Growth plan) | 50,000 |
| Apollo.io (1 Pro seat) | 75,000 |
| Make.com (10K ops) | 12,000 |
| OpenAI API | 30,000 |
| Clay enrichment | 75,000 |
| Outbound Specialist (1/4 time) | 75,000 |
| **Total Cost** | **373,000** |

**Growth tier margin: ₦1,200,000 – ₦373,000 = ₦827,000/month (69% margin)**

With setup fee of ₦250,000, first-month margin is ₦1,077,000.

## Procedure 10.2: Build the Financial Tracker

Create a Google Sheet called "Agency-Financials." Structure:

**Tab 1: Revenue Tracker**

| Client | Tier | Monthly Retainer | Meetings Delivered | Overage Revenue | Total Monthly Revenue | Contract Start | Renewal Date |
|--------|------|-----------------|-------------------|-----------------|----------------------|----------------|--------------|
| | | | | | | | |

**Tab 2: Expense Tracker**

| Category | Vendor | Amount (₦) | Billing Cycle | Next Payment Date | Auto-Renew? |
|----------|--------|------------|---------------|-------------------|-------------|
| Domains | Namecheap | | Yearly | | Yes |
| Email Hosting | Google Workspace | | Monthly | | Yes |
| Sending | Instantly.ai | | Monthly | | Yes |
| Lead Data | Apollo.io | | Monthly | | Yes |
| Automation | Make.com | | Monthly | | Yes |
| AI | OpenAI | | Monthly (usage) | | No |
| Enrichment | Clay | | Monthly | | Yes |
| Salaries | Team | | Monthly | | No |
| Miscellaneous | | | | | |

**Tab 3: Profit & Loss (Monthly)**

| Month | Total Revenue | Total Expenses | Net Profit | Margin % | Clients | Revenue/Client |
|-------|--------------|----------------|------------|----------|---------|----------------|
| Month 1 | | | | | | |
| Month 2 | | | | | | |
| ... | | | | | | |

## Procedure 10.3: Set Up Recurring Invoicing

**For Nigerian clients:** Use Paystack (https://paystack.com).

1. Create a Paystack business account.
2. Set up a recurring payment plan:
   - Plan name: "Outbound Agency — Growth Tier"
   - Amount: ₦1,200,000
   - Interval: Monthly
   - Send invoice on: 1st of each month
3. Share payment link with client. They enter card details once. Paystack auto-charges monthly.

**For US/international clients:** Use Stripe (https://stripe.com).

1. Create a Stripe account (requires Wyoming LLC or equivalent).
2. Set up a Subscription product:
   - Product: "AI Outbound Agency — Growth Tier"
   - Price: $800/month (convert ₦1,200,000 at prevailing rate)
   - Billing cycle: Monthly
3. Share Stripe Payment Link with client.

**For one-time setup fees:** Send a single invoice via Paystack or Stripe. Do NOT waive setup fees. They cover your initial infrastructure cost and signal commitment from the client.

{{% accent-box %}}HACK: Add a clause to every contract: "Payment is due within 5 business days of invoice date. Late payments incur a 5% penalty per week. Services will be paused after 14 days of non-payment." You are not a bank. Do not finance your clients' cash flow problems.{{% /accent-box %}}

## Procedure 10.4: Model Three Growth Scenarios

Create a "Growth Model" tab in your Agency-Financials Google Sheet:

**Conservative (1 new client/month):**

| Month | Clients | Monthly Revenue (₦) | Monthly Expenses (₦) | Net Profit (₦) |
|-------|---------|---------------------|----------------------|-----------------|
| 1 | 1 | 1,450,000 | 373,000 | 1,077,000 |
| 3 | 3 | 4,350,000 | 1,119,000 | 3,231,000 |
| 6 | 6 | 8,700,000 | 2,238,000 | 6,462,000 |
| 12 | 12 | 17,400,000 | 4,476,000 | 12,924,000 |

**Moderate (2 new clients/month):**

| Month | Clients | Monthly Revenue (₦) | Monthly Expenses (₦) | Net Profit (₦) |
|-------|---------|---------------------|----------------------|-----------------|
| 1 | 2 | 2,900,000 | 746,000 | 2,154,000 |
| 3 | 6 | 8,700,000 | 2,238,000 | 6,462,000 |
| 6 | 12 | 17,400,000 | 4,476,000 | 12,924,000 |
| 12 | 24 | 34,800,000 | 8,952,000 | 25,848,000 |

**Aggressive (3 new clients/month):**

| Month | Clients | Monthly Revenue (₦) | Monthly Expenses (₦) | Net Profit (₦) |
|-------|---------|---------------------|----------------------|-----------------|
| 1 | 3 | 4,350,000 | 1,119,000 | 3,231,000 |
| 3 | 9 | 13,050,000 | 3,357,000 | 9,693,000 |
| 6 | 18 | 26,100,000 | 6,714,000 | 19,386,000 |
| 12 | 36 | 52,200,000 | 13,428,000 | 38,772,000 |

Note: These models assume all clients are on the Growth tier (₦1.2M/month). Actual mix will vary. Track real numbers in your Financial Tracker and compare against these models monthly.

## Procedure 10.5: Manage Client Churn and Renewals

Churn kills agencies. Your target: under 5% monthly churn.

**Churn prevention checklist (run monthly for each client):**

1. Is the client receiving 10+ meetings/month? → If NO, this is a churn risk. Escalate immediately.
2. Is the client responding to your weekly reports? → If NO, they are disengaged. Schedule a call.
3. Has the client's business changed (new ICP, new product, layoff)? → If YES, update their campaign.
4. Is the renewal date within 60 days? → If YES, schedule a renewal conversation. Present results and propose next-term improvements.

**Renewal conversation script:**

```
"Hey [Client Name], I wanted to review our last [X] months together.

We've booked [Y] meetings at a cost of ₦[Z] per meeting. That's [A]% 
better than the industry average for outbound.

For the next term, I'd recommend [specific improvement — new ICP segment, 
additional sequence, multichannel expansion]. This should push us to 
[B] meetings/month.

Would you like to continue at the current tier, or should we discuss 
scaling up?"
```

If a client does decide to churn:
1. Ask for a candid exit reason. Log it.
2. Offer a 30-day pause instead of full cancellation (sometimes they just need time).
3. Transfer their domains and data within 7 days (contractual obligation).
4. Reallocate their infrastructure to a new client immediately.

## Procedure 10.6: Annual Financial Review and Reinvestment

Every December, conduct an annual review:

1. **Revenue:** What was total annual revenue? How did it compare to your model?
2. **Margins:** What was average monthly margin? Target: 70%+. Below 60% means you have a cost problem.
3. **Client concentration:** Is any single client more than 25% of revenue? If yes, that is a risk. Diversify.
4. **Tool cost optimization:** Review every tool subscription. Are you using all seats? Can you negotiate annual pricing (usually 15–20% discount)?
5. **Team efficiency:** Revenue per team member. Target: ₦3M+/month per team member.
6. **Reinvestment:** Allocate 15–20% of net profit to: new tool evaluation, team training, and infrastructure expansion.

{{% accent-box %}}HACK: Negotiate annual contracts with Apollo.io, Instantly.ai, and Make.com. Pre-paying for 12 months typically saves 15–25%. At your scale, that is ₦500K–₦1.5M saved per year. That is a junior team member's salary.{{% /accent-box %}}

## Check-In: Module 10 Complete

- [ ] Three-tier pricing model documented (Starter ₦500K, Growth ₦1.2M, Enterprise ₦2.5M)
- [ ] Delivery cost per client calculated (Growth tier: ₦373,000/month, 69% margin)
- [ ] Agency-Financials Google Sheet created with Revenue, Expense, and P&L tabs
- [ ] Recurring invoicing configured via Paystack (Nigerian clients) and Stripe (international clients)
- [ ] Three growth scenarios modeled in spreadsheet
- [ ] Churn prevention checklist documented and running monthly
- [ ] Renewal conversation script written and tested

---

# COMPLETION: YOUR AGENCY IS LIVE

You have built the complete operating system. 44 procedures executed across 10 modules. Here is what you now own:

**Infrastructure:** Multiple sending domains with full DNS configuration, Google Workspace accounts, warmup running, deliverability verified.

**Automation:** Make.com scenarios for AI personalization, primary sending, follow-up sequences, and analytics collection — all running on schedule.

**Data:** Apollo.io saved searches for your ICP, Clay-enriched lead lists, verified email data flowing through your pipeline.

**AI Engine:** OpenAI-powered personalization with quality-controlled prompts, generating hyper-relevant emails that achieve 5–8% reply rates.

**Operations:** Daily runbook, weekly optimization loop, monthly client reports, objection tracking, and bounce management.

**Financials:** Three-tier pricing, recurring invoicing, growth models, and churn prevention — all tracked in a central financial dashboard.

**Scaling Roadmap:** Hiring plan, SOPs with Loom video documentation, client onboarding system, and your own agency outbound engine running 100 emails/day to acquire new clients.

**Your next 30 days:**

1. Sign your first client (use your own outbound engine from Procedure 9.3).
2. Execute the full onboarding sequence (Procedure 9.4).
3. Send your first campaign on Day 15.
4. Deliver your first weekly report on Day 21.
5. Book your first 10 meetings by Day 30.
6. Use those results to sign Client #2.
7. Repeat.

The machine is built. Now turn it on.
