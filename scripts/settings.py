#!/usr/bin/env python3
"""
settings.py — build the workbench page (میز کار، تنظیمات پیشرفته) for one text.

The page carries the whole checkpoint, in the order the user decides it:
  1. the outline of THIS text: printed heading, what the section says (not
     printed), where it comes from, alternative headings, add / remove / move /
     nest; every heading is checked live against the heading rules;
  2. the questions and the conflicts, each with answer buttons;
  3. the term list (official names, replacements, banned words);
  4. three style suggestions, each with a plain explanation and a short sample
     on the real material; the full parameter panel is folded away.
The user copies the resulting «کارت تنظیمات» back into the conversation.

Usage (preferred: one JSON file):
  python settings.py --config checkpoint.json --out work/nasr-desk.html

checkpoint.json:
  {"brief": "...",
   "suggestions": [{"name": "سند راهبردی", "why": "...", "sample": "پاراگراف نمونه"}],
   "outline": [{"title": "مقدمه", "job": "وضع امروز گروه", "source": "تازه",
                "level": 1, "type": "مسئله و وضعیت", "alts": ["..."]}],
   "questions": [{"q": "...", "options": ["...", "..."]}],
   "conflicts": [{"text": "...", "detail": "...", "options": ["...", "..."]}],
   "terms": [{"from": "موتور", "rule": "جایگزین شود", "to": "پیشران"}]}

Older flags still work (--brief, --suggest "recipe|why", --sections TYPE ...).
Data: assets/style_matrix.json. Python 3.8+, standard library only.
"""
import argparse, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = {"تازه", "از متن قبلی", "قبلی با افزوده", "—"}


def load_config(a, matrix):
    names = {r["name"] for r in matrix["recipes"]}
    secs = {s["name"] for s in matrix["sections"]}
    cfg = json.loads(Path(a.config).read_text(encoding="utf-8")) if a.config else {}
    if a.brief:
        cfg["brief"] = a.brief
    for item in a.suggest[:3]:
        name, _, why = item.partition("|")
        cfg.setdefault("suggestions", []).append({"name": name.strip(), "why": why.strip()})
    for s in a.sections:
        cfg.setdefault("outline", []).append({"title": s, "type": s})
    errors = []
    for s in cfg.get("suggestions", [])[:3]:
        if s.get("name") not in names:
            errors.append(f"unknown recipe: {s.get('name')} (choose from: {'، '.join(sorted(names))})")
    for s in cfg.get("outline", []):
        if s.get("type") and s["type"] not in secs:
            errors.append(f"unknown section type: {s['type']} (choose from: {'، '.join(sorted(secs))})")
        if s.get("source") and s["source"] not in SOURCES:
            errors.append(f"unknown source «{s['source']}» (choose from: {'، '.join(sorted(SOURCES))})")
    if errors:
        sys.exit("\n".join(errors))
    return cfg or None


def main():
    ap = argparse.ArgumentParser(description="Build the nasr workbench page.")
    ap.add_argument("--config", help="checkpoint JSON (outline, questions, conflicts, terms, suggestions)")
    ap.add_argument("--brief", default="", help="what the user wants to write")
    ap.add_argument("--suggest", nargs="*", default=[], help='up to three "recipe|reason" items, best first')
    ap.add_argument("--long", action="store_true", help="ignored; kept for old calls")
    ap.add_argument("--sections", nargs="*", default=[], help="section types, used as placeholder headings")
    ap.add_argument("--out", default="nasr-desk.html")
    a = ap.parse_args()
    matrix = json.loads((ROOT / "assets" / "style_matrix.json").read_text(encoding="utf-8"))
    config = load_config(a, matrix)
    page = (ROOT / "assets" / "settings.html").read_text(encoding="utf-8")
    page = page.replace("/*NASR_MATRIX*/null", json.dumps(matrix, ensure_ascii=False))
    page = page.replace("/*NASR_CONFIG*/null", json.dumps(config, ensure_ascii=False))
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    # Windows consoles default to a legacy code page and crash on Persian output.
    for _stream in (sys.stdout, sys.stderr):
        try:
            _stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    main()
