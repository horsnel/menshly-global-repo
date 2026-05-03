---
title: "Build and Automate an AI Video Production Agency with HeyGen, Runway, and Make.com"
date: 2026-05-01
category: "Implementation"
difficulty: "INTERMEDIATE"
readTime: "24 MIN"
excerpt: "The complete execution guide for building an AI video production pipeline. From script generation to AI avatar creation to social clip remixing to client delivery dashboards."
image: "/images/articles/intelligence/build-ai-video-production-agency.png"
heroImage: "/images/heroes/intelligence/build-ai-video-production-agency.png"
relatedOpportunity: "/opportunities/ai-video-production-agency/"
relatedPlaybook: "/playbooks/ai-video-production-agency-playbook/"
---

Manual video production is for agencies that want to stay small forever. If you want to run an AI video operation that generates $10,000+/month in recurring revenue, you need an automated engine that generates scripts, produces AI video assets, assembles polished content, and delivers it to clients on a consistent schedule — all without you spending 40 hours per week in an editing suite. This guide is the technical implementation manual. Follow every step in order. Skip nothing. If you skip the script quality gate, your AI produces generic content that sounds like every other AI video on the internet. If you skip the artifact check, you deliver videos with glitched visuals that destroy client trust. Every step exists because someone lost a client by skipping it.

This guide assumes you have zero infrastructure set up. By the end, you will have a fully automated pipeline that can produce 30+ videos per month across multiple clients with minimal manual intervention.

## Prerequisites

Before you start, you need the following:

- **HeyGen** — $24/mo (Creator plan for 15 avatar video credits)
- **Runway ML** — $12/mo (Standard plan for 625 credits)
- **ElevenLabs** — $5/mo (Starter plan for 30,000 characters)
- **Fliki** — $21/mo (Standard plan for 180 minutes)
- **Make.com** — $16/mo (Teams plan for 10,000 operations/month)
- **OpenAI API key** — $10 credit minimum (platform.openai.com/api-keys)
- **CapCut** — Free (video editing and assembly)
- **Canva Pro** — $13/mo (thumbnails and branded assets)
- **Frame.io** — $15/mo (client review and approval)
- **6-8 hours of uninterrupted time** for initial setup

Total upfront cost: $122/mo + $10 API credit. A single client at $1,200/month covers this 9x over.

## Step 1: Set Up Your AI Video Tool Integrations

This is the most critical step. Without reliable connections to your AI video tools, nothing else works. Each tool produces a different type of video asset, and they must work together seamlessly.

### Sub-step 1a: HeyGen Setup and API Configuration

Go to heygen.com and sign up for the Creator plan. Create your first test video: select a professional avatar, type a 30-second script, and generate. Verify the output quality meets your standards.

Navigate to **Settings** → **API** and generate an API key. Store it securely. In Make.com, add a HeyGen connection using your API key. Test the connection by creating a short video via the API.

### Sub-step 1b: Runway ML Setup

Go to runwayml.com and sign up for the Standard plan. Generate a test 4-second clip using the prompt: "Professional office workspace, warm lighting, cinematic, 4K." Verify the quality and download the clip.

Runway does not have a public API as of May 2026. You will trigger Runway generation manually and download clips to Google Drive for automated assembly. Build a Make.com scenario that monitors the Google Drive folder for new clips and routes them to the appropriate project.

### Sub-step 1c: ElevenLabs Setup and API Configuration

Go to elevenlabs.io and sign up for the Starter plan. Test the voice generation: paste a 100-word script and generate a voiceover using the "Adam" voice. Verify the quality sounds natural and professional.

Navigate to **Profile** → **API Keys** and generate a key. In Make.com, add an ElevenLabs connection. Test by generating a short voiceover via the API.

### Sub-step 1d: Fliki Setup

Go to fliki.ai and sign up for the Standard plan. Test the text-to-video pipeline: paste a 150-word script about a business topic and generate a 60-second social clip. Verify the voiceover, stock footage selection, and caption sync.

Fliki does not have a direct Make.com integration. Use the Fliki API (available on Standard plans) via Make.com's HTTP module, or trigger generation manually and download to Google Drive.

### Step 1 Check-In

Verify each of these before moving on:
1. HeyGen account active with test video generated, API key stored, Make.com connection green
2. Runway ML account active with test clip generated and saved to Google Drive
3. ElevenLabs account active with test voiceover generated, API key stored, Make.com connection green
4. Fliki account active with test social clip generated
5. All AI tool outputs meet professional quality standards

## Step 2: Build the AI Script Generation Engine

The script is the foundation of every video. A great script with mediocre visuals outperforms a mediocre script with stunning visuals every time. This module builds the AI script generation system that produces professional scripts from client briefs.

