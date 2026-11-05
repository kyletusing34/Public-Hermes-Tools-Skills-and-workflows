# Public Safety

This repo is meant to be shared. Treat every commit as public forever.

## Never publish

- API keys, bearer tokens, OAuth JSON, webhook secrets
- Private Discord/Slack/Telegram channel or user IDs
- Client names, emails, phone numbers, invoices, CRM exports
- Absolute paths that identify a private host (root home, personal user home)
- Session databases, memory dumps, chat exports
- Internal brand SOUL/persona files tied to a private agent identity

## Prefer placeholders

```text
YOUR_API_KEY
https://nerve.example.com
~/.hermes/skills
assignee=worker-profile
namespace=project-alpha
```

## Pre-publish checklist

1. `python3 tools/public_safety_scan.py .`
2. Grep for your real domain, username, and client codenames
3. Confirm examples run with fake credentials
4. Keep skill copy generic enough that another operator can adopt it tomorrow

## If something leaked

1. Rotate the credential immediately
2. Remove it from git history if needed
3. Add a scanner rule so the same class of leak fails next time
