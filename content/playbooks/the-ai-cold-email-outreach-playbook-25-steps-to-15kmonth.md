---
title: "The AI Cold Email Outreach Playbook: 25 Steps to $15K/Month"
date: 2026-07-11
category: "Playbook"
price: "₦35,000"
readTime: "81 MIN"
excerpt: "The AI Cold Email Outreach Playbook: 25 Steps to $15K/Month This playbook is a full‑blown OPERATING SYSTEM, not a blog post or loose guide. 25 procedures. 10 modules. 12+ hours of reading and execution. By the end of every procedure you will own a tu..."
image: "/images/articles/playbooks/the-ai-cold-email-outreach-playbook-25-steps-to-15kmonth.png"
heroImage: "/images/heroes/playbooks/the-ai-cold-email-outreach-playbook-25-steps-to-15kmonth.png"
relatedOpportunity: "/opportunities/how-to-build-an-ai-cold-email-outreach-system-10k-20kmonth/"
relatedGuide: "/intelligence/build-an-ai-data-analysis-automation-service-with-chatgpt-the-complete-step-by-s/"
---
**The AI Cold Email Outreach Playbook: 25 Steps to $15K/Month**  
This playbook is a full‑blown OPERATING SYSTEM, not a blog post or loose guide. **25 procedures. 10 modules. 12+ hours of reading and execution.** By the end of every procedure you will own a turnkey, AI‑powered cold email outreach engine that blends Mailchimp’s mass‑email capabilities with PhantomBuster’s data‑scraping automation to generate a steady stream of high‑quality leads, convert them into sales, and scale the system to $15,000+ in monthly recurring revenue. You will have every SOP, exact API key configuration, and revenue calculator baked in, so you can hit target metrics from day one. This playbook extends our free implementation guide with complete procedures, SOPs, and revenue calculators. For the free step‑by‑step guide, see our [implementation guide]({< ref "/intelligence/build-a...">}).

---

# MODULE 1: FOUNDATION

## Overview  
In this first module we lay the bedrock upon which your AI‑powered cold‑email engine will thrive. You’ll register and verify all required business accounts, lock down a dedicated domain and email address, and bind the core automation tools together. Skipping any of these steps will leave your outreach brittle: without a verified domain you’ll sit on a high spam‑score; without a dedicated email you’ll lose deliverability; without the integration layer you’ll be stuck in a spreadsheet‑driven nightmare and can’t scale.

You will also learn how to structure a minimal, self‑contained tech stack that can grow from a single person to a team of five without a rewrite. By the end of this module you’ll have a clean, audited workflow that can generate, qualify, and send cold‑email sequences, all while logging every touch in an audit‑ready database. That foundation is the key to the next modules, where you’ll inject AI intelligence, refine subject‑line A/B tests, and automate follow‑ups at scale.

| Tool          | Purpose                                                    | Free Tier (Limits)                      | Paid Tier (Monthly) |
|---------------|-------------------------------------------------------------|-----------------------------------------|---------------------|
| Mailchimp     | Email delivery, autoresponder, analytics                   | 2 000 contacts, 10 000 emails/mo        | $10 (5 000 contacts)|
| PhantomBuster | LinkedIn/website data extraction, auto‑email triggers      | 1 000 actions/mo                       | $49 (10 000 actions)|
| Make.com      | Workflow orchestration, API integration                     | 3 000 operations/mo                    | $29 (15 000 operations)|
| Replit        | AI‑code prototyping, quick script deployment                | Unlimited free repls                    | $7 (private repls)|
| Notion        | Knowledge base, SOPs, task tracker                          | Unlimited pages, 5 MB storage           | $8 (unlimited)      |

**Estimated time to complete:** 3 days (≈ 8 hrs).  

This module is non‑negotiable. If you rush through it, you’ll waste hours later fixing domain‑authentication errors, re‑authorizing APIs, or re‑building a broken integration. Follow each step precisely, and you’ll own a resilient, production‑grade foundation that can handle 1,000+ warm leads per month without a hitch.

---

**Procedure 1.1** — Generation failed due to AI backend unavailability. Please retry later.

---

## Procedure 1.2: Set Up Domain Email Forwarding in Hostinger

1. Open your web browser and go to **https://www.hostinger.com/login**.  
   - In the login form, type your Hostinger email address into the **Email** field.  
   - Enter your password in the **Password** field.  
   - Click the **Log In** button in bold.  

2. On the Hostinger dashboard, locate the **Hosting** tab in the top navigation bar and click it.  
   - In the list of sites, find the domain you want to forward emails for.  
   - Click the **Manage** button (bold) next to that domain.  

3. On the Hostinger cPanel page, scroll to the **Email** section and click **Email Forwarders** (bold).  
   - The Email Forwarders page will load with a table of any existing forwarders.  

4. Click the **Create Forwarder** button (bold) at the top right of the page.  
   - In the **Address** field, type the local part of the email you want to forward (e.g., `sales`).  
   - In the **Domain** drop‑down, confirm your domain is selected.  
   - In the **Destination** field, enter the full email address you want to forward to (e.g., `yourname@gmail.com`).  

5. Click the **Save** button (bold).  
   - The screen should refresh and display a success banner: **“Forwarder has been created”**.  

**Do you see the success banner?**  
If not, double‑check that the destination email is valid and that you clicked **Save**.  

6. Return to the cPanel main page by clicking the **Dashboard** link in the top left.  
7. Scroll down to the **Domains** section and click **Advanced DNS Zone Editor** (bold).  
8. In the **Domain** drop‑down, select your domain.  
9. Scroll to the **Records** table and locate the **MX** row.  
10. If an MX record exists, click the **Edit** icon (pencil) next to it.  
    - If it does not exist, click **Add Record** (bold) and select **MX** from the drop‑down.  

**Do you see the MX record row?**  
If you do not, ensure you are in the correct domain and that the DNS editor is fully loaded.  

11. In the **Priority** field, enter **10**.  
12. In the **Server** field, type `mail.yourdomain.com` (replace `yourdomain.com` with your actual domain).  
13. Click the **Save** button (bold) at the bottom.  

**Do you see the updated MX record with priority 10?**  
If the priority defaults to 0, you may have entered the field incorrectly—re‑enter **10** and save again.  

14. Back in the cPanel, navigate to **Email Accounts** (bold).  
15. Click **Create** (bold) to add a new email account that will serve as the destination for your forwarder.  
    - **Login**: `sales@yourdomain.com`  
    - **Password**: Generate a strong password using Hostinger’s password generator.  
    - **Storage**: Set to **Unlimited** if available, otherwise **500 MB**.  
16. Click **Create** (bold).  

17. Open a new tab and go to **https://make.com**.  
    - Sign in or create a free account.  
    - Create a new scenario that triggers on a new **Email Forwarder** creation (use the Hostinger webhook if available).  
    - Add an action step to **Send an email** via **Zapier** (or Make.com’s own email module).  
    - Map the forwarded email address to the destination email you created in step 15.  

**Do you see the Make.com scenario with a Hostinger trigger and Zap

---

## Procedure 1.3: Create a Make.com Scenario for Lead Data Collection

1. **Open a web browser** and navigate to **https://www.make.com**.  
2. Click the **Sign Up** button in the top‑right corner.  
3. Enter your email (e.g., you@example.com), create a password, and click **Create account**.  
4. Verify your email by clicking the link sent to your inbox.  
5. After verification, you will be taken to the **Dashboard**.  
   *Do you see the “Dashboard” screen with a “Create new scenario” button?*  
   If not, refresh the page or log out and back in.  

6. Click the **Create new scenario** button (the big **+** icon on the right).  
7. In the pop‑up, type **Lead Collection** in the scenario name field and click **Create**.  
8. The scenario editor opens. Click the **+** icon to add the first module.  
9. In the search field, type **HTTP** and select **HTTP > Make a request**.  
10. Configure the HTTP request:  
    - **URL**: `https://api.apollo.io/v1/leads/search`  
    - **Method**: **GET**  
    - **Headers**: `Authorization: Bearer YOUR_APOLLO_API_KEY` (replace with your key)  
    - **Parameters**: `limit=100`  
    - Click **Save**.  
    *Do you see the HTTP request module with the URL and headers you entered?*  
    If the **Authorization** header is missing, add it manually.  

11. Click the **+** icon again and search for **PhantomBuster**. Since Make.com does not have a native PhantomBuster module, we will use an HTTP request to trigger it. Select **HTTP > Make a request**.  
12. Configure this second HTTP request:  
    - **URL**: `https://phantombuster.com/api/v1/run`  
    - **Method**: **POST**  
    - **Headers**:  
      - `Content-Type: application/json`  
      - `PhantomBuster-Token: YOUR_PHANTOMBUSTER_API_KEY`  
    - **Body (raw)**:  
      ```json
      {
        "phantomName": "LinkedIn Lead Scraper",
        "phantomParams": {
          "input": {
            "source": "https://www.linkedin.com/search/results/people/?keywords=software%20engineer"
          },
          "outputFileName": "linkedin_leads.csv"
        }
      }
      ```  
    - Click **Save**.  
13. Drag a line from the first HTTP module to the second HTTP module to set execution order.  
14. Add a **Data Store > Store a record** module from the **Data Store** app to capture PhantomBuster output.  
15. Configure the Data Store module:  
    - **Data Store**: `LeadCollectionStore` (create a new one if it does not exist)  
    - **Record ID**: `{{trigger.id}}` (use the unique ID from the first HTTP module)  
    - **Data**: `{{2.output}}` (the JSON response from the second request)  
    - Click **Save**.  

*Do you see the three modules connected in a straight line?*  
If the second HTTP module is not connected, drag its arrow to the first module.

16. Click the **Scenario Settings** icon (gear) in the top‑right.  
17. Under **Execution**, set **Execution mode** to **Automatic** and **Cron** to `0 2 * * *` (run daily at 02:00 UTC).  
18. Choose **Save**.  
19. Click the **Run once** button (the orange play icon) to test the scenario.  
20. Observe the execution log panel. The log should show:  
    - **HTTP request to Apollo**: `200 OK`  
    - **HTTP request to PhantomBuster**: `202 Accepted`  
    - **Data Store**: `Record created (ID: 12345)`  
    *Do you see those three steps with the expected status codes?*  
    If you see `401 Unauthorized` on the Apollo request, double‑check the API key. If you see `403 Forbidden` on the PhantomBuster request, verify your token and that your Phantom name matches the one you have purchased.

21. Return to the **Scenario Settings** and click **Enable scenario**.  
22. A banner will appear: **“Scenario is now enabled”**.  

### Expected Output
When the scenario runs, the Data Store will contain a JSON object like:

```json
{
  "id": "12345",
  "lead_data": [
    {
     

## Check-In: Module 1 Complete

- [ ] Register Your Business Accounts on Mailchimp and PhantomBuster completed and verified
- [ ] Set Up Domain Email Forwarding in Hostinger completed and verified
- [ ] Create a Make.com Scenario for Lead Data Collection completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 2: TECH STACK

## Overview

This module is the foundation of your AI‑powered cold email outreach engine. It walks you through every single tool that will become the nervous system of your operation, from data ingestion via PhantomBuster to list management in Mailchimp, and the automation layer in Make.com. If you skip this module, your outreach will be a chaotic blend of manual spreadsheets and unconnected APIs, leading to data silos, inconsistent email deliverability, and ultimately wasted dollars. Completing this module guarantees that every click, every field, and every API key is correctly wired so that your outbound campaigns run like a well‑orchestrated machine.

You will spend approximately **2 hours** connecting, configuring, and validating the data flows. The process is deliberate: each tool must be verified before moving on, because a single mis‑configured integration can cascade into bounced emails, API limits, and even account suspension. By the end of this module you will have a clean, auditable tech stack that can be replicated, scaled, and handed off to a junior operator without loss of functionality.

| Tool            | Purpose                                          | Free Tier                                 | Paid Tier                                  |
|-----------------|--------------------------------------------------|-------------------------------------------|--------------------------------------------|
| Mailchimp       | Email list management & transactional emails    | 2,000 contacts, 10,000 sends/month        | Essentials $9.99/mo (5,000 contacts)       |
| PhantomBuster   | Data extraction & lead enrichment                | 300 runs/month (1 run = 200 rows)          | Pro $36/mo (1,000 runs/month)              |
| Make.com        | Workflow automation & API orchestration           | 1,000 operations/month, 15 min intervals | Starter $9/mo (15,000 operations)          |
| Replit          | Code execution & small‑scale scripts             | Unlimited free accounts, 500 MB storage   | Hacker $5/mo (10 GB storage)               |
| Vapi            | Voice‑to‑text transcription for call scripts     | 5 min/day                                 | Pro $24/mo (50 min/day)                    |
| Canva           | Email template design & graphics creation        | Unlimited free access, limited templates  | Pro $12.99/mo (full library)               |

*Estimated Time to Complete:* **2 hours** (inclusive of account creation, API key retrieval, and validation checks).

---

## Procedure 2.1: Register and Configure Mailchimp API Key for Campaign Automation

1. **Open a web browser** and navigate to **https://mailchimp.com**.  
2. In the top‑right corner click the **“Sign up free”** button (labelled **SIGN UP FREE**).  
3. On the sign‑up form, fill in **Name**, **Email address**, and **Password** with exactly the values you want to use.  
4. Click **“Create your account”** (button text: **CREATE YOUR ACCOUNT**).  
   *Do you see the Mailchimp dashboard with a green banner “Welcome to Mailchimp!”? If not, refresh the page or clear your browser cache.*  
5. In the left‑hand navigation panel click **Account** (icon: person silhouette).  
6. From the dropdown, click **Account** again to open the account settings page.  
7. On the top menu, click **Extras** (arrow icon) → **API keys**.  
8. You should now see the **API keys** page. In the **Create A Key** section, click the blue **Create A Key** button.  
9. A modal dialog appears with a generated key. Copy the entire key to your clipboard.  
   *Do you see the modal titled “New API key” with a 32‑character string? If not, click the **Refresh** button on the API keys page.*  
10. Close the modal by clicking **Close**.  
    - **Expected output:** You are back on the **API keys** page with a new row containing the copied key and its **Create date**.  

| Tool | Free Tier | Paid Tier | Price | Features |
|------|-----------|-----------|-------|----------|
| Mailchimp | 2,000 contacts & 10,000 sends/month | Essentials $13.39/mo | Unlimited sends, advanced reports | Email templates, basic automation |
| Make.com | 500 operations/month | 1,000 ops/month $25/mo | Unlimited operations, premium modules |
| Zapier | 100 tasks/month | Starter $19.99/mo | Unlimited Zaps, multi‑step Zaps |
| PhantomBuster | 5 scripts/day | Unlimited $50/mo | API scraping, scheduled runs |

11. **Open a new tab** and go to **https://replit.com**.  
12. Click **Log in** (top‑right) and authenticate via Google or GitHub.  
13. Once logged in, click **+ Create** → **New repl**.  
14. Choose **Python** as the language and name the repl **mailchimp_test**.  
    *Do you see the Replit editor with a `main.py` file? If not, double‑check you selected the correct language.*  
15. In `main.py`, paste the following code, replacing `YOUR_API_KEY` with the key you copied:  

```python
import requests
import json

