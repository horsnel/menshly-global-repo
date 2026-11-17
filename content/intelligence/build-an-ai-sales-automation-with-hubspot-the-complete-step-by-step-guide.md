---
title: "Build an AI Sales Automation with HubSpot: The Complete Step-by-Step Guide"
date: 2026-11-17
category: "Implementation"
difficulty: "ADVANCED"
readTime: "25 MIN"
excerpt: "*Section content pending review.*"
image: "/images/articles/intelligence/automate-qualify-and-optimize-sales-with-hubspot-and-pipedrive.png"
heroImage: "/images/heroes/intelligence/automate-qualify-and-optimize-sales-with-hubspot-and-pipedrive.png"
relatedOpportunity: "/opportunities/how-to-build-an-ai-hubspot-sales-automation-agency-35k-45kmonth/"
---



## Prerequisites

*Section content pending review.*


## Step 1: Setup and Configuration  

**Goal:** Create the foundation that will let your AI‑driven sales engine communicate with both HubSpot and Pipedrive.  
**Time estimate:** 20–30 minutes.  

### 1.1 Create the Development Sandbox in HubSpot  

1. Log in to your HubSpot account.  
2. In the top‑right corner click **“Settings”** (gear icon).  
3. From the left‑hand menu select **“Integrations → API keys.”**  
4. Click **“Create API key.”**  
5. Enter a name (e.g., `SalesAutomationKey`) and click **“Generate.”**  
6. Copy the key – you will paste it into Replit later.  

*Check‑in:* Do you see the key in the list? If not, confirm you are on the **Portal‑level** and not a sub‑account.  

> **Error:** `HubSpot API key exceeded its usage limit.`  
> **Cause:** You have hit the free tier request cap.  
> **Fix:** Upgrade to the Starter plan (≈$50/month) or request a new key after a 24‑hour cooldown.

### 1.2 Create the Pipedrive Sandbox  

1. Log in to Pipedrive.  
2. Click your avatar → **“Account settings.”**  
3. Choose **“API”** from the sidebar.  
4. Click **“Generate new key.”**  
5. Name it `SalesAutomationPipedrive` and click **“Generate.”**  
6. Copy the key.  

*Check‑in:* Are you seeing the key in the list? If not, ensure you’re on the **Main account** and not a sub‑user.

> **Error:** `Invalid API key`  
> **Cause:** The key contains a trailing space.  
> **Fix:** Re‑copy without spaces or regenerate.

### 1.3 Spin up a Replit Workspace  

