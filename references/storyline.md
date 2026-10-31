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

The recipe's arc (style-skeletons.md) tells you what kind of claims the
storyline needs and where the payoff goes: a strategy needs a diagnosis, a
crux and a trade-off; a report puts targets at the end. The arc is the plan;
the storyline is the plan filled with claims.

**Show the level-1 storyline and headings to the user before going on** for
any long or high-stakes text. It is ten lines; correcting it costs nothing
compared with correcting prose.

## Level 2: the storyline of each section

Under each heading, write the section's own chain: 3–6 claim sentences,
which will become the first sentences of its paragraphs. Next to each one,
note its support:
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
