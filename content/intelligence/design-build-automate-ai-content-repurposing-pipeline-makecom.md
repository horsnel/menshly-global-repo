---
title: "Build an AI Content Repurposing Pipeline with Make.com: The Complete Step-by-Step Guide"
date: 2026-04-29
category: "Implementation"
difficulty: "INTERMEDIATE"
readTime: "28 MIN"
excerpt: "The complete execution guide for building an AI content repurposing system — from Make.com scenario setup to automating 30+ content pieces from a single source."
image: "/images/articles/intelligence/design-build-automate-ai-content-repurposing-pipeline-makecom.png"
heroImage: "/images/heroes/intelligence/design-build-automate-ai-content-repurposing-pipeline-makecom.png"
relatedOpportunity: "/opportunities/ai-content-repurposing-agency-2026/"
---

This is the execution guide for building the AI content repurposing business we outlined in our opportunity deep-dive. Content repurposing is not about copying and pasting the same caption across three platforms. It is about taking one long-form asset — a YouTube video, a podcast episode, a webinar recording — and systematically transforming it into 30+ platform-native pieces of content, each optimized for the algorithm, audience behavior, and format constraints of its destination platform. This guide covers every Make.com scenario, every ChatGPT prompt template, every Canva configuration, every Fliki AI video setting, every Buffer schedule, and every Beehiiv newsletter integration. Follow it in order. Do not skip steps. By the end, you will have a fully automated pipeline that turns a single piece of source content into an entire week's worth of multi-platform output.

## Prerequisites

Before you build anything, set up these accounts. Every tool listed here has a free tier or free trial. You will not spend money until you have paying clients.

**Required accounts (create these now):**

- **Make.com** — go to make.com and sign up. Free tier includes 1,000 operations per month and 2 active scenarios. This is your orchestration layer — every module, trigger, and data flow runs through Make.com.
- **ChatGPT API** — go to platform.openai.com and create an account. Add $5-10 of API credit. You will use the API (not the chat interface) inside Make.com for automated content generation. If you prefer to test prompts manually first, sign up for ChatGPT Plus ($20/mo) at chat.openai.com for GPT-4o access.
- **Canva** — go to canva.com and sign up. Free tier includes basic templates and 5GB storage. You will use Canva for quote card graphics, Instagram story templates, and branded visual assets.
- **Fliki AI** — go to fliki.ai and sign up. Free tier includes 5 minutes of video per month. You will use Fliki AI to convert text scripts into short-form video clips with AI voiceover and stock visuals.
- **Buffer** — go to buffer.com and sign up. Free tier includes 3 social channels and 10 scheduled posts per channel. You will use Buffer to schedule and publish content across Twitter/X, LinkedIn, and Instagram.
- **Beehiiv** — go to beehiiv.com and sign up. Free tier includes up to 2,500 subscribers. You will use Beehiiv to compose and send email newsletters from repurposed content.

**Recommended supplementary accounts:**

- **Notion** — go to notion.so and sign up. Free tier includes unlimited pages. You will use Notion for client dashboards, content calendars, and reporting.
- **Grammarly** — go to grammarly.com and sign up. Free tier includes basic grammar and spelling checks. Run every AI output through Grammarly before delivery.
- **Loom** — go to loom.com and sign up. Free tier includes 25 videos per month. You will use Loom to record client onboarding walkthroughs and QC review explanations.
- **Google Workspace** — go to workspace.google.com. You need Google Drive for file storage, Google Sheets for tracking, and Google Docs for transcript storage.

**Time required:** 10-14 hours for your first complete pipeline build, from Make.com account creation to end-to-end test with 30+ content pieces generated.

**Total upfront cost:** $0 if you use free tiers for everything. ~$20/mo if you upgrade to ChatGPT Plus for prompt testing. ~$5-10 one-time if you add OpenAI API credit. Everything else is free until you have paying clients. Expect to invest ~$100/mo once you have 2-3 active clients and need paid tiers for volume.

## Step 1: Set Up Your Make.com Workspace

Before you drag a single module onto the Make.com canvas, you need a clean workspace with proper folder structure, team settings, and API connections. A disorganized workspace leads to broken scenarios, lost API keys, and hours of debugging. Set it up right the first time.

### Create Your Make.com Account and Team

Go to make.com and sign up with your Google account or email. After verifying your email, you land on the Make.com dashboard. You should see a left sidebar with Scenarios, Connections, Templates, and Organization sections.

If you plan to work with contractors or virtual assistants later, set up a team now. Click **Organization** in the left sidebar → **Teams** → **Create a Team**. Name it "Content Repurposing Agency." Add team members later when you hire. For now, this creates a clean separation between personal and work scenarios.

### Create Your Scenario Folder Structure

In the Make.com dashboard, click **Scenarios** in the left sidebar. You should see an empty scenarios list. Click the **folder icon** at the top of the scenarios list → **Create Folder**. Create these five folders:

- `01_Ingest` — scenarios that watch for new content and transcribe it
- `02_Transform` — scenarios that generate platform-specific content from transcripts
- `03_Produce` — scenarios that create visual and video assets
- `04_Distribute` — scenarios that schedule and publish content
- `05_Utilities` — helper scenarios, error handlers, and data routing

This folder structure mirrors your pipeline stages. When something breaks, you know exactly which folder to check. When onboarding a new client, you duplicate scenarios within the same folders and update the client-specific parameters.

### Connect Your API Services

Click **Connections** in the left sidebar. You should see an empty connections list. Click **Add Connection** and add these services one by one:

1. **Google Drive** — Search for "Google Drive," click it, click **Create a connection**, and authenticate with your Google Workspace account. Grant all requested permissions. If you skip a permission checkbox, the connection appears to succeed but fails when modules try to access files. After authentication, you should see "Connected" in green.

2. **OpenAI** — Search for "OpenAI," click it, click **Create a connection**. Enter your OpenAI API key (from platform.openai.com/api-keys — click "Create new secret key," copy it immediately, you cannot view it again). After entering the key, you should see "Connected" in green.

3. **Google Sheets** — Search for "Google Sheets," click it, click **Create a connection**, and authenticate with the same Google Workspace account. Grant all permissions.

