---
title: "Build a Content Repurposing Agency with AI: The Complete Step-by-Step Guide"
date: 2026-04-24
category: "Implementation"
difficulty: "BEGINNER"
readTime: "28 MIN"
excerpt: "The complete execution guide for building an AI-powered content repurposing agency — from setting up your transformation pipeline to landing clients to scaling with batch processing."
image: "/images/articles/intelligence/build-content-repurposing-agency.png"
heroImage: "/images/heroes/intelligence/build-content-repurposing-agency.png"
relatedOpportunity: "/opportunities/content-repurposing-agency-deep-dive/"
relatedPlaybook: "/playbooks/chatgpt-prompt-engineering-guide/"
---

You are going to build a content repurposing agency that turns one piece of content into twelve platform-native assets using AI. No design degree. No video editing certification. No team of five. You, a browser, and the right prompts. This guide covers every click, every setting, every prompt, every optimization. Follow it in order. Do not skip steps.

## Prerequisites

Before you do anything else, set up these accounts. Every tool listed here has a free tier or free trial. You will not spend more than $0 to start.

**Required accounts (create these now):**

- ChatGPT account (free tier works) — go to chat.openai.com and sign up
- Canva account (free tier works) — go to canva.com and sign up
- Google account for Google Docs and Google Drive — go to accounts.google.com
- Buffer account (free tier works) — go to buffer.com and sign up
- Notion account (free tier works) — go to notion.so and sign up

**Optional but recommended (start free trials when you have a client):**

- Opus Clip — go to opus.pro and start a 7-day free trial
- Repurpose.io — go to repurpose.io and start a 14-day free trial
- Make.com — go to make.com and start a 14-day free trial
- Descript — go to descript.com and start a 7-day free trial

**Time required:** 6-8 hours to build your first complete workflow and produce portfolio-ready samples.

**Total upfront cost:** $0. You upgrade to paid tools only after you have paying clients. The business funds itself.

## Step 1: Build Your Content Transformation Pipeline

This is the engine of your entire agency. You will create a system that takes raw content in, processes it through AI with calibrated prompts, and outputs platform-native assets ready for review. Build this once. Use it for every client forever.

### 1.1 Set Up Your Client Folder Structure

Open Google Drive. Create a main folder called `Repurposing Agency`. Inside it, create three subfolders:

- `01_Inbox` — where raw content lands
- `02_Working` — where transcripts and AI outputs live during processing
- `03_Deliverables` — where final reviewed content waits for client approval

Inside `02_Working`, create a subfolder called `Prompt Library`. This is where you store your transformation prompts. You will populate it in Step 1.3.

Inside `03_Deliverables`, create a Google Doc template called `Client Delivery Template`. Open it and add this structure:

```
WEEK OF: [Date]
CLIENT: [Name]

PLATFORM DELIVERABLES:

📋 TWITTER THREAD
[Paste thread here]

💼 LINKEDIN POST
[Paste post here]

📱 INSTAGRAM REEL SCRIPT
[Paste script here]

📝 BLOG ARTICLE
[Paste article here or link to doc]

📧 EMAIL NEWSLETTER SEGMENT
[Paste segment here]

🎨 QUOTE GRAPHICS
[Link to Canva designs]

NOTES:
[Strategic notes about each piece — angle, positioning, scheduling suggestion]
```

Save this as a template. You will duplicate it for each client each week.

### 1.2 Master the Ingest Process

You need to get raw content into text form fast. Every second counts when you are processing 8-10 clients per week. Here is the exact method for each content type.

**For YouTube videos:**

1. Open the YouTube video in your browser
2. Click the "...More" button below the video description
3. Click "Show Transcript"
4. The transcript panel opens on the right side of the screen
5. Click the three-dot menu in the transcript panel
6. Click "Toggle timestamps" to remove timestamps
7. Select all text (Ctrl+A or Cmd+A)
8. Copy (Ctrl+C or Cmd+C)
9. Open a new Google Doc in the client's `02_Working` folder
10. Paste the transcript
11. Name the file: `[ClientName]_[VideoTitle]_[Date]_transcript`

If the video has no transcript (rare), open Descript, click "New Project," paste the YouTube URL, and let Descript transcribe it. This takes 2-3 minutes for a 30-minute video.

**For podcast episodes:**

1. Download the MP3 file from the podcast host (most provide direct download links)
2. Open Descript or go to otter.ai
3. Upload the MP3 file
4. Wait for transcription (2-5 minutes depending on length)
5. Export the transcript as a .txt file
6. Save it to the client's `02_Working` folder with the same naming convention

**For written content (blogs, newsletters):**

1. Copy the full text from the source
2. Paste into a Google Doc in `02_Working`
3. Done. This is the fastest input type.

**For Zoom or Loom recordings:**

1. Install the TLDV Chrome extension from the Chrome Web Store
2. TLDV automatically records and transcribes any Zoom or Google Meet call
3. After the call, open TLDV, find the recording, click "Export Transcript"
4. Save to `02_Working`

### 1.3 Build Your Prompt Library

This is the single most important asset in your agency. Your prompts determine the quality of your output. Bad prompt = bad content = lost client. Open your `Prompt Library` folder and create a separate Google Doc for each prompt below.

**Create a new Google Doc called `00_Voice_Calibration_Prompt`:**

Paste this prompt:

```
You are writing in the voice of [CLIENT NAME]. Their style is [direct/conversational/authoritative/witty]. They frequently use phrases like [EXAMPLE 1, EXAMPLE 2, EXAMPLE 3]. They never use corporate jargon like "leverage" or "synergy" or "circle back." Their audience is [DEMOGRAPHIC — e.g., SaaS founders, fitness coaches, real estate agents]. Their go-to storytelling format is [anecdote then lesson / bold claim then proof / question then framework]. They prefer [short punchy sentences / longer flowing paragraphs]. They [do/don't] use emojis. They [do/don't] use personal stories. They [do/don't] swear occasionally.

Before writing anything, confirm you understand this voice profile. Then apply it to every piece of content you generate.
```

This is your master voice prompt. You customize the bracketed fields for each client during onboarding. Every other prompt in your library references this voice calibration.

