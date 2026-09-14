# PULSE Pharm — progress tracker (single source of truth)

## Goal
Build `pulse-pharm-complete.html` (quiz app, Marrow Pharmacology E8) line-by-line from the
scanned book PDF until ALL 74 chapters are live. User demands: no quality compromise,
line-by-line questions, first line → last line, strict book order, identical style/schema
to PULSE Ortho (https://github.com/Deva20045/ORTHO). Every explanation ends `(Book pX)`.
No generic/page-meta questions; test understanding, recall, clinical application,
comparisons, values, exceptions; convert every table/diagram/flowchart into questions.

## Sources
- `uploads/Pharmacology Marrow E8 (1).pdf` = 298 pdf pages = book pages 1-293 (book ends p293).
- **PAGE-OFFSET FORMULA: `book page = pdf page − 5`** (pdf 1 = cover, pdf 2-5 = Contents,
  pdf 6 = book p1; verified p1 "INTRODUCTION TO PHARMACOKINETICS…" on pdf 6,
  p2 "PHARMACOKINETICS: ABSORPTION - PART 1" on pdf 7, p293 "Miscellaneous Drugs" on pdf 298).
- Scans have NO text layer → read pages as images (render to work/pages/bNNN.png via
  `work/render.py`, then read_file the PNGs; handwritten notes → read carefully at ≥100 dpi,
  re-inspect the page if any word is unclear; never fabricate).

## Schema (must match exactly — same as ORTHO, PHARM prefix)
- Question: {id:"PHARM-C{ch}-{nnn}" sequential per chapter from 001, sec, page(book),
  q, opts[4], ans(idx 0-3), exp ends "(Book pX)"}
- Unit: {id:"PHARM-U{ch}-{n}" sequential per chapter from 1, ch, n, title,
  sec:"<Heading> · p<page>", qs:[ids contiguous & ordered], guide: vivid 2-3 sentence prose}
- Units must cover every question exactly once, in order.
- Deliverable format inside HTML: `const QUESTIONS = [{...}]`, `const UNITS = [{...}]`
  (compact JSON, natural key order), `const CHAPTERS = [{n,t,p,live:true}]` (live only when built).

## Chapter page map (book pages) — 74 chapters, all LISTED in app from day one ("Soon" until live)
### General Pharmacology
1: p1 DONE (22 qs, 3 units) | 2: 2-4 DONE (85 qs, 9 units) | 3: 5-8 DONE (93 qs, 11 units) |
4: 9-10 DONE (78 qs, 10 units) | 5: 11-14 DONE (80 qs, 11 units) | 6: 15-17 DONE (69 qs, 11 units) |
7: 18-19 DONE (60 qs, 6 units) | 8: 20-24 NEXT | 9: 25-28 | 10: 29-32 | 11: 33-36 |
### Autonomic Nervous System
12: 37-41 | 13: 42-47 | 14: 48-51 | 15: 52-55 | 16: 56-57 | 17: 58-62 | 18: 63-68
### Cardiovascular System
19: 69-73 | 20: 74-76 | 21: 77-82 | 22: 83-88 | 23: 89-90 | 24: 91-93 | 25: 94-100
### Renal System
26: 101-105 | 27: 106-112
### Central and Peripheral Nervous System
28: 113-117 | 29: 118-119 | 30: 120-122 | 31: 123-126 | 32: 127-130 | 33: 131-133 |
34: 134-140 | 35: 141-144 | 36: 145-149 | 37: 150-152
### Antimicrobials
38: 153-154 | 39: 155-158 | 40: 159-163 | 41: 164-166 | 42: 167-170 | 43: 171-173 |
44: 174-179 | 45: 180-183 | 46: 184-188 | 47: 189-192 | 48: 193-198 | 49: 199-204 | 50: 205-206
### Endocrine System
51: 207-210 | 52: 211-214 | 53: 215-217 | 54: 218-220 | 55: 221-223 | 56: 224-226 | 57: 227-229
### Autacoids
58: 230-232 | 59: 233-236 | 60: 237-241 | 61: 242-243 | 62: 244-246
### Hematology
63: 247-250 | 64: 251-255
### Respiratory System
65: 256-258 | 66: 259-260
### Gastrointestinal Drugs
67: 261-265 | 68: 266-268 | 69: 269-271
### Immunomodulators
70: 272-275
### Anti-neoplastic Agents
71: 276-281 | 72: 282-285 | 73: 286-289 | 74: 290-293

## Pipeline per chapter
1. `python3 work/render.py <book_a> <book_b> 100`  (renders work/pages/bNNN.png from uploads/ PDF)
2. read_file the pages (batches), transcribe every line mentally; re-render at higher dpi if unsure
3. write data/chNN_a.json / _b.json / _c.json (last holds "units"), assemble to data/chNN.json
4. `python3 work/validate.py data/chNN.json`
5. `python3 work/build.py pulse-pharm-complete.html`  (DETERMINISTIC rebuild of QUESTIONS/UNITS
   from every data/chNN.json in chapter order; also updates live flags + data/chapters_live.json.
   Use this instead of merge.py once a chapter is already embedded — merge.py only appends
   chapters above the highest embedded one, so it cannot replace an existing chapter.)
6. `python3 work/integrity.py` + extract inline JS → `node --check`
7. commit & push, present_file pulse-pharm-complete.html

## How to CONTINUE in a new session (user says "continue")
1. Clone the repo: `git clone https://github.com/Deva20045/Pharm.git`
2. Read this PROGRESS.md — it is the single source of truth.
3. Find NEXT chapter below, run the pipeline above (source PDF is IN the repo at uploads/).
4. Commit+push after each chapter so progress is never lost.

## Status  (last updated: 2026-09-14, session 3)
- DONE: repo skeleton (all 74 chapters listed, index.html redirect, work/ pipeline, this tracker).
- DONE: **ch1** Introduction to Pharmacokinetics and Pharmacodynamics (p1) - 22 qs, 3 units.
- DONE: **ch2** Absorption - Part 1 (p2-4) - 85 qs, 9 units
  (4 transport mechanisms + carrier-mediated/ATP braces, P-gp/MDR1 ABC pump, gut+hepatic efflux &
  first pass, digoxin dosing by efflux, BBB/loperamide, placenta, hepatocytes, Pgp resistance,
  substrates/inducers/inhibitors, blockade table, passive diffusion + charged membrane proteins).
- DONE: **ch3** Absorption - Part 2 (p5-8) - 93 qs, 11 units
  (criteria table + LUNA/WIPE, unionization, short bowel, ion trapping with bicarbonate/ammonium
  chloride, Henderson-Hasselbalch incl. pKa 4 in pH 2 -> 99% unionised, IR/SR/CR curves,
  delayed & enteric release, bioavailability f + AUC ratio, route table, Cmax/Tmax,
  bioequivalence/ANDA +/-20%).
- DONE: **ch4** Distribution (p9-10) - 78 qs, 10 units
  (AVd definition, D/C0 formula, loading dose D = AVd x CT/f, fat/pKa/albumin factors, digoxin &
  lean body mass, dialysis ineffective at high vd, BADDOC + antidotes, albumin vs alpha-1 acid
  glycoprotein, hypoalbuminaemia and inflammation).
- DONE: **ch5** Metabolism (p11-14) - 80 qs, 11 units
  (phase I/II flowchart, prodrugs, ORCHAD, phase II conjugates, CYP nomenclature, CYP1A2/2B6/
  2C9/2C19/2D6/2E1/3A4, omeprazole-clopidogrel, tamoxifen, NAPQI in chronic alcohol, Crigler
  Najjar, estrogen enterohepatic circulation & OCP failure, HIPS Dance, inducer/inhibitor table,
  OCP failure/theophylline arrhythmia/statin toxicity).
- DONE: **ch6** Excretion (p15-17) - 69 qs, 11 units
  (filtration 20% vs secretion 80%, -ve basement membrane, saliva/sweat, GFR, RDE = PC x CL,
  infusion phases I/II/III, 4-5 T1/2 to steady state, maintenance dose PC x CL x Time/f,
  T1/2 = 0.693 x vd/CL, Kel, zero vs first order table, pseudozero order, example list).
- DONE (this session): **ch7** Pharmacodynamics: Potency, Efficacy and Dose Response Curve
  (p18-19) - 60 qs, 6 units (affinity/efficacy/potency, quantal DRC ED50/TD50/LD50,
  TI = TD50/ED50 humans and LD50/ED50 animals, lithium window 0.6-1.5 meq/L, graded DRC
  efficacy B>A>C and potency PA>PB>PC, affinity only between parallel lines, full/partial/
  antagonist/inverse agonist + intrinsic efficacy +1 / 1-0 / 0 / -1, curve A/B/C/D, note that
  antagonists are m/c used).
- **TOTAL LIVE NOW: 487 questions, 61 units, chapters 1-7.**
- SESSION 3 NOTES (merge of the two parallel workstreams + verified corrections):
  * A failed earlier session of this same branch had already pushed ch2-ch6; those files were
    kept as the base (they carry more questions), and this session's audited additions were
    merged into them (7 ch2, 2 ch3, 1 ch6 questions that were not covered: carrier-mediated/
    ATP wording, loperamide GIT action, MDR1 site matching, tumour-cell resistance mechanism,
    inducer -> failure, inducers = enzyme inducers, lipid-solubility determinant, LUNA meaning,
    two successive peaks = IR, steady state depends on vd).
  * TWO MISREADS IN THE EARLIER FILES WERE CAUGHT AND FIXED after re-reading the scan at
    420-500 dpi: (1) the ch3 mnemonic is **LUNA** (not "LUNJA"); (2) the generic-drug approval
    criterion is **±20%** (not "±30%").
  * work/build.py added for deterministic rebuilds; run it instead of merge.py whenever a chapter
    that is already embedded has changed.
- NEXT: **ch8 "Pharmacodynamics: Drug Receptors and Interactions"** (book p20-24 = pdf p25-29),
  then ch9 (25-28), ch10 (29-32), ch11 (33-36) -> General Pharmacology complete.
- LIVE LINK: https://deva20045.github.io/Pharm/ (index.html redirects -> pulse-pharm-complete.html).
  GitHub Pages: enable once via Repo -> Settings -> Pages -> "Deploy from a branch" -> main /(root).
- Deliverable file: `pulse-pharm-complete.html` (repo root).
- GitHub repo: https://github.com/Deva20045/Pharm
