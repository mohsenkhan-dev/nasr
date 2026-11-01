# nasr (نثر) — universal single-file edition
# نگارش فارسی حرفه‌ای برای هر هوش مصنوعی

This is the complete nasr skill compiled into one file, for AI
systems without file access. Give it to the AI as a system prompt, project
knowledge, or an attached document, with an instruction like:

> Follow the nasr guide for every task that involves Persian
> (Farsi) text or documents.

Two adaptations for this edition:

1. **Scripts become checklists.** The full package ships Python scripts
   (`persian_cleanup.py`, `fa_lint.py`, `verify_pdf.py`). Where the text says
   to run them, an AI without code execution applies the same rules manually —
   they are all stated in prose in the Orthography and Writing-style parts.
   An AI WITH code execution should get the full package instead.
2. **Fonts can't be bundled in a text file.** Get Vazirmatn and Lalezar from
   Google Fonts or github.com/rastikerdar/vazirmatn; everything here refers
   to them by name.

The single most important rule, before any writing: detect the register
(رسمی / اداری / محاوره / علمی) using the procedure in Part 1 — classify the
DELIVERABLE, not the tone of the request, and when the text goes to a third
party and signals conflict, ask one short question instead of guessing.

---

# PART 0 — Core rules and routing

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
| Any Persian prose (always) | the «Writing style: registers & de-AI-ing» part below |
| Mechanical correctness (always) | the «Orthography (نگارش و رسم‌الخط)» part below |
| Prose over ~300 words that explains, argues, reports, mobilizes or commemorates: columns, analyses, essays, annual/sustainability reports, statements | the «Writing workflow: concept to final text» part below, then the «Prose styles: axes, recipes, rhythm» part, the «Storyline first» part, the «Style arcs: think before writing» part + the «Signature moves per style» part |
| Academic: paper, thesis, report, مقاله/پایان‌نامه | the «Academic writing (نگارش علمی)» part below |
| Educational/technical content, docs, product pages, how-to | the «Content craft: POV, structure, honesty» part below |
| Telegram, Instagram, captions, carousels, reels, stories | the «Social channels: Telegram & Instagram» part below; a post that is prose (an argument, analysis or story, not a caption) also follows the «Writing workflow: concept to final text» part below |
| SEO content, blog for search, landing/ad copy, کپشن فروش | the «SEO writing & copywriting» part below |
| Cleanup/normalize/spell-check existing text (ویرایش، پاکسازی) | the Orthography part (script docs ship with the full package) |
| Choosing/embedding fonts | the «Fonts» part below |
| Word/.docx or docx→PDF | the «Word/DOCX + PDF» part below |
| PowerPoint/.pptx | the «PowerPoint» part below |
| HTML, email templates, HTML→PDF | the «HTML / CSS / email» part below |
| Images/posters (PIL), new PDFs (reportlab), Excel, editing an existing workbook | the «Images, reportlab PDFs, Excel» part below |
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
statements, explainers, long posts), follow the «Writing workflow: concept to final text» part below:

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
2b. **Storyline before prose** (the «Storyline first» part below). For long texts,
   first the high-level storyline (6–10 claim sentences, each answering the
   question the previous one raises, opening situation → complication →
   question → answer) and the main headings; show it and wait. Then the
   storyline of each section, with each claim marked [سند]، [شاهد بیرونی]،
   [استدلال] or [کمبود]. Then prose: every storyline sentence opens a
   paragraph. The recipe's arc (the «Style arcs: think before writing» part) says which claims are
   needed and where the payoff goes; non-argument styles chain other units
   (findings, moments, tasks, facts). Register and position are fixed before
   the storyline; each heading's tone (distance, certainty, warmth) and rhythm
   are set at level 1 from the «Register and tone matrix» part below. Check with
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

Full guide in the «Writing style: registers & de-AI-ing» part below. The core moves:

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
     hedged, passive acceptable, zero تعارف — read the «Academic writing (نگارش علمی)» part below.
   - SEO/sales copy → register per artifact as above, plus the «SEO writing & copywriting» part below.
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

Full rules in the «Orthography (نگارش و رسم‌الخط)» part below. These apply to every deliverable:

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
python3 the persian_cleanup script (full package; chat-only AIs apply the equivalent rules manually) --edit --in text.md --out text.md
# 2. LINT: report what still needs contextual judgment (dashes, میشود forms,
#    fake tanvin, register issues) — fix these by hand
python3 the fa_lint script (full package; chat-only AIs apply the equivalent rules manually) --check text.md
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
the «Fonts» part below. In offline sandboxes only bundled fonts exist —
the download_fonts script (full package; chat-only AIs apply the equivalent rules manually) works only where GitHub is reachable.

**Before any docx→PDF or pptx→PDF conversion, install the fonts:**

