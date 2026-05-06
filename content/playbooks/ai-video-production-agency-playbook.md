---
title: "The AI Video Production Agency Playbook: 31 Steps to $20K/Month"
date: 2026-05-01
category: "Playbook"
price: "₦35,000"
readTime: "90 MIN"
excerpt: "The complete operating system for building an AI video production agency from zero. 10 modules, 35 procedures, exact tool configurations, client delivery workflows, three pricing tiers, and a scaling roadmap. From empty Notion workspace to ₦10M/month in recurring revenue."
image: "/images/articles/playbooks/ai-video-production-agency-playbook.png"
heroImage: "/images/heroes/playbooks/ai-video-production-agency-playbook.png"
relatedOpportunity: "/opportunities/ai-video-production-agency/"
relatedGuide: "/intelligence/build-ai-video-production-agency/"
---

This is not a blog post condensed into a PDF. This is an operating system for building an AI video production agency from zero to ₦10,000,000/month in recurring revenue. Every module contains exact procedures — not theories, not possibilities, not "consider doing X." You will do X, in this order, with these tools, and you will verify it worked before moving on.

**35 procedures. 10 modules. 8+ hours of reading and execution.** If you complete every procedure, you will have a functioning video production practice with paying clients. If you skip procedures, you will have a folder of half-finished AI-generated videos and no revenue. The choice is yours.

---

# MODULE 1: FOUNDATION — YOUR VIDEO PRODUCTION COMMAND CENTER

## Overview

Before you render a single frame, you need the infrastructure that runs your video production agency. This module sets up your project management, client portal, financial tracking, and communication systems. These are not optional. Every successful video agency operator has these systems in place before their first client call. Every failed operator skipped them.

**Time to complete:** 3-4 hours
**Tools needed:** Notion (free), Zapier (free tier), Paystack (free), Frame.io (free trial)

## Procedure 1.1: Create Your Video Production Command Center in Notion

Open your browser and go to notion.so. Sign in or create a free account. You should see the Notion dashboard — a clean sidebar on the left and a main area with a "New page" button.

Click **New page** in the left sidebar. Name it: `[Your Agency Name] Command Center`. This is the single source of truth for your entire business.

Inside this page, create seven sub-pages by typing `/page` and naming each one:

1. **Clients** — Every client, their status, their active projects, their revenue
2. **SOPs** — Standard Operating Procedures for every repeatable video production process
3. **Prompt Library** — Every AI prompt your agency uses, organized by video type
4. **Templates** — Client-facing documents, proposals, storyboards, delivery checklists
5. **Finance** — Revenue tracking, expense tracking, margin analysis
6. **Pipeline** — Prospects, leads, and their position in your sales process
7. **Automation Logs** — Every Zapier workflow, its status, its last run time, its error count

Do you see all seven sub-pages listed inside your Command Center? If any are missing, add them now. You should have exactly seven. Count them.

### The Clients Database

Open the **Clients** sub-page. Type `/table` and select **Table — Full page**. Name it `Client Roster`.

Add these columns:

| Column Name | Type | Description |
|---|---|---|
| Client Name | Title | The business name |
| Status | Select: Active, Onboarding, Paused, Churned | Current relationship state |
| Tier | Select: Starter, Growth, Enterprise | Service tier |
| Monthly Revenue | Number | Retainer amount in Naira |
| Setup Fee | Number | One-time setup fee in Naira |
| Start Date | Date | When the engagement began |
| Active Projects | Number | Number of videos currently in production |
| Avg Delivery Time | Number | Average days from brief to delivery |
| Health Score | Select: Green, Yellow, Red | Subjective assessment of the relationship |

### The Projects Database

Create another full-page table called `Project Tracker`.

| Column Name | Type |
|---|---|
| Project Name | Title |
| Client | Relation (linked to Client Roster) |
| Video Type | Select: Explainer, Social Clip, Testimonial, Product Demo, Faceless Long-form |
| Status | Select: Briefing, Scripting, Production, Review, Final Delivery |
| Deadline | Date |
| Assigned To | Text |
| AI Tools Used | Multi-select: HeyGen, Runway, Fliki, ElevenLabs, Midjourney, CapCut |
| Revision Count | Number |

## Procedure 1.2: Set Up Your Financial Infrastructure

### Create Your Paystack Account

Go to paystack.com and create a business account. Complete the business verification process. This typically takes 2-5 business days for approval.

### Create Your Payment Products

| Product Name | Price | Type |
|---|---|---|
| Starter Setup Fee | ₦200,000 | One time |
| Starter Monthly Retainer | ₦100,000/month | Recurring |
| Growth Setup Fee | ₦400,000 | One time |
| Growth Monthly Retainer | ₦250,000/month | Recurring |
| Enterprise Setup Fee | ₦750,000 | One time |
| Enterprise Monthly Retainer | ₦500,000/month | Recurring |

Create payment links for each product. Save these links in your Notion **Templates** page under "Payment Links."

### Set Up Revenue Tracking

In your Notion **Finance** page, create a table called `Revenue Tracker` with these columns:

| Column Name | Type |
|---|---|
| Month | Title (e.g., "May 2026") |
| Total MRR | Number |
| Project Fees | Number |
| Total Revenue | Formula: Total MRR + Project Fees |
| Expenses | Number |
| Net Profit | Formula: Total Revenue - Expenses |
| Active Clients | Number |
| Videos Delivered | Number |

