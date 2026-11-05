---
name: public-safety-audit
description: Scan skills, workflows, and docs for secrets, private paths, and client leakage before publishing.
version: 1.0.0
metadata:
  hermes:
    tags: [security, publishing, redaction, audit]
---

# Public Safety Audit

Use before any git push to a public repo or any "share this skill" request.

## Run the scanner

```bash
python3 tools/public_safety_scan.py .
```

Exit code `1` means findings. Fix or rewrite before publishing.

## Manual pass

Search for:

- `sk-`, `Bearer `, `AKIA`, `api_key`, `BEGIN PRIVATE`
- Real domains and hostnames you would not want public
- Absolute paths under root home or personal user home directories
- Client names, emails, phone numbers
- Channel IDs, webhook URLs with tokens

## Rewrite pattern

Replace concrete private facts with placeholders, then keep the procedure.

Before:

```text
Post to Discord channel 123456 using bot token from the private agent auth file on the host
```

After:

```text
Post to the configured ops channel using the bot token from your secret store
```

## Ship rule

If the scanner is dirty, do not push. Public contribution quality includes
public safety.
