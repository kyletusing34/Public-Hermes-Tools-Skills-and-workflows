# Readiness Rubric

## Categories

### Authority
- `0`: owner unclear, scope vague, escalation undefined
- `1`: scope partly defined, but exceptions or owner still fuzzy
- `2`: one-sentence mission, named owner, clear escalation boundary

### Inputs
- `0`: workflow relies on guessed values, copied secrets, or memory
- `1`: some verified sources exist, but not all inputs are controlled
- `2`: links, IDs, paths, models, and secrets all come from verified sources

### Review Gates
- `0`: risky actions can happen without human review
- `1`: some review gates exist, but paid, public, or destructive actions are not fully covered
- `2`: review rules are explicit and consistently scoped

### Proof
- `0`: success is inferred from process state, not artifacts
- `1`: some outputs are visible, but proof is incomplete or inconsistent
- `2`: success is tied to a clear artifact and visible finish condition

### Spend Control
- `0`: no default model policy, no escalation rule
- `1`: default model exists, but escalation is informal
- `2`: cheap default, explicit escalation trigger, and approver defined

## Stop-Sign Risks

Any one of these should block expansion:
- public, paid, or production changes can happen without review
- no one can name the artifact that proves the workflow worked
- the workflow still relies on manual secret copying or hidden operator knowledge

## Next-Step Logic

- Missing authority or review gates: recommend `operator baseline`
- Missing proof or artifact path: recommend `workflow cleanup`
- Multi-workflow systems debt: recommend `systems diagnosis`
- Stable controls but missing implementation: recommend `custom build`
