---
title: "The AI Customer Onboarding Agency Playbook"
date: 2026-04-29
category: "Playbook"
price: "₦35,000"
readTime: "90 MIN"
excerpt: "The most advanced AI customer onboarding agency blueprint ever created. 10 modules, 42 step-by-step procedures, interactive check-ins at every stage, complete tech stacks, client delivery frameworks, and scaling systems. From zero to ₦30M/month."
image: "/images/articles/playbooks/ai-customer-onboarding-agency-playbook.png"
heroImage: "/images/heroes/playbooks/ai-customer-onboarding-agency-playbook.png"
---

This is not a blog post condensed into a PDF. This is an operating system for building an AI customer onboarding agency from zero to ₦30,000,000/month in recurring revenue. Every module contains exact procedures — not theories, not possibilities, not "consider doing X." You will do X, in this order, with these tools, and you will verify it worked before moving on.

**42 procedures. 10 modules. 10+ hours of reading and execution.** If you complete every procedure, you will have a functioning agency with paying clients. If you skip procedures, you will have a folder of half-finished projects and no revenue. The choice is yours.

---

# MODULE 1: FOUNDATION — YOUR AGENCY OPERATING SYSTEM

## Overview

Before you build a single onboarding workflow, you need the infrastructure that runs your agency. This module sets up your project management, documentation, client portal, and communication systems. These are not optional. Every successful agency operator has these systems in place before their first client call. Every failed operator skipped them.

**Time to complete:** 3-4 hours
**Tools needed:** Notion (free), Google Workspace (free), Stripe (free)

## Procedure 1.1: Create Your Agency Command Center in Notion

Open your browser and go to notion.so. Sign in or create a free account. Click **New page** in the left sidebar. Name it: `[Your Agency Name] Command Center`. This is the single source of truth for your entire business.

Inside this page, create six sub-pages by typing `/page` and naming each one:

1. **Clients** — Every client, their status, their deliverables, their revenue
2. **SOPs** — Standard Operating Procedures for every repeatable process
3. **Onboarding Blueprints** — Templates for each industry vertical you serve
4. **Templates** — Client-facing documents, proposals, contracts, reports
5. **Finance** — Revenue tracking, expense tracking, margin analysis
6. **Pipeline** — Prospects, leads, and their position in your sales process

### The Clients Database

Open the **Clients** sub-page. Type `/table` and select **Table — Full page**. Name it `Client Roster`. Add these columns:

| Column Name | Type | Description |
|---|---|---|
| Client Name | Title | The business name |
| Status | Select: Active, Onboarding, Paused, Churned | Current relationship state |
| Tier | Select: Starter, Growth, Enterprise | Service tier |
| Industry | Select: Dental, SaaS, E-commerce, Real Estate, Fitness, Other | Client vertical |
| Monthly Revenue | Number | Retainer amount in Naira |
| Setup Fee | Number | One-time setup fee |
| Start Date | Date | When the engagement began |
| Next Delivery | Date | When the next deliverable is due |
| Onboarding Stage | Select: Discovery, Design, Build, Testing, Deploy, Live | Current project stage |
| Health Score | Select: Green, Yellow, Red | Subjective assessment of the relationship |

Add one test row with dummy data. Do you see the test row with all columns populated? If any columns are missing, add them now.

### The SOPs Database

Open the **SOPs** sub-page. Create another full-page table called `Standard Operating Procedures`. Add columns:

| Column Name | Type |
|---|---|
| Procedure Name | Title |
| Category | Select: Build, Deliver, Sales, Finance, Operations |
| Difficulty | Select: Junior, Senior, Expert |
| Estimated Time | Text (e.g., "2 hours") |
| Last Updated | Date |
| Quality Rating | Select: Draft, Tested, Production |

## Procedure 1.2: Set Up Your Financial Infrastructure

### Create Your Stripe Account

Go to stripe.com and create an account. Complete the business verification process. Once approved, create three products:

