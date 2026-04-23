---
title: "Build and Monetize AI SaaS Micro-Products on Replit"
date: 2026-04-24
category: "Implementation"
difficulty: "INTERMEDIATE"
readTime: "25 MIN"
excerpt: "The complete execution guide for building, deploying, and monetizing AI-powered SaaS micro-products. From idea validation to first paying users."
image: "/images/articles/intelligence/create-ai-saas-micro-products-replit.png"
---

Building an AI SaaS micro-product is not about building the most impressive software. It is about solving one narrow problem so well that people will pay you $9-29 per month to make it go away. A micro-product does one thing. It does not have a dashboard with twelve tabs. It does not try to be a platform. It is a scalpel, not a Swiss Army knife. This guide walks you through the entire process — from finding an idea people will pay for to deploying it on Replit and acquiring your first 100 users. Follow it in order. Do not skip steps.

## Prerequisites

Before you start, you need the following:

- A laptop with a modern browser (Chrome or Firefox)
- A Replit account (free tier works for development) — go to replit.com and sign up
- An OpenAI API key ($5 minimum credit) — go to platform.openai.com/api-keys
- A Stripe account for collecting payments — go to stripe.com and sign up
- A Clerk account for authentication (free tier covers 10,000 monthly active users) — go to clerk.com and sign up
- A custom domain name ($10-12/yr from Namecheap or Cloudflare) — optional until launch
- 6-8 hours of uninterrupted time for your first build

Total upfront cost: $5 for the OpenAI API key. Everything else is free until you have paying users.

## Step 1: Find and Validate Your SaaS Idea

Most people build first and validate second. That is backwards. You will spend 20 hours building something nobody wants. Validate first. Build second. Here is the method.

### Market Research: The Three-Source Method

Open three browser tabs. In the first, go to trends.google.com. Type a problem domain you are interested in — examples: "AI resume," "AI contract review," "AI product description." Look at the trend line over the past 12 months. You want a line that is flat or rising. A declining trend means the market is contracting. A spike-and-crash pattern means it was a fad. You want steady or growing interest.

In the second tab, go to reddit.com and search for your problem domain. Sort by "Top" in the past year. Read the top 20 posts. You are looking for two signals: people complaining about a specific pain point ("I spend 3 hours every week writing product descriptions") and people asking for tools to solve it ("Is there an app that does X?"). Copy every complaint and request into a spreadsheet. These are your demand signals.

In the third tab, go to chatgpt.com/gpts (the GPT Store) and search for your problem domain. Sort by "Most popular." Read the reviews on the top 10 GPTs. You are looking for what users like and — more importantly — what they complain about. Common complaints in GPT Store reviews include: "It forgets my context," "I can't save my outputs," "I hit the message limit," "I wish it could process files." These complaints are feature gaps you can build into a paid product.

### The 3-Criteria Validation Checklist

After your research, you should have 3-5 idea candidates. Run each through these three criteria:

1. **Specific pain, not vague interest.** Can you state the problem in one sentence? "Freelancers waste 2+ hours per week writing cold outreach emails" is a specific pain. "People want AI to help with work" is vague interest. Only proceed with specific pains.

2. **Willingness to pay evidence.** Did you find existing paid tools in this space? Are people already paying for partial solutions? If nobody is paying for anything in this space, they will not pay for your product either. Existing competition is a positive signal — it proves the market has money.

3. **Narrow enough to build in a weekend.** Can you ship a working version with one core feature in 48 hours? If your idea requires a database schema with 15 tables, it is not a micro-product. If it requires more than 3 API integrations at launch, it is not a micro-product. Scope down until it fits.

**Interactive check-in:** Did your idea pass all 3 criteria? If not, go back and find another. Do not proceed with an idea that fails even one criterion. You will waste weeks on something that cannot sustain a business. Here is a quick reference:

| Criterion | Pass | Fail |
|-----------|------|------|
| Specific pain | "Spend 2 hrs/week on X" | "People want AI" |
| Willingness to pay | Competitors charge $10-50/mo | No paid tools exist |
| Buildable in a weekend | 1 core feature, 1-2 APIs | Multi-feature, 4+ APIs |

