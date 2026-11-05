# Install

## Requirements

- Hermes Agent with a writable skills directory (usually `~/.hermes/skills`)
- Python 3.10+ for the optional safety scanner and readiness report scripts

## Install all skills

```bash
./tools/install_skills.sh ~/.hermes/skills
```

The installer copies each `skills/*` package into category-friendly folders when
a category is obvious, otherwise into `~/.hermes/skills/community/`.

## Install one skill

```bash
mkdir -p ~/.hermes/skills/operations
cp -R skills/cron-operations ~/.hermes/skills/operations/
```

Then ask Hermes to `skill_view` the new skill name, or restart the gateway if
your profile caches the skill index.

## Pair with Agent Nerve

```bash
pip install agent-nerve
export AGENT_NERVE_API_KEY="change-me"
agent-nerve serve --host 127.0.0.1 --port 8787
```

Point Hermes/Claude/Codex at the same `AGENT_NERVE_SERVER` and namespace so
handoffs survive session restarts. See the `task-continuity` and
`mixed-agent-handoff` skills.

## Workflows

Workflows are operator docs, not auto-loaded skills. Keep them next to your
runbooks or paste the relevant checklist into a cron prompt.
