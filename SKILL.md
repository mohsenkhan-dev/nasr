---
name: nasr
description: >
  Write natural Persian (Farsi) prose and build correct right-to-left Persian
  deliverables. For longer texts it runs a writing workflow: understand the
  concept, propose 2–4 combinable style cards measured on real Persian writers
  and Iranian reports, write short samples, then finalize (سبک نوشتن، یادداشت،
  ستون، تحلیل، گزارش سالانه). Use for ANY Persian task: writing, editing,
  translating, humanizing, SEO and copywriting, academic papers/theses, and
  output in Word/.docx, PDF, PowerPoint, HTML, Excel, images, emails, social
  posts. Covers register (رسمی/اداری/محاوره/علمی), AI-tell removal,
  orthography (نیم‌فاصله، اعداد فارسی، «گیومه»), cleanup and spell-check
  (ویرایش، پاکسازی), RTL layout fixes and bundled Vazirmatn fonts. Trigger
  whenever you see Persian script or words like فارسی, Farsi, Persian, RTL,
  راست‌چین, ویرایش, مقاله, پایان‌نامه, سئو, کپشن — even if the user never
  mentions this skill.
metadata:
  version: 2.7.0
license: MIT (bundled fonts under SIL OFL)
compatibility: >
  Any agent that reads Markdown skills (Claude, Claude Code, Cursor, Codex,
  custom harnesses; chat-only AIs via universal/nasr-universal.md).
  Scripts: Python 3.8+ stdlib only. docx/pptx→PDF conversion: LibreOffice +
  installed fonts. PDF checks: poppler-utils, pypdf, or PyMuPDF (any one).
---

# nasr (نثر): Persian prose and RTL documents

Two failure modes make Persian output look machine-made, and they are independent:

1. **The prose sounds like AI.** Technically correct, but stiff, کتابی, inflated —
   no Iranian would write it that way.
2. **The layout betrays the text.** Persian rendered left-aligned, Arabic ي/ك glyphs,
   Latin digits breaking RTL flow, headings orphaned at page bottoms, fonts falling
   back to DejaVu.

Fixing one without the other still produces something a native reader screenshots
and laughs at. This skill fixes both. Work through the two checklists below, and
read the reference file for your output format before generating anything.

## Step 0: Route by task

| Task | Read |
|---|---|
| Any Persian prose (always) | `references/writing-style.md` |
| Mechanical correctness (always) | `references/orthography.md` |
| Prose over ~300 words that explains, argues, reports, mobilizes or commemorates: columns, analyses, essays, annual/sustainability reports, statements | `references/writing-workflow.md`, then `style-framework.md`, `storyline.md`, `style-skeletons.md` + `style-moves.md` |
| Academic: paper, thesis, report, مقاله/پایان‌نامه | `references/academic.md` |
| Educational/technical content, docs, product pages, how-to | `references/content-structures.md` |
| Telegram, Instagram, captions, carousels, reels, stories | `references/social-channels.md`; a post that is prose (an argument, analysis or story, not a caption) also follows `references/writing-workflow.md` |
| SEO content, blog for search, landing/ad copy, کپشن فروش | `references/seo-copywriting.md` |
| Cleanup/normalize/spell-check existing text (ویرایش، پاکسازی) | `references/cleanup/paknevis-rules.md` + `usage-patterns.md` |
| Choosing/embedding fonts | `references/fonts.md` |
| Word/.docx or docx→PDF | `references/docx-pdf.md` |
| PowerPoint/.pptx | `references/pptx.md` |
| HTML, email templates, HTML→PDF | `references/html-css.md` |
| Images/posters (PIL), new PDFs (reportlab), Excel, editing an existing workbook | `references/format-skills-fa.md` |
| A designed document (cover, colours, «زیبا»، «حرفه‌ای»), or building on the user's own designed file | `references/document-design.md`, then the format's reference |

**Visual neutrality, and when to design.** The simple level is the default:
this skill governs direction, spacing, fonts-for-shaping and text, and every
hex, border and fill in the code examples is a grey/black stand-in that shows
WHERE a property goes, not what value to use. Unstyled black text is the
correct default, and a surprise purple heading is a bug. Design is allowed in
two cases (document-design.md): the user asks for a designed document or it
goes to a board, investors, clients or the public, and then you **offer three
or four rendered directions** (`scripts/design_samples.py`) and build the one
the user picks; or the user hands over a designed file, and then you build on
its own elements (docx-pdf.md §7.3). Never invent one look silently, and never
carry a palette from one user or example to the next.

