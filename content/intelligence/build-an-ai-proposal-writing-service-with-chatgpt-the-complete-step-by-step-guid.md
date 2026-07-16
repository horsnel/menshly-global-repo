---
title: "Build an AI Proposal Writing Service with ChatGPT: The Complete Step-by-Step Guide"
date: 2026-07-16
category: "Implementation"
difficulty: "INTERMEDIATE"
readTime: "25 MIN"
excerpt: "In this article you will build a fully operational AI‑powered proposal and grant writing service that can churn out high‑quality documents in minutes, then automatically deliver, track, and optimize t..."
image: "/images/articles/intelligence/write-optimize-and-automate-proposals-and-grants-with-ai-tools.png"
heroImage: "/images/heroes/intelligence/write-optimize-and-automate-proposals-and-grants-with-ai-tools.png"
relatedOpportunity: "/opportunities/how-to-build-an-ai-proposal-writing-agency-8k-12kmonth/"
---

In this article you will build a fully operational AI‑powered proposal and grant writing service that can churn out high‑quality documents in minutes, then automatically deliver, track, and optimize them for your clients. You’ll learn how to harness ChatGPT for drafting, use Make.com to orchestrate data flows, and integrate ElevenLabs for polished voice‑over summaries—all while keeping the entire stack under a $200 monthly budget. This is not a conceptual overview; it’s a hands‑on, step‑by‑step execution guide that will walk you through every click, configuration, and code snippet required to launch a repeatable, scalable service.

The entire build will take roughly 12–15 hours of focused work, spread over a few days, plus an ongoing monthly commitment of about $120 for API usage (ChatGPT, ElevenLabs) and $30 for automation and hosting (Make.com, Hostinger). Once the system is live, you can start onboarding clients and generating proposals at scale, turning a few hours of effort into a recurring revenue stream.

This is the execution guide for the AI Proposal Writing Agency business we outlined in our opportunity deep‑dive.  
Ready to understand the full business opportunity? Read our [opportunity deep‑dive]({< ref "/opportunities/how-to-build-an-ai-proposal-writing-agency-8k-12kmonth.md" >}).

## Prerequisites  

### Accounts, tools, costs, and time required  

- **ChatGPT (OpenAI) – Pro plan**  
  - **Purpose**: Core LLM for drafting, summarizing, and paraphrasing proposals.  
  - **Cost**: $20 / month.  
  - **Free tier**: 5 k tokens/day (insufficient for production).  
  - **Setup time**: 10 min (create account → verify email → upgrade to Pro).

