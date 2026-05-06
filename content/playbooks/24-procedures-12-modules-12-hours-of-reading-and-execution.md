---
title: "26 procedures. 10 modules. 12+ hours of reading and execution"
date: 2026-05-02
category: "Playbook"
price: "₦25,000"
readTime: "45 MIN"
excerpt: "This playbook extends our free implementation guide with complete procedures, SOPs, and revenue calculators. 26 procedures. 10 modules. 12+ hours of reading and execution. Completing every procedure will give you a fully functional, subscription‑base..."
image: "/images/articles/playbooks/24-procedures-12-modules-12-hours-of-reading-and-execution.png"
heroImage: "/images/heroes/playbooks/24-procedures-12-modules-12-hours-of-reading-and-execution.png"
relatedOpportunity: "/opportunities/how-to-launch-an-ai-personal-finance-automation-service-in-2026-2k-10kmonth/"
relatedGuide: "/intelligence/research-automate-and-monetize-an-ai-affiliate-marketing-system-with-semrush-and/"
---
This playbook extends our free implementation guide with complete procedures, SOPs, and revenue calculators.
**26 procedures. 10 modules. 12+ hours of reading and execution.** Completing every procedure will give you a fully functional, subscription-based AI Personal Finance Automation System that you can start monetizing at ₦25,000 per month, with a clear path to scaling and profit.

---

# MODULE 1: FOUNDATION – Set Up Core Accounts and Infrastructure

## Overview
In this module you will create every foundational account you need. Skipping this step will mean you cannot pay for services, host code, or collect payments. Every downstream module depends on the accounts and infrastructure you set up here — without a domain, hosting, and a workspace, nothing else works.
**Time to complete:** 90 minutes
**Tools needed:** Hostinger, Notion, Calendly

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| **Hostinger** | Web hosting & domain | $1.99/mo starter | $3.95/mo premium |
| **Notion** | Workspace & documentation | Free (1 user) | $8/mo per user |
| **Calendly** | Scheduling & appointments | Free (1 event type) | $10/mo |

## Procedure 1.1: Create a Hostinger Web Hosting Account

1. Visit **https://www.hostinger.com**.
2. Click the **Get Started** button next to the "Shared Hosting" plan.
3. On the signup page, fill in:
   - **Email:** your personal email
   - **Password:** a strong password (e.g., `Passw0rd!2026`)
   - **Password confirmation:** repeat the password
4. Click **Continue**.
5. On the "Choose a domain" screen, enter `myfinancebot.com` (or a domain you own).
6. Click **Add Domain**.
7. Click **Continue**.
8. On the payment screen, select **Monthly** billing and click **Continue**.
9. You will be redirected to a confirmation page that reads **"Your order has been placed."**
10. Click the **"Go to Dashboard"** button.
11. Do you see the **Hostinger Dashboard** with a green banner that says *"Welcome to Hostinger! Your site is live."* If you do not, refresh the page.
12. In the left-hand menu, click **Hosting** → **Manage**.
13. Click **Add Hosting** > **Add Domain**.
14. Enter your domain `myfinancebot.com` again, select **"Add to existing plan"**, and click **Save**.
15. Do you see the domain listed under **My Domains**? If not, go back to **Hosting** and verify the domain name.
16. In the top bar, click the **cog icon** (Settings) next to your domain and set the **PHP version** to **8.1**.
17. Click **Save**.
18. In the left-hand menu, click **File Manager**.
19. Create a new folder named **`financebot`**.
20. Inside `financebot`, create a file named **`index.php`** with the following content:

```php
<?php
echo "<h1>Welcome to AI Personal Finance Automation</h1>";
?>
```

21. Do you see the file `index.php` in the File Manager? If not, refresh the File Manager.
22. In the top bar, click **"Go to URL"** and paste `http://myfinancebot.com/financebot`.
23. You should see the text *"Welcome to AI Personal Finance Automation"* rendered in the browser.

**Error scenario:** If you see a *403 Forbidden* error, the folder permissions are wrong. Go back to File Manager, right-click the `financebot` folder, set permissions to **755**, and try again.

## Procedure 1.2: Set Up a Notion Workspace for Client Data

1. Open **https://www.notion.so** in your browser.
2. Click **Sign Up** and create an account with your business email.
3. Once logged in, click **+ New Page** in the left sidebar.
4. Title the page **"AI Finance Automation — Command Center"**.
5. Inside the page, type `/table` and select **Table — Full Page**.
6. Name the table **"Client Pipeline"**.
7. Add the following columns:
   - **Client Name** (Title)
   - **Email** (Text)
   - **Status** (Select: Lead, Onboarding, Active, Churned)
   - **Monthly Revenue** (Number, format as Naira)
   - **Start Date** (Date)
   - **Notes** (Text)
8. Add a second table by typing `/table` below the first one. Name it **"API Keys Vault"** with columns:
   - **Service** (Title)
   - **API Key** (Text)
   - **Date Created** (Date)
   - **Status** (Select: Active, Revoked)
9. Do you see both tables on the page? If not, scroll down — they may be below the fold.
10. Click **Share** in the top-right corner, toggle **Share to web** OFF (this is sensitive data).

**Error scenario:** If you cannot create a table, you may be on a limited workspace. Click **Settings & Members → Plans** and confirm you are on the Free plan with at least 1,000 blocks available.

## Procedure 1.3: Configure Calendly for Client Onboarding Calls

1. Visit **https://www.calendly.com** and click **Get Started**.
2. Sign up with your business email and set a password.
3. On the **"What type of meetings do you want to schedule?"** screen, select **One-on-One**.
4. Name your event type **"AI Finance Automation — Discovery Call"**.
5. Set the duration to **30 minutes**.
6. Under **"When are you available?"**, select **Monday–Friday, 9:00 AM – 5:00 PM** in your timezone.
7. Click **Save & Close**.
8. Copy your Calendly link (e.g., `https://calendly.com/yourname/ai-finance-automation-discovery-call`).
9. Paste the link into your Notion **"Command Center"** page under a new heading called **"Booking Links"**.
10. Do you see the link in Notion? If not, make sure you saved the Calendly event first.

