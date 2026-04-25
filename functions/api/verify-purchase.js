// CloudFlare Pages Function: Purchase Verification + Delivery
// GET /api/verify-purchase?token=<token>&slug=<slug>
// Verifies a purchase token against KV and returns delivery info

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Content-Type': 'application/json',
};

export async function onRequestOptions() {
  return new Response(null, { status: 204, headers: CORS_HEADERS });
}

export async function onRequestGet(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const token = url.searchParams.get('token');
  const slug = url.searchParams.get('slug');

  if (!token || !slug) {
    return new Response(JSON.stringify({ error: 'Token and slug are required' }), {
      status: 400,
      headers: CORS_HEADERS,
    });
  }

  if (!env.PURCHASES) {
    return new Response(JSON.stringify({ error: 'Purchase database not configured' }), {
      status: 503,
      headers: CORS_HEADERS,
    });
  }

  try {
    // Look up by token
    const purchaseData = await env.PURCHASES.get(`token:${token}`);
    if (!purchaseData) {
      return new Response(JSON.stringify({ valid: false, error: 'Invalid or expired token' }), {
        headers: CORS_HEADERS,
      });
    }

    const purchase = JSON.parse(purchaseData);

    // Verify slug matches
    const purchaseSlug = purchase.pdf_slug || purchase.product?.toLowerCase().replace(/[^a-z0-9]+/g, '-');
    if (purchaseSlug !== slug) {
      return new Response(JSON.stringify({ valid: false, error: 'Token does not match this product' }), {
        headers: CORS_HEADERS,
      });
    }

    // Check expiration (90 days)
    const purchasedAt = new Date(purchase.purchasedAt);
    const now = new Date();
    const daysSincePurchase = (now - purchasedAt) / (1000 * 60 * 60 * 24);
    if (daysSincePurchase > 90) {
      return new Response(JSON.stringify({ valid: false, error: 'Access expired. Purchase was more than 90 days ago.' }), {
        headers: CORS_HEADERS,
      });
    }

    return new Response(JSON.stringify({
      valid: true,
      product: purchase.product,
      email: purchase.email,
      purchasedAt: purchase.purchasedAt,
      reference: purchase.reference,
      pdfUrl: purchase.pdfUrl,
      daysRemaining: Math.max(0, Math.floor(90 - daysSincePurchase)),
    }), {
      headers: CORS_HEADERS,
    });

  } catch (error) {
    console.error('Verification error:', error);
    return new Response(JSON.stringify({ error: 'Verification failed' }), {
      status: 500,
      headers: CORS_HEADERS,
    });
  }
}
