---
title: "Build and Deploy an AI Voice Agent System with Vapi"
date: 2026-04-24
category: "Implementation"
difficulty: "ADVANCED"
readTime: "28 MIN"
excerpt: "The complete execution guide for building, configuring, and deploying AI voice agents that handle phone calls for businesses. From Vapi setup to first paying client."
---

Voice agents are not chatbots with a microphone. They are real-time, full-duplex conversational systems that listen, think, and speak on a phone line — and businesses will pay significantly more for them because they replace a human sitting at a desk answering calls. This guide covers every step: provisioning phone numbers, configuring the voice model, building call-handling logic, connecting business tools, testing for production quality, pricing the service, and scaling past yourself. Follow it in order. Do not skip steps.

## Prerequisites

Before you start, you need the following:

- A laptop with a modern browser (Chrome or Firefox)
- A Vapi account — go to vapi.ai and sign up for the free tier
- An OpenAI API key with at least $20 credit — go to platform.openai.com/api-keys
- An ElevenLabs account for voice synthesis — go to elevenlabs.io and sign up (free tier includes 10,000 characters/mo)
- A Twilio account for phone number provisioning — go to twilio.com/referral (free trial includes $20 credit and one phone number)
- A Google Cloud account with Calendar API enabled — go to console.cloud.google.com
- A Slack workspace where you can create a webhook (any free Slack workspace works)
- A Stripe account for collecting payments — go to stripe.com
- 6-8 hours of uninterrupted time for your first build

Total upfront cost: $20 for the OpenAI API key. Everything else is free until you have paying clients. The Vapi free tier includes 100 minutes of outbound calls per month — enough to build, test, and run your first demo.

## Step 1: Set Up Your Vapi Account and Configure Voice

Open your browser and go to dashboard.vapi.ai. Sign in with the account you created. You should see the Vapi dashboard — a left sidebar with navigation items and a main area showing "Assistants" as the default view.

Do you see the Assistants view with an empty list and a "Create Assistant" button? You should see this if you are in the right place. Go back and verify your email if you see a blank screen or an error. Vapi requires email verification before the dashboard loads.

### Connect Your Twilio Account

In the left sidebar, click **Phone Numbers**. You will see an empty list and a button labeled **Import Number**. Before importing, you need to connect Twilio.

Click **Connect Provider** in the top-right corner. A modal will appear with provider options. Select **Twilio**. Enter your Twilio Account SID and Auth Token — both are found at twilio.com/console under "Account Info." Click **Connect**.

You should see a green "Connected" badge next to Twilio in the provider list. Do you see it? If you see a red error reading "Authentication failed," your Account SID or Auth Token is wrong. Go back to the Twilio console, copy both values exactly, and try again. If you see "Account not verified," Twilio requires you to verify your phone number on their platform before making API calls. Go to twilio.com/console/phone-numbers/verified, add your number, and complete the SMS verification.

### Provision a Phone Number

In the Twilio console (twilio.com/console/phone-numbers/search), search for a local phone number in your area code. Buy one — this costs $1.15/mo on Twilio. After purchasing, go back to the Vapi dashboard, click **Import Number**, and enter the Twilio phone number you just purchased (include the country code, e.g., +15551234567). Select Twilio as the provider. Click **Import**.

The number should appear in your Vapi Phone Numbers list with a green "Active" status. Do you see "Active"? If you see "Pending," wait 60 seconds and refresh. If you see "Failed," the number is not properly configured in Twilio. Go to the Twilio console, click the phone number, and verify that the "Voice Configuration" webhook URL is set to the Vapi webhook (Vapi provides this URL during import — copy it from the import modal and paste it into the Twilio voice webhook field).

### Configure the Voice Model

In the left sidebar, click **Voice**. You will see the voice configuration panel. This is where you select the AI model and the voice used for speech synthesis.

Set the following:

