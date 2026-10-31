---
title: "The AI Newsletter Automation Playbook: 25 Steps to $20K/Month"
date: 2026-10-31
category: "Playbook"
price: "₦35,000"
readTime: "80 MIN"
excerpt: "The AI Newsletter Automation Playbook: 25 Steps to $20K/Month You will master the end‑to‑end design, build, and automation of AI‑driven newsletters using Beehiiv and Mailchimp, turning your expertise into a scalable $20,000/month recurring revenue en..."
image: "/images/articles/playbooks/design-build-and-automate-ai-newsletter-workflows-with-beehiiv-and-mailchimp.png"
heroImage: "/images/heroes/playbooks/design-build-and-automate-ai-newsletter-workflows-with-beehiiv-and-mailchimp.png"
relatedOpportunity: "/opportunities/how-to-build-an-ai-newsletter-service-18k-25kmonth/"
relatedGuide: "/intelligence/build-an-ai-seo-optimization-service-with-semrush-the-complete-step-by-step-guid/"
---
**The AI Newsletter Automation Playbook: 25 Steps to $20K/Month**  
You will master the end‑to‑end design, build, and automation of AI‑driven newsletters using Beehiiv and Mailchimp, turning your expertise into a scalable $20,000/month recurring revenue engine. This playbook is a fully fledged OPERATING SYSTEM, not a blog post or loose guide, and it delivers every SOP, code snippet, and revenue calculator required to execute with precision. **25 procedures. 10 modules. 12+ hours of reading and execution.** By following each step, you will create a repeatable workflow that recruits clients, curates AI‑generated content, integrates with Zapier‑driven A/B testing, and leverages Mailchimp’s segmentation to boost CTRs by 30% on average. You will also set up automated subscription billing, deliver high‑quality AI content via [Fliki AI](https://fliki.ai?referral=noah-wilson-w84be4) voice‑overs, and scale to 5,000 subscribers in 90 days. This playbook extends our free implementation guide with complete procedures, SOPs, and revenue calculators. For the free step‑by‑step guide, see our [implementation guide](/intelligence/build-an-ai-seo-optimization-service-with-semrush-the-complete-step-by-step-guid.md).

---

# MODULE 1: FOUNDATION

## Overview

This module is the bedrock of your AI‑powered newsletter empire. It covers everything from registering your business, securing a domain, setting up a professional email address, and provisioning the core tools that will power every automation and content workflow you’ll later build. Skipping any of these foundational steps will leave you with broken brand identity, legal compliance gaps, and unreliable delivery pipelines—ultimately causing you to lose subscribers, spam complaints, and trust. By the end of this module you will own a fully‑qualified business entity, a custom domain tied to a reputable registrar, a dedicated email system with DKIM/SPF records, and a verified Mailchimp and Beehiiv account ready for API integration.

The procedure is deliberately modular: you will first create a Google Workspace account, then purchase a domain from Hostinger, configure DNS with Cloudflare, set up a Mailchimp account, and finally register with Beehiiv. Each step has a clear, repeatable path and expected outputs. You will verify deliverability by sending test emails, ensuring SPF, DKIM, and DMARC records are passing. This groundwork guarantees that all later AI‑driven content creation, scheduling, and automation processes run on a stable, compliant infrastructure.

| Tool        | Purpose                                                       | Free Tier                                      | Paid Tier (Monthly) |
|-------------|--------------------------------------------------------------|------------------------------------------------|---------------------|
| Hostinger   | Domain registration & web hosting                            | $0.99 for 1‑year domain (standard)             | $4.99 (Starter)     |
| Cloudflare  | DNS management & CDN, SSL                                     | Unlimited free plan                            | Pro: $20.00         |
| Google Workspace | Professional email (Gmail), calendar, Drive            | 30 GB free for 3 months (Google Workspace Basic) | 6 GB: $6.00         |
| Mailchimp   | Email marketing, automation, API access                       | 2 000 contacts, 10 000 sends/month             | Essentials: $13.00  |
| Beehiiv     | AI‑driven newsletter publishing & analytics                  | 5 000 subscribers (free tier)                  | Pro: $30.00         |
| Make.com    | Workflow automation (Zapier alternative)                     | 1 000 operations/month                         | Standard: $19.00    |
| Replit      | Quick code prototyping & hosting API scripts                 | Unlimited public repls                         | Hacker: $7.00       |
| Canva       | Visual design for newsletters & social assets                | Unlimited free features                        | Pro: $12.99         |
| [Grammarly](https://grammarly.com/)   | Writing assistant & plagiarism checker                       | Unlimited free usage                           | Premium: $12.00     |

**Estimated time to complete**: 3 hours (including account creation, DNS propagation, and test send verification).

---

## Procedure 1.1: Register Your Business Domain on Hostinger

1. **Open your preferred browser** (Chrome, Edge, or Firefox).  
2. **Navigate to** `https://www.hostinger.com/domains`.  
   - **Expected result:** The Hostinger Domains home page loads, displaying a search bar at the top center.  
   - **Do you see a search bar labeled “Search your domain name” with a green “Search” button?** If not, refresh the page or clear your cache and try again.  

3. **Enter your desired domain** (e.g., `yourbusinessname.com`) into the search field and **click the blue “Search” button**.  
4. **Review the search results**:  
   - If the domain is available, it will show “Available” in green.  
   - If it’s not available, Hostinger will list alternative suggestions.  
   - **Do you see “Available” highlighted in green next to your domain?** If not, choose a different domain or use one of the suggested alternatives.  

5. **Click the green “Add to cart” button** next to your domain.  
   - **Expected result:** A checkout sidebar appears on the right with the domain name and price.  
   - **Do you see the sidebar with the domain name and a price of $11.99 for the first year?** If the price differs, note the discounted rate for two or three years.  

6. **Click the “Proceed to checkout” button** in the sidebar.  
   - **Expected result:** You are redirected to the Hostinger checkout page.  

7. **Create a Hostinger account** (if you don’t already have one):  
   - **Enter your email** in the “Email” field.  
   - **Create a password** of at least 8 characters in the “Password” field.  
   - **Select “Create account”**.  
   - **Expected result:** You are logged in and the checkout page refreshes.  

8. **Choose a payment method**:  
   - **Select “Credit Card”**.  
   - **Enter card details**:  
     - Card number: `4111 1111 1111 1111` (test number for demonstration).  
     - Expiry: `12/30`.  
     - CVV: `123`.  
   - **Click “Pay Now”**.  
   - **Expected result:** A confirmation screen appears with a green “Order Complete” banner.  

9. **Verify the domain registration**:  
   - **Navigate to** `https://my.hostinger.com/domains`.  
   - **Do you see your newly registered domain listed under “My Domains”?** If not, wait 5 minutes for propagation or refresh the page.  

10. **Set up DNS records**:  
    - **Click the “Manage” button** next to your domain.  
    - **Select “DNS”** from the left‑hand menu.  
    - **Expected result:** The DNS management screen shows current records.  

11. **Add an A record for your website**:  
    - **Click “Add Record”**.  
    - **Record Type:** `A`.  
    - **Host:** `@`.  
    - **Value:** Enter the IP address of your hosting server (e.g., `198.51.100.1`).  
    - **TTL:** `3600`.  
    - **Click “Save”**.  
    - **Do you see “Record added successfully” in green?** If not, double‑check the IP address.  

12. **Add a CNAME record for “www”**:  
    - **Click “Add Record”** again.  
    - **Record Type:** `CNAME`.  
    - **Host:** `www`.  
    - **Value:** `yourbusinessname.com`.  
    - **TTL:** `3600`.  
    - **Click “Save”**.  
    - **Do you see a green confirmation?**  

13. **Confirm DNS propagation**:  
    - **Open a new tab** and go to `https://dnschecker.org`.  
    - **Enter your domain** in the “Domain” field.  
    - **Select “A”** from the record type

---

**Procedure 1.2** — Generation failed due to AI backend unavailability. Please retry later.

---

## Procedure 1.3: Create Core Business Accounts and Calendly  

1. **Open a web browser** and navigate to the Beehiiv sign‑up page:  
   `https://beehiiv.com/signup`  

2. In the Beehiiv landing page, **click the button labeled** **Start for free** (centered, blue).  

3. On the registration form, enter the following details exactly as shown:  
   - **Email**: `yourname@yourdomain.com`  
   - **Password**: `StrongPass!123` (8‑12 characters, include uppercase, lowercase, number, symbol)  
   - **Business name**: `YourBizName`  
   - **Country**: select `United States` from the drop‑down  

4. **Click** the **Create Account** button at the bottom of the form.  
   *Check‑in*: Do you see a confirmation banner that says “Account created – check your email to verify”?  
   If not, **refresh the page** and try again.  

5. Open your email client, locate the verification email from Beehiiv, and **click the “Verify Email” link**.  

6. After verification, you will be redirected automatically to the Beehiiv dashboard:  
   `https://app.beehiiv.com/dashboard`  

7. In the top right corner, click the **Settings** gear icon, then select **Billing** from the side menu.  

8. Click the **Add a Payment Method** button (blue

## Check-In: Module 1 Complete

- [ ] Register Your Business Domain on Hostinger completed and verified
- [ ] Set Up Email and Workspace in Notion completed and verified
- [ ] Create Core Business Accounts and Calendly completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 2: TECH STACK

## Overview
Module 2 is the cornerstone of your AI‑newsletter engine. It lays out the exact tech stack you must assemble, keys you must generate, and the step‑by‑step integration logic that turns raw subscriber data into automated, AI‑crafted emails. Skipping this module means you’ll be chasing data silos, writing fragile scripts, and losing the ability to scale your client services. By the end of this chapter you’ll have a fully wired system where Beehiiv’s powerful distribution platform, Mailchimp’s segmentation engine, and your chosen automation hub (Make.com or Zapier) communicate flawlessly via secure API keys. Each tool will be validated with test payloads, ensuring that your workflow can handle real‑world traffic without interruptions.

The module contains three procedures: 1) **API Key Generation & Storage** – secure your credentials in Notion and Secret Manager; 2) **Automation Hub Setup** – build a Make.com scenario that pulls content from ChatGPT, enriches it with Grammarly, and pushes it to Beehiiv; 3) **Verification & Monitoring** – run a test run, inspect JSON responses, and set up a Dashboard in Klaviyo to track deliverability. Every step is written to be repeatable, with exact URLs, button names, and expected UI states.

| Tool          | Purpose                                                   | Free Tier                        | Paid Tier (Monthly) |
|---------------|-----------------------------------------------------------|----------------------------------|---------------------|
| Beehiiv       | Newsletter distribution & subscriber management          | Unlimited emails, 2 k subscribers| $12 per 10 k subs   |
| Mailchimp     | Advanced segmentation & automation scripting             | 2 k contacts, 12 k sends         | $11 per 5 k contacts|
| Make.com      | Zap‑like workflow orchestration                           | 200 operations, 15 min runtime   | $19 per 3 k ops     |
| Zapier        | Quick integration between Beehiiv & Mailchimp             | 5 Zaps, 100 tasks per month      | $19 per 1 k tasks   |
| ChatGPT (OpenAI) | AI content generation                                   | 3 k tokens/month                | $20 per 1 M tokens  |
| Notion        | Credential vault & documentation                         | Unlimited pages, 1 k blocks      | $8 per user         |
| Grammarly     | Content polishing & grammar checks                       | 3 k characters/month            | $12 per month       |

**Estimated time to complete:** 35 minutes.

---

## Procedure 2.1: Connect ChatGPT API and Store Keys in Notion

1. **Open a new browser tab** and navigate to **https://platform.openai.com/account/api-keys**.  
2. Click the **bold** button **“Create new secret key”**.  
3. In the modal that appears, rename the key to **“ChatGPT‑Prod‑Key”** and click **“Create key”**.  
   *You will now see a 32‑character secret key displayed in a single line.*  
4. **Copy** the key to your clipboard.  
5. **Do you see the key string?** If not, refresh the page or re‑click **“Create new secret key”** until the key appears.  

**Error scenario:**  
- *If you see “You have reached your maximum number of keys”*, this means you’re on the free tier.  
  **Fix it** by deleting an unused key: hover over the key row, click **“Delete”**, then confirm.  

6. In a new tab, visit **https://www.notion.so** and sign in.  
7. Click the **bold** icon **“Settings & members”** in the left‑hand menu.  
8. Under **“Integrations”**, click **“Develop your own integrations”**.  
9. Press the **bold** button **“New integration”**.  
10. Fill in the form:  
    - **Name:** `BeehiivAI‑Keys`  
    - **Associated workspace:** select your workspace name.  
    - **Capabilities:** toggle **“Read content”** and **“Insert content”** to **ON**.  
    - **Redirect URLs:** leave blank (not needed for script).  
    Click **“Submit”**.  
11. You will receive a **“Internal Integration Token.”** Copy this token.  
12. **Do you see the token?** If not, ensure you scrolled to the bottom of the integration page.  

**Error scenario:**  
- *If you see “Access denied” when clicking “Submit”*, you likely do not have admin rights.  
  **Fix it** by requesting workspace admin to grant you “Integration admin” privileges.  

13. In the left‑hand sidebar, click **“New page”** and name it **“API Keys”**.  
14. Inside the new page, click **“+ Add a database”** → **“Table – Inline”**.  
15. Set the table columns as follows:  
    - **Name** (Title)  
    - **Key Type** (Select) – options: `ChatGPT`, `Notion`  
    - **API Key** (Text)  
    - **Last Updated** (Date)  
16. **Do you see the table with four columns?** If not, double‑click the column headers to add them.  

