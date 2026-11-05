---
name: ai-operator-baseline
description: Use when a user wants to install a real operator baseline into a workspace so an agent gains authority boundaries, review gates, model-tier rules, safety notes, and a scaffolding path instead of vague templates.
---

# AI Operator Baseline

Use this skill to turn a loose agent setup into a structured operator baseline.

## When To Use

Use this skill when the user wants to:
- add operational guardrails to an agent stack
- scaffold baseline config files into a repo or workspace
- define authority, review, proof, and model-spend rules
- create a controlled starting point before a bigger build

## Workflow

1. Inspect the target workspace first.
2. Decide whether the baseline should be created fresh or merged into existing files.
3. Run `scripts/scaffold_operator_baseline.py` when deterministic scaffolding is useful.
4. Replace placeholders with real workspace context.
5. Leave unresolved fields as `[HUMAN_FILL_REQUIRED: item]` instead of guessing.

## What This Skill Installs

The scaffold script creates:
- `CONFIG/AGENT_SYSTEM.md`
- `CONFIG/REVIEW_GATES.md`
- `CONFIG/MODEL_TIERS.md`
- `CONFIG/SECURITY_REVIEW.md`
- `CONFIG/FREE_MODELS.md`
- `scripts/update_free_models.py`

## Merge Rules

- Do not overwrite existing files blindly.
- If the repo already has operator or policy docs, merge the relevant sections instead of duplicating.
- Keep public promises conservative; this baseline improves control, not absolute security.

## References

- Read `references/baseline-files.md` for what each baseline file is supposed to do.
- The actual scaffold templates live in `assets/templates/`.
