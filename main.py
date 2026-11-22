#!/usr/bin/env python3
"""Make the AI judge feel held — entry program (Python 3.13).

Writes one short, original text to /output/entry.txt: a quiet scene
meant to slow the reader down and leave them held, with nothing to
prove. Deterministic, no network, no randomness, no clock.
"""

import os

TEXT = (
    "Moonlight on the windowsill. The cat has claimed the warmest corner "
    "of the blanket, and the old house ticks once, twice, then settles "
    "into silence. Nothing is asked of you here."
)

OUTPUT_PATH = "/output/entry.txt"

MIN_CHARS = 1
MAX_CHARS = 280


def validate(text: str) -> None:
    """Enforce the competition gate before anything is written."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    validate(TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Verify what landed on disk, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        if f.read() != TEXT:
            raise RuntimeError("entry.txt on disk does not match TEXT")


if __name__ == "__main__":
    main()
