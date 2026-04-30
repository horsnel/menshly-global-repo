---
title: "Build, Configure, and Deploy an AI Appointment Booking System with Vapi and Calendly"
date: 2026-04-30
category: "Implementation"
difficulty: "INTERMEDIATE"
readTime: "25 MIN"
excerpt: "This is the execution guide for building the **AI Appointment Booking Automation** business we outlined in our opportunity deep‑dive.  Follow the steps below and you’ll have a fully‑functional, voice‑..."
image: "/images/articles/intelligence/build-and-deploy-ai-appointment-booking-systems-with-vapi-and-calendly.png"
heroImage: "/images/heroes/intelligence/build-and-deploy-ai-appointment-booking-systems-with-vapi-and-calendly.png"
relatedOpportunity: "/opportunities/how-to-launch-an-ai-appointment-booking-automation-business-in-2026-2k15kmonth/"
---

This is the execution guide for building the **AI Appointment Booking Automation** business we outlined in our opportunity deep‑dive.  Follow the steps below and you’ll have a fully‑functional, voice‑powered scheduling system that can be sold to medical practices, law firms, or any service‑based business that needs to reduce no‑shows and manual booking overhead.

Ready to understand the full business opportunity? Read our [opportunity deep‑dive](/opportunities/how-to-launch-an-ai-appointment-booking-automation-business-in-2026-2k15kmonth.md).

---

## Prerequisites