## Procedure 1.3: Configure Your Communication Stack

### Create Your Business Email

Set up Google Workspace ($6/mo) with a custom domain. Create your professional email address.

### Create Your Review and Approval System

Go to frame.io and sign up for a free trial. Frame.io is the industry standard for video review and approval. Clients leave timestamped comments directly on the video — no more "at 2:34, can you change the text" emails.

Configure your Frame.io workspace:
- Create a team called `[Your Agency Name]`
- Set up review templates with default reviewers and approval workflows
- Connect Frame.io to Zapier for automated status updates

{{% accent-box %}}
**HACK:** Use Notion's "Template" button inside your Project Tracker database to create a pre-filled template for new projects. Include default values for Status ("Briefing"), Revision Count (0), and a checklist of production steps: "Receive brief," "Write script," "Generate AI visuals," "Record voiceover," "Edit and assemble," "Internal review," "Client review," "Final delivery." This saves 15 minutes every time you start a new project.
{{% /accent-box %}}

## Check-In: Module 1 Complete

- [ ] Notion Command Center created with all 7 sub-pages
- [ ] Client Roster database with all 9 columns
- [ ] Project Tracker database with all 8 columns
- [ ] Paystack account with 6 products and 6 payment links
- [ ] Revenue Tracker table in Notion
- [ ] Professional email address on custom domain
- [ ] Frame.io workspace with review templates

7 checkmarks. Do not proceed to Module 2 with an incomplete foundation.

---

# MODULE 2: TECH STACK — YOUR VIDEO PRODUCTION ARSENAL

## Overview

Your video agency runs on tools. This module sets up every AI video tool you need, connects them, and verifies each one works. The total monthly cost can be as low as ₦0 for free tiers — and most paid tools are free until you have paying clients.

**Time to complete:** 3-4 hours
**Total monthly cost (startup):** ₦0–₦20,000 depending on your choices

## Procedure 2.1: Set Up AI Video Generation Tools

### HeyGen — AI Avatar Videos

Go to heygen.com and create a free account. HeyGen produces the most realistic AI avatar videos available in 2026. You type a script, select an avatar, and receive a video of a realistic human presenter speaking your words with natural gestures and expressions.

After signing in, test the system: create a 30-second video using a default avatar. Type a script: "Welcome to our company. We help businesses grow through the power of AI video production. Let me show you how." Select a professional-looking avatar. Click **Generate**.

Wait for the video to render (typically 2-5 minutes). Watch the playback. Does the avatar look natural? Does the lip-sync match? Are the gestures smooth? If the quality meets your standards, HeyGen is your primary tool for presenter-led videos.

### Runway ML — AI Visual Effects and B-Roll

Go to runwayml.com and create a free account. Runway is the leading AI video generation platform. You describe a scene in text, and Runway generates video footage from that description. Use it for: B-roll generation, visual effects, background scenes, and creative transitions.

Test the system: generate a 4-second clip using the prompt "Aerial view of a modern office building at sunrise, cinematic, 4K." Wait for the generation (typically 1-3 minutes). Does the output look professional? Runway's Gen-3 Alpha model produces remarkably realistic footage, though it sometimes generates artifacts in complex scenes.

### Fliki — Text-to-Video for Social Content

Go to fliki.ai and create a free account. Fliki converts text scripts into social media videos with AI voiceovers, stock footage, and captions. It is the fastest way to produce Instagram Reels, TikToks, and YouTube Shorts.

Test the system: paste a 100-word script about "5 AI tools every business needs" and generate a 60-second video. Does the voiceover sound natural? Are the stock clips relevant? Are the captions synced?

### ElevenLabs — AI Voice Generation

Go to elevenlabs.io and create a free account. ElevenLabs produces the most natural-sounding AI voices available. You will use it for voiceovers on all video content.

Test the system: paste your script into the text box and generate a voiceover using the "Adam" voice. Listen to the output. Does it sound human? Is the pacing natural? Are difficult words pronounced correctly? If you hear robotic artifacts, try different voice models until you find one that passes the "could this be a real person?" test.

## Procedure 2.2: Set Up Your Editing and Post-Production Tools

### CapCut Pro — Video Editing

Go to capcut.com and download CapCut (free). CapCut is the best free video editor available, with built-in AI features: auto-captions, background removal, AI color correction, and template-based editing.

### Canva Pro — Thumbnail and Social Asset Creation

Go to canva.com and sign up for Canva Pro ($13/month). You will use Canva to create video thumbnails, social media graphics, and branded templates for clients.

### Midjourney — AI Image Generation for Storyboards

Go to midjourney.com and create an account. You will use Midjourney to generate storyboard frames, concept art, and visual references for client projects.

## Procedure 2.3: Connect Everything with Zapier

In Zapier, connect these services:

1. **HeyGen** — For automated video generation triggers
2. **Google Sheets** — For project tracking and data management
3. **Gmail** — For client communication
4. **Notion** — For project management
5. **Frame.io** — For review and approval workflows
6. **Slack** — For team notifications

Verify all connections show green status.

## Procedure 2.4: Complete Tool Cost Summary