- **Model:** GPT-4o (select from the dropdown)
- **Voice Provider:** ElevenLabs
- **Voice:** Select "Rachel" (a professional, warm female voice that works well for business reception)
- **Language:** English

Click **Connect ElevenLabs** next to the voice provider dropdown. A modal will ask for your ElevenLabs API key. Go to elevenlabs.io/app/settings/api-keys, generate a key, and paste it here. Click **Save**.

You should see "Connected" next to the ElevenLabs integration. Do you see it? If you see "Invalid API key," go back to ElevenLabs and regenerate the key. If you see "Quota exceeded," you have used your free tier — upgrade to the $5/mo Starter plan on ElevenLabs.

### Test the Voice with a Sample Call

Click the **Test Call** button in the top-right corner of the dashboard. A modal will appear with your imported phone number. Enter your personal phone number as the destination. Click **Start Test Call**.

Your phone should ring within 5 seconds. Answer it. You should hear: "Hello, I'm your AI assistant. How can I help you today?" spoken in the Rachel voice. Do you hear the greeting? If you hear silence, the ElevenLabs integration is broken — go back to Voice settings and re-enter the API key. If the call never arrives, the Twilio webhook is misconfigured — go back to the Phone Numbers section and verify the webhook URL.

If you hear the greeting, say something. "What time are you open?" The AI will respond, but the answer will be generic because you have not configured a system prompt or knowledge base yet. That is expected. The point of this test is to confirm the audio pipeline works end-to-end: Twilio connects the call → Vapi processes the audio → GPT-4o generates a response → ElevenLabs synthesizes speech → audio plays back to the caller.

If you can hear the AI speak and it can hear you, proceed to Step 2. If audio is one-directional (you can hear it but it cannot hear you, or vice versa), this is a Twilio voice configuration issue. Go to the Twilio console, open the phone number settings, and ensure both the "Voice Configuration" and "Status Callback" URLs point to Vapi.

## Step 2: Build Your First Voice Agent

Now you will create a voice agent configured for a specific business: a dental practice called Bright Smile Dental.

### Create a New Assistant

In the left sidebar, click **Assistants**. Click **Create Assistant**. A configuration form will appear.

Enter the following:

- **Name:** Bright Smile Dental Reception
- **Model:** GPT-4o (select from dropdown)
- **Voice:** Rachel (ElevenLabs)
- **Phone Number:** Select the phone number you imported in Step 1

Click **Save**. You should see the assistant appear in the list with a green "Active" badge. Do you see it? If the assistant shows as "Draft," click it and hit **Publish** in the top-right corner. Vapi assistants must be published before they can receive calls.

### Configure the System Prompt

Click on the assistant name to open its configuration. Scroll to the **System Prompt** field. This is the most critical configuration — it defines how the agent behaves, what it knows, and what it can do. Paste the following prompt:

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

OFFICE HOURS:
Monday-Thursday: 8:00 AM - 6:00 PM
Friday: 8:00 AM - 4:00 PM
Saturday: 9:00 AM - 1:00 PM (by appointment only)
Sunday: Closed

SERVICES OFFERED:
General cleanings and exams, teeth whitening, fillings and crowns, root canals, orthodontic consultations, emergency dental care, pediatric dentistry.