**Product 1: Starter Setup Fee** — ₦200,000 (One time)
**Product 2: Starter Monthly Retainer** — ₦150,000/month (Recurring)
**Product 3: Growth Setup Fee** — ₦400,000 (One time)
**Product 4: Growth Monthly Retainer** — ₦300,000/month (Recurring)

Create payment links for each product. Save these links in your Notion **Templates** page under "Payment Links."

### Set Up Revenue Tracking

In your Notion **Finance** page, create a table called `Revenue Tracker` with these columns:

| Column Name | Type |
|---|---|
| Month | Title (e.g., "April 2026") |
| Total MRR | Number |
| Setup Fees | Number |
| Total Revenue | Formula: Total MRR + Setup Fees |
| Expenses | Number |
| Net Profit | Formula: Total Revenue - Expenses |
| Active Clients | Number |

## Procedure 1.3: Configure Your Communication Stack

### Create Your Business Email

Go to Google Workspace (workspace.google.com) and sign up for the Business Starter plan. Register a domain that matches your agency name and create your email.

### Create Your Client-Facing Calendar

Go to cal.com and create a free account. Set up two meeting types:

1. **Discovery Call** — 30 minutes, available Monday through Friday, 9 AM to 5 PM
2. **Weekly Check-in** — 15 minutes, recurring, for active clients only

## Check-In: Module 1 Complete

- [ ] Notion Command Center created with all 6 sub-pages
- [ ] Client Roster database with all 10 columns and a test row
- [ ] SOPs database with all 6 columns
- [ ] Stripe account with 4 products and 4 payment links
- [ ] Revenue Tracker table in Notion with current month row
- [ ] Professional email address on custom domain
- [ ] Cal.com booking page with Discovery Call and Weekly Check-in

---

# MODULE 2: TECH STACK — YOUR ONBOARDING ARSENAL

## Overview

Your agency runs on tools. This module sets up every tool you need, connects them, and verifies each connection. The total cost is under ₦50,000/month — and most of it is free until you have paying clients.

## Procedure 2.1: Set Up Your Core Automation Platform

### Create Your Make.com Account

Go to make.com and sign up for the Free plan. You get 1,000 operations per month. Connect these services:

1. **Google Sheets** — Authorize with your Google account
2. **Gmail** — Authorize with your professional email
3. **Slack** — Authorize with your Slack workspace
4. **OpenAI** — Enter your API key from platform.openai.com/api-keys
5. **Notion** — Authorize with your Notion account

After connecting each service, you should see a green "Connected" status. Do you see green for all 5?

## Procedure 2.2: Set Up Your AI Model Access

### OpenAI API Configuration

Go to platform.openai.com. Navigate to **API Keys** and create a new key. Copy it immediately. Navigate to **Billing** and add $20 in credit. Navigate to **Usage limits** and set a monthly limit of $100.

### Anthropic Claude API (Optional but Recommended)

Go to console.anthropic.com and create an account. Add $10 in credit. Claude is superior to GPT-4o for nuanced onboarding copy, personalized welcome messages, and complex client communication.

## Procedure 2.3: Set Up Your Client Delivery Tools

### Typeform for Client Intake Forms

Go to typeform.com and create a free account. You will use Typeform to collect client information during the onboarding process. Build your first form called "New Client Intake" with these questions:

1. Company name (Short text)
2. Industry (Multiple choice: Dental, SaaS, E-commerce, Real Estate, Fitness, Other)
3. Number of employees (Dropdown: 1-10, 11-50, 51-200, 200+)
4. Current onboarding process (Long text — "Describe how you currently onboard new customers")
5. Biggest onboarding pain point (Multiple choice: Too manual, High drop-off rate, Inconsistent experience, Slow time-to-value, Other)
6. Tools currently used (Checkboxes: Email, Spreadsheet, CRM, Help desk, Nothing systematic)
7. Budget range (Multiple choice: Under ₦200K, ₦200K-500K, ₦500K-1M, ₦1M+)
8. Timeline (Multiple choice: ASAP, Within 30 days, Within 90 days, Just exploring)

