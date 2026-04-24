#!/usr/bin/env node
/**
 * AI Bridge - Node.js bridge for Python generators to call z-ai-web-dev-sdk.
 *
 * Usage:
 *   node scripts/ai-bridge.js --prompt "Your prompt here" --system "System prompt" --max-tokens 8000 --temperature 0.7
 *   node scripts/ai-bridge.js --input-file /tmp/prompt.json
 *
 * Reads a JSON payload, calls the AI, and writes the response to stdout.
 * Returns OpenAI-compatible JSON format.
 */

const fs = require('fs');
const path = require('path');

function findSDK() {
  const paths = [
    path.join(process.cwd(), 'node_modules', 'z-ai-web-dev-sdk'),
    '/home/z/.bun/install/global/node_modules/z-ai-web-dev-sdk',
  ];
  for (const p of paths) {
    try {
      const mod = require(p);
      return mod.default || mod;
    } catch (e) {
      continue;
    }
  }
  throw new Error('z-ai-web-dev-sdk not found');
}

async function main() {
  const args = process.argv.slice(2);

  let messages = [];
  let maxTokens = 4096;
  let temperature = 0.7;

  // Parse args
  let i = 0;
  while (i < args.length) {
    switch (args[i]) {
      case '--input-file': {
        const filePath = args[++i];
        const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
        messages = data.messages || [];
        maxTokens = data.max_tokens || 4096;
        temperature = data.temperature || 0.7;
        break;
      }
      case '--prompt': {
        const prompt = args[++i];
        messages.push({ role: 'user', content: prompt });
        break;
      }
      case '--system': {
        const system = args[++i];
        messages.unshift({ role: 'system', content: system });
        break;
      }
      case '--max-tokens': {
        maxTokens = parseInt(args[++i], 10);
        break;
      }
      case '--temperature': {
        temperature = parseFloat(args[++i]);
        break;
      }
      case '--messages': {
        // Read messages from a JSON string
        messages = JSON.parse(args[++i]);
        break;
      }
    }
    i++;
  }

  if (messages.length === 0) {
    console.error('Error: No messages provided');
    process.exit(1);
  }

  const ZAI = findSDK();
  const zai = await ZAI.create();

  const completion = await zai.chat.completions.create({
    messages,
    max_tokens: maxTokens,
    temperature,
  });

  // Output OpenAI-compatible JSON
  const result = {
    id: completion.id || `chatcmpl-${Date.now()}`,
    object: 'chat.completion',
    created: Math.floor(Date.now() / 1000),
    model: completion.model || 'z-ai',
    choices: (completion.choices || []).map(choice => ({
      index: choice.index || 0,
      message: {
        role: (choice.message && choice.message.role) || 'assistant',
        content: (choice.message && choice.message.content) || '',
      },
      finish_reason: choice.finish_reason || 'stop',
    })),
    usage: completion.usage || { prompt_tokens: 0, completion_tokens: 0, total_tokens: 0 },
  };

  console.log(JSON.stringify(result));
}

main().catch(err => {
  console.error('Error:', err.message);
  process.exit(1);
});
