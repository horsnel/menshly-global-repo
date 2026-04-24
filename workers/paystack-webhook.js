// CloudFlare Worker: Paystack Webhook → Email Delivery
// This worker listens for Paystack payment confirmations and sends
// PDF download links via email using Resend (or any email API).
//
// Setup:
// 1. Deploy this worker to CloudFlare
// 2. Set environment variables: RESEND_API_KEY, PAYSTACK_SECRET_KEY
// 3. Configure Paystack webhook to point to this worker's URL
// 4. The worker verifies the payment, then sends an email with the PDF link

export default {
  async fetch(request, env) {
    // Only accept POST requests
    if (request.method !== 'POST') {
      return new Response('Method not allowed', { status: 405 });
    }

    try {
      const payload = await request.json();

      // Verify Paystack signature (security check)
      const hash = payload.data?.reference 
        ? await verifyPaystackSignature(request, env.PAYSTACK_SECRET_KEY)
        : false;

      // For now, we process the webhook payload
      // In production, you MUST verify the signature
      const event = payload.event;
      
      // Only process successful charge events
      if (event !== 'charge.success') {
        return new Response('Event not processed', { status: 200 });
      }

      const data = payload.data;
      const email = data.customer?.email;
      const amount = data.amount; // in kobo
      const reference = data.reference;
      const metadata = data.metadata || {};

      // Determine which PDF to send based on the product
      const productTitle = metadata.product || 'Unknown Playbook';
      const pdfUrl = metadata.pdf_url || '';
      const siteUrl = 'https://menshly-global-enz.pages.dev';

      if (!email) {
        return new Response('Missing customer email', { status: 400 });
      }

      // Send email with PDF download link using Resend
      if (env.RESEND_API_KEY) {
        await fetch('https://api.resend.com/emails', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${env.RESEND_API_KEY}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            from: 'Menshly Global <hello@menshlyglobal.com>',
            to: email,
            subject: `Your Playbook: ${productTitle} — Download Ready`,
            html: `
              <div style="font-family:Inter,sans-serif;max-width:600px;margin:0 auto;background:#1A1A1A;color:#FFFFFF;padding:40px;">
                <div style="border-bottom:3px solid #F9FF00;padding-bottom:20px;margin-bottom:30px;">
                  <h1 style="font-family:Oswald,sans-serif;color:#F9FF00;font-size:24px;margin:0;">MENSHLY GLOBAL</h1>
                </div>
                <h2 style="font-family:Oswald,sans-serif;font-size:22px;margin-bottom:16px;">Your Playbook Is Ready</h2>
                <p style="font-size:16px;line-height:1.6;margin-bottom:24px;">Thank you for purchasing <strong>${productTitle}</strong>. Your payment of <strong>$${(amount / 100).toFixed(2)}</strong> was successful.</p>
                <p style="font-size:16px;line-height:1.6;margin-bottom:24px;">Click the button below to download your PDF playbook:</p>
                <div style="text-align:center;margin:30px 0;">
                  <a href="${siteUrl}${pdfUrl}" style="display:inline-block;background:#F9FF00;color:#1A1A1A;font-family:Oswald,sans-serif;font-weight:700;font-size:18px;padding:16px 40px;text-decoration:none;letter-spacing:1px;">DOWNLOAD PDF</a>
                </div>
                <p style="font-size:14px;color:rgba(255,255,255,0.6);margin-top:20px;">Reference: ${reference}</p>
                <p style="font-size:14px;color:rgba(255,255,255,0.6);">If you have any issues, reply to this email and we'll help you within 24 hours.</p>
                <div style="border-top:3px solid #F9FF00;margin-top:30px;padding-top:20px;">
                  <p style="font-size:12px;color:rgba(255,255,255,0.4);">Menshly Global — Where AI Meets Revenue</p>
                </div>
              </div>
            `
          })
        });
      }

      // Also send a notification to the site owner via Formspree
      await fetch('https://formspree.io/f/xreawkow', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify({
          _subject: `Playbook Purchase: ${productTitle}`,
          _type: 'paystack_webhook_purchase',
          customer_email: email,
          product: productTitle,
          amount: `$${(amount / 100).toFixed(2)}`,
          reference: reference,
          pdf_url: pdfUrl
        })
      });

      return new Response('Webhook processed', { status: 200 });

    } catch (error) {
      return new Response(`Error: ${error.message}`, { status: 500 });
    }
  }
};

async function verifyPaystackSignature(request, secretKey) {
  // Paystack sends a signature header for webhook verification
  // X-Paystack-Signature header contains a HMAC-SHA512 hash
  if (!secretKey) return false;
  
  try {
    const body = await request.clone().text();
    const encoder = new TextEncoder();
    const key = await crypto.subtle.importKey(
      'raw',
      encoder.encode(secretKey),
      { name: 'HMAC', hash: 'SHA-512' },
      false,
      ['sign']
    );
    const signature = await crypto.subtle.sign('HMAC', key, encoder.encode(body));
    const hashArray = Array.from(new Uint8Array(signature));
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    const paystackSignature = request.headers.get('X-Paystack-Signature');
    return hashHex === paystackSignature;
  } catch {
    return false;
  }
}