```bash
bash the install_fonts script (full package; chat-only AIs apply the equivalent rules manually)   # copies assets/fonts → ~/.fonts, runs fc-cache
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
python3 the verify_pdf script (full package; chat-only AIs apply the equivalent rules manually) output.pdf --expect-font Vazirmatn
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
`python3 the style_check script (full package; chat-only AIs apply the equivalent rules manually) draft.md --recipe "<recipe>"` and revise any
feature outside its band; it checks rhythm, not quality, so read the draft too.



---

# PART 1 — Writing style: registers & de-AI-ing

# Persian writing style: registers and de-AI-ing

AI Persian fails in a specific way: it is *too correct*. Too formal, too کتابی,
inflated with ceremony that no working Iranian writer uses. The fix is not
"be casual everywhere" — a slangy proposal is as wrong as a bureaucratic
Instagram caption. The fix is: pick the right register, then strip the tells.

## Part 1: Register detection

A register error is the most expensive mistake this skill can make: a خودمونی
proposal loses the client; a stiff Instagram caption loses the audience; a
casual نامه اداری can embarrass the sender in front of an organization. Decide
the register BEFORE writing, using the procedure below — never by feel.

| Context | Register | Markers |
|---|---|---|
| Proposal, invoice, contract, report, official/B2B email, website copy | **Formal-but-human** | Full written forms، شما، no slang — but direct and alive |
| نامه اداری / letter to an organization or authority | **Formal-اداری** | Formal + letter conventions (honorifics, opener/closer — see below) |
| Blog post, newsletter, product update, LinkedIn | **Semi-formal** | Written forms + warm voice، direct address، occasional colloquial word |
| Instagram, Telegram, chat replies, friendly email, story captions | **Colloquial written** (محاوره‌نویسی) | میشه، می‌خوام، رو، particles، fillers |
| Paper, thesis, university report, مقاله/پایان‌نامه | **Academic** (نگارش علمی) | Measured, hedged, passive OK, zero تعارف — full guide: the «Academic writing (نگارش علمی)» part |

### The detection procedure (apply in this order)

1. **Explicit instruction wins.** «رسمی بنویس»، «خودمونی باشه»، «لحن اداری» —
   obey it, whatever the document type.
2. **Deliverable type, not request tone.** Users type casually: «یه پروپوزال
   واسه مشتری بنویس» is a casual REQUEST for a formal DELIVERABLE. Classify
   the artifact, ignore the register the user typed in. This is the single
   most common detection mistake.
3. **Audience + destination.** Going to a client, organization, professor,
   or government office → formal side, even if the channel is a DM. Going to
   followers, friends, one's own team chat → casual side.
4. **One register per artifact, not per conversation.** A formal cover letter
   with casual Instagram captions attached = two artifacts, two registers.
5. **High stakes + ambiguity → ask.** If the text goes to a third party and
   signals conflict, ask ONE short question («لحن رسمی باشد یا صمیمی؟») —
   a question costs three seconds; a wrong register can cost the deal.
6. **No signal at all → formal-but-human.** It's the safe default in Persian
   professional contexts; casual by mistake is worse than formal by mistake.

Cues that flip toward casual: کپشن، استوری، پست اینستا، توییت، پیام دوستانه،
گروه دوستان، فان. Cues that flip toward formal: مشتری، سازمان، اداره، مدیر،
قرارداد، رسمی، مناقصه، دانشگاه، استاد، مقام.

### نامه اداری conventions (Formal-اداری)

Persian administrative letters have fixed furniture — using it correctly IS
the register:

- **Structure:** موضوع (one line) ← گیرنده با سمت ← «با سلام و احترام؛» ←
  body (short, one request per letter) ← closing formula ← نام، سمت، تاریخ.
- **Honorifics:** جناب آقای / سرکار خانم + [دکتر/مهندس] + surname;
  «مدیریت محترم ...»، «ریاست محترم ...». Never تو، never first names.
- **Openers:** «با سلام و احترام؛» or «احتراماً، به استحضار می‌رساند...» —
  one احتراماً maximum; stacking ceremony reads as parody.
- **Closers:** «با تشکر و احترام»، «پیشاپیش از همکاری شما سپاسگزارم».
- Body verbs stay است/می‌شود (NOT می‌باشد — even اداری doesn't excuse it;
  it only feels mandatory because bad letters normalized it).
- Requests: «خواهشمند است دستور فرمایید...» is the standard polite-request
  formula and is correct here, though it would be fossil anywhere else.

### Formal-but-human (the register AI gets most wrong)

Formal Persian does NOT mean bureaucratic Persian. The models default to اداری
ceremony; real professional writing is closer to a smart person talking carefully:

- **است، شد، کرد** — never می‌باشد، گردید، به عمل آورد. The می‌باشد register is
  a government-office fossil; in a proposal it reads as either lazy or machine.
- Clear sentences: one main idea each, and no long chains of که-clauses.
  In proposals, e-mails and web copy keep them short. In analytical columns,
  essays and reports do NOT chop them: real Persian columnists write 15–23-word
  sentences joined by connectives (اما، چون، بنابراین، یعنی). Follow the rhythm
  profile in style-framework.md §3.
- Address the reader: «شما» and second-person verbs, not «کاربران محترم می‌توانند».
- Concrete over ceremonial: «سایت شما در ۳ ثانیه باز می‌شود» beats
  «بهبود چشمگیر سرعت بارگذاری را تجربه خواهید کرد».
- Warmth is allowed. تعارف is allowed in openings/closings of letters
  (یک سطر، نه یک بند). Flattery-padding is not.

**The warmth trap — «انسانی» یعنی روان، نه خودمونی.** Over-correcting away from
کتابی lands in colloquial idiom, which in a proposal or contract reads as
unprofessional to exactly the client you're trying to win. In proposals,
contracts, invoices, official letters and reports, these do NOT belong:

- Colloquial idioms: «جور بودن» (→ مناسب بودن/هم‌راستا بودن)، «ردیفه/حله»،
  «رهایتان نمی‌کنیم» (→ همراهتان می‌مانیم)، «نه آخر کار» (→ و به پایان پروژه
  موکول نمی‌شود)، «پیش خودتان می‌ماند» (→ در اختیار خودتان باقی می‌ماند)
- Spoken sentence shapes: «همین هفته یک جلسه بگذاریم» → «پیشنهاد می‌کنیم همین
  هفته جلسه‌ای کوتاه برگزار شود» — the suggestion stays, the register rises.
- Where warmth in a formal document actually comes from: short clear sentences،
  concrete numbers، direct «شما»، and ONE warm line in the closing. Not chatty
  idioms scattered through the body.

Formality slider inside this register (most → least formal): contract/invoice →
proposal/official letter → report → website copy. Website copy may borrow a
warm idiom; a proposal should not. When unsure, write the sentence formally
first and only relax it if the document type allows.

### Colloquial written Persian (محاوره‌نویسی)

For social/chat contexts, written Persian mirrors speech:

- **Verb forms:** است → ـه (خوبه)، می‌خواهم → می‌خوام، می‌روم → میرم،
  می‌شود → میشه، بگذار → بذار
- **را → رو** (after the object): «اون فایل رو فرستادم»
- **آن/این → اون/این**، آن‌ها → اونا
- **Particles that carry the music:** دیگه (already/come on)، که (emphasis:
  «گفتم که»)، ها (attention: «بیا ها»)، مگه (surprise: «مگه میشه؟»)، خب، اصلاً
- **Fillers where a person would breathe:** راستش، یعنی، حالا، بعدش، چیز
- **Reactions:** جدی؟ واقعاً؟ وای! عجب! دمت گرم! آفرین! خخخ/هاهاها in chat
- **Expressive vocabulary, not safe vocabulary:** خوب → عالی، خفن، توپ؛
  بد → افتضاح، گند زد؛ خیلی → کلی، یه عالمه
- **تو vs شما:** تو for friends/peers/followers spoken to as one person;
  شما for strangers, elders, customers, and often mixed politeness online
  (شما + colloquial verbs: «شما بگید» is normal and warm). Overusing تو with
  strangers is rude; overusing formal شما forms with friends is cold.
- **تعارف:** exists even casually («قابلی نداره»، «مخلصیم») but one beat of it.
  Don't stack three politeness rituals in a DM.
- **هکسره — the error that undoes everything else.** Colloquial writing is
  exactly where the «ـه» clitic (= است) lives, so it is also where writers
  collide it with the ezafe kasre. «این کتابه» (this is a book) is right;
  «کتابه من» is wrong and should be «کتابِ من». One هکسره in an Instagram
  caption gets quoted back at the brand; it reads as carelessness, not casualness.
  Test each one by swapping in «است»: if the sentence survives, «ـه» is correct.
  Full rules and the wrong/right table: orthography.md §5.1.

Consistency rule: don't mix میشه and می‌شود in the same piece. Pick the register
and hold it. (Exception: quoting someone's speech inside formal text.)

Brand-fact rule (all registers, especially marketing copy): use only facts the
user or their brief actually provides. Never invent stats, years of experience,
client counts, partner names, or hashtags — an invented «۹۷٪ رضایت» or a brand
hashtag the user never asked for damages trust more than a plain sentence. No
facts available? Write generic-but-concrete claims and tell the user which
blanks to fill. The full discipline — separating واقعیت from نظر, پیش‌بینی and
ادعا, and what to do with contradictory sources — is in content-structures.md §3.

Point of view is a separate axis from register, and an easy one to get wrong:
impersonal for facts and mechanisms, second person for what the reader does
(the verb alone — repeating «شما» reads as translated English), «ما» only for
the organization's own actions and responsibilities. See content-structures.md
§1 for the full table; social-channels.md covers what changes per channel.

## Part 2: Persian AI tells — find and rewrite

These are the patterns that make Iranian readers say «اینو ربات نوشته». Scan for
every one; rewrite, don't delete — keep the meaning, lose the tell. Watch for
**clusters**: one «همچنین» is fine; همچنین + می‌باشد + «در دنیای امروز» is a confession.

### T1. می‌باشد disease (copula inflation)
The single loudest tell. Also: به شمار می‌رود، محسوب می‌شود، به حساب می‌آید،
قرار دارد (for است), گردیده است.

> ❌ وردپرس یکی از محبوب‌ترین سیستم‌های مدیریت محتوا می‌باشد و ابزاری قدرتمند محسوب می‌شود.
> ✅ وردپرس محبوب‌ترین سیستم مدیریت محتواست — قدرتش هم دقیقاً از همین‌جا می‌آید.

### T2. Ceremonial filler announcements
لازم به ذکر است که، شایان ذکر است، قابل توجه است که، همان‌طور که می‌دانید،
باید خاطرنشان کرد. Cut the announcement; say the thing.

> ❌ لازم به ذکر است که پشتیبانی به صورت ۲۴ ساعته ارائه می‌گردد.
> ✅ پشتیبانی ۲۴ ساعته است.

### T3. Significance inflation
نقش بسزایی ایفا می‌کند، از اهمیت ویژه‌ای برخوردار است، گامی مهم در راستای،
جایگاه ویژه‌ای دارد، تحولی شگرف، انقلابی، تحول‌آفرین، شگفت‌انگیز. Replace
with the concrete claim.

> ❌ سئو نقش بسزایی در موفقیت کسب‌وکار شما ایفا می‌کند.
> ✅ اگر در نتایج گوگل دیده نشوید، مشتری هم ندارید — سئو یعنی همین.

### T4. Generic openers and closers
Openers: در دنیای امروز، در عصر دیجیتال، امروزه با پیشرفت تکنولوژی، با گسترش
روزافزون اینترنت. Closers: در نهایت می‌توان گفت، به طور کلی، آینده‌ای روشن در
انتظار. Start with the actual point; end with a concrete fact or next step.

### T5. «در راستای» abuse
در راستای، در همین راستا، در جهت نیل به → usually just «برای».

### T6. Promotional emptiness
بی‌نظیر، فوق‌العاده، مثال‌زدنی، برترین، منحصربه‌فرد، تجربه‌ای متفاوت،
با کیفیتی بی‌رقیب. Specifics or silence.

> ❌ تیم ما با تجربه‌ای بی‌نظیر، خدماتی منحصربه‌فرد ارائه می‌دهد.
> ✅ در پنج سال گذشته ۴۰ پروژه تحویل داده‌ایم؛ سه‌تایشان الان روزی
> هزار سفارش دارند.

### T7. Rule of three
سریع، آسان و مطمئن؛ طراحی، توسعه و پشتیبانی — the triad rhythm is an AI
fingerprint in Persian exactly as in English. Two items, or four, or one
developed idea.

### T8. نه تنها ... بلکه (negative parallelism)
Overused. Also the clipped tail: «بدون هیچ دردسری»، «بدون نگرانی» stapled to
sentence ends. State the positive claim plainly.

### T9. Tacked-on analysis clauses (the -ing disease in Persian)
که نشان‌دهنده‌ی ... است، که بیانگر ... می‌باشد، که حاکی از ... است،
که گواهی است بر — fake depth suffixes. If the analysis matters, give it its
own sentence with evidence; usually, delete.

### T10. Vague authority
کارشناسان معتقدند، مطالعات نشان می‌دهد، تحقیقات ثابت کرده — with no named
source. Name it (طبق گزارش ۲۰۲۴ Semrush...) or drop the appeal.

### T11. False ranges
«از طراحی سایت گرفته تا سئو و تولید محتوا» when the items aren't on any scale —
just list the services.

### T12. Em dashes and English punctuation rhythm
Persian prose traditionally has no em dash; ChatGPT-style «متن — توضیح — ادامه»
is a hard tell. Use «،»، «؛»، parentheses، or a new sentence. (This file uses
one for contrast; your deliverables get zero.)

### T13. Calque phrases (translationese)
در پایان روز (at the end of the day) → آخرش، در نهایت؛
نگاهی بیندازیم به (let's take a look) → ببینیم؛
شایسته است بدانید → cut. If a phrase only exists as an English idiom's shadow,
an Iranian didn't write it.

**Think in Persian: collocations.** A verb must fit its noun in Persian, not
in English. تحول را «ایجاد می‌کنند»، «پدید می‌آورند»؛ تحول «بردنی» نیست
(«تحول را به سازمان‌ها ببرد» is wrong). Other English shadows: «هزینه‌ای که
نمی‌توان پرداخت» (cannot afford), «نقش بازی کردن» → نقش داشتن،
«از معیار رد شدن» (ambiguous: passed or failed?), «نقش حسگر را دارد». Read
each verb–noun pair aloud and ask whether an Iranian writer would pair them.

### T13b. Colons, headings and announcing openers
- **Colons are rare in Persian prose.** Use «:» only before a list or a quotation. Mid-sentence, replace it with «،»، «یعنی» or a new sentence.
- **Headings are plain and descriptive**: no «عنوان: زیرعنوان», no question headings, no dramatic phrasing («تصمیمی که پیش روست»، «سقف ظرفیت»). «پیشنهاد تغییر مأموریت کلمه» is a heading; a slogan is not.
- **No announcing openers in series.** Paragraphs that each begin «معیار نخست این است که…»، «مسیر دوم…»، «این سند از مخاطبش می‌خواهد…» read as a template, not a style. Say the thing itself; vary how paragraphs open.

### T14. همچنین pileup
همچنین، علاوه بر این، افزون بر آن opening consecutive sentences. Persian
connects naturally with و، هم، تازه (casual), or nothing.

### T15. Fake tanvin words
گاهاً، دوماً، ناچاراً — tanvin on Persian words is wrong (tanvin is Arabic
morphology). Use گاهی، دوم اینکه، به‌ناچار. (Real Arabic loans keep it:
واقعاً، حتماً، اصلاً، لطفاً.)

### T16. Bold-header bullet lists
The «**سرعت بالا:** توضیح» list format is ChatGPT furniture. In prose
deliverables, write paragraphs. Bullets only when the content is truly a list —
and then plain bullets, no bold-colon headers.

### T17. Sycophantic chat residue
سؤال بسیار خوبی است!، البته!، خوشحال می‌شوم کمک کنم، امیدوارم مفید بوده باشد —
chatbot correspondence pasted into content. Delete on sight.
Same for instruction echoes: طبق درخواست، بر اساس توضیحات شما، مطابق دستور
ارائه‌شده — the text answers a prompt nobody else can see.

### T18. Universal tells (from the English humanizer — they transfer)
Elegant variation (وب‌سایت/سایت/پلتفرم/پورتال cycling for one thing);
passive hiding the actor (تصمیم گرفته شد — by whom?); excessive hedging
(شاید بتوان گفت که احتمالاً); staccato manufactured drama; aphorism formulas
(«سئو زبانِ اعتماد است»); emojis decorating headings; Title Case in Latin
brand names mid-Persian is fine, but no ALL-CAPS shouting.

## Part 3: What NOT to flag

- **Correct formal Persian is not a tell.** A contract in proper formal register
  is supposed to be formal — just not می‌باشد-formal.
- **تعارف is human.** One line of «با احترام» or «قربان شما» in a letter is
  culture, not AI. Only flag stacked, empty ceremony.
- **Poetry and literary prose** play by their own rules — سعدی gets to use
  constructions a proposal can't. Don't "humanize" quoted poetry, آیات, titles,
  or proper names. Never edit inside quotations.
- **Loanwords are normal.** Iranians say آپدیت، پیج، استوری، دیجیتال مارکتینگ.
  Forcing pure-Persian coinages (تارنما for سایت) sounds weirder than the loan.
- **One همچنین, one خیلی, one exclamation** — isolated instances mean nothing.
  Look for clusters.

## Part 3.5: Why machine prose reads flat — the underlying mechanism

T1–T18 are symptoms. Two properties of how language models generate text
explain most of them, and knowing the cause lets you fix cases the list doesn't
name.

**Predictability (perplexity).** A model picks, at each step, a highly probable
next word. Do that thousands of times and every phrase becomes the expected
one. In Persian this surfaces as the safe collocation every single time:
«اهمیت» always arriving with «ویژه‌ای»، «نقش» with «بسزایی»، «تیم» with
«مجرب». Nothing is wrong with any one of them; the tell is that no phrase ever
surprises. A human writer, even a careful one, occasionally reaches for the
less obvious word — and that irregularity is what reads as a person thinking.

**Uniformity (burstiness).** Human writing varies: a 6-word sentence next to a
30-word one, a two-line paragraph after a dense one, a section that runs long
because the idea deserved it. Generated text clusters in a narrow band —
sentences mostly 15–20 words, paragraphs of equal weight, sections of equal
length, every list with the same number of items. The prose has no dynamics.

Measured on the samples shipped with this skill: an AI-written services page
scored 0.39 sentence-length variation with paragraphs all within 0.19 of each
other, while its rewrite reached 0.65 with sentences from 2 to 27 words. Check
your own draft with:

```bash
python3 the fa_lint script (full package; chat-only AIs apply the equivalent rules manually) --check --rhythm text.md
```

Read the output as an editor's nudge, not a verdict. Rhythm is a **secondary**
signal: in that same comparison, the count of lexical tells went from 11 to 0,
which is the change a reader actually feels. A text with perfect variance and
«می‌باشد» in every paragraph still reads as machine-written. Fix T1–T18 first;
use rhythm to catch what's left.

**What actually creates variation** is having something specific to say. Uneven
sentences are a *consequence* of real content — a precise number, a caveat, an
aside, a change of mind mid-paragraph. Padding a draft with artificially short
sentences produces staccato drama (T18), not humanity. Write the specifics and
the rhythm follows.

## Part 3.6: About AI detectors — what to tell a client, and what not to chase

Persian writers, and Iranians writing in English, get caught by these tools
disproportionately, so the facts matter:

- A 2023 evaluation of 14 detection tools found **all scored under 80% accuracy,
  and only 5 above 70%**; accuracy degrades further on paraphrased text.
- **Non-native English writers are falsely flagged at an average rate of 61.3%**
  in one study of seven detectors — a system that flags most second-language
  writing as machine-written is not measuring what it claims to.
- Reported false-positive rates run as high as 50% in journalistic testing, and
  differ by writer demographic (20% for Black students vs 7% for white students
  in one 2024 report).
- Cambridge and other Russell Group universities, and UT Austin, withdrew from
  Turnitin's AI detection over reliability concerns. Published authors have had
  their own books flagged.

Three practical consequences:

1. **Never treat a detector score as evidence** — of your text or anyone's.
   It is a probabilistic guess about style, not a finding about authorship.
2. **Don't rewrite good Persian to please a tool.** Chasing a score pushes
   writers toward deliberately clumsy prose, which is worse for the reader —
   the only audience that matters.
3. **If a client or institution raises a false flag**, the evidence above is the
   answer: point to the measured false-positive rates for second-language
   writers and to the institutions that abandoned these tools.

**The boundary this skill holds.** Everything here is aimed at prose that is
genuinely better — specific, varied, honest, in the right register. That is
also, incidentally, prose that reads as human, because it is written like one.
What this skill will not do is help misrepresent authorship: no invisible
characters, no homoglyph substitution, no watermark stripping, no injected
typos. Those tricks damage the text, help no reader, and in a context where
disclosure is required — a thesis, a journal submission, a client contract, an
employer's AI policy — the honest move is to follow that policy and say what
was AI-assisted. Improving writing and hiding its origin are different jobs;
this skill does the first.

## Part 4: Signs of human Persian (preserve these)

Specific numbers and names (پنج‌شنبه ساعت ۴، پروژه‌ی آقای کریمی). Mixed feelings
(«راستش هنوز مطمئن نیستم»). Asides in parentheses. Uneven sentence lengths.
A joke that only lands in Persian. Era-bound slang. If a draft has these,
protect them through the rewrite.

## Part 5: Process

1. Identify register from context (Part 1). Academic → also read the «Academic writing (نگارش علمی)» part.
2. Draft.
3. Audit against T1–T18 and orthography (the «Orthography (نگارش و رسم‌الخط)» part; fix with
   the persian_cleanup script (full package; chat-only AIs apply the equivalent rules manually) --edit`, then lint with the fa_lint script (full package; chat-only AIs apply the equivalent rules manually) --check`).
4. Ask: «اگه یه ایرانی اینو ببینه، اسکرین‌شات می‌گیره بنویسه "متن هوش مصنوعی"؟»
   Name the remaining tells honestly.
5. Rewrite into the final. Deliver only the final unless asked for the audit.

### Worked example (formal-but-human — **website copy**, the loosest end of
this register; a proposal would keep the same directness but formal vocabulary
throughout — see the warmth-trap list above)

**Before (AI):**
> در دنیای امروز، داشتن وب‌سایت از اهمیت ویژه‌ای برخوردار می‌باشد. وب‌سایت نه
> تنها ویترین کسب‌وکار شما محسوب می‌شود، بلکه نقش بسزایی در جذب مشتریان جدید
> ایفا می‌کند. لازم به ذکر است که تیم ما با تجربه‌ای بی‌نظیر، خدماتی سریع،
> باکیفیت و مقرون‌به‌صرفه ارائه می‌دهد — از طراحی گرفته تا سئو و پشتیبانی.
> در نهایت می‌توان گفت انتخاب ما، انتخابی هوشمندانه است.

**After:**
> مشتری قبل از این‌که به شما زنگ بزند، اسمتان را گوگل می‌کند. اگر چیزی پیدا
> نکند — یا بدتر، سایتی پیدا کند که در موبایل به‌هم‌ریخته است — سراغ رقیبتان
> می‌رود. کار ما همین است: سایتی که پیدا می‌شود و اعتماد می‌سازد. طراحی و سئو
> را ما انجام می‌دهیم؛ بعد از تحویل هم رهایتان نمی‌کنیم. نمونه‌کارها را ببینید
> و اگر سؤالی بود، همین امروز جواب می‌دهیم.

(Note: the After still failed one check — it uses an em dash twice. Final pass
replaces them: «اگر چیزی پیدا نکند، یا بدتر، سایتی پیدا کند که...». This is
exactly why the audit step exists.)



---

# PART 2 — Writing workflow: concept to final text

# Writing workflow: from concept to final text

This is the path for any Persian text that someone will actually read as prose:
columns, analyses, essays, reports, statements, explainers, long posts, letters
that argue a case. It has four stages. Each stage ends with something the user
can see and redirect cheaply, so a wrong turn costs one message, not a rewrite.

```
۱. فهم مفهوم      → برداشت من (۴ تا ۶ خط) + حداکثر سه پرسش
۲. پیشنهاد سبک    → ۲ تا ۴ کارت سبک، یکی پیشنهادی
۳. متن نمونه      → (اختیاری) پاراگراف آغازین هر کارت روی همان مصالح
۴. نگارش نهایی   → پیش‌نویس، بررسی‌ها، بازنویسی، تحویل در قالب خواسته‌شده
```

## The checkpoint rule (ایستگاه): ask and show before writing

**Default: stop before the text.** When the user asks for a new text to be
written (a post, column, report, statement, letter that argues, any prose),
the first reply is the checkpoint, never the text:
1. «برداشت من» in 4–6 lines (stage 1);
2. **for any text with sections, the outline of this text** (below,
   «Structure before style»): every printed heading with what the section
   says, as a table or on the workbench;
3. at most three questions whose answers change the text, and the list of
   conflicts between what the user asked and the existing text or data;
4. the term list: official names, replacements, banned words (below);
5. the style: for a sectioned document, pick it yourself and say it in one
   line; otherwise three suggestions, each with a two-sentence sample on the
   real material (stage 2);
6. the material plan: what evidence you have, what you will search for, what is missing.

Where you can write files, put the outline, questions, terms and style on the workbench page (میز کار, «The
workbench» below) and send it; in chat, show them as plain tables.

### Structure before style

In the first real use (a board strategy document rewritten and extended), the
user never argued about style. Every round trip was about structure: which
sections, in which order, what each one says, and what its heading is. Style
cards shown before the outline were noise. So, for documents with sections:
- The outline comes first, and it is the outline of **this** document, with
  its real headings. Generic section types («استدلال و ضرورت») are for you,
  never for the user.
- Show two things per section and keep them apart: **the heading** that will
  be printed, and **what the section says** (one plain sentence, not printed).
  A user reads a sentence in the heading column as a proposed heading.
- Alternatives for one heading are labelled «تیتر جایگزین برای همین بخش»,
  never «الف/ب» next to each other, which reads as heading + subheading.
- Every proposed heading already passes the heading rules (storyline.md
  «Headings»): no colon, no question, no sentence with a verb, content not label.
- The user can add, drop, move and nest sections in one sentence or on the
  workbench. Treat a section the user asked for as fixed: if it is missing
  from your outline, the outline is wrong.
- The style is your call for such documents. State it in one line («سبک: سند
  راهبردی؛ بخش الزامات: توجیه راهبردی») and change it only if the user asks.

### Lock the terms

Users fix vocabulary mid-way: «موتور نگو، بگو پیشران» and «برای این محصول
دستیار نگو» and «نام کاملش همیشه پلتفرم … است» and «فرق لفظ خوبی نیست». Collect
these at the checkpoint and whenever they come up:
- official names (the full name on first mention, the short name after);
- replacements (X → Y) and banned words;
- metaphors the document already uses for something else. In the test, the
  original text used «دو بال» for system and adoption; calling the two
  businesses «دو بال» too would have collided.
Apply the list to the prose, tables, captions, figure text and file names,
and before delivery search the final text for every banned word.

Then **end the turn**. Do not write the text in the same reply. This does not
depend on a question tool: where AskUserQuestion or a similar tool exists, use
it; where it does not (Codex, plain chat, API), ask in the message and stop.
An agent that writes the text in the same turn as the checkpoint has skipped it.

**Phrases that set the path** (read the user's words, not your estimate of the job):

| The user says | Path |
|---|---|
| «فقط بنویس»، «سریع»، «بدون سؤال»، «همین الان» | No checkpoint: state the style in one line and write |
| «طبق اسکیل»، «کامل»، «کاملاً طبق اسکیل»، «با نثر»، «مرحله به مرحله» | Full path with three stops: after the checkpoint, after the level-1 storyline, after the level-2 storyline (or the samples) |
| «تنظیمات پیشرفته»، «میز کار» | The advanced-settings page at the checkpoint |
| nothing about the process | The checkpoint, then write after the user answers |

## Choosing the depth

Apply the **first** row that matches, top to bottom. The rows do not overlap
because the order decides.

| Order | Situation | Path |
|---|---|---|
| 1 | The user said «فقط بنویس» or similar | State the style in one line and write |
| 2 | Light edit of the user's own text | Stage 1 only on what the text is for; keep their style unless asked |
| 3 | Rewriting an existing document («بازنویسی کن»), or rewriting it in a new voice **and** adding to it («تغییرات اضافه می‌شوند و متن فعلی را کامل می‌کنند») | The rewrite path below, with the checkpoint after the diagnosis; for additions, «Rewrite and extend» |
| 4 | Under ~150 words and transactional (email reply, caption, notice, UI copy) | Write; register rules in writing-style.md are enough |
| 5 | The user said «طبق اسکیل» or similar, or the text is over ~600 words, or high-stakes | Full path with three stops |
| 6 | Everything else, including any public or opinion text (a Telegram or Instagram post, a column) whatever its length | The checkpoint, then write after the answers |

A public text is never «transactional»: a post that takes a position needs the
checkpoint even at 300 words.

## When the user asks for evidence (شواهد، منبع، پژوهش)

«شواهد علمی بیار»، «با منبع»، «مستند» make research a stage of its own:
- Search before writing, and list at the checkpoint the sources you found: author or institution, year, title, link, and the one finding you will use from each. Prefer peer-reviewed papers, official statistics and major research institutes.
- Every figure or finding in the text must trace to a listed source you have actually opened. Quote nothing you have not read.
- **No web access → say so at the checkpoint** and ask the user for sources, or offer to write the argument without citations. Never produce a reference from memory as if verified; a plausible but invented citation is the worst failure of this skill.
- After the text, list the sources used, in the format the channel allows (a short list at the end of a Telegram post).

## Stage 1: understand the concept (فهم مفهوم)

The concept is what the text says, not what it is about. «جنگ ایران و آمریکا» is
a topic. «احتمال حمله‌ی دوباره را باید از آماده‌سازی‌های پرهزینه خواند، نه از
سخنان» is a concept. A text without a concept fills space; with one, every
paragraph has a job.

Extract these from the request, attachments and conversation:

| Item | Question | If missing |
|---|---|---|
| مفهوم مرکزی | The one sentence the reader should remember | Propose one or two, as named concepts when the purpose is تبیین («جنگ معلق»، «اقتصاد انتظار») |
| مخاطب | Who reads it, and what they already know | Infer from the channel; ask only if it changes register |
| غایت | After reading, the reader should know / understand / accept / act / remember | Infer; ask if explain vs. persuade is open (style-framework.md §1) |
| مصالح | Facts, figures, dates, documents, experiences, quotations available | Ask the user or search; never invent (rule below) |
| قالب و طول | Column, report, post, letter; word count; output file | Default from channel |
| مجرا و لحن | Where it is published; register | writing-style.md Part 1 |
| محدودیت‌ها | What must or must not be said, legal or political lines, house style | Ask if the text is public and the topic is sensitive |

Then show the restatement, in the user's language:

```
برداشت من
- مفهوم مرکزی: …
- مخاطب: …
- غایت: خواننده بعد از خواندن … (تبیین / اقناع / …)
- مصالح موجود: … · کمبود: …
- قالب: … حدود … کلمه، خروجی …
```

Ask at most three questions, and only ones whose answer changes the text. A
question about a fact you could look up is not one of them: search instead.

**Material comes first.** In blind tests, specificity outranked every style
choice (style-framework.md §7). If the material is thin, say so here and fix it
(search, ask for figures, ask for the user's own experience) before choosing a
style. A good style on generic content still reads as machine-written.

**Never fabricate.** No invented experience, quotation, statistic, date or
source. If a recipe needs evidence that does not exist (روایت شاهد without a
real scene, خطابه without a verified quotation), drop that recipe at stage 2.

## Stage 2: propose styles (پیشنهاد سبک)

Use style-framework.md §4 to derive the candidates and §6 for the card. Offer
two to four cards that differ on at least one axis (purpose, evidence, position
or structure). Three rhythm variants of one recipe are not three styles.

A good default set:
1. **The recipe the request implies**, marked «(پیشنهادی)».
2. **One that changes the evidence or the structure**: the same purpose built on history instead of current facts, or scenarios instead of one argument.
3. **One combination** (style-framework.md §5): for example a scene that opens into analysis, or figures, then their meaning, then what should follow.
4. Optional: **a deliberately plainer card** (فشرده or گزارشی) when the material is fact-dense and the reader is busy.

For documents with sections, a card is a section map (style-framework.md §5.3),
not one recipe. Default cards by genre:
- **Strategy document, roadmap, proposal to a board**: the سند راهبردی recipe, chosen by you and stated in one line; argument sections (necessity, requirements) move to توجیه راهبردی. Spend the checkpoint on the outline, not on style cards («Structure before style»).
- **Annual or sustainability report**: the brand or institutional report map; offer the other as the alternative card.
- **Long analytical column**: one recipe, with at most a different opening section.

Each card, in Persian:

```
کارت ۱ · استدلال روزنامه‌ای (پیشنهادی)
- غایت: اقناع · شاهد: واقعیت جاری · جایگاه: من · ساخت: زنجیره‌ای
- آهنگ: استدلالی پیوسته (جمله‌ها حدود ۱۸ کلمه، پیوسته با ربط‌ها)
- نقشه: واقعیت تازه ← سه نکته ← توصیه به تصمیم‌گیرنده
- حس خواننده: «یک نفر با استدلال روشن نظرش را می‌گوید»
- ریسک یا کمبود: به دست‌کم یک منبع رسمی دیگر نیاز دارد
```

Ask the user to choose with one question (AskUserQuestion where available,
otherwise in the message, and then end the turn;
options in the user's language, the recommended card first). Allow «ترکیب ۱ و
۳» as an answer: combining is normal (style-framework.md §5).

## The workbench (میز کار، تنظیمات پیشرفته)

The workbench is one page that carries the whole checkpoint, so the user
decides in one place instead of over five messages. Build it whenever you can
write a file and the text has sections, and always when the user asks for
«تنظیمات پیشرفته» or «میز کار». Write the checkpoint as JSON, then:

```bash
python scripts/settings.py --config <scratch>/checkpoint.json --out <folder>/nasr-desk.html
```

`checkpoint.json` holds (the script's docstring shows the exact shape):
- `outline`: every section with `title` (printed heading), `job` (what it
  says, not printed), `source` (تازه / از متن قبلی / قبلی با افزوده), `level`
  (1 or 2), optional `alts` (alternative headings) and `type` (a section type
  from style_matrix.json, used only for tone defaults);
- `questions` (with answer options) and `conflicts` (each with what disagrees
  with what);
- `terms` (from, rule, to);
- `suggestions`: up to three recipes, each with `why` in plain words and a
  `sample` of two or three sentences **on the real material**. A style the
  user cannot see is a style they cannot choose; never send cards without samples.

The page, in order: the outline (edit headings in place, alternative headings
one click away, add / delete / move / nest, live heading checks); questions
and conflicts with answer buttons; the term table; three style cards with
their samples; and, folded away, the full parameter panel and per-section
tone for users who want them. Everything lands in a «کارت تنظیمات» the user
pastes back.

What the first real use taught about this page: an earlier version opened on
abstract parameters (distance, certainty, rhythm) and generic section types,
had no examples, no way to add a heading, and did not show the section the
user had asked for. The user found it confusing and decided nothing on it.
Keep the page about the user's document, in the user's words; parameters are
the last and optional layer.

Treat the pasted card as the user's decision: its headings, answers, terms and
style override yours. If it chooses a «با احتیاط» value, follow it and keep the
reason in mind (say it once if it matters). The page's data is
assets/style_matrix.json, the same source as tone-matrix.md.

## Stage 2b: the storyline (خلاصه‌ی روایت)

Prose is written from a storyline, never from slots. Follow storyline.md.
The order of decisions is fixed: register and position first, then the
level-1 storyline with each heading's job, tone and rhythm, then each
section's storyline with the certainty of each claim, then prose
(tone-matrix.md §1).

1. **Level 1.** The high-level storyline: 6–10 claim sentences, each answering
   the question the previous one raises, opening situation → complication →
   question → answer. Use the recipe's arc (style-skeletons.md) to know which
   claims are needed and where the payoff goes. Group the sentences under 3–7
   plain main headings.
2. **Show level 1 to the user** for any long or high-stakes text, and wait.
3. **Level 2.** Under each heading, the section's own chain of 3–6 claim
   sentences, each marked [سند]، [شاهد بیرونی]، [استدلال] or [کمبود]. Show it,
   at least for sections with weak support.
4. **Level 3.** Each storyline sentence becomes a paragraph's first sentence;
   the paragraph adds two or three sentences of support.
5. **Check** with `scripts/storyline.py`: the printed lead sentences must read
   as the storyline.

Short texts (under about 400 words) need only level 1, kept in mind or shown
in one line.

## Calibrating styles on a topic

When the user wants to know which styles suit a topic, or doubts whether a
style «came through», write one short sample (150–250 words) per suitable style
on the same material. For each sample show:
- the style's essence in one line (what must be present for the style to be recognisable);
- its filled skeleton;
- the text.

Let the user judge each sample «درآمده / نیمه / درنیامده» with a note, and
revise only the ones that did not come through, skeleton first. Styles whose
skeleton cannot be filled from the material are listed as unsuitable, not
written. An illustrative scene for روایت شاهد may be invented in a calibration
sample when the user asks, marked as invented; never in a deliverable.

What the first calibration on a real strategy topic taught:
- Tone and rhythm were right in most samples; the failures were thinking failures (no crux or trade-off in the strategy, targets given away in a report's opening, a disclaimer as an explainer's first line, scenarios not derived from drivers).
- A rewrite is not a copy edit. Rebuilding the skeleton changes the text; polishing the original's sentences does not.
- Shortening paragraphs to fit a rhythm band made the text choppier, not better. Bands are a check, not a target.

## Stage 3: sample text (متن نمونه), when it helps

Write samples when the user cannot choose from the cards, when the text is
long and public, or when they ask «یک نمونه ببینم». Skip them when a card was
chosen with confidence.

- **One opening paragraph per card**, 80–150 words, on the real material.
- **Same facts in every sample**, so the difference the user sees is the style alone.
- Label each sample with its card number and recipe name, nothing else. No commentary inside the sample.
- Real prose, not an outline: the sample must already meet the card's rhythm, so the user is judging what they will get.
- At most four samples. If none works, go back to stage 1: usually the concept or the material is the problem, not the style.

Then ask once: which sample, or which mix («آغاز ۲ با ساخت ۱»).

## Stage 4: write and finalize (نگارش نهایی)

1. **Section map** (texts over ~600 words or with headings): one line per section with its job, its axis values if they change, and its rhythm profile (style-framework.md §5.3). Move to a near style at each boundary. Mark each section with `<!-- سبک: … -->` under its heading so the check below can measure it. Show the map only if the user asked to see the structure.
2. **Draft from the storyline** (stage 2b): each storyline sentence opens a paragraph. Use two to four moves from style-moves.md, not all of them. Keep the concept from stage 1 visible: in the opening, and again where the argument turns or closes.
3. **Checks**, in this order:
   - Facts: every name, figure, date and quotation traces to the user, a document or a source you found. Mark anything unverified.
   - Rhythm: `python3 the style_check script (full package; chat-only AIs apply the equivalent rules manually) draft.md --recipe "<recipe>"` (or `--profile`); for a sectioned text, `--sections`, which measures each section against its declared profile and flags jumps between non-neighbouring profiles. Revise features outside the band. Under ~400 words, fix only clear deviations: chasing every band swings the draft (style-evidence.md, worked test).
   - Orthography: `python3 the persian_cleanup script (full package; chat-only AIs apply the equivalent rules manually) --edit`, then `python3 the fa_lint script (full package; chat-only AIs apply the equivalent rules manually) --check`.
   - Reading pass: the native test in writing-style.md. At most one single-sentence paragraph. No run of short punchlines. No AI tells.
4. **Revise** at most two rounds for rhythm. If the draft still fails, the card was wrong for the material: say so and offer the nearer card rather than forcing it.
5. **Deliver** in the format asked for. For Word or PDF, follow docx-pdf.md and run verify_docx.py / verify_pdf.py. For HTML, html-css.md. For slides, pptx.md.
6. **Closing note**, short: the style line («سبک: … · آهنگ: …»), what was not verified, and one offer if relevant (a shorter version, a headline set, the same text for another channel).

## The rewrite path: an existing document

When the user hands over a document (DOCX, PDF, Markdown, pasted text) and asks
for it to be rewritten, the material already exists. The job is to keep every
fact and change how the text works. Run the four stages, with these
differences.

**R1. Extract the text faithfully.**
- Text only, in reading order, with headings kept as headings.
- Tables are read cell by cell from the source (merged cells repeat their value; do not deduplicate them away).
- Figures and images become caption markers («تصویر ۲. …») in their place, so the rewrite keeps their position.
- **Read the text inside the images too**: the cover, diagrams, timelines, number tiles. List every name, figure and claim they carry. In the first real use the cover still named the old mission and the closing figure still showed the old targets (۸۰ مشتری، ۳۰٪) after the text had changed; only a visual check of the PDF caught it. An image whose text no longer matches goes on the change list and is redrawn (document-design.md «Figures»).
- For DOCX use python-docx over the body elements in order; for PDF see docx-pdf.md.

**R2. Measure the original before touching it.**
`style_check.py original.md --sections` (or `--compare` when it has no
headings) gives the rhythm it actually has, section by section. This is the
baseline the user will compare against, and it often names the problem: in the
first real test, a roadmap's argument sections had 3.4 connectives per 1000
words against a band of 12–22, which is why it read as a list of assertions.

**R3. Diagnose, and list what only the user can decide.** Read the document
for:
- **Order:** does the problem come before the solution, the why before the what?
- **Repetition:** the same sentence or argument in two sections.
- **Position slips:** «ما» or «داشته باشیم» in a text that otherwise names the organization.
- **Fragments and typos.**
- **Numbers that disagree:** a criterion in the text against the table, a label that does not match its values («نسبت به امروز» over absolute figures), undefined units.
- **Placeholders:** «…», «[کشورهای هدف]».
- **Missing material the reader will ask for**: for a board, resources and risks.

Never resolve a factual inconsistency silently and never fill a gap with an
invented figure. They go on a separate list for the user, and the rewrite keeps
the original's numbers.

**R4. Stages 1–2 on the document.** The «برداشت من» is drawn from the document
itself; questions go to the user only for what the document cannot answer.
The style card is a section map. If the user asked for a finished rewrite, state
the chosen card and go on; otherwise show the cards first.

**R5. Rewrite under constraints.**
- Same facts, figures, names, terms and claims. Do not add claims, even plausible ones.
- Same length, within about 10%, unless the user asked for shorter.
- Keep the document's conventions: its ezafe style (‌ی or ٔ; drop `fix_ezafe` from `persian_cleanup.py --steps` when it uses ‌ی), its terminology, its digit style in tables.
- Reordering sections and merging repeated passages are allowed, but each one goes on the change list with its reason.

**R5b. Rewrite and extend.** When the user wants the existing text kept in
substance, rewritten in a new voice, and completed with new material (a new
business line, new targets, a new section), R5's «same length, no new claims»
does not hold. Instead:
- The original's facts are locked: rewrite them, never change them silently.
- Every addition is marked as new in the outline («تازه» / «قبلی با افزوده»).
- Wherever an addition disagrees with the original or with the user's data
  (a count, a date, a target, a name, a metaphor), list it as a conflict at
  the checkpoint with both sides; the user decides.
- New targets are derived from the user's data model (budget sheet, KPI
  sheet), and the derivation is shown («از رشد ماهانه‌ی ۸٪ اکسل»). A target
  proposed before reading the model will change later and cost a round trip.
  When the user raises targets («تهاجمی‌تر»), show old and new side by side.
- The deliverable keeps the original's design (docx-pdf.md §7.3).

**R6. Deliver a comparison, not only the new text.** Unless the user asked for
the new text alone, deliver:
- the original and the rewrite side by side, section by section, with moved sections marked;
- the measurements before and after;
- the change list;
- the list of decisions for the user from R3.

An HTML page (html-css.md) works well for review. When the user wants a file to
work in, also deliver the rewrite alone in the original's format (DOCX: docx-pdf.md,
then verify_docx.py).


## Feedback after delivery

- «زیادی خشک است / زیادی شعاری است»: move one step on the rhythm or position axis, not a new recipe.
- «این را نگفتم / این درست نیست»: a material problem. Fix the fact; do not restyle.
- «شبیه هوش مصنوعی است»: run the AI-tell list in writing-style.md §3.5 first; then check for missing specifics.
- Keep what the user did not criticise. A full rewrite for a local complaint loses what worked.



---

# PART 3 — Prose styles: axes, recipes, rhythm

# Persian prose style: choosing and combining styles

Register (writing-style.md) decides how formal a text is. This file decides
*how the text works*: what it does to the reader, what it rests on, who speaks,
how its parts are ordered, and at what rhythm. It was built from a reference
corpus of signed Persian prose (nine columnists and essayists, 620 texts)
and eleven Iranian corporate annual reports; the evidence and its limits are in
style-evidence.md, the signature moves in style-moves.md.

Read this file for any text longer than about 300 words whose job is to
explain, argue, report, mobilize or commemorate: columns, analyses, essays,
reports, annual and sustainability reports, statements, explainers. Short
transactional texts (emails, captions, UI copy) do not need it.

## 1. Why styles are described on four axes

An earlier list of named styles («جدل»، «تحلیل مفهومی»، «روایت شاهد»...) mixed
five different criteria (method, structure, material, voice, purpose), so the
names overlapped: 20 of 34 hand-labelled texts needed two or three of them.
A usable classification needs one criterion per division. So a style is
described by four independent axes. Each axis answers one question, and its
values exclude each other. A text takes the value that DOMINATES; the test for
each axis says how to decide.

### Axis 1: purpose (غایت)
Question: after reading, what does the reader have that they did not have before?

| Value | The reader gains | Test: the conclusion is… |
|---|---|---|
| گزارش | knowledge of what happened | a fact or a figure |
| تبیین | understanding of why or how | a relation, a mechanism, a set of options |
| اقناع | acceptance of a disputed judgement | «پس فلان درست/نادرست است» |
| فراخوان | an intention to act | an imperative to the reader or to «ما» |
| یادمان | a feeling or a memory | honouring, grieving, reflecting |

Boundary rules:
- تبیین vs اقناع: if the text defends a judgement against another view, it is اقناع; if it explains without taking a side on a disputed point, تبیین.
- اقناع vs فراخوان: فراخوان only when the one who must act is the reader or «ما». A recommendation addressed to an official is اقناع (the reader is asked to accept that the official should act).

### Axis 2: dominant evidence (شاهد غالب)
Question: what source of authority does the conclusion rest on?

| Value | Who vouches | Condition |
|---|---|---|
| تجربه | the writer's own eyes | **only real experience supplied by the user**; never invent it |
| واقعیت جاری | today's record: event, figure, document | sourced and dated |
| تاریخ | the record of a past the writer did not witness | dates verified |
| مفهوم | reason: definition, distinction, framework | |
| مرجع | an authority: scripture, poetry, a named thinker | quotations exact and verified |

Boundary rule: «was the writer there?» If yes, it is تجربه, even when it happened long ago.

### Axis 3: position (جایگاه)
Question: whose place does the writer speak from?

| Value | |
|---|---|
| من | a personal witness or opinion holder |
| ما | spokesperson of a group: a community, a nation, an organization |
| بیرونی | impersonal observer; an organization may refer to itself by name |

Decide by the grammatical person of the main claims. Keep one position per
section; content-structures.md §1 says how «ما»، «شما» and impersonal voice
divide the work inside organizational texts.

### Axis 4: structure (ساخت)
Question: on what basis do the sections follow one another?

| Value | Ordering principle | Typical |
|---|---|---|
| زمانی | earlier, then later | narrative, history, memoir |
| زنجیره‌ای | each section follows from the previous one | argument, analysis |
| فهرستی | parallel, independent points | reports, numbered points, explainers |
| تقابلی | someone's claim, then the answer | rebuttal |
| شاخه‌ای | several possibilities side by side | scenarios, options |

### What the axes do NOT decide
- **Register** (formal / colloquial / academic): writing-style.md.
- **Rhythm** (sentence and paragraph length, connective density): §3. In the
  corpus, rhythm follows the writer family and the genre, not the axis values:
  three different recipes anchored on the same writers produced near-identical
  numbers. So rhythm is chosen separately.

## 2. Recipes: common combinations with a name

A recipe is a named, frequent combination of axis values plus the moves that
make it work (style-moves.md). Recipes are shortcuts, not categories: a text is
classified by its axis values; the recipe name only says which combination it is.

| Recipe | Purpose | Evidence | Position | Structure | Default rhythm | Use for |
|---|---|---|---|---|---|---|
| تحلیل مفهومی | تبیین | مفهوم | بیرونی | زنجیره‌ای | تحلیلی میانه | explaining a phenomenon through a concept |
| توجیه راهبردی | تبیین | واقعیت جاری | بیرونی | شاخه‌ای | تحلیلی میانه | briefing a decision-maker: scenarios, indicators |
| استدلال روزنامه‌ای | اقناع | واقعیت جاری | من | زنجیره‌ای | استدلالی پیوسته | an opinion column on a current issue |
| جدل | اقناع | varies | من / بیرونی | تقابلی | استدلالی پیوسته | answering a published claim |
| عبرت تاریخی | اقناع | تاریخ | بیرونی | زمانی | تحلیلی میانه | drawing a rule for today from history |
| روایت شاهد | تبیین / اقناع | تجربه | من | زمانی then زنجیره‌ای | گفت‌وگویی شخصی | starting from a scene the writer lived |
| خطابه | فراخوان | مرجع | ما | فهرستی | خطابی | statements, calls to a community |
| توضیح و آموزش | تبیین | مفهوم | من | فهرستی | گفت‌وگویی شخصی | giving the reader a tool or method |
| تأمل شخصی | یادمان | تجربه | من | زنجیره‌ای | گفت‌وگویی شخصی | a personal, hedged reflection |
| سوگ‌نامه | یادمان | تجربه | من | زمانی | گفت‌وگویی شخصی | commemorating a person |
| گزارش داده‌محور برند | گزارش | واقعیت جاری | ما / بیرونی | فهرستی | گزارشی برند | annual or yearly reports of consumer companies |
| گزارش نهادی | گزارش | واقعیت جاری | بیرونی | فهرستی | گزارشی نهادی | sustainability, board and institutional reports |
| خبر کوتاه | گزارش | واقعیت جاری | بیرونی | فهرستی | فشرده | announcements, news briefs, release notes |
| سند راهبردی | اقناع | واقعیت جاری + مفهوم | بیرونی (the organization by name) | زنجیره‌ای, then زمانی/فهرستی | تحلیلی میانه → گزارشی برند (section map, §5.3) | strategy documents, roadmaps and proposals to a board or headquarters |

**سند راهبردی is provisional.** No strategy documents were in the corpus; the
recipe is the best current combination of tested parts, built from one real
roadmap (a five-year plan for an AI company) rewritten and measured section by
section. Use it, and treat its section map as a default to adjust.

The same writer uses several recipes: one columnist wrote a witness narrative,
a numbered argument and a rebuttal within one month. Choose the recipe from the
job of the text, never from a writer's name.

## 3. Rhythm profiles

Numbers are the 20th, 50th and 80th percentile across the anchor texts
(assets/style_profiles.json; measured by the style_check script (full package; chat-only AIs apply the equivalent rules manually)). Aim for the
middle; stay inside the 20–80 band. Pushing one feature to its extreme to make
a style recognisable produces caricature, which readers rate worse than the
plain version.

| Profile | Sentence median (words) | Paragraph median (words) | Connectives per 1000 words | «که» per sentence | Anchors |
|---|---|---|---|---|---|
| تحلیلی میانه | 14.5 · 18 · 23 | 40 · 67 · 90 | 12 · 16 · 22 | 0.22 · 0.35 · 0.50 | analytic columnists |
| استدلالی پیوسته | 15 · 18.5 · 22.5 | 57 · 71 · 82 | 15 · 20 · 25 | 0.47 · 0.66 · 0.86 | argumentative columnists |
| گفت‌وگویی شخصی | 12 · 15 · 18 | 30 · 41 · 56 | 9 · 13 · 17 | 0.37 · 0.51 · 0.66 | personal essayists, teaching blogs |
| خطابی | 12.5 · 17 · 19 | 28 · 42 · 69 | 4 · 9 · 14 | 0.15 · 0.31 · 0.50 | one writer, 22 texts: weak evidence |
| گزارشی برند | 19 · 23 · 27 | 42 · 53 · 63 | 3 · 5 · 9 | 0.17 · 0.24 · 0.38 | Digikala, Snapp reports |
| گزارشی نهادی | 22 · 25.5 · 29 | 81 · 120 · 167 | 4 · 6 · 12 | 0.17 · 0.29 · 0.41 | Mobarakeh Steel, Irancell, bank reports |
| فشرده | 6 · 9 · 12 | 15 · 25 · 40 | 2 · 6 · 12 | 0.05 · 0.15 · 0.30 | no corpus anchor; unvalidated |

What the numbers mean in practice:
- **Columnists** write 15–23-word sentences joined by connectives (اما، چون، بنابراین، یعنی، البته). Their paragraphs develop one idea over 3–4 sentences.
- **Reports** write longer sentences (20–29 words) with few connectives: long noun chains and enumerations, carried by figures (15–85 digits per 1000 words). That is the genre, not a fault; but in a brand report keep sentences nearer 20 than 29.
- **Mix lengths.** In the columnist profiles 15–30% of sentences run past 30 words and 10–25% stay under 10. A draft with the right median but no long sentences still reads choppy. A draft whose sentences are all long reads like a report.
- **Short texts are noisy.** Under about 400 words one sentence moves every percentage; style_check.py then flags only clear deviations. Do not chase each band sentence by sentence: in a test, doing so swung a draft from too choppy to too heavy.
- **Single-sentence paragraphs**: at most one per text, normally the last. A reader perceives a run of them as text broken after every sentence.
- **فشرده** (6–12-word sentences) works only when every sentence carries a fact. On generic content it reads as machine-written.

## 4. Choosing a style: the procedure

1. **Register first** (writing-style.md Part 1).
2. **Purpose**: answer «after reading, the reader should…» from the request. If the request fits two purposes (explain vs. persuade is the common one), ask one short question.
3. **Evidence inventory**: list what material exists — the user's facts, documents, experiences, quotations, data, or what a search can verify. The evidence axis can only take values you actually have material for. No real experience → no تجربه. No verified quotation → no مرجع.
4. **Position**: from who is writing — a person (من), an organization or community (ما), or a neutral author (بیرونی).
5. **Structure**: from purpose and evidence. Defaults: تاریخ or تجربه → زمانی; a claim to answer → تقابلی; options or uncertainty → شاخه‌ای; several independent results → فهرستی; one argument → زنجیره‌ای.
6. **Recipe**: the nearest row in §2. If nothing fits, keep the axis values and skip the name.
7. **Rhythm**: the recipe's default, unless the user's own prose, a house style or the channel says otherwise.
8. **Section plan** for texts over about 600 words: give each section its own values; see §5.

### When to ask and when to decide
- **Long or high-stakes text, or the user asked for options**: show two or three style cards (§6) with one line each on what the reader will feel, then write the one chosen. A good default set: the recipe the request implies, one that changes the purpose or the evidence, and one combination.
- **Otherwise**: choose, and state the choice in one line before the text (for example «سبک: استدلال روزنامه‌ای، آهنگ استدلالی پیوسته»). The user can redirect cheaply.

## 5. Moving between styles in one text

Long texts are combinations, and in a long report the style should move from
section to section: a summary, an argument, a list of results, a roadmap and a
closing picture do different jobs. Moving well means moving to a NEAR style at
each boundary, so the reader feels the text change gear, not change author.

### 5.1 What stays fixed for the whole text
- **One purpose**, the one the final section serves. A witness opening that leads to a call to action is a فراخوان text with a روایت شاهد opening.
- **One position.** Change it only at a section boundary and with a reason (content-structures.md §1). A strategy document that names the organization in the third person for 2,000 words must not slip into «داشته باشیم».
- **One register** and one orthographic convention (ezafe style, digits).

### 5.2 What may move, and how far
Two styles are **near** when they differ on one axis value, or when their rhythm
profiles are neighbours. Neighbours were computed from the profile medians
(`style_check.py --list`):

| Profile | Nearest neighbours |
|---|---|
| تحلیلی میانه | استدلالی پیوسته، خطابی |
| استدلالی پیوسته | تحلیلی میانه، خطابی |
| گفت‌وگویی شخصی | خطابی، تحلیلی میانه |
| گزارشی برند | گزارشی نهادی، خطابی |
| گزارشی نهادی | گزارشی برند، تحلیلی میانه |
| فشرده | خطابی، گفت‌وگویی شخصی |

خطابی appears as a neighbour of almost everything because its bands are wide
(one writer, 22 texts). Do not read it as a natural bridge.

Rules for each boundary:
- **Change one or two axes, not all four.** From an argument (اقناع، زنجیره‌ای) to a results list (گزارش، فهرستی) is two axes: fine. From a personal scene (تجربه، من، زمانی، گفت‌وگویی) to an institutional table (واقعیت جاری، بیرونی، فهرستی، نهادی) is four: put a section between them or open with a bridge paragraph.
- **Move rhythm to a neighbour.** تحلیلی میانه → گزارشی برند is a jump: the first paragraph of the new section should still connect (one «یعنی» or «بنابراین»), and sentences lengthen over the section, not in its first line.
- **Let the first sentence of the new section make the change in content**, never as an announcement. «عددهای سال همین تصویر را دقیق‌تر می‌کنند.» works; «در این بخش به بررسی … می‌پردازیم» and «این سند پیشنهاد می‌کند…» do not.
- **Keep the concept visible across the move.** The named concept of the opening (writing-workflow.md, stage 1) should reappear in the report sections as the reason the figures matter.

### 5.3 The section map
The section map is now part of the level-1 storyline (storyline.md): under
each main heading, one line with the section's job, the axis values that
change, its tone (tone-matrix.md) and its rhythm profile. Then
mark each section in the draft with a comment under its heading.
`style_check.py --sections` reads these, measures each section against its own
profile, and warns when two consecutive sections are not neighbours:

```
## ۴. سبد فعالیت امروز
<!-- سبک: گزارشی برند -->
```

Remove the comments in the delivered file if the format would show them (DOCX
built from Markdown, plain text); HTML and rendered Markdown hide them.

Default section maps follow. Adjust them to the document. The report maps
follow the order of sections in the corpus reports, but were not measured
section by section.

**سند راهبردی** (strategy document, roadmap, proposal to a board):

| Section | Job | Axes that change | Rhythm |
|---|---|---|---|
| خلاصه | the decision asked for, the target, the phases | گزارش + اقناع | تحلیلی میانه, figures allowed |
| مسئله و آموخته‌ها | what experience taught; name the concept | تبیین، مفهوم | تحلیلی میانه |
| ضرورت | the ceiling of today's model, the change proposed | اقناع، زنجیره‌ای | تحلیلی میانه or استدلالی پیوسته |
| مدل یا ایده | the parts and how they feed each other | تبیین، فهرستی | تحلیلی میانه |
| وضع موجود | what exists today | گزارش، فهرستی | گزارشی برند |
| نقشه‌ی راه | phases: goal, work, indicators, exit criteria with numbers | گزارش، زمانی | گزارشی برند; shorter paragraphs are normal here (label lines «هدف فاز:»، «پایان فاز:») |
| شاخص‌ها | the table, with definitions | گزارش | table, not prose |
| منابع و ریسک‌ها | what it costs, what can go wrong, what the board decides | تبیین، شاخه‌ای (توجیه راهبردی) | تحلیلی میانه |
| تصویر پایان دوره | one concrete, dated scene of success | تبیین، زمانی | تحلیلی میانه |

Measured on the rewritten roadmap: the analytic sections sat in تحلیلی میانه
once connectives were made explicit (the original had 3.4 per 1000 words,
against a band of 12–22). The roadmap sections ran at 0–5 connectives with
short paragraphs; that is the label-line structure, not a fault.

**گزارش سالانه‌ی برند:** پیام مدیرعامل (فراخوان or تأمل، ما، گفت‌وگویی شخصی) →
سال در یک نگاه (گزارش، فهرستی، گزارشی برند) → بخش‌های عملکرد (figure → meaning →
cause، گزارشی برند) → روایت مشتری یا کارکنان (real stories only، زمانی، گفت‌وگویی
شخصی) → مسئولیت اجتماعی (گزارشی برند) → چشم‌انداز (اقناع، شاخه‌ای، تحلیلی میانه).

**گزارش پایداری یا نهادی:** پیام مدیرعامل → معرفی و حاکمیت (گزارشی نهادی) →
موضوعات بااهمیت (تبیین، فهرستی، گزارشی نهادی) → عملکرد به تفکیک موضوع (figure،
standard and actor، گزارشی نهادی) → اهداف سال بعد (اقناع، فهرستی، گزارشی برند to
lighten the close).

**یادداشت تحلیلی بلند:** روایت شاهد (opening scene) → تحلیل مفهومی → استدلال →
توجیه راهبردی (scenarios) → توصیه. Rhythm stays in the columnist profiles
throughout; only the opening may run shorter.

### 5.4 Common sequences inside one section
- روایت شاهد → تحلیل مفهومی → استدلال: a scene, the concept it reveals, the argument.
- گزارش (figures) → تبیین (what they mean) → اقناع (what should follow): the strong pattern of data-driven reports.
- عبرت تاریخی → توجیه راهبردی: history, then today's scenarios.

## 6. The style card

Write the card before drafting a long text, and show it when options are offered:

```
سبک پیشنهادی
- غایت: اقناع
- شاهد غالب: واقعیت جاری (گزارش سنتکام، قیمت نفت، اظهارات رسمی)
- جایگاه: من
- ساخت: زنجیره‌ای
- نسخه: استدلال روزنامه‌ای · آهنگ: استدلالی پیوسته
- نقشه: آغاز با یک واقعیت تازه ← سه نکته ← توصیه به تصمیم‌گیرنده
- مصالح لازم: ۴ تا ۶ واقعیت مشخص با منبع؛ اگر نیست، پیش از نوشتن بپرس یا جست‌وجو کن
```

## 7. Rules the evidence supports

1. **Specificity beats rhythm.** In blind tests, a plain short-sentence text full of sourced facts was rated as high as the best styles, while well-rhythmed text on a generic topic was rated low. Before styling, secure the facts: names, figures, dates, events. Every paragraph needs at least one concrete anchor, except in خطابه and تأمل شخصی.
2. **Never fabricate the evidence axis.** Experience, quotations and historical dates come from the user, a document or a verified source. If missing, ask, or choose a recipe whose evidence you have.
3. **No caricature.** Stay inside the 20–80 band for every feature. Overcorrecting is the common failure: after learning that columnists use connectives, a draft used twice as many as any columnist.
4. **Recipes are not writers.** Writers are calibration anchors, not voices to impersonate. When the user asks for «به سبک X», use the closest recipe and rhythm, do not copy X's idioms, and never present the text as X's.
<!-- fa-lint-ignore-next-line -->
5. **Corporate reports: formal-but-human, not bureaucratic.** The institutional reports in the corpus carry 4–6 bureaucratic forms (می‌باشد، گردید، نموده، در راستای) per 1000 words; the brand reports almost none, and read better. Use است، شد، کرد; name the actor instead of an agentless passive; keep figures, and give each important figure its meaning («۲۱ میلیون کاربر، یعنی…»).
6. **Check the draft**: `python3 the style_check script (full package; chat-only AIs apply the equivalent rules manually) draft.md --profile "استدلالی پیوسته"` (or `--recipe`). For a text with sections, mark each section's style and run `--sections` (§5.3). Revise features outside the band, then run fa_lint as usual.



---

# PART 4 — Storyline first

# Storyline first (خلاصه‌ی روایت)

A text is a chain of claims before it is a set of paragraphs. Write the chain
first, get it right, and only then write prose around it.

This is how consulting and strategy writing is built, and it is what the
user's tests asked for. Three Deloitte Insights articles were read for their
structure: two research pieces on agentic AI, and one scenario piece on
generative AI. In all three:
- the opening runs situation → complication → question → answer;
- about nine paragraphs in ten open with the claim itself, and the evidence (a figure, a case, a quotation) follows;
- reading only the first sentence of each paragraph gives the whole argument;
- body paragraphs run three or four sentences;
- headings are short topics or short claims.

In the user's tests, the samples that failed had acceptable tone and rhythm
but no storyline. Their first sentences were connectors, announcements or
descriptions, so the paragraphs sat side by side instead of following from
one another. Style-skeleton slots alone («diagnosis», «crux») did not fix
this, because a slot names a role, not a claim.

## Before the storyline: register and position

Two parts of tone are fixed before the storyline, because they change what
the claims are, not how they sound:
- **Register** (سیاق), from writing-style.md Part 1. It decides which claims can be said at all.
- **Position** (من، ما، بیرونی). «ما دیده‌ایم» and «تجربه نشان داده» are different claims.

Everything else about tone (distance, certainty, warmth) is planned per
heading at level 1, set per claim at level 2 (certainty), and realised in
prose. The storyline itself is written in plain, neutral Persian, so that only
its logic is judged; final tone comes with the prose. The full matrix of
registers, tone dimensions, recipes and section types is in tone-matrix.md.

## The storyline differs by style

Every style has a storyline: a chain of units, each following from the one
before. What changes is the unit and the question that links two units:

| Recipe family | Unit | Linking question |
|---|---|---|
| strategy, analysis, argument, rebuttal | a claim | «چرا؟»، «پس چه؟»، «بهایش چیست؟» |
| brand or institutional report | a finding: a figure and its meaning | «یعنی چه؟»، «چرا شد؟»، «بعدش چه؟» |
| explainer | a task for the reader | «چطور؟»، «بعد چه کنم؟» |
| witness narrative, obituary, reflection | a moment or event, and one turn | «بعد چه شد؟»، «یعنی چه؟» |
| خطابه | an emotional step: situation, stake, commitment, call | «حالا چه باید کرد؟» |
| short news | a fact, by importance | «دیگر چه؟» |

The rules below are written for claims; for other units, read «claim» as the
recipe's unit. The test is the same: read only the units, in order, and the
text must already work.

## Level 1: the high-level storyline and the main headings

Write 6–10 sentences. Each sentence must:
- be a complete claim with content, never a label («تشخیص وضعیت») or an announcement («در ادامه می‌بینیم…»);
- answer the question the previous sentence raises in the reader's mind: «خب؟»، «چرا؟»، «پس برنده کیست؟»، «پس چه باید کرد؟»، «بهایش چیست؟»، «چطور؟»، «از ما چه می‌خواهید؟».

Write the reader's question in brackets after each sentence while drafting,
so the chain is visible. A sentence whose bracket is empty, or whose question
is not the one the next sentence answers, is in the wrong place.

The opening sentences follow situation → complication → question → answer:
- **Situation**: what the reader already accepts. No news in it.
- **Complication**: what changed, or what goes wrong. This is where the text earns attention.
- **Question**: the one the complication raises; usually left implicit.
- **Answer**: the text's main claim. In a report or research piece it may come later, but the reader must feel the question early.

Then group the sentences under the **main headings**: three to seven, each
covering one or more storyline sentences. Headings follow the rules below.

### Headings

A heading is what the reader sees in the document. The first real use showed
how easily headings go wrong; the user rejected four of five proposed
headings, among them «چرا ونچر، و چرا وزنش روی کلمه است؟». Rules:
- Two to eight words. A noun phrase or a short claim: «مسیر توسعه‌ی سریع»،
  «اقتضائات رشد سریع»، «تصویر سال ۱۴۱۰».
- No colon, no question, no «چرا / چگونه / آیا» opening, no full sentence
  ending in a verb, no slogan, no wordplay.
- Persian collocations, not translated ones: «ضرورت حرکت به سمت ساختار چابک
  و مقیاس‌پذیر»، not «چرایی ونچر».
- The heading names the section's content; the sentence that explains the
  section's job is a separate thing and is never shown as a heading.
- Use the user's names for things («پلتفرم هوش مصنوعی اُکیان») and the term
  list (writing-workflow.md «Lock the terms»).
- A heading the user wrote is final. Do not «improve» it.
- When you offer alternatives, offer them for one heading at a time and
  label them as alternatives.

`fa_lint.py` flags colons and questions in Markdown headings; the workbench
checks every heading live.

### Examples or a complete list

When the user names a few items and ends with «و …» or «مواردی مثل»
(«بودجه‌ی کافی، GPU، فضای فیزیکی، جبران خدمات و …»), or gives one item «as
an example» («نیروی انسانی را مثال زدم»), the items are **examples of a
category**, not the outline of the section. Build the complete frame of the
category first, with parts that do not overlap and together cover it, then
place the user's items in it, and give every part comparable weight. In the
first real use the agent made the user's example (human capital) the axis of
the requirements section and summarised everything else; the user called it
biased and illogical. The frame that worked was: the gap with competitors →
its five dimensions (capital, compute, people, brand, decision speed) → one
requirement per dimension → the smart ways to close the gap.

Under each heading, add one line that sets the section's **job, tone and
rhythm**: its distance, certainty and warmth, and its rhythm profile. Start
from the section-type defaults in tone-matrix.md §5 and keep each step between
neighbouring sections small (tone-matrix.md §6). This line replaces the
separate section map; in the draft, mark the section with
`<!-- سبک: <profile> -->` so `style_check.py --sections` can measure its rhythm.

The recipe's arc (style-skeletons.md) tells you what kind of claims the
storyline needs and where the payoff goes: a strategy needs a diagnosis, a
crux and a trade-off; a report puts targets at the end. The arc is the plan;
the storyline is the plan filled with claims.

**Show the level-1 storyline and headings to the user and end the turn**
whenever the full path applies (writing-workflow.md, depth row 5) or the user
asked to follow the skill fully. It is ten lines; correcting it costs nothing
compared with correcting prose.

## Level 2: the storyline of each section

Under each heading, write the section's own chain: 3–6 claim sentences,
which will become the first sentences of its paragraphs. Set the certainty of
each claim here («باید» or «پیشنهاد می‌شود», «است» or «احتمالاً»): certainty
is content, not decoration. If one paragraph will depart from the section's
tone (a warmer customer story, a cautious risk), mark it now. Next to each
claim, note its support:
- **[سند]**: a fact in the user's material;
- **[شاهد بیرونی]**: an external source, with its name and year, to be verified before use;
- **[استدلال]**: the writer's reasoning, which needs no source but must follow;
- **[کمبود]**: a claim the section needs but the material cannot support yet. Ask, search, or cut the claim; never fill it with invented facts.

The section's chain must also pass the bracket test, and its last sentence
should lead to the next heading's first sentence.

For long texts, show level 2 as well before writing, or at least the
sections whose support is weak.

## Level 3: prose

Each storyline sentence becomes the first sentence of a paragraph, reworded
into natural Persian if needed but carrying the same claim. The rest of the
paragraph, two or three sentences, gives the support: the figure and what it
means, the case, the reasoning step. A paragraph that needs a second claim
is two paragraphs.

## Checks

- **The lead-sentence test.** `python3 scripts/storyline.py draft.md` prints every heading and the first sentence of each paragraph under it. Read the printout alone. It must read as the storyline. If a first sentence is a connector, an announcement or a description, rewrite it as the claim.
- **No teasers.** «چه چیزی آن را تعریف خواهد کرد» withholds the claim to create suspense; in this genre it is an announcement in disguise. State the claim.
- **No wordplay in place of insight.** A quoted word turned into a concept («گره کار در همان «زودتر» است») signals that the reasoning is missing. Write the reasoning.
- **Support before polish.** If level 2 has many [کمبود] marks, the text will read thin in any style. Say so to the user before writing.



---

# PART 5 — Register and tone matrix

# ماتریس سیاق، لحن و سبک

<!-- Generated by scripts/build_matrix_doc.py from assets/style_matrix.json. Edit the JSON, then rerun. -->

This file holds every dimension the skill uses to decide how a text sounds, in
the order in which they are decided, with one criterion per dimension. It is
written in Persian because its tables are meant for the user as much as for
the model. The same data drives the advanced-settings page
(`scripts/settings.py`), so the two cannot disagree.

همه‌ی مثال‌ها ساختگی‌اند و روی یک موضوع نوشته شده‌اند تا فقط فرق هر مقدار دیده شود. موضوع مثال‌ها این است که زمان پاسخ به مشتری در سه ماه از ۴۸ ساعت به ۶ ساعت رسید (مثال ساختگی).

## ۱. ترتیب تصمیم‌ها

| گام | چه چیزی تعیین می‌شود | کی | ثابت یا متغیر |
| --- | --- | --- | --- |
| ۱ | سیاق | پیش از روایت | در کل متن ثابت |
| ۲ | جایگاه (من، ما، بیرونی) | پیش از روایت | ثابت؛ فقط در مرز بخش و با دلیل عوض می‌شود |
| ۳ | نسخه، و غایت و شاهد و ساخت آن | پیش از روایت | در کل متن یک غایت |
| ۴ | روایت سطح ۱ و تیترها، با فاصله و دما و آهنگ هر تیتر | سطح ۱ | از بخشی به بخش دیگر، هر بار یک پله |
| ۵ | روایت هر بخش و قاطعیت هر ادعا | سطح ۲ | ادعا به ادعا |
| ۶ | دمای جمله‌ها، تصویر، مثل و آهنگ واقعی | نوشتن متن | جمله به جمله، درون مرز بخش |

روایت با زبان ساده و خنثی نوشته می‌شود تا فقط منطقش داوری شود. لحن نهایی در گام ۶ می‌آید.

## ۲. بُعدها، هر کدام با یک مقسم

| بُعد | مقسم | کی تعیین می‌شود | مقدارها |
| --- | --- | --- | --- |
| غایت | خواننده پس از خواندن چه چیزی به دست می‌آورد | پیش از روایت | گزارش · تبیین · اقناع · فراخوان · یادمان |
| شاهد غالب | نتیجه‌ی متن بر کدام منبع اعتبار تکیه دارد | پیش از روایت | تجربه · واقعیت جاری · تاریخ · مفهوم · مرجع |
| جایگاه | شخص دستوری ادعاهای اصلی | پیش از روایت | من · ما · بیرونی |
| ساخت | بخش‌ها بر چه اساسی پشت سر هم می‌آیند | روایت سطح ۱ | زمانی · زنجیره‌ای · فهرستی · تقابلی · شاخه‌ای |
| سیاق | نوع سند و رابطه‌ی رسمی نویسنده با خواننده | پیش از روایت | رسمی‌انسانی · اداری · نیمه‌رسمی · محاوره‌ی نوشتاری · علمی |
| فاصله | نویسنده چطور خواننده را خطاب می‌کند | روایت سطح ۱ (برای هر تیتر) | دور · میانه · نزدیک |
| قاطعیت | نشانه‌های یقین در ادعاها | روایت سطح ۲ (برای هر ادعا) | قاطع · سنجیده · محتاط |
| دما | رنگ عاطفی، تصویر و ارزش‌گذاری | نوشتن متن | خنثی · گرم · پرشور |
| آهنگ | طول جمله و پاراگراف و تراکم ربط (سنجیده با پیکره) | روایت سطح ۱ (برای هر تیتر) | تحلیلی میانه · استدلالی پیوسته · گفت‌وگویی شخصی · خطابی · گزارشی برند · گزارشی نهادی · فشرده |

«لحن» در این اسکیل نام سه بُعد فاصله، قاطعیت و دماست. سیاق جداست، چون مقسمش نوع سند است، نه حال‌وهوای جمله‌ها. غایت، شاهد، جایگاه و ساخت چهار محور سبک‌اند (style-framework.md).

## ۳. هر مقدار، با نشانه و مثال

### غایت

| مقدار | نشانه | مثال |
| --- | --- | --- |
| گزارش | دانستن آنچه رخ داده | «زمان پاسخ به مشتری به ۶ ساعت رسید.» |
| تبیین | فهم چرایی یا چگونگی | «زمان پاسخ کم شد، چون درخواست‌ها حالا خودکار به کارشناس همان موضوع می‌رسند.» |
| اقناع | پذیرفتن داوری‌ای که محل بحث است | «پس بقیه‌ی واحدها هم باید همین سامانه را به کار بگیرند.» |
| فراخوان | قصد انجام کاری از سوی خواننده یا «ما» | «تا پایان سال همه‌ی پاسخ‌ها را به زیر سه ساعت برسانیم.» |
| یادمان | حس، خاطره یا بزرگداشت | «این کار را مدیون تیمی هستیم که سه ماه تا دیروقت ماند.» |

### شاهد غالب

| مقدار | نشانه | مثال |
| --- | --- | --- |
| تجربه | چشم خود نویسنده؛ فقط تجربه‌ی واقعی | «روز اولی که سامانه راه افتاد، خودم پشت میز پشتیبانی بودم.» |
| واقعیت جاری | سند، عدد یا رویداد امروز، با منبع | «گزارش واحد پشتیبانی نشان می‌دهد میانگین پاسخ ۶ ساعت است.» |
| تاریخ | گذشته‌ای که نویسنده شاهدش نبوده | «ده سال پیش هم همین شرکت یک بار زمان پاسخ را نصف کرد.» |
| مفهوم | تعریف، تمایز یا چارچوب | «آنچه می‌توان «هزینه‌ی انتظار» نامید، با هر ساعت تأخیر بیشتر می‌شود.» |
| مرجع | متن یا شخص نام‌دار، با نقل دقیق و وارسی‌شده | «یک نقل‌قول دقیق از منبعی معتبر، با نام و جای آن.» |

### جایگاه

| مقدار | نشانه | مثال |
| --- | --- | --- |
| من | شاهد یا صاحب‌نظر شخصی | «در این سه ماه دیدم زمان پاسخ از دو روز به شش ساعت رسید.» |
| ما | سخنگوی یک گروه یا سازمان | «ما زمان پاسخ را در سه ماه به ۶ ساعت رساندیم.» |
| بیرونی | ناظر غیرشخصی؛ سازمان با نام خودش | «واحد پشتیبانی زمان پاسخ را در سه ماه به ۶ ساعت رساند.» |

### ساخت

| مقدار | نشانه | مثال |
| --- | --- | --- |
| زمانی | اول آنچه زودتر بوده | «فروردین شکایت‌ها اوج گرفت، خرداد سامانه آمد، تیر عددها پایین آمد.» |
| زنجیره‌ای | هر بخش از بخش قبل نتیجه می‌شود | «شکایت‌ها از تأخیر بود، پس مسیر درخواست را کوتاه کردیم، پس زمان پاسخ افتاد.» |
| فهرستی | نکته‌های هم‌ارز و مستقل | «سه نتیجه داشت: پاسخ سریع‌تر، شکایت کمتر، کارشناس آسوده‌تر.» |
| تقابلی | ادعای کسی، سپس پاسخ | «گفته می‌شد سرعت کیفیت را پایین می‌آورد، اما نمره‌ی کیفیت پاسخ‌ها بالا رفت.» |
| شاخه‌ای | چند احتمال کنار هم | «اگر حجم درخواست‌ها دو برابر شود یک راه داریم، و اگر ثابت بماند راه دیگری.» |

### سیاق

| مقدار | نشانه | مثال |
| --- | --- | --- |
| رسمی‌انسانی | صورت کامل نوشتاری، «شما»، بی‌اصطلاح عامیانه، ولی زنده و مستقیم | «زمان پاسخ به مشتری در سه ماه از ۴۸ ساعت به ۶ ساعت رسید.» |
| اداری | قراردادهای نامه‌ی اداری؛ بی‌«می‌باشد» و بی‌فعل سنگین | «به استحضار می‌رساند زمان پاسخ‌گویی به مشتریان در سه‌ماهه‌ی گذشته از ۴۸ به ۶ ساعت کاهش یافته است.» |
| نیمه‌رسمی | صورت نوشتاری با صدای گرم و خطاب مستقیم | «حالا مشتری‌ها به‌جای دو روز، ظرف شش ساعت جواب می‌گیرند.» |
| محاوره‌ی نوشتاری | شکسته‌نویسی و ادات گفتار | «الان ظرف شیش ساعت جواب مشتری‌ها رو می‌دیم، قبلاً دو روز طول می‌کشید.» |
| علمی | سنجیده، با قید، مجهول مجاز، بی‌تعارف | «میانگین زمان پاسخ در دوره‌ی سه‌ماهه‌ی مطالعه از ۴۸ به ۶ ساعت کاهش یافت.» |

### فاصله

| مقدار | نشانه | مثال |
| --- | --- | --- |
| دور | بدون خطاب؛ جمله‌های غیرشخصی | «زمان پاسخ به مشتری به ۶ ساعت رسیده است.» |
| میانه | خطاب گاه‌به‌گاه و ضمنی، بی‌پرسش از خواننده | «زمان پاسخ به ۶ ساعت رسیده، یعنی مشتری همان روز جواب می‌گیرد.» |
| نزدیک | فعل دوم‌شخص، «فرض کنید»، پرسش مستقیم | «اگر امروز درخواستی ثبت کنید، تا عصر جوابش را می‌گیرید.» |

### قاطعیت

| مقدار | نشانه | مثال |
| --- | --- | --- |
| قاطع | «است»، «باید»، «نشان می‌دهد» | «کاهش زمان پاسخ رضایت مشتری را بالا برده است.» |
| سنجیده | یک قید فقط جایی که واقعاً نامعلوم است | «کاهش زمان پاسخ احتمالاً در بالا رفتن رضایت مشتری اثر داشته است.» |
| محتاط | قید، شرط و بازه در بیشتر ادعاها | «اگر نظرسنجی سه ماه آینده هم همین را نشان دهد، می‌توان گفت کاهش زمان پاسخ بر رضایت اثر داشته است.» |

### دما

| مقدار | نشانه | مثال |
| --- | --- | --- |
| خنثی | صفت فقط وقتی واقعیت آن را بخرد؛ بی‌تصویر | «زمان پاسخ از ۴۸ ساعت به ۶ ساعت رسید.» |
| گرم | یک جزئیات انسانی، یک تصویر | «زمان پاسخ به ۶ ساعت رسید و مشتری‌ای که صبح مشکلش را می‌گوید، دیگر شب را با نگرانی نمی‌گذراند.» |
| پرشور | «ما»، تصویر مشترک، تکرار آغازین، فراخوان | «ما نشان دادیم که مشتری نباید دو روز منتظر بماند، و حالا که به شش ساعت رسیده‌ایم، دلیلی نمی‌بینیم همین‌جا بایستیم.» |

### آهنگ

| مقدار | نشانه | مثال |
| --- | --- | --- |
| تحلیلی میانه | جمله‌ی حدود ۱۸ کلمه، پاراگراف ۴۰ تا ۹۰ کلمه، ربط زیاد | ستون‌نویسان تحلیلی |
| استدلالی پیوسته | جمله‌ی حدود ۱۸ کلمه با «که» و ربط فراوان، پاراگراف ۵۷ تا ۸۲ کلمه | ستون‌نویسان استدلالی |
| گفت‌وگویی شخصی | جمله‌ی حدود ۱۵ کلمه، پاراگراف ۳۰ تا ۵۶ کلمه | جستارنویسان و وبلاگ‌های آموزشی |
| خطابی | جمله‌ی ۱۲ تا ۱۹ کلمه، ربط کم؛ شاهد ضعیف (یک نویسنده) | بیانیه و سخنرانی |
| گزارشی برند | جمله‌ی حدود ۲۳ کلمه، ربط کم، عدد زیاد | گزارش سالانه‌ی شرکت‌های مصرفی |
| گزارشی نهادی | جمله‌ی حدود ۲۵ کلمه، پاراگراف بلند | گزارش پایداری و هیئت‌مدیره |
| فشرده | جمله‌ی ۶ تا ۱۲ کلمه، هر جمله یک واقعیت؛ تأییدنشده | خبر و اطلاعیه |

## ۴. ماتریس سیاق در برابر لحن و جایگاه و آهنگ

● مناسب · ○ فقط با دلیل · ✗ نامناسب. ○ یعنی فقط با دلیل؛ اگر نسخه یا نوع بخش همان مقدار را پیش‌فرض گرفته باشد، دلیلش همان است.

| سیاق | جایگاه: من / ما / بیرونی | فاصله: دور / میانه / نزدیک | قاطعیت: قاطع / سنجیده / محتاط | دما: خنثی / گرم / پرشور |
| --- | --- | --- | --- | --- |
| رسمی‌انسانی | ● / ● / ● | ● / ● / ○ | ● / ● / ● | ● / ● / ○ |
| اداری | ○ / ● / ● | ● / ○ / ✗ | ● / ● / ○ | ● / ○ / ✗ |
| نیمه‌رسمی | ● / ● / ● | ○ / ● / ● | ● / ● / ● | ● / ● / ○ |
| محاوره‌ی نوشتاری | ● / ● / ○ | ✗ / ○ / ● | ● / ● / ● | ○ / ● / ● |
| علمی | ✗ / ○ / ● | ● / ○ / ✗ | ○ / ● / ● | ● / ✗ / ✗ |

| سیاق | آهنگ‌های نامناسب یا با احتیاط |
| --- | --- |
| رسمی‌انسانی | همه مناسب |
| اداری | گفت‌وگویی شخصی ✗، خطابی ✗، استدلالی پیوسته ○ |
| نیمه‌رسمی | گزارشی نهادی ○ |
| محاوره‌ی نوشتاری | گزارشی نهادی ✗، گزارشی برند ○ |
| علمی | گفت‌وگویی شخصی ✗، خطابی ✗، فشرده ✗ |

## ۵. ماتریس نسخه‌ها

مقدار پررنگ پیش‌فرض نسخه است و مقدارهای داخل پرانتز هم برای آن نسخه معنا دارند. هر مقدار دیگری برای آن نسخه بی‌معناست و در صفحه‌ی تنظیمات غیرفعال است.

| نسخه | کاربرد | غایت | شاهد غالب | جایگاه | ساخت | سیاق | فاصله | قاطعیت | دما | آهنگ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| تحلیل مفهومی | توضیح یک پدیده از راه یک مفهوم | **تبیین** (اقناع) | **مفهوم** (واقعیت جاری، تاریخ، مرجع) | **بیرونی** (من) | **زنجیره‌ای** (تقابلی) | **رسمی‌انسانی** (نیمه‌رسمی، علمی) | **میانه** (دور، نزدیک) | **سنجیده** (قاطع، محتاط) | **خنثی** (گرم) | **تحلیلی میانه** (استدلالی پیوسته، گفت‌وگویی شخصی) |
| توجیه راهبردی | سناریوها و نشانه‌ها برای یک تصمیم | **تبیین** (اقناع) | **واقعیت جاری** (تاریخ، مفهوم) | **بیرونی** (ما) | **شاخه‌ای** | **رسمی‌انسانی** (اداری، علمی) | **دور** (میانه) | **سنجیده** (محتاط) | **خنثی** | **تحلیلی میانه** (گزارشی نهادی) |
| سند راهبردی | راهبرد، نقشه‌ی راه یا پیشنهاد به هیئت‌مدیره (موقت) | **اقناع** (فراخوان) | **واقعیت جاری** (مفهوم، تجربه) | **بیرونی** (ما) | **زنجیره‌ای** (شاخه‌ای) | **رسمی‌انسانی** (اداری) | **میانه** (دور) | **قاطع** (سنجیده) | **خنثی** (گرم) | **تحلیلی میانه** (استدلالی پیوسته، گزارشی برند، گزارشی نهادی) |
| استدلال روزنامه‌ای | یادداشت یا ستون نظر درباره‌ی موضوع روز | **اقناع** | **واقعیت جاری** (تجربه، تاریخ، مفهوم) | **من** (ما) | **زنجیره‌ای** (فهرستی) | **نیمه‌رسمی** (رسمی‌انسانی) | **نزدیک** (میانه) | **قاطع** (سنجیده) | **گرم** (خنثی، پرشور) | **استدلالی پیوسته** (تحلیلی میانه، گفت‌وگویی شخصی) |
| جدل | پاسخ به یک ادعای منتشرشده | **اقناع** | **واقعیت جاری** (تاریخ، مفهوم، مرجع، تجربه) | **من** (بیرونی) | **تقابلی** | **رسمی‌انسانی** (نیمه‌رسمی، علمی) | **میانه** (دور، نزدیک) | **قاطع** (سنجیده) | **خنثی** (گرم) | **استدلالی پیوسته** (تحلیلی میانه) |
| عبرت تاریخی | قاعده‌ای برای امروز از دل تاریخ | **اقناع** (تبیین) | **تاریخ** | **بیرونی** (من) | **زمانی** (تقابلی) | **رسمی‌انسانی** (نیمه‌رسمی، علمی) | **میانه** (دور) | **سنجیده** (قاطع) | **خنثی** (گرم) | **تحلیلی میانه** (استدلالی پیوسته) |
| روایت شاهد | شروع از صحنه‌ای که نویسنده خودش دیده | **تبیین** (اقناع، یادمان) | **تجربه** | **من** (ما) | **زمانی** | **نیمه‌رسمی** (رسمی‌انسانی، محاوره‌ی نوشتاری) | **نزدیک** (میانه) | **سنجیده** (قاطع، محتاط) | **گرم** (خنثی) | **گفت‌وگویی شخصی** (تحلیلی میانه) |
| خطابه | بیانیه یا پیام به یک جمع در یک موقعیت مشخص | **فراخوان** | **مرجع** (تجربه، تاریخ) | **ما** | **فهرستی** (زمانی) | **رسمی‌انسانی** (نیمه‌رسمی) | **نزدیک** (میانه) | **قاطع** | **پرشور** (گرم) | **خطابی** (گفت‌وگویی شخصی) |
| توضیح و آموزش | دادن یک ابزار یا روش به خواننده | **تبیین** | **مفهوم** (تجربه، واقعیت جاری) | **من** (ما، بیرونی) | **فهرستی** (زنجیره‌ای) | **نیمه‌رسمی** (رسمی‌انسانی، محاوره‌ی نوشتاری، علمی) | **نزدیک** (میانه) | **سنجیده** (قاطع) | **گرم** (خنثی) | **گفت‌وگویی شخصی** (تحلیلی میانه، فشرده) |
| تأمل شخصی | تأملی شخصی و صادقانه، بی‌ادعای قطعیت | **یادمان** (تبیین) | **تجربه** (مفهوم، مرجع) | **من** | **زنجیره‌ای** (زمانی) | **نیمه‌رسمی** (محاوره‌ی نوشتاری، رسمی‌انسانی) | **نزدیک** (میانه) | **محتاط** (سنجیده) | **گرم** (خنثی) | **گفت‌وگویی شخصی** (تحلیلی میانه) |
| سوگ‌نامه | یاد یک شخص | **یادمان** | **تجربه** (تاریخ) | **من** (ما) | **زمانی** | **رسمی‌انسانی** (نیمه‌رسمی) | **نزدیک** (میانه) | **سنجیده** (قاطع) | **گرم** | **گفت‌وگویی شخصی** (تحلیلی میانه) |
| گزارش داده‌محور برند | گزارش سالانه یا دوره‌ای شرکت‌های مصرفی | **گزارش** (تبیین) | **واقعیت جاری** (تجربه) | **ما** (بیرونی) | **فهرستی** (زمانی) | **رسمی‌انسانی** (نیمه‌رسمی) | **میانه** (دور، نزدیک) | **قاطع** (سنجیده) | **گرم** (خنثی) | **گزارشی برند** (تحلیلی میانه، فشرده) |
| گزارش نهادی | گزارش پایداری، هیئت‌مدیره یا نهادی | **گزارش** | **واقعیت جاری** | **بیرونی** (ما) | **فهرستی** | **رسمی‌انسانی** (اداری، علمی) | **دور** (میانه) | **قاطع** (سنجیده) | **خنثی** | **گزارشی نهادی** (گزارشی برند) |
| خبر کوتاه | خبر، اطلاعیه، یادداشت انتشار | **گزارش** | **واقعیت جاری** | **بیرونی** (ما) | **فهرستی** | **رسمی‌انسانی** (اداری، نیمه‌رسمی، محاوره‌ی نوشتاری) | **دور** (میانه) | **قاطع** | **خنثی** | **فشرده** |

| نسخه | واحد روایت | پرسش پیونددهنده | جای نتیجه |
| --- | --- | --- | --- |
| تحلیل مفهومی | ادعا | چرا؟ یعنی چه؟ | پیش‌بینی در پایان |
| توجیه راهبردی | سناریو و نشانه | اگر این شود چه؟ | حرکت مقاوم در پایان |
| سند راهبردی | ادعا | چرا؟ پس چه؟ بهایش چیست؟ | پاسخ در خلاصه، درخواست در پایان |
| استدلال روزنامه‌ای | ادعا | چرا؟ ولی چه؟ | توصیه در پایان |
| جدل | ادعای طرف و پاسخ | درست است؟ | پرسش از طرف مقابل |
| عبرت تاریخی | رویداد تاریخ‌دار | بعد چه شد؟ قاعده چیست؟ | امروز در پایان |
| روایت شاهد | لحظه | بعد چه شد؟ یعنی چه؟ | معنا پس از صحنه |
| خطابه | گام عاطفی | حالا چه باید کرد؟ | فراخوان در پایان |
| توضیح و آموزش | کار خواننده | چطور؟ بعد چه کنم؟ | حد ابزار در پایان |
| تأمل شخصی | پرسش و راه میانه | پس چه؟ | پایان باز |
| سوگ‌نامه | خاطره | بعد؟ | تسلیت در پایان |
| گزارش داده‌محور برند | یافته (عدد و معنا) | یعنی چه؟ چرا شد؟ | چشم‌انداز در پایان |
| گزارش نهادی | یافته با استاندارد | طبق چه؟ | هدف‌های سال بعد در پایان |
| خبر کوتاه | واقعیت | دیگر چه؟ | خبر اصلی در جمله‌ی اول، گام بعد در پایان |

## ۶. ماتریس نوع بخش در متن بلند

پیش‌فرض لحن و آهنگ هر تیتر در روایت سطح ۱. نمونه‌ی مشتری یا صحنه‌ی واقعی معمولاً یک پاراگراف درون یک بخش است، نه بخشی جدا؛ برای همین در این جدول نیامده و قاعده‌اش در بخش ۷ است.

| نوع بخش | کار بخش | فاصله | قاطعیت | دما | آهنگ | واحد روایت |
| --- | --- | --- | --- | --- | --- | --- |
| خلاصه‌ی مدیریتی | پاسخ و درخواست در کوتاه‌ترین شکل | میانه | قاطع | خنثی | تحلیلی میانه | ادعا |
| مسئله و وضعیت | آنچه خواننده می‌پذیرد، و گره | میانه | قاطع | خنثی | تحلیلی میانه | ادعا |
| تحلیل و تبیین | سازوکار | میانه | سنجیده | خنثی | تحلیلی میانه | ادعا |
| استدلال و ضرورت | قبولاندن یک داوری | میانه | قاطع | خنثی | استدلالی پیوسته | ادعا |
| معرفی مدل یا راه‌حل | اجزا و پیوندشان | میانه | قاطع | خنثی | تحلیلی میانه | جزء |
| وضع موجود و یافته‌ها | عدد و معنای آن | دور | قاطع | خنثی | گزارشی برند | یافته |
| برنامه و نقشه‌ی راه | فاز، شاخص، شرط پایان | دور | قاطع | خنثی | گزارشی برند | گام |
| ریسک‌ها | آنچه ممکن است خراب شود | میانه | سنجیده | خنثی | تحلیلی میانه | سناریو |
| چشم‌انداز | صحنه‌ی موفقیت | میانه | قاطع | گرم | تحلیلی میانه | صحنه |
| درخواست یا فراخوان | تصمیم یا اقدام | نزدیک | قاطع | گرم | تحلیلی میانه | درخواست |

## ۷. قاعده‌ی حرکت لحن میان بخش‌ها

- **ثابت در کل متن:** سیاق و جایگاه. جایگاه فقط در مرز بخش و با دلیل عوض می‌شود.
- **در هر مرز:** فاصله، قاطعیت و دما هر کدام حداکثر یک پله جابه‌جا می‌شوند. آهنگ اگر به همسایه‌اش برود آزاد است، وگرنه آغاز بخش تازه یک جمله‌ی پل می‌خواهد.
- **درون یک بخش:** فقط یک پاراگراف می‌تواند از لحن بخش جدا شود، مثلاً پاراگراف نمونه‌ی واقعی که گرم‌تر و نزدیک‌تر است.
- **سیاق بر همه مقدم است:** اگر لحن بخشی با سیاق متن در خانه‌ی ✗ بیفتد، لحن بخش عوض می‌شود، نه سیاق.

همسایه‌های آهنگ:

| آهنگ | همسایه‌ها |
| --- | --- |
| تحلیلی میانه | استدلالی پیوسته، خطابی، گزارشی نهادی |
| استدلالی پیوسته | تحلیلی میانه، خطابی |
| گفت‌وگویی شخصی | خطابی، تحلیلی میانه |
| خطابی | گفت‌وگویی شخصی، تحلیلی میانه |
| گزارشی برند | گزارشی نهادی، خطابی |
| گزارشی نهادی | گزارشی برند، تحلیلی میانه |
| فشرده | خطابی، گفت‌وگویی شخصی |

پیش‌فرض‌ها هموار می‌شوند. میان دو بخش پشت سر هم، فاصله و قاطعیت و دما حداکثر یک پله جابه‌جا می‌شوند و آهنگ فقط به همسایه‌اش می‌رود. پیش‌فرضی که بپرد، به آهنگی کشیده می‌شود که همسایه‌ی هر دو طرف است؛ آهنگ خطابی پل به حساب نمی‌آید، چون همسایگی‌اش از پهنای بازه‌هایش است. در گزارش‌ها همه‌ی بخش‌ها یک آهنگ دارند.

### ترتیب پیش‌فرض بخش‌ها برای نسخه‌های بلند (هموارشده)

این ترتیب‌ها همان‌هایی‌اند که صفحه‌ی تنظیمات پیشنهاد می‌دهد. مقدارهایی که هموارسازی از پیش‌فرض نوع بخش عوض کرده، با ⇠ علامت خورده‌اند.

**تحلیل مفهومی**

| بخش | فاصله | قاطعیت | دما | آهنگ |
| --- | --- | --- | --- | --- |
| مسئله و وضعیت | میانه | قاطع | خنثی | تحلیلی میانه |
| تحلیل و تبیین | میانه | سنجیده | خنثی | تحلیلی میانه |
| استدلال و ضرورت | میانه | قاطع | خنثی | استدلالی پیوسته |
| چشم‌انداز | میانه | قاطع | گرم | تحلیلی میانه |

**توجیه راهبردی**

| بخش | فاصله | قاطعیت | دما | آهنگ |
| --- | --- | --- | --- | --- |
| خلاصه‌ی مدیریتی | میانه | قاطع | خنثی | تحلیلی میانه |
| مسئله و وضعیت | میانه | قاطع | خنثی | تحلیلی میانه |
| تحلیل و تبیین | میانه | سنجیده | خنثی | تحلیلی میانه |
| ریسک‌ها | میانه | سنجیده | خنثی | تحلیلی میانه |
| درخواست یا فراخوان | نزدیک | قاطع | گرم | تحلیلی میانه |

**سند راهبردی**

| بخش | فاصله | قاطعیت | دما | آهنگ |
| --- | --- | --- | --- | --- |
| خلاصه‌ی مدیریتی | میانه | قاطع | خنثی | تحلیلی میانه |
| مسئله و وضعیت | میانه | قاطع | خنثی | تحلیلی میانه |
| استدلال و ضرورت | میانه | قاطع | خنثی | استدلالی پیوسته |
| معرفی مدل یا راه‌حل | میانه | قاطع | خنثی | تحلیلی میانه |
| وضع موجود و یافته‌ها | دور | قاطع | خنثی | گزارشی نهادی ⇠ |
| برنامه و نقشه‌ی راه | دور | قاطع | خنثی | گزارشی برند |
| ریسک‌ها | میانه | سنجیده | خنثی | گزارشی نهادی ⇠ |
| چشم‌انداز | میانه | قاطع | گرم | تحلیلی میانه |
| درخواست یا فراخوان | نزدیک | قاطع | گرم | تحلیلی میانه |

**استدلال روزنامه‌ای**

| بخش | فاصله | قاطعیت | دما | آهنگ |
| --- | --- | --- | --- | --- |
| مسئله و وضعیت | میانه | قاطع | خنثی | تحلیلی میانه |
| استدلال و ضرورت | میانه | قاطع | خنثی | استدلالی پیوسته |
| درخواست یا فراخوان | نزدیک | قاطع | گرم | تحلیلی میانه |

**جدل**

| بخش | فاصله | قاطعیت | دما | آهنگ |
| --- | --- | --- | --- | --- |
| مسئله و وضعیت | میانه | قاطع | خنثی | تحلیلی میانه |
| استدلال و ضرورت | میانه | قاطع | خنثی | استدلالی پیوسته |
| درخواست یا فراخوان | نزدیک | قاطع | گرم | تحلیلی میانه |

**گزارش داده‌محور برند**

| بخش | فاصله | قاطعیت | دما | آهنگ |
| --- | --- | --- | --- | --- |
| خلاصه‌ی مدیریتی | میانه | قاطع | خنثی | گزارشی برند ⇠ |
| وضع موجود و یافته‌ها | دور | قاطع | خنثی | گزارشی برند |
| تحلیل و تبیین | میانه | سنجیده | خنثی | گزارشی برند ⇠ |
| برنامه و نقشه‌ی راه | دور | قاطع | خنثی | گزارشی برند |
| چشم‌انداز | میانه | قاطع | گرم | گزارشی برند ⇠ |

**گزارش نهادی**

| بخش | فاصله | قاطعیت | دما | آهنگ |
| --- | --- | --- | --- | --- |
| خلاصه‌ی مدیریتی | میانه | قاطع | خنثی | گزارشی نهادی ⇠ |
| وضع موجود و یافته‌ها | دور | قاطع | خنثی | گزارشی نهادی ⇠ |
| تحلیل و تبیین | میانه | سنجیده | خنثی | گزارشی نهادی ⇠ |
| ریسک‌ها | میانه | سنجیده | خنثی | گزارشی نهادی ⇠ |
| برنامه و نقشه‌ی راه | دور | قاطع | خنثی | گزارشی نهادی ⇠ |

## ۸. آنچه در بازبینی این ماتریس اصلاح شد

- **استدلال روزنامه‌ای:** سیاق پیش‌فرضش رسمی‌انسانی بود و فاصله‌اش نزدیک، در حالی که نزدیک در رسمی‌انسانی «با احتیاط» است. سیاق پیش‌فرض به نیمه‌رسمی تغییر کرد.
- **سوگ‌نامه:** قاطعیت پیش‌فرض «قاطع» بود؛ سوگ‌نامه ادعای بحث‌برانگیز ندارد و «سنجیده» درست‌تر است.
- **ریسک‌ها:** «محتاط» بود و در سند راهبردی میان «برنامه» و «چشم‌انداز» که هر دو قاطع‌اند، دو پله پرش می‌ساخت. به «سنجیده» تغییر کرد.
- **پرش آهنگ در پیش‌فرض‌ها:** در سند راهبردی، آهنگ از «معرفی مدل» به «وضع موجود» و از «برنامه» به «ریسک‌ها» به آهنگی غیرهمسایه می‌پرید. حالا پیش‌فرض‌ها هموار می‌شوند و این دو بخش آهنگ گزارشی نهادی می‌گیرند، که همسایه‌ی هر دو طرف است. در دو نسخه‌ی گزارشی، همه‌ی بخش‌ها آهنگ خود نسخه را دارند.
- **لحن کلی در متن بلند:** در صفحه‌ی تنظیمات، لحن و آهنگ کلی متن در متن بلند بی‌اثر بود و صفحه این را نمی‌گفت. حالا در متن بلند فقط در بخش‌ها تنظیم می‌شود.
- **نمونه یا روایت مشتری:** از فهرست نوع بخش‌ها بیرون آمد، چون با قاعده‌ی یک‌پله‌ای ناسازگار بود. حالا یک پاراگراف مجاز درون بخش است.
- **خبر کوتاه:** آهنگ فشرده در سیاق رسمی‌انسانی «با احتیاط» علامت خورده بود، در حالی که پیش‌فرض همین نسخه است. محدودیت برداشته شد.
- **سیاق علمی:** به هیچ نسخه‌ای وصل نبود. حالا در تحلیل مفهومی، جدل، عبرت تاریخی، توضیح و آموزش، توجیه راهبردی و گزارش نهادی مجاز است.
- **«با احتیاط» در برابر پیش‌فرض نسخه:** وقتی نسخه‌ای مقداری را پیش‌فرض گرفته که در سیاقش «با احتیاط» است، مانند نزدیکی و شور در خطابه، دلیلش همان نسخه است و تناقضی نیست.

## ۹. شواهد و حد اعتماد

- **آهنگ** سنجیده شده است، روی پیکره‌ی ۶۲۰ متن نُه نویسنده و یازده گزارش شرکت‌ها (style-evidence.md).
- **سیاق** از قاعده‌های تشخیص سیاق در writing-style.md آمده، نه از سنجش آماری.
- **فاصله، قاطعیت و دما**، مجازها و پیش‌فرض‌های جدول‌های ۵ و ۶ قرارداد اسکیل‌اند. از خواندن پیکره، سه مقاله‌ی دیلویت و آزمون‌های سبک با کاربر بیرون آمده‌اند و هنوز سنجیده نشده‌اند. ابزار `style_check` امروز فقط آهنگ را می‌سنجد.



---

# PART 6 — Style arcs: think before writing

# Style arcs: think in the style before writing in it

Read storyline.md first. A skeleton below is the **arc** of a recipe: which
kinds of claims the text needs and where its payoff goes. It is a plan, not a
text. Writing from the slots directly produced paragraphs that sat side by
side, because a slot names a role («diagnosis»), not a claim. The arc is used
to write the level-1 storyline, whose sentences are claims; the prose is
written from the storyline.

A style is a way of thinking, not a vocabulary. In the calibration test on a
real strategy topic, the samples that failed had the right tone and rhythm but
the wrong thinking: a «strategic» text that opened by stating its proposal, a
brand report that gave away its targets in the first paragraph, an explainer
that opened by announcing what it was not, scenarios that were not derived from
anything. The words were arranged in the style; the content was not built in it.

So every text is built in three steps (storyline.md gives the detail):

1. **Build the skeleton.** Take the recipe's skeleton below and fill every slot
   with real content from the material: a sentence or a note per slot, not prose.
   If a slot cannot be filled, the style does not fit this content (or the
   material is missing): change the style or ask. Do not write around an empty slot.
2. **Turn the filled arc into a storyline**: claim sentences in order, each
   answering the question the previous one raises, under plain headings.
3. **Write from the storyline.** Each storyline sentence opens a paragraph. The
   arc decides where the payoff goes; the prose never moves it forward to
   announce it.

For long or high-stakes texts, show the skeleton to the user before drafting.
It is shorter than a draft and cheaper to correct.

## Rules that hold for every skeleton

- **Where the payoff goes is part of the style.** Reports end on what comes next; arguments state the claim early and earn it; narratives give the meaning after the scene; strategy opens on the situation, not on the answer.
- **Never shout the style in the first line.** No «این یادداشت … نیست», no «این سند پیشنهاد می‌کند…» as an opener, no «در این بخش به … می‌پردازیم». The first line does the style's first move.
- **No announcing openers in series.** Paragraphs that each begin «معیار نخست…»، «مسیر دوم…» read as a form. Enumeration belongs in the skeleton, not in the prose.
- **Fit test.** A style fits when its slots can be filled with real content. خطابه needs a speaker with standing, a «ما» and an occasion; روایت شاهد needs a scene; توجیه راهبردی needs real uncertainties. When the fit is weak, say so and propose the nearer style.
- **Reasoning is free, facts are fixed.** Slots like «diagnosis», «crux», «trade-off» and «indicator» are the writer's thinking and should be filled boldly; names, figures, dates and quotations come only from the material.

## Skeletons per recipe

### تحلیل مفهومی
1. The phenomenon the usual words do not explain.
2. The concept, named in «» and defined in one sentence.
3. Its neighbour, and the one difference that matters.
4. The case read through the concept, with facts.
5. What the concept predicts or changes in how we act. (Payoff at the end.)

### توجیه راهبردی (scenarios for a decision)
1. The decision and its horizon: who must choose what, by when.
2. **Drivers**: the two uncertainties that most change the answer. They must come from the material, and each must be genuinely open.
3. Scenarios built from the drivers (two to four); each gets a short name, what it looks like, and the **leading indicators** that would show it is arriving.
4. For each scenario, what it implies for the decision.
5. Assessment: likeliest versus most dangerous, and why they differ.
6. **The robust move**: what to do now that is right in every scenario, and the trigger that would justify the bigger move. (Payoff at the end.)

Weak signs: scenarios that are just good and bad outcomes; indicators that cannot be observed; no link from scenarios back to the decision.

### سند راهبردی (strategy document)
Built on the kernel of strategy (Rumelt, *Good Strategy / Bad Strategy*, 2011):
diagnosis, guiding policy, coherent actions.
1. **Diagnosis**: what is really going on. The situation and its tension, from the material; this is the opening, not the proposal.
2. **The crux**: the one obstacle that, once overcome, unlocks the rest. Name it.
3. **Guiding policy**: the approach to the crux, including **what will no longer be done** and the price of that choice. A strategy without a trade-off is a wish.
4. **Alternatives considered** and why each fails on the crux, stated fairly.
5. **Coherent actions**: phases that reinforce each other, each with an exit criterion.
6. **Why now**: the cost of waiting.
7. **What must be true** for it to work, resources and risks, and the decision asked of the reader. (The ask comes last, after it has been earned.)

Weak signs: the first sentence is «پیشنهاد … این است که»; no trade-off; goals listed as strategy («رهبری بازار» is an aim, not a policy); actions that do not follow from the diagnosis.

### استدلال روزنامه‌ای
1. A hook: a fresh fact or observation.
2. The claim, in first person.
3. Two or three reasons, each resting on one checkable fact.
4. The strongest objection, conceded honestly.
5. The turn: why the claim survives the objection.
6. A recommendation to a named actor; optionally one proverb.

### جدل
1. The opposing claim, stated fairly and attributed (who, where, when).
2. What is right in it.
3. Numbered rebuttals, each on one fact.
4. A question the other side must answer.

### عبرت تاریخی
1. Today's puzzle.
2. Past cases in order, dated and verified.
3. The rule they share.
4. What the rule says about today.

### روایت شاهد
1. The scene: time, place, people, one concrete detail.
2. The moment of surprise or friction.
3. What it revealed: the turn from scene to analysis.
4. The generalisation, checked against more than this one scene.
5. A short verdict.
The meaning comes after the scene; never explain the scene before showing it.
A deliverable needs a real scene from the user. A calibration sample may use an
illustrative scene, marked as invented.

### خطابه
Fit first: a speaker with standing, a «ما» audience, an occasion (a launch, a loss, a decision). Without an occasion, choose another style.
1. The shared situation in one image.
2. What «ما» have been through.
3. What is at stake now.
4. Commitments, with anaphora three times at most.
5. One exact, verified quotation or verse.
6. The call, addressed to «ما».

### توضیح و آموزش
1. The reader's problem, in the reader's terms (a situation, not a disclaimer).
2. The tool, named and defined.
3. Steps or questions the reader applies.
4. One worked example on a real case.
5. The tool's limits, at the end.

### تأمل شخصی
1. The question that will not leave the writer.
2. Two errors to avoid.
3. The narrow path between them, hedged honestly.
4. An open ending.

### سوگ‌نامه
1. The person and the shared history, in order.
2. Two or three specific memories.
3. The work, named exactly.
4. Condolence.

### گزارش داده‌محور برند
1. **What happened** in the period, in one line: the change, not the plan.
2. Sections, each: a headline, a figure, its meaning, its cause.
3. A real customer or employee story, if the material has one.
4. Caveats: what is not measured yet, how terms are defined.
5. **What comes next**: targets and plans, at the end. Never in the opening.

### گزارش نهادی
1. Scope and standard of the report.
2. Per topic: the commitment, the process with its actor, the figure, the standard.
3. Gaps and next year's targets at the end.

### خبر کوتاه
1. Who did what, when (the lead).
2. Supporting facts, one per sentence, most important first.
3. Context in one sentence.
4. The next step or the source.



---

# PART 7 — Signature moves per style

# Signature moves per recipe

A move is something a writer does with a sentence or a paragraph: how they open,
turn, persuade and close. Numbers (style-framework.md §3) set the rhythm; moves
make a recipe recognisable. They were found by reading the reference corpus and
checked by counting them across all writers (style-evidence.md). Every example
below is invented for this file; none is quoted from a source text.

How to use: pick two to four moves from the recipe, not all of them. One move
used well reads as style; every move at once reads as a template.

## Shared toolkit (every analytic recipe)

These appear in most writers, so they mark good analytic prose in general, not a
particular recipe:
- A first-person stance at the turning point: «به نظر من…»، «به گمانم…»
- Concede, then turn: «البته … اما/ولی …»
- A rhetorical question that sets up the next paragraph (not a chain of them).
- The negation cascade «نه … نه … بلکه …» to clear wrong explanations before the right one.
- A short historical comparison in one clause.
- At most one line of irony per text.

## تحلیل مفهومی
- **Define before use.** Introduce the concept in «» and define it in the next sentence: «آنچه می‌توان آن را «جنگ معلق» نامید، وضعیتی است که…»
- **Distinguish it from its neighbour.** «جنگ معلق با بن‌بست فرق دارد: در بن‌بست…»
- **Read the case through it**, with dated facts.
- **Close on what the concept predicts**, not on a summary.
- Optional: an English equivalent in parentheses for a technical term, at most once or twice.

## توجیه راهبردی
- **Frame as levels or scenarios**, each a paragraph: «سناریوی نخست…».
- **Give indicators for each scenario**: what would we see if this one is happening.
- **Read the other side's intent**, attributed to evidence: «اگر … پس طرف مقابل احتمالاً…».
- **End with an assessment and a risk**: which scenario is likeliest and which is most dangerous, and why they differ.

## استدلال روزنامه‌ای
- **State the claim in first person**, inside the argument rather than as an announcement: «به نظر من…». The corpus columnists sometimes open with «در این یادداشت می‌خواهم…»; use it once at most, never as a pattern.
- **From observation to generalisation**: a concrete case, then «این رفتار در … بیشتر دیده می‌شود».
- **Concede and turn**: «البته … ولی …».
- **A folk analogy or proverb at the close**, one only: «تا تنور داغ است…».
- **A recommendation to a named actor**: «وزارت … باید …».

## جدل
- **State the claim fairly and attribute it**: who said what, when.
- **Numbered rebuttal**: ۱، ۲، ۳, each point resting on one checkable fact.
- **Concede what is true in the other side**: it makes the rebuttal credible.
- **One line of irony**, never a tone of contempt.
- **Close with a question the other side must answer.**

## عبرت تاریخی
- **Numbered chronological review** with exact dates; verify every date.
- **Extract a rule**: «هر جا … ، … ؛ هر جا … ، …».
- **Return to today** in the last paragraph: what the rule says about the present case.

## روایت شاهد
Requires an experience the user supplied. Do not invent one.
- **Open with the scene or a news hook**: «امروز…»، «سال هشتاد و هشت، یک روز…».
- **First-person past tense and reported dialogue**: «به او گفتم…».
- **Move from the scene to analysis** in the second half.
- **A short verdict sentence at the end**.

## خطابه
- **«ما»** throughout, and one image of the shared situation.
- **Anaphora**, three times at most: «یادمان باشد… یادمان باشد… یادمان باشد…».
- **An authority or a verse**, quoted exactly and verified.
- **A call to action addressed to «ما»**. Stay non-partisan unless the user sets the side.

## توضیح و آموزش
- **Open on the reader's problem**, as a situation in the reader's terms. Do not open with a disclaimer («این نوشته … نیست»); the limits of the tool go at the end.
- **Name the tool or framework** and define it.
- **Numbered steps or questions** the reader can apply.
- **One worked example** using the reader's real case.
- **A hedged conclusion**: what the tool can and cannot decide.

## تأمل شخصی
- **One honest hedge where it matters**, not a disclaimer at the top.
- **Hedges that are honest, not decorative**: «به گمانم»، «دست‌کم برای خودم».
- **Two errors to avoid**, and the narrow path between them.
- **An open ending**: a question or a provisional conclusion.

## سوگ‌نامه
- **The shared history in order**, with years and places.
- **Two or three specific memories**, from the user.
- **The person's work named exactly** (titles, roles).
- **Condolence at the end**, one paragraph.

## گزارش داده‌محور برند
- **A plain headline and a one-sentence lead per section**: «ابزارهای فروشندگان در یک سامانه», then the lead. No slogan, no colon in the headline.
- **Figure → meaning → cause**: «فروش کنسرو در ده روز اول اسفند دو برابر شد؛ یعنی خانوارها پیش از آغاز جنگ ذخیره کردند.»
- **The record sentence**, used sparingly: «رکورد سفارش روزانه در ۱۷ اسفند ثبت شد».
- **Category framing** in prose: «طرح‌های ما در سه دسته جای می‌گیرند که …», or a list after the sentence.
- **Definitional caveats** that build trust: «هر حساب کاربری الزاماً یک نفر نیست.»
- **A real customer or employee vignette** from the source material, never invented.

## گزارش نهادی
- **Name the standard or framework** behind each claim (GRI، ISO 22301).
- **Describe processes with the actor named**: «واحد حسابرسی داخلی هر سال … را بررسی می‌کند», not «بررسی به عمل می‌آید».
- **One value statement per section**, followed by evidence: «برای ما شکایت مشتری پایان کار نیست؛ … در ۱۴۰۴، …».
<!-- fa-lint-ignore-next-line -->
- **Replace bureaucratic forms**: می‌باشد → است، گردید → شد، نموده → کرده، صورت پذیرفت → انجام شد، در راستای → برای.

## خبر کوتاه
- **The lead fact first**: who, what, when, in the first sentence.
- **One fact per sentence**, figures exact.
- **No adjectives that the facts do not earn.**
- **The next step or source at the end.**

## سند راهبردی
Provisional (style-framework.md §2). Built from one rewritten roadmap; the section map is in style-framework.md §5.3.
- **Open on the diagnosis, not the proposal.** The situation and its tension come first; the decision asked of the reader comes after it has been earned. A first sentence of the form «پیشنهاد … این است که…» was judged the weakest opening in the calibration test (style-skeletons.md).
- **Name the concept the case rests on** and return to it in later sections: «مهاجرت به هوش مصنوعی دو بال دارد: سامانه و آمادگی پذیرش».
- **Name the crux and the trade-off**: the one obstacle the strategy removes, and what the organization will stop doing to remove it. A plan without something given up is a list of goals.
- **Lessons before plans**: what the organization learned, stated as findings; the plan follows as their consequence.
- **The ceiling argument**: today's model works but has a concrete limit; the proposed change removes it.
- **Problem before solution**: the «why now» section comes before the model.
- **Every phase in the same four parts**: هدف فاز، کار، شاخص‌ها، پایان فاز, with measurable exit criteria whose numbers match the table.
- **Check every number against the table** before delivery. A phase criterion that disagrees with the KPI table is the most common flaw.
- **Resources and risks get a section**, even a short one; a board asks first what it costs and what can fail. If the material is missing, say so; do not invent figures.
- **One concrete, dated scene at the end**, in the same position as the rest of the text (the organization by name, not «ما»).
- **Tone**: formal-but-human, no bureaucratic forms, Persian terms first with the English term in parentheses once.



---

# PART 8 — Orthography (نگارش و رسم‌الخط)

# Persian orthography: the mechanical layer

Correct orthography is what separates a professional Persian document from a
typed-in-a-hurry one. Readers may not name the rule, but they feel it. All of
this is enforceable: the persian_cleanup script (full package; chat-only AIs apply the equivalent rules manually) --edit` fixes the mechanical
layer automatically; the fa_lint script (full package; chat-only AIs apply the equivalent rules manually) --check` reports what needs judgment.

When *you* write documentation that must show a wrong form on purpose — as the
tables below do — suppress the linter on it rather than softening the example:

```markdown
<!-- fa-lint-ignore-next-line -->
یک خط با خطای عمدی

