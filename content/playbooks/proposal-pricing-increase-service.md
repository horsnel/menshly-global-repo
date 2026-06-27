---
title: "Proposal: Pricing Increase Service"
date: 2026-06-27
category: "Playbook"
price: "₦25,000"
readTime: "89 MIN"
excerpt: "This is your complete operating system for Launch, manage, and scale an AI-powered lead generation business with Apollo.io and Notion. The AI Playbook: 25 Steps to $25K/Month. 25 procedures. 10 modules. 12+ hours of reading and execution. Follow ever..."
image: "/images/articles/playbooks/proposal-pricing-increase-service.png"
heroImage: "/images/heroes/playbooks/proposal-pricing-increase-service.png"
relatedOpportunity: "/opportunities/how-to-build-an-ai-lead-generation-agency-10k-20kmonth/"
relatedGuide: "/intelligence/build-an-ai-social-media-management-tool-with-chatgpt-the-complete-step-by-step-/"
---
This is your complete operating system for Launch, manage, and scale an AI-powered lead generation business with Apollo.io and Notion. **The AI Playbook: 25 Steps to $25K/Month.** **25 procedures. 10 modules. 12+ hours of reading and execution.** Follow every procedure in order and you will have a fully operational business generating revenue within 30 days. Skip nothing. Every step exists because someone before you failed by skipping it.

---

# MODULE 1: FOUNDATION

## Overview

Welcome to the Foundation module – the launchpad that turns a raw idea into a fully‑functional AI‑powered lead‑generation engine. In this module you will register your business accounts, wire up a professional domain, create a dedicated email inbox, and install the core productivity stack that will keep your operations humming. Without this foundational layer every subsequent step collapses: Apollo.io can’t pull data because your API keys are missing, Notion can’t sync your lead database, and your email domain will bounce every outreach attempt. Skipping any of these tasks will result in wasted time, lost data, and a brand that looks unprofessional.