4. **Slack** (or Gmail) — Search for "Slack," click it, click **Create a connection**, and authenticate with your Slack workspace. You will use this for pipeline notifications. If you do not use Slack, connect Gmail instead.

5. **Buffer** — Search for "Buffer," click it, click **Create a connection**, and authenticate with your Buffer account.

6. **HTTP** — This is not a connection but a module type. Make.com includes it by default. You will use HTTP modules to call the Fliki AI and Canva APIs since Make.com does not have native integrations for these.

After connecting all services, verify each one. Click the three dots next to each connection → **Test**. A successful test returns "Connection is working." If any test fails, delete the connection and re-authenticate. Common failure: Google OAuth requires you to select the specific Google account and grant every permission — skipping one causes silent failures later.

### Set Up Your Google Drive Folder Structure

Open Google Drive. Create a main folder called `Content Repurposing`. Inside it, create these subfolders:

- `01_Inbox` — where raw video and audio files land for processing
- `02_Transcripts` — where OpenAI Whisper transcriptions are saved
- `03_AI_Outputs` — where ChatGPT-generated text assets are stored by platform
- `04_Produced` — where Fliki videos and Canva graphics are saved
- `05_Deliverables` — where final reviewed content waits for client approval
- `06_Archive` — where old content is moved after delivery

Inside `03_AI_Outputs`, create subfolders: `Twitter`, `LinkedIn`, `Instagram`, `Blog`, `Newsletter`, `Quotes`.

### Interactive Check-in

You should now have:

- ✓ Make.com account active with a dedicated team created
- ✓ Five scenario folders created: 01_Ingest, 02_Transform, 03_Produce, 04_Distribute, 05_Utilities
- ✓ Google Drive, OpenAI, Google Sheets, Slack, and Buffer connections all tested and showing "Connected"
- ✓ Google Drive folder structure created with all six main folders and the six AI_Output subfolders
- ✓ Clear understanding of the pipeline flow: Ingest → Transform → Produce → Distribute

If any Make.com connection shows "Not connected" or returns an error during testing, delete it and re-authenticate. Pay special attention to Google Drive permissions — you must grant access to "See, edit, create, and delete all your Google Drive files." If you choose "View only," your scenarios will fail when they try to create documents.

## Step 2: Build the Core Transcription and Extraction Module

This is the entry point of your pipeline. Every piece of repurposed content originates from a transcript. You will build a Make.com scenario that watches for new content, transcribes it using OpenAI Whisper, and extracts key quotes and topics. This module runs automatically once configured — no manual intervention required.

### Create the Ingest Scenario

1. In Make.com, click **Scenarios** → open the `01_Ingest` folder → click **Create a new scenario**. Name it "Content Ingest — YouTube RSS."

2. Add a **RSS — Retrieve RSS Feed Items** module as the trigger. Configure:
   - **Feed URL:** Enter the YouTube channel's RSS feed URL. The format is `https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID`. To find a channel ID, go to the YouTube channel page, view the page source, and search for `channelId`. Alternatively, use a YouTube channel ID finder tool.
   - **Limit:** Set to `1` (process one new video at a time)
   - **Schedule:** Set to run **Every 30 minutes** during business hours

   If you do not have a YouTube RSS feed yet, you can use a **Google Sheets — Watch Rows** trigger instead. Create a Google Sheet called "Content Input Queue" with columns: URL, Type, Status, Date Added. When a new row is added with Type = "YouTube," this trigger fires.

3. Add a **Text Parser** module to extract the video ID from the YouTube URL. Use this regex pattern: `(?:youtube\.com\/(?:watch\?v=|embed\/|v\/)|youtu\.be\/)([a-zA-Z0-9_-]{11})`. Map the RSS feed item's link URL as the input string. The output is the 11-character video ID.

4. Add an **HTTP — Make a Request** module to fetch the YouTube transcript. Configure:
   - **URL:** `https://youtube-transcript-api.example.com/transcript?video_id={{3.videoId}}` (replace with your actual hosted API endpoint — see the Replit script below)
   - **Method:** GET
   - **Headers:** `Content-Type: application/json`

   Alternatively, host a Python script on Replit that extracts YouTube transcripts:

   ```python
   from youtube_transcript_api import YouTubeTranscriptApi
   import json
   import sys

   video_id = sys.argv[1]
   try:
       transcript = YouTubeTranscriptApi.get_transcript(video_id)
       text = " ".join([entry['text'] for entry in transcript])
       print(json.dumps({"transcript": text, "video_id": video_id}))
   except Exception as e:
       print(json.dumps({"error": str(e), "video_id": video_id}))
   ```

   Deploy this on Replit as a web server (using Flask), then call it from Make.com via the HTTP module.

5. Add an **OpenAI — Create a Transcription** module (for audio/video file uploads, not YouTube). Configure:
   - **Connection:** Your OpenAI connection
   - **Model:** `whisper-1`
   - **File:** Map the downloaded file from the Google Drive module (if using file upload instead of YouTube)
   - **Language:** `en` (English — change if your clients produce content in other languages)
   - **Response format:** `text`

6. Add a **OpenAI — Create a Chat Completion** module for key quote extraction and topic identification. Configure:
   - **Model:** `gpt-4o`
   - **System Message:** `You are a content analyst. You extract key information from transcripts.`
   - **User Message:**

   ```
   Analyze the following transcript and extract:

   1. KEY QUOTES: Extract 5-7 quotable lines. Each quote must:
      - Make sense without context
      - Be 8-25 words long
      - Express an insight, opinion, or framework (not a fact)
      - Sound like something someone would highlight and share

   2. TOPIC IDENTIFICATION: Identify the 3-5 main topics discussed. For each topic, provide:
      - Topic name (2-4 words)
      - One-sentence summary of what was said about it
      - Relevance score (1-10, where 10 = most central to the content)

   3. CONTENT ANGLES: Suggest 3 different angles for repurposing this content:
      - The contrarian take
      - The how-to angle
      - The story-driven angle

   Format your response as structured text with clear section headers.

   Here is the transcript:
   {{5.transcriptionText}}
   ```

   - **Temperature:** 0.5 (lower temperature for extraction tasks — you want accuracy, not creativity)
   - **Max Tokens:** 1500