This skill composes with the general docx/pptx/pdf skills: those handle file
mechanics; this one overrides and extends them for Persian. When both disagree
about RTL behavior, this skill wins — its rules come from debugging real Persian
documents. If another active skill or the user specifies particular fonts or
colors, those win on aesthetics; this skill still governs RTL mechanics and
orthography. This skill itself is brand-neutral: colors in the code examples are
placeholders, and Vazirmatn is just the default font, not a requirement.

## Writing workflow: concept → styles → samples → final text

**Checkpoint first.** When the user asks for a new prose text, the first reply
is never the text. It is «برداشت من»; for a text with sections, the outline of
THIS text (printed heading + what the section says, kept apart); at most three
questions and the list of conflicts; the term list; the style (your call in one
line for sectioned documents, otherwise three suggestions with short samples
on the real material); and the material plan. Where you can write files, all
of it goes on the workbench page (`scripts/settings.py --config`); then end the
turn and wait. Structure comes before style: in real use users argue about
sections and headings, not about tone. Without a
question tool, ask in the message and stop. Skip only when the user says
«فقط بنویس» or similar, edits their own text, or asks for a short
transactional text (writing-workflow.md, «The checkpoint rule» and the depth
table, read top to bottom). «طبق اسکیل»، «کامل»، «با نثر» mean the full path
with three stops. When the user asks for evidence («شواهد»، «منبع»), search and
list verified sources at the checkpoint; with no web access say so, and never
cite from memory.

For any text that will be read as prose (columns, analyses, essays, reports,
statements, explainers, long posts), follow `references/writing-workflow.md`:

1. **Understand the concept.** Find the one sentence the reader should keep,
   the audience, the purpose and the material (facts, figures, experiences,
   quotations). Show a 4–6-line «برداشت من» and ask at most three questions
   whose answers change the text. Thin material is fixed here, by asking or
   searching, never by inventing.
2. **Outline, terms, then style.** For sectioned texts, the outline with real
   headings that pass the heading rules (storyline.md «Headings»), the term
   list, and the style stated in one line. For single-piece texts, two to four
   style cards that differ on an axis (style-framework.md), each with a short
   sample on the real material. The workbench (`scripts/settings.py --config`,
   writing-workflow.md «The workbench») carries all of it and returns one
   settings card the user pastes back. When the user names a few items with
   «و …», they are examples of a category: build the complete frame first
   (storyline.md «Examples or a complete list»).
2b. **Storyline before prose** (`references/storyline.md`). For long texts,
   first the high-level storyline (6–10 claim sentences, each answering the
   question the previous one raises, opening situation → complication →
   question → answer) and the main headings; show it and wait. Then the
   storyline of each section, with each claim marked [سند]، [شاهد بیرونی]،
   [استدلال] or [کمبود]. Then prose: every storyline sentence opens a
   paragraph. The recipe's arc (`style-skeletons.md`) says which claims are
   needed and where the payoff goes; non-argument styles chain other units
   (findings, moments, tasks, facts). Register and position are fixed before
   the storyline; each heading's tone (distance, certainty, warmth) and rhythm
   are set at level 1 from `references/tone-matrix.md`. Check with
   `scripts/storyline.py`.
   Never open with an announcement or a teaser.
3. **Sample text, when it helps.** One opening paragraph per card on the same
   real facts, so the user compares style alone.
4. **Write and finalize.** Draft to the chosen card, check facts, run
   `style_check.py`, `persian_cleanup.py --edit` and `fa_lint.py --check`, read
   it as a native reader, then deliver in the requested format (DOCX, PDF,
   HTML, slides) with the verifiers below.

**Long texts move between styles section by section.** Write a section map
(style-framework.md §5.3), move to a near style at each boundary, mark each
section with `<!-- سبک: … -->` and check with `style_check.py --sections`.
**Rewriting an existing document** follows the rewrite path in
writing-workflow.md: extract (the text inside images and the cover too),
measure the original, list inconsistencies for the user instead of fixing
facts silently, rewrite under the same facts, and deliver a side-by-side
comparison. **Rewrite and extend** (new voice plus new material) locks the
original's facts, marks every addition, lists every conflict, and derives new
targets from the user's data model.

