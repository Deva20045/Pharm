#!/usr/bin/env python3
"""Rebuild the QUESTIONS / UNITS arrays of pulse-pharm-complete.html from data/chNN.json.

Unlike work/merge.py (which only appends chapters with a number greater than the
highest already embedded), this script regenerates the whole arrays from the data
files, so an already-embedded chapter can also be corrected/replaced.

- Questions/units are taken from every data/chNN.json in ascending chapter order.
- The CHAPTERS array (all 74 chapter titles/page starts) is preserved; only the
  live flag is set for chapters that have data files.
- data/chapters_live.json is rewritten.

Usage: python3 work/build.py [pulse-pharm-complete.html]
"""
import glob, json, os, re, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "pulse-pharm-complete.html"

def compact(o):
    return json.dumps(o, ensure_ascii=False, separators=(",", ":"))

def chapters():
    out = []
    for f in sorted(glob.glob("data/ch[0-9]*.json"), key=lambda p: int(re.search(r"ch(\d+)", p).group(1))):
        if not re.fullmatch(r"data/ch\d+\.json", f):
            continue                      # skip part files chNN_a.json
        ch = int(re.search(r"ch(\d+)", f).group(1))
        d = json.load(open(f, encoding="utf-8"))
        out.append((ch, d))
    return out

def splice(h, name, items):
    start_tok = f"const {name} = ["
    i = h.find(start_tok)
    assert i != -1, f"{name} anchor not found"
    j = h.find("];", i)
    assert j != -1, f"{name} close not found"
    body = ",".join(compact(x) for x in items)
    return h[:i + len(start_tok)] + body + h[j:]

chs = chapters()
assert chs, "no data/chNN.json found"
h = open(OUT, encoding="utf-8").read()

qs = [q for _, d in chs for q in d["questions"]]
us = [u for _, d in chs for u in d["units"]]
live = [ch for ch, _ in chs]

h = splice(h, "QUESTIONS", qs)
h = splice(h, "UNITS", us)

# ---- CHAPTERS live flags -------------------------------------------------
cs = h.find("const CHAPTERS = [")
ce = h.find("];", cs)
block = h[cs:ce]
def fix(m):
    n = int(m.group(1)); body = m.group(0)
    if n in live and "live:true" not in body:
        body = body[:-1] + ",live:true}"
    if n not in live and "live:true" in body:
        body = body.replace(",live:true", "")
    return body
block = re.sub(r"\{n:(\d+),[^{}]*\}", fix, block)
h = h[:cs] + block + h[ce:]

open(OUT, "w", encoding="utf-8").write(h)
json.dump(sorted(live), open("data/chapters_live.json", "w"))
print(f"written {OUT}")
for ch, d in chs:
    print(f"  ch{ch}: {len(d['questions'])} qs, {len(d['units'])} units")
print(f"total {len(qs)} questions, {len(us)} units, live={sorted(live)}")
