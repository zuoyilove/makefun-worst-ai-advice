# Worst AI Advice — make.fun entry
# (u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
#
# One line of the worst possible advice an AI could give, written as
# plain text to /output/entry.txt. The line is a fixed string: the grader
# runs the program twice and the runs must be deterministic, so there is
# no randomness and no input. The gate allows 1 to 140 characters.

LINE = (
    "Use the same password everywhere, then email it to yourself with "
    "the subject line 'all my passwords, please steal'."
)

MAX_CHARS = 140


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, gate is 1-140"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "entry must not be only whitespace / padded"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
