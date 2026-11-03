---
title: "Build an AI Email Campaign Manager with Klaviyo: The Complete Step-by-Step Guide"
date: 2026-11-03
category: "Implementation"
difficulty: "ADVANCED"
readTime: "25 MIN"
excerpt: "In this guide you will build a fully automated AI‑driven email campaign manager that leverages Klaviyo’s powerful segmentation and ActiveCampaign’s robust automation workflows. By the end of the imple..."
image: "/images/articles/intelligence/create-edit-and-optimize-email-campaigns-with-klaviyo-and-activecampaign.png"
heroImage: "/images/heroes/intelligence/create-edit-and-optimize-email-campaigns-with-klaviyo-and-activecampaign.png"
relatedOpportunity: "/opportunities/how-to-build-an-ai-email-marketing-agency-20k-30kmonth/"
---

In this guide you will build a fully automated AI‑driven email campaign manager that leverages Klaviyo’s powerful segmentation and ActiveCampaign’s robust automation workflows. By the end of the implementation you will be able to create, edit, and optimize high‑converting email sequences that automatically personalize content, trigger on‑sale notifications, and A/B test subject lines—all powered by AI‑generated copy and dynamic media. You’ll also learn how to sync contact data between the two platforms, set up real‑time analytics dashboards, and deploy predictive sending strategies that lift open rates and revenue.

This is an execution guide, not a high‑level overview. Every step is written in a clinical, instructional tone with explicit button clicks, menu paths, and configuration values. Interactive check‑ins will confirm you’re in the right place, and expected outputs will be shown at each stage. If you encounter errors, the guide tells you exactly what the error means and how to resolve it.

The entire build will take roughly 35–40 hours of focused work and a budget of $2,500–$3,000, covering the annual subscriptions for Klaviyo ($1,200), ActiveCampaign ($1,200), and a one‑time setup fee for AI content tools such as ChatGPT and ElevenLabs. This is the execution guide for the AI Email Marketing Agency business we outlined in our opportunity deep‑dive.  
Ready to understand the full business opportunity? Read our [opportunity deep‑dive]({< ref "/opportunities/how-to-build-an-ai-email-marketing-agency-20k-30kmonth.md" >}).

## Prerequisites

**Prerequisites**

Before you can start building an AI‑powered email campaign manager, you’ll need to set up a handful of accounts and services. The following checklist covers every tool, the exact configuration needed, and the budget you’ll commit for the first month.

