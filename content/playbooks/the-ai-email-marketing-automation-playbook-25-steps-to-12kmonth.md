---
title: "The AI Email Marketing Automation Playbook: 25 Steps to $12K/Month"
date: 2026-07-04
category: "Playbook"
price: "₦35,000"
readTime: "85 MIN"
excerpt: "The AI Email Marketing Automation Playbook: 25 Steps to $12K/Month"
image: "/images/articles/playbooks/the-ai-email-marketing-automation-playbook-25-steps-to-12kmonth.png"
heroImage: "/images/heroes/playbooks/the-ai-email-marketing-automation-playbook-25-steps-to-12kmonth.png"
relatedOpportunity: "/opportunities/how-to-build-an-ai-email-marketing-automation-10k-20kmonth/"
relatedGuide: "/intelligence/build-an-ai-seo-automation-service-with-chatgpt-the-complete-step-by-step-guide/"
---
**The AI Email Marketing Automation Playbook: 25 Steps to $12K/Month**

This playbook extends our free implementation guide with complete procedures, SOPs, and revenue calculators. It is an OPERATING SYSTEM, not a blog post or a loose set of tips. **25 procedures. 10 modules. 12+ hours of reading and execution.** Follow each procedure in the exact order and you will build a turnkey AI‑powered email marketing automation business that delivers $12,000+ monthly recurring revenue, scales past 100 accounts, and eliminates the need for manual copy‑editing or inbox

---

# MODULE 1: FOUNDATION

## Overview

Module 1 is the bedrock upon which every AI‑powered email marketing automation business is built. In the next few hours you will register your legal entity, secure a professional domain, set up a verified email address, and install the core automation stack—Klaviyo, ActiveCampaign, and the integration engine Make.com. These steps are non‑negotiable: without a verified domain you cannot deliver campaign emails at scale; without a properly configured email identity you will be blocked by inbox providers; and without a reliable integration layer you will waste hours on manual data syncs that could be automated. Skipping this module risks low deliverability, compliance violations, and an unscalable workflow that will choke your growth.

The foundation also establishes the audit trail and security posture you need to protect client data. By integrating a single‑sign‑on (SSO) solution via Zapier and setting up two‑factor authentication (2FA) on all accounts, you create a secure environment that satisfies GDPR and CAN‑SPAM standards. When you finish this module you will have a fully functional SaaS stack that can ingest leads, segment lists, and launch automated nurture paths—all while collecting the data you need for hyper‑personalized AI content later in the playbook.

| Tool          | Purpose                                                      | Free Tier (Limit)                                 | Paid Tier (Price)                                 |
|---------------|--------------------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| Klaviyo       | Transactional & behavioral email automation                 | 2,000 contacts, 10,000 sends/month               | Growth: $20/month (10,000 contacts)              |
| ActiveCampaign| Lead scoring, CRM, and email automation                      | 500 contacts, 500 actions/month                  | Lite: $35/month (500 contacts)                   |
| Make.com      | Visual integration platform (formerly Integromat)           | 1,000 operations/month, 100 MB data transfer      | Pro: $9/month (10,000 operations)                |
| Zapier        | Quick‑start integration bridge                               | 5 Zaps, 100 tasks/month                          | Starter: $19.99/month (750 tasks)                |
| Hostinger     | Domain registration & shared hosting                         | Free domain with purchase, 10 GB storage         | Premium: $0.99/month (30 GB, 1 TB traffic)        |
| Notion        | Knowledge base & project management                          | Unlimited pages, 5 MB file uploads per workspace | Personal Pro: $10/month (Unlimited)              |
| Grammarly     | Writing & compliance checks                                 | 500 words/day, browser extension                 | Premium: $12/month (Unlimited)                   |

**Estimated time to complete:** 2 – 3 hours (including account verifications, DNS propagation, and tool onboarding).

---

## Procedure 1.1: REGISTER YOUR BUSINESS DOMAIN ON HOSTINGER

1. **Open your browser** and navigate to **https://www.hostinger.com/domains**.  
   *Expected result:* Hostinger domain search page with the search bar centered.  

2. **Sign in** to your Hostinger account.  
   - Click the **SIGN IN** button in the top‑right corner.  
   - Enter your email and password.  
   - Click the **LOG IN** button.  
   *Expected result:* Dashboard with “My Account” in the header.

3. **Navigate to Domain Registration**.  
   - From the left‑hand navigation panel, click **Domains → Register**.  
   - The Domain Registration page loads.  

4. **Search for your desired domain**.  
   - In the search field, type `yourbusinessname.com`.  
   - Click the **SEARCH** button.  
   *Expected result:* List of domain availability options; your domain shows “Available”.

5. **Add domain to cart**.  
   - Click the **ADD TO CART** button next to your domain.  
   - A confirmation banner appears: “`yourbusinessname.com` added to cart.”  

   **CHECK‑IN:** Do you see the confirmation banner “added to cart”?  
   If not, verify that the domain is still listed as “Available” and try again.

6. **Proceed to Checkout**.  
   - Click the **CART** icon at the top‑right.  
   - Review the cart and then click the **PROCEED TO CHECKOUT** button.  

7. **Select billing cycle**.  
   - On the billing page, choose the **3‑year** plan (cheapest per‑year rate).  
   - Click the **SELECT** button next to the 3‑year plan.  

8. **Enter registrant details**.  
   - Fill **Full Name**, **Company Name**, **Address**, **City**, **State/Province**, **ZIP/Postal Code**, **Country**, **Phone**, **Email**.  
   - Leave the **Privacy Protection** toggle set to **ON** (default).  

9. **Confirm domain privacy**.  
   - Ensure the **WHOIS Privacy** box is checked.  
   - Click the **CONTINUE** button.  

10. **Review and place order**.  
    - Verify the domain name, billing period, and price ($8.99/year).  
    - Click the **PLACE ORDER** button.  

    **CHECK‑IN:** Do you see the order summary with the correct price?  
    If the price differs, double‑check the billing period and domain extension.

11. **Complete payment**.  
    - Choose **Credit Card**.  
    - Enter card number, expiry, CVV, and billing address.  
    - Click the **PAY NOW** button.  

12. **Domain purchase confirmation**.  
    - A success page appears: “Your domain has been registered!”  
    - A confirmation email is sent to your inbox.  

    **ERROR SCENARIO:** If you see **“Domain already taken”**, this means someone else registered the domain in the last few minutes.  
    *Fix it by:*  
      - Returning to step 4 and searching for an alternative domain (e.g., `yourbusinessname.net`).  
      - Or adding a short suffix like `yourbusinessnamehq.com`.

13. **Log into your Hostinger control panel** again.  
    - Click **Hosting → Control Panel** at the top.  

14. **Set up DNS records** for email authentication.  
    - In the control panel, navigate to **Advanced → DNS**.  
    - Click **ADD RECORD**.  
    - For **Type**, select **TXT**.  
    - For **Host**, enter `@`.  
    - For **TXT Value**, paste the SPF record:  
      `v=spf1 include:klaviyo.com include:activecampaign.com ~all`.  
    - Click **SAVE**.  

15. **Add DKIM record**.  
    - Click **ADD RECORD** again.  
    - Choose **TXT**.  
    - Host: `k1._domainkey`.  
    - TXT Value: `v=DKIM1; k=rsa; p=YOUR_DKIM_PUBLIC_KEY_FROM_KLAVIYO_OR_ACTIVECAMPAIGN`.  
    - Click **SAVE**.  

    **CHECK‑IN:** Do you see the two TXT records listed under DNS?  
    If not, ensure you filled the exact host values and TXT values; retry the steps.

16. **Verify domain ownership with Google Search Console** (optional but recommended).  
    - Open a new tab and go to **https://search.google.com/search-console/welcome**.  
    - Click **Add Property** → **Domain** → enter `yourbusinessname.com`.  
    - Follow the **DNS verification** instructions: Host: `google-site-verification`.  
    - Paste the verification code provided by Google.  
    - Click **VERIFY**.  

17. **Automate domain verification** using Make.com.  
    - Open **https://www.make.com** and

---

## Procedure 1.2: Configure Email Forwarding in Hostinger for Client Communication

1. **Open your browser** and go to the Hostinger login page:  
   `https://www.hostinger.com/login`.  
   *Enter your email and password, then click the **Login** button.*

2. **Navigate to the dashboard** by clicking the **Dashboard** link in the top‑right corner after login.  
   *You should now see the Hostinger control panel.*

3. **Access the Email section**:  
   - Click the **Emails** tab in the left‑hand sidebar.  
   - In the dropdown, select **Email Forwarders**.  
   *You should see a table of existing forwarders (or an empty list).*

4. **Create a new forwarder**:  
   - Click the **Add Forwarder** button (top‑right).  
   - In the modal window, fill in:
     - **Email address**: `info@yourclientdomain.com`  
     - **Forward to**: `your.email@personal.com`  
   - Click **Create**.  

   **Do you see a new row appear in the forwarders table with your email address?**  
   *If not, check that you typed the addresses correctly. The button label must read **Create**.*

5. **Verify the forwarder**:  
   - Hover over the new row; you should see a **Copy** icon and a **Delete** icon.  
   - Click the **Copy** icon to copy the forwarder address to the clipboard.  
   - Paste the address into a test email client and send a test email to `info@yourclientdomain.com`.  
   - Confirm it arrives in `your.email@personal.com`.  

6. **Set up email forwarding for additional aliases** (optional):  
   - Repeat steps 4–5 for each alias you want to forward (e.g., `support@yourclientdomain.com`, `sales@yourclientdomain.com`).  

7. **Configure SPF and DKIM records** (recommended for deliverability):  
   - In the dashboard, go to **Domains** → **Manage** → **DNS Zone Editor**.  
   - Add an **SPF** TXT record:  
     `v=spf1 include:mail.hostinger.com ~all`  
   - Add a **DKIM** TXT record provided by Hostinger.  
   *After adding, click **Save**.*

   **Do you see the new TXT records listed in the DNS zone?**  
   *If not, ensure you are editing the correct domain and the records are formatted exactly as shown.*

8. **Test SPF/DKIM**:  
   - Send a test email from `info@yourclientdomain.com` to an external inbox (e.g., Gmail).  
   - Open the email headers and verify that SPF and DKIM pass.  

9. **Integrate forwarded emails with Klaviyo** (optional but recommended for automation):  
   - Log in to `https://app.klaviyo.com`.  
   - Navigate to **Integrations** → **Email** → **Add New Integration**.  
   - Choose **Zapier** as the integration method.  
   - Click **Connect**.  

   **Do you see the Klaviyo integration screen appear?**  
   *If not, confirm you are in the correct Klaviyo account and that your subscription allows integrations.*

10. **Set up a Zapier trigger**:  
    - Open `https://zapier.com/app/dashboard` and click **Make a Zap**.  
    - In the **Trigger** step, search for **Email Parser by Zapier**.  
    - Select **New Email** and click **Continue**.  
    - Create a new mailbox in Zapier and copy the unique email

---

## Procedure 1.3: CREATE A KLAVIYO ACCOUNT AND CONNECT YOUR DOMAIN FOR EMAIL DELIVERABILITY

1. Open Chrome, type **https://www.klaviyo.com/** and press **Enter**.  
2. In the upper‑right corner click the **Sign Up** button.  
3. Fill the form:  
   - **Email address**: you@example.com  
   - **Password**: StrongPassword123!  
   - **Company name**: YourBiz Inc.  
   Click **Create Account**.  
4. You should now see the Klaviyo dashboard with a blue banner “**Welcome! Let’s

## Check-In: Module 1 Complete

- [ ] REGISTER YOUR BUSINESS DOMAIN ON HOSTINGER completed and verified
- [ ] Configure Email Forwarding in Hostinger for Client Communication completed and verified
- [ ] CREATE A KLAVIYO ACCOUNT AND CONNECT YOUR DOMAIN FOR EMAIL DELIVERABILITY completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 2: TECH STACK

## Overview  
This module is the backbone of your AI‑powered email marketing automation venture. It walks you through every tool, connection, and API key that will keep your workflows humming and data flowing seamlessly. If you skip this step, your emails will be sent without real‑time personalization, your analytics will be fragmented, and your billing will be chaotic. In short, the stack is the nervous system of your operation; a weak connection here ripples into lost revenue downstream.  

You will:  
1. Set up hosting on Hostinger for your code repositories and static assets.  
2. Deploy a Replit instance to run your Python‑based AI content generator.  
3. Connect Klaviyo and ActiveCampaign via Zapier and Make.com to automate list segmentation, trigger sends, and sync engagement data.  
4. Hook Semrush for keyword insights that feed into subject‑line optimization scripts.  
5. Use Notion to log campaign parameters and Canva for dynamic image generation.  

By the end of this module you will have a fully wired ecosystem that pulls data from Klaviyo, pushes creative assets from Canva, and pushes AI‑generated copy from Replit into ActiveCampaign—all with zero manual intervention.

| Tool           | Purpose                                                                    | Free Tier                                   | Paid Tier (Monthly)                     |
|----------------|----------------------------------------------------------------------------|---------------------------------------------|----------------------------------------|
| Hostinger      | Web hosting for scripts and static files                                   | 1 GB SSD, 1 GB bandwidth, $0.99/month      | $3.95/month (Premium)                  |
| Replit         | Cloud IDE & execution environment for AI models                            | Unlimited private repls, 500 MB RAM         | $7/month (Hacker)                      |
| Zapier         | Workflow automation between Klaviyo, ActiveCampaign, and other services     | 5 Zaps, 100 tasks/month                    | $19.99/month (Starter)                 |
| Make.com       | Visual automation for complex data pipelines                               | 250 operations/month, 1 GB data             | $14/month (Starter)                    |
| Klaviyo        | Email platform & data lake                                                 | 500 contacts, 5 k emails/month             | $20/month (Starter)                    |
| ActiveCampaign | Email automation & CRM                                                     | 500 contacts, 3 k emails/month             | $15/month (Lite)                       |
| Notion         | Campaign documentation & parameter tracking                               | Unlimited pages, 5 MB file upload           | $8/month (Personal Pro)                |
| Canva          | Dynamic image generation for subject lines and email creatives             | Unlimited designs, 5 GB storage             | $12.99/month (Pro)                     |
| Semrush        | Keyword & competitive research to inform subject‑line AI                   | 10 queries/day, 1 project                  | $119.95/month (Pro)                    |

**Estimated Time to Complete:** 2 hours 30 minutes.

---

## Procedure 2.1: Configure Klaviyo API Credentials for Automated Segmentation