| Tool | Purpose | Free Tier | Paid Tier | When to Upgrade |
|---|---|---|---|---|
| HeyGen | AI avatar videos | 1 credit/month | $24/mo (15 credits) | At first paying client |
| Runway ML | AI visual generation | 125 credits free | $12/mo (625 credits) | At first paying client |
| Fliki | Text-to-video social | 5 min/month | $21/mo (180 min) | At first paying client |
| ElevenLabs | AI voiceovers | 10,000 chars/month | $5/mo (30,000 chars) | At first paying client |
| CapCut | Video editing | Free | $8/mo | When you need Pro features |
| Canva Pro | Thumbnails and assets | Limited | $13/mo | Immediately |
| Midjourney | Storyboard images | — | $10/mo | At first paying client |
| Frame.io | Review and approval | Free (2 projects) | $15/mo | At 3+ clients |
| Zapier | Automation | 100 tasks/mo | $20/mo | At first paying client |
| Notion | Project management | Free | $10/mo | At 5+ team members |
| Google Workspace | Email + docs | — | $6/mo | Immediately |

**Startup cost: $19/mo (Google Workspace + Canva Pro). Everything else is free until you have revenue.**

## Check-In: Module 2 Complete

- [ ] HeyGen account with test video generated
- [ ] Runway ML account with test clip generated
- [ ] Fliki account with test social video generated
- [ ] ElevenLabs account with test voiceover generated
- [ ] CapCut installed and tested
- [ ] Canva Pro account active
- [ ] Midjourney account with test images generated
- [ ] Frame.io workspace configured
- [ ] Zapier with 6 connected services (all green)

9 checkmarks required to proceed.

---

# MODULE 3: SCRIPT AND STORYBOARD AUTOMATION — THE NARRATIVE ENGINE

## Overview

Every great video starts with a great script. This module builds the AI-powered scriptwriting and storyboarding system that turns a client brief into a production-ready script in minutes instead of days. The script is the foundation of every video — a bad script produces a bad video regardless of how impressive the AI visuals are.

**Time to complete:** 3-4 hours
**Tools needed:** OpenAI API, Notion, Google Sheets

## Procedure 3.1: Create Your Script Template Library

Open your Notion **Templates** page. Create a sub-page called `Script Templates`. Build templates for these video types:

1. **Explainer Video** (60-90 seconds) — Problem → Solution → Benefits → CTA
2. **Product Demo** (2-3 minutes) — Hook → Feature Walkthrough → Social Proof → CTA
3. **Social Media Clip** (15-60 seconds) — Hook → Value → CTA
4. **Testimonial Compilation** (60-120 seconds) — Challenge → Solution → Result
5. **Faceless YouTube Long-form** (8-15 minutes) — Hook → Story → Insights → CTA
6. **Brand Story** (2-3 minutes) — Origin → Mission → Vision → CTA
7. **Training/How-To** (5-10 minutes) — Overview → Step-by-Step → Summary → CTA

Each template must include:
- **Hook** (first 3 seconds — the moment that stops the scroll)
- **Act Structure** (setup, conflict, resolution)
- **Scene Descriptions** (visual direction for each section)
- **Voiceover Text** (exact words the AI voice or avatar will speak)
- **On-Screen Text** (captions, titles, lower thirds)
- **CTA** (clear, specific call to action)
- **Estimated Duration** (based on word count and pacing)

## Procedure 3.2: Build the AI Script Generator

Create a Zapier workflow: "Script Generator Pipeline."

**Trigger:** Google Sheets — New Row (in a sheet called "Video Briefs")

The brief sheet should have these columns: Client Name, Video Type, Target Audience, Key Message, Desired Length, Tone, Competitor Examples, CTA Type.

**Step 1:** OpenAI — Generate script:

System prompt:
```
You are an award-winning video scriptwriter. Given a client brief, write a complete video script that:

1. Opens with a hook that stops scrolling within the first 3 seconds
2. Follows the appropriate act structure for the video type
3. Includes specific visual direction for each scene
4. Uses conversational, jargon-free language
5. Ends with a clear, specific call-to-action

SCRIPT FORMAT:
[SCENE 1]
Visual: [What appears on screen]
Voiceover: [Exact words spoken]
On-screen text: [Any text overlays]
Duration: [Estimated seconds]

[SCENE 2]
...

Rules:
- Explainer videos: maximum 150 words per minute
- Social clips: maximum 2 sentences per scene
- Long-form: include chapter markers and transition phrases
- Never use corporate jargon or filler phrases
- Every sentence must earn its place — cut anything that does not advance the message
- The hook must create curiosity, urgency, or relatability in the first 3 seconds

Respond in JSON:
{
  "title": "",
  "hook": "",
  "scenes": [{"visual": "", "voiceover": "", "on_screen_text": "", "duration_seconds": 0}],
  "cta": "",
  "total_duration_seconds": 0,
  "word_count": 0,
  "seo_keywords": [],
  "estimated_engagement_rate": 0.0
}
```

**Step 2:** Code by Zapier — Parse and validate
**Step 3:** Notion — Create a new page in the client's Scripts database
**Step 4:** Gmail — Send the draft script to the client for review

{{% accent-box %}}
**HACK:** Generate three hook variations for every script and A/B test them. The hook is the most important part of any video — 65% of viewers decide whether to keep watching within the first 3 seconds. Run these three hooks through an AI scoring prompt: "Rate this video hook on a scale of 1-10 for curiosity gap, emotional impact, and scroll-stopping power. Which one would make you keep watching and why?" Use the highest-scoring hook as your primary, and save the others for social media remixes.
{{% /accent-box %}}

## Procedure 3.3: Build the AI Storyboard Generator

Once the script is approved, generate a visual storyboard using Midjourney.

Create a Zap: "Storyboard Generator."