7. Add a **Google Docs — Create a Document** module. Configure:
   - **Title:** `{{2.videoTitle}}_transcript_{{formatDate(now; "YYYY-MM-DD")}}`
   - **Content:** Map the full transcript text from the HTTP or OpenAI module
   - **Folder:** Select your `02_Transcripts` folder

8. Add a second **Google Docs — Create a Document** module for the analysis. Configure:
   - **Title:** `{{2.videoTitle}}_analysis_{{formatDate(now; "YYYY-MM-DD")}}`
   - **Content:** Map the ChatGPT analysis output (quotes, topics, angles)
   - **Folder:** Select your `02_Transcripts` folder

9. Add a **Slack — Create a Message** module. Configure:
   - **Channel:** `#content-pipeline` (create this channel in your Slack workspace first)
   - **Text:** `:new: New content ingested: {{2.videoTitle}}. Transcript and analysis saved to Drive. Ready for transformation.`

10. Click **Save**. Set the scenario schedule to **Every 30 minutes** during business hours (8 AM - 8 PM in your timezone).

### Test the Ingest Pipeline

Add a YouTube URL to your RSS feed or Google Sheets input queue. Click **Run once** in Make.com. Check the scenario execution log. You should see each module execute in sequence:

- Module 1 (RSS/Sheets): Found the new content entry
- Module 2 (Text Parser): Extracted video ID successfully
- Module 3 (HTTP): Fetched transcript from API
- Module 4 (OpenAI Whisper — if using file upload): Transcription completed
- Module 5 (OpenAI ChatGPT): Key quotes, topics, and angles extracted
- Module 6 (Google Docs — Transcript): Document created in `02_Transcripts`
- Module 7 (Google Docs — Analysis): Document created in `02_Transcripts`
- Module 8 (Slack): Notification sent

If the HTTP module fails with a timeout, your Replit script may be sleeping (free tier sleeps after inactivity). Wake it by visiting the Replit URL in your browser, then re-run the scenario. If the OpenAI module fails with "File too large," the audio exceeds Whisper's 25MB limit — split it using ffmpeg: `ffmpeg -i input.mp3 -f segment -segment_time 600 -c copy output_%03d.mp3`.

Go to your `02_Transcripts` folder. Open the transcript document. Read through it — it should be clean with minimal errors. Open the analysis document — you should see extracted quotes, identified topics, and suggested content angles. This analysis document becomes the strategic input for Step 3.

### Handle Audio and Video File Uploads

For clients who send raw audio or video files instead of YouTube links, create a second ingest scenario:

1. Create a new scenario in the `01_Ingest` folder called "Content Ingest — File Upload."
2. Add a **Google Drive — Watch Files in a Folder** trigger. Configure:
   - **Folder:** Select your `01_Inbox` folder
   - **Watch:** Select "New files"
3. Add a **Filter** module. Condition: `File name` `Ends with` `.mp4` OR `File name` `Ends with` `.mp3` OR `File name` `Ends with` `.wav` OR `File name` `Ends with` `.m4a`.
4. Add a **Google Drive — Download a File** module. Map the File ID from the Watch module.
5. Add the same **OpenAI — Create a Transcription** module configured with `whisper-1`.
6. Add the same **OpenAI — Create a Chat Completion** module for quote and topic extraction.
7. Add the same Google Docs and Slack modules.

### Interactive Check-in

You should now have:

- ✓ YouTube RSS ingest scenario running and monitoring a channel for new videos
- ✓ File upload ingest scenario watching `01_Inbox` for new audio/video files
- ✓ Transcription pipeline working: YouTube URL or file upload → transcript generated → analysis document created → Slack notification sent
- ✓ Analysis document contains extracted quotes, identified topics, and suggested content angles
- ✓ Test transcript and analysis documents verified for accuracy in `02_Transcripts` folder

If the transcript quality is poor, check the audio source — Whisper achieves 95-98% accuracy on clear audio but struggles with heavy accents, background noise, or low-quality recordings. If the analysis document is missing quotes or topics, increase the Max Tokens to 2000 and re-run.

## Step 3: Create the Multi-Format Content Generator

This is the engine of your pipeline. You will build Make.com scenarios that take a transcript and analysis document and generate 5 different types of platform-native content using ChatGPT. Each output is voice-calibrated and platform-optimized. The prompts below are production-ready — copy them exactly.

### Set Up Voice Calibration

Every piece of content you generate must match the client's voice. Create a Google Sheet called "Voice Profiles" with these columns: Client Name, Tone, Vocabulary Patterns, Sentence Style, Go-To Frameworks, Emoji Usage, Forbidden Words, Signature Phrases, Audience Description.

Fill in one row per client. For your test client, analyze their existing content to extract these attributes. In Make.com, add a **Google Sheets — Search Rows** module at the start of each transformation scenario. Filter by Client Name. Map the voice profile fields into every ChatGPT system prompt.

### Build the Blog Post Module

1. In Make.com, open the `02_Transform` folder → click **Create a new scenario**. Name it "Transform — Blog Post."
2. Add a **Google Drive — Watch Files in a Folder** trigger. Point it to `02_Transcripts`.
3. Add a **Google Sheets — Search Rows** module to fetch the client's voice profile.
4. Add an **OpenAI — Create a Chat Completion** module. Configure:
   - **Model:** `gpt-4o`
   - **System Message:**

   ```
   You are writing in the voice of {{3.clientName}}. Their style is {{3.tone}}. They frequently use phrases like {{3.signaturePhrases}}. They never use words like {{3.forbiddenWords}}. Their audience is {{3.audienceDescription}}. They prefer {{3.sentenceStyle}}. Apply this voice to every piece of content you generate.
   ```

   - **User Message:**

   ```
   Transform the following transcript into a 1,800-2,500 word blog article.

   Instructions:
   - Do NOT summarize the entire transcript. Pick the single most valuable angle or insight and go deep on it.
   - Structure: Compelling headline (no clickbait), introduction (2-3 sentences that hook the reader), 4-6 sections with H2 headings, conclusion with a CTA.
   - Each section should include a specific example, anecdote, or data point from the transcript.
   - Write in short paragraphs (2-3 sentences max). Make it scannable.
   - Use bold text for key phrases a reader would want to skim.
   - Include at least two actionable takeaways the reader can implement today.
   - The tone should feel like a trusted mentor sharing hard-won knowledge, not a textbook.
   - Include a meta title (under 60 characters) and meta description (under 155 characters) at the top.

   Do not use these phrases: "In today's world," "It's important to note," "At the end of the day," "Let's dive in."

   Here is the transcript:
   {{2.transcriptText}}
   ```

   - **Temperature:** 0.7
   - **Max Tokens:** 4000

