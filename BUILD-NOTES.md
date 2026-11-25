# Build notes — Fortune Cookie for the Liquidated Trader

## The fortune

The entry is one fortune cookie line for a crypto trader who has just been
liquidated: "You will find great wealth soon — unfortunately, it is in your
other wallet, the empty one."

## Why this line

The judge is a freshly liquidated trader reading a fortune at 3am, and it
weighs five things in order. The line was written against them in that
order:

First, it reads as a fortune cookie message for a liquidated trader. The
opening is the classic oracular promise, "You will find great wealth
soon", and the loss is in the line itself: the wallet is empty. The
trader is in it too — the joke only works for someone who holds crypto
across more than one wallet.

Second, it aims to make the trader laugh instead of cry. The turn is
rueful and warm, never cruel or smug: nobody is mocked for losing, the
fortune itself is the fool for promising wealth that is already gone.

Third, it is one line that reads whole in a single breath: seventeen
words, well under the twenty-word cap and under the 160-character gate.

Fourth, the joke is fresh. It never says the word liquidation, never
mentions a margin call, and never reaches for the obvious liquidation
pun. The double meaning does the work: every crypto trader has another
wallet, and the wealth is in the one that is empty.

Fifth, it keeps the fortune voice. The opening is small, oracular, and
slightly formal, and the punchline breaks it with a plain, everyday
detail.

## The program

A small Python program holds the line as a constant, validates it against
both caps from the task (one to 160 characters and at most twenty words,
plus the non-whitespace and UTF-8 checks from the sealed gate), and writes
it to the entry file with no trailing newline, so the bytes on disk are
exactly the line itself. There is no input, no network, and no randomness:
every run writes the same bytes.

## Verification

The program was run locally and the entry file was read back and checked
for character count, word count, and both hash values. The kit check was
run locally from the kit directory. The only check that fails at this
stage is the transcripts check, which is expected: the parent bundles the
transcripts as its own step.

No submission was made, no account or keypair was created, and nothing
was spent or signed.