### Sub-step 2a: Create the Script Quality Framework

In Google Sheets, create a spreadsheet called "Script Quality Framework." Define the rules that every script must follow:

| Rule | Description | Validation Method |
|---|---|---|
| Hook within 3 seconds | First sentence must create curiosity, urgency, or relatability | AI scoring (1-10) |
| Max 150 words/minute | Speaking pace must be natural, not rushed | Word count check |
| Single clear message | One idea per video, not five | AI topic analysis |
| Specific CTA | "Click the link" not "learn more" | CTA keyword check |
| No jargon | No corporate buzzwords (synergy, leverage, paradigm) | Banned word list |
| Conversational tone | Write like you talk to a friend, not a boardroom | AI tone scoring |

### Sub-step 2b: Build the Script Generator Workflow

Create a Make.com scenario: "Script Generator"

1. **Trigger:** Google Sheets — New Row (in "Video Briefs" sheet)

The brief sheet columns: Client Name, Video Type, Target Audience, Key Message, Desired Length, Tone, CTA Type, Competitor Examples.

2. **Module 1 — OpenAI "Create a Chat Completion":**
   - Model: `gpt-4o`
   - System message:

```
You are an award-winning video scriptwriter. Given a client brief, write a complete video script.

SCRIPT FORMAT:
[SCENE N]
Visual: [What appears on screen]
Voiceover: [Exact words spoken]
On-screen text: [Any text overlays]
Duration: [Estimated seconds]

Rules:
- The first 3 seconds must stop the scroll (curiosity, urgency, or relatability)
- Maximum 150 words per minute of video
- Every sentence must earn its place — cut anything that does not advance the message
- End with a clear, specific CTA ("Click the link in bio" not "Learn more")
- Never use corporate jargon
- Conversational tone — write like talking to a colleague

Respond in JSON:
{
  "title": "",
  "hook": "",
  "scenes": [{"visual": "", "voiceover": "", "on_screen_text": "", "duration_seconds": 0}],
  "cta": "",
  "total_duration_seconds": 0,
  "word_count": 0,
  "seo_keywords": []
}
```

3. **Module 2 — OpenAI "Create a Chat Completion" (Quality Scoring):**

```
Score this video script on a scale of 1-10 for:
- Hook strength (stops scrolling?)
- Message clarity (one idea?)
- Conversational tone (natural, not corporate?)
- CTA specificity (clear action?)
- Overall quality (would you keep watching?)

If any score is below 7, regenerate the script with improvements.
```

4. **Module 3 — Code by Zapier:** Parse the script and validate against quality framework rules
5. **Module 4 — Notion:** Create a script page in the client's Scripts database
6. **Module 5 — Gmail:** Send the draft script to the client for review

### Sub-step 2c: Build the Three-Hook A/B Testing System

Modify the script generator to produce three hook variations:

1. **Curiosity hook:** "What if I told you [surprising fact]?"
2. **Urgency hook:** "If you do not do [X] by [deadline], you will lose [Y]."
3. **Relatability hook:** "You know that feeling when [common experience]?"

Send all three hooks to the client and let them choose. Track which hook style performs best for each client and video type. After 20 videos, you will have statistical significance to default to the best-performing hook style.

### Step 2 Check-In

1. Script Quality Framework defined with 6+ rules
2. Script Generator workflow produces scripts from briefs automatically
3. Quality scoring ensures scripts meet minimum standards before delivery
4. Three-hook A/B testing system generates variations
5. Scripts are delivered to clients for review via Notion and email

## Step 3: Build the Video Production Pipeline

This is where scripts become videos. The production pipeline generates all AI assets, assembles them in CapCut, and delivers drafts for client review.

### Sub-step 3a: Build the Explainer Video Pipeline

Create a Make.com scenario: "Explainer Production — [Client Name]"

1. **Trigger:** Notion — Script status changes to "Approved"
2. **Module 1 — ElevenLabs:** Generate voiceover from the script's voiceover text
3. **Module 2 — HeyGen:** Generate AI avatar segments for presenter-led sections
4. **Module 3 — Google Sheets:** Log all generated assets with file URLs
5. **Module 4 — Slack:** Notify you that assets are ready for assembly

Assembly in CapCut (manual, 30-60 minutes per video):
1. Import all generated assets
2. Arrange scenes in script order
3. Add transitions (simple cuts or crossfades only)
4. Sync voiceover to visuals
5. Add captions using CapCut's auto-caption, then manually correct errors
6. Add background music from royalty-free library
7. Add brand elements (logo, colors, lower thirds)
8. Export at 1080p
9. Upload to Frame.io for client review

### Sub-step 3b: Build the Social Clip Pipeline

Social clips are your highest-volume product. Build for speed, not perfection.

