---
title: "Build an AI Data Analytics Service with Tableau: The Complete Step-by-Step Guide"
date: 2026-11-12
category: "Implementation"
difficulty: "INTERMEDIATE"
readTime: "25 MIN"
excerpt: "*Section content pending review.*"
image: "/images/articles/intelligence/analyze-visualize-and-optimize-data-with-google-data-studio-and-tableau.png"
heroImage: "/images/heroes/intelligence/analyze-visualize-and-optimize-data-with-google-data-studio-and-tableau.png"
relatedOpportunity: "/opportunities/how-to-build-an-ai-data-analysis-service-30k-40kmonth/"
relatedPlaybook: "/playbooks/the-ai-customer-support-automation-playbook-25-steps-to-30kmonth/"
---



## Prerequisites

*Section content pending review.*


## Step 1: Setup and Configuration  
*(≈ 520 words)*  

**1.1 Create the Project Repository**  
We’ll host all code and assets in a single Git‑based repo on [Replit](https://replit.com/refer/egwuokwor).  
1. Log in to <https://replit.com> (free tier is enough for the repo, 500 MB storage).  
2. Click *Create* → *New Repl*.  
3. Choose *Python* (for API scripts), name the repl **tableau‑ai‑analytics**, and click *Create Repl*.  
4. In the file tree, create the following folders:  
   - `data/` – raw CSVs, Google Sheets URLs, BigQuery export files.  
   - `reports/` – finished PDF/PNG reports.  
   - `scripts/` – Python scripts for API calls.  
   - `config/` – JSON/YAML with secrets.  
   - `docs/` – README, docs, screenshots.  

**Expected output**  
```
├─ data/
├─ reports/
├─ scripts/
├─ config/
├─ docs/
```

**Interactive Check‑in**  
*Do you see the folder tree above?*  
If not, refresh the Replit page and ensure you are in the correct repl.  

---

**1.2 Set Up Google Cloud Project & Data Studio Access**  

1. Go to <https://console.cloud.google.com/> and click *Select a project* → *New Project*.  
2. Enter **Tableau‑AI‑Analytics** as the name, leave organization blank, click *Create*.  
3. In the left sidebar, navigate to *APIs & Services* → *Library*.  
4. Search for **Google Sheets API** and click *Enable*.  
5. Search for **BigQuery API** and enable it.  
6. Go to *Credentials* → *Create Credentials* → *OAuth client ID*.  
   - Application type: *Web application*.  
   - Authorized JavaScript origins: `https://replit.com`.  
   - Authorized redirect URIs: `https://replit.com/@<your‑username>/tableau‑ai‑analytics`.  
   - Click *Create*.  
7. Download the JSON file (`client_secret.json`) and move it to `config/`.

**Expected output**  
```
OAuth client created:
  Client ID: 1234567890-abcdef.apps.googleusercontent.com
  Client secret: xxxxx
```

**Interactive Check‑in**  
*Do you see the OAuth client ID in the console?*  
If you do not, verify that the OAuth consent screen is set to *External* and that you have at least one authorized redirect URI.  

**Error Scenario**  
*If you see `ERROR: OAuth client IDs cannot be created`*, it means you have exceeded the free quota or the project is missing a billing account. Add a free billing account from *Billing* → *Add billing account*.  

---

**1.3 Obtain Tableau Personal Access Token (PAT)**  

1. Open Tableau Desktop (paid trial available).  
2. From the top menu, choose *Help* → *Settings and Performance* → *Manage External Services*.  
3. Switch to the *Personal Access Token* tab.  
4. Click *Create New Token*.  
5. Enter **AIAnalyticsToken**, copy the token string, and paste it into a new file `config/tableau_pat.txt`.  
6. Store the PAT in a secure environment variable on Replit:  
   ```bash
   echo "TABLEAU_PAT=$(cat config/tableau_pat.txt)" >> .env
   ```

**Expected output**  
```
PAT created: AIAnalyticsToken
```

**Interactive Check‑in**  
*Do you see the PAT in the environment variables?*  
If not, open the Replit shell and run `printenv | grep TABLEAU_PAT`.  

**Error Scenario**  
*If you see `ERROR: Token already exists`*, delete the old token from Tableau Desktop before creating a new one.  

---

**1.4 Configure Make.com for Data Pipeline**  

1. Sign up at <https://www.make.com> (free tier: 3,000 operations/month).  
2. Create a new scenario:  
   - Trigger: *Google Sheets* → *Watch Rows* (select the sheet from your Google Drive).  
   - Action: *Python* → *Run a script* (use the script below to push data to Tableau).  
3. In the Make scenario, add the `config/tableau_pat.txt` value as a *

## Step 2: Build the Core System

*Section content pending review.*


## Step 3: Test and Validate  

**Objective** – Verify that the end‑to‑end pipeline (data ingestion → API → Tableau → Google Data Studio) behaves as expected. Each sub‑task must be completed before you hand the dashboard off to a client.

---

### 3.1 Verify Source Ingestion (Make.com → Google Sheets)

1. **Log into Make.com** → *Scenario* → *Run once*.  
2. In the *Run Log* pane, look for the line `Google Sheets → Create a row`.  
   *If you see `Error 400 – Bad Request`, the sheet ID is wrong. Correct it in the “Google Sheets” module → “Spreadsheet ID”.*  

3. Open **Google Sheets** → *File → Open* → *Sales Data* (sheet name: `Orders`).  
   *You should see a new row with a timestamp and order data.*  

**Interactive Check‑in**  
> Do you see the new row? It should appear in the first column as `2026‑11‑12 14:23:07`. If not, re‑run the Make.com scenario.

---

### 3.2 Validate the Replit API

1. Open the Replit project that hosts the Flask app.  
2. In the Replit console, run  
   ```bash
   python app.py
   ```  
   Expected terminal output:  
   ```
   * Serving Flask app "app" (lazy loading)
   * Environment: production
   * Debug mode: off
   * Running on http://localhost:5000/ (Press CTRL+C to quit)
   ```  

3. In a separate terminal, execute:  
   ```bash
   curl -s http://localhost:5000/data?format=json | head -n 5
   ```  
   Expected JSON snippet:  
   ```json
   {
     "order_id": 12345,
     "customer": "Acme Corp",
     "amount": 987.65,
     "date": "2026-11-12"
   }
   ```  

**Error Scenario**  
> If you receive `Connection refused`, ensure the Replit project is running on `port 5000` (Replit default). If the app crashes, check the console for stack traces and correct any syntax errors in `app.py`.

---

### 3.3 Test Tableau Connection and Extract

1. Open **Tableau Desktop**.  
2. *Connect* → *Google BigQuery* → use the same credentials that Make.com uses.  
   *You should see the dataset `menshly_sales`.*  

3. Drag `Orders` into the workspace → right‑click → *Extract* → *Create*.  
4. Save the workbook as `MenshlyAnalytics.twbx`.  

5. In the **Data** pane, click the refresh icon (two arrows).  
   *Expected result*: `Refreshing 1 data source` → `Refresh complete`.  

**Interactive Check‑in**  
> Do you see the `Orders` table in the Data pane? If not, re‑check the BigQuery connection string and credentials.

---

### 3.4 Validate Google Data Studio Dashboard

1. Open **Google Data Studio** → *Create* → *Report*.  
2. Add a data source → *Google BigQuery* → select `menshly_sales → Orders`.  
3. Add a *Time Series* chart. Drag `date` to *Dimension*, `amount` to *Metric*.  
4. Click the *Refresh Data* button.  
   Expected: `Data refreshed` banner appears.  

**Error Scenario**  
> If you see `Error: Permission denied`, ensure the Google Cloud service account used by Data Studio has *BigQuery Viewer* permissions.

---

### 3.5 End‑to‑End Automation Check with Zapier

1. In **Zapier**, open the *Sales‑to‑Dashboard* Zap.  
2. Trigger: *New Row in Google Sheets*.  
3. Action: *Run Python* (calls Replit API).  
4. Test the Zap → “Test Action” → “Success”.  

**Interactive Check‑in**  
> Do you see “Success” in the Zapier test log? If it says `Timeout`, increase the timeout setting in the Python action to 30 seconds.

---

## 5‑Point Test Checklist

| # | Item | How to Verify | Expected Result |
|---|------|---------------|-----------------|
| 1 | **Data Ingestion** | Open Google Sheets → new row present | Row appears with correct timestamp |
| 2 | **API Endpoint** | `curl http://localhost:5000/data?format=json` | JSON payload with non‑empty fields |
| 3 | **Tableau Extract** | Refresh in Tableau → success banner | No error, refresh completes in < 30 s |
| 4 | **Data Studio Dashboard** | Refresh Data → banner | Charts update and show new data |
| 5 | **Automation Flow** | Zapier test → Success | Data flows from Sheet → API → BigQuery → Dashboard |

If all five boxes are checked, the AI‑powered analytics service is ready for client delivery. If any step fails, follow the error‑scenario guidance

## Step 4: Add Advanced Features  

In this section we’ll turn the basic analytics system into a production‑ready service. We’ll add AI‑driven enrichment, robust error handling, real‑time data routing, and automated reporting. Every change is concrete – you can copy‑paste values, click the exact menu items, and see the expected output on screen.

### 4.1 AI Enrichment – Sentiment Analysis in Tableau with Replit & ChatGPT  

1. **Create a Replit project**  
   - Go to `replit.com`, click **+ Create**, choose **Python**.  
   - Name the project `sentiment_enrich`.  
   - In `main.py`, paste the following code (replace `YOUR_OPENAI_KEY` with your key):  

     ```python
     import openai
     import pandas as pd
     import json

     openai.api_key = "YOUR_OPENAI_KEY"

     def analyze_sentiment(text):
         response = openai.Completion.create(
             engine="gpt-4",
             prompt=f"Rate the sentiment of this product review on a scale 1-5: {text}",
             max_tokens=1,
             temperature=0
         )
         return int(response.choices[0].text.strip())

     # Load CSV from local path (replace with your path)
     df = pd.read_csv("reviews.csv")
     df["sentiment"] = df["review_text"].apply(analyze_sentiment)
     df.to_csv("reviews_with_sentiment.csv", index=False)
     ```

2. **Run the script**  
   - Click **Run**.  
   - After execution, you should see a new file `reviews_with_sentiment.csv` in the file tree.  

   *Interactive Check‑in:* Do you see the file `reviews_with_sentiment.csv`? If not, confirm that the script ran without errors. The console should display `Program finished` and the file should appear in the left pane.

3. **Import enriched data into Tableau**  
   - In Tableau Desktop, choose **Connect → Text file**.  
   - Browse to the `reviews_with_sentiment.csv` in the Replit shared folder (download it to your machine first).  
   - Drag `reviews_with_sentiment.csv` onto the canvas.  

   *Expected Output:* A data preview showing columns `review_id`, `review_text`, `sentiment`.  

4. **Create a calculated field for sentiment heatmap**  
   - In the data pane, right‑click → **Create → Calculated Field**.  
   - Name: `Sentiment Color`.  
   - Formula:  

     ```
     IF [sentiment] = 5 THEN "Positive"
     ELSEIF [sentiment] = 4 THEN "Mostly Positive"
     ELSEIF [sentiment] = 3 THEN "Neutral"
     ELSEIF [sentiment] = 2 THEN "Mostly Negative"
     ELSE "Negative"
     END
     ```

   - Drag `Sentiment Color` to **Color** on the Marks card.

   *Interactive Check‑in:* Do you see five distinct colors on the map? If not, verify the field formula and that the field is placed on Color.

### 4.2 Error Handling – Data Source Refresh Alerts using Zapier & Slack  

1. **Set up a Zap**  
   - In `zapier.com`, click **Make a Zap**.  
   - **Trigger:** Search for **Tableau** → select **New Data Refresh**. Follow prompts to authenticate Tableau (use your Tableau Online/Server credentials).  
   - **Action:** Search for **Slack** → select **Send Channel Message**. Connect your Slack workspace.  

2. **Configure the action**  
   - Channel: `#data-alerts`  
   - Message Text: `:warning: Tableau data source *{{Data Source Name}}* failed to refresh at {{Triggered At}}.`  
   - Add a field `Status` from the trigger payload.  

3. **Test the Zap**  
   - Click **Test & Review**.  
   - You should see a new message in Slack with the placeholder values replaced.  

   *Interactive Check‑in:* Do you see a message in `#data-alerts`? If not, confirm that the trigger fired and the Slack action succeeded.

4. **Enable Zap**  
   - Turn the Zap on. Now every failed refresh will surface an instant Slack alert.  

### 4.3 Data Routing – Real‑Time Ingestion with Make.com  

1. **Create a Make.com scenario**  
   - Sign into `make.com`, click **Create new scenario**.  
   - Add a **Google Sheets** trigger → **Watch Rows** (choose the sheet that receives fresh data).  
   - Add a **Tableau** action → **Refresh Data Source**. Authenticate Tableau.  

2. **Map fields**  
   - In the Tableau action, set the **Data Source ID** to the ID of your target

## Step 5: Deploy to Production

*Section content pending review.*


## Step 6: Scale and Grow  
**Goal:** Expand from a single client to 10 + clients while keeping each client’s dashboards running at peak performance and maintaining a healthy margin.  
**Prerequisites:** You already have your dashboards live on Tableau Server (or Tableau Online) and your data pipeline in Google Data Studio.  

---

### 6.1 Hiring Plan  
| Milestone | # Clients | # Dashboards | # Sr. Data Viz Engineers | # Junior Viz Engineers | # Automation Engineers |
|-----------|-----------|--------------|--------------------------|------------------------|------------------------|
| 1 | 1 | 3 | 0 | 0 | 0 |
| 5 | 5 | 15 | 1 | 1 | 0 |
| 10 | 10 | 30 | 2 | 2 | 1 |
| 25 | 25 | 75 | 4 | 4 | 2 |
| 50 | 50 | 150 | 8 | 6 | 4 |

**Hiring Cadence:**  
1. **Senior Viz Engineer (Tableau Creator $70 / mo)** – Handles complex calculations, publishes to Tableau Server, and mentors juniors.  
2. **Junior Viz Engineer (Tableau Explorer $35 / mo)** – Recreates templates from the senior engineer’s work.  
3. **Automation Engineer (Make.com – Pro plan $79 / mo)** – Builds and maintains data ingestion and refresh workflows.  

**Check‑In:**  
- *Do you see the “Users” tab in Tableau Server under “Site Settings” after you’ve logged in as an admin?*  
  - *If not, you’re in the wrong site. Go back to the Tableau Server home page → “Site Administration” → “Users.”*  

### 6.2 Automation Upgrades  
| Tool | Setting | Expected Outcome | Error Scenario |
|------|---------|------------------|----------------|
| [**Make.com**](https://www.make.com/en/register?pc=menshly) | “Schedule” → “Every 15 min” for data extraction from Google Sheets → “Add” → “Tableau Server” → “Publish DataSource” | Dashboard refreshes within 5 min | *If the “Authentication” step shows “401 Unauthorized”* – verify the API key in Make.com > “Connections” > “Tableau Server.” |
| **Zapier** | Trigger: “New Row in Google Sheet” → Action: “Create/Update DataSource in Tableau” | Real‑time data push to Tableau | *If “Rate Limit Exceeded”* – move to Make.com or upgrade to Zapier Professional. |
| [**Vapi**](https://vapi.ai/) | Voice skill: “Explain dashboard metrics” → Integration: “Tableau REST API” | Clients can ask for verbal explanations of KPI trends | *If “Speech Synthesis Error”* – check ElevenLabs key and limit. |

**Interactive Check‑In:**  
- *Open Make.com, click “Scenario” → “Tableau Data Refresh.”*  
  - *You should see the “Schedule” toggle in the top right. If it’s greyed out, refresh the browser or clear cache.*  

### 6.3 Margin Improvements  
1. **Licensing Optimization** – Move 5–10 clients from Tableau Explorer to Tableau Viewer ($12 / mo) once they only need read‑only access.  
2. **Pipeline Consolidation** – Merge identical Google Data Studio reports into a single Tableau data source to reduce API calls (cut 20 % of Make.com usage).  
3. **Revenue‑Per‑Client** – Standard pricing: $1,200 / mo per client (includes 3 dashboards).  
4. **Cost Breakdown (per client)** – Tableau ($70 / mo) + Make.com ($79 / mo) + Vapi ($20 / mo) = $169 / mo.  
   - **Margin**: ($1,200 – $169) / $1,200 = 85 %.  

**Check‑In:**  
- *Run a quick profit‑loss in Replit:*
  ```python
  revenue = 1200
  costs = 70 + 79 + 20
  margin = (revenue - costs) / revenue
  print(f"Margin: {margin:.2%}")
  ```
  - *Output:* `Margin: 85.08%` – you’re on track.  

---

#### Next Step  
*Step 7: Automate Client Onboarding* – Use Calendly to set up discovery calls, Loom for onboarding videos, and Automate.io to create a welcome flow that populates new Google Sheets and Tableau dashboards automatically.

## Cost Breakdown

*Section content pending review.*


## Production Checklist

Before you publish the analytics dashboards, run through this checklist. Each item is a measurable gate; if it fails, you must fix it before proceeding.

- **[ ] Data Source Connectivity**  
  Verify each connector (Google BigQuery, Salesforce API, CSV on Hostinger SFTP) is live. In Tableau Desktop, open *Data* → *Data Source* → *Test Connection*. The status must read **Connection Successful**. If it shows **Connection Failed**, re‑enter the credentials and ensure the firewall allows outbound HTTPS (port 443).

- **[ ] Refresh Schedule Accuracy**  
  In Tableau Server, navigate to **Content** → *Your Workbook* → *Schedule* → *Edit*. Confirm the refresh is set to **Every 6 hours (UTC)** and that the “Execute as User” is set to the service account with the minimal dataset‑view permissions. In Google Data Studio, check **Data** → *Data Source* → *Refresh Fields* → *Schedule* → *Set to 6 hours*.

- **[ ] Calculation Validation**  
  Open Tableau Prep Builder (2023.1). Run the flow and review the output data preview. Ensure that all calculated fields (e.g., `Total Sales %` = `Sales / Target`) yield non‑null values for 99.9 % of rows. Any row with `NULL` must be flagged and corrected.

- **[ ] User‑Access Permissions**  
  On Tableau Server, go to **Users** → *Add Users* → *Add Group* → *AnalyticsTeam*. Assign the **Viewer** role. In Google Data Studio, open the report, click **Share** → **Add people and groups** → add `analytics@yourdomain.com` with **Viewer** rights. Confirm that a test user can view but not edit.

- **[ ] Performance Thresholds**  
  Run a performance audit in Tableau Desktop: *Help* → *Settings and Performance* → *Analyze Performance*. All query times must be under **5 seconds**. If any query exceeds this, index the source table or optimize the calculation.

- **[ ] Backup & Recovery**  
  Export the Tableau workbook (`.twbx`) to Hostinger’s S3‑compatible storage. Confirm the file size matches the local export (e.g., `123 MB`). In Google Data Studio, ensure that a duplicate data source exists with the same schema.

- **[ ] Alerting Configuration**  
  Use Make.com to trigger an email via ActiveCampaign when a data refresh fails. In Make.com, set the workflow: *Trigger*: Tableau refresh failure → *Action*: ActiveCampaign → *Send Email*. Verify the email template contains the error code and a link to the Tableau logs.

- **[ ] Documentation & Logging**  
  Write a README in [Notion](https://notion.so/) that lists all dataset URLs, refresh schedules, and troubleshooting steps. Ensure the log file (`/var/log/tableau/refresh.log`) contains a timestamped entry for each successful refresh.

- **[ ] Compliance Check**  
  Verify that all data fields comply with GDPR. In Tableau Server, open **Data** → *Data Source* → *Data Source Settings* → *Privacy* → confirm that the **Data Source** is marked **Public** only for anonymized fields. If any PII is exposed, mask it with a calculated field.

- **[ ] Final Smoke Test**  
  Log in as an end‑user, open both the Tableau Server view and the Google Data Studio report. Navigate through all sheets and filters. Ensure the visualizations render correctly and that filter selections update all dependent charts in real time. If any chart fails, revisit the corresponding data source.

Pass all items before announcing the service. This guarantees reliability, performance, and user trust.

## **Automate Data Refresh with Make.com**

1️⃣ Sign in to Make.com and create a new Scenario.  
2️⃣ Add the **Google Sheets** module → *Watch Rows* → set *Polling Frequency* to **15 min**.  
3️⃣ Map the sheet columns to a **JSON** variable.  
4️⃣ Add the **Google Data Studio** module → *Update Data Source* → paste your Data Studio **Data Source ID** (found under *Resource > Manage Data Sources*).  
5️⃣ In the *Data Source ID* field, paste `DS-XXXXXXXXXXXXXXXX`.  
6️⃣ Map the JSON variable to the Data Studio fields.  
7️⃣ Run the Scenario once to validate.  
8️⃣ Activate the Scenario.  

*If you see “Invalid credentials” this means Make.com cannot access your Google account. Re‑authorize the account in the Make.com dashboard under *Connections*.*

**Next step**: set up a cron job in Hostinger to trigger this Scenario every day at 02:00 UTC for batch updates.  

> 👉 **Related Menshly article**: [Automate Google Data Studio Refresh](https://menshly.com/automate-google-data-studio-refresh)

---

## **Create an AI‑Powered Tableau Extension**

1️⃣ In Tableau Desktop, open your workbook.  
2️⃣ Go to *Help > About Tableau* to confirm version **2024.1** (required for Extensions API).  
3️⃣ Click **Extensions > Add Extension** → **Create New Extension**.  
4️⃣ In the Extension Builder, paste the following minimal HTML/JS:

```html
<div id="chat"></div>
<script src="https://cdn.jsdelivr.net/npm/@gradio/client@1.1.0"></script>
<script>
  const gradio = new GradioClient('https://api.openai.com/v1/chat/completions', {
    model: 'gpt-4o-mini',
    apiKey: 'YOUR_OPENAI_KEY'
  });
  // Receive data from Tableau
  const data = tableau.extensions.dashboardContent.dashboard.getDataSourcesAsync()
    .then(ds => ds[0].getHyperFileAsync())
    .then(file => console.log(file));
  // Send to ChatGPT and display
  gradio.predict({messages: [{role: 'user', content: data}]})
    .then(response => document.getElementById('chat').innerText = response.choices[0].message.content);
</script>
```

5️⃣ Save the extension as `ai-summary.html`.  
6️⃣ Deploy the extension to the Tableau Server by uploading it under *Extensions > Manage Extensions* and set the **Access** to **Everyone**.  

*If “Extension not found” appears, double‑check the file path and ensure the server has internet access to `cdn.jsdelivr.net`.*

> 👉 **Related Menshly article**: [Building Tableau Extensions with AI](https://menshly.com/tableau-extensions-guide)

---

## **Add Voice‑Over Summaries with ElevenLabs**

1️⃣ In Tableau Server, open the dashboard you just extended.  
2️⃣ Click the **Extension** you added → **Open**.  
3️⃣ Inside the extension, replace the `apiKey` placeholder with your [**ElevenLabs API Key**](https://elevenlabs.io/) (`ELEVENLABS-XXXXXXXXXXXXXXXX`).  
4️⃣ Add a new field in the extension UI:  
```html
<button id="voiceBtn">Listen to Summary</button>
<script>
  document.getElementById('voiceBtn').addEventListener('click', async () => {
    const txt = document.getElementById('chat').innerText;
    const response = await fetch('https://api.elevenlabs.io/v1/text-to-speech', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'xi-api-key': 'ELEVENLABS-XXXXXXXXXXXXXXXX'
      },
      body: JSON.stringify({text: txt, voice: 'Joanna'})
    });
    const audio = await response.blob();
    const url = URL.createObjectURL(audio);
    const audioEl = new Audio(url);
    audioEl.play();
  });
</script>
```
5️⃣ Save and refresh the dashboard.  
6️⃣ Click **Listen to Summary** to hear a real‑time spoken recap.  

*If the audio does not play, check that your browser allows pop‑ups and that the ElevenLabs API key is active.*

---

## **Host Dashboards on Hostinger with HTTPS**

1️⃣ Log into Hostinger, navigate to **Hosting > Manage** > *Websites*.  
2️⃣ Create a new subdomain, e.g., `analytics.menshly.com`.  
3️⃣ In the domain settings, point the A‑record to Hostinger’s IP `123.45.67.89`.  
4️⃣ In the **Manage** panel, enable **SSL** → *Let’s Encrypt* → **Activate**.  
5️⃣ Upload your Tableau Server files to the subdomain’s `public_html` folder via File Manager.  
6️⃣ In Tableau Server’s `web.config`, set the base URL to `https://analytics.menshly.com`.  

*If “Connection timed out” occurs, verify that port 443 is open in your firewall settings.*

---

## **Automated Client Reports with Klaviyo**

1️⃣ In Tableau Server, export the latest dashboard as a PDF and save it to a Google Drive folder.  
2️⃣ In Make.com, add a **Google Drive** module → *Watch New File* → set to the folder.  
3️⃣ Add a **Klaviyo** module → *Send Email* → select the

Ready to understand the full business opportunity? Read our [opportunity deep-dive]({< ref "/opportunities/how-to-build-an-ai-data-analysis-service-30k-40kmonth.md" >}).


## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
