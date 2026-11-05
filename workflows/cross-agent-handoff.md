# Workflow: Cross-Agent Handoff

Use whenever work moves between Hermes, Claude Code, Codex, or a human.

## Packet

Copy and fill:

```text
task_id:
from_owner:
to_owner:
summary:
already_done:
next_action:
claims_held:
blockers:
verify_with:
rollback:
```

## Sequence

1. Update the shared ledger owner and status to `in_progress` for the receiver
   (or `blocked` if waiting on a human)
2. Emit a `handoff` event in Agent Nerve (or append the packet to the ledger)
3. Release claims the receiver should not inherit, or document claims they must keep
4. Stop working the task in the sender session

## Receiver first moves

1. Read the packet and recent events
2. Re-verify the claimed state with one cheap check
3. Continue from `next_action`, do not restart discovery unless verification fails
