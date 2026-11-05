# Workflow: Overnight Batch Guardrails

Use before arming a long overnight Hermes/local-model batch.

## Preflight

- [ ] Input corpus path exists and is writable only where expected
- [ ] Resume/overwrite behavior is explicit
- [ ] Kill switch script exists and is tested
- [ ] Log path is rotated or capped
- [ ] Model/service health checked once
- [ ] Expected runtime and cost ceiling written down

## Runtime rules

1. Process bounded batches, not unbounded streams
2. Persist progress after each successful unit
3. On judge/model failure, skip or retry with a hard cap
4. Never require a human mid-batch unless the kill switch was hit

## Morning after

```text
units_attempted:
units_shipped:
skipped:
failures:
resume_from:
kill_switch_used: yes|no
```

Create follow-up tasks for systemic failures. Do not silently re-arm a broken batch.
