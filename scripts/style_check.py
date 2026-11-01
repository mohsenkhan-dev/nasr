#!/usr/bin/env python3
"""
style_check.py — measure a Persian draft against a rhythm profile.

The profiles (assets/style_profiles.json) hold the 20th/50th/80th percentile of
each feature across the reference corpus described in references/style-evidence.md.
A feature outside the 20–80 band is reported with the direction to move it.
The features are defined exactly as in the corpus build, so the comparison is fair.

Usage:
  python3 style_check.py draft.md --profile "استدلالی پیوسته"
  python3 style_check.py draft.md --recipe "گزارش داده‌محور برند"   # uses the recipe's default profile
  python3 style_check.py draft.md --compare                          # nearest profile for an existing text
  python3 style_check.py report.md --sections                        # each section against its own style
  python3 style_check.py --list

Long texts move between styles section by section (style-framework.md §5).
With --sections the file is split at its Markdown headings (## by default,
--level to change) and each section is measured on its own. A section declares
its style with a comment right under its heading:
  <!-- سبک: گزارشی برند -->        (a profile)
  <!-- سبک: گزارش داده‌محور برند --> (or a recipe)
Undeclared sections fall back to --profile/--recipe, or get their nearest
profiles. Sections under 60 words are listed but not measured.

Captions (a line in *italics*, or starting «تصویر ۲:»، «جدول ۱:»، «نمودار»،
«شکل»), Markdown table rows and HTML comments are not prose and are skipped.

Exit code: 0 = all core features inside the band, 1 = something to revise.
Python 3.8+, standard library only.
"""
import argparse, json, re, statistics as st, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROFILES = json.loads((ROOT / "assets" / "style_profiles.json").read_text(encoding="utf-8"))["profiles"]

# recipe → default rhythm profile (references/style-framework.md §2)
RECIPE_PROFILE = {
    "تحلیل مفهومی": "تحلیلی میانه", "توجیه راهبردی": "تحلیلی میانه", "عبرت تاریخی": "تحلیلی میانه",
    "استدلال روزنامه‌ای": "استدلالی پیوسته", "جدل": "استدلالی پیوسته",
    "روایت شاهد": "گفت‌وگویی شخصی", "توضیح و آموزش": "گفت‌وگویی شخصی", "تأمل شخصی": "گفت‌وگویی شخصی",
    "سوگ‌نامه": "گفت‌وگویی شخصی", "خطابه": "خطابی",
    "گزارش داده‌محور برند": "گزارشی برند", "گزارش نهادی": "گزارشی نهادی", "خبر کوتاه": "فشرده",
    "سند راهبردی": "تحلیلی میانه",
}
FA_WORD = re.compile(r"[؀-ۿ]+(?:‌[؀-ۿ]+)*")
CONNECTIVES = ["اما", "ولی", "با این حال", "با این همه", "در حالی که", "حال آنکه", "چون", "زیرا", "چرا که",
               "از آنجا که", "به دلیل", "به خاطر", "بنابراین", "پس", "از این رو", "در نتیجه", "به همین دلیل",
               "به همین جهت", "لذا", "یعنی", "به عبارت دیگر", "به بیان دیگر", "البته", "به‌ویژه", "به ویژه",
               "بالاخص", "مثلا", "مثلاً", "برای نمونه", "همچنین", "علاوه بر این", "افزون بر", "نیز", "حتی",
               "از سوی دیگر", "از یک سو", "وانگهی"]
BUREAUCRATIC = ["می‌باشد", "می‌باشند", "گردید", "گردیده", "گردد", "نمود", "نموده", "نماید", "نمایند",
                "در راستای", "مبادرت", "صورت پذیرفت"]
