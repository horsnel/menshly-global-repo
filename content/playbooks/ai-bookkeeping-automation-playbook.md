---
title: "The AI Bookkeeping Automation Playbook: 37 Steps to $20K/Month"
date: 2026-05-01
category: "Playbook"
price: "₦35,000"
readTime: "90 MIN"
excerpt: "The complete operating system for building an AI bookkeeping automation business from zero. 10 modules, 35 procedures, exact tool configurations, client onboarding scripts, three pricing tiers, and a scaling roadmap. From empty Notion workspace to ₦10M/month in recurring revenue."
image: "/images/articles/playbooks/ai-bookkeeping-automation-playbook.png"
heroImage: "/images/heroes/playbooks/ai-bookkeeping-automation-playbook.png"
---

This is not a blog post condensed into a PDF. This is an operating system for building an AI bookkeeping automation business from zero to ₦10,000,000/month in recurring revenue. Every module contains exact procedures — not theories, not possibilities, not "consider doing X." You will do X, in this order, with these tools, and you will verify it worked before moving on.

**35 procedures. 10 modules. 8+ hours of reading and execution.** If you complete every procedure, you will have a functioning bookkeeping automation practice with paying clients. If you skip procedures, you will have a folder of half-finished Zapier workflows and no revenue. The choice is yours.

---

# MODULE 1: FOUNDATION — YOUR BOOKKEEPING COMMAND CENTER

## Overview

Before you automate a single transaction, you need the infrastructure that runs your bookkeeping practice. This module sets up your project management, client portal, financial tracking, and communication systems. These are not optional. Every successful bookkeeping operator has these systems in place before their first client call. Every failed operator skipped them.

**Time to complete:** 3-4 hours
**Tools needed:** Notion (free), QuickBooks Online Accountant (free for accountants), Zapier (free tier), Paystack (free)

## Procedure 1.1: Create Your Bookkeeping Command Center in Notion

Open your browser and go to notion.so. Sign in or create a free account. You should see the Notion dashboard — a clean sidebar on the left and a main area with a "New page" button.

Do you see the dashboard? If you see a blank screen, clear your browser cache and reload. If you see a pricing page, close it — the free tier is sufficient for everything in this module.

Click **New page** in the left sidebar. Name it: `[Your Practice Name] Command Center`. This is the single source of truth for your entire business.

Inside this page, create seven sub-pages by typing `/page` and naming each one:

1. **Clients** — Every client, their status, their chart of accounts, their revenue
2. **SOPs** — Standard Operating Procedures for every repeatable bookkeeping process
3. **Prompt Library** — Every AI prompt your practice uses, organized by workflow type
4. **Templates** — Client-facing documents, engagement letters, reports, proposals
5. **Finance** — Revenue tracking, expense tracking, margin analysis
6. **Pipeline** — Prospects, leads, and their position in your sales process
7. **Automation Logs** — Every Zapier workflow, its status, its last run time, its error count

Do you see all seven sub-pages listed inside your Command Center? If any are missing, add them now. You should have exactly seven. Count them.

### The Clients Database

Open the **Clients** sub-page. Type `/table` and select **Table — Full page**. This creates a database. Name it `Client Roster`.

Add these columns (click the `+` button at the right end of the header row):

| Column Name | Type | Description |
|---|---|---|
| Client Name | Title | The business name |
| Status | Select: Active, Onboarding, Paused, Churned | Current relationship state |
| Tier | Select: Starter, Growth, Enterprise | Service tier |
| Monthly Revenue | Number | Retainer amount in Naira |
| Setup Fee | Number | One-time setup fee in Naira |
| Start Date | Date | When the engagement began |
| QBO Entity ID | Text | QuickBooks Online company ID |
| Last Reconciliation | Date | When bank rec was last completed |
| Health Score | Select: Green, Yellow, Red | Subjective assessment of the relationship |

Add one row for yourself as a test: Client Name = "Test Client," Status = "Active," Tier = "Starter," Monthly Revenue = 150000, Setup Fee = 200000. Fill in the remaining fields with any values.

Do you see the test row in your table with all columns populated? If any columns are missing, add them. Incomplete data tracking is the number one cause of bookkeeping practice cash flow problems.

### The Automation Logs Database

Open the **Automation Logs** sub-page. Create another full-page table called `Zapier Workflow Registry`.

Add these columns:

| Column Name | Type |
|---|---|
| Workflow Name | Title |
| Client | Relation (linked to Client Roster) |
| Status | Select: Active, Paused, Broken, Draft |
| Trigger App | Text |
| Last Successful Run | Date |
| Error Count (30d) | Number |
| Zap URL | URL |

You will populate this database throughout this playbook. By the end, you will have entries for every Zapier workflow across every client.

## Procedure 1.2: Set Up Your Financial Infrastructure

### Create Your Paystack Account

Go to paystack.com and create a business account. Complete the business verification process (you will need a Nigerian bank account, BVN, and business registration documents). This typically takes 2-5 business days for approval.

Once approved, you should see the Paystack dashboard with a "Test mode" toggle in the top-right corner. Do you see it? If your account is still pending verification, continue with the rest of this module and return to this step when approved.

### Create Your Payment Products

In Paystack, go to **Products** in the left sidebar. Click **Add product**. Create six products — three setup fees and three monthly retainers:

| Product Name | Price | Type |
|---|---|---|
| Starter Setup Fee | ₦150,000 | One time |
| Starter Monthly Retainer | ₦75,000/month | Recurring |
| Growth Setup Fee | ₦300,000 | One time |
| Growth Monthly Retainer | ₦200,000/month | Recurring |
| Enterprise Setup Fee | ₦500,000 | One time |
| Enterprise Monthly Retainer | ₦400,000/month | Recurring |

Create payment links for each product (click the product → **Create payment link**). Save these links in your Notion **Templates** page under a sub-page called "Payment Links."

Do you see all six products listed in your Paystack dashboard? Do all six have payment links? If any are missing, create them now. A missing payment link means a delayed payment, which means a delayed start, which means a frustrated client.

### Set Up Revenue Tracking

In your Notion **Finance** page, create a table called `Revenue Tracker` with these columns:

| Column Name | Type |
|---|---|
| Month | Title (e.g., "May 2026") |
| Total MRR | Number (Monthly Recurring Revenue in Naira) |
| Setup Fees | Number |
| Total Revenue | Formula: Total MRR + Setup Fees |
| Expenses | Number |
| Net Profit | Formula: Total Revenue - Expenses |
| Active Clients | Number |
| Average Revenue Per Client | Formula: Total MRR / Active Clients |

Add a row for the current month with zero values. This is your starting line.

## Procedure 1.3: Configure Your Communication Stack

### Create Your Business Email

If you do not have a professional email address on a custom domain, set one up now. Go to Google Workspace (workspace.google.com) and sign up for the Business Starter plan ($6/mo). Register a domain that matches your practice name (e.g., yourpractice.com) and create your email (e.g., hello@yourpractice.com or yourname@yourpractice.com).

Do not use a personal Gmail address for client communication. It signals amateur status. A custom domain email costs $6/month and instantly elevates your perceived professionalism.

### Create Your Client-Facing Calendar

Go to cal.com and create a free account. Set up a booking page with two meeting types:

1. **Discovery Call** — 30 minutes, available Monday through Friday, 9 AM to 5 PM WAT
2. **Monthly Review** — 30 minutes, recurring, for active clients only

Connect your Google Calendar so bookings appear automatically. Copy your booking link and save it in your Notion **Templates** page.

{{% accent-box %}}
**HACK:** Use Notion's "Template" button inside your Client Roster database to create a pre-filled template for new clients. Include default values for Status ("Onboarding"), Health Score ("Green"), and a checklist of onboarding tasks: "Collect QBO access," "Obtain bank statements," "Review chart of accounts," "Set up Zapier triggers." This saves 15 minutes every time you sign a new client.
{{% /accent-box %}}

## Check-In: Module 1 Complete

Before moving to Module 2, verify every item:

- [ ] Notion Command Center created with all 7 sub-pages
- [ ] Client Roster database with all 9 columns and a test row
- [ ] Zapier Workflow Registry database with all 7 columns
- [ ] Paystack account with 6 products and 6 payment links
- [ ] Revenue Tracker table in Notion with current month row
- [ ] Professional email address on custom domain
- [ ] Cal.com booking page with Discovery Call and Monthly Review

Count your checkmarks. Do you have all 7? If not, go back and complete the missing items. Do not proceed to Module 2 with an incomplete foundation.

---

# MODULE 2: TECH STACK — YOUR BOOKKEEPING AUTOMATION ARSENAL

## Overview

Your bookkeeping practice runs on tools. This module sets up every tool you need, connects them, and verifies each connection. The total cost is under ₦50,000/month — and most of it is free until you have paying clients.

**Time to complete:** 3-4 hours
**Total monthly cost (startup):** ₦0–₦15,000 depending on your choices

## Procedure 2.1: Set Up QuickBooks Online Accountant

Go to quickbooks.intuit.com/accountants/ and sign up for QuickBooks Online Accountant. This is free for accounting professionals and gives you access to the Accountant Toolbox, wholesale pricing on QBO subscriptions, and the ability to manage multiple client books from a single dashboard.

After signing in, you should see the QBO Accountant dashboard with a "Add client" button. Do you see it? If you see a different interface, click "Clients" in the left sidebar.

### Configure Your Firm Settings

Click the gear icon (top-right) → **Firm Settings**. Fill in:

- **Firm name:** Your practice name
- **Email:** Your professional email address
- **Phone:** Your business phone number
- **Website:** Your domain URL
- **Industry:** Accounting/Bookkeeping

Click **Save**.

