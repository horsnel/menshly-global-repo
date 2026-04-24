---
title: "Build and Automate an AI Lead Generation System with Make.com and OpenAI"
date: 2026-04-18
category: "Implementation"
difficulty: "INTERMEDIATE"
readTime: "26 MIN"
excerpt: "The complete execution guide for building an AI-powered lead generation system that finds, enriches, scores, and delivers qualified leads on autopilot."
image: "/images/articles/intelligence/build-ai-lead-generation-system.png"
heroImage: "/images/heroes/intelligence/build-ai-lead-generation-system.png"
relatedOpportunity: "/opportunities/ai-lead-generation-machine/"
relatedPlaybook: "/playbooks/ai-automation-agency-playbook/"
---

Lead generation is the lifeblood of every business. Most businesses do it manually — searching LinkedIn, copying emails into spreadsheets, writing generic outreach messages, and hoping something sticks. That process is slow, inconsistent, and does not scale. An AI-powered lead generation system fixes every one of those problems. It finds prospects, enriches their data, scores them, writes personalized outreach, and routes the best leads to your sales team — all without human intervention.

This guide builds the complete system from zero. Follow every step in order. Each step depends on the previous one. If you skip ahead, your data will not flow correctly and troubleshooting will take longer than building it right the first time.

## Prerequisites

Before you start, gather these accounts and tools:

- A Make.com account — go to make.com and sign up for the Free plan (1,000 operations/mo)
- An OpenAI API key with $10 credit — go to platform.openai.com/api-keys
- An Apollo.io account (free tier) — go to apollo.io and sign up, or a Hunter.io account (free tier) — go to hunter.io
- A Google account (for Google Sheets and Gmail modules)
- A Slack account with a workspace where you have admin or app-install permissions
- A LinkedIn Sales Navigator account (free trial works for setup)
- A test email address you control (separate from your personal email)
- 6-8 hours of uninterrupted time for your first full build

Total upfront cost: $10 for the OpenAI API key. Apollo.io and Hunter.io free tiers cover your first 50-100 lead lookups. Everything else is free until you have paying clients.

## Step 1: Set Up Your Lead Data Sources

Your lead generation system needs data to work with. You will configure three sources: an email finder for contact discovery, a Google Sheet as your central lead database, and LinkedIn Sales Navigator for professional context. These three sources together give you enough raw material for AI to produce high-quality, enriched leads.

### Configure Apollo.io or Hunter.io for Email Finding

Open your browser and go to apollo.io. Sign in with the account you created. You should see the Apollo dashboard — a top navigation bar with "Search," "Sequences," and "Analytics" tabs.

Do you see the dashboard? If you see an onboarding wizard, complete it first (select the free plan when prompted). You need to reach the main dashboard before continuing.

Click the **Search** tab in the top navigation. You will see a filter panel on the left and a list of contacts on the right. This is Apollo's lead database. The free tier gives you 60 email credits per month — enough for testing and your first few clients.

If you prefer Hunter.io, go to hunter.io, sign in, and click **Domain Search** in the top navigation. Enter any company domain (e.g., "stripe.com") and Hunter will return email addresses with names and titles. The free tier gives you 25 searches per month.

You do not need to do anything else in Apollo or Hunter right now. You will connect them to Make.com in Step 2. But confirm that you can find at least one lead manually before moving on. Search for "VP of Marketing" at a company you know. Do you see results with names, titles, and email addresses? If you see "Upgrade to view" on every email, your free credits are exhausted. Create a new account or switch to Hunter.io.

### Set Up Google Sheets as Lead Database

Go to Google Drive (drive.google.com). Create a new Google Sheet. Name it `Lead Gen Pipeline`. Create the following column headers in Row 1:

| Column | Header |
|--------|--------|
| A | Timestamp |
| B | First Name |
| C | Last Name |
| D | Email |
| E | Company |
| F | Title |
| G | LinkedIn URL |
| H | Source |
| I | Enrichment Data |
| J | Lead Score |
| K | Status |

This sheet is the single source of truth for your entire pipeline. Every lead enters here, gets enriched, and gets routed. Do not skip any column — you will use every one of them.