5. Add a **Google Docs — Create a Document** module. Save the output to `03_AI_Outputs/Blog`. Filename: `{{2.fileName}}_blog_article`.

### Build the Twitter Thread Module

Duplicate the Blog Post scenario. Rename it "Transform — Twitter Thread." Replace the ChatGPT user message with:

```
Transform the following transcript into a Twitter/X thread of 7-10 tweets.

Rules:
- Tweet 1 is the hook. One sentence that stops the scroll. No "Thread 🧵" — start with the insight.
- Tweets 2-8 each contain one standalone insight extracted from the transcript. Each must be valuable on its own.
- The final tweet is the CTA. Link to the original content or ask a question.
- Use line breaks between ideas within a tweet for readability.
- Do not use hashtags in the body of any tweet.
- Maximum 280 characters per tweet.
- Do not use phrases like "In this thread" or "Let me explain." Just deliver the insight.
- Sound like a real person sharing a genuine takeaway, not a summarizer.

Here is the transcript:
{{2.transcriptText}}
```

Set **Max Tokens:** 1500. Save the output to `03_AI_Outputs/Twitter`.

### Build the LinkedIn Post Module

Duplicate the scenario. Rename it "Transform — LinkedIn Post." Replace the ChatGPT user message with:

```
Transform the following transcript into a LinkedIn post.

Structure:
- Opening hook: One sentence that creates curiosity or states a contrarian take. Do not start with "I recently" or "Just had a realization."
- Body: 3-5 short paragraphs. Use the most compelling story or insight from the transcript. Each paragraph is 1-3 sentences max.
- Key takeaway: 1-2 sentences that distill the lesson.
- Closing: Ask a question that invites comments. Do not use "What do you think?" — use a specific question related to the content.
- Hashtags: 3-5 relevant hashtags at the very end, separated by spaces.

Formatting rules:
- Maximum 1,300 characters total including hashtags.
- Use double line breaks between paragraphs (LinkedIn needs the white space).
- No bullet points. LinkedIn's algorithm deprioritizes list-style posts.
- No external links in the body (LinkedIn penalizes posts with links). Put any link in the comments.

Here is the transcript:
{{2.transcriptText}}
```

Set **Max Tokens:** 1000. Save the output to `03_AI_Outputs/LinkedIn`.

### Build the Instagram Caption Module

Duplicate the scenario. Rename it "Transform — Instagram Caption." Replace the ChatGPT user message with:

```
Transform the following transcript into 3 separate Instagram Reel scripts and captions, each 30-60 seconds long. Each script should cover a different insight from the transcript.

Format each script exactly like this:

SCRIPT [NUMBER]: [Title]
[VISUAL: Describe what the viewer sees]
[TEXT OVERLAY: The 3-5 words that appear on screen — this is the pattern interrupt]
[VOICEOVER: What the person says — conversational, punchy, no filler]
[CAPTION: The Instagram caption text for this post]
[HASHTAGS: 15-20 relevant hashtags]

Rules for each script:
- Seconds 0-2: Pattern interrupt. The text overlay must stop the scroll. State something surprising or counterintuitive.
- Seconds 3-15: Deliver the core insight. One idea only.
- Seconds 15-25: Provide the "so what" — why this matters, what to do with it.
- Seconds 25-30: CTA — "Save this for later" or "Follow for more" or ask them to comment a specific word.
- Maximum 75 words in the voiceover. Every word earns its place.
- No "Hey guys" or "So today I want to talk about." Start mid-thought.

Here is the transcript:
{{2.transcriptText}}
```

Set **Max Tokens:** 2000. Save the output to `03_AI_Outputs/Instagram`.

### Build the Newsletter Summary Module

Duplicate the scenario. Rename it "Transform — Newsletter Summary." Replace the ChatGPT user message with:

```
Transform the following transcript into a 200-300 word email newsletter segment.

Structure:
- Subject line: 3-6 words. Curiosity-driven. No clickbait. Examples: "The thing nobody tells you about [topic]" or "[Number] mistakes I made with [topic]"
- Opening line: Jump straight into the insight. No "Hope you're having a great week." No "I wanted to share..."
- Body: One idea. One story from the transcript. Written like you're texting a smart friend.
- CTA: One clear action. "Reply and tell me [specific question]" or "Check out the full episode: [link]" or "Hit reply if you've experienced this."
- Sign-off: Use the client's usual sign-off style.

Rules:
- Maximum 300 words total.
- Write at a 6th grade reading level. Short words. Short sentences.
- No corporate newsletter energy. This should feel personal, not broadcast.
- One idea per email. If the transcript has five insights, pick the most surprising one.

Here is the transcript:
{{2.transcriptText}}
```

Set **Max Tokens:** 800. Save the output to `03_AI_Outputs/Newsletter`.

### Set Up the Master Orchestrator

Running 5 scenarios individually is inefficient. Build a master orchestration scenario that triggers all 5 transformations when a new transcript arrives.

1. Create a new scenario in `02_Transform` called "Transform — Master Orchestrator."
2. Add a **Google Drive — Watch Files** trigger pointing to `02_Transcripts`.
3. Add a **Make an API Call** or **HTTP — Make a Request** module for each transformation scenario. Make.com allows you to trigger other scenarios via webhook URLs. Set up a webhook in each transformation scenario first (add a **Webhooks — Custom Webhook** module as the first module in each scenario), then call those webhook URLs from the orchestrator.
4. When a new transcript lands, the orchestrator fires all 5 transformation scenarios simultaneously.

This cuts processing time from 5 sequential runs to 1 parallel run. A 30-minute video transcript processes through all 5 transformations in under 2 minutes.

### Interactive Check-in

You should now have:

- ✓ Voice calibration system pulling from Google Sheets Voice Profiles
- ✓ Blog post generation scenario built and tested
- ✓ Twitter thread generation scenario built and tested
- ✓ LinkedIn post generation scenario built and tested
- ✓ Instagram caption and Reel script generation scenario built and tested
- ✓ Newsletter summary generation scenario built and tested
- ✓ Each scenario saving output to the correct subfolder in `03_AI_Outputs`
- ✓ Master orchestrator scenario triggering all 5 in parallel
- ✓ Test run completed: one transcript → 5 types of content generated in `03_AI_Outputs`

Test the full pipeline: add a YouTube URL to your input queue or upload a test MP3 to `01_Inbox`. Wait for the Ingest scenario to create the transcript. Then run the Master Orchestrator. Check `03_AI_Outputs` — you should see 5 new documents across all subfolders. Open each one. Read through the content. Does it match the client's voice? Is it platform-appropriate? Are there factual errors? If the voice is off, adjust the voice profile in Google Sheets. If the content is too generic, add more specific instructions to the prompt templates.

## Step 4: Add Visual Content with Canva and Fliki AI

Text content is valuable, but video and visual content commands the highest engagement on social media. This step automates video production with Fliki AI and streamlines graphic creation with Canva. By the end, your pipeline produces both text and visual assets automatically.

### Auto-Generate Quote Cards with Canva

Canva's API allows automated design creation, but it requires a Canva Connect integration (available on Canva Pro, $13/mo). For your first deployment, create a batch-processing workflow that minimizes manual design time to under 60 seconds per graphic.

1. Open Canva. Click **Create a design** → **Instagram Post** (1080 x 1080px).
2. On the left sidebar, click **Templates**. Search for "quote post minimal." Select a clean template with large text and a simple background — the words should dominate, not the decoration.
3. Customize the template for your client: upload the client's logo, set brand colors (get hex codes from the client's brand guide or pick them from their website using a color picker extension), select brand fonts. Save this as a **Brand Template** by clicking **File → Save as template**. Name it "Quote_Dark_1."
4. Create 5-7 variants of the quote template: different background colors, different text placements, different font sizes. Save each as a separate template. Name them: "Quote_Dark_1", "Quote_Light_1", "Quote_Gradient_1", "Quote_Photo_Overlay_1", "Quote_Minimal_1", etc.
5. When processing a new batch of quotes from the analysis document (Step 2), open each template, paste the quote text, adjust font size to fit, and download as PNG. With practice, each graphic takes 45-60 seconds.

For automation at scale (5+ clients), integrate Canva's API:

1. In Make.com, add an **HTTP — Make a Request** module.
2. **URL:** `https://api.canva.com/rest/v1/designs`
3. **Method:** POST
4. **Headers:**
   ```
   Content-Type: application/json
   Authorization: Bearer YOUR_CANVA_API_KEY
   ```
5. **Body (JSON):**
   ```json
   {
     "design_type": "InstagramPost",
     "title": "{{quoteText}}",
     "asset_ids": ["YOUR_TEMPLATE_ASSET_ID"]
   }
   ```

This creates a new design from your template. You then use Canva's Autofill API to replace text elements programmatically. The Canva API documentation at canva.dev provides the full Autofill endpoint details.

### Generate Short-Form Video Clips with Fliki AI

Fliki AI converts text scripts into short-form videos with AI voiceover, stock footage, and text overlays. This is where your Instagram Reel scripts from Step 3 become actual video content.

1. Go to fliki.ai and sign in. You should see the Fliki dashboard with a "New File" button.
2. Click **New File**. Enter a title: "Reel Test." You should see the Fliki editor with a script input area on the left and a preview area on the right.
3. Test the video creation manually first. Paste one of your generated Instagram Reel scripts into the script area. Select a voice — choose one that matches your client's brand. Fliki offers 2,000+ AI voices across 75+ languages. For a professional male voice, try "Adam" or "Daniel." For a professional female voice, try "Rachel" or "Emma." Select a visual style: **Stock Footage** (best for educational and business content), **AI-Generated Images** (best for motivational and abstract content), or **Text-on-Screen** (best for data-driven and quote content). Click **Generate**. Wait 2-3 minutes for the video to render. Preview it. Download as MP4.
4. If the video looks good, automate this via Make.com. Create a new scenario in `03_Produce` called "Produce — Fliki Videos."
5. Add a **Google Drive — Watch Files** trigger pointing to `03_AI_Outputs/Instagram`.
6. Add an **HTTP — Make a Request** module. Configure:
   - **URL:** `https://api.fliki.ai/v1/generate`
   - **Method:** POST
   - **Headers:**
     ```
     Content-Type: application/json
     Authorization: Bearer YOUR_FLIKI_API_KEY
     ```
   - **Body (JSON):**
     ```json
     {
       "title": "{{1.fileName}}",
       "script": "{{2.fileContent}}",
       "voice": "rachel",
       "visual_style": "stock_footage",
       "aspect_ratio": "9:16",
       "duration": "auto"
     }
     ```

   If you see "401 Unauthorized," your Fliki API key is incorrect. Go to fliki.ai/app/settings, generate a new key, and update the Make.com module.

7. Add a **Sleep** module set to 180 seconds (3 minutes) — Fliki needs time to render the video.
8. Add an **HTTP — Make a Request** module to download the rendered video:
   - **URL:** `https://api.fliki.ai/v1/video/{{3.videoId}}/download`
   - **Method:** GET
9. Add a **Google Drive — Upload a File** module. Save the MP4 to `04_Produced` with the filename `{{1.fileName}}_reel.mp4`.

If Fliki's API does not fit your workflow, use Fliki manually for the first 3-5 clients and automate later. The manual process takes 5-7 minutes per Reel script, which is still 10x faster than traditional video editing.

### Create Instagram Stories

Instagram Stories are a high-engagement, low-effort format. Use Canva to create Story-sized graphics (1080 x 1920px) from your extracted quotes.

1. In Canva, click **Create a design** → **Instagram Story** (1080 x 1920px).
2. Select a template from the "Instagram Story" category. Choose one with a large text area and minimal graphic elements.
3. Paste a quote from the analysis document. Add the client's logo at the bottom. Add a subtle "Swipe up" or "Link in bio" CTA.
4. Download as PNG or MP4 (if using animated text). Save to `04_Produced`.

