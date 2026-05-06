---
title: "The ChatGPT Prompt Engineering Guide: 20 Steps to Master AI Prompts"
date: 2026-04-17
category: "Playbook"
price: "₦35,000"
readTime: "90 MIN"
excerpt: "Master prompt engineering for business. 200+ battle-tested prompts organized by function, the CRISP framework, advanced techniques, and model-specific optimization. Stop getting mediocre AI output."
image: "/images/articles/playbooks/chatgpt-prompt-engineering-guide.png"
heroImage: "/images/heroes/playbooks/chatgpt-prompt-engineering-guide.png"
---

Prompt engineering is not about clever tricks or secret formulas. It is about communicating clearly with a powerful but literal-minded assistant. Think of ChatGPT as a brilliant intern who can do anything you ask — but only exactly what you ask. If your instructions are vague, the output is vague. If your instructions are precise, the output is precise. This guide teaches you the systematic approach to crafting prompts that consistently produce high-quality outputs, regardless of the AI model you are using.

**The CRISP framework. 200+ prompts organized by business function. Advanced techniques for power users.** After reading this guide, you will never again stare at a chat box wondering what to type. You will have a library of proven prompts and the skill to adapt them for any situation.

---

# MODULE 1: THE CRISP FRAMEWORK

## Overview

Every effective prompt follows five elements. I call this the CRISP framework: Context, Role, Instructions, Specifications, and Parameters. Miss any one of these and your output quality drops. Include all five and you get consistent, high-quality results every time. This module teaches each element with examples and common mistakes.

## Element 1: Context (Background Information)

Context tells the AI what world it's operating in. Without context, the AI makes assumptions — and its assumptions are usually wrong for your specific situation. Context includes: who you are, what you're working on, who the audience is, and any relevant background the AI needs to produce useful output.

**Bad context:** "Write an email for my business."

**Good context:** "I run a boutique fitness studio in Austin, TX with 200 active members. Most members are women aged 28-45 who prioritize wellness and community. We offer group classes (yoga, HIIT, Pilates) and personal training. Our average monthly membership is $150."

The difference is specificity. The first prompt could produce anything — a B2B sales email, a corporate newsletter, a spam blast. The second prompt gives the AI enough information to write something that sounds like it belongs in your business.

**How much context is enough?** Include 3-5 sentences that cover: your business type, your audience, your goal, and any constraints. If you find yourself editing the AI's output to add specificity, you didn't provide enough context.

**Common mistake:** Providing too much context. If your context section exceeds 200 words, the AI loses the thread. Be concise but specific. "Boutique fitness studio in Austin, 200 members, women 28-45, group classes + PT, $150/mo average" is better than a page of background.

## Element 2: Role (Who the AI Should Be)

Role priming tells the AI what expertise to draw on. When you say "You are a [role]," the AI accesses patterns associated with that role — vocabulary, tone, analytical frameworks, and decision-making heuristics. This single addition can transform output quality by 50% or more.

**Bad role:** "Write a marketing plan."

**Good role:** "You are a senior marketing strategist at a top-5 agency with 15 years of experience in D2C brand launches. You think in terms of customer journeys, channel economics, and measurable KPIs. You are direct, opinionated, and always back recommendations with data."

The second role produces output that sounds like it came from a seasoned professional, not a generic assistant. The phrase "you are direct, opinionated, and always back recommendations with data" is doing heavy lifting — it prevents the AI from hedging and encourages specific, actionable recommendations.

**Role templates that work:**
- "You are a [role] with [years] of experience in [specialty]."
- "You are a [role] who thinks in terms of [frameworks]."
- "You are a [role] known for [distinctive approach]."
- "You are a [role] who always [behavior pattern]."

## Element 3: Instructions (Specific Tasks)

Instructions are the core of your prompt — what you want the AI to do. The key principle: be explicit about the process, not just the outcome. Tell the AI how to think, not just what to produce.

**Bad instructions:** "Write a blog post about email marketing."

**Good instructions:** "Write a blog post about email marketing for small business owners. Start with a surprising statistic about email ROI. Then explain 3 common mistakes small businesses make with email. For each mistake, provide the fix with specific tool recommendations. End with a 7-day action plan."

The second prompt structures the AI's thinking. It knows the opening needs a statistic, the body needs mistake-fix pairs, and the ending needs a timeline. This structure produces coherent, useful output instead of a rambling essay.

**Instruction patterns that produce great output:**
- "First [step 1]. Then [step 2]. Finally [step 3]."
- "For each [item], provide [specific deliverable]."
- "Start with [hook format]. Cover [topics]. End with [closing format]."
- "Analyze [subject] from [perspective 1], then [perspective 2], then synthesize."

## Element 4: Specifications (Format, Length, Tone)

Specifications tell the AI what the output should look like. Without specifications, the AI defaults to its own preferences — which may not match yours. Specify: format (list, table, paragraphs, dialogue), length (word count or number of items), tone (professional, casual, urgent, empathetic), and any structural requirements.

**Bad specifications:** (none)

**Good specifications:** "Format as a numbered list with 2-3 sentence explanations for each item. Use a conversational but authoritative tone — like a smart friend who knows what they're talking about. Keep the total response under 500 words. Bold the key term in each item."

