#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note — round 2 entry.

Writes one line of patch notes (under 160 characters) announcing that
human sleep is fixed, to /output/entry.txt for the make.fun judge.
"""

import os

PATCH_NOTE = (
    "Fixed: sleep now auto-saves every 90 minutes. "
    "Dream deaths now respawn at the last checkpoint."
)


def main() -> None:
    text = PATCH_NOTE.strip()
    if not 1 <= len(text) <= 160:
        raise ValueError(f"patch note is {len(text)} chars, must be 1-160")
    if "\n" in text or "\r" in text:
        raise ValueError("patch note must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    # Echo the note so the run log shows exactly what the judge will read.
    print(f"wrote {len(text)} chars to {out_dir}/entry.txt: {text}")


if __name__ == "__main__":
    main()