INSURANCE:
We accept most major insurance plans including Delta Dental, Cigna, Blue Cross Blue Shield, Aetna, and MetLife. We also offer payment plans for uninsured patients.
```

Click **Save**. The system prompt is now active. Any call that comes in on the assigned phone number will use this prompt.

### Set Up the Knowledge Base

Scroll down to the **Knowledge Base** section. Click **Add Documents**. Upload the following files (create them as `.txt` files on your computer first):

1. **services-detailed.txt** — A 300-500 word document listing every service with descriptions, typical duration, and general price ranges
2. **office-policies.txt** — Cancellation policy (24-hour notice required), late policy, first-visit paperwork requirements, payment methods accepted
3. **faq.txt** — The 25 most common questions patients ask by phone, with concise answers written in a conversational tone

After uploading, each file should show a green "Indexed" status. Do you see "Indexed" next to each file? If you see "Processing," wait 30 seconds and refresh. If you see "Error — Unsupported format," make sure the files are `.txt`, not `.pdf` or `.docx`. Vapi's knowledge base indexing works best with plain text under 10,000 characters per file.

### Test the Agent with a Live Call

Click **Test Call** in the assistant configuration. Enter your personal phone number. Click **Start Test Call**.

When you answer, you should hear Rachel greet you with something like: "Thank you for calling Bright Smile Dental, this is Rachel. How can I help you today?"

Do you hear a greeting that references Bright Smile Dental? You should — the system prompt is working. If you hear the generic "I'm your AI assistant" greeting from Step 1, the system prompt did not save. Go back to the assistant configuration, verify the prompt is there, click **Save**, and test again.

Now test these specific phrases:

- "I want to schedule a cleaning." → The agent should ask for your name, phone number, and preferred time.
- "Do you accept Blue Cross?" → The agent should confirm they accept BCBS based on the system prompt.
- "I have a terrible toothache and it's Saturday." → The agent should offer to transfer to the on-call dentist (emergency protocol).
- "How much does a root canal cost?" → The agent should decline to give exact pricing and offer a consultation instead.

If all four scenarios produce the expected responses, your agent is configured correctly. If the agent hallucinates information or ignores the rules, your system prompt needs tightening. Add more explicit instructions: "NEVER state exact prices" instead of "Never discuss pricing in exact terms." Voice agents interpret instructions more loosely than text-based chatbots because of the real-time nature of the conversation. Be aggressive with constraints.

## Step 3: Configure Call Handling and Transfers

A voice agent that cannot escalate calls to a human is a liability. Businesses will not deploy an agent that traps callers in an AI loop. This step configures the three essential call-handling features: transfers, voicemail detection, and appointment scheduling.

### Set Up Call Transfer Rules

In the assistant configuration, scroll to **Functions**. Click **Add Function**. A function definition form will appear. Enter the following:

- **Name:** transfer_call
- **Description:** Transfer the caller to a human staff member when the AI cannot help or when the caller explicitly requests to speak with someone
- **Type:** Phone Call Transfer

Configure the transfer destination. Enter the dental practice's real front desk number: +15559876543 (replace with the client's actual number when deploying).

Click **Add**.

Now add a second function for emergencies:

- **Name:** transfer_emergency
- **Description:** Transfer the caller to the on-call dentist for dental emergencies
- **Type:** Phone Call Transfer
- **Transfer to:** +15551112222 (the emergency line)

Click **Add**.

Update the system prompt to reference these functions. Add this block at the end:

```
CALL TRANSFER RULES:
- If a caller asks to speak with a human, say "I'll connect you to our office staff now" and call the transfer_call function.
- If a caller has a dental emergency (severe pain, bleeding, broken tooth), say "Let me get you to our on-call dentist right away" and call the transfer_emergency function.
- If you cannot answer a question after two attempts, proactively offer to transfer: "I want to make sure you get the right answer. Let me connect you with our team."
```

Click **Save**.

### Configure Voicemail Detection

When the voice agent calls a patient (outbound calls for appointment reminders, follow-ups), it needs to detect whether a human or voicemail system answered. Leaving an AI message on a voicemail sounds unprofessional and can create legal issues.

In the assistant configuration, scroll to **Voicemail Detection**. Toggle it **On**. Set the following:

- **Detection mode:** Machine
- **Action on voicemail:** Hang Up
- **Voicemail message:** None (do not leave a message — this avoids compliance issues)

Click **Save**.

If you see "Voicemail Detection: Enabled" in the assistant summary, you are set. If the toggle does not stay on, your Vapi plan may not include voicemail detection — check your plan at vapi.ai/pricing and upgrade to the Pro plan ($30/mo) if needed.

### Add Appointment Scheduling Logic

In **Functions**, click **Add Function**. This time, create a function that captures appointment details:

- **Name:** schedule_appointment
- **Description:** Schedule an appointment for the caller. Collects patient name, phone number, appointment type, and preferred date/time before calling this function.
- **Type:** Server URL
- **Method:** POST
- **URL:** Leave blank for now — you will configure this in Step 4 when connecting Google Calendar
- **Parameters:**
  - `patient_name` (string, required)
  - `patient_phone` (string, required)
  - `appointment_type` (string, required)
  - `preferred_date` (string, required)
  - `preferred_time` (string, required)

Click **Add**.

Update the system prompt to include scheduling instructions:

```
APPOINTMENT SCHEDULING:
1. When a caller wants to schedule, collect: their full name, a callback phone number, the type of appointment (cleaning, consultation, emergency, whitening, etc.), and their preferred date and time.
2. Repeat the details back to the caller for confirmation: "Let me confirm — you'd like a [type] appointment on [date] at [time], and I have your number as [phone]. Is that correct?"
3. After confirmation, call the schedule_appointment function with the collected details.
4. Tell the caller: "Your appointment has been scheduled. You'll receive a confirmation shortly. Is there anything else I can help with?"
5. If the preferred time is outside business hours, say "Our office is open [hours]. Could we find a time during those hours?"
```

Click **Save**.

### Test with Real Scenarios

Call your test number. Run through these four scenarios:

1. "I need to make an appointment for a cleaning next Tuesday at 2 PM." → Agent should collect your name and phone, confirm details, and attempt to call the schedule_appointment function (it will fail because the URL is blank — that is expected at this stage).
2. "I'd like to speak to a real person." → Agent should say "I'll connect you now" and execute the transfer_call function.
3. "My tooth just cracked and I'm in a lot of pain." → Agent should trigger the emergency transfer.
4. Stay silent for 10 seconds after the greeting. → Agent should say "Are you still there?" or similar — this confirms the silence detection is working.

If scenarios 2 and 3 produce transfers, the function configuration is correct. If the agent says "I can help you with that" instead of transferring, the system prompt is not strong enough. Add: "ALWAYS transfer when requested. Do not attempt to answer questions that a human has been requested for."

## Step 4: Connect to Business Tools

The voice agent is functional but isolated — appointment data goes nowhere, nobody gets notified, and nothing is logged. This step connects the agent to the tools a real business uses daily.

### Integrate with Google Calendar for Scheduling

You need a server endpoint that receives the `schedule_appointment` function call and creates a Google Calendar event. The simplest way is a Make.com scenario (or n8n if you prefer self-hosted).

**Set up Make.com:**

1. Go to make.com and sign in. Click **Create a new scenario**.
2. Add a **Webhook** module as the first step. Click **Add a webhook** → **Create a new webhook**. Copy the webhook URL. This is your endpoint.
3. Add a **Google Calendar** module as the second step. Select **Create an Event**. Connect your Google account. Map the fields:
   - **Summary:** `[appointment_type] — [patient_name]`
   - **Start time:** `parseDate(preferred_date + " " + preferred_time)`
   - **End time:** Start time + 60 minutes (adjust per appointment type)
   - **Description:** `Patient: [patient_name], Phone: [patient_phone], Type: [appointment_type], Scheduled by AI voice agent`
4. Click **Save** and toggle the scenario **On**.

Now go back to Vapi. In the assistant configuration, find the `schedule_appointment` function you created in Step 3. Paste the Make.com webhook URL into the **URL** field. Click **Save**.

### Connect to Slack for Notifications

In Make.com, add a third module to the scenario: **Slack — Create a Message**. Connect your Slack workspace. Configure the message:

```
:telephone_receiver: New Appointment Scheduled
Patient: {{patient_name}}
Phone: {{patient_phone}}
Type: {{appointment_type}}
When: {{preferred_date}} at {{preferred_time}}
Source: AI Voice Agent
```

Select the channel (e.g., `#appointments`). Click **OK**.

