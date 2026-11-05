#!/usr/bin/env python3
"""Scan a tree for common public-safety leaks before publishing."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SKIP_DIR_NAMES = {".git", ".venv", "venv", "__pycache__", "node_modules", ".tox"}
TEXT_SUFFIXES = {
    "",
    ".md",
    ".py",
    ".sh",
    ".yml",
    ".yaml",
    ".json",
    ".toml",
    ".txt",
    ".example",
    ".html",
    ".css",
    ".js",
    ".ts",
}

PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("openai-like key", re.compile(r"\bsk-[A-Za-z0-9_-]{12,}\b")),
    ("bearer token", re.compile(r"\bBearer\s+[A-Za-z0-9._\-]{12,}\b", re.I)),
    ("aws access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("slack/discord webhook", re.compile(r"hooks\.slack\.com/services/|discord(?:app)?\.com/api/webhooks/")),
    ("absolute macos home", re.compile(r"/Users/[A-Za-z0-9._-]+")),
    ("absolute linux home", re.compile(r"/home/[A-Za-z0-9._-]+")),
    ("root private path", re.compile(r"/root/\.(?:hermes|openclaw|config)/")),
    ("env assignment secret", re.compile(r"(?i)\b(api[_-]?key|token|password|secret)\s*=\s*['\"][^'\"]{8,}")),
]


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {
            "LICENSE",
            "Makefile",
            "Dockerfile",
        }:
            continue
        yield path


def scan(root: Path) -> list[str]:
    findings: list[str] = []
    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError as exc:
            findings.append(f"{path}: unreadable ({exc})")
            continue
        for label, pattern in PATTERNS:
            if pattern.search(text):
                rel = path.relative_to(root)
                findings.append(f"{rel}: possible {label}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default=".", help="Repo or skill path to scan")
    args = parser.parse_args()
    root = Path(args.path).resolve()
    findings = scan(root)
    if not findings:
        print(f"public-safety scan clean: {root}")
        return 0
    print(f"public-safety findings in {root}:")
    for item in findings:
        print(f"  - {item}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
