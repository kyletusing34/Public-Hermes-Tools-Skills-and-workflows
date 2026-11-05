# Workflow: Cron Health Review

Use weekly or after a burst of new scheduled jobs.

## Checklist

- [ ] Every job has an owner and a purpose line
- [ ] Noop paths end with `[SILENT]` when appropriate
- [ ] Required toolsets are explicit
- [ ] Delivery target is intentional (channel vs conversation vs none)
- [ ] Failures page a human or create a task (not silent forever)
- [ ] Logs rotate
- [ ] Secrets are referenced by name, not inlined in the cron prompt

## Output

Write a short report:

```text
jobs_reviewed:
noisy:
silent_but_suspicious:
missing_toolsets:
actions:
```

Create follow-up tasks instead of patching everything in one unbounded session.