CORE = ["sent_median", "para_words", "conn_k", "ke_per_sent", "comma_per_sent", "short_pct", "long_pct"]
LABEL = {
    "sent_median": "میانه‌ی طول جمله (کلمه)", "para_words": "میانه‌ی طول پاراگراف (کلمه)",
    "conn_k": "واژه‌ی ربط در هزار کلمه", "ke_per_sent": "«که» در هر جمله", "comma_per_sent": "ویرگول در هر جمله",
    "short_pct": "جمله‌ی زیر ۱۰ کلمه (٪)", "long_pct": "جمله‌ی بالای ۳۰ کلمه (٪)", "q_pct": "جمله‌ی پرسشی (٪)",
    "digits_k": "عدد در هزار کلمه", "formal_k": "فعل و قالب اداری در هزار کلمه",
}
ADVICE = {
    ("sent_median", "low"): "جمله‌های کوتاه پشت سر هم را با ربط یا بند وابسته به هم وصل کن.",
    ("sent_median", "high"): "جمله‌های بلند را در جای «و» یا «که» بشکن.",
    ("para_words", "low"): "پاراگراف‌های کوتاه را که یک فکر را ادامه می‌دهند یکی کن؛ پاراگراف تک‌جمله‌ای فقط یک بار.",
    ("para_words", "high"): "پاراگراف را در جایی که فکر عوض می‌شود بشکن.",
    ("conn_k", "low"): "پیوند جمله‌ها را آشکار کن: اما، چون، بنابراین، یعنی.",
    ("conn_k", "high"): "ربط اضافه را حذف کن؛ جاهایی که رابطه روشن است ربط لازم ندارد.",
    ("ke_per_sent", "low"): "جایی که دو جمله‌ی کوتاه یک مرجع دارند، با «که» یکی‌شان کن.",
    ("ke_per_sent", "high"): "زنجیره‌ی «که»ها را با شکستن جمله باز کن.",
    ("comma_per_sent", "low"): "در شمارش‌ها و بندهای هم‌پایه ویرگول بگذار.",
    ("comma_per_sent", "high"): "فهرست‌های بلند داخل جمله را به جمله‌های جدا یا فهرست تبدیل کن.",
    ("short_pct", "high"): "جمله‌های خیلی کوتاه زیادند؛ متن تکه‌تکه خوانده می‌شود.",
    ("long_pct", "high"): "جمله‌های بالای ۳۰ کلمه زیادند؛ بعضی را بشکن.",
}


def count_phrase(t, ph):
    tail = r"(?!\s+از)" if ph == "پس" else ""  # «پس از» means "after", not "therefore"
    return len(re.findall(r"(?<![؀-ۿ‌])" + re.escape(ph) + r"(?![؀-ۿ‌])" + tail, t))


def sentences(t):
    parts = re.split(r"(?<=[.!؟?…])\s+|\n", t)
    return [p for p in (s.strip() for s in parts) if len(FA_WORD.findall(p)) >= 2]


CAPTION = re.compile(r"^\s*(?:[*_][^*_\n].*[*_]|(?:تصویر|جدول|نمودار|شکل)\s*[0-9۰-۹]+\s*[:：.].*)\s*$", re.M)
LIST_MARK = "⁣"  # invisible separator: marks a former list item


def strip_markup(t):
    t = re.sub(r"```.*?```", " ", t, flags=re.S)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"^\s*\|.*\|\s*$", "", t, flags=re.M)  # Markdown table rows
    t = CAPTION.sub("", t)  # captions are labels, not paragraphs
    t = re.sub(r"^\s{0,3}#{1,6}\s+.*$", "", t, flags=re.M)  # headings are not paragraphs
    # list items keep a mark: a one-sentence bullet is normal, a one-sentence paragraph is not
    t = re.sub(r"^\s*([-*•>]|\d+[.)]|[۰-۹]+[.)-])\s+", LIST_MARK, t, flags=re.M)
    return re.sub(r"\n\s*\n", "\n", t)


def measure(txt):
    ss = sentences(txt)
    words = FA_WORD.findall(txt)
    if len(ss) < 3 or len(words) < 60:
        raise ValueError("متن برای سنجش کوتاه است: دست‌کم ۶۰ کلمه و ۳ جمله لازم است.")
    L = [len(FA_WORD.findall(s)) for s in ss]
    k = 1000 / len(words)
    paras = [p for p in txt.split("\n") if len(FA_WORD.findall(p)) >= 8]
    one_sentence = sum(1 for p in paras if not p.startswith(LIST_MARK) and len(sentences(p)) == 1)
    anchored = sum(1 for p in paras if re.search(r"[0-9۰-۹]|«[^»]+»|\b[A-Z][a-zA-Z]+", p))
    return {
        "sent_median": st.median(L), "para_words": st.median([len(FA_WORD.findall(p)) for p in paras]) if paras else 0,
        "conn_k": sum(count_phrase(txt, c) for c in CONNECTIVES) * k, "ke_per_sent": count_phrase(txt, "که") / len(ss),
        "comma_per_sent": txt.count("،") / len(ss), "short_pct": 100 * sum(x < 10 for x in L) / len(L),
        "long_pct": 100 * sum(x > 30 for x in L) / len(L), "q_pct": 100 * sum("؟" in s for s in ss) / len(ss),
        "digits_k": len(re.findall(r"[0-9۰-۹]+", txt)) * k,
        "formal_k": sum(count_phrase(txt, f) for f in BUREAUCRATIC) * k,
        "_words": len(words), "_paras": len(paras), "_one_sentence_paras": one_sentence,
        "_anchored_paras": anchored,
    }