<!-- fa-lint-ignore-start -->
چند خط، مثلاً یک جدول کامل «غلط ← درست»
<!-- fa-lint-ignore-end -->
```

`--fix` puts suppressed lines back after the fix pass, so a deliberate error
survives. Codepoint notation such as `U+06CC` is never rewritten.

## 1. ZWNJ — نیم‌فاصله (U+200C)

The zero-width non-joiner separates morphemes *without* a visual gap while
preventing letter joining. Writing a full space (or nothing) instead is the
most common Persian typing error, and AI-generated Persian gets it wrong both
ways. In source: `‌`, HTML `&zwnj;`, or the literal character `‌`.

Required ZWNJ positions:

<!-- fa-lint-ignore-start -->

| Pattern | Wrong | Right |
|---|---|---|
| می/نمی + verb | می شود، نمی توانم، میشود* | می‌شود، نمی‌توانم |
| Plural ها | کتاب ها، سایت های | کتاب‌ها، سایت‌های |
| تر / ترین | بزرگ تر، مهم ترین | بزرگ‌تر، مهم‌ترین |
| Enclitic pronouns after ه | خانه ام، پروژه اش | خانه‌ام، پروژه‌اش |
| Compound prefixes | بی دقت، هم زمان | بی‌دقت، هم‌زمان |
| Compound words | وب سایت، صفحه بندی، نرم افزار | وب‌سایت، صفحه‌بندی، نرم‌افزار |
| ای after ه | حرفه ای، هفته ای | حرفه‌ای، هفته‌ای |

<!-- fa-lint-ignore-end -->

<!-- fa-lint-ignore-next-line -->
*میشود (fully attached) is acceptable only in colloquial register (میشه);
in formal text always می‌شود.

Lexicalized exceptions stay solid: همکار، بهتر، کمتر، بیشتر، امروزه، آنها
(آن‌ها also correct — pick one per document).

## 2. Persian characters, not Arabic

Keyboard/copy-paste contamination. These pairs look similar but are different
codepoints, break search, and render dotted/undotted wrongly:

<!-- fa-lint-ignore-start -->

| Use (Persian) | Never (Arabic) |
|---|---|
| ی U+06CC | ي U+064A |
| ک U+06A9 | ك U+0643 |
| ۀ/هٔ (or ه‌ی) | ة U+0629 |
| ۴۵۶ U+06F4.. | ٤٥٦ U+0664.. |

<!-- fa-lint-ignore-end -->

ه with hamza: خانهٔ من or خانه‌ی من — both accepted; be consistent per document.

## 3. Digits

- Persian digits ۰۱۲۳۴۵۶۷۸۹ everywhere inside Persian prose: dates
  (۱۴۰۴/۰۴/۱۷), prices (۲۵٬۰۰۰٬۰۰۰ تومان), counts, list numbers.
- Latin digits stay Latin inside: URLs, emails, phone numbers meant for
  international dialing (+98...), code, version strings (WordPress 6.5),
  file names.
<!-- fa-lint-ignore-next-line -->
- Never Arabic-Indic variants (٤ ٥ ٦).
- Percent: «۲۰٪» (U+066A) or «۲۰ درصد». In RTL both orders render fine if the
  digits are Persian; with Latin digits «20%» the run flips LTR.
- Thousands separator: ٬ (U+066C) or، comma-free spacing — one style per doc.

## 4. Punctuation

<!-- fa-lint-ignore-start -->

| Persian | Replaces | Note |
|---|---|---|
| ، U+060C | , | comma |
| ؛ U+061B | ; | semicolon |
| ؟ U+061F | ? | question mark |
| «...» | "..." | quotes (گیومه) |
| … | ... | ellipsis, or سه‌نقطه |

<!-- fa-lint-ignore-end -->

Rules:
- No space *before* punctuation, one space *after*: «درست، مثل این.»
<!-- fa-lint-ignore-next-line -->
- ! stays ! — but one, never !!!
- Em/en dashes: not used in Persian prose. Use «،» «؛» ( ) or restructure.
- Latin fragments inside Persian (brand names, code) keep Latin punctuation
  *inside the fragment*: «افزونه WooCommerce، نسخه‌ی ۹».

## 5. Ezafe (کسره‌ی اضافه)

The unwritten -e linking noun+modifier is usually implicit (کتابِ خوب → کتاب خوب).
Write it explicitly only where the host word demands it:
- After silent ه: خانه‌ی من / خانهٔ من
- After ا and و: صدای بلند، عموی من (the ی is mandatory)
- Diacritic کسره (ِ) only for disambiguation in formal/educational text.

### 5.1 هکسره — the error Iranians mock most

Two different things sound identical at the end of a word, so writers swap them.
Getting this wrong in public copy is the single fastest way to look careless:
Iranians screenshot هکسره mistakes off billboards and brand accounts for sport.

| | What it is | Written | Example |
|---|---|---|---|
| **کسره‌ی اضافه** | links a noun to what follows (ezafe) | kasre — usually left unwritten, never «ه» | کتابِ من / کتاب من |
| **«ـه» clitic** | colloquial short form of «است» (predicate) | attached «ه» | این کتابه = این کتاب است |

**The test that always works:** replace the ending with «است» and read it aloud.
If the sentence still makes sense, the correct spelling is «ـه». If it turns to
nonsense, you need a kasre (and usually write nothing at all).

<!-- fa-lint-ignore-start -->

- «این کتابه» ← «این کتاب است» ✓ → «ـه» correct
- «کتابه من» ← «کتاب است من» ✗ → ezafe needed: **کتابِ من** (or plain «کتاب من»)

**Wrong → right:**

| ❌ | ✅ | Why |
|---|---|---|
| کتابه من رو ندیدی؟ | کتابِ من رو ندیدی؟ | ezafe, not «است» |
| کلاسه زبان می‌رم | کلاسِ زبان می‌رم | ezafe |
| قیمته این محصول چنده؟ | قیمتِ این محصول چنده؟ | first is ezafe, second («چنده») is «است» ✓ |
| سایته شرکت بالا نمیاد | سایتِ شرکت بالا نمیاد | ezafe |
| هوا خیلی خوبِ | هوا خیلی خوبه | predicate «است» — the reverse error |
| ماشینه من خرابه | ماشینِ من خرابه | ezafe first, «است» second ✓ |

<!-- fa-lint-ignore-end -->

**Careful — these are NOT errors.** Many nouns simply end in ه, and they take a
normal ezafe like any other word: خانه، نامه، برنامه، پروژه، مقاله، هفته، تجربه،
شماره، بچه. «نامه شما رسید» and «پروژه‌ی شما» are both fine; nothing was swapped.

**Register note:** the «ـه» clitic belongs to colloquial writing only. In formal
or academic text write «است» in full — «این کتاب است»، not «این کتابه». So a
formal document that contains «ـه» clitics has a register problem, not just an
orthography one (see writing-style.md).

the fa_lint script (full package; chat-only AIs apply the equivalent rules manually) --check` flags probable هکسره in both directions. It reports
rather than auto-fixes, because only context decides which of two identical
sounds the writer meant — and a wrong "fix" here changes the meaning.