Depth follows the ordered table in writing-workflow.md: «فقط بنویس» → write;
own-text edit → light; rewrite → rewrite path; short transactional → write;
«طبق اسکیل», over ~600 words or high-stakes → full path with three stops;
everything else, including any public or opinion post → the checkpoint.

## Writing: the five-second summary

Full guide in `references/writing-style.md`. The core moves:

1. **Detect register before writing a word — a register error is the costliest
   mistake this skill can make.** Follow the 6-step detection procedure in
   writing-style.md Part 1. The core rules: classify the DELIVERABLE, not the
   tone the user typed in (a casual «یه پروپوزال بنویس» still needs a formal
   proposal); when the text goes to a third party and signals conflict, ask
   ONE short question instead of guessing; no signal at all → formal-but-human.
   - Proposal, invoice, report, official email, website copy → **formal-but-human**:
     full written forms (می‌شود نه میشه), شما, zero slang — but است نه می‌باشد,
     short sentences, concrete claims. Human ≠ خودمونی: proposals/contracts keep
     formal vocabulary (no «جور است»-style idioms); warmth comes from clarity,
     numbers, and one warm closing line (writing-style.md, "warmth trap").
   - نامه اداری → formal + letter conventions (honorifics, «با سلام و احترام؛»
     — writing-style.md).
   - Instagram/Telegram, chat, friendly email → **colloquial written Persian**
     (محاوره‌نویسی): میشه، می‌خوام، رو، particles like دیگه/که/مگه.
   - Blog, newsletter → between: written forms, warm direct voice.
   - Paper, thesis, university report → **academic** (نگارش علمی): measured,
     hedged, passive acceptable, zero تعارف — read `references/academic.md`.
   - SEO/sales copy → register per artifact as above, plus `references/seo-copywriting.md`.
1b. **For longer prose, choose a style before writing**: style-framework.md.
   A style is four independent choices: purpose (گزارش، تبیین، اقناع، فراخوان،
   یادمان), dominant evidence (تجربه، واقعیت جاری، تاریخ، مفهوم، مرجع), position
   (من، ما، بیرونی) and structure (زمانی، زنجیره‌ای، فهرستی، تقابلی، شاخه‌ای).
   Named recipes (جدل، توجیه راهبردی، گزارش داده‌محور برند…) are common
   combinations. Rhythm is chosen separately, from profiles measured on real
   Persian columnists and annual reports. Columnists write 15–23-word sentences
   joined by connectives, so do not chop analytical prose into short lines.
   For long or high-stakes texts, offer two or three style cards. Otherwise
   state the chosen style in one line. Specificity outranks rhythm: secure real
   names, figures and dates first. Never invent experiences or quotations to
   fill the evidence axis.
2. **Ban the bureaucratic tells:** می‌باشد، لازم به ذکر است، در راستای،
   از اهمیت ویژه‌ای برخوردار است، نقش بسزایی ایفا می‌کند.
3. **Ban the AI tells:** em dashes (—), rule-of-three triads (سریع، آسان و مطمئن),
   نه تنها ... بلکه, tacked-on «که نشان‌دهنده‌ی ... است», vague «کارشناسان معتقدند»,
   generic «در دنیای امروز» openers, «در نهایت می‌توان گفت» closers.