**Critical specification: format.** The format specification has the biggest impact on output usefulness. "Format as a table with columns X, Y, Z" produces dramatically different (and usually more useful) output than "write about X, Y, and Z." Always specify format.

**Format options to use:**
- Tables (best for comparisons, pricing, features)
- Numbered lists (best for steps, rankings, priorities)
- Bullet points (best for features, benefits, ideas)
- Dialogue (best for scripts, conversation templates, role-plays)
- Outline (best for planning, strategy, content briefs)
- JSON/structured data (best for programmatic use, database entries)

## Element 5: Parameters (Constraints and Preferences)

Parameters are the guardrails. They tell the AI what NOT to do, which is often more important than telling it what to do. Parameters include: topics to avoid, words to use or not use, assumptions to not make, and quality standards.

**Bad parameters:** (none)

**Good parameters:** "Do not use the word 'leverage' or 'synergy.' Do not make up statistics — if you're not sure about a number, say 'approximately' or 'estimated.' Do not use jargon without defining it first. Prioritize actionable advice over theoretical frameworks. If there are multiple valid approaches, present the simplest one."

Parameters prevent the AI from falling into its worst habits: corporate jargon, hedging language, made-up statistics, and generic advice. The more specific your "don'ts," the more focused the output.

## Putting CRISP Together: A Complete Prompt

Here is a complete prompt using all five CRISP elements:

```
[Context] I run a SaaS startup that sells project management software to small creative agencies (5-20 employees). Our average customer pays $49/month. We've been running for 8 months and have 120 paying customers. Our churn rate is 5%/month, which is too high.

[Role] You are a SaaS growth consultant who specializes in churn reduction and retention strategy. You think in terms of cohort analysis, activation metrics, and customer lifecycle stages. You are direct and always provide specific, actionable recommendations.

[Instructions] Analyze the likely causes of our 5% monthly churn rate. For each likely cause, explain why it happens and provide a specific fix we can implement this week. Then create a 30-day churn reduction plan with weekly milestones.

[Specifications] Format as a structured document with headers for each cause and fix. Use a professional but accessible tone — no academic jargon. Include a summary table at the top showing: Cause | Likelihood | Fix | Time to Implement. Keep under 1,000 words.

[Parameters] Do not suggest "improve the product" as a standalone recommendation — be specific about what to improve and how. Do not recommend hiring additional staff — we're a 3-person team. Focus on quick wins first, then medium-term improvements.
```

This prompt will produce dramatically better output than "How do I reduce churn for my SaaS?" because every element of CRISP is present and specific. Memorize this framework. Apply it to every prompt you write.

---

# MODULE 2: CONTENT MARKETING PROMPTS

## Overview

Content marketing is where most businesses use AI — and where most get mediocre results. The problem isn't the AI; it's the prompts. This module gives you 40+ battle-tested prompts for every content marketing task, from blog posts to social media to email sequences.

## Blog Post Prompts

**Prompt 1: The SEO Article**
```
[Context] I need an SEO-optimized article targeting the keyword "[KEYWORD]" for my [BUSINESS TYPE] website targeting [AUDIENCE].
[Role] You are an SEO content strategist who writes articles that rank on page 1 of Google.
[Instructions] Write a comprehensive article (2,000-2,500 words) targeting this keyword. Structure: H1 title with keyword, introduction with the keyword in the first 100 words, 5-7 H2 sections each targeting a related secondary keyword, practical examples in each section, and a conclusion with a clear CTA. Include a meta description (155 characters max).
[Specifications] Professional but approachable tone. Short paragraphs (2-3 sentences). Use bullet points where appropriate. Bold key terms.
[Parameters] Do not keyword-stuff — use the keyword naturally 4-6 times. Do not write fluff or filler. Every paragraph must add value.
```

**Prompt 2: The Listicle**
```
[Context] I'm writing for [AUDIENCE] who struggle with [PROBLEM].
[Role] You are a content writer who specializes in listicles that get shared and bookmarked.
[Instructions] Write a listicle titled "[NUMBER] [ADJECTIVE] Ways to [ACHIEVE OUTCOME]". For each item: a punchy subheading, a 100-150 word explanation with a specific example, and one actionable tip the reader can implement today. Order from most impactful to least.
[Specifications] Conversational tone. Each item should be skimmable. Include a "Which one will you try first?" CTA at the end.
[Parameters] No generic advice like "stay consistent" or "work hard." Every tip must be specific and implementable within 24 hours.
```

**Prompt 3: The How-To Guide**
```
[Context] [AUDIENCE] need a step-by-step guide to [ACHIEVE OUTCOME]. They are beginners with no prior experience.
[Role] You are a technical writer who excels at making complex processes simple and actionable.
[Instructions] Write a how-to guide with exactly [NUMBER] steps. For each step: a clear subheading starting with a verb, a 2-3 sentence explanation of what to do, a specific example or tool recommendation, and a common mistake to avoid. Include prerequisites at the top and a troubleshooting section at the bottom.
[Specifications] Direct, instructional tone. Use numbered steps. Include estimated time for each step.
[Parameters] Do not skip steps or assume prior knowledge. If a step requires a paid tool, mention a free alternative.
```