Example ideas that pass all three: AI-powered cold email rewriter, AI contract clause explainer, AI product description generator for Shopify, AI meeting notes summarizer, AI job description optimizer.

## Step 2: Set Up Your Replit Development Environment

Go to replit.com and sign in. You should see your Replit dashboard — a clean interface with a "Create Repl" button in the top-right corner.

Do you see that button? You should see a dashboard with your profile photo and a "Create Repl" button if you are in the right place. If you see a blank screen, verify your email address. Replit requires email verification before you can access the dashboard. Check your inbox, click the verification link, and come back.

Click **Create Repl**. A modal will appear. Configure the following:

- **Template:** Select "Python" (not "Python with GUI")
- **Name:** Enter your product name in snake_case (e.g., `cold-email-rewriter`)
- Click **Create Repl**

You should now see the Replit IDE — a code editor on the left, a console/terminal at the bottom, and a preview pane on the right. If you see this, you are in the right place. If you see something else (a different IDE layout, no terminal), you may have selected the wrong template. Go back and make sure you selected "Python."

### Configure Environment Variables

You need to store API keys securely. In the left sidebar, click the **Secrets** icon (it looks like a lock). This is Replit's environment variable manager. Add the following secrets one by one:

| Key | Value | Where to Get It |
|-----|-------|-----------------|
| `OPENAI_API_KEY` | `sk-proj-...` | platform.openai.com/api-keys |
| `STRIPE_SECRET_KEY` | `sk_test_...` | dashboard.stripe.com/apikeys |
| `STRIPE_WEBHOOK_SECRET` | `whsec_...` | Set up after deployment |
| `CLERK_SECRET_KEY` | `sk_test_...` | dashboard.clerk.com |

**Important:** Always use test keys (`sk_test_`) during development. Never use live keys until you are ready to accept real payments.

### Install Dependencies

Open the Shell tab at the bottom of the Replit IDE. Run the following command:

```bash
pip install fastapi uvicorn openai stripe python-dotenv pydantic
```

You should see output like this:

```
Successfully installed fastapi-0.115.0 uvicorn-0.32.0 openai-1.52.0 stripe-10.0.0 python-dotenv-1.0.1 pydantic-2.9.0
```

Do you see "Successfully installed" with the package names? If you see errors, check your internet connection and try again. If a specific package fails, install it individually: `pip install <package-name>`.

### Create the Project Structure

In the Files panel on the left, create the following structure:

```
cold-email-rewriter/
├── main.py
├── routers/
│   ├── ai.py
│   ├── billing.py
│   └── auth.py
├── models.py
├── requirements.txt
└── static/
    └── index.html
```

Create each file by right-clicking the parent directory and selecting "New File." The `routers/` directory needs to be created first — right-click the project root, select "New Folder," name it `routers."

### Start the Development Server

Open `main.py` and add the following:

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI(title="Cold Email Rewriter", version="1.0.0")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse("static/index.html")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
```

In the Shell, run:

```bash
python main.py
```

You should see:

```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
```

Click the **Webview** tab in the top-right of the Replit IDE. You should see a blank page (because `index.html` is empty). Now navigate to `localhost:8000/docs` in the Webview URL bar.

**Interactive check-in:** Do you see the FastAPI interactive documentation page with your endpoints listed? You should see a heading that says "Cold Email Rewriter - 1.0.0" and a list of endpoints. If you see this, your server is running correctly. If you see a "404 Not Found" error, check that `main.py` saved correctly and the server is still running. If you see a connection refused error, restart the server.

## Step 3: Build the Core Product

Now you build the three essential components: the AI backend, the user interface, and the payment system.

### Build the AI Backend

Open `routers/ai.py` and add:

```python
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
from openai import OpenAI

router = APIRouter(prefix="/api/ai", tags=["AI"])

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

class RewriteRequest(BaseModel):
    original_email: str
    tone: str = "professional"  # professional, casual, friendly
    target_role: str = ""       # job title of the recipient

class RewriteResponse(BaseModel):
    rewritten_email: str
    word_count: int
    suggestions: list[str]

@router.post("/rewrite", response_model=RewriteResponse)
async def rewrite_email(request: RewriteRequest):
    if not request.original_email.strip():
        raise HTTPException(status_code=400, detail="Email text is required")

    system_prompt = f"""You are an expert cold email writer. Rewrite the given email
    to be more effective at getting responses. Use a {request.tone} tone.
    {"The recipient is a " + request.target_role + "." if request.target_role else ""}
    Keep it concise (under 150 words). Focus on one clear ask."""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Rewrite this cold email:\n\n{request.original_email}"}
            ],
            temperature=0.7,
            max_tokens=300
        )

        rewritten = response.choices[0].message.content

        # Generate improvement suggestions
        suggestion_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "List 2-3 specific improvements you made. Be brief."},
                {"role": "user", "content": f"Original:\n{request.original_email}\n\nRewritten:\n{rewritten}"}
            ],
            temperature=0.3,
            max_tokens=150
        )

        suggestions = [s.strip().lstrip("0123456789.-) ")
                       for s in suggestion_response.choices[0].message.content.split("\n")
                       if s.strip()]

        return RewriteResponse(
            rewritten_email=rewritten,
            word_count=len(rewritten.split()),
            suggestions=suggestions
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI processing failed: {str(e)}")
```

Now register this router in `main.py`. Add this import at the top:

```python
from routers import ai, billing, auth
```

And add these lines after `app = FastAPI(...)`:

```python
app.include_router(ai.router)
app.include_router(billing.router)
app.include_router(auth.router)
```

### Build the User Interface