## Check-In: Module 1 Complete
- [ ] Hostinger account created and verified
- [ ] Domain added to hosting plan and index.php deployed
- [ ] Notion workspace created with Client Pipeline and API Keys tables
- [ ] Calendly event created and link saved in Notion

---

# MODULE 2: TECH STACK – Acquire API Keys and Set Up Make.com Automation

## Overview
You will secure all the API keys you need and wire them into Make.com, our central automation engine. Missing any key will break downstream workflows. This module connects every tool in your stack so that data flows automatically from one service to the next without manual intervention.
**Time to complete:** 75 minutes
**Tools needed:** Make.com, ChatGPT (OpenAI), Vapi, ElevenLabs, Klaviyo

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| **Make.com** | Low-code automation hub | 1,000 ops/month | $9/mo for 10K ops |
| **ChatGPT** | AI analysis engine | Free tier | $20/mo Plus |
| **Vapi** | AI voice agents | 5 calls/month free | $15/mo starter |
| **ElevenLabs** | Text-to-speech | 10,000 chars/month | $5/mo starter |
| **Klaviyo** | Email marketing | 250 contacts free | $20/mo |

## Procedure 2.1: Create a Make.com Account and Get the API Token

1. Open **https://www.make.com**.
2. Click **SIGN UP** in the top-right corner.
3. Choose **"Create a free account"** and enter your business email and a strong password.
4. Click **Continue** and verify your email.
5. Log in to the Make.com dashboard.
6. In the top-right, click your avatar → **Account Settings** → **API**.
7. Click **Generate a new token**.
8. Copy the token and paste it into your Notion **API Keys Vault** table under the row for **Make.com**.
9. Do you see the token displayed in Notion? If not, go back to Make.com and regenerate it.

## Procedure 2.2: Create and Store All Required API Keys

1. **ChatGPT (OpenAI):** Visit https://platform.openai.com/account/api-keys. Log in, click **API keys**, then **Create new secret key**. Copy the key and paste it into Notion under **OpenAI Key**.
2. **Vapi:** Visit https://app.vapi.ai/. Sign up, then navigate to **Dashboard → API Keys**. Click **Create Key**, copy it, and paste into Notion under **Vapi Key**.
3. **ElevenLabs:** Visit https://elevenlabs.io/. Sign up, then go to **Profile → API Keys**. Copy the key and save in Notion under **ElevenLabs Key**.
4. **Klaviyo:** Visit https://www.klaviyo.com/. Sign up, then go to **Settings → API Keys → Create API Key**. Set permissions to **Full Access** and copy the key into Notion.
5. **Hostinger:** In the Hostinger dashboard, go to **Hosting → Manage → Advanced → API**. Generate a token and save it in Notion.

Do you see all 5 API keys in your Notion **API Keys Vault** table? If any are missing, go back and complete that step before proceeding.

**Error scenario:** If OpenAI shows *"You need to add a payment method"*, add a card with at least $5 credit. OpenAI requires a payment method on file to use the API, even for the free trial tokens.

## Procedure 2.3: Build Your First Make.com Scenario — API Health Check

1. In Make.com, click **+ Create a new scenario** in the top-left.
2. Name the scenario **"API Health Check"**.
3. Click the **+** icon and search for **HTTP**. Select **Make a Request**.
4. Configure the HTTP module:
   - **URL:** `https://api.openai.com/v1/models`
   - **Method:** GET
   - **Headers:** Add `Authorization: Bearer YOUR_OPENAI_KEY` (replace with your actual key from Notion)
5. Click **OK** to save the module.
6. Click **Run once** (the play button at the bottom-left).
7. Do you see a **200 OK** response with a list of models in the output? If you see **401 Unauthorized**, your API key is wrong — go back to Notion and double-check it.
8. Repeat steps 3–7 for each API endpoint:
   - Vapi: `https://api.vapi.ai/v1/assistants` (GET, with Bearer token)
   - ElevenLabs: `https://api.elevenlabs.io/v1/voices` (GET, with `xi-api-key` header)
9. If all three return 200, your API connections are live. Click **Save** on the scenario.

## Check-In: Module 2 Complete
- [ ] Make.com account created with API token saved in Notion
- [ ] All 5 API keys (OpenAI, Vapi, ElevenLabs, Klaviyo, Hostinger) stored in Notion
- [ ] Make.com API Health Check scenario runs successfully with 200 responses
- [ ] At least 3 API endpoints verified as working

---

# MODULE 3: FRAMEWORK – Design Your Service Delivery Framework

## Overview
This module turns your tech stack into a repeatable, high-value service. You will define every touchpoint from lead capture to final billing, and codify a client onboarding flow that guarantees 100% data integrity and first-day ROI. Without a documented framework, you will deliver inconsistent results, lose clients to confusion, and waste hours reinventing the wheel for every new customer.
**Time to complete:** 60 minutes
**Tools needed:** Notion, ChatGPT

## Procedure 3.1: Design Your Service Delivery Framework in Notion

1. Open your Notion **"AI Finance Automation — Command Center"** page.
2. Below the existing tables, type `/page` and title it **"Service Delivery Framework"**.
3. Inside the new page, create a Kanban board by typing `/board` and selecting **Board — Full Page**.
4. Name the board **"Client Journey"** and set the grouping property to **Stage**.
5. Create the following stages as columns: **Lead**, **Qualified**, **Onboarding**, **Active**, **Review**, **Renewal**, **Churned**.
6. For each stage, add a card describing the key actions:
   - **Lead:** "Received inquiry via Calendly or website form"
   - **Qualified:** "Completed discovery call; confirmed budget ≥ ₦25,000/month"
   - **Onboarding:** "Sent welcome email; collected bank credentials via secure form"
   - **Active:** "AI automation running; monthly reports delivered"
   - **Review:** "30-day check-in call scheduled via Calendly"
   - **Renewal:** "Sent renewal invoice via Klaviyo"
   - **Churned:** "Exit survey sent; feedback logged"
