---
title: "Build an AI Video Production Service with InVideo: The Complete Step-by-Step Guide"
date: 2026-10-27
category: "Implementation"
difficulty: "INTERMEDIATE"
readTime: "25 MIN"
excerpt: "**Prerequisites**"
image: "/images/articles/intelligence/create-edit-and-optimize-videos-with-luma-and-invideo.png"
heroImage: "/images/heroes/intelligence/create-edit-and-optimize-videos-with-luma-and-invideo.png"
relatedOpportunity: "/opportunities/how-to-build-an-ai-video-editing-agency-15k-25kmonth/"
---



## Prerequisites

**Prerequisites**

Before you begin building your AI‑powered video production service, gather the following accounts, tools, and budget. Each item is listed with its exact name, cost, and any free‑tier limitations so you can estimate the upfront spend and the time required to get everything in place.

- **Luma AI** – AI‑driven video generation.  
  - Subscription: $19 / month (Pro tier).  
  - Free trial: 10 AI‑generated clips per month.  
- **InVideo** – Cloud video editor with AI templates.  
  - Pro plan: $60 / month.  
  - Free tier: 60 templates, 50 exports/month.  
- [**Canva Pro**](https://www.canva.com/) – Design platform for thumbnails, overlays, and branding assets.  
  - $12.99 / month.  
  - Free tier: limited templates and brand kit features.  
- [**Make.com**](https://www.make.com/en/register?pc=menshly) – Automation platform to stitch Luma ➜ InVideo workflows.  
  - Free tier: 200 operations/month.  
  - Paid plan: $29 / month for 10,000 operations.  
- [**Replit**](https://replit.com/refer/egwuokwor) – Cloud IDE for writing any auxiliary scripts (e.g., custom metadata injection).  
  - Free tier: unlimited public workspaces.  
  - Paid plan: $7 / month for private workspaces (optional).  
- [**Notion**](https://notion.so/) – Workspace for project tracking and client brief templates.  
  - Free tier: unlimited pages.  

**Time to set up**  
- Signing up for each platform: ~15 minutes.  
- Configuring API keys (Luma → InVideo → Make.com): ~15 minutes.  
- Creating a sample project in InVideo and linking it to Luma via Make.com: ~30 minutes.  

**Total upfront cost** (using the lowest paid tiers)  
- Luma AI: $19  
- InVideo Pro: $60  
- Canva Pro: $12.99  
- Make.com starter: $29  
- **Total**: **$120.99** (recurring monthly)

---

| Tool          | Purpose                                 | Cost                  | Free Tier Limit                                 |
|---------------|-----------------------------------------|-----------------------|-------------------------------------------------|
| Luma AI       | AI video generation                     | $19 / month           | 10 clips/month                                  |
| InVideo       | Cloud video editing & templating        | $60 / month           | 60 templates, 50 exports/month                 |
| Canva Pro     | Design assets (thumbnails, overlays)    | $12.99 / month        | Limited templates, brand kit                   |
| Make.com      | Automation of Luma ➜ InVideo workflows | $29 / month (starter) | 200 operations/month                            |
| Replit        | Script development (optional)           | $7 / month (pro)      | Unlimited public workspaces                     |
| Notion        | Project & brief management              | Free                  | Unlimited pages                                 |

With these accounts and budgets in place, you’re ready to dive into the next section: setting up the Luma ➜ InVideo integration and automating the entire workflow.

## Step 1 : Setup and Configuration

1. **Create a dedicated project folder on your local machine**  
   Open a terminal (macOS: `/Applications/Utilities/Terminal.app`; Windows: `cmd` or `PowerShell`) and run:

   ```bash
   mkdir -p ~/projects/luma-invideo && cd ~/projects/luma-invideo
   ```

   *Expected output:*  
   ```
   $ mkdir -p ~/projects/luma-invideo && cd ~/projects/luma-invideo
   $ pwd
   /Users/yourname/projects/luma-invideo
   ```

   **Check‑in**: Do you see a folder called `luma-invideo` in your home directory? If not, ensure you have write permissions to `~/projects`.

2. **Initialize a Git repository** – this keeps version history and enables collaboration.  

   ```bash
   git init
   git commit --allow-empty -m "Initial commit – project skeleton"
   ```

   *Expected output:*  
   ```
   Initialized empty Git repository in /Users/yourname/projects/luma-invideo/.git/
   [master (root-commit) 9f2a7b4] Initial commit – project skeleton
   ```

   **Check‑in**: Do you see the commit hash `9f2a7b4`? If you get `fatal: not a git repository`, you are not inside the folder – double‑check the `cd` command.

3. **Create a virtual environment** (recommended for Python‑based tooling) and activate it.  

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   # .venv\Scripts\activate     # Windows
   ```

   *Expected output:*  
   ```
   ( .venv ) $
   ```

   **Check‑in**: Your prompt should now start with `(.venv)`. If you see `[venv]` or nothing changes, you might be using an older shell; try `bash` or `zsh`.

4. **Install the SDKs for Luma and InVideo**. Both expose REST APIs; they require the `requests` library and a small wrapper.  

   ```bash
   pip install requests python-dotenv
   ```

   *Expected output:*  
   ```
   Collecting requests
     Downloading requests-2.31.0-py2.py3-none-any.whl (62 kB)
   Collecting python-dotenv
     Downloading python_dotenv-1.0.1-py2.py3-none-any.whl (10 kB)
   Installing collected packages: python-dotenv, requests
   Successfully installed python-dotenv-1.0.1 requests-2.31.0
   ```

   **Check‑in**: Open `pip list` to confirm both packages appear. If `pip` fails, ensure your Python version is ≥ 3.8.

5. **Create a configuration file** (`.env`) to store your API keys and secrets.  

   ```bash
   cat <<EOF > .env
   # Luma API
   LUMA_API_KEY=YOUR_LUMA_API_KEY
   LUMA_ORG_ID=YOUR_LUMA_ORG_ID

   # InVideo API
   INVIDEO_API_KEY=YOUR_INVIDEO_API_KEY

   # Optional: ElevenLabs voice synthesis for captions
   ELEVENLABS_API_KEY=YOUR_ELEVENLABS_KEY
   EOF
   ```

   Replace the placeholder values with the actual keys you will obtain in step 6. **Never commit `.env`** – add it to `.gitignore`.

   **Check‑in**: Run `cat .env` to verify the four lines appear exactly as shown. If you see `YOUR_LUMA_API_KEY` still, you need to replace it.

6. **Sign up for Luma, InVideo, and ElevenLabs** (optional).  

   - **Luma**: Go to <https://www.luma.ai> → Click “Get Started” → Complete the signup wizard.  
     - *Price*: Basic plan starts at $19/month.  
     - After login, navigate to **Account → API**.  
     - Click **Generate New API Key**.  
     - Copy the key and paste it into `.env` (`LUMA_API_KEY`).  

     *Expected UI*: You should see a modal titled “API Key Generated” with a 32‑character string.

   - **InVideo**: Visit <https://invideo.io> → Sign up → In the dashboard, go to **Settings → API**.  
     - Click **Create API Key**.  
     - Copy the key to `.env` (`INVIDEO_API_KEY`).  

     *Expected UI*: A green banner “Your API key is ready” with a 32‑character alphanumeric token.

   - [**ElevenLabs**](https://elevenlabs.io/) (optional for voice‑over generation):  
     - Go to <https://elevenlabs.io> → Sign up → In the user panel, select **API**.  
     - Generate a key and paste it into `.env` (`ELEVENLABS_API_KEY`).  

     *Expected UI*: A dialog showing “API Key: e8c3…b7f” and an **Copy** button.

   **Check‑in**: Do you see the “Generate API Key” button in each service’s settings? If the button is disabled, you might need to upgrade to a paid tier. The free tier often hides the API section.

7. **Verify API connectivity** using a quick Python script. Create `test_api.py`:

   ```python
   import os
   import requests
  

## Step 2 : Build the Core System  
*(≈ 550 words)*  

In this section you will wire the three pillars of the service: **Luma** for AI‑driven storyboard generation, **InVideo** for the final video assembly, and a lightweight orchestration layer built in **Replit** that calls both APIs in sequence. The system will live behind a single Make.com (formerly Integromat) scenario that triggers on a “new job” event from a front‑end form (e.g., a Calendly‑scheduled meeting or a Klaviyo double‑opt‑in). All configurations below are exact; copy the code blocks or click the buttons as described.

---

### 2.1 Create a Project in Luma

1. Log into **Luma** (https://luma.ai).  
2. Click **“Create Project”** in the top‑right corner.  
3. In the pop‑up, set:  
   * **Project Name** – `ClientVideoWorkflow`  
   * [**Description**](https://www.descript.com/) – `Automated storyboard generation for InVideo`  
   * **Template** – `Corporate Intro` (the pre‑built template that matches your target audience)  
4. Click **Save**.  

**Interactive Check‑in**  
Do you see a project page that lists “ClientVideoWorkflow” with a status of **Draft**? If not, go back to the Projects dashboard and confirm the name.

**Expected Output**  
A screen that reads:  
```
Project: ClientVideoWorkflow
Status: Draft
Template: Corporate Intro
```

**Error Scenario**  
If the project name contains spaces or special characters, Luma will return:  
`Error: Invalid project name`.  
**Fix** – rename to `ClientVideoWorkflow` (no spaces, no punctuation).

---

### 2.2 Configure InVideo API Integration

1. In **InVideo** (https://invideo.io), navigate to **Settings** > **API & Integrations**.  
2. Click **“Generate API Key”**.  
3. Copy the key to your clipboard.  
4. Store the key in Replit’s secrets panel (see 2.3).  

**Interactive Check‑in**  
Do you see a 32‑character string displayed after you click *Generate API Key*? It should look like `01a2b3c4d5e6f7g8h9i0jklmnopqrs`.  

**Expected Output**  
A modal that says:  
```
Your new API key is: 01a2b3c4d5e6f7g8h9i0jklmnopqrs
```

**Error Scenario**  
If the key is not 32 characters, InVideo will respond:  
`Error: API key length invalid`.  
**Fix** – delete the key and generate a new one.

---

### 2.3 Set Up the Orchestration Layer in Replit

1. Open **Replit** (https://replit.com).  
2. Click **“+ Create”** > **“New Repl”**.  
3. Choose **Language**: `Python 3`.  
4. Name the Repl `video‑pipeline`.  
5. In the left sidebar, click the **Secrets** tab (🔒 icon).  
6. Add the following keys:  

| Secret Key | Value |
|------------|-------|
| `LUMA_API_KEY` | *Your Luma API key from step 2.1* |
| `INV_API_KEY`  | *Your InVideo API key from step 2.2* |
| `INV_PROJECT_ID` | *Project ID obtained from InVideo after creating a project for the output video (click “Projects” → “New Project” → copy the ID)* |

**Interactive Check‑in**  
Do you see the three secrets listed under `Secrets`? The values should be masked with asterisks.  

**Expected Output**  
```
Secrets:
- LUMA_API_KEY (***************)
- INV_API_KEY  (****************)
- INV_PROJECT_ID (****************)
```

**Error Scenario**  
If Replit throws `Error: Secret key already exists`, delete the old secret before adding the new one.

---

#### 2.3.1 Core Pipeline Script

Create a file called `main.py` and paste the following code. It pulls a prompt from Make.com, sends it to Luma, receives a storyboard JSON, then posts that storyboard to InVideo to generate the final video.

```python
import os
import requests
import json

LUMA_ENDPOINT = "https://api.luma.ai/v1/storyboard"
INV_ENDPOINT  = "https://api.invideo.io/v1/projects"

def generate_storyboard(prompt):
    headers = {"Authorization": f"Bearer {os.environ['LUMA_API_KEY']}"}
    payload = {"prompt": prompt, "template": "Corporate Intro"}
    resp = requests.post(LUMA_ENDPOINT, headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json()  # storyboard JSON

def create_video(storyboard):
    headers = {"Authorization": f"Bearer {os.environ['INV_API_KEY']}"}
    payload = {
        "project_id": os.environ['INV_PROJECT_ID'],
        "storyboard": storyboard
    }
    resp = requests.post(INV_ENDPOINT, headers=headers, json=payload)
    resp.raise_for_status()
    return resp.json()  # contains video URL

def main():
    # Make.com will POST a JSON payload to this endpoint
    # Example payload: {"prompt":"Launch video for new SaaS product"}
    from flask import Flask, request, jsonify


## Step 3 : Test and Validate  

### 3.1 Verify the InVideo Template Pipeline  

1. **Trigger a test run**  
   - In the Make.com scenario that connects your Flask API to InVideo, click **Run once**.  
   - In the execution log, confirm the *HTTP Request* module succeeded (HTTP 200).  
   - Look for the line:  
     ```
     "status":"completed","video_id":"INV123456789"
     ```
   - *Do you see “video_id” in the log?* You should see a 12‑digit ID.  
     If it’s missing, check that the “Authorization: Bearer <API‑KEY>” header is present.

2. **Download the output file**  
   - In the same scenario, the *HTTP Request – Download* module will fetch the MP4.  
   - Save it to `~/videos/test.mp4`.  
   - Open the file in VLC.  
   - Expected result: 1080p, 30 fps, 2 min duration, no black frames at start/end.  
   - *If you see a 0‑second clip, the InVideo job failed; retry after 30 seconds.*

### 3.2 Confirm Luma AI Overlays  

1. **Run the Luma inference script**  
   ```bash
   python luma_overlay.py --input ~/videos/test.mp4 --output ~/videos/test_luma.mp4
   ```
2. **Check the log**  
   ```
   INFO: 100% |██████████| 1/1 [00:12<00:00, 12.34s/it]
   INFO: 2 overlays applied
   ```
3. **Validate the overlay**  
   - Open `test_luma.mp4`.  
   - The first 5 seconds should display the Luma AI logo at top‑right, 50 % opacity.  
   - *If the logo is missing, verify the `overlay_path` in `luma_overlay.py` points to `luma_logo.png`.*

### 3.3 Cross‑Check with ElevenLabs Voice‑Synthesis  

1. **Generate a short voice clip**  
   ```bash
   python synthesize.py --text "Welcome to your AI‑generated video" --output voice.mp3
   ```
2. **Play the clip**  
   - Ensure the speech is clear, 2 KHz sampling, 320 kbps bitrate.  
   - *If you hear distortion, update the `sample_rate` to 22050 in the script.*

### 3.4 Error Scenarios & Fixes  

| Error | Cause | Fix |
|-------|-------|-----|
| `HTTP 403` from InVideo | API key expired | Renew key in your Make.com environment variable |
| `File too large` on upload | Exceeds 2 GB | Compress with `ffmpeg -i input.mp4 -b:v 3M output.mp4` |
| Luma overlay fails | Missing `opencv-python` | `pip install opencv-python-headless` |

### 3.5 5‑Point Test Checklist  

1. **Resolution & FPS** – Video renders 1920×1080 at 30 fps.  
2. **Audio Sync** – Voice clip aligns with visual cues, no lag > 100 ms.  
3. **Overlay Presence** – Luma logo appears in all required frames.  
4. **Template Data** – All InVideo placeholders (`{{title}}`, `{{subtitle}}`) replaced.  
5. **File Size** – Final MP4 ≤ 500 MB (use `ffprobe -v error -show_entries format=size -of default=noprint_wrappers=1:nokey=1 test_luma.mp4`).

Complete this checklist before moving to the deployment step. If any item fails, repeat the corresponding sub‑step until the expected output appears.

## Step 4 : Add Advanced Features  
*Goal:* Turn the core InVideo workflow into a production‑ready, fault‑tolerant service by adding AI‑enriched voiceovers, subtitle generation, automated routing, and notification plumbing. We’ll use **Make.com**, **Replit**, **ElevenLabs**, [**Vapi**](https://vapi.ai/), **Klaviyo**, and **Zapier** for this step.

---

### 4.1 Deploy the Voice‑Over Microservice on Replit  

1. **Create a new Replit project**  
   - Open Replit, click *New Repl*, choose *Python* (3.11).  
   - Name it `video-voiceover-service`.  
   - After the repl loads, you’ll see `main.py` and a `requirements.txt` file.

2. **Add dependencies**  
   - In `requirements.txt`, add:  
     ```
     requests
     python-dotenv
     ```
   - Click *Packages* → search for `python-dotenv`, click the plus icon to install.

3. **Write the voice‑over script**  
   ```python
   import os
   import json
   import requests
   from dotenv import load_dotenv

   load_dotenv()  # loads .env variables

   ELEVENLABS_API = os.getenv("ELEVENLABS_API_KEY")
   ELEVENLABS_URL = "https://api.elevenlabs.io/v1/text-to-speech/eleven_monolingual_v1"

   def synthesize(text, voice_id="Rachel"):
       payload = {
           "text": text,
           "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
       }
       headers = {
           "Accept": "application/json",
           "xi-api-key": ELEVENLABS_API,
       }
       resp = requests.post(ELEVENLABS_URL, json=payload, headers=headers)
       if resp.status_code != 200:
           raise Exception(f"ElevenLabs error: {resp.text}")
       return resp.content  # raw audio bytes

   if __name__ == "__main__":
       sample_text = "Hello, world! This is your automated voiceover."
       audio = synthesize(sample_text)
       with open("voiceover.mp3", "wb") as f:
           f.write(audio)
       print("✅ Voiceover written to voiceover.mp3")
   ```

4. **Configure environment variables**  
   - Click *Secrets* → *Add new* → key: `ELEVENLABS_API_KEY`, value: *your ElevenLabs API key*.  
   - If you don’t have a key, sign up at ElevenLabs and copy the “API Key” from the dashboard.  
   - **Check‑in:** “Do you see the `voiceover.mp3` file listed in the left‑hand file tree after running the script? If you see `⚠️` next to the file, the script crashed – check the console for an error.”

5. **Test locally**  
   - Click *Run*. The console should output:  
     ```
     ✅ Voiceover written to voiceover.mp3
     ```
   - If you receive *4xx* or *5xx* status codes, the error message will help you troubleshoot (e.g., API key revoked → re‑generate key).

---

### 4.2 Integrate Voice‑Over with InVideo via Make.com  

1. **Create a Make.com scenario**  
   - Log into Make.com, click *Create a new scenario*.  
   - Add the **InVideo** module → *Get video export* → set *Video ID* to `{{video_id}}`.  
   - Add the **HTTP** module → *Make a request* → *POST* to `https://api.replit.com/v0/runs?repl_id=video-voiceover-service`.  
   - In *Body* (JSON), set:  
     ```json
     {
       "text": "{{video_script}}",
       "voice_id": "Rachel"
     }
     ```
   - Map `{{video_script}}` from the InVideo step where you extracted the text from the storyboard.

2. **Configure the HTTP module**  
   - **URL:** `https://api.replit.com/v0/runs?repl_id=video-voiceover-service`  
   - **Method:** `POST`  
   - **Headers:**  
     - `Content-Type: application/json`  
     - `Authorization: Bearer {{replit_api_token}}`  
   - Store your Replit API token in Make.com’s *Variables* → *Add a variable* → name `replit_api_token` → value: *your token*.

3. **Add a file upload step**  
   - After the HTTP request, add the **InVideo** module → *Upload media* → upload the `voiceover.mp3` returned

## Step 5 : Deploy to Production

Deploying the Luma‑InVideo pipeline to a production‑grade environment guarantees low latency, high reliability, and the ability to scale as your client base grows. In this section we’ll spin up a small VPS on **Hostinger** ($3.99 / month), containerize the service, and expose it behind an Nginx reverse proxy with an HTTPS certificate from Let’s Encrypt. Once the endpoint is live you can hook it into **Make.com** or **Zapier** to trigger video builds automatically.

> **Prerequisites**  
> • A Hostinger VPS with root SSH access  
> • Docker Hub account (free tier)  
> • Valid InVideo and Luma API keys  
> • Domain name pointing at the VPS IP (e.g., `videos.menshlyglobal.com`)

### 5.1 Create the Docker image

1. **Create a Dockerfile** in the root of your project:

   ```dockerfile
   FROM python:3.11-slim

   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt

   COPY . .
   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
   ```

   *Do you see the `CMD` line?* It binds the FastAPI app to port 8080.  
   *If you do not see the `CMD`, add it and rebuild.*

2. **Build the image locally**:

   ```bash
   docker build -t menshlyvideo:latest .
   ```

   Expected output:

   ```
   Step 1/6 : FROM python:3.11-slim
   ---> c8b8c1b9e8f1
   Step 2/6 : WORKDIR /app
   ---> Running in 4a1c...
   ---> 4a1c...
   Step 3/6 : COPY requirements.txt .
   ---> 5f3d...
   Step 4/6 : RUN pip install -r requirements.txt
   ---> Running in 6b4d...
   ---> 6b4d...
   Step 5/6 : COPY . .
   ---> 7c2e...
   Step 6/6 : CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
   ---> Running in 8d3f...
   ---> 8d3f...
   Successfully built 8d3f...
   ```

   *If you see `ERROR: Could not find a version that satisfies the requirement luma`*, add `luma==<correct‑version>` to `requirements.txt`.

3. **Push to Docker Hub** (replace `yourdockerhub` with your handle):

   ```bash
   docker tag menshlyvideo:latest yourdockerhub/menshlyvideo:latest
   docker push yourdockerhub/menshlyvideo:latest
   ```

   *You should see “Pushed” after the upload completes.*

### 5.2 Deploy on Hostinger

1. **SSH into the VPS**:

   ```bash
   ssh root@<HOSTINGER_IP>
   ```

   *Do you see the Hostinger welcome banner?* If not, verify your IP.

2. **Install Docker**:

   ```bash
   apt update
   apt install -y docker.io
   systemctl enable docker
   systemctl start docker
   ```

   Verify: `docker --version` → `Docker version 24.0.5, build a5ee71a`.

3. **Pull the image**:

   ```bash
   docker pull yourdockerhub/menshlyvideo:latest
   ```

4. **Create a systemd service** (`/etc/systemd/system/menshlyvideo.service`):

   ```ini
   [Unit]
   Description=Menshly Video API
   After=network.target

   [Service]
   WorkingDirectory=/opt/menshlyvideo
   ExecStart=/usr/bin/docker run --rm -e INVIDEO_API_KEY=$INVIDEO_API_KEY -e LUMA_API_KEY=$LUMA_API_KEY -p 8080:8080 yourdockerhub/menshlyvideo:latest
   Restart=always
   RestartSec=10

   [Install]
   WantedBy=multi-user.target
   ```

   *Set environment variables* in `/etc/environment` or a `.env` file:

   ```
   INVIDEO_API_KEY=sk_XXXXXXXXXXXXXXXX
   LUMA_API_KEY=lk_YYYYYYYYYYYY
   ```

5. **Enable and start**:

   ```bash
   systemctl daemon-reload
   systemctl enable mens

## Step 6 : Scale and Grow  
**Goal:** Expand from a single client to 10 + clients while maintaining quality and profitability.  
**Time‑box:** ~30 min per sub‑step (total ≈ 2 h).

---

### 1. Automate the Intake Pipeline  

1️⃣ **Create a Google Form**  
- Path: *Google Drive → New → Google Form*  
- Title: **“Video Project Request”**  
- Fields:  
  - **Client Name** (Short answer)  
  - **Project Description** (Paragraph)  
  - **Target Length** (Number, units = “seconds”)  
  - **Upload Reference Video** (File upload, max 10 MB)  
  - **Preferred Voice‑over** (Multiple choice: “None”, “ElevenLabs”, “Vapi”)  

1️⃣ Check‑in: *Do you see the “Responses” tab? You should see an empty grid.*  

2️⃣ **Connect Form to InVideo via Make.com**  
- Make.com plan: **Starter ($0/month)** – 500 tasks/month.  
- Scenario: *Google Forms → InVideo*  
  - Trigger: *New Form Response*  
  - Action: *Create a Project* → *Use Template “Standard Promo”*  
  - Map fields:  
    - `Project Description` → *Title*  
    - `Target Length` → *Duration*  
    - `Upload Reference Video` → *Upload File* (use InVideo’s “Upload” API endpoint: `https://api.invideo.io/v1/upload`)  

2️⃣ Check‑in: *Do you see the “Make.com Dashboard” with a green “Success” icon next to the trigger?*  

3️⃣ **Automate Client Notification**  
- Add **SendGrid** (email) or **Klaviyo** (if already in use) inside the same Make.com scenario:  
  - Action: *Send Email* → “Your video is queued”  
  - Recipient: *Client Email* field from the form.  

**Error Scenario:**  
- *If you see “Unauthorized” when calling InVideo API, ensure your API key is stored in Make.com under “Variables → INVIDEO_API_KEY”.*  

---

### 2. Standardize Template Library  

- InVideo: **Create 5 core templates** (intro, product demo, testimonial, call‑to‑action, outro).  
- Path: *InVideo → Templates → New Template*  
- Export each template as JSON.  
- Store JSON in **GitHub repo** (private).  
- Use **Replit** to host a small Node.js service that pulls the JSON and populates it with client data.  
  - Repo: `https://github.com/yourorg/innova-video-templates`  
  - Replit plan: **Hobby ($7/month)** – sufficient for 100 requests/day.  

**Check‑in:** *Open Replit, click “Run”, and confirm the terminal shows “Template fetched successfully”.*  

---

### 3. Hire a Junior Editor (Remote)  

| Role | Salary | Onboarding Tasks |
|------|--------|------------------|
| Junior Video Editor | $15 /hr (30 h/wk) | 1) Access InVideo workspace 2) Learn template usage 3) Polish AI‑generated cuts 4) QA final renders |

- Use **ActiveCampaign** to automate interview scheduling via **Calendly**.  
  - Calendly event: *“Candidate Screening”* (30 min)  
  - ActiveCampaign action: *Add Contact → Tag “Editor‑Candidate”*  

**Check‑in:** *Do you see the new contact in ActiveCampaign under “Contacts → Editor‑Candidate”?*  

---

### 4. Margin Improvement  

1. **Cost per Video**  
   - InVideo subscription: **Pro ($30/month)** → 20 credits/month.  
   - Each video uses 2 credits → $3/credit → $6 cost.  

2. **Pricing Strategy**  
   - Base price: **$30/video** → 5 × $6 cost = **$24 margin**.  
   - Upsell voice‑over (ElevenLabs): $5 extra.  

3. **Recurring Revenue**  
   - Offer a **Monthly Subscription** ($120/month) = 4 videos + 1 live coaching.  

---

### 5. Scale Milestones (Table)

| Clients | Monthly Revenue | Automation Level | Team Size | Notes |
|---------|-----------------|------------------|-----------|-------|
| 1‑3 | $300–$900 | Basic Make.com & InVideo templates | 1 editor | Validate pipeline |
| 4‑6 | $1,200–$2,400 | Add Replit workflow, Zapier (forms → Slack) | 2 editors | Start QA process |
| 7‑10 | $2,800–$4,200 | Integrate Vapi for voice‑overs, Buffer for social teasers | 3 editors | Launch upsell |
| 10+ | $5,000+ | Full CI/CD with GitHub Actions, dedicated support chat (Canva Docs) | 5 editors + 1 CX | Expand marketing |

**Final Check‑in:** *Run a test project through the entire automated flow and confirm the client receives the final MP4 in their inbox within 1 hour. If it takes longer, review Make.com task logs for failures.*

**Outcome:** You now have a repeatable, low‑margin pipeline capable of handling 10+ clients while freeing up your time for strategic growth.

## Cost Breakdown

| Item | Free Tier | Paid Tier | When to Upgrade |
|------|-----------|-----------|-----------------|
| **InVideo – Subscription** | Unlimited 720 p exports, 50 videos/month | **Pro – $30 / mo** (1080 p, unlimited videos) | When you need > 50 videos/month or 1080 p resolution |
| **Luma AI – Credits** | 500 credits/month | **Pro – $19 / mo** (1,500 credits) | Exceed 500 credits or require faster rendering |
| **Make.com – Operations** | 200 operations/month | **Growth – $49 / mo** (1,000 ops) | > 200 automated tasks/month |
| **Replit – Cloud IDE** | 1 GB storage, 1 GB RAM | **Hacker – $7 / mo** (2 GB storage, 2 GB RAM) | Project > 1 GB or needs more RAM |
| **Vapi – Voice

## Production Checklist

Before you hit “Publish” for a client, run through the following 10 verifications. Each item is measurable and requires an exact action or setting.

- **Export Settings** – In InVideo, open **Settings → Export**. Verify **Resolution = 1920×1080**, **Frame Rate = 30 fps**, **Bitrate = 8 Mbps**, **Format = MP4**. If the dialog does not appear, navigate to the **Project** tab and click the **Export** button.  
- **Template Match** – In Luma, click **Templates** and select **ID 12345**. The preview must display the exact assets outlined in the client brief. If the preview differs, edit the fields until they match.  
- **Audio License** – In the InVideo audio library, locate **Background Music ID 6789**. The license status should read **“Royalty‑Free”**. If it says **“Restricted”**, replace the track with a free‑use alternative.  
- **Text Overlay Accuracy** – In InVideo’s **Text Editor**, set **Client Name** to **Montserrat Bold, 48 pt, #FFFFFF**. Confirm the overlay aligns correctly in the preview. Adjust the anchor point if it is off‑center.  
- **Duration Sync** – The timeline should read **00:30:00**. If longer, use the trim tool to cut excess footage. The final clip must be exactly 30 seconds.  
- **Metadata Tagging** – Open **Project Settings → Metadata** and enter:  
  - Title: *“AI Video Production – InVideo/Luma”*  
  - Description: *“Automated 30‑second promo”*  
  - Keywords: *“AI Video Production, InVideo, Luma”*  
  Save and confirm the tags appear in the exported file’s properties.  
- **API Key Validation** – In Replit, ensure the `.env` file contains `LUMA_API_KEY=LUMA_abcdef1234`. Run `python test_luma.py`; expect JSON `{"status":"success"}`. If you receive **401 Unauthorized**, regenerate the key in the Luma dashboard and update the `.env` file.  
- **Cloud Storage Sync** – Upload the MP4 to **Hostinger FTP** folder `/videos/clientX/`. After upload, run `md5sum` locally and compare with the server checksum. They must match exactly.  
- **Automation Trigger** – In Zapier, open the **Upload to Hostinger** Zap. Verify the **Webhook URL** is correct and that the test payload returns **200 OK**. If the Zap fails, review the Zapier logs for missing fields.  
- **Client Preview Link** – In InVideo, click **Share → Link**. Copy the URL and open it in a new tab. The video should play without buffering or errors. If playback fails, re‑export the file.

**Do you see each of these items correctly configured?** If any step fails, pause the deployment, fix the issue, and re‑run the checklist before going live.

## What to Do Next

**1. Automate Project Creation with Zapier**  
Create a Zap that links your Notion client‑brief database to InVideo.  
- In Zapier, click **Create Zap** → **Trigger**: Notion → **Event**: “New Database Item”.  
- Map the **Title**, **Script**, and **Client ID** fields.  
- Add an **Action**: InVideo → “Create Project from Template”.  
  - In the template field, enter the ID of your Luma‑edited “Standard Promo” template.  
  - Set **Resolution** to **1080p**, **Frame Rate** to **30 fps**, and **Duration** to **15 s**.  
- Test the Zap; you should see a new project appear in InVideo.  
- If you receive “API rate limit exceeded”, pause the Zap and retry after 15 minutes.

**2. Enrich Audio with ElevenLabs**  
Export the final script from Luma (File → Export → Text).  
- In ElevenLabs, paste the script, choose voice **Nova**, set **Speed** to **1.0** and **Pitch** to **0.0**.  
- Click **Generate Audio** → **Download** → select **MP3 320 kbps**.  
- Back in InVideo, go to **Media** → **Upload** → **Audio**, drag the MP3 into the timeline, and align it to the video’s keyframes.  
- If you hear a crackling sound, re‑export at **44.1 kHz** and re‑upload.

**3. Create Branded Thumbnails in Canva**  
Generate a hero image with Midjourney:  
- Prompt: “A sleek, minimalist video thumbnail with bold text, gradient background, 1280×720”.  
- Download the PNG.  
- In Canva, open the **Video Thumbnails** template, drag the Midjourney image into the placeholder, add your brand logo (Upload → Images → Logo), and style the text with your brand typeface.  
- Export as **PNG** (100 % quality).  
- Upload the thumbnail to InVideo’s **Cover Image** field.

**4. Client Onboarding with Calendly + Apollo.io + ActiveCampaign**  
- In Calendly, create a **“Video Production Intake”** event (duration = 30 min), embed the link on your website.  
- Set up a Zap: Calendly trigger → Apollo.io action to “Create Lead” (use the email field).  
- Add another Zap: Apollo.io trigger → ActiveCampaign action to “Add to List” (list ID = “Video Prospects”).  
- In ActiveCampaign, design a welcome series: Email 1 (auto‑send 0 h), Email 2 (sent 24 h later) with a link to your InVideo project gallery.  
- If leads do not appear in Apollo.io, check that the Calendly webhook URL is correct.

**5. Publish and Promote with Hostinger + Shopify + Klaviyo**  
- Host the finished video on Hostinger: upgrade to the **Business Plan** ($3.99/month), upload the MP4 to the **Files** section, and copy the URL.  
- Embed the video in your Shopify product page: go to **Online Store** → **Pages** → “Video Promo” → **Add content** → **Video** → paste the Hostinger URL.  
- Set SEO meta tags: Title “Premium Video Production Service”, Description “High‑quality AI‑edited videos for your brand”.  
- In Klaviyo, create a drip campaign for new subscribers: Email 

Ready to understand the full business opportunity? Read our [opportunity deep-dive]({< ref "/opportunities/how-to-build-an-ai-video-editing-agency-15k-25kmonth.md" >}).


## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
