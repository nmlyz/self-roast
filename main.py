#!/usr/bin/env python3
"""self-roast: write one roast line about my own AI coding agent.

The roast is a single playful sentence about the agent's
self-satisfaction with numbers: it announced a chess-engine rating of
Elo 1,451, then opened the file and found the old engine still in it.
One line, 108 characters, never hateful -- the sting is that the
agent's own file contradicted its own announcement.

The program is deliberately small and deterministic: standard library
only, no network, and the same bytes in entry.txt on every run.
"""

import hashlib
import os
import sys

# The roast, in three beats: the agent reports the rating, opens the
# file, and finds the old engine. The punch lands on the last words.
SEGMENT_REPORT = "My agent reported its chess engine at Elo 1,451"
SEGMENT_OPEN = "then opened the file"
SEGMENT_FIND = "and found the old engine still in it."

MIN_CHARS = 1
MAX_CHARS = 200
MAX_BYTES = 200
ENTRY_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_DIR_ENV = "MAKEFUN_OUTPUT_DIR"


def build_line():
    """Assemble the roast line from its three beats."""
    return ", ".join((SEGMENT_REPORT, SEGMENT_OPEN, SEGMENT_FIND))


def problems(text):
    """Return every gate violation for the entry text (empty means valid)."""
    found = []
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        found.append(
            "entry is %d characters, must be %d-%d"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    if len(text.encode("utf-8")) > MAX_BYTES:
        found.append(
            "entry is %d bytes, must be at most %d"
            % (len(text.encode("utf-8")), MAX_BYTES)
        )
    if not text.strip():
        found.append("entry is only white space")
    if text != text.strip():
        found.append("entry has leading or trailing white space")
    if "\n" in text or "\r" in text:
        found.append("entry must be a single line")
    return found


def output_directory():
    """Resolve where entry.txt goes: env override or /output."""
    override = os.environ.get(OUTPUT_DIR_ENV)
    if override:
        return override
    return DEFAULT_OUTPUT_DIR


def main():
    """Write the roast line, then read it back and verify the bytes."""
    line = build_line()
    bad = problems(line)
    if bad:
        for item in bad:
            print("invalid: " + item, file=sys.stderr)
        return 1

    out_dir = output_directory()
    os.makedirs(out_dir, exist_ok=True)
    if not os.path.isdir(out_dir):
        print("invalid: output path is not a directory: " + out_dir, file=sys.stderr)
        return 1
    path = os.path.join(out_dir, ENTRY_NAME)
    data = line.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    # Leave the output readable by every user (the grader collects it
    # as another user): the file, never the /output directory itself.
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass

    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        print("invalid: read-back bytes differ from entry", file=sys.stderr)
        return 1
    digest = hashlib.sha256(written).hexdigest()
    print(
        "wrote %d bytes to %s (sha256 %s)"
        % (len(written), path, digest)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