Open `static/index.html` and add a minimal but functional interface:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cold Email Rewriter — AI-Powered</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, sans-serif;
               background: #0a0a0a; color: #e5e5e5; max-width: 720px;
               margin: 0 auto; padding: 48px 24px; }
        h1 { font-size: 28px; margin-bottom: 8px; color: #fff; }
        .subtitle { color: #888; margin-bottom: 32px; font-size: 15px; }
        textarea { width: 100%; height: 160px; background: #1a1a1a; border: 1px solid #333;
                   border-radius: 8px; padding: 16px; color: #e5e5e5; font-size: 15px;
                   resize: vertical; margin-bottom: 16px; }
        textarea:focus { outline: none; border-color: #6366f1; }
        select { width: 100%; padding: 12px; background: #1a1a1a; border: 1px solid #333;
                 border-radius: 8px; color: #e5e5e5; font-size: 14px; margin-bottom: 16px; }
        button { width: 100%; padding: 14px; background: #6366f1; color: white; border: none;
                 border-radius: 8px; font-size: 16px; font-weight: 600; cursor: pointer;
                 transition: background 0.2s; }
        button:hover { background: #4f46e5; }
        button:disabled { background: #333; cursor: not-allowed; }
        .result { margin-top: 24px; padding: 20px; background: #1a1a1a; border: 1px solid #333;
                  border-radius: 8px; display: none; }
        .result h3 { margin-bottom: 12px; color: #6366f1; }
        .suggestions { margin-top: 16px; }
        .suggestions li { margin-bottom: 6px; color: #aaa; font-size: 14px; }
        .usage-bar { margin-top: 24px; padding: 12px; background: #1a1a1a;
                     border-radius: 8px; font-size: 13px; color: #888; }
        .upgrade-prompt { display: none; margin-top: 16px; padding: 16px;
                          background: #1e1b4b; border: 1px solid #6366f1;
                          border-radius: 8px; text-align: center; }
        .upgrade-prompt a { color: #6366f1; font-weight: 600; }
    </style>
</head>
<body>
    <h1>Cold Email Rewriter</h1>
    <p class="subtitle">Paste your draft. Get a higher-response version in seconds.</p>

    <textarea id="emailInput" placeholder="Paste your cold email draft here..."></textarea>

    <select id="toneSelect">
        <option value="professional">Professional</option>
        <option value="casual">Casual</option>
        <option value="friendly">Friendly</option>
    </select>

    <button id="rewriteBtn" onclick="rewriteEmail()">Rewrite Email</button>

    <div class="result" id="resultBox">
        <h3>✉️ Rewritten Email</h3>
        <p id="rewrittenText"></p>
        <p style="margin-top:8px;font-size:13px;color:#888;">
            Word count: <span id="wordCount"></span>
        </p>
        <ul class="suggestions" id="suggestionsList"></ul>
    </div>

    <div class="usage-bar" id="usageBar">
        Free uses remaining: <span id="usesLeft">3</span> / 3
    </div>

    <div class="upgrade-prompt" id="upgradePrompt">
        You have used all free rewrites. <a href="#upgrade">Upgrade to Pro</a> for unlimited rewrites — $9/month.
    </div>

    <script>
        let usesRemaining = 3;

        async function rewriteEmail() {
            const email = document.getElementById('emailInput').value;
            const tone = document.getElementById('toneSelect').value;
            const btn = document.getElementById('rewriteBtn');

            if (!email.trim()) { alert('Please paste an email first.'); return; }
            if (usesRemaining <= 0) {
                document.getElementById('upgradePrompt').style.display = 'block';
                return;
            }

            btn.disabled = true;
            btn.textContent = 'Rewriting...';

            try {
                const res = await fetch('/api/ai/rewrite', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ original_email: email, tone: tone })
                });

                if (!res.ok) throw new Error('Request failed');
                const data = await res.json();

                document.getElementById('rewrittenText').textContent = data.rewritten_email;
                document.getElementById('wordCount').textContent = data.word_count;
                const list = document.getElementById('suggestionsList');
                list.innerHTML = '';
                data.suggestions.forEach(s => {
                    const li = document.createElement('li');
                    li.textContent = s;
                    list.appendChild(li);
                });
                document.getElementById('resultBox').style.display = 'block';

                usesRemaining--;
                document.getElementById('usesLeft').textContent = usesRemaining;

                if (usesRemaining <= 0) {
                    document.getElementById('upgradePrompt').style.display = 'block';
                }
            } catch (err) {
                alert('Something went wrong. Please try again.');
            } finally {
                btn.disabled = false;
                btn.textContent = 'Rewrite Email';
            }
        }
    </script>
</body>
</html>
```

Save the file. Restart your development server (press Ctrl+C in the Shell, then run `python main.py` again). Open the Webview. You should see a dark-themed page with a textarea, a tone dropdown, and a "Rewrite Email" button.

**Test it:** Paste a cold email draft, select a tone, and click "Rewrite Email." You should see a rewritten version appear below with word count and improvement suggestions. Do you see the rewritten email? If you get an error, check your OpenAI API key in Secrets. If the page does not load, check that `main.py` mounts the static directory correctly.

### Add Stripe Checkout for Subscriptions

Open `routers/billing.py` and add:

```python
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
import os
import stripe

router = APIRouter(prefix="/api/billing", tags=["Billing"])

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

# Price ID — create this in Stripe Dashboard > Products
PRICE_ID = os.environ.get("STRIPE_PRICE_ID", "price_placeholder")

class CheckoutRequest(BaseModel):
    email: str

@router.post("/create-checkout-session")
async def create_checkout(request: CheckoutRequest):
    try:
        session = stripe.checkout.Session.create(
            mode="subscription",
            payment_method_types=["card"],
            line_items=[{"price": PRICE_ID, "quantity": 1}],
            customer_email=request.email,
            success_url="https://your-app.replit.app/?success=true",
            cancel_url="https://your-app.replit.app/?canceled=true",
        )
        return {"url": session.url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")
    webhook_secret = os.environ.get("STRIPE_WEBHOOK_SECRET", "")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        customer_email = session["customer_email"]
        # TODO: Update user record — set tier to "pro"
        print(f"New subscriber: {customer_email}")

    elif event["type"] == "customer.subscription.deleted":
        subscription = event["data"]["object"]
        # TODO: Downgrade user to free tier
        print(f"Subscription cancelled: {subscription['id']}")

    return {"status": "success"}
```

Before testing Stripe, you need to create a Product and Price in your Stripe Dashboard:

1. Go to dashboard.stripe.com/products
2. Click **Add Product**
3. Name: "Cold Email Rewriter Pro"
4. Pricing: Recurring, $9/month
5. Click **Save Product**
6. Copy the Price ID (starts with `price_`) and add it as a Replit Secret: `STRIPE_PRICE_ID`

**Interactive check-in:** Test the checkout flow by calling the API. In the Shell, run:

```bash
curl -X POST http://localhost:8000/api/billing/create-checkout-session \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com"}'
```

You should see a JSON response with a `"url"` field containing a Stripe checkout link. Open that URL in a new browser tab. Use Stripe's test card (`4242 4242 4242 4242`, any future expiry, any CVC) to complete the payment. Did the Stripe test payment succeed? You should see a "Payment successful" confirmation page. If you get an error about the Price ID, go back to your Stripe Dashboard and verify the Price ID matches your Secret. If you get an authentication error, verify your Stripe secret key is correct.

## Step 4: Add User Authentication and Usage Limits

Authentication and usage limits are what separate a toy from a product. Without them, you cannot enforce free/paid tiers or track who is using your service.

### Set Up Clerk Authentication

Go to dashboard.clerk.com. Create a new application named "Cold Email Rewriter." Enable Email/Password sign-in. Copy the **Publishable Key** (starts with `pk_test_`) and **Secret Key** (starts with `sk_test_`). Add the Secret Key to your Replit Secrets as `CLERK_SECRET_KEY`.

Open `routers/auth.py` and add:

```python
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
import os
import jwt

router = APIRouter(prefix="/api/auth", tags=["Auth"])

CLERK_SECRET = os.environ.get("CLERK_SECRET_KEY", "")

# In-memory user store (replace with database for production)
users_db = {}

class UserUsage(BaseModel):
    email: str
    tier: str = "free"        # free or pro
    rewrites_used: int = 0
    rewrites_limit: int = 3   # free = 3, pro = unlimited

def get_user(email: str) -> UserUsage:
    if email not in users_db:
        users_db[email] = UserUsage(email=email)
    return users_db[email]

def verify_clerk_token(request: Request) -> str:
    """Extract and verify Clerk session token. Returns user email."""
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing auth token")

    token = auth_header.split(" ")[1]
    try:
        # Decode without full verification for dev (production: verify with Clerk JWKS)
        payload = jwt.decode(token, options={"verify_signature": False})
        email = payload.get("email_address", "")
        if not email:
            raise HTTPException(status_code=401, detail="Invalid token")
        return email
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.get("/me")
async def get_current_user(request: Request):
    email = verify_clerk_token(request)
    user = get_user(email)
    return {
        "email": user.email,
        "tier": user.tier,
        "rewrites_used": user.rewrites_used,
        "rewrites_limit": user.rewrites_limit,
        "is_pro": user.tier == "pro"
    }

@router.post("/upgrade")
async def upgrade_user(request: Request):
    email = verify_clerk_token(request)
    user = get_user(email)
    user.tier = "pro"
    user.rewrites_limit = 999999
    return {"status": "upgraded", "tier": "pro"}
```

Now update the AI router to enforce usage limits. Open `routers/ai.py` and modify the rewrite endpoint. Add this import at the top:

```python
from routers.auth import verify_clerk_token, get_user
```

Then add this block at the beginning of the `rewrite_email` function, before the OpenAI call:

```python
    # Check authentication and usage limits
    try:
        email = verify_clerk_token(request=request._request)
        user = get_user(email)
        if user.tier == "free" and user.rewrites_used >= user.rewrites_limit:
            raise HTTPException(
                status_code=403,
                detail="Free tier limit reached. Upgrade to Pro for unlimited rewrites."
            )
    except HTTPException as e:
        if e.status_code == 401:
            # Allow anonymous usage with separate tracking (simpler for MVP)
            pass
        else:
            raise
```

And add this after a successful rewrite (before the return statement):

```python
    # Increment usage counter
    try:
        email = verify_clerk_token(request=request._request)
        user = get_user(email)
        user.rewrites_used += 1
    except:
        pass  # Anonymous user, handled by frontend counter
```

**Important:** The `request._request` access is a simplification for this guide. In production, pass the `Request` object properly through FastAPI dependency injection.

### Add the Clerk Frontend Widget

Add this script tag to `static/index.html`, right before `</head>`:

```html
<script
    async
    data-clerk-publishable-key="pk_test_YOUR_KEY_HERE"
    src="https://cdn.jsdelivr.net/npm/@clerk/clerk-js@5/dist/clerk.browser.js">
</script>
```

Replace `pk_test_YOUR_KEY_HERE` with your actual Clerk Publishable Key.

### Set Up Rate Limiting

For basic rate limiting without external dependencies, add this to `main.py`:

```python
from fastapi import Request
from fastapi.responses import JSONResponse
import time

rate_limit_store = {}

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    # Only rate limit the AI endpoint
    if "/api/ai" not in request.url.path:
        return await call_next(request)

    client_ip = request.client.host
    now = time.time()

    if client_ip in rate_limit_store:
        last_request = rate_limit_store[client_ip]
        if now - last_request < 2:  # 2 seconds between requests
            return JSONResponse(
                status_code=429,
                content={"detail": "Too many requests. Please wait a moment."}
            )

    rate_limit_store[client_ip] = now
    return await call_next(request)
```

This limits each IP to one AI request every 2 seconds. For production, use a proper rate limiter like `slowapi` and key by user ID instead of IP.

### Test the Free vs Paid Flow

**Interactive check-in:** Sign up as a free user. Make 3 rewrite requests. After the third, does the usage counter show 0 remaining? Does the upgrade prompt appear? If you see "Free uses remaining: 0 / 3" and the upgrade prompt is visible, your free tier logic is working. If the counter does not decrease, check that the JavaScript in `index.html` is updating the `usesLeft` span. If the upgrade prompt does not appear, check that the `usesRemaining <= 0` condition in the JavaScript is being evaluated.

Next, test the upgrade path: call the `/api/auth/upgrade` endpoint (or simulate it by setting a user's tier to "pro" in `users_db`). Then make additional rewrite requests. They should succeed without the limit message.

## Step 5: Deploy and Launch

Your product works locally. Now it needs to be accessible to anyone with a URL.

### Deploy on Replit

In the Replit IDE, click the **Deploy** button in the top-right corner (it looks like a rocket). Replit will present deployment options:

- **Deployments type:** Select "Cloud Run" (the managed option)
- **Machine:** Select the $0.12/day tier (sufficient for launch traffic)
- **Build command:** `pip install -r requirements.txt`
- **Run command:** `python main.py`
- **Port:** `8000`

Click **Deploy.** Replit will build and deploy your application. This takes 2-5 minutes.

When deployment completes, Replit gives you a URL like `cold-email-rewriter-xyz123.replit.app`. Open this URL in a new browser tab.

**Do you see your landing page?** You should see the same interface you saw locally — the dark-themed page with the textarea and "Rewrite Email" button. If you see a 502 error, the server is still starting. Wait 60 seconds and refresh. If you see a different error, check the deployment logs in the Replit Deployments tab.

### Set Up a Custom Domain

A custom domain looks more professional and builds trust. In the Replit Deployments tab, click **Settings** > **Custom Domain.** Enter your domain name (e.g., `coldemailrewriter.com`). Replit will give you DNS records to add:

1. Go to your domain registrar (Namecheap, Cloudflare, etc.)
2. Add a CNAME record pointing your domain to the Replit-provided target
3. Wait 10-60 minutes for DNS propagation
4. Replit will automatically provision an SSL certificate

### Set Up Monitoring and Error Tracking

For a micro-product, you do not need a complex observability stack. Add this lightweight error tracking to `main.py`:

```python
import logging
import traceback
from fastapi.responses import JSONResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {traceback.format_exc()}")
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred. Please try again."}
    )
```

For production monitoring, sign up for a free Sentry account (sentry.io) and add the SDK:

```bash
pip install sentry-sdk[fastapi]
```

Then add to `main.py` before the app initialization:

```python
import sentry_sdk

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN", ""),
    traces_sample_rate=0.1,
)
```

Add `SENTRY_DSN` to your Replit Secrets. You will get this from the Sentry project settings page.

### Create the Landing Page

Your `index.html` is functional but it is not a landing page — it is the product itself. You need a page that communicates value before the visitor tries the tool. Replace the content of `static/index.html` with a landing page that has the tool embedded below it. Alternatively, create `static/landing.html` and redirect `/` to it while moving the tool to `/app`.

A high-converting landing page needs exactly five elements:

1. **Headline:** One sentence that states the benefit. Not the feature. "Write cold emails that get replies" — not "AI-powered email rewriting tool."
2. **Subheadline:** One sentence that adds specificity. "Average response rate increases 3x for Pro users."
3. **Social proof:** Even at launch, you can show a counter ("127 emails rewritten today") or a testimonial from your beta testers.
4. **Free trial CTA:** "Try it free — 3 rewrites, no signup required." Remove every barrier between the visitor and their first experience of value.
5. **Pricing:** Visible, simple, one tier. "$9/month for unlimited rewrites. Cancel anytime."

**Interactive check-in:** Visit your live URL. Does the landing page load? Test the full signup flow: visit the page, paste an email, click rewrite, see the result, hit the free limit, see the upgrade prompt, click upgrade, complete Stripe checkout (test mode). Does every step work end-to-end? If any step breaks, fix it before launching. A broken checkout flow at launch is unrecoverable — users who hit a bug will not come back.

## Step 6: Acquire Your First 100 Users

Your product is live. Nobody knows it exists. Here is how to fix that.

### Product Hunt Launch Strategy

Product Hunt can drive 500-2,000 visitors in a single day if you execute well. Here is the playbook:

1. **Schedule your launch** on a Tuesday or Wednesday (highest traffic days). Avoid weekends and Mondays.
2. **Prepare your assets** 48 hours before: a 60-second demo video (use Loom), 3-4 screenshots, a clear tagline ("AI cold email rewriter that 3xes your response rate"), and a first comment that explains why you built this.
3. **Build your "upvote squad"** — tell 15-20 people in your network to upvote and comment on launch day. Not all at once — stagger them between 6am and 12pm PST.
4. **Respond to every comment** within 30 minutes. Engagement signals push you up the algorithm.
5. **Offer a launch discount** — 50% off the first 3 months for Product Hunt users. Create a Stripe coupon and mention it in your first comment.

**Expected result:** 200-800 visitors, 20-80 signups, 3-10 paid conversions on launch day.

### Community Posting Templates

Post in communities where your target users already are. For a cold email tool, that is r/Entrepreneur, r/SaaS, r/sales, Indie Hackers, and relevant Slack communities. Use this template — adjust the brackets:

**Reddit post title:** "I built an AI tool that rewrites cold emails to get more replies — 3 free rewrites, no signup"

**Reddit post body:**
> I was spending 2+ hours a day writing and rewriting cold outreach emails. My response rate was stuck at 3%. So I built a tool that uses GPT-4 to rewrite your drafts with better hooks, clearer asks, and more effective tone. My response rate went from 3% to 9%.
>
> It is simple: paste your draft, pick a tone, get a better version. 3 free rewrites, then $9/month for unlimited.
>
> Would love feedback from anyone who sends cold emails regularly. What would make this more useful for you?

**Do not:** post in more than 2 subreddits per day, use marketing language ("revolutionary," "game-changing"), or skip engaging with comments. Reddit detects and punishes self-promotion that does not contribute value.

### Cold Outreach for B2B Micro-SaaS

If your tool serves a business function (and a cold email rewriter absolutely does), direct outreach is your highest-converting channel. Here is the method:

1. Build a list of 200 prospects. Use Apollo.io (free tier gives 50 emails/month) or LinkedIn Sales Navigator. Target: sales reps, SDRs, founders of B2B companies with 1-50 employees.
2. Send this email:

> Subject: your cold emails
>
> Hi [Name],
>
> I noticed [specific observation about their company/role]. I built a tool that rewrites cold emails to get more replies — it takes a draft you have and sharpens the hook, ask, and tone.
>
> 3 free rewrites, no signup: [your URL]
>
> If it helps, great. If not, no worries.
>
> [Your name]

3. Send 20 per day. Track opens and replies. After 5 business days, follow up with anyone who opened but did not reply: "Hey [Name], just bumping this — the free rewrites reset weekly if you want to try it."

**Expected conversion rate:** 5-15% of people who open the email will try the tool. 10-20% of those will hit the paywall. 5-10% of those will subscribe. At 20 outreach emails/day, expect 1-3 new paying users per week.

### Pricing Strategy

For micro-SaaS, pricing is simple:

| Tier | Price | Includes | Target User |
|------|-------|----------|-------------|
| Free | $0 | 3 rewrites per week | Try-before-you-buy users |
| Pro | $9/month | Unlimited rewrites, all tones, priority processing | Individual sellers, freelancers |
| Team | $29/month | 5 seats, shared templates, usage analytics | Small sales teams |

Start with Free + Pro. Add Team when users start asking for it (they will — this is how you know the market is ready for a higher tier).

Do not price below $9/month. A $5/month product attracts support-heavy users who cost more in OpenAI API calls than they pay in subscription revenue. A $9/month product attracts professionals who value their time.

## Cost Breakdown

| Item | Free Tier | Paid Tier | When to Upgrade |
|------|-----------|-----------|-----------------|
| Replit | Free (limited) | $0.12/day Cloud Run | At launch — you need a stable URL |
| OpenAI API | $5 credit (pay per use) | ~$0.15 per 1K output tokens | Scales with usage; monitor daily |
| Stripe | Free | 2.9% + 30c per transaction | Always use — no free alternative |
| Clerk | Free (10K MAU) | $25/mo (Pro, 100K MAU) | At 10,000+ monthly active users |
| Custom Domain | — | $10-12/year | Immediately — builds trust |
| Sentry | Free (5K errors/mo) | $26/mo (Team) | At 5,000+ monthly errors |
| Email (Resend) | Free (100 emails/day) | $20/mo (Pro) | When sending transactional emails |

**Total monthly cost at 50 users (10 paying):** ~$15-25/mo
**Total monthly revenue at 50 users (10 paying):** $90/mo (10 × $9)
**Break-even:** ~15 paying users

Your primary variable cost is OpenAI API usage. At $0.15 per 1K output tokens, each rewrite costs approximately $0.003-0.01. A Pro user doing 100 rewrites/month costs you $0.30-1.00 in API calls and pays you $9. That is an 89-97% gross margin. This is why AI micro-SaaS is attractive — the unit economics are exceptional once you cross the break-even point.

## Production Checklist

Before announcing your product publicly, verify every item:

- [ ] AI endpoint returns accurate, relevant rewrites (tested with 20+ different inputs)
- [ ] Stripe checkout completes successfully in test mode and live mode
- [ ] Webhook handler updates user tier correctly on subscription creation and deletion
- [ ] Free tier enforces usage limits — users cannot bypass the 3-rewrite cap
- [ ] Upgrade prompt appears when free limit is reached and links to working checkout
- [ ] Authentication flow works end-to-end — sign up, sign in, sign out, session persistence
- [ ] Rate limiting prevents abuse — no more than 1 request per 2 seconds per user
- [ ] Error tracking is active — Sentry (or equivalent) captures unhandled exceptions
- [ ] Landing page loads in under 3 seconds on mobile and desktop
- [ ] Custom domain is configured with SSL certificate (HTTPS, not HTTP)

## What to Do Next

Once you have 50-100 users and 10-20 paying subscribers, expand:

- **Add templates.** Let Pro users save and reuse rewrite templates ("SaaS follow-up," "investor outreach," "job application"). This increases retention because saved templates are switching costs.
- **Integrate with email tools.** Build a Chrome extension that works inside Gmail, Outlook, or Apollo. This removes the copy-paste step and dramatically increases usage frequency.
- **Add team features.** Shared rewrite history, team templates, and usage analytics. Price it at $29/month per team. Team plans have lower churn than individual plans.
- **Build a second micro-product.** Use the same stack, the same deployment, the same auth — just swap the AI prompt and the UI. Your second product is 50% faster to build because the infrastructure is reusable.
- **Explore affiliate distribution.** Offer sales trainers and consultants a 30% recurring commission for every user they refer. Affiliates who already have audiences in your target market will acquire users faster than you can.
