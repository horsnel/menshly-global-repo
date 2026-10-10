---
title: "APPENDIX A: COMPLETE TOOL REFERENCE"
date: 2026-10-10
category: "Playbook"
price: "₦25,000"
readTime: "88 MIN"
excerpt: "This is your complete operating system for Create, optimize, and deploy AI customer onboarding workflows with Calendly and Klaviyo. The AI Playbook: 25 Steps to $25K/Month. 25 procedures. 10 modules. 12+ hours of reading and execution. Follow every p..."
image: "/images/articles/playbooks/appendix-a-complete-tool-reference.png"
heroImage: "/images/heroes/playbooks/create-optimize-and-deploy-ai-customer-onboarding-workflows-with-calendly-and-kl.png"
relatedOpportunity: "/opportunities/how-to-build-an-ai-customer-onboarding-service-3k-6kmonth/"
relatedGuide: "/intelligence/build-an-ai-bookkeeping-automation-with-zapier-the-complete-step-by-step-guide/"
---
This is your complete operating system for Create, optimize, and deploy AI customer onboarding workflows with Calendly and Klaviyo. **The AI Playbook: 25 Steps to $25K/Month.** **25 procedures. 10 modules. 12+ hours of reading and execution.** Follow every procedure in order and you will have a fully operational business generating revenue within 30 days. Skip nothing. Every step exists because someone before you failed by skipping it.

---

# MODULE 1: FOUNDATION

## Overview  
Module 1 lays the essential groundwork for creating, optimizing, and deploying AI‑driven customer onboarding workflows that marry Calendly’s scheduling intelligence with Klaviyo’s email automation. By establishing a clean, authenticated infrastructure first, you eliminate late‑stage friction that can derail campaign performance, inflate costs, and erode trust with your clients. A solid foundation guarantees that every subsequent workflow triggers correctly, data flows seamlessly between services, and you can audit every step of the onboarding journey.

Skipping this module means you’ll confront “unknown variable” errors in Make.com, broken webhook URLs, or GDPR‑compliant data handling gaps—all of which can trigger bounce rates, duplicate emails, and lost revenue. Moreover, without a properly registered domain and verified email list, Klaviyo will flag your messages as spam, and Calendly invites will fail to render. By dedicating time now to verify every link, API key, and DNS record, you secure a reliable launchpad that scales effortlessly as you add new clients or expand feature sets.

| Tool          | Purpose                                 | Free Tier                                         | Paid Tier                                 |
|---------------|------------------------------------------|---------------------------------------------------|-------------------------------------------|
| Calendly      | Appointment scheduling & event hooks    | 1 calendar, 5 events/month, basic integrations   | Pro: $10/mo (per user), Unlimited events |
| Klaviyo       | Email automation & segmentation         | 500 contacts, 3,000 emails/mo, basic templates   | Growth: $20/mo (500-2,500 contacts)      |
| Make.com      | Workflow automation & API connectors    | 100 operations/month, 5 active scenarios          | Starter: $9/mo (1,000 ops/month)         |
| Notion        | Project & docs management                | Unlimited pages, 5 guests                         | Team: $8/mo (per user)                   |
| Hostinger     | Domain & hosting                         | 1 free domain with 50GB space, 1 email           | Premium: $1.99/mo (unlimited domains)    |

**Estimated time to complete:** 1 hour 30 minutes. This includes account creation, domain DNS setup, email verification, and initial tool integrations.



---

**Support Pollinations.AI:**

---