- [**Replit – Hacker plan**](https://replit.com/refer/egwuokwor)  
  - **Purpose**: Cloud IDE for running Python scripts that orchestrate the proposal workflow.  
  - **Cost**: $7 / month (includes 2 GB RAM, 1 CPU).  
  - **Free tier**: 500 MB memory, 1 GB storage.  
  - **Setup time**: 5 min (sign‑up → create new Repl → enable “Always On” for continuous scripts).

- [**Make.com – Starter plan**](https://www.make.com/en/register?pc=menshly)  
  - **Purpose**: Automation platform that stitches together ChatGPT, Replit, and e‑mail services.  
  - **Cost**: $15 / month (200 tasks/month).  
  - **Free tier**: 100 tasks/month.  
  - **Setup time**: 10 min (create account → add “ChatGPT” and “Webhooks” modules).

- [**Vapi – Basic tier**](https://vapi.ai/)  
  - **Purpose**: Voice‑to‑text transcription of stakeholder interviews to feed into the proposal engine.  
  - **Cost**: $0.01 per minute of audio.  
  - **Free tier**: 5 h/month.  
  - **Setup time**: 5 min (API key generation → add to Replit script).

- **Klaviyo (optional)**  
  - **Purpose**: Email marketing for proposal delivery and follow‑ups.  
  - **Cost**: $30 / month (minimum 500 contacts).  
  - **Free tier**: 250 contacts.  
  - **Setup time**: 5 min (API key → integrate via Make.com).

**Total upfront monthly cost**: **$72** (ChatGPT + Replit + Make.com + Klaviyo).  
If you stay on free tiers, the cost drops to $0 but you will need to manually trigger code, limiting throughput.

**Estimated initial setup time**: 35–45 minutes.  

| Tool      | Purpose                                 | Cost      | Free Tier Limit                |
|-----------|-----------------------------------------|-----------|--------------------------------|
| ChatGPT   | Generate & edit proposal text           | $20 / mo  | 5 k tokens/day                 |
| Replit    | Run orchestration scripts               | $7 / mo   | 500 MB memory, 1 GB storage    |
| Make.com  | Automate data flow and notifications    | $15 / mo  | 100 tasks/month                |
| Vapi      | Transcribe stakeholder audio            | $0.01/min | 5 h/month                      |
| Klaviyo   | Email delivery & tracking              | $30 / mo  | 250 contacts                   |

**Note**: All prices are current as of July 2026; verify on the vendor sites before purchasing. These tools will give you a robust, repeatable pipeline for writing, optimizing, and automating proposals and grant applications.

## Step 1: Setup and Configuration  
**Objective** – Create a reproducible, secure development environment that ties together all the AI‑driven services required to generate, optimize, and deliver proposals.  
**Estimated effort** – 20 minutes; each sub‑task will take 10–30 minutes to complete.

---

### 1.1 Create a Replit Workspace  

1. Visit **https://replit.com** and click **Sign up**.  
2. Choose the **Free** plan (500 MB storage, 1 GB RAM).  
3. After authentication, click **+ Create** → **Python** → **Create Repl**.  
4. Rename the Repl to **ai‑proposal-service** (click the pencil icon next to the default name).  

> **Expected UI** – The left pane shows `main.py` and the console pane is empty.  
> **Interactive Check‑in** – Do you see a Repl named **ai‑proposal-service** with a `main.py` file? If not, refresh the page and confirm the Repl’s name.

---

### 1.2 Establish the Directory Skeleton

Open the Replit shell (click the **Shell** button) and run:

```bash
# Navigate to the project root
cd $HOME

# Create directories
mkdir -p ai-proposal-service/src
mkdir -p ai-proposal-service/data
mkdir -p ai-proposal-service/templates
mkdir -p ai-proposal-service/tests

# List structure
tree ai-proposal-service
```

**Expected Output**

```
ai-proposal-service
├── src
├── data
├── templates
└── tests
```

> **Interactive Check‑in** – Do you see the four folders listed above? If the `tree` command is missing, install it with `sudo apt-get install tree -y`.

---

### 1.3 Install Python Dependencies

In the shell, execute:

```bash
cd ai-proposal-service/src
pip install openai python-dotenv
```

**Expected Output**

```
Collecting openai
  Downloading openai-1.0.0-py3-none-any.whl (1.2 MB)
Collecting python-dotenv
  Downloading python_dotenv-1.0.0-py3-none-any.whl (18 kB)
Installing collected packages: openai, python-dotenv
Successfully installed openai-1.0.0 python-dotenv-1.0.0
```

> **Error Scenario** – If you see `ERROR: Could not find a version that satisfies the requirement openai`, the Replit environment is offline. Wait a minute and retry.  
> **Solution** – Run `pip install --upgrade pip` then retry the install.

---

### 1.4 Securely Store the OpenAI API Key

1. In the Replit file explorer, click **+** → **New File** → name it `.env`.  
2. Paste the following line, replacing `<YOUR_OPENAI_KEY>` with your actual key:

   ```
   OPENAI_API_KEY=<YOUR_OPENAI_KEY>


## Step 2: Build the Core System  

In this section we assemble the runtime stack that turns a raw grant brief into a polished, ready‑to‑send proposal. The core system is a three‑tier architecture:

| Tier | Tool | Purpose |
|------|------|---------|
| 1 | **Replit** | Host the Python/Flask API that drives the ChatGPT call |
| 2 | **Make.com** | Trigger the API from a spreadsheet entry and orchestrate post‑processing |
| 3 | **Zapier** | Send the final proposal to the client via email and record the activity in a CRM |

Below you’ll find a step‑by‑step recipe that can be finished in roughly 30 minutes per tier.

---

### 2.1 Deploy the Proposal Engine on Replit  

**1. Create a new Replit project**  
1. Login to Replit (free tier is fine).  
2. Click **+ Create** > **Python (Flask)**.  
3. Name it `proposal-engine`.  

**2. Install dependencies**  
In the Replit shell (`⌃` + `⇧` + `C`), run:  

```bash
pip install openai Flask python-dotenv google-api-python-client
```

**3. Add the OpenAI key**  
1. Click **Secrets** (lock icon).  
2. Add key `OPENAI_API_KEY` and paste your key.  
3. Add key `GOOGLE_APPLICATION_CREDENTIALS` and paste the JSON credentials from a service account that has Drive access.  

**4. Create `app.py`** – this is the core API. Paste:

```python
from flask import Flask, request, jsonify
import openai
import json
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load prompt template
with open("prompt_template.json", "r") as f:
    prompt_template = json.load(f)

# Google Drive service
SCOPES = ["https://www.googleapis.com/auth/drive.file"]
creds = service_account.Credentials.from_service_account_info(
    json.loads(os.getenv("GOOGLE_APPLICATION_CREDENTIALS")),
    scopes=SCOPES
)
drive_service = build("drive", "v3", credentials=creds)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    # Populate template
    prompt = prompt_template["content"].format(**data)
    # Call ChatGPT
    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    proposal_text = completion.choices[0].message.content

    # Save to Drive
    file_metadata = {"name": f"{data['project_name']}_proposal.pdf",
                     "parents": [data.get("drive_folder", "root")]}
    # Convert Markdown to PDF via pandoc (assumes pandoc is pre‑installed)
    with open("proposal.md", "w") as f:
        f.write(f"# {data['project_name']}\n\n{proposal_text}")
    os.system("pandoc proposal.md -o proposal.pdf")
    media = MediaFileUpload("proposal.pdf", mimetype="application/pdf")
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields="id").execute()
    return jsonify({"proposal_id": file.get("id"),
                    "download_url": f"https://drive.google.com/uc?id={file.get('id')}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

**5. Add the prompt template**  
Create `prompt_template.json` with:

```json
{
  "content": "You are a professional grant writer. Write a proposal for the following project:\n\nProject Name: {project_name}\n\nFunding Agency: {agency}\n\nBudget: {budget}\n\nScope: {scope}\n\nDeliverables: {deliverables}\n\nPlease include an executive summary, methodology, timeline, and budget justification."
}
```

**6. Test locally**  
1. Click **Run**.  
2. In the console, hit `curl`:

```bash
curl -X POST https://proposal-engine.up.railway.app/generate \
  -H "Content-Type: application/json" \
  -d '{"project_name":"Water Filter Initiative","agency":"CDC","budget":"$50,000","scope":"Provide clean water for 10 villages","deliverables":"Filter units, training manuals","drive_folder":"YOUR_DRIVE_FOLDER_ID"}'
```

**Check‑in** – Do you see a 200 status and a JSON payload containing `proposal_id`? If no, verify the OpenAI key and that the `prompt_template.json` exists.

---

### 2.2 Orchestrate with Make.com  

**1. Create a new scenario**  
1. Log in to Make.com.  
2. Click **Create a new scenario**.  

**2. Set the trigger**  
1. Search for **Google Sheets** > **Watch Rows**.  
2. Connect your spreadsheet that contains proposal requests.  
3.

## Step 3: Test and Validate  

### 3.1 Run a Dry‑Run Proposal Pipeline  

1. **Create a dummy grant brief**  
   - In [**Notion**](https://notion.so/), open the “Grant Briefs” database.  
   - Press **Ctrl + N** (Windows) or **Cmd + N** (Mac) to add a new page.  
   - Title it **“Test – Climate Action Fund”**.  
   - Add the following properties:  
     - **Funding Body**: “Climate Action Fund” (select from the dropdown).  
     - **Budget**: “$50,000”.  
     - **Deadline**: “2026‑09‑30”.  
     - **Key Requirements**: type “1. Demonstrate measurable impact. 2. Provide a sustainability plan.”  
   - Click **Save**.

2. **Trigger the Make.com automation**  
   - Open **Make.com** → **Scenarios** → click the scenario you created for “Grant Draft”.  
   - Press **Run once**.  
   - In the log panel, confirm the following sequence:  
     1. **Trigger** – “Database Item Added” → “Notion – New Page”.  
     2. **Filter** – “Check Deadline > Today”.  
     3. **Text Generation** – “ChatGPT – Send a prompt”.  
     4. **Write to Notion** – “Update Page – Add Draft Section”.  

   If any module shows **Error**:  
   - **Error**: *“Invalid authentication”* → Re‑authenticate your Notion token in the Make.com module settings.  
   - **Error**: *“Rate limit exceeded”* → Wait 30 s and rerun; check your ChatGPT pricing plan (you need at least the *“ChatGPT‑Plus”* tier for 30 k tokens/day).  

3. **Verify ChatGPT output**  
   - Open the **ChatGPT** Web UI (https://chat.openai.com).  
   - Paste the following prompt:  
     ```
     Draft a 250‑word grant proposal for the Climate Action Fund. Use the brief:
     • Funding Body: Climate Action Fund
     • Budget: $50,000
     • Deadline: 2026‑09‑30
     • Key Requirements: 1. Demonstrate measurable impact. 2. Provide a sustainability plan.
     ```
   - Copy the response.  
   - Compare the **first paragraph** with the draft saved in Notion.  
     - Expected output starts with “**Executive Summary**” and contains the key metrics.  
     - If the paragraph does not match, adjust the prompt in the Make.com “ChatGPT – Send a prompt” module to include “Use the structure: Executive Summary, Impact Metrics, Sustainability Plan, Budget Breakdown.”  

### 3.2 Checkpoint: 5‑Point Validation Checklist  

| # | Item | How to Verify | Expected Result |
|---|------|---------------|-----------------|
| 1 | **Trigger firing** | In Make.com log, ensure the “Notion – New Page” trigger fires. | Yes, timestamped. |
| 2 | **Prompt formatting** | In the ChatGPT module, inspect the “Prompt” field; it should contain the JSON schema with “brief” and “structure”. | Prompt shows key requirements. |
| 3 | **Response length** | In Notion, the “Draft” section’s text length ≈ 250 words. | 240‑260 words. |
| 4 | **Token usage** | In OpenAI dashboard → *Usage* → *Chat Completions* → check tokens ≈ 400. | ≤ 450 tokens. |
| 5 | **Error handling** | No “Error” state in any module; the scenario status shows “Finished”. | Status = Finished. |

### 3.3 Common Error Scenarios & Fixes  

- **Error**: *“Missing required field: brief”*  
  - **Cause**: The Notion property “Key Requirements” is empty or mis‑named.  
  - **Fix**: Ensure the property name matches exactly; rebuild the filter in Make.com to pass `brief` as a JSON object.  

- **Error**: *“Exceeded token limit (4096)”*  
  - **Cause**: The prompt includes unnecessary “debug” text.  
  - **Fix**: Trim the prompt to the essential fields; use the `max_tokens` setting in the ChatGPT module to 800.  

- **Error**: *“Connection refused to Replit”*  
  - **Cause**: Replit app‑token expired.  
  - **Fix**: Generate a new API key in Replit → *Account* → *Create New Token*; update the Make.com “Webhooks by Replit” module.  

By following this test and validation sequence, you confirm that the AI‑driven proposal pipeline produces accurate, compliant drafts and that the automation chain is robust before scaling to live client work.

## Step 4: Add Advanced Features  
*(Build a production‑ready, AI‑enriched, error‑resilient, and auto‑routed proposal engine)*  

1. **Add AI Enrichment Layer**  
   1.1. Open the **Replit** workspace created in Step 2.  
   1.2. Create a new Python file `enrich.py`.  
   1.3. Install the `openai` and `pandas` packages via the Replit shell:  
   ```
   pip install openai pandas
   ```  
   1.4. In `enrich.py`, paste the following code:
   ```python
   import openai
   import pandas as pd
   import os

   openai.api_key = os.getenv("OPENAI_API_KEY")
   MODEL = "gpt-4o-mini"

   def enrich_proposal(text: str) -> str:
       """
       Sends the proposal draft to ChatGPT for a second pass of polish,
       style consistency, and keyword optimization for grant agencies.
       """
       response = openai.ChatCompletion.create(
           model=MODEL,
           temperature=0.2,
           max_tokens=1500,
           messages=[
               {"role": "system", "content": "You are a senior grant writer."},
               {"role": "user", "content": text}
           ]
       )
       return response.choices[0].message.content.strip()
   ```
   1.5. **Interactive Check‑In**: After saving `enrich.py`, run the file in Replit.  
   ```
   python enrich.py
   ```  
   You should see a **JSON** block with the enriched text.  
   If you get `UNAUTHORIZED`, the API key is wrong; update the Replit secret `OPENAI_API_KEY` under `Secrets (Environment Variables)`.

2. **Error Handling & Logging**  
   2.1. In the main `app.py` (or `main.py`), import `logging` and `enrich_proposal`.  
   ```python
   import logging
   from enrich import enrich_proposal

   logging.basicConfig(
       level=logging.INFO,
       format="%(asctime)s [%(levelname)s] %(message)s",
       handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
   )
   ```
   2.2. Wrap every external call in `try/except` blocks. Example for the OpenAI call:
   ```python
   try:
       enriched = enrich_proposal(raw_text)
   except openai.error.OpenAIError as e:
       logging.error(f"OpenAI error: {e}")
       enriched = raw_text  # fallback to original
   ```
   2.3. **Interactive Check‑In**: Submit a test proposal via the API endpoint. Open `app.log` in Replit; you should see an `INFO` line “Proposal enriched successfully” or an `ERROR` if the call fails.

3. **Routing & Workflow Automation with Make.com**  
   3.1. Log into **Make.com**. Create a new Scenario named “Proposal‑to‑CRM‑Flow”.  
   3.2. Set the **Trigger** to “Webhooks > Custom Webhook” and copy the generated URL.  
   3.3. In Replit, expose the Flask endpoint `/webhook` to receive the webhook payload.  
   ```python
   from flask import Flask, request, jsonify
   app = Flask(__name__)

   @app.route("/webhook", methods=["POST"])
   def webhook():
       data = request.json
       # Pass data to enrichment
       enriched = enrich_proposal(data["draft"])
       # Store in buffer (for demo)
       with open("buffer.txt", "a") as f:
           f.write(enriched + "\n---\n")
       # Forward to CRM
       forward_to_kraviyo(enriched)
       return jsonify({"status": "received"}), 200
   ```
   3.4. Back in Make.com, add an **Action**: “Klaviyo > Add/Update Contact”. Map the JSON fields:  
   ```
   email = {{Webhook_Data.email}}
   name = {{Webhook_Data.name}}
   proposal = {{Webhook_Data.enriched}}
   ```
   3.5. **Interactive Check‑In**: Trigger the webhook via Postman with a sample JSON payload. In Make.com, you should see the “Klaviyo” action executed and a success status.  
   3.6. If Make.com returns “Invalid authentication,” verify the Klaviyo API key in the Make.com “Klaviyo” module settings.

4. **Voice‑to‑Text / Text‑to‑Voice Integration (Optional Advanced Feature)**  
   4.1. In Replit, create `voice.py`. Install `vapi` and `elevenlabs`:
   ```
   pip install vapi elevenlabs
   ```
   4.2. Add the following snippet:
   ```python
   from vapi import VapiClient
   from elevenlabs import generate, play

   VAPI_KEY = os.getenv("VAPI_KEY")
   ELEVENLABS_KEY = os.getenv("ELEVENLABS_KEY")

   def synthesize_proposal(text: str) -> str:
       client = VapiClient(VAPI_KEY)
       # Transcribe user audio (if needed) – Example only
       # audio_file = client.transcribe("audio.wav")

       # Generate voice
       audio = generate(
          

## Step 5: Deploy to Production

Below is a concrete, end‑to‑end deployment flow that moves the proposal‑generation API from a local Replit instance to a fully‑managed production environment on Hostinger Cloud.  The process uses Docker for reproducibility, Make.com for post‑deployment webhook notifications, and Zapier to push new proposals to a Klaviyo mailing list.  All commands are terminal‑level and can be copied verbatim.

### 5.1 Prepare the Docker Image

1. **Create a `Dockerfile`** in the root of your Replit repo.  
   ```dockerfile
   FROM python:3.10-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   COPY . .
   ENV PYTHONDONTWRITEBYTECODE=1
   ENV PYTHONUNBUFFERED=1
   CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
   ```
   *Do you see the `Dockerfile` in the file list?*  
   *If not, create it via the Replit editor’s “+ File” button.*

2. **Build the image locally** to catch syntax errors.  
   ```bash
   docker build -t proposal-api .
   ```
   Expected output: `Successfully built <hash>` and `Successfully tagged proposal-api:latest`.  
   *If you see `ERROR: Failed to build`… check that the `requirements.txt` contains `Flask==2.3.2` and `openai==0.27.2`.*

3. **Push the image to Docker Hub** (or Hostinger’s registry).  
   ```bash
   docker login
   docker tag proposal-api yourdockerhub/proposal-api:latest
   docker push yourdockerhub/proposal-api:latest
   ```

### 5.2 Provision a Hostinger Cloud Server

1. Log into Hostinger, select **Cloud Hosting → New Server**.  
2. Pick the **Starter Plan** (USD 5.95/month, 1 GB RAM, 1 vCPU).  
3. In the **Server Settings** panel, enable *Docker* support.  
4. Click **Create Server**.  
   *You should see a status “Creating…” → then “Running”.*  
   *If the status stays “Failed”, verify that the server has at least 1 GB RAM.*

5. In the **Server Dashboard → Docker** tab, click **Deploy Image**.  
6. Enter the image URL `yourdockerhub/proposal-api:latest`.  
7. Set the **Container Port** to `8000` and the **Internal Port** to `80`.  
8. Click **Deploy**.  
   *You should see “Container started” and the container ID.*

### 5.3 Configure Environment Variables

1. In the same Docker tab, click **Environment Variables** → **Add Variable**.  
2. Add the following keys and values:
   ```
   OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   DATABASE_URL=postgres://user:pass@db:5432/proposals
   ```
   Replace the placeholders with your actual secrets.  
3. Save.  
   *Check that the variables appear in the list.*

### 5.4 Expose the Domain

1. In the Hostinger dashboard, go to **Domains → Add Domain**.  
2. Point `proposal.menshly.ai` (or your own domain) to the server’s public IP.  
3. In **DNS Settings**, create an `A` record for `proposal` pointing to the IP.  
4. Enable **Let’s Encrypt SSL** (free).  
5. Wait 5–10 minutes for propagation.  

### 5.5 Verify the API

1. Open a browser and navigate to `https://proposal.menshly.ai/api/health`.  
2. Expected JSON:
   ```json
   { "status": "ok", "uptime": "12:34:56" }
   ```
3. If you receive `404` or `500`, double‑check the Docker port mapping and that the Gunicorn command is correct.

### 5.6 Post‑Deployment Automation

1. **Make.com**:  
   - Create a new scenario → trigger “HTTP Request” → URL `https://proposal.menshly.ai/api/webhook`.  
   - Add an action “Send Email” via Gmail to notify the dev team.  
2. **Zapier**:  
   - Trigger “Webhooks by Zapier” → Catch Hook → URL `https://proposal.menshly.ai/api/webhook`.  
   - Action “Create Subscriber” in Klaviyo → map proposal author email.

### 5.7 Monitoring & Scaling

- Hostinger provides a **Metrics** tab. Verify CPU < 30 % and memory < 700 MB.  
- If traffic spikes, upgrade to the **Growth Plan** (USD 11.95/month, 2 GB RAM).  
- Enable **Auto‑Scale** under **Server Settings** → *Auto‑Scale* → “On”.

### 5.8 Rollback Plan

1. In Docker tab, click **Stop Container**.  
2. Delete the failing image.  
3. Deploy the previous stable tag (`proposal-api:v1.2.3`).  
4. Confirm the health endpoint again.

With these steps, your AI‑powered proposal generator is live, secure, and ready for production traffic.  The process is repeatable:

## Step 6: Scale and Grow  

Below is a practical playbook that moves your solo AI‑proposal service from a single client to 10 + clients, while tightening margins and automating repetitive tasks. Follow the checklist, hit the checkpoints, and watch your revenue scale.

---

### 1. Build a Mini‑Team  

| Role | Hiring Channel | Salary (USD) | Tool for Onboarding |
|------|----------------|--------------|---------------------|
| Proposal Editor | LinkedIn / Apollo.io | $45 k | Notion template + Loom demo |
| Voice‑over Specialist | Upwork | $35 k | ElevenLabs API key |
| Automation Engineer | GitHub Jobs | $60 k | Replit “Hacker” plan ($7/mo) |

**Checklist**  
- Do you have a LinkedIn Recruiter account? → *If not, subscribe to the free trial.*  
- Open `Apollo.io`, search “proposal writer” and add 30 prospects to the “Hiring” list.  
- Create a Notion “Onboarding” database with pages: *Welcome*, *Project Brief*, *Voice‑over Guide*.  

---

### 2. Automate Client Intake  

1. **Calendly → Make.com → ActiveCampaign**  
   - In Calendly, go to *Booking Pages* → *Add integration* → *Make.com* (API key).  
   - In Make.com, create a new scenario:  
     - **Trigger**: *Calendly – New Event*.  
     - **Action 1**: *Create Notion Page* (`Database ID: 123‑abc`).  
     - **Action 2**: *Add Subscriber to ActiveCampaign* (`List ID: 42`).  
   - Test: Schedule a dummy meeting, confirm a new Notion page appears.  

2. **Error check**  
   - If you see “HTTP 403 – Forbidden”, verify the Make.com API key has “Calendly” permissions.  
   - If ActiveCampaign fails, re‑check the List ID and API credentials.  

---

### 3. Batch‑Process Proposals on Replit  

- Fork the GitHub repo `ai-proposal-batch` into Replit.  
- In `main.py`:  
  ```python
  import openai, json, os
  openai.api_key = os.getenv("OPENAI_API_KEY")
  def generate_proposal(prompt):
      return openai.ChatCompletion.create(
          model="gpt-4o-mini",
          temperature=0.7,
          max_tokens=2000,
          messages=[{"role":"user","content":prompt}]
      )
  ```
- Set Replit env variable `OPENAI_API_KEY = <your key>`.  
- Run the script; it will output 10 proposals as JSON files.  
- **Tip**: Turn on *Auto‑deploy* so every push triggers a fresh job.  

---

### 4. Add Voice & Video Enhancements  

| Tool | Configuration | Purpose |
|------|---------------|---------|
| **Vapi** | `api_key = "YOUR_VAPI_KEY"`; `endpoint = "https://api.vapi.ai/v1/voice/summary"` | Summarize proposal in 60 s voice clip |
| [**ElevenLabs**](https://elevenlabs.io/) | `voice_id = "Rachel"`; `api_key = "YOUR_ELEVEN_KEY"` | Convert summary to high‑quality MP3 |
| [**Fliki AI**](https://fliki.ai?referral=noah-wilson-w84be4) | `video_template = "Professional Pitch"`; `text = proposal_text` | Generate 2‑minute explainer video |

**Interactive Check‑in**  
- After generating the MP3, play it in your browser. You should hear a clear female voice.  
- If the MP3 is garbled, ensure `voice_id` is correctly spelled and the key is active.  

---

### 5. Tighten Margins  

1. **Cost Tracking**  
   - Use the OpenAI cost calculator: `tokens / 1000 * $0.03` for GPT‑4o-mini.  
   - Store cost in a Google Sheet via Make.com’s *Google Sheets* action.  

2. **Subscription Billing**  
   - Integrate Stripe with Zapier: *New Stripe Invoice* → *Send to Klaviyo* → *Trigger Email Nurture*.  
   - Set up a recurring plan of $199/month for “Pro‑Bundle” (proposal + audio/video).  

3. **Revenue Projection**  
   - 10 clients × $199 = $1,990/month.  
   - Subtract: OpenAI ($200), Stripe fee (2.9 % + 30¢ × 10), Replit ($7), others ($50) = $400.  
   - **Net** ≈ $1,590 → 80 % margin.  

---

### 6. Scale Outreach with [Semrush](https://www.semrush.com/) & Canva  

- Run a Semrush “Keyword Gap” report for “grant writing services” → export top 20 keywords

## Cost Breakdown

| Item | Free Tier | Paid Tier | When to Upgrade |
|------|-----------|-----------|-----------------|
| **ChatGPT (OpenAI API)** | 100 k tokens/month (GPT‑4 Turbo) | $0.01 per 1 k tokens (GPT‑4 Turbo) | Once you exceed 70 k tokens or need higher concurrency |
| **Make.com** | 500 operations/month | $25/month (25 k operations) | When automating > 200 proposals per month |
| **Replit** | Unlimited projects, 512 MiB RAM | $7/month (Hacker) | When you hit > 2 GB RAM usage or need private repos |
| **Vapi** | 10 calls/day | $19/month (1 000 calls) | If you generate > 30 calls/day |
| **ElevenLabs** | 5 min audio/day | $20/month (1 000 min) | For > 15 min of synthesized voice per day |
| [**Canva**](https://www.canva.com/) | 5 templates/month | $12/month (Pro) | When you need > 20 custom graphics per proposal |
| **Zapier** | 100 tasks/month | $19/month (3 k tasks) | When automating > 500 tasks/month |
| **Klaviyo** | 500 contacts | $30/month (5 k contacts) | If you surpass 500 contacts or need advanced segmentation |
| **Hostinger** | 3 GB SSD, 1 GB RAM | $3.99/month (Basic) | When traffic > 50 k visits/month |
| **Shopify** | 14‑day free trial | $29/month (Basic) | If you need a storefront for paid services |

### Monthly Cost Analysis

| Scale | ChatGPT | Make.com | Replit | Vapi | ElevenLabs | Canva | Zapier | Klaviyo | Hostinger | Shopify | **Total** |
|-------|---------|----------|--------|------|------------|-------|--------|---------|-----------|---------|-----------|
| **Solo** (1 client, 2 proposals/mo) | $0.50 | $0 | $0 | $0 | $0 | $0 | $0 | $0 | $3.99 | $0 | **$4.49** |
| **5 Clients** (10 proposals/mo, 5% churn) | $5 | $25 | $0 | $19 | $20 | $12 | $19 | $30 | $3.99 | $29 | **$167.99** |
| **10+ Clients** (30 proposals/mo, 10% churn) | $15 | $25 | $7 | $19 | $20 | $12 | $19 | $30 | $3.99 | $29 | **$200.99** |

**Explanation of the numbers**

1. **ChatGPT** – 2 k tokens per proposal × 30 proposals = 60 k tokens → $0.60 (rounded to $0.50 for the solo case).
2. **Make.com** – 200 operations/month (30 proposals × 6 steps) → $25 when > 200 operations.
3. **Replit** – All development stays in the free tier; only the paid Hacker plan is needed if CPU usage > 2 GB RAM.
4. **Vapi** – 10 calls/day × 30 days = 300 calls → $19/month.
5. **ElevenLabs** – 15 min of voice per proposal × 30 = 450 min → $20/month.
6. **Canva** – 1 graphic per proposal → 30 graphics → Pro plan $12/month.
7. **Zapier** – 300 tasks/month → $19/month.
8. **Klaviyo** – 1,000 contacts (5 clients × 200 contacts each) → $

## Production Checklist

Before you open the service to clients, run through the following items. Check each box only when the condition is met.

- **[ ] API Key Validation** – In Replit, ensure the environment variable `OPENAI_API_KEY` equals the key shown in your OpenAI dashboard. Run `print(os.getenv("OPENAI_API_KEY"))`; it should output a 32‑character string. If it outputs `None`, the key is missing.  
- **[ ] Make.com Trigger Test** – In Make.com, open the “Proposal Builder” scenario, click “Run once.” The log should show a success status (200) and a JSON object containing `proposal_id`. Any 4xx/5xx indicates a connectivity issue.  
- **[ ] Zapier Email Workflow** – In Zapier, trigger the “Send Proposal PDF” Zap manually. The test email must reach the inbox within 30 seconds and contain the PDF attachment. If you see “No email sent,” verify the SMTP credentials in the Zap.  
- **[ ] PDF Generation Accuracy** – Generate 3 test proposals. Open each PDF and confirm that the title, client name, and deadline match the input data. Missing fields mean the template rendering in Replit failed.  
- **[ ] Voice Output Check** – Use ElevenLabs to synthesize the proposal summary. In the ElevenLabs UI, click “Generate” and confirm the audio file downloads without error.  
- **[ ] Rate‑Limit Monitoring** – In the Replit console, run `curl https://api.openai.com/v1/engines` with your key. The response header `x-ratelimit-remaining` must be >0. If it’s 0, you need to upgrade your plan.  
- **[ ] Billing & Usage Logs** – Check the OpenAI billing dashboard. Daily usage should not exceed the “Standard” tier quota. If it does, adjust the prompt length in `prompt_builder.py`.  
- **[ ] Security Hardening** – Verify that the Replit app is set to “private” and that the `RESTRICTED_IPS` variable contains the IPs of your internal network.  
- **[ ] SEO & SEO Metadata** – In the static site generator, confirm that each proposal page includes `<meta name="description">` with the first 160 characters of the summary.  
- **[ ] Backup & Rollback Plan** – Export the current Replit project snapshot. Store it in a separate branch named `prod_backup`. If a rollback is needed, run `git checkout prod_backup`.  

Complete all items before toggling the “Live” switch. Happy deploying!

## What to Do Next

**1. Hook ChatGPT into a Client Intake Form with Make.com**  
1. Log into Make.com and click **Create a new scenario**.  
2. Drag a **Webhook > Custom Webhook** trigger onto the canvas and click **Add**.  
3. Copy the generated URL (e.g., `https://hook.make.com/abc123`).  
4. In your client‑facing form (Google Forms or Typeform), add a **Submit** button that POSTs to the URL.  
5. In Make.com, add an **OpenAI > Generate** action.  
   * **Model**: `gpt-4o-mini`  
   * **Prompt**:  
     ```
     Generate a 1000‑word grant proposal outline for a nonprofit seeking $50k for community outreach.  
     Use the following client data: {webhook_request.body}.  
     Output in markdown.
     ```  
6. Add a **Google Docs > Create a Document** action to save the output.  
   * **Title**: `Proposal – {{webhook_request.body.name}} – {{current_date}}`  
   * **Content**: `{{openai_generate.output}}`  
7. Finish the scenario and turn it **ON**.  
Do you see the “Scenario running” status? If the scenario fails with “Error: Invalid API key”, verify your OpenAI API key in the **Tools** tab of Make.com.

**2. Automate Proposal Tracking in Notion via Zapier**  
1. Open Zapier and create a new Zap.  
2. Trigger: **Notion > New Database Item** (select the “Proposals” database).  
3. Action: **Email by Gmail > Send Email**.  
   * **To**: `{{trigger.email}}`  
   * **Subject**: “Your proposal draft is ready”  
   * **Body**: “Hi {{trigger.name}}, your draft is available at {{trigger.google_docs_url}}.”  
4. Add a second action: **Notion > Update Database Item**.  
   * **Status**: `Draft Sent`  
   * **Timestamp**: `{{zap_meta_timestamp}}`  
Check that the status field changes to “Draft Sent” after the Zap runs. If you see “No matching triggers”, ensure the database has the required properties (Name, Email, Google Docs URL).

**3. Turn Proposals into Video Summaries with Fliki AI**  
1. In Fliki AI, create a new project and select **Text to Video**.  
2. Paste the Markdown output from Step 1 into the text box.  
3. Choose the “Professional” voice (price: $0.04/second) and set **Video Quality** to **1080p**.  
4. Click **Generate**.  
5. Download the video and upload it to the Google Doc you created earlier (use the **Insert > Video** menu).  
You should see the video embedded at the top of the document. If the video fails to load, check that the file size is under 500 MB—Fliki AI limits larger uploads.

**4. Automate Follow‑Ups with Klaviyo**  
1. In Klaviyo, create a new flow titled “Proposal Follow‑Up”.  
2. Trigger: **Email > Email Opened** (segment: “Proposal Recipients”).  
3. Action: **Email > Send Email** (template: “Thank you for opening the proposal”).  
   * **Subject**: “Any questions about your proposal?”  
   * **Body**: “Hello {{first_name}}, let’s discuss next steps.”  
4. Add a conditional split: if the email is not opened within 72 h, send a reminder.  
5. Enable the flow and monitor the analytics dashboard.  
If you see “No recipients found”, verify that the email address is present in the “Email” property of the Notion database.

**5. Expand to Multi‑Lingual Proposals with Replit and GPT‑4**  
1. Spin up a Replit workspace (`python` template).  
2. Install the `openai` library (`pip install openai`).  
3. Create a script that calls `openai.ChatCompletion.create` with `model="gpt-4o"` and `temperature=0.7`.  
4. Add a prompt that includes a translation step:  
   ```
   Translate the following proposal into Spanish: {{proposal_text}}
   ```  
5. Save the translated output to a new Markdown file and push it to GitHub.  
6. Set up a GitHub Action that triggers on new commits to the `translations` branch, automatically generating a PDF via `pandoc` (`pandoc -s -o proposal.pdf proposal.md`).  
If the script throws `openai.error.AuthenticationError`, double‑check that the `OPENAI_API_KEY` environment variable is set correctly in Replit’s “Secrets” tab.

Ready to understand the full business opportunity? Read our [opportunity deep-dive]({< ref "/opportunities/how-to-build-an-ai-proposal-writing-agency-8k-12kmonth.md" >}).


## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Notion](https://notion.so/)** — All-in-one workspace — notes, docs, project management
- **[Grammarly](https://grammarly.com/)** — AI writing assistant — grammar, tone, clarity
- **[Canva](https://www.canva.com/)** — Design anything — social graphics, presentations, videos with AI