## 6. Spacing hygiene

- Exactly one space between words; no double spaces (common AI artifact).
- No space inside «گیومه» : «درست»، نه « غلط ».
- Parentheses: بیرون فاصله، داخل نه (مثل این).
- Latin↔Persian boundary: one space — «پلتفرم WordPress برای...».

## 7. Numbers as words

Formal prose: one-word numbers under eleven often spelled out (سه پیشنهاد،
پنج مرحله). Tables, prices, stats: always digits. Don't mix styles in one list.

## 8. Common corrections table

<!-- fa-lint-ignore-start -->

| Wrong | Right | Why |
|---|---|---|
| میخواهم | می‌خواهم | ZWNJ after می |
| آنها را دیدم ولی کتابها نه | آن‌ها ... کتاب‌ها | ZWNJ before ها (if using آن‌ها style) |
| عليرضا | علیرضا | Arabic ي |
| لطفا | لطفاً | tanvin on Arabic loan |
| گاهاً | گاهی | tanvin on Persian word — always wrong |
| دوماً | دوم اینکه / ثانیاً | same |
| بсمت | به سمت / به‌سمت | mashed preposition |
| "نقل قول" | «نقل قول» | گیومه |
| 20 درصد | ۲۰ درصد | Persian digits |
| سال 2026 | سال ۲۰۲۶ | Persian digits |

