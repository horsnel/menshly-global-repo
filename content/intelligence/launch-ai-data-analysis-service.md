---
title: "Build an AI Data Analysis Service with ChatGPT: The Complete Step-by-Step Guide"
date: 2026-04-24
category: "Implementation"
difficulty: "INTERMEDIATE"
readTime: "28 MIN"
excerpt: "The complete execution guide for building an AI-powered data analysis service — from setting up your tool stack to delivering your first client report to scaling with automation."
image: "/images/articles/intelligence/launch-ai-data-analysis-service.png"
heroImage: "/images/heroes/intelligence/launch-ai-data-analysis-service.png"
relatedOpportunity: "/opportunities/ai-data-analysis-service/"
relatedPlaybook: "/playbooks/ai-side-hustle-blueprint/"
---

You are going to build an AI data analysis service. Not a blog about data. Not a course about data. A service that takes a business's raw data, extracts insights, and delivers recommendations they can act on — for money. This guide covers every step. Every tool. Every setting. Every optimization. Follow it in order. Do not skip steps.

## Prerequisites

Before you write a single line of code or talk to a single client, you need the following tools set up and accounts created. Do not proceed until every item is checked.

- **A laptop with at least 8GB RAM** — You will run Jupyter notebooks locally. 4GB machines will choke on datasets over 50,000 rows.
- **Python 3.11 or later installed** — Go to python.org/downloads. Download the installer for your OS. Run it. On Windows, check the box that says "Add Python to PATH." On Mac, use the installer. Verify by opening a terminal and typing `python --version`. You should see `Python 3.11.x` or higher. If you see `Python 2.x`, something is wrong — reinstall and check the PATH box.
- **A ChatGPT Plus account ($20/mo)** — Go to chat.openai.com. Sign up. Click "Upgrade to Plus." You need the Code Interpreter (Advanced Data Analysis) feature, which is Plus-only. This is non-negotiable. The free tier does not support file uploads or code execution.
- **A Jupyter Notebook environment** — Open your terminal and run: `pip install jupyterlab pandas plotly openpyxl scipy scikit-learn`. This installs JupyterLab, Pandas (data manipulation), Plotly (interactive charts), openpyxl (Excel file reading), SciPy (statistics), and scikit-learn (machine learning). Wait for the install to complete. Verify by running `jupyter lab` — a browser window should open with the Jupyter interface.
- **A Google Sheets account (free)** — Go to sheets.google.com. You will use this for quick data previews and sharing with clients who live in Google Workspace.
- **A Notion account (free tier)** — Go to notion.so. Sign up. You will use this for client onboarding forms, project tracking, and report templates.
- **A Canva account (free tier)** — Go to canva.com. Sign up. You will use this for presentation-quality report covers and infographics.
- **A Make.com account (free tier)** — Go to make.com. Sign up. You will use this for automating data pipelines and report delivery later.
- **A Stripe account (free)** — Go to stripe.com. Sign up. You will use this to collect payments from clients.
- **4-6 hours of uninterrupted time for setup and your first practice analysis**

Total upfront cost: $20 for ChatGPT Plus. Everything else is free until you have paying clients.

## Step 1: Configure Your Python Analysis Environment

Open your terminal. Navigate to the directory where you want your projects to live. Create a project folder:

```bash
mkdir ai-data-analysis
cd ai-data-analysis
mkdir templates clients output
```

You should now have three subdirectories: `templates/` (for reusable analysis scripts), `clients/` (for client data and work), and `output/` (for generated reports and charts). If you are missing any of these, create them now.

### Set Up a Virtual Environment

Run this in your terminal:

```bash
python -m venv venv
```

On Windows, activate it:
```bash
venv\Scripts\activate
```

On Mac/Linux, activate it:
```bash
source venv/bin/activate
```

You should see `(venv)` at the start of your terminal prompt. Do you see it? If not, the virtual environment is not active. Stop and fix this before proceeding. Running without a virtual environment will pollute your system Python and create dependency nightmares later.

Now install your analysis stack inside the virtual environment:

```bash
pip install jupyterlab pandas plotly openpyxl scipy scikit-learn kaleido nbconvert
```

The `kaleido` package exports Plotly charts as static images. The `nbconvert` package converts Jupyter notebooks to HTML and PDF. Both are essential for client deliverables.

Verify the installation. Run:

```bash
python -c "import pandas; import plotly; import scipy; import sklearn; print('All packages installed successfully')"
```

You should see `All packages installed successfully`. If you get an `ImportError`, that specific package failed to install. Run `pip install [package-name]` again and check for error messages.

### Create Your Jupyter Configuration

Run:

```bash
jupyter lab --generate-config
```

This creates a config file at `~/.jupyter/jupyter_lab_config.py`. Open it in a text editor. Find the line that says `# c.ServerApp.port = 0` and change it to:

```python
c.ServerApp.port = 8888
```

Find `# c.ServerApp.open_browser = True` and change it to:

```python
c.ServerApp.open_browser = True
```

Save the file. Now when you run `jupyter lab`, it will always open on port 8888 and launch your browser automatically.

### Start Jupyter and Create Your First Notebook

Run:

```bash
cd ai-data-analysis
jupyter lab
```

A browser tab should open with the JupyterLab interface. In the left sidebar, you should see your `templates/`, `clients/`, and `output/` folders. Click the `+` icon in the top-left to create a new Notebook. Select Python 3 (your venv kernel). Name the notebook `analysis-template.ipynb` and save it in the `templates/` folder.

In the first cell, paste this boilerplate and run it (Shift+Enter):

```python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.float_format', '{:.2f}'.format)

print("Analysis environment ready.")
```

You should see `Analysis environment ready.` printed below the cell. Do you? If you get an import error, go back and reinstall the missing package. If you see a warning about deprecated features, ignore it — that is normal.

### CHECK-IN: Step 1 Complete

Verify each of these before moving on:

1. Virtual environment is active (`(venv)` in your terminal prompt)
2. All Python packages import without errors
3. Jupyter Lab opens on port 8888
4. Your `analysis-template.ipynb` notebook runs the boilerplate cell successfully
5. Your directory structure has `templates/`, `clients/`, and `output/` folders

If all 5 pass, move to Step 2. If any fail, stop and fix them now. A broken environment will waste hours later.

## Step 2: Master the ChatGPT Code Interpreter Pipeline

ChatGPT's Code Interpreter is your fastest path from raw data to initial insights. You will use it for every new client dataset before you touch Jupyter. It handles the exploratory analysis in minutes instead of hours. Here is the exact prompt sequence you will run for every new dataset.

### Upload and Describe

Open ChatGPT. Click the paperclip icon (or the `+` button) in the message input. Upload your client's CSV or Excel file. Type this prompt:

> Analyze this dataset. Provide: (1) Total rows and columns, (2) Data type for each column, (3) Count of missing values per column, (4) Count of duplicate rows, (5) Basic statistics for numeric columns (mean, median, std, min, max), (6) Count of unique values for categorical columns, (7) The 3 most obvious data quality issues you can identify.

ChatGPT will write and execute Python code to analyze your dataset. It will return a structured summary. Save this summary — you will include it in your client's data audit report.

### Identify Patterns and Anomalies

In the same conversation, type this prompt:

> Identify the 10 most interesting patterns, correlations, or anomalies in this data. For each one: (1) Describe the pattern in plain English, (2) Provide the statistical evidence (correlation coefficient, p-value, or relevant metric), (3) Rate the business impact as HIGH, MEDIUM, or LOW, (4) Suggest one specific action the business should take based on this finding.

ChatGPT will run correlation analysis, outlier detection, and trend identification. It will prioritize findings by business impact. This output is the backbone of your deliverable.

### Generate Visualizations