For automation, use the same Canva API approach described above, but change `"design_type": "InstagramPost"` to `"design_type": "InstagramStory"`.

### Build the Production QC Step

Add a quality control checkpoint before any content moves to distribution. Create a Google Sheet called "Production QC" with columns: Asset Name, Asset Type, Client Name, Status, Reviewer Notes, Approved Date, Scheduled Date. Every produced asset gets a row. Status starts as "Pending Review." After human review, status changes to "Approved" or "Needs Revision."

In Make.com, add a **Google Sheets — Add a Row** module to each production scenario that creates a QC entry. Then add a **Google Sheets — Search Rows** module to the Distribute stage (Step 5) that only processes assets where Status = "Approved." This gate prevents unreviewed content from being published.

Run every AI text output through Grammarly before marking it as "Pending Review." Copy the text from the Google Doc, paste it into the Grammarly editor, accept or dismiss suggestions, then paste the corrected version back into the Google Doc. This catches the 5-10% of errors that ChatGPT consistently makes: repeated words, missing articles, and awkward phrasing.

### Interactive Check-in

You should now have:

- ✓ Canva brand templates created for quote graphics (5-7 variants) and Instagram Stories (2-3 variants)
- ✓ Fliki AI configured and tested — can generate Reel videos from scripts manually
- ✓ Fliki AI automation scenario built in Make.com (or manual workflow documented)
- ✓ Production QC sheet set up and integrated into Make.com
- ✓ Grammarly review step integrated into your QC workflow
- ✓ At least 3 produced video clips and 5 quote graphics from your test content in `04_Produced`

If Fliki videos look robotic or low quality, try different visual styles. "Stock footage" works for educational content. "AI-generated images" works for motivational content. "Text-on-screen" works for data-driven content. Match the visual style to the content type. If Canva graphics feel generic, invest more time in template design — a distinctive template library is a competitive advantage.

## Step 5: Set Up Distribution with Buffer

Producing content is useless if it sits in a Google Drive folder. This step automates distribution via Buffer (social media scheduling) and Beehiiv (newsletter publishing). By the end, your pipeline automatically schedules approved content across all platforms.

### Connect Buffer to Your Social Accounts

1. Go to buffer.com and sign in. Click **Connect a Channel** in the left sidebar. Add your client's social accounts one by one:
   - **Twitter/X:** Click the Twitter icon, authenticate with the client's Twitter account (you need their login credentials or they can authenticate for you via a shared screen on Loom).
   - **LinkedIn:** Click the LinkedIn icon, authenticate with the client's LinkedIn account. For LinkedIn Company Pages, you need Page Admin access.
   - **Instagram:** Click the Instagram icon, authenticate with the client's Instagram Business or Creator account (personal accounts do not work with Buffer — the client must convert to Business or Creator in Instagram settings first).
   - **Facebook Page** (optional): Click the Facebook icon, authenticate with the client's Facebook Page.

   Each platform requires OAuth authentication. Buffer walks you through this. If any connection fails, the most common issue is using a personal Instagram account instead of a Business/Creator account. Have the client convert it first, then retry.

2. After connecting all accounts, go to Buffer's **Publishing Queue** view. You should see columns for each connected platform with empty scheduling slots.

### Build the Distribution Scenario in Make.com

1. In Make.com, open the `04_Distribute` folder → click **Create a new scenario**. Name it "Distribute — Social Posts."
2. Add a **Google Sheets — Search Rows** trigger. Point it to "Production QC" where Status = "Approved." Set it to run **Every 30 minutes** during business hours.
3. Add a **Router** module to split the workflow by content type. Create routes:
   - Route 1: Type = "Twitter" → Buffer Twitter module
   - Route 2: Type = "LinkedIn" → Buffer LinkedIn module
   - Route 3: Type = "Instagram" → Buffer Instagram module
   - Route 4: Type = "Newsletter" → Beehiiv module
4. For each social route, add a **Buffer — Create an Update** module. Configure:
   - **Profile IDs:** Select the client's account for that platform
   - **Text:** Map the approved content from the Google Drive file
   - **Media:** Map image or video URLs if applicable (for Instagram, you must include media — Buffer does not support Instagram posts without images)
   - **Scheduled At:** Calculate optimal posting time using Make.com's date functions:

### Optimize Posting Times

Research consistently shows these optimal posting windows. Configure them in Make.com using the `setDate` and `addHours` functions:

| Platform | Best Days | Best Time | Worst Days | Worst Time |
|----------|-----------|-----------|------------|------------|
| Twitter/X | Tue, Wed, Thu | 9:00 AM - 11:00 AM | Saturday | After 8 PM |
| LinkedIn | Tue, Wed, Thu | 8:00 AM - 10:00 AM | Sunday | After 6 PM |
| Instagram | Tue, Wed, Fri | 11:00 AM - 1:00 PM | Sunday | Late night |
| Newsletter | Tuesday | 6:00 AM - 8:00 AM | Friday | Afternoon |

In Make.com, use a **Set Variable** module before each Buffer module to calculate the next optimal posting time:

```
{{if(dayOfWeek(now) = 1; setDate(now; "next tuesday 9:00"); if(dayOfWeek(now) = 5; setDate(now; "next tuesday 9:00"); addDays(now; 1))}}
```

This ensures content is always scheduled for the next optimal window, never on a low-engagement day.

### Set Up Analytics Tracking

After content is published, you need to track performance. Build a tracking loop:

1. In Buffer, go to **Analytics** → review each post's performance metrics (impressions, engagements, click-throughs, shares).
2. Create a Google Sheet called "Content Performance Tracker" with columns: Asset Name, Platform, Publish Date, Impressions, Engagements, CTR, Shares, Notes.
3. In Make.com, create a scenario in `05_Utilities` called "Analytics — Weekly Pull." Schedule it to run every Monday at 9 AM. Use the **Buffer — List Updates** module to fetch the previous week's posts, then use **Google Sheets — Add Rows** to log the metrics. This builds a performance dataset over time that informs your content strategy.

### Configure Beehiiv for Newsletter Distribution

