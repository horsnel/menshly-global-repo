---
title: "Automation Agency Starter Kit"
date: 2026-04-19
category: "Playbook"
price: "$29"
readTime: "35 MIN"
excerpt: "The complete launch system for starting an automation agency from zero. 8 modules, 26 procedures, exact tool configurations, cold outreach scripts, three pricing tiers, and a scaling roadmap. From empty Notion workspace to $10K/month in recurring revenue."
image: "/images/articles/playbooks/automation-agency-starter-kit.png"
heroImage: "/images/heroes/playbooks/automation-agency-starter-kit.png"
---

This is not a blog post condensed into a PDF. This is a launch system for building an automation agency from zero to $10,000/month in recurring revenue. Every module contains exact procedures — not theories, not possibilities, not "consider doing X." You will do X, in this order, with these tools, and you will verify it worked before moving on.

**26 procedures. 8 modules. 5+ hours of reading and execution.** If you complete every procedure, you will have a functioning agency with paying clients. If you skip procedures, you will have a folder of half-finished projects and no revenue. The choice is yours.

---

# MODULE 1: FOUNDATION — YOUR AGENCY OPERATING SYSTEM

## Overview

Before you build a single automation, you need the infrastructure that runs your agency. This module sets up your project management, payments, email, and scheduling systems. These are not optional. Every successful agency operator has these systems in place before their first client call. Every failed operator skipped them.

**Time to complete:** 2-3 hours
**Tools needed:** Notion (free), Stripe (free), Google Workspace ($6/mo), Cal.com (free)

## Procedure 1.1: Create Your Agency Command Center in Notion

Open your browser and go to notion.so. Sign in or create a free account. You should see the Notion dashboard — a clean sidebar on the left and a main area with a "New page" button.

Do you see the dashboard? If you see a blank screen, clear your browser cache and reload. If you see a pricing page, close it — the free tier is sufficient for everything in this module.

Click **New page** in the left sidebar. Name it: `[Your Agency Name] Command Center`. This is the single source of truth for your entire business.

Inside this page, create five sub-pages by typing `/page` and naming each one:

1. **Clients** — Every client, their status, their deliverables, their revenue
2. **SOPs** — Standard Operating Procedures for every repeatable process
3. **Templates** — Client-facing documents, proposals, contracts, reports
4. **Finance** — Revenue tracking, expense tracking, margin analysis
5. **Pipeline** — Prospects, leads, and their position in your sales process

Do you see all five sub-pages listed inside your Command Center? If any are missing, add them now. You should have exactly five. Count them.

### The Clients Database

Open the **Clients** sub-page. Type `/table` and select **Table — Full page**. This creates a database. Name it `Client Roster`.

Add these columns (click the `+` button at the right end of the header row):

| Column Name | Type | Description |
|---|---|---|
| Client Name | Title | The business name |
| Status | Select: Active, Onboarding, Paused, Churned | Current relationship state |
| Tier | Select: Starter, Growth, Enterprise | Service tier |
| Monthly Revenue | Number | Retainer amount in dollars |
| Setup Fee | Number | One-time setup fee |
| Start Date | Date | When the engagement began |
| Next Delivery | Date | When the next deliverable is due |
| Health Score | Select: Green, Yellow, Red | Your subjective assessment of the relationship |

Add one row as a test: Client Name = "Test Client," Status = "Active," Tier = "Starter," Monthly Revenue = 1500, Setup Fee = 2000. Fill in the remaining fields with any values.

Do you see the test row in your table with all columns populated? If any columns are missing, add them. If the row has empty cells, fill them in. Incomplete data tracking is the number one cause of agency cash flow problems.

{{% accent-box %}}
**HACK:** Use Notion's "Template" button inside your Client Roster database to create a pre-filled template for new clients. Include default values for Status ("Onboarding"), Health Score ("Green"), and a checklist of onboarding tasks. This saves 10 minutes every time you sign a new client.
{{% /accent-box %}}

## Procedure 1.2: Set Up Your Financial Infrastructure

### Create Your Stripe Account

Go to stripe.com and create an account. Complete the business verification process (you will need a bank account and personal identification). This typically takes 1-2 business days for approval.

Once approved, you should see the Stripe dashboard with a "Test mode" toggle in the top-right corner. Do you see it? If your account is still pending verification, continue with the rest of this module and return to this step when approved.

### Create Your Payment Products

In Stripe, go to **Products** in the left sidebar. Click **Add product**. Create six products — three setup fees and three monthly retainers:

| Product Name | Price | Type |
|---|---|---|
| Starter Setup Fee | $2,000 | One time |
| Starter Monthly Retainer | $1,500/month | Recurring |
| Growth Setup Fee | $4,000 | One time |
| Growth Monthly Retainer | $3,000/month | Recurring |
| Enterprise Setup Fee | $6,000 | One time |
| Enterprise Monthly Retainer | $5,000/month | Recurring |

Create payment links for each product (click the product → **Create payment link**). Save these links in your Notion **Templates** page under a sub-page called "Payment Links."

Do you see all six products listed in your Stripe dashboard? Do all six have payment links? If any are missing, create them now. A missing payment link means a delayed payment, which means a delayed start, which means a frustrated client.

### Set Up Revenue Tracking

In your Notion **Finance** page, create a table called `Revenue Tracker` with these columns:

| Column Name | Type |
|---|---|
| Month | Title (e.g., "April 2026") |
| Total MRR | Number (Monthly Recurring Revenue) |
| Setup Fees | Number |
| Total Revenue | Formula: Total MRR + Setup Fees |
| Expenses | Number |
| Net Profit | Formula: Total Revenue - Expenses |
| Active Clients | Number |
| Average Revenue Per Client | Formula: Total MRR / Active Clients |

Add a row for the current month with zero values. This is your starting line.

## Procedure 1.3: Configure Your Communication Stack

### Create Your Business Email