Type this prompt:

> Create 5 visualizations that tell the most compelling story from this data. Use Plotly for all charts. Each chart must have: a clear title, axis labels, and a 2-sentence annotation explaining what the chart shows and why it matters. Save each chart as a PNG at 1200x800 resolution.

ChatGPT will generate the charts and download them as files. Save each PNG to your `output/` folder. You will include these in your client presentation.

### Develop Recommendations

Type this prompt:

> Based on all the patterns and anomalies you found, create a prioritized list of 7 recommendations for this business. For each recommendation: (1) State the recommendation in one sentence, (2) Explain the data evidence supporting it, (3) Estimate the expected business impact (revenue increase, cost reduction, or risk mitigation), (4) Rate the implementation difficulty as EASY, MEDIUM, or HARD, (5) Suggest a timeline for implementation.

This is the section your client cares about most. Every recommendation must tie directly to data. No fluff. No vague advice. "Change X because the data shows Y, expect Z impact."

### Export the Full Analysis

Type this prompt:

> Compile all your findings into a structured report with these sections: Executive Summary (3 key findings), Data Quality Assessment, Key Patterns and Anomalies (top 10), Visualizations (embed all 5 charts with annotations), Recommendations (prioritized list of 7), and Appendix (full statistical output). Export as a PDF.

ChatGPT will generate a PDF. Download it and save it to your `output/` folder. This is your first draft deliverable. You will refine it in Jupyter for the final version.

### CHECK-IN: Step 2 Complete

1. You can upload a CSV to ChatGPT and get a structured data summary
2. You can generate a prioritized list of patterns with statistical evidence
3. You can produce 5 annotated visualizations via Plotly
4. You can generate actionable recommendations tied to data
5. You can export the full analysis as a PDF

If all 5 pass, move to Step 3. If any fail, practice with a sample dataset from Kaggle (kaggle.com/datasets — search for "sales data" and download any CSV with 1,000+ rows) until you are confident.

## Step 3: Build Reusable Analysis Templates

Templates are your competitive advantage. Without templates, every client project starts from scratch. With templates, you cut build time from 10 hours to 2. You are going to build three templates that cover 80% of client requests: sales analysis, customer segmentation, and financial reporting.

### Template 1: Sales Analysis

Create a new Jupyter notebook. Save it as `templates/sales-analysis.ipynb`. This template analyzes sales data to identify revenue trends, top products, seasonal patterns, and growth opportunities.

Paste this into the first cell:

```python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
import numpy as np
import warnings
warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.2f}'.format)

# ============================================
# SALES ANALYSIS TEMPLATE
# ============================================
# Expected columns (rename your client's columns to match):
# - date: order/purchase date (datetime)
# - product: product name or SKU (string)
# - category: product category (string)
# - quantity: units sold (numeric)
# - revenue: total revenue per line item (numeric)
# - customer_id: unique customer identifier (string)
# - region: geographic region (string)

# LOAD DATA
# Replace 'path' with your client's file path
df = pd.read_csv('clients/CLIENT_NAME/data.csv', parse_dates=['date'])
print(f"Dataset loaded: {len(df):,} rows, {len(df.columns)} columns")
print(f"Date range: {df['date'].min()} to {df['date'].max()}")
```

In the second cell, add data cleaning:

```python
# DATA CLEANING
# Remove duplicates
initial_rows = len(df)
df = df.drop_duplicates()
print(f"Removed {initial_rows - len(df)} duplicate rows")

# Handle missing values
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
print("\nMissing values (%):")
print(missing_pct[missing_pct > 0])

# Fill or drop missing values based on column type
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

categorical_cols = df.select_dtypes(include=['object']).columns
df[categorical_cols] = df[categorical_cols].fillna('Unknown')

# Validate data types
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')

# Remove rows with invalid dates or negative revenue
df = df.dropna(subset=['date'])
df = df[df['revenue'] >= 0]

print(f"\nCleaned dataset: {len(df):,} rows")
```

In the third cell, add the revenue trend analysis:

```python
# REVENUE TREND ANALYSIS
df['month'] = df['date'].dt.to_period('M').astype(str)
df['week'] = df['date'].dt.to_period('W').astype(str)

monthly_revenue = df.groupby('month')['revenue'].sum().reset_index()
monthly_revenue['mom_change'] = monthly_revenue['revenue'].pct_change() * 100

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=monthly_revenue['month'],
    y=monthly_revenue['revenue'],
    mode='lines+markers',
    name='Monthly Revenue',
    line=dict(color='#2563EB', width=3),
    marker=dict(size=8)
))
fig.add_trace(go.Bar(
    x=monthly_revenue['month'],
    y=monthly_revenue['mom_change'],
    name='MoM Change %',
    yaxis='y2',
    marker_color=np.where(monthly_revenue['mom_change'] >= 0, '#10B981', '#EF4444')
))
fig.update_layout(
    title='Monthly Revenue Trend & Month-over-Month Change',
    xaxis_title='Month',
    yaxis_title='Revenue ($)',
    yaxis2=dict(title='MoM Change %', overlaying='y', side='right'),
    template='plotly_white',
    height=500
)
fig.show()
fig.write_image('output/revenue_trend.png', width=1200, height=800, scale=2)

# Calculate key metrics
total_revenue = df['revenue'].sum()
avg_monthly = monthly_revenue['revenue'].mean()
best_month = monthly_revenue.loc[monthly_revenue['revenue'].idxmax()]
worst_month = monthly_revenue.loc[monthly_revenue['revenue'].idxmin()]
avg_order_value = df['revenue'].mean()

print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Average Monthly Revenue: ${avg_monthly:,.2f}")
print(f"Best Month: {best_month['month']} (${best_month['revenue']:,.2f})")
print(f"Worst Month: {worst_month['month']} (${worst_month['revenue']:,.2f})")
print(f"Average Order Value: ${avg_order_value:,.2f}")
```

In the fourth cell, add the product and category analysis:

```python
# PRODUCT & CATEGORY ANALYSIS
# Top 10 products by revenue
top_products = df.groupby('product').agg(
    revenue=('revenue', 'sum'),
    quantity=('quantity', 'sum'),
    orders=('revenue', 'count')
).sort_values('revenue', ascending=False).head(10)

fig = px.bar(
    top_products.reset_index(),
    x='product',
    y='revenue',
    title='Top 10 Products by Revenue',
    color='revenue',
    color_continuous_scale='Blues'
)
fig.update_layout(xaxis_title='Product', yaxis_title='Revenue ($)', template='plotly_white', height=500)
fig.show()
fig.write_image('output/top_products.png', width=1200, height=800, scale=2)

# Pareto analysis: what % of revenue comes from top 20% of products?
product_revenue = df.groupby('product')['revenue'].sum().sort_values(ascending=False)
cumulative_pct = product_revenue.cumsum() / product_revenue.sum() * 100
top_20_pct_count = max(1, int(len(product_revenue) * 0.2))
top_20_revenue_share = cumulative_pct.iloc[top_20_pct_count - 1]

print(f"\nPareto Analysis: Top 20% of products ({top_20_pct_count} products) generate {top_20_revenue_share:.1f}% of revenue")
print(f"\nTop 10 Products:")
print(top_products.to_string())
```

In the fifth cell, add seasonal pattern detection:

```python
# SEASONAL PATTERN DETECTION
df['day_of_week'] = df['date'].dt.day_name()
df['hour'] = df['date'].dt.hour if 'hour' in df.columns or df['date'].dt.hour.nunique() > 1 else None

day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dow_revenue = df.groupby('day_of_week')['revenue'].sum().reindex(day_order)

fig = px.bar(
    x=dow_revenue.index,
    y=dow_revenue.values,
    title='Revenue by Day of Week',
    labels={'x': 'Day of Week', 'y': 'Revenue ($)'},
    color=dow_revenue.values,
    color_continuous_scale='Blues'
)
fig.update_layout(template='plotly_white', height=400, showlegend=False)
fig.show()
fig.write_image('output/day_of_week_revenue.png', width=1200, height=600, scale=2)

peak_day = dow_revenue.idxmax()
slowest_day = dow_revenue.idxmin()
print(f"Peak day: {peak_day} (${dow_revenue[peak_day]:,.2f})")
print(f"Slowest day: {slowest_day} (${dow_revenue[slowest_day]:,.2f})")
print(f"Revenue gap: {((dow_revenue[peak_day] - dow_revenue[slowest_day]) / dow_revenue[slowest_day] * 100):.1f}%")
```

Save the notebook. This template is your starting point for any client with sales data.

### Template 2: Customer Segmentation

Create a new notebook. Save it as `templates/customer-segmentation.ipynb`. This template segments customers by behavior and value, identifying who to retain, who to grow, and who to let go.

First cell — load and prepare:

```python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
import warnings
warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.2f}'.format)

# ============================================
# CUSTOMER SEGMENTATION TEMPLATE
# ============================================
# Expected columns:
# - customer_id: unique customer identifier
# - date: transaction date
# - revenue: transaction revenue
# - product: product name (optional)

df = pd.read_csv('clients/CLIENT_NAME/data.csv', parse_dates=['date'])
print(f"Dataset loaded: {len(df):,} transactions")
```

Second cell — RFM analysis (Recency, Frequency, Monetary):

```python
# RFM ANALYSIS
analysis_date = df['date'].max() + pd.Timedelta(days=1)

rfm = df.groupby('customer_id').agg(
    recency=('date', lambda x: (analysis_date - x.max()).days),
    frequency=('date', 'count'),
    monetary=('revenue', 'sum')
).reset_index()

# Score each dimension 1-5 (5 is best)
rfm['r_score'] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1]).astype(int)
rfm['f_score'] = pd.qcut(rfm['frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5]).astype(int)
rfm['m_score'] = pd.qcut(rfm['monetary'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5]).astype(int)

rfm['rfm_score'] = rfm['r_score'] * 100 + rfm['f_score'] * 10 + rfm['m_score']

# Segment customers
def segment_customer(row):
    if row['r_score'] >= 4 and row['f_score'] >= 4 and row['m_score'] >= 4:
        return 'Champions'
    elif row['r_score'] >= 3 and row['f_score'] >= 3:
        return 'Loyal Customers'
    elif row['r_score'] >= 4 and row['f_score'] <= 2:
        return 'New Customers'
    elif row['r_score'] <= 2 and row['f_score'] >= 3:
        return 'At Risk'
    elif row['r_score'] <= 2 and row['f_score'] <= 2:
        return 'Lost'
    elif row['r_score'] >= 3 and row['m_score'] >= 4:
        return 'Big Spenders'
    else:
        return 'Need Attention'

rfm['segment'] = rfm.apply(segment_customer, axis=1)

segment_summary = rfm.groupby('segment').agg(
    count=('customer_id', 'count'),
    avg_monetary=('monetary', 'mean'),
    avg_frequency=('frequency', 'mean'),
    avg_recency=('recency', 'mean')
).sort_values('count', ascending=False)

print("Customer Segments:")
print(segment_summary.to_string())
```

Third cell — visualization:

```python
# SEGMENT VISUALIZATION
fig = px.scatter(
    rfm, x='recency', y='monetary',
    size='frequency', color='segment',
    title='Customer Segments: Recency vs. Monetary Value',
    labels={'recency': 'Days Since Last Purchase', 'monetary': 'Total Spend ($)'},
    hover_data=['customer_id', 'frequency'],
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig.update_layout(template='plotly_white', height=600)
fig.show()
fig.write_image('output/customer_segments.png', width=1200, height=800, scale=2)

# Segment revenue contribution
segment_revenue = rfm.groupby('segment')['monetary'].sum().sort_values(ascending=False)
segment_revenue_pct = (segment_revenue / segment_revenue.sum() * 100).round(1)

fig = px.pie(
    values=segment_revenue.values,
    names=segment_revenue.index,
    title='Revenue Contribution by Customer Segment',
    hole=0.4
)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(template='plotly_white', height=500)
fig.show()
fig.write_image('output/segment_revenue_pie.png', width=1200, height=800, scale=2)

print("\nRevenue by Segment:")
for seg, pct in segment_revenue_pct.items():
    print(f"  {seg}: {pct}%")
```

Fourth cell — K-means clustering as an alternative:

```python
# K-MEANS CLUSTERING (Alternative to rule-based segmentation)
features = rfm[['recency', 'frequency', 'monetary']]
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Find optimal k using elbow method
inertias = []
k_range = range(2, 9)
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(features_scaled)
    inertias.append(km.inertia_)

fig = px.line(x=list(k_range), y=inertias, markers=True,
              title='Elbow Method: Optimal Number of Clusters',
              labels={'x': 'Number of Clusters (k)', 'y': 'Inertia'})
fig.update_layout(template='plotly_white', height=400)
fig.show()

# Use 4 clusters as default (adjust based on elbow)
optimal_k = 4
km = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
rfm['cluster'] = km.fit_predict(features_scaled)

cluster_summary = rfm.groupby('cluster').agg(
    count=('customer_id', 'count'),
    avg_recency=('recency', 'mean'),
    avg_frequency=('frequency', 'mean'),
    avg_monetary=('monetary', 'mean')
)
print("\nK-Means Cluster Summary:")
print(cluster_summary.to_string())
```

Save the notebook.

### Template 3: Financial Reporting

Create a new notebook. Save it as `templates/financial-reporting.ipynb`. This template turns raw financial data into P&L summaries, cash flow analysis, and margin tracking.

First cell — load and clean:

```python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import warnings
warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.2f}'.format)

# ============================================
# FINANCIAL REPORTING TEMPLATE
# ============================================
# Expected columns:
# - date: transaction date
# - category: revenue/expense category
# - type: 'income' or 'expense'
# - amount: transaction amount (positive)
# - description: transaction description

df = pd.read_csv('clients/CLIENT_NAME/data.csv', parse_dates=['date'])
df['month'] = df['date'].dt.to_period('M').astype(str)

print(f"Financial data loaded: {len(df):,} transactions")
print(f"Date range: {df['date'].min()} to {df['date'].max()}")
```

Second cell — P&L summary:

```python
# PROFIT & LOSS SUMMARY
monthly_pl = df.pivot_table(
    index='month',
    columns='type',
    values='amount',
    aggfunc='sum',
    fill_value=0
).reset_index()

if 'income' not in monthly_pl.columns:
    monthly_pl['income'] = 0
if 'expense' not in monthly_pl.columns:
    monthly_pl['expense'] = 0

monthly_pl['profit'] = monthly_pl['income'] - monthly_pl['expense']
monthly_pl['margin_pct'] = (monthly_pl['profit'] / monthly_pl['income'] * 100).round(1)

fig = go.Figure()
fig.add_trace(go.Bar(name='Revenue', x=monthly_pl['month'], y=monthly_pl['income'], marker_color='#10B981'))
fig.add_trace(go.Bar(name='Expenses', x=monthly_pl['month'], y=monthly_pl['expense'], marker_color='#EF4444'))
fig.add_trace(go.Scatter(name='Profit', x=monthly_pl['month'], y=monthly_pl['profit'],
                          mode='lines+markers', line=dict(color='#2563EB', width=3)))
fig.update_layout(
    title='Monthly Profit & Loss',
    xaxis_title='Month',
    yaxis_title='Amount ($)',
    barmode='group',
    template='plotly_white',
    height=500
)
fig.show()
fig.write_image('output/monthly_pl.png', width=1200, height=800, scale=2)

print("\nMonthly P&L Summary:")
print(monthly_pl.to_string(index=False))
```