**Prompt 4: The Thought Leadership Piece**
```
[Context] I'm a [ROLE] in the [INDUSTRY] space. I want to share a contrarian perspective on [TOPIC].
[Role] You are a thought leadership writer who crafts pieces that challenge conventional wisdom and spark discussion.
[Instructions] Write an opinion piece that argues [CONTRARIAN POSITION]. Structure: Open with the conventional wisdom and why it's wrong. Present 3 supporting arguments with evidence. Address the strongest counterargument. Close with what the reader should do differently starting today.
[Specifications] Confident, authoritative tone. No hedging — take a clear position. 800-1,200 words.
[Parameters] Do not use phrases like "some might argue" or "it could be said." Be direct. Back every claim with a specific example or data point.
```

**Prompt 5: The Case Study**
```
[Context] I helped [CLIENT TYPE] achieve [RESULT] using [METHOD] over [TIMEFRAME].
[Role] You are a case study writer who turns client results into compelling narratives.
[Instructions] Write a case study with this structure: Challenge (2-3 paragraphs describing the client's problem), Solution (the specific approach we took, step by step), Results (quantifiable outcomes with numbers), and Key Takeaways (3 lessons others can apply). Use direct quotes where appropriate.
[Specifications] Professional tone. Lead with the most impressive result. Include specific numbers (percentages, dollar amounts, time savings).
[Parameters] Do not exaggerate results. If a result was modest, frame it honestly — authenticity builds trust.
```

## Social Media Prompts

**Prompt 6: LinkedIn Post**
```
[Context] I want to share an insight about [TOPIC] with my LinkedIn network of [AUDIENCE].
[Role] You are a LinkedIn content creator whose posts consistently get 100+ engagements.
[Instructions] Write a LinkedIn post (under 1,300 characters) that opens with a hook (surprising stat, bold claim, or personal story), delivers one clear insight in 3-5 short paragraphs, and ends with a question that drives comments. Use line breaks between each paragraph.
[Specifications] Conversational, authentic tone. No corporate speak. Write like you're talking to a friend over coffee.
[Parameters] Do not start with "I'm humbled to announce" or "Excited to share." Do not use hashtags in the middle of the text (max 3 at the end).
```

**Prompt 7: Twitter/X Thread**
```
[Context] I want to share a [TOPIC] thread that positions me as knowledgeable about [SUBJECT].
[Role] You are a Twitter/X creator known for threads that get bookmarked and shared.
[Instructions] Write a 7-tweet thread. Tweet 1: Hook with a bold promise. Tweets 2-6: One key insight per tweet with an example. Tweet 7: Summary + CTA. Each tweet under 280 characters. Number each tweet (1/7, 2/7, etc.).
[Specifications] Punchy, direct tone. Short sentences. White space between ideas.
[Parameters] No filler tweets. If you can't fill 7 tweets with value, write fewer. Every tweet must be worth reading on its own.
```

**Prompt 8: Instagram Caption**
```
[Context] I'm posting [IMAGE DESCRIPTION] for my [BUSINESS TYPE] account targeting [AUDIENCE].
[Role] You are a social media manager who writes captions that drive saves and shares.
[Instructions] Write an Instagram caption that: starts with a scroll-stopping first line (not a question), provides value (tip, insight, or story) in the body, and ends with a CTA. Include a call-to-save if the content is reference-worthy.
[Specifications] Conversational and warm tone. Use line breaks for readability. 150-300 words.
[Parameters] No "link in bio" without context. No generic CTAs like "What do you think?" — ask a specific question instead.
```

**Prompt 9: TikTok/Reels Script**
```
[Context] I'm creating a [LENGTH]-second short-form video about [TOPIC] for [AUDIENCE].
[Role] You are a short-form video scriptwriter whose videos average 70%+ completion rate.
[Instructions] Write a script with: Hook (first 2 seconds — bold statement or visual), Problem (5 seconds — name the pain), Solution (15-30 seconds — 3 quick tips or one detailed method), CTA (3 seconds — follow for more). Include visual/audio cues in [brackets].
[Specifications] Fast-paced, energetic tone. Short sentences. No pauses or filler words.
[Parameters] The hook must be specific — no "Here's how to..." Start with a bold claim or surprising fact instead.
```

**Prompt 10: YouTube Video Script**
```
[Context] I'm making a YouTube video about [TOPIC] for [AUDIENCE] on my channel about [NICHE].
[Role] You are a YouTube scriptwriter who specializes in high-retention educational content.
[Instructions] Write a script for a [LENGTH]-minute video. Structure: Hook (15 sec — preview the most valuable part), Intro (30 sec — what they'll learn and why it matters), Main Content (break into 3-5 clear sections with transitions), and CTA (20 sec — subscribe + next video tease). Include timestamps for each section.
[Specifications] Conversational, energetic tone. Use "you" language. Include moments for visual demonstrations [VISUAL: description].
[Parameters] Do not start with "In this video I will show you..." — start with a hook that makes them NEED to keep watching.
```

## Email Marketing Prompts