**Create a Google Doc called `01_Twitter_Thread_Prompt`:**

Paste this prompt:

```
Using the voice profile provided, transform the following transcript into a Twitter/X thread of 7-10 tweets.

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
[PASTE TRANSCRIPT]
```

**Create a Google Doc called `02_LinkedIn_Post_Prompt`:**

Paste this prompt:

```
Using the voice profile provided, transform the following transcript into a LinkedIn post.

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
[PASTE TRANSCRIPT]
```

**Create a Google Doc called `03_Instagram_Reel_Script_Prompt`:**

Paste this prompt:

```
Using the voice profile provided, transform the following transcript into a 30-60 second Instagram Reel script.

Format each section exactly like this:

[VISUAL: Describe what the viewer sees — e.g., "Talking head, zoom in slowly" or "B-roll of workspace with text overlay"]
[TEXT OVERLAY: The 3-5 words that appear on screen — this is the pattern interrupt]
[VOICEOVER: What the person says — conversational, punchy, no filler]

Script structure:
- Seconds 0-2: Pattern interrupt. The text overlay and visual must stop the scroll. State something surprising or counterintuitive.
- Seconds 3-15: Deliver the core insight from the transcript. One idea only. Strip everything else.
- Seconds 15-25: Provide the "so what" — why this matters, what to do with it.
- Seconds 25-30: CTA — "Save this for later" or "Follow for more [topic]" or ask them to comment a specific word.

Rules:
- Maximum 75 words in the voiceover. Every word earns its place.
- No "Hey guys" or "So today I want to talk about." Start mid-thought.
- The first 2 seconds determine everything. Make them count.

Here is the transcript:
[PASTE TRANSCRIPT]
```

**Create a Google Doc called `04_Blog_Article_Prompt`:**

Paste this prompt:

```
Using the voice profile provided, transform the following transcript into an 800-1,200 word blog article.

Instructions:
- Do NOT summarize the entire transcript. Pick the single most valuable angle or insight and go deep on it.
- Structure: Compelling headline (no clickbait), introduction (2-3 sentences that hook the reader), 3-4 sections with H2 headings, conclusion with a CTA.
- Each section should include a specific example, anecdote, or data point from the transcript.
- Write in short paragraphs (2-3 sentences max). Make it scannable.
- Use bold text for key phrases a reader would want to skim.
- Include at least one actionable takeaway the reader can implement today.
- The tone should feel like a trusted mentor sharing hard-won knowledge, not a textbook.

Do not use these phrases: "In today's world," "It's important to note," "At the end of the day," "Let's dive in."

Here is the transcript:
[PASTE TRANSCRIPT]
```

**Create a Google Doc called `05_Email_Newsletter_Prompt`:**

Paste this prompt:

```
Using the voice profile provided, transform the following transcript into a 200-300 word email newsletter segment.

Structure:
- Subject line: 3-6 words. Curiosity-driven. No clickbait. Examples: "The thing nobody tells you about [topic]" or "[Number] mistakes I made with [topic]"
- Opening line: Jump straight into the insight. No "Hope you're having a great week." No "I wanted to share..."
- Body: One idea. One story from the transcript. Written like you're texting a smart friend.
- CTA: One clear action. "Reply and tell me [specific question]" or "Check out the full episode: [link]" or "Hit reply if you've experienced this."
- Sign-off: Their usual sign-off style.

Rules:
- Maximum 300 words total.
- Write at a 6th grade reading level. Short words. Short sentences.
- No corporate newsletter energy. This should feel personal, not broadcast.
- One idea per email. If the transcript has five insights, pick the most surprising one.

Here is the transcript:
[PASTE TRANSCRIPT]
```

**Create a Google Doc called `06_Quote_Graphics_List_Prompt`:**

Paste this prompt:

```
Extract the 5 most quotable lines from the following transcript. These will become quote graphics for social media.

Criteria for a quotable line:
- It must make sense without context (no "this" or "that" referring to something earlier)
- It should express an insight, opinion, or framework — not a fact
- It should be 8-20 words long
- It should sound like something someone would highlight and share

Format each quote exactly like this:
1. "[Exact quote]"
   Context: [2-3 words describing the topic]
   Platform fit: [LinkedIn / Instagram / Twitter]

Here is the transcript:
[PASTE TRANSCRIPT]
```

You now have seven prompt documents. This library is your production line. Every piece of content you produce for every client runs through these prompts with the voice calibration attached.

### ✅ Check-In: Pipeline Ready

Before moving on, verify:
- Your Google Drive folder structure exists with `01_Inbox`, `02_Working`, and `03_Deliverables`
- Your `Client Delivery Template` doc is created
- All seven prompt documents exist in your `Prompt Library` folder
- You can locate and open each prompt within 10 seconds

If any of these are missing, stop and create them now. You cannot operate efficiently without this infrastructure.

## Step 2: Build Your First Portfolio Piece

You need proof that this works before you approach clients. You will now take a real piece of content and run it through your entire pipeline. This becomes your portfolio sample.

### 2.1 Select Your Source Content

Pick a YouTube video from a creator you admire. Choose one that is 15-45 minutes long and covers a specific topic. The more specific, the better your repurposed content will be.

Go to the video. Follow the YouTube transcript extraction process from Step 1.2. Save the transcript to `02_Working` with the file name `Portfolio_Transcript`.

Read through the transcript once. You need to understand the content before you transform it. If you skip this read-through, you cannot do quality control later.

### 2.2 Generate All Platform Assets

Open six browser tabs. In each tab, open ChatGPT. You will run all six transformation prompts in parallel. This is the batch processing method and it cuts your production time in half.

**Tab 1 — Voice Calibration:**

Paste the `00_Voice_Calibration_Prompt` into ChatGPT. Fill in the bracketed fields for the creator you selected. Base the voice profile on your familiarity with their content. If you are not sure about specific phrases, go watch 2-3 of their other videos or read their recent social posts first.

ChatGPT will confirm it understands the voice profile. Keep this tab open. You will reference it if the output in other tabs feels off-brand.

**Tab 2 — Twitter Thread:**

Paste the `01_Twitter_Thread_Prompt` with the full transcript appended at the bottom. Hit Enter. While it generates, move to the next tab.

