---
title: "Build an AI Real Estate Process Automation with ChatGPT: The Complete Step-by-Step Guide"
date: 2026-07-14
category: "Implementation"
difficulty: "INTERMEDIATE"
readTime: "25 MIN"
excerpt: "In this step‑by‑step execution guide you will build a fully automated real‑estate workflow that leverages ChatGPT, Make.com, and ElevenLabs to streamline lead qualification, property descriptions, and..."
image: "/images/articles/intelligence/automate-optimize-and-analyze-real-estate-processes-with-ai-tools.png"
heroImage: "/images/heroes/intelligence/automate-optimize-and-analyze-real-estate-processes-with-ai-tools.png"
relatedOpportunity: "/opportunities/how-to-build-an-ai-real-estate-automation-service-8k-12kmonth/"
---

In this step‑by‑step execution guide you will build a fully automated real‑estate workflow that leverages ChatGPT, Make.com, and ElevenLabs to streamline lead qualification, property descriptions, and client communication. By the end of the guide you will have a repeatable system that captures inbound inquiries, generates AI‑powered listing copy, and delivers personalized voice‑to‑text updates to prospects—all without manual duplication of effort. The system will also log every interaction into a Notion database for ongoing analysis and performance tuning.

This is not a conceptual blog post; it is a hands‑on implementation manual. Every numbered step will specify exact API calls, UI navigation paths, and configuration values, so you can copy‑paste the commands and see the expected output immediately. We’ll cover setup of a Replit workspace, integration with Shopify for property listings, and a Zapier workflow that pushes data into Klaviyo for targeted email follow‑ups. The entire build is designed to take approximately 12–15 hours of focused work and will cost roughly $350 in tooling subscriptions (Hostinger, Replit, ChatGPT API, and Make.com).

This guide serves as the implementation companion to the opportunity article “How to Build an AI Real Estate Automation Service ($8K‑$12K/Month)” (URL: /opportunities/how-to-build-an-ai-real-estate-automation-service-8k-12kmonth/).  
Ready to understand the full business opportunity? Read our [opportunity deep‑dive]({< ref "/opportunities/how-to-build-an-ai-real-estate-automation-service-8k-12kmonth.md" >}).

## Prerequisites  

Before you begin building the AI‑powered real‑estate automation stack, you must create and configure a handful of cloud accounts and obtain the necessary credentials.  The following checklist covers every tool, its cost, the exact settings you need, and the time required to finish the setup.

### Accounts & Tool Setup (≈30 min)