If you do not have a professional email address on a custom domain, set one up now. Go to Google Workspace (workspace.google.com) and sign up for the Business Starter plan ($6/mo). Register a domain that matches your agency name (e.g., youragency.com) and create your email (e.g., hello@youragency.com or yourname@youragency.com).

Do not use a personal Gmail address for client communication. It signals amateur status. A custom domain email costs $6/month and instantly elevates your perceived professionalism.

### Create Your Client-Facing Calendar

Go to cal.com and create a free account. Set up a booking page with two meeting types:

1. **Discovery Call** — 30 minutes, available Monday through Friday, 9 AM to 5 PM your timezone
2. **Weekly Check-in** — 15 minutes, recurring, for active clients only

Connect your Google Calendar so bookings appear automatically. Copy your booking link and save it in your Notion **Templates** page.

## Module Check-In

- [ ] Notion Command Center created with all 5 sub-pages
- [ ] Client Roster database with all 8 columns and a test row
- [ ] Stripe account with 6 products and 6 payment links
- [ ] Revenue Tracker table in Notion with current month row
- [ ] Professional email address on custom domain
- [ ] Cal.com booking page with Discovery Call and Weekly Check-in

Count your checkmarks. Do you have all 6? If not, go back and complete the missing items. Do not proceed to Module 2 with an incomplete foundation.

---

# MODULE 2: TECH STACK — YOUR AUTOMATION ARSENAL

## Overview

Your agency runs on tools. This module sets up every tool you need, connects them, and verifies each connection. The total cost is under $100/month to start — and most of it is free until you have paying clients.

**Time to complete:** 2 hours
**Total monthly cost (startup):** $26–$86 depending on your choices

## Procedure 2.1: Set Up Your Core Automation Platform

### Create Your Make.com Account

Go to make.com and sign up for the Free plan. You get 1,000 operations per month — enough to build and test your first 3-5 workflows.

After signing in, you should see the Make.com dashboard with a "Create a new scenario" button in the center. Do you see it? If you see a different interface, click "Scenarios" in the left sidebar.

### Connect Your Core Services

In Make.com, click your profile icon (top-right) → **Connections** → **Add connection**. Connect the following services:

1. **Google Sheets** — Authorize with your Google account
2. **Gmail** — Authorize with your professional email
3. **Slack** — Authorize with your Slack workspace (create one at slack.com if needed)
4. **OpenAI** — Enter your API key from platform.openai.com/api-keys
5. **Notion** — Authorize with your Notion account

After connecting each service, you should see a green "Connected" status next to it. Do you see green for all 5? If any show red or yellow:
- Google/Gmail/Slack/Notion: Re-authorize and make sure you approve all permissions
- OpenAI: Verify your API key starts with `sk-` and your account has at least $5 credit

## Procedure 2.2: Set Up Your AI Model Access

### OpenAI API Configuration

Go to platform.openai.com. Navigate to **API Keys** and create a new key. Copy it immediately — you cannot view it again. Store it in a password manager (1Password, Bitwarden, or the Mac Keychain). Do not store API keys in Notion pages that you share with anyone.

Navigate to **Billing** and add $20 in credit. This funds your API usage for approximately 500-1,000 workflow executions.

Navigate to **Usage limits** and set a monthly limit of $50. This prevents a buggy workflow from draining your credit overnight. You can increase this limit as your agency grows.

{{% accent-box %}}
**HACK:** Set up two separate OpenAI API keys — one for production automations and one for testing. When a test workflow goes haywire, it burns through the testing key's credit, not your production budget. Create the keys at platform.openai.com/api-keys and label them "prod" and "dev."
{{% /accent-box %}}

## Procedure 2.3: Set Up Your Client Delivery Tools

### Slack Workspace Configuration

Go to slack.com and create a workspace if you have not already. Create these channels:

- `#automation-errors` — All error notifications from Make.com go here
- `#hot-leads` — Hot lead alerts from client automations
- `#new-clients` — Notifications when a new client signs

Do you see all the channels in your Slack sidebar? The `#automation-errors` channel is the most important — it is your early warning system for broken automations.

### Loom for Client Communication

Go to loom.com and create a free account. Install the Loom browser extension (Chrome or Firefox). You will use Loom to record walkthrough videos for clients — showing them how to use their automations, explaining reports, and answering questions. A 3-minute Loom video replaces a 30-minute call and can be rewatched indefinitely.

Record a test video: open Loom, click record, say "This is a test video for my agency setup," and stop. Watch the playback. Does the audio sound clear? If it sounds echoey or quiet, adjust your microphone settings. Clear audio is non-negotiable — clients will not watch videos they cannot hear.

### Tally for Lead Capture Forms

Go to tally.so and create a free account. Create a simple test form with fields: Name, Email, Phone, Message. You will use this form in Module 4. Publish the form and copy the URL.

Do you see the published form URL? Save it in your Notion Templates page under "Demo Forms."

## Procedure 2.4: Complete Tool Cost Summary

| Tool | Purpose | Free Tier | Paid Tier | When to Upgrade |
|---|---|---|---|---|
| Make.com | Workflow automation | 1,000 ops/mo | $9/mo (10K ops) | At first paying client |
| OpenAI API | AI in automations | Pay per use | ~$20-50/mo | At first automation |
| Slack | Team communication | Free | $8/user/mo | At 3+ team members |
| Notion | Project management | Free | $10/mo | At 5+ team members |
| Google Workspace | Email + docs | — | $6/mo | Immediately |
| Stripe | Payment processing | Free | 2.9% + 30c/tx | Always |
| Loom | Video communication | Free (25 videos) | $13/mo | When free tier limits are hit |
| Tally | Form builder | Free | $29/mo | When you need advanced logic |
| Cal.com | Scheduling | Free | $12/mo | When you need team scheduling |

**Startup cost: $6/mo (Google Workspace only). Everything else is free until you have revenue.**

## Module Check-In

- [ ] Make.com account with 5 connected services (all green)
- [ ] OpenAI API key with $20+ credit and $50 monthly limit
- [ ] Slack workspace with #automation-errors, #hot-leads, #new-clients channels
- [ ] Loom account with test video recorded and clear audio
- [ ] Tally account with a published test form
- [ ] All tool costs documented in Notion Finance page