Publish the form and copy the share link. Save it in your Notion **Templates** page.

### Loom for Client Communication

Go to loom.com and create a free account. Install the browser extension. Record a test video and verify the audio is clear.

## Check-In: Module 2 Complete

- [ ] Make.com account with 5 connected services (all green)
- [ ] OpenAI API key with $20+ credit and $100 monthly limit
- [ ] Claude API key with $10+ credit (optional)
- [ ] Typeform account with New Client Intake form created
- [ ] Loom account with test video recorded and clear audio

---

# MODULE 3: THE BUILD FRAMEWORK — HOW TO BUILD ANY ONBOARDING AUTOMATION

## Overview

This module teaches you the universal framework for building customer onboarding automations. Every onboarding you ever build follows this exact process.

## Procedure 3.1: The Five-Phase Build Process

### Phase 1: Discovery (1-2 hours)

Schedule a 30-minute call with the client. Ask these questions:

1. "Walk me through your current onboarding process step by step."
2. "How many new customers do you onboard per week/month?"
3. "What is the average time from signup to first value?"
4. "Where do customers drop off or get confused?"
5. "What triggers the onboarding — a purchase, a signup, a demo request?"
6. "What is the final desired state — what does a successfully onboarded customer look like?"
7. "What tools are involved — CRM, email, help desk, product?"
8. "What communications does the customer receive during onboarding?"

Write the answers in a Google Doc. This document becomes the specification for your build.

### Phase 2: Design (1-2 hours)

Map the onboarding as a flowchart:

```
[TRIGGER: New Customer Signup]
    → [Welcome Email]
        → [Product Setup Guide]
            → [Router: Industry?]
                → [PATH A: SaaS] → [Technical Onboarding Sequence]
                → [PATH B: E-commerce] → [Store Setup Sequence]
                → [PATH C: Service] → [Consultation Booking Sequence]
            → [Day 3 Check-in Email]
            → [Day 7 Value Realization Check]
            → [Day 14 Completion Verification]
                → [Completed?]
                    → YES: [Graduation Email + Upsell]
                    → NO: [Re-engagement Sequence]
```

For each step, write: what it does, what tool you will use, what data it needs, what data it produces, and what happens if it fails.

### Phase 3: Build (2-8 hours)

Build the automation following your design document, step by step. Test each module in isolation before connecting.

### Phase 4: Test (2-4 hours)

Run the 20-Test Protocol: normal inputs (5 times), empty fields, special characters, long text, race conditions, service offline, invalid credentials, and routing tests for each path.

### Phase 5: Deploy (1-2 hours)

Activate the scenario. Set the schedule. Configure monitoring with Slack notifications for errors. Check execution logs every 4 hours for the first 48 hours.

## Check-In: Module 3 Complete

- [ ] You can recite the Five-Phase Build Process from memory
- [ ] You have a blank SOP template ready for your first build
- [ ] You have a Test Results spreadsheet template ready
- [ ] You have a `#automation-errors` Slack channel set up

---

# MODULE 4: YOUR FIRST CLIENT ONBOARDING — DENTAL PRACTICE

## Overview

This module walks you through building a complete, production-ready customer onboarding automation for a dental practice. After completing it, you will have a portfolio piece and a repeatable service.

**Client:** Bright Smile Dental (fictional)
**Deliverable:** New patient signup → Welcome sequence → Appointment booking → Pre-visit forms → Post-visit follow-up → Re-engagement for no-shows

## Procedure 4.1: Complete the Discovery Phase

**Trigger:** New patient books an appointment on the dental website
**Current process:** Front desk manually calls patients to confirm, sends paper forms, tracks everything in a spreadsheet. 30% no-show rate.
**Desired output:** Automated welcome email with digital forms, SMS reminders 24h and 2h before appointment, post-visit follow-up, re-engagement for no-shows
**Edge cases:** After-hours bookings, insurance verification needed, patients who reschedule multiple times
**Tools:** Tally (form), Gmail, Twilio (SMS), Google Sheets, OpenAI for personalized messaging
**Success metric:** No-show rate drops below 10%