def fa(x):
    s = f"{x:.2f}".rstrip("0").rstrip(".") if isinstance(x, float) else str(x)
    return s.translate(str.maketrans("0123456789.", "۰۱۲۳۴۵۶۷۸۹٫"))


def report(m, name):
    prof = PROFILES[name]
    rng = prof["ranges"]
    print(f"آهنگ: {name}  (پایه: {fa(prof['n_texts'])} متن{'، تأییدنشده' if prof.get('validated') is False else ''})")
    print(f"متن: {fa(m['_words'])} کلمه، {fa(m['_paras'])} پاراگراف\n")
    # In a short text one sentence moves every percentage a lot; chasing each band then swings the
    # draft from one extreme to the other. Below 400 words, only clear deviations count as issues.
    short = m["_words"] < 400
    if short:
        print("متن کوتاه است: عددها پرنوسان‌اند و فقط انحراف آشکار (بیش از یک‌چهارم پهنای بازه) ایراد شمرده می‌شود.\n")
    issues = 0
    for f in CORE + ["q_pct", "digits_k", "formal_k"]:
        if f not in rng:
            continue
        lo, mid, hi = rng[f]
        v = m[f]
        slack = 0.25 * (hi - lo) if short else 0.0
        state = "low" if v < lo - slack else ("high" if v > hi + slack else "ok")
        near = state == "ok" and not lo <= v <= hi
        mark = "≈ نزدیک مرز" if near else {"ok": "✓", "low": "↓ کم", "high": "↑ زیاد"}[state]
        print(f"  {LABEL[f]:32s} {fa(round(v, 2)):>7s}   بازه {fa(lo)}–{fa(hi)} (میانه {fa(mid)})   {mark}")
        if state != "ok" and f in CORE:
            issues += 1
            if (f, state) in ADVICE:
                print(f"      ← {ADVICE[(f, state)]}")
    notes = []
    if m["_one_sentence_paras"] > 1:
        notes.append(f"{fa(m['_one_sentence_paras'])} پاراگراف تک‌جمله‌ای: بیش از یکی، متن را بریده‌بریده نشان می‌دهد.")
    if m["_paras"] and m["_anchored_paras"] / m["_paras"] < 0.5 and name not in ("خطابی",):
        notes.append("کمتر از نیمی از پاراگراف‌ها عدد، نام یا نقل‌قول دارند؛ جزئیات مشخص بیفزای (style-framework.md §7).")
    if m["formal_k"] > 2 and name != "گزارشی نهادی":
        notes.append("قالب‌های اداری (می‌باشد، گردید، نموده، در راستای) زیادند؛ با است، شد، کرده، برای عوض کن.")
    if notes:
        print("\nنکته‌ها:")
        for n in notes:
            print("  • " + n)
    return issues


def nearest(m):
    def dist(name):
        rng = PROFILES[name]["ranges"]
        d = 0.0
        for f in CORE:
            if f in rng:
                lo, mid, hi = rng[f]
                d += abs(m[f] - mid) / max(1e-6, hi - lo)
        return d
    return sorted(PROFILES, key=dist)


def profile_distance(a, b):
    """Distance between two profiles' medians, in band widths: used for neighbours."""
    ra, rb = PROFILES[a]["ranges"], PROFILES[b]["ranges"]
    fs = [f for f in CORE if f in ra and f in rb]
    return sum(abs(ra[f][1] - rb[f][1]) / max(1e-6, (ra[f][2] - ra[f][0] + rb[f][2] - rb[f][0]) / 2) for f in fs) / len(fs)


def neighbours(name, k=2):
    return sorted((p for p in PROFILES if p != name), key=lambda p: profile_distance(name, p))[:k]