7. Do you see all 7 columns with cards? If not, click the **+** icon at the end of the board to add missing columns.
8. Add a **Property** called **Revenue** (Number type, Naira format) to the board.
9. Add a **Property** called **Owner** (Person type) and set yourself as the owner on all cards.

## Procedure 3.2: Create the AI Prompt Template for Financial Analysis

1. Open **ChatGPT** at https://chat.openai.com.
2. Start a new chat and paste the following system prompt:

```
You are an AI Personal Finance Analyst. Your job is to:
1. Categorize transactions into: Housing, Food, Transport, Entertainment, Savings, Debt, Other
2. Calculate the percentage of income spent in each category
3. Flag any category exceeding 30% of total income as "OVER BUDGET"
4. Generate a monthly savings recommendation based on the 50/30/20 rule
5. Identify subscription services that can be cancelled or downgraded

Format your response as a structured report with:
- Category Breakdown Table
- Budget Alerts (if any)
- Savings Recommendations
- Subscription Audit
```

3. Test the prompt by pasting a sample set of transactions:

```
Salary: ₦500,000
Rent: ₦150,000
Groceries: ₦80,000
Uber: ₦45,000
Netflix: ₦5,000
Spotify: ₦2,000
Gym: ₦15,000
Electricity: ₦20,000
Loan Payment: ₦60,000
Dining Out: ₦40,000
```

4. Do you see a categorized breakdown with percentages and alerts? If the output is incomplete, add "Continue your response" and re-send.
5. Save the full prompt as a template in your Notion workspace under a new page titled **"Prompt Templates"**.

## Check-In: Module 3 Complete
- [ ] Service Delivery Framework board created with 7 stages
- [ ] Client Journey Kanban populated with action cards
- [ ] AI financial analysis prompt tested with sample transactions
- [ ] Prompt template saved in Notion

---

# MODULE 4: FIRST BUILD – Build Your Core AI Finance Product

## Overview
In this module you build, deploy, and test the core AI Personal Finance Automation product. This is the minimum viable product that your first paying client will use. You will create a Python application that ingests transaction data, runs it through ChatGPT for analysis, and outputs a structured financial report. If you skip this module, you have nothing to sell.
**Time to complete:** 3 hours
**Tools needed:** Replit, ChatGPT API, Make.com, Hostinger

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| **Replit** | Cloud IDE & deployment | 500 MB RAM, public repos | $7/mo for private repos |
| **ChatGPT** | AI analysis engine | Free tier | $20/mo Plus |

## Procedure 4.1: Build the Core Finance Analysis App in Replit

1. Open **https://replit.com** and sign up for a free account.
2. Click **+ Create Repl** in the top-right corner.
3. Select the **Python** template and name the repl **`ai-finance-bot`**.
4. In the **`main.py`** file, replace the starter code with:

```python
import os
import json
from openai import OpenAI
from flask import Flask, request, jsonify

app = Flask(__name__)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are an AI Personal Finance Analyst. Your job is to:
1. Categorize transactions into: Housing, Food, Transport, Entertainment, Savings, Debt, Other
2. Calculate the percentage of income spent in each category
3. Flag any category exceeding 30% of total income as OVER BUDGET
4. Generate a monthly savings recommendation based on the 50/30/20 rule
5. Identify subscription services that can be cancelled or downgraded

Format your response as JSON with keys: category_breakdown, budget_alerts, savings_recommendations, subscription_audit"""

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    transactions = data.get("transactions", [])
    tx_text = "\n".join([f"{t['description']}: {t['amount']}" for t in transactions])

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Analyze these transactions:\n{tx_text}"}
        ],
        max_tokens=1000,
        temperature=0.3
    )

    return jsonify({"analysis": response.choices[0].message.content})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "service": "ai-finance-bot"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
```

5. In the **Shell** tab (bottom panel), run: `pip install openai flask`
6. Click the **Secrets** tab (lock icon in the sidebar) and add: `OPENAI_API_KEY` = your key from Notion.
7. Click **Run** at the top. Do you see `* Running on http://0.0.0.0:8080` in the console? If not, check that `main.py` is set as the entry point.
8. Test the health endpoint: Open the Webview URL and append `/health`. Do you see `{"status": "healthy", "service": "ai-finance-bot"}`?

**Error scenario:** If you see `ModuleNotFoundError: No module named 'openai'`, the pip install did not complete. Re-run `pip install openai flask` and wait for the installation to finish.

## Procedure 4.2: Create the Make.com Workflow to Connect ChatGPT and Email Delivery

1. In Make.com, click **+ Create a new scenario** and name it **"Finance Analysis Pipeline"**.
2. Add a **Webhook** trigger: Click **+**, search **Webhook**, select **Custom Webhook**. Name it `finance-webhook`. Copy the webhook URL — you will need it later.
3. Add an **HTTP** module after the webhook: Click **+**, search **HTTP**, select **Make a Request**. Configure:
   - **URL:** Your Replit app URL + `/analyze` (e.g., `https://ai-finance-bot.yourusername.repl.co/analyze`)
   - **Method:** POST
   - **Body Type:** JSON
   - **Body:** Map the webhook data to the `transactions` field
4. Add a **Klaviyo** module after the HTTP module: Search **Klaviyo**, select **Send Email**. Configure:
   - **To:** Map from webhook `email` field
   - **Subject:** "Your AI Financial Analysis Report"
   - **Body:** Map the `analysis` field from the HTTP response
5. Click **Save** and then **Run once** to test.
6. Send a test POST to your webhook URL with sample transaction data. Do you see the email arrive in your inbox?

## Procedure 4.3: Deploy the App to Production on Hostinger

1. In Replit, click the **Version Control** tab (git icon in the sidebar).
2. Click **Connect to GitHub** and authorize Replit to access your GitHub account.
3. Create a new repository named **`ai-finance-bot`** and push the code.
4. In Hostinger, go to **Hosting → Manage → SSH Access**. Enable SSH and note the credentials.
5. Connect via SSH using Terminal: `ssh u123456789@myfinancebot.com` (replace with your actual SSH credentials).
6. Clone your GitHub repo: `git clone https://github.com/yourusername/ai-finance-bot.git`
7. Install dependencies: `cd ai-finance-bot && pip install -r requirements.txt`
8. Start the app with: `nohup python main.py &`
9. Visit `https://myfinancebot.com/financebot/health`. Do you see the health check response? If you get a 502 error, the app hasn't started yet — wait 30 seconds and retry.

