# Install Notes

## What is in this bundle

- `ai-agent-readiness-audit`
- `ai-operator-baseline`
- example readiness report
- example scaffolded baseline workspace

## Generic install flow

1. Unzip the bundle.
2. If your agent product supports skill folders, place the skill folder inside its skills directory or point the agent at the unpacked skill folder.
3. If your agent product does not support skill folders directly, use the included scaffold script or copy the generated example files into your workspace manually.

## Best first use

1. Run the readiness audit on one workflow.
2. Only after that, scaffold the operator baseline into the workspace that owns that workflow.
3. Keep the first operationalized workflow internal and proof-bearing.
