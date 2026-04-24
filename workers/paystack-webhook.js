// CloudFlare Worker: Paystack Webhook → PDF Delivery via Email
// Verifies payment, stores purchase record in KV, sends branded email with download link
//
// Environment Variables needed:
//   PAYSTACK_SECRET_KEY — Paystack secret key for signature verification
//   EMAIL_API_KEY — Resend / Mailgun / SendGrid API key
//   EMAIL_FROM — Sender address (e.g. "Menshly Global <hello@menshlyglobal.com>")
//   EMAIL_PROVIDER — "resend" | "mailgun" | "sendgrid" (default: resend)
//   SITE_URL — Base URL of the site (default: https://menshly-global-enz.pages.dev)
//
// KV Namespace binding:
//   PURCHASES — CloudFlare KV namespace for storing purchase records

export default {
  async fetch(request, env) {
    // Only accept POST
    if (request.method !== 'POST') {
      return json({ error: 'Method not allowed' }, 405);
    }

    try {
      // 1. Read raw body for signature verification
      const rawBody = await request.text();
      let payload;

      try {
        payload = JSON.parse(rawBody);
      } catch {
        return json({ error: 'Invalid JSON' }, 400);
      }

      // 2. Verify Paystack signature (async)
      const signatureValid = await verifyPaystackSignatureAsync(rawBody, env.PAYSTACK_SECRET_KEY, request.headers.get('X-Paystack-Signature'));

      if (!signatureValid) {
        console.error('Invalid Paystack signature');
        return json({ error: 'Invalid signature' }, 401);
      }

      // 3. Only process charge.success events
      const event = payload.event;
      if (event !== 'charge.success') {
        return json({ status: 'ignored', event }, 200);
      }

      const data = payload.data;
      const customerEmail = data.customer?.email;
      const amount = data.amount; // in kobo (or cents for USD)
      const currency = data.currency || 'USD';
      const reference = data.reference;
      const metadata = data.metadata || {};
      const productTitle = metadata.product || 'Unknown Playbook';
      const productType = metadata.type || 'playbook';
      const pdfSlug = metadata.pdf_slug || '';
      const source = metadata.source || '';

      if (!customerEmail) {
        return json({ error: 'Missing customer email' }, 400);
      }

      // 4. Check for duplicate processing (idempotency)
      const siteUrl = env.SITE_URL || 'https://menshly-global-enz.pages.dev';

      if (env.PURCHASES) {
        const existing = await env.PURCHASES.get(`ref:${reference}`);
        if (existing) {
          console.log(`Duplicate webhook for reference ${reference}, skipping`);
          return json({ status: 'already_processed', reference }, 200);
        }
      }

      // 5. Build PDF download URL
      const pdfUrl = pdfSlug
        ? `${siteUrl}/pdfs/${pdfSlug}.pdf`
        : `${siteUrl}/pdfs/${productTitle.toLowerCase().replace(/[^a-z0-9]+/g, '-')}.pdf`;

      // 6. Store purchase record in KV
      const purchaseRecord = {
        email: customerEmail,
        product: productTitle,
        type: productType,
        amount: amount,
        currency: currency,
        reference: reference,
        pdfUrl: pdfUrl,
        source: source,
        purchasedAt: new Date().toISOString(),
        emailSent: false,
      };

      if (env.PURCHASES) {
        // Store by reference (for idempotency check)
        await env.PURCHASES.put(`ref:${reference}`, JSON.stringify(purchaseRecord), { expirationTtl: 7776000 }); // 90 days
        // Store by email (for customer lookup)
        const emailKey = `email:${customerEmail}:${reference}`;
        await env.PURCHASES.put(emailKey, JSON.stringify(purchaseRecord), { expirationTtl: 7776000 });
      }

      // 7. Send email with PDF download link
      let emailSent = false;
      if (env.EMAIL_API_KEY) {
        try {
          emailSent = await sendDeliveryEmail(env, {
            to: customerEmail,
            productTitle,
            amount,
            currency,
            reference,
            pdfUrl,
            siteUrl,
          });
        } catch (emailError) {
          console.error('Email sending failed:', emailError.message);
        }
      }

      // Update purchase record with email status
      if (env.PURCHASES && emailSent) {
        purchaseRecord.emailSent = true;
        await env.PURCHASES.put(`ref:${reference}`, JSON.stringify(purchaseRecord), { expirationTtl: 7776000 });
      }

      // 8. Send admin notification via Formspree (always attempt)
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
            reference: reference,
            pdf_url: pdfUrl,
            email_sent: emailSent,
            signature_valid: signatureValid,
          }),
        });
      } catch {}

      return json({
        status: 'processed',
        reference,
        emailSent,
      }, 200);

    } catch (error) {
      console.error('Webhook processing error:', error);
      return json({ error: error.message }, 500);
    }
  },
};

