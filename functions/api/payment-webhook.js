export async function onRequestPost(context) {
  try {
    const payload = await context.request.json();

    // Log the event for debugging
    console.log('Paystack webhook event:', payload.event);

    if (payload.event === 'charge.success') {
      const data = payload.data;
      console.log('Payment successful:', {
        reference: data.reference,
        amount: data.amount,
        currency: data.currency,
        email: data.customer?.email,
        product: data.metadata?.product || 'Unknown',
        type: data.metadata?.type || 'Unknown'
      });

      // TODO: In production, verify Paystack signature with secret key
      // TODO: Store purchase in KV or external database
      // TODO: Send confirmation email via Resend/SendGrid
      // TODO: Generate and deliver PDF download link
    }

    if (payload.event === 'transfer.success' || payload.event === 'transfer.failed') {
      console.log('Transfer event:', payload.event, payload.data?.reference);
    }

    return new Response(JSON.stringify({ status: 'ok' }), {
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (error) {
    console.error('Webhook error:', error);
    return new Response(JSON.stringify({ error: 'Invalid payload' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}

// GET endpoint for health check
export async function onRequestGet() {
  return new Response(JSON.stringify({
    status: 'active',
    service: 'Menshly Global Payment Webhook',
    version: '1.0.0'
  }), {
    headers: { 'Content-Type': 'application/json' }
  });
}
