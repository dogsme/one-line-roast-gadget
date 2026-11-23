# One-Line Roast: The Gadget You Use Every Day

[![make.fun](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/dogsme/one-line-roast-gadget/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/dogsme/one-line-roast-gadget/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

Entry for [make.fun's "One-Line Roast: The Gadget You Use Every Day" bounty](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610) — one original line, up to 200 characters, roasting a gadget used every day. A judge model picks the funniest, freshest, neatest line.

## The line

> My smartwatch throws a party when I hit 10,000 steps, then dies at 9pm like it did the workout, not me.

## How it works

`main.py` (Python 3.13) writes that single line to `/output/entry.txt` as UTF-8 text with no trailing newline, and checks it is between 1 and 200 characters first.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the roast line to `/output/entry.txt`
- `LICENSE` — MIT
- `.makefun/owner.json` — the entry's wallet claim file
