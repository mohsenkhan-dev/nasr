#!/usr/bin/env python3
"""
storyline.py — print the storyline of a draft: its headings and the first
sentence of every paragraph under them (references/storyline.md).

Read the printout alone. In well-built prose it reads as the argument; a first
sentence that is a connector, an announcement or a description is flagged.

Usage:
  python3 storyline.py draft.md
Python 3.8+, standard library only.
"""
import re, sys
from pathlib import Path

FA_WORD = re.compile(r"[؀-ۿ]+(?:‌[؀-ۿ]+)*")
ANNOUNCE = re.compile(
    r"^(?:در\s+(?:این\s+(?:سند|یادداشت|نوشته|بخش|گزارش)|ادامه)|این\s+(?:سند|یادداشت|نوشته|بخش|گزارش)\s+|"
    r"(?:معیار|مسیر|گام|نکته|دلیل)\s+(?:نخست|اول|دوم|سوم)\s+(?:این|آن)\s+است|"
    r"همان‌طور\s+که|چنان‌که\s+گفته\s+شد)")
CONNECTOR = re.compile(r"^(?:اما|ولی|همچنین|بنابراین|پس|البته|از\s+سوی\s+دیگر|علاوه\s+بر\s+این)\b")
TEASER = re.compile(r"(?:چه\s+چیزی|چه\s+کسی|کدام).*(?:خواهد|می‌)\S*\s*[.]?$")


def first_sentence(p):
    m = re.search(r"(.+?[.!؟?…])(?:\s|$)", p.strip())
    return (m.group(1) if m else p.strip())


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    text = Path(sys.argv[1]).read_text(encoding="utf-8")
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    flagged = 0
    for block in re.split(r"\n\s*\n", text):
        b = block.strip()
        if not b or b.startswith("|") or re.match(r"^\*[^*].*\*$", b):
            continue
        h = re.match(r"^(#{1,6})\s+(.+)$", b.split("\n")[0])
        if h:
            print(("\n" if len(h.group(1)) <= 2 else "") + "  " * (len(h.group(1)) - 1) + "■ " + h.group(2))
            b = "\n".join(b.split("\n")[1:]).strip()
            if not b:
                continue
        if len(FA_WORD.findall(b)) < 8 or re.match(r"^\s*([-*]|[۰-۹0-9]+[.)])\s", b):
            continue
        s = first_sentence(b)
        body = re.sub(r"^\*\*.+?\*\*\s*", "", s)
        mark = ""
        if ANNOUNCE.match(body):
            mark = "  ← اعلام، نه ادعا"
        elif CONNECTOR.match(body):
            mark = "  ← با ربط شروع شده؛ ادعا را اول بگو"
        elif TEASER.search(body):
            mark = "  ← تعلیق؛ ادعا را بگو"
        flagged += bool(mark)
        print("   • " + s + mark)
    print(f"\n{flagged} جمله‌ی آغازین علامت خورد.")
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main())
