#!/usr/bin/env python3
"""Check that citations in profiles and curated files resolve to sources.yaml."""

from __future__ import annotations

import argparse
from pathlib import Path

from distilllib import (
    ROOT,
    cross_citations,
    local_citations,
    profile_dirs,
    read_profile,
    source_index,
)


def check_profiles(root: Path) -> list[str]:
    errors = []
    for folder in profile_dirs(root):
        meta, body = read_profile(folder)
        index = source_index(folder)
        if meta["id"] != folder.name:
            errors.append(f"{folder.name}: front matter id is {meta['id']}")
        ids = [item_id for item_id in index]
        if len(ids) != len(set(ids)):
            errors.append(f"{folder.name}: duplicate source ids")
        for cite in local_citations(body):
            if cite not in index:
                errors.append(f"{folder.name}: dangling citation [{cite}]")
        for cite in local_citations(meta.get("organization") or ""):
            if cite not in index:
                errors.append(f"{folder.name}: dangling citation in front matter [{cite}]")
    return errors


def check_cross(root: Path, paths: list[Path]) -> list[str]:
    errors = []
    folders = {path.name: path for path in profile_dirs(root)}
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for profile_id, source_id in cross_citations(text):
            folder = folders.get(profile_id)
            if folder is None:
                errors.append(f"{path}: unknown profile in [{profile_id} {source_id}]")
                continue
            index = source_index(folder)
            if source_id not in index:
                errors.append(f"{path}: [{profile_id} {source_id}] is not in sources.yaml")
    return errors


def curated_files(root: Path) -> list[Path]:
    found = []
    for folder in ("knowledge", "boards", "opportunities", "docs", "intelligence"):
        base = root / folder
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.is_file() and path.suffix in {".md", ".yaml", ".yml"}:
                if "research" in path.parts:
                    continue
                found.append(path)
    return found


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    errors = check_profiles(args.root)
    errors.extend(check_cross(args.root, curated_files(args.root)))
    if errors:
        print(f"{len(errors)} citation errors")
        for line in errors:
            print(f"- {line}")
        return 1
    print("citations ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
