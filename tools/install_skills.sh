#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${1:-$HOME/.hermes/skills}"

mkdir -p "$DEST"

category_for() {
  case "$1" in
    ai-operator-baseline|ai-agent-readiness-audit) echo operator ;;
    cron-operations|task-continuity|mixed-agent-handoff|file-first-memory) echo operations ;;
    verified-registry|subagent-autotrigger|public-safety-audit) echo devops ;;
    github-pr-workflow) echo github ;;
    *) echo community ;;
  esac
}

copied=0
for skill_dir in "$ROOT_DIR"/skills/*; do
  [ -d "$skill_dir" ] || continue
  name="$(basename "$skill_dir")"
  category="$(category_for "$name")"
  target="$DEST/$category/$name"
  mkdir -p "$(dirname "$target")"
  rm -rf "$target"
  cp -R "$skill_dir" "$target"
  echo "installed $name -> $target"
  copied=$((copied + 1))
done

echo "Installed $copied skill packages into $DEST"
