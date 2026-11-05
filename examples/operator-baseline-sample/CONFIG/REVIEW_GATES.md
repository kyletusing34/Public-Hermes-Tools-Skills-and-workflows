# Review Gates

## Always Review
- billing and payment actions
- public publishing
- auth or secret changes
- destructive actions
- new external integrations

## Usually Safe
- internal drafts
- formatting
- deterministic summaries
- local documentation
- queue preparation with no irreversible step

## Rollback Rule
If an action meaningfully changes production or public state, write the rollback or fallback before execution.
