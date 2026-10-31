# nasr (نثر)

**از مفهوم تا متن نهایی: سبک‌های نثر فارسی و اسناد راست‌چین برای هوش مصنوعی**
**Persian prose styles and RTL documents for Claude and any AI agent**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Claude Skill](https://img.shields.io/badge/Claude-Skill-cc785c)](https://claude.ai)
[![Works with any agent](https://img.shields.io/badge/agents-any-blue)](AGENTS.md)
[![Fonts: Vazirmatn + Lalezar](https://img.shields.io/badge/fonts-Vazirmatn%20%2B%20Lalezar-8A2BE2)](references/fonts.md)

<div dir="rtl">

## نثر چه می‌کند

متن فارسیِ هوش مصنوعی معمولاً یا بوی ماشین می‌دهد (می‌باشد، سه‌گانه‌ها، خط تیره)
یا کوتاه و بریده است: جمله‌های پنج‌شش‌کلمه‌ای پشت هم، بی‌آن‌که فکری را پیش ببرند.
نثر این مهارت را به هوش مصنوعی می‌دهد که پیش از نوشتن بفهمد متن قرار است چه بگوید،
چند سبک برای گفتنش پیشنهاد کند و متن را تا نسخه‌ی نهایی و فایل تحویلی پیش ببرد.

گردش کار چهار مرحله دارد:

۱. **فهم مفهوم.** جمله‌ای که خواننده باید به خاطر بسپارد، مخاطب، غایت و مصالح
   (واقعیت، عدد، تجربه، نقل‌قول). خروجی این مرحله یک «برداشت من» چندخطی است و
   حداکثر سه پرسش. کمبود مصالح همین‌جا با پرسیدن یا جست‌وجو جبران می‌شود، نه با
   ساختن.
۲. **پیشنهاد سبک.** دو تا چهار کارت سبک که دست‌کم در یک محور با هم فرق دارند؛
   ترکیب سبک‌ها هم مجاز است.
۳. **متن نمونه** (در صورت نیاز). پاراگراف آغازین هر کارت روی همان واقعیت‌ها، تا
   تفاوت فقط در سبک دیده شود.
۴. **نگارش نهایی.** پیش‌نویس، بررسی واقعیت‌ها، سنجش آهنگ با `style_check.py`،
   ویرایش نگارشی با `persian_cleanup.py` و `fa_lint.py`، و تحویل در قالب
   خواسته‌شده: Word، PDF، HTML یا اسلاید.

### سبک‌ها از کجا آمده‌اند

سبک‌ها حدس نیستند. هر سبک روی چهار محور مستقل تعریف شده و هر محور یک معیار دارد:
غایت (گزارش، تبیین، اقناع، فراخوان، یادمان)، شاهد غالب (تجربه، واقعیت جاری، تاریخ،
مفهوم، مرجع)، جایگاه (من، ما، بیرونی) و ساخت (زمانی، زنجیره‌ای، فهرستی، تقابلی،
شاخه‌ای). سیزده «نسخه» مثل جدل، توجیه راهبردی، تحلیل مفهومی، روایت شاهد، گزارش
داده‌محور برند و گزارش نهادی ترکیب‌های رایج همین محورها هستند.

آهنگ متن (طول جمله و پاراگراف، تراکم ربط‌ها) جداگانه انتخاب می‌شود. هفت نیم‌رخ آهنگ
از سنجش ۶۲۰ متن امضادار نُه نویسنده و ستون‌نویس فارسی و یازده گزارش سالانه و
پایداری شرکت‌های ایرانی ساخته شده است. روش، آزمون‌های کور و محدودیت‌ها در
[`references/style-evidence.md`](references/style-evidence.md) آمده است. هیچ متنی
از منابع در این مخزن بازتولید نشده؛ فقط سنجه‌ها و مثال‌های ساختگی.

همه‌ی مقسم‌ها و دسته‌بندی‌ها، مرزهایشان و دلیل همپوشانی نداشتنشان در
**[راهنمای دسته‌بندی‌های نثر](GUIDE.fa.md)** آمده است.

</div>

## Built on persian-writing

nasr is an extended edition of
[**persian-writing**](https://github.com/ali2000hos/persian-writing) by
ali2000hos and contributors (MIT). Everything in it is kept: register detection,
Persian AI-tell removal, orthography, the paknevis + davat cleanup toolkit, RTL
fixes for Word/PDF/PowerPoint/HTML/Excel/images, the verifiers and the bundled
fonts. nasr adds the writing workflow and the evidence-based style layer on top.
The upstream history is preserved in this repository.

## What it does

| Layer | Coverage |
|---|---|
| **Writing workflow** (nasr) | concept → 2–4 style cards → optional opening samples → draft, checks and delivery (references/writing-workflow.md) |
| **Prose styles** (nasr) | four axes, 13 recipes, 7 rhythm profiles measured on real Persian prose; `style_check.py` measures a draft against its band |
| **Register detection** | ۶-step procedure: رسمی / اداری / محاوره / علمی — classifies the deliverable, not the request tone; asks when stakes are high |
| **De-AI-ing (humanizer-fa)** | 18 Persian AI-tell patterns with before/after fixes، مکانیزم زیربنایی، و گزارش ریتم جمله |
| **Orthography** | نیم‌فاصله (ZWNJ)، ی/ک فارسی، اعداد فارسی، «گیومه»، کسره‌ی اضافه، **هکسره** |
| **Cleanup toolkit** | paknevis + davat merged: `--edit`, `--preset persian`, spell-check against a 453K-word frequency dictionary — zero dependencies |
| **RTL documents** | Word/docx (START-not-RIGHT, `bidi`, `cs` fonts), pagination (keepNext, cantSplit, no blank pages), PDF verification, PowerPoint, HTML/CSS/email, Excel (`rightToLeft`), images (PIL raqm) |
| **Academic** | نگارش علمی: structure, citations without fabrication, formulas/stats LTR |
| **Content craft** | POV discipline، آموزش vs تبلیغ، الگوهای بدنه، وفاداری به منبع |
| **Social channels** | تلگرام و اینستاگرام: قالب، هوک، کاروسل، ریلز، استوری، کپشن، بازطراحی |
| **SEO + copywriting** | Search intent, Persian keyword variants, E-E-A-T, doorway-page warning, PAS/AIDA, CTA per register, «قیمت همیشه با تومان» |
| **Fonts** | Vazirmatn (5 weights) + Lalezar bundled (SIL OFL); catalog & pairings for 8 families |

## Install

**Claude.ai / Cowork:** zip this folder as `nasr.skill` (or download it from
[Releases](../../releases)) → open in Claude → **Save skill**.

**Claude Code:**
```bash
git clone https://github.com/mohsenkhan-dev/nasr ~/.claude/skills/nasr
```
or as a plugin: `/plugin marketplace add mohsenkhan-dev/nasr`, then `/plugin install nasr@nasr`.
Installed under `~/.claude/skills/`, it is available in every project.
Do not keep persian-writing installed next to it: both trigger on Persian text.

**Cursor / Windsurf / other agents:** clone into your repo (e.g.
`skills/nasr/`) and add one rule line:
`For any Persian/Farsi task, read skills/nasr/SKILL.md and follow it.`
See [AGENTS.md](AGENTS.md).

**ChatGPT / Gemini / chat-only AIs:** upload
[`universal/nasr-universal.md`](universal/nasr-universal.md)
as knowledge (GPTs / Projects / Gems) — the whole skill in one self-contained file.

**No AI at all (plain CLI):**
```bash
python3 scripts/persian_cleanup.py --edit --spellcheck draft.txt   # fix + spell-check
python3 scripts/fa_lint.py --check draft.txt                       # lint report
python3 scripts/verify_docx.py out.docx --fix --sanitize            # DOCX RTL + integrity
python3 scripts/verify_pdf.py out.pdf --expect-font Vazirmatn      # PDF QA
python3 scripts/style_check.py draft.md --recipe "جدل"              # rhythm vs profile
```
Python 3.8+, standard library only.

## Before / after (one of 18 patterns)

> ❌ در دنیای امروز، داشتن وب‌سایت از اهمیت ویژه‌ای برخوردار می‌باشد و نقش
> بسزایی در جذب مشتریان ایفا می‌کند.
>
> ✅ مشتری قبل از این‌که به شما زنگ بزند، اسمتان را گوگل می‌کند. اگر چیزی
> پیدا نکند، سراغ رقیبتان می‌رود.

## Package layout

```
SKILL.md                 entry point: routing + non-negotiables
AGENTS.md                guidance for any AI agent
references/              writing-workflow, style-framework, style-moves, style-evidence,
                         writing-style, orthography, content-structures, academic,
                         social-channels, seo-copywriting, fonts, docx-pdf, pptx,
                         html-css, format-skills-fa, cleanup/
scripts/                 persian_cleanup, fa_lint, style_check, verify_docx, verify_pdf,
                         check_version, install_fonts, download_fonts, build_universal
assets/                  fonts (TTF), 453K-word dictionary, style_profiles.json
universal/               single-file edition for chat-only AIs
.claude-plugin/          Claude Code plugin manifests
evals/                   regression test prompts
```

After editing SKILL.md or references, regenerate the single-file edition:
`python3 scripts/build_universal.py`

## Version history

- **2.2.0** — think in the style before writing in it. New
  references/style-skeletons.md: the thinking skeleton of every recipe (slots
  to fill with real content, where the payoff goes, a fit test), with a strategy
  skeleton built on diagnosis, crux, guiding policy with its trade-off, and
  coherent actions. The workflow gains stage 2b (build the skeleton before
  drafting) and a calibration procedure: one short sample per suitable style
  with its essence and skeleton, judged «درآمده / نیمه / درنیامده». New writing
  rules from that test: think in Persian collocations, colons only before a list
  or quotation, plain headings, no announcing paragraph openers.
  fa_lint now flags colons in headings, question headings, mid-sentence colons
  and announcing openers.
- **2.1.0** — moving between styles in long texts, and the rewrite path.
  Long documents now get a section map: each section takes its own style,
  moves to a near style at each boundary (neighbouring rhythm profiles, at
  most one or two axes changed) and declares it with `<!-- سبک: … -->`;
  `style_check.py --sections` measures every section against its own profile
  and flags jumps between non-neighbours. Default section maps for strategy
  documents, brand and sustainability reports and long columns. New
  provisional recipe سند راهبردی. Rewriting an existing document has its own
  path: faithful extraction, measuring the original, a list of
  inconsistencies for the user, a rewrite under the same facts, and a
  side-by-side comparison. style_check skips captions, table rows and HTML
  comments. New Persian guide to every axis and category: GUIDE.fa.md.
- **2.0.0** — nasr. Renamed and published as its own repository. New writing
  workflow (references/writing-workflow.md): understand the concept and show a
  short restatement, propose two to four style cards that differ on an axis,
  write opening samples on the same facts when the choice is hard, then draft,
  check (facts, style_check, cleanup, lint, read-aloud) and deliver. Depth
  scales with the job: short transactional texts skip it. The single-file
  edition now includes the workflow and the style framework.
- **1.5.0** — prose styles from evidence. A new style layer for columns,
  analyses, essays and corporate reports. Each style is described on four axes,
  each with a single criterion: purpose, dominant evidence, position, and
  structure. Named recipes (جدل، توجیه راهبردی، روایت شاهد، گزارش داده‌محور
  برند، گزارش نهادی…) are common combinations, and long texts can combine them
  section by section. Rhythm is chosen separately, from seven profiles built
  from a reference corpus of 620 signed texts by nine Persian writers and
  eleven Iranian annual and sustainability reports. New files:
  references/style-framework.md (choosing, combining, the style card),
  references/style-moves.md (signature moves, invented examples),
  references/style-evidence.md (corpus, tests, limits),
  scripts/style_check.py (measure a draft against a profile) and
  assets/style_profiles.json. The formal-but-human rule «short sentences» now
  applies to proposals and web copy only; analytical prose follows its profile.
- **1.4.0** — source-faithful academic paraphrase. Rewriting a paper into a
  thesis chapter now follows one rule: change wording and structure only. No
  inference or bridging link is added, nothing is dropped, and every qualifier
  keeps its strength: a mapping table for approximately, mainly, may, suggest,
  up to, at least, significantly and more, plus the four drifts that change a
  finding (rounding, hardening, softening, scope creep). The researcher's own
  reasoning is marked «این بخش در مقاله وجود ندارد» rather than folded in, and
  a four-question fidelity check runs before handover (academic.md §5.5). Also
  new: instruction-residue and decorative-vocabulary tells, list-vs-prose rules
  for thesis parts, and §7.5 on house style. A department's banned-word list is
  honoured, but never at the cost of a hedge the source has, and a negative
  finding is never rewritten as a positive one. The linter no longer reads
  section references (§5.5) as Latin digits.
- **1.3.9** — Persian text that mixes in English words no longer renders
  backwards. Chat apps, GitHub, Telegram and most editors set a paragraph's
  direction from its first letter, so a Persian line opening with a Latin word
  («React یک کتابخانه است.») displayed left-to-right: wrong alignment, the
  period on the wrong side, words scrambled. New non-negotiable rule: every
  Persian sentence, bullet, heading and table cell starts with a Persian word
  («کتابخانه‌ی React…»), with a full guide in orthography.md §9.
  `fa_lint.py` reports offending lines as `bidi-start`, and the new opt-in
  `persian_cleanup.py --bidi` adds an invisible RLM (U+200F) to exactly those
  lines for plain-text output. It skips code and English lines, is idempotent,
  and is never applied by default. Reported by
  [@aliamini587](https://github.com/aliamini587) in
  [#4](https://github.com/ali2000hos/persian-writing/issues/4).
- **1.3.8** — `--edit` stopped corrupting the non-prose inside Persian
  documents. URLs (`?lang=fa` became `؟lang=fa`), email addresses, IBANs,
  international phone numbers, software versions, DOIs and English citations
  are now protected before the typographic pass, so their digits and
  punctuation stay exact. Fixed: ezafe on a final ه produced a doubled heh
  (`خانهۀ` → `خانهٔ`); the prepositions بی/در/بر were fused onto verbs
  (`در گفتن` → `درگفتن`); `أ` and `ؤ` were stripped of hamza, turning
  standard spellings like مؤلف، تأکید، سؤال into nonstandard ones; «تر و تازه»
  got a ZWNJ; commas inside numbers now become the Persian thousands separator
  (`۴٬۷۵۰٬۰۰۰`); deliberate wide spacing (signature lines, aligned columns)
  survives. `fa_lint.py` shares the same protected regions, no longer flags
  -انه adverbs (همکارانه) as هکسره, and skips the rhythm warning on technical
  text. `verify_docx.py` reads style-level `w:rtl`/`w:cs`/`w:szCs` from
  `styles.xml`, and `verify_pdf.py` ignores en-dashes in numeric ranges.
  First test suite added under `tests/`. Contributed by
  [@nimagh-18](https://github.com/nimagh-18) in
  [#3](https://github.com/ali2000hos/persian-writing/pull/3).
- **1.3.7** — the linter stopped crying wolf. Unicode codepoint notation
  (`U+06CC`) was reported as Latin digits and rewritten by `convert_digits`
  into `U+۰۶CC`, which damaged the typography documents this toolkit exists
  for. Persian rules are now scoped to Persian prose: an em dash or Latin
  comma is flagged only between two Persian words, so bilingual glosses and
  English sentences quoting a Persian term are left correct instead of being
  reworded. Deliberate error examples can be marked with
  `<!-- fa-lint-ignore-next-line -->` or a `…-start`/`…-end` block, and `--fix`
  restores them instead of quietly repairing them. Also fixed: `--fix` glued
  punctuation onto Markdown list markers (`- !` → `-!`), and the dictionary is
  now located by search rather than one hardcoded path, so the scripts work
  from any call site while the repository keeps a single copy. Across the
  bundled docs, reported issues fell from 246 to 73 with no rule weakened;
  `references/orthography.md` now passes clean. The codepoint bug was found and
  fixed by [@bbmo9892-cpu](https://github.com/bbmo9892-cpu) in
  [#2](https://github.com/ali2000hos/persian-writing/pull/2). New
  `CONTRIBUTING.md` documents the design contract.
- **1.3.6** — `--edit` no longer damages structured files. Code fences, inline
  code and table rows are now lifted out before the typographic pass and
  restored unchanged, and leading indentation is preserved. Previously the
  Persian rules ran over everything: straight quotes inside a code block became
  «guillemets» (breaking the code), ASCII digits became Persian, and collapsing
  runs of spaces flattened both indentation and table alignment. Verified across
  four real reference files and nine edge cases; the pass is idempotent.
- **1.3.5** — fixed a silent structure-destroying bug: `persian_cleanup.py --edit`
  used `\s` in its punctuation-spacing rules, and since `\s` matches newlines, a
  sentence-ending period followed by a blank line collapsed into one line. Running
  it on a Markdown file merged paragraphs and folded lists into prose. Both rules
  now use `[ \t]`, a trailing newline is preserved, and the behaviour is verified
  against a real reference file (line count, blank lines, headings and table rows
  all unchanged). Repo banner added.
- **1.3.0** — the mechanism behind AI-sounding prose (predictability and uniformity),
  measured on the bundled samples, plus `fa_lint.py --rhythm` for sentence-rhythm
  hints; evidence on AI-detector unreliability and its heavy bias against
  second-language writers, with an explicit boundary: this skill improves writing
  and never helps disguise authorship.
- **1.2.0** — content craft from professional editorial practice: point-of-view
  discipline (impersonal / second person / «ما»), separation of teaching from
  selling, the واقعیت-نظر-پیش‌بینی-ادعا distinction and source-fidelity rules,
  six body patterns for educational content, and a Telegram/Instagram module
  (formats, hooks, carousels, reels, stories, captions, repurposing, and the
  bidi reason the first word after an emoji must be Persian).
- **1.1.0** — هکسره detection (ezafe kasre vs the colloquial «ـه» clitic) with a
  dictionary-backed linter in both directions; OOXML package-integrity validation
  (Content_Types ordering, dangling relationships, malformed XML, control chars)
  and `--sanitize` to strip the Word-for-Mac template artifacts python-docx
  inherits — the classic "file is corrupt" fingerprint. Repairs are validated
  before replacing the original.
- **1.0.2** — verified RTL fixes: section-level `<w:bidi/>` position (silent column reversal), built-in list numbering producing Latin digits, Word template heading colors, font fallback. New `scripts/verify_docx.py` with `--fix`.
- **1.0.0** — initial release: 4 registers + detection procedure, 18 AI-tell
  patterns, paknevis+davat cleanup with frequency-ranked spell-check, RTL
  recipes for docx/pptx/html/xlsx/images, PDF verification, academic + SEO +
  copywriting modules, Vazirmatn/Lalezar bundled. Benchmarked at 100% vs 79%
  (with/without skill) on register, orthography and RTL-structure assertions.

## Credits & license

MIT — see [LICENSE](LICENSE). Fonts under SIL OFL: [Vazirmatn](https://github.com/rastikerdar/vazirmatn)
and the rastikerdar family, [Lalezar](https://github.com/BornaIz/Lalezar) by
Borna Izadpanah. Cleanup toolkit merges [paknevis](https://github.com/afshin-ir/paknevis)
(afshin-ir) and [davat](https://github.com/mh-salari/davat) (mh-salari);
dictionary from [Persian-Words-Database](https://github.com/shahind/Persian-Words-Database).
AI-tell patterns adapted for Persian from Wikipedia's
["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
via the [humanizer](https://github.com/blader/humanizer) skill. E-E-A-T and
quality-gate principles adapted from [claude-seo](https://github.com/AgriciDaniel/claude-seo).

## Sponsor

Thanks to [ParsPack (پارس‌پک)](https://parspack.com/) for supporting this project.
