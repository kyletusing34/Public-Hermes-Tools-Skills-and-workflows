---
name: loop-cap-escalation
description: Bound agent refinement loops and escalate with a packaged handoff instead of burning tokens forever.
version: 1.0.0
metadata:
  hermes:
    tags: [loops, escalation, qa, cost]
---

# Loop Cap Escalation

Cheap local loops are useful. Infinite retries are not.

## Defaults

| Role | Cap |
|------|-----|
| Mobile / triage assistant | 2 refinement iterations |
| Coding orchestrator | 5 orchestration iterations |
| Local worker / Hermes | 5 QA iterations |

Override only with explicit operator approval.

## Loop shape

1. Execute
2. Judge against explicit exit criteria
3. Retry with enriched failure context
4. Stop at cap and escalate

## Escalation packet

When the cap is hit, package:

```text
task_id:
objective:
attempts:
best_result_summary:
failure_modes:
artifacts:
recommended_owner:
next_action:
```

Do not make the upstream agent rediscover the whole problem.

## Anti-patterns

- Retrying the exact same prompt without new evidence
- Raising the cap silently
- Escalating to a human with "it failed" and no options