4. **Hold one point of view.** Explain facts impersonally, address the reader
   directly (the verb carries it — don't repeat «شما»), and use «ما» only for
   what the organization actually did or is responsible for. Sliding between
   the three inside one section is the most common flaw in Persian brand
   content — content-structures.md §1.
5. **Separate teaching from selling.** The explanation must be worth reading
   without buying anything: state the problem before the product, never hide
   the main answer, tie each feature to a checkable result, and never delete
   limitations or prerequisites — they are what make the rest believable.
6. **Claim only what the source supports.** Distinguish واقعیت / نظر /
   پیش‌بینی / ادعا; never invent a statistic, version, price, or quote to fill
   a section; surface contradictions instead of silently resolving them; ask
   one question rather than guessing (content-structures.md §3).
   When paraphrasing a paper (thesis chapters especially), change only wording
   and structure: add no inference or bridging link, keep every qualifier
   (حدود، عمدتاً، ممکن است، تا، حداقل، معنادار) and every number exactly as the
   source states it, and mark the researcher's own reasoning «این بخش در مقاله
   وجود ندارد» instead of folding it in (academic.md §5.5).
7. **The native test:** would an Iranian screenshot this as «متن هوش مصنوعی»?
   If yes, rewrite before delivering. Two properties cause most of it:
   *predictability* (the expected collocation every time — اهمیتِ ویژه، نقشِ
   بسزا) and *uniformity* (every sentence 15–20 words, every paragraph the same
   weight). Real specifics create real variation; `fa_lint.py --check --rhythm`
   flags flat rhythm, but lexical tells matter far more — writing-style.md §3.5.
   The goal is prose that is genuinely better, not prose tuned to a detector:
   AI detectors are unreliable and falsely flag second-language writers at very
   high rates, and this skill never helps disguise authorship (§3.6).
8. **Numbers, punctuation, spacing** must be Persian — next section.

## Orthography: non-negotiables

Full rules in `references/orthography.md`. These apply to every deliverable:

1. **ZWNJ (نیم‌فاصله, U+200C)** — می‌شود نه می شود؛ کتاب‌ها نه کتاب ها؛
   بزرگ‌تر، خانه‌ام، به‌عنوان. In code: `‌` or HTML `&zwnj;`.
2. **Persian characters only:** ی (U+06CC) not ي، ک (U+06A9) not ك.
3. **Persian digits** ۰۱۲۳۴۵۶۷۸۹ inside Persian text. Latin digits stay in URLs,
   emails, codes, version numbers. Never Arabic-Indic ٤٥٦ forms.
4. **Persian punctuation:** ، ؛ ؟ and «گیومه» for quotes. No space before, one after.
4b. **هکسره** — never write the ezafe kasre as «ـه»: «کتابِ من»، not «کتابه من».
   The «ـه» ending is only the colloquial «است» («این کتابه» = این کتاب است).
   Test by substituting «است»; if the sentence breaks, you need a kasre.
   Iranians treat this error as a mark of carelessness — orthography.md §5.1.
5. **No em/en dashes** in Persian prose — use «،» or restructure.
6. **Never letter-space Persian** (it breaks letter joining), never fake bold/italic.
7. **Never start a Persian line with a Latin word.** Chat apps, GitHub, Telegram
   and most editors set each paragraph's direction from its FIRST letter, so
   «React یک کتابخانه است.» renders left-to-right — wrong alignment, the period
   on the wrong side, words scrambled. This covers every sentence, bullet,
   heading, table cell and caption. Lead with a Persian word instead:
   «کتابخانه‌ی React…»، «ابزار Docker…»، «دستور `npm install`…».
   For plain-text output where a line must open with a name,
   `persian_cleanup.py --bidi` adds an invisible direction mark. Full rules:
   orthography.md §9.

Two scripts enforce this mechanically — use both before delivering Persian text:

```bash
# 1. FIX: paknevis-style editorial pass (ZWNJ, chars, digits, punctuation, گیومه)
python3 scripts/persian_cleanup.py --edit --in text.md --out text.md
# 2. LINT: report what still needs contextual judgment (dashes, میشود forms,
#    fake tanvin, register issues) — fix these by hand
python3 scripts/fa_lint.py --check text.md
```

`--edit` is safe on structured files. Fenced code blocks, inline code and table
rows are lifted out before processing and restored byte-identical, and leading
indentation is never collapsed. This matters because Persian typography rules
are correct for prose and destructive in code: they would turn `"text"` into
`«text»`, rewrite ASCII digits as Persian, and flatten the spacing a table's
columns rely on. Pass `protect_code=False` (Python API) only if you truly want
those rules applied everywhere. Keep the file in version control either way —
the tool is careful, not omniscient.

`persian_cleanup.py` is a full toolkit (paknevis + davat merged): aggressive
cleaning for NLP (`--preset persian`), single functions (`--fn convert_digits`),
spell-check against the bundled 453K-word frequency dictionary
(`--edit --spellcheck`), custom pipelines. Persian «ویرایش» requests → `--edit`
(conservative, content preserved); «پاکسازی/نرمالایز» → `--preset persian`
(strips links/mentions/emojis). Details: `references/cleanup/`. Ezafe after
silent heh: `--edit` keeps the text's own style by default (`--ezafe auto`; a
document that already writes خانه‌ی stays خانه‌ی), `--ezafe hamza` writes خانهٔ.