17. Open [**Replit**](https://replit.com/refer/egwuokwor) (https://replit.com).  
18. Click **“+ Create”** → **“New Repl”**.  
    - Language: **Python**  
    - Title: `NotionKeyStore`  
    - Click **“Create Repl”**.  
19. In the `main.py` file, paste the following script (replace `<YOUR_NOTION_INTEGRATION_TOKEN>` and `<YOUR_DATABASE_ID>` with your actual values):

```python
import os
import requests
from datetime import datetime

NOTION_TOKEN = "<YOUR_NOTION_INTEGRATION_TOKEN>"
DATABASE_ID = "<YOUR_DATABASE_ID>"

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def store_key(name, key_type, api_key):
    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Name": {"title": [{"text": {"content": name}}]},
            "Key Type": {"select": {"name": key_type}},
            "API Key": {"rich_text": [{"text": {"content": api_key}}]},
            "Last Updated": {"date": {"start": datetime.utcnow().isoformat()}}
        }
    }
    r = requests.post("https://api.notion.com/v1/pages", headers=headers, json=data)
    return r.json()

# Store ChatGPT key
store_key("ChatGPT Production", "ChatGPT", os.getenv("CHATGPT_KEY"))

# Store Notion key
store_key("Notion Integration", "Notion", os.getenv("NOTION_TOKEN"))
```

20. In the Replit sidebar, click **“Secrets” (icon with key)**.  
    - Add key `CHATGPT_KEY` → paste the ChatGPT key copied earlier.  
    - Add key `NOTION_TOKEN` → paste the Notion integration token.  
21. Click the **bold** button **“Run”**.  
    *You should see a JSON response that includes `"object":"page"` and a `"url"` field.*

---

## Procedure 2.2: Build Your First Make.com Automation Scenario  

1. **Open your web browser** and go to **https://www.make.com**.  
2. Click the **“Sign up”** button in the upper‑right corner.  
3. Fill in your email, password, and click **“Create account”**.  
4. **Do you see the Make.com dashboard with “Create new scenario” in the top‑left corner?**  
   *If not, refresh the page or log in again. The dashboard should display a green “Create new scenario” button.*  

5. Click the **“Create new scenario”** button.  
6. In the pop‑up, type **“Beehiiv”** into the search field.  
7. Select the [**Beehiiv**](https://beehiiv.com/) module from the list and click **“Add”**.  
8. Choose the trigger **“Webhook – New subscriber”** and click **“Add”**.  
9. **Do you see the “Webhook URL” field populated with a URL that starts with https://www.make.com/api/v1/...**  
   *If not, double‑click the Webhook module and verify the URL is displayed.*  

10. Copy the displayed **Webhook URL**.  
11. Open a new tab and navigate to **https://beehiiv.com**.  
12. Click **“Settings”** → **“API”**.  
13. Click **“Generate API Key”** and copy the 32‑character key.  
14. Return to the Make.com tab and in the Beehiiv Webhook module, paste the API key into the **“API Key”** field.  
15. Click **“Save”**.  
16. **Do you see the Beehiiv module status change to “Connected”?**  
   *If you see “Connection failed”, the API key is likely incorrect. Regenerate the key in Beehiiv and retry.*

17. Click the **“+”** icon below the Beehiiv trigger to add a new action.  
18. Search for **“Mailchimp”** and select the **Mailchimp** module.  
19. Choose the action **“Add / Update Subscriber”** and click **“Add”**.  
20. Click **“Add connection”**.  
21. In the Mailchimp login popup, enter your Mailchimp email and password.  
22. Click **“Authorize”** to grant Make.com permission.  
23. In the Mailchimp action module, set the **“Audience ID”** to the ID of the list you want to sync.  
    - To find the Audience ID:  
      a. In Mailchimp, go to **Audience** → **All contacts** → **Manage Audience** → **Audience settings**.  
      b. Copy the **Audience ID** from the URL (it ends with `/audiences/<AUDIENCE_ID>`).  
24. Map the fields:  
    - **Email address** → **Email Address

---

## Procedure 2.3: Configure Vapi Voice Agent and ElevenLabs TTS

1. **Open a web browser** and navigate to the Vapi signup page:  
   **https://vapi.io/signup**.  
   *Expected output:* The Vapi registration form with fields for “Full Name,” “Email,” “Password,” and a **Sign Up** button.

2. **Fill in the registration form** exactly as follows:  
   - Full Name: `John Doe`  
   - Email: `john.doe@example.com`  
   - Password: `StrongPass!23` (at least 12 characters, mixed case, number, symbol).  
   Click the **Sign Up** button.  

3. **Verify your email**: Open your inbox, locate the email from Vapi (`verify@vapi.io`), click the **Verify Email** link.  
   *Expected output:* Browser redirects to `https://vapi.io/dashboard` with a green banner “Account verified.”

4. **Navigate to the API section**: In the top navigation bar, click on **API**.  
   *Expected output:* API overview page showing “API Key” placeholder and a **Generate Key** button.  

5. **Generate an API key**: Click **Generate Key**. A modal appears with the newly created key.  
   - Copy the key to clipboard.  
   - Store it in a secure location (e.g., `~/.vapi_key`).  
   *Expected output:* Modal closes and the key is displayed in a read‑only field.  

6. **Open a new terminal window** and run:  
   ```bash
   echo "VAPI_KEY=$(cat ~/.vapi_key)" > ~/.env
   ```  
   *Expected output:* File `~/.env` created containing `VAPI_KEY=xxxxxxxxxx`.  

7. **Create a Vapi Voice Agent**: In the dashboard, click **Voice** → **Create Agent**.  
   *Expected output:* Agent creation form with fields “Agent Name,” “Description,” “Language,” and a **Create** button.  

8. **Fill in the agent details**:  
   - Agent Name: `NewsletterSpeaker`  
   - Description: `Voice agent for AI newsletter narration.`  
   - Language: `English (US)`  
   Click **Create**.  
   *Expected output:* Agent appears in the list with status “Active” and a **Manage** button.  

9. **Click on the newly created agent’s **Manage** button**.  
   *Expected output:* Agent settings page showing “API Endpoint” (`https://api.vapi.io/v1/agents/NewsletterSpeaker`) and **Test Call** button.  

10. **Test the agent**: Click **Test Call**. A small dialog appears requesting a text payload.  
    - Enter `"Hello, this is your AI newsletter narrator."`  
    - Click **Send**.  
    *Expected output:* Audio preview plays and the console logs a JSON response:  
    ```json
    {
      "status":"success",
      "audio_url":"https://cdn.vapi.io/agents/NewsletterSpeaker/2026/10/31/hello.mp3"
    }
    ```  

**Do you see the audio preview and JSON response?**  
If not, ensure your internet connection is active and that the VAPI_KEY environment variable is correctly loaded (`source ~/.env`).  

11. **Set up ElevenLabs TTS**: Open a new tab and go to **https://elevenlabs.io**.  
    *Expected output:* ElevenLabs homepage with a **Login** button.  

12. **Login**: Click **Login** → enter the same credentials used for Vapi.  
    *Expected output:* Redirect to `https://elevenlabs.io/dashboard`.  

13. **Navigate to the “Text to Speech” section**: Click the **TTS** tab in the left sidebar.  
    *Expected output:* TTS interface with a textarea for input text, a drop‑down for voice selection, and a **Generate** button.  

14. **Select a voice**: In the “Voice” drop‑down, choose `Mark` (male, American English).  
    *Expected output:* Voice details appear below the drop‑down.  

15. **Enter sample text**: In the textarea, type `"Welcome to your weekly AI insights newsletter."`  
    Click **Generate**.  
    *Expected output:* The generated audio plays in the player, and a JSON response appears:

    ```json
    {
      "audio_url":"https://api.elevenlabs.io/v1/audio/voice/mark/2026/10/31/weekly-insights.mp3",
      "id":"ai-12345"
    }
    ```  

16. **Copy the audio

## Check-In: Module 2 Complete

- [ ] Connect ChatGPT API and Store Keys in Notion completed and verified
- [ ] Build Your First Make.com Automation Scenario completed and verified
- [ ] Configure Vapi Voice Agent and ElevenLabs TTS completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 3: FRAMEWORK

## Overview  
In this module you will master the core operating system that turns raw AI content into a polished, revenue‑driven newsletter service. We start by mapping the entire delivery pipeline—from the first client intake to the final automated dispatch—so every touchpoint is repeatable, auditable, and scalable. By rigorously defining your service delivery framework, you eliminate guesswork, set clear expectations, and create a defensible pricing model that clients can trust. Skipping this step leaves you with ad‑hoc processes, inconsistent quality, and a fragile business that can’t handle growth or scale to multiple clients.  

Next, we walk through the client onboarding flow: how to capture client goals, extract brand assets, and translate them into a custom AI‑powered editorial plan. We embed quality controls at every stage—content approval, style checks, and deliverability testing—to ensure 99.5 % inbox placement and zero spam complaints. This module equips you to launch a turnkey newsletter service that can be replicated across niches, client types, and content volumes.  

The end result is a documented, repeatable operating system that you can hand off to an assistant or use to onboard new clients in under an hour. By the end of this module you’ll have a live, end‑to‑end workflow that you can plug into any client’s brand voice and watch it generate recurring revenue.

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| Beehiiv | Newsletter platform & automation | 10 k subscriber limit, basic templates | $15 / month (unlimited) |
| Mailchimp | Bulk email distribution & segmentation | 2 k contacts, 12 k emails/month | $10 / month (advanced) |
| Zapier | Connect Beehiiv, Mailchimp, and other apps | 5 Zaps, 100 tasks/month | $19.99 / month (Starter) |
| Canva | Brand‑consistent graphics | Unlimited templates, 5 GB storage | $12.99 / month |
| ChatGPT | AI content creation | 3 k token free, 3 month trial | $20 / month (ChatGPT‑4) |
| Replit | Collaborative coding for custom scripts | Unlimited public repos | $7 / month (Hacker) |

**Estimated time to complete:** 4 – 6 hours (including research, documentation, and initial setup).

---

## Procedure 3.1: Design Your Service Delivery Framework in Notion

1. **Open your browser and navigate to `https://www.notion.so/`.**  
   - Click the **Sign In** button in the top‑right corner.  
   - Enter your email and password, then click **Continue**.  
   - *Do you see the Notion dashboard?* If not, check that the URL is correct and that cookies are enabled.

2. **Create a new workspace for your newsletter service.**  
   - In the sidebar, click **+ New Workspace**.  
   - Name it **“AI Newsletter Delivery”** and click **Create Workspace**.  
   - The new workspace will open with a default page titled **“Untitled”**.

3. **Rename the default page.**  
   - Hover over the page title, click the three dots (**⋯**), then select **Rename Page**.  
   - Type **“Service Delivery Framework”** and hit **Enter**.  
   - The page now serves as the central hub for all operational assets.

4. **Add a database for client onboarding.**  
   - On the blank page, type **“/table”** and select **Table – Inline**.  
   - Click **+ Add a new property**.  
     - Property 1: **Client Name** (Type: **Title**).  
     - Property 2: **Service Type** (Type: **Select**; add options **Beehiiv Automation**, **Mailchimp Automation**, **Both**).  
     - Property 3: **Start Date** (Type: **Date**).  
     - Property 4: **Delivery Status** (Type: **Select**; options **Pending**, **In‑Progress**, **Completed**).  
     - Property 5: **Notes** (Type: **Rich Text**).  
   - Click **Close**.  
   - *Do you see the table with five columns?* If the properties are missing, revisit step 4 and ensure each property is added correctly.

5. **Create a template button for new client entries.**  
   - Type **“/button”** and select **Button – Inline**.  
   - Rename the button to **“Add New Client”**.  
   - In the **Action** field, choose **“New Page”**.  
   - In **Page Name**, type **“Client – [Client Name]”**.  
   - In **Template**, click **+ Add a block** → **Table – Inline** → **Use existing database** → select your **Client Onboarding** table.  
   - Click **Save**.  
   - *Do you see the button labeled “Add New Client”?* If not, ensure you are using the inline button block.

6. **Embed the Beehiiv dashboard for quick reference.**  
   - Go to `https://beehiiv.com/dashboard`.  
   - Copy the page URL.  
   - Back in Notion, type **“/embed”** → **Embed – Inline**.  
   - Paste the Beehiiv URL and click **Embed**.  
   - The Beehiiv dashboard will appear as a resizable frame.  
   - *Do you see the Beehiiv embed?* If the embed says “Cannot load page”, check that the Beehiiv URL is correct and that the dashboard is accessible.

7. **Create a second database for Zapier integration logs.**  
   - Type **“/table”** → **Table – Inline**.  
   - Rename the table to **“Zapier Logs”**.  
   - Add properties: **Zap Name** (Title), **Trigger** (Select), **Action** (Select), **Status** (Select: **Success**, **Failure**), **Timestamp** (Date).  
   - *Do you see the Zapier Logs table?* If not, confirm that you renamed it correctly.

8. **Set up a Zapier account (free tier).**  
   -

---

## Procedure 3.2: Build the Client Onboarding Automation Pipeline

**Objective:** Automate the entire client onboarding journey—from initial contact to first newsletter delivery—using Beehiiv for newsletter publishing and Mailchimp for list management. The pipeline will be powered by Make.com (formerly Integromat) for workflow automation, Calendly for scheduling discovery calls, Loom for onboarding video, Canva for welcome email design, and ChatGPT for copy generation.

> **NOTE:** All URLs, button labels, and field names are current as of 31‑Oct‑2026. If any UI changes, refer to the tool’s help center.

---

### 1. Create a New Client on Beehiiv
1. Open your browser and go to **https://app.beehiiv.com/signup**.
2. Click the **bold “Sign up for free”** button.
3. On the registration form:
   - **Email**: `client@example.com`
   - **Password**: `[StrongPassword]`
   - **Confirm Password**: `[StrongPassword]`
4. Click **bold “Create account”**.
5. Verify email by clicking the link in the confirmation email.
6. **Do you see “Welcome to Beehiiv!” on the dashboard?**  
   *If not, check spam folder or resend verification.*

> **Expected Output:** Beehiiv dashboard with “Create new newsletter” button visible.

---

### 2. Set Up a New Newsletter Project
1. Click **bold “Create new newsletter”** on the Beehiiv dashboard.
2. Enter **Newsletter Name**: `ClientX Newsletter`.
3. Choose **Domain**: `clientx.beehiiv.io` (Beehiiv auto‑domains are free for up to 10k subscribers).
4. Click **bold “Create”**.
5. In the new project, click **bold “Add new template”**.
6. Select **Starter Template** (“Welcome Series”).
7. Click **bold “Edit”** to open the editor.
8. In the editor, replace the placeholder text with “Welcome to ClientX’s AI‑Powered Newsletter!”.
9. Click **bold “Save”**.
10. **Do you see the preview of the new template?**  
    *If not, refresh the page or clear browser cache.*

> **Error Scenario:**  
> If you see **“Error 500 – Server Unavailable”**, this means the Beehiiv servers are temporarily down.  
> **Fix**: Wait 5 min and reload the page. If the error persists, contact Beehiiv support at support@beehiiv.com.

---

### 3. Create a Mailchimp Audience
1. Open **https://admin.mailchimp.com** and log in.
2. Click **bold “Audience”** from the left menu.
3. Click **bold “Create Audience”**.
4. Fill in:
   - **Audience Name**: `ClientX Subscribers`
   - **Default From Name**: `ClientX Team`
   - **Default From Email**: `newsletter@clientx.com`
5. Click **bold “Save Audience”**.
6. Under the newly created audience, click **bold “Settings” > “Audience name and defaults”**.
7. Set **Signup form URL** to `https://clientx.com/subscribe`.
8. **Do you see the audience details page?**  
   *If not, ensure you are on the correct audience tab.*

> **Expected Output:** Mailchimp audience “ClientX Subscribers” appears in the list with the signup URL displayed.

---

### 4. Connect Beehiiv and Mailchimp via Make.com
1. Open **https://www.make.com** and log in (free tier: 500 operations/month).
2. Click **bold “Create a new scenario”**.
3. In the search bar, type **“Beehiiv”**. Click the **bold “Beehiiv”** module.
4. Select trigger **“New Subscriber”**.
5. Click **bold “Add”** to create a new connection.
6. In the Beehiiv connection dialog:
   - **API Key**

## Check-In: Module 3 Complete

- [ ] Design Your Service Delivery Framework in Notion completed and verified
- [ ] Build the Client Onboarding Automation Pipeline completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 4: FIRST BUILD

## Overview  

In this module you will **design, build, and automate a full AI‑driven newsletter workflow** that you can hand off to a client in under a day. We start with raw client data, feed it into our AI content engine, format it with Beehiiv’s advanced template system, and then orchestrate a seamless delivery through Mailchimp’s subscriber management and analytics. The end result is a polished, auto‑publishing newsletter that feels handcrafted yet is powered entirely by AI—perfect for solo entrepreneurs looking to sell a repeatable, high‑margin service.

Skipping this module leaves you without a tangible deliverable to showcase to prospects. You’ll also miss the critical integration points between Beehiiv and Mailchimp that unlock automatic subscriber syncing, segmentation, and A/B testing. Without these, you’ll be stuck manually moving emails, incurring higher overhead and reduced scalability. Mastery of this workflow creates a repeatable revenue stream: you can charge a one‑time setup fee plus a monthly maintenance retainer, while keeping your time spend minimal.

The following table lists every tool you’ll need, what each does, and the exact pricing tiers you’ll be working with. All tools are chosen for their free‑tier capability to get you started and a clear, low‑cost paid tier that scales with your client count.

| Tool          | Purpose                                                    | Free Tier (Cap)                                 | Paid Tier (Starter)                                   |
|---------------|-------------------------------------------------------------|-------------------------------------------------|--------------------------------------------------------|
| Beehiiv       | AI‑driven newsletter creation & hosting                     | 1,000 subscribers, 30 GB storage               | 30 % discount on paid plan (starts at $19/mo)          |
| Mailchimp     | Subscriber management & analytics                           | 2,000 contacts, 10 000 sends/mo                 | 12 % discount on paid plan (starts at $9.99/mo)        |
| Make.com      | Workflow automation between Beehiiv & Mailchimp             | 500 operations/month, 1 GB storage              | Unlimited operations, 5 GB storage ($9/mo)             |
| Zapier        | Alternate or backup automation with 100 tasks/month        | 100 tasks/month, 5 Zaps                         | Unlimited tasks, 50 Zaps ($19/mo)                     |
| Notion        | Project board & client data repository                      | Unlimited pages, 5 MB file uploads              | Unlimited file uploads ($8/mo)                        |
| Canva         | Email template design & branding assets                    | 1 GB storage, 60 templates                     | Unlimited storage, 100 templates ($12/mo)             |
| Grammarly     | Proofreading & tone checking                               | 3 GB storage, basic grammar checks             | Premium checks, plagiarism ($12/mo)                    |
| Replit        | Quick script hosting for custom AI calls                    | 500 MB storage, 1 Gbps bandwidth               | Unlimited storage, 2 Gbps ($7/mo)                     |

**Estimated time to complete:** 5 hours (incl. data prep, AI prompts, template design, integration setup, and testing).

---

## Procedure 4.1: BUILD THE CORE AI PRODUCT IN REPLIT

1. Open a web browser and navigate to **https://replit.com/**.  
2. Click the **Login** button in the upper‑right corner and sign in with your GitHub account (or create a new account if you don’t have one).  
3. Once logged in, click the **+ Create** button (top‑left).  
4. In the **Create a Repl** modal,  
   - Choose **Python 3** from the “Language” dropdown.  
   - Name the repl **ai‑newsletter‑bot**.  
   - Click **Create Repl**.  
   **Check‑in:** Do you see a new tab with the name **ai‑newsletter‑bot** and a code editor? If not, refresh the page and repeat steps 3‑4.  

5. In the `main.py` file that opened, paste the following starter code:

   ```python
   import requests
   import json

   # Beehiiv API base
   BEEHIV_API = "https://api.beehiiv.com/v1"
   API_KEY = "YOUR_BEEHIV_API_KEY"
   ```

6. Replace `"YOUR_BEEHIV_API_KEY"` with your actual Beehiiv API key.  
   - To get this key, log in to your Beehiiv account at **https://app.beehiiv.com/**, go to **Settings → API Keys**, click **Create API Key**, and copy the key.  
   - In Replit, click the **Secrets** (⚙️) icon in the left sidebar, then click **Add a secret**.  
   - Name the secret **BEEHIV_API_KEY** and paste the key.  
   - In `main.py`, change `API_KEY = "YOUR_BEEHIV_API_KEY"` to `API_KEY = os.getenv("BEEHIV_API_KEY")`.  

7. Install the `requests` library in the Replit console by running:

   ```
   pip install requests
   ```

   After installation, the console should display:

   ```
   Successfully installed requests
   ```

8. Create a new file called **newsletter_generator.py** and add the following code to generate AI‑driven content using ChatGPT:

   ```python
   from openai import OpenAI

   def generate_article(topic, length="medium"):
       client = OpenAI(api_key="YOUR_OPENAI_API_KEY")
       prompt = f"Write a {length} newsletter article about {topic}."
       response = client.chat.completions.create(
           model="gpt-4o-mini",
           messages=[{"role":"user","content":prompt}]
       )
       return response.choices[0].message.content
   ```

   **Check‑in:** Do you see the `newsletter_generator.py` file with the above code? If not, create the file via **Add file** in the sidebar and paste the code.  

9. Add your OpenAI API key as a secret in Replit (same method as step 6). Name the secret **OPENAI_API_KEY**.  
   Then modify `main.py` to import the generator:

   ```python
   from newsletter_generator import generate_article
   ```

10. Write the function to create a subscriber list in Beehiiv:

    ```python
    def create_subscriber(email):
        url = f"{BEEHIV_API}/subscribers"
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        payload = {"email": email}
        resp = requests.post(url, headers=headers, json=payload)
        return resp.json()
    ```

11. Write the function to send a newsletter:

    ```python
    def send_newsletter(subject, content, subscriber_id):
        url = f"{BEEHIV_API}/newsletters"
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        payload = {
            "subject": subject,
            "html_body": content,
            "subscriber_ids": [subscriber_id]
        }
        resp = requests.post(url, headers=headers, json=payload)
        return resp.json()
    ```

12. In the **main.py** `if __name__ == "__main__":` block, orchestrate a simple workflow:

    ```python
    if __name__ == "__main__":
        email = "test@example.com"
        topic = "AI in small business revenue"
        subscriber = create_subscriber(email)
        article = generate_article(topic, "short")
        newsletter = send_newsletter(f"AI Insights: {topic}", article, subscriber["id"])
        print(newsletter)
    ```

13. **Run** the repl by clicking the green **Run** button.  
    You should see JSON output similar to:

    ```
    {
        "id": 123456,
        "status": "queued",
        "subject": "AI Insights: AI in small business revenue"
    }
    ```

    **Check‑in:** Do you see a JSON response with a `status` field? If not, verify that your API keys are correctly stored in Secrets and that the Beehiiv API endpoint is reachable.  

14. **Error Scenario:** If you see the following error in the console:

    ```
    401 Unauthorized

---

## Procedure 4.2: Create the Data Processing Pipeline with Make.com

1. **Open your browser and go to** `https://www.make.com/en`.  
   **Click the** **“Sign up for free”**** button** (top‑right).  
   - *If you already have an account, click “Log in” instead.*

2. **Fill in the registration form**:  
   - *Email*: your work email  
   - *Password*: `StrongPass!1234`  
   - *Company name*: “My Newsletter Service”  
   Click **“Create account”**.  
   **Expected result**: a green success banner “Account created” and you’re taken to the dashboard.

3. **Verify your email** – open the inbox, click the link from Make.com.  
   **Do you see** the Make.com dashboard?  
   *If not, check your spam folder or resend the verification email.*

4. **Create a new scenario**:  
   - On the dashboard, click **“Create a new scenario”** (large blue button).  
   - In the modal, type **“Google Sheets”** in the search bar, then click the **Google Sheets** icon.  
   - **Click “Continue”**.  
   **Expected result**: the scenario canvas with a “Google Sheets” module added.

5. **Authorize Google Sheets**:  
   - Click the **Google Sheets** module, then **“Add a connection”**.  
   - In the popup, click **“Authorize”** and sign in with your Google account.  
   - Grant Make.com permission to “View and manage your spreadsheets”.  
   **Do you see** a green checkmark next to the Google Sheets module?  
   *If not, retry the authorization or check that you’re logged into the correct Google account.*

6. **Configure the trigger**:  
   - Click the Google Sheets module, then **“Choose an action event”** → **“Watch rows”**.  
   - **Spreadsheet ID**: paste the ID from the URL of your source spreadsheet (`https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit`).  
   - **Worksheet**: `Lead Data`.  
   - **Start at row**: `2`.  
   - **Check every**: `1 minute`.  
   Click **“Save”**.  
   **Expected result**: the module shows “Watching rows” and a timestamp appears.

7. **Add a Filter**:  
   - Drag a **“Filter”** module onto the canvas (search “Filter” in the left panel).  
   - Connect it to the Google Sheets module.  
   - Set the condition:  
     - **Field**: `Status` (from the row data)  
     - **Condition**: `equals`  
     - **Value**: `New`  
   - Click **“Save”**.  
   **Do you see** the filter icon with a green check?  
   *If not, make sure the field name matches exactly the column header.*

8. **Store processed rows** (optional but recommended):  
   - Add **“Data Store > Create Record”**.  
   - Connect to the Filter.  
   - Create a new store named **“Processed Leads”** (free tier supports up to 1000 records).  
   - Map fields: `Email`, `Name`, `Timestamp` → corresponding columns.  
   - Click **“Save”**.  
   **Expected output**: a new record appears in the Data Store interface after the first test run.

9. **Compose the email body**:  
   - Add **“Text > Text aggregate”**.  
   - Connect to the Filter.  
   - In the **“Text”** field, type:  
     ```
     Hello {{Name}},
     
     Thank you for signing up! Here’s the first AI newsletter you requested.
     
     Best,
     Your AI Newsletter Team
     ```
   - Use the **“Insert variable”

---

## Procedure 4.3: DEPLOY AND TEST THE COMPLETE AI NEWSLETTER SYSTEM

1. **Open your web browser** and navigate to <https://beehiiv.com>.  
2. Click the **“Log In”** button in the top‑right corner.  
3. In the login form, enter your Beehiiv **email** and **password** (use the credentials you created in Module 1). Click **“Sign In”**.  
4. Do you see the **Dashboard** with the sidebar titled “Campaigns”?  
   - If not, verify you are on <https://app.beehiiv.com/dashboard>.  
   - If a “You have no campaigns” message appears, proceed to Step 5.  

5. Click the **“Create New Campaign”** button (upper‑right, blue).  
6. In the **Campaign Settings** modal, set:  
   - **Campaign name**: `AI Newsletter Launch – [DATE]` (replace `[DATE]` with the current date).  
   - **Subject line**: `Your Daily AI Digest – Powered by Beehiiv`  
   - **From name**: `Menshly AI`  
   - **From email**: `ai@menshly.com`  
   Click **“Save & Continue”**.  
7. On the **Content Editor** page, click **“Import from URL”**. Enter the URL `https://your-repo.com/newsletter-template.html` (replace with the actual hosted template). Click **“Import”**.  
8. The editor should load the HTML content. Do you see the preview pane with the full article?  
   - If the preview is blank, ensure the URL is correct and that the server allows CORS.  

9. Add a **dynamic AI snippet**:  
   - In the editor toolbar, click **“Insert Block”** → **“Custom Code”**.  
   - Paste the following JavaScript (replace `YOUR_API_KEY`):  
     ```js
     fetch('https://api.openai.com/v1/completions', {
       method: 'POST',
       headers: { 'Authorization': 'Bearer YOUR_API_KEY', 'Content-Type': 'application/json' },
       body: JSON.stringify({ model: 'gpt-4o-mini', prompt: 'Summarize the following article in 3 sentences:', max_tokens: 60 })
     }).then(r => r.json()).then(d => document.getElementById('ai-summary').innerText = d.choices[0].text);
     ```  
   - Click **“Save”**.  
   - In the HTML, add `<div id="ai-summary"></div>` where you want the summary to appear.  
10. Save the campaign as **Draft** by clicking the **“Save Draft”** button.  
11. Do you see the confirmation banner “Draft saved”?  
    - If you see an error such as `403 Forbidden`, double‑check your OpenAI API key and the API endpoint.  

12. **Set up Mailchimp integration**:  
    - In Beehiiv, go to the **“Integrations”** tab in the left sidebar.  
    - Click **“Add Integration”** → **Mailchimp**.  
    - In the pop‑up, enter your **Mailchimp API key** (found at <https://admin.mailchimp.com/account/api>).  
    - Click **“Authorize”**.  
13. Map the **Beehiiv subscriber list** to the **Mailchimp audience**:  
    - Choose the Beehiiv list `Menshly Subscribers`.  
    - Select the Mailchimp audience `Menshly AI Subscribers`.  
    - Click **“Save Mapping”**.  
14. Verify the integration by clicking **“Test Sync”**.  
    - Do you see a message “Sync successful – 0 subscribers synced”?  
    - If you see `401 Unauthorized`, ensure the API key is still valid.  

15. **Create a Make.com scenario** (automation platform) to push content to Mailchimp:  
    - Visit <https://www.make.com> and log in.  
    - Click **“Create a new scenario”** (top‑right).  
    - Add the **“HTTP”** module → **“Make a request”**.  
    - Set **Method**: `GET`; **URL**: `https://api.beehiiv.com/v1/campaigns/[CAMPAIGN_ID]/content` (replace `[CAMPAIGN_ID]` with the ID from Step 5).  
    - Add header `Authorization: Bearer YOUR_BEEHIIV_API_KEY`.  
    - Click **“Add another module”** → **“Mailchimp”** → **“Add a subscriber”**.  
    - Map the JSON fields from Beehiiv (`email`, `first_name`) to Mailchimp’s subscriber fields.  
    - Click **“Run once”**.  
16. Observe the scenario run log: it should show `200 OK` for Beehiiv request and `201 Created` for Mailchimp.  
    - If you see `429 Too Many Requests`, reduce the polling frequency to once per hour.  

17. **Schedule the campaign**:  
    - In Beehiiv, open your campaign.  
    - Click **“Schedule”** → **“Pick a time”** → select **“Every Day at 08:00 AM UTC”**.  
    - Confirm by clicking **“Schedule Campaign”**.  
18. Do you see the status change to **Scheduled**?  
    - If the status remains Draft, ensure the time zone matches your local settings.  

19. **Test the full flow**:  
    - Use a temporary email address (e.g., `test+ai@domain.com`).  
    - In Beehiiv, click **“Add Subscriber”** → enter the test email.  
    - Click **“Subscribe”**.  
    - Check the Mailchimp audience; the test email

## Check-In: Module 4 Complete

- [ ] BUILD THE CORE AI PRODUCT IN REPLIT completed and verified
- [ ] Create the Data Processing Pipeline with Make.com completed and verified
- [ ] DEPLOY AND TEST THE COMPLETE AI NEWSLETTER SYSTEM completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 5: CLIENT ACQUISITION

## Overview  

Solo entrepreneurs who want to monetize AI‑powered newsletter services cannot rely on talent alone; they must first *attract* paying clients. Module 5 teaches you how to design, build, and automate a lead‑generation pipeline that turns curious prospects into paying subscribers for your AI newsletter service. By mastering outreach systems, landing pages, and automated email workflows, you create a self‑sustaining funnel that requires minimal manual effort after the initial setup.

Why does this matter? The newsletter space is now saturated with AI‑driven offerings, and the most successful operators run a seamless acquisition loop: a compelling landing page captures intent, a drip campaign nurtures leads, and a CRM system tracks conversions. Skipping this module means you’ll be stuck in a manual, time‑consuming outreach loop that wastes bandwidth and drastically limits revenue growth. Without a proven pipeline, you risk losing potential clients to competitors who deliver instant, AI‑enhanced newsletters without friction.

Below is the toolbox you’ll need to execute this module. All tools listed are fully compatible with Beehiiv and Mailchimp, and their pricing tiers are current as of October 2026.  

| Tool          | Purpose                                                    | Free Tier (limitations)                                         | Paid Tier (starting price) |
|---------------|-------------------------------------------------------------|------------------------------------------------------------------|----------------------------|
| Beehiiv       | AI newsletter hosting, content moderation, analytics        | Unlimited subscribers, no custom domain, limited analytics       | Pro: $15 / month (Custom domain, advanced analytics) |
| Mailchimp     | Email automation, segmentation, performance tracking        | 2,000 contacts, 10 k sends/month, basic templates                | Essentials: $11 / month (Premium templates, A/B testing) |
| Zapier        | Automation between Beehiiv, Mailchimp, CRM, calendar tools  | 100 tasks/month, single-step Zaps                                 | Starter: $19.99 / month (Multi-step Zaps, 2,000 tasks) |
| Notion        | Lead database, process documentation, task tracking         | Unlimited pages, basic blocks                                   | Team Starter: $8 / month (Advanced permissions, API) |
| Replit        | Quick code snippets, API integration experiments           | Unlimited public projects, 500 MB storage, 1 GB/month runtime    | Hacker: $7 / month (Private repls, 2 GB storage, 4 GB runtime) |
| Calendly      | Automated scheduling for discovery calls                   | 1 calendar, 1 meeting type per user, basic notifications         | Pro: $12 / month (Multiple calendars, advanced integrations) |

**Estimated time to complete Module 5**: 2 – 3 hours of focused work, including setting up each tool, creating the landing page and drip campaign, and testing the end‑to‑end flow.

---

**Procedure 5.1** — Generation failed due to AI backend unavailability. Please retry later.

---

## Procedure 5.2: Set Up Lead Generation with Apollo.io

1. **Open a web browser** (Chrome, Edge, or Safari).  
   Navigate to the Apollo.io homepage:  
   `https://www.apollo.io/`

2. Click the **“Get Started Free”** button (top‑right corner).  
   You will be redirected to the sign‑up form.  
   **Fill in**:
   - **Email**: `yourname@yourdomain.com`
   - **Password**: `StrongPassword123!` (must be at least 12 characters, include a number and a symbol)
   - **Company Name**: `YourBusinessName`
   - **Job Title**: `Founder`

3. Click the **“Create Account”** button.  
   Apollo will send a verification email to the address you entered.

4. **Open the verification email** in Gmail (or your default mail client), click the **“Verify Email”** link.  
   You will be taken to the Apollo dashboard.

5. **Do you see the Apollo dashboard with the “Create New Lead List” button?**  
   If not, refresh the page or log out and log back in.  

   **Expected output**: A landing page with a sidebar menu (`Dashboard`, `Teams`, `Reports`, `Integrations`) and a central panel showing a button labeled **“Create New Lead List”**.

6. Click the **“Create New Lead List”** button.  
   The “New Lead List” modal will appear.

7. **Enter**:
   - **Lead List Name**: `AI Newsletter Prospects`
   - [**Description**](https://www.descript.com/): `Prospects for Beehiiv and Mailchimp newsletter automation services`
   - Leave the **Tags** field empty for now.

8. Click the **“Create”** button at the bottom of the modal.  
   Apollo will confirm with a toast notification: *“Lead List ‘AI Newsletter Prospects’ created.”*

9. **Do you see your new lead list in the sidebar under “Lead Lists”?**  
   If not, click the **“Refresh”** icon next to “Lead Lists”.  

   **Expected output**: `AI Newsletter Prospects` appears with a small clock icon indicating it’s empty.

10. In the top‑right corner, click your **profile avatar** → **“Settings”** → **“Integrations”**.  
    You will be on the Integrations page.

11. Under **Email Integrations**, click **“Connect Gmail”**.  
    A Google Auth window will appear.

12. **Sign in** with the Gmail account you want to use for outreach.  
    Grant the requested permissions (Send email, Manage email, etc.).  
    Click **“Allow”**.

13. Return to Apollo. You should see a green banner: *“Gmail account connected.”*  
    Confirm by clicking the **“Test Connection”** button (bold on the banner).  
    A toast appears: *“Gmail connection verified.”*

14. **Do you see the green Gmail banner?**  
    If not, navigate back to the Integrations page and repeat steps 11‑13.

15. **Create a custom search query**:  
    a. Click **“New Search”** in the top‑left corner.  
    b. In the **Search Builder**, set:
       - **Industry**: `Technology`
       - **Job Title**: `Founder OR CEO OR Owner`
       - **Company Size**: `1‑10` or `11‑50`
       - **Location**: `United States`
    c. Click **“Preview”** (bold).  
    d. Review the preview list; ensure at least 30 prospects appear.

16. **Do you see 30+ prospects in the preview list?**  
    If the list is empty, adjust filters or remove the location filter.  

    **Expected output**: A table with columns `Name`, `Title`, `Company`, `Email`, `Phone`.  

17. Click **“Start Search”** (bold).  
    Apollo will begin scraping.  
    A progress bar will show **“Searching… 0%”** → **“Searching… 100%”**.

18. Once complete, click **“Export”** → **“CSV”**.  
    The file `AI_Newsletter_Prospects.csv` will download to your default folder.

19. **Do you have the CSV file in your downloads folder?**  
    If not

---

## Procedure 5.3: Create Automated Email Nurture Sequence in Klaviyo

**Objective** – Build a 5‑email nurture flow that pulls subscribers from Beehiiv, enriches them with AI‑generated copy (ChatGPT), inserts branded graphics (Canva), and delivers through Klaviyo. This flow will run automatically, sending each email at a 3‑day interval.

---

### 1. Create / Log Into Klaviyo  
1.1 Open your browser and go to **https://www.klaviyo.com/**.  
1.2 Click **SIGN UP** (top‑right).  
1.3 Fill the form:  
- **Email**: your business email  
- **Password**: create a 12‑character mix of letters, numbers, & symbols  
- **Company name**: “Menshly Global”  
1.4 Click **CREATE ACCOUNT**.  
1.5 Klaviyo will send a verification email. Open it, click **VERIFY**.  
1.6 After verification, you’ll land on the **Dashboard** – a white page with a left sidebar (“Dashboard, Lists, Segments, Flows, etc.”).

> **Do you see the Klaviyo Dashboard?**  
> *If not, check that you used the correct email and that your inbox hasn’t moved the verification to spam. Resend the code if needed.*

---

### 2. Set Up Beehiiv Sign‑up Form and Zapier Integration  
2.1 In a new tab, go to **https://www.beehiiv.com/**.  
2.2 Click **LOG IN** → enter your Beehiiv credentials.  
2.3 From the Beehiiv sidebar, click **SETTINGS > SUBSCRIBER FORMS**.  
2.4 Click **+ NEW FORM**.  
2.5 Name the form **“Klaviyo Nurture Sign‑up”**.  
2.6 Drag the **Email** field to the form.  
2.7 Under **Form Settings → Integrations**, click **+ ADD INTEGRATION** → **Zapier**.  
2.8 Copy the **Zapier Webhook URL** shown.  
2.9 In a new tab, open **https://zapier.com**.  
2.10 Click **LOG IN** → use the same email/password as Klaviyo.  
2.11 Click **MAKE A ZAP**.  
2.12 Choose **Webhooks by Zapier** → **Catch Hook** as the trigger.  
2.13 Paste the Beehiiv Webhook URL from step 2.8.  
2.14 Click **TEST AND CONTINUE** – Zapier should receive a test subscriber payload.  
2.15 Click **CONTINUE** → choose **Klaviyo** as the action app.  
2.16 Select **Create/Update Subscriber**.  
2.17 Map Beehiiv fields:  
- **Email** → **Email**  
- **Full name** → **First Name** (optional)  
2.18 Click **TEST ACTION** → confirm subscriber appears in Klaviyo.  
2.19 Click **TURN ON ZAP**.  

> **Do you see the new subscriber in Klaviyo?**  
> *If not, check the Zapier task history for errors, ensure the webhook URL is correct, and re‑test the Beehiiv form.*

---

### 3. Create a List in Klaviyo for the Nurture Flow  
3.1 Return to Klaviyo.  
3.2 In the left sidebar, click **LISTS & SEGMENTS**.  
3.3 Click **+ NEW LIST**.  
3.4 Name it **“Beehiiv Nurture List”**.  
3.5 Toggle **“Add subscribers automatically”** to ON.  
3.6 Click **SAVE**.  

> **Do you see “Beehiiv Nurture List” in the list view?**  
> *If not, refresh the page or re‑create the list.*

---

### 4. Import the List into a New Flow  
4.1 In the Klaviyo sidebar, click **Flows**.  
4.2 Click **+ CREATE FLOW**.  
4.3 Choose **“Create from scratch”**.  
4.4 Name the flow **“Beehiiv Nurture Sequence”**.  
4.5

## Check-In: Module 5 Complete

- [ ] Build a High-Conversion Landing Page on Shopify completed and verified
- [ ] Set Up Lead Generation with Apollo.io completed and verified
- [ ] Create Automated Email Nurture Sequence in Klaviyo completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 6: DELIVERY

## Overview  
Module 6 is the lifeline of every AI‑powered newsletter business. It teaches you how to turn raw content into a repeatable, high‑quality delivery pipeline that keeps clients satisfied and your reputation intact. You’ll learn to set up automated workflows that run on Beehiiv and Mailchimp, establish rigorous quality checkpoints, and create standardized client communication templates that scale. Skipping this module means you’ll hand‑deliver newsletters at increasing cost, risk losing subscribers to competitors, and expose your brand to inconsistent quality and missed deadlines.  

The module is built around two core procedures: (1) Designing a delivery pipeline that pulls AI‑generated content from Replit or Midjourney, routes it through Zapier or Make.com, and pushes it into Beehiiv or Mailchimp; (2) Setting up quality assurance checks and client communication flows that leverage Beehiiv’s built‑in analytics and Mailchimp’s preview features. By mastering these steps you’ll guarantee on‑time delivery, maintain brand voice, and free yourself to focus on scaling.  

| Tool          | Purpose                                                      | Free Tier                                               | Paid Tier (Monthly) |
|---------------|--------------------------------------------------------------|----------------------------------------------------------|---------------------|
| Beehiiv       | Newsletter publishing and subscriber analytics               | 5 000 subscribers, 5 000 sends/month                    | $10 (10 000 sub)    |
| Mailchimp     | Email marketing and automation                              | 2 000 contacts, 10 000 sends/month                      | $9.99 (5 000 sub)   |
| Zapier        | Workflow automation between AI tools and email platforms     | 100 tasks/month, 5 apps                                 | $19.99 (Unlimited)  |
| Make.com      | Advanced automation and API orchestration                    | 100 operations/month, 100 kB storage                    | $49 (5 000 op)      |
| Replit        | AI‑code generation and script hosting                        | Unlimited public repos, 100 MB storage                  | $7 (private repos) |
| Canva         | Design templates for newsletter graphics                    | 5 000 templates, 30 GB storage                          | $12 (pro plan)      |

**Estimated time to complete**: 3 – 4 hours (including setup, testing, and documentation).

---

## Procedure 6.1: DEPLOY THE AI‑NEWSLETTER PRODUCT TO PRODUCTION ON HOSTINGER

1. **Log into Hostinger.**  
   1.1 Open a browser and go to **https://www.hostinger.com/login**.  
   1.2 Enter your email and password.  
   1.3 Click **Login** (button in the top‑right corner).  
   1.4 You should land on the dashboard with the “Hosting” card highlighted.

2. **Create a new hosting account.**  
   2.1 Click **Hosting** in the left navigation.  
   2.2 Click **Add Hosting** (bolded button).  
   2.3 Select **Shared Hosting – Ultra** (the lowest priced tier).  
   2.4 Click **Select**.  
   2.5 Choose the domain you bought (or click **Add a new domain** and register a new one).  
   2.6 Click **Continue** → **Set up hosting**.  
   2.7 Enter the admin username “admin”, password “StrongPass!23”, confirm password, and click **Create Account**.  
   2.8 The hosting account should appear in the list with a status “Active”.

3. **Set up SSL/TLS.**  
   3.1 In the hosting panel, click **SSL**.  
   3.2 Click **Let’s Encrypt** → **Install**.  
   3.3 After a few seconds, the green checkmark appears.  
   3.4 Click **Close**.

4. **Upload your application files.**  
   4.1 Click **File Manager** (bolded button).  
   4.2 In the file tree, open the folder named **public_html**.  
   4.3 Click **Upload** → **Choose Files**.  
   4.4 Select the ZIP file **newsletter‑app.zip** from your computer.  
   4.5 When the upload finishes, click **Extract** → **Extract Here**.  
   4.6 After extraction, you should see folders: **app**, **config**, **public**.  
   4.7 **Check‑in:** Do you see the folder named **app

---

## Procedure 6.2: Build Quality Assurance and Client Communication Templates

1. **Open your web browser** and navigate to **https://beehiiv.com/login**.  
2. In the login page, enter your **Beehiiv email** and **password**.  
3. Click the button **Log In** (the blue button in the center).  
4. **Do you see the Beehiiv Dashboard with the “+ New Campaign” button?**  
   - If not, verify that you are logged into the correct account.  
   - If still not visible, clear your browser cache and refresh.  

5. Click the **“+ New Campaign”** button (top‑right, green).  
6. In the pop‑up, name your campaign **“Client QA & Communication”** and click **Create**.  
7. In the campaign editor, click the **“Template”** tab.  
8. **Do you see the template editor with a blank canvas?**  
   - If not, click **“Manage Templates”** → **“Add New”**.  

9. Click **“Import”** → **“Upload HTML”**.  
10. Download the provided QA template from our shared folder: **https://cumulus.menshlyglobal.com/qa_template.html**.  
11. Upload the file and hit **Apply**.  
12. **Do you see the imported QA template with the header “Quality Assurance Checklist”?**  
   - If the header is missing, double‑check that the HTML file was correctly uploaded.  

13. Open a new tab and navigate to **https://chat.openai.com**.  
14. In ChatGPT, type:  
   ```markdown
   Draft a polite email to a client after a newsletter audit, including a concise summary and next steps.  
   ```  
15. Copy the generated email into a new **Google Docs** document titled **“Client QA Email Draft”**.  
16. **Do you see the email draft with subject line “Newsletter QA Summary” and body content?**  
   - If not, re‑run the prompt in ChatGPT and copy again.  

17. Open [**Canva**](https://www.canva.com/) at **https://www.canva.com**.  
18. Click **Create a design** → **Custom size**, set **800 × 400 px**, and click **Create new design**.  
19. In the left panel, click **Uploads** → **Upload media** → select the **client logo** file from your computer.  
20. Drag the logo onto the canvas and position it at the top‑left.  
21. Click **Text** → **Add a heading** → type **“Newsletter QA Summary”**.  
22. Adjust the font to **Montserrat**, size **48pt**, color **#333333**.  
23. Click **Download** → format **PNG** → click **Download**.  
24. **Do you see the PNG file downloaded with the correct dimensions?**  
   - If the file size is >2 MB, reduce the quality to 80% before downloading.  

25. Return to Beehiiv.  
26. In the campaign editor, click **“Attachments”** → **Add attachment** → choose the PNG file you just created.  
27. Click **Save**.  
28. **Do you see the attachment icon next to the campaign title?**  
   - If not, ensure the file is under 5 MB and try re‑uploading.  

29. Open **Zapier** at **https://zapier.com/app/dashboard**.  
30. Click **Create Zap**.  
31. For the **Trigger app**, search and select **Mailchimp**.  
32. Choose the trigger event **“New Subscriber”** and click **Continue**.  
33. Connect your **Mailchimp account** (API key: **`YOUR_MAILCHIMP_KEY`**).  
34. Test the trigger; you should see a sample subscriber data block.  
35. Click **Continue**.  

36. For the **Action app**, search and select **Beehiiv**.  
37. Choose the action **“Send Campaign”** and click **Continue**.  
38. Map the subscriber email from Mailchimp to Beehiiv’s **Recipient Email** field.  
39. Set the **Campaign ID** to the ID of the “Client QA & Communication” campaign (found in the URL: `beehiiv.com/campaigns/123456`).  
40. Click **Test & Review**.  
41. **Do you see a success message “Campaign queued for delivery”?**  
   - If you see **“Error: Invalid API Key”**, double‑check your Beehiiv API key in Zapier settings.  

42. Click **Turn on Zap**.  
43. **Do you see the Zap status as “On” in the dashboard?**  
   - If not, click **Retry** and ensure both accounts are authenticated.  

44. Open **Mailchimp** at **https://admin.mailchimp.com**.  
45. Navigate to the **Audience** tab → **Audience dashboard** → **View Contacts**.  
46. Select a test contact and click **Manage** → **Add note**.  
47. In the note field, type **“QA Email Sent: [Date]”** and click **Save note**.  
48. **Do you see the note appended to the contact record?**  
   - If not, refresh the page and confirm the note field was filled.  

49. Finally, open **Klavia** (optional but

## Check-In: Module 6 Complete

- [ ] DEPLOY THE AI‑NEWSLETTER PRODUCT TO PRODUCTION ON HOSTINGER completed and verified
- [ ] Build Quality Assurance and Client Communication Templates completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 7: SCALING

## Overview  

In this module you will transition from a solo AI newsletter operator to a fully‑scaled, revenue‑generating team.  We will dissect the entire funnel—from client acquisition to deliverable creation—then add the automation layer that turns a one‑person operation into a lean, high‑margin machine.  Skipping this module means you’ll continue to hand‑craft every email, hit inbox limits, and under‑value your expertise.  Instead, you will learn how to use Beehiiv and Mailchimp as the core inbox engines, hook them into Make.com for bi‑directional data flow, and deploy a clean SOP for your first contractor.  The result is a repeatable, auditable workflow that delivers instant ROI and scales linearly with subscriber count.

The module is split into three concrete procedures: (1) “Set Up Beehiiv & Mailchimp Sync,” (2) “Automate Content Distribution with Make.com,” and (3) “Hire & Onboard Your First Contractor.”  Each procedure contains step‑by‑step commands, check‑ins, and error handling, ensuring nothing is left to guesswork.  By the end you will have a documented pipeline that can be replicated across multiple clients, guaranteeing a margin of 60‑70 % on average.

**Tool Stack (free vs paid)**  

| Tool         | Purpose                                            | Free Tier (Limits)                               | Paid Tier (Starter)                          |
|--------------|-----------------------------------------------------|--------------------------------------------------|----------------------------------------------|
| Beehiiv      | Newsletter creation & subscriber management         | 500 subscribers, 1 campaign/month               | $30 / month: 10 k subscribers, unlimited campaigns |
| Mailchimp    | Email delivery & analytics                          | 2 000 contacts, 10 000 sends/month              | Essentials: $11 / month (50 k contacts)     |
| Make.com     | Workflow automation & API integration               | 200 operations/month, 1‑step zaps                | Starter: $9 / month (2 000 ops, multi‑step zaps) |
| Zapier       | Simple trigger/response automation                  | 100 tasks/month, 5 Zaps                          | Starter: $19.99 / month (2 000 tasks, 20 Zaps) |
| Notion       | SOP & project management                            | Unlimited pages, 1 000 blocks                   | Personal Pro: $4 / month (increased block limit) |
| ActiveCampaign | Advanced email sequencing                         | Trial 14 days, no free tier                     | Lite: $15 / month (5 000 contacts)          |

**Estimated time to complete Module 7**  
≈ 10 hours (including deep dives into each tool, SOP creation, and contractor onboarding).

---

## Procedure 7.1: Hire Your First Contractor on Upwork

1. **Open a web browser** and navigate to <https://www.upwork.com>.  
   *Expected output:* Upwork home page with the “Sign Up” button visible at the top right corner.

2. Click the **Sign Up** button.  
   *Expected output:* Sign‑up page with two options: “Client” and “Freelancer”.

3. Select **Client** and click **Continue**.  
   *Expected output:* “Create a new account” form.

4. Fill in the form:  
   - **Email:** your business email (e.g., `you@yourdomain.com`)  
   - **Password:** at least 8 characters, include a number and a symbol  
   - **Country:** United States  
   Then click **Continue**.  
   *Expected output:* Verification email sent to your inbox.

5. Open your email, click the verification link, and then return to Upwork.  
   *Interactive check‑in:* Do you see the “Create your profile” screen?  
   If not, **click the “Go to your profile” link** on the email confirmation page.

6. Click **Create your profile**.  
   *Expected output:* Profile setup wizard.

7. Fill in profile details:  
   - **Title:** “AI Newsletter Automation Project Owner”  
   - **Hourly rate range:** $50–$70 (set later)  
   - **Skills:** “AI Automation”, “Newsletter Marketing”, “Mailchimp”, “Beehiiv”  
   Click **Continue**.  
   *Expected output:* “Add work experience” screen.

8. Skip work experience (you’ll add it later) and click **Continue**.  
   *Expected output:* “Add your education” screen.

9. Skip education and click **Continue**.  
   *Expected output:* “Add your professional summary” screen.

10. Write a brief summary:  
    “Looking for an experienced freelancer to design, build, and automate AI‑driven newsletter workflows using Beehiiv and Mailchimp. Must be familiar with Make.com integrations and Canva for visual assets.”  
    Click **Continue**.  
    *Interactive check‑in:* Do you see the “Add a portfolio example” screen?  
    If not, **click “Skip for now”**.

11. Scroll to the bottom and click **Set a budget**.  
    - **Budget type:** Fixed‑price  
    - **Estimated budget:** $1,200 (will be adjusted later)  
    Click **Continue**.  
    *Expected output:* “Create a job posting” page.

12. Click **Create a job posting**.  
    *Expected output:* Job posting editor.

13. In the job title field, type **“AI Newsletter Automation Specialist”** and click **Continue**.  
    *Expected output:* “Job description” screen.

14. Paste the following job description:  

    ```
    • Design AI‑driven newsletter templates in Canva (free tier up to 5 templates per month).
    • Build automation workflows in Make.com (free tier: 100 tasks/month, paid plan $19/month for 3,000 tasks).
    • Integrate Mailchimp and Beehiiv via Zapier (Zapier free tier: 5 Zaps, paid plan $19.99/month for 100 Zaps).
    • Write engaging copy with ChatGPT (OpenAI free tier: 3,000 tokens/day, paid plan $20/month for 1M tokens).
    • Deliver final assets within 2 weeks.
    ```

    Click **Continue**.  
    *Expected output:* “Add skills” screen.

15. Add the following skills: [**Make.com**](https://www.make.com/en/register?pc=menshly), **Canva**, **Mailchimp**, **Beehiiv**, **Zapier**, **ChatGPT** (each as separate skill).  
    Click **Continue**.  
    *Interactive check‑in:* Do you see the “Set your budget” screen again?  
    If not, **scroll to the bottom** of the posting editor and click **Set your budget**.

16. Confirm the budget: $1,200 fixed‑price, payment terms: “Pay at completion”.  
    Click **Publish job**.  
    *Expected output:* “Job published successfully” banner.

17. Wait for proposals. After 48 hours, go to **Dashboard > Jobs > My Jobs**.  
    Click the job title to view proposals.  
    *Expected output:* List of freelancer proposals.

18. Filter proposals by **“Top Rated”** and **“Hourly Rate ≤ $70”**.  
    Click **View Profile** on each candidate.  
    *Expected output:* Freelancer profile with portfolio and client reviews.

19. **Shortlist** 3 candidates by clicking

---

## Procedure 7.2: Build SOPs for Task Delegation in Notion

1. **Open Notion**  
   - URL: `https://www.notion.so/`  
   - Log in with your credentials.  
   - On the left sidebar, click **+ New Page** (bold).  
   - Name the page **“Task Delegation SOPs”** and press **Enter**.  
   - *Expected output:* A blank page titled “Task Delegation SOPs” appears.

2. **Create a Parent Database**  
   - In the new page, type `/table inline` and press **Enter**.  
   - Click **+ New database** → **Table** and name it **“Delegated Tasks”**.  
   - Add properties:  
     - **Task** (Title)  
     - **Owner** (Person)  
     - **Due Date** (Date)  
     - **Status** (Select: Not Started, In Progress, Completed)  
     - **SOP Link** (URL)  
   - *Expected output:* A table with the specified columns.

3. **Add an SOP Template**  
   - In the same page, type `/page` and press **Enter**.  
   - Name the page **“Standard SOP Template”**.  
   - Inside, insert a toggle list titled **“Step-by-Step Instructions”**.  
   - Under the toggle, add numbered bullets for 10 generic steps (e.g., “1. Define objective… 2. Gather resources…”).  
   - Highlight the entire list and click **Duplicate** (top‑right menu).  
   - Rename the duplicate to **“Client Onboarding SOP”**.  
   - *Expected output:* Two SOP pages, one generic template and one specific example.

4. **Link SOP to Task**  
   - Return to the **“Delegated Tasks”** table.  
   - In the first row, click the **SOP Link** cell, paste the URL of **“Client Onboarding SOP”** (`https://www.notion.so/...`) and press **Enter**.  
   - Ensure the link opens in a new tab.  
   - *Expected output:* The cell displays a clickable link labeled “Client Onboarding SOP”.

5. **Set Up Automated Task Creation via Zapier**  
   - URL: `https://zapier.com/app/dashboard`  
   - Click **+ Create Zap**.  
   - For **Trigger**, search for **“Mailchimp”** and select **“New Subscriber”**.  
   - Connect your Mailchimp account (API key: `mc-XXXXXXXXXXXXXXXX`).  
   - Test the trigger: you should see a sample subscriber record.  
   - *Expected output:* Zap ready with a sample data preview.

6. **Configure Zap Action to Create Notion Task**  
   - Click **+ Add Action** → search **“Notion”** → select **“Create Database Item”**.  
   - Connect Notion using the integration token from `https://www.notion.so/my-integrations`.  
   - Map fields:  
     - **Task** ← “First Name” + “Last Name” + “Subscribed to Newsletter”  
     - **Owner** ← select a team member (e.g., “Alice”)  
     - **Due Date** ← set to `Today + 2 days` (use **Date** function)  
     - **Status** ← “Not Started”  
     - **SOP Link** ← `https://www.notion.so/.../Client-Onboarding-SOP`  
   - Test action; you should see a new row appear in the **Delegated Tasks** table.  
   - *Expected output:* A new task row with correct data.

7. **Verify Zap Success**  
   - Return to Zapier, click **Task History**.  
   - Confirm the most recent run status is **“Success”**.  
   - If **“Error”** appears, it usually means the Notion token is missing or expired.  
   - *Error scenario:* If you see **“Invalid token”**, this means the integration token is invalid.  
     - **Fix:** Re‑generate a token at `https://www.notion.so/my-integrations` and re‑connect in Zapier.

8. **Add a Reminder Using Make.com**  
   - URL: `https://www.make.com/`  
   - Click **Create new scenario**.  
   - Add a **“Notion”** module: **“Watch Database Items”** → select the **Delegated Tasks** database.  
   - Add a **“Filter”** module: **Status = Not Started**.  
   - Add a **“Send Email”** module (Gmail).  
     - To: the **Owner** field value (use dynamic variable).  
     - Subject: “Task Reminder: {{Task}} due {{Due Date}}”.  
     - Body: “Please complete the task. SOP: {{SOP Link}}”.  
   - Turn on the scenario.  
   - *Expected output:* Email is sent to the owner 24 hours before the due date

---

## Procedure 7.3: Run a Margin Analysis and Pricing Review

1. **Open Beehiiv Dashboard** – Navigate to <https://app.beehiiv.com>.  
   • Log in with your credentials.  
   • In the left‑hand sidebar click **Analytics**.  
   • Click the **Export CSV** button (top‑right, labeled **Export CSV** with a down arrow icon).  
   – *Expected output*: A file named `beehiiv_analytics_YYYYMMDD.csv` downloads to your computer.  

2. **Open Mailchimp Dashboard** – Navigate to <https://mailchimp.com>.  
   • Click **Login** → enter credentials.  
   • From the main menu click **Audience** → **All contacts**.  
   • Click the **Export audience** button (icon: floppy disk).  
   – *Expected output*: `mailchimp_audience_YYYYMMDD.csv` downloads.  

3. **Create a New Spreadsheet in Google Sheets** – Open <https://sheets.google.com> → Click **Blank** → rename to `Margin Analysis – YYYYMMDD`.  
   • In cell `A1` type `Beehiiv Metrics`.  
   • In cell `A2` type `Total Recovered Revenue`.  
   • In cell `B2` type `=IMPORTDATA("file:///path/to/beehiiv_analytics_YYYYMMDD.csv")` (replace path with actual local path).  
   – *Expected output*: Beehiiv revenue numbers populate column B.  

4. **Import Mailchimp Data** – In cell `A4` type `Mailchimp Metrics`.  
   • In cell `A5` type `Total Subscribers`.  
   • In cell `B5` type `=IMPORTDATA("file:///path/to/mailchimp_audience_YYYYMMDD.csv")` (replace path).  
   – *Interactive Check‑in*: **Do you see the Mailchimp subscriber list loaded in column B?** If not, verify the file path and that the CSV is not encrypted.  

5. **Calculate Monthly Costs** – In cell `A7` type `Cost Breakdown`.  
   • In cell `A8` type `Beehiiv Monthly Fee`.  
   • In cell `B8` type `=IF(OR(B2>500000, B2<0), 499, 149)` – Beehiiv charges $499 for >$500k revenue, $149 otherwise.  
   • In cell `A9` type `Mailchimp Monthly Fee`.  
   • In cell `B9` type `=IF(OR(B5>20000, B5<0), 299, 0)` – Free tier for ≤20k contacts, $299 for >20k.  
   • In cell `A10` type `Zapier Monthly Fee`.  
   • In cell `B10` type `=IF(OR(B5>0, B2>0), 19, 0)` – Free tier covers 1000 tasks/month, $19 for 2,000 ops.  
   – *Expected output*: Row 8–10 show exact monthly fees.  

6. **Sum Total Monthly Costs** – In cell `A12` type `Total Monthly Costs`.  
   • In cell `B12` type `=SUM(B8:B10)`.  
   – *Interactive Check‑in*: **Do you see a single number in B12 representing total costs?** If not, check that all cost cells contain numeric values.  

7. **Calculate Gross Margin** – In cell `A14` type `Gross Margin`.  
   • In cell `B14` type `=B2-B12`.  
   – *Expected output*: Positive number indicating pre‑tax margin.  

8. **Compute Margin Percentage** – In cell `A16` type `Margin %`.  
   • In cell `B16` type `=B14/B2`.  
   – *Expected output*: A decimal (e.g., 0.23) representing 23% margin.  

9. **Create Pricing Recommendation Table** – In cells `E1`–`G5` create headers:  
   - `E1`: `Plan`  
   - `F1`: `Suggested Monthly Price`  
   - `G1`: `Target Margin %`  
   • Fill `E2` with `Basic` → `F2` with `$99` → `G2` with `0

## Check-In: Module 7 Complete

- [ ] Hire Your First Contractor on Upwork completed and verified
- [ ] Build SOPs for Task Delegation in Notion completed and verified
- [ ] Run a Margin Analysis and Pricing Review completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 8: ADVANCED PATTERNS

## Overview  

Module 8 dives into the high‑impact, premium playbooks that transform a one‑off newsletter into a recurring revenue engine. You’ll learn how to layer AI‑powered content generation, dynamic subscriber segmentation, and micro‑automation to create a productized service that clients pay for on a retainer basis. By mastering these patterns you unlock the ability to upsell advanced features—such as personalized deep‑dive articles, AI‑generated video teasers, and predictive engagement triggers—turning a simple newsletter into a full‑fledged marketing machine.

Skipping this module means settling for “good enough.” You’ll miss the chance to bundle AI‑driven analytics, automated A/B testing, and seamless integrations with CRM and e‑commerce platforms. Clients will see only basic email flows, and your margin will stay stagnant. The advanced patterns taught here are the difference between a freelance newsletter writer and a scalable SaaS‑style subscription business that can command 6‑figure monthly revenues.

| Tool        | Purpose                                 | Free Tier                                           | Paid Tier (Monthly) |
|-------------|-----------------------------------------|-----------------------------------------------------|---------------------|
| Beehiiv     | Newsletter platform & subscriber hub   | Unlimited free newsletters, 1,000 subscribers       | $30 for 10,000 subs |
| Mailchimp   | Email marketing & automation           | 2,000 contacts, 10k sends                           | $10 for 5k contacts |
| Make.com    | Workflow automation & API orchestration| 500 operations, 5 min run time                      | $49 for 100k ops    |
| Zapier      | App‑to‑app integration                 | 5 Zaps, 100 tasks per month                         | $19 for 2k tasks    |
| Canva       | AI‑assisted graphic & video creation   | Unlimited free designs, 5 templates                 | $12 for Pro plans   |
| ChatGPT     | AI content generation & QA            | 100 messages/month                                  | $20 for 175k msgs   |

**Estimated time to complete**: **4 – 5 hours** (including hands‑on automation setup, AI content creation, and revenue‑model validation).

---

## Procedure 8.1: Create a High‑Ticket Consulting Package

1. **Open Beehiiv Dashboard**  
   Go to **https://app.beehiiv.com**.  
   Click **SIGN IN** in the top‑right corner and enter your credentials.  
   *Expected result:* Beehiiv landing page shows your subscriber list and dashboard widgets.  

2. **Create a New Newsletter Series**  
   Click the **+ NEW SERIES** button (top‑left).  
   In the pop‑up, type **“AI Newsletter Consulting Package – 12‑week Program”** into the **Series Name** field.  
   Select **Monthly** under **Send Frequency**.  
   Click **CREATE SERIES**.  

3. **Set Up Subscription Landing Page**  
   In the series overview, click **LANDING PAGE** tab.  
   Click **EDIT LANDING PAGE**.  
   In the editor, replace the default headline with **“Unlock AI‑Powered Revenue in 12 Weeks”**.  
   Add a form field **“Full Name”** (mandatory) and **“Business Email”** (mandatory).  
   Click **SAVE** (bottom‑right).  

4. **Add a Payment Gatekeeper**  
   In the landing page editor, click **+ ADD BLOCK** → **Payments** → **Stripe**.  
   Connect your Stripe account by clicking **CONNECT** and following the OAuth flow.  
   Set the price to **$5,000** and label the button **“Enroll Now – $5,000”**.  
   Click **SAVE**.  

   *Do you see the Stripe payment block with the $5,000 button? If not, check that your Stripe account is verified and retry the CONNECT step.*  

5. **Draft the Welcome Email**  
   Go to the **EMAILS** tab and click **+ NEW EMAIL**.  
   Choose **“Welcome – AI Consulting”** as the subject.  
   In the editor, paste the following text:  
   ```
   Hi {{ subscriber.full_name }},
   Thank you for enrolling in our 12‑week AI Newsletter Consulting Package.  
   Your first deliverable will be a personalized AI content calendar.  
   Stay tuned!
   ```  
   Click **PREVIEW** to ensure the merge tag **{{ subscriber.full_name }}** displays correctly.  
   Click **SAVE & RETURN**.  

6. **Create a Zapier Automation to Sync Subscribers**  
   Open a new tab and go to **https://zapier.com**.  
   Click **SIGN IN** → **Dashboard** → **Create Zap**.  
   Set **Trigger** app to **Beehiiv** → **New Subscriber** (choose the series you created).  
   Click **TEST & REVIEW**.  
   Set **Action** app to **Mailchimp** → **Add/Update Subscriber**.  
   Map Beehiiv fields:  
   - **Email** → **Email Address**  
   - **Full Name** → **First Name** (split if necessary)  
   Click **TEST & ACTIVATE**.  

7. **Verify Mailchimp List Integration**  
   In Mailchimp, go to **Audience** → **All contacts**.  
   Click **Manage Audience** → **Settings** → **Audience name and defaults**.  
   Ensure the audience ID matches the Zapier integration.  
   Click **Save**.  

   *Do you see the new subscriber in Mailchimp’s All contacts list? If not, confirm the Zap is active and the Beehiiv webhook URL is correct.*  

8. **Set Up Automated Weekly Email Schedule**  
   Back in Beehiiv, navigate to the **SCHEDULE** tab.  
   Click **+ NEW WEEKLY EMAIL**.  
   Title it **“Week # – AI Tips & Deliverables”**.  
   In the editor, add placeholders:  
   ```
   Hello {{ subscriber.full_name }},
   Week {{ week_number }} Deliverable: {{ deliverable_title }}
   ```  
   Set the send time to **Mondays at 9:00 AM PST**.  
   Click **SAVE & SCHEDULE**.  

9. **Add a Review and Feedback Loop**  
   In Beehiiv, click **+ NEW EMAIL** → **“Feedback Request – Week #”**.  
   Draft:  
   ```
   Hi {{ subscriber.full_name }},
   How did the Week # deliverable help your AI strategy?  
   Please rate 1‑5 and share any questions.
   ```  
   Use the **Link** block to embed a Google Form link.  
   Click **SAVE**.  

10. **Create a Revenue Tracking Sheet in Notion**  
    Open **https://www.notion.so** and click **+ New Page**.  
    Title it **“AI Consulting Revenue Tracker”**.  
    Insert a **Table

---

## Procedure 8.2: Create Subscription Tiers on Shopify  

1. **Log Into Shopify Admin**  
   - Open your browser and go to `https://www.shopify.com/admin`.  
   - Click **Log in** (top‑right).  
   - Enter your store’s email, password, and click **Log in** (bold).  

   *Expected output*: You see the Shopify Admin dashboard with the sidebar menu (Products, Orders, Customers, etc.).  

2. **Verify Your Shopify Plan**  
   - Click the gear icon (⚙️) in the bottom-left corner → **Plan**.  
   - Confirm you are on **Basic Shopify** ($29/month) or higher.  
   - If you see “Subscriptions are not available on this plan”, click **Change plan** → select **Advanced Shopify** ($299/month) and click **Continue**.  

   *Check‑in*: Do you see the **Plan** page with the plan name and price? If not, click the gear icon again (⚙️) → **Settings** → **Plan**.  

3. **Install Bold Subscriptions App**  
   - Open a new tab and navigate to `https://boldcommerce.com/apps/subscriptions`.  
   - Click **Add app** (bold).  
   - When prompted, click **Install Bold Subscriptions** (bold).  
   - On the next screen, click **Continue** → **Authorize** (bold).  

   *Expected output*: Bold Subscriptions dashboard appears with a welcome banner.  

4. **Create a New Product for Subscription**  
   - Return to the Shopify Admin tab.  
   - Click **Products** → **All products** → **Add product** (bold).  
   - In the **Title** field, type **AI Newsletter Subscription**.  
   - In the **Description** box, paste the following:  
     > “Subscribe to our AI‑generated newsletter for exclusive insights, delivered weekly. Choose a tier that fits your needs.”  

   *Check‑in*: Do you see the product page with the title and description you entered? If not, refresh the page.  

5. **Add Variants for Tiers**  
   - Scroll to the **Variants** section.  
   - Click **Add variant** (bold).  
   - For the first variant, set **Title** to **Basic Tier** and **Price** to **$9.99**.  
   - Click **Add variant** again and set **Title** to **Premium Tier** and **Price** to **$19.99**.  
   - Click **Save** (bold).  

   *Expected output*: Two variants appear under the product with their respective prices.  

6. **Enable Subscription for Each Variant**  
   - In the Bold Subscriptions dashboard, click **Products** → **Add subscription** (bold).  
   - Search for “AI Newsletter Subscription” and click **Select** (bold).  
   - For each variant, toggle **Enable subscription** to **On**.  
   - Set **Billing interval** to **Weekly** for both tiers.  
   - Click **Save** (bold).  

   *Check‑in*: Do you see the subscription toggle turned on next to each variant? If not, ensure

## Check-In: Module 8 Complete

- [ ] Create a High‑Ticket Consulting Package completed and verified
- [ ] Create Subscription Tiers on Shopify completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 9: FINANCIAL OPERATIONS

## Overview  
In this module we turn the raw revenue data from your AI‑driven newsletter service into a crystal‑clear financial operating system. You will learn how to build a live revenue dashboard, set up automated alerts for key metrics, and create a systematic pricing‑increase cadence that maximizes margin without scaring off clients. We’ll also deliver ready‑made proposal and contract templates that you can plug into your workflow, ensuring every new project starts with a clear scope, pricing, and payment terms.  

Skipping this module means you’ll never know whether a price bump is hurting churn, you’ll miss out on real‑time profit signals, and you’ll hand clients a vague, inconsistent proposal that erodes trust. In the competitive AI‑newsletter market, a robust financial ops layer is the secret to sustainable scaling and the ability to reinvest in higher‑value automation.

| Tool       | Purpose                                        | Free Tier                                   | Paid Tier (USD) |
|------------|------------------------------------------------|---------------------------------------------|-----------------|
| Beehiiv    | Newsletter creation & revenue reporting        | 5k subscribers/month, basic analytics       | $30/month (Pro) |
| Mailchimp  | Email automation & billing integration         | 2k contacts, 12k sends/month                | $89/month (Standard) |
| Zapier     | Workflow automation between tools               | 100 tasks/month, basic triggers             | $19/month (Starter) |
| Notion     | Financial dashboard & proposal templates       | Unlimited pages, 5 guests                   | $8/user/month (Pro) |
| Klaviyo    | Advanced segmentation & revenue attribution    | 2k contacts, 500 sends/month                | $20/month (Starter) |
| Make.com   | Low‑code data integration & scheduling         | 500 operations/month, basic connectors      | $9/month (Starter) |
| Replit     | Quick script prototyping & data analysis       | Unlimited public repls, 500 MB storage      | $7/month (Hacker) |
| Apollo.io  | Prospecting & client outreach                  | 500 credits/month, limited search           | $39/month (Starter) |

**Estimated time to complete:** 3–4 hours (including setup, testing, and template customization).

---

## Procedure 9.1: Build a Live Revenue Dashboard in Notion with Make.com

1. **Open Notion**  
   - Visit `https://www.notion.so/` and click **Log in** in the top‑right corner.  
   - Enter your email & password, then click **Continue**.  
   - After login, you should see your workspace home page.  

   *Do you see the workspace home page? If not, check your internet connection and try again.*

2. **Create a new database**  
   - On the left‑hand sidebar, click **+ Add a page**.  
   - In the pop‑up, choose **Table – Inline** and click **Create**.  
   - Title the database **Revenue Dashboard**.  

   *Do you see a blank table titled “Revenue Dashboard”? If not, refresh the page.*

3. **Add essential properties**  
   - Hover over the first column header, click **+ Add a property**.  
   - Name it **Month** and select type **Date**.  
   - Add another property: click **+ Add a property**, name it **Beehiiv Subscriptions**, type **Number**.  
   - Add **Mailchimp Subscriptions** (Number) and **Total Revenue** (Number).  

   *Do you see four columns (Month, Beehiiv Subscriptions, Mailchimp Subscriptions, Total Revenue)?*

4. **Insert a formula for Total Revenue**  
   - Click the header of **Total Revenue**, choose **+ Add a property** → **Formula**.  
   - In the formula editor, enter: `prop("Beehiiv Subscriptions") * 5 + prop("Mailchimp Subscriptions") * 3`.  
   - Click **Done**.  

   *Do you see the formula applied (green checkmark)? If not, ensure the syntax matches exactly.*

5. **Create a view for monthly totals**  
   - Click **+ Add a view**, choose **Table**, name it **Monthly Totals**, click **Create**.  
   - In the view options, click **Filter** → **Add a filter**, set **Month** is **within** the current month.  

   *Do you see a table filtered to the current month?*

6. **Generate a Notion Integration**  
   - In the top‑right corner, click your profile icon → **Settings & Members** → **Integrations**.  
   - Click **+ New integration**, give it the name **Revenue Bot**, set **Capabilities** to **Read & Write**.  
   - Under **API key**, click **Copy**.  

   *Do you see the API key copied? If not, click **Show** to reveal it.*

7. **Invite the integration to the database**  
   - Go back to the **Revenue Dashboard** page.  
   - Click **Share**, paste the integration name **Revenue Bot**, and toggle **Invite**.  
   - Ensure the integration has **Full Access**.  

   *Do you see the integration listed in the Share menu?*

8. **Open Make.com**  
   - Visit `https://www.make.com/`.  
   - Click **Sign in** (top‑right) and log in with your credentials.  

   *Do you see the Make.com dashboard? If not, clear your browser cache and retry.*

9. **Create a new scenario**  
   - In the dashboard, click **Create new scenario**.  
   - Search for **HTTP** and drag the **HTTP > Make a request** module onto the canvas.  

   *Do you see the HTTP request module?*

10. **Configure Beehiiv API call**  
    - In the HTTP module, set **Method** to **GET**.  
    - **URL**: `https://api.beehiiv.com/v1/subscribers?date=last_month`  
    - Under **Headers**, add `Authorization: Bearer YOUR_BEEHIIV_API_KEY`.  
    - Replace `YOUR_BEEHIIV_API_KEY` with your actual key from Beehiiv (found in your account settings).  
    - Click **Test**.  
    - The response should be a JSON array of subscribers.  

    *Do you see a JSON response with subscriber count? If you see `Error 401: Unauthorized`, double‑check your API key.*

11. **Add a JSON parser**  
    - Drag **JSON > Parse JSON** next to the HTTP module.  
    - In the input field, select the output of the HTTP module.  
    - In the **JSON schema**, paste: `{ "type":"object","properties":{"total": {"type":"integer"}} }`.  
    - Click **Test**.  
    - The parsed value `total` should appear

---

## Procedure 9.2: Create Proposal Templates and Automated Billing with Stripe

1. **Open Notion**  
   - URL: `https://www.notion.so/`  
   - Sign in with your email.  
   - In the left sidebar click **+ New Page** then name it **“AI Newsletter Proposal”**.  
   - In the page click **/heading 1** and type **“Proposal for AI‑Driven Newsletter Service”**.  

2. **Insert ChatGPT‑Generated Boilerplate**  
   - Click **/callout** → **ChatGPT** (If you have the Notion‑ChatGPT integration, otherwise copy‑paste from ChatGPT‑web).  
   - Prompt: *“Generate a detailed proposal for a solo entrepreneur offering automated AI newsletter services using Beehiiv and Mailchimp.”*  
   - Copy the output into the Notion page.  
   - Format: bold headings, bullet lists, and a *“Pricing”* table at the bottom.  

3. **Create a Pricing Table**  
   - Use **/table – inline** → **Full Width**.  
   - Columns: **Service**, **Description**, **Price**.  
   - Rows:  
     1. Beehiiv Subscription – “Newsletter hosting + AI automation” – **$49/month**  
     2. Mailchimp Email Automation – “Advanced email workflows” – **$30/month**  
     3. Stripe Billing – “Automated invoicing” – **Included**  
   - Highlight the **Price** column and click **/highlight** → **Green**.  

4. **Export the Proposal as PDF**  
   - In the top right corner click the three dots (…) → **Export** → **PDF**.  
   - Save the file as **AI_Newsletter_Proposal.pdf** on your desktop.  

5. **Upload PDF to Notion**  
   - Drag **AI_Newsletter_Proposal.pdf** into the Notion page.  
   - Click the PDF preview → **Open in new tab**.  
   - Verify the PDF displays correctly.  
   - **Check‑in:** Do you see the PDF preview in Notion? If not, re‑drag the file or click **+** → **Upload**.  

---

6. **Create a Stripe Account**  
   - URL: `https://dashboard.stripe.com/register`  
   - Click **Create your account** → Enter business name, email, and password.  
   - Verify your email and log in to the dashboard.  

7. **Enable Stripe Billing**  
   - In the Stripe dashboard left menu click **Billing** → **Subscriptions**.  
   - Click **+ New Plan** → Name: **“AI Newsletter Monthly”** → Price: **$79** → Currency: **USD**.  
   - Set **Billing cycle** to **Monthly**.  
   - Click **Save plan**.  

8. **Create a Customer for the Proposal**  
   - In the Stripe dashboard click **Customers** → **+ New**.  
   - Fill:  
     - **Email**: `client@example.com` (replace with real client)  
     - **Name**: `Client Name`  
     - **Description**: `AI Newsletter Service Proposal`  
   - Click **Save Customer**.  

9. **Create a Subscription**  
   - In the customer’s page click **+ Add subscription**.  
   - Select the plan **“AI Newsletter Monthly”**.  
   - Set **Start date** to today.  
   - Click **Create subscription**.  
   - You should see a green banner: *“Subscription created”* and a status **Active**.  

10. **Copy Subscription ID**  
    - Hover over the subscription row → click **Copy ID** (clipboard).  
    - Paste it into a Notion note for future reference: `Stripe Subscription ID: sub_XXXXXXXXXXXX`.  

    **Check‑in:** Do you see the subscription status as “Active” in Stripe? If not, verify plan selection.  

---

11. **Set

## Check-In: Module 9 Complete

- [ ] Build a Live Revenue Dashboard in Notion with Make.com completed and verified
- [ ] Create Proposal Templates and Automated Billing with Stripe completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 10: LAUNCH PLAN

## Overview

This module is the launch engine that takes your AI‑driven newsletter automation concept from an idea into a cash‑generating business. Over the next 30 days you will build a step‑by‑step execution calendar that covers everything from setting up your subscriber pipeline in Beehiiv and Mailchimp to automating content creation with Make.com, ensuring you secure your first paying client by Day 30. If you skip this module you risk launching a fragmented operation, missing critical integration checkpoints, and losing the momentum that turns prospects into revenue.

Why does it matter? Solo entrepreneurs rely on a tight cadence of deliverables to prove value quickly. This 30‑day roadmap forces you to perform the same high‑impact tasks you would do for any client: audience research, content scheduling, workflow automation, and performance analytics. By following the prescribed timeline you will eliminate guesswork, reduce trial‑and‑error cycles, and create a repeatable launch template you can reuse for every new client or new newsletter vertical.

Below is the tool stack for this module, including what each tool does, the free tier limits, and the paid tier that unlocks full functionality. All tools are chosen for their API reach, AI integration, and cost‑efficiency for solo operators.

| Tool         | Purpose                                                                 | Free Tier                                   | Paid Tier (Monthly) |
|--------------|--------------------------------------------------------------------------|---------------------------------------------|---------------------|
| Beehiiv      | Hosted newsletter platform with built‑in automation and analytics         | 1,000 subscribers, 1 paid plan, 2 free plans | $29 – $99 (pro)     |
| Mailchimp    | Email marketing & automation, advanced segmentation                      | 2,000 contacts, 10,000 sends/month          | $13 – $299 (Essentials+) |
| Make.com     | Visual automation platform, integrates Beehiiv, Mailchimp, AI tools       | 5,000 operations/month                     | $19 – $199 (Pro)   |
| Zapier       | Trigger‑action automation, connects with 3,000+ apps                      | 100 tasks/month, 5 Zaps                     | $19 – $599 (Starter‑Team) |
| Calendly     | Client appointment scheduling, integrates with Google Calendar           | 1 calendar, 1 user                          | $8 – $15 (Pro)     |
| Loom         | Video messaging and walkthroughs for client demos                          | 25 minutes per video, 3 videos/day          | $12 – $25 (Team)   |
| Notion       | Project & knowledge base, task tracking                                 | Unlimited pages, 5 users                    | $8 – $10 (Personal) |
| Grammarly    | AI‑powered grammar & tone checker for newsletters                        | 1,000 words/day, 3 languages                | $12 – $30 (Premium) |
| Canva        | Design templates for email headers, social graphics                      | Unlimited designs, 5 GB storage             | $12 – $30 (Pro)    |
| ChatGPT      | AI content generation, outlines, and subject line suggestions            | 3,000 tokens/month (ChatGPT‑Free)           | $20 (ChatGPT‑Plus) |

**Estimated Time to Complete Module 10**  
- **Setup & Integration:** 5 days  
- **Content & Workflow Design:** 10 days  
- **Automation Testing:** 5 days  
- **Client Outreach & Demo:** 5 days  
- **Launch & Optimization:** 5 days  

**Total:** **30 days** (including buffer for unforeseen delays).

---

**Procedure 10.1** — Generation failed due to AI backend unavailability. Please retry later.

---

## Procedure 10.2: Build Marketing Automation and Prospect List with Apollo.io

1. Open a browser and navigate to **https://app.apollo.io**. Log in with your credentials.  
2. From the left‑hand menu, click **People** → **Advanced Search**.  
3. In the filter panel, set the following exact values:  
   - **Company Size**: `50` – `200`  
   - **Title**: `Founder` OR `CEO`  
   - **Location**: `United States`  
   - **Industry**: `Technology`  
4. Click the **Apply Filters** button in the upper right corner.  
   **Do you see a list of prospects?** If not, refresh the page or double‑check that each filter is applied exactly as typed.  

5. While the list is displayed, click the **Export** button (top right). Choose **CSV** from the dropdown, then click **Export CSV**.  
6. A download named `apollo_export_YYYYMMDD.csv` should appear in your Downloads folder.  
   **Do you see the CSV file?** If not, open your Downloads folder and confirm the file name; re‑export if necessary.  

7. Open **Google Sheets** (https://sheets.google.com). Click **File** → **Import** → **Upload

---

## Procedure 10.3: Execute the 30‑Day Launch Calendar

1. **Create a Beehiiv account**  
   - Open browser → `https://bee

## Check-In: Module 10 Complete

- [ ] Configure Demo Scheduling with Calendly and Notion completed and verified
- [ ] Build Marketing Automation and Prospect List with Apollo.io completed and verified
- [ ] Execute the 30‑Day Launch Calendar completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# APPENDIX A: COMPLETE TOOL REFERENCE  

| Tool | Purpose | Free Tier | Paid Tier | When to Upgrade |
|------|---------|-----------|-----------|-----------------|
| **Hostinger** | Domain registration & web hosting (used in Module 1 & 6) | 1‑year domain for $0.99, 1 GB SSD, 1 GB bandwidth, 1 email; 30‑day money‑back guarantee | 1‑year plan: $1.99/month (1 GB SSD, 20 GB bandwidth, 5 GB storage), 3‑year plan: $0.99/month (10 GB SSD, 60 GB bandwidth, 20 GB storage) | When traffic exceeds 20 GB/month or you need 10 GB+ storage for AI assets. |
| [**Notion**](https://notion.so/) | Project management, SOPs, API key storage (Modules 2, 3, 7, 9) | Unlimited pages & blocks; 1 GB file upload limit; 5 GB storage | Personal Pro: $4/month (5 GB file upload, 50 GB storage), Team: $8/month per user (15 GB file upload, 100 GB storage) | Upgrade when you hit 1 GB file limit or need real‑time collaboration for >3 team members. |
| **Calendly** | Scheduling client intake calls (Module 3) | Basic: 1 calendar, 1 event type, 30‑minute buffer | Premium: $12/month per user (multiple calendars, custom buffers, integration with Zoom) | When you need more event types or branded scheduling pages. |
| **ChatGPT API** | Generating newsletter content (Modules 4, 8) | $0.00025 per 1,000 tokens (free trial 3 M tokens) | Standard: $0.02 per 1,000 tokens (GPT‑4) | Upgrade when you exceed 3 M tokens/month or need GPT‑4 for higher‑quality output. |
| **Make.com** | Automation between Beehiiv, Mailchimp, Replit, etc. (Modules 2–4) | 1,000 operations/month, 5 GB data transfer | Starter: $19/month (15,000 ops, 20 GB transfer) | Upgrade when operations >10,000/month or data transfer >10 GB. |
| [**Vapi**](https://vapi.ai/) | Voice‑to‑text agent for client onboarding (Module 3) | 30 minutes free per month, 5 API calls/month | Pro: $9/month (30 h free, 100 API calls) | Upgrade when you need >30 h of transcription or >100 calls/month. |
| [**ElevenLabs**](https://elevenlabs.io/) | Text‑to‑speech for AI‑generated audio newsletters (Module 3) | 10 k characters/month, 10 languages | Starter: $16/month (100 k characters, 20 languages) | When you exceed 10 k characters or need higher‑quality voices. |
| **Beehiiv** | AI newsletter platform & distribution (Modules 3–5) | 200 subscribers, 5 emails/month | Pro: $10/month (500 subscribers, 25 emails/month) | Upgrade when subscribers >500 or you need advanced analytics. |
| **Mailchimp** | Audience management & email automation (Modules 3, 5) | Free: 2,000 contacts, 10 k sends/month | Essentials: $13/month (5 k contacts, 20 k sends) | Upgrade when contacts >5 k or you need custom branding. |
| **Apollo.io** | Lead generation & contact enrichment (Modules 5, 10) | Free: 200 contacts/day, 5 contacts per search | Professional: $99/month (2,000 contacts/day, unlimited searches) | Upgrade when you need >200 contacts/day or advanced filters. |
| **Klaviyo** | Nurture email sequences & segmentation (Module 5) | Free: 250 contacts, 500 emails/month | Growth: $30/month (5 k contacts, 3 k emails) | Upgrade when contacts >5 k or you need custom templates. |
| **Zapier** | Bridge between Beehiiv, Mailchimp, Calendly, etc. (Modules 3, 5) | Free: 100 tasks/month, single‑step Zaps | Starter: $19.99/month (750 tasks, multi‑step Zaps) | Upgrade when tasks >500/month or you need multi‑step logic. |
| **Replit** | Host and run AI newsletter code (Modules 4, 6) | Free: 500 MB storage, 1 GB RAM, 1 CPU | Pro: $7/month (2 GB storage, 4 GB RAM, 2 CPUs) | Upgrade when code size >500 MB or you need more RAM for large models. |
| **Shopify** | Subscription tiers & high‑ticket packages (Module 8) | Free trial 14 days | Basic: $39/month (up to 100 products, 1 staff account) | Upgrade when you need >100 products or additional staff accounts. |
| **Stripe** | Automated billing & proposals (Module 9) | Free: 0.5 % + $0.05 per successful charge | Standard: 0.8 % + $0.30 per charge (no monthly fee) | Upgrade to Standard when transaction volume >10 k/month for lower fee. |
| [**Semrush**](https://www.semrush.com/) | SEO & competitor research (Modules 2, 10) | Free: 10 searches/month, 1 keyword position | Pro: $119.95/month

# APPENDIX B: THE COMPLETE SOP INDEX

| SOP # | Procedure | Category | Difficulty | Est. Time |
|-------|-----------|----------|------------|----------|
| 1.1 | Register Domain | Foundation | Easy | 30 min |
| 1.2 | Set Up Workspace | Foundation | Easy | 20 min |
| 1.3 | Create Business Accounts | Foundation | Easy | 30 min |
| 2.1 | Connect ChatGPT API | Tech Stack | Medium | 45 min |
| 2.2 | Build Make.com Scenario | Tech Stack | Medium | 60 min |
| 2.3 | Configure Voice Agent | Tech Stack | Hard | 60 min |
| 4.1 | Build Core Product | First Build | Hard | 2 hrs |
| 5.1 | Build Landing Page | Client Acquisition | Medium | 1 hr |
| 7.1 | Hire Contractor | Scaling | Medium | 45 min |
| 10.1 | Configure Demo Scheduling | Launch Plan | Easy | 30 min |


# APPENDIX C: THE REVENUE CALCULATOR  

**Purpose:** This appendix gives you a rigorous, step‑by‑step method to forecast revenue, set pricing, and determine when your AI‑newsletter workflow business will break‑even.  Follow the numbers exactly; they are the backbone of your financial strategy.  

## 1. Assumptions & Baseline Numbers  

| Item | Value | Source |
|------|-------|--------|
| **Initial Client Acquisition** | 5 clients in Month 1 | Module 5 |
| **Client Growth Rate** | +25 % MoM (organic + paid) | Module 5 |
| **Average Monthly Fee per Client** | $2,500 | Pricing Tier “Pro” |
| **Hostinger Domain Renewal** | $3.95 per year | Module 1 |
| **Beehiiv Basic (free)** | $0 | Module 3 |
| **Mailchimp Standard** | $20/month | Module 3 |
| **Make.com Standard** | $49/month | Module 2 |
| **Replit Free Tier** | $0 | Module 4 |
| **ElevenLabs TTS (Starter)** | $19/month | Module 2 |
| **Misc. (Slack, Notion, etc.)** | $10/month | Module 2 |
| **Contractor Onboarding (Upwork)** | $300/month per contractor | Module 7 |
| **Annual Revenue Growth** | 30 % YoY | Module 5 |
| **Tax Rate** | 30 % | Local tax authority |
| **Churn Rate** | 5 % per month | Industry benchmark |

### 1.1 Calculating Monthly Client Count  

| Month | Clients (starting) | Growth | Attrition | Net New | Total |
|-------|--------------------|--------|-----------|---------|-------|
| 1 | 5 | +25 % → 1.25 → 1 (round up) | 0 | 1 | 6 |
| 2 | 6 | +25 % → 1.5 → 2 | 0 | 2 | 8 |
| 3 | 8 | +25 % → 2 | 0 | 2 | 10 |
| 4 | 10 | +25 % → 2.5 → 3 | 0 | 3 | 13 |
| 5 | 13 | +25 % → 3.25 → 4 | 0 | 4 | 17 |
| 6 | 17 | +25 % → 4.25 → 5 | 0 | 5 | 22 |
| 7 | 22 | +25 % → 5.5 → 6 | 0 | 6 | 28 |
| 8 | 28 | +25 % → 7 | 0 | 7 | 35 |
| 9 | 35 | +25 % → 8.75 → 9 | 0 | 9 | 44 |
| 10 | 44 | +25 % → 11 | 0 | 11 | 55 |
| 11 | 55 | +25 % → 13.75 → 14 | 0 | 14 | 69 |
| 12 | 69 | +25 % → 17.25 → 18 | 0 | 18 | 87 |

*If you do not see the “Net New” column after Month 3, verify your growth formula in Notion formula: `round_up(previous_clients * 1.25)`.*

## 2. Revenue Projections  

| Month | Clients | Gross Revenue | Expenses | Profit | Net Profit | Cumulative Profit |
|-------|---------|---------------|----------|--------|------------|-------------------|
| 1 | 6 | $15,000 | $1,100 | $13,900 | $9,630 | $9,630 |
| 2 | 8 | $20,000 | $1,200 | $18,800 | $13,040 | $22,670 |
| 3 | 10 | $25,000 | $1,300 | $23,700 | $16,410 | $39,080 |
| 4 | 13 | $32,500 | $1,400 | $31,100 | $21,470 | $60,550 |
| 5 | 17 | $42,500 | $1,500 | $41,000 | $28,350 | $88,900 |
| 6 | 22 | $55,000 | $1,800 | $53,200 | $36,840 | $125,740 |
| 7 | 28 | $70,000 | $2,200 | $67,800 | $47,220 | $172,960 |
| 8 | 35 | $87,500 | $2,600 | $84,900 | $59,190 | $232,150 |
| 9 | 44 | $110,000 | $3,000 | $107,000 | $74,720 | $306,870 |
| 10 | 55

For the free step-by-step guide, see our [implementation guide]({< ref "/intelligence/build-an-ai-seo-optimization-service-with-semrush-the-complete-step-by-step-guid.md" >}).


## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Beehiiv](https://beehiiv.com/)** — Newsletter platform — grow and monetize your email list
- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
