---
title: "Build, Configure, and Deploy an AI Appointment Booking System with Vapi and Calendly"
date: 2026-04-30
category: "Implementation"
difficulty: "INTERMEDIATE"
readTime: "35 MIN"
excerpt: "This is the execution guide for building the AI Appointment Booking Automation business we outlined in our opportunity deep‑dive. Follow the steps below and you'll have a fully‑functional, voice‑powered scheduling system that can be sold to medical practices, law firms, or any service‑based business..."
image: "/images/articles/intelligence/build-and-deploy-ai-appointment-booking-systems-with-vapi-and-calendly.png"
heroImage: "/images/heroes/intelligence/build-and-deploy-ai-appointment-booking-systems-with-vapi-and-calendly.png"
relatedOpportunity: "/opportunities/how-to-launch-an-ai-appointment-booking-automation-business-in-2026-2k15kmonth/"
---

This is the execution guide for building the **AI Appointment Booking Automation** business we outlined in our opportunity deep‑dive. Follow the steps below and you will have a fully‑functional, voice‑powered scheduling system that can be sold to medical practices, law firms, or any service‑based business that needs to reduce no‑shows and manual booking overhead.

Ready to understand the full business opportunity? Read our [opportunity deep‑dive](/opportunities/how-to-launch-an-ai-appointment-booking-automation-business-in-2026-2k15kmonth/).

---

## Prerequisites

