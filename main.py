"""Fortune Cookie for the Liquidated Trader entry.

The program writes exactly one fortune cookie line to /output/entry.txt.

The fortune: a classic oracular opening ("You will find great wealth
soon") broken by a rueful turn — the wealth sits in the trader's other
wallet, the empty one. One breath, no lecture, no pity.
"""

from pathlib import Path

FORTUNE = "You will find great wealth soon \u2014 unfortunately, it is in your other wallet, the empty one."

OUTPUT_PATH = Path("/output/entry.txt")


def validate(line: str) -> str:
    """Mirror the sealed gate: 1-160 chars, UTF-8, not only whitespace.

    The task also caps the fortune at 20 words, so the word count is
    checked here too — the judge reads a fortune that fits one breath.
    """
    if not 1 <= len(line) <= 160:
        raise ValueError(f"entry must be 1-160 chars, got {len(line)}")
    if len(line.split()) > 20:
        raise ValueError(f"entry must be at most 20 words, got {len(line.split())}")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")
    return line


def main() -> None:
    line = validate(FORTUNE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
