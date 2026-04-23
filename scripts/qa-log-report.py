#!/usr/bin/env python3
"""Log QA report from output/qa-report.json to stdout.
Called by the article-qa.yml GitHub Actions workflow.
"""
import json
import sys

try:
    with open("output/qa-report.json") as f:
        r = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Could not read QA report: {e}")
    sys.exit(1)

s = r.get("summary", {})
print(f"Total: {s.get('total', 0)}")
print(f"Pass: {s.get('pass', 0)}")
print(f"Warning: {s.get('warning', 0)}")
print(f"Fail: {s.get('fail', 0)}")

for a in r.get("articles", []):
    status = a.get("status", "?")
    icon = {"PASS": "PASS", "FAIL": "FAIL", "WARNING": "WARN"}.get(status, "?")
    issues = "; ".join(a.get("issues", []))
    warnings = "; ".join(a.get("warnings", []))
    fixes = "; ".join(a.get("fixes_applied", []))
    line = f"[{icon}] {a.get('filename', '?')} - {status}"
    if issues:
        line += f" | Issues: {issues}"
    if warnings:
        line += f" | Warnings: {warnings}"
    if fixes:
        line += f" | Fixes: {fixes}"
    print(line)
