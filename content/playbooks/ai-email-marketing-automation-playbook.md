---
title: "The AI Email Marketing Automation Playbook: 52 Steps to $5K/Month"
date: 2026-05-01
category: "Playbook"
price: "₦35,000"
readTime: "90 MIN"
excerpt: "The complete operating system for building an AI email marketing automation business from zero. 10 modules, 36 procedures, exact tool configurations, client acquisition scripts, three pricing tiers, and a scaling roadmap. From empty Klaviyo account to ₦12M/month in recurring revenue."
image: "/images/articles/playbooks/ai-email-marketing-automation-playbook.png"
heroImage: "/images/heroes/playbooks/ai-email-marketing-automation-playbook.png"
relatedOpportunity: "/opportunities/how-to-build-ai-powered-email-marketing-automation-in-2026-5000month-revenue-pot/"
relatedGuide: "/intelligence/deploy-ai-email-marketing-automations/"
---

This is not a blog post condensed into a PDF. This is an operating system for building an AI-powered email marketing automation business. Every module contains exact procedures — not theories, not possibilities, not "consider doing X." You will do X, in this order, with these tools, and you will verify it worked before moving on.

**36 procedures. 10 modules. 90+ hours of reading and execution.**

---

# MODULE 1: FOUNDATION & BUSINESS ARCHITECTURE

## Overview

You are not building an "email marketing agency." You are building a revenue infrastructure company that uses AI to deliver measurable ROI through email. The distinction is not semantic — it determines what you charge, who you sell to, and how you scale. Every agency sends emails. A revenue infrastructure company owns the systems that turn subscribers into revenue. Your client does not pay you to write newsletters. They pay you because every ₦1 they spend on your service generates ₦15-₦35 in attributed revenue. That ratio is your entire business.

Before you touch a single tool, you will lock down three things: your business entity, your service definition, and your financial architecture. Skipping any of these guarantees failure at scale — you will either lose money on taxes, attract the wrong clients, or fly blind on profitability.

## Procedure 1.1: Register Your Business Entity