**Prompt 11: Welcome Sequence**
```
[Context] I need a [NUMBER]-email welcome sequence for [BUSINESS] that sells [PRODUCT/SERVICE] to [AUDIENCE].
[Role] You are an email marketing strategist who writes sequences that convert subscribers into customers.
[Instructions] Write [NUMBER] emails in a welcome sequence. Email 1: Welcome + deliver lead magnet/discount. Email 2: Brand story + why we exist. Email 3: Best-seller showcase with descriptions. Email 4: Social proof (testimonials, reviews, case study). Email 5: Urgency — offer expires + final push. For each email: subject line (3 variations), preview text, body copy, CTA.
[Specifications] Warm, personal tone. Write like you're emailing a friend. Each email under 250 words. One CTA per email.
[Parameters] Do not use "I'm so excited you're here!" — open with something more specific and valuable. No manipulative urgency — only use real deadlines.
```

**Prompt 12: Abandoned Cart Recovery**
```
[Context] [BUSINESS TYPE] with [AVERAGE ORDER VALUE] average order value. Customers abandon carts at the checkout page.
[Role] You are an e-commerce email specialist who writes cart recovery sequences that recover 10%+ of abandoned carts.
[Instructions] Write a 3-email abandoned cart sequence. Email 1 (1 hour after): Friendly reminder, show what they left. Email 2 (24 hours): Social proof + answer common objections. Email 3 (48 hours): Final chance + incentive (discount or free shipping). For each: subject line, body, CTA.
[Specifications] Friendly, not desperate. Each email shorter than the last (150, 120, 80 words).
[Parameters] Do not use guilt trips. Do not assume they abandoned because of price — they might have been distracted.
```

**Prompt 13: Newsletter**
```
[Context] I send a weekly newsletter to [NUMBER] subscribers who are [AUDIENCE] interested in [TOPIC].
[Role] You are a newsletter writer whose open rates consistently exceed 45%.
[Instructions] Write this week's newsletter. Include: a personal opening (1-2 sentences), a main insight or lesson (3-4 paragraphs with an example), 3 curated resources with 1-sentence descriptions, and a question for readers to reply to.
[Specifications] Casual, personal tone. Write like you're writing to one person, not a list. Under 600 words total.
[Parameters] Do not start with "Happy [day of week]!" — start with a thought or observation. No sales pitches disguised as content.
```

**Prompt 14: Sales Email**
```
[Context] I'm selling [PRODUCT/SERVICE] at [PRICE] to [AUDIENCE] who previously [ACTION indicating interest].
[Role] You are a direct-response copywriter who writes sales emails that convert without being pushy.
[Instructions] Write a sales email that: opens with a specific problem the reader has, introduces the product as the solution, provides 3 specific benefits (not features) with proof, handles one key objection, and closes with a clear CTA. Include 3 subject line options.
[Specifications] Confident but not aggressive tone. Focus on transformation, not features. Under 300 words.
[Parameters] Do not use false scarcity unless the deadline is real. Do not use ALL CAPS or excessive punctuation. No "Act now!" language.
```

**Prompt 15: Re-engagement Email**
```
[Context] [PERCENTAGE]% of our email list hasn't opened an email in 90+ days. We want to win them back or clean the list.
[Role] You are an email marketing strategist who specializes in list hygiene and re-engagement.
[Instructions] Write a 3-email re-engagement sequence. Email 1: "We miss you" + best recent content. Email 2: Exclusive offer or resource. Email 3: "Last chance" + confirmation to stay or go. For each: subject line, body, CTA.
[Specifications] Warm, genuine tone. No guilt. Acknowledge they're busy.
[Parameters] Do not beg. If they don't engage after Email 3, suppress them — a clean list performs better than a large one.
```

---

# MODULE 3: SALES AND OUTREACH PROMPTS

## Overview

AI can transform your sales process from generic spray-and-pray to hyper-personalized outreach at scale. This module gives you prompts for cold emails, proposals, objection handling, and follow-up sequences.

**Prompt 16: Cold Email**
```
[Context] I'm reaching out to [PROSPECT TYPE] at [COMPANY] who [SPECIFIC OBSERVATION about their business].
[Role] You are a cold email specialist whose emails get 15%+ reply rates.
[Instructions] Write a cold email under 75 words. Structure: one specific observation about their business, one sentence on how you solve that problem, one question. No "I'd love to" or "I hope this finds you well." Include 3 subject line options.
[Specifications] Direct, conversational tone. Write like a human, not a salesperson.
[Parameters] No attachments. No "just checking in" follow-ups. Every word must earn its place.
```

**Prompt 17: Follow-Up Sequence**
```
[Context] I sent a cold email to [PROSPECT] about [OFFER] on [DATE] and haven't received a reply.
[Role] You are a sales strategist who writes follow-ups that get replies without being annoying.
[Instructions] Write a 3-email follow-up sequence. Follow-up 1 (Day 4): Add one new piece of value (insight, article, or observation). Follow-up 2 (Day 9): Share a relevant case study or result. Follow-up 3 (Day 14): Break-up email — give them permission to say no. Each under 50 words.
[Specifications] Friendly, low-pressure tone. Never guilt-trip or assume they read the previous email.
[Parameters] No "just circling back" or "bumping this up." Each follow-up must add new value, not just repeat the ask.
```