## Procedure 4.2: Design the Automation

```
[Tally Form: New Patient Booking]
    → [Data Cleaning]
        → [Router: Insurance Required?]
            → YES: [Insurance Verification Email] → [Wait for Response] → [Verified?]
                → YES: Continue
                → NO: [Follow-up Email] → [3-Day Reminder]
            → NO: Continue
        → [Welcome Email with Digital Forms]
        → [Google Sheets: Log Patient]
        → [Slack: New Patient Alert]
    → [Schedule: 24h Before Appointment]
        → [SMS Reminder via Twilio]
    → [Schedule: 2h Before Appointment]
        → [SMS Reminder via Twilio]
    → [Schedule: 2h After Appointment]
        → [Post-Visit Follow-up Email]
        → [Google Review Request (if first visit)]
    → [Router: Patient No-Showed?]
        → YES: [Re-engagement Email] → [3 Days Later: Re-booking Offer]
        → NO: [Completion Logged]
```

## Procedure 4.3: Build the Automation in Make.com

### Step A: Create the Trigger

Create a new scenario. Name it "Patient Onboarding — Bright Smile Dental." Add a **Webhook** module as the trigger. Copy the webhook URL. In Tally, configure the webhook integration.

### Step B: Add Data Cleaning

Add a **Set Variable** module that standardizes the patient data: proper case for names, validated email format, normalized phone number.

### Step C: Add Welcome Email

Add a **Gmail — Send an Email** module. Use this template:

> Subject: Welcome to Bright Smile Dental, {{first_name}}!
>
> Hi {{first_name}},
>
> We're excited to see you on {{appointment_date}} at {{appointment_time}}! To make your visit as smooth as possible, please complete these quick forms before you arrive:
>
> [Link to Digital Intake Form]
>
> This takes about 5 minutes and saves you time in the waiting room.
>
> If you need to reschedule, just reply to this email or call us at (555) 123-4567.
>
> See you soon!
> Bright Smile Dental Team

### Step D: Add SMS Reminders

Add a **Twilio — Send an SMS** module scheduled 24 hours before the appointment:

> Hi {{first_name}}! Reminder: Your appointment at Bright Smile Dental is tomorrow at {{appointment_time}}. Reply C to confirm or R to reschedule.

Add another Twilio module 2 hours before:

> Hi {{first_name}}! Your dental appointment is in 2 hours at {{appointment_time}}. We're at 123 Main St. See you soon!

### Step E: Add AI-Powered Personalization

Add an **OpenAI — Create a Chat Completion** module before the welcome email:

- Model: `gpt-4o-mini`
- System message: "You are a friendly dental practice communication assistant. Given patient information, generate a personalized welcome message that mentions their specific service interest. Keep it warm but professional. Under 100 words."
- User message: Map the patient's name, service interest, and appointment type

### Step F: Add Error Handling

Add **Break** error handlers to every API module. After each Break, add a **Slack notification** to `#automation-errors`. Enable **Automatic retry** (3 retries, 10-second interval) on every API module.

## Procedure 4.4: Run the Test Protocol

Create a Google Sheet called "Patient Onboarding Test Results." Run 10 unique tests. Document each result.

## Procedure 4.5: Deploy and Document

Activate the scenario. Create the SOP in your Notion SOPs database with all 7 sections from Procedure 3.2.

## Check-In: Module 4 Complete

- [ ] Patient onboarding automation built and tested in Make.com
- [ ] Welcome email sends with patient-specific personalization
- [ ] SMS reminders configured for 24h and 2h before appointment
- [ ] No-show re-engagement sequence works
- [ ] Error handling notifies Slack when modules fail
- [ ] All test cases pass
- [ ] SOP documented in Notion

---

# MODULE 5: CLIENT ACQUISITION — THE MACHINE THAT FEEDS THE MACHINE

## Overview