## Check-In: Module 4 Complete
- [ ] Replit app created and running with /analyze and /health endpoints
- [ ] Make.com Finance Analysis Pipeline scenario built and tested
- [ ] App deployed to Hostinger production server
- [ ] Health check returns 200 on production URL

---

# MODULE 5: CLIENT ACQUISITION – Build Your Lead Generation Engine

## Overview
This module builds the systems that turn strangers into paying clients. You will create a landing page, set up automated outreach, and build a lead nurturing sequence. Without these systems, you will have a great product but no revenue.
**Time to complete:** 90 minutes
**Tools needed:** Shopify, Klaviyo, Apollo.io, Buffer

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| **Shopify** | Landing page & checkout | 3-day free trial | $29/mo Basic |
| **Klaviyo** | Email nurturing | 250 contacts | $20/mo |
| **Apollo.io** | B2B lead generation | 500 credits/month | $49/mo |
| **Buffer** | Social media scheduling | 3 accounts, 10 posts | $6/mo |

## Procedure 5.1: Build a High-Conversion Landing Page on Shopify

1. Visit **https://www.shopify.com** and click **Start free trial**.
2. Enter your email, password, and store name: **"AI Finance Bot"**.
3. Select the **Debut** theme and click **Publish**.
4. Go to **Online Store → Pages → Add page**.
5. Title the page **"AI Personal Finance Automation"**.
6. In the Rich Text Editor, click the **+** button, select **Custom HTML**, and paste:

```html
<h1>Automate Your Finances in 5 Minutes</h1>
<p>Get real-time expense tracking, smart budgeting, and investment insights — all powered by ChatGPT.</p>
<form action="https://app.klaviyo.com/lists/YOUR_LIST_ID/subscribe" method="POST">
  <input type="email" name="email" placeholder="Your email" required>
  <button type="submit">Get Free Demo</button>
</form>
```

7. Click **Save** and then **Preview**. Do you see the form with the "Get Free Demo" button?
8. Add a pricing section below the form with three tiers:

| Tier | Price | Includes |
|------|-------|----------|
| Starter | ₦15,000/mo | Basic expense tracking + monthly report |
| Pro | ₦25,000/mo | Full automation + weekly reports + voice alerts |
| Enterprise | ₦50,000/mo | Custom integrations + daily reports + dedicated analyst |

9. Click **Save**. Set the page as your homepage under **Online Store → Preferences → Homepage**.

## Procedure 5.2: Set Up Lead Generation with Apollo.io

1. Visit **https://www.apollo.io** and click **Sign Up Free**.
2. Complete the onboarding — select **"Sales"** as your role and **"Small Business"** as your company size.
3. Go to **Search → People** and apply these filters:
   - **Location:** Nigeria (or your target country)
   - **Title:** CFO, Finance Director, Finance Manager, Business Owner
   - **Company Size:** 1–50 employees
4. Click **Search**. Do you see a list of prospects with email addresses?
5. Select **25 prospects** by checking the boxes next to their names.
6. Click **Save → Save to List** and create a list called **"Finance Prospects — Q1"**.
7. Click **Email → Compose Sequence**. Write a 3-email sequence:
   - **Email 1 (Day 1):** "Hi {first_name}, I noticed you're managing finances at {company}. Our AI tool automates expense tracking and saves 10+ hours per month. Can I show you a 5-minute demo?"
   - **Email 2 (Day 3):** "Hi {first_name}, just following up. Here's a free sample report I generated for a company like {company}: [link]. Would love to walk you through it."
   - **Email 3 (Day 7):** "Hi {first_name}, last email — our Pro plan is ₦25,000/month and typically pays for itself in the first week. Book a call: [Calendly link]"
8. Click **Activate Sequence**. Do you see the sequence status as "Active"?

## Procedure 5.3: Create an Automated Email Nurture Sequence in Klaviyo

1. Log in to **Klaviyo** at https://www.klaviyo.com.
2. Go to **Flows → Create Flow → Create from Scratch**.
3. Name the flow **"Lead Nurture — Finance Bot"**.
4. Set the trigger to **"When someone is added to the 'Finance Leads' list"**.
5. Add the following email sequence:
   - **Email 1 (Immediate):** "Welcome! Here's your free Financial Health Checklist" — attach a PDF with a simple budget template.
   - **Email 2 (Day 2):** "See how AI analyzes your spending in 60 seconds" — include a screenshot or GIF of the Replit app.
   - **Email 3 (Day 5):** "3 ways AI saves you ₦100,000/year on subscriptions" — include a sample subscription audit.
   - **Email 4 (Day 7):** "Ready to automate? Book your free demo" — include your Calendly link.
6. Click **Save** and then **Activate Flow**.
7. Do you see the flow listed as "Live" in your Flows dashboard?

## Check-In: Module 5 Complete
- [ ] Shopify landing page live with email capture form and pricing tiers
- [ ] Apollo.io prospect list created with 25+ leads
- [ ] 3-email outreach sequence active in Apollo.io
- [ ] Klaviyo nurture flow live with 4-email sequence

---

# MODULE 6: DELIVERY – Build Your Client Delivery Pipeline

## Overview
Delivery is where the money is made. This module ensures you can deliver consistent, high-quality results to every client without burning out. You will build a repeatable delivery pipeline with quality checkpoints and client communication templates.
**Time to complete:** 60 minutes
**Tools needed:** Make.com, Notion, Loom

## Procedure 6.1: Build the Client Delivery Automation in Make.com

