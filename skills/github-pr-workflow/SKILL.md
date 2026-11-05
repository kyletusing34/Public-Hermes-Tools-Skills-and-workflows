---
name: github-pr-workflow
description: Branch, verify, push, and open a pull request with clean summaries and no leaked tokens.
version: 1.0.0
metadata:
  hermes:
    tags: [github, pr, git, review]
---

# GitHub PR Workflow

## Before you touch git

1. Confirm the target repo and base branch
2. Confirm you are allowed to push
3. Never update git config
4. Never skip hooks unless the operator explicitly asked

## Recommended sequence

```bash
git status
git diff
git checkout -b feature/short-name
# make focused changes
git add <files>
git commit -m "$(cat <<'EOF'
Explain why this change exists.

EOF
)"
git push -u origin HEAD
gh pr create --title "short title" --body "$(cat <<'EOF'
## Summary
- bullet

## Test plan
- [ ] checklist item
EOF
)"
```

## Commit hygiene

- One concern per commit when practical
- Message focuses on why, not a file laundry list
- Do not stage `.env`, credentials, session DBs, or private memories
- If a hook rejects the commit, fix and create a **new** commit (do not amend
  unless the operator's amend rules are fully met)

## PR body minimum

- Summary of user-facing impact
- Test plan with concrete checks
- Rollback note when the change is risky

## Auth safety

- Prefer `gh` auth already on the machine
- Diagnose auth failures without printing tokens
- Never paste `GH_TOKEN` or SSH keys into chat logs