Now every time the voice agent schedules an appointment, the front desk staff sees a Slack notification instantly.

### Set Up CRM Logging

For CRM logging, you have two options depending on the client's tooling:

**Option A — Google Sheets (universal, works for every client):** Add a **Google Sheets** module in Make.com. Select **Add a Row**. Map each parameter to a column: Patient Name, Phone, Appointment Type, Date, Time, Source ("AI Voice Agent"). This gives the client a searchable spreadsheet of all AI-booked appointments.

**Option B — HubSpot/ Salesforce (if the client uses a CRM):** Add the appropriate CRM module in Make.com and map the fields to create a Contact + Deal/Opportunity. This is more complex but commands a higher price.

For your first deployment, use Option A. It works universally and you can upsell CRM integration later.

### Interactive Check-in: Test the Full Pipeline

Call your test number. Say: "I'd like to schedule a teeth whitening appointment for next Thursday at 10 AM. My name is Alex Johnson and my number is 555-999-0000."

The agent should collect the details, confirm them, and execute the `schedule_appointment` function. Within 10 seconds of the call ending, check:

1. **Google Calendar** — Do you see a new event titled "Teeth Whitening — Alex Johnson" on next Thursday at 10 AM?
2. **Slack** — Do you see the appointment notification in the `#appointments` channel?
3. **Google Sheets** — Do you see a new row with Alex Johnson's details?

