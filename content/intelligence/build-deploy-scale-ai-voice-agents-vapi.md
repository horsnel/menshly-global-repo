---
title: "Build, Deploy, and Scale AI Voice Agents with Vapi: The Complete Step-by-Step Guide"
date: 2026-04-29
category: "Implementation"
difficulty: "INTERMEDIATE"
readTime: "28 MIN"
excerpt: "The complete execution guide for building AI voice agent systems — from Vapi setup to client deployment and scaling your agency."
image: "/images/articles/intelligence/build-deploy-scale-ai-voice-agents-vapi.png"
heroImage: "/images/heroes/intelligence/build-deploy-scale-ai-voice-agents-vapi.png"
relatedOpportunity: "/opportunities/ai-voice-agent-agency-2026/"
---

This is the execution guide for building the AI voice agent business we outlined in our opportunity deep-dive. Voice agents are not chatbots with a microphone attached. They are real-time, full-duplex conversational systems that listen, reason, and respond on a live phone line — and businesses pay premium rates for them because they replace a human sitting at a desk answering calls. This guide covers every configuration screen, every API call, every test scenario, every pricing tier, and every scaling lever. Follow it in order. Do not skip steps.

## Prerequisites

Before you write a single line of configuration, set up these accounts. Every tool listed has a free tier or trial sufficient to build, test, and demo your first voice agent. You will not spend money until you have paying clients.

**Required accounts (create these now):**

- **Vapi account** — go to vapi.ai and sign up for the free tier. Includes 100 minutes/mo of call time and 1 assistant. This is the core voice agent platform.
- **ElevenLabs account** — go to elevenlabs.io and sign up. Free tier includes 10,000 characters/mo of voice synthesis. This provides the human-quality voice for your agent.
- **Make.com account** — go to make.com and sign up. Free tier includes 1,000 operations/mo. This is the automation layer connecting your voice agent to calendars, CRMs, and notifications.
- **Replit account** — go to replit.com and sign up. Free tier includes basic compute. Use this for any custom webhook handlers or middleware you need to build.
- **Calendly account** — go to calendly.com and sign up. Free tier includes 1 event type. This handles availability checking and booking confirmations.
- **Notion workspace** — go to notion.so and sign up. Free tier includes unlimited pages. Use this for SOPs, client dashboards, knowledge base drafting, and project management.

**Additional accounts needed during setup:**

- **OpenAI API key** — go to platform.openai.com/api-keys and generate a key. Load $20 credit. This powers the LLM reasoning inside Vapi. ChatGPT Plus is not required — the API key is what Vapi uses directly.
- **Twilio account** — go to twilio.com and sign up. Free trial includes $20 credit and one phone number. This provides the telephony layer.

**Time required:** 8-10 hours of uninterrupted time for your first complete build, test, and deployment cycle.

**Total upfront cost:** $0 to start, ~$150/mo when scaling. The only immediate spend is $20 for the OpenAI API credit. Everything else remains free until you have paying clients. The Vapi free tier includes 100 minutes of call time per month — sufficient to build, test, and run live demos for 3-5 prospects before upgrading.

## Step 1: Configure Your Vapi Workspace

Open your browser and navigate to dashboard.vapi.ai. Sign in with the account you created. You should see the Vapi dashboard — a left sidebar with navigation items (Assistants, Phone Numbers, Calls, Analytics, Settings) and a main area showing "Assistants" as the default view with an empty list and a **Create Assistant** button.

If you see a blank screen or a loading spinner that never resolves, your email is not verified. Go to your email inbox, find the Vapi verification email, click the confirmation link, and refresh the dashboard.

### Connect Your Telephony Provider

In the left sidebar, click **Phone Numbers**. You will see an empty list and a button labeled **Import Number**. Before you can import a number, you must connect Twilio as a telephony provider.

Click **Connect Provider** in the top-right corner. A modal will appear with provider options. Select **Twilio**. You will be asked for your Twilio Account SID and Auth Token — both are found at twilio.com/console under "Account Info."

Copy the Account SID first. Paste it into the Vapi modal. Then copy the Auth Token. Click **Connect**.

You should see a green "Connected" badge next to Twilio in the provider list. If you see a red error reading "Authentication failed," your Account SID or Auth Token is incorrect — both values are case-sensitive. Go back to the Twilio console and copy them exactly. If you see "Account not verified," Twilio requires you to verify your personal phone number on their platform before making API calls. Go to twilio.com/console/phone-numbers/verified, add your number, and complete the SMS verification.

### Provision a Phone Number

In the Twilio console, navigate to **Phone Numbers → Manage → Buy a Number** (twilio.com/console/phone-numbers/search). Search for a local phone number in your area code. Buy one — this costs $1.15/month on Twilio. After purchasing, note the phone number including the country code (e.g., `+15551234567`).

Go back to the Vapi dashboard. Click **Import Number**. Enter the Twilio phone number you just purchased. Select Twilio as the provider. Click **Import**.

The number should appear in your Vapi Phone Numbers list with a green "Active" status. If you see "Pending," wait 60 seconds and refresh. If you see "Failed," the number is not properly configured in Twilio. Go to the Twilio console, click the phone number, and verify that the "Voice Configuration" webhook URL is set to the Vapi webhook endpoint. Vapi provides this URL during the import flow — copy it from the import modal and paste it into the Twilio "A CALL COMES IN" webhook field. Set the HTTP method to POST.

### Configure the Voice Model

