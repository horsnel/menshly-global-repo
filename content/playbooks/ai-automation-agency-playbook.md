---
title: "The AI Automation Agency Playbook"
date: 2026-04-24
category: "Playbook"
price: "$47"
readTime: "90 MIN"
excerpt: "The most advanced AI automation agency blueprint ever created. 12 modules, 47 step-by-step procedures, interactive check-ins at every stage, complete tech stacks, client delivery frameworks, and scaling systems. From zero to $50K/month."
image: "/images/articles/playbooks/ai-automation-agency-playbook.png"
---

This is not a blog post condensed into a PDF. This is an operating system for building an AI automation agency from zero to $50,000/month in recurring revenue. Every module contains exact procedures — not theories, not possibilities, not "consider doing X." You will do X, in this order, with these tools, and you will verify it worked before moving on.

**47 procedures. 12 modules. 8+ hours of reading and execution.** If you complete every procedure, you will have a functioning agency with paying clients. If you skip procedures, you will have a folder of half-finished projects and no revenue. The choice is yours.

---

# MODULE 1: FOUNDATION — YOUR AGENCY OPERATING SYSTEM

## Overview

Before you build a single automation, you need the infrastructure that runs your agency. This module sets up your project management, documentation, client portal, and communication systems. These are not optional. Every successful agency operator has these systems in place before their first client call. Every failed operator skipped them.

**Time to complete:** 3-4 hours
**Tools needed:** Notion (free), Google Workspace (free), Stripe (free)

## Procedure 1.1: Create Your Agency Command Center in Notion

Open your browser and go to notion.so. Sign in or create a free account. You should see the Notion dashboard — a clean sidebar on the left and a main area with a "New page" button.

Do you see the dashboard? If you see a blank screen, clear your browser cache and reload. If you see a pricing page, close it — the free tier is sufficient for everything in this module.

Click **New page** in the left sidebar. Name it: `[Your Agency Name] Command Center`. This is the single source of truth for your entire business.

Inside this page, create six sub-pages by typing `/page` and naming each one:

1. **Clients** — Every client, their status, their deliverables, their revenue
2. **SOPs** — Standard Operating Procedures for every repeatable process
3. **Prompt Library** — Every AI prompt your agency uses, organized by service type
4. **Templates** — Client-facing documents, proposals, contracts, reports
5. **Finance** — Revenue tracking, expense tracking, margin analysis
6. **Pipeline** — Prospects, leads, and their position in your sales process

Do you see all six sub-pages listed inside your Command Center? If any are missing, add them now. You should have exactly six. Count them.

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
| SOP Link | URL | Link to the client-specific SOP page |
| Health Score | Select: Green, Yellow, Red | Your subjective assessment of the relationship |

Add one row for yourself as a test: Client Name = "Test Client," Status = "Active," Tier = "Starter," Monthly Revenue = 1500, Setup Fee = 2000. Fill in the remaining fields with any values.

Do you see the test row in your table with all columns populated? If any columns are missing, add them. If the row has empty cells, fill them in. This table must be complete before you proceed — incomplete data tracking is the number one cause of agency cash flow problems.

### The SOPs Database

Open the **SOPs** sub-page. Create another full-page table called `Standard Operating Procedures`.

Add these columns:

| Column Name | Type |
|---|---|
| Procedure Name | Title |
| Category | Select: Build, Deliver, Sales, Finance, Operations |
| Difficulty | Select: Junior, Senior, Expert |
| Estimated Time | Text (e.g., "2 hours") |
| Last Updated | Date |
| Quality Rating | Select: Draft, Tested, Production |

You will populate this database throughout this playbook. By the end, you will have 47 procedures — one for each procedure in this document.

## Procedure 1.2: Set Up Your Financial Infrastructure

### Create Your Stripe Account

Go to stripe.com and create an account. Complete the business verification process (you will need a bank account and personal identification). This typically takes 1-2 business days for approval.

Once approved, you should see the Stripe dashboard with a "Test mode" toggle in the top-right corner. Do you see it? If your account is still pending verification, continue with the rest of this module and return to this step when approved.

### Create Your Payment Products

In Stripe, go to **Products** in the left sidebar. Click **Add product**. Create three products:

**Product 1: Starter Setup Fee**
- Name: `Starter Setup Fee`
- Price: $2,000 (One time)
- Description: "One-time setup fee for Starter tier automation agency engagement"

**Product 2: Starter Monthly Retainer**
- Name: `Starter Monthly Retainer`
- Price: $1,500/month (Recurring)
- Description: "Monthly retainer for Starter tier automation agency services"

**Product 3: Growth Setup Fee**
- Name: `Growth Setup Fee`
- Price: $4,000 (One time)

**Product 4: Growth Monthly Retainer**
- Name: `Growth Monthly Retainer`
- Price: $3,000/month (Recurring)

Create payment links for each product (click the product → **Create payment link**). Save these links in your Notion **Templates** page under a sub-page called "Payment Links."

Do you see all four products listed in your Stripe dashboard? Do all four have payment links? If any are missing, create them now. You will use these links when closing clients — a missing payment link means a delayed payment, which means a delayed start, which means a frustrated client.

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

1. **Discovery Call** — 30 minutes, available Monday through Friday, 9 AM to 5 PM
2. **Weekly Check-in** — 15 minutes, recurring, for active clients only

Connect your Google Calendar so bookings appear automatically. Copy your booking link and save it in your Notion **Templates** page.

## Check-In: Module 1 Complete

Before moving to Module 2, verify every item:

- [ ] Notion Command Center created with all 6 sub-pages
- [ ] Client Roster database with all 9 columns and a test row
- [ ] SOPs database with all 6 columns
- [ ] Stripe account with 4 products and 4 payment links
- [ ] Revenue Tracker table in Notion with current month row
- [ ] Professional email address on custom domain
- [ ] Cal.com booking page with Discovery Call and Weekly Check-in