api_key = 'YOUR_API_KEY'
server_prefix = api_key.split('-')[1]  # e.g., us17
url = f'https://{server_prefix}.api.mailchimp.com/3.0/lists'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)
print('Status Code:', response.status_code)
print('Response:', json.dumps(response.json(), indent=2))
```

16. Click the **Run** button (green triangle) to execute the script.  
    - **Expected output:** `Status Code: 200` and a JSON object listing your Mailchimp lists.  
    - If you see **`Status Code: 401`**, this means **“Invalid API key.”** Fix it by re‑copying the key from step 9 and replacing it in the script.  

17. Return to the browser and open **https://make.com**.  
18. Log in with the same credentials you used for Replit.  
19. In the Make dashboard, click **Create a new scenario**.  
20. In the scenario editor, click the **+ Add** button and search for **HTTP** → select **HTTP

---

## Procedure 2.2: Set Up PhantomBuster Workflow to Scrape LinkedIn Leads

1. **Open your web browser and navigate to** `https://phantombuster.com/`.  
   - Click **“Sign up”** in the top‑right corner.  
   - Enter your email, password, and click **“Create account”**.  
   - Check your inbox for the verification email, click **“Verify email”**, and you are logged in.  
   - *Do you see the PhantomBuster dashboard with the **“Create new Phantom”** button? If not, refresh the page or clear cache.*

2. **Create a new Phantom**  
   - On the dashboard, click **“Create new Phantom”**.  
   - In the “Select a Phantom” dropdown, type **“LinkedIn Lead Gen”** and select **“LinkedIn Lead Gen”**.  
   - Click **“Continue”**.  
   - In the “Name your Phantom” field, type **“LinkedIn Lead Scraper – Module 2”** and click **“Create”**.  
   - *Do you see the Phantom configuration screen with the **“Set up Phantom”** button? If not, ensure you are on the correct Phantom page.*

3. **Configure LinkedIn credentials**  
   - In the “LinkedIn Credentials” section, click **“Add new credentials”**.  
   - A modal will appear; in the **“Username”** field, type your LinkedIn login email.  
   - In the **“Password”** field, type your LinkedIn password.  
   - Click **“Save credentials”**.  
   - *Do you see the green checkmark next to your credentials? If you see “LinkedIn login failed”, it means your password is incorrect or LinkedIn has blocked the account. Fix it by re‑entering the correct password or enabling 2FA on LinkedIn.*

4. **Define scraping parameters**  
   - Under **“Target URL”**, input `https://www.linkedin.com/search/results/people/?keywords=software+engineer&origin=GLOBAL_SEARCH_HEADER`.  
   - In **“Pagination”**, enter `5` (number of pages to scrape).  
   - In **“Scrape Fields”**, click **“Add field”** and enter `Full Name`, `Title`, `Company`, `Location`, `Profile URL`.  
   - Click **“Save”**.  
   - *Do you see the fields listed in the “Scrape Fields” table? If not, double‑check the field names.*

5. **Set execution settings**  
   - In **“Execution”**, set **“Run every”** to `1` day.  
   - Set **“Timeout”** to `30` minutes.  
   - Under **“Phantom Run”**, choose **“Run now”** (you’ll run a test later).  
   - Click **“Save”**.  
   - *Do you see the **“Run now”** button highlighted? If it’s disabled, ensure all required fields are filled.*

6. **Create a Zapier integration**  
   - Open a new tab and go to `https://zapier.com/`.  
   - Click **“Sign up”** (free tier) and complete the email verification.  
   - After login, click **“Make a Zap”**.  
   - For the trigger app, search for **“PhantomBuster”** and select it.  
   - Choose the trigger event **“New Data Export”** and click **“Continue”**.  
   - Connect your PhantomBuster account by pasting the API key from PhantomBuster (found under **“Account Settings” > “API Key”**).  
   - Confirm connection.  
   - *Do you see the trigger “New Data Export” ready? If you see “Connection failed”, double

---

## Procedure 2.3: Create and Test Make.com Scenario to Sync Lead Data to Google Sheets

1. **Open your browser** and navigate to **https://www.make.com/**.  
   - If you have no account, click **Sign up** in the top‑right corner, enter your email, set a password, and confirm.  
   - After login, you will land on the **Dashboard** screen showing any existing scenarios.

2. **Create a new scenario**  
   - Click the **+ CREATE** button in the upper left.  
   - In the pop‑up, type **Scenario name**: `LeadSyncToSheets`.  
   - Click **Create**.

3. **Add the Google Sheets module**  
   - In the empty canvas, click the big **+** icon.  
   - In the search bar, type **Google Sheets** and press **Enter**.  
   - Select **Google Sheets > Watch Rows** from the list.  
   - Click **Add**.  

4. **Connect your Google account**  
   - A modal titled **Choose connection** will appear.  
   - Click **Create a new connection**.  
   - In the next window, click **Allow** to grant Make.com access to your Google Drive.  
   - After authorization, you’ll see **Connection name**: `GoogleSheets-LeadSync`.  
   - Click **Save**.  

5. **Configure the Google Sheets module**  
   - Click on the Google Sheets icon you just added.  
   - In the **Spreadsheet** dropdown, choose the spreadsheet named `LeadDatabase`.  
   - In **Sheet** dropdown, select `RawLeads`.  
   - Set **Range** to `A1:D`.  
   - In **Only new rows** toggle, switch to **ON**.  
   - Click **OK**.  

**Check‑in**  
Do you see the Google Sheets module with the spreadsheet `LeadDatabase` and sheet `RawLeads` selected? If not, verify you are connected to the correct Google account and that the spreadsheet exists.  

6. **Add a PhantomBuster module**  
   - Click another **+** on the canvas, next to the Google Sheets module.  
   - Search for **PhantomBuster** and select **PhantomBuster > Run**.  
   - Click **Add**.  

7. **Connect PhantomBuster**  
   - In the PhantomBuster modal, click **Create a new connection**.  
   - Paste your PhantomBuster **API Key** (found in your PhantomBuster dashboard > Settings > API Key).  
   - Name the connection `PhantomBuster-LeadAPI`.  
   - Click **Save**.  

8. **Configure the PhantomBuster module**  
   - Click the PhantomBuster icon.  
   - In **Phantom URL**, paste the URL of the lead‑fetching phantom you created (e.g., `https://phantombuster.com/api/v1/runPhantom?phantomId=123456`).  
   - Set **Parameters** as:
     ```
     {
       "maxResults": 100,
       "country": "US"
     }
     ```  
   - In **Output format**, choose `JSON`.  
   - Click **OK**.  

**Check‑in**  
Do you see the PhantomBuster module with the URL and parameters displayed? If not, re‑enter the phantom URL and ensure the JSON is correctly formatted.  

9. **Add a filter to pass only successful runs**  
   - Click **+** after the PhantomBuster module.  
   - Search for **Filter** and select **Filter > Only if**.  
   - Click the filter icon and set **Condition** to `status Code` **equals** `200`.  
   - Click **OK**.  