Your sheet should look like this after adding the headers:

> | Timestamp | First Name | Last Name | Email | Company | Title | LinkedIn URL | Source | Enrichment Data | Lead Score | Status |
> |-----------|-----------|-----------|-------|---------|-------|-------------|--------|----------------|-----------|--------|
> | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) | (empty) |

Do you see all 11 column headers? If any are missing, add them now. The Make.com modules you configure later will fail silently if the expected columns do not exist.

### Connect LinkedIn Sales Navigator

Open LinkedIn and navigate to Sales Navigator (linkedin.com/sales). If you have a free trial, activate it. Sales Navigator gives you advanced search filters — department headcount, years in role, company growth rate — that make your lead lists far more targeted than basic LinkedIn search.

You will not connect Sales Navigator directly to Make.com. Instead, you will export lead lists from Sales Navigator as CSV files and import them into your Google Sheet. This approach avoids LinkedIn's strict API restrictions and keeps your workflow simple.

Export a test list: search for "Marketing Director" in your target industry, select 10 leads, and click **Export**. Download the CSV. Open it and copy the relevant columns (First Name, Last Name, Email, Company, Title, LinkedIn URL) into your `Lead Gen Pipeline` Google Sheet. Add today's timestamp in Column A and "LinkedIn" in Column H for each row.

### Interactive Check-in

Search for 10 leads using either Apollo.io, Hunter.io, or LinkedIn Sales Navigator. Import them into your `Lead Gen Pipeline` Google Sheet. Do they appear in your Google Sheet with all columns populated?

You should see 10 rows of data below your headers. If any cells are empty, go back and fill them — incomplete rows will cause errors in the enrichment step. Expected output:

> | Timestamp | First Name | Last Name | Email | Company | Title | LinkedIn URL | Source |
> |-----------|-----------|-----------|-------|---------|-------|-------------|--------|
> | 2026-04-24 | Sarah | Chen | sarah.chen@acmecorp.com | Acme Corp | VP Marketing | linkedin.com/in/sarahchen | LinkedIn |
> | 2026-04-24 | Marcus | Williams | m.williams@techflow.io | TechFlow | CMO | linkedin.com/in/marcusw | Apollo |
> | ... | ... | ... | ... | ... | ... | ... | ... |

If you see 10 populated rows, move to Step 2. If the import created duplicate rows or garbled data, clean the sheet manually before proceeding. Dirty data now means broken automations later.

## Step 2: Build the Lead Enrichment Workflow

This is the core of the system. You will build a Make.com scenario that watches your Google Sheet for new leads, enriches each lead with company data from Clearbit, scores the lead using OpenAI, and writes the results back to the sheet. This scenario runs on autopilot — every time you add a new lead, it gets enriched and scored within minutes.

### Create the Make.com Scenario

Open Make.com and sign in. From the dashboard, click **Create a new scenario**. A blank canvas will appear with a large "+" button in the center.

Click the **+** button. Search for "Google Sheets" and select the **Watch Rows** trigger module.

Configure it:
1. **Connection:** Click "Add" and connect your Google account. Follow the OAuth flow.
2. **Spreadsheet:** Select `Lead Gen Pipeline` from the dropdown.
3. **Sheet:** Select "Sheet1."
4. **Range:** `A1:K1000`
5. **Column with timestamps:** Select column A.
6. **Polling interval:** Set to 5 minutes.

Click **OK**. The module should turn from gray to colored with a small clock icon. Do you see this? If the module is still gray, the Google Sheets connection failed. Remove the connection, reconnect your Google account, and try again.

### Add the Clearbit Enrichment Module

Hover over the right edge of the Google Sheets module until a "+" appears. Click it. Search for "HTTP" and select **Make a Request**. You will use this to call the Clearbit Discovery API directly, since Make.com does not have a native Clearbit module.

Configure it:
1. **URL:** `https://company.clearbit.com/v2/companies/find?domain={{4.email}}`
   - Replace `{{4.email}}` with the mapped Email variable from the Google Sheets module. Click in the URL field, type the URL up to `domain=`, then click and select the Email variable from the popup.
