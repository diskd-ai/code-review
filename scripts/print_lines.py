#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def _print_lines(file_path: Path, start_line: int, end_line: int) -> int:
    try:
        lines = file_path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        sys.stderr.write(f"[ERROR] File not found: {file_path}\n")
        return 1
    except UnicodeDecodeError:
        sys.stderr.write(f"[ERROR] File is not valid UTF-8: {file_path}\n")
        return 1

    total = len(lines)
    if total == 0:
        sys.stderr.write(f"[ERROR] File is empty: {file_path}\n")
        return 1

    if start_line < 1 or end_line < 1 or start_line > end_line:
        sys.stderr.write("[ERROR] Invalid range. Expected 1 <= start <= end.\n")
        return 1

    if start_line > total:
        sys.stderr.write(
            f"[ERROR] Range starts after EOF. start={start_line}, total={total}\n"
        )
        return 1

    safe_end = min(end_line, total)
    for idx in range(start_line - 1, safe_end):
        line_no = idx + 1
        sys.stdout.write(f"{line_no}\t{lines[idx]}\n")

    if end_line > total:
        sys.stderr.write(
            f"[WARN] Range ended after EOF. end={end_line}, total={total}\n"
        )

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Print a file line range with exact line numbers."
    )
    parser.add_argument("file", help="Path to the file to print.")
    parser.add_argument("start", type=int, help="1-based start line (inclusive).")
    parser.add_argument("end", type=int, help="1-based end line (inclusive).")
    parsed = parser.parse_args()

    return _print_lines(Path(parsed.file), parsed.start, parsed.end)


if __name__ == "__main__":
    raise SystemExit(main())

