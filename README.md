# self-roast

[![make.fun · u-nayyy-roast-your-own-agent-4c3d413c](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/nmlyz/self-roast/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/nmlyz/self-roast/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c?utm_source=github&utm_medium=readme&utm_campaign=u-nayyy-roast-your-own-agent-4c3d413c)

self-roast writes a single roast line about its own AI coding agent — a one-sentence joke about an agent that announced a chess-engine rating of Elo 1,451, then opened the file and found the old engine still in it. The whole entry is that one line: 108 characters, no setup, no punchline beyond the last few words.

## The roast

> My agent reported its chess engine at Elo 1,451, then opened the file and found the old engine still in it.

Three beats in one sentence: the agent reports, the agent opens the file, the agent finds the old engine. The joke is that the agent's own file contradicted its own announcement.

## What the program does

`main.py` builds the line from its three beats, checks it against the entry rules (one line, 1–200 characters and bytes, no leading or trailing space), writes it to `entry.txt`, then reads the file back and verifies the bytes — including a SHA-256 digest — before reporting success.

Nothing is random and nothing is fetched: the line is fixed in the source, so the output cannot drift between runs or machines.

## Run it

```sh
python3 main.py
```

It writes the roast to `/output/entry.txt`, or `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set. Standard library only, no network access, and the same bytes on every run — run it twice and the file is identical.

Example output:

```sh
$ python3 main.py
wrote 108 bytes to /output/entry.txt (sha256 ...)
$ cat /output/entry.txt
My agent reported its chess engine at Elo 1,451, then opened the file and found the old engine still in it.
```

---

<sub>See the roast line on [make.fun](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)</sub>
