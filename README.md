# Public Hermes Tools, Skills, and Workflows

Battle-tested operator patterns for [Hermes Agent](https://github.com/NousResearch/hermes-agent) fleets.

This repo is a **public-safe** extract of patterns we use daily to run mixed
agent stacks (Hermes workers, Claude Code, Codex, local models). It is not a
dump of a private workstation. Secrets, client data, personal memories, channel
IDs, and machine-specific paths stay out.

Homepage context: [ai.kyletusing.com](https://ai.kyletusing.com)

## What you get

| Area | Contents |
|------|----------|
| Skills | Drop-in `SKILL.md` packages for Hermes skill trees |
| Workflows | Repeatable operator loops (cron health, handoffs, skill review) |
| Tools | Install helper + public-safety scanner before you publish anything |
| Examples | Operator baseline sample + readiness report sample |

## Quick install

```bash
git clone https://github.com/kyletusing34/Public-Hermes-Tools-Skills-and-workflows.git
cd Public-Hermes-Tools-Skills-and-workflows
./tools/install_skills.sh ~/.hermes/skills
```

Or copy one skill at a time:

```bash
mkdir -p ~/.hermes/skills/operations
cp -R skills/cron-operations ~/.hermes/skills/operations/
```

See `docs/INSTALL.md` for profile notes and Agent Nerve wiring.

## Skills included

### Operator foundation
- `ai-operator-baseline` — sane CONFIG templates, model tiers, review gates
- `ai-agent-readiness-audit` — score a business or stack before automation spend

### Daily operations (upgraded from live use)
- `cron-operations` — silence protocol, skill review cron, job debugging
- `task-continuity` — shared task ledger + progress logging across sessions
- `mixed-agent-handoff` — Claude Code / Codex / Hermes ownership rules
- `file-first-memory` — keep durable knowledge in files, not chat memory bloat
- `verified-registry` — JSON registries so agents stop inventing endpoints
- `subagent-autotrigger` — keyword-triggered specialist spawn pattern
- `public-safety-audit` — scan skills/workflows before publishing
- `github-pr-workflow` — branch, verify, push, open PR without leaking tokens

## Workflows included

- `workflows/daily-ops-loop.md`
- `workflows/cron-health-review.md`
- `workflows/cross-agent-handoff.md`
- `workflows/skill-review-cycle.md`

## Pair with Agent Nerve

For durable cross-agent task state, claims, and event history, use:

[github.com/kyletusing34/agent-nerve](https://github.com/kyletusing34/agent-nerve)

Hermes skills here tell agents *how* to operate. Agent Nerve is where they
*write* shared operational memory.

## Public safety rules

Before adding anything to this repo:

1. Run `python3 tools/public_safety_scan.py .`
2. Replace real hosts, tokens, client names, and absolute home paths with placeholders
3. Prefer short operational summaries over full logs or diffs
4. Never commit `.env`, auth JSON, session DBs, or private memories

Details: `docs/PUBLIC_SAFETY.md`

## Versioning

See `CHANGELOG.md`. Skills use SemVer in frontmatter when they change behavior.

## License

MIT