6 checkmarks required to proceed. Do you have all 6?

---

# MODULE 3: THE BUILD FRAMEWORK — HOW TO BUILD ANY AUTOMATION

## Overview

This module teaches you the universal framework for building automations. Every automation you ever build — for yourself or for clients — follows this exact five-phase process. Memorize it. Internalize it. When you can execute this framework without referring to this playbook, you are ready to build for clients.

**Time to complete:** 1-2 hours (study) + 2-8 hours (practice in Module 4)

## Procedure 3.1: The Five-Phase Build Process

Every automation has five phases: Discovery, Design, Build, Test, Deploy. You will learn each one now and practice on a real build in Module 4.

### Phase 1: Discovery (1-2 hours)

Before you touch any software, you must understand the problem. Schedule a 30-minute call with the stakeholder (your client, or yourself for internal projects). Ask these questions in this exact order:

1. "What is the manual process you want to automate? Walk me through every step."
2. "How often does this process run? Daily? Weekly? On demand?"
3. "What triggers the process? A form submission? A time of day? A human decision?"
4. "What is the final output? An email? A spreadsheet row? A notification? A document?"
5. "What are the edge cases? What happens when [thing goes wrong]?"
6. "Who needs to be notified and when?"
7. "What tools are currently involved? What tools do you wish were involved?"
8. "What does success look like? How will you measure whether this automation is working?"

Write the answers in a Google Doc. This document becomes the specification for your build.

### Phase 2: Design (1-2 hours)

Open a blank page in Notion (or draw on paper). Map the automation as a flowchart:

```
[TRIGGER] → [STEP 1] → [STEP 2] → [ROUTER] → [PATH A] → [OUTPUT 1]
                                       ↓
                                   [PATH B] → [OUTPUT 2]
                                       ↓
                                   [PATH C] → [OUTPUT 3]
```

For each step, write:
- **What it does** (one sentence)
- **What tool/module** you will use
- **What data it needs** as input
- **What data it produces** as output
- **What happens if it fails** (error handling)

This design document becomes your build plan. Do not start building without one. A build without a design is a build that takes 3x longer and breaks in production.

### Phase 3: Build (2-8 hours)

Open Make.com. Create a new scenario. Build the automation following your design document, step by step. For each module:

1. Add the module
2. Configure the connection
3. Map the input data from the previous module
4. Configure the output format
5. Test the module in isolation (right-click → **Run this module only**)
6. Verify the output matches your design document

After all modules are connected, test the full scenario using "Run once." Check the output at every module by clicking the bubble above it. Do you see the data flowing correctly through each step?

If a module shows an error (red bubble), read the error message. 90% of errors are caused by:
- **Missing variable mapping** — you forgot to map an input field
- **Wrong data type** — you are passing text where a number is expected
- **Expired connection** — re-authorize the service connection
- **API rate limit** — wait 60 seconds and retry

### Phase 4: Test (2-4 hours)

Testing is not optional. Testing is not "run it once and hope." Testing is a systematic process.

**The 10-Test Protocol:**
1. Run with normal input data (3 times)
2. Run with empty fields (does it handle missing data gracefully?)
3. Run with special characters in text fields (quotes, ampersands, unicode)
4. Run with extremely long text inputs (does it truncate or break?)
5. Run with the trigger firing twice in rapid succession (race condition test)
6. Run with one downstream service offline (does the error handler catch it?)
7. Run with data that should route to Path A — verify it goes to Path A
8. Run with data that should route to Path B — verify it goes to Path B
9. Run with data that should route to Path C — verify it goes to Path C
10. Run with invalid input (wrong email format, missing required field)

Document every test result in a Google Sheet called "[Automation Name] Test Results" with columns: Test #, Input, Expected Output, Actual Output, Pass/Fail, Notes.

Do all 10 tests pass? If any fail, fix the automation and re-run the failed tests. Do not proceed to Phase 5 until all 10 tests pass.

### Phase 5: Deploy (1-2 hours)

Activate the scenario (toggle the ON/OFF switch in Make.com). Set the schedule. Configure monitoring:

1. Add a **Break** error handler to every API module
2. After each Break, add a **Slack notification** that sends the error details to your `#automation-errors` channel
3. Enable **Automatic retry** (3 retries, 10-second interval) on every API module
4. For the first 48 hours, check the execution log every 4 hours (click the scenario → **History** tab)

Do you see successful executions in the History tab? If you see any errors, investigate and fix before telling the client the automation is live.

## Procedure 3.2: Document Your Build

After deploying, create an SOP in your Notion SOPs page for this specific automation. The SOP must include:

