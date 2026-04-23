---
title: "Design, Build, and Deploy Make.com Automation Workflows"
date: 2026-04-20
category: "Implementation"
difficulty: "ADVANCED"
readTime: "28 MIN"
excerpt: "The complete execution guide for building production-grade Make.com automation workflows. From architecture principles to 5 deployable templates to scaling with error handling."
---

Make.com (formerly Integromat) is the backbone of the automation economy. Zapier gets the mainstream attention, but Make.com offers superior flexibility, lower costs at scale, and more sophisticated error handling — making it the platform of choice for serious automation builders. This guide takes you from your first workflow to production-grade systems that run reliably for paying clients.

Follow every step in order. Each step builds on the previous one. If you skip ahead, your workflows will break in ways that are difficult to diagnose later.

## Prerequisites

- A Make.com account — go to make.com and sign up for the Free plan (1,000 operations/mo)
- A Google account (for Google Sheets, Gmail, and Google Docs modules)
- A Slack account with a workspace where you have admin or the ability to install apps
- An OpenAI API key with $10 credit — go to platform.openai.com/api-keys
- A test email address you control (separate from your personal email)
- 6-8 hours of uninterrupted time for your first full build

Total upfront cost: $10 for the OpenAI API key. The Make.com free tier handles your first 3-4 workflows.

## Step 1: Understand Make.com Architecture

Before you build anything, you need to understand how Make.com thinks. Every workflow follows the **Trigger → Process → Output** pattern. Data comes in from a trigger (a webhook, a schedule, or a poll), gets transformed through a series of modules, and produces a defined output (an email, a spreadsheet row, a Slack message, a CRM update).

Open your browser and go to make.com. Sign in. You should see the Make.com dashboard — a left sidebar with "Scenarios" at the top and a main area showing any existing scenarios or a "Create a new scenario" button.

Do you see the dashboard? If you see a pricing page or an onboarding wizard, complete the wizard first (skip the paid upgrade). You need to reach the main dashboard before continuing.

### Key Concepts to Memorize

- **Scenario** — A complete automation workflow. One scenario = one automation.
- **Module** — A single step in a scenario (e.g., "Watch Google Sheets," "Send Email," "HTTP Request").
- **Operation** — One execution of one module. Make.com bills by operations. A scenario with 8 modules that runs once uses 8 operations.
- **Bundle** — A single data item passing through a module. If a trigger finds 5 new emails, it produces 5 bundles.
- **Router** — A module that splits a workflow into multiple paths based on conditions.
- **Iterator** — A module that takes an array of items and processes them one at a time.
- **Aggregator** — A module that collects multiple bundles back into a single bundle.

You will use every one of these in this guide. Do not proceed until you can explain what each one does in your own words.

## Step 2: Build Your First Workflow — Lead Capture Pipeline

This is the automation that every business needs. It captures leads from a web form, enriches them, notifies the team, and logs them in a spreadsheet. You will build it from scratch.

### Create a New Scenario

From the dashboard, click **Create a new scenario**. A blank canvas will appear with a large "+" button in the center. This is the Make.com scenario editor.

Click the **+** button. A module search bar will appear. Type "Google Sheets" and select it. Then select the **Watch Rows** trigger module. This module will check a Google Sheet for new rows at regular intervals.

Do you see the Google Sheets module configuration panel? If the panel does not appear, click the module icon on the canvas. A configuration panel should slide in from the right.

### Configure the Trigger

In the Google Sheets module configuration:

1. **Connection:** Click "Add" and connect your Google account. Follow the OAuth flow. When you return to Make.com, you should see your Google account listed. Select it.
2. **Spreadsheet:** Click into the field and select "Create a spreadsheet." Name it `Lead Capture Test`. Make.com will create this spreadsheet in your Google Drive.
3. **Sheet:** Select "Sheet1."
4. **Range:** Select "A1:Z1000."
5. **Column with timestamps:** Select column A (this is how Make.com knows which rows are new).
6. **Polling interval:** Set to 5 minutes (this is how often Make.com checks for new rows).

Click **OK** to save. You should see the module turn from gray to colored, with a small clock icon indicating it is a scheduled trigger. Do you see this? If the module is still gray, the connection to Google Sheets failed. Go back, remove the connection, and reconnect your Google account.

### Add the Data Transformation Step

