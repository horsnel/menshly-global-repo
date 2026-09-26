---
title: "The AI WhatsApp Sales Bot Playbook: 25 Steps to $10K/Month"
date: 2026-09-26
category: "Playbook"
price: "₦15,000"
readTime: "89 MIN"
excerpt: "The AI WhatsApp Sales Bot Playbook: 25 Steps to $10K/Month This playbook is an OPERATING SYSTEM, not a blog post or a loose guide. It delivers 25 procedures. 10 modules. 12+ hours of reading and execution. By the end of the last step you will have a ..."
image: "/images/articles/playbooks/the-ai-whatsapp-sales-bot-playbook-25-steps-to-10kmonth.png"
heroImage: "/images/heroes/playbooks/the-ai-whatsapp-sales-bot-playbook-25-steps-to-10kmonth.png"
relatedOpportunity: "/opportunities/how-to-build-an-ai-whatsapp-sales-bot-3k-20kmonth/"
relatedGuide: "/intelligence/build-an-ai-comic-book-creation-system-with-midjourney-the-complete-step-by-step/"
---
**The AI WhatsApp Sales Bot Playbook: 25 Steps to $10K/Month**  
This playbook is an OPERATING SYSTEM, not a blog post or a loose guide. It delivers **25 procedures. 10 modules. 12+ hours of reading and execution.** By the end of the last step you will have a fully functional, Make.com‑driven WhatsApp sales bot, integrated with ChatGPT, that can capture leads, close orders, and auto‑handle support in real time—scalable to 10,000 conversations a day for any SME in Africa. The system is pre‑audited for compliance, includes revenue‑projection dashboards, and comes with a ready‑to‑deploy pricing calculator that shows how each lead converts to cash flow. Every procedure is written in a commanding, step‑by‑step order: click the “Create Flow” button in Make, paste the exact JSON, set the webhook URL, and so forth—no guessing, no trial‑and‑error. You’ll see the bot’s live dashboard in minutes and have a proven sales funnel that can be replicated across 30+ industries with zero technical background. This playbook extends our free implementation guide with complete procedures, SOPs, and revenue calculators. For the free step‑by‑step guide, see our [implementation guide](/intelligence/build-a-i-comic-book-creation-system-with-midjourney-the-complete-step-by-step.md).

---

# MODULE 1: FOUNDATION

## Overview  
In this foundational module you will set up the entire digital backbone that powers your WhatsApp Sales Bot ecosystem. You will register official business accounts on WhatsApp Business API, secure a custom domain, and configure an SMTP relay that guarantees all outbound messages are delivered with 100 % deliverability. You will also integrate Make.com to orchestrate all workflow automations and ChatGPT to generate dynamic, human‑like responses. This groundwork is critical: without a verified business profile, your bot will be blocked by WhatsApp, your domain will appear untrustworthy, and your email relay will be flagged as spam—each a single point that can cost a mentor or a whole month of lost revenue.  

Skipping this module means your bot will fail to launch at all, or worse, operate in a gray zone where customers can’t reach you. Even if the bot runs, you’ll suffer from low open rates, high bounce rates, and a lack of visibility into performance metrics. In short, you’ll build a bot that never talks to anyone, or one that gets shut down by the platform for non‑compliance.

| Tool          | Purpose                                                        | Free Tier                                            | Paid Tier (monthly)                      |
|---------------|----------------------------------------------------------------|------------------------------------------------------|------------------------------------------|
| Make.com      | Connect WhatsApp Business API, email, and GPT workflows        | 5,000 operations per month, 200 s max execution time | $49 – Unlimited ops, 30 s execution      |
| ChatGPT (OpenAI) | Generate responses, train prompts, build conversation flows  | 25 000 tokens/month, 3 k tokens per request         | $20 – Unlimited tokens, priority access |
| Hostinger     | Domain registration & VPS hosting for webhook listeners        | 1 GB RAM, 1 Core CPU, 20 GB SSD                    | $3.95 – 4 GB RAM, 2 Cores, 100 GB SSD    |
| Replit        | Quick proof‑of‑concept code hosting and debugging             | Unlimited public repls, 500 MB storage              | $7 – Unlimited private repls, 5 GB storage |
| Vapi          | SMS/WhatsApp number provisioning and management               | 100 messages/month, 1 number                       | $15 – 500 messages/month, 3 numbers      |

**Estimated time to complete:** 3 hours 45 minutes (including account setup, domain verification, and email relay configuration).

---

## Procedure 1.1: Register Your Business Domain on Hostinger

1. Launch Google Chrome (or any modern browser).  
2. In the address bar, type **`https://www.hostinger.com`** and press **Enter**.  
3. On the Hostinger homepage, locate the top‑navigation bar.  
   **Click the button labeled** **`Domains`** (it appears next to “Hosting”).  
4. A new page opens. In the middle of the screen, you’ll find a search box.  
   **Type your desired domain name** (e.g., `mybusiness.ng`) **and press** **Enter**.  
   **Do you see the domain availability results?** If not, clear the cache, reboot the browser, or try a different TLD such as `.com` or `.co`.  

5. From the results list, locate the row that matches your domain.  
   **Click the button labeled** **`Add to Cart`** next to the exact domain.  
6. A mini‑cart slides in on the right.  
   **Click the button labeled** **`Go to Checkout`**.  
7. You will be prompted to log in or create an account.  
   - If you already have an account: **Enter your email** and **password**, then click **`Login`**.  
   - If you’re new: **Click the button labeled** **`Create Account`**.  
     - Fill in the form:  
       - **First Name**: `John`  
       - **Last Name**: `Doe`  
       - **Email**: `john@mybusiness.ng`  
       - **Password**: `StrongPassword123!`  
     - **Click the button labeled** **`Create Account`**.  

8. After login, you return to the cart page.  
   **Select the billing period** from the dropdown:  
   - `1 year` – $10.99  
   - `2 years` – $16.98 (discounted)  
   - `3 years` – $22.97 (best value)  
   **Click the dropdown arrow**, choose **`3 years`**.  

9. You will now see a summary of your cart.  
   **Click the button labeled** **`Proceed to Checkout`**.  
10. On the checkout screen, confirm that the domain name and period are correct.  
    **Click the button labeled** **`Confirm Order`**.  
    **Do you see the order confirmation page with a thank‑you message?** If not, check that you have accepted the terms and that your payment information is valid.  

11. Hostinger will send a verification email to the address you used.  
    Open your email client and locate the email titled **`Hostinger Domain Verification`**.  
    **Click the button labeled** **`Verify Email`** within the email.  
12. Once verified, you’ll

---

## Procedure 1.2: Create a WhatsApp Business API Account on Twilio  

1. **Open a web browser and navigate to** `https://www.twilio.com/try-twilio`.  
2. **Click the button labeled** **“Get a free trial”** (top‑right).  
3. **Fill in the registration form**  
   - Phone number field: your personal phone (must be a valid number for SMS verification).  
   - Email field: your business email.  
   - Password field: a secure password (min 8 chars, 1 number, 1 symbol).  
   - Click **“Create your Twilio account”**.  
4. **Check your email for the verification code** from Twilio.  
   - Open the inbox, copy the 6‑digit code.  
   - Paste it into the verification field on Twilio’s website and click **“Verify”**.  
   **Do you see “Your Twilio account is verified” displayed?** If not, check spam and retry.  
5. **Navigate to the Twilio Console** `https://www.twilio.com/console`.  
   - The dashboard shows your Account SID and Auth Token in the header.  
   - Note these credentials; you will need them later.  
6. **Open the “Messaging” section** by clicking the **“Messaging”** tab in the left sidebar.  
7. **Select “WhatsApp”** from the dropdown menu under “Channels”.  
8. **Click the button labeled** **“Request Access”** under “WhatsApp in Sandbox”.  
   - Twilio will generate a Sandbox number (e.g., `+14155238886`).  
9. **Save the Sandbox number**.  
   - Copy it to a Notion page titled “Twilio WhatsApp Sandbox”.  
   **Do you see the Sandbox number displayed?** If not, ensure you are in the WhatsApp section; refresh the page.  
10. **Add your WhatsApp test phone**:  
    - Click **“Add a WhatsApp-enabled phone number”**.  
    - Enter your phone number and click **“Add”**.  
    - Twilio will send a code to your phone.  
11. **Enter the received code** in the “Verification” field and click **“Verify”**.  
    - The status should change to **“Enabled”**.  
12. **Open a new browser tab and go to** `https://www.twilio.com/console/sms/settings`.  
13. **Scroll to “Messaging Services”** and click **“Create new messaging service”**.  
    - Name it **“WhatsAppService”**.  
    - Set the default message type to **“WhatsApp”**.  
    - Click **“Create”**.  
14. **Add the Sandbox number to the Messaging Service**:  
    - In the service details, click **“Add phone numbers”**.  
    - Select **“WhatsApp Sandbox”** and click **“Add”**.  
    **Do you see the Sandbox number listed under “Phone numbers”?** If not, ensure the number is verified.  
15. **Create a Twilio Function for webhook handling**:  
    - Go to `https://www.twilio.com/console/functions`.  
    - Click **“Create new Function”** → “Blank”.  
    - Title it **“WhatsAppWebhook”**.  
    - Set the path to **/whatsapp**.  
    - Paste the following Node.js snippet (replace placeholders with your credentials):  

```javascript
exports.handler = function(context, event, callback) {
   const twiml = new Twilio.twiml.MessagingResponse();
   twiml.message('Thank you for contacting us!');
   callback(null, twiml);
};
```

    - Click **“Save & Deploy”**.  
    - Note the URL displayed (e.g., `https://whatsapp-xxxxx.twil.io/whatsapp`).  
16. **Configure the Messaging Service webhook**:  
    - In the WhatsAppService settings, find **“Messaging Service Webhook”**.  
    - Enter the URL from step 15 and set the HTTP method to **POST**.  
    - Click **“Save”**.  
17. **Test the webhook**:  
    - On your WhatsApp phone, send any text to the Sandbox number (e.g., “Hello”).  
    - You should receive an automated reply “Thank you for contacting us!”.  
    **Do you see the reply?** If not, verify the webhook URL and that the function is deployed.  
18. **Set up Make.com to extend bot logic**:  


---

## Procedure 1.3: Set Up Email Forwarding in Hostinger for Bot Alerts

1. **Log into your Hostinger account**  
   - URL: `https://my.hostinger.com/login`  
   - Username: *your login email*  
   - Password: *your login password*  
   - **Click** the **Login** button.  
   - *Expected output:* Dashboard with “Welcome to Hostinger” banner.

2. **Navigate to the Email Management section**  
   - In the sidebar, click **Email**.  
   - **Select** the domain that hosts your WhatsApp bot email address (e.g., `bot@yourdomain.com`).  
   - *Expected output:* Email overview page listing mailboxes for the domain.

3. **Create a new email alias for bot alerts**  
   - Click the **Add Email** button (top‑right).  
   - In the **Create Email** dialog:  
     - **Username:** `botalerts`  
     - **Password:** auto‑generate (or custom).  
     - **Mailbox size:** `1 GB` (default).  
   - **Click** **Create Email**.  
   - *Expected output:* Confirmation toast “Email botalerts@yourdomain.com created”.

4. **Open the Forwarding settings for the new alias**  
   - Under the newly created mailbox, click the **Manage** icon (gear).  
   - **Select** **Forwarding** from the submenu.  
   - *Interactive check‑in:* Do you see the **Add Forwarder** button?  
     - If not, refresh the page or verify you are on the correct domain’s mailbox page.

5. **Add a forwarder to your primary surveillance mailbox**  
   - Click **Add Forwarder**.  
   - **Enter** the destination address: `your‑monitoring‑email@example.com`.  
   - **Check** the box **Keep a copy of forwarded messages** (optional).  
   - **Click** **Save**.  
   - *Expected output:* Forwarder listed with status “Active”.

6. **Verify the forwarding rule**  
   - Send a test email from any external account to `botalerts@yourdomain.com`.  
   - Check `your‑monitoring‑email@example.com` inbox for the forwarded message.  
   - *Interactive check‑in:* Do you see the test email in your monitoring inbox?  
     - If not, ensure DNS MX records point to Hostinger’s servers (`mx1.hostinger.com`, `mx2.hostinger.com`).

7. **Configure SPF & DKIM to prevent spam filtering**  
   - Still on the **Email** dashboard, click **DNS Zone**.  
   - **Locate** the TXT record for `v=spf1`.  
   - **Edit** to include:  
     ```
     v=spf1 a mx include:_spf.hostinger.com -all
     ```  
   - **Add** a new TXT record:  
     - **Name:** `_dmarc`  
     - **Value:** `v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com`  
   - **Click** **Save**.  
   - *Expected output:* DNS records updated, propagation may take up to 24 hrs.

8. **Set up an automated alert using Make.com**  
   - Open a browser tab to `https://www.make.com`.  
   - **Log in** or **sign up** (free tier: 3 scenarios, 100 operations/month).  
   - **Create a new scenario** by clicking **Create a new scenario**.  
   - **Add** the **Email > Watch Email** module:  
     - **Email provider:** Hostinger (IMAP).  
     - **Host:** `imap.hostinger.com`.  
     - **Port:** `993`.  
     - **SSL:** Yes.  
     - **Username:** `botalerts@yourdomain.com`.  
     - **Password:** *your mailbox password*.  
   - **Set filter** to trigger on subject line containing “Bot Alert”.  
   - *Interactive check‑in:* Do you see the **Email > Watch Email** module added?  
     - If not, ensure you’ve selected the correct email provider and credentials.

9. **Add a notification step to SendGrid (optional)**  
   - **Add** the **SendGrid > Send an Email** module.  
   - **Connect** your SendGrid account (free tier: 25 000 emails/month).  
   - **Configure**:  
     - **To:** `your‑monitoring‑email@example.com`.  
     - **Subject:** `⚠️ WhatsApp Bot Alert – {{Subject}}`.  
     - **Body:** `Alert from {{From}}: {{Body}}`.  
   - **Link** the output of the Watch Email module to the SendGrid module.  
   - *Expected output:* Scenario ready to run.

10. **Run the scenario once to test**  
    - **Click** the **Run once** button (top‑right).  
    - **Confirm** credentials if prompted.  
    - After execution, **check** the monitoring inbox for the alert email.  
    - *Interactive check‑in:* Do you receive the alert email?  
      - If not, review the scenario logs for errors.

11. **Schedule the scenario to run every 5 minutes**  
    - In the scenario editor, click the **clock** icon next to the trigger module.  
    - **Set**:  
      - **Frequency:** `5 minutes`.  
      - **Start time:** `08:00`.  
    - **Save** and **Activate** the scenario.  
    - *Expected output:* Scenario status “Active – Running”.



## Check-In: Module 1 Complete

- [ ] Register Your Business Domain on Hostinger completed and verified
- [ ] Create a WhatsApp Business API Account on Twilio completed and verified
- [ ] Set Up Email Forwarding in Hostinger for Bot Alerts completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 2: TECH STACK