1. **Automation name and purpose** (2-3 sentences)
2. **Trigger description** (what starts it, how often)
3. **Complete module-by-module walkthrough** (description of each module's configuration)
4. **Data flow diagram** (which module passes what data to which module)
5. **Error handling documentation** (what errors can occur, how they are handled)
6. **Client-specific notes** (any quirks or customizations)
7. **Update log** (date, what changed, why)

This SOP serves three purposes: (1) you can rebuild the automation if Make.com loses it, (2) a junior builder can maintain it while you focus on sales, (3) it is a deliverable the client receives as part of their engagement.

{{% accent-box %}}
**HACK:** After writing the SOP, paste it into ChatGPT with the prompt: "Review this SOP for an automation agency. Identify any steps that are unclear, any missing error-handling scenarios, and any variables that might break if the input data changes format." This 60-second review catches 80% of documentation gaps before they become production problems.
{{% /accent-box %}}

## Module Check-In

- [ ] You can recite the Five-Phase Build Process from memory
- [ ] You have a blank SOP template in Notion ready for your first build
- [ ] You have a Test Results spreadsheet template ready
- [ ] You understand the four most common Make.com errors and how to fix them
- [ ] You have a `#automation-errors` Slack channel set up

5 checkmarks. Do you have all 5?

---

# MODULE 4: FIRST BUILD — LEAD CAPTURE PIPELINE

## Overview

This module walks you through building a complete, production-ready lead capture automation. After completing it, you will have a portfolio piece and a repeatable service you can sell immediately.

**Client scenario:** A local business receives leads through a web form. Currently, someone manually copies each lead into a spreadsheet and follows up by phone. Half the leads never get called. Staff is overwhelmed. You will automate the entire pipeline.

**Deliverable:** Web form → AI enrichment → Lead scoring → Routing → Notification → Logging

## Procedure 4.1: Complete the Discovery Phase

Open a new Google Doc. Title it "Lead Capture Pipeline — Discovery Notes." Write this specification (this is what you would extract from a real client call):

**Trigger:** New lead submits a form on the business website
**Current process:** Staff manually enters leads into a spreadsheet, then calls each one within 24 hours. Half the leads never get called.
**Desired output:** Instant Slack notification with enriched lead data. Automatic logging in Google Sheets. Hot leads flagged for immediate callback.
**Edge cases:** Spam form submissions. After-hours submissions. Duplicate submissions.
**Tools involved:** Website form (Tally), Google Sheets, Slack, OpenAI for enrichment
**Success metric:** 100% of leads logged, hot leads receive a Slack alert within 60 seconds

Read through this specification twice. Do you understand every requirement? If anything is unclear, re-read it.

## Procedure 4.2: Design the Automation

Create a flowchart in Notion:

```
[Tally Form Submission]
    → [Spam Filter: email contains "test" or ".xyz"?]
        → YES: [Sheets: Log Spam] → STOP
        → NO: [OpenAI: Enrich & Score]
            → [Parse JSON Response]
                → [Router: Score ≥ 8?]
                    → YES: [Slack: Hot Lead Alert] + [Sheets: Log Hot Lead]
                    → NO: [Router: Score 4-7?]
                        → YES: [Sheets: Log Warm Lead]
                        → NO: [Sheets: Log Cold Lead]
```

Does your design match this flow? The design above covers every requirement: spam filtering, AI enrichment, scoring, and three-tier routing.

## Procedure 4.3: Build the Automation in Make.com

### Step A: Create the Trigger

Create a new scenario in Make.com. Name it "Lead Capture Pipeline."

Add a **Webhook** module as the trigger. Select "Custom webhook." Click **Create a webhook** and copy the URL.

Go to tally.so and open the test form you created in Module 2. Add fields: Name, Email, Phone, Service Interest (dropdown with 5 options relevant to your target market), and a Message field.

In Tally, go to **Integrations** → **Webhooks** → paste your Make.com webhook URL. Submit a test response on the form. Come back to Make.com — the Webhook module should now show the test data structure.

Do you see the test data in Make.com? You should see fields like `name`, `email`, `phone`, `service_interest`, and `message`. If you see empty data, go back to Tally and verify the webhook URL is correct.

### Step B: Add Spam Filtering

Add a **Router** module after the Webhook. On Path 1 (the clean path), add a filter:
- Condition: `email` does NOT contain "test" AND `email` does NOT contain ".xyz"

On Path 2 (the spam path), add a **Google Sheets — Add a Row** module that logs the spam submission and then stops.

Test: Submit a form with email "test@test.com." Verify it goes to the spam path. Then submit a real form. Verify it goes to Path 1.

Do both tests pass? If the real submission goes to the spam path, your filter conditions are too aggressive.

### Step C: Add AI Enrichment and Scoring

After the Router's clean path, add an **OpenAI — Create a Chat Completion** module:

- Model: `gpt-4o`
- System message: "You are a lead qualification assistant. Given a lead's information, score them from 1-10 and identify their primary need. Respond ONLY in this JSON format: {\"score\": 8, \"primary_need\": \"description\", \"is_new_customer\": true, \"urgency\": \"high\", \"suggested_action\": \"Call within 1 hour\"}"
- User message: Map the lead's name, email, phone, service interest, and message

Add a **Parse JSON** module after OpenAI to convert the text response into structured variables.

Test: Submit a real-looking form. Check the Parse JSON output. Do you see `score`, `primary_need`, `is_new_customer`, `urgency`, and `suggested_action` as separate variables? If the Parse JSON module shows an error, add "Respond ONLY in valid JSON, no markdown formatting" to the system prompt and test again.

### Step D: Add Routing and Notifications

Add another **Router** after Parse JSON.

**Path 1: Hot Lead (Score ≥ 8)**
Filter: `score` ≥ 8
Module: **Slack — Create a Message**
Channel: `#hot-leads`
Message:

```
🔴 HOT LEAD — Score: {{score}}/10
Name: {{name}}
Email: {{email}}
Phone: {{phone}}
Service Interest: {{service_interest}}
Primary Need: {{primary_need}}
Urgency: {{urgency}}
Suggested Action: {{suggested_action}}
```

Also add a **Google Sheets — Add a Row** module logging to a "Hot Leads" sheet.

**Path 2: Warm Lead (Score 4-7)**
Filter: `score` between 4 and 7
Module: **Google Sheets — Add a Row** logging to a "Warm Leads" sheet

**Path 3: Cold Lead (Score 1-3)**
Filter: `score` ≤ 3
Module: **Google Sheets — Add a Row** logging to a "Cold Leads" sheet

### Step E: Add Error Handling

Add a **Break** error handler to the OpenAI module. After the Break, add a **Slack — Create a Message** to `#automation-errors`:

```
⚠️ Lead enrichment failed for {{name}} ({{email}})
Error: {{error.message}}
Manual action required: Enrich this lead and add to the appropriate sheet.
```

Enable **Automatic retry** (3 retries, 10-second interval) on the OpenAI module.

## Procedure 4.4: Run the 10-Test Protocol

Create a Google Sheet called "Lead Capture Test Results." Run all 10 tests from Procedure 3.1. Document each result. Do all tests pass? If any fail, fix and re-test until all pass.

## Procedure 4.5: Deploy and Document

Activate the scenario. Set the schedule to "Immediately" (webhook-triggered scenarios run in real time). Create the SOP in your Notion SOPs page. Include all 7 sections from Procedure 3.2.

{{% accent-box %}}
**HACK:** Record a 3-minute Loom video walking through the working automation. Show the form submission, the data flowing through Make.com, and the Slack notification arriving. This video becomes your most powerful sales asset — prospects see a real system working in real time, not a mockup or a slide deck.
{{% /accent-box %}}

## Module Check-In

- [ ] Lead capture automation built and tested in Make.com
- [ ] Spam filtering works (tested with spam and non-spam submissions)
- [ ] AI enrichment produces valid JSON with score, need, urgency, and action
- [ ] Router correctly separates hot/warm/cold leads
- [ ] Error handling notifies Slack when OpenAI fails
- [ ] All 10 test cases pass
- [ ] SOP documented in Notion with all 7 sections
- [ ] Loom walkthrough video recorded

8 checkmarks. Every single one must be checked before proceeding.

---

# MODULE 5: CLIENT ACQUISITION — THE MACHINE THAT FEEDS THE MACHINE

## Overview

You can build automations. Now you need clients who will pay you to build them. This module gives you the exact scripts, templates, and processes for acquiring clients consistently. No guessing. No hoping. Follow the procedures and clients will appear.

**Time to complete:** 6-8 hours (mostly prospect research and email sending)

## Procedure 5.1: Define Your Target Market

Pick one business category. Not five. Not three. One. The best categories for starting automation agencies:

- Dental practices
- Real estate agencies
- Law firms
- E-commerce stores (Shopify)
- Gyms and fitness studios
- Insurance agencies
- Accounting firms
- Marketing agencies (yes, agencies hire other agencies)

Write your chosen category on a sticky note. Put it on your monitor. Do not change it for 90 days. Niche focus is the single biggest advantage a new agency has — you learn the specific pain points, build reusable templates, and can speak their language from day one.

{{% accent-box %}}
**HACK:** The fastest path to your first client is the category where you already have domain knowledge. Former dental assistant? Target dental practices. Ran an Etsy shop? Target e-commerce. Personal experience gives you instant credibility that no script can replicate.
{{% /accent-box %}}

## Procedure 5.2: Build Your 50-Prospect List

Open Google Maps. Search for "[your category] in [your city/region]." You should see a list of businesses with names, addresses, phone numbers, and websites.

Create a Google Sheet called "Prospect List" with columns: Business Name, Website, Contact Email, Contact Name, Automation Opportunity, Email Sent Date, Reply (Y/N), Meeting Booked (Y/N), Outcome.

Open each website and check:
1. Do they have a contact form? (Automation opportunity: lead capture)
2. Do they have a chatbot? (If no, automation opportunity)
3. Do they post consistently on social media? (If no, automation opportunity)
4. Does their site look modern? (If no, they probably do not have automation)

Find 50 businesses. Yes, 50. This takes 3-4 hours. Do it in one sitting. Do not stop at 20.

Do you have 50 rows in your Prospect List? If you have fewer, go back to Google Maps and find more. 50 is the minimum for statistical significance in outreach.

## Procedure 5.3: Cold Outreach Script

Here is the script. Do not modify it until you have sent 50 emails and tracked the results:

**Subject line:** Quick question about [their business name]

**Body:**

> Hi [First Name],
>
> I noticed [specific observation about their business — e.g., "you don't have a chatbot on your site" or "your contact form goes to a generic email"].
>
> I build automations for [category] businesses that handle the repetitive stuff — lead capture, follow-ups, scheduling, reporting — so your team can focus on the work that actually requires a human.
>
> I put together a live demo built specifically for [category] practices. It shows how an automated lead pipeline works in real time: [link to your lead capture demo]
>
> Would it be worth a 15-minute chat to see if this could work for [their business name]?
>
> [Your Name]

Send this email to all 50 prospects. Use your professional email address. Send no more than 10 per day (to avoid spam filters). Space them throughout the day: 9 AM, 11 AM, 1 PM, 3 PM, 5 PM — two emails at each time slot.

**Expected results:** 8-12 replies (16-24% reply rate). 3-5 meetings booked. 1-2 clients closed.

If your reply rate is below 10% after 50 emails, the problem is one of three things:
1. Your subject line is landing in spam (check with mail-tester.com)
2. Your observation is not specific enough (generic observations = generic replies)
3. Your target market does not see the value (try a different category)

## Procedure 5.4: The Demo Call Script

When a prospect books a discovery call, follow this script:

**Minutes 0-5:** Introduce yourself briefly. Ask: "Before I show you anything, tell me — what's the most annoying manual process in your business right now?" Listen. Take notes.

**Minutes 5-15:** Show your live demo. Do not use slides. Open the actual working automation in Make.com. Show the Slack notification arriving in real time when a form is submitted. Show the AI enrichment. Show the lead scoring. The prospect should see a real system working in real time, not a mockup.

**Minutes 15-25:** Ask: "How would this work for [their business]?" Let them imagine their own business running on this system. Ask follow-up questions: "Where would you want the notifications to go?" "What information would you want AI to enrich?" This makes them mentally own the solution before they have bought it.

**Minutes 25-30:** Present pricing. Use this exact framing: "Our Starter package is $2,000 setup plus $1,500/month. That includes one core automation — like the lead pipeline you just saw — plus monthly maintenance and optimization. Most clients see ROI within the first 30 days because the automation saves 10-20 hours of manual work per week."

If they say yes, send the Stripe payment link immediately (from your Notion Templates page). If they say "let me think about it," say: "Totally understand. I'll send you a summary email with the demo link so you can share it with your team. What's the best way to follow up with you next week?"

## Module Check-In

- [ ] Target market chosen (one category, written on a sticky note)
- [ ] 50 prospects in your Prospect List spreadsheet
- [ ] Cold outreach script saved in Notion Templates
- [ ] First batch of 10 outreach emails sent
- [ ] Demo call script memorized or printed and on your desk

5 checkmarks. The outreach emails are the hardest part — most people overthink and under-send. Send the emails.

---

# MODULE 6: CLIENT DELIVERY — THE SYSTEM THAT KEEPS THEM PAYING

## Overview

Landing a client is 20% of the work. Delivering value month after month is 80%. This module gives you the exact delivery framework that keeps clients for 12+ months (instead of the industry average of 3-4 months).

**Time to complete:** Ongoing (4-5 hours per client per month after initial setup)

## Procedure 6.1: The First-Week Onboarding Protocol

**Day 1:** Send the welcome email. Schedule the kickoff call via your Cal.com link. Create a Google Drive folder for the client using this structure:

```
[Client Name]/
├── Discovery/
├── Assets/
├── Deliverables/
└── Reports/
```

**Day 2: Kickoff Call (30 minutes)**
- Confirm the scope of work (which automation(s) you are building)
- Collect access credentials (website CMS, email platforms, CRM, social accounts)
- Ask the 8 discovery questions from Procedure 3.1
- Set expectations: "You will receive the first working automation within 5 business days"

**Days 3-5:** Build the automation following the Five-Phase Build Process. Use the client's real data and real tools.

**Day 6:** Internal testing. Run the 10-Test Protocol. Fix every failure.

**Day 7:** Client walkthrough via Loom video. Record yourself explaining the automation, showing it working, and explaining what to do if something breaks. Send the video and the SOP document to the client.

Do you have a completed Loom walkthrough? This video is your safety net — it answers the client's questions before they ask them, reduces "how does this work?" emails by 80%, and proves you delivered even if the client claims otherwise.

## Procedure 6.2: The Monthly Delivery Calendar

Every client receives these touchpoints every month:

| Week | Deliverable | Time Investment |
|---|---|---|
| Week 1 | Monthly optimization review — check execution logs, fix errors, update prompts | 1 hour |
| Week 2 | New feature or enhancement — add one small improvement to an existing automation | 1-2 hours |
| Week 3 | Performance report — generate and send the monthly summary | 30 minutes |
| Week 4 | Check-in call (15 minutes) — review performance, discuss needs, identify upsell opportunities | 15 minutes |

Total monthly time per Starter client: ~4 hours. At $1,500/month, that is $375/hour effective rate. This is why automation agencies are so profitable.

{{% accent-box %}}
**HACK:** Automate your own delivery calendar. Build a Make.com scenario that runs every Monday at 8 AM and sends you a Slack message listing: which clients need optimization reviews this week, which clients have upcoming check-in calls, and which clients have not been contacted in 14+ days. This prevents the "I forgot about Client X" problem that causes churn.
{{% /accent-box %}}

## Procedure 6.3: The Churn Prevention System

Client churn follows predictable patterns. Here are the four warning signs and how to address each one:

**Warning Sign 1: Client stops responding to emails**
Action: Send a Loom video showing a new feature or optimization you added proactively. This reminds them of the value without requiring a response.

**Warning Sign 2: Client asks "Are we still using this?"**
Action: Immediately send a performance report showing exactly what the automation has done in the last 30 days (leads captured, emails sent, hours saved). Quantify the value. A client who asks this question has not seen your work recently — that is your failure, not theirs.

**Warning Sign 3: Client asks for a discount**
Action: Do not discount. Instead, offer to reduce scope: "We can move to a lighter package at $1,000/month that covers maintenance only, with no new features or optimization. Would that work better for you?" Most clients will stay at the current tier rather than lose features.

**Warning Sign 4: Client's business is struggling**
Action: Offer to build one additional automation at no extra cost for one month. This creates goodwill and often leads to an upgrade when their business recovers.

Log all churn warning signs in the Client Roster. Set the Health Score to Yellow or Red. Review weekly.

## Module Check-In

- [ ] First-week onboarding protocol documented as an SOP
- [ ] Monthly delivery calendar created for your first client
- [ ] Churn prevention system documented with all 4 warning signs and responses
- [ ] You have sent at least one proactive Loom video to a client or test account

4 checkmarks. The Loom video is the most important one — proactive communication is the single strongest predictor of client retention.

---

# MODULE 7: PRICING & PROPOSALS — CHARGE WHAT YOU ARE WORTH

## Overview

Most new agency operators undercharge. This module gives you the exact pricing tiers, proposal template, and contract essentials so you never again wonder "how much should I charge for this?" The prices in this module are floor prices — increase them by 20% after every 5th client.

**Time to complete:** 1-2 hours (initial setup)

## Procedure 7.1: The Three Pricing Tiers

Present three tiers to every prospect. The middle tier should feel like the obvious choice — this is called the anchoring effect. Price the lowest tier so it barely covers your costs, and the highest tier so it feels like a premium upgrade.

| Tier | Setup Fee | Monthly Retainer | What's Included | Your Time/Month |
|---|---|---|---|---|
| **Starter** | $2,000 | $1,500/mo | 1 core automation + maintenance + monthly report | ~4 hours |
| **Growth** | $4,000 | $3,000/mo | 2 core automations + maintenance + monthly report + weekly check-in | ~6 hours |
| **Enterprise** | $6,000 | $5,000/mo | 3+ automations + priority support + quarterly strategy session + dedicated Slack channel | ~8 hours |

**Effective hourly rates:** Starter = $375/hr | Growth = $500/hr | Enterprise = $625/hr

These rates are achievable because automation delivers measurable ROI. A $1,500/month automation that saves 15 hours of manual labor at $30/hour saves the client $450/month in direct labor. Factor in faster lead response (which increases conversion by 20-40%) and the client's ROI is 2-5x your fee.

{{% accent-box %}}
**HACK:** Always present the Growth tier first. Say: "Most of our clients start with the Growth tier at $3,000/month — it gives you two automations, which is usually enough to cover your biggest pain points." If they flinch at the number, the Starter tier feels like a relief. If they do not flinch, the Enterprise tier is the natural upsell. Never present the cheapest option first.
{{% /accent-box %}}

## Procedure 7.2: The Proposal Template

Create this proposal in your Notion **Templates** page. Copy and customize it for each prospect.

### Proposal Structure

**Section 1: Executive Summary** (3-4 sentences)
"[Agency Name] will design, build, and maintain custom automations for [Client Name]. Our approach eliminates manual workflows in [specific area identified on demo call], saving your team an estimated [X] hours per week. We propose a [Tier Name] engagement starting on [date]."

**Section 2: Scope of Work**
List each automation you will build. For each one, include:
- Name (e.g., "Lead Capture Pipeline")
- Current manual process (2-3 sentences)
- Automated process (2-3 sentences)
- Estimated hours saved per week

**Section 3: Investment**

| Item | Cost |
|---|---|
| Setup Fee (one-time) | $[amount] |
| Monthly Retainer | $[amount]/month |
| Billing cycle | Monthly, starting on delivery date |
| Payment method | Stripe payment link (embedded in proposal email) |

**Section 4: Timeline**

| Milestone | Target Date |
|---|---|
| Kickoff call | Within 3 business days of signing |
| First automation live | Within 7 business days of kickoff |
| Second automation live (Growth/Enterprise) | Within 14 business days of kickoff |
| Monthly optimization begins | First full month after deployment |

**Section 5: Terms**
- 30-day cancellation notice (either party)
- All automations remain active during notice period
- Client retains access to all logged data after cancellation
- Automation configurations are proprietary to [Agency Name]; client receives a perpetual license to use them

Save this template. Use it for every proposal. Do not customize the structure — only the specific details. Consistency speeds up your sales cycle.

## Procedure 7.3: The Pricing Increase Schedule

After every 5th client, increase all prices by 20%. Here is the schedule:

| Clients Signed | Starter Monthly | Growth Monthly | Enterprise Monthly |
|---|---|---|---|
| 1-5 | $1,500 | $3,000 | $5,000 |
| 6-10 | $1,800 | $3,600 | $6,000 |
| 11-15 | $2,160 | $4,320 | $7,200 |
| 16-20 | $2,592 | $5,184 | $8,640 |

Your early clients get the best price. They also get your most attentive service because you have fewer clients. This is a feature, not a bug — it keeps your first clients loyal and generates referrals. When you raise prices, your existing clients stay at their original rate (grandfathered). New clients pay the new rate.

## Module Check-In

- [ ] Three pricing tiers documented in Notion and Stripe
- [ ] Proposal template saved in Notion Templates page
- [ ] Pricing increase schedule documented
- [ ] You understand the anchoring effect and present Growth tier first

4 checkmarks. The proposal template is the most important one — a consistent proposal closes deals faster because the client sees professionalism, not improvisation.

---

# MODULE 8: SCALING — FROM SOLO TO AGENCY

## Overview

Solo operators hit a ceiling at ~6-8 clients (~$10-15K/month). Breaking through requires systems and people. This module shows you exactly how and when to hire, what to delegate, and how to maintain margins as you grow.

## Procedure 8.1: The Hiring Roadmap

**When you have 5 clients:** Hire a Virtual Assistant (VA) on Upwork. Budget: $5-8/hour, 10-15 hours/week. The VA handles:
- Client communication (responding to emails, scheduling calls)
- Data entry (updating Client Roster, logging test results)
- Basic QC (running test protocols, reporting failures to you)
- Social media posting (scheduling content in Buffer or Hootsuite)

**When you have 10 clients:** Hire a Junior Builder. Budget: $15-25/hour, 20-30 hours/week. The Junior Builder handles:
- Building new automations from your SOPs
- Running the 10-Test Protocol
- Client onboarding (following your onboarding SOP)
- Monthly maintenance and optimization

**When you have 15 clients:** Hire a Salesperson. Budget: $40-60K base + 10% commission on first-year client revenue. The Salesperson handles:
- Prospecting (building the 50-business list from Procedure 5.2)
- Cold outreach (sending the script from Procedure 5.3)
- Demo calls (following the script from Procedure 5.4)
- Pipeline management

**When you have 20+ clients:** Hire a Senior Builder. Budget: $30-40/hour, full-time. This person handles complex integrations, custom API work, and issues the Junior Builder cannot resolve.

{{% accent-box %}}
**HACK:** Before hiring anyone, write the SOP for their role first. If you cannot document the process, you cannot delegate it. The act of writing the SOP reveals whether you actually have a repeatable system or just a habit. If it is a habit, systematize it before hiring — otherwise you will spend all your time training and none of your time selling.
{{% /accent-box %}}

## Procedure 8.2: Margin Analysis at Scale

| Clients | Revenue/mo | Team Cost/mo | Tool Cost/mo | Net Profit/mo | Margin |
|---|---|---|---|---|---|
| 5 | $7,500 | $600 (VA) | $200 | $6,700 | 89% |
| 10 | $15,000 | $2,800 (VA + Junior) | $300 | $11,900 | 79% |
| 15 | $22,500 | $5,800 (VA + Junior + Sales) | $400 | $16,300 | 72% |
| 20 | $30,000 | $10,500 (VA + 2 Builders + Sales) | $500 | $19,000 | 63% |
| 30 | $45,000 | $16,000 (Full team) | $700 | $28,300 | 63% |

Margins compress as you hire, but absolute profit increases. A 63% margin on $45,000 is $28,300/month — far more than a solo operator earning 89% on $7,500 ($6,675/month).

The key insight: do not optimize for margin percentage. Optimize for profit dollars. A 63% margin on $45K beats an 89% margin on $7.5K every time.

{{% accent-box %}}
**HACK:** Track your effective hourly rate weekly. Divide your monthly profit by the total hours you worked that month. If your effective rate drops below $200/hour, you are doing tasks that should be delegated. Every hour you spend on a $20/hour task is an hour you are not spending on a $500/hour task (selling, building, or strategizing).
{{% /accent-box %}}

## Module Check-In

- [ ] Hiring roadmap is saved in Notion with trigger points for each hire
- [ ] You understand margin compression and why it is acceptable
- [ ] You have written at least one SOP for a future hire's role
- [ ] Your Revenue Tracker is updated and reflects current month actuals

4 checkmarks. The SOP is the most important one — it proves you are building systems, not just doing work.

---

# APPENDIX A: TOOL REFERENCE

Every tool mentioned in this playbook, with direct links and current pricing as of April 2026.

| Tool | URL | Free Tier | Paid Start | Purpose |
|---|---|---|---|---|
| Make.com | make.com | 1,000 ops/mo | $9/mo | Workflow automation engine |
| OpenAI API | platform.openai.com | Pay per use | ~$20/mo | AI for enrichment, scoring, writing |
| Anthropic Claude | console.anthropic.com | Pay per use | ~$10/mo | AI for long-form content |
| Notion | notion.so | Free | $10/mo | Command center, databases, SOPs |
| Google Workspace | workspace.google.com | — | $6/mo | Email, docs, drive |
| Stripe | stripe.com | Free | 2.9%+$0.30/tx | Payment processing |
| Slack | slack.com | Free | $8/user/mo | Team + client communication |
| Loom | loom.com | 25 videos | $13/mo | Walkthrough videos |
| Tally | tally.so | Free | $29/mo | Form builder for lead capture |
| Cal.com | cal.com | Free | $12/mo | Scheduling and booking |
| Upwork | upwork.com | Free | 5-10% fee | Hiring contractors |

**Rule:** Never pay for a tool until the free tier actively limits your ability to deliver. Every dollar of unnecessary SaaS spend is a dollar not going toward your profit.

---

# APPENDIX B: SOP INDEX

A complete list of every Standard Operating Procedure you should have in your Notion SOPs database by the time you complete this playbook.

| SOP # | Name | Category | Difficulty | Est. Time | When Created |
|---|---|---|---|---|---|
| SOP-001 | New Client Onboarding | Deliver | Junior | 2 hours | Module 6 |
| SOP-002 | Lead Capture Pipeline Build | Build | Senior | 8 hours | Module 4 |
| SOP-003 | Five-Phase Build Process | Build | Expert | Varies | Module 3 |
| SOP-004 | 10-Test Protocol | Build | Junior | 2 hours | Module 3 |
| SOP-005 | Monthly Optimization Review | Deliver | Junior | 1 hour | Module 6 |
| SOP-006 | Monthly Performance Report | Deliver | Junior | 30 min | Module 6 |
| SOP-007 | Client Check-in Call | Deliver | Senior | 15 min | Module 6 |
| SOP-008 | Cold Outreach (50-Prospect Method) | Sales | Junior | 4 hours | Module 5 |
| SOP-009 | Demo Call Script | Sales | Senior | 30 min | Module 5 |
| SOP-010 | Proposal Creation | Sales | Senior | 1 hour | Module 7 |
| SOP-011 | Churn Prevention Protocol | Operations | Senior | 30 min | Module 6 |
| SOP-012 | New Client Folder Setup | Operations | Junior | 15 min | Module 6 |
| SOP-013 | Loom Walkthrough Recording | Deliver | Junior | 15 min | Module 4 |
| SOP-014 | Make.com Error Handler Setup | Build | Senior | 30 min | Module 3 |
| SOP-015 | Stripe Product + Payment Link Creation | Finance | Junior | 15 min | Module 1 |

Each SOP should follow the 7-section format from Procedure 3.2. If an SOP has fewer than 7 sections, it is incomplete. Fix it before using it to train anyone.

---

# APPENDIX C: REVENUE CALCULATOR

Use this table to project your agency revenue based on the number and mix of clients you acquire. These calculations assume the base pricing tiers (before price increases).

## Single-Tier Revenue Projections

| Clients | Starter Only | Growth Only | Enterprise Only |
|---|---|---|---|
| 1 | $1,500/mo | $3,000/mo | $5,000/mo |
| 3 | $4,500/mo | $9,000/mo | $15,000/mo |
| 5 | $7,500/mo | $15,000/mo | $25,000/mo |
| 8 | $12,000/mo | $24,000/mo | $40,000/mo |
| 10 | $15,000/mo | $30,000/mo | $50,000/mo |

## Realistic Mixed-Tier Scenario

Most agencies have a mix of tiers. Here is a realistic progression:

| Milestone | Client Mix | Monthly MRR | Setup Fees | Total First-Year Revenue |
|---|---|---|---|---|
| Month 3 | 2 Starter | $3,000 | $4,000 | $40,000 |
| Month 6 | 2 Starter + 2 Growth | $9,000 | $12,000 | $120,000 |
| Month 9 | 2 Starter + 3 Growth + 1 Enterprise | $17,000 | $22,000 | $226,000 |
| Month 12 | 3 Starter + 4 Growth + 2 Enterprise | $25,500 | $34,000 | $340,000 |
| Month 18 | 4 Starter + 6 Growth + 3 Enterprise | $37,000 | $48,000 | $492,000 |

## Setup Fee Revenue Alone

Setup fees are the most overlooked revenue source in new agencies. Here is what setup fees look like at each milestone:

| Milestone | Cumulative Setup Fees |
|---|---|
| 3 clients signed | $6,000 - $18,000 |
| 6 clients signed | $12,000 - $36,000 |
| 10 clients signed | $20,000 - $60,000 |

Setup fees fund your agency's growth — they pay for tool upgrades, contractor onboarding, and the cash-flow buffer you need to deliver great work without panicking about payroll. Never waive setup fees. If a client cannot afford the setup fee, offer a payment plan (2 payments over 60 days), not a discount.

---

You now have everything you need to launch an automation agency: the infrastructure, the tools, the build framework, a working portfolio piece, client acquisition scripts, a delivery system, pricing tiers, a proposal template, and a scaling roadmap. The only variable left is your execution. Start with Module 1. Do not skip. Do not skim. Complete every procedure and every check-in. Your future clients are waiting.
