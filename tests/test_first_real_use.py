"""Regressions from the first real use of nasr (a strategy document rewritten
and extended, 2026-11-01): each test pins one bug that reached the user."""
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from scripts.fa_lint import ISSUES, check_remaining
from scripts.persian_cleanup import ZWNJ, edit_persian, ezafe_style
from scripts.style_check import measure, strip_markup


class TestFirstRealUse(unittest.TestCase):
    def setUp(self):
        ISSUES.clear()

    def test_tanvin_whole_words_only(self):
        """«گاها» inside «آگاهانه» is not fake tanvin; the bare word still is."""
        check_remaining("این کار آگاهانه انجام شد.")
        self.assertFalse([i for i in ISSUES if i[0] == "fake-tanvin"])
        check_remaining("این کار گاها تکرار شد.")
        self.assertTrue([i for i in ISSUES if i[0] == "fake-tanvin"])

    def test_builder_placeholder_is_not_a_paragraph(self):
        """A whole-line placeholder like «[CAP تصویر ۱]» is markup, not an LTR paragraph."""
        check_remaining("متن فارسی این سند است و به فارسی ادامه دارد.\n[CAP تصویر ۱. دو بال]\n[TABLE okian]")
        self.assertFalse([i for i in ISSUES if i[0] == "bidi-start"])

    def test_ezafe_auto_keeps_ye_documents(self):
        ye = "سامانه" + ZWNJ + "ی"
        doc = f"{ye} اول و {ye} دوم و {ye} سوم در خانه" + ZWNJ + "ی ما."
        self.assertEqual(ezafe_style(doc), "ye")
        self.assertIn(ye, edit_persian(doc))
        self.assertIn("خانهٔ", edit_persian("خانه" + ZWNJ + "ی ما"))   # one stray ‌ی → default ٔ
        self.assertIn("خانهٔ", edit_persian(doc, ezafe="hamza"))

    def test_bullets_are_not_one_sentence_paragraphs(self):
        prose = ("گروه کلمه دو کسب‌وکار دارد که هر دو بر هوش مصنوعی بنا شده‌اند و در دو بازار کار می‌کنند. "
                 "هر کدام هدف و بودجه‌ی جدا دارد، چون قاعده‌ی رشد این دو بازار یکی نیست و این تفاوت مهم است.\n\n")
        bullets = "".join(f"- فاز {n} (سال {n}). این فاز با هدف‌های روشن و معیار تکمیل مشخص به پایان می‌رسد.\n"
                          for n in "۱۲۳")
        box = "> هدف فاز این است که تجربه‌ی پروژه‌ها به محصولات استاندارد و قابل تکرار تبدیل شود.\n"
        m = measure(strip_markup(prose * 3 + bullets + box))
        self.assertEqual(m["_one_sentence_paras"], 0)


if __name__ == "__main__":
    unittest.main()