DECL = re.compile(r"<!--\s*(?:سبک|style)\s*:\s*(.+?)\s*-->")


def resolve(name):
    name = (name or "").strip()
    return name if name in PROFILES else RECIPE_PROFILE.get(name)


def split_sections(txt, level):
    head = re.compile(r"^#{1,%d}\s+(.+)$" % level, re.M)
    marks = list(head.finditer(txt))
    out = []
    if marks and txt[:marks[0].start()].strip():
        out.append(("(پیش از نخستین سرفصل)", txt[:marks[0].start()]))
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(txt)
        out.append((m.group(1).strip(), txt[m.end():end]))
    return out or [("(کل متن)", txt)]


def run_sections(txt, level, default):
    rows, issues, prev = [], 0, None
    for title, body in split_sections(txt, level):
        d = DECL.search(body)
        declared = resolve(d.group(1)) if d else None
        if d and not declared:
            print(f"⚠ «{d.group(1)}» نه آهنگ است نه نسخه؛ بخش «{title}» بی‌اعلام سنجیده می‌شود.")
        try:
            m = measure(strip_markup(body))
        except ValueError:
            rows.append((title, None, declared, None))
            continue
        name = declared or default
        print("─" * 60)
        print(f"بخش: {title}")
        if name:
            n = report(m, name)
            issues += n
        else:
            order = nearest(m)
            print("بی‌اعلام؛ نزدیک‌ترین آهنگ‌ها:", "، ".join(order[:2]))
            print()
            n = report(m, order[0])
            name = order[0]
        if prev and prev != name and name not in neighbours(prev, 3):
            print()
            print(f"  ↔ پرش از «{prev}» به «{name}»: این دو همسایه نیستند؛ با یک جمله‌ی پل یا یک بخش میانی گذار را نرم کن.")
        rows.append((title, m["_words"], name, n))
        prev = name
    print("═" * 60)
    print("نقشه‌ی سبک بخش‌ها:")
    for title, w, name, n in rows:
        if w is None:
            print(f"  {title[:40]:40s}  کوتاه، سنجیده نشد")
        else:
            print(f"  {title[:40]:40s}  {fa(w):>6s} کلمه  {name:16s}  {'✓' if not n else fa(n) + ' ایراد'}")
    return issues


def main():
    ap = argparse.ArgumentParser(description="Measure a Persian draft against a rhythm profile.")
    ap.add_argument("file", nargs="?", help="draft file (Markdown or plain text); '-' for stdin")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--profile", help="rhythm profile name")
    g.add_argument("--recipe", help="recipe name; its default profile is used")
    g.add_argument("--compare", action="store_true", help="rank profiles by closeness")
    ap.add_argument("--list", action="store_true", help="list profiles and recipes")
    ap.add_argument("--sections", action="store_true", help="measure each section against its declared style")
    ap.add_argument("--level", type=int, default=2, help="deepest heading level that starts a section (default 2)")
    a = ap.parse_args()
    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    if a.list:
        print("آهنگ‌ها:", "، ".join(PROFILES))
        print("نسخه‌ها:", "، ".join(f"{r} → {p}" for r, p in RECIPE_PROFILE.items()))
        print("همسایه‌ها (نزدیک‌ترین آهنگ‌ها برای گذار بین بخش‌ها):")
        for p in PROFILES:
            print(f"  {p}: " + "، ".join(neighbours(p)))
        return 0
    if not a.file:
        ap.error("file is required")
    txt = sys.stdin.read() if a.file == "-" else Path(a.file).read_text(encoding="utf-8")
    if a.sections:
        default = a.profile or RECIPE_PROFILE.get(a.recipe or "")
        return 1 if run_sections(txt, a.level, default) else 0
    try:
        m = measure(strip_markup(txt))
    except ValueError as e:
        sys.exit(str(e))
    if a.compare:
        order = nearest(m)
        print("نزدیک‌ترین آهنگ‌ها:", "، ".join(order[:3]), "\n")
        return report(m, order[0]) and 1
    name = a.profile or RECIPE_PROFILE.get(a.recipe or "", None)
    if a.recipe and not name:
        ap.error(f"recipe not found: {a.recipe}")
    if not name:
        ap.error("give --profile, --recipe or --compare")
    if name not in PROFILES:
        ap.error(f"profile not found: {name}")
    return 1 if report(m, name) else 0


if __name__ == "__main__":
    sys.exit(main())