1. In Make.com, create a new scenario named **"Client Delivery Pipeline"**.
2. Add a **Schedule** trigger: Set it to run **every Monday at 8:00 AM**.
3. Add a **HTTP** module: Configure it to call your Replit app's `/analyze` endpoint with each active client's transaction data.
4. Add a **Klaviyo** module: Send the analysis report to each client's email with the subject **"Your Weekly Financial Analysis — {date}"**.
5. Add a **Notion** module: Create a new entry in the **Client Pipeline** table for each client, updating the **Status** to "Active" and logging the report date.
6. Click **Save** and **Activate** the scenario.
7. Do you see the scenario listed as "On" in your Make.com dashboard?

## Procedure 6.2: Create Client Communication Templates

1. Open your Notion workspace and create a new page titled **"Client Communication Templates"**.
2. Add the following templates:

**Welcome Email:**
```
Subject: Welcome to AI Finance Automation, {client_name}!

Hi {client_name},

Your AI Personal Finance Automation system is now live. Here's what to expect:
- Weekly financial analysis reports delivered to your inbox every Monday
- Real-time budget alerts when you exceed 30% in any category
- Monthly savings recommendations based on the 50/30/20 rule

Your dashboard: https://myfinancebot.com/dashboard/{client_id}
Book a check-in call: {calendly_link}

Best,
{your_name}
```

**Monthly Review Email:**
```
Subject: Your Month-in-Review — {month} Financial Summary

Hi {client_name},

Here's your {month} financial summary:
- Total Income: {total_income}
- Total Expenses: {total_expenses}
- Savings Rate: {savings_rate}%
- Top Budget Alert: {top_alert}

Full report: https://myfinancebot.com/report/{report_id}

Any questions? Book a call: {calendly_link}
```

3. Save both templates. Do you see them in Notion? Use these for every new client.

## Check-In: Module 6 Complete
- [ ] Client Delivery Pipeline scenario running weekly in Make.com
- [ ] Welcome email and monthly review templates created in Notion
- [ ] Automated report delivery confirmed via Klaviyo

---

# MODULE 7: SCALING – From Solo to Team

## Overview
Scaling a boutique AI service requires disciplined delegation, documented SOPs, and margin analysis. This module transforms your one-person operation into a lean, repeatable system that can handle 10–50 clients without breaking.
**Time to complete:** 90 minutes
**Tools needed:** Notion, Upwork, Google Sheets

## Procedure 7.1: Hire Your First Contractor on Upwork

1. Visit **https://www.upwork.com** and create a client account.
2. Click **Post a Job** and fill in:
   - **Title:** "Make.com Automation Specialist — AI Finance Bot"
   - **Description:** "Build & maintain Make.com scenarios for a ChatGPT-powered budgeting tool. Must have experience with Make.com, API integrations, and Python. Monthly deliverables: 5 new scenario builds, 2 performance reviews. $25–35/hr, 20 hours/week."
   - **Skill Level:** Intermediate
   - **Budget:** Hourly, $30/hr
3. Click **Post Job**. Do you see "Your job is live" confirmation?
4. Wait 24 hours for proposals to arrive. Shortlist 3–5 candidates based on:
   - Make.com experience (look for portfolio screenshots)
   - API integration experience
   - Response time and communication quality
5. Send each shortlisted candidate the same test task: "Describe how you would build a Make.com scenario that triggers on a new Stripe payment and sends a customized email via Klaviyo."
6. Hire the best candidate and create a **Notion** page for onboarding with links to all API keys, the service delivery framework, and communication templates.

## Procedure 7.2: Build SOPs for Task Delegation in Notion

1. In Notion, create a new page titled **"Standard Operating Procedures (SOPs)"**.
2. Create the following SOP documents:
   - **SOP-001: New Client Onboarding** — Steps from discovery call to first report delivery (15 steps)
   - **SOP-002: Weekly Report Generation** — How to run the Make.com pipeline and verify output (8 steps)
   - **SOP-003: Client Support Escalation** — How to handle support requests, when to escalate (6 steps)
   - **SOP-004: Monthly Review Call** — Preparation checklist and talking points (10 steps)
3. For each SOP, use this format:
   - **Purpose:** Why this SOP exists
   - **Owner:** Who is responsible
   - **Time Estimate:** How long it takes
   - **Steps:** Numbered, detailed instructions
   - **Check-In:** What "done" looks like
4. Do you see all 4 SOPs in the Notion page? Share the page with your contractor.

## Procedure 7.3: Run a Margin Analysis

1. Open **Google Sheets** and create a new spreadsheet titled **"Margin Analysis — AI Finance Bot"**.
2. Create the following table:

| Metric | Starter (₦15K) | Pro (₦25K) | Enterprise (₦50K) |
|--------|-----------------|-------------|---------------------|
| Monthly Revenue | ₦15,000 | ₦25,000 | ₦50,000 |
| API Costs (OpenAI) | ₦2,000 | ₦3,000 | ₦5,000 |
| Make.com | ₦1,500 | ₦1,500 | ₦1,500 |
| Hosting (Hostinger) | ₦800 | ₦800 | ₦800 |
| Contractor Cost | ₦0 | ₦3,000 | ₦6,000 |
| Email (Klaviyo) | ₦0 | ₦0 | ₦3,000 |
| **Total Costs** | **₦4,300** | **₦8,300** | **₦16,300** |
| **Gross Profit** | **₦10,700** | **₦16,700** | **₦33,700** |
| **Margin** | **71%** | **67%** | **67%** |

3. Below the table, add a **Break-Even Calculator**:
   - Monthly fixed costs: ₦50,000 (hosting + tools + contractor)
   - Average client revenue: ₦25,000
   - Break-even clients: 50,000 / 16,700 = **3 Pro clients**
4. Do you see the break-even point? With just 3 Pro clients, you cover all costs.

## Check-In: Module 7 Complete
- [ ] Upwork job posted for Make.com specialist
- [ ] 4 SOPs documented in Notion
- [ ] Margin analysis spreadsheet completed
- [ ] Break-even point calculated (3 Pro clients)

---

# MODULE 8: ADVANCED PATTERNS – Premium Techniques and Upsells

## Overview
This module converts your lean MVP into a recurring-revenue engine. You will add high-ticket consulting packages, productize the bot into a subscription SaaS, and create upsell paths that increase client lifetime value from ₦25,000/month to ₦75,000+/month.
**Time to complete:** 90 minutes
**Tools needed:** Shopify, Stripe, Make.com

