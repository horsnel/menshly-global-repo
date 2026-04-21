/**
 * Cloudflare Pages Function: Promote Article to Homepage
 * Copies an article from content/ai-newsroom/ to content/posts/
 * This makes it appear on the homepage alongside other news articles.
 *
 * Required Cloudflare Environment Variables:
 *   GITHUB_TOKEN   - GitHub PAT with repo write access
 *   GITHUB_REPO    - owner/repo format
 */

export async function onRequestPost(context) {
  try {
    const { slug, target } = await context.request.json();

    if (!slug || !slug.trim()) {
      return jsonResponse({ error: "Article slug is required" }, 400);
    }

    const githubToken = context.env.GITHUB_TOKEN || "";
    const githubRepo = context.env.GITHUB_REPO || "";

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
      "User-Agent": "MenshlyGlobal-Bot",
      "Accept": "application/vnd.github.v3+json"
    };

    // Determine source path — can be ai-newsroom or posts
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

    // 2. Generate a unique filename for the homepage version
    // Add timestamp prefix for posts (matching the generate-news.py pattern)
    var timestamp = Date.now();
    var homepageSlug = timestamp + "-" + slug;
    var targetPath = "content/posts/" + homepageSlug + ".md";

    // Check if this article is already in posts (by checking the original slug in content)
    // Update the slug in front matter to match the new filename
    content = content.replace(
      /^slug:\s*["']?[^"'\n]+["']?\s*$/m,
      'slug: "' + homepageSlug + '"'
    );

    // 3. Create the article in content/posts/
    var createBody = {
      message: "Promote: publish article to homepage - " + slug,
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
      message: "Article promoted to homepage! It will appear on the front page within 1-2 minutes.",
      slug: homepageSlug,
      originalSlug: slug,
      url: "https://menshly-global.pages.dev/posts/" + homepageSlug + "/",
      commitSha: (result.commit && result.commit.sha) ? result.commit.sha.substring(0, 7) : "?"
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
