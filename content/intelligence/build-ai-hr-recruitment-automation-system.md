---
title: "Build and Automate an AI HR & Recruitment System with Greenhouse, Lever, and Make.com"
date: 2026-05-02
category: "Implementation"
difficulty: "INTERMEDIATE"
readTime: "24 MIN"
excerpt: "The complete execution guide for building an AI recruitment pipeline. From job description optimization to resume screening to interview scheduling to candidate matching dashboards."
image: "/images/articles/intelligence/build-ai-hr-recruitment-automation-system.png"
heroImage: "/images/heroes/intelligence/build-ai-hr-recruitment-automation-system.png"
relatedOpportunity: "/opportunities/ai-hr-recruitment-automation-agency/"
relatedPlaybook: "/playbooks/ai-hr-recruitment-automation-playbook/"
---

Manual recruitment is for agencies that want to stay small forever. If you want to run an AI recruitment operation that generates $10,000+/month in recurring revenue, you need an automated engine that imports applications, screens them with AI, schedules interviews, generates customized interview guides, and delivers pipeline analytics — all without you touching a keyboard after the initial setup. This guide is the technical implementation manual. Follow every step in order. Skip nothing. If you skip the screening prompt engineering, your AI advances unqualified candidates that waste your client's time. If you skip the bias audit, your AI perpetuates existing hiring inequalities that expose your clients to legal risk. Every step exists because someone lost a client by skipping it.

This guide assumes you have zero infrastructure set up. By the end, you will have a fully automated pipeline that can handle 10+ clients simultaneously with minimal manual intervention.

## Prerequisites

Before you start, you need the following:

- **Greenhouse or Lever** — Free trial (greenhouse.io or lever.co)
- **Make.com** — $16/mo (Teams plan for 10,000 operations/month)
- **OpenAI API key** — $10 credit minimum (platform.openai.com/api-keys)
- **Google Workspace** — $6/mo for professional email and Sheets access
- **Cal.com** — Free (scheduling automation)
- **Notion** — Free (client dashboards and documentation)
- **6-8 hours of uninterrupted time** for initial setup

Total upfront cost: $32/mo + $10 API credit. A single client at $1,000/month covers this 25x over.

## Step 1: Set Up Your Applicant Tracking System Integration

This is the most critical step. Without a reliable connection to your client's ATS, nothing else works. You have two primary options: Greenhouse (most popular for structured hiring) and Lever (best for candidate relationship management). Set up both so you can serve any client.

### Sub-step 1a: Greenhouse Setup

Go to greenhouse.io and sign up for a free trial. Create your first test job posting: "Senior Product Manager — Test Client." Add these pipeline stages: Application Received → AI Pre-Screen → Phone Screen → Assessment → Interview Panel → Offer.

Navigate to **Dev Tools** → **API Credentials**. Create a Harvest API key with permissions: Candidates (read/write), Applications (read/write), Jobs (read), and Stages (read). Copy the API key and store it securely.

### Sub-step 1b: Connect Greenhouse to Make.com

Open Make.com. Go to **Connections** → **Add connection**. Search for "Greenhouse" and enter your API key. Click **Connect** — the connection should show a green "Connected" status.

Verify the connection works: create a test scenario with Greenhouse "List Candidates" module — it should return your test candidates.

### Sub-step 1c: Lever Setup (Alternative/Additional)

If you also want Lever capability, go at lever.co and sign up for a trial. Create an API key in Settings → Integrations → API. In Make.com, add a Lever connection using your API credentials.

### Step 1 Check-In

Verify each of these before moving on:
1. ATS account is active with a test job posting created
2. API credentials generated and stored securely
3. Make.com ATS connection shows green "Connected" status
4. Test API call works: List Candidates returns test data
5. (Optional) Second ATS connection also shows green

## Step 2: Build the AI Resume Screening Engine