Hover over the right edge of the Google Sheets module until a small "+" appears. Click it. Search for "Text Parser" and select the **Replace** module. This step cleans up the raw data from the spreadsheet.

Configure it:
- **Text:** Map the Name field from the Google Sheets module (click in the field, then select the Name variable from the popup)
- **Pattern:** `\s+` (this matches extra whitespace)
- **Replacement:** A single space
- **Global match:** Yes

This ensures that names with extra spaces get cleaned up before they go anywhere. Data cleaning is not optional — dirty data causes problems in every downstream module.

### Add the Notification Step

Add another module after Text Parser. Search for "Slack" and select **Create a Message**.

Configure it:
1. **Connection:** Connect your Slack workspace (follow the OAuth flow)
2. **Channel:** Select a test channel (create one called `#lead-notifications` if needed)
3. **Text:** Type this message, mapping variables from the previous modules:

```
New Lead Captured!
Name: {{2.name}}
Email: {{2.email}}
Source: {{2.source}}
Timestamp: {{2.timestamp}}
```

The `{{2.name}}` syntax is Make.com's variable mapping. The number refers to the module position in the chain, and the text after the dot is the field name. When you type `{{`, a popup will appear showing available variables — use this to select the correct ones rather than typing them manually.

Click **OK**. Your Slack module should now be connected to the Text Parser module with a line between them.

### Test the Workflow

Before going further, test what you have built. Go to your Google Drive, open the "Lead Capture Test" spreadsheet, and add a row:
- Column A: Current timestamp (type the current date and time)
- Column B: "John Smith" (Name)
- Column C: "john@test.com" (Email)
- Column D: "Website" (Source)

Come back to Make.com and click the **Run once** button at the bottom-left of the scenario editor. The scenario should execute: the Google Sheets module finds the new row, the Text Parser cleans the name, and the Slack module posts a message.

Check your Slack channel. Do you see the notification? You should see something like:

> New Lead Captured!
> Name: John Smith
> Email: john@test.com
> Source: Website
> Timestamp: 2026-04-22 14:30

If you see this, your first workflow is working. If Slack shows empty fields, your variable mapping is wrong — go back to the Slack module, click in each field, and re-map the variables using the popup selector.

## Step 3: Add AI Enrichment

Now you will add an OpenAI module that enriches each lead with a quality score and suggested next action. This is what separates a basic automation from one worth paying $2,000 for.

### Add the OpenAI Module

Between the Text Parser and Slack modules, insert a new module. Click on the line connecting them and select **Insert module**. Search for "OpenAI" and select **Create a Chat Completion**.

Configure it:
1. **Connection:** Add your OpenAI API key
2. **Model:** Select `gpt-4o`
3. **Messages:** Add one message with role "System" and content:

```
You are a lead qualification assistant. Given a lead's name, email, and source, you:
1. Score the lead from 1-10 (10 = hottest)
2. Suggest the best next action
3. Identify the likely industry

Respond in this exact JSON format:
{"score": 8, "next_action": "Call within 1 hour", "industry": "SaaS"}
```

4. Add a second message with role "User" and content:

```
Name: {{2.name}}
Email: {{2.email}}
Source: {{2.source}}
```

Click **OK**. The OpenAI module should now sit between the Text Parser and Slack modules.

### Update the Slack Notification

Open the Slack module. Update the message text to include the AI enrichment:

```
New Lead Captured!
Name: {{2.name}}
Email: {{2.email}}
Source: {{2.source}}

AI Enrichment:
Score: {{4.choices[1].message.content.score}}/10
Next Action: {{4.choices[1].message.content.next_action}}
Industry: {{4.choices[1].message.content.industry}}
```

Wait — there is a problem. The OpenAI module returns a JSON string inside the message content, but Make.com cannot directly access nested JSON from a text response. You need to parse it first.

### Add a JSON Parser

Between the OpenAI module and the Slack module, insert a **JSON → Parse JSON** module. Map the OpenAI response content to the JSON string field. This converts the AI's text response into structured data that Make.com can access as variables.

Now update the Slack message to use the parsed variables:

```
New Lead Captured!
Name: {{2.name}}
Email: {{2.email}}
Source: {{2.source}}

AI Enrichment:
Score: {{5.score}}/10
Next Action: {{5.next_action}}
Industry: {{5.industry}}
```