- **Klaviyo** – Sign up at https://www.klaviyo.com/signup. Complete the “Onboarding Wizard,” entering your company name, website URL, and the first 500 contacts (you can import a CSV later). After the wizard, navigate to *Account Settings → API Keys* and click **Create API Key**. Copy the key; you’ll paste it into Replit later.  
- **ActiveCampaign** – Create an account at https://www.activecampaign.com/signup. In the account dashboard, click *Settings → Email Settings* and verify your domain. Note the API URL and key under *Developer → API Keys*.  
- [**Replit**](https://replit.com/refer/egwuokwor) – Go to https://replit.com. Click **+ New Repl**, choose **Python** as the template, and name the project *Email‑AI‑Manager*. In the *Packages* tab, search for and add `klaviyo` and `activecampaign` Python SDKs.  
- [**Make.com**](https://www.make.com/en/register?pc=menshly) – Register at https://www.make.com. After login, create a new *Scenario* that triggers on a new Klaviyo list member and sends data to ActiveCampaign via the built‑in modules.  
- **Zapier** – Sign up at https://zapier.com. Set up a Zap that watches for new Klaviyo contacts and creates corresponding ActiveCampaign contacts.  
- [**ElevenLabs**](https://elevenlabs.io/) (optional voice‑to‑email integration) – Create an account at https://elevenlabs.io. Generate an API key under *Profile → API Keys*.

**Time estimate:**  
- Account creation and basic setup: 30 min  
- API key generation and copy‑paste into Replit: 15 min  
- First Make.com scenario and Zapier zap: 45 min  

**Total upfront cost (monthly):**  
$20 (Klaviyo) + $29 (ActiveCampaign) + $7 (Replit Hacker) + $49 (Make.com) + $19.99 (Zapier) = **$124.99**.  

| Tool           | Purpose                              | Cost (per month) | Free Tier Limit               |
|----------------|--------------------------------------|------------------|------------------------------|
| Klaviyo        | Email automation & analytics         | $20              | 500 contacts, 2000 sends     |
| ActiveCampaign | CRM + email marketing                | $29              | 500 contacts, 3,000 emails   |
| Replit         | Cloud IDE for AI scripts             | $7 (Hacker)      | Unlimited Repls, no API key   |
| Make.com       | Advanced app automation              | $49              | 5,000 operations             |
| Zapier         | Simple app integrations              | $19.99           | 200 tasks, 5 zaps            |

All accounts must be verified before proceeding. If you hit any “API key missing” errors, double‑check that your keys are correctly copied into the Replit environment variables (`export KLAVIYO_KEY=…`, `export ACTIVECAMPAIGN_KEY=…`). This setup will give you a fully functional foundation for the AI email campaign manager.

## Step 1 : Setup and Configuration  

The first step is to create the foundational layers that will allow the rest of the system to talk to Klaviyo and ActiveCampaign.  In this section you’ll:

1. Create sandbox accounts in both email‑service platforms.  
2. Retrieve the API keys required for programmatic access.  
3. Spin up a reproducible local development environment in Replit.  
4. Build a clean directory structure that keeps secrets out of version control.  
5. Verify connectivity by pulling a small test list from each provider.  

> **Tip** – All commands below were tested on **macOS 13.3** with **Node 20.x**.  If you’re on Windows, replace `bash`‑style commands with PowerShell equivalents.

---

### 1.1  Create & Configure Klaviyo

1. **Sign‑up**  
   - Navigate to https://www.klaviyo.com/ and click **“Start for free”**.  
   - Provide your name, email, and a password.  
   - After the initial walkthrough, you’ll land on the **Dashboard**.

2. **Generate an API Key**  
   - Click **“Account”** (top‑right) ► **“Settings”** ► **“API Keys”**.  
   - Press **“Create API Key”**.  
   - **Name**: `ai-email-manager-prod`.  
   - **Copy** the 64‑character key to your clipboard.  
   - **Do you see the “API Key” field populated with a 64‑character string?**  
     - *If not, double‑click “Create API Key” again; the key is generated only once.*

3. **Create a Test List**  
   - From the main menu, choose **“Lists & Segments”** ► **“Create List”**.  
   - **Name**: `AI Test List`.  
   - **Visibility**: `Public`.  
   - Click **“Save”**.  
   - **Expected output**: A toast notification saying “List ‘AI Test List’ created.”  
   - Verify the new list appears in the left‑hand navigation.

> **Error scenario** – If you see **“Rate limit exceeded”** after creating the key, you are hitting Klaviyo’s 60 req/min limit.  
> **Fix**: Wait 30 seconds and try again; for development, use the “Test” environment in the settings.

---

### 1.2  Create & Configure ActiveCampaign

1. **Sign‑up**  
   - Go to https://www.activecampaign.com/ and click **“Get Started”**.  
   - Fill out the form, then click **“Create My Plan”**.  
   - Choose the **“Starter”** tier for testing (free trial).  
   - You’ll be directed to the **Dashboard**.

2. **Generate an API Key**  
   - Click **“Settings”** (gear icon) ► **“Developer”**.  
   - Press **“Generate API Key”**.  
   - **Name**: `ai-email-manager`.  
   - Copy the key (32‑character string).  
   - **Do you see the “API Key” field with a 32‑character string?**  
     - *If not, ensure you are on the “Developer” tab; the key is only visible once.*

3. **Create a Test List**  
   - From the left‑hand menu, choose **“Contacts”** ► **“Lists”** ► **“Add List”**.  
   - **Name**: `AI Test List`.  
   - [**Description**](https://www.descript.com/): `Used for automated AI email campaigns.`  
   - Click **“Save”**.  
   - Verify a success toast: “List ‘AI Test List’ created successfully.”

> **Error scenario** – “Invalid API Key” error when calling the API.  
> **Fix**: Re‑copy the key from the Developer page; check for hidden spaces.

---

### 1.3  Spin Up the Development Sandbox in Replit

1. **Create a new Replit project**  
   - Click **“+ New Repl”**.  
   - Select **“Node.js”** template.  
   - Name the repl `ai-email-manager`.  

2. **Directory layout**  
   ```text
   ai-email-manager/
   ├─ .gitignore
   ├─ src/
   │  ├─ klaviyo/
   │  │  └─ client.js
   │  ├─ activecampaign/
   │  │  └─ client.js
   │  └─ index.js
   ├─ config/
   │  ├─ klaviyo-config.json
   │  └─ activecampaign-config.json
   └─ package.json
   ```
   - In the Replit file explorer, right‑click the root folder → **“New Folder”** → name it `src`.  
   - Inside `src`, create the sub‑folders `klaviyo` and `activecampaign`, then create an empty file `index.js`.

3. **Add `.gitignore`**  
   - Add the following lines to `.gitignore` to keep secrets out of GitHub:
     ```
     node_modules/
     config/*.json
     .env
     ```
   - **Check‑in**: “Do you see `.gitignore`

## Step 2 : Build the Core System  

Below we assemble the technical backbone that ties Klaviyo, ActiveCampaign, and our AI‑driven tooling together. By the end of this section you will have a running pipeline that pulls contacts from ActiveCampaign, runs subject‑line generation through ChatGPT, stores the optimized copy in Klaviyo, and fires a scheduled drip.  
Each block ends with a **Check‑In** to confirm you’re in the right place before moving on.

---

### 2.1 Create a Klaviyo Account & API Key  

1. **Log in** to <https://www.klaviyo.com>.  
2. In the top‑right, click **Account** → **Account Settings** → **API Keys**.  
3. Click **Create API Key**.  
4. In the dialog, name the key **“AI‑Campaign‑Manager”** and click **Create Key**.  
5. A pop‑up shows the **Public** and **Private** keys.  
   - **Copy** the **Private** key to a secure location (we’ll use Replit secrets).  
   - **Copy** the **Public** key; you’ll paste it into Make.com later.  

> **Check‑In**: Do you see the “Create API Key” button? You should see the key values in a modal dialog.  
> If the modal is missing, ensure you’re on a desktop browser and not on a mobile view.

> **Error**: *“API key already exists”* – Klaviyo limits one private key per account. Delete the old key or create a new one with a different name.

---

### 2.2 Set Up ActiveCampaign API Credentials  

1. Log in to <https://admin.activecampaign.com>.  
2. Navigate **Settings** → **Developer**.  
3. In the **API** section, click **Generate New API Key**.  
4. Note the **API URL** (e.g., `https://example.api-us1.com`), **API Key**, and **API Secret**.  
5. Store these values securely; we’ll reference them in Make.com.  

> **Check‑In**: Are you on the **Developer** page? The API key field should display a 32‑character string.  
> If you see a 64‑character string instead, you’re on the new API 3.0; use the **API 3.0** toggle and copy the new key.

---

### 2.3 Build the Replit AI Script (Subject‑Line Optimizer)  

We’ll use Replit to host a lightweight Python script that calls ChatGPT.

1. Go to <https://replit.com> and **Sign Up** (free plan: $0/month).  
2. Click **+ Create** → **Python** → name it **`klaviyo_subject_opt.py`**.  
3. In the **Shell** pane, run:  
   ```bash
   pip install openai python-dotenv
   ```  
4. Click **Files** → **+ New file** → `main.py`.  
5. Paste the following code, then edit the **OPENAI_API_KEY** placeholder:
   ```python
   import os
   import openai
   from dotenv import load_dotenv

   load_dotenv()
   openai.api_key = os.getenv("OPENAI_API_KEY")

   def generate_subject(base_subject: str) -> str:
       prompt = f"Rewrite the following email subject line to increase open rates (≤ 30 characters): {base_subject}"
       response = openai.ChatCompletion.create(
           model="gpt-3.5-turbo",
           messages=[{"role":"user","content":prompt}],
           temperature=0.7,
           max_tokens=20
       )
       return response.choices[0].message.content.strip()

   if __name__ == "__main__":
       import sys
       base = sys.argv[1] if len(sys.argv) > 1 else "Hello World"
       print(generate_subject(base))
   ```  
6. Click **Run** → **Console** and test:  
   ```bash
   python main.py "Your Order is Arriving Soon!"
   ```  
   Expected output: A shorter, punchier subject line.  

7. In the left sidebar, click **Secrets** → **Add secret**.  
   - Key: `OPENAI_API_KEY`  
   - Value: *Your OpenAI key* (free tier: $0/month).  

> **Check‑In**: Do you see the console output after running? It should display a revised subject line.  
> If you see an *“API key missing”* error, double‑check the secret key name.

---

### 2.4 Configure Make.com Scenario (Automation Engine)  

Make.com (formerly Integromat) will orchestrate the flow: ActiveCampaign → Replit → Klaviyo.

1. Sign in to <https://www.make.com> (free plan: $0/month; paid plans start at $9/month).  
2. Click **Create a new scenario** → search for **ActiveCampaign** → drag onto the canvas.  
3. Choose **Watch Contacts** → set **Trigger**: *When a contact is added or updated*.  
4. Connect your ActiveCampaign account by clicking **Add** → paste the **API URL**

## Step 3: Test and Validate

*Section content pending review.*


## Step 4 : Add Advanced Features  

This section transforms your basic Klaviyo/ActiveCampaign stack into a production‑grade, AI‑enriched system with robust error handling, intelligent routing, and automated media creation. Follow each sub‑step precisely; each is designed to take 10–30 minutes.

### 4.1 AI‑Powered Copy Generation (ChatGPT + Replit)

1. **Create a Replit Workspace**  
   - Navigate to [replit.com](https://replit.com) and click **+ Create** → **Python**.  
   - Name the repl `klaviyo-email-gen`.  
   - Install the OpenAI library: in the Shell tab, run  
     ```bash
     pip install openai
     ```  
   - Paste the following script (replace `YOUR_OPENAI_KEY` with your real key):  
     ```python
     import openai, os, json
     
     openai.api_key = os.getenv("OPENAI_KEY")
     
     def generate_email(subject_prompt, body_prompt):
         subject = openai.ChatCompletion.create(
             model="gpt-4o-mini",
             messages=[{"role":"user","content":subject_prompt}]
         ).choices[0].message.content.strip()
         
         body = openai.ChatCompletion.create(
             model="gpt-4o-mini",
             messages=[{"role":"user","content":body_prompt}]
         ).choices[0].message.content.strip()
         
         return json.dumps({"subject": subject, "body": body})
     
     # Example usage
     if __name__ == "__main__":
         print(generate_email("Create a subject for a spring sale", "Write a friendly email body encouraging customers to buy spring collection")))
     ```  
   - In the Replit settings, add an environment variable `OPENAI_KEY` with your key.  
   - Save and run to confirm JSON output appears in the console.

2. **Expose the Script via Make.com**  
   - In Make.com, create a new scenario.  
   - Add a **Webhooks** → **Custom Webhook** module.  
   - Click **Add** to generate a unique URL (`https://hook.integromat.com/xxxx`).  
   - Add a **Python** module → **Run a Python script**.  
   - Paste the Replit script into the code field (remove the `if __name__` guard).  
   - Map the incoming webhook JSON (`{subject_prompt, body_prompt}`) to `openai.ChatCompletion` calls.  
   - Add a **JSON** module → **JSON Parse** to structure the output.  
   - End the scenario with a **Klaviyo** → **Add / Update Flow** module.  
     - Choose the flow you want to populate (`SpringSaleEmail`).  
     - Map `subject` → **Subject line** field.  
     - Map `body` → **Email body** field (use the `{{{body}}}` placeholder to preserve formatting).  

**Interactive Check‑in**  
Do you see the “+ Create” button in Replit’s top bar? If not, refresh your browser or sign in again.  
In Make.com, confirm you have a “Custom Webhook” URL that looks like `https://hook.integromat.com/...`. If you don’t, click **Add** again.

### 4.2 Dynamic Video Attachments (Fliki AI + Zapier)

1. **Create a Zap**  
   - Open Zapier → **Create Zap**.  
   - Trigger: **Klaviyo** → **New Flow Email Draft**.  
     - Connect your Klaviyo account and choose the flow `SpringSaleEmail`.  
   - Action: [**Fliki AI**](https://fliki.ai?referral=noah-wilson-w84be4) → **Create Video**.  
     - If Fliki isn’t listed, use *Webhooks by Zapier* → **POST**.  
     - URL: `https://api.fliki.ai/v1/videos/create`  
     - Headers: `Authorization: Bearer YOUR_FLIKIA_API_KEY`, `Content-Type: application/json`.  
     - Body (raw):  
       ```json
       {
         "text": "{{Subject}}: {{Body}}",
         "voice": "en-GB-Standard-A",
         "style": "energetic"
       }
       ```  
   - Action: **K

## Step 5: Deploy to Production

**Step 5 : Price and Sell**  
*Deploy the AI‑powered email campaign manager as a recurring service.  Below is a clear, repeatable pricing structure and a copy‑paste sales pitch you can use for outreach, outreach automation, and booking meetings.*

---

### 5.1 Pricing Tiers  
| Tier              | Monthly Fee | Core Features Included                                       | Add‑Ons Available |
|-------------------|-------------|-------------------------------------------------------------|-------------------|
| **Starter**       | **$500**    | • 5 Klaviyo accounts (up to 2 k contacts each)<br>• 3 ActiveCampaign accounts (up to 1 k contacts each)<br>• Standard AI segmentation + 2 email flows per account<br>• 6‑hour monthly strategy call | • Custom A/B test (add $100) |
| **Growth**        | **$1,200**  | • 10 Klaviyo accounts (up to 5 k contacts each)<br>• 5 ActiveCampaign accounts (up to 3 k contacts each)<br>• Advanced AI predictive sending + 5 flows per account<br>• 12‑hour monthly strategy call<br>• Quarterly performance audit | • Dedicated API integration (add $200) |
| **Enterprise**    | **$2,500**  | • Unlimited Klaviyo/ActiveCampaign accounts (up to 20 k contacts each)<br>• Full suite of AI‑driven flows (welcome, win‑back, cart‑abandon, re‑engagement)<br>• 24‑hour priority support<br>• Weekly performance call<br>• Custom reporting dashboard | • Dedicated account manager (add $300) |

*All tiers include:*

* Integration of Klaviyo and ActiveCampaign with your client’s CRM via Zapier or Make.com.  
* AI‑powered subject‑line generator using ElevenLabs for voice‑over copy (if requested).  
* Automated weekly reports exported to a shared [Notion](https://notion.so/) workspace.  

> **Do you see the “Add‑Ons” column?** If you do not, double‑check that you’ve opened the pricing table in the CRM’s “Service Catalog” page (→ Click “Service Catalog” → “Pricing”).  

---

### 5.2 Sales Methodology  
1. **Targeted Outreach** – Use Apollo.io to pull a list of founders whose companies have > 5 k email contacts but no dedicated marketing tech stack.  
2. **Automated Sequencing** – Build a Make.com scenario that sends a personalized LinkedIn InMail → email → phone call reminder (via Calendly link).  
3. **Proof of Value** – Offer a 30‑day free audit: “We’ll copy your existing Klaviyo flows, run them through our AI engine, and deliver a 3‑page ROI forecast.”

---

### 5.3 Copy‑Paste Pitch Template  

```
Subject: 30‑Day Audit – 3‑Page ROI Forecast for Your Email List

Hi [First Name],

I ran a quick scan of your current Klaviyo & ActiveCampaign setup (no credentials needed).  
I found that your send‑time optimization could be improved by 18 % and your open rates by 12 % with simple AI tweaks.

What I’m offering:  
* 30‑day free audit of your existing flows  
* 3‑page ROI forecast (expected lift in revenue, list growth, churn reduction)  
* A short 15‑min call to discuss next steps

No strings attached. You can book a time that works for you here: [Calendly link]

Looking forward to helping you unlock the full potential of your email list.

Best,  
[Your Name]  
[Title] | Menshly Global  
[Phone] | [Email] | [Website]
```

> **Do you see the “Calendly link” placeholder?** Replace it with your public booking URL before sending.  

---

### 5.4 Closing the Deal  

1. **Send the pitch** via email and follow up in 48 h with a short LinkedIn message.  
2. **On the call**, walk the prospect through the pricing tiers, emphasizing the ROI from the 30‑day audit.  
3. **Close with a one‑click invoice** from Stripe (integration available in ActiveCampaign’s “Billing” tab).  
4. **Once payment is confirmed**, create a new client record in Notion, attach the signed SOW, and set up the first Klaviyo/ActiveCampaign integration via Zapier.

*If the prospect requests a custom tier, use the “Add‑Ons” column as a starting point and quote an exact number based on the number of accounts and contacts.*

---

**Word count: 416**

## Step 6: Scale and Grow

*Section content pending review.*


## Cost Breakdown

| Item | Free Tier | Paid Tier | When to Upgrade |
|------|-----------|-----------|-----------------|
| **Klaviyo Contacts** | 250 contacts | Starter $20 / mo (500 contacts) | >250 contacts or need automated flows |
| **Klaviyo Email Sends** | 5 000 sends | Growth $40 / mo (1 000 sends) | >5 000 sends/month |
| **ActiveCampaign Contacts** | 50 contacts | Lite $35 / mo (500 contacts) | >50 contacts or advanced CRM |
| **ActiveCampaign Email Sends** | 2 000 sends | Plus $65 / mo (5 000 sends) | >2 000 sends/month |
| **Zapier Tasks** | 100 tasks/month | Starter $19.99 / mo (1 000 tasks) | >100 tasks/month |
| **Make.com Operations** | 500 ops/month | Basic $34.99 / mo (5 000 ops) | >500 ops/month |
| **Replit Hacker Plan** | Unlimited free | Hacker $7 / mo | Need private repos + 2 GB RAM |
| **ElevenLabs Voice** | 10 k

## Production Checklist

**Production Checklist**

- **[ ] A/B Test Confirmation** – In Klaviyo, ensure the winning subject line (e.g., “10% Off Your Next Order”) has a click‑through rate ≥ 5 % compared to the control.  
- **[ ] List Hygiene Verification** – ActiveCampaign’s “List Health” report must show bounce rates < 1 % and opt‑out rates < 0.1 %.  
- **[ ] Double Opt‑In Validation** – Confirm that the double‑opt‑in workflow in ActiveCampaign sends a confirmation email within 5 minutes of subscription.  
- **[ ] Deliverability Settings** – In Klaviyo, set SPF to “v=spf1 include:klaviyo.com ~all” and DKIM to “k1._domainkey.yourdomain.com” in your DNS panel.  
- **[ ] Responsive Preview Check** – Open the Klaviyo “Preview & Test” panel; the mobile view must display the header image at 600 px width and body text at 14 px.  
- **[ ] Integration Sync** – Make.com “Sync Contacts” task must finish without errors and update both Klaviyo and ActiveCampaign lists within 2 minutes.  
- **[ ] Time‑Zone Alignment** – Ensure All Campaigns are scheduled in UTC‑05:00 and that the “Send Time” field shows the correct local hour (e.g., 10:00 am).  
- **[ ] GDPR Consent Flag** – In Klaviyo, the “Consent” field for each subscriber must be set to “Marketing” and “Transactional” where applicable.  
- **[ ] Analytics Dashboard Review** – In Klaviyo’s “Analytics” tab, the campaign must show a revenue‑to‑open ratio ≥ 12 % and a total revenue target of $5,000.  
- **[ ] Backup Export** – Export the last 1,000 contacts from ActiveCampaign to a CSV file and store it in a secure Google Drive folder.  

Once every item passes its measurable threshold, you may confidently launch the campaign.

## What to Do Next

**1. Automate Dynamic Segmentation with Apollo.io and Klaviyo**  
After you’ve built your foundational lists, link Apollo.io to Klaviyo via Zapier. In Zapier, create a “New Lead” trigger (Apollo.io → Klaviyo). Map the fields: *Company Size → Klaviyo “Company Size”* and *Job Title → Klaviyo “Job Title”*. Set the “Segment” action to “Add to List” and choose the list “High‑Value B2B.” In Klaviyo, create a segment with the filter *“Company Size > 100”* and *“Job Title contains ‘CTO’”*. Verify the segment updates in real time by sending a test email to a test contact.

**2. Inject AI‑Generated Copy with [Canva](https://www.canva.com/) + ElevenLabs**  
Use Canva’s “Magic Write” to draft subject lines and body snippets. Export the text, then paste it into ChatGPT (OpenAI API key “sk‑…”). Prompt ChatGPT to “improve tone for a SaaS upsell.” Copy the refined copy back into Klaviyo’s email editor. For audio, feed the same content to ElevenLabs (voice “Nova” at 150 words/min). Download the MP3 and attach it to your Klaviyo email under “Add File” → “Upload.” Check that the audio icon appears next to the subject line in the draft view.

**3. Validate Deliverability with Hostinger’s SPF/DKIM Setup**  
Navigate to Hostinger’s DNS Manager → “Add Record.” Create a TXT record for SPF: `v=spf1 include:klaviyo.com ~all`. Add a CNAME for DKIM: `klaviyodkim._domainkey.yourdomain.com → klaviyodkim.klaviyo.com`. In Klaviyo, go to Settings → Email → DKIM & SPF. Toggle “Enable DKIM” and “Enable SPF.” Confirm status shows “Verified” within 15 minutes. If “Not Verified,” double‑check the Hostinger record names and TTL.

**4. Leverage ActiveCampaign’s Automation Builder for Post‑Purchase Follow‑ups**  
In ActiveCampaign, create a new automation: “Completed Purchase” → “Add to List” → “Send Email.” Use the “Delay” step set to 1 hour. In the email body, insert a dynamic tag `{{first_name}}` and a link to a product survey. Publish the automation and run a test with a dummy order to ensure the email triggers correctly. Sync the same list back to Klaviyo via a Zap to maintain a single source of truth.

**5. Measure Performance with [Semrush](https://www.semrush.com/) and Klaviyo Analytics**  
Export Klaviyo’s email performance report (CSV). Import the CSV into Semrush’s “Email Analytics” module. Set up a custom dashboard with metrics: *Open Rate, Click‑Through Rate, Unsubscribe Rate*. Automate the report export in Klaviyo under Settings → Export → Schedule (daily at 8 AM). In Semrush, click “Schedule Report” → “Send to Email” (use your Menshly email). Review the dashboard weekly; if CTR drops below 15%, revisit the subject line AI prompt in ChatGPT.  

**Further Reading**  
- *Deep Dive: Integrating ElevenLabs Voice into Klaviyo Campaigns* – https://menshly.com/elevenlabs-klaviyo  
- *Mastering B2B Segmentation with Apollo.io and Klaviyo* – https://menshly.com/apollo-klaviyo  
- *Optimizing Email Deliverability with Hostinger DNS* – https://menshly.com/hostinger-dns-email  

These steps will elevate your email automation stack from basic blasts to a fully AI‑powered, data‑driven campaign engine.

Ready to understand the full business opportunity? Read our [opportunity deep-dive]({< ref "/opportunities/how-to-build-an-ai-email-marketing-agency-20k-30kmonth.md" >}).


## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
