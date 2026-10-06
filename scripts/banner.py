"""Generate the profile banners (assets/banner-dark.svg, assets/banner-light.svg).

Same art direction as martinpoiroux.com: soot background, a single gold accent,
Cinzel for the name, Marcellus SC for labels, Sorts Mill Goudy for prose.
GitHub serves README images through a proxy that blocks external fonts, so the
fonts are subset to the glyphs actually used and embedded as base64 WOFF2.

Usage: python scripts/banner.py [path/to/site-perso]
"""
import base64
import io
import sys
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
SITE = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT.parent / "site-perso"
FONTS = SITE / "node_modules" / "@fontsource"

NAME = "MARTIN POIROUX"
KICKER = "SOFTWARE ENGINEER  ·  TOULOUSE"
LINES = [
    "Chess engines since 2019, and the tooling around them.",
    "Web applications end to end, from interface to production.",
    "C++  ·  C# / .NET  ·  TypeScript  ·  Rust  ·  Python",
    "Games, solvers, and the measurements behind them.",
]
SITE_LABEL = "MARTINPOIROUX.COM"

PALETTES = {
    "dark": dict(bg="#0c0a09", bg_hi="#151211", rule="#241f1b", gold="#c8a96a",
                 ink="#edebe7", ink_soft="#96928a", ink_faint="#8a857b"),
    "light": dict(bg="#f7f4ee", bg_hi="#ffffff", rule="#d3ccc0", gold="#7d5f1f",
                  ink="#14110f", ink_soft="#4f4a44", ink_faint="#4f4a44"),
}

W, H = 1200, 300
CYCLE = 4.0  # seconds each subtitle stays up


def font_face(family, path, text, style="normal", weight=400):
    font = TTFont(path)
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = ["kern", "liga"]
    sub = subset.Subsetter(opts)
    sub.populate(text=text)
    sub.subset(font)
    buf = io.BytesIO()
    font.flavor = "woff2"
    font.save(buf)
    b64 = base64.b64encode(buf.getvalue()).decode()
    return (f"@font-face{{font-family:'{family}';font-style:{style};font-weight:{weight};"
            f"src:url(data:font/woff2;base64,{b64}) format('woff2');}}")


def subtitle_css(n):
    total = CYCLE * n
    show = CYCLE / total * 100
    fade = 0.6 / total * 100
    keys = (f"@keyframes cycle{{0%{{opacity:0;transform:translateY(6px)}}"
            f"{fade:.2f}%{{opacity:1;transform:translateY(0)}}"
            f"{show - fade:.2f}%{{opacity:1;transform:translateY(0)}}"
            f"{show:.2f}%,100%{{opacity:0;transform:translateY(-6px)}}}}")
    rules = "".join(
        f".l{i}{{animation:cycle {total:.0f}s linear {2.0 + i * CYCLE:.1f}s infinite}}"
        for i in range(n))
    return keys + rules


