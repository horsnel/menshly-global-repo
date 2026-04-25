---
title: "Build an AI Image Generation Agency: The Complete Step-by-Step Guide"
date: 2026-04-24
category: "Implementation"
difficulty: "BEGINNER"
readTime: "28 MIN"
excerpt: "The complete execution guide for launching an AI image generation agency — from mastering Midjourney and DALL-E to building a client delivery pipeline to scaling with batch production."
image: "/images/articles/intelligence/build-ai-image-generation-agency.png"
heroImage: "/images/heroes/intelligence/build-ai-image-generation-agency.png"
relatedOpportunity: "/opportunities/ai-image-generation-agency/"
relatedPlaybook: "/playbooks/ai-side-hustle-blueprint/"
---

Building an AI image generation agency is not about typing prompts and hoping something pretty comes out. It is about producing consistent, brand-aligned, professionally finished visual assets at a speed and price point that traditional creative agencies cannot match. This guide walks you through every step — from setting up Midjourney and DALL-E 3 to building a batch production system that delivers 50 images to a client in a single afternoon. Follow it in order. Do not skip steps.

## Prerequisites

Before you start, you need the following:

- A laptop with a modern browser (Chrome or Firefox)
- A Discord account — go to discord.com and sign up (required for Midjourney)
- A Midjourney subscription ($10/mo Basic plan) — go to midjourney.com and subscribe
- A ChatGPT Plus subscription ($20/mo) — go to chat.openai.com and upgrade (includes DALL-E 3 access)
- A Leonardo.ai account (free tier works for your first 10 projects) — go to leonardo.ai and sign up
- A Canva Pro account ($13/mo) — go to canva.com and sign up (free tier works initially, but Pro is needed for brand kits and background remover)
- A Topaz Photo AI license ($15/mo or $199 one-time) — go to topazlabs.com and download (for upscaling AI images to print resolution)
- A Google Drive or Dropbox account for client delivery — free tier is fine
- A Notion account for project tracking and style guides — free tier is fine
- 6-8 hours of uninterrupted time for your first complete build

Total upfront cost: $58/mo ($10 Midjourney + $20 ChatGPT Plus + $13 Canva Pro + $15 Topaz). One client paying $300-500 for an image pack covers this for months. If you want to start at zero cost, use Bing Image Creator (free DALL-E 3), Leonardo.ai free tier, and Canva free tier. The workflow is the same. The paid tools just produce better output faster.

## Step 1: Set Up Midjourney and Learn Prompt Engineering

Midjourney is the highest-quality AI image generator available. It runs through Discord. This step gets you running and teaches you the prompt structure you will use for every client project.

### Create Your Midjourney Account

Open your browser and go to midjourney.com. Click **Join the Beta**. You will be redirected to Discord. If you already have a Discord account, log in. If not, create one. After logging in, you should see the Midjourney server in your Discord sidebar.

Do you see the Midjourney server? If you see only your own username and no servers, the invite did not process. Go back to midjourney.com, click **Join the Beta** again, and accept the Discord invite when prompted.