10. **Map PhantomBuster output to Google Sheets**  
    - Click the arrow from the Filter to the Google Sheets module.  
    - In the mapping screen, drag the following fields from PhantomBuster to Google Sheets columns:
      - `leadEmail` → Column **A**  
      - `leadName` → Column **B**  
      - `leadCompany` → Column **C**  
      - `leadTitle` → Column **D`  

11. **Set the trigger schedule**  
    - Click the clock icon on the top‑left of the left panel.  
    - Select **Schedule** > **Every 15 minutes**.  
    - Click **OK**.  

12. **Save the scenario**  
    - In the top right, click the **Save** button (disk icon).  
    - Confirm by clicking **Save** in the

## Check-In: Module 2 Complete

- [ ] Register and Configure Mailchimp API Key for Campaign Automation completed and verified
- [ ] Set Up PhantomBuster Workflow to Scrape LinkedIn Leads completed and verified
- [ ] Create and Test Make.com Scenario to Sync Lead Data to Google Sheets completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 3: FRAMEWORK

## Overview

In this module you will master the universal process that turns raw data into a repeatable, scalable AI‑powered cold‑email outreach engine. You will learn how to map every touchpoint of the client lifecycle—from first contact to final delivery—into a documented framework that guarantees consistency, quality, and rapid growth. The playbook is designed for solo entrepreneurs who need a turnkey system that can be replicated for multiple clients without sacrificing speed or precision. Skipping this module will leave you with a fragmented stack, inconsistent onboarding, and an inability to scale beyond a handful of clients.

Why does this matter? A well‑defined framework is the backbone of any high‑margin service business. It removes guesswork, reduces onboarding time, and creates a repeatable template that can be sold as a product. Without it, you risk over‑engineering, losing clients due to inconsistent deliverables, and burning through time on ad‑hoc fixes. In contrast, a razor‑sharp framework means you can double your client load in 30 days while keeping your quality score above 95 %.  

Below is a concise inventory of the core tools you’ll need, their free‑tier caps, and the cost of the essential paid plans. All prices are current as of July 2026 and are rounded to the nearest dollar.

| Tool          | Purpose                                            | Free Tier (limits)                                      | Paid Tier (monthly) |
|---------------|----------------------------------------------------|----------------------------------------------------------|---------------------|
| **Mailchimp** | Email list management & automation                | 2 000 contacts, 10 000 emails/month, basic templates     | Essentials $14.99   |
| **PhantomBuster** | LinkedIn/LinkedIn Sales Navigator scraping & automation | 150 API calls/month, 1 000 extraction records per month   | Pro $79             |
| [**Make.com**](https://www.make.com/en/register?pc=menshly) | Integration & workflow orchestration               | 5 000 operations/month, 1 000 operations/day             | Starter $29         |
| [**Replit**](https://replit.com/refer/egwuokwor) | Code execution environment for custom scripts      | Unlimited projects, 512 MB RAM, 1 Gb storage             | Hacker $7           |
| **ChatGPT** (OpenAI) | AI content generation & personalization          | GPT‑3.5, 90 000 tokens/month                             | ChatGPT Plus $20    |
| [**Canva**](https://www.canva.com/) | Graphic & email header design                      | Unlimited free templates, 5 GB storage                   | Pro $12.99          |
| [**Grammarly**](https://grammarly.com/) | Writing assistant & style checks                  | 3 000 words/month, basic grammar checks                 | Premium $12         |

**Estimated time to complete this module**: 4 – 5 hours. This includes reading, setting up the tools, drafting the framework document, and running a single test outreach workflow to validate every step.

---

**Procedure 3.1** — Generation failed due to AI backend unavailability. Please retry later.

---

## Procedure 3.2: Map Your Client Onboarding Workflow for AI Outreach Campaigns

1. **Create a Dedicated Notion Workspace for the Client**  
   - Open your browser and go to https://www.notion.so.  
   - Click **Sign In** (top right) and log in with your credentials.  
   - In the left sidebar, click **+ New Page**.  
   - Name the page **“Client XYZ – AI Outreach Onboarding”** and press **Enter**.  
   - In the new page, type `/table – inline` and hit **Enter** to create a table.  
   - Label the columns: *Client Name, Email, Phone, Campaign Goal, Start Date, Status*.  
   - **Expected Output:** A fresh table with the six columns ready for data entry.  

2. **Populate Client Contact Details**  
   - Click the first empty cell under *Client Name* and type **Client XYZ**.  
   - Under *Email*, type **contact@clientxyz.com**.  
   - Under *Phone*, type **+1 555‑123‑4567**.  
   - Under *Campaign Goal*, type **Generate 200 qualified leads**.  
   - Under *Start Date*, click the calendar icon, pick **today’s date**, and click **OK**.  
   - Under *Status*, type **Pending**.  
   - Click the three dots in the top right of the table and select **Export → CSV**.  
   - Save the file as **client_xyz_onboarding.csv** on your desktop.  

3. **Create a Mailchimp Account (or Log In)**  
   - Open a new tab, go to https://mailchimp.com/signup.  
   - Click **Sign up free** (bolded button).  
   - Enter **contact@clientxyz.com** as the email, **StrongPass123!** as the password, and **Client XYZ** as the account name.  
   - Click **Create a new account**.  
   - Complete the survey: set *Business size* to **1–5 employees** and *Industry* to **Marketing & Advertising**.  
   - Click **Continue**.  
   - **Expected Output:** You should land on the Mailchimp dashboard with a welcome banner.  

4. **Create a New Audience for the Client**  
   - In Mailchimp, click **Audience** (top navigation bar).  
   - Click **View audiences** (green button).  
   - Click **Create Audience** (bolded button).  
   - Fill in:  
     - *Audience name*: **Client XYZ Leads**  
     - *Default from email*: **contact@clientxyz.com**  
     - *Default from name*: **Client XYZ Outreach**  
   - Click **Save**.  
   - **Check‑in:** Do you see the new audience listed under “Audience” in the sidebar? If not, refresh the page.  

5. **Import the Client CSV into Mailchimp**  
   - Within the *Client XYZ Leads* audience, click **Manage contacts** → **Import contacts**.  
   - Select **Upload a file** → **Choose File** → locate **client_xyz_onboarding.csv**.  
   - Click **Continue**.  
   - Map the columns: ensure *Email* matches *Email Address*, *First name* matches *Client Name*, *Phone* matches *Phone*.  
   - Click **Finalize import**.  
   - **Expected Output:** “Import complete – 1 contact added.”  

6. **Set Up a PhantomBuster Lead Scraper**  
   - Open a new tab, go to https://phantombuster.com.  
   - Click **Log in** (top right) and log in with your credentials.  
   - Click **New Buster** → **Choose a Buster** → search for **“LinkedIn Profile Scr

## Check-In: Module 3 Complete

- [ ] Define Your AI Cold Email Delivery Framework completed and verified
- [ ] Map Your Client Onboarding Workflow for AI Outreach Campaigns completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 4: FIRST BUILD

## Overview

In this module you will launch, manage, and scale an AI‑powered cold email outreach system that leverages **Mailchimp** for email delivery and **PhantomBuster** for data extraction and automation. The module is built around a single end‑to‑end deliverable: a fully functional outreach workflow that pulls real‑world prospect data, tailors personalized AI‑generated email bodies, and schedules mass send-outs—all while tracking opens, clicks, and responses in real time. By mastering this workflow, you’ll be able to offer a turnkey lead‑generation service to clients, generate recurring revenue, and position yourself as a high‑value solo entrepreneur in the AI‑driven sales niche.

Skipping this module means missing the critical integration of a proven email marketing platform (Mailchimp) with a powerful web‑automation tool (PhantomBuster). Without this foundation, your outreach campaigns will lack scalability, deliverability, and the data‑driven insights that convert prospects into paying customers. You’ll also lose the opportunity to automate repetitive tasks—saving countless hours—and you’ll be unable to provide your clients with the metrics they demand to prove ROI.

| Tool          | Purpose                                        | Free Tier                                                | Paid Tier                                                       |
|---------------|------------------------------------------------|----------------------------------------------------------|-----------------------------------------------------------------|
| Mailchimp     | Email delivery, list management, analytics     | 2,000 contacts, 10,000 sends/month                       | Standard $13/month (up to 50,000 contacts, unlimited sends)     |
| PhantomBuster | Web scraping, automation, lead extraction     | 150 jobs/month, 1,000 actions/month                      | Pro $29/month (2,500 jobs/month, 10,000 actions/month)         |
| Make.com      | Workflow automation (optional)                 | 300 operations/month                                     | Premium $49/month (up to 30,000 operations/month)              |
| Replit        | Code editing & execution (optional)            | Unlimited free projects                                  | Hacker plan $7/month (1,000 GB‑hrs/month)                       |
| Canva         | Email template design (optional)               | Unlimited free designs                                   | Pro $12.99/month (access to premium assets)                     |

**Estimated time to complete:** 4 hours (including research, setup, and testing).

---

## Procedure 4.1: Configure PhantomBuster to Scrape Target Leads

1. **Open your web browser** and navigate to **https://phantombuster.com/**.  
2. In the top‑right corner click **bold “Login”**.  
3. Enter your **email** and **password** (the credentials you used when creating the PhantomBuster account).  
   - Expected result: You are taken to the **Dashboard** page that lists “Phantoms” and “API Key.”  
4. Click **bold “API Key”** in the left sidebar.  
5. Copy the displayed **API Key** into your clipboard.  
   - Check‑in: *Do you see a long string of characters under “API Key”? If not, refresh the page or log out and back in.*  
6. Open a new tab and go to **https://app.make.com/** (Make.com integration).  
7. If you do not have an account, click **bold “Start for free”** and complete the sign‑up wizard.  
   - Expected result: You land on the **Make.com dashboard** with a prompt to create a new scenario.  
8. In Make.com, click **bold “Create a new scenario”**.  
9. Search for “PhantomBuster” in the “Choose app & event” box and select the **PhantomBuster trigger**.  
10. Click **bold “Connect a new account”** and paste the **API Key** from step 4.  
    - Expected result: A green “Connected” badge appears.  
11. Click **bold “Test”** to confirm connectivity.  
    - If a **500 error** appears, double‑check that the API Key is correctly copied and that your PhantomBuster plan allows API usage.  
12. In the left pane, click **bold “Add a new Phantom”**.  
13. From the list, choose **“LinkedIn Profile Scraper”** (or “LinkedIn Lead Gen Scraper” if you prefer).  
14. Click **bold “Add”** to create the Phantom.  
15. In the Phantom settings panel, fill the following fields exactly:  

| Field | Exact Value | Notes |
|-------|-------------|-------|
| **Name** | `LeadGen_Scraper_Q2` | Keep consistent naming convention |
| **URL** | `https://www.linkedin.com/search/results/people/?keywords=Marketing%20Director&location=United%20States` | Replace keywords/loc as needed |
| **Limit** | `100` | Max leads to scrape per run |
| **Scroll delay** | `2000` | 2 seconds between scrolls |
| **Timeout** | `60000` | 60 seconds total run time |
| **Output format** | `CSV` | Output will be a CSV file |

16. Click **bold “Save”**.  
    - *Do you see the new Phantom listed in your PhantomBuster dashboard?* If not, ensure you clicked “Save” and that you’re on the correct dashboard page.  
17. Return to **Make.com** scenario editor.  
18. Click **bold “Add another module”** on the right‑hand side.  
19. Search for “Google Sheets” (free up to 90,000 rows) and select the **“Create a Spreadsheet row”** event.  
20. Click **bold “Connect a new account”** and choose the Google account that owns the target spreadsheet.  
21. Set the sheet name to **“Leads_Q2”** and map the columns to the CSV fields:  
    - `First Name` → `First Name`  
    - `Last Name` → `Last Name`  
    - `Company` → `Company`  
    - `Email` → `Email`  
    - `LinkedIn URL` → `LinkedInURL`  
22. Click **bold “Settings”** and set **“Maximum number of rows”** to `100`.  
    - *Do you see the column mapping screen? If not, click “Map fields” again.*  
23. Click **bold “Save”** in the Google Sheets module.  
24. Click **bold “Run once”** in the Make.com scenario to test the workflow.  
    - Expected result: A new row appears in the Google Sheet with the scraped lead data.  
25. If you see **“Error: Rate limit exceeded”**, it means PhantomBuster has hit the daily request cap.  
    - Fix: Go back to the PhantomBuster dashboard, increase your plan or wait 24 hours before rerunning.  

---

### Tool Comparison Table

| Tool | Price (Monthly) | Free Tier Limit | Key Features | Ideal Use |
|------|-----------------|-----------------|--------------|-----------|
| PhantomBuster | $29 (Pro) | 1,000 API calls/month | Web scraping, automation, API integration | Lead scraping, data extraction |
| Apollo.io | $49 (Starter) | 500 leads/month | Email finder, outreach platform, CRM | Email outreach, lead management |
| Make.com | $9 (Starter) | 1,000 operations/month | No‑code automation, multi‑app workflow | Orchestrate PhantomBuster + Sheets |
| Zapier | $19 (Starter) | 300 tasks/month | App integrations, simple triggers | Simple lead import to CRM |

---

### Cost Breakdown for the First Month

| Item | Cost | Rationale |
|------|------|-----------|
| PhantomBuster Pro | $29 | Enables 3,000 API calls, unlimited Phantoms |
| Make.com Starter | $9 | 5,000 operations, enough for 100 leads/day |
| Google Sheets

---

## Procedure 4.2: Set Up Mailchimp Campaign for Automated Cold Outreach

1. **Navigate** to <https://mailchimp.com/> and click **Sign up for free** at the top right.  
2. **Enter** your email (`you@example.com`), password (`StrongPass!2026`), and company name (`Solo AI Outreach`). Click **Create an account**.  
3. **Verify** your email by clicking the link sent to your inbox.  
4. **Log in** again to the Mailchimp dashboard.  
5. **Click** the **Audience** tab, then click **Manage Audience** → **View Audiences**.  
   - **Check‑in:** Do you see a list of audiences? If not, refresh the page or clear the cache.  
   - *Expected output:* A single audience named “Default Audience” with **0 subscribers**.  

6. **Click** **Create Audience** (top right).  
7. **Fill** the form:  
   - Audience name: **Cold Outreach Leads**  
   - Audience type: **Transactional** (default)  
   - Primary email address: `you@example.com`  
   - Primary phone number: leave blank.  
   Click **Create Audience**.  
8. **Set** the audience settings:  
   - Click **Audience Dashboard** → **Audience Settings** → **Audience name & defaults**.  
   - Set **Name** to `Cold Outreach Leads`.  
   - Leave default fields.  
   Click **Save**.  
   - *Expected output:* Confirmation banner “Audience settings saved.”  

9. **Create** a CSV file (`leads.csv`) with columns `Email`, `First Name`, `Last Name`.  
10. **Upload** the CSV:  
    - Click **Add Contacts** → **Import Contacts** → **Upload a file**.  
    - Drag `leads.csv` or click **Browse** to locate it.  
    - Click **Continue to Setup**.  
    - Map columns: `Email` → **Email Address**, `First Name` → **First Name**, `Last Name` → **Last Name**.  
    Click **Import**.  
   - *Check‑in:* Do you see “Import complete” with 100% success? If not, ensure column names match exactly.  

11. **Navigate** to the **Campaigns** tab → click **Create Campaign** → **Email**.  
12. **Name** the campaign `Cold Outreach 01`. Click **Begin**.  
13. **Choose** **Regular** email type.  
14. **Click** **Design Email** → **Create Template** → **Classic** → **Continue**.  
15. **Select** **Basic** layout. Click **Next**.  
   - *Expected output:* WYSIWYG editor with a single column.  

