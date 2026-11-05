---
name: subagent-autotrigger
description: Reusable pattern for keyword-triggered specialist subagents with bounded iterations and cost-aware model tiers.
version: 1.0.0
metadata:
  hermes:
    tags: [subagent, routing, triggers, specialization]
---

# Specialized Subagent Auto-Trigger

Create specialists that activate on clear task shapes instead of forcing one
generalist to do everything.

## Three parts

1. **Skill** — domain knowledge and constraints
2. **Dispatcher** — detects triggers and spawns the specialist
3. **Middleware** — hooks the dispatcher into the main agent loop

## Trigger design

Use specific phrases, not vague nouns:

```python
TRIGGERS = [
    r"\b(build|create|scaffold)\s+(landing page|marketing site)\b",
    r"\b(audit|review)\s+(cron|scheduled jobs?)\b",
]
```

Bad triggers: `help`, `fix`, `website` alone.

## Spawn rules

- Cap iterations (`--max-iterations`)
- Prefer a cheaper model tier for narrow execution
- Pass only the needed skill and toolset
- Return a structured result (`success`, `summary`, `next_action`, `error`)
- Time out rather than hang forever

## Example spawn shape

```bash
hermes agent \
  --skill operations/cron-operations \
  --max-iterations 40 \
  --model tier2 \
  "Audit cron silence failures and propose patches"
```

## Safety

- Never auto-trigger destructive actions (deploy, DNS, send, delete) without an
  approval gate
- Log the trigger match and chosen specialist for auditability
- If no specialist matches, fall back to the main agent or ask the operator
