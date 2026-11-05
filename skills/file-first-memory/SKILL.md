---
name: file-first-memory
description: Audit agent memory, remove low-value chat residue, and keep durable knowledge in files agents can re-read.
version: 1.0.0
metadata:
  hermes:
    tags: [memory, files, maintenance, context]
---

# File-First Memory

Chat memory is for preferences and behavioral rules. Durable procedures belong
in files.

## When to run

- Memory usage is high or climbing
- The same facts exist in both memory and files
- Before a long session that needs headroom
- After a burst of one-off ops work

## Keep vs remove

Keep in memory:

- Voice and behavior rules
- Stable user preferences
- Workflow logic not yet written to a file

Remove from memory:

- Duplicates of file-backed docs
- One-time "I created X" confirmations
- Stale status lines about systems that have a runbook
- Intermediate steps no longer needed

## Procedure

1. List memory entries
2. Flag low-value items against the keep/remove rules
3. Move any still-useful procedure into a dated file under your docs/runbooks tree
4. Remove the memory residue
5. Write a short changelog entry of what moved and what was deleted

## File layout suggestion

```text
docs/
  runbooks/
  decisions/
  handoffs/
TASKS.md          # active ledger only
```

## Rule of thumb

If another agent on another machine needs it tomorrow, put it in a file or in
Agent Nerve. Do not trust a single session's memory store.
