/**
 * Cloudflare Pages Function: Promote Article to Homepage (with AI Verification)
 * Copies an article from content/ai-newsroom/ to content/posts/
 * Runs content verification and image relevance checks before promoting.
 * Auto-fixes issues when possible.
 *
 * Required Cloudflare Environment Variables:
 *   GITHUB_TOKEN   - GitHub PAT with repo write access
 *   GITHUB_REPO    - owner/repo format
 *   AI_API_KEY     - AI API key for content verification
 *   AI_API_BASE    - API base URL (optional)
 *   PEXELS_API_KEY - Pexels API key for image replacement (optional)
 */

export async function onRequestPost(context) {
  try {
    const { slug, target, skipVerification } = await context.request.json();

    if (!slug || !slug.trim()) {
      return jsonResponse({ error: "Article slug is required" }, 400);
    }

    const githubToken = context.env.GITHUB_TOKEN || "";
    const githubRepo = context.env.GITHUB_REPO || "";
    const apiKey = (context.env.AI_API_KEY || "").replace(/[\u200b-\u200f\u2028-\u202e\ufeff\u00ad]/g, "").trim();
    const apiBase = (context.env.AI_API_BASE || "https://api.cerebras.ai/v1").replace(/\/+$/, "");
    const pexelsKey = context.env.PEXELS_API_KEY || "";

    if (!githubToken) {
      return jsonResponse({ error: "GITHUB_TOKEN not set in Cloudflare env vars.", hint: "Pages > Settings > Environment variables" }, 503);
    }
    if (!githubRepo) {
      return jsonResponse({ error: "GITHUB_REPO not set.", hint: "Format: owner/repo" }, 503);
    }

    var rp = githubRepo.split("/");
    var ab = "https://api.github.com";
    var headers = {
      "Authorization": "Bearer " + githubToken,
      "User-Agent": "Menshlyglobal-Bot",
      "Accept": "application/vnd.github.v3+json"
    };

    // Determine source path
    var sourceDir = target === "posts" ? "content/ai-newsroom" : "content/ai-newsroom";
    var sourcePath = sourceDir + "/" + slug + ".md";

    // 1. Read the source article from GitHub
    var getResp = await fetch(ab + "/repos/" + rp[0] + "/" + rp[1] + "/contents/" + sourcePath, {
      headers: headers
    });

    if (!getResp.ok) {
      if (getResp.status === 404) {
        return jsonResponse({ error: "Article not found: " + sourcePath }, 404);
      }
      var errText = await getResp.text();
      var errMsg = "GitHub API error " + getResp.status;
      try { errMsg = JSON.parse(errText).message || errMsg; } catch(e) {}
      return jsonResponse({ error: "Failed to read article: " + errMsg }, 500);
    }

    var sourceData = await getResp.json();
    var content = decodeURIComponent(escape(atob(sourceData.content)));

    // ═══════════════════════════════════════════════
    // 2. CONTENT VERIFICATION (AI-powered)
    // ═══════════════════════════════════════════════
    var verificationResult = {
      passed: true,
      checks: [],
      warnings: [],
      fixes: []
    };

    if (!skipVerification) {
      // A. Parse front matter
      var fmMatch = content.match(/^---\n([\s\S]*?)\n---/);
      var fmText = fmMatch ? fmMatch[1] : "";
      var bodyText = content.substring(content.indexOf("---", 4) + 3).trim();

      // B. Check for ripped content patterns
      var rippedPatterns = [
        /<div\s+class="cnn-header"/i,
        /OFFICIAL DISPATCH/i,
        /TECH DISPATCH/i,
        /LIVE DISPATCH/i,
        /<img\s+src=/i,
        /<iframe/i,
        /<figure>/i,
        /@Olhmescraxes1/i
      ];
      for (var p = 0; p < rippedPatterns.length; p++) {
        if (rippedPatterns[p].test(bodyText)) {
          verificationResult.warnings.push("Ripped content pattern detected: " + rippedPatterns[p].source);
          // Auto-fix: strip HTML artifacts from body
          bodyText = bodyText.replace(/<div[^>]*>[\s\S]*?<\/div>/gi, "");
          bodyText = bodyText.replace(/<img[^>]*>/gi, "");
          bodyText = bodyText.replace(/<iframe[^>]*>[\s\S]*?<\/iframe>/gi, "");
          bodyText = bodyText.replace(/<figure[^>]*>[\s\S]*?<\/figure>/gi, "");
          bodyText = bodyText.replace(/<script[^>]*>[\s\S]*?<\/script>/gi, "");
          verificationResult.fixes.push("Stripped HTML artifacts from article body");
          break;
        }
      }

      // C. Check essential front matter fields
      if (!/categories?\s*:/.test(fmText)) {
        verificationResult.warnings.push("Missing categories in front matter");
        fmText += '\ncategories: ["world"]';
        verificationResult.fixes.push("Added default category: world");
      }
      if (!/author\s*:/.test(fmText)) {
        verificationResult.warnings.push("Missing author in front matter");
        fmText += '\nauthor: "Menshlyglobal Editorials"';
        verificationResult.fixes.push("Added author: Menshlyglobal Editorials");
      } else {
        fmText = fmText.replace(/^author\s*:.*$/m, 'author: "Menshlyglobal Editorials"');
        verificationResult.fixes.push("Standardized author to Menshlyglobal Editorials");
      }
      if (!/description\s*:/.test(fmText)) {
        verificationResult.warnings.push("Missing description in front matter");
        // Extract first line of body as description
        var firstLine = bodyText.replace(/<[^>]+>/g, "").trim().substring(0, 160);
        fmText += '\ndescription: "' + firstLine.replace(/"/g, "'") + '"';
        verificationResult.fixes.push("Added description from article body");
      }

      // D. Check image URL quality
      var imageMatch = fmText.match(/^image\s*:\s*["']?(.+?)["']?\s*$/m);
      var imageUrl = imageMatch ? imageMatch[1] : "";

      if (!imageUrl) {
        verificationResult.warnings.push("No image in front matter");
        // Try to find a relevant image from Pexels
        if (pexelsKey) {
          var titleMatch = fmText.match(/^title\s*:\s*["']?(.+?)["']?\s*$/m);
          var searchQ = titleMatch ? titleMatch[1].split(/\s+/).filter(function(w) { return w.length > 3; }).slice(0, 4).join(" ") : "news";
          try {
            var imgResp = await fetch("https://api.pexels.com/v1/search?query=" + encodeURIComponent(searchQ) + "&per_page=3&orientation=landscape", {
              headers: { "Authorization": pexelsKey }
            });
            if (imgResp.ok) {
              var imgData = await imgResp.json();
              if (imgData.photos && imgData.photos.length > 0) {
                imageUrl = imgData.photos[0].src.large;
                fmText += '\nimage: "' + imageUrl + '"';
                verificationResult.fixes.push("Added relevant image from Pexels");
              }
            }
          } catch(e) {
            verificationResult.warnings.push("Failed to fetch replacement image: " + e.message);
          }
        }
      } else if (apiKey) {
        // Check if image is from a news/external source (ripped) vs stock photo
        var rippedImageSources = ["bwbx.io", "moneycontrol", "ctfassets", "seekingalpha", "cnet", "jpnn.com", "bloomberg", "reuters", "apnews"];
        var isRippedImage = rippedImageSources.some(function(src) { return imageUrl.toLowerCase().includes(src); });

        if (isRippedImage) {
          verificationResult.warnings.push("Image appears to be from external news source (possibly ripped): " + imageUrl.substring(0, 60) + "...");
          // Try to replace with stock photo
          if (pexelsKey) {
            var titleMatch2 = fmText.match(/^title\s*:\s*["']?(.+?)["']?\s*$/m);
            var searchQ2 = titleMatch2 ? titleMatch2[1].split(/\s+/).filter(function(w) { return w.length > 3; }).slice(0, 4).join(" ") : "news";
            try {
              var imgResp2 = await fetch("https://api.pexels.com/v1/search?query=" + encodeURIComponent(searchQ2) + "&per_page=3&orientation=landscape", {
                headers: { "Authorization": pexelsKey }
              });
              if (imgResp2.ok) {
                var imgData2 = await imgResp2.json();
                if (imgData2.photos && imgData2.photos.length > 0) {
                  var newImageUrl = imgData2.photos[0].src.large;
                  fmText = fmText.replace(/^image\s*:\s*["']?.+?["']?\s*$/m, 'image: "' + newImageUrl + '"');
                  verificationResult.fixes.push("Replaced ripped image with stock photo from Pexels");
                }
              }
            } catch(e) {
              verificationResult.warnings.push("Failed to replace ripped image: " + e.message);
            }
          }
        }
      }

      // E. AI Content Quality Check (if API key available)
      if (apiKey) {
        try {
          var titleForAI = fmText.match(/^title\s*:\s*["']?(.+?)["']?\s*$/m);
          var descForAI = fmText.match(/^description\s*:\s*["']?(.+?)["']?\s*$/m);
          var cleanBody = bodyText.replace(/<[^>]+>/g, "").trim().substring(0, 1500);

          var aiCheckResp = await fetch(apiBase + "/chat/completions", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "Authorization": "Bearer " + apiKey
            },
            body: JSON.stringify({
              model: "llama-3.3-70b",
              messages: [
                {
                  role: "system",
                  content: "You are a content verification AI for Menshlyglobal Editorials. Analyze the article and respond with ONLY a JSON object: {\"verdict\":\"PASS\"|\"FAIL\"|\"WARNING\",\"reason\":\"brief explanation\",\"content_type\":\"ORIGINAL\"|\"RIPPED\"|\"MISINFORMATION\"|\"LOW_QUALITY\",\"confidence\":0-100}. A PASS means the article is legitimate analysis/opinion. FAIL means it's ripped content, misinformation, or extremely low quality. WARNING means borderline."
                },
                {
                  role: "user",
                  content: "Title: " + (titleForAI ? titleForAI[1] : "Unknown") + "\nDescription: " + (descForAI ? descForAI[1] : "N/A") + "\n\nBody (excerpt):\n" + cleanBody
                }
              ],
              max_tokens: 200,
              temperature: 0.3
            })
          });

          if (aiCheckResp.ok) {
            var aiData = await aiCheckResp.json();
            var aiContent = aiData.choices && aiData.choices[0] && aiData.choices[0].message && aiData.choices[0].message.content || "";
            // Try to parse AI response
            var jsonMatch = aiContent.match(/\{[\s\S]*\}/);
            if (jsonMatch) {
              var aiVerdict = JSON.parse(jsonMatch[0]);
              verificationResult.checks.push({
                check: "AI Content Verification",
                verdict: aiVerdict.verdict || "UNKNOWN",
                reason: aiVerdict.reason || "No reason provided",
                content_type: aiVerdict.content_type || "UNKNOWN",
                confidence: aiVerdict.confidence || 0
              });

              if (aiVerdict.verdict === "FAIL") {
                verificationResult.passed = false;
                verificationResult.warnings.push("AI verification FAILED: " + aiVerdict.reason);
              } else if (aiVerdict.verdict === "WARNING") {
                verificationResult.warnings.push("AI verification WARNING: " + aiVerdict.reason);
              }
            }
          }
        } catch(e) {
          verificationResult.warnings.push("AI verification unavailable: " + e.message);
        }
      }

      // F. Reconstruct content with fixes
      content = "---\n" + fmText + "\n---\n\n" + bodyText;

      // G. If verification failed, don't promote
      if (!verificationResult.passed) {
        return jsonResponse({
          success: false,
          error: "Article failed content verification and cannot be promoted to homepage.",
          verification: verificationResult,
          suggestion: "Edit the article to fix the issues, then try promoting again."
        }, 400);
      }
    }

    // 3. Generate a unique filename for the homepage version
    var timestamp = Date.now();
    var homepageSlug = timestamp + "-" + slug;
    var targetPath = "content/posts/" + homepageSlug + ".md";

    // Update the slug in front matter
    content = content.replace(
      /^slug:\s*["']?[^"'\n]+["']?\s*$/m,
      'slug: "' + homepageSlug + '"'
    );

    // 4. Create the article in content/posts/
    var createBody = {
      message: "Promote: AI-verified article to homepage - " + slug,
      content: btoa(unescape(encodeURIComponent(content)))
    };

    // Check if target already exists
    var checkResp = await fetch(ab + "/repos/" + rp[0] + "/" + rp[1] + "/contents/" + targetPath, {
      headers: headers
    });
    if (checkResp.ok) {
      var existingData = await checkResp.json();
      createBody.sha = existingData.sha;
      createBody.message = "Promote: update homepage article - " + slug;
    }

    var putResp = await fetch(ab + "/repos/" + rp[0] + "/" + rp[1] + "/contents/" + targetPath, {
      method: "PUT",
      headers: Object.assign({}, headers, { "Content-Type": "application/json" }),
      body: JSON.stringify(createBody)
    });

    if (!putResp.ok) {
      var putErrText = await putResp.text();
      var putErrMsg = "GitHub API error " + putResp.status;
      try { putErrMsg = JSON.parse(putErrText).message || putErrMsg; } catch(e) {}
      return jsonResponse({ error: "Failed to promote article: " + putErrMsg }, 500);
    }

    var result = await putResp.json();

    return jsonResponse({
      success: true,
      message: "Article promoted to homepage after AI verification! It will appear on the front page within 1-2 minutes.",
      slug: homepageSlug,
      originalSlug: slug,
      url: "https://menshly-global.pages.dev/posts/" + homepageSlug + "/",
      commitSha: (result.commit && result.commit.sha) ? result.commit.sha.substring(0, 7) : "?",
      verification: verificationResult
    });

  } catch (err) {
    return jsonResponse({ error: "Promote failed: " + (err.message || "Unknown error") }, 500);
  }
}

export async function onRequestOptions() {
  return new Response(null, {
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type"
    }
  });
}

function jsonResponse(data, status) {
  return new Response(JSON.stringify(data), {
    status: status || 200,
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*"
    }
  });
}