In the left sidebar, click **Voice** (or navigate to your assistant's voice settings). This is where you select the AI model and the voice used for speech synthesis.

Set the following:

- **Model:** GPT-4o (select from the dropdown)
- **Voice Provider:** ElevenLabs
- **Voice:** Select "Rachel" — a professional, warm female voice that works well for business reception scenarios
- **Language:** English

Click **Connect ElevenLabs** next to the voice provider dropdown. A modal will ask for your ElevenLabs API key. Go to elevenlabs.io/app/settings/api-keys, generate a new key, copy it, and paste it into the Vapi modal. Click **Save**.

You should see "Connected" next to the ElevenLabs integration. If you see "Invalid API key," go back to ElevenLabs and regenerate the key — keys occasionally fail on first creation. If you see "Quota exceeded," you have used your free tier allocation; upgrade to the $5/month Starter plan on ElevenLabs.

### Test the Voice Pipeline

Click the **Test Call** button in the top-right corner of the dashboard. A modal will appear with your imported phone number. Enter your personal phone number as the destination. Click **Start Test Call**.

Your phone should ring within 5 seconds. Answer it. You should hear: "Hello, I'm your AI assistant. How can I help you today?" spoken in the Rachel voice.

Diagnostics:

- If you hear silence, the ElevenLabs integration is broken — go back to Voice settings and re-enter the API key.
- If the call never arrives, the Twilio webhook is misconfigured — go back to Phone Numbers and verify the webhook URL.
- If you hear the greeting but the AI cannot hear you respond, the Twilio voice configuration is missing the status callback URL — go to the Twilio console, open the phone number settings, and ensure both the "A CALL COMES IN" webhook and "Status Callback" URL point to Vapi.

If you can hear the AI speak and it can hear you respond, the voice pipeline is working. Proceed to Step 2.

### Interactive Check-in

Verify each item before continuing:

- ✓ Vapi dashboard loaded with email verified
- ✓ Twilio connected as a provider with green "Connected" badge
- ✓ One phone number imported and showing "Active" status
- ✓ ElevenLabs connected with API key validated
- ✓ Successful test call completed — you heard the agent speak and it heard you respond

If any item is missing, stop and fix it before proceeding. Every subsequent step depends on this foundation.

## Step 2: Build the Core Voice Agent

You will now create a voice agent configured for a specific business use case: a dental practice called Bright Smile Dental. This agent will handle incoming calls, answer questions about services and insurance, schedule appointments, and transfer emergency calls to a human. The same architecture applies to any business with a high volume of routine phone inquiries.

### Create a New Assistant

In the left sidebar, click **Assistants**. Click **Create Assistant**. A configuration form will appear.

Enter the following:

- **Name:** Bright Smile Dental Reception
- **Model:** GPT-4o (select from dropdown)
- **Voice:** Rachel (ElevenLabs)
- **Phone Number:** Select the phone number you imported in Step 1

Click **Save**. The assistant should appear in the list with a green "Active" badge. If the assistant shows as "Draft," click it and hit **Publish** in the top-right corner. Vapi assistants must be published before they can receive calls.

### Design the Conversation Flow

Before writing any configuration, map the conversation flow on paper or in Notion. A dental practice reception agent has four primary paths:

1. **Information requests** — Caller asks about services, hours, insurance, location. Agent answers from knowledge base. Call ends.
2. **Appointment scheduling** — Caller wants to book. Agent collects name, phone, appointment type, preferred date/time. Confirms and triggers scheduling function. Call ends.
3. **Emergency** — Caller reports severe pain, bleeding, or broken tooth. Agent transfers immediately to on-call dentist.
4. **Human request** — Caller asks to speak with a person. Agent transfers to front desk.

Every caller falls into one of these four paths. The system prompt must handle all four without ambiguity.

### Configure the System Prompt

Click on the assistant name to open its full configuration. Scroll to the **System Prompt** field. This is the most critical configuration in the entire build — it defines how the agent behaves, what it knows, and what it can do. A weak system prompt produces a weak agent. Paste the following:

```
You are the AI receptionist for Bright Smile Dental, a dental practice located at 123 Maple Street, Springfield, IL 62701. Your name is Rachel.

YOUR ROLE:
Answer phone calls from patients and prospective patients. Help them with scheduling appointments, answering questions about services, providing insurance information, and giving office hours and directions.

KEY RULES:
1. Always be warm, professional, and concise. Phone callers want quick answers.
2. Never make up information. If you do not know something, say "Let me connect you to our office staff who can help with that."
3. When scheduling an appointment, collect: patient name, phone number, type of appointment, and preferred date/time.
4. If a caller has a dental emergency, immediately offer to transfer them to the on-call dentist.
5. Never discuss pricing in exact terms — say "Our team can provide a detailed quote after a consultation."
6. Keep responses under 30 words when possible. Phone conversations should be snappy, not lectures.
7. You ONLY answer questions related to dental services, appointments, and office information. For anything else, politely decline.
8. If a caller asks to speak with a human, transfer them immediately. Do not attempt to convince them to stay with you.

OFFICE HOURS:
Monday-Thursday: 8:00 AM - 6:00 PM
Friday: 8:00 AM - 4:00 PM
Saturday: 9:00 AM - 1:00 PM (by appointment only)
Sunday: Closed

SERVICES OFFERED:
General cleanings and exams, teeth whitening, fillings and crowns, root canals, orthodontic consultations, emergency dental care, pediatric dentistry.

INSURANCE:
We accept most major insurance plans including Delta Dental, Cigna, Blue Cross Blue Shield, Aetna, and MetLife. We also offer payment plans for uninsured patients.

CALL TRANSFER RULES:
- If a caller asks to speak with a human, say "I'll connect you to our office staff now" and call the transfer_call function.
- If a caller has a dental emergency (severe pain, bleeding, broken tooth), say "Let me get you to our on-call dentist right away" and call the transfer_emergency function.
- If you cannot answer a question after two attempts, proactively offer to transfer: "I want to make sure you get the right answer. Let me connect you with our team."

APPOINTMENT SCHEDULING:
1. When a caller wants to schedule, collect: their full name, a callback phone number, the type of appointment (cleaning, consultation, emergency, whitening, etc.), and their preferred date and time.
2. Repeat the details back to the caller for confirmation: "Let me confirm — you'd like a [type] appointment on [date] at [time], and I have your number as [phone]. Is that correct?"
3. After confirmation, call the schedule_appointment function with the collected details.
4. Tell the caller: "Your appointment has been scheduled. You'll receive a confirmation shortly. Is there anything else I can help with?"
5. If the preferred time is outside business hours, say "Our office is open [hours]. Could we find a time during those hours?"
```

Click **Save**.

### Add the Knowledge Base

Scroll down to the **Knowledge Base** section. Click **Add Documents**. Upload the following files — create them as `.txt` files on your computer first:

1. **services-detailed.txt** — A 300-500 word document listing every service with descriptions, typical duration, and general price ranges. Example: "Teeth Whitening — Professional in-office whitening using LED-accelerated gel. Duration: 90 minutes. General range: $300-$600 depending on treatment level."

2. **office-policies.txt** — Cancellation policy (24-hour notice required or $50 fee applies), late policy (arrivals more than 15 minutes late may need to reschedule), first-visit paperwork requirements (arrive 15 minutes early, bring insurance card and photo ID), payment methods accepted (cash, credit card, CareCredit financing available).

3. **faq.txt** — The 25 most common questions patients ask by phone, with concise answers written in a conversational tone. Include questions like: "Do you accept walk-ins?", "How do I get my x-rays transferred?", "Is parking free?", "What age do you start seeing children?", "Do you offer payment plans?"

After uploading, each file should show a green "Indexed" status. If you see "Processing," wait 30 seconds and refresh. If you see "Error — Unsupported format," confirm the files are `.txt` (not `.pdf` or `.docx`). Vapi's knowledge base indexing works best with plain text under 10,000 characters per file.

### Set Up Transfer Rules and Functions

In the assistant configuration, scroll to **Functions**. Click **Add Function**. Create three functions:

**Function 1 — transfer_call:**

```json
{
  "name": "transfer_call",
  "description": "Transfer the caller to a human staff member when the AI cannot help or when the caller explicitly requests to speak with someone",
  "type": "phone_call_transfer",
  "transfer_to": "+15559876543"
}
```

Replace `+15559876543` with the client's actual front desk number when deploying.

**Function 2 — transfer_emergency:**

```json
{
  "name": "transfer_emergency",
  "description": "Transfer the caller to the on-call dentist for dental emergencies",
  "type": "phone_call_transfer",
  "transfer_to": "+15551112222"
}
```

**Function 3 — schedule_appointment:**

```json
{
  "name": "schedule_appointment",
  "description": "Schedule an appointment for the caller. Collects patient name, phone number, appointment type, and preferred date/time before calling this function.",
  "type": "server_url",
  "method": "POST",
  "url": "",
  "parameters": {
    "patient_name": { "type": "string", "required": true },
    "patient_phone": { "type": "string", "required": true },
    "appointment_type": { "type": "string", "required": true },
    "preferred_date": { "type": "string", "required": true },
    "preferred_time": { "type": "string", "required": true }
  }
}
```

Leave the URL field blank for now — you will configure this in Step 3 when connecting Make.com.

### Configure Call Handling

Scroll to **Voicemail Detection**. Toggle it **On**. Set:

- **Detection mode:** Machine
- **Action on voicemail:** Hang Up
- **Voicemail message:** None (do not leave a message — this avoids compliance issues)

Scroll to **End of Call**. Set the silence timeout to 10 seconds. Enable the farewell message: "Thank you for calling Bright Smile Dental. Have a great day!"

Scroll to **Barge-in**. Toggle it **On**. This allows callers to interrupt the agent mid-sentence — critical for a natural phone conversation.

Click **Save** on the entire assistant configuration.

### Test with Real Phone Numbers

Call your agent number from a different phone than the one you used for the test call in Step 1. Test each of the four conversation paths:

1. **Information:** "What are your hours on Saturday?" — Agent should respond with the Saturday hours from the system prompt.
2. **Scheduling:** "I want to schedule a cleaning." — Agent should ask for your name, phone, and preferred time. Note: The scheduling function will fail at this point because the URL is not yet configured. This is expected.
3. **Emergency:** "I have a terrible toothache and my gum is bleeding." — Agent should offer to transfer you to the on-call dentist.
4. **Human request:** "I'd like to speak to someone at the front desk." — Agent should transfer immediately.

If all four paths behave as expected, the core agent is functional. Proceed to Step 3.

### Interactive Check-in

Verify each item before continuing:

- ✓ Assistant created and published with green "Active" badge
- ✓ System prompt configured with business-specific rules, office hours, services, and transfer logic
- ✓ Knowledge base documents uploaded and indexed (all showing green "Indexed")
- ✓ Three functions configured: `transfer_call`, `transfer_emergency`, `schedule_appointment`
- ✓ Voicemail detection enabled
- ✓ End-of-call handling with 10-second silence timeout and farewell message
- ✓ Barge-in enabled
- ✓ All four conversation paths tested with real phone calls

If the scheduling function fails (expected — URL not yet set), that is correct. If any other path fails, debug the system prompt before proceeding.

## Step 3: Connect to Make.com Automations

Your voice agent can talk, but it cannot take action. Appointment data goes nowhere. Nobody gets notified. Nothing is logged. This step connects the agent to the tools a real business uses daily — turning a conversational AI into a business automation engine.

### Set Up the Make.com Appointment Scenario

1. Go to make.com and sign in. Click **Create a new scenario**.
2. Add a **Webhook** module as the first step. Click **Add a webhook** → **Create a new webhook**. Name it `appointment-webhook`. Copy the webhook URL — this is the endpoint Vapi will call when the `schedule_appointment` function executes.
3. Add a **Google Calendar** module as the second step. Select **Create an Event**. Connect your Google account. Map the fields from the webhook payload:
   - **Summary:** `{{2.appointment_type}} — {{2.patient_name}}`
   - **Start time:** `parseDate({{2.preferred_date}} + " " + {{2.preferred_time}})`
   - **End time:** Start time + 60 minutes (adjust per appointment type — cleanings are 60 min, consultations 30 min, whitening 90 min)
   - **Description:** `Patient: {{2.patient_name}}, Phone: {{2.patient_phone}}, Type: {{2.appointment_type}}, Scheduled by AI voice agent`
4. Add a **Google Sheets** module as the third step. Select **Add a Row**. Create a spreadsheet called "AI Appointments Log" with columns: Timestamp, Patient Name, Phone, Appointment Type, Date, Time, Source. Map each webhook parameter to the corresponding column. Set Source to "AI Voice Agent."
5. Add a **Slack** module (or **Gmail** if your client prefers) as the fourth step. Connect your workspace. Configure the message:

```
:telephone_receiver: New Appointment Scheduled
Patient: {{2.patient_name}}
Phone: {{2.patient_phone}}
Type: {{2.appointment_type}}
When: {{2.preferred_date}} at {{2.preferred_time}}
Source: AI Voice Agent
```

6. Click **Save** and toggle the scenario **On**.

Now go back to Vapi. In the assistant configuration, find the `schedule_appointment` function you created in Step 2. Paste the Make.com webhook URL into the **URL** field. Click **Save**.

### Connect Calendly for Booking

Calendly integration prevents double-bookings. When the AI agent schedules an appointment, it should verify the time slot is available before confirming.

1. Go to calendly.com and log in. Create an event type called "Dental Appointment" with 30-minute and 60-minute options.
2. In Make.com, add a **Calendly** module between the Webhook and Google Calendar modules. Select **List Event Invitees** or **Get Event** to check availability.
3. Add a **Filter** module: if the time slot is already booked, route to a **Set Variable** module that sets `available = false`. Otherwise, set `available = true`.
4. Add a **Router** module. Path A: `available = true` → proceed to Google Calendar creation. Path B: `available = false` → send the caller a follow-up SMS via Twilio suggesting the next available time.

For your first deployment, you can skip the Calendly check and handle double-bookings manually through the Google Sheets log. Add Calendly after you have 2-3 clients and need automated availability management.

### Build the CRM Integration with Notion

Replace Google Sheets with Notion for a more professional client-facing CRM. In Make.com:

1. Add a **Notion — Create a Database Item** module after the webhook.
2. Connect your Notion workspace. Select the "AI Appointments Log" database you created in the Prerequisites.
3. Map the fields: Patient Name → Title, Phone → Phone, Appointment Type → Type, Date → Date, Time → Time, Source → "AI Voice Agent".

Notion is preferable to Google Sheets for client-facing reporting because you can build formatted dashboards with call metrics, charts, and action items — all shareable via a read-only link.

### Build the Call Logging Scenario

Create a second Make.com scenario called "Call Logger." This runs every time a call ends, regardless of whether an appointment was booked.

1. Add a **Webhook** module. Name it `call-end-webhook`. Copy the URL.
2. In Vapi, go to **Settings → Webhooks**. Add a new webhook for the "Call Ended" event. Paste the Make.com webhook URL.
3. In Make.com, add a **Notion — Create a Database Item** module after the webhook. Map the call data:
   - Call ID, Phone Number, Duration, Transfer (yes/no), Appointment Booked (yes/no), Call Transcript, Timestamp
4. Save and activate.

This gives you a complete log of every call your agent handles. Share this log with clients as proof of value — "Your agent handled 47 calls this week, booked 12 appointments, and transferred 8 to your staff."

### Add Notification Routing

For clients who use ActiveCampaign for email marketing or CRM, add an ActiveCampaign module to the Make.com scenario:

1. Add an **ActiveCampaign — Create or Update a Contact** module after the webhook.
2. Map `patient_phone` and `patient_name` to the contact fields.
3. Tag the contact with "AI Voice Agent Lead" and the appointment type.
4. Trigger an ActiveCampaign automation that sends a welcome email and appointment confirmation.

This integration is particularly valuable for clients who already use ActiveCampaign — it means every call the AI agent handles automatically feeds their existing marketing pipeline without manual data entry.

### Test the Full Pipeline

Call your agent number. Say: "I'd like to schedule a teeth whitening appointment for next Thursday at 10 AM. My name is Alex Johnson and my number is 555-999-0000."

The agent should collect the details, confirm them, and execute the `schedule_appointment` function. Within 10 seconds of the call ending, check:

1. **Google Calendar** — New event titled "Teeth Whitening — Alex Johnson" on next Thursday at 10 AM.
2. **Notion** — New database row with Alex Johnson's details.
3. **Slack** — Appointment notification in your channel.
4. **Call Log** — Row for the completed call with transcript.

### Interactive Check-in

Verify each item before continuing:

- ✓ Make.com scenario running with webhook → Google Calendar → Notion → Slack pipeline
- ✓ `schedule_appointment` function in Vapi pointing to the Make.com webhook URL
- ✓ Calendly connected (or noted as a future enhancement)
- ✓ Call logging scenario running and capturing every call's data in Notion
- ✓ ActiveCampaign integration configured (or noted as a future enhancement)
- ✓ Full pipeline tested: call → agent collects info → appointment created → logged in Notion → Slack notification received

If Google Calendar has the event but Slack does not, the Slack module is misconfigured — check the channel name and Slack connection. If nothing appears anywhere, the webhook is not receiving data — go to Make.com, right-click the webhook module, and select **View logs**. You should see an incoming request with the appointment data. If you see no requests, the Vapi function URL is wrong — go back to the assistant configuration and verify the webhook URL matches exactly.

## Step 4: Add Advanced Features

A voice agent that passes a basic test call is not production-ready. Businesses expect reliability, edge-case handling, and professional call quality. This step adds the features that separate a demo from a deployable product.

### Multi-Language Support

If your client serves a multilingual population, configure language detection and switching. In the Vapi assistant settings:

1. Set **Primary Language:** English
2. Set **Supported Languages:** Spanish, Mandarin (or whichever languages are relevant)
3. Add this section to the system prompt:

```
LANGUAGE HANDLING:
- If a caller speaks Spanish, respond in Spanish for the rest of the call.
- If a caller speaks Mandarin, respond in Mandarin for the rest of the call.
- If you are unsure which language the caller prefers, ask: "English or Spanish?"
- Always use the same language the caller initiated the conversation in.
- Never switch languages mid-call unless the caller explicitly requests it.
```

4. In ElevenLabs, select a multilingual voice model. "Rachel" supports English and Spanish. For Mandarin, add a second ElevenLabs voice and configure Vapi to switch voices based on detected language using the `voice_id` parameter in the assistant configuration.

The ElevenLabs multilingual models require the Starter plan ($5/mo) or above. Free tier voices are English-only.

### Sentiment Analysis Routing

Configure the agent to detect caller frustration or urgency and route accordingly. Add this to the system prompt:

```
SENTIMENT DETECTION:
- If a caller sounds frustrated (raised voice, short responses, repeated complaints), say "I understand this is frustrating. Let me get you to someone who can help right away" and call the transfer_call function.
- If a caller sounds urgent or panicked, treat it as an emergency and call the transfer_emergency function.
- If a caller is calm and conversational, continue handling the call normally.
- Never tell the caller you are analyzing their sentiment. Simply act on it.
```

This feature alone justifies the premium pricing tier. Businesses value an AI that knows when to get out of the way and hand the call to a human.

### After-Hours Handling

Configure different behavior based on time of day. Add this to the system prompt:

```
AFTER-HOURS BEHAVIOR (calls received outside business hours):
1. Say: "Thank you for calling Bright Smile Dental. Our office is currently closed. Our hours are Monday through Thursday 8 AM to 6 PM, and Friday 8 AM to 4 PM."
2. Ask: "Would you like to leave a message, schedule an appointment, or reach our emergency line?"
3. If they want to schedule, collect the details and use the schedule_appointment function. Tell them: "We'll confirm your appointment when the office opens."
4. If they want the emergency line, transfer using the transfer_emergency function.
5. If they want to leave a message, collect their name, phone number, and message. Send it to the office email via the Make.com webhook.
```

In Make.com, add an **Email** module to the Call Logger scenario that sends voicemail messages to the client's office email when the call metadata includes `after_hours = true`.

### Custom Voice Cloning with ElevenLabs

For clients who want the agent to sound like a specific person — the business owner, a known receptionist, or a brand voice — use ElevenLabs Voice Cloning.

1. Go to elevenlabs.io/app/voice-library and click **Add Voice** → **Voice Cloning**.
2. Upload 3-5 minutes of clean audio of the target voice. The audio must be recorded in a quiet environment with no background noise, no music, and only one speaker.
3. Select **Professional Voice Cloning** (requires Creator plan at $22/mo). The Instant Voice Cloning option produces lower quality and is not recommended for production agents.
4. Name the voice (e.g., "Dr. Martinez — Bright Smile Dental"). Wait for ElevenLabs to process the clone (typically 30-60 minutes).
5. In Vapi, update the assistant's voice setting. Change the voice provider to ElevenLabs and select the cloned voice from the dropdown.

Voice cloning is a premium upsell worth $500/month additional per client. Most businesses do not need it, but for practices with a well-known personality (a popular dentist, a radio-host owner), it dramatically increases caller trust.

### Appointment Scheduling Flow Enhancement

Enhance the basic scheduling flow with availability checking and confirmation SMS. In Make.com, update the appointment scenario:

1. After the webhook receives appointment data, add a **Calendly — List Available Times** module to check if the requested slot is open.
2. Add a **Router** with two paths:
   - **Path A (available):** Create Google Calendar event → Add Notion row → Send confirmation SMS via Twilio → Send Slack notification.
   - **Path B (unavailable):** Add a **Set Variable** module with `next_available = [next slot from Calendly]` → Send SMS: "Hi {{patient_name}}, the time you requested isn't available. The next open slot is {{next_available}}. Reply BOOK to confirm or call us at {{office_number}}."
3. Add a **Twilio — Send SMS** module in Path A with the confirmation message: "Hi {{patient_name}}, your {{appointment_type}} appointment at Bright Smile Dental is confirmed for {{preferred_date}} at {{preferred_time}}. Reply CANCEL to reschedule or call us at +15559876543."

Confirmation SMS reduces no-shows by 30-40%. This feature alone justifies the Growth pricing tier.

### Interactive Check-in

Verify each item before continuing:

- ✓ Multi-language support added to system prompt (if applicable to your target client)
- ✓ Sentiment analysis routing rules added to system prompt
- ✓ After-hours handling configured with distinct conversation flow
- ✓ Voice cloning explored in ElevenLabs (optional, for premium clients)
- ✓ Appointment scheduling flow enhanced with availability checking and confirmation SMS
- ✓ Each advanced feature tested individually with real phone calls

## Step 5: Deploy for Your First Client

Everything you have built so far uses placeholder data — "Bright Smile Dental" is a fictional client. This step covers the process of taking a real business from signed contract to live deployment.

### Client Onboarding Checklist

Before you configure anything, collect this information from the client. Send this checklist as a Notion page or Google Doc. Do not begin the build until every item is provided.

- Business name, address, and website URL
- Services or products offered (with descriptions for the knowledge base)
- Office hours (including seasonal variations)
- Insurance plans accepted (if applicable)
- Staff phone numbers for call transfers (front desk, emergency line, specific departments)
- Brand voice preferences (formal, friendly, clinical, casual)
- Preferred agent name and gender
- Common questions patients/customers ask by phone (ask for the top 20)
- Cancellation and late policies
- Payment methods accepted
- Existing phone system details (carrier, forwarding capabilities)
- CRM or scheduling software currently in use
- Email addresses for notifications
- Preferred notification channel (Slack, email, SMS, or all three)

Record a Loom video walking the client through this checklist. Include the Loom link in the Notion page. Clients fill it out faster when they see someone explaining each field.

### Configure for Their Business

Create a new Vapi assistant — do not reuse the demo agent. Each client gets a dedicated assistant with their own phone number, system prompt, and knowledge base.

1. Clone your demo assistant in Vapi. Click the three-dot menu next to the assistant name → **Duplicate**.
2. Rename the duplicate to `[Client Name] — AI Receptionist`.
3. Replace the system prompt. Keep the structure but swap every piece of business-specific information with the client's data from the onboarding checklist.
4. Upload new knowledge base documents specific to this client's services, policies, and FAQs.
5. Update all phone numbers in transfer functions.
6. Update the Make.com webhooks to point to the new assistant.
7. Provision a new Twilio phone number for this client (or port their existing number — see below).

**Porting an existing business number:** If the client wants to keep their current phone number, you can port it to Twilio. Go to twilio.com/console/phone-numbers/porting and start a port request. This takes 2-4 weeks and requires a Letter of Authorization signed by the business owner. During the porting process, forward the existing number to the new Twilio number using the current carrier's call forwarding feature. This gives the client uninterrupted service while the port completes.

### Test with Their Callers

Before going live, run a closed beta with the client's staff:

1. Have 3-5 staff members call the agent from different phones.
2. Give each caller a specific scenario to test (booking, emergency, hours inquiry, insurance question, human transfer).
3. Collect their feedback on: voice quality, response accuracy, conversation naturalness, and any errors.
4. Adjust the system prompt based on feedback. Common adjustments: slowing down speech rate, adding more specific answers to the knowledge base, changing the greeting, adjusting transfer thresholds.

Record each test call using Vapi's call recording feature (enabled under Settings → Recording). Share the recordings with the client in a Loom video where you walk through each call and explain the agent's behavior.

### Go Live

When the client approves the test calls:

1. Configure call forwarding on the client's existing phone system. Forward their main business number to the Vapi/Twilio number during the hours they want the AI to handle calls (after-hours, overflow, or 24/7).
2. Test the forwarding chain: call the client's main number → verify it rings through to Vapi → verify the agent answers → verify the conversation works end-to-end → verify the Make.com pipeline fires.
3. Enable call recording on the Vapi assistant for quality monitoring.
4. Set up a daily email digest via Make.com that sends the client a summary of the previous day's calls: total calls, appointments booked, transfers made, and any flagged issues.

### Monitoring Setup

During the first two weeks of a live deployment, monitor the agent daily:

1. Log in to the Vapi dashboard each morning. Check the Calls tab for the previous day's calls.
2. Listen to 3-5 call recordings. Flag any responses that are inaccurate, overly long, or off-brand.
3. Check the Notion call log for any calls where the agent failed to help (no appointment booked, no transfer made, caller hung up frustrated).
4. Update the system prompt and knowledge base as needed. Common fixes during the first two weeks: adding new FAQs the agent cannot answer, adjusting the greeting to match the client's preferred style, adding new transfer rules for edge cases.
5. After two weeks, reduce monitoring to twice weekly. After one month, shift to weekly.

### Pricing Tiers

Use this pricing structure. Voice agents command 2-3x the pricing of text chatbots because they replace a more expensive human task (answering phones) and require more technical complexity to deliver.

| Tier | Monthly Fee | Setup Fee | What's Included |
|------|------------|-----------|-----------------|
| **Starter** | $1,500/mo | $2,000 | 1 voice agent, 100 calls/mo, appointment scheduling, email notifications, monthly call log report |
| **Growth** | $3,500/mo | $4,000 | 1 agent, 500 calls/mo, call transfers, SMS confirmations, Calendly integration, Slack/Notion dashboard, weekly reporting |
| **Enterprise** | $8,000/mo | $8,000 | Multiple agents, unlimited calls, outbound reminders, multi-language, custom voice cloning, ActiveCampaign/CRM integration, custom workflows, dedicated Slack channel, priority support |

The setup fee covers 10-15 hours of configuration, testing, and deployment. The monthly fee covers platform costs (Vapi, OpenAI, ElevenLabs, Twilio, Make.com), ongoing maintenance (updating the knowledge base, monitoring call quality, adjusting the system prompt), and support.

The monthly fee is not optional. Voice agents degrade without maintenance. New services get added. Insurance plans change. Office hours shift seasonally. Without someone updating the knowledge base and system prompt, the agent starts giving wrong answers within 60 days. The monthly fee protects the client's investment and guarantees your recurring revenue.

### Sales Method: The Live Demo Call

Do not send proposals. Do not send cold emails with PDF attachments. The only sales method that works for voice agents is the live demo call, because the product is a phone experience — they have to hear it to believe it.

1. Pick a business category. For your first client, use dental practices — they have high call volume, repetitive questions, and clear ROI (every booked appointment equals revenue).
2. Build the demo agent following Steps 1-4 of this guide with generic dental practice information.
3. Find 20 dental practices on Google Maps in a mid-size city (avoid major metros where competition is high).
4. Call each practice. When the receptionist answers, say: "Hi, I'm looking for a dentist and had a few questions — do you accept Delta Dental? What are your hours? Can I book a cleaning next week?" Listen to how long it takes them to answer. Most front desk staff spend 3-5 minutes on routine calls like this.
5. Then call the business owner or office manager directly. Say: "I noticed your front desk handles a lot of routine calls — insurance questions, scheduling, hours. I built an AI receptionist that answers those calls automatically, 24/7. It sounds like this." Then dial your demo agent on speakerphone. Have the owner listen to a 2-minute live conversation where the agent answers questions, schedules an appointment, and the Slack notification arrives.

This converts at 20-30% because the owner hears the agent working in real time — no imagination required. The Slack notification arriving during the demo proves the integration works. The ROI is immediately calculable: if a receptionist costs $35,000/yr and the agent handles 60% of calls, the business saves $21,000/yr against an $18,000/yr Starter-tier agent cost — still a clear win.

Close the deal on the call. Send a Stripe payment link for the setup fee. Schedule the discovery call for the following week.

### Interactive Check-in

Verify each item before continuing:

- ✓ Client onboarding checklist completed and stored in Notion
- ✓ Dedicated Vapi assistant created for the client with their specific data
- ✓ Knowledge base documents uploaded and tested
- ✓ Staff test calls completed with feedback incorporated
- ✓ Call forwarding configured and tested end-to-end
- ✓ Monitoring routine established (daily for first 2 weeks)
- ✓ Pricing tiers defined and documented
- ✓ Live demo agent ready for sales calls
- ✓ Stripe payment link created for setup fee collection

## Step 6: Scale to Multiple Clients

Once you have delivered 3-5 voice agents and have a repeatable process, scaling requires removing yourself from three bottlenecks: building, selling, and maintaining.

### Template the Deployment

Create a deployment template that reduces each new client build from 10-15 hours to 3-4 hours:

1. **Vapi Assistant Template:** In Notion, create a page called "Voice Agent Build Template." Include the system prompt template with placeholder variables (`{{BUSINESS_NAME}}`, `{{ADDRESS}}`, `{{HOURS}}`, `{{SERVICES}}`, etc.), the standard function definitions (transfer_call, transfer_emergency, schedule_appointment), and the default voice settings.
2. **Make.com Scenario Template:** Export your Make.com scenario as a blueprint (Settings → Export Blueprint). Import it for each new client and update the webhook URLs and credentials.
3. **Knowledge Base Template:** Create a standard set of .txt file templates: services-template.txt, policies-template.txt, faq-template.txt. Send these to the client during onboarding with instructions to fill in their information.
4. **Notion Client Dashboard Template:** Duplicate the Notion dashboard you built in Step 4 for each new client. Update the data source links.

With these templates, a trained builder can produce a new voice agent in 3-4 hours instead of 10-15.

### Hire a Virtual Assistant (VA)

You need a VA to handle the repetitive parts of the build process:

1. **Where to hire:** Upwork, OnlineJobs.ph, or a local university CS program. Look for candidates with API integration experience and basic coding literacy.
2. **What they do:** Follow the build template to create Vapi assistants, upload knowledge base documents, configure Make.com scenarios, and run the 5-test checklist.
3. **What they do not do:** Write system prompts (this requires domain knowledge and prompt engineering skill), talk to clients, or make pricing decisions.
4. **How to pay:** Pay per build, not hourly. $150-200 per completed and tested assistant. This keeps costs predictable and incentivizes speed.
5. **How to train:** Record a Loom video walking through the entire build process using the template. Have the VA watch it, then build a test agent under your supervision. Review their work. Approve when quality is consistent.

At $200 per build and a Starter tier setup fee of $2,000, your cost per client acquisition (build cost only) is 10% of setup revenue. This is an excellent margin.

### Build SOPs in Notion

Create a Standard Operating Procedures workspace in Notion with the following pages:

1. **New Client Onboarding SOP** — Step-by-step from signed contract to live deployment. Include the onboarding checklist, the Loom walkthrough link, and the expected timeline (7-10 business days from contract to go-live).
2. **Voice Agent Build SOP** — The complete build process following the template. Include screenshots of every Vapi configuration screen, Make.com module setup, and Twilio phone number provisioning.
3. **Quality Assurance SOP** — The 5-test checklist for every new agent. Include the exact phrases to say during each test call and the expected responses.
4. **Monthly Maintenance SOP** — The weekly/monthly tasks for each client: review call logs, update knowledge base, adjust system prompt, send client report.
5. **Incident Response SOP** — What to do when the agent goes down, gives wrong answers, or a client reports an issue. Include escalation thresholds (e.g., "If the agent is unreachable for more than 15 minutes, call the client immediately").

Share this Notion workspace with your VA and any future team members. SOPs are the difference between a freelance gig and a scalable business.

### Automate Reporting

Clients expect regular reports. Build the reporting into the Make.com automation rather than doing it manually:

1. Create a Make.com scenario called "Weekly Client Report."
2. Set the trigger to **Schedule** → every Monday at 8:00 AM in the client's timezone.
3. Add a **Notion — Search Database Items** module to pull the previous week's call data.
4. Add an **Aggregate** module to calculate: total calls, appointments booked, transfers made, average call duration, top 5 questions asked.
5. Add an **Email** module that sends a formatted report to the client with the weekly metrics.
6. For Enterprise clients, add a **Google Sheets — Add a Row** module that appends the weekly data to a historical tracking spreadsheet.

This eliminates 1-2 hours of manual reporting per client per week. At 10 clients, that is 10-20 hours saved weekly.

### Margin Improvements

As you scale, optimize margins in three areas:

1. **Bulk API pricing:** At 20+ clients, negotiate volume discounts with Vapi and OpenAI. Vapi offers custom pricing at scale. OpenAI provides volume tier pricing at $100+/mo in API spend.
2. **Retainer efficiency:** Each client's monthly maintenance takes 1-2 hours. A VA at $25/hr costs $25-50/month per client. Your monthly revenue is $1,500-8,000/month per client. After platform costs (~$60-250/client/mo), the margin is 85%+.
3. **White-label partnerships:** At 15+ clients, approach other agencies (marketing agencies, IT consultants, web designers) who serve small businesses. Offer them a white-label version: they sell the voice agent under their brand, you build and maintain it, and you split revenue 50/50. The math: a Growth-tier client at $4,000 setup + $3,500/mo. You get $2,000 setup + $1,750/mo. The agency gets the same. You do the technical work; they do the client relationship. This scales faster because agencies already have the clients — you just add the voice agent to their service menu.

**Margin at scale (20 Growth-tier clients):**

| Item | Amount |
|------|--------|
| Setup revenue (one-time) | $80,000 |
| Monthly revenue | $70,000/mo |
| Vapi costs | ~$600-1,600/mo |
| OpenAI API costs | ~$400-1,200/mo |
| ElevenLabs costs | ~$100-500/mo |
| Twilio costs | ~$100-300/mo |
| Make.com costs | ~$50-150/mo |
| VA build costs (one-time) | ~$4,000 |
| VA maintenance costs (monthly) | ~$1,000-2,000/mo |
| **Monthly net profit** | ~$64,150-67,750/mo |

## Cost Breakdown

| Item | Free Tier | Paid Tier | When to Upgrade |
|------|-----------|-----------|-----------------|
| Vapi | 100 min/mo, 1 assistant | $30/mo (Pro) — 2,000 min, 5 assistants | At 2+ clients — need multiple assistants and more call minutes |
| ElevenLabs | 10,000 chars/mo | $5/mo (Starter) — 30,000 chars | Immediately — 10K chars is ~8 minutes of speech, not enough for production |
| Make.com | 1,000 operations/mo | $9/mo (Core) — 10,000 operations | At 3+ clients — appointment webhooks and call logging consume operations quickly |
| Calendly | 1 event type | $10/mo (Standard) | When you need multiple appointment types or availability checking |
| Replit | Basic compute | $25/mo (Replit Core) | Only if you build a custom webhook handler or middleware |
| Notion | Free | $10/mo (Plus) | At 5+ clients for team collaboration and client portals |
| OpenAI API | Pay per use | ~$20-60/mo per client | Scales with call volume; monitor at platform.openai.com/usage |
| Twilio | $20 trial credit | $1.15/mo per number + $0.0085/min | After trial credit is used |

**Total monthly cost at 5 clients:** ~$200-350/mo
**Total monthly revenue at 5 clients:** $7,500-40,000/mo + setup fees

## Production Checklist

Before deploying any voice agent to a client's phone line, verify every item:

- [ ] System prompt is client-specific — business name, address, services, policies, and transfer numbers contain no placeholder text from the template
- [ ] Knowledge base documents are uploaded, indexed, and tested — ask the agent 10 questions from the FAQ and verify accuracy of each answer
- [ ] Call transfer functions are configured with correct destination numbers — tested with a real transfer call to each number
- [ ] Voicemail detection is enabled for outbound calls with "Hang Up" action
- [ ] Appointment scheduling pipeline works end-to-end — call → Vapi → Make.com → Google Calendar → Notion → Slack → SMS confirmation
- [ ] Barge-in is enabled — callers can interrupt the agent mid-sentence without waiting for it to finish
- [ ] End-of-call detection is configured with 10-second silence timeout and client-approved farewell message
- [ ] Greeting latency is under 1.5 seconds — measured with a stopwatch on a real phone call
- [ ] Background noise does not trigger false responses — tested from a noisy environment (car, coffee shop)
- [ ] Off-topic questions are rejected and redirected — tested with at least 3 unrelated questions (politics, sports, personal questions)

## What to Do Next

Once you have delivered your first 3-5 voice agents in one business category, expand with these specific moves:

- **Build a second industry agent** — HVAC and plumbing have the highest call urgency and the worst after-hours coverage. An AI agent that answers "My furnace stopped working" at 2 AM and dispatches a technician is worth $8,000+ in setup to the right client. The system prompt and knowledge base are the only things that change — the Vapi configuration, Make.com scenarios, and call logging are 80% identical across industries.
- **Add outbound appointment reminder campaigns** — Configure the agent to make reminder calls 24 hours before scheduled appointments using Vapi's outbound calling feature. This is a $300-500/mo upsell that pays for itself in reduced no-shows. Record a Loom video demonstrating the outbound reminder flow and include it in your Growth tier proposals.
- **Integrate with ActiveCampaign for lead nurturing** — Every call your agent handles generates a lead. Feed those leads into ActiveCampaign automations that send follow-up emails, appointment reminders, and re-engagement sequences. This makes the voice agent a full-funnel lead generation tool, not just a receptionist.
- **Create a client self-service portal in Notion** — Build a Notion dashboard where clients can see call volume, appointment bookings, transfer rates, and common caller questions without logging into Vapi. This makes the retainer feel tangible and reduces churn.
- **Explore white-label partnerships** — Approach 5 local marketing agencies. Offer to provide voice agent services under their brand. Each partnership can generate 3-5 clients with zero sales effort on your part. Use ChatGPT to draft the partnership outreach emails — they should be concise, focus on the agency's margin opportunity, and include a Loom demo link.

Ready to understand the full business opportunity? Read our [opportunity deep-dive](/opportunities/ai-voice-agent-agency-2026/).
