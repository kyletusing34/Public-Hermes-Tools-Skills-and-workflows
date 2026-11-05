# Workflow: Daily Ops Loop

A short morning loop for an operator running Hermes plus coding agents.

## Steps

1. **Health**
   - Gateway/services up?
   - Disk and queue depth acceptable?
2. **Ledger**
   - Read shared `TASKS` / Agent Nerve namespaces
   - Pick the highest-leverage blocked or in-progress item
3. **Cron residue**
   - Scan overnight cron for unexpected non-`[SILENT]` noise
   - File one bug or patch task for any recurring failure
4. **Execute one slice**
   - Claim the resource
   - Do the next action only
   - Log progress
5. **Handoff or close**
   - Update owner/status/`next_action`
   - Release claims you no longer need

## Done when

You either cleared one blocker or left a crisp handoff packet for another agent.