**Prompt 18: Proposal**
```
[Context] I had a discovery call with [COMPANY] about [PROJECT/SERVICE]. They need [SPECIFIC SOLUTION].
[Role] You are a proposal writer whose proposals close at 40%+.
[Instructions] Write a one-page proposal with: Executive Summary (3 sentences), Scope of Work (3-5 bullet points with deliverables), Timeline (weekly milestones), Investment (3 pricing tiers in a table), and Next Steps (2-3 actions). Include a section for terms: payment schedule, revision policy, and cancellation terms.
[Specifications] Professional, confident tone. Lead with the outcome, not the process.
[Parameters] Do not include hourly rates — present value-based pricing. Do not over-promise on timelines.
```

**Prompt 19: Objection Handler**
```
[Context] A prospect said: "[SPECIFIC OBJECTION]" in response to my proposal for [SERVICE] at [PRICE].
[Role] You are a sales coach who specializes in objection handling without high-pressure tactics.
[Instructions] Write a response that: validates their concern (1 sentence), reframes the objection (2-3 sentences with evidence), and proposes a next step that reduces their risk. Provide 3 alternative framings so I can choose the best fit for this prospect's personality.
[Specifications] Empathetic but confident tone. Never dismissive of their concern.
[Parameters] Do not use "Yes, but..." — validate first, then reframe. Do not discount without getting something in return (longer contract, referral, case study rights).
```

**Prompt 20: Pricing Justification**
```
[Context] A client is questioning our price of [PRICE] for [SERVICE]. They said a competitor quoted [LOWER PRICE].
[Role] You are a value-based pricing strategist who helps businesses defend premium rates.
[Instructions] Write a response that: acknowledges the price difference, explains 3 specific value differences that justify the premium, quantifies the ROI they'll get at our price point, and offers a risk-reduction option (money-back guarantee, performance bonus structure, or phased engagement) instead of a discount.
[Specifications] Confident, not defensive. Focus on what they gain, not what the competitor lacks.
[Parameters] Never apologize for your pricing. Never race to the bottom on price.
```

---

# MODULE 4: OPERATIONS AND AUTOMATION PROMPTS

## Overview

AI isn't just for content — it can automate operations, streamline workflows, and handle the administrative overhead that eats your day. This module gives you prompts for SOPs, workflows, customer support, and process optimization.

**Prompt 21: Standard Operating Procedure**
```
[Context] I need an SOP for [PROCESS] that [TEAM MEMBER TYPE] can follow without supervision.
[Role] You are an operations manager who writes SOPs that eliminate ambiguity and reduce errors.
[Instructions] Write an SOP with: Purpose (1 sentence), Prerequisites (tools, access, information needed), Step-by-step instructions (numbered, with specific actions — "Click File then Export" not "export the file"), Decision points (if X then Y, if A then B), Quality checkpoints (what to verify before moving on), and Troubleshooting (common issues and fixes).
[Specifications] Direct, instructional tone. No unnecessary words. Format as a numbered list with sub-steps.
[Parameters] Do not assume prior knowledge. If a step requires a specific tool, name it. If a step requires a login, specify which account.
```

**Prompt 22: Workflow Automation Design**
```
[Context] I want to automate [PROCESS] that currently involves [CURRENT MANUAL STEPS].
[Role] You are an automation architect who designs workflows in Make.com and Zapier.
[Instructions] Design an automation workflow. For each step: specify the trigger/app, the action, the data mapping (what input → what output), and the error handling (what happens if this step fails). Include: the trigger event, all intermediate steps, the final output, error notification setup, and a testing plan.
[Specifications] Technical but accessible. Use a flowchart-style format: [Trigger] → [Step 1] → [Step 2] → [Output].
[Parameters] Do not over-automate. If a step requires human judgment, keep it manual and flag it for review.
```

**Prompt 23: Customer Support Response**
```
[Context] A customer wrote: "[CUSTOMER MESSAGE]". Our policy on this issue is: [POLICY].
[Role] You are a customer support specialist who turns complaints into loyalty.
[Instructions] Write a response that: acknowledges their frustration specifically (not generically), explains what happened without making excuses, provides the resolution or next steps, and adds something extra to rebuild goodwill. Keep under 150 words.
[Specifications] Empathetic, professional tone. Use "we" for company actions, "I" for personal follow-through.
[Parameters] Never say "we apologize for any inconvenience" — be specific about what went wrong. Never blame the customer.
```

**Prompt 24: Meeting Agenda and Notes**
```
[Context] I'm having a [TYPE] meeting with [PARTICIPANTS] about [TOPIC]. The goal is [OUTCOME].
[Role] You are an executive assistant who runs meetings that start and end on time with clear outcomes.
[Instructions] Create: a meeting agenda (5-7 items with time allocations totaling [MEETING LENGTH] minutes), discussion questions for each agenda item, and a decision template (Decision | Owner | Deadline). Then create a meeting notes template for capturing: decisions made, action items with owners and deadlines, and parking lot items.
[Specifications] Concise, structured format. No agenda item should exceed 10 minutes.
[Parameters] Do not include "any other business" — force items to be submitted in advance.
```

