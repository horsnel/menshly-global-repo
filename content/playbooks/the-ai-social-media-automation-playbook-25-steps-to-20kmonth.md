---
title: "The AI Social Media Automation Playbook: 25 Steps to $20K/Month"
date: 2026-10-03
category: "Playbook"
price: "₦25,000"
readTime: "88 MIN"
excerpt: "The AI Social Media Automation Playbook: 25 Steps to $20K/Month This is an OPERATING SYSTEM, not a blog post or a loose guide. You will follow 25 procedures organized into 10 modules that together demand 12+ hours of focused reading and execution. By..."
image: "/images/articles/playbooks/the-ai-social-media-automation-playbook-25-steps-to-20kmonth.png"
heroImage: "/images/heroes/playbooks/design-build-and-automate-ai-social-media-workflows-with-makecom-and-buffer.png"
relatedOpportunity: "/opportunities/how-to-build-an-ai-social-media-management-agency-5k-5kmonth/"
relatedGuide: "/intelligence/build-an-automate-streamline-and-scale-ngo-operations-with-makecom-with-chatgpt-/"
---
**The AI Social Media Automation Playbook: 25 Steps to $20K/Month**  
This is an OPERATING SYSTEM, not a blog post or a loose guide. You will follow **25 procedures** organized into **10 modules** that together demand 12+ hours of focused reading and execution. By completing every step, you will master the art of designing, building, and automating AI‑driven social media workflows with Make.com and Buffer, enabling you to charge clients a predictable monthly retainer and scale that retainer to $20,000/month. This playbook extends our free implementation guide with complete procedures, SOPs, and revenue calculators, giving you a turnkey framework that transforms ideas into cash‑flow. The system covers every nuance—from sourcing AI content with Midjourney, generating captions via ChatGPT, converting them to videos with [Fliki AI](https://fliki.ai?referral=noah-wilson-w84be4), to scheduling, monitoring, and reporting through Buffer—all wired together in Make.com. Each module ends with a revenue calculator that shows you the exact profit margin you can expect, ensuring you never guess your earnings. For the free step‑by‑step guide, see our [implementation guide]({< ref "/intelligence/build-an-automate-streamline-and-scale-ngo-operations-with-makecom-with-chatgpt-.md" >}).

---

# MODULE 1: FOUNDATION

## Overview

In this foundational module you will establish the digital backbone that powers every AI‑driven social media workflow you will later automate with Make.com and Buffer. You will create and verify your business accounts, claim a custom domain, set up a professional email address, and install the core productivity tools that keep everything running smoothly. Skipping any of these steps will cripple your ability to authenticate API calls, store and share content, and deliver consistent branding to your clients. Without a verified domain and a professional email, clients will see you as untrustworthy; without a proper API connection, your automations will fail and your inbox will be clogged with error messages.

The procedures in this module are the building blocks for all subsequent modules. They provide the data pipelines, secure credentials, and shared workspaces that Make.com and Buffer rely on. If you rush through them or leave any credential out of place, every script you later write will break at runtime, leading to lost client trust and wasted time debugging root causes that were preventable.  

Below is a quick reference of every tool you will need in this phase, what it does, and the cost of its free and paid tiers.

| Tool          | Purpose                                      | Free Tier (per month)            | Paid Tier (per month)                 |
|---------------|----------------------------------------------|----------------------------------|---------------------------------------|
| [**Make.com**](https://www.make.com/en/register?pc=menshly)  | Visual automation platform, API orchestration| 1 000 operations, 100 MB data    | 5 000 operations, $29.00 (Starter)    |
| **Buffer**    | Social‑media scheduling & analytics          | 3 social accounts, 10 posts queued| 3 accounts, 100 posts queued, $12.00 |
| **Gmail (Google Workspace)** | Professional email, calendar | 15 GB storage, free            | 30 GB per user, $6.00 (Business Starter) |
| [**Notion**](https://notion.so/)    | Project docs, SOPs, shared knowledge base  | Unlimited pages, 5 MB file limit | Unlimited, $8.00 per user (Personal Pro) |
| [**Canva**](https://www.canva.com/)     | Graphic assets for posts, thumbnails        | 5 GB storage, limited templates | Unlimited storage, $12.95 per user (Pro) |
| **Hostinger** | Domain registration & email hosting         | N/A                             | Domain: $10.99/year; Email: $1.99/month |

**Estimated time to complete:** 2 – 3 hours.

---

## Procedure 1.1: Register Business Email in Google Workspace

This procedure will walk you through creating an official business email address (e.g., **contact@yourbrand.com**) using Google Workspace. Follow each step exactly. After every 4–5 steps, we’ll pause for a quick check‑in.

---

### 1. Go to the Google Workspace site  
- Open your browser and navigate to **https://workspace.google.com/**.  
- Click the **bold** button **“Try for free”**.

> **Expected output**: A new tab opens to the “Get Started” wizard for a 14‑day free trial.

### 2. Enter your domain name  
- In the field **“Domain (the domain you own)”**, type **yourbrand.com**.  
- Click **“Continue”** (button **bold**).

> **Expected output**: The wizard verifies the domain and asks you to proceed to “Verify ownership”.

### 3. Verify domain ownership  
- Google will present a TXT record string.  
- Copy the entire TXT record value.  
- **If you own the domain with Hostinger**:  
  1. Log in to **https://www.hostinger.com**.  
  2. Go to **“Domains”** → **“DNS Zone Editor”**.  
  3. Choose your domain.  
  4. Click **“Add Record”** → select **TXT**.  
  5. Paste the copied TXT value into the **“Value”** field.  
  6. Click **“Save”** (button **bold**).  

> **Check‑in**: Do you see the TXT record listed under your domain’s DNS records? If not, refresh the DNS page and wait 5 minutes before continuing.

### 4. Return to Google Workspace wizard  
- Once the TXT record is saved, go back to the Google Workspace tab.  
- Click **“Verify”** (button **bold**).  
- If verification succeeds, click **“Next”** (button **bold**).  

> **Expected output**: A green checkmark “Domain verified” appears.

---

### 5. Create an admin account  
- In the field **“Admin email”**, type **admin@yourbrand.com**.  
- In **“Password”**, enter a strong password (e.g., **StrongPass!2026**).  
- Re‑enter the password in **“Confirm password”**.  
- Click **“Continue”** (button **bold**).  

> **Expected output**: A screen confirming “You’ve created an admin account”.

### 6. Add at least one user (yourself)  
- In **“User name”**, type **yourname**.  
- **“First name”**: Your first name.  
- **“Last name”**: Your last name.  
- **“User email”**: Should auto‑populate as **yourname@yourbrand.com**.  
- **“Password”**: Use the same password as admin or a new one.  
- Click **“Create user”** (button **bold**).  

> **Expected output**: “User created” toast notification.

### 7. Review plan details  
- You’ll be taken to the plan comparison page.  
- Select **Business Standard** ($12/user/month).  
- Click **“Continue”** (button **bold**).  

> **Check‑in**: Do you see the plan details with the 14‑day free trial highlighted? If not, scroll down to the “Business Standard” card and click the **bold** button “Try free”.

### 8. Enter billing information  
- Click **“Add billing account”** (button **bold**).  
- Enter your credit card details.  
- Click **“Continue”** (button **bold**).  

> **Expected output**: “Billing verified” confirmation.  

### 9. Finish setup  
- Click **“

---

## Procedure 1.2: Create Buffer Workspace for Social Media

1. Open your web browser and navigate to **https://buffer.com**.  
   *Expected result:* Buffer homepage with prominent “**Get Started**” button.

2. Click the **bold** button **“Get Started”** in the top‑right corner.  
   *Result:* You are taken to the “Create an account” page.

3. On the account creation form, fill in the following fields:  
   - **Email address:** *your‑email@example.com*  
   - **Password:** *StrongPass!123* (at least 12 characters, mix of upper/lowercase, numbers, and symbols)  
   - **Confirm password:** *StrongPass!123*  
   Click the **bold** button **“Create free Buffer account”**.  
   *Check‑in:* Do you see a confirmation email in your inbox? If not, verify the spam folder or click **“Resend email”**.

4. Open the confirmation email, click the verification link, and you will be redirected to **https://buffer.com/dashboard**.  
   *Result:* Dashboard home with a greeting “**Welcome to Buffer**”.

5. In the top navigation bar, click the **bold** button **“Create a new Workspace”**.  
   *Result:* Modal window titled “Create a new Workspace”.

6. In the modal, enter the following:  
   - **Workspace name:** *YourBusiness Social*  
   - **Workspace URL slug:** *yourbusinesssocial* (no spaces, only lowercase letters and dashes)  
   Click the **bold** button **“Create Workspace”**.  
   *Check‑in:* Do you see the new workspace listed under “Your Workspaces” on the left sidebar? If not, refresh the page.

7. Return to the left sidebar, click the newly created workspace name **“YourBusiness Social”**.  
   *Result:* Dashboard specific to this workspace.

8. In the workspace dashboard, locate the **“Add Social Accounts”** button in the upper‑center area and click it (bold).  
   *Result:* Social account selection screen.

9. Choose **“Twitter”** by clicking the **bold** button **“Connect”** next to it.  
   *Check‑in:* Do you see a pop‑up window asking to authorize Buffer? If not, click **“Refresh”** on the browser.

10. In the Twitter authorization pop‑up, log in with your Twitter credentials and click **bold** “Authorize app”.  
    *Result:* Return to Buffer with a success banner: “**Twitter account added**”.

11. Repeat steps 8‑10 for **“LinkedIn”** and **“Instagram”** (use the same authorization flow).  
    *Check‑in:* Are all three accounts listed under “Social Accounts” in the workspace sidebar? If any are missing, revisit the respective authorization steps.

12. Navigate to the **“Content”** tab at the top of the workspace dashboard.  
    *Result:* Blank content calendar view.

13. Click the **bold** button **“Add a Post”** in the top‑right corner.  
    *Result:* New post editor opens.

14. In the post editor, fill in the following fields:  
    - **Post text:** *“Welcome to our new AI‑powered social media hub. Stay tuned for updates!”*  
    - **Post date/time:** *Today, 10:00 AM* (use the calendar picker)  
    - **Social accounts:** Tick **Twitter**, **LinkedIn**, **Instagram**.  
    Click the **bold** button **“Schedule Post”**.  
    *Check‑in:* Do you see the post appear on the calendar with a green checkmark? If not, ensure the date/time is correct.

15. Return to the **“Analytics”** tab.  
    *Result:* Dashboard shows engagement metrics (impressions, clicks, etc.).

16. Open a new browser tab and go to **https://make.com**.  
    *Result:* Make.com login page.

17. Click **bold** “**Sign up**” and register with the same email address used for Buffer.  
    *Check‑in:* Do you receive a verification email? If not, click **“Resend”**.

18. After email verification, you are directed to the Make.com dashboard.  
    *Result:* Workspace overview with “**Create a new scenario**” button.

19. Click **bold** “Create a new scenario” and choose **“Buffer”** from the list of apps.  
    *Result:* Scenario editor with a blank canvas.

20. Drag the **“Buffer – Create a Post”** module onto the canvas.  
    Configure it:  
    - **Workspace URL:** `https://yourbusinesssocial.buffer.com`  
    - **Post text:** *Use the same text as step 14*  
    - **Schedule time:** *Today, 10:00 AM*  
    - **Social accounts:** *Twitter, LinkedIn, Instagram*  
    Click **bold** “Save” and then **“Run once”**.  
    *Expected output:* JSON response in the console that includes `"status":"success"`.  
    *Error scenario:* If you see `"error":"Invalid workspace URL"`, double‑check the URL slug; it must exactly match the one displayed in Buffer’s dashboard.

**Table 1 – Cost Comparison for Buffer and Make.com (Free Tier)**

| Tool        | Free Tier Limits                                   | Paid Tier (Monthly) | Price |
|-------------|-----------------------------------------------------|---------------------|-------|
| Buffer      | 3 social accounts, 10 scheduled posts per month     | Pro: 15 social accounts, 100 scheduled posts | $6.00 |
| Make.com    | 100 tasks per month, 1,000 executions

---

## Procedure 1.3: Set Up Make.com Scenario to Sync Buffer with Google Sheets

1. **Open your web browser** and navigate to **https://www.make.com**.  
2. Click the **“Sign Up”** button in the top‑right corner.  
3. In the **Sign‑Up form**, enter your **email** (e.g., `you@yourdomain.com`) and a **secure password**. Click **“Create account”** in bold.  
4. **Do you see a verification email** in your inbox? If not, check your spam folder and click the **“Resend email”** link on the Make.com page.  
   *Expected output:* A “Verification email sent” banner appears.  
5. Open the email, click the **“Verify email address”** button. You’ll be redirected to **https://www.make.com/dashboard**.  
6. On the dashboard, click the **“Create a new Scenario”** button in bold.  
7. In the scenario editor, click the **“+ Add another module”** icon (the plus sign).  
8. In the module picker, type **“Buffer”** into the search bar. Hover over **“Buffer > Get all posts”** and click **“Add”** in bold.  
9. **Do you see a prompt to connect Buffer?** If not, click the **“Add connection”** button in the Buffer module panel.  
10. A new window titled **“Connect Buffer”** opens. Click **“Authorize”** in bold.  
    *Expected output:* Buffer’s OAuth consent screen with scopes `read` and `write` highlighted.  
11. Log in to Buffer with your Buffer credentials (`yourbufferemail@domain.com`). Click **“Allow”**.  
12. Return to Make.com. The Buffer module now shows **“Connection: yourbufferemail@domain.com”**.  
13. **Do you see the Buffer module populated with your social accounts?** If not, refresh the page after a minute.  
    *Error scenario:* If you see **“Error: OAuth 2.0 authentication failed”**, it means the token expired. Fix it by repeating steps 10‑12.  
14. Click the **“+ Add another module”** icon again. Search for **“Google Sheets”** and select **“Google Sheets > Add a row”**.  
15. In the Google Sheets module, click **“Add connection”**.  
16. A new window titled **“Connect Google Sheets”** appears. Click **“Authorize”** in bold.  
17. Log in to your Google account (`you@google.com`). Click **“Allow”** to grant Make.com access to your spreadsheets.  
18. Return to Make.com. In the Google Sheets module, click the **“Spreadsheet”** dropdown and select **“New Sheet – Social_Media_Posts”** (or create a new sheet by clicking **“Create new spreadsheet”**).  
19. Click the **“Sheet”** dropdown and choose **“Sheet1”**.  
20. Map the Buffer fields to Google Sheets columns:  
    - In the **“Title”** field, click **“Map”** and choose **“Post title”** from Buffer.  
    - In **“Content”**, map to **“Post content”**.  
    - In **“Post URL”**, map to **“Post URL”**.  
    - In **“Scheduled At”**, map to **“Scheduled at”**.  
21. Click the **“Save”** button at the top right of the scenario editor.  
22. Click the **“Run once”** button in bold to test the flow.  
23. **Do you see a green “Success” banner** and a new row inserted into your Google Sheet? If not, check the error panel on the right for any mapping issues.  
    *Expected output:* A row appears in `Sheet1` with columns: Title, Content, Post URL, Scheduled At.  
24. Click the **“Enable scenario”** toggle (turn from gray to green).  
25. Your scenario will now run automatically whenever a new post is scheduled in Buffer.  

### Tool Pricing & Free Tier Limits

| Tool | Free Tier | Paid Tier | Key Limits (Free) | Key Limits (Paid) |
|------|-----------|-----------|-------------------|-------------------|
| Make.com | 1,000 operations/month, 100 MB data, 1 scenario | 3,000 ops/month, 200 MB, 3 scenarios (Starter) | 1,000 ops, 1 scenario | 3,000 ops, 3 scenarios |
| Buffer | 3 social accounts, 10 scheduled posts/account | Unlimited accounts, 100 scheduled posts/account (Pro) | 3 accounts, 10 posts | Unlimited |

> **Tip:** Buffer’s free tier allows 10 scheduled posts per account; if you need more, upgrade to Buffer Pro at $15/month per account.

### Error Handling

- **Error:** *“Error: Buffer module: No posts found”*  
  **Cause:** No posts scheduled in Buffer at the time of test.  
  **Fix:** Schedule a test post in Buffer and re‑run step 22.

- **Error:** *“Error: Google Sheets module: Spreadsheet not found”*  
 

## Check-In: Module 1 Complete

- [ ] Register Business Email in Google Workspace completed and verified
- [ ] Create Buffer Workspace for Social Media completed and verified
- [ ] Set Up Make.com Scenario to Sync Buffer with Google Sheets completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 2: TECH STACK

## Overview  

In this module you will construct the digital backbone that powers every AI‑driven social media workflow you’ll sell. The focus is on two critical engines: **Make.com** for orchestration and **Buffer** for publishing. Together, they allow you to pull data from APIs, run inference models, and push content to multiple platforms with zero manual touch. If you skip this module, your entire automation strategy will collapse—your clients will see broken pipelines, delayed posts, and a complete loss of trust in your service.

You’ll learn to:

1. Generate and secure API keys for every service.  
2. Create Make.com scenarios that pull content from a content‑generation API (ChatGPT or [Replit](https://replit.com/refer/egwuokwor)) and route it to Buffer.  
3. Validate the data flow by inspecting the “Scenario run history” and Buffer’s “Content Planner” to ensure posts appear exactly as scheduled.  

Additionally, you’ll be introduced to a lightweight debugging toolkit that catches token‑limit issues and rate‑limit throttling before they break your production runs.

| Tool        | Purpose                                      | Free Tier                                 | Paid Tier                           |
|-------------|----------------------------------------------|-------------------------------------------|-------------------------------------|
| Make.com    | Workflow orchestration, API integration      | 1,000 operations/month, 5 scenarios        | $49/month (Starter) – 30,000 ops    |
| Buffer      | Social media publishing and scheduling       | 3 social accounts, 10 posts/month          | $15/month (Essentials) – unlimited  |
| ChatGPT     | AI content generation                        | 3,000 tokens/day (ChatGPT‑Free)           | $20/month (ChatGPT‑Plus) – 1M tokens/day |
| Replit      | Quick coding sandbox for custom scripts      | Unlimited public projects, 500 MB RAM      | $7/month (Hacker) – 10 GB RAM       |

**Estimated time to complete:** 2 hours 30 minutes, including key‑generation, scenario building, and validation steps.

---

## Procedure 2.1: CONNECT ChatGPT API AND STORE KEYS IN NOTION

1. **Open the OpenAI API portal**  
   - Navigate to **https://platform.openai.com/account/api-keys**.  
   - Log in with your OpenAI credentials (or create an account if you do not have one).  

2. **Create a new API key**  
   - Click the **bold “Create new secret key”** button.  
   - In the pop‑up, name the key **“ChatGPT‑Prod‑Key”**.  
   - Click **“Create key”**.  
   - Copy the generated key to your clipboard.  

3. **Open Notion**  
   - Go to **https://www.notion.so** and log in.  
   - In the left sidebar, click the **bold “+ New Page”** button.  

4. **Create a dedicated database for API keys**  
   - In the new page, type **“API Keys”** and press **Enter**.  
   - Click the **bold “+ Add a view”** button, name it **“Table”**, and click **“Create”**.  

5. **Add required properties**  
   - Click the **bold “+ Add a property”** button.  
   - Choose **“Title”** and rename it to **“Service”**.  
   - Add a **“Text”** property named **“API Key”**.  
   - Add a **“Date”** property named **“Created”**.  

**Do you see the “API Keys” table with three columns (Service, API Key, Created)? If not, make sure you are in Table view and that you added the properties correctly.**

6. **Insert the ChatGPT key**  
   - Click **“New”** at the top right of the table.  
   - In the **Service** column, type **“ChatGPT”**.  
   - In the **API Key** column, paste the key you copied earlier.  
   - Leave the **Created** column blank (Notion will auto‑populate it).  

7. **Secure the key**  
   - Click the three dots **(•••)** in the top right of the page and choose **“Share”**.  
   - Toggle **“Share to the web”** **off** to keep the page private.  
   - In the same menu, click **“Copy link”** and store it somewhere safe (e.g., a password manager).  

8. **Set up Make.com to read the key**  
   - Open a new tab and go to **https://www.make.com**.  
   - Log in or sign up.  
   - Click the **bold “Create a new scenario”** button.  

9. **Add Notion module**  
   - In the scenario builder, click the **bold “+ Add another module”** button.  
   - Search for **“Notion”** and select **“Search database”**.  
   - Click **“Add”**.  

10. **Connect your Notion account**  
    - When prompted, click **“Add a connection”**.  
    - In the pop‑up, click **“Authorize”**.  
    - Copy the **integration key** from Notion’s integration settings (found under **https://www.notion.so/my-integrations**).  
    - Paste it into the Make.com field and click **“Test & Continue”**.  

**Do you see the Notion module connected and the “Search database” ready? If not, verify that the integration key was copied correctly and that the database ID is correct.**

11. **Configure the search**  
    - In the Notion module settings, set **Database ID** to the ID found in your Notion URL (e.g., `https://www.notion.so/YourWorkspace/xxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`).  
    - In the **Filter** field, add:  
      ```
      Service = "ChatGPT"
      ```  

12. **Add a “Set variable” module**  
    - Click **“+ Add another module”** → search **“Set variable”** → select **“Set variable”** → click **“Add”**.  
    - Set **Name** to **“CHATGPT_KEY”**.  
    - In **Value**, click **“Insert a variable”** → choose **“Notion → Result → Items → 0 → API Key”**.  

13. **Export the variable to a JSON file** (optional for debugging)  
    - Add a **“HTTP”** module → choose **“Make a request”**.  
    - Configure:  
      - **Method**: `POST`  
      - **URL**: `https://api.jsonstorage.net/v1/json`  
      - **Headers**: `Content-Type: application/json`  
      - **Body type**: `Raw`  
      - **Body**:  
        ```json
        {
          "api

---

## Procedure 2.2: Build Your First Make.com Automation Scenario  

1. **Open a browser and navigate to** `https://www.make.com`.  
2. **Click the button** **“Log In”** in the top‑right corner.  
3. **Enter your email** `you@example.com` and **password** `YourStrongPassword1!`.  
4. **Click** **“Sign In”**.  

> **Do you see the Make.com dashboard with the “Create a new scenario” button?**  
> If not, refresh the page and **click** **“Retry”** at the bottom of the screen.  

5. **Click** **“Create a new scenario”** (green button).  
6. In the modal, **type** `Social Media Content Scheduler` into the **“Scenario name”** field.  
7. **Click** **“Create”**.  
8. You are now on the scenario editor canvas.  

> **Do you see the blank canvas with the plus (+) icon in the center?**  
> If not, click the **“New scenario”** icon in the top‑left corner again.  

9. **Search for “Buffer”** in the **“Choose a service”** search bar and **click** the **Buffer** icon.  
10. **Select** the **“Add a new module”** button (blue button).  
11. Choose **“Buffer > Create a new post”** from the list.  
12. **Click** **“Add connection”**.  
13. In the pop‑up, **enter** your Buffer API key (obtain it from `https://buffer.com/settings/api`).  
14. **Click** **“Confirm credentials”**.  

> **Do you see the Buffer module with the “Post to profile” field?**  
> If not, double‑check that the API key is correct and **re‑click** **“Confirm credentials”**.  

15. **Drag a “HTTP” module** from the left panel and place it to the left of the Buffer module.  
16. **Configure the HTTP module**:  
   - **Method**: `GET`  
   - **URL**: `https://api.pexels.com/v1/search?query=summer+beach&per_page=1`  
   - **Headers**: `Authorization: YOUR_PEXELS_API_KEY` (replace with your key).  
17. **Click** **“Save”** in the HTTP module, then **click** **“Save”** again in the Buffer module.  

> **Do you see the two modules connected via arrows?**  
> If not, drag the small blue node from the HTTP module’s right side to the Buffer module’s left side.  

18. **Map the Buffer module fields**:  
   - **Content** → `{{HTTP.Response.body.photos[0].alt}}`  
   - **Media URL** → `{{HTTP.Response.body.photos[0].url}}`  
   - **Profile** → `Your Business Profile ID` (found in your Buffer dashboard).  

19. **Click** **“Add a schedule”** in the top toolbar.  
20. Set the schedule to **“Every day at 10:00 AM (UTC)”**.  
21. **Click** **“Save”** at the top right to lock the scenario.  

22. **Run the scenario once** by clicking the **“Run once”** button (orange button).  
23. In the execution history, **check the status**: it should read **“Success”**.  
24. **Hover over the HTTP module**; the execution log should show a 200 status and a JSON body with a photo.  
25. **Confirm the post** appears in your Buffer queue at the scheduled time.  

### Error Scenario  
- **If you see “Error: 401 Unauthorized” when running the HTTP module**, this means the Pexels API key is missing or invalid.  
  - **Fix it by**:  
    1. Go to `https://api.pexels.com` and regenerate a new key.  
    2. Update the **Headers** field in the HTTP module with the new key.  
    3. **Run** the scenario again.  

### Cost Breakdown Table  

| Tool | Free Tier Limits | Paid Tier (Monthly) | Notes |
|------|------------------|---------------------|-------|
| Make.com | 1,000 operations/month, 5 scenarios | Starter: $29.99 (10,000 ops) | Buffer API usage included in free tier |
| Buffer | 3 social profiles, 10 posts/month | Pro: $15/month (5 profiles, 100 posts) | API key requires Pro plan |
| Pexels API | 1,200 requests/month | Unlimited (free) | No subscription needed |

### Expected Final Output  
- A Make.com scenario named **“Social Media Content Scheduler”** that pulls a random beach photo from Pexels and posts it to your Buffer profile every day at 10:00 AM UTC.  
- The scenario execution log shows **“Success”** with a 200 HTTP status and a JSON payload containing the photo details.  
- Buffer queue reflects the scheduled post with the correct image and caption.  

You have now built a fully automated AI social media workflow using Make.com and Buffer. Execute this scenario daily to deliver fresh, AI‑generated content to your clients’ social channels.

---

## Procedure 2.3: Configure Vapi Voice Agent and ElevenLabs TTS

1. **Open a web browser and navigate to Vapi’s signup page**  
   URL: `https://www.vapi.ai/signup`  
   Click the **Sign Up** button in the top‑right corner.  
   *Expected output:* A registration form with fields for Email, Password, and Confirm Password.  

2. **Fill out the Vapi registration form**  
   - Email: `yourname@example.com`  
   - Password: `YourStrongPassword123` (must be at least 12 characters, include one number and one symbol)  
   - Confirm Password: same as above.  
   Click **Create Account** (in bold).  
   *Expected output:* A success banner “Account created! Check your inbox for a verification email.”  

3. **Verify your email**  
   Open your email client, locate the message from Vapi, and click the **Verify Email** link.  
   *Expected output:* Browser redirects to `https://www.vapi.ai/dashboard`.  

4. **Navigate to the API Keys section**  
   In the dashboard left‑hand menu, click **Settings** → **API Keys**.  
   *Check‑in:* Do you see the **API Keys** page with a table of keys? If not, refresh the page or return to the dashboard and retry.  

5. **Create a new API key for the Voice Agent**  
   Click the **Generate API Key** button (bold).  
   - Key Name: `VoiceAgentKey`  
   - Select **Read & Write** permissions.  
   Click **Create**.  
   *Expected output:* A modal displays your new key. Copy it to your clipboard.  

6. **Store the Vapi API key securely**  
   Open Notion (URL: `https://www.notion.so/`).  
   - Create a new page titled [**Vapi Keys**](https://vapi.ai/).  
   - Add a database table with columns: `Key Name`, `API Key`, `Created On`.  
   Paste the key into the `API Key` cell.  
   *Check‑in:* Do you see the key stored in Notion? If not, ensure the database is visible and you’re logged in.  

7. **Open ElevenLabs’ beta portal**  
   URL: `https://www.elevenlabs.io/beta`  
   Click **Log In** (top‑right).  
   If you have no account, click **Sign Up** and use the same email as Vapi.  

8. **Generate an ElevenLabs API key**  
   After logging in, click your profile icon → **API Keys**.  
   Click **Generate Key** (bold).  
   - Key Name: `ElevenLabsTTSKey`  
   - Permissions: Default (Read & Write).  
   Click **Create**.  
   *Expected output:* A pop‑up shows your key. Copy it to clipboard.  

9. **Store the ElevenLabs API key**  
   In the same Notion page **Vapi Keys**, add a new row:  
   - Key Name: `ElevenLabsTTSKey`  
   - API Key: paste the key.  
   *Check‑in:* Do you see both keys in the same table? If not, confirm you’re editing the correct Notion page.  

10. **Create a Vapi Voice Agent**  
    In the Vapi dashboard, click **Voice Agents** → **Create New Agent**.  
    - Agent Name: `SocialMediaVoiceAgent`  
    - Description: “Automated voice bot for social media captions.”  
    - Language: English (US).  
    Click **Create Agent** (bold).  

11. **Configure the agent’s trigger**  
    On the agent detail page, click **Triggers** → **Add Trigger**.  
    - Trigger Type: **Webhook**  
    - URL: Leave blank for now (we’ll set it in Make.com).  
    - Method: POST.  
    Click **Save**.  
    *Expected output:* A confirmation banner “Trigger added.”  

12. **Set up the agent’s response**  
    In the same agent page, click **Responses** → **Add Response**.  
    - Response Type: **Text to Speech**  
    - TTS Engine: [**ElevenLabs**](https://elevenlabs.io/) (select from dropdown).  
   

## Check-In: Module 2 Complete

- [ ] CONNECT ChatGPT API AND STORE KEYS IN NOTION completed and verified
- [ ] Build Your First Make.com Automation Scenario completed and verified
- [ ] Configure Vapi Voice Agent and ElevenLabs TTS completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 3: FRAMEWORK

## Overview  
In this module we lay the foundation for a repeatable, scalable AI‑social‑media service. We codify the **universal process** that turns raw client intent into a polished, automated posting schedule delivered through Buffer, while Make.com orchestrates the data flow and AI content generation. By defining a clear service‑delivery framework, you eliminate guesswork, set measurable quality standards, and create a blueprint that any junior operator can follow without losing your brand voice or client expectations.  

Skipping this framework means you’ll be improvising every client call, risking inconsistent output, over‑ or under‑promising, and ultimately damaging your reputation. You’ll also miss the opportunity to embed automation early, leading to double‑handling of content and wasted time on manual uploads. In contrast, a solid framework guarantees that each workflow is **repeatable** (any one of your team can roll it out in 30 minutes) and **audit‑ready** (every step is logged in Make.com and visible in Buffer’s analytics).  

Below is the essential toolkit for this module. All tools are listed with their free‑tier limits and the recommended paid tier that unlocks the features needed for a production‑ready service.

| Tool          | Purpose                                         | Free Tier | Paid Tier (Monthly) |
|---------------|-------------------------------------------------|-----------|---------------------|
| Make.com      | Automate content curation, scheduling, and API calls | 2,500 operations / month | 5,000 operations / month – $19.99 |
| Buffer        | Social‑media publishing, analytics, and collaboration | 3 social accounts, 10 scheduled posts | Unlimited posts – $15.00 |
| ChatGPT (OpenAI) | AI‑driven copywriting, tone‑matching, and content ideation | 1000 tokens/day | Unlimited tokens – $20.00 |
| Canva         | Quick visual creation for social posts | 5 templates/month | Unlimited templates – $12.99 |
| Zapier        | Optional secondary connector for non‑Make integrations | 100 tasks/month | 750 tasks/month – $19.99 |

**Estimated time to complete Module 3**: 4 hours (including tool setup, workflow diagram, and quality‑control checklist).

---

## Procedure 3.1: Design Your Service Delivery Framework in Notion

1. **Open Notion**  
   - URL: https://www.notion.so/  
   - Click **LOG IN** in the top‑right corner.  
   - Enter your email and password.  
   - Once logged in, you should see the **Workspace Home** with a sidebar on the left.

2. **Create a New Workspace**  
   - In the sidebar, click **+ NEW WORKSPACE**.  
   - Name it **“AI Social Media Service Framework”** and choose **“Private”**.  
   - Click **CREATE**.  
   - Expected output: A fresh workspace with a blank page titled “Untitled”.

3. **Add a Database Page**  
   - On the new page, type `/table` and select **“Table – Full page”**.  
   - Title the table **“Client Onboarding & Deliverables”**.  
   - The table automatically creates 5 columns: **Name, Channel, Status, Deadline, Notes**.

4. **Customize Columns**  
   - Click the column header **Name** → **Rename** → **Client**.  
   - Click **Channel** → **Rename** → **Social Platform**.  
   - Add a new column: click the **+** icon → choose **Select** → name it **Service Type**.  
   - Add options: *Social Media Management*, *AI‑Generated Content*, *Analytics Reporting*.  
   - Add a new column: click **+** → choose **Date** → name it **Start Date**.  
   - Expected output: Table with five customized columns.

> Do you see the table with the updated columns?  
> If not, refresh the page or re‑open the workspace.  

5. **Create a Template for New Clients**  
   - In the table view, click **+ NEW** → **+ Add a new template**.  
   - Title the template **“Client Setup”**.  
   - Under **Template Content**, add the following pages:  
     - **Scope of Work** (text page)  
     - **Content Calendar** (linked database view of a new calendar table)  
     - **Buffer Integration** (embed link).  
   - Click **SAVE**.  
   - Expected output: A new template button labeled **“Client Setup”**.

6. **Embed Buffer Link**  
   - Open a new tab: https://buffer.com/  
   - Click **LOG IN** → sign in.  
   - Go to **Dashboard** → click **+ New Post** to create a placeholder post.  
   - Copy the URL of the placeholder post.  
   - Return to Notion → open the **Client Setup** template → click **+** → **Embed** → paste the Buffer URL → click **Embed link**.  
   - Expected output: Buffer post link embedded in Notion.

7. **Add Make.com Scenario Link**  
   - Open a new tab: https://www.make.com/  
   - Click **LOG IN** → sign in.  
   - Create a new Scenario: click **+ CREATE** → name it **“Social Media Auto‑Publish”**.  
   - Add the **Buffer** app → choose **“Create Schedule”** → connect your Buffer account.  
   - Add a **Google Sheet** trigger → link to a sheet that will hold your content calendar.  
   - Save the Scenario.  
   - Copy the Scenario URL.  
   - Return to Notion → open the **Client Setup** template → click **+** → **Embed** → paste the Make.com URL → click **Embed link**.  
   - Expected output: Make.com scenario link embedded.

8. **Add a Calendar View**  
   - In the **Client Onboarding & Deliverables** table, click **+ Add a View** → select **Calendar** → name it **“Content Calendar”**.  
   - Set the date property to **Start Date**.  
   - Expected output: A calendar view showing client

---

## Procedure 3.2: Build the Client Onboarding Automation Pipeline

1. **Open a new Make.com project.**  
   - Navigate to **https://www.make.com/en**.  
   - Click the **bold** button **“Create a new scenario”**.  
   - Confirm the pop‑up by clicking **“Create”**.  
   - *Expected output*: A blank scenario canvas and a toast “Scenario created – ID 000123”.

2. **Add a “Webhooks” trigger.**  
   - In the left‑hand menu, type **“Webhooks”** and select **“Make a Webhook”**.  
   - Click **“Add”** → **“Webhook URL”**.  
   - Copy the generated URL; store it in a clipboard‑ready file called **`webhook_url.txt`**.  
   - *Expected output*: A URL like `https://hook.integromat.com/123abc456def`.

3. **Insert a “HTTP” module to capture form data.**  
   - Click the **“+”** icon next to the webhook.  
   - Search for **“HTTP”** → choose **“Make an HTTP request”**.  
   - Set the **Method** to **POST**, **URL** to `https://api.formstack.com/v2/form/1234567/submit`.  
   - In **Headers**, add **`Content-Type: application/json`**.  
   - In **Body Type**, select **“Raw”** and paste the following JSON template:  
     ```json
     {
       "first_name": "{{1.first_name}}",
       "last_name": "{{1.last_name}}",
       "email": "{{1.email}}",
       "company": "{{1.company}}"
     }
     ```  
   - *Expected output*: A module that will forward the webhook payload to FormStack for storage.

4. **Add a “Buffer” module to create a new social media client.**  
   - Click **“+”** → search **“Buffer”** → select **“Add a new team”**.  
   - Log in to Buffer by clicking **“Sign in with Buffer”** and entering your credentials.  
   - In the **Team Name** field, type **“Client - {{1.first_name}} {{1.last_name}}”**.  
   - Click **“Create”**.  
   - *Check‑in*: Do you see **“Team created successfully”** in the output panel? If not, confirm the Buffer API key is valid (see troubleshooting below).

5. **Set up a “Google Sheets” module to store client data.**  
   - Click **“+”** → search **“Google Sheets”** → choose **“Add a row to a sheet”**.  
   - Sign in to Google, select the spreadsheet **“Client Onboarding”**.  
   - In the **Sheet** dropdown, pick **“Clients”**.  
   - Map the following columns:  
     - `A`: `{{1.first_name}}`  
     - `B`: `{{1.last_name}}`  
     - `C`: `{{1.email}}`  
     - `D`: `{{1.company}}`  
     - `E`: `{{2.Team ID}}` (output from Buffer).  
   - Click **“Save”**.  
   - *Expected output*: A new row appears in the Clients sheet with the client’s details.

6. **Create a “Calendly” meeting link template for the onboarding call.**  
   - Open **https://calendly.com** in a new tab.  
   - Click **“Event Types”** → **“Create event type”** → choose **“One‑to‑one”**.  
   - Set the duration to **30 min** and name it **“AI Social Media Onboarding”**.  
   - Under **Advanced**, enable **“Invitee can reschedule”**.  
   - Save and copy the event URL (e.g., `https://calendly.com/yourname/ai-social-onboarding`).  
   - Store this URL in a variable **`calendly_url`** for later use.

7. **Add a “Buffer” module to schedule a welcome post.**  
   - Click **“+”** → search **“Buffer”** → select **“Add a message to a queue”**.  
   - Choose the queue named **“Welcome Posts”**.  
   - In the **Message** field, type:  
     ```
     Hi {{1.first_name}}, welcome to your new AI‑powered social media plan! 🚀
     ```
   - Set **Scheduled Time** to **`{{now+1h}}`** (one hour from now).  
   - Click **“Add”**.  
   - *Expected output*: A confirmation with “Message queued for {{1.first_name}}”.

8. **Create a “Slack” module to notify the internal team.**  
   - Click **“+”** → search **“Slack”** → select **“Send a message”**.  
   - Choose the channel **#social_media_onboarding**.  
   - In the message box, paste:  
     ```
     New client onboarded: {{1.first_name}} {{1.last_name}} ({{1.email}}). Buffer team ID: {{2.Team ID}}. Scheduling call: {{calendly_url}}
     ```  
   - Click **“Send”**.  
   - *Expected output*: The Slack channel shows a new message with the client’s name and calendar

## Check-In: Module 3 Complete

- [ ] Design Your Service Delivery Framework in Notion completed and verified
- [ ] Build the Client Onboarding Automation Pipeline completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 4: FIRST BUILD

## Overview  
This module is the hands‑on heart of your AI‑driven social media service. You will design, build, and launch a fully automated workflow that pulls content from a client’s brand assets, transforms it with AI‑generated captions, schedules it across multiple platforms, and reports performance—all in a single, repeatable stack. By the end of this module you will have a live, client‑ready deliverable that demonstrates your capability to deliver scalable, low‑maintenance social media management.  

Skipping this module means you’ll lack the practical, proven workflow that differentiates your service in a crowded market. Without a demonstrable pipeline, prospects will doubt your ability to deliver on time and at scale, and you’ll miss the opportunity to showcase how AI tools can slash your own time‑to‑value. The entire revenue engine hinges on the ability to deploy a repeatable, automated system that can be handed off to clients with minimal hand‑holding. This module guarantees that knowledge.  

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| **Make.com** | Automate data flow between Buffer, AI captioning, and analytics | 200 operations/month | 1,200 operations/month (Starter $9/mon) |
| **Buffer** | Schedule & publish posts across platforms | 3 social accounts, 10 posts per account | Pro $15/mon (5 accounts, unlimited posts) |
| **ChatGPT (OpenAI)** | Generate creative captions & hashtags | 3,000 tokens/day | ChatGPT‑plus $20/mon (infinite tokens) |
| **Canva** | Create visual assets & templates | Unlimited free content | Pro $12.99/mon (premium assets) |
| **Notion** | Document workflow & store client assets | Unlimited pages | Unlimited (free) |
| **Zapier** | Optional integration bridge for niche apps | 100 tasks/month | Starter $19.99/mon |
| **Midjourney** | Generate custom imagery for posts | 25 images/month | Basic $10/mon (100 images) |

**Estimated time to complete:** 5–6 hours of focused work, including setup, data import, testing, and final client hand‑off.

---

**Procedure 4.1** — Generation failed due to AI backend unavailability. Please retry later.

---

## Procedure 4.2: Create the Data Processing Pipeline with Make.com

1. **Open your browser** → Navigate to **https://app.make.com**.  
   *Expected result*: Make.com dashboard with “Create a new scenario” button visible.  

2. **Click** the **blue “Create a new scenario”** button on the top‑right corner.  
   *Expected result*: Blank scenario canvas with “Add an app” icon.  

3. **Search** for “Google Sheets” in the app picker. **Select** the Google Sheets module.  
   *Expected result*: “Google Sheets – Watch Rows” module appears on canvas.  

4. **Click** the module to open its settings.  
   - Under **Account**, click **“Add new connection”**.  
   - Authorize with your Google account: click **“Allow”**.  
   *Check‑in*: Do you see the “Google Sheets – Watch Rows” module with a green connection status? If not, ensure you are logged into the correct Google account and re‑click “Allow”.  

5. **Configure** the module:  
   - **Spreadsheet**: type the name of the sheet that contains new post ideas (e.g., “Client Ideas”).  
   - **Worksheet**: type “Ideas”.  
   - **Only new rows**: toggle ON.  
   *Expected result*: Module shows “Spreadsheet: Client Ideas | Worksheet: Ideas | Only new rows: ON”.  

6. **Click** the **+ icon** to add a second module. Search for “Text – Clean Text” and select it.  
   *Expected result*: “Text – Clean Text” module appears connected to the first module.  

7. **Link** the two modules by dragging the arrow from the Google Sheets module to the Clean Text module.  
   *Check‑in*: Do you see a green arrow connecting the two modules? If not, drag again.  

8. **Configure** the Clean Text module:  
   - **Text**: click the variable icon → choose **“Add a variable”** → select **“Row values → Description”** (the column that holds the post idea).  
   *Expected result*: Clean Text module shows “Text: Row values → Description”.  

9. **Add** a third module by clicking the **+ icon** → search for “OpenAI – Complete” (ChatGPT).  
   - **API Key**: click **“Add new connection”** → paste your OpenAI API key (free tier: 5,000 messages/month).  
   *Expected result*: OpenAI module appears with a green connection status.  

10. **Configure** the OpenAI module:  
    - **Prompt**: type “Generate a 280‑character tweet about the following topic: {{Clean Text – Output}}”.  
    - **Model**: set to **“gpt‑3.5‑turbo”**.  
    - **Temperature**: 0.7.  
    *Check‑in*: Do you see the prompt and model fields populated? If not, re‑enter them.  

11. **Add** a fourth module → search for “Buffer – Create a scheduled post”.  
    - **Account**: click **“Add new connection”** → log in with your Buffer account (free tier: 10 scheduled posts/month).  
    *Expected result*: Buffer module shows “Create a scheduled post” with a green connection status.  

12. **Configure** the Buffer module:  
    - **Account**: choose your Buffer account.  
    - **Social account**: select **“Client Twitter”** (ensure this Twitter account is linked in Buffer).  
    - **Message**: click the variable icon → select **“OpenAI – Complete → Output”**.  
    - **Scheduled time**: set to **“Now + 1 hour”** (use the relative time dropdown).  
    *Expected result*: Buffer module displays the chosen Twitter account and scheduled time.  

13. **Click** the **clock icon** in the top right → set the scenario to run **“every 5 minutes”**.  
    *Check‑in*: Do you see the schedule set to 5 minutes? If not, adjust the interval.  

14. **Save** the scenario by clicking the **“Save”** button at the top left.  
    - Name it **“AI Tweet Pipeline”**.  
    *Expected result*: Confirmation toast “Scenario saved successfully”.  

15. **Test** the scenario manually: click **“Run once”**.  
    - If the Google Sheets module finds a new row, the pipeline should output a tweet in Buffer.  
    *Check‑in*: Do you see the tweet scheduled in Buffer’s dashboard? If not, verify each module’s output in the run history.  

16. **Open Buffer** → go to **https://buffer.com** → log in.  
    - Navigate to the **“Scheduled”** tab → confirm the new tweet appears with status “Scheduled”.  

17. **Create a Make.com webhook** to allow external data ingestion:  
    - In Make.com, add a new module → “Webhooks – Custom Webhook”.  
    - Click **“Add”** → name it **“ClientPostWebhook”**.  
    - Copy the generated URL (e.g., `https://hook.make.com/abcd1234`).  
    *Expected result*: URL displayed in a modal.  

18. **Set up a Zapier** integration (free tier: 100 tasks/month) to forward data from your client’s form to the webhook:  
    - In Zapier, create a new Zap → trigger: “Webhooks by Zapier – Catch Hook”.  
    - Paste the Make.com URL.  
    - Test trigger → Zapier pulls sample data.  
    - Action: “Make.com – Add a row to Google Sheet”.  
    - Map the form fields to the Google Sheet columns (“Title”, “Description”).  
    - Turn on the Zap.  
    *Check‑in*: Does Zap

---

## Procedure 4.3: DEPLOY AND TEST THE COMPLETE SYSTEM

1. **Open Make.com and log in**  
   - URL: https://www.make.com/  
   - Click **Sign in** (top‑right).  
   - Enter your credentials and click **Log in**.  
   - *Check‑in*: Do you see the dashboard with “My Scenarios” tab? If not, clear cache or try a different browser.

2. **Create a new scenario**  
   - On the dashboard, click **Create a new scenario** (center of the page).  
   - A blank canvas opens.  
   - At top left, click **+ Add another module**.  
   - Search for **Buffer** and click the **Buffer** icon.  
   - *Check‑in*: Do you see the Buffer module in the canvas? If not, search “Buffer” again; Make.com may need to refresh.

3. **Connect your Buffer account**  
   - In the Buffer module settings, click **Add** next to “Buffer account.”  
   - A pop‑up appears: choose **Connect a new account**.  
   - A new window opens: click **Authorize** to allow Make.com to access Buffer.  
   - Return to Make.com; the module now displays “Connected to Buffer.”  
   - *Check‑in*: Do you see “Connected to Buffer” in the module? If you see “Authorization needed,” re‑authorize from Buffer’s app page (https://buffer.com/settings/apps).

4. **Set the trigger to run daily at 10:00 AM**  
   - Click the first module (Buffer).  
   - In the left pane, under **Trigger**, select **Schedule** → **Every day**.  
   - Set **Time** to **10:00 AM** (choose your time zone).  
   - Click **Save**.  
   - *Check‑in*: Do you see the schedule displayed as “Every day at 10:00 AM”? If not, ensure the time zone matches your account’s setting.

5. **Add a ChatGPT module for content generation**  
   - Click **+ Add another module**.  
   - Search for **ChatGPT** (Make.com integration).  
   - Click the **ChatGPT** icon.  
   - In the module, click **Add** next to “OpenAI API key.”  
   - Paste your API key from https://platform.openai.com/account/api-keys.  
   - Set **Prompt** to:  
     ```
     Generate a 280‑character tweet about new AI social media workflow tools. Include a call‑to‑action: “Try our service now!” 
     ```  
   - Under **Model**, choose **gpt‑3.5‑turbo**.  
   - Set **Max tokens** to **60**.  
   - Click **Save**.  
   - *Check‑in*: Do you see “ChatGPT – gpt‑3.5‑turbo” in the canvas? If you see “Error: Invalid API key,” double‑check the key.

6. **Route ChatGPT output to Buffer**  
   - Drag the arrow from the ChatGPT module to the Buffer module.  
   - In the Buffer module’s **Content** field, click **Add variable** → **ChatGPT – text**.  
   - In the **Channel** field, select **Twitter**.  
   - Click **Save**.  
   - *Check‑in*: Does the Buffer module now display “Content: {{ChatGPT – text}}”? If not, re‑click **Add variable**.

7. **Add a “Set variable” module to log the post ID**  
   - Click **+ Add another module**.  
   - Search for **Set variable**.  
   - Click the icon.  
   - In the field **Name**, type **post_id**.  
   - In **Value**, click **Add variable** → **Buffer – post_id**.  
   - Click **Save**.  
   - Connect this module to the Buffer module (drag arrow).  
   - *Check‑in*: Do you see “post_id” listed under **Variables**? If not, ensure the arrow connects correctly.

8. **Add a Slack notification (optional)**  
   - Click **+ Add another module**.  
   - Search **Slack** → **Send a message**.  
   - Connect your Slack

## Check-In: Module 4 Complete

- [ ] Build the Core AI Product in Replit completed and verified
- [ ] Create the Data Processing Pipeline with Make.com completed and verified
- [ ] DEPLOY AND TEST THE COMPLETE SYSTEM completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 5: CLIENT ACQUISITION

## Overview  
In this module we turn raw social‑media automation potential into a cash‑generating client pipeline. You will learn how to craft irresistible outreach, build a high‑converting landing page, and set up a lead‑generation funnel that feeds directly into your AI‑powered posting engine. Skipping this module means spending months chasing leads, building custom dashboards from scratch, and missing out on the first‑mover advantage in the booming AI social‑media service market.  

By mastering the steps here, you will:  
1. Create a landing page that converts strangers into qualified prospects in under 30 minutes.  
2. Automate every outreach touchpoint—email, LinkedIn, direct messages—using Make.com to trigger Buffer posts that showcase your service.  
3. Capture, score, and nurture leads through a seamless pipeline that turns free trials into paid contracts.  

You will also get a detailed cost map of every tool, so you know exactly what you pay for and can scale without hidden surprises.

| Tool      | Purpose                                 | Free Tier                                    | Paid Tier (Monthly) |
|-----------|------------------------------------------|----------------------------------------------|---------------------|
| Make.com  | Workflow automation & API integration   | 2,000 operations / 100 MB data transfer      | $9 (10,000 ops)     |
| Buffer    | Social‑media scheduling & analytics      | 3 social accounts, 10 posts/account          | Pro $12 (8 accounts, 100 posts) |
| Notion    | Project & pipeline management            | Unlimited pages & collaborators              | Personal $4 (5 GB)  |
| ChatGPT   | Content ideation & copywriting          | 3 M tokens/month (free)                      | ChatGPT‑4 $20 (3 M tokens) |

**Estimated time to complete this module**: **3 hours** (includes building the landing page, configuring Make.com flows, and setting up Buffer scheduling).

---

## Procedure 5.1: BUILD A HIGH‑CONVERSION LANDING PAGE ON SHOPIFY

1. **Open the Shopify pricing page**  
   - URL: `https://www.shopify.com/plan`  
   - Click the **bold** button **“Start free trial”**.  
   - In the popup, fill:  
     - **Email**: `yourname@example.com`  
     - **Password**: `StrongPass!23`  
     - **Store name**: `SocialAIPro`  
   - Click **“Create your store”**.  
   - You should see the **Shopify admin dashboard** with a welcome banner.

2. **Set up basic store details**  
   - In the left sidebar, click **“Settings”** → **“General”**.  
   - Under **“Store details”**, enter:  
     - **Primary domain**: `socialaipro.com` (you can use a free domain or a test domain).  
     - **Contact email**: `sales@socialaipro.com`  
   - Scroll to the bottom and click **“Save”**.  
   - Expected result: A confirmation toast ‑ “Store details saved”.

3. **Add the free Debut theme**  
   - In the sidebar, click **“Online Store”** → **“Themes”**.  
   - Under **“Explore free themes”**, locate **Debut** and click the **“Add”** button.  
   - After adding, click **“Actions”** → **“Publish”**.  
   - The banner “Debut theme published” should appear.

4. **Customize the header**  
   - Click **“Customize”** next to Debut.  
   - In the left panel, click **“Header”**.  
   - In the header editor, enter:  
     - **Store name**: `SocialAIPro`  
     - **Logo**: Upload a PNG (use `https://cdn.craft.co/logo.png`).  
   - Click **“Save”**.  
   - **Do you see the updated header with your store name and logo?**  
     - If not, refresh the page and repeat the above steps.

5. **Create

---

## Procedure 5.2: Set Up Lead Generation with Apollo.io  

1. **Open your browser** and go to **https://app.apollo.io/**.  
2. Click the **“Sign up free”** button in the top‑right corner.  
3. In the sign‑up form, fill in the following fields:  
   - **Full name** – “John Doe”  
   - **Company** – “Menshly Global”  
   - **Email** – “john@menshlyglobal.com”  
   - **Password** – “M3nsHly2024!”  
4. Click the **“Create account”** button.  
   *Do you see the Apollo dashboard with a green “Welcome to Apollo” banner? If not, check your email for a verification link and click it.*  

5. In the top navigation, click **“Settings”** (gear icon).  
6. Under **“Account”**, locate **“API Key”** and click **“Generate new key”**.  
7. Copy the 32‑character key and paste it into a secure note in **Notion** (URL: **https://www.notion.so/**).  
8. Return to the Apollo dashboard and click **“Lead Sources”** in the left sidebar.  
   *Do you see the “Create Lead Source” button? If not, ensure you have admin privileges.*  

9. Click **“Create Lead Source”**.  
10. In the modal, fill in:  
    - **Name** – “Buffer Social Flow”  
    - **Type** – “Manual Upload”  
    - [**Description**](https://www.descript.com/) – “Leads collected via Buffer social media posts”  
11. Click **“Save”**.  
12. Apollo will display a success toast: “Lead source ‘Buffer Social Flow’ created.”  
    *Do you see this toast? If not, refresh the page.*  

13. Open a new tab and navigate to **https://app.buffer.com/**.  
14. Log in with your Buffer account or create a free account at **https://buffer.com/signup**.  
15. In Buffer, go to the **“Content Library”** tab.  
16. Click **“Create New Post”** → **“Add Post”** → **“Upload CSV”**.  
    *Do you see the CSV upload dialog? If not, ensure you’re on the “Content Library” page.*  

17. Prepare a CSV file named **“BufferLeads.csv”** with columns: `First Name`, `Last Name`, `Company`, `Email`, `Phone`.  
18. In Buffer, upload **BufferLeads.csv**.  
19. After upload, Buffer will show a preview. Verify that all rows display correctly.  
20. Click **“Save & Publish”** to publish the post.  
    *Do you see the post in your scheduled queue? If not, confirm the file format matches Buffer’s CSV requirements.*  

21. Return to Apollo.  
22. Click the **“Import”** button on the **“Buffer Social Flow”** lead source you created earlier.  
23. In the import dialog, choose **“From CSV”** and upload the same **BufferLeads.csv** file.  
24. Map the CSV columns to Apollo fields exactly:  
    - `First Name` → **First Name**  
    - `Last Name` → **Last Name**  
    - `Company` → **Company**  
    - `Email` → **Email**  
    - `Phone` → **Phone**  
25. Click **“Start Import”**.  
    *Do you see the import progress bar reach 100%? If not, check for duplicate emails or missing required fields.*  

26. Once imported, Apollo will display a summary: **“50 leads imported, 0 duplicates, 0 errors.”**  
27. In the Apollo dashboard, click **“Lists”** → **“Create List”**.  
28. Name the list **“Buffer Leads Q4”** and add the imported leads via the **“Add to List”** button.  
29. Click the **“Create”** button.  
30. Apollo now has a fully populated lead list ready for outreach.  

**Error Scenario**  
- *If you see “Error: Duplicate email detected” during import, this means the same email appears more than once in the CSV.*  
  - **Fix it by**:  
    1. Opening the CSV in Excel.  
    2. Removing duplicate rows.  
    3. Re‑uploading the cleaned file.  

**Pricing Comparison Table**

| Tool | Free Tier | Paid Tier (USD/mo) | Key Feature |
|------|-----------|--------------------|-------------|
| Apollo.io | 50 credits/month | Pro: $99/mo (unlimited credits) | Advanced prospect search, email sequences |
| Buffer | 3 social accounts | Premium: $15/mo (10 accounts) | Scheduling & analytics |
| Make.com (formerly Integromat) | 1,000 operations/month | Basic: $9/mo (10,000 ops) | Workflow automation |
| Zapier | 100 tasks/month | Starter: $19.99/mo (750 tasks) | App integrations |

**Cost Breakdown for this Setup**

| Item | Quantity | Unit Price | Total |
|------|----------|------------|-------|
| Apollo Pro | 1 | $99 | $99 |
| Buffer Premium | 1 | $15 | $15 |
| Make.com Basic | 1 | $9 | $9 |
| **Total Monthly** | | | **$123** |

*All prices are current as of October 2026. Free tiers are listed in the table. No hidden fees.*

Follow each step exactly; the lead generation pipeline will now feed Apollo.io, enabling you to launch automated outreach powered by Buffer and Make.com.

---

## Procedure 5.3: CREATE AUTOMATED EMAIL NURTURE SEQUENCE IN KLAVIYO

1. **Open a Web Browser**  
   - Launch Chrome, Firefox, or Edge.  
   - In the address bar type `https://www.klaviyo.com/` and press **Enter**.  
   - Expected screen: Klaviyo landing page with a large **“Sign Up”** button in the top‑right corner.

2. **Create a Klaviyo Account**  
   - Click **“Sign Up”** (bold).  
   - In the modal, enter your *Name*, *Email*, and *Password*.  
   - Click **“Create Account”** (bold).  
   - Expected result: Dashboard with the “Welcome to Klaviyo” overlay.  

3. **Connect a Shopify Store (Optional)**  
   - From the left sidebar, click **“Integrations”** (bold).  
   - Under “Shopify”, click **“Connect”** (bold).  
   - Log in with your Shopify credentials and approve permissions.  
   - Expected result: Integration status shows **“Connected”**.

4. **Create a Contact List**  
   - In the left sidebar, click **“Lists & Segments”** (bold).  
   - Click **“Create List / Segment”** (bold).  
   - Select **“List”**, name it **“Email Nurture Subscribers”**, and click **“Create List”** (bold).  
   - *Check‑in*: Do you see the new list named “Email Nurture Subscribers” in your dashboard?  
     - **If not**, click **Refresh** at the top and verify your internet connection.

5. **Add a Signup Form to Capture Leads**  
   - Click **“Signup Forms”** (bold) in the left sidebar.  
   - Click **“Create Signup Form”** (bold).  
   - Choose **“Pop‑Up”**, give it the name **“Nurture Pop‑Up”**, and click **“Create”** (bold).  
   - In the editor, drag a **“Form”** widget onto the canvas.  
   - Under **Form Settings**, set the *List* to **“Email Nurture Subscribers”**.  
   - Click **“Save”** (bold) and then **“Publish”** (bold).  
   - Expected outcome: A preview URL appears; copy this URL for later.

6. **Create Email Templates**  
   - In the left sidebar, click **“Email Templates”** (bold).  
   - Click **“Create Template”** (bold).  
   - Choose **“Drag & Drop”**, name it **“Nurture Email 1”**, and click **“Create”** (bold).  
   - In the editor, add a **“Text”** block, type “Welcome to our community!”, and style it using the toolbar.  
   - Add a **“Button”** block linking to `https://yourdomain.com/learn-more`.  
   - Click **“Save”** (bold).  
   - Repeat steps 6.1‑6.4 for **“Nurture Email 2”** and **“Nurture Email 3”**.

7. **Set Up an Email Flow**  
   - In the left sidebar, click **“Flows”** (bold).  
   - Click **“Create Flow”** (bold).  
   - Name the flow **“Client Nurture Sequence”**, choose **“Triggered by List Signup”**, and click **“Create Flow”** (bold).  
   - Drag the **“Add Action”** node onto the canvas and select **“Send Email”** (bold).  
   - In the email picker, choose **“Nurture Email 1”**.  
   - Set the delay to **“0 days”**.  
   - Add a second **“Send Email”** node, select **“Nurture Email 2”**, and set the delay to **“3 days”**.  
   - Add a third **“Send Email”** node, select **“Nurture Email 3”**, and set the delay to **“7 days”**.  
   - Click **“Done”** (bold) to close the flow editor.  
   - Expected result: Flow diagram shows three sequential emails with correct delays.

8. **Activate the Flow**  
   - In the flow editor, locate the **“Status”** toggle in the top-right corner.  
   - Click the toggle to switch from **“Draft”** to **“Active”** (bold).  
   - Confirm with the pop‑up by clicking **“Activate Flow”** (bold).  
   - *Check‑in*: Do you see the flow status change to **“Active”**?  
     - **If not**, ensure you have no pending validation errors; resolve any highlighted fields.

9. **Test the Flow with a Test Email Address**  
   - In the left sidebar, click **“People”** (bold).  
   - Click **“Add Person”** (bold).  
   - Enter **Email**

## Check-In: Module 5 Complete

- [ ] BUILD A HIGH‑CONVERSION LANDING PAGE ON SHOPIFY completed and verified
- [ ] Set Up Lead Generation with Apollo.io completed and verified
- [ ] CREATE AUTOMATED EMAIL NURTURE SEQUENCE IN KLAVIYO completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 6: DELIVERY

## Overview

Module 6 is the linchpin that converts your AI‑driven social media blueprints into repeatable, client‑ready services. In this module you learn how to **build a delivery pipeline** that guarantees consistent quality, establishes clear checkpoints, and automates all client‑communication touchpoints. By mastering this workflow, you prevent the common pitfalls of ad‑hoc content delivery—delays, mis‑aligned expectations, and frustrated customers. If you skip this module, your clients will receive uneven output, your brand will lose credibility, and you’ll struggle to scale beyond a handful of accounts.

You will also create **quality assurance templates** (e.g., post‑launch audit sheets, KPI dashboards in Notion) and **client‑communication scripts** (welcome emails, progress reports) that are fully integrated into Buffer’s scheduling UI and Make.com’s automation paths. This ensures that every post, analytics report, and feedback loop is handled automatically, freeing you to focus on strategy and growth. Skipping this module means losing the ability to systematically monitor performance, which translates directly to missed revenue opportunities and higher churn rates.

**Tools required for this module**

| Tool      | Purpose                                                    | Free Tier                          | Paid Tier (Monthly) |
|-----------|------------------------------------------------------------|------------------------------------|---------------------|
| Make.com  | Orchestrate end‑to‑end AI content creation, Buffer API, and client‑notification workflows | 25 operations/month, 100 MB storage | $29/month (Starter) |
| Buffer    | Social‑media scheduling, analytics, and team collaboration | 10 posts per social account, 1 account | $15/month (Pro) |
| Notion    | Client brief templates, KPI dashboards, and quality checklists | Unlimited pages, 5 users, 1 GB upload | $8/month (Personal Pro) |
| Zapier    | Optional fallback for low‑volume clients (1 000 tasks/month) | Unlimited apps, 100 tasks/month | $19/month (Starter) |
| Mailchimp | Client‑communication templates (email updates, reporting) | 2 000 contacts, 12 000 emails/month | $9.99/month (Free) |

> **Estimated time to complete:** 3 hours (2 hours for pipeline setup, 30 min for templates, 30 min for testing and QA).

---

## Procedure 6.1: Deploy the Product to Production on Hostinger

1. **Create a Hostinger account**  
   - Visit **https://www.hostinger.com**.  
   - Click **SIGN UP** (upper‑right corner).  
   - Choose the **Shared Hosting** plan (price: **$2.95** / mo, billed annually).  
   - Enter your email, password, and click **CREATE ACCOUNT**.  
   - Verify your email and log in to the Hostinger control panel.  
   - *Do you see the dashboard with “Hosting” and “Sites” tabs?* If not, check your email for a verification link or contact Hostinger support.

2. **Register a domain**  
   - In the Hostinger control panel, click **Domains → Add Domain**.  
   - Type `yourbrand.ai` and click **SEARCH**.  
   - If the domain is available, click **ADD**.  
   - Confirm your order (free domain with the plan).  
   - *Do you see “Domain added” confirmation?* If not, ensure the domain is not already in use.

3. **Create a new hosting package**  
   - Click **Hosting → Add Hosting**.  
   - Select the domain you just added (`yourbrand.ai`).  
   - Choose the **Starter Pack** (same $2.95 / mo).  
   - Leave the default settings and click **ADD HOSTING**.  
   - *Do you see “Hosting package created” on the summary page?* If not, re‑select the domain.

4. **Set up SSH access**  
   - In the hosting package page, click **SSH → Enable**.  
   - Copy the generated **SSH Username** (`yourusername`).  
   - Click **Generate SSH Key** and download the private key (`id_rsa`).  
   - *Do you see the SSH key details?* If not, re‑enable SSH.

5. **Upload the project files via SFTP**  
   - Open **FileZilla** (free, 0 $).  
   - Create a new site:  
     - **Host**: `yourbrand.ai`  
     - **Port**: `22`  
     - **Protocol**: SFTP – File Transfer Protocol  
     - **Logon Type**: Normal  
     - **User**: `yourusername` (from step 4)  
     - **Password**: paste the private key content in the password field.  
   - Click **Quickconnect**.  
   - Drag the entire `ai-social-workflow` folder (local) to the `/public_html/` directory.  
   - *Do you see the folder on the remote side?* If not, check the SSH key and port.

6. **Install Node.js on Hostinger**  
   - From the Hostinger control panel, go to **Advanced → Terminal**.  
   - In the terminal, run: `curl -sL https://deb.nodesource.com/setup_20.x | sudo -E bash -`  
   - Then `sudo apt-get install -y nodejs`.  
   - Verify with `node -v` (should output `v20.x.x`).  
   - *Do you see the node version?* If `node` not found, reinstall with `sudo apt-get install nodejs`.

7. **Install project dependencies**  
   - In the terminal, navigate to `/public_html/ai-social-workflow`: `cd /public_html/ai-social-workflow`.  
   - Run `npm install`.  
   - Wait for all packages to download (should finish within a minute).  
   - *Do you see “added 123 packages” in the terminal?* If errors about missing build tools, run `sudo apt-get install build-essential`.

8. **Configure environment variables**  
   - In the Hostinger control panel, go to **Advanced → Environment Variables**.  
   - Click **Add Variable** three times:  
     - **Key**: `NODE_ENV` → **Value**: `production`  
     - **Key**: `MAKE_TOKEN` → **Value**: *(copy from Make.com, see step 9)*  
     - **Key**: `BUFFER_TOKEN` → **Value**: *(copy from Buffer, see step 9)*  
   - Click **Save**.  
   - *Do you see the variables listed?* If not, refresh the page.

9. **Obtain API tokens**  
   - **Make.com**:  
     - Log in at **https://www.make.com**.  
     - Navigate to **My Apps → Add new app** → **HTTP**.  
     - Copy the **Access Token** displayed; this is your `MAKE_TOKEN`.  
   - **Buffer**:  
     - Log in at **https://buffer.com**.  
     - Go to **Settings → API**.  
     - Click **Generate New Token** and copy the token; this is your `BUFFER_TOKEN`.  
   - *Do you see your tokens in the clipboard?* If not, ensure you’re in the correct account.

10. **Start the application with PM2**  
    - In the terminal, install PM2 globally: `sudo npm install -g pm2`.  
    - Start the app: `pm2 start server.js --name ai-social-workflow`.  
    - Save the PM2 process list: `pm2 save`.  
    - Set PM2 to restart on boot: `pm2 startup systemd`.  
    - Follow the printed instruction to run the generated `sudo env PATH=$PATH:/usr/bin pm2 startup systemd -u yourusername --hp /home/yourusername`.  
    - *Do you see “Process ai-social-workflow online” in PM2

---

## Procedure 6.2: Build Quality Assurance and Client Communication Templates

1. **Open Notion**  
   - Go to https://www.notion.so/  
   - Click **Sign In** (top right), enter your credentials, then click **Log In**.  
   - Once inside, click the **+ New Page** button on the left sidebar, then choose **Blank**.  
   - Name the page **“Client QA & Communication Templates”**.  

2. **Create a QA Checklist Sub‑Page**  
   - Inside the new page, type `/page` and select **“Add a sub‑page”**.  
   - Title it **“Social Media QA Checklist”**.  
   - In the sub‑page, type `/toggle list` to create a collapsible list.  
   - Add the following items:  
     - ✅ Check post copy length (≤280 characters)  
     - ✅ Verify image resolution (1080×1080 px)  
     - ✅ Confirm correct hashtags (max 10)  
     - ✅ Validate link URL (no broken links)  
     - ✅ Ensure brand voice consistency (use brand guide)  

3. **Insert a Client Communication Template**  
   - Return to the main page, type `/toggle list` again.  
   - Add items:  
     - 📬 **Client Update Email**  
     - 📬 **Response to Feedback**  
   - For **Client Update Email**, click the bullet, then type `/table – 2 columns` to insert a table.  
   - In column A, list **“Subject”**, **“Body”**, **“Attachments”**.  
   - In column B, add placeholders:  
     - Subject: `Weekly Social Media Update – [Date]`  
     - Body: `Hi [Client Name],\n\nHere’s the overview of the posts scheduled for this week...\n\nBest regards,\n[Your Name]`  
     - Attachments: `Link to Buffer Dashboard`  

4. **Proofread with [Grammarly](https://grammarly.com/)**  
   - Open a new tab and go to https://app.grammarly.com/  
   - Click **“Start for free”**.  
   - Copy the **Client Update Email** body from Notion and paste into Grammarly’s editor.  
   - Click **Check**.  
   - Review suggestions and click **“Accept all”** to finalize.  
   - Copy the corrected text back into Notion’s table cell.  

**Do you see the corrected email body in Notion? If not, check that you copied the entire block and that Grammarly highlighted the text.**

5. **Set up Buffer for Client Accounts**  
   - Go to https://app.buffer.com/  
   - Click **“Add a new account”** (top right).  
   - Choose the social platform (e.g., **Instagram**).  
   - Follow the OAuth flow: log in, allow permissions, click **“Authorize”**.  
   - Once added, click **“Add another account”** if you have multiple clients.  

6. **Create a Buffer Playlist for QA**  
   - In Buffer, click **Playlists** on the left menu.  
   - Click **“Create playlist”** (bold button).  
   - Name it **“QA & Client Deliverables”**.  
   - Add the first client’s Instagram account by selecting it from the dropdown, then click **“Add”**.  

7. **Schedule a Test Post**  
   - In Buffer, click **“Content”** > **“Add to Queue”** (bold).  
   - Paste a test caption: `Testing QA workflow #socialmedia`.  
   - Upload an image (1080×1080 px) from your computer.  
   - Set the posting date to tomorrow at 10 AM.  
   - Click **“Schedule”**.  

8. **Create a Make.com Scenario for QA Notification**  
   - Open https://www.make.com/  
   - Click **“Create a new scenario”**.  
   - Search for **Buffer** in the first module, select **“Watch posts”**.  
   - Click **“Add”** (bold).  
   - Connect your Buffer account (click **“Add”**, login, then **“Authorize”**).  

9. **Configure the Scenario Trigger**  
   - In the Buffer module, set **“Post status”** to **“Scheduled”**.  
   - Click **“Add another module”** (bold).  
   - Search for **Email by Gmail**, select **“Send an email”**.  
   - Click **“Add”**, authorize Gmail.  
   - Map fields:  
     - **To** → `{{ClientEmail}}` (you will set this in the

## Check-In: Module 6 Complete

- [ ] Deploy the Product to Production on Hostinger completed and verified
- [ ] Build Quality Assurance and Client Communication Templates completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 7: SCALING

## Overview  
In this module you will transform a solo AI‑social‑media operation into a scalable, high‑margin service business. By integrating Make.com’s visual automation engine with Buffer’s robust scheduling platform, you’ll create repeatable, client‑ready workflows that run on autopilot. The lesson will show you how to hand off routine tasks to contractors, document every step in SOPs, and perform real‑time margin analysis to ensure each campaign remains profitable.

Skipping this module means you’ll continue to manage every post manually or with ad‑hoc scripts, capping your billable hours at 20‑30 per week. Without automated pipelines you’ll miss the opportunity to scale revenue beyond the “one‑person‑bandwidth” ceiling, and you’ll have no systematic way to measure profitability per client. You’ll also lack the documentation necessary to onboard talent quickly, exposing your business to inconsistency and risk.

**Tools Needed**

| Tool          | Purpose                                      | Free Tier                                | Paid Tier (Monthly) |
|---------------|---------------------------------------------|------------------------------------------|---------------------|
| Make.com      | Build and schedule AI‑driven social workflows | 500 operations per month, 2 GB data | $29 for 15,000 operations, 5 GB data |
| Buffer        | Publish & analyze posts across platforms      | 3 social accounts, 10 scheduled posts | $12 for 3 accounts, unlimited posts |
| ChatGPT‑4     | Generate captions, hashtags, & copy          | 3 M tokens per month (free)             | $20 for 100 M tokens |
| Airtable      | Store client data, SOPs, and metrics         | Unlimited records, 2 GB attachment      | $10 for 2 TB attachment |
| Zapier        | Connect Buffer to other tools (optional)     | 100 tasks per month                      | $19 for 2 000 tasks |

**Estimated Time to Complete**  
Total time: **4 hours** – 1 hour to set up Make.com, 1 hour to configure Buffer, 1 hour to document SOPs, 1 hour to run margin analysis and finalize templates.

---

## Procedure 7.1: Hire Your First Contractor on Upwork

1. **Open a Web Browser**  
   - Launch Google Chrome (latest version).  
   - In the address bar type `https://www.upwork.com` and press **Enter**.  
   - Expected output: Upwork homepage with a blue “Sign In” button at the top right.

2. **Create an Upwork Account**  
   - Click **Sign Up** (top right).  
   - Select **“I’m looking for talent”** and click **Continue**.  
   - Fill the form:  
     - *Email*: `yourname@example.com`  
     - *Password*: `StrongPassword!23` (exactly 12 characters, upper/lowercase, number, symbol)  
     - *Name*: `Your Full Name`  
     - *Country*: `United States`  
   - Click **Create Account**.  
   - Expected output: Account verification email with “Verify your email”.

3. **Verify Your Email**  
   - Open your email client, locate the Upwork email, click **Verify Email**.  
   - Expected output: Browser redirects to `https://www.upwork.com/ab/account-security/confirm` and shows “Email verified”.

4. **Complete Profile Setup**  
   - Click **Complete Profile** (blue button).  
   - Upload a professional headshot: click **Upload Photo**, select `headshot.jpg`.  
   - Fill *Title*: `Social Media Automation Specialist`.  
   - Fill *Overview*: “I build AI‑driven workflows with Make.com and Buffer for brands.”  
   - Click **Save & Continue**.  
   - Do you see a green checkmark next to each section? If not, re‑upload the photo or re‑fill the fields.

5. **Set Up Payment Method**  
   - From the dashboard, click **Settings** (gear icon) > **Billing**.  
   - Click **Add a Payment Method**.  
   - Choose **PayPal** and enter your PayPal credentials.  
   - Confirm with **Add**.  
   - Expected output: “Payment method added” banner.

6. **Search for Contractors**  
   - In the top search bar, type **“AI Social Media Manager”**.  
   - Click **Search**.  
   - Filter results:  
     - *Location*: “Anywhere”  
     - *Hourly Rate*: “$20 – $50” (slide bar to 50)  
     - *Job Success*: “>90%” (toggle on)  
   - Click **Apply Filters**.  
   - Expected output: List of 20‑30 freelancers.

7. **Review Profiles**  
   - Click the first profile.  
   - Verify the following:  
     - *Profile Photo*: professional.  
     - *Title*: “Social Media Automation Expert”.  
     - *Hourly Rate*: $35.00.  
     - *Job Success*: 95%.  
     - *Number of Completed Jobs*: 120+.  
   - Check the *Portfolio* tab for 2‑3 case studies.  
   - If any red flags (no portfolio, <50 jobs), skip to next.

8. **Send an Invitation**  
   - On the profile page, click **Invite to Job** (blue button).  
   - In the popup, fill:  
     - *Job Title*: “Hire AI Social Media Contractor”.  
     - *Budget*: $500 (fixed price).  
     - *Duration*: 1 month.  
   - Click **Invite**.  
   - Expected output: “Invitation sent” toast at bottom right.

9. **Follow Up with Candidate**  
   - Open your email client.  
   - Draft reply:  
     - Subject: “Re: Invitation for AI Social Media Contractor”  
     - Body: “Hi [Name], thanks for accepting. I’d like to schedule a 15‑minute call to discuss Scope, Deliverables, and Buffer integration.”  
   - Attach a Google Docs link: `https://docs.google.com/document/d/XYZ` (create a brief brief).  
   - Click **Send**.  
   - Do you see the email sent confirmation? If not, check spam or resend.

10. **

---

## Procedure 7.2: Build SOPs for Task Delegation in Notion

1. **Open a web browser** and navigate to <https://www.notion.so>.  
2. **Log in** using your email and password. If you do not have an account, click **Sign up** and complete the registration.  
3. **Create a new workspace** by clicking the drop‑down arrow next to your workspace name in the top‑left corner, then select **Add a new workspace**. Name it **“Social Media SOPs”**.  
4. **Create a new page** inside the workspace: click **+ New Page** on the left sidebar, choose **Blank** and title it **“Task Delegation SOP”**.  
   *Do you see the new page with the title “Task Delegation SOP”? If not, refresh the browser and repeat steps 3‑4.*  

5. **Add a database table**: type `/table` → select **Table – Full page**.  
6. **Rename the table** to **“Task Delegation Matrix”**.  
7. **Edit the default columns**:  
   - **Name** → **Task Title** (click the column header → **Rename**).  
   - **Tags** → **Task Category** (rename).  
   - **Person** → **Owner** (rename).  
   - **Date** → **Due Date** (rename).  
8. **Add a new column**: click **+ Add a property** → choose **Select** → name it **Status**.  
9. **Define status options**: click the **Status** column → **+ Add a new option** → create **Pending**, **In Progress**, **Completed**, **On Hold**.  
   *Do you see the four status options? If you don’t, delete the column and recreate it.*  

10. **Create a template button**: type `/button` → select **Button**.  
11. **Configure the button**:  
    - **Name**: **Create New Task**.  
    - **Action**: **Create a new page**.  
    - **Template**: choose the **Task Delegation Matrix** table.  
12. **Place the button** at the top of the page by dragging it into the page header.  
13. **Set up a view**: click **+ Add a view** → choose **Board** → name it **By Owner**.  
14. **Configure board groups**: drag **Owner** column into the board view, then click **Group by Owner**.  
    *Do you see the board grouped by owners? If the board shows no groups, double‑click the Owner column header and confirm the grouping.*  

15. **Embed a Make.com workflow**:  
    - Open <https://www.make.com>.  
    - Click **Create a new scenario** → choose **Buffer** → **Add a “Publish content” module**.  
    - Connect your Buffer account and set the **Schedule** to **Immediate**.  
    - In the **Content** field, enter `{{task_title}} - {{task_description}}`.  
    - Save and activate the scenario.  
16. **Link Make.com to Notion**:  
    - In Make.com, add a **Notion** module → **Create a database item**.  
    - Authenticate with your Notion API key (found under Settings & Members → Integrations → New integration).  
    - Map the **Task Delegation Matrix** database to the module.  
    - Map fields: **Task Title** → `title`, **Task Category** → `tags`, **Owner** → `person`, **Due Date** → `date`.  
    - Save and activate.  
17. **Test the workflow**:  
    - Click the **Create New Task** button on Notion.  
    - Fill in **Task Title**: *“Schedule Instagram Reel”*.  
    - Select **Task Category**: *“Content Creation”*.  
    - Assign **Owner**: *“John Doe”*.  
    - Set **Due Date**: *today + 3 days*.  
    - Click **Create**.  
    - Verify that a new row appears in the **Task Delegation Matrix** and that the Make.com scenario logs a **Publish content** event in Buffer.  
    - Check Buffer’s dashboard (<https://buffer.com/dashboard>) to see the queued post.  

**Error Scenario**  
If after creating a new task you see **“Error 401 – Unauthorized”** in Make.com:  
- This means the Notion integration key has expired or missing permissions.  
- Fix it by:  
  1. Going to Notion → Settings & Members → Integrations → **Revoke** the current key.  
  2. Click **Create new integration**, name it **“Buffer SOP Bot”**, check **“Read content”**, **“Insert content”**, and **“Update content”**.  
  3. Copy the new integration token.  
  4. In Make.com, delete the old Notion module and add a new one, pasting the new token.  

**Pricing Comparison Table**

| Tool | Plan | Monthly Cost | Free Tier Limit | Key Features |
|------|------|--------------|-----------------|--------------|
| Notion | Personal | $0 | 5,000 blocks | Unlimited pages, databases, inline widgets |
| Notion | Team | $8/user | • | Team sharing, advanced permissions |
| Buffer | Free | $0 | 3 social accounts, 10 scheduled posts | Basic scheduling |
| Buffer | Pro | $12/user | • | Unlimited accounts, analytics, team collaboration |
| Make.com | Free | $0 | 100 operations/month | Basic automations, 5 active scenarios |
| Make.com | Professional | $29 | • | 2,000 operations, 3 active scenarios, priority support |

**Expected Output**  
- A single Notion page titled **“Task Delegation SOP”** containing:  
  - A **Task Delegation Matrix** table with columns **Task Title**, **Task Category**, **Owner**, **Due Date**, **Status**.  
  - A **Create New Task** button

---

## Procedure 7.3: Run a Margin Analysis and Pricing Review

1. **Open Google Sheets**  
   - URL: <https://sheets.google.com>  
   - Click **NEW** (top‑left) → **Google Sheets**.  
   - Name the spreadsheet **“Margin Analysis – AI Social Media”** by clicking the default title and typing the new name.  
   - Do you see the blank spreadsheet? If not, refresh the page or clear your browser cache.

2. **Set up column headers**  
   - In cell **A1** type **Service**.  
   - In cell **B1** type **Monthly Client Count**.  
   - In cell **C1** type **Revenue per Client ($)**.  
   - In cell **D1** type **Buffer Cost ($)**.  
   - In cell **E1** type **Make.com Cost ($)**.  
   - In cell **F1** type **Other Costs ($)**.  
   - In cell **G1** type **Total Cost ($)**.  
   - In cell **H1** type **Gross Margin (%)**.  
   - In cell **I1** type **Net Margin (%)**.  
   - Do you see all nine columns labeled? If not, check that you entered the exact text and that the cells are in the correct order.

3. **Enter sample data for your flagship service**  
   - **A2**: *AI Social Media Automation*  
   - **B2**: *10* (client count)  
   - **C2**: *500* (USD per client)  
   - Do you see the data in the first row? If not, verify you typed in the correct cells.

4. **Input Buffer cost**  
   - Buffer offers three paid plans:  
     - Starter: $15/mo (3 accounts)  
     - Standard: $65/mo (5 accounts)  
     - Premium: $99/mo (10 accounts)  
   - For 10 clients, select **Standard** plan: **$65**.  
   - In **D2** type **65**.  
   - **Do you see $65 in D2?** If the cell shows a different value, double‑check the number.

5. **Input Make.com cost**  
   - Make.com pricing:  
     - Start: $49/mo (400 operations)  
     - Growth: $99/mo (1,200 operations)  
     - Pro: $149/mo (3,000 operations)  
   - For a 10‑client workflow, choose **Growth** plan: **$99**.  
   - In **E2** type **99**.  
   - **Do you see $99 in E2?** If not,

## Check-In: Module 7 Complete

- [ ] Hire Your First Contractor on Upwork completed and verified
- [ ] Build SOPs for Task Delegation in Notion completed and verified
- [ ] Run a Margin Analysis and Pricing Review completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 8: ADVANCED PATTERNS

## Overview  
Module 8 dives deep into the high‑value patterns that transform a one‑time social‑media service into a recurring, high‑ticket revenue stream. You’ll learn how to layer AI‑driven content creation, automation, and data‑driven insights to offer premium packages that command 3‑to‑5× the price of a standard posting service. By mastering these patterns you’ll build productized funnels, upsell clients on advanced reporting, and lock in monthly retainers that scale with minimal incremental effort.  

Why it matters: In the social‑media marketplace, agencies that automate rather than manual‑batch workflows win the war on price and time. Skip this module and you’ll stay stuck in a “post‑every‑day” mode, unable to justify higher rates or secure long‑term contracts. Clients will default to cheaper, less automated competitors, and you’ll miss out on the recurring revenue that keeps the business profitable beyond the first month.  

If you ignore the advanced patterns, you’ll keep offering generic, flat‑rate services that erode profit margins. You’ll also lose the ability to upsell data‑rich dashboards, AI‑generated caption bundles, or niche‑market content packages that differentiate your brand and drive referral traffic.  

### Tools Required

| Tool          | Purpose                                           | Free Tier                             | Paid Tier                     |
|---------------|---------------------------------------------------|---------------------------------------|-------------------------------|
| Make.com      | Build AI‑powered workflows that pull, transform, and push content | 500 tasks/month (basic)                | $99/month (Professional)     |
| Buffer        | Schedule, publish, and analyze social posts      | 3 social accounts, 10 posts queued     | $59/month (Pro)               |
| ChatGPT       | Generate captions, headlines, and copy           | 3,000 tokens/day (free)               | $20/month (ChatGPT Plus)      |
| Canva         | Design visual assets for posts and stories       | Unlimited free features               | $12.99/month (Pro)            |

**Estimated time to complete**: 8 – 10 hours (focus on the two procedures that build recurring revenue and productized offerings).

---

## Procedure 8.1: Create a High‑Ticket Consulting Package

**Goal:** Build a turnkey AI‑powered social‑media service that you can sell for $3,000‑$5,000/month. The package will include a client onboarding portal, an automated content‑generation workflow (Make.com + ChatGPT), a brand‑consistent visual kit (Canva), and a publishing pipeline (Buffer). By the end of this procedure you will have a ready‑to‑sell consulting offer, a demo deck, and a fully automated pipeline.

---

### 1. Set Up the Consulting Offer Canvas  
1.1 Open **Notion** (https://notion.so).  
1.2 In the sidebar, click **+ New Page**.  
1.3 Title the page **“AI Social Media Consulting – High‑Ticket Package”**.  
1.4 Inside the page, add a **Table** block (click **+**, search for “Table – Inline”).  
1.5 Create columns:  
- **Feature** (text)  
- **Client Benefit** (text)  
- **Pricing Tier** (select: Basic, Premium, Enterprise)  
- **Deliverable** (file)  

1.6 Fill the first row:  
- Feature: **AI‑Generated Content Calendar**  
- Client Benefit: “30 days of ready‑to‑publish posts”  
- Pricing Tier: **Premium**  
- Deliverable: (leave blank for now)  

1.7 Duplicate the table three times to cover Basic, Premium, Enterprise tiers.

*Check‑in:* Do you see the three tables with the columns above? If not, double‑check that you’re in the correct Notion workspace and that the “Table – Inline” block is selected.

---

### 2. Create a Client Intake Form in Google Forms  
2.1 Visit https://forms.google.com.  
2.2 Click **Blank** to start a new form.  
2.3 Title the form **“Client Onboarding – AI Social Media Consulting”**.  
2.4 Add the following fields (use the exact field types):  
- **Short answer** – “Client Name”  
- **Email** – “Client Email”  
- **Short answer** – “Brand Name”  
- **Multiple choice** – “Desired Social Platforms” (options: Instagram, Facebook, LinkedIn, TikTok, Twitter)  
- **Paragraph** – “Current Social Media Challenges”  
- **File upload** – “Brand Assets (logo, colors, guidelines)”  

2.5 At the top right, click **Settings** (gear icon).  
2.6 Under **General**, enable **Collect email addresses**.  
2.7 Under **Presentation**, check **Show progress bar**.  
2.8 Click **Save**.  
2.9 Copy the **Form URL** (top bar “Send” → link icon → click **Copy**).  

2.10 In Notion, embed the form by typing “/embed” and pasting the URL.  

*Check‑in:* Do you see the embedded form in Notion? If not, ensure the form’s sharing settings allow “Anyone with the link can respond”.  

---

### 3. Build the AI Content Generation Workflow in Make.com  
3.1 Open **Make.com** (https://www.make.com).  
3.2 Click **Create a new scenario**.  
3.3 Search for the **Google Forms** module and drag it onto the canvas.  
3.4 Click **Add a new connection** → choose the form you created → **Continue**.  
3.5 Select **Watch new responses** as the trigger.  
3.6 Drag the **ChatGPT** module (from “OpenAI”) to the right of the trigger.  
3.7 Connect the output of Google Forms to ChatGPT.  
3.8 Click **Set up the module** → choose **“Completions”**.  
3.9 In the **Prompt** field, paste:  
```
You are a social media strategist. Generate a 30‑day content calendar for a brand named {{Brand Name}} targeting {{Desired Social Platforms}}. Include post titles, captions, and suggested hashtags. Format as a table with columns: Day, Platform, Post Type, Caption, Hashtags.  
```  
3.10 Set **Model** to **gpt‑4o-mini** (free tier available).  
3.11 Set **Max tokens** to 600.  
3.12 Drag the **Buffer** module onto the canvas (search “Buffer”).  
3.13 Connect ChatGPT’s output to Buffer’s **Create a new post** module.  
3.14 In Buffer, set **Account** to the Buffer account you’ll create below.  
3.15 Map **Text** to

---

## Procedure 8.2: **Set Up Subscription Tiers on Shopify**

1. **Create a Shopify Store**  
   - Open a browser and go to **https://www.shopify.com**.  
   - Click the **bold button** **“Start free trial”**.  
   - Fill in **Email** (your business email), **Password** (choose a strong password), and **Store name** (“Menshly AI Subs”).  
   - Click **bold button** **“Create my store”**.  
   - You should see the Shopify admin dashboard with a welcome banner “**Welcome to Shopify**”.  

2. **Purchase a Shopify Plan**  
   - In the left‑hand menu, click **bold button** **“Settings”** → **“Plan”**.  
   - Click **bold button** **“Change plan”**.  
   - Select **“Basic Shopify” ($29.00/month)**.  
   - Click **bold button** **“Continue to checkout”**.  
   - Enter billing details and click **bold button** **“Start plan”**.  
   - Expected output: “**Your plan is now active**” banner appears.  

3. **Install Recharge Subscriptions App**  
   - In the Shopify admin, go to **Apps** → **bold button** **“Visit the Shopify App Store”**.  
   - Search for **“Recharge Subscriptions”**.  
   - Click **bold button** **“Add app”** on the Recharge listing.  
   - Click **bold button** **“Install app”**.  
   - You will be redirected to **https://rechargepayments.com**.  
   - Click **bold button** **“Start free trial”** (30‑day trial).  
   - On the next page, click **bold button** **“Connect to Shopify”** and authorize the app.  

4. **Create a Subscription Product**  
   - In Shopify admin, click **bold button** **“Products”** → **bold button** **“Add product”**.  
   - Enter **Title** “Menshly AI Monthly Subscription”.  
   - In **Description**, paste:  
     > “Get exclusive AI‑powered content delivered to your inbox every month. Choose from 3 tiers: Basic, Pro, and Enterprise.”  
   - Click **bold button** **“Add image”** to upload a placeholder image.  
   - Under **Pricing**, set **Price** $9.99.  
   - Scroll to **“Inventory”** section, ensure **“Track quantity”** is **off**.  
   - Click **bold button** **“Save”**.  

5. **Enable Subscription for the Product**  
   - After saving, you’ll be on the product page.  
   - In the right‑hand panel, find **“Recharge”** section.  


## Check-In: Module 8 Complete

- [ ] Create a High‑Ticket Consulting Package completed and verified
- [ ] **Set Up Subscription Tiers on Shopify** completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 9: FINANCIAL OPERATIONS

## Overview

In Module 9 you will master the financial backbone of your AI‑driven social media service. We cover revenue tracking, dynamic pricing, and proposal/contract creation so you can bill accurately, justify rate hikes, and protect yourself legally. By building a live financial dashboard you will instantly see cash flow, margin, and profitability across every client. You will also learn to automate proposal generation with Make.com and Buffer, ensuring that every pitch looks professional and every contract is enforceable. Skipping this module leaves you exposed to mis‑priced services, revenue leakage, and contract disputes that can halt your growth.

If you bypass revenue tracking, you will never know which clients are profitable or which campaigns consume more resources than they return. Ignoring pricing strategy means you’ll under‑charge early, then scramble to hike rates later, damaging client trust. Without a standardized proposal template you’ll waste time customizing each offer, increasing error risk and decreasing win rates. A weak contract system exposes you to non‑payment or scope‑creep issues that can drain your time and profits.

You will build a complete financial dashboard in Notion, set up automated invoicing in Klaviyo, and create scalable proposal templates in Make.com that pull client data from Buffer. By the end of this module you’ll have a repeatable, auditable financial workflow that scales as your client base grows.

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| **Make.com** | Automate data feeds for revenue dashboards | 1,000 operations/month | $19/month (Starter) |
| **Buffer** | Publish and schedule social posts, track engagement for invoicing | Basic plan – 3 social accounts | $12/month (Pro) |
| **Notion** | Central financial dashboard, client records, proposal templates | Unlimited pages, 1,000 blocks | $8/month per user (Personal Pro) |
| **Klaviyo** | Send automated invoices & payment reminders | 250 contacts | $20/month (Starter) |
| **Zapier** | Bridge between Buffer, Make.com, and accounting tools | 100 tasks/month | $19.99/month (Starter) |

**Estimated Time to Complete:** 4–5 hours (including data setup, template creation, and testing).

---

## Procedure 9.1: Build a Live Revenue Dashboard in Notion with Make.com

1. **Open a web browser** and navigate to `https://www.notion.so/`.  
2. **Sign in** with your email or use the “**Sign in with Google**” button.  
3. In the left‑hand sidebar, click the **“**+ New page**”** button at the bottom.  
4. In the modal that appears, enter **“Revenue Dashboard”** as the page title, select **“Database – Table”** as the template, then click **“**Create**”**.  
   - **Expected output**: A new Notion page opens with an empty table named “Revenue Dashboard”.  
   - **Check‑in**: Do you see a table with columns “Name”, “Tags”, “Created time”, and “Last edited time”? If not, refresh the page or re‑create the page.  

5. Click on the **“+ Add a property”** button (top‑left of the table).  
6. In the property menu, choose **“Date”** as the property type, name it **“Date”**, and click **“**Create**”**.  
7. Repeat step 5, this time selecting **“Number”** as the property type, name it **“Amount”**, set the format to **“Currency”** (choose USD), and click **“**Create**”**.  
8. Add a third property: click **“+ Add a property”**, choose **“Text”**, name it **“Source”**, and click **“**Create**”**.  
   - **Check‑in**: Do you now see three custom columns: Date, Amount, Source? If not, delete the last column and re‑add it.  

9. Click the **three‑dot menu** (…) next to the table’s name, select **“**Duplicate**”** to create a copy titled “Revenue Dashboard – Backup”.  
10. Go back to the original table, click the **“**…**”** button again, and choose **“**Export**”** → **“CSV”**. Save the file to your desktop.  
    - **Expected output**: A CSV file “Revenue Dashboard – Backup.csv” containing the table’s schema.  

11. Open a new browser tab and go to `https://www.make.com/en`.  
12. Click **“**Sign up free**”** at the top‑right, fill in your email, password, and confirm.

---

## Procedure 9.2: Create Proposal Templates and Automated Billing with Stripe

1. **Open Stripe Dashboard**  
   - Go to **https://dashboard.stripe.com/login**.  
   - Click **Sign in** with your email and password.  
   - After login, you should see the **Stripe Dashboard** home screen with the **“Customers”** tab highlighted on the left.  

   *Do you see the Stripe Dashboard with the “Customers” side‑nav? If not, ensure you are logged into the correct Stripe account and that your browser is not blocking pop‑ups.*

2. **Create a New Customer for the Client**  
   - In the left menu, click **Customers** (bold).  
   - Click the **“+ New”** button in the top right corner.  
   - Fill in **Name**: “Client Name”.  
   - Fill in **Email**: “client@example.com”.  
   - Click **Create customer** (bold).  

   *Expected output*: A modal pops up confirming “Customer created successfully.” The new customer appears in the list.

3. **Add a Product for the Proposal**  
   - In the left menu, click **Products** (bold).  
   - Click **“+ New”**.  
   - Set **Product name**: “Social Media AI Package”.  
   - Set **Description**: “Automated AI‑driven social media workflow using Buffer and Make.com.”  
   - Under **Pricing**, click **“Add price”**.  
   - Choose **“One‑time”**.  
   - Set **Unit amount**: 15000 (USD).  
   - Set **Currency**: USD.  
   - Click **Save product** (bold).  

   *Do you see the product “Social Media AI Package” listed under Products? If not, confirm you are in the correct Stripe account.*

4. **Create a Proposal PDF with Canva**  
   - Open **Canva** at **https://www.canva.com**.  
   - Click **“Create a design”** → **“Custom size”** → Width = 800 px, Height = 1125 px.  
   - Click **“Elements”**, search for “invoice template”, and drag one onto the canvas.  
   - Replace placeholder text with:  
     - **Client**: “Client Name”  
     - **Project**: “Social Media AI Workflow”  
     - **Description**: “Automated posting with Buffer, AI content generation via Make.com, and analytics.”  
     - **Price**: **$150.00**  
   - Click **“Download”** → **PDF – Print**.  
   - Save the file as **Proposal_Client‑Name.pdf** on your desktop.  

   *At this point you should have a PDF proposal ready to attach.*

5. **Upload Proposal to Stripe as a File**  
   - Return to the **Stripe Dashboard**.  
   - In the left menu, click **Settings** (gear icon).  
   - Under **Platform**, click **File uploads** → **Upload**.  
   - Drag **Proposal_Client‑Name.pdf** or click **Select a file** and choose it.  
   - Click **Upload** (bold).  

   *Do you see the file listed under “Uploaded files” with a status of “complete”? If not, ensure the file size is under 5 MB (Stripe limit).*

6. **Create a One‑time Invoice**  
   - In the left menu, click **Invoices** → **+ New**.  
   - Select the customer “Client Name”.  
   - In the **Invoice items** section, click **Add item** → choose **Social Media AI Package**.  
   - Ensure the amount is **$150.00**.  
   - Under **Add file**, click **Attach** → choose the uploaded proposal PDF.  
   - Click **Save draft** (bold).  

   *Expected output*: Invoice shows “Draft” status with the attached PDF.  

7. **Send the Invoice via Email**  
   - In the invoice preview, click **Send** (bold).  
   - In the recipient field, confirm the email is “client@example.com”.  
   - Add a subject: “Social Media AI Workflow Proposal – Invoice”.  
   - Click **Send email** (bold).  

   *Do you see the email status “sent” in the invoice history? If not, check the email address and spam folder.*

8. **Set Up Stripe Billing for Recurring Monthly Service**  
   - In the left menu, click **Billing** → **Subscriptions**.  
   - Click **+ New** → **Create subscription**.  
   - Choose the same customer “Client Name”.  
   - Click **Add plan** → **Create a new plan**.  
   - Set **Plan name**: “Monthly AI Social Media Service”.  
   - Set **Billing period**: Monthly.  
   - Set **Amount**: 7500 (USD).  
   - Set **Currency**: USD.  
   - Click **Save** (bold).  

   *At this point you should see a subscription card with “Active” status.*

9. **Link Subscription to Make.com for Automation**  
   - Open **Make.com** at **https://www.make.com**.  
   - Sign in or create an account (free tier: 1000 operations/month).  
   - Click **Create a new scenario** (bold).  
   - Search for “Stripe” in the module library and drag the **Stripe > New Payment** trigger onto the canvas.  
   - Connect your Stripe account by clicking **Add new connection** → paste the **Secret Key** from **https://dashboard.stripe.com/apikeys**.  
   - Set **Event type**: “invoice.payment_succeeded”.  

   *Expected output*: Trigger is saved and ready to run.  



## Check-In: Module 9 Complete

- [ ] Build a Live Revenue Dashboard in Notion with Make.com completed and verified
- [ ] Create Proposal Templates and Automated Billing with Stripe completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 10: LAUNCH PLAN

## Overview  
This module delivers the precise, day‑by‑day execution calendar that turns a blank‑sheet social media automation strategy into a live, revenue‑generating service within 30 days. You’ll learn how to set up AI‑driven content pipelines with Make.com, schedule and optimize posts in Buffer, and bundle everything into a repeatable service you can pitch to prospects. Each day is broken into actionable tasks—no guesswork, no wasted time—so you can move from zero knowledge to your first paying client without over‑engineering or costly trial runs.

Skipping this module means you’ll struggle to translate your technical know‑how into a tangible, marketable offering. Without the step‑by‑step calendar, you risk spending weeks troubleshooting isolated problems instead of focusing on client acquisition and revenue. The launch plan ensures you meet the critical milestones that attract paying clients: a polished workflow, a demo-ready portfolio, and a proven pricing structure ready to roll out.

**Tools you’ll need (exact names, free‑tier limits, and paid‑tier entry points):**

| Tool          | Purpose                                        | Free Tier                           | Paid Tier (Entry Point) |
|---------------|------------------------------------------------|-------------------------------------|------------------------|
| Make.com      | Automate content creation & scheduling         | 500 operations/month, 2 000 000 API calls | €15/month (Basic)     |
| Buffer        | Schedule, publish, and analyze social posts    | 10 scheduled posts per account      | €12/month (Pro)       |
| Notion        | Project calendar & documentation              | Unlimited pages, 1 000 blocks      | €4/month (Personal)   |
| Canva         | Design eye‑catching visuals for posts          | Unlimited designs, 5 GB storage     | €12/month (Pro)       |
| Zapier        | Connect Buffer to external tools (optional)    | 100 tasks/month                    | $19/month (Starter)   |
| ChatGPT (OpenAI) | Generate copy, captions, and AI‑enhanced content | 3 000 tokens/month (free)          | $20/month (ChatGPT‑Plus) |

**Estimated time to complete Module 10:**  
- Reading & planning: 1 h  
- Tool setup & initial automation build: 2 h  
- Daily execution calibration (30 days) + review: 3 h  
- Total: **≈ 6 hours** (spread over the 30‑day launch period)

By the end of this module, you will have a fully automated, AI‑powered social media workflow that is ready to be pitched and sold to clients, giving you a clear path from zero to first‑payment in just one month.

---

## Procedure 10.1: Configure Demo Scheduling with Calendly and Notion

1. **Open your browser and navigate to Calendly**  
   URL: `https://calendly.com/`  
   Click the **Sign up** button in the top‑right corner.  
   *Expected output:* A sign‑up form with fields for **Name**, **Email**, and **Password**.

2. **Create a Calendly account**  
   - Fill in the form:  
     - Name: *Your Full Name*  
     - Email: *you@example.com*  
     - Password: *StrongPassword123!*  
   Click **Create account**.  
   *Expected output:* You are redirected to the Calendly dashboard.

3. **Verify your email**  
   Check your inbox for a verification email from Calendly.  
   Click the **Verify** link.  
   *Expected output:* A confirmation page that says “Your email has been verified.”  

4. **Login to Calendly**  
   In the browser, go to `https://calendly.com/` again.  
   Click **Login**, enter your credentials, and click **Login**.  
   *Expected output:* You land on the calendar overview page.

5. **Create a new event type**  
   - Click the **+ New event type** button.  
   - Choose **One‑on‑one**.  
   - Click **Continue**.  
   *Interactive check‑in:* Do you see the **Event name** field? If not, refresh the page and ensure you are logged in.

6. **Configure the event details**  
   - Event name: **Demo Scheduling**  
   - Description: *“Schedule a live demo with our AI social media workflow.”*  
   - Location: **Zoom** (or **Google Meet**) – choose from the dropdown.  
   - Duration: **30 minutes**.  
   Click **Continue**.  
   *Expected output:* You see the **Invitee questions** screen.

7. **Set availability**  
   - Click **Edit availability**.  
   - Select **Custom** schedule.  
   - Set working hours: **Mon‑Fri 9:00‑17:00** (Pacific Time).  
   - Click **Save**.  
   *Interactive check‑in:* Do you see a calendar grid with the selected hours highlighted? If not, ensure you saved changes.

8. **Enable automatic buffer**  
   - In the event settings, toggle **Add buffer before** to `15` minutes.  
   - Toggle **Add buffer after** to `15` minutes.  
   Click **Save**.  
   *Expected output:* The event details page now shows buffer times.

9. **Publish the event**  
   Click the **Publish** button in the top‑right corner.  
   *Expected output:* A modal shows “Event published” and a link to the event.

10. **Copy the event link**  
    - In the publish modal, click **Copy link**.  
    - Paste the link into a clipboard manager or note.

---

**Procedure 10.2** — Generation failed due to AI backend unavailability. Please retry later.

---

## Procedure 10.3: Execute the 30‑Day Launch Calendar  

**Goal:** Populate Buffer with a fully automated 30‑day social‑media schedule that pulls AI‑generated content from Make.com, ensuring daily posts across chosen platforms without manual intervention.

---

### 1. Log into Buffer  
- Open your browser and go to **https://buffer.com/login**.  
- Click **“Log in”** in the upper‑right corner.  
- Enter your **email** and **password** exactly as saved.  
- Click the **bold button** **“Log in”**.  
- **Expected output:** You land on the Buffer dashboard with “Add your first account” highlighted.

**Check‑in:** Do you see the Buffer dashboard with the “Add your first account” prompt?  
If not, verify you are logged into the correct email and that no pop‑up blockers are active.

### 2. Add the first social account  
- Click **“Add an account”** under “Social accounts”.  
- Choose **“Twitter”** from the list and click **bold button** **“Connect”**.  
- Authorize Buffer to access your Twitter account.  
- After authorization, you’ll see **“Twitter (username)”** listed.  
- **Expected output:** Twitter appears under “Social accounts” with a green checkmark.

**Check‑in:** Do you see your Twitter account listed?  
If not, re‑authorize by clicking **“Re‑authorize”** next to the account.

### 3. Create a content calendar view  
- In the left sidebar, click **“Plan”**.  
- Click the **bold button** **“Create new calendar”**.  
- Name it **“30‑Day Launch Calendar”** and press **bold button** **“Create”**.  
- The calendar view now shows 30 columns labeled 1‑30.  
- **Expected output:** A blank 30‑day grid with column headers “Day 1” to “Day 30”.

**Check‑in:** Are 30 columns displayed?  
If you only see 15, refresh the page and ensure you’re in the **“Plan”** tab.

### 4. Connect Make.com to Buffer via Zapier  
- Open a new tab and go to **https://zapier.com/app/dashboard**.  
- Click **bold button** **“Make a Zap”**.  
- In the **Trigger** app search, type **“Make”** and select **Make.com**.  
- Choose the trigger event **“New Scenario Run”**.  
- Click **bold button** **“Continue”**.  
- Sign in to Make.com (https://www.make.com) with your credentials.  
- Authorize Zapier to read your Make.com scenarios.  
- **Expected output:** Zapier lists your Make.com scenarios under “Choose a trigger”.

**Check‑in:** Do you see your Make.com account connected in Zapier?  
If not, click **“Reconnect”** and follow the authentication flow again.

### 5. Set up the Make.com scenario for AI content generation  
- In Make.com (https://www.make.com), click **bold button** **“Create new scenario”**.  
- Add a **“OpenAI”** module → **“Generate text”**.  
- Configure the prompt: “Generate a 280‑character tweet about [your niche] for day X.”  
- Add a **“Formatter”** → **“Text”** → **“Extract JSON”** to pull out the tweet text.  
- Add a **“Buffer”** module → **“Create a post”**.  
- Map the extracted text to **“Message”** and set **“Social account”** to your Twitter handle.  
- Set **“Publish date”** to the current date + X days (use a **“Date & Time”** module to calculate).  
- Click **bold button** **“Save”**.  
- Run the scenario once to test.  
- **Expected output:** A single tweet appears in Buffer’s “Drafts” with the correct content.

**Check‑in:** Do you see a new tweet in Buffer Drafts?  
If not, verify the OpenAI API key and that the Buffer module has the correct account selected.

### 6. Automate the scenario to run daily  
- In Make.com, click **bold button** **“Schedule”** next to your scenario.  
- Set frequency to **“Every 24 hours”** and start time to **00:00 UTC**.  
- Click **bold button** **“Save”**.  
- **Expected output:** Scenario shows “Schedule: Daily at 00:00 UTC”.

**Check‑in:** Is the schedule active?  
If not, toggle the **“Enable”** switch to on.

### 7. Create a 30‑day Make.com trigger list  
- In Make.com, create a second scenario titled **“30‑Day Trigger”**.  
- Add a **“Numbers”** module → **“Generate a sequence”**.  
- Set start to **1**, end to **30**, step **1

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
| **Make.com** | Visual automation platform (formerly Integromat) | 1 000 operations/month, 10 GB data transfer | $49 /month for 5 000 ops, 50 GB transfer | When your Buffer‑to‑Google‑Sheets sync exceeds 1 000 ops or you need premium connectors (e.g., Webhooks, HTTP, premium HTTP) |
| **Buffer** | Social‑media scheduling & analytics | 3 social accounts, 10 scheduled posts per account | $15 /month for 8 accounts, 100 posts per account | When you need more than 3 accounts or >10 posts per account, or require advanced analytics |
| **Google Workspace** | Email, Drive, Docs, Sheets, Admin console | Trial 14 days, no permanent free tier | Business Starter $6 /user/month (1 TB per user) | When you need a dedicated domain email or more than 14 days of trial |
| **Notion** | Knowledge base, project tracker, database | Unlimited pages, blocks, guests | Team $8 /user/month (collaboration tools) | When you need shared workspaces, advanced permissions, or API access |
| **ChatGPT API** | Generating AI content, chatbots | 3 000 tokens/month credit | $0.002 /1 000 tokens (GPT‑3.5) or $0.03 /1 000 tokens (GPT‑4) | When your content volume exceeds free credit or you require GPT‑4 |
| **Vapi** | Voice‑to‑text transcription & speech‑to‑text | 100 calls/month, 30 min total | $0.01 /minute + $0.10 /100 calls | When daily transcription >100 calls or >30 min |
| **ElevenLabs** | Text‑to‑speech (TTS) | 30 min audio/month | $20 /month for 1 000 min | When you need >30 min of generated audio per month |
| **Apollo.io** | Lead sourcing & outreach automation | 100 credits/month | $39 /month (Starter) | When you need >100 outreach actions per month or advanced filters |
| **Klaviyo** | Email marketing & automation | 250 contacts | $20 /month (500 contacts) | When contacts >250 or you need advanced segmentation |
| **Hostinger** | Web hosting & domain registration | No free tier | Shared Hosting $1.99 /month | When you need a live production server |
| **Shopify** | E‑commerce storefront | 14‑day free trial | Basic Shopify $39 /month | When you need to create a paid subscription page or store |
| **Zapier** | Connect apps & automate workflows | 100 tasks/month | Starter $19.99 /month (750 tasks) | When tasks >100/month or you need premium connectors |
| **Calendly**

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

This appendix is an operating‑system‑level playbook that will let you build, run, and validate the financial model for your AI‑driven social‑media service. Every step is concrete, every value is explicit, and every tool is named with its exact pricing tier. Follow the instructions exactly; the calculator will be your single source of truth for revenue, profit, and break‑even analysis.

---

## 1. Create the Core Spreadsheet

1. **Open Google Sheets**  
   - URL: `https://docs.google.com/spreadsheets/`.  
   - Click **New** → **Google Sheets**.  
2. **Rename the file**  
   - Click the default title (“Untitled spreadsheet”) and type `Menshly Revenue Calculator – 2026`.  
   - Do you see the new title? If not, refresh the page.  
3. **Insert three sheets**  
   - Click the `+` icon at the bottom left.  
   - Rename the first sheet `Projections`, the second `Pricing`, the third `BreakEven`.  
4. **Freeze the first row in each sheet**  
   - In `Projections`, select row 1 → `View` → `Freeze` → `1 row`.  
   - Repeat for `Pricing` and `BreakEven`.  

> **Error Scenario:**  
> If `View` → `Freeze` is missing, you are on the new Google Sheets UI. Click the three‑dot menu → `View options` → enable `Freeze`.  

---

## 2. Revenue Projection Template (Sheet: **Projections**)

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| **Month** | **Revenue** | **Clients** | **Expenses** | **Profit** | **Cumulative Profit** |
| 1 | `=Clients_A1*Price_A1` | `=Clients_A1` | `=Expenses_A1` | `=Revenue_A1-Expenses_A1` | `=Profit_A1` |
| 3 | `=Clients_B1*Price_B1` | `=Clients_B1` | `=Expenses_B1` | `=Revenue_B1-Expenses_B1` | `=CumulativeProfit_B1+Profit_B1` |
| 6 | `=Clients_C1*Price_C1` | `=Clients_C1` | `=Expenses_C1` | `=Revenue_C1-Expenses_C1` | `=CumulativeProfit_C1+Profit_C1` |
| 12 | `=Clients_D1*Price_D1` | `=Clients_D1` | `=Expenses_D1` | `=Revenue_D1-Expenses_D1` | `=CumulativeProfit_D1+Profit_D1` |

> **Step‑by‑Step Instructions**  
> 1. In cell `A2`, type `1`.  
> 2. In cell `A3`, type `3`.  
> 3. In cell `A4`, type `6`.  
> 4. In cell `A5`, type `12`.  
> Do you see the month numbers 1, 3, 6, 12? If not, check that you are editing column A.  

> 5. In cell `B2`, type `=Clients_A1*Price_A1`.  
> 6. In cell `B3`, type `=Clients_B1*Price_B1`.  
> 7. In cell `B4`, type `=Clients_C1*Price_C1`.  
> 8. In cell `B5`, type `=Clients_D1*Price_D1`.  
> Do you see formulas starting with `=`? If the formulas display as text, change the cell format to `Automatic`.  

> 9. In cell `E2`, type `=B2-D2`.  
> 10. In cell `E3`, type `=B3-D3`.  
> 11. In cell `E4`, type `=B4-D4`.  
> 12. In cell `E5`, type `=B5-D5`.  
> Do you see the profit values updating? If any cell shows `#VALUE!`, ensure that the referenced cells contain numeric data.  

> 13. In cell `F2`, type `=E2`.  
> 14. In cell `F3`, type `=F2+E3`.  
> 15. In cell `F4`, type `=F3+E4`.  
> 16. In cell `F5`, type `=F4+E5`.  
> Do you see a growing cumulative profit column? If `F5` is `#REF!`, check that prior cells are numeric.  

> **Expected Output**  
> When you input sample numbers (see Section 3), the sheet should display:  

``

For the free step-by-step guide, see our [implementation guide]({< ref "/intelligence/build-an-automate-streamline-and-scale-ngo-operations-with-makecom-with-chatgpt-.md" >}).


## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
- **[Semrush](https://www.semrush.com/)** — All-in-one SEO and marketing toolkit — keyword research, audits, rank tracking