// ─── Paystack Signature Verification (Async) ────────────────────────────────
async function verifyPaystackSignatureAsync(rawBody, secretKey, headerSignature) {
  if (!secretKey || !headerSignature) return false;

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

// ─── Email Sending ────────────────────────────────────────────────────────────
async function sendDeliveryEmail(env, { to, productTitle, amount, currency, reference, pdfUrl, siteUrl }) {
  const provider = env.EMAIL_PROVIDER || 'resend';
  const from = env.EMAIL_FROM || 'Menshly Global <onboarding@resend.dev>';
  const amountDisplay = `${currency} ${(amount / 100).toFixed(2)}`;

  const htmlBody = buildEmailHtml({
    productTitle,
    amountDisplay,
    reference,
    pdfUrl,
    siteUrl,
  });

  const textBody = `MENSHLY GLOBAL — Your Playbook Is Ready\n\nThank you for purchasing ${productTitle}. Your payment of ${amountDisplay} was successful.\n\nDownload your PDF: ${pdfUrl}\n\nReference: ${reference}\n\nIf you have any issues, reply to this email and we'll help you within 24 hours.\n\nMenshly Global — Where AI Meets Revenue`;

  if (provider === 'resend') {
    return await sendViaResend(env.EMAIL_API_KEY, from, to, `Your Playbook: ${productTitle} — Download Ready`, htmlBody, textBody);
  } else if (provider === 'mailgun') {
    return await sendViaMailgun(env.EMAIL_API_KEY, env.MAILGUN_DOMAIN, from, to, `Your Playbook: ${productTitle} — Download Ready`, htmlBody, textBody);
  } else if (provider === 'sendgrid') {
    return await sendViaSendGrid(env.EMAIL_API_KEY, from, to, `Your Playbook: ${productTitle} — Download Ready`, htmlBody, textBody);
  }

  console.error(`Unknown email provider: ${provider}`);
  return false;
}

// ─── Resend ───────────────────────────────────────────────────────────────────
async function sendViaResend(apiKey, from, to, subject, html, text) {
  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ from, to: [to], subject, html, text }),
  });

  if (!res.ok) {
    const err = await res.text();
    console.error('Resend error:', err);
    return false;
  }
  return true;
}

// ─── Mailgun ──────────────────────────────────────────────────────────────────
async function sendViaMailgun(apiKey, domain, from, to, subject, html, text) {
  const res = await fetch(`https://api.mailgun.net/v3/${domain}/messages`, {
    method: 'POST',
    headers: {
      'Authorization': `Basic ${btoa(`api:${apiKey}`)}`,
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
      from,
      to,
      subject,
      html,
      text,
    }),
  });

  if (!res.ok) {
    const err = await res.text();
    console.error('Mailgun error:', err);
    return false;
  }
  return true;
}

