#!/usr/bin/env python3
"""Refresh CONFIG/FREE_MODELS.md with currently available free LLM models."""

import argparse
import json
import os
import urllib.request
from datetime import datetime, timezone

OUTPUT_PATH = os.environ.get("FREE_MODELS_OUTPUT", "CONFIG/FREE_MODELS.md")
OPENROUTER_URL = "https://openrouter.ai/api/v1/models"
NVIDIA_URL = "https://integrate.api.nvidia.com/v1/models"
USER_AGENT = "ai-operator-baseline-free-model-refresh/1.0"


def fetch_json(url, headers=None):
    req_headers = {"User-Agent": USER_AGENT}
    req_headers.update(headers or {})
    req = urllib.request.Request(url, headers=req_headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def parse_price(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def md(value):
    return str(value or "").replace("|", "\\|").replace("\n", " ").strip()


def get_openrouter_free_models():
    data = fetch_json(OPENROUTER_URL)
    free = []
    for m in data.get("data", []):
        pricing = m.get("pricing", {})
        prompt_price = parse_price(pricing.get("prompt"))
        completion_price = parse_price(pricing.get("completion"))
        if prompt_price == 0 and completion_price == 0:
            free.append(
                {
                    "id": m["id"],
                    "context_length": int(m.get("context_length") or 0),
                    "description": (m.get("description") or "").split("\n")[0][:160],
                }
            )
    return free


def get_nvidia_nim_models(api_key):
    if not api_key:
        return None
    try:
        data = fetch_json(NVIDIA_URL, headers={"Authorization": f"Bearer {api_key}"})
        return [{"id": m["id"]} for m in data.get("data", [])]
    except Exception as e:
        return [{"error": str(e)}]


def suggest_picks(openrouter_free, min_context):
    candidates = [m for m in openrouter_free if (m.get("context_length") or 0) >= min_context]
    return sorted(candidates, key=lambda item: (-item["context_length"], item["id"]))[:5]


def render(openrouter_free, nvidia_models, min_context):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    picks = suggest_picks(openrouter_free, min_context)
    lines = [
        "# Free Model Inventory (auto-generated)",
        "",
        f"**Last refreshed:** {now}",
        f"**Refresh script:** `scripts/update_free_models.py`",
        "",
        "| Model ID | Context | Notes |",
        "|---|---|---|",
    ]
    for m in sorted(openrouter_free, key=lambda x: (-x["context_length"], x["id"])):
        lines.append(f"| `{md(m['id'])}` | {m.get('context_length', '?') or '?'} | {md(m['description'])} |")
    lines += ["", "## NVIDIA NIM catalog", ""]
    if nvidia_models is None:
        lines.append("_Skipped — set `NVIDIA_API_KEY` to include NVIDIA's catalog._")
    elif nvidia_models and "error" in nvidia_models[0]:
        lines.append(f"_Lookup failed: {nvidia_models[0]['error']}_")
    else:
        for m in nvidia_models:
            lines.append(f"- `{md(m['id'])}`")
    lines += ["", "## Suggested Tier 0 pick", ""]
    if picks:
        for item in picks:
            lines.append(f"- `{md(item['id'])}` ({item['context_length']} context)")
    else:
        lines.append(f"No free models met the >= {min_context} context filter during this refresh.")
    lines.append("")
    return "\n".join(lines)


def build_arg_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default=OUTPUT_PATH)
    parser.add_argument("--min-context", type=int, default=32000)
    parser.add_argument("--nvidia-api-key", default=os.environ.get("NVIDIA_API_KEY", ""))
    return parser


def main():
    args = build_arg_parser().parse_args()
    openrouter_free = get_openrouter_free_models()
    nvidia_models = get_nvidia_nim_models(args.nvidia_api_key)
    content = render(openrouter_free, nvidia_models, args.min_context)
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w") as f:
        f.write(content)
    print(f"Wrote {len(openrouter_free)} free OpenRouter models -> {args.output}")


if __name__ == "__main__":
    main()