Third cell — expense breakdown:

```python
# EXPENSE BREAKDOWN
expenses = df[df['type'] == 'expense']
expense_by_cat = expenses.groupby('category')['amount'].sum().sort_values(ascending=False)
expense_pct = (expense_by_cat / expense_by_cat.sum() * 100).round(1)

fig = px.treemap(
    names=expense_by_cat.index,
    parents=['Total Expenses'] * len(expense_by_cat),
    values=expense_by_cat.values,
    title='Expense Breakdown by Category',
    color=expense_by_cat.values,
    color_continuous_scale='Reds'
)
fig.update_layout(height=500)
fig.show()
fig.write_image('output/expense_breakdown.png', width=1200, height=800, scale=2)

print("Top 5 Expense Categories:")
for cat, amt in expense_by_cat.head(5).items():
    print(f"  {cat}: ${amt:,.2f} ({expense_pct[cat]}%)")
```

Fourth cell — cash flow analysis:

```python
# CASH FLOW ANALYSIS
monthly_pl['cumulative_profit'] = monthly_pl['profit'].cumsum()

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=monthly_pl['month'],
    y=monthly_pl['cumulative_profit'],
    mode='lines+markers',
    fill='tozeroy',
    line=dict(color='#2563EB', width=3),
    name='Cumulative Profit'
))
fig.update_layout(
    title='Cumulative Cash Flow',
    xaxis_title='Month',
    yaxis_title='Cumulative Profit ($)',
    template='plotly_white',
    height=400
)
fig.show()
fig.write_image('output/cumulative_cashflow.png', width=1200, height=600, scale=2)

avg_margin = monthly_pl['margin_pct'].mean()
trend = "improving" if monthly_pl['margin_pct'].iloc[-1] > monthly_pl['margin_pct'].iloc[0] else "declining"
print(f"\nAverage Profit Margin: {avg_margin:.1f}%")
print(f"Margin Trend: {trend}")
print(f"Best Margin Month: {monthly_pl.loc[monthly_pl['margin_pct'].idxmax(), 'month']} ({monthly_pl['margin_pct'].max():.1f}%)")
print(f"Worst Margin Month: {monthly_pl.loc[monthly_pl['margin_pct'].idxmin(), 'month']} ({monthly_pl['margin_pct'].min():.1f}%)")
```

Save the notebook.

### CHECK-IN: Step 3 Complete

1. Sales analysis template runs end-to-end on a sample CSV
2. Customer segmentation template produces RFM scores and K-means clusters
3. Financial reporting template generates P&L, expense breakdown, and cash flow charts
4. All Plotly charts render correctly and export as PNGs to your `output/` folder
5. Each template has clear column expectations documented at the top

If all 5 pass, move to Step 4. If any fail, debug the specific cell that errors before proceeding. Templates are your foundation — they must work flawlessly.

## Step 4: Build the Client Onboarding Process

Before you analyze a single row of client data, you need a professional onboarding process. This is where you set expectations, collect the right data, and protect yourself legally. Skip this and you will have scope creep, unhappy clients, and potentially serious liability.

### Create the Onboarding Form in Notion

Open Notion. Create a new page called "Client Onboarding." Add a form using Notion's form feature (or use a free Typeform account at typeform.com if you prefer more customization). Your form must collect the following information:

**Business Information:**
- Company name
- Industry
- Number of employees
- Primary business goal for this analysis

**Data Questions:**
- What data sources do you have? (Checkbox: CRM, Spreadsheet, Accounting Software, E-commerce Platform, Marketing Platform, Other)
- Where does your data currently live? (Text field)
- What file format can you provide? (CSV, Excel, Google Sheets, Other)
- Approximately how many rows of data? (Dropdown: Under 1,000 / 1,000-10,000 / 10,000-100,000 / 100,000+)
- How would you rate your data quality? (1-5 scale — and assume it is worse than they say)

**Business Questions:**
- What are the top 3 questions you want answered from your data?
- What decision will this analysis inform?
- Who will receive the final report?
- Have you worked with a data analyst before?

**Legal:**
- Data handling agreement checkbox (confirming they have the right to share this data with you)
- NDA acknowledgment checkbox

### Create the Data Handling Agreement

You need a standard data handling agreement. This is not optional. You are handling potentially sensitive business data. Create a simple document in Notion (or Google Docs) with these sections:

1. **Scope of Data Processing:** You will analyze the data provided by the client for the purpose of generating business insights and recommendations.
2. **Data Security:** You will store client data in encrypted storage, will not share it with third parties, and will delete it within 30 days of project completion unless the client requests otherwise.
3. **Data Ownership:** All data remains the property of the client. You claim no ownership or rights to use the data for any purpose beyond the agreed analysis.
4. **Confidentiality:** You will not disclose any findings, data, or insights to third parties without written client consent.
5. **Liability Limit:** Your liability is limited to the fees paid for the analysis. You are not liable for business decisions made based on your recommendations.

Have a lawyer review this if you can afford it. At minimum, use this as your starting framework. It will not fully protect you in court, but it establishes boundaries and signals professionalism.

### Set Up the Client Folder Structure

When a client signs, create this folder structure inside your `clients/` directory:

```
clients/
  CLIENT_NAME/
    raw/            # Original, unmodified client data
    cleaned/        # Cleaned and transformed datasets
    analysis/       # Jupyter notebooks for this client
    output/         # Charts, reports, deliverables
    communication/  # Meeting notes, email threads
    contract/       # Signed agreements
```

Create this structure for every client. No exceptions. The `raw/` folder must never be modified — it is your audit trail. If the client disputes a finding, you can trace it back to the original data.

### The First Client Call

Schedule a 30-minute onboarding call. Here is your agenda, minute by minute:

**Minutes 0-5:** Introductions. Confirm the scope of work and the 3 questions they want answered. Write these down verbatim.

**Minutes 5-15:** Review their data together. Ask them to share their screen and walk through the spreadsheet or dashboard. Identify: what columns exist, how far back the data goes, known data issues, and any transformations they have already applied. Take detailed notes.

**Minutes 15-20:** Discuss data transfer. How will they send you the data? The safest method is a shared Google Drive folder — they upload, you download. Agree on a deadline for data delivery.

**Minutes 20-25:** Set expectations. Tell them: "I will deliver a data quality report within 2 business days of receiving your data. Then I will deliver the full analysis within 5 business days. You will receive a presentation with key findings, visualizations, and specific recommendations. We will have a 30-minute review call to discuss the findings."

**Minutes 25-30:** Confirm timeline, next steps, and send the data handling agreement for signature.

### CHECK-IN: Step 4 Complete

1. Onboarding form is live and collects all required information
2. Data handling agreement document exists and has been reviewed
3. Client folder structure template is ready to duplicate
4. You have a written 30-minute call agenda
5. You can explain your delivery timeline confidently

If all 5 pass, move to Step 5. If any fail, complete them before taking on a client.

## Step 5: Execute the Data Cleaning Workflow

This is the unglamorous core of data analysis. Every dataset you receive will be messy. Every single one. Your cleaning workflow must be systematic and repeatable. Here is the exact process you follow for every client.

### Step 5.1: Create a Data Quality Report

When you receive client data, save the original file to `clients/CLIENT_NAME/raw/`. Never modify this file. Open a new Jupyter notebook and save it to `clients/CLIENT_NAME/analysis/01-data-quality.ipynb`.

First cell:

```python
import pandas as pd
import numpy as np

# Load raw data
df = pd.read_csv('../raw/data.csv')
print(f"Shape: {df.shape}")
print(f"\nColumn types:\n{df.dtypes}")
```

Second cell — automated quality checks:

```python
# DATA QUALITY REPORT
report = {}

# 1. Missing values
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
report['missing_values'] = missing[missing > 0].to_dict()

# 2. Duplicate rows
report['duplicate_rows'] = int(df.duplicated().sum())
report['duplicate_pct'] = round(df.duplicated().sum() / len(df) * 100, 2)

# 3. Constant columns (no variance — useless for analysis)
constant_cols = [col for col in df.columns if df[col].nunique() <= 1]
report['constant_columns'] = constant_cols

# 4. Numeric columns with suspicious ranges
numeric_cols = df.select_dtypes(include=[np.number]).columns
outlier_info = {}
for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 3 * iqr
    upper = q3 + 3 * iqr
    outliers = df[(df[col] < lower) | (df[col] > upper)][col]
    if len(outliers) > 0:
        outlier_info[col] = {
            'count': len(outliers),
            'pct': round(len(outliers) / len(df) * 100, 2),
            'min': float(df[col].min()),
            'max': float(df[col].max())
        }
report['potential_outliers'] = outlier_info

# 5. Date column validation
date_cols = [col for col in df.columns if 'date' in col.lower() or 'time' in col.lower()]
for col in date_cols:
    try:
        parsed = pd.to_datetime(df[col], errors='coerce')
        unparseable = parsed.isnull().sum() - df[col].isnull().sum()
        if unparseable > 0:
            report[f'{col}_unparseable_dates'] = int(unparseable)
    except:
        pass

# Print report
print("=" * 60)
print("DATA QUALITY REPORT")
print("=" * 60)
print(f"\nTotal rows: {len(df):,}")
print(f"Total columns: {len(df.columns)}")
print(f"Duplicate rows: {report['duplicate_rows']} ({report['duplicate_pct']}%)")
if report['missing_values']:
    print(f"\nMissing values:")
    for col, count in report['missing_values'].items():
        print(f"  {col}: {count} ({missing_pct[col]}%)")
if report['constant_columns']:
    print(f"\nConstant columns (no analysis value): {report['constant_columns']}")
if report['potential_outliers']:
    print(f"\nPotential outliers:")
    for col, info in report['potential_outliers'].items():
        print(f"  {col}: {info['count']} outliers ({info['pct']}%), range: [{info['min']}, {info['max']}]")
```

Save this report. Send a summary to the client within 2 business days. This builds trust and sets realistic expectations about what the data can and cannot reveal.

### Step 5.2: Clean the Data

Create a second notebook: `clients/CLIENT_NAME/analysis/02-data-cleaning.ipynb`.

First cell — load and document transformations:

```python
import pandas as pd
import numpy as np

df = pd.read_csv('../raw/data.csv')
transformations = []  # Document every change

# 1. Remove exact duplicates
before = len(df)
df = df.drop_duplicates()
after = len(df)
transformations.append(f"Removed {before - after} duplicate rows")

# 2. Standardize column names (lowercase, underscores, no spaces)
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_')
transformations.append(f"Standardized {len(df.columns)} column names to snake_case")

# 3. Parse date columns
date_cols = [col for col in df.columns if 'date' in col]
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')
    null_count = df[col].isnull().sum()
    if null_count > 0:
        transformations.append(f"Parsed '{col}' as datetime ({null_count} unparseable values set to NaT)")

# 4. Handle missing values based on type
for col in df.columns:
    missing_count = df[col].isnull().sum()
    if missing_count == 0:
        continue
    missing_pct = missing_count / len(df) * 100

    if missing_pct > 50:
        transformations.append(f"Dropped column '{col}' ({missing_pct:.1f}% missing)")
        df = df.drop(columns=[col])
    elif df[col].dtype in [np.float64, np.int64, float, int]:
        median_val = df[col].median()
        df[col] = df[col].fillna(median_val)
        transformations.append(f"Filled {missing_count} missing values in '{col}' with median ({median_val:.2f})")
    else:
        df[col] = df[col].fillna('Unknown')
        transformations.append(f"Filled {missing_count} missing values in '{col}' with 'Unknown'")

# 5. Remove obvious data entry errors
numeric_cols = df.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    if 'revenue' in col or 'price' in col or 'amount' in col or 'cost' in col:
        negative_count = (df[col] < 0).sum()
        if negative_count > 0:
            df.loc[df[col] < 0, col] = np.nan
            df[col] = df[col].fillna(df[col].median())
            transformations.append(f"Replaced {negative_count} negative values in '{col}' with median")

# Save cleaned data
df.to_csv('../cleaned/data_cleaned.csv', index=False)

# Print transformation log
print("DATA CLEANING LOG")
print("=" * 60)
for t in transformations:
    print(f"  - {t}")
print(f"\nFinal dataset: {len(df):,} rows, {len(df.columns)} columns")
```

This notebook is your audit trail. Every transformation is documented. If the client asks "why did you change X?", you have the answer.

### Step 5.3: Validate the Cleaned Data

In the same notebook, add a validation cell:

```python
# VALIDATION CHECKS
assert df.isnull().sum().sum() == 0 or df.isnull().sum().max() / len(df) < 0.05, "Too many missing values remain"
assert df.duplicated().sum() == 0, "Duplicates still present after cleaning"
assert len(df) > 0, "Dataset is empty after cleaning"

# Check that key columns exist (customize per client)
required_cols = ['date', 'revenue']
for col in required_cols:
    if col in df.columns:
        assert df[col].notnull().all(), f"Column '{col}' has remaining null values"

print("All validation checks passed. Data is ready for analysis.")
```

If any assertion fails, stop and fix the issue before proceeding to analysis.

### CHECK-IN: Step 5 Complete

1. Data quality report is generated and sent to the client
2. Cleaning notebook documents every transformation
3. Cleaned data is saved separately from raw data
4. Validation checks all pass
5. You can explain every transformation you made to the client

If all 5 pass, move to Step 6. If any fail, do not proceed. Bad data produces bad insights, and bad insights destroy client trust.

## Step 6: Produce Client Visualizations with AI

Your visualizations must tell a story. A chart without context is decoration. A chart with context is a weapon. Here is how to produce weapon-grade visualizations every time.

### The Visualization Rules

Follow these rules for every chart you produce. No exceptions.

1. **Every chart has a headline.** Not "Revenue by Month." That is a title. A headline is "Revenue Dropped 23% in Q3 — Here is the Monthly Breakdown."
2. **Every chart has a 2-sentence annotation.** First sentence: what the chart shows. Second sentence: why it matters for the business.
3. **Use color intentionally.** Green for positive, red for negative, blue for neutral. Never use more than 3 colors per chart. Rainbow charts are for kindergartens.
4. **Remove chart junk.** Delete gridlines that do not add information. Remove legends when there is only one data series. Eliminate 3D effects. Every pixel must earn its place.
5. **Export at 1200x800 minimum, 2x scale.** Charts will be viewed on screens, projected in meetings, and printed. Low-resolution charts look amateur.

### The Chart Generation Workflow

After running your analysis template, you will have a set of Plotly charts. Enhance each one with these formatting additions:

```python
# Add to every Plotly figure before fig.show()
fig.update_layout(
    font=dict(family='Inter, Arial, sans-serif', size=14),
    title_font=dict(size=20),
    annotations=[dict(
        text="Your 2-sentence annotation here explaining the insight.",
        xref="paper", yref="paper",
        x=0.5, y=-0.15,
        showarrow=False,
        font=dict(size=12, color="#666666")
    )],
    margin=dict(b=80)  # Space for annotation
)
```

### AI-Enhanced Chart Generation