### Enable ProConnect Tax (Optional for Nigerian Market)

If you plan to offer tax filing services, navigate to the **Tax** tab in QBO Accountant. For Nigerian clients, you will handle VAT, WHT, and CIT manually or through dedicated Nigerian tax software. QBO does not natively support Nigerian tax forms. This is an opportunity — you will build custom tax computation workflows in Module 7.

## Procedure 2.2: Set Up Zapier and Connect Core Services

Go to zapier.com and sign up for the Free plan. You get 100 tasks per month — enough to build and test your first 3-5 workflows.

After signing in, you should see the Zapier dashboard with a "Create a Zap" button. Do you see it?

### Connect Your Core Services

In Zapier, click **My Apps** in the left sidebar → **Add connection**. Connect the following services:

1. **QuickBooks Online** — Authorize with your QBO Accountant credentials
2. **Google Sheets** — Authorize with your Google account
3. **Gmail** — Authorize with your professional email
4. **Notion** — Authorize with your Notion account
5. **Slack** — Authorize with your Slack workspace (create one at slack.com if needed)

After connecting each service, you should see a green "Connected" status next to it. Do you see green for all 5? If any show red or yellow:

- Google/Gmail/Slack/Notion: Re-authorize and make sure you approve all permissions
- QuickBooks Online: Ensure you are using QBO Accountant (not a regular QBO subscription)

## Procedure 2.3: Set Up AI Model Access

### OpenAI API Configuration

Go to platform.openai.com. Navigate to **API Keys** and create a new key. Copy it immediately — you cannot view it again. Store it in a password manager (1Password, Bitwarden, or the Mac Keychain). Do not store API keys in Notion pages that you share with anyone.

Navigate to **Billing** and add $20 in credit. This funds your API usage for approximately 500-1,000 transaction categorization and enrichment operations.

Navigate to **Usage limits** and set a monthly limit of $100. This prevents a buggy Zap from draining your credit overnight.

### Anthropic Claude API (Recommended for Bookkeeping)

Go to console.anthropic.com and create an account. Navigate to **API Keys** and create a key. Add $10 in credit. Claude is superior to GPT-4o for financial document analysis, nuanced transaction categorization, and complex reasoning tasks involving multi-step accounting logic. Use GPT-4o for structured outputs (JSON) and Claude for document analysis and reconciliation tasks.

{{% accent-box %}}
**HACK:** Set up two separate OpenAI API keys — one for production automations and one for testing. When a test workflow goes haywire, it burns through the testing key's credit, not your production budget. Create the keys at platform.openai.com/api-keys and label them "prod-bookkeeping" and "dev-bookkeeping."
{{% /accent-box %}}

## Procedure 2.4: Set Up Your Client Delivery Tools

### Slack Workspace Configuration

Go to slack.com and create a workspace if you have not already. Create these channels:

- `#automation-errors` — All error notifications from Zapier go here
- `#reconciliation-alerts` — Alerts when bank reconciliations fail or show discrepancies
- `#new-clients` — Notifications when a new client signs

Do you see all the channels in your Slack sidebar? The `#automation-errors` channel is the most important — it is your early warning system for broken automations.

### Loom for Client Communication

Go to loom.com and create a free account. Install the Loom browser extension. You will use Loom to record walkthrough videos for clients — showing them their financial dashboards, explaining reconciliation results, and answering questions. A 3-minute Loom video replaces a 30-minute call and can be rewatched indefinitely.

Record a test video: open Loom, click record, say "This is a test video for my bookkeeping practice setup," and stop. Watch the playback. Does the audio sound clear? If it sounds echoey or quiet, adjust your microphone settings. Clear audio is non-negotiable.

### Google Drive Client Folder Structure

Create a folder structure in Google Drive:

```
Practice Drive/
├── Clients/
│   ├── [Client Name]/
│   │   ├── Onboarding/
│   │   ├── Bank Statements/
│   │   ├── Invoices/
│   │   ├── Receipts/
│   │   └── Reports/
├── Templates/
├── Internal/
│   ├── Finance/
│   └── SOPs/
└── Prospects/
```

Create this structure now. Do you see all the folders? This organization prevents the chaos that kills bookkeeping practices — the "where did I put that client's bank statement?" problem that wastes hours every week.

## Procedure 2.5: Complete Tool Cost Summary

| Tool | Purpose | Free Tier | Paid Tier | When to Upgrade |
|---|---|---|---|---|
| QuickBooks Online Accountant | Client bookkeeping | Free for accountants | Wholesale pricing from $10/mo per client | At first paying client |
| Zapier | Workflow automation | 100 tasks/mo | $20/mo (750 tasks) | At first paying client |
| OpenAI API | AI categorization & analysis | Pay per use | ~$20-80/mo | At first automation |
| Notion | Project management | Free | $10/mo | At 5+ team members |
| Google Workspace | Email + docs | — | $6/mo | Immediately |
| Paystack | Payment processing | Free | 1.5% + ₦100/tx | Always |
| Loom | Video communication | Free (25 videos) | $13/mo | When free tier limits are hit |
| Slack | Team communication | Free | $8/user/mo | At 3+ team members |
| DocuMint (or Stampify) | Nigerian receipt/invoice OCR | Free trial | ₦15,000/mo | At 3+ clients |

**Startup cost: $6/mo (Google Workspace only). Everything else is free until you have revenue.**

## Check-In: Module 2 Complete

- [ ] QuickBooks Online Accountant account with firm settings configured
- [ ] Zapier account with 5 connected services (all green)
- [ ] OpenAI API key with $20+ credit and $100 monthly limit
- [ ] Claude API key with $10+ credit (recommended)
- [ ] Slack workspace with #automation-errors, #reconciliation-alerts, #new-clients channels
- [ ] Loom account with test video recorded and clear audio
- [ ] Google Drive folder structure created
- [ ] All tool costs documented in Notion Finance page

8 checkmarks required to proceed. Do you have all 8?

---

# MODULE 3: CHART OF ACCOUNTS SETUP — THE SPINE OF EVERY CLIENT

## Overview

Every bookkeeping engagement starts with a properly structured chart of accounts (CoA). A bad CoA produces bad financial statements, which produces bad business decisions, which produces churned clients. This module gives you the exact CoA templates, the exact QuickBooks setup steps, and the exact AI-powered categorization rules that make your practice deliver accurate books on day one.

**Time to complete:** 2-3 hours per client
**Tools needed:** QuickBooks Online, Notion, OpenAI API

## Procedure 3.1: Create Your Master Chart of Accounts Template

Open your Notion **Templates** page. Create a new sub-page called `Master Chart of Accounts`. This template will be cloned and customized for every new client.

Build the following CoA structure. These are the standard accounts required for Nigerian SMEs. Every account listed below must exist in your template.

### Asset Accounts (1000–1999)

| Account Number | Account Name | Type | Detail Type |
|---|---|---|---|
| 1000 | Cash on Hand | Bank | Cash on hand |
| 1010 | GTBank Operating Account | Bank | Checking |
| 1020 | Access Bank Savings Account | Bank | Savings |
| 1030 | USD Domiciliary Account | Bank | Checking |
| 1100 | Accounts Receivable | Accounts Receivable | Accounts Receivable (A/R) |
| 1200 | Employee Advances | Other Current Asset | Employee Advances |
| 1300 | Prepaid Expenses | Other Current Asset | Prepaid Expenses |
| 1400 | Inventory — Finished Goods | Other Current Asset | Inventory |
| 1500 | Fixed Assets — Office Equipment | Fixed Asset | Furniture and Fixtures |
| 1510 | Fixed Assets — Vehicles | Fixed Asset | Vehicles |
| 1520 | Accumulated Depreciation | Fixed Asset | Accumulated Depreciation |

### Liability Accounts (2000–2999)

| Account Number | Account Name | Type | Detail Type |
|---|---|---|---|
| 2000 | Accounts Payable | Accounts Payable | Accounts Payable (A/P) |
| 2100 | Accrued Expenses | Other Current Liability | Accrued Liabilities |
| 2200 | VAT Payable | Other Current Liability | Nigerian VAT |
| 2210 | WHT Payable | Other Current Liability | Withholding Tax |
| 2300 | PAYE Payable | Other Current Liability | Payroll Liabilities |
| 2400 | Pension Payable | Other Current Liability | Pension Contributions |
| 2500 | Customer Deposits | Other Current Liability | Customer Deposits |
| 2600 | Bank Loan — GTBank | Long Term Liability | Notes Payable |

### Equity Accounts (3000–3999)

| Account Number | Account Name | Type | Detail Type |
|---|---|---|---|
| 3000 | Owner's Equity | Equity | Owner's Equity |
| 3100 | Retained Earnings | Equity | Retained Earnings |
| 3200 | Owner's Drawings | Equity | Owner's Drawings |

### Revenue Accounts (4000–4999)

| Account Number | Account Name | Type | Detail Type |
|---|---|---|---|
| 4000 | Sales Revenue — Products | Income | Sales of Product Income |
| 4100 | Sales Revenue — Services | Income | Service/Fee Income |
| 4200 | Interest Income | Income | Interest Earned |
| 4300 | Other Income | Income | Other Miscellaneous Income |

### Cost of Goods Sold (5000–5999)

| Account Number | Account Name | Type | Detail Type |
|---|---|---|---|
| 5000 | Cost of Goods Sold | Cost of Goods Sold | Cost of Goods Sold |
| 5100 | Freight and Delivery | Cost of Goods Sold | Shipping and Delivery |

### Expense Accounts (6000–6999)