1. Go to [cac.gov.ng](https://cac.gov.ng) and register a Limited Liability Company. Name format: `[Your Brand] Digital Ltd.` or `[Your Brand] Marketing Technologies Ltd.` Do not register as a sole proprietorship — you need the liability shield when clients dispute attributed revenue numbers.
2. Cost: ₦25,000–₦30,000 including name reservation and filing.
3. Timeline: 7–14 business days. Begin this immediately. You will complete Modules 2–4 while waiting.
4. Obtain your Tax Identification Number (TIN) from [firrs.gov.ng](https://firrs.gov.ng). This takes 48 hours.
5. Open a business bank account with Moniepoint, OPay Business, or Wema Bank. You need a dedicated account that separates business revenue from personal funds. If you commingle, you will have no idea what your margins are by month 3.

## Procedure 1.2: Define Your Service Architecture

Your service has three tiers. Do not customize pricing per client. Do not negotiate. The tiers exist to make the buying decision simple and to anchor the client to the middle tier.

| Tier | Name | Monthly Fee | What's Included | Target Client |
|------|------|-------------|-----------------|---------------|
| 1 | Starter | ₦150,000 | 4 email flows, 2 campaigns/month, basic segmentation, monthly report | E-commerce stores doing ₦5M–₦20M/month revenue |
| 2 | Growth | ₦350,000 | 8 email flows, 4 campaigns/month, AI segmentation, A/B testing, biweekly report, ChatGPT content engine | E-commerce stores doing ₦20M–₦80M/month revenue |
| 3 | Enterprise | ₦750,000 | 12+ email flows, unlimited campaigns, advanced AI segmentation, full A/B program, weekly report, dedicated Slack channel, quarterly strategy review | E-commerce stores doing ₦80M+/month revenue |

Write these tiers into a one-page PDF. This is your rate card. You will send this PDF to prospects. You will not deviate from it.

## Procedure 1.3: Set Up Your Financial Tracking

1. Create a Notion workspace at [notion.so](https://notion.so). Name it `[Your Brand] Operations`.
2. Inside this workspace, create three databases:
   - **Clients**: Columns — Client Name, Tier, Monthly Fee, Start Date, Status (Active/Churned), MRR Contribution, Next Renewal Date
   - **Revenue Tracker**: Columns — Month, Total MRR, New MRR, Churned MRR, Net New MRR, Tool Costs, Net Profit
   - **Task Board**: Columns — Task Name, Client, Status (To Do / In Progress / Review / Done), Due Date, Assignee
3. Track every ₦ from day one. If you cannot tell me your net profit margin within 60 seconds of being asked, your financial tracking is broken.

{{% accent-box %}}HACK: Create a "MRR Clock" in Notion — a formula property that multiplies each client's monthly fee by 12 and displays annualized revenue. When you see ₦4,200,000 in annualized recurring revenue from just one Growth-tier client, it changes how you value every prospect call and every hour of work. The MRR Clock is a psychological tool that keeps you selling when you'd rather stop.{{% /accent-box %}}

## Check-In: Module 1 Complete

- [ ] Business entity registered with CAC
- [ ] TIN obtained from FIRS
- [ ] Business bank account opened
- [ ] Three-tier rate card written and saved as PDF
- [ ] Notion operations workspace created with three databases
- [ ] At least one test client entry added to the Clients database

---

# MODULE 2: TECH STACK CONFIGURATION

## Overview

You will configure exactly seven tools. Not six. Not eight. Seven. Every tool in this stack has a specific job. Every tool connects to at least one other tool. If a tool does not integrate or does not serve a measurable purpose, it does not enter the stack. Tool sprawl kills margins. Every ₦1 you spend on a tool that does not directly produce revenue is a ₦1 stolen from your profit.

## Procedure 2.1: Configure Klaviyo (Primary ESP for E-Commerce)

1. Go to [klaviyo.com](https://klaviyo.com) and create an account. Select the "Email + SMS" plan.
2. Pricing at launch (under 250 contacts): ₦0 free tier. You will upgrade when you cross 250 contacts. The ₦0 tier gives you 500 emails/month. This is enough for your first client.
3. Install the Klaviyo snippet on your client's store:
   - **Shopify**: Go to Klaviyo → Integrations → Shopify → Click "Install" → Authorize. Done in 90 seconds.
   - **WooCommerce**: Go to Klaviyo → Integrations → WooCommerce → Copy the API key → Install the [Klaviyo WooCommerce plugin](https://wordpress.org/plugins/klaviyo/) → Paste API key in Settings → Enable "Track Added to Cart" and "Track Checkout Start."
4. Verify the integration: Go to Klaviyo → Analytics → Activity Feed. Add an item to cart on the client store. If the activity appears within 60 seconds, the integration works. If it does not, recheck the API key and JavaScript snippet placement.
5. Enable double opt-in: Go to Klaviyo → Account → Settings → Email → Set "Double Opt-In" to "On." This protects deliverability. Do not skip this.

## Procedure 2.2: Configure ActiveCampaign (Primary ESP for Non-E-Commerce & B2B)

1. Go to [activecampaign.com](https://activecampaign.com) and create an account. Select the "Plus" plan at $49/month (approximately ₦78,000/month).
2. Configure your sending domain:
   - Go to Settings → Advanced → Domain Settings → Add Domain → Enter `mail.[clientdomain].com`
   - Add the three CNAME records and one TXT record to the client's DNS. Provide these exact values to the client's IT person:
     ```
     CNAME: em.key1._domainkey.[clientdomain].com → dkim1.activecampaign.com
     CNAME: em.key2._domainkey.[clientdomain].com → dkim2.activecampaign.com
     CNAME: mail.[clientdomain].com → send.acemlna.com
     TXT: [clientdomain].com → "v=spf1 include:acemlna.com ~all"
     ```
3. Verify: Go back to Settings → Advanced → Domain Settings → Click "Verify." If the checkmarks turn green, you are done. If not, DNS propagation may take up to 48 hours. Set a calendar reminder to re-verify.
4. Set up the site tracking snippet: Go to Settings → Tracking → Copy the JavaScript snippet → Paste it before the `</head>` tag on every page of the client's website.
5. Enable event tracking: Go to Settings → Tracking → Event Tracking → Enable "Track Events" → Add events: `form_submit`, `page_view`, `purchase`, `trial_start`.

## Procedure 2.3: Configure ChatGPT (Content Engine)

1. Go to [chat.openai.com](https://chat.openai.com) and subscribe to ChatGPT Plus at $20/month (approximately ₦32,000/month).
2. Create a Custom GPT named "Email Copy Engine." Configure it with the following system prompt:

```
You are an elite email marketing copywriter who writes for African e-commerce and B2B brands. You never use the phrase "I hope this email finds you well." You never write subject lines longer than 45 characters. You always include a single clear CTA. You write at a 6th-grade reading level. You use short paragraphs — maximum 2 sentences each. You always quantify claims. You write in the brand voice provided. When no brand voice is provided, default to: direct, warm, slightly urgent, never corporate.

Output format for every email:
- Subject line (45 chars max)
- Preview text (90 chars max)
- Email body (HTML-ready, using <p>, <strong>, <a> tags)
- CTA button text (5 words max)
- Sending time recommendation (day + time in WAT)
```

3. Save the Custom GPT. You will use it in Module 5.

## Procedure 2.4: Configure Make.com (Automation Orchestration)

1. Go to [make.com](https://www.make.com/en/register?pc=menshly) and create an account. Select the "Core" plan at €9/month (approximately ₦16,000/month).
2. Connect the following modules in Make.com:
   - Klaviyo (OAuth connection)
   - ActiveCampaign (API key + URL from Settings → Developer)
   - ChatGPT (API key from [platform.openai.com](https://platform.openai.com) → API Keys → Create New Key)
   - Google Sheets (OAuth connection)
   - Slack (OAuth connection — for internal alerts)
3. Test each connection by creating a simple scenario: "Watch Google Sheet → Send a test Slack message." If the message arrives, your connections work.

## Procedure 2.5: Configure Google Sheets (Data Backbone)

1. Create a Google Sheet named `[Client Name] — Email Operations`.
2. Create four tabs:
   - **Campaign Calendar**: Columns — Send Date, Campaign Name, Segment, Subject Line, Status (Draft/Scheduled/Sent)
   - **Flow Performance**: Columns — Flow Name, Trigger, Entry Rate, Open Rate, Click Rate, Revenue, Status (Live/Paused)
   - **A/B Test Log**: Columns — Test Date, Element Tested, Variant A, Variant B, Winner, Lift %
   - **Revenue Attribution**: Columns — Date, Email/Flow Name, Attributed Revenue, Orders, AOV
3. Share this sheet with your client using "Viewer" permissions. This sheet is your monthly reporting backbone.

## Procedure 2.6: Configure Canva (Visual Asset Production)

1. Go to [canva.com](https://canva.com) and subscribe to Canva Pro at $13/month (approximately ₦21,000/month).
2. Create a Brand Kit for each client: upload their logo, set their primary color (#hex), secondary color (#hex), and font pair (one heading font, one body font).
3. Create three email header templates (1200×400px): promotional, educational, transactional. Save them in a folder named `[Client Name] — Email Assets`.

## Procedure 2.7: Configure Slack (Client Communication)

1. Create a Slack workspace named `[Your Brand] Clients`. Use the free plan.
2. For each client, create a private channel named `#client-[brandname]`.
3. Invite the client's point of contact to their channel.
4. Set channel topic to: "Weekly performance updates and urgent communications. Response time: 4 business hours."
5. Install the Make.com Slack integration so that critical flow errors and revenue milestones automatically post to the client channel.

{{% accent-box %}}HACK: Never give clients your personal WhatsApp number. The moment a client has your WhatsApp, every "quick question" at 11 PM becomes your problem. Slack channels create professional boundaries, keep communication searchable, and let you bring team members into conversations without sharing phone numbers. If a client insists on WhatsApp, create a WhatsApp Business account with automated away hours. But push for Slack — it is the difference between a freelance gig and a real business.{{% /accent-box %}}

## Check-In: Module 2 Complete

- [ ] Klaviyo account created and integrated with at least one client store
- [ ] ActiveCampaign account created with custom sending domain configured
- [ ] ChatGPT Plus subscribed and Custom GPT "Email Copy Engine" created
- [ ] Make.com Core plan active with all five module connections tested
- [ ] Google Sheets operations workbook created with four tabs
- [ ] Canva Pro active with Brand Kit for at least one client
- [ ] Slack workspace created with at least one client channel

---

# MODULE 3: EMAIL INFRASTRUCTURE SETUP

## Overview

Deliverability is the foundation of everything. If your emails land in spam, nothing else matters — not your copy, not your segmentation, not your automation flows. You will configure the technical infrastructure that ensures every email reaches the inbox. This module is the least glamorous and the most critical. A 5% improvement in inbox placement is worth more than a 50% improvement in copy quality. Complete every procedure. Verify every record. Then verify again.

## Procedure 3.1: Configure DNS Records for Deliverability

For every client domain, you will add or verify four DNS record types. Open the client's DNS management panel (Cloudflare, GoDaddy, Namecheap, etc.).

**SPF Record (Sender Policy Framework):**
```
Type: TXT
Host: @
Value: v=spf1 include:klaviyo.com include:acemlna.com ~all
TTL: 3600
```

**DKIM Record (Klaviyo):**
- In Klaviyo, go to Account → Settings → Domains → Click "Get DKIM Set Up" → Copy the CNAME records provided.
- Add each CNAME to the client's DNS exactly as Klaviyo provides them.

**DKIM Record (ActiveCampaign):**
- Already configured in Procedure 2.2. Verify it is active by sending a test email from ActiveCampaign to [mail-tester.com](https://www.mail-tester.com) and checking the DKIM result.

**DMARC Record:**
```
Type: TXT
Host: _dmarc.[clientdomain].com
Value: v=DMARC1; p=none; rua=mailto:dmarc@[clientdomain].com
TTL: 3600
```
Start with `p=none` (monitoring mode). After 30 days of clean DMARC reports with no failures, change to `p=quarantine`. After 60 days with no failures, change to `p=reject`.

## Procedure 3.2: Warm Up Sending Domains

New sending domains have zero reputation. If you send 10,000 emails on day one, you will land in spam. You must warm up the domain over 14 days.

**Klaviyo Warm-Up Schedule:**
| Day | Daily Send Volume |
|-----|-------------------|
| 1–2 | 50 |
| 3–4 | 100 |
| 5–6 | 250 |
| 7–8 | 500 |
| 9–10 | 1,000 |
| 11–12 | 2,500 |
| 13–14 | 5,000 |

**ActiveCampaign Warm-Up Schedule:**
| Day | Daily Send Volume |
|-----|-------------------|
| 1–2 | 25 |
| 3–4 | 50 |
| 5–6 | 125 |
| 7–8 | 250 |
| 9–10 | 500 |
| 11–12 | 1,500 |
| 13–14 | 3,000 |

Send to the most engaged segment first (people who opened an email in the last 30 days). Do not send to cold or unengaged contacts during warm-up.

## Procedure 3.3: Set Up Deliverability Monitoring

1. Create a free account at [google.com/postmaster](https://www.google.com/postmaster). Add each client domain. This gives you Google's direct reputation score for that domain. You want to see "High" or "Medium." If you see "Low" or "Bad," you have a deliverability emergency.
2. Set up a Make.com scenario that runs daily:
   - **Trigger**: Schedule → Every day at 08:00 WAT
   - **Action 1**: HTTP Request → Call the Klaviyo API endpoint `GET /api/v1/metrics` → Filter for `email_delivery_rate`
   - **Action 2**: If `email_delivery_rate` < 95%, send a Slack alert to `#client-[brandname]` with the message: "⚠️ Deliverability drop detected for [Client]. Delivery rate: [X]%. Investigate immediately."
3. Subscribe to [monitorbacklinks.com](https://monitorbacklinks.com) free plan and add each client domain to monitor if they appear on any blacklists. Check weekly.

## Procedure 3.4: Configure List Hygiene Automation

1. In Klaviyo, go to Lists & Segments → Create Segment → Name it "Unengaged — 90 Days." Set the conditions:
   - `Received Email` at least 1 time AND
   - `Opened Email` zero times in the last 90 days AND
   - `Clicked Email` zero times in the last 90 days

2. Create a second segment named "Unengaged — 180 Days." Set the conditions:
   - `Received Email` at least 3 times AND
   - `Opened Email` zero times in the last 180 days

3. In ActiveCampaign, go to Contacts → Segments → Create Segment → Name it "Unengaged — 90 Days." Set conditions:
   - `Opens` is less than 1 in the last 90 days AND
   - `Campaign Opens` is less than 1 in the last 90 days

4. Create a "Sunset Flow" in Klaviyo (you will configure the full flow in Module 6). For now, create the segment and a placeholder email: "We noticed you haven't been opening our emails. Would you like to update your preferences or unsubscribe? We'll miss you, but we respect your inbox."

{{% accent-box %}}HACK: Never delete unengaged contacts. Suppress them instead. In Klaviyo, go to the segment → Manage Suppressions → Suppress All. Suppressed contacts don't count toward your bill but remain in your database for future re-engagement campaigns. If you delete them and they re-subscribe, you lose all their historical data. Suppress, don't delete. This saves ₦50,000–₦200,000/year per client on Klaviyo overages.{{% /accent-box %}}

## Check-In: Module 3 Complete

- [ ] SPF, DKIM (Klaviyo + ActiveCampaign), and DMARC records configured for client domain
- [ ] DMARC set to `p=none` with calendar reminder to escalate after 30 and 60 days
- [ ] Sending domain warm-up schedule created and day-1 sends executed
- [ ] Google Postmaster Tools account created with client domain added
- [ ] Make.com deliverability monitoring scenario live and tested
- [ ] "Unengaged — 90 Days" and "Unengaged — 180 Days" segments created in both Klaviyo and ActiveCampaign
- [ ] Sunset Flow placeholder email drafted

---

# MODULE 4: AUDIENCE SEGMENTATION & DATA ARCHITECTURE

## Overview

Segmentation is the difference between a 12% click rate and a 3% click rate. It is the difference between ₦2M in email-attributed revenue and ₦800K. Most email marketers segment by demographics. You will segment by behavioral signals and purchase intent — because behavior predicts revenue, demographics predict assumptions.

You will build a segmentation architecture that automatically categorizes every contact into one of five engagement tiers. This architecture runs on autopilot. Every new subscriber is tagged within 60 seconds of their first action. Every existing contact is re-evaluated daily.

## Procedure 4.1: Define the Five-Tier Engagement Model

Create the following engagement tiers in your Google Sheet under a new tab called "Segmentation Architecture":

| Tier | Name | Definition | Email Frequency | Content Type |
|------|------|------------|-----------------|--------------|
| 1 | VIP | Purchased 3+ times in last 90 days OR lifetime value > ₦100K | 3–4/week | Exclusive drops, early access, loyalty rewards |
| 2 | Active | Opened or clicked in last 30 days, purchased 1–2 times in last 90 days | 2–3/week | Product recommendations, educational content, offers |
| 3 | Warm | Opened in last 60 days but not last 30, zero purchases in last 90 days | 1/week | Re-engagement content, bestseller roundups, social proof |
| 4 | Cold | No open or click in last 60–90 days | 1/2 weeks | Win-back campaigns, survey emails, sunset warning |
| 5 | Dormant | No activity in 90+ days | 0 (suppressed) | Sunset flow only |

## Procedure 4.2: Build Klaviyo Segments

1. In Klaviyo, go to Lists & Segments → Create Segment. Build each tier as a separate segment.

**Tier 1 — VIP:**
- Condition: `Placed Order` at least 3 times in the last 90 days
- OR Condition: `Placed Order` → `Total Value` is greater than ₦100,000 (lifetime)
- Click "Create Segment"

**Tier 2 — Active:**
- Condition: `Opened Email` at least 1 time in the last 30 days
- AND Condition: `Placed Order` between 1 and 2 times in the last 90 days
- AND Condition: `Not in Segment` → "Tier 1 — VIP"

**Tier 3 — Warm:**
- Condition: `Opened Email` at least 1 time between 31 and 60 days ago
- AND Condition: `Placed Order` zero times in the last 90 days
- AND Condition: `Not in Segment` → "Tier 1 — VIP" AND `Not in Segment` → "Tier 2 — Active"

**Tier 4 — Cold:**
- Condition: `Opened Email` zero times in the last 60 days
- AND Condition: `Received Email` at least 1 time in the last 60 days
- AND Condition: `Not in Segment` → "Tier 1", "Tier 2", "Tier 3"

**Tier 5 — Dormant:**
- Condition: `Opened Email` zero times in the last 90 days
- AND Condition: `Received Email` at least 1 time in the last 90 days
- AND Condition: `Not in Segment` → "Tier 1", "Tier 2", "Tier 3", "Tier 4"

2. Verify: Klaviyo will show you the count of contacts in each segment. These should total approximately 100% of your emailable list (minus suppressed contacts). If they do not, your conditions have overlap or gaps. Fix them before proceeding.

## Procedure 4.3: Build ActiveCampaign Segments

1. In ActiveCampaign, go to Contacts → Segments → Create Segment.

**Tier 1 — VIP:**
- Condition: `Tags` contains `vip-customer`
- AND Condition: `Purchase Count` is greater than 2 in the last 90 days

**Tier 2 — Active:**
- Condition: `Opens` is greater than 0 in the last 30 days
- AND Condition: `Purchase Count` is between 1 and 2 in the last 90 days
- AND Condition: `Tags` does not contain `vip-customer`

**Tier 3 — Warm:**
- Condition: `Opens` is greater than 0 between 31 and 60 days ago
- AND Condition: `Purchase Count` is 0 in the last 90 days

**Tier 4 — Cold:**
- Condition: `Opens` is 0 in the last 60 days
- AND Condition: `Campaign Sends` is greater than 0 in the last 60 days

**Tier 5 — Dormant:**
- Condition: `Opens` is 0 in the last 90 days
- AND Condition: `Campaign Sends` is greater than 0 in the last 90 days

2. ActiveCampaign segments update in real time. Verify by checking the contact count matches your Klaviyo segment counts within a 5% margin (slight differences are normal due to timing).

## Procedure 4.4: Set Up Automated Tagging via Make.com

1. Create a Make.com scenario named "Engagement Tier Tagger":
   - **Trigger**: Klaviyo → Watch Events → Select "Placed Order" event
   - **Router**: Route based on conditions:
     - Path A: If `Total Order Value (Lifetime)` > ₦100,000 → Klaviyo → Add Tag → `tier-1-vip`
     - Path B: If `Order Count (90 days)` between 1 and 2 → Klaviyo → Add Tag → `tier-2-active`
     - Path C: Default → Klaviyo → Add Tag → `tier-3-warm`
   - **Schedule**: Run every 15 minutes

2. Create a second scenario named "Tier Demotion Engine":
   - **Trigger**: Schedule → Run daily at 02:00 WAT
   - **Action 1**: Klaviyo → Get all contacts in "Tier 2 — Active" segment
   - **Action 2**: Filter → If last open date > 30 days ago, remove tag `tier-2-active`, add tag `tier-3-warm`
   - **Action 3**: Klaviyo → Get all contacts in "Tier 3 — Warm" segment
   - **Action 4**: Filter → If last open date > 60 days ago, remove tag `tier-3-warm`, add tag `tier-4-cold`

This automation ensures contacts are always in the correct tier without manual intervention.

## Procedure 4.5: Build Custom Properties for AI Personalization

In Klaviyo, go to Account → Settings → Custom Properties. Create the following:

| Property Name | Data Type | Source |
|---------------|-----------|--------|
| `predicted_gender` | Text | Klaviyo AI (enabled by default on Plus plans) |
| `average_order_value` | Number | Calculated from order data |
| `favorite_category` | Text | Most-purchased product category |
| `discount_sensitivity` | Text | Values: `high`, `medium`, `low` — calculated from % of orders placed during sales |
| `preferred_send_time` | Text | Values: `morning`, `afternoon`, `evening` — calculated from most frequent open time |
| `churn_risk` | Text | Values: `low`, `medium`, `high` — based on days since last purchase vs. average purchase frequency |

In ActiveCampaign, create equivalent custom fields under Contacts → Settings → Custom Fields.

{{% accent-box %}}HACK: The `discount_sensitivity` custom property is worth ₦500K–₦2M per client per year. When you know who buys at full price and who only buys on sale, you stop sending 20% off codes to people who would have paid full price anyway. Send full-price new arrivals to "low" sensitivity contacts. Send 15% off clearance to "high" sensitivity contacts. One e-commerce client recovered ₦1.8M in margin in a single quarter by not over-discounting. This property alone justifies your Growth-tier fee.{{% /accent-box %}}

## Check-In: Module 4 Complete

- [ ] Five-tier engagement model documented in Google Sheet
- [ ] All five segments created and verified in Klaviyo
- [ ] All five segments created and verified in ActiveCampaign
- [ ] Make.com "Engagement Tier Tagger" scenario live and tested
- [ ] Make.com "Tier Demotion Engine" scenario live and tested
- [ ] Six custom properties created in Klaviyo
- [ ] Equivalent custom fields created in ActiveCampaign

---

# MODULE 5: AI CONTENT GENERATION ENGINE

## Overview

Content is where most email agencies spend 70% of their time and deliver 30% of their value. You will invert this ratio. AI generates 80% of your first-draft content. You spend 20% of your time on human editing and strategic oversight. This is not lazy — this is leverage. The AI produces competent copy in 90 seconds. You make it excellent in 10 minutes. The alternative is a human writing for 45 minutes and producing something equally competent. Excellence comes from editing, not from typing.

## Procedure 5.1: Build the Email Prompt Library

Create a Google Doc named `[Your Brand] — Email Prompt Library`. Organize prompts into five categories. Each prompt follows the same structure: Context → Task → Constraints → Output Format.

**Category 1: Promotional Emails**
```
CONTEXT: You are writing a promotional email for [BRAND NAME], a [BUSINESS TYPE] that sells [PRODUCT/SERVICE]. The target audience is [SEGMENT DESCRIPTION]. The offer is [OFFER DETAILS].

TASK: Write a promotional email that drives urgency and click-through to the product page.

CONSTRAINTS:
- Subject line: 45 characters maximum
- Preview text: 90 characters maximum
- Body: 150 words maximum
- One CTA only: "[CTA TEXT]"
- No generic phrases ("I hope this finds you well", "We're excited to announce")
- Include one specific product detail (price, feature, benefit)
- Create urgency without deception

OUTPUT FORMAT:
Subject: [subject line]
Preview: [preview text]
Body: [HTML body]
CTA: [button text]
```

**Category 2: Welcome Series**
```
CONTEXT: You are writing email #[NUMBER] of a 4-email welcome series for [BRAND NAME]. The subscriber just [HOW THEY JOINED — e.g., "signed up for a 10% discount"]. Their first purchase has [NOT BEEN MADE / BEEN MADE].

TASK: Write a welcome email that builds brand affinity and drives [FIRST PURCHASE / SECOND PURCHASE].

CONSTRAINTS:
- Subject line: 40 characters maximum
- Body: 120 words maximum
- Tone: Warm, direct, slightly personal
- Include one brand story element (origin, values, or customer transformation)
- One CTA only

OUTPUT FORMAT:
Subject: [subject line]
Preview: [preview text]
Body: [HTML body]
CTA: [button text]
```

**Category 3: Abandoned Cart**
```
CONTEXT: A customer added [PRODUCT NAMES] to their cart [HOURS AGO] but did not complete checkout. Cart value: [₦AMOUNT]. Their name is [FIRST NAME].

TASK: Write a cart abandonment email that recovers the purchase.

CONSTRAINTS:
- Subject line: 35 characters maximum
- Body: 80 words maximum
- Mention the specific products by name
- Include the cart total in Naira
- One CTA: "Complete Your Order"
- Do NOT offer a discount in this email (first touch)
- Create gentle urgency: "Your cart expires in 24 hours"

OUTPUT FORMAT:
Subject: [subject line]
Preview: [preview text]
Body: [HTML body]
CTA: [button text]
```

**Category 4: Win-Back**
```
CONTEXT: [FIRST NAME] has not purchased from [BRAND NAME] in [DAYS] days. Their last purchase was [PRODUCT NAME]. They are in the [TIER] engagement segment.

TASK: Write a win-back email that reactivates this customer.

CONSTRAINTS:
- Subject line: 40 characters maximum
- Body: 100 words maximum
- Acknowledge their absence without guilt-tripping
- Reference their last purchase category
- Include a [DISCOUNT]% offer if tier is Cold; no discount if tier is Warm
- One CTA only

OUTPUT FORMAT:
Subject: [subject line]
Preview: [preview text]
Body: [HTML body]
CTA: [button text]
```

**Category 5: Post-Purchase**
```
CONTEXT: [FIRST NAME] just purchased [PRODUCT NAME] for ₦[AMOUNT]. This is their [ORDINAL] order with [BRAND NAME].

TASK: Write a post-purchase email that drives the next action: [CROSS-SELL / REVIEW / REFERRAL / LOYALTY SIGN-UP].

CONSTRAINTS:
- Subject line: 40 characters maximum
- Body: 80 words maximum
- Thank them for the specific purchase
- Suggest one complementary product (cross-sell) OR request a review (if 7+ days post-delivery)
- One CTA only

OUTPUT FORMAT:
Subject: [subject line]
Preview: [preview text]
Body: [HTML body]
CTA: [button text]
```

## Procedure 5.2: Create the AI Content Production Workflow

1. Open your "Email Copy Engine" Custom GPT in ChatGPT.
2. For each email needed, paste the appropriate prompt from your library. Fill in ALL bracketed variables with real data from the client's Klaviyo/ActiveCampaign account.
3. Copy the AI output into a Google Doc named `[Client] — [Month] Email Drafts`.
4. Edit the draft using this checklist:
   - [ ] Subject line is under the character limit
   - [ ] Preview text complements (not repeats) the subject line
   - [ ] Opening sentence creates curiosity or relevance — not a greeting
   - [ ] Every paragraph is 1–2 sentences maximum
   - [ ] One CTA, clearly visible, above the fold
   - [ ] No filler phrases removed ("In today's email...", "We wanted to let you know...")
   - [ ] Product claims are specific (prices, quantities, dates)
   - [ ] Tone matches brand voice guidelines
   - [ ] No AI artifacts ("delve into", "it's worth noting", "in conclusion")
5. Paste the final copy into Klaviyo or ActiveCampaign's email builder.
6. Add the Canva-designed header image.
7. Send a test email to yourself and the client. Verify rendering on desktop and mobile.

## Procedure 5.3: Build the Subject Line Generator

1. In ChatGPT, save this prompt as "Subject Line Generator":
```
Generate 10 subject lines for a [EMAIL TYPE] email targeting [SEGMENT] for [BRAND NAME].

Rules:
- Maximum 45 characters each
- No punctuation at the end
- No ALL CAPS (maximum 2 words in caps for emphasis)
- Include 3 curiosity-driven, 3 urgency-driven, 2 benefit-driven, 2 social-proof-driven
- Rank by predicted open rate (highest first)
```

2. For every campaign, generate 10 subject lines. Select the top 3. Use the #1 pick for the send. Save the other two for A/B testing (Module 7).

## Procedure 5.4: Set Up the AI Batch Production System

You will not write emails one at a time. You will batch-produce an entire month's content in a single 3-hour session.

1. Open a fresh ChatGPT conversation.
2. Paste this master prompt:
```
I need you to write [NUMBER] emails for [BRAND NAME] for the month of [MONTH]. Here is the campaign calendar:

[COPY THE FULL CAMPAIGN CALENDAR FROM YOUR GOOGLE SHEET — INCLUDE: DATE, CAMPAIGN NAME, SEGMENT, OBJECTIVE]

For each email, use the appropriate prompt template from the Email Prompt Library. Output all emails in sequence, separated by "---" dividers. Include subject lines and preview text for each.
```

3. Review and edit all emails in the Google Doc during the same session.
4. Schedule all emails in Klaviyo/ActiveCampaign according to the campaign calendar.
5. This 3-hour session replaces what would otherwise be 15–20 hours of individual email writing across the month.

{{% accent-box %}}HACK: Save every AI-generated email that performs well (open rate > 35% OR click rate > 5%) into a "Winning Swipe File" folder in your Google Drive. After 3 months, you will have 30–50 proven email templates. When you onboard a new client, you don't start from zero — you adapt from a library of winners. This swipe file becomes your most valuable asset. It is the difference between "I'll write some emails" and "I have a tested library of high-performing email frameworks adapted to your brand."{{% /accent-box %}}

## Check-In: Module 5 Complete

- [ ] Email Prompt Library Google Doc created with all five categories
- [ ] "Email Copy Engine" Custom GPT configured with system prompt
- [ ] Content Production Workflow checklist created and used for at least one email
- [ ] "Subject Line Generator" prompt saved in ChatGPT
- [ ] AI Batch Production System used to produce one full month of content
- [ ] "Winning Swipe File" folder created in Google Drive
- [ ] At least 5 high-performing emails saved to the swipe file

---

# MODULE 6: AUTOMATION FLOW DESIGN

## Overview

Flows are where the money lives. Campaigns are one-time sends. Flows run forever. A single well-configured abandoned cart flow can generate ₦500K–₦3M per month in attributed revenue for a mid-size e-commerce client. A welcome series can convert 15–25% of new subscribers into first-time buyers within 14 days. Flows are the asset that compounds. Every flow you build today generates revenue tomorrow, next week, next month, and next year — without additional effort.

You will build eight core flows. Each flow has a trigger, a series of timed emails, conditional logic, and a revenue attribution tag. Build them in this order. The first four are non-negotiable. The last four differentiate you from every "email marketer" the client has hired before.

## Procedure 6.1: Build the Welcome Series (4 Emails)

**In Klaviyo:**
1. Go to Flows → Create Flow → Create From Scratch → Name: "Welcome Series"
2. Trigger: "List" → "Added to List" → Select the client's newsletter signup list
3. Configure the flow:

| Email | Delay | Subject Line Template | Objective |
|-------|-------|-----------------------|-----------|
| Welcome 1 | Immediately | "You're in. Here's your [X]% off" | Deliver sign-up incentive, set expectations |
| Welcome 2 | 24 hours | "3 things [Brand] insiders know" | Brand story, bestsellers, social proof |
| Welcome 3 | 72 hours | "Still thinking it over?" | Address hesitation, feature reviews/testimonials |
| Welcome 4 | 168 hours (7 days) | "Last chance: Your [X]% expires in 24hrs" | Urgency, final discount push |

4. For each email, configure:
   - **Smart Sending**: ON (prevents someone from receiving multiple flow emails on the same day)
   - **Urgent**: OFF
   - **Filter**: `Not in Segment` → "Tier 5 — Dormant" (don't send to dormant contacts)
5. Add a conditional split after Welcome 3: `Placed Order` = Yes in the last 7 days → Route to a "Thank You + Cross-Sell" email instead of Welcome 4.
6. Set revenue attribution: Go to Flow Settings → Attribution Window → Set to "5 days" (this means any purchase within 5 days of a flow email is attributed to that flow).

**In ActiveCampaign:**
1. Go to Automations → New Automation → Start from Scratch → Name: "Welcome Series"
2. Trigger: "Subscribes to List" → Select the client's signup list
3. Add the following actions in sequence:
   - **Wait**: 0 minutes → Send Email: Welcome 1
   - **Wait**: 24 hours → Send Email: Welcome 2
   - **Wait**: 72 hours → Send Email: Welcome 3
   - **If/Else**: Condition → "Has purchased" → "Yes" → Send "Thank You + Cross-Sell" email / "No" → Continue
   - **Wait**: 168 hours → Send Email: Welcome 4
4. Enable "Goal" action: Place Order. If the contact makes a purchase at any point, they exit the Welcome Series and enter the Post-Purchase Flow.

## Procedure 6.2: Build the Abandoned Cart Flow (3 Emails)

**In Klaviyo:**
1. Go to Flows → Create Flow → Abandoned Cart (pre-built template) → Customize
2. Trigger: "Checkout Started" (default) — this fires when someone enters checkout but doesn't complete
3. Configure the flow:

| Email | Delay | Subject Line Template | Strategy |
|-------|-------|-----------------------|----------|
| Cart 1 | 2 hours | "[First Name], you left something behind" | Gentle reminder, no discount |
| Cart 2 | 24 hours | "Your cart is waiting — see what's inside" | Product images, social proof |
| Cart 3 | 48 hours | "Here's [X]% off if you complete your order" | Discount offer, final push |

4. Critical settings:
   - **Filter on the trigger**: `Placed Order` = Zero times since starting checkout (this prevents sending to people who already completed the purchase)
   - **Smart Sending**: ON
   - **Use dynamic product blocks**: In the email body, insert a "Product Block" that automatically pulls the exact items left in the cart with images, names, and prices.
5. Conditional split after Cart 2: If `discount_sensitivity` = "high" → send Cart 3 with 15% off. If `discount_sensitivity` = "low" or "medium" → send Cart 3 with free shipping instead of a percentage discount.

**In ActiveCampaign:**
1. Go to Automations → New Automation → Name: "Abandoned Cart"
2. Trigger: "Site Event" → `checkout_started`
3. Configure the same three-email sequence with equivalent delays.
4. Add a Goal action: "Purchases" → If the contact purchases at any point, they exit the flow.
5. Use ActiveCampaign's dynamic content blocks: Insert `{{contact.fieldValues.product_name}}` and `{{contact.fieldValues.cart_total}}` to personalize the cart contents.

## Procedure 6.3: Build the Browse Abandonment Flow (2 Emails)

**In Klaviyo:**
1. Trigger: "Viewed Product" → Add condition: `Placed Order` = Zero times in the last 24 hours (exclude recent buyers)
2. Add filter: `Viewed Product` at least 2 times in the last 7 days (only trigger for people browsing repeatedly, not casual visitors)
3. Email 1 (delay: 4 hours): "Still thinking about [Product Name]?" — Feature the viewed product, related items, and one customer review.
4. Email 2 (delay: 24 hours after Email 1): "Customers also loved these" — Show top 3 related products. No discount.
5. Smart Sending: ON. Max sends per person: 1 per 7 days (prevent over-sending to heavy browsers).

## Procedure 6.4: Build the Post-Purchase Flow (3 Emails)

**In Klaviyo:**
1. Trigger: "Placed Order"
2. Filter: `Placed Order` = 1 time (first-time buyers) OR remove this filter to include repeat buyers with different content branches.
3. Configure:

| Email | Delay | Subject | Objective |
|-------|-------|---------|-----------|
| Post-Purchase 1 | 1 hour | "Thank you, [First Name]! Your order is confirmed" | Order confirmation, delivery expectations, support info |
| Post-Purchase 2 | 7 days | "How's your [Product Category]?" | Review request, tips for product use, community invite |
| Post-Purchase 3 | 14 days | "Since you loved [Product], you might like..." | Cross-sell complementary products based on purchase category |

4. Add conditional logic: After Email 2, split by `Number of Orders`:
   - If 1 order → send loyalty program invite email
   - If 2+ orders → send referral program email with unique referral link
5. Revenue attribution window: 10 days.

## Procedure 6.5: Build the Win-Back Flow (3 Emails)

**In Klaviyo:**
1. Trigger: "Date-Based" → `Last Purchase Date` is more than 60 days ago
2. Configure:

| Email | Delay | Subject | Strategy |
|-------|-------|---------|----------|
| Win-Back 1 | Immediately | "We miss you, [First Name]" | Nostalgia, new arrivals since last visit |
| Win-Back 2 | 5 days | "Here's [X]% just for you" | Personalized discount (15% for "high" discount sensitivity, 10% for "medium") |
| Win-Back 3 | 10 days | "This is your last email from us" | Sunset warning, final offer, unsubscribe option |

3. After Win-Back 3: If no purchase → Add to "Tier 5 — Dormant" segment → Suppress from all future campaigns (not flows — they still get transactional emails).

## Procedure 6.6: Build the VIP Loyalty Flow (2 Emails)

**In Klaviyo:**
1. Trigger: "Entered Segment" → "Tier 1 — VIP"
2. Email 1 (immediately): "Welcome to the inner circle" — Exclusive access announcement, early product drops, loyalty points balance.
3. Email 2 (30 days after entering segment): "Your VIP [MONTH] perks" — Monthly exclusive offer, birthday reward if applicable, referral bonus.
4. This flow runs in a loop. Email 2 repeats every 30 days with updated content via a "Time Delay" + "Update Flow" action.

## Procedure 6.7: Build the Customer Re-Engagement Flow (3 Emails)

**In ActiveCampaign:**
1. Trigger: "Tag Added" → `tier-3-warm`
2. Email 1 (immediately): "We've got something you'll love" — Bestsellers, new arrivals, no discount.
3. Email 2 (7 days): "Your favorites are back in stock" — Use `favorite_category` custom field to show relevant restocks.
4. Email 3 (14 days): "Take [X]% off before these are gone" — Discount offer, urgency.
5. Goal action: "Clicks Link" in any email → Remove `tier-3-warm` tag, add `tier-2-active` tag → Contact exits flow.

## Procedure 6.8: Build the Sunset Flow (2 Emails)

**In Klaviyo:**
1. Trigger: "Entered Segment" → "Tier 5 — Dormant"
2. Email 1 (immediately): "Before you go..." — Preference center link, option to update email frequency instead of unsubscribing.
3. Email 2 (14 days): "This is your last email from [Brand]" — Final farewell, unsubscribe link, option to stay with reduced frequency.
4. After Email 2: If no action → Suppress contact from all lists and segments.

{{% accent-box %}}HACK: Add a "dead man's switch" to your Sunset Flow. After the second email, if the contact takes no action within 14 days, run a Make.com scenario that suppresses them in Klaviyo, removes them from all ActiveCampaign lists, and logs the suppression date in your Google Sheet. Unengaged contacts destroy your sender reputation and inflate your Klaviyo bill. A 50,000-contact list with 30% dormant contacts costs ₦75,000/month more than it should and drags your deliverability score down by 10-15 points. Aggressive list hygiene is not optional — it is a profit center.{{% /accent-box %}}

## Check-In: Module 6 Complete

- [ ] Welcome Series (4 emails) built and live in Klaviyo AND ActiveCampaign
- [ ] Abandoned Cart Flow (3 emails) built with dynamic product blocks and discount-sensitivity branching
- [ ] Browse Abandonment Flow (2 emails) built with repeat-browser trigger filter
- [ ] Post-Purchase Flow (3 emails) built with conditional splits for loyalty/referral
- [ ] Win-Back Flow (3 emails) built with sunset action
- [ ] VIP Loyalty Flow (2 emails) built with 30-day loop
- [ ] Customer Re-Engagement Flow (3 emails) built in ActiveCampaign
- [ ] Sunset Flow (2 emails) built with dead man's switch automation
- [ ] Revenue attribution windows set on all flows
- [ ] Smart Sending enabled on all flows

---

# MODULE 7: A/B TESTING & OPTIMIZATION

## Overview

You will not guess. You will test. Every assumption you hold about subject lines, send times, CTA placement, and offer structure is wrong until proven right by data. A/B testing is not a nice-to-have — it is the mechanism by which you turn a ₦150,000/month Starter client into a ₦350,000/month Growth client by proving that your optimizations generate measurable revenue lift.

## Procedure 7.1: Set Up Your Testing Framework

Create a new tab in your Google Sheet named "A/B Test Log." Columns:
| Column | Description |
|--------|-------------|
| Test ID | Auto-incrementing number |
| Test Date | When the test was launched |
| Flow/Campaign | Which flow or campaign is being tested |
| Element Tested | Subject line / Preview text / CTA / Send time / Offer / Design |
| Variant A | Control (current version) |
| Variant B | Challenger (new version) |
| Sample Size | Number of contacts per variant |
| Metric | Primary metric being measured (open rate / click rate / conversion rate / revenue per recipient) |
| Minimum Detectable Effect | Smallest lift you consider meaningful (default: 15%) |
| Confidence Threshold | 95% (industry standard) |
| Winner | A / B / Inconclusive |
| Lift % | Percentage improvement of winner over loser |
| Revenue Impact | ₦ amount attributed to the lift |

## Procedure 7.2: Calculate Required Sample Sizes

Before running any test, calculate whether you have enough contacts for statistical significance.

1. Go to [evanmiller.org/ab-testing/sample-size.html](https://www.evanmiller.org/ab-testing/sample-size.html)
2. Enter:
   - Baseline conversion rate: Use the current rate for the metric you're testing (e.g., if your current open rate is 25%, enter 25%)
   - Minimum detectable effect: 15% (this means you're looking for at least a 15% improvement)
   - Statistical significance: 95%
   - Statistical power: 80%
3. The calculator will give you the sample size per variant. If a client's segment doesn't have at least 2× that number of contacts, the test is underpowered. Either combine segments or test on a higher-volume flow.

Example: Baseline open rate = 25%, MDE = 15%, significance = 95%, power = 80% → Required sample per variant = ~5,100 contacts. You need at least 10,200 contacts total to run this test.

## Procedure 7.3: Configure A/B Tests in Klaviyo

**For Campaigns:**
1. Create a new campaign → Design your email → At the "Send" step, click "A/B Test"
2. Select the element to test:
   - **Subject Line**: Enter Variant A and Variant B subject lines
   - **From Name**: Enter two different from names (e.g., "Brand Name" vs. "Founder's Name")
   - **Send Time**: Select two different send times
3. Set the split: 50/50 (equal split for cleanest data)
4. Set the winning metric: "Opens" for subject line tests, "Clicks" for CTA/content tests, "Revenue" for offer tests
5. Set the test duration: 24 hours for open-rate tests, 72 hours for click/revenue tests
6. After the test period, Klaviyo automatically sends the winning variant to the remaining audience

**For Flows:**
1. Klaviyo does not have native flow A/B testing. Use this workaround:
2. Duplicate the flow email you want to test → Create Variant A and Variant B as separate emails in the flow
3. Add a "Conditional Split" before the test point: Random Sample = 50% → Route to Variant A / Route to Variant B
4. Monitor results in the Flow Analytics tab
5. After reaching statistical significance, remove the losing variant and keep the winner as the sole email

## Procedure 7.4: Configure A/B Tests in ActiveCampaign

1. Create a new campaign → Design your email → At the "Send" step, select "A/B Test"
2. Choose your test variable: Subject, From Name, or Full Email
3. Set the distribution: 50/50
4. Select the winning condition: Open rate or click rate
5. Set the test window: 24 hours
6. ActiveCampaign will automatically send the winner to the remainder of the list after the test window

## Procedure 7.5: Run the First 30-Day Optimization Sprint

Week 1: **Subject Line Tests** — Test curiosity-driven vs. urgency-driven subject lines on your Welcome Series Email 1. Run 3 tests, one per campaign send.

Week 2: **Send Time Tests** — Test morning (08:00 WAT) vs. evening (18:00 WAT) sends on your highest-volume campaign. Test Monday vs. Thursday vs. Saturday.

Week 3: **CTA Tests** — Test button text ("Shop Now" vs. "See the Collection" vs. "Claim Your [X]%"). Test button placement (in-text link vs. standalone button vs. both).

Week 4: **Offer Tests** — Test 10% off vs. ₦5,000 off vs. free shipping on your Win-Back Flow Email 2. Calculate which offer generates the highest revenue per recipient, not the highest conversion rate.

{{% accent-box %}}HACK: Always test offer structure before offer amount. A "₦5,000 off your next order" consistently outperforms "10% off" even when the monetary value is identical, because flat amounts feel more tangible than percentages. Test flat-amount vs. percentage vs. free shipping vs. free gift before you ever test "10% vs. 15%." The structure of the offer matters more than the size of the discount. This insight alone can increase Win-Back flow revenue by 25–40%.{{% /accent-box %}}

## Procedure 7.6: Build the Optimization Feedback Loop

1. After every test, record results in the A/B Test Log Google Sheet.
2. Implement the winning variant immediately. Do not wait for a "perfect" dataset.
3. After implementing a win, schedule a follow-up test in 30 days to see if a new challenger can beat the current champion.
4. Monthly, calculate the cumulative revenue impact of all optimizations. This number goes into your client report and justifies your monthly retainer.

## Check-In: Module 7 Complete

- [ ] A/B Test Log created in Google Sheet with all columns configured
- [ ] Sample size calculator bookmarked and used for at least one test
- [ ] First campaign A/B test launched in Klaviyo or ActiveCampaign
- [ ] Flow A/B test workaround implemented for at least one flow email
- [ ] 30-day optimization sprint planned with one test per week
- [ ] Optimization feedback loop documented and first results recorded
- [ ] At least 3 completed tests logged with winners and revenue impact

---

# MODULE 8: ANALYTICS & REPORTING

## Overview

Your client does not care about open rates. They care about revenue. You will report on revenue first, attribution second, and engagement metrics third. Every report you deliver must answer one question: "What did my email program generate in revenue this month, and what will it generate next month?"

## Procedure 8.1: Configure Klaviyo Analytics

1. Go to Klaviyo → Analytics → Configure → Enable the following metrics:
   - Placed Order
   - Ordered Product
   - Refunded Order
   - Started Checkout
   - Viewed Product
   - Added to Cart
   - Subscribed to List
   - Unsubscribed
2. Set attribution model: Go to Analytics → Attribution → Select "Last Touch" attribution with a 5-day window for flows and a 1-day window for campaigns.
3. Create a custom dashboard named "Client [X] — Monthly Performance":
   - **Widget 1**: Total Revenue (attributed) — Last 30 days — Bar chart by week
   - **Widget 2**: Revenue by Flow — Last 30 days — Table with flow name, revenue, orders, AOV
   - **Widget 3**: Revenue by Campaign — Last 30 days — Table with campaign name, revenue, open rate, click rate
   - **Widget 4**: List Growth — Last 30 days — Line chart with new subscribers vs. unsubscribes
   - **Widget 5**: Engagement Trend — Last 90 days — Line chart with open rate and click rate
   - **Widget 6**: Top Performing Emails — Last 30 days — Table ranked by revenue per recipient

## Procedure 8.2: Configure ActiveCampaign Analytics

1. Go to Reports → Campaign Reports → Enable tracking for all campaigns
2. Go to Reports → Automation Reports → Enable revenue tracking by connecting ActiveCampaign to the client's e-commerce platform via the integration settings
3. Create a custom report:
   - **Section 1**: Automation Performance — Revenue attributed, entries, exits, completion rate
   - **Section 2**: Campaign Performance — Opens, clicks, revenue, unsubscribes
   - **Section 3**: Contact Growth — Net new contacts, churn rate, segment distribution
4. Schedule this report to auto-generate on the 1st of every month and email it to your client's address.

## Procedure 8.3: Build the Monthly Client Report Template

Create a Google Slides or Canva presentation template with the following slides:

**Slide 1: Executive Summary**
- Total email-attributed revenue: ₦[X]
- Month-over-month change: [+/-X%]
- Net new subscribers: [X]
- Total active subscribers: [X]

**Slide 2: Revenue Breakdown**
- Flow revenue: ₦[X] ([%] of total)
- Campaign revenue: ₦[X] ([%] of total)
- Top 3 revenue-generating flows with their individual ₦ amounts

**Slide 3: Flow Performance**
- Table: Flow Name | Entries | Revenue | Conversion Rate | MoM Change
- Highlight: Best-performing flow and why
- Highlight: Worst-performing flow and action plan

**Slide 4: Campaign Performance**
- Table: Campaign Name | Sent | Open Rate | Click Rate | Revenue | Revenue per Recipient
- Highlight: Best-performing campaign and why

**Slide 5: A/B Test Results**
- Table: Test | Winner | Lift % | Revenue Impact
- Cumulative optimization revenue: ₦[X]

**Slide 6: Next Month's Plan**
- Upcoming campaigns and flow updates
- Planned A/B tests
- Revenue forecast: ₦[X] (based on current trends × planned optimizations)

## Procedure 8.4: Automate Report Generation via Make.com

1. Create a Make.com scenario named "Monthly Report Generator":
   - **Trigger**: Schedule → Run on the 1st of every month at 06:00 WAT
   - **Action 1**: Klaviyo → Get Campaign Metrics (last 30 days) → Store in Google Sheet "Revenue Attribution" tab
   - **Action 2**: Klaviyo → Get Flow Metrics (last 30 days) → Store in Google Sheet "Flow Performance" tab
   - **Action 3**: Google Sheets → Calculate totals and MoM changes
   - **Action 4**: Slack → Post summary to `#client-[brandname]`: "📊 [Month] Report: ₦[X] attributed revenue. [X]% MoM growth. Full report: [link]"
2. The detailed slide deck is still built manually — the automation handles data extraction and the Slack notification. Building a fully automated slide deck is possible but error-prone; the 30 minutes of manual deck assembly is time well spent.

## Procedure 8.5: Set Up Real-Time Revenue Alerts

1. Create a Make.com scenario named "Revenue Milestone Alerts":
   - **Trigger**: Klaviyo → Watch for "Placed Order" events
   - **Filter**: `Attributed to Email` = Yes
   - **Accumulator**: Running total of email-attributed revenue for the current month
   - **Action**: When the running total crosses a milestone (₦500K, ₦1M, ₦2.5M, ₦5M), send a Slack message to `#client-[brandname]`: "🎉 [Brand] just crossed ₦[X] in email-attributed revenue this month!"

2. Create a second scenario named "Deliverability Alert":
   - **Trigger**: Klaviyo → Watch for bounce events
   - **Filter**: If bounce count > 2% of total sends in the last 24 hours
   - **Action**: Send Slack alert to your internal channel `#ops-alerts`: "⚠️ High bounce rate for [Client]. [X]% bounce rate in last 24h. Investigate immediately."

## Check-In: Module 8 Complete

- [ ] Klaviyo analytics configured with all 8 metrics enabled
- [ ] Klaviyo custom dashboard created with 6 widgets
- [ ] ActiveCampaign analytics configured with revenue tracking
- [ ] Monthly report template created (Google Slides or Canva)
- [ ] Make.com "Monthly Report Generator" scenario live
- [ ] Make.com "Revenue Milestone Alerts" scenario live
- [ ] Make.com "Deliverability Alert" scenario live
- [ ] First monthly report delivered to client

---

# MODULE 9: CLIENT ACQUISITION

## Overview

You have the skills. You have the stack. You have the playbooks. Now you need paying clients. Client acquisition is not a creative exercise — it is a numbers game with a conversion rate. You will run three acquisition channels simultaneously. Each channel has a specific cost-per-acquisition target and a specific conversion rate expectation. You will track both.

## Procedure 9.1: Build Your Case Study Portfolio

Before you pitch anyone, you need proof. Complete Modules 2–8 for one business — your own, a friend's, or a free-trial client — and document every result.

1. Write three case studies using this template:

```
CASE STUDY: [Brand Name]

Challenge: [Brand] had [X] subscribers and ₦[X] in monthly email revenue with no automation flows and basic batch-and-blast campaigns.

Solution: Implemented [X] automated flows, AI-powered segmentation into 5 engagement tiers, and a monthly A/B testing program.

Results:
- Email-attributed revenue: ₦[X]/month (up from ₦[X])
- Open rate: [X]% (up from [X]%)
- Click rate: [X]% (up from [X]%)
- Abandoned cart recovery rate: [X]%
- ROI: For every ₦1 spent on our service, [Brand] generated ₦[X] in email revenue.
```

2. Design each case study as a one-page PDF in Canva using the client's brand colors. Export at high resolution.
3. Post the case studies on your website (even a Notion page published to the web counts).

## Procedure 9.2: Set Up the Cold Outreach Engine

**Channel 1: Cold Email via ActiveCampaign**

1. Build a prospect list using [apollo.io](https://apollo.io) (free tier gives you 60 email credits/month):
   - Search: "E-commerce" + "Lagos" OR "Nigeria" + Revenue: ₦5M–₦100M/month
   - Export: Founder name, email, company name, website URL
2. In ActiveCampaign, create a new list named "Prospects — Cold."
3. Build a 5-email cold outreach sequence:

| Email | Delay After Previous | Subject | Body Summary |
|-------|---------------------|---------|--------------|
| 1 | 0 | "Your email program is leaving money on the table" | Specific observation about their current email program (check their site for a popup or signup form — if they don't have one, that's your hook) |
| 2 | 3 days | "₦[X] in recovered revenue — case study" | Share a relevant case study with specific numbers |
| 3 | 7 days | "Quick question about [Brand]'s abandoned carts" | Ask if they know their cart abandonment rate — most don't, and this creates curiosity |
| 4 | 14 days | "Free audit: your email program" | Offer a free mini-audit of their current setup |
| 5 | 21 days | "Closing the loop" | Final touch, no pressure, leave the door open |

4. Each email must be under 100 words. No attachments. One CTA per email. The CTA is always "Reply to this email" or "Book a 15-minute call" (with Calendly link).

**Channel 2: LinkedIn Outreach via PhantomBuster**

1. Go to [phantombuster.com](https://phantombuster.com) and subscribe to the Starter plan at $69/month (approximately ₦110,000/month).
2. Create a LinkedIn search for: "Founder" OR "CEO" + "E-commerce" + Location: "Nigeria" or "Lagos"
3. Set up an auto-connect campaign with this connection note:
   ```
   Hi [First Name], I help Nigerian e-commerce brands recover ₦500K-₦3M/month through AI-powered email automation. Saw [Brand Name] and thought we should connect.
   ```
4. After connection, send a DM within 24 hours:
   ```
   Thanks for connecting, [First Name]. Quick question — do you know what percentage of your abandoned carts you're currently recovering? Most stores I see are at 5-8%. The good ones hit 15-20%. Happy to run a free audit if you're curious.
   ```
5. Target: 30 new connections per day, 5 DM conversations per day, 1 discovery call booked per day.

**Channel 3: Free Audit Funnel**

1. Create a landing page on your website (or a Notion page) offering a "Free Email Program Audit."
2. The audit takes you 20 minutes using this process:
   - Sign up for the prospect's email list with a fresh email address
   - Document: Welcome sequence (exists? how many emails? quality?), email frequency, popup offer, segmentation quality
   - Use ChatGPT to analyze: "This is a [brand type] email program. Based on the 5 emails I received, rate the following on a scale of 1-10: subject line quality, segmentation, automation maturity, content quality, and revenue potential. Suggest 3 specific improvements."
3. Deliver the audit as a Loom video (5 minutes max) with a PDF summary.
4. At the end of the video: "I can implement all three of these improvements within 2 weeks. Would you like to see what that looks like?"
5. Conversion rate target: 20–30% of free audit recipients book a discovery call.

## Procedure 9.3: Run the Discovery Call

1. Send a Calendly link for a 30-minute call.
2. Before the call, research the prospect's email program (sign up for their list, check their flows, review their social media for recent promotions).
3. On the call, follow this script:

**Minutes 0–5**: "Tell me about your business. What's working? What's frustrating you about your current email program?"

**Minutes 5–15**: Share two specific observations about their email program (from your pre-call research). Example: "I noticed you don't have an abandoned cart flow. Based on stores similar to yours, that's typically ₦500K–₦2M/month in left-on-the-table revenue."

**Minutes 15–20**: Present your three-tier pricing. Show the rate card PDF. Say: "Most clients start at the Growth tier because it includes A/B testing and AI segmentation, which are the two things that move revenue fastest. But I'll let you decide what fits."

**Minutes 20–25**: Ask: "Which tier feels like the right fit?" Then be silent. Let them answer.

**Minutes 25–30**: If they choose a tier, send the contract immediately after the call. If they hesitate, offer the free audit (if you haven't already delivered one).

## Procedure 9.4: Close and Onboard

1. Create a contract template in Google Docs. Key terms:
   - Minimum commitment: 3 months
   - Payment: Due on the 1st of each month
   - Termination: 30 days written notice after the minimum period
   - Scope: Defined by the tier they selected
   - Exclusions: One-off promotional designs outside the agreed campaign count billed at ₦25,000 each
2. Send the contract via [hellosign.com](https://hellosign.com) or [signwithdocuSign](https://docusign.com) for e-signature.
3. Upon signing, create the client's Slack channel, Google Sheet, Klaviyo/ActiveCampaign account, and Canva Brand Kit within 24 hours.
4. Send the "Onboarding Questionnaire" via a Notion form:
   - Brand guidelines (colors, fonts, tone of voice)
   - Product catalog (top 10 bestsellers with images and prices)
   - Current email list size and source breakdown
   - Existing flows (if any) — export from current ESP
   - Business goals for the next 90 days
5. Schedule the kickoff call within 48 hours of signing. On this call, present the 90-day roadmap: what you'll build, in what order, and what revenue to expect.

{{% accent-box %}}HACK: The 3-month minimum commitment is non-negotiable. Email automation takes 60–90 days to show full results. Flows need time to accumulate data. A/B tests need sample sizes. Deliverability warm-up takes 14 days alone. A client who cancels after 30 days has seen zero results and will tell everyone your service doesn't work. A client who stays for 90 days has seen ₦2M–₦10M in attributed revenue and will refer you to three other founders. The minimum commitment protects them from premature termination and protects you from bad reviews. Frame it as: "Results compound over 90 days. The first month is setup, the second month is optimization, the third month is when you see the full revenue impact."{{% /accent-box %}}

## Check-In: Module 9 Complete

- [ ] Three case studies written and designed as PDFs
- [ ] Case studies published on website or Notion page
- [ ] Apollo.io account created with first prospect list exported
- [ ] 5-email cold outreach sequence built in ActiveCampaign
- [ ] PhantomBuster LinkedIn outreach campaign live
- [ ] Free audit landing page created
- [ ] Free audit process documented and tested on at least one prospect
- [ ] Discovery call script memorized and used on at least 3 calls
- [ ] Contract template created and sent via e-signature platform
- [ ] Onboarding questionnaire created in Notion
- [ ] At least 1 paying client signed and onboarded

---

# MODULE 10: SCALING & TEAM BUILDING

## Overview

At ₦1.5M/month in MRR (roughly 4–5 Growth-tier clients or 10 Starter clients), you will hit the solo operator ceiling. There are only so many hours in a day. You can write emails, build flows, and run reports for 4–5 clients by yourself. Beyond that, quality drops or you burn out. The only way past this ceiling is to build a team and systematize everything you do.

This module is about turning your skills into systems that other people can execute. If the business depends on you personally, you have a job — not a business. If the business runs without you for a week, you have a business.

## Procedure 10.1: Hire Your First Team Member

You need an Email Operations Associate. This person executes the procedures you've built in Modules 3–8. They do not need to be an email marketing expert. They need to be detail-oriented, comfortable with technology, and able to follow written procedures exactly.

1. Write a job posting:
```
TITLE: Email Operations Associate

ABOUT: We are an AI-powered email marketing automation company that helps e-commerce brands generate revenue through intelligent email programs. You will execute email campaigns, build automation flows, and generate AI-assisted content using our proprietary playbooks and tools.

REQUIREMENTS:
- Proficient in English (written) at a professional level
- Comfortable learning new software (Klaviyo, ActiveCampaign, Make.com, ChatGPT)
- Extremely detail-oriented (one wrong setting in an email flow can send 50,000 people the wrong email)
- Available full-time, Monday–Friday, 08:00–17:00 WAT
- Reliable internet connection and personal laptop

COMPENSATION: ₦180,000–₦250,000/month (based on experience)

TO APPLY: Send a 200-word email to [your email] explaining why you're detail-oriented enough to manage email automation for 10+ clients. Include the word "Klaviyo" in the subject line.
```

2. Post on: [jobberman.com](https://jobberman.com), LinkedIn, and Twitter/X.
3. Screen applicants: Send a paid test (₦10,000 stipend) — "Configure a 3-email welcome series in this Klaviyo account using this procedure document." If they can follow the procedure exactly and produce a working flow, they pass.
4. Hire within 14 days. Do not spend more than 14 days on hiring — every day without a team member is a day you're capping revenue.

## Procedure 10.2: Document Every Procedure as an SOP

Every procedure in this playbook becomes a Standard Operating Procedure (SOP) document in Notion. Each SOP follows this format:

```
SOP: [Procedure Name]
Last Updated: [Date]
Owner: [Name]
Time Estimate: [X minutes]

PURPOSE: [Why this procedure exists]

PREREQUISITES: [What must be completed before starting]

STEPS:
1. [Exact step with tool name, button to click, and field to fill]
2. [Next step]
...

VERIFICATION: [How to confirm the procedure was completed correctly]

COMMON ERRORS: [Mistakes others have made and how to avoid them]

SCREENSHOTS: [Annotated screenshots of every tool interface]
```

1. Document all 36 procedures from this playbook as individual SOPs in Notion.
2. For each SOP, record a Loom video walkthrough (5–10 minutes).
3. Your new hire learns by reading the SOP, watching the Loom video, and then executing the procedure on a test account while you watch.
4. Target: New hire is fully productive within 21 days.

## Procedure 10.3: Implement Quality Assurance

1. Create a "QA Checklist" in Notion for every deliverable type:

**Campaign QA Checklist:**
- [ ] Subject line under 45 characters
- [ ] Preview text complements subject line
- [ ] Links tested and working (click every link)
- [ ] Images loading correctly on desktop and mobile
- [ ] Correct segment selected
- [ ] Smart sending enabled
- [ ] UTM parameters added to all links (utm_source=klaviyo, utm_medium=email, utm_campaign=[campaign_name])
- [ ] Send test to yourself and client — approved in writing before scheduling

**Flow QA Checklist:**
- [ ] Trigger conditions correct
- [ ] All delays configured correctly
- [ ] Conditional splits logic verified
- [ ] Smart sending enabled
- [ ] Revenue attribution window set
- [ ] Goal actions configured (where applicable)
- [ ] Test contact added to verify flow entry and email receipt
- [ ] Client approval documented in Slack

2. No email or flow goes live without a completed QA checklist. This is non-negotiable. One misconfigured flow can send 10,000 people a discount code meant for 50 VIPs. The QA checklist is your insurance policy.

## Procedure 10.4: Scale from 5 to 15 Clients

**Revenue Target: ₦5.25M/month** (15 Growth-tier clients at ₦350,000 each)

1. Your team structure at this stage:
   - **You (Founder)**: Strategy, client relationships, A/B test design, reporting
   - **Email Operations Associate 1**: Flow building, campaign execution, list management (handles 7–8 clients)
   - **Email Operations Associate 2**: Same scope (handles 7–8 clients)
   - **Part-time Copy Editor**: Reviews all AI-generated content before publishing (₦80,000/month, 15 hours/week)

2. Client distribution: Each associate manages 7–8 client accounts. You oversee all accounts and handle strategy, client calls, and reporting.

3. Hiring timeline:
   - Month 1: Hire Associate 1 (you train while managing 5 clients)
   - Month 3: Hire Associate 2 (Associate 1 takes on 5 clients, you take on 2 new clients)
   - Month 4: Hire part-time Copy Editor
   - Month 5–6: Scale to 15 clients

4. Your time allocation at 15 clients:
   - Client strategy calls: 8 hours/week (30 min per client, weekly for Enterprise, biweekly for Growth)
   - A/B test design and analysis: 6 hours/week
   - Team management and QA: 6 hours/week
   - Reporting: 4 hours/week
   - New business: 6 hours/week
   - **Total: 30 hours/week**

## Procedure 10.5: Scale from 15 to 35 Clients — The ₦12M/month Milestone

**Revenue Target: ₦12.25M/month** (35 clients across all tiers: 15 Starter at ₦150K, 15 Growth at ₦350K, 5 Enterprise at ₦750K)

1. Your team structure:
   - **You (Founder/CEO)**: No client work. Strategy, sales, team leadership, and brand building only.
   - **Operations Manager**: Oversees the two associates, handles QA escalations, manages client onboarding (₦400,000/month)
   - **Email Operations Associate 1**: 12 clients (Starter and Growth)
   - **Email Operations Associate 2**: 12 clients (Starter and Growth)
   - **Email Operations Associate 3**: 8 clients (Growth and Enterprise)
   - **Senior Strategist**: Handles Enterprise client strategy, A/B test design, and complex flow architecture (₦500,000/month)
   - **Copy Editor**: Full-time, reviews all content (₦180,000/month)
   - **Sales Associate**: Runs the cold outreach engine, books discovery calls, manages the pipeline (₦200,000/month + commission)

2. Total payroll at ₦12M/month revenue: approximately ₦2.5M/month (including all salaries, tool costs, and overhead). Net margin: 75–80%.

3. At this stage, you stop executing and start leading. If you are still building flows at 35 clients, you have not built a business — you have built a prison. The SOPs, the QA process, and the team structure exist specifically to remove you from execution.

## Procedure 10.6: Build the Recurring Revenue Engine

The ultimate goal is not more clients. It is more predictable revenue from existing clients with lower churn.

1. **Reduce churn to under 5% monthly**: The industry average for email marketing retainers is 15–20% monthly churn. You will target 5% or less. How:
   - Deliver results within 90 days (the minimum commitment period ensures they see results before they can leave)
   - Send the monthly report religiously — clients who see their numbers stay
   - Respond to Slack messages within 4 business hours — responsiveness = trust
   - Proactively suggest new tests and optimizations — demonstrate that you're always improving, not just maintaining

2. **Increase average revenue per client**:
   - Starter clients who see results will upgrade to Growth. Pitch the upgrade at month 3.
   - Growth clients with 3+ product categories will benefit from Enterprise. Pitch at month 6.
   - Each upgrade increases your MRR without adding a new client.

3. **Build referral incentives**: Offer any active client one free month of service for every referral that signs a 3-month contract. At ₦350,000/month, one free month costs you ₦350,000 in gross revenue but gains you a new ₦350,000/month client — a 2-month payback period on the "investment."

4. **Track this dashboard monthly**:
   - MRR: ₦[Total]
   - Net New MRR: ₦[New] - ₦[Churned]
   - Churn Rate: [X]%
   - Average Revenue Per Client: ₦[X]
   - Client Count: [X]
   - Revenue per Team Member: ₦[X] (target: ₦1M+/month per team member at scale)

{{% accent-box %}}HACK: Create a "Quarterly Business Review" (QBR) for every client, even Starter-tier. This is a 30-minute video call where you present the last 90 days of results and the next 90 days of strategy. The QBR does three things: (1) reminds the client of the value you're delivering, (2) surfaces upsell opportunities, and (3) makes it psychologically harder to cancel because they have a personal relationship with you that goes beyond a monthly invoice. Clients who receive QBRs churn at half the rate of clients who don't. Schedule them on day 90, 180, 270, and 365 from onboarding.{{% /accent-box %}}

## Check-In: Module 10 Complete

- [ ] Job posting written and published on three platforms
- [ ] At least one Email Operations Associate hired and trained
- [ ] All 36 procedures documented as SOPs in Notion
- [ ] Loom walkthrough videos recorded for each SOP
- [ ] Campaign QA Checklist and Flow QA Checklist created in Notion
- [ ] QA process enforced — no deliverable goes live without a signed checklist
- [ ] Scaling roadmap documented: 5 → 15 → 35 clients with hiring timeline
- [ ] Churn tracking added to your Notion Revenue Tracker database
- [ ] Referral incentive program created and communicated to all active clients
- [ ] Quarterly Business Review scheduled for all active clients

---

# THE THREE-TIER PRICING TABLE

| | **Starter** | **Growth** | **Enterprise** |
|---|---|---|---|
| **Monthly Fee** | ₦150,000 | ₦350,000 | ₦750,000 |
| **Automated Flows** | 4 | 8 | 12+ |
| **Campaigns/Month** | 2 | 4 | Unlimited |
| **Segmentation** | Basic (3 tiers) | AI-Powered (5 tiers) | AI-Powered (5 tiers + custom) |
| **A/B Testing** | ❌ | ✅ (2 tests/month) | ✅ (Unlimited) |
| **AI Content Engine** | ❌ | ✅ | ✅ |
| **Reporting** | Monthly | Biweekly | Weekly |
| **Communication Channel** | Email | Slack | Slack + Weekly Call |
| **Strategy Reviews** | ❌ | Quarterly | Monthly |
| **Best For** | Small e-commerce (₦5M–₦20M/mo revenue) | Growing e-commerce (₦20M–₦80M/mo revenue) | Scale e-commerce (₦80M+/mo revenue) |
| **Expected ROI** | 5–10x | 10–20x | 15–35x |

**Minimum commitment: 3 months for all tiers.** No exceptions.

---

# TOOL COST SUMMARY

| Tool | Monthly Cost (₦) | Purpose |
|------|-------------------|---------|
| Klaviyo (250–500 contacts) | ₦0–₦25,000 | Primary ESP (e-commerce) |
| ActiveCampaign Plus | ₦78,000 | Primary ESP (B2B) |
| ChatGPT Plus | ₦32,000 | AI content engine |
| Make.com Core | ₦16,000 | Automation orchestration |
| Canva Pro | ₦21,000 | Visual asset production |
| Google Workspace | ₦10,000 | Docs, Sheets, Slides |
| PhantomBuster Starter | ₦110,000 | LinkedIn outreach |
| Apollo.io Free | ₦0 | Prospect data |
| Notion Team | ₦8,000 | SOPs, project management |
| Slack Free | ₦0 | Client communication |
| **Total (at launch)** | **₦275,000–₦300,000** | |

At your first Growth-tier client (₦350,000/month), your tool stack is fully covered and you are net positive. Every client after that is 90%+ margin.

---

# 12-MONTH REVENUE PROJECTION

| Month | Clients | MRR | Tool Costs | Payroll | Net Profit |
|-------|---------|-----|------------|---------|------------|
| 1 | 1 | ₦350,000 | ₦300,000 | ₦0 | ₦50,000 |
| 2 | 2 | ₦700,000 | ₦300,000 | ₦0 | ₦400,000 |
| 3 | 3 | ₦850,000 | ₦300,000 | ₦0 | ₦550,000 |
| 4 | 4 | ₦1,200,000 | ₦300,000 | ₦180,000 | ₦720,000 |
| 5 | 5 | ₦1,500,000 | ₦300,000 | ₦180,000 | ₦1,020,000 |
| 6 | 7 | ₦2,100,000 | ₦350,000 | ₦360,000 | ₦1,390,000 |
| 7 | 9 | ₦2,800,000 | ₦350,000 | ₦360,000 | ₦2,090,000 |
| 8 | 12 | ₦3,800,000 | ₦400,000 | ₦540,000 | ₦2,860,000 |
| 9 | 15 | ₦5,250,000 | ₦400,000 | ₦900,000 | ₦3,950,000 |
| 10 | 20 | ₦6,500,000 | ₦450,000 | ₦1,380,000 | ₦4,670,000 |
| 11 | 28 | ₦8,400,000 | ₦500,000 | ₦1,880,000 | ₦6,020,000 |
| 12 | 35 | ₦12,250,000 | ₦600,000 | ₦2,500,000 | ₦9,150,000 |

These numbers assume: 70% of clients at Growth tier, 20% at Starter, 10% at Enterprise. They also assume you follow every procedure in this playbook, hire on schedule, and maintain under 5% monthly churn. If you cut corners, these numbers are fiction. If you execute, they are conservative.

---

# FINAL DIRECTIVE

You now have a complete operating system. 10 modules. 36 procedures. Every tool named. Every setting specified. Every flow configured. Every script written. There is nothing missing. There is no additional information you need to start.

The only variable left is execution.

Open Klaviyo. Create the account. Build the first flow. Send the first campaign. Get the first client. Deliver the first result. Then do it again. And again. And again.

The gap between reading this playbook and building a ₦12M/month business is not knowledge. It is reps. Do the reps.

Start now.