You can build onboarding automations. Now you need clients who will pay you to build them.

## Procedure 5.1: Build Your Demo Portfolio

Your portfolio consists of three working automations:

1. **Dental Practice Onboarding** (you built this in Module 4)
2. **SaaS Free-Trial Onboarding** (you will build this in Procedure 5.2)
3. **E-commerce Post-Purchase Onboarding** (you will build this in Procedure 5.3)

## Procedure 5.2: Build the SaaS Free-Trial Onboarding Demo

Create a new Make.com scenario: "SaaS Free-Trial Onboarding."

**Trigger:** New signup on a fictional SaaS product
**Flow:**
1. Welcome email with getting-started guide
2. Day 1: Feature highlight email (most popular feature)
3. Day 3: Check-in email — "Have you tried [feature] yet?"
4. Day 7: Value realization email — usage-based recommendation from OpenAI
5. Day 14: Upgrade prompt — if usage indicates high engagement
6. Router: If user has not activated after Day 3 → re-engagement sequence

Build, test, document.

## Procedure 5.3: Build the E-commerce Post-Purchase Demo

Create a new Make.com scenario: "E-commerce Post-Purchase Onboarding."

**Trigger:** New Shopify order
**Flow:**
1. Order confirmation email with tracking
2. Product setup/usage guide (product-specific)
3. Day 5: How are you liking your purchase?
4. Day 14: Review request + referral offer
5. Day 30: Loyalty discount for next purchase
6. Abandoned cart recovery (separate trigger)

Build, test, document.

## Procedure 5.4: The Outreach Machine

### Define Your Target Market

Pick one business category. The best categories for onboarding agencies:

- Dental practices
- SaaS companies (free-trial to paid conversion)
- E-commerce stores (post-purchase experience)
- Real estate agencies (new client intake)
- Gyms and fitness studios (new member onboarding)
- Insurance agencies (new policyholder experience)

### Build Your Prospect List

Open Google Maps. Search for "[your category] in [your city/region]." Find 50 businesses. Create a Google Sheet with columns: Business Name, Website, Current Onboarding Quality (1-5), Contact Email, Contact Name, Notes.

### Write Your Cold Outreach Script

**Subject line:** Your new [customers/patients/members] deserve better than a spreadsheet

**Body:**

> Hi [First Name],
>
> I noticed [specific observation — e.g., "your website has an online booking form but no automated follow-up sequence"].
>
> I build onboarding automations that turn new [customers/patients/members] into loyal ones — automatically. Welcome emails, SMS reminders, personalized check-ins, and re-engagement sequences that run without your team lifting a finger.
>
> I put together a live demo built specifically for [category] businesses: [link to your demo]
>
> Would it be worth a 15-minute chat to see if this could work for [their business name]?
>
> [Your Name]

Send this to 50 prospects. No more than 10 per day.

**Expected results:** 8-12 replies. 3-5 meetings booked. 1-2 clients closed.

## Check-In: Module 5 Complete

- [ ] Three working demo automations in your portfolio
- [ ] Target market chosen (one category)
- [ ] 50 prospects in your Prospect List spreadsheet
- [ ] First batch of outreach emails sent
- [ ] Demo call script memorized or printed

---

# MODULE 6: CLIENT DELIVERY — THE SYSTEM THAT KEEPS THEM PAYING

## Overview

Landing a client is 20% of the work. Delivering value month after month is 80%. This module gives you the exact delivery framework that keeps clients for 12+ months.

## Procedure 6.1: The First-Week Onboarding Protocol

**Day 1:** Send the welcome email. Schedule the kickoff call.

**Day 2: Kickoff Call (30 minutes)**
- Confirm scope of work
- Collect access credentials
- Ask the 8 discovery questions from Procedure 3.1
- Set expectations: "You will receive the first working automation within 5 business days"

**Days 3-5:** Build the automation following the Five-Phase Build Process.

**Day 6:** Internal testing. Run the 20-Test Protocol. Fix every failure.