## Procedure 8.1: Create a High-Ticket Consulting Package

1. In your **Shopify** admin, go to **Products → Add product**.
2. Create a product titled **"Financial Freedom Blueprint — 12-Month Consulting"**.
3. Set the price to **₦500,000** (one-time) or **₦50,000/month** for 12 months.
4. In the description, include:
   - Monthly 1-on-1 strategy calls (30 minutes)
   - Custom AI model trained on your specific financial data
   - Voice-enabled financial assistant via Vapi
   - Priority support with 4-hour response time
   - Quarterly business review with margin optimization
5. Under **Inventory**, uncheck **Track quantity** (this is a service, not a physical product).
6. Click **Save product**. Do you see it listed in your Products page?
7. Add a **Make.com** scenario that triggers when this product is purchased:
   - Trigger: **Shopify → New Order** (filter by product = "Financial Freedom Blueprint")
   - Action 1: **Klaviyo → Add to List** ("Premium Clients")
   - Action 2: **Notion → Create Page** (in Client Pipeline, set Status = "Onboarding", Revenue = ₦50,000)
   - Action 3: **Slack/Email → Send Notification** to you ("New Premium client signed up!")

## Procedure 8.2: Build Recurring Revenue with Subscription Tiers on Shopify

1. In Shopify, go to **Settings → Payments** and enable **Shopify Payments**.
2. Install the **Recharge** app from the Shopify App Store for subscription management.
3. Create 3 subscription products:

| Tier | Monthly Price | Annual Price (20% discount) | Deliverables |
|------|---------------|------------------------------|-------------|
| Starter | ₦15,000 | ₦144,000 | Weekly report, basic alerts |
| Pro | ₦25,000 | ₦240,000 | Weekly report, voice alerts, monthly review |
| Enterprise | ₦50,000 | ₦480,000 | Daily reports, custom integrations, dedicated analyst |

4. Set billing to **monthly** with **annual discount** option.
5. Add an **upsell flow** in Klaviyo: After 30 days on Starter, send an email offering a Pro upgrade with a 14-day free trial.
6. Click **Save**. Do you see all 3 subscription products active in your store?

## Check-In: Module 8 Complete
- [ ] High-ticket consulting product created on Shopify
- [ ] Make.com automation for premium client onboarding active
- [ ] 3 subscription tiers set up with annual discount options
- [ ] Upsell flow configured in Klaviyo

---

# MODULE 9: FINANCIAL OPERATIONS – Revenue Tracking and Billing

## Overview
This module builds your financial backbone. You will create a live revenue dashboard, set up automated billing, and create professional proposal templates. Without these systems, you will lose track of payments, miss renewals, and leave money on the table.
**Time to complete:** 60 minutes
**Tools needed:** Notion, Make.com, Stripe

## Procedure 9.1: Build a Live Revenue Dashboard in Notion

1. In Notion, create a new page titled **"Revenue Dashboard"**.
2. Create a **Table** database with columns:
   - **Client** (Title)
   - **Tier** (Select: Starter, Pro, Enterprise, Consulting)
   - **Monthly Revenue** (Number, Naira)
   - **Status** (Select: Active, Past Due, Cancelled)
   - **Start Date** (Date)
   - **Next Billing** (Formula: `dateAdd(prop("Start Date"), 1, "months")`)
   - **Lifetime Value** (Rollup from payments table)
3. Add a **Summary** view at the top with these formulas:
   - **Total MRR:** `sum(prop("Monthly Revenue"))` where Status = Active
   - **Active Clients:** `count()` where Status = Active
   - **Average Revenue per Client:** Total MRR / Active Clients
4. Create a second table called **"Payments"** with columns:
   - **Date** (Date)
   - **Client** (Relation to Revenue Dashboard)
   - **Amount** (Number)
   - **Status** (Select: Paid, Pending, Failed)
5. Add a **Make.com** scenario: Trigger = **Stripe → New Payment** → Action = **Notion → Create Entry** in Payments table.
6. Activate the scenario. Do you see it running in Make.com?

## Procedure 9.2: Create Proposal Templates and Automated Billing

1. In Notion, create a page titled **"Proposal Templates"**.
2. Write a template for new client proposals:

```
PROPOSAL: AI Personal Finance Automation
Client: {client_name}
Date: {date}

RECOMMENDED TIER: {tier}
MONTHLY INVESTMENT: {price}

WHAT YOU GET:
✅ Automated expense tracking and categorization
✅ Weekly financial analysis reports via email
✅ Real-time budget alerts (30% threshold)
✅ Monthly savings recommendations (50/30/20 rule)
✅ Subscription audit and cancellation suggestions

ROI PROJECTION:
Based on average savings of ₦100,000/year from subscription optimization
and 10+ hours/month saved on manual tracking at ₦5,000/hour:
Annual savings: ₦700,000+
Monthly time saved: 10+ hours

NEXT STEPS:
1. Sign up via {shopify_link}
2. Complete onboarding form (5 minutes)
3. First report delivered within 24 hours
```

3. Set up **Stripe** automated billing:
   - Log in to https://dashboard.stripe.com
   - Go to **Products → Add Product** for each subscription tier
   - Set **Recurring** billing with monthly interval
   - Copy the **Payment Link** for each product
4. Add the Stripe payment links to your Shopify landing page.

## Check-In: Module 9 Complete
- [ ] Revenue Dashboard live in Notion with MRR calculation
- [ ] Payments table linked to Stripe via Make.com
- [ ] Proposal template created in Notion
- [ ] Stripe billing set up for all 3 tiers

---

# MODULE 10: LAUNCH PLAN – Your 30-Day Execution Calendar

## Overview
This is your action plan to go from zero to first paying client in 30 days. Every day has a specific task. Follow the calendar exactly — no skipping, no rearranging. The sequence is designed so each day builds on the previous one.
**Time to complete:** 30 days (1–3 hours/day)
**Tools needed:** All tools from previous modules

## Procedure 10.1: Execute Days 1–15 (Foundation to First Build)