Use ChatGPT to generate custom visualizations for findings that your templates do not cover. Upload the cleaned dataset and use this prompt:

> I found the following insight in this data: [describe the insight]. Create a Plotly visualization that best communicates this insight. The chart must have: (1) A headline-style title that includes the key number, (2) Clear axis labels with units, (3) An annotation that explains the business implication, (4) Professional styling with no more than 3 colors. Export as PNG at 1200x800.

ChatGPT will write the code. Copy it into your client notebook. Run it. Verify the output. This is how you produce bespoke visualizations without spending hours on chart design.

### The Insight-to-Chart Mapping

Not every finding deserves a chart. Use this mapping to decide:

| Insight Type | Best Chart Type | When to Use |
|-------------|-----------------|-------------|
| Trend over time | Line chart with markers | When showing how a metric changes across time periods |
| Comparison between groups | Horizontal bar chart | When comparing categories (products, regions, segments) |
| Part of whole | Donut chart (not pie) | When showing composition with 3-6 categories |
| Correlation | Scatter plot with trendline | When showing relationship between two variables |
| Distribution | Histogram or box plot | When showing how values are spread |
| Before/after | Grouped bar chart | When comparing periods or scenarios |
| Ranking | Sorted bar chart | When showing top/bottom performers |

### CHECK-IN: Step 6 Complete

1. Every chart has a headline, annotation, and intentional color use
2. All charts export at 1200x800 minimum, 2x scale
3. You can generate custom visualizations using ChatGPT Code Interpreter
4. Your charts tell a story — a non-technical person can understand each one
5. Chart count matches insight count (no filler charts, no missing charts)

If all 5 pass, move to Step 7.

## Step 7: Generate the Automated Client Report

The report is your deliverable. It is what the client pays for. It must be professional, clear, and actionable. Here is the exact report structure and generation process.

### Report Structure

Every report follows this structure. Do not deviate from it.

1. **Cover Page** — Client name, report title, date, your logo
2. **Executive Summary** — 3-5 key findings, each in one sentence with the supporting number
3. **Data Quality Assessment** — What you received, what you cleaned, what was missing
4. **Key Findings** — 5-10 findings, each with: headline, data evidence, business implication, recommended action
5. **Visualizations** — 5-8 charts, each with headline and annotation
6. **Recommendations** — Prioritized list with expected impact and implementation difficulty
7. **Appendix** — Methodology, full statistical output, data dictionary

### Generate the Report from Jupyter

Create a notebook: `clients/CLIENT_NAME/analysis/03-report-generation.ipynb`.

First cell — convert your analysis notebook to HTML:

```python
import subprocess

# Convert analysis notebook to HTML
result = subprocess.run([
    'jupyter', 'nbconvert',
    '--to', 'html',
    '--no-input',  # Hide code cells
    '02-analysis.ipynb',  # Your analysis notebook
    '--output', '../output/analysis-report.html'
], capture_output=True, text=True)

if result.returncode == 0:
    print("HTML report generated successfully")
else:
    print(f"Error: {result.stderr}")
```

The `--no-input` flag hides all code cells. The client sees only your markdown explanations and chart outputs. This is critical — code cells confuse non-technical clients and make the report look unfinished.

### Create the Presentation Version

For client presentations, you need slides, not an HTML document. Use this approach:

1. Open Canva. Search for "data report presentation." Pick a template with a dark or neutral background.
2. For each finding, create one slide with: the headline at the top, the chart image in the center, and the recommended action at the bottom.
3. The Executive Summary gets its own slide with 3-5 bullet points.
4. The Recommendations slide lists all recommendations ranked by impact.

Export as PDF. This is your presentation deliverable.

### Automated PDF Report (Advanced)

For a fully automated pipeline, use Python to generate a PDF report directly:

```python
from fpdf import FPDF
import glob

class DataReport(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 10)
        self.cell(0, 10, 'CONFIDENTIAL — Prepared for [CLIENT NAME]', 0, 1, 'R')
        self.line(10, 15, 200, 15)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def section_title(self, title):
        self.set_font('Helvetica', 'B', 16)
        self.set_fill_color(37, 99, 235)  # Blue
        self.set_text_color(255, 255, 255)
        self.cell(0, 12, f'  {title}', 0, 1, 'L', fill=True)
        self.set_text_color(0, 0, 0)
        self.ln(5)

    def body_text(self, text):
        self.set_font('Helvetica', '', 11)
        self.multi_cell(0, 7, text)
        self.ln(3)

    def add_chart(self, image_path, width=180):
        if self.get_y() + 100 > 270:
            self.add_page()
        self.image(image_path, x=15, w=width)
        self.ln(5)

# Build report
pdf = DataReport()
pdf.set_auto_page_break(auto=True, margin=20)

# Cover page
pdf.add_page()
pdf.ln(50)
pdf.set_font('Helvetica', 'B', 28)
pdf.cell(0, 15, 'Data Analysis Report', 0, 1, 'C')
pdf.set_font('Helvetica', '', 16)
pdf.cell(0, 10, 'Prepared for [CLIENT NAME]', 0, 1, 'C')
pdf.cell(0, 10, '[DATE]', 0, 1, 'C')
pdf.ln(20)
pdf.set_font('Helvetica', 'I', 12)
pdf.cell(0, 10, 'CONFIDENTIAL', 0, 1, 'C')

# Executive Summary
pdf.add_page()
pdf.section_title('Executive Summary')
pdf.body_text('[Insert 3-5 key findings here, each with supporting numbers]')

# Key Findings
pdf.add_page()
pdf.section_title('Key Findings')
pdf.body_text('[Finding 1 with data evidence and recommendation]')
pdf.body_text('[Finding 2 with data evidence and recommendation]')
pdf.body_text('[Finding 3 with data evidence and recommendation]')

# Charts
pdf.add_page()
pdf.section_title('Visualizations')
for chart in sorted(glob.glob('../output/*.png')):
    pdf.add_chart(chart)

# Save
pdf.output('../output/client-report.pdf')
print("PDF report generated: ../output/client-report.pdf")
```

Install fpdf2 first: `pip install fpdf2`. This approach lets you regenerate reports automatically when data updates — essential for monthly retainer clients.

### CHECK-IN: Step 7 Complete

1. HTML report generates from Jupyter notebook with code cells hidden
2. Presentation version exists as a Canva-exported PDF
3. (Optional) Automated PDF pipeline works with fpdf2
4. Report follows the exact structure: Cover, Executive Summary, Data Quality, Findings, Visualizations, Recommendations, Appendix
5. Every recommendation ties to a specific data finding with expected impact

If all 5 pass, move to Step 8.

## Step 8: Set Up Pricing and Payment Collection

You have a working service. Now you need to charge for it. Here is the pricing model, the payment infrastructure, and the sales approach.

### Pricing Tiers

| Tier | Price | Deliverables | Best For |
|------|-------|-------------|----------|
| **Quick Analysis** | $2,000-3,000 one-time | Data quality report, 5-7 key findings, 5 visualizations, recommendation list, 30-min review call | First-time clients, specific questions, one-off projects |
| **Deep Dive** | $5,000-7,500 one-time | Full analysis across all relevant dimensions, 10+ visualizations, interactive dashboard, prioritized recommendations with ROI estimates, 60-min presentation | Businesses with complex data, multi-question projects |
| **Monthly Insights** | $500-2,000/month | Monthly analysis update, fresh insights, trend tracking, email report, quarterly strategy call | Ongoing data monitoring, recurring reporting needs |
| **Dashboard Build** | $3,000-10,000 one-time + $300-500/month maintenance | Custom interactive dashboard (Looker Studio or Plotly Dash), data pipeline setup, training session | Businesses that want self-service access to insights |
| **Predictive Model** | $5,000-15,000 one-time | Custom ML model (churn prediction, sales forecasting, customer segmentation), documentation, integration support | Businesses ready for advanced analytics |

