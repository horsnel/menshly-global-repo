---
title: "Build an AI Legal Document Management Service with LawGeex: The Complete Step-by-Step Guide"
date: 2026-11-24
category: "Implementation"
difficulty: "INTERMEDIATE"
readTime: "25 MIN"
excerpt: "*Section content pending review.*"
image: "/images/articles/intelligence/create-edit-and-optimize-legal-documents-with-lawgeex-and-contractbook.png"
heroImage: "/images/heroes/intelligence/create-edit-and-optimize-legal-documents-with-lawgeex-and-contractbook.png"
relatedOpportunity: "/opportunities/how-to-build-an-ai-legal-document-automation-service-48k-55kmonth/"
---



## Prerequisites

*Section content pending review.*


## Step 1: Setup and Configuration

*Section content pending review.*


## Step 2: Build the Core System

Below we assemble the infrastructure that turns raw legal text into an AI‑driven contract‑review service.  
All commands are valid in a Linux‑based environment (Ubuntu 22.04).  
If you’re using [Replit](https://replit.com/refer/egwuokwor), paste the `Dockerfile` and `docker-compose.yml` into the workspace and run `replit run` to spin up the stack.

---

### 2.1. Create the Project Repository

1. **Open a terminal** (or Replit console).  
2. **Clone the starter repo**:  
   ```bash
   git clone https://github.com/menshly/legal‑ai‑core.git
   cd legal‑ai‑core
   ```  
   *The repo contains the base Flask API, Docker config, and sample contract templates.*

3. **Check the repository**:  
   ```bash
   ls
   ```
   You should see:  
   ```
   Dockerfile  docker‑compose.yml  app.py  config.yaml  templates/  requirements.txt
   ```
   *If `docker‑compose.yml` is missing, you’re in the wrong branch. Go back to `main`.*

---

### 2.2. Configure the Flask API

The API will expose two endpoints:  
- `/upload` – receives a PDF or DOCX and returns a JSON summary.  
- `/review` – sends the text to LawGeex and returns the compliance report.

1. **Open `config.yaml`**:  
   ```bash
   nano config.yaml
   ```
2. **Set the LawGeex API key** (obtain from your LawGeex dashboard):

   ```yaml
   lawgeex:
     api_key: "YOUR_LAWGEEX_API_KEY"
     endpoint: "https://api.lawgeex.com/v1/evaluate"
   ```

   *Replace `YOUR_LAWGEEX_API_KEY` with the 32‑character key.*

3. **Set the Flask port**:

   ```yaml
   server:
     host: "0.0.0.0"
     port: 5000
   ```

4. **Save and exit** (`Ctrl+O`, `Enter`, `Ctrl+X`).  
5. **Verify integrity**:

   ```bash
   cat config.yaml
   ```
   You should see the exact YAML structure above.

**Interactive Check‑in**  
Do you see the `lawgeex:` block with an `api_key` value?  
If the key is blank or the line is missing, re‑enter it.

---

### 2.3. Build the Docker Image

1. **Navigate to the project root** (you should already be there).  
2. **Build the image**:

   ```bash
   docker build -t legal-ai-core:latest .
   ```

   Expected output (last few lines):

   ```
   Step 12/12 : CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
   => [12/12] RUN gunicorn -b 0.0.0.0:5000 app:app
   => => collecting static files
   => => 0 static files copied
   => => booting worker with pid 1
   => [12/12] CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"] 0.0s
   => exporting to image
   => => exporting layers
   => => writing image sha256:...
   => => naming to docker.io/library/legal-ai-core:latest
   ```

3. **Run the container**:

   ```bash
   docker run -d --name legal-api -p 5000:5000 legal-ai-core:latest
   ```

4. **Verify the service**:

   ```bash
   curl -I http://localhost:5000
   ```

   You should receive:

   ```
   HTTP/1.1 200 OK
   Content-Type: text/html; charset=utf-8
   ```

**Interactive Check‑in**  
Do you see the `docker run` command succeed and the `curl` output show `200 OK`?  
If the container fails to start, run `docker logs legal-api` and look for `ERROR: Could not connect to LawGeex API`. That usually means the API key is wrong.

---

### 2.4. Integrate [Make.com](https://www.make.com/en/register?pc=menshly) for Automated Workflow

We’ll use Make.com (formerly Integromat) to trigger the API whenever a new contract lands in a shared Dropbox folder.

1. **Create a Make.com scenario**:  
   - **Trigger**: “Watch Files” (Dropbox)  
   - **Action**: “HTTP Request” (POST to `http://<YOUR_SERVER>/upload`)

2. **Configure the Dropbox trigger**:  
   - Path: `/contracts/incoming/`  
   - Polling frequency: 15 minutes

3. **Configure the HTTP Request**:  
   - Method: POST  
   - URL: `http://<YOUR_SERVER>/upload`  
   - Body type: `Form Data`  
   - Field name: `file` → **Map** to the file from Dropbox

4. **Add a second action**: “Delay” (10 s) to allow the Flask API to process.  
5. **Add a third action**: “HTTP Request” (POST to `http://<YOUR_SERVER>/review`)  
   - Body type: JSON  
   - JSON body: `{ "file_id": "{{File ID}}" }`

**Interactive Check‑in**  
Do you see the “HTTP Request” module set to POST with the correct URL?  
If the Make.com trigger shows “No data received”, verify the Dropbox folder path matches the one in the scenario.

---

### 2.5. Connect to ContractBook for Document Management

ContractBook will hold the final, signed versions of the contracts.

1. **Obtain the ContractBook API token** from the admin panel.  
2. **Add a new step in Make.com** after the review: “ContractBook – Create Document”.  
   - API endpoint: `https://api.contractbook.com/v1/documents`  
   - Method: POST  
   - Headers: `Authorization: Bearer YOUR_CONTRACTBOOK_TOKEN`  
   - Body (raw JSON):

     ```json
     {
       "title": "{{File Name}}",
       "content": "{{Review Report}}",
       "tags": ["AI‑Reviewed"]
     }
     ```

3. **Test the flow** by uploading a test PDF to Dropbox.  
   The Make.com scenario should finish with a “Document Created” status in ContractBook.

**Interactive Check‑in**  
Do you see the new document listed in ContractBook under the “AI‑Reviewed” tag?  
If

## Step 3: Test and Validate

*Section content pending review.*


## Step 4: Add Advanced Features

*Section content pending review.*


## Step 5: Deploy to Production (or Price & Sell)

**Objective:** Move your AI‑powered legal document service from a local sandbox to a live, scalable environment or, if you prefer to launch a SaaS‑style business, define clear pricing tiers and a ready‑to‑copy sales pitch.

---

### A. Deploy to Production

1. **Create a Production VPC on Hostinger**  
   - Log in to the Hostinger admin panel.  
   - Navigate: **Hosting → VPS → Create VPS**.  
   - Choose **Linux (Ubuntu 24.04 LTS)**, **2 GB RAM**, **1 vCPU**, **50 GB SSD**.  
   - Click **Create**.  
   - *Check‑in*: Do you see a green “Running” status? If not, wait 2 min and refresh.

2. **Set up SSH and Firewall**  
   - From your local terminal:  
     ```bash
     ssh root@<HOSTINGER_IP>
     ```
   - Once logged in, run:  
     ```bash
     ufw enable
     ufw allow 22/tcp
     ufw allow 443/tcp
     ufw allow 80/tcp
     ```
   - *Verification*: `sudo ufw status` should list ports 22, 80, 443 as allowed.

3. **Install Docker & Compose**  
   ```bash
   apt update && apt upgrade -y
   apt install docker.io docker-compose -y
   systemctl enable docker
   systemctl start docker
   ```
   - *Check‑in*: `docker --version` → `Docker version 26.x.x`.

4. **Clone your Repository**  
   ```bash
   git clone https://github.com/<your-username>/lawgeex-service.git
   cd lawgeex-service
   ```

5. **Configure Environment Variables**  
   - Create `.env.prod`:
     ```dotenv
     LAWGEEX_API_KEY=sk-XXXXXXXXXXXXXXXX
     CONTRACTBOOK_API_KEY=cbp-XXXXXXXXXXXXXXXX
     DATABASE_URL=mysql://root:rootpass@db:3306/lawgeex_prod
     APP_BASE_URL=https://legal.yourdomain.com
     ```
   - Ensure `.env.prod` **is not** committed to Git.  

6. **Set Up MySQL Container**  
   ```yaml
   # docker-compose.yml snippet
   services:
     db:
       image: mysql:8
       environment:
         MYSQL_ROOT_PASSWORD: rootpass
         MYSQL_DATABASE: lawgeex_prod
       volumes:
         - db-data:/var/lib/mysql
   volumes:
     db-data:
   ```
   - Run `docker-compose up -d db`.

7. **Build & Deploy the App**  
   ```bash
   docker-compose build
   docker-compose up -d
   ```
   - *Verification*: `docker ps` should list `lawgeex_service_app` running.  
   - Access `https://legal.yourdomain.com` in a browser. You should see the login page with a “Welcome to LawGeex Service” banner.

8. **Configure HTTPS via Let’s Encrypt**  
   ```bash
   apt install certbot python3-certbot-nginx -y
   certbot --nginx -d legal.yourdomain.com
   ```
   - Follow prompts: enter email, agree to TOS.  
   - *Check‑in*: Browser shows padlock; `curl -I https://legal.yourdomain.com | grep -i ssl` returns `HTTP/2 200`.

9. **Automate Zero‑Downtime Deploys with Replit & Zapier**  
   - In Replit, set up a **CI/CD pipeline** that pulls from GitHub, runs tests, and pushes new Docker images to Hostinger.  
   - Use Zapier to trigger the pipeline on every push to `main`.  
   - *Error scenario*: If “Build failed” appears in Replit, open the build log, fix the failing test, and re‑push.

10. **Set Up Monitoring**  
    - Deploy **Prometheus** via Docker Compose (see official docs).  
    - Use Grafana dashboards to track response times and error rates.  
    - *Check‑in*: Grafana shows metrics; set an alert for > 5 % 5xx errors.

---

### B. Price & Sell

| Tier        | Monthly Fee | Features                                                                 | Ideal For                                   |
|-------------|-------------|--------------------------------------------------------------------------|---------------------------------------------|
| Starter     | $49         | 5 document templates, 10 AI reviews/month, email support                | Solo entrepreneurs, freelancers             |
| Growth      | $149        | 20 templates, 50 AI reviews/month, API access, priority support         | Small law firms, SMBs                       |
| Enterprise  | $499        | Unlimited templates, 200 AI reviews/month, SSO, custom integrations     | Mid‑size to large legal teams, agencies     |

**Copy‑Paste Pitch Template**

```
Subject: Automate Your Legal Docs – 50% Off for 30 Days

Hi {FirstName},

Tired of spending hours drafting contracts? Let LawGeex + ContractBook do the heavy lifting. With our AI‑review engine and seamless template library, you can:

- Draft & review 10+ contracts per day in under 5 min
- Reduce legal spend by 30%
- Get 24/7 support & custom integrations

Try our Starter plan for just $49/month – no credit card required, 30‑day free trial included.

Book a quick 15‑minute demo: https://calendly.com/yourname/15min

Best,
{YourName}
```

**Sales Method**

1. **Calendly** – Embed the link above into your website and email signatures.  
2. **ActiveCampaign** – Trigger a drip sequence if the demo isn’t booked within 48 h.  
3. **Buffer** – Schedule a 3‑post campaign on LinkedIn/Twitter every week highlighting success stories.

Follow the exact URLs and token placements above; any deviation may break the flow. If you hit a “404 – Demo Not Found” error, double‑check that your Calendly URL ends with `/15min` and that the event type is “15‑Minute Meeting”.

By following these steps, you will have a fully‑functioning, production‑ready legal document automation service, or a clear go‑to‑market plan that turns visitors into paying customers.

## Step 6: Scale and Grow

*Section content pending review.*


## Cost Breakdown

*Section content pending review.*


## Production Checklist

Before pushing the AI‑powered document workflow live, run through this checklist to guarantee a stable, compliant, and customer‑ready service.

- [ ] **LawGeex Integration Health**  
  *Navigate to “Integrations → LawGeex” in your Replit project. Confirm the API key is set to the production value (not the sandbox). The status should read “Connected – 200 OK”. If you see a 401, double‑check the key and regenerate it in the LawGeex dashboard.*

- [ ] **ContractBook Data Sync**  
  *In the ContractBook admin panel, go to “Settings → API → Data Sync”. Verify the “Sync Frequency” is set to “15 minutes” and “Webhook URL” matches your Replit endpoint (`https://<app>.repl.co/webhook/contractbook`). Click “Test Webhook” – you should receive a 200 response.*

- [ ] **User Authentication & Role‑Based Access**  
  *Open your Auth0 console, select the application, and confirm that only users with the “Legal Advisor” role can access the “Generate Document” page. Test by logging in as a non‑role user; the page should redirect to the role‑assignment prompt.*

- [ ] **Error Logging & Alerting**  
  *In the Replit console, ensure the `winston` logger writes to a file (`logs/production.log`). Configure a Slack webhook via Zapier to send any log entries containing “ERROR” to the #legal‑ops channel. Verify by triggering a fake API failure and checking Slack.*

- [ ] **Legal Compliance Review**  
  *Open the ContractBook “Compliance” tab and confirm that the “GDPR” and “CCPA” toggle switches are ON. Export the compliance report and confirm the PDF includes the correct jurisdiction clauses.*

- [ ] **Performance Benchmark**  
  *Run `ab -n 1000 -c 100 https://<app>.repl.co/generate` and confirm the average response time stays below 2 s. If it exceeds, revisit your LawGeex batch size setting in the Replit environment (`LAWGEEX_BATCH=50`).*

- [ ] **Email Notification Flow**  
  *Using Klaviyo, navigate to “Flows → Document‑Ready”. Confirm the trigger is set to “ContractBook: Document Completed”. Send a test email; the subject should read “Your Contract is Ready”, and the body must include the direct link to the PDF.*

- [ ] **Backup & Disaster Recovery**  
  *In Hostinger, schedule a nightly backup of the ContractBook database (via the “Backup” tab). Verify that the backup file can be restored in a test environment within 5 min.*

- [ ] **Cost Monitoring**  
  *Set up a Zapier alert to trigger when the LawGeex usage reaches 90% of the monthly quota. Ensure the alert email is routed to the billing email address.*

- [ ] **Final User Acceptance Test (UAT)**  
  *Invite three external beta users to generate a sample NDA. Confirm they receive the PDF via email, can download it, and that the document matches the template in ContractBook. Record any discrepancies in a shared [Notion](https://notion.so/) page for last‑minute fixes.*

Once all boxes are ticked, you’re ready to announce the launch. This rigorous pre‑flight check will safeguard uptime, compliance, and customer trust.

## What to Do Next

*Section content pending review.*


Ready to understand the full business opportunity? Read our [opportunity deep-dive]({< ref "/opportunities/how-to-build-an-ai-legal-document-automation-service-48k-55kmonth.md" >}).


## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