2. **Method:** GET
3. **Headers:** Add a header with key `Authorization` and value `Bearer YOUR_CLEARBIT_API_KEY`
   - If you do not have a Clearbit API key, you can sign up at clearbit.com for a free trial. Alternatively, skip this module and move to the OpenAI scoring module — OpenAI can generate enrichment data from the lead's email domain and company name alone, though the data will be less precise.
4. **Parse response:** Yes

Click **OK**. This module takes the lead's email domain, queries Clearbit, and returns company data including industry, employee count, annual revenue, funding stage, and tech stack.

**Troubleshooting:** If the HTTP module returns a 401 error, your Clearbit API key is invalid. If it returns a 404, the company domain was not found in Clearbit's database — this is normal for very small companies. If it returns a 429, you hit the rate limit — add a **Sleep** module before the HTTP request set to 2 seconds.

### Add the OpenAI Scoring Module

Add another module after the Clearbit HTTP module. Search for "OpenAI" and select **Create a Chat Completion**.

Configure it:
1. **Connection:** Add your OpenAI API key.
2. **Model:** Select `gpt-4o`.
3. **Messages:** Add one message with role "System" and this content:

```
You are a B2B lead scoring assistant. Given a lead's name, title, company, and enrichment data, you will:

1. Score the lead from 1 to 10 based on fit with the ideal customer profile.
   Scoring criteria:
   - Title seniority (VP, Director, C-suite = higher score)
   - Company size (50-500 employees = sweet spot)
   - Industry relevance (SaaS, technology, professional services = higher score)
   - Growth signals (hiring, funding, expansion = higher score)
2. Write a 1-sentence rationale for the score.
3. Suggest the best outreach channel and approach.

Respond in this exact JSON format and nothing else:
{"score": 8, "rationale": "VP-level decision maker at a mid-market SaaS company actively hiring", "channel": "LinkedIn InMail", "approach": "Reference their recent funding round and offer a specific ROI case study"}
```

4. Add a second message with role "User" and this content:

```
Name: {{2.firstName}} {{2.lastName}}
Title: {{2.title}}
Company: {{2.company}}
Email: {{2.email}}
Company Enrichment: {{5.body}}
```

Map each variable from the previous modules. The `{{2.firstName}}` style references come from Make.com's variable selector — always click into the field and use the popup to select variables rather than typing them manually. The `{{5.body}}` maps to the Clearbit HTTP response.

Click **OK**.

### Parse the OpenAI Response

The OpenAI module returns a JSON string inside a text field. Make.com cannot access nested values from raw text. You need to parse it.

Add a **JSON — Parse JSON** module after the OpenAI module. In the JSON string field, map the OpenAI response content variable (`choices[1].message.content`). This converts the AI's text response into structured fields that Make.com can access as individual variables.

### Write Results Back to Google Sheets

Add a **Google Sheets — Update a Row** module at the end. Configure it:
1. **Spreadsheet:** `Lead Gen Pipeline`
2. **Sheet:** Sheet1
3. **Row number:** Map the row number variable from the Watch Rows trigger
4. **Column I (Enrichment Data):** Map the Clearbit company description or industry
5. **Column J (Lead Score):** Map `{{6.score}}` from the parsed JSON
6. **Column K (Status):** Set to `Scored`

Click **OK**.

### Test the Enrichment Workflow

Go to your Google Sheet and add a new test lead:
- Column A: Current timestamp
- Column B: "Jessica"
- Column C: "Park"
- Column D: "jessica.park@meridiantech.com"
- Column E: "Meridian Tech"
- Column F: "Director of Operations"
- Column G: (leave blank)
- Column H: "Manual"

Come back to Make.com and click **Run once**. The scenario should execute: the Google Sheets module finds the new row, Clearbit enriches the company data, OpenAI scores the lead, the JSON parser structures the response, and the Update module writes the results back.

Check your Google Sheet. Do you see the enriched data and score in columns I, J, and K? Expected output:

> | Enrichment Data | Lead Score | Status |
> |----------------|-----------|--------|
> | SaaS company, 120 employees, Series B, $8M ARR | 8 | Scored |

If the enrichment data is empty, the Clearbit API call failed — check the HTTP module's execution log for the error code. If the score is missing, the OpenAI response was not parsed correctly — open the Parse JSON module and verify that the JSON string field contains the OpenAI response variable, not literal text. If the status still says empty, the Update module is writing to the wrong row — check the row number mapping.

### Interactive Check-in

Add a test lead to your Google Sheet. Does the enriched data appear with a score? You should see the Lead Score column populated with a number between 1 and 10, the Enrichment Data column filled with company information, and the Status column changed from empty to "Scored." If all three are correct, your enrichment workflow is complete.

## Step 3: Build the Outreach Automation

A scored lead that sits in a spreadsheet is worthless. This step generates personalized cold emails using AI and sends them automatically with rate limiting and follow-up sequences.

### Generate Personalized Cold Emails

Go back to your Make.com scenario. After the Parse JSON module (but before the Google Sheets Update module), insert a new **OpenAI — Create a Chat Completion** module.

Configure it:
1. **Model:** `gpt-4o`
2. **System message:**

```
You are an expert cold email writer. Given a lead's name, title, company, score rationale, and suggested approach, write a personalized cold email that:

1. Opens with a specific observation about their company or role (never "I hope this finds you well")
2. States a clear value proposition tied to their likely pain point
3. Includes one concrete proof point (metric, case study result, or testimonial)
4. Ends with a low-friction CTA (never "Let's schedule a 30-minute call")
5. Is under 100 words total

Do not use exclamation marks. Do not use the word "excited." Sound like a peer, not a salesperson.
```

3. **User message:**

```
Name: {{2.firstName}} {{2.lastName}}
Title: {{2.title}}
Company: {{2.company}}
Score Rationale: {{6.rationale}}
Suggested Approach: {{6.approach}}
```

Click **OK**. This module generates a unique, personalized email for every lead based on their profile and score.

### Set Up Gmail Sending with Rate Limiting

Add a **Gmail — Send an Email** module after the new OpenAI module. Configure it:
1. **Connection:** Connect your Gmail account (follow the OAuth flow)
2. **To:** Map the Email variable from the Google Sheets trigger
3. **Subject:** `{{2.firstName}}, a thought on [their challenge]`
   - Replace `[their challenge]` with a mapped variable or a general placeholder like `{{2.company}} growth`
4. **Body (HTML):** Map the generated email from the OpenAI module

Click **OK**.

**Rate limiting is critical.** Gmail's sending limit is 500 emails per day for regular accounts and 2,000 per day for Google Workspace accounts. If you blast 200 emails in 10 minutes, Gmail will flag your account. To prevent this:

1. Right-click the Gmail module and select **Settings**.
2. Enable **Make.com's built-in rate limiting**. Set it to send no more than 1 email per 30 seconds. This caps you at 120 emails per hour — well within Gmail's limits.
3. Alternatively, add a **Sleep** module before the Gmail module set to 30 seconds. This inserts a 30-second delay between each email.

### Configure Follow-Up Sequences

A single email rarely converts. You need follow-ups. The simplest approach in Make.com is a second scenario triggered by time delays.

Create a new scenario. Add a **Google Sheets — Search Rows** trigger. Configure it to search your `Lead Gen Pipeline` sheet for rows where:
- Status = "Scored" (email was sent)
- AND the Timestamp is more than 3 days ago

This finds leads who received your first email 3+ days ago but have not responded.

After the search module, add a **Gmail — Send an Email** module. Write a shorter follow-up:

1. **Subject:** `Re: {{2.subject}}` (this threads the conversation)
2. **Body:** Generate a brief follow-up using another OpenAI module with this prompt:

```
Write a 2-sentence follow-up email to a cold outreach. Reference the previous email's value proposition. Be brief and confident — never apologetic. No exclamation marks.
```

After sending, add a **Google Sheets — Update a Row** module that changes the Status from "Scored" to "Follow-up 1 Sent."