### The Free Sample Strategy

This is your primary client acquisition method. It works. Do it exactly as described.

1. Identify a prospect. Find a business that clearly has data but is not using it. Check their website for phrases like "data-driven" (with no evidence), look at their job postings for data roles they have not filled, or ask your network for introductions.
2. Ask for 100 rows of their data. Not the full dataset. 100 rows. This is low-risk for them and enough for you.
3. Run the ChatGPT Code Interpreter pipeline (Step 2) on the sample data.
4. Send them 3 specific insights they did not know. "Your average order value on weekdays is 34% higher than weekends." "Your top 10% of customers by revenue have not made a purchase in 90+ days." "Your product return rate for Category X is 3x the overall average."
5. End with: "This is from 100 rows. Imagine what the full dataset would reveal."

This converts at 20-30%. The free sample proves your value before the client has to make a financial commitment.

### Set Up Stripe for Payments

Go to stripe.com and complete your account setup. You need a business bank account linked. Under **Products** in the Stripe dashboard, create each of your pricing tiers as separate products with the appropriate pricing.

For monthly retainers, create a **Subscription** product. For one-time analyses, create a **One-time** product.

Enable **Stripe Checkout** so clients can pay via a link you send. Go to **Payment Links** in the dashboard, create a payment link for each tier, and save the URLs. You will send these links in your proposal emails.

### The Proposal Template

Create a Notion page called "Proposal Template." Use this structure for every proposal:

```
# Data Analysis Proposal for [CLIENT NAME]

## Understanding
[2-3 sentences showing you understand their business and data challenges]

## Scope of Work
[What you will deliver, specific to their stated questions]

## Deliverables
- Data Quality Report
- [X] Key Findings with supporting data
- [X] Visualizations
- Prioritized Recommendations with expected impact
- [30/60]-minute presentation and Q&A

## Timeline
- Data received: [DATE]
- Data Quality Report delivered: [DATE + 2 business days]
- Full analysis delivered: [DATE + 5 business days]
- Presentation call: [DATE + 7 business days]

## Investment
[PRICE] — [Link to Stripe payment]

## What I Need From You
1. Full dataset in [CSV/Excel] format
2. Data dictionary or column descriptions
3. Signed data handling agreement (attached)
4. Payment before analysis begins
```

Send this as a Notion page (share with "can view" permissions) or export as PDF.

### CHECK-IN: Step 8 Complete

1. All pricing tiers are defined with specific deliverables
2. Stripe account is active with payment links for each tier
3. Proposal template is ready in Notion
4. You have practiced the free sample strategy with a test dataset
5. You can explain your pricing confidently on a call

If all 5 pass, move to Step 9.

## Step 9: Automate with Make.com

Once you have 3+ monthly retainer clients, manual report generation becomes a bottleneck. You need automation. Make.com is your tool. Here is how to build automated data pipelines that generate and deliver reports without your involvement.

### Set Up Your Make.com Account

Go to make.com. Sign up for the Basic plan ($9/mo). This gives you 10,000 operations per month, which is sufficient for 5-10 automated client pipelines.

### Build the Monthly Report Automation

This automation runs on the 1st of every month for each retainer client. It pulls fresh data, runs analysis, generates a report, and emails it to the client.

**Step 1: Add the Scheduler trigger.** Click **Create a new scenario**. Click the `+` icon and select **Schedule**. Set it to run on the 1st day of every month at 8:00 AM in the client's timezone.

**Step 2: Add a Google Sheets module.** Click `+` after the Scheduler. Search for **Google Sheets** and select **Get Values**. Connect your Google account. Select the spreadsheet where the client's data is stored. Select the specific sheet. Set the range to the full data range (e.g., `A1:Z`). This module pulls the latest data from the client's spreadsheet.

**Step 3: Add an HTTP module.** Click `+` after the Google Sheets module. Select **HTTP - Make a request**. This module sends the data to your analysis endpoint. Configure it:
- URL: Your analysis API endpoint (you will set this up next)
- Method: POST
- Headers: `Content-Type: application/json`
- Body type: Raw
- Content type: JSON
- Body: Map the Google Sheets output to the JSON structure your analysis script expects

**Step 4: Create the analysis endpoint.** You need a simple API that accepts data and returns analysis results. The easiest way is a Google Cloud Function or a simple Flask app hosted on Render.com (free tier). Here is a minimal Flask app:

```python
from flask import Flask, request, jsonify
import pandas as pd
import plotly.express as px
import json

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    df = pd.DataFrame(data['rows'])

    # Run analysis (customize per client template)
    summary = {
        'total_revenue': float(df.get('revenue', pd.Series([0])).sum()),
        'avg_order_value': float(df.get('revenue', pd.Series([0])).mean()),
        'total_orders': len(df),
        'top_product': str(df.get('product', pd.Series(['N/A'])).value_counts().index[0]) if 'product' in df.columns else 'N/A'
    }

    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Deploy this on Render.com: create a free account, connect your GitHub repo, and deploy as a Web Service. You will get a URL like `https://your-analysis-app.onrender.com/analyze`. Use this URL in your Make.com HTTP module.

**Step 5: Add an Email module.** Click `+` after the HTTP module. Select **Email - Send an email**. Configure it:
- To: Client's email address
- Subject: `Your Monthly Data Analysis Report — [Month, Year]`
- Body: HTML email template with the analysis summary embedded. Use the output from the HTTP module to populate the numbers.
- Attachments: Attach any generated chart images or PDF reports

**Step 6: Add an error handler.** Right-click the line between any two modules and select **Add error handler**. Select **Email - Send an email**. Configure it to send an alert to YOUR email if the automation fails. Set the subject to `URGENT: Automation failed for [CLIENT NAME]` and the body to include the error message. This ensures you know about failures before the client does.

**Step 7: Test the full pipeline.** Click **Run once** in Make.com. Verify: the scheduler triggers, data is pulled from Google Sheets, the analysis API returns results, and the email is sent with the correct numbers. Check the email on your phone. Does it look professional? Are the numbers correct?

If everything works, activate the scenario by toggling the ON/OFF switch in the bottom-left corner. It will now run automatically every month.

### Build the Data Freshness Monitor

Create a second Make.com scenario that checks if the client's data has been updated. This catches situations where the client forgets to update their spreadsheet — you do not want to send a report based on stale data.

**Step 1: Add a Schedule trigger** — Run daily at 7:00 AM.

**Step 2: Add a Google Sheets module** — Get the last modified timestamp of the client's spreadsheet.

**Step 3: Add a Filter** — If the last modified date is more than 7 days ago, proceed. Otherwise, stop.

**Step 4: Add an Email module** — Send a gentle reminder to the client: "Hi [Name], just a heads-up that your data hasn't been updated in [X] days. Fresh data means fresh insights — could you update the spreadsheet when you get a chance?"

This automation prevents the awkward conversation where the client complains about stale insights when they are the ones who stopped updating the data.

### CHECK-IN: Step 9 Complete

1. Make.com account is active with the Basic plan
2. Monthly report automation is configured and tested for at least one client
3. Error handler sends alerts to your email on failure
4. Data freshness monitor is active
5. You can modify the automation for new clients without starting from scratch

If all 5 pass, move to Step 10.

## Step 10: Scale the Operation

You can handle 3-5 clients solo. Beyond that, you need systems and (eventually) people. Here is how to scale without breaking the machine.

### Build the Vertical Template Library

Your three core templates (sales, segmentation, financial) work across industries. But industry-specific templates close deals faster because the client sees their exact metrics. Build these vertical templates:

**SaaS Template** — Metrics: MRR, ARR, churn rate, LTV, CAC, payback period, expansion revenue, net revenue retention. Sources: Stripe, Mixpanel, ChartMogul. Key analyses: cohort analysis, churn prediction, upgrade path optimization.

**E-commerce Template** — Metrics: AOV, repeat purchase rate, cart abandonment rate, ROAS, customer acquisition cost, inventory turnover. Sources: Shopify, WooCommerce, Google Analytics. Key analyses: product affinity, seasonality modeling, pricing optimization.

**Agency Template** — Metrics: utilization rate, project profitability, client LTV, employee cost per hour, margin by service type. Sources: Harvest, Toggl, QuickBooks. Key analyses: resource allocation, pricing by client tier, project scoping accuracy.

For each vertical, create a dedicated notebook in `templates/` with the specific metrics, chart types, and recommendation frameworks for that industry. When you get a new SaaS client, you duplicate the SaaS template, swap in their data, and deliver in 2 hours instead of 10.

### Document Everything as SOPs

Create a Notion workspace called "Data Analysis SOPs." Document every process:

- **Client Onboarding SOP** — Step-by-step from first contact to data receipt
- **Data Cleaning SOP** — The exact cleaning workflow with code snippets
- **Analysis SOP** — How to select the right template and customize it
- **Visualization SOP** — Chart rules, formatting standards, annotation guidelines
- **Report Generation SOP** — Structure, formatting, delivery method
- **Monthly Retainer SOP** — Automation setup, data freshness checks, client communication

These SOPs let you hire junior analysts to execute the work while you focus on sales and strategy.

### Hire Your First Analyst

When you hit 5-6 clients and are turning down work, it is time to hire. Post on Upwork for a "Junior Data Analyst (Python/Pandas)" at $15-25/hour. Requirements: Python, Pandas, Plotly, Jupyter, basic statistics. Give them your SOPs and have them complete a test project using one of your templates with sample data.

Review their work. Check: are the insights accurate? Are the visualizations clean? Do the recommendations tie to data? If yes, you have your first team member. A junior analyst can handle 8-10 client projects per month at 4-6 hours each. Your cost: $800-1,500/month. Your revenue from those projects: $8,000-15,000/month.

### The Pricing Evolution

As you scale, your pricing should increase. Here is the progression:

- **Months 1-3:** Charge lower end of pricing tiers. You are building portfolio and references.
- **Months 4-6:** Move to mid-range. You have case studies and testimonials.
- **Months 6-12:** Charge top of range. You have a track record, specialized templates, and demand exceeds supply.
- **Month 12+:** Introduce premium tiers. Custom predictive models at $10,000-15,000. Executive dashboard packages at $8,000-12,000. Data strategy consulting at $200-300/hour.

Never race to the bottom on price. A $2,000 analysis and a $500 analysis take roughly the same amount of time. The difference is perceived value, not effort. Invest in presentation quality, recommendation specificity, and industry specialization — these justify premium pricing.

## Cost Breakdown

| Item | Free Tier | Paid Tier | When to Upgrade |
|------|-----------|-----------|-----------------|
| ChatGPT Plus | N/A | $20/mo | Immediately — Code Interpreter is essential |
| Python + Jupyter | $0 | $0 | Always free |
| Pandas + Plotly + SciPy + scikit-learn | $0 | $0 | Always free |
| Google Sheets | $0 | $0 | Always free for basic use |
| Notion | $0 (1,000 blocks) | $10/mo | At 5+ clients for team features |
| Canva | $0 | $13/mo | When you need brand kit and premium templates |
| Make.com | 1,000 ops/mo | $9/mo (Basic) | At 2+ monthly retainer clients |
| Stripe | $0 | 2.9% + 30c per transaction | Always use |
| Render.com (API hosting) | $0 | $7/mo | When free tier limits are hit |
| Tableau (optional) | N/A | $70/mo | When clients demand Tableau dashboards |
| Obviously.ai (optional) | N/A | $75/mo | When you need automated predictive models |
| Domain for portfolio site | — | $12/yr | Immediately |
| Portfolio site hosting | — | $0 (Netlify free) | Immediately |

**Total monthly cost at launch (1-2 clients):** $20-30/mo
**Total monthly cost at 5 clients:** $60-100/mo
**Total monthly cost at 10+ clients (full stack):** $200-300/mo

A single Quick Analysis project at $2,000 covers your tool costs for 6-10 months. The margins in this business are exceptional.

## Production Checklist

Before delivering any analysis to a client, verify every item on this list. No exceptions.

### Data Quality
- [ ] Raw data is saved unmodified in `clients/CLIENT_NAME/raw/`
- [ ] Data quality report was generated and shared with the client
- [ ] All cleaning transformations are documented in the cleaning notebook
- [ ] Validation checks pass (no excessive missing values, no duplicates, no negative revenue)
- [ ] Cleaned data is saved separately from raw data

### Analysis
- [ ] The analysis directly addresses the client's stated business questions
- [ ] Statistical evidence supports every finding (correlation coefficients, p-values, confidence intervals where applicable)
- [ ] Outlier analysis has been performed and documented
- [ ] At least 5 key findings are identified with business implications
- [ ] No finding is presented without a recommended action

### Visualizations
- [ ] Every chart has a headline-style title (not just a label)
- [ ] Every chart has a 2-sentence annotation explaining the insight
- [ ] Colors are used intentionally (green=positive, red=negative, blue=neutral)
- [ ] Charts are exported at 1200x800 minimum, 2x scale
- [ ] No chart is included that does not support a key finding

### Report
- [ ] Report follows the standard structure (Cover, Executive Summary, Data Quality, Findings, Visualizations, Recommendations, Appendix)
- [ ] Executive Summary contains 3-5 findings with supporting numbers
- [ ] Every recommendation includes: the action, the data evidence, the expected impact, and implementation difficulty
- [ ] Data handling agreement is signed and filed
- [ ] Report is delivered in both PDF and presentation format

### Delivery
- [ ] 30-minute review call is scheduled
- [ ] Client receives the report at least 24 hours before the review call
- [ ] Follow-up email is prepared with next steps and retainer proposal
- [ ] All client data will be deleted within 30 days unless retainer is active

## What to Do Next

You have the complete playbook. Here is what to do in the next 72 hours.

**Hour 0-4:** Set up your Python environment (Step 1). Install everything. Verify it works. Run the boilerplate cell in Jupyter.

**Hour 4-8:** Download a sample dataset from Kaggle. Run it through the ChatGPT Code Interpreter pipeline (Step 2). Generate a full analysis with visualizations. This is your practice run.

**Hour 8-16:** Build the three analysis templates (Step 3). Run each one on the sample data. Fix any errors. Save the notebooks.

**Hour 16-20:** Set up your client onboarding infrastructure (Step 4). Create the Notion form, the data handling agreement, and the folder structure. Practice the onboarding call script out loud.

**Hour 20-24:** Build your first portfolio piece. Take the analysis you produced in Hour 4-8. Format it into a professional report (Step 7). Create the Canva presentation. This is your sample deliverable — the thing you show prospects to prove you can do the work.

**Hour 24-48:** Find 10 prospects. Use the free sample strategy (Step 8). Send personalized emails with one industry-specific insight. Your goal: get 3 responses. Close 1 client.

**Hour 48-72:** Deliver your first paid analysis. Follow every step in this guide. Use the Production Checklist. Overdeliver. Ask for a testimonial. Ask for a referral.

After your first client, the flywheel spins. Testimonials bring prospects. Templates reduce build time. Automation frees your hours. Specialization justifies higher pricing. The business compounds.

Every business has data. Almost none of them know what it means. You do now. Go tell them.