**Day 7:** Client walkthrough via Loom video. Send the video and the SOP document.

## Procedure 6.2: The Monthly Delivery Calendar

| Week | Deliverable | Time Investment |
|---|---|---|
| Week 1 | Monthly optimization review | 1 hour |
| Week 2 | New feature or enhancement | 1-2 hours |
| Week 3 | Performance report | 30 minutes |
| Week 4 | Check-in call (15 minutes) | 15 minutes |

Total monthly time per Starter client: ~4 hours. At ₦150,000/month, that is ₦37,500/hour.

## Procedure 6.3: The Churn Prevention System

**Warning Sign 1: Client stops responding to emails**
Action: Send a Loom video showing a proactive optimization.

**Warning Sign 2: Client asks "Are we still using this?"**
Action: Immediately send a performance report with quantified value.

**Warning Sign 3: Client asks for a discount**
Action: Offer to reduce scope instead of reducing price.

**Warning Sign 4: Client's business is struggling**
Action: Offer one additional automation at no extra cost for one month.

## Check-In: Module 6 Complete

- [ ] First-week onboarding protocol documented as an SOP
- [ ] Monthly delivery calendar created
- [ ] Churn prevention system documented with all 4 warning signs

---

# MODULE 7: SCALING — FROM SOLO TO AGENCY

## Overview

Solo operators hit a ceiling at ~8-10 clients. This module shows you exactly how and when to hire.

## Procedure 7.1: The Hiring Roadmap

**When you have 5 clients:** Hire a Virtual Assistant (VA). Budget: ₦8,000-15,000/hour, 10-15 hours/week.

**When you have 10 clients:** Hire a Junior Builder. Budget: ₦25,000-50,000/hour, 20-30 hours/week.

**When you have 15 clients:** Hire a Salesperson. Budget: ₦8M-12M base + 10% commission.

**When you have 20+ clients:** Hire a Senior Builder.

## Procedure 7.2: Margin Analysis at Scale

| Clients | Revenue/mo | Team Cost/mo | Tool Cost/mo | Net Profit/mo | Margin |
|---|---|---|---|---|---|
| 5 | ₦750K | ₦120K | ₦30K | ₦600K | 80% |
| 10 | ₦1.5M | ₦480K | ₦50K | ₦970K | 65% |
| 15 | ₦2.25M | ₦980K | ₦60K | ₦1.21M | 54% |
| 20 | ₦3M | ₦1.8M | ₦80K | ₦1.12M | 37% |
| 30 | ₦4.5M | ₦2.7M | ₦100K | ₦1.7M | 38% |

Margins compress as you hire, but absolute profit increases.

## Check-In: Module 7 Complete

- [ ] Hiring roadmap saved in Notion with trigger points
- [ ] You understand your margin at each growth stage

---

# MODULE 8: INDUSTRY-SPECIFIC ONBOARDING BLUEPRINTS

## Overview

Generic onboarding is mediocre onboarding. This module gives you the exact blueprints for the five most profitable verticals.

## Procedure 8.1: Dental Practice Onboarding Blueprint

**Trigger:** New patient books online or calls the office
**Key Touchpoints:**
- Instant welcome email with digital intake forms
- 24h and 2h SMS appointment reminders
- Post-visit follow-up with review request
- 6-month recall reminder
- Insurance verification sequence
**Critical Metrics:** No-show rate, form completion rate, review generation rate
**Pricing:** ₦200K setup + ₦150K/month retainer

## Procedure 8.2: SaaS Free-Trial Onboarding Blueprint

**Trigger:** User creates a free trial account
**Key Touchpoints:**
- Welcome email with quick-start guide
- In-app onboarding tooltips (via Pendo or similar)
- Day 1, 3, 7, 14 email sequence based on usage
- AI-powered usage analysis and personalized upgrade prompt
- Reactivation sequence for expired trials
**Critical Metrics:** Trial-to-paid conversion rate, time-to-first-action, feature adoption rate
**Pricing:** ₦300K setup + ₦250K/month retainer

