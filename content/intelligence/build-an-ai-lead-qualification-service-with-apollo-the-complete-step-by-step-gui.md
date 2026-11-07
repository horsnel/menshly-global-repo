---
title: "Build an AI Lead Qualification Service with Apollo: The Complete Step-by-Step Guide"
date: 2026-11-05
category: "Implementation"
difficulty: "INTERMEDIATE"
readTime: "25 MIN"
excerpt: "In this guide you will build a fully automated lead qualification service that pulls raw prospects from Apollo, enriches and scores them with PhantomBuster, and delivers a ready‑to‑contact list to you..."
image: "/images/articles/intelligence/find-qualify-and-optimize-leads-with-apollo-and-phantombuster.png"
heroImage: "/images/heroes/intelligence/find-qualify-and-optimize-leads-with-apollo-and-phantombuster.png"
relatedOpportunity: "/opportunities/how-to-build-an-ai-lead-generation-25k-35kmonth/"
relatedPlaybook: "/playbooks/api-credentials/"
---

In this guide you will build a fully automated lead qualification service that pulls raw prospects from Apollo, enriches and scores them with PhantomBuster, and delivers a ready‑to‑contact list to your sales team—all within a single, repeatable pipeline. By the end of the walkthrough you will have a production‑ready workflow that can ingest thousands of leads per hour, apply AI‑driven scoring, and push the highest‑quality prospects straight into your CRM or email marketing stack.  

This is a deep‑execution manual, not a high‑level overview. Every step will be broken into numbered actions, with explicit button names, menu paths, and configuration values. You’ll learn how to spin up an Apollo API key, set up PhantomBuster automation, and integrate the output with Zapier or Make.com to update a Google Sheet or your Salesforce instance in real time. We’ll also cover how to monitor the pipeline, troubleshoot common errors, and tune scoring thresholds to maximize conversion rates.

Expect to spend roughly 10–12 hours over the course of a week to fully complete the setup, including initial data imports, testing, and refining the scoring logic. The total cost will be under $200: $59/month for an Apollo Pro plan, $49/month for a PhantomBuster Basic plan, and $39/month for a Make.com Essential plan.  

This is the execution guide for the **How to Build an AI Lead Generation ($25K‑$35K/Month)** business we outlined in our opportunity deep‑down.  

Ready to understand the full business opportunity? Read our [opportunity deep‑dive]({< ref "/opportunities/how-to-build-an-ai-lead-generation-25k-35kmonth.md" >}).

## Prerequisites

**Prerequisites**

Before you start building the AI‑powered lead qualification service, make sure you have the following accounts, tools, and resources in place. Each item is listed with its exact purpose, monthly cost, and free‑tier limits so you can budget accurately.

- **Apollo.io** – Professional plan (B2B sales intelligence)
  - **Cost:** $49 USD/month
  - **Free tier:** 30 000 contact searches per month, 1 000 email credits
- **PhantomBuster** – Automation platform for LinkedIn outreach
  - **Cost:** $39 USD/month (Basic)
  - **Free tier:** 25 API calls/day, 1 automation workflow
