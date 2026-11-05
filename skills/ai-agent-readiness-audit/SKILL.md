---
name: ai-agent-readiness-audit
description: Use when a user wants to audit one AI agent or one workflow for operational readiness, score authority and review controls, identify the biggest control gap, and produce a concrete next-step decision instead of vague advice.
---

# AI Agent Readiness Audit

Use this skill to evaluate one live or proposed agent workflow at a time.

## When To Use

Use this skill when the user wants to:
- check whether an agent is ready for real work
- score one workflow before expanding automation
- find the first missing control that makes the stack unsafe or sloppy
- produce a clean readiness report with a recommendation

Do not use this skill for broad architecture design across many systems at once. Narrow the audit to one agent or one workflow first.

## Workflow

1. Identify the exact workflow being audited.
2. Gather evidence for five categories:
   authority, inputs, review_gates, proof, spend_control
3. Score each category from `0` to `2`.
4. Name the biggest control gap and the safest workflow this stack should own next.
5. Produce a readiness report with:
   total score
   readiness band
   stop-sign risks
   next-step recommendation

## Output Standard

Every audit should include:
- workflow name
- category scores
- total score out of 10
- readiness band
- biggest control gap
- safest next workflow
- recommended next step

Use `scripts/render_readiness_report.py` when a deterministic markdown report is useful.

## Decision Rules

- `0-3`: not ready
- `4-7`: partly ready
- `8-10`: operationally usable for one supervised internal workflow

If any of these are true, treat the workflow as not ready even if the numeric score looks acceptable:
- it can publish, spend, or change production without review
- nobody can point to the artifact that proves success
- the workflow still depends on guessed paths, copied secrets, or hidden prompts

## References

- Read `references/readiness-rubric.md` for the scoring rubric and stop-sign rules.
- Read `references/report-template.md` when you need a clean markdown audit structure.