| Account Number | Account Name | Type | Detail Type |
|---|---|---|---|
| 6000 | Rent Expense | Expense | Rent or Lease of Buildings |
| 6100 | Salaries and Wages | Expense | Payroll Expenses |
| 6110 | Pension Contributions | Expense | Pension |
| 6200 | Utilities — Electricity | Expense | Utilities |
| 6210 | Utilities — Internet | Expense | Utilities |
| 6300 | Office Supplies | Expense | Office/General Administrative Expenses |
| 6400 | Professional Fees | Expense | Legal and Professional Fees |
| 6500 | Marketing and Advertising | Expense | Advertising/Promotional |
| 6600 | Travel and Transportation | Expense | Travel |
| 6700 | Bank Charges | Expense | Bank Charges |
| 6800 | Depreciation Expense | Expense | Depreciation |
| 6900 | Insurance | Expense | Insurance |

Do you see all accounts listed in your Notion template? Count them. You should have 35+ accounts. This is your starting template — every client will have additions, but no client should have fewer accounts than this.

## Procedure 3.2: Set Up the Chart of Accounts in QuickBooks Online

For each new client, follow this exact procedure:

1. Log in to QBO Accountant. Click **Add client** → enter the client's business name and email → select **QuickBooks Online Plus** (or Essentials for Starter tier clients).
2. Once the client's QBO company is created, click **Go to client's QuickBooks** (this switches you into their books).
3. Click the gear icon → **Chart of Accounts** → **New**.
4. For each account in your Master CoA template, enter the Account Number, Name, Type, and Detail Type exactly as listed.
5. After all accounts are entered, click **Run Report** → **Balance Sheet** to verify the accounts appear correctly.

### AI-Powered CoA Customization

After entering the standard accounts, use OpenAI to generate client-specific additions. Create a Zapier workflow (you will build this in Module 4) that:

1. Takes the client's industry and business description as input
2. Sends it to OpenAI with this prompt: "Given a Nigerian [industry] business described as [description], suggest additional chart of accounts entries beyond the standard SME template. For each suggestion, provide: Account Number (in the correct 1000-range), Account Name, Type, and Detail Type. Format as a JSON array."
3. Returns the suggestions to a Google Sheet for your review
4. You manually add approved accounts to QBO

Do NOT add AI-suggested accounts without human review. AI generates plausible-sounding but sometimes incorrect account types. You are the professional. You verify.

{{% accent-box %}}
**HACK:** Create a Notion database called "Industry CoA Add-ons" with columns: Industry, Account Number, Account Name, Type, Detail Type, and Notes. Every time you customize a CoA for a new industry, save the additions here. After 5 clients in the same industry, you will have a complete industry-specific CoA that requires zero AI generation — you just clone it from Notion.
{{% /accent-box %}}

## Procedure 3.3: Configure QBO Bank Rules for Auto-Categorization

After the CoA is set up, configure bank rules in QBO to auto-categorize recurring transactions. This is the first layer of automation — before Zapier, before AI.