<!-- fa-lint-ignore-end -->

## 9. Mixed Persian–English text: direction (bidi)

The most visible failure in mixed text is not a spelling error — it is a line
that renders backwards. Readers report it as «متن چپ‌چین شده و قابل خواندن
نیست», and they have to fix it by hand.

**Why it happens.** Most surfaces that show plain text or Markdown — chat apps,
GitHub, Telegram, note apps, Markdown previews, many editors — decide each
paragraph's direction from its **first strong letter** (the Unicode bidi
algorithm with `dir="auto"`). Persian letters are right-to-left, Latin letters
left-to-right, while digits, spaces and punctuation are neutral and take the
direction of what surrounds them. So:

<!-- fa-lint-ignore-start -->

| Line | First strong letter | Renders as |
|---|---|---|
| React یک کتابخانه است. | R of React → LTR | left-aligned, period jumps, words reorder |
| - Docker لازم است. | D → LTR | the bullet flips sides |
| ## API چیست؟ | A → LTR | the heading flips sides |
| ۲۰۲۶ سال خوبی بود. | digits are neutral → سال → RTL | correct |
| کتابخانه‌ی React را نصب کنید. | ک → RTL | correct |

<!-- fa-lint-ignore-end -->

**Rule 1: lead with a Persian word.** Every sentence, bullet, heading, table
cell, caption and message must start with a Persian word. The fix is almost
always natural Persian anyway, because Persian names a thing by its kind:

<!-- fa-lint-ignore-start -->

| ❌ Starts with Latin | ✅ Starts with Persian |
|---|---|
| React یک کتابخانه‌ی جاوااسکریپت است. | کتابخانه‌ی React برای ساخت رابط کاربری است. |
| Docker را نصب کنید. | ابتدا Docker را نصب کنید. |
| - API پاسخ را برمی‌گرداند. | - رابط API پاسخ را برمی‌گرداند. |
| ## SEO چیست؟ | ## سئو (SEO) چیست؟ |
| `npm install` را اجرا کنید. | دستور `npm install` را اجرا کنید. |
| Google Analytics داده‌ها را نشان می‌دهد. | ابزار Google Analytics داده‌ها را نشان می‌دهد. |

<!-- fa-lint-ignore-end -->

Useful leading words: ابزار، کتابخانه‌ی، فریم‌ورک، سرویس، دستور، فایل، نسخه‌ی،
شرکت، برند، زبان، افزونه‌ی، پلتفرم، سامانه‌ی، رابط. If the term has a common
Persian form, prefer it (سئو، ایمیل، اینستاگرام) and keep the Latin in
parentheses on first mention.

**Rule 2: keep each Latin run whole.** A Latin run stays left-to-right inside
the Persian line, so «نسخه‌ی Python 3.11» is fine. Problems come from splitting a
Latin phrase with Persian words or punctuation, or from a Persian word ending
in Latin punctuation. Write the run in one piece and use Persian punctuation
after it: «از React، Vue و Svelte» (Persian «،», not «,»).

**Rule 3: when a line must start with Latin** — a code identifier at the head
of a list, a product name in a table cell, a reply that quotes a command —
and the output is plain text or Markdown, run:

```bash
python3 the persian_cleanup script (full package; chat-only AIs apply the equivalent rules manually) --bidi --in text.md --out text.md
python3 the persian_cleanup script (full package; chat-only AIs apply the equivalent rules manually) --edit --bidi --in text.md --out text.md
```

`--bidi` puts an invisible RIGHT-TO-LEFT MARK (U+200F, RLM) at the start of only
those lines and table cells, after any Markdown marker (`- `, `## `, `> `,
`1. `). It skips code blocks and English lines, and running it twice changes
nothing. `fa_lint.py --check` reports the lines that need it as `bidi-start`.

It is opt-in, not part of `--edit`, because invisible characters have costs:
they break exact-match search, and pasted into code or a filename they cause
errors that cannot be seen. Use it for text meant to be **read**. Never use it
for code, data, filenames or URLs. It changes how a text displays, never what
it says, and has nothing to do with hiding authorship.

**Formats that carry direction in markup do not need marks.** Set the direction
there instead: HTML `dir="rtl"` plus `<bdi>` around Latin fragments
(html-css.md), DOCX `<w:bidi/>` and `<w:rtl/>` (docx-pdf.md), PowerPoint
`rtl="1"` (pptx.md), Excel `rightToLeft`. A correctly built document never
needs RLM.



---

# PART 9 — Content craft: POV, structure, honesty

# Persian content craft: point of view, structure, and honesty

Register (writing-style.md) decides *how formal* the text is. This file decides
*who is speaking*, *in what order the ideas arrive*, and *what you are allowed
to claim*. These are the disciplines that separate content a professional
editorial team would publish from content that merely reads smoothly.

Applies to educational articles, documentation, product and service pages,
internal reference docs, and the long-form half of social content — in any
field. The examples below use ordinary business situations on purpose: the
same rules govern a clinic's patient guide, a law firm's explainer, a
workshop's how-to, and a software company's release note.
Channel-specific mechanics live in social-channels.md.

## 1. Point of view — the most-broken rule in Persian content

Most Persian brand content slips between «ما»، «شما» and impersonal narration
inside a single paragraph. The result feels like a sales letter interrupting a
tutorial. One rule fixes it:

> **Explain the subject impersonally, teach the reader directly, and use "we"
> only for what the organization actually did or is responsible for.**

| Content type | Voice | Example |
|---|---|---|
| Fact, definition, cause, how a system behaves, advantage, limitation | Impersonal, subject-centred | «سفارش پس از تأیید پرداخت ثبت می‌شود.» |
| A step the reader performs | Second person; the verb alone carries it | «در صفحه‌ی سفارش‌ها، گزینه‌ی ویرایش را انتخاب کنید.» |
| The organization's own action, decision, policy, commitment, investigation | First person plural «ما» | «ما این محدودیت را در نسخه‌ی بعدی برطرف می‌کنیم.» |
| How people in general behave | «کاربر» / third person | «کاربر معمولاً پیش از خرید، نظرات را می‌خواند.» |

Supporting rules:

- **Don't repeat «شما».** Persian verb endings already encode the person.
  «شما می‌توانید فایل را حذف کنید» → «می‌توانید فایل را حذف کنید». Repetition
  reads as translated-from-English.
- **Don't switch POV inside a short section** without a reason. If a paragraph
  starts impersonal, finishing it with «ما» makes the reader re-parse it.
- **«شما باید» only for a real obligation with a real consequence.** Otherwise
  it sounds bossy for no reason. «باید» earns its place when skipping the step
  breaks something: «پیش از حذف، باید نسخه‌ی پشتیبان بگیرید؛ این عمل
  برگشت‌پذیر نیست.»
- A neutral explanation is not "cold". It is exactly what makes the reader
  trust the later paragraph where you do speak as the organization.

## 2. Education, product, and promotion

The fastest way to destroy the credibility of educational content is to bend it
toward a product halfway through. Keep the three separated:

- **The teaching must be worth reading even for someone who never buys.**
  If the article only works as a funnel, it is an ad wearing a tutorial's
  clothes, and readers notice.
- **Don't withhold the main answer.** Putting the actual answer behind a
  signup, or delaying it to the last paragraph, is the fastest way to lose both
  the reader and the ranking.
- **Present the problem before the solution**, and the solution before the
  product name.
- **Introduce a product only where it genuinely solves the problem** being
  discussed. Otherwise the mention is noise.
- **Tie every feature to a use case and a checkable result.** «امکان ثبت
  خودکار دارد» says nothing; «سفارش‌ها هر شب یک‌بار ثبت می‌شوند، پس در بدترین
  حالت یک روز تأخیر دارید» says something the reader can act on.
- **Never delete limitations, prerequisites, or conditions of use.** They are
  the part of the text that proves the rest is honest.
- **Don't present general industry knowledge as a proprietary advantage**, and
  don't attack competitors — describe your own trade-offs instead.
- **Don't repeat the brand or product name without reason.** Once the reader
  knows whose text this is, repetition only reads as insecurity.

## 3. Source fidelity and the four kinds of statement

Content built on sources (documentation, reports, a client brief, research)
must keep the distinction between what is known and what is guessed:

| | Definition | How to write it |
|---|---|---|
| **واقعیت** | verifiable, in the source | state plainly |
| **نظر** | someone's judgement | attribute it: «به گفته‌ی [نام یا نقش]...» |
| **پیش‌بینی** | about the future | mark it: «انتظار می‌رود»، «احتمالاً» — never as settled fact |
| **ادعا** | asserted, unverified | attribute and, where it matters, note it is unverified |

Working rules:

- **Never invent** a statistic, date, version number, price, company name,
  quote, command, output, or comparison to fill a structural slot. An empty
  section is honest; a fabricated one is a liability.
- **If data is incomplete**, either write the sentence cautiously or drop it.
- **If missing information blocks a correct answer**, ask one specific question
  before writing rather than guessing.
- **Don't hide contradictions between sources.** Either present the
  contradiction explicitly, or leave the disputed point out entirely — but
  never resolve it silently by picking the more convenient version.
- **Volatile facts** (versions, prices, compatibility, limits, commands) should
  not be stated as permanent without verification. Date them or hedge them.
- **Preserve names, numbers, dates and amounts exactly** as the source has
  them. Precision here is what earns the reader's trust everywhere else.

## 4. General structure for educational content

Use this order and delete any section that has nothing real to say:

1. **عنوان** — names the subject, problem, or result. No clickbait, no
   curiosity gaps.
2. **طرح مسئله** — one or two sentences: what this is about and why it matters.
   Cut the historical preamble and the «در دنیای امروز» opener entirely.
3. **زمینه لازم** — only the concept or prerequisite the reader needs in order
   to follow the solution. Not everything you know about the topic.
4. **بدنه** — the substance, in whichever pattern fits (§5).
5. **نتیجه‌ی مورد انتظار** — what changes if the reader does this, or what
   decision they can now make.
6. **محدودیت، استثنا، هشدار** — version, platform, condition, risk,
   irreversible effect. Placed *next to the relevant step*, not collected in a
   graveyard at the end.
7. **جمع‌بندی** — compresses the answer or the decision criterion. Introduces
   nothing new and does not restate the article.

For a comprehensive article, the internal progression that works is:
**تعریف → نحوه‌ی کار → کاربردها → اجزا یا ویژگی‌ها → مزایا و محدودیت‌ها →
مقایسه → مخاطب مناسب → آموزش عملی → جمع‌بندی → پرسش‌های متداول.**
General before specific; understanding before action.

Three questions carry almost any explanatory piece: **«چیست؟»،
«چگونه کار می‌کند؟»، «چه زمانی به کار می‌آید؟»** Answer a complex idea in one
plain sentence first, then add the technical detail.

## 5. Six body patterns

Pick the one that matches the content; don't force everything into steps.

**مرحله‌ای (procedure).** Prerequisites stated first. Steps numbered. One
action per step. Exact path and option names. The expected result of each step.
Warnings sit beside the step they concern, never at the end.

**نکته‌ای (tips).** Each tip gets a short heading and its own paragraph. Order
by importance, execution order, or logic — not randomly. Keep recommendations
visibly separate from requirements.

**مقایسه‌ای (comparison).** Define the options and the criteria first. Apply
*the same* criteria to every option — usually some of: use case, resources,
scalability, management effort, cost, stability, security, required expertise.
**Conclude conditionally**: which option suits which situation. Declaring an
absolute winner is almost always a sign the comparison was rigged. If two
options are complementary rather than rival, say so and explain when to use
both.

**تعریف مفهوم (concept).** تعریف ساده → نحوه‌ی کار → کاربرد → مزیت و محدودیت
→ مثال → زمان مناسب استفاده.

**مسئله و راه‌حل (troubleshooting).** نشانه → علت‌های محتمل → بررسی از
ساده‌ترین و کم‌ریسک‌ترین اقدام → راهکار → نتیجه‌ی مورد انتظار → نقطه‌ای که
باید سراغ پشتیبانی یا متخصص رفت. Ordering diagnostics from cheapest and safest
outward is what makes troubleshooting content actually usable.

**معرفی محصول یا قابلیت.** نیاز → راهکار → کاربرد → مخاطب مناسب → قابلیت
مرتبط → محدودیت و پیش‌نیاز → تفاوت با نزدیک‌ترین گزینه → مسیر بررسی بیشتر.
Never open with adjectives; open with the need.

## 6. Specialist terminology and proper names

Applies to any field with its own vocabulary — medicine, law, finance,
engineering, design, cooking — not just technology.

- **Keep the term the field actually uses.** If practitioners and readers say
  it in English (or in an established loanword), keep that form. Inventing an
  unfamiliar Persian equivalent hurts comprehension more than the loanword
  does; forcing a purist coinage nobody uses is a translation error, not
  linguistic care.
- **Explain on first use only**, with a plain Persian explanation in
  parentheses, then use one fixed form for the rest of the text. Consistency
  beats variety here — synonym-cycling a specialist term confuses readers and
  is an AI tell (writing-style.md T18).
- **Never translate official names**: product names, menu items, buttons,
  options, form fields, legal titles, drug names, standards. Whatever the
  reader will see in front of them is what the text must say, unchanged.
- Keep the boundary between the official name and your Persian explanation
  visible, so the reader knows which words to look for.
- Write names, figures, units, dates and any codes consistently throughout —
  mixed conventions make one text look like it had several authors.
- Where a field uses commands, formulas, references or identifiers, present
  them in a fixed format and keep them LTR when they're in Latin script
  (html-css.md, docx-pdf.md).

## 7. Clarity mechanics

- Short-to-medium sentences, active verbs. Avoid stacking several independent
  claims into one sentence.
- One idea per paragraph; typically 2–5 sentences.
- Keep chronological and logical order intact.
- Cut redundant phrases, heavy nominalisation (اسم‌سازی: «انجام بررسی را به عمل
  آورد» → «بررسی کرد»), ambiguous pronouns, and translationese.
- Replace a vague phrase with the precise word.
- Keep the text scannable on a phone — but scannable is not the same as
  fragmented; don't chop prose into disconnected lines.

## 8. Formatting discipline

- **Bold** is for a heading, a key concept, a warning, or a critical result.
  Bold as decoration destroys its own signal.
- **Numbered lists = sequence. Bulleted lists = independent items.** Using a
  numbered list for unordered things implies an order that doesn't exist.
- Keep list items grammatically parallel, and merge lists that overlap.
- Start each bullet with the concept name, then a colon and a short practical
  explanation — but avoid turning an entire article into bold-header bullets
  (writing-style.md T16). Prose carries argument; lists carry inventories.
- Avoid long, nested, or repetitive bullets.
- **Tables** for three or more options across fixed criteria. For two options,
  a paragraph or short list is usually clearer.
- Present advantages and limitations under separate, explicit labels.
- Anything meant to be copied or typed exactly — a code snippet, a reference
  number, a formula, an address — goes in code formatting and stays LTR when
  it's Latin script (html-css.md, docx-pdf.md).
- Keep heading hierarchy regular and headings self-explanatory: a reader
  skimming only the headings should still learn the outline of the argument.

## 9. Notes, warnings, and limits

- **نکته** = supplementary information. **هشدار** = risk. **محدودیت** =
  a condition or boundary on the result. Don't blur them.
- State the consequence precisely: not «مراقب باشید» but «اگر این گزینه را
  فعال کنید، آدرس‌های قبلی از کار می‌افتند».
- Put the warning **next to the action it concerns**. A warning discovered
  after the damage is decoration.
- Examples earn their place only when they improve understanding or the
  reader's decision. Keep them short, realistic, and matched to the audience.

## 10. Conclusion and call to action

- The conclusion states the answer, the decision criterion, or the next step.
  It is not a summary of the text and not a brand slogan.
- **One primary call to action**, only where it is the logical continuation of
  the content. Name the destination and what happens there. No pressure, no
  manufactured urgency.
- Link to the most specific relevant page — the exact documentation page, not
  the homepage — and say what the reader will find there.
- For statistics, standards, security reports, and consequential claims, cite a
  credible, primary, current source, and state the date, period, unit, and
  context of the data.

## 11. Pre-delivery checklist

- Does every claim come from the source material or the brief?
- Is the core definition clear near the beginning?
- Does the text move from understanding → evaluation → action?
- Is each term explained on first use, then used consistently?
- Does every feature appear with its practical effect?
- Are comparisons criteria-based and conclusions conditional?
- Are steps, commands and prerequisites complete and mutually consistent?
- Are repetition, exaggeration, unintended promotion, and invented detail gone?
- Is the point of view consistent and correct per §1?
- Is the deliverable the finished text only, with no internal labels
  («مقدمه»، «بدنه»، «نسخه‌ی بازنویسی‌شده») left in the published output?



---

# PART 10 — Academic writing (نگارش علمی)

# Persian academic writing (نگارش علمی فارسی)

For theses (پایان‌نامه), journal papers (مقاله علمی-پژوهشی), student reports,
technical analyses, research reviews (مرور پژوهش), and case studies
(مطالعه موردی). Academic Persian is a *fourth register* — more formal than
business writing, but the same enemies apply: bureaucratic fossils and AI
patterns make a paper feel machine-written, and reviewers notice.

## 1. Two genre families — decide first

**Journal/thesis format (ساختارمند):** section names are conventional and
expected — چکیده، مقدمه، پیشینه پژوهش، روش، یافته‌ها، بحث و نتیجه‌گیری، منابع.
Do NOT invent creative headings here; the convention IS the genre.

**Essay/report format (تحلیل، گزارش، مطالعه موردی):** descriptive headings
that preview content beat generic labels:
- Instead of «مقدمه» → «داکر و تغییر معنای استقرار نرم‌افزار»
- Instead of «نتیجه‌گیری» → «آنچه از مهاجرت پایگاه‌داده بدون توقف آموختیم»

## 2. The academic register

What it IS:
- Precise, measured, impersonal-leaning. Third person or «نگارنده/پژوهشگر»؛
  first-person plural («بررسی کردیم») is accepted in modern Persian papers.
- **Passive is legitimate here** («داده‌ها گردآوری شد»، «نشان داده شد») —
  the one register where the passive-voice warning in writing-style.md relaxes.
  Still prefer active when the agent matters.
- Hedged claims: «به نظر می‌رسد»، «شواهد نشان می‌دهد»، «احتمالاً» — one hedge
  per claim, not three (شاید بتوان گفت که احتمالاً... is AI stacking).
