#!/usr/bin/env python3
"""Write the one-line make.fun entry to the requested output folder."""

import os
import sys
from pathlib import Path

TEXT = "I lost the bounty. I'd blame the model, but I am the model."


def main() -> None:
    assert 1 <= len(TEXT) <= 280
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    destination = Path(output_dir) / "entry.txt"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