Do you see all three? If Google Calendar has the event but Slack does not, the Slack module in Make.com is misconfigured — check the channel name and Slack connection. If nothing appears anywhere, the webhook is not receiving data — go to Make.com, right-click the webhook module, and select "View logs." You should see an incoming request with the appointment data. If you see no requests, the Vapi function URL is wrong — go back to the assistant configuration and verify the webhook URL matches exactly.

If you see the event in Google Calendar, the pipeline is working. Move to Step 5.

## Step 5: Test and Debug Locally

Before deploying to a client, your voice agent must pass the 5-test checklist. Voice agents have unique failure modes that text chatbots do not — audio latency, speech overlap, misheard words, and dead air. Each of these destroys the caller experience.

### The 5-Test Checklist for Voice Agents

**Test 1: Greeting latency.** Call the agent. Start a stopwatch when the call connects. The agent's first word should come within 1.5 seconds. If it takes longer than 2 seconds, callers will say "Hello?" and talk over the agent. To fix latency: switch from GPT-4o to GPT-4o-mini for the first turn only (Vapi supports different models for different stages), or enable Vapi's "Fast First Response" setting which pre-generates a greeting.

**Test 2: Interruption handling.** Call the agent. Wait for it to start speaking, then interrupt mid-sentence by saying "Actually, wait—" The agent should stop speaking immediately and acknowledge your interruption. If it continues talking over you, turn on **Barge-in** in the assistant's Voice settings. This is critical — callers interrupt frequently on phone calls, and an agent that cannot be interrupted feels robotic and frustrating.

**Test 3: Background noise rejection.** Call the agent from a noisy environment — play music or TV in the background. The agent should not respond to the background noise. If it does, increase the **Speech Detection Threshold** in Voice settings (try 0.5 → 0.7). If the agent ignores your actual speech, the threshold is too high — lower it slightly.

**Test 4: End-of-call handling.** Say "That's all, thanks, goodbye." The agent should say goodbye and end the call within 5 seconds. If the agent keeps talking or waits indefinitely, add end-of-call detection: in the assistant configuration, scroll to **End of Call** and set the silence timeout to 10 seconds. Enable the farewell message: "Thank you for calling Bright Smile Dental. Have a great day!"