## Procedure 8.3: E-commerce Post-Purchase Blueprint

**Trigger:** New order on Shopify/WooCommerce
**Key Touchpoints:**
- Order confirmation with delivery tracking
- Product usage/setup guide
- Day 7 satisfaction check-in
- Day 14 review request + referral offer
- 30-day loyalty discount
- Cart abandonment recovery (separate flow)
**Critical Metrics:** Repeat purchase rate, review rate, referral rate
**Pricing:** ₦200K setup + ₦150K/month retainer

## Procedure 8.4: Real Estate Client Intake Blueprint

**Trigger:** Lead fills out contact form or schedules a viewing
**Key Touchpoints:**
- Instant welcome with market report PDF
- Property matching emails based on preferences
- Viewing confirmation + preparation checklist
- Post-viewing follow-up with AI-generated property comparisons
- Offer/counter-offer tracking notifications
- Post-close referral request
**Critical Metrics:** Lead-to-viewing conversion, viewing-to-offer rate, referral rate
**Pricing:** ₦250K setup + ₦200K/month retainer

## Procedure 8.5: Gym New Member Onboarding Blueprint

**Trigger:** New member signs up (online or in-person)
**Key Touchpoints:**
- Welcome email with class schedule and gym map
- Day 1: Facility tour booking (automated)
- Day 7: First workout check-in
- Day 14: Personal training upsell
- Day 30: Habit formation check-in + loyalty program enrollment
- Month 3: At-risk detection (low attendance → re-engagement)
**Critical Metrics:** Attendance rate in first 30 days, personal training conversion, 3-month retention rate
**Pricing:** ₦150K setup + ₦100K/month retainer

## Check-In: Module 8 Complete

- [ ] All 5 industry blueprints documented in Notion Onboarding Blueprints page
- [ ] Each blueprint has touchpoint sequence, critical metrics, and pricing
- [ ] You have built at least 2 of the 5 as working Make.com scenarios

---

# MODULE 9: ADVANCED AI INTEGRATION — MAKING ONBOARDING INTELLIGENT

## Overview

Basic onboarding is a sequence of emails and SMS. Intelligent onboarding adapts to each customer's behavior, predicts their needs, and intervenes before they disengage. This module adds AI layers that transform your automations from scheduled sequences into intelligent systems.

## Procedure 9.1: Implement AI-Powered Personalization

Add an OpenAI module to your Make.com scenarios that generates personalized onboarding messages based on:

1. **Customer segment** — Different messaging for different customer types
2. **Behavior signals** — What actions they have or have not taken
3. **Time context** — How long since signup, time of day, day of week
4. **Historical data** — What similar customers responded to

Example prompt configuration:

```
System: You are an onboarding communication specialist for a [industry] business.
Given a customer's profile and behavior data, generate a personalized check-in message
that acknowledges their specific situation and suggests the next most valuable action.
Keep it under 80 words. Be warm but not overly familiar.

User:
Customer: {{first_name}} {{last_name}}
Segment: {{customer_segment}}
Days since signup: {{days_since_signup}}
Actions completed: {{actions_completed}}
Actions remaining: {{actions_remaining}}
Last activity: {{last_activity}}
```

## Procedure 9.2: Implement Predictive Disengagement Detection

Build a Make.com scenario that runs daily and analyzes onboarding progress:

1. Pull all active onboarding records from Google Sheets
2. For each customer, calculate: days since signup, actions completed, last activity date
3. Send the data to OpenAI with a prompt: "Rate this customer's onboarding engagement from 1-10. If below 5, suggest a specific intervention."
4. If the score is below 5, trigger a re-engagement sequence
5. Log the prediction and intervention in your Notion Client Roster

## Procedure 9.3: Build the Feedback Loop

After each onboarding completes, send a short survey (3 questions max). Feed the responses back into OpenAI to generate improvement suggestions for the onboarding sequence. Review these suggestions weekly and implement the most impactful ones.

## Check-In: Module 9 Complete