This is the heart of your recruitment automation. The screening engine takes incoming applications, sends them to OpenAI with the job requirements and a structured evaluation rubric, and routes candidates into the appropriate pipeline stage. When it works, you screen 1,000 applicants in 10 minutes. When it fails, you advance unqualified candidates that waste everyone's time.

### Sub-step 2a: Create the Role Specification Reference

In Google Sheets, create a spreadsheet called "Role Spec — [Client Name]." This sheet stores the job requirements in a format the AI can understand.

Column A: Requirement | Column B: Type (Required/Preferred) | Column C: Weight (1-5) | Column D: Evaluation Criteria

Example rows:

| Requirement | Type | Weight | Evaluation Criteria |
|---|---|---|---|
| 5+ years product management experience | Required | 5 | Look for PM titles, product launches, roadmap ownership |
| B2B SaaS experience | Required | 4 | Company types, product categories, customer segments |
| Data analysis skills | Required | 3 | SQL, analytics tools, A/B testing, metric ownership |
| Technical background | Preferred | 2 | Engineering degree, technical PM roles, API product experience |
| MBA or advanced degree | Preferred | 1 | Not required but signals analytical rigor |

Fill in 10-15 requirements that match the client's actual job. The weights are critical — they tell the AI which criteria matter most for the overall score. Without weights, the AI treats all requirements equally, which reduces screening accuracy by 20-30%.

### Sub-step 2b: Build the Make.com Screening Workflow

Create a new Make.com scenario called "AI Screening — [Client Name]":

1. **Trigger:** Greenhouse — "Watch Applications" (polls every 2 hours for new applications). Filter for applications in "Application Received" stage.

2. **Module 1 — Google Sheets "Search Rows":** Look up the Role Specification. This pulls the full requirements list so the AI knows what to evaluate against.

3. **Module 2 — OpenAI "Create a Chat Completion":**
   - Model: `gpt-4o`
   - System message:

```
You are a senior technical recruiter evaluating candidates for a specific role. Given a resume and a job specification with weighted requirements, evaluate the candidate's fit.

Respond ONLY in valid JSON:
{
  "overall_score": 0-100,
  "skills_match": 0-100,
  "experience_match": 0-100,
  "culture_signal": 0-100,
  "red_flags": [],
  "strengths": [],
  "recommended_action": "ADVANCE|PHONE_SCREEN|MANUAL_REVIEW|REJECT",
  "reasoning": "2-3 sentence explanation",
  "deal_breaker_flags": [],
  "salary_estimate": "range based on experience",
  "screening_notes": "specific observations about the candidate"
}

Scoring rules:
- Weight each requirement by its assigned weight when calculating overall_score
- A single deal-breaker (required requirement not met) sets recommended_action to "REJECT" regardless of overall score
- Score 80+ = ADVANCE (strong candidate, fast-track)
- Score 60-79 = PHONE_SCREEN (promising, needs validation)
- Score 40-59 = MANUAL_REVIEW (borderline, human judgment needed)
- Score below 40 = REJECT (does not meet minimum requirements)
- Never score based on: university prestige, age, gender, or name origin
- Flag employment gaps > 6 months as red_flags
- Flag 3+ jobs in 2 years as a red_flag
```

   - User message:

```
Job Title: {{job_title}}
Role Specification: {{1.values}}
Resume Text: {{resume_text}}
Cover Letter: {{cover_letter}}
Source: {{source}}
```

4. **Module 3 — Parse JSON:** Convert the OpenAI response into structured variables

5. **Module 4 — Router:**
   - **Path A (ADVANCE):** Greenhouse → Move to "AI Pre-Screen Passed" + Gmail → Send advancement email + Slack → Notify #candidate-alerts
   - **Path B (PHONE_SCREEN):** Greenhouse → Move to "Phone Screen" + Gmail → Send scheduling email with Cal.com link
   - **Path C (MANUAL_REVIEW):** Greenhouse → Move to "Manual Review" + Google Sheets → Add to Review Queue + Slack → Summary to #candidate-alerts
   - **Path D (REJECT):** Greenhouse → Move to "Rejected" + Gmail → Send respectful rejection email