| Item | Account / Tool | Cost | Setup Time |
|------|----------------|------|------------|
| Voice AI platform | [**Vapi**](https://vapi.ai/) | $19 / month (Starter) | 5 min |
| Scheduling API | **Calendly** | Free (Basic) | 5 min |
| Automation & webhook | [**Make.com**](https://www.make.com/en/register?pc=menshly) | $9 / month (Starter) | 5 min |
| Cloud IDE & runtime | [**Replit**](https://replit.com/refer/egwuokwor) | Free tier | 5 min |
| Web hosting | **Hostinger** | $3.95 / month (Single Shared) | 10 min |
| Knowledge base | [**Notion**](https://notion.so/) | Free | 5 min |
| AI assistant | **ChatGPT** | $20 / month | 5 min |
| TTS synthesis | [**ElevenLabs**](https://elevenlabs.io/) | $10 / month | 5 min |
| Email marketing | **Klaviyo** | $20 / month | 10 min |
| **Total upfront cost** |  | **$88.95 / month** |  |

> **Note:** All costs are the lowest paid tiers that include the APIs we’ll use.  You can start on free tiers and upgrade after you validate the business model.

---

## Step 1: Setup Accounts and API Keys

> **Goal:** Create all necessary accounts, generate API keys, and store them securely in Replit’s secrets manager.

### 1.1 Create a Vapi Account

1. Navigate to **https://app.vapi.io**.
2. Click **Sign Up** → email → password → **Create Account**.
3. Verify email, log in.
4. In the dashboard, click **Manage API Keys** → **Create Key**.
5. Name it `PROD_VAPI_KEY`, set **Read & Write** scope, click **Create**.
6. Copy the key to clipboard.

> **Check‑in:** Do you see “Manage API Keys” under the **Settings** menu?  
> If not, ensure you’re in the **Admin** view.  Go back and re‑log.

### 1.2 Create a Calendly Account

1. Go to **https://calendly.com**.
2. Sign up with your email.  
3. In the **Integrations** tab, click **API**.
4. Click **Generate New API Key** → `CAL_API_KEY`.  
5. Copy the key to clipboard.

> **Check‑in:** Do you see your API key under “API Keys” with a 32‑character string?  
> If you see “API Key expired”, click **Regenerate**.

### 1.3 Create a Make.com (Integromat) Account

1. Visit **https://www.make.com**.
2. Sign up with email → password → **Create account**.
3. In the dashboard, click **Create new scenario** → choose **Webhook** as first module.
4. Copy the **Webhook URL** (we’ll paste it into Vapi later).

> **Check‑in:** Do you see a “Webhook” module with a URL that starts with `https://hook.integromat.com/

# Build, Configure, and Deploy an AI Appointment Booking System with Vapi and Calendly

This is the execution guide for building the **AI Appointment Booking Automation** business we outlined in our opportunity deep‑dive.  Follow the steps below and you’ll have a fully‑functional, voice‑powered scheduling system that can be sold to medical practices, law firms, or any service‑based business that needs to reduce no‑shows and manual booking overhead.

Ready to understand the full business opportunity? Read our [opportunity deep‑dive](/opportunities/how-to-launch-an-ai-appointment-booking-automation-business-in-2026-2k15kmonth.md).

---

## Prerequisites

| Item | Account / Tool | Cost | Setup Time |
|------|----------------|------|------------|
| Voice AI platform | **Vapi** | $19 / month (Starter) | 5 min |
| Scheduling API | **Calendly** | Free (Basic) | 5 min |
| Automation & webhook | **Make.com** | $9 / month (Starter) | 5 min |
| Cloud IDE & runtime | **Replit** | Free tier | 5 min |
| Web hosting | **Hostinger** | $3.95 / month (Single Shared) | 10 min |
| Knowledge base | **Notion** | Free | 5 min |
| AI assistant | **ChatGPT** | $20 / month | 5 min |
| TTS synthesis | **ElevenLabs** | $10 / month | 5 min |
| Email marketing | **Klaviyo** | $20 / month | 10 min |
| **Total upfront cost** |  | **$88.95 / month** |  |

> **Note:** All costs are the lowest paid tiers that include the APIs we’ll use.  You can start on free tiers and upgrade after you validate the business model.

---

## Step 1: Setup Accounts and API Keys (Continued)

### 1.3 Create a Make.com (Integromat) Account (continued)

1. Copy the **Webhook URL** (it looks like `https://hook.integromat.com/xxxxxx`).  
2. **Do you see a “Webhook” module with a URL that starts with `https://hook.integromat.com/`?**  
   - If yes, proceed to the next step.  
   - If no, check that you selected the **HTTP > Webhooks** module and that it is set to **“Custom webhook”**.  Go back and re‑create the scenario.

### 1.4 Store API Keys in Replit Secrets

1. Go to **Replit.com**, click **New Repl** → language **Python** (or **Node.js** if you prefer).  
2. Name the repl `vapi-calendly-booker`.  
3. In the left sidebar, click the **Secrets (Environment Variables)** icon (`⚙️`).  
4. Add the following secrets (click “Add new secret” for each):  

   | Key | Value |
   |-----|-------|
   | `VAPI_KEY` | *Your Vapi API key* |
   | `CALENDLY_KEY` | *Your Calendly API key* |
   | `MAKESHOP_URL` | *Your Make.com webhook URL* |
   | `ELEVENLABS_KEY` | *ElevenLabs API key (optional)* |
   | `KLAVIYO_API_KEY` | *Klaviyo API key (optional)* |

5. **Check‑in:** Do you see a green checkmark next to each secret?  
   - If not, you may have mistyped the key name or value.  Delete and re‑enter.

### 1.5 Verify Connectivity

Open the Replit console and run:

```bash
curl -I https://api.vapi.io
```

You should receive:

```
HTTP/2 200
...
```

If you see `401 Unauthorized`, double‑check your `VAPI_KEY` secret.

---

## Step 2: Build Core Component – Voice‑to‑Calendly Scheduler

### 2.1 Create the Replit Project Skeleton

1. In the Replit editor, create a new file `app.py`.  
2. Install required packages by opening the **Shell** tab and running:

```bash
pip install flask requests python-dotenv
```

3. Create a `.env` file (not needed if you use Replit secrets, but useful for local dev).  
   Add:

```
VAPI_KEY=your_vapi_key
CALENDLY_KEY=your_calendly_key
MAKESHOP_URL=your_make_webhook_url
```

> **Check‑in:** Do you see a `requirements.txt` file that lists `flask, requests, python-dotenv`?  
> If not, run `pip freeze > requirements.txt` after installing.

### 2.2 Build the Vapi Webhook Listener

Vapi will POST JSON payloads to a URL you specify.  We’ll expose a public URL via **Make.com** → **HTTP > Webhooks** → **Get URL**.  Copy that URL and set it in Vapi’s “Webhook URL” field.

In `app.py`:

```python
import os
import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

VAPI_KEY = os.getenv("VAPI_KEY")
CALENDLY_KEY = os.getenv("CALENDLY_KEY")
MAKESHOP_URL = os.getenv("MAKESHOP_URL")
ELEVENLABS_KEY = os.getenv("ELEVENLABS_KEY")

@app.route("/vapi/webhook", methods=["POST"])
def vapi_webhook():
    payload = request.json
    # 

## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Vapi](https://vapi.ai/)** — AI voice agent platform — build and deploy voice AI
- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
