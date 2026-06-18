---
title: "Build an AI HR Recruitment Automation Service with ChatGPT: The Complete Step-by-Step Guide"
date: 2026-06-18
category: "Implementation"
difficulty: "ADVANCED"
readTime: "25 MIN"
excerpt: "This guide will walk you through building a fully automated HR and recruitment service that leverages ChatGPT, Make.com, and Vapi to screen candidates, schedule interviews, and generate personalized o..."
image: "/images/articles/intelligence/automate-optimize-and-analyze-hr-and-recruitment-tasks-with-ai-tools.png"
heroImage: "/images/heroes/intelligence/automate-optimize-and-analyze-hr-and-recruitment-tasks-with-ai-tools.png"
relatedOpportunity: "/opportunities/how-to-build-an-ai-hr-recruitment-automation-10k-20kmonth/"
---

This guide will walk you through building a fully automated HR and recruitment service that leverages ChatGPT, Make.com, and Vapi to screen candidates, schedule interviews, and generate personalized onboarding content. By the end, you’ll have a production‑ready pipeline that reduces manual hiring hours by 70%, improves candidate experience, and produces detailed analytics for hiring managers.  

Unlike a conceptual blog, this is a hands‑on execution manual. Every step lists the exact UI clicks, API calls, and configuration files you must create. You’ll copy‑paste JSON payloads, set Make.com workflow triggers, and deploy Replit notebooks—all with precise details so you can hit production without guessing.  

The entire build takes roughly 90 hours of focused work and costs about $2,500: $1,200 for a Replit pro plan, $900 for Make.com premium, $400 for a Vapi subscription, and $500 for ancillary services (e.g., a 30‑minute slack bot integration). This is the execution guide for the AI HR Recruitment Automation business we outlined in our opportunity deep‑dive.  

Ready to understand the full business opportunity? Read our [opportunity deep‑dive](/opportunities/how-to-build-an-ai-hr-recruitment-automation-10k-20kmonth.md).

## Prerequisites

**Prerequisites**  
Before you dive into building the AI‑powered HR recruitment automation service, you must prepare a set of accounts, tools, and infrastructure. The steps below outline the exact resources you’ll need, the cost of each, and the time commitment to get everything up and running.

- **OpenAI ChatGPT API** – Create an API key in the OpenAI dashboard.  
  - *Plan*: Pay‑as‑you‑go (GPT‑4 8k)  
  - *Estimated monthly cost*: $20.00 at 500 k tokens/ month  
  - *Free tier*: 100 k tokens/month

- **Zapier** – Automate data flow (e.g., candidate data → Airtable → email).  
  - *Plan*: Starter ($19.99/month) – 5 “Zaps”, 100 tasks each month  
  - *Free tier*: 5 Zaps, 100 tasks/month

