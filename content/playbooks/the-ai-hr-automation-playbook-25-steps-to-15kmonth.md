---
title: "The AI HR Automation Playbook: 25 Steps to $15K/Month"
date: 2026-10-17
category: "Playbook"
price: "₦25,000"
readTime: "76 MIN"
excerpt: "The AI HR Automation Playbook: 25 Steps to $15K/Month This is an operating system, not a blog post or guide. In 25 procedures. 10 modules. 12+ hours of reading and execution. you will master the art of building, scaling, and monetizing AI‑driven recr..."
image: "/images/articles/playbooks/the-ai-hr-automation-playbook-25-steps-to-15kmonth.png"
heroImage: "/images/heroes/playbooks/design-build-and-deploy-ai-hrrecruitment-automation-workflows-with-zapier-and-in.png"
relatedOpportunity: "/opportunities/how-to-build-an-ai-hr-automation-agency-9k-15kmonth/"
relatedGuide: "/intelligence/build-an-ai-voice-agent-system-with-vapi-the-complete-step-by-step-guide/"
---
**The AI HR Automation Playbook: 25 Steps to $15K/Month**  
This is an operating system, not a blog post or guide. In **25 procedures. 10 modules. 12+ hours of reading and execution.** you will master the art of building, scaling, and monetizing AI‑driven recruitment workflows that integrate Zapier, Indeed, and LinkedIn. By following every procedure, you will launch a fully automated HR agency capable of generating $15,000/month in recurring revenue while freeing your clients from manual candidate triage. Every module is a ready‑to‑execute SOP, complete with JSON templates, Zapier flowcharts, and revenue calculators that show exactly how many clients and placements are needed to hit target profits. You will also learn how to monetize your workflows with tiered service packages, upsell AI interview bots, and automate follow‑up sequences in Klaviyo and ActiveCampaign. This playbook extends our free implementation guide with complete procedures, SOPs, and revenue calculators. For the free step‑by‑step guide, see our [implementation guide]({< ref "/intelligence/build-a-voice-agent-system-with-vapi-the-complete-step-by-step-guide.md" >}).

---

# MODULE 1: FOUNDATION

## Overview

The Foundation module is the bedrock of your AI‑powered HR and recruitment automation business. In the first 60‑minute sprint, you will create a fully functional digital storefront that can accept inquiries, route candidate data, and launch automated workflows. This foundational layer lets you focus on higher‑value value‑creation tasks later, instead of wrestling with broken integrations or incomplete infrastructure. Skipping this module means your clients will see broken email sequences, untracked leads, and a domain that no longer resolves — all of which erode trust before the first deal closes.

During this module you will:
1. Register a legally compliant business entity and secure the domain that will host your service portal.  
2. Deploy a low‑cost hosting plan on Hostinger, set up SSL, and integrate a professional email address via Zoho or Gmail.  
3. Install Notion as the project hub, Calendar, and Zapier as the glue that will trigger your AI‑driven workflows.  
4. Create a basic landing page in Canva and connect it to a Zapier webhook that captures leads into a Mailchimp list.  

You will be guided step‑by‑step through each tool’s UI, with explicit button names, URLs, and expected JSON payloads. By the end of this module you will have a live, secure domain, a functional email system, and a Zapier‑powered funnel that is ready to be expanded in the next modules.

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| Hostinger | Domain registration & web hosting | 1‑month free trial, $1.39/mo for 1‑year | $2.91/mo for 1‑year plan |
| Notion | Project management & documentation hub | Unlimited, free | $8/user/month (Pro) |
| Zapier | Automate HR workflow triggers | 5 Zaps, 100 tasks/month | $19.90/month (Starter) |
| Calendly | Client booking & lead capture | 1 user, 1 event type | $10/user/month (Professional) |
| Canva | Landing‑page & asset design | Unlimited access, limited templates | $12.95/user/month (Pro) |
| Grammarly | Writing & editing tool | Unlimited usage | $12/month (Premium) |
| Mailchimp | Email list capture & autoresponder | 2,000 contacts, 10K sends | $10/month (Essentials) |

**Estimated Time to Complete:** 4 – 5 hours (including account creation, basic configuration, and testing).

---

## Procedure 1.1: REGISTER YOUR BUSINESS DOMAIN ON HOSTINGER

1. **Open your preferred browser** (Chrome, Edge, or Safari) and navigate to the Hostinger domain search page:  
   `https://www.hostinger.com/domains`.  
   *Expected result:* The Hostinger landing page loads with a prominent domain search bar at the top.

2. **Click the “Register” button** located under the search bar.  
   *Expected result:* A new window opens titled “Create an Account” with email, password, and confirm password fields.

3. **Fill in the account fields** exactly as follows:  
   - **Email:** `yourname@example.com` (use a real, active email)  
   - **Password:** `StrongPass!123` (must be at least 8 characters, 1 uppercase, 1 number, 1 special character)  
   - **Confirm Password:** `StrongPass!123`  
   Click the **“Create account”** button.  
   *Expected result:* A confirmation page asking you to verify your email.

4. **Check your inbox** for a verification email from Hostinger. Open the

---

## Procedure 1.2: Set Up Email and Workspace in Notion

1. **Open a browser** and navigate to the Notion free‑tier sign‑up page:  
   https://www.notion.so/signup  
   *If you have an existing Notion account, skip to step 5.*

2. **Click the button labeled **_Sign up with Google_**.  
   *You will be redirected to the Google OAuth page.*

3. **Enter your Gmail address** in the field that says _"Email or phone"_, then click **_Next_**.  
   *Expected output:* Google login screen.

4. **Enter your Gmail password** in the field labeled _"Enter your password"_, then click **_Next_**.  
   *Expected output:* A prompt asking to allow Notion access to your Google account.  

   **Do you see the permission screen with the list of scopes?**  
   If not, double‑check that you entered the correct Gmail address and password.  

5. **Click the button labeled **_Allow_** to give Notion permission to read your Google account.**  
   *Expected result:* You are redirected to the Notion onboarding wizard.

6. **Select the option **_Start from scratch_** on the first onboarding screen, then click **_Continue_**.  
   *Expected output:* Blank workspace page with a sidebar.

7. **Rename your workspace**: click the dropdown in the top‑left corner that shows **_Workspace Name_**, type **_HR‑Automation Hub_**, then press **Enter**.  
   *Expected result:* Workspace name updates in the sidebar header.

8. **Add a team member**: In the sidebar, click **_Add member_** (bolded button).  
   *Expected output:* Modal window to invite by email.  

   **Do you see the invite modal?**  
   If not, click the **_⋮_** icon next to the workspace name and select **_Settings & Members > Members_**.

9. **Enter the email address** of the person you want to invite (e.g., `team@hrautomation.com`).  
   Click **_Invite_**.  
   *Expected output:* Confirmation toast “Sent invitation to team@hrautomation.com”.

10. **Create your first database**:  
    a. In the left sidebar, click **_Add a page_** (bolded).  
    b. In the modal, type **_Candidate Tracker_** and press **Enter**.  
    c. On the new page, click **_Table – Full page_** (bolded).  

    *Expected output:* A new table with columns `Name`, `Email`, `Phone`, `Position`.

11. **Add a new column** for “Application Source”:  
    a. Hover over the column header `Position`, click the **_⋮_** icon, and choose **_Add a property_**.  
    b. Name it **_Source_**, select the type **_Select_**, then click **_Create_**.  
    *Expected output:* New column appears with a dropdown icon.

12. **Populate your first row** with sample data:  
    a. Click the first empty row.  
    b. Enter `John Doe` in **Name**, `johndoe@example.com` in **Email**, `555‑123‑4567` in **Phone**, `Software Engineer` in **Position**, and `Indeed` in **Source**.  
    *Expected output:* Row fully populated.

13. **Share the database with external clients**:  
    a. Click the **_Share_** button in the top‑right corner.  
    b. Toggle **_Share to the web_** on.  
    c. Click **_Copy link_**.  

    **Do you see the share modal with the toggle turned on?**  
    If not, ensure you are on the page’s top‑right corner, not the sidebar.

14. **Set up your email forwarding rule in Gmail** to catch applicant emails:  
    a. Go to Gmail settings: https://mail.google.com/mail/u/0/#settings/filters.  
    b. Click **_Create a new filter_** (bolded).  
    c. In the “From” field, enter `*@indeed.com`.  
    d. Click **_Create filter_**.  
    e. Check **_Forward it to_** and choose the email address you use for Notion (e.g., `hrautomation@notion.com`).  

    *Expected output:* Filter listed in your Gmail filters.

15. **Create a Zapier integration to auto‑add candidates to Notion**:  
    a. Visit https://zapier.com/app/dashboard and click **_Make a Zap_**.  
    b. Set the trigger app to **_Gmail_** and trigger event to **_New Email Matching Search_**.  
    c. Connect your Gmail account and test the trigger.  
    d. Set the action app to **_Notion_**, action event **_Create Database Item_**, and connect your Notion account.  
    e. Map Gmail fields:  
       - `From` → `Candidate Tracker → Email`  
       - `Subject` → `Candidate Tracker → Name`  
       - `Body` → `Candidate Tracker → Position`  
       - `Custom` → `Candidate Tracker → Source` (set to “Indeed”).  
    f. Turn the Zap **on**.  

    *Expected output:* Zap status shows

---

## Procedure 1.3: CREATE CORE BUSINESS ACCOUNTS AND CALENDLY

**Objective**  
Set up verified business accounts on the core platforms—Calendly, Zapier, and Notion—so you have a single source of truth for scheduling, automation, and project tracking. Each step includes exact URLs, button names, field values, interactive checkpoints, expected outputs, and error‑handling instructions.

---

### 1. Sign Up for Calendly (Free Plan)

1. Open **Google Chrome**.  
2. Go to **https://calendly.com**.  
3. Click the **SIGN UP FREE** button in the top‑right corner.  
4. In the **Create your Calendly account** form, fill in:  
   - **Email**: `yourname@yourbusiness.com`  
   - **Password**: a secure 12‑character password (e.g., `S3cur3!Passw0rd`)  
   - **Company Name**: `YourBusiness Inc.`  
5. Click **CREATE ACCOUNT**.  

**Check‑in**  
Do you see the “Your calendar is ready” confirmation banner?  
*If not, verify that your email domain is correctly entered and click **CONTINUE** again.*  

6. Calendly will send a verification email.  
7. Open your inbox, locate the email from “Calendly”, click **VERIFY EMAIL**.  

**Expected output**  
You should land on the Calendly dashboard with a default “One‑on‑One” event type already created.  

---

### 2. Create a Calendly Event Type for Initial Interviews

8. On the dashboard, click the **+ NEW EVENT TYPE** button on the top‑right.  
9. Select **One‑on‑One**.  
10. In the **Event type name** field, type **“Initial Interview”**.  
11. Set **Location** to **“Zoom”** (Calendly will auto‑create a Zoom link).  
12. Under **Duration**, choose **30 minutes**.  
13. Click **SAVE & CLOSE**.  

**Check‑in**  
Do you see “Initial Interview” listed under your event types?  
*If not, confirm you’re on the Event Types page and click **+ NEW EVENT TYPE** again.*  

13. Click **SCHEDULE** next to the new event type to view the schedule widget.  
14. Verify the widget shows **“Available for 30‑minute interview”**.  

**Error scenario**  
If you see **“Location options are unavailable”**, it means your Calendly account is still on the free plan which only supports “Zoom” if integrated.  
*Fix it by going to **Calendly Settings → Integrations → Zoom** and clicking **CONNECT**. Use your Zoom credentials. If Zoom integration is not available, upgrade to the Pro plan via **Billing → Upgrade**.*

---

### 3. Sign Up for Zapier (Free Plan)

15. In a new tab, visit **https://zapier.com**.  
16. Click **SIGN UP** in the top‑right corner.  
17. Fill in:  
    - **Email**: `yourname@yourbusiness.com`  
    - **Password**: same as used for Calendly  
    - **Full name**: `Your Name`  
18. Click **CREATE ACCOUNT**.  

**Check‑in**  
Do you see the “Welcome to Zapier” onboarding screen?  
*If not, ensure you’re not logged in on a different account; sign out and try again.*  

19. Zapier will email a verification link.  
20. Click the link in your inbox.  

**Expected output**  
You should land on the Zapier dashboard with a button **“Make a Zap”**.  

---

### 4. Create a Basic Zap: Calendly → Notion