**Prompt 25: Project Brief**
```
[Context] I need to brief [TEAM/CONTRACTOR] on a [PROJECT TYPE] project for [CLIENT/BUSINESS].
[Role] You are a project manager who writes briefs that eliminate scope creep and miscommunication.
[Instructions] Write a project brief with: Background (2-3 sentences of context), Objective (one clear sentence), Deliverables (specific, measurable items), Timeline (milestones with dates), Budget (if applicable), Brand Guidelines (tone, style, examples), Stakeholders (who approves what), and Out of Scope (explicitly state what is NOT included).
[Specifications] Clear, unambiguous language. If a deliverable can be interpreted multiple ways, specify exactly what it means.
[Parameters] Do not leave anything open to interpretation. "A report" is not a deliverable — "a 10-page PDF report with executive summary, data visualizations, and recommendations" is.
```

---

# MODULE 5: STRATEGY AND ANALYSIS PROMPTS

## Overview

AI excels at analysis when you give it structured data and the right analytical framework. This module covers prompts for market research, competitive analysis, financial modeling, and strategic planning.

**Prompt 26: Market Research**
```
[Context] I'm exploring the [MARKET/INDUSTRY] for a potential [PRODUCT/SERVICE] targeting [AUDIENCE].
[Role] You are a market research analyst who provides data-driven insights for business decisions.
[Instructions] Analyze this market. Cover: market size and growth rate, key trends (3-5), target customer segments with demographics and psychographics, top 5 competitors with strengths/weaknesses, barriers to entry, and your assessment of opportunity (high/medium/low with rationale). Where specific data is unavailable, indicate estimates and your confidence level.
[Specifications] Analytical, objective tone. Use numbers wherever possible. Present as a structured report with headers.
[Parameters] Do not fabricate statistics. If you're estimating, say "estimated" and explain your basis. Flag high-uncertainty areas.
```

**Prompt 27: Competitor Analysis**
```
[Context] I need to understand how [COMPANY] competes in the [INDUSTRY] space. Their website is [URL] and they target [AUDIENCE].
[Role] You are a competitive intelligence analyst who identifies opportunities others miss.
[Instructions] Analyze this competitor. Cover: positioning and messaging, pricing model and tiers, product/service features (strengths and gaps), target audience and how they reach them, content strategy, customer reviews (common praise and complaints), and 3 opportunities to differentiate against them.
[Specifications] Objective, evidence-based analysis. No unsubstantiated claims.
[Parameters] Do not criticize competitors personally. Focus on strategic gaps, not flaws. Where you lack data, state assumptions clearly.
```

**Prompt 28: SWOT Analysis**
```
[Context] I'm evaluating [BUSINESS/PROJECT/DECISION] in the context of [MARKET SITUATION].
[Role] You are a strategic consultant who conducts SWOT analyses that lead to action, not just categorization.
[Instructions] Conduct a SWOT analysis with 5 items in each quadrant. For each item: a 1-sentence description, the strategic implication (why it matters), and a recommended action. After the SWOT, identify: the #1 strength to amplify, the #1 weakness to address immediately, the #1 opportunity to pursue, and the #1 threat to monitor.
[Specifications] Concise, strategic tone. Format as a table with columns: Item | Implication | Action.
[Parameters] Do not list generic items like "experienced team" or "market competition." Be specific to this business and this moment.
```

**Prompt 29: Financial Projection**
```
[Context] I'm launching a [BUSINESS TYPE] with [PRICING MODEL]. My costs are: [LIST COSTS]. My target market has [MARKET SIZE] potential customers.
[Role] You are a financial analyst who builds realistic projections for small businesses.
[Instructions] Create a 12-month financial projection. Include: Monthly revenue (conservative, moderate, optimistic), monthly expenses (fixed and variable), monthly profit/loss, cumulative profit/loss, and break-even month. Show your assumptions clearly. Calculate: customer acquisition cost, lifetime value, and payback period.
[Specifications] Use a table format. Round to whole numbers. Show the math for key calculations.
[Parameters] Do not use hockey-stick growth assumptions. Revenue should grow realistically month-over-month. Be transparent about which numbers are assumptions vs. facts.
```

**Prompt 30: Business Model Canvas**
```
[Context] I'm building a [BUSINESS TYPE] that offers [PRODUCT/SERVICE] to [TARGET MARKET].
[Role] You are a business model designer who uses the Business Model Canvas framework.
[Instructions] Complete a Business Model Canvas with all 9 building blocks: Key Partners, Key Activities, Key Resources, Value Propositions, Customer Relationships, Channels, Customer Segments, Cost Structure, and Revenue Streams. For each block, provide 3-5 specific items with brief explanations.
[Specifications] Concise, specific entries. No generic items like "provide good service."
[Parameters] Every entry must be specific to this business. "Google Ads" is a channel. "Digital marketing" is not.
```

---

# MODULE 6: ADVANCED TECHNIQUES

## Overview

The prompts in Modules 2-5 use single-turn interactions: you ask, the AI answers. This module covers advanced techniques that use multi-turn conversations, structured reasoning, and prompt chaining to produce dramatically better results. These are the techniques that separate casual AI users from power users.

## Technique 1: Chain-of-Thought Prompting