6. **Module 5 — Error Handler:** On any OpenAI failure, add Break (3 retries, 30-second interval) + Slack notification

### Sub-step 2c: Test the Screening Engine

Submit 10 test applications through your ATS with varying quality levels. Include a strong fit, a moderate fit, a career changer, an underqualified candidate, and an overqualified candidate. Run the Make.com scenario once.

Check the ATS: do the candidates appear in the correct pipeline stages? Check the Review Queue: are borderline candidates flagged for manual review? Check Slack: did error notifications appear?

Expected results: 8-9 out of 10 candidates routed correctly. 1-2 flagged for manual review. If more than 2 are misrouted, improve your Role Specification weights. If none are flagged for manual review, your thresholds are too permissive.

### Step 2 Check-In

1. Role Specification sheet created with 10+ requirements and weights
2. Screening workflow processes test applications correctly
3. AI routing accuracy is 85%+ on test data
4. All four routing paths function correctly
5. Error handling catches API failures and notifies Slack

## Step 3: Build the Interview Scheduling and Guide System

Screening is useless if qualified candidates sit in the pipeline without interviews being scheduled. This module automates the scheduling process and generates customized interview guides that help interviewers ask targeted questions.

### Sub-step 3a: Create the Scheduling Automation

Create a new scenario: "Interview Scheduling — [Client Name]"

1. **Trigger:** Greenhouse — "Watch Stage Changes" (when candidate moves to "Phone Screen")
2. **Module 1:** Cal.com → Get available slots for the next 7 days
3. **Module 2:** Gmail → Send scheduling email to candidate with booking link
4. **Module 3:** Cal.com → Watch for confirmed bookings
5. **Module 4:** Greenhouse → Update candidate with interview date/time
6. **Module 5:** Gmail → Send calendar invite to the interviewer

### Sub-step 3b: Build the Interview Guide Generator

Create a second scenario: "Interview Guide — [Client Name]"

1. **Trigger:** Cal.com → Booking confirmed
2. **Module 1:** Greenhouse → Pull the candidate's resume and AI scorecard
3. **Module 2:** OpenAI → Generate customized interview guide

System prompt:
```
You are a senior hiring manager preparing for an interview. Given a candidate's resume, their AI evaluation scorecard, and the job requirements, create a focused interview guide.

Include:
1. Opening question (icebreaker based on something specific in their background)
2. 5 targeted questions (based on skills gaps or areas that need validation from the scorecard)
3. 2 behavioral questions (STAR format, probing specific past experiences)
4. 1 challenge question (a real problem the hire would face in this role)
5. Red flag probes (questions to investigate concerns from the scorecard)
6. Culture fit assessment (2 questions about work style and values)

Keep the guide to one page. The interviewer should be able to scan it in 60 seconds.
```

4. **Module 3:** Notion → Create a page in the client's Interview Guides database
5. **Module 4:** Gmail → Send the guide to the interviewer 2 hours before the scheduled call

### Step 3 Check-In

1. Scheduling automation sends candidates booking links within minutes of advancement
2. Confirmed bookings update the ATS automatically
3. Interview guides are generated and delivered for each scheduled interview
4. Guides contain targeted questions based on the candidate's specific scorecard
5. The system handles rescheduling and cancellations gracefully

## Step 4: Build the Candidate Matching and Pipeline Analytics System

This module builds the AI candidate matching system that goes beyond keyword matching and the analytics dashboard that proves your value to clients.

### Sub-step 4a: Create the Candidate Matching Database

Create a Google Sheet called "Candidate Pool — [Client Name]" with these columns:

| Column | Type |
|---|---|
| Candidate ID | Text |
| Name | Text |
| Primary Skills | Text (comma-separated) |
| Years of Experience | Number |
| Industry | Text |
| Current Role | Text |
| Career Level | Text (Junior/Mid/Senior/Executive) |
| AI Score | Number |
| Status | Text (Available, Placed, Unresponsive) |
| Last Contacted | Date |
| Notes | Text |

