# Evidence behind the style framework

What style-framework.md and style-moves.md rest on, and how far to trust them.
No source text is reproduced in this skill; only measurements and invented
examples are.

## Corpus (collected 2026-10)

| Group | Sources | Texts | Words |
|---|---|---|---|
| Columnists and essayists | signed posts and columns of nine writers: personal Telegram channels, personal WordPress sites, and news republications of signed notes | 620 | ~560,000 |
| Brand annual reports | Digikala 1403 and 1404 (PDF), Snapp 1403 (PDF) and Snapp yearly report posts 1401, 1402, 1403 CSR, 1404 | 7 | ~34,000 |
| Institutional reports | Mobarakeh Steel sustainability 1402 and 1404, Irancell sustainability 1402, Middle East Bank annual report 1401 | 4 | ~94,000 |

Not obtained: MCI board reports (Codal requires a CAPTCHA), the MCI human-capital
report (behind an e-mail form), Okala 1403 and two other reports (image-only PDFs),
two petrochemical reports (download failed), one bank report (too damaged after
extraction).

Kept: only signed, single-author texts. Interviews, speeches, panel write-ups,
reposts and texts signed by someone else were removed.

## Method
- **Seventeen surface features per text**: sentence length, paragraph length, commas, «که», connectives, questions, quotation marks, pronouns, word length, and more.
- **22 moves defined before testing**, each counted automatically across all writers. A move counted as a signature only if it was frequent in its writer (at least 30% of texts) and rare in the others.
- **Mode labels on 34 unseen texts**, read with names hidden and shuffled; then the four-axis labels on 42 texts.
- **Two blind tests with the user.** In the first, the user rated reconstructions and real texts. In the second, the user labelled 8 real texts and recognised the styles of 9 written pieces.

## Results that shaped the framework
- The first list of named styles mixed criteria and overlapped: 20 of 34 texts needed two or more labels. This led to the four axes.
- Surface features identify a writer only about half the time (balanced accuracy 51%, chance 12.5%). Style lives in moves and specificity more than in counts.
- Recipes anchored on the same writers produced near-identical numbers. This led to separating rhythm from recipe.
- On the purpose axis most columns are اقناع (26 of 42). Writers differ mainly on evidence and position.
- Structure depends on the text, not the writer.
- **User agreement on mode labels**: 5 of 8 with four options (chance 25%, p ≈ 3%). All three disagreements were texts that mixed two old modes.
- **Recognition**: 7 of 8 written pieces were recognised in their intended style (p < 0.1%).
- **Ratings**: a fact-dense control in the skill's old short-sentence style was rated 3/3. Generic, well-rhythmed reconstructions had been rated lower. This is the basis of the specificity rule.

- **style_check.py `--compare`** puts a real text in its own rhythm profile 51% of the time (top two: 70%; chance 14%). Profiles overlap because one writer's texts vary. Use it as a band check, not as a judge of quality or authorship.
- **Worked test**: a 250-word argument drafted for استدلال روزنامه‌ای needed three revisions to sit inside the band. The first was choppy (no long sentences, too many connectives). The second overcorrected (long paragraphs, too many «که»). The fourth passed every core feature, and `--compare` then ranked its intended profile first.

- **Storyline in consulting writing**: three Deloitte Insights articles (two research pieces on agentic AI, one scenario piece on generative AI) were read for structure only. All open situation → complication → question → answer; about nine body paragraphs in ten open with the claim; reading only the first sentences gives the argument; body paragraphs run three or four sentences. The scenario piece builds four scenarios on two uncertain, high-impact axes, gives each a name and story, impacts, present-day signals and strategies, and ends by asking which strategies hold in every scenario. McKinsey's site refused automated reading, so no McKinsey text was analysed.
- **Calibration tests with the user** (a strategy document for an AI company): conceptual analysis, journalistic argument, short news, explainer and witness narrative came through once rebuilt; the strategy samples failed until the storyline method, because their first sentences announced or teased instead of claiming.

## Known limits
- **One labeller** (the model) for axis labels, plus 8 texts labelled by the user. No full inter-annotator agreement.
- **Unreliable blinding**: topics and outlets gave authors away when labelling «blind».
- **Small samples**: some writers have under 10 texts. The خطابی profile rests on one writer.
- **Paragraph length is distorted in two sources**: Telegram one-line posts, and news republications, whose paragraphing may be the editor's.
- **Report PDFs** needed repair. Words reversed per line, a broken lam-alef and swapped ZWNJ were fixed. Paragraphs still out of order were dropped with a verb-final test, which biases report numbers slightly towards verb-final sentences.
- **The فشرده profile has no corpus anchor.**