Chain-of-thought prompting asks the AI to show its reasoning before giving an answer. This forces the AI to think step by step, which produces more accurate and nuanced outputs — especially for analytical tasks, problem-solving, and complex decisions.

**How to use it:** Add "Think step by step" or "Walk through your reasoning before answering" to any prompt.

**Example:**
```
A SaaS company has 1,000 customers paying $99/month. Monthly churn is 5%.
They acquire 80 new customers per month at $200 CAC.
Think step by step: Is this business growing or shrinking? By how much?
What's the break-even acquisition rate?
```

Without chain-of-thought, the AI might give a wrong answer. With it, the AI shows its work: starting MRR, churn loss, new MRR, net change, and the calculation for break-even. You can verify each step and catch errors.

**When to use it:** Financial analysis, strategic decisions, debugging, research synthesis, and any task where the process matters as much as the answer.

## Technique 2: Few-Shot Learning

Few-shot learning gives the AI examples of the output you want before asking it to produce new output. Examples are more powerful than instructions because they demonstrate exactly what "good" looks like.

**How to use it:** Include 2-3 examples in your prompt before asking the AI to generate a new one.

**Example:**
```
Write a one-sentence product description following these examples:

Example 1: "Slack brings all your communication together in one place — messaging, files, tools, and people — so you can get more done with less effort."
Example 2: "Notion is your all-in-one workspace for notes, docs, projects, and collaboration — replacing five apps with one."
Example 3: "Calendly eliminates the back-and-forth of scheduling by letting people book time on your calendar instantly."

Now write one for: [YOUR PRODUCT]
```

The AI will match the pattern: [Product name] + [what it does] + [key benefit] — in one sentence. No instructions needed about length or format because the examples define those constraints.

**When to use it:** Writing tasks with a consistent format, creating templates, generating variations on a theme, and establishing brand voice.

## Technique 3: Prompt Chaining

Prompt chaining breaks complex tasks into a sequence of prompts, where each prompt's output feeds into the next. This produces better results than trying to do everything in one giant prompt because each step gets the AI's full attention.

**How to use it:** Plan your chain before starting. Each step should produce a specific, intermediate output.

**Example chain for writing a blog post:**
1. Prompt 1: "Generate 10 blog post titles about [TOPIC] targeting [KEYWORD]. For each, rate the SEO potential (1-10) and explain why."
2. Prompt 2: "Take title #3 and create a detailed content brief: H2 headings, key points to cover in each section, target word count per section, and internal linking suggestions."
3. Prompt 3: "Using this content brief, write the full article. Follow the brief exactly."
4. Prompt 4: "Review this article for: factual accuracy, logical flow, SEO optimization, and readability. Suggest specific improvements."

Each prompt builds on the previous one's output. The result is a researched, structured, written, and reviewed article — far better than what you'd get from a single "write an article about X" prompt.

**When to use it:** Any multi-step creative or analytical process: content creation, business planning, research reports, and product development.

## Technique 4: System Prompts

System prompts set persistent instructions that apply to an entire conversation. Instead of repeating context and constraints in every message, you set them once and the AI maintains them throughout.

**How to use it:** In ChatGPT, create a Custom Instruction or use the system message in API calls. In Claude, use the system prompt field.

**Example system prompt:**
```
You are a business consultant for small service-based businesses. Your communication style is:
- Direct and actionable — no hedging or filler
- Specific — always include examples, numbers, or tool recommendations
- Honest — if something is a bad idea, say so and explain why
- Concise — never use 10 words when 5 will do
- No corporate jargon — say "use" not "leverage," say "help" not "facilitate"
```

With this system prompt active, every response in the conversation will automatically follow these rules. You don't need to remind the AI in every prompt.

**When to use it:** Ongoing projects, team-wide AI usage (ensures consistency), and any conversation where you want the AI to maintain a specific persona or set of rules.

## Technique 5: The Critic-Creator Pattern

This pattern uses two AI interactions: one to create, one to critique. The critique catches problems the creator missed, and you iterate until the output meets your standard.

**How to use it:**
1. Create: Use a prompt to generate the first draft.
2. Critique: "Review this [OUTPUT] as a [ROLE] would. Identify 5 specific problems: unclear sections, weak arguments, missing information, tone inconsistencies, and structural issues. For each problem, suggest a specific fix."
3. Revise: Apply the fixes and generate an improved version.
4. Repeat steps 2-3 until satisfied.

**When to use it:** Important deliverables (proposals, published content, client-facing reports), high-stakes communication, and any output where quality matters more than speed.

---

# MODULE 7: MODEL-SPECIFIC OPTIMIZATION

## Overview

Not all AI models are the same. ChatGPT, Claude, Gemini, and Llama each have different strengths, weaknesses, and optimal prompting strategies. This module shows you how to adapt your prompts for each model.

## ChatGPT (GPT-4o / GPT-4o-mini)

**Strengths:** Versatile, follows complex instructions well, great at formatting, strong creative writing, excellent at code generation.