You will learn how to:  
* Secure a domain with Hostinger’s affordable plans and set up DNS records for email and web services.  
* Create a Gmail or Outlook business account and configure SPF, DKIM, and DMARC to improve deliverability.  
* Set up Apollo.io with your API key, build a workspace, and import your first lead list.  
* Build a Notion workspace, create a lead‑management template, and connect it to Apollo.io via Zapier.  
* Install and configure complementary tools (Zapier, [Canva](https://www.canva.com/), Grammarly) that keep the funnel moving automatically.

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| Apollo.io | Lead data extraction & enrichment | 30 contacts/day | $39/month (Starter) |
| Notion | Project/DB management | Unlimited pages, 5MB file upload | $8/month (Team) |
| Hostinger | Domain & web hosting | 100GB bandwidth, 1GB storage | $3.95/month (Premium) |
| Zapier | Automation between Apollo & Notion | 100 tasks/month | $19.99/month (Starter) |
| Gmail (Google Workspace) | Professional email | 15GB free | $6/month (Business Starter) |

**Estimated time to complete:** 2 hours. This includes account creation, DNS propagation, and initial data import.

---

## Procedure 1.1: Set Up Apollo.io Account for Lead Management

1. **Open your preferred web browser** and navigate to the Apollo.io signup URL:  
   `https://app.apollo.io/auth/signup`

2. On the landing page, locate the **Sign Up with Email** button and click it.  
   *Expected UI*: A modal popup titled “Create Your Apollo Account”.

3. In the modal, fill out the following fields exactly as shown:  
   - **First Name**: “Alex”  
   - **Last Name**: “Smith”  
   - **Company Name**: “Alex Consulting”  
   - **Email**: “alex.smith@example.com”  
   - **Password**: “StrongPass!2024” (must be ≥ 8 characters, include a number, uppercase, and special character)

4. Click the **Create Account** button.  
   *Outcome*: Apollo sends a verification email to “alex.smith@example.com”.

5. **Do you see the verification email in your inbox?**  
   - If yes, open it.  
   - If no, check the **Spam** folder.  
   - If still not found, click **Resend Email** in the Apollo modal and repeat step 4.

6. In the email, click the **Verify Email** link.  
   *Expected Result*: Browser redirects to `https://app.apollo.io/auth/verified` and displays “Account Verified” banner.

7. Back in Apollo, you’re now logged in. Click the **Get Started** button on the home screen.  
   *Expected UI*: Dashboard with tabs “Leads”, “Prospects”, “Accounts”.

8. Navigate to the **Settings** icon (gear) in the top-right corner and click it.  
   *Expected Result*: Settings sidebar slides in from the right.

9. In the Settings sidebar, click **API & Webhooks**.  
   *Expected Output*: API Key is auto-generated with a “Copy” button.

10. **Do you see the API Key displayed?**  
    - If yes, click **Copy** and paste it into a secure note in [**Notion**](https://notion.so/) under a new page titled “Apollo API Key”.  
    - If no, click **Generate New Key**.  
    - If a **500 Internal Server Error** appears, this means Apollo’s servers are currently overloaded. Wait 5 minutes and retry.

11. Return to the main dashboard and click the **Integrations** tab.  
    *Expected UI*: List of available integrations including **Zapier**, [**Make.com**](https://www.make.com/en/register?pc=menshly), and **Notion**.

12. Click the **Zapier** integration card and then the **Connect** button.  
    *Expected Result*: Redirects to `https://zapier.com/app/connected-accounts`.

13. On Zapier, click **Make a Zap**.  
    *Outcome*: Opens Zapier’s editor with “Choose a Trigger App”.

14. In the search bar, type “Apollo” and select the Apollo app.  
    - Choose the trigger event **New Lead**.  
    - Click **Continue**.

15. **Do you see the “Choose Account” dropdown populated with your Apollo account?**  
    - If yes, select it and click **Continue**.  
    - If the dropdown is empty, click **Add a New Account** and log in again using your Apollo credentials.

16. Zapier will prompt you to **Test Trigger**. Click **Test Trigger** and wait for a sample lead to load.  
    *Expected Result*: A sample lead JSON appears in Zapier’s editor.

17. Click **Continue** and set up the action step. Search for “Notion” and select it.  
    - Choose the action event **Create Database Item**.  
    - Click **Continue**.

18

---

## Procedure 1.2: Configure Notion Workspace for Lead Tracking

1. **Open your browser and navigate to https://www.notion.so**.  
   - Click **SIGN IN** in the upper‑right corner.  
   - Enter your email and password, then hit **SIGN IN**.  
   - **Do you see your Notion dashboard?** If not, ensure your credentials are correct; if you receive “Invalid credentials” this means you typed the wrong password. Reset via the “Forgot password?” link.

2. **Create a new workspace** (if you don’t already have one).  
   - Click **+ NEW WORKSPACE** on the left sidebar.  
   - Enter **“AI Lead Gen”** as the workspace name.  
   - Click **CREATE**.  
   - **Do you see “AI Lead Gen” listed in your workspace list?** If not, refresh the page or double‑check the name you typed.

3. **Add a new page for lead tracking**.  
   - Inside the “AI Lead Gen” workspace, click the **+ NEW PAGE** button.  
   - Choose **“Table – Full page”** from the template picker.  
   - Title the page **“Leads Database”** and press **CREATE**.  
   - **Do you see a blank table titled “Leads Database”?** If not, ensure you selected the correct template.

4. **Configure table columns**.  
   - Click the first column header (**“Name”**) and rename to **“Lead Name”**.  
   - Click the second column header (**“Company”**) and rename to **“Company”**.  
   - Click the third column header (**“Email”**) and rename to **“Email”**.  
   - Click the fourth column header (**“Phone”**) and rename to **“Phone”**.  
   - Click the fifth column header (**“Source”**) and rename to **“Source”**.  
   - **Do you see five columns with the proper names?** If a column name is missing, double‑click the header to rename again.

5. **Add a “Status” column**.  
   - Click the plus sign (**+**) to the right of the last column.  
   - Select **“Select”** from the property type list.  
   - Name the property **“Status”**.  
   - Add options: **“New”**, **“Contacted”**, **“Qualified”**, **“Won”**, **“Lost”**.  
   - **Do you see the “Status” column with all options?** If options don’t save, ensure you’re in “Edit” mode for the property.

6. **Add a “Created At” column**.  
   - Add another column (**+**) and choose **“Created time”**.  
   - Name it **“Created At”**.  
   - **Do you see the “Created At” column?** If it’s blank, refresh the page.

7. **Set default status for new entries**.  
   - Hover over the **“Status”** column, click the three dots (**⋮**) and select **“Default value”**.  
   - Choose **“New”**.  
   - **Do you see the default set to “New”?** If not, re‑open the default value dialog.

8. **Create a template button for quick lead entry**.  
   - Click **+** in the left sidebar and select **“Template button”**.  
   - Name it **“Add Lead”**.  
   - In the **Template** area, click **+** and choose **“Table – Inline”**.  
   - Under **Properties**, set **Lead Name**, **Company**, **Email**, **Phone**, **Source** to empty fields.  
   - Set **Status** default to **“New”**.  
   - Click **Save**.  
   - **Do you see the “Add Lead” button?** If not, ensure you’re in the correct workspace.

9. **Share the database with your Apollo.io integration user**.  
   - Click **Share** in the top right of the Leads Database page.  
   - Enter the email address **apollo-integration@yourdomain.com** and hit **Invite**.  
   - Set permission to **“Can edit”**.  
   - **Do you see the user listed as “Can edit”?** If the invitation fails, verify the email.

10. **Create an Apollo.io API key**.  
    - Log in to https://app.apollo.io.  
    - Go to **Settings → Integrations → API**.  
    - Click **Generate API Key**, copy the key.  
    - **Do you see the API key displayed?** If it says “Access denied”, ensure you have admin rights in Apollo.

11. **Set up Make.com (formerly Integromat) to sync Apollo leads**.  
    - Open https://www.make.com.  
    - Click **SIGN UP** (free tier: 1,000 operations/month).  
    - After login, click **Create new scenario**.  
    - Search for **Apollo.io** and click **Add**.  
    - Choose the trigger **“Watch New Leads”**.  
    - Paste your API key in the **API Key** field and click **Test**.  
    - **Do you see “Connection successful”?** If it shows **“Error: 401 Unauthorized”**, double‑check the key.

12. **Add the Notion module to the scenario**.  
    - Click the plus sign next to the Apollo module and search for **Notion**.  
    - Select **“Create a Database Item”**.  
    - Click **Add an account**.  
    - In the pop‑up, click **Add** next to **Notion**.  
    - Authorize with your Notion account, then choose the **“Leads Database”** page as the target database.  
    - Map fields:  
      - **Lead Name** → `name`  
      - **Company** → `properties.Company.title[0].text

---

**Procedure 1.3** — Generation failed due to AI backend unavailability. Please retry later.

## Check-In: Module 1 Complete

- [ ] Set Up Apollo.io Account for Lead Management completed and verified
- [ ] Configure Notion Workspace for Lead Tracking completed and verified
- [ ] Integrate Email Verification Service with Apollo.io completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 2: TECH STACK

## Overview
In MODULE 2 you will assemble the core technology backbone that powers your AI‑driven lead generation empire. The goal is to cement reliable data pipelines between Apollo.io, Notion, Make.com (formerly Integromat), Zapier, and complementary AI services such as ChatGPT and ElevenLabs. If you skip this module, your system will suffer from data silos, stale leads, and manual bottlenecks that erode the ROI of every cold outreach attempt. Every click, API key, and mapping must be verified—otherwise your funnel will drop leads before they even reach your sales team.

You will complete step‑by‑step integration of each tool, set up authentication, define data schemas, and run test flows. By the end you will have a fully automated, end‑to‑end pipeline that pulls prospects from Apollo.io, enriches them with AI, stores them in Notion, and triggers follow‑up sequences via Zapier or Make.com. This module also teaches you how to monitor, audit, and troubleshoot data exchanges to keep the pipeline humming with minimal oversight.

The following table lists all mandatory tools, their primary purpose, and pricing details for both free and paid tiers. Use this as your quick reference when configuring each connection.

| Tool          | Purpose                                                                 | Free Tier                                 | Paid Tier (Starter)                             |
|---------------|--------------------------------------------------------------------------|-------------------------------------------|-------------------------------------------------|
| Apollo.io     | Prospect search, contact enrichment, email outreach                      | 30 credits/month (30 emails/day)          | $99/month (unlimited credits, 2000 emails/day) |
| Notion        | Central lead database, task tracking, documentation                      | Unlimited pages, 1,000 blocks/month       | $8/user/month (pro workspace, unlimited blocks)|
| Make.com      | Automation of API calls, data transformation                              | 100 operations/month, 1 scenario          | $49/month (1,500 operations/month)             |
| Zapier        | Trigger‑action workflows, third‑party integrations                       | 5 Zaps, 100 tasks/month                  | $19.99/month (20 Zaps, 2,000 tasks/month)      |
| ChatGPT / GPT‑4| AI lead qualification, email drafting, content generation                 | Unlimited requests (free tier)            | $20/month (ChatGPT Plus)                        |
| ElevenLabs    | Text‑to‑speech for outreach, voicemail automations                      | 5,000 characters/month                   | $10/month (20,000 characters/month)            |

**Estimated Time to Complete**: 1 hour 30 minutes (incl. API key retrieval, UI navigation, and test flow verification).

---

## Procedure 2.1: Configure Apollo.io API Keys and Integrations

1. **Open your web browser** and navigate to the Apollo.io login page:  
   `https://app.apollo.io/login`  
   *Enter your corporate email and password, then click the button labeled **“Sign In”**.  
   **Expected output:** You should reach the Apollo dashboard with the sidebar visible.*

2. **Click the profile icon** in the top‑right corner, then select **“Settings”** from the dropdown.  
   *The Settings page will load, showing multiple tabs on the left.*

3. In the left‑hand menu, click **“API & Integrations.”**  
   *The API & Integrations pane will appear on the right.*

4. **Locate the “Apollo API Key” section**. Click the button labeled **“Generate Key.”**  
   *A modal dialog appears with a newly generated key.  
   **Do you see the generated key? If not, refresh the page and try again.**  
   **Expected output:** A 32‑character alphanumeric key displayed in a read‑only field.*

5. **Click the green button** labeled **“Copy to clipboard.”**  
   *A toast notification appears: “Key copied to clipboard.”  
   **Interactive check‑in:** Do you see the toast? If not, ensure your browser allows clipboard access.*

6. **Open a new tab** and navigate to `https://www.notion.so/my-integrations`.  
   *If prompted, sign in with the same credentials used for Apollo.*

7. In Notion, click the button labeled **“+ New integration.”**  
   *The Integration Creation page opens.*

8. Fill in the **“Name” field** with `Apollo Lead Sync`.  
   *Enter any optional description if desired.*

9. Under **“Capabilities,”** toggle the switch next to **“Read content”** and **“Insert content.”**  
   *The toggles should turn blue.*

10. **Click the button** labeled **“Submit.”**  
    *A modal appears confirming the integration creation.*

11. In the modal, click **“Copy Integration Token.”**  
    *A toast appears: “Token copied.”  
    **Expected output:** The integration token is now in your clipboard.*

12. **Open a terminal** in Replit at `https://replit.com/~` and create a new Repl named `apollo‑notion‑sync` using the `Python` template.  
    *Replit will prompt you to sign in; use your free tier credentials.*

13. In the `main.py` file, paste the following snippet, replacing `YOUR_AUPO_API_KEY` and `YOUR_NOTION_TOKEN` with the values you just copied:  
    ```python
    import requests
    import json
    
    APOLLO_KEY = "YOUR_AUPO_API_KEY"
    NOTION_TOKEN = "YOUR_NOTION_TOKEN"
    HEADERS_AUPO = {"Authorization": f"Bearer {APOLLO_KEY}"}
    HEADERS_NOTION = {"Authorization": f"Bearer {NOTION_TOKEN}",
                      "Notion-Version": "2022-06-28",
                      "Content-Type": "application/json"}
    ```
    *If you see a `SyntaxError: EOL while scanning string literal`, it means you missed a closing quote. Fix it by adding the missing quote.*

14. **Create a new Notion database** where leads will be stored:  
    - In Notion, click **“Add a page.”**  
    - Choose **“Table – Full page.”**  
    - Title it `Apollo Leads`.  
    - Add columns: `Name` (Title), `Email` (Email), `Company` (Text), `Lead Score` (Number), `Source` (Select, options: Apollo).

15. **Return to Replit** and add the following function

---

## Procedure 2.2: Set Up Notion Database for Lead Tracking

1. **Open Notion**  
   - URL: https://www.notion.so/  
   - Log in with your credentials.  
   - Expected result: You see your workspace’s sidebar and a blank page preview.

2. **Create a new page**  
   - Click the **"+ New Page"** button on the sidebar.  
   - In the title field, type **"Lead Tracker"** and press **Enter**.  
   - Expected result: A fresh page titled *Lead Tracker* opens.

3. **Add a database**  
   - On the new page, click the **"Add a database"** button.  
   - Select **"Table - Full Page"** from the dropdown.  
   - Expected result: A table view appears with columns “Name,” “Created time,” etc.

4. **Rename the database**  
   - Hover over the default database title at the top of the table.  
   - Click **"Database Title"** → type **"Leads"** → press **Enter**.  
   - Expected result: Table header now reads *Leads*.

5. **Delete unnecessary columns**  
   - Hover over the “Tags” column header → click the **three‑dot menu** → choose **"Delete property"**.  
   - Repeat for any columns you don’t need (e.g., “Files”).  
   - Expected result: Only “Name” and “Created time” columns remain.

6. **Add required properties**  
   - Click the **"+ Add a property"** button on the right.  
   - **Property 1**:  
     - Name: **"Lead Source"**  
     - Type: **"Select"**  
     - Click **"Add option"** → type **"Apollo.io"** → press **Enter**.  
   - **Property 2**:  
     - Name: **"Status"**  
     - Type: **"Select"**  
     - Add options: **"New," "Contacted," "Qualified," "Converted"**.  
   - **Property 3**:  
     - Name: **"Email"**  
     - Type: **"Email"**  
   - **Property 4**:  
     - Name: **"Phone"**  
     - Type: **"Phone"**  
   - Expected result: Four new columns appear with the specified types.

7. **Create a “Relation” to Apollo.io contacts**  
   - Click **"+ Add a property"** → choose **"Relation"**.  
   - In the popup, search for the page where you store Apollo.io data (create one if it doesn’t exist yet).  
   - Select that page → click **"Create relation"**.  
   - Name the relation **"Apollo Contact"**.  
   - Expected result: A relation column appears, linking to Apollo.io contacts.

8. **Add a “Rollup” for lead score**  
   - Click **"+ Add a property"** → choose **"Rollup"**.  
   - Relation: **"Apollo Contact"**  
   - Property: **"Lead Score"** (must exist in the referenced Apollo page)  
   - Calculation: **"Average"**  
   - Name: **"Avg Lead Score"**  
   - Expected result: New rollup column shows average scores when linked.

9. **Create a “Board” view for status tracking**  
   - Click the **"Add a view"** button → name it **"Lead Status Board"** → choose **"Board"** → click **"Create"**.  
   - In the view settings, select **"Status"** as the property to group by.  
   - Expected result: Kanban board with columns for each status.

10. **Set up filtering for Apollo.io leads**  
    - In the *Leads* table view, click the **"Filter"** button → **"Add a filter"**.  
    - Condition: **Lead Source** **equals** **"Apollo.io"**.  
    - Expected result: Only rows tagged with Apollo.io appear.

11. **Create a “Template” for new leads**  
    - In the table view, click the **"⋮"** button next to **"New"** → choose **"Create a template"**.  
    - Name the template **"Apollo New Lead"**.  
    - In the template editor:  
      - Set **Lead Source** to **"Apollo.io"**.  
      - Add a placeholder in the **Notes** property: *“Lead created via Apollo integration.”*  
    - Click **"Close"**.  
    - Expected result: A reusable template appears under the New button.

12. **Add a “Formula” for email domain**  
    - Click **"+ Add a property"** → choose **"Formula"**.  
    - Name: **"Domain"**  
    - Formula: `format(formatDate(prop("Email"), "YYYY-MM-DD"))` *[Use the actual Notion formula to parse domain]*  
    - Click **"Close"**.  
    - Expected result: Domain column auto‑populates when an email is entered.

13. **Create a “Page” for Apollo.io API credentials**  
    - In the sidebar, click **"+ New Page"** → title **"Apollo API"**.  
    - Add a **“Text”** block → paste your Apollo.io API key: `***YOUR_APO_API_KEY***`.  
    - Click the lock icon to **“Share”** → toggle **"Share to the web"

---

## Procedure 2.3: Create Zapier Workflow to Sync Apollo and Notion

1. **Open Zapier**  
   - Go to **https://zapier.com**.  
   - Click **Sign In** (top‑right) and log in with your credentials.  
   *Do you see the Zapier dashboard with the “Create Zap” button? If not, refresh the page or clear your cache.*

2. **Create a New Zap**  
   - Click **Create Zap** (bold).  
   - In the “Choose a Trigger App” search bar, type **Apollo.io** and click **Apollo.io**.  
   - Select the trigger event **“New Lead”**.  
   - Click **Continue** (bold).  
   *Do you see the “New Lead” trigger screen? If the “Apollo.io” app does not appear, click “Explore More Apps” and search again.*

3. **Connect Apollo.io Account**  
   - Click **Sign in to Apollo.io** (bold).  
   - In the popup, enter your Apollo.io **API Key** (found in Apollo → Settings → API).  
   - Click **Continue** (bold).  
   - Zapier will test the connection; you should see “✅ Successful authentication.”  
   *Do you see the authentication success message? If you see “❌ Authentication failed”, double‑check the API key length and copy it again.*

4. **Set Up Trigger Options**  
   - In the “Set up trigger” screen, leave **Lead Type** as **Any**.  
   - Click **Test trigger** (bold).  
   - Zapier will pull a sample lead; you should see a JSON preview like:  
     ```
     {
       "id": "12345",
       "first_name": "Jane",
       "last_name": "Doe",
       "email": "jane@example.com",
       "company": "Acme Corp"
     }
     ```  
   *Do you see the sample lead data? If the test returns “No data found”, create a new lead in Apollo.io first.*

5. **Add an Action: Notion**  
   - Click **+** (Add a new action).  
   - Search for **Notion** and click **Notion**.  
   - Choose the action event **“Create Database Item”**.  
   - Click **Continue** (bold).  
   *Do you see the “Create Database Item” screen? If Notion does not appear, ensure you have the latest Zapier integration installed.*

6. **Connect Notion Account**  
   - Click **Sign in to Notion** (bold).  
   - In the popup, click **Connect**.  
   - Grant Zapier access to your Notion workspace.  
   - Click **Continue** (bold).  
   *Do you see the “Connected” status? If you see “❌ Connection failed”, check that you are logged into the correct Notion account.*

7. **Select Notion Database**  
   - In the “Set up action” section, click the dropdown next to **Database**.  
   - Choose the database named **“Apollo Leads”** (create it in Notion if it doesn’t exist).  
   - Click **Continue** (bold).  
   *Do you see your “Apollo Leads” database listed? If not, create it in Notion first.*

8. **Map Apollo Fields to Notion Properties**  
   - For each Notion property, click the field and select the corresponding Apollo data:  

     | Notion Property | Apollo Field |
     |-----------------|--------------|
     | First Name      | `first_name` |
     | Last Name       | `last_name`  |
     | Email           | `email`      |
     | Company         | `company`    |
     | Lead ID         | `id`         |

   - Click **Continue** (bold).  
   *Do you see each field mapped correctly? If a field shows “(Unmapped)”, re‑select the correct Apollo data.*

9. **Test the Notion Action**  
   - Click **Test & Review** (bold).  
   - Zapier will create a new database item in Notion.  
   - Open your Notion workspace and navigate to **Apollo Leads**.  
   - You should see a new page titled with the Lead ID, containing the mapped properties.  
   *Do you see the new lead entry in Notion? If the entry is missing, check the “Test & Review” log for errors.*

10. **Name and Turn On the Zap**  
    - Click **Name your Zap** (top-left) and type **Apollo‑Notion Sync**.  
    - Toggle the switch at the top-right to **On** (green).  
    - Confirm by clicking **Turn on Zap** (bold).  
    *Do you see the green “ON” indicator? If not, double‑click the toggle.*

11. **Verify Real‑Time Sync**  
    - In Apollo.io, create a new lead with unique data.  
    - Wait 30 seconds.  
    - In Notion, the **Apollo Leads** database should now contain a

## Check-In: Module 2 Complete

- [ ] Configure Apollo.io API Keys and Integrations completed and verified
- [ ] Set Up Notion Database for Lead Tracking completed and verified
- [ ] Create Zapier Workflow to Sync Apollo and Notion completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 3: FRAMEWORK

## Overview

In this module we lay the foundation that turns a raw idea into a repeatable, scalable AI‑powered lead generation business. You will learn how to map the entire client journey—from the moment a prospect lands on your website to the final handover of a verified contact list—into a solid, auditable framework. By defining service delivery standards, onboarding protocols, and quality gates, you’ll eliminate the guesswork that plagues most solo operators and create a system that can be replicated at any scale.

Skipping this module means you’ll be constantly tweaking ad hoc processes, losing time on manual data cleanup, and delivering inconsistent results. The lack of a clear framework also makes it impossible to onboard new team members or automate tasks with Zapier, Make.com, or Apollo.io, leaving you trapped in a cycle of firefighting rather than growth. Mastering this framework ensures every lead you generate is accurate, your clients see measurable ROI, and you can scale without compromising quality.

| Tool        | Purpose                                                     | Free Tier                                 | Paid Tier                                  |
|-------------|-------------------------------------------------------------|-------------------------------------------|--------------------------------------------|
| Apollo.io   | Prospect sourcing, email outreach, data enrichment          | 5,000 credits/month (search + outreach)   | Pro: $99/month (unlimited credits)         |
| Notion      | Project management, SOPs, knowledge base                    | Unlimited pages, 5 editors                | Plus: $8/seat/month (advanced permissions) |
| Make.com    | Automate workflows between Apollo, Notion, email, etc.      | 5,000 operations/month                    | Standard: $49/month (unlimited ops)       |
| Zapier      | Connect Apollo, Notion, CRM, email, analytics               | 5 Zaps, 100 tasks/month                   | Starter: $19.99/month (unlimited Zaps)    |
| Canva       | Create lead‑gen assets (emails, landing pages, social posts)| Unlimited free templates, 5 GB storage    | Pro: $12.99/month (advanced features)     |
| ChatGPT     | Generate copy, scripts, and data enrichment ideas           | 3,000 tokens/day                          | Plus: $20/month (advanced models)         |

**Estimated Time to Complete:** 3–4 hours (including tool setup, SOP drafting, and workflow testing).

---

## Procedure 3.1: Create a Service Delivery Framework in Apollo.io

1. **Open Apollo.io**  
   - URL: https://app.apollo.io/  
   - Log in with your credentials.  
   - Expected UI: Dashboard with a sidebar containing **"Contacts"**, **"Lists"**, **"Tasks"**, **"Reports"**.  

2. **Create a New Lead List**  
   - Click **"Lists"** in the sidebar.  
   - Press the **"New List"** button (top‑right, blue).  
   - Name the list **“Client‑Ready Leads”** and select **“Public”** for visibility.  
   - Click **"Create List"**.  

3. **Set List Filters**  
   - In the list view, click **"Add Filter"**.  
   - Choose **“Industry” → “Technology”**.  
   - Add another filter: **“Company Size” → “51‑200 employees”**.  
   - Add a third filter: **“Location” → “United States”**.  
   - Click **"Apply Filters"**.  

4. **Save Filtered Results as a Static List**  
   - Once the results load, click **"Export"** (top‑right, gray).  
   - Select **"CSV"** and **"Export All"**.  
   - Download the file to your computer.  
   - **Do you see the CSV file download?**  
     - If not, refresh the page and re‑apply filters.  

5. **Upload CSV to Notion**  
   - Open Notion (URL: https://www.notion.so/) and navigate to the workspace **“AI Lead Gen Ops”**.  
   - Create a new page titled **“Lead Intake Sheet”**.  
   - Click **“+ Add a block”** → **“Table – Inline”**.  
   - In the table, click **"Empty Table"** → **"Import"** → **"CSV"**.  
   - Upload the CSV file from step 4.  
   - Verify that all columns (Name, Title, Email, Phone, Company, Industry, Location) appear correctly.  
   - **Do you see all columns populated?**  
     - If columns are missing, re‑import the CSV ensuring “Header row” is checked.  

6. **Create a Notion Template for Lead Entries**  
   - In the **“Lead Intake Sheet”**, click **"New"** → **"Template"**.  
   - Name the template **“Lead Detail”**.  
   - Add properties:  
     - **Name** (Title)  
     - **Email** (Email)  
     - **Phone** (Phone)  
     - **Company** (Text)  
     - **Industry** (Select)  
     - **Stage** (Select: “New”, “Contacted”, “Qualified”, “Proposal Sent”, “Closed”)  
     - **Notes** (Text)  
   - Save the template.  

7. **Link Apollo.io to Notion via Zapier**  
   - Open Zapier (URL: https://zapier.com/).  
   - Click **"Make a Zap"**.  
   - **Trigger App**: Apollo.io → **Trigger Event**: “New Contact”.  
   - Connect your Apollo.io account by clicking **"Sign in to Apollo.io"** and authorizing.  
   - **Do you see the “New Contact” trigger?**  
     - If not, check that your Apollo.io account has API access (enabled in Settings → API).  

8. **Configure Zap Trigger**  
   - In the **Trigger** step, choose the list **“Client‑Ready Leads”**.  
   - Test trigger: click **"Test Trigger"**.  
   - Zapier should pull one contact record.  
   - Confirm the record shows **Name**, **Email**, **Company** fields.  

9. **Set Up Zap Action to Create Notion Page**  
   - **Action App**: Notion → **Action Event**: “Create Page”.  
   - Connect your Notion account (click **"Sign in to Notion"**).  
   - In the **Page Properties**, map Apollo.io fields to Notion properties:  
     - **Title** → “Name”  
     - **Email** → “Email”  
     - **Phone** → “Phone”  
     - **Company** → “Company”  
     - **Industry** → “Industry”  
     - **Stage** → “Stage” (default to “New”)  
   - Set the **Parent Page** to **“Lead Intake Sheet”**.  
   - Click **"Continue"** and **"Test & Review"**.  
   - Verify a new page appears in Notion with the mapped data.  

10. **Enable Zap**  
    - Turn the Zap “On”.  
    - **Do you see the Zap status as “ON”?**  
      - If not, click the toggle in the top right of the Zap editor.  

11. **Create Apollo.io Task Workflow**  
    - In Apollo.io, go to **"Tasks"**.  
    - Click **"New Task"** → **"Create Task"**.  
    - Set **Task Type** to **“Follow‑Up Email”**.  
    - Assign to **"You"

---

## Procedure 3.2: BUILD a Client Onboarding Flow Map in Notion

1. **Open Notion**  
   - URL: https://www.notion.so/  
   - Log in with your workspace credentials.  
   - If you do not have an account, click **Create new account** → email → **Continue** → verify email → **Create a new workspace** → name it “AI Lead Gen Onboarding”.  

2. **Create the Onboarding Page**  
   - In the left sidebar, click **+ Add a page**.  
   - Title the page **Client Onboarding Flow Map**.  
   - Under “Page type”, select **Table** (the default).  

3. **Add Table Columns**  
   - Click the first column header → rename to **Step** (type `Step`).  
   - Click **+ Add a property** → choose **Number** → name it **Order**.  
   - Click **+ Add a property** → choose **Select** → name it **Status**.  
   - Click **+ Add a property** → choose **Text** → name it **Notes**.  

4. **Populate the Table with Core Steps**  
   - In row 1, fill:  
     - Step: “Initial Contact”  
     - Order: `1`  
     - Status: **TODO** (select “TODO” from dropdown)  
     - Notes: “Send introductory email via Apollo.io”.  
   - Repeat rows for:  
     - “Discovery Call” (Order 2)  
     - “Proposal Draft” (Order 3)  
     - “Contract Signing” (Order 4)  
     - “Kick‑off Meeting” (Order 5).  

5. **Link Apollo.io Email Templates**  
   - Open Apollo.io: https://app.apollo.io.  
   - Click **Templates** → **Create Template**.  
   - Name it **Onboarding Intro Email**.  
   - Copy the template ID from the URL (e.g., `https://app.apollo.io/templates/123456`).  
   - Return to Notion, edit the **Notes** field for “Initial Contact” and paste:  
     `Apollo Template ID: 123456`.  

Do you see the “Client Onboarding Flow Map” page with the table and the five rows? If not, refresh Notion, ensure you are on the correct workspace, and verify the page title.

6. **Embed Apollo.io Dashboard**  
   - In Apollo.io, click **Dashboard** → **Share** → **Create Public Link**.  
   - Copy the link (e.g., `https://app.apollo.io/dashboard/abcde`).  
   - Back in Notion, type “/embed” → select **Embed** → paste the link → hit **Enter**.  
   - Resize the embed to full width.  

7. **Add a Calendar View**  
   - In the table view, click **+ Add a view** → select **Calendar** → name it **Onboarding Calendar** → **Create**.  
   - In the new view, change the property to display **Order** as the date field (use a custom date formula: `dateAdd(now(), prop("Order")-1, "days")`).  

8. **Create a Zapier Workflow for Status Sync**  
   - Open Zapier: https://zapier.com.  
   - Click **Make a Zap** → trigger **Notion** → event **New Database Item** → connect your Notion account.  
   - Choose the **Client Onboarding Flow Map** database.  
   - Test trigger → data appears.  
   - Action: **Apollo.io** → event **Send Email** → map **Step** to email subject, **Notes** to email body.  
   - Turn on the Zap.  

9. **Add a Status Tracker Dashboard**  
   - In Notion, click **+ Add a page** → title **Onboarding Dashboard**.  
   - Type “/linked database” → choose **Client Onboarding Flow Map** → select **Table** view.  
   - Hide the **Order** column (click column header → **Hide**).  
   - Add a filter: **Status** is **DONE** → this view shows completed steps.  

10. **Embed a Loom Recording of the Kick‑off Meeting**  
    - Record the meeting in Loom: https://www.loom.com.  
    - After recording, click **Share** → **Copy Link**.  
    - In Notion, go to the **Kick‑off Meeting** row → edit **Notes** → add “Loom URL: https://www.loom.com/share/xyz”.  
    - Optionally, embed the video: type “/embed” → paste Loom link.  

11. **Add a Toggle for Client Feedback**  
    - In the **Notes** column for “Kick‑off Meeting”, type “/toggle” → title **Client Feedback**.  
    - Inside the toggle, add a text block: “Please rate the kickoff on a scale of 1‑5.”  

12. **Set Up a Notion Reminder for Follow‑ups**  
    - Click the date icon on the **Order** column for “Contract Signing”.  
    - Set date to “Contract Signing Date + 7 days”.  
    - In the reminder field, type “Contract Signed? Follow‑up call”.  

13. **Create a Client Onboarding Template in Notion**  
    - In the sidebar, click **+ New** → **Template** → name **Client Onboarding**.  
    - Add the table and all the columns above.  
    - Save.  



## Check-In: Module 3 Complete

- [ ] Create a Service Delivery Framework in Apollo.io completed and verified
- [ ] BUILD a Client Onboarding Flow Map in Notion completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 4: FIRST BUILD

## Overview  
In this module you will *build your very first AI‑powered lead‑generation deliverable* from scratch and deploy it to a real client. We’ll use **Apollo.io** to harvest and qualify leads, and **Notion** as a living data hub and reporting dashboard. By the end of the session you’ll have a repeatable workflow that pulls fresh prospects, enriches them with AI‑generated insights, and presents them in a crystal‑clear Notion table ready for outreach.  

Skipping this module means you’ll be stuck in a cycle of ad‑hoc spreadsheets, manual data entry, and endless copy‑pasting. Your clients will see inconsistent results, and you’ll lose the competitive edge that automated data pipelines deliver. Without the first build you cannot prove the value of your service, so you’ll struggle to upsell, scale, or even secure your next client.  

**Tools you’ll need** (free and paid tiers are listed to help you budget):

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| Apollo.io | Lead discovery & enrichment | 1,000 credits/month, 5 lead syncs | $99/month (Pro) |
| Notion | Data hub, reporting, client portal | Unlimited pages, 5 MB file upload | $8/user/month (Personal Pro) |
| Make.com | Automate Apollo → Notion workflow | 500 operations/month | $49/month (Starter) |
| Zapier | Alternative automation trigger | 100 tasks/month | $19.99/month (Starter) |
| ChatGPT | AI content & data enrichment | GPT‑3.5 free | $20/month (ChatGPT Plus) |
| Replit | Quick code snippets for custom scripts | 500 MB storage, 1 GB RAM | $7/month (Hacker) |
| [Vapi](https://vapi.ai/) | Voice‑to‑text for lead notes | 100 voice calls | $0.02/min (paid) |
| ElevenLabs | Audio summaries of lead data | 5 hrs/month | $10/month (Starter) |
| Canva | Lead‑pack visual design | Limited templates | $12.99/month (Pro) |
| Midjourney | AI image generation for lead assets | 25 images/month | $10/month (Basic) |
| Grammarly | Copy‑editing for outreach | Basic | $12/month (Premium) |

**Estimated time to complete**: 2 hours 30 minutes (including data import, automation setup, and first deliverable review).



---

**Support Pollinations.AI:**

---

🌸 **Ad** 🌸
Powered by Pollinations.AI free text APIs. [Support our mission](https://pollinations.ai/redirect/kofi) to keep AI accessible for everyone.

---

## Procedure 4.1: INTEGRATE Apollo.io Lead Data into a Notion Database

1. **Open Apollo.io**  
   - URL: `https://app.apollo.io/login`  
   - Enter your email and password, then click **LOG IN**.  
   - *Expected*: Apollo dashboard with “Leads”, “Companies”, “Tasks” tabs.  

2. **Export your leads**  
   - Click the **LEADS** tab.  
   - In the top right, click **BULK ACTIONS** → **EXPORT**.  
   - Choose **CSV** and click **EXPORT** again.  
   - Apollo will send a download link to your registered email within 30 seconds.  

3. **Download the CSV**  
   - Open the email, click the download link, and save the file to `C:\Users\<your‑name>\Downloads\apollo_leads.csv`.  

4. **Verify the CSV file**  
   - Open the file in Notepad.  
   - *Do you see a header row with fields like `FirstName,LastName,Email,Company,Phone`?*  
   - If not, re‑export from Apollo or check the email attachment.  

5. **Open Notion**  
   - URL: `https://www.notion.so/login`  
   - Log in with your workspace email, click **LOG IN**.  

6. **Create a new database**  
   - On the left sidebar, click **+ ADD A PAGE**.  
   - Choose **DATABASE** → **TABLE – FULL PAGE**.  
   - Name the page **Apollo Leads**.  

7. **Add database columns**  
   - Click the first column header (**Name**) and rename to **Name** (type: Title).  
   - Click **+ Add a property** → **Email** (type: Email).  
   - Add **Company** (type: Text).  
   - Add **Phone** (type: Phone).  
   - Add **Lead Source** (type: Select; add options: Apollo, LinkedIn, Referral).  
   - Add **Status** (type: Select; add options: New, Contacted, Qualified, Lost).  

8. **Do you see the new database table with the above columns?**  
   - If not, refresh the page or repeat step 7.  

9. **Create a Notion integration**  
   - Click your avatar → **Settings & Members** → **Integrations** → **+ New integration**.  
   - Name it **Apollo‑Notion Sync**, set the role to **Full Access**, and click **Create integration**.  
   - Copy the **Internal Integration Token** (e.g., `secret_XXXXXXXXXXXXXXXXXXXX`).  

10. **Share the database with the integration**  
    - Open the **Apollo Leads** database.  
    - Click **Share** → **Invite** → paste the integration name **Apollo‑Notion Sync** → **Invite**.  

11. **Open Zapier**  
    - URL: `https://

---

## Procedure 4.2: Automate Email Outreach Campaigns Using Apollo.io and Notion

1. **Open Apollo.io**  
   - Navigate to `https://app.apollo.io/`.  
   - Click **Sign in** at the top‑right corner.  
   - Enter your email and password, then click **Log In**.  
   - *Do you see the Apollo dashboard? If not, clear your browser cache and try again.*

2. **Create a New Campaign**  
   - In the left sidebar, click **Campaigns**.  
   - Click the **+ New Campaign** button in the upper‑right corner.  
   - In the “Create Campaign” modal, type **“Lead Gen Q3”** into the **Campaign name** field.  
   - Select **Email** from the **Campaign type** dropdown.  
   - Click **Create**.  
   - *Expected output:* A new campaign page with a blank “Email Sequence” section.

3. **Add Email Sequence**  
   - Click **+ Add Email**.  
   - In the email editor, set **Subject** to “Grow Your SaaS with AI‑Powered Leads”.  
   - In the body, paste the following text:  
     > Hi {{firstName}},  
     >  
     > I help SaaS founders like you scale quickly with AI‑generated leads.  
     >   
     > Let’s set a 15‑min call to discuss!  
     >   
     > – Alex  
   - Click **Send Test** at the bottom, then **Close**.  
   - *Do you see the email preview? If not, ensure the editor has loaded fully.*

4. **Enable Apollo’s Email Scheduler**  
   - In the campaign header, click **Schedule**.  
   - Toggle **Send emails automatically** to **ON**.  
   - Set **Start date** to the next Monday (e.g., `2026‑07‑04`).  
   - Set **Send frequency** to **1 per day**.  
   - Click **Save Schedule**.  
   - *Expected output:* A green banner “Schedule set for 2026‑07‑04” appears.

   **Check‑in:** Do you see the schedule banner? If not, confirm the date format is `YYYY‑MM‑DD`.  

5. **Create a Lead List in Apollo**  
   - Click **Lists** in the left sidebar.  
   - Click the **+ New List** button.  
   - Name it **“SaaS Founders”**.  
   - Under **Add Leads**, select **Manual Upload**.  
   - Download the CSV template, fill it with at least 100 rows of dummy leads (Name, Email, Company, Title).  
   - Upload the CSV, then click **Import**.  
   - *Expected output:* “100 leads imported” confirmation.  

   **Check‑in:** Do you see the “100 leads imported” message? If not, verify the CSV columns match Apollo’s required format.

6. **Assign Leads to Campaign**  
   - Return to the **Lead Gen Q3** campaign page.  
   - Click **Add Leads**.  
   - Choose **SaaS Founders** from the list dropdown.  
   - Click **Add**.  
   - *Expected output:* The list count shows “100 leads” next to the campaign name.

7. **Integrate Apollo with Notion via Zapier**  
   - Open a new tab and go to `https://zapier.com`.  
   - Log in or sign up for the free plan (100 tasks/month).  
   - Click **Make a Zap**.  
   - For **Trigger**, search for and select **Apollo**.  
   - Choose trigger event **New Lead**.  
   - Click **Continue** and connect your Apollo account using the OAuth prompt.  
   - Test the trigger; Zapier will fetch a sample lead.  

   **Check‑in:** Do you see a sample lead in Zapier? If not, ensure Apollo API access is enabled in your Apollo settings.

8. **Set Up Notion as the Action**  
   - In Zapier, click **+ Add Action**.  
   - Search for **Notion** and select it.  
   - Choose action event **Create Database Item**.  
   - Connect your Notion account via OAuth.  
   - In the “Choose Database” dropdown, select **Lead Tracker** (create this database in Notion if it doesn’t exist, see step 10).  
   - Map Apollo fields:  
     * **Name** → `{{name}}`  
     * **Email** → `{{email}}`  
     * **Company** → `{{company}}`  
     * **Title** → `{{title}}`  
     * **Campaign** → *hard‑code* “Lead Gen Q3”.  
   - Click **Test & Continue**.  

   **Check‑in:** Does the test create a new Notion page? If not, verify that the database has the correct properties.

9. **Enable Zap**  
   - Toggle the Zap to **ON**.  
   - Note the Zap status: “All set – 0 tasks used today”.  
   - *Expected output:* Zapier shows “Zap is live” with a green checkmark.

10.

---

## Procedure 4.3: Create a Notion Dashboard for Real‑Time Lead Generation Metrics

1. **Open Notion**  
   • Visit https://www.notion.so/ and log in with your credentials.  
   • In the left sidebar, click the **+ New page** button.  
   • Name the page **“Lead Gen Dashboard”** and press **Enter**.  
   • Expected output: A blank page titled *Lead Gen Dashboard* appears.

2. **Add a Database**  
   • In the new page, type `/database` and press **Enter**.  
   • Select **“Table – Inline”**.  
   • Rename the first column header from *Title* to **“Lead ID”**.  
   • Click the **+ Add a property** button, choose **“Text”**, and name it **“Company”**.  
   • Add another property, choose **“Number”**, name it **“Lead Score”**.  
   • Add a property, choose **“Select”**, name it **“Status”**, with options *New*, *Contacted*, *Qualified*, *Lost*.

3. **Configure Apollo.io API Key**  
   • Open a new tab, go to https://app.apollo.io/settings/api.  
   • Click **“Generate New API Key”**.  
   • Copy the 32‑character key.  
   • Return to Notion, open the page settings by clicking **⋯** → **Page settings**.  
   • In the **“Webhooks”** section, click **“Add webhook”**.  
   • Paste the key into **“API Key”** field, set **Event** to **“New Lead”**, and **URL** to `https://hook.integromat.com/xxxxxxxx`.  
   • Click **Save**.  
   • Expected output: A new webhook entry showing *Apollo New Lead* with status *Active*.

4. **Create a Zapier Integration**  
   • Visit https://zapier.com/ and log in.  
   • Click **“Make a Zap”**.  
   • Search for **Apollo.io** in the Trigger app list, select it, and choose **“New Lead”**.  
   • Click **“Continue”**, then **“Test Trigger”**; you should see a sample lead record.  
   • Click **“Continue”**.  
   • For the Action app, search for **Notion** and choose **“Create Database Item”**.  
   • Connect your Notion account, then select the **Lead Gen Dashboard** database.  
   • Map Apollo fields to Notion properties: *Lead ID*, *Company*, *Lead Score*, *Status*.  
   • Click **“Continue”**, then **“Test & Continue”**.  
   • The test should create a new row in Notion.  
   • Click **“Turn on Zap”**.  
   • **Do you see a new row in the Notion database? If not, check that the Zap is switched to “On” and that the Apollo API key is active.**

5. **Add a Summary View**  
   • In the Notion database, click **“+ Add a view”**, name it **“Summary”**, choose **“Table”**.  
   • Click **“Filter”** → **Add a filter** → **Status** → **“Equals”** → **“Qualified”**.  
   • Click **“Sort”** → **Add a sort** → **Lead Score** → **Descending**.  
   • Expected output: A filtered table showing only qualified leads, sorted by highest score.

6. **Create a Graphical Card**  
   • In the same database page, type `/chart` → select **“Bar chart”**.  
   • In the chart settings, set **“Data source”** to the *Lead Gen Dashboard* database.  
   • For **“X‑axis”**, choose **“Lead Score”**; for **“Y‑axis”**, choose **“Count”**.  
   • Label the chart **“Lead Score Distribution”**.  
   • Click **“Save”**.  
   • Expected output: A bar chart dynamically updating with each new lead.

7. **Embed an Apollo Lead Map**  
   • In Notion, type `/embed` → choose **“Embed”**.  
   • Paste the Apollo map URL: `https://app.apollo.io/map

## Check-In: Module 4 Complete

- [ ] INTEGRATE Apollo.io Lead Data into a Notion Database completed and verified
- [ ] Automate Email Outreach Campaigns Using Apollo.io and Notion completed and verified
- [ ] Create a Notion Dashboard for Real‑Time Lead Generation Metrics completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 5: CLIENT ACQUISITION

## Overview

In this module you will learn how to convert the leads your AI‑powered system harvests into paying customers. You’ll build a high‑velocity outreach workflow that leverages Apollo.io’s data enrichment and Notion’s project orchestration to deliver a seamless sales funnel. Without completing Module 5, you risk letting high‑quality leads slip through the cracks, wasting the time and money you spent on data collection, and ultimately stalling your revenue growth. The outbound system you build here is the linchpin that transforms raw data into bookings, pipeline, and cash flow.  

You’ll set up a multi‑channel outreach cadence (email, LinkedIn, SMS) that automatically escalates leads through a Notion‑based pipeline, trigger follow‑ups via Make.com or Zapier, and capture responses in a real‑time dashboard. By the end of this module you will have a repeatable, scalable process that turns a single lead into a closed deal in less than 48 hours on average.

| Tool          | Purpose                                                  | Free Tier          | Paid Tier (Monthly) |
|---------------|----------------------------------------------------------|--------------------|---------------------|
| Apollo.io     | Targeted lead sourcing, enrichment, and bulk outreach   | 10 contacts/day    | $99 (Starter) – 2 k contacts/month |
| Notion        | Pipeline management, CRM, task automation               | Unlimited pages    | $8 (Personal Pro) – Unlimited blocks |
| Make.com      | Workflow automation between Apollo, Notion, and email    | 500 operations/month | $49 (Team) – 15 k operations/month |
| Zapier        | Alternative integration platform                          | 100 tasks/month    | $19 (Starter) – 2 k tasks/month |
| Semrush       | Competitive keyword and market research                  | 10 keywords/month  | $119 (Pro) – Unlimited keywords |
| Hostinger     | Affordable web hosting for landing pages                 | Free subdomain     | $3.95 (Single) – Unlimited bandwidth |
| Canva         | Design landing pages and email templates                 | 5 templates/month  | $12.99 (Pro) – Unlimited templates |
| ElevenLabs    | AI voice‑over for video content                         | 5 minutes/day      | $24 (Starter) – Unlimited minutes |

**Estimated time to complete:** 4 hours (including setup, testing, and initial outreach).

---

## Procedure 5.1: **Set Up Apollo.io Lead Scoring for Target Accounts**

1. **Open Apollo.io Login Page**  
   – Go to `https://app.apollo.io/login`.  
   – In the **Email** field, type `your.email@example.com`.  
   – In the **Password** field, type your password.  
   – Click the **Sign In** button (centered, blue).  

   *Expected result*: The Apollo.io dashboard loads with the left‑hand navigation bar visible.

2. **Navigate to Lead Scoring**  
   – In the navigation bar, click **Scoring** (icon: graph).  
   – Click **Lead Scoring** from the dropdown.  
   – On the Lead Scoring page, click **Create New Model** (top‑right, green button).

   *Expected result*: A blank model editor appears with “Model Name” input at the top.

3. **Name Your Model**  
   – In the **Model Name** input, type `High‑Value SMB Leads`.  
   – Click **Save Draft** (bottom‑right, gray button).  

   *Expected result*: The model appears in the list with status “Draft”.

4. **Add Scoring Criteria**  
   – Click **Add Criterion** (blue button).  
   – From the **Field** dropdown, select **Company Size**.  
   – Set **Operator** to **Greater Than**.  
   – In **Value**, type `50`.  
   – Click **Add 5 Points** in the **Score** box.  
   – Click **Save Criterion** (bottom‑right).  

   *Expected result*: Criterion shows under the model with “+5” points.

5. **Add Second Criterion**  
   – Click **Add Criterion** again.  
   – Choose **Industry** → **Equals** → type `Technology`.  
   – Click **Add 3 Points**.  
   – Click **Save Criterion**.  

   *Expected result*: Second criterion appears with “+3” points.

6. **Add Third Criterion**  
   – Click **Add Criterion**.  
   – Choose **Job Title** → **Contains** → type `Decision Maker`.  
   – Click **Add 4 Points**.  
   – Click **Save Criterion**.  

   *Expected result*: Third criterion appears with “+4” points.

7. **Set Minimum Score Threshold**  
   – In the **Minimum Score** field, type `12`.  
   – Click **Set Threshold** (green button).  

   *Expected result*: A red banner “Minimum Score set to 12” appears.

8. **Publish Model**  
   – Click **Publish Model** (top‑right, green button).  
   – Confirm by clicking **Yes, Publish** in the modal.  

   *Expected result*: Model status changes to “Active” and displays the number of leads scored.

**Do you see the “Active” status banner?**  
If not, *troubleshooting*: Refresh the page; ensure you are on the latest model, not a draft. If still missing, contact Apollo support at `support@apollo.io`.

---

9. **Export Scored Leads to CSV**  
   – In the left navigation, click **Leads**.  
   – Click the **Filters** icon (funnel).  
   – Set **Scoring Model** to `High‑Value SMB Leads`.  
   – Click **Apply Filters** (blue button).  
   – Click the **Export** button (top‑right, icon: download arrow).  

   *Expected result*: A CSV file downloads named `high_value_smb_leads.csv`.

10. **Create Notion Database for Leads**  
    – Open Notion in a new tab: `https://www.notion.so`.  
    – Click **+ New Page** in the left sidebar.  
    – Select **Table – Full Page**.  
    – Name the table `Apollo Leads`.  
    – Add columns:  
      - **Name** (Title)  
      - **Company** (Text)  
      - **Email** (Email)  
      - **Phone** (Phone)  
      - **Score** (Number)  
      - **Source** (Select: Apollo)  
      - **Status** (Select: New, Contacted, Qualified, Converted)  

    *Expected result*: A fully‑structured table appears with the specified columns.

11. **Import CSV into Notion**  
    – In the `Apollo Leads` table, click **⋮** (three dots) on the top right.  
    – Select **Merge with CSV**.  
    – Drag `high_value_smb_leads.csv` into the drop zone or click **Browse**.  
    – Map CSV columns to Notion columns (click each column header and select).  
    – Click **Import** (green button).  

    *Expected result*: Leads populate the table, each row matching a lead from the CSV.

12. **Create a Zapier Automation**  
    – Open Zapier: `https://zapier.com`.  
    – Click **Create Zap** (top‑right, orange button).  

    *Expected result*: Zap editor opens with “Trigger” step.

13. **Set

---

## Procedure 5.2: Automate Outreach Sequences with Apollo.io and Notion Workflow  

1. **Open Apollo.io** at https://app.apollo.io/ and click the **“Sign Up”** button in the top‑right corner.  
2. Enter your **email address** and a **strong password** (e.g., `Replit$2026`). Click **“Create account”**.  
3. Check your inbox for the verification email from Apollo. Click the **“Verify Email”** link.  
4. Log in again. Apollo will display the **Dashboard** with a blue bar at the top showing **“Welcome, [Your Name]”**.  
5. Click the **“Search”** tab on the left sidebar, then click **“New Search”**.  
6. In the search builder, set **Industry = “Software”**, **Job Title = “Product Manager”**, **Location = “United States”**. Click **“Save & Run”**.  
7. Wait for the search to complete. The results page will show **“1,235 results”**. Click the **“Export”** button (top-right) and choose **“CSV”**.  
8. Download the file to `C:\Users\<YourName>\Downloads\Apollo_Leads.csv`.  
9. **Open Notion** at https://www.notion.so/ and click **“New Page”** in the left sidebar.  
10. Name the page **“Lead Database – Apollo”** and choose **“Table – Full Page”** from the template picker.  
11. In the new table, click the **“+ Add a property”** button, select **“File”**, name it **“Lead File”**, and click **“Close”**.  
12. Click **“… •••”** next to the table title, choose **“Merge with CSV”**, and upload `Apollo_Leads.csv`.  
13. After import, you should see **1,235 rows**. Verify by scrolling to the bottom of the table.  
14. **Create a new Notion template** for outreach: click **“… •••”** → **“Template”** → **“New Template”**. Name it **“Apollo Outreach”**.  
15. Inside the template, add a **“Text”** block with the email subject: **“Intro – [Company]”**.  
16. Add a **“Text”** block for the body:  
    ```
    Hi {{FirstName}},
    
    I noticed you’re leading product initiatives at {{Company}}. Our AI‑driven analytics can help streamline your roadmap.
    
    Let’s schedule a quick call.
    
    Best,
    {{YourName}}
    ```  
17. Click **“Close”** to finish the template.  
18. **Set up a Zapier integration**: open https://zapier.com/, sign in (free tier: 100 tasks/month).  
19. Click **“Make a Zap”**.  

   **Trigger**:  
   - App: **Notion**  
   - Trigger Event: **“New Database Item”**  
   - Connect your Notion account.  
   - Choose **Database**: *Lead Database – Apollo*.  

   **Action**:  
   - App: **Apollo.io**  
   - Action Event: **“Send Email Sequence”**  
   - Connect your Apollo account.  
   - Map the following fields:  
     - **To** = `{{Email}}` (from Notion)  
     - **Sequence** = *“Initial Outreach”* (create this sequence in Apollo first – see step 21)  
     - **Personalization** = `{{FirstName}}`, `{{Company}}` (Apollo will replace tokens).  

   Click **“Continue”**, test the trigger, then test the action.  

20. Save the Zap and toggle it **ON**.  

**Do you see the new Zap listed in your Zapier dashboard with “ON” status?**  
If not, re‑authenticate Notion or Apollo, then retry step 19.  

21. In Apollo, click **“Sequences”** → **“New Sequence”**.  
22. Name it **“Initial Outreach”**. Add an email:

   - **Subject**: `Intro – {{Company}}`  
   - **Body**: copy the body from the Notion template.  
   - Click **“Add follow‑up”** → **“Day 2”** → **Email**  
     - **Subject**: `Following up – {{Company}}`  
     - **Body**:  
       ```
       Hi {{FirstName}},
       
       Just checking in to see if you’d like to discuss how our AI tools can benefit your product team.
       
       Cheers,
       {{YourName}}
       ```  

   Click **“Save Sequence”**.  

23. Return to Zapier and test the action again. The test should launch the **“

---

## Procedure 5.3: Build a Notion Dashboard to Track Lead Conversion Metrics

1. Open a web browser and navigate to **https://www.notion.so/login**.  
   - Enter your email and password.  
   - Click the **Login** button.  
   - Expected result: You land on the Notion workspace home screen with the “+ New Page” button visible on the left sidebar.

2. In the left sidebar, click the **+ New Page** button.  
   - In the pop‑up, type **Lead Conversion Dashboard** as the page title.  
   - Leave the icon as “📊”.  
   - Click **Create**.  
   - Expected result: A blank page titled “Lead Conversion Dashboard” opens.

3. Inside the new page, click the **+** button that appears when you hover over the first line.  
   - From the menu, select **Table – Full Page**.  
   - In the dialog, choose **Table** and click **Create**.  
   - Expected result: A new table view named “Table – Full Page” appears with one sample row.

4. Rename the first column header from **Name** to **Lead ID** by clicking the header and typing.  
   - Add a second column by clicking the **+** icon to the right of the last column.  
   - Choose **Title** and name it **Lead Source**.  
   - Add a third column: click the **+** icon again, select **Number**, and name it **Conversion Rate (%)**.  
   - Add a fourth column: click the **+** icon, select **Date**, and name it **Last Contacted**.  
   - Add a fifth column: click the **+** icon, select **Select**, and name it **Stage**.  
   - In the **Stage** column, click “+ New option” and add the following options: “Cold”, “Warm”, “Hot”, “Converted”.  
   - Expected result: Five columns exist with the appropriate data types and options.

   **Do you see the five columns with the correct names and data types? If not, ensure you have clicked the correct icons and typed the names exactly as shown.**

5. Click the **+** button in the first empty row under the **Lead ID** column.  
   - Enter **LD-0001**.  
   - Press **Tab** to move to **Lead Source** and type **Apollo.io**.  
   - Press **Tab** to move to **Conversion Rate (%)** and type **30**.  
   - Press **Tab** to move to **Last Contacted** and pick today’s date from the calendar.  
   - Press **Tab** to move to **Stage** and select **Warm** from the dropdown.  
   - Expected result: One fully populated row appears.

6. Click the three‑dot menu in the top right corner of the table and select **Properties**.  
   - Ensure the **Lead ID** column is set to **Unique** by toggling the switch next to the column name.  
   - Expected result: The **Lead ID** column now has a “Unique” badge.

7. Click **+** again in the first empty row to add a second lead:  
   - **LD-0002**, **Lead Source**: **Google Ads**, **Conversion Rate (%)**: **45**, **Last Contacted**: yesterday’s date, **Stage**: **Hot**.  
   - Expected result: Two rows now exist.

8. Now create a **Dashboard** view.  
   - Click the **+ Add a view** button above the table.  
   - Choose **Board** and name it **Lead Pipeline**.  
   - In the “Group by” dropdown, select **Stage**.  
   - Click **Create**.  
   - Expected result: A board view appears with four columns: Cold, Warm, Hot, Converted.

   **Do you see the board view with Stage‑grouped columns? If not, confirm that you selected “Board” and set “Group by” to Stage.**

9. Switch back to the **Table – Full Page** view by clicking its tab.  
   - Click the three‑dot menu in the top right and select **Sort**.  
   - Add a sort rule:  
     - Choose **Last Contacted** → **Descending**.  
   - Click **Apply**.  
   - Expected result: Rows are sorted with the most recent contact at the top.

10. Add a **Formula** column to calculate the days since last contact.  
    - Click the **+** icon, choose **Formula**, and name it **Days Since Contact**.  
    - In the formula editor, type:  
      ```
      dateBetween(now(), prop("Last Contacted"), "days")
      ```  
    - Click **Done**.  
    - Expected result: A new column shows the number of days elapsed for each row.

11. Open **Apollo.io** in a new tab (https://www.apollo.io).  
    - Log in with your credentials.  
    - Click **Leads** → **Lead List**.  
    - Apply a filter: Status = “New” and Source = “Generated”.  
    - Click **Export** → **CSV**.  
    - Save the file as **apollo_leads.csv** on your desktop.

12. Return to Notion, open the **Lead Conversion Dashboard** page, and click the **+** button in the left sidebar.  
    - Select **Embed** → **File**.  
    - Drag and drop **apollo_leads.csv** or click **Upload file**.  
    - Expected result: The CSV data appears as a table embedded within the page.

    **Do you see the embedded CSV table? If not, confirm that the file was uploaded correctly and that you are in the same Notion workspace.**

13. Click the three‑dot menu of the embedded CSV table and choose **Duplicate** → **Duplicate to page**.  
    - Name the new page **Apollo Lead Import**.  
    - Click **Duplicate**.  
    - Expected result: A new page with the imported leads is created.

14. In the **Apollo Lead Import** page, click the **+**

## Check-In: Module 5 Complete

- [ ] **Set Up Apollo.io Lead Scoring for Target Accounts** completed and verified
- [ ] Automate Outreach Sequences with Apollo.io and Notion Workflow completed and verified
- [ ] Build a Notion Dashboard to Track Lead Conversion Metrics completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 6: DELIVERY

## Overview  
In this module you will master the art of turning your AI‑powered lead‑generation promise into a repeatable, scalable service. We will walk through constructing a delivery pipeline that moves leads from Apollo.io extraction to Notion‑driven hand‑off, with built‑in quality checkpoints and automated client communication templates. This is the bridge between the “sell” and the “deliver” parts of your business model – without a robust delivery system you’ll see churn, unhappy clients, and wasted time chasing down errors.

Skipping Module 6 means you’ll be left with a spry lead‑gen engine but no reliable way to guarantee the leads meet client expectations. Your reputation will suffer, upsell opportunities vanish, and you’ll lose the ability to scale because you can’t confidently add new clients without risking quality. By the end of this module you will have a fully documented, repeatable workflow that you can hand off to a junior or automate with Zapier, ensuring every lead is verified, contextualized, and delivered on schedule.

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| **Apollo.io** | Enterprise‑grade prospect lookup, email finder, and outreach automation | Limited to 100 credits/month | $49/month (Starter) – 10,000 credits, $99/month (Professional) – 50,000 credits |
| **Notion** | Central knowledge base, project tracking, and client‑specific lead dashboards | Unlimited pages & blocks | $8/month per seat (Personal Pro) |
| **Zapier** | Automate data flow between Apollo, Notion, and email tools | 100 tasks/month | $19.99/month (Starter) – 750 tasks |
| **ChatGPT (OpenAI)** | Draft email templates, generate lead summaries, and QA notes | 3 million tokens/month | $20/month (ChatGPT‑Plus) |
| **Calendly** | Schedule discovery calls and hand‑off meetings | Unlimited events | $8/month per user |
| [**Grammarly**](https://grammarly.com/) | Ensure every client message is error‑free | 10 k characters/month | $12/month (Premium) |

**Estimated time to complete:** 4 hours of focused work, plus 2 hours for testing and refining the pipeline.

---

## Procedure 6.1: Set Up Quality Checkpoints for Lead Generation Pipelines  

**Objective:** Create a repeatable, auditable pipeline that pulls leads from Apollo.io, stores them in Notion, applies a quality scoring system, and flags leads that fail deliverability tests.  

---

### 1. Log in to Apollo.io  
- Open a browser and go to **https://app.apollo.io/login**.  
- Click **“Log in”** in the top‑right corner.  
- Enter your **email** and **password** and click **“Sign In”**.  

### 2. Create a Lead Search Query  
- Click the **“Search”** tab in the left menu.  
- Click **“+ New Search”** (button label is **“Create Search”**).  

### 3. Define Search Criteria  
- In the “Name” field, type **“Tech Startups – 2024”**.  
- Under **“Industry”**, select **“Information Technology & Services”**.  
- Under **“Company Size”**, check **“1–10”**, **“11–50”**, and **“51–200”**.  
- Under **“Location”**, type **“United States”** and select **“United States”** from the dropdown.  
- Click **“Save Search”** (button **“Save”**).  

### 4. Export Leads to CSV  
- With the search open, click the **“Export”** icon (top‑right, labeled **“Export”**).  
- In the modal, choose **“CSV”** and click **“Export”**.  
- **Do you see the “Download CSV” button?** If not, verify that the search returned >0 results.  

> **Expected Output:** A file named `Tech_Startups_2024.csv` appears in your browser’s download folder, containing at least 200 rows.  

---

### 5. Log in to Notion  
- Open **https://www.notion.so**.  
- Click **“Sign in”** and enter the same email used for Apollo.io.  

### 6. Create a New Database  
- In the workspace sidebar, click **“+ New Page”**.  
- Title the page **“Lead Quality Checklist”**.  
- In the body, type **“/table – inline”** and press **Enter** to create a new table database.  

### 7. Add Required Columns  
- Click **“+ Add a property”** (top‑right of the table).  
- Add the following columns:  
  1. **Lead ID** – **Number**  
  2. **Company** – **Title**  
  3. **Email** – **Email**  
  4. **Phone** –

---

## Procedure 6.2: Craft Automated Client Communication Templates with Apollo.io  

1. **Open Apollo.io** – Navigate to https://app.apollo.io and log in with your credentials.  
2. **Create a new Campaign** – In the left‑hand menu, click **Campaigns** → **+ New Campaign**.  
3. **Name the Campaign** – In the modal that appears, type **“Client Outreach – 2026 Q3”** into the **Campaign Name** field.  
4. **Select a Contact List** – Click **Choose List** → **+ New List** → **Name** the list **“Prospect Clients 2026”** → click **Save**.  
5. **Attach a Template** – In the same modal, click **Choose Template** → **+ New Template**.  
   - **Do you see the “+ New Template” button?** If not, refresh the page or clear your cache.  
6. **Open Notion** – In a new tab, go to https://www.notion.so and open the workspace **“LeadGen Ops”**.  
7. **Locate the Template Folder** – Inside the workspace, click the **Templates** page → **Client Communication**.  
8. **Copy the Email Template** – Open **“Email – Initial Outreach”** → click the **•••** icon → **Copy Link**.  
9. **Return to Apollo.io** – Paste the Notion link into the **Template Description** field.  
10. **Insert Placeholders** – In the Apollo editor, replace the default placeholders with **{{first_name}}**, **{{company_name}}**, **{{job_title}}**.  
    - **Do you see the placeholders correctly inserted?** If they appear as plain text, click the **Edit** icon and type them manually.  
11. **Add a Follow‑Up Sequence** – Click **Add Follow‑Up** → **+ New Email** → set **Subject** to **“Quick question about your 2026 goals”**.  
12. **Insert a Calendly Link** – In the body, type **“Schedule a call with us here: https://calendly.com/yourname/15min”**.  
13. **Enable “Send from Apollo”** – In the top right, toggle **Enable Email Sending** to **ON**.  
14. **Set Sending Parameters** – Under **Send Settings**, set **Start Date** to **2026‑07‑01** → **Time** to **09:00 AM EST** → **Frequency** to **1 per day**.  
15. **Activate Zapier Integration** – Open https://zapier.com → **Create Zap** → **Trigger**: Apollo → **Action**: Notion → **Event**: “New Email Sent”.  
    - **Do you see the Trigger “Apollo” in Zapier?** If not, search “Apollo” in the app directory and install the integration.  
16. **Configure Zapier Action** – In the Notion action, select the **LeadGen Ops** workspace → **Page** → **Client Communication Log**. Map the **Subject**, **Body**, and **Recipient** fields.  
17. **Test the Zap** – Click **Test Trigger** → **Test Action** → confirm that a new page appears in Notion titled **“Email Sent – John Doe”**.  
18. **Turn on the Zap** – Click **ON** in the top right corner of Zapier.  
19. **Review the Campaign in Apollo** – In the **Campaign Overview**, confirm that the status shows **“Active – 0 sent”**.  
20. **Send a Test Email** – In Apollo, click **Send Test Email** → choose **“Test to self”** → **Send**.  
    - **If you see “ERROR: Invalid email address”** – this means the placeholder **{{email}}** is missing. Go back to step 11 and add **{{email}}** to the body.  

---

### Tool Comparison Table: Apollo.io Plans

| Plan | Monthly Price | Email Credits | Lead Access | Support |
|------|---------------|---------------|-------------|---------|
| Free | $0 | 0 | 2,000 contacts | Community |
| Starter | $99 | 10,000 | 5,000 contacts | Email |
| Pro | $199 | 100,000 | 25,000 contacts | Priority |
| Enterprise | Custom | Unlimited | Unlimited | Dedicated |

*All plans include 30‑day free trial. The Pro plan is recommended for scaling.*

---

### Expected Output Checklist  

- **Step 10:** Placeholders appear as **{{first_name}}** etc. in the Apollo editor.  
- **Step 13:** The toggle shows **ON** and the sending icon turns green.  
- **Step 17:** A new Notion page titled **“Email Sent – Test Recipient”** appears.  
- **Step 20:** A confirmation banner reads **“Test email sent successfully”**.  

---

### Common Error Scenario  

- **Error:** “ERROR: Apollo API rate limit exceeded.”  
  - **Cause:** Too many automated sends in a short period.  
  - **Solution:** Pause the campaign → Reduce **Frequency** to **1 per 2 days** → Resume after 24 hours.  

Follow these steps precisely to create a fully automated, tracked client communication workflow that leverages Apollo.io’s outreach engine and Notion’s documentation power.

## Check-In: Module 6 Complete

- [ ] Set Up Quality Checkpoints for Lead Generation Pipelines completed and verified
- [ ] Craft Automated Client Communication Templates with Apollo.io completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 7: SCALING  

## Overview  
In this module you will transition your AI‑powered lead generation operation from a solo hustle to a scalable, team‑run business. We will walk you through the exact steps to hire your first contractor, draft SOPs that enable seamless delegation, and perform a rigorous margin analysis that guarantees 70 %+ gross profit. Skipping this module means you’ll keep bottlenecking on manual tasks, under‑utilizing your high‑margin AI workflow, and losing the ability to grow revenue linearly.  

You will learn how to use Apollo.io’s advanced prospecting API to feed leads straight into Notion, then trigger automated follow‑ups via Make.com and Zapier. With the SOPs you create, future hires can manage lead qualification, outreach sequencing, and reporting without your constant oversight. The margin analysis will teach you to price tiers, account for contractor rates, and project cash flow for 12 months ahead.  

**Tools Needed**  

| Tool          | Purpose                                   | Free Tier                                      | Paid Tier (Monthly) |
|---------------|-------------------------------------------|-----------------------------------------------|---------------------|
| Apollo.io     | Lead sourcing & enrichment API            | 5 lead searches/day, 100 contacts per project | $39 (Starter)       |
| Notion        | SOP repository, project board, database   | Unlimited pages, 1 GB file uploads             | $8 (Personal Pro)   |
| Make.com      | Automation of API calls & email sequences | 1 000 operations/month, 1 scenario            | $14 (Starter)       |
| Zapier        | Cross‑app triggers & actions              | 5 zaps, 100 tasks/month                       | $19 (Starter)       |
| Canva         | Lead‑gen landing page & email templates   | 30 templates, 5 GB storage                    | $12 (Pro)           |
| ElevenLabs    | Voice‑over for outreach videos            | 5 minutes/day                                 | $24 (Starter)       |

**Estimated Time to Complete**  
12–14 hours total, split into three 4–5 hour procedures: hiring, SOP creation, and margin analysis.  

---

---

## Procedure 7.1: HIRE YOUR FIRST LEAD OUTREACH CONTRACTOR VIA UPWORK

**Goal:** Secure a vetted, hourly‑rate lead outreach specialist to scale your AI‑powered lead generation service. By the end of this procedure you will have a signed contract, a clear scope of work, and a workflow in Notion that tracks the contractor’s deliverables.

---

### 1. Create or Log Into Your Upwork Account  
1.1 Open **https://www.upwork.com/ab/hire** in Chrome.  
1.2 Click ****SIGN UP** (top‑right).  
1.3 In the modal, select **“I’m a client”** and enter your **Email** (e.g., josh@menshlyglobal.com), **Password** (min 8 chars, include a number), and **Company Name** (Menshly Global).  
1.4 Click ****CREATE ACCOUNT**.  
1.5 Check your inbox for the verification email from Upwork and click the verification link.  

> **Do you see the “Welcome to Upwork” dashboard?**  
> If not, double‑check the verification link; you may need to click **“Resend verification”** on the Upwork login page.

---

### 2. Complete Your Client Profile  
2.1 In the top navigation, click ****MY ACCOUNT** → **Profile**.  
2.2 Fill in:  
- **Title**: “Founder – AI Lead Generation”  
- **Hourly Rate**: “$0” (client side, Upwork handles billing).  
- **Company Size**: “1–5 employees”.  
2.3 Scroll to

---

## Procedure 7.2: Create SOPs for Delegating Apollo.io Lead Scoring

1. **Open Apollo.io** – Go to https://app.apollo.io/auth/login.  
   In the login form, type your email in the **Email** field and your password in the **Password** field.  
   Click the **Login** button (bold).  

2. **Navigate to Lead Scoring** – Once logged in, locate the left‑sidebar menu.  
   Click **Lead Scoring** (bold).  

3. **Create a New Scorecard** – On the Lead Scoring page, click **Create New Scorecard** (bold).  
   In the pop‑up, enter **Delegated Lead Scoring SOP** as the name.  
   Click **Save** (bold).  

4. **Add First Scoring Rule** – In the new scorecard, click **Add Rule** (bold).  
   In the rule editor, set:  
   - **Field**: Company Size  
   - **Operator**: Greater Than  
   - **Value**: 100  
   - **Points**: 10  
   Click **Save Rule** (bold).  

5. **Add Second Scoring Rule** – Click **Add Rule** again (bold).  
   Set:  
   - **Field**: Job Title  
   - **Operator**: Contains  
   - **Value**: CEO  
   - **Points**: 15  
   Click **Save Rule** (bold).  

   **Do you see both rules listed?**

---

## Procedure 7.3: ANALYZE PROFIT MARGINS OF YOUR LEAD GENERATION PIPELINES

1. **Open Apollo.io**  
   - Navigate to `https://app.apollo.io/login`.  
   - Enter your corporate email and password.  
   - Click the **Login** button.  
   - *Expected:* Apollo dashboard with your “My Leads” view.

2. **Export Lead List**  
   - Click the **Export** button in the top‑right corner of the “My Leads” page.  
   - In the pop‑up, choose **CSV** as the format.  
   - Click **Export CSV**.  
   - *Expected:* A `leads_YYYYMMDD.csv` file downloads to your computer’s default folder.

3. **Open Notion**  
   - Go to `https://www.notion.so`.  
   - Sign in with the same credentials used for Apollo.  
   - Click on the workspace named **LeadGen Pipeline**.  
   - Open the database view called **Pipeline Tracker**.

4. **Export Pipeline Tracker**  
   - In the top‑right of the database, click the three‑dot menu (**⋮**).  
   - Select **Export** → **CSV**.  
   - Name the file `pipeline_YYYYMMDD.csv`.  
   - *Expected:* The file is saved locally.

5. **Do you see both CSV files in your Downloads folder?**  
   - If not, check the browser’s download settings or try the **Download** icon in the export dialog.  
   - If the files are missing, repeat steps 2 and 4.

6. **Launch Google Sheets**  
   - Open `https://docs.google.com/spreadsheets/`.  
   - Click **Blank** to create a new spreadsheet.  
   - Rename the file to **LeadGen Profit Analysis**.

7. **Import Apollo Leads**  
   - In Google Sheets, click **File** > **Import** > **Upload** > drag `leads_YYYYMMDD.csv` into the box.  
   - Choose **Insert new sheet(s)** and click **Import data**.  
   - *Expected:* A new sheet named **Apollo_Leads** appears with all columns.

8. **Import Pipeline Tracker**  
   - Repeat step 7, uploading `pipeline_YYYYMMDD.csv`.  
   - The sheet should be named **Pipeline_Tracker**.

9. **Create a Cost Sheet**  
   - Add a new sheet named **Cost Breakdown**.  
   - In column A, list the following tools:  
     | Tool | Monthly Cost | Free Tier | Notes |
     |------|--------------|-----------|-------|
     | Apollo.io | $99 | 5,000 credits/month | Pro plan |
     | Notion | $8/seat | Unlimited blocks | Team plan |
     | Zapier | $19 | 100 tasks/month | Starter plan |
     | Make.com | $49 | 1,000 operations/month | Professional plan |
     | Google Workspace | $6/seat | 15 GB | Basic plan |
   - In column B, enter the monthly cost values.  
   - In column C, enter the free‑tier usage.  
   - *Expected:* A fully populated table.

10. **Calculate Total Cost**  
    - In cell `B7` of **Cost Breakdown**, enter:  
      ```
      =SUM(B2:B6)
      ```
    - In cell `C7`, enter:  
      ```
      =SUM(C2:C6)
      ```
    - *Expected:* `B7` shows **$183** and `C7` shows the free‑tier totals.

11. **Determine Total Leads**  
    - In **Apollo_Leads**, find the column labeled **Lead ID**.  
    - In cell `A1` of a new sheet named **Metrics**, type:  
      ```
      =COUNTA(A2:A)
      ```
    - Rename the formula result to **Total Leads**.  
    - *Expected:* A number like **3,200**.

12. **Compute Cost Per Lead**  
    - In **Metrics**, in cell `B1`, enter:  
      ```
      =CostBreakdown!B7 / A1
      ```
    - Format the cell as **Currency**.

## Check-In: Module 7 Complete

- [ ] HIRE YOUR FIRST LEAD OUTREACH CONTRACTOR VIA UPWORK completed and verified
- [ ] Create SOPs for Delegating Apollo.io Lead Scoring completed and verified
- [ ] ANALYZE PROFIT MARGINS OF YOUR LEAD GENERATION PIPELINES completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 8: ADVANCED PATTERNS

## Overview

In Module 8 you will master the high‑stakes playbooks that transform a basic AI‑driven lead‑gen service into a scalable, recurring‑revenue machine. This module teaches you how to layer premium upsells, create high‑ticket service tiers, and lock in clients with productized packages that deliver measurable ROI. Skipping this module means you’ll continue to churn low‑margin leads and miss the opportunity to command premium pricing—your competitors will fill the gap while you stay stuck in the free‑lead generation rabbit hole.

You will learn to orchestrate Apollo.io’s bulk outreach with Notion’s database workflow, then plug the pipeline into Make.com for seamless automation. You’ll also acquire techniques for upselling with AI‑generated content from Vapi or [Fliki AI](https://fliki.ai?referral=noah-wilson-w84be4), and for building a subscription funnel that uses Zapier to sync with Klaviyo or ActiveCampaign. By the end of the module you’ll have a repeatable, gamified lead‑gen system that can be scaled to handle thousands of prospects per month while you earn a steady stream of recurring revenue.

| Tool          | Purpose                                  | Free Tier                                   | Paid Tier                          |
|---------------|------------------------------------------|---------------------------------------------|------------------------------------|
| Apollo.io     | Prospect discovery & outreach            | 1 day free trial, 20 credit/day             | $99/month (Pro)                    |
| Notion        | Knowledge base & workflow orchestration  | Unlimited pages, 5 MB file uploads          | $8/month per seat (Personal Pro)  |
| Make.com      | Automation & integrations                | 1 000 operations/month, 30 min scenario run  | $19/month (Starter)                |
| Zapier        | Workflow automation                      | 5 Zaps, 100 tasks/month                    | $19.99/month (Starter)             |
| Vapi          | AI‑powered voice & SMS services          | 1 000 tokens/month                          | $20/month (Standard)               |
| Fliki AI      | Text‑to‑video production                | 200 minutes/month                           | $15/month (Pro)                    |

**Estimated time to complete:** 4 – 6 hours.

---

## Procedure 8.1: Create Premium Lead Qualification Bundles for Apollo.io Campaigns

1. **Open Apollo.io**  
   - URL: `https://app.apollo.io/`  
   - Log in with your credentials (Enterprise plan – $99/month per user).  
   - Expected UI: Dashboard with “Campaigns” tab highlighted.

2. **Navigate to Campaigns**  
   - In the left sidebar, click **Campaigns**.  
   - On the top right, click the **+ New Campaign** button (bold).  
   - Expected: Blank campaign form appears.

3. **Name the Campaign**  
   - Field: “Campaign Name”  
   - Input: `Premium Lead Bundle – Q3 2026`  
   - Click **Save** (bold).  
   - Expected: Campaign card appears in the list.

4. **Set Target Criteria**  
   - In the campaign editor, scroll to “Targeting” section.  
   - Toggle “Industry” to **Finance** and “Job Title” to **CFO**.  
   - Set “Company Size” to **51–200** employees.  
   - **Check‑in**: Do you see “Finance” and “CFO” filters applied? If not, return to the Targeting tab and re‑select.

5. **Enable Lead Qualification Rules**  
   - Scroll to “Lead Qualification” section.  
   - Toggle “Enable Qualification” to ON.  
   - Set “Score Minimum” to **80**.  
   - Add rule: “Number of Open Positions > 5”.  
   - Click **Add Rule** (bold).  
   - Expected: Three rules listed under Qualification.

6. **Configure Lead Export Settings**  
   - Scroll to “Export” section.  
   - Choose “Export Format” = **CSV**.  
   - Check “Include Notes” and “Include Email Domains”.  
   - Click **Save Settings** (bold).  
   - Expected: Confirmation toast “Export settings saved”.

7. **Run a Test Export**  
   - At the top, click **Run Export** (bold).  
   - Wait for the spinner to disappear.  
   - Download the CSV file.  
   - Open the file in Excel; verify columns: Name, Email, Company, Score, Notes.  
   - **Check‑in**: Does the CSV contain at least 10 rows? If not, reduce the score threshold to 60 and re‑run.

8. **Upload CSV to Notion**  
   - Open Notion in a new tab: `https://www.notion.so/`.  
   - Sign in with your workspace.  
   - Create a new page titled **Lead Bundles – Q3 2026**.  
   - Inside the page, click the **+ Add a block** button and select **Table – Full Page**.  
   - Name the table `Premium Leads`.  
   - Click the **Import** icon (cloud with arrow) in the top right of the table and choose the CSV file.  
   - Expected: Table populated with 10+ rows.

9. **Add Bundle Metadata**  
   - In Notion, add a new column **Bundle ID** (select “Number” type).  
   - Add another column **Bundle Price** (select “Number” type, format as currency).  
   - Populate Bundle ID sequentially (1, 2, 3…).  
   - Set Bundle Price to **$499** for each lead.  
   - **Check‑in**: Do you see the new columns and sample data? If not, ensure the column type is set correctly.

10. **Create Bundle Summary Page**  
    - In the same Notion workspace, click **+ New Page** → **Template** → **Database** → **Table**.  
    - Name it **Bundle Summary – Q3 2026**.  
    - Add properties: `Bundle ID` (Number), `Lead Count` (Number), `Total Value` (Formula: `Lead Count * 499`).  
    - Click **Create**.  
    - Expected: Empty summary table ready for linkage.

11. **Link Leads to Summary**  
    - Go back to `Premium Leads` table.  
    - Add a new column **Bundle Ref** (select “Relation”).  
    - Link it to the **Bundle Summary** database.  
    - For each lead, select the appropriate Bundle ID.  
    - Expected: Relationship icon appears next to each lead.

12. **Calculate Lead Count per Bundle**  
    - In **Bundle Summary**, click the three dots on the right of the `Lead Count` column header.  
    - Select **Rollup** → `Premium Leads` → `Bundle Ref` → `Count`.  
    - Expected: Each row now shows the number of leads in that bundle.

13. **Set Bundle Price Formula**  
    - In **Bundle Summary**, click the three dots on the right of the `Total Value` column header.  
    - Select **Formula** → `Lead Count * 499`.  
    - Expected: Total value updates automatically.

14. **Export Summary for Billing**  
    - Click the **•••** button on the top right of **Bundle Summary** → **Export** → **CSV**.  
    - Save the file as `Bundle_Summary_Q3_2026.csv`.  
    - **Check‑in**: Does the CSV contain columns Bundle ID, Lead Count, Total Value? If not, revisit the rollup and formula settings.

15. **Integrate Billing via Zapier**  
    - Open Zapier: `https://zapier.com/`.  
    - Click **Make a Zap** (bold).  
    - Trigger App: **Notion** → Trigger Event: **New Database Item** (choose `Bundle

---

## Procedure 8.2: Build Subscription‑Based Lead Nurture Workflows in Notion

1. **Open Notion**  
   Go to <https://www.notion.so/> and sign in or sign up with your business email.  
   *Expected output:* You should land on your personal dashboard.  
   *Do you see the “+ Add a page” button? If not, log out and log back in.*

2. **Create a new “Leads” database**  
   - Click **"+ Add a page"** (bold).  
   - Select **"Table – Full page"** from the pop‑up.  
   - Name the page **“Leads”** and press **Enter**.  
   - In the top right, click **"… (More options)"** and choose **"Add a property"** (bold).  
   - Add the following properties:  
     - **Name** (Title)  
     - **Email** (Email)  
     - **Stage** (Select) – options: *New, Prospect, Nurture, Qualified, Closed*  
     - **Source** (Select) – options: *Apollo, Referral, Website*  
     - **Subscription Level** (Select) – options: *Basic, Premium, Enterprise*  
     - **Last Contacted** (Date)  
     - **Days Since Contacted** (Formula) – formula: `dateBetween(now(), prop("Last Contacted"), "days")`  
   *Expected output:* The table should display 7 columns ready for data entry.  
   *Do you see the “Days Since Contacted” column? If not, re‑create the formula.*

3. **Export leads from Apollo.io**  
   - Open Apollo.io at <https://app.apollo.io/>.  
   - Navigate to **“Projects”** → click on the project **“Lead Generation – Nurture”**.  
   - Click the **"Export"** button (bold) in the top right, choose **"CSV"**, and download the file.  
   *Expected output:* A file named `leads_nurture_YYYYMMDD.csv` appears in your Downloads folder.  
   *Do you see the CSV file? If not, check that the project has contacts.*

4. **Import the CSV into Notion**  
   - In the **“Leads”** database, click **"…" (More options)** → **"Merge CSV"** (bold).  
  

## Check-In: Module 8 Complete

- [ ] Create Premium Lead Qualification Bundles for Apollo.io Campaigns completed and verified
- [ ] Build Subscription‑Based Lead Nurture Workflows in Notion completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 9: FINANCIAL OPERATIONS

## Overview

Module 9 is the bedrock of every profitable AI‑lead generation venture. It teaches you to **track revenue in real‑time, strategically increase pricing, and craft razor‑sharp proposal and contract templates** that convert prospects into paying customers. Without this module, you’ll be operating in a revenue blind‑spot: no clear view of cash flow, no data‑driven price hikes, and a chaotic proposal process that wastes time and erodes trust. Skipping it means you’ll miss incremental margin opportunities, risk over‑ or under‑pricing, and expose yourself to legal pitfalls from poorly drafted contracts.

This module’s two core procedures build a **financial dashboard** in Notion that pulls live data from Apollo.io and Stripe via Make.com, then uses that data to trigger automated price‑increase notifications in Klaviyo. You’ll also create a **proposal template library** that auto‑fills client details, pricing tiers, and terms, ensuring every bid is consistent, compliant, and ready for instant delivery.

| Tool        | Purpose                           | Free Tier                                | Paid Tier |
|-------------|-----------------------------------|------------------------------------------|-----------|
| Notion      | Database, dashboard, contract repo| Unlimited pages, 5 GB storage            | Plus: $8 / mo (10 GB) |
| Apollo.io   | Lead data & contact management    | 50 credits/month (limited searches)      | Pro: $99 / mo (1,000 credits) |
| Stripe      | Payment processing & invoicing    | 0 % platform fee, 2.9 % + 30 ¢ per tx   | Standard: 2.9 % + 30 ¢ |
| Make.com    | Automation between tools          | 500 operations/month                     | Starter: $49 / mo (5,000 ops) |
| Klaviyo     | Email automation & billing alerts | 200 contacts, 2,500 emails/month        | Essentials: $30 / mo (5,000 emails) |

**Estimated time to complete:** 1 hour 30 minutes (including dashboard setup and template finalization).

---

## Procedure 9.1: SET UP YOUR AI LEAD GENERATION REVENUE DASHBOARD IN NOTION

1. **Open Notion**  
   - URL: https://www.notion.so  
   - Click **LOG IN** in the top‑right corner.  
   - Enter your email and password, then **CLICK** **SIGN IN**.  
   - *Expected output*: You are taken to the workspace home page with a blue “+ NEW PAGE” button.  
   - *Do you see the “+ NEW PAGE” button? If not, refresh the page or clear your cache.*

2. **Create a new database**  
   - Click **+ NEW PAGE** → **TEMPLATE** → **TABLE – FULL PAGE**.  
   - Name the page **Lead Revenue Dashboard**.  
   - Click **CREATE**.  
   - *Expected output*: A blank table with columns “Name”, “Date”, “Source”, “Revenue”, “Status”.  
   - *Do you see the table with those columns? If not, click the “+” in the top‑right of the table to add a new table.*

3. **Add custom properties**  
   - Click the column header “Name” → **PROPERTY** → **Edit property type** → **Text**.  
   - Add a new property: click **+ ADD A PROPERTY** → **Revenue** → **Number** → **Currency** → “USD”.  
   - Add **Lead Source** → **Select** → options: “Apollo.io”, “LinkedIn”, “Referral”.  
   - Add **Status** → **Select** → options: “New”, “Contacted”, “Qualified”, “Closed‑Won”.  
   - *Expected output*: Table now has five columns: Name, Date, Lead Source, Revenue, Status.  
   - *Check-in*: Do you see all five columns? If “Revenue” shows as “Number” instead of “Currency”, click the column header → **PROPERTY** → **Edit property type** → **Currency** → “USD”.

4. **Connect Apollo.io to Zapier**  
   - Open new tab → https://zapier.com.  
   - Click **SIGN UP** → use your email → **CREATE ACCOUNT**.  
   - Once logged in, click **Make a Zap**.  
   - Search for **Apollo.io** in the trigger app search bar → click **Apollo.io**.  
   - Choose trigger **New Lead** → **Continue**.  
   - Connect your Apollo.io account by clicking **Sign in to Apollo.io** → enter your API key (found in Apollo.io → Settings → API).  
   - *Expected output*: Zapier shows “Apollo.io account connected”.  
   - *Check‑in*: Do you see “Apollo.io account connected”? If you see **ERROR: Authentication failed**, double‑check your API key and try again.

5. **Set up the action step**  
   - Click **+ ADD ACTION** → search **Notion** → click **Notion**.  
   - Choose action **Create Database Item** → **Continue**.  
   - Connect your Notion account: click **Sign in to Notion** → allow **Read & Write** permissions.  
   - In **Database**, choose **Lead Revenue Dashboard**.  
   - Map fields:  
     - **Name** → **Lead Name** (from Apollo.io field)  
     - **Date** → **Date Added** (from Apollo.io)  
     - **Lead Source** → **“Apollo.io”** (static text)  
     - **Revenue** → **“0”** (static number, will be updated later)  
     - **Status** → **“New”** (static text)  
   - Click **Continue** → **Test & Review** → **Turn on Zap**.  
   - *Expected output*: “Zap is live” banner.  
   - *Check‑in*: Do you see “Zap is live”? If not, verify that all fields are mapped correctly.

6. **Verify Zapier sync**  
   - In Apollo.io, create a test lead (Name: “Test Lead 1”, Email: test1@example.com).  
   - Wait 2–3 minutes for Zapier to process.  
   - In Notion, open **Lead Revenue Dashboard**.  
   - *Expected output*: A new row appears with “Test Lead 1”, current date, “Apollo.io”, $0, “New”.  
   - *Check‑in*: Do you see the new row? If not, click Zapier → Task History → find the Zap → view logs for errors.

7. **Add a formula for monthly revenue**  
   - In Notion, click the column header **Revenue** → **PROPERTY** → **Edit property type** → **Formula**.  
   - Enter formula: `if(prop("Status") == "Closed‑Won", prop("Revenue"), 0)`  
   - Create a new property **Monthly Revenue** → **Formula** → `sum(prop("Revenue"))` (this will be a roll‑up if you nest databases; for simplicity, keep as a separate column).  
   - *Expected output*: Total revenue updates automatically when status changes to Closed‑Won.  
   - *Check‑in*: Do you see the formula applied? If the formula shows errors, ensure parentheses are balanced.

8. **Create a view for closed‑won leads**  
   - In the table, click **+ ADD A VIEW** → name **Closed‑Won** → select **Table** → **Create**.  
   - Click the filter icon → **Add a filter** → **Status** → **Is** → **Closed‑Won**.  
   - *Expected output*: Only rows with status “Closed‑Won” are visible.  
   - *Check‑in*: Do you see the filter applied? If not, ensure the filter is set to “Status” → “Is” → “

---

## Procedure 9.2: Draft Automated Pricing Increase Proposal Templates with Apollo.io

1. **Open Apollo.io**  
   - Go to **https://www.apollo.io**.  
   - Click the **LOGIN** button in the upper‑right corner.  
   - Enter your credentials (username/email and password).  
   - Click **SIGN IN**.  
   - *Expected output:* Apollo dashboard with the “My Pipeline” tab highlighted.

2. **Create a New Lead List**  
   - In the left sidebar, click **LISTS**.  
   - Click the **+ NEW LIST** button.  
   - In the dialog, type **“Pricing Increase Prospects”** into the **LIST NAME** field.  
   - Select **“Prospecting”** from the **CATEGORY** dropdown.  
   - Click **CREATE LIST**.  
   - *Expected output:* A new list appears with the heading “Pricing Increase Prospects”.

3. **Add Criteria to the List**  
   - In the newly created list, click **ADD CRITERIA**.  
   - Choose **“Company Size”** → **“> 50 employees”**.  
   - Click **APPLY**.  
   - Select **“Industry”** → **“Technology”**.  
   - Click **APPLY**.  
   - *Expected output:* Filters applied; list shows 0 results initially.

4. **Populate the List with Leads**  
   - Click **+ ADD LEADS**.  
   - Select **“Apollo Database”**.  
   - In the search box, type **“software company”** and hit **ENTER**.  
   - Check the first 20 checkboxes in the results.  
   - Click **ADD TO LIST**.  
   - *Interactive check‑in:* Do you see at least 20 leads added to “Pricing Increase Prospects”? If not, refresh Apollo and repeat step 4.

5. **Export Lead Data to CSV**  
   - In the list view, click the **EXPORT** button (top right).  
   - Choose **CSV**.  
   - Click **EXPORT** again.  
   - Download the file when the browser prompts.  
   - *Expected output:* A file named `Pricing_Increase_Prospects.csv` in your Downloads folder.

6. **Open Notion**  
   - Navigate to **https://www.notion.so**.  
   - Click **LOGIN** and enter your credentials.  
   - Click **SIGN IN**.  
   - *Expected output:* Notion workspace with your home dashboard.

7. **Create a New Database Page**  
   - Click **+ NEW PAGE** in the left sidebar.  
   - Enter **“Pricing Increase Proposal Templates”** as the page title.  
   - Select **“Table – Full page”** from the database options.  
   - Click **CREATE**.  
   - *Expected output:* A blank table with columns: Name, Lead, Client, Proposal, Status.

8. **Import CSV into Notion**  
   - In the new table, click **⋮⋮** on the top right and select **“Merge with CSV”**.  
   - Upload the `Pricing_Increase_Prospects.csv` file.  
   - Map the CSV columns:  
     - `Name` → **Title**  
     - `Email` → **Lead** (create a new **Email** property, type **Email**)  
     - `Company` → **Client** (create a new **Text** property, type **Text**)  
   - Click **IMPORT**.  
   - *Expected output:* 20 rows populated with lead data.

9. **Add New Properties for Proposal Workflow**  
   - Click the **+ ADD A PROPERTY** button.  
   - Create **“Proposal Template”** → **Select**.  
   - Add options: **“Standard”, “Premium”, “Enterprise”**.  
   - Create **“Status”** → **Select**.  
   - Add options: **“Draft”, “Sent”, “Accepted”, “Rejected”**.  
   - *Interactive check‑in:* Do you see the new “Proposal Template” and “Status” columns? If not, ensure you are editing the correct database.

10. **Create a Sample Proposal Template**  
    - In the **Proposal Template** column, click the first cell, choose **“Standard”**.  
    - In the **Status** column, set **“Draft”**.  
    - Click the **three dots** on the right of the row and select **“Duplicate”**.  
    - Rename the duplicated row to **“Standard Proposal – ABC Corp.”**  
    - In the new row, in the **Proposal** column, paste the following Markdown template:

```
# Proposal: Pricing Increase Service

**Client:** {{Client}}

**Date:** {{Date}}

## Scope of Work
- AI‑driven lead generation
- Monthly reporting

## Pricing
- Base: ${{BasePrice}}
- Increase: ${{Increase}}

## Terms
- 30‑day payment
- 12‑month contract
```

    - Replace placeholders with actual values (e.g., $2,000 base, $200 increase).  
    - *Expected output:* A fully populated proposal row.

11. **Automate Placeholder Replacement via Make.com**  
    - Open Make.com (free tier up to 10,000 operations per month).  
    - Click **CREATE A new scenario**.  
    - Add the first module: **Notion** → **Watch Database Items**.  
      - Connect your Notion account; select the **“Pricing Increase Proposal Templates”** database.  
      - Set **Trigger** to **“New or updated item”**.  
    - Add a second module: **Text** → **Text replace**.  
      - Map the **Proposal** field to the Text input.  
      - Create a mapping rule: Replace `{{Client}}` with the **Client** property.  
      - Repeat for `{{Date}}`, `{{BasePrice}}`, `{{Increase}}`.  
    - Add a third module: **

## Check-In: Module 9 Complete

- [ ] SET UP YOUR AI LEAD GENERATION REVENUE DASHBOARD IN NOTION completed and verified
- [ ] Draft Automated Pricing Increase Proposal Templates with Apollo.io completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 10: LAUNCH PLAN

## Overview

In this module you will receive a day‑by‑day execution calendar that propels your AI‑powered lead generation business from zero to the first paying client in exactly 30 days. The plan is broken into actionable blocks: research & validation, pipeline setup, automation scripting, outreach, and client hand‑over. Each day builds directly on the previous, ensuring you never waste time on redundant tasks. Skipping this module means launching without a clear roadmap, which typically results in wasted hours on ineffective outreach, lost leads, and a slow, uncertain revenue start‑up.

The calendar is not a generic template; it is a proven sequence that aligns Apollo.io’s prospecting engine with Notion’s workflow engine, wrapped in Zapier automations for instant lead capture and email dispatch. By following every step, you will have a fully automated pipeline that generates, qualifies, and nurtures leads while you focus on closing deals. Missing any step will break the flow, cause data silos, and leave you unable to scale efficiently.

| Tool          | Purpose                                | Free Tier                                        | Paid Tier (Monthly) |
|---------------|----------------------------------------|--------------------------------------------------|---------------------|
| Apollo.io     | Lead search & email outreach           | 20 credits/month, 10,000 profile views           | $99 (Pro)           |
| Notion        | Project & CRM tracking                 | Unlimited pages, 5GB file storage                | $8/user (Personal)  |
| Zapier        | Automation between Apollo & Notion     | 100 tasks/month, 5 Zaps                          | $19 (Starter)       |
| Replit        | Scripting & testing automation scripts | Unlimited public repls, 500MB storage            | $7 (Hacker)         |
| Canva         | Email templates & social graphics      | Unlimited free designs, 5 GB storage             | $12 (Pro)           |

**Estimated time to complete:** 3 full days of focused work (≈ 9‑10 hours total).

---

## Procedure 10.1: Launch Your Apollo.io Lead Generation Pipeline

1. **Open** your browser and go to the Apollo.io sign‑up page:  
   `https://apollo.io/signup`.  
2. **Fill** in the form:  
   * Email: `you@yourdomain.com`  
   * Password: `StrongPass!2026` (at least 12 characters, upper‑case, lower‑case, number, symbol).  
   **Click** the **Sign Up** button.  
3. **Check** your inbox for the verification email from Apollo.io.  
   **Click** the verification link inside the email.  
4. **Log in** to Apollo.io: `https://apollo.io/login`.  
   **Verify** you see the **Dashboard** with the **Explore** tab.  
   *If you do not see the Dashboard, close the tab, open a new one, and log in again.*



---

## Procedure 10.2: Configure Your Notion Lead Tracking Dashboard

1. **Open your browser and navigate to** `https://www.notion.so/`.  
2. **Log in** with your existing credentials or click **SIGN UP** to create a new account (free tier: 1 GB storage, unlimited pages).  
3. **Create a new workspace** by clicking the **Add a new workspace** button on the left sidebar.  
4. **Name the workspace** “LeadGen AI” and click **Create**.  
5. **Do you see the new workspace with the default “Home” page?** If not, refresh the page or log in again.  

6. **Click the + New Page** button in the left sidebar, then choose **Database → Table – Full Page**.  
7. **Rename the table** to “Leads” by double‑clicking the title and typing **Leads**.  
8. **Add the following columns** by clicking **+ Add a property**:  
   - **Lead Name** (Title)  
   - **Company** (Text)  
   - **Email** (Email)  
   - **Phone** (Phone)  
   - **Status** (Select) – options: New, Contacted, Qualified, Unqualified, Converted  
   - **Source** (Select) – options: Apollo, LinkedIn, Email, Referral  
9. **Do you see all six columns?** If “Phone” or “Source” is missing, reopen the column menu and add them again.  

10. **Configure the “Status” property** by clicking the dropdown arrow next to the column header, selecting **+ New option**, and entering each status value.  
11. **Make “Source” a Select property** by clicking the dropdown, choosing **+ New option**, and adding the source values.  
12. **Set the default status** to “New” by opening the property settings and checking **Default value → New**.  
13. **Apply a filter** to show only “New” leads: click the **Filter** button, choose **Status** → **Is** → **New**.  
14. **Do you see only rows with “New” status?** If all rows appear, ensure the filter is active; click the filter icon again and confirm the rule.  

15. **Create a new template** for Apollo leads: click **+ New** → **+ New template** → name it **Apollo Lead**.  
16. **Add the following default values** inside the template:  
   - **Status** set to **New**  
   - **Source** set to **Apollo**  
   - **Lead Name, Company, Email, Phone** left blank for auto‑population.  
17. **Do you see the Apollo Lead template?** If not, reopen the template section and create a new one.  

18. **Integrate Apollo.io with Notion via Zapier**:  
   - Open a new tab and go to `https://zapier.com/app/editor`.  
   - Click **Make a Zap**.  
   - For the **Trigger** app, search for **Apollo.io**, select **New Lead**.  
   - Connect your Apollo account using the **Connect an Account** button, follow the OAuth flow, and click **Continue**.  
   - Test the trigger by clicking **Test Trigger**; you should see a sample lead.  
   - For the **Action** app, search for **Notion**, select **Create Database Item**.  
   - Connect your Notion account, choose the **Leads** database, and map the fields:  
     - **Lead Name** → `Name`  
     - **Company** → `Company`  
     - **Email** → `Email`  
     - **Phone** → `Phone`  
     - **Status** → `Status` (set to “New”)  
     - **Source** → `Source` (set to “Apollo”)  
   - Click **Test Action** to confirm a new row appears in Notion.  
   - If the test fails, check that you selected the correct database and that your Notion integration has **Full Access**.  

19. **Activate the Zap** by toggling the switch to **On**.  
20. **Do you see a new lead row automatically added when a lead is captured in Apollo?** If not, wait a few minutes and refresh the Notion table.  

### Expected Output

- A **Leads** table in Notion with all specified columns.  
- New Apollo leads creating rows with **Status = New** and **Source = Apollo** automatically.  
- Filtered view showing only “New” leads.  

### Error Scenario

- **If you see “Error: Notion API limit reached”**  
  - *Cause*: Exceeded the free tier daily API call limit (500 calls).  
  - *Solution*: Upgrade to the Notion Team plan at $8/month for 10 000 calls, or throttle your Zapier schedule to run every 15 minutes instead of every 5.  

### Tool Comparison Table

| Tool | Free Tier | Paid Tier | Primary Use | Cost (USD) |
|------|-----------|-----------|-------------|------------|
| Notion | 1 GB storage, unlimited pages | Team: $8/month per user | Knowledge base & database | $8/user |
| Zapier | 5 Zaps, 100 tasks/month | Starter: $19.99/month | Automate Apollo → Notion | $19.99/month |
| Make.com | 400 operations/month | Starter: $9/month | Alternative automation, cheaper | $9/month |

> **Note**: For solo entrepreneurs, the **Make.com Starter** plan often provides a cheaper alternative to Zapier while still offering Apollo → Notion triggers.

You have now a fully functional, AI‑powered lead tracking dashboard in Notion, automatically fed by Apollo.io. This system

---

## Procedure 10.3: EXECUTE FIRST PAID CLIENT ACQUISITION CAMPAIGN

1. **Open Apollo.io**  
   - Navigate to `https://app.apollo.io/`.  
   - Click **Sign up** (top‑right), enter your email, password, and confirm.  
   - In the confirmation email, click **Activate account**.  
   - You should see the Apollo dashboard with the **“Getting Started”** overlay.  
   > *Do you see the Apollo dashboard? If not, verify the confirmation email and click the activation link again.*

2. **Generate an Apollo API Key**  
   - In the top‑right, click your avatar → **Settings**.  
   - Under **API & Integrations**, click **Create new API key**.  
   - Name it “Notion‑Zapier‑Client” and click **Generate**.  
   - Copy the key to a secure clipboard.  
   - Paste the key into a Notion page titled **Apollo API Key** (plain text).  
   > *Do you see the API key copied? If not, check that the key is displayed and not truncated.*

3. **Create a Notion Database for Leads**  
   - Open `https://www.notion.so/`.  
   - In the sidebar, click **+ New Page** → choose **Table – Full Page**.  
   - Title the table **Client Leads**.  
   - Add the following properties:  
     - **Name** (Title)  
     - **Email** (Email)  
     - **Company** (Text)  
     - **Status** (Select) → options: “Prospect”, “Contacted”, “Qualified”, “Closed‑Won”.  
     - **Apollo List** (Relation) → link to a new database **Apollo Lists**.  
   - Save the page URL; you will need it for Zapier.  
   > *Do you see the “Client Leads” table with all properties? If not, add the missing columns.*

4. **Set up Apollo List “Paid Campaign Prospects”**  
   - In Apollo, click **Lists** → **Create new list**.  
   - Name it **Paid Campaign Prospects** and set visibility to **Private**.  
   - Under **Custom Filter**, choose **Industry** → **Finance**, **Job Title** → **CFO**, **Location** → **United States**.  
   - Click **Save**.  
   - Note the list ID displayed in the URL (e.g., `list/1234567890`).  
   > *Do you see the list ID? If not, confirm the filter is applied and the list is saved.*

5. **Create a Zapier Integration to Push Leads to Notion**  
   - Open `https://zapier.com/`.  
   - Click **Make a Zap**.  
   - **Trigger**: Search for **Apollo.io**, select **New

## Check-In: Module 10 Complete

- [ ] Launch Your Apollo.io Lead Generation Pipeline completed and verified
- [ ] Configure Your Notion Lead Tracking Dashboard completed and verified
- [ ] EXECUTE FIRST PAID CLIENT ACQUISITION CAMPAIGN completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# APPENDIX A: COMPLETE TOOL REFERENCE

| Tool | Purpose | Free Tier | Paid Tier | When to Upgrade |
|------|---------|-----------|-----------|------------------|
| Make.com | Automation | 1,000 ops/mo | $9/mo | 10,000+ ops/mo |
| ChatGPT | AI Assistant | Free | $20/mo | API integration |
| Notion | Workspace | Free | $8/mo | Team collaboration |
| Canva | Design | Free | $13/mo | Brand kit needed |
| Apollo.io | Sales Intel | Free | $49/mo | 100+ leads/mo |
| Hostinger | Hosting | $1.99/mo | $3.95/mo | Custom domain needed |
| Klaviyo | Email Marketing | 250 contacts | $20/mo | 500+ contacts |
| Shopify | E-commerce | 3-day trial | $29/mo | Product sales |
| Replit | Cloud IDE | Free | $7/mo | Private repos |
| Vapi | Voice AI | 5 calls/mo | $15/mo | Production use |


# APPENDIX B: THE COMPLETE SOP INDEX

This index is the master reference that the entire playbook hinges upon. Every SOP (Standard Operating Procedure) is catalogued here with its unique identifier, a concise title, the functional category it belongs to, the relative difficulty level, and the estimated time required to complete it. Use this table to locate the exact procedure you need, verify that you have the right skill set, and schedule your workday accordingly. Do not skip the “Estimated Time” column; it is the only metric that guarantees you will finish each task within the projected window and keep the overall pipeline moving at a sustainable pace.

| SOP # | Procedure | Category | Difficulty | Est. Time |
|-------|-----------|----------|------------|-----------|
| 1.1 | Set Up Apollo.io Account for Lead Management | Setup | Easy | 20 min |
| 1.2 | Configure Notion Workspace for Lead Tracking | Setup | Easy | 15 min |
| 2.1 | Configure Apollo.io API Keys and Integrations | Integration | Medium | 25 min |
| 2.2 | Set Up Notion Database for Lead Tracking | Database | Medium | 30 min |
| 2.3 | Create Zapier Workflow to Sync Apollo and Notion | Automation | Medium | 45 min |
| 3.1 | Create a Service Delivery Framework in Apollo.io | Framework | Hard | 1 hr |
| 3.2 | Build a Client Onboarding Flow Map in Notion | Framework | Medium | 50 min |
| 4.1 | Integrate Apollo.io Lead Data into a Notion Database | Data Sync | Medium | 35 min |
| 4.2 | Automate Email Outreach Campaigns Using Apollo.io and Notion | Outreach | Hard | 1 hr 15 min |
| 4.3 | Create a Notion Dashboard for Real‑Time Lead Generation Metrics | Dashboard | Medium | 40 min |
| 5.1 | Set Up Apollo.io Lead Scoring for Target Accounts | Lead Scoring | Hard | 1 hr |
| 5.2 | Automate Outreach Sequences with Apollo.io and Notion Workflow | Outreach | Hard | 1 hr 10 min |
| 5.3 | Build a Notion Dashboard to Track Lead Conversion Metrics | Dashboard | Medium | 45 min |
| 6.1 | Set Up Quality Checkpoints for Lead Generation Pipelines | Quality Assurance | Medium | 1 hr |
| 6.2 | Craft Automated Client Communication Templates with Apollo.io | Templates | Medium | 55 min |
| 7.1 | Hire Your First Lead Outreach Contractor via Upwork | Talent Acquisition | Medium | 1 hr 5 min |
| 7.2 | Create SOPs for Delegating Apollo.io Lead Scoring | Delegation | Hard | 1 hr 20 min |
| 7.3 | Analyze Profit Margins of Your Lead Generation Pipelines | Finance | Hard | 1 hr 15 min |
| 8.1 | Create Premium Lead Qualification Bundles for Apollo.io Campaigns | Productization | Hard | 1 hr 30 min |
| 8.2 | Build Subscription‑Based Lead Nurture Workflows in Notion | Subscription | Medium | 1 hr 10 min |
| 9.1 | Set Up Your AI Lead Generation Revenue Dashboard in Notion | Finance | Medium | 45 min |
| 9.2 | Draft Automated Pricing Increase Proposal Templates with Apollo.io | Proposal | Medium | 40 min |
| 10.1 | Launch Your Apollo.io Lead Generation Pipeline | Launch | Hard | 1 hr 25 min |
| 10.2 | Configure Your Notion Lead Tracking Dashboard | Dashboard | Medium | 50 min |
| 10.3 | Execute First Paid Client Acquisition Campaign | Campaign | Hard | 1 hr 30 min |

**Key Usage Instructions**

1. **Locate the SOP** – Enter the SOP # into the playbook search bar or cross‑reference the table to find the exact procedure you must execute.
2. **Assess Difficulty** – Use the difficulty rating to determine

# APPENDIX C: THE REVENUE CALCULATOR  

## 1. Purpose  
This appendix supplies a turnkey, **exact** operating system for forecasting cash flow, sizing pricing tiers, and determining the break‑even point for your AI‑powered lead‑generation business built on Apollo.io and Notion.  Follow every command verbatim; deviations will produce inaccurate numbers and wasted time.

---

## 2. Tool Stack & Pricing (Real, Current Prices)  

| Tool | Plan | Monthly Cost | Free Tier | Notes |
|------|------|--------------|-----------|-------|
| **Apollo.io** | Standard | **$99** | 1,000 contacts | Unlimited email sends |
| **Notion** | Personal Pro | **$8** | Unlimited pages | Unlimited databases |
| **Zapier** | Starter | **$19.99** | 100 tasks | 5‑step Zaps |
| **Make.com** | Basic | **$9** | 1,000 operations | Unlimited app connectors |
| [**Replit**](https://replit.com/refer/egwuokwor) | Hacker | **$7** | 500 MB storage | Unlimited repls |
| **ChatGPT** | Plus | **$20** | 3 k tokens/day | 100k token/month |
| [**ElevenLabs**](https://elevenlabs.io/) | Starter | **$15** | 5 k characters | Text‑to‑speech |
| **Klaviyo** | Starter | **$20** | 250 contacts | Email automation |
| **ActiveCampaign** | Lite | **$29** | 500 contacts | CRM + email |
| [**Semrush**](https://www.semrush.com/) | Pro | **$119.95** | 7,500 keywords | SEO research |
| **Hostinger** | Premium | **$2.95** | 1 GB | Web hosting |
| **Shopify** | Basic | **$29** | 100 products | E‑commerce storefront |
| **PhantomBuster** | Basic | **$39** | 20,000 calls | Web scraping |
| **Buffer** | Pro | **$15** | 3 accounts | Social scheduler |
| **Loom** | Pro | **$12** | 5 GB | Video messaging |
| **Calendly** | Pro | **$10** | 1 calendar | Scheduling |
| [**Beehiiv**](https://beehiiv.com/) | Starter | **$10** | 1,000 subscribers | Newsletter |
| **Midjourney** | Basic | **$10** | 200 GPU hours | AI art |
| **Grammarly** | Premium | **$12** | 3,000 words/day | Writing assistant |

> **Command:** Keep a running ledger of tool costs in a Notion table titled “Tool Costs.”  Populate each row with *Tool*, *Plan*, *Monthly Cost*, and *Annual Cost* (Monthly Cost × 12).  
> **Check‑in:** Do you see a table with 18 rows and 4 columns? If not, create a new database and add those columns.  

---

## 3. Building the Revenue Calculator in Notion  

### 3.1 Create the “Revenue Calculator” Database  

1. Open Notion → Click **+ New Page** → Name it **Revenue Calculator**.  
2. Select **Table – Full Page**.  
3. Add the following columns (exact names):  
   - **Month** (Number)  
   - **Clients** (Number)  
   - **Revenue** (Number, Currency)  
   - **Expenses** (Number, Currency)  
   - **Profit** (Formula)  
   - **Cumulative Profit** (Formula)  

> **Check‑in:** Do you see a table with 6 columns? If not, rename the default “Name” column to “Month” and add the others.  

### 3.2 Input Base Variables  

Create a separate **Settings** page (linked to the database) to store constants:

| Field | Type | Value | Explanation |
|-------|------|-------|-------------|
| **Base Clients per Month** | Number | 5 | Average new clients in Month 1 |
| **Client Growth % (Month‑to‑Month)** | Number | 50 | 50 % growth each subsequent month |
| **Base Revenue per Client** | Number | $2,500 | Average paid package |
| **Fixed Monthly Expense** | Number | $1,200 | Rent, utilities, subscriptions

For the free step-by-step guide, see our [implementation guide]({< ref "/intelligence/build-an-ai-social-media-management-tool-with-chatgpt-the-complete-step-by-step-.md" >}).


## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Notion](https://notion.so/)** — All-in-one workspace — notes, docs, project management
- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