1. **Open a browser** and navigate to **https://www.klaviyo.com/login**.  
   *Enter your email and password, then click **Log In**.*

2. **Click your account avatar** (top‑right corner) and select **Account** from the drop‑down.  
   *You should now see the Account dashboard.*

3. In the left‑hand menu, click **Settings** > **API Keys**.  
   *The API Keys page lists any existing keys.*

4. **Click the blue button labeled** **Create API Key**.  
   *A modal opens titled “Create a new API key.”*  
   **Do you see the modal with a “Create” button?**  
   *If not, refresh the page or clear your browser cache.*

5. In the modal, type **Automated Segmentation** into the **Name** field.  
   *The field is a single‑line text box.*

6. Click **Create**.  
   *The modal closes and the new key appears in the list.*

7. **Click the copy icon** next to the new key to copy it to your clipboard.  
   *The key looks like: `1234567890abcdef1234567890abcdef`.*

8. **Open Notion** at **https://www.notion.so** and navigate to the “API Credentials” database.  
   *If you don’t have one, create a new database called “API Credentials.”*

9. Click **New** to add a record.  
   *Fill in:*

   | Property | Value |
   |----------|-------|
   | Service | Klaviyo |
   | Key Name | Automated Segmentation |
   | API Key | *Paste the key from step 7* |
   | Notes | Generated on 2026‑07‑04 |

   *Click **Save**.*

   **Do you see the new record with the key displayed?**  
   *If the key is blank, re‑paste it from the clipboard.*