**Tab 3 — LinkedIn Post:**

Paste the `02_LinkedIn_Post_Prompt` with the full transcript. Hit Enter. Move on.

**Tab 4 — Instagram Reel Script:**

Paste the `03_Instagram_Reel_Script_Prompt` with the full transcript. Hit Enter.

**Tab 5 — Blog Article:**

Paste the `04_Blog_Article_Prompt` with the full transcript. Hit Enter.

**Tab 6 — Email Newsletter:**

Paste the `05_Email_Newsletter_Prompt` with the full transcript. Hit Enter.

**Final — Quote Graphics List:**

You can reuse Tab 1 for this. Paste the `06_Quote_Graphics_List_Prompt` with the full transcript.

All six outputs should generate within 60-90 seconds. By the time you finish pasting the last prompt, the first outputs are already done.

### 2.3 Review and Refine Each Output

This step is where amateurs fail and professionals win. Every single piece of AI-generated content needs human review. No exceptions. You are looking for five things on every deliverable:

**Voice match:** Read the output aloud. Does it sound like the creator? If it sounds like a marketing intern wrote it, rewrite the stiff parts. Replace generic phrases with the creator's characteristic expressions. If the creator says "look" a lot, use "look." If they never say "utilize," change "utilize" to "use."

**Fact check:** AI fabricates things with confidence. Verify every statistic, every name, every claim. If the transcript says "70% of founders" and the AI output says "most founders," change it back to "70% of founders" — specificity is better. If the AI added a statistic that was not in the transcript, remove it.

**Platform formatting:** LinkedIn posts need double line breaks between paragraphs. Twitter threads need proper numbering. Reel scripts need the visual/text/voiceover format. Blog articles need H2 headings. Email newsletters need a subject line at the top. Check every piece against its platform's formatting requirements.

**Repetition check:** Since all six pieces come from the same transcript, you will naturally see the same insights repeated. This is fine across platforms — your LinkedIn audience is not your Twitter audience. But within a single platform, make sure each piece offers a unique angle. If the LinkedIn post and the email segment both use the same anecdote, change one.

**CTA check:** Every piece must end with a call to action. Twitter thread ends with a CTA tweet. LinkedIn post ends with a question. Reel ends with "Follow for more" or "Save this." Blog article ends with a next step. Email ends with a reply prompt or link. AI tends to trail off with vague conclusions. Replace them with specific CTAs.

Copy each reviewed and refined output into your `Client Delivery Template` doc. This is your portfolio piece.

### 2.4 Create the Quote Graphics in Canva

Open Canva. Click "Create a design." Select "Instagram Post" (1080 x 1080px).

On the left sidebar, click "Templates." Search for "quote post." Pick a clean, minimal template — no busy backgrounds, no excessive decoration. The words should dominate.

Click the text elements. Replace the placeholder text with your first quote from the AI output. Adjust font size so the quote fills the canvas without crowding. Use a bold or semi-bold font for the quote. Use a light or regular font for the attribution.

Click "Share" in the top right, then "Download." Select PNG format. Download.

Repeat for the top 2-3 quotes. You now have your visual assets.

### ✅ Check-In: Portfolio Complete

Before moving on, verify:
- You have a complete `Client Delivery Template` doc with all six text deliverables filled in
- Each piece has been reviewed against the five QC criteria (voice, facts, formatting, repetition, CTA)
- You have 2-3 quote graphics downloaded as PNGs
- The total package looks like something a creator would pay for

If anything feels thin or generic, go back and refine. This portfolio piece is your sales tool. It must impress.

## Step 3: Set Up Opus Clip and Repurpose.io for Video Content

Video repurposing is where the money is. Clients who produce video content (YouTube, podcasts, webinars) need short-form clips for TikTok, Instagram Reels, and YouTube Shorts. Doing this manually takes hours per video. AI tools do it in minutes.

### 3.1 Configure Opus Clip

Go to opus.pro and sign up. Start the 7-day free trial — you get enough credits to process several videos.

Once logged in, you see the Opus Clip dashboard. Here is how to configure it for client work:

1. Click "New Clip" in the top navigation
2. Paste a YouTube URL from your portfolio creator's video
3. Before clicking "Generate," configure these settings:
   - **Clip length:** Select "30-60 seconds" — this is the sweet spot for TikTok and Reels
   - **Number of clips:** Select "10" — Opus will find the top 10 most engaging segments
   - **Aspect ratio:** Select "9:16" (vertical) — this is the format for TikTok, Reels, and Shorts
   - **Language:** Select the language of the video
4. Click "Generate"

Opus Clip analyzes the video and scores each segment for viral potential. This takes 5-10 minutes for a 30-minute video. You will see a progress bar.

When processing completes, you see a list of clips ranked by "virality score." Each clip has a thumbnail, a score (out of 100), and a preview button. Click "Preview" on the top 3-5 clips. Watch each one.

**Quality criteria for selecting clips:**
- The clip must make sense without context (no references to "what I said earlier")
- The speaker must look engaged and animated (not mid-sentence or looking away)
- The insight must be self-contained and valuable
- The score matters but is not gospel — a clip scored 85 that feels boring is worse than a clip scored 70 that has a great hook

For each clip you want to keep, click "Edit." This opens Opus Clip's editor where you can:

- Trim the start and end points more precisely
- Add captions (click "Captions" in the left sidebar, select a style — the bold white text with colored highlight words performs best)
- Adjust the framing if the speaker is off-center

When finished, click "Export." Download as MP4. Save to `03_Deliverables` with the naming convention `[ClientName]_Clip[number]_[Date].mp4`.

### 3.2 Configure Repurpose.io

Repurpose.io automates cross-platform video distribution. When your client posts a TikTok, Repurpose automatically publishes it as an Instagram Reel and a YouTube Short. No manual uploading.

Go to repurpose.io and sign up. Start the 14-day free trial.

Once logged in:

1. Click "Add Connection" in the left sidebar
2. Connect the platforms your client uses. For a typical creator, connect:
   - TikTok (as a source)
   - Instagram (as a destination)
   - YouTube (as a destination)
   - You need login credentials for each platform. For your own testing, use your personal accounts.