16. **Edit** the template:  
    - Click **Add Content** → **Text**.  
    - Replace placeholder with:  
      ```
      Hi *|FNAME|*,

      I help tech founders like you double their sales pipeline with AI‑driven outreach.  
      Let’s chat about a quick 15‑minute call.  
      <https

---

**Procedure 4.3** — Generation failed due to AI backend unavailability. Please retry later.

## Check-In: Module 4 Complete

- [ ] Configure PhantomBuster to Scrape Target Leads completed and verified
- [ ] Set Up Mailchimp Campaign for Automated Cold Outreach completed and verified
- [ ] Integrate AI Response Analysis into Your Email Automation Pipeline completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 5: CLIENT ACQUISITION

## Overview

In the current marketplace, AI‑driven cold email outreach is the fastest path to high‑quality leads for solo entrepreneurs. This module teaches you to **launch, manage, and scale** a fully automated outreach system that leverages Mailchimp for email delivery and list management, and PhantomBuster for data extraction and contact enrichment. By mastering these tools, you transform a manual outreach process into a repeatable, revenue‑generating machine that can attract paying customers without constant manual oversight.

Skipping this module means your funnel will stay stagnant: you’ll spend hours hunting leads, manually sending emails, and chasing responses. Your lead pipeline will remain shallow, and you’ll miss the opportunity to convert prospects into paying clients at scale. The result is lost time, wasted budget, and a stagnant business that cannot grow beyond a handful of manual leads.

**Tools Required**

| Tool          | Purpose                                                                 | Free Tier                                   | Paid Tier |
|---------------|--------------------------------------------------------------------------|---------------------------------------------|-----------|
| Mailchimp     | Email campaign creation, list management, automation workflows           | 2 000 contacts, 12 000 emails/month         | $10/month (Essentials) |
| PhantomBuster | Web scraping, LinkedIn/CRM data extraction, automated contact retrieval | 5 processes/month, 5 000 records/month      | $50/month (Starter) |
| Make.com      | Workflow automation between Mailchimp & PhantomBuster, scheduling        | 5 000 operations/month, 1 000 steps/month  | $49/month (Starter) |
| Replit        | Quick script execution for custom email personalization (optional)       | Unlimited projects, 500 MB storage          | $7/month (Hacker) |

**Estimated Time to Complete:** 3–4 hours (incl. testing, troubleshooting, and optimization).

---

## Procedure 5.1: Configure Mailchimp Campaign for AI Cold Email Outreach  

1. **Open Mailchimp** – Go to **https://mailchimp.com** and log in with your credentials.  
   - Click the **“Log In”** button (top‑right).  
   - Enter your **email** and **password**.  
   - Click **“Log In”** again.  
   *Expected output:* You land on the **Dashboard** with the orange “Create a Campaign” button visible.  

2. **Create a new campaign** –  
   - Click **“Create a Campaign”** (orange button).  
   - In the dropdown, choose **“Email”**.  
   - Select **“Regular”**.  
   - Click **“Create Campaign”** (blue button).  
   - Name the campaign **“AI Cold Outreach 2026”** in the text box and click **“Continue”**.  
   *Expected output:* You’re on the **Campaign Builder** page with the campaign name at the top.  

3. **Add recipients** –  
   - In the left menu, click **“Add Recipients”**.  
   - Select **“Create a Segment”**.  
   - Choose **“All subscribers in list”** (sub‑list **“Cold Leads”**).  
   - Click **“Save Segment”**.  
   - Return to the campaign by clicking **“Save & Continue”**.  
   *Expected output:* Segment **“Cold Leads”** appears under **Recipients**.  

4. **Configure email subject line** –  
   - Click **“Subject Line”** in the editor.  
   - Enter **“Quick Question About Your Business”**.  
   - Click **“Save”**.  
   *Do you see the subject line updated with “Quick Question About Your Business”? If not, refresh and re‑enter the text.*  

5. **Insert AI‑generated preview text** –  
   - Click **“Preview Text”**.  
   - Enter **“Let’s discuss how AI can boost your revenue.”**  
   - Click **“Save”**.  
   - Click **“Design Email”** to move to the design step.  

6. **Choose a template** –  
   - In the design editor, click **“Choose a template”**.  
   - Select **“Simple”** from the grid.  
   - Click **“Use this template”**.  
   *Expected output:* The editor loads the Simple template with a single content block.  

7. **Add an AI‑generated headline** –  
   - Click inside the headline block.  
   - Type **“Boost Your Revenue with AI”**.  
   - Highlight the text and click **“Bold”** icon.  
   - Click **“Save”**.  

8. **Insert body copy generated by ChatGPT** –  
   - Open a new tab and go to **https://chat.openai.com**.  
   - Log in with your OpenAI credentials.  
   - Prompt: *“Write a concise cold email body for a small business owner about using AI to increase sales, 150 words.”*  
   - Copy the response.  
   - Return to Mailchimp’s editor, click **“Add a text block”** below the headline.  
   - Paste the ChatGPT text.  
   - Click **“Save”**.  

9. **Add a call‑to‑action button** –  
   - Click **“Add a button”** below the text block.  
   - Enter **“Schedule a Free Call”** as the button text.  
   - Set the link to **https://calendly.com/yourbusiness/15min**.  
   - Click **“Save”**.  
   *Do you see a clickable button labeled “Schedule a Free Call”? If not, ensure the “Link” field is populated with the Calendly URL.*  

10. **Auto‑populate email body with AI‑generated images using Midjourney** –  
    - Open **https://www.midjourney.com/app**.  
   

---

## Procedure 5.2: **Integrate PhantomBuster to Harvest LinkedIn Leads into Mailchimp**

1. **Open your web browser** and navigate to **https://phantombuster.com**.  
   *User Action:* Type the URL into the address bar and press **Enter**.  
   *Expected UI:* PhantomBuster login page with fields “Email” and “Password”.

2. **Log in** with your PhantomBuster credentials.  
   *Click:* **Login** (bottom right button).  
   *Result:* Dashboard showing “My Scripts” and “New Script” button.

3. **Create a new LinkedIn Lead Search script**.  
   *Click:* **New Script** (top‑right).  
   *Select:* **LinkedIn Lead Search** from the list.  
   *Name:* Enter **LLS‑Mailchimp‑Sync** in the “Script Name” field.  
   *Click:* **Create Script** (bottom button).  
   *Result:* Script editor opens with a default JSON payload.

4. **Configure the LinkedIn search parameters**.  
   *In the JSON editor, replace the placeholder values with:*
   ```json
   {
     "searchKeywords": "Software Engineer",
     "location": "United States",
     "companySize": "51-200",
     "profileUrl": ""
   }
   ```  
   *Click:* **Save** (top‑right).  
   *Do you see the script JSON updated with your values? If not, double‑check the field names and ensure you pressed **Save**.*

5. **Set up your LinkedIn credentials** in PhantomBuster.  
   *Click:* **Launch** (top‑right) → **Set up LinkedIn** (dialog).  
   *Fill:*  
   - **LinkedIn Email:** your LinkedIn login email.  
   - **LinkedIn Password:** your LinkedIn password.  
   *Click:* **Save Credentials**.  
   *Result:* A green checkmark appears next to “LinkedIn Auth” in the script editor.

6. **Enable the “Save to CSV” option**.  
   *In the script settings panel, toggle the switch labeled **Export to CSV** to ON.  
   *Click:* **Save Settings** (bottom).  
   *Do you see the CSV toggle ON? If not, ensure you toggled the switch and saved.*

7. **Run a test execution** to verify data capture.  
   *Click:* **Run** (top‑right).  
   *Wait:* Until the progress bar reaches 100 %.  
   *Result:* A CSV file appears in the “Results” tab labeled **LLS‑Mailchimp‑Sync‑results.csv**.

8. **Download the CSV file**.  
   *Click:* **Download** button next to the file.  
   *Open:* The file in [**Notion**](https://notion.so/) (or any spreadsheet app).  
   *Verify:* The columns include **Name**, **Title**, **Company**, **LinkedIn URL**, **Email** (blank if not available).  
   *Do you see the CSV populated with at least 10 rows? If not, re‑run the script.*

9. **Set up a Zapier account** at **https://zapier.com** (free tier: 5,000 tasks/month, $19.99/month for Unlimited).  
   *Click:* **Sign up** → enter your email, create a password.  
   *Verify:* Email confirmation and log in.

10. **Create a new Zap** in Zapier.  
    *Click:* **Create Zap** (top‑left).  
    *Choose Trigger App:* **Email Parser by Zapier** (free).  
    *Name the Zap:* **LLS‑CSV‑to‑Mailchimp**.  
    *Click:* **Continue**.

11. **Set up the Email Parser mailbox**.  
    *Click:* **Set up Mailbox** → choose **Create a new mailbox** → name it **LLS-Parser**.  
    *Copy the mailbox address* (e.g., **parser@lls-parser.zapier.com**).  
    *Do you see the mailbox address? If not, re‑open the mailbox settings.*

12. **Create a template for parsing**.  
    *Open the mailbox in a browser tab.*  
    *Upload the CSV file you downloaded earlier.*  
    *Zapier will prompt you to “Create a new template.”*  
    *Select the first row as a sample.*  
    *Click:* **Save Template**.  
    *Result:* Fields “Name”, “Title”, “Company”, “LinkedIn URL”, “Email” appear under “Parsed Data”.

13. **Return to the Zap editor** and complete the trigger.  
    *Click:* **Test Trigger** → Zapier pulls the first row.  
    *Do you see the parsed data in the test results? If not, check the template mapping.*

14. **Add an Action step

---

## Procedure 5.3: Build a Lead Capture Landing Page with AI‑Generated Copy  

1. **Log into Hostinger**  
   - Open your browser, go to **https://www.hostinger.com/hosting/shared**.  
   - Click the **blue “Get Started”** button.  
   - Sign in with your Hostinger credentials or create a new account (free tier: *$1.99/mo for 3‑month plan*).  

2. **Create a new WordPress site**  
   - In the Hostinger dashboard, click **“Create New Website”**.  
   - Choose **“Start from Scratch”**.  
   - Select **“WordPress”** as the platform.  
   - Click **“Create”**.  

3. **Install Elementor**  
   - In the WordPress admin panel, go to **Plugins → Add New**.  
   - Search for **“Elementor Page Builder”**.  
   - Click **“Install Now”** then **“Activate”**.  

4. **Create a landing page**  
   - In WordPress, navigate to **Pages → Add New**.  
   - Title the page **“AI Cold Email Outreach – Capture Leads”**.  
   - Click **“Edit with Elementor”**.  
   - Do you see the Elementor canvas? If not, refresh the page or clear your browser cache.  

5. **Generate headline copy with ChatGPT**  
   - Open **https://chat.openai.com/**.  
   - Log in with your OpenAI account (free tier: 3,000 tokens/month).  
   - Input: *“Write a 12‑word headline for a landing page that offers AI‑powered cold email outreach services.”*  
   - Copy the headline text.  

6. **Add the headline to Elementor**  
   - Drag the **“Heading”** widget to the top of the canvas.  
   - In the left panel, set **“Title”** to the text you copied.  
   - Under **Style → Typography → Font Size**, set to **48px**.  

7. **Generate sub‑headline and body copy**  
   - Back in ChatGPT, prompt: *“Generate a 30‑word sub‑headline and a 100‑word sales paragraph for the same landing page.”*  
   - Copy the sub‑headline and paragraph.  

8. **Insert sub‑headline and paragraph**  
   - Drag **“Heading”** below the main headline, set **Title** to the sub‑headline, font size **30px**.  
   - Drag **“Text Editor”** widget below, paste the 100‑word paragraph into the editor.  

9. **Create hero image in Canva**  
   - Open **https://www.canva.com/**.  
   - Click **“Create a design” → “Custom size”** and enter **1920 x 1080**.  
   - In the left panel, click **“Photos” → “AI”** and search for *“AI email outreach”*.  
   - Drag the chosen image onto the canvas.  

10. **Export and upload image**  
    - Click **“Share” → “Download”**.  
    - Choose **PNG** and click **“Download”**.  
    - In Elementor, drag the **“Image”** widget below the paragraph.  
    - Click **“Choose Image”**, upload the PNG file, and set **“Width”** to **100%**.  

11. **Add a Mailchimp signup form**  
    - Visit **https://mailchimp.com/** and log in.  
    - In the top menu, click **“Audience” → “Signup forms” → “Embedded forms”**.  
    - Select **“Basic”** form style, click **“Generate Code”

## Check-In: Module 5 Complete

- [ ] Configure Mailchimp Campaign for AI Cold Email Outreach completed and verified
- [ ] **Integrate PhantomBuster to Harvest LinkedIn Leads into Mailchimp** completed and verified
- [ ] Build a Lead Capture Landing Page with AI‑Generated Copy completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 6: DELIVERY

## Overview  
Module 6 is the engine room of your AI‑powered cold email outreach service. It teaches you how to turn raw data from PhantomBuster into a polished, compliant Mailchimp campaign, then deliver that campaign to clients with razor‑sharp quality checkpoints and professional communication templates. Without this module you risk sending buggy sequences, missing GDPR compliance, and delivering sub‑par results that erode client trust and inflate churn. The delivery pipeline you build here is the single source of truth that keeps your service scalable, repeatable, and profitable.  

You’ll learn to set up a transparent workflow that tracks every email, monitors deliverability, and logs client feedback in Notion. We’ll walk through creating a “Delivery Playbook” that includes: a pre‑launch checklist, an automated status‑reporting dashboard, and a set of “Client‑Facing Templates” for onboarding, status updates, and post‑campaign reports. Each step is anchored to a real tool, so you can copy the exact clicks and settings and hit the ground running.  

**Time to complete:** 4 – 6 hours (including setup, testing, and documentation).  

| Tool          | Purpose                                        | Free Tier                                      | Paid Tier                        |
|---------------|------------------------------------------------|------------------------------------------------|----------------------------------|
| PhantomBuster | Harvest prospect lists & contact data         | 1 000 actions/month (limited API calls)        | $49/month (Pro)                  |
| Mailchimp     | Email sending, automation, reporting           | 2 000 contacts, 12 000 sends/month             | $13/month (Essentials)           |
| Make.com      | Orchestrate workflows between tools            | 200 operations/month (limited logic)          | $19/month (Creator)              |
| Zapier        | Connect Mailchimp, PhantomBuster, Notion       | 100 tasks/month (basic triggers)               | $19/month (Starter)              |
| Notion        | Project documentation & client status tracking | Unlimited pages & blocks (free)                | $8/month (Personal Pro)          |
| Grammarly     | Email copy proofreading & tone consistency    | Basic grammar & spell check (free)             | Premium $12/month (Pro)          |

This module is non‑negotiable: skip it, and you’ll lose the disciplined delivery that turns an AI‑toolkit into a repeatable, high‑margin business.

---

## Procedure 6.1: ESTABLISH AUTOMATED QUALITY CHECKPOINTS FOR AI EMAIL OUTREACH  

**Goal:** Build an end‑to‑end pipeline that automatically validates lead quality, email deliverability, and response fidelity before any AI‑generated email is sent.  

**Tools Required (All free tiers listed in parentheses):**  
- **Mailchimp** – Free tier: 2,000 contacts, 10 k sends/month.  
- **PhantomBuster** – Free tier: 50 tasks/month, 1 min task runtime.  
- **Make.com** – Free tier: 300 operations/month, 15 min scenario trigger.  
- **Zapier** – Free tier: 5 zaps, 100 tasks/month.  
- **ChatGPT (OpenAI)** – Free tier: 3 k tokens/day (GPT‑3.5).  
- **Canva** – Free tier: Unlimited free templates.  

---

### 1. Create a Mailchimp List for Cold Outreach  
1.1. Visit <https://mailchimp.com/> and **log in**.  
1.2. Click the **Audience** tab in the top menu.  
1.3. Click **Manage Audience** → **View audiences**.  
1.4. Click **Create audience**, then **Create a new audience**.  
1.5. Fill the form:  
- **Audience name:** ColdOutreach2026  
- **Audience email:** outreach@menshlyglobal.com  
- **Audience subject line:** “Exclusive AI Lead Generation”  
- **Reply-to email:** reply@menshlyglobal.com  
- **Default-from name:** Menshly AI Outreach  
1.6. Click **Save audience**.  
**Expected Output:** A new audience card labeled “ColdOutreach2026” appears in the Audience list.  

Do you see the “ColdOutreach2026” audience card? If not, verify that the **Audience name** field matches exactly and click **Save audience** again.

---

### 2. Add Custom Fields for Lead Score and Bounce Flag  
2.1. Inside the new audience, click **Add a field** → **Single line text**.  
2.2. Name the field **LeadScore** and click **Save**.  
2.3. Add a second field: **Single line text**, name it **BounceFlag**, click **Save**.  
2.4. Confirm that **LeadScore** and **BounceFlag** appear in the list view.  
**Expected Output:** Two new columns in the audience table: `LeadScore` and `BounceFlag`.  

Do you see the two new columns? If not, ensure the field names are spelled exactly as above.

---

### 3. Build a Make.com Scenario to Pull Leads from a CSV  
3.1. Go to <https://www.make.com/> and **log in**.  
3.2. Click **Create a new scenario**.  
3.3. Click the big **+** icon, search for **Google Sheets**, and click **Google Sheets**.  
3.4. Choose the **Watch Rows** trigger.  
3.5. Connect your Google account, select the spreadsheet **ColdLeads.xlsx**, sheet **RawData**.  
3.6. Set **Polling interval** to **15 minutes** and click **OK**.  
3.7. Click the next **+** icon, search for **Mailchimp**, and click **Mailchimp**.  
3.8. Choose the **Add a subscriber** action.  
3.9. Map the columns:  
- Email → **Email address**  
- Name → **Full name**  
- LeadScore → **LeadScore**  
- BounceFlag → **BounceFlag** (initially left blank)  
3.10. Click **Save** and then **Run once** to test.  
**Expected Output:** A new subscriber row appears in the Mailchimp audience with the mapped data.  

Do you see the new subscriber? If not, verify that the spreadsheet columns match the mapping fields.

---

### 4. Configure PhantomBuster to Verify Email Deliverability  
4.1. Visit <https://phantombuster.com/> and **log in**.  
4.2. Click **+ New Buster** → **Email Verifier** (search bar).  
4.3. **Import** the CSV of email addresses from the Google Sheet (click **Import** → **File**).  
4.4. Set **Verification threshold** to **80%**.  
4.5. Click **Run Buster**.  
4.6. Wait for the status to change to **Completed**.  
4.7. Click **Download** → **CSV** to download the results.  
**Expected Output:** A CSV file with columns `email`, `valid` (TRUE/FALSE), `score`.  

**Interactive Check‑in

---

## Procedure 6.2: Develop Client Communication Templates for Outreach Campaigns

1. **Open Notion**  
   - URL: https://www.notion.so  
   - Click **“Sign In”** in the upper‑right corner.  
   - Use your email **john.doe@example.com** and password **••••••**.  
   - Expected output: Your workspace dashboard with “Inbox” and “Projects” pages visible.  

2. **Create a new page**  
   - In the sidebar, click **“+ Add a page”**.  
   - Title the page **“Cold Email Templates – Client X”**.  
   - Select the template **“Database”** → **“Table – Full page”**.  
   - Expected output: A fresh table with columns “Template ID”, “Subject Line”, “Body”, “Personalization Markers”, “Status”.  

3. **Add columns**  
   - Click **“+ Add a property”** → choose **“Text”** → name **“CTA”**.  
   - Add another property → **“Select”** → name **“Stage”** (options: Draft, Reviewed, Approved, Live).  
   - Expected output: Table now has six columns.  

4. **Insert first template record**  
   - Click **“+ New”**.  
   - Fill “Template ID” with **T-001**.  
   - Fill “Subject Line” with **“Quick intro – {FirstName}?”**.  
   - Fill “Body” with:  
     ```
     Hi {FirstName},

     I noticed you’re doing great work at {Company}. I’ve helped similar companies increase leads by 30% using AI-driven outreach.

     Could we schedule a 15‑min call next week?

     Best,
     John
     ```
   - Fill “Personalization Markers” with **{FirstName}, {Company}**.  
   - Fill “CTA” with **“Schedule a Call”**.  
   - Set “Stage” to **Draft**.  
   - Expected output: One row appears with all fields populated.  

5. **Check template formatting**  
   - Do you see the placeholders `{FirstName}` and `{Company}` highlighted in bold? If not, click the ellipsis (**⋮**) on the record, select **“Toggle content”**, and ensure the text is wrapped in curly braces.  

6. **Add AI‑generated subject line**  
   - Open a new tab and go to **ChatGPT** (https://chat.openai.com).  
   - Click **“New chat”**.  
   - Prompt:  
     ```
     I need a subject line for a cold email to a fintech recruiter named Emily. Use a friendly tone and mention “AI” and “lead generation”.
     ```  
   - Copy the response: **“Emily, let’s boost your leads with AI”**.  
   - Return to Notion, edit the “Subject Line” cell, replace the old subject with the new one.  
   - Expected output: Updated subject line in the table.  

7. **Validate placeholders with Vapi**  
   - Open [**Vapi**](https://vapi.ai/) (https://www.vapi.io).  
   - Click **“Create a new API”** → name **“Template Validation”**.  
   - In the request body, paste:  
     ```json
     {
       "template": "Hi {FirstName},\n\nI noticed you’re doing great work at {Company}."
     }
     ```  
   - Click **“Run”**.  
   - Expected output: JSON response:  
     ```json
     {
       "valid": true,
       "missing_markers": []
     }
     ```  
   - If you see **“valid”: false**, the placeholders are malformed. Fix by ensuring each marker is enclosed in `{}`.  

8. **Create a secondary version**  
   - Duplicate the T-001 record by clicking the three dots (**⋮**) → **“Duplicate”**.  
   - Change “Template ID” to **T-002**.  
   - Update “Body” to a more personalized version:  
     ```
     Hi {FirstName},

     I saw your recent post about AI in fintech. I’ve helped similar firms like {Company} cut acquisition costs by 25%.

     Let’s chat for 10 minutes – does Tuesday 3 PM work?

     Cheers,
     John
     ```  
   - Set “Stage” to **Draft**.  

9. **Integrate with PhantomBuster**  
   - Open PhantomBuster (https://phantombuster.com).  
   - Log in with your credentials.  
   - Click **“Create a new Phantom”** → select **“Email Sequence Builder”**.  
   - In the **“Template”** field, paste the raw text of T-001.  
   - Click **“Run”**.  
   - Expected output: Phantom shows **“Email 1: Ready”** and a preview screenshot of the email.  

10. **Test email rendering**  
    - In PhantomBuster, click **“Send Test Email”** → enter **yourself@example.com**.  
    - Open your inbox (https://mail.google.com).  
    - Do you see the email with **{FirstName}** replaced by your actual name? If not, click **“Edit Template”** in Phantom, ensure that the merge tag syntax is **`{{FirstName}}`** and re‑run.  

11. **Add CTA link**  
    - In Notion, edit the “CTA” cell for T-001 to **“https://calendly.com/john-demo”**.  
    - In PhantomBuster’s template, replace the text **“Schedule a Call”** with **`<a href="https://calendly.com/john-demo">Schedule a Call</a>`**.  
    - Expected output: Clicking the CTA in the test email opens Calendly scheduling page.  

12.

## Check-In: Module 6 Complete

- [ ] ESTABLISH AUTOMATED QUALITY CHECKPOINTS FOR AI EMAIL OUTREACH completed and verified
- [ ] Develop Client Communication Templates for Outreach Campaigns completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 7: SCALING

## Overview  
Module 7 is the bridge from a one‑person operation to a lean, scalable outreach machine. You will learn how to transition from solo execution to a small team, hire your first contractor, and write SOPs that let you delegate without losing quality or speed. The module also covers margin analysis: you’ll calculate the true cost of each outreach cycle, identify the biggest levers for profit, and adjust your pricing model accordingly. If you skip this module, you’ll remain stuck in a manual loop, over‑paying for labor or reinventing workflows for each new campaign.

Why does it matter? AI‑powered cold email campaigns can grow linearly, but without a clear scaling strategy your growth will hit a plateau. This module teaches you to quantify runway, set realistic KPI targets, and automate recurring tasks so that you can focus on strategy instead of troubleshooting. By the end, you’ll have a documented playbook that any new hire can follow, a cost‑benefit matrix for your outreach stack, and a margin framework that keeps profit above 60%.

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| Mailchimp | Bulk email sending, list hygiene, basic analytics | 2,000 contacts, 12,000 sends/mo | Essentials – $11 / month |
| PhantomBuster | Scrape leads, trigger email sequences | 1,000 runs/mo, 1 API call per run | Pro – $49 / month |
| Make.com | Orchestrate Mailchimp ↔️ PhantomBuster workflows | 100 operations/mo, 5 min runtime | Starter – $9 / month |
| Replit | Build & host outreach scripts (Python, Node) | Unlimited public repos | Hacker – $7 / month |
| Zapier | Quick integrations for Slack, CRM, and analytics | 5 zaps, 100 tasks/mo | Starter – $19.99 / month |
| Notion | SOP, contractor onboarding, project tracking | Unlimited pages | Personal Pro – $4 / month |
| Grammarly | Email copy review, tone & style checks | Free | Premium – $30 / year |
| [ElevenLabs](https://elevenlabs.io/) | Voice‑to‑text for voicemail follow‑ups | Free 3 hrs/mo | Pro – $25 / month |

**Estimated time to complete**: 3–4 hours (reading, setting up the stack, creating SOPs, and running a test campaign).

---

## Procedure 7.1: Hire Your First AI Outreach Contractor

1. Open **Replit** (https://replit.com) and click **+ Create** → **New Repl**.  
   - Choose **Python 3** as the language.  
   - Name the repl “Outreach‑Contractor‑Recruit”.  
   - Click **Create Repl**.  
   - Expected output: A fresh Replit workspace with a `main.py` file and a console panel.

2. In the Replit console, type `pip install openai` and press **Enter**.  
   - When the console shows `Successfully installed openai`, you have the OpenAI Python package ready.

3. Create a new file called `job_desc.py`.  
   - Paste the following code snippet (replace `YOUR_API_KEY` with your OpenAI key from https://platform.openai.com/account/api-keys):

   ```python
   import openai

   openai.api_key = "YOUR_API_KEY"

   prompt = """
   Write a concise job description for a freelance AI‑powered cold email outreach contractor who will:
   • Create personalized cold email sequences
   • Use Mailchimp and PhantomBuster for automation
   • Deliver at least 200 qualified leads per week
   • Provide weekly performance reports
   """

   response = openai.Completion.create(
       engine="text-davinci-003",
       prompt=prompt,
       max_tokens=200,
       temperature=0.7,
   )
   print(response.choices[0].text.strip())
   ```

4. Run `job_desc.py` by clicking **▶ Run**.  
   - Verify that the job description prints in the console.  
   - **Interactive check‑in:** Do you see a complete job description? If not, check that your API key is correct and that the console shows no `403` errors.  

---

5. Open **Upwork** (https://www.upwork.com) and log in.  
   - Click **+ Post a Job** (top right).  

6. In the job posting form:  
   - **Title**: “Freelance AI‑Powered Cold Email Outreach Contractor”  
   - **Category**: “Marketing” → “Email Marketing”  
   - [**Description**](https://www.descript.com/): Copy the job description from step 4.  
   - **Hourly Rate**: $30/hr (default)  
   - **Duration**: 6 months (minimum)  
   - **Skill Requirements**: “Mailchimp”, “PhantomBuster”, “Python”, “AI Writing”  
   - Click **Continue** → **Continue** → **Post Job** (bottom).  

7. After posting, you will see a job ID displayed (e.g., `Job # 123456789`).  
   - Copy this ID to your clipboard.  
   - Expected output: Confirmation screen with “Job posted successfully” and the ID number.

