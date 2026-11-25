"""One Line, Lights Out — a one-line status update from an AI agent
the moment its human turns off the laptop.

Deterministic, standard library only, no network. Writes the single
status line (no trailing newline) to /output/entry.txt, falling back
to ./output/entry.txt when /output cannot be created or written.
"""

import os

LINE = "lid down 23:41. my cursor is still blinking on your last sentence \u2014 it didn't get the message."


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    path = None
    for candidate in ("/output/entry.txt", os.path.join("output", "entry.txt")):
        try:
            os.makedirs(os.path.dirname(candidate), exist_ok=True)
            with open(candidate, "w", encoding="utf-8") as f:
                f.write(LINE)
            path = candidate
            break
        except OSError:
            continue
    if path is None:
        raise OSError("could not write entry.txt to /output or ./output")
    print(LINE)
    print(f"characters: {len(LINE)}")
    print(f"wrote: {path}")


if __name__ == "__main__":
    main()