Populate this database with all candidates who scored above 40 on any screening — even those who were not selected for the current role. These candidates are your client's talent pool for future openings.

### Sub-step 4b: Build the Smart Matching Workflow

Create a new scenario: "Smart Matching — [Client Name]"

1. **Trigger:** New job requirement entered (Google Sheets or Notion form)
2. **Module 1:** OpenAI → Analyze the job requirements against the Candidate Pool

System prompt:
```
You are an expert talent matcher. Given a new job opening and a pool of pre-screened candidates, identify the top 5 candidates who best fit the role.

Consider:
1. Direct skills match (40% weight)
2. Experience level alignment (25% weight)
3. Career trajectory compatibility (15% weight)
4. Previous AI screening scores (10% weight)
5. Logistics compatibility (availability, location — 10% weight)

For each recommended candidate, explain:
- Why they fit (specific skills and experiences)
- Potential concerns (gaps or mismatches)
- Suggested interview focus areas
```

3. **Module 2:** Notion → Create a "Match Report" page
4. **Module 3:** Gmail → Send the match report to the client

### Sub-step 4c: Build the Pipeline Analytics Dashboard

Create a Notion dashboard for each client with these components:

- **Pipeline Funnel:** Applications → Screened → Phone Screen → Interview → Offer → Hired
- **Key Metrics:** Time-to-fill, Screening accuracy rate, Offer acceptance rate, Cost per hire
- **Weekly Trend:** Applications per week, Screening accuracy trend, Pipeline health score
- **Cost Savings:** Traditional recruiter cost vs. your service cost, with cumulative savings

Build a Make.com scenario that updates this dashboard weekly:

1. **Trigger:** Schedule — Every Friday at 4 PM
2. **Module 1:** Google Sheets → Pull all pipeline data for the week
3. **Module 2:** Code by Zapier → Calculate KPIs
4. **Module 3:** OpenAI → Generate narrative analysis
5. **Module 4:** Notion → Update the client dashboard
6. **Module 5:** Gmail → Send weekly report email

### Step 4 Check-In

1. Candidate Pool database populated with pre-screened candidates
2. Smart Matching generates top-5 recommendations for new roles
3. Match Reports are delivered to clients automatically
4. Pipeline Analytics Dashboard updates weekly
5. Weekly report email includes narrative analysis and cost savings

## Step 5: Build the Bias Audit and Compliance System

This module is non-negotiable. AI screening without bias auditing is a legal and ethical liability. You must demonstrate that your screening process is fair and does not systematically disadvantage candidates from any demographic group.

### Sub-step 5a: Create the Bias Audit Workflow

Create a Make.com scenario: "Bias Audit — [Client Name]"

1. **Trigger:** Schedule — Runs after every 50 screened candidates
2. **Module 1:** Google Sheets → Pull screening results for the last 50 candidates
3. **Module 2:** OpenAI → Analyze for bias patterns

System prompt:
```
You are a diversity and inclusion auditor analyzing recruitment screening results. Given the screening scores and recommendations for the last 50 candidates, check for:

1. Score distribution: Is there a statistically significant difference in average scores between identifiable demographic groups?
2. Rejection rates: Are certain groups being rejected at disproportionately high rates?
3. Advancement rates: Are certain groups being advanced at disproportionately low rates?
4. Language patterns: Do the AI's reasoning comments contain biased language or stereotypes?
5. Geographic bias: Are candidates from certain locations consistently scored lower?

Provide:
- Bias risk level (HIGH/MEDIUM/LOW/NONE)
- Specific patterns detected (if any)
- Recommended adjustments to the screening criteria
- Confidence level in the assessment

Note: You are working with limited data (name patterns, resume language, geographic indicators). Flag potential concerns even if they are not statistically significant with this sample size.
```

4. **Module 3:** Notion → Log the audit results
5. **Module 4:** Slack → Send alert if bias risk is HIGH or MEDIUM