1. Go to beehiiv.com and sign in. Create a new publication if you haven't already. Set up basic branding: logo, colors, footer text, sender name and email address.
2. Import your subscriber list (or start with a test list of your own email addresses).
3. In Make.com, add Beehiiv as a connected service. Go to Connections → Add Connection → search for "Beehiiv." Enter your Beehiiv API key (found in your publication settings under **Integrations → API**).
4. Add a Beehiiv route to the Router module in your Distribute scenario. Configure:
   - **Module:** Beehiiv — Create a Post
   - **Title:** Map the newsletter subject line from the approved content
   - **Content:** Map the newsletter body from the Google Drive file
   - **Status:** Set to "Draft" (never auto-publish without review)
   - **Audience:** Select "All subscribers" or the appropriate segment
5. After the Beehiiv module, add a **Google Sheets — Update Row** module to mark the newsletter as "Scheduled" in the Production QC sheet.

### Distribution Pricing Table

If you are building this pipeline as a service, here is how to price the distribution component:

| Service | What's Included | Monthly Price |
|---------|----------------|---------------|
| Social Only | Twitter + LinkedIn + Instagram scheduling via Buffer, 20+ posts/mo | Included in retainer |
| Social + Newsletter | All social platforms + Beehiiv newsletter management (1 send/week) | +$500/mo |
| Full Distribution | Social + newsletter + blog publishing + analytics reporting + performance optimization | +$1,000/mo |

### Interactive Check-in

You should now have:

- ✓ Buffer connected to all client social accounts (Twitter, LinkedIn, Instagram)
- ✓ Beehiiv connected with publication configured and API key stored in Make.com
- ✓ Distribute scenario running: approved content → scheduled in Buffer → queued in Beehiiv
- ✓ Optimal posting times configured for each platform
- ✓ Analytics tracking scenario pulling weekly performance data into Google Sheets
- ✓ Distribution log tracking every piece of content distributed
- ✓ Full end-to-end test completed: upload source content → 30+ assets distributed across all platforms

Run a full end-to-end test now. Upload a test MP3 to `01_Inbox`. Watch it flow through Ingest → Transform → Produce → Distribute. Verify that content appears in Buffer's scheduling queue for each platform and in Beehiiv's draft posts. This full pipeline test should take 15-20 minutes from upload to distribution. If any stage fails, check the Make.com execution log for the failing module and debug from there.

## Step 6: Scale to Multiple Clients

You have a working pipeline for one client. Now you turn it into a system that handles 10+ clients without collapsing. Scaling requires template workflows, standardized onboarding, reporting dashboards, and eventually, hiring help.

### Template Workflows for Client Duplication

When a new client signs, you should not be building scenarios from scratch. Instead, duplicate existing scenarios and update client-specific parameters.

