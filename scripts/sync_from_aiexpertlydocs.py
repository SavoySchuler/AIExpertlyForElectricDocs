#!/usr/bin/env python3
"""Clone AIExpertlyDocs into this repo and apply only founder-count edits.

Usage:
    python3 scripts/sync_from_aiexpertlydocs.py <source_repo_dir> <target_repo_dir>

The source repo is treated as canonical. This script copies all tracked Markdown
and repository files from source to target, excluding .git, then applies only the
minimum text changes needed to convert the package from a two-founder 50/50
structure to a three-founder equal-ownership structure.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

SOURCE_FOUNDER_A = "Founder A"
SOURCE_FOUNDER_B = "Founder B"
FOUNDER_A = "Savoy Schuler"
FOUNDER_B = "Jonathan Cain"
FOUNDER_C = "Teemu Karvonen"

EXCLUDED_DIRS = {".git", ".github"}
SELF_KEEP = {
    Path(".github/workflows/sync-from-aiexpertlydocs.yml"),
    Path("scripts/sync_from_aiexpertlydocs.py"),
}

TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".yml",
    ".yaml",
    ".json",
    ".csv",
}


def run(cmd: list[str], cwd: Path) -> str:
    return subprocess.check_output(cmd, cwd=cwd, text=True).strip()


def tracked_files(repo: Path) -> list[Path]:
    output = run(["git", "ls-files"], repo)
    return [Path(line) for line in output.splitlines() if line.strip()]


def copy_source_to_target(source: Path, target: Path) -> list[Path]:
    files = tracked_files(source)

    # Remove target files except this workflow/script so the sync can commit itself.
    for path in tracked_files(target):
        if path in SELF_KEEP:
            continue
        full = target / path
        if full.exists():
            full.unlink()

    copied: list[Path] = []
    for rel in files:
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        src = source / rel
        dst = target / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        copied.append(rel)
    return copied


def transform_text(text: str, rel: Path) -> str:
    original = text

    # Founder names.
    text = text.replace("Founder A", FOUNDER_A)
    text = text.replace("Founder B", FOUNDER_B)

    # Generic two-founder references.
    text = text.replace("two equal founders", "three equal founders")
    text = text.replace("two founders", "three founders")
    text = text.replace("Two founders", "Three founders")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two-Founder", "three-Founder")
    text = text.replace("two Founder", "three Founder")
    text = text.replace("2 founders", "3 founders")
    text = text.replace("50/50", "one-third / one-third / one-third")
    text = text.replace("50%/50%", "33.3333% / 33.3333% / 33.3333%")
    text = text.replace("50% / 50%", "33.3333% / 33.3333% / 33.3333%")
    text = text.replace("50% of the initial Membership Units", "33.3333% of the initial Membership Units")
    text = text.replace("50% of initial Membership Units", "33.3333% of initial Membership Units")
    text = text.replace("each holding 50%", "each holding 33.3333%")
    text = text.replace("each holding one-half", "each holding one-third")
    text = text.replace("equal halves", "equal thirds")
    text = text.replace("half", "one-third")
    text = text.replace("Half", "One-third")

    # Approval mechanics that explicitly depend on only two original Founders.
    text = text.replace(
        "while both original Founders remain Members, approval of each original Founder",
        "while all three original Founders remain Members, approval of at least two original Founders",
    )
    text = text.replace(
        "while both original Founders remain Members, each original Founder",
        "while all three original Founders remain Members, at least two original Founders",
    )
    text = text.replace(
        "while there are two Founders",
        "while there are three Founders",
    )
    text = text.replace(
        "dual founder approval",
        "approval of at least two Founders",
    )
    text = text.replace(
        "both founders",
        "the Founders",
    )
    text = text.replace(
        "both Founders",
        "the Founders",
    )
    text = text.replace(
        "each original Founder",
        "at least two original Founders",
    )

    # Common cap table / vesting values from the canonical two-founder package.
    text = text.replace("50,000,000", "33,333,333")
    text = text.replace("25,000,000", "16,666,667")
    text = text.replace("12,500,000", "8,333,333")
    text = text.replace("37,500,000", "25,000,000")
    text = text.replace("100,000,000", "99,999,999")

    # Add Teemu Karvonen where files have founder tables/lists but source only had two rows.
    lines = text.splitlines()
    out: list[str] = []
    for line in lines:
        out.append(line)
        if FOUNDER_B in line and FOUNDER_C not in text:
            # Conservative insertion for Markdown tables only.
            if line.strip().startswith("|"):
                inserted = line.replace(FOUNDER_B, FOUNDER_C)
                out.append(inserted)
    text = "\n".join(out)
    if original.endswith("\n"):
        text += "\n"

    # Document-specific cleanup for README and common schedules.
    if rel.name == "README.md":
        text = text.replace(
            "The Company begins with three founders, each holding 33.3333% of the initial Membership Units.",
            "The Company begins with three founders: Savoy Schuler, Jonathan Cain, and Teemu Karvonen, each holding 33.3333% of the initial Membership Units.",
        )

    return text


def transform_files(target: Path, copied: list[Path]) -> None:
    for rel in copied:
        path = target / rel
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        path.write_text(transform_text(text, rel), encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: sync_from_aiexpertlydocs.py <source_repo_dir> <target_repo_dir>", file=sys.stderr)
        return 2
    source = Path(sys.argv[1]).resolve()
    target = Path(sys.argv[2]).resolve()
    copied = copy_source_to_target(source, target)
    transform_files(target, copied)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