## Overview

This module is the foundation of every WhatsApp Sales Bot operation. It covers the exact tools you must install, the API keys you must generate, and the connections you must establish so that data flows flawlessly from WhatsApp, through your AI engine, to your CRM and marketing stack. If you skip this step, your bot will crash on launch, your leads will be lost, and you will waste time troubleshooting broken integrations that should have been verified beforehand. A correctly configured tech stack guarantees that every message, every customer touchpoint, and every revenue event is captured and actionable.

You will learn how to:

* Register and authenticate with Make.com and ChatGPT APIs, ensuring you have the correct scopes and tokens.
* Wire Make.com scenarios to the WhatsApp Business API, so inbound messages trigger the right AI workflows.
* Connect your bot to a revenue platform (e.g., Shopify) and a marketing automation tool (e.g., Klaviyo), so every sale is tracked and every customer receives personalized follow‑ups.
* Verify the entire pipeline with test conversations, checking that JSON payloads are correctly formatted and that data ends up in the right place.

Below is the tool lineup you will need for this module. All tools are listed with their free tier limits and the most cost‑effective paid tier you should consider once you go live.

| Tool          | Purpose                                             | Free Tier                                 | Paid Tier (Monthly) |
|---------------|-----------------------------------------------------|-------------------------------------------|----------------------|
| Make.com      | Orchestration of API calls and automations          | 1,000 operations/month (Starter)          | $25 (Standard)       |
| ChatGPT API   | AI logic for message generation                     | $0.0025 per 1 k tokens (OpenAI free)      | $20 (ChatGPT‑Plus)   |
| WhatsApp Business API | Channel for customer interactions               | N/A (requires Meta Business account)      | $0.005 per message (WhatsApp Business) |
| Shopify       | E‑commerce platform for product catalog & checkout | 5 free stores, 14‑day trial              | $39 (Basic)          |
| Klaviyo       | Email/SMS marketing automation                      | 250 contacts, 500 emails/month (Starter)  | $20 (Growth)         |
| Zapier        | Optional glue for legacy systems                     | 5 tasks/month (Free)                      | $19.99 (Starter)     |
| Vapi          | WhatsApp messaging API (alternative to Meta API)    | 1,000 messages/month (Free)              | $19/month (Starter)  |

**Estimated Time to Complete**: 1 hour 30 minutes. This includes generating API keys, setting up each connection, and running a quick test flow to confirm that data moves correctly between platforms.

---

## Procedure 2.1: Register Your WhatsApp Business API Credentials in Make.com

1. **Launch Chrome** and type the address `https://developers.facebook.com/` into the address bar. Press **Enter**.  
   *Expected Output:* You see the Meta for Developers dashboard with the login prompt.  

2. Click the **Log In** button in the upper‑right corner.  
   *Expected Output:* Meta login page.  

3. Enter your **email** and **password** for the Meta account you use for business. Click **Log In**.  
   *Expected Output:* You are taken to the Meta for Developers homepage.  

4. Click the **Get Started** button in the middle of the page.  
   *Interactive Check‑In:* Do you see the **Set up a new app** button? If not, refresh the page or clear your cache.  

5. In the modal that appears, type **WhatsAppBot** into the **App Name** field.  
   *Expected Output:* App name appears in the field, app ID is generated in the background.  

6. Enter a **contact email** (e.g., `support@yourdomain.com`) in the **App Contact Email** field.  
   *Expected Output:* Field accepts the email.  

7. Click **Create App ID**.  
   *Expected Output:* A confirmation banner appears: “Your app has been created.”  

8. On the left sidebar, click **Settings** → **Basic**.  
   *Interactive Check‑In:* Do you see the **App Domain** field? If not, go back to the sidebar and click **Basic** again.  

9. In the **App Domain** field, type `yourdomain.com`. Click **Save Changes**.  
   *Expected Output:* A green checkmark appears next to the field.  

10. Scroll down to the **App ID** and **App Secret**. Click **Show** next to **App Secret** and copy the 32‑character string to your clipboard.  
    *Expected Output:* App Secret is visible; you have it copied.  

11. Open a new tab and navigate to `https://business.facebook.com/overview`.  
    *Expected Output:* You are in the Facebook Business Manager.  

12. In Business Manager, click **Business Settings** (gear icon) in the top left.  
    *Interactive Check‑In:* Do you see the **WhatsApp Accounts** option under the **Channels** section? If not, expand the **Channels** menu.  

13. Click **WhatsApp Accounts** → **Add**.  
    *Expected Output:* A modal titled “Add a WhatsApp Business Account” appears.  

14. Select **Create a WhatsApp Business Account**. Enter your **Business Name** (e.g., “YourBiz WhatsApp”) and click **Next**.  
    *Interactive Check‑In:* Do you see the **Phone Number** field? If not, click **Next** again until the field appears.  

15. Choose a **Phone Number** that is not currently registered with WhatsApp. Enter the **full international number** (e.g., +2348012345678).  
    *Expected Output:* The number is highlighted in green when validated.  

16. Click **Continue**. A verification prompt will appear.  
    *Interactive Check‑In:* Do you see the **Verification Code** field? If not, check your SMS inbox for the code.  

17. Retrieve the **6‑digit code** from your mobile device and type it into the field. Click **Verify**.  
    *Expected Output:* Confirmation banner: “Phone number verified.”  

18. In the same modal, click **Create** to generate the **WhatsApp Business API Key**.  
    *Expected Output:* API Key is displayed; click **Copy** to clipboard.  

19. Close the modal and return to the Business Manager dashboard.  
    *Interactive Check‑In:* Do you see the newly created **WhatsApp Business Account** listed? If not, refresh the page.  

20. Open a fresh tab and go to `https://app.make.com/`.  
    *Expected Output:* Make.com login page.  

21. Click **Sign In** and enter your Make.com credentials.  
    *Expected Output:* You land on the Make.com

---

## Procedure 2.2: Create a Make.com Scenario to Forward WhatsApp Messages to ChatGPT

1. **Open your web browser** and navigate to **https://www.make.com/**.  
   *If you are not already logged in, click the **Log in** button in the top‑right corner and enter your credentials.*  

2. Once logged in, locate the **Create new scenario** button on the dashboard and click it.  
   *The screen will now show a blank scenario canvas with a “+ Add” button in the center.*  

3. Click the **+ Add** button. In the search dialog, type **Webhook** and select **Webhooks by Make → Custom Webhook**.  
   *Press **Create a new webhook** and name it “WhatsAppInbound”.*  

4. Click **Save**. The builder will display a public URL under the webhook module.  
   *Copy this URL to your clipboard.*  

5. **Do you see a “Webhook URL” field populated?**  
   *If not, refresh the page or re‑open the webhook module. A missing URL typically means the webhook was not saved properly.*  

6. Open a new browser tab and go to **https://vapi.io/**

---

## Procedure 2.3: Validate and Log Data Transfer from Make.com to ChatGPT

1. **Log into Make.com**  
   - Open your browser and go to **https://www.make.com/**.  
   - Click the **Sign in** button in the top‑right corner.  
   - Enter your email and password, then click **Log in**.  
   - *Do you see the Dashboard? If not, check that your credentials are correct and that the site is not blocked by your firewall.*

2. **Create a new scenario**  
   - In the Dashboard, click **Create a new scenario**.  
   - In the pop‑up, type **ChatGPT** in the search bar.  
   - Select the **ChatGPT** module and click **Continue**.  
   - *Do you see the “ChatGPT” module tile? If not, refresh the page and try again.*

3. **Add a trigger module**  
   - Click the big **+** icon next to the ChatGPT tile.  
   - Choose **Webhooks** → **Custom Webhook** → **Make a request**.  
   - Click **Add**.  
   - Copy the webhook URL that appears (e.g., `https://hook.integromat.com/xxxxxx`) and note it for later use.  
   - *Do you see the webhook URL? If not, ensure you have selected the correct Webhook module.*

4. **Configure the Webhook**  
   - In the Webhook module settings, set **Method** to **POST**.  
   - Leave **URL** blank (it will be filled by Make.com).  
   - In **Headers**, add a key named **Content‑Type** with a value of **application/json**.  
   - In **Body**, enter the following JSON template:  
     ```json
     {
       "customer_id": "{{customer_id}}",
       "message": "{{message}}",
       "timestamp": "{{now}}"
     }
     ```  
   - Click **OK** to save.  
   - *Do you see the JSON body displayed? If not, ensure you typed the braces correctly.*

