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

## Choosing the depth

| Situation | Path |
|---|---|
| Long (over ~600 words), high-stakes, public, or the user asked for options | All four stages |
| 300–600 words, purpose clear | Stage 1 as a short restatement, stage 2 as one stated choice, then stage 4 |
| Under 300 words, transactional (email, caption, UI copy, notice) | Skip to writing; register rules in writing-style.md are enough |
| The user named the style or said «فقط بنویس» | State the style in one line and go to stage 4 |
| Light edit of the user's own text | Stage 1 only on what the text is for; keep their style unless asked |
| Rewriting an existing document («بازنویسی کن»، «با نثر بنویس») | The rewrite path below: measure, diagnose, then the four stages on the document's own material |

When in doubt, run stages 1 and 2 in one message: a restatement plus style cards.
That is one exchange and it prevents most rewrites.

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
- **Strategy document, roadmap, proposal to a board**: the سند راهبردی recipe and its section map (recommended), plus a variant that changes one thing, for example «ما» instead of the organization's name when the document is signed by its management.
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

Ask the user to choose with one question (AskUserQuestion where available;
options in the user's language, the recommended card first). Allow «ترکیب ۱ و
۳» as an answer: combining is normal (style-framework.md §5).

## Stage 2b: build the skeleton (اسکلت)

A style is a way of thinking before it is a way of writing. Before any prose,
fill the chosen recipe's skeleton (style-skeletons.md) with real content: one
note per slot. Check it:
- **Every slot filled with real content.** An empty slot means the style does not fit or material is missing. Change the style or ask; do not write around the gap.
- **The payoff is where the style puts it.** Reports end on targets; strategy opens on the diagnosis and ends on the ask; narratives give the meaning after the scene.
- **The thinking slots are filled boldly**: diagnosis, crux, trade-off, drivers, indicators. These are the writer's reasoning and are expected; facts stay as the material gives them.

For long or high-stakes texts, show the skeleton before drafting.

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
2. **Draft from the skeleton** (stage 2b), slot by slot. Use two to four moves from style-moves.md, not all of them. Keep the concept from stage 1 visible: in the opening, and again where the argument turns or closes.
3. **Checks**, in this order:
   - Facts: every name, figure, date and quotation traces to the user, a document or a source you found. Mark anything unverified.
   - Rhythm: `python3 scripts/style_check.py draft.md --recipe "<recipe>"` (or `--profile`); for a sectioned text, `--sections`, which measures each section against its declared profile and flags jumps between non-neighbouring profiles. Revise features outside the band. Under ~400 words, fix only clear deviations: chasing every band swings the draft (style-evidence.md, worked test).
   - Orthography: `python3 scripts/persian_cleanup.py --edit`, then `python3 scripts/fa_lint.py --check`.
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
- Figures and images become caption markers («تصویر ۲: …») in their place, so the rewrite keeps their position.
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
