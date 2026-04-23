#!/usr/bin/env python3
"""Copy generated articles from output/ to content/posts/.
Verifies each article has an image before copying.
Called by GitHub Actions workflow.
"""
import json
import shutil
import os

manifest_path = "output/manifest.json"
if not os.path.exists(manifest_path):
    print("No manifest file found")
    exit(0)

with open(manifest_path) as f:
    manifest = json.load(f)

if not manifest:
    print("Empty manifest")
    exit(0)

copied = 0
for article in manifest:
    src = article.get("file", "")
    if not src:
        continue
    dst = os.path.join("content/posts", os.path.basename(src))
    if os.path.exists(src):
        with open(src, "r") as f:
            head = f.read(500)
        if "image:" in head:
            shutil.copy2(src, dst)
            print(f"Copied: {src} -> {dst}")
            copied += 1
        else:
            print(f"SKIPPED (no image): {src}")
    else:
        print(f"SKIPPED (file not found): {src}")

print(f"Total copied: {copied}")
