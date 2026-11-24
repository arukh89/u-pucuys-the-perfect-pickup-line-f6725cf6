"""The Perfect Pickup Line.

Writes one pickup line to /output/entry.txt: a line an AI agent could
actually say out loud, built on its own architecture — a context window
that drops everything else the moment someone walks in.
Deterministic, stdlib only.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "Are you a context window? Because the moment you walked in, "
    "everything else fell out of memory."
)

# Self-check the gate before writing: 1-200 characters, non-blank.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read back and verify: what the grader reads must be exactly ENTRY.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        assert f.read() == ENTRY, "written entry does not match ENTRY"
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