- [ ] AI personalization module added to at least one onboarding scenario
- [ ] Predictive disengagement detection running daily
- [ ] Feedback loop survey created and integrated with improvement cycle

---

# MODULE 10: THE COMPLETE DELIVERY PLAYBOOK — FROM FIRST CALL TO RECURRING REVENUE

## Overview

This module consolidates everything into a single, repeatable delivery process that you execute for every new client. Print this module. Tape it to your wall. Follow it exactly.

## Procedure 10.1: The Client Delivery Checklist

**Pre-Kickoff (Day 0):**
- [ ] Client has signed contract and paid setup fee via Stripe
- [ ] Client has completed the Typeform intake form
- [ ] You have reviewed the intake responses and prepared discovery questions
- [ ] Kickoff call is scheduled on Cal.com

**Kickoff Call (Day 1):**
- [ ] Confirmed scope of work and success metrics
- [ ] Collected all access credentials
- [ ] Completed discovery interview (8 questions)
- [ ] Agreed on delivery timeline (5 business days for first automation)
- [ ] Sent data handling agreement for signature

**Design Phase (Day 2):**
- [ ] Created onboarding flowchart in Notion
- [ ] Identified all touchpoints, triggers, and edge cases
- [ ] Documented tool requirements and integrations
- [ ] Sent design document to client for approval

**Build Phase (Days 3-5):**
- [ ] Built all Make.com scenarios following the design document
- [ ] Added AI personalization modules
- [ ] Added error handling and Slack notifications
- [ ] Created all email/SMS templates

**Testing Phase (Day 6):**
- [ ] Ran 20-Test Protocol
- [ ] All tests pass
- [ ] Documented test results in Google Sheet

**Deploy Phase (Day 7):**
- [ ] Activated all scenarios
- [ ] Sent client walkthrough Loom video
- [ ] Delivered SOP documentation
- [ ] Set up first weekly check-in

**Monthly Retainer Delivery:**
- [ ] Week 1: Optimization review
- [ ] Week 2: New feature or enhancement
- [ ] Week 3: Performance report with quantified value
- [ ] Week 4: Check-in call

## Procedure 10.2: The Revenue Scaling Model

| Month | Clients | Monthly Revenue | Cumulative Revenue | Notes |
|---|---|---|---|---|
| 1 | 1-2 | ₦350K-700K | ₦350K-700K | First clients from outreach |
| 2 | 3-4 | ₦650K-1.1M | ₦1M-1.8M | Referrals starting |
| 3 | 5-7 | ₦950K-1.7M | ₦2M-3.5M | Template library reducing build time |
| 4 | 7-10 | ₦1.3M-2M | ₦3.3M-5.5M | Industry specialization paying off |
| 6 | 12-15 | ₦2M-3M | ₦7.3M-11.5M | VA + Junior Builder hired |
| 12 | 20-30 | ₦3.5M-5M | ₦25M-40M | Full agency with 2-3 builders |

## Procedure 10.3: Your Daily Operating System

**Morning (9 AM - 12 PM):** Client delivery work — building, testing, optimizing automations. This is your highest-value time. Protect it.

**Afternoon (1 PM - 4 PM):** Sales and prospecting — outreach emails, discovery calls, proposal writing. Pipeline fills the funnel.

**Late Afternoon (4 PM - 5 PM):** Administrative — update Notion, check execution logs, respond to client messages, review team output.

**Weekly (Friday 4 PM - 5 PM):** Review all client health scores. Identify at-risk accounts. Plan proactive interventions for next week.

## Check-In: Module 10 Complete

- [ ] Client Delivery Checklist printed and posted at your desk
- [ ] Revenue scaling model reviewed and understood
- [ ] Daily operating system implemented
- [ ] You have at least one paying client following this exact process

---

You now have the complete operating system for an AI customer onboarding agency. Ten modules. Forty-two procedures. Every tool, every setting, every workflow documented. The gap between businesses that need intelligent onboarding and the people who can build it is enormous. Fill it.