8. Open **Apollo.io** (https://www.apollo.io

---

## Procedure 7.2: Draft SOPs for Delegating Email Campaign Tasks

1. **Open Notion**  
   - URL: `https://www.notion.so/`  
   - Click **Sign in** (top‑right), choose **Google** and log in with your work account.  
   - Expected output: You are on the Notion dashboard with your workspace name in the left sidebar.  

2. **Create a new SOP page**  
   - In the left sidebar, click the **+ New Page** button.  
   - Title the page **“Email Campaign SOP – Delegation”**.  
   - Under the title, click **+ Add a block** → **Table – Inline**.  
   - Expected output: A blank table appears beneath the title.  

3. **Configure the table columns**  
   - Click the column header **Name** → **Rename** → `Task`.  
   - Click the **+** to add a new column → **Select** → choose **Person** → rename to `Owner`.  
   - Add a **Date** column → rename to `Deadline`.  
   - Add a **Select** column → rename to `Status`; add options **Not Started**, **In Progress**, **Completed**.  
   - Add a **Text** column → rename to `Notes`.  
   - Expected output: The table now has five columns: Task, Owner, Deadline, Status, Notes.  

4. **Populate the SOP table with core delegation tasks**  
   - Row 1: `Create Campaign List` | Owner: **[Your Name]** | Deadline: *Enter Date* | Status: **Not Started** | Notes: *Use Mailchimp audience import*.  
   - Row 2: `Draft Email Copy` | Owner: **[Copywriter Name]** | Deadline: *Enter Date* | Status: **Not Started** | Notes: *Use ChatGPT 4.0 for first draft*.  
   - Row 3: `Design Email Template` | Owner: **[Designer Name]** | Deadline: *Enter Date* | Status: **Not Started** | Notes: *Use Canva Pro for brand‑compliant design*.  
   - Row 4: `Integrate PhantomBuster Leads` | Owner: **[Data Engineer]** | Deadline: *Enter Date* | Status: **Not Started** | Notes: *Use Make.com scenario to sync leads*.  
   - Row 5: `Schedule Campaign Send` | Owner: **[Campaign Manager]** | Deadline: *Enter Date* | Status: **Not Started** | Notes: *Set send time in Mailchimp*.  

5. **Do you see the completed table with five rows? If not, double‑check that each column header was correctly renamed and that the table contains the rows above.**  

6. **Create a Mailchimp audience for the campaign**  
   - Open a new tab: `https://mailchimp.com/`.  
   - Click **Sign In** → choose your account.  
   - In the left sidebar, click **Audience** → **View audiences** → **Create Audience**.  
   - Title the audience **“Cold Email Outreach – 2026”**.  
   - Accept default settings; click **Save & Continue** → **Create Audience**.  
   - Expected output: Confirmation banner “Audience created” and the new audience appears in the list.  

7. **Import initial leads into Mailchimp**  
   - In the audience view, click **Import Contacts** → **CSV or tabular file**.  
   - Upload your `leads.csv` file (max 5 000 rows free tier).  
   - Map columns: `Email` → `Email Address`, `First Name` → `First Name`, `Last Name` → `Last Name`.  
   - Click **Continue to Review** → **Import**.  
   - Expected output: Import progress bar → “Import complete – 4 500 contacts added”.  

8. **Do you see the imported contacts in the audience? If not, refresh the page or verify the CSV headers match the mapping.**  

9. **Set up a Make.com scenario to auto‑create Notion tasks when a new Mailchimp campaign is launched**  
   - Open `https://www.make.com/` and log in.  
   - Click **Create a new scenario**.  
   - In the search bar, type **Mailchimp** → click **Mail

---

**Procedure 7.3** — Generation failed due to AI backend unavailability. Please retry later.

## Check-In: Module 7 Complete

- [ ] Hire Your First AI Outreach Contractor completed and verified
- [ ] Draft SOPs for Delegating Email Campaign Tasks completed and verified
- [ ] Analyze Profit Margins of Cold Email Campaigns completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 8: ADVANCED PATTERNS

## Overview  
Module 8 dives into the high‑impact playbooks that transform a basic AI‑powered cold email system into a scalable, revenue‑generating machine. You will learn how to layer premium upsells, lock in recurring revenue streams, and productize your outreach services so that each client is a self‑sustaining revenue source. Skipping this module means you’ll be stuck with a one‑off campaign that never turns into a predictable income stream; you’ll miss the opportunity to lock in high‑ticket clients and build a brand that sells itself.

The module’s two procedures are built around Mailchimp (for email distribution) and PhantomBuster (for data extraction and automation), but they also integrate Make.com for orchestrating workflows, and ChatGPT for content generation. By the end of this module you will have a fully automated, AI‑driven outreach engine that not only finds leads but also upsells them to premium packages and enrolls them in recurring funnels. This is the bridge between “sending a single campaign” and “running a profitable, repeatable business model.”

| Tool          | Purpose                                                              | Free Tier                               | Paid Tier                                                                 |
|---------------|----------------------------------------------------------------------|----------------------------------------|---------------------------------------------------------------------------|
| Mailchimp     | Email delivery & analytics                                          | 2,000 contacts, 10,000 sends/month     | Essentials ($13/mo) – 50,000 contacts, 200,000 sends/month                |
| PhantomBuster | Scrape & automate LinkedIn, Twitter, and email discovery             | 5,000 requests/month                   | Pro ($49/mo) – 50,000 requests/month, 30 min pause between requests       |
| Make.com      | Workflow automation between Mailchimp, PhantomBuster, and CRM        | 500 operations/month                   | Creator ($29/mo) – 15,000 operations/month, 1 min pause between tasks      |
| ChatGPT       | AI content generation (subject lines, email copy, follow‑ups)       | 1,000 tokens/day (free)                | ChatGPT‑Plus ($20/mo) – Unlimited tokens, priority access                 |
| Notion        | Project planning & documentation                                    | Unlimited pages & blocks               | Team ($8/user/mo) – Advanced permissions, API access                      |
| Grammarly     | Grammar & style checking for email copy                             | Unlimited text, basic checks           | Premium ($12/mo) – Advanced tone, plagiarism check, business style       |

**Estimated time to complete Module 8:** 5 hours (includes reading, tool setup, and execution of both procedures).

---

## Procedure 8.1: Package Your AI Cold Email Service Into a High‑Ticket Offer

1. **Create a dedicated Notion workspace**  
   - URL: <https://www.notion.so/signup>  
   - Click **“SIGN UP”** with your professional email.  
   - After login, click **“+ NEW PAGE”** in the left sidebar, name it **“AI Cold Email Offer”**, and set the icon to a **“📩”**.  
   - Expected result: A blank page titled *AI Cold Email Offer* appears.

2. **Set up an Airtable base for client pipeline**  
   - URL: <https://airtable.com/signup>  
   - Click **“Create a base from scratch”** → name it **“Cold Email Pipeline”**.  
   - Add the following fields:  
     - *Client Name* (Single line text)  
     - *Email* (Email)  
     - *Lead Source* (Single select: LinkedIn, Apollo, Other)  
     - *Deal Stage* (Single select: Prospect, Demo, Proposal, Closed)  
     - *Ticket Price* (Currency)  
   - Expected result: A table with the five columns above.

3. **Create a Mailchimp account and obtain an API key**  
   - URL: <https://mailchimp.com/> → click **“SIGN IN”** → **“Get Started”** (free tier).  
   - In the top right, click your profile icon → **“Account”** → **“Extras”** → **“API keys”**.  
   - Click **“Create A Key”**, copy the key, and store it in a password manager.  
   - Expected result: API key is visible on the screen.

4. **Create a new Mailchimp audience**  
   - In Mailchimp, go to **“Audience”** → **“View audiences”** → **“Create Audience”**.  
   - Name it **“Cold Email Leads”**.  
   - Under **“Settings”** → **“Audience name & defaults”**, set the default email address to **support@yourdomain.com**.  
   - Expected result: Audience *Cold Email Leads* is listed with default email.

5. **Generate email copy with ChatGPT**  
   - Open <https://chat.openai.com/> → click **“New Chat”**.  
   - Prompt:  
     ```
     I need a cold email to software founders offering a high‑ticket AI cold‑email service.  
     Include a 3‑sentence hook, a problem statement, and a call‑to‑action for a 30‑minute demo.  
     Keep it under 150 words.  
     ```
   - Copy the generated text into a Notion block titled **“Draft Email Copy”**.  
   - **Do you see the email draft?** If not, refresh the chat window and try again.

6. **Create a header image with Canva**  
   - URL: <https://www.canva.com/> → click **“SIGN UP”** → choose **“Free”** plan.  
   - Click **“Create a design”** → **“Email header”** (1200 × 400 px).  
   - Use the left panel to add a background image, overlay text “AI‑Powered Lead Generation”, and adjust font to **Montserrat, 48 pt**.  
   - Click **“Download”** → select **PNG** → click **“Download”**.  
   - Save the PNG to your computer.  
   - Expected result: A PNG file named *header.png*.

7. **Upload header image to Mailchimp**  
   - In Mailchimp, click **“Campaigns”** → **“Create a Campaign”** → **“Email”** → **“Regular”**.  
   - Name the campaign **“High‑Ticket Offer Launch”**.  
   - In the **“Design”** step, click **“Add image”** → **“Upload”** → choose *header.png*.  
   - Drag the image to the top of the email.  
   - Expected result: Header image appears in the email builder.

8. **Insert the drafted copy into the email body**  
   - In the same Mailchimp campaign, delete the placeholder text.  
   - Click **“Copy & paste”** from the Notion block *Draft Email Copy* into the body.  
   - Highlight the email body, click **“Link”** (chain icon), and paste the link to the Notion page for future edits.  
   - Expected result: Email body contains the copy with a working link to Notion.

9. **Automate lead scraping

---

## Procedure 8.2: Launch a Subscription‑Based Upsell for AI Outreach

1. **Open a web browser and navigate to Mailchimp.**  
   URL: <https://mailchimp.com/>  
   Click the **“Sign up free”** button in the top‑right corner.  
   *Expected output:* A registration form with fields for **Email address**, **Password**, and **Company name**.  

2. **Fill out the Mailchimp registration form.**  
   - Email: `yourname@yourdomain.com`  
   - Password: `StrongPass!2026` (at least 12 characters, one number, one symbol)  
   - Company name: `AI Outreach Co.`  
   Click the **“Get started”** button.  

3. **Verify your email address.**  
   Open your inbox, locate the Mailchimp verification email, and click the **“Confirm my account”** link.  
   *Expected output:* Browser redirects to the Mailchimp dashboard.  

4. **Create an audience for your outreach leads.**  
   - From the dashboard, click **Audience** > **Manage Audience** > **Add a new audience**.  
   - Name: `Cold Email Leads`  
   - Contact info: `aioutreach@yourdomain.com`  
   - Default audience settings: unchecked **“Track opens and clicks”** (we’ll track manually).  
   - Click **“Create audience”**.  
   *Do you see the new audience listed? If not, refresh the page or check the **“All audiences”** tab.*  

5. **Enable the signup form for the audience.**  
   - Inside the audience, click **Audience dashboard** > **Signup forms** > **Subscriber pop‑up**.  
   - Set the theme to **Light**.  
   - Under **Form fields**, ensure **First name** and **Last name** are checked.  
   - Click **“Save”**.  

6. **Create a landing page for the upsell offer.**  
   - In the dashboard, click **Campaigns** > **Create Campaign** > **Landing page**.  
   - Name: `AI Outreach Upsell`  
   - Click **“Create”**.  
   - In the editor, drag a **Header** block, type **“Upgrade to AI‑Powered Outreach”**.  
   - Drag a **Text** block below, paste:  
     ```
     Unlock unlimited AI‑generated cold emails, real‑time analytics, and priority support.  
     Start a 14‑day free trial today!
     ```  
   - Drag a **Button** block, set text to **“Start Free Trial”**.  
   - Under **Button settings**, set link to `https://checkout.stripe.com/pay/cs_test_123456` (placeholder).  
   - Click **“Publish”**.  
   *Expected output:* A live URL in the form `https://yourdomain.com/ai-outreach-landing`.  

7. **Create a Stripe account for billing.**  
   URL: <https://dashboard.stripe.com/register>  
   - Email: `yourname@yourdomain.com`  
   - Password: `StrongPass!2026`  
   - Click **“Create account”**.  

8. **Add a product in Stripe.**  
   - In the Stripe dashboard, click **Products** > **+ Add product**.  
   - Name: `AI Outreach Monthly Subscription`  
   - Description: `$49/month for unlimited AI‑generated cold emails and analytics.`  
   - Set **Price**: `$49.00` recurring, monthly.  
   - Click **“Add price”**.  
   - Click **“Save product”**.  
   *Do you see the product listed under “Products”? If not, double‑check the product name or refresh the page.*  

9. **Create a Checkout Session link.**  
   - Click **Payments** > **Checkout** > **+ New Checkout Session**.  
   - Product: `AI Outreach Monthly Subscription`  
   - Success URL: `https://yourdomain.com/thank-you`

## Check-In: Module 8 Complete

- [ ] Package Your AI Cold Email Service Into a High‑Ticket Offer completed and verified
- [ ] Launch a Subscription‑Based Upsell for AI Outreach completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 9: FINANCIAL OPERATIONS

## Overview  
This module arms you with a command‑center for the money side of your AI‑driven cold‑email agency. You’ll learn how to design a real‑time revenue dashboard, lock in predictable profit margins through systematic pricing ramps, and craft legally sound proposal & contract templates that close deals faster. If you skip this module, you’ll be left chasing invoices in a spreadsheet, charging arbitrarily, and vulnerable to disputes—exactly the conditions that kill early‑stage AI services.

You’ll build a modular financial hub that pulls data from Mailchimp, PhantomBuster, and your billing system, then pushes updates to Notion and Zapier for instant visibility. With ChatGPT‑generated proposal blocks, you’ll standardize your pitch language while saving hours of copy‑editing. The end result is a repeatable, auditable workflow that scales with your client base, not your manual labor.

**Estimated time to complete:** 4 – 5 hours (including setup, data mapping, and template drafting).  

| Tool          | Purpose                                      | Free Tier                        | Paid Tier (Monthly) |
|---------------|----------------------------------------------|----------------------------------|---------------------|
| Notion        | Central dashboard & contract repository      | Unlimited pages, 5 MB storage    | Plus: $4.00 (All‑features) |
| Zapier        | Automate data sync (Mailchimp → Notion)      | 100 tasks, single‑step zaps      | Professional: $19.99 (Unlimited tasks) |
| Make.com      | Advanced workflow orchestration              | 250 operations, 60 min runtime   | Team: $49.00 (Unlimited) |
| Canva         | Design proposal PDF templates                | Unlimited templates, 5 GB storage| Pro: $12.99 (Premium assets) |
| ChatGPT (OpenAI) | Generate proposal language & pricing tables | 3 M tokens/month (free)         | ChatGPT‑4: $20.00 (Standard) |
| PhantomBuster | Pull lead data & send cold emails           | 10 000 actions/month (free)     | Premium: $49.00 (Unlimited) |

---

---

## Procedure 9.1: Configure a Real‑Time Revenue Dashboard with Google Data Studio  

**Objective:** Build a live revenue dashboard that pulls daily email‑outreach metrics from Mailchimp and PhantomBuster, stores them in Google Sheets, and visualises them in Google Data Studio.  

**Tools & Pricing (as of 2026‑07‑11)**  

| Tool | Free Tier | Paid Tier | Notes |
|------|-----------|-----------|-------|
| **Google Data Studio** | Unlimited | N/A | Completely free |
| **Google Sheets** | Unlimited | N/A | Included with Google Drive |
| **Mailchimp** | 2,000 contacts, 12,000 emails/month | Essentials: $9.99/mo

---

## Procedure 9.2: Draft Standard AI Outreach Service Pricing Contracts

1. **Open Notion**  
   - URL: https://www.notion.so  
   - Log in with your workspace credentials.  
   - In the left sidebar, click **Create new page** (button **+ New Page**).  
   - Title the page **“AI Outreach Pricing Contract Template.”**  
   - Choose **“Table – Full page”** from the template options.  
   - Expected result: A blank table with columns “Field,” “Description,” “Default Value,” and “Notes.”  

2. **Populate Contract Skeleton**  
   - In the first row, under **Field**, type **“Client Name.”**  
   - Under **Description**, type **“Full legal name of the client.”**  
   - Under **Default Value**, leave blank.  
   - Repeat for the following fields:  
     1. Project Scope  
     2. Service Level (Monthly Outreach Volume)  
     3. Pricing Model (Fixed + Variable)  
     4. Payment Terms  
     5. Term & Renewal  
     6. Confidentiality Clause  
     7. Termination Conditions  
     8. Governing Law  
   - Expected output: A 8‑row table ready for data entry.  

3. **Insert Pricing Table**  
   - In row 4, under **Field**, type **“Pricing Table.”**  
   - Under **Description**, type **“Breakdown of fixed & variable fees.”**  
   - Click the empty cell in **Default Value** and select **“Toggle list.”**  
   - Inside the toggle, insert a Markdown table:  
     ```
     | Service Component | Fixed Monthly ($) | Variable ($ per 1,000 emails) | Notes |
     |-------------------|-------------------|------------------------------|-------|
     | Setup & Integration | 200 | 0 | Includes PhantomBuster setup |
     | Monthly Outreach | 0 | 0.05 | Calculated per 1,000 emails |
     | AI Content Generation | 100 | 0 | Fixed for first 5,000 emails |
     | Reporting & Analytics | 50 | 0 | Included |
     ```
   - Expected output: A neatly formatted Markdown table inside the toggle.  

4. **Add Client‑Specific Variables**  
   - Under **Service Level**, set **Default Value** to **“10,000 emails/month.”**  
   - Under **Pricing Model**, set **Default Value** to **“Fixed + Variable.”**  
   - Under **Payment Terms**, set **Default Value** to **“Net 30 days upon invoice.”**  
   - Check: Do you see the updated values in the table?  
     - If not, refresh the page and verify you are editing the correct row.  

5. **Create a PDF Export Block**  
   - In a new row, type **“Export PDF.”**  
   - Under **Description**, type **“Button to generate PDF contract.”**  
   - Click the empty cell in **Default Value** and select **“Button.”**  
   - Configure the button:  
     - **Name**: Export to PDF  
     - **Action**: “Export a page as PDF.”  
     - **Target**: Current page (auto‑selected).  
   - Expected output: A button labeled **Export to PDF** at the bottom of the Notion page.  

6. **Generate Contract Draft in ChatGPT**  
   - Open ChatGPT (https://chat.openai.com) with the paid plan ($20/month).  
   - Paste the following prompt:  
     ```
     Draft a professional AI outreach service contract using the following template fields:
     Client Name: [Client Name]
     Project Scope: [Project Scope]
     Service Level: [Service Level]
     Pricing Model: [Pricing Model]
     Payment Terms: [Payment Terms]
     Term & Renewal: [Term & Renewal]
     Confidentiality Clause: [Confidentiality Clause]
     Termination Conditions: [Termination Conditions]
     Governing Law: [Governing Law]
     Pricing Table: (include the Markdown table above)
     ```
   - Press **Enter**.  
   - Wait for the response.  
   - Expected output: A full contract text in Markdown format.  

7. **Copy Contract Text to Notion**  
   - Select all text from ChatGPT’s response.  
   - Return to Notion and paste into the **Default Value** cell of the **Pricing Table** row (inside the toggle).  
   - The contract should now appear as a single block beneath the table.  

8. **Insert Conditional Clauses**  
   - In the contract block, add the following conditional clause after the “Pricing Table”:  
     ```
     • Variable fees may be adjusted if monthly outreach volume exceeds 20,000 emails.
     • Additional AI content generation beyond 5,000 emails will be billed at $0.02 per 1,000 emails.
     ```
   - Press **Enter** to separate the clauses.  
   - Check: Do you see the new clauses formatted correctly?  
     - If not, ensure you are inside the Markdown block and not in the table header.  

9. **Add Signature Fields**  
   - Scroll to the bottom of the contract block.  
   -

## Check-In: Module 9 Complete

- [ ] Configure a Real‑Time Revenue Dashboard with Google Data Studio completed and verified
- [ ] Draft Standard AI Outreach Service Pricing Contracts completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 10: LAUNCH PLAN

## Overview

This module delivers a **30‑day, day‑by‑day execution calendar** that takes you from zero to your first paying client for an AI‑powered cold email outreach service. We will walk you through every step—from setting up Mailchimp campaigns and automating lead extraction with PhantomBuster, to integrating AI content generators like ChatGPT and managing follow‑ups with Make.com. By the end of the month, you’ll have a fully functional, scalable outreach engine that continually feeds qualified leads into your sales funnel.

Skipping this module means you’ll reinvent the wheel each time you launch a new campaign. You’ll miss the proven cadence that ensures consistent deliverability, high engagement rates, and measurable ROI. The risk is wasted time on manual research, inconsistent email cadences, and poor data hygiene—factors that historically kill 80 % of cold‑email programs before they even launch.

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| **Mailchimp** | Email campaign management, list segmentation, A/B testing | 2 000 contacts, 10 000 sends/month | $11/month (Essentials) |
| **PhantomBuster** | Scrape LinkedIn, Twitter, and other sites for leads | 200 actions/month | $49/month (Pro) |
| **Make.com** | Automate workflows between PhantomBuster, Mailchimp, and ChatGPT | 500 tasks/month | $18/month (Starter) |
| **Zapier** | Quick automation between Mailchimp, Calendly, and CRM | 100 tasks/month | $19/month (Starter) |
| **Notion** | Project dashboard, daily check‑ins, task tracking | Unlimited pages, 5 MB file uploads | $8/month (Personal Pro) |
| **Grammarly** | AI‑powered copy editing for email subject lines & body | Unlimited checks, 1 GB upload | $12/month (Premium) |

**Estimated time to complete:** 30 consecutive days of daily execution, plus an initial 1‑hour setup phase to configure each tool and build the workflow skeleton.

---

## Procedure 10.1: Start Your AI Cold Email Campaign with Mailchimp & PhantomBuster

1. **Open your web browser** and navigate to the Mailchimp free‑tier sign‑up page:  
   `https://mailchimp.com/signup/`.  
   *Enter your email, create a password, and click **Sign up**.*

2. **Confirm your email** by clicking the link sent to the inbox you used.  
   *You should see a Mailchimp welcome screen with a banner that says “Welcome to Mailchimp.”*

3. **In the Mailchimp dashboard, click the button labeled **Create Campaign** (top‑right corner).**  
   *A modal appears titled “Create a Campaign.”*

4. **Select “Email” from the options.**  
   *The next screen shows “Campaign type” with options: Regular, Plain‑Text, Automation, RSS. Click **Regular** and then **Begin**.*

5. **Do you see the “Campaign name” field?**  
   If not, check that you are on the Regular email campaign page.  
   *Enter “AI Cold Outreach – Phase 1” and click **Save & Continue**.*

6. **Choose a recipient list.**  
   - If you have no list, click **Add a list** (button).  
   - In the popup, select **Create a new list**.  
   - Fill in the list name “Cold Leads 2026”, default email address `sales@yourcompany.com`, and click **Create List**.  
   *You should now see the list “Cold Leads 2026” selected.*

7. **Set up the email subject line.**  
   - Click the text field next to “Subject line” and type: `🚀 Unlock Your Next Lead with AI`.  
   - Click **Save & Continue**.

8. **Configure the email from name and address.**  
   - Set **From name** to `Your Name`.  
   - Set **From email** to `sales@yourcompany.com`.  
   - Click **Save & Continue**.  

9. **Do you see the “Design Email” canvas?**  
   If not, ensure you clicked **Save & Continue** after the subject line step.  

10. **Select “Design Email” → **Drag & Drop** editor.**  
    - On the left panel, click **Text** → drag a **Header** block to the canvas.  
    - In the header, type “Hello {{first_name}},” and click **Save**.  
    - Drag a **Text** block below the header and type the AI‑generated body:  
      ```
      I’ve built a quick AI tool that predicts the best outreach timing for your prospects.  
      Want to see a free demo? Let’s schedule a 15‑minute call.  
      ```  
    - Click **Save**.

11. **Add a CTA button.**  
    - Drag a **Button** block, set the text to “Schedule a Call,” link to `https://calendly.com/yourname/15min`.  
    - Click **Save**.

12. **Insert dynamic content for personalization.**  
    - In the **Header** block, replace `{{first_name}}` with a *Merge Tag* by clicking the **Insert Merge Tag** icon and selecting *First Name*.  
    *If you see an error “Merge tag not found,” it means the list doesn’t have a “first_name” field. Fix it by adding a “First Name” column in the list under **Audience** → **Manage Audience** → **Add a Field** → **Text Field** → “First Name.”*

13. **Do you see the preview icon (eye icon) at the top‑right?**  
    If not, scroll to the top of the editor.  

14. **Click the preview icon** to view the email in desktop and mobile views.  
    - Verify the merge tag displays correctly in both views.  
    - Click **Close**.

15. **Open a new tab and go to `https://phantombuster.com/`.**  
    *Sign up using the same email, or log in if you already have an account.*

16. **Navigate to the dashboard → click **Create a new script**.**  
    - Choose **Phantom** → **LinkedIn Lead Gen** (example) or **Custom Phantom** if you have a custom API.  
    - Click **Create**.

17. **In the script editor, paste the following code snippet** (this pulls prospects from LinkedIn and writes them to a Google Sheet; adapt if you use a CSV):  
    ```js
    const { LinkedIn } = require('phantombuster');
    const sheet = new GoogleSheets('YourSpreadsheetID');
    const profileUrls = ['https://www.linkedin.com/in/user1', 'https://www.linkedin.com/in/user2'];
    
    profileUrls.forEach(async url => {
      const profile = await LinkedIn.getProfile(url);
      sheet.appendRow([profile.firstName, profile.lastName, profile.email]);
    });
    ```  
    - Replace `YourSpreadsheetID` with the ID from your Google Sheet.  
    - Click **Save** → **Run** → **Schedule** → choose **Daily** at 9 AM.

18. **Do you see the “Schedule” window with the daily trigger?**  
    If not, click the

---

## Procedure 10.2: Configure Automated Lead Extraction Using PhantomBuster  

1. **Open PhantomBuster** – Go to https://phantombuster.com/.  
2. Click **SIGN UP** in the upper‑right corner.  
3. Enter your email (e.g., `you@yourdomain.com`), password (`StrongPass!123`), and tick **I agree to the Terms of Service**.  
4. Click **CREATE ACCOUNT**.  
5. **Do you see the “Dashboard” screen with a blue “Start a new process” button?** If not, refresh the page or clear your browser cache.

6. Click the **START A NEW PROCESS** button.  
7. In the search bar type **“LinkedIn Lead Gen”** and select the Phantom named **“LinkedIn Lead Gen”**.  
8. Click **ADD THIS PHANTOM**.  
9. Click **BEGIN CONFIGURATION**.  
10. In the **Account** tab, click **ADD ACCOUNT**.  

11. In the popup, enter your LinkedIn credentials:  
    - **Username**: `yourlinkedinemail@company.com`  
    - **Password**: `YourLinkedInPass!`  
    - Click **SAVE & CONNECT**.  
12. In the **Target** tab, select **LinkedIn Search**.  
13. Paste the search URL you want to scrape (e.g., `https://www.linkedin.com/search/results/people/?keywords=marketing%20manager&origin=GLOBAL_SEARCH_HEADER`).  
14. Click **SAVE**.  
15. **Do you see the “Schedule” tab with a green “START” button?** If not, return to the previous tab and click **SAVE** again.

16. In the **Schedule** tab, set:  
    - **Run frequency**: **Once**  
    - **Start time**: Current time + 5 minutes  
    - **Max requests/sec**: 2 (to stay within the free tier limit)  
    - Click **SCHEDULE**.  
17. Wait until the process status changes to **“Running”**.  
18. Once complete, click **DOWNLOAD** and choose **CSV**.  
19. **Do you see a CSV file named `LinkedInLeadGen_YYYYMMDD.csv` in your Downloads folder?** If not, go to **PHANTOM STATS** and click **RETRY**.

20. Open **Google Sheets** (https://docs.google.com/spreadsheets/).  
21. Create a new sheet titled **“Lead Extraction”**.  
22. In cell **A1**, type `Name`. In **B1**, type `Headline`. In **C1**, type `Email`.  
23. Import the CSV:  
    - Click **File > Import > Upload**.  
    - Drag the CSV file into the box and select **Replace current sheet**.  
24. In column **C**, use a formula to extract emails from the LinkedIn profile URL:  
    - `=REGEXEXTRACT(A2, "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")`  
    - Drag down to fill all rows.  
25. **Do you see a list of names, headlines, and extracted emails?** If emails are blank, the LinkedIn profile may not contain a public email. Use a separate Phantom (e.g., “Hunter.io Lead Gen”) or manually add emails.

---

### Error Scenario  

- **If you see “Rate limit exceeded” in the Phantom logs** – this means you have hit the free tier limit of 100 requests per month.  
  - **Fix**: Upgrade to the **Basic** plan ($9/month) or reduce the **Max requests/sec** to 1 and reschedule.

---

### Table 1 – PhantomBuster Pricing & Free Tier

| Plan | Monthly Cost | Monthly Requests | Unlimited Requests |
|------|--------------|------------------|--------------------|
| Free | $0 | 100 | No |
| Basic | $9 | 500 | No |
| Pro | $29 | Unlimited | Yes |

---

### Table 2 – Lead Extraction Output Sample

| Name | Headline | Email |
|------|----------|-------|
| Jane Doe | Marketing Manager at ABC Corp | jane.doe@abc.com |
| John Smith | Senior Lead Gen Specialist | john.smith@xyz.com |

---

**Outcome**: You now have an automated pipeline that pulls LinkedIn leads into a Google Sheet, ready for mass‑email outreach via Mailchimp. The next step will be to import this sheet into Mailchimp and set up the AI‑powered cold email sequences.

---

## Procedure 10.3: Deploy Dynamic Email Segmentation in Mailchimp

1. **Open your browser** and go to [https://mailchimp.com/](https://mailchimp.com/).  
2. In the top right corner click **Sign In** (exact button text **Sign In**).  
3. Enter your **email address** and **password**, then click **Log In**.  
4. You arrive at the **Dashboard**. In the left‑hand menu click **Audience** → **All contacts**.  
   - *Do you see the “All contacts” page with a blue “View reports” button?*  
   - *If not, refresh the page or clear the cache.*  

5. Click the **Manage contacts** drop‑down button, then select **Segments**.  
6. On the Segments page click the **Create segment** button (top right, label **Create segment**).  
7. In the **Segment builder** window, set the first rule:  
   - **Field**: **Tags**  
   - **Operator**: **is**  
   - **Value**: **Lead**  
   (Select each dropdown by clicking and choosing the exact option).  
8. Click **Add another rule** (the thin blue button).  
   - *Do you see the “Add another rule” button?*  
   - *If it is gray, you may need to upgrade your Mailchimp plan to “Premium”.*  

9. For the second rule set:  
   - **Field**: **Signup Source**  
   - **Operator**: **is**  
   - **Value**: **LinkedIn**  
10. Click **Save** (bottom right, label **Save**).  
    - *Expected output*: A new segment named “Lead – LinkedIn” appears in the list with the count of contacts that match.  

11. Open a new tab and go to [https://make.com/](https://make.com/).  
12. Click **Log in** (top right). Use your existing Make account or sign up (free tier allows 1,000 operations/month).  
    - *Do you see the dashboard with “Create a new scenario” button?*  
    - *If not, check that you are logged into the correct domain.*  

13. Click **Create a new scenario**. In the scenario editor, click the plus icon (+) and search for **Mailchimp**.  
    - Select the **Mailchimp – Add a subscriber** module.  
    - Click **Continue**.  
14. Click **Add a connection** to connect your Mailchimp account.  
    - In the popup, click **Authorize**.  
    - In the permission window, click **Authorize** again.  
    - *Expected output*: A green checkmark and “Connected” status beside the module.  

15. Click the plus icon (+) again, search for **PhantomBuster**.  
    - Select **PhantomBuster – Run a phantom**.  
    - Click **Continue**.  
16. In the PhantomBuster module, set:  
    - **Phantom**: **LinkedIn Lead Gen** (exact name from your PhantomBuster library)  
    - **Parameters**:  
      - **URL**: `https://www.linkedin.com/in/{profile}` (leave placeholder)  
      - **Token**: `{{phantombuster_api_token}}` (replace with your API token from PhantomBuster).  
    - Click **Save**.  
    - *Do you see the PhantomBuster module with “LinkedIn Lead Gen” selected?*  
    - *If the Phantom name does not appear, refresh the module list or check your PhantomBuster API key.*  

17. Click the arrow from the PhantomBuster module to the Mailchimp module to link them.  
18. In the Mailchimp module, map the fields:  
    - **Email address** → `{{phantombuster_results.email}}`  
    - **First name** → `{{phantombuster_results.first_name}}`  
    - **Last name** → `{{phantombuster_results.last_name}}`  
    - **Tags** → **Lead** (type “Lead” into the Tags field).  
19. Click the **Run once** button (top left, label **Run once**).  
    - Wait for execution to finish. The log will show **“1 subscriber added”**.  
    - *Expected output*: The subscriber appears in Mailchimp under **Audience** → **All contacts** with the tag “Lead”.  

20. Return to Mailchimp. In the **Segments** page, click **Create segment** again.  
    - Use the rule: **Tags** → **is** → **Lead**.  
    - Add a second rule: **Custom field** → **Lead score** → **greater than** → **70**.  
    - Save as **High‑Value Leads**.  

### Error Scenario  
If during step 15 you see **“Invalid API key”**:  
- *Cause*: Your PhantomBuster API token is incorrect or expired.  
- *Fix*: Go to PhantomBuster > Settings >

## Check-In: Module 10 Complete

- [ ] Start Your AI Cold Email Campaign with Mailchimp & PhantomBuster completed and verified
- [ ] Configure Automated Lead Extraction Using PhantomBuster completed and verified
- [ ] Deploy Dynamic Email Segmentation in Mailchimp completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# APPENDIX A: COMPLETE TOOL REFERENCE  

| Tool | Purpose | Free Tier | Paid Tier | When to Upgrade |
|------|---------|-----------|-----------|-----------------|
| **Hostinger** | Domain registration, email forwarding, low‑cost VPS hosting | Free domain registration for 1 year with a Hostinger account; 1 GB storage, 10 GB bandwidth, 1 GB email quota | Starter VPS: $2.99 / month (10 GB storage, 100 GB bandwidth, 10 GB email) <br>Business VPS: $4.99 / month (20 GB storage, 200 GB bandwidth, 20 GB email) | Upgrade when lead volume exceeds 10 GB of traffic or when you need dedicated IP for email deliverability. |
| **Make.com** | Automate data collection, sync Mailchimp → Google Sheets → PhantomBuster | 100 operations/month, 2 GB of data transfer | Starter: $19 / month (5 000 operations, 10 GB transfer) <br>Advanced: $49 / month (50 000 ops, 100 GB transfer) | Upgrade when you hit 80 % of the free quota or need > 5 k operations to keep up with daily lead scraping. |
| **PhantomBuster** | Scrape LinkedIn leads, verify email deliverability, export CSV | 10 requests/day, 1 GB data export | Starter: $19 / month (200 requests/day, 5 GB export) <br>Pro: $49 / month (500 requests/day, 20 GB export) | Upgrade when you need > 200 requests/day or when you exceed 5 GB of exported data per month. |
| **Mailchimp** | Campaign automation, list management, A/B testing | 2 000 contacts, 10 000 sends/month, 1 000 subscribers per list | Essentials: $10 / month (up to 500 contacts, 12 000 sends) <br>Standard: $20 / month (up to 2 500 contacts, 24 000 sends) <br>Premium: $90 / month (up to 10 000 contacts, 60 000 sends) | Upgrade when contacts > 2 000 or when you need advanced segmentation and multivariate testing. |
| **Google Sheets** | Data storage, real‑time collaboration, integration with Make.com | Unlimited sheets, 15 GB of total file storage | Included in Google Workspace Business Starter: $6 / user/month (100 GB storage) | Upgrade to Workspace Business if you need more than 15 GB of file storage or advanced admin controls. |
| **Zapier** | Connect Mailchimp, PhantomBuster, Google Sheets, and other SaaS tools | 100 tasks/month, 5 Zaps | Starter: $19.99 / month (750 tasks, 20 Zaps) <br>Professional: $49 / month (2 000 tasks, 50 Zaps) | Upgrade when you hit 80 % of free tasks or need to add more Zaps for complex workflows. |
| **Apollo.io** | Lead enrichment, email finder, outreach sequencing | 5 000 contact searches/month, 500 email sends | Team: $99 / month (20 000 searches, 2 000 sends) <br>Enterprise: $499 / month (100 000 searches, 10 000 sends) | Upgrade when your daily lead scrape exceeds 5 000 searches or when you need bulk email capabilities. |
| **Notion** | Project management,

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

This appendix is your instant‑on‑demand operating system that turns the raw numbers from the playbook into a crystal‑clear financial roadmap. Follow the steps exactly; the calculator will load in a Google Sheet, populate all projections, and give you a real‑time break‑even window. No guessing, no spreadsheet gymnastics—just the data you need to scale.

---

## 1. Set Up the Master Sheet

1. **Open Google Sheets**  
   - URL: `https://docs.google.com/spreadsheets/`  
   - Click **Blank** to create a new spreadsheet.

2. **Rename the file**  
   - Double‑click the title bar and type **“Menshly Revenue Calculator – AI Cold Email”**.

3. **Create three sheets**  
   - At the bottom left, click the **+** icon three times.  
   - Rename the tabs:  
     1. **Revenue Projections**  
     2. **Pricing Tiers**  
     3. **Break‑Even Analysis**

4. **Set up shared access**  
   - Click **Share** top‑right.  
   - Enter the email of any collaborator and set role to **Editor**.  
   - Click **Send**.

> **Do you see three tabs now?**  
> If not, refresh the page or click the **+** again.  

---

## 2. Populate the Revenue Projections Sheet

| Cell | Value / Formula | Explanation |
|------|-----------------|-------------|
| A1 | **Month** | Header |
| B1 | **Revenue** | Header |
| C1 | **Clients** | Header |
| D1 | **Expenses** | Header |
| E1 | **Profit** | Header |
| A2 | **1** | Month 1 |
| A3 | **3** | Month 3 |
| A4 | **6** | Month 6 |
| A5 | **12** | Month 12 |
| B2 | =C2*D2 | Revenue = Clients × Price per Client |
| B3 | =C3*D3 | Revenue = Clients × Price per Client |
| B4 | =C4*D4 | Revenue = Clients × Price per Client |
| B5 | =C5*D5 | Revenue = Clients × Price per Client |
| C2 | **5** | Clients in Month 1 |
| C3 | **15** | Clients in Month 3 |
| C4 | **30** | Clients in Month 6 |
| C5 | **60** | Clients in Month 12 |
| D2 | **$2,000** | Price per client (Tier 2) |
| D3 | **$2,000** | Same price |
| D4 | **$2,000** | Same price |
| D5 | **$2,000** | Same price |
| E2 | =B2-D2 | Profit = Revenue – Expenses |
| E3 | =B3-D3 | Profit = Revenue – Expenses |
| E4 | =B4-D4 | Profit = Revenue – Expenses |
| E5 | =B5-D5 | Profit = Revenue – Expenses |

> **Do you see the formulas working?**  
> If any cell shows `#VALUE!`, double‑click the cell, press **Enter**, and confirm the formula starts with `=`.

---

## 3. Build the Pricing Tiers Sheet

| Cell | Value / Formula | Explanation |
|------|-----------------|-------------|
| A1 | **Tier** | Header |
| B1 | **Price** | Header |
| C1 | **Deliverables** | Header |
| D1 | **Margin** | Header |
| A2 | **Basic** | Tier 1 |
| B2 | **$1,200** | Monthly fee |
| C2 | **10 cold emails, 2 follow‑ups** | Deliverables |
| D2 | =B2*0.20 | 20 % margin (example) |
| A3 | **Standard** | Tier 2 |
| B3 | **$2,000** | Monthly fee |
| C3 | **30 cold emails, 3 follow‑ups, email copy** | Deliverables |
| D3 | =B3*0.25 | 25 % margin |
| A4 | **Premium** | Tier 3 |
| B4 | **$4,000** | Monthly fee |
| C4 | **Unlimited cold emails, 5 follow‑ups, AI‑generated copy, analytics** | Deliverables |
| D4 | =B4*0.30 | 30 % margin |

> **Do you see the calculated margins?**  
> If any margin shows `#DIV/0!`, ensure the price cell is numeric.

---

## 4. Draft the Break‑Even Analysis Sheet

1. **Set up constants**  
   - A1: **Initial Investment**  
   - B1: **$3,500** (Hostinger domain $10, Mailchimp free tier, PhantomBuster free tier, Canva free tier, 30‑day Replit trial, 1‑month Zapier free tier)  
   - A2: **Monthly Profit**  
   - B2: =E5 (profit from Month 12, the highest monthly profit)

2. **Calculate months to break‑even**  
   - A4: **Months to Break‑Even**  
   - B4: =ROUNDUP(B1/B2,0)

3. **Break‑Even Timeline**  
   - A6: **Month**  
   - B6: **Cumulative Profit**  
   - A7: **1**  
   - B7: =E2 (Month 1 profit)  
   - A8: **3**  
   - B8: =B7+E3 (Profit up to Month 3)  
   - A9: **6**  
  

For the free step-by-step guide, see our [implementation guide]({< ref "/intelligence/build-an-ai-data-analysis-automation-service-with-chatgpt-the-complete-step-by-s.md" >}).


## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
