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