Create a third scenario for the second follow-up, triggered 7 days after the first follow-up, using the same pattern. Change the Status to "Follow-up 2 Sent" after execution.

### Interactive Check-in

Check the draft folder of your sending email account. Do you see the personalized emails? If you configured the Gmail module to send directly (not save as draft), check the Sent folder instead. You should see at least one email addressed to your test lead with a personalized subject line and body that references their company and role.

If the email is blank or generic, the OpenAI module is not receiving the mapped variables. Open the OpenAI email generation module, click in the User message field, and verify that each `{{}}` reference shows a green variable tag. If you see plain text instead of a green tag, the mapping is broken — clear the field and re-map using the variable selector.

If the email was not sent at all, check the Gmail module's execution log. A 403 error means your Gmail OAuth scope does not include "send" — reconnect your Gmail account and grant full permissions. A 429 error means you hit the rate limit — increase the delay between sends.

## Step 4: Build the Lead Routing System

Not all leads deserve the same level of attention. A lead scored 8-10 is hot and needs an immediate response. A lead scored 4-7 is warm and belongs in a daily digest. A lead scored 1-3 is cold and should enter a long-term nurture sequence. This routing logic ensures your sales team focuses on the leads most likely to convert.

### Add a Router Module

Go back to your main Make.com scenario (the enrichment workflow). After the Parse JSON module, insert a **Router** module. A Router splits the workflow into multiple paths based on conditions. You will see two output paths labeled 1 and 2. Click the Router and add a third path (click the "+" on the Router).

### Configure Path 1: Hot Lead (Score 8-10)

Click the filter icon on Path 1. Set the condition:
- **Variable:** Map the `score` field from the Parse JSON module
- **Operator:** Greater than or equal to
- **Value:** `8`

On this path, add a **Slack — Create a Message** module. Configure it:
1. **Connection:** Connect your Slack workspace
2. **Channel:** `#hot-leads` (create this channel if it does not exist)
3. **Text:**

```
HOT LEAD ALERT
Name: {{2.firstName}} {{2.lastName}}
Title: {{2.title}} at {{2.company}}
Email: {{2.email}}
Score: {{6.score}}/10
Rationale: {{6.rationale}}
Approach: {{6.approach}}

Respond within 1 hour for best conversion odds.
```

Click **OK**.

Also on this path, add a **Google Sheets — Update a Row** module that sets the Status column to "Hot — Alerted." This gives you an audit trail.

### Configure Path 2: Warm Lead (Score 4-7)

Click the filter icon on Path 2. Set the condition:
- **Variable:** Map the `score` field from the Parse JSON module
- **Operator:** Between
- **Value:** `4` and `7`

On this path, add a **Google Sheets — Update a Row** module that sets the Status column to "Warm — Digest." Also add a **Google Sheets — Add a Row** module that writes the lead to a separate spreadsheet called "Warm Leads Daily Digest." This spreadsheet is what your sales team reviews once per day.

### Configure Path 3: Cold Lead (Score 1-3)

Click the filter icon on Path 3. Set the condition:
- **Variable:** Map the `score` field from the Parse JSON module
- **Operator:** Less than or equal to
- **Value:** `3`

On this path, add a **Google Sheets — Update a Row** module that sets the Status column to "Cold — Nurture." Add a second Google Sheets module that writes the lead to a "Nurture Campaign" spreadsheet. These leads will receive automated educational content over the next 30-60 days — not a sales pitch.

### CRM Integration for Warm Leads

If your client uses a CRM (HubSpot, Pipedrive, Salesforce), add the integration on the warm lead path. For HubSpot:

1. Add a **HubSpot — Create a Contact** module on Path 2
2. Map the lead's first name, last name, email, company, and title
3. Set a custom property "Lead Score" with the AI-generated score
4. Set the Lifecycle Stage to "Lead"

For Pipedrive:
1. Add a **Pipedrive — Create a Person** module on Path 2
2. Map the same fields
3. Add a **Pipedrive — Create a Deal** module after it
4. Set the deal value based on the lead score (score 7 = $5K estimated deal, score 5 = $2K, etc.)

### Test All Three Paths