**Trigger:** Script status changes to "Approved" in Notion
**Step 1:** OpenAI → Extract scene descriptions from the script and generate Midjourney prompts:

```
Convert this scene description into a Midjourney prompt:
Scene: [Visual description from script]

Midjourney prompt format:
[Subject], [Action/Pose], [Setting/Background], [Lighting], [Camera Angle], [Style], --ar [aspect ratio] --v 6

Rules:
- Use cinematic lighting descriptions (golden hour, dramatic side lighting, soft diffused)
- Specify camera angles (close-up, wide shot, medium shot, over-the-shoulder)
- Include style keywords (photorealistic, cinematic, editorial, corporate, minimalist)
- Always include --ar 16:9 for landscape video or --ar 9:16 for vertical social
```

**Step 2:** Midjourney → Generate images (via Discord bot or API)
**Step 3:** Notion → Create storyboard page with images alongside script text

## Check-In: Module 3 Complete

- [ ] Script Template Library with 7 video types
- [ ] AI Script Generator Zap built and tested with 5+ briefs
- [ ] Three-hook A/B testing system integrated
- [ ] AI Storyboard Generator creates visual references from scripts
- [ ] Storyboard pages created in Notion with images and script text

5 checkmarks. The script determines 80% of the video's success. Invest the time here.

---

# MODULE 4: VIDEO PRODUCTION AUTOMATION — THE FACTORY FLOOR

## Overview

This module builds the core production engine: scripts flow in, AI generates visuals and voiceovers, you assemble and polish the final video. This is where the magic happens — and where most agencies fail by trying to do everything manually.

**Time to complete:** 4-6 hours
**Tools needed:** HeyGen, Runway, Fliki, ElevenLabs, CapCut, Zapier

## Procedure 4.1: Build the Explainer Video Production Pipeline

Create a Zap: "Explainer Video Production."

**Trigger:** Script approved for "Explainer" video type
**Step 1:** ElevenLabs → Generate voiceover from the script's voiceover text
**Step 2:** HeyGen → Generate AI avatar video segments for presenter-led sections
**Step 3:** Runway → Generate B-roll clips from scene descriptions
**Step 4:** CapCut → (Manual) Assemble the video:

Assembly checklist:
1. Import all generated assets into CapCut
2. Arrange scenes in script order
3. Add transitions between scenes (use simple cuts or crossfades — avoid flashy transitions)
4. Sync voiceover to visuals
5. Add captions (use CapCut's auto-caption feature, then manually correct errors)
6. Add background music (use royalty-free from CapCut's library or Epidemic Sound)
7. Add brand elements (logo watermark, brand colors, lower thirds)
8. Export at 1080p (or 4K for premium clients)
9. Upload to Frame.io for client review

**Step 5:** Frame.io → Upload the draft video
**Step 6:** Gmail → Notify the client that their draft is ready for review
**Step 7:** Notion → Update project status to "Review"

## Procedure 4.2: Build the Social Media Clip Production Pipeline

Social media clips are your high-volume, low-price product. You should be able to produce 10-15 social clips per day with AI automation.

Create a Zap: "Social Clip Production."

**Trigger:** Script approved for "Social Clip" video type
**Step 1:** Fliki → Generate the video from the script (Fliki handles voiceover, stock footage, and captions in one step)
**Step 2:** CapCut → (Manual) Polish and brand:
- Add client logo intro (3 seconds)
- Adjust caption styling to match brand fonts
- Add end card with CTA
- Export in all required formats: 9:16 (Reels/TikTok), 1:1 (Feed), 16:9 (YouTube Shorts)
**Step 3:** Upload to Frame.io
**Step 4:** Gmail → Notify client

{{% accent-box %}}
**HACK:** Create a "video remix" system that takes every long-form video and automatically generates 3-5 social clips from it. Build a Zap that: (1) takes the approved long-form script, (2) uses AI to identify the 3-5 most clip-worthy moments (highest emotional impact, best soundbites), (3) generates short-form scripts for each moment, (4) routes each to the social clip pipeline. One long-form video becomes a content machine — this is how you deliver 20+ videos per month for a Growth-tier client while only producing 4-5 from scratch.
{{% /accent-box %}}

## Procedure 4.3: Build the Faceless YouTube Video Pipeline

Faceless YouTube channels are a massive opportunity. The videos are entirely AI-generated: AI voiceover, AI visuals, AI-edited. No human appears on camera.

Create a Zap: "Faceless YouTube Production."

**Trigger:** Script approved for "Faceless Long-form" video type
**Step 1:** ElevenLabs → Generate full voiceover (8-15 minutes)
**Step 2:** OpenAI → Break the script into B-roll prompts for Runway:

```
Given a video script, generate Runway ML prompts for each section. Each prompt should describe a 4-second video clip that visually represents the narration.

Rules:
- Use cinematic, high-quality visual descriptions
- Vary camera angles and subjects between clips
- Avoid text in the generated clips (it will be garbled)
- Prefer abstract, atmospheric, and conceptual visuals over specific people
- Each clip should flow naturally into the next
```

**Step 3:** Runway → Generate all B-roll clips (may require multiple batches)
**Step 4:** CapCut → (Manual) Assemble:
1. Lay the voiceover on the timeline
2. Cut B-roll clips to match narration timing
3. Add captions throughout (critical for faceless videos — 85% of social viewers watch without sound)
4. Add intro and outro graphics
5. Add chapter markers for YouTube
6. Export at 1080p minimum

**Step 5:** Upload to Frame.io for review

## Procedure 4.4: Quality Control Checklist

Before sending any video to client review, verify:

- [ ] Audio levels between -14 and -16 LUFS (use CapCut's audio meter)
- [ ] No AI generation artifacts (extra fingers, glitchy text, unnatural movements)
- [ ] Captions are 100% accurate (AI captions always have errors — verify manually)
- [ ] Brand elements (logo, colors, fonts) match the client's brand guide
- [ ] Video duration matches the brief (±10%)
- [ ] Export quality is at least 1080p
- [ ] File size is reasonable (under 2GB for a 10-minute video)
- [ ] Opening hook plays correctly without buffering artifacts

8 quality checks. Do not skip any. A single artifact or wrong caption can destroy a client's trust in your AI-powered production.

## Check-In: Module 4 Complete

- [ ] Explainer Video Production Pipeline built and tested
- [ ] Social Media Clip Production Pipeline producing clips at volume
- [ ] Faceless YouTube Video Pipeline generating long-form content
- [ ] Video remix system creating social clips from long-form content
- [ ] Quality control checklist applied to every video
- [ ] All pipelines added to the Zapier Workflow Registry

6 checkmarks. The production pipeline is your factory floor. It must run smoothly.

---

# MODULE 5: CLIENT REVIEW AND REVISION MANAGEMENT

## Overview

Revisions are where agencies lose money. Unlimited revisions destroy margins. No revisions destroy relationships. This module builds a structured revision process that protects your margins while keeping clients happy.

**Time to complete:** 2-3 hours
**Tools needed:** Frame.io, Zapier, Notion

## Procedure 5.1: Set Up the Revision Policy

Define your revision tiers:

**Starter Tier:** 2 rounds of revisions included, ₦25,000 per additional round
**Growth Tier:** 3 rounds of revisions included, ₦50,000 per additional round
**Enterprise Tier:** 5 rounds of revisions included, ₦75,000 per additional round

A "round" is defined as: all feedback submitted by the client at one time. If the client sends 5 comments on Monday and 3 more on Wednesday, that counts as one round (if submitted within the review window).

## Procedure 5.2: Build the Review and Revision Workflow

Create a Zap: "Review Tracking."

**Trigger:** Frame.io → New comment on a video
**Step 1:** Notion → Add the comment to the project's revision log
**Step 2:** Track the review deadline (48 hours for Starter, 72 hours for Growth/Enterprise)

Create a second Zap: "Revision Deadline Enforcer."

**Trigger:** Schedule → Check every 6 hours for overdue reviews
**Step 1:** Gmail → Send reminder to client: "Your review for [Project Name] is overdue. We need your feedback by [deadline] to maintain the delivery schedule. If we do not receive feedback by [extended deadline], we will proceed with the current version."

This prevents the "client went silent for two weeks" problem that clogs your production pipeline.

## Procedure 5.3: Build the Revision Implementation Workflow

When the client submits revision feedback:

**Step 1:** Review all comments in Frame.io. Categorize each as:
- **Simple fix** (text change, color adjustment, timing tweak) — implement immediately
- **Creative revision** (scene replacement, script change, voiceover redo) — implement within 24 hours
- **Scope creep** (new scene not in the original brief, additional video format) — flag for client approval and additional billing

**Step 2:** Implement all simple fixes and creative revisions
**Step 3:** Upload the revised video to Frame.io
**Step 4:** Notion → Update project status and increment revision count
**Step 5:** Gmail → Notify client that the revised video is ready

{{% accent-box %}}
**HACK:** When a client requests a revision that is actually scope creep, do not say "that will cost extra." Instead, say: "Great idea! That falls outside the current project scope, so I've drafted a quick add-on: [description] for [price]. Want me to add that to this project or save it for the next one?" This frames the upsell positively and gives the client a choice rather than a rejection. You will close 60-70% of these add-on requests.
{{% /accent-box %}}

## Check-In: Module 5 Complete

- [ ] Revision policy defined and communicated to all clients
- [ ] Review Tracking Zap logs all Frame.io comments to Notion
- [ ] Revision Deadline Enforcer prevents overdue reviews from blocking production
- [ ] Scope creep is identified and converted to add-on opportunities
- [ ] Revision count is tracked per project

5 checkmarks. Revision management protects your margins. Do not skip it.

---

# MODULE 6: CONTENT CALENDAR AND SCHEDULING

## Overview

Producing videos is only half the job. Delivering them on a consistent schedule is what keeps clients paying month after month. This module builds an automated content calendar that ensures every client receives their videos on time, every time.

**Time to complete:** 2-3 hours
**Tools needed:** Notion, Zapier, Google Sheets

## Procedure 6.1: Build the Content Calendar System

Create a Notion database called `Content Calendar` with these columns:

| Column | Type |
|---|---|
| Video Title | Title |
| Client | Relation |
| Video Type | Select |
| Script Due | Date |
| Production Start | Date |
| Review Date | Date |
| Delivery Date | Date |
| Platform | Multi-select: YouTube, Instagram, TikTok, LinkedIn, Website |
| Status | Select: Planned, Scripting, Production, Review, Delivered |

## Procedure 6.2: Build the Automated Scheduling Workflow

Create a Zap: "Content Calendar Scheduler."

**Trigger:** New project added to the Project Tracker
**Step 1:** Code by Zapier → Calculate all dates based on the delivery deadline:

For a 60-second social clip (5-day production):
- Script due: Delivery - 5 days
- Production start: Delivery - 4 days
- Review: Delivery - 2 days
- Delivery: Client's specified date

For a 3-minute explainer (10-day production):
- Script due: Delivery - 10 days
- Production start: Delivery - 8 days
- Review: Delivery - 3 days
- Delivery: Client's specified date

For a 10-minute faceless video (15-day production):
- Script due: Delivery - 15 days
- Production start: Delivery - 12 days
- Review: Delivery - 4 days
- Delivery: Client's specified date

**Step 2:** Notion → Add all dates to the Content Calendar
**Step 3:** Gmail → Send the client a production schedule

## Procedure 6.3: Build the Deadline Alert System

Create a Zap: "Deadline Alerts."

**Trigger:** Schedule → Check every morning at 8 AM
**Step 1:** Notion → Find all projects with deadlines within the next 48 hours
**Step 2:** Slack → Send alerts for:
- Scripts due today
- Videos entering production today
- Client reviews due today
- Final deliveries due today

This prevents missed deadlines — the number one reason clients cancel video retainers.

{{% accent-box %}}
**HACK:** Offer clients a "content batch" option where you produce an entire month's worth of videos in one production sprint. Instead of producing 4 social clips spread across the month, produce all 4 in the first week. This lets you batch AI generation (run multiple HeyGen/Runway jobs simultaneously), batch editing (assemble all clips in one CapCut session), and batch review (client reviews everything in one Frame.io session). Batching reduces production time by 40% and increases your effective hourly rate by 2x.
{{% /accent-box %}}

## Check-In: Module 6 Complete

- [ ] Content Calendar database created in Notion
- [ ] Automated Scheduling Workflow calculates and populates all dates
- [ ] Deadline Alert System sends daily notifications
- [ ] Content batch option designed and ready to offer clients

4 checkmarks. Consistency is what separates professional agencies from hobbyists.

---

# MODULE 7: CLIENT ONBOARDING — SETTING EXPECTATIONS

## Overview

A smooth onboarding process prevents 80% of client problems. When expectations are clear, deliverables are defined, and communication channels are established from day one, the relationship runs smoothly. When onboarding is rushed or skipped, misunderstandings multiply and clients churn.

**Time to complete:** 2-3 hours
**Tools needed:** Notion, Zapier, Gmail

## Procedure 7.1: Create the Onboarding Package

Build a Notion template called "Client Onboarding" that includes:

1. **Welcome Email** — Sent within 1 hour of signing
2. **Brand Guide Questionnaire** — Google Form collecting: logo files, brand colors (hex codes), preferred fonts, tone of voice, competitor examples, brand dos and don'ts
3. **Content Strategy Brief** — Google Form collecting: target audience, key messages, preferred video types, posting frequency, platform priorities
4. **Review and Approval Workflow** — Frame.io tutorial for the client (2-minute Loom video)
5. **Content Calendar** — First month's planned videos with dates
6. **Communication Protocols** — How and when to reach you, expected response times

## Procedure 7.2: Build the Onboarding Automation

Create a Zap: "New Client Onboarding."

**Trigger:** Paystack → New subscription created (or manual trigger in Notion)
**Step 1:** Gmail → Send welcome email with brand guide questionnaire link
**Step 2:** Notion → Create client folder with all onboarding templates
**Step 3:** Frame.io → Create a project folder for the client
**Step 4:** Notion → Add client to the Content Calendar
**Step 5:** Slack → Notify `#new-clients` channel

## Procedure 7.3: Build the Brand Asset Storage System

Create a Google Drive folder structure for each client:

```
Client Drive/
├── Brand Assets/
│   ├── Logo Files/
│   ├── Brand Guidelines/
│   ├── Fonts/
│   └── Color Palette/
├── Scripts/
├── Storyboards/
├── Production Files/
├── Final Deliverables/
│   ├── YouTube/
│   ├── Instagram/
│   ├── TikTok/
│   └── Website/
└── Reviews/
```

Save the brand guide questionnaire responses here once the client submits them. Every video you produce must reference this folder for brand consistency.

{{% accent-box %}}
**HACK:** During onboarding, ask the client to share their top 3 competitor videos and their top 3 favorite videos (not necessarily in their industry). The competitor videos show you what to differentiate from. The favorite videos show you the aesthetic and emotional tone the client aspires to. This single question prevents more revision rounds than any other onboarding step.
{{% /accent-box %}}

## Check-In: Module 7 Complete

- [ ] Client Onboarding Package with all 6 components
- [ ] Onboarding Automation Zap sends welcome email and sets up client infrastructure
- [ ] Brand Asset Storage System with folder structure
- [ ] Brand guide questionnaire captures all essential information
- [ ] Competitor and favorite video references collected

5 checkmarks. Good onboarding prevents bad relationships.

---

# MODULE 8: PRICING AND PACKAGES — MONETIZING YOUR AGENCY

## Overview

Pricing is the difference between a hobby and a business. This module gives you the exact pricing tiers, package structures, and upsell strategies that maximize revenue while delivering clear value to clients.

**Time to complete:** 2-3 hours
**Tools needed:** Notion, Paystack

## Procedure 8.1: Define Your Service Packages

### Starter Package — ₦100,000/month (₦200K setup)

Deliverables per month:
- 4 social media clips (15-60 seconds each)
- 1 short explainer video (60-90 seconds)
- Basic captions and branding
- 2 rounds of revisions per video

Your cost: ~₦15,000 in AI tools + 4-6 hours of assembly time
Your margin: 80%+

Best for: Small businesses, startups, solopreneurs

### Growth Package — ₦250,000/month (₦400K setup)

Deliverables per month:
- 8 social media clips
- 2 explainer videos (60-90 seconds)
- 1 product demo or testimonial video (2-3 minutes)
- Advanced captions, animations, and transitions
- 3 rounds of revisions per video
- Monthly content strategy call

Your cost: ~₦40,000 in AI tools + 8-12 hours
Your margin: 78%+

Best for: Growing businesses with active social media presence

### Enterprise Package — ₦500,000/month (₦750K setup)

Deliverables per month:
- 15 social media clips
- 4 explainer videos
- 2 long-form faceless YouTube videos (8-15 minutes)
- Full branding, custom animations, premium voiceovers
- 5 rounds of revisions per video
- Weekly strategy calls
- Priority turnaround (3-day production for social clips)

Your cost: ~₦80,000 in AI tools + 15-20 hours
Your margin: 75%+

Best for: Agencies, media companies, large brands

## Procedure 8.2: Define Add-On Services

| Add-On | Price | Description |
|---|---|---|
| Extra social clip | ₦25,000 | Additional 15-60 second clip |
| Extra explainer | ₦75,000 | Additional 60-90 second explainer |
| Rush delivery | 50% surcharge | Same-day or next-day turnaround |
| Custom avatar (HeyGen) | ₦50,000 one-time | Client-specific AI avatar creation |
| YouTube SEO package | ₦50,000/month | Titles, descriptions, tags, thumbnails |
| Multi-language version | ₦30,000 per language | Translate and voiceover in additional languages |
| Raw project files | ₦25,000 | Deliver editable CapCut project files |

## Procedure 8.3: Build the Proposal Generator

Create a Zap: "Proposal Generator."

**Trigger:** Discovery call completed (logged in Notion)
**Step 1:** OpenAI → Generate a personalized proposal based on the client's needs:

```
You are a video agency sales consultant. Given a discovery call summary, generate a proposal that:
1. Reflects the client's specific goals and challenges
2. Recommends the appropriate package tier
3. Includes relevant add-ons based on their needs
4. Shows clear ROI expectations (projected views, engagement rates, brand awareness metrics)
5. Includes a comparison to traditional video production costs
```

**Step 2:** Notion → Create the proposal page
**Step 3:** Gmail → Send the proposal to the client

{{% accent-box %}}
**HACK:** Always show the traditional production cost alongside your price. A 60-second explainer video from a traditional agency costs ₦500,000-2,000,000 and takes 4-6 weeks. Your AI-powered version costs ₦100,000/month (as part of a package) and takes 5-7 days. Frame it as: "Traditional agency: ₦1.5M per video, 6-week timeline. Menshly AI Video: ₦100K/month for 4+ videos, 5-day timeline." The comparison is so stark that most prospects sign immediately.
{{% /accent-box %}}

## Check-In: Module 8 Complete

- [ ] Three service packages defined with clear deliverables and margins
- [ ] Add-on services priced and documented
- [ ] Proposal Generator Zap creates personalized proposals
- [ ] Pricing comparison framework ready for sales conversations

4 checkmarks. Pricing is where your business becomes profitable or stays broke.

---

# MODULE 9: ANALYTICS AND REPORTING — PROVING ROI

## Overview

Clients cancel when they cannot see results. This module builds automated reporting that proves the ROI of your video content every month. When a client can see that your videos generated 50,000 views, 2,000 clicks, and 15 new leads — they never cancel.

**Time to complete:** 2-3 hours
**Tools needed:** Zapier, Google Sheets, OpenAI API

## Procedure 9.1: Build the Monthly Performance Report

Create a Zap: "Monthly Video Performance Report."

**Trigger:** Schedule → 3rd of each month
**Step 1:** Google Sheets → Pull video performance data (views, engagement, clicks, shares)
**Step 2:** OpenAI → Generate performance analysis:

```
You are a video marketing analyst. Given performance data for the month's videos, write a report that:
1. Highlights the top-performing video and why it worked
2. Identifies underperforming videos with improvement suggestions
3. Calculates the cost per view and cost per engagement
4. Compares performance to industry benchmarks
5. Recommends content adjustments for next month
```

**Step 3:** Gmail → Send the report to the client
**Step 4:** Notion → Update the client dashboard

## Procedure 9.2: Build the ROI Calculator

Create a Google Sheet that calculates:

- **Cost per video** = Monthly retainer / Videos delivered
- **Cost per view** = Monthly retainer / Total views
- **Cost per engagement** = Monthly retainer / Total engagements
- **Estimated lead value** = Leads generated × Average deal value × Close rate
- **ROI** = (Estimated lead value - Monthly retainer) / Monthly retainer × 100

When the ROI is positive (and it usually is after month 2-3), highlight it prominently in the monthly report.

{{% accent-box %}}
**HACK:** Track "earned media value" — the equivalent advertising cost of the organic reach your videos generate. If your client's YouTube video gets 10,000 views and YouTube ads in their industry cost $0.10 per view, the earned media value is $1,000. For a client paying ₦100,000/month (≈$65), you are delivering 15x their investment in advertising-equivalent value. This metric alone justifies the retainer.
{{% /accent-box %}}

## Check-In: Module 9 Complete

- [ ] Monthly Performance Report Zap generates and delivers reports
- [ ] AI performance analysis provides specific, actionable recommendations
- [ ] ROI Calculator sheet computes cost per view and cost per engagement
- [ ] Earned media value tracked and reported

4 checkmarks. Prove your value, and clients will never leave.

---

# MODULE 10: SCALING — FROM SOLO EDITOR TO VIDEO AGENCY

## Overview

You have a working practice with 3-5 clients, automated production, and positive cash flow. This module takes you from solo operator to a scalable video agency. You will hire editors, build team workflows, and create the infrastructure to grow from 5 clients to 50.

**Time to complete:** 4-6 hours (ongoing)
**Tools needed:** Everything from previous modules, plus hiring tools

## Procedure 10.1: Hire Your First Video Editor

When you reach 5+ active clients, hire a junior video editor. The ideal candidate knows CapCut, understands social media video formats, and can follow your SOPs for assembly and quality control.

Pay range: ₦120,000-200,000/month (Nigeria) or $2,000-3,500/month (remote global).

The editor handles: CapCut assembly, caption correction, quality control checks, and Frame.io uploads. You continue handling: script writing, AI generation, client communication, and strategy.

## Procedure 10.2: Build the Team Production Workflow

Create a Notion page called "Team Workflow" with a Kanban board:

| Column | Owner | Tasks |
|---|---|---|
| Briefing | You | Review brief, generate script |
| AI Generation | You | Run HeyGen, Runway, ElevenLabs, Fliki |
| Assembly | Editor | CapCut assembly, captions, branding |
| QC | Editor | Quality control checklist |
| Review | You | Internal review before client |
| Client Review | Client | Frame.io review |
| Revisions | Editor | Implement feedback |
| Delivery | Editor | Export and deliver final files |

This workflow lets you produce 3-4x more videos per week by delegating assembly and QC to the editor while you focus on creative direction and AI generation.

## Procedure 10.3: Revenue Scaling Projections

| Month | Revenue | Clients | Videos/Month | Team | Notes |
|---|---|---|---|---|---|
| 1 | ₦0-300K | 0-2 | 0-10 | 1 (you) | Free samples converting |
| 3 | ₦600K-1.2M | 3-5 | 20-40 | 1 | Retainers compounding |
| 6 | ₦1.8M-3.6M | 8-15 | 60-120 | 2-3 | First editor hired |
| 9 | ₦3.6M-6M | 15-25 | 120-200 | 4-5 | Senior creative added |
| 12 | ₦6M-10M | 25-40 | 200-350 | 6-8 | Full video production agency |
| 18 | ₦10M-20M | 40-60 | 350-500 | 10-15 | Multiple specializations |
| 24 | ₦20M-35M | 60-100 | 500-800 | 15-25 | Regional market leader |

{{% accent-box %}}
**HACK:** Create a "white-label video agency" model where marketing agencies resell your video services under their own brand. The agency handles the client relationship; you handle the production. Price the white-label service at 60-70% of your retail price. The agency marks it up and pockets the difference. One mid-size marketing agency with 20 clients can generate 15-20 video retainers for you — that is ₦1.5M-3M/month in revenue from a single partnership. The agency wins (higher margins than producing video in-house), the client wins (better videos at lower cost), and you win (steady production volume with zero client acquisition cost).
{{% /accent-box %}}

## Check-In: Module 10 Complete

- [ ] Video Editor job posting created
- [ ] Team Production Workflow defined in Notion
- [ ] Delegation boundaries clear between creative and production tasks
- [ ] Revenue scaling projections documented
- [ ] White-label partnership model designed

5 checkmarks. Scaling is about building systems that produce quality at volume.

---

# FINAL VERIFICATION: THE COMPLETE AGENCY CHECKLIST

Before declaring your agency operational, verify every item across all 10 modules:

**Infrastructure:**
- [ ] Notion Command Center with 7 sub-pages
- [ ] Paystack account with 6 payment products
- [ ] Professional email on custom domain
- [ ] Frame.io workspace configured

**AI Tools:**
- [ ] HeyGen tested with sample avatar video
- [ ] Runway ML tested with sample B-roll generation
- [ ] Fliki tested with sample social clip
- [ ] ElevenLabs tested with sample voiceover
- [ ] CapCut installed and tested
- [ ] Canva Pro active
- [ ] Midjourney generating storyboard images

**Automation:**
- [ ] Script Generator Zap working
- [ ] Storyboard Generator Zap working
- [ ] Explainer Video Production Pipeline working
- [ ] Social Clip Production Pipeline working
- [ ] Faceless YouTube Production Pipeline working
- [ ] Review Tracking Zap working
- [ ] Content Calendar Scheduler working
- [ ] Deadline Alert System working
- [ ] Client Onboarding Zap working
- [ ] Monthly Performance Report working

**Operations:**
- [ ] Client Roster database
- [ ] Project Tracker database
- [ ] Content Calendar database
- [ ] Revision policy defined
- [ ] Three service packages priced
- [ ] Add-on services documented
- [ ] Team Workflow defined

**25+ checkmarks required.** If you have them all, congratulations — you have a fully operational AI video production agency. If you are missing items, go back and complete them. The agency only works when every component is in place.

The video production industry is being rebuilt by AI right now. The agencies that learn to produce 10x the content at 1/10th the cost will replace those that do not. Your agency is built on that principle. Now go find your first client.
