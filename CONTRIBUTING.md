# Contributing

This repo is public. Assume every line is forever.

## Before you open a PR

1. `python3 tools/public_safety_scan.py .`
2. Prefer placeholders over real hosts, tokens, and client names
3. Keep skills focused: one job per `SKILL.md`
4. Update `CHANGELOG.md`
5. Re-render the catalog after adding skills:

```bash
python3 tools/render_catalog.py
```

## Skill format

```text
skills/<name>/SKILL.md
```

Frontmatter should include at least `name` and `description`.

## Do not contribute

- Private memories or chat exports
- Auth JSON / `.env`
- Client deliverables
- Absolute personal home paths