10. **Test the key** using Postman (free

---

## Procedure 2.2: Set Up ActiveCampaign to Zapier Integration for Lead Capture

1. **Open your web browser and navigate to Zapier**  
   URL: `https://zapier.com/app/dashboard`  
   You should see the Zapier Dashboard with a green **Create Zap** button in the top‑right.

2. **Click the bold button** **Create Zap**.  
   This opens the Zap editor with the screen *"Choose a Trigger App"*.

3. **Search for “Webhooks by Zapier” in the search box** and click the result.  
   The trigger list appears; choose **Catch Hook**.

4. **Select “Catch Hook”** and click **Continue**.  
   Zapier will generate a unique URL like `https://hooks.zapier.com/hooks/catch/123456/abcdef`.

5. **Copy the generated URL** to your clipboard.  
   *Do you see the webhook URL? If not, refresh the page and re‑generate it.*

6. **Open

---

## Procedure 2.3: Verify Data Flow Between Klaviyo and ActiveCampaign via Webhooks

**Goal:** Confirm that an event triggered in Klaviyo is successfully received and parsed by ActiveCampaign, using a test webhook endpoint created in Replit.  
**Tools Needed:** Klaviyo (free tier up to 250 contacts), ActiveCampaign (free 14‑day trial), Replit (free tier unlimited), Make.com (free tier 100 operations/month).

> **Price Snapshot (2026‑07)**  
> | Tool | Free Tier | Paid Tier (Lowest) | Notes |
> |------|-----------|--------------------|-------|
> | Klaviyo | 250 contacts / $0 | Starter $20/mo | Includes basic webhooks |
> | ActiveCampaign | 500 contacts / $0 | Lite $15/mo | Includes webhook creation |
> | Make.com | 100 operations / $0 | Starter $59/mo | 10‑minute scenario run |
> | Replit | Unlimited | Pro $7/mo | Free hosting for webhook endpoint |

### Step 1 – Log In to Klaviyo  
1. Open **browser** and navigate to `https://www.klaviyo.com/login`.  
2. Enter your **email** and **password** and click **bold**`Log In`.  
3. After login, you should land on the **Dashboard** page.  

**Do you see the Klaviyo Dashboard with the “Audience” and

## Check-In: Module 2 Complete

- [ ] Configure Klaviyo API Credentials for Automated Segmentation completed and verified
- [ ] Set Up ActiveCampaign to Zapier Integration for Lead Capture completed and verified
- [ ] Verify Data Flow Between Klaviyo and ActiveCampaign via Webhooks completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 3: FRAMEWORK

## Overview  

In this module you will lock down the operating system that turns your AI‑powered email marketing service into a repeatable, scalable business. We start with the universal process that every client will experience: from the initial pitch to the final hand‑off of a fully automated Klaviyo/ActiveCampaign stack. By defining a rigid service delivery framework you eliminate guesswork, set clear expectations, and guarantee that every inbox you manage hits its KPIs.  

Skipping this foundation means you’ll be chasing ad‑hoc fixes, losing time on manual work, and, worst of all, delivering inconsistent results that erode trust. A clear framework lets you onboard clients in under two hours, double your throughput in months, and surface quality issues before they become revenue‑draining bugs.  

You’ll learn how to map the entire customer journey—lead capture, data enrichment, AI content generation, automation choreographies, and reporting—into a single, repeatable playbook. Each step will be codified in Notion, automated with Make.com or Zapier, and monitored with Klaviyo’s native analytics and ActiveCampaign’s deliverability dashboards. By the end of this module you’ll have a signed‑off SOP that you can hand over to a junior operator and expect 100 % compliance.

| Tool          | Purpose                                                                 | Free Tier                                      | Paid Tier (Starter) |
|---------------|--------------------------------------------------------------------------|------------------------------------------------|---------------------|
| Klaviyo       | Email delivery, segmentation, A/B testing, analytics                     | 2,000 contacts / 14,000 sends/month           | $20/month (up to 500 contacts) |
| ActiveCampaign | Automation builder, CRM integration, deliverability monitoring           | 500 contacts, 1,000 emails/month              | $45/month (up to 500 contacts) |
| Make.com      | Workflow automation between Klaviyo, ActiveCampaign, and other apps      | 1,000 operations/month, 2,000 operations/day | $19/month (10,000 ops/month) |
| Zapier        | Quick, low‑code connectors for 3rd‑party data feeds                     | 5 zaps, 100 tasks/month                       | $19/month (1000 tasks/month) |
| Notion        | SOP documentation, client intake templates, status dashboards           | Unlimited pages, 5 users, 2000 blocks/month   | $4/user/month (3 users) |
| Canva         | AI‑driven email template design, social graphics                        | Unlimited free templates, 5GB storage         | $12.99/month (Pro) |
| ChatGPT‑4     | Content generation, tone adjustment, subject line optimization         | 3,000 messages/month (free)                   | $20/month (ChatGPT Plus) |

**Estimated time to complete:** 5 – 6 hours (including documentation, tool setup, and dry‑run testing).

---

## Procedure 3.1: Draft Your AI Email Automation Service Blueprint  

1. **Open Notion**  
   - URL: `https://www.notion.so`  
   - Click **“Log In”** (top‑right).  
   - Insert your master **“AI Email Automation Blueprint”** database.  
   - Click **“+ New Page”**, name it **“Blueprint – Phase 1”**, and set the icon to a lightbulb.  

2. **Create a new table** inside the page.  
   - Click **“Table – Full Page”**.  
   - Add columns: **Stage, Tool, Action, Deliverable, Owner, Due Date, Status**.  
   - In the first row, enter **“Research & Ideation”** for Stage, **“Notion”** for Tool, etc.  

3. **Add a sub‑page** titled **“Client Discovery Sheet”**.  
   - Inside the table, click **“+ Add a page”**.  
   - In the sub‑page, create a form using **Google Forms** (free tier).  
   - Set questions:  
     - “Business Name (text)”  
     - “Industry (multiple choice)” – options from [**Semrush industry list**](https://www.semrush.com/).  
     - “Current Email List Size (number)”  
     - “Primary Goal (text)”.  

4. **Generate a preliminary service offering**.  
   - Open **ChatGPT (OpenAI) – ChatGPT‑Plus** at `https://chat.openai.com`.  
   - Prompt:  
     ```
     Draft a 3‑page AI‑powered email marketing service offer for a small e‑commerce store. Include:  
     • Service name  
     • 3 core deliverables  
     • Pricing tiers (Starter, Growth, Enterprise)  
     • AI tools used (Klaviyo, ActiveCampaign, Make.com, ChatGPT)
     ```  
   - Copy the resulting markdown into the Notion sub‑page under **“Service Draft”**.  

5. **Save the draft**.  
   - Press **Ctrl‑S** (Windows) or **Cmd‑S** (Mac).  
   - Verify the sub‑page shows the three sections and pricing table.  

> **Do you see the draft with the pricing tiers?**  
> If not, double‑check you pasted the Markdown correctly and refreshed the page.  

6. **Create a pricing calculator** in **Google Sheets** (free tier).  
   - URL: `https://sheets.google.com`  
   - Sheet name: **“Pricing Calculator”**.  
   - Columns: **Tier, Base Price, AI Add‑on Cost, Total**.  
   - Formula for Total: `=B2+C2`.  

7. **Populate AI Add‑on Cost**.  
   - In cell **C2**, enter `=IF(A2="Starter", 200, IF(A2="Growth", 500, IF(A2="Enterprise", 1000, 0)))`.  
   - Drag down for all tiers.  

8. **Create a section in Notion** for **Tool Stack**.  
   - List each tool with its exact pricing:  

| Tool | Free Tier | Paid Tier | Monthly Cost |
|------|-----------|-----------|--------------|
| Klaviyo | 2,500 contacts free | Starter $20 | $20 |
| ActiveCampaign | 500 contacts free | Lite $15 | $15 |
| Make.com | 2,000 operations/month | Basic $25 | $25 |
| ChatGPT‑Plus | N/A | Plus $20 | $20 |
| Zapier | 100 tasks/month | Starter $19.99 | $19.99 |

> **Do you see the table with accurate pricing?**  
> If a price is missing, consult each provider’s pricing page:  
> - Klaviyo: `https://www.klaviyo.com/pricing`  
> - ActiveCampaign: `https://www.activecampaign.com/pricing`  

9. **Draft the AI content workflow**.  
   - Use [**Make.com**](https://www.make.com/en/register?pc=menshly) to map email flow.  
   - URL: `https://www.make.com/en`.  
   - Click **“Create a new scenario”**.  
   - Add modules:  
     1. **Webhooks** → **Trigger** → **Incoming Webhook** (copy URL).  
     2. **ChatGPT** → **Send Prompt** → “Generate welcome email copy for {Business Name}.”  
     3. **Klaviyo** → **Add Subscriber** → Map fields from webhook.  
     4. **Klaviyo** → **Send Email** → Use template “Welcome”.  

10. **Save the scenario**.  
    - Click **“Save”**, name it **“Welcome Flow”**.  
    - Verify the status bar shows **“Ready”**.  

> **Do you see the scenario status as “Ready”?**  
> If it shows **“Error”**, check that the ChatGPT module has a valid API key:  
> - Go to **Make.com → My Account → API Keys** → copy your key.  
> - Re‑enter it in the ChatGPT module.  

11. **Integrate the webhook into Notion**.  
    - In Notion, open the **“Client Discovery Sheet”**.  
    - Click **“Share”** → **“Copy Link”**.  
    - In Make.com, add a **HTTP → Make a request** module after the webhook trigger.  
    - Method: **POST**  
    - URL: Notion API endpoint `https://api

---

## Procedure 3.2: Set Up Your Client Onboarding Flow in ActiveCampaign

1. **Open a browser** and navigate to the ActiveCampaign login page:  
   `https://app.activecampaign.com/login`.  
   *Enter your email and password, then click the **Login** button.*  

   **Do you see the “Dashboard” page?** If not, clear cache or try incognito mode.

2. **Create a dedicated onboarding list**.  
   - Click the **Lists** tab in the left sidebar.  
   - Press **Create List** (top right).  
   - Fill in:  
     - *List name:* `Client Onboarding`  
     - *Description:* `List for new clients signing up via the onboarding form.`  
   - Click **Save List**.  

   *Expected output:* The list appears in the list grid with 0 contacts.

3. **Build a signup form**.  
   - Click **Forms** > **Email Form** > **Create Form**.  
   - Name the form `OnboardingSignup`.  
   - In the *Form Settings* pane, select the `Client Onboarding` list for *Add to List*.  
   - Click **Save**.  

4. **Add required fields**.  
   - In the form editor, click **Add Field** > **Text**.  
     - *Label:* `First Name` (make required).  
     - *Label:* `Last Name` (make required).  
     - *Label:* `Email Address` (make required, choose *Email* type).  
   - Click **Save**.  

   **Do you see the three required fields on the preview?** If not, review the *Required* toggle.

5. **Publish the form**.  
   - In the form editor, click **Publish** > **Embed Code**.  
   - Copy the entire `<iframe>` or `<script>` snippet.  

6. **Create a new automation**.  
   - Click **Automations** > **New Automation** > **Start from Scratch**.  
   - Name it `Client Onboarding Flow`.  
   - Click **Create**.  

7. **Set the trigger**.  
   - In the automation canvas,

## Check-In: Module 3 Complete

- [ ] Draft Your AI Email Automation Service Blueprint completed and verified
- [ ] Set Up Your Client Onboarding Flow in ActiveCampaign completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 4: FIRST BUILD

## Overview  
In MODULE 4 you will **launch, manage, and scale a fully‑functional AI‑powered email marketing automation business** that leverages Klaviyo and ActiveCampaign as the core engines. You’ll learn how to ingest real client data, build a personalized email workflow, and set up automated triggers that drive revenue without manual hand‑offs. By the end of this module you’ll have a production‑ready deliverable that you can pitch to an actual client and immediately start generating recurring income. Skipping this module means you’ll never move beyond the “idea” stage; without a concrete, repeatable workflow you can’t prove value, secure contracts, or scale the operation.

The delivery you produce will be a **complete end‑to‑end email marketing system**: from data ingestion in Replit, AI‑generated copy in ChatGPT, visual assets in Canva, to scheduled sends in Klaviyo, and automated follow‑ups in ActiveCampaign. You’ll also set up a Make.com (formerly Integromat) scenario to sync data between the two platforms, ensuring your client’s contacts always stay current. This module gives you the hands‑on confidence to claim “I can automate email marketing for you” and back it up with a live, functioning prototype.

### Tool Set & Pricing Snapshot  
| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| **Klaviyo** | Email campaign creation & analytics | Unlimited emails for 500 contacts | $20/mo (500 contacts) |
| **ActiveCampaign** | Drip automation & CRM | 500 contacts, 5 automations | $35/mo (500 contacts) |
| **Make.com** | Workflow automation between Klaviyo & ActiveCampaign | 100 operations/month | $9/mo (100 ops) |
| [**Replit**](https://replit.com/refer/egwuokwor) | Code runner for data ingestion scripts | Unlimited public repls | $7/mo (Pro) |
| [**Canva**](https://www.canva.com/) | Visual asset creation | Unlimited free templates | $12/mo (Pro) |
| **ChatGPT** (OpenAI) | AI copy generation | 3,000 tokens/month | $20/mo (ChatGPT+ 1M tokens) |
| [**ElevenLabs**](https://elevenlabs.io/) | AI voice‑over for video assets | 5,000 characters/month | $10/mo (Standard) |

### Estimated Time to Complete  
- **Preparation & Tool Setup**: 1 hour  
- **Client Data Ingestion & Script Development**: 2 hours  
- **AI‑Driven Copy & Asset Creation**: 1.5 hours  
- **Workflow Configuration (Make.com, Klaviyo, ActiveCampaign)**: 2 hours  
- **Testing & QA**: 1 hour  
- **Documentation & Delivery Handoff**: 0.5 hour  

**Total: ~8 hours** (including buffer for troubleshooting).

---

## Procedure 4.1: Set Up Klaviyo Account for Client

1. **Open a web browser** (Chrome, Firefox, or Edge).  
2. Navigate to **https://www.klaviyo.com**.  
3. In the top‑right corner click **SIGN UP** (button label: **SIGN UP**).  
4. On the sign‑up page, choose **“Start for free”** and click **FREE**.  
5. Enter the client’s email address in the **Email** field (e.g., `client@example.com`).  
   - If you see a pop‑up asking for a phone number, click **SKIP**.  
   - **Check‑in**: Do you see the **Continue** button? If not, refresh the page and try again.  

6. Click **Continue**.  
7. Enter a secure password in the **Password** field (e.g., `Client$1234`).  
   - The password must be at least 8 characters, contain a number, and a special character.  
8. Check the box that says **“I agree to the Terms of Service and Privacy Policy.”**  
9. Click **Create Free Account**.  
10. Klaviyo will send a verification email to the client’s inbox.  
    - **Check‑in**: Do you see an email from Klaviyo? If not, ask the client to check spam/junk folders.  

11. Open the verification email and click **VERIFY EMAIL**.  
    - The browser should now open **https://www.klaviyo.com/app/dashboard**.  
12. The dashboard displays a welcome banner titled **“Welcome to Klaviyo”**.  
    - **Check‑in**: Do you see a **Get Started** wizard? If not, click **Dashboard** in the left sidebar.  

13. Click **Get Started**.  
14. In the wizard, choose **“I want to start from scratch”** and click **Continue**.  
15. Enter the client’s business name in the **Business Name** field (e.g., `Acme Widgets`).  
16. Select the primary industry from the dropdown (e.g., **Retail**).  
17. Click **Create Account**.  
    - Klaviyo will create a new account and redirect to the **Account Settings** page.  

18. In **Account Settings**, click **“Billing”** in the left menu.  
19. Review the current plan: it should display **“Free Plan – 500 contacts”**.  
    - **Check‑in**: Do you see the **Upgrade Plan** button? If not, scroll down.  

20. Click **Upgrade Plan**.  
21. On the pricing page, select the **Pro** tier.  
    - Pricing: **$20/month** for up to 500 contacts, **$200/month** for up to 5,000 contacts.  
    - Free tier limit: 500 contacts, 15,000 emails/month.  
22. Click **Start Free Trial** (30‑day free trial).  
23. Enter credit card details (or use a virtual card if you prefer).  
    - For a test account, use a Visa card ending in `1111`.  
24. Click **Confirm** to activate the subscription.  
    - You should see a confirmation banner: **“Your Pro plan is active. You have 30 days free.”**  
25. **Optional**: Install the Klaviyo Chrome Extension by visiting **https://chrome.google.com/webstore/detail/klaviyo** and clicking **Add to Chrome**.  
    - After installation, the extension icon appears in the browser toolbar.  

**Error Scenario**  
- **If you see “Email already in use”**:  
  - This means the email address already belongs to an existing Klaviyo account.  
  - **Fix**: Either log in with that account or use a different email address for the new client.  

**Tool Comparison Table: Klaviyo Pricing vs. Competitor (ActiveCampaign)**  

| Feature                     | Klaviyo Free | Klaviyo Pro (30‑day trial) | ActiveCampaign Free | ActiveCampaign Paid (Lite) |
|-----------------------------|--------------|----------------------------|---------------------|----------------------------|
| Contacts                    | 500          | 500 – 5,000                | 500                 | 500 – 5,000                |
| Emails per month            | 15,000       | 15,000                    | 500                 | Unlimited                  |
| Automation workflows       | 0            | 1,000 (unlimited)         | 0                   | Unlimited                  |
| AI‑powered content creation| No           | No                         | No                   | Yes (AI Writer)            |
| Pricing (monthly)           | $0           | $20 – $200                 | $0                   | $15 – $125                 |
| Free tier limits            | 500 contacts | 500 contacts (trial)      | 500 contacts         | 500 contacts               |

**Affiliate Tool Mention**  
- After setting up Klaviyo, use **Make.com** (formerly Integromat) to automate data syncs between Klaviyo and Shopify:  
  - Create a new scenario → “HTTP > Webhook” → “Shopify > New Order” → “Klaviyo > Add/Update Subscriber”.  
- Leverage **ChatGPT** (OpenAI) to generate personalized email copy for each segment; set up a Zapier integration: **Zapier > Trigger: Klaviyo > New Subscriber** → **Action: OpenAI > Complete Text** → **Action: Klaviyo > Add/Update Subscriber** with the generated content.

**End of Procedure**

---

## Procedure 4.2: Create ActiveCampaign Email Automation Funnel

1. **Open your web browser** and navigate to the ActiveCampaign sign‑up page:  
   `https://www.activecampaign.com/signup`.  
2. Click the **Sign up free** button.  
3. In the pop‑up form, enter your **First Name**, **Last Name**, and **Work Email** exactly as they appear in the fields.  
   - First Name: `John`  
   - Last Name: `Doe`  
   - Work Email: `john.doe@example.com`  
4. Click **Continue**.  
   **Do you see a pop‑up asking for your company name?** If not, refresh the page and retry.  
5. On the next page, select the **Free Trial** plan and click **Start free trial**.  
6. Complete the **Account Setup** wizard:  
   - Company Name: `Doe Enterprises`  
   - Time Zone: `America/New_York`  
   - Date Format: `MM/DD/YYYY`  
   Click **Save & Continue**.  
7. Verify your email by clicking the link sent to `john.doe@example.com`.  
   **Do you see a message that says “Your email has been verified”?** If not, check your spam folder.  
8. Log into the ActiveCampaign dashboard at `https://app.activecampaign.com`.  
9. In the top navigation bar, click **Automation**.  
   **Do you see the Automation page with the “+ New Automation” button?** If not, ensure you’re logged in.  
10. Click the **+ New Automation** button.  
    In the pop‑up, choose **Start from Scratch** and click **Continue**.  
11. Name the automation **“Welcome Series – New Subscribers”** and click **Save**.  
12. Drag the **“Add a Start Trigger”** block onto the canvas.  
    Select **“Subscribes to a list”** and click **Save**.  
13. Choose the list **“Newsletter List”** from the dropdown.  
    Click **Save**.  
14. Drag a **“Send Email”** action onto the canvas.  
    Click **Create Email**.  
15. In the email editor, click **Import** and upload a template file you created in **Canva** (PNG header, CTA button).  
    - Upload file: `welcome_header.png`  
    - Drag the PNG to the top of the email canvas.  
    Click **Save**.  
16. In the email body, click the text block and replace placeholder text with AI‑generated copy from **ChatGPT**.  
    - Prompt: “Generate a 150‑word welcome email for new newsletter subscribers.”  
    - Copy the resulting text and paste into the editor.  
17. Click **Set From Name** and enter **“Doe Enterprises”**.  
    Click **Set From Email** and enter `support@doeenterprises.com`.  
18. Click **Schedule** and set the send time to **Immediate**.  
    Click **Save & Exit**.  
    **Do you see the email scheduled for immediate delivery?** If not, check the “Schedule” tab.  
19. Drag a **“Wait”** action onto the canvas.  
    Set the wait time to **2 days**.  
20. Drag a second **“Send Email”** action.  
    - Click **Create Email**.  
    - Paste the AI‑generated “2‑day follow‑up” copy into the editor.  
    - Click **Set From Name** → `Doe Enterprises`; **Set From Email** → `support@doeenterprises.com`.  
    - Set send time to **Immediate** and click **Save & Exit**.  
    **Do you see the second email scheduled 2 days after the first?** If not, verify the wait block.  
21. Click **Save** in the top right corner.  
    **Do you see the confirmation banner “Automation saved successfully”?**  
22. **Publish** the automation by clicking the **Activate** toggle.  
    Confirm when prompted.  
    **Do you see the green “Active” status on the automation card?**  
23. Test the funnel:  
    - Go to **Contacts → Lists** and click **Add Contact**.  
    - Enter a test email `test@example.com` and subscribe to the **Newsletter List**.  
    -

---

## Procedure 4.3: TRAIN AI MODEL FOR PERSONALIZED EMAIL CONTENT

1. **Create a Replit workspace**  
   - Navigate to <https://replit.com/> and click ****Sign Up** (if not logged in).**  
   - Click ****+ Create** (top‑right).  
   - Choose **Python** as the language, name the project **EmailAI‑Trainer**, click ****Create repl**.  
   - Do you see the Replit editor with a default `main.py` file? If not, refresh the page or clear cache.

2. **Set up OpenAI API credentials**  
   - Go to <https://platform.openai.com/account/api-keys> and click ****+ Create new key**.  
   - Copy the key to the clipboard.  
   - In Replit, click the **Secrets (⚙️)** icon on the left sidebar, click ****Add a new secret**.  
   - Key: `OPENAI_API_KEY`, Value: *paste key*, click ****Add secret**.  
   - Do you see the secret listed? If not, ensure the key is copied correctly and try again.

3. **Install required Python packages**  
   - In the Replit shell (bottom pane), run:  
     ```bash
     pip install openai pandas sklearn
     ```  
   - Expected output: `Successfully installed openai pandas sklearn`.  
   - If you see `ERROR: Could not find a version that satisfies the requirement`, verify you have internet access and try again.

4. **Download sample customer data**  
   - Open a new tab, go to <https://raw.githubusercontent.com/menshly/global-data/master/email_demo.csv>.  
   - Right‑click the link and select **Save link as…**, name it `email_demo.csv`.  
   - In Replit, click ****Add file** (top of sidebar), name it `email_demo.csv`, drag the downloaded file into the editor.  
   - Do you see the CSV file listed in the file tree? If not, confirm the upload succeeded.

5. **Load and preview the data**  
   - In `main.py`, paste:  
     ```python
     import pandas as pd
     df = pd.read_csv('email_demo.csv')
     print(df.head())
     ```  
   - Run the script by clicking ****Run**.  
   - Expected output: first five rows of the dataset, including columns `customer_id`, `name`, `email`, `purchase_history`, `preferences`.  
   - If you see `FileNotFoundError`, ensure the file is named exactly `email_demo.csv`.

6. **Clean and preprocess the data**  
   - Add the following to `main.py`:  
     ```python
     df['purchase_history'] = df['purchase_history'].fillna('None')
     df['preferences'] = df['preferences'].str.lower()
     df = df.dropna(subset=['email'])
     print(df.describe())
     ```  
   - Run the script.  
   - Expected output: descriptive statistics and confirmation that no missing emails remain.  
   - If you see `KeyError: 'preferences'`, double‑check the CSV column names; adjust the script accordingly.

7. **Tokenize text for fine‑tuning**  
   - Install the `tiktoken` package:  
     ```bash
     pip install tiktoken
     ```  
   - In `main.py`, add:  
     ```python
     import tiktoken
     enc = tiktoken.encoding_for_model('gpt-3.5-turbo')
     df['tokens'] = df['preferences'].apply(lambda x: len(enc.encode(x)))
     print(df[['preferences', 'tokens']].head())
     ```  
   - Expected output: token counts for each preference string.  
   - If you see `ModuleNotFoundError: No module named 'tiktoken'`, verify the installation succeeded.

8. **Create fine‑tuning JSONL file**  
   - Convert the dataframe to the required format:  
     ```python
     with open('fine_tune.jsonl', 'w', encoding='utf-8') as f:
         for _, row in df.iterrows():
             prompt = f"Customer preferences: {row['preferences']}"
             completion = f"Personalized email subject: Boost your {row['preferences']}!"
             f.write(f'{{"prompt":"{prompt}","completion":"{completion}"}}\n')
     ```  
   - Run the script; a file named `fine_tune.jsonl` should appear in the file tree.  
   - Do you see the file? If not, check for syntax errors.

9. **Upload training file to OpenAI**  
   - In Replit, open the **Shell** and run:

## Check-In: Module 4 Complete

- [ ] Set Up Klaviyo Account for Client completed and verified
- [ ] Create ActiveCampaign Email Automation Funnel completed and verified
- [ ] TRAIN AI MODEL FOR PERSONALIZED EMAIL CONTENT completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 5: CLIENT ACQUISITION

## Overview  
In this module you will learn how to turn prospects into paying clients for your AI‑powered email marketing automation service. You’ll set up a high‑converting outreach system, build a landing page that captures intent‑driven leads, and orchestrate a lead‑generation pipeline that feeds your sales funnel. Skipping this module means you’ll spend months chasing random leads, wasting ad spend, and failing to convert even the most qualified prospects. Every step is designed to maximize ROI and ensure a steady stream of recurring revenue from the very first month of launch.

You will master the following skills:
1. Deploy a multi‑channel outreach workflow that automatically engages prospects on LinkedIn, Twitter, and email.  
2. Design a conversion‑optimized landing page that uses AI‑generated copy, dynamic pricing tables, and a clear call‑to‑action.  
3. Build a fully automated lead‑scoring system that pushes qualified contacts into Klaviyo and ActiveCampaign for nurture and closing.

**If you skip this module, you will:**
- Lose the ability to systematically identify and qualify leads.  
- Miss out on automated follow‑ups that turn cold contacts into warm prospects.  
- Incur higher CAC (Customer Acquisition Cost) because your outreach will be manual and inconsistent.

**Estimated time to complete:**  
| Stage | Time |
|-------|------|
| Research & Ideation | 1 h |
| Outreach Workflow Setup | 2 h |
| Landing Page Design & Hosting | 3 h |
| Lead‑Scoring & Integration | 2 h |
| **Total** | **8 h** |

**Required Tools**

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| Klaviyo | Email automation, segmentation, and analytics | 5 k contacts | $20 / month (5 k‑12 k contacts) |
| ActiveCampaign | Sales pipeline & CRM, email marketing | 500 contacts | $15 / month (500‑1 k contacts) |
| Make.com | Workflow automation (LinkedIn → Klaviyo → ActiveCampaign) | 1 000 operations/mo | $9 / month (5 000 operations/mo) |
| Replit | Code sandbox for custom scripts (Python, JavaScript) | Unlimited | $7 / month (Pro) |
| Canva | Landing page mockup & graphic creation | Unlimited | $12 / month (Pro) |
| ChatGPT | AI copywriting for outreach & landing page | 3 k tokens/month | $20 / month (ChatGPT‑4) |
| ElevenLabs | AI voice for video demos | 5 min / month | $15 / month (Standard) |

Follow the procedures in this module to build a repeatable, scalable client acquisition engine that delivers a predictable revenue pipeline for your AI‑powered email marketing service.

---

## Procedure 5.1: Create a Lead Magnet Landing Page with Klaviyo Sign‑Up Forms

1. **Open a web browser and navigate to the Klaviyo sign‑up page**  
   URL: `https://www.klaviyo.com/`  
   Click the **“Start free trial”** button in the top‑right corner.  
   *Expected output:* Klaviyo registration form with fields for “Email”, “Password”, and “Company name”.

2. **Fill in the registration form**  
   - Email: `yourname@yourdomain.com`  
   - Password: `StrongPass!2026` (exact 12 characters, at least one uppercase, one number, one special character)  
   - Company name: `YourAgencyName`  
   Click **“Create account”**.  
   *Expected output:* Email verification page.

3. **Verify your email**  
   Open your inbox, click the link in the “Welcome to Klaviyo” email.  
   You will be redirected to the Klaviyo dashboard at `https://www.klaviyo.com/dashboard`.  
   *Expected output:* Dashboard home with “Add List” button visible.

4. **Create a new list for the lead magnet**  
   - Click **“Add List”** (top‑right).  
   - In the modal, enter **List name**: `Lead Magnet Subscribers`.  
   - Click **“Create List”**.  
   *Interactive check‑in:* **Do you see the new list “Lead Magnet Subscribers” in the Lists panel?**  
   If not, refresh the page or log out and back in.

5. **Create a new signup form**  
   - From the dashboard, click the **“Signup Forms”** tab.  
   - Click **“Create signup form”**.  
   - Choose **“Classic Form”** and click **“Continue”**.  
   *Expected output:* Classic form editor with default fields.

6. **Configure form fields**  
   - Delete the default **“Phone”** field by clicking the trash icon.  
   - Add a **“First name”** field: click **“Add field”** → select **“First Name”** → click **“Add”**.  
   - Add a **“Last name”** field similarly.  
   - Ensure the **“Email”** field is marked **“Required”** (toggle is on).  
   *Interactive check‑in:* **Do you see the form with First Name, Last Name, and Email fields?**  
   If not, scroll to the form builder and verify fields.

7. **Set form behavior**  
   - Click the **“Form Actions”** tab.  
   - Under **“Success Message”**, type: `Thank you! Check your inbox for the free e‑Book.`  
   - Under **“Redirect URL”**, leave blank (form will stay on the page).  
   - Click **“Update”**.  
   *Expected output:* Success message preview shows.

8. **Publish the form**  
   - Click the **“Publish”** button in the top‑right.  
   - In the popup, select **“Embed a form on your website”**.  
   - Copy the **JavaScript embed code**.  
   *Interactive check‑in:* **Do you see the embed code displayed in the popup?**  
   If not, click the **“Copy”** button to view the code.

9. **Create a new landing page on Hostinger**  
   - Open a new tab and go to `https://www.hostinger.com/`.  
   - Log in or click **“Get Started Free”** → choose the **“Free Plan”** (30‑day trial).  
   - After account creation, select **“Create a Website”** → choose **“WordPress”**.  
   - Follow the wizard:  
     - Site name: `LeadMagnetSite`  
     - Domain: `leadmagnetsite.hostinger.com` (free subdomain)  
     - Click **“Finish”**.  
   *Expected output:* WordPress dashboard at `https://leadmagnetsite.hostinger.com/wp-admin`.

10. **Install the Elementor page builder**  
    - In WordPress, go to **Plugins → Add New**.  
    - Search for **“Elementor”**.  
    - Click **“Install Now”** → **“Activate”**.  
    - Go to **Pages → Add New** → title the page `Lead Magnet`.  
    - Click **“Edit with Elementor”**.  
    *Interactive check‑in:* **Do you see the Elementor editor canvas?**  
    If not, ensure Elementor is activated.

11. **Design the landing page**  
    - Drag a **“Heading”** widget to the canvas.  
      - Text: `Unlock Your Free e‑Book on AI‑



---

**Support Pollinations.AI:**

---

🌸 **Ad** 🌸
Powered by Pollinations.AI free text APIs. [Support our mission](https://pollinations.ai/redirect/kofi) to keep AI accessible for everyone.

---

## Procedure 5.2: Set Up an ActiveCampaign Outreach Email Sequence to Convert Visitors

1. **Log into ActiveCampaign**  
   - Open a browser and go to **https://app.activecampaign.com/login**.  
   - Enter your email and password, then click the **Log In** button.  
   - *Expected output*: You are taken to the ActiveCampaign dashboard with the sidebar on the left.

2. **Create a New Contact List**  
   - In the sidebar, click **Lists**.  
   - Click the **Create List** button (top‑right, **+** icon).  
   - In the **List Name** field, type **“Visitor Outreach – Week 1”**.  
   - Toggle **List Visibility** to **Public**.  
   - Click **Create List**.  
   - *Expected output*: A confirmation banner “List created” appears and the new list appears in the list table.

3. **Add a Signup Form to Capture Visitors**  
   - In the sidebar, click **Forms**.  
   - Click **Create New Form** → choose **Standard** → click **Create**.  
   - Name the form **“Visitor Opt‑In”**.  
   - Drag the **Email** field to the form canvas.  
   - Click the **Save** button.  
   - *Expected output*: Form preview with an email input and a **Submit** button.

4. **Publish the Form to a Landing Page**  
   - In the form editor, click **Publish** → **Embed** tab.  
   - Copy the embed code.  
   - **Do you see a code block labeled “Copy Embed Code”?** If not, click **Show Embed Code**.  
   - Paste the code into the header of your website’s landing page (or use a WordPress block if applicable).  
   - *Expected output*: Visitors can now see the form on your landing page.

5. **Create a Zapier Account (Free Tier)**  
   - Open a new tab and go to **https://zapier.com**.  
   - Click **Sign Up** → enter email → click **Sign Up**.  
   - *Expected output*: You are on the Zapier dashboard (Free plan: 5 Zaps, 100 tasks/month).

6. **Build a Zap to Add Form Submissions to ActiveCampaign**  
   - In Zapier, click **Make a Zap**.  
   - For the **Trigger App**, search and select **ActiveCampaign** → choose **New Form Entry**.  
   - Connect your ActiveCampaign account by clicking **Continue** → **Connect an Account** → log in with your ActiveCampaign credentials.  
   - *Expected output*: Trigger event “New Form Entry” listed.

7. **Configure the Trigger Settings**  
   - In the **Set up trigger** step, select **Form Name** → choose **“Visitor Opt‑In”**.  
   - Click **Test Trigger** → Zapier will pull a recent form entry.  
   - Click **Continue**.  
   - *Expected output*: Confirmation “Zap tested successfully”.

8. **Add an Action to Create a New Contact in ActiveCampaign**  
   - Click **+ Add Action** → search for **ActiveCampaign** → choose **Add / Update Contact**.  
   - Map the **Email** field from the trigger to the **Email** field in the action.  
   - In the **List** field, select **“Visitor Outreach – Week 1”**.  
   - Click **Continue** → **Test Action**.  
   - *Expected output*: “Contact created” message and a new contact appears in the ActiveCampaign list.

9. **Publish the Zap**  
   - Click **Turn on Zap** (toggle switch in the upper right).  
   - *Do you see the Zap status switch turned on? If not, click the toggle to activate it.*  
   - *Expected output*: Zap status shows “ON” and the next task limit is displayed.

10. **Draft Email Copy Using ChatGPT**  
    - Open **https://chat.openai.com**.  
    - Click **New Chat** → type:  
      ```
      Write a 4‑email outreach sequence for new visitors who signed up for a free trial of an AI‑powered email marketing service.  
      Tone: friendly, professional.  
      Include a call‑to‑action in each email.  
      Keep each email under 200 words.  
      ```
    - Click **Submit**.  
    - Copy the generated emails into a Notion page titled **“Visitor Outreach Sequence”**.  
    - *Expected output*: Four distinct email drafts ready for editing.

11. **Create the Email Sequence in ActiveCampaign**  
    - In ActiveCampaign, click **Campaigns** → **Create Campaign**.  
    - Choose **Automated**

---

## Procedure 5.3: Automate Lead Scoring and Follow‑Up Using Make.com and Klaviyo

1. **Open a web browser** and navigate to the Make.com login page:  
   `https://www.make.com/en/login`.  
   If you do not have an account, click the **Sign up** button in the upper‑right corner and create a free account.

2. **Create a new Scenario** by clicking the **Create new scenario** button on the dashboard.  
   In the pop‑up, search for **Klaviyo** and click the **Klaviyo** module icon.  
   The screen should display “**Choose an action**” with a list of available triggers and actions.

3. **Select the trigger** “**New or Updated Contact**”.  
   Click the **Continue** button.  
   You will be prompted to connect a Klaviyo account.  

4. **Connect a Klaviyo account**:  
   - Click **Add a new connection**.  
   - In the pop‑up, enter your Klaviyo API key (found in Klaviyo → Account Settings → API Keys).  
   - Name the connection “LeadScoringAPI” and click **Create**.  
   - The screen should now show **Connected** next to “LeadScoringAPI”.  

   **Do you see the “Connected” status?**  
   If not, double‑check that the API key is valid.  
   If you see **“Invalid API key”**, this means your key is incorrect. Fix it by generating a new key in Klaviyo and repeating step 4.

5. **Add a Filter** to the scenario:  
   - Click the **➕** icon between the trigger and the next module.  
   - Choose **Filter** → **Filter**.  
   - Set the condition: `contact.email contains @`.  
   - This ensures only valid email addresses proceed.  
   - Click **Save**.

6. **Add a “Set variable” module**:  
   - Click **➕** → **Tools** → **Set variable**.  
   - Name the variable `LeadScore`.  
   - Set the value to `0`.  
   - Click **Save**.

7. **Add a “Router”**:  
   - Click **➕** → **Tools** → **Router**.  
   - The router will split the flow into three paths: Low, Medium, High.

8. **Configure the Low path**:  
   - Click the first line of the router → **Add a new route**.  
   - Name the route “Low”.  
   - Add a filter: `LeadScore < 3`.  
   - Click **Save**.  
   - Add an **Update Contact** action in this route:  
     - Module: Klaviyo → **Update Contact**.  
     - In the **Properties** field, add `lead_score` = `Low`.  
     - Click **Continue** → **Test** → **Save**.  

   **Do you see the “Update Contact” module in the Low route?**  
   If not, ensure you are within the router and have added a new route.  
   If you see **“Update Contact” fails", this means the contact ID is missing; verify the trigger returns a `contact.id` field.

9. **Configure the Medium path**:  
   - Click the second line of the router → **Add a new route**.  
   - Name the route “Medium”.  
   - Add a filter: `LeadScore >= 3 AND LeadScore < 7`.  
   - Click **Save**.  
   - Add an **Update Contact** action:  
     - Module: Klaviyo → **Update Contact**.  
     - Set `lead_score` = `Medium`.  
     - Click **Save**.  

10. **Configure the High path**:  
    - Click the third line of the router → **Add a new route**.  
    - Name the route “High”.  
    - Add a filter: `LeadScore >= 7`.  
    - Click **Save**.  
    - Add an **Update Contact** action:  
      - Module: Klaviyo → **Update Contact**.  
      - Set `lead_score` = `High`.  
      - Click **Save**.  

    **Do you see all three routes with their respective filters?**  
    If not, double‑check

## Check-In: Module 5 Complete

- [ ] Create a Lead Magnet Landing Page with Klaviyo Sign‑Up Forms completed and verified
- [ ] Set Up an ActiveCampaign Outreach Email Sequence to Convert Visitors completed and verified
- [ ] Automate Lead Scoring and Follow‑Up Using Make.com and Klaviyo completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 6: DELIVERY

## Overview  
This module is the backbone of your AI‑powered email marketing automation service. It trains you to build a repeatable delivery pipeline that guarantees consistent value for every client, from onboarding to post‑campaign analysis. Mastering this module means you can scale your agency with confidence, knowing that each campaign follows the same high‑quality checkpoints and that communication with clients is streamlined, professional, and automated.  

Skipping MODULE 6 will leave you with a great product but unreliable delivery. Your clients will receive inconsistent reports, emails will lag behind, and you’ll spend countless hours chasing manual approvals. The result? Lost revenue, negative reviews, and a tarnished brand. By the end of this module, you’ll have fully automated workflows, checklists, and templates that let you focus on strategy rather than firefighting, ensuring every inbox gets the right message at the right time.  

| Tool           | Purpose                                                        | Free Tier                                      | Paid Tier                                                  |
|----------------|----------------------------------------------------------------|------------------------------------------------|------------------------------------------------------------|
| Klaviyo        | Email automation, segmentation, and analytics                  | 500 contacts, unlimited sends                  | $20/month for 2000 contacts, +$20 per 2000 contacts thereafter |
| ActiveCampaign | Advanced automation, CRM, and contact scoring                  | 14‑day free trial                              | $29/month (Lite) for 500 contacts, $49/month (Standard) for 500 contacts |
| Make.com       | Workflow automation, data sync, and API orchestration           | 500 operations/month, 100 MB storage           | $9/month Basic (2000 operations/month, 1 GB storage)         |
| Zapier         | Integrations and trigger‑action automation                      | 100 tasks/month, 5 apps                        | $19.99/month Starter (750 tasks, 5 apps)                    |
| Notion         | Project management, documentation, and knowledge base           | Unlimited pages, blocks, users                 | $8/month Personal Pro, $8/user/month Team                   |
| Loom           | Video client updates and quick demos                            | 25,000 minutes/month, 1 MB per video          | $12/month Pro (unlimited minutes, 4 GB storage)             |
| Canva          | Email template graphics, social assets, and branding visuals    | Unlimited designs, 5GB storage                 | $12.95/month Pro (10 TB storage, brand kit)                 |
| Grammarly      | Email copy proofreading and tone optimization                  | Basic grammar & spelling                      | $12/month Premium (advanced style checks)                   |
| ChatGPT        | Content ideation, copywriting, and data‑driven insights        | GPT‑3.5 free, 3 000 tokens/day                 | $20/month Plus (GPT‑4, priority access)                    |

**Estimated time to complete:** 4 hours (includes setting up integrations, creating templates, and running a full test campaign).

---

## Procedure 6.1: Map Your Email Delivery Pipeline Using Klaviyo and ActiveCampaign

1. **Open your web browser and navigate to** <https://www.klaviyo.com/>.  
   - Click the **“Log In”** button in the upper‑right corner.  
   - Enter your Klaviyo credentials (email: `you@email.com`, password: `YourStrongPassword123`).  
   - Click **“Sign In”**.  
   - *Expected output*: Klaviyo Dashboard with left‑hand menu showing “Dashboard”, “Lists & Segments”, “Flows”, etc.

2. **Create a new list** to house the contacts that will flow from ActiveCampaign.  
   - In left menu, click **“Lists & Segments”**.  
   - Click the **“Create List”** button.  
   - Fill in **List Name**: `AC_Generated_Contacts`.  
   - Leave [**Description**](https://www.descript.com/) blank.  
   - Click **“Create List”**.  
   - *Expected output*: Confirmation toast “List created successfully” and the list appears in the list table.

3. **Export your ActiveCampaign contact list** for mapping reference.  
   - Open a new tab, go to <https://app.activecampaign.com/>.  
   - Log in with the same credentials.  
   - In left menu, click **“Contacts”** → **“Export”**.  
   - Choose **“All Contacts”**, click **“Export”**.  
   - Wait for the CSV file to download.  
   - *Expected output*: `activecampaign_contacts_YYYYMMDD.csv` in the Downloads folder.

4. **Open Make.com** (formerly Integromat) at <https://www.make.com/>.  
   - Log in or sign up (free plan: 1,000 operations/month).  
   - In the dashboard, click **“Create a new scenario”**.  
   - Search for **“ActiveCampaign”** and **“Klaviyo”** modules.  
   - Drag the **ActiveCampaign > Watch Contacts** module onto the canvas.  
   - Click **“Add”** under “Connection” and authorize Make.com to access your ActiveCampaign account.  
   - In the module settings, set **“Limit”** to `100` and **“Filter”** to `date_added > 30 days ago`.  
   - Click **“Save”**.  
   - *Expected output*: Module icon with a green checkmark and parameters displayed.

5. **Add a Klaviyo “Add Contact” module** to the scenario.  
   - Drag the **Klaviyo > Add Contact** module next to the ActiveCampaign module.  
   - Connect it by dragging the arrow from the ActiveCampaign module to the Klaviyo module.  
   - Click **“Add”** under “Connection” to authorize Klaviyo (`API Key` from Klaviyo settings → **Account** → **API Keys**).  
   - Map fields:  
     - **Email** → `{{watch_contacts.email}}`  
     - **First Name** → `{{watch_contacts.first_name}}`  
     - **Last Name** → `{{watch_contacts.last_name}}`  
     - **List** → `AC_Generated_Contacts` (select from dropdown).  
   - Click **“Save”**.  
   - *Expected output*: Arrow labeled “OK” and mapping confirmation.

**Do you see the two modules connected with an arrow? If not, check that you dragged the arrow correctly and that both modules have a green checkmark.**

6. **Add a filter to prevent duplicate contacts**.  
   - Drag a **“Filter”** module between ActiveCampaign and Klaviyo.  
   - Set the filter condition: `{{watch_contacts.email}} != ""`.  
   - Click **“Save”**.  
   - *Expected output*: Filter icon with condition displayed.

7. **Test the scenario once** to verify data flow.  
   - Click the **“Run once”** button in the top‑right corner.  
   - When prompted, confirm the test run.  
   - Wait for the scenario to finish (usually < 30 seconds).  
   - Inspect the execution log: you should see a record of at least one contact being added to Klaviyo.  
   - *Expected output*: “Scenario executed successfully” toast and log entries showing `ActiveCampaign: 1 contact watched`, `Klaviyo: 1 contact added`.

8. **Schedule the scenario to run hourly**.  
   - Click the **“Schedule settings”** icon (clock).  
   - Set **“Run every”** to `1 hour`, start time `00:00`.  
   - Enable **“Keep scenario active”**.  
   - Click **“OK”**.  
   - *Expected output*: Scenario status shows “Active” and schedule icon displays `Hourly`.

9. **Create a Klaviyo Flow that triggers on list subscription**.  
   - Return to Klaviyo Dashboard, click **“Flows”** → **“Create Flow”**.  
   - Select **“List”** trigger.  
   - Choose the `AC_Generated_Contacts` list.  
   - Click **“Create Flow”**.  
   - In the Flow editor, drag a **“Send Email”** action onto the canvas.  
   - Click **“Create Email”** and design a welcome email using **Canva** (free plan: 5 templates/month).  
   - Save the email, set **“Send after”** to `0 days`.  
   - Click **“Activate”**.  
   - *Expected output*: Flow diagram with trigger → email action, and flow status “Active”.

10. **Verify email deliverability settings**.  
    - In Klaviyo, go to **“Account”** → **“Email Settings”**.  
    - Ensure **“From Email”** is set to `support@yourdomain.com`.  
    - Click **“Add Sender”** → enter `support@yourdomain.com` and follow the SPF/D

---

**Procedure 6.2** — Generation failed due to AI backend unavailability. Please retry later.

## Check-In: Module 6 Complete

- [ ] Map Your Email Delivery Pipeline Using Klaviyo and ActiveCampaign completed and verified
- [ ] Set Up Quality Checkpoints for AI Campaign Performance completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 7: SCALING

## Overview

Welcome to the scaling phase of your AI‑powered email marketing automation business. This module is the bridge from a solo operation to a high‑margin, multi‑contractor enterprise. You will learn how to transition ownership of repetitive tasks to vetted contractors, build Standard Operating Procedures (SOPs) that enforce consistency, and perform margin analysis that tells you exactly when a new hire is profitable. Skipping this module means you’ll remain stuck in a “busy‑work” cycle, unable to harness the full revenue potential of your AI stack. You’ll continue to pay double the cost of your own time, and your clients will see diminishing returns as your workload grows.

At its core, Module 7 equips you with the operational discipline to scale without sacrificing quality or over‑paying for talent. You’ll be taught how to:  
1. **Hire and onboard your first contractor** – from posting on marketplaces to setting up a performance review cadence.  
2. **Create SOPs that translate your workflow into a repeatable playbook** – so any new team member can hit the ground running.  
3. **Run a margin analysis** – using real data from Klaviyo, ActiveCampaign, and your billing system to decide when the incremental cost of a contractor is justified by incremental revenue.

The module is designed for completion in **3 business days**: 8 hours of focused work per day. By the end, you will own a scalable, repeatable system that turns your AI expertise into a scalable revenue engine.

| Tool           | Purpose                                                   | Free Tier                                               | Paid Tier (Monthly) |
|----------------|-----------------------------------------------------------|--------------------------------------------------------|---------------------|
| Klaviyo        | Email automation, segmentation, revenue analytics          | 500 contacts, 2,500 emails                             | $20 (Starter) – $400+ (Growth) |
| ActiveCampaign | CRM, automation, predictive sending                       | 1,000 contacts, 2,500 messages                        | $29 (Lite) – $159+ (Enterprise) |
| Make.com       | Workflow automation between Klaviyo and other apps        | 1,000 tasks, 15 min sync                               | $19 (Starter) – $299+ (Professional) |
| Zapier         | Quick integration hub (optional for small tasks)          | 5 zaps, 100 tasks per month                            | $19 (Starter) – $599+ (Team) |
| Notion         | SOP documentation, knowledge base                         | Unlimited pages, 5 collaborators                       | $8 (Personal Pro) – $15 (Team) |
| Grammarly      | Quality control for copy                                 | 10,000 characters per month, limited features         | $12 (Premium) – $30 (Business) |
| Replit         | Quick coding experiments, small scripts                   | Unlimited public projects, 500 MB storage              | $7 (Hacker) – $25 (Pro) |
| Canva          | Email template design & image creation                    | 5 team members, 30 GB storage                          | $12 (Pro) – $30 (Enterprise) |

*All prices reflect the lowest paid tier that satisfies the module’s requirements. Use the free tiers to validate the tools before committing.*

By the end of this module you will have a repeatable, data‑driven scaling process that can be duplicated for any client portfolio, turning your solo operation into a profitable, growth‑ready business.

---

## Procedure 7.1: Recruit Your First AI Email Design Contractor

1. **Open your web browser** and go to **https://chat.openai.com**.  
2. **Login** with your OpenAI credentials or click **Sign‑Up** and complete the email verification.  
3. Once inside the ChatGPT chat window, type:  
   ```
   Draft a concise, high‑impact job posting for an AI‑powered email design contractor who can create responsive templates in Canva and integrate with Klaviyo. Include required skills, deliverables, and rate expectations.  
   ```  
4. **Copy** the generated text (Ctrl +C).  
   *Do you see the job description text box filled? If not, refresh the page and try again.*  

5. Open a new tab and navigate to **https://www.upwork.com**.  
6. Click **Sign Up** (top right). Choose **I want to hire** and click **Continue**.  
7. **Enter** your email (e.g., yourbusiness@domain.com), set a password, and click **Create an account**.  
8. Verify your email by clicking the link sent to your inbox.  
   *Do you see the “Account verified” banner? If not, check spam and verify within 15 minutes.*  

9. Back in Upwork, click **Post a Job** (top bar).  
10. In the **Title** field, paste the job description title from ChatGPT.  
11. In the **Description** field, paste the full job description.  
12. Under **Project type**, select **Fixed‑price**.  
13. Set the budget to **$30–$50 per email template**.  
14. Click **Continue**.  
   *Do you see the budget preview? If not, ensure the currency is USD and re‑enter the amount.*  

15. **Click** **Set a timeline** and choose **2 weeks**.  
16. Under **Skills**, type **Canva**, **HTML/CSS**, **Email Marketing**, **Klaviyo**, and **AI Design**; click **Add** after each.  
17. Click **Continue** to the Review page.  
18. **Review** the posting for accuracy; if everything is correct, click **Post Job**.  
   *Do you see the “Job posted” confirmation screen? If not, the posting fee may be pending; check the payment section.*  

19. Open **https://www.apollo.io** in a new tab.  
20. **Login** with your Apollo credentials or click **Sign‑Up** and choose the free tier (10 000 contacts/month).  
21. In the dashboard, click **People** → **Add New Search**.  
22. Set the filter **Job Title** to **Email Designer** and **Industry** to **Marketing**.  
23. Click **Search** and then **Export** the first 50 results as CSV.  
   *Do you see the CSV file download? If not, ensure you’re not on a mobile device.*  

24. Open **https://www.canva.com**.  
25. Click **Log in** (top right) and authenticate with Google.  
26. Click **Create a design** → **Custom size** → enter **800 × 600 px** → **Create new design**.  
27. In the left panel, click **Templates** → search for **Email** → choose a free template.  
28. Replace the placeholder text with the company name **Menshly Global** and logo (upload via **Uploads**).  
29. Click **Download** (top right) → choose **PNG** → click **Download**.  
30. **Upload** the PNG to your Upwork job post by clicking **Add files** → **Upload file**.  
   *Do you see the PNG thumbnail in the job posting? If not, clear browser cache and try again.*  

31. Open **https://www.loom.com**.  
32. Click **Sign Up** → choose **Free** → verify email.  
33. Click **New Recording** → choose **Screen + Camera**.  
34. Record a 30‑second pitch: introduce yourself, the project scope, and why the contractor should apply.  
35. Click **Stop** → **Save** → **Share** → copy the share link.  
36. Return to Upwork’s job posting and paste

---

## Procedure 7.2: **Delegate Email List Segmentation**

1. **Open the Klaviyo Dashboard**  
   - URL: `https://www.klaviyo.com/login`  
   - Enter your credentials (email, password).  
   - Click **Log In** (bottom button).  
   - *Expected output:* You land on the Klaviyo “Home” page with the left‑hand menu visible.

2. **Create a New Segment**  
   - In the left‑hand menu, click **Lists & Segments** → **Segments**.  
   - On the top right, click **Create Segment** (blue button).  
   - In the “Segment Name” field, type **“High‑Engagement Leads”**.  
   - Click **Save**.  
   - *Expected output:* A new blank segment editor opens with “High‑Engagement Leads” displayed.

3. **Define Segmentation Criteria**  
   - Click **Add Condition** → **Profile Property**.  
   - Choose **“Total Email Opens”** → **Greater than** → **10**.  
   - Click **Add Condition** → **Profile Property** → **“Time on Site (minutes)”** → **Greater than** → **5**.  
   - Click **Add Condition** → **Profile Property** → **“Location”** → **In** → **“United States”**.  
   - Click **Save**.  
   - *Expected output:* The segment shows a preview of matching contacts.

4. **Export Segment for Review**  
   - In the segment editor, click **Export** → **CSV** (top right button).  
   - Choose **“Include all fields”**.  
   - Click **Export**.  
   - *Check‑in:* Do you see a download link for `High-Engagement_Leads.csv`?  
     If not, verify that you are in the correct segment and that the “Export” button is highlighted.  

5. **Upload CSV to Replit for Automated Tagging**  
   - Open your browser, go to `https://replit.com`.  
   - Log in or sign up for the free tier (free tier allows 500 MB storage, 100 MB RAM).  
   - Click **+ Create** → **New Repl** → **Python**.  
   - Name the Repl **“Klaviyo‑Tagger”**.  
   - In the file sidebar, click **Upload File** → select `High-Engagement_Leads.csv`.  
   - In `main.py`, paste the following script:

     ```python
     import csv
     import requests

     API_KEY = "YOUR_KLAVIYO_PRIVATE_API_KEY"
     LIST_ID = "YOUR_LIST_ID"

     def tag_contacts():
         with open('High-Engagement_Leads.csv', newline='') as csvfile:
             reader = csv.DictReader(csvfile)
             for row in reader:
                 email = row['email']
                 data = {
                     "profiles": [
                         {
                             "email": email,
                             "list_id": LIST_ID,
                             "tags": ["HighEngagement"]
                         }
                     ]
                 }
                 response = requests.post(
                     f"https://a.klaviyo.com/api/v1/list/{LIST_ID}/members",
                     json=data,
                     auth=(API_KEY, '')
                 )
                 print(f"{email}: {response.status_code}")

     if __name__ == "__main__":
         tag_contacts()
     ```

   - Replace `YOUR_KLAVIYO_PRIVATE_API_KEY` with your actual private API key (found in **Account Settings** → **API Keys**).  
   - Replace `YOUR_LIST_ID` with the ID of the list you want to tag (found in **Lists & Segments** → list name → **List ID** in the URL).  
   - Click **Run** (green triangle).  
   - *Expected output:* Each line prints `email@example.com: 201` indicating successful tagging.

6. **Verify Tags in Klaviyo**  
   - Return to Klaviyo dashboard.  
   - Click **Lists & Segments** → choose the list you tagged.  
   - Go to **Tag Management** → **Tags**.  
   - Search for **“HighEngagement”**.  
   - Verify that the tag count matches the number of processed emails.  
   - *Check‑in:* Do you see the tag “HighEngagement” applied to the expected number of contacts?  
     If not, re‑run the Replit script and confirm the API key and list ID are correct.

7. **Create a Corresponding ActiveCampaign Tag**  
   - Open `https://app.activecampaign.com/login`.  
   - Log in with your credentials.  
   - In the left‑hand menu, click **Contacts** → **Tags**.  
   - Click **Add Tag** (top right).  
   - Name the tag **“HighEngagement”** and click **Save**.  
   - *Expected output:* Tag appears in the list of tags.

8. **Automate Tag Sync via Zapier**  
   - Visit `https://zapier.com/app/dashboard

---

## Procedure 7.3: Compute Net Margins on Klaviyo Email Automation

1. **Open a browser and go to Klaviyo’s login page**  
   URL: `https://www.klaviyo.com/login`  
   In the **Email / Phone** field, type `your‑email@example.com`.  
   In the **Password** field, type your password.  
   Click the **Login** button (button text is **Login**).

2. **Navigate to the Revenue analytics panel**  
   From the left‑hand menu, click **Analytics** → **Revenue** → **Revenue by Campaign**.  
   In the top right corner, click the **Download CSV** icon (cloud‑download icon).  
   Confirm the download dialog by clicking **Save**.  
   The file will be saved as `klaviyo_revenue_by_campaign_YYYY-MM-DD.csv`.

3. **Close Klaviyo** (click the **X** on the browser tab).  
   Open a new tab and go to ActiveCampaign’s login page: `https://go.2cqa.com/activecampaign/login`.  
   Enter your **Username** and **Password**.  
   Click the **Log In** button.

4. **Export your email send cost data**  
   From the main menu, click **Reports** → **Email Statistics**.  
   In the upper right, click **Export** → **CSV**.  
   Confirm by clicking **Export**.  
   The file will be saved as `activecampaign_email_stats_YYYY-MM-DD.csv`.

   **Do you see the “Export” button with a CSV icon?**  
   *If not, verify you’re in the “Email Statistics” report. If still missing, clear your browser cache and reload.*

5. **Identify your current ActiveCampaign plan cost**  
   In the top right corner, click your **Profile** icon → **Account Settings**.  
   Under **Subscriptions**, note the **Plan** (e.g., “Lite”) and the **Monthly Cost** displayed (e.g., `$29.00`).  
   Write this cost in a text file named `plan_cost.txt`.

6. **Calculate per‑send cost**  
   Open a terminal or command prompt.  
   Run `python -c "import csv, sys; csvfile='activecampaign_email_stats_YYYY-MM-DD.csv'; total_sends=0; with open(csvfile, newline='') as f

## Check-In: Module 7 Complete

- [ ] Recruit Your First AI Email Design Contractor completed and verified
- [ ] **Delegate Email List Segmentation** completed and verified
- [ ] Compute Net Margins on Klaviyo Email Automation completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 8: ADVANCED PATTERNS

## Overview  
Module 8 is the capstone of the playbook, teaching you how to take an already‑running AI‑powered email marketing automation business and propel it into a scalable, high‑margin, recurring‑revenue engine. You’ll learn premium upsell strategies, create tiered productized services, and embed AI‑driven personalization at scale. By skipping this module you risk stagnation: your clients will plateau, your margins will erode, and competitors will capture the high‑ticket market.  

In this module you’ll master the art of bundling AI features—such as predictive segmentation, dynamic content generation via ChatGPT, and voice‑enabled newsletters with ElevenLabs—into irresistible high‑ticket packages. You’ll also learn how to automate upsell funnels with Klaviyo’s flow builder, set up recurring billing in ActiveCampaign, and use Make.com to sync data between platforms for real‑time analytics. The result is a repeatable, low‑manual‑touch operation that turns one‑off projects into predictable monthly revenue streams.  

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| Klaviyo | Email automation & segmentation | $0 (up to 250 contacts, 500 emails/month) | $20/month (500 contacts) |
| ActiveCampaign | CRM + email automation | $0 (5 contacts) | $29/month (500 contacts) |
| Make.com | Workflow automation | $0 (100 operations/month) | $19/month (1,000 operations) |
| ChatGPT (OpenAI) | AI content generation | $0 (free tier, 3k tokens/day) | $20/month (30k tokens/day) |
| ElevenLabs | AI voice synthesis | $0 (5 min/day) | $14/month (30 min/day) |
| Canva | Design assets for email templates | $0 (basic) | $12.99/month (Pro) |
| Notion | Project & knowledge base | $0 (personal) | $8/month (Team) |
| Zapier | Cross‑app automation | $0 (5 zaps, 100 tasks/month) | $19/month (Unlimited tasks) |

**Estimated Time to Complete:** 2–3 hours of focused work.

---

**Procedure 8.1** — Generation failed due to AI backend unavailability. Please retry later.

---

## Procedure 8.2: Package a High‑Ticket AI Email Automation Service for Enterprise Clients

1. **Create a new project in Make.com**  
   - Go to <https://www.make.com> and log in.  
   - Click the **+ New scenario** button in the top‑right corner.  
   - In the “Scenario name” field type **“Enterprise AI Email Service – 2026”** and hit **Enter**.  
   - *Expected output:* The left‑hand canvas should now display a blank scenario labeled *Enterprise AI Email Service – 2026*.  

2. **Add the Klaviyo trigger**  
   - Click the **+ Add another module** button.  
   - Search for “Klaviyo” and select the **“When a new subscriber is added”** trigger.  
   - Click **Continue** and choose the Klaviyo account you want to use.  
   - In the **List ID** field, type **“EnterpriseClients”** and click **Test**.  
   - *Expected output:* A green confirmation “Connection successful – 12 test subscribers found.”  

3. **Insert a “Filter” module to target enterprise leads**  
   - Add a **Filter** module.  
   - Set the condition: **`{{trigger.email_domain}}` contains `enterprise.com`**.  
   - Save the scenario.  

4. **Add a “HTTP request” module to call ChatGPT**  
   - Add a **HTTP** module → **Make a request**.  
   - Set **Method** to **POST**.  
   - In **URL**, enter: `https://api.openai.com/v1/chat/completions`.  
   - In **Headers**, add:  
     - Key: `Authorization` – Value: `Bearer YOUR_OPENAI_API_KEY`  
     - Key: `Content-Type` – Value: `application/json`  
   - In **Body type**, select **Raw** and choose **JSON**.  
   - Paste the following JSON, replacing `{{trigger.email}}` with the actual email field:  
     ```json
     {
       "model": "gpt-4o-mini",
       "messages": [
         {"role":"system","content":"You are a senior email marketing strategist."},
         {"role":"user","content":"Generate a personalized welcome email for a new enterprise subscriber at {{trigger.email}} who just signed up for our AI email service."}
       ],
       "max_tokens": 150
     }
     ```  
   - Click **Test**.  
   - *Expected output:* In the “Response” pane you should see a JSON block with a field `choices[0].message.content` containing the drafted email.  

5. **Check that the AI email content appears**  
   - Do you see the email body in the JSON response?  
   - If not, verify that the `YOUR_OPENAI_API_KEY` is correct and that your OpenAI account has the `gpt-4o-mini` model enabled.  

   **Interactive Check‑In**  
   *Do you see “choices[0].message.content” in the test response? If not, go back to step 4’s body JSON and correct any syntax errors.*  

6. **Create a new mail template in Klaviyo**  
   - In a new browser tab, go to <https://www.klaviyo.com> and open the **Email Templates** section.  
   - Click **+ Create Template** → **HTML Email**.  
   - In the editor title, type **“Enterprise AI Welcome”**.  
   - Paste the email body from step 5 into the HTML area.  
   - Click **Save**.  

7. **Insert a “Set variable” module in Make.com to store the email content**  
   - Add a **Set variable** module.  
   - Name the variable **`welcome_email_body`**.  
   - Set the value to `{{response.content}}` from the HTTP request.  

8. **Add an “ActiveCampaign” action to create a custom field**  
   - Add an **ActiveCampaign** module → **Create/Update Contact**.  
   - Connect your ActiveCampaign account.  
   - In the **Email** field, map `{{trigger.email}}`.  
   - In the **Custom Fields** section, add a field named **“AI_Welcome_Body”** and map it to `{{welcome_email_body}}`.  
   - Click **Test**.  
   - *Expected output:* “Contact created – ID 987654321.”  

9. **Set up a “Schedule” module to send the welcome email after 1 hour**  
   - Add a **Schedule** module → **Delay**.  
   -

## Check-In: Module 8 Complete

- [ ] Design a Tiered Subscription Model for Continuous AI Email Service completed and verified
- [ ] Package a High‑Ticket AI Email Automation Service for Enterprise Clients completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 9: FINANCIAL OPERATIONS

## Overview  
Module 9 is the financial backbone of your AI‑powered email marketing agency. It teaches you how to capture every dollar, scale price points, and protect your margins with professional contract templates. Skipping this module means you’ll launch with an invisible revenue leak—improper tracking leads to missed upsells, pricing that undercuts competitors, and a lack of evidence‑based decision making. In the fast‑moving world of AI‑driven campaigns, you can’t afford to be playing guess‑work; you need a live dashboard that shows real‑time Gross Profit, CAC, LTV, and churn. This module equips you with a fully‑functional financial stack, so you can negotiate from data, push price adjustments confidently, and present polished proposals that close deals quickly.

The procedures that follow will guide you through setting up a revenue‑tracking spreadsheet in Notion, automating invoice issuance with Make.com and Zapier, and building dynamic contract templates in Canva powered by ChatGPT. You’ll also learn how to embed AI‑generated pricing models into your Klaviyo/ActiveCampaign flows and generate custom dashboards that feed directly into your Stripe and QuickBooks accounts. At the end of this module, you’ll own a single, interactive dashboard that updates every minute, a library of proposal templates that auto‑populate client data, and a contract generator that enforces your new pricing tiers.

| Tool | Purpose | Free Tier | Paid Tier |
|------|---------|-----------|-----------|
| [**Notion**](https://notion.so/) | Centralized financial database & dashboard | Unlimited pages, 5 MB file uploads | Personal Pro: $8 / month (pro 1‑user) |
| **Klaviyo** | Email automation & revenue attribution | 2 000 contacts, 500 email sends | Growth: $20 / month + $0.08 / email |
| **ActiveCampaign** | CRM & advanced automation | 500 contacts, 3 days email history | Lite: $15 / month |
| **Make.com** | Multi‑app workflow automation | 1 000 operations/month | Starter: $9 / month |
| **Zapier** | App‑to‑app connectors | 100 tasks/month | Starter: $19.99 / month |
| **QuickBooks Online** | Accounting & invoicing | 250 transactions/month | Simple Start: $25 / month |
| **Canva** | Proposal & contract design | Unlimited designs, 5 GB storage | Pro: $12.99 / month |
| **ChatGPT** | AI content for proposals & contracts | 3 k tokens/month | Plus: $20 / month |
| **Stripe** | Payment collection & reporting | Unlimited transactions | Standard: 2.9 % + $0.30/transaction |

**Estimated time to complete Module 9:** 3 hours (including setup, testing, and template finalization).

---

## Procedure 9.1: Set Up Revenue Tracking in Klaviyo

1. **Open a web browser and go to** `https://www.klaviyo.com/`.  
   *Login with your email and password. If you do not have an account, click **Sign up** in the top‑right corner and follow the on‑screen wizard.*

2. **Navigate to the dashboard.**  
   Click **Account** in the top‑right corner and select **Account Settings** from the dropdown.  
   *Expected output:* You should see the “Account Settings” page with tabs: Profile, Billing, API Keys, Integrations.

3. **Create an API Key.**  
   - In the **API Keys** tab, click **Create API Key**.  
   - Enter a name “Revenue‑Tracking‑Key” and click **Create**.  
   - Copy the generated key into a secure location (e.g., a Notion page).  
   *Do you see the “API Key created” confirmation? If not, verify that you are in the correct tab and that your account has admin privileges.*

4. **Open the Klaviyo Integrations page.**  
   Click **Integrations** in the left‑hand menu, then select **All Integrations**.  
   *Expected output:* A grid of available integrations, including “Shopify”, “WooCommerce”, “Stripe”, etc.  
   **Check‑in:** Do you see the “Shopify” integration? If not, scroll down or use the search bar.

5. **Add the Shopify integration.**  
   - Click **Shopify** → **Connect**.  
   - A modal appears: select **My Shopify Store** (or paste your store URL) and click **Continue**.  
   - In the Shopify admin page that opens, click **Install app**.  
   - Back in Klaviyo, click **Grant Access**.  
   *Expected output:* “Shopify store connected” banner at the top of the Integrations page.

6. **Configure Revenue Tracking.**  
   - In the Integrations page, find the newly connected Shopify integration and click **Configure**.  
   - Under **Revenue Settings**, click the toggle to **Enable Order Tracking**.  
   - Set **Order Import Frequency** to **Every 15 minutes**.  
   - Click **Save**.  
   *Do you see the green “Settings saved” banner? If not, ensure the toggle is on and the frequency is a valid value.*

7. **Verify that revenue data is being imported.**  
   - Go to **Analytics** → **Dashboard**.  
   - In the top‑right, click **+ Add Report** → **Revenue**.  
   - Select **Shopify Orders** as the source and click **Create**.  
   *Expected output:* A revenue chart appears with recent order totals.  
   **Check‑in:** Do you see at least one order plotted? If not, wait 15‑20 minutes for the first sync.

8. **Create a revenue‑based list segment.**  
   - In the left‑hand menu, click **Lists & Segments** → **Create List / Segment** → **Segment**.  
   - Name the segment “High‑Value Customers”.  
   - Under **Define Conditions**, choose **Revenue** → **Total Revenue** → **Greater than** → **$500**.  
   - Click **Create Segment**.  
   *Expected output:* “Segment created” banner and the segment appears in the list.

9. **Set up a revenue‑triggered flow.**  
   - Go to **Flows** → **Create Flow** → **Trigger‑Based**.  
   - Name the flow “Order Confirmation + Upsell”.  
   - Click **Trigger** → **Shopify Order** → **Placed**.  
   - Drag an **Email** node onto the canvas and click **Create Email**.  
   - In the email editor, click **Add Dynamic Content** → **Revenue** → **Total Order Value**.  
   - Click **Save** → **Activate**.  
   *Do you see the flow graph with an email node? If not, ensure the trigger is set to Shopify Order Placed.*

10. **Test the revenue tracking.**  
    - In Shopify, create a dummy order of $120.  
    - Wait 15 minutes for Klaviyo to sync.  
    - In Klaviyo, go to **Analytics** → **Dashboard** and confirm the order appears.  
    - In the **Flows** page, verify the “Order Confirmation + Upsell” flow fired for the test email.  
    *Expected output:* The flow status shows “Sent” for the test email with the correct order amount displayed.

11. **Create a revenue report in Klaviyo.**  
    - Navigate to **Analytics** → **Reports** → **

---

## Procedure 9.2: Generate Tiered Pricing Proposal Templates for ActiveCampaign

1. **Open your web browser and navigate to https://www.notion.so.**  
   - Log in with your credentials.  
   - In the left‑hand sidebar, click **Create new page** (icon: **+**).  
   - Title the page **“ActiveCampaign Tiered Pricing Proposal – [Client Name]”** and set the visibility to **Private**.

2. **Create a pricing table in Notion.**  
   - In the page, type `/table – inline` and press **Enter**.  
   - In the table, rename the first column header to **Tier**.  
   - Add four columns: **Contacts**, **Features**, **Price (USD)**, **Notes**.  
   - Insert three rows for the tiers: **Basic**, **Pro**, **Enterprise**.

3. **Populate the table with baseline data.**  
   - **Tier**: “Basic”; **Contacts**: “Up to 1,000”; **Features**: “Standard Template, 10 automation workflows, 24/7 support”; **Price (USD)**: “$49/month”; **Notes**: “Includes 5% discount for annual billing”.  
   - **Tier**: “Pro”; **Contacts**: “1,001–5,000”; **Features**: “All Basic features + Advanced segmentation, 50 automation workflows, priority support”; **Price (USD)**: “$199/month”; **Notes**: “Includes 10% discount for annual billing”.  
   - **Tier**: “Enterprise”; **Contacts**: “5,001+”; **Features**: “All Pro features + Dedicated account manager, unlimited workflows, custom integrations”; **Price (USD)**: “$499/month”; **Notes**: “Custom quote required for high‑volume clients”.

4. **Do you see the table with the three tiers correctly entered?**  
   - If the table is missing any column or row, delete and re‑create it using the same steps.  
   - Expected output: a 5‑column table with three fully populated rows in Notion.

5. **Generate the tier description text using ChatGPT.**  
   - Open https://chat.openai.com and log in.  
   - Copy the following prompt into the chat:  
     ```
     Draft a concise, persuasive description for each pricing tier (Basic, Pro, Enterprise) for an ActiveCampaign email automation service. Include benefits, key features, and a call to action. Use a professional tone suitable for a B2B client.  
     ```
   - Copy the resulting text and paste each description into the **Notes** column of the corresponding tier row in Notion.

6. **Create a header image with Canva.**  
   - Visit https://www.canva.com and log in.  
   - Click **Create a design** → **Custom size** → enter **1200 x 400 px**.  
   - Choose a background color (#1A73E8) and add a text box with the title “ActiveCampaign Tiered Pricing Proposal”.  
   - Download the image as **PNG** and save it to your local drive.

7. **Insert the header image

## Check-In: Module 9 Complete

- [ ] Set Up Revenue Tracking in Klaviyo completed and verified
- [ ] Generate Tiered Pricing Proposal Templates for ActiveCampaign completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# MODULE 10: LAUNCH PLAN

## Overview  
Module 10 is the definitive roadmap that takes you from zero to your first paying client in exactly 30 days. It delivers a day‑by‑day execution calendar, pre‑built AI‑powered email templates, and step‑by‑step integration playbooks that lock in Klaviyo and ActiveCampaign as the core engines of your service. By following this module you will have a repeatable, scalable launch process that eliminates guesswork, guarantees deliverables, and ensures you can start billing immediately after month one.

Skipping this module leaves you stranded in the “idea” phase: you’ll spend endless hours tinkering with APIs, building custom scripts, and guessing which automation will convert. Without the structured calendar, you’ll miss critical milestones—such as the first outreach email, the first demo, and the first paid pilot—leading to lost momentum, frustrated prospects, and ultimately a stagnant business. The precision of this playbook turns the chaotic launch phase into a predictable, repeatable operation that any solo entrepreneur can execute with confidence.

| Tool          | Purpose                                 | Free Tier (limits)                                     | Paid Tier (starting price) |
|---------------|-----------------------------------------|--------------------------------------------------------|-----------------------------|
| Klaviyo       | Email marketing automation & analytics | 250 contacts, 500 sends/month                          | $20 / month (Starter)      |
| ActiveCampaign| CRM + email automation                  | 500 contacts, 3 k emails/month                         | $29 / month (Lite)          |
| Make.com      | Integration & workflow automation       | 1 000 operations/month, 100 GB data transfer          | $9 / month (Basic)          |
| Zapier        | Automation & app connectivity           | 100 tasks/month, 5 Zaps                                | $19.99 / month (Starter)    |
| Canva         | Graphic & email design                  | Unlimited free templates, limited brand kits           | $12.99 / month (Pro)        |
| ChatGPT       | AI content creation & copywriting       | 3 k tokens per 3 months                                 | $20 / month (Plus)          |
| ElevenLabs    | Text‑to‑speech conversion              | 1 000 characters/day, 5 k characters/month            | $10 / month (Starter)       |
| Midjourney    | AI image generation                     | 200 free credits per month                             | $10 / month (Basic)         |
| Notion        | Project management & documentation      | Unlimited pages, 5 GB file uploads                     | $8 / month (Personal Pro)   |
| Calendly      | Appointment scheduling                  | 1 calendar, unlimited meetings, basic integrations     | $12 / month (Premium)       |

**Estimated time to complete Module 10:** 30 days of daily execution, ~4 hours per day (≈120 hours total).

---

## Procedure 10.1: Set Up Your Klaviyo Account and Initial Campaign Templates

1. **Open a Web Browser**  
   Launch Chrome, Firefox, or Edge.  
   Navigate to **https://www.klaviyo.com/**.  
   *Expected output*: Klaviyo homepage with a blue “Sign up for free” button.

2. **Create a New Klaviyo Account**  
   Click the **bold “Sign up for free”** button.  
   In the modal that appears, fill in the following fields:  
   - **First name**: *Your first name*  
   - **Last name**: *Your last name*  
   - **Email address**: *Your business email*  
   - **Password**: *Strong password (≥12 characters, mix of letters, numbers, symbols)*  
   Click **bold “Continue”**.  
   *Expected output*: A verification email sent to your inbox.

3. **Verify Your Email**  
   Open your email client, locate the Klaviyo verification email, and click **bold “Verify Email”**.  
   *Expected output*: Browser redirects to **https://www.klaviyo.com/dashboard** displaying a green “Verified” badge on your profile.

4. **Add Your First List**  
   In Klaviyo, click **bold “Lists & Segments”** in the left navigation.  
   Click **bold “Create List”**.  
   - **List name**: “Starter Subscribers”  
   - **Description**: “Initial list for AI email service clients”  
   Click **bold “Save”**.  
   *Expected output*: New list appears in the Lists & Segments table with a fresh row.  
   **Do you see the "Starter Subscribers" list?**  
   *If not, check that you are on the Lists & Segments page and that the list name is unique.*  

5. **Import Contacts from a CSV (Optional)**  
   If you have a CSV, click **bold “Import”** next to the list name.  
   Drag and drop your file or click **bold “Choose File”** and select **customers.csv**.  
   Map the columns:  
   - **Email** → **Email Address**  
   - **First Name** → **First Name**  
   - **Last Name** → **Last Name**  
   Click **bold “Continue”**, review the preview, then click **bold “Import Contacts”**.  
   *Expected output*: Import progress bar reaches 100% and a success toast appears.

6. **Set Up a Klaviyo API Key**  
   In the top right, click your profile icon → **bold “Account”**.  
   Go to **API Keys** tab.  
   Click **bold “Create API Key”**.  
   - **Key name**: “Core Automation Key”  
   Click **bold “Create”**.  
   Copy the key to your clipboard.  
   *Expected output*: Key appears in the list with a green “Active” status.  

7. **Connect Klaviyo to Shopify (Optional)**  
   Open a new tab and go to **https://zapier.com/app/editor**.  
   Sign in with your Zapier account or click **bold “Sign up for free”** if new.  
   Click **bold “Make a Zap”**.  
   Search for “Shopify” in the trigger app dropdown and select **Shopify** → **New Order**.  
   Connect your Shopify store by pasting the store URL and API credentials.  
   Set “Only new orders” as the trigger event.  
   In the action step, search for “Klaviyo” and choose **Klaviyo** → **Create/Update Subscriber**.  
   Map the Shopify order fields to Klaviyo subscriber fields.  
   Test the Zap and click **bold “Turn on Zap”**

---

## Procedure 10.2: DEPLOY AN ACTIVECAMPAIGN AUTOMATION FUNNEL FOR A LEAD MAGNET

1. **Open your browser and navigate to** `https://www.activecampaign.com/login`.  
   - If you do not have an account, click **Bold**“Sign Up Free”‑button, select the **Basic** plan (free tier: 100 contacts, 1 automation).  
   - Fill in your email, password, and company name. Click **Bold**“Create Account”.  
   - Expected outcome: You are taken to the ActiveCampaign Dashboard home screen with the “Contacts” menu on the left.

2. **Create a new list** for the lead magnet.  
   - In the left sidebar, click **Bold**“Contacts” → **Bold**“Lists & Tags”.  
   - Click **Bold**“Add List” at the top right.  
   - Enter `Lead Magnet List` in the “Name” field, `leads@example.com` in “Email Address (From)”.  
   - Click **Bold**“Save”.  
   - Expected outcome: The list appears in the list table with 0 contacts.

3. **Create a new email template** to deliver the lead magnet.  
   - Click **Bold**“Campaigns” → **Bold**“Email Templates”.  
   - Click **Bold**“Create Template”.  
   - Choose the **Basic HTML** option, click **Bold**“Next”.  
   - In the editor, paste the following minimal HTML:

     ```html
     <h1>Thank you for signing up!</h1>
     <p>Below is your free e‑book: <a href="https://example.com/ebook.pdf">Download PDF</a></p>
     ```

   - Click **Bold**“Save & Exit”.  
   - Expected outcome: Template named “Lead Magnet Email” appears in the list.

4. **Set up a landing page** that collects email addresses.  
   - Click **Bold**“Marketing” → **Bold**“Landing Pages”.  
   - Click **Bold**“Create Landing Page”.  
   - Select the **Lead Capture** template.  
   - In the editor, replace the headline with “Get Your Free e‑Book Now”.  
   - Under **Form** → **Edit Form**, add a field “Email” (required).  
   - Click **Bold**“Publish” at the top right.  
   - *Do you see the published URL? If not, check that the page status says “Published” and refresh the page.*

5. **Create a new automation** that sends the lead magnet email.  
   - Click **Bold**“Automations” → **Bold**“Automations”.  
   - Click **Bold**“Create an Automation”.  
   - Choose the **“When a contact subscribes to a list”** trigger.  
   - Click **Bold**“Choose a list” → select `Lead Magnet List`.  
   - Click **Bold**“Continue”.  

6. **Add a “Send Email” action**.  
   - In the automation canvas, click the **+** icon, then choose **Bold**“Send Email”.  
   - Select the template you created earlier, “Lead Magnet Email”.  
   - Click **Bold**“Save & Exit”.  

7. **Add a “Delay” step** to give time for the email to be read.  
   - Click the **+** icon after the email step, choose **Bold**“Delay”.  
   - Set the delay to **1 day**.  
   - Click **Bold**“Save & Exit”.  

8. **Add a “Send Email” step for a follow‑up**.  
   - Click the **+** icon, choose **Bold**“Send Email”.  
   - Create a new email: “Follow‑up: Did you find the e‑book useful?” with a short CTA to book a call.  
   - Click **Bold**“Save & Exit”.  

9. **Publish the automation**.  
   - Click **Bold**“Publish” at the top right of the canvas.  
   - You will see a confirmation banner: “Automation published successfully”.  
   - *Do you see the banner? If not, ensure all steps are completed and click “Publish” again.*

10. **Export the landing page URL** and copy it for distribution.  
    - In the landing page editor, click **Bold**“Share” → **Bold**“Copy URL”.  
    - Store this URL in a Notion page for future use.  

11. **Set up a Make.com scenario to log new subscribers into a Google Sheet** (optional but recommended for reporting).  
    - Visit `https://www.make.com/` and log in.  
    - Click **Bold**“Create a new scenario”.  
    - Search for “ActiveCampaign” → add “New Subscriber” trigger.  
    - Connect your ActiveCampaign account using the API key found in **Bold**“Settings” → **Bold**“Developer API” (copy the key).  
    - Add a “Google Sheets” module → “Add a row”.  
    - Map the subscriber email to the “Email” column.  
    - Click **Bold**“Save” → **Bold**“Run once” to test.  
    - Expected output: A new row appears in the Google Sheet with the email address.  

12. **



---

**Support Pollinations.AI:**

---

🌸 **Ad** 🌸
Powered by Pollinations.AI free text APIs. [Support our mission](https://pollinations.ai/redirect/kofi) to keep AI accessible for everyone.

---

## Procedure 10.3: Pitch Your AI‑Powered Email Service to Targeted SMBs

1. **Open Apollo.io** → Navigate to https://www.apollo.io.  
   - Click **“Create a List”** (top‑right).  
   - Name the list **“SMB Target Pitch”**.  
   - Under **“Filters”**, set:  
     - **Industry** = “Retail, E‑Commerce, Hospitality”  
     - **Company Size** = “5‑50 employees”  
     - **Location** = “United States”  
   - Click **“Save List”** (green button).  
   - Expected result: List appears in the left‑hand sidebar with 230 contacts.

2. **Export the list** → Hover over the list name, click the three‑dot menu, then **“Export CSV”**.  
   - Save the file to **C:\Pitch\SMB_Targets.csv**.

3. **Open Notion** → Go to https://www.notion.so.  
   - Create a new page titled **“Pitch Deck – AI Email Service”**.  
   - Insert a **“Table – Inline”** block; add columns: **Company, Contact, Email, Pitch Status**.  
   - Import the CSV by selecting **“Import” → “CSV”** and mapping columns accordingly.  
   - Expected output: 230 rows populated with company, contact, email, and empty status.

4. **Create a Canva template** → Visit https://www.canva.com.  
   - Click **“Create a design”** → **“Presentation (16:9)”**.  
   - Choose the template **“Professional Pitch Deck”**.  
   - Replace placeholder text with:  
     - Slide 1: **“AI‑Powered Email Automation for SMBs”**  
     - Slide 2: **“Why SMBs Need AI”** – list 3 pain points.  
     - Slide 3: **“Our Solution”** – bullet points on Klaviyo + ActiveCampaign integration.  
   - Save the deck as **“Pitch_Deck.pdf”** in the same folder.  
   - **Do you see the modified slides?** If not, refresh Canva or re‑upload the PDF.

5. **Record a short explainer video** → Open Fliki AI (https://fliki.ai).  
   - Click **“New Video”** → Upload the **Pitch_Deck.pdf**.  
   - Select the **“English – Male”** voice, speed 1.0.  
   - Click **“Generate”**.  
   - Download the MP4 to **C:\Pitch\Pitch_Explainer.mp4**.  
   - Expected outcome: 2‑minute video covering key benefits.

6. **Upload the video to Loom** → Go to https://www.loom.com.  
   - Click **“New Recording”** → **“Screen + Cam”**.  
   - Play the video during recording, then click **“Stop”**.  
   - In the title field, enter **“AI Email Pitch – SMBs”**.  
   - Click **“Save & Share”** → copy the share link.  
   - Paste the link into the **“Pitch Deck”** Notion page under a new block titled **“Pitch Video”**.  
   - **Do you see the Loom link?** If not, ensure Loom is logged in.

7. **Draft a personalized email template** → Open Mailchimp (free tier).  
   - Navigate to **https://mailchimp.com** → **“Campaigns”** → **“Create Campaign”** → **“Email”**.  
   - Choose **“Plain‑text”**.  
   - In the subject line field, type **“Boost Your Email ROI with AI – Quick Demo”**.  
   - Body:  
     ```
     Hi [[First Name]],

     I noticed that {{Company}} could benefit from AI‑driven email automation. Our solution, built on Klaviyo and ActiveCampaign, delivers:
     - 30% higher open rates
     - 25% lift in conversions
     - Automated personalization in real‑time

     Would you like a 15‑minute demo? Click here: https://calendly.com/yourname/demo
     ```
   - Click **“Save”** (blue button).  
   - Expected result: Campaign appears in “Drafts”.

8. **Integrate Calendly** → Visit https://calendly.com.  
   - Click **“Create Event Type”** → **“One‑to‑One”**.  
   - Set duration **15 minutes**, location **“Zoom”** (or “Google Meet”), buffer 10 min.  
   - Enable **“Invitee can add to calendar”**.  
   - Click **“Save & Publish”** → copy the event link.  
   - Paste into the email template above.  
   - **Do you see the Calendly link?** If not, check the “Share” tab.

9. **Use Make.com to automate email sending** → Go to https://www.make.com.  
   - Click **“Create a new scenario”** → Add **“CSV File”** (trigger) → set path **C:\Pitch\SMB_Targets.csv**.  
   - Add **“Mailchimp”** (action) → “Add/Update Subscriber”.  
   - Map fields:  
     - *Email* → **email**  
     - *First Name* → **first_name**  
     - *Last Name* → **last_name**  
   - Add **“Mailchimp”** → “Send Campaign” → choose the draft created earlier.  
   - Click **“Save”**

## Check-In: Module 10 Complete

- [ ] Set Up Your Klaviyo Account and Initial Campaign Templates completed and verified
- [ ] DEPLOY AN ACTIVECAMPAIGN AUTOMATION FUNNEL FOR A LEAD MAGNET completed and verified
- [ ] Pitch Your AI‑Powered Email Service to Targeted SMBs completed and verified
- [ ] All tools connected and working
- [ ] No errors or warnings in any dashboard


---

# APPENDIX A: COMPLETE TOOL REFERENCE  

| Tool | Purpose | Free Tier | Paid Tier | When to Upgrade |
|------|---------|-----------|-----------|-----------------|
| **Hostinger** | Domain registration & DNS hosting | None (pay‑as‑you‑go) | Domain $6.99/year, 1‑year hosting $3.99/month | When you need a dedicated domain for brand identity and email deliverability |
| **Klaviyo** | Email marketing automation & analytics | 250 contacts, 500 emails/month | Starter (500 contacts) $20/month, Growth (1,000 contacts) $30/month | Exceed 250 contacts or 500 emails/month; need dedicated support |
| **ActiveCampaign** | CRM + marketing automation | 14‑day free trial | Lite $15/month (1,000 contacts), Plus $30/month (1,000 contacts), Professional $60/month (1,000 contacts) | Pass 1,000 contacts or need advanced automation features |
| **Make.com (Integromat)** | Low‑code integration & workflow automation | 200 operations/month | 1,000 operations $9/month, 5,000 operations $39/month | Reach 200 ops/month or need more parallel scenarios |
| **Zapier** | App‑to‑app automation | 100 tasks/month | 2,000 tasks $19/month, 3,000 tasks $49/month | Cross‑platform sync beyond 100 tasks/month |
| **Apollo.io** | Lead sourcing & email outreach | 100 credits/month | 500 credits $99/month, 2,000 credits $199/month | Need bulk outreach or advanced filters |
| **PhantomBuster** | Social media & web data extraction | 200 requests/month | 2,500 requests $49/month, 10,000 requests $149/month | More than 200 requests or larger datasets |
| **Buffer** | Social media scheduling | 3 accounts, 10 posts per account | Pro $15/month (10 accounts, 100 posts) | Need more accounts or higher post limits |
| **Loom** | Video recording & sharing | 25 minutes/upload | Pro $12/month (unlimited uploads) | Need longer videos or team collaboration |
| **Calendly** | Appointment scheduling | 1 calendar, 1 user | Premium $12/month (4 calendars, 3 users) | Need multiple calendars or team scheduling |
| [**Beehiiv**](https://beehiiv.com/) | Newsletter hosting & analytics | 2,000 subscribers | Pro $19/month (unlimited) | Exceed 2,000 subscribers or need advanced segmentation |
| **Notion** | Knowledge base & project tracking | Unlimited pages | Personal Pro $8/month (single user) | Need team collaboration or advanced permissions |
| **Midjourney** | AI image generation | 25 free invites | Standard $10/month (60 invites) | Need more images or higher resolution |
| [**Grammarly**](https://grammarly.com/) | Writing assistance & style checks | Free | Premium $12/month (single user) | Need advanced tone detection, plagiarism check |
| **ChatGPT** | Conversational AI & copywriting | Free | Plus $20/month (priority access) | Need higher usage limits or priority |
| **ElevenLabs** | Text‑to‑speech voice synthesis | 10 hours/month | $20/month (10,000 words) | Need more hours or higher quality voices |
| [**Fliki AI**](https://fliki.ai?referral=noah-wilson-w84be4) | AI video creation from text | 30 minutes/month | $9/month (1,500 minutes) | Need longer videos or higher resolution |
| **Canva** | Graphic design & email templates | Free | Pro $12/month (single user) | Need brand kit, premium assets, or team collaboration |
| **Replit** | Code hosting & AI development | Unlimited public repos | Hacker $7/month (private repos, 1 GB RAM) | Need private repos or more compute |
| [**Vapi**](https://vapi.ai/) | Voice‑enabled contact center | 5 calls/month | $15/month (1,000 calls) | Need more calls or advanced IVR scripting |

---

### Tool‑Specific Quick‑Start Notes

1. **Hostinger Domain Setup**  
   - Go to **hostinger.com

# APPENDIX B: THE COMPLETE SOP INDEX  

The following index is the master reference for every Standard Operating Procedure (SOP) in this playbook.  Each row is a *single, atomic* action that the operator must complete before moving to the next entry.  The columns are defined as follows:  

- **SOP #** – Sequential identifier used throughout the playbook.  
- **Procedure** – Exact title of the SOP, matching the module heading.  
- **Category** – High‑level grouping that maps to the ten modules.  
- **Difficulty** – Skill tier required (Easy, Medium, Hard, Expert).  
- **Est. Time** – Rough duration for a seasoned operator; includes all clicks, data entry, and brief verification steps.  

Use this table as a checklist.  Cross‑reference the module overview to understand context, then execute each SOP in order.  When you finish a module, you should have a fully operational foundation before launching the next phase.

| SOP # | Procedure | Category | Difficulty | Est. Time |
|-------|-----------|----------|------------|-----------|
| 1.1 | REGISTER YOUR BUSINESS DOMAIN ON HOSTINGER | FOUNDATION | Easy | 15 min |
| 1.2 | Configure Email Forwarding in Hostinger for Client Communication | FOUNDATION | Easy | 10 min |
| 1.3 | CREATE A KLAVIYO ACCOUNT AND CONNECT YOUR DOMAIN FOR EMAIL DELIVERABILITY | FOUNDATION | Medium | 30 min |
| 2.1 | Configure Klaviyo API Credentials for Automated Segmentation | TECH STACK | Medium | 20 min |
| 2.2 | Set Up ActiveCampaign to Zapier Integration for Lead Capture | TECH STACK | Medium | 25 min |
| 2.3 | Verify Data Flow Between Klaviyo and ActiveCampaign via Webhooks | TECH STACK | Hard | 45 min |
| 3.1 | Draft Your AI Email Automation Service Blueprint | FRAMEWORK | Hard | 2 hrs |
| 3.2 | Set Up Your Client Onboarding Flow in ActiveCampaign | FRAMEWORK | Medium | 1 hr |
| 4.1 | Set Up Klaviyo Account for Client | FIRST BUILD | Medium | 30 min |
| 4.2 | Create ActiveCampaign Email Automation Funnel | FIRST BUILD | Medium | 1 hr |
| 4.3 | TRAIN AI MODEL FOR PERSONALIZED EMAIL CONTENT | FIRST BUILD | Hard | 3 hrs |
| 5.1 | Create a Lead Magnet Landing Page with Klaviyo Sign‑Up Forms | CLIENT ACQUISITION | Medium | 1 hr |
| 5.2 | Set Up an ActiveCampaign Outreach Email Sequence to Convert Visitors | CLIENT ACQUISITION | Medium | 1 hr |
| 5.3 | Automate Lead Scoring and Follow‑Up Using Make.com and Klaviyo | CLIENT ACQUISITION | Hard | 2 hrs |
| 6.1

# APPENDIX C: THE REVENUE CALCULATOR  

---

## 1.  Purpose & Assumptions  

The Revenue Calculator is the *single source of truth* you will use to validate every growth hypothesis, pricing decision, and capital allocation. It forces you to:
- Quantify **exact revenue** per client and per month.  
- Map **fixed vs. variable expenses** (hosting, SaaS, contractor wages).  
- Compute **gross margin** and **net profit**.  
- Identify the **break‑even point** for the initial $5,000 investment (domain, tooling, initial marketing).  

**Assumptions** – keep these locked unless you deliberately change them:  

| Variable | Value | Notes |
|----------|-------|-------|
| **Client Acquisition Rate** | 5 new clients per month | Linear growth until Month 12 |
| **Average Monthly Revenue per Client** | $1,200 | Includes basic Klaviyo + ActiveCampaign setup + ongoing AI content generation |
| **Fixed Monthly Expenses** | $1,200 | Hostinger domain renewal ($10 / yr), Klaviyo Starter ($20 / mo), ActiveCampaign Starter ($29 / mo), Zapier Free ($0) |
| **Variable Expense per Client** | $200 | AI model training (ElevenLabs text‑to‑speech + Fliki AI video), Contractor pay (Midjourney illustration + Canva branding) |
| **Initial Investment** | $5,000 | Domain, initial marketing (Apollo.io outreach), first‑month contractor fees |
| **Tax & Accounting Fees** | 0% | Not included in this model; add later if needed |

---

## 2.  Revenue Projections Table  

| Month | Clients | Revenue | Fixed Expenses | Variable Expenses | Total Expenses | Profit | Margin % |
|-------|---------|---------|----------------|-------------------|----------------|--------|----------|
| 1 | 5 | $6,000 | $1,200 | $1,000 | $2,200 | $3,800 | 63.3% |
| 3 | 15 | $18,000 | $1,200 | $3,000 | $4,200 | $13,800 | 76.7% |
| 6 | 30 | $36,000 | $1,200 | $6,000 | $7,200 | $28,800 | 80.0% |
| 12 | 60 | $72,000 | $1,200 | $12,000 | $13,200 | $58,800 | 81.7% |

**How to fill the table:**  

1. **Clients** – start at 5, add 5 each month.  
2. **Revenue** – `Clients × $1,200`.  
3. **Variable Expenses** – `Clients × $200`.  
4. **Total Expenses** – `Fixed + Variable`.  
5. **Profit** – `Revenue – Total Expenses`.  
6. **Margin %** – `(Profit ÷ Revenue) × 100`.  

> **Do you see the revenue formula in column C correctly?**  
> If not, double‑check that the cell references are absolute (e.g., `$A$2 * 1200`).  

> **Error scenario:** If *Profit* shows a negative number, the *Variable Expense* per client is too high. Reduce the contractor fee or negotiate a better rate with Midjourney or Canva.

---

## 3.  Pricing Tiers Table  

| Tier | Price (USD) | Deliverables | Variable Cost | Gross Margin |
|------|-------------|--------------|---------------|--------------

For the free step-by-step guide, see our [implementation guide]({< ref "/intelligence/build-an-ai-seo-automation-service-with-chatgpt-the-complete-step-by-step-guide.md" >}).


## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
