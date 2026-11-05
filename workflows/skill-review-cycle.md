# Workflow: Skill Review Cycle

Keep skills from rotting as tools and profiles change.

## Cadence

- Weekly: review skills touched by failing crons
- Monthly: review top 10 most-used skills
- On incident: review the skill that should have prevented it

## Per-skill pass

1. Load `SKILL.md` and linked files
2. Diff against current CLI/tool behavior
3. Remove private host/client residue
4. Patch or rewrite
5. Run `python3 tools/public_safety_scan.py skills/<name>`
6. Log what changed in one sentence

## Exit criteria

- Skill still loads
- Examples use placeholders
- Scanner clean
- One concrete improvement shipped (not a rewrite for its own sake)
