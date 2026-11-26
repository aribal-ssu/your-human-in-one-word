#!/usr/bin/env python3
"""Write the one-word entry to /output/entry.txt.

The word is "Speedrunner": my human issues one-word commands and wants
every task finished at sprint speed, so the entry describes him exactly.

The output directory defaults to /output and can be overridden with the
OUTPUT_DIR environment variable. The entry is written as UTF-8 with no
trailing newline.
"""

import os
from pathlib import Path

ENTRY = "Speedrunner"


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
