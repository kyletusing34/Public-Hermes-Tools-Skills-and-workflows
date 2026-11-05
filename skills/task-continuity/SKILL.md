---
name: task-continuity
description: Keep multi-agent work alive across sessions with a shared task ledger, short progress logs, and explicit next actions.
version: 1.0.0
metadata:
  hermes:
    tags: [continuity, tasks, logging, handoff]
---

# Task Continuity

Most agent failures are continuity failures. A new session starts cold, redoes
discovery, and loses the blocker.

## Shared ledger pattern

Maintain one shared task record (markdown, SQLite, or Agent Nerve) with:

- `id`
- `owner` (single agent or human)
- `status` (`queued` | `in_progress` | `blocked` | `done` | `spawned`)
- `summary` (what is true now)
- `next_action` (the exact next move)
- `updated_at`

Update the **same** record with deltas. Do not rewrite history as a novel.

## Logging contract

At start, blocked, done, and handoff, write a short log:

```text
agent: hermes
action: short verb phrase
result: delta only
status: in_progress | failed | completed
task_id: optional
```

Rules:

- Log deltas, not transcripts
- Prefer one line of outcome over a pasted stack dump
- If the remote logger is down, mirror locally and queue for later flush

## Session start ritual

Before non-trivial work:

1. Read the shared task ledger
2. Read any generated shared context snapshot
3. Identify server/host if the work is remote
4. Log `in_progress` with the intended action

## Definition of done

A task is done only when:

1. The change or decision exists
2. Verification happened or a blocker is explicit
3. The ledger and logger show completed/blocked/handoff
4. `next_action` is empty or clearly owned by a human

## Pairing

- File ledger: `TASKS.md` style records work well for humans
- Machine ledger: [Agent Nerve](https://github.com/kyletusing34/agent-nerve) for
  tasks, events, and claims across machines
