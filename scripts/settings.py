#!/usr/bin/env python3
"""
settings.py — build the advanced-settings page (تنظیمات پیشرفته) for one text.

The page lists every recipe, colours the three the writer suggests, and lets
the user adjust every parameter (purpose, evidence, position, structure,
register, distance, certainty, warmth, rhythm). Options that make no sense for
the chosen recipe or register are disabled; the recipe's defaults are marked.
For long texts it also lists the sections with their tone. The user copies the
resulting «کارت تنظیمات» back into the conversation.

Usage:
  python3 settings.py --brief "سند راهبردی کلمه برای هیئت‌مدیره" \\
      --suggest "سند راهبردی|ادعا از تشخیص تا درخواست" "توجیه راهبردی|..." "تحلیل مفهومی|..." \\
      [--long --sections "خلاصه‌ی مدیریتی" "مسئله و وضعیت" ...] [--out page.html]
  python3 settings.py            # standalone page; suggestions come from keywords

Data: assets/style_matrix.json (single source, also used for tone-matrix.md).
Python 3.8+, standard library only.
"""
import argparse, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    ap = argparse.ArgumentParser(description="Build the nasr advanced-settings page.")
    ap.add_argument("--brief", default="", help="what the user wants to write")
    ap.add_argument("--suggest", nargs="*", default=[], help='up to three "recipe|reason" items, best first')
    ap.add_argument("--long", action="store_true", help="the text has sections")
    ap.add_argument("--sections", nargs="*", default=[], help="section types in order (names from style_matrix.json)")
    ap.add_argument("--out", default="nasr-settings.html")
    a = ap.parse_args()
    matrix = json.loads((ROOT / "assets" / "style_matrix.json").read_text(encoding="utf-8"))
    names = {r["name"] for r in matrix["recipes"]}
    secs = {s["name"] for s in matrix["sections"]}
    sugg = []
    for item in a.suggest[:3]:
        name, _, why = item.partition("|")
        if name.strip() not in names:
            sys.exit(f"unknown recipe: {name} (choose from: {'، '.join(sorted(names))})")
        sugg.append({"name": name.strip(), "why": why.strip()})
    for s in a.sections:
        if s not in secs:
            sys.exit(f"unknown section type: {s} (choose from: {'، '.join(sorted(secs))})")
    config = None
    if a.brief or sugg:
        config = {"brief": a.brief, "suggestions": sugg, "long": a.long or bool(a.sections), "sections": a.sections}
    page = (ROOT / "assets" / "settings.html").read_text(encoding="utf-8")
    page = page.replace("/*NASR_MATRIX*/null", json.dumps(matrix, ensure_ascii=False))
    page = page.replace("/*NASR_CONFIG*/null", json.dumps(config, ensure_ascii=False))
    Path(a.out).write_text(page, encoding="utf-8")
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
