---
title: "Build an AI Freelance Opportunity Finder with Upwork: The Complete Step-by-Step Guide"
date: 2026-11-26
category: "Implementation"
difficulty: "INTERMEDIATE"
readTime: "25 MIN"
excerpt: "*Section content pending review.*"
image: "/images/articles/intelligence/find-qualify-and-optimize-freelance-opportunities-with-upwork-and-freelancer.png"
heroImage: "/images/heroes/intelligence/find-qualify-and-optimize-freelance-opportunities-with-upwork-and-freelancer.png"
relatedOpportunity: "/opportunities/how-to-build-an-ai-freelance-arbitrage-20k-50kmonth/"
---



## Prerequisites

*Section content pending review.*


## Step 1: Setup and Configuration

*Section content pending review.*


## Step 2: Build the Core System

In this step we assemble the actual “engine” that will (1) pull job listings from Upwork and Freelancer, (2) score each listing against your AI‑service catalog, and (3) output a ready‑to‑pitch bundle. The architecture is a lightweight micro‑service written in Node.js, orchestrated by [Make.com](https://www.make.com/en/register?pc=menshly), and persisted in a PostgreSQL database hosted on Hostinger. We will use Replit for the code repository, [ElevenLabs](https://elevenlabs.io/) for voice‑to‑text transcription of job descriptions, and Zapier to push qualified leads into Klaviyo for nurture.

> **Tip:** Keep the service running 24/7 on Replit (paid plan $5/month) so that job scores refresh every 30 minutes.

---

### 2.1 Create the Replit Project

1. Log into [**Replit**](https://replit.com/refer/egwuokwor) (https://replit.com).  
2. Click **+ Create** → **New Repl**.  
3. Name: `upwork-freelance-finder`.  
4. Language: **Node.js** (Node 20.x).  
5. Click **Create Repl**.

> **Check‑in**: You should see a terminal at the bottom and a file tree on the left. The main file is `index.js`.  
> If you don’t see “Node.js”, go to **Settings** → **Language** → select **Node.js**.

---

### 2.2 Install Dependencies

Open the terminal and run:

```bash
npm install axios dotenv pg node-cron
```

- `axios` – HTTP client for Upwork/Freelancer APIs.  
- `dotenv` – load environment variables.  
- `pg` – PostgreSQL driver.  
- `node-cron` – schedule jobs.

> **Check‑in**: After the install, you should see a `node_modules` folder and a `package-lock.json`.  
> If you see `npm ERR!`, run `npm cache clean --force` then retry.

---

### 2.3 Configure Environment Variables

Create a `.env` file in the root:

```env
UPWORK_CLIENT_ID=YOUR_UPWORK_CLIENT_ID
UPWORK_CLIENT_SECRET=YOUR_UPWORK_CLIENT_SECRET
FREELANCER_API_KEY=YOUR_FREELANCER_API_KEY
PGHOST=db.hostinger.com
PGPORT=5432
PGDATABASE=freelance_finder
PGUSER=your_pg_user
PGPASSWORD=your_pg_password
```

- **Upwork**: Register an app at https://developers.upwork.com to get the client ID/secret.  
- **Freelancer**: Generate an API key from your Freelancer dashboard.  
- **Postgres**: Create a database on Hostinger (price $2.99/month). Use the credentials from the Hostinger control panel.

> **Check‑in**: Open `.env` and verify all keys are present.  
> If you see `undefined`, re‑check your API key generation steps.

---

### 2.4 Database Schema

In the Replit console, run:

```bash
psql -h $PGHOST -U $PGUSER -d $PGDATABASE
```

Then execute:

```sql
CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    platform VARCHAR(20),
    job_id VARCHAR(50),
    title TEXT,
    description TEXT,
    score INT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

> **Check‑in**: After running the script, type `\d jobs` to see the table definition.  
> If you get `psql: could not connect to server`, verify your Hostinger credentials.

---

### 2.5 Fetch & Score Jobs

Paste the

## Step 3: Test and Validate

*Section content pending review.*


## Step 4: Add Advanced Features

*Section content pending review.*


## Step 5: Deploy to Production

Below is the full, production‑ready deployment workflow for your AI‑powered freelance opportunity finder.  
We’ll spin up a Docker‑based service on Hostinger’s VPS, expose it behind an Nginx reverse proxy, and set up automated scaling with Make.com. All commands are written for a Debian‑based system; adjust the package manager if you’re on a different distro.

### 5.1 Provision a Hostinger VPS

1. Log into your Hostinger control panel.  
2. Navigate to **VPS Hosting → Create VPS**.  
3. Pick a **Debian 12** image, 2 GB RAM, 1 vCPU, 20 GB SSD.  
4. Click **Launch**.  
5. Once the VPS is ready, note the public IP (e.g., `123.45.67.89`) and the root SSH credentials.

> **Check‑in:** Do you see the “VPS Details” page with the IP and SSH key? If not, verify that your billing is active.

### 5.2 SSH into the VPS

```bash
ssh root@123.45.67.89
```

> **Error:** If you see “Permission denied (publickey)”, confirm that your SSH key is added to Hostinger and that your local key is listed in `~/.ssh/id_rsa`.

### 5.3 Install Docker and Docker‑Compose

```bash
apt update && apt install -y docker.io docker-compose
systemctl enable --now docker
```

Verify Docker:

```bash
docker --version
# Expected: Docker version 24.x.x
docker compose version
# Expected: Docker Compose version v2.x.x
```

> **Check‑in:** Are the Docker versions at least 24.x.x? If not, run `apt install -y docker.io` again.

### 5.4 Clone the Project Repository

```bash
git clone https://github.com/yourorg/ai-freelance-finder.git
cd ai-freelance-finder
```

Replace the URL with your fork.  
The repository contains `Dockerfile`, `docker-compose.yml`, and the `app/` source.

### 5.5 Configure Environment Variables

Create a `.env` file in the project root:

```bash
cat > .env <<EOF
UPWORK_CLIENT_ID=your_upwork_client_id
UPWORK_CLIENT_SECRET=your_upwork_client_secret
OPENAI_API_KEY=sk-xxxx
DATABASE_URL=postgres://user:pass@localhost:5432/finderdb
PORT=8000
EOF
```

> **Check‑in:** Do you see a file named `.env` with those variables? If not, create it manually.

### 5.6 Build and Run the Docker Stack

```bash
docker compose up --build -d
```

This command builds the image (`ai-freelance-finder:latest`) and starts three containers:  
- `app` – FastAPI backend  
- `db` – PostgreSQL database  
- `worker` – Celery workers for background scraping

Verify container status:

```bash
docker compose ps
# Expected output: 3 containers in “Up” state
```

### 5.7 Set Up Nginx Reverse Proxy

Install Nginx:

```bash
apt install -y nginx
```

Create `/etc/nginx/sites-available/finder`:

```bash
cat > /etc/nginx/sites-available/finder <<EOF

## Step 6: Scale and Grow

*Section content pending review.*


## Cost Breakdown

*Section content pending review.*


## Production Checklist

Before you let your AI‑powered freelance opportunity finder go live, run through the following items to ensure reliability, compliance, and optimal performance.

- [ ] **API Rate‑Limit Verification** – In the Replit console, open `config.env` and confirm that `UPWORK_CLIENT_ID`, `UPWORK_CLIENT_SECRET`, and `FREELANCER_API_KEY` are present. Run `python -m scripts.check_limits` and verify the output shows “Upwork rate limit: 50 req/min, Freelancer limit: 100 req/min.” If the script reports “429 Too Many Requests,” increase your `REQUEST_INTERVAL_MS` in `app/config.py` to 3000 ms.

- [ ] **Webhook Security** – Using Make.com, create a webhook with the URL `https://<your‑replit‑app>.repl.co/webhooks/upwork`. In the Make.com dashboard, enable “Verify signature” and paste the `UPWORK_WEBHOOK_SECRET` from `config.env`. Test by sending a sample payload from the Upwork developer portal and confirm the Make.com scenario logs “Webhook verified.”

- [ ] **Data Persistence** – In the Replit database, navigate to `replit.db` → `tasks`. Run `replit run scripts.verify_db` and confirm the output shows “All 1,200 task records contain `created_at`, `updated_at`, and `status` fields.” If any record is missing, re‑run `python -m scripts.migrate_db` to add the missing columns.

- [ ] **Email Notification Threshold** – In Klaviyo, edit the “Opportunity Alert” flow. Ensure the trigger “Task score > 80” is active and the email template contains the placeholder `{{ task.title }}`. Send a test email via the Klaviyo sandbox and confirm the subject line reads “High‑Scoring Opportunity: {{ task.title }}.”

- [ ] **Performance Benchmark** – Deploy the app to Hostinger’s Node.js plan. Run `ab -n 500 -c 50 https://<your‑app>.hostingerapp.com/api/scan` and verify the average latency is < 200 ms and error rate < 0.1 %. If latency exceeds 250 ms, enable Cloudflare caching on the `/api/*` routes.

- [ ] **Compliance Check** – Open the Upwork Terms of Service in your browser. Ensure your `README.md` contains the clause: “This tool complies with Upwork’s API usage policy and does not store user credentials.” Verify that the `privacy_policy.html` is linked in the footer of the app.

- [ ] **Logging & Alerting** – In the Replit console, execute `python -m scripts.setup_logging`. Confirm that logs are sent to a Loggly account (URL: `https://logs-01.loggly.com/inputs/<token>`) and that an alert is configured in Buffer for error logs > 5/min.

- [ ] **Backup Strategy** – In the Replit project, run `python -m scripts.backup_db`. Check that a gzipped dump appears in the `backups/` folder with a timestamp. Schedule this script to run nightly via Make.com’s scheduler.

- [ ] **User Acceptance Test** – Log in with a test Upwork account, run the “Scan” endpoint, and verify that the top 5 results appear in the UI with correct bid suggestions. If any result shows “No match,” review the scoring logic in `app/scoring.py`.

- [ ] **Pricing & Billing Confirmation** – In Stripe, confirm that the “Freelance Finder” plan is active, priced at $49/month, and that trial periods are correctly set to 

## What to Do Next

*Section content pending review.*


Ready to understand the full business opportunity? Read our [opportunity deep-dive]({< ref "/opportunities/how-to-build-an-ai-freelance-arbitrage-20k-50kmonth.md" >}).


## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