### Sub-step 5b: Build the Compliance Documentation

Create a Notion template called "Screening Compliance Report" that documents:

- Screening criteria and their business justification
- Bias audit results and any corrective actions taken
- Human review rate (percentage of candidates manually reviewed)
- Appeal process for candidates who believe they were unfairly screened
- Data retention policy (how long candidate data is stored)

This documentation protects you and your client in case of a discrimination complaint or audit.

{{% accent-box %}}
**HACK:** Proactively share your bias audit results with clients. Most recruitment agencies do not audit their own processes for bias — they just assume they are fair. By showing clients your audit methodology and results, you position yourself as a responsible, transparent partner. This builds trust and differentiates you from every traditional recruiter who cannot tell you whether their screening process is biased because they have never checked.
{{% /accent-box %}}

### Step 5 Check-In

1. Bias Audit workflow runs automatically after every 50 screened candidates
2. Audit results are logged and reviewed
3. HIGH or MEDIUM bias risk triggers immediate alerts
4. Compliance Documentation template is complete
5. Data retention policy is defined and communicated to clients

## Pricing and Cost Breakdown

### Service Tiers

| Tier | Monthly | Setup Fee | What's Included | Your Cost | Margin |
|------|---------|-----------|-----------------|-----------|--------|
| Starter | $500 | $1,000 | AI screening (3 roles), weekly reports | ~$30/mo + 6 hrs | 85%+ |
| Growth | $1,200 | $2,000 | Full screening, scheduling, guides, matching | ~$70/mo + 12 hrs | 82%+ |
| Scale | $2,500 | $4,000 | Everything + passive sourcing, bias audits, analytics | ~$150/mo + 20 hrs | 80%+ |
| Enterprise | $5,000 | $8,000 | Full-service with custom models, dedicated support | ~$300/mo + 35 hrs | 78%+ |

### Cost Breakdown

| Item | Free Tier | Paid Tier | When to Upgrade |
|------|-----------|-----------|-----------------|
| Greenhouse/Lever | Free trial | $100-200/mo | At first paying client |
| Make.com | 1,000 ops/mo | $16/mo (10K ops) | At first paying client |
| OpenAI API | Pay per use | ~$20-50/mo | Scales with volume |
| Cal.com | Free | Free | — |
| Notion | Free | $10/mo (Team) | At 5+ clients |
| Google Workspace | — | $6/mo | Immediately |
| LinkedIn Recruiter | — | $170/mo | At 2+ clients |

**Total monthly cost at 1 client (Growth tier):** ~$312/mo
**Total monthly revenue at 1 client (Growth tier):** $1,200/mo + $2,000 setup
**Total monthly cost at 5 clients:** ~$550/mo
**Total monthly revenue at 5 clients:** $6,000/mo + setup fees

## Production Checklist

Before activating the recruitment automation for any client, verify every item:

- [ ] ATS connection is active and pulling applications correctly
- [ ] Role Specification sheet has 10+ requirements with weights
- [ ] AI screening workflow processes test applications with 85%+ accuracy
- [ ] All four routing paths (ADVANCE, PHONE_SCREEN, MANUAL_REVIEW, REJECT) work correctly
- [ ] Interview scheduling automation sends booking links automatically
- [ ] Interview guides are generated and delivered for each scheduled interview
- [ ] Candidate Pool database is set up and receiving screened candidates
- [ ] Smart Matching generates recommendations for new roles
- [ ] Pipeline Analytics Dashboard updates weekly
- [ ] Bias Audit workflow runs automatically after every 50 candidates
- [ ] Compliance Documentation is complete and shared with the client
- [ ] Error handling (Break + Slack) is attached to every API module
- [ ] Automatic retry (3 attempts, 30-second interval) is enabled on all API modules
- [ ] Client has been trained on how to read their dashboard and pipeline reports
- [ ] Rejection emails are professional and respectful (no ghosting)
