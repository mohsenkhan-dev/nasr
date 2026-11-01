# Document design: simple, designed, or on an existing template

A Persian document can be correct and still look like a printout of a chat.
This file decides how much design a deliverable gets, and how to give it
without inventing a look the user did not choose.

There are three levels. Pick one at the checkpoint and say which.

| Level | When | What you do |
|---|---|---|
| **۱. ساده** (default) | Notes, letters, internal memos, drafts, anything the user did not ask to be designed | The RTL mechanics only: Vazirmatn, black text, plain headings, plain tables (SKILL.md «Visual neutrality», docx-pdf.md §1–§6). No accent colour, no cover. |
| **۲. طراحی‌شده** | The user asks for a «سند زیبا»، «طراحی‌شده»، «حرفه‌ای»، a cover, or the document goes to a board, investors, clients or the public | Offer three or four design directions as rendered sample pages, let the user pick or mix, then build with the chosen tokens. Never ship one invented look silently. |
| **۳. روی قالب موجود** | The user hands over a designed DOCX/PPTX, a brand guide, or a previous version | Reuse that file's own paragraphs, tables and images as templates (docx-pdf.md §7.3). The design is the user's; do not restyle it. |

The simple level is the base of the other two: every RTL, font and pagination
rule still applies to a designed document. Design is added on top, never
instead.

## Level 2: design directions

1. Put the document's real material in a small JSON: title, subtitle, date,
   one heading and subheading, one real paragraph, one callout box, one real
   table, three or four headline numbers. Samples on lorem ipsum or on
   another topic do not let the user judge.
2. Render the directions:
   ```bash
   python scripts/design_samples.py --content <scratch>/sample.json --out <folder>/design.html
   python scripts/render_html.py <folder>/design.html <folder>/design.png --size 1000x2700
   ```
   The page shows each direction as a cover plus one content page. The four
   built-in directions differ on real axes: «رسمی و آرام» (navy, ruled
   headings), «مدرن و پررنگ» (gradient cover, Lalezar headings, soft
   callouts), «مینیمال تک‌رنگ» (black on white, outlines only) and «گزارش
   داده‌محور» (teal and amber, filled number tiles). A brand colour in the
   JSON (`"brand": {"accent": "#…"}`) overrides the accent of every direction.
3. Send the image (and the HTML) and ask which direction, or which mix
   («جلد ۲ با جدول ۴»). The user's answer is a design decision; record it with
   the term list.
4. Build with the chosen direction's tokens (`design.tokens.json`):
   docx-pdf.md §7.1 for Word, html-css.md for HTML/PDF, pptx.md for slides.

Directions are proposals, not a house style. Do not reuse the last user's
choice for a new user, and do not add a fifth direction by copying one of the
four with another colour: a direction must differ in typography, density or
layout, not only in hue.

## Figures, covers and number tiles

Text inside images must be Persian-shaped. Pillow without libraqm draws
disconnected letters, and libraqm is often missing on Windows. Write the
figure as HTML (bundled fonts through a file:// `@font-face`) and render it:

```bash
python scripts/render_html.py figure.html figure.png --size 1900x750
```

- Keep the original pixel size when you replace a figure inside a DOCX, so
  its frame in the document does not change.
- Take colours from the chosen direction or from the original design.
- Every number in a figure must match the text. When targets change, redraw
  the figures that show them (writing-workflow.md, R1).
- To change the text of a raster cover, erase the old text by fitting a
  smooth gradient to the surrounding background, then render the new title
  over the cleaned image as HTML. Check the result visually.

## Checks for a designed document

- Render the final DOCX/PDF to images and look at every page: covers, figure
  text, tables that break, headings at page bottoms.
- `verify_docx.py --expect-font Vazirmatn` warns about Lalezar when it is a
  chosen display font; that warning is expected.
- No colour or font outside the chosen tokens.