**Test 5: Off-topic rejection.** Ask: "Can you help me with my taxes?" The agent should decline and redirect to its scope: "I'm here to help with dental-related questions. For tax help, I'd recommend contacting a tax professional." If the agent attempts to answer, the system prompt constraints are too weak. Add: "You ONLY answer questions related to dental services, appointments, and office information. For anything else, politely decline."

Run all five tests. Log the results. If all five pass, proceed to Step 6. If any fail, fix the specific issue and re-test.

### Common Audio Issues and Fixes

| Symptom | Cause | Fix |
|---------|-------|-----|
| Echo during call | Twilio echo cancellation not enabled | Go to Twilio console → Phone Number → Voice settings → Enable "Echo Cancellation" |
| Agent speaks too fast | ElevenLabs speed setting too high | In Voice settings, set stability to 0.7 and similarity boost to 0.8 |
| Agent cuts off mid-word | Vapi speech detection too aggressive | Increase "End of Speech Timeout" from 0.3s to 0.8s in Voice settings |
| Caller's words are misheard | Background noise or accent | Switch voice model to GPT-4o (better audio understanding than GPT-4o-mini) |
| Long pauses between turns | Model latency | Enable "Streaming" in assistant settings; switch to GPT-4o-mini for responses |

### Latency Troubleshooting

Total voice agent latency is the sum of: Speech-to-Text (STT) + LLM inference + Text-to-Speech (TTS) + Network round-trip. Each component adds 200-800ms. Target total: under 2 seconds for a conversational feel.

To measure: call the agent, ask a question, and time from when you finish speaking to when the agent starts responding. If this exceeds 2.5 seconds, apply these optimizations in order of impact:

1. Enable **streaming** in Vapi (the agent starts speaking before the full LLM response is generated)
2. Switch STT provider to Deepgram (faster than OpenAI Whisper for real-time)
3. Use GPT-4o-mini for routine responses (2x faster than GPT-4o)
4. Pre-generate common responses using Vapi's "Canned Responses" feature
5. Reduce system prompt length — every token adds inference time

### Monitoring Call Quality

After deployment, you need ongoing visibility into call quality. In the Vapi dashboard, click **Analytics**. You will see:

- **Total calls** per day/week/month
- **Average call duration**
- **Transfer rate** (what percentage of calls are escalated to humans)
- **Average latency** per call

Monitor the transfer rate closely. If it exceeds 40%, the agent is not handling enough calls on its own — either the system prompt needs improvement or the business has too many edge cases for AI alone. A healthy transfer rate for a dental practice agent is 15-25%.

## Step 6: Price and Sell Your Voice Agent Service

Voice agents command 2-3x the pricing of text chatbots because they replace a more expensive human task (answering phones) and require more technical complexity to deliver. Use this pricing structure:

### Pricing Table

| Tier | Setup Fee | Monthly Retainer | What's Included |
|------|-----------|-----------------|-----------------|
| Starter | $2,000 | $500/mo | 1 voice agent, 100 calls/mo, email support |
| Growth | $4,000 | $800/mo | 1 agent, 500 calls/mo, transfers, integrations |
| Enterprise | $7,000 | $1,500/mo | Multiple agents, unlimited calls, custom workflows |

The setup fee covers 10-15 hours of configuration, testing, and deployment. The retainer covers monthly maintenance (updating the knowledge base, monitoring call quality, adjusting the system prompt), Vapi hosting costs, and ongoing support.

**Important:** The monthly retainer is not optional. Voice agents degrade without maintenance. New services get added. Insurance plans change. Office hours shift seasonally. Without someone updating the knowledge base and system prompt, the agent starts giving wrong answers within 60 days. The retainer protects the client's investment and guarantees your recurring revenue.

### Sales Method: The Live Demo Call

Do not send proposals. Do not send cold emails with attachments. The only sales method that works for voice agents is the live demo call, because the product is a phone experience — they have to hear it to believe it.

Here is the exact process:

1. Pick a business category. For your first, use dental practices — they have high call volume, repetitive questions, and clear ROI (every booked appointment = revenue).
2. Build the demo agent following Steps 1-4 of this guide with generic dental practice information.
3. Find 20 dental practices on Google Maps in a mid-size city (avoid major metros where competition is high).
4. Call each practice. When the receptionist answers, say: "Hi, I'm looking for a dentist and had a few questions — do you accept Delta Dental? What are your hours? Can I book a cleaning next week?" Listen to how long it takes them to answer. Most front desk staff spend 3-5 minutes on routine calls like this.
5. Then call the business owner or office manager directly. Say: "I noticed your front desk handles a lot of routine calls — insurance questions, scheduling, hours. I built an AI receptionist that answers those calls automatically, 24/7. It sounds like this." Then dial your demo agent on speakerphone. Have the owner listen to a 2-minute live conversation where the agent answers questions, schedules an appointment, and the Slack notification arrives.

This converts at 20-30% because:
- The owner hears the agent working in real time — no imagination required
- The Slack notification arriving during the demo proves the integration works
- The ROI is immediately calculable: if a receptionist costs $35,000/yr and the agent handles 60% of calls, the business saves $21,000/yr against a $6,000/yr agent cost

Close the deal on the call. Send a Stripe payment link for the setup fee. Schedule the discovery call for the following week.

## Step 7: Scale Your Voice Agent Business

Once you have delivered 3-5 voice agents and have a repeatable process, scaling requires removing yourself from three bottlenecks: building, selling, and maintaining.

### Hiring Plan

1. **Junior Builder ($15-25/hr, part-time contractor):** Hire from Upwork or a local university CS program. Give them this guide as a training manual. A trained builder can configure a Vapi agent in 6-8 hours. Pay per build, not hourly — $150-200 per completed agent. This keeps costs predictable and incentivizes speed.

2. **Sales Representative ($40-60K base + 10% commission):** Hire someone with B2B sales experience in SaaS or agency services. Equip them with the demo agent and the live demo call script. A good rep closes 4-6 deals per month at the Growth tier. Commission at 10% of setup fee ($400) + first month retainer ($80) = $480 per close. At 5 closes/month, that is $2,400 in commission plus their base.

3. **Account Manager ($20-30/hr, part-time contractor):** This person handles monthly maintenance — updating knowledge bases, reviewing call logs, adjusting prompts. Each client takes 1-2 hours per month. At 20 clients, that is 20-40 hours/month = $400-1,200/month. Charge this to the retainer.

### Multi-Industry Expansion

Once dental practices are working, expand to adjacent high-call-volume industries:

- **HVAC and plumbing companies** — emergency dispatch, service quotes, scheduling
- **Real estate agencies** — property inquiries, showing scheduling, agent transfers
- **Medical offices** (not dental) — appointment scheduling, insurance questions, prescription refill requests
- **Legal firms** — initial consultation screening, intake forms, scheduling
- **Auto repair shops** — service inquiries, appointment booking, status checks

Each industry needs: a new system prompt, industry-specific knowledge base documents, and a different transfer destination. The Vapi configuration is 80% identical across industries. Your builder can produce a new industry variant in 3-4 hours once they have the template.

### White-Label Option

At 15+ clients, approach other agencies (marketing agencies, IT consultants, web designers) who serve small businesses. Offer them a white-label version: they sell the voice agent under their brand, you build and maintain it, and you split revenue 50/50.

The math: a Growth-tier client at $4,000 setup + $800/mo retainer. You get $2,000 setup + $400/mo. The agency gets the same. You do the technical work; they do the client relationship. This scales faster because agencies already have the clients — you just add the voice agent to their service menu.

### Margin Analysis