(The module numbers shift when you insert new modules — verify the numbers by clicking in the field and using the variable selector.)

### Test Again

Add another row to your Google Sheet. Run the scenario once. Check Slack.

Do you see the enriched notification with a score, next action, and industry? If the score field is empty, the JSON parser is not configured correctly. Open the Parse JSON module and verify that the JSON string field contains the OpenAI response variable. If it contains raw text like `{"score": 8, ...}` instead of a variable reference, you mapped it wrong — clear the field and click to re-map.

## Step 4: Add Routing Logic

Not all leads deserve the same treatment. A lead scored 8-10 should trigger an immediate Slack alert. A lead scored 4-7 should go to a daily digest. A lead scored 1-3 should just be logged.

### Add a Router

Between the Parse JSON module and the Slack module, insert a **Router** module. A Router splits the workflow into multiple paths. You will see two output paths from the Router (labeled 1 and 2). Click the Router and add a third path (click the "+" on the Router).

### Configure Path 1: Hot Lead (Score 8-10)

Click the filter icon (the wrench) on Path 1. Set the condition:
- **Variable:** `5.score` (the parsed score)
- **Operator:** Greater than or equal to
- **Value:** `8`

Connect this path to the existing Slack module. This ensures hot leads get an immediate notification.

### Configure Path 2: Warm Lead (Score 4-7)

Click the filter icon on Path 2. Set the condition:
- **Variable:** `5.score`
- **Operator:** Between
- **Value:** `4` and `7`

Add a **Google Sheets — Add a Row** module on this path. Configure it to add the lead to a different spreadsheet called "Warm Leads Digest." This spreadsheet gets reviewed once daily instead of triggering an immediate alert.

### Configure Path 3: Cold Lead (Score 1-3)

Click the filter icon on Path 3. Set the condition:
- **Variable:** `5.score`
- **Operator:** Less than or equal to
- **Value:** `3`

Add a **Google Sheets — Add a Row** module on this path. Configure it to add the lead to a "Cold Leads Log" spreadsheet. These leads are archived for future reference but no immediate action is taken.

### Test All Three Paths

Add three test rows to your spreadsheet with names that will trigger different scores (a corporate email from a known company will score higher than a generic Gmail address). Run the scenario once for each.

Verify: the high-scoring lead appears in Slack. The medium lead appears in the Warm Leads Digest spreadsheet. The low-scoring lead appears in the Cold Leads Log. Do all three paths work? If any path does not trigger, check the filter conditions — make sure you are comparing numbers to numbers, not strings to numbers. If the score variable is a string type (text), wrap it in a `parseNumber()` function in the filter.

## Step 5: Add Error Handling

This is what separates amateur automations from professional ones. Every production workflow needs error handling, because APIs go down, rate limits get hit, and data comes in unexpected formats.

### Add a Break Handler

Right-click the OpenAI module. Select **Add error handler** → **Break**. A Break module will appear attached to the OpenAI module with a red dotted line.

The Break handler catches any error from the OpenAI module (API timeout, rate limit, invalid response) and stops that specific bundle from proceeding. Without it, a failed OpenAI call would crash the entire scenario.

### Add a Notification for Failed Calls

After the Break module, add a **Slack — Create a Message** module. Configure it to post to a different channel called `#automation-errors`:

```
Lead enrichment failed for:
Name: {{2.name}}
Email: {{2.email}}
Error: {{6.message}}

Action required: Check OpenAI API status and re-run.
```

Now, when OpenAI fails, you get notified instead of the scenario silently crashing. This is how professional automation builders operate — they assume everything will fail eventually and plan for it.

### Add a Retry Mechanism

For transient errors (rate limits, temporary outages), automatic retry is more efficient than manual intervention. Right-click the OpenAI module, select **Settings**, and enable **Automatic retry**. Set it to retry 3 times with a 10-second interval between retries.

With this configuration, most transient failures resolve themselves without any human intervention. The error notification only fires if all 3 retries fail.

## Step 5: Build the Daily Digest Workflow

Create a new scenario (click "Scenarios" in the left sidebar, then "+ New Scenario"). This scenario runs once per day and sends a summary of warm leads.

### Configure the Trigger

Add a **Schedule** trigger. Set it to run every day at 8:00 AM in the client's timezone.