In QBO (inside the client's books), go to **Banking** → **Rules** → **New Rule**.

Create these standard rules:

| Rule Name | Condition | Category | Payee |
|---|---|---|---|
| GTBank Monthly Fee | Description contains "GTB MAINTENANCE" | 6700 Bank Charges | GTBank |
| DSTV Subscription | Description contains "DSTV" or "MULTICHOICE" | 6000 Rent Expense | MultiChoice |
| MTN Data Purchase | Description contains "MTN" AND amount < ₦10,000 | 6210 Utilities — Internet | MTN Nigeria |
| PHCN Electricity | Description contains "PHCN" or "AEDC" or "IKEDC" | 6200 Utilities — Electricity | [Distribution Co] |
| Salary Payment | Description contains "SALARY" | 6100 Salaries and Wages | [Employee Name] |
| VAT Remittance | Description contains "VAT" AND payee contains "FIRS" | 2200 VAT Payable | FIRS |

After creating each rule, go to **Banking** → **For Review** tab. Find a transaction that matches the rule. Does QBO suggest the correct category? If yes, the rule works. If no, adjust the condition and test again.

Create at least 6 bank rules before proceeding. These rules will auto-categorize 40-60% of all transactions, reducing the manual work your AI workflows need to handle.

## Check-In: Module 3 Complete

- [ ] Master Chart of Accounts template created in Notion with 35+ accounts
- [ ] Test client QBO company created with full CoA entered
- [ ] AI CoA customization prompt tested with at least one industry
- [ ] 6+ bank rules configured in QBO test client
- [ ] Bank rules verified against real (or test) transactions in For Review tab

5 checkmarks. The bank rules are the invisible workhorse of your practice. Do not skip them.

---

# MODULE 4: TRANSACTION AUTOMATION — THE CORE ENGINE

## Overview

This module builds the core automation engine: bank transactions flow from QBO into your categorization pipeline, AI categorizes what the bank rules miss, and everything is logged and verified. This is the single most valuable automation in your entire practice. It replaces 15-20 hours of manual transaction categorization per client per month.

**Time to complete:** 4-6 hours
**Tools needed:** Zapier, QuickBooks Online, OpenAI API, Google Sheets, Slack

## Procedure 4.1: Build the Transaction Categorization Zap

### Step A: Create the Trigger

In Zapier, click **Create a Zap**. Name it "Transaction Categorization Pipeline."

For the trigger, select **QuickBooks Online** → **New Transaction**. Connect your QBO Accountant account. Select the test client's company.

Test the trigger. Do you see sample transaction data? You should see fields like: `Id`, `TxnType`, `Amount`, `Description`, `AccountRef`, `Date`. If the trigger returns empty data, go to QBO and manually add a test transaction, then re-test the trigger.

### Step B: Filter Out Already-Categorized Transactions

Add a **Filter** step (Zapier built-in):

Condition: `Category` does NOT exist (is empty) OR `Category` equals "Uncategorized Income" OR `Category` equals "Uncategorized Expense"

This ensures the Zap only processes transactions that QBO's bank rules did NOT already categorize. Do not re-process categorized transactions — that wastes API credits and can overwrite correct categories.

### Step C: AI Categorization

Add a **ChatGPT** step (OpenAI in Zapier):

- **Model:** `gpt-4o`
- **System Message:**

```
You are a Nigerian bookkeeping categorization assistant. Given a bank transaction, categorize it into the correct chart of accounts. You must respond ONLY with valid JSON in this exact format:
{
  "account_number": "6700",
  "account_name": "Bank Charges",
  "confidence": 0.95,
  "payee": "GTBank",
  "reasoning": "GTB MAINTENANCE FEE is a standard bank maintenance charge"
}

Available accounts: [PASTE YOUR FULL COA HERE]

Rules:
- If the description contains "POS" and a merchant name, categorize as the merchant's industry
- If confidence is below 0.7, set account_number to "9999" and account_name to "REVIEW REQUIRED"
- Nigerian bank descriptions are often abbreviated: "TRF" = transfer, "VAT" = value added tax, "WHT" = withholding tax, "POS" = point of sale
- Salary payments always go to 6100
- Any payment to FIRS goes to the appropriate tax liability account
```

- **User Message:** Map the transaction fields:

```
Transaction Type: {{TxnType}}
Amount: {{Amount}}
Description: {{Description}}
Date: {{Date}}
Account: {{AccountRef__name}}
```

### Step D: Parse the AI Response

Add a **Code by Zapier** step (JavaScript):

```javascript
const response = inputData.aiResponse;
try {
  const parsed = JSON.parse(response);
  output = {
    account_number: parsed.account_number,
    account_name: parsed.account_name,
    confidence: parsed.confidence,
    payee: parsed.payee,
    reasoning: parsed.reasoning,
    needs_review: parsed.account_number === "9999" ? "yes" : "no"
  };
} catch (e) {
  output = {
    account_number: "9999",
    account_name: "REVIEW REQUIRED - PARSE ERROR",
    confidence: 0,
    payee: "",
    reasoning: "AI response was not valid JSON: " + e.message,
    needs_review: "yes"
  };
}
```

### Step E: Route Based on Confidence

Add a **Paths** step (Zapier built-in):

**Path A: High Confidence (needs_review = "no")**
Add a **QuickBooks Online** step → **Update Transaction**:
- Map the `account_number` and `account_name` from the Code step
- This auto-categorizes the transaction in QBO

Also add a **Google Sheets** step → **Add Row** to your "Transaction Log" spreadsheet with columns: Date, Description, Amount, AI Category, Confidence, Action Taken.

**Path B: Needs Review (needs_review = "yes")**
Add a **Slack** step → **Send Message** to `#reconciliation-alerts`:

```
⚠️ TRANSACTION NEEDS REVIEW
Client: [Client Name]
Date: {{Date}}
Description: {{Description}}
Amount: ₦{{Amount}}
AI Suggestion: {{account_name}} ({{confidence}} confidence)
Reasoning: {{reasoning}}
Link: [QBO Transaction URL]
```

Also add a **Google Sheets** step → **Add Row** to the same "Transaction Log" spreadsheet with Action Taken = "FLAGGED FOR REVIEW".

## Procedure 4.2: Test the Transaction Pipeline

Create 10 test transactions in QBO that simulate real Nigerian business activity:

| Description | Amount | Expected Category |
|---|---|---|
| TRF TO JOHN DOE SALARY MARCH | ₦250,000 | 6100 Salaries and Wages |
| POS PURCHASE SHOPRITE IKEJA | ₦15,400 | 6300 Office Supplies (or 6000 Rent) |
| GTB MAINTENANCE FEE | ₦1,050 | 6700 Bank Charges |
| VAT REMITTANCE FIRS Q1 2026 | ₦187,500 | 2200 VAT Payable |
| DSTV SUBSCRIPTION MULTICHOICE | ₦21,000 | 6000 Rent Expense |
| MTN DATA BUNDLE 10GB | ₦5,000 | 6210 Utilities — Internet |
| PHCN AEDC TOKEN PURCHASE | ₦8,500 | 6200 Utilities — Electricity |
| INVOICE PAYMENT FROM CLIENT ABC | ₦750,000 | 1100 Accounts Receivable |
| PETTY CASH REIMBURSEMENT | ₦3,200 | 6300 Office Supplies |
| TRANSFER TO SAVINGS ACCOUNT | ₦500,000 | 1020 Access Bank Savings Account |

Run the Zap for each test transaction. Does the AI categorize at least 8 out of 10 correctly? If accuracy is below 80%, refine the system prompt with additional Nigerian banking abbreviations and common transaction patterns. Re-test until you achieve 80%+ accuracy.

## Procedure 4.3: Build the Weekly Transaction Summary Zap

Create a second Zap that runs every Friday at 5 PM WAT:

**Trigger:** Schedule by Zapier → Every Friday at 5:00 PM
**Step 1:** QuickBooks Online → Find Transactions (last 7 days)
**Step 2:** Code by Zapier → Generate summary statistics (total categorized, total flagged, categorization rate)
**Step 3:** Gmail → Send email to client with the summary

Email template:

```
Subject: Weekly Bookkeeping Summary — [Client Name] — [Date Range]

Hi [Client First Name],

Here's your weekly bookkeeping summary:

✅ Transactions categorized: [X] (Auto: [Y], AI: [Z])
⚠️ Transactions needing review: [X]
📊 Categorization accuracy: [X]%

Review items:
[List of flagged transactions with amounts]

Please reply with corrections or approvals by Monday 12 PM.

[Your Name]
[Your Practice Name]
```

## Check-In: Module 4 Complete

- [ ] Transaction Categorization Zap built with trigger, filter, AI, parser, and paths
- [ ] 10 test transactions run through the pipeline
- [ ] AI categorization accuracy at 80%+ on test transactions
- [ ] High-confidence transactions auto-categorized in QBO
- [ ] Low-confidence transactions flagged in Slack with reasoning
- [ ] Transaction Log spreadsheet created and receiving data
- [ ] Weekly Transaction Summary Zap built and tested
- [ ] Both Zaps added to the Zapier Workflow Registry in Notion

8 checkmarks. The Transaction Categorization Zap is the revenue engine of your practice. It must work before you move forward.

---

# MODULE 5: INVOICE PROCESSING — FROM CHAOS TO CLEAN

## Overview

Client invoices arrive in every format imaginable — WhatsApp photos, email attachments, crumpled paper, PDFs, and Excel sheets. This module builds the automation pipeline that captures, extracts, and processes invoices into QuickBooks with minimal human intervention.

**Time to complete:** 3-4 hours
**Tools needed:** Zapier, Gmail, Google Drive, OpenAI API (GPT-4o with Vision), QuickBooks Online

## Procedure 5.1: Set Up the Invoice Capture Pipeline

### Configure Gmail Inbox for Invoice Intake

Create a dedicated email address or label for invoice intake: `invoices@yourpractice.com` or set up a Gmail filter that labels emails containing "invoice," "receipt," or "bill" as "Invoice Intake."

In Gmail, click the search bar → **Show search options** → enter the following:
- **Has the words:** invoice OR receipt OR bill OR remita OR payment voucher
- Click **Create filter** → check **Apply the label** → create new label "Invoice Intake" → check **Also apply filter to matching conversations** → **Create filter**

### Build the Invoice Capture Zap

Create a new Zap: "Invoice Processing Pipeline."

**Trigger:** Gmail → New Email Matching Search
- Search/label: "label:invoice-intake"

**Step 1: Filter for Attachments**
Add a **Filter** step:
- Condition: `Attachments Exists` is `true`
- This skips emails that mention invoices but have no actual invoice attached

**Step 2: Save Attachment to Google Drive**
Add **Google Drive** → **Upload File**:
- Drive: Your Practice Drive
- Folder: Clients/[Client Name]/Invoices/
- File: Map the attachment from the Gmail trigger

**Step 3: AI Invoice Extraction**
Add **ChatGPT** step with Vision capability:

- **Model:** `gpt-4o`
- **Enable Vision:** Yes
- **System Message:**

```
You are a Nigerian invoice processing assistant. Extract the following fields from the attached invoice image/document. Respond ONLY in valid JSON:
{
  "vendor_name": "",
  "invoice_number": "",
  "invoice_date": "YYYY-MM-DD",
  "due_date": "YYYY-MM-DD",
  "subtotal": 0.00,
  "vat_amount": 0.00,
  "wht_amount": 0.00,
  "total_amount": 0.00,
  "currency": "NGN",
  "line_items": [
    {"description": "", "quantity": 1, "unit_price": 0.00, "amount": 0.00}
  ],
  "vendor_tin": "",
  "category_suggestion": "",
  "confidence": 0.0
}

Nigerian invoice specifics:
- VAT is 7.5% on applicable goods/services
- WHT ranges from 5% (contracts) to 10% (royalties, dividends)
- Look for TIN (Tax Identification Number) format: 00000000-0000
- Common vendors: PHCN, DSTV, MTN, Glo, Airbnb, hotel chains
- If the document is not an invoice, set confidence to 0 and all fields to null
```

- **User Message:** "Extract data from this invoice."
- **Image:** Map the attachment from the Gmail trigger

**Step 4: Parse and Validate**
Add **Code by Zapier** (JavaScript):

```javascript
const data = JSON.parse(inputData.aiResponse);
const errors = [];

if (!data.vendor_name) errors.push("Missing vendor name");
if (!data.invoice_date) errors.push("Missing invoice date");
if (!data.total_amount || data.total_amount <= 0) errors.push("Invalid total amount");
if (data.confidence < 0.6) errors.push("Low confidence: " + data.confidence);

output = {
  vendor_name: data.vendor_name || "UNKNOWN",
  invoice_number: data.invoice_number || "N/A",
  invoice_date: data.invoice_date || "UNKNOWN",
  due_date: data.due_date || "UNKNOWN",
  subtotal: data.subtotal || 0,
  vat_amount: data.vat_amount || 0,
  wht_amount: data.wht_amount || 0,
  total_amount: data.total_amount || 0,
  currency: data.currency || "NGN",
  category_suggestion: data.category_suggestion || "",
  confidence: data.confidence || 0,
  has_errors: errors.length > 0 ? "yes" : "no",
  error_list: errors.join("; "),
  line_items_json: JSON.stringify(data.line_items || [])
};
```

**Step 5: Route Based on Validation**

Add **Paths**:

**Path A: Clean Invoice (has_errors = "no")**
1. QuickBooks Online → **Create Bill** (for vendor invoices) or **Create Expense** (for paid receipts)
   - Map vendor_name, invoice_date, due_date, total_amount, category_suggestion
   - Line items: Map from line_items_json
2. Google Sheets → **Add Row** to "Invoice Processing Log"

**Path B: Invoice Has Errors (has_errors = "yes")**
1. Slack → **Send Message** to `#reconciliation-alerts`:

```
📋 INVOICE PROCESSING ERROR
Vendor: {{vendor_name}}
Date: {{invoice_date}}
Amount: ₦{{total_amount}}
Errors: {{error_list}}
Confidence: {{confidence}}
Action: Manual review required
```

2. Google Sheets → **Add Row** to "Invoice Processing Log" with status "ERROR"

## Procedure 5.2: Set Up WhatsApp Invoice Forwarding

Nigerian SMEs send invoices via WhatsApp. You need a way to capture these.

### Option A: WhatsApp Business API + Zapier

If you have WhatsApp Business API access, connect it to Zapier using the WhatsApp Business module. Set up a trigger for incoming messages with images. Route images through the same AI extraction pipeline.

### Option B: Manual Forwarding Rule (Simpler, Works Immediately)

Create a standard operating procedure for clients:

1. Client receives an invoice on WhatsApp
2. Client forwards the invoice image to `invoices@yourpractice.com` via email (WhatsApp → Share → Email)
3. The Gmail invoice capture Zap picks it up automatically

Create a client-facing instruction document in Notion **Templates** called "How to Send Us Invoices." It should contain:

```
SENDING INVOICES TO [YOUR PRACTICE NAME]

Option 1: Email
Forward all invoices and receipts to: invoices@yourpractice.com

Option 2: WhatsApp
Save this number: [+234 XXX XXX XXXX]
Send photos of invoices and receipts directly

Option 3: Google Drive
Upload to your shared folder: [Link]

Please send invoices within 48 hours of receipt.
The clearer the image, the faster we process it.
```

{{% accent-box %}}
**HACK:** Create a WhatsApp group for each client called "[Client Name] — Bookkeeping." Add the business owner and their admin. Tell them to drop invoice photos directly in the group. You (or your VA) monitor the group daily and forward images to the invoices@ email address. This creates a paper trail and makes the client feel supported in real time.
{{% /accent-box %}}

## Procedure 5.3: Build the Accounts Payable Aging Zap

Create a Zap that runs every Monday at 9 AM WAT:

**Trigger:** Schedule by Zapier → Every Monday at 9:00 AM
**Step 1:** QuickBooks Online → Find Bills (status: unpaid, due date within 7 days)
**Step 2:** Code by Zapier → Format the aging report
**Step 3:** Gmail → Send email to client:

```
Subject: ⏰ Upcoming Payables — [Client Name] — Week of [Date]

Hi [Client First Name],

The following bills are due within the next 7 days:

[Vendor Name] — ₦[Amount] — Due: [Date]
[Vendor Name] — ₦[Amount] — Due: [Date]

Total upcoming payables: ₦[Total]

Reply to approve payment or flag any discrepancies.

[Your Name]
```

This Zap alone is worth the monthly retainer. Clients love it because it prevents late payment penalties and damaged vendor relationships.

## Check-In: Module 5 Complete

- [ ] Gmail invoice filter and label configured
- [ ] Invoice Processing Pipeline Zap built with AI extraction
- [ ] AI invoice extraction tested with 5+ sample invoices
- [ ] Validation parser catches missing fields and low-confidence extractions
- [ ] Error path sends Slack alerts for manual review
- [ ] Invoice Processing Log spreadsheet receiving data
- [ ] Client-facing invoice submission instructions created
- [ ] Accounts Payable Aging Zap built and tested
- [ ] Both Zaps added to the Zapier Workflow Registry in Notion

9 checkmarks. Invoice processing is the most client-visible automation. It must be flawless.

---

# MODULE 6: BANK RECONCILIATION — AUTOMATED TRUTH

## Overview

Bank reconciliation is where bookkeeping becomes valuable. It is the process of confirming that every transaction in QBO matches the bank statement. Manual reconciliation takes 4-8 hours per client per month. This module reduces it to 30-60 minutes.

**Time to complete:** 3-4 hours
**Tools needed:** QuickBooks Online, Google Sheets, OpenAI API, Zapier

## Procedure 6.1: Configure QBO Bank Feeds

For each client, connect their bank accounts to QBO:

1. In QBO, go to **Banking** → **Add Account**
2. Search for the client's bank (GTBank, Access Bank, First Bank, UBA, Zenith Bank)
3. Log in with the client's internet banking credentials
4. QBO will begin importing transactions automatically

**If the bank is not supported by QBO direct feed** (common with some Nigerian banks), you have two options:

**Option A:** Import CSV statements manually each month
- Download the bank statement CSV from the client's internet banking
- In QBO, go to **Banking** → **Upload transactions** → select the CSV file
- Map the columns: Date, Description, Amount

**Option B:** Build a Zapier workflow that monitors the client's email for monthly bank statements
- Many Nigerian banks email monthly statements as PDF attachments
- Create a Gmail filter for "[bank name] statement" → label "Bank Statements"
- Use a PDF parsing tool (Docparser at docparser.com, ₦0-15,000/mo) to extract transaction data
- Push extracted data to a Google Sheet for import into QBO

Do you have at least one bank feed connected or importing for your test client? If not, do not proceed. Reconciliation requires bank data.

## Procedure 6.2: Build the Reconciliation Helper Zap

Create a new Zap: "Reconciliation Assistant."

**Trigger:** Schedule by Zapier → 1st of every month at 8:00 AM WAT
**Step 1:** QuickBooks Online → Find Transactions (last month)
**Step 2:** QuickBooks Online → Get Bank Register (last month)
**Step 3:** Code by Zapier → Compare the two datasets:

```javascript
const qboTransactions = JSON.parse(inputData.qboTransactions);
const bankTransactions = JSON.parse(inputData.bankTransactions);

const matched = [];
const unmatched_qbo = [];
const unmatched_bank = [];

// Match by amount + date (within 2-day tolerance)
for (const qt of qboTransactions) {
  const match = bankTransactions.find(bt =>
    Math.abs(bt.amount - qt.amount) < 1 &&
    Math.abs(new Date(bt.date) - new Date(qt.date)) < 3 * 86400000
  );
  if (match) {
    matched.push({...qt, match_type: "auto"});
  } else {
    unmatched_qbo.push(qt);
  }
}

// Find bank transactions not in QBO
for (const bt of bankTransactions) {
  const match = qboTransactions.find(qt =>
    Math.abs(bt.amount - qt.amount) < 1 &&
    Math.abs(new Date(bt.date) - new Date(qt.date)) < 3 * 86400000
  );
  if (!match) {
    unmatched_bank.push(bt);
  }
}

output = {
  total_qbo: qboTransactions.length,
  total_bank: bankTransactions.length,
  matched_count: matched.length,
  unmatched_qbo_count: unmatched_qbo.length,
  unmatched_bank_count: unmatched_bank.length,
  match_rate: (matched.length / Math.max(qboTransactions.length, 1) * 100).toFixed(1),
  unmatched_qbo: JSON.stringify(unmatched_qbo.slice(0, 20)),
  unmatched_bank: JSON.stringify(unmatched_bank.slice(0, 20))
};
```

**Step 4:** AI Analysis of Unmatched Transactions
Add **ChatGPT** step:

- **System Message:** "You are a bank reconciliation assistant for a Nigerian bookkeeping practice. Given lists of unmatched transactions from QBO and the bank statement, identify likely matches that the date/amount algorithm missed. Look for: split payments, combined deposits, bank fees added to payments, timing differences, and partial payments. Respond in JSON with an array of suggested matches and unmatched items requiring manual review."
- **User Message:** Map the unmatched_qbo and unmatched_bank arrays

**Step 5:** Generate Reconciliation Report
Add **Google Docs** step → **Create Document from Template**:

Template content:

```
MONTHLY BANK RECONCILIATION REPORT
Client: [Client Name]
Period: [Month Year]
Generated: [Date]

SUMMARY
Total QBO Transactions: {{total_qbo}}
Total Bank Transactions: {{total_bank}}
Auto-Matched: {{matched_count}} ({{match_rate}}%)
Unmatched QBO: {{unmatched_qbo_count}}
Unmatched Bank: {{unmatched_bank_count}}

UNMATCHED ITEMS — REQUIRES REVIEW
[AI-generated analysis and suggestions]

ACTION ITEMS
[Number] transactions require manual matching
[Number] transactions are potential bank fees not yet recorded
[Number] transactions may be duplicate entries
```

**Step 6:** Send the report via Gmail to the client and post a summary in Slack.

## Procedure 6.3: Build the Discrepancy Alert Zap

Create a Zap that monitors for reconciliation discrepancies in real time:

**Trigger:** QuickBooks Online → New Transaction (with a filter for large amounts)
**Filter:** Amount > ₦500,000 (or client-specific threshold)
**Step 1:** QuickBooks Online → Get Transaction Details
**Step 2:** Code by Zapier → Check if the transaction has a matching bank entry
**Step 3:** If no match found → Slack alert to `#reconciliation-alerts`

This catches large discrepancies immediately rather than waiting for month-end reconciliation. A ₦5,000,000 transaction with no bank match is a problem you need to know about today, not on the 1st of next month.

{{% accent-box %}}
**HACK:** Set your reconciliation threshold per client based on their transaction volume. A client with 50 transactions/month should have a threshold of ₦100,000. A client with 500 transactions/month should have a threshold of ₦500,000. The formula: threshold = (monthly revenue ÷ transaction count) × 3. Store this in the Client Roster and reference it in your Zaps.
{{% /accent-box %}}

## Check-In: Module 6 Complete

- [ ] At least one bank feed connected or importing into QBO test client
- [ ] Reconciliation Assistant Zap built with transaction matching logic
- [ ] AI analysis of unmatched transactions producing useful suggestions
- [ ] Reconciliation Report template created and generating documents
- [ ] Discrepancy Alert Zap built for large transactions
- [ ] All Zaps added to the Zapier Workflow Registry in Notion

6 checkmarks. Bank reconciliation is the proof of your value. Clients stay when their books match their bank.

---

# MODULE 7: FINANCIAL REPORTING — THE DELIVERABLE THAT SELLS

## Overview

Clients do not pay for bookkeeping. They pay for financial clarity. This module builds automated financial reporting — the monthly deliverable that proves your value and prevents churn. Every report you generate is a retention tool and a sales asset.

**Time to complete:** 3-4 hours
**Tools needed:** QuickBooks Online, Google Sheets, OpenAI API, Zapier, Notion

## Procedure 7.1: Build the Monthly Financial Report Generator

Create a new Zap: "Monthly Financial Report."

**Trigger:** Schedule by Zapier → 5th of every month at 7:00 AM WAT (gives you 5 days after month-end to complete reconciliation)

**Step 1:** QuickBooks Online → Run Reports (multiple API calls):
- Profit and Loss (current month)
- Profit and Loss (previous month, for comparison)
- Balance Sheet (as of month-end)
- A/R Aging Summary
- A/P Aging Summary

**Step 2:** Code by Zapier → Compile all report data into a structured object

**Step 3:** AI Narrative Generation
Add **ChatGPT** step:

- **Model:** `gpt-4o`
- **System Message:**

```
You are a CFO-level financial analyst for a Nigerian SME bookkeeping practice. Given financial statement data, write a clear, jargon-free financial summary for the business owner. Include:

1. **Revenue Performance** — How did revenue compare to last month? What changed?
2. **Expense Highlights** — Which expense categories grew? Which shrank? Any anomalies?
3. **Cash Position** — Is the business building cash or burning it? What is the runway?
4. **Receivables Risk** — How much is owed to the business? How much is overdue?
5. **Payables Pressure** — What bills are coming due? Any at risk of late payment?
6. **Key Metric** — Calculate: Current Ratio, Burn Rate (if applicable), Revenue per Employee (if headcount known)
7. **Action Items** — 3-5 specific, actionable recommendations based on the data

Tone: Professional but conversational. The reader is a business owner, not an accountant.
Currency: Nigerian Naira (₦)
Do not use accounting jargon without explanation.
```

**Step 4:** Generate the Report Document
Add **Google Docs** → **Create Document from Template**:

Use this template structure:

```
📊 MONTHLY FINANCIAL SUMMARY
[Client Name] — [Month Year]

REVENUE
Current Month: ₦[Amount]
Previous Month: ₦[Amount]
Change: [+/- ₦Amount / +/- X%]

EXPENSES
Current Month: ₦[Amount]
Previous Month: ₦[Amount]
Change: [+/- ₦Amount / +/- X%]

NET PROFIT
Current Month: ₦[Amount]
Margin: [X]%

CASH POSITION
Bank Balance: ₦[Amount]
[AI narrative summary]

ACCOUNTS RECEIVABLE
Total Outstanding: ₦[Amount]
Current: ₦[Amount]
1-30 Days Overdue: ₦[Amount]
31-60 Days Overdue: ₦[Amount]
60+ Days Overdue: ₦[Amount]

ACCOUNTS PAYABLE
Total Outstanding: ₦[Amount]
Due within 7 days: ₦[Amount]

KEY METRICS
Current Ratio: [X.X]
[Other metrics from AI]

ACTION ITEMS
1. [Specific recommendation]
2. [Specific recommendation]
3. [Specific recommendation]

---
Generated by [Your Practice Name]
Questions? Reply to this email or book a call: [Cal.com link]
```

**Step 5:** Gmail → Send the report as a PDF attachment to the client.

## Procedure 7.2: Build the Client Dashboard in Notion

For each client, create a Notion dashboard that provides real-time visibility into their financial health.

Open the **Clients** sub-page. Create a template for new client dashboards with these sections:

### Section 1: Financial Snapshot (Linked Database)
Create a linked view of your Revenue Tracker filtered to this client only.

### Section 2: Key Metrics Board
Add a callout block with these metrics (updated manually or via Zapier Notion integration):

| Metric | This Month | Last Month | Trend |
|---|---|---|---|
| Revenue | ₦[Auto] | ₦[Auto] | ↑↓→ |
| Net Profit | ₦[Auto] | ₦[Auto] | ↑↓→ |
| Cash Balance | ₦[Auto] | ₦[Auto] | ↑↓→ |
| A/R Outstanding | ₦[Auto] | ₦[Auto] | ↑↓→ |

### Section 3: Action Items Tracker
A to-do list with columns: Item, Priority, Due Date, Status, Notes

### Section 4: Document Repository
Links to: Latest monthly report, Current chart of accounts, Engagement letter, Tax filings

### Section 5: Communication Log
A table with columns: Date, Type (Email/Call/WhatsApp), Summary, Follow-Up Required

Share this dashboard with the client by clicking **Share** → **Share to web** or inviting their email. The client sees their financial health at a glance without logging into QBO. This alone justifies your monthly retainer.

## Procedure 7.3: Build the Tax Computation Helper

Nigerian SMEs must compute and remit VAT (7.5%), WHT (5-10%), PAYE (progressive), and Pension (8% employer + 10% employee). QBO does not do this natively. Build a Google Sheet that automates the computation.

### Create the Tax Computation Template

In Google Sheets, create a workbook with these tabs:

**Tab 1: VAT Computation**
| Column | Formula |
|---|---|
| Output VAT (7.5% of taxable sales) | =SUM(Sales)*7.5% |
| Input VAT (7.5% of taxable purchases) | =SUM(Purchases)*7.5% |
| VAT Payable | =Output_VAT - Input_VAT |
| VAT Filing Due Date | =EOMONTH(TODAY(),0)+21 |

**Tab 2: WHT Computation**
| Column | Formula |
|---|---|
| WHT on Contracts (5%) | =SUM(Contract_Payments)*5% |
| WHT on Rent (10%) | =SUM(Rent_Payments)*10% |
| Total WHT Deducted | =Sum of above |
| WHT Credit Note | =Total_WHT_Deducted |

**Tab 3: PAYE Computation (Nigeria 2024 Rates)**
Use the progressive tax bands:
- First ₦300,000: 7%
- Next ₦300,000: 11%
- Next ₦500,000: 15%
- Next ₦500,000: 19%
- Next ₦1,600,000: 21%
- Above ₦3,200,000: 24%

Build a formula that applies these bands to each employee's gross salary.

**Tab 4: Pension Computation**
- Employer: 8% of gross salary
- Employee: 10% of gross salary (deducted from salary)

Build a Zap that pulls transaction data from QBO monthly and populates this spreadsheet automatically. The Zap:
1. QuickBooks Online → Find Transactions (category: VAT, WHT, Salaries)
2. Code by Zapier → Classify and sum by tax type
3. Google Sheets → Update rows in the Tax Computation workbook

{{% accent-box %}}
**HACK:** Offer tax computation as a premium add-on for ₦50,000/month on top of the standard retainer. Most Nigerian SMEs pay an external tax consultant ₦100,000-200,000/year just for VAT returns. Your automated spreadsheet does it in 5 minutes per month. This is the highest-margin service in your entire practice.
{{% /accent-box %}}

## Check-In: Module 7 Complete

- [ ] Monthly Financial Report Generator Zap built and tested
- [ ] AI narrative producing clear, jargon-free financial summaries
- [ ] Report template created in Google Docs and generating PDFs
- [ ] Client Dashboard template created in Notion with all 5 sections
- [ ] Tax Computation spreadsheet built with VAT, WHT, PAYE, and Pension tabs
- [ ] Tax computation Zap pulling data from QBO to spreadsheet
- [ ] All Zaps added to the Zapier Workflow Registry in Notion

7 checkmarks. Financial reporting is what makes the client say "this is the best money I spend every month."

---

# MODULE 8: CLIENT ACQUISITION — THE MACHINE THAT FEEDS THE MACHINE

## Overview

You can automate bookkeeping. Now you need clients who will pay you to automate theirs. This module gives you the exact scripts, templates, and processes for acquiring bookkeeping clients consistently. No guessing. No hoping. Follow the procedures and clients will appear.

**Time to complete:** 6-8 hours (mostly prospect research and outreach)
**Tools needed:** Google Sheets, Gmail, Cal.com, Notion, Loom

## Procedure 8.1: Define Your Target Market

Pick one business category. Not five. Not three. One. The best categories for AI bookkeeping practices in Nigeria:

- Logistics and transportation companies (high transaction volume, many receipts)
- E-commerce stores (Shopify, WooCommerce, high invoice volume)
- Restaurants and food businesses (daily cash reconciliation nightmare)
- Real estate agencies (commission tracking, multiple payment channels)
- Professional services firms (law firms, consulting, project-based billing)
- Medical practices and pharmacies (inventory + service revenue)
- Construction companies (project cost tracking, vendor management)
- NGOs and nonprofits (donor reporting, grant compliance)

Write your chosen category on a sticky note. Put it on your monitor. Do not change it for 90 days. Niche focus is the single biggest advantage a new practice has — you learn the specific pain points, build reusable templates, and can speak their language from day one.

## Procedure 8.2: Build Your 50-Prospect List

Open Google Maps. Search for "[your category] in Lagos" (or your target city). You should see a list of businesses with names, addresses, phone numbers, and websites.

Create a Google Sheet called "Bookkeeping Prospect List" with columns: Business Name, Website, Contact Email, Contact Name, Current Bookkeeping Setup, Pain Point, Email Sent Date, Reply (Y/N), Meeting Booked (Y/N), Outcome.

Open each website and check:
1. Do they list an accountant or bookkeeper on their team? (If no, they probably need one)
2. Do they have a physical location? (If yes, they have rent and utilities — guaranteed bookkeeping complexity)
3. Are they on social media? (Active businesses generate more transactions)
4. Do they have multiple locations? (Multi-location = more bookkeeping pain)

Find 50 businesses. Yes, 50. This takes 3-4 hours. Do it in one sitting. Do not stop at 20.

Do you have 50 rows in your Prospect List? If you have fewer, go back to Google Maps and find more. 50 is the minimum for statistical significance.

## Procedure 8.3: Cold Outreach Script

Here is the script. Do not modify it until you have sent 50 emails and tracked the results:

**Subject line:** Your books are costing you money, [First Name]

**Body:**

> Hi [First Name],
>
> I noticed [specific observation — e.g., "you're running 3 locations across Lagos" or "your Instagram shows daily deliveries which means daily transactions that need tracking"].
>
> I run an AI-powered bookkeeping practice that automates the stuff most Nigerian businesses still do manually — transaction categorization, bank reconciliation, invoice processing, and monthly financial reporting. My system uses QuickBooks + AI to deliver accurate books in a fraction of the time, which means you get real-time financial clarity instead of waiting until tax season.
>
> I put together a quick demo showing how this works: [Loom video link — your walkthrough of the automation pipeline]
>
> Would it be worth a 20-minute chat to see if this could save [their business name] some serious time and money?
>
> [Your Name]
> [Your Practice Name]

Send this email to all 50 prospects. Use your professional email address. Send no more than 10 per day (to avoid spam filters). Space them throughout the day: 9 AM, 11 AM, 1 PM, 3 PM, 5 PM — two emails at each time slot.

**Expected results:** 8-12 replies (16-24% reply rate). 3-5 meetings booked. 1-2 clients closed.

If your reply rate is below 10% after 50 emails, the problem is one of three things:
1. Your subject line is landing in spam (check with mail-tester.com)
2. Your observation is not specific enough (generic observations = generic replies)
3. Your target market does not see the value (try a different category)

## Procedure 8.4: The Demo Call That Closes

When a prospect books a discovery call, follow this script:

**Minutes 0-5:** Introduce yourself briefly. Ask: "Before I show you anything, tell me — what is the most painful part of managing your business finances right now?" Listen. Take notes. Write their exact words — you will use these words in your proposal.

**Minutes 5-15:** Show your live demo. Open QBO with your test client's books. Show the auto-categorized transactions. Show the bank reconciliation matching. Show the monthly financial report. Show the Notion dashboard. The prospect should see a real system producing real financial data in real time.

**Minutes 15-25:** Ask: "How would this work for [their business]?" Let them imagine their own business running on this system. Ask: "How many bank accounts do you operate?" "How many invoices do you process per month?" "When did you last reconcile your books?" These questions reveal the depth of their pain.

**Minutes 25-30:** Present pricing. Use this exact framing:

"We have three tiers. Most of our clients start with the Growth tier at ₦200,000/month, which gives you full transaction automation, bank reconciliation, invoice processing, and monthly financial reporting. The setup fee is ₦300,000, which covers configuring QuickBooks, building your chart of accounts, and setting up all the automations."

If they say yes, send the Paystack payment link immediately. If they say "let me think about it," say: "Totally understand. I'll send you a summary email with a link to the demo video so you can share it with your team. What is the best way to follow up with you next week?"

## Procedure 8.5: The Three Pricing Tiers

Present three tiers to every prospect. The middle tier should feel like the obvious choice — this is the anchoring effect.

| Tier | Setup Fee | Monthly Retainer | What's Included | Your Time/Month |
|---|---|---|---|---|
| **Starter** | ₦150,000 | ₦75,000/mo | Basic transaction categorization + bank rec + monthly report | ~4 hours |
| **Growth** | ₦300,000 | ₦200,000/mo | Full automation (transactions, invoices, bank rec, AP aging) + monthly report + Notion dashboard | ~6 hours |
| **Enterprise** | ₦500,000 | ₦400,000/mo | Everything in Growth + tax computation + CFO-level advisory + priority support + weekly check-ins | ~10 hours |

**Effective hourly rates:** Starter = ₦18,750/hr | Growth = ₦33,333/hr | Enterprise = ₦40,000/hr

These rates are achievable because automated bookkeeping delivers measurable ROI. A ₦200,000/month bookkeeping service that saves a business owner 20 hours of manual work (worth ₦30,000-50,000 at staff rates) AND prevents tax penalties AND provides real-time financial clarity is worth 3-5x the fee.

{{% accent-box %}}
**HACK:** Always present the Growth tier first. Say: "Most of our clients start with the Growth tier at ₦200,000/month — it covers everything from transaction automation to monthly financial reporting." If they flinch, the Starter tier feels like a relief at ₦75,000. If they do not flinch, the Enterprise tier is the natural upsell. Never present the cheapest option first.
{{% /accent-box %}}

## Check-In: Module 8 Complete

- [ ] Target market chosen (one category, written on a sticky note)
- [ ] 50 prospects in your Prospect List spreadsheet
- [ ] Cold outreach script saved in Notion Templates
- [ ] Loom demo video recorded and linked in outreach emails
- [ ] First batch of 10 outreach emails sent
- [ ] Demo call script memorized or printed
- [ ] Pricing tiers configured in Paystack with payment links

7 checkmarks. The outreach emails are the hardest part — most people overthink and under-send. Send the emails.

---

# MODULE 9: DELIVERY & RETENTION — THE SYSTEM THAT KEEPS THEM PAYING

## Overview

Landing a client is 20% of the work. Delivering value month after month is 80%. This module gives you the exact delivery framework that keeps bookkeeping clients for 18+ months (instead of the industry average of 6-8 months).

**Time to complete:** Ongoing (4-10 hours per client per month after initial setup)

## Procedure 9.1: The First-Week Onboarding Protocol

**Day 1:** Send the welcome email with onboarding document. Schedule the kickoff call via Cal.com. Create a Google Drive folder for the client using this structure:

```
[Client Name]/
├── Onboarding/
├── Bank Statements/
├── Invoices/
├── Receipts/
└── Reports/
```

Also create the client's Notion dashboard (from the Module 7 template).

**Day 2: Kickoff Call (30 minutes)**
- Confirm the scope of work (which tier they purchased)
- Collect access credentials (QBO login, bank login, email for invoice forwarding)
- Review their existing chart of accounts (or start from your template)
- Ask: "What financial reports do you currently receive? What do you wish you received?"
- Set expectations: "You will receive your first automated monthly report within 2 weeks"

**Days 3-4:** Set up the Chart of Accounts in QBO (Procedure 3.2). Configure bank rules (Procedure 3.3). Connect bank feeds (Procedure 6.1).

**Day 5:** Build all Zapier workflows for this client:
- Transaction Categorization Pipeline (Procedure 4.1)
- Invoice Processing Pipeline (Procedure 5.1)
- Accounts Payable Aging (Procedure 5.3)
- Reconciliation Assistant (Procedure 6.2)
- Discrepancy Alert (Procedure 6.3, set threshold per client)
- Monthly Financial Report (Procedure 7.1)

**Day 6:** Internal testing. Run test transactions through every Zap. Verify QBO data matches. Check Slack alerts fire correctly.

**Day 7:** Client walkthrough via Loom video. Record yourself:
- Showing the QBO dashboard with auto-categorized transactions
- Explaining the invoice submission process
- Walking through the Notion dashboard
- Showing the monthly report template
- Explaining what to do if something looks wrong

Send the video and the engagement letter (from Notion Templates) to the client.

## Procedure 9.2: The Monthly Delivery Calendar

Every client receives these touchpoints every month:

| Week | Deliverable | Time Investment |
|---|---|---|
| Week 1 | Monthly Financial Report (auto-generated, reviewed by you) | 30 min review |
| Week 2 | Bank reconciliation completion + discrepancy resolution | 1-2 hours |
| Week 3 | Accounts Payable aging report + invoice processing review | 30 min |
| Week 4 | Check-in call (15-30 minutes) — review report, discuss questions, identify upsell | 15-30 min |

Total monthly time per Growth client: ~4 hours. At ₦200,000/month, that is ₦50,000/hour effective rate.

## Procedure 9.3: The Churn Prevention System

Client churn follows predictable patterns. Here are the warning signs and how to address each one:

**Warning Sign 1: Client stops responding to emails**
Action: Send a Loom video showing a reconciliation you just completed or a discrepancy you caught proactively. This reminds them of the value without requiring a response.

**Warning Sign 2: Client asks "What exactly do you do for us?"**
Action: Immediately send a comprehensive summary of all automation activity in the last 30 days: transactions categorized, invoices processed, reconciliation items resolved, tax computations completed. Quantify the hours saved. A client who asks this question has not seen your work recently — that is your failure, not theirs.

**Warning Sign 3: Client asks for a discount**
Action: Do not discount. Instead, offer to reduce scope: "We can move to the Starter tier at ₦75,000/month, which covers transaction categorization and monthly reporting only — no invoice processing, no dashboard, no tax computation. Would that work better?" Most clients will stay at the current tier rather than lose features.

**Warning Sign 4: Client's business is growing rapidly**
Action: This is NOT a churn risk — it is an upsell opportunity. Proactively suggest the Enterprise tier: "I noticed your transaction volume doubled this quarter. The Growth tier is designed for up to 200 transactions/month. You're at 350. Let me show you what the Enterprise tier includes for businesses at your scale."

**Warning Sign 5: Client's accountant or auditor questions your work**
Action: Invite the auditor to a call. Walk them through your processes, your automation logs, and your reconciliation procedures. Professional bookkeeping practices welcome scrutiny. If the auditor finds a genuine error, fix it immediately and add a new bank rule or Zapier validation to prevent recurrence. Document the fix in your SOP.

Log all churn warning signs in the Client Roster. Set the Health Score to Yellow or Red. Review weekly.

{{% accent-box %}}
**HACK:** Build a Zapier workflow that monitors client engagement. If a client has not opened your monthly report email in 2 consecutive months, automatically flag their Health Score as Yellow in your Notion Client Roster and send yourself a Slack reminder to schedule a check-in call. Silent disengagement is the number one predictor of churn.
{{% /accent-box %}}

## Check-In: Module 9 Complete

- [ ] First-week onboarding protocol documented as an SOP in Notion
- [ ] Monthly delivery calendar created for your first client
- [ ] Loom walkthrough video recorded and sent for first client
- [ ] Churn prevention system documented with all 5 warning signs and responses
- [ ] Engagement letter template saved in Notion Templates
- [ ] Client engagement monitoring Zap configured

6 checkmarks. The engagement letter and the Loom video are non-negotiable — they protect you legally and professionally.

---

# MODULE 10: SCALING OPERATIONS — FROM SOLO PRACTICE TO ₦10M/MONTH

## Overview

Solo operators hit a ceiling at ~8-10 clients (~₦1.6-2M/month). Breaking through requires systems and people. This module shows you exactly how and when to hire, what to delegate, and how to maintain margins as you grow to ₦10M/month in recurring revenue.

**Time to complete:** Ongoing (as you grow)

## Procedure 10.1: The Hiring Roadmap

**When you have 5 clients (₦1M/month MRR):** Hire a Virtual Assistant (VA) on Upwork or through Nigerian freelance platforms. Budget: ₦100,000-150,000/month, part-time. The VA handles:
- Client communication (responding to emails, scheduling calls)
- Invoice intake monitoring (checking WhatsApp groups, forwarding to Gmail)
- Bank statement downloads from client internet banking
- Data entry (updating Client Roster, logging test results)
- Basic QC (running test protocols, reporting failures to you)

**When you have 10 clients (₦2M/month MRR):** Hire a Junior Bookkeeper. Budget: ₦200,000-300,000/month, full-time. The Junior Bookkeeper handles:
- Manual reconciliation review (verifying AI-matched transactions)
- Invoice processing review (checking AI-extracted data before QBO entry)
- Monthly report formatting and distribution
- Client onboarding (following your onboarding SOP)
- Basic QBO configuration for new clients

**When you have 15 clients (₦3M/month MRR):** Hire a Salesperson. Budget: ₦150,000/month base + 10% commission on first-year client revenue. The Salesperson handles:
- Prospecting (building the 50-business list from Procedure 8.2)
- Cold outreach (sending the script from Procedure 8.3)
- Demo calls (following the script from Procedure 8.4)
- Pipeline management

**When you have 20+ clients (₦4M+/month MRR):** Hire a Senior Bookkeeper/Accountant. Budget: ₦350,000-500,000/month, full-time. This person handles:
- Complex reconciliation issues the Junior Bookkeeper cannot resolve
- Tax computation and filing oversight
- Advisory services (budgeting, forecasting, cash flow planning)
- Quality assurance across all clients
- Training and mentoring the Junior Bookkeeper

## Procedure 10.2: Margin Analysis at Scale

| Clients | Revenue/mo | Team Cost/mo | Tool Cost/mo | Net Profit/mo | Margin |
|---|---|---|---|---|---|
| 5 | ₦1,000,000 | ₦150,000 (VA) | ₦50,000 | ₦800,000 | 80% |
| 10 | ₦2,000,000 | ₦450,000 (VA + Junior) | ₦80,000 | ₦1,470,000 | 74% |
| 15 | ₦3,000,000 | ₦750,000 (VA + Junior + Sales) | ₦120,000 | ₦2,130,000 | 71% |
| 20 | ₦4,000,000 | ₦1,250,000 (VA + Jr + Sr + Sales) | ₦150,000 | ₦2,600,000 | 65% |
| 30 | ₦6,000,000 | ₦1,800,000 (Full team) | ₦200,000 | ₦4,000,000 | 67% |
| 50 | ₦10,000,000 | ₦3,500,000 (Full team + 2 Sr) | ₦350,000 | ₦6,150,000 | 62% |

Margins compress as you hire, but absolute profit increases. A 62% margin on ₦10,000,000 is ₦6,150,000/month — far more than a solo operator earning 80% on ₦1,000,000 (₦800,000/month).

## Procedure 10.3: Build the Internal Dashboard

Create a Notion page called `Practice Dashboard` that tracks:

### KPI Board

| Metric | Current | Target | Status |
|---|---|---|---|
| Active Clients | [Auto] | [Goal] | ↑↓→ |
| Monthly Recurring Revenue | ₦[Auto] | ₦[Goal] | ↑↓→ |
| Average Revenue Per Client | ₦[Auto] | ₦[Goal] | ↑↓→ |
| Client Churn Rate | [Auto]% | <5% | ↑↓→ |
| Automation Uptime | [Auto]% | 99%+ | ↑↓→ |
| Zapier Tasks Used | [Auto] | [Limit] | ↑↓→ |

### Client Health Overview
A linked view of the Client Roster filtered by Health Score: Red clients first, Yellow next, Green last.

### Revenue Trend
A linked view of the Revenue Tracker showing the last 6 months of MRR growth.

### Team Workload
A table showing each team member, their assigned clients, and their current capacity.

Update this dashboard weekly. It is your command center for scaling decisions.

## Procedure 10.4: Zapier Scaling Strategy

As you add clients, you will hit Zapier task limits. Here is the scaling plan:

| Zapier Plan | Tasks/mo | Cost/mo | Clients Supported |
|---|---|---|---|
| Free | 100 | ₦0 | 1-2 (testing only) |
| Starter | 750 | ₦15,000 | 3-5 |
| Professional | 2,000 | ₦35,000 | 5-10 |
| Team | 2,000+ | ₦50,000 | 10-15 |
| Company | 2,000+ | ₦75,000 | 15-25 |

**Optimization strategies to reduce task usage:**

1. **Consolidate Zaps per client:** Instead of 6 separate Zaps per client, build 2-3 multi-step Zaps that handle multiple functions.
2. **Batch processing:** Use Schedule triggers instead of real-time triggers where possible. A daily batch reconciliation uses 1 task instead of 30-50.
3. **Filter aggressively:** Add Filter steps early in each Zap to skip processing for transactions already handled by QBO bank rules.
4. **Use QBO bank rules first:** Push as much auto-categorization as possible into QBO's native bank rules (free) before routing to Zapier (paid).

## Procedure 10.5: The Vertical Expansion Playbook

Once you dominate one industry vertical, expand to adjacent verticals using your existing CoA templates and Zapier workflows as a foundation.

### Expansion Strategy

1. **Clone your Notion Client Dashboard** for the new vertical
2. **Clone and modify the Chart of Accounts** — add industry-specific accounts (e.g., for construction: Project Costs, Retention Money, Performance Bonds)
3. **Clone and modify the AI categorization prompts** — add industry-specific keywords and vendor names
4. **Update the bank rules** in QBO with industry-specific patterns
5. **Test with 2-3 pilot clients** at a discounted rate before full launch

### Vertical Expansion Sequence (Recommended)

| Phase | Vertical | Why It Works Next |
|---|---|---|
| Phase 1 | Your initial niche | Deep expertise, reusable templates |
| Phase 2 | Adjacent industry with similar CoA | e.g., restaurants → catering companies |
| Phase 3 | High-volume industry | e.g., e-commerce (highest transaction volume) |
| Phase 4 | Regulated industry (premium pricing) | e.g., NGOs, healthcare, financial services |

Each phase should add 5-10 clients before moving to the next. By Phase 4, you will have 20-40 clients and ₦4-10M/month in recurring revenue.

{{% accent-box %}}
**HACK:** Create a "Client Referral Program" that gives existing clients one free month of service for every referral that signs. At ₦200,000/month, one free month costs you ₦200,000 in revenue but the referral brings in ₦2,400,000 in first-year revenue. That is a 12:1 return. Most clients know other business owners in their industry — your best leads come from your best clients.
{{% /accent-box %}}

## Procedure 10.6: Build the Quality Assurance System

At scale, quality becomes your biggest risk. One reconciliation error across 30 clients is 30 potential churn events. Build a QA system:

### Weekly QA Checklist (Run Every Friday)

1. Check Zapier Workflow Registry — are any Zaps showing status "Broken"?
2. Check Slack `#automation-errors` — how many errors this week? Are any recurring?
3. Spot-check 5 random transactions per client in QBO — are they categorized correctly?
4. Review the Transaction Log spreadsheet — what is the AI categorization accuracy rate this week?
5. Review the Invoice Processing Log — any invoices stuck in "ERROR" status for more than 48 hours?
6. Check bank feeds — are all client bank feeds still connected and importing?
7. Review client Health Scores — any new Red or Yellow clients?

### Monthly QA Checklist (Run on the 5th)

1. Re-verify bank reconciliation for all clients (are the books still matching?)
2. Review AI categorization accuracy — if it dropped below 85%, add new bank rules or update the AI prompt
3. Review the Tax Computation spreadsheets — are the formulas still correct given any regulatory changes?
4. Check Zapier task usage — are you approaching your limit?
5. Review team workload — is anyone over capacity?

Document all QA findings in your Notion SOPs page under "QA Reports."

## Check-In: Module 10 Complete

- [ ] Hiring roadmap saved in Notion with trigger points for each hire
- [ ] Margin analysis table saved in Notion Finance page
- [ ] Practice Dashboard created in Notion with all 4 sections
- [ ] Zapier scaling plan documented with optimization strategies
- [ ] Vertical expansion plan written with target industries
- [ ] QA system documented with weekly and monthly checklists
- [ ] Client Referral Program created and added to Notion Templates

7 checkmarks. Scaling without systems is how practices die. Build the systems first, then grow into them.

---

# THE COMPLETE PLAYBOOK AT A GLANCE

You have now built the complete operating system for an AI bookkeeping automation practice. Here is what you have:

**10 Modules:**
1. Foundation — Command Center, financial infrastructure, communication stack
2. Tech Stack — QBO Accountant, Zapier, AI APIs, delivery tools
3. Chart of Accounts — Master template, QBO setup, bank rules
4. Transaction Automation — Categorization pipeline, confidence routing, weekly summaries
5. Invoice Processing — Capture pipeline, AI extraction, AP aging
6. Bank Reconciliation — Auto-matching, discrepancy alerts, reconciliation reports
7. Financial Reporting — Monthly reports, Notion dashboards, tax computation
8. Client Acquisition — Target market, prospect lists, outreach scripts, demo calls, pricing
9. Delivery & Retention — Onboarding protocol, monthly calendar, churn prevention
10. Scaling Operations — Hiring roadmap, margin analysis, QA system, vertical expansion

**35 Procedures executed across 10 modules.**

**6+ HACK tips embedded throughout.**

**3 Pricing Tiers:**

| Tier | Setup Fee | Monthly Retainer | Target Client |
|---|---|---|---|
| Starter | ₦150,000 | ₦75,000/mo | Small businesses, <50 transactions/month |
| Growth | ₦300,000 | ₦200,000/mo | Growing businesses, 50-200 transactions/month |
| Enterprise | ₦500,000 | ₦400,000/mo | Established businesses, 200+ transactions/month |

**Revenue Roadmap:**

| Milestone | Timeline | Revenue |
|---|---|---|
| First client | Month 1-2 | ₦275,000 (setup + first month) |
| 5 clients | Month 4-6 | ₦1,000,000/month MRR |
| 10 clients | Month 8-12 | ₦2,000,000/month MRR |
| 20 clients | Month 14-18 | ₦4,000,000/month MRR |
| 50 clients | Month 24-30 | ₦10,000,000/month MRR |

The system is built. The tools are connected. The scripts are written. The pricing is set. The only variable left is your execution. Start with Module 1. Do not skip. Do not abbreviate. Do every procedure. Check every box. The clients are waiting.