**On Windows** run the scripts with `python` or `py -3` (`python3` is often a
Store alias); they set UTF-8 output themselves.

## Fonts

Bundled in `assets/fonts/` (SIL OFL — free for commercial use):

- **Vazirmatn** — the default for everything: body, UI, documents. 9 weights.
- **Lalezar** — display font for headlines, covers, posters. One weight; never body.

Other families (Shabnam, Sahel, Samim, Parastoo, Tanha, Gandom) and pairing advice:
`references/fonts.md`. In offline sandboxes only bundled fonts exist —
`scripts/download_fonts.py` works only where GitHub is reachable.

**Before any docx→PDF or pptx→PDF conversion, install the fonts:**

```bash
bash scripts/install_fonts.sh   # copies assets/fonts → ~/.fonts, runs fc-cache
fc-list | grep -i vazir         # verify — else LibreOffice silently falls back
```

Skipping this is the #1 cause of broken Persian PDFs: conversion "succeeds" but
every glyph is DejaVu tofu or disconnected letters.

## Documents: the rules that always apply

Format-specific recipes live in the reference files. The universal ones:

1. **RTL means START, not RIGHT.** In OOXML, with `bidirectional: true`,
   `AlignmentType.RIGHT` renders at the *visual left*. Always align `START`.
2. Every Persian run: `rightToLeft: true` + font with `hint: "cs"` (Complex Script).
3. Every section: `bidi: true`. Tables that must flow right-to-left:
   `visuallyRightToLeft: true`.
4. **Persian digits in numbered content** — a Latin "1." flips the paragraph LTR.
   Corollary for docx: never use the built-in `List Number`/`List Bullet` styles.
   Their markers live in `numbering.xml`, which has no bidi and renders Latin
   `1.` on the wrong side plus an OpenSymbol bullet that breaks font embedding.
   Write markers as ordinary runs («۱.  », «•  ») — docx-pdf.md §6.1.
5. **Fix the document defaults before adding content.** python-docx starts from
   a Latin template: `styles.xml` has no Persian font and Word's Heading styles
   carry a blue color you never asked for. Run `persianize_styles(doc)` from
   docx-pdf.md §6.1 immediately after `Document()`. Headers/footers are separate
   XML parts and need the RTL treatment applied to them directly.
6. **Pagination:** headings get `keepNext + keepLines` (no orphan headings);
   cards/boxes go inside a single-cell table with `cantSplit: true` (never split
   across pages); no separator after the last list item; no stray `PageBreak`
   before a section break (blank pages).
7. **Symbols:** Persian fonts miss many glyphs. In bundled Vazirmatn/Lalezar
   only • and · are verified; ▪ ■ ✓ ✕ ● ◆ ⊙ fall back to DejaVu. For any other
   symbol/font, check the cmap first (fonts.md shows how).

## Verify before delivering