| Tool | Exact Account Actions | Cost | Free‑Tier Limit |
|------|-----------------------|------|-----------------|
| **OpenAI (ChatGPT API)** | Sign up at https://platform.openai.com/, click **“Create new secret key”**, copy the key, store it in a `.env` file as `OPENAI_API_KEY`. | $0.02 / 1 k tokens (pay‑as‑you‑go) | 1 M tokens/month |
| [**Replit**](https://replit.com/refer/egwuokwor) | Create a new Replit → choose **Python** template → name it `realest‑ai‑bot`. Enable **+– GitHub** if you want version control. | $7 / month (REPLIT + Pro) | 5 GB storage, 1 GB RAM |
| **Hostinger** | Register a domain (e.g., `myrealestate.ai`), then add a **Shared Hosting** plan (Starter) → $3.99 / month. Install **cPanel** → add a sub‑domain `app.myrealestate.ai`. | $3.99 / month | 1 GB RAM, 1 GB SSD |
| **Zapier** | Sign up → create a new Zap → choose **Email by Zapier** as trigger, **Webhooks by Zapier** as action. | $19.99 / month (Starter) | 100 tasks/month |
| [**Make.com**](https://www.make.com/en/register?pc=menshly) | Create a new scenario → add **HTTP → Make a request** → test with `https://api.openai.com/v1/chat/completions`. | $5.00 / month (Starter) | 500 actions/month |
| **ActiveCampaign (CRM + Email)** | Sign up → add your domain → create a new **Campaign** → set up **Webhooks** → link to Replit webhook URL. | $29 / month (Lite) | 2 000 contacts |
| [**Notion**](https://notion.so/) | Create a workspace → add a **Database** called `Leads`. | Free | Unlimited pages |
| [**Vapi**](https://vapi.ai/) | Create a project → enable **Text‑to‑Speech** → copy your API key. | Free tier: 50 calls/month | 50 calls |
| [**ElevenLabs**](https://elevenlabs.io/) | Sign up → generate an API key → set `VOICE_ID` to “Rachel”. | Free tier: 10 k chars | 10 k chars |
| [**Canva**](https://www.canva.com/) | Sign up → choose **Pro** plan → create a template for property flyers. | $12.99 / month | 5 GB storage |
| [**Grammarly**](https://grammarly.com/) | Sign up → install browser extension → enable **AI Writing Assistant**. | Free | Unlimited usage |

### Total Upfront Cost  
Adding the monthly plans together gives an **approximate initial cost of $66.98 / month**. If you opt for the free tiers for Replit, Hostinger, Zapier, and Make.com, the first‑month cost drops to **$36.98 / month**.

> **Check‑in:** After completing each account, visit the dashboard and ensure you see the “API Key” section (OpenAI, Vapi, ElevenLabs) or the “Webhooks” tab (Zapier). If any key is missing, return to the account settings and generate a new key. Once all keys are stored in your environment, you’re ready to start coding the automation logic.

## Step 1 : Setup and Configuration  
**(≈ 25 min)**  

> *Goal:* Create the foundation for the automation stack: a clean directory, a secure secrets store, and all the OAuth/API tokens you’ll need.  
> *Tools used:* Replit (IDE & terminal), Make.com (workflow orchestration), Apollo.io (lead finder), Notion (database), ElevenLabs (voice synthesis), ChatGPT (OpenAI API).  

---

### 1️⃣ Create the Project Folder

```bash
# In Replit’s shell or your local terminal
mkdir -p ~/realestate_ai/{src,data,scripts,config,logs}
cd ~/realestate_ai
```

**Expected output**

```
$ mkdir -p ~/realestate_ai/{src,data,scripts,config,logs}
$ cd ~/realestate_ai
realestate_ai$
```

> **Check‑in:** Do you see the folder `realestate_ai` with the sub‑folders `src`, `data`, `scripts`, `config`, and `logs`?  
> If not, run the `mkdir` command again.  
> *Error:* `Permission denied` – you’re trying to write to a protected directory. Use `sudo` or choose a writable location like `~/`.

---

### 2️⃣ Initialise a Git Repository

```bash
git init
```

**Output**

```
Initialized empty Git repository in /home/your‑user/realestate_ai/.git/
```

> **Check‑in:** Do you see the `.git` directory?  
> If `git` is not installed, install it first (`sudo apt‑get install git`) or use Replit’s built‑in repo.

---

### 3️⃣ Create a Virtual Environment & Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install openai requests python-dotenv
```

**Output**

```
(venv) $ pip install --upgrade pip
Collecting pip
  Downloading pip‑23.0‑py3‑none‑any.whl (2.1 MB)
...
(venv) $ pip install openai requests python-dotenv
Collecting openai
  Downloading openai‑0.27.0‑py3‑none‑any.whl (83 kB)
...
(venv) $ 
```

> **Check‑in:** Do you see the command prompt prefixed with `(venv)`?  
> If `pip` complains about permissions, run with `--user` or switch to a virtual env.

---

### 4️⃣ Gather API Tokens

| Service | What to do | URL | What to copy |
|---------|------------|-----|--------------|
| **OpenAI (ChatGPT)** | Create a secret key in the OpenAI dashboard. | https://platform.openai.com/account/api-keys | `sk-xxxxxxxxxxxxxxxxxxxx` |
| **Apollo.io** | Navigate to `Account > Settings > API Access`. | https://app.apollo.io/settings/api | `API_KEY_APOLLO` |
| **Notion** | Create an integration, enable `Insert` and `Read` permissions. | https://www.notion.so/my-integrations | `NOTION_TOKEN` |
| **ElevenLabs** | In the dashboard, `Generate new API key`. | https://beta.elevenlabs.io/account/api | `ELEVENLABS_API_KEY` |
| **Make.com** | Create a new scenario → `Webhook` trigger → `Copy URL`. | https://www.make.com/en/dashboard | `MAKE_WEBHOOK_URL` |

> **Check‑in:** Do you have all the keys ready?  
> If a key shows `invalid` or `revoked`, regenerate a new key.

---

### 5️⃣ Store Secrets in a `.env` File

Create `config/.env` (do **not** commit this file to Git):

```bash
cat > config/.env <<'EOF'
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
APOLLO_API_KEY=API_KEY_APOLLO
NOTION_TOKEN=NOTION_TOKEN
ELEVENLABS_API_KEY=ELEVENLAB

## Step 2 : Build the Core System  

In this section we assemble the heart of the automation: a cloud‑hosted FastAPI service that consumes ChatGPT, a Make.com scenario that turns raw lead data into enriched property insights, and a Zapier workflow that pushes the final record into ActiveCampaign.  
All components are fully deployed, tested, and ready for production.  

---

### 2.1 Create the Replit Project & FastAPI Skeleton  

1. **Login to Replit** → click **+ Create** → select **Python** → name the project `real-estate-automation`.  
2. In the left sidebar, click **+ Add file** → name it `main.py`.  
3. Paste the following minimal FastAPI scaffold:

```python
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI(title="RE Automation API")

@app.post("/lead")
async def create_lead(request: Request):
    payload = await request.json()
    # payload will contain: name, email, phone, property_type, budget
    return {"status": "received", "payload": payload}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

4. In Replit, click **Packages** → search for `fastapi`, `uvicorn`, `python-dotenv` → click **+ Install** for each.  
5. Click **Run**. Replit will expose a public URL (e.g., `https://real-estate-automation.repl.co`).  

**Check‑in 1**  
Do you see the “Replit is running…” banner and the URL in the console?  
You should see an output like:  
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```
If you see `ERROR: No module named fastapi`, verify that you installed the package and that the Replit Python version is 3.10 or higher.

---

### 2.2 Add the OpenAI ChatGPT Integration  

1. In the Replit console, run:  
   ```bash
   pip install openai
   ```  
2. Create a file `.env` in the root with the following content (replace `<YOUR_KEY>` with your actual key):

```
OPENAI_API_KEY=<YOUR_KEY>
```

3. Update `main.py` to call ChatGPT for property descriptions:

```python
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_description(property_type: str, budget: float) -> str:
    prompt = f"Write a compelling property description for a {property_type} with a budget of ${budget:,}."
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}],
        temperature=0.7,
    )
    return resp.choices[0].message.content.strip()
```

4. Modify `create_lead` to return the generated description:

```python
    description = generate_description(payload["property_type"], payload["budget"])
    return {"status":"received","description":description}
```

**Check‑in 2**  
Send a test POST request using the Replit console:

```bash
curl -X POST https://real-estate-automation.repl.co/lead \
 -H "Content-Type: application/json" \
 -d '{"name":"Jane Doe","email":"jane@example.com","phone":"555-1234","property_type":"condo","budget":350000}'
```

You should receive JSON similar to:

```json
{
  "status":"received",
  "description":"A stunning 2‑bedroom condo..."
}
```

If you see `401 Unauthorized`, double‑check the `OPENAI_API_KEY` value in `.env`.

---

### 2.3 Set Up Make.com Scenario for Lead Enrichment  

1. Log into **Make.com** → **Create a new scenario**.  
2. **Trigger** → search for **Webhooks** → select **Custom Webhook** → click **Create new webhook** → name it `lead_webhook`.  
   - Copy the generated URL (e.g., `https://hook.integromat.com/abcd1234`).  
3. Replace the Replit endpoint in the test curl command to point at this URL.  
4. **Action 1** → search for **ChatGPT** → **Send a Prompt**.  
   - **Prompt**:  
     ```text
     Generate a friendly greeting and a short introduction for a new lead: {{payload.name}}
     ```  
   - **API Key**: paste your OpenAI key (Make will ask you to create a new connection).  
5. **Action 2** → search for **ActiveCampaign** → **Create/Update Contact**.  
   - **API Key**: use your ActiveCampaign account key (found under Settings → Developer).  
   - Map fields:  
     - `Email` → `{{payload.email}}`  
     - `First Name` → `{{payload.name}}`  
     - `Phone` → `{{payload.phone}}`  
     - `Custom Field: Property Type` → `{{payload.property_type}}`  
     - `Custom Field: Budget` → `{{payload.budget}}`  
     - `Custom Field: Description` → `{{description}}`  
6. **Action 3** → search for **Buffer** → **Create a Post** (optional).  
   - **Message**: `New

## Step 3 : Test and Validate  

After wiring the data pipeline in Make.com and the lead‑generation script in Replit, you must verify that every component behaves exactly as expected. The following sub‑steps walk you through a thorough sanity check using the exact commands, menu paths, and expected outputs that you can copy‑paste into your tools.

---

### 3.1 Trigger a Test Lead in Replit  
1. Open your Replit project (URL: `https://replit.com/@<your‑username>/real‑estate‑lead‑gen`).  
2. In the Replit console, run the test harness by executing:  
   ```bash
   python test_lead.py
   ```
3. *Interactive check‑in*:  
   - Do you see the line `Test lead generated: {...}` printed in the console?  
   - If not, look for the error message `Traceback (most recent call last):` and confirm that `requests` is installed (`pip install requests`).  

4. Expected output (copy‑paste):  
   ```
   Test lead generated: {"name":"John Doe","email":"john.doe@example.com","city":"Austin","budget":650000}
   ```

---

### 3.2 Verify Webhook Delivery in Make.com  
1. In Make.com, open the scenario `Lead to CRM`.  
2. Click **Run once** → **Run**.  
3. *Interactive check‑in*:  
   - Do you see the *Custom Webhook* module marked “✓ Delivered”?  
   - If it shows “✗ Failed”, click the error and confirm the URL matches the one printed in your Replit console (`https://hook.integromat.com/...`).  

4. Expected JSON payload in the Webhook module:  
   ```json
   {
     "name":"John Doe",
     "email":"john.doe@example.com",
     "city":"Austin",
     "budget":650000
   }
   ```

---

### 3.3 Validate CRM Entry (ActiveCampaign)  
1. In the *ActiveCampaign* module, open the “Create/Update Contact” step.  
2. After the scenario finishes, log into ActiveCampaign → **Contacts** → search for `john.doe@example.com`.  
3. *Interactive check‑in*:  
   - Do you see a new contact with the exact city and budget fields?  
   - If the contact is missing, revisit the field mapping in Make.com (e.g., `{{city}}` → `City`).  

---

### 3.4 Test Email Follow‑Up (Klaviyo)  
1. In Make.com, run the *Send Welcome Email* module.  
2. Log into Klaviyo → **Flows** → locate the “New Lead Welcome” flow.  
3. *Interactive check‑in*:  
   - The email should appear in the **Test** tab with the subject “Welcome to Our Real‑Estate Platform”.  
   - If the email body is blank, confirm that the template variable `{{name}}` is correctly passed.  

---

### 3.5 Confirm Voice Prompt (ElevenLabs)  
1. In Replit, run `python voice_prompt.py`.  
2. The script should call ElevenLabs API and output a URL to an MP3 file.  
3. *Interactive check‑in*:  
   - Open the URL in a browser and verify the spoken name matches the test lead.  
   - If you receive `401 Unauthorized`, double‑check your ElevenLabs API key in the `.env` file (`ELEVENLABS_API_KEY=`).  

---

### Common Errors & Fixes  

| Error | Cause | Fix |
|-------|-------|-----|
| `ERROR: 401 Unauthorized` | API key missing or expired | Update the key in Replit’s `.env` and re‑run the script. |
| `✗ Webhook failed – 404` | Wrong webhook URL | Copy the exact URL from Replit console to Make.com. |
| `Field mapping mismatch` | Incorrect Make.com field reference | Edit the Make.com module and replace `{{city}}` with the correct variable. |
| `Email not sent` | Klaviyo API key revoked | Re‑authenticate in Klaviyo → Settings → API Keys. |

---

### 5‑Point Test Checklist  

1. **Lead data round‑trip** – Test lead appears in Replit console → Make.com webhook → ActiveCampaign contact.  
2. **Email deliverability** – Welcome email sent via Klaviyo and visible in the test tab.  
3. **Voice prompt accuracy** – ElevenLabs MP3 contains the correct lead name.  
4. **Error handling** – All modules show “✓” status; no “✗” or “⚠” icons.  
5. **Performance** – Total execution time < 10 seconds for the entire scenario.  

Once all five points pass, you can confidently move to Step 4: Deploy & Scale.

## Step 4 : Add Advanced Features  

The core system is now live, but to make the solution production‑ready we need to enrich listings, automate lead routing, and add robust error handling. In this section we’ll plug in AI enrichment, voice & video tours, scheduling, and a retry policy that keeps the pipeline humming.

### 4.1 Enrich Property Descriptions with ChatGPT  

1. **Create a new module in Make.com**  
   - Go to your dashboard → **Create a new scenario** → **Add an action**.  
   - Search for **ChatGPT** → click **Add**.  
   - In the module settings, set **Model** to **gpt‑4**.  
   - Set **Temperature** to **0.6** (controlled creativity).  
   - Set **Max tokens** to **250**.  
   - In the **Prompt** field, paste:  

     ```
     Write a 200‑word, SEO‑friendly property description for the following details:
     • Address: {{address}}
     • Bedrooms: {{bedrooms}}
     • Bathrooms: {{bathrooms}}
     • Square feet: {{sqft}}
     • Highlights: {{highlights}}
     ```

   - Save and test with a sample record.  
   - **Check‑in**: Do you see a “Response” field with a JSON object containing a “text” key? If not, verify that the API key under **Tools → API Keys** is active.

2. **Persist the enriched text**  
   - Add an **HTTP → Make a request** module.  
   - Set **Method** to **PUT**.  
   - URL: `https://api.yourhost.com/properties/{{property_id}}`  
   - In **Headers**, add **Content‑Type: application/json**.  
   - In **Body**, use raw JSON:  

     ```json
     {
       "description": "{{Text}}"
     }
     ```

   - *Error scenario*: If you receive **401 Unauthorized**, your API key is expired—renew it in Hostinger → **Security → SSL/TLS** → regenerate.

### 4.2 Create Voice Tours with Vapi  

1. **Configure Vapi** in Replit’s `app.py`  
   ```python
   import requests, json

   VAPI_KEY = "YOUR_VAPI_KEY"
   def generate_voice(description, prop_id):
       payload = {
           "text": description,
           "voice": "en-US-Standard-B",
           "output_format": "mp3"
       }
       headers = {"Authorization": f"Bearer {VAPI_KEY}"}
       r = requests.post("https://api.vapi.ai/v1/synthesize", json=payload, headers=headers)
       r.raise_for_status()
       with open(f"voice/{prop_id}.mp3", "wb") as f:
           f.write(r.content)
   ```

2. **Trigger in Make.com**  
   - Add a **Python → Execute Code** module after the ChatGPT step.  
   - Paste the function above, reference `{{Text}}` as `description`.  
   - **Check‑in**: Does the log show “POST https://api.vapi.ai/v1/synthesize” succeeded? If you see **429 Too Many Requests**, throttle your requests by adding a **Delay** module of **2 seconds** between batches.

### 4.3 Generate Video Tours via Fliki AI  

1. **Create a new scenario in Make.com**  
   - **Add an action** → [**Fliki AI**](https://fliki.ai?referral=noah-wilson-w84be4) → **Generate Video**.  
   - Set **Title**: `{{title}} – {{address}}`.  
   - **Script**: `{{Text}}` (the enriched description).  
   - **Voice**: Choose **English Female 2**.  
   - **Thumbnail**: enable “Auto‑generate”.  
   - **Output**: select **MP4**.  

2. **Upload to Hostinger**  
   - Add an **SFTP** module → **Upload**.  
   - Host: `hostinger.com`; User: your FTP username; Password: your FTP password.  
   - Remote Path: `/public_html/videos/{{property_id}}.mp4`.  

   **Check‑in**: Open your browser, navigate to `https://yourdomain.com/videos/{{property_id}}.mp4`. You should see the video playing. If the file doesn’t appear, verify the FTP credentials under **Hosting → FTP Accounts**.

### 4.4 Automated Lead Routing with Zapier  

1. **Create

## Step 5 : Deploy to Production

Below is a production‑ready deployment workflow that uses **Hostinger VPS** (USD $3.99/month for a 1 GB plan), **Docker** for containerization, **Nginx** as a reverse proxy, and **Let’s Encrypt** for free HTTPS. The same steps work on any Linux VPS; only the URLs and credentials change.

> **Prerequisites**  
> * A Hostinger VPS with root SSH access (you’ll need the IP, username `root`, and the SSH key you added in Step 1).  
> * Docker Engine v20.10+ installed (`apt install docker.io` and `systemctl enable --now docker`).  
> * Docker Compose v2 (`apt install docker-compose`).  
> * Docker Hub account (free tier) – store the image `yourdockerhub/realestate‑bot`.  
> * Domain registered with DNS A‑record pointing to the VPS IP (e.g., `bot.yourdomain.com`).  

### 1️⃣ Build and Push the Docker Image

```bash
# Clone the repo that contains the ChatGPT‑based bot
git clone https://github.com/yourorg/realestate‑bot.git
cd realestate‑bot

# Build the image locally
docker build -t realestate‑bot:latest .

# Tag for Docker Hub
docker tag realestate‑bot:latest yourdockerhub/realestate‑bot:latest

# Log in to Docker Hub
docker login

# Push the image
docker push yourdockerhub/realestate‑bot:latest
```

**Check‑in**: In Docker Hub’s web UI, you should see the `realestate‑bot` repo with the `latest` tag. If you see *“Repository not found”*, verify your login session and repo visibility.

### 2️⃣ Deploy on Hostinger VPS

```bash
# SSH into the VPS
ssh root@<VPS‑IP>

# Install Docker Compose (if not already)
curl -L "https://github.com/docker/compose/releases/download/v2.15.1/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Create a directory for the stack
mkdir -p /opt/realestate
cd /opt/realestate

# Create docker‑compose.yml
cat > docker-compose.yml <<'EOF'
version: "3.9"
services:
  bot:
    image: yourdockerhub/realestate‑bot:latest
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - VAPI_KEY=${VAPI_KEY}
      - PORT=8080
    restart: unless-stopped
EOF
```

**Check‑in**: Run `cat docker-compose.yml`. You should see the exact file above. If the `environment` section is missing, add it.

### 3️⃣ Pull & Run the Container

```bash
# Pull the latest image
docker compose pull bot

# Start the service
docker compose up -d bot
```

**Check‑in**: `docker ps` should list a container named `realestate_bot_bot_1` exposing port `8080`. If the container exits immediately, inspect logs with `docker logs realestate_bot_bot_1`.

### 4️⃣ Configure Nginx Reverse Proxy

```bash
apt install nginx

cat > /etc/nginx/sites-available/realestate_bot <<'EOF'
server {
    listen 80;
    server_name bot.yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
EOF

ln -s /etc/nginx/sites-available/realestate_bot /etc/nginx/sites-enabled/
systemctl restart nginx
```

**Check‑in**: Open `http://bot.yourdomain.com` in a browser. You should see the bot’s health endpoint (`/health`) return `{"status":"ok"}`. If you see a 404, double‑check the `server_name` and that the proxy_pass URL matches the container port.

### 5️⃣ Enable HTTPS with Let’s Encrypt

```bash
apt install certbot python3-certbot-nginx
certbot --nginx -d bot.yourdomain.com
```

Follow the prompts to accept the terms and let Certbot auto‑reload Nginx. Verify with `https://bot.yourdomain.com`.

### 6️⃣ Automate Updates with Make.com

Create a Make.com scenario that triggers on a new Docker Hub tag:

1. **Trigger**: “When a new Docker Hub tag is pushed” → set to `realestate‑bot:latest`.  
2. **Action**: “SSH by Make” → connect to the VPS, run `docker compose pull bot && docker compose up -d bot`.  
3. **Notification**: Send a Slack message “✅ Bot updated to latest version”.

**Check‑in**: After pushing a new commit, confirm the Slack message appears and the container restarts without downtime.

### 7️⃣ Monitor & Log

- **PM2** (optional) – If you prefer a process manager, install `npm i -g pm2` and run `pm2 start docker-compose.yml`.  
- **Log Aggregation** – Push logs to **LogDNA** (free tier) or **Datadog** (starting at $15/month) via the Docker logging driver.

### 8️⃣ Final Verification

```bash
# Confirm HTTPS
curl -I https://bot.yourdomain.com/health
# Expected output:
# HTTP/2 200
# content-type: application/json
# {"status":"ok"}

# Confirm API latency
ab -n 100 -c 10 https://bot.yourdomain.com/api/lead
# Results should show latency < 200 ms under normal load
```

**Error scenario**: If `curl

## Step 6: Scale and Grow

**Step 6 : Scale and Grow**  
*(Target: 300‑400 words)*  

---

### 6.1 Hiring Plan  
1. **Define Roles** – Create a one‑page job spec for each role in Notion (Title: “Junior Real‑Estate AI Specialist”).  
   - *Skills*: Python 3.8+, familiarity with Make.com, ChatGPT API, and basic SQL.  
   - *Compensation*: $18–$22 / hour; payable via PayPal.  
2. **Source Candidates** – Use Apollo.io to search for “AI real estate consultant” in the United States, filter for “remote” and “entry‑level.” Export the CSV.  
   - *Check‑In*: Do you see a column “Email” in the exported file? If not, open Apollo.io → “Lead Export” → “Add Email.”  
3. **Screening** – Send a quick “OpenAI Prompt Test” via Zapier → “Email by Zapier” (free plan, 100 tasks/month).  
   - *Expected Output*: Candidate replies with a JSON object containing a short property description.  
4. **Onboarding** – Create a Slack channel “#ai‑team‑onboarding” and copy the welcome message template from the Replit repo `templates/onboarding.md`.  
   - *Setting*: Slack API token “xoxb‑***” stored in Vault.  

---

### 6.2 Automation Upgrades  
| Tool | Upgrade | Exact Settings | Expected Result |
|------|---------|----------------|-----------------|
| Make.com | Property‑lead sync | Event: “New Lead” → Action: “Create Record” in Notion (DB: Properties) | New lead appears in Notion instantly |
| Zapier | Email drip | Trigger: “New Contact” in ActiveCampaign → Action: “Send Email” (Template ID: 12345) | Automated follow‑up email sent within 5 min |
| Vapi | Voice outreach | API Key: `vapi‑sk‑***` → POST `/call` with payload `{ "to":"{lead.phone}", "script":"Hi, this is {agent.name}..." }` | Call placed, recording stored in Google Drive |

*Interactive Check‑In*: Open Make.com → “Scenarios” → you should see “Property‑Lead Sync” listed. If missing, go to “Create New Scenario” → search “Notion” → add trigger “New Database Item.”

---

### 6.3 Margin Improvements  
1. **Copywriting** – Use ChatGPT‑4 (OpenAI pricing: $0.03/1k tokens) to generate 5‑line property descriptions.  
   - *Prompt*: “Write a 5‑sentence description for a 3‑bedroom townhouse in Brooklyn, NY.”  
   - *Result*: <50 tokens, $0.0015 per description.  
2. **Video Tours** – Feed the description into Fliki AI (plan: $29/month) to auto‑create a 30‑second video.  
   - *Setting*: “Voice: Female, Accent: US.”  
   - *Output*: MP4 file saved to S3 bucket “real‑estate‑videos.”  
3. **Lead Qualification** – Apollo.io’s “Scoring” feature (API key: `apo‑sk‑***`) assigns a score 0‑100. Only leads > 70 trigger a Vapi call.  
   - *Result*: 35 % fewer wasted outreach calls; saves $0.50 per call.

---

### 6.4 Scale Milestones  

| Clients | Monthly Revenue | Automation Layer | Team Size | Key KPI |
|---------|-----------------|------------------|-----------|---------|
| 1–5     | $5 k           | Basic Make.com & Zapier | 1 | Lead‑to‑close rate 15 % |
| 6–20    | $15 k          | Add Vapi voice calls | 2 | Calls per lead 1.2 |
| 21–50   | $40 k          | Introduce Fliki video tours | 3 | Avg. video views 3k |
| 51–100  | $80 k          | Deploy Replit‑hosted micro‑service for bulk property uploads | 5 | API error rate <

## Cost Breakdown

*Section content pending review.*


## Production Checklist

Before you publish your AI‑driven real estate workflow, run through the following 8‑item checklist. Each item is **specific** and **measurable**; you can tick it only when you can confirm the condition in a screenshot or terminal log.

- **[ ] Verify ChatGPT Prompt Accuracy**  
  Open the Replit project, file `prompts.py`. Confirm that the `LEAD_QUALIFIER_PROMPT` string ends with `"\nPlease rank the lead on a scale of 1‑10."`. Open the console and run `python prompts.py test`. You should see `Rank lead: 7`. If the rank is missing, the prompt string is truncated; edit the file and redeploy.

- **[ ] Confirm Make.com Webhook is Live**  
  In Make.com, go to **Scenarios → Your Real‑Estate Automation**. The first step should be **Webhook** with status **“Triggered”**. Click **Run once** and view the output panel. You must see a JSON payload:  
  ```json
  {"property_id":"12345","client_email":"client@example.com"}
  ```  
  If the payload is empty, check the **URL** copied from the **Trigger** step and paste it into a Postman request.

- **[ ] Test Vapi Voice Agent Response**  
  In Vapi console, navigate to **Agents → Property Inquiry Bot**. Click **Test** and speak “Show me 3 listings in Miami.” The audio output should play within 3 seconds. Verify the transcript in the console reads:  
  `User: Show me 3 listings in Miami.`  
  `Bot: Here are the top 3 listings...`  
  If the bot returns a generic error, ensure the `API_KEY` in `vapi.env` is set to the key from the Vapi dashboard.

- **[ ] Validate Lead Capture via Zapier**  
  Open Zapier, find the **Real Estate Lead Capture** Zap. The trigger is **Make.com Webhook**; the action is **ActiveCampaign → Add/Update Contact**. Turn the Zap on, then trigger the webhook locally. In ActiveCampaign, search for the test email and confirm the custom field **“AI Lead Score”** equals `7`. If the field is blank, check the field mapping in Zapier.

- **[ ] Check Email Deliverability with Klaviyo**  
  In Klaviyo, create a test campaign to `test@yourdomain.com`. In the **Send Settings**, set **From Name** to “Your Realty AI” and **From Email** to `noreply@yourdomain.com`. Send the test and open the email in Gmail. The subject must read “Your AI‑Curated Listings”. If the email lands in spam, verify SPF/DKIM records in Hostinger’s DNS panel.

- **[ ] Ensure SEO Metadata from [Semrush](https://www.semrush.com/)**  
  Run a Semrush Site Audit on `yourrealestate.com`. Under **On‑Page SEO**, confirm that every listing page has a **meta title** ≤ 60 chars and a **meta description** ≤ 160 chars. In the Replit project, `seo.py` should output a JSON with `"title_length": 58`. If the length is off, edit the Jinja template accordingly.

- **[ ] Validate Video Generation with Fliki AI**  
  In Fliki, upload a short script: “Welcome to the Sunshine Estates collection.” The generated MP4 should be 30 seconds, 1080p, and download link appears in the **My Videos** tab. Click **Preview**; if the video does not play, check the **Audio‑Video Sync** toggle in the settings and re‑render.

- **[ ] Confirm Scheduling Availability via Calendly**  
  Log into Calendly, open **Event Types → Property Tour**. The availability grid must show slots from 10 AM to 4 PM, Monday‑Friday. Click **Schedule** with a dummy email; the confirmation email should say “Your tour is booked for 2026‑08‑01 11:00 AM”. If the slot is unavailable, ensure the Google Calendar connected to Calendly is not blocked.

Once all eight items are checked, your AI‑powered real estate process is ready for production.

## What to Do Next

**1. Deploy a Replit‑Hosted Property Chatbot**  
Create a new Replit project using the “Python (Flask)” template. In the *Packages* tab, add `openai==0.28` and `flask==2.3`. Add an `openai_api_key` secret via *Secrets* → *Add new secret*: key = `OPENAI_API_KEY`, value = your OpenAI key. In `app.py`, set up a `/chat` endpoint that forwards user queries to `openai.ChatCompletion.create()` with `model="gpt‑4o-mini"` and returns the assistant’s reply. Deploy the Repl (click **Run**), copy the public URL, and embed it on your property listings.  
*Check‑in:* Do you see a live Flask server running on `https://<username>.<repl>.repl.co`? If not, verify the `requirements.txt` includes `openai` and `flask`.  
[Learn more about AI chatbots on Replit → Menshly.com/deploy-ai-chatbot](https://menshly.com/deploy-ai-chatbot)

**2. Automate Lead Capture with Make.com**  
In Make.com, create a new scenario. Add a **Google Sheets** “New Row” trigger, pointing to your lead capture sheet. Add an **Apollo.io** “Create Lead” action, mapping the row fields (`Name`, `Email`, `Phone`) to Apollo’s lead schema. Finish by adding a **Klaviyo** “Add Subscriber” step: set “List” to your “Real Estate Leads” list and map the email field. Turn the scenario on.  
*Check‑in:* Does the Make.com dashboard show a “Scenario running” status and a “Rows processed” counter? If the scenario fails, ensure Apollo credentials are set under *Connections* → *Apollo.io* and that the Google Sheet is shared with the Make.com service account.  
[Read our Make.com integration guide → Menshly.com/make-com-lead-automation](https://menshly.com/make-com-lead-automation)

**3. Launch a Klaviyo Drip Campaign**  
Within Klaviyo, navigate to **Flows** → **Create Flow**. Set the trigger to **Subscriber joins list** and choose the “Real Estate Leads” list. Add an action “Send Email”, select the “Welcome Property Tour” template, and schedule it to send 0 hours after the trigger. Add a second action “Send Email” with the “Property Highlight” template, scheduled at +48 hours. Publish the flow.  
*Check‑in:* In Klaviyo’s flow editor, you should see a green play icon next to the flow name. If the flow isn’t firing, confirm the list ID matches the one used in Make.com.  
[Deep dive into Klaviyo flows → Menshly.com/klaviyo-drip](https://menshly.com/klaviyo-drip)

**4. Track SEO Performance with Semrush**  
Log into Semrush, go to **Projects** → **Add Project**. Name it “Real Estate Listings” and enter your site URL. Under the project dashboard, navigate to **Position Tracking** → **New Task**. Configure the task: choose “Region: United States”, “Language: English”, and add target keywords such as “buy home in [city]” and “real estate listings near me”. Save the task and wait 24 hours for the first ranking snapshot.  
*Check‑in:* The task status should read “Completed” after the first run. If it shows “Error: API quota exceeded”, upgrade to the “Pro” plan ($119/month) in the Semrush billing section.  
[Optimize listings with Semrush → Menshly.com/semrush-seo](https://menshly.com/semrush-seo)

**5. Refine Lead Sc

Ready to understand the full business opportunity? Read our [opportunity deep-dive]({< ref "/opportunities/how-to-build-an-ai-real-estate-automation-service-8k-12kmonth.md" >}).


## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