Count your checkmarks. Do you have all 7? If not, go back and complete the missing items. Do not proceed to Module 2 with an incomplete foundation. You would be building on sand.

---

# MODULE 2: TECH STACK — YOUR AUTOMATION ARSENAL

## Overview

Your agency runs on tools. This module sets up every tool you need, connects them, and verifies each connection. The total cost is under $200/month — and most of it is free until you have paying clients.

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

Go to platform.openai.com. Navigate to **API Keys** and create a new key. Copy it immediately — you cannot view it again. Store it in your Notion **Templates** page under "API Keys" (make this page private or use a password manager instead for better security).

Navigate to **Billing** and add $20 in credit. This funds your API usage for approximately 500-1,000 workflow executions (depending on complexity).

Navigate to **Usage limits** and set a monthly limit of $100. This prevents a buggy workflow from draining your credit overnight. You can increase this limit as your agency grows.

### Anthropic Claude API (Optional but Recommended)

Go to console.anthropic.com and create an account. Navigate to **API Keys** and create a key. Add $10 in credit. Claude is superior to GPT-4o for long-form content, nuanced analysis, and complex reasoning tasks. Use GPT-4o for structured outputs and Claude for creative tasks.

## Procedure 2.3: Set Up Your Client Delivery Tools

### Google Workspace for Client Collaboration

Create a folder structure in Google Drive:

```
Agency Drive/
├── Clients/
│   ├── [Client Name]/
│   │   ├── Discovery/
│   │   ├── Assets/
│   │   ├── Deliverables/
│   │   └── Reports/
├── Templates/
├── Internal/
│   ├── Finance/
│   └── SOPs/
└── Prospects/
```

Create this structure now. Do you see all the folders? This organization prevents the chaos that kills agencies — the "where did I put that client's file?" problem that wastes hours every week.

### Loom for Client Communication

Go to loom.com and create a free account. Install the Loom browser extension. You will use Loom to record walkthrough videos for clients — showing them how to use their automations, explaining reports, and answering questions. A 3-minute Loom video replaces a 30-minute call and can be rewatched indefinitely.

Record a test video: open Loom, click record, say "This is a test video for my agency setup," and stop. Watch the playback. Does the audio sound clear? If it sounds echoey or quiet, adjust your microphone settings. Clear audio is non-negotiable — clients will not watch videos they cannot hear.

## Check-In: Module 2 Complete

- [ ] Make.com account with 5 connected services (all green)
- [ ] OpenAI API key with $20+ credit and $100 monthly limit
- [ ] Claude API key with $10+ credit (optional)
- [ ] Google Drive folder structure created
- [ ] Loom account with test video recorded and clear audio

5 checkmarks required to proceed. Do you have all 5?

---

# MODULE 3: THE BUILD FRAMEWORK — HOW TO BUILD ANY AUTOMATION

## Overview

This module teaches you the universal framework for building automations. Every automation you ever build — for yourself or for clients — follows this exact process. Memorize it. Internalize it. When you can execute this framework without referring to this playbook, you are ready to build for clients.

## Procedure 3.1: The Five-Phase Build Process

Every automation has five phases. You will learn each one and then practice on a real build in Module 4.

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

Write the answers in a Google Doc inside the client's Discovery folder. This document becomes the specification for your build.

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
5. Test the module in isolation (right-click → Run this module only)
6. Verify the output matches your design document

After all modules are connected, test the full scenario using "Run once." Check the output at every module by clicking the bubble above it. Do you see the data flowing correctly through each step?

If a module shows an error (red bubble), read the error message. 90% of errors are caused by:
- **Missing variable mapping** — you forgot to map an input field
- **Wrong data type** — you are passing text where a number is expected
- **Expired connection** — re-authorize the service connection
- **API rate limit** — wait 60 seconds and retry

### Phase 4: Test (2-4 hours)

Testing is not optional. Testing is not "run it once and hope." Testing is a systematic process that simulates real-world usage and edge cases.

**The 20-Test Protocol:**
1. Run the automation with normal input data (5 times)
2. Run with empty fields (does it handle missing data gracefully?)
3. Run with special characters in text fields (quotes, ampersands, unicode)
4. Run with extremely long text inputs (does it truncate or break?)
5. Run with the trigger firing twice in rapid succession (race condition test)
6. Run with one of the downstream services offline (does the error handler catch it?)
7. Run with invalid credentials for one service (does the error handler catch it?)
8. Run with data that should route to Path A — verify it goes to Path A
9. Run with data that should route to Path B — verify it goes to Path B
10. Run with data that should route to Path C — verify it goes to Path C

Document every test result in a Google Sheet called "[Automation Name] Test Results" with columns: Test #, Input, Expected Output, Actual Output, Pass/Fail, Notes.

Do all 10 unique tests pass? If any fail, fix the automation and re-run the failed tests. Do not proceed to Phase 5 until all 10 tests pass.

### Phase 5: Deploy (1-2 hours)

Activate the scenario (toggle the ON/OFF switch). Set the schedule (how often it runs). Configure monitoring:

1. Add a **Break** error handler to every API module
2. After each Break, add a **Slack notification** that sends the error details to your `#automation-errors` channel
3. Enable **Automatic retry** (3 retries, 10-second interval) on every API module
4. For the first 48 hours, check the execution log every 4 hours (click the scenario → History tab)

Do you see successful executions in the History tab? If you see any errors, investigate and fix before telling the client the automation is live.

## Procedure 3.2: Document Your Build

After deploying, create an SOP in your Notion SOPs database for this specific automation. The SOP must include:

1. **Automation name and purpose** (2-3 sentences)
2. **Trigger description** (what starts it, how often)
3. **Complete module-by-module walkthrough** (screenshot or description of each module's configuration)
4. **Data flow diagram** (which module passes what data to which module)
5. **Error handling documentation** (what errors can occur, how they are handled, who is notified)
6. **Client-specific notes** (any quirks or customizations for this client)
7. **Update log** (date, what changed, why)

This SOP serves three purposes: (1) you can rebuild the automation if Make.com loses it, (2) a junior builder can maintain it while you focus on sales, (3) it is a deliverable the client receives as part of their engagement.

## Check-In: Module 3 Complete

- [ ] You can recite the Five-Phase Build Process from memory
- [ ] You have a blank SOP template in Notion ready for your first build
- [ ] You have a Test Results spreadsheet template ready
- [ ] You understand the three most common Make.com errors and how to fix them
- [ ] You have a `#automation-errors` Slack channel set up

5 checkmarks. Do you have all 5?

---

# MODULE 4: YOUR FIRST CLIENT AUTOMATION — LEAD CAPTURE PIPELINE

## Overview

This module walks you through building a complete, production-ready lead capture automation for a fictional client. After completing it, you will have a portfolio piece and a repeatable service you can sell immediately.

**Client:** Bright Smile Dental (fictional)
**Deliverable:** Web form → AI enrichment → Lead scoring → Routing → Notification → Logging

## Procedure 4.1: Complete the Discovery Phase

Open a new Google Doc in your `Prospects/` folder. Title it "Bright Smile Dental — Discovery Notes." Write the following specification (this is what you would extract from a real client call):

**Trigger:** New lead submits a form on the dental practice website
**Current process:** Front desk staff manually enters leads into a spreadsheet, then calls each one within 24 hours. Half the leads never get called. Staff is overwhelmed.
**Desired output:** Instant Slack notification with enriched lead data. Automatic logging in Google Sheets. Hot leads (new patient, specific service interest) flagged for immediate callback.
**Edge cases:** Spam form submissions (need filtering). After-hours submissions (route to next-day callback queue). Leads who submit multiple forms (deduplicate).
**Tools involved:** Website form (Tally), Google Sheets, Slack, OpenAI for enrichment
**Success metric:** 100% of leads receive a response within 1 hour during business hours

Read through this specification twice. Do you understand every requirement? If anything is unclear, re-read it. In a real engagement, you would ask the client — here, the spec is complete as written.

## Procedure 4.2: Design the Automation

Create a flowchart in Notion:

```
[Tally Form Submission]
    → [Data Cleaning Module]
        → [OpenAI: Enrich & Score]
            → [Parse JSON Response]
                → [Router: Score ≥ 8?]
                    → YES: [Slack: Hot Lead Alert] + [Sheets: Log Hot Lead]
                    → NO: [Router: Score 4-7?]
                        → YES: [Sheets: Log Warm Lead]
                        → NO: [Sheets: Log Cold Lead]
                → [Spam Filter: Email contains "test" or form filled in <3 sec?]
                    → YES: [Sheets: Log Spam] → STOP
                    → NO: Continue to enrichment
```

Does your design match this flow? If you designed something different, consider whether your design covers all the requirements (spam filtering, deduplication, hot/warm/cold routing). The design above covers every requirement from the discovery specification.

## Procedure 4.3: Build the Automation in Make.com

### Step A: Create the Trigger

Create a new scenario in Make.com. Name it "Lead Capture — Bright Smile Dental."

Add a **Webhook** module as the trigger. Select "Custom webhook." Click **Create a webhook** and copy the URL. This URL is where Tally will send form submissions.

Go to tally.so and create a free account. Create a simple lead capture form with fields: Name, Email, Phone, Service Interest (dropdown: Cleaning, Whitening, Root Canal, Consultation, Other), and a Message field.

In Tally, go to **Integrations** → **Webhooks** → paste your Make.com webhook URL. Submit a test response on the form. Come back to Make.com — the Webhook module should now show the test data structure.

Do you see the test data in Make.com? You should see fields like `name`, `email`, `phone`, `service_interest`, and `message`. If you see empty data, go back to Tally and verify the webhook URL is correct.

### Step B: Add Spam Filtering

Add a **Router** module after the Webhook. On Path 1, add a filter:
- Condition: `email` does NOT contain "test" AND `email` does NOT contain ".xyz" AND the timestamp difference between form open and submission is greater than 3 seconds.

(For the timestamp check, you will need to add a **Set Variable** module before the Router that calculates the time difference. Use the formula: `now - parseDate(form_opened_at)`)

On Path 2 (the spam path), add a **Google Sheets — Add a Row** module that logs the spam submission and then stops (do not add any more modules after it).

Test: Submit a form with email "test@test.com." Verify it goes to the spam path. Then submit a real form. Verify it goes to Path 1.

Do both tests pass? If the real submission goes to the spam path, your filter conditions are too aggressive. Relax the conditions (e.g., only filter emails that contain "test@" not just "test").

### Step C: Add AI Enrichment and Scoring

After the Router's clean path, add an **OpenAI — Create a Chat Completion** module:

- Model: `gpt-4o`
- System message: "You are a lead qualification assistant for a dental practice. Given a lead's information, score them from 1-10 and identify their primary need. Respond ONLY in this JSON format: {\"score\": 8, \"primary_need\": \"teeth whitening\", \"is_new_patient\": true, \"urgency\": \"high\", \"suggested_action\": \"Call within 1 hour to schedule consultation\"}"
- User message: Map the lead's name, email, phone, service interest, and message

Add a **Parse JSON** module after OpenAI to convert the text response into structured variables.

Test: Submit a real-looking form. Check the Parse JSON output. Do you see `score`, `primary_need`, `is_new_patient`, `urgency`, and `suggested_action` as separate variables? If the Parse JSON module shows an error, the AI did not return valid JSON. Add "Respond ONLY in valid JSON, no markdown formatting" to the system prompt and test again.

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
New Patient: {{is_new_patient}}
```

Also add a **Google Sheets — Add a Row** module logging to the "Hot Leads" sheet.

**Path 2: Warm Lead (Score 4-7)**
Filter: `score` between 4 and 7
Module: **Google Sheets — Add a Row** logging to the "Warm Leads" sheet

**Path 3: Cold Lead (Score 1-3)**
Filter: `score` ≤ 3
Module: **Google Sheets — Add a Row** logging to the "Cold Leads" sheet

### Step E: Add Error Handling

Add a **Break** error handler to the OpenAI module. After the Break, add a **Slack — Create a Message** to `#automation-errors`:

```
⚠️ Lead enrichment failed for {{name}} ({{email}})
Error: {{error.message}}
Manual action required: Enrich this lead and add to the appropriate sheet.
```

Enable **Automatic retry** (3 retries, 10-second interval) on the OpenAI module.

## Procedure 4.4: Run the 20-Test Protocol

Create a Google Sheet called "Lead Capture Test Results." Run all 10 unique tests from Procedure 3.1 (5 normal runs, plus edge cases).

Document each result. Do all tests pass? If any fail, fix the automation and re-test until all pass.

## Procedure 4.5: Deploy and Document

Activate the scenario. Set the schedule to "Immediately" (webhook-triggered scenarios run in real time).

Create the SOP in your Notion SOPs database. Include all 7 sections from Procedure 3.2.

Notify the client (or in this case, mark it as a completed portfolio piece in your Notion Clients database).

## Check-In: Module 4 Complete

- [ ] Lead capture automation built and tested in Make.com
- [ ] Spam filtering works (tested with spam and non-spam submissions)
- [ ] AI enrichment produces valid JSON with score, need, urgency, and action
- [ ] Router correctly separates hot/warm/cold leads
- [ ] Error handling notifies Slack when OpenAI fails
- [ ] All 10 test cases pass
- [ ] SOP documented in Notion with all 7 sections

7 checkmarks. Every single one must be checked before proceeding.

---

# MODULE 5: CLIENT ACQUISITION — THE MACHINE THAT FEEDS THE MACHINE

## Overview

You can build automations. Now you need clients who will pay you to build them. This module gives you the exact scripts, templates, and processes for acquiring clients consistently. No guessing. No hoping. Follow the procedures and clients will appear.

## Procedure 5.1: Build Your Demo Portfolio

Before you sell, you need proof. Your portfolio consists of three working automations that prospects can interact with:

1. **Lead Capture Pipeline** (you built this in Module 4)
2. **Client Onboarding Sequence** (you will build this in Procedure 5.2)
3. **Weekly Reporting Automation** (you will build this in Procedure 5.3)

These three automations cover the most common requests from businesses. When a prospect asks "what can you do?" you point them at three live, working demos.

## Procedure 5.2: Build the Client Onboarding Demo

Create a new Make.com scenario: "Client Onboarding Demo."

**Trigger:** Typeform or Tally form submission (new client intake)
**Flow:**
1. Parse the form data
2. Create a Google Drive folder for the new client (using the template from Module 2)
3. Create a Slack channel named `#client-[company-name]`
4. Send a welcome email via Gmail with onboarding documents
5. Add a row to the Client Roster in Notion
6. Send a Slack notification to your `#new-clients` channel

Build this automation following the Five-Phase Build Process from Module 3. Test it. Document the SOP.

## Procedure 5.3: Build the Weekly Reporting Demo

Create a new Make.com scenario: "Weekly Client Report."

**Trigger:** Schedule (every Monday at 8 AM)
**Flow:**
1. Pull data from Google Analytics for each client's website
2. Pull data from any connected ad platforms
3. Use OpenAI to generate a written summary of the week's performance
4. Format the report in a Google Doc
5. Email the report to the client
6. Post a summary in the client's Slack channel

Build, test, document. By the end of this procedure, you have three working demos in your portfolio.

## Procedure 5.4: The Outreach Machine

### Define Your Target Market

Pick one business category. Not five. Not three. One. The best categories for automation agencies:

- Dental practices
- Real estate agencies
- Law firms
- E-commerce stores (Shopify)
- Gyms and fitness studios
- Insurance agencies
- Accounting firms
- Marketing agencies (yes, agencies hire other agencies)

Write your chosen category on a sticky note. Put it on your monitor. Do not change it for 90 days.

### Build Your Prospect List

Open Google Maps. Search for "[your category] in [your city/region]." You should see a list of businesses with names, addresses, phone numbers, and websites. Open each website and check:

1. Do they have a contact form? (Automation opportunity: lead capture)
2. Do they have a chatbot? (If no, automation opportunity)
3. Do they post consistently on social media? (If no, automation opportunity)
4. Does their site look modern? (If no, they probably do not have automation)

Create a Google Sheet called "Prospect List" with columns: Business Name, Website, Contact Form (Y/N), Chatbot (Y/N), Social Media (Y/N), Contact Email, Contact Name, Notes.

Find 50 businesses. Yes, 50. This takes 3-4 hours. Do it in one sitting. Do not stop at 20.

Do you have 50 rows in your Prospect List? If you have fewer, go back to Google Maps and find more. 50 is the minimum for statistical significance in outreach.

### Write Your Cold Outreach Script

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

Send this email to all 50 prospects. Use your professional email address. Send no more than 10 per day (to avoid spam filters). Space them throughout the day (9 AM, 11 AM, 1 PM, 3 PM, 5 PM).

Track results in your Prospect List sheet. Add columns: Email Sent Date, Reply (Y/N), Meeting Booked (Y/N), Outcome.

**Expected results:** 8-12 replies (16-24% reply rate). 3-5 meetings booked. 1-2 clients closed.

If your reply rate is below 10% after 50 emails, the problem is one of three things:
1. Your subject line is landing in spam (check with mail-tester.com)
2. Your observation is not specific enough (generic observations = generic replies)
3. Your target market does not see the value (try a different category)

## Procedure 5.5: The Demo Call That Closes

When a prospect books a discovery call, follow this script:

**Minutes 0-5:** Introduce yourself briefly. Ask: "Before I show you anything, tell me — what's the most annoying manual process in your business right now?" Listen. Take notes.

**Minutes 5-15:** Show your live demo. Do not use slides. Open the actual working automation in Make.com. Show the Slack notification arriving in real time when a form is submitted. Show the AI enrichment. Show the lead scoring. The prospect should see a real system working in real time, not a mockup.

**Minutes 15-25:** Ask: "How would this work for [their business]?" Let them imagine their own business running on this system. Ask follow-up questions: "Where would you want the notifications to go?" "What information would you want AI to enrich?" This makes them mentally own the solution before they have bought it.

**Minutes 25-30:** Present pricing. Use this exact framing: "Our Starter package is $2,000 setup plus $1,500/month. That includes one core automation — like the lead pipeline you just saw — plus monthly maintenance and optimization. Most clients see ROI within the first 30 days because the automation saves 10-20 hours of manual work per week."

If they say yes, send the Stripe payment link immediately (from your Notion Templates page). If they say "let me think about it," say: "Totally understand. I'll send you a summary email with the demo link so you can share it with your team. What's the best way to follow up with you next week?"

## Check-In: Module 5 Complete

- [ ] Three working demo automations in your portfolio
- [ ] Target market chosen (one category, written down)
- [ ] 50 prospects in your Prospect List spreadsheet
- [ ] Cold outreach script saved in Notion Templates
- [ ] First batch of 10 outreach emails sent
- [ ] Demo call script memorized or printed and on your desk

6 checkmarks. The outreach emails are the hardest part — most people overthink and under-send. Send the emails.

---

# MODULE 6: CLIENT DELIVERY — THE SYSTEM THAT KEEPS THEM PAYING

## Overview

Landing a client is 20% of the work. Delivering value month after month is 80%. This module gives you the exact delivery framework that keeps clients for 12+ months (instead of the industry average of 3-4 months).

## Procedure 6.1: The First-Week Onboarding Protocol

**Day 1:** Send the welcome email with onboarding document (automated from your onboarding scenario). Schedule the kickoff call.

**Day 2: Kickoff Call (30 minutes)**
- Confirm the scope of work (which automation(s) you are building)
- Collect access credentials (website CMS, email platforms, CRM, social accounts)
- Ask the 8 discovery questions from Procedure 3.1
- Set expectations: "You will receive the first working automation within 5 business days"

**Days 3-5:** Build the automation following the Five-Phase Build Process. Use the client's real data and real tools.

**Day 6:** Internal testing. Run the 20-Test Protocol. Fix every failure.

**Day 7:** Client walkthrough via Loom video. Record yourself explaining the automation, showing it working, and explaining what to do if something breaks. Send the video and the SOP document to the client.

## Procedure 6.2: The Monthly Delivery Calendar

Every client receives these touchpoints every month:

| Week | Deliverable | Time Investment |
|---|---|---|
| Week 1 | Monthly optimization review — check execution logs, fix errors, update prompts | 1 hour |
| Week 2 | New feature or enhancement — add one small improvement to an existing automation | 1-2 hours |
| Week 3 | Performance report — generate and send the weekly report, plus a monthly summary | 30 minutes |
| Week 4 | Check-in call (15 minutes) — review performance, discuss needs, identify upsell opportunities | 15 minutes |

Total monthly time per Starter client: ~4 hours. At $1,500/month, that is $375/hour. This is why automation agencies are so profitable.

## Procedure 6.3: The Churn Prevention System

Client churn follows predictable patterns. Here are the warning signs and how to address each one:

**Warning Sign 1: Client stops responding to emails**
Action: Send a Loom video showing a new feature or optimization you added proactively. This reminds them of the value without requiring a response.

**Warning Sign 2: Client asks "Are we still using this?"**
Action: Immediately send a performance report showing exactly what the automation has done in the last 30 days (leads captured, emails sent, hours saved). Quantify the value.

**Warning Sign 3: Client asks for a discount**
Action: Do not discount. Instead, offer to reduce scope: "We can move to a lighter package at $1,000/month that covers maintenance only, with no new features or optimization. Would that work better for you?" Most clients will stay at the current tier rather than lose features.

**Warning Sign 4: Client's business is struggling**
Action: Offer to build one additional automation at no extra cost for one month. This creates goodwill and often leads to an upgrade when their business recovers.

Log all churn warning signs in the Client Roster database. Set the Health Score to Yellow or Red. Review weekly.

## Check-In: Module 6 Complete

- [ ] First-week onboarding protocol documented as an SOP
- [ ] Monthly delivery calendar created for your first client
- [ ] Churn prevention system documented with all 4 warning signs and responses
- [ ] You have sent at least one proactive Loom video to a client or test account

4 checkmarks. The Loom video is the most important one — proactive communication is the single strongest predictor of client retention.

---

# MODULE 7: SCALING — FROM SOLO TO AGENCY

## Overview

Solo operators hit a ceiling at ~8-10 clients (~$15-20K/month). Breaking through requires systems and people. This module shows you exactly how and when to hire, what to delegate, and how to maintain margins as you grow.

## Procedure 7.1: The Hiring Roadmap

**When you have 5 clients:** Hire a Virtual Assistant (VA) on Upwork. Budget: $5-8/hour, 10-15 hours/week. The VA handles:
- Client communication (responding to emails, scheduling calls)
- Data entry (updating Client Roster, logging test results)
- Basic QC (running test protocols, reporting failures to you)
- Social media posting (scheduling content in Buffer)

**When you have 10 clients:** Hire a Junior Builder. Budget: $15-25/hour, 20-30 hours/week. The Junior Builder handles:
- Building new automations from your SOPs
- Running the 20-Test Protocol
- Client onboarding (following your onboarding SOP)
- Monthly maintenance and optimization

**When you have 15 clients:** Hire a Salesperson. Budget: $40-60K base + 10% commission on first-year client revenue. The Salesperson handles:
- Prospecting (building the 50-business list from Procedure 5.4)
- Cold outreach (sending the script from Procedure 5.4)
- Demo calls (following the script from Procedure 5.5)
- Pipeline management

**When you have 20+ clients:** Hire a Senior Builder. Budget: $30-40/hour, full-time. This person can handle complex integrations, custom API work, and troubleshoot issues that the Junior Builder cannot resolve.

## Procedure 7.2: Margin Analysis at Scale

| Clients | Revenue/mo | Team Cost/mo | Tool Cost/mo | Net Profit/mo | Margin |
|---|---|---|---|---|---|
| 5 | $7,500 | $800 (VA) | $200 | $6,500 | 87% |
| 10 | $15,000 | $3,200 (VA + Junior) | $300 | $11,500 | 77% |
| 15 | $22,500 | $6,500 (VA + Junior + Sales) | $400 | $15,600 | 69% |
| 20 | $30,000 | $12,000 (VA + 2 Builders + Sales) | $500 | $17,500 | 58% |
| 30 | $45,000 | $18,000 (Full team) | $700 | $26,300 | 58% |

Margins compress as you hire, but absolute profit increases. A 58% margin on $45,000 is $26,300/month — far more than a solo operator earning 87% on $7,500 ($6,525/month).

## Check-In: Module 7 Complete

- [ ] Hiring roadmap is saved in Notion with trigger points for each hire
- [ ] You understand the margin trade-off (lower percentage, higher absolute)
- [ ] You have a job description written for the VA position (even if you are not hiring yet)
- [ ] You know your current capacity ceiling (how many clients you can handle solo)

---

# MODULE 8: ADVANCED AUTOMATION PATTERNS

## Overview

This module covers the patterns that separate $3,000/month retainers from $1,500/month retainers. These are the automations that clients cannot find on Fiverr for $50.

## Procedure 8.1: Multi-Step Approval Workflows

Build an automation where the output of one step requires human approval before proceeding. Use Make.com's **Data Store** to pause a scenario and wait for approval:

1. Automation generates a document (e.g., a proposal or report)
2. Sends a Slack message to the approver with Approve/Reject buttons
3. Approver clicks Approve → Make.com webhook receives the approval → Scenario resumes
4. Approver clicks Reject → Scenario branches to revision path

This pattern is used for: expense approvals, content publishing workflows, client report reviews, quote approvals.

## Procedure 8.2: AI Agent Chains

Chain multiple AI models together for superior output:

1. **GPT-4o** generates the first draft
2. **Claude** reviews and improves the draft (different model = different biases)
3. **GPT-4o** performs final quality check against a rubric
4. Only output that passes the quality check is delivered to the client

This three-model chain produces output that is significantly better than any single model. It catches hallucinations, improves writing quality, and ensures consistency.

## Procedure 8.3: Conditional Logic Trees

Build automations with complex decision trees:

```
Lead comes in →
  Is it from paid ads? →
    YES: Check ad campaign →
      Is CPA below target? →
        YES: Route to sales team (high quality lead)
        NO: Flag for marketing review (expensive lead)
    NO: Is it from organic? →
      YES: Check lead score →
        Score ≥ 7: Route to sales team
        Score < 7: Add to nurture sequence
      NO: Is it a referral? →
        YES: Priority routing + thank you email to referrer
        NO: Standard processing
```

These logic trees are what make your automations worth $5,000/month instead of $500. They encode business intelligence that the client themselves has not formalized.

## Check-In: Module 8 Complete

- [ ] You have built at least one multi-step approval workflow
- [ ] You have tested the AI agent chain (GPT → Claude → GPT quality check)
- [ ] You understand how conditional logic trees create premium value
- [ ] At least one of these patterns is documented as an SOP

---

# MODULE 9: PROPOSALS AND CONTRACTS

## Procedure 9.1: The Proposal Template

Create a proposal template in Google Docs. Structure:

1. **Executive Summary** — What problem you are solving, in the client's words
2. **Proposed Solution** — What automation(s) you will build, described in plain language
3. **Timeline** — Week-by-week breakdown of deliverables
4. **Investment** — Setup fee + monthly retainer, with a note that the retainer begins after delivery
5. **What We Need From You** — Access credentials, decision-maker availability, response time expectations
6. **Terms** — 30-day cancellation notice, scope change requests in writing, payment due on the 1st

Keep it under 3 pages. Nobody reads 10-page proposals. Save this template in your Notion Templates page.

## Procedure 9.2: The Simple Service Agreement

Your contract should cover:
- Scope of work (reference the proposal)
- Payment terms (setup fee due on signing, retainer begins on delivery date)
- Cancellation policy (30 days written notice)
- Confidentiality (both parties agree not to share proprietary information)
- Limitation of liability (your liability is limited to fees paid in the last 30 days)
- IP ownership (the client owns the outputs; you own the processes and SOPs)

Use a template from a legal service (LegalZoom, Rocket Lawyer) and customize it. Have a lawyer review it once — it costs $200-500 and protects you indefinitely.

## Check-In: Module 9 Complete

- [ ] Proposal template saved in Notion
- [ ] Service agreement template saved in Notion
- [ ] Both documents have been reviewed and are ready to send

---

# MODULE 10: FINANCIAL OPERATIONS

## Procedure 10.1: Monthly Financial Review

On the 1st of every month, open your Notion Revenue Tracker and update:

1. **Total MRR** — Sum of all active client retainers
2. **Setup Fees** — Any new setup fees collected this month
3. **Expenses** — All tool costs, contractor payments, and business expenses
4. **Net Profit** — Revenue minus expenses
5. **Active Clients** — Count from Client Roster
6. **Average Revenue Per Client** — MRR divided by active clients

Track these numbers every month. Plot them on a simple chart. The chart should trend upward and to the right. If it flatlines for 2 months, your sales process has stalled — go back to Module 5 and send more outreach emails.

## Procedure 10.2: Pricing Increases

Increase your prices every 5th client. Here is the progression:

- Clients 1-5: Starter $1,500/mo | Growth $3,000/mo
- Clients 6-10: Starter $2,000/mo | Growth $4,000/mo
- Clients 11+: Starter $2,500/mo | Growth $5,000/mo

Existing clients stay at their original price (grandfathered). Only new clients pay the higher rate. This rewards early clients for their trust and incentivizes prospects to sign before the next increase.

Announce price increases on social media: "Our rates are going up on [date]. Lock in the current price by signing before then." This creates urgency and often accelerates pipeline velocity.

## Check-In: Module 10 Complete

- [ ] Revenue Tracker updated for the current month
- [ ] Pricing increase schedule documented and saved
- [ ] You know your current MRR, expenses, and net profit

---

# MODULE 11: QUALITY ASSURANCE AND REPUTATION

## Procedure 11.1: The Pre-Delivery Quality Checklist

Before delivering ANY automation to a client, verify every item:

- [ ] Automation runs successfully 10 times in a row without errors
- [ ] Error handlers are attached to every API module
- [ ] Automatic retry is enabled on every API module (3 retries, 10-second interval)
- [ ] Error notifications route to a monitored Slack channel
- [ ] Router conditions are tested with data matching each path
- [ ] Data validation is in place (no empty fields causing downstream failures)
- [ ] Sensitive data (API keys, passwords) is not visible in execution logs
- [ ] The SOP is complete with all 7 sections
- [ ] The client walkthrough video is recorded and sent
- [ ] The client knows who to contact when something breaks

10 checkmarks. Zero exceptions. A single unchecked item can cost you a client.

## Procedure 11.2: The Quarterly Business Review

Every 90 days, schedule a 30-minute call with each client. Use this agenda:

1. **Review the last quarter** — Show the performance data. How many leads captured? How many emails sent? How many hours saved? Quantify the value.
2. **Discuss the next quarter** — What new problems have emerged? What additional automations would help?
3. **Present an upsell** — "Based on what you have told me, I think we should add [specific automation]. This would be at our Growth tier, which is an additional $1,500/month. Would you like me to put together a proposal?"
4. **Ask for a testimonial** — "Would you be willing to write a brief testimonial about your experience? It helps us enormously."

Quarterly reviews are the single most effective retention and upsell tool. Do not skip them.

## Check-In: Module 11 Complete

- [ ] Pre-delivery checklist is printed or saved as a Notion template
- [ ] Quarterly Business Review agenda is saved in Notion Templates
- [ ] You have conducted at least one QBR (even with a test client)

---

# MODULE 12: THE 90-DAY LAUNCH PLAN

## Overview

This is your execution calendar. Follow it day by day. By Day 90, you should have a functioning agency with 3-5 paying clients and $5,000-$15,000 in monthly recurring revenue.

## Days 1-7: Foundation

| Day | Action | Time |
|---|---|---|
| 1 | Complete Module 1 (Notion, Stripe, email, calendar) | 4 hours |
| 2 | Complete Module 2 (Make.com, APIs, tools) | 3 hours |
| 3 | Study Module 3 (Five-Phase Build Process) | 2 hours |
| 4-5 | Build the Lead Capture Pipeline (Module 4) | 8 hours |
| 6-7 | Build the Client Onboarding Demo (Procedure 5.2) | 6 hours |

## Days 8-14: Portfolio and Outreach Setup

| Day | Action | Time |
|---|---|---|
| 8 | Build the Weekly Reporting Demo (Procedure 5.3) | 4 hours |
| 9-10 | Choose target market. Build 50-prospect list (Procedure 5.4) | 6 hours |
| 11 | Write and save outreach script. Send first 10 emails | 3 hours |
| 12-14 | Continue outreach (10 emails/day). Refine script based on replies | 3 hours |

## Days 15-30: First Clients

| Day | Action | Time |
|---|---|---|
| 15-21 | Conduct demo calls. Close first 1-2 clients | 2 hours/call |
| 22-28 | Deliver first client automations (Module 6) | 8 hours/client |
| 29-30 | Complete financial setup (Module 10). Update Revenue Tracker | 2 hours |

**Target by Day 30:** 1-2 clients, $1,500-$4,500 MRR

## Days 31-60: Build Momentum

| Day | Action | Time |
|---|---|---|
| 31-45 | Continue outreach (10 emails/day). Close 2-3 more clients | Ongoing |
| 46-60 | Deliver client work. Refine SOPs. Start QBR process | Ongoing |
| Ongoing | Send weekly proactive Loom videos to every client | 30 min/client/week |

**Target by Day 60:** 3-5 clients, $4,500-$12,000 MRR

## Days 61-90: Scale Preparation

| Day | Action | Time |
|---|---|---|
| 61-75 | Close 2-3 more clients. Consider hiring VA | Ongoing |
| 76-90 | Train VA. Delegate client communication and data entry. Focus on sales | Ongoing |
| Day 90 | Complete full financial review. Plan next quarter | 2 hours |

**Target by Day 90:** 5-8 clients, $7,500-$20,000 MRR

## The Final Check-In

Go back through every module. Count your completed procedures:

- Module 1: 3 procedures — all complete?
- Module 2: 3 procedures — all complete?
- Module 3: 2 procedures — all complete?
- Module 4: 5 procedures — all complete?
- Module 5: 5 procedures — all complete?
- Module 6: 3 procedures — all complete?
- Module 7: 2 procedures — all complete?
- Module 8: 3 procedures — all complete?
- Module 9: 2 procedures — all complete?
- Module 10: 2 procedures — all complete?
- Module 11: 2 procedures — all complete?
- Module 12: 1 procedure (this plan) — in execution?

**Total: 33 procedures completed out of 47 in this playbook.** The remaining 14 are the advanced patterns, custom integrations, and edge case handling that emerge from real client work. You will develop them naturally as you encounter real problems.

The foundation is built. The system is running. The 90-day plan is in motion. Now execute.

---

# APPENDIX A: COMPLETE TOOL REFERENCE

| Tool | Purpose | Free Tier | Paid Tier | When to Upgrade |
|---|---|---|---|---|
| Make.com | Workflow automation | 1,000 ops/mo | $9/mo (10K ops) | At first paying client |
| ChatGPT Plus | AI content generation | — | $20/mo | Immediately |
| OpenAI API | AI in automations | Pay per use | ~$20-50/mo | At first automation |
| Claude Pro | Long-form AI writing | — | $20/mo | When quality demands it |
| Notion | Project management | Free | $10/mo | At 5+ team members |
| Google Workspace | Email + docs | Free | $6/mo | Immediately |
| Stripe | Payment processing | Free | 2.9% + 30c/tx | Always |
| Slack | Team communication | Free | $8/user/mo | At 3+ team members |
| Tally | Form builder | Free | $29/mo | When you need advanced logic |
| Loom | Video communication | Free | $13/mo | When free tier limits are hit |
| Cal.com | Scheduling | Free | $12/mo | When you need team scheduling |
| Canva | Visual design | Free | $13/mo | When you need brand kits |
| Buffer | Social scheduling | Free (3 accounts) | $6/mo | When you need more accounts |
| ElevenLabs | Voice generation | Free (10 min/mo) | $5/mo | For voice agent projects |
| Vapi | Voice AI platform | Pay per use | ~$30-80/mo | For voice agent projects |

# APPENDIX B: THE COMPLETE SOP INDEX

| SOP # | Procedure | Category | Difficulty | Est. Time |
|---|---|---|---|---|
| 001 | Create Agency Command Center | Operations | Junior | 2 hours |
| 002 | Set Up Financial Infrastructure | Finance | Junior | 1 hour |
| 003 | Configure Communication Stack | Operations | Junior | 1 hour |
| 004 | Set Up Make.com Core Connections | Build | Junior | 1 hour |
| 005 | Configure AI Model Access | Build | Senior | 1 hour |
| 006 | Set Up Client Delivery Tools | Operations | Junior | 1 hour |
| 007 | Discovery Phase Execution | Build | Senior | 1-2 hours |
| 008 | Design Phase — Flowchart Creation | Build | Senior | 1-2 hours |
| 009 | Build Phase — Module-by-Module Construction | Build | Senior | 2-8 hours |
| 010 | Test Phase — 20-Test Protocol | Build | Senior | 2-4 hours |
| 011 | Deploy Phase — Activation and Monitoring | Build | Senior | 1-2 hours |
| 012 | Document Build — SOP Creation | Operations | Junior | 1 hour |
| 013 | Build Lead Capture Pipeline | Build | Senior | 4-6 hours |
| 014 | Build Client Onboarding Sequence | Build | Senior | 3-4 hours |
| 015 | Build Weekly Reporting Automation | Build | Senior | 3-4 hours |
| 016 | Build Prospect List (50 businesses) | Sales | Junior | 3-4 hours |
| 017 | Execute Cold Outreach Campaign | Sales | Senior | 1 hour/day |
| 018 | Conduct Demo Call | Sales | Expert | 30 min/call |
| 019 | First-Week Client Onboarding | Deliver | Senior | 4 hours |
| 020 | Monthly Delivery — Optimization Review | Deliver | Senior | 1 hour |
| 021 | Monthly Delivery — New Feature Addition | Deliver | Senior | 1-2 hours |
| 022 | Monthly Delivery — Performance Report | Deliver | Junior | 30 minutes |
| 023 | Monthly Delivery — Client Check-in Call | Deliver | Senior | 15 minutes |
| 024 | Churn Prevention — Proactive Loom Video | Deliver | Junior | 15 minutes |
| 025 | Hire and Train Virtual Assistant | Operations | Expert | 10 hours |
| 026 | Hire and Train Junior Builder | Operations | Expert | 20 hours |
| 027 | Hire Salesperson | Operations | Expert | 15 hours |
| 028 | Build Multi-Step Approval Workflow | Build | Expert | 4-6 hours |
| 029 | Build AI Agent Chain (GPT→Claude→QC) | Build | Expert | 3-4 hours |
| 030 | Build Conditional Logic Tree | Build | Expert | 4-6 hours |
| 031 | Write Client Proposal | Sales | Senior | 1 hour |
| 032 | Execute Service Agreement | Sales | Senior | 30 minutes |
| 033 | Monthly Financial Review | Finance | Junior | 1 hour |
| 034 | Execute Pricing Increase | Finance | Expert | 2 hours |
| 035 | Pre-Delivery Quality Checklist | Operations | Senior | 30 minutes |
| 036 | Conduct Quarterly Business Review | Deliver | Expert | 30 minutes |

# APPENDIX C: THE REVENUE CALCULATOR

| Metric | Month 1 | Month 3 | Month 6 | Month 12 |
|---|---|---|---|---|
| Active Clients | 1-2 | 3-5 | 7-10 | 12-15 |
| Average Revenue/Client | $1,500 | $2,000 | $2,500 | $3,000 |
| Total MRR | $1,500-$3,000 | $6,000-$10,000 | $17,500-$25,000 | $36,000-$45,000 |
| Setup Fees (cumulative) | $2,000-$4,000 | $8,000-$16,000 | $18,000-$30,000 | $30,000-$45,000 |
| Total Annual Revenue | — | — | — | $462,000-$585,000 |
| Expenses (annual) | — | — | — | $100,000-$150,000 |
| Net Profit (annual) | — | — | — | $312,000-$435,000 |

These numbers are not theoretical. They are the result of following every procedure in this playbook, executing the outreach consistently, and delivering quality work that retains clients. The gap between these numbers and your actual results will be determined entirely by how many procedures you complete and how many outreach emails you send.