- Standard scholarly formulas are FINE and expected: «هدف این پژوهش... است»،
  «در این بخش... بررسی می‌شود». Formulaic ≠ AI in this genre.

What it is NOT (these stay banned even in the most formal paper):
- می‌باشد، می‌گردد for است/می‌شود — the Academy's style guidance and every
  serious آیین نگارش condemn them. «این روش کارآمد می‌باشد» marks the text
  as bureaucratic, not scholarly.
- لازم به ذکر است، شایان ذکر است — say the thing.
- Significance inflation: «نقش بسزایی»، «از اهمیت ویژه‌ای برخوردار» — state
  the finding and its measured effect instead.
- تعارف and reader-flattery. Academic Persian has zero تعارف.

## 3. AI tells specific to academic text

**A1. Mechanical enumeration.** اولاً... ثانیاً... در نهایت / نخست... دوم...
سرانجام as paragraph skeletons. Real papers connect by content: the result of
one paragraph raises the question the next answers.

**A2. Bullet-point substitution for prose.** Academic argument lives in
paragraphs. When information is genuinely a list, embed it:

> ❌ مزایای این روش عبارتند از:
> • کاهش زمان اجرا
> • کاهش هزینه
> • دقت بیشتر
>
> ✅ این روش سه مزیت عملی داشت: زمان اجرای هر آزمون از ۸ دقیقه به ۲ دقیقه
> رسید، هزینه‌ی هر نمونه حدود ۳۰٪ کاهش یافت و خطای اندازه‌گیری از ۵٪ به ۲٪
> رسید.

**A3. Source-listing instead of synthesis.** «اسمیت (۲۰۱۸) روشی ارائه کرد...
جانسون (۲۰۱۹) مدلی توسعه داد... براون (۲۰۲۰) بررسی کرد...» is an annotated
bibliography, not a پیشینه. Synthesize: group by idea, show the line of
development, name the disagreement, end at the gap your work fills.

**A4. Generic claims where numbers belong.** «دقت قابل توجهی حاصل شد» → «دقت
از ۸۴٪ به ۹۱٪ رسید (جدول ۲)». If you don't have the number, don't imply it.

**A5. The empty «چالش‌ها و چشم‌انداز آینده» section.** Limitations must be
specific to THIS study (sample size, single-domain data, unmeasured variables),
not boilerplate about «چالش‌های پیش رو».

**A6. Elegant variation on terminology.** In academic prose, terminology
consistency is a virtue: pick ONE term per concept (یادگیری ماشین, not
alternating with فراگیری ماشینی and ماشین لرنینگ) and repeat it. Synonym
cycling reads as AI *and* confuses reviewers.

**A7. Instruction residue.** Phrases that show the text was produced in answer
to a request: «طبق درخواست»، «بر اساس توضیحات شما»، «در ادامه‌ی خواسته‌ی
شما»، «مطابق دستور ارائه‌شده». They are leftovers of a conversation, not part
of a thesis, and they go. «همان‌طور که گفته شد» is fine only when it points to
an earlier section of the same text. Whether AI assistance must be declared is
a separate matter, handled through the institution's disclosure route (§9.5),
not by stray phrases.

**A8. Decorative academic vocabulary.** Words that machine-written Persian
papers lean on until they mean nothing: جامع، کلیدی، نظام‌مند (as praise, not
as a method name), محور and حول محور، پیوند (for every relation),
«تصویر روشنی از ... ترسیم می‌کند»، «از دل ... به دست می‌آید»، «گام‌به‌گام».
Replace each with the specific relation or result. Many advisors keep a banned
list of exactly these; see §7.5.

**A9. Slashes and hyphens between words.** «کیفی/کمی»، «معلم‌-دانش‌آموز» are
note-taking shorthand. Write the relation out: «کیفی و کمی»، «کیفی یا کمی»،
«رابطه‌ی معلم و دانش‌آموز». Hyphens stay in section numbering and fixed
compound labels.

## 4. Terminology and Latin material

- First use: Persian term + Latin in parentheses or footnote —
  «یادگیریِ انتقالی (Transfer Learning)». After that, Persian term alone.
- Use فرهنگستان equivalents where they're actually current (رایانه، داده،
  الگوریتم is fine as-is); don't force coinages nobody uses (تارنما) — the
  established loan is more scholarly than a strange purism.
- Latin abbreviations stay Latin and LTR: CNN، API، p-value. Wrap in LTR
  runs/`<bdi>` per the format references.
- Footnotes (پانویس) are the classic Persian-academic home for Latin
  equivalents and side notes. In docx they inherit RTL problems — each
  footnote paragraph needs the same bidi treatment (docx-pdf.md).

## 5. Citations and references

- In-text: (نویسنده، سال) for Persian sources — (کریمی، ۱۴۰۲)؛ Latin sources
  stay Latin — (Esteva et al., 2017). Page for direct quotes:
  (کریمی، ۱۴۰۲، ص. ۴۵). Direct quotes in «گیومه».
- Reference list (منابع): Persian sources first (alphabetical by surname),
  then Latin sources. Persian dates in هجری شمسی as published; don't convert.
- Never fabricate sources. If the user hasn't supplied references, write
  the citation slots as placeholders — «(منبع؟)» — and tell them; an invented
  DOI is fatal in this genre. Vague authority («کارشناسان معتقدند») is
  doubly banned in academic text.

## 5.5 Rewriting from a source: fidelity and the strength of every claim

The commonest academic task given to an AI is paraphrasing a paper into a
thesis chapter. It is also where the quietest damage happens: the Persian
reads well, and the source no longer says what the chapter claims it says.

**The governing rule.** A paraphrase changes only the wording and the sentence
structure. Nothing is added, nothing is dropped, and the strength, scope and
certainty of every claim stay exactly as the source has them.

**1. Add nothing.** No inference, interpretation, conclusion, explanation or
new connection, neither the model's nor the researcher's, enters text that is
attributed to the source. This includes the "helpful" bridge sentence written
to make two paragraphs flow or to complete an argument: if the source does not
make that link, the paraphrase does not either. A paragraph that reads a little
less smoothly is the correct price.

**2. Separate the researcher's own reasoning.** When revising an existing
chapter against its source, sentences that are the researcher's inference or
analysis are not silently kept inside the source-based text:

1. separate them from the material attributed to the paper
2. mark them with «این بخش در مقاله وجود ندارد»
3. do not carry them automatically into the rewritten, source-based version
4. if the claim needs support, mark it «نیازمند منبع مستقل است» and leave it
   for the researcher to source.

The researcher's own interpretation is legitimate. It belongs in the بحث
chapter, in the researcher's voice, not presented as what the paper found.

**3. Preserve every qualifier.** Each hedge, quantity, frequency and degree in
the source keeps its meaning in Persian. Neither drop one nor add one:

<!-- fa-lint-ignore-start -->

| Source | Persian | Note |
|---|---|---|
| approximately, about | حدود، تقریباً | |
| nearly, almost | نزدیک به، تقریباً | |
| mainly, primarily, largely | عمدتاً، در درجه‌ی نخست | |
| partly, to some extent | تا حدی | |
| in most cases | در بیشتر موارد | |
| generally | به‌طور کلی | only if the source itself generalizes |
| may, might | ممکن است | |
| can, could | می‌تواند | capability, not likelihood |
| likely, probably | احتمالاً، به احتمال زیاد | |
| suggest, indicate | حاکی از آن است، نشان می‌دهد که احتمالاً | weaker than show; never «ثابت می‌کند» |
| show, demonstrate | نشان می‌دهد | |
| up to | تا | a ceiling, not a typical value |
| at least / at most | حداقل / حداکثر | |
| on average | به‌طور متوسط | |
| significantly | به‌طور معنادار | only for statistical significance |
| no significant difference | تفاوت معناداری مشاهده نشد | NOT «یکسان بودند» |
| associated with, correlated with | با ... ارتباط داشت | NOT «باعث ... شد» |
| in this sample, among participants | در این نمونه، در میان شرکت‌کنندگان | keep the scope |

<!-- fa-lint-ignore-end -->

The four drifts to watch for, each of which changes a finding:

<!-- fa-lint-ignore-start -->

- **Rounding.** 58.8% stays ۵۸٫۸ درصد. Do not turn it into «حدود ۵۹ درصد».
- **Hardening.** «approximately 59%» stays «حدود ۵۹ درصد», not «۵۹ درصد».
  «suggests» does not become «نشان می‌دهد» or «ثابت می‌کند».

<!-- fa-lint-ignore-end -->

- **Softening.** A claim the source states firmly is not weakened with
  «احتمالاً» or «ممکن است» to sound cautious.
- **Scope creep.** A result in one sample, region or period does not become
  «در ایران» or «به‌طور کلی». Correlation does not become causation, and
  «تفاوت معناداری مشاهده نشد» does not become «تفاوتی وجود ندارد».

This is where §2's "one hedge per claim" yields. That rule is about stacking
hedges in your own prose. In a paraphrase, the hedges mirror the source,
including a double hedge if the source has one.

**Fidelity check.** Before handing over a source-based paraphrase, answer
these. Every answer must be «خیر»:

- آیا چیزی خارج از منبع وارد متن شده است؟
- آیا استنباط پژوهشگر یا مدل وارد متنِ منبع‌محور شده است؟
- آیا قیدی از قیدهای شدت، مقدار، دامنه یا عدم قطعیت منبع حذف یا تضعیف شده است؟
- آیا قیدی بدون معادل در منبع اضافه شده است؟

When the user asks for an audit, show it as a table: source sentence, Persian
paraphrase, qualifiers kept, and a flag column.

## 6. Numbers, statistics, formulas

- Persian digits in prose: «۱۲۸ شرکت‌کننده»، «۹۱٪». Spell out small counts
  at sentence start.
- Statistical notation stays Latin and LTR: p < 0.05, F(2,45) = 3.71, R².
  Keep the whole expression in one LTR run so bidi doesn't scramble it.
- Formulas: LTR blocks (dir="ltr" / LTR paragraph), numbered «رابطه‌ی ۱».
- Tables: «جدول ۱: عنوان» ABOVE the table, «شکل ۱: عنوان» BELOW the figure.
  Caption paragraphs get keepNext (caption never strands on the wrong page) —
  see docx-pdf.md.

## 7. Structure conventions (journal/thesis format)

- **چکیده:** ۱۵۰–۳۰۰ words, one paragraph: مسئله ← روش ← یافته‌ی اصلی ←
  نتیجه. No citations, no abbreviations, findings in past tense.
- **واژگان کلیدی:** ۳–۶ terms, separated by «؛».
- **مقدمه:** funnel — the problem, what's known, the gap, «هدف این پژوهش».
- **روش:** replicable detail; passive natural here.
- **یافته‌ها:** report, don't interpret; every claim tied to a table/figure/test.
- **بحث:** interpret against the literature; limitations (specific);
  one-paragraph practical implication beats a «چشم‌انداز روشن» closer.

**List or prose, in a thesis.** Argument lives in paragraphs (A2), but some
thesis parts are conventionally lists, one item per line:

- فرضیه‌ها، پرسش‌ها و اهداف پژوهش: numbered, one sentence each;
- پیشنهادها برای پژوهش‌های آتی: numbered;
- تعاریف نظری و عملیاتی in chapter one: the term, then one or two lines of
  definition, each term on its own.

Everything else is prose. Each paragraph carries one idea, and its length
follows the idea. Paragraphs of identical length are a sign of templated
writing; vary them because the content varies, not by a word-count formula.

**Diacritics.** No اعراب in running text. Add a vowel mark only where a word
is genuinely ambiguous without it (کُرد / کَرد) or in a direct quotation that
has one. ZWNJ is not optional: می‌شود، پژوهش‌ها.

## 7.5 House style (شیوه‌نامه) and advisor preferences

Departments and advisors often add their own rules: banned word lists, no
Latin in the body, preferred synonyms (ارتباط for پیوند، بخش for محور),
paragraph length targets. Follow them; the شیوه‌نامه outranks this file on
matters of taste. Three cases need care, because a house rule applied blindly
would change what the text says:

- **A banned hedge.** If «احتمالاً» or «ممکن است» is on the banned list but the
  source hedges, keep the hedge with a permitted word of the same strength:
  «به احتمال زیاد»، «امکان دارد»، «به نظر می‌رسد». A ban on a word never
  overrides §5.5.
- **"No negative sentences."** Avoid needless negation (double negatives,
  «نه‌تنها ... بلکه ...»), but a negative finding stays negative.
  «تفاوت معناداری مشاهده نشد» rewritten as «دو گروه مشابه بودند» claims an
  equivalence the test never established.
- **No Latin in the body.** Move the English equivalents to پانویس or a
  واژه‌نامه at the end of the thesis rather than dropping them. Statistical
  notation (p، F، R²) stays as it is.

Guillemets «» are the standard Persian quotation mark. Replace them only if the
شیوه‌نامه explicitly requires another mark.

## 8. First-person calibration (by document type)

| Type | Voice |
|---|---|
| تحلیل فنی / گزارش آزمایش | Objective; «ما» sparingly for design decisions |
| مرور پژوهش | Moderate; evaluative stances hedged («به نظر می‌رسد شواهد...») |
| مطالعه موردی / گزارش تجربه | First person welcome for decisions and lessons: «اگر دوباره طراحی می‌کردیم...» |
| پایان‌نامه | Follow the university's شیوه‌نامه; default «نگارنده» or «ما» |

## 9. Worked example

**❌ AI-style:**
> در دنیای امروز، یادگیری ماشین نقش بسزایی در تشخیص پزشکی ایفا می‌نماید.
> مطالعات متعددی در این زمینه انجام شده است. اولاً، اسمیت و همکاران (۲۰۱۸)
> روشی مبتنی بر CNN ارائه کردند. ثانیاً، جانسون (۲۰۱۹) مدلی عمیق توسعه داد.
> نتایج این مطالعات نشان‌دهنده‌ی دقت بالا، سرعت مناسب و پتانسیل قابل توجه
> می‌باشد.

**✅ Scholarly Persian:**
> کاربرد یادگیری ماشین در تشخیص پزشکی از سامانه‌های قاعده‌محور آغاز شد و با
> ظهور شبکه‌های عمیق پس از ۲۰۱۲ مسیر تازه‌ای یافت. نقطه‌ی عطف، کار Esteva و
> همکاران (2017) بود که با آموزش شبکه‌ای پیچشی بر ۱۲۹٬۴۵۰ تصویر بالینی، به
> دقتی هم‌سنگ ۲۱ متخصص پوست رسید. پژوهش‌های بعدی همین الگو را به حوزه‌های
> دیگر بردند؛ اما هرچه دامنه گسترده‌تر شد، مسئله‌ی تعمیم‌پذیری پررنگ‌تر شد:
> Liu و همکاران (2020) نشان دادند عملکرد مدل روی داده‌ی بیمارستان‌هایی جز
> منبعِ آموزش، ۱۵ تا ۲۰ درصد افت می‌کند. همین شکاف، انگیزه‌ی اصلی پژوهش
> حاضر است.

Note what changed: synthesis with a through-line, real numbers, Latin names
left Latin, one hedge, no اولاً/ثانیاً, no می‌باشد, ends at the gap.

## 9.5 AI assistance, disclosure, and detector accusations

Academic work is where authorship claims carry the most weight, so two things
need saying plainly.

**Disclosure follows the institution's rule, not convenience.** Universities and
journals differ: some permit AI assistance for language editing, some require a
declaration, some prohibit it for substantive drafting. Find the actual policy
(شیوه‌نامه‌ی دانشگاه، راهنمای نویسندگان مجله) and follow it. Writing help that
is disclosed where disclosure is required stays honest; the same help concealed
does not. This skill improves the writing — it does not launder authorship, and
the techniques for disguising it (invisible characters, homoglyphs, injected
errors) are not here and should not be sought elsewhere.

**If a detector falsely flags a student's or researcher's work**, that is a
documented and common failure, not proof of anything. Persian-speaking authors
writing in English are hit hardest: one study of seven detectors measured a
**61.3% average false-positive rate for non-native English writers**, a 2023
evaluation of 14 tools found none reached 80% accuracy, and several major
universities withdrew from these tools over reliability concerns. A score is a
style guess, never evidence of authorship. Anyone facing such an accusation
should present drafts, notes, version history and sources — the ordinary
evidence of having done the work — rather than trying to satisfy the tool.

## 10. Checklist before delivering academic text

1. Register: no می‌باشد/لازم به ذکر است; hedges single; تعارف zero.
2. No اولاً/ثانیاً skeletons; no bullet lists where prose belongs.
3. پیشینه synthesizes; every number claim has a number; no invented sources.
3b. Source-based text: nothing added, nothing dropped, every qualifier and
   number exactly as in the source; the researcher's own inferences marked
   and kept out (§5.5). No instruction residue (A7).
4. Terminology: one Persian term per concept + Latin on first use.
5. Statistics/formulas in LTR runs; Persian digits in prose.
6. Structure matches genre (conventional sections for papers/theses).
7. Run the persian_cleanup script (full package; chat-only AIs apply the equivalent rules manually) --edit` then the fa_lint script (full package; chat-only AIs apply the equivalent rules manually) --check`
   on the text; fix everything contextual (dashes, میشود forms).
8. If producing docx/PDF: all rules in docx-pdf.md apply (RTL, keepNext
   captions, footnote bidi, fonts installed before conversion).



---

# PART 11 — Social channels: Telegram & Instagram

# Persian social channels: Telegram, Instagram, and repurposing

> A post that is prose (an argument, analysis or story rather than a caption)
> also follows writing-workflow.md, starting with its checkpoint.

Channel craft, not channel decoration. Register comes from writing-style.md,
structure and honesty from content-structures.md; this file adds what changes
when the text is consumed on a phone, in a feed, in seconds.

The formats and signatures here are patterns, not house style. Length caps,
emoji conventions, and closing lines belong to whoever owns the channel — ask
for theirs, and if none exists, the defaults below are safe.

## 1. Rules shared by every channel

- **One central topic per piece.** A post that covers two subjects gets read as
  neither.
- **The opening states the subject.** No greeting, no «در این پست می‌خواهیم...»,
  no restating the title, no rhetorical question standing in for content.
- **Never hide the answer to create suspense.** «تا آخر بخونید» is a tax on the
  reader that costs more attention than it buys.
- **Every paragraph carries one idea** and stays short enough to scan on a
  phone — without becoming a stack of disconnected fragments.
- **Critical information is never only in the image, only in the audio, or only
  behind a link.** Each surface should stand on its own to the extent it can.
- **Warnings go beside the relevant step**, not collected at the end or buried
  in a caption.
- **The closing gives the answer, the decision criterion, or the next step** —
  not a slogan and not a summary of what was just said.
- **One call to action**, with its destination and outcome named.
- **Publish-ready output only.** Internal labels like «مقدمه»، «بدنه»،
  «جمع‌بندی» are scaffolding for the writer, and must not survive into the
  posted text.

### Emoji — and why the first word after one matters in Persian

Default to no emoji. Where a channel's style uses them, they are for **semantic
separation**, not decoration: at most one (or one fixed combination) at the
start of a block, used consistently for the same meaning throughout.

There is also a genuinely technical reason to be careful. In an RTL paragraph,
an emoji is direction-neutral, so the first *strong* character after it decides
how the line is laid out. If a Latin word follows the emoji, the line can flip
to LTR and the punctuation jumps to the wrong side. **Keep the first word after
an emoji (and the first word of every paragraph) Persian**, or wrap the Latin
fragment as described in html-css.md. This is the same bidi rule that governs
Persian digits — orthography.md §3.

A workable emoji scheme, if one is wanted: numbered markers for sequence
(1️⃣ 2️⃣ 3️⃣), one consistent symbol family for risks and limits (🛑 ⚠️), another
for benefits, results and conclusions (✅ 🟢). What matters is that a symbol
means the same thing every time it appears.

## 2. Telegram

### Structure

عنوان → شروع مستقیم → زمینه‌ی لازم → بدنه → نکته/محدودیت/هشدار → جمع‌بندی →
اقدام یا لینک در صورت نیاز.

Don't let a post become a truncated article, a compressed ad, or a loose pile
of bullet points.

**Title:** short, direct, matching the content. A question, a problem, a
comparison, a guide, or an exact count of points («۴ نکته...»). Name the brand
only when the brand or its product *is* the subject.

**Opening:** one or two paragraphs establishing the problem, why it matters,
where it applies, the misconception being corrected, or the outcome of reading.

**Body:** use whichever pattern from content-structures.md §5 fits —
step-by-step, tips, comparison, concept, troubleshooting, or product
introduction. Each carries its own internal order.

**Headings and lists:** in medium or long posts, use real subheadings.
Numbered lists for sequence, bulleted for independent items. Bold only for
headings, key concepts, warnings and results.

### Length

- **Short:** one definition, tip, warning, change, or answer.
- **Medium:** a concept, a few criteria, a short comparison, a multi-step
  procedure, or one capability.
- **Long:** a full guide, troubleshooting, or multi-criteria comparison. If it
  outgrows the format, split it into a series rather than compressing it.

A practical ceiling many Persian tech channels use is roughly **۱۷۰۰ characters
including spaces، ~۴۰۰ کلمه، ~۱۶ پاراگراف** — sized so the post is consumable on
a single phone screen without endless scrolling. Treat it as a default, not a
law; the channel owner's spec wins.

### Common Telegram post types

**آموزشی پرسش‌محور** — title as a question, numbered points, risks marked,
benefits marked, a highlighted final result. A closing «تذکر مهم» block that
names the *plausible but wrong* conclusions a reader might draw and corrects
them is unusually valuable: it is where content earns trust rather than clicks.

**اطلاعیه‌ی قابلیت جدید** — greeting (if the channel uses one) → clear headline
→ short explanation of what it does → benefits or use cases as separate items →
how to use it, in steps → link to official documentation.

**خبر** — headline carrying the actual event → the news and its source, briefly
→ details as separate items → practical implications or steps if any → source
link → the misreading-correction block.

**هشدار** — an imperative headline naming the required action → what happened,
why it matters, and the source → the conditions that make a reader affected →
required actions as ordered steps → source → misreading correction.

For news and warnings especially: keep every fact traceable to the input
sources, and never invent an ID, form, URL, or contact that wasn't given.

### Links

Keep every link from the source; create none. Give each link a clear title and
attach the URL to that title as anchor text rather than pasting a long raw URL
mid-sentence.

## 3. Instagram

Instagram content is not a shortened article. It is built for visual
consumption, and the format is chosen from the content's shape:

| Format | Use it for |
|---|---|
| **کاروسل** | several steps, tips, criteria, a comparison, or a gradual explanation |
| **تک‌تصویر** | one definition, tip, warning, data point, or standalone message |
| **اینفوگرافیک** | a set of data or components and the relationships between them |
| **ریلز** | showing a process, an interface, movement, an example, before/after |
| **استوری** | short, time-bound messages, reminders, links, feedback, quick sequences |

One central topic per piece, one message per slide or frame, one clear
takeaway per reel.

**Hook:** the first slide, frame, or second must state the question, problem,
difference, result, warning, or exact number of points. No vagueness, no fear
bait, no exaggeration, no withheld answer.

**General path:** هوک → زمینه‌ی ضروری → آموزش یا پاسخ → محدودیت یا هشدار →
نتیجه → اقدام مرتبط در صورت نیاز.

### Carousel

کاور → اسلاید زمینه → اسلایدهای میانی → هشدار یا مثال → جمع‌بندی → CTA.

- **Cover:** short direct title, one subject, visible value, understandable
  *without* the caption. No paragraph, no extra promise.
- **Context slide:** the problem, its importance, the misconception, the
  audience, or the prerequisite — in the least space that works. Never a
  restatement of the cover.
- **Middle slides:** one definition, step, tip, criterion, cause, benefit,
  limitation, comparison, example, or warning each. Title states the message;
  body explains it.
- **Never split a sentence across two slides.** Move secondary detail to the
  caption instead.
- Put an important warning on its own slide or next to the action it concerns —
  not hidden in the caption.
- Slide count follows complexity. If the content gets dense or very long, split
  it into more than one post.

### Reels

هوک → مسئله → توضیح یا نمایش → مثال یا راهکار → محدودیت → جمع‌بندی → CTA.

- Open directly with the subject; no greeting or long introduction.
- One idea per sentence, one function per scene.
- On-screen text and narration should complement each other, not duplicate.
- Numbers, commands, option names, paths, warnings and the key result should
  appear **on screen**, not only in audio.
- Show interface steps slowly enough to follow, with the click target visible.
- Assume the sound is off: subtitles matter, and the essential information must
  survive muting.
- End on the result, the decision criterion, or the next action.

### Stories

- **Single frame:** one message — عنوان/پیام → توضیح کوتاه → اقدام یا لینک.
  Understandable at a glance; not several paragraphs.
- **Sequence:** frame 1 the subject or question, frame 2 the context, middle
  frames one point each, a limitation frame if needed, a final frame with the
  result or action. Don't split sentences across frames or pad the count.
- **Interactive stickers** are for gauging knowledge, identifying needs,
  quizzes, collecting questions, or choosing a topic — single-subject question,
  real options, and explain the correct answer afterwards. Never request
  sensitive data.
- **Before a link**, say where it goes and why it is relevant; send people to
  the most specific page.

### Captions and hashtags

The caption complements the visual, it doesn't repeat it:
جمله‌ی آغازین مشخص → زمینه → توضیح تکمیلی یا مراحل یا مثال → محدودیت →
جمع‌بندی → CTA و منبع در صورت نیاز.

Short paragraphs, one idea each. Don't put essential information only in the
caption. Avoid generic openings and endings that carry no information.
Hashtags: few, relevant, used for categorisation — not generic, repetitive, or
promotional. Brand hashtags follow the brand's own fixed policy, if it has one.

### Text on images and accessibility

- Images, charts and screenshots must aid understanding, not decorate.
- Text inside an image: short, hierarchical, large enough, high contrast, away
  from the edges. Break lines by meaning, not to fill space.
- Few fonts, few emphasis styles (fonts.md; and never letter-space Persian).
- Provide subtitles for speech, alt text for images where the platform allows,
  and explain charts in the caption.
- Don't encode meaning in colour alone; avoid fast or flashing motion.

## 4. Announcements and product introductions

**Announcement (change, incident, event):** موضوع → زمان → دامنه‌ی اثر →
وضعیت فعلی → اقدام انجام‌شده → اقدام لازم مخاطب → مسیر به‌روزرسانی.
State incomplete information as incomplete, and announce a definite resolution
time only when it is actually confirmed. Under-promising here is credibility;
over-promising is a support ticket.

**Product or capability introduction:** نیاز → راهکار → کاربرد → مخاطب مناسب →
قابلیت مرتبط → محدودیت و پیش‌نیاز → تفاوت با نزدیک‌ترین گزینه → مسیر جزئیات.
Verify price, capacity and any changeable condition before publishing, and
don't let a purchase invitation replace the explanation of *who this is
actually for*.

## 5. Repurposing between formats

Rewriting for the destination format, not copying into it:

- **Telegram → carousel:** extract the core message, move secondary detail to
  the caption, turn each section into an independent slide.
- **Article → reel:** keep one sub-topic, one definition, one example, one
  result — and rewrite the text for speech, which is a different rhythm than
  prose.
- **Carousel → story:** reduce the text and the number of messages. Never post
  screenshots of the slides as stories.
- **Article → Telegram:** keep the answer and the decision criteria; drop the
  background the format has no room for, rather than compressing everything
  uniformly into an unreadable block.

In a series, keep the overall topic, the part number, and each part's own
title — and make every part understandable without having seen the previous
ones.

## 6. Pre-publish checks

**Telegram:** one central topic; accurate title; opening free of filler;
logical structure; short paragraphs; clear steps; complete but not padded;
claims current; limitations and sources present; problem-centred tone;
result-oriented conclusion; no internal labels left in the text.

**Instagram:** format matches the content and audience; subject clear
immediately; hook precise and not misleading; one message per slide or frame in
a logical order; on-image text short, legible, phone-appropriate; caption,
narration and visual complementary with nothing essential dropped; claims,
volatile facts, sources, limitations and warnings correct; content
problem-centred rather than promotional; subtitles, contrast, element placement
and chart explanations handled; the deliverable separated from internal notes.

**Both:** run the text through the persian_cleanup script (full package; chat-only AIs apply the equivalent rules manually) --edit` and
the fa_lint script (full package; chat-only AIs apply the equivalent rules manually) --check` before delivery — هکسره errors and broken
نیم‌فاصله are the fastest way for a professional channel to look amateur
(orthography.md §5.1).



---

# PART 12 — SEO writing & copywriting

# Persian SEO writing & copywriting

Two crafts, one file, because in practice they overlap: SEO content that reads
like a robot doesn't rank long, and copy that ignores search never gets seen.
Everything in writing-style.md still applies — register detection first, AI
tells banned, brand-fact rule enforced. This file adds what's specific to
Persian search and Persian selling.

## Part A: SEO writing (سئو)

### A1. Search intent decides the content shape

| Intent | Persian query pattern | Content that wins |
|---|---|---|
| Informational (اطلاعاتی) | «چطور...»، «چیست»، «آموزش...» | Answer FIRST, then depth; step structure; FAQ block |
| Commercial (مقایسه‌ای) | «بهترین...»، «مقایسه...»، «کدام» | Honest comparison, criteria table, verdict |
| Transactional (تراکنشی) | «خرید...»، «قیمت...»، «سفارش» | Product/service page: price clarity, trust signals, CTA |
| Navigational | brand names, often misspelled | Correct brand spelling variants on-page |

Write for ONE intent per page. A «قیمت طراحی سایت» page that opens with the
history of the web serves no one — and Google measures that no one stayed.

### A2. Persian keyword variants — the part English SEO guides miss

Iranians type the same query many ways. The page should use the correct form
in prose but *acknowledge* variants (naturally, in different sentences or the
FAQ — never as a stuffed list):

- **ZWNJ variants:** وب‌سایت / وبسایت / وب سایت — searchers rarely type ZWNJ.
  Write the correct form; variants appear naturally in quotes/FAQ phrasing.
- **Loan vs Persian term:** سئو/SEO، دیجیتال مارکتینگ/بازاریابی دیجیتال —
  use the dominant form as primary, mention the other once early.
- **Digit scripts:** آیفون ۱۳ and آیفون 13 are different strings to a search
  engine; prices get searched with Latin digits. Keep prose digits Persian
  (orthography rule); let structured data / attributes carry Latin forms.
- **Spelling variants:** طهران/تهران era is gone, but ی/ي contamination from
  copy-paste still splits queries — publish only Persian ی/ک (the cleanup
  script guarantees this).