Create a Make.com scenario: "Social Clip Production"

1. **Trigger:** Notion — Script status changes to "Approved" for "Social Clip" type
2. **Module 1 — Fliki:** Generate the video from the script (voiceover, stock footage, captions)
3. **Module 2 — Slack:** Notify you that the clip is ready for branding

Branding in CapCut (manual, 15-20 minutes per clip):
1. Add client logo intro (3 seconds)
2. Adjust caption styling to match brand fonts
3. Add end card with CTA
4. Export in 3 formats: 9:16 (Reels/TikTok), 1:1 (Feed), 16:9 (Shorts)
5. Upload all formats to Frame.io

### Sub-step 3c: Build the Video Remix System

This is your margin multiplier. One long-form video becomes 3-5 social clips.

Create a Make.com scenario: "Video Remix"

1. **Trigger:** Notion — Long-form video status changes to "Delivered"
2. **Module 1 — OpenAI:** Identify the 3-5 most clip-worthy moments from the script

```
Given this video script, identify the 5 most clip-worthy moments for social media.
Criteria: emotional peak, surprising statement, quotable soundbite, actionable tip, controversial opinion.
For each moment, provide: timestamp range, hook text (3 seconds), and why it works as a standalone clip.
```

3. **Module 2:** Create social clip scripts for each moment
4. **Module 3:** Route each to the Social Clip Production pipeline

{{% accent-box %}}
**HACK:** Build a CapCut template library for each client. Once you have produced 5+ videos for a client, create CapCut templates with their brand elements pre-loaded: logo intro, font styles, color overlays, end card, and music bed. When you start a new video, you load the template instead of manually adding brand elements from scratch. This reduces assembly time from 45 minutes to 15 minutes per video.
{{% /accent-box %}}

### Step 3 Check-In

1. Explainer Video Pipeline generates and delivers AI avatar videos
2. Social Clip Pipeline produces branded clips in 3 formats
3. Video Remix System creates social clips from long-form content automatically
4. CapCut template library accelerates assembly time
5. Quality control checklist is applied before every Frame.io upload

## Step 4: Build the Client Review and Revision System

Revisions are where agencies lose money. This module builds a structured review system that protects margins while keeping clients happy.

### Sub-step 4a: Configure the Review Workflow

Create a Make.com scenario: "Review Tracking"

1. **Trigger:** Frame.io — New comment on a video
2. **Module 1 — Notion:** Add the comment to the project's revision log
3. **Module 2 — Code by Zapier:** Categorize the comment:
   - **Simple fix** (text change, color adjustment) → implement immediately
   - **Creative revision** (scene replacement, voiceover redo) → implement within 24 hours
   - **Scope creep** (new scene not in brief, additional format) → flag for upsell

### Sub-step 4b: Build the Revision Enforcer

Create a scenario: "Revision Deadline Enforcer"

1. **Trigger:** Schedule — Check every 6 hours for overdue reviews
2. **Module 1 — Notion:** Find projects in "Review" status past the deadline
3. **Module 2 — Gmail:** Send reminder: "Your review for [Project] is overdue. If we do not receive feedback by [extended deadline], we will proceed with the current version."

### Sub-step 4c: Build the Scope Creep Detector

Create a scenario that flags revision requests that exceed the original brief:

1. **Trigger:** Frame.io comment contains keywords suggesting new scope ("also add," "can you create," "instead of X, can we do Y")
2. **Module 1 — OpenAI:** Analyze whether the request is within scope or constitutes a change
3. **Module 2 — Gmail:** If out of scope, send: "Great idea! That falls outside the current project scope. I have drafted an add-on: [description] for [price]. Want me to add it?"

### Step 4 Check-In

1. Review Tracking logs all Frame.io comments to Notion
2. Comments are categorized as simple fix, creative revision, or scope creep
3. Revision deadlines are enforced with automatic reminders
4. Scope creep is identified and converted to add-on opportunities
5. Revision count is tracked per project and against package limits

## Step 5: Build the Analytics and Reporting System

Clients cancel when they cannot see results. This module builds automated reporting that proves the ROI of your video content.

### Sub-step 5a: Build the Monthly Performance Report

Create a Make.com scenario: "Monthly Video Report"

1. **Trigger:** Schedule — 3rd of each month
2. **Module 1 — Google Sheets:** Pull video performance data (views, engagement, clicks, shares)
3. **Module 2 — Code by Zapier:** Calculate KPIs:
   - Total videos delivered
   - Total views across all platforms
   - Average engagement rate
   - Cost per view (monthly retainer / total views)
   - Cost per engagement (monthly retainer / total engagements)
   - Earned media value (views × industry CPM)
4. **Module 3 — OpenAI:** Generate narrative analysis

