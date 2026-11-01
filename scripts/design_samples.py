#!/usr/bin/env python3
"""
design_samples.py — show a Persian document in several design directions, side
by side, so the user picks a look before the real file is built.

Each direction is a full set of design tokens (fonts, colours, heading style,
callout box, table, number tiles, cover). The page renders, for every
direction, a cover and one content page made from the user's REAL title,
headings, a paragraph, a table and a few figures. The chosen direction's
tokens are written to <out>.tokens.json; docx-pdf.md §7 applies them to Word.

Usage:
  python design_samples.py --content sample.json --out work/design.html
  python design_samples.py --content sample.json --only 2,4 --out work/design.html
  python design_samples.py --list                # the directions and their tokens

sample.json:
  {"title": "نقشه‌ی راه پنج‌ساله", "subtitle": "گروه نمونه", "date": "پاییز ۱۴۰۵",
   "heading": "مقدمه", "subheading": "دو کسب‌وکار، یک گروه",
   "paragraph": "…", "box": "هدف فاز. …",
   "table": [["شاخص", "امروز", "سال ۱"], ["مشتری", "۵", "۱۵"]],
   "kpis": [["۱۰۰", "مشتری"], ["۴۵٪", "سهم بازار"]],
   "brand": {"accent": "#…"}}           # optional: a brand colour overrides the palette

The colours here are design directions, not a house style: the agent offers
them only when the user asks for a designed document (document-design.md).
Fonts are the bundled Vazirmatn and Lalezar, loaded from assets/fonts, so the
page renders offline. Python 3.8+, standard library only.
"""
import argparse, html, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS = (ROOT / "assets" / "fonts").as_uri()

DIRECTIONS = [
    {"id": 1, "name": "رسمی و آرام", "for": "گزارش هیئت‌مدیره، نامه‌ی رسمی، سند سازمانی محافظه‌کار",
     "head_font": "Vazirmatn", "head_weight": 700, "body_font": "Vazirmatn",
     "ink": "#1d2433", "muted": "#5c6577", "accent": "#1f3a5f", "accent2": "#8a6d3b",
     "box_bg": "#f3f5f8", "box_rule": "#1f3a5f", "table_head_bg": "#1f3a5f", "table_head_ink": "#ffffff",
     "tile_bg": "#f3f5f8", "cover_bg": "#ffffff", "cover_ink": "#1f3a5f", "cover_band": "#1f3a5f",
     "heading_rule": True},
    {"id": 2, "name": "مدرن و پررنگ", "for": "نقشه‌ی راه، ارائه به سرمایه‌گذار، سند استارتاپی",
     "head_font": "Lalezar", "head_weight": 400, "body_font": "Vazirmatn",
     "ink": "#262338", "muted": "#857fa3", "accent": "#3b2a8f", "accent2": "#6e4cff",
     "box_bg": "#f3f0ff", "box_rule": "#6e4cff", "table_head_bg": "#3b2a8f", "table_head_ink": "#ffffff",
     "tile_bg": "#f3f0ff", "cover_bg": "linear-gradient(160deg,#21166a,#4a32c9 60%,#8b65ff)",
     "cover_ink": "#ffffff", "cover_band": "#ffffff", "heading_rule": False},
    {"id": 3, "name": "مینیمال تک‌رنگ", "for": "یادداشت تحلیلی، گزارش پژوهشی، متن بلند خواندنی",
     "head_font": "Vazirmatn", "head_weight": 400, "body_font": "Vazirmatn",
     "ink": "#111111", "muted": "#777777", "accent": "#111111", "accent2": "#999999",
     "box_bg": "#ffffff", "box_rule": "#111111", "table_head_bg": "#ffffff", "table_head_ink": "#111111",
     "tile_bg": "#ffffff", "cover_bg": "#ffffff", "cover_ink": "#111111", "cover_band": "#111111",
     "heading_rule": False},
    {"id": 4, "name": "گزارش داده‌محور", "for": "گزارش عملکرد، داشبورد چاپی، گزارش سالانه",
     "head_font": "Vazirmatn", "head_weight": 900, "body_font": "Vazirmatn",
     "ink": "#14302e", "muted": "#5d7472", "accent": "#0f766e", "accent2": "#d97706",
     "box_bg": "#ecfdf8", "box_rule": "#d97706", "table_head_bg": "#0f766e", "table_head_ink": "#ffffff",
     "tile_bg": "#0f766e", "cover_bg": "#0f766e", "cover_ink": "#ffffff", "cover_band": "#d97706",
     "heading_rule": True},
]