Add three test leads to your Google Sheet with data designed to trigger different scores:

1. **Hot lead:** C-suite title at a Series B SaaS company → should score 8+
2. **Warm lead:** Manager at a mid-size professional services firm → should score 4-7
3. **Cold lead:** Junior title at a small local business → should score 1-3

Run the scenario once for each lead. Verify each path triggers correctly.

### Interactive Check-in

Add a hot lead to your Google Sheet. Did the Slack notification arrive within 5 minutes? Open your `#hot-leads` Slack channel. You should see a message like:

> HOT LEAD ALERT
> Name: Jessica Park
> Title: Director of Operations at Meridian Tech
> Email: jessica.park@meridiantech.com
> Score: 8/10
> Rationale: VP-level decision maker at a mid-market SaaS company actively hiring
> Approach: Reference their recent funding round and offer a specific ROI case study
>
> Respond within 1 hour for best conversion odds.

If the Slack notification arrived, your routing is working. If it did not arrive, check three things:
1. Is the Slack app installed in your workspace? Go to Slack's app management page and verify.
2. Is the filter condition comparing numbers to numbers? If the parsed score is a string type, the comparison will fail. Wrap it in `parseNumber()` in the filter.
3. Did the scenario run at all? Check the execution history (click the scenario name → History tab) for errors.

If the warm lead did not appear in the "Warm Leads Daily Digest" spreadsheet, verify the Google Sheets Add a Row module is pointing to the correct spreadsheet and that the column mappings are right.

## Step 5: Monitor, Optimize, and Price

A lead generation system that runs without monitoring will degrade. Email deliverability drops, AI prompts produce stale outputs, lead sources change their data structure. You need a dashboard and a regular optimization cadence.

### Dashboard Setup in Google Sheets or Notion

Create a new Google Sheet called "Lead Gen Dashboard" or a Notion database. Track these metrics weekly:

| Metric | How to Measure | Target |
|--------|---------------|--------|
| Leads generated | Count of new rows in Lead Gen Pipeline | 50-100/week |
| Average lead score | Average of Column J | 5.5+ |
| Hot lead % | Count of Score 8+ / Total leads | 15-20% |
| Email open rate | Gmail tracking or a tool like Mixmax | 40%+ |
| Reply rate | Manual tracking or CRM | 8-12% |
| Hot lead response time | Time between Slack alert and first outreach | Under 1 hour |
| Cost per lead | Total tool costs / Leads generated | Under $2.00 |

Set up a weekly Make.com scenario that calculates these metrics automatically:
1. **Schedule trigger:** Every Monday at 9 AM
2. **Google Sheets — Search Rows:** Pull all leads from the past 7 days
3. **Aggregator:** Count total leads
4. **Math functions:** Calculate averages and percentages
5. **Slack — Create a Message:** Post the weekly summary to `#lead-gen-metrics`

### Response Rate Tracking and Email Optimization

The most impactful optimization is improving your cold email copy. Here is the process:

1. **After 2 weeks**, review open rates. If below 35%, your subject lines are the problem. Rewrite them to be shorter (under 5 words), more specific (reference the lead's company), and less salesy.
2. **After 4 weeks**, review reply rates. If below 5%, your email body is the problem. Shorten it (under 75 words), make the CTA lower friction ("Worth a quick reply?" instead of "Can we schedule a call?"), and A/B test two versions.
3. **After 8 weeks**, review lead quality. If hot leads are not converting to meetings, your scoring criteria are wrong. Adjust the OpenAI scoring prompt — weight title seniority more heavily, or add negative factors like "freelancer" or "consultant" that tend to score high but never buy.

To A/B test emails, duplicate your OpenAI email generation module with a different prompt variant. Use a Router with a random 50/50 split (set the condition to `modulo(lead.rowNumber, 2) = 0` for one path and `= 1` for the other). Track which variant gets more replies in your dashboard.

### Pricing

Your AI lead generation system is a product. Price it like one.

| Tier | Setup Fee | Monthly Retainer | What's Included |
|------|-----------|-----------------|-----------------|
| Starter | $2,000 | $500/mo | 1 lead source, basic enrichment, cold email, Slack alerts, weekly report |
| Growth | $4,000 | $1,000/mo | 3 lead sources, Clearbit enrichment, AI scoring, 3-email sequence, CRM integration, weekly optimization |
| Enterprise | $7,000 | $2,000/mo | Unlimited sources, custom scoring model, multi-channel outreach, dedicated account manager, daily optimization |

The setup fee covers your build time. The Growth tier takes 8-12 hours to build. At $4,000, that is $330-500/hour. The retainer covers ongoing monitoring, optimization, and tool costs.

Your tool costs per client:
- Make.com: $9-16/mo (Core or Pro plan)
- OpenAI API: $15-50/mo (depends on lead volume)
- Clearbit: $0-99/mo (free trial, then Enrichment API)
- Apollo.io: $0-49/mo (free tier, then Basic plan)

**Total monthly cost per Growth client:** ~$60-120/mo
**Monthly retainer revenue per Growth client:** $1,000/mo
**Gross margin:** ~88-94%

## Cost Breakdown

| Item | Free Tier | Paid Tier | When to Upgrade |
|------|-----------|-----------|-----------------|
| Make.com | 1,000 ops/mo | $9/mo (10K ops) → $16/mo (10K ops, Pro) | At first paying client |
| OpenAI API | Pay per use | ~$15-50/mo per client | Scales with lead volume |
| Apollo.io | 60 email credits/mo | $49/mo (Basic, unlimited) | At 60+ leads/mo per client |
| Hunter.io | 25 searches/mo | $34/mo (Starter) | If using Hunter instead of Apollo |
| Clearbit | Free trial (50 enrichments) | $99/mo (Enrichment API) | At first paying client |
| Google Sheets | Free | Free | — |
| Gmail | 500 emails/day | Google Workspace ($6/mo, 2K/day) | At 500+ emails/day |
| Slack | Free | Free | — |
| Notion | Free | $10/mo | At 5+ clients for team features |

**Total monthly cost at 1 client (Growth tier):** ~$120-220/mo
**Total monthly revenue at 1 client (Growth tier):** $1,000/mo retainer + $4,000 setup
**Total monthly cost at 3 clients:** ~$250-400/mo
**Total monthly revenue at 3 clients:** $3,000/mo retainers + setup fees

## Production Checklist

Before activating the lead generation system for any client, verify every item:

- [ ] All three routing paths (hot, warm, cold) trigger correctly with test data
- [ ] Error handlers are attached to the OpenAI, Clearbit, and Gmail modules
- [ ] Automatic retry is enabled on every API module (3 retries, 10-second interval)
- [ ] Email rate limiting is configured (1 email per 30 seconds minimum)
- [ ] Follow-up sequences are tested end-to-end (first email → 3-day follow-up → 7-day follow-up)
- [ ] Slack notifications for hot leads arrive within 5 minutes of lead scoring
- [ ] CRM integration writes contacts and deals with correct field mappings
- [ ] The scoring prompt produces consistent results (test with 10 leads and verify no wild outliers)
- [ ] Weekly dashboard scenario runs and posts metrics to Slack
- [ ] Client has been trained on how to read the dashboard and respond to hot lead alerts

## What to Do Next

Once the core system is running for your first client, expand and compound:

- Add **multi-channel outreach** — connect LinkedIn InMail automation via Expandi or Zopto ($50-100/mo) for leads who do not respond to email
- Build a **nurture content engine** — automatically send educational content to cold leads over 60 days using a Make.com scenario with a daily schedule trigger
- Create a **client portal in Notion** where clients can view their dashboard, submit new target criteria, and track response rates
- Offer **lead list building as a standalone service** — some clients just want enriched, scored lists without the outreach automation. Price it at $1,000-1,500/mo
- Implement **reply detection** — connect your inbox to Make.com, use OpenAI to classify replies as positive/negative/neutral, and route positive replies to the client's sales team in real time
- Scale horizontally — clone the entire system for new business verticals. A dental lead gen system and a SaaS lead gen system use the same architecture with different scoring prompts and email templates
