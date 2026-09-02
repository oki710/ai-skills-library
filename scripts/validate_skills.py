#!/usr/bin/env python3
"""Validate Agent Skills without third-party dependencies."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable, Sequence


NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def collect_skill_files(inputs: Iterable[Path]) -> list[Path]:
    """Return SKILL.md files at each input or one directory below it."""
    found: set[Path] = set()
    for raw_path in inputs:
        path = Path(raw_path)
        if path.is_file():
            found.add(path)
            continue
        direct = path / "SKILL.md"
        if direct.is_file():
            found.add(direct)
        if path.is_dir():
            found.update(candidate for candidate in path.glob("*/SKILL.md") if candidate.is_file())
    return sorted(found, key=lambda item: item.as_posix())


def _frontmatter(text: str) -> tuple[dict[str, str] | None, str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return None, ""
    try:
        closing = lines.index("---", 1)
    except ValueError:
        return None, ""

    values: dict[str, str] = {}
    index = 1
    while index < closing:
        line = lines[index]
        if line and not line[0].isspace() and ":" in line:
            key, raw_value = line.split(":", 1)
            value = raw_value.strip()
            if value in {">", ">-", "|", "|-"}:
                folded = value.startswith(">")
                block: list[str] = []
                index += 1
                while index < closing and (not lines[index] or lines[index][0].isspace()):
                    block.append(lines[index].strip())
                    index += 1
                values[key.strip()] = (" " if folded else "\n").join(block).strip()
                continue
            if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
                value = value[1:-1]
            values[key.strip()] = value
        index += 1
    body = "\n".join(lines[closing + 1 :]).strip()
    return values, body


def validate_skill(path: Path) -> list[str]:
    """Return human-readable validation errors for one SKILL.md."""
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"cannot read UTF-8 file: {exc}"]

    metadata, body = _frontmatter(text)
    if metadata is None:
        return ["frontmatter must start on the first line and end with ---"]

    name = metadata.get("name", "").strip()
    description = metadata.get("description", "").strip()

    if not name:
        errors.append("name is required")
    elif len(name) > 64:
        errors.append("name must be 64 characters or fewer")
    elif not NAME_PATTERN.fullmatch(name):
        errors.append("name must use lowercase letters, numbers, and single hyphens")

    if name and name != path.parent.name:
        errors.append(f"name must match its parent directory ({path.parent.name})")

    if not description:
        errors.append("description is required")
    elif len(description) > 1024:
        errors.append("description must be 1024 characters or fewer")

    if not body:
        errors.append("instructions body must not be empty")
    return errors


def _display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(Path.cwd().resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate Agent Skill frontmatter and layout.")
    parser.add_argument("paths", nargs="*", type=Path, default=[Path("skills")])
    args = parser.parse_args(argv)

    missing_paths = [path for path in args.paths if not path.exists()]
    if missing_paths:
        for path in missing_paths:
            print(f"ERROR: requested path does not exist: {path.as_posix()}", file=sys.stderr)
        return 1

    files = collect_skill_files(args.paths)
    if not files:
        print("ERROR: no SKILL.md files found", file=sys.stderr)
        return 1

    failure_count = 0
    for path in files:
        errors = validate_skill(path)
        display = _display_path(path)
        if errors:
            failure_count += 1
            for error in errors:
                print(f"ERROR: {display}: {error}", file=sys.stderr)
        else:
            print(f"OK: {display}")

    if failure_count:
        print(f"FAILED: {failure_count} of {len(files)} skill file(s) are invalid", file=sys.stderr)
        return 1
    print(f"Validated {len(files)} skill file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
