#!/usr/bin/env python3
"""Render a deterministic AI agent readiness report from structured inputs."""

from __future__ import annotations

import argparse
from pathlib import Path


def clamp(score: int) -> int:
    return max(0, min(2, score))


def band(total: int) -> str:
    if total <= 3:
        return "not ready"
    if total <= 7:
        return "partly ready"
    return "operationally usable"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workflow", required=True, help="Workflow or agent being audited.")
    parser.add_argument("--authority", type=int, required=True)
    parser.add_argument("--inputs", type=int, required=True)
    parser.add_argument("--review-gates", type=int, required=True, dest="review_gates")
    parser.add_argument("--proof", type=int, required=True)
    parser.add_argument("--spend-control", type=int, required=True, dest="spend_control")
    parser.add_argument("--control-gap", required=True, help="Biggest missing control.")
    parser.add_argument("--next-workflow", required=True, help="Safest workflow to trust next.")
    parser.add_argument("--recommendation", required=True, help="Recommended next step.")
    parser.add_argument(
        "--risk",
        action="append",
        default=[],
        help="Stop-sign risk. Repeat for multiple items.",
    )
    parser.add_argument("--output", required=True, help="Markdown output path.")
    args = parser.parse_args()

    scores = {
        "Authority": clamp(args.authority),
        "Inputs": clamp(args.inputs),
        "Review gates": clamp(args.review_gates),
        "Proof": clamp(args.proof),
        "Spend control": clamp(args.spend_control),
    }
    total = sum(scores.values())
    score_band = band(total)
    risks = args.risk or ["none noted"]

    lines = [
        "# AI Agent Readiness Report",
        "",
        "## Workflow",
        f"- Name: {args.workflow}",
        "",
        "## Scores",
    ]
    for label, value in scores.items():
        lines.append(f"- {label}: {value}/2")
    lines += [
        f"- Total: {total}/10",
        f"- Band: {score_band}",
        "",
        "## Biggest control gap",
        args.control_gap,
        "",
        "## Stop-sign risks",
    ]
    for risk in risks:
        lines.append(f"- {risk}")
    lines += [
        "",
        "## Safest next workflow",
        args.next_workflow,
        "",
        "## Recommendation",
        args.recommendation,
        "",
    ]

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines))
    print(f"Wrote readiness report -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