| Day | Task | Time | Tool |
|-----|------|------|------|
| 1 | Complete Module 1 — set up Hostinger, Notion, Calendly | 90 min | Hostinger, Notion, Calendly |
| 2 | Complete Module 2 — collect all API keys, run health check | 75 min | Make.com, OpenAI |
| 3 | Complete Module 3 — design service framework, test prompts | 60 min | Notion, ChatGPT |
| 4 | Build Replit app (Module 4, Procedure 4.1) | 2 hrs | Replit |
| 5 | Build Make.com pipeline (Module 4, Procedure 4.2) | 90 min | Make.com, Klaviyo |
| 6 | Deploy to production (Module 4, Procedure 4.3) | 60 min | Hostinger, GitHub |
| 7 | Build Shopify landing page (Module 5, Procedure 5.1) | 60 min | Shopify |
| 8 | Set up Apollo.io lead list (Module 5, Procedure 5.2) | 45 min | Apollo.io |
| 9 | Create Klaviyo nurture flow (Module 5, Procedure 5.3) | 45 min | Klaviyo |
| 10 | Send first 25 outreach emails via Apollo.io | 30 min | Apollo.io |
| 11 | Follow up on responses — schedule discovery calls | 60 min | Calendly |
| 12 | Conduct 3–5 discovery calls | 2 hrs | Calendly, Loom |
| 13 | Send proposals to qualified leads | 60 min | Notion, Stripe |
| 14 | Build delivery pipeline (Module 6) | 60 min | Make.com |
| 15 | QA test entire system end-to-end | 90 min | All tools |

Do you have all tasks for Days 1–15 logged in your Notion workspace? Create a **Checklist** page and mark each day as complete.

## Procedure 10.2: Execute Days 16–30 (Delivery to Revenue)

| Day | Task | Time | Tool |
|-----|------|------|------|
| 16 | Deliver first client onboarding (welcome email, dashboard access) | 60 min | Klaviyo, Notion |
| 17 | Run first automated report for client | 30 min | Make.com |
| 18 | Check in with client — collect feedback | 30 min | Calendly |
| 19 | Send second round of outreach emails (25 more leads) | 30 min | Apollo.io |
| 20 | Optimize landing page based on first client feedback | 60 min | Shopify |
| 21 | Set up Stripe billing for active clients | 45 min | Stripe |
| 22 | Build margin analysis spreadsheet (Module 7, Procedure 7.3) | 45 min | Google Sheets |
| 23 | Document SOPs (Module 7, Procedure 7.2) | 90 min | Notion |
| 24 | Create consulting upsell package (Module 8, Procedure 8.1) | 60 min | Shopify |
| 25 | Set up subscription tiers (Module 8, Procedure 8.2) | 60 min | Shopify, Recharge |
| 26 | Build revenue dashboard (Module 9, Procedure 9.1) | 45 min | Notion, Make.com |
| 27 | Create proposal templates (Module 9, Procedure 9.2) | 45 min | Notion, Stripe |
| 28 | Review all automation scenarios — fix any errors | 90 min | Make.com |
| 29 | Conduct 30-day review with first client — ask for referral | 60 min | Calendly, Loom |
| 30 | **MILESTONE: Calculate MRR and set Month 2 targets** | 30 min | Notion |

## Procedure 10.3: Set Your Month 2 Growth Targets

1. Open your Notion **Revenue Dashboard**.
2. Add a new page titled **"Month 2 Targets"**.
3. Set these targets:

| Metric | Month 1 (Actual) | Month 2 (Target) | Growth |
|--------|-------------------|-------------------|--------|
| Active Clients | {count} | {count} + 3 | +3 |
| Monthly Recurring Revenue | ₦{amount} | ₦{amount} + ₦75,000 | +3 Pro clients |
| Outreach Emails Sent | 50 | 100 | +50 |
| Discovery Calls Booked | 5 | 10 | +5 |
| Conversion Rate | {rate}% | 30% | Optimize |

4. Identify your **#1 bottleneck** from Month 1:
   - If leads < 10 → invest more time in Apollo.io outreach
   - If calls < 5 → improve your landing page and email copy
   - If conversions < 20% → improve your discovery call script
5. Write your bottleneck and action plan in the Month 2 Targets page.

## Check-In: Module 10 Complete
- [ ] Days 1–15 tasks completed and logged in Notion
- [ ] Days 16–30 tasks completed
- [ ] First paying client onboarded and receiving reports
- [ ] Month 2 targets documented with growth plan

---

# APPENDIX A: COMPLETE TOOL REFERENCE