def build(p, faces):
    cx = W / 2
    lines = "\n    ".join(
        f'<text class="sub l{i}" x="{cx}" y="222">{t}</text>' for i, t in enumerate(LINES))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Martin Poiroux, software engineer, Toulouse">
  <title>Martin Poiroux, software engineer, Toulouse</title>
  <defs>
    <radialGradient id="glow" cx="50%" cy="42%" r="65%">
      <stop offset="0" stop-color="{p['bg_hi']}"/>
      <stop offset="1" stop-color="{p['bg']}"/>
    </radialGradient>
    <linearGradient id="fadeL" x1="1" x2="0"><stop offset="0" stop-color="{p['gold']}"/><stop offset="1" stop-color="{p['gold']}" stop-opacity="0"/></linearGradient>
    <linearGradient id="fadeR" x1="0" x2="1"><stop offset="0" stop-color="{p['gold']}"/><stop offset="1" stop-color="{p['gold']}" stop-opacity="0"/></linearGradient>
  </defs>
  <style>
    {faces}
    .name{{font-family:'Cinzel',Georgia,serif;font-weight:600;font-size:66px;letter-spacing:9px;fill:{p['ink']};text-anchor:middle;opacity:0;animation:rise 1.2s ease-out .2s forwards}}
    .kicker{{font-family:'Marcellus SC',Georgia,serif;font-size:17px;letter-spacing:5px;fill:{p['gold']};text-anchor:middle;opacity:0;animation:rise 1s ease-out .9s forwards}}
    .sub{{font-family:'Sorts Mill Goudy',Georgia,serif;font-style:italic;font-size:25px;fill:{p['ink_soft']};text-anchor:middle;opacity:0}}
    .site{{font-family:'Marcellus SC',Georgia,serif;font-size:13px;letter-spacing:4px;fill:{p['ink_faint']};text-anchor:middle;opacity:0;animation:rise 1s ease-out 1.6s forwards}}
    .rule{{transform-box:fill-box;transform:scaleX(0);animation:draw 1.4s cubic-bezier(.2,.7,.2,1) .7s forwards}}
    .ruleL{{transform-origin:100% 50%}} .ruleR{{transform-origin:0% 50%}}
    .diamond{{transform-box:fill-box;transform-origin:50% 50%;opacity:0;animation:gem 1s ease-out .6s forwards, shine 6s ease-in-out 2s infinite}}
    @keyframes rise{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:translateY(0)}}}}
    @keyframes draw{{to{{transform:scaleX(1)}}}}
    @keyframes gem{{from{{opacity:0;transform:rotate(45deg) scale(.2)}}to{{opacity:1;transform:rotate(45deg) scale(1)}}}}
    @keyframes shine{{0%,100%{{fill-opacity:1}}50%{{fill-opacity:.35}}}}
    {subtitle_css(len(LINES))}
  </style>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="url(#glow)" stroke="{p['rule']}"/>
  <rect x="14.5" y="14.5" width="{W - 29}" height="{H - 29}" rx="8" fill="none" stroke="{p['rule']}" stroke-opacity=".6"/>
  <text class="kicker" x="{cx}" y="78">{KICKER}</text>
  <text class="name" x="{cx}" y="150">{NAME}</text>
  <rect class="rule ruleL" x="{cx - 320}" y="178.5" width="300" height="1.5" fill="url(#fadeL)"/>
  <rect class="rule ruleR" x="{cx + 20}" y="178.5" width="300" height="1.5" fill="url(#fadeR)"/>
  <rect class="diamond" x="{cx - 5}" y="174" width="10" height="10" fill="{p['gold']}"/>
  <g>
    {lines}
  </g>
  <text class="site" x="{cx}" y="268">{SITE_LABEL}</text>
</svg>
"""


def main():
    faces = "".join([
        font_face("Cinzel", FONTS / "cinzel/files/cinzel-latin-600-normal.woff2", NAME, weight=600),
        font_face("Marcellus SC", FONTS / "marcellus-sc/files/marcellus-sc-latin-400-normal.woff2",
                  KICKER + SITE_LABEL),
        font_face("Sorts Mill Goudy", FONTS / "sorts-mill-goudy/files/sorts-mill-goudy-latin-400-italic.woff2",
                  "".join(LINES), style="italic"),
    ])
    out = ROOT / "assets"
    out.mkdir(exist_ok=True)
    for name, palette in PALETTES.items():
        path = out / f"banner-{name}.svg"
        path.write_text(build(palette, faces), encoding="utf-8")
        print(path, path.stat().st_size // 1024, "KB")
    # Section divider: one mid-tone gold that reads on both GitHub themes.
    (out / "divider.svg").write_text(f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="24" viewBox="0 0 {W} 24" role="presentation">
  <defs>
    <linearGradient id="l" x1="1" x2="0"><stop offset="0" stop-color="#a8894f"/><stop offset="1" stop-color="#a8894f" stop-opacity="0"/></linearGradient>
    <linearGradient id="r" x1="0" x2="1"><stop offset="0" stop-color="#a8894f"/><stop offset="1" stop-color="#a8894f" stop-opacity="0"/></linearGradient>
  </defs>
  <rect x="{W / 2 - 380}" y="11.5" width="360" height="1" fill="url(#l)"/>
  <rect x="{W / 2 + 20}" y="11.5" width="360" height="1" fill="url(#r)"/>
  <rect x="{W / 2 - 4}" y="8" width="8" height="8" fill="#a8894f" transform="rotate(45 {W / 2} 12)"/>
</svg>
""", encoding="utf-8")


if __name__ == "__main__":
    main()
