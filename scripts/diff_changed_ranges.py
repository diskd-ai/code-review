#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass(frozen=True)
class HunkRange:
    old_start: int
    old_count: int
    new_start: int
    new_count: int


@dataclass(frozen=True)
class FileHunks:
    path: str
    status: str  # modified | added | deleted | renamed
    hunks: tuple[HunkRange, ...]


_HUNK_HEADER_RE = re.compile(
    r"^@@ -(?P<old_start>\d+)(?:,(?P<old_count>\d+))? "
    r"\+(?P<new_start>\d+)(?:,(?P<new_count>\d+))? @@"
)


def _parse_hunk_header(line: str) -> HunkRange | None:
    match = _HUNK_HEADER_RE.match(line)
    if match is None:
        return None

    old_start = int(match.group("old_start"))
    old_count = int(match.group("old_count") or "1")
    new_start = int(match.group("new_start"))
    new_count = int(match.group("new_count") or "1")

    return HunkRange(
        old_start=old_start,
        old_count=old_count,
        new_start=new_start,
        new_count=new_count,
    )


def _strip_diff_path(path: str) -> str:
    if path in {"/dev/null", ""}:
        return path
    if path.startswith("a/") or path.startswith("b/"):
        return path[2:]
    return path


def _status_from_paths(old_path: str, new_path: str) -> str:
    if old_path == "/dev/null" and new_path != "/dev/null":
        return "added"
    if old_path != "/dev/null" and new_path == "/dev/null":
        return "deleted"
    if old_path != new_path:
        return "renamed"
    return "modified"


def parse_unified_diff(diff_text: str) -> tuple[FileHunks, ...]:
    files: list[FileHunks] = []

    current_old_path = ""
    current_new_path = ""
    current_file_key = ""
    current_hunks: list[HunkRange] = []

    def flush_current() -> None:
        nonlocal current_old_path, current_new_path, current_file_key, current_hunks
        if not current_file_key:
            return
        status = _status_from_paths(current_old_path, current_new_path)
        files.append(
            FileHunks(
                path=current_file_key,
                status=status,
                hunks=tuple(current_hunks),
            )
        )
        current_old_path = ""
        current_new_path = ""
        current_file_key = ""
        current_hunks = []

    for raw_line in diff_text.splitlines():
        line = raw_line.rstrip("\n")

        if line.startswith("diff --git "):
            flush_current()
            parts = line.split()
            if len(parts) >= 4:
                current_old_path = _strip_diff_path(parts[2])
                current_new_path = _strip_diff_path(parts[3])
                current_file_key = current_new_path
            else:
                current_old_path = ""
                current_new_path = ""
                current_file_key = ""
            current_hunks = []
            continue

        if line.startswith("--- "):
            current_old_path = _strip_diff_path(line[len("--- ") :].strip())
            continue

        if line.startswith("+++ "):
            current_new_path = _strip_diff_path(line[len("+++ ") :].strip())
            current_file_key = (
                current_new_path if current_new_path != "/dev/null" else current_old_path
            )
            continue

        hunk = _parse_hunk_header(line)
        if hunk is not None:
            current_hunks.append(hunk)
            continue

    flush_current()
    return tuple(files)


def _run_git(args: Sequence[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        check=False,
        capture_output=True,
        text=True,
    )


def _build_diff_args(rev_range: str | None, staged: bool, unified: int) -> list[str]:
    args: list[str] = ["diff", f"--unified={unified}"]
    if staged:
        args.append("--cached")
    if rev_range:
        args.append(rev_range)
    return args


def _format_hunk(h: HunkRange) -> str:
    return (
        f"  new: +{h.new_start},{h.new_count} "
        f"| old: -{h.old_start},{h.old_count}"
    )


def _print_hunks(files: Iterable[FileHunks]) -> None:
    for file in files:
        print(f"{file.path} ({file.status})")
        if not file.hunks:
            print("  (no hunks found)")
            continue
        for hunk in file.hunks:
            print(_format_hunk(hunk))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="List changed line ranges (hunks) from `git diff`."
    )
    parser.add_argument(
        "--range",
        dest="rev_range",
        default=None,
        help="Git revision range passed to `git diff` (e.g., main..HEAD).",
    )
    parser.add_argument(
        "--staged",
        action="store_true",
        help="Use staged changes (`git diff --cached`).",
    )
    parser.add_argument(
        "--unified",
        type=int,
        default=0,
        help="Number of context lines for `git diff` (default: 0).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON instead of text.",
    )
    parsed = parser.parse_args()

    result = _run_git(_build_diff_args(parsed.rev_range, parsed.staged, parsed.unified))
    if result.returncode != 0:
        sys.stderr.write(result.stderr or "git diff failed\n")
        return 1

    files = parse_unified_diff(result.stdout)

    if parsed.json:
        payload = {
            "files": [
                {
                    "path": f.path,
                    "status": f.status,
                    "hunks": [
                        {
                            "old_start": h.old_start,
                            "old_count": h.old_count,
                            "new_start": h.new_start,
                            "new_count": h.new_count,
                        }
                        for h in f.hunks
                    ],
                }
                for f in files
            ]
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0

    _print_hunks(files)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
