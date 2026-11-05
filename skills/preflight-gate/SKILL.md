---
name: preflight-gate
description: Run a freshness-checked preflight before infra actions like pull, deploy, restart, or bootstrap. Stop and escalate when gates fail.
version: 1.0.0
metadata:
  hermes:
    tags: [preflight, infra, safety, deploy]
---

# Preflight Gate

Never guess machine state. Read a preflight result first.

## When required

Before:

- `git pull` / rebase / merge on a managed host
- scripted bootstrap or deploy
- service restart on shared infra
- cron edits that touch production paths

## Freshness window

Treat preflight as stale after 15 minutes. If missing or stale, refresh it before acting.

## Gate table

| Condition | Allowed action |
|-----------|----------------|
| `bootstrap_ready=true` | Proceed |
| `safe_pull=false` | Do not pull. Surface recovery options |
| `script_found=false` | Do not run the script. Stop |
| `bootstrap_ready=false` | Escalate. Present options. Never invent a path |

## Operator output when blocked

```text
gate_failed:
reason:
recommended_recovery:
options:
owner: human
```

## Rule

If any required gate is false, log failed/blocked and stop. Do not retry the infra action until a human chooses a recovery option.