### Fetch Warm Leads

Add a **Google Sheets — Search Rows** module. Configure it to search the "Warm Leads Digest" spreadsheet for rows added in the last 24 hours. Use a date filter on the timestamp column.

### Format the Digest

Add an OpenAI module with this prompt:

```
Format these leads into a clean daily digest email. Group by industry.
Make it scannable — use bullet points, not paragraphs.
Include the lead score and suggested next action for each.

Leads:
{{2.data}}
```

### Send the Email

Add a **Gmail — Send an Email** module. Configure it to send the formatted digest to the client's sales team.

### Test the Daily Digest

Add 3-4 rows to the Warm Leads Digest spreadsheet with today's date. Run the scenario once. Check the recipient's inbox. Do you see a well-formatted digest email? If the email is empty, the Google Sheets search did not find the rows — check your date filter. If the formatting is messy, refine the OpenAI prompt.

## Step 6: Deploy for a Client

When you deliver this automation to a paying client, follow this process:

1. **Duplicate** your working scenario in Make.com (right-click → Clone)
2. **Reconfigure** the cloned scenario with the client's Google Sheets, Slack workspace, and email
3. **Add the client's OpenAI API key** (or use your own and include the cost in your retainer)
4. **Activate** the scenario (toggle the ON/OFF switch in the bottom-left corner from OFF to ON)
5. **Set the schedule** — the lead capture scenario should run every 5 minutes; the digest should run daily at 8 AM
6. **Monitor** for 48 hours — check the execution log (click the scenario name → History tab) for errors

The client should see new lead notifications appearing in Slack within 5 minutes of a form submission. The daily digest should arrive in their inbox at 8 AM sharp.

## Pricing for Client Delivery

| Tier | Setup Fee | Monthly Retainer | What's Included |
|------|-----------|-----------------|-----------------|
| Basic | $1,500 | $200/mo | 1 workflow, error handling, monthly check-in |
| Standard | $3,000 | $400/mo | 3 workflows, AI enrichment, daily digest, weekly optimization |
| Premium | $5,000 | $700/mo | 5+ workflows, custom integrations, real-time monitoring, dedicated Slack channel |

Include the Make.com cost in your retainer. A Standard client uses roughly 5,000-10,000 operations per month. Make.com's Core plan ($9/mo) covers 10,000 operations — your cost is $9, your retainer is $400.

## Cost Breakdown

| Item | Free Tier | Paid Tier | When to Upgrade |
|------|-----------|-----------|-----------------|
| Make.com | 1,000 ops/mo | $9/mo (10K ops) | At first paying client |
| OpenAI API | Pay per use | ~$15-40/mo per client | Scales with usage |
| Google Sheets | Free | Free | — |
| Slack | Free | Free | — |
| Notion (client docs) | Free | $10/mo | At 5+ clients |

**Total monthly cost at 3 clients:** ~$30-60/mo
**Total monthly revenue at 3 clients:** $1,200/mo retainers + setup fees

## Production Checklist

Before activating any workflow for a client:

- [ ] Error handlers are attached to every API module (OpenAI, HTTP requests, third-party APIs)
- [ ] Automatic retry is enabled on modules that call external APIs
- [ ] Error notifications route to a monitored channel (not just your personal email)
- [ ] Router filters are tested with data that matches each path
- [ ] The scenario runs successfully 10 times in a row without errors
- [ ] Rate limiting is accounted for (Make.com has built-in rate limiting, but check API limits too)
- [ ] Sensitive data (API keys, client emails) is not logged in execution history
- [ ] The daily digest arrives at the correct time in the client's timezone
- [ ] The client knows who to contact when something breaks
- [ ] You have a rollback plan (the previous version of the scenario is saved as a backup)

## What to Do Next

Once this workflow is running smoothly, expand your automation portfolio:
- Build a **content distribution engine** — one piece of content, automatically reformatted and posted to LinkedIn, Twitter, email, and Slack
- Build a **client onboarding sequence** — contract signed → welcome email → project setup → team notification
- Build an **e-commerce order pipeline** — Shopify order → fulfillment trigger → customer notification → accounting entry
- Add **Make.com Data Stores** for caching API responses and reducing operations
- Implement **webhook triggers** instead of polling for real-time workflows (webhooks use fewer operations and respond instantly)