| Tool | Purpose | Free Tier | Paid Tier | When to Upgrade |
|------|---------|-----------|-----------|-----------------|
| **Hostinger** | Web hosting & domain management | 1 GB SSD, free domain for 1 year | 5 GB SSD, 30 GB storage, $3.95/mo | When you exceed 1 GB bandwidth |
| [**Replit**](https://replit.com/refer/egwuokwor) | Cloud IDE for rapid prototyping | Unlimited public repos, 500 MB storage | 1 GB storage, private repos, $7/mo | When you need private code |
| [**Make.com**](https://www.make.com/en/register?pc=menshly) | Low-code automation hub | 1,000 operations/month, 5 scenarios | 10,000 ops/month, $9/mo | When you hit 1,000 ops/month |
| **Vapi** | AI voice-agent platform | 5 voice calls/month | 10,000 calls/month, $15/mo | When your user base scales past free tier |
| [**ElevenLabs**](https://elevenlabs.io/) | AI voice synthesis | 10,000 characters/month | 50,000 chars/month, $5/mo | When you need higher TTS volume |
| **Klaviyo** | Email marketing & automation | 250 contacts, 500 emails/month | 1,000 contacts, $20/mo | When you exceed 250 contacts |
| **ActiveCampaign** | CRM + email automation | 500 contacts, 2,000 emails/month | 1,000 contacts, $15/mo | When you need advanced automation |
| [**Semrush**](https://www.semrush.com/) | SEO & competitive research | 10 searches/day | Full access, $129/mo | When you need deeper keyword analysis |
| **Shopify** | E-commerce storefront & checkout | 3-day free trial | Unlimited products, $29/mo | After trial ends |
| **Zapier** | App automation | 100 tasks/month | 2,000 tasks/month, $20/mo | When you need more than 100 tasks/month |
| **Apollo.io** | B2B sales intelligence | 500 credits/month | Unlimited, $49/mo | When you need larger prospect lists |
| **PhantomBuster** | LinkedIn automation | 1,000 requests/month | 5,000 requests/month, $59/mo | When you need more LinkedIn outreach |
| **Buffer** | Social media scheduling | 3 accounts, 10 posts/month | 10 accounts, 100 posts, $6/mo | When you exceed 10 posts/month |
| **Loom** | Video messaging | 5 minutes recording/day | Unlimited recording, $13/mo | When you need longer recordings |
| **Calendly** | Scheduling appointments | 1 calendar, 1 event type | 5 calendars, $10/mo | When you need multiple event types |
| [**Beehiiv**](https://beehiiv.com/) | Newsletter platform | 500 subscribers | 2,500 subscribers, $39/mo | When you exceed 500 subscribers |
| **Notion** | Workspace & documentation | Unlimited pages, 5,000 blocks | Unlimited blocks, $8/mo | When you hit 5,000 blocks |
| **Midjourney** | AI image generation | 200 generations/month | 1,200 generations/month, $10/mo | When you need more image generations |
| [**Grammarly**](https://grammarly.com/) | AI writing assistant | Basic suggestions | Full suggestions, $12/mo | When you need advanced grammar checks |

*Key take-away:* Start with free tiers to keep costs under ₦10,000/month. Upgrade only when usage metrics cross the thresholds above.

---

# APPENDIX B: THE COMPLETE SOP INDEX

| SOP # | Procedure | Category | Difficulty | Est. Time |
|-------|-----------|----------|------------|-----------|
| 1.1 | Create Hostinger Hosting & Domain | Foundation | Easy | 60 min |
| 1.2 | Set Up Notion Workspace for Client Data | Foundation | Easy | 20 min |
| 1.3 | Configure Calendly for Onboarding Calls | Foundation | Easy | 15 min |
| 2.1 | Create Make.com Account & API Token | Tech Stack | Easy | 30 min |
| 2.2 | Create and Store All API Keys | Tech Stack | Medium | 45 min |
| 2.3 | Build Make.com API Health Check | Tech Stack | Medium | 30 min |
| 3.1 | Design Service Delivery Framework | Framework | Medium | 45 min |
| 3.2 | Create AI Prompt Template for Analysis | Framework | Medium | 30 min |
| 4.1 | Build Core Finance Analysis App in Replit | First Build | Hard | 90 min |
| 4.2 | Create Make.com Workflow for Pipeline | First Build | Medium | 60 min |
| 4.3 | Deploy App to Production on Hostinger | First Build | Hard | 60 min |
| 5.1 | Build Landing Page on Shopify | Client Acquisition | Medium | 60 min |
| 5.2 | Set Up Lead Generation with Apollo.io | Client Acquisition | Medium | 45 min |
| 5.3 | Create Email Nurture Sequence in Klaviyo | Client Acquisition | Medium | 45 min |
| 6.1 | Build Client Delivery Automation | Delivery | Medium | 45 min |
| 6.2 | Create Client Communication Templates | Delivery | Easy | 30 min |
| 7.1 | Hire First Contractor on Upwork | Scaling | Medium | 60 min |
| 7.2 | Build SOPs for Task Delegation | Scaling | Easy | 60 min |
| 7.3 | Run Margin Analysis | Scaling | Medium | 30 min |
| 8.1 | Create High-Ticket Consulting Package | Advanced Patterns | Medium | 45 min |
| 8.2 | Build Subscription Tiers on Shopify | Advanced Patterns | Medium | 60 min |
| 9.1 | Build Live Revenue Dashboard in Notion | Financial Ops | Medium | 45 min |
| 9.2 | Create Proposal Templates & Billing | Financial Ops | Medium | 45 min |
| 10.1 | Execute Days 1–15 Launch Calendar | Launch Plan | Mixed | 30 days |
| 10.2 | Execute Days 16–30 Launch Calendar | Launch Plan | Mixed | 15 days |
| 10.3 | Set Month 2 Growth Targets | Launch Plan | Easy | 30 min |

*Note:* Each SOP is designed to be completed in 15–90 minutes. The total execution time across all procedures is approximately 12+ hours of focused work.

---

# APPENDIX C: THE REVENUE CALCULATOR

## Revenue Projections

| Month | Revenue | Clients | Expenses | Profit |
|-------|---------|---------|----------|--------|
| 1 | ₦25,000 | 1 | ₦8,300 | ₦16,700 |
| 3 | ₦75,000 | 3 | ₦16,000 | ₦59,000 |
| 6 | ₦175,000 | 7 | ₦28,000 | ₦147,000 |
| 12 | ₦500,000 | 15 | ₦55,000 | ₦445,000 |

## Pricing Tiers

| Tier | Monthly Price | Deliverables | Margin |
|------|---------------|-------------|--------|
| Starter | ₦15,000 | Weekly report, basic alerts | 71% |
| Pro | ₦25,000 | Weekly report, voice alerts, monthly review | 67% |
| Enterprise | ₦50,000 | Daily reports, custom integrations, analyst | 67% |
| Consulting | ₦50,000/month | 1-on-1 calls, custom AI, priority support | 75% |

## Break-Even Analysis

| Metric | Value |
|--------|-------|
| Monthly Fixed Costs | ₦50,000 |
| Average Revenue per Client | ₦25,000 |
| Average Gross Margin | 67% |
| Break-Even Clients | 3 Pro clients |
| Break-Even Revenue | ₦75,000/month |
| Time to Break-Even | ~3 months |

*Key take-away:* You need just 3 Pro clients to cover all costs. Every client after that is pure profit. Focus on acquiring your first 3 clients as fast as possible.

## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
- **[Notion](https://notion.so/)** — All-in-one workspace — notes, docs, project management
