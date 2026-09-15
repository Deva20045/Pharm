# PULSE · Pharmacology — Marrow Edition 8 Companion

Single-file quiz app (`pulse-pharm-complete.html`) built chapter-by-chapter,
line-by-line from the Marrow Pharmacology E8 book (74 chapters total, book pages 1-293).
Same architecture and schema as [PULSE Ortho](https://github.com/Deva20045/ORTHO).

## Repo layout
```
pulse-pharm-complete.html   ← the deliverable app (open in any browser)
index.html                  ← redirects to the app (GitHub Pages landing)
uploads/                    ← source book PDF (scanned, no text layer)
data/chNN.json              ← per-chapter source data {questions, units}
data/chapters_live.json     ← list of chapters merged into the app
work/render.py              ← render book pages from source PDF to PNG
work/validate.py            ← schema validator for data/chNN.json
work/merge.py               ← merge data into the HTML (idempotent)
work/integrity.py           ← post-merge integrity check (node-backed)
PROGRESS.md                 ← memory / single source of truth for continuation
```

## ▶ Play
**https://deva20045.github.io/Pharm/** — opens the quiz directly (index.html redirects).
(Requires GitHub Pages: Settings → Pages → Deploy from a branch → main /(root).)

## Continue work (new session)
1. Say **"continue"** in the Arena session — the agent clones this repo
   (`git clone https://github.com/Deva20045/Pharm.git`) and reads PROGRESS.md.
2. Run the pipeline (render → transcribe → data/chNN.json → validate → merge →
   integrity → commit+push). The source PDF lives in `uploads/`.

## Schema contract (see PROGRESS.md for full detail)
- Question: `{id:"PHARM-C{ch}-{nnn}", sec, page, q, exp}` — exp ends `(Book pX)`.
  Optional `type`: `mcq` (default, CHOOSE), `fill` (FILL IN THE BLANK), `match` (MATCH).
  - mcq: `opts[4]`, `ans` 0-3 — four near-miss options of similar length, never dummy "Only X" pads.
  - fill: stem contains `____`, `blank` + optional `aliases[]` (typed, case-insensitive).
  - match: `left[]`/`right[]` (3-4 pairs); tap-to-pair.
- Unit: `{id:"PHARM-U{ch}-{n}", ch, n, title, sec:"<Heading> · p<page>", qs:[...], guide}`.
- Units cover every question exactly once, strictly in book order.
- PDF↔book map: **book page = pdf page − 5**.

## Checks before shipping a chapter
```bash
python3 work/validate.py data/chNN.json
python3 work/merge.py pulse-pharm-complete.html
python3 work/integrity.py
```