Two gates. Check the .docx BEFORE converting (catches what code review can't),
then check the PDF:

```bash
# 1. DOCX: package integrity FIRST (a file Word won't open can't be RTL-checked),
#    then section bidi, jc=right traps, cs fonts, list numbering, heading colors.
#    --fix repairs missing <w:bidi/>; --sanitize strips the Word-for-Mac template
#    artifacts python-docx inherits (the classic "file is corrupt" fingerprint).
python3 scripts/verify_docx.py output.docx --expect-font Vazirmatn --fix --sanitize

# 2. PDF: fallback fonts, blank pages, template leaks, Arabic chars
python3 scripts/verify_pdf.py output.pdf --expect-font Vazirmatn
```

`verify_docx.py` exists because setting an RTL flag and that flag reaching the
XML are different things: libraries drop `bidi` from section properties, and
OOXML requires `<w:bidi/>` to be the FIRST child of `<w:sectPr>` — appended
anywhere else, renderers ignore it. Verify the artifact, never the source code.

It also guards the package itself: `[Content_Types].xml` must be the first ZIP
entry, every relationship Target must resolve, every XML part must be
well-formed and free of control characters. Repairs are written to a temp file
and validated before replacing anything, so a failed repair can't destroy the
document. Details and the already-corrupt-file procedure: docx-pdf.md §4.5.

It checks: near-empty pages, "undefined"/template leaks, non-embedded or fallback
fonts, Arabic ي/ك in extracted text, and page count. Fix every warning, regenerate,
re-verify. For prose, re-read your final text against the native test — one pass of
`persian_cleanup.py --edit` + `fa_lint.py --check` plus one honest read-aloud
catches most disasters. For styled prose, also run
`python3 scripts/style_check.py draft.md --recipe "<recipe>"` and revise any
feature outside its band; it checks rhythm, not quality, so read the draft too.

## Files

```
nasr/
├── SKILL.md                    ← you are here
├── references/
│   ├── writing-style.md        ← registers, Persian AI tells, colloquial patterns
│   ├── writing-workflow.md     ← concept → style cards → samples → final text
│   ├── style-framework.md      ← four style axes, recipes, rhythm profiles, choosing and combining
│   ├── tone-matrix.md          ← registers × tone dimensions × recipes × section types, order of decisions
│   ├── storyline.md            ← storyline first: level 1 and headings, level 2 per section, lead-sentence test
│   ├── style-skeletons.md      ← the thinking skeleton of each style: slots, payoff, fit test
│   ├── style-moves.md          ← signature moves per recipe (invented examples)
│   ├── style-evidence.md       ← the reference corpus behind the styles, and its limits
│   ├── academic.md             ← نگارش علمی: papers, theses, citations, formulas
│   ├── orthography.md          ← ZWNJ, characters, digits, punctuation, ezafe
│   ├── cleanup/                ← paknevis rules, davat API, usage patterns
│   ├── fonts.md                ← catalog, personalities, pairings, embedding
│   ├── content-structures.md   ← POV, education vs promotion, body patterns
│   ├── social-channels.md      ← Telegram/Instagram craft, repurposing
│   ├── seo-copywriting.md      ← Persian SEO writing + کپی‌رایتینگ
│   ├── docx-pdf.md             ← RTL docx recipes, pagination, PDF post-processing
│   ├── pptx.md                 ← RTL PowerPoint via python-pptx / html2pptx
│   ├── html-css.md             ← RTL web, mixed-direction text, print CSS
│   ├── format-skills-fa.md     ← PIL posters, reportlab PDFs, Excel RTL, editing existing workbooks
│   └── document-design.md      ← simple / designed / on the user's template; design directions; figures
├── scripts/
│   ├── persian_cleanup.py      ← FIX: edit/clean/normalize/spell-check (paknevis+davat)
│   ├── fa_lint.py              ← LINT: report issues needing contextual judgment
│   ├── settings.py             ← build the workbench (میز کار): outline, questions, conflicts, terms, styles with samples
│   ├── design_samples.py       ← render a document in 3–4 design directions; writes the chosen tokens
│   ├── render_html.py          ← HTML → PNG/PDF with headless Chrome/Edge (Persian text in images)
│   ├── build_matrix_doc.py     ← regenerate tone-matrix.md from assets/style_matrix.json
│   ├── storyline.py            ← print headings and paragraph lead sentences; flag announcements
│   ├── style_check.py          ← measure a draft against a rhythm profile
│   ├── verify_docx.py          ← DOCX RTL checks (+ --fix for section bidi)
│   ├── verify_pdf.py           ← post-generation PDF checks
│   ├── check_version.py        ← verify the version matches in all four places
│   ├── install_fonts.sh        ← bundled fonts → ~/.fonts (run before PDF export)
│   └── download_fonts.py       ← fetch extra families (needs GitHub access)
└── assets/
    ├── fonts/                  ← Vazirmatn + Lalezar TTFs
    ├── style_matrix.json       ← single source: dimensions, examples, recipes, sections, limits
    ├── settings.html           ← template of the workbench page
    ├── style_profiles.json     ← rhythm ranges per profile (from the reference corpus)
    └── persian_words.txt       ← 453K-word frequency dictionary (spell-check)
```
