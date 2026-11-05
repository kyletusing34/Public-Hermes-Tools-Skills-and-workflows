---
name: mixed-agent-handoff
description: Ownership and handoff rules for fleets that mix Hermes workers with Claude Code, Codex, and a human operator.
version: 1.0.0
metadata:
  hermes:
    tags: [handoff, multi-agent, routing, ownership]
---

# Mixed Agent Handoff

## Default roles

| Role | Owns |
|------|------|
| Hermes / local worker | Bulk generation, long loops, cheap inference, queue draining |
| Claude Code / Codex | File/code orchestration, risky edits, verification |
| Human | Secrets, destructive changes, paid actions, strategy locks |

One owner at a time. Handoffs must update owner in the shared ledger.

## When to hand off

Hand off when:

- The next step needs a different tool budget or model tier
- The current agent hit a loop cap
- The work needs human approval (deploy, DNS, billing, outbound send)
- Another agent already holds a claim on the target resource

## Handoff packet (minimum)

```text
task_id:
from_owner:
to_owner:
summary: what is true now
done: what already landed
next_action: exact next step
claims: resources still held
blockers: none | specific external wait
verify: how the receiver should check progress
```

Emit this as an Agent Nerve `handoff` event or append it to the shared ledger.

## Anti-patterns

- "Continuing in chat" without updating owner/status
- Re-discovering a repo the previous agent already mapped
- Holding a claim after the handoff without documenting it
- Asking the human vague questions when a concrete approval ask would unblock

## Routing preference

1. Prefer local/cheap workers for bulk and repetitive work
2. Escalate to Claude/Codex for orchestration and delicate patches
3. Escalate to human only with a specific decision and options