1. Navigate to [**Replit.com**](https://replit.com/refer/egwuokwor) and sign in or create an account.  
2. Click **“+ Create” → “New Repl.”**  
3. Choose **“Python (3.11)”** as the template.  
4. Name it `hubspot-pipedrive-automation`.  
5. Click **“Create Repl.”**  

The editor will show a default `main.py`. Replace its contents with the following skeleton to set environment variables:

```python
# main.py
import os
from hubspot import HubSpot
from hubspot.crm.objects import SimplePublicObjectInput
from pipedrive import Pipedrive
from pipedrive.client import Client

# HubSpot API key
os.environ["HUBSPOT_API_KEY"] = "<YOUR_HUBSPOT_KEY>"

# Pipedrive API key
os.environ["PIPEDRIVE_API_KEY"] = "<YOUR_PIPEDRIVE_KEY>"

# Instantiation
hubspot = HubSpot(api_key=os.getenv("HUBSPOT_API_KEY"))
pipedrive = Client(domain="api.pipedrive.com", api_token=os.getenv("PIPEDRIVE_API_KEY"))
```

*Check‑in:* The terminal should show a green checkmark next to the file.  
If you see `SyntaxError`, ensure you replaced `<YOUR_HUBSPOT_KEY>` and `<YOUR_PIPEDRIVE_KEY>` with the actual keys, not the angle brackets.

### 1.4 Install Required Packages  

Open the **Shell** tab in Replit and run:

```bash
pip install hubspot-api-client pipedrive-python
```

You should see:

```
Collecting hubspot-api-client
  Downloading hubspot_api_client-0.7.0.tar.gz (49 kB)
...
Successfully installed hubspot-api-client-0.7.0 pipedrive-python-0.4.0
```

*Check‑in:* Are the installations listed with `Successfully installed`? If you see `Could not find a version that satisfies the requirement`, upgrade pip:

```bash
pip install --upgrade pip
```

### 1.5 Verify Connectivity  

Add the following to `main.py`:

```python
# Verify HubSpot
try:
    contacts = hubspot.crm.contacts.basic_api.get_page(limit=1)
    print("HubSpot connection OK:", contacts)
except Exception as e:
    print("HubSpot error:", e)

# Verify Pipedrive
try:
    deals = pipedrive.deals.get_all(limit=1)
    print("Pipedrive connection OK:", deals)
except Exception as e:
    print("Pipedrive error:", e)
```

Run the script via the **Run** button. Expected output:

```
HubSpot connection OK: <HubSpotContactPage ...>
Pipedrive connection OK: <DealsResponse ...>
```

If you see `HubSpotError: 401 Unauthorized`, double‑check that the key is correct and that you’re using the **Portal API key**.

### 1.6 Create Directory Structure  

In the Replit file tree, create the following folders:

```
/src
    /hubspot
    /pipedrive
    /ai
/tests
    test_connection.py
```

Move `main.py` into `/src/ai`.  
Add a `README.md` at the root with the following header:

```
# HubSpot-Pipedrive AI Sales Automation

This repo contains the integration code that pulls leads from HubSpot, enriches them with AI (via Make.com), and pushes qualified deals into Pipedrive.
```

*Check‑in:* Do you see the folder structure? If not, click the **+ folder** icon and name each folder exactly as shown.

### 1.7 Configure Make.com to Receive Webhooks  

1. Go to [**Make.com**](https://www.make.com/en/register?pc=menshly) and create a new scenario.  
2. Add a **“Webhooks” → “Custom Webhook”** trigger.  
3. Click **“Add”** and name it `HubSpotLead`.  
4. Copy the generated URL (e.g., `https://hook.integromat.com/abcd1234`).  
5. In HubSpot, create a workflow:  
   - **Trigger:** New contact created.  
   - **Action:** “Send webhook” → paste the Make.com URL.  
   - Map required fields: `email`, `firstname`, `lastname`.  

When a new contact is created in HubSpot, Make.com will receive a JSON payload.  

*Check‑in:* Do you see the Webhook trigger in Make.com? If not, verify you selected **Custom Webhook** and not **Form**.  

> **Error:** `Webhook timeout`  
> **Cause:** Make.com scenario is paused.  
> **Fix:** Click **“Run once”** to activate and ensure the scenario is set to **“On demand

## Step 2: Build the Core System  

In this step we wire the data flow that powers the automated sales engine. We will:

1. Create a **HubSpot custom pipeline** that mirrors the stages in Pipedrive.  
2. Build a **Pipedrive webhook** that pushes deal updates into Make.com.  
3. Use **Make.com** to create a multi‑step scenario that:  
   - pulls the deal into a **Google Sheet** for audit,  
   - triggers an [**ElevenLabs**](https://elevenlabs.io/) voice‑to‑text transcription of the deal notes,  
   - updates the **HubSpot deal record** with the transcription, and  
   - sends a **Klaviyo** email to the owner if the deal is stuck in a “Negotiation” stage for >3 days.

Each block is followed by an interactive check‑in and a table of key settings.

---

### 1. Create the HubSpot Pipeline

1. Log into HubSpot → **Sales** → **Deals** → **Settings** → **Pipelines**.  
2. Click **Create pipeline**.  
3. **Pipeline name:** `Pipedrive Sync`  
   *Description:* Mirrors Pipedrive stages.  
4. Add the following stages in order:  
   1. Lead – `0%`  
   2. Qualified – `20%`  
   3. In‑Progress – `40%`  
   4. Negotiation – `60%`  
   5. Closed Won – `80%`  
   6. Closed Lost – `100%`  

   For each stage:  
   - Click **Add stage** → Name → **Save**.  

5. **Check‑in:** Do you see the `Pipedrive Sync` pipeline listed under your pipelines? It should show the six stages with the correct percentages.  
   *If not:* Go back to **Pipelines** → **Create pipeline** and repeat.

| Setting | Value |
|---------|-------|
| Pipeline name | `Pipedrive Sync` |
| Stage 1 | Lead – 0% |
| Stage 2 | Qualified – 20% |
| Stage 3 | In‑Progress – 40% |
| Stage 4 | Negotiation – 60% |
| Stage 5 | Closed Won – 80% |
| Stage 6 | Closed Lost – 100% |

---

### 2. Configure Pipedrive Webhook

1. Log into Pipedrive → **Tools & Apps** → **Webhooks**.  
2. Click **Add webhook**.  
3. **Webhook name:** `HubSpot Sync`  
4. **URL:** `https://hook.make.com/your-unique-endpoint` (replace `your-unique-endpoint` with the one generated in Make.com, see Step 3).  
5. **Events:** Select `Deal updated`, `Deal created`, and `Deal deleted`.  
6. **Save**.  

**Check‑in:** In Pipedrive’s **Webhooks** list you should now see `HubSpot Sync` with the URL you entered.  
*If you see an error such as “Invalid URL”* it means you copied the wrong Make.com endpoint; go back to Make.com and copy the correct one.

| Setting | Value |
|---------|-------|
| Webhook name | `HubSpot Sync` |
| URL | `https://hook.make.com/your-unique-endpoint` |
| Events | Deal updated, Deal created, Deal deleted |

---

### 3. Build the Make.com Scenario

1. Log into Make.com → **Create a new scenario**.  
2. **Add module** → Search for **Pipedrive** → **Watch Deals**.  
   - **API key:** `PD-xxxxxxxxxxxxxxxxx` (your Pipedrive API key).  
   - **Limit:** 50 deals per run.  
   - **Trigger type:** `Deal updated`.  

3. **Add module** → **Google Sheets** → **Create a row**.  
   - Spreadsheet: `Sales Audit Log`.  
   - Sheet: `Deals`.  
   - Column mapping:  
     - `Deal ID` → `{{deal.id}}`  
     - `Title` → `{{deal.title}}`  
     - `Stage` → `{{deal.stage_id}}`  
     - `Owner` → `{{deal.owner_id}}`  
     - `Last Updated` → `{{deal.updated_at}}`  

4. **Add module** → **Text to Speech** → **ElevenLabs – Convert Text to Audio**.  
   - **Audio format:** `mp3`  
   - **Voice:** `Matthew` (English US)  
   - **Text input:** `{{deal.notes[0].content}}` (first note).  

5. **Add module** → **HTTP** → **Make a request** (to HubSpot).  
   - **Method:** `PATCH`  
   - **URL:** `https://api.hubapi.com/crm/v3/objects/deals/{{deal.id}}`  
   - **Headers:**  
     - `Authorization: Bearer <HUBSPOT_API_KEY>`  
     - `Content-Type: application/json`  
   - **Body (JSON):**  
     ```json
     {
       "properties": {
         "dealname": "{{deal.title}}",
         "dealstage": "{{deal.stage_id}}",
         "hs_note_data": "{{deal.notes[0].content}}",
         "audio_url": "{{audio.url}}"
       }
     }
     ```  

6. **Add module** → **Klaviyo** → **Send Email**.  
   - **Trigger:** `If stage is Negotiation AND Days since last update > 3` (use a conditional router).  
   - **Email template:** `Deal Stuck Alert`  
   - **Recipient:** Deal owner email (`{{deal.owner.email}}`).  

7. **Save** and **Run once** to test.  

**Check‑in:** After running, you should see:  
- A new row in Google Sheets under `Sales Audit Log` → `Deals`.  
- An MP3 file created in your ElevenLabs account.  
- A PATCH request in Make.com’s execution history showing `200 OK`.  
- If the deal was in Negotiation >3 days, a Klaviyo email appears in your sent items.  

*If you see a 4xx error in the HTTP module:*  
- Verify the HubSpot API key and that the deal ID exists in HubSpot.  
- Ensure the JSON body keys match HubSpot’s property names (`dealname`, `dealstage`, etc.).  

| Module | Purpose | Key Parameters |
|--------|---------|----------------|
| Pipedrive – Watch Deals | Capture deal events | API key, Trigger type |
| Google Sheets

## Step 3: Test and Validate  
(Estimated effort: 10 – 15 minutes)

### 3.1 Trigger a Sample Lead in HubSpot  
1. **Login** to HubSpot → **Marketing** → **Lead Capture** → **Forms**.  
2. Open the **“Demo Request”** form we created in Step 2.  
3. Fill in the following test data:  
   * First name: *John*  
   * Last name: *Doe*  
   * Email: *johndoe_test@demo.com*  
   * Phone: *555‑123‑4567*  
   * Company: *Acme Corp*  
4. Click **Submit**.  
5. **Expected UI**: A green toast “Form submitted successfully” appears.  
6. **Interactive Check‑in**: Do you see the green toast? If not, verify you are on the **HubSpot CRM > Marketing > Lead Capture > Forms** page and that the form is published.

### 3.2 Verify HubSpot → Make.com Zap  
1. Open **Make.com** → **My scenario** → **HubSpot‑to‑Pipedrive**.  
2. Click **Run once**.  
3. In the **HubSpot trigger** window, confirm the latest record shows *johndoe_test@demo.com*.  
4. **Expected JSON** (excerpt):  
   ```json
   {
     "properties": {
       "firstname": "John",
       "lastname": "Doe",
       "email": "johndoe_test@demo.com",
       "phone": "555-123-4567",
       "company": "Acme Corp"
     }
   }
   ```  
5. **Interactive Check‑in**: Do you see the test lead in the trigger output? If not, ensure the **Trigger** module is set to **Watch Contacts** and the **Limit** is > 1.

### 3.3 Confirm Pipedrive Deal Creation  
1. Go to **Pipedrive** → **Deals** → **All deals**.  
2. Locate the deal titled **“Acme Corp – Demo Request”**.  
3. Open the deal and verify:  
   * **Stage** = *New*  
   * **Owner** = *Your user*  
   * **Value** = *$0* (default)  
4. **Expected output**: Deal card shows the correct owner and stage.  
5. **Interactive Check‑in**: Do the deal details match the test lead? If the deal is missing, double‑check the Make.com scenario’s **Create Deal** module has the correct field mapping.

### 3.4 Validate AI Qualification in Pipedrive  
1. In Pipedrive, open the **“Acme Corp – Demo Request”** deal.  
2. Click **Automation** → **Run** → **Qualify Lead** (the custom workflow created in Step 2).  
3. The system should send an **email** via **ActiveCampaign** to the lead asking for budget.  
4. **Expected email content**: Subject “Let’s Talk Budget” with CTA button “Set Budget”.  
5. **Interactive Check‑in**: Check your inbox for the test email. If you don’t receive it, confirm the ActiveCampaign integration in HubSpot is active and the **“Send Email”** module in Make.com has the correct campaign ID.

### 3.5 Test Follow‑up Voice Call (Vapi)  
1. In Pipedrive, click the **“Call”** button on the deal.  
2. The Vapi integration should trigger a **text‑to‑speech call**.  
3. **Expected behavior**: You receive a call with the script “Hi John, this is the AI sales assistant. Let’s discuss your needs.”  
4. **Interactive Check‑in**: Did the call play the expected script? If you hear “Invalid credentials”, ensure the Vapi API key is stored in Pipedrive’s **Integrations** > [**Vapi**](https://vapi.ai/) section.

### 3.6 Common Errors & Fixes  
| Error | Cause | Fix |
|-------|-------|-----|
| **Make.com “No records found”** | HubSpot form not publishing | Publish the form, then re‑run the scenario. |
| **Pipedrive deal missing fields** | Incorrect mapping in Make.com “Create Deal” module | Edit the module to map HubSpot properties to Pipedrive fields. |
| **ActiveCampaign email not sent** | API key expired | Re‑enter the key in HubSpot > Settings > Integrations > ActiveCampaign. |
| **Vapi audio not playing** | Incorrect phone number format | Use E.164 format (e.g., +15551234567). |

### 3.7 5‑Point Test Checklist  
Before moving to production, tick off each item:  

1. **Lead capture** – Form submits, HubSpot shows success toast.  
2. **Zap trigger** – Make.com shows the test lead in the trigger output.  
3. **Deal creation** – Pipedrive displays the new deal with correct owner and stage.  
4. **AI qualification** – ActiveCampaign email reaches the lead and includes CTA.  
5. **Voice follow‑up** – Vapi call rings and plays the scripted message.

If all five boxes are marked **✓**, your automation pipeline is fully validated and ready for live deployment.

## Step 4: Add Advanced Features  

In Step 4 we harden the pipeline, add AI enrichment, implement real‑time error handling, and set up smart routing that lets HubSpot and Pipedrive work together like a well‑tuned orchestra. All changes are made through the native UIs or via API calls that can be copied and pasted directly into your terminal or Replit notebook.

### 4.1 Enable HubSpot AI Enrichment (Lead Scoring + Smart Tags)

1. **Navigate to Lead Scoring**  
   - In HubSpot, click *Contacts* → *Lead Scoring* → *Create score*.  
   - Title the score **“AI‑Enhanced Lead Score”** and click *Create*.

2. **Add AI‑Driven Properties**  
   - Inside the score editor, click *Add property* → *Create new property*.  
   - Name it **“AI Interest Score”**, type *Number*, and scope *Contact*.  
   - Click *Save*.

3. **Configure the Score Formula**  
   - In the score editor, click *Add rule* → *Custom formula*.  
   - Paste the following formula:

     ```text
     if (AI_Interest_Score > 70) then 30
     else if (AI_Interest_Score > 40) then 15
     else 0
     ```

   - Click *Save rule* → *Save score*.

4. **Activate the Score via Zapier**  
   - In Zapier, create a new Zap:  
     *Trigger*: HubSpot → *New Contact*  
     *Action*: Make.com → *HTTP Request* (POST to `https://api.hubapi.com/contacts/v1/contact/vid/<CONTACT_ID>/profile?hapikey=YOUR_KEY`)  
     *Body* (JSON):

     ```json
     {
       "properties": [
         {
           "property": "ai_interest_score",
           "value": {{AI_Interest_Score}}
         }
       ]
     }
     ```

   - Test the Zap to ensure the property updates correctly.

**Check‑In**  
Do you see the new property “AI Interest Score” in the contact record? It should appear under *Properties* → *Custom*. If not, refresh the HubSpot UI or re‑run the Zap.

### 4.2 Set Up Error Handling in Pipedrive

1. **Create a “Failed Deals” Status**  
   - In Pipedrive, go to *Tools & Integration* → *Pipeline settings*.  
   - Add a new status called **“Failed Deals”** in the *Closed* column.

2. **Configure Webhooks for Failure Notification**  
   - In Pipedrive, click *Tools & Integration* → *Webhooks* → *Add webhook*.  
   - Set *Event* to *Deal updated*.  
   - URL: `https://api.telegram.org/botYOUR_BOT_TOKEN/sendMessage`  
   - Payload (JSON):

     ```json
     {
       "chat_id": "YOUR_CHAT_ID",
       "text": "Deal {{deal.title}} has moved to Failed Deals. Action required."
     }
     ```

   - Enable *Active* and *Save*.

3. **Add a Delay and Retry Logic Using Make.com**  
   - In Make.com, create a scenario:  
     *Trigger*: Pipedrive → *Deal Updated* (filter *status = Failed Deals*)  
     *Action*: Delay → *30 minutes*  
     *Action*: Pipedrive → *Update Deal* (set status to *In Progress*).  
   - Turn the scenario on.

**Check‑In**  
Move a test deal to *Failed Deals* and observe the Telegram notification. If you do not receive it, verify the bot token and chat ID, and ensure the webhook URL is reachable.

### 4.3 Smart Routing Between HubSpot and Pipedrive

1. **Create a HubSpot Workflow for Lead Routing**  
   - In HubSpot, go to *Automation* → *Workflows* → *Create workflow*.  
   - Choose *Contact-based* → *Start from scratch*.  
   - Name it **“Pipedrive Lead Router”**.

2. **Add Enrollment Triggers**  
   - Trigger: *Contact property changes* → *AI Interest Score* > 50.  
   - Set *Enrollment* to *One time per contact*.

3. **Add Action: Create Pipedrive Deal**  
   - Action type: *Pipedrive → Create a Deal*.  
   - Map HubSpot fields to Pipedrive:  
     - *Deal title* = `{{contact.firstname}} {{contact.lastname}} – AI Lead`  
     - *Deal value* = `{{contact.ai_interest_score}}`  
     - *Deal stage* = *New* (pipeline: *Sales*).

4. **Return Deal ID to HubSpot**  
   - Action: *HubSpot → Update contact property*.  
   - Property: *Pipedrive Deal ID* (create if needed).  
   - Value: `{{pipedrive_deal_id}}`.

5. **Activate the Workflow**  
   - Click *Review* → *Turn on*.

**Check‑In**  
Create a new contact with an AI Interest Score of 60. After 2–3 minutes you should see a new deal in Pipedrive and the contact record should have the *Pipedrive Deal ID* populated. If you don’t see it, confirm that the Pipedrive API key and the HubSpot integration have permission to create deals.

### 4.4 Final Validation and Monitoring

1. **Run a Full Flow Test**  
   - Using Replit, paste the following script to simulate a new contact creation:

     ```python
     import requests, json

     hubspot_url = "https://api.hubapi.com/contacts/v1/contact"
     payload = {
       "properties": [
         {"property": "firstname", "value": "Test"},
         {"property": "lastname", "value": "User"},
         {"property": "ai_interest_score", "value": 65}
       ]
     }
     headers = {"Content-Type": "application/json", "Authorization": "Bearer YOUR_HUBSPOT_TOKEN"}
     r = requests.post(hubspot_url, headers=headers, data=json.dumps(payload))
     print(r.json())
     ```

   - Observe that a new contact appears, the workflow triggers, and a deal is created in Pipedrive.

2. **Monitor with Grafana (Optional)**  
   - Set up a Grafana dashboard that pulls metrics from both HubSpot (via Make.com) and Pipedrive API to visualize deal pipeline health.  
   - Add panels for *Active Deals*, *Failed Deals*, and *Lead Score Distribution*.

**Error Handling**  
If you receive a `400 Bad Request` when creating a deal, check that the Pipedrive API key is correct and that the pipeline ID matches the one used in the workflow. For a `403 Forbidden`, ensure the HubSpot workflow has

## Step 5: Deploy to Production

Deploying the HubSpot‑Pipedrive integration to a live environment is the culmination of the build and testing phases. Follow these instructions exactly; any deviation will result in API throttling or data loss.

1. **Create a Dedicated Deployment Branch**  
   ```bash
   git checkout -b production
   git push origin production
   ```
   *Do you see a new branch named `production` in the GitHub UI?* If not, refresh the page.

2. **Configure Environment Variables for Production**  
   Open the `environment.yaml` file in Replit. Replace the staging keys with production keys:

   ```yaml
   HUBSPOT_CLIENT_ID: "a1b2c3d4e5f6g7h8"
   HUBSPOT_CLIENT_SECRET: "yz1234567890"
   HUBSPOT_REDIRECT_URI: "https://app.menshlyglobal.com/hubspot/callback"
   PIPEDRIVE_TOKEN: "pipedrive_prod_token_987654321"
   ```
   Save the file. Replit will prompt you to **Save & Commit**. Commit with the message `Deploy production keys`.

3. **Update the OAuth Flow**  
   In `src/auth.py`, change the redirect URI to match the production redirect:

   ```python
   redirect_uri = os.getenv("HUBSPOT_REDIRECT_URI")
   ```
   Confirm that the `redirect_uri` matches the one registered in the HubSpot developer console. In the HubSpot console, navigate to **Apps → Edit → OAuth → Redirect URLs** and ensure it contains `https://app.menshlyglobal.com/hubspot/callback`.

4. **Push to the Production Server**  
   Use Hostinger’s SSH endpoint. In the terminal, run:

   ```bash
   ssh root@production.menshlyglobal.com
   cd ~/menshly-hubspot-pipedrive
   git pull origin production
   ```
   *If you see `permission denied` errors, verify your SSH key is added to Hostinger under **Security → SSH Keys**.*

5. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
   *You should see output like `Collecting Flask==2.3.2`, `Requirement already satisfied`, etc.*

6. **Run Database Migrations**  
   ```bash
   flask db upgrade
   ```
   The terminal should return `Running upgrade ... OK`. If you see `ERROR: No such table: users`, run `flask db init` first.

7. **Start the Application**  
   ```bash
   gunicorn --workers 4 --bind 0.0.0.0:8000 wsgi:app
   ```
   *You should see `[2026-11-17 12:00:00 +0000] [1234] [INFO] Starting gunicorn*.  
   Verify by navigating to `https://app.menshlyglobal.com` in a browser. The login page should load without any 500 errors.

8. **Verify Data Sync**  
   - In HubSpot, go to **Reports → Dashboard → Custom Report Builder**. Create a report that pulls `Contact` data where `Lifecycle stage = Qualified`.  
   - In Pipedrive, check the **Deals** list for a new deal titled `Prospect – HubSpot Sync`.  
   If the deal appears, the sync is functioning.

9. **Set Up Webhooks for Real‑Time Updates**  
   In HubSpot, navigate to **Automation → Workflows → Create workflow → Triggered by API → Create a webhook**. Use the following payload URL:  
   `https://app.menshlyglobal.com/webhooks/hubspot`.  
   In the workflow, set the trigger to `Contact property changes → Lifecycle stage changes`.

   In Pipedrive, set up a webhook via the API:

   ```bash
   curl -X POST https://api.pipedrive.com/v1/webhooks?api_token=${PIPEDRIVE_TOKEN} \
   -H "Content-Type: application/json" \
   -d '{"name":"HubSpot Sync","url":"https://app.menshlyglobal.com/webhooks/pipedrive","event_types":["deal_updated"]}'
   ```
   *The response should contain `"success":true`.*

10. **Enable Monitoring and Alerting**  
    - Create a Zapier workflow that watches the `flask_app_logs` endpoint.  
    - If a log contains `"ERROR"`, send a Slack message to `#dev-alerts`.  
    - Set up a Make.com scenario to post a daily summary to your Beehiiv newsletter.

**If you see a 429 error after deployment, it means you’ve hit HubSpot’s rate limit.**  
Fix it by pausing the sync job for 60 seconds (`time.sleep(60)`) and retrying the request.

Your production environment is now live, fully integrated with HubSpot and Pipedrive, and ready to serve real clients. From here, focus on monitoring performance, refining the AI scoring model, and iterating on the user experience.

## Step 6: Scale and Grow  
**Objective:** Expand from serving a single client to 10 + clients while keeping margins above 45 %.  

| Milestone | Target Clients | Automation Layer | Resource Allocation | Margin Goal |
|-----------|----------------|------------------|---------------------|-------------|
| 1 | 1–2 | Manual Pipedrive setup | 1 junior sales engineer | 35 % |
| 2 | 3–5 | HubSpot → Pipedrive sync + email sequences | 1 engineer + 1 data analyst | 40 % |
| 3 | 6–10 | Full AI‑driven lead scoring + chatbot | 1 engineer + 1 AI specialist | 45 % |
| 4 | 11–20 | Multi‑channel nurturing + reporting | 2 engineers + 1 marketing lead | 48 % |
| 5 | 21+ | Franchise‑ready platform | 3 engineers + 2 ops | 50 % |

### 1. Hiring Plan  
1. **Junior Sales Engineer (Full‑time) – $50k /yr**  
   - *Role*: Onboard new clients, configure HubSpot pipelines, set up Pipedrive deal stages.  
   - *Tools*: HubSpot UI → “Automation” → “Workflows” → “Create workflow”.  
2. **Data Analyst (Part‑time 20 hrs/wk) – $30k /yr**  
   - *Role*: Build dashboards in HubSpot → “Reports” → “Custom report”.  
   - *Tools*: HubSpot → “Reports” → “Custom Report Builder” → drag “Deal Stage” + “Revenue”.  
3. **AI Specialist (Contract 10 hrs/wk) – $40k/yr**  
   - *Role*: Train Vapi voice agents, integrate ElevenLabs TTS, fine‑tune ChatGPT prompts.  

*Recruit via LinkedIn (use Apollo.io to find prospects) and post on remote‑job boards.*  

### 2. Automation Upgrades  
| Layer | Tool | Exact Settings | Expected Time‑Saved |
|-------|------|----------------|---------------------|
| Lead Intake | Make.com → HubSpot → Pipedrive | **Make.com workflow**: “HubSpot → Pipedrive” <br> - Trigger: *New Contact* <br> - Action: *Create Deal in Pipedrive* with stage “Qualified”. <br> - Frequency: *Instant* | 20 min/lead |
| Email Nurture | ActiveCampaign → HubSpot | **ActiveCampaign automation**: “New Pipedrive deal” <br> - Action: *Send email sequence* (3 emails, 2‑day gap). <br> - Conditional: *Only if contact has not opened previous email*. | 10 min/lead |
| Voicemail AI | Vapi + ElevenLabs | **Vapi script**: “If no reply after 3 days, trigger ElevenLabs TTS to record personalized voicemail”. <br> - Endpoint: `https://api.vapi.ai/v1/voice` <br> - Payload: `{ "prompt":"Hello {name}, we wanted to follow up…", "voice":"en-US-Wavenet-D" }` | 5 min/lead |
| Reporting | HubSpot → Google Data Studio | **Data Studio connector**: *HubSpot* → *Data Source* → *Report* “Monthly Pipeline Health” <br> - Fields: “Deal Stage”, “Closed Won”, “Revenue” <br> - Schedule: *Daily refresh at 6 AM* | 2 hrs/week |

> **Interactive Check‑in:** Open Make.com. If you don’t see the “Create workflow” button, ensure you’re in the “Automations” tab. If still missing, upgrade to the “Professional” tier ($52 / month).

### 3. Margin Improvements  
1. **Standardize Deal Templates** – Use HubSpot “Deal templates” with pre‑filled product pricing.  
   - *Path*: HubSpot → “Deals” → “Templates” → “Create template”.  
   - *Fields*: `{{product_price}}`, `{{discount}}`.  
2. **AI‑Generated Proposals** – Use Replit to build a lightweight Flask app that pulls data from HubSpot (API key) and renders PDF proposals in Canva.  
   - *API call*: `GET https://api.hubapi.com/contacts/v1/contact/vid/12345/profile?hapikey=demo`.  
   - *Result*: JSON with email, company, role. Feed into Canva “Template 5” via Canva API.  
3. **Automated Billing** – Connect Shopify to HubSpot via Zapier.  
   - *Zap*: Trigger: *New Shopify Order* → Action: *Create HubSpot Deal* with price = order total.  
   - *Cost*: Zapier “Professional” ($49 / month).  

> **Error scenario:** If Zapier shows “Authentication failed”, verify that the Shopify API key has “read” permissions. Re‑authorize via Zapier > “Connected Accounts”.

### 4. Go‑Live Checklist  
1. **Client Onboarding SOP** – Document in [Notion](https://notion.so/), share link with engineers.  
2. **Security** – Enable 2FA on all accounts (HubSpot → Settings → Security).  
3. **Monitoring** – Set up Slack alerts via Make.com: *If any workflow fails, send message to #ops*.  

**Result:** By following this plan, you’ll deliver a fully automated, AI‑enhanced sales pipeline that scales naturally, reduces manual effort by 70 %, and pushes gross margin to 48 %+ with 10 + clients by month 12.

## Cost Breakdown

| Item | Free Tier | Paid Tier | When to Upgrade |
|------|-----------|-----------|-----------------|
| **HubSpot Marketing Hub** | Free (contacts, email, forms) | Starter $45 / mo (1 000 mktg contacts) | When you exceed 1 000 marketing contacts or need email templates & A/B testing |
| **HubSpot Sales Hub** | Free (contact & deal pipelines) | Professional $65 / mo (10 SAs) | When you need custom deal stages, meeting scheduling, or advanced reporting |
| **HubSpot CMS** | Free (single page) | Professional $100 / mo (10 sites) | When you require custom templates, CMS API, or SSL |
| **Pipedrive** | Free (1 user, 5 deals) | Standard $33 / mo (1 user, unlimited deals) | When you need more users or advanced reporting |
| **Zapier** | Free (100 tasks/month) | Starter $19.99 / mo (750 tasks) | When your workflow exceeds 1 000 tasks/month |
| **Make.com** | Free (1 000 operations/month) | Basic $49.99 / mo (10 000 ops) | When you need more operations or premium connectors |
| **Calendly** | Free (1 calendar) | Premium $12 / mo (unlimited calendars) | When you need multiple booking types or custom branding |
| **ElevenLabs** | Free (5 hrs audio/month) | Pro $20 / mo (25 hrs) | When you generate >10 hrs of AI voice per month |
| [**Canva Pro**](https://www.canva.com/) | Free (limited templates) | Pro $12.99 / mo (unlimited templates & brand kit) | When you need brand kit & team collaboration |
| **ActiveCampaign** | Free (1 user, 500 contacts) | Lite $15 / mo (1 user, 500 contacts) | When you need automation workflows beyond 500 contacts |

### Monthly Cost Analysis

| Scale | Monthly Cost |
|-------|--------------|
| **Solo** (1 HubSpot user, 1 Pipedrive user, 1 Zapier task set, 1 Make.com plan, 1 Calendly) | **$124.99** (HubSpot Sales $65 + Pipedrive $33 + Zapier $19.99 + Make.com $49.99 + Calendly $12) |
| **5 Clients** (5 HubSpot users, 5 Pipedrive users, 5 Zapier tasks, 5 Make.com, 5 Calendly) | **$624.95** (HubSpot $325 + Pipedrive $165 + Zapier $99.95 + Make.com $249.95 + Calendly $60) |
| **10+ Clients** (10 HubSpot users, 10 Pipedrive users, 10 Zapier tasks, 10 Make.com, 10 Calendly) | **$1,224.90** (HubSpot $650 + Pipedrive $330 + Zapier $199.90 + Make.com $499.90 + Calendly $120) |

*All prices are listed in USD and are the lowest‑tier paid plans that support the required features. Prices may fluctuate with promotional discounts or currency changes.*

---

**Key Takeaways**

- **Start with the Free tiers**: For a solo operator, the free HubSpot Marketing, Sales, and CMS plans combined with the Pipedrive free plan will cover basic lead capture and deal tracking.
- **Upgrade when contact volume or automation complexity grows**: HubSpot’s Starter/Professional tiers unlock A/B testing, scheduled emails, and advanced reporting—critical when managing >1 000 contacts.
- **Leverage Make.com or Zapier for orchestration**: The free Make.com tier allows 1 000 operations/month; upgrade to Basic when you hit 5 000 ops/month. Zapier Starter gives you 750 tasks; upgrade when you exceed 1 000 tasks/month.
- **Add Calendly premium** only if you need multiple booking types or custom branding—otherwise the free version suffices.
- **Use ElevenLabs Pro** if you plan to synthesize >10 hrs of AI voice per month; otherwise the free tier (5 hrs) is adequate.

By monitoring contact counts, task usage, and feature requirements, you can shift between tiers without over‑paying while still delivering a robust AI‑powered sales automation stack.

## Production Checklist

*Section content pending review.*


## What to Do Next

**1. Integrate HubSpot with Make.com for Lead Scoring Automation**  
Open Make.com, create a new scenario, and add the “HubSpot → New Contact” trigger. Set “Trigger Mode” to **Instant** and map the email, company name, and lifecycle stage fields. Add a **Filter** module that checks if the contact’s “Lead Score” (a custom property you’ll create in HubSpot) is below 30. If true, route to an **Email** module that sends a personalized nurture email via HubSpot’s transactional email service. In HubSpot, navigate to **Settings → Properties → Create Property → Type: Number → Default Value: 0**. In Make.com, use the “HubSpot → Update Contact” action to increment the Lead Score by 10 each time an email opens (track opens via HubSpot’s engagement API). Do you see the new property in HubSpot? If not, verify that you’re in the right **Account** under **Settings → Properties**.  

**2. Sync Pipedrive Deals with Klaviyo Segments for Post‑Sale Follow‑Up**  
In Pipedrive, go to **Tools & Apps → API → Generate API Token**. Copy the token. In Klaviyo, navigate to **Account → Settings → Integrations → API Keys** and create a new private API key. Use Zapier (or Make.com) to create a trigger: **Pipedrive → New Deal**. Map deal stage, revenue, and contact email to Klaviyo’s “Prospect” event. Add a filter: **Deal Stage = “Closed Won”**. Then send a “Thank You” email series via Klaviyo’s flow editor. Ensure the email subject reads “Thank You from Menshly”, and the body contains a link to a [**Beehiiv**](https://beehiiv.com/) survey for NPS scoring.  

**3. Leverage Pipedrive’s AI Pipeline Insights with Midjourney for Visual Dashboards**  
Export your Pipedrive pipeline data to a CSV via **Pipedrive → Settings → Data Export**. In Replit, install the `pandas` and `matplotlib` libraries, and load the CSV. Generate a heatmap of deal velocity using `seaborn`. Export the figure as PNG. Use Midjourney (via its Discord bot) to create a stylized version of the heatmap: type `!imagine /heatmap of sales pipeline, high contrast, modern minimalistic`. Replace the original PNG in your Notion dashboard with the Midjourney output.  

**4. Automate Voice‑to‑Text Follow‑Ups with ElevenLabs and Vapi**  
Set up an ElevenLabs account, generate a voice model ID. In Vapi, create a **Voice Agent** that listens for new Pipedrive contacts. Configure the agent’s “On New Contact” trigger to call ElevenLabs’ **Speech-to-Text** endpoint (`POST https://api.elevenlabs.io/v1/speech/to_text`). Parse the response for keywords like “interested” or “budget”. If detected, enqueue a Vapi outbound call script that uses the **Text-to-Speech** endpoint to deliver a pre‑recorded pitch. In HubSpot, add the call log via **HubSpot → Log Call**. Verify the call status indicator turns to **Completed** after the call.  

**5. Expand with ActiveCampaign for Lifecycle Marketing**  
Create an ActiveCampaign account, import your HubSpot contact list via the **ActiveCampaign → Import Contacts** module (CSV import). Map custom fields such as “HubSpot Lead Score” to ActiveCampaign’s custom field “hs_lead_score”. Build a **Automation** that triggers when “hs_lead_score” > 70 and sends a targeted upsell email. In the email editor, embed a Calendly link for a discovery call. Ensure the Calendly event type is set to **30‑minute Discovery** under **Calendly → Event Types → 30‑Minute Discovery**.  

**Next Reading**: Dive deeper into AI‑driven lead qualification in our article on **“AI Lead Scoring with HubSpot and Make.com”** (link to Menshly content).

Ready to understand the full business opportunity? Read our [opportunity deep-dive]({< ref "/opportunities/how-to-build-an-ai-hubspot-sales-automation-agency-35k-45kmonth.md" >}).


## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