3. After connecting, click "Create Workflow"
4. Select "TikTok" as the source
5. Select "Instagram Reels" and "YouTube Shorts" as destinations
6. Click "Next"
7. Configure publishing settings:
   - **Instagram Reels:** Enable "Remove watermark" (critical — Instagram's algorithm demotes content with TikTok watermarks). Set "Publish immediately" or schedule for optimal posting times.
   - **YouTube Shorts:** Enable "Add as Short" (videos under 60 seconds automatically get the Shorts format). Set title format to "[Original TikTok Title]" — you can customize later.
8. Click "Activate"

Now, whenever your client posts a TikTok, Repurpose.io automatically publishes it to Instagram Reels and YouTube Shorts within minutes. This saves you 10-15 minutes per video in manual uploading.

### ✅ Check-In: Video Pipeline Ready

Verify:
- Opus Clip can generate 3-5 quality clips from a YouTube video
- You can edit clips, add captions, and export them as MP4s
- Repurpose.io is connected to at least two platforms with an active workflow
- You understand the flow: long video → Opus Clip for clips → client approval → scheduling → Repurpose.io for cross-platform distribution

If Opus Clip's output feels low quality, try a different source video. Some videos produce better clips than others — highly conversational, insight-dense content works best. Lecture-style or slow-paced content produces weaker clips.

## Step 4: Set Up Make.com Automation

This is the step that takes you from "freelancer doing everything manually" to "agency owner running a system." Make.com connects your tools together so that content flows from ingest to transformation to delivery with minimal manual intervention.

### 4.1 Create Your Make.com Account

Go to make.com and sign up. Start the 14-day free trial of the Pro plan — you need more operations than the free tier allows.

Once logged in, you see the Make dashboard. Click "Create a new scenario" in the top right. You are now on the scenario builder canvas.

### 4.2 Build the Auto-Ingest Scenario

This scenario watches a Google Drive folder for new transcripts and notifies you when content is ready to process.

1. Click the large "+" button in the center of the canvas
2. Search for "Google Drive" and select it
3. Select the "Watch Files in a Folder" module
4. Connect your Google Drive account (click "Add," follow the OAuth flow)
5. Configure the module:
   - **Folder:** Select your `01_Inbox` folder
   - **Watch:** Select "New files"
   - **File types:** Select "Documents" (this catches .txt and .docx files)
6. Set the schedule: Click the clock icon at the bottom of the module. Set it to run "Every 15 minutes" during business hours
7. Click "OK" to save the module

Now add the notification module:

1. Click the "+" that appears on the right side of the Google Drive module
2. Search for "Slack" (or "Gmail" if you prefer email notifications)
3. Select "Send a Message" (Slack) or "Send an Email" (Gmail)
4. Connect your Slack or Gmail account
5. Configure the message:
   - **To:** Your personal channel or email
   - **Subject/Message:** "New content ready for processing: [File name from Google Drive module]"
6. Click "OK"

Click "Save" in the bottom left. Name this scenario "Auto-Ingest." Click the "Run once" button to test it. Drop a test file into your `01_Inbox` folder. You should receive a notification within 15 minutes.

### 4.3 Build the Transcript-to-ChatGPT Scenario

This is the advanced automation. It takes a new transcript, sends it to ChatGPT with your Twitter Thread prompt, and saves the output to a Google Doc. Build this after you have 2-3 clients and are comfortable with the manual process.

1. Create a new scenario called "Auto-Twitter-Thread"
2. Add a Google Drive "Watch Files" module (same as 4.2, pointing to `01_Inbox`)
3. Add a Google Drive "Download a File" module connected to the watch module
4. Add an OpenAI "Create a Chat Completion" module:
   - Connect your OpenAI API key (from platform.openai.com/api-keys)
   - **Model:** Select "gpt-4o"
   - **Messages:** Add a system message with your voice calibration prompt text. Add a user message with your Twitter Thread prompt text plus the transcript content (mapped from the download module output)
   - **Temperature:** 0.7 (good balance of creativity and consistency)
   - **Max tokens:** 1000 (enough for a 7-10 tweet thread)
5. Add a Google Docs "Create a Document" module:
   - **Title:** "[ClientName]_Twitter_Thread_[Date]"
   - **Content:** Map the ChatGPT output (choices[1].message.content) into the document body
   - **Folder:** Select the client's `03_Deliverables` folder
6. Click "OK" and save

Repeat this pattern for each platform prompt. Create separate scenarios for LinkedIn, Instagram Reel, Blog, and Email. Each follows the same structure: Google Drive trigger → Download → ChatGPT with specific prompt → Google Docs output.

### 4.4 Build the Delivery Notification Scenario

1. Create a new scenario called "Delivery-Ready"
2. Add a Google Drive "Watch Files" module pointing to `03_Deliverables`
3. Add an Email module (Gmail) configured to send the client an email:
   - **To:** Client's email (you set this per client)
   - **Subject:** "Your repurposed content is ready — Week of [Date]"
   - **Body:** "Hi [Client Name], your content for this week is ready for review. Access it here: [Link to Google Drive folder]. Please review and approve by [Day]. Reply with any changes."
4. Save and activate

### ✅ Check-In: Automation Live

Verify:
- The Auto-Ingest scenario runs and notifies you of new files
- The Auto-Twitter-Thread scenario (if built) processes a transcript end-to-end
- The Delivery-Ready scenario sends a test email
- All three scenarios are activated and running on schedule

You do not need the advanced ChatGPT scenarios running immediately. Start with the Auto-Ingest and Delivery scenarios. Add the transformation automations once your manual process is dialed in and you have paying clients.

## Step 5: Land Your First Client

You have a portfolio, a workflow, and automation infrastructure. Now you need paying clients. This step covers the exact outreach method, the pitch, and the onboarding process.

### 5.1 Identify Target Clients

Open LinkedIn. Search for terms related to your niche. If you want to serve SaaS founders, search "SaaS founder." If you want to serve fitness coaches, search "online fitness coach." If you want to serve real estate agents, search "real estate coach."

Look for creators who meet all three criteria:

1. **They produce long-form content regularly** (YouTube videos, podcasts, or long newsletters) — this is your raw material
2. **They post inconsistently on short-form platforms** — this is your value proposition
3. **They have 10,000-100,000 followers** — small enough to be approachable, large enough to afford your services

Build a list of 20 targets. Use a simple Google Sheet with columns: Name, Platform, Follower Count, Content Type (YouTube/Podcast/Newsletter), Last LinkedIn Post Date, Email/DM Contact.

### 5.2 Execute the Proof of Value Method

This is the highest-converting client acquisition method in the content repurposing space. Conversion rate: 30-40%. Here is exactly how to do it.

**For each target client:**

1. Find their best performing piece of content from the last 30 days. Look for the YouTube video or podcast episode with the most views, or the newsletter with the most engagement.
2. Extract the transcript using the method from Step 1.2.
3. Run the transcript through your full pipeline: all six prompts, quality control, quote graphics. This takes 30-45 minutes per client now that your workflow is dialed.
4. Load everything into a `Client Delivery Template` doc.
5. Add strategic notes for each piece: "Twitter thread positioned around the contrarian take because your audience engages with hot takes." "LinkedIn post uses the vulnerability angle — your top-performing posts all share personal stories." "Reel script uses the [specific insight] because it's the most clip-worthy moment."
6. Send the client a DM or email with this exact message:

```
Hey [Name],

I'm a huge fan of your content — especially your recent [video/episode] on [topic].

I took that piece and repurposed it into 6 platform-native assets: a Twitter thread, LinkedIn post, Instagram Reel script, blog article, email segment, and quote graphics. Everything is attached and ready to post.

No strings attached. I just wanted to show you what's possible.

If you like the quality, I do this every week for creators like you. One piece of content, turned into a full week of posts across every platform, without you lifting a finger.

Let me know what you think.

[Your Name]
```

**Key detail:** Attach the content directly. Do not send a link to a Notion page or a Google Doc that requires login. Make it frictionless. The creator should be able to open the email, see the content, and decide in 60 seconds whether it is good.

### 5.3 Handle the Response

**If they say yes (30-40% of the time):** Move to Step 6 for onboarding.

**If they say "How much?":** Give them the Starter tier price: $1,500/month for one primary content piece per week and six derivative assets across three platforms. Do not negotiate down. If they cannot afford $1,500/month, they are not ready for this service. Thank them and move on.

**If they say "Can you do a trial?":** You already did a trial — that free work you sent them. One free sample is marketing. Two free samples is charity. Politely say: "I'd love to, but the sample I sent is representative of the weekly quality. I offer a month-to-month agreement so there's no long-term risk."

**If they ghost:** Follow up once after 5 days. If they still ghost, move on. Do not chase. You have 19 more targets.

### 5.4 Scale Your Outreach

Do 10 Proof of Value outreach attempts in your first week. At a 30% conversion rate, that is 3 clients at $1,500/month = $4,500 in monthly revenue.

As you land clients, reduce outreach volume but never stop completely. Even with a full roster, spend 2-3 hours per week on outreach. Clients churn. New clients fill the gaps. The pipeline never stops.

## Step 6: Onboard a New Client

Onboarding is where you set the tone for the entire relationship. A sloppy onboarding leads to endless revisions and dissatisfied clients. A tight onboarding leads to smooth production and long retainers. Do it right.

### 6.1 Send the Onboarding Questionnaire

When a client signs, send them this questionnaire immediately. Create it as a Google Form for easy completion.

**The 15-Question Onboarding Form:**

1. What is your full name and brand/business name?
2. What are your primary social media accounts? (List all handles)
3. What type of content do you produce most often? (YouTube videos / Podcasts / Newsletters / Blog posts / Other)
4. How often do you publish new primary content? (Daily / 2-3x per week / Weekly / Biweekly)
5. What are 3 words that describe your brand voice? (e.g., direct, witty, authoritative)
6. Which creators do you admire stylistically? (Name 2-3 whose writing/speaking style resonates with you)
7. What's a post you wrote that performed really well, and why do you think it worked?
8. What's a post that flopped, and why?
9. What words or phrases do you use frequently? (List 5-10)
10. What words or phrases would you NEVER use? (List 5-10)
11. Do you use emojis? If yes, which ones and how often?
12. Do you share personal stories or keep things professional?
13. Who is your target audience? (Demographics, job titles, interests)
14. What is the #1 goal for your content? (Build authority / Drive sales / Grow audience / Generate leads)
15. How do you prefer to receive deliverables? (Google Doc / Notion / Email / Other)

### 6.2 Build the Voice Profile

While the client fills out the questionnaire, do your own research:

1. Find their last 10-15 LinkedIn posts. Copy all of them into a single document.
2. Find their last 10-15 tweets or Twitter threads. Copy them.
3. If they have a newsletter, read the last 5 issues.
4. If they have a YouTube channel, watch 2-3 recent videos and note speaking patterns.

Feed all of this collected content into ChatGPT with this prompt:

```
Analyze these [number] posts and create a detailed voice profile for this writer. Include:
- Tone (formal/casual/punchy/academic/etc.)
- Vocabulary patterns (words they use often, words they avoid)
- Sentence structure (short and punchy / long and flowing / mixed)
- Go-to frameworks (listicle / story-lesson / question-answer / contrarian-proof)
- Humor style (dry / self-deprecating / sarcastic / dad jokes / none)
- Words they overuse
- Words they would never use
- Typical post structure (hook-body-CTA / story-moral-question / claim-proof-action)
- Emoji usage patterns
- Hashtag usage patterns
```

Merge the AI-generated voice profile with the client's questionnaire answers. This combined document becomes your definitive voice reference for that client. Save it in `02_Working` as `[ClientName]_Voice_Profile`.

Update your `00_Voice_Calibration_Prompt` with this client's specific information. Save it as a new version: `00_Voice_Calibration_Prompt_[ClientName]`.

### 6.3 Run the Calibration Test

Before producing real deliverables, run a test. Take the client's most recent piece of content, run it through your full pipeline using their calibrated voice prompt, and send them the output with this message:

```
Hey [Name],

I've calibrated your voice profile and ran a test transformation on your recent [content piece]. Here are the outputs.

Please review and tell me:
1. Does this sound like you? (If not, what feels off?)
2. Is the tone right, too formal, or too casual?
3. Are there specific words or phrases that feel out of character?

This calibration step ensures every piece I deliver going forward matches your voice perfectly. Takes 5 minutes and saves us weeks of revisions.
```

The client will give you feedback. Apply it to the voice profile. This is the most important 5-minute conversation in the entire client relationship. Get the voice right here, and the next 12 months of production will be smooth.

### 6.4 Set Up the Client Infrastructure

For each new client, create:

1. **Google Drive folder:** `Repurposing Agency > Clients > [ClientName]` with subfolders `Inbox`, `Working`, `Deliverables`
2. **Canva brand kit:** Click "Brand" in Canva's left sidebar, then "Create a brand kit." Upload the client's logo, set their brand colors (hex codes), and select their fonts. Every future graphic uses this kit automatically.
3. **Buffer queue:** Add the client's social accounts to Buffer. Set their preferred posting schedule based on the questionnaire.
4. **Notion client portal:** Create a Notion page with the client's content calendar, delivery log, and feedback section. Share it with the client.
5. **Repurpose.io workflow:** If the client produces video content, set up a Repurpose.io workflow connecting their TikTok to Reels and Shorts.

### ✅ Check-In: Client Onboarded

Verify:
- Client questionnaire is completed and saved
- Voice profile is calibrated and tested with client feedback incorporated
- All infrastructure is created (Drive, Canva, Buffer, Notion, Repurpose.io)
- The first real week of production is scheduled

## Step 7: Weekly Production Workflow

This is your operating rhythm. Every week, for every client, you follow this exact sequence. It becomes second nature after 3-4 weeks.

### 7.1 Monday: Ingest

Block 30 minutes. For each client:

1. Check `01_Inbox` for new content. If the client sent a YouTube link, extract the transcript. If they uploaded an MP3, run it through Descript. If they sent written content, copy it to `02_Working`.
2. Name the transcript file: `[ClientName]_[ContentTitle]_[Date]_transcript`
3. If you have the Make.com Auto-Ingest scenario running, you already received a notification. Just verify the transcript is clean and readable.

### 7.2 Tuesday: Transform

Block 2-3 hours. This is your production block.

For each client:

1. Open six ChatGPT tabs with the client's calibrated voice prompt pre-loaded
2. Paste the transcript into each tab with the appropriate platform prompt
3. Hit Enter on all six tabs simultaneously
4. While AI generates, review the previous client's outputs from QC

### 7.3 Wednesday: Quality Control

Block 2-3 hours.

For each client's AI output:

1. Read every piece against the five QC criteria: voice match, fact check, platform formatting, repetition check, CTA check
2. Rewrite anything that sounds robotic or off-brand
3. Verify specific claims against the original transcript
4. Check that each platform piece uses a different angle from the same source material
5. Load all reviewed content into the `Client Delivery Template`
6. Add strategic notes explaining the angle for each piece
7. Create quote graphics in Canva using the client's brand kit

### 7.4 Thursday: Deliver and Schedule

Block 1 hour.

For each client:

1. Send the delivery doc via email or update the Notion portal
2. Include a brief summary: "This week's content is ready. Twitter thread focuses on [angle]. LinkedIn post uses the [story/framework] approach. Reel script highlights [specific insight]."
3. Schedule all approved content in Buffer based on optimal posting times:
   - LinkedIn: Tuesday and Thursday at 8:00 AM in the client's timezone
   - Twitter: Monday through Friday at 9:00 AM
   - Instagram: Wednesday and Friday at 11:00 AM
   - Email: Tuesday at 6:00 AM

### 7.5 Friday: Review and Prospect

Block 2 hours.

1. Review the week's content performance in Buffer analytics (if available)
2. Note any posts that significantly over- or under-performed — this informs next week's strategy
3. Spend 60-90 minutes on client outreach: Proof of Value attempts, follow-ups, networking

### ✅ Check-In: Production Rhythm Established

After your first full production week, verify:
- Monday ingest took under 30 minutes per client
- Tuesday transformation took under 3 hours total
- Wednesday QC took under 3 hours total
- Thursday delivery took under 1 hour total
- Total weekly time per client is under 90 minutes

If any step takes longer than expected, identify the bottleneck. Common bottlenecks: slow transcript extraction (solution: use Descript), excessive QC rewrites (solution: improve voice calibration), slow graphic creation (solution: pre-build more Canva templates).

## Step 8: Pricing and Packaging

You need to offer clear, simple pricing that makes the buying decision easy. Three tiers. No custom quotes for new clients. No negotiations.

### 8.1 The Three-Tier Model

**Starter — $1,500/month**

- 1 primary content piece per week (4 per month)
- 6 derivative assets per piece: Twitter thread, LinkedIn post, Instagram Reel script, blog article excerpt, email segment, 2 quote graphics
- Content delivered in Google Doc with strategic notes
- Up to 2 revision rounds per week
- Month-to-month agreement

**Growth — $2,500/month**

- 2 primary content pieces per week (8 per month)
- 6 derivative assets per piece (48 total assets per month)
- Scheduling in Buffer included (you post on their behalf)
- Hashtag research and optimization
- Monthly performance review call (30 minutes)
- Quarterly content strategy document
- 3-month minimum commitment

**Enterprise — $5,000/month**

- Daily primary content processing (4-5 per week, 16-20 per month)
- Full derivative suite per piece (96-120 assets per month)
- Opus Clip integration (3-5 short-form video clips per video)
- Repurpose.io cross-platform distribution
- Weekly performance dashboard
- Bi-weekly strategy calls (30 minutes each)
- Priority turnaround (24-hour delivery)
- 3-month minimum commitment

### 8.2 How to Present Pricing

Never send a PDF pricing sheet. Never list prices on your website. Price is always discussed in a conversation after you have demonstrated value. Here is the sequence:

1. Send the Proof of Value work (free sample)
2. They respond positively
3. You say: "Great to hear you like it. I offer three tiers — Starter at $1,500/month, Growth at $2,500/month, and Enterprise at $5,000/month. Most creators start with Growth because it includes scheduling and optimization, which saves them another 3-4 hours per week. Which feels right for where you are?"

The phrase "Which feels right for where you are?" is intentional. It frames the decision as about their readiness, not about the price. Most people do not want to admit they are "not ready" for Growth, so they select the middle tier. This is not manipulation — Growth is genuinely the best value. You are just framing the conversation to help them see it.

### 8.3 Quarterly Discount Strategy

Offer 10% off for a 3-month upfront payment. This means:

- Starter quarterly: $4,050 (saves client $450)
- Growth quarterly: $6,750 (saves client $750)
- Enterprise quarterly: $13,500 (saves client $1,500)

Why do this? The first month with any client is calibration-heavy. You spend more time on voice tuning and revisions. By month two, you are efficient. By month three, you are profitable. The quarterly commitment ensures you reach the profitable months. Without it, clients might leave after month one when the ROI is not yet obvious.

### 8.4 Contract Essentials

Use a simple service agreement. Key clauses:

- **Scope:** Exactly what is delivered each week (number of pieces, platforms, formats)
- **Turnaround:** 48 hours from receipt of source content to delivery
- **Revisions:** 2 rounds per week included. Additional revisions at $100/hour.
- **Payment:** Due on the 1st of each month. No work starts until payment is received.
- **Termination:** 30-day notice for month-to-month. No early termination for quarterly commitments.
- **Content ownership:** All content produced belongs to the client upon payment. Templates and workflows belong to you.

## Step 9: Scale with Batch Processing and Team

Once you have 5-6 clients, you will hit a time ceiling. Each client takes 60-90 minutes per week. At 6 clients, that is 6-9 hours of production time. Add prospecting, admin, and communication, and you are at 20-25 hours per week. This is manageable. But at 8+ clients, you need help.

### 9.1 The Batch Processing Method

Before hiring anyone, maximize your own output with batch processing. The principle: group identical tasks across all clients and do them all at once.

**Batch Ingest (Monday, 30 minutes):** Process all client transcripts in one block. Do not switch between ingest and transformation. Just ingest.

**Batch Transform (Tuesday, 2-3 hours):** Open 30+ ChatGPT tabs if needed. Paste all prompts for all clients. Hit Enter on all of them. While the first batch generates, start reviewing the second batch's output. By the time you finish reviewing, the third batch is done.

**Batch QC (Wednesday, 2-3 hours):** Review all LinkedIn posts for all clients first (you develop a rhythm for LinkedIn voice calibration). Then all Twitter threads. Then all Reel scripts. Same platform, different clients. Your brain stays in "LinkedIn mode" rather than switching contexts.

**Batch Deliver (Thursday, 45 minutes):** Send all delivery emails at once. Schedule all Buffer posts in one session.

Batch processing reduces context-switching overhead by 30-40%. You are not a switch — you are a production line.

### 9.2 Hire a Quality Control Assistant

The first hire is not a writer or a strategist. It is a QC assistant. This person reviews AI output against the voice profile, checks facts, and fixes formatting. You still do the strategic work (prompt engineering, client communication, content planning). The QC assistant handles the tedious review work.

Where to find one: Upwork. Search for "content editor" or "proofreader." Budget: $15-25/hour. You need someone who reads carefully, follows instructions, and communicates clearly. Test candidates with a paid trial: give them 3 AI-generated pieces and your QC checklist. If they catch the same issues you would catch, they are a good fit.

How to train them: Share your Notion SOP that documents every step of this guide. Give them access to each client's voice profile. Review their first two weeks of work closely. After that, trust the process.

### 9.3 Hire a Production Assistant

At 10+ clients, hire someone to run the transformation pipeline. This person takes transcripts, runs them through your prompt library, and produces first drafts. You review their work and handle client delivery.

Budget: $15-25/hour, or $500-800/month part-time. This person does not need to be a writer. They need to follow your process precisely. The prompts do the creative work. The production assistant operates the machine.

### 9.4 Systematize Everything

Create a Notion workspace called `Agency SOP` with these pages:

1. **Onboarding Checklist** — Step 6 of this guide, formatted as a checklist
2. **Weekly Production Workflow** — Step 7 of this guide, with time blocks
3. **QC Checklist** — The five criteria, with examples of common AI errors
4. **Prompt Library** — All seven prompts, with instructions for customization
5. **Client Voice Profiles** — A sub-page for each client with their calibrated profile
6. **Pricing and Contracts** — Templates for proposals and service agreements
7. **Troubleshooting** — Common issues (AI hallucination, voice drift, client scope creep) and solutions

This SOP is your business in document form. It allows anyone you hire to produce consistent output without you hovering over their shoulder.

## Step 10: Optimize and Expand

Once the core operation is running smoothly, optimize for margin and expand for revenue.

### 10.1 Reduce Production Time with Advanced Prompts

After 4-6 weeks with a client, you have enough data to identify patterns. Which platforms get the most engagement? Which content angles work best? Feed this data back into your prompts.

Add a "Performance Notes" section to each client's voice profile:

```
PERFORMANCE NOTES (updated monthly):
- LinkedIn posts with personal stories get 3x engagement vs. framework posts
- Twitter threads that start with a contrarian take get 2x impressions
- Email segments under 200 words have the highest click rates
- Reel scripts under 45 seconds outperform longer ones
```

Then update your prompts to bias toward what works. In the LinkedIn prompt, add: "Default to the personal story angle unless the transcript has no relevant anecdote." In the Twitter prompt, add: "Lead with the most contrarian or surprising insight."

This feedback loop makes your output progressively better. Each month, the AI generates content that is more aligned with what the client's audience wants. The client sees improving results. You see fewer revision requests and longer retainers.

### 10.2 Add Video Clip Production as an Upsell

If a client does not already have Opus Clip in their package, offer it as a $500/month add-on. This includes 3-5 AI-generated short-form clips per video, with captions, formatted for TikTok/Reels/Shorts, and distributed via Repurpose.io.

The marginal cost to you: $19/month for Opus Clip plus 15-20 minutes of review time per video. At $500/month, the margin on this add-on is 90%+.

### 10.3 Expand into New Niches

Once you dominate one creator niche (e.g., SaaS founders), expand into adjacent niches (e.g., indie hackers, tech entrepreneurs, startup advisors). Your workflow is identical. Only the voice profiles and prompt customizations change.

Each new niche requires:
1. 3-5 Proof of Value samples (2-3 hours each)
2. Updated prompt calibrations for the niche's common voice patterns
3. Outreach to 20 targets in the new niche

You are not starting from scratch each time. You are deploying the same machine with different inputs.

### 10.4 Build a Referral Engine

Every client you have is connected to other creators. Creators are in group chats, masterminds, and communities together. Activate this network.

Offer every client a free month of service for every referral that signs a 3-month contract. The free month costs you roughly $77 in tool costs and a few hours of your time (or your assistant's time). The referral is worth $2,500-$5,000/month in new revenue.

Send this message to existing clients after month two (once they are happy with the service):

```
Hey [Name], quick ask — if you know any other creators who could use this service, I'll give you a free month for every referral who signs up. Most of my best clients come from word of mouth, so I want to reward the people who spread the word. Just CC me on an intro email or send them my way.
```

Simple. No affiliate links. No tracking software. Just trust and a handshake.

## Cost Breakdown

| Item | Free Tier | Paid Tier | When to Upgrade |
|------|-----------|-----------|-----------------|
| ChatGPT | Free (limited messages) | $20/mo (Plus) | At 2-3 clients |
| Claude | Free (limited messages) | $20/mo (Pro) | At 3-4 clients for better long-form output |
| Opus Clip | 7-day free trial | $19/mo | At first video client |
| Descript | 7-day free trial | $24/mo | At 2+ clients with audio/podcast content |
| Canva | Free | $13/mo (Pro) | At 2+ clients for brand kits and resize |
| Buffer | Free (3 accounts, 10 posts) | $6/channel/mo | At 2+ clients for scheduling |
| Make.com | 14-day free trial | $9/mo (Basic) | At 3+ clients for automation |
| Repurpose.io | 14-day free trial | $15/mo | At first video client for cross-posting |
| Notion | Free (personal) | $8/mo (Plus) | At 5+ clients for team features |
| Otter.ai | Free (300 min/mo) | $17/mo (Pro) | Only if you process 5+ hours of audio per week |
| Google Workspace | Free (gmail) | $6/mo (Business) | At 5+ clients for professional email |

**Total monthly cost at 0 clients:** $0
**Total monthly cost at 3 clients:** ~$89/mo (ChatGPT Plus, Canva Pro, Buffer)
**Total monthly cost at 6 clients:** ~$154/mo (full paid stack)
**Total monthly cost at 10+ clients:** ~$200/mo (with automation and team features)

**Revenue at 3 clients (Starter):** $4,500/mo
**Revenue at 6 clients (Growth):** $15,000/mo
**Revenue at 10 clients (mixed tiers):** $25,000+/mo

**Gross margin at every stage: 93-97%.** These are not theoretical numbers. Tool costs are negligible relative to revenue. The only meaningful cost at scale is labor (your assistants), and even that is a fraction of revenue.

## Production Checklist

Before delivering any week's content to any client, verify every item:

**Content Quality:**
- [ ] Every piece sounds like the client wrote it (voice match verified by reading aloud)
- [ ] All facts, statistics, and claims verified against the original transcript
- [ ] No AI hallucinations — no fabricated quotes, stats, or anecdotes
- [ ] Each platform piece uses a different angle from the same source material
- [ ] Every piece ends with a specific call to action (no vague trailing off)
- [ ] AI-typical phrases removed ("In today's landscape," "It's worth noting," "Let's dive in")

**Platform Formatting:**
- [ ] LinkedIn post has double line breaks between paragraphs, under 1,300 characters, 3-5 hashtags at the end
- [ ] Twitter thread has 7-10 tweets, numbered or unnumbered, hook first, CTA last, under 280 chars each
- [ ] Instagram Reel script has visual/text/voiceover format, under 75 voiceover words, pattern interrupt in first 2 seconds
- [ ] Blog article has H2 headings, bold key phrases, 800-1,200 words, scannable paragraphs
- [ ] Email segment has subject line, under 300 words, one idea, one CTA
- [ ] Quote graphics use client's brand kit colors and fonts

**Client Infrastructure:**
- [ ] Content saved in the client's delivery template with strategic notes
- [ ] Quote graphics uploaded to the shared folder or Notion portal
- [ ] Video clips (if applicable) exported with captions, no watermarks
- [ ] Scheduling set in Buffer for optimal posting times per platform
- [ ] Repurpose.io workflow active for cross-platform video distribution
- [ ] Client notified of delivery with summary of angles and approaches used

**Monthly:**
- [ ] Performance review pulled from Buffer analytics
- [ ] Top-performing and underperforming content identified
- [ ] Voice profile updated with performance notes
- [ ] Prompts adjusted based on performance data
- [ ] Client sent a brief monthly performance summary

## What to Do Next

Once you have 3-5 clients and your workflow is dialed:

1. **Automate the transformation pipeline** — Build the full Make.com scenarios from Step 4.3 for every platform prompt. This reduces your transformation time from 15 minutes per piece to 2 minutes per piece. At 8 pieces per client per week and 5 clients, that saves you 8+ hours per week.

2. **Hire a QC assistant** — Follow the process in Step 9.2. Start with 10 hours per week. Review their work closely for the first two weeks. After that, trust the system.

3. **Launch a content calendar service** — For an additional $500/month, plan the client's content themes 4 weeks in advance. This makes your weekly production even faster because you know what angles to take before the source content arrives.

4. **Build a case study** — After 3 months with a strong client, document the results. "How we took [Creator] from 4 posts/month to 48 posts/month and grew their LinkedIn engagement by 340%." Use this as a sales asset. Case studies convert 2-3x better than Proof of Value samples because they show sustained results, not a one-off.

5. **Explore vertical SaaS** — If you are processing 15+ clients and have a trained team, package your workflow as a self-serve product. Build a simple web app where creators upload content and get AI-repurposed assets automatically. This transitions you from agency revenue (linear, capped by capacity) to SaaS revenue (scalable, uncapped). This is the long game. Most operators never reach this stage, and that is fine — $20,000-$30,000/month from a lean agency is an excellent outcome. But if you want to build something bigger, this is the path.