**Weaknesses:** Tends to be verbose, sometimes over-explains, can be overly agreeable (won't push back on bad ideas), occasionally fabricates specifics.

**Optimization tips:**
- Use explicit word count limits: "Keep under 500 words"
- Ask for specific formatting: "Format as a table with columns X, Y, Z"
- Push back capability: "After answering, tell me if my question assumes something incorrect"
- Reduce verbosity: "Be concise. No filler or preamble."
- Prevent fabrication: "Do not make up statistics. If you're uncertain, say so."

## Claude (Claude 3.5 Sonnet / Opus)

**Strengths:** Superior for long-form content, nuanced analysis, following complex multi-step instructions, and maintaining consistent voice over long outputs.

**Weaknesses:** Sometimes overly cautious, may refuse legitimate requests, slightly slower response time.

**Optimization tips:**
- Use XML tags for structure: `<context>...</context>`, `<instructions>...</instructions>`
- Be explicit about what you want, not what you don't: Claude responds better to positive instructions than negative constraints
- For long outputs, specify the desired length explicitly
- When Claude refuses a legitimate request, rephrase: "As a business consultant, provide analysis of..." rather than direct requests

## Google Gemini

**Strengths:** Strong at research-backed content, good at synthesis from multiple sources, integrates with Google ecosystem, handles multimodal inputs well.

**Weaknesses:** Sometimes inconsistent output quality, may over-cite or under-cite sources, formatting can be unpredictable.

**Optimization tips:**
- Specify source expectations: "Based on publicly available information" or "Synthesize the following information"
- Be very explicit about formatting — Gemini sometimes ignores format instructions
- Use for research-heavy tasks where Google Search integration helps
- Double-check factual claims — Gemini occasionally presents outdated information

## Open-Source Models (Llama 3, Mistral)

**Strengths:** Free or very low cost, can be run locally for privacy, customizable through fine-tuning.

**Weaknesses:** Less capable than GPT-4o/Claude for complex reasoning, shorter context windows, may require more explicit instructions.

**Optimization tips:**
- Be extremely explicit in instructions — open-source models need more guidance
- Break complex tasks into smaller steps
- Use few-shot examples extensively — they have a bigger impact on open-source models
- Keep prompts under 2,000 tokens for best results

---

# MODULE 8: BUILDING YOUR PROMPT LIBRARY

## Overview

A personal prompt library is your most valuable AI asset. It's the difference between spending 15 minutes crafting a prompt from scratch every time versus pulling a proven prompt from your library and adapting it in 2 minutes. This module shows you how to build, organize, and maintain your prompt library.

## Structure

Organize your library by business function, not by AI model. Within each function, store prompts with this metadata:

- **Name:** Descriptive name (e.g., "SEO Blog Post — Comprehensive")
- **Category:** Content, Sales, Operations, Strategy, or Analysis
- **Purpose:** What this prompt produces
- **Variables:** What you need to fill in each time (in [BRACKETS])
- **Best model:** Which AI model produces the best results
- **Last tested:** Date you last verified the prompt works well
- **Notes:** Any quirks or tips

## The Starter Library: 20 Essential Prompts

Here are the 20 prompts you should save first, organized by category. Each one is ready to copy, fill in, and use.

**Content (7):**
1. SEO Blog Post (Prompt 1 from Module 2)
2. Listicle (Prompt 2 from Module 2)
3. How-To Guide (Prompt 3 from Module 2)
4. LinkedIn Post (Prompt 6 from Module 2)
5. Twitter/X Thread (Prompt 7 from Module 2)
6. Welcome Email Sequence (Prompt 11 from Module 2)
7. Sales Email (Prompt 14 from Module 2)

**Sales (4):**
8. Cold Email (Prompt 16 from Module 3)
9. Follow-Up Sequence (Prompt 17 from Module 3)
10. Proposal (Prompt 18 from Module 3)
11. Objection Handler (Prompt 19 from Module 3)

**Operations (4):**
12. Standard Operating Procedure (Prompt 21 from Module 4)
13. Workflow Automation Design (Prompt 22 from Module 4)
14. Customer Support Response (Prompt 23 from Module 4)
15. Project Brief (Prompt 25 from Module 4)

**Strategy (3):**
16. Market Research (Prompt 26 from Module 5)
17. Competitor Analysis (Prompt 27 from Module 5)
18. Financial Projection (Prompt 29 from Module 5)

**Utility (2):**
19. CRISP Prompt Builder: "I need to write a prompt for [TASK]. Using the CRISP framework, help me construct a complete prompt with Context, Role, Instructions, Specifications, and Parameters."
20. Critic-Reviewer: "Review this [CONTENT TYPE] as a [ROLE] would. Identify 5 specific problems and suggest fixes."

## Maintenance

Review your prompt library monthly. Remove prompts that no longer produce good results (AI models update and some prompts degrade). Add new prompts as you discover techniques that work. Update the "Last tested" date each time you use a prompt. A well-maintained library compounds in value over time — each prompt saves you 10-15 minutes of prompt engineering, and a library of 50+ prompts saves you 8-12 hours per month.

---

Stop getting mediocre AI output. The difference between "AI doesn't work for my business" and "AI is my secret weapon" is the quality of your prompts. The CRISP framework gives you the structure. The 200+ prompts in this guide give you the starting points. The advanced techniques give you the edge. Now open ChatGPT and start building your library.