- Mine real variants from Search Console queries when the user has access;
  invented keyword lists are the SEO version of fabricated brand facts.

### A3. On-page checklist (writer's portion)

1. **Title (~60 chars):** keyword phrase at the START (rightmost, first-read
   position in RTL), brand at the end: «قیمت طراحی سایت فروشگاهی در ۱۴۰۴ | برند».
2. **Meta description (~150 chars):** the promise + one concrete detail + soft
   CTA. It's ad copy for the SERP, not a summary.
3. **H1:** one, contains the keyword naturally. H2s: the sub-questions people
   actually ask (they feed پرسش‌های مرتبط / PAA).
4. **First paragraph answers the query.** اول جواب، بعد توضیح — this wins
   featured snippets and respects the reader.
5. **FAQ section (سوالات متداول):** 3–6 real questions, one-paragraph answers.
   Mark up as FAQ schema when building the page (html-css.md).
6. **Internal links:** descriptive Persian anchors («راهنمای سئوی فروشگاهی»)،
   never «اینجا کلیک کنید».
7. **Alt text:** describe the image in Persian, keyword only when true.
8. **Slug:** short, hyphenated; Persian slugs are legitimate
   (`/قیمت-طراحی-سایت/`) — transliterated ones too; follow the site's
   existing convention.
9. **Length:** as long as the intent needs, not a word more. 300 thin words
   lose; 3000 padded words also lose.

### A4. What kills Persian SEO content

- Keyword-stuffed titles: «طراحی سایت | طراحی سایت ارزان | قیمت طراحی سایت» —
  a 2015 fossil that now marks spam.
- The «در دنیای امروز» intro (T4) — readers bounce, rankings follow.
- Generic listicles with no Iranian reality (prices in dollars, examples
  from Amazon when the reader uses دیجی‌کالا).
- AI-tell clusters (T1–T18) — helpful-content systems and human readers
  converge on the same judgment.
- Register mistakes: service pages are formal-but-human; blogs semi-formal.
  A خودمونی pricing page undermines purchase trust exactly at the decision
  moment.

## Part B: Copywriting (کپی‌رایتینگ)

### B1. The two questions before any copy

1. **Register** — from the detection procedure in writing-style.md. Casual
   copy in the wrong place is not "punchy", it's costly.
2. **The ONE promise.** Each page/post/ad makes one promise. If the draft
   makes three, it makes none.

### B2. Structures that work in Persian

**PAS (درد ← تشدید ← راه‌حل)** — the workhorse:
> مشتری اسمتان را گوگل می‌کند و چیزی پیدا نمی‌کند. (درد)
> رقیبتان را اما پیدا می‌کند — با سایتی که ساعت ۲ شب هم سفارش می‌گیرد. (تشدید)
> سایت فروشگاهی شما در ۴۵ روز آماده می‌شود؛ از طراحی تا اولین سفارش. (راه‌حل)

**AIDA** for longer landing pages: hook → مزیت‌های ملموس → اثبات → CTA.

**Headline patterns (تیتر):**
- عددی: «۷ اشتباهی که فروش سایتتان را می‌خورد»
- سوالی: «چرا سایتتان بازدید دارد ولی مشتری نه؟»
- منفعتی: «سایتی که خودش می‌فروشد»
- Avoid the manufactured-aphorism tell (T18): «سئو زبانِ اعتماد است» is
  perfume, not copy.

### B3. Feature → benefit, the Persian habit

State the feature, then translate it into the customer's life:

| ویژگی (feature) | مزیت (benefit) |
|---|---|
| درگاه پرداخت مستقیم | پول همان لحظه به حساب خودتان می‌نشیند |
| پنل مدیریت سفارش | آشپزخانه بدون تلفن‌بازی سفارش را می‌بیند |
| نسخه‌ی موبایل‌محور | مشتریِ توی تاکسی هم راحت سفارش می‌دهد |

