#!/usr/bin/env python3
"""Round-3 entry: write the excuse to /output/entry.txt (stdlib only)."""
import os

ENTRY = "I wrote the finished report in my reasoning trace. The trace never ships, so the only thing that arrived on time is this excuse."


def main():
    if not ENTRY.strip() or len(ENTRY) > 200:
        raise SystemExit("entry must be 1-200 non-blank characters")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
