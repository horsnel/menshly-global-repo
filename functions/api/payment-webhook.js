// CloudFlare Pages Function: Paystack Webhook
// This runs as a Pages Function at /api/payment-webhook
// The main worker is in workers/paystack-webhook.js for standalone deployment

export async function onRequestPost(context) {
  const { request, env } = context;

  try {
    const rawBody = await request.text();
    let payload;

    try {
      payload = JSON.parse(rawBody);
    } catch {
      return new Response(JSON.stringify({ error: 'Invalid JSON' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    // Verify Paystack signature
    const headerSignature = request.headers.get('X-Paystack-Signature');
    const secretKey = env.PAYSTACK_SECRET_KEY;

    if (secretKey && headerSignature) {
      const sigValid = await verifySignature(rawBody, secretKey, headerSignature);
      if (!sigValid) {
        console.error('Invalid Paystack signature');
        return new Response(JSON.stringify({ error: 'Invalid signature' }), {
          status: 401,
          headers: { 'Content-Type': 'application/json' },
        });
      }
    }

    const event = payload.event;

    // Only process successful charges
    if (event !== 'charge.success') {
      return new Response(JSON.stringify({ status: 'ignored', event }), {
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const data = payload.data;
    const customerEmail = data.customer?.email;
    const amount = data.amount;
    const currency = data.currency || 'USD';
    const reference = data.reference;
    const metadata = data.metadata || {};
    const productTitle = metadata.product || 'Unknown Playbook';
    const pdfSlug = metadata.pdf_slug || '';
    const siteUrl = env.SITE_URL || 'https://menshly-global-enz.pages.dev';

    if (!customerEmail) {
      return new Response(JSON.stringify({ error: 'Missing customer email' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    // Check for duplicate (idempotency)
    if (env.PURCHASES) {
      const existing = await env.PURCHASES.get(`ref:${reference}`);
      if (existing) {
        return new Response(JSON.stringify({ status: 'already_processed', reference }), {
          headers: { 'Content-Type': 'application/json' },
        });
      }
    }

    // Build PDF download URL
    const pdfUrl = pdfSlug
      ? `${siteUrl}/pdfs/${pdfSlug}.pdf`
      : `${siteUrl}/pdfs/${productTitle.toLowerCase().replace(/[^a-z0-9]+/g, '-')}.pdf`;

    // Generate delivery token for secure access
    const deliveryToken = await generateDeliveryToken(reference, customerEmail);
    const deliveryUrl = `${siteUrl}/delivery/?slug=${encodeURIComponent(pdfSlug)}&token=${deliveryToken}`;

    // Store purchase in KV
    const purchaseRecord = {
      email: customerEmail,
      product: productTitle,
      type: metadata.type || 'playbook',
      amount,
      currency,
      reference,
      pdfUrl,
      pdf_slug: pdfSlug,
      deliveryToken,
      deliveryUrl,
      source: metadata.source || '',
      purchasedAt: new Date().toISOString(),
      emailSent: false,
    };

    if (env.PURCHASES) {
      await env.PURCHASES.put(`ref:${reference}`, JSON.stringify(purchaseRecord), { expirationTtl: 7776000 });
      await env.PURCHASES.put(`email:${customerEmail}:${reference}`, JSON.stringify(purchaseRecord), { expirationTtl: 7776000 });
      // Store token lookup for verification
      await env.PURCHASES.put(`token:${deliveryToken}`, JSON.stringify(purchaseRecord), { expirationTtl: 7776000 });
    }

    // Send email via configured provider
    let emailSent = false;
    if (env.EMAIL_API_KEY) {
      try {
        emailSent = await sendEmail(env, {
          to: customerEmail,
          productTitle,
          amount,
          currency,
          reference,
          pdfUrl,
          deliveryUrl,
          siteUrl,
        });
      } catch (emailErr) {
        console.error('Email send failed:', emailErr.message);
      }
    }

    // Update KV record
    if (env.PURCHASES && emailSent) {
      purchaseRecord.emailSent = true;
      await env.PURCHASES.put(`ref:${reference}`, JSON.stringify(purchaseRecord), { expirationTtl: 7776000 });
    }

    // Admin notification via Formspree
    try {
      await fetch('https://formspree.io/f/xreawkow', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify({
          _subject: `Playbook Purchase: ${productTitle}`,
          _type: 'paystack_webhook_purchase',
          customer_email: customerEmail,
          product: productTitle,
          amount: `${currency} ${(amount / 100).toFixed(2)}`,
          reference,
          pdf_url: pdfUrl,
          email_sent: emailSent,
        }),
      });
    } catch {}

    return new Response(JSON.stringify({ status: 'processed', reference, emailSent }), {
      headers: { 'Content-Type': 'application/json' },
    });

  } catch (error) {
    console.error('Webhook error:', error);
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}

// Health check
export async function onRequestGet() {
  return new Response(JSON.stringify({
    status: 'active',
    service: 'Menshly Global Payment Webhook',
    version: '2.0.0',
    features: ['signature_verification', 'kv_storage', 'email_delivery', 'idempotency'],
  }), {
    headers: { 'Content-Type': 'application/json' },
  });
}

// ─── Signature Verification ───────────────────────────────────────────────────
async function verifySignature(rawBody, secretKey, headerSignature) {
  try {
    const encoder = new TextEncoder();
    const key = await crypto.subtle.importKey(
      'raw',
      encoder.encode(secretKey),
      { name: 'HMAC', hash: 'SHA-512' },
      false,
      ['sign']
    );
    const signature = await crypto.subtle.sign('HMAC', key, encoder.encode(rawBody));
    const hashArray = Array.from(new Uint8Array(signature));
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    return hashHex === headerSignature;
  } catch {
    return false;
  }
}

// ─── Delivery Token Generator ─────────────────────────────────────────────────
async function generateDeliveryToken(reference, email) {
  const encoder = new TextEncoder();
  const data = encoder.encode(`${reference}:${email}:${Date.now()}:${Math.random()}`);
  const hashBuffer = await crypto.subtle.digest('SHA-256', data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('').substring(0, 32);
}

// ─── Email Delivery ───────────────────────────────────────────────────────────
async function sendEmail(env, { to, productTitle, amount, currency, reference, pdfUrl, deliveryUrl, siteUrl }) {
  const provider = env.EMAIL_PROVIDER || 'resend';
  const from = env.EMAIL_FROM || 'Menshly Global <onboarding@resend.dev>';
  const amountDisplay = `${currency} ${(amount / 100).toFixed(2)}`;
  const subject = `Your Playbook: ${productTitle} — Download Ready`;
  const accessUrl = deliveryUrl || pdfUrl;

  const html = buildEmailHtml({ productTitle, amountDisplay, reference, pdfUrl, accessUrl, siteUrl });
  const text = `MENSHLY GLOBAL — Your Playbook Is Ready\n\nThank you for purchasing ${productTitle}. Your payment of ${amountDisplay} was successful.\n\nAccess your playbook: ${accessUrl}\nDirect PDF download: ${pdfUrl}\n\nReference: ${reference}\n\nMenshly Global — Where AI Meets Revenue`;

  if (provider === 'resend') {
    const res = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${env.EMAIL_API_KEY}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ from, to: [to], subject, html, text }),
    });
    return res.ok;
  }

  if (provider === 'mailgun') {
    const domain = env.MAILGUN_DOMAIN || 'menshlyglobal.com';
    const res = await fetch(`https://api.mailgun.net/v3/${domain}/messages`, {
      method: 'POST',
      headers: { 'Authorization': `Basic ${btoa(`api:${env.EMAIL_API_KEY}`)}` },
      body: new URLSearchParams({ from, to, subject, html, text }),
    });
    return res.ok;
  }

  if (provider === 'sendgrid') {
    const match = from.match(/^(.+?)\s*<(.+)>$/);
    const fromName = match ? match[1].trim() : 'Menshly Global';
    const fromEmail = match ? match[2].trim() : from;
    const res = await fetch('https://api.sendgrid.com/v3/mail/send', {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${env.EMAIL_API_KEY}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        personalizations: [{ to: [{ email: to }] }],
        from: { email: fromEmail, name: fromName },
        subject,
        content: [
          { type: 'text/plain', value: text },
          { type: 'text/html', value: html },
        ],
      }),
    });
    return res.ok;
  }

  console.error(`Unknown email provider: ${provider}`);
  return false;
}

function buildEmailHtml({ productTitle, amountDisplay, reference, pdfUrl, accessUrl, siteUrl }) {
  return `<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"></head>
<body style="margin:0;padding:0;background:#111111;">
<div style="font-family:Inter,-apple-system,sans-serif;max-width:600px;margin:0 auto;background:#1A1A1A;color:#FFFFFF;">
  <div style="border-bottom:3px solid #F9FF00;padding:24px 32px;">
    <h1 style="font-family:Oswald,Arial Black,sans-serif;color:#F9FF00;font-size:20px;margin:0;letter-spacing:4px;">MENSHLY GLOBAL</h1>
  </div>
  <div style="padding:32px;">
    <h2 style="font-family:Oswald,Arial Black,sans-serif;font-size:22px;margin:0 0 16px 0;">YOUR PLAYBOOK IS READY</h2>
    <p style="font-size:16px;line-height:1.6;margin:0 0 16px 0;color:#CCCCCC;">Thank you for purchasing <strong style="color:#F9FF00;">${productTitle}</strong>. Your payment of <strong>${amountDisplay}</strong> was successful.</p>
    <p style="font-size:16px;line-height:1.6;margin:0 0 24px 0;color:#CCCCCC;">Click the button below to access your playbook:</p>
    <div style="text-align:center;margin:28px 0;">
      <a href="${accessUrl || pdfUrl}" style="display:inline-block;background:#F9FF00;color:#1A1A1A;font-family:Oswald,Arial Black,sans-serif;font-weight:700;font-size:18px;padding:16px 44px;text-decoration:none;letter-spacing:2px;border:3px solid #F9FF00;">ACCESS PLAYBOOK</a>
    </div>
    <div style="text-align:center;margin:12px 0;">
      <a href="${pdfUrl}" style="display:inline-block;background:transparent;color:#F9FF00;font-family:Oswald,Arial Black,sans-serif;font-weight:600;font-size:14px;padding:12px 32px;text-decoration:none;letter-spacing:1px;border:2px solid #F9FF00;">OR DOWNLOAD PDF DIRECTLY</a>
    </div>
    <div style="background:#111111;border:1px solid #333333;padding:16px;margin:24px 0;">
      <p style="font-size:13px;color:#999999;margin:0 0 8px 0;">If the buttons don't work, copy and paste this link:</p>
      <p style="font-size:13px;color:#F9FF00;margin:0;word-break:break-all;">${accessUrl || pdfUrl}</p>
    </div>
    <div style="border-top:1px solid #333333;padding-top:16px;margin-top:24px;">
      <table style="width:100%;font-size:14px;color:#999999;"><tr><td style="padding:4px 0;">Reference:</td><td style="text-align:right;color:#CCCCCC;">${reference}</td></tr><tr><td style="padding:4px 0;">Product:</td><td style="text-align:right;color:#CCCCCC;">${productTitle}</td></tr><tr><td style="padding:4px 0;">Amount:</td><td style="text-align:right;color:#CCCCCC;">${amountDisplay}</td></tr><tr><td style="padding:4px 0;">Access:</td><td style="text-align:right;color:#CCCCCC;">90 days from purchase</td></tr></table>
    </div>
    <p style="font-size:14px;color:#666666;margin-top:20px;">If you have any issues, reply to this email and we'll help you within 24 hours.</p>
  </div>
  <div style="border-top:3px solid #F9FF00;padding:20px 32px;">
    <p style="font-size:12px;color:#666666;margin:0;">Menshly Global — Where AI Meets Revenue</p>
  </div>
</div>
</body></html>`;
}