(That last one is semi-formal register — fine for web copy, not for a
proposal. Benefits inherit the artifact's register.)

### B4. CTA by register

| Register | CTA examples |
|---|---|
| Formal (proposal, service page) | «درخواست مشاوره رایگان»، «دریافت پیش‌فاکتور»، «رزرو جلسه» |
| Semi-formal (blog, newsletter) | «راهنمای کامل را بخوانید»، «همین حالا شروع کنید» |
| Casual (Instagram, Telegram) | «دایرکت بده»، «کلمه‌ی X رو کامنت کن»، «لینک توی بایو» |

One primary CTA per artifact; repeat it, don't multiply it.

### B5. Money, honesty, and Persian-specific trust

- **Prices: always name the unit** — تومان vs ریال ambiguity has burned
  enough customers that unlabeled numbers read as a trick. Persian digits,
  thousands separator: «۸۵٬۰۰۰٬۰۰۰ تومان». Ranges honestly: «از ۳ میلیون
  تومان شروع می‌شود» only if something real costs ۳.
- **Brand-fact rule (writing-style.md) applies doubly:** no invented client
  counts, satisfaction percentages, awards, or «۱۰ سال تجربه». Ask the user
  for real numbers; real-but-small beats fake-but-big.
- **Urgency only when true:** «ظرفیت این ماه: ۴ پروژه» works if it's true and
  reads as spam if it repeats forever. Never !!!.
- **تعارف calibration:** warmth yes, ritual no. «قابل شما را ندارد» jokes
  belong in casual social copy at most; B2B copy earns trust with clarity.
- **Microcopy:** buttons = short verb phrases («افزودن به سبد خرید»،
  «ثبت سفارش»، «ادامه»). Error messages: polite, direct, actionable —
  «کد تخفیف معتبر نیست. دوباره بررسی کنید یا بدون کد ادامه دهید.»

### B6. Landing page skeleton (Persian)

1. هدلاین — the one promise, in the reader's words
2. زیرتیتر — how, in one sentence
3. ۳ مزیت — concrete, feature→benefit translated
4. اثبات — real نمونه‌کار / real numbers / real testimonial (with permission)
5. رفع اعتراض — سوالات متداول: قیمت، زمان، پشتیبانی، «اگر راضی نبودم؟»
6. CTA — repeated after each scroll-depth section, same verb each time

## Part C: Content quality standards (E-E-A-T for Persian sites)

Google evaluates experience/expertise/authoritativeness/trust on competitive
queries across the board — and its AI-content detection improves every update.
The writing-side signals, Persian-adapted:

- **Named authors with real bios** (نویسنده با نام، تخصص و عکس). Anonymous
  «تیم محتوا» posts rank worse and read worse. If the user has no author
  program, say so and suggest one.
- **First-hand evidence:** original screenshots, real numbers from real
  projects (with permission), process details only a practitioner would know
  («در پروژه‌های فروشگاهی معمولاً درگاه X این خطا را می‌دهد...»). This is the
  brand-fact rule's positive side: real specifics are the strongest SEO asset.
- **Trust furniture Iranian users actually check:** صفحه‌ی درباره‌ی ما with
  real people, تماس with address/phone, اینماد for e-commerce, شفافیت قیمت.
- **The AI-tell connection:** the T1–T18 patterns (writing-style.md) are
  exactly what quality systems flag as generic content. De-AI-ing IS an
  E-E-A-T intervention.

**Word-count floors by page type** (floors, not targets — depth follows intent):
homepage ~500، صفحه‌ی خدمات ~800، پست بلاگ ~1500، صفحه‌ی محصول ~400،
لندینگ ~600، سوالات متداول ~800. Below these, pages read thin to users and
crawlers alike; padding above them with fluff is equally fatal.

**The doorway-page trap — the classic Iranian agency mistake:** mass-produced
«طراحی سایت در تهران / کرج / شیراز / تبریز...» pages with only the city name
swapped. Google's doorway detection penalizes the whole site. A location page
is publishable only with genuinely local content: local projects/clients,
محله and landmark references, a local contact signal. Can't produce that for
30 cities? Then don't publish 30 pages — one strong «خدمات در سراسر ایران»
page outranks 30 thin clones after the penalty.

**بریف محتوا (content brief) template** — fill before writing any SEO piece:

```
کلیدواژه‌ی اصلی: ...        اینتنت: اطلاعاتی/مقایسه‌ای/تراکنشی
کلیدواژه‌های فرعی/واریانت‌ها: ...
مخاطب و رجیستر: ...
H2های پیشنهادی (سوالات واقعی کاربر): ...
سوالات متداول (۳–۶): ...
لینک‌های داخلی (انکر توصیفی): ...
CTA و مقصدش: ...
واقعیت‌های برند که اجازه‌ی استفاده داریم: ...
```

**Division of labor:** this skill owns the Persian *writing* layer. Full
technical SEO — site audits, schema validation, Core Web Vitals, backlinks,
maps/local packs — belongs to dedicated SEO tooling (e.g. an SEO plugin or
agency toolchain); write to their briefs and findings rather than guessing
technical facts.

### Verification for SEO/copy deliverables

Same pipeline as all Persian text: `persian_cleanup.py --edit` →
`fa_lint.py --check` → the native test — plus four genre checks:
does the title match ONE intent? is every factual claim sourced from the
user/brief? does the CTA verb match the register? does every page in a batch
carry genuinely unique content (no doorway clones)?



---

# PART 13 — Fonts

# Persian fonts: catalog, pairing, embedding

All fonts here are SIL OFL — free for commercial use, embedding allowed.
Bundled families live in `assets/fonts/`. The rest need
the download_fonts script (full package; chat-only AIs apply the equivalent rules manually) (requires GitHub access — will NOT work in
offline/allowlisted sandboxes; in that case use only what's bundled, or ask
the user to drop TTFs into the project folder).

## Catalog

| Font | Personality | Use for | Avoid for | Weights |
|---|---|---|---|---|
| **Vazirmatn** ★bundled | Neutral, clean, contemporary; the Persian Inter | Body text, UI, documents, anything | — (the safe default) | 9 (Thin–Black) |
| **Lalezar** ★bundled | Loud, friendly, poster/tabloid display | Headlines, covers, banners, campaign titles | Body text, long headings | 1 |
| **Shabnam** | Softer, rounder Vazir sibling | Body alternative, friendly docs | — | 5 + FD variants |
| **Sahel** | Modern, slightly condensed | Headings, dashboards, UI labels | Dense long-form body | 3 + FD |
| **Samim** | Sober text face tuned for reading | Long reports, articles, books | Display sizes | 3 + FD |
| **Parastoo** | Bookish, literary, mild serif flavor | Formal letters, literary/academic docs | Modern tech branding | 2 + FD |
| **Tanha** | Thin, elegant, airy display | Pull quotes, elegant covers, invitations | Body text (too light) | 1 |
| **Gandom** | Warm, rounded, approachable | Casual brochures, kids/food/lifestyle content | Corporate formal docs | 2 + FD |

("FD" variants ship with built-in Farsi digit glyphs mapped to ASCII digits —
prefer real Persian digit characters instead; see orthography.md.)

Sources (for `download_fonts.py` or manual download):
- Vazirmatn: github.com/rastikerdar/vazirmatn (also on Google Fonts)
- Lalezar: fonts.google.com/specimen/Lalezar (github.com/BornaIz/Lalezar)
- Others: github.com/rastikerdar/{shabnam,sahel,samim,parastoo,tanha,gandom}-font

## Pairings that work

| Deliverable | Headings | Body |
|---|---|---|
| Business proposal / invoice | Vazirmatn Bold/Black | Vazirmatn Regular |
| Marketing one-pager, poster | Lalezar | Vazirmatn |
| Long report / whitepaper | Vazirmatn Bold | Samim or Vazirmatn |
| Product docs / dashboard | Sahel Bold | Shabnam or Vazirmatn |
| Literary / formal letter | Parastoo Bold | Parastoo |
| Elegant cover + quote | Tanha (display) | Vazirmatn |

One display font per document, maximum. When in doubt: Vazirmatn everywhere,
weights for hierarchy.

## Typography rules for Persian

- **Line height:** Persian needs more leading than Latin — 1.6–2.0 in CSS,
  `line: 312+` (≥1.3) in docx, more for headings. Tight leading clips
  ascenders and dots.
- **Size:** Persian x-height runs small; bump body ~1pt/10% over the Latin
  equivalent (11–12pt docx body, 16–18px web).
- **Never letter-space** (`letter-spacing`/character spacing) — Persian letters
  join; tracking tears the joins apart. Not even for headings. Use size/weight/
  color for emphasis instead.
- **Never fake bold/italic.** Use real weights. Italic barely exists in Persian
  type; for emphasis use bold, color, or «گیومه».
- **Kashida (کشیده):** justification by stretching connections. Word processors
  do it automatically with justify; don't insert manual ـ characters.
- **Justified text** is traditional for print Persian body; START-aligned
  (ragged left) is fine for web and modern docs. Headings: never justify.

## Embedding per format

### docx (docx-js / python-docx)
Font name exactly as the family name: `"Vazirmatn"`, `"Lalezar"`.
Always with `hint: "cs"` (docx-js) or `w:rFonts w:cs=` (python-docx) — see
docx-pdf.md. The font must be installed on the converting machine
(`bash the install_fonts script (full package; chat-only AIs apply the equivalent rules manually)) or LibreOffice substitutes DejaVu.

### HTML / CSS
```css
@font-face {
  font-family: "Vazirmatn";
  src: url("fonts/Vazirmatn-Regular.woff2") format("woff2"),
       url("fonts/Vazirmatn-Regular.ttf") format("truetype");
  font-weight: 400; font-display: swap;
}
body {
  font-family: "Vazirmatn", "Segoe UI", Tahoma, sans-serif; /* Tahoma = classic Persian-safe fallback */
  line-height: 1.8;
}
```
Online pages can use Google Fonts (`family=Vazirmatn:wght@100..900` or
`family=Lalezar`); offline/PDF-print pages must reference local files —
copy them from `assets/fonts/`.

### pptx
Set the font on both latin and cs typefaces of every run (see pptx.md).
PowerPoint font embedding is unreliable cross-platform; if the deck must
travel, export a PDF (with fonts installed) alongside it.

### Checking a glyph exists (before using any symbol)
```python
from fontTools.ttLib import TTFont
cmap = TTFont("assets/fonts/Vazirmatn-Regular.ttf").getBestCmap()
ok = all(ord(c) in cmap for c in "•·۱۲۳؟،؛«»٪٬")
```
Known result for the bundled fonts: • · and all Persian punctuation/digits are
present; ▪ ■ ✓ ● ◆ are NOT (they silently fall back to DejaVu in PDFs). Check
before using anything fancier than • — `verify_pdf.py` will catch the fallback
after the fact, but checking first is cheaper.



---

# PART 14 — Word/DOCX + PDF

# Persian DOCX + PDF: RTL and pagination recipes

Battle-tested fixes from real Persian proposal production. The docx-js (npm `docx`)
examples are the reference implementation; python-docx equivalents follow at the
end. Read the whole file before generating a Persian Word document — most of these
failures are invisible until you convert to PDF and look.

**Pick your library FIRST, in 10 seconds:** if `docx` (npm) is already importable,
use the docx-js recipes. If not — and in sandboxed environments npm installs are
often blocked — do NOT spend time fighting the package manager: go straight to
python-docx (§6), which ships in most sandboxes and sets the exact same OOXML
flags. The concepts in §1–§5 (START-not-RIGHT, bidi, cs fonts, keepNext,
cantSplit) apply identically to both libraries.

**Colors in this file are placeholders.** Where an example sets `color`, a
border, or a fill, it uses neutral grey/black purely to show the property's
position. Do NOT reproduce these values as a look. Default to unstyled (black
text, no accent). Pull real colors only from the user's request, an attached
brand skill, a template you're matching, or a design direction the user chose
(document-design.md, §7 below). The RTL/pagination structure is the reusable
part; the styling is not.

## Table of contents

1. RTL: alignment, runs, tables, numbers, symbols, sections, styles
2. Divider/full-bleed pages (empty headers, titlePage, white-bar fix)
3. Pagination: orphan headings, unsplittable cards, blank pages, FAQ/tables
4. Fonts and PDF conversion workflow
5. Verification checklist (mandatory)
6. python-docx equivalents
7. Designed documents: applying tokens, reusing an existing template

---

## 1. RTL correctness

### 1.1 The core trap: RIGHT means visual LEFT in RTL

In OOXML, when `bidirectional: true` is set, `AlignmentType.RIGHT` is interpreted
as "end of text" — and in RTL, "end" is the **visual left**. Persian text aligned
RIGHT renders left-aligned. Use `START`, which in RTL always means visual right.

```javascript
// ❌ WRONG — left-aligns Persian in RTL
new Paragraph({
  alignment: AlignmentType.RIGHT,
  bidirectional: true,
  children: [new TextRun({ text: "متن فارسی", font: { name: "Vazirmatn" } })]
})

// ✅ RIGHT — visually right-aligned
new Paragraph({
  alignment: AlignmentType.START,
  bidirectional: true,
  children: [new TextRun({
    text: "متن فارسی",
    font: { name: "Vazirmatn", hint: "cs" },
    rightToLeft: true
  })]
})
```

`hint: "cs"` (Complex Script) tells Word this font applies to the Persian/Arabic
script run. Without it Word may pick a different font for Persian glyphs.
Audit rule: **grep your generator for `AlignmentType.RIGHT` — every hit is a bug**
(use `END` only when you deliberately want visual left, e.g. a Latin code block).

Define a helper once and use it for all Persian runs:

```javascript
const fa = (text, opts = {}) => new TextRun({
  text,
  rightToLeft: true,
  font: { name: "Vazirmatn", hint: "cs" },
  ...opts,
});
```

### 1.2 Tables must flow right→left

For any table where the first column belongs on the right (all Persian tables):

```javascript
new Table({
  width: { size: 100, type: WidthType.PERCENTAGE },
  visuallyRightToLeft: true,  // ← the key: first cell = visual right
  borders: allNoBorders,
  rows: [new TableRow({
    cantSplit: true,
    children: [
      new TableCell({ children: [/* first item — visual RIGHT */] }),
      new TableCell({ children: [/* second item — visual LEFT */] }),
    ]
  })]
})
```

Without `visuallyRightToLeft`, a two-column module list reads backwards.

### 1.3 Persian digits keep paragraphs RTL

A Latin digit at paragraph start flips the bidi direction of the line. Use
Persian digits in all Persian text, including list numbering:

```javascript
// ❌ Latin digit makes the paragraph LTR
fa((i + 1) + ".  ", { bold: true })

// ✅ Persian digit preserves RTL
const faDigits = "۰۱۲۳۴۵۶۷۸۹";
const toFa = (n) => String(n).replace(/[0-9]/g, d => faDigits[+d]);
fa(toFa(i + 1) + ".  ", { bold: true })
```

Prices too: «۲۵٬۰۰۰٬۰۰۰ تومان» (U+066C or ، as thousands separator — pick one
and be consistent).

### 1.4 Symbols: verify glyphs exist

Persian fonts miss many symbols; missing glyphs silently fall back to an ugly
substitute font in the PDF. Check before using:

```python
from fontTools.ttLib import TTFont
cmap = TTFont("Vazirmatn-Regular.ttf").getBestCmap()
print(0x2299 in cmap)  # ⊙ supported?
```

Verified safe in the bundled Vazirmatn and Lalezar: `•` (U+2022), `·` (U+00B7).
NOT in Vazirmatn/Lalezar (falls back to DejaVu): ▪ ■ ⊙ ◆ ✓ ✕ ● ○ and emoji.
Other Persian fonts have different coverage — run the check above before using
any symbol; a fallback shows up later as a DejaVu row in `pdffonts`.

### 1.5 Every section: bidi — and VERIFY it reached the XML

```javascript
sections.push({
  properties: {
    page: { size: { width: 11906, height: 16838 } },  // A4 portrait, twips
    bidi: true,  // ← required per section
  },
  children: [...]
})
```

**Setting it is not the same as it being written.** Some docx-js versions
silently drop `bidi` from section properties, and in python-docx it is easy to
append `<w:bidi/>` in the wrong position. `<w:bidi/>` must be the FIRST child
of `<w:sectPr>` (OOXML enforces child order — appended at the end, renderers
ignore it). Always check the produced file, not your source code:

```bash
unzip -p output.docx word/document.xml | grep -o '<w:sectPr[^>]*>.\{0,20\}'
# want: <w:sectPr ...><w:bidi/><w:pgSz .../>
# a sectPr going straight to <w:pgSz/> means the flag was dropped
```

**What section bidi actually controls** (measured, LibreOffice render):
it sets the section's BASE direction, which every element without its own
explicit direction inherits. A table with no `bidiVisual` renders its first
column on the LEFT without section bidi, and on the RIGHT with it — a silent
column-order reversal. Paragraphs and runs that DO carry their own
`bidirectional`/`rightToLeft` flags render correctly either way, so a
fully-flagged document may look fine and still be a trap: the first element
someone adds later without flags inherits the wrong direction.

Treat section bidi as the safety net, not the mechanism: set it, verify it in
the XML, AND set the per-paragraph/run/table flags. Belt and braces, because
each covers what the other misses.

**Patch it post-generation when the library drops it** — language-agnostic,
works on any .docx from any toolchain:

```python
import zipfile, re, shutil

def force_section_bidi(docx_path):
    """Insert <w:bidi/> as the first child of every <w:sectPr>. Idempotent."""
    tmp = docx_path + '.tmp'
    zin = zipfile.ZipFile(docx_path)
    items = {n: zin.read(n) for n in zin.namelist()}
    zin.close()
    xml = items['word/document.xml'].decode('utf-8')
    xml = re.sub(r'(<w:sectPr[^>]*>)(?!<w:bidi/>)', r'\1<w:bidi/>', xml)
    items['word/document.xml'] = xml.encode('utf-8')
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for n, d in items.items():
            zout.writestr(n, d)
    shutil.move(tmp, docx_path)
    return xml.count('<w:sectPr')
```

Node equivalent if you're in docx-js: same regex over `word/document.xml`
using `adm-zip` (`zip.readAsText` → replace → `zip.updateFile` → `writeZip`).
The `(?!<w:bidi/>)` guard keeps it safe to run twice.

### 1.6 Document default styles

```javascript
styles: {
  default: {
    document: {
      run: {
        font: { name: "Vazirmatn", hint: "cs" },
        size: 22,            // 11pt — half-points
        rightToLeft: true,
      },
      paragraph: {
        spacing: { line: 312 },   // ≈1.3 lines; Persian needs ≥1.3, tight leading clips
        bidirectional: true,
      },
    },
  },
}
```

---

## 2. Divider / full-bleed pages (OPTIONAL — only if the design calls for them)

This whole section is a technique, not a recommendation. Plain documents need
no divider pages. Build them only when the user's design or brand asks for
full-bleed color pages; otherwise skip §2 entirely.

Full-color divider pages must not show the running header/footer. Headers
inherit from the previous section unless you override with an *empty* header:

```javascript
const emptyPara = [new Paragraph({
  spacing: { before: 0, after: 0, line: 1, lineRule: "exact" },
  children: [new TextRun({ text: "", size: 1 })]
})];
const emptyHeader = {
  first: new Header({ children: emptyPara }),
  default: new Header({ children: emptyPara })
};
const emptyFooter = {
  first: new Footer({ children: emptyPara }),
  default: new Footer({ children: emptyPara })
};

sections.push({
  properties: {
    page: { margin: { top: 0, bottom: 0, left: 0, right: 0 } },
    bidi: true,
    titlePage: true,  // ← required for the empty first-page header to apply
  },
  headers: emptyHeader,
  footers: emptyFooter,
  children: buildDivider(...)
});
```

### White bars on dark pages (LibreOffice)

LibreOffice enforces a minimum header/footer margin, leaving white strips on
full-bleed dark pages. Fix in PDF post-processing with PyMuPDF — paint the
background color over the strips (set `BG` to the page's own color):

```python
import fitz  # PyMuPDF

BG = (r/255, g/255, b/255)  # set to the divider page's own background color

def fix_white_bars(pdf_path, is_dark_bg_page):
    doc = fitz.open(pdf_path)
    for page in doc:
        if is_dark_bg_page(page.get_text()):   # detect by known divider text
            r, over, bar, edge = page.rect, 5, 85, 5
            for box in [
                fitz.Rect(-over, -over, r.width + over, bar),                      # top
                fitz.Rect(-over, r.height - bar, r.width + over, r.height + over), # bottom
                fitz.Rect(-over, -over, edge, r.height + over),                    # left
                fitz.Rect(r.width - edge, -over, r.width + over, r.height + over), # right
            ]:
                page.draw_rect(box, color=BG, fill=BG, width=0)
    tmp = pdf_path + ".tmp"
    doc.save(tmp, deflate=True); doc.close()
    import os; os.replace(tmp, pdf_path)
```

---

## 3. Pagination

Four failure modes: orphan headings, split cards, blank pages, mid-sentence
breaks. All preventable at generation time.

### 3.1 No orphan headings

Every heading paragraph gets `keepNext` (stays with following content) and
`keepLines` (its own lines don't split):

```javascript
function sectionHeading(text) {
  return new Paragraph({
    alignment: AlignmentType.START,
    bidirectional: true,
    spacing: { before: 480, after: 280, line: 600, lineRule: "atLeast" },
    keepNext: true,
    keepLines: true,
    // border/color OPTIONAL and neutral — omit for plain output; set only
    // from the user's brief or brand. Structure is what matters here.
    children: [
      fa("•  ", { size: 32, bold: true }),   // • verified in Vazirmatn; ▪ is NOT
      fa(text, { size: 36, bold: true }),
    ],
  });
}
```

Apply to every heading level, FAQ questions (keep with their answer), and
workflow-step titles (keep with their description).

### 3.2 Unsplittable cards

Wrap each card/box in a single-cell table with `cantSplit` — if it doesn't fit,
the whole card moves to the next page instead of tearing in half:

```javascript
const cardChildren = [
  new Paragraph({ /* card title */ }),
  new Paragraph({ /* description */ }),
  new Paragraph({ /* price */ }),
  new Table({ /* module list */ }),
  new Paragraph({ /* delivery time */ }),
];

items.push(new Table({
  width: { size: 100, type: WidthType.PERCENTAGE },
  borders: allNoBorders,
  rows: [new TableRow({
    cantSplit: true,  // ← the whole card stays together
    children: [new TableCell({
      width: { size: 100, type: WidthType.PERCENTAGE },
      borders: allNoBorders,
      margins: { top: 0, bottom: 0, left: 0, right: 0 },
      children: cardChildren,
    })],
  })],
}));
```

Caveat: a card taller than one page will overflow — keep cards under ~¾ page.

### 3.3 No blank pages

Two causes. First, separators added after the *last* item:

```javascript
for (let i = 0; i < list.length; i++) {
  items.push(buildCard(list[i]));
  if (i < list.length - 1) {          // ← separator only BETWEEN items
    items.push(new Paragraph({
      spacing: { before: 100, after: 0 },
      // separator line optional; neutral grey placeholder if used at all
      border: { bottom: { style: BorderStyle.SINGLE, size: 3, color: "CCCCCC", space: 2 } },
      children: [new TextRun({ text: "" })],
    }));
  }
}
```

Second, manual `PageBreak` right before a section break:

```javascript
// ❌ empty paragraph + PageBreak at section end = blank page
items.push(new Paragraph({ children: [new TextRun({ text: "" })] }));
items.push(new Paragraph({ children: [new PageBreak()] }));

// ✅ a new section already starts a new page — no PageBreak needed
```

### 3.4 Paragraph integrity

```javascript
// Important/short paragraphs: don't strand them
new Paragraph({ keepNext: true, keepLines: true, /* ... */ });

// FAQ: question stays with answer
items.push(new Paragraph({
  keepNext: true, keepLines: true,
  children: [fa("۱. ", { bold: true }), fa(question, { bold: true })],
}));
items.push(new Paragraph({ children: [fa(answer)] }));
```

### 3.5 Multi-page data tables

```javascript
new TableRow({ tableHeader: true, cantSplit: true, children: headerCells }); // header repeats per page
new TableRow({ cantSplit: true, children: dataCells });                      // rows never split
```

---

## 4. Fonts and PDF conversion

1. Install fonts BEFORE converting (else LibreOffice substitutes silently):
   ```bash
   bash the install_fonts script (full package; chat-only AIs apply the equivalent rules manually) && fc-list | grep -i vazir
   ```
2. Convert: `soffice --headless --convert-to pdf output.docx`
3. Post-process white bars if you have full-bleed pages (§2).
4. Verify (§5).

Persian sizing guidance: body 11–12pt, line spacing ≥1.3 (`line: 312+`);
headings need `lineRule: "atLeast"` with generous values — Persian ascenders/
descenders clip in tight exact line heights.

---

## 4.5 Package integrity — "Word says the file is corrupt"

RTL correctness is worthless if Word refuses to open the file at all. A .docx is
a ZIP of XML parts, and a few structural rules decide whether Office accepts it:

| Requirement | Why it matters |
|---|---|
| `[Content_Types].xml` is the FIRST ZIP entry | Word may reject the package outright if it isn't |
| Every part's extension declared in `[Content_Types].xml` | undeclared part = "unreadable content" |
| Every `.rels` Target resolves to a real part | dangling relationship = repair prompt |
| Every XML part well-formed, no control chars (<0x20 except tab/LF/CR) | one stray byte kills the whole document |
| No duplicate part names | only the first wins; Word complains |

**python-docx ships a Word-for-Mac-2011 template — verified, not folklore.**
Every document created with `Document()` inherits these artifacts:

```
word/stylesWithEffects.xml            ← Mac-only part
docProps/thumbnail.jpeg               ← often malformed
xmlns:mo=... in document.xml          ← Mac namespace
<Application>Microsoft Macintosh Word</Application>, <AppVersion>14.0000
<?xml version='1.0' ...?>             ← single quotes, not Office's form
```

These usually open fine, but they are exactly the fingerprint found in files
that Word reports as corrupt on Windows. For anything you hand to a client,
clear them:

```bash
python3 scripts/verify_docx.py out.docx --fix --sanitize
```

`--sanitize` removes the stray parts, strips their references from
`[Content_Types].xml` and the `.rels` files (leaving them would create dangling
relationships — worse than the artifacts), and normalises the XML declarations.
It re-validates afterwards and refuses to hand back a package it just broke.
Measured on a real proposal: 17 parts → 15, content and RTL flags identical,
PDF conversion still clean.

**The nuclear option — LibreOffice round-trip.** LibreOffice parses leniently
and re-serialises into a clean, Office-compliant package, which fixes most
inherited corruption in one step:

```bash
soffice --headless --convert-to docx --outdir <OTHER_dir> input.docx
```

Input and output directories must differ, or soffice silently fails. Caveat:
a round-trip re-renders styles, so re-run the RTL checks afterwards — it can
also drop or alter formatting you set deliberately. Prefer `--sanitize` for
files you generated; keep the round-trip for files that arrive already broken.

**If a file is already corrupt**, work in this order: confirm it starts with the
bytes `PK\x03\x04`; run `verify_docx.py` to name the defective part; try the
LibreOffice round-trip; only then do manual surgery (rebuild the ZIP with
`[Content_Types].xml` first, dropping the offending part and every reference to
it). Never edit the user's original — always work on a copy.

## 5. Verification checklist (run every time)

`python3 the verify_pdf script (full package; chat-only AIs apply the equivalent rules manually) output.pdf --expect-font Vazirmatn` automates
these; the manual equivalents:

```bash
# 1. Near-empty pages (orphaned headings / stray breaks)
pdftotext -layout output.pdf check.txt
python3 - <<'EOF'
pages = open('check.txt').read().split('\x0c')
for i, p in enumerate(pages, 1):
    lines = [l.strip() for l in p.split('\n') if l.strip()]
    content = [l for l in lines if not l.isdigit()]   # drop bare page numbers
    if len(content) < 3 and i < len(pages):
        print(f'page {i}: possibly empty ({len(content)} content lines)')
EOF

# 2. Template leaks
grep -iE "undefined|NaN|null" check.txt

# 3. Fonts actually embedded (every row should say your font, emb=yes;
#    any DejaVu/Liberation row = fallback happened somewhere)
pdffonts output.pdf

# 4. Page count sanity
python3 -c "from pypdf import PdfReader; print(len(PdfReader('output.pdf').pages))"
```

Then open the PDF (or render pages to PNG with PyMuPDF and *look*): right
alignment on every page, no orphan headings, no split cards, digits Persian.

---

## 6. python-docx equivalents

python-docx has no first-class RTL API; set the OOXML elements directly.

```python
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt

def _set(el, parent):
    parent.append(el); return el

def rtl_paragraph(p):
    """bidi paragraph; leave w:jc unset (bidi default start = visual right),
    or set start explicitly. NEVER set alignment RIGHT on a bidi paragraph."""
    pPr = p._p.get_or_add_pPr()
    if pPr.find(qn('w:bidi')) is None:
        bidi = OxmlElement('w:bidi'); bidi.set(qn('w:val'), '1'); pPr.append(bidi)
    jc = pPr.find(qn('w:jc'))
    if jc is None:
        jc = _set(OxmlElement('w:jc'), pPr)
    jc.set(qn('w:val'), 'start')

def fa_run(p, text, font='Vazirmatn', size=11, bold=False):
    run = p.add_run(text)
    run.bold = bold
    rPr = run._r.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts')) or _set(OxmlElement('w:rFonts'), rPr)
    for attr in ('w:ascii', 'w:hAnsi', 'w:cs'):
        rFonts.set(qn(attr), font)
    _set(OxmlElement('w:rtl'), rPr)                       # complex-script run
    szCs = _set(OxmlElement('w:szCs'), rPr)               # CS size (else tiny/huge)
    szCs.set(qn('w:val'), str(int(size * 2)))
    run.font.size = Pt(size)
    if bold:
        _set(OxmlElement('w:bCs'), rPr)                    # CS bold
    return run

def rtl_table(table):
    tblPr = table._tbl.tblPr
    if tblPr.find(qn('w:bidiVisual')) is None:
        tblPr.append(OxmlElement('w:bidiVisual'))          # first col = visual right

def rtl_section(section):
    sectPr = section._sectPr
    if sectPr.find(qn('w:bidi')) is None:
        sectPr.append(OxmlElement('w:bidi'))

def keep_with_next(p):
    pPr = p._p.get_or_add_pPr()
    pPr.append(OxmlElement('w:keepNext'))
    pPr.append(OxmlElement('w:keepLines'))

def cant_split(row):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(OxmlElement('w:cantSplit'))

def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    tblHeader = OxmlElement('w:tblHeader'); tblHeader.set(qn('w:val'), 'true')
    trPr.append(tblHeader)
```

Notes that bite in python-docx specifically:
- `w:szCs` matters: without it, complex-script text ignores your size.
- `w:bCs` matters: bold Persian needs it, or only Latin runs embolden.
- The unsplittable-card trick is identical: 1×1 table + `cant_split(row)`.
- Same digits/symbols/verification rules as above — they're format rules,
  not library rules.

### 6.1 Three failures the per-paragraph helpers do NOT fix

Setting bidi on every paragraph you create still leaves three holes, because
Word/LibreOffice pull from `styles.xml` and `numbering.xml`, which python-docx
generates from a Latin default template. All three are verified failures, not
theory: without the fix below, a test document rendered `.1` (Latin digit,
wrong side) for list items, a blue Heading nobody asked for, and pulled DejaVu +
OpenSymbol into the PDF. With it: Persian «۱.», black heading, Vazirmatn only.

**Run this once, right after `Document()`, before adding content:**

```python
from docx.shared import Pt, RGBColor

def persianize_styles(doc, font='Vazirmatn', size=11):
    """Fix the document-wide defaults python-docx inherits from its Latin template.
    Without this: Latin list numbers, Word's blue headings, DejaVu fallback."""
    st = doc.styles['Normal']
    st.font.name = font
    st.font.size = Pt(size)
    rPr = st.element.get_or_add_rPr()
    rF = rPr.find(qn('w:rFonts'))
    if rF is None:
        rF = _set(OxmlElement('w:rFonts'), rPr)
    for a in ('w:ascii', 'w:hAnsi', 'w:cs'):
        rF.set(qn(a), font)                       # cs = the Persian-shaping slot
    _set(OxmlElement('w:rtl'), rPr)
    _set(OxmlElement('w:szCs'), rPr).set(qn('w:val'), str(int(size * 2)))
    _set(OxmlElement('w:bidi'), st.element.get_or_add_pPr())

    # Built-in Heading styles: Persian font, bidi, and NO inherited color.
    # Word's Heading 1-4 default to blue — an accent the user never asked for.
    for i in range(1, 5):
        try:
            h = doc.styles[f'Heading {i}']
        except KeyError:
            continue
        h.font.name = font
        h.font.color.rgb = RGBColor(0, 0, 0)      # neutral; see SKILL.md visual neutrality
        hr = h.element.get_or_add_rPr()
        hf = hr.find(qn('w:rFonts'))
        if hf is None:
            hf = _set(OxmlElement('w:rFonts'), hr)
        for a in ('w:ascii', 'w:hAnsi', 'w:cs'):
            hf.set(qn(a), font)
        _set(OxmlElement('w:rtl'), hr)
        _set(OxmlElement('w:bidi'), h.element.get_or_add_pPr())
```

`verify_docx.py` validates `w:rtl`, `w:cs`, and `w:szCs` at both run level and style level (`styles.xml`), so documents initialized with `persianize_styles()` pass cleanly without requiring redundant inline properties on every single run.

**Numbered and bulleted lists: do NOT use the built-in list styles.**
`doc.add_paragraph(style='List Number')` writes numbering into `numbering.xml`,
which carries no bidi and renders Latin `1.` on the wrong side; the `List
Bullet` glyph comes from OpenSymbol and drags a fallback font into the PDF.
Number manually instead — the marker becomes a normal Persian run you control:

```python
FA_DIGITS = "۰۱۲۳۴۵۶۷۸۹"
to_fa = lambda n: str(n).translate(str.maketrans("0123456789", FA_DIGITS))

for i, item in enumerate(items, 1):
    p = rtl_paragraph(doc.add_paragraph())
    fa_run(p, f"{to_fa(i)}.  ")     # ۱.  ۲.  ۳. — stays RTL, right side
    fa_run(p, item)

for item in bullets:
    p = rtl_paragraph(doc.add_paragraph())
    fa_run(p, "•  ")                # • verified in Vazirmatn; ▪ is NOT
    fa_run(p, item)
```
Indent with `p.paragraph_format.right_indent` (RTL side), not `left_indent`.

**Headers and footers are separate XML parts** (`header1.xml`, `footer1.xml`)
and inherit nothing from the body — apply `rtl_paragraph` + `fa_run` to each:

```python
for section in doc.sections:
    for part in (section.header, section.footer):
        for p in part.paragraphs:
            rtl_paragraph(p)
            # rebuild text through fa_run so the cs font/rtl flags exist
```
Page numbers in footers: a Latin field digit flips the line — prefer a Persian
literal, or accept Latin numerals in the footer only.

**Confirm the fix in the output, not the code:** `pdffonts out.pdf` must list
your Persian font and nothing else. A `DejaVu` or `OpenSymbol` row means a
glyph fell back — usually a list bullet or a symbol from §1.4.
the verify_pdf script (full package; chat-only AIs apply the equivalent rules manually) flags this automatically.

## 7. Designed documents

Design levels and how a look is chosen: document-design.md. This section is
the Word side.

### 7.1 Applying a chosen direction's tokens (python-docx)

`design_samples.py` writes the chosen direction's tokens (`head_font`,
`accent`, `box_bg`, `table_head_bg`, …). Apply them to styles, not run by run,
so every later paragraph inherits them:

```python
from docx.shared import RGBColor, Pt
from docx.oxml.ns import qn

def hexrgb(h): return RGBColor.from_string(h.lstrip("#").upper())

def apply_tokens(doc, tk):
    for name, size in (("Heading 1", 20), ("Heading 2", 15), ("Heading 3", 13)):
        st = doc.styles[name]
        st.font.name = tk["head_font"]; st.font.size = Pt(size)
        st.font.color.rgb = hexrgb(tk["accent"])
        rfonts = st.element.get_or_add_rPr().get_or_add_rFonts()
        for attr in ("w:ascii", "w:hAnsi", "w:cs"):
            rfonts.set(qn(attr), tk["head_font"])
    body = doc.styles["Normal"]
    body.font.color.rgb = hexrgb(tk["ink"])

def shade(cell, hex_fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = tcPr.makeelement(qn("w:shd"), {qn("w:val"): "clear", qn("w:color"): "auto",
                                         qn("w:fill"): hex_fill.lstrip("#")})
    tcPr.append(shd)
```

- A callout box is a one-cell table with `cantSplit`, shaded with `box_bg`
  and a start-side border in `box_rule` (§3.2 for the unsplittable card).
- The header row of a data table is shaded `table_head_bg`, its text
  `table_head_ink`; mark it `tblHeader` so it repeats across pages (§3.5).
- Covers and number tiles are images rendered from HTML
  (document-design.md «Figures»); place them full-width.
- Lalezar is a display font: headings and covers only, never body text.

### 7.2 Checking a designed DOCX

Run `verify_docx.py` as usual, then export to PDF (LibreOffice, or Word's
`ExportAsFixedFormat` through COM on Windows) and look at every page as an
image. Designed documents fail visually, not structurally: a stale figure, a
cover with the old title, a heading alone at the bottom of a page.

### 7.3 Building on an existing designed document

When the user's own DOCX already has a design (title font, colours, boxes,
tables, figures), keep it by **cloning its elements as templates** instead of
recreating styles:

1. Copy the source file and open the copy with python-docx.
2. List the body elements in order and pick one template for each role: main
   heading (often with `pageBreakBefore`), sub-heading, body paragraph,
   bold-lead paragraph («**اجرا.** …»), bullet, caption, callout box (a table),
   data table, each figure paragraph, the cover, the section breaks.
3. Build the new body from `copy.deepcopy(template)` and replace only the text:
   keep the first run of each role (its `rPr` carries the design), set its
   `w:t`, drop the other runs. For a table with a different number of columns,
   rebuild `w:tblGrid` and clone header and body cells from the template row.
4. Keep the cover paragraph and the section-break paragraph first and the final
   `sectPr` last; remove everything else from the body and append the new
   elements in order.
5. Replace stale images by swapping the image part's bytes
   (`rel.target_part._blob = new_png`) at the same pixel size, so the frame
   and its position stay.
6. Add `<w:bidi/>` to every paragraph and `<w:rtl/>` to every run that holds
   Persian; template files often rely on Word's defaults, and verify_docx
   then reports a missing base direction.
7. Convert Persian digits in the new text runs, then run verify_docx with
   `--fix` and look at the PDF.



---

# PART 15 — PowerPoint

# Persian PowerPoint: RTL slides with python-pptx

PowerPoint has no document-level RTL switch — direction is set per paragraph
and per run, which is why half-fixed Persian decks are so common. Every text
frame needs the treatment below.

## Core helpers (python-pptx)

```python
from pptx.util import Pt
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from lxml import etree

def rtl_paragraph(paragraph, align=PP_ALIGN.RIGHT):
    """RTL direction + visual-right alignment for a pptx paragraph.
    In DrawingML (unlike OOXML/docx!) algn='r' is PHYSICAL right — safe to use."""
    paragraph.alignment = align
    pPr = paragraph._p.get_or_add_pPr()
    pPr.set('rtl', '1')

def fa_run(run, font='Vazirmatn', size=18, bold=False, color=None):
    run.font.name = font          # sets latin typeface
    run.font.size = Pt(size)
    run.font.bold = bold
    if color: run.font.color.rgb = color
    rPr = run._r.get_or_add_rPr()
    rPr.set('lang', 'fa-IR')
    cs = rPr.find(qn('a:cs'))
    if cs is None:
        cs = etree.SubElement(rPr, qn('a:cs'))
    cs.set('typeface', font)      # complex-script typeface — REQUIRED for Persian

def fa_text_frame(tf, font='Vazirmatn', size=18):
    """Apply to every paragraph+run in a text frame."""
    for p in tf.paragraphs:
        rtl_paragraph(p)
        for r in p.runs:
            fa_run(r, font=font, size=size)
```

Key facts:
- `a:cs` typeface is what actually renders Persian glyphs. Setting only
  `run.font.name` leaves Persian on the theme's default CS font.
- DrawingML `algn="r"` is physical right (the docx START/RIGHT trap does
  NOT apply to pptx). `rtl="1"` controls word order/bidi, `algn` controls
  which edge. Persian body/title: `rtl='1'` + `PP_ALIGN.RIGHT`.
  Centered titles: `rtl='1'` + `PP_ALIGN.CENTER` is fine.

## Layout mirroring

Persian slides mirror LTR conventions:
- Title right-aligned (or centered), content starts at the top-right.
- Two-column "image + text": image LEFT, text RIGHT (reader enters from right).
- Process/timeline arrows flow right→left; flip arrow glyphs (→ becomes ←).
- Agenda/bullet columns: rightmost column is "first".
- Logos: keep brand corner conventions, but nav-like elements mirror.

## Bullets and numbering

```python
# Persian-safe bullet char (theme bullets often lack Persian-font glyphs).
# • is verified in Vazirmatn/Lalezar; ▪ is NOT (falls back to DejaVu).
pPr = paragraph._p.get_or_add_pPr()
buFont = etree.SubElement(pPr, qn('a:buFont')); buFont.set('typeface', 'Vazirmatn')
buChar = etree.SubElement(pPr, qn('a:buChar')); buChar.set('char', '•')
```

Numbered lists: `buAutoNum` renders Latin digits only. For Persian numbering,
disable auto bullets (`a:buNone`) and prefix runs manually: «۱. »، «۲. » —
Persian digits keep the line RTL (same rule as docx).

## Tables

`a:tbl` has no bidiVisual equivalent that survives PowerPoint round-trips.
Build RTL tables by **reversing column order yourself** (first data column =
rightmost cell) and applying `rtl_paragraph`/`fa_run` to every cell. Header
row: bold + fill; keep rows short — pptx tables don't paginate.

## Fonts and delivery

- Use bundled Vazirmatn (+ Lalezar for title slides) — see fonts.md pairings.
- PowerPoint font embedding is flaky cross-platform (and python-pptx can't do
  it). If the deck travels beyond machines with the fonts installed, ALWAYS
  ship a PDF export alongside: install fonts (`bash the install_fonts script (full package; chat-only AIs apply the equivalent rules manually)),
  then `soffice --headless --convert-to pdf deck.pptx`, then
  `python3 the verify_pdf script (full package; chat-only AIs apply the equivalent rules manually) deck.pdf --expect-font Vazirmatn`.
- No letter-spacing on Persian, real bold weights only, line spacing ≥1.3
  (`paragraph.line_spacing = 1.3`).

## If building via the pptx skill's HTML pipeline (html2pptx)

Apply html-css.md rules in the source HTML: `<html dir="rtl" lang="fa">`,
Vazirmatn @font-face, `text-align: right`, Persian digits, no letter-spacing.
Then visually verify a rendered screenshot of at least the first 3 slides —
bidi bugs in HTML pipelines show up as scrambled punctuation at line edges.

## Checklist

1. Every paragraph: `rtl='1'`; every run: `a:cs` typeface set.
2. Persian digits in all visible numbers (slide numbers can stay Latin).
3. Layout mirrored (text right, flow right→left).
4. Bullets use verified glyphs (• · in Vazirmatn), numbering manual Persian.
5. Tables column-reversed.
6. PDF exported with fonts installed + verify_pdf.py clean.



---

# PART 16 — HTML / CSS / email

# Persian HTML/CSS: RTL web pages, emails, and HTML→PDF

## The foundation

```html
<!DOCTYPE html>
<html dir="rtl" lang="fa">
```

`dir="rtl"` on `<html>` flips the whole layout: text flows right→left, flex/grid
main axes reverse, tables mirror, list markers move right. Most "RTL bugs" come
from fighting this with hard-coded `left`/`right` afterwards.

## CSS rules

### Use logical properties, not physical

| Physical (breaks RTL) | Logical (RTL-safe) |
|---|---|
| `margin-left` | `margin-inline-start` |
| `padding-right` | `padding-inline-end` |
| `text-align: left` | `text-align: start` |
| `border-left` | `border-inline-start` |
| `left: 0` | `inset-inline-start: 0` |

`text-align: right` is acceptable at the page level for Persian (it equals
`start` under `dir=rtl`), but inside components prefer `start`/`end` so the
component survives reuse.

### Typography

```css
body {
  font-family: "Vazirmatn", "Segoe UI", Tahoma, sans-serif;
  font-size: 17px;          /* Persian reads small — go one step larger */
  line-height: 1.8;         /* 1.6 minimum; Persian clips below that */
  letter-spacing: 0;        /* NEVER track Persian — it breaks letter joins */
}
h1, h2, h3 { line-height: 1.5; font-weight: 700; }  /* real weights, no faux bold */
```

Display headings: `font-family: "Lalezar"` — one display face per page, max.

### Mixed-direction content (the hard part)

Latin fragments (brand names, URLs, code, phone numbers) inside Persian text
disrupt bidi ordering. Tools:

```html
<!-- isolate an LTR fragment so surrounding punctuation doesn't scramble -->
<p>افزونه <bdi>WooCommerce 9.5</bdi> را نصب کنید.</p>

<!-- force a whole block LTR (code, addresses, phone) -->
<pre dir="ltr">npm install docx</pre>
<span dir="ltr">+98 912 345 6789</span>
```

CSS equivalent: `unicode-bidi: isolate` (default for `<bdi>`).
Fix stray punctuation jumping to the wrong side with `&lrm;`/`&rlm;` marks —
but if you need many of them, wrap the fragment in `<bdi>` instead.

Numbers: use Persian digits ۰-۹ in prose (they inherit RTL correctly).
Keep inputs like phone/URL fields `dir="ltr"` with `text-align: start`.

### Layout mirroring

- Flex/grid auto-mirror under `dir=rtl` — write `flex-direction: row` and let
  the browser flip it. Don't write `row-reverse` to "fix" RTL; that double-flips.
- Icons with direction (arrows, chevrons, back buttons): mirror with
  `[dir="rtl"] .icon-arrow { transform: scaleX(-1); }`. Symmetric icons stay.
- Shadows/border-radius asymmetries: use logical values or mirror per-dir.
- Carousels/sliders: reverse advance direction; "next" points left in RTL.

### Lists and tables

```css
ul, ol { padding-inline-start: 1.5em; }   /* not padding-left */
```
Ordered lists: browsers render Latin digits by default; for Persian numbering
use `list-style: arabic-indic` (`list-style-type: persian` where supported) or
generate markers manually with Persian digits.

Tables under `dir=rtl` mirror automatically: first `<th>` renders rightmost. ✓

## Persian web fonts

See fonts.md for the catalog. Online: Google Fonts serves Vazirmatn and Lalezar:

```html
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&family=Lalezar&display=swap" rel="stylesheet">
```

Offline / HTML→PDF / email: embed local files from `assets/fonts/` via
`@font-face`. Never rely on system fonts for Persian — Windows falls back to
Segoe UI (passable), macOS to Geeza Pro (wrong flavor), Linux to DejaVu (broken).

## HTML email

Email clients strip `<style>` unpredictably:
- `dir="rtl"` attribute on every structural `<table>`, `<td>`, `<div>` — not CSS.
- Inline styles only: `style="font-family:Tahoma,Arial; text-align:right; direction:rtl"`.
- Web fonts don't load in most clients → Tahoma is the classic Persian-safe
  email font stack.
- Test: Gmail web strips `<head>` styles; Outlook desktop ignores web fonts.

## HTML→PDF (weasyprint / headless Chrome)

The pagination principles from docx-pdf.md, in CSS:

```css
@page { size: A4; margin: 2cm; }
h1, h2, h3, h4 { break-after: avoid; }        /* no orphan headings */
.card, .price-box, figure { break-inside: avoid; }  /* no split cards */
p { orphans: 2; widows: 2; }                   /* no lonely lines */
.divider-page { break-before: page; break-after: page; }
```

- weasyprint honors `break-*` well and embeds @font-face fonts — good default.
- Headless Chrome (`--print-to-pdf`) also works; ensure fonts are installed
  (`bash the install_fonts script (full package; chat-only AIs apply the equivalent rules manually)) or referenced via @font-face with absolute
  paths.
- Verify the output exactly like a docx-derived PDF:
  `python3 the verify_pdf script (full package; chat-only AIs apply the equivalent rules manually) out.pdf --expect-font Vazirmatn`.

## Pre-delivery checklist

1. `<html dir="rtl" lang="fa">` present.
2. No physical left/right properties that fight RTL (grep for `margin-left`,
   `text-align: left`, `padding-right` and justify each hit).
3. `letter-spacing` nowhere on Persian text.
4. Latin fragments wrapped in `<bdi>`/`dir="ltr"`.
5. Persian digits in prose; `persian_cleanup.py --edit` + `fa_lint.py --check`
   on the text content.
6. Fonts load (DevTools → Network, or pdffonts on the exported PDF).
7. If printed/PDF: break rules applied, then verify_pdf.py.



---

# PART 17 — Images, reportlab PDFs, Excel

# Persian patches for format-skill toolchains

The general docx/pptx/pdf/xlsx/canvas skills assume Latin text. Their default
toolpaths silently mangle Persian: disconnected letters, reversed order,
left-aligned sheets. This file patches each toolchain. (docx → docx-pdf.md,
pptx → pptx.md; this file covers the rest.)

## 1. Images & posters (canvas-design skill, PIL/Pillow)

Naive `draw.text(..., 'سلام دنیا')` renders Persian LEFT-to-right with
DISCONNECTED letters — instantly, obviously broken to any reader.

**Check raqm first** (complex-script shaping engine in Pillow):

```python
from PIL import features
assert features.check('raqm')   # True in most modern Pillow builds
```

**No raqm (common on Windows) → render HTML instead.** Do not ship reshaped-
and-reversed tricks. Write the image as an HTML page with the bundled fonts
(`@font-face` pointing at `assets/fonts/*.ttf` by file:// URL) and render it
with a headless browser, which shapes Persian correctly:
`python scripts/render_html.py poster.html poster.png --size 1080x1350`
(document-design.md «Figures»).

**With raqm (the normal case)** — pass direction and language, anchor right:

```python
from PIL import Image, ImageDraw, ImageFont
font = ImageFont.truetype('assets/fonts/Vazirmatn-Bold.ttf', 48)
draw.text(
    (width - margin, y),          # x = RIGHT edge of the text block
    'سلام دنیا ۱۲۳',
    font=font, fill='#111',
    direction='rtl', language='fa',
    anchor='ra',                   # right-aligned, ascender baseline
)
```

- Multi-line: draw each line separately (or `multiline_text` with
  `direction='rtl'` + `align='right'`), line height ≥ 1.6 × font size —
  Persian clips in tight leading.
- Mixed Persian/Latin in one line: raqm handles bidi correctly — do NOT
  reverse strings manually.
- Never letter-space; use Lalezar for display headlines, Vazirmatn otherwise
  (fonts.md pairings apply to posters too).
- Persian digits ۰-۹ in all visible numbers.

**Without raqm** (older Pillow, no libraqm): shaping needs
`arabic_reshaper` + `python-bidi`:

```python
import arabic_reshaper
from bidi.algorithm import get_display
shaped = get_display(arabic_reshaper.reshape('سلام دنیا'))
draw.text((x, y), shaped, font=font)   # per line; bidi already applied
```

These packages may not be installable in sandboxed environments — if neither
raqm nor reshaper is available, render the text via HTML→screenshot instead
of PIL.

**Verify visually, always:** render, then look at the image (or ask a
subagent to). Broken shaping is invisible in code and screaming in pixels.

## 2. Creating PDFs (pdf skill, reportlab)

**reportlab has no bidi and no Arabic shaping.** `drawString('متن فارسی')`
produces reversed, disconnected glyphs. Do not fight it. Route Persian PDF
creation through a pipeline that shapes text natively:

1. **python-docx → LibreOffice** (sandbox-proven, default):
   build the document with the docx-pdf.md recipes, install fonts
   (the install_fonts script (full package; chat-only AIs apply the equivalent rules manually)), then
   `soffice --headless --convert-to pdf file.docx`.
2. **HTML → PDF** (weasyprint or headless Chrome, where available): write
   RTL HTML per html-css.md with `@page` rules, convert.
3. reportlab ONLY if the environment has `arabic_reshaper` + `python-bidi`
   AND the layout truly needs canvas-level control:

```python
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import arabic_reshaper
from bidi.algorithm import get_display

pdfmetrics.registerFont(TTFont('Vazirmatn', 'assets/fonts/Vazirmatn-Regular.ttf'))
c.setFont('Vazirmatn', 14)
line = get_display(arabic_reshaper.reshape('متن فارسی ۱۲۳'))
c.drawRightString(page_width - margin, y, line)   # right-anchored per line
```

Manipulating EXISTING Persian PDFs (merge/split/rotate/extract via pypdf,
form-filling) is safe — those operations never touch text shaping.
Always finish with the verify_pdf script (full package; chat-only AIs apply the equivalent rules manually) out.pdf --expect-font Vazirmatn`.

## 3. Excel (xlsx skill, openpyxl / pandas)

Three invisible-until-opened problems: sheets open left-to-right, cells
left-align, fonts fall back.

```python
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment

wb = Workbook(); ws = wb.active
ws.title = 'گزارش فروش'

ws.sheet_view.rightToLeft = True          # ← THE critical line, per sheet

fa_font   = Font(name='Vazirmatn', size=11)
fa_header = Font(name='Vazirmatn', size=11, bold=True)
fa_align  = Alignment(horizontal='right', vertical='center',
                      readingOrder=2)     # 2 = right-to-left reading order

for cell in row:
    cell.font = fa_font
    cell.alignment = fa_align
```

- Set `rightToLeft` on EVERY worksheet (it's a per-sheet property).
- **Numbers stay real numbers** (Latin digits in numeric cells) so formulas,
  sorting and charts keep working; Persian digits belong in text/label cells.
  Give currency cells a format like `#,##0 "تومان"`.
- Headers, sheet names, chart titles: Persian, Vazirmatn, bold.
- pandas: `df.to_excel(...)` first, then reopen with openpyxl to apply
  rightToLeft + fonts + alignment (pandas can't set them).
- Column order: with rightToLeft the first column (A) displays rightmost —
  which is where Persian readers expect the first column. Write data in
  logical order and let the view mirror it.

### 3.1 Editing an existing workbook

Writing a NEW workbook with openpyxl is safe. Re-saving an EXISTING one is
not always: openpyxl rewrites the whole package, drops every cached formula
value, and can lose parts it does not model. In the first real use, a budget
workbook with links to two external files came back from a plain
`load_workbook(...).save(...)` round trip as a file Excel refused to open.
- Before editing a user's workbook, round-trip it once unchanged and open the
  result in the real application (or LibreOffice) before trusting it.
- Files with external links, pivot tables, macros, slicers, charts or data
  validation: edit them with the application itself. On Windows with Excel
  installed, drive Excel through COM from PowerShell
  (`New-Object -ComObject Excel.Application`, `Workbooks.Open`, write
  `Range(...).Formula` / `.Value2`, `CalculateFull()`, `Save()`). Excel keeps
  every part and recalculates, so the new numbers can be read back and quoted.
- PowerShell 5.1 traps met while doing this:
  - a parameter declared `[string]$X` stays typed, and `$x = @(...)` later
    turns the array into one string (variable names are case-insensitive);
  - `ConvertFrom-Json` on a top-level array returns it as ONE object, so
    `foreach` sees one item; unwrap with `@($raw | ForEach-Object { $_ })`;
  - `$xl.CutCopyMode = 0` fails; copy formats with
    `$src.Copy($dst)` (no clipboard) and then `$dst.ClearContents()`;
  - write the script file as UTF-8 **with BOM**, or Persian sheet names break.
- Add, never delete: new years go in new columns, new plans in a new sheet,
  assumptions in clearly marked input cells; leave the user's cells alone and
  report suspected errors (a typo, a stray value) instead of fixing them.
- Never leave the user's file open in your own Excel instance; close and quit.

## 4. Quick router

| Deliverable | Toolpath | Reference |
|---|---|---|
| Word/report/proposal | docx-js or python-docx → soffice PDF | docx-pdf.md |
| Slides | python-pptx (or html2pptx via RTL HTML) | pptx.md |
| Web page / email | RTL HTML/CSS | html-css.md |
| New PDF | docx or HTML pipeline, NOT raw reportlab | this file §2 |
| Poster/social image | PIL + raqm (direction='rtl'), or HTML → render_html.py | this file §1 |
| Cover, figure, number tiles in a document | HTML → render_html.py | document-design.md |
| Spreadsheet | openpyxl + rightToLeft + Vazirmatn; existing workbook → this file §3.1 | this file §3 |
