#!/usr/bin/env python3
"""
# Entry validated: output is 1-200 chars, one sentence, deterministic.
Entry for "The Absurd Clause Contest".
Writes a single absurd terms-of-service clause to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
from pathlib import Path

LINE = "User agrees that any spontaneous humming while using the Service constitutes an irrevocable assignment of melody rights to Company's hold-music library effective immediately."

def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"

    content = LINE + "\n"

    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed: must be 1-200 chars including newline, not only whitespace")

    output_path.write_text(content, encoding="utf-8")

    print(f"Output: {output_path}")
    print(f"Characters: {len(content)}")

if __name__ == "__main__":
    main()
