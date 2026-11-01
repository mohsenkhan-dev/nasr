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
   (`scripts/install_fonts.sh`), then
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
Always finish with `scripts/verify_pdf.py out.pdf --expect-font Vazirmatn`.

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