🌸 **Ad** 🌸
Powered by Pollinations.AI free text APIs. [Support our mission](https://pollinations.ai/redirect/kofi) to keep AI accessible for everyone.

---

## Procedure 1.1: REGISTER YOUR BUSINESS DOMAIN ON HOSTINGER

1. Open a web browser and go to **https://www.hostinger.com/**.  
2. Click the **bold button** **“Get Started”** in the upper‑right corner.  
3. On the signup page, select **“Create an account”** and fill the form:  
   * **Email**: your business email (e.g., johndoe@yourbiz.com)  
   * **Password**: a strong password (min 8 chars, mix of letters, numbers, symbols)  
   * **Confirm password**: re‑type the same password  
4. Click **“Create account”**.  
   *Expected output*: You should see a verification email sent to your inbox.  
   *Do you see the “Verify your email” page? If not, check the spam folder and click the “Resend” link.*

5. Open the verification email, click **“Verify Email”**.  
6. Return to the browser, you should now be logged into the Hostinger dashboard.  
7. In the dashboard sidebar, click **“Domains”** → **“Register a Domain”**.  
8. In the search box, type your desired domain (e.g., **yourbiz.com**) and click **“Search”**.  
   *Expected output*: List of available domain names and prices.  
   *Do you see the domain price list? If not, clear your browser cache and refresh.*

9. If your chosen domain is available, click **“Add to Cart”** next to it.  
10. On the cart page, verify the domain name, then click **“Proceed to Checkout”**.  
11. In the checkout form, fill:  
    * **Name**: Your full legal name  
    * **Address**: Street, City, State/Province, Zip, Country  
    * **Phone**: +1‑555‑123‑4567 (or local code)  
12. Choose the **1‑year** term (default) and click **“Continue”**.  
    *Expected output*: Summary of order and total cost.  
    *Do you see the order summary? If not, ensure all fields are filled and click “Continue” again.*

13. Select a payment method:  
    * **Credit Card** – enter card number, expiry, CVV, billing zip.  
    * **PayPal** – you will be redirected to PayPal to approve payment.  
    *For this procedure, use **Credit Card**.  
14. Click **“Pay Now”**.  
15. Once payment is processed, you will see a confirmation page that says **“Domain Successfully Registered!”** and a confirmation email will be sent.  

**Error Scenario**  
If you see **“Domain registration failed – unavailable”** after clicking “Add to Cart”, this means the domain was already taken by another registrar in the interim.  
*Fix it by:*  
   1. Returning to the search page (step 8).  
   2. Selecting a slightly different domain (e.g., **yourbiz.co.uk**).  
   3. Repeating steps 9‑15.  

16. Return to the Hostinger dashboard, click **“Domains”** → **“Manage”**.  
17. Locate your newly registered domain and click the **“Manage”** button.  
18. In the domain management panel, click **“DNS Settings”** → **“Edit DNS Records”**.  
19. Add the following A record:  
    * **Type**: **A** (select from dropdown)  
    * **Host**: **@**  
    * **Points to**: **216.239.37.21** (Hostinger’s default IP for shared hosting)  
    * **TTL**: **3600** (1 hour)  
    Click **“Save”**.  
    *Expected output*: Confirmation “DNS record added successfully.”  

20. Click **“Add Record”** again to create a **CNAME** for www:  
    * **Type**: **CNAME**  
    * **Host**: **www**  
    * **Points to**: **@**  
    * **TTL**: **3600**  
    Click **“Save”**.  
    *Do you see the new DNS records listed? If not, wait a few minutes for propagation or clear the cache.*  

**TABLE: HOSTINGER DOMAIN REGISTRATION COST BREAKDOWN**  

| Domain Extension | 1‑Year Price | 2‑Year Price | 3‑Year Price | Free Tier (with Hosting) |
|-------------------|--------------|--------------|--------------|--------------------------|
| .com | $10.99 | $19.98 | $29.97 | $0 (if you purchase a hosting plan) |
| .net | $12.99 | $23.96 | $35.95 | $0 (with Hosting) |
| .biz | $9.99 | $18.98 | $28.97 | $0 (with Hosting) |
| .co | $13.99 | $25.98 | $37.97 | $0 (with Hosting) |

**Affiliation Integration Tip**  
After domain registration, automate

---

## Procedure 1.2: Set Up Email and Workspace in Notion

1. **Open your web browser** and navigate to the Notion sign‑up page:  
   `https://www.notion.so/signup`.

2. **Click the button labeled “+ Create free account”** (it is a blue button in the upper‑right corner).

3. **Enter your personal email address** in the field that says “Enter your email”.  
   *Example*: `john.doe@example.com`.  
   Click **“Continue with Email”**.

4. **Create a strong password** in the field “Password”. Use at least 12 characters, mix of upper/lower case, numbers, and symbols.  
   Click **“Create password”**.

5. **Verify your email**: Open your inbox, locate the email from Notion titled “Welcome to Notion”, and click **“Verify Email”** inside the email.  
   Do you see the confirmation message “Your email has been verified”? If not, check the spam folder and repeat step 4.

6. **Return to the browser and refresh the Notion page**. The site should now display the “Create Workspace” prompt.  
   Click **“Create a new workspace”**.

7. **Name your workspace** in the field “Workspace name”.  
   *Example*: `Menshly Onboarding Hub`.  
   Click **“Next”**.

8. **Choose a primary purpose**: select **“For myself”** (you can change it later).  
   Click **“Next”**.

9. **Select a plan**: click the button that says **“Free”** to start with the free tier.  
   Click **“Start free”**.

10. **Configure workspace branding**:  
    - Upload a logo by clicking the **“Upload logo”** button, then select an image file (`logo.png`).  
    - Set the workspace color by clicking the **“Choose color”** dropdown and selecting **“Blue”**.  
    - Click **“Save”**.  
    Do you see the new logo and blue theme? If not, re‑upload the logo and confirm the color selection.

11. **Invite your team (optional)**: In the left sidebar, click **“Share”** (top‑right of the workspace).  
    - In the invite field, type your partner’s email (`partner@example.com`).  
    - Set permission to **“Can edit”**.  
    - Click **“Invite”**.  
    Do you see the message “Invitation sent”? If not, ensure the email format is correct.

12. **Create a new page for onboarding**:  
    - In the left sidebar, click **“+ New Page”**.  
    - Title the page **“Client Onboarding Flow”**.  
    - Click **“Add icon”**, choose a simple icon (e.g., a briefcase), and click **“Save”**.  
    Expected outcome: A blank page titled “Client Onboarding Flow” appears.

13. **Add a table database**:  
    - In the page, type `/table` and select **“Table – Inline”**.  
    - Name the table **“Client Leads”**.  
    - Add columns:  
      - **Name** (default).  
      - **Email** (type: “Email”).  
      - **Status** (type: “Select”; options: “New”, “Contacted”, “Onboarded”).  
      - **Calendly Link** (type: “URL”).  
    Expected outcome: A table with four columns appears.

14. **Set up a Gmail account for automated emails**:  
    - Go to `https://mail.google.com/`.  
    - Click **“Create account”** (button in the upper‑right).  
    - Follow the prompts to set up a free Gmail account (`onboarding@menshly.com`).  
    - Enable **“Allow less secure apps”** in the account settings (Settings → Security → Less secure app access → Turn on).  
    Expected outcome: Email account ready for SMTP use.

15. **Create an SMTP relay in [Replit](https://replit.com/refer/egwuokwor)**:  
    - Visit `https://replit.com/` and sign up for a free account.  
    - Create a new Repl, choose “Python” template.  
    - Install the `smtplib` library (already built‑in).  
    - Add the following code snippet to `main.py`:

      ```python
      import smtplib
      from email.mime.text import MIMEText

      smtp_server = "smtp.gmail.com"
      smtp_port = 587
      smtp_user = "onboarding@menshly.com"
      smtp_password = "YOUR_APP_PASSWORD"

      msg = MIMEText("Welcome to Menshly!")
      msg['Subject'] = 'Onboarding Started'
      msg['From'] = smtp_user
      msg['To'] = 'client@example.com'

      with smtplib.SMTP(smtp_server, smtp_port) as server:
          server.starttls()
          server.login(smtp_user, smtp_password)
          server.sendmail(smtp_user, [msg['To']], msg.as_string())
      ```

    - Replace `YOUR_APP_PASSWORD` with the App Password you generate in Gmail (Settings → Security → App passwords).  
    - Run the Repl.  
    Expected outcome: Console shows `250 2.0.0 OK 12345`.  
    Do you see the success message? If not, verify the app password and ensure `smtp_port` is 587.

16. **Integrate Calendly into the Notion table**:  
    - Go to `https://calendly.com/`.  
    - Click **“Sign up free”**, use the same Gmail address.  
    - Create a new

---

## Procedure 1.3: Create Core Business Accounts and Calendly

**Objective:** Establish a professional business infrastructure by creating a dedicated business email, registering a domain, and setting up a Calendly account that is ready for subsequent AI‑driven onboarding automation with Klaviyo and Make.com.

---

### 1. Create a Business Email Account on Zoho Mail (Free Tier)

1. Open **https://www.zoho.com/mail/** in Chrome.  
2. Click the **Sign up for free** button (upper‑right).  
3. In the dialog, enter **yourbusiness@yourdomain.com** in the *Email ID* field.  
4. Click **Create Free Account**.  
5. You will be prompted to verify your domain.  
   - In the **Domain Verification** section, type **yourdomain.com** (replace with your chosen domain).  
   - Click **Verify**.  
   - If the domain exists, Zoho will show a green tick; if not, it will prompt you to create a new domain (skip for now).  
6. **Interactive Check‑In:** Do you see a green tick next to your domain name?  
   - If not, ensure you typed the domain correctly.  
   - If the domain still fails, go to **Step 4** to register a new domain on Hostinger.

*Expected Output:* A confirmation page stating “Domain successfully verified. Your free Zoho Mail account is ready.”  

---

### 2. Register a Domain on Hostinger (Monthly $1.99)

7. Navigate to **https://www.hostinger.com/domains**.  
8. In the search bar, type **yourdomain.com** and click **Search**.  
9. Click **Add to Cart** next to the domain.  
10. On the cart page, click **Proceed to Checkout**.  
11. Sign in or create a Hostinger account using your newly created Zoho email.  
12. In the **Billing** section, choose **Monthly** and confirm the price **$1.99**.  
13. Click **Confirm Order** and complete the payment via PayPal or credit card.  
14. After payment, you will receive a confirmation email from Hostinger.  
15. **Interactive Check‑In:** Do you see the domain listed under “My Domains” in Hostinger?  
    - If not, check the email for confirmation or re‑login to Hostinger.  

*Expected Output:* Domain status “Active” with a DNS management page.

---

### 3. Configure DNS for Zoho Email

16. In Hostinger, click **Manage** next to your domain.  
17. Go to **DNS Zone Editor**.  
18. Add the following TXT record for Zoho verification:  
    - **Host:** @  
    - **Value:** `zoho-verification=XXXXX` (replace XXXXX with the token provided in Zoho).  
19. Add MX records as listed in Zoho’s email setup guide (usually:  
    - `mx.zoho.com` priority 10  
    - `mx2.zoho.com` priority 20).  
20. Save changes.  
21. **Interactive Check‑In:** Do you see the new TXT and MX records appear in the DNS list?  
    - If not, refresh the page or wait 5 minutes for propagation.  

*Expected Output:* DNS records displayed; Zoho will later confirm email service is active.

---

### 4. Sign Up for Calendly

22. Open **https://calendly.com/**.  
23. Click **Sign up free** in the top‑right corner.  
24. Choose **Email** as the sign‑up method.  
25. Enter **yourbusiness@yourdomain.com** and click **Continue**.  
26. Set a strong password (e.g., `P@ssw0rd!123`).  
27. Click **Create account**.  
28. Calendly will send a verification email to Zoho.  
29. Open the Zoho inbox, click **Verify email**.  
30. **Interactive Check‑In:** Do you see a confirmation screen saying “Account verified!”?  
    - If not, check spam or resend verification from Calendly.  

*Expected Output:* Calendly dashboard with your name and a “Create Event Type” button visible.

---

### 5. Create a Basic Event Type

31. Click **Event Types** in the left sidebar.  
32. Click **+ New event type** → **One‑to‑One**.  
33. Enter **“AI Onboarding Intro Call”** in the *Event name* field.  
34. Set **Location** to **Zoom** (default).  
35. Click **Continue**.  
36. In the *Availability* tab, set **Duration** to **30 minutes**.  
37. Click **Save & Close**.  
38. **Interactive Check‑In:** Do you see the new event type listed with a green “Active” badge?  
    - If not, ensure you clicked “Save & Close” and check the Dashboard.  

*Expected Output:* Event type “AI Onboarding Intro Call” appears under “Event Types”.

---

### 6. Create a Calendly API Key

39. In Calendly, click your profile icon → **Integrations**.  
40. Under **API & Webhooks**, click **Generate API Key**.  
41. Copy the 32‑character key to clipboard.  


## Check-In: Module 1 Complete

- [ ] REGISTER YOUR BUSINESS DOMAIN ON HOSTINGER completed and verified
- [ ] Set Up Email and Workspace in Notion completed and verified
- [ ] Create Core Business Accounts and Calendly completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 2: TECH STACK

## Overview

In Module 2 you will assemble the core technology stack that powers every AI‑driven onboarding funnel. This module is the foundation that lets you connect Calendly, Klaviyo, Make.com, and the ancillary tools that transform raw data into a seamless customer journey. By following these steps you will:

1. **Generate secure API keys** for each service.  
2. **Create a unified data schema** that ensures contact fields flow correctly between Calendly, Make.com, and Klaviyo.  
3. **Verify bidirectional sync** so that a new booking in Calendly automatically triggers a welcome email, a task in Notion, and a replay in Loom.

Skipping this module means your automation will be fragmented—bookings will go to inboxes, emails will miss personalization tokens, and analytics will be incomplete. A fractured stack leads to lost leads, manual follow‑ups, and a churn rate that climbs faster than your revenue.

| Tool      | Purpose                                                                 | Free Tier                                         | Paid Tier (Monthly) |
|-----------|--------------------------------------------------------------------------|---------------------------------------------------|---------------------|
| Calendly  | Schedule and capture client appointments                               | Unlimited events, 1 calendar, basic branding      | $10 / calendar      |
| Klaviyo   | Email/SMS marketing automation, segmentation                           | 250 contacts, 500 emails, basic templates        | $20 / 500 contacts  |
| Make.com  | Visual workflow automation, API integration                            | 1,000 operations, 20 scenarios, 15 min timeout    | $19 / 15,000 ops    |
| Zapier    | Bridge between non‑API apps, simple logic                              | 5 Zaps, 100 tasks/month                           | $20 / 2,000 tasks   |
| Notion    | Project tracking, SOPs, knowledge base                                 | Unlimited pages, 5 users, 5,000 blocks            | $8 / user           |
| Replit    | Quick code snippets, API testing, sandboxed Python scripts             | Unlimited public repos, 500 MB storage            | $7 / private repo   |

**Estimated time to complete:** 30 minutes

You will build a single, coherent pipeline that lets you launch AI‑powered onboarding in under an hour—once the stack is in place, the rest of the playbook is a series of click‑throughs, not code.

---

## Procedure 2.1: Connect ChatGPT API and Store Keys in Notion

1. **Open a web browser** and navigate to the OpenAI API portal:  
   <https://platform.openai.com/account/api-keys>  
   **Login** with your OpenAI credentials (or create an account if you don’t have one).

2. Click the **bold button** **“+ Create new key”**.  
   In the popup, give the key a name such as **“Menshly Onboarding Key”** and click **“Create key”**.

3. **Copy** the newly generated key by selecting the key text and pressing **Ctrl+C** (Windows) or **⌘C** (macOS).  
   The key looks like `sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`.

4. **Open a new tab** and go to Notion: <https://www.notion.so>.  
   **Login** to your Notion workspace.

   *Do you see the Notion dashboard with “+ New Page”? If not, refresh the page or check your internet connection.*

5. In the left sidebar, click **“+ New Page”**.  
   Title the page **“API Keys”** and set the page icon to a 🔑 emoji.

6. Inside the “API Keys” page, click **“Add a database”** → **“Table – Inline”**.  
   Name the database **“ChatGPT API Keys”**.

7. In the database, click the **“+ Add a property”** button, choose **“Text”** and name it **“API Key”**.

8. Click the **first empty row** under the **“API Key”** column.  
   Paste the key you copied earlier (**Ctrl+V** / **⌘V**).  
   The entry should now display a long alphanumeric string.

   *Do you see the new row with the key? If the key is blank, double‑click the cell and paste again.*

9. Click the **three dots** in the top-right of the database and choose **“Copy link to page”**.  
   Store this URL in your clipboard; it will be used by Make.com to access the database.

10. **Open a new browser tab** and go to Make.com: <https://www.make.com>.  
    **Login** or sign‑up. (Free tier: 200 operations/month, 1 scenario, 15 min refresh).

11. Click **“Create new scenario”** and name it **“Store ChatGPT Key in Notion”**.

12. In the scenario editor, click **“+ Add another module”**, search for **“Notion”**, and select **“Create a database row”**.

13. Connect your Notion account by clicking **“Add new connection”**.  
    Follow the OAuth flow: click **“Authorize”**, then **“Allow”**.  
    In the dialog, choose the workspace that contains the **“ChatGPT API Keys”** database and click **“Finish”**.

14. In the [**Notion module settings**](https://notion.so/), set **Database** to **“ChatGPT API Keys”** (use the dropdown).  
    For the **Properties** field, click **“Add a property”** → **“API Key”** → **“Text”** and paste the API key into the value box.

15. Click the **green “Run once” button** at the top right of the scenario.  
    The module will create a new row in the database.  
    The **output panel** should display JSON similar to:  
    ```
    {
      "id": "some-id",
      "created_time": "2026-10-10T12:34:56.789Z",
      "properties": {
        "API Key": [
          {
            "type": "rich_text",
            "rich_text": [
              {
                "plain_text": "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
              }
            ]
          }
        ]
      }
    }
    ```

   *Do you see a JSON response with “sk-…”? If the key appears truncated, check that you pasted the entire string.*

16. Click **“Save”** in the top right of Make.com to keep the scenario.

17. To **automate future key updates**, add a trigger module:  
    a. Click **“+ Add another module”** → search **“Notion”** → select **“Watch database items”**.  
    b. Set **Database** to **“ChatGPT API Keys”** and **Trigger** to **“New or updated rows”**.  
    c. Connect the same Notion connection used earlier.

18. Click **“Run once”** again to test the trigger.  
    The scenario should fire, create a new row

---

## Procedure 2.2: Build Your First Make.com Automation Scenario  

**Goal:** Connect a Calendly booking to a Klaviyo welcome email using Make.com.  
**Tools:** Make.com (https://www.make.com), Calendly (https://calendly.com), Klaviyo (https://www.klaviyo.com).  
**Prerequisites:**  
- Active Calendly account with a “New Meeting” event type.  
- Active Klaviyo account with a list named “Onboarding Leads”.  
- API keys: Calendly API token and Klaviyo private API key.  

> **Tip:** Keep your API keys in a secure password manager.  

---

### 1. Sign in to Make.com
1. Open a browser and go to **https://www.make.com**.  
2. Click the **“Log in”** button in the top‑right corner.  
3. Enter your email and password, then click **“Log in”**.  
4. You should see the **Dashboard** page with a blue banner that reads “Welcome to Make.com”.  

**Check‑in:** Do you see the Dashboard with the “Welcome to Make.com” banner?  
If not, ensure you are logged in and that your browser isn’t blocking pop‑ups.

### 2. Create a New Scenario
5. In the left‑hand menu, click **“Scenarios”**.  
6. Click the **“Create a new scenario”** button (green, top‑right).  
7. The **Scenario Editor** opens with a blank canvas.  
8. Click the **“+”** icon left of the canvas to add a module.  

**Check‑in:** Do you see the “Scenario Editor” with a blank canvas and a “+” icon?  
If not, refresh the page or log out/in again.

### 3. Add the Calendly Trigger
9. A modal appears titled “Choose a trigger module”.  
10. In the search bar type **“Calendly”** and press **Enter**.  
11. Select **“New booking”** and click **“Create”**.  
12. In the **“Calendly API token”** field, paste your token (from Calendly’s settings → Integrations → API Key).  
13. In the **“Event type”** dropdown, choose **“New Meeting”**.  
14. Click **“Save”**.  

**Check‑in:** Do you see the Calendly trigger module with “New booking” and your token displayed?  
If the token field is blank, double‑check that you copied the full token without spaces.

### 4. Add a Filter (Optional but Recommended)
15. Click the **“+”** icon next to the Calendly module.  
16. Search for **“Filter”** and select the **“Filter”** module.  
17. In the filter editor, set the rule:  
   - **Field:** `Event type`  
   - **Condition:** `equals`  
   - **Value:** `New Meeting`  
18. Click **“Save”**.  

**Check‑in:** Do you see a filter with the rule “Event type equals New Meeting”?  
If the rule isn’t saved, ensure you clicked **“Save”** after editing.

### 5. Add the Klaviyo Action
19. Click the **“+”** icon after the filter.  
20. Search for **“Klaviyo”** and select **“Add contact to list”**.  
21. In the **“Klaviyo API key”** field, paste your private key (found under Klaviyo → Settings → API Keys → Private API Key).  
22. In the **“List”** dropdown, select **“Onboarding Leads”**.  
23. In the **“Email”** field, click the dropdown > **“Map a value”** > choose **`Email`** from the Calendly trigger.  
24. In the **“First name”** field, map **`First name`** from Calendly.  
25. In the **“Last name”** field, map **`Last name`** from Calendly.  
26. Click **“Save”**.  

**Check‑in:** Do you see the Klaviyo module with “Add contact to list: Onboarding Leads” and

---

## Procedure 2.3: Configure Vapi Voice Agent and ElevenLabs TTS

1. **Open your web browser** and navigate to **https://app.vapi.io**.  
   *If you are not already logged in, click **SIGN IN** in the top‑right corner and enter your email/password. If you do not have an account, click **SIGN UP** and create a free tier account (50 calls/month).*

2. Click **GET STARTED** on the Vapi dashboard home screen.  
   You should see a page titled “Create a Voice Agent.”  

3. In the **Agent Name** field, type **“Onboarding Voice Agent”** and press **ENTER**.  
   Click **CREATE AGENT** (button appears in blue).  

4. **Do you see the Agent Overview page with a green “Agent Created” banner?**  
   *If not, refresh the page or verify you have a stable internet connection.*

5. Click **ADD SKILL** (button in the top‑center).  
   Choose **“Text‑to‑Speech”** from the dropdown and click **SELECT**.  

6. In the **Skill Settings** dialog, set **Language** to **English (US)**, **Voice** to **“Joanna”**, **Speed** to **1.0x**, and **Pitch** to **0 dB**.  
   Click **SAVE SETTINGS**.  

7. Click **ADD ACTION** in the skill panel.  
   Select **“Webhook”** and then click **CONFIGURE**.  

8. In the **Webhook URL** field, paste the URL you will generate later in Make.com (placeholder: `https://hook.integromat.com/xxxxxxxx`).  
   Set **Method** to **POST**, **Content Type** to **application/json**, and leave **Headers** empty.  
   Click **SAVE**.  

9. **Do you see the Webhook action listed under the skill with a status of “Ready”?**  
   *If you see “Failed”, check that the URL is correct and that you have saved the webhook in Make.com.*

10. Open a new tab and go to **https://www.elevenlabs.io**.  
    Log in with your credentials or sign up for the free tier (5 hours/month).  

11. Click **API** in the top navigation bar, then **Create API Key**.  
    Copy the key displayed and paste it into a secure note (e.g., Notion).  

12. Return to the Vapi tab, click **SETTINGS** (gear icon in the top‑right).  
    Under **API Keys**, paste the ElevenLabs key into the **Third‑Party Integration** field.  
    Click **VERIFY**.  

13. **Do you see “Integration Verified” in green?**  
    *If you see “Invalid Key”, double‑check that you copied the entire key and that you are pasting it into the correct field.*

14. In Vapi, click **TEST CALL** in the Agent Overview.  
    Type “Hello, this is your onboarding voice agent.” in the prompt field and click **SEND**.  

15. The call should play back with the Joanna voice at normal speed.  
    If the audio does not play, verify that your speaker is not muted and that your browser has permission to play audio.  

16. Open **https://www.make.com** and log in.  
    Click **CREATE A SCENARIO** in the top‑center.  

17. Drag the [**Vapi**](https://vapi.ai/) module from the left panel to the canvas.  
    Select **“Get Agent Message”** event and click **CONNECT**.  
    Use the Vapi API credentials you created earlier.  

18. Drag a **Webhook** module onto the canvas and connect it to the Vapi module.  
    Choose **“Catch Hook”** and click **CREATE**.  
    Copy the generated URL and paste it back into Vapi’s Webhook URL field (step 8).  

19. Add a **Text‑to‑Speech** module from the [**ElevenLabs**](https://elevenlabs.io/) connector.  
    Map the **Message** field from Vapi to the **Text** input of ElevenLabs.  
    Set **Voice** to **“Joanna”** and **Speed** to **1.0x**.  

20. Add an **Audio Upload** module from **Google Drive** (free tier).  
    Map the **Audio File** output from ElevenLabs to the **Upload File** input.  
    Set the folder to **“Onboarding Audio”** and click **CREATE**.  

21. Click **SAVE** and then **RUN** the scenario.  
    Vapi should trigger the webhook, ElevenLabs will generate TTS, and the audio file will appear in Google Drive.  

22. **Do you see the audio file in Google Drive with a filename containing the timestamp?**  
    *If not, check the scenario logs in Make.com for errors such as “Invalid API Key” or “Rate Limit Exceeded.”*  

23. Return to Vapi, click **ADD ACTION** again, select **“Send Email”**, and configure it to send the audio file URL to a test email address.  
    Verify that the email arrives with the correct attachment link.  

---

### Cost Breakdown Table (Free Tier Limits)

| Tool | Free Tier | Paid Tier (USD) | Free Limit | Paid Limit |
|------|-----------|-----------------|------------|------------|
| Vapi | $0 | $29/mo | 50 API calls/month | Unlimited |
| ElevenLabs | $0 | $

## Check-In: Module 2 Complete

- [ ] Connect ChatGPT API and Store Keys in Notion completed and verified
- [ ] Build Your First Make.com Automation Scenario completed and verified
- [ ] Configure Vapi Voice Agent and ElevenLabs TTS completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 3: FRAMEWORK

## Overview  

In this module you will master the universal process that turns raw AI ideas into a repeatable, client‑ready onboarding system. We begin by defining a **service delivery framework** that maps each touchpoint—from initial contact to post‑onboarding satisfaction—into discrete, automatable steps. Next, you craft a **client onboarding flow** that leverages Calendly for scheduling and Klaviyo for nurturing, embedding AI‑driven messaging and data capture at every junction. Finally, we establish **quality standards**: metrics, audit checkpoints, and rollback protocols that ensure each deployment meets 99 % uptime and 95 % client satisfaction.

Skipping this module means launching unstructured, error‑prone workflows that waste time, frustrate clients, and erode trust. Without a clear framework, you’ll struggle to reproduce success, scale, or bill clients for incremental value. You’ll also miss the crucial automation benefits of Calendly’s event hooks and Klaviyo’s segmentation, leading to lower conversion rates and higher churn.

| Tool       | Purpose                                            | Free Tier                             | Paid Tier (monthly) |
|------------|-----------------------------------------------------|---------------------------------------|---------------------|
| Calendly   | Schedule & trigger onboarding events                | 1 event type, 1 calendar, 5 team members | Pro: $12 (per user) |
| Klaviyo    | Email nurture, segmentation, and analytics          | 250 contacts, 500 email sends         | Growth: $20 (1‑2k contacts) |
| Make.com   | Connect Calendly → Klaviyo → database & reports    | 1,000 operations/month                 | Starter: $9 (10,000 ops) |
| Notion     | Document the framework, store SOPs, & version control| Unlimited pages, 5 users              | Personal: $4 (5 users) |
| Zapier     | Quick 3‑step automations for prototyping            | 5 zaps, 100 tasks/month               | Starter: $19.99 (750 tasks) |

**Estimated time to complete**: 4–5 hours (including research, schema design, and test runs).

---

## Procedure 3.1: Design Your Service Delivery Framework in Notion

1. **Open Notion**  
   - Navigate to **https://www.notion.so** and click **Login** in the top‑right corner.  
   - Enter your email and password, then click **Sign in**.  
   - *Expected result*: You land on the **Workspace Home** page with a sidebar listing **Pages** and **Templates**.

2. **Create a New Workspace Page**  
   - In the sidebar, click **+ Add a page**.  
   - Set the title to **“AI Onboarding Service Framework”** and press **Enter**.  
   - In the top toolbar, click **🗂️ Icon** (next to the title) and choose **📁 Folder** to place it under **“Projects”**.  
   - *Expected result*: A blank page titled *AI Onboarding Service Framework* appears.

3. **Add a Cover and Icon**  
   - Hover over the top of the page until the **Add cover** button appears. Click it and select **“AI”** from the gallery.  
   - Click the default **🗃️** icon next to the title, choose **🤖** from the emoji picker.  
   - *Expected result*: The page now has an AI cover image and robot icon.

4. **Insert a Table of Contents (TOC)**  
   - Type `/table of contents` and select **Table of contents**.  
   - It auto‑populates with any headings on the page.  
   - *Check‑in*: Do you see a **Table of contents** block at the top of the page? If not, click the block menu (three dots) and choose **Table of contents**.  

5. **Create Section Headings**  
   - Type `## 1. Client Intake` and press **Enter**.  
   - Repeat for `## 2. Onboarding Workflow`, `## 3. AI Tools Stack`, `## 4. KPI Dashboard`, `## 5. Feedback Loop`.  
   - *Expected result*: Five level‑2 headings appear, automatically added to the TOC.

6. **Populate “1. Client Intake” with a Table**  
   - Type `/table - full page` and select **Table – Full Page**.  
   - Name the table **“Client Intake Form”**.  
   - Create columns: **Name** (Title), **Email** (Email), **Onboarding Date** (Date), **Service Package** (Select: Basic, Advanced, Premium).  
   - Add a row for a test client: *John Doe, john@example.com, 2026‑10‑15, Premium*.  
   - *Check‑in*: Do you see the table with the columns and test row? If not, ensure the column types match the names exactly.

7. **Add a Calendar View for “Onboarding Date”**  
   - Click the `+ Add a view` button in the table header.  
   - Choose **Calendar**, name it **“Onboarding Calendar”**, and click **Create**.  
   - *Expected result*: Calendar view shows the test client’s date.

8. **Embed a Calendly Scheduling Link**  
   - Go to **https://calendly.com** and sign in.  
   - Click **Create Event Type** → **One‑to‑one**, name it **“Onboarding Call”**.  
   - Under **When can people book this event?** set the default buffer to **15 min**.  
   - Copy the **Public link** (e.g., `https://calendly.com/yourname/onboarding-call`).  
   - Return to Notion, type `/link` and paste the Calendly URL.  
   - The block will auto‑convert into an embedded Calendly widget.  
   - *Check‑in*: Do you see a live Calendly widget embedded? If not, click the block’s **•••** and select **Open in new window** to verify the link.

9. **Create a “Klaviyo Email Sequence” Database**  
   - Type `/database - inline` → **Table - Inline**.  
   - Name it **“Klaviyo Sequences”**.  
   - Add columns: **Email Subject** (Title), **Send Day** (Number), **Automation ID** (Rich Text).  
   - Insert two rows:  
     - *Welcome Email*, `0`, `k-12345`  
     - *First Check‑in*, `3`, `k-67890`.  
   - *Expected result*: Table displays the two sequences.

10. **Set Up Make.com Integration**  
    - Visit **https://www.make.com** and log in.  
    - Click **Create a new scenario**.  
    - Search for **Calendly** in the app list, select **Calendly** → **Trigger** → **Invitee created**.  
    - Click **Continue** and connect your Calendly account using the OAuth prompt.  
    - Add a second module: **Klaviyo** → **Add a subscriber**.  
    - Map fields: **Email** → `invitee.email`, **First name** → `invitee.first_name`.  
    - Set **List ID** to your onboarding list (e.g., `list-001`).  
    - Click **Save** and **Run once** to test.  
    - *Check‑in*: Do

---

## Procedure 3.2: Build the Client Onboarding Automation Pipeline

1. **Open your web browser** and navigate to **https://calendly.com/**.  
   - If you do not have an account, click the **SIGN UP FREE** button in the top‑right corner.  
   - Use your Google account or enter your email + password.  
   - After signing up, you will see the **Calendly Dashboard** – the screen should display “**Your Dashboard**” in the header.

2. **Create the “Client Onboarding Call” event type**  
   - Click the **+ NEW EVENT TYPE** button in the center of the dashboard.  
   - Choose **ONE‑TIME**.  
   - In the form that appears, set **Event name** to “Client Onboarding Call”, **Duration** to 30 minutes, and **Location** to “Calendly Meeting”.  
   - Click **SAVE & CONTINUE** at the bottom.  
   - On the next screen, under **Availability**, set “**Everyone**” to “**Mon‑Fri 9 AM‑5 PM (EST)**”.  
   - Click **SAVE & CONTINUE** again.  
   - On the final screen, click **FINISH**.  
   - **Expected output:** The new event type appears in your dashboard list with a green status “Active”.

3. **Configure email reminders**  
   - In the event type card, click **EDIT INVITEE NOTIFICATIONS**.  
   - Toggle **Send a reminder email 24 hrs before** to ON.  
   - Enter the message body: “Hi {{invitee.firstName}}, your onboarding call is tomorrow at {{event.startTime}}. Looking forward to speaking with you!”  
   - Click **SAVE**.  
   - **Expected output:** The reminder section shows “24 hrs before” with your custom message displayed.

4. **Open Make.com**  
   - In a new tab, go to **https://www.make.com/en**.  
   - Click **LOGIN** in the top-right corner and enter your credentials (or click **SIGN UP FREE** if you need an account).  
   - Once logged in, you will see the **Dashboard** with a button **+ CREATE SCENARIO**.

5. **Create a new scenario**  
   - Click **+ CREATE SCENARIO**.  
   - Search for **Calendly** in the search box and click the icon.  
   - Select the trigger **“When a new event is scheduled”** and click **ADD**.  
   - In the module settings, click **ADD** next to **Calendly API key**.  
   - Open another tab to **https://calendly.com/settings/integrations**.  
   - Under **API & Webhooks**, click **CREATE API KEY**.  
   - Copy the generated key and paste it into Make.com's Calendly module field.  
   - Click **TEST**

## Check-In: Module 3 Complete

- [ ] Design Your Service Delivery Framework in Notion completed and verified
- [ ] Build the Client Onboarding Automation Pipeline completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 4: FIRST BUILD

## Overview

In this module you will **create, optimize, and deploy a fully‑functional AI customer onboarding workflow** that connects Calendly scheduling with Klaviyo email automation, all orchestrated through Make.com. You will learn how to turn a raw client data set into a seamless, self‑service onboarding experience that captures leads, scores them with AI logic, and sends personalized welcome sequences—all without writing a single line of code. This is the core deliverable that will prove your agency’s value to prospects; missing it means you’ll offer generic onboarding services that lack the AI edge your competitors already possess.

The hands‑on procedures walk you through every step: building a Calendly event flow, feeding attendee data into Make.com, parsing and scoring the data with an AI model, and triggering Klaviyo workflows that nurture each lead. You’ll finish with a live demo scheduled for a real client, complete with analytics dashboards and performance metrics. Skipping this module will leave you unable to showcase a repeatable, AI‑powered onboarding pipeline, and clients will see you as a standard service provider rather than a tech‑savvy revenue generator.

| Tool     | Purpose                                 | Free Tier                                         | Paid Tier                                 |
|----------|-----------------------------------------|---------------------------------------------------|-------------------------------------------|
| Calendly | Schedule & capture new customers        | 1 calendar, 1 event type, basic reporting         | Premium: $49/month (Unlimited calendars)  |
| Klaviyo | Email automation & segmentation         | 500 contacts, 5,000 sends/month                   | Essentials: $20/month (scales with contacts) |
| Make.com | Workflow orchestration & AI integration | 100 operations/month, 5 “My Apps”                 | Pro: $39/month (1,000 operations/month)  |
| Zapier   | Optional redundancy & alternate triggers| 5 apps, 100 tasks/month                           | Starter: $19.99/month (Unlimited tasks)  |

**Estimated time to complete:** 4–5 hours.

---

## Procedure 4.1: Create the Core AI Onboarding Product in Replit  

**Goal:** Build a fully‑functional AI‑powered customer onboarding system that receives Calendly scheduling data, triggers an OpenAI ChatGPT prompt, and fires a Klaviyo email flow—all hosted on Replit.  

> **Practical tip:** Keep every file version‑controlled by committing to the built‑in Replit Git.  

---

### 1. Set up the Replit project  
1. Open your browser and go to **https://replit.com**.  
2. Click **SIGN IN** in the top‑right. Use your Google or GitHub account.  
3. After login, click **+ CREATE** in the top‑right corner.  
4. Select **Python** from the language dropdown.  
5. In the *Name* field, type **ai‑onboarding**.  
6. Click **CREATE REPL**.  

> **Do you see a new Replit workspace titled "ai‑onboarding" with a `main.py` file?**  
> If not, refresh the page or double‑check you’re logged in.  

---

### 2. Install required packages  
1. Click the **Shell** tab at the bottom of the editor.  
2. Paste the following command and press **Enter**:  
   ```bash
   pip install flask openai requests python-dotenv
   ```  
3. Wait for the shell to finish. The output should end with `Successfully installed ...`.  

> **Expected output:**  
> ```text
> Successfully installed flask==2.2.5 openai==0.27.5 requests==2.31.0 python-dotenv==1.0.0
> ```  

---

### 3. Create environment variables file  
1. In the file tree, right‑click **ai‑onboarding** → **New File** → name it **`.env`**.  
2. Add the following lines, replacing placeholders with your real API keys:  
   ```dotenv
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   KLAVIYO_API_KEY=YOUR_KLAVIYO_PRIVATE_API_KEY
   CALENDLY_WEBHOOK_SECRET=YOUR_CALENDLY_WEBHOOK_SECRET
   ```  
3. Save the file.  

> **Do you see a `.env` file with the three keys?**  
> If you see an error “File not found,” re‑create the

---

## Procedure 4.2: BUILD THE DATA PROCESSING PIPELINE WITH MAKE.COM

1. Open your web browser and navigate to **https://www.make.com**.  
   **Do you see the left‑hand navigation panel with “Dashboard” and “Scenarios”?**  
   If not, refresh the page or clear your browser cache.

2. Click the **blue “Sign Up” button** in the upper right corner.  
   - In the modal, choose **“Use Google”** and authenticate with your Google account.  
   - After authentication, you’ll land on the [**Make.com Dashboard**](https://www.make.com/en/register?pc=menshly).  
   **Expected output:** A screen showing “Your Scenarios” and a **“Create a new scenario”** button.

3. On the Dashboard, click **“Create a new scenario”**.  
   - The Scenario editor opens.  
   - In the search bar at the top, type **“Calendly”** and press **Enter**.  
   - Click the **Calendly icon** (blue with a calendar).  
   - Select **“Watch Event”** from the list and click **“Continue”**.  
   **Do you see the Calendly module set to “Watch Event” with the “Event type” dropdown?**  
   If not, ensure you are using the latest Make.com plan (Free tier allows 100 operations/month).

4. Click the settings icon (gear) next to the Calendly module.  
   - In the “Calendly Settings” panel, click **“Add a new connection”**.  
   - Choose **“API Key”** and click **“Create new key”**.  
   - Copy the generated key and paste it into the **API Key field**.  
   - Click **“Save”**.  
   **Check‑in:** Do you see “Calendly connection: active” in the module?  
   If you see “Error: 401 Unauthorized”, it means the key is invalid—re‑generate it on Calendly’s API page and retry.

5. Click **“+ Add another module”** below the Calendly module.  
   - Search for **“JSON”** and select **“Parse JSON”**.  
   - Connect the output of Calendly to the input of Parse JSON.  
   - In the Parse JSON settings, paste the following sample JSON schema (replace with your actual schema if needed):  
     ```json
     {
       "type": "object",
       "properties": {
         "event": {"type":"string"},
         "attendee": {"type":"object","properties": {"email":{"type":"string"}}}
       }
     }
     ```  
   - Click **“Save”**.  
   **Expected output:** The Parse JSON module shows “Schema parsed successfully”.

6. Add a third module by clicking **“+ Add another module”**.  
   - Search for **“Klaviyo”** and pick **“Add Subscriber”**.  
   - Connect Parse JSON → Klaviyo.  
   - In Klaviyo settings, click **“Add a new connection”**.  
   - Choose **“API Key”** and use the **public API key** from your Klaviyo account (found under Account > Settings > API Keys).  
   - Click **“Save”**.  
   - Map fields:  
     - **Email** → **attendee.email** (click the dropdown and select *attendee.email*).  
     - **First Name** → **attendee.first_name** (if present).  
     - **List** → choose your onboarding list (e.g., “New Clients”).  
   **Do you see the Klaviyo module’s field mapping?**  
   If the list is missing, double‑check the list ID in Klaviyo.

7. Click the **blue “Save” button** at the top right of the Scenario editor.  
   - Name the scenario **“Calendly → Klaviyo Onboarding”**.  
   **Expected output:** A notification “Scenario saved successfully”.

8. Turn the scenario on by clicking the **green “Run once” toggle** next to the scenario name.  
   - In the pop‑up, click **“Run”**.  
   - Make will poll Calendly for a new event.  
   **Check‑in:** After a few seconds, does the scenario run log show “Calendly event received”?  
   If it times out, verify your Calendly webhook URL in your Calendly account settings.

9. Create a test Calendly event:  
   - Log into **https://calendly.com** with the same

---

## Procedure 4.3: Deploy and Test the Complete System

1. **Log into Calendly**  
   - URL: `https://calendly.com/`  
   - Click **Log in** (top‑right).  
   - Enter your email and password, then click **Log in**.  
   - **Expected output:** You land on the Calendly dashboard with your scheduled events.

2. **Create a new “AI Onboarding Call” event**  
   - Click **+ New event type** (button in the left sidebar).  
   - Select **One‑on‑one**.  
   - Click **Create event type**.  
   - **Expected output:** A new event form appears.

3. **Configure event details**  
   - Title: **AI Onboarding Call**.  
   - Duration: **30 minutes**.  
   - Click **Save & next**.  
   - **Expected output:** Event preview page with “Event details saved”.

4. **Set availability**  
   - Under **When can people book this event?** click **Custom**.  
   - Add working days: Monday‑Friday, 9:00 AM‑5:00 PM (local time).  
   - Click **Save & next**.  
   - **Expected output:** Availability calendar shows 10 slots per day.

5. **Add a hidden question to capture onboarding data**  
   - Click **Add question** → **Short answer**.  
   - Label: **Client ID**.  
   - Toggle **Make this question required** off.  
   - Click **Advanced** → **Show on scheduling page** → **Hidden**.  
   - Click **Save**.  
   - **Expected output:** Question appears in the event form but is hidden from the client.

6. **Create a webhook for Make.com**  
   - Click **Integrations** → **Calendly Webhooks**.  
   - Click **Add webhook**.  
   - URL: `https://hooks.maker.com/webhook/your‑unique‑id` (replace with your Make.com webhook URL).  
   - Trigger: **Invitee created**.  
   - Click **Save**.  
   - **Expected output:** Webhook status “Active”.

7. **Open Make.com**  
   - URL: `https://www.make.com/`  
   - Click **Log in** → enter credentials → **Log in**.  
   - **Expected output:** Dashboard with “Create a new scenario”.

8. **Create a new scenario**  
   - Click **Create a new scenario**.  
   - Search and add **Calendly** → **Watch Invitee**.  
   - Click the Calendly icon, then **Add webhook** → paste the same URL from step 6.  
   - Click **Save** → **OK**.  
   - **Expected output:** Trigger module shows “Calendly – Watch Invitee” with “Webhook URL copied”.

9. **Add Klaviyo action**  
   - Click the plus icon next to the trigger → search **Klaviyo** → **Add contact**.  
   - Click **Connect** → enter your Klaviyo API key (`https://www.klaviyo.com/account/api-keys`).  
   - Map fields:  
     - **First name** → `{{Calendly.invitee.first_name}}`  
     - **Email** → `{{Calendly.invitee.email}}`  
     - **Client ID** → `{{Calendly.invitee.custom_questions.Client_ID}}`  
   - Click **Save**.  
   - **Expected output:** Action module displays “Klaviyo – Add contact” with mapped fields.

10. **Add email send step**  
    - Click plus icon → search **Klaviyo** → **Send email**.  
    - Choose your welcome email template “Welcome to AI Onboarding”.  
    - Map **Recipient** → `{{Klaviyo Add contact.email}}`.  
    - Click **Save**.  
    - **Expected output:** Email module ready with template preview.

11. **Test the scenario**  
    - Click **Run once**.  
    - In a new tab, open `https://calendly.com/your‑profile/ai‑onboarding-call` and schedule a test meeting with a dummy email.  
    - Return to Make.com → **Run once**.  
    - **Expected output:** Modules run successfully, green check marks on each step.

> **Check‑in 1**  
> Do you see the green check marks on the Calendly trigger, Klaviyo add contact, and Klaviyo send email modules?  
> If not, refresh the scenario, ensure the webhook URL matches, and re‑run the test.

12. **Verify contact in Klaviyo**  
    - URL: `https://www.klaviyo.com/account/contacts`  
    - Search for the dummy email.  
    - **Expected output:** New contact appears with first name, email, and custom

## Check-In: Module 4 Complete

- [ ] Create the Core AI Onboarding Product in Replit completed and verified
- [ ] BUILD THE DATA PROCESSING PIPELINE WITH MAKE.COM completed and verified
- [ ] Deploy and Test the Complete System completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 5: CLIENT ACQUISITION

## Overview

In the rapidly evolving landscape of customer experience, the ability to attract and convert prospects into paying clients hinges on delivering a frictionless, AI‑driven onboarding journey. MODULE 5 equips you with a step‑by‑step operating system to **design, launch, and refine** customer onboarding workflows that combine Calendly’s scheduling power with Klaviyo’s hyper‑personalized email automation. By mastering these tools, you can turn every first interaction into a revenue‑generating touchpoint, ensuring clients feel guided, valued, and immediately productive from day one.

Skipping this module means leaving critical revenue leakage on the table: prospects will linger on a manual sign‑up process, your conversion rates will stagnate, and you’ll miss the chance to scale your services through automated, high‑margin acquisition funnels. The module’s procedures will show you how to set up an instant lead capture landing page, trigger AI‑powered qualification sequences, and nurture leads through a series of targeted, conversational emails that convert at industry‑best rates.

| Tool         | Purpose                                                    | Free Tier                         | Paid Tier (Monthly) |
|--------------|------------------------------------------------------------|-----------------------------------|---------------------|
| Calendly     | Schedule discovery calls, onboarding sessions              | Unlimited meetings, 1 calendar    | Pro: $8 (solo)      |
| Klaviyo      | Email automation, onboarding sequences, segmentation       | 5,000 contacts, 500 emails       | Growth: $20 (500)   |
| Make.com     | Connect Calendly ↔ Klaviyo, trigger workflows             | 500 operations/month             | Starter: $9.99      |
| [Canva](https://www.canva.com/)        | Design lead‑capture landing page graphics                  | Unlimited free templates         | Pro: $12.99         |
| Notion       | Store lead data, workflow documentation                    | Unlimited pages, guests           | Team: $10 (5 users) |

**Estimated time to complete**: 3 hours – 3 hours 45 minutes, including setup, testing, and launch of the first acquisition pipeline.

---

## Procedure 5.1: Build a High‑Conversion Landing Page on Shopify

1. **Log into Shopify Admin**  
   - Open your web browser and go to **https://www.shopify.com/login**.  
   - Enter your email, password, and click the **bold** button **“Log in.”**  
   - Expected result: You see the Shopify Dashboard with the “Orders” tab highlighted.

2. **Create a New Store (if you don’t already have one)**  
   - Click **bold** “Create a store” on the welcome page.  
   - Fill “Store name” field **exactly** with `AcmeOnboardingLanding`.  
   - Choose “No” for “Do you already have a store?” and click **bold** “Start free trial.”  
   - Wait for the 14‑day free trial confirmation page.  

3. **Select a Theme**  
   - From the Dashboard, click **bold** “Online Store” → “Themes.”  
   - Under “Explore free themes,” click **bold** “Add theme.”  
   - Choose the **“Debut”** theme (free) and click **bold** “Add to theme library.”  
   - Expected output: Debut appears in your “Theme library” list.

4. **Duplicate the Theme for Editing**  
   - In the “Theme library,” hover over Debut and click **bold** “Duplicate.”  
   - Name the duplicate **“AcmeLanding”** in the popup and click **bold** “Duplicate.”  
   - Do you see the new theme “AcmeLanding” listed? If not, refresh the page and repeat step 4.

5. **Activate the Duplicate Theme**  
   - In the “Theme library,” click **bold** “Actions” → **“Publish.”**  
   - Confirm by clicking **bold** “Yes, publish.”  
   - Expected result: The preview pane updates to show the Debut theme with the store URL `https://acmeonboardinglanding.myshopify.com`.

6. **Set Up a Dedicated Landing Page**  
   - From the Dashboard, go to **bold** “Online Store” → “Pages.”  
   - Click **bold** “Add page.”  
   - Title the page **“Welcome to Acme Onboarding”** and set the URL handle to `welcome`.  
   - In the content editor, click **bold** “Show HTML.”  
   - Paste the following minimal HTML skeleton:

   ```html
   <div id="hero" style="background:url('{{hero_image}}') no-repeat center center; height:600px; color:#fff;">
     <h1 style="font-size:48px;">Accelerate Your Success</h1>
   </div>
   <div id="cta" style="text-align:center; margin-top:50px;">
     <a href="/apps/calendly" class="btn-primary">Book a Demo</a>
   </div>
   ```

   - Replace `{{hero_image}}` with the URL of the image you’ll upload in step 7.  
   - Click **bold** “Save.”  

7. **Create Hero Image in Canva**  
   - Open **https://www.canva.com** (free tier: 12 GB storage, 8 design types).  
   - Click **bold** “Create a design” → **“Custom size.”**  
   - Set width = 1920 px, height = 1080 px, click **bold** “Create new design.”  
   - In the left panel, click **bold** “Background” → use a gradient or upload your own via **bold** “Uploads.”  
   - Add a headline text “Accelerate Your Success” with font **Montserrat**, size = 96 pt, color = #FFFFFF.  
   - Click **bold** “Share” → **“Download.”**  
   - Choose **PNG** format, click **bold** “Download.”  
   - Upload the PNG to Shopify by returning to the page editor, clicking **bold** “Add image.”  

8. **Upload Hero Image to Shopify**  
   - In the page editor, click the image placeholder in the hero `<div>`.  
   - Choose **bold** “Upload files.”  
   - Select the PNG you downloaded from Canva.  
   - Once uploaded, click **bold** “Insert image.”  
   - The URL will appear in the editor (e.g., `https://cdn.shopify.com/s/files/1/XXXX/XXXX/...`).  
   - Replace `{{hero_image}}` in the HTML with this URL.  
   - Click **bold** “Save.”  
   - Do you see the hero banner rendered correctly on the preview? If not, double‑check the URL and reload.

9. **Create Calendly Scheduling Page**  
   - Open **https://calendly.com** (free tier: 1 event type).  
   - Click **bold** “New event type.”  
   - Choose **“One‑on‑one”**, name it **“Onboarding Demo”**, and click **bold** “Continue.”  
   - Set availability: click **bold** “Edit availability,” select Monday‑Friday, 9 am‑5 pm (your timezone).  
   - Under “Invitee questions,” add a required field **“Company Name.”**  
  

---

## Procedure 5.2: Configure Lead Generation with Apollo.io  

1. **Open a Web Browser** – Launch Chrome, Edge, or Firefox.  
2. **Navigate to Apollo.io** – Type `https://app.apollo.io` into the address bar and press **Enter**.  
3. **Create an Account** – On the Apollo.io landing page, click **Sign Up** in the upper‑right corner.  
4. **Fill the Registration Form** –  
   - **Email**: Enter a valid business email (e.g., `john.doe@menshlyglobal.com`).  
   - **Password**: Type a secure password (at least 12 characters, mix of upper/lowercase, numbers, and symbols).  
   - **Company Name**: `Menshly Global`.  
   - **Industry**: `Consulting`.  
   - **Number of Employees**: `1`.  
   Click **Create Account**.  
5. **Verify Email** – Check your inbox for a verification email from Apollo.io. Click **Verify** inside the email.  
6. **Login** – Return to `https://app.apollo.io` and click **Login**. Enter the same email and password, then click **Login**.  
   *Do you see the Apollo.io dashboard with a “Lead Pipeline” tab? If not, check that you used the correct credentials or that your email is verified.*  

7. **Set Up a Lead Source** –  
   - Click **Lead Sources** in the left‑hand navigation.  
   - Click **Add Lead Source** (button in the upper‑right corner).  
   - Choose **LinkedIn** from the dropdown.  
   - Click **Authorize** to grant Apollo.io permission to scrape LinkedIn profiles.  
   - In the **Source Name** field, type `LinkedIn Prospecting`.  
   - Click **Save Source**.  
8. **Create a Lead List** –  
   - Click **Lists** on the left.  
   - Click **New List** (bold **New List** button).  
   - Name the list `Prospecting – 2026Q4`.  
   - In the [**Description**](https://www.descript.com/) field, type `Leads gathered via Apollo.io LinkedIn source`.  
   - Click **Create**.  
9. **Add Leads to the List** –  
   - Inside the list, click **Add Leads** (bold **Add Leads**).  
   - Choose **Source** → `LinkedIn Prospecting`.  
   - Select the top 10 search results by checking the boxes.  
   - Click **Add Selected**.  
   *Do you see a confirmation banner that says “10 leads added to Prospecting – 2026Q4”? If not, ensure you selected at least one lead and clicked **Add Selected**.*  

10. **Export Lead Data to CSV** –  
    - On the list page, click the **Export** icon (three‑dot menu → **Export CSV**).  
    - In the export dialog, keep default settings: **All Fields** and **All Rows**.  
    - Click **Export**.  
    - The file `Prospecting–2026Q4.csv` will download to your default Downloads folder.  

11. **Upload CSV to Make.com** –  
    - Open a new tab and go to `https://www.make.com`.  
    - Click

---

## Procedure 5.3: Create Automated Email Nurture Sequence in Klaviyo  

1. **Open Klaviyo**  
   *URL:* `https://www.klaviyo.com/signin`  
   - Click **SIGN IN** (top right).  
   - Enter your email and password.  
   - Click **SIGN IN** button.  
   - *Expected output:* You are taken to the Klaviyo dashboard with the left‑hand navigation panel visible.  

2. **Create a New List**  
   - From the dashboard, click **_Lists & Segments_** in the left nav.  
   - Click the **+ NEW LIST** button (top right).  
   - In the modal:  
     - **Name:** `Client Onboarding`  
     - **Description:** `Subscribers who book a Calendly session.`  
     - Toggle **_Add subscribers automatically_** OFF.  
   - Click **_Create List_**.  
   - *Expected output:* A new list named “Client Onboarding” appears with 0 subscribers.  

3. **Create a Segment for Calendly Bookers**  
   - Click **_Lists & Segments_** → **+ NEW SEGMENT**.  
   - In the builder:  
     - **Segment Name:** `Calendly Bookers`  
     - **Condition:** `Event` → **_Any event_** → **_Book a Session_** (choose the event name you’ll create in Calendly).  
   - Click **_Create Segment_**.  
   - *Expected output:* Segment “Calendly Bookers” shows 0 members.  

4. **Set Up a Make.com Scenario to Push Calendly Bookings to Klaviyo**  
   - Open a new tab and go to `https://www.make.com/en`.  
   - Click **SIGN IN** → use your credentials.  
   - Click **Create a new Scenario**.  
   - Search for **Calendly** and click the icon.  
   - Choose the **Watch Event** trigger.  
   - Click **Connect** → authorize Make to access your Calendly account.  
   - Select the calendar event “Client Onboarding Call”.  
   - Click **Continue**.  
   - Add an action: search for **Klaviyo** → select **Add/Update Subscriber**.  
   - Connect to Klaviyo → authorize with your API key (found under Settings → Account & Settings → API Keys).  
   - Map fields:  
     - Email → `{{Calendly.event.attendee.email}}`  
     - First Name → `{{Calendly.event.attendee.first_name}}`  
     - List ID → choose `Client Onboarding`.  
   - Click **Save** → **Run once** to test.  
   - *Expected output:* The test shows “Subscriber added to Klaviyo” with the subscriber’s email.  

5. **Confirm the Subscriber Appears in Klaviyo**  
   - Return to Klaviyo → **_Lists & Segments_** → **Client Onboarding** → **Members** tab.  
   - You should see the new subscriber with the email captured from Calendly.  
   - *Interactive check‑in:*  
     - **Do you see the new subscriber listed?**  
     - **If not,** refresh the page, double‑check the Make.com scenario ran successfully, and ensure the API key is correct.  

---

**[Continue with email nurture flow creation]**

6. **Create a New Flow**  
   - In Klaviyo, click **Flows** in the left nav.  
   - Click **+ NEW FLOW** → choose **_Start from Scratch_**.  
   - Name the flow `Onboarding Nurture`.  
   - Click **_Create Flow_**.  
   - *Expected output:* You’re taken to the flow canvas with a blank canvas.  

7. **Add a Trigger**  
   - Drag the **_Trigger_** node from the left panel onto the canvas.  
   - In the dialog:  
     - **Trigger Type:** `Segment` → choose `Calendly Bookers`.  
   - Click **Save**.  
   - *Expected output:* A trigger node labeled “Calendly Bookers” appears connected to the rest of the flow.  

8. **Add First Email (Welcome Email)**  
   - Drag a **_Send Email_** node onto the canvas, connect it to the trigger.  
   - Click the node → **Edit Email**.  
   - In the email editor:  
     - **Subject:** `Welcome to Your New Service!`  
     - **From Name:** `Your Company`  
     - **From Email:** `support@yourcompany.com`  
     - **Body:** Use Canva to design a simple welcome banner:  
       - Open `https://www.canva.com/create/email-

## Check-In: Module 5 Complete

- [ ] Build a High‑Conversion Landing Page on Shopify completed and verified
- [ ] Configure Lead Generation with Apollo.io completed and verified
- [ ] Create Automated Email Nurture Sequence in Klaviyo completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 6: DELIVERY

## Overview  
Module 6 is the linchpin that turns your AI‑powered onboarding designs into live, revenue‑generating services. By mastering this section you learn how to orchestrate end‑to‑end workflows that greet every new customer with a smooth, personalized experience—no manual touch required. Skipping this module means delivering half‑finished integrations, leaving clients frustrated, and losing repeat business. Every click, API call, and email blast must be vetted through our quality checkpoints, ensuring that your clients receive consistent, error‑free onboarding flows that drive retention and upsell opportunities.

We will build a delivery pipeline that includes a repeatable deployment routine, a clear set of acceptance criteria, and a library of client‑facing communication templates. You’ll also learn how to use data‑driven dashboards to monitor live performance, trigger alerts on anomalies, and iterate quickly. The end result is a turnkey system that you can hand off to clients with confidence, while still retaining the ability to tweak and expand the workflows on demand.

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| Calendly | Scheduling & automated calendar invites | 1 event type, 5 team members | $8/month (Pro) |
| Klaviyo | Email & SMS onboarding automation | 250 contacts, 500 emails/month | $20/month (Starter) |
| Make.com | Low‑code workflow orchestration | 1,000 operations/month | $29/month (Starter) |
| Replit | Code sandbox for quick script tests | Unlimited public projects | $7/month (Hacker) |
| Zapier | Connectivity between Calendly/Klaviyo and other apps | 5 Zaps, 100 tasks/month | $19.99/month (Starter) |
| Microsoft Excel | Data export & analysis | Free (online) | $6/month (Office 365 Personal) |

Estimated Time to Complete: **7–9 hours** (includes setting up integrations, creating templates, and performing end‑to‑end testing).

---

## Procedure 6.1: Deploy the Product to Production on Hostinger

1. **Log in to Hostinger**  
   - Open your browser and go to **https://www.hostinger.com**.  
   - Click **Login** in the top‑right corner.  
   - Enter your **username** and **password** then click ****LOGIN**.  
   - *Expected result*: You should see the **hPanel dashboard** with a green “Welcome” banner.

2. **Create a new web hosting plan**  
   - In the left sidebar, click **Web Hosting** → **Add New**.  
   - Choose the **Business Starter** plan (starts at **$1.99/month** with 10 GB SSD, 50 GB transfer).  
   - Click **Select** → **Proceed to Checkout**.  
   - Enter payment details and click ****PAY**.  
   - *Interactive Check‑in*: Do you see the new hosting plan listed under “My Hosting”? If not, refresh the page or contact Hostinger support.  

3. **Launch the hPanel for the new site**  
   - In the **My Hosting** section, click the **Launch** button next to your new plan.  
   - The hPanel opens in a new tab.  
   - *Expected result*: Home page of hPanel with “Welcome to your new hosting plan” banner.  

4. **Create a MySQL database**  
   - In hPanel, find **Databases** → **MySQL Databases**.  
   - In **Create new database**, type **onboarding_db** then click ****Create**.  
   - Under **Add user to database**, enter user **onboard_user** with password **StrongPass!23** and click ****Create**.  
   - *Interactive Check‑in*: Do you see “onboarding_db” listed? If not, double‑check the name or try creating again.

5. **Upload website files via FTP**  
   - Open **FileZilla** (free, 0 GB data transfer per month).  
   - In the top menu, click **File** → **Site Manager** → **New Site**.  
   - Set **Host** to your Hostinger domain (e.g., **example.com**).  
   - **Protocol**: **SFTP - SSH File Transfer Protocol**.  
   - **Logon Type**: **Normal**.  
   - **User**: **your_hostinger_ssh_user** (found in hPanel → **SSH Access**).  
   - **Password**: your SSH password.  
   - Click **Connect**.  
   - Drag your project folder from the local pane to the `/public_html/` folder.  
   - *Expected result*: All files appear in `/public_html/` with a green check mark.  

6. **Set file permissions**  
   - In FileZilla, select all uploaded files.  
   - Right‑click → **File Permissions…**.  
   - Set numeric value to **644** for files and **755** for folders.  
   - Click **OK**.  
   - *Interactive Check‑in*: Do you see the permission numbers change? If not, try refreshing FileZilla.  

7. **Edit the `.env` configuration**  
   - In hPanel, open **File Manager** → `/public_html/`.  
   - Click **Edit** on the `.env` file.  
   - Replace placeholders:  
     ```
     DB_HOST=localhost
     DB_DATABASE=onboarding_db
     DB_USERNAME=onboard_user
     DB_PASSWORD=StrongPass!23
     ```
   - Click **Save**.  
   - *Expected result*: The `.env` file shows the new credentials.  

8. **Install Composer dependencies (via SSH)**  
   - In hPanel, click **Terminal**.  
   - In the terminal, run:  
     ```
     cd public_html
     composer install --no-dev
     ```
   - *Interactive Check‑in*: If you see “Installing dependencies…”, the command is running. If you see an error “composer: command not found”, you must install Composer first (see Hostinger docs).  

9. **Run database migrations**  
   - Still in the terminal, execute:  
     ```
     php artisan migrate
     ```
   - *Expected result*: “Migrated: 12 tables”.  

10. **Configure DNS**  
    - In hPanel, go to **Domains** → **DNS**.  
    - Point the **A record** for `@` to Hostinger’s IP (e.g., `165.227.165.165`).  
    - Set **TTL** to **3600**.  
    - Add an **ALIAS** record for **www** pointing to `@`.  
    - *Interactive Check‑in*: Do you see the new records? If not, double‑check the IP address.

11. **Enable Let’s Encrypt SSL**  
    - In hPanel, click **SSL** → **Let’s Encrypt**.  
    - Select your domain, tick the box for **Force HTTPS**, then click ****Install**.  
    - *Expected result

---

## Procedure 6.2: Build Quality Assurance and Client Communication Templates

1. **Navigate to Calendly**  
   - Open your browser and go to **https://calendly.com/**.  
   - If you are not logged in, click **“Log in”** in the upper‑right corner and enter your credentials.  

2. **Create a New Event Type**  
   - Click the blue **“+ New Event Type”** button on the dashboard.  
   - Choose **“One‑time event”** and click **“Continue”**.  

3. **Define Event Details**  
   - **Event name**: type *“AI Onboarding Call”*.  
   - **Location**: select **“Zoom”** (Calendly will auto‑populate a Zoom link).  
   - **Duration**: set to **30 minutes**.  
   - Click **“Continue”**.  

4. **Add Custom Questions**  
   - In the **“Invitee questions”** section, click **“Add question”**.  
   - **Question type**: choose **“Multiple choice”**.  
   - **Question text**: *“What is your company’s primary industry?”*.  
   - Add two options: *“Tech”* and *“Retail”*.  
   - Click **“Save”**.  

5. **Set Up Email Confirmation**  
   - Under **“Notifications & Cancellation policy”**, toggle **“Send a confirmation email”** to **ON**.  
   - In the **“Email body”** field, paste:  
     ```
     Hi {{invitee.firstName}},
     
     Thanks for scheduling your AI Onboarding Call.  
     Your call is confirmed for {{invitee.eventDateTime}}.  
     
     Regards,  
     [Your Name]
     ```  
   - Click **“Save & Close”**.  

   **Do you see the “AI Onboarding Call” event listed under your scheduled events?**  
   If not, go back to the dashboard and verify the event is **published** (look for the green status badge).  

6. **Open Klaviyo**  
   - In a new tab, go to **https://www.klaviyo.com/**.  
   - Log in or create an account using your email.  

7. **Create a New List**  
   - Click **“Lists & Segments”** in the left sidebar.  
   - Press the **blue “+ New List”** button.  
   - **Name**: *“AI Onboarding Leads”*.  
   - Click **“Create List”**.  

8. **Import Contacts (Optional)**  
   - If you already have a CSV of leads, click **“Import Contacts”**.  
   - Upload the file, map columns (e.g., **First Name**, **Last Name**, **Email**), and click **“Import”**.  

9. **Create an Email Template**  
   - Navigate to **“Email Templates”** → **“Create Template”**.  
   - Choose **“Drag & Drop”**.  

10. **Design the Template**  
    - Drag a **Text block** onto the canvas.  
    - Insert the following content:  
      ```
      Subject: Welcome to Your AI Onboarding Journey
      Body:
      Hi {{firstName}},
      
      Thank you for scheduling your AI Onboarding Call. Your session is set for {{eventDateTime}}.  
      
      In the meantime, please review the attached onboarding guide (link).  
      
      Best,  
      [Your Name]
      ```  
    - Replace **{{

## Check-In: Module 6 Complete

- [ ] Deploy the Product to Production on Hostinger completed and verified
- [ ] Build Quality Assurance and Client Communication Templates completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 7: SCALING

## Overview

Module 7 equips you to transition from a solo AI‑onboarding operator to a scalable service organization. You’ll learn how to design and automate end‑to‑end onboarding workflows using Calendly for scheduling and Klaviyo for email nurturing, then extend those flows with Make.com to connect data across your stack. The module breaks down the entire scaling journey: hiring your first contractor, authoring SOPs for delegation, and rigorously analyzing margins to ensure every dollar invested drives revenue. If you skip this module, your funnel will remain a one‑person bottleneck, limiting growth, inflating costs, and compromising client experience.

You’ll also tackle the practicalities of scaling: defining role responsibilities, creating clear handover documents, and setting up automated performance dashboards. The learning culminates in a margin analysis worksheet that compares projected revenue against fixed and variable costs, allowing you to set realistic pricing tiers and forecast profitability. By the end, you’ll have a repeatable, low‑overhead system that can be replicated for multiple clients without sacrificing quality.

| Tool       | Purpose                                  | Free Tier                 | Paid Tier (Typical)                     |
|------------|------------------------------------------|---------------------------|-----------------------------------------|
| Calendly   | Appointment scheduling & sync            | 1 event type, 2 users     | Pro: $10/month per user                 |
| Klaviyo    | Email marketing & automation             | 250 contacts, 500 emails | Starter: $20/month for 500 contacts    |
| Make.com   | Workflow automation & API integration    | 500 operations/month      | Basic: $29/month for 25k operations    |
| ChatGPT    | Content creation & copy editing          | 3,000 tokens/day          | Plus: $20/month for 100k tokens        |

**Estimated time to complete Module 7:** **3 – 4 hours** (includes hiring SOPs, workflow setup, and margin analysis).

---

## Procedure 7.1: Hire Your First Contractor on Upwork

1. **Open the Upwork website**  
   - URL: https://www.upwork.com/  
   - In the top right corner, click the button labeled **“Sign Up”**.  
   - Select **“I’m a client”** and click **“Continue”**.  
   - Fill in the email, password, and company name fields.  
   - Click **“Create account”**.  
   - Expected result: You should see the Upwork dashboard with the “Find Talent” tab highlighted.  

2. **Verify your email**  
   - Check your inbox for the Upwork verification email.  
   - Click the **“Verify Email”** link inside the email.  
   - You should be redirected to the Upwork dashboard with a green “Email Verified” banner.  

3. **Add a payment method**  
   - Hover over your profile picture and click **“Account Settings”**.  
   - Navigate to **“Billing & Invoices”** → **“Add a payment method”**.  
   - Choose **“Credit Card”**, enter your card details, and click **“Save”**.  
   - Expected result: Your card status shows “Verified”.  

4. **Create a new job posting**  
   - Click **“Post a Job”** in the top menu.  
   - Enter the job title: **“AI Onboarding Workflow Designer (Calendly + Klaviyo)”**.  
   - In the “Job description” field, paste the following:  
     ```
     We need a contractor to design, optimize, and deploy an AI‑powered customer onboarding workflow using Calendly for scheduling and Klaviyo for email automation. Must have experience with Make.com (Integromat) for integration and be able to produce a step‑by‑step SOP. Deliverables include a functional workflow, SOP document, and a short video walkthrough (use Loom).  
     ```  
   - Set the budget to **$300–$500**.  
   - Set the duration to **4–6 weeks**.  
   - Click **“Post Job”**.  

5. **Interact with candidates**  
   - After posting, go to the **“Jobs”** tab, then **“All Jobs”** → **“Clicks”**.  
   - Sort by **“New”** to see the newest proposals.  
   - For each proposal, click **“Message”**.  
   - Send a templated message:  
     ```
     Hi [Name],  
     Your profile looks great. Could you share a brief example of a Calendly‑Klaviyo workflow you’ve built?  
     Thanks!  
     ```  

6. **Screen candidates**  
   - Create a Google Sheet (use Google Sheets free tier).  
   - In column A, list candidate names.  
   - In column B, note their hourly rate.  
   - In column C, mark **“Calendly+Klaviyo”** skill if confirmed.  
   - Use the **“Sort range”** → **“Sort by column B”** (ascending) to prioritize cost.  

7. **Schedule interviews**  
   - Open **Calendly** (https://calendly.com/).  
   - Click **“New Event Type”** → **“One‑to‑One”**.  
   - Title: **“Upwork Contractor Interview”**.  
   - Set duration to **30 min** and pick the next available time slot.  
   - Click **“Done”** and copy the invitation link.  
   - In the candidate’s message, paste the link and say:  
     ```
     Please book a 30‑minute interview slot here: [link].  
     ```  

8. **Conduct the interview**  
   - Join the interview via Zoom (free tier).  
   - Ask:  
     - “How many Calendly‑Klaviyo workflows have you built?”  
     - “Show me a recent workflow (you can use a screen share).”  
     - “What integration tool do you use? (Make.com or Zapier)?”  
   - Record the call with **Loom** (https://www.loom.com/).  
   - After recording, download the video and upload it to **Google Drive**.  

9. **Evaluate technical skills**  
   - Review the candidate’s Loom video.  
   - Open the **Make.com** (https://www.make.com/) dashboard.  
   - Check if the candidate has used **“Scenario”** with **“Calendly”** and **“Klaviyo”** modules.  
   - Expected output: A functioning scenario that triggers on Calendly event creation and sends a welcome email via Klaviyo.  

10. **Select a contractor**  
    - In the Google Sheet, add a new column **“Score”**.  
    - Score each candidate on:  
      - Calendly skill (1–5)  
      - Klaviyo skill (1–5)  
      - Integration expertise (1–5)  
      - Budget fit (1–5)  
    - Sum the scores.  




---

**Support Pollinations.AI:**

---

🌸 **Ad** 🌸
Powered by Pollinations.AI free text APIs. [Support our mission](https://pollinations.ai/redirect/kofi) to keep AI accessible for everyone.

---

## Procedure 7.2: Build SOPs for Task Delegation in Notion

1. **Open** your web browser and navigate to **https://www.notion.so**.  
   - Log in with your credentials.  
   - If you are new, sign up with your email, then click **“Create a free account”**.  
   - Expected result: You see the Notion dashboard with a left‑hand sidebar.

2. In the sidebar, click the **“+ New page”** button (bottom left).  
   - Title the page **“Task Delegation SOP”** and press **Enter**.  
   - Click the icon left of the title and choose the **“Table”** template from the dropdown.  
   - Expected result: A new full‑width table appears titled **“Task Delegation SOP”**.

3. Rename the first column header from **“Name”** to **“Task”** by clicking the header, typing **“Task”**, and pressing **Enter**.  
   - Add a second column by clicking the **“+ Add a property”** button on the right.  
   - Select **“Select”** and name it **“Status”**.  
   - Add a third property, choose **“Person”**, name it **“Assignee”**.  
   - Add a fourth property, choose **“Date”**, name it **“Due Date”**.  
   - Expected result: Four columns labeled Task, Status, Assignee, Due Date.

4. Create a new row for the first task:  
   - Click **“+ New”** at the bottom of the table.  
   - In the **Task** cell, type **“Create onboarding workflow for client X”**.  
   - In **Status**, select **“Not Started”**.  
   - In **Assignee**, type the name of the team member and select from the list.  
   - In **Due Date**, click the calendar icon, pick **today + 7 days**, and press **Enter**.  
   - Expected result: Row populated with the task details and colored status tag **Not Started**.

5. **Do you see** the row you just created with all four columns filled? **If not,** verify each field was entered correctly and that you pressed **Enter** after each entry.  

6. Click the **three dots** (**⋮**) in the top-right corner of the page and select **“Template”** → **“Create new template.”**  
   - Name the template **“Task”**.  
   - In the template editor, click **“+ Add a property”** and add a **“Checkbox”** property called **“Completed”**.  
   - Add a **“Rich Text”** property called **“Notes.”**  
   - Click **“Save”** and then **“Close.”**  
   - Expected result: A template named “Task” appears in the page sidebar.

7. **Do you see** the new “Task” template listed? **If not,** ensure you clicked **“Save”** before closing the editor.

8. Open your browser and go to **https://www.make.com**.  
   - Sign in or sign up for a free account.  
   - In the dashboard, click **“Create new scenario.”**  
   - Search for **“Calendly”** in the app list, click it, and choose **“New Event”** trigger.  
   - Follow the prompts to connect your Calendly account (click **“Add a connection”**, paste the API key, then click **“Authorize.”**)  
   - Expected result: A scenario canvas with a **Calendly > New Event** box.

9. Drag a **“HTTP”** module from the left panel to the canvas.  
   - Configure it to send a **POST** request to **https://api.notion.com/v1/pages**.  
   - In the request body, paste the following JSON template, replacing placeholders with variable names from the Calendly trigger:

   ```json
   {
     "parent": { "database_id": "YOUR_NOTION_DATABASE_ID" },
     "properties": {
       "

---

## Procedure 7.3: Run a Margin Analysis and Pricing Review

1. **Open Notion**  
   - Visit **https://www.notion.so**.  
   - Click **SIGN IN** in the top‑right corner and enter your credentials.  
   - Once logged in, click **+ NEW PAGE** on the left sidebar.  
   - Name the page **“Margin Analysis & Pricing Review”** and set the icon to a calculator emoji (⚙️).  
   - Do you see the new page with the title “Margin Analysis & Pricing Review”? If not, refresh the browser or re‑login.

2. **Create a Database**  
   - In the new page, type **/table full page** and select **Table – Full Page**.  
   - Click **+ ADD A COLUMN** five times to add the following columns:  
     1. **Product Name** (Title type)  
     2. **SKU** (Text)  
     3. **Cost Price** (Number, format: Currency)  
     4. **Selling Price** (Number, format: Currency)  
     5. **Margin %** (Formula)  
     6. **Status** (Select: “Under Review”, “Approved”, “Rejected”)  
   - For the **Margin %** column, click **+ Add a property → Formula** and paste:  
     `round((prop("Selling Price") - prop("Cost Price")) / prop("Selling Price") * 100, 2) & " %"`  
   - Do you see the six columns with the formula applied? If not, ensure the formula syntax matches exactly.

3. **Import Existing Product Data**  
   - Export your existing product list from Shopify as a CSV.  
   - In Notion, click **⋮** in the top‑right of the table → **Merge with CSV**.  
   - Upload the CSV file and map the columns to the database fields.  
   - After import, you should see rows populated with product names, SKUs, costs, and selling prices.  
   - If the import shows blank cells, double‑check that the CSV headers match the Notion column names exactly.

4. **Calculate Margins**  
   - The **Margin %** column will auto‑calculate for each row.  
   - Scan the table for any **Margin %** values below 20%.  
   - Highlight those rows by clicking the row selector, then clicking **⋮ → Highlight** and choosing a red color.  
   - Do you see the red‑highlighted rows with low margins? If not, verify the formula in step 2.

5. **Set Up a Klaviyo Email Template**  
   - Open **https://www.klaviyo.com** and sign in.  
   - Click **EMAILS** → **Create Email** → choose **HTML**.  
   - Name the email **“Pricing Review – Action Needed”**.  
   - In the email body, paste the following HTML snippet:  
     ```html
     <h2>Pricing Review for <b>{{ product_name }}</b></h2>
     <p>Current Selling Price: ${{ selling_price }}</p>
     <p>Cost Price: ${{ cost_price }}</p>
     <p>Margin: {{ margin_percent }}</p>
     <p>Please review and adjust pricing if margin < 20%.</p>
     ```  
   - Save the template.  
   - Do you see the new email template with the placeholder variables? If not, double‑check the variable names.

6. **Create a Make.com Scenario to Pull Data from Notion**  
   - Visit **https://www.make.com** and log in.  
   - Click **CREATE** → **Scenario**.  
   - Click **+** to add a module and search for **Notion → Database Items**.  
   - Select the database “Margin Analysis & Pricing Review”.  
   - In the module settings, set **Filter** to `prop("Margin %") < 20`.  
   - Click **+** again, search for **Klaviyo → Send Email**.  
   - Map the fields:  
     - `product_name` → **Product Name**  
     - `selling_price` → **Selling Price**  
     - `cost_price` → **Cost Price**  
     - `margin_percent` → **Margin %**  
   - Click **RUN** once to test.  
   - Expected output: A single email is sent to the address set in Klaviyo for each low‑margin product.  
   - If you see **“Invalid API Key”** in the Notion module, it means your Notion integration key is wrong. Fix it by revisiting the Notion integration in the Settings → Integrations → New Integration, copying the new key, and pasting it into the Make.com module.

7. **Schedule the Scenario**  
   - Click the clock icon in the upper right of the Make.com scenario.  
   - Set the schedule to **Every Friday at 10 AM UTC**.  
   - Confirm by

## Check-In: Module 7 Complete

- [ ] Hire Your First Contractor on Upwork completed and verified
- [ ] Build SOPs for Task Delegation in Notion completed and verified
- [ ] Run a Margin Analysis and Pricing Review completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 8: ADVANCED PATTERNS

## Overview

In this module you will master the art of building, fine‑tuning, and monetizing AI‑driven customer onboarding workflows that combine Calendly’s scheduling precision with Klaviyo’s marketing automation depth. You will learn how to layer sophisticated triggers, conditional logic, and AI‑generated content to deliver a frictionless, personalized onboarding experience for each new customer. The result is a repeatable, scalable service that can be sold as a high‑ticket offering or added as a recurring revenue stream to your existing funnel.

Skipping this module means you’ll miss the opportunity to lock in clients with a seamless, data‑rich onboarding process that keeps churn rates low and upsell potential high. Without the advanced patterns you’ll be limited to basic triggers and static emails, which many competitors already provide for free. By the end of the module you’ll be able to package these workflows as a turnkey product, upsell premium AI enhancements, and generate predictable monthly revenue from a single client.

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| Calendly | Appointment scheduling, calendar sync, and webhook triggers | Unlimited free events, 1 calendar integration | Pro ($8/mo billed annually) – 10 calendars, custom branding, integrations |
| Klaviyo | Email & SMS automation, segmentation, AI‑powered content | Unlimited contacts, 500 emails/month | Growth ($20/mo billed annually) – 2,000 emails/mo, advanced segmentation |
| Make.com | Low‑code automation, multi‑step workflows, API integration | 1,200 operations/month | Starter ($9/mo) – 12,000 ops, advanced connectors |
| Replit | Coding sandbox for custom scripts | Unlimited use, 500 MB storage | Pro ($7/mo) – 2 GB storage, private repos |
| ElevenLabs | AI voice generation for onboarding scripts | 5 hours free | Starter ($15/mo) – 20 hours, higher quality voices |

**Estimated Time to Complete:** 3 hours 45 minutes (includes tool setup, workflow design, testing, and packaging for sale).

---

## Procedure 8.1: Create a High‑Ticket Consulting Package

1. **Open a web browser** and go to the Calendly homepage:  
   <https://calendly.com>.  
2. **Click the blue button** that says **“Sign up”** (top right).  
   - Enter your **email** (e.g., `you@yourdomain.com`), **first name**, **last name**, and **password**.  
   - Click **“Create account”**.  
3. **Confirm your email** by clicking the link sent to your inbox.  
4. **Log in** again to Calendly.  
   - You should see the **Dashboard** with a “Welcome” banner and an **“Add event type”** button.  
   - **Do you see the “Add event type” button?** If not, ensure you’re on the **Calendly.com** domain and refresh the page.  

**Expected Output:** You should now be on Calendly’s main dashboard, ready to create a new event.

5. **Click the bold button** **“Add event type”**.  
6. **Choose “One‑on‑one”** and click **“Next”**.  
7. **Enter the event title** “High‑Ticket Consulting Call”.  
   - Set **location** to “Zoom” (Calendly will auto‑create a Zoom link).  
   - Set **duration** to **30 minutes**.  
   - Click **“Done”**.  
8. **Under “Availability”** set **“Every weekday, 10 AM – 4 PM”**.  
   - Click **“Save… and add questions”**.  

**Check‑in 1:**  
Do you see the “Add questions” screen with default “Name” and “Email” fields? If not, click **“Edit questions”** in the top right corner.

9. **Add a new question**:  
   - Click **“+ Add question”**.  
   - Set **label** to **“Company”**.  
   - Choose **“Single line answer”**.  
   - Toggle **“Required”** on.  
   - Click

---

## Procedure 8.2: Deploy Subscription Onboarding Workflow

**Objective:** Create a seamless AI‑powered onboarding funnel that uses Calendly to schedule a kickoff call, Klaviyo to nurture the lead, and Shopify to sell and manage subscription tiers. Follow each instruction exactly; this is the only path to a functioning recurring‑revenue engine.

---

### 1. Set Up the Shopify Subscription Product

1. Open your web browser and go to **https://www.shopify.com**.  
2. Log in with your merchant credentials.  
3. From the Admin dashboard, click **Products** → **All products** → **Add product** (button in the top‑right).  
4. In the product form, type **Premium AI Onboarding Package** in the **Title** field.  
5. In the **Description** box, paste the following (copy exactly, including line breaks):

```
Subscribe to our AI‑powered customer onboarding system.  
Monthly fee: $29.  
Features:  
 • 1‑on‑1 kickoff call via Calendly  
 • Customized onboarding checklist in Klaviyo  
 • Unlimited AI‑generated welcome emails  
```

6. Under **Pricing**, click **Set price** → **Price**: **$29.00**.  
7. Click the **+** icon next to **Compare at price** and set it to **$39.00**.  
8. Scroll to **Inventory** → **Track quantity** → **No** (unlimited).  
9. Drag the **Product image** placeholder to add a banner image from your local drive.  
10. Click **Save product** (bottom‑right).  

**Expected Result:** A new product page titled “Premium AI Onboarding Package” appears in the product list with a price of $29.00.

---

#### Check‑In 1  
**Do you see the new product listed under “All products” with the correct price?**  
*If not,* verify you are on the correct store and that you clicked **Save product**. In Shopify, the product will appear immediately upon saving.

---

### 2. Enable Shopify Subscriptions

11. From the Admin menu, navigate to **Apps** → **Find more apps**.  
12. Search for “Shopify Subscriptions” and click **Add app**.  
13. In the app installation dialog, click **Install app**.  
14. Once installed, open the app and click **Create plan** → **Monthly**.  
15. In the plan editor, set **Plan name** to **Premium AI Onboarding** and **Price** to **$29.00**.  
16. Under **Billing details**, set **Trial period** to **7 days**.  
17. Click **Save plan**.  

**Expected Result:** The subscription plan “Premium AI Onboarding” is now available in the Shopify product page under **Variants** → **Add variant** → **Subscription**.

---

#### Check‑In 2  
**Do you see the “Subscription” variant added to the product?**  
*If not,* ensure you are in the product’s variant section and that the Shopify Subscriptions app is active. Try refreshing the page.

---

### 3. Create a Calendly Event Type for the Kickoff Call

18. Open a new tab and go to **https://calendly.com**.  
19. Log in or sign up for the free tier.  
20. On the dashboard, click **Event types** → **New event type** → **One‑on‑one**.  
21. Name the event **AI Onboarding Kickoff**.  
22. Set **Location** to **Zoom** (you must have a Zoom account linked).  
23. In the **Availability** tab, set a default slot of **30‑minute appointments**.  
24. Under **Invitee Questions**, add a single field: **Company Name** (short answer).  
25. Click **Save & close**.  

**Expected Result:** A new Calendly event URL appears in the **Event types** list.

---

#### Check

## Check-In: Module 8 Complete

- [ ] Create a High‑Ticket Consulting Package completed and verified
- [ ] Deploy Subscription Onboarding Workflow completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 9: FINANCIAL OPERATIONS

## Overview

This module equips you with the financial infrastructure necessary to monetize AI‑driven onboarding workflows. You’ll learn how to set up a revenue‑tracking dashboard that captures every dollar earned from Calendly appointments and Klaviyo email campaigns, how to implement dynamic pricing models for tiered onboarding packages, and how to generate professional proposal and contract templates that close deals faster. The focus is on turning your service into a scalable, data‑driven revenue generator rather than a one‑off engagement.

Skipping this module will leave you with a beautiful onboarding system that earns no money or, worse, operates on an untracked cash flow that blinds you to profitability. Without real‑time financial metrics you’ll be unable to justify pricing increases, negotiate with clients, or forecast growth. In short, you’ll be “flying blind” while competitors build automated revenue engines that keep money in the bank.

| Tool        | Purpose                                                  | Free Tier | Paid Tier (monthly) |
|-------------|----------------------------------------------------------|-----------|---------------------|
| Calendly    | Schedule client onboarding appointments                  | Unlimited 5 events, 1 calendar | $10 (Pro) – unlimited events, advanced features |
| Klaviyo     | Automate onboarding email sequences & revenue tracking  | 500 contacts, 3,000 emails | $20 (Starter) – 3,000 contacts |
| Make.com    | Orchestrate workflows between Calendly, Klaviyo, and accounting | 500 operations | $49 (Pro) – 5,000 operations |
| Notion      | Store proposal templates and contract boilerplates       | Unlimited pages & databases | $8 (Personal Pro) – advanced integrations |
| Hostinger   | Host a simple static website for invoices & contracts   | 100 GB bandwidth | $3.95 (Single Shared) – 100 GB bandwidth |

Estimated time to complete this module: **3.5 – 4 hours** (including dashboard setup, pricing model calibration, and template generation).

---

## Procedure 9.1: BUILD a Live Revenue Dashboard in Notion with Make.com  

1. **Open your web browser** → navigate to https://www.notion.so/.  
   - If you are not yet a Notion user, click **SIGN UP** (top‑right), enter your email, confirm, and log in.  
   - **Expected output:** You are on the Notion home screen with the left‑hand sidebar showing “Workspace”, “Friends”, “Templates”, etc.  

2. **Create a new database** → click the **+ NEW PAGE** button at the bottom of the sidebar, then select **Table – Full page**.  
   - Title the page **“Live Revenue Dashboard”** and press **ENTER**.  
   - **Check‑in:** Do you see a blank table with columns *Name*, *Tags*, *Created*? If not, scroll down until the table appears.  

3. **Add required columns** →  
   - Click the header of **Name**, rename it to **Client**.  
   - Click the **+** icon to the right of the last column and select **Date** → rename to **Date**.  
   - Add a **Number** column → rename to **Revenue**.  
   - Add a **Text** column → rename to **Notes**.  
   - **Expected output:** The table now has four columns: Client, Date, Revenue, Notes.  

4. **Save the database URL** → click the **•••** menu in the top‑right corner of the page and select **Copy link**.  
   - Store this URL in a secure note for later use.  
   - **Check‑in:** Do you see the link copied to your clipboard? If not, click **Copy link** again.  

5. **Open Make.com** → go to https://www.make.com/en.  
   - Click **SIGN IN** if you already have an account; otherwise click **SIGN UP** and register with your email.  
   - **Pricing note:** Free tier → 100 operations/month, 1 scenario, 5‑minute delay. Paid plan starts at $25/month for 2,000 operations.  

6. **Create a new scenario** → click **CREATE** → **NEW SCENARIO**.  
   - **Check‑in:** Do you see the blank canvas with a plus (+) icon in the center? If not, refresh the page.  

7. **Add Calendly trigger** → click the **+** icon, type “Calendly” in the search bar, select **Calendly – Webhook** → choose **When a new event is scheduled**.  
   - Click **CONNECT** → paste your Calendly API key (found under *Integrations → API Key* in your Calendly account).  
   - **Expected output:** The Calendly module appears on the canvas, showing “Calendly – When a new event is scheduled.”  

8. **Set Calendly webhook** → click the Calendly module, then **Configure**.  
   - Choose **Event type** → “All event types”.  
   - Set **Trigger type** → “Event scheduled”.  
   - Click **SAVE**.  
   - **Check‑in:** Do you see the module with “Event scheduled” next to it? If not, ensure the correct trigger is selected.  

9. **Add Make.com HTTP request to fetch event details** → click the **+** icon next to Calendly module → search for **HTTP** → select **Make –

---

## Procedure 9.2: Create Proposal Templates and Automated Billing with Stripe

1. **Open Stripe Dashboard**  
   - URL: https://dashboard.stripe.com/login  
   - Click **LOGIN** (top‑right).  
   - Enter your registered email and password.  
   - Click **SIGN IN**.  
   *Do you see the Stripe Dashboard home page with the “Products” tab on the left? If not, re‑login or clear browser cache.*

2. **Create a New Product for Proposals**  
   - In the left sidebar, click **Products**.  
   - Click **+ NEW** (top‑right).  
   - In the **Product name** field, type `Onboarding Proposal`.  
   - Optional: Add a short description “Automated proposal and billing for new clients.”  
   - Click **SAVE PRODUCT** (bottom).  
   *Expected output: The product appears under “Products” with a status of “Active.”*

3. **Add a One‑Time Price**  
   - While viewing the product, click **+ ADD PRICE**.  
   - Set **Price type** to **One‑time**.  
   - In **Amount**, enter `150.00`.  
   - Currency: `USD`.  
   - Click **SAVE PRICE**.  
   *Result: A price ID (e.g., `price_1Y7cNq2eZvKYloBf...`) is generated.*

4. **Create a Stripe Checkout Session URL**  
   - In the browser, go to https://dashboard.stripe.com/test/checkout.  
   - Click **CREATE CHECKOUT SESSION** (top‑right).  
   - For **Payment method types**, leave defaults.  
   - In **Line items**, click **+ ADD ITEM**.  
   - Field **Price**: paste the price ID from step 3.  
   - Field **Quantity**: `1`.  
   - Click **CREATE**.  
   - Copy the **Session URL** displayed (e.g., `https://checkout.stripe.com/pay/cs_test_...`).  
   *Do you see the Session URL? If not, ensure the price ID is correct.*

5. **Set Up Stripe Billing for Invoices**  
   - In the left sidebar, click **Billing** → **Invoices**.  
   - Click **+ CUSTOMIZE** (top‑right).  
   - In **Invoice template**, set **Logo URL** to your company logo (e.g., `https://example.com/logo.png`).  
   - Set **Footer** to “Thank you for choosing Menshly Global.”  
   - Click **SAVE**.  
   *Expected output: Invoice preview shows the new logo and footer.*

6. **Create Klaviyo Email List**  
   - Open a new tab: https://www.klaviyo.com/login  
   - Click **SIGN IN** (top‑right).  
   - Enter credentials, click **LOGIN**.  
   - In the dashboard, click **Lists & Segments** → **Create List**.  
   - Name the list `New Onboarding Clients`.  
   - Click **CREATE LIST**.  
   *Do you see the new list in the sidebar? If not, refresh the page.*

7. **Build a Proposal Email Template in Klaviyo

## Check-In: Module 9 Complete

- [ ] BUILD a Live Revenue Dashboard in Notion with Make.com completed and verified
- [ ] Create Proposal Templates and Automated Billing with Stripe completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 10: LAUNCH PLAN

## Overview

In this module you will build a fully automated AI‑powered customer onboarding workflow that leverages Calendly for scheduling, Klaviyo for email automation, and Make.com for orchestrating the data flow between them. The day‑by‑day execution calendar will guide you through every step—from setting up the Calendly event types, to scripting the welcome email content in Klaviyo, to testing the entire flow in Make.com. By the end of 30 days you will have a proven, repeatable system that can deliver an onboarding experience to a new client in under 48 hours, with a clear path to upsell or cross‑sell.

Skipping this module means you’ll launch without a validated onboarding process, risking lost leads, inconsistent customer communication, and a diluted brand experience. It also removes the opportunity to capture early data on customer behavior, which is essential for iterative improvement and future personalization. The structured timeline ensures you allocate the right amount of time to each tool’s configuration, reduce costly trial‑and‑error, and hit the first paying client before the end of the month.

**Tools Needed**

| Tool        | Purpose                                                     | Free Tier                                | Paid Tier (Lowest) |
|-------------|-------------------------------------------------------------|------------------------------------------|--------------------|
| Calendly    | Schedule onboarding calls, set up automated reminders       | 1 calendar, 1 user, basic branding       | Professional – $10 / month |
| Klaviyo     | Send welcome emails, drip campaigns, track engagement      | 250 contacts, 500 emails/month           | Starter – $20 / month |
| Make.com    | Orchestrate data between Calendly, Klaviyo, and other APIs | 1,000 operations/month, 5 apps          | Basic – $9 / month   |
| Zapier      | Quick fallback integration for edge cases                  | 5 zaps, 100 tasks/month                  | Starter – $19.99 / month |
| Notion      | Project planning, task board, documentation                | Unlimited pages, guests                  | Personal Pro – $4 / month |
| Loom        | Record walkthroughs for clients and internal training      | 25 min per recording, 5 recordings/month | Business – $12 / month |

**Estimated Time to Complete**

- **Planning & Setup**: 3 hours (spread across 5 days)
- **Configuration & Testing**: 8 hours (spread across 10 days)
- **Launch & First Client**: 2 days (day 15–16)
- **Iterative Refinement**: 4 days (day 20–24)

Total: **≈ 17 days of focused work** within the 30‑day framework.

---

## Procedure 10.1: Configure Calendly to Trigger Klaviyo Workflow

**Objective:** Set up Calendly to send a webhook to Make.com, which then pushes the attendee data into a Klaviyo workflow. This will automate the first‑touch onboarding email to every new customer.

---

### Step‑by‑Step Instructions

1. **Open Calendly**  
   - Launch a browser and go to **https://calendly.com**.  
   - Click the **blue “Log in” button** in the upper‑right corner.  
   - Enter your credentials and click **“Log in”** again.  
   - *Expected output:* You see your dashboard with a list of event types.

2. **Create a New Event Type**  
   - Click **“New event type”** (orange button).  
   - Choose **“One‑on‑one”** and click **“Continue”**.  
   - In the “Event name” field, type **“AI Onboarding Call”**.  
   - Set **Duration** to **30 minutes** and click **“Continue”**.  
   - *Expected output:* You are on the “Invitee Questions” page.

3. **Add Custom Questions**  
   - Click **“Add a question”** (green plus icon).  
   - Choose **“Short answer”**.  
   - Label it **“Customer Name”** and toggle **“Required”** on.  
   - Repeat to add **“Email Address”** (short answer, required).  
   - Click **“Done”**.  
   - *Expected output:* Two new questions appear in the list.

4. **Set Availability**  
   - Click **“Availability”** tab.  
   - Toggle **“Busy times”** off.  
   - Set **“Working hours”** to **9 AM – 5 PM** (your local time).  
   - Click **“Save & Close”**.  
   - *Expected output:* Event type saved and visible in the dashboard.

5. **Check‑in**  
   - **Do you see “AI Onboarding Call” listed under your event types?**  
   - *If not,* scroll down or refresh the page. If still missing, go back to **Step 1** and ensure you saved the event correctly.

6. **Generate a Calendly Webhook URL**  
   - In the Calendly dashboard, click **“Integrations”** top‑right.  
   - Click **“Webhooks”** (under “Automation”).  
   - Click **“Add webhook”** (green button).  
   - In the **“Webhook URL”** field, temporarily paste **`https://www.make.com/placeholder`** and click **“Save”**.  
   - *Expected output:* Webhook created with “Status: Pending”.

7. **Copy Webhook ID**  
   - After saving, hover over the new webhook row and click the **three‑dot menu** → **“Copy webhook ID”**.  
   - Store this ID in a safe place (we’ll need it in Make.com).  
   - *Expected output:* Clipboard contains a string like `wh_1234abcd`.

8. **Open Make.com**  
   - In a new tab, go to **https://www.make.com/en**.  
   - Click **“Sign up for free”** (top‑right).  
   - Enter your email, click **“Get Started”**, and confirm via the email link.  
   - *Expected output:* You are directed to the Make.com dashboard.

9. **Create a New Scenario**  
   - Click **“Create a new scenario”** (purple button).  
   - In the search bar, type **“Calendly”** and click the **Calendly icon**.  
   - Choose the **“Watch Events”** trigger.  
   - Click **“Continue”**.  
   - *Expected output:* Calendly trigger added to the canvas.

10. **Configure Calendly Trigger**  
    - Click the **Calendly trigger module**.  
    - In the “Webhook

---

**Procedure 10.2** — Generation failed due to AI backend unavailability. Please retry later.

---

## Procedure 10.3: **Launch First Live Onboarding Workflow to Capture New Clients**

> **Goal:** Deploy an end‑to‑end AI‑powered onboarding system that automatically captures new clients through Calendly, syncs them into Klaviyo, and fires a welcome email with a scheduling CTA.

---

### Step 1 – Create the Calendly Event

1. Open a browser and go to **https://calendly.com/**.  
2. Click **SIGN IN** (top‑right) and enter your credentials.  
3. Once logged in, click **EVENT TYPES** on the left sidebar.  
4. Click **+ NEW EVENT TYPE** (top‑right).  
5. Select **ONE‑ON‑ONE** and click **CREATE**.  
6. In the **Event Name** field, type **“AI Onboarding Call”**.  
7. In **Location**, choose **Zoom** (Calendly will auto‑generate a Zoom link).  
8. Set **Duration** to **30** minutes.  
9. Click **SAVE & CLOSE** (bottom).  

> **Check‑in 1** – Do you see a new event type titled “AI Onboarding Call” listed in your dashboard?  
> *If not, confirm you’re logged into the correct Calendly account and that you clicked **SAVE & CLOSE**.*

---

### Step 2 – Add Custom Questions for Lead Capture

10. In the “AI Onboarding Call” event, click **EDIT** (pencil icon).  
11. Under **Invitee Questions**, click **+ ADD A QUESTION**.  
12. Choose **“Email”** from the dropdown, set to **Required**.  
13. Click **+ ADD A QUESTION** again, choose **“Phone”** (Optional).  
14. Click **SAVE** (top).  

> **Expected Output:** The event page now shows two new fields (Email, Phone) that will appear when a user schedules the call.  

---

### Step 3 – Configure Confirmation Emails

15. Still in the event editor, scroll to **Notifications & Cancellation Policy**.  
16. Click **Edit Email Confirmation** (link).  
17. In the editor, replace the default subject with **“Your AI Onboarding Call is Confirmed”**.  
18. In the body, add a friendly message:  
    ```
    Hi {{invitee.firstName}},
    Your onboarding call is scheduled for {{invitee.eventStartTime}}.
    Click below to join: {{invitee.eventLocation}}
    ```
19. Click **SAVE & CLOSE**.  

> **Check‑in 2** – Do you see the updated subject line and body in the preview pane?  
> *If the subject didn’t change, double‑check you edited the correct email template.*

---

### Step 4 – Set Up a Klaviyo Account

20. Open a new tab and go to **https://www.klaviyo.com/**.  
21. Click **SIGN UP** (top‑right).  
22. Enter your email, first name, and a password.  
23. Choose **“I’m a small business owner”** and click **GET STARTED**.  
24. Verify your email via the link Klaviyo sends.  

> **Expected Output:** You’re now in the Klaviyo dashboard, free tier (10,000 emails/month, 250 contacts).  

---

### Step 5 – Create a List for Onboarding Leads

25. In Klaviyo, click **Lists & Segments** from the left menu.  
26. Click **CREATE LIST** (top‑right).  
27. Name the list **“Onboarding Leads”** and click **SAVE**.  

> **Check‑in 3** – Do you see “Onboarding Leads” under your lists?  
> *If not, refresh the page and confirm you clicked **SAVE**.*

---

### Step 6 – Build a Welcome Flow

28. Click **Flows** on the left sidebar.  
29. Click **+ CREATE FLOW** (top‑right).  
30. Choose **“Trigger”** → **“New Subscriber”** and select the **“Onboarding Leads”** list.  
31. Click **CONTINUE**.  

---

### Step 7 – Add an Email Message

32. Drag the **EMAIL** block to the canvas.  
33. Click **CONFIGURE EMAIL**.  
34. Set **Subject** to **“Welcome to Your AI Onboarding”**.  
35. In the body, insert a personalized greeting:  
    ```
    Hi {{ first_name }},
    Thank you for scheduling your AI onboarding call.  
    ```
36. Add a button:  
    - **Text:** “Schedule Your

## Check-In: Module 10 Complete

- [ ] Configure Calendly to Trigger Klaviyo Workflow completed and verified
- [ ] Design AI-Driven Welcome Email Sequence in Klaviyo completed and verified
- [ ] **Launch First Live Onboarding Workflow to Capture New Clients** completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# APPENDIX A: COMPLETE TOOL REFERENCE

Below is a definitive, no‑fluff reference for every tool that powers the AI‑driven customer onboarding workflow.  Treat this as your cheat‑sheet: read it, memorize the limits, and know exactly when to hit “upgrade” so your automation never stalls.

| Tool | Purpose | Free Tier | Paid Tier | When to Upgrade |
|------|---------|-----------|-----------|-----------------|
| **Hostinger** | Domain registration & low‑cost web hosting | No free tier – but the **Starter** plan starts at **$1.99 / mo** (1 GB storage, 1 TB bandwidth, 1 domain) | **Starter** $1.99 / mo – 10 GB storage, 10 TB bandwidth, 10 domains | When you need more than 1 GB storage or 1 TB bandwidth, or want to host multiple domains. |
| **Notion** | Knowledge base, SOPs, and data storage | Unlimited pages, 5,000 blocks, 1 GB file upload | **Personal Pro** $4 / mo (unlimited blocks, 5 GB upload) | Upgrade when your SOP archive exceeds 5,000 blocks or 1 GB storage. |
| **Zoho Mail** | Business email, integrated with Hostinger DNS | 5 users, 5 GB per user, IMAP/SMTP | **Mail Lite** $1 / user / mo (10 GB per user, unlimited users) | When you exceed 5 users or need >5 GB per mailbox. |
| **Calendly** | Scheduling & Calendly API | 1 user, 1 event type, 60‑min meetings | **Pro** $12 / mo (5 users, unlimited event types, 24‑hour buffer) | Upgrade when you need more than 1 user or more than 1 event type per calendar. |
| **Make.com (formerly Integromat)** | Automation platform for API triggers | 1,000 operations/month, 2 active scenarios, 1 GB storage | **Starter** $9 / mo (10,000 ops, 4 scenarios, 10 GB) | When your workflow exceeds 1,000 operations or you need more than 2 scenarios. |
| **Vapi** | Voice‑to‑text & text‑to‑voice API | 500 calls/month, 10 min total | **Starter** $0.01 / min (unlimited calls) | Upgrade when your call volume exceeds 500 per month or you need the premium voice library. |
| **ElevenLabs** | AI TTS with neural voices | 1,000 characters/month, 5 voices | **Premium** $15 / mo (25,000 characters, 10 voices, priority support) | When you need to generate >1,

# APPENDIX B: THE COMPLETE SOP INDEX  

The following index is the definitive reference for every Standard Operating Procedure (SOP) that powers our playbook on building, optimizing, and deploying AI‑driven customer onboarding workflows with Calendly and Klaviyo. Each entry is tagged with a unique SOP number, a concise procedure title, the module category, an explicit difficulty level, and an estimated completion time. Use this table as a master checklist to verify that every component of the onboarding pipeline is fully configured before you move to the next stage.  

| SOP # | Procedure | Category | Difficulty | Est. Time |
|-------|-----------|----------|------------|-----------|
| 1.1 | Register Your Business Domain on Hostinger | Foundation | Easy | 15 min |
| 1.2 | Set Up Email and Workspace in Notion | Foundation | Easy | 30 min |
| 1.3 | Create Core Business Accounts and Calendly | Foundation | Medium | 45 min |
| 2.1 | Connect ChatGPT API and Store Keys in Notion | Tech Stack | Medium | 30 min |
| 2.2 | Build Your First Make.com Automation Scenario | Tech Stack | Hard | 1 hr |
| 2.3 | Configure Vapi Voice Agent and ElevenLabs TTS | Tech Stack | Hard | 1 hr |
| 3.1 | Design Your Service Delivery Framework in Notion | Framework | Medium | 45 min |
| 3.2 | Build the Client Onboarding Automation Pipeline | Framework | Hard | 1 hr 30 min |
| 4.1 | Create the Core AI Onboarding Product in Replit | First Build | Medium | 1 hr |
| 4.2 | Build the Data Processing Pipeline with Make.com | First Build | Hard | 1 hr 30 min |
| 4.3 | Deploy and Test the Complete System | First Build | Hard | 2 hr |
| 5.1 | Build a High‑Conversion Landing Page on Shopify | Client Acquisition | Medium | 1 hr |
| 5.2 | Configure Lead Generation with Apollo.io | Client Acquisition | Medium | 45 min |
| 5.3 | Create Automated Email Nurture Sequence in Klaviyo | Client Acquisition | Medium | 1 hr |
| 6.1 | Deploy the Product to Production on Hostinger | Delivery | Medium | 30 min |
| 6.2 | Build Quality Assurance and Client Communication Templates | Delivery

# APPENDIX C: THE REVENUE CALCULATOR  

## 1. SET‑UP THE CALCULATOR IN NOTION  
1. Open **Notion** → click **+ New Page** → name it **“Revenue Calculator – AI Onboarding”**.  
2. In the new page, click **+ Add a database** → pick **Table – Inline**.  
3. Rename the table to **“Monthly Projections”**.  
4. Add the following columns with the exact types:  

| Column Name | Type | Notes |
|-------------|------|-------|
| **Month** | Title | e.g., “Month 1” |
| **Clients** | Number | Integer |
| **Revenue** | Formula | `prop("Clients") * prop("Price per Client")` |
| **Expenses** | Formula | `prop("Tool Costs") + prop("Marketing") + prop("Contractor")` |
| **Profit** | Formula | `prop("Revenue") - prop("Expenses")` |

5. Insert a second database on the same page titled **“Pricing Tiers”**. Add these columns:  

| Column | Type | Notes |
|--------|------|-------|
| **Tier** | Title | “Basic”, “Pro”, “Enterprise” |
| **Price** | Number | USD |
| **Deliverables** | Text | Description |
| **Margin** | Formula | `((prop("Price") - prop("Cost per Tier")) / prop("Price")) * 100` |

6. Insert a third database titled **“Break‑Even Analysis”**. Add these columns:  

| Column | Type | Notes |
|--------|------|-------|
| **Cumulative Revenue** | Formula | `sum(prop("Revenue") for all rows up to current)` |
| **Cumulative Expenses** | Formula | `sum(prop("Expenses") for all rows up to current)` |
| **Cumulative Profit** | Formula | `sum(prop("Profit") for all rows up to current)` |
| **Break‑Even Point** | Formula | `if(prop("Cumulative Profit") >= 0, "YES", "NO")` |

**Interactive Check‑In:**  
Do you see the three databases correctly created? If not, verify that you selected the exact column types listed above. Changing a column type after entries will corrupt formulas – delete and recreate if necessary.

## 2. ENTER YOUR BASELINE ASSUMPTIONS  
1. In the **Monthly Projections** table, add four rows labeled **Month 1**, **Month 3**, **Month 6**, **Month 12**.  
2. For each row, fill **Clients** with the projected new clients for that month (see Module 5 for acquisition rates).  
3. Add a new property in the table called **Price per Client** (Number) and set it to **$200** (one‑time onboarding fee).  
4. Add **Tool Costs** (Number) and input the monthly recurring costs:  

| Tool | Monthly Cost |
|------|--------------|
| Hostinger Domain | $1.99 |
| Calendly Pro | $10.00 |
| Klaviyo (500 contacts) | $20.00 |
| Make.com (10,000 ops) | $49.00 |
| **Total Tool Costs** | $80.99 |

5. Add **Marketing** (Number) and set it to **$300** per month for paid ads and lead‑gen tools.  
6. Add **Contractor** (Number) and set it to **$0** for Month 1, **$400** for Month 3 (first contractor), **$800** for Month 6, **$1,200** for Month 12.  
7. The **Expenses** formula will automatically sum these three fields.  
8. The **Revenue** formula will output **Clients × $200**.  

**Expected Output (Month 1):**  
- Clients: 10  
- Revenue: 10 × 200 = **$2,000**  
- Expenses: 80.99 + 300 + 0 = **$380.99**  
- Profit: 2,000 – 380.99 = **$1,619.01**

Do you see the correct numbers appear in the table? If the formulas are not calculating, double‑check that the column names match exactly and that the formula syntax uses `prop("Column Name")` with correct capitalization.

## 3. CALCULATE REVENUE PROJECTIONS  
| Month | Clients | Revenue | Expenses | Profit |
|-------|---------|---------|----------|--------|
| 1 | 10 | $2,000 | $380.99 | $1,619.01 |
| 3 | 25 | $5,000 | $490.99 | $4,509.01 |
| 6 | 50 | $10,000 | $680.99 | $9,319.01 |
| 12 | 120 | $24,000 | $1,180.99 | $22,819.01 |

*How the numbers were derived

For the free step-by-step guide, see our [implementation guide]({< ref "/intelligence/build-an-ai-bookkeeping-automation-with-zapier-the-complete-step-by-step-guide.md" >}).


## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