- [**Replit**](https://replit.com/refer/egwuokwor) – Host the micro‑service that will call the ChatGPT API.  
  - *Plan*: Hacker ($7.00/month) – 1GB RAM, unlimited private repos  
  - *Free tier*: 500 MB RAM, 60 min per day

- [**Notion**](https://notion.so/) – Document the workflow, store candidate logs, and prototype UI mockups.  
  - *Plan*: Personal Pro ($8.00/month) – 1,000 integrations, unlimited blocks  
  - *Free tier*: 1,000 blocks, 5 integrations

- **Apollo.io** – Retrieve B2B contact data for targeted sourcing.  
  - *Plan*: Growth ($99.00/month) – 5,000 contacts, 50,000 credits  
  - *Free tier*: 100 contacts, 200 credits

- **Hostinger** – Domain and web‑hosting for static assets (landing page, onboarding).  
  - *Plan*: Personal Shared Hosting ($3.95/month) – 1 GB SSD, 1 domain  
  - *Free tier*: 1 GB SSD, 1 domain (basic hosting)

- **Calendly** – Schedule interviews with candidates.  
  - *Plan*: Professional ($15.00/month) – 1 calendar, 2 event types  
  - *Free tier*: 1 calendar, 1 event type

**Estimated Upfront Cost**  
All monthly subscriptions total **$167.94**. No additional one‑time fees are required unless you upgrade plans later.

| Tool        | Purpose                                   | Cost (Monthly) | Free Tier Limit                 |
|-------------|-------------------------------------------|----------------|---------------------------------|
| ChatGPT API | Candidate screening, response generation  | $20.00         | 100 k tokens                    |
| Zapier      | Automation between services               | $19.99         | 5 Zaps, 100 tasks               |
| Replit      | Host API wrapper, webhooks                | $7.00          | 500 MB RAM, 60 min/day          |
| Notion      | Documentation & prototype design          | $8.00          | 1,000 blocks, 5 integrations   |
| Apollo

## Step 1 – Setup and Configuration  
*(Estimated time: 20–30 minutes)*  

In this first step you will (1) create the development environment, (2) set up the repository structure, (3) register for the key AI and automation services, and (4) store the secrets in a secure, version‑controlled manner.  
All commands are written for a Unix‑style shell (Linux or macOS). If you’re on Windows, use the Git‑Bash terminal or WSL.  

---

### 1. Create the Project Workspace on Replit  

1.1. Open <https://replit.com> and sign in (or create an account).  
1.2. Click **+ Create** → **New Repl**.  
1.3. Choose **Node.js** as the template.  
1.4. Name the Repl `ai-hr-recruitment`.  
1.5. Click **Create Repl**.  

**Expected UI**  
- You should see the Replit IDE with a left pane (file tree), an editor pane, and a bottom terminal pane.  
- The terminal should automatically run `npm install` for the default `package.json`.  

**Interactive Check‑in**  
> Do you see a file called `index.js` in the file tree?  
> If not, refresh the page and make sure the Repl was created with the Node.js template.  

**Error scenario**  
> *If the terminal shows `npm ERR!`, it usually means the network is blocked.*  
> **Fix**: In the Replit menu, go to **Settings → Proxies** and enable a proxy, or switch to a different network.

---

### 2. Initialize a Git Repository & Create a Directory Skeleton  

2.1. In the Replit terminal, run:  
```bash
git init
```

2.2. Create the following folders:  
```bash
mkdir -p src/{controllers,models,routes,utils}
mkdir -p config public tests
```

2.3. Create a `.gitignore` file with common Node.js exclusions:  
```bash
cat > .gitignore <<'EOF'
node_modules/
.env
*.log
EOF
```

2.4. Commit the initial structure:  
```bash
git add .
git commit -m "Initial repo skeleton"
```

**Expected Terminal Output**  
```
[master (root-commit) 6f3d2a9] Initial repo skeleton
 7 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 .gitignore
 create mode 100644 src/controllers/
 create mode 100644 src/models/
 create mode 100644 src/routes/
 create mode 100644 src/utils/
 create mode 100644 config/
 create mode 100644 public/
 create mode 100644 tests/
```

**Interactive Check‑in**  
> Do you see the folder tree exactly as shown above?  
> If any folder is missing, run the `mkdir` command again.

---

### 3. Register for Essential API Services  

| Tool | Purpose | Registration Steps | Key Settings |
|------|---------|---------------------|--------------|
| **ChatGPT (OpenAI)** | Language model for resume parsing and candidate messaging | 1. Go to <https://platform.openai.com/account/api-keys> 2. Click **Create new secret key** | Name: `OPENAI_API_KEY` |
| **Apollo.io** | B2B contact database for sourcing candidates | 1. Sign up at <https://app.apollo.io> 2. In the dashboard, go to **API** → **Create API key** | Name: `APOLLO_API_KEY` |
| [**Make.com**](https://www.make.com/en/register?pc=menshly) | Automation platform to connect ChatGPT, Apollo, and email workflows | 1. Create an account <https://www.make.com> 2. In the dashboard, navigate to **Integrations** → **Add new integration** → **OpenAI** and **Apollo.io** | No key needed here, but you’ll use the platform’s connector |
| **Hostinger** | Hosting for the final deployed service | 1. Sign up at <https://www.hostinger.com> 2. Purchase a shared plan (starts at $2.99/month) 3. In the control panel, set up a **Node.js** application (Node 18 LTS) | Domain: `hr-recruit.ai` (example) |

> **TIP**: Keep a printed or PDF copy of each key in a secure location (e.g., a password manager like 1Password).

---

### 4. Store API Keys in a `.env` File  

4.1. Create a file named `.env` in the project root:  

```bash
cat > .env <<'EOF'
OPENAI_API_KEY="your-openai-key-here"
APOLLO_API_KEY="your-apollo-key-here"
EOF
```

4.2. Ensure `.gitignore` already excludes `.env`.  
4.3. Install the `dotenv` package to load these variables:  

```bash
npm install dotenv
```

4.4. In `src/utils/config.js`,

## Step 2 – Build the Core System  
*(Estimated time: 2 hrs 30 min)*  

In this section we assemble the runtime engine that will accept resumes, run them through ChatGPT, and route the results to downstream automation tools (Make.com, Zapier, Vapi). All code will live in a Replit workspace so that the service is instantly deployable and version‑controlled. The architecture is a single Express server exposing a `/resume` POST endpoint; the handler calls the OpenAI API, then fires a Make.com webhook, a Zapier webhook, and a Vapi voice call.

> **NOTE** – All credentials are stored in Replit’s `.env` file. Never commit this file to GitHub.

---

### 2.1 Create the Replit Project

1. Log into Replit (free tier is sufficient).  
2. Click **+ Create** > **New Repl**.  
3. **Language**: `Node.js (JavaScript)`  
4. **Name**: `hr-recruitment-ai`  
5. Click **Create Repl**.  

**Check‑in**  
Do you see a terminal at the bottom of the screen with a prompt `> node`? You should see a file tree with `index.js`, `package.json`, and a blank `README.md`.

> **Error** – If the terminal shows “Cannot find Node.js”, confirm the Node.js version in the sidebar under **Packages** > **Node.js** and ensure it is at least **14.17.0**.

---

### 2.2 Install Dependencies

Open the **Packages** sidebar, search for each of the following, and click **+ Add**:

| Package | Purpose |
|---------|---------|
| express | Web framework |
| dotenv | Load env vars |
| openai | Official OpenAI SDK |
| axios | HTTP client for Make.com & Zapier |
| body-parser | Parse JSON payloads |

Alternatively, run in the terminal:

```bash
npm install express dotenv openai axios body-parser
```

**Check‑in**  
Your `package.json` should now list the four dependencies under `"dependencies"`. Do you see `"express": "^4.18.2"` and `"openai": "^3.2.1"`?

---

### 2.3 Configure Environment Variables

Click **Secrets** in the left sidebar. Add the following keys:

| Key | Value | Description |
|-----|-------|-------------|
| `OPENAI_API_KEY` | *Your OpenAI key* | Used by the OpenAI SDK |
| `MAKESCOM_WEBHOOK_URL` | *URL from Make.com scenario* | Triggers Make.com workflow |
| `ZAPIER_WEBHOOK_URL` | *URL from Zapier webhook* | Triggers Zapier actions |
| `VAPI_API_KEY` | *Your Vapi key* | Authenticate Vapi voice API |
| `VAPI_SENDER_NUMBER` | *Your Vapi number* | Caller ID for voice calls |
| `VAPI_RECIPIENT_NUMBER` | *Candidate number* | Destination number (placeholder) |

> **Tip** – Keep the phone numbers in E.164 format (e.g., `+15551234567`).

**Check‑in**  
Do you see all five secrets listed? If any are missing, click **Add new secret** again.

---

### 2.4 Write the Server Code

Replace the contents of `index.js` with:

```js
// index.js
require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const { Configuration, OpenAIApi } = require('openai');
const axios = require('axios');

const app = express();
app.use(bodyParser.json());

const openai = new OpenAIApi(
  new Configuration({ apiKey: process.env.OPENAI_API_KEY })
);

// Helper: call Make.com scenario
async function triggerMake(payload) {
  try {
    await axios.post(process.env.MAKESCOM_WEBHOOK_URL, payload);
  } catch (e) {
    console.error('Make.com error', e.response?.data || e.message);
  }
}

// Helper: call Zapier webhook
async function triggerZapier(payload) {
  try {
    await axios.post(process.env.ZAPIER_WEBHOOK_URL, payload);
  } catch (e) {
    console.error('Zapier error', e.response?.data || e.message);
  }
}

// Helper: initiate Vapi voice call
async function callCandidate(name, phone) {
  const body = {
    to: phone,
    from: process.env.VAPI_SENDER_NUMBER,
    voice: {
      text: `Hello ${name}, your resume has been processed. We'll reach out soon.`
    }
  };
  try {
    await axios.post('https://api.vapi.ai/v1/call', body, {
      headers

## Step 3 – Test and Validate  

At this point your AI‑powered HR automation stack is ready to run. The goal of this step is to confirm that every component behaves as expected, that data flows correctly between services, and that the end‑to‑end candidate experience is seamless. Follow the checklist below, re‑run the tests after each fix, and capture logs for audit.

### 3.1 Launch a “Smoke Test” Pipeline  

1. **Trigger a test candidate record**  
   - Open your Replit workspace.  
   - In `app.py`, locate the route `/test_candidate`.  
   - Run `python app.py` (output: `* Running on http://127.0.0.1:5000/`).  
   - In your browser, navigate to `http://127.0.0.1:5000/test_candidate`.  

   **Expected output**  
   ```
   {
     "status": "ok",
     "candidate_id": "test-123",
     "steps": ["resume_parsing", "skills_match", "initial_screening"]
   }
   ```  
   If you see `{"status":"error"}` instead, proceed to the error section.

2. **Validate resume parsing**  
   - In Replit, open `resume_parser.py`.  
   - Run `python resume_parser.py tests/sample_resume.pdf`.  
   **Expected console**  
   ```
   Parsed Skills: ['Python', 'SQL', 'Machine Learning']
   Parsed Experience: 3 years
   ```  

3. **Confirm ChatGPT screening**  
   - In `chatgpt_screening.py`, run `python chatgpt_screening.py test-123`.  
   **Expected output**  
   ```
   Screening Score: 8.2
   Recommendation: Proceed to interview
   ```  

4. **Check Zapier webhook**  
   - Go to your Zapier dashboard → “My Zaps.”  
   - Open the Zap named “HR Candidate Intake.”  
   - Click “Test & Review” → “Test Trigger.”  
   **Expected**: “Test data received: candidate_id = test-123.”  

5. **Verify ActiveCampaign sync**  
   - In ActiveCampaign, navigate to “Contacts” → “Import.”  
   - Download the CSV of the last import.  
   **Expected**: A row with `candidate_id: test-123` and `status: Screening`.  

### 3.2 Common Errors & Quick Fixes  

| Error | Cause | Fix |
|-------|-------|-----|
| `ConnectionError: HTTPSConnectionPool(host='api.openai.com', port=443): Max retries exceeded with url` | OpenAI key expired or network blocked | Renew API key in Replit secrets (`OPENAI_API_KEY`) and confirm outbound HTTPS to `api.openai.com` |
| `FileNotFoundError: 'tests/sample_resume.pdf'` | Path typo in script | Verify file path or upload PDF to Replit storage as `tests/sample_resume.pdf` |
| `Zapier: 401 Unauthorized` | Wrong webhook URL | Re‑copy the webhook URL from Zapier and paste into Replit env var `ZAPIER_WEBHOOK` |
| `ActiveCampaign: 400 Bad Request` | Missing required field (`email`) | Add a dummy email (`test@example.com`) to the payload before sending to ActiveCampaign |

### 3.3 5‑Point Test Checklist  

1. **Data Ingestion** – Confirm that the test candidate’s JSON appears in the Replit console and is logged in Hostinger’s MySQL database (`SELECT * FROM candidates WHERE id='test-123';`).  
2. **Resume Parsing Accuracy** – Verify that extracted skills match those in `sample_resume.pdf` (compare to manual extraction).  
3. **ChatGPT Response Quality** – Ensure the screening score is numeric (0‑10) and contains the phrase “Proceed to interview.”  
4. **Automation Flow** – Check that the Zapier webhook triggers an ActiveCampaign contact creation and that the contact’s custom field `status` is set to “Screening.”  
5. **Failure Path** – Intentionally send a malformed resume (e.g., `tests/invalid_resume.txt`) and ensure the system logs an error and returns a 400 HTTP status without creating a candidate record.

### 3.4 Final Validation Run  

After all fixes, perform a full end‑to‑end run:

1. Replace `tests/sample_resume.pdf` with a fresh PDF from your candidate pool.  
2. Trigger `/test_candidate` again.  
3. Verify the entire chain: Replit logs → MySQL record → ChatGPT score → Zapier webhook → ActiveCampaign contact.  
4. Capture screenshots of the Replit console, MySQL query result, and ActiveCampaign contact detail.  

If every step passes, your AI HR recruitment automation service is ready for production. Store the screenshots and logs in a Notion page titled “HR Automation Test Report” for audit and future reference.

## Step 4 – Add Advanced Features  
*(≈ 10‑15 minutes per major subsection)*  

The core system now screens and scores resumes, but a production‑ready service needs intelligent enrichment, robust error handling, and dynamic routing. In this step we’ll:

1. **Enrich candidate data with ChatGPT‑4**  
2. **Add automated voice follow‑ups via Vapi**  
3. **Route qualified candidates to ActiveCampaign**  
4. **Log all events in Make.com for auditability**  
5. **Implement graceful error handling**  

> **Interactive Check‑In 1** – After completing 4.1, open your Replit console. Do you see the line `{"score": 88, "skills": ["Python", "AWS"]}`? If not, check that the `CHATGPT_API_KEY` env variable is set and retry.

---

### 1. Enrich Candidate Data with ChatGPT‑4  
**Goal:** Append a concise “candidate summary” and a “culture‑fit” score to each applicant.  

1. **Open your Replit project** (Hacker plan, $7 / month).  
2. In the left sidebar, click **Files** → **open** → **`enrichment.py`**.  
3. Replace the placeholder function with:

```python
import openai, os, json

openai.api_key = os.getenv("CHATGPT_API_KEY")

def enrich(candidate):
    prompt = f"""
    You are a senior HR analyst. Summarize the following resume and rate culture fit (1–10):
    {candidate['resume_text']}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}],
        temperature=0.2,
        max_tokens=200
    )
    data = response.choices[0].message.content.strip()
    summary, fit = data.split("\n\nCulture Fit:")  # assumes format
    return {"summary": summary, "culture_fit": int(fit.strip())}
```

> **Check‑In 2** – Run `python enrichment.py` with a sample JSON. You should see a JSON object with `summary` and `culture_fit`. If you get a 401 error, verify the API key.

4. Commit the file and push to GitHub.  
5. In Make.com (Starter plan, $25 / month), create a **Scenario**:  
   - **Trigger:** Webhook → “When a new candidate is added.”  
   - **Action:** Replit → “Run script `enrichment.py`.”  
   - **Output:** Store the enriched data back into the candidate record.  

---

### 2. Add Automated Voice Follow‑Ups via Vapi  
**Goal:** Deliver a 60‑second voice note to candidates who pass the screening.  

1. In your Replit console, install Vapi SDK:  
   ```bash
   pip install Vapi
   ```  
2. Add the following function to `voice.py`:

```python
from vapi import VapiClient

client = VapiClient(api_key=os.getenv("VAPI_KEY"))

def send_voice(candidate):
    message = f"Hi {candidate['first_name']}, we reviewed your application. Your score is {candidate['score']}. Let's talk!"
    client.send_voice(
        to=candidate['phone'],
        from_number="+1234567890",
        text=message,
        voice="en-US-Wavenet-D"
    )
```

3. In Make.com, extend the previous scenario:  
   - **Action:** Vapi → “Send Voice Call.”  
   - Map `candidate['phone']` and the `message` field.  

> **Check‑In 3** – In the Make.com dashboard, you should see a “Vapi – Send Voice Call” step with “Success” status. If it fails, ensure your `VAPI_KEY` is correct.

---

### 3. Route Qualified Candidates to ActiveCampaign  
**Goal:** Push candidates with a culture‑fit ≥ 7 into a dedicated email nurture workflow.  

1. In Replit, add:

```python
import requests

AC_KEY = os.getenv("AC_API_KEY")
AC_URL = "https://youraccount.api-us1.com/api/3/contacts"

def push_to_ac(candidate):
    payload = {
        "contact": {
            "email": candidate["email"],
            "firstName": candidate["first_name"],
            "lastName": candidate["last_name"],
            "tags": "HR-Qualified"
        }
    }
    r = requests.post(AC_URL, json=payload, auth=(AC_KEY, ""))
    return r.json()
```

2. In Make.com:  
   - **Conditional Router:** If `culture_fit >= 7` → **ActiveCampaign** action “Add Contact.”  
   - Map fields accordingly.  

> **Check‑In 4** – In ActiveCampaign, go to **Contacts** → you should see the new candidate tagged “HR‑Qualified.” If not, verify the API token and URL.

---

### 4. Log All Events in Make.com  
**Goal:** Keep a single source of truth for audit.  

1. In the same Make.com scenario, add:
   - **Action:** Google

## Step 5 – Deploy to Production

Below is a production‑ready workflow that takes the finished code from Step 4 straight into a managed Cloud VPS on Hostinger. The deployment uses Docker for isolation, GitHub Actions for CI/CD, and Make.com to trigger the build whenever a new commit lands on `main`. We’ll also wire in a basic health‑check endpoint so that the system can be monitored by a free UptimeRobot alert.  

> **Prerequisites** –  
> • A Hostinger Cloud VPS (minimum 1 GB RAM, 1 vCPU, 20 GB SSD, Ubuntu 22.04) – $3.99/month.  
> • A GitHub repository with the repo root containing `Dockerfile`, `docker-compose.yml`, and `.github/workflows/deploy.yml`.  
> • A Make.com account (free tier, $9/month) for CI trigger.  
> • An UptimeRobot account (free tier) for health‑checks.  

### 5.1  Prepare the Hostinger VPS

1. **SSH into the server**  
   ```bash
   ssh root@<HOSTINGER_IP>
   ```  
   *Do you see the Ubuntu prompt? If you get “Permission denied”, double‑check the IP and the key you used at Hostinger.*

2. **Add the Docker APT repository**  
   ```bash
   apt-get update && apt-get install -y ca-certificates curl gnupg
   install -m 0755 -d /etc/apt/keyrings
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
     gpg --dearmor -o /etc/apt/keyrings/docker.gpg
   echo \
     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
     $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
   apt-get update
   ```  
   *If you see “dpkg: warning: ...” it’s ok – just keep going.*

3. **Install Docker Engine and Docker Compose**  
   ```bash
   apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
   systemctl enable --now docker
   docker version
   ```  
   Expected output: a JSON block with `Client` and `Server` versions.  
   *If you get “Cannot connect to the Docker daemon”, run `sudo usermod -aG docker $USER` and log out/in.*

4. **Create a dedicated deployment user**  
   ```bash
   adduser deployer
   usermod -aG docker deployer
   exit
   ```  
   *Log back in as `deployer`.*

5. **Set up an SSH key pair** for the GitHub Actions runner (used by Make.com).  
   ```bash
   ssh-keygen -t ed25519 -C "github-actions@<YOUR_DOMAIN>"
   ```
   Copy the `~/.ssh/id_ed25519.pub` into GitHub → Settings → Deploy keys → `Add deploy key`.  
   *Do you see “Deploy key added” in the GitHub UI? If not, double‑check the key.*

### 5.2  Configure GitHub Actions

Create a file `.github/workflows/deploy.yml` with the following content:

```yaml
name: Deploy to Hostinger

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v4

      - name: Install Docker
        uses: docker/setup-buildx-action@v3

      - name: Build and push image
        env:
          REGISTRY: registry.hub.docker.com
          IMAGE_NAME: username/hr-recruit
          IMAGE_TAG: latest
        run: |
          docker build -t $REGISTRY/$IMAGE_NAME:$IMAGE_TAG .
          echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin $REGISTRY
          docker push $REGISTRY/$IMAGE_NAME:$IMAGE_TAG

      - name: Deploy via SSH
        uses: appleboy/ssh-action@v0.1.12
        with:
          host: ${{ secrets.HOSTINGER_IP }}
          username: deployer
          key: ${{ secrets.SSH_PRIVATE_KEY }}
          script: |
            docker pull $REGISTRY/$IMAGE_NAME:$IMAGE_TAG
            docker compose down
            docker compose up -d
```

1. **Set the following repository secrets**:  
   • `DOCKER_USERNAME` – your Docker Hub username.  
   • `DOCKER_PASSWORD` – your Docker Hub password.  
   • `HOSTINGER_IP` – the public IP of your VPS.  
   • `SSH_PRIVATE_KEY` – the contents of `~/.ssh/id_ed25519`.

2. **Trigger the workflow** by pushing a commit to `main`.  
   *You should see the “Deploy to Hostinger” job run and finish with “Finished”.*

### 5.3  Verify the Deployment

1. **Check Docker containers**  
   ```bash
   docker ps
   ```  
   Expected output: one container named `hr_recruit_api_1` running on `0.0.0.0:8000->8000/tcp`.  

2. **Test the health‑check endpoint**  
   ```bash
   curl -s http://<HOSTINGER_IP>:

## Step 6 – Scale and Grow  
**Goal:** Transition from a one‑client MVP to a 10 + client SaaS with a lean internal team, automated workflows, and razor‑thin margins.  
**Estimated time:** 10 – 15 hours (spread across a 1‑week sprint).  

1. **Define the Client‑Onboarding Funnel**  
   1.1. In **Zapier** create a “New Client” trigger: **Webhooks by Zapier → Catch Hook**.  
   1.2. Add an action to **Create a New Company Row** in a **Google Sheet** (or Airtable if you prefer).  
   1.3. Add a second action: **Send Welcome Email** via **ActiveCampaign**.  
   1.4. *Check‑in*: If the sheet shows a new row with the client’s name, you’re in the right place. If not, verify the webhook URL and re‑test the trigger.  

2. **Automate On‑boarding Workflows**  
   2.1. In **Make.com** (formerly Integromat), set up a scenario:  
   - **Trigger:** New row in Google Sheet.  
   - **Action 1:** **Create a New Company** in **HubSpot CRM** (or Salesforce if you prefer).  
   - **Action 2:** **Schedule a Meeting** in **Calendly** (send link via email).  
   - **Action 3:** **Create a New Project Folder** in **Notion** (use the “Create a Page” module).  
   2.2. *Expected output:* A fully populated HubSpot contact, a Calendly link in the email, and a Notion page titled “<Client‑Name> On‑boarding”.  
   2.3. *Error scenario:* If “HubSpot” returns “401 Unauthorized”, your API key is wrong. Re‑generate the key in HubSpot → Settings → API Keys and paste it into the Make.com module.  

3. **Hiring Plan (Phase‑1: 2‑3 hires)**  
   - **Role 1 – AI Engineer** (1 FTE): Use **Replit** to host all custom ChatGPT prompts and fine‑tuning scripts. Replit offers a $10/month plan for team collaboration.  
   - **Role 2 – Automation Specialist** (0.5 FTE): Must be fluent with **Zapier** and **Make.com**. Use **Skilled** (online courses) to certify.  
   - **Role 3 – Growth Marketing** (0.5 FTE): Manage **ActiveCampaign** email flows and **Buffer** for social posting.  
   *Check‑in:* After hiring, confirm each new employee has access to the shared **Notion** workspace and the **Replit** team.  

4. **Upgrade Automation (Phase‑2: 4‑6 clients)**  
   - Replace manual resume parsing with **ChatGPT** + **Python** (hosted on Replit).  
   - Use [**ElevenLabs**](https://elevenlabs.io/) to synthesize interview summaries into audio for recruiters.  
   - Integrate [**Vapi**](https://vapi.ai/) to allow candidates to submit voice‑only responses, automatically transcribed by ChatGPT.  
   *Exact settings:*  
     - **ChatGPT API Key**: stored in Replit Secrets (`OPENAI_API_KEY`).  
     - **ElevenLabs Voice**: “Nova” voice, speed 1.0, volume 1.0.  
     - **Vapi**: “Speech to Text” endpoint with `language=en-US`.  

5. **Margin Improvement (Phase‑3: 7‑10+ clients)**  
   - Move hosting from **Hostinger** (shared plan $3.95/month) to a **DigitalOcean Droplet** ($5/month) for better scaling and uptime.  
   - Implement subscription billing in **Shopify** using the **Shopify Billing API**; set plan tiers at $99/month for 1‑3 clients, $199/month for 4‑6, and $299/month for 7+.  
   - Use **ActiveCampaign** to automate renewal reminders 15 days before expiry.  
   *Expected output:* Clean revenue reconciliation via Shopify’s “Orders” export and automated email triggers.  

6. **Monitoring & Analytics**  
   - Deploy **Grafana** on a free DigitalOcean droplet to visualize API response times and error rates.  
   - Set up a **Slack** channel “#ops‑alerts” with **Zapier** integration: any failure from Make.com pushes a message to Slack.  

---

### Scale Milestones Table  

| Clients | Monthly Recurring Revenue | Team Size | Key Automation | Hosting | Billing Model |
|---------|---------------------------|-----------|----------------|---------|---------------|
| 1–3     | $99 – $199                | 2 (AI + Automation) | Zapier + Make.com | Hostinger $3.95 | Shopify Starter |
| 4–6     | $200 – $600               | 4 (add Growth Marketer) | ChatGPT + Vapi + ElevenLabs | DigitalOcean $5 | Shopify Pro |
| 7–10+   | $700 – $2,000+            | 6 (add Ops & Support) | Full AI pipeline + Analytics | DigitalOcean $5 | Shopify Plus |

**Next steps:**  
- Commit to the hiring plan within 48 hours.  
- Deploy the Make.com scenario and verify all integrations.  
- Set up the Shopify store and billing API.  
- Begin quarterly reviews at each milestone to reassess resource allocation.  

*If any integration fails during the sprint, refer to the “Error scenarios” in the previous steps or consult the tool’s official troubleshooting guide.*

## Cost Breakdown

Below is a granular cost analysis for the AI‑driven HR recruitment automation stack. All figures are **USD** and reflect the most recent published plans (as of June 2026). Prices are rounded to the nearest dollar for clarity.

| Item | Free Tier | Paid Tier | When to Upgrade |
|------|-----------|-----------|-----------------|
| **ChatGPT‑4 (OpenAI API)** | 12 k tokens/month (~$0.03 / 1K tokens) | $20/month (as of 2024) | When average token usage > 12 k per month *or* you need priority access for high‑volume candidates. |
| **Make.com (Automation)** | 200 operations/month | $49/month (Starter) | When automation runs > 200 ops/month or you need more advanced connectors. |
| **ElevenLabs (Text‑to‑Speech)** | 5 hours/month | $29/month | When you need voice interview summaries > 5 hrs/month. |
| **Hostinger (Web Hosting)** | Free sub‑domain, 1 GB SSD | $3.99/month (Premium) | When you exceed 1 GB monthly traffic or need a custom domain for candidate portals. |
| **Zapier (App Automation)** | 100 tasks/month | $19.99/month (Starter) | When tasks > 100/month or you require multi‑step zaps. |
| **Buffer (Social Scheduling)** | 10 scheduled posts/month | $12/month (Pro) | When you run > 10 posts/month or need analytics. |
| [**Semrush (SEO Toolkit)**](https://www.semrush.com/) | 10 reports/month | $99.95/month (Pro) | When you need deeper keyword research for career pages. |
| **Calendly (Scheduling)** | 1 calendar per account | $12/month (Team) | When you need multiple calendars or advanced integrations. |
| **Notion (Workspace)** | Unlimited pages | $8/month (Personal Pro) | When you need version history or API access. |
| **ActiveCampaign (CRM + Email)** | 500 contacts | $15/month (Lite) | When contacts > 500 or you need automation workflows. |

### Monthly Cost Analysis by Scale

| Scale | Solo (1 client) | 5 Clients | 10+ Clients |
|-------|-----------------|-----------|-------------|
| **ChatGPT‑4** | $20 | $20 | $20 |
| **Make.com** | $0 | $49 | $49 |
| **ElevenLabs** | $0 | $29 | $29 |
| **Hostinger** | $3.99 | $3.99 | $3.99 |
| **Zapier** | $19.99 | $19.99 | $19.99 |
| **Buffer** | $12 | $12 | $12 |
| **Semrush** | $99.95 | $99.95 | $99.95 |
| **Calendly** | $12 | $12 | $12 |
| **Notion** | $8 | $8 | $8 |
| **ActiveCampaign** | $15 | $75 | $150 |
| **Total** | **$304.92** | **$400.92** | **$496.92** |

*Notes:*

1. **ChatGPT‑4**: Even on the free tier you can process up to 12 k tokens per month; most solo recruiters stay below this threshold.
2. **Make.com**: The Starter plan gives 4 k operations/month, enough for 200–300 candidate flows; upgrade only when you hit the 200‑op ceiling.
3. **ElevenLabs**: Voice summaries are optional; skip the paid tier if you prefer plain text.
4. **Hostinger**: The $3.99 plan includes a free SSL and 1 GB SSD; upgrade if you need a dedicated IP for SSO.
5. **Zapier**: The Starter plan’s 100 tasks/month covers 10‑step workflows for 1 client; scale to Starter when you have 5 clients each with 2 workflows.
6. **ActiveCampaign**: Pricing scales linearly with contacts. At 10 clients, you’ll likely exceed 1 000 contacts, justifying the Lite plan.

**Bottom line:** A solo entrepreneur can launch the service for **≈ $305/month** using the free tiers where possible. When expanding to 5 clients, the cost bumps to **≈ $401/month**; for 10+ clients it stabilizes around **≈ $497/month**. These figures assume no additional cloud compute or data‑storage costs, which can be added later if your candidate database outgrows the included limits.

## Production Checklist

[ ] **Confirm API Keys and Secrets**  
- Verify the OpenAI API key used by ChatGPT is stored in the `.env` file (`OPENAI_API_KEY=sk-…`).  
- Do you see the key listed under **Settings → API Keys** in Make.com? If not, re‑generate it in the **Developer Console** and paste it into the file.  
- Expected check: `cat .env | grep OPENAI_API_KEY` returns the full key.

[ ] **Validate Make.com Scenario Health**  
- Open the Make.com dashboard and run the “Resume‑Screening” scenario manually.  
- The result panel should display “All steps executed successfully” with a 200‑OK status for each HTTP request.  
- If you see “Error 401”, the API key is invalid; update the credentials in the scenario.

[ ] **Test Vapi Voice Agent Prompt**  
- In Vapi, navigate to **Agents → Resume‑Reader**.  
- Click “Play Test” and confirm the spoken output matches the JSON payload structure.  
- Expected output: “Your CV shows 5 years in software engineering…” If the voice synth returns “Error 500”, check the ElevenLabs key in Vapi settings.

[ ] **Check Slack Webhook Integration**  
- In Slack, open **Apps → Incoming Webhooks** and confirm the webhook URL is active.  
- Post a test message via `curl -X POST -H 'Content-type: application/json' --data '{"text":"Test"}' <WEBHOOK_URL>`.  
- The message should appear in the channel; otherwise, verify the URL in Zapier’s “Send to Slack” action.

[ ] **Validate Email Trigger in Klaviyo**  
- Log into Klaviyo, go to **Flows → New Flow → Trigger**.  
- Ensure the flow “Candidate‑Welcome” is triggered by the Make.com webhook.  
- Simulate a candidate signup; the welcome email should be sent within 2 seconds.

[ ] **Ensure Hostinger Site Accessibility**  
- Visit your production URL (`https://hr‑auto.menshly.com`).  
- The page should load within 3 seconds and show the “Candidate Dashboard” UI.  
- If the page returns 502, check the DNS A record in Hostinger’s control panel.

[ ] **Audit Data Retention Policies**  
- In Notion, open the “Candidate Database” and confirm the retention rule is set to “Delete after 90 days”.  
- Verify the deletion log shows a record entry for the last automated purge.

[ ] **Run End‑to‑End Smoke Test**  
- Use Replit to execute the script `tests/smoke_test.py`.  
- All assertions should pass and the console should output `SMOKE TEST PASSED`.  
- Any failure indicates a missing integration or misconfigured endpoint.

[ ] **Confirm Analytics Tracking**  
- In Google Analytics, open the real‑time report and select “Recruitment Site”.  
- Verify a new user is recorded when the test candidate signs up.  
- If no hit appears, check the GA tracking snippet in the `index.html` file on Hostinger.

---  

**When all nine items pass, you are ready to launch.**

## What to Do Next

**1. Hook ChatGPT Screening into Your ATS**  
Open Zapier, click **Create Zap** → Trigger: *New Resume* (e.g., Workable → “New Candidate”).  
Add Action: *Webhooks by Zapier* → *POST*.  
In the *URL* field put `https://api.openai.com/v1/chat/completions`.  
In *Data* set:  
```
{
  "model":"gpt-4o-mini",
  "messages":[{"role":"user","content":"Screen this résumé: {{Resume_Text}}"}],
  "temperature":0.2
}
```  
Under *Headers* add `Authorization: Bearer YOUR_OPENAI_KEY`.  
Test the Zap; you should see a JSON response with a `choices[0].message.content` field containing the screening score.  
Store that score in Airtable (Table: “Screened Candidates”) by adding an *Update Record* action.  
Check Airtable: the new record should now show the “Score” field.

**2. Source Candidates with Apollo.io & PhantomBuster**  
Log in to Apollo.io, create a search with filters (Industry: “Software”, Title: “Senior Engineer”). Export results to CSV.  
In PhantomBuster, select *LinkedIn Lead Gen* → upload the CSV → map “First Name” and “Last Name” to the script.  
Run the run; the output JSON will contain LinkedIn URLs and emails.  
Import the JSON back into Airtable.  
Validate: you should see a new column “LinkedIn Profile” populated.

**3. Automate Email Drips in Klaviyo**  
In Klaviyo, create a Flow triggered by *Airtable Record Created* (via Zapier integration).  
Add an *Email* step: use the dynamic template `{{first_name}}, we noticed you might be a good fit for ...`.  
Insert a *ChatGPT* block (Zapier → Webhook → ChatGPT) to generate personalized subject lines.  
Publish the Flow.  
Verify in Klaviyo’s “Preview” that the subject line contains the AI‑generated snippet.

**4. Send Voice Interview Prompts with Vapi**  
Create a Zap: Trigger → *Airtable Record Updated* (Score ≥ 80).  
Action: *Vapi* → “Send Voice Message”.  
Set *Prompt*: “Hi {{first_name}}, thanks for applying. Please record a 60‑second video answering: “What excites you about this role?”.”  
Add a *Delay* (5 min) then *Vapi* → “Transcribe Voice” to capture the response.  
Check Vapi dashboard; you should see the transcription in the “Transcriptions” tab.

**5. Track Impact with Google Analytics & Mixpanel**  
Add Google Tag Manager to your recruitment portal.  
Create a Custom Event named `chatgpt_screening_complete` triggered when the Airtable webhook fires.  
In Mixpanel, set up a funnel: *Submit Resume* → *ChatGPT Screening Complete* → *Email Drip Sent*.  
Verify Mixpanel reports daily conversion rates.  
For deeper insight, add a *Heatmap* in Hotjar (free tier) to see where candidates spend most time on the form.  

For more on integrating Zapier with HR workflows, read our article **“Zapier Automation for Recruitment”** (https://menshly.com/zapier-recruitment).

Ready to understand the full business opportunity? Read our [opportunity deep-dive]({< ref "/opportunities/how-to-build-an-ai-hr-recruitment-automation-10k-20kmonth.md" >}).


## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Notion](https://notion.so/)** — All-in-one workspace — notes, docs, project management
- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