| Item | Account / Tool | Cost | Setup Time |
|------|----------------|------|------------|
| Voice AI platform | [**Vapi**](https://vapi.ai/) | $19 / month (Starter) | 5 min |
| Scheduling API | **Calendly** | Free (Basic) | 5 min |
| Automation & webhook | [**Make.com**](https://www.make.com/en/register?pc=menshly) | $9 / month (Starter) | 5 min |
| Cloud IDE & runtime | [**Replit**](https://replit.com/refer/egwuokwor) | Free tier | 5 min |
| Web hosting | **Hostinger** | $3.95 / month (Single Shared) | 10 min |
| Knowledge base | [**Notion**](https://notion.so/) | Free | 5 min |
| AI assistant | **ChatGPT** | $20 / month | 5 min |
| TTS synthesis | [**ElevenLabs**](https://elevenlabs.io/) | $10 / month | 5 min |
| Email marketing | **Klaviyo** | $20 / month | 10 min |
| **Total upfront cost** | | **$88.95 / month** | |

> **Note:** All costs are the lowest paid tiers that include the APIs we will use. You can start on free tiers and upgrade after you validate the business model. The total monthly investment is less than a single client pays you, so the unit economics work from day one.

---

## Step 1: Setup Accounts and API Keys

> **Goal:** Create all necessary accounts, generate API keys, and store them securely in Replit's secrets manager.

### 1.1 Create a Vapi Account

1. Navigate to **https://app.vapi.io**.
2. Click **Sign Up** and enter your email and password, then click **Create Account**.
3. Verify your email address through the confirmation link sent to your inbox.
4. Log in to the Vapi dashboard.
5. In the dashboard, click **Manage API Keys** and then **Create Key**.
6. Name the key `PROD_VAPI_KEY`, set the scope to **Read & Write**, and click **Create**.
7. Copy the key to your clipboard immediately — Vapi will not display it again after you navigate away from the page.

> **Check‑in:** Do you see "Manage API Keys" under the **Settings** menu? If not, ensure you are in the **Admin** view. Log out and log back in if necessary.

### 1.2 Create a Calendly Account

1. Go to **https://calendly.com** and sign up with your email address.
2. Complete the onboarding wizard: set your timezone, default meeting duration, and available hours.
3. In the **Integrations** tab, click **API & Webhooks**.
4. Click **Generate New API Key** and name it `CAL_API_KEY`.
5. Copy the key to your clipboard.
6. While you are in the API settings, copy your **Organization URI** and **User URI** — you will need both for programmatic scheduling.

> **Check‑in:** Do you see your API key listed under "API Keys" with a 32‑character string? If you see "API Key expired", click **Regenerate** and copy the new key.

### 1.3 Create a Make.com Account

1. Visit **https://www.make.com** and sign up with your email and password.
2. In the dashboard, click **Create new scenario**.
3. Choose **Webhook** as your first module and set it to **Custom webhook**.
4. Copy the **Webhook URL** — it looks like `https://hook.integromat.com/xxxxxx`. You will paste this into Vapi later.
5. Name the scenario "Vapi Booking Webhook" and save it.

> **Check‑in:** Do you see a "Webhook" module with a URL that starts with `https://hook.integromat.com/`? If yes, proceed. If no, make sure you selected the **HTTP > Webhooks** module and that it is set to **"Custom webhook"**.

### 1.4 Store API Keys in Replit Secrets

1. Go to **Replit.com**, click **New Repl**, and select the **Python** template.
2. Name the repl `vapi-calendly-booker`.
3. In the left sidebar, click the **Secrets (Environment Variables)** icon (the lock symbol).
4. Add the following secrets one at a time:

   | Key | Value |
   |-----|-------|
   | `VAPI_KEY` | Your Vapi API key |
   | `CALENDLY_KEY` | Your Calendly API key |
   | `CALENDLY_USER_URI` | Your Calendly User URI |
   | `MAKESHOP_URL` | Your Make.com webhook URL |
   | `ELEVENLABS_KEY` | ElevenLabs API key (optional) |
   | `KLAVIYO_API_KEY` | Klaviyo API key (optional) |

5. **Check‑in:** Do you see a green checkmark next to each secret? If not, delete the entry and re‑enter the key name and value carefully — typos in secret names are the number one cause of "key not found" errors at runtime.

### 1.5 Verify Connectivity

Open the Replit Shell and run:

```bash
curl -I https://api.vapi.io
```

You should receive `HTTP/2 200`. If you see `401 Unauthorized`, your `VAPI_KEY` is incorrect. Verify it in the Vapi dashboard and update the Replit secret. Test Calendly connectivity with:

```bash
curl -H "Authorization: Bearer $CALENDLY_KEY" https://api.calendly.com/users/me
```

You should see a JSON response with your user profile. If you get a 401, regenerate the Calendly API key.

---

## Step 2: Build the Vapi Voice Agent

### 2.1 Configure the Voice Agent in Vapi Dashboard

1. In the Vapi dashboard, click **Create Assistant**.
2. Set the assistant name to `BookingAgent`.
3. Under **Voice**, select a voice from the ElevenLabs library. Choose a voice that matches your target vertical — a warm, professional female voice works well for dental and medical practices; a confident, direct male voice suits legal and financial services.
4. Under **Model**, select `gpt-4o-mini` for cost efficiency. You can upgrade to `gpt-4o` later if the client needs more nuanced conversation handling.
5. Under **System Prompt**, paste the following template and customize it for your client:

```
You are a professional appointment booking agent for [BUSINESS NAME], a [VERTICAL] practice in [CITY]. Your job is to:

1. Greet the caller warmly and ask how you can help them today.
2. Determine what type of appointment they need (e.g., cleaning, consultation, follow-up, emergency).
3. Check available time slots using the Calendly integration.
4. Offer the next 3 available slots and let the caller choose.
5. Confirm the booking by repeating the date, time, and appointment type.
6. Ask if they would like an email or SMS confirmation.
7. Thank them and end the call professionally.

Rules:
- Never give medical, legal, or financial advice.
- If the caller asks a question you cannot answer, say "Let me connect you with a team member who can help with that."
- Always confirm the booking details before ending the call.
- Speak at a natural pace — not too fast, not too slow.
- Use the business's preferred terminology (e.g., "visit" not "appointment" for dental practices).
```

6. Under **Functions**, add a new function called `check_availability` with the following schema:

```json
{
  "name": "check_availability",
  "description": "Check available appointment slots in Calendly",
  "parameters": {
    "type": "object",
    "properties": {
      "event_type": {
        "type": "string",
        "description": "Type of appointment (cleaning, consultation, follow-up)"
      },
      "date_range_start": {
        "type": "string",
        "description": "Start date in YYYY-MM-DD format"
      },
      "date_range_end": {
        "type": "string",
        "description": "End date in YYYY-MM-DD format"
      }
    },
    "required": ["event_type", "date_range_start", "date_range_end"]
  }
}
```

7. Add a second function called `book_appointment`:

```json
{
  "name": "book_appointment",
  "description": "Book an appointment in Calendly",
  "parameters": {
    "type": "object",
    "properties": {
      "event_type": { "type": "string" },
      "start_time": { "type": "string", "description": "ISO 8601 datetime" },
      "caller_name": { "type": "string" },
      "caller_email": { "type": "string" },
      "caller_phone": { "type": "string" }
    },
    "required": ["event_type", "start_time", "caller_name", "caller_email"]
  }
}
```

8. Under **Server URL**, enter your Make.com webhook URL. Vapi will POST function call payloads to this URL whenever the AI agent needs to check availability or book an appointment.
9. Click **Save** and then **Test** to verify the agent responds correctly to a simulated call.

### 2.2 Test the Voice Agent

Click **Call** in the Vapi dashboard to place a test call to your own phone number. Walk through the entire booking flow:

- Say "I'd like to schedule a cleaning."
- When the agent offers time slots, choose one.
- Confirm the booking.
- Check that the function call payload arrived in your Make.com scenario.

If the agent does not call the functions, check that the **Server URL** is correct and that your Make.com webhook is active (it must receive at least one test payload before it starts listening for real data).

---

## Step 3: Build the Make.com Automation Scenarios

### 3.1 Scenario 1: Check Availability

This scenario receives a `check_availability` function call from Vapi, queries the Calendly API, and returns available slots.

1. In Make.com, create a new scenario called "Check Availability."
2. Add a **Webhook** module as the trigger. Use the same webhook URL you configured in Vapi.
3. Add a **HTTP** module configured as follows:
   - Method: `GET`
   - URL: `https://api.calendly.com/user_availability_schedules`
   - Headers: `Authorization: Bearer {{CALENDLY_KEY}}`
4. Add a **JSON Parser** module to extract the available time slots from the Calendly response.
5. Add a **Webhook Response** module that returns the available slots to Vapi in the format it expects:

```json
{
  "result": [
    {"start_time": "2026-05-05T09:00:00Z", "end_time": "2026-05-05T09:30:00Z"},
    {"start_time": "2026-05-05T10:00:00Z", "end_time": "2026-05-05T10:30:00Z"},
    {"start_time": "2026-05-05T14:00:00Z", "end_time": "2026-05-05T14:30:00Z"}
  ]
}
```

6. Save and activate the scenario.

### 3.2 Scenario 2: Book Appointment

This scenario receives a `book_appointment` function call, creates the booking in Calendly, sends a confirmation email, and logs the booking in the CRM.

1. Create a new scenario called "Book Appointment."
2. Add a **Webhook** module as the trigger.
3. Add an **HTTP** module to create the Calendly booking:
   - Method: `POST`
   - URL: `https://api.calendly.com/scheduled_events`
   - Headers: `Authorization: Bearer {{CALENDLY_KEY}}`, `Content-Type: application/json`
   - Body:
   ```json
   {
     "event_type": "{{1.event_type}}",
     "start_time": "{{1.start_time}}",
     "invitee": {
       "name": "{{1.caller_name}}",
       "email": "{{1.caller_email}}",
       "phone": "{{1.caller_phone}}"
     }
   }
   ```
4. Add an **Email** module to send a confirmation to the caller:
   - To: `{{1.caller_email}}`
   - Subject: `Your Appointment is Confirmed — [BUSINESS NAME]`
   - Body: Include the appointment date, time, type, and a link to reschedule or cancel.
5. Add an **HTTP** module to log the booking in ActiveCampaign or Klaviyo (optional but highly recommended for churn prevention).
6. Add a **Webhook Response** module to confirm the booking back to Vapi:

```json
{
  "result": "Booking confirmed for {{1.caller_name}} on {{1.start_time}}. Confirmation email sent."
}
```

7. Save and activate the scenario.

### 3.3 Scenario 3: Appointment Reminders

This scenario runs on a schedule and sends automated reminders to reduce no‑shows.

1. Create a new scenario called "Appointment Reminders."
2. Add a **Scheduler** trigger set to run every hour.
3. Add an **HTTP** module to fetch upcoming Calendly events within the next 24 hours.
4. Add an **Iterator** module to loop through each event.
5. Add a **Filter** module that passes only events where a reminder has not yet been sent (track this with a custom field in your CRM).
6. Add an **SMS** module (via Twilio or ClickSend) to send a reminder: "Hi {{name}}, this is a reminder that you have an appointment at {{business_name}} tomorrow at {{time}}. Reply C to confirm or R to reschedule."
7. Add an **HTTP** module to update the CRM record marking the reminder as sent.
8. Save and activate the scenario.

---

## Step 4: Build the Replit Webhook Handler

While Make.com handles most of the automation logic visually, you need a lightweight server to handle edge cases, custom transformations, and fallback logic. This is your Replit app.

### 4.1 Project Structure

```
/vapi-calendly-booker
├── app.py              # Flask webhook server
├── calendly.py         # Calendly API wrapper
├── requirements.txt    # Python dependencies
└── .env               # Environment variables (for local dev)
```

### 4.2 Install Dependencies

Open the Replit Shell and run:

```bash
pip install flask requests python-dotenv
pip freeze > requirements.txt
```

### 4.3 The Webhook Server (app.py)

```python
import os
import json
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

VAPI_KEY = os.getenv("VAPI_KEY")
CALENDLY_KEY = os.getenv("CALENDLY_KEY")
CALENDLY_USER_URI = os.getenv("CALENDLY_USER_URI")

@app.route("/vapi/webhook", methods=["POST"])
def vapi_webhook():
    """Handle function calls from Vapi voice agent."""
    payload = request.json
    function_name = payload.get("function", {}).get("name")
    arguments = payload.get("function", {}).get("arguments", {})

    if function_name == "check_availability":
        return handle_check_availability(arguments)
    elif function_name == "book_appointment":
        return handle_book_appointment(arguments)
    else:
        return jsonify({"error": f"Unknown function: {function_name}"}), 400

def handle_check_availability(args):
    """Query Calendly for available slots."""
    event_type = args.get("event_type")
    start_date = args.get("date_range_start")
    end_date = args.get("date_range_end")

    headers = {"Authorization": f"Bearer {CALENDLY_KEY}"}
    params = {
        "user": CALENDLY_USER_URI,
        "start_time": f"{start_date}T00:00:00Z",
        "end_time": f"{end_date}T23:59:59Z",
    }

    response = requests.get(
        "https://api.calendly.com/user_availability_schedules",
        headers=headers,
        params=params,
    )

    if response.status_code != 200:
        return jsonify({"result": "I'm sorry, I couldn't check availability right now. Please try again."})

    slots = parse_available_slots(response.json())
    return jsonify({"result": format_slots_for_voice(slots)})

def handle_book_appointment(args):
    """Create a booking in Calendly."""
    headers = {
        "Authorization": f"Bearer {CALENDLY_KEY}",
        "Content-Type": "application/json",
    }
    booking_data = {
        "event_type": args.get("event_type"),
        "start_time": args.get("start_time"),
        "invitee": {
            "name": args.get("caller_name"),
            "email": args.get("caller_email"),
            "phone": args.get("caller_phone", ""),
        },
    }

    response = requests.post(
        "https://api.calendly.com/scheduled_events",
        headers=headers,
        json=booking_data,
    )

    if response.status_code in (200, 201):
        return jsonify({"result": f"Booking confirmed for {args.get('caller_name')} on {args.get('start_time')}. A confirmation email has been sent."})
    else:
        return jsonify({"result": "I'm sorry, I couldn't complete the booking. Please try again or call the office directly."})

def parse_available_slots(data):
    """Extract and format available time slots from Calendly response."""
    # Implementation depends on Calendly API version
    # This is a simplified example
    slots = []
    for day in data.get("days", []):
        for slot in day.get("slots", []):
            slots.append({
                "start": slot.get("start_time"),
                "end": slot.get("end_time"),
            })
    return slots[:3]  # Return next 3 available slots

def format_slots_for_voice(slots):
    """Format slots into natural language for the voice agent."""
    if not slots:
        return "I'm sorry, there are no available slots in that time range. Would you like to check a different week?"

    messages = []
    for i, slot in enumerate(slots, 1):
        start = slot["start"]
        # Convert to natural language
        day_name = parse_day_name(start)
        time_str = parse_time(start)
        messages.append(f"Option {i}: {day_name} at {time_str}")

    return "I found the following available times: " + ". ".join(messages) + ". Which works best for you?"

def parse_day_name(iso_datetime):
    """Convert ISO datetime to day name."""
    from datetime import datetime
    dt = datetime.fromisoformat(iso_datetime.replace("Z", "+00:00"))
    return dt.strftime("%A, %B %d")

def parse_time(iso_datetime):
    """Convert ISO datetime to readable time."""
    from datetime import datetime
    dt = datetime.fromisoformat(iso_datetime.replace("Z", "+00:00"))
    return dt.strftime("%I:%M %p")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

### 4.4 Deploy and Test

1. Click **Run** in Replit to start the Flask server.
2. Copy the Replit URL (e.g., `https://vapi-calendly-booker.username.repl.co`).
3. Update the Vapi assistant's **Server URL** to point to `https://your-repl.repl.co/vapi/webhook`.
4. Place another test call through the Vapi dashboard and verify that the agent can check availability and book appointments end‑to‑end.

---

## Step 5: Deploy to Production on Hostinger

When you are ready to move off Replit's shared infrastructure, deploy to a Hostinger VPS for reliability and performance.

### 5.1 Server Setup

1. Purchase a Hostinger VPS plan (the $9.99/month plan with 4 GB RAM is sufficient for handling 500+ concurrent webhook requests).
2. SSH into your server: `ssh root@your-server-ip`.
3. Install Python 3, pip, and nginx:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv nginx -y
```

4. Clone your Replit project:

```bash
git clone https://github.com/your-username/vapi-calendly-booker.git
cd vapi-calendly-booker
```

5. Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt gunicorn
```

6. Set environment variables by creating a `.env` file with your production API keys.

### 5.2 Configure Gunicorn as a System Service

Create a systemd service file at `/etc/systemd/system/vapi-booker.service`:

```ini
[Unit]
Description=Vapi Calendly Booking Agent
After=network.target

[Service]
User=www-data
WorkingDirectory=/root/vapi-calendly-booker
Environment="PATH=/root/vapi-calendly-booker/venv/bin"
ExecStart=/root/vapi-calendly-booker/venv/bin/gunicorn -w 4 -b 0.0.0.0:8080 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```bash
sudo systemctl enable vapi-booker
sudo systemctl start vapi-booker
```

### 5.3 Configure Nginx Reverse Proxy

Create an nginx configuration at `/etc/nginx/sites-available/vapi-booker`:

```nginx
server {
    listen 80;
    server_name booking.yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable the site and restart nginx:

```bash
sudo ln -s /etc/nginx/sites-available/vapi-booker /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

Add SSL with Let's Encrypt:

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d booking.yourdomain.com
```

Update the Vapi assistant's **Server URL** to `https://booking.yourdomain.com/vapi/webhook`.

---

## Step 6: Monitoring and Maintenance

### 6.1 Set Up Health Checks

Add a health check endpoint to your Flask app:

```python
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy", "timestamp": datetime.utcnow().isoformat()})
```

Use a free monitoring service like UptimeRobot to ping this endpoint every five minutes. If it goes down, you will get an email alert before your clients notice.

### 6.2 Log All Booking Events

Create a simple logging middleware that records every webhook payload:

```python
import logging

logging.basicConfig(
    filename="bookings.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

@app.before_request
def log_request():
    if request.path.startswith("/vapi"):
        logging.info(f"Webhook received: {request.json}")
```

These logs are invaluable for debugging integration issues and providing audit trails to clients who ask "Did the AI book that appointment correctly?"

### 6.3 Weekly Reporting Dashboard

Build a simple reporting page that displays:

- Total bookings this week vs. last week
- Booking conversion rate (calls received vs. appointments booked)
- No‑show rate for AI‑booked appointments vs. manually booked appointments
- Average time from call to confirmed booking
- Most common appointment types

You can build this with a simple Flask route that queries your booking log and renders an HTML template, or connect the data to a Google Sheet that updates automatically via Make.com.

---

## Step 7: Onboarding Your First Client

### 7.1 Pre‑Onboarding Checklist

Before onboarding a new client, complete the following:

- [ ] Client has signed the service agreement and provided payment details
- [ ] Client has shared their Calendly login or API key
- [ ] Client has provided their business name, address, and preferred terminology
- [ ] Client has confirmed their available hours and appointment types
- [ ] Client has designated a point of contact for technical questions
- [ ] You have created a Vapi assistant with the client's custom system prompt
- [ ] You have configured the Make.com scenarios for the client's specific workflow
- [ ] You have tested the end‑to‑end flow with the client's real Calendly account

### 7.2 Phone Number Provisioning

Purchase a dedicated phone number for each client through Vapi or a provider like Twilio. The number should be local to the client's area code — callers are 40% more likely to answer a local number. Configure the number to forward to the Vapi assistant during business hours and to voicemail after hours.

### 7.3 Go‑Live Process

1. Forward the client's existing phone line to the new AI number (or set up a parallel ring so both the human receptionist and the AI receive calls simultaneously during the transition period).
2. Monitor the first 48 hours of calls closely. Be available to intervene manually if the AI mishandles a call.
3. After 48 hours, review call transcripts with the client and make adjustments to the system prompt, available appointment types, or call routing logic.
4. After two weeks, generate a performance report comparing the AI‑assisted booking rate to the client's historical baseline.

---

## Troubleshooting Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| Vapi agent does not call functions | Server URL not configured or Make.com webhook inactive | Verify Server URL in Vapi dashboard; send a test payload from Make.com |
| Calendly returns 401 | API key is invalid or expired | Regenerate API key in Calendly and update all secrets |
| Voice agent sounds robotic | Wrong voice selected or poor prompt design | Switch to a more natural ElevenLabs voice; add conversational filler to the system prompt |
| Double bookings | Race condition between AI and human booking | Add a 30‑second buffer in Calendly and implement optimistic locking in the webhook handler |
| High no‑show rate despite reminders | Reminder timing is wrong | Test different reminder intervals (48h, 24h, 2h) and channels (SMS vs. email) |
| Client reports missing bookings | CRM sync failure | Check Make.com scenario execution logs; add error‑handling and retry logic |

---

## Recommended Tools

These are the tools we recommend for building and scaling AI automation businesses:

- **[Vapi](https://vapi.ai/)** — AI voice agent platform — build and deploy voice AI
- **[Make.com](https://www.make.com/en/register?pc=menshly)** — Visual automation platform — connect any app without code
- **[ElevenLabs](https://elevenlabs.io/)** — AI voice synthesis — human‑quality voiceovers and agents
- **[Semrush](https://www.semrush.com/)** — SEO and content marketing — outrank your competitors
- **[Replit](https://replit.com/refer/egwuokwor)** — Cloud IDE — build and deploy without infrastructure
