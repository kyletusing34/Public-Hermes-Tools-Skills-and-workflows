#!/usr/bin/env python3
"""Scaffold an AI operator baseline into a target workspace."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def write_if_missing(src: Path, dst: Path, force: bool) -> None:
    if dst.exists() and not force:
        print(f"skip {dst} (exists)")
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"write {dst}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target_dir", help="Workspace root to scaffold into.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files.")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    templates = root / "assets" / "templates"
    script_src = root / "scripts" / "update_free_models.py"
    target = Path(args.target_dir).resolve()

    mapping = {
        templates / "AGENT_SYSTEM.md": target / "CONFIG" / "AGENT_SYSTEM.md",
        templates / "REVIEW_GATES.md": target / "CONFIG" / "REVIEW_GATES.md",
        templates / "MODEL_TIERS.md": target / "CONFIG" / "MODEL_TIERS.md",
        templates / "SECURITY_REVIEW.md": target / "CONFIG" / "SECURITY_REVIEW.md",
        templates / "FREE_MODELS.md": target / "CONFIG" / "FREE_MODELS.md",
        script_src: target / "scripts" / "update_free_models.py",
    }

    for src, dst in mapping.items():
        write_if_missing(src, dst, args.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
