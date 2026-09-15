#!/usr/bin/env python3
"""Splice CHOOSE / FILL / MATCH quiz runtime into pulse-pharm-complete.html."""
from pathlib import Path

HTML = Path("pulse-pharm-complete.html")
JS = Path("work/quiz_runtime.js")
h = HTML.read_text(encoding="utf-8")
js = JS.read_text(encoding="utf-8").strip() + "\n"

CSS = """
  .qtag{display:inline-flex;align-items:center;flex-wrap:wrap;gap:6px;font-size:11.5px;
    color:var(--teal);margin-top:8px;border:0;padding:0;background:transparent;border-radius:0;}
  .qsec{display:inline-block;border:1px solid #5fd0b555;border-radius:999px;padding:3px 10px;}
  .qtype{display:inline-block;font-size:10.5px;letter-spacing:1.5px;font-weight:800;
    border-radius:999px;padding:3px 9px;}
  .qtype.mcq{color:var(--teal);border:1px solid #5fd0b555;}
  .qtype.fill{color:var(--gold);border:1px solid #c99a4b66;}
  .qtype.match{color:var(--pink);border:1px solid #e0607e66;}
  .blank{display:inline-block;min-width:4.8em;border-bottom:3px solid var(--pink);
    color:var(--pink);font-weight:800;padding:0 6px;margin:0 2px;}
  .fillin{display:block;width:100%;margin:4px 0 12px;padding:16px;font-size:18px;
    color:var(--txt);background:var(--card);border:1.5px solid var(--line);border-radius:16px;outline:none;}
  .fillin:focus{border-color:var(--pink);}
  .fillin.correct{border-color:var(--good);background:#3ddc841c;}
  .fillin.wrong{border-color:var(--bad);background:#ff5d6c1c;}
  .mrow{display:flex;gap:8px;align-items:stretch;margin:8px 0;}
  .mleft{flex:1;padding:12px 14px;background:var(--card);border:1.5px solid var(--line);
    border-radius:14px;font-size:14.5px;font-weight:700;display:flex;align-items:center;line-height:1.35;}
  .mslot{flex:1;padding:12px 14px;background:var(--card2);border:1.5px dashed var(--line);
    border-radius:14px;font-size:14px;color:var(--mut);cursor:pointer;text-align:left;line-height:1.35;}
  .mslot.filled{border-style:solid;color:var(--txt);font-weight:700;}
  .mslot.sel{border-color:var(--pink);box-shadow:0 0 0 3px #e0607e33;}
  .mslot.correct{border-color:var(--good);background:#3ddc841c;color:var(--txt);}
  .mslot.wrong{border-color:var(--bad);background:#ff5d6c1c;}
  .mbank{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 8px;}
  .chip{padding:10px 14px;background:var(--card);border:1.5px solid var(--line);
    border-radius:999px;font-size:13.5px;color:var(--txt);cursor:pointer;font-weight:600;}
  .chip:active{border-color:var(--pink);}
  .chip.used{opacity:.35;pointer-events:none;}
  .chip:disabled{cursor:default;}
"""

# CSS: keep original .qtag then override with new rules before </style>
old_qtag = """  .qtag{display:inline-block; font-size:11.5px; color:var(--teal); border:1px solid #5fd0b555;
    border-radius:999px; padding:3px 10px; margin-top:8px;}"""
if old_qtag not in h:
    raise SystemExit("qtag CSS not found")
if ".qtype.mcq" not in h:
    h = h.replace(old_qtag, old_qtag + "\n" + CSS, 1)

old_foot = "question order follows the book line-by-line<br>options shuffled every run · progress saved on this device"
new_foot = "question order follows the book line-by-line<br>CHOOSE · FILL · MATCH · options shuffled · progress saved on this device"
h = h.replace(old_foot, new_foot)

start = h.find("let order=[],idx=0")
end = h.rfind("render();\n</script>")
if start < 0 or end < 0:
    raise SystemExit(f"JS anchors missing start={start} end={end}")
h = h[:start] + js + h[end + len("render();\n"):]

HTML.write_text(h, encoding="utf-8")
print("patched", HTML, "bytes", HTML.stat().st_size)