1. In Make.com, open each scenario folder. For each scenario, click the **three dots** → **Clone**. Rename the clone with the client's name prefix: `[ClientName] Transform — Blog Post`.
2. Update the cloned scenario's client-specific parameters:
   - Google Drive folder paths (point to the client's folder structure)
   - Voice profile reference in the Google Sheets Search module
   - Buffer account connections (the client's social accounts)
   - Beehiiv publication ID
   - Slack notification channel
3. Test each cloned scenario individually before activating the full pipeline.

At 3+ clients, this cloning process becomes tedious. Create a Make.com template scenario that uses variables instead of hardcoded values. Store client configuration in a "Client Config" Google Sheet with columns: Client Name, Drive Folder ID, Voice Profile Row, Buffer Profile IDs, Beehiiv Publication ID, Slack Channel. Each scenario reads the client config from this sheet at runtime, eliminating the need to clone scenarios per client.

### Client Onboarding Process

Follow this exact 5-step onboarding for every new client. Record the process using Loom for future reference and team training:

1. **Voice Calibration (Day 1):** Collect 10-15 existing posts from the client across all platforms. Feed them into ChatGPT to generate a voice profile. Save the profile in your Voice Profiles Google Sheet. Send the profile to the client for review using a Loom video that walks through each attribute and explains how it was derived. Get written confirmation.

2. **Account Setup (Day 1-2):** Connect the client's social accounts to Buffer. Set up Beehiiv publication or connect to their existing email tool. Create all Google Drive folders for the client. Create the client's Canva brand kit. Record a Loom walkthrough of the connected accounts for the client's reference.

3. **Pipeline Configuration (Day 2-3):** Duplicate or configure all Make.com scenarios for the new client. Update folder paths, voice profile references, and Buffer/Beehiiv connections. Test each scenario individually. Verify the Production QC sheet has a row template for the new client.

4. **Test Run (Day 3-4):** Process one piece of the client's content through the full pipeline. Deliver all outputs for review using the delivery template. Get feedback. Adjust voice calibration and prompt parameters. Common adjustments: tone too formal (add "Write like you're texting a smart friend" to system prompt), too many hashtags (reduce hashtag count in prompt), missing industry jargon (add specific terms to voice profile).

5. **Go Live (Day 5):** Start weekly production. Set the recurring schedule. Confirm the client knows when to expect deliveries and how to provide source content. Create a Notion page for the client with their content calendar, delivery log, and feedback section.

### Reporting Dashboards in Notion

Clients who see data stay clients. Build a Notion dashboard for each client that shows:

1. **Content Pipeline Status** — A kanban board with columns: Inbox, Transcribing, Transforming, In Review, Approved, Scheduled, Published. Each card is a piece of content moving through the pipeline.

2. **Weekly Delivery Summary** — A table showing every piece of content delivered this week, organized by platform. Include the content angle (e.g., "Contrarian take on pricing"), the platform, and the scheduled publish time.

3. **Performance Metrics** — A linked database that pulls from your Content Performance Tracker Google Sheet. Show impressions, engagement rate, and CTR for each post. Update weekly.

4. **Feedback Log** — A running list of client feedback with columns: Date, Feedback, Action Taken, Status. This creates accountability and shows the client you are responsive.

Create a Notion template for this dashboard. Duplicate it for each new client. Share the page with the client so they have real-time visibility into their content pipeline. This reduces "Where is my content?" emails by 90%.

### Hire Editors to Scale Quality

At 1-3 clients, you review every piece of content yourself. This takes 10-15 hours per week. At 4+ clients, you need help.

**Hire a content editor ($20-30/hr, 20 hrs/week).** This person handles the QC step — reviewing AI outputs, fixing voice mismatches, running content through Grammarly, approving distributions. Post the job on Upwork, OnlineJobs.ph, or WeWorkRemotely. Look for candidates with social media management experience and strong writing skills. Give them this guide as their training manual. Record a Loom video showing your exact QC process. Have them do a test run with a real transcript before hiring.

**At 8-12 clients, hire a pipeline operator ($15-25/hr, part-time).** This person monitors Make.com scenarios, troubleshoots errors, ensures the pipeline runs without interruption, and handles the manual steps (Canva graphics, Fliki video generation) that are not yet fully automated.

**At 12+ clients, add a sales representative ($40-60K base + 15% commission on first-month revenue).** This person handles prospecting, outreach, and closing new deals. You focus exclusively on operations and strategy.

### Margin Analysis

| Item | Per Client (Growth Tier) |
|------|-------------------------|
| Revenue (monthly) | $3,000 |
| Make.com costs | ~$15-25/mo |
| ChatGPT/OpenAI API | ~$30-60/mo |
| Fliki AI | ~$20-40/mo |
| Canva Pro | ~$13/mo (shared across clients) |
| Buffer | ~$6-15/mo per client |
| Beehiiv | ~$0-25/mo (free under 2,500 subs) |
| Content editor (allocated) | ~$100-150/mo |
| **Gross profit (monthly)** | ~$2,680-2,820/mo |

At 10 Growth-tier clients: $30,000/mo revenue, ~$2,500/mo in tool costs, ~$4,000/mo in editor costs. Net profit: ~$23,500/mo.

## Cost Breakdown

| Item | Free Tier | Paid Tier | When to Upgrade |
|------|-----------|-----------|-----------------|
| Make.com | 1,000 ops/mo, 2 scenarios | $9/mo (Core) | At 2+ clients — need more scenarios and operations |
| ChatGPT / OpenAI API | Free (GPT-3.5) / Pay per use | $20/mo (Plus) / ~$30-60/mo API per client | Immediately for GPT-4o quality; API scales with volume |
| Canva | Free tier | $13/mo (Pro) | At first client — need brand kits, premium templates, and API access |
| Fliki AI | 5 min video/mo | $21/mo (Standard) | At 2+ clients — 5 minutes is one short reel |
| Buffer | 3 channels, 10 posts | $6/mo per channel | At first client — need more channels and posts |
| Beehiiv | 2,500 subscribers | $49/mo (Scale) | When a client's list exceeds 2,500 subscribers |
| Notion | Free | $10/mo (Plus) | At 5+ clients for team workspace and shared dashboards |
| Grammarly | Free (basic) | $12/mo (Premium) | At 3+ clients — catches tone and clarity issues free tier misses |
| Loom | 25 videos/mo | $12.50/mo (Business) | At 3+ clients — need unlimited videos for onboarding walkthroughs |
| Google Workspace | Free Gmail | $7.20/mo | Immediately — need Drive, Docs, Sheets under one account |
| Domain for agency site | — | $12/yr | Immediately |
| Hosting for agency site | — | Free (Netlify/Vercel) | Immediately |

**Total monthly cost at launch:** ~$70/mo (ChatGPT Plus + Canva Pro + domain)
**Total monthly cost at 5 clients:** ~$250-400/mo
**Total monthly cost at 10 clients:** ~$500-700/mo (before editor hire)

## Production Checklist

Before delivering any content repurposing service to a client, verify every item:

- [ ] Voice calibration is complete and approved by the client in writing
- [ ] All Make.com scenarios are configured for the client's specific accounts and folder paths
- [ ] Ingest pipeline tested: YouTube RSS or file upload → transcript generated → analysis document created → Slack notification sent
- [ ] All 5 transformation scenarios tested with client-specific voice calibration and saving to correct output folders
- [ ] Fliki AI producing acceptable quality video clips (test at least 3 clips from a real script)
- [ ] Canva brand kit created with client's logo, colors, and fonts (minimum 5 quote card templates)
- [ ] Buffer connected to all client social accounts with optimal posting schedules configured per platform
- [ ] Beehiiv connected with newsletter template customized for the client's branding
- [ ] Production QC sheet set up with approval workflow — no content moves to distribution without human review
- [ ] Full end-to-end pipeline test completed successfully: upload source content → 30+ assets generated and distributed

## What to Do Next

Once your pipeline is running and you have 2-3 clients, expand with these specific moves:

- **Add podcast-to-content as a dedicated service** — Many clients produce podcasts but never repurpose them. Add an RSS trigger in Make.com that watches podcast feeds (Apple Podcasts, Spotify) for new episodes, automatically transcribes them, and feeds them into your existing pipeline. Charge $1,000-1,500/mo additional per client.

- **Build a client content dashboard in Notion** — Show clients their content pipeline status, upcoming scheduled posts, and performance metrics in a shared Notion workspace. This makes the retainer feel tangible and reduces churn. Set up the dashboard during onboarding (Step 6) and update it weekly.

- **Integrate Apollo.io for lead generation** — Use Apollo.io to find creators and businesses producing long-form content but with weak social media presence. Build a prospect list of 500+ targets. Automate the Proof of Value outreach: find their best content, run it through your pipeline, and send them the repurposed assets as a sample. Conversion rate on this method: 30-40%.

- **Offer content strategy consulting as an upsell** — Beyond repurposing, advise clients on what content to create next. Analyze their top-performing pieces. Recommend topics based on keyword research and audience gaps. Charge $500-1,000/mo additional for strategy. This also improves your pipeline inputs — better source content produces better repurposed content.

- **Explore Beehiiv ad network revenue** — If you manage newsletters for clients with 10,000+ subscribers, Beehiiv's ad network generates $2-5 CPM. At 50,000 subscribers, that is $100-250 per send. Split this with the client or keep it as your margin. Either way, it makes the newsletter component more profitable.

Ready to understand the full business opportunity? Read our [opportunity deep-dive](/opportunities/ai-content-repurposing-agency-2026/).
