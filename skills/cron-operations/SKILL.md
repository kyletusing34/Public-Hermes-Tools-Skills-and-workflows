---
name: cron-operations
description: Reusable patterns for Hermes cron job operations. Silence protocol, skill review, job management, output handling, and debugging.
version: 1.1.0
metadata:
  hermes:
    tags: [cron, operations, debugging, silence]
---

# Cron Operations

Patterns for managing and debugging Hermes cron jobs without noisy false alarms.

## Cron silence protocol

When a job should produce no operator-facing output:

1. Decide whether the task found anything actionable. If not, end with `[SILENT]`.
2. Honor the job's `deliver` setting when present. Otherwise keep delivery in the
   current conversation context only.
3. Confirm required toolsets are enabled before the job runs. Missing toolsets
   cause delivery errors that look like "silent failures."
4. Prefer channel delivery or silent completion over appending to a giant global
   cron log for every noop run.

### Debugging silent jobs

If a job keeps returning `[SILENT]` when you expected work:

1. Inspect `enabled_toolsets` and `deliver`
2. Run the job immediately with `action='run'`
3. Confirm the trigger logic still matches current data
4. Check whether the job is attached to a stale session or profile

## Cron skill review

Use during a scheduled skill-review session:

1. `skill_view(name=<skill-name>)`
2. Read linked references/templates/scripts
3. Compare against current tools and docs
4. Patch outdated sections with `skill_manage(action='patch', ...)`
5. Verify the skill loads
6. Report a short structured summary (what changed, what stayed, risks)

### Review checklist

- [ ] SKILL.md matches current tool commands
- [ ] Linked files are current
- [ ] No duplicated content better owned by another skill
- [ ] No session-specific secrets or host paths
- [ ] Skill name still matches scope

## Action queue processing

For cron jobs that drain a work queue:

1. Acquire a claim or lock for the queue resource
2. Process a bounded batch (N items), not the whole infinite backlog
3. Write progress events with counts, not full payloads
4. On partial failure, leave failed items retryable and continue the batch
5. Release the claim and emit one completion summary

## Log hygiene

- Rotate cron logs. Do not let a single file grow without bound.
- Keep per-job output separable when possible.
- Never log secrets, full auth headers, or customer PII.
