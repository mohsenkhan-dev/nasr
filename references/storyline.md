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
covering one or more storyline sentences. Headings are plain: a short topic
or a short claim, no colon, no question mark, no slogan.

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