21. Click **MAKE A ZAP**.  
22. In the **Trigger** search box, type **Calendly** and select it.  
23. Choose the **Trigger event** **“Invitee Created”**.  
24. Click **Continue**.  

**Check‑in**  
Do you see the **“Connect Calendly account”** screen?  
*If not, your Calendly integration may be blocked by a pop‑up blocker. Disable it and try again.*  

25. Click **+ CONNECT A NEW ACCOUNT**.  
26. In the pop‑up, paste your Calendly API key (found under **Calendly Settings → Integrations → API & Webhooks → Generate New API Key**).  
27. Click **ALLOW**.  
28. Back on Zapier, click **Test Trigger**.  
29. Zapier will pull a recent invitee. Click **Continue**.  

### 5. Set Up Notion Integration

30. In the **Action** step, search for [**Notion**](https://notion.so/) and select it.  
31. Choose **“Create Database Item”** as the action event.  
32. Click **Continue**.

## Check-In: Module 1 Complete

- [ ] REGISTER YOUR BUSINESS DOMAIN ON HOSTINGER completed and verified
- [ ] Set Up Email and Workspace in Notion completed and verified
- [ ] CREATE CORE BUSINESS ACCOUNTS AND CALENDLY completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 2: TECH STACK

## Overview

This module is the backbone of your AI‑powered HR automation service. It walks you through the exact tools, credentials, and API connections required to launch end‑to‑end workflows that source candidates, screen resumes, and sync data between Indeed and your internal systems. Skipping this step will leave you with broken pipelines, data loss, and unhappy clients—your entire service collapses if the data never flows correctly.

You will learn to:
1. Register and secure API keys for every platform (Zapier, Indeed, Make.com, etc.).
2. Map out the data flow diagram that shows how applicant data moves across services.
3. Test each connection in isolation before wiring them together, ensuring every trigger and action behaves as expected.

If you skip or rush this module, your later operations will suffer: duplicate hires, missed deadlines, and a reputation for unreliability. The precision of a well‑configured tech stack is the single most important lever for scaling your AI recruitment service.

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| Zapier | Workflow automation between Indeed and internal tools | 5 Zaps, 100 tasks/month | Starter $19.99/mo (unlimited Zaps, 750 tasks) |
| Indeed | Job posting & applicant sourcing | API limited to 1,000 requests/day | Enterprise API $149/mo |
| Make.com | Advanced integration logic & conditional branching | 100 operations/month | Basic $9/mo (2,500 ops) |
| Replit | Code sandbox for custom Python scripts | Unlimited public projects | Hacker $7/mo (private projects) |
| Vapi | Voice‑to‑text transcription for candidate interviews | 10,000 chars/Month | Pro $9/mo (unlimited) |
| ChatGPT | Candidate chat assistant & resume parsing | 3,000 tokens/day | Plus $20/mo (unlimited) |
| Notion | Central knowledge base & workflow documentation | Unlimited pages | Personal Pro $4/mo (enhanced) |

**Estimated time to complete:** 3 hours (includes key‑generation, connection testing, and validation).

---

## Procedure 2.1: Connect ChatGPT API and Store Keys in Notion

1. **Open the OpenAI API Key page**  
   - URL: `https://platform.openai.com/api-keys`  
   - Log in with your OpenAI credentials.  
   - Click the **Create new secret key** button in the top‑right corner.  
   - Copy the displayed key to your clipboard.  
   - *Do you see the new key displayed? If not, refresh the page or log in again.*

2. **Create a new Notion integration**  
   - Navigate to `https://www.notion.so/my-integrations`.  
   - Click **+ New integration**.  
   - Name the integration **ChatGPT‑API‑Key**.  
   - Under **Capabilities**, check only **Read content** and **Insert content**.  
   - Under **Environment**, leave **Development** selected.  
   - Click **Submit**.  
   - Copy the **Internal Integration Token** shown on the next screen.  
   - *Do you see the token displayed? If not, ensure you have not exceeded the free integration limit (5 per workspace).*

3. **Create a Notion database for API keys**  
   - Open your workspace home page.  
   - Click **+ New page** → **Table – Full page**.  
   - Name the page **API Keys**.  
   - Add a property named **Service** (Select).  
   - Add a property named **API Key** (Text).  
   - Add a property named **Created At** (Date).  
   - Click **+ Add a row**.  
   - In **Service**, type `ChatGPT`.  
   - In **API Key**, paste the key you copied in step 1.  
   - In **Created At**, set the current date.  
   - Click **Share** → **Invite** → paste the integration name **ChatGPT‑API‑Key** → **Invite**.  
   - *Do you see the new row with your key? If not, check that the integration has the correct permissions.*

4. **Verify Notion integration access**  
   - In the same database, click the three dots in the top‑right corner → **Properties** → **Advanced** → **Internal ID**.  
   - Note the **Database ID** (e.g., `c3f9d2a1b4e842e5a3f7e8b9c4d6f7a8`).  
   - Open a browser console and run:  
     ```javascript
     fetch('https://api.notion.com/v1/databases/c3f9d2a1b4e842e5a3f7e8b9c4d6f7a8', {
       headers: {
         'Authorization': 'Bearer <Internal Integration Token>',
         'Notion-Version': '2024-04-27'
       }
     }).then(r => r.json()).then(console.log)
     ```  
   - Expected output: JSON object containing the database schema.  
   - *Do you see a JSON response? If you see `invalid_token`, this means the token is incorrect. Fix it by re‑copying the token from step 2.*

5. **Create a Replit project for key management**  
   - Visit `https://replit.com/` and sign in.  
   - Click **+ New Repl** → language **Python** → name **ChatGPT-Key-Store**.  
   - In the `main.py` file, add:  
     ```python
     import os
     from notion_client import Client

     notion = Client(auth=os.getenv("NOTION_TOKEN"))
     database_id = os.getenv("NOTION_DATABASE_ID")

     def get_key():
         result = notion.databases.query(database_id=database_id)
         for page in result["results"]:
             if page["properties"]["Service"]["select"]["name"] == "ChatGPT":
                 return page["properties"]["API Key"]["rich_text"][0]["text"]["content"]
         return None
     ```  
   - Click **Run** to ensure Replit installs `notion-client` automatically.  
   - *Do you see the script running without errors? If you see `ModuleNotFoundError`, go to **Packages** → search `notion-client` → **Add**.*

6. **Set environment variables in Replit**  
   - Click the **Secrets** icon (lock) on the left sidebar.  
   - Add `NOTION_TOKEN` with the value from step 2.  
   - Add `NOTION_DATABASE_ID` with the value from step 4.  
   - Click **Save**.  
   - *Do you see the

---

**Procedure 2.2** — Generation failed due to AI backend unavailability. Please retry later.

---

## Procedure 2.3: Configure Vapi Voice Agent and ElevenLabs TTS

1. **Open your browser** and navigate to Vapi’s sign‑up page:  
   <https://vapi.ai/signup>.  
   Click the **SIGN UP WITH GOOGLE** button.  
   Fill in the requested fields (Name, Email, Company) and click **CONTINUE**.  

2. In the Vapi dashboard, click the **CREATE VOICE AGENT** button.  
   Enter the name **“Recruitment Assistant”** in the *Agent Name* field.  
   Choose **English (US)** as the language and click **NEXT**.  

3. On the *Select Voice* screen, select **“VAPI‑VOICE‑001”** (the default female voice).  
   Click **SAVE**.  

4. **Do you see the “Training Data” tab?** If not, refresh the page or click **RELOAD DASHBOARD**.  
   Expected output: the tab should display “Training Data” beside “Settings” and “Logs”.  

5. Click the **Training Data** tab and then **UPLOAD SAMPLE QUESTIONS**.  
   Upload the following CSV file (copy/paste the text below into a file named *questions.csv* and download):  
   ```
   Intent,Question
   HireCandidate,"Please provide details for hiring a backend developer."
   CandidateStatus,"What’s the status of Jane Doe’s application?"
   ```  
   Click **UPLOAD**.  

6. After upload, Vapi will parse the file. A confirmation banner will read *“2 intents successfully added.”*  

7. Open a new tab and go to ElevenLabs sign‑up: <https://elevenlabs.io/signup>.  
   Click **SIGN UP** and complete the wizard with your email and a password.  

8. Once logged in, click the **API** tab in the left sidebar.  
   Copy the displayed **API Key** (it starts with `eyJhbGciOiJIUzI1…`).  
   Store it in a secure note; you’ll need it later.  

9. **Do you see the “Voice Models” section?** If not, click **VOICE MODELS** in the sidebar.  
   Expected output: a list of available voice models such as “Nova” and “Elliot”.  

10. Click **Nova** and then **GENERATE SAMPLE**.  
    In the prompt box, type **“Hello, this is RecruitBot speaking.”**  
    Click **GENERATE**.  
    The audio preview should play automatically.  

11. Return to the Vapi dashboard. Click **Settings** → **Integrations**.  
    Under *Text‑to‑Speech*, toggle the switch to **ON**.  

12. In the *TTS Provider* dropdown, select [**ElevenLabs**](https://elevenlabs.io/).  
    Paste the API key you copied earlier into the *API Key* field.  
    Click **SAVE SETTINGS**.  

13. Create a Zapier account at <https://zapier.com/app/dashboard>.  
    Click **SIGN UP** with your Google credentials.  

14. In Zapier, click **MAKE A ZAP**.  
    For the trigger, search for **“Indeed Resume Search”** and select it.  
    Authenticate with your Indeed API key (found in your Indeed recruiter account under *API Access*).  

15. Set the trigger options: *Job Title = “Backend Engineer”* and *Location = “Remote”*.  
    Click **TEST & REVIEW**.  
    You should see a sample resume record in the preview pane.  

16. For the action step, search for **“Vapi Voice Agent”** and select it.  
    Authenticate using the *VAPI‑VOICE‑001* agent you created.  

17. Map the *Candidate Name* field from the Indeed trigger to the **“candidate_name”** parameter in Vapi.  
    In the *Prompt* field, enter:  
    `"Hello {candidate_name}, this is RecruitBot. We have a new opportunity for a Backend Engineer. Would you like to schedule an interview?"`  

18. Click **TEST ACTION**.  
    A phone call will be placed to the phone number you entered in the Vapi dashboard under *Contact List*.  
    You should hear the ElevenLabs TTS voice read the prompt.  

19. **Do you see the call log in Vapi?** If not, go to **Logs** → **Call History**.  
    Expected output: a record titled “Interview Invite” with status **COMPLETED**.  

20. If the call fails with **“Error 503 – Service Unavailable”**, this means the ElevenLabs TTS service is temporarily down.  
    Fix it by waiting 5 minutes and re‑running the Zap, or by switching the TTS provider in Vapi to **Google Cloud TTS** (under *Settings* → *TTS Provider*).  

### Pricing & Cost Table

| Tool | Free Tier | Paid Tier | Monthly Cost | Key Feature |
|------|-----------|-----------|--------------|-------------|
| Vapi | 10,000 minutes/month | Starter: 50,000 min | $29 | Voice Agent creation |
| ElevenLabs | 20 hrs TTS per month | Pro: 200 hrs | $20 | High‑quality AI voices |
| Zapier | 5 Zaps, 100 tasks/month | Starter: 20 Zaps | $19.99 | Workflow automation |

All prices are current as of 17 Oct 2026. Use the free tiers to test; upgrade only after confirming the workflow.

## Check-In: Module 2 Complete

- [ ] Connect ChatGPT API and Store Keys in Notion completed and verified
- [ ] Build Your First Make.com Automation Scenario completed and verified
- [ ] Configure Vapi Voice Agent and ElevenLabs TTS completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 3: FRAMEWORK

## Overview  
Module 3 is the blueprint that turns raw automation ideas into a repeatable, profitable service offering. It teaches you how to map the entire client journey—from the first discovery call to the final hand‑off of a fully‑functional AI‑powered HR stack—using a rigorously defined framework. Skipping this module leaves you with ad‑hoc scripts that produce inconsistent results, erode client trust, and make scaling impossible.  

The core of the framework is a three‑layered process: **(1) Service Definition** – crystallize what problems you solve and the exact deliverables you promise; **(2) Client Onboarding Flow** – automate intake, data capture, and contract signing so every new client starts with the same high‑quality baseline; and **(3) Quality Assurance Standards** – embed continuous monitoring, error‑handling, and performance metrics so you can guarantee uptime and ROI. By mastering these layers you create a repeatable “cookbook” that any solo entrepreneur can sell to HR departments, staffing agencies, or founders who need instant hiring pipelines.  

You will learn to leverage industry‑leading tools (Zapier, Indeed, Make.com, Notion, Replit) in a tightly choreographed sequence that eliminates manual data entry, reduces time‑to‑hire by 60‑80 %, and scales your service without needing a full‑time developer. The module is designed to be completed in **5 hours** of focused work, after which you will have a live, testable workflow that you can offer to your first client.  

| Tool      | Purpose                                               | Free Tier                                 | Paid Tier                                  |
|-----------|--------------------------------------------------------|-------------------------------------------|-------------------------------------------|
| Zapier    | Automate HR app integrations (Slack, Sheets, etc.)    | 5 zaps, 100 tasks/month                   | $19.99/month – 1000 tasks, 15‑min latency |
| Indeed    | Source candidates & post jobs                         | Free job posting                          | $120/month per sponsored job              |
| Make.com  | Alternative low‑code automation platform               | 100 operations/month                      | $9/month – 1000 operations                 |
| Notion    | Project documentation & knowledge base                 | Unlimited pages, 5 GB storage              | $4/user/month – 10 GB storage             |
| Replit    | Host and run custom script snippets                    | 500 MB storage, 50 MB RAM                 | $7/month – 2 GB storage, 1 GB RAM         |

> **Estimated time to complete**: **5 hours** of hands‑on building and testing.

---

## Procedure 3.1: Define Your Service Delivery Framework

Below is a step‑by‑step operating system for mapping out the exact workflow you will charge clients for when you automate their hiring pipeline with Zapier and Indeed. Follow the instructions verbatim; any deviation will break the automation.

---

### 1. Create a Zapier Workspace

1.1 Open your browser and go to **https://zapier.com/signup**.  
1.2 Click **SIGN UP WITH EMAIL**.  
1.3 Enter **your‑email@example.com** in the **Email** field.  
1.4 Enter a **strong password** (e.g., `P@ssw0rd2026`) in the **Password** field.  
1.5 Click **SIGN UP** (the button is **bolded** on the page).  
1.6 Confirm your email by clicking the link sent to your inbox.  

> **Expected Output**: You land on the Zapier Dashboard with the title “Welcome to Zapier” and a sidebar listing **My Zaps** and **Explore**.

> **If you see “Error: Email already in use”** this means the address is already registered. Use a different email or click **Forgot Password?** and reset.

---

### 2. Create a New Zap

2.1 On the Zapier Dashboard, click the **+ CREATE** button (top‑right, bold).  
2.2 In the popup, click **START FROM SCRATCH** (bold).  
2.3 In the search box, type **Indeed** and highlight **Indeed – New Job Application**.  
2.4 Click **Continue** (bold).

---

### 3. Connect Your Indeed Account

3.1 Click **+ CONNECT ACCOUNT** (bold).  
3.2 A new window opens titled “Authorize Indeed”.  
3.3 In the **Username** field, enter the email you use for your Indeed recruiter account.  
3.4 In the **Password** field, enter your Indeed password.  
3.5 Click **ALLOW** (bold).  
3.6 Zapier will display **“Indeed (Your‑Company‑Name)”** as the connected account.  
3.7 Click **Continue** (bold).

> **Interactive Check‑in**  
> **Do you see the “Indeed (Your‑Company‑Name)” account listed?**  
> **If not,** verify your Indeed credentials or re‑try the connection; ensure your Indeed account has “Recruiter” permissions.

---

### 4. Set Trigger Parameters

4.1 In the **Trigger** section, set **Job Post ID** to **All** (dropdown).  
4.2 Set **Application Status** to **All** (dropdown).  
4.3 Click **Continue** (bold).  
4.4 Zapier runs a test; you should see **“We found 1 new application”** in the test results.  
4.5 If you see **“No applications found”**, wait until a real candidate applies or create a dummy application via Indeed’s demo tools.  
4.6 Click **Done Editing** (bold).

> **Do you see “We found 1 new application”** in the test results?  
> **If not,** confirm that your Indeed job posting is live and has at least one application.

---

### 5. Add a Filter (Optional)

5.1 Click **+ ADD** next to the trigger in the Zap editor.  
5.2 Select **Filter by Zapier** (bold).  
5.3 Set **Only continue if…**:  
- **Field:** `Application Status`  
- **Condition:** `Exactly matches`  
- **Value:** `New`  
5.4 Click **Continue** (bold).  
5.5 Zapier shows a test; you should see **“Filter passed”**.  
5.6 Click **Done Editing** (bold).

---

### 6. Create

---

**Procedure 3.2** — Generation failed due to AI backend unavailability. Please retry later.

## Check-In: Module 3 Complete

- [ ] Define Your Service Delivery Framework completed and verified
- [ ] Streamline Client Onboarding Flow completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 4: FIRST BUILD

## Overview  
In MODULE 4 you will **design, build, and deploy the first AI‑driven HR and recruitment workflow** that you can hand over to a real client. This is the “show‑off” deliverable that proves your entire system works end‑to‑end—from pulling candidate data from Indeed, to enriching resumes with AI, to automatically emailing personalized follow‑ups and logging every interaction in a CRM. You’ll start with a raw data set, set up the data pipeline, apply natural‑language processing, and finally wire everything into a Zapier automation that runs on a schedule or on a trigger. By the end of this module you will have a fully functional, repeatable workflow that you can present to a client as a tangible proof of concept.

Why this matters: In the AI‑HR marketplace, the first tangible product is the biggest differentiator. Clients will evaluate your capability based on a real, working demo, not a white‑paper. The workflow you build here will also serve as the foundation for all future services—scaling it to different industries, adding more AI features, or turning it into a subscription product. Skipping this module means you’ll lack a working prototype, lose credibility with potential clients, and miss out on the early‑stage revenue that comes from selling a finished, deployable workflow.

If you skip this module, you will be ill‑prepared to answer the most common client questions: “Can you deliver a working system?” and “How quickly can you deploy?” Your pitch deck will feel theoretical, and you’ll likely lose early deals. Moreover, you’ll miss the critical learning loop of debugging live data, handling API rate limits, and optimizing workflow efficiency—all key skills that only surface during actual build and deployment.

| Tool          | Purpose                                                  | Free Tier                         | Paid Tier (per month)      |
|---------------|----------------------------------------------------------|-----------------------------------|---------------------------|
| Zapier        | Orchestrate actions between Indeed, Gmail, Notion        | 100 tasks, 5 Zaps                 | Starter: $19.99 (unlimited tasks, 20 Zaps) |
| Indeed API    | Pull candidate listings and detailed job info           | None (requires API key)           | $0.05 per API call (paid key) |
| Make.com      | Alternative to Zapier for complex multi‑step logic      | 3,000 operations, 15 min delay    | Creator: $15 (unlimited ops, 1 min delay) |
| Replit        | Run Python scripts that scrape, parse, and enrich data   | Unlimited public projects         | Hacker: $7 (private projects, GPU) |
| Notion        | Store candidate data, workflow logs, and documentation  | Unlimited pages, 1,000 blocks     | Personal Pro: $4 (unlimited blocks) |
| Grammarly     | Proofread workflow emails and documentation             | 20,000 characters/month          | Premium: $12 (unlimited) |
| Canva         | Design visual email templates and résumé summaries      | 5GB storage, 1 editor             | Pro: $12.99 (unlimited) |

**Estimated time to complete:** 3 – 4 hours (including data prep, scripting, Zapier setup, and testing).

---

## Procedure 4.1: Build the Core AI Product in Replit

**Objective:** Deploy a minimal viable AI‑powered recruitment workflow on Replit that receives candidate data from Zapier, enriches it with Indeed API calls, and stores results in a simple JSON database. The workflow will later be wrapped in a Zapier “trigger” for client use.

> **Tool stack**  
> • Replit (Python, free tier $0, paid Hacker plan $7/month)  
> • Zapier (free tier 100 tasks/month, Starter $19.99/month)  
> • Indeed API (free up to 1,000 requests/month)  
> • OpenAI API (GPT‑3.5, $0.02/1k tokens)  
> • Vapi (optional voice layer, free tier 10 minutes/day)  

---

### 1. Create a Replit Account
1. Open your browser and go to **https://replit.com**.  
2. Click **Sign up** in the top‑right corner.  
3. Enter **your email**, set a **password** (≥ 12 characters), and click **SIGN UP**.  
4. Verify your email via the link sent from Replit.  

**Check‑in**: Do you see the “Your Repls” dashboard with a “Create” button? If not, refresh or try a different browser.

### 2. Create a New Repl Project
1. From the dashboard, click **Create** → **New Repl**.  
2. In the “Language” dropdown, select **Python**.  
3. Name the Repl **ai-hire-workflow**.  
4. Click **Create Repl**.  

**Expected output**: A new Repl opens with a default `main.py` and a **Packages** tab on the left.  

### 3. Import a

---

## Procedure 4.2: CREATE THE DATA PROCESSING PIPELINE WITH MAKE.COM

1. **Open a web browser** and go to **https://www.make.com/**.  
   - If you do not have an account, click **Sign Up** in the top‑right corner, choose the **Free Plan** (200 operations/month), and complete the email verification.

2. In the Make.com dashboard, click the **Create a new scenario** button (top‑center, **+ New scenario**).  
   - The **Scenario Overview** screen appears with a blank canvas.

3. Search for the **HTTP** module in the left panel, drag it onto the canvas, and double‑click it to configure.  
   - Set the **Method** to **GET**.  
   - For **URL**, type `https://api.indeed.com/ads/apisearch?publisher=YOUR_PUBLISHER_ID&format=json&q=software+developer&l=remote&sort=date&radius=25&st=software+developer&jt=fulltime&limit=50`.  
   - Replace **YOUR_PUBLISHER_ID** with your Indeed publisher ID (obtainable from the Indeed API portal).  
   - Under **Headers**, add **Key**: `User-Agent`, **Value**: `Make.com Integration`.  
   - Click **Save**.

4. **Do you see the “HTTP Request” module with the URL and headers you just entered?**  
   - If not, double‑click the module again and verify each field.  
   - **Expected output**: a green checkmark next to the module and a preview pane showing “Request URL: …”.

5. Click the **Run once** button in the top‑right to test the request.  
   - A modal will display the raw JSON response from Indeed.  
   - **Do you see the JSON payload?** If you see an error `Error 401: Unauthorized`, it means your publisher ID is wrong.  
   - **Fix**: Go to the Indeed API portal, regenerate the publisher ID, and paste it into the URL again.

6. Drag a **JSON > Parse JSON** module onto the canvas, connect it to the HTTP module’s output.  
   - In the **JSON** field, paste the entire JSON preview from step 5.  
   - Click **Parse**.  
   - The module now exposes individual fields such as `results`, `totalResults`, etc.

7. Click the **Filter** module (under “Tools”) and connect it to the JSON module.  
   - Set the **Condition** to `results->[0]->jobtitle contains "Senior"`.  
   - This will pass only postings that mention “Senior” in the job title.

8. **Do you see the Filter module showing “Condition: jobtitle contains Senior”?**  
   - If the condition appears incorrect, re‑select the `jobtitle` field from the JSON list.

9. Drag a **Notion** module onto the canvas, connect it after the Filter.  
   - Click **Add Connection** → **Connect** to Notion.  
   - Follow the OAuth prompt: grant access to your Notion workspace.  
   - In the module, choose **Create a database item**.  
   - **Database ID**: paste the ID from the URL of your target Notion database (e.g., `https://www.notion.com/.../database/xxxxxxxxxxxxxxxx`).  
   - Map fields:  
     - `Title` → `results->[0]->jobtitle`  
     - `Company` → `results->[0]->company`  
     - `Location` → `results->[0]->formattedLocation`  
     - `Summary` → `results->[0]->snippet`  
     - `URL` → `results->[0]->url`.  
   - Click **Save**.



---

## Procedure 4.3: Deploy and Test the Complete AI HR Workflow

1. **Open your web browser** and navigate to the Zapier editor: <https://zapier.com/app/editor>.  
   *If you are not already logged in, you’ll be prompted to log in with your email and password. Use the credentials you created during onboarding.*  

2. Click the **Create Zap** button located in the upper‑right corner of the editor.  
   *The screen will change to the Trigger setup page, displaying “Choose a trigger app.”*  

3. In the search bar, type **Indeed** and select the “Indeed” app from the drop‑down list.  
   *Choose the trigger event “New Job Application” and click **Continue**.*  

4. Click **Sign in to Indeed**.  
   *A new window will open asking for your Indeed API key. Paste your API key into the “API Key” field and click **Continue**.*  
   **Do you see “Connection Successful” displayed in green?** If not, check that your API key matches the one provided in your Indeed account dashboard.  

5. **Test Trigger** by clicking the **Test Trigger** button.  
   *Zapier will pull the most recent application data. You should see a JSON preview that includes fields such as “applicant_name,” “email,” “resume_link,” and “job_id.”*  

6. Click **Continue** to proceed to the Action step.  

7. In the Action app search bar, type **Notion** and select the “Notion” app.  
   *Choose the action event “Create Database Item” and click **Continue**.*  

8. Connect your Notion account by clicking **Sign in to Notion**.  
   *Authorize Zapier to access your workspace. Once authorized, you’ll see “Connection Successful.”*  

9. Under **Set up action**, select the target database “Recruitment Pipeline.”  
   *Map the fields: “applicant_name” → “Name,” “email” → “Email,” “resume_link” → “Resume URL,” “job_id” → “Job ID.”*  

10. Click **Continue** and then **Test Action**.  
    *The screen will show “Action succeeded” with a preview of the created database item. Verify that the item appears correctly in your Notion database.*  

11. **Name your Zap** “HR‑Auto‑Applicant‑Ingest” and toggle the switch to **ON**.  
    *You should see a green banner: “Zap is Live.”*  

12

## Check-In: Module 4 Complete

- [ ] Build the Core AI Product in Replit completed and verified
- [ ] CREATE THE DATA PROCESSING PIPELINE WITH MAKE.COM completed and verified
- [ ] Deploy and Test the Complete AI HR Workflow completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 5: CLIENT ACQUISITION

## Overview  
In this module you will learn how to attract, convert, and onboard paying clients for your AI‑driven HR and recruitment automation service. We start by mapping the entire client acquisition funnel—from initial outreach to closing the first deal—so that you can replicate high‑value leads at scale. Each step is anchored in proven automation: use Zapier to connect job boards, CRM, and email sequences, while Indeed’s API pulls candidate data into your workflow. If you skip this module, you risk building an impressive product that no one knows about, wasting time and capital on a product that fails to generate revenue.

You will also create a high‑converting landing page, set up LinkedIn and Indeed outreach templates, and build a lead‑generation pipeline that feeds directly into your CRM. By the end, you will have a repeatable system that turns cold prospects into paying customers in under 48 hours. The playbook’s instructions are actionable and ready‑to‑execute, with check‑ins and error handling built in, so you won’t be left guessing at any point.

| Tool          | Purpose                                           | Free Tier                                 | Paid Tier (Monthly) |
|---------------|---------------------------------------------------|-------------------------------------------|---------------------|
| Zapier        | Automate triggers between HR tools and CRM        | 100 tasks/month, 5 Zaps                   | $19.99 (Starter)    |
| Indeed API    | Pull job listings and candidate data             | 1,000 requests/month                      | $99.00 (Pro)        |
| HubSpot CRM   | Store leads, track outreach, and automate emails | Free (unlimited contacts)                | $45.00 (Starter)    |
| Canva         | Design landing page graphics and social posts    | Unlimited free features                   | $12.99 (Pro)        |
| Mailchimp     | Email outreach and automation                    | 2,000 contacts, 12,000 emails/month      | $9.99 (Essentials)  |
| Calendly      | Schedule discovery calls                          | 1 calendar, 30 days of scheduling         | $12.00 (Pro)        |
| LinkedIn Sales Navigator | Target prospects by industry and role | 0 (requires paid LinkedIn)                | $79.00 (Pro)         |

**Estimated time to complete:** 3 hours (including landing page setup, Zapier workflow creation, and outreach template crafting).

---

## Procedure 5.1: Build a High‑Conversion Landing Page on Shopify

1. **Create a Shopify Store**  
   - Open a browser and go to **https://www.shopify.com**.  
   - Click **START FREE TRIAL** (top‑right).  
   - Fill in the form:  
     - **Email**: your email address  
     - **Password**: `Shopify!2026` (exactly that string)  
     - **Store name**: `HR‑Automation‑Hub`  
   - Click **Create store** (bold).  
   - **Do you see the “Welcome to your Shopify admin” dashboard?** If not, reload the page and ensure cookies are enabled.  

2. **Add a Domain**  
   - In the Admin, go to **Online Store > Domains**.  
   - Click **Buy new domain** (bold).  
   - Search for `hrautomationhub.com`.  
   - Click **Add domain** (bold).  
   - Follow the onscreen instructions to purchase for **$14.00**.  
   - **Do you see the domain listed as “Connected” in the Domains panel?** If it shows “Pending DNS Verification”, wait 5 minutes and refresh.  

3. **Choose a Theme**  
   - From the Admin, go to **Online Store > Themes**.  
   - Under **Free themes**, click **Explore free themes** (bold).  
   - Select the theme **Debut** and click **Add theme** (bold).  
   - Click **Publish** (bold).  
   - **Do you see “Debut” as the live theme?** If not, open the Themes page again and click **Publish**.  

4. **Install the “Page Builder by Hulk” App**  
   - In the Admin, go to **Apps > Explore free apps**.  
   - Search for **Page Builder by Hulk**.  
   - Click **Add app** (bold).  
   - Grant permissions by clicking **Install app** (bold).  
   - **Do you see the Hulk Page Builder dashboard?** If it says “App not installed”, re‑install.  

5. **Create a New Landing Page**  
   - In Hulk, click **+ New Page** (bold).  
   - Name the page **“AI‑HR‑Automation”**.  
   - Click **Create Page** (bold).  
   - In the editor, click **Add Section** (bold).  
   - Choose **Hero**.  
   - **Do you see the Hero section added?** If not, click **Add Section** again.  

6. **Design the Hero Section**  
   - Click **Image** → **Upload image** (bold).  
   - Upload a royalty‑free image from **Unsplash** (e.g., `https://unsplash.com/photos/ABC123`).  
   - Set **Title** to `AI‑Powered HR Automation`.  
   - Set **Subtitle** to `Streamline hiring, reduce time‑to‑hire, and scale your talent pipeline.`  
   - Click **Button** → **Edit** (bold).  
   - Set **Button text** to `Get Started`.  
   - Set **Link** to `#contact-form`.  
   - Click **Save** (bold).  
   - **Do you see the hero section with the image, title, subtitle, and button?** If the button is missing, re‑edit the section.  

7. **Add a Contact Form**  
   - In Hulk, click **Add Section** (bold) → **Form**.  
   - Drag the Form to below the Hero.  
   - Set **Form name** to `ContactForm`.  
   - Add fields:  
     - **Name** (Text, required)  
     - **Email** (Email, required)  
     - **Company** (Text, optional)  
     - **Message** (Textarea, required)  
   - Click **Save** (bold).  
   - **Do you see the form with all four fields?** If the “Message” field is missing, double‑check the field list.  

8. **Configure Form to Zapier**  
   - Open a new tab to **https://zapier.com**.  
   - Click **SIGN UP** (top‑right).  
   - Use the same email as Shopify.  
   - **Do you see the Zapier dashboard?** If not, verify email.  
   - In Zapier, click **Make a Zap** (bold).  
   - For **Trigger App**, search and select **Shopify**.  
   - Choose **New Order** (though we’ll use a custom trigger later).  
   - Click **Continue** (bold).  
   - **Do you see the “Choose a trigger event” screen?** If it says “No apps found”, refresh.  

9. **Set Up Custom Trigger for Contact Form**  
   - In Zapier, after selecting Shopify, click **Add Trigger** → **Custom Webhook** (bold).  
   - Choose **Catch Hook**.  
   - Click **Continue** (bold).  
   - Zapier will provide a **Webhook URL** (e.g., `https://hooks.zapier.com/hooks/catch/123456/abcd`).  
   - Copy the URL.  
   - Return to Shopify Hulk editor.  
   - Click the form’s **Settings** → **Form Actions** → **Add Action** (bold).  
   - Select **Webhook**.  
   - Paste the Zapier URL in **Webhook URL** field.  
   - Set **Method** to **POST**.  
   - Click **Save** (bold).  
   - **Do you see the webhook action listed under the form?** If not, re‑

---

## Procedure 5.2: SET UP LEAD GENERATION WITH APOLLO.IO

1. **Open a browser** and navigate to **https://www.apollo.io/signup**.  
2. Click the **Start free trial** button (top‑right corner, green).  
3. In the form that appears, type the following:  
   * **First name**: *YOUR FIRST NAME*  
   * **Last name**: *YOUR LAST NAME*  
   * **Email**: *YOUR EMAIL@DOMAIN.COM*  
   * **Password**: *A secure password (≥12 chars, mix letters, numbers, symbols)*  
4. Check the box **I agree to Apollo’s Terms of Service and Privacy Policy**.  
   ***Do you see the checkbox ticked?*** If not, scroll to the bottom of the form and try again.  

5. Click **Create Account** (button in the center, blue).  
6. Check your inbox for an email from *“Apollo.io: Verify your email”*.  
7. Open the email and click the **Activate Account** link.  
   *You should be redirected to a browser tab that says “Your account is now active.”*  

8. Return to the Apollo.io login page (**https://www.apollo.io/login**) and log in with your credentials.  
9. On the dashboard, locate the **Lead Generation** tab in the left sidebar and click it.  
10. Click the **Create New Lead List** button (top‑left, orange).  

11. In the “New Lead List” modal, type **HR Recruiter Leads** into the **List Name** field.  
12. Under **Filters**, click the **Industry** dropdown, select **Human Resources**.  
13. Click **Job Title** ➜ type **Recruiter** ➜ press **Enter**.  
14. Click **Company Size** ➜ choose **50–200** from the dropdown.  

15. Under **Location**, click the field and type **United States** ➜ press **Enter**.  
    ***Do you see the filters applied?*** If the city or state shows up incorrectly, double‑check the spelling or clear the field and re‑enter.  

16. Click the **Generate Leads** button (bottom right, green).  
17. Wait for the progress bar to finish.  
18. Once complete, a table appears with columns: **Name, Email, Phone, Company, Title, Location, Lead Score**.  
19. Click the **Export CSV** button (top right of the table).  
20. Choose **Download** from the dropdown; the file named *HR Recruiter Leads.csv* will be saved to your Downloads folder.  

21. **Open Zapier** in a new tab (**https://zapier.com/app/dashboard**).  
22. Click **Make a Zap** (top‑right, blue).  
23. For the trigger app, search and select **Apollo.io**.  
24. Choose the trigger event **New Lead** ➜ click **Continue**.  
25. Click **Sign in to Apollo.io** and authorize Zapier to access your Apollo account (OAuth screen).  

26. In the **Set up trigger** step, select the **Lead List** you created: **HR Recruiter Leads**.  
27. Click **Test trigger**; Zapier pulls the first lead from the list.  
28. Click **Continue**.  

29. For the action app, search and select **Google Sheets** (free tier allows 10,000 rows/month).  
30. Choose the action event **Create Spreadsheet Row** ➜ click **Continue**.  
31. Connect your Google account, authorize access.  

32. Select the **Spreadsheet**: *Recruitment Leads* (create one if it doesn’t exist).  
33. Map Apollo fields to sheet columns:  
   * **Name** → *A1*  
   * **Email** → *B1*  
   * **Phone** → *C1*  
   * **Company** → *D1*  
   * **Title** → *E1*  
   * **Location** → *F1*  
34. Click **Test action**; a new row should appear in your sheet.  

35. Click **Turn on Zap

---

## Procedure 5.3: Create Automated Email Nurture Sequence in Klaviyo

1. **Open a web browser** and navigate to **https://www.klaviyo.com/**.  
   - Click the **“Log In”** button in the upper‑right corner.  
   - Enter your **email** and **password**, then click **“Log In”**.  
   - *Expected output:* You should land on the Klaviyo Dashboard with the sidebar displaying **Account**, **Lists & Segments**, **Flows**, etc.

2. **Create a new list** for your recruitment leads.  
   - Click **“Lists & Segments”** in the sidebar.  
   - Press **“Create List”** (bold).  
   - In the popup, type **“Recruitment Leads”** into the **List Name** field, leave the description blank, then click **“Create”**.  
   - *Expected output:* The list “Recruitment Leads” appears in the list table with a status of **“Active”**.

3. **Set up a Zapier trigger** to feed Indeed candidates into Klaviyo.  
   - Open a new tab and go to **https://www.zapier.com/**.  
   - Click **“Make a Zap”** (bold).  
   - Search for **“Indeed”** in the trigger app field and select **“New Job Applicant”**.  
   - Choose your **Indeed account** (connected via API key) and click **“Continue”**.  
   - *Expected output:* Zapier shows a sample applicant record with fields such as **First Name**, **Last Name**, **Email**, **Resume URL**.

4. **Add a Klaviyo action** to add the applicant to the list.  
   - In Zapier, click **“+ Add Action”** (bold).  
   - Search for **“Klaviyo”**

## Check-In: Module 5 Complete

- [ ] Build a High‑Conversion Landing Page on Shopify completed and verified
- [ ] SET UP LEAD GENERATION WITH APOLLO.IO completed and verified
- [ ] Create Automated Email Nurture Sequence in Klaviyo completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 6: DELIVERY

## Overview

In Module 6 you transition from building AI‑powered recruitment workflows to consistently delivering them to paying clients. The focus is on establishing a repeatable delivery pipeline, setting quality checkpoints, and automating all client touchpoints with ready‑made templates. Without a disciplined delivery system, you risk late hand‑offs, inconsistent output, and ultimately a damaged reputation that can stall future contracts. This module teaches you how to scaffold every step—from the initial “run‑through” of the workflow to the final client demo—so that you can scale the same high‑value service to multiple clients without sacrificing quality.

You will learn how to map each workflow into a concrete sprint, attach automated testing and validation steps, and deploy notification triggers that keep both you and your client in the loop. By the end of this module you will have a fully documented, repeatable delivery process that you can hand off to a virtual assistant or use in your own solo practice.

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| **Zapier** | Automate workflow triggers between Indeed, Google Sheets, and Slack | 5 Zaps, 100 tasks/mo | Starter: $19.99/mo (5,000 tasks) |
| **Indeed** | Source candidate data & extract resumes | Free | Paid: $10/mo for resume database access |
| [**Make.com**](https://www.make.com/en/register?pc=menshly) | Alternative low‑code integration engine | 100 operations/mo | Starter: $19/mo (10,000 ops) |
| **Notion** | Workflow documentation & project tracking | Unlimited pages, 5 MB file uploads | Personal Pro: $8/mo |
| [**Grammarly**](https://grammarly.com/) | Ensure all client communications are polished | 3,000 words/month | Premium: $12/mo |
| **Calendly** | Schedule client walkthroughs | 1 calendar, 1 event type | Pro: $10/mo |

**Estimated time to complete:** 5 – 7 hours.

---

## Procedure 6.1: Deploy the Product to Production on Hostinger

1. **Create a Hostinger Account**  
   - Open your browser and navigate to **https://www.hostinger.com**.  
   - Click the **Get Started** button in the top‑right corner.  
   - On the next page, click **Create account**.  
   - Enter your email **(example@yourdomain.com)**, choose a strong password **(e.g., P@ssw0rd2026)**, and click **Create account**.  
   - Verify your email by clicking the link sent to your inbox.  
   - After verification, log in to the Hostinger dashboard.

2. **Select a Hosting Plan**  
   - In the dashboard, click **Hosting** in the left menu.  
   - Click **Choose plan** next to the **Starter** plan.  
   - On the plan details page, click **Add to cart**.  
   - Choose a billing cycle of **Annually** to receive the lowest price.  
   - Click **Proceed to checkout**.  
   - Fill in the payment details (Credit Card or PayPal) and click **Place Order**.  
   - *Do you see a confirmation page with “Order Successful” and a green checkmark? If not, check your payment status in the “Payments” section of the dashboard.*

3. **Register a Domain**  
   - In the dashboard, click **Domains** > **Add Domain**.  
   - Type the domain name you own (e.g., **myhrbot.com**) and click **Check Availability**.  
   - If available, click **Add to Cart**.  
   - If you already own the domain elsewhere, click **Use an Existing Domain** and follow the instructions to point it to Hostinger.  
   - Click **Proceed**.  
   - Confirm the domain registration and pay the annual fee (free for the first year if you use Hostinger’s free domain service).  
   - *Do you see the domain listed under “My Domains” with the status “Active”? If not, wait 5 minutes and refresh.*

4. **Set Up DNS and Nameservers**  
   - In the domain management page, locate **DNS Settings**.  
   - Click **Change Nameservers**.  
   - Enter the Hostinger nameservers:  
     - ns1.registrar-servers.com  
     - ns2.registrar-servers.com  
   - Click **Save**.  
   - Wait 5–10 minutes for the DNS to propagate.  
   - *Do you see “DNS Settings updated” with a timestamp? If not, clear your browser cache and try again.*

5. **Create a New Hosting Account for the Domain**  
   - Click **Hosting** > **Add Hosting**.  
   - Choose the domain you just registered (**myhrbot.com**) from the drop‑down list.  
   - Click **Add Hosting**.  
   - The new hosting account will appear under “My Hosting” with the plan details.  
   - *Do you see the hosting account listed with “Ready to use” status? If not, verify the domain and DNS settings.*

6. **Upload Your Application Files**  
   - In the hosting dashboard, click **File Manager**.  
   - Navigate to the root folder **public_html**.  
   - Click **Upload** in the top toolbar.  
   - Drag and drop the ZIP file of your AI HR bot (containing `index.php`, `config.php`, `vendor/`, etc.) into the upload area.  
   - Once uploaded, click the ZIP file and choose **Extract**.  
   - *Do you see the files listed in the File Manager after extraction? If not, check the upload size limit (Hostinger’s free tier allows up to 500 MB per upload).*

7. **Configure Environment Variables**  
   - In the File Manager, locate **.env** and click “Edit”.  
   - Add the following lines,

---

## Procedure 6.2: Build Quality Assurance and Client Communication Templates

1. **Open Notion** – navigate to https://www.notion.so/, log in, and create a new page titled **“HR Automation QA & Client Templates.”**  
   - In the top left corner click **+ New Page**.  
   - Enter the title and select **“Table – Full Page.”**  
   - Expected output: A blank table with columns **Task ID, Description, Owner, Due Date, Status, Notes**.

2. **Add QA Checklist** – in the table, click **+ New Row** and fill out the first row:  
   - **Task ID:** QA‑01  
   - [**Description:**](https://www.descript.com/) Verify Indeed API connector returns candidate data.  
   - **Owner:** Your name.  
   - **Due Date:** Set to 2 days from today using the calendar picker.  
   - **Status:** **Pending**.  
   - Click **Save**.  
   - Expected output: Row appears with status set to **Pending**.

3. **Create a Client Email Template** – open https://www.canva.com/, log in, click **Create a design → Email Newsletter**.  
   - In the left panel, select **“Text” → Add a heading**.  
   - Type **“Your Weekly Recruitment Update”**.  
   - Add a subheading **“Automation Status & Next Steps”**.  
   - Choose a free Canva template “Modern Email” and customize colors to match your brand.  
   - Click **Download → PDF**.  
   - Expected output: PDF file named **Recruitment_Update.pdf**.

4. **Upload PDF to Notion** – return to the Notion page, click **+** in the **Notes** column of row QA‑01, choose **Upload file**, and select the PDF.  
   - Once uploaded, click **Link Preview** to ensure the PDF opens.  
   - Expected output: PDF preview appears in the table cell.

   **Do you see the PDF preview?**  
   If not, check that the file was fully uploaded; re‑upload if necessary.  

5. **Create a QA Email in ActiveCampaign** – open https://www.activecampaign.com/, log in, navigate to **Campaigns → Create a Campaign**.  
   - Name the campaign **“IndieRecruit QA – Week 1.”**  
   - Click **+ Add an Email**.  
   - In the editor, click **Insert → File** and attach the PDF from step 4.  
   - Add a concise subject line: **“Automation Health Check – Week 1.”**  
   - In the body, include a short paragraph: “Hi [First Name], please review the attached QA report. Let us know if you spot any anomalies.”  
   - Click **Save & Exit**.  
   - Expected output: Email draft with the PDF attached and a preview of the subject line.

6. **Set Up Zapier Trigger for Email Delivery** – open https://zapier.com/, log in, click **Make a Zap**.  
   - For the **Trigger app**, search and select **ActiveCampaign** → choose event **“New Email Sent.”**  
   - Connect your ActiveCampaign account with the API key from the **Settings → Developer** page.  
   - Test the trigger by sending a test email; Zapier should show “Found 1 record.”  
   - Expected output: Zap shows sample data with fields **Email ID, Recipient, Subject**.

7. **Add Action to Slack for QA Notification** – in the same Zap, click **+ Add Action**.  
   - Search and select **Slack → Send Channel Message.**  
   - Connect to your workspace.  
   - In the **Message Text** field, enter:  
     ```
     QA Report Delivered: {{Email Subject}}  
     Recipient: {{Recipient}}  
     Status: Sent
     ```
   - Choose channel **#qa-alerts**.  
   - Click **Test & Review**; Slack should post the message.  
   - Expected output: A message appears in #qa-alerts with the QA report details.

   **Do you see the Slack message?**  
   If not, verify Slack app permissions and channel name.  

8. **Create a Loom Video Script** – open https://www.loom.com/, log in, click **New Video → Screen + Camera**.  
   - In the text editor, type:  
     ```
     Hello [Client Name],

     Here’s a quick snapshot of this week’s recruitment automation status.  
     1. Indeed API health

## Check-In: Module 6 Complete

- [ ] Deploy the Product to Production on Hostinger completed and verified
- [ ] Build Quality Assurance and Client Communication Templates completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 7: SCALING

## Overview  
Module 7 is the launchpad that turns your single‑handed AI HR automation pilot into a profitable, scalable operation. You’ll learn how to transition from solo execution to a vetted contractor team, write SOPs that let you delegate without loss of quality, and run a rigorous margin analysis that tells you exactly how many clients your bundle can support before you hit a revenue plateau. Ignoring this module means you’ll keep cycling through the same manual onboarding loops, under‑utilizing the AI you built, and over‑charging for a service that can be delivered at a fraction of the cost. The result? Stunted growth, diminishing client satisfaction, and a brand that can’t command premium pricing.

By the end of this module you will have:  
1. A clear SOP hierarchy that lets any new contractor hit the ground running.  
2. A 3‑tier contractor hiring checklist that balances cost, skill, and reliability.  
3. A dynamic margin calculator (built in Google Sheets) that feeds directly into your pricing strategy.  

**Estimated time to complete:** 2 h 30 min (including time to set up the spreadsheet and run a mock margin scenario).

| Tool           | Purpose                                                      | Free Tier                                           | Paid Tier (Monthly)                               |
|----------------|--------------------------------------------------------------|-----------------------------------------------------|---------------------------------------------------|
| Zapier         | Connect Indeed, Gmail, Slack, and your CRM into a single workflow | 5 tasks / 2 000 tasks per month (Starter plan)        | $19.99 (Starter) – 50 tasks / 2 000 tasks / 15 000 actions |
| Indeed          | Pull candidate data, push job listings, and sync applicant data | Standard posting (no fee for basic listings)        | $0.75 per click (Premium listings)                 |
| Google Sheets  | Build the margin calculator and SOP templates                | Unlimited (Google account)                          | N/A (free)                                         |
| Canva          | Create branded SOP templates and onboarding decks            | 5 GB storage, 1 GB uploads per month                 | $12.99 (Pro) – Unlimited storage, premium assets   |
| Zapier         | Trigger S3 uploads, Slack alerts, and email digests          | 5 tasks / 2 000 tasks per month                     | $19.99 (Starter) – 50 tasks / 2 000 tasks          |
| Notion         | Store SOPs, contractor contracts, and project backlog       | Unlimited pages, 1 GB file uploads per month        | $8 (Personal Pro) – 10 GB of uploads               |

*Note: Tool pricing is accurate as of October 2026 and may change. Always double‑check the vendor’s pricing page before committing.*

---

## Procedure 7.1: HIRE YOUR FIRST CONTRACTOR ON UPWORK

1. **Open your web browser** and navigate to **https://www.upwork.com**.  
   *Expected UI:* The Upwork home page with a prominent **Sign Up** button in the top‑right corner.  
   *Do you see the **Sign Up** button? If not, refresh the page or clear your cache.*

2. Click the **Sign Up** button.  
   *Expected Output:* A modal with two options: **Create a Client** and **Create a Freelancer**.  
   *Do you see the **Create a Client** button? If not, scroll down the modal.*

3. Click **Create a Client**.  
   *Expected Output:* A new registration form appears.  
   *Do you see the form with fields: Email, Password, First Name, Last Name? If not, check that you are on the client registration page.*

4. Fill in the form:  
   - Email: **yourname@example.com**  
   - Password: **[Strong 12‑char mix]** (e.g., **P@ssw0rd1234**)  
   - First Name: **Your**  
   - Last Name: **Name**  
   Then click **Create Account** (button in bold).  
   *Expected Output:* A verification email is sent to your inbox.

5. Open your email client, locate the Upwork verification email, and click the **Verify Email** link.  
   *Expected Output:* Browser opens **https://www.upwork.com/freelancers/verify?token=xxxx** and displays “Email verified successfully.”  
   *Do you see the verification success message? If not, check your spam folder.*

6. **Log back into Upwork** at **https://www.upwork.com** using the same credentials.  
   *Expected Output:* You land on the Upwork dashboard with a welcome banner.  
   *Do you see the dashboard? If not, clear your cookies and try again.*

7. Click **Find Work** in the top navigation bar, then select **Post a Job**.  
   *Expected Output:* Job posting wizard opens.  
   *Do you see the “Post a Job” page? If not, ensure you are logged in.*

8. In the job posting wizard, complete the following fields:  
   - **Title:** “AI‑Driven Recruitment Automation Workflow Designer”  
   - **Description:** Paste the following (copy‑paste exactly):  
     ```
     We need a contractor with expertise in Zapier, Indeed, and AI tools (ChatGPT, Midjourney) to design, build, and deploy recruitment automation workflows. Must deliver a fully functional Zapier integration that pulls candidate data from Indeed and stores it in a Google Sheet.  
     ```
   - **Skills:** Type **Zapier**, **Indeed API**, **AI Automation**; click the checkboxes.  
   - **Budget type:** **Fixed Price**; **Budget:** **$500** (enter 500 in the field).  
   - **Duration:** **4 weeks** (set start date to today).  
   - **Job type:** **One‑time Project**.  
   Click **Continue** (button in bold).  
   *Expected Output:* Review screen summarizing your job posting.

9. Review the job details. If everything looks correct, click **Post Job** (button in bold).  
   *Expected Output:* Confirmation page with job posting ID **JOB‑202610‑XXXXX** displayed.  
   *Do you see the job ID? If not, use the browser’s “View Page Source” to locate it.*

10. **Set up Zapier automation** to notify you of new proposals.  
    - Open **https://zapier.com** and log in (use free tier).  
    - Click **Make a Zap** (top‑right).  
    - In the **Trigger** app search, type **Upwork** and select **New Proposal**.  
    - Click **Continue**.  
    - Connect your Upwork account (click **Sign in to Upwork** and allow permissions).  
    - Choose **Job** field: **JOB‑202610‑XXXXX**.  
    - Click **Test Trigger** → you should see a sample proposal JSON.  
    *Expected Output:* Sample JSON with fields: `proposal_id`, `freelancer_name`, `amount`.  
    *Do you see a sample proposal? If not, ensure the job ID is correct.*

11. In the **Action** step, search for **Slack** (free tier includes 10,000 messages/month).  
    - Select **Send Channel Message** → **Continue**.  
    - Connect your Slack workspace (click **Sign in to Slack**

---

## Procedure 7.2: Build SOPs for Task Delegation in Notion

1. **Open your web browser** and go to the Notion homepage:  
   `https://www.notion.so/`.  
   Click the **"Log in"** button (top‑right) and sign in with your existing credentials or create a new account.  
   *Expected output:* You are on your main workspace dashboard with a sidebar on the left.

2. In the sidebar, click the **"+"** icon next to **"Private"** to create a new page.  
   In the popup, type `Task Delegation SOP` and press **Enter**.  
   *Expected output:* A blank page titled “Task Delegation SOP” appears.

3. With the new page open, click the first icon under the title and select **"Table – Full page"**.  
   Name the table `Delegation Tasks`.  
   *Expected output:* A fully‑editable table appears with default columns `Name`, `Tags`, `Created`, `Last edited`.

4. **Add custom columns**:  
   - Click the **"+"** at the right of the table header.  
   - Choose **"Select"** → name it **"Status"**.  
   - Repeat to add a **"Date"** column named **"Due Date"**.  
   - Add a **"People"** column named **"Assignee"**.  
   *Interactive check‑in:* Do you see the four columns (`Name`, `Status`, `Due Date`, `Assignee`)?  
   If not, refresh the page or re‑open the table editor.

5. In the `Status` column, click the dropdown on the header and choose **"Add option"**.  
   Add the following options with colors:  
   - **Pending** (Red)  
   - **In Progress** (Yellow)  
   - **Completed** (Green)  
   *Expected output:* Status column now offers three color‑coded options.

6. Scroll to the bottom of the page and click **"Template button"** (under **"More blocks"** → **"Templates"**).  
   Name the button **"New Delegation Task"**.  
   Inside the template, add a **new table row** with default values:  
   - `Status`: **Pending**  
   - `Due Date`: **Today + 7 days** (use `+7d` notation)  
   - `Assignee`: leave blank.  
   *Expected output:* Clicking the button inserts a ready‑to‑edit row.

7. In the page header, click **"Share"** (top‑right) → **"Copy link"**.  
   Turn on **"Allow editing"** for collaborators you’ll add later.  
   *Expected output:* Link copied to clipboard, sharing toggled.

8. **Add your first delegate**:  
   - Click the **"People"** column header → **"Add a person"**.  
   - Search for the email of the delegate (e.g., `john.doe@example.com`) and click **"Invite"**.  
   *Expected output:* Delegate appears in the list and receives an email invite.

9. Create a **Zapier** automation to auto‑populate the `Due Date` based on a trigger from an external HR tool (e.g., Indeed).  
   - Go to `https://zapier.com/app/dashboard`.  
   - Click **"Make a Zap"**.  
   - Choose **"Indeed"** as the Trigger app (search and select **"New Job Posting"**).  
   - Connect your Indeed account by clicking **"Continue"** → **"Sign in to Indeed"** → enter credentials.  
   *Interactive check‑in:* Do you see the **"Trigger"** step set to “New Job Posting”?  
   If not, double‑check the Indeed integration status in **My Apps**.

10. In the **Zapier** action step, search for **"Notion"** → select **"Create Database Item"**.  
    - Connect your Notion account by clicking **"Continue"** → **"Sign in to Notion"** → paste the integration token (see step 12).  
    - Choose the workspace and select the `Delegation Tasks` database you created.  
    - Map fields:  
      - **Name** ← `Job Title` (from Indeed)  
      - **Status** ← **Pending** (manual selection)  
      - **Due Date** ← `Application Deadline` (from Indeed)  
      - **Assignee** ← **HR Manager** (enter email).  
    *Expected output:* Zapier shows a preview of the mapped data.

11. Test the Zap by clicking **"Test & Review"**.  


---

## Procedure 7.3: Run a Margin Analysis and Pricing Review

1. **Open your web browser** and navigate to **https://zapier.com**.  
   - *Expected output*: Zapier landing page with “Sign in” button visible.

2. **Click the **bold** button** “Sign in” in the upper‑right corner.  
   - *Expected output*: Login form with fields “Email” and “Password”.

3. **Enter your email and password** (use the credentials you created during Module 6).  
   - *Expected output*: Logged‑in dashboard showing “Dashboard” and “Explore” tabs.

4. **Click the **bold** button** “My Zaps” in the left navigation pane.  
   - *Expected output*: List of existing Zaps (empty if none created).

5. **Click the **bold** button** “Make a Zap” at the top center of the page.  
   - *Expected output*: Zap creation wizard opens.

6. **Search for “Google Sheets”** in the Trigger app search bar and select it.  
   - *Expected output*: Google Sheets trigger options appear.

7. **Choose the trigger event** “New Spreadsheet Row” from the list.  
   - *Expected output*: “Continue” button enabled.

8. **Click the **bold** button** “Continue”.  
   - *Expected output*: Prompt to connect Google account.

9. **Click the **bold** button** “Connect a new account”.  
   - *Expected output*: Google OAuth window pops up.

10. **Authorize Zapier** to access your Google Sheets.  
    - *Expected output*: Connection successful message.

11. **Do you see the “Set up trigger” screen with your spreadsheet list?**  
    - If not, **go back to step 9** and ensure you logged into the correct Google account.

12. **Select the spreadsheet** named “MarginAnalysis” (you created it in Module 6).  
    - *Expected output*: Sheet list shows “MarginAnalysis” with available sheets.

13. **Choose the sheet** “Data” and click **bold** “Continue”.  
    - *Expected output*: Sample row preview appears.

14. **Click the **bold** button** “Test trigger”.  
    - *Expected output*: Zapier pulls the first row and displays “Test data”.

15. **Click the **bold** button** “Continue”.  
    - *Expected output*: You’re taken to “Choose an Action” step.

16. **Search for “Notion”** in the Action app search bar and select it.  
    - *Expected output*: Notion action options appear.

17. **Choose the action event** “Create Database Item” and click **bold** “Continue”.  
    - *Expected output*: Prompt to connect to Notion.

18. **Click the **bold** button** “Connect a new account”.  
    - *Expected output*: Notion OAuth window opens.

19. **Authorize Zapier** to access your Notion workspace.  
    - *Expected output*: Connection successful message.

20. **Select the database** “MarginAnalysisDB” created in Module 6.  
    - *Expected output*: List of properties in the database.

21. **Map the Google Sheets columns to Notion properties**:  
    - **Column A** → “Client Name” (text)  
    - **Column B** → “Service Scope” (text)  
    - **Column C** → “Base Cost (USD)” (number)  
    - **Column D** → “Margin %” (number)  
    - **Column E** → “Recommended Price (USD)” (formula: `C * (1 + D/100)`)  
    - *Expected output*: Mapping confirmation screen.

22. **Click the **bold** button** “Continue”.  
    - *Expected output*: Test data preview shows correct mappings.

23. **Click the **bold** button** “Test & Review”.  
    - *Expected output*: Zapier creates a new item in Notion with the test data.

24. **Open Notion** in a new tab at **https://www.notion.so**.  
    - *Expected output*: Your workspace with the “MarginAnalysisDB” database open.

25. **Verify that the new test entry appears** with correct values in each column.  
    - *Expected output*: Row displays “Client A”, “Recruitment Automation”, “$2000”, “25%”, “$2500”.

26. **Do you see the new row in Notion?**  
    - If **not**, **return to Zapier** and re‑run the test.  
    - If the row appears but the “Recommended Price” column shows a blank or wrong value, **check the formula syntax**: `C *

## Check-In: Module 7 Complete

- [ ] HIRE YOUR FIRST CONTRACTOR ON UPWORK completed and verified
- [ ] Build SOPs for Task Delegation in Notion completed and verified
- [ ] Run a Margin Analysis and Pricing Review completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 8: ADVANCED PATTERNS

## Overview  

Module 8 dives into the high‑value tactics that transform a basic AI‑powered HR workflow into a scalable, revenue‑driven service. You will learn how to layer premium features—such as real‑time candidate scoring, automated interview scheduling, and predictive attrition alerts—over the core Zapier‑Indeed integration. These patterns unlock the ability to upsell clients, generate recurring revenue, and package your service into a product that can be sold to multiple companies at once.  

Skipping this module means you’ll stay stuck in the “first‑look” automation zone: simple data pulls and one‑off triggers. You’ll miss the opportunity to differentiate yourself from the growing crowd of solo recruiters offering generic bots. By mastering advanced patterns, you’ll command higher price points, reduce churn, and create a repeatable sales funnel that feeds your business automatically.  

**Tools needed for this module**  

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| **Zapier** | Connects Indeed, Gmail, Google Sheets, Calendly, etc. | 5,000 tasks/month, 3 Zaps | Starter: $19.99/mo (15,000 tasks), 20 Zaps |
| **Indeed API** | Pull candidate data, job listings, and applicant tracking | N/A (API key only) | N/A |
| **Calendly** | Automate interview scheduling and reminders | 1 user, 1 event type | Pro: $12/user/mo |
| **Google Sheets** | Central database for candidate records | Unlimited | Unlimited |
| **Mailchimp** | Email nurturing for candidate follow‑ups | 2,000 contacts | Essentials: $9.99/mo |
| **ChatGPT** | Draft email templates, generate job descriptions | 90 min/month | Plus: $20/mo |
| **Zapier Webhooks** | Custom triggers for bespoke actions | — | — |
| **Zapier Paths** | Conditional logic for multi‑step flows | — | — |

**Estimated time to complete**  
The full module, including reading, hands‑on labs, and testing, requires approximately **12 hours** of focused work. This includes 4 hours of video instruction, 3 hours of hands‑on Zap creation, 2 hours of testing and debugging, and 3 hours for documentation and packaging.

---

**Procedure 8.1** — Generation failed due to AI backend unavailability. Please retry later.

---

## Procedure 8.2: BUILD Subscription Tiers on Shopify for AI‑HR Automation Services

1. **Open a web browser** and navigate to **https://www.shopify.com/**.  
2. Click the **bold button “Start free trial”**.  
3. Fill the form:  
   - Email: *you@example.com*  
   - Password: *StrongPass!123*  
   - Store name: *AI‑HR‑Solutions*  
   Click **“Create your store”**.  
4. You now land on the **Shopify Admin Dashboard**.  
   **Do you see the “Dashboard” page with your store name at the top?** If not, refresh the page or log in again.  
5. Click **“Settings”** → **“Plan and permissions”** → **“Change plan”**.  
6. Select the **“Basic Shopify”** plan ($29 / month) and click **“Select”**.  
7. Confirm the purchase by clicking **“Start plan”** and then **“Confirm”**.  
8. Return to the dashboard, click **“Products”** → **“Add product”**.  
9. Create a new product named **“AI‑HR Automation Package”**.  
   - Description: “Automated recruitment workflow powered by Zapier & Indeed.”  
   - Upload a banner image from Canva (free tier: 30 templates).  
   - Set **Price** to **$0** (since we'll set subscription fees via Shopify’s billing API).  
   Click **“Save product”**.  
10. In the product page, toggle **“This is a subscription product”** (Shopify’s “Subscriptions” app is included in the Basic plan).  
11. Click **“Add price”** → **“Add tier”**.  
    - Tier 1: **Basic – $50 / month**  
    - Tier 2: **Pro – $120 / month**  
    - Tier 3: **Enterprise – $250 / month**  
12. Save the tiers.  
    **Do you see the three subscription tiers listed under the product?** If not, ensure you toggled the subscription switch.  
13. Navigate to **“Apps”** → **“Visit Shopify App Store”**.  
14. Search for **“Zapier”** and click **“Add app”**.  
15. In the Zapier portal, click **“Add a Zap”** → **Trigger**: **Shopify** → **Event**: **“New Order”**.  
16. Authenticate your Shopify store by clicking **“Sign in to Shopify”** and allow access.  
17. Test the trigger: place a dummy order for the subscription product.  
    **Do you see the test order appear in Zapier?** If not, ensure the product is enabled for subscriptions.  
18. Add an **Action**: **Make.com** (Webhooks by Make).  
    - Choose **“Make a request”**.  
    - Method: **POST**.  
    - URL: `https://api.indeed.com/ads/v4/ads`.  
    - Headers:  
      ```
      Authorization: Bearer YOUR_INDEED_API_KEY
      Content-Type: application/json
      ```  
    - Body (JSON):  
      ```json
      {
       

## Check-In: Module 8 Complete

- [ ] Create a High-Ticket Consulting Package completed and verified
- [ ] BUILD Subscription Tiers on Shopify for AI‑HR Automation Services completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 9: FINANCIAL OPERATIONS

## Overview  
In Module 9 you will master the financial backbone of your AI‑powered HR and recruitment automation service. Without a reliable revenue tracking system, pricing strategy, and contract framework, every automated workflow you build will be a shell of a business. This module teaches you how to construct a real‑time financial dashboard, set dynamic pricing tiers, and generate proposal and contract templates that close deals and protect your margins. Skipping this step means you’ll miss critical insights into cash flow, client profitability, and scalability. You’ll also risk under‑charging for high‑value services or over‑charging and losing clients to competitors.

You’ll start by integrating Zapier with Indeed and your accounting software to auto‑capture leads, payments, and performance metrics. Next, you’ll use Make.com to pull data into Notion tables, which feed a dynamic pricing engine built in Google Sheets. Finally, you’ll create reusable proposal and contract templates in Canva, and set up automated email workflows in Klaviyo to deliver them upon client confirmation. By the end of this module, your pipeline will be transparent, your pricing will reflect true value, and every closing will be backed by legally sound agreements.

| Tool          | Purpose                                         | Free Tier                                   | Paid Tier                                 |
|---------------|-------------------------------------------------|---------------------------------------------|-------------------------------------------|
| Zapier        | Automate data sync between Indeed, Notion, and accounting | 100 tasks/month, 5 Zaps                     | Starter $19.99/mo (Unlimited Zaps)        |
| Make.com      | Advanced workflow orchestration and data manipulation | 300 operations/month, 2 min delay           | Starter $9.99/mo (Unlimited ops, 5 sec delay) |
| Notion        | Central database for proposals, contracts, and dashboards | Unlimited pages for free                     | Pro $8/mo (per person)                    |
| Canva         | Design proposal & contract templates | 5 templates/month, 30 GB storage | Pro $12.99/mo (Unlimited templates, 100 GB) |
| Klaviyo       | Automated proposal delivery & follow‑ups | 5 k emails/month                           | Growth $30/mo (Unlimited emails)          |

**Estimated time to complete:** 4 – 6 hours of focused work.

---

**Procedure 9.1** — Generation failed due to AI backend unavailability. Please retry later.

---

## Procedure 9.2: Create Proposal Templates and Automated Billing with Stripe  

1. **Create a Stripe Business Account**  
   1.1. Open a web browser and go to **https://stripe.com**.  
   1.2. Click the **SIGN UP** button in the upper‑right corner.  
   1.3. Fill the form:  
        - **Email**: your‑business@email.com  
        - **Password**: a strong password (e.g., `Str0ngP@ssw0rd!`)  
        - **Business name**: *Menshly AI HR Services*  
   1.4. Click **CREATE ACCOUNT**.  
   1.5. Verify your email by clicking the link Stripe sends to your inbox.  
   1.6. **Do you see the Stripe Dashboard with “Dashboard” tab selected?** If not, refresh the page or log in again.

2. **Enable Stripe Billing**  
   2.1. In the Dashboard, click **Billing** in the left sidebar.  
   2.2. Click **+ Create product**.  
   2.3. Enter **Product name**: *HR Automation Proposal* and **Description**: “Automated proposal & billing for HR services.”  
   2.4. Under **Pricing**, click **+ Add price** → **One‑time** → **USD 250**.  
   2.5. Click **Save product**.  
   2.6. **Do you see the product listed with a price of USD 250?** If not, double‑check the price field.

3. **Create a Stripe Invoice Template**  
   3.1. From the left sidebar, go to **Billing** → **Invoices**.  
   3.2. Click **+ New template**.  
   3.3. Name the template **“HR Automation Proposal Invoice”**.  
   3.4. In the **Template editor**, add the following block:  
        - **Company logo**: Upload the logo file `menshly_logo.png`.  
        - **Client details**: `{{customer.name}}`, `{{customer.email}}`.  
        - **Item list**: Auto‑populate product line.  
   3.5. Click **Save template**.  
   3.6. **Do you see your new template in the list?** If not, check the “Templates” tab.

4. **Build a Proposal Template in Canva**  
   4.1. Open **https://www.canva.com** and log in.  
   4.2. Click **Create a design** → **Custom size** → **800 × 1120 px**.  
   4.3. Drag and drop a **Text box** → type **“Proposal for {{clientName}}”**.  
   4.4. Insert a **Table** with the following columns: Service, Description, Price.  
   4.5. Leave the price cell blank; it will be auto‑filled by Zapier.  
   4.6. Click **Download** → **PDF (Print)** → name the file `HR_Proposal_Template.pdf`.  
   4.7. **Do you see the downloaded PDF?** If not, check the Downloads folder.

5. **Set Up a Zapier Workflow for Proposal Generation**  
   5.1. Open **https://zapier.com** and log in.  
   5.2. Click **Make a Zap**.  
   5.3. For the **Trigger App**, search and select **Stripe** → choose **New Customer**.  
   5.4. Click **Continue** → connect your Stripe account using the API key from **Developers → API keys** in Stripe.  
   5.5. In the **Test Trigger**, click **Test** → confirm a test customer appears.  
   5.6. **Do you see a test customer in the Zap history?** If not, ensure the API key is correct (see error scenario below).

6. **Add an Action to Create a Proposal in Notion**  
   6.1. Click **+ Add Action** → search for **Notion** → select **Create Database Item**.  
   6.2. Connect your Notion workspace (you’ll be redirected to `https://www.notion.so/oauth`).  
   6.3. Choose the database **“HR Proposals”** (create it first in Notion if missing).  
   6.4. Map fields:  
        - **Title** → `{{customer.name}} – Proposal`  
        - **Client Email** → `{{customer.email}}`  
        - **Proposal PDF** → upload the Canva PDF file from step 4.  
   6.5. Click **Continue** → **Test Action** → confirm a new database item appears.  
   6.6. **Do you see the new proposal entry in Notion?** If not, verify the database name.

7. **Send an Email with the Proposal via Gmail**  
   7.1. Click **+ Add Action** → search for **Gmail** → choose **Send Email**.  
   7.2. Connect your Gmail account.  
   7.3. Fill the email fields:  
        - **To**: `{{customer.email}}`  
        - **Subject**: “Your HR Automation Proposal”  
        - **Body**:  
          ```
          Hi {{customer.name}},

          Please find attached the proposal for our HR automation services. Let us know if you have any questions.

          Best,


## Check-In: Module 9 Complete

- [ ] Build a Live Revenue Dashboard in Notion with Make.com completed and verified
- [ ] Create Proposal Templates and Automated Billing with Stripe completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 10: LAUNCH PLAN

## Overview  
This module is the *execution engine* that transforms your AI‑HR automation blueprint into revenue‑generating action. Over the next 30 days you will follow a day‑by‑day calendar that moves you from zero configuration to securing your first paying client. Every step is measured, documented, and validated against the KPIs you set in Module 9. Skipping this module means you will never move beyond the “idea” stage; without a concrete launch cadence you’ll waste time on ad hoc tweaks, miss early revenue, and lose the competitive edge that automation gives solo entrepreneurs.

The launch plan is split into three tightly‑scheduled procedures: **(1) Market‑ready service setup**, **(2) Client‑onboarding workflow construction**, and **(3) Paid‑client acquisition & delivery**. Each procedure includes precise UI actions, data‑export checks, and error‑handling scripts. The calendar forces you to hit milestones on day‑5, day‑12, day‑20, and day‑30, ensuring momentum and a clear exit point for the next phase.

**Tool Stack Snapshot**

| Tool      | Purpose                                           | Free Tier Details                                    | Paid Tier (Monthly) |
|-----------|---------------------------------------------------|-------------------------------------------------------|---------------------|
| **Zapier**| Connect Indeed ↔ email, CRM, calendar, etc.      | 100 tasks/month, 3 Zaps, 15‑min schedule             | Starter – $19.99*   |
| **Indeed**| Job posting & candidate sourcing                 | Unlimited free job posts                              | Premium – $49.99*   |
| **Make.com**| Advanced workflow logic & data enrichment        | 1,000 operations/month, 5 scenarios                  | Starter – $29.99*   |
| [**Replit**](https://replit.com/refer/egwuokwor)| Code snippets for custom API hooks                | Unlimited public repls, 500 MB storage                | Hacker – $7.99*     |
| [**Vapi**](https://vapi.ai/)  | Voice‑to‑text/call‑automation for candidate replies | 500 minutes/month, 3 calls/day                       | Pro – $39.99*       |
| [**Canva**](https://www.canva.com/) | Branding assets for proposals & proposals        | Unlimited designs, 5GB storage                        | Pro – $12.99*       |
| **ChatGPT** | Content generation for outreach & FAQs          | 3 M tokens/month, 30‑min limit per request           | Plus – $20.00*      |
| **ElevenLabs** | AI‑voice for candidate messaging            | 5 hrs audio/month, 2 voices                          | Pro – $29.00*       |
| **Notion** | Project tracking & documentation                 | Unlimited pages, 5 GB storage                        | Personal Pro – $8.00|

\*All prices are the lowest paid tier available at the time of writing and may vary.

**Estimated Time to Complete**  
30 days of focused execution (≈ 2 hours/day). By day 30 you will have a validated workflow, a signed client contract, and a delivery pipeline in place.

---

## Procedure 10.1: Configure Demo Scheduling with Calendly and Notion

1. **Open Calendly**  
   - URL: `https://calendly.com/`.  
   - Click the **“Sign up”** button in the top‑right corner.  
   - Use your Gmail address; click **“Continue with Google”**.  
   - Accept the permissions and click **“Allow”**.  

2. **Create a new event type**  
   - In Calendly’s dashboard, click **“Event Types”** on the left panel.  
   - Click the **“+ New event type”** button.  
   - Select **“One‑on‑one”** and click **“Create event type.”**  

3. **Name and set duration**  
   - In the **“Event name”** field, type **“AI HR Demo – 30 min.”**  
   - Set **“Duration”** to **30** minutes.  
   - Click **“Save & Continue.”**  

4. **Configure availability**  
   - Under **“When can people book this event?”** set the days to **Monday‑Friday** and the time range to **9:00 am – 5:00 pm** (local time).  
   - Click **“Save & Continue.”**  

5. **Add invitee questions**  
   - Click **“Invitee questions”**.  
   - Click **“Add a question.”**  
   - Choose **“Short answer”** and type **“Candidate Name.”**  
   - Click **“Save.”**  
   - Add another question, choose **“Email address.”**  
   - Add a third, choose **“Short answer”** and type **“Position Applying For.”**  
   - Click **“Save & Continue.”**  

6. **Set up reminders**  
   - Click **“Notifications & cancellation”**.  
   - Toggle **“Email reminder”** to ON.  
   - Set **“Send reminder 15 minutes before the event.”**  
   - Toggle **“SMS reminder”** to ON (note: SMS requires a paid plan).  
   - Click **“Save & Continue.”**  

7. **Publish the event**  
   - Click **“Publish”**.  
   - The page will display **“Your event link is ready.”**  
   - Copy the URL shown (e.g., `https://calendly.com/yourname/ai-hr-demo`).  

**Do you see the event link displayed?**  
If not, refresh the page and ensure you have clicked **“Publish.”**  

8. **Open Notion**  
   - URL: `https://www.notion.so/`.  
   - Log in with your Google account.  

9. **Create a new database**  
   - In Notion, click **“+ New page”** in the left sidebar.  
   - Choose **“Table – Full page.”**  
   - Name the table **“Demo Sign‑Ups.”**  

10. **Add columns**  
    - Keep the default **“Name”** column.  
    - Click the **“+ Add a property”** button.  
    - Create **“Email”** (type **Email**).  
    - Create **“Position”** (type **Text**).  
    - Create **“Scheduled Time”** (type **Date**).  
    - Create **“Calendly Link”** (type **URL**).  

11. **Retrieve Notion integration token**  
    - In Notion, click your profile icon > **“Settings & Members.”**  
    - Click **“Integrations”** > **“Develop your own integrations.”**  
    - Click **“+ New integration.”**  
    - Name it **“Calendly‑Automation.”**  
    - Set **“Capabilities”** to **“Read content”** and **“Insert content.”**  
    - Click **“Submit.”**  
    - Copy the **“Internal Integration Token”** and store it securely (e.g., in a password manager).  

12. **Set up Zapier integration**  
    - URL: `https://zapier.com/`.  
    - Log in or create an account (free tier: 100 tasks/month).  
    - Click **“Create Zap.”**  
    - **Trigger**: Search for **“Calendly.”** Select **“New Invitee.”**  
    - Connect your Calendly account by clicking **“Connect an Account”** and following the OAuth prompt.  

13. **Configure the trigger**  
    - Choose the event type **“AI HR Demo – 30 min.”**  
    - Click **“Test trigger.”**  
    - Zapier will show a sample event; click **“Continue.”**

---

## Procedure 10.2: BUILD MARKETING AUTOMATION AND PROSPECT LIST WITH APOLOGIO

1. **Open Apollo.io**  
   - URL: `https://app.apollo.io/`  
   - Click **Login** (top‑right corner).  
   - Enter your email and password, then click **Log In**.  
   - *Expected output:* You are taken to the Apollo dashboard with the “Leads” tab highlighted.

2. **Create a New Search**  
   - In the left sidebar, click **Leads** → **Search**.  
   - Click **+ New Search** (button in the top‑right corner).  
   - In the **Search Criteria** panel, set:  
     *Industry: “Information Technology”*  
     *Job Title: “HR Manager”, “Talent Acquisition”, “Recruiter”*  
     *Location: “United States”*  
     *Company Size: “51‑200”*  
     *Experience: “5‑10 years”*  
   - Click **Apply Filters**.  
   - *Expected output:* A list of 200–300 prospects appears.

3. **Refine Search by Company Stage**  
   - In the same panel, under **Company Stage**, choose **“Series A”** and **“Series B”**.  
   - Click **Apply Filters** again.  
   - *Expected output:* The prospect count decreases to ~120.

4. **Export the Prospect List**  
   - Click the **Export** icon (download arrow) above the table.  
   - Select **CSV** as file type.  
   - Click **Export CSV**.  
   - *Expected output:* A `prosp_list.csv` file downloads to your computer.

**Do you see the CSV file in your Downloads folder?**  
If not, check that your browser is not blocking downloads. Go to `Settings → Privacy → Downloads` and allow downloads from `apollo.io`.

5. **Open Zapier**  
   - URL: `https://zapier.com/app/dashboard`  
   - Click **Sign In** (top‑right).  
   - Use your Google account to log in.  
   - *Expected output:* Zapier dashboard with “My Zaps” tab.

6. **Create a New Zap**  
   - Click **Make a Zap** (top‑left).  
   - In the **Choose App & Event** search bar, type **Google Sheets**.  
   - Select **Google Sheets → New Spreadsheet Row**.  
   - Click **Continue**.

7. **Connect Google Sheets**  
   - Click **Sign in to Google**.  
   - Choose the Google account that hosts your spreadsheet.  
   - Click **Allow** (grant permissions).  
   - *Expected output:* “Google Sheets Connected” status.

8. **Set Up the Trigger**  
   - In **Spreadsheet** dropdown, select `ProspectList`.  
   - In **Worksheet** dropdown, select `Sheet1`.  
   - Click **Continue**.  
   - Zapier will test by finding a row.  
   - *Expected output:* “Test Trigger Successful” and sample data preview.

9. **Add Action: Send Email via Gmail**  
   - Click **+ Add Step** → **Action**.  
   - Search for **Gmail**.  
   - Choose **Send Email**.  
   - Click **Continue**.

10. **Connect Gmail**  
    - Click **Sign in to Gmail**.  
    - Choose your Gmail account.  
    - Click **Allow**.  
    - *Expected output:* “Gmail Connected” status.

11. **Map Email Fields**  
    - In **To** field, click the dropdown → **Custom**, then select `Email` from the trigger data.  
    - In **Subject** field, type `🚀 Let’s Talk About Your Hiring Strategy`.  
    - In **Body** field, paste:  
      ```
      Hi {{FirstName}},
      
      I’m reaching out because we help companies like yours streamline hiring with AI‑powered automation. 
      
      Could we schedule a quick 15‑minute call?  
      
      Click here to book: https://calendly.com/yourname/15min
      
      Thanks,  
      Your Name
      ```  
    - Click **Continue**.

12. **Test Gmail Action**  
    - Click **Test & Review**.  
    - Zapier will send an email to the address in the sample row.  
    - *Expected output:* “Success” and a preview of the sent email.

13. **Activate the Zap**  
    - Click **Turn on Zap**.  
    - *Expected output:* Zap status changes to “ON”.

**Do you see the Zap labeled “Prospect Emailer” in your dashboard?**  
If not, refresh the page. If still missing, ensure you clicked “Turn on Zap”.

14. **Upload CSV to Google Sheets**  
    - Open `https://docs.google.com/spreadsheets/u/0/` and create a new spreadsheet named `ProspectList`.  
    - In the top menu, click **File → Import** → **Upload** → drag `prosp_list.csv`.  
    - Select **Replace current sheet** and click **Import data**.  
    - *Expected output:* First row contains headers, subsequent rows contain prospect data.

15. **Enable Auto‑Update

---

**Procedure 10.3** — Generation failed due to AI backend unavailability. Please retry later.

## Check-In: Module 10 Complete

- [ ] Configure Demo Scheduling with Calendly and Notion completed and verified
- [ ] BUILD MARKETING AUTOMATION AND PROSPECT LIST WITH APOLOGIO completed and verified
- [ ] Execute the 30-Day Launch Calendar completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# APPENDIX A: COMPLETE TOOL REFERENCE

| Tool | Purpose | Free Tier | Paid Tier | When to Upgrade |
|------|---------|-----------|-----------|-----------------|
| **Hostinger** | Domain registration & shared hosting for the HR‑automation website. | Domain registration $12.99 / yr (free with hosting); Starter Hosting $1.99 / mo (single shared). | Premium Hosting $3.99 / mo (more bandwidth, SSL, 24‑hr support). | When traffic >10 GB / month, need dedicated IP, or require custom email hosting. |
| **Notion** | Central knowledge base, client intake forms, SOPs, and integration hub. | Unlimited pages, 5 MB per file, 1 GB file storage. | Team $10 / seat / mo, Enterprise $20 / seat / mo. | When you need >1 GB storage, advanced permissions, or audit logs. |
| **Calendly** | Schedule interviews and demos with candidates or clients. | 1 event type, 1 calendar, 1 participant. | Premium $12 / mo (multiple calendars, team scheduling). | When you need >1 calendar or team members to book on your behalf. |
| **Zapier** | Automate data flow between Calendly, Notion, Indeed, and other services. | 100 tasks/month, 5 Zaps, 15‑min polling. | Starter $19.99 / mo (Unlimited Zaps, 15‑min polling), Professional $49 / mo (5‑min polling). | When tasks >100/month or need faster polling and multi‑step Zaps. |
| **Indeed** | Job

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

## 1. PREPARE YOUR DATA SHEET  
**Tool:** Notion (Free Plan, 1 000 blocks, $8/month for Personal Pro).  
**Why:** Central repository for all numeric inputs, automatically refreshed by Make.com and Zapier.  

1.1. Open your workspace in Notion.  
1.2. Create a new database called **“Revenue Forecast”**.  
- Click **+ New Page** → **Table – Full Page**.  
- Title the page **Revenue Forecast**.  
1.3. Add the following columns:  
| Column | Type | Description |
|--------|------|-------------|
| Month | Date | First day of the month (e.g. 2026‑10‑01). |
| Clients | Number | Expected new clients that month. |
| Revenue | Number | Gross revenue (USD). |
| Expenses | Number | Monthly operating costs (USD). |
| Profit | Formula | `Revenue - Expenses`. |
1.4. **Populate** the first row with the current month’s data (e.g. 2026‑10‑01).  
1.5. **Do you see the table with five columns?**  
- *If not, check that you are in Table view and that all column types match the above.*  

## 2. CALCULATE MONTHLY REVENUE  
**Tool:** Make.com (Free Plan: 100 operations/month; Paid Plan: $49/month for 1 000 ops).  

2.1. Log into Make.com.  
2.2. Click **Create a new scenario**.  
2.3. Add a **Notion** module:  
- Choose **“Retrieve a database entry”**.  
- Connect to your Notion account by clicking **Add new connection** → follow the OAuth prompt.  
- In the **Database** field, select **Revenue Forecast**.  
2.4. Add a **Set variable** module.  
- Variable name: `monthly_clients`.  
- Value: `{{Notion.entry.Clients}}`.  
2.5. Add a **Set variable** module.  
- Variable name: `client_price`.  
- Value: `{{Pricing_Tiers.Price}}` (see §3 for pricing tier definitions).  
2.6. Add a **Math** module.  
- Operation: `Multiply`.  
- Input 1: `{{monthly_clients}}`.  
- Input 2: `{{client_price}}`.  
- Output variable: `monthly_revenue`.  
2.7. Add a **Set variable** module.  
- Variable name: `monthly_expenses`.  
- Value: `{{Expenses_Tier.Total}}` (see §4).  
2.8. Add a **Math** module.  
- Operation: `Subtract`.  
- Input 1: `{{monthly_revenue}}`.  
- Input 2: `{{monthly_expenses}}`.  
- Output variable: `monthly_profit`.  
2.9. Add a **Notion** module: **Update a database entry**.  
- Map `Revenue` to `{{monthly_revenue}}`.  
- Map `Expenses` to `{{monthly_expenses}}`.  
- Map `Profit` to `{{monthly_profit}}`.  
2.10. **Do you see the "Run once" button?**  
- *If not, ensure the scenario is saved and that all modules are connected.*  

## 3. DEFINE PRICING TIERING  
**Tool:** Shopify (Basic Plan: $29

For the free step-by-step guide, see our [implementation guide]({< ref "/intelligence/build-an-ai-voice-agent-system-with-vapi-the-complete-step-by-step-guide.md" >}).


## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