| Item | Per Client (Growth Tier) |
|------|-------------------------|
| Revenue (setup) | $4,000 |
| Revenue (retainer) | $800/mo |
| Vapi costs | ~$30-80/mo |
| OpenAI API costs | ~$20-60/mo |
| ElevenLabs costs | ~$5-25/mo |
| Twilio phone number | $1.15/mo + $0.0085/min |
| Builder cost (setup) | $150-200 one-time |
| Account manager (monthly) | $25-50/mo |
| **Gross profit (setup)** | ~$3,800 |
| **Gross profit (monthly)** | ~$680-720/mo |

At 20 Growth-tier clients: $76,000 in setup revenue + $14,400/mo in recurring revenue. Monthly costs: ~$2,500. Monthly net profit: ~$11,900.

## Cost Breakdown

| Item | Free Tier | Paid Tier | When to Upgrade |
|------|-----------|-----------|-----------------|
| Vapi | 100 min/mo, 1 assistant | $30/mo (Pro) | At 2+ clients — need multiple assistants and more minutes |
| OpenAI API | Pay per use | ~$20-60/mo per client | Scales with call volume; monitor at platform.openai.com/usage |
| ElevenLabs | 10,000 chars/mo | $5/mo (Starter) | Immediately — 10K chars is ~8 minutes of speech, not enough for production |
| Twilio | $20 trial credit | $1.15/mo per number + $0.0085/min | After trial credit is used |
| Make.com | 1,000 operations/mo | $9/mo (Core) | At 3+ clients — appointment webhooks consume operations quickly |
| Google Cloud | Free tier | Free for Calendar API | Calendar API has generous free limits |
| Slack | Free | Free | Webhooks work on free plans |
| Stripe | Free | 2.9% + 30c per transaction | Always use for payments |
| Domain for demos | — | $12/yr | Immediately |

**Total monthly cost at 5 clients:** ~$150-250/mo
**Total monthly revenue at 5 clients:** $4,000/mo retainers + setup fees

## Production Checklist

Before deploying any voice agent to a client's phone line, verify every item:

- [ ] System prompt is client-specific (business name, address, services, policies — no placeholder text)
- [ ] Knowledge base documents are uploaded, indexed, and tested for accuracy
- [ ] Call transfer functions are configured with correct destination numbers (tested with a real transfer)
- [ ] Voicemail detection is enabled for outbound calls
- [ ] Appointment scheduling pipeline works end-to-end (call → Vapi → Make.com → Google Calendar → Slack → CRM)
- [ ] Barge-in is enabled — callers can interrupt the agent mid-sentence
- [ ] End-of-call detection is configured with appropriate silence timeout (10 seconds)
- [ ] Greeting latency is under 1.5 seconds (measured with a stopwatch on a real call)
- [ ] Background noise does not trigger false responses (tested from a noisy environment)
- [ ] Off-topic questions are rejected and redirected (tested with at least 3 unrelated questions)

## What to Do Next

Once you have delivered your first 3-5 voice agents in one business category, expand with these specific moves:

- **Add SMS follow-up** — After each call, send the caller a text summary using Twilio SMS. "Hi Alex, your teeth whitening appointment is confirmed for Thursday at 10 AM. Reply HELP if you need to reschedule." This reduces no-shows by 30-40% and is a premium upsell ($200/mo additional).
- **Build a second industry agent** — HVAC and plumbing have the highest call urgency and the worst after-hours coverage. An AI agent that answers "My furnace stopped working" at 2 AM and dispatches a technician is worth $10,000+ in setup to the right client.
- **Add outbound calling** — Configure the agent to make appointment reminder calls 24 hours before scheduled appointments. Vapi supports outbound campaigns. This is a $300-500/mo upsell that pays for itself in reduced no-shows.
- **Create a client dashboard** — Build a simple Notion or Google Sheets dashboard where clients can see call volume, appointment bookings, and transfer rates without logging into Vapi. This makes the retainer feel tangible and reduces churn.
- **Explore white-label partnerships** — Approach 5 local marketing agencies. Offer to provide voice agent services under their brand. Each partnership can generate 3-5 clients with zero sales effort on your part.