CSS = """
@font-face{font-family:Vazirmatn;font-weight:400;src:url("%(f)s/Vazirmatn-Regular.ttf")}
@font-face{font-family:Vazirmatn;font-weight:500;src:url("%(f)s/Vazirmatn-Medium.ttf")}
@font-face{font-family:Vazirmatn;font-weight:700;src:url("%(f)s/Vazirmatn-Bold.ttf")}
@font-face{font-family:Vazirmatn;font-weight:600;src:url("%(f)s/Vazirmatn-SemiBold.ttf")}
@font-face{font-family:Vazirmatn;font-weight:900;src:url("%(f)s/Vazirmatn-Black.ttf")}
@font-face{font-family:Lalezar;src:url("%(f)s/Lalezar-Regular.ttf")}
*{box-sizing:border-box}
body{margin:0;background:#e9e9e6;font-family:Vazirmatn,Tahoma,sans-serif;color:#222;direction:rtl}
.intro{max-width:1200px;margin:0 auto;padding:20px 16px 0}
.intro h1{font-size:22px;margin:0}.intro p{color:#555;margin:4px 0 0}
.dir{max-width:1200px;margin:18px auto;padding:0 16px}
.dir h2{font-size:18px;margin:0}.dir .for{color:#666;font-size:14px;margin-bottom:10px}
.pages{display:flex;gap:18px;flex-wrap:wrap}
.page{width:420px;height:594px;background:#fff;box-shadow:0 2px 10px rgba(0,0,0,.12);position:relative;overflow:hidden;flex:none}
.cover{display:flex;flex-direction:column;justify-content:center;padding:0 40px}
.cover .t{font-size:38px;line-height:1.35}.cover .s{font-size:17px;margin-top:10px;opacity:.85}
.cover .band{width:70px;height:5px;border-radius:3px;margin:22px 0}
.cover .d{position:absolute;bottom:34px;font-size:13px;opacity:.8}
.content{padding:34px 34px 0;font-size:11.5px;line-height:2}
.content h3{font-size:22px;margin:0 0 6px;line-height:1.4}
.content h4{font-size:13.5px;margin:10px 0 2px}
.content p{margin:0 0 8px;text-align:justify}
.box{padding:8px 12px;margin:8px 0;border-radius:6px}
table{width:100%;border-collapse:collapse;margin:8px 0;font-size:10.5px}
td,th{padding:4px 6px;text-align:start}
.tiles{display:flex;gap:8px;margin-top:8px}
.tile{flex:1;border-radius:8px;padding:6px 4px;text-align:center}
.tile b{display:block;font-size:20px;line-height:1.5}.tile span{font-size:10px}
.pick{margin-top:8px;font-size:14px}
"""


