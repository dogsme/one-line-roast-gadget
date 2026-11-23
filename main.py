#!/usr/bin/env python3
"""One-line roast entry.

Writes a single original roast line about a gadget used every day
to /output/entry.txt, UTF-8, no trailing newline, well inside the
200-character limit.
"""

from pathlib import Path

LINE = "My smartwatch throws a party when I hit 10,000 steps, then dies at 9pm like it did the workout, not me."


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"roast line is {len(text)} characters, must be 1-200")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