- [**Notion**](https://notion.so/) – Workspace & documentation
  - **Cost:** Free tier (no charge)
  - **Free tier limit:** Unlimited pages, limited file uploads
- **Zapier** – App‑to‑app automation (connect Apollo, PhantomBuster, email, etc.)
  - **Cost:** $19.99 USD/month (Starter)
  - **Free tier:** 100 tasks/month, 5 Zaps
- **Calendly** – Scheduling for discovery calls
  - **Cost:** Free tier (no charge)
  - **Free tier limit:** 1 calendar, 1 event type
- **Slack** – Team communication (optional)
  - **Cost:** Free tier
  - **Free tier limit:** 10 000 messages/month, 10 integrations

**Estimated upfront cost**  
Total monthly subscription cost: **$49 + $39 + $19.99 = $107.99 USD**.  
(If you opt for free tiers, you can run a pilot for $0, but you’ll hit limits within 1–2 weeks.)

**Table of Tools**

| Tool        | Purpose                                 | Cost (USD/month) | Free Tier Limit                         |
|-------------|-----------------------------------------|------------------|----------------------------------------|
| Apollo.io   | B2B contact data & email outreach       | 49               | 30 000 searches, 1 000 email credits   |
| PhantomBuster | LinkedIn automation & data extraction | 39               | 25 calls/day, 1 workflow                |
| Notion      | Project documentation & knowledge base | 0                | Unlimited pages, limited uploads        |
| Zapier      | Workflow automation between services    | 19.99            | 100 tasks, 5 Zaps                      |
| Calendly    | Scheduling discovery calls             | 0                | 1 calendar, 1 event type               |

**Preparation Checklist**

1. Sign up for Apollo.io and upgrade to the Professional plan.  
2. Create a PhantomBuster account and enable the “LinkedIn Search” and “LinkedIn Connect” APIs.  
3. Set up a Notion workspace titled “Lead Qualification Pipeline”.  
4. Create a Zapier account and install the Apollo, PhantomBuster, and Gmail integrations.  
5. Verify your Calendly profile and create a “Discovery Call” event type.  

Once these accounts are configured, you’ll be ready to move on to the data ingestion and qualification steps.

## Step 1: Setup and Configuration  
**Objective** – Create a clean, reproducible development environment, register for Apollo and PhantomBuster, and securely store the API credentials that the rest of the pipeline will consume.

> **Time estimate:** 20–25 minutes

---

### 1.1 Create the project directory

1. Open a terminal on your workstation or use Replit’s built‑in shell.  
2. Execute the following commands exactly:

```bash
mkdir lead-qualifier
cd lead-qualifier
git init
```

> **Expected output**  
> ```
> Initialized empty Git repository in /home/user/lead-qualifier/.git/
> ```

3. Verify the current working directory:

```bash
pwd
```

> **You should see** `/home/user/lead-qualifier` or the equivalent path on your system.  
> **If you do not,** you are not in the correct directory. Use `cd` to navigate to the folder you just created.

---

### 1.2 Set up a virtual environment (Python) or Node.js project

> We’ll use Node.js because Apollo’s SDK is JavaScript‑friendly and PhantomBuster offers a REST API that we’ll call from Node.

```bash
# Ensure Node 18+ is installed
node -v
# If not, install via nvm
nvm install 18
nvm use 18

# Initialize npm project
npm init -y
```

> **Expected output**  
> ```
> added 1 package, removed 0 packages, changed 0 packages
> ```

---

### 1.3 Install dependencies

```bash
npm install axios dotenv
```

> **Expected output**  
> ```
> added 2 packages, removed 0 packages, changed 0 packages
> ```

- `axios` – HTTP client for calling the APIs.  
- `dotenv` – Loads environment variables from a `.env` file.

---

### 1.4 Create a .gitignore

```bash
echo "node_modules/" > .gitignore
echo ".env" >> .gitignore
```

> **Check**: `cat .gitignore`  
> **You should see**  
> ```
> node_modules/
> .env
> ```

---

### 1.5 Register for Apollo

1. Navigate to <https://www.apollographql.com> and click **Sign up**.  
2. Use a Gmail address, create a password, and verify via email.  
3. Once logged in, go to **Account Settings** → **API Keys**.  
4. Click **Generate API Key**, name it `LEAD_QUALIFIER_KEY`, and copy the key.

> **Interactive Check‑in**  
> *Do you see the “API Keys” tab under Account Settings?*  
> If not, go to the top‑right menu → **Profile** → **API Keys**.  
> If you still can’t locate it, Apollo may have moved the UI; check the help center for “API key management”.

5. Store the key in a secure location; you’ll paste it into a `.env` file later.

---

### 1.6 Register for PhantomBuster

1. Open <https://phantombuster.com> and click **Sign up**.  
2. Verify your email; you’ll receive a confirmation link.  
3. After login, click the **API** icon in the left sidebar.  
4. Click **Generate New API Key**, name it `PHANTOMBUSTER_KEY`, and copy the key.

> **Expected output** – a 32‑character alphanumeric string (e.g., `d4f7e2a1b3c9...`).  
> **If you see a 404 error** while accessing the API page, your browser’s cache is stale. Clear cache or try incognito mode.

---

### 1.7 Create the `.env` file

In the project root, run:

```bash
touch .env
```

Open `.env` in your editor and paste:

```
APOLLO_API_KEY=YOUR_APOLLO_KEY_HERE
PHANTOMBUSTER_API_KEY=YOUR_PHANTOMBUSTER_KEY_HERE
```

> Replace `YOUR_APOLLO_KEY_HERE` and `YOUR_PHANTOMBUSTER_KEY_HERE` with the keys you just copied.

> **Check**: `cat .env`  
> **You should see** the two lines above with the keys inserted.

---

### 1.8 Verify environment variable loading

Create a small test script `test-env.js`:

```js
require('dotenv').config();
console.log('Apollo key:', process.env.APOLLO_API_KEY);
console.log('PhantomBuster key:', process.env.PHANTOMBUSTER_API_KEY);
```

Run:

```bash
node test-env.js
```

> **Expected output**  
> ```
> Apollo key: d4f7e2a1b3c9...
> PhantomBuster key: a1b2c3d4e5f6...
> ```

If you see `undefined` for either variable, the `.env` file is not in the project root or the keys were omitted. Re‑open `.env`, verify the spelling of `APOLLO_API_KEY` and `PHANTOMBUSTER_API_KEY`, and try again.

---

### 1.9 Create the initial API wrapper files

Create a folder `src` and files `apollo.js` and `phantombuster.js`.

```bash
mkdir src
touch src/apollo.js src/phantombuster.js
```

**src/apollo.js**

```js
const axios = require('axios');
require('dotenv').config();

const apolloClient = axios.create({
  baseURL: 'https://api.ap

## Step 2: Build the Core System  
**Objective:** Wire Apollo, PhantomBuster, and an AI‑driven qualification engine into a single, repeatable pipeline that pulls raw leads, enriches them, and outputs a ready‑to‑contact list.  

> **NOTE:** Every section below contains an *interactive check‑in*. If you do not see the element described, double‑check the navigation path or return to the previous step.  

---

### 2.1 Initiate an Apollo Lead Search  
1. Log into **Apollo** (https://app.apollo.io).  
2. From the left‑hand menu, click **“Search”** → **“Leads”**.  
3. In the search bar, type a query such as `industry:technology AND location:United States AND title:“Product Manager”`.  
4. Click the **“Run”** button (top‑right).  
5. When the results load, click **“Download”** (icon: downward arrow) → **“CSV”**.  
6. Save the file as `lead_search.csv` in your local workspace.  

> **Check‑in:** Do you see the CSV download option? The downloaded file should contain columns: *First Name, Last Name, Email, Company, Title, LinkedIn URL*.  

---

### 2.2 Export Leads via Apollo API  
Apollo’s API allows programmatic access; we’ll use it to fetch a fresh batch each run.

1. In Apollo, click your avatar → **“Settings”** → **“API”**.  
2. Click **“Generate New Key”**.  
3. Copy the key; it will be displayed only once.  
4. Open [**Replit**](https://replit.com/refer/egwuokwor) (https://replit.com).  
5. Create a new **Python** repl named `apollo_export`.  
6. In the repl’s `.env` file, add:  
   ```
   APO_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```
7. In `main.py`, paste the following code:

   ```python
   import os, requests, csv

   API_KEY = os.getenv("APO_API_KEY")
   URL = "https://api.apollo.io/v1/companies/search"

   headers = {
       "Authorization": f"Bearer {API_KEY}",
       "Content-Type": "application/json"
   }

   params = {
       "q": "industry:technology AND location:United States AND title:\"Product Manager\"",
       "page": 1,
       "page_size": 100
   }

   resp = requests.get(URL, headers=headers, params=params)
   data = resp.json()

   with open("apollo_leads.csv", "w", newline="") as f:
       writer = csv.writer(f)
       writer.writerow(["First Name", "Last Name", "Email", "Company", "Title", "LinkedIn"])
       for lead in data["companies"]:
           writer.writerow([lead["first_name"], lead["last_name"], lead["email"],
                            lead["company"], lead["title"], lead["linkedin_url"]])
   print("CSV written: apollo_leads.csv")
   ```

8. Click the **“Run”** button.  
9. Verify that `apollo_leads.csv` appears in the **Files** pane.  

> **Check‑in:** Do you see the console output “CSV written: apollo_leads.csv”? The file should contain 100 rows unless the API returned fewer.  

> **Error Scenario:** If you see `401 Unauthorized`, the API key is wrong. Re‑generate the key in Apollo and update the `.env` file.  

---

### 2.3 Enrich Leads with PhantomBuster  
PhantomBuster will scrape LinkedIn for profile details that Apollo may miss.

1. Sign into **PhantomBuster** (https://phantombuster.com).  
2. Click **“Phantoms”** → **“New Phantom”**.  
3. Search for **“LinkedIn Profile Scraper”** and select it.  
4. In the **Configuration** panel:  
   - **Input**: Upload `apollo_leads.csv`.  
   - **CSV Column Name**: `LinkedIn`.  
   - **Output**: `linkedin_enriched.csv`.  
   - **Maximum API Calls**: `200`.  
5. Under **“Advanced Settings”**, set **“Use Proxy”** to `True` (Plan: `PhantomBuster Pro – $79/month`).  
6. Click **“Run”** → **“Schedule”** → **“19:00 UTC”** (or click **“Run Now”** for immediate execution).  



## Step 3: Test and Validate

In this phase we confirm that the Apollo‑PhantomBuster pipeline is pulling the correct data and routing it to your downstream stack (e.g., Make.com → Notion → Klaviyo). Follow the checklist below before you hand the service off to a client.

### 3.1 Quick‑start test run

1. **Trigger a manual run in PhantomBuster**  
   - Navigate to the **Phantom** you created in the dashboard.  
   - Click **“Run”** (top‑right).  
   - In the **Run Settings** pop‑up, set **“Iterations”** to **3** and leave **“Delay”** at the default **5 s**.  
   - Click **“Run”** again to start.  
   > *Interactive check‑in:* Do you see a green “Running” indicator next to the Phantom? If not, verify that your API key is enabled in **Settings → API Keys**.

2. **Verify the output in the Phantom’s log**  
   - Once finished, click **“View Log”**.  
   - You should see **three JSON objects** printed, each containing at least the fields `firstName`, `lastName`, `email`, and `company`.  
   ```json
   {"firstName":"Jane","lastName":"Doe","email":"jane.doe@example.com","company":"Acme Corp"}
   ```  
   > *Error scenario:* If the log shows `{"error":"Invalid credentials"}`, the Apollo API key in your Phantom’s settings is wrong. Go to **Settings → API Keys → Apollo** and re‑enter the key.

3. **Check the Make.com webhook**  
   - In Make.com, open the scenario that receives the Phantom payload.  
   - Click **“Run once”** and watch the **HTTP module**.  
   - The JSON payload should mirror the log output.  
   - The next module (e.g., **Notion → Create a database item**) should return a **200 OK** response.  
   > *If you see a 401 status*, the Make.com webhook URL was copied incorrectly. Re‑copy it from **Scenario → Settings → Webhook URL**.

4. **Confirm data in Notion**  
   - Open the Notion database you configured.  
   - There should be three new rows with the names and emails you saw in the log.  
   > *If rows are missing*, the Notion API token in the Make.com scenario is expired. Regenerate it under **Notion → Settings → API Tokens**.

5. **Validate Klaviyo tagging**  
   - In Klaviyo, go to **Lists & Segments → Segments**.  
   - Search for the segment you created (`New Apollo Leads`).  
   - It should list the three test contacts.  
   > *If the segment is empty*, check that the **“Add to List”** action in Make.com is pointing to the correct list ID.

### 3.2 5‑Point Test Checklist

| # | Item | Expected Result | How to Verify |
|---|------|-----------------|---------------|
| 1 | Phantom runs without errors | Green “Success” badge | Check **Run Log** |
| 2 | JSON payload contains all required fields | `firstName`, `lastName`, `email`, `company` | Inspect log entries |
| 3 | Make.com HTTP module returns 200 OK | Status code 200 | Look at module output |
| 4 | Notion database records are created | Three new rows with matching data | Open database |
| 5 | Klaviyo segment contains new contacts | Segment shows 3 members | View segment details |

### 3.3 Common Pitfalls & Fixes

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Phantom stops after 1 iteration | “Maximum requests per hour” limit reached | Increase **“Iterations”** or wait 1 h |
| Make.com fails with 403 | Wrong API token for Notion | Regenerate token in Notion and update in Make |
| Klaviyo shows “Invalid email” errors | Email format wrong in Phantom | Add a regex filter in Make before sending to Klaviyo |
| Data missing in Notion | Notion database schema mismatch | Update Notion schema to match the JSON keys |

Once all five checklist items pass and no errors surface, the pipeline is production‑ready. You can now scale to 100‑plus leads per run with confidence.

## Step 4: Add Advanced Features  
*(AI enrichment, error handling, routing, monitoring – production‑ready)*  

Below you’ll find a detailed, copy‑and‑paste‑ready walkthrough to turn the core system into a robust, production‑grade service. Every configuration change is spelled out, every expected UI state is described, and interactive check‑ins keep you on track.  

---

### 4.1 AI‑Driven Lead Enrichment (Replit + ChatGPT)

1. **Create a Replit workspace**  
   - Open Replit.com → “Create a new repl” → choose “Python” → name it `lead-enrichment`.  
   - Click **Create repl**.  
   - Do you see the **Shell** tab? You should see a terminal that says `Python 3.10`. If not, refresh the page.

2. **Add the OpenAI SDK**  
   ```bash
   pip install openai
   ```  
   - In the **Shell**, run the command above.  
   - Expected output: `Successfully installed openai-<latest-version>`.

3. **Create a `.env` file** with your OpenAI key (replace `<YOUR_KEY>`).  
   ```dotenv
   OPENAI_API_KEY=<YOUR_KEY>
   ```  
   - In the Replit file explorer, click **New File** → name it `.env`.  
   - Paste the content and save.

4. **Write the enrichment script** (`main.py`):  
   ```python
   import os, json, openai
   from dotenv import load_dotenv

   load_dotenv()
   openai.api_key = os.getenv("OPENAI_API_KEY")

   def enrich_lead(lead):
       prompt = f"""
       Enrich the following lead profile with:
       • Company size (small/medium/large)
       • Annual revenue estimate
       • Key pain points (3 bullets)
       • Suggested next step

       Lead data:
       {json.dumps(lead, indent=2)}
       """
       response = openai.ChatCompletion.create(
           model="gpt-4",
           messages=[{"role":"user","content":prompt}],
           temperature=0.2,
           max_tokens=250
       )
       return json.loads(response.choices[0].message.content)

   if __name__ == "__main__":
       sample_lead = {"name":"Acme Corp","industry":"Manufacturing","location":"Berlin"}
       enriched = enrich_lead(sample_lead)
       print(json.dumps(enriched, indent=2))
   ```  
   - Save the file.

5. **Run a test**  
   - In the **Shell**, type `python main.py`.  
   - Expected output: a JSON block with the enriched fields.  
   - If you see an `AuthenticationError`, double‑check the `.env` key.

6. **Expose a tiny API via Replit’s built‑in web server**  
   ```python
   from flask import Flask, request, jsonify

   app = Flask(__name__)

   @app.route("/enrich", methods=["POST"])
   def enrich():
       lead = request.json
       enriched = enrich_lead(lead)
       return jsonify(enriched)

   if __name__ == "__main__":
       app.run(host="0.0.0.0", port=8000)
   ```  
   - Add `flask` to the **Shell**: `pip install flask`.  
   - Restart the Replit (click **Run**).  
   - Confirm the **Running** badge shows `https://lead-enrichment.username.repl.co`.

> **Interactive Check‑in**  
> Do you see the Replit *run* button turning green and the URL in the address bar? If you don’t, click **Run** again and wait until the “Running” status appears.

---

### 4.2 Error Handling in PhantomBuster

1. **Open your Phantom** that scrapes LinkedIn profiles.  
2. In the **Advanced Settings** panel → **Error Handling**:  
   - **Retry Count**: `3`  
   - **Retry Delay**: `30` seconds  
   - **Timeout**: `120` seconds  
   - **Error Log**: `Save to Google Sheet (link below)`.  
   - Click **Save**.

3. **Set up a Google Sheet** (`Lead Errors`) with columns: `Timestamp`, `Lead ID`, `Error Message`, `Retry Count`.  
   - In PhantomBuster, choose “Save to Sheet” and paste the sheet URL.

4. **Configure the “On Error” webhook** to hit a Zapier endpoint:  
   - Go to Zapier → create a new Zap → trigger “Webhooks

## Step 5: Deploy to Production  

Below is a practical, production‑ready deployment workflow for the Apollo‑PhantomBuster lead‑qualification service.  
It assumes you have already built the core API on Replit, tested it locally, and added advanced features such as scheduled crawls and email triggers.  
We’ll move the service to a production environment on **Hostinger Cloud VPS** (Node 14, 1 GB RAM) and expose it behind an Nginx reverse proxy.  
The workflow also shows how to wire Apollo and PhantomBuster credentials into the environment and how to verify the deployment with a quick test call.

> **Prerequisites**  
> * A Hostinger account with a Cloud VPS (Plan: “Basic 1 GB” – $5/month).  
> * SSH access to the VPS (public key added to Hostinger’s SSH keys).  
> * Replit project URL and GitHub repo URL.  
> * Apollo API key (`APOLLO_API_KEY`) and PhantomBuster API key (`PHANTOM_BUSTER_KEY`).  

### 5.1 Provision the VPS

1. Log into Hostinger’s control panel → **Cloud VPS** → **Create New VPS**.  
   * **Name**: `lead-svc-prod`  
   * **Region**: `United States (N. Virginia)`  
   * **CPU**: `1 vCPU`  
   * **RAM**: `1 GB`  
   * **Storage**: `20 GB SSD`  
   * **OS**: `Ubuntu 22.04 LTS`  
   * **Password**: generate a strong password or use SSH key.  
   Click **Create**.

2. Once the VPS is ready, click **Manage** → **SSH** → **Open Terminal**.  
   You should see a terminal prompt:  

   ```
   ubuntu@lead-svc-prod:~$
   ```

   *If you see “Connection timed out” or “Authentication failed”, double‑check that the SSH key is correctly uploaded in Hostinger and that the VPS firewall allows port 22.*

### 5.2 Set Up the Runtime

```bash
# Update package index
sudo apt update && sudo apt upgrade -y

# Install Node.js 14
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt install -y nodejs

# Verify installation
node -v   # should output v14.x.x
npm -v    # should output 6.x.x
```

### 5.3 Clone the Repository

```bash
# Install Git if missing
sudo apt install -y git

# Clone the repo
git clone https://github.com/your-org/lead-qualification-service.git
cd lead-qualification-service
```

*Interactive check‑in:*  
Do you see the `package.json` file in the current directory?  
If not, verify the repo URL and that you’re in the correct branch (`main`).

### 5.4 Install Dependencies & Configure Secrets

```bash
# Install dependencies
npm ci

# Create .env file
cat <<EOF > .env
PORT=3000
APOLLO_API_KEY=YOUR_AU_KEY
PHANTOM_BUSTER_KEY=YOUR_PB_KEY
SMTP_HOST=mail.example.com
SMTP_PORT=465
SMTP_USER=mailer@example.com
SMTP_PASS=superSecret
EOF
```

> **Error:** If you receive `npm ERR! code EACCES`, run the install command with `sudo`.  
> **Fix:** `sudo npm ci`.

### 5.5 Start the Service with PM2

```bash
# Install PM2 globally
sudo npm install -g pm2

# Start the app
pm2 start src/index.js --name lead-service --watch

# Save the process list and configure startup
pm2 startup systemd
sudo env PATH=\$PATH:/usr/bin /usr/local/lib/node_modules/pm2/bin/pm2 startup systemd -u ubuntu --hp /home/ubuntu
pm2 save
```

*Interactive check‑in:*  
Run `pm2 list`.  
You should see an entry `lead-service` with status `online`.  
If status is `errored`, run `pm2 logs lead-service` to view stack trace.

### 5.6 Configure Nginx Reverse Proxy

```bash
# Install Nginx
sudo apt install -y nginx

# Create site config
sudo bash -c 'cat > /etc/nginx/sites-available/lead-service <<EOF
server {
    listen 80;
    server_name lead.example.com;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF'

# Enable site
sudo ln -s /etc/nginx/sites-available/lead-service /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

*Interactive check‑in:*  
Open `http://lead.example.com/health` in a browser.  
You should see JSON: `{ "status": "ok" }`.  
If you see a 502 Bad Gateway, verify that the Node app is listening on the expected port.

### 5.7 Schedule PhantomBuster Craw

## Step 6: Scale and Grow

### Step 6: Scale and Grow  

| Milestone | Clients | Key Tasks | Resources | KPI | Expected Outcome |
|-----------|---------|-----------|-----------|-----|------------------|
| 1 → 3 | 1‑3 | Tight‑en qualification criteria, add AI‑video outreach (Fliki AI) | Apollo, PhantomBuster, Fliki AI | Avg. CPL  < $30 | Stable pipeline, 30 % close rate |
| 3 → 5 | 3‑5 | Deploy Make.com workflow, hire junior automation engineer | Apollo API key, Make.com, Notion | Avg. turnaround 12 h | 3‑day lead response |
| 5 → 10+ | 5‑10 | Implement pricing tiers, automate billing via Stripe, optimize margin | Apollo, Zapier, Klaviyo | 50 % margin | Monthly recurring revenue |
| 10+ | 10+ | Expand team (sales, support), upgrade PhantomBuster to 1,000 requests/day | Apollo, PhantomBuster, Hostinger | CAC < $200 | Scale to 50+ clients |

#### 6.1 Tighten Qualification and Add AI‑Video Outreach  
1. **Apollo** – Open the “Prospecting” tab → “Filters.”  
   - Set “Industry = Technology” → “Title = Product Manager.”  
   - Toggle “Lead Score” slider to > 70.  
   - *Check‑in:* Do you see the “Lead Score” filter? It should be next to “Title.”  
2. [**Fliki AI**](https://fliki.ai?referral=noah-wilson-w84be4) – Create a video template.  
   - In the dashboard, click “+ New Video” → “Text to Video.”  
   - Paste your outreach script and click “Generate.”  
   - Download MP4.  
   - *Error:* If the script exceeds 200 words, Fliki will return “Payload size too large.” Reduce the script or use “Split” to create two videos.  
3. Attach the video to your Apollo outreach email.  
   - In the email template editor, click “Insert Media” → “Upload Video.”  
   - Select the Fliki MP4.  
   - *Expected output:* Video appears inline in the email preview.

#### 6.2 Upgrade PhantomBuster & Automate with Make.com  
1. **PhantomBuster** – Log in → “Account.”  
   - Upgrade to “Pro” plan (USD $75/month).  
   - Set “Max parallel requests = 5” → “Delay between requests = 500 ms.”  
   - *Check‑in:* In the PhantomBuster console, you should see “Daily limit: 200 requests.”  
2. [**Make.com (formerly Integromat)**](https://www.make.com/en/register?pc=menshly) – Create a new scenario.  
   - Trigger: “Apollo – New Contact.”  
   - Action 1: “Filter” → “Qualification score > 80.”  
   - Action 2: “Create record” → “Notion – Lead table.”  
   - Action 3: “Send email” → “Klaviyo – Send Email.”  
   - *Interactive:* In the scenario editor, click “Add an action” → search “Notion.” Select the “Create a database item” module and map fields.  
3. **Error handling:** If you receive “API rate limit exceeded” from Apollo, add a “Delay” module (set 2 s) before the next request.  

#### 6.3 Hire a Junior Automation Engineer  
1. Post a job on LinkedIn.  
2. Require experience with Apollo API, PhantomBuster, and Make.com.  
3. Sign a 6‑month NDA, provide the Apollo API key (from “Settings” → “API”) and PhantomBuster API token (found under “Account” → “API”).  

#### 6.4 Optimize Pricing & Margins  
1. Set up a tiered pricing model in Stripe:  
   - Basic $99/month (3 leads

## Cost Breakdown

| Item                | Free Tier                                       | Paid Tier (Monthly) | When to Upgrade                                                                                              |
|---------------------|-------------------------------------------------|---------------------|--------------------------------------------------------------------------------------------------------------|
| **Apollo**          | 150 lead credits / month; 5 API calls / day     | Standard: $59       | When you need > 150 leads/month or > 5 API calls/day (e.g., 300 leads/month)                                 |
| **PhantomBuster**   | 10 tasks / month; 3 concurrent tasks           | Standard: $59       | When you exceed 10 tasks/month or need > 3 concurrent runs (e.g., 30 tasks/day)                                |
| **Make.com**        | 500 operations / month; 1 GB storage           | Basic: $49          | When you need > 500 operations/month or > 1 GB storage (e.g., 2,000 operations)                              |
| **Zapier**          | 100 tasks / month; 5 min polling interval       | Starter: $19.99     | When you need > 100 tasks/month or faster polling (e.g., 500 tasks)                                           |
| **ChatGPT API**     | 100 000 tokens / month (free tier)              | $0.02/1 k tokens (gpt‑3.5) | When you exceed 100 000 tokens/month (e.g., 500 leads × 5 k tokens = 2.5 M tokens → ~$50)                |
| **Hostinger**       | 512 MB RAM, 1 GB storage (shared)               | Cloud Hosting: $9.99| When you need more RAM, bandwidth, or SSL (e.g., 1 GB RAM, 10 GB bandwidth)                                   |
| **Replit**          | Free (200 MB RAM, 1 GB storage)                 | Hacker: $7          | When you need 512 MB RAM, 2 GB storage, or private repos (e.g., production backend)                          |
| [**Canva**](https://www.canva.com/)           | 5 GB storage, basic templates                  | Pro: $12.99         | When you need brand kits, custom fonts, or more templates (e.g., 20 email designs per client)                 |
| **Klaviyo**         | 2 500 contacts; 500 email sends / month         | $30 (5 000 contacts) | When you have > 2 500 contacts or > 500 sends (e.g., 10 000 contacts)                                        |
| **Buffer**          | 3 social accounts; 10 posts/month              | Pro: $12            | When you need > 3 accounts or > 10 posts/month (e.g., 10 accounts)                                            |

### Monthly Cost Analysis

| Scale          | Typical Usage                                   | Total Monthly Cost |
|----------------|-------------------------------------------------|--------------------|
| **Solo**       | 200 leads/month, 1 client, 1 API call per lead  | **$59 (Apollo)** + **$59 (PhantomBuster)** + **$7 (Replit)** + **$12 (Buffer)** + **$0.20 (ChatGPT)** ≈ **$137** |
| **5 Clients**  | 1,000 leads/month, 5 API calls per lead, 1 GB storage | **$59 (Apollo)** + **$59 (PhantomBuster)** + **$49 (Make.com)** + **$19.99 (Zapier)** + **$7 (Replit)** + **$12 (Buffer)** + **$12.99 (Canva)** + **$30 (Klaviyo)** + **$50 (ChatGPT)** ≈ **$400** |
| **10+ Clients**| 5,000 leads/month, 10 API calls per lead, 10 GB storage | **$79

## Production Checklist

Before you switch your AI Lead Qualification Service to “live” mode, run through this checklist to ensure every component is correctly configured and fully tested.

- **[ ] Apollo Integration is Live**  
  *Verify the API key is stored in your environment variable `APOLLO_API_KEY` and that a test request to `https://api.apollo.io/v1/people/search` returns a 200 status with at least one record.*  
  *If you receive a 401 error, double‑check the key copy‑paste and the “Read” scope in Apollo’s developer portal.*

- **[ ] PhantomBuster Script is Triggered**  
  *Open PhantomBuster, select the “LinkedIn Lead Gen” template, and confirm the trigger URL is set to your webhook endpoint (`https://<your‑domain>/phantombuster/webhook`).*  
  *Run a manual trigger; the console should log “LinkedIn data fetched: 50 profiles.” If not, confirm the LinkedIn credentials are still valid.*

- **[ ] Data Pipeline is Functional**  
  *In Replit, execute `python pipeline.py` manually. The script should output “Pipeline processed 50 leads.” No connection errors should appear.*  
  *If errors arise, check that the environment variables `REPLIT_DB_URL` and `APOLLO_API_KEY` are correctly loaded.*

- **[ ] Email Qualification Workflow is Configured**  
  *Navigate to Klaviyo → Flow Builder → “Lead Qualifier”. Confirm the trigger is “Webhook received” and the email template contains the dynamic merge tag `{{lead.score}}`.*  
  *Send a test webhook; the email preview should render a score between 0‑100.*

- **[ ] Rate Limits are Respected**  
  *In Apollo, confirm “Requests per minute” is set to 50. In PhantomBuster, ensure the “Throttle” setting equals 5 requests/sec. If you exceed limits, the logs will show “429 Too Many Requests.”*

- **[ ] Logging & Alerting are Enabled**  
  *Check the CloudWatch dashboard (or Replit’s console) for a live stream of log entries. Alerts should be configured to email `ops@menshly.global` when a failure exceeds three consecutive attempts.*

- **[ ] Security Hardening is Complete**  
  *Verify that your API keys are stored in AWS Secrets Manager and not in plaintext. Confirm HTTPS is enforced on all endpoints (`https://`).*  
  *Run a quick OWASP ZAP scan; no critical vulnerabilities should be reported.*

- **[ ] Backup & Recovery Plan is Tested**  
  *Restore a recent snapshot from your PostgreSQL backup (`pg_dump`) into a staging environment. Confirm that the restored database matches the live schema.*  
  *If restoration fails, the error log should indicate missing extensions; install them with `CREATE EXTENSION IF NOT EXISTS citext;`.*

- **[ ] Performance Benchmark is Met**  
  *Load test the webhook endpoint with 200 concurrent requests using k6. Target response time < 300 ms. If latency exceeds, investigate the bottleneck in the `process_leads()` function.*  

- **[ ] Documentation is Updated**  
  *Confirm that the README in your repository includes the latest API endpoints, environment variables, and a “Troubleshooting” section. If a user cannot find the “API key” entry, update the doc accordingly.*

Once every box is ticked, you’re ready to roll out the service to real clients. Happy hunting!

## What to Do Next

**Expand to Multi‑Channel Outreach**  
After you’ve built your Apollo + PhantomBuster pipeline, integrate Zapier to push qualified leads into both ActiveCampaign and Klaviyo. In Zapier, create a “New Apollo Contact” trigger, then add two actions: “Create/Update Contact” in ActiveCampaign (use “Email Address” and “First Name” fields) and “Add Subscriber” in Klaviyo (include the same fields). Verify that the first lead lands in both inboxes by checking the ActiveCampaign Dashboard and Klaviyo’s “Subscribers” tab. If you see “No records found,” double‑check that the Zap’s “Data” mapping uses the correct fields and that both accounts are authenticated. For more on multi‑channel syncing, see our guide on [Seamless CRM & Email Integration](https://menshly.com/lead-automation-analytics).

**Automate Voice‑Based Follow‑Ups**  
Use [Vapi](https://vapi.ai/) to send AI‑generated voice messages to leads that haven’t responded after the initial email. In the Vapi console, create a “Lead Follow‑Up” flow, connect it to your Apollo contact list via a webhook, and set the greeting to “Hi {{first_name}}, this is Menshly AI…”. Enable the “Send to Phone” action and map the lead’s phone number. Test by triggering the flow on a single lead; the call log in Vapi should show “Delivered.” If you encounter “Invalid phone number,” confirm the E.164 format in Apollo. Learn how to personalize voice scripts in our [AI Voice Sales Playbook](https://menshly.com/ai-voice-sales).

**Visualize Lead Health with [Semrush](https://www.semrush.com/) and Notion**  
Export the Apollo contact list to a CSV and import it into Semrush’s “Domain Analytics” to assess lead domain authority. In Notion, create a “Lead Health Dashboard” template: add a “Table” block linked to the CSV, then embed a Semrush “Organic Search” chart via the “Embed” block. Use the “Filter” function to show only leads with Domain Authority > 40. If the chart fails to load, ensure your Semrush API key is correctly entered under “Settings → API.” For advanced visualization, check out our [Lead Health Dashboard Setup](https://menshly.com/ai-sales-dashboard).

**Deploy a Replit AI Chatbot for Real‑Time Qualification**  
Spin up a new Replit project (Python) and clone the Apollo‑PhantomBuster integration API. Add a Flask endpoint that receives a lead’s email, calls Apollo’s “Get Contact” API, and returns a JSON response. Wrap the logic in an AI prompt using OpenAI’s “text‑davinci‑003” to generate a qualification score. Deploy the Replit app, copy its HTTPS URL, and expose it via Make.com’s “Webhooks” trigger. In Make.com, set a “Webhook → New Lead” scenario, then route the JSON to a “Text to Speech” step with [ElevenLabs](https://elevenlabs.io/) to read the score aloud. Test by submitting a lead email; the chatbot should reply with “Qualified: 78%.” For a deeper dive, read our [AI Chatbot Deployment Guide](https://menshly.com/ai-chatbot-setup).

**Schedule Live Demo Calls with Calendly and Loom**  
Once leads pass the qualification threshold, automatically create a Calendly event. In Zapier, add a “Create Event” action with the “Event Type” set to “30‑Minute Demo.” Map the lead’s name and email to the event’s attendee fields. Add a “Send Email” action via Mailchimp (or your preferred tool) with a Loom recording attached that explains next steps. Verify that the Calendly link appears in the email body and that the Loom video plays correctly. If the email fails to send, confirm your Mailchimp API key and that the attachment path is correct. Explore our [Scheduling Automation Playbook](https://menshly.com/scheduling-automation) for additional tips.

Ready to understand the full business opportunity? Read our [opportunity deep-dive]({< ref "/opportunities/how-to-build-an-ai-lead-generation-25k-35kmonth.md" >}).


## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