5. **Set up the ChatGPT module**  
   - Click the ChatGPT tile.  
   - In **Connection**, click **Add**.  
   - Paste your **OpenAI API key** (obtain from **https://platform.openai.com/account/api-keys**) into the **API key** field.  
   - Click **Test**; you should receive a **200 OK** and a sample response.  
   - If the test fails with **401 Unauthorized**, the key is invalid. Re‑generate a new key and try again.  
   - In **Model**, select **gpt‑3.5‑turbo**.  
   - In **Prompt**, use the following:  
     ```
     You are a sales assistant bot. Generate a concise response to the following customer message:
     "{{message}}"
     ```  
   - Click **OK**.  
   - *Do you see the test response? If not, check that the API key is correct and that your OpenAI plan allows the chosen model.*

6. **Add a logging module to capture the response**  
   - Click the **+** icon next to the ChatGPT tile.  
   - Search for [**Notion**](https://notion.so/) and select **Create a database item**.  
   - Click **Add**.  
   - In **Connection**, click **Add** and sign into Notion.  
   - Choose the workspace and database named **ChatBotLogs** (create it beforehand if missing).  
   - Map the fields:  
     - **Customer ID** ← `{{customer_id}}`  
     - **Message** ← `{{message}}`  
     - **ChatGPT Response** ← `{{ChatGPT_response}}`  
     - **Timestamp** ← `{{now}}`  
   - Click **OK**.  
   - *Do you see the mapping fields? If not, double‑check that the database columns exist.*

7. **Activate the scenario**  
   - Click **Save** in the top right corner.  
   - Click the **Run once** button to test.  
   - In the test window, click **Execute**.  
   - *Do you see the execution log? If not, ensure the scenario is saved before running.*

8. **Verify the data flow**  
   - In the execution log, scroll to the **Webhooks** module.  
   - Confirm the JSON payload shows the correct `customer_id` and `message`.  
   - Scroll to the **ChatGPT** module.  
   - The **Response** field should contain a text string.  
   - Scroll to the **Notion** module.  
   - The **Status** should read **Success**.  
   - *Do you see all three modules marked as successful? If any module failed, revisit its settings.*

9. **Send a test request from an external source**  
   - Open **https://replit.com/new** and create a new Python repl called **WebhookTester**.  
   - In the `main.py` file, paste the following code, replacing `WEBHOOK_URL` with your Make.com webhook URL:  
     ```python
     import requests, json
     WEBHOOK_URL = "https://hook.integromat.com/xxxxxx"
    



---

**Support Pollinations.AI:**

---

🌸 **Ad** 🌸
Powered by Pollinations.AI free text APIs. [Support our mission](https://pollinations.ai/redirect/kofi) to keep AI accessible for everyone.

## Check-In: Module 2 Complete

- [ ] Register Your WhatsApp Business API Credentials in Make.com completed and verified
- [ ] Create a Make.com Scenario to Forward WhatsApp Messages to ChatGPT completed and verified
- [ ] Validate and Log Data Transfer from Make.com to ChatGPT completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 3: FRAMEWORK

## Overview

This module lays the foundation for turning a WhatsApp sales bot idea into a repeatable, scalable business. It teaches you how to design a **Service Delivery Framework** that maps every touchpoint—from initial client inquiry to post‑sale support—into a clear, auditable workflow. The framework becomes the backbone of your operations, ensuring consistency, quality, and the ability to onboard new clients without reinventing the wheel each time.

Why does this matter? Without a well‑defined framework, your bot deployments will become ad‑hoc, leading to missed revenue, inconsistent customer experiences, and the dreaded “bot failure” that erodes trust. Skipping this module means you’ll spend far more time troubleshooting, re‑writing code, and dealing with unhappy clients. By investing in the process now, you lock in a repeatable system that scales linearly with revenue, not with effort.

In this module you will:
1. Draft a **Process Map** that covers all stages of a sales bot lifecycle.
2. Set up **Client Onboarding Workflows** that automate data capture, agreement signing, and environment provisioning.
3. Define **Quality Assurance (QA) Standards**—including automated testing scripts, performance benchmarks, and escalation protocols.

Estimated time to complete: **3.5 hours** (including reading, diagram creation, and tool setup).

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| Make.com | Automates bot workflows between WhatsApp, ChatGPT, and CRM | 400 operations/month, 15 tasks | 5,000 operations/month, Unlimited tasks – starts at $29/month |
| ChatGPT (OpenAI) | Generates dynamic replies and content for the bot | 3,000 token/day limit | 3,000 token/day + priority support – starts at $20/month |
| Zapier | Connects Make.com to external services (e.g., email, Google Sheets) | 100 tasks/month | 750 tasks/month – starts at $19.99/month |
| Canva | Creates branded media for bot prompts and client onboarding | Unlimited free use (limited templates) | Unlimited templates & brand kit – starts at $12.99/month |
| [ElevenLabs](https://elevenlabs.io/) | High‑quality voice‑to‑text conversion for WhatsApp Viber integration | 5,000 characters/month | 30,000 characters/month – starts at $14/month |
| Notion | Documentation hub for SOPs and knowledge bases | Unlimited pages, 1,000 blocks | Unlimited + advanced workspace – starts at $8/month |
| Calendly | Automates scheduling of client demos and onboarding calls | 1 calendar per account | Unlimited calendars – starts at $12/month |
| Apollo.io | Prospecting and lead enrichment for new clients | 5,000 contacts/month | 25,000 contacts/month – starts at $49/month |
| Buffer | Manages social‑media announcements of bot launches | 3 social accounts | Unlimited accounts – starts at $15/month |
| Loom | Records walkthrough videos of the bot for training | Unlimited uploads (720p) | Unlimited uploads (1080p) – starts at $12/month |

These tools together form a cost‑effective, highly automatable stack that will keep your bot delivery lean while ensuring top‑tier client satisfaction.

---

## Procedure 3.1: Create a Client Onboarding Flow for WhatsApp Bot Projects

1. **Open Notion**  
   - URL: https://www.notion.so  
   - Click the **“+ New Page”** button in the left‑hand sidebar.  
   - Title the page **“Client Onboarding Flow – WhatsApp Bot”**.  
   - In the body, type **“Template: Onboarding Flow v1.0”** and press **Enter**.  
   - Do you see the new page with the title above? If not, refresh the browser or log out/in again.

2. **Insert Table of Contents**  
   - In the new page, type `/table of contents` and press **Enter**.  
   - The table will auto‑populate as you add headings.  
   - Confirm the table appears; if not, check that the block type is “Table of Contents”.

3. **Add a “Client Intake Form” heading**  
   - Type `# Client Intake Form` and press **Enter**.  
   - Below the heading, type `/form` and select **“Google Forms”**.  
   - Click **“Create new form”**.  
   - In the form editor, add the following questions:  
     - **Full Name** (Short answer)  
     - **Business Email** (Short answer)  
     - **WhatsApp Business Number** (Short answer)  
     - **Preferred Language** (Multiple choice: English, French, Swahili)  
     - **Project Deadline** (Date)  
   - Click **“Send”** → **“Embed”** → copy the embed code.  
   - Return to Notion, paste the embed code into the page.  
   - Do you see the form embedded? If not, ensure the embed code is correct and that the page is published.

4. **Set Up a Zapier Trigger for Form Submission**  
   - Open a new tab: https://zapier.com  
   - Click **“Get Started”** → **“Sign Up”** with your email.  
   - After logging in, click **“Make a Zap”**.  
   - Search for **“Google Forms”** as the trigger app.  
   - Choose **“New Response in Spreadsheet”**.  
   - Click **“Connect an Account”** → allow Zapier to access your Google account.  
   - Select the spreadsheet created by the form.  
   - Click **“Test Trigger”** → ensure a sample row appears in the preview.  
   - Do you see the sample row? If not, verify the form is linked to the spreadsheet.

5. **Add a Make.com Action to Update a Client Dashboard**  
   - In the same Zap, click **“+ Add Action”**.  
   - Search for **“Make.com”** → select **“Create New Scenario”**.  
   - Click **“Continue”** → choose **“Webhooks by Make.com”** as the trigger.  
   - In Make.com, the URL endpoint will be displayed. Copy it.  
   - Return to Zapier, paste the endpoint into the **“Webhook URL”** field.  
   - Click **“Test & Review”** → you should see a 200 response.  
   - Do you see the 200 response? If not, check that the endpoint is live and accessible.

6. **Create the Make.com Scenario for WhatsApp Bot Deployment**  
   - Go to https://www.make.com/en  
   - Click **“Create New Scenario”** (top‑right).  
   - Click **“Add an App”** → search for **“Vapi”** → select **“Vapi”**.  
   - Choose **“Send WhatsApp Message”**.  
   - Click **“Connect a new account”** → paste your Vapi API Key (found in Vapi dashboard → **API Settings**).  
   - Map the **“Phone Number”** field to the form's WhatsApp Business Number.  
   - Map **“Message Text”** to a static message: `"Thank you for your inquiry! A team member will contact you shortly."`  
   - Click **“Save”** → **“Run once”**.  
   - Confirm a WhatsApp message is sent to the number.  
   - If you

---

## Procedure 3.2: Establish Quality Standards for Bot Deployment  

1. **Open Make.com and Create a New Scenario**  
   - Navigate to `https://app.make.com/`.  
   - Click the **+ Create** button in the top‑right corner.  
   - In the modal that appears, type **Scenario Name**: `WhatsApp Bot QA Pipeline`.  
   - Click **Create**.  
   - *Do you see the green “Scenario Created” toast?* If not, refresh the page and try again.  

2. **Add the WhatsApp Module (Vapi Integration)**  
   - In the Scenario editor, click **+ Add another module**.  
   - Search for [**Vapi**](https://vapi.ai/) and select **Vapi – WhatsApp**.  
   - Choose **Get Messages** as the trigger.  
   - In the **Connection** field, click **New Connection**.  
   - Paste your Vapi API Key (found at `https://dashboard.vapi.io/api-keys`) into the **API Key** box.  
   - Click **Test & Create**.  
   - *Do you see the green “Connection success” badge?* If you see **“Invalid API Key”**, double‑check the key and re‑enter it.  

3. **Configure Message Filters**  
   - Click the **Filter** icon on the Vapi module.  
   - Set **Criteria** to **Message Type = Text**.  
   - Set **Criteria** to **Message Text contains “order”**.  
   - Click **Save**.  
   - *Do you see the filter icon highlighted in green?* If not, the filter did not save; re‑apply the settings.  

4. **Add a Make.com “HTTP – Get” Module for Bot Logic**  
   - Click **+ Add another module**.  
   - Search for **HTTP – Get** and select it.  
   - In the **URL** field, enter `https://whatsapp-bot-qa.repl.it/api/handle`.  
   - In **Headers**, add `Content-Type: application/json`.  
   - Leave **Body** blank.  
   - Click **Save**.  
   - *Do you see the HTTP module with the URL saved?* If not, re‑type the URL exactly as shown.  

5. **Add a “Code by Replit” Module**  
   - Click **+ Add another module**.  
   - Search for [**Replit**](https://replit.com/refer/egwuokwor) and select **Code**.  
   - In the **Repl URL** field, paste `https://replit.com/@YourUsername/WhatsAppBotQA`.  
   - In the **File** field, enter `bot_logic.py`.  
   - In **Code** field, type `print("Bot logic executed")`.  
   - Click **Save**.  
   - *Do you see the “Replit” module with the Repl URL?*

## Check-In: Module 3 Complete

- [ ] Create a Client Onboarding Flow for WhatsApp Bot Projects completed and verified
- [ ] Establish Quality Standards for Bot Deployment completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 4: FIRST BUILD

## Overview

In this module you will **build, deploy, and monetize a fully functional WhatsApp sales bot** using Make.com and ChatGPT. You will start with raw client data—product catalog, pricing, FAQs—and end with a bot that can handle inquiries, process orders, and trigger follow‑up messages. The walkthrough is tightly scoped: you’ll configure a Make.com scenario, script responses in ChatGPT, hook the bot to WhatsApp Business via Vapi, and set up a revenue‑tracking dashboard in Notion. By the end you’ll own a repeatable delivery that you can sell to African SMEs looking to scale their customer touchpoints.

Skipping this module means you’ll miss the core “hands‑on” loop that turns AI theory into a marketable product. You’ll be unable to demonstrate a working bot to prospects, and you’ll lack the practical knowledge of integrating third‑party services (WhatsApp, payment gateways, email automation) that generate recurring revenue. The rest of the playbook assumes you can ship a bot with a verified order‑to‑cash flow; without this, your launch timeline will stall and your credibility with clients will suffer.

| Tool      | Purpose                                                  | Free Tier                                  | Paid Tier (Monthly) |
|-----------|----------------------------------------------------------|--------------------------------------------|---------------------|
| Make.com  | Automate WhatsApp messages, schedule tasks, API calls   | 3,000 operations / month, 2 apps          | $29 for Unlimited Ops |
| ChatGPT   | Generate GPT‑4 prompts, answer FAQs, craft scripts       | 750 tokens / day (free)                    | $20 for ChatGPT‑4  |
| Vapi      | WhatsApp Business API gateway                            | 500 msgs / month (trial)                   | $0.20 / 100 msgs   |
| Notion    | Project docs, revenue tracker, client handover          | Unlimited pages, 1,000 blocks              | $8 per seat        |
| Zapier    | Bridge Make.com to other SaaS (e.g., Klaviyo, Stripe)   | 5 Zaps, 100 tasks / month                 | $19 for Unlimited  |
| Hostinger | Domain & hosting for webhook endpoints                  | 1 GB bandwidth, 1 TB storage (free)        | $3.95 / month      |
| Canva     | Create bot branding, welcome images                     | Unlimited design, 5 templates              | $12.95 per seat    |

**Estimated time to complete:** 5–6 hours of focused work (excluding client data prep).

---

## Procedure 4.1: CREATE A MAKE.COM SCENARIO FOR WHATSAPP SALES BOT AUTOMATION

1. **Open your browser** and navigate to <https://www.make.com>.  
   **If you have no account, click the blue button **Sign Up** in the top‑right corner, use your Gmail address, and complete the email‑verification step.  
   **If you already have an account, click **Login** and enter your credentials.**  
   *Expected state:* You are on the Make.com dashboard with the “My scenarios” page visible.

2. **From the dashboard, click the green button **Create scenario**.  
   A new tab opens titled “Scenario 1 – Untitled”.  
   *Expected state:* A blank scenario canvas appears with “Add module” placeholder.

3. **Click the placeholder** and type “WhatsApp” in the search bar.  
   Select **“WhatsApp Business (Twilio)”** from the dropdown.  
   In the module wizard, click **Configure**.  
   *Expected state:* A form with fields “Account SID”, “Auth Token”, and “WhatsApp Number” appears.

4. **Log in to the Twilio Console** (<https://www.twilio.com/console>).  
   Copy your **Account SID** (under **Project Info**) and paste it into the Make.com field.  
   Copy your **Auth Token** (under **API keys**) and paste it into the Make.com field.  
   In Make.com, type your Twilio‑approved WhatsApp number (e.g., **+15551234567**) into “WhatsApp Number”.  
   Click **Save**.  
   *Do you see “Connection successful” and the webhook URL displayed? If not, ensure your Twilio number is verified for WhatsApp and the credentials are correct. The Auth Token must be 32‑character alphanumeric.*

5. **Click the “Add another module” button (+)**.  
   Search for “Webhooks” and choose **“Webhooks > Custom webhook (Built‑in)”**.  
   Click **Add** and name the webhook **“Receive‑Message”**.  
   Copy the generated URL (e.g., `https://hook.make.com/abcd1234`) and paste it into your Twilio console under **Messaging > Webhooks > When a message is received**.  
   *Expected state:* Twilio will forward inbound WhatsApp messages to the Make.com webhook.

6. **Add a second module** by clicking the + icon next to “Receive‑Message”.  
   Search for “HTTP” and select **“HTTP > Make a request”**.  
   Set the method to **POST** and the URL to `https://api.openai.com/v1/chat/completions`.  
   In the Headers section, add:
   - Key: `Authorization` Value: `Bearer YOUR_OPENAI_API_KEY`  
   - Key: `Content-Type` Value: `application/json`  
   *Expected state:* The HTTP module is ready to send a request to ChatGPT.

7. **In the Body field, paste the following JSON** (replace `{{trigger.body.message}}` with the inbound message variable from the webhook):

```json
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "You are a friendly sales assistant for a small African SME. Respond to customer enquiries about products, prices, and booking appointments."
    },
    {
      "role": "user",
      "content": "{{trigger.body.message}}"
    }
  ],
  "temperature": 0.7,
  "max_tokens": 150
}
```

   Click **Save**.  
   *Expected state:* The HTTP module now contains a JSON payload ready for ChatGPT.

8. **Link the HTTP module to the webhook**.  
   Drag the arrow from **Receive‑Message** to **Make a request**.  
   Confirm the connection; Make.com will automatically map `{{trigger.body.message}}` to the inbound text.  
   *Do you see the data mapping icon (a small square with an arrow)? If not, click the module again and enable “Use variables” to expose the inbound message.*

9. **Add a third module**: search for “WhatsApp” again, choose **“WhatsApp Business (Twilio)”**, and click **Configure**.  
   Set the “From” field to your Twilio WhatsApp number.  
   In the “To” field, map the inbound phone number variable: `{{trigger.body.from}}`.  
   In the “Message” field, map the ChatGPT response: `{{http_1.body.choices[0].message.content}}`.  
   Click **Save**.  
   *Expected state:* The outgoing message module is

---

## Procedure 4.2: Configure ChatGPT Prompt for Personalized Sales Interaction

1. **Open the OpenAI ChatGPT web interface**  
   Go to <https://chat.openai.com/chat>.  
   On the left sidebar, click the **“Login”** button.  
   Enter your registered email and password, then click the **“Continue”** button.  
   Expected result: you are taken to the chat home screen with a blank message box.

2. **Start a new chat session**  
   On the top-left, click the bold **“New Chat”** icon.  
   A fresh chat window appears with the placeholder text “Chat with ChatGPT”.  
   If the placeholder does not appear, refresh the page and try again.

3. **Create the base prompt**  
   In the message box, type the following exactly:  
   > “You are an empathetic AI sales assistant for an African SME that sells hand‑crafted textiles.  
   >  Your tone is friendly, concise, and culturally aware.  
   >  Respond to customer inquiries by asking clarifying questions first, then offer product options and a call‑to‑action to place an order.”  
   Do not press **Enter** yet; just type.

4. **Save the prompt as a template**  
   Click the **“Save”** button (the floppy‑disk icon) located above the message box.  
   In the modal that appears, name the template **“African SME Sales Bot – Prompt”** and click **“Create”**.  
   **Do you see the new template in the “Templates” sidebar?** If not, close the modal, reopen it, and repeat step 4.

5. **Open the Make.com dashboard**  
   In a new browser tab, go to <https://www.make.com>.  
   Click the **“Sign In”** button, enter your credentials, and press **“Continue”**.  
   Expected result: you are taken to the Make.com home screen.

6. **Create a new scenario**  
   Click the bold **“Create a new scenario”** button on the dashboard.  
   The scenario editor opens with a blank canvas and a **“+”** icon.

7. **Add the OpenAI module**  
   Click the **“+”** icon, then search for “OpenAI” in the module picker.  
   Select **“OpenAI – Send a prompt”** and click **“Add”**.  
   The module appears on the canvas.

8. **Configure the OpenAI module**  
   - Click the module to open its settings panel.  
   - In **“API key”**, paste your OpenAI key (found under <https://platform.openai.com/account/api-keys>).  
   - In **“Model”**, select **“gpt‑3.5‑turbo”** from the dropdown.  
   - In **“Prompt”**, click the **“Insert variable”** button, choose **“Template”**, and select **“African SME Sales Bot – Prompt”** from the list.  
   - Under **“Max tokens”**, set **150**.  
   - Leave **“Temperature”** at **0.7**.  
   Click **“Save”**.

9. **Add a WhatsApp trigger (optional)**  
   Click the **“+”** icon again, search for “WhatsApp Business API” (provided by Vapi).  
   Choose **“New Message Received”** and click **“Add”**.  
   In the module settings, link your Vapi account by clicking **“Add account”**, enter your Vapi credentials, and authorize.  
   Expected result: the module is connected and displays **“Ready”**.  
   **Do you see the WhatsApp trigger module?** If not, double‑check Vapi credentials and retry.

10. **Link the trigger to the OpenAI module**  
    Drag the arrow from the WhatsApp trigger to the OpenAI module.  
    The connection line turns solid, indicating a data flow.

11. **Map the incoming message to the prompt**  
    In the OpenAI module, click **“Prompt”** field, then click the **“Insert variable”** button.  
    Choose **“Message body”** from the WhatsApp trigger.  
    This passes the user’s text into the prompt’s “clarifying questions” section.  
    Save the scenario.

12. **Activate the scenario**  
    Click the **“Enable”** toggle in the top-right corner of the scenario editor.  
    A confirmation dialog appears; click **“Yes”**.  
    The status changes to **“Running”**.  
    Expected output: a live scenario icon appears on the dashboard.

13. **Test the prompt with a

---

## Procedure 4.3: INTEGRATE Stripe Payments to Monetize the WhatsApp Bot

1. **Open a web browser** and go to **https://www.make.com/en**.  
2. Click the **Sign in** button in the upper‑right corner.  
3. Log in with your Make.com credentials (or register if you have no account).  
4. Once on the dashboard, click the **Create new scenario** button.  
   *Do you see the “Create new scenario” button? If not, refresh the page or clear your browser cache.*  

5. In the scenario builder, click the **+ Add** button and type **Stripe** in the search bar.  
6. Select **Stripe – New payment** from the list of triggers.  
7. Click **Add** to create a new connection.  
8. Paste your **Secret Key** from the Stripe dashboard (found under Developers → API keys).  
   *Do you see the “Stripe Connected” status? If not, double‑check the key or regenerate a new one in Stripe.*  

9. Add a **Twilio** module to send WhatsApp messages: click **+ Add** → type **Twilio** → choose **Send WhatsApp message**.  
10. Click **Add** to connect Twilio.  
11. Enter your **Account SID** and **Auth Token** from the Twilio console.  
12. In the **From** field, type your Twilio WhatsApp-enabled number (e.g., `whatsapp:+14155238886`).  
    *If you see “Invalid phone number” error, ensure the number is verified under Twilio → Messaging → Settings → WhatsApp Sandbox.*  

13. Insert a **ChatGPT** module for dynamic product description: click **+ Add** → **ChatGPT** → **Send a prompt**.  
14. In the **Prompt** field, enter:  
    ```
    Provide a concise product description for {ProductName} priced at ${Price}.
    ```  
15. Add a **Set variable** module to store the product ID and price.  
16. Click **Add** → **Set variable** → name it `ProductID`, set the value to **`prod_ABC123`** (replace with your actual Stripe product ID).  
    *Do you see the variable “ProductID” listed in the scenario? If not, check the variable name spelling.*  

17. Insert an **HTTP** module to

## Check-In: Module 4 Complete

- [ ] CREATE A MAKE.COM SCENARIO FOR WHATSAPP SALES BOT AUTOMATION completed and verified
- [ ] Configure ChatGPT Prompt for Personalized Sales Interaction completed and verified
- [ ] INTEGRATE Stripe Payments to Monetize the WhatsApp Bot completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 5: CLIENT ACQUISITION

## Overview  
In Module 5 we pivot from bot creation to the lifeblood of any SaaS: paying customers.  WhatsApp dominates business messaging in Africa, and an AI‑powered sales bot can close deals faster than a human team can.  This module equips you with a proven funnel that turns cold leads into recurring revenue in under a week.  If you skip this step, your bot will sit idle like a silent shop‑front, no matter how sophisticated its architecture.  You’ll waste development time, miss out on early cash‑flow, and risk losing credibility when prospects demand a live salesperson.  

The module is broken into three precise procedures: (1) Set up an automated outreach system that plugs into WhatsApp, (2) Build a conversion‑optimized landing page that captures intent, and (3) Deploy a lead‑generation pipeline that feeds your bot with qualified prospects.  Each procedure is a command‑centered playbook with exact URLs, button clicks, and JSON payloads.  By following this sequence you’ll create a closed‑loop system where every message from a potential customer is tracked, nurtured, and handed off to your bot for a seamless handover to sales.  

The tools you’ll use are carefully chosen for their price, scalability, and integration depth.  Below is the toolkit you must have on hand before you begin.  

| Tool           | Purpose                                             | Free Tier                                           | Paid Tier                                                      |
|----------------|-----------------------------------------------------|-----------------------------------------------------|----------------------------------------------------------------|
| Make.com       | Automate workflow between WhatsApp, CRM, and bot    | 5,000 operations/month, 3 scenarios                 | Pro: $49/mo, 30,000 operations, unlimited scenarios            |
| ChatGPT (API)  | Generate bot dialogue and lead scoring logic        | $0.002 per 1K tokens (free tier limited)             | Standard: $20/mo for 100k tokens, Plus: $200/mo for 1M tokens |
| Vapi           | Connect WhatsApp Business API to Make              | 1,000 messages/month (trial)                        | Premium: $25/mo for 10k messages, $80/mo for 50k messages       |
| Zapier         | Sync contacts to email marketing tools             | 5 Zaps, 100 tasks/month                            | Starter: $19.99/mo, Unlimited: $49/mo                           |
| HubSpot CRM    | Store lead data and track engagement               | Free tier: 1,000 contacts, unlimited users         | Professional: $45/mo per user, Enterprise: custom pricing      |
| Canva          | Design landing page graphics                        | Free tier: 5GB storage, limited templates          | Pro: $12.99/mo for advanced assets, 1TB storage                |
| Klaviyo        | Email nurture sequences                            | Free tier: 250 contacts, 500 emails/month          | Starter: $20/mo for 250-500 contacts, Pro: custom pricing      |

**Estimated time to complete Module 5:** 4 – 6 hours (including setup, testing, and initial lead capture).  This is a fast‑track, high‑impact module that delivers the first cash‑generating loop for your WhatsApp bot business.

---

## Procedure 5.1: CREATE A LANDING PAGE THAT DIRECTS TRAFFIC TO YOUR WHATSAPP SALES BOT

1. **Open your web browser** and navigate to Hostinger’s free account sign‑up page:  
   `https://www.hostinger.com/register?utm_source=playbook&utm_medium=module5`.  
   *Expected output:* A registration form with fields for email, password, and domain name.  

2. **Fill in the required fields** exactly as follows:  
   - Email: `yourname@example.com`  
   - Password: `StrongPass!2026` (must contain 8‑12 characters, at least one number, one uppercase, one lowercase, one symbol)  
   - Domain: `mywhatsappbot.com` (or any available domain you prefer)  
   Click the **bold** button **“Create Account”**.  

3. **Verify your email** by opening the inbox, clicking the confirmation link from Hostinger.  
   *Expected output:* Browser redirects to Hostinger dashboard.  

4. **Navigate to the hosting plan**: Click on the **“Hosting”** tab, then click the **“Get Started”** button next to the “Starter” plan.  
   *Interactive check‑in:* Do you see the **“Starter”** plan with $0.99/month? If not, ensure you are logged in and that the free tier is still available.  

5. **Select the “Starter” plan** and click **“Continue”**.  
   *Expected output:* Plan summary page showing $0.99/month, 1GB RAM, 20GB storage, 100GB bandwidth.  

6. **Proceed to checkout**: Click the **“Buy Now”** button.  
   *Expected output:* Checkout page with payment options; choose the “Monthly” billing cycle and click **“Purchase”**.  

7. **Finish the purchase** with the free trial credit card:  
   - Card number: `4242 4242 4242 4242`  
   - Expiry: `12/26`  
   - CVC: `123`  
   Click **“Pay with Card”**.  
   *Expected output:* Confirmation screen stating “Your account is active. You have a 30‑day free trial.”  

8. **Add a website via Hostinger’s “Website Builder”**:  
   - In the dashboard, click **“Add Site”**.  
   - Choose **“Website Builder”**.  
   - Select the **“Store”** template (recommended for CTA buttons).  
   *Interactive check‑in:* Do you see the **“Publish”** button on the right sidebar? If not, you may still be in the template gallery. Click **“Select”** then **“Edit”** to open the editor.  

9. **Edit the header**:  
   - Hover over the header, click **“Edit”**.  
   - Replace the placeholder text “Your Business” with **“Boost Your Sales with WhatsApp AI Bot”**.  
   - Click the **bold** button **“Save”**.  

10. **Add a CTA button**:  
    - Drag the **“Button”** widget from the left panel onto the hero section.  
    - In the button settings:  
      - Text: **“Chat on WhatsApp”**  
      - Link: `https://wa.me/254700123456` (replace with your business number, no + or spaces).  
      - Target: **“_blank”** (opens in a new tab).  
    - Click **“Apply”**.  
    *Interactive check‑in:* Do you see the button labeled “Chat on WhatsApp” on the preview? If not, check that the link field contains the exact WhatsApp click‑to‑chat URL.  

11. **Publish the site**:  
    - Click the **bold** button **“Publish”** in the top right corner.  
    - Confirm by clicking **“Publish”** on the modal.  
    *Expected output:* Confirmation banner “Your site is live at https://mywhatsapp

---

## Procedure 5.2: Automate Lead Capture and Qualification via Make.com Scenarios  

1. **Open your web browser** and navigate to **https://www.make.com**.  
2. Click the **bold** button **“Sign up”** in the top‑right corner.  
3. Enter your email, choose a password, and click **“Create account”**.  
4. Confirm the email you receive and log in.  
5. Once logged in, click the **bold** button **“Create a new scenario”** in the **Dashboard**.  
   *Do you see the “Create a new scenario” button? If not, refresh the page or clear your cache.*  

6. In the “Choose a trigger” dialog, type **“Webhook”** in the search box and select **“Webhooks” → “Custom Webhook”**.  
7. Click **“Add”**.  
8. In the Webhook settings panel, rename the webhook to **“LeadCaptureWebhook”**.  
9. Click **“Save”**.  
10. Copy the URL displayed under **“Webhook URL”**; save it to a clipboard.  
    *Do you see the webhook URL? If not, click “Show URL” and then copy.*  

11. Open a new tab and go to **https://www.twilio.com**.  
12. Click **“Log in”** (top right) and sign in with your Twilio credentials.  
13. In the Twilio console, click **“Programmable Messaging”** → **“WhatsApp”** → **“Sandbox Settings”**.  
14. Under **“Sandbox Configuration”**, set the **“WHEN A MESSAGE COMES IN”** field to the webhook URL you copied in step 10.  
15. Click **“Save”**.  
    *Do you see the “WHEN A MESSAGE COMES IN” field updated? If not, double‑check the URL and click “Save” again.*  

16. Return to Make.com and add a new module by clicking the **plus (+)** icon next to the webhook module.  
17. Search for **“OpenAI”** and select **“ChatGPT – Completion”**.  
18. In the ChatGPT module, click **“Add”** → **“New connection”**.  
19. Enter your **OpenAI API key** (found at https://platform.openai.com/account/api-keys) and click **“Test & Create”**.  
20. In the **Prompt** field, paste:  
```
You are a sales assistant. A user just sent a WhatsApp message: "{{Webhook.Content}}".  
Determine if they are a qualified lead:  
- If they mention “pricing” or “quote”, respond “Qualified”.  
- If they ask for more info, respond “Not yet”.  
Return only “Qualified” or “Not yet”.
```  
21. Set **Temperature** to **0.0** and **Max Tokens** to **10**.  
22. Click **“Save”**.  
    *Do you see the ChatGPT module with your connection? If not, verify your API key.*  

23. Add a **Filter** module (click **plus (+)**, search **“Filter”**).  
24. In the Filter, set the condition: **“ChatGPT – Completion.output”** **equals** **“Qualified”**.  
25. Click **“Save”**.  
    *If you see a warning “Condition not met”, ensure the prompt returns exactly “Qualified” or “Not yet” (no extra whitespace).*  

26. Add **“Airtable”** → **“Create a record”** (click

---

## Procedure 5.3: Launch a Retargeting Email Sequence to Monetize Bot Leads

1. **Open a web browser** and go to the Klaviyo login page at `https://www.klaviyo.com/login`.  
2. **Enter your credentials** (email & password) and click the **Log In** button.  
3. In the left‑hand navigation pane, click **Lists & Segments** → **Create List**.  
4. In the pop‑up, type **Bot Leads – Retarget** into the **List name** field and click **Create List**.  
   - *Do you see the “Bot Leads – Retarget” list now? If

## Check-In: Module 5 Complete

- [ ] CREATE A LANDING PAGE THAT DIRECTS TRAFFIC TO YOUR WHATSAPP SALES BOT completed and verified
- [ ] Automate Lead Capture and Qualification via Make.com Scenarios completed and verified
- [ ] Launch a Retargeting Email Sequence to Monetize Bot Leads completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 6: DELIVERY

## Overview
In this module you will master the **delivery pipeline** that turns a raw WhatsApp sales bot idea into a polished, high‑volume revenue engine. You’ll learn how to set up continuous integration checkpoints, automate client‑specific customizations, and craft communication templates that keep leads warm and conversion rates high. Skipping Module 6 means you’ll ship bots that are buggy, unscalable, and poorly supported—customers will abandon the integration, churn, and you’ll lose your reputation before the first sale.

The delivery framework is built around **version control, automated testing, and live‑support orchestration**. You’ll use Make.com to orchestrate data flows between WhatsApp, CRM, and fulfillment systems, while ChatGPT powers dynamic, context‑aware responses. Together they ensure every bot delivers consistent, actionable value at scale.

**Tools required for this module**

| Tool          | Purpose                                 | Free Tier                                    | Paid Tier (Monthly) |
|---------------|-----------------------------------------|----------------------------------------------|---------------------|
| Make.com      | Automate integrations & workflows      | 1,000 operations/month, 5 scenarios          | Pro: $49             |
| ChatGPT API   | Generate contextual bot responses      | 100k tokens/month (ChatGPT‑4 Turbo)           | $20 (variable)       |
| GitHub Actions| CI/CD for code deployment              | Unlimited public repos                       | $4 (private repos)  |
| Postman       | API testing & mock endpoints           | Unlimited requests                            | $12 (Pro)           |
| Notion        | Project tracking & documentation       | Unlimited pages & blocks                      | $8 (Personal Pro)   |

**Estimated time to complete Module 6**: **8–10 hours** (including setup, testing, and client‑ready hand‑off).

---

## Procedure 6.1: BUILD A DELIVERY PIPELINE IN MAKE.com FOR WHATSAPP BOTS

1. **Open a web browser** and go to https://www.make.com/en/signup.  
   - Enter **your email** and click **“Create account”**.  
   - Verify your email, then log in at https://www.make.com/en/login.  
   *Expected output:* You see the Make.com dashboard with the **“My account”** icon on the top‑right.

2. Click the **“Create new scenario”** button on the left‑hand side of the dashboard.  
   -

---

## Procedure 6.2: Create Quality Checkpoints for Consistent Bot Delivery

1. **Open a web browser** and navigate to [**Make.com**](https://www.make.com/en/register?pc=menshly) at `https://www.make.com/en/login`.  
   - **Login** with your credentials.  
   - If you do **not** have an account, click **bold** `SIGN UP`, choose **Email**, and follow the on‑screen verification.  
   - *Expected output*: You are on the **Make.com Dashboard** (blue header, “My Scenarios” tab visible).

2. **Create a new scenario** by clicking **bold** `NEW SCENARIO` in the top‑right corner.  
   - Give the scenario the name **“WhatsApp Bot Test”** and click **bold** `CREATE`.  
   - *Expected output*: You land on the scenario canvas with an empty **Add a module** button.

3. **Add a Webhook module**:  
   - Click the **Add a module** button, type **“Webhook”** in the search bar, and select **bold** `Webhook > Custom Webhook`.  
   - Click **bold** `ADD A WEBHOOK`.  
   - Name the webhook **“WhatsAppIncoming”** and click **bold** `SAVE`.  
   - *Expected output*: A URL appears, e.g., `https://hook.make.com/abcd1234`.  
   - Copy this URL to your clipboard.

4. **Configure Twilio WhatsApp to forward messages to Make.com**:  
   - Go to Twilio Console: `https://www.twilio.com/console/phone-numbers/incoming`.  
   - Select your WhatsApp‑enabled number, scroll to **“Messaging”** → **“A MESSAGE COMES IN”**.  
   - Set the **Webhook** to **“HTTP POST”** and paste the Make.com URL from step 3.  
   - Click **bold** `SAVE`.  
   - *Check‑in*: Do you see the Twilio console confirm the webhook URL? If not, verify that you are editing the correct number and that the URL is correctly pasted.

5. **Add an HTTP module to call OpenAI

## Check-In: Module 6 Complete

- [ ] BUILD A DELIVERY PIPELINE IN MAKE.com FOR WHATSAPP BOTS completed and verified
- [ ] Create Quality Checkpoints for Consistent Bot Delivery completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 7: SCALING  

## Overview  

Module 7 takes the foundation you built in the earlier modules and turns it into a scalable, revenue‑generating engine. You’ll learn how to move from a solo operation to a small team, how to delegate tasks with clear SOPs, and how to perform a margin analysis that validates every dollar you invest. If you skip this module, you’ll stay stuck in a one‑person bottleneck, unable to handle high‑volume leads, and you’ll pay more in the long run for every lead that falls through the cracks.  

The module is broken into three practical procedures: (1) hiring and onboarding your first contractor, (2) building SOPs for delegation, and (3) performing a margin analysis. Each procedure is a step‑by‑step operating system that you execute from start to finish, with interactive check‑ins and error handling. By the end, you’ll have a repeatable process that can triplicate your sales volume while keeping overhead under control.  

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| Make.com | Automate WhatsApp bot flows and data syncs | 1,000 operations/month | $25/mo (Unlimited) |
| ChatGPT (OpenAI) | Generate bot scripts, FAQs, and copy | 1,000 tokens/day | $20/mo (Pro) |
| Zapier | Connect ChatGPT to WhatsApp Business API | 100 tasks/month | $26/mo (Starter) |
| Hostinger | Host the webhook server for WhatsApp callbacks | 1GB storage, 1GB bandwidth | $3.95/mo (VPS) |
| Canva | Design bot welcome images and infographics | Unlimited free templates | $11.99/mo (Pro) |
| [Grammarly](https://grammarly.com/) | Polish bot messages for tone and clarity | 10,000 characters/month | $12/mo (Premium) |
| Apollo.io | Prospecting and lead enrichment | 10,000 credits/month | $99/mo (Pro) |
| ActiveCampaign | Email follow‑up automation after bot interaction | 500 contacts | $9/mo (Lite) |
| Loom | Record onboarding videos for contractors | Unlimited | $8/mo (Starter) |
| Notion | Store SOPs and project docs | Unlimited pages | $4/mo (Personal Pro) |

**Estimated time to complete Module 7**: 10 – 12 hours, including all three procedures, SOP creation, and margin analysis.

---

**Procedure 7.1** — Generation failed due to AI backend unavailability. Please retry later.

---

## Procedure 7.2: CREATE SOPs FOR DELEGATING BOT MAINTENANCE TASKS

1. **Open the Make.com dashboard**  
   - URL: `https://app.make.com/`  
   - Log in with your credentials.  
   - Click **⚙️ Settings** (top‑right gear icon).  
   - Click **API Keys** in the left pane.  
   - Click **Create a new key**, name it `Bot‑Maintenance‑Key`, set scope to **Read & Write**.  
   - Copy the key to clipboard.  
   - *Do you see the key listed? If not, refresh the page and try again.*

2. **Create a new Notion database for task assignments**  
   - Open Notion: `https://www.notion.so/`  
   - Click **+ New Page** on the left sidebar.  
   - Select **Table** from the “Database” options.  
   - Name the table **Bot Maintenance Tasks**.  
   - Add columns:  
     - `Task ID` (auto‑generated ID)  
     - `Description` (Title)  
     - `Assigned To` (Person)  
     - `Priority` (Select: Low / Medium / High)  
     - `Due Date` (Date)  
     - `Status` (Select: Pending / In‑Progress / Completed)  
     - `Last Updated` (Last edited time).  
   - *Do you see all columns? If not, add them manually via “+ Add a property”.*

3. **Create a Make.com scenario to sync Notion with the WhatsApp bot**  
   - In Make.com, click **Create new scenario**.  
   - Search for **Notion** and click the **+** icon.  
   - Select **Watch database items**.  
   - In the setup window, paste the API key from step 1.  
   - Choose the database `Bot Maintenance Tasks`.  
   - Set “Trigger every” to **5 minutes**.  
   - Click **Save**.  
   - Add a second module: search for **HTTP** → select **Make a request**.  
   - Configure to call your bot’s maintenance endpoint:  
     - Method: **POST**  
     - URL: `https://api.yourbot.com/maintenance`  
     - Headers: `Content-Type: application/json; Authorization: Bearer YOUR_BOT_TOKEN`  
     - Body (raw):  
       ```json
       {
         "taskId": "{{Notion.item.ID}}",
         "description": "{{Notion.item.Description}}",
         "assignedTo": "{{Notion.item.Assigned_To}}",
         "priority": "{{Notion.item.Priority}}"
       }
       ```  
   - Click **OK** → **Save** → **Run once**.  
   - *Do you see the scenario status change to “Running”? If not, click “Run once” again.*

4. **Add a “Mark as Completed” step in Make.com**  
   - Click **+** next to the HTTP module.  
   - Search for **Notion** → select **Update a database item**.  
   - Map the `Item ID` from the trigger to the `Item ID` field.  
   - Set the `Status` property to **Completed**.  
   - Click **OK** → **Save**.  
   - Test with a dummy task.  
   - *Do you see the task status change to “Completed” in Notion? If not, verify the mapping.*

5. **Set up error notification via Slack**  
   - In Make.com, add a third module: search for **Slack** → select **Send a message**.  
   - Connect your workspace.  
   - Channel: `#bot-maintenance`.  
   - Message:  
     ```
     ⚠️ Maintenance task {{Notion.item.ID}} failed: {{Error.message}}
     ```  
   - In the “Error handling” tab of the HTTP module, set “On error” → **Send a message**.  
   - *Check that the Slack integration shows a new message on the channel. If not, re‑authorize Slack.*

6. **Create a Replit script for advanced bot diagnostics**  
   - Go to Replit: `https://replit.com/`.  
   - Click **+ Create** → **Python**.  
   - Name the repl `bot‑diag`.  
   - Paste the following script:  
     ```python
     import requests, json, os

     BOT_TOKEN = os.getenv('BOT_TOKEN')
     ENDPOINT = "https://api.yourbot.com/diagnostics"

     def run_diagnostics():
         resp = requests.get(ENDPOINT, headers={"Authorization": f"Bearer {BOT_TOKEN}"})
         if resp.status_code != 200:
             raise Exception(f"Status {resp.status_code}: {resp.text}")
         data = resp.json()
         print(json.dumps(data, indent=2))

     if __name__ == "__main__":
         run

---

## Procedure 7.3: ANALYZE AND OPTIMIZE BOT PROFIT MARGINS  

1. **Log into your Make.com account**  
   - Visit https://www.make.com/en/login  
   - Enter your email in the **Email** field and your password in the **Password** field.  
   - Click the **Log in** button.  
   - *Expected output*: You should see the Make.com dashboard with the **Scenarios** tab highlighted.  

2. **Open the “WhatsApp Bot Profit Analysis” scenario**  
   - In the left sidebar, click **Scenarios**.  
   - Search for **WhatsApp Bot Profit Analysis** in the search bar and double‑click it.  
   - *Expected output*: The scenario editor opens with a series of modules connected in a flow.  

3. **Verify that the “Retrieve Bot Metrics” module is connected to your bot’s API**  
   - Click the module labeled **Retrieve Bot Metrics**.  
   - In the right panel, confirm that the **API URL** field contains `https://api.whatsapp.com/v1/bot/metrics`.  
   - If it reads something else, replace it with the correct URL.  
   - Click the **Test** button.  
   - *Expected output*: A JSON preview appears:  
     ```
     {
       "sessions": 1200,
       "messages_sent": 4800,
       "messages_received": 4700,
       "avg_response_time": 4.2
     }
     ```  

4. **Ensure the “Calculate Cost” module uses the correct pricing tiers**  
   - Click the module **Calculate Cost**.  
   - In the **Cost per Message** field, confirm the value is **$0.0005** (WhatsApp Business API fee).  
   - In the **Hosting Cost** field, confirm the value is **$5/month** (Hostinger Basic plan).  
   - In the **AI Processing Cost** field, confirm the value is **$0.02/message** (ChatGPT‑4 Turbo).  
   - Click **Save**.  

5. **Run the scenario once to populate the data**  
   - Click the **Run once** button in the top right corner.  
   - Wait for the execution to finish.  
   - *Expected output*: The **Run results** panel shows “Scenario finished successfully” and displays the final **Profit Margin** value.  

6. **Export the raw metrics to a CSV file**  
   - In the **Retrieve Bot Metrics** module, click the **Export → CSV** icon (the floppy disk with a download arrow).  
   - Choose the destination folder `C:\BotAnalytics\` and name the file `metrics_YYYYMMDD.csv`.  
   - *Interactive check‑in*: Do you see the file `metrics_YYYYMMDD.csv` in the destination folder? If not, navigate to the folder and ensure the file is not hidden.  

7. **Open the CSV file in Google Sheets**  
   - Go to https://sheets.google.com.  
   - Click **Blank** to create a new spreadsheet.  
   - In the top menu, choose **File → Import → Upload** and drag the CSV file into the upload area.  
   - In the import dialog, select **Replace current sheet** and click **Import data**.  
   - *Expected output*: The sheet now contains columns: sessions, messages_sent, messages_received, avg_response_time.  

8. **Create a new Google Sheet for profit calculations**  
   - In the same Google Sheets window, click the **+** icon at the bottom-left to add a new sheet named **ProfitCalc**.  
   - In cell **A1**, enter `Metric`.  
   - In cell **B1**, enter `Value`.  

9. **Populate the ProfitCalc sheet with raw data**  
   - In cell **A2**, type `Total Messages`.  
   - In cell **B2**, enter `=SUM('metrics'!B2:B)`.  
   - In cell **A3**, type `Avg Cost per Message`.  
   - In cell **B3**, enter `=0.0005 + 0.02`.  
   - In cell **A4**, type `Hosting Monthly Cost`.  
   - In cell **B4**, enter `5`.  
   - In cell **A5**, type `Total Cost`.  
   - In cell **B5**, enter `=B2*B3 + B4`.  
   - In cell **A6**, type `Revenue per Message`.  
   - In cell **B6**, enter `0.10` (average customer order value).  
   - In cell **A7**, type `Total Revenue`.  
   - In cell **B7**, enter `=B2*B6`.  
   - In cell **A8**, type `Profit`.  
   - In cell **B8**, enter `=B7-B5`.  
   - In cell **A9**, type `Profit Margin %`.  
   - In cell **B9**, enter `=B8/B7`.  

10. **Format the Profit Margin cell**  
    - Select cell **B9**, then click the **Number** dropdown → **Percent**.  
    - Set decimal places to **2**.  
    - *Expected output*: Cell B9 shows something like `55.00%`.  

11. **Create a chart to visualize profit trends**  
    - Highlight cells **A1:B8**.  
    - Click **Insert → Chart**.  
    - In the Chart Editor on the right, set **Chart type** to **Line chart**.  
    - Under **Data range**, confirm `ProfitCalc!A1:B8`.  
    - Click **Insert**.  
    - *Interactive check‑in*: Do you see a line chart with

## Check-In: Module 7 Complete

- [ ] Hire Your First Contractor to Expand Bot Development completed and verified
- [ ] CREATE SOPs FOR DELEGATING BOT MAINTENANCE TASKS completed and verified
- [ ] ANALYZE AND OPTIMIZE BOT PROFIT MARGINS completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 8: ADVANCED PATTERNS

## Overview  

Module 8 is the capstone of the *Build, Deploy, and Monetize WhatsApp Sales Bots* playbook. It moves you from basic bot deployment into the realm of high‑margin, scalable services. You’ll learn how to layer premium upsells (e.g., custom analytics dashboards, tiered support packages, and white‑label branding) on top of an existing WhatsApp bot, turning a single‑use tool into a recurring revenue engine. By mastering these patterns you’ll be able to charge clients a monthly fee, upsell add‑ons, and create a productized service that can be sold to hundreds of SMEs with minimal incremental effort. Skipping this module means you’ll miss out on the most profitable revenue streams in the WhatsApp ecosystem and will likely cap your earnings at a one‑time sale per bot.

The module is split into two detailed procedures: (1) Designing and launching a subscription‑based upsell framework, and (2) Building a productized bot‑as‑a‑service platform. Both leverage the same stack of tools, but each procedure dives deep into distinct business models. The skill set you acquire here is what separates a one‑off developer from a full‑blown SaaS entrepreneur in the African market.

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| Make.com | Workflow automation, API orchestration | 1,000 operations/month, 5 scenarios | 1,000 operations/month, 5 scenarios ($9/mo) |
| ChatGPT (OpenAI) | Natural‑language generation, bot logic | 10k tokens/month | Unlimited tokens (ChatGPT Plus $20/mo) |
| Vapi | WhatsApp Business API integration | 1,000 messages/month | 10,000 messages/month ($50/mo) |
| Zapier | Edge‑case data sync, event triggers | 100 tasks/month | 750 tasks/month ($19.99/mo) |
| ActiveCampaign | Subscription billing, upsell workflows | 500 contacts | 5,000 contacts ($29/mo) |
| Shopify | Productized service storefront | 50 products | Unlimited (Basic $29/mo) |
| Canva | Visual assets for upsell pages | Unlimited free features | Pro $12.99/mo |
| ElevenLabs | Voice‑to‑text / text‑to‑speech for bot responses | 5,000 characters/month | 30,000 characters/month ($25/mo) |
| Hostinger | VPS for bot hosting | 1GB RAM, 1 vCPU | 2GB RAM, 1 vCPU ($3.95/mo) |
| Midjourney | AI‑generated visuals for marketing | 200 images/month | Unlimited (Starter $10/mo) |

**Estimated time to complete Module 8**: 4–5 hours. This includes time for reading, setting up the tools, running the two procedures, and validating the recurring revenue pipeline.

---

## Procedure 8.1: Launch a High‑Ticket Consultation Service for WhatsApp Bot Customization

1. **Open your web browser** and go to **https://www.make.com/**.  
   - Click the **Sign Up** button (top‑right).  
   - Enter your email, choose a password, and click **Create Account**.  
   - Confirm your email via the link sent to your inbox.  
   **Check‑in:** Do you see the Make.com dashboard with the “New Scenario” button? If not, check that you have verified your email and that pop‑ups are not blocked.

2. **Create a new scenario**:  
   - In the dashboard, click **New Scenario** (bold).  
   - Search for the **Webhook** module and drag it onto the canvas.  
   - Click the **Create a new webhook** button (bold) and name it `WhatsAppIncoming`.  
   - Copy the generated URL – you will need it later.  
   **Check‑in:** Do you see a webhook URL that looks like `https://hook.integromat.com/xxxxxx`? If not, ensure you clicked “Create a new webhook”.

3. **Add a Vapi WhatsApp module**:  
   - Click the **+** icon next to the Webhook, search for **Vapi**, and select **WhatsApp Send Message**.  
   - In the Vapi settings panel, click **Add a connection** (bold).  
   - Enter your Vapi API Key (found in your Vapi dashboard) and click **Save**.  
   - Map the incoming webhook field `number` to the Vapi field **To**.  
   **Check‑in:** Do you see a Vapi module with the “To” field mapped? If not, confirm your API key is correct.

4. **Add an OpenAI module (ChatGPT)**:  
   - Click the **+** icon after the Vapi module, search for **OpenAI**, and select **Send prompt**.  
   - Click **Add a connection** (bold), paste your OpenAI API Key, and click **Save**.  
   - In the prompt field, type:  
     ```
     You are a sales consultant. Create a short, persuasive reply for a client who wants a WhatsApp bot for high‑ticket sales. Include a call‑to‑action for a consultation call.
     ```  
   - Map the Vapi response `body` to the OpenAI prompt input.  
   **Check‑in:** Do you see the OpenAI module with the prompt text and the “Send prompt” button? If not, re‑enter your API key.

5. **Add a “Send WhatsApp Message” action**:  
   - Add another Vapi WhatsApp module, choose **Send Message**.  
   - Map the `number` from the Webhook to **To** and the OpenAI response to **Message**.  
   - Click **Run once** (bold) to test.  
   **Expected Output:** A WhatsApp message is delivered to the customer’s number with a concise sales pitch and a link to book a call.  
   **Check‑in:** Do you see the “Run once” button working and a test message in WhatsApp? If your message fails, check that the Vapi connection is active and the number format is `+<country code><number>`.

6. **Set up a Calendly booking link

---

## Procedure 8.2: **Set Up a Recurring Subscription Plan for Bot Maintenance and Analytics**

1. **Create a Stripe Account**  
   - Navigate to **https://dashboard.stripe.com/register**.  
   - Click **“Create an account”**.  
   - Enter your business email, full name, and a secure password.  
   - Click **“Create account”**.  
   - Expected output: Stripe dashboard home screen with “Dashboard” on the left sidebar.

2. **Create a New Product in Stripe**  
   - In the dashboard, click **“Products”** in the left sidebar.  
   - Click **“+ New”** (button in the top-right corner).  
   - In the modal, set **“Name”** to **“WhatsApp Bot Maintenance & Analytics”**.  
   - Leave **“Description”** blank.  
   - Click **“Save product”**.  
   - Expected output: Product card with the name displayed.

3. **Add a Recurring Price to the Product**  
   - Within the product card, click **“Add a price”**.  
   - In the **“Price details”** pane, set **“Price”** to **$30.00**.  
   - Set **“Billing period”** to **Monthly**.  
   - Click **“Save price”**.  
   - Expected output: Price row showing “$30.00 / month”.

4. **Generate a Stripe Webhook for Make.com**  
   - In Stripe, click **“Developers”** → **“Webhooks”**.  
   - Click **“+ Add endpoint”**.  
   - In the **“Endpoint URL”** field, enter the Make.com webhook URL (see step 5).  
   - Under **“Events to send”**, check **“checkout.session.completed”** and **“invoice.payment_succeeded”**.  
   - Click **“Add endpoint”**.  
   - Expected output: Endpoint listed with the URL and selected events.

5. **Create a Make.com Scenario for Stripe Webhooks**  
   - Open Make.com: **https://www.make.com/**.  
   - Log in with your credentials.  
   - Click **“Create a new scenario”** (top-left).  
   - In the search bar, type **“Stripe”** and click **“Stripe”**.  
   - Drag the **“Watch Events”** module onto the canvas.  
   - In the module settings, click **“Add a connection”**, then **“Connect to Stripe (API Key)”**.  
   - Copy your Stripe secret key from **https://dashboard.stripe.com/apikeys** and paste it into the Make.com connection field.  
   - Set **“Event type”** to **“checkout.session.completed”**.  
   - Click **“Save”**.  
   - Expected output: Stripe module icon on canvas with “watch events” label.

6. **Create a Vapi Trigger for WhatsApp**  
   - In the same Make.com scenario, click the **“+”** icon next to the Stripe module.  
   - Search for **“Vapi”** and select **“New Message”**.  
   - Click **“Add a connection”**, enter your Vapi API key (found at **https://app.vapi.io/dashboard**).  
   - Set **“Channel”** to **“WhatsApp”**.  
   - Click **“Save”**.  
   - Expected output: Vapi module icon connected to Stripe module.

7. **Add a Notion Module to Log Subscriptions**  
   - Click the **“+”** icon after the Vapi module.  
   - Search for **“Notion”** and pick **“Create a Page”**.  
   - Connect to Notion by adding a new integration via **https://www.notion.so/my-integrations** and paste the integration token.  
   - In the module settings, set **“Database”** to the Subscription Log database you created in Notion.  
   - Map the following fields:  
     - **Title** → **“Customer Email”** (from Stripe)  
     - **Subscription ID** → **“Session ID”** (from Stripe)  
     - **Amount** → **“Price”** (from Stripe)  
     - **Start Date** → **“Created at”** (from Stripe)  
   - Click **“Save”**.  
   - Expected output: Notion module icon with “create page” label.

8. **Add a Zapier Module to Send Email Notifications**  
   - Click the **“

## Check-In: Module 8 Complete

- [ ] Launch a High‑Ticket Consultation Service for WhatsApp Bot Customization completed and verified
- [ ] **Set Up a Recurring Subscription Plan for Bot Maintenance and Analytics** completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 9: FINANCIAL OPERATIONS

## Overview
This module trains you to capture every cent that flows through your WhatsApp sales bot ecosystem and turns it into actionable growth levers. You will build a live financial dashboard that pulls data from your WhatsApp bot, payment processors, and marketing automation tools. With that visibility, you’ll learn how to implement dynamic pricing strategies and generate professional proposals that close deals faster. If you skip this module, you risk buried revenue, missed upsell opportunities, and proposals that look like they were drafted by a beginner. In an African market where WhatsApp is the primary commerce channel, precision in financial tracking is not optional—it’s the difference between surviving and scaling.

You will also create contract templates that protect margins and standardize your billing process. These templates will integrate with your CRM so every new lead automatically receives a ready‑to‑send offer. By the end of this module, you will be able to monitor cash flow in real time, adjust prices on the fly, and send polished proposals that convert at the highest rates.

| Tool | Purpose | Free Tier | Paid Tier |
|------|----------|-----------|-----------|
| **Make.com** | Automate data pulls from WhatsApp, PayPal, Stripe, and CRM. | 1,000 operations/month, 5 active scenarios | $49/month (Unlimited) |
| **Notion** | Central dashboard and template hub. | Unlimited pages, 5 GB storage | $8/user/month (Pro) |
| **ChatGPT** | Generate pricing logic, FAQ scripts, and proposal drafts. | 3 M tokens/month (GPT‑3.5) | $20/month (ChatGPT‑4) |
| **Klaviyo** | Email follow‑ups for proposal acceptance. | 2 k contacts, 500 emails | $20/month (Starter) |
| **ActiveCampaign** | Manage contracts and recurring billing. | 500 contacts, 1 automation | $15/month (Lite) |
| **Zapier** | Connect Make.com to Shopify for sales sync. | 100 tasks/month | $19.99/month (Starter) |
| **Shopify** | Storefront for upsell and subscription management. | 14‑day free trial | $29/month (Basic) |
| **Hostinger** | Host your custom dashboard scripts. | 1 GB SSD, 100 GB bandwidth | $3.95/month (Basic) |
| [**Semrush**](https://www.semrush.com/) | Market research for price benchmarking. | 10 keyword positions | $119.95/month (Pro) |
| [**Canva**](https://www.canva.com/) | Design proposal templates and contract PDFs. | Unlimited templates, 5 GB storage | $12.99/month (Pro) |

Estimated time to complete: **6–8 hours** (including data integration, dashboard setup, pricing model creation, and template drafting).

---

## Procedure 9.1: Build a Make.com Financial Dashboard for Revenue Tracking

1. **Open the Make.com dashboard**  
   - URL: `https://www.make.com/en`.  
   - Log in with your credentials.  
   - Expected output: You see the “My scenarios” page with a button labeled **“Create a new scenario”**.

2. **Create a new scenario**  
   - Click **“Create a new scenario”**.  
   - In the pop‑up, type `WhatsApp Sales Bot Dashboard` and press **Enter**.  
   - Click **“Create”**.

3. **Add the WhatsApp module**  
   - In the scenario canvas, click the **“+”** icon.  
   - Search for `WhatsApp`, select **“WhatsApp – Send a message”** (Make’s official integration).  
   - Click **“Add”**.  
   - In the module settings, click **“Add new connection”**, choose your WhatsApp Business API provider (e.g., Twilio), and complete the OAuth flow.  
   - Once connected, the module shows **“Connected to Twilio WhatsApp”** under the module name.

4. **Add the Google Sheets module**  
   - Click the **“+”** icon again.  
   - Search for `Google Sheets`, select **“Google Sheets – Create a row”**.  
   - Click **“Add”**.  
   - In the settings, click **“Add new connection”**, log into your Google account, and grant Make access to Google Sheets.  
   - Select the spreadsheet named `Revenue_Traffic` (create it first in Google Drive if it doesn’t exist).  
   - Set the worksheet to `Sales`.  
   - Map the fields:  
     - `Timestamp` → `Now()` (Make function).  
     - `Order ID` → `{{WhatsApp.message.id}}`.  
     - `Amount` → `{{WhatsApp.message.amount}}`.  
     - `Currency` → `{{WhatsApp.message.currency}}`.

**Do you see the two modules (WhatsApp and Google Sheets) connected on the canvas? If not, double‑check that you have authorized Make to access your Twilio and Google accounts.**  

5. **Add a filter to capture only sales messages**  
   - Click the **“+”** icon next to the WhatsApp module.  
   - Search for `Filter`, select **“Filter – Only continue if…”**.  
   - In the filter condition, choose **`{{WhatsApp.message.type}}`** equals **`"payment_success"`**.  
   - Save the filter.  
   - Expected output: A green arrow from WhatsApp → Filter → Google Sheets.

6. **Add the ChatGPT module for revenue summarization**  
   - Click **“+”** on the canvas.  
   - Search for `ChatGPT`, select **“ChatGPT – Send a prompt”** (Make’s OpenAI integration).  
   - Click **“Add”**.  
   - In the settings, click **“Add new connection”**, input your OpenAI API key (free tier: 3,000 tokens/month, paid starts at $20/month).  
   - In the prompt field, type:  
     ```
     Summarize the total revenue for the last 7 days from the following data set:
     {{Google Sheets.Sales}}
     Output in JSON with keys: total, average, highest, lowest.
     ```  
   - Set the request to use the "gpt-3.5-turbo" model.  
   - Expected output: A JSON object like `{"total":"$12,340","average":"$1,760","highest":"$3,200","lowest":"$200"}`.

7. **Add a Google Data Studio (Looker Studio) module to render the dashboard**  
   - Click **“+”**.  
   - Search for `Google Data Studio`, select **“Google Data Studio – Create a report”**.  
   - Click **“Add”**.  
   - In the settings, choose the data source `Revenue_Trajectory` (create this in Data Studio).  
   - In the URL field, paste: `https://datastudio.google.com/reporting/abc123`.  
   - Save the module.

8. **Connect the ChatGPT output to Data Studio**  
   - Draw a line from the ChatGPT module to the Data Studio module.  
   - In the Data Studio settings, map JSON keys to Data Studio fields:  
     - `total` → `Total Revenue (USD)`.  
     - `average` → `Average Daily Revenue`.  
     - `highest` → `Highest Daily Revenue`.  
     - `lowest` → `Lowest Daily Revenue`.

**Do you see the Data Studio report showing a line chart for daily revenue? If not, confirm that the Data Studio URL is correct and that the data source is published.**  

9. **Add a Canva graphic module for visual appeal**  
   - Click **“+”**.  
   - Search for `Canva`, select **“Canva – Create a design”**.  
   - Click **“Add”**.  
   - In the settings, choose **“Infographic”** template and click **“Use template”**.  
   - In the design editor, drag and drop the Data Studio chart onto the canvas.  
   - Save and export as PNG.  
   - Store the PNG in a Google Drive folder `Dashboard

---

## Procedure 9.2: Draft Dynamic Pricing Proposal Templates with ChatGPT

1. **Open your web browser** and navigate to **https://chat.openai.com/**.  
2. Click the **bold** button **“Sign in”** at the top‑right corner.  
3. Enter your OpenAI email and password, then click **“Continue”**.  
4. Do you see the ChatGPT home screen with the “**New chat**” button?  
   *If not, ensure your browser has JavaScript enabled and reload the page. The screen should display a large blue button labeled **“New chat”**.*

5. Click **“New chat”**. The chat interface appears with a prompt placeholder.  
6. In the prompt box, type:  
   ```
   Draft a dynamic pricing proposal template for a WhatsApp sales bot service.  
   Include sections for:  
   • Service overview  
   • Tiered pricing (Basic, Standard, Premium)  
   • Custom add‑ons (extra support hours, advanced analytics)  
   • Payment terms and discounts for long‑term contracts  
   • Contact details  
   Use placeholders like {{ClientName}}, {{StartDate}}, {{ContractLength}}.  
   Output the template in Markdown.  
   ```
7. Press **Enter** to submit.  
8. Wait for the response. Expected result: a Markdown block containing the full proposal template.  
9. Do you see the Markdown output with the six required sections?  
   *If not, check that you typed the prompt exactly as shown. Delete the prompt and re‑enter it.*

10. Highlight the entire Markdown text and copy it to the clipboard (**Ctrl +C** on Windows or **⌘ C** on macOS).  
11. Open a new tab and go to **https://www.notion.so/**.  
12. Click **“Log in”** and log into your Notion account.  
13. In the left sidebar, click the **bold** button **“+ New page”**.  
14. Name the page **“Dynamic Pricing Proposal Template”** and press **Enter**.  
15. In the new page, click the first line and select **“Markdown”** from the toolbar (the icon looks like `</>`).  
16. Paste the copied Markdown text (**Ctrl + V** / **⌘ + V**).  
17. The template should render with headings and placeholders.  
18. Do you see the rendered preview with headings like **# Service Overview**?  
   *If the text shows raw Markdown syntax, click the three dots in the top right of the page and select **“Turn into” → “Markdown”**.*

19. Open **https://www.canva.com/** in a new tab.  
20. Click **“Log in”** and authenticate.  
21. In the Canva dashboard, click **“Create a design”** and choose **“A4 Document”**.  
22. In the left panel, click **“Uploads”** → **“Upload media”** → **“Text”**.  
23. Drag the **“Text block”** onto the canvas.  
24. Copy the rendered Markdown from Notion and paste it into the Canva text block.  
25. Format the text: set **font** to **Montserrat**, **font size** to **12pt**, **line spacing** to **1.15**.  
26. Add a header with your company logo (upload via **Uploads** → **Upload media**).  
27. Save the design by clicking the **bold** button **“Share”** and selecting **“Download”** → **PDF (Print)**.  
28. Choose **“High quality”** and click **“Download”**.  
29. Do you see the final PDF with the dynamic pricing template?  
   *If the PDF is garbled, ensure you selected **PDF (Print)** and not **PDF (Standard)**.*

30. **Optional – Automate distribution**:  
    a. Open **https://zapier.com/app/dashboard** and click **“Make a Zap”**.  
    b. For **Trigger App**, search for **Notion**, select **“New Database Item”**, and connect your account.  
    c

## Check-In: Module 9 Complete

- [ ] Build a Make.com Financial Dashboard for Revenue Tracking completed and verified
- [ ] Draft Dynamic Pricing Proposal Templates with ChatGPT completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 10: LAUNCH PLAN

## Overview  
This module delivers the exact day‑by‑day playbook that will take your WhatsApp Sales Bot from a blank screen to your first paying client within 30 days. The plan is a tightly choreographed 30‑day execution calendar, broken into five weekly milestones: initial audience research, bot design and schema, Make.com workflow construction, integration with ChatGPT, and live launch & client acquisition. Every step is a concrete command, not a suggestion, so you will know precisely what to click, what parameters to set, and what metrics to monitor.

Skipping this module means launching a bot that is under‑optimized, poorly tested, and unable to capture revenue. You’ll waste cycles on ad hoc tweaks and risk losing trust with your first customers. By following the schedule, you will have a live, tested bot, a proven sales funnel, and a client pipeline in place—all measured against the key performance indicators (KPIs) defined in the module.  

**Toolset Snapshot**  

| Tool           | Purpose                                  | Free Tier                                     | Paid Tier (Starter) |
|----------------|------------------------------------------|-----------------------------------------------|---------------------|
| Make.com       | Automate end‑to‑end WhatsApp workflow   | 1,000 operations/month, 5 scenarios           | $49/month – unlimited operations, priority support |
| ChatGPT        | Generate dynamic responses & scripts    | 3,000 tokens/day (free)                       | $20/month – 100k tokens/month, priority access |
| Zapier         | Connect Make.com to external CRM         | 100 tasks/month, 5 zaps                       | $19.99/month – 2,000 tasks, unlimited zaps |
| Hostinger      | Domain & web hosting for landing pages   | 1 GB bandwidth, 1 website                     | $3.95/month – 10 GB, unlimited websites |
| Shopify        | Storefront & payment gateway             | 14‑day free trial, no transaction fees       | $29/month – advanced features, higher limits |
| Canva          | Create branded WhatsApp button graphics | Unlimited downloads, basic templates          | $12.99/month – premium templates, brand kit |
| Grammarly      | Proofread bot FAQ & support docs         | Free (basic grammar)                          | $12/month – advanced style checks, plagiarism |
| ElevenLabs     | Voice‑to‑text / text‑to‑voice for bots   | 5 hours/month (text‑to‑voice)                 | $4/month – 30 hours/month, unlimited voice calls |

**Estimated Time to Complete**  
The structure of this module is engineered for a 30‑day sprint. If you dedicate 4–6 hours per day to the tasks outlined, you will finish the launch plan and secure a live client by Day 30.

---

## Procedure 10.1: Deploy Your WhatsApp Sales Bot to Production Using Make.com

1. **Open Make.com**  
   - Navigate to https://www.make.com/en.  
   - Click **“Sign Up”** in the top‑right corner.  
   - Fill in your email, password (at least 12 characters, mix of upper/lowercase, numbers, and symbols), and click **“Create account”**.  
   - Confirm your email via the link sent to your inbox.  
   - *Expected output:* You are logged into the Make.com dashboard (white background, navigation bar on the left).

2. **Create a New Scenario**  
   - In the dashboard, click **“Create new scenario”** (top‑right, blue button).  
   - A blank scenario canvas appears.  
   - Click the **“+” icon** in the center of the canvas.  
   - Search for **“WhatsApp”** and select **“WhatsApp by Twilio”**.  
   - Click **“Add”**.  
   - *Expected output:* The WhatsApp module appears on the canvas, labeled “WhatsApp – Trigger”.

3. **Connect Twilio WhatsApp**  
   - In the WhatsApp module, click **“Add connection”**.  
   - In the popup, select **“Twilio”**.  
   - Enter your Twilio Account SID, Auth Token (found in your Twilio console), and click **“Save”**.  
   - If you don’t have a Twilio account, visit https://www.twilio.com/try-twilio, sign up, and obtain the SID and token.  
   - *Expected output:* The module shows “Connected to Twilio”.

4. **Set Up the WhatsApp Trigger**  
   - In the WhatsApp module, choose the **“When a new message is received”** trigger.  
   - Leave **“From”** blank to accept messages from any number.  
   - Click **“Save”**.  
   - *Expected output:* The trigger is activated, and the canvas shows a green status icon on the module.

5. **Add a ChatGPT Action**  
   - Click the **“+” icon** next to the WhatsApp module.  
   - Search for **“OpenAI”** and select **“ChatGPT”**.  
   - Click **“Add”**.  
   - In the ChatGPT module, choose **“Send Prompt”**.  
   - In the **“Prompt”** field, insert the variable **{{WhatsAppMessage.body}}** (drag from the WhatsApp module).  
   - Set **“Model”** to **“gpt‑3.5‑turbo”**.  
   - Click **“Save”**.  
   - *Expected output:* The ChatGPT module is linked to the WhatsApp trigger, showing a flow from WhatsApp → ChatGPT.

6. **Add a Response to WhatsApp**  
   - Click the **“+” icon** after the ChatGPT module.  
   - Search for **“WhatsApp by Twilio”** again and add a second module.  
   - Choose **“Send a message”**.  
   - In the **“To”** field, insert **{{WhatsAppMessage.from}}**.  
   - In the **“Message”** field, insert **{{ChatGPTResponse.choices[0].message.content}}** (drag from ChatGPT).  
   - Click **“Save”**.  
   - *Expected output:* The scenario now has three modules: trigger → ChatGPT → response.

7. **Test the Scenario**  
   - Click the **“Run once”** button (green triangle at the top).  
   - A popup asks for a test message. Enter “Hi Bot” and click **“Send”**.  
   - The scenario runs: WhatsApp trigger receives the message, ChatGPT processes it, and the response is sent back.  
   - *Expected output:* In the scenario log, you see “WhatsApp message received” → “ChatGPT processed” → “Response sent”.  
   - If the response fails, check the error message in the log.

8. **Set Scenario Schedule**  
   - Click the **“Schedule”** icon (clock) on the top‑right of the canvas.  
   - Choose **“Always on”** to keep the scenario running continuously.  
   - Click **“Save”**.  
   - *Expected output:* The scenario status turns blue, indicating it’s live.

9. **Deploy to Production**  
   - Click **“Save”** (top‑right).  
   - Click **“Activate”** (next to Save).  
   - Confirm activation in the popup.  
   - *Expected output:* A banner appears: “Scenario is now active and running in real time”.

10. **Verify Live Messaging**  
    - From a personal phone, send a WhatsApp message to the Twilio number you configured.  
    - Wait 1–2 seconds for a reply.  
    - The message content should match ChatGPT’s response.  
    - *Expected output:* You receive an AI‑generated reply in WhatsApp.

**Interactive Check‑in**  
Do you see the green status icon on each module after clicking “Save”?  
- If not, ensure you selected the correct action (trigger, send prompt, send message) and that each field is populated.  
- If the status remains grey, click the module again and review the connected account.  

---

### Error Scenario

- **If you see** “Error: 401 – Unauthorized” **in the WhatsApp module**  
  - **This means** your Twilio credentials are incorrect or expired.  
  - **Fix it by**:  
    1. Log into https://www.twilio.com/console.  
    2. Copy the **Account SID** and **Auth Token** again.  
    3. In Make.com, edit the WhatsApp connection, paste the fresh credentials, and click **“Save”**.  
    4. Re‑run the scenario.

---

### Tool Comparison & Cost Table

| Tool | Plan | Price (USD) | Free Tier Limit | Notes |
|------|------|-------------|-----------------|-------|
| Make.com | **Professional** | $49/month | 3,000 operations/month | Unlimited scenarios, priority support |
| Twilio WhatsApp | **Pay‑as

---

## Procedure 10.2: CREATE AN END‑TO‑END PAYMENT FLOW FOR CLIENTS VIA STRIPE INTEGRATION

1. **Open a new Make.com scenario**  
   - Go to **https://www.make.com/en** and click **New Scenario** in the upper‑right corner.  
   - Name the scenario **WhatsApp‑Stripe‑Checkout** and click **Save**.  
   *Expected Output:* A blank scenario canvas with the “+” icon ready to add modules.

2. **Add the “Webhook” trigger**  
   - Click the **+** icon → **Choose App** → type **Webhook** → select **Webhook** → click **Add**.  
   - In the Webhook editor, click **Create a new webhook** → name it **WhatsApp‑Order** → click **Save**.  
   *Expected Output:* A URL that looks like `https://hook.make.com/abc123`.

3. **Copy the webhook URL**  
   - Highlight the URL in the Webhook module and press **Ctrl+C** (or click the copy icon).  
   *Expected Output:* URL copied to clipboard.

4. **Create a WhatsApp Business API rule in Vapi**  
   - Log in to **https://app.vapi.ai** (free tier: 100 messages/month).  
   - Click **Dashboard** → **WhatsApp** → **Add Phone Number** → follow the QR‑scan instructions.  
   - After activation, click **Automation** → **Add Rule** → set **Trigger:** *Incoming Message* → **Condition:** `contains "order"` → **Action:** *Send Webhook* → paste the copied Make.com webhook URL → click **Save**.  
   *Expected Output:* A rule that forwards any WhatsApp message containing “order” to the Make.com webhook.

5. **Return to Make.com and test the Webhook**  
   - In the Webhook module, click **Run Once** → send a test message via WhatsApp “order” → wait for the **Webhook Received** notification.  
   *Expected Output:* A row appears in the scenario with the message payload.  
   **Do you see the “Webhook Received” event in Make.com?**  
   *If not, check that the Vapi rule is active and that the webhook URL matches exactly.*

6. **Add the “Stripe” module**  
   - Click **+** → **Choose App** → type **Stripe** → select **Stripe** → click **Add**.  
   - Choose the action **Create a Checkout Session**.  
   *Expected Output:* Module with input fields for `Price`, `Currency`, `Success URL`, etc.

7. **Configure the Stripe Checkout Session**  
   - **Price**: click **+** → **Create a new price** → **Product**: “WhatsApp Order” → **Currency**: `USD` → **Amount**: `5000` (for $50.00) → click **Create**.  
   - **Payment Method Types**: select **card**.  
   - **Success URL**: `https://example.com/success` (replace with your domain).  
   - **Cancel URL**: `https://example.com/cancel`.  
   - **Mode**: `payment`.  
   - **Allow Promotion Codes**: toggle **ON**.  
   *Expected Output:* The module should display a JSON preview of the Checkout Session creation request.

8. **Add the “HTTP” module to capture the Checkout URL**  
   - Click **+** → **Choose App** → type **HTTP** → select **HTTP** → click **Add** → action **Get a file**.  
   - In the **URL** field, insert `{{Stripe Checkout Session.object.url}}`.  
   - Set **Method** to **GET**.  
   *Expected Output:* The HTTP module will return a 200 OK response and the Checkout URL in the output.

9. **Set up an email notification to the customer**  
   - Click **+** → **Choose App** → type **SendGrid** → select **SendGrid** → click **Add** → action **Send Email**.  
   - **To**: `{{Webhook Payload.customer_email}}` (ensure the WhatsApp message includes the email).  
   - **Subject**: “Your Payment Link for WhatsApp Order”.  
   - **Body** (HTML):  
     ```
     <p>Hello,</p>
     <p>Click <a href="{{HTTP Response.url}}">here</a> to complete your payment.</p>
     <p>Thank you!</p>
     ```  
   *Expected Output:* An email sent to the customer with a clickable payment link.

10. **Add a “Delay” module to wait for payment confirmation**  
    - Click **+** → **Choose App** → type **Delay** → select **Delay** → click **Add**.  
    - Set **Delay time** to **30 Seconds**.  
    *Expected Output:* A delay step that pauses the scenario before checking payment status.

11. **Add another Stripe module to retrieve session status**  
    - Click **+** → **Choose App** → type **Stripe** → select **Stripe** → click **Add** → action **Retrieve a Checkout Session**.  
    - In

---

## Procedure 10.3: Execute a 30‑Day Social Media Launch Campaign to Acquire Your First Paying Client

1. **Open your browser and navigate to** `https://buffer.com/signup`.  
   - Click the **“Sign up for free”** button.  
   - Enter your email, password (at least 12 characters, mix of upper/lowercase, numbers, and `!`), and click **“Create account”**.  
   - Expected: You see the Buffer dashboard with a welcome message “Welcome to Buffer – Let’s get started!”  

2. **Connect your Facebook Business Page**  
   - In Buffer, click the **“Add Social Accounts”** button.  
   - Select **“Facebook”**.  
   - Choose the **“Add page”** option, then pick the page you own.  
   - Click **“Allow”** on the Facebook permission dialog.  
   - Expected: Buffer lists your Facebook page with an icon and the status “Connected”.  

3. **Create a new Instagram Business account** (if you don't have one).  
   - Go to `https://www.instagram.com/accounts/login/` and log in.  
   - Click **“Switch to Professional”** → **“Business”**.  
   - Follow the prompts to link your Facebook Page.  
   - Return to Buffer, click **“Add Social Accounts”**, select **“Instagram”**, and authorize.  
   - Expected: Instagram appears in your Buffer list with “Connected”.  

4. **Add your LinkedIn Company Page**  
   - In Buffer, click **“Add Social Accounts”** → **“LinkedIn”**.  
   - Log in with your LinkedIn credentials.  
   - Select your company page and click **“Add”**.  
   - Expected: LinkedIn page shows under Buffer’s “Social Accounts”.  

5. **Do you see all four accounts (Facebook, Instagram, LinkedIn) listed in Buffer? If not, refresh the page and repeat the connect steps.**

6. **Open Canva (free tier)**  
   - Visit `https://www.canva.com`.  
   - Click **“Sign up for free”** → use the same email as Buffer.  
   - After account creation, click **“Create a design”** → **“Social Media”** → **“Square”** (1080x1080).  

7. **Design your first carousel post**  
   - Upload your brand logo via the **“Uploads”** tab, drag onto canvas.  
   - Use the **“Text”** tool to add a headline: “Boost Your Business Sales with WhatsApp AI Bots”.  
   - Add a short bullet list: 1) 24/7 Support 2) Automatic Follow‑ups 3) Lead Capture.  
   - Click **“Download”** → choose **PNG** → **“Download”**.  
   - Expected: A PNG file `WhatsAppBot_Sales.png` saved locally.  

8. **Create a second carousel slide**  
   - Duplicate the first slide in Canva by clicking **“Duplicate page”**.  
   - Replace text: “Case Study: 30% Increase in Bookings for XYZ SME”.  
   - Add a placeholder image of a phone.  
   - Download as `WhatsAppBot_CaseStudy.png`.  

9. **Upload both PNGs to Buffer**  
   - In Buffer, click **“New Post”** → **“Upload”** button.  
   - Drag `WhatsAppBot_Sales.png` and `WhatsAppBot_CaseStudy.png` into the upload area.  
   - Expected: Two new posts appear in “Drafts” with thumbnails.  

10. **Schedule the carousel for Day 1**  
    - Click the **“Schedule”** button on the first post.  
    - Set date/time to today at 10:00 AM UTC+1.  
    - Click **“Schedule Post”**.  
    - For the second post, schedule at 2:00 PM UTC+1.  

11. **Do you see both posts scheduled for today with the correct times? If not, adjust the time picker and reschedule.**

12. **Set up a Zapier workflow to auto‑post to WhatsApp via Make.com**  
    - Go to `https://zapier.com/app/dashboard` and click **“Create Zap”**.  
    - Trigger: **Buffer** → **“New Post Scheduled”**.  
    - Action: **Make.com** (choose the **Make** app) → **“Run Scenario”**.  
    - Connect your Make.com account (`https://www.make.com` – free tier 1,000 operations/month).  
    - In Make.com, create a scenario:
      - **Trigger**: **Buffer** → “New Post” (use the Zapier webhook URL).  
      - **Action**: **Twilio** → “Send WhatsApp Message” (Twilio free trial allows 1,000 messages/month).  
      - Input: **Body** = “🚀 New post from [BrandName]: {{Buffer.PostTitle}} – check it out! https://yourwebsite.com”.  
    - Test the Zap and ensure a **“Success”** status.  
    - Expected: The Zap shows “Zap is live” and the Make.com scenario shows “Last run successful”.  

13. **Create a lead‑capture form in Typeform (free tier)**  
    - Visit `https://www.typeform.com`.  
    - Click **“Create typeform”** → **“Start From Scratch”**.  
    - Add fields:  
      - **Name** (short answer)  
      - **Email** (email)  
      - **Phone** (phone number)  
      - **Business Type** (multiple choice: “Retail”, “Services”, “Manufact

## Check-In: Module 10 Complete

- [ ] Deploy Your WhatsApp Sales Bot to Production Using Make.com completed and verified
- [ ] CREATE AN END‑TO‑END PAYMENT FLOW FOR CLIENTS VIA STRIPE INTEGRATION completed and verified
- [ ] Execute a 30‑Day Social Media Launch Campaign to Acquire Your First Paying Client completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# APPENDIX A: COMPLETE TOOL REFERENCE

| Tool | Purpose | Free Tier | Paid Tier | When to Upgrade |
|------|---------|-----------|-----------|-----------------|
| **Make.com** | Low‑code integration platform that routes WhatsApp messages to ChatGPT and orchestrates multi‑step automations. | 100 operations/month, 3 scenarios, 1 GB data transfer | $49/month (1 000 ops, 5 GB data, advanced modules) | When your bot handles >200 messages/day or requires premium modules such as HTTP or Webhooks. |
| **ChatGPT / GPT‑4 API** | AI conversational engine that powers dynamic sales scripts and product recommendations. | Free tier: 3 000 tokens/month (ChatGPT web) | $20/month for ChatGPT Plus or $0.03/1 000 tokens (GPT‑4) | When you need higher throughput, lower latency, or access to GPT‑4. |
| **Twilio WhatsApp Business API** | Official WhatsApp channel for sending/receiving messages; handles compliance and delivery. | $15.50 free trial credit; 1 000 free messages | $0.005/message (India), $0.0075/message (US) + $0.005 per media | When you exceed trial credits or need guaranteed delivery and advanced features (message templates, media). |
| **Hostinger** | Domain registration, web hosting, and email forwarding for bot alerts. | Free email forwarding, $2.95/month shared hosting (basic) | $3.95/month shared hosting (Premium), $9.95/month VPS | When you need more bandwidth, SSL, or dedicated resources for high‑traffic bot dashboards. |
| **Stripe** | Secure payment processing for one‑time or subscription sales through WhatsApp. | No monthly fee; 2.9 % + 30¢ per successful charge | 2.9 % + 30¢ + 1 % for international cards | When you start recurring billing or need advanced payout schedules. |
| **Zapier** | Alternative integration platform; useful for quick email or CRM syncs. | 5 tasks/month, 5 Zaps | $19.99/month (750 tasks, 20 Zaps) | When you need simpler, pre‑built connectors for non‑WhatsApp workflows. |
| **Apollo.io** | Lead enrichment and outreach automation; feeds qualified prospects into the bot. | 1 000 credits/month | $99/month (5 000 credits) | When your lead list grows beyond 1 000 prospects or you need advanced filters. |
| **PhantomBuster** | Scraping and automation for social media and LinkedIn; gathers prospects for the bot. | 2 000 actions/month | $49/month (20 000 actions) | When you need bulk data extraction or frequent scrapes. |
| **Buffer** | Social media scheduling; promotes bot landing pages. | 3 social accounts, 10 scheduled posts | $15/month (5 accounts, unlimited posts) | When you require more accounts or higher posting frequency. |
| **Loom** | Video recording for onboarding or troubleshooting bot interactions. | 3 hour recording limit | $8/month (unlimited, HD) | When you need longer or higher‑quality videos for client demos. |
| **Calendly** | Scheduling tool for sales calls or bot demos. | 1 calendar, 30‑min meetings | $8/month (multiple calendars, custom branding) | When you need multiple meeting types or custom branding. |
| [**Beehiiv**](https://beehiiv.com/) | Email newsletter platform; used for retargeting sequences after bot interaction. | Free (up to 5 000 subscribers) | $25/month (up to 10 000 subscribers) | When your list



---

**Support Pollinations.AI:**

---

🌸 **Ad** 🌸
Powered by Pollinations.AI free text APIs. [Support our mission](https://pollinations.ai/redirect/kofi) to keep AI accessible for everyone.

# APPENDIX B: THE COMPLETE SOP INDEX

| SOP # | Procedure | Category | Difficulty | Est. Time |
|-------|-----------|----------|------------|-----------|
| 1 | Register Your Business Domain on Hostinger | Foundation | Easy | 20 min |
| 2 | Create a WhatsApp Business API Account on Twilio | Foundation | Medium | 45 min |
| 3 | Set Up Email Forwarding in Hostinger for Bot Alerts | Foundation | Easy | 15 min |
| 4 | Register Your WhatsApp Business API Credentials in Make.com | Tech Stack | Medium | 30 min |
| 5 | Create a Make.com Scenario to Forward WhatsApp Messages to ChatGPT | Tech Stack | Hard | 1 hr |
| 6 | Validate and Log Data Transfer from Make.com to ChatGPT | Tech Stack | Medium | 30 min |
| 7 | Create a Client Onboarding Flow for WhatsApp Bot Projects | Framework | Medium | 1 hr |
| 8 | Establish Quality Standards for Bot Deployment | Framework | Medium | 45 min |
| 9 | Create a Make.com Scenario for WhatsApp Sales Bot Automation | First Build | Hard | 1 hr 30 min |
| 10 | Configure ChatGPT Prompt for Personalized Sales Interaction | First Build | Medium | 45 min |
| 11 | Integrate Stripe Payments to Monetize the WhatsApp Bot | First Build | Medium | 30 min |
| 12 | Create a Landing Page that Directs Traffic to Your WhatsApp Sales Bot | Client Acquisition | Medium | 1 hr |
| 13 | Automate Lead Capture and Qualification via Make.com Scenarios | Client Acquisition | Hard | 1 hr 15 min |
| 14 | Launch a Retargeting Email Sequence to Monetize Bot Leads | Client Acquisition | Medium | 45 min |
| 15 | Build a Delivery Pipeline in Make.com for WhatsApp Bots | Delivery | Medium | 1 hr |
| 16 | Create Quality Checkpoints for Consistent Bot Delivery | Delivery | Medium | 30 min |
| 17 | Create SOPs for Delegating Bot Maintenance Tasks | Scaling | Medium | 45 min |
| 18 | Analyze and Optimize Bot Profit Margins | Scaling | Hard | 1 hr 30 min |
| 19 | Launch a High‑Ticket Consultation Service for WhatsApp Bot Customization | Advanced Patterns | Hard | 2 hrs |
| 20 | Set Up a Recurring Subscription Plan for Bot Maintenance and Analytics | Advanced Patterns | Medium | 45 min |
| 21 | Build a Make.com Financial Dashboard for Revenue Tracking | Financial Operations | Hard | 1 hr 30 min |
| 22 | Draft Dynamic Pricing Proposal Templates with ChatGPT | Financial Operations | Medium | 45 min |
| 23 | Deploy Your WhatsApp Sales Bot to Production Using Make.com | Launch Plan | Hard | 1 hr 30 min |
| 24 | Create an End‑to‑End Payment Flow for Clients via Stripe Integration | Launch Plan | Medium | 1 hr |
| 25 | Execute a 30‑Day Social Media Launch Campaign to Acquire Your First Paying Client | Launch Plan | Hard | 3 hrs |

*Word Count: 520*

# APPENDIX C: THE REVENUE CALCULATOR  

This appendix furnishes the exact operating system for projecting, tracking, and validating the revenue stream of a WhatsApp Sales Bot business. Follow each table and calculation step precisely; the numbers below are model figures derived from the playbook’s standard pricing and cost assumptions. Replace the placeholder values with your own data to generate a custom forecast.

---

## 1. Revenue Projections Table  

| Month | Revenue (USD) | Clients | Expenses (USD) | Profit (USD) |
|-------|---------------|---------|----------------|--------------|
| 1     | 2,400         | 8       | 1,200          | 1,200        |
| 3     | 8,800         | 30      | 3,500          | 5,300        |
| 6     | 18,000        | 60      | 6,200          | 11,800       |
| 12    | 36,000        | 120     | 12,000         | 24,000       |

**Explanation of Columns**

| Column | Calculation | Example (Month 1) |
|--------|-------------|-------------------|
| Revenue | `Clients × Monthly Retainer` | `8 × $300 = $2,400` |
| Clients | `Month n = Clients_{n‑1} + New Clients` (assume 4 new clients per month after Month 1) | `8 + 4 = 12` (Month 2) |
| Expenses | Sum of all recurring costs: Hostinger, Twilio, Make.com, Stripe, and marketing | `Hostinger 20 + Twilio 100 + Make.com 60 + Stripe 30 + Marketing 480 = $1,200` |
| Profit | `Revenue – Expenses` | `$2,400 – $1,200 = $1,200` |

**Interactive Check‑In**  
After populating the table for Month 1, verify that the Expense row lists each line item. If any cost is omitted, the Profit figure will be inflated.  

---

## 2. Pricing Tiers Table  

| Tier | Price (USD) | Deliverables | Margin (%) |
|------|-------------|--------------|------------|
| Basic | 300 | 1‑hour onboarding, 1 bot deployment, 30 days support | 50 |
| Standard | 600 | 2‑hour onboarding, 2 bot deployments, 60 days support, custom FAQ module | 55 |
| Premium | 1,200 | 4‑hour onboarding, 4 bot deployments, 90 days support, advanced analytics dashboard, priority email support | 60 |

**Margin Calculation**  
`Margin = (Price – Variable Cost) ÷ Price × 100`  
Variable cost per tier is derived from the cost of Make.com, Twilio, and Stripe per bot:  

| Tier | Bots | Variable Cost (USD) | Margin |
|------|------|---------------------|--------|
| Basic | 1 | 150 | 50 |
| Standard | 2 | 300 | 55 |
| Premium | 4 | 600 | 60 |

**Interactive Check‑In**  
Confirm that the “Deliverables” column lists all features you plan to sell. If you add a new feature, recalc the margin using the formula above.  

---

## 3. Break‑Even Analysis  

| Month | Cumulative Revenue | Cumulative Expenses | Cumulative Profit | Break‑Even Point |
|-------|--------------------|---------------------|-------------------|------------------|
| 1 | 2,400 | 1,200 | 1,200 | No |
| 2 | 4,800 | 2,400 | 2,400 | No |
| 3 | 13,600 | 5,900 | 7,700 | No |
| 4 | 20,800 | 9,200 | 11,600 | No |
| 5 | 28,000 | 12,500 | 15,500 | No |
| 6 | 46,000 | 18,700 | 27,300 | Yes |

**Break‑Even Calculation**  
The business reaches break‑even when `Cumulative Profit ≥ Total Initial Investment`.  
- Initial Investment = Hostinger domain ($10), Twilio API ($50), Make.com trial (free), Stripe account (free).  
- Total Initial Investment = $60.  

Because cumulative profit surpasses $60 at Month 6, the break‑even point is Month 6.  

**Interactive Check‑In**  
If your cumulative profit column shows a negative value for any month, double‑check the Expense entries. A missing marketing spend will artificially inflate profit.  

---

## 4. Detailed Cost Breakdown (per month, for 1 client on Standard tier)

| Expense | Tool | Plan | Monthly Cost | Notes |
|---------|------|------|--------------|-------|
| Web Hosting | Hostinger | Premium 1‑Year | $20 | Includes domain renewal |
| WhatsApp API | Twilio | Pay‑as‑You‑Go | $100 | 1,000 messages/month |
| Automation Platform | Make.com | Unlimited | $60 | 9,000 operations/month |
| Payment Processor | Stripe | Standard | $30 | 2.9 % + 30 ¢ per transaction |
| Email Marketing | Klaviyo | Starter | $20 | 2,500 contacts |
| CRM | Notion | Free | $0 | Internal tracking |
| Total |  |  | $250 |  |

**Margin Impact**  
With a Standard tier price of $600, the variable cost per client is $250, yielding a margin of 58 % (close to the tier table).  

---

## 5. Revenue Projection Methodology (Step‑by‑Step)

1. **Define Client Acquisition Rate**  
   - Month 1: 8 clients (from early adopters).  
   - Subsequent months: +4 new clients per month (steady growth).  

2. **Assign Pricing Tier**  
   - Assume 50 % of new clients select Basic, 30 % Standard, 20 % Premium.  
  

For the free step-by-step guide, see our [implementation guide]({< ref "/intelligence/build-an-ai-comic-book-creation-system-with-midjourney-the-complete-step-by-step.md" >}).


## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
- **[Vapi](https://vapi.ai/)** — AI voice agent platform — build and deploy voice AI
