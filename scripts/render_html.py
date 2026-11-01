#!/usr/bin/env python3
"""
render_html.py — render an HTML file to PNG or PDF with a headless Chromium
browser (Chrome, Edge or Chromium), found automatically.

Why: Persian text in images needs real shaping. PIL without libraqm draws
disconnected, left-to-right letters, and there is often no raqm on Windows.
A browser shapes Persian correctly, so cover pages, figures, number tiles and
design samples are written as HTML and rendered here (format-skills-fa.md §5).

Usage:
  python render_html.py page.html out.png --size 1900x750
  python render_html.py page.html out.pdf            # print to PDF (A4)
  python render_html.py page.html out.png --size 1100x3000 --wait 3000

Fonts: reference the bundled TTFs with a file:// @font-face, or install them.
Python 3.8+, standard library only.
"""
import argparse, os, shutil, subprocess, sys, tempfile, time
from pathlib import Path

CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
]
NAMES = ["chromium", "chromium-browser", "google-chrome", "google-chrome-stable", "chrome", "msedge", "microsoft-edge"]


def find_browser():
    env = os.environ.get("NASR_BROWSER")
    if env and Path(env).exists():
        return env
    for p in CANDIDATES:
        if Path(p).exists():
            return p
    for n in NAMES:
        p = shutil.which(n)
        if p:
            return p
    sys.exit("no Chromium-based browser found; set NASR_BROWSER to its path")


def main():
    ap = argparse.ArgumentParser(description="Render HTML to PNG or PDF with headless Chromium.")
    ap.add_argument("html"); ap.add_argument("out")
    ap.add_argument("--size", default="1900x1000", help="viewport WIDTHxHEIGHT for PNG")
    ap.add_argument("--wait", type=int, default=2000, help="virtual time budget in ms (fonts, scripts)")
    a = ap.parse_args()
    src, out = Path(a.html).resolve(), Path(a.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    w, h = a.size.lower().split("x")
    if out.exists():
        out.unlink()
    prof = tempfile.mkdtemp(prefix="nasr-render-")
    cmd = [find_browser(), "--headless=new", "--disable-gpu", "--hide-scrollbars",
           "--force-device-scale-factor=1", f"--user-data-dir={prof}", f"--virtual-time-budget={a.wait}"]
    if out.suffix.lower() == ".pdf":
        cmd += ["--no-pdf-header-footer", f"--print-to-pdf={out}"]
    else:
        cmd += [f"--window-size={w},{h}", f"--screenshot={out}"]
    subprocess.run(cmd + [src.as_uri()], check=False, capture_output=True, timeout=120)
    # Edge's launcher can return before the headless child has written the file.
    for _ in range(60):
        if out.exists() and out.stat().st_size > 0:
            break
        time.sleep(0.5)
    shutil.rmtree(prof, ignore_errors=True)
    if not out.exists():
        sys.exit(f"rendering failed: {out} was not written")
    print(f"wrote {out}")


if __name__ == "__main__":
    for _stream in (sys.stdout, sys.stderr):
        try:
            _stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    main()