```
You are a video marketing analyst. Given performance data for the month's videos, write a report that:
1. Highlights the top-performing video and analyzes why it worked
2. Identifies underperforming videos with specific improvement suggestions
3. Calculates the earned media value and ROI
4. Compares performance to industry benchmarks
5. Recommends content strategy adjustments for next month
```

5. **Module 4 — Notion:** Update the client dashboard
6. **Module 5 — Gmail:** Send the report to the client

### Sub-step 5b: Build the Earned Media Value Calculator

Create a Google Sheet that calculates:

- **CPM (Cost Per Thousand):** Average cost of ads in the client's industry
- **Earned Media Value:** (Total views / 1000) × CPM
- **ROI:** (Earned Media Value - Monthly Retainer) / Monthly Retainer × 100

Example: A client in the SaaS industry (CPM ~$15) whose videos get 50,000 views/month has an earned media value of $750. If their monthly retainer is $1,200, the ROI is -37.5% — but this improves dramatically as view counts grow. At 200,000 views/month, the earned media value is $3,000 and the ROI is 150%.

{{% accent-box %}}
**HACK:** Track the "content velocity" metric — how quickly your videos are published relative to the client's competitors. Most businesses post 1-2 videos per month. Your AI production pipeline delivers 10-20+. Show the client a side-by-side comparison: "Your competitor posted 3 videos last month. You posted 15. You are dominating the algorithm because you have 5x the content velocity." This metric is immediately gratifying and directly attributable to your service.
{{% /accent-box %}}

### Step 5 Check-In

1. Monthly Performance Report generates and delivers automatically
2. AI narrative analysis provides specific, actionable recommendations
3. Earned Media Value calculated and included in reports
4. Content velocity tracked and compared to competitors
5. Client Notion dashboard updates monthly with latest metrics

## Pricing and Cost Breakdown

### Service Tiers

| Tier | Monthly | Setup Fee | What's Included | Your Cost | Margin |
|------|---------|-----------|-----------------|-----------|--------|
| Starter | $500 | $1,000 | 4 social clips + 1 explainer, basic branding | ~$30/mo + 6 hrs | 85%+ |
| Growth | $1,200 | $2,000 | 8 social clips + 2 explainers + 1 demo, full branding | ~$60/mo + 12 hrs | 82%+ |
| Scale | $2,500 | $4,000 | 15 clips + 4 explainers + 2 long-form, premium | ~$120/mo + 20 hrs | 80%+ |
| Enterprise | $5,000 | $8,000 | Unlimited within capacity, custom avatars, multi-language | ~$300/mo + 30 hrs | 78%+ |

### Cost Breakdown

| Item | Free Tier | Paid Tier | When to Upgrade |
|------|-----------|-----------|-----------------|
| HeyGen | 1 credit/mo | $24/mo (15 credits) | At first paying client |
| Runway ML | 125 credits | $12/mo (625 credits) | At first paying client |
| Fliki | 5 min/mo | $21/mo (180 min) | At first paying client |
| ElevenLabs | 10K chars/mo | $5/mo (30K chars) | At first paying client |
| Make.com | 1,000 ops/mo | $16/mo (10K ops) | At first paying client |
| CapCut | Free | $8/mo (Pro) | When needed |
| Canva Pro | Limited | $13/mo | Immediately |
| Frame.io | 2 projects | $15/mo | At 3+ clients |

**Total monthly cost at 1 client (Growth tier):** ~$156/mo
**Total monthly revenue at 1 client (Growth tier):** $1,200/mo + $2,000 setup
**Total monthly cost at 5 clients:** ~$350/mo
**Total monthly revenue at 5 clients:** $6,000/mo + setup fees

## Production Checklist

Before activating the video production pipeline for any client, verify every item:

- [ ] HeyGen account active with API key, test video generated
- [ ] Runway ML account active with test clip generated
- [ ] ElevenLabs account active with API key, test voiceover generated
- [ ] Fliki account active with test social clip generated
- [ ] Script Generator workflow produces quality scripts from briefs
- [ ] Explainer Video Pipeline generates and delivers avatar videos
- [ ] Social Clip Pipeline produces clips in 3 formats (9:16, 1:1, 16:9)
- [ ] Video Remix System creates social clips from long-form content
- [ ] Review Tracking logs Frame.io comments to Notion
- [ ] Revision deadlines are enforced automatically
- [ ] Scope creep is detected and converted to add-on opportunities
- [ ] Monthly Performance Report generates and delivers
- [ ] Earned Media Value calculated and included
- [ ] Client brand assets are stored in Google Drive with consistent naming
- [ ] CapCut templates are created for the client's brand
- [ ] Quality control checklist is applied to every video before delivery