Click on the Midjourney server. You should see a list of channels on the left sidebar. Find any channel named "newbies" followed by a number (e.g., #newbies-42). Click it. This is where you will generate your first images.

### Subscribe to a Paid Plan

Midjourney no longer offers free generations. You need a paid plan. In the #newbies channel, type `/subscribe` and press Enter. A link will appear. Click it. You will be taken to the Midjourney pricing page.

Select the **Basic Plan** at $10/mo. This gives you approximately 200 fast generations per month. Enter your payment details. Confirm.

After subscribing, go back to Discord. Type `/imagine` in the #newbies channel. A prompt box should appear. If you see "You need an active subscription to use this bot," your payment has not processed. Wait 5 minutes and try again. If it still fails, check your billing page at midjourney.com/account.

### Generate Your First Image

Type `/imagine` and then type your prompt:

```
professional product photography of a ceramic coffee mug on a minimalist wooden desk, soft natural lighting from a window, warm tones, shallow depth of field, shot on Canon R5 with 85mm f/1.4 lens --ar 16:9 --s 750 --v 6.1
```

Press Enter. You should see four image variations appear after 30-60 seconds. If you see "Job queued" and nothing happens, the server is busy — wait up to 2 minutes.

Do you see four images? If you see an error about content policy, remove any words that might trigger the filter and try again. If you see "No results," your prompt was empty or malformed — make sure the text appears after `/imagine` in the same message.

### Learn the Midjourney Parameter System

Every prompt you write for clients will use parameters. These are the dials that control the output. Memorize these:

- **--ar [ratio]** — Aspect ratio. Use `--ar 16:9` for landscapes and banners, `--ar 1:1` for Instagram squares, `--ar 9:16` for Stories and Reels, `--ar 4:5` for Pinterest and Facebook posts.
- **--s [number]** — Stylize value (0-1000). Higher = more artistic interpretation. Lower = closer to literal prompt. For product photography, use `--s 250-500`. For artistic illustrations, use `--s 750-1000`.
- **--q [number]** — Quality (0.25, 0.5, 1). Lower = faster but less detail. Always use `--q 1` for client work.
- **--cref [URL]** — Character reference. Upload an image, get its URL, use `--cref` to maintain the same person across images. Critical for brand storytelling.
- **--sref [URL]** — Style reference. Upload a mood board image, use `--sref` to match its aesthetic across all outputs. Critical for brand consistency.
- **--cw [number]** — Character weight (0-100). Use with --cref. 100 = match face + hair + outfit. 0 = match face only.
- **--sw [number]** — Style weight (0-1000). Use with --sref. Higher = closer to reference style.
- **--seed [number]** — Seed number. Using the same seed with the same prompt produces similar images. Use this for batch consistency.
- **--v 6.1** — Model version. Always specify the latest model. Currently 6.1.
- **--no [term]** — Negative prompt. Exclude elements. Example: `--no text, watermark, blurry`.

### Build Your Prompt Template

You will use this template structure for every client image. Copy it into a Notion document called "Prompt Templates":

```
[subject description] in [setting/background], [lighting description], [color palette], [composition/camera angle], shot on [camera] with [lens], [mood/atmosphere] --ar [ratio] --s [stylize] --v 6.1 --no [exclusions]
```

Example for a fitness brand:

```
athletic woman doing yoga in a bright modern studio with large windows, golden hour natural lighting streaming through, warm earth tones with sage green accents, wide angle shot from slightly above, shot on Sony A7IV with 35mm f/1.8 lens, calm and empowering atmosphere --ar 4:5 --s 500 --v 6.1 --no text, watermark, distorted limbs
```

Example for an e-commerce product shot:

```
minimalist leather wallet on a concrete surface with dried eucalyptus leaves, soft directional studio lighting from the left, neutral warm tones, overhead flat lay composition, shot on Canon R5 with 100mm f/2.8 macro lens, clean and premium feel --ar 1:1 --s 350 --v 6.1 --no text, shadows, clutter
```

Generate 5 images using this template structure. Adjust the parameters. Observe how each change affects the output. You need at least 20 practice generations before you are ready for client work.

### Step 1 Check-In

Verify each of these before moving on:

1. You can generate images in Midjourney without errors
2. You understand and can use at least 5 parameters (--ar, --s, --cref, --sref, --no)
3. You have generated at least 20 practice images across 3 different styles (product photography, editorial illustration, social media graphic)
4. You have saved the prompt template to your Notion document
5. You can reliably produce an image in a specific aspect ratio on the first attempt

If any of these fail, go back and practice. Client work requires predictability. If you cannot control the output, you cannot deliver.

## Step 2: Set Up DALL-E 3 for Text-Heavy and Commercial Work

DALL-E 3 is your tool for images that contain text, images that need commercial safety, and images that require conversational refinement. It runs inside ChatGPT. This step gets you set up and teaches you the workflow.

### Access DALL-E 3 Through ChatGPT Plus

Open your browser and go to chat.openai.com. Log in. You should see the ChatGPT interface with a text input at the bottom.

Click the **GPT-4** dropdown at the top. Select **DALL-E 3** from the model options. If you do not see this option, your account does not have ChatGPT Plus active. Go to chat.openai.com/subscribe and upgrade.

Do you see the DALL-E 3 model selected? You should see "DALL-E 3" or an image icon next to the model selector. If you see only GPT-3.5 and GPT-4, DALL-E 3 is not enabled for your account. Try creating a new chat — DALL-E 3 sometimes appears only in fresh conversations.

### Generate an Image with Text

Type this prompt:

```
Create a professional social media graphic for a coffee shop. The image should show a latte with latte art on a rustic wooden table. Include the text "MORNING RITUAL" in elegant serif typography at the top. Use warm brown and cream tones. Minimalist style. Square format.
```

DALL-E 3 will generate one image. You should see the latte with the text "MORNING RITUAL" rendered correctly. DALL-E 3 is the best AI tool for text rendering — but it is still not perfect. Check the text carefully. Are all letters correct? Is the spelling right? If the text has errors, regenerate. DALL-E 3 gets text right approximately 70-80% of the time for short phrases.

### Learn DALL-E 3's Strengths and Limits

Use DALL-E 3 for these specific tasks:

- **Social media graphics with text overlays** — DALL-E 3 renders text more reliably than any other image generator. For Instagram posts with headlines, email headers with CTAs, and ad creatives with taglines, this is your tool.
- **Commercially safe images** — DALL-E 3 is trained on licensed data. There are fewer copyright concerns compared to Midjourney or Stable Diffusion. For clients in regulated industries (healthcare, finance, legal), DALL-E 3 is the safer choice.
- **Iterative refinement** — You can tell DALL-E 3 "make the text larger" or "change the background to blue" and it will adjust. This conversational workflow is faster than regenerating from scratch in Midjourney.
- **Simple illustrations and icons** — DALL-E 3 produces clean, consistent vector-style illustrations.

Do NOT use DALL-E 3 for:

- **Photorealistic imagery** — Midjourney is significantly better at photorealism. DALL-E 3 images often look "AI-generated" at close inspection.
- **Batch production** — DALL-E 3 generates one image at a time with no parameter control. For producing 50 variations, Midjourney or Stable Diffusion is faster.
- **Style matching** — DALL-E 3 has no style reference or character reference feature. You cannot lock in a specific visual style across multiple generations.

### Build the DALL-E 3 Prompt Template

Save this to your Notion "Prompt Templates" document:

```
Create a [format] for [client industry]. The image should show [subject description]. Include the text "[exact text]" in [typography style]. Use [color palette]. [Style/mood description]. [Aspect ratio] format.
```

Example:

```
Create a LinkedIn banner for a SaaS startup. The image should show an abstract data visualization in blue and white. Include the text "DATA DRIVES DECISIONS" in bold modern sans-serif typography. Use navy blue, white, and electric blue. Clean and professional corporate style. Landscape format.
```

### Step 2 Check-In

Verify each of these:

1. You can generate images with DALL-E 3 through ChatGPT Plus
2. You have produced at least 5 images containing text, with at least 3 having correct text rendering
3. You understand when to use DALL-E 3 vs. Midjourney (text/commercial safety vs. photorealism/batch)
4. You have saved the DALL-E 3 prompt template to Notion
5. You can refine an image conversationally ("make the background darker," "change text to X")

Move on only when all 5 are confirmed.

## Step 3: Set Up Stable Diffusion for Bulk Production

Midjourney and DALL-E 3 are your quality tools. Stable Diffusion is your quantity tool. When a client needs 100 product images, 50 social media variations, or 30 blog illustrations in the same style, Stable Diffusion produces them faster and cheaper. This step sets up the bulk production pipeline.

### Choose Your Stable Diffusion Platform

You have two options. Pick one:

**Option A: Leonardo.ai (recommended for beginners)** — Browser-based. No local GPU required. Free tier gives 150 tokens/day (approximately 15-30 images). Pro tier at $12/mo gives unlimited generations. Go to leonardo.ai, sign up, and you should see the dashboard with model selection and generation options.

**Option B: Automatic1111 (for advanced users with a strong GPU)** — Self-hosted. Requires an NVIDIA GPU with 8GB+ VRAM. Free to run but requires technical setup. Go to github.com/AUTOMATIC1111/stable-diffusion-webui and follow the installation instructions.

For this guide, we use Leonardo.ai because it requires no installation and the interface is straightforward.

### Configure Leonardo.ai for Batch Production

Open your browser and go to leonardo.ai. Log in. You should see the main dashboard with a "Image Generation" button prominently displayed.

Click **Image Generation**. You should see a generation panel on the left with model selection, prompt input, and settings. Do you see this panel? If you see a different interface, click the "AI Image Generation" tab in the left sidebar.

Configure these settings:

1. **Select Model:** Click the model dropdown. Select "Leonardo Diffusion XL" or "Leonardo Vision XL" — these are the highest quality models available. If you see only "Leonardo Diffusion," use that.
2. **Set Dimensions:** Click the dimension selector. Choose 1024x1024 for square images, 1344x768 for landscape, or 768x1344 for portrait.
3. **Set Number of Images:** Use the batch slider to set 4 images per generation (the maximum on free tier). On Pro, you can set up to 8.
4. **Enable Alchemy:** If you have Pro, toggle "Alchemy" on. This significantly improves image quality and coherence.
5. **Set Guidance Scale:** 7-9 for most work. Higher values follow the prompt more closely but can look rigid. Lower values are more creative but less predictable.

### Build the Bulk Prompt Template

Stable Diffusion prompts use a different structure than Midjourney. They benefit from weighted keywords and negative prompts. Save this to Notion:

```
Positive: (masterpiece), (best quality), [subject], [setting], [lighting], [color palette], [composition], [mood], [style], (detailed), (sharp focus), (professional)
Negative: (worst quality), (low quality), (blurry), (distorted), (text), (watermark), (deformed), (extra limbs), (bad anatomy), (mutated hands)
```

The parentheses add weight. Double parentheses add more weight. Example for batch product photography:

```
Positive: (masterpiece), (best quality), (product photography), minimalist leather bag on white marble surface, soft studio lighting, neutral warm tones, centered composition, premium feel, (ultra detailed), (sharp focus), (8k resolution)
Negative: (worst quality), (low quality), (blurry), (distorted), (text), (watermark), (shadows), (cluttered background), (grain)
```

### Generate a Test Batch

Paste the template into Leonardo.ai with a real subject. Click **Generate**. You should see 4 images appear after 20-40 seconds.

Review each image. Check for: correct subject, clean background, proper lighting, no artifacts (extra fingers, distorted shapes, floating objects). Discard any images with visible errors. In a batch of 4, expect 1-2 usable images on average. This is normal. That is why you generate in bulk.

### Step 3 Check-In

Verify each of these:

1. You can generate images on Leonardo.ai or your chosen Stable Diffusion platform
2. You have produced at least 20 images across 2 different subjects
3. You understand the positive/negative prompt structure
4. You can configure batch generation (4+ images at once)
5. You have saved the bulk prompt template to Notion

If any fail, go back and practice. Bulk production is where money is made. If you cannot generate consistent batches, you cannot deliver on retainer contracts.

## Step 4: Build Your Portfolio

You have zero clients. You need a portfolio that proves you can deliver. This step creates one from scratch. Do not skip this. No portfolio means no clients. Ever.

### Choose Three Target Industries

Pick three industries you want to serve. Choose based on your interest and the visual demand in that sector. Good options:

1. **E-commerce / Product Brands** — High volume, recurring need, easy to demonstrate before/after
2. **Restaurants / Food & Beverage** — Visual-heavy industry, constant social media demand, easy to find prospects
3. **Real Estate / Interior Design** — Premium clients, high willingness to pay, strong visual needs

Write these three industries down. You will build a mini-portfolio for each.

### Create 10 Images Per Industry

For each industry, produce 10 images using your full toolkit. Follow this breakdown per industry:

**5 product/lifestyle images** — Use Midjourney with photorealistic prompts. These are your hero shots. Make them stunning.

Example for e-commerce:
```
premium wireless headphones on a matte black surface with subtle blue accent lighting, studio photography, dark moody aesthetic, shot on Phase One IQ4 with 120mm lens, luxurious and modern --ar 4:5 --s 600 --v 6.1
```

**3 social media graphics** — Use DALL-E 3 with text overlays. These show you can produce ready-to-post content.

Example for restaurant:
```
Create an Instagram post for a Mediterranean restaurant. Show a beautifully plated dish of grilled halloumi with pomegranate and herbs on a white plate. Include the text "TASTE THE MEDITERRANEAN" in elegant serif typography at the bottom. Use warm orange and deep green tones. Square format.
```

**2 blog/website illustrations** — Use Leonardo.ai for consistency. These demonstrate bulk capability.

Example for real estate:
```
Positive: (masterpiece), (best quality), modern minimalist living room interior with floor-to-ceiling windows, natural daylight, Scandinavian design, neutral tones with blue accent, wide angle, (architectural photography), (8k)
Negative: (worst quality), (furniture distortion), (distorted), (cluttered), (dark), (grain)
```

### Edit Every Image

Raw AI output is not portfolio-ready. Edit every single image before it goes into your portfolio. Follow this editing sequence:

1. **Upscale** — Open Topaz Photo AI. Drag your image in. Click "Upscale" and set the target to 4x. This turns a 1024x1024 image into a 4096x4096 print-ready asset. Wait for processing (10-30 seconds per image). Save the upscaled version.

2. **Fix artifacts** — Open the upscaled image in Canva. Zoom to 200%. Check: hands (correct number of fingers?), faces (symmetrical?), text (spelled correctly?), edges (clean or frayed?), objects (floating or grounded?). Use Canva's eraser tool, clone tool, or text tool to fix issues. If an artifact is too severe to fix, discard the image and regenerate.

3. **Color correct** — In Canva, click "Edit Photo" → "Adjust." Set brightness, contrast, and saturation to match a consistent look. If your portfolio images look like they came from different sources, clients will notice. Aim for a cohesive visual language.

4. **Add branding** — Add a subtle watermark with your agency name in the bottom-right corner. Use a small, semi-transparent text element. This prevents theft and shows professionalism.

### Build the Portfolio Page

Create a portfolio using one of these options:

**Option A: Notion portfolio (fastest)** — Create a new Notion page called "[Your Agency Name] Portfolio." Add a gallery block. Upload all 30 edited images organized by industry. Add captions describing each project: the brief, the tool used, and the result.

**Option B: Canva portfolio website** — Go to canva.com and search for "portfolio website." Pick a template. Replace the placeholder images with your 30 images. Add project descriptions. Publish using Canva's free domain (youragency.canva.site).

**Option C: Carrd.co portfolio (most professional for $19/yr)** — Go to carrd.co. Pick a portfolio template. Upload images. Add descriptions. Publish on a custom domain.

Pick one. Build it today. A finished portfolio today beats a perfect portfolio next month.

### Step 4 Check-In

Verify each of these:

1. You have 30 edited images (10 per industry) that look professional at full size
2. Every image has been upscaled, artifact-checked, and color-corrected
3. Your portfolio is live and accessible via a URL you can share
4. Each image has a caption explaining the project context
5. Three people you trust have reviewed the portfolio and confirmed the quality is professional-grade

If you have fewer than 30 usable images after editing, generate more. Never pad a portfolio with mediocre work. Ten exceptional images per industry is better than twenty that look like AI experiments.

## Step 5: Build a Client Onboarding System

When a client says yes, you need a system. Not a feeling, not a vibe — a documented, repeatable system that captures every detail you need to produce images that match their brand. This step builds that system.

### Create the Brand Discovery Questionnaire

Open Notion. Create a new page called "Client Onboarding — [Client Name]" (you will duplicate this for each client). Build this questionnaire into it:

**Section 1: Brand Basics**
- Brand name
- Website URL
- Primary brand color (hex code, e.g., #2563EB)
- Secondary brand color (hex code)
- Brand fonts (or "no specific fonts")
- Brand tone in 3 adjectives (e.g., "professional, warm, innovative")

**Section 2: Visual Preferences**
- Share 5 images you love and 5 you hate (ask them to save these to a Pinterest board or share URLs)
- Preferred photography style: photorealistic / editorial / illustration / abstract / mixed
- Preferred lighting: natural / studio / dramatic / soft / mixed
- Preferred composition: centered / rule of thirds / flat lay / dynamic / minimal
- Color temperature: warm / cool / neutral
- Any visual elements to always include or always avoid

**Section 3: Project Details**
- What types of images do you need? (product shots, social media graphics, blog illustrations, ad creatives, email headers, website banners)
- How many images per month?
- What platforms? (Instagram, LinkedIn, Pinterest, website, email, print)
- Aspect ratios needed for each platform
- Any text that needs to appear regularly? (taglines, URLs, CTAs)
- Deadline for first delivery

**Section 4: Technical Requirements**
- Minimum resolution needed (web: 1080px, print: 300 DPI at target size)
- File format preference (PNG, JPG, SVG for illustrations)
- File naming convention preference
- Delivery method (Google Drive folder, Dropbox, WeTransfer)

Send this questionnaire to every new client before you start any work. Do not skip a single question. Missing information leads to revisions, and revisions kill your margin.

### Build the Visual Style Guide Template

After the client returns the questionnaire, create a Visual Style Guide for them. This document ensures consistency across every image you produce — even months later. Open Notion and create this template:

```
# [Client Name] — Visual Style Guide

## Brand Colors
- Primary: [hex code] — [usage: backgrounds, accents, text]
- Secondary: [hex code] — [usage: highlights, CTAs, borders]
- Neutral: [hex code] — [usage: backgrounds, body text]
- Accent: [hex code] — [usage: callouts, featured elements]

## Typography
- Headline font: [font name] or closest AI-friendly equivalent
- Body font: [font name] or closest AI-friendly equivalent
- Text style in AI images: [serif / sans-serif / script / bold / light]

## Style Keywords (use in every prompt)
- Photography style: [e.g., "editorial, clean, bright"]
- Lighting: [e.g., "soft natural window light, golden hour"]
- Composition: [e.g., "centered with breathing room, minimal background"]
- Color treatment: [e.g., "warm tones, slightly desaturated, cream highlights"]
- Mood: [e.g., "calm, sophisticated, approachable"]

## Midjourney Prompt Template
[subject] in [setting], [lighting from above], [color treatment from above], [composition from above], shot on [camera], [mood from above] --ar [ratio] --s [stylize value] --v 6.1 --no [exclusions]

## DALL-E 3 Prompt Template
Create a [format] for [client]. Show [subject]. Include text "[text]". Use [color palette]. [Mood from above]. [Aspect ratio].

## Reference Images
1. [URL or description] — "Like this because: [reason]"
2. [URL or description] — "Like this because: [reason]"
3. [URL or description] — "Like this because: [reason]"
4. [URL or description] — "Avoid this because: [reason]"
5. [URL or description] — "Avoid this because: [reason]"

## Aspect Ratios by Platform
- Instagram Feed: 1:1 (--ar 1:1)
- Instagram Reels/Stories: 9:16 (--ar 9:16)
- LinkedIn: 16:9 (--ar 16:9)
- Pinterest: 2:3 (--ar 2:3)
- Website Banner: 21:9 (--ar 21:9)
- Email Header: 3:1 (--ar 3:1)
- Facebook: 4:5 (--ar 4:5)
```

Fill this out for every client. Save it in Notion. Reference it before every generation. This document is the difference between a client who stays for 12 months and a client who churns after the first delivery.

### Step 5 Check-In

Verify each of these:

1. Your onboarding questionnaire is complete and saved in Notion
2. Your Visual Style Guide template is built and ready to duplicate for each client
3. You have tested the questionnaire by filling it out for a fictional client
4. You can create a complete Visual Style Guide in under 30 minutes from a completed questionnaire
5. The style guide includes reusable prompt templates for both Midjourney and DALL-E 3

## Step 6: Create a Revision Workflow

Clients will request revisions. This is not a problem — it is a feature. Revisions are where you prove your value and justify your pricing. But uncontrolled revisions will destroy your profitability. This step builds a revision system that keeps clients happy and your margins intact.

### Set the Revision Policy

Define this policy before your first client. Put it in your proposals and contracts. Here is the industry-standard structure:

**Tier 1: Image Pack ($200-500)** — Includes 2 rounds of revisions per image. Additional revisions: $25 per image per round.

**Tier 2: Monthly Retainer ($500-2,000)** — Includes 3 rounds of revisions per batch. Additional revisions: included if they take less than 30 minutes total; otherwise billed at $50/hour.

**Tier 3: Brand Visual Identity ($2,000-5,000)** — Includes unlimited revisions until the client signs off on the style guide. After sign-off, standard revision rules apply.

These limits exist because AI image generation is iterative by nature. You can produce 10 variations in 5 minutes. The client will always want "one more tweak." Boundaries prevent scope creep.

### Build the Revision Request Form

Create a form in Notion or Google Forms. Every revision request must come through this form. No DMs, no verbal requests, no "can you just quickly change..." messages. The form fields:

1. Client name
2. Project name
3. Image file name (the specific image to revise)
4. What to change (be specific: "make the background darker," "change text from X to Y," "remove the plant on the left")
5. Reference image (optional — attach an image showing the desired change)
6. Priority: standard (3-day turnaround) / rush (24-hour turnaround, +50% fee)

### Create the Revision Execution Process

When a revision request comes in, follow this exact sequence:

1. **Log the request** in your project tracker (Notion). Note the timestamp, the client, the image, and the requested change.

2. **Classify the change:**
   - **Prompt adjustment** — The change requires regenerating the image with a modified prompt. Example: "make the lighting warmer." Go back to Midjourney or DALL-E 3, modify the prompt, regenerate. Time: 5-15 minutes.
   - **Compositional edit** — The change requires moving, adding, or removing elements within the existing image. Example: "remove the plant on the left" or "add our logo in the corner." Open Canva, use the eraser or add elements. Time: 10-20 minutes.
   - **Text change** — The change involves modifying text in the image. Example: "change the tagline from X to Y." If the text was generated by AI, regenerate with the correct text. If the text was added in Canva, edit the text layer directly. Time: 5-10 minutes.
   - **Full redo** — The client wants a fundamentally different image. Example: "I don't like the style, can you try something completely different?" This counts as a new image, not a revision. Clarify with the client that this uses one of their revision rounds.

3. **Execute the revision** using the appropriate method above.

4. **Quality check** — Upscale if needed. Check for artifacts. Verify the change was implemented correctly.

5. **Deliver** the revised image with the same file name appended with "_v2" (or "_v3" for the third revision). Place it in the client's delivery folder.

6. **Log completion** in your project tracker. Note the time spent.

### Step 6 Check-In

Verify each of these:

1. Your revision policy is written and ready to include in proposals
2. Your revision request form is built and accessible
3. You have practiced the revision execution process on 3 of your portfolio images
4. You can complete a prompt-adjustment revision in under 15 minutes
5. You can complete a compositional edit in under 20 minutes

If your revision times are longer, practice. Speed is profit. Every extra minute on a revision is a minute you are not generating revenue.

## Step 7: Build Pricing Packages

Pricing is where most AI image agencies fail. They charge too little because AI generation "feels easy." It is not easy — the skill is in the prompting, the curation, the editing, and the consistency. Price for the value you deliver, not the effort you expend. This step builds your pricing structure.

### Define Your Service Tiers

Create this pricing table. Save it in Notion. Use it in every proposal.

| Tier | Price | What's Included | Turnaround | Revisions |
|------|-------|----------------|------------|-----------|
| **Single Image** | $25-75 per image | 1 AI-generated, edited, and branded image at up to 3 aspect ratios | 48 hours | 1 round |
| **Image Pack** | $300-500 for 10 images | 10 AI-generated, edited, and branded images in your choice of aspect ratios | 5 business days | 2 rounds per image |
| **Social Media Bundle** | $500-800 for 20 images | 20 images sized for 3 platforms (60 total files), with text overlays and brand elements | 7 business days | 3 rounds per batch |
| **Monthly Retainer** | $750-2,000/mo | 20-50 images/mo, all platforms, priority turnaround, style guide included | 48 hours per batch | 3 rounds per batch |
| **Brand Visual Identity** | $2,000-5,000 one-time | Complete visual style guide + 50 branded images + templates for ongoing use | 3-4 weeks | Unlimited until style sign-off |
| **Product Photography** | $500-2,000 per product | 10-25 AI product shots per product (lifestyle, white background, contextual, detail shots) | 7 business days | 3 rounds per product |

### Set Your Minimums

Never work below these minimums:

- **Minimum project value: $150.** Any project below this is not worth the admin overhead of onboarding, delivery, and invoicing.
- **Minimum per-image price: $15.** Below this, you are competing with stock photo pricing and losing.
- **Minimum retainer: $500/mo.** Below this, the client is not committed and will churn within 2 months.

### Create the Proposal Template

Build a reusable proposal in Notion or Google Docs. Structure:

```
# Visual Content Proposal for [Client Name]

## Understanding Your Needs
[2-3 sentences showing you understand their brand and visual challenges]

## Recommended Package
[Package name and price]

## What You'll Receive
- [X] AI-generated, professionally edited images
- Images sized for [platforms]
- [X] rounds of revisions per batch
- Delivery via [Google Drive / Dropbox]
- [Turnaround time] delivery

## Style Approach
Based on your brand, I'll produce images in [style description from style guide].
Here are 3 sample directions: [attach 3 test images]

## Investment
[Package price] — due upon project start
[Recurring price if retainer] — billed monthly

## Timeline
- Day 1-2: Brand discovery and style guide creation
- Day 3-5: First batch production
- Day 5-7: Revisions and final delivery

## Next Steps
1. Sign the proposal
2. Complete the onboarding questionnaire
3. Receive first batch by [date]
```

### Step 7 Check-In

Verify each of these:

1. Your pricing table is complete with at least 4 tiers
2. Your minimums are set and you will not negotiate below them
3. Your proposal template is built and saved
4. You have practiced writing a proposal for a fictional client
5. You can confidently explain your pricing to a prospect in under 2 minutes

## Step 8: Build a Batch Production System

This is where your agency becomes profitable. Producing one image is easy. Producing 50 consistent, brand-aligned images in a single afternoon is a system. This step builds that system.

### Create the Batch Production Workflow

Open Notion. Create a new page called "Batch Production System." Build this workflow:

**Phase 1: Batch Planning (30 minutes)**

1. Open the client's Visual Style Guide in Notion
2. Open the client's content calendar or image request list
3. For each image, write the subject, the platform, the aspect ratio, and any text to include
4. Group images by type: all product shots together, all social graphics together, all blog illustrations together
5. Write prompts for each group using the style guide's prompt templates

**Phase 2: Bulk Generation (1-2 hours)**

For Midjourney (photorealistic images):
1. Open Discord. Navigate to a private channel or your own server with the Midjourney bot
2. Generate images in sequence, using the style guide's consistent parameters (--s, --ar, --sref if applicable)
3. For each image, generate 4 variations (the default output)
4. From each set of 4, select the 1-2 best. Mark them with the envelope emoji to upscale (U1, U2, U3, U4)
5. Save the prompt and seed number for each selected image in your project tracker

For DALL-E 3 (text-heavy images):
1. Open ChatGPT. Select DALL-E 3
2. Generate each image sequentially, using the style guide's DALL-E template
3. If text is incorrect, regenerate immediately with a corrected prompt
4. Download each successful image

For Leonardo.ai (bulk variations):
1. Open Leonardo.ai. Select the appropriate model
2. Use the bulk prompt template from the style guide
3. Generate in batches of 4-8 images at once
4. Curate ruthlessly — discard any image with visible artifacts

**Phase 3: Editing Pipeline (1-3 hours)**

1. **Batch upscale** — Open Topaz Photo AI. Process all images through the upscale workflow. Set to 4x. Batch process if your license allows it.
2. **Batch artifact check** — Open each upscaled image in Canva. Zoom to 200%. Check hands, faces, text, edges. Flag any that need repair.
3. **Batch color correction** — Apply the style guide's color treatment to all images. In Canva, create a preset adjustment (brightness, contrast, saturation, warmth) and apply it to every image for consistency.
4. **Batch text/branding** — Add any required text overlays, logos, or brand elements using Canva. Use consistent positioning and sizing across all images.
5. **Batch resize** — For images that need multiple platform sizes, use Canva's "Resize" feature (Pro only) or manually resize and adjust composition for each aspect ratio.

**Phase 4: Quality Gate and Delivery (30 minutes)**

1. **Final review** — Scroll through all images in sequence. They should look like they belong to the same brand. If any image stands out as visually inconsistent, re-edit or regenerate it.
2. **File naming** — Use this convention: `[client]_[project]_[platform]_[number]_[version].png`. Example: `acme_social_IG_001_v1.png`.
3. **Folder structure** — Create a delivery folder in Google Drive or Dropbox:
   ```
   [Client Name]/
     [Project Name]/
       01_Final/
         Instagram/
         LinkedIn/
         Website/
       02_Revisions/
       03_Source_Files/
   ```
4. **Upload** — Place final images in the appropriate subfolders. Upload source files (unwatermarked, full resolution) to the Source Files folder for your records.
5. **Notify** — Send the client a link to the 01_Final folder with a brief message: "Your [X] images are ready. [Link]. Revisions are welcome via the revision form — details in the folder."

### Build the Batch Tracking Spreadsheet

Create a Google Sheet called "Batch Tracker — [Client Name]":

| Image # | Subject | Platform | Aspect Ratio | Status | Prompt | Seed | Notes | Revisions |
|---------|---------|----------|-------------|--------|--------|------|-------|-----------|
| 001 | Product hero shot | Instagram | 1:1 | Final | [prompt text] | 847291 | Gold version selected | v2: warmer lighting |
| 002 | Team illustration | LinkedIn | 16:9 | In Review | [prompt text] | 384721 | Hands need fixing | — |

This spreadsheet is your production record. It lets you reproduce any image, track revision history, and maintain consistency across batches. Fill it out during Phase 2 as you generate each image.

### Step 8 Check-In

Verify each of these:

1. Your batch production workflow is documented in Notion
2. You have executed one complete batch (10+ images) from planning to delivery
3. The batch took you under 4 hours from start to delivery
4. All images in the batch are visually consistent (same color treatment, same quality level)
5. Your batch tracking spreadsheet is set up and filled out for your test batch

If your batch took longer than 4 hours, identify the bottleneck. It is almost always the editing phase. Practice faster editing in Canva — learn keyboard shortcuts, create reusable templates, and build a library of brand element presets.

## Step 9: Master Style Consistency Techniques

Inconsistent output is the number one reason clients leave AI image agencies. One image looks photorealistic, the next looks like a watercolor painting, the next looks like a stock photo from 2012. This step teaches you the specific techniques that lock in visual consistency across an entire project.

### Technique 1: Style Reference (--sref) in Midjourney

Style reference is the single most powerful tool for consistency. Here is how to use it:

1. Generate or find one image that perfectly represents the desired visual style. This is your "anchor image."
2. Upload the anchor image to Discord (drag and drop into any message).
3. Right-click the uploaded image and select "Copy Link."
4. In your prompt, add `--sref [URL] --sw 500` (500 is a moderate style weight — increase to 750 for closer matching, decrease to 250 for more variation).
5. Every image generated with this --sref will share the same visual aesthetic.

Example:
```
modern office workspace with laptop and coffee cup, bright natural lighting, minimalist decor --sref https://cdn.discordapp.com/attachments/.../anchor.png --sw 500 --ar 16:9 --v 6.1
```

Generate 5 images using the same --sref. They should share a cohesive look — similar color treatment, lighting style, and compositional feel. If they look too similar (near-identical), lower the --sw value. If they look too different, raise it.

### Technique 2: Character Reference (--cref) in Midjourney

When a brand campaign needs the same person across multiple images (a brand ambassador, a founder portrait, a recurring character):

1. Generate or upload one clear image of the person (front-facing, good lighting, neutral expression works best).
2. Upload to Discord and copy the link.
3. Add `--cref [URL] --cw 100` to every prompt (100 = match face + hair + outfit; 0 = match face only).

Example:
```
woman in business casual outfit presenting at a whiteboard in a modern conference room --cref https://cdn.discordapp.com/attachments/.../person.png --cw 100 --ar 16:9 --v 6.1
```

Generate 3 images with the same --cref. The person should be recognizable across all of them. If the likeness is weak, try a different anchor image — some reference photos produce better results than others. Front-facing, evenly lit headshots work best.

### Technique 3: Seed Consistency

Midjourney assigns a random seed number to every generation. If you use the same seed with the same prompt, you get nearly identical images. If you use the same seed with a modified prompt, you get variations that share a visual "DNA."

1. Generate an image you love. After generation, react to the image with the envelope emoji to get the job ID and seed.
2. Note the seed number (it appears in the response or you can type `/info` after reacting).
3. In future prompts, add `--seed [number]` to maintain visual continuity.

This technique is subtle but powerful for batch work. Images with the same seed share a visual texture — similar grain, similar lighting angles, similar color rendering — even when the subject changes.

### Technique 4: The Color Lock Method

AI generators drift on color. To lock colors across a batch:

1. Define 3-5 hex codes from the client's brand palette.
2. Include the color names and hex codes in every prompt: "color palette of navy blue (#1B2A4A), warm cream (#F5F0E8), and copper accent (#B87333)."
3. In post-production, apply a color correction preset in Canva or Photoshop that pulls every image toward the target palette.
4. Use the "HSL" (Hue, Saturation, Luminance) adjustment to shift any off-brand colors toward the nearest brand color.

### Technique 5: The Composite Method for Complex Scenes

AI struggles with complex compositions (multiple people, specific layouts, product-in-context shots). The composite method breaks the scene into elements:

1. **Generate the background** — Prompt for the setting only. Example: "empty modern kitchen with marble countertops and natural lighting, wide angle --ar 4:5 --v 6.1"
2. **Generate the product** — Prompt for the product on a solid white or transparent-looking background. Example: "ceramic vase on pure white background, studio lighting, product photography --ar 1:1 --v 6.1"
3. **Composite in Canva** — Open Canva. Place the background image. Remove the background from the product image using Canva's Background Remover (Pro feature). Position the product on the background. Adjust lighting, shadows, and scale to match.
4. **Add final elements** — Add text, logos, or overlays.

This method produces images that look like cohesive professional photographs, not AI generations. It takes 10-15 minutes per composite, but the result is worth it for hero images and key deliverables.

### Step 9 Check-In

Verify each of these:

1. You have used --sref to produce 5 visually consistent images
2. You have used --cref to produce 3 images with the same person
3. You have used seed numbers to create a batch with shared visual DNA
4. You have applied the color lock method to correct off-brand colors in 3 images
5. You have created at least 1 composite image using the background + product method

These techniques separate you from people who just type prompts and hope. Practice until each technique is reliable.

## Step 10: Create and Deliver Brand Guidelines

Brand guideline creation is your highest-ticket service ($2,000-5,000). It is also your strongest retention tool — clients who receive a brand guide from you will come back for execution because you already know their system. This step builds your brand guideline product.

### Build the Brand Guideline Template

Create this document structure in Canva (for visual presentation) and Notion (for internal use):

**Section 1: Brand Overview**
- Brand mission (1-2 sentences)
- Brand voice (3 adjectives)
- Target audience (1-2 sentences)

**Section 2: Color System**
- Primary color with hex code, RGB, and CMYK values
- Secondary color with hex code, RGB, and CMYK values
- Neutral colors (2-3) with hex codes
- Accent color with hex code
- Color usage rules: which color dominates, which is accent, which is background
- Example images showing each color in context

**Section 3: Typography**
- Headline font (or AI prompt equivalent, e.g., "bold sans-serif" or "elegant serif")
- Body font (or AI prompt equivalent)
- Font pairing examples with sample text

**Section 4: Image Style**
- Photography style description (e.g., "bright, natural, editorial")
- Lighting direction (e.g., "soft window light, golden hour")
- Composition rules (e.g., "centered with negative space, never crowded")
- Mood descriptors (e.g., "warm, approachable, confident")
- 5-10 sample images representing the desired style
- 3-5 "anti-examples" — images that do NOT match the brand

**Section 5: AI Prompt Library**
- 5 reusable Midjourney prompts for the brand (one per common image type)
- 3 reusable DALL-E 3 prompts for text-heavy graphics
- The --sref anchor image and --sw recommended value
- The --cref reference image (if applicable) and --cw recommended value
- Recommended seed numbers for visual continuity

**Section 6: Social Media Templates**
- Instagram post template (with text overlay zones marked)
- Instagram Story template
- LinkedIn post template
- Facebook cover template
- Email header template

**Section 7: Usage Guidelines**
- Where to use AI-generated images vs. where to use photography
- Copyright and usage rights information
- Resolution and file format requirements by platform
- Brand element placement rules (logo size, position, clear space)

### Deliver the Brand Guideline

When the client signs off on the brand guide, deliver it in three formats:

1. **PDF presentation** — Export the Canva document as a high-quality PDF. This is the client-facing deliverable. It should look like a professional design agency produced it.

2. **Notion workspace** — Share the Notion version with the client. This is the living document they can reference anytime. Include all prompts, hex codes, and reference images in copy-paste format.

3. **Asset folder** — Deliver a Google Drive or Dropbox folder containing:
   - All 50+ branded images
   - The anchor images used for --sref and --cref
   - Canva template links for social media templates
   - The raw prompt library in a text file

### Step 10 Check-In

Verify each of these:

1. Your brand guideline template is complete with all 7 sections
2. You have created one full brand guideline for a fictional client
3. The guideline includes at least 5 reusable AI prompts
4. The guideline includes sample images that demonstrate the style
5. You can deliver a complete brand guideline package within 3 weeks of client onboarding

## Cost Breakdown

| Item | Free Tier | Paid Tier | When to Upgrade |
|------|-----------|-----------|-----------------|
| Midjourney | No free tier | $10/mo (Basic) or $30/mo (Standard) | Immediately — you need it for quality work |
| ChatGPT Plus (DALL-E 3) | Free ChatGPT (no DALL-E) | $20/mo | Immediately — text rendering requires it |
| Leonardo.ai | 150 tokens/day (~15-30 images) | $12/mo (Pro, unlimited) | At 3+ clients — free tier is too limiting for bulk |
| Canva | Free (limited) | $13/mo (Pro) | Immediately — background remover and brand kits are essential |
| Topaz Photo AI | Trial (watermarked) | $15/mo or $199 one-time | Immediately — client images must be high resolution |
| Adobe Firefly | 25 credits/mo | $5/mo (Premium) | When clients need commercially safe images |
| Notion | Free (for individuals) | $10/mo (Plus) | At 5+ clients for team collaboration |
| Google Drive | 15GB free | $2/mo (100GB) | At 3+ clients — image files add up fast |
| Domain for agency | — | $12/yr | Immediately — professional email and portfolio |
| Hosting for portfolio | — | Free (Carrd, Canva, Netlify) | Immediately |

**Total monthly cost at launch:** $58/mo
**Total monthly cost at 5 clients:** ~$90/mo (adding Leonardo Pro and extra storage)
**Total monthly cost at 10 clients:** ~$130/mo (adding team tools and increased storage)

A single Image Pack client at $300-500 covers your entire tool stack for 3-5 months. One Monthly Retainer client at $750+ covers everything with room to spare.

## Production Checklist

Before delivering any image batch to a client, verify every item:

- [ ] Every image has been upscaled to at least 2048px on the longest side (4K for print)
- [ ] Every image has been inspected at 200% zoom for AI artifacts (extra fingers, distorted text, floating objects)
- [ ] All text in images is spelled correctly and properly rendered
- [ ] Color treatment is consistent across the entire batch — no single image that looks "off"
- [ ] All images match the client's Visual Style Guide (lighting, composition, mood, color palette)
- [ ] Images are sized correctly for each target platform (correct aspect ratios and minimum dimensions)
- [ ] Brand elements (logos, text overlays, CTAs) are consistently positioned and sized
- [ ] File names follow the naming convention: `[client]_[project]_[platform]_[number]_[version].png`
- [ ] Delivery folder is organized by platform with clear subfolders
- [ ] Batch tracker spreadsheet is updated with prompts, seeds, and revision notes for reproducibility
- [ ] A cover image or summary sheet is included showing all delivered images in a grid view
- [ ] No watermarks remain on any delivered image (Topaz trial, Canva free elements, etc.)
- [ ] Client has received the delivery link and a message explaining revision policy
- [ ] Project is logged in your financial tracker with hours spent, revenue, and margin

## What to Do Next

Once you have delivered your first 3-5 client projects and have a repeatable production system, expand:

- **Add video content as an upsell.** Every image you generate can become a 5-second animated clip using Runway Gen-3 or Luma Dream Machine. Charge $20-50 per animated image. This doubles your revenue per client with 10 minutes of extra work per image. Open runway.ml, upload your image, type a motion description ("subtle camera pan to the right, gentle parallax effect"), generate, and deliver the MP4.

- **Build a client portal.** Create a Notion workspace for each client where they can view their Visual Style Guide, submit image requests, track delivery status, and access their asset library. This eliminates "where is that image from March?" emails and makes your service feel like a premium product.

- **Productize the brand audit.** Offer a $299 "Visual Brand Audit" where you analyze a prospect's current visuals and produce a 5-image sample pack showing what their brand could look like with AI-generated imagery. This converts at 25-40% because the value is tangible and immediate.

- **Hire a junior image editor.** At 8+ clients, your editing pipeline becomes the bottleneck. Hire someone on Upwork ($10-18/hr) to handle the editing phase (upscaling, artifact fixing, color correction, resizing). You focus on prompt engineering and client relationships. Document your editing SOP with screenshots in Notion — the editor should be able to follow it without asking you questions.

- **Explore Stable Diffusion Fine-Tuning.** If you have a strong GPU or use a cloud service like RunPod ($0.40/hr for an A100 GPU), you can train a LoRA (Low-Rank Adaptation) on a client's brand style. This produces images that are inherently consistent because the model has been fine-tuned on the brand's visual language. This is an advanced technique that commands premium pricing ($5,000-10,000 per fine-tuned model).

- **White-label your service.** Partner with marketing agencies, web designers, and social media managers who do not offer visual content creation. They resell your service under their brand. You handle production. Revenue split: 60/40 in your favor. One agency partnership can bring you 5-10 clients per quarter with zero sales effort on your part.
