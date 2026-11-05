---
name: verified-registry
description: Build small verified JSON registries so agents stop inventing endpoints, affiliate links, or brand strings.
version: 1.0.0
metadata:
  hermes:
    tags: [registry, grounding, anti-hallucination, config]
---

# Verified Registry Pattern

Agents invent URLs and IDs when the ground truth is not loaded. Fix that with a
tiny verified registry plus a hard instruction to use only registry values.

## Components

1. **Registry JSON** — the only allowed values for a domain
2. **Boot instruction** — "never invent; look up or ask"
3. **Auto-load** — include the registry in the profile/session context

## Example registry

```json
{
  "version": 1,
  "updated_at": "2026-11-05",
  "endpoints": {
    "status_page": "https://status.example.com",
    "nerve": "https://nerve.example.com/api/log"
  },
  "public_links": {
    "docs": "https://example.com/docs",
    "github": "https://github.com/example/project"
  },
  "do_not_invent": [
    "payment_links",
    "affiliate_urls",
    "support_emails"
  ]
}
```

## Hard rule for the agent

```text
If a value is not in the verified registry, do not guess.
Look it up from an approved source or ask the operator.
```

## Maintenance

- Change registry values in one place only
- Bump `version` on every intentional change
- Keep secrets out of the registry; store secret *names*, not secret values
- Add a CI or pre-commit check that public copy only uses registry URLs