def page_html(d, c):
    e = html.escape
    brand = (c.get("brand") or {}).get("accent")
    acc = brand or d["accent"]
    head = f"font-family:{d['head_font']};font-weight:{d['head_weight']};color:{acc}"
    rule = f"border-bottom:2px solid {acc};padding-bottom:4px" if d["heading_rule"] else ""
    rows = c.get("table") or []
    thead = "".join(f"<th>{e(x)}</th>" for x in rows[0]) if rows else ""
    head_style = f"background:{d['table_head_bg'] if not brand or d['table_head_bg'] == '#ffffff' else brand};color:{d['table_head_ink']}"
    if d["table_head_bg"] == "#ffffff":
        head_style += f";border-bottom:1.5px solid {d['ink']}"
    tbody = "".join("<tr>" + "".join(f"<td style='border-bottom:1px solid #e5e5e5'>{e(x)}</td>" for x in r) + "</tr>" for r in rows[1:])
    tile_dark = d["tile_bg"] not in ("#ffffff",) and d["id"] == 4
    tiles = "".join(
        f"<div class='tile' style='background:{d['tile_bg']};{'color:#fff' if tile_dark else ''};"
        f"{'border:1px solid ' + d['ink'] if d['tile_bg'] == '#ffffff' else ''}'>"
        f"<b style='font-family:{d['head_font']};color:{'#fff' if tile_dark else acc}'>{e(n)}</b><span>{e(l)}</span></div>"
        for n, l in (c.get("kpis") or [])[:4])
    box_border = f"border-inline-start:4px solid {d['box_rule']}" if d["id"] != 3 else f"border:1px solid {d['box_rule']}"
    cover = (f"<div class='page cover' style='background:{d['cover_bg']};color:{d['cover_ink']}'>"
             f"<div class='t' style='font-family:{d['head_font']};font-weight:{max(d['head_weight'], 400)}'>{e(c.get('title', ''))}</div>"
             f"<div class='s'>{e(c.get('subtitle', ''))}</div><div class='band' style='background:{d['cover_band']}'></div>"
             f"<div class='d'>{e(c.get('date', ''))}</div></div>")
    content = (f"<div class='page content' style='color:{d['ink']}'>"
               f"<h3 style='{head};{rule}'>{e(c.get('heading', ''))}</h3>"
               + (f"<h4 style='color:{acc}'>{e(c['subheading'])}</h4>" if c.get("subheading") else "")
               + f"<p>{e(c.get('paragraph', ''))}</p>"
               + (f"<div class='box' style='background:{d['box_bg']};{box_border}'>{e(c['box'])}</div>" if c.get("box") else "")
               + (f"<table><tr style='{head_style}'>{thead}</tr>{tbody}</table>" if rows else "")
               + (f"<div class='tiles'>{tiles}</div>" if tiles else "") + "</div>")
    return cover + content


def main():
    ap = argparse.ArgumentParser(description="Render a Persian document in several design directions.")
    ap.add_argument("--content", help="sample.json with the real title, heading, paragraph, table, kpis")
    ap.add_argument("--only", help="comma-separated direction ids, e.g. 2,4")
    ap.add_argument("--out", default="nasr-design.html")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    if a.list:
        print(json.dumps(DIRECTIONS, ensure_ascii=False, indent=1))
        return
    if not a.content:
        sys.exit("--content is required (see the docstring for its shape)")
    c = json.loads(Path(a.content).read_text(encoding="utf-8"))
    dirs = [d for d in DIRECTIONS if not a.only or str(d["id"]) in a.only.split(",")]
    body = "".join(
        f"<section class='dir'><h2>گزینه‌ی {'۰۱۲۳۴۵۶۷۸۹'[d['id']]} · {html.escape(d['name'])}</h2>"
        f"<div class='for'>مناسب برای {html.escape(d['for'])}</div><div class='pages'>{page_html(d, c)}</div></section>"
        for d in dirs)
    page = (f"<!doctype html><html lang='fa' dir='rtl'><head><meta charset='utf-8'>"
            f"<meta name='viewport' content='width=device-width, initial-scale=1'><title>گزینه‌های طراحی</title>"
            f"<style>{CSS.replace('%(f)s', FONTS)}</style></head><body><div class='intro'><h1>گزینه‌های طراحی سند</h1>"
            f"<p>هر گزینه یک جلد و یک صفحه‌ی متن از همین سند است. یکی را انتخاب کنید یا بگویید از کدام چه چیزی را می‌خواهید.</p></div>"
            f"{body}</body></html>")
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    tok = out.with_suffix(".tokens.json")
    tok.write_text(json.dumps(dirs, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {out}\nwrote {tok}")


if __name__ == "__main__":
    for _stream in (sys.stdout, sys.stderr):
        try:
            _stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    main()