// ─── SendGrid ─────────────────────────────────────────────────────────────────
async function sendViaSendGrid(apiKey, from, to, subject, html, text) {
  const [fromName, fromEmail] = parseFromAddress(from);
  const res = await fetch('https://api.sendgrid.com/v3/mail/send', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
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

  if (!res.ok) {
    const err = await res.text();
    console.error('SendGrid error:', err);
    return false;
  }
  return true;
}

function parseFromAddress(from) {
  const match = from.match(/^(.+?)\s*<(.+)>$/);
  if (match) return [match[1].trim(), match[2].trim()];
  return ['Menshly Global', from];
}

// ─── Email HTML Template ──────────────────────────────────────────────────────
function buildEmailHtml({ productTitle, amountDisplay, reference, pdfUrl, siteUrl }) {
  return `<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"></head>
<body style="margin:0;padding:0;background:#111111;">
  <div style="font-family:Inter,-apple-system,BlinkMacSystemFont,sans-serif;max-width:600px;margin:0 auto;background:#1A1A1A;color:#FFFFFF;">
    <!-- Header -->
    <div style="border-bottom:3px solid #F9FF00;padding:24px 32px;">
      <h1 style="font-family:Oswald,Arial Black,sans-serif;color:#F9FF00;font-size:20px;margin:0;letter-spacing:4px;">MENSHLY GLOBAL</h1>
    </div>

    <!-- Body -->
    <div style="padding:32px;">
      <h2 style="font-family:Oswald,Arial Black,sans-serif;font-size:22px;margin:0 0 16px 0;color:#FFFFFF;">YOUR PLAYBOOK IS READY</h2>

      <p style="font-size:16px;line-height:1.6;margin:0 0 16px 0;color:#CCCCCC;">
        Thank you for purchasing <strong style="color:#F9FF00;">${productTitle}</strong>. Your payment of <strong>${amountDisplay}</strong> was successful.
      </p>

      <p style="font-size:16px;line-height:1.6;margin:0 0 24px 0;color:#CCCCCC;">
        Click the button below to download your PDF playbook:
      </p>

      <!-- CTA Button -->
      <div style="text-align:center;margin:28px 0;">
        <a href="${pdfUrl}" style="display:inline-block;background:#F9FF00;color:#1A1A1A;font-family:Oswald,Arial Black,sans-serif;font-weight:700;font-size:18px;padding:16px 44px;text-decoration:none;letter-spacing:2px;border:3px solid #F9FF00;">DOWNLOAD PDF</a>
      </div>

      <!-- Backup Link -->
      <div style="background:#111111;border:1px solid #333333;padding:16px;margin:24px 0;border-radius:0;">
        <p style="font-size:13px;color:#999999;margin:0 0 8px 0;">If the button doesn't work, copy and paste this link into your browser:</p>
        <p style="font-size:13px;color:#F9FF00;margin:0;word-break:break-all;">${pdfUrl}</p>
      </div>

      <!-- Receipt Info -->
      <div style="border-top:1px solid #333333;padding-top:16px;margin-top:24px;">
        <table style="width:100%;font-size:14px;color:#999999;">
          <tr><td style="padding:4px 0;">Reference:</td><td style="text-align:right;color:#CCCCCC;">${reference}</td></tr>
          <tr><td style="padding:4px 0;">Product:</td><td style="text-align:right;color:#CCCCCC;">${productTitle}</td></tr>
          <tr><td style="padding:4px 0;">Amount:</td><td style="text-align:right;color:#CCCCCC;">${amountDisplay}</td></tr>
        </table>
      </div>

      <p style="font-size:14px;color:#666666;margin-top:20px;">If you have any issues downloading your playbook, reply to this email and we'll help you within 24 hours.</p>
    </div>

    <!-- Footer -->
    <div style="border-top:3px solid #F9FF00;padding:20px 32px;">
      <p style="font-size:12px;color:#666666;margin:0;">Menshly Global — Where AI Meets Revenue</p>
      <p style="font-size:11px;color:#444444;margin:8px 0 0 0;">${siteUrl}</p>
    </div>
  </div>
</body>
</html>`;
}

// ─── Helper ───────────────────────────────────────────────────────────────────
function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}
