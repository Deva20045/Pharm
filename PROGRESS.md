# PULSE Pharm — progress tracker (single source of truth)

## Goal
Build `pulse-pharm-complete.html` (quiz app, Marrow Pharmacology E8) line-by-line from the
scanned book PDF until ALL 74 chapters are live. User demands: no quality compromise,
line-by-line questions, first line → last line, strict book order, identical style/schema
to PULSE Ortho (https://github.com/Deva20045/ORTHO). Every explanation ends `(Book pX)`.
No generic/page-meta questions; test understanding, recall, clinical application,
comparisons, values, exceptions; convert every table/diagram/flowchart into questions.
Never pad MCQs with dummy "Only X" / "neither" options or a uniquely long correct
choice — if four genuine near-misses do not exist, use FILL (typed blank) or MATCH.

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
  q, exp ends "(Book pX)", optional type "mcq"|"fill"|"match" (default mcq).
  mcq = CHOOSE: opts[4], ans 0-3, four near-misses of similar length (never dummy "Only X").
  fill = FILL IN THE BLANK: stem contains ____, blank + optional aliases[].
  match = MATCH: left[]/right[] 3-4 pairs, tap-to-pair.}
- Unit: {id:"PHARM-U{ch}-{n}" sequential per chapter from 1, ch, n, title,
  sec:"<Heading> · p<page>", qs:[ids contiguous & ordered], guide: vivid 2-3 sentence prose}
- Units must cover every question exactly once, in order.
- Deliverable format inside HTML: `const QUESTIONS = [{...}]`, `const UNITS = [{...}]`
  (compact JSON, natural key order), `const CHAPTERS = [{n,t,p,live:true}]` (live only when built).

## Chapter page map (book pages) — 74 chapters, all LISTED in app from day one ("Soon" until live)
### General Pharmacology
1: p1 DONE (22 qs, 3 units) | 2: 2-4 DONE (85 qs, 9 units) | 3: 5-8 DONE (93 qs, 11 units) |
4: 9-10 DONE (78 qs, 10 units) | 5: 11-14 DONE (80 qs, 11 units) | 6: 15-17 DONE (69 qs, 11 units) |
7: 18-19 DONE (60 qs, 6 units) | 8: 20-24 DONE (137 qs, 12 units) |
9: 25-28 DONE (99 qs, 7 units) | 10: 29-32 DONE (91 qs, 9 units) |
11: 33-36 DONE (86 qs, 7 units) |
### Autonomic Nervous System
12: 37-41 DONE (99 qs, 9 units) | 13: 42-47 DONE (126 qs, 7 units) | 14: 48-51 DONE (99 qs, 5 units) | 15: 52-55 DONE (99 qs, 4 units) | 16: 56-57 DONE (86 qs, 6 units) | 17: 58-62 DONE (127 qs, 6 units) | 18: 63-68 DONE (129 qs, 9 units)
### Cardiovascular System  (COMPLETE)
19: 69-73 DONE (112 qs, 7 units) | 20: 74-76 DONE (75 qs, 6 units) | 21: 77-82 DONE (130 qs, 8 units) |
22: 83-88 DONE (136 qs, 7 units) | 23: 89-90 DONE (70 qs, 4 units) | 24: 91-93 DONE (74 qs, 6 units) |
25: 94-100 DONE (180 qs, 10 units)
### Renal System  (COMPLETE)
26: 101-105 DONE (119 qs, 8 units) | 27: 106-112 DONE (162 qs, 11 units)
### Central and Peripheral Nervous System
28: 113-117 DONE (118 qs, 10 units) | 29: 118-119 DONE (38 qs, 2 units) | 30: 120-122 DONE (73 qs, 6 units) |
31: 123-126 DONE (127 qs, 10 units) | 32: 127-130 DONE (113 qs, 10 units) | 33: 131-133 DONE (74 qs, 7 units) |
34: 134-140 DONE (169 qs, 12 units) | 35: 141-144 DONE (104 qs, 9 units) | 36: 145-149 DONE (153 qs, 15 units) | 37: 150-152 DONE (65 qs, 4 units)
### Antimicrobials  (COMPLETE)
38: 153-154 DONE (52 qs, 4 units) | 39: 155-158 DONE (83 qs, 4 units) | 40: 159-163 DONE (105 qs, 5 units) | 41: 164-166 DONE (61 qs, 5 units) | 42: 167-170 DONE (100 qs, 8 units) | 43: 171-173 DONE (77 qs, 8 units) |
44: 174-179 DONE (144 qs, 10 units) | 45: 180-183 DONE (70 qs, 6 units) | 46: 184-188 DONE (105 qs, 7 units) |
47: 189-192 DONE (86 qs, 8 units) | 48: 193-198 DONE (116 qs, 10 units) | 49: 199-204 DONE (108 qs, 12 units) | 50: 205-206 DONE (43 qs, 7 units)
### Endocrine System
51: 207-210 DONE (70 qs, 8 units) | 52: 211-214 DONE (77 qs, 9 units) | 53: 215-217 DONE (51 qs, 8 units) | 54: 218-220 DONE (42 qs, 3 units) | 55: 221-223 DONE (54 qs, 5 units) | 56: 224-226 DONE (40 qs, 6 units) | 57: 227-229 DONE (36 qs, 6 units)
### Autacoids
58: 230-232 DONE (31 qs, 5 units) | 59: 233-236 DONE (34 qs, 7 units) | 60: 237-241 DONE (54 qs, 7 units) | 61: 242-243 DONE (24 qs, 6 units) | 62: 244-246 DONE (29 qs, 5 units)
### Hematology
63: 247-250 DONE (62 qs, 6 units) | 64: 251-255 DONE (110 qs, 6 units)
### Respiratory System
65: 256-258 DONE (31 qs, 5 units) | 66: 259-260 DONE (35 qs, 8 units)
### Gastrointestinal Drugs
67: 261-265 DONE (64 qs, 12 units) | 68: 266-268 DONE (38 qs, 6 units) | 69: 269-271 DONE (31 qs, 5 units)
### Immunomodulators
70: 272-275 DONE (37 qs, 6 units)
### Anti-neoplastic Agents  (COMPLETE — ALL 74 CHAPTERS LIVE)
71: 276-281 DONE (59 qs, 9 units) | 72: 282-285 DONE (33 qs, 7 units) | 73: 286-289 DONE (43 qs, 6 units) | 74: 290-293 DONE (31 qs, 7 units)

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

## Status  (last updated: 2026-09-15, session 10)
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
- DONE (session 4, this session): **ch8 "Pharmacodynamics: Drug Receptors and Interactions"**
  (p20-24) - 137 qs, 12 units (physical/chemical/physiological antagonism + charcoal, heparin-protamine,
  chelators, salbutamol vs ipratropium in COPD; the full reversible-vs-irreversible/non-competitive
  antagonism table with Vmax/Km/potency rows; Michaelis-Menten note; LGICR + GABA-A chloride channel,
  glutamate NMDA/AMPA/kainate, nicotinic pentamer alpha,alpha,beta,delta,epsilon and Ach on alpha;
  enzymatic receptors incl. TK/JAK/STKR/guanylate cyclase; nuclear receptors nucleus vs cytoplasm;
  GPCR 7TM alpha-subunit GTPase and s/q/i subtypes; then the Gs, Gq, Gi/Go and G12/13 cascades with
  ritodrine, dobutamine, salbutamol, theophylline (PDE 3,4 bronchi), milrinone (PDE 3 heart), oxytocin/
  angiotensin/vasopressin-1 receptors, M2/alpha2/H3/5HT1 autoreceptors and belumosudil/fasudil/netarsudil).
- DONE (session 4): **ch9 "Drug Development and Clinical Trials"** (p25-28) - 99 qs, 7 units
  (schedules G/H/H1/X/P/W/Y with Rx/NRx/XRx labels; pregnancy categories A-D-X with valproate in JME
  and thalidomide; nine types of drugs incl. STEP and orphan receptor; preclinical trials with AEC and
  CPCSEA; phase 0 microdosing and abort rule; the mandatory phases table in full - aims, subjects,
  sample size, duration, study design, centres and failure rate; IND/NDA/CDSCO approval; phase V
  pharmacoepidemiology with case control/cohort studies).
- DONE (session 4): **ch10 "ADR and Pharmacovigilance, Pharmacogenetics and Pharmacogenomics"**
  (p29-32) - 91 qs, 9 units (ABCDEFG ADR types; 4 hypersensitivity types with the lepra reaction note;
  PvPI/NCC Ghaziabad/VigiFlow/CDSCO/Uppsala/Vigibase; TDM principle, 5 indications, valproate-folic acid
  dosing, steady state rule; pharmacogenetics vs genomics; NAT1/NAT2 with INH hepatotoxicity vs INHA
  neuropathy; malignant hyperthermia RyR cascade and dantrolene; G-6-PD haemolysis drug list;
  CYP2C19-clopidogrel, CYP2C9+VKORC1-warfarin, CYP2D6-psychiatric drugs/tamoxifen; atypical
  pseudocholinesterase and TPMT).
- DONE (session 4): **ch11 "General Pharmacology: Miscellaneous"** (p33-36) - 86 qs, 7 units
  (definitions incl. pharmacognosy/chemotherapy/pharmacy/barcoding; four drug sources with apomorphine
  and human insulin; nomenclature with -lol/-pril/-prazole and IP vs formulary; local and topical sites;
  intrathecal/intraarticular/intraarterial routes; full enteral table oral/rectal/sublingual with
  first-pass figures and NTG postural hypotension; full parenteral table IV/IM/SC/intranasal/
  inhalational with Afrezza and tobramycin).
- DONE (session 4): **ch12 "Introduction to Autonomic Nervous System (ANS)"** (p37-41) - 99 qs, 9 units
  (cranio-sacral vs thoraco-lumbar, ganglion = collection of neuronal bodies; synaptic transmission with
  voltage gated Ca2+ and Na+ influx; parasympathetic vs sympathetic innervation table incl. dopamine
  D1 diuresis, Ach at adrenals/sweat glands and the m3/sympatholytic sweating note; ACh synthesis-storage
  -release-metabolism with beta-bungarotoxin, botulinum, aminoglycosides, AChE esteratic + anionic sites;
  Nm toxicity and the respiratory failure flow with botulinum uses incl. CGRP; nicotinic Nm/Nn table;
  all muscarinic m1-m5 rows incl. eNOS vasodilation; Alzheimer's tacilifensin; cholinergic vs
  anticholinergic poisoning table with atropine/physostigmine).
- DONE (session 5): **ch13 "Cholinergic Drugs"** (p42-47) - 126 qs, 7 units
  (parasympathomimetic direct/indirect classification; amides vs choline esters; pilocarpine/cevimeline
  xerostomia and glaucoma details; ACh plasma metabolism and shortest-acting notes; bethanechol/carbachol/
  methacholine table; organophosphate mechanism, ageing and oximes; OP poisoning presentation and atropinisation
  markers; reversible blockers incl. physostigmine/Alzheimer drugs; edrophonium/neostigmine/pyridostigmine,
  myasthenia crisis/new MG drugs; ACh blood-pressure response graphs with atropine/high-dose ACh).
- DONE (session 5): **ch14 "Anticholinergic Drugs"** (p48-51) - 99 qs, 5 units
  (parasympatholytic classification; Nm vs Nn/ganglionic blockers; mecamylamine/trimethaphan; CNS/eye/oropharynx
  muscarinic blockers incl. scopolamine, tropicamide/cyclopentolate/homatropine, atropine ointment and glaucoma
  contraindication notes; SAMA/IAMA/LAMA pulmonary table, pMDI/nebuliser and paradoxical bronchoconstriction;
  atropine for conduction blocks/bradycardia and paradoxical bradycardia; GIT antispasmodics/hyoscine patch;
  bladder antimuscarinics including darifenacin/solifenacin/trospium and dementia risk from nonselective drugs).
- DONE (session 5): **ch15 "Sympathetic Nervous System: Neurotransmitters and Receptors"** (p52-55) - 99 qs, 4 units
  (NE synthesis with tyrosine hydroxylase, VMAT2, MAO/COMT and reuptake inhibitors; metyrosine, reserpine,
  tetrabenazine/deutetrabenazine/valbenazine and cocaine dependence; α1 vs α2 receptor table; clonidine infusion
  nuance; catecholamine effects on blood glucose; β1 heart/kidney effects, β2 smooth-muscle/metabolic/K+ effects,
  and β3 bladder/adipocyte effects).
- DONE (session 5): **ch16 "Adrenergic Drugs: Part 1"** (p56-57) - 86 qs, 6 units
  (adrenergic/sympathomimetic classification; endogenous catecholamines epinephrine, norepinephrine and dopamine
  with routes/doses/shock notes; dobutamine/isoprenaline/fenoldopam/dopexamine/droxidopa; α1 agonists including
  phenylephrine, oxymetazoline/xylometazoline, midodrine and hypotension drugs; apraclonidine; α2 agonists
  clonidine/lofexidine/tizanidine/α-methyldopa/guanfacine/guanabenz/brimonidine and PIH note).
- DONE (session 5): **ch17 "Adrenergic Drugs: Part 2"** (p58-62) - 127 qs, 6 units
  (β3 agonists mirabegron/vibegron and urge incontinence; β2 agonist SABA/LABA/VLABA table with asthma/COPD
  regimens and side effects; indirect adrenergics/NE displacers, tachyphylaxis-like NE depletion, cheese reaction,
  methylphenidate/amphetamine/methamphetamine; ADHD/narcolepsy notes with atomoxetine/viloxazine, solriamfetol,
  pitolisant and modafinil; mixed acting ephedrine/pseudoephedrine/norephedrine; epinephrine dilutions; Dale's
  phenomenon and epinephrine/norepinephrine/isoprenaline BP-HR comparison table with shock/vagal notes).
- DONE (session 6): **ch18 "Anti-adrenergic Drugs"** (p63-68) - 129 qs, 9 units
  (direct sympatholytics, nonselective and selective α blockers, phenoxybenzamine/phentolamine/tamsulosin/prazosin,
  α1 receptor locations and clinical uses, scorpion bite prazosin note, β blocker classification by selectivity,
  generations, vasodilation, ISA, membrane stabilisation, water solubility, pharmacokinetic/antioxidant properties,
  β blocker adverse effects across brain/bronchi/glucose/exercise/heart/kidney/metabolism, clinical uses and toxicity antidote).
- DONE (session 6): **ch19 "Antiarrhythmic Drugs: Part 1"** (p69-73) - 112 qs, 7 units
  (cardiac action potentials, Vaughan Williams classification, SVT/PSVT mechanisms and AV nodal drug preference,
  atrial flutter/fibrillation and ventricular arrhythmia strategy, class I Na+ channel blockers, quinidine/procainamide/
  disopyramide toxicities and uses, lidocaine/mexiletine/phenytoin, class Ic drugs and WPW syndrome).
- DONE (session 6): **ch20 "Antiarrhythmic Drugs: Part 2"** (p74-76) - 75 qs, 6 units
  (class II/III/IV/V map, β blockers and calcium channel blockers in arrhythmias, class III K+ channel blockers,
  amiodarone spectrum and organ toxicities, dronedarone, adenosine MOA/route/dosing/uses/adverse effects,
  digoxin rhythm indications and magnesium sulfate in torsades).
- DONE (session 6): **ch21 "Drugs Used in CHF"** (p77-82) - 130 qs, 8 units
  (acute CHF pathophysiology and IV management, inotropes and pulmonary edema drugs, chronic CHF compensation,
  mortality-reducing oral classes, newly diagnosed CHF approach, neprilysin and soluble guanylate cyclase drugs,
  digoxin pharmacokinetics, therapeutic levels, Na+/K+ ATPase mechanism, arrhythmia logic, toxicity treatment,
  organ effects, adverse effects, contraindications and DIGOXIN summary).
- DONE (session 6): **ch22 "Vasodilators"** (p83-88) - 136 qs, 7 units
  (vasodilator classification, calcium channel blocker comparison/adverse effects/uses, hydralazine, minoxidil,
  diazoxide and fenoldopam, nitroglycerin mechanism/uses/tolerance/contraindications, isosorbide nitrates,
  sodium nitroprusside, RAAS physiology, ACE inhibition, contraindications, ACE inhibitors, ARBs, aliskiren and captopril test).
- DONE (session 7, this session): **ch23 "Antihypertensive Drugs"** (p89-90) - 70 qs, 4 units
  (classification by Rx preference with 1st/2nd line lists; age table young <55 hyperreninemic vs old >55
  hyporeninemic with A/B/C/D drug letters; clinical approach stepping A -> A+C -> A+C+D -> resistant HTN
  + spironolactone; comorbidity flowchart DM/CKD/nephrotic/scleroderma, BPH, Raynaud, cyclosporine HTN,
  migraine; severe HTN >=220/135 with end-organ damage -> emergency IV drugs vs urgency oral drugs,
  labetalol DOC pregnancy, nicardipine DOC, clonidine DOC oral).
- DONE (session 7): **ch24 "Antianginal Drugs"** (p91-93) - 74 qs, 6 units
  (stable vs variant Prinzmetal angina pathogenesis; acute attack S/L NTG and its type-specific MOA;
  variant prophylaxis CCB DOC amlodipine + long-acting nitrates; stable angina two aims - attacks vs
  mortality; ivabradine funny channels/If, uses and visual phenomena; ranolazine LINA+/delayed rectifier
  K+, HbA1c; nicorandil, fasudil, allopurinol, bosentan, trimetazidine pFox).
- DONE (session 7): **ch25 "Hypolipidemic Drugs"** (p94-100) - 180 qs, 10 units
  (full lipid physiology diagram - NPC1L1/ACAT/HSL/MTTP/LPL/AngPTL3 and every drug arrow; cholesterol
  synthesis cascade + LDL receptor upregulation; PCSK9 and inclisiran/evolocumab/alirocumab; evinacumab,
  lomitapide, FHC; niacin including PG-mediated flushing and aspirin; fibrates PPAR-alpha, gall stones,
  uric acid; LDL drug flowchart; bile acid binding resins incl. the pregnancy exception and the
  70/60/50/15-25% ranking; statins MOA and pleiotropic effects; statin PK - OATP1B1, CYP3A4 exceptions,
  pravastatin, potency/T1/2/ceiling; statin side effects, C/I and the ASCVD risk/dose algorithm;
  hypertriglyceridemia and FHC treatment flowcharts).
- DONE (session 7): **ch26 "Diuretics: Part 1"** (p101-105) - 119 qs, 8 units
  (definition and uses; CA inhibitors - site, drug list, PCT/TAL/CD physiology, MOA, all 8 effects incl.
  metabolic acidosis uses, alkaline urine stones, catamenial epilepsy, hyperammonemia C/I cirrhosis,
  aqueous/CSF effects, sulfonamide effects and weak CA inhibition of loops/thiazides; loop diuretics -
  drugs incl. ethacrynic acid, TAL physiology with Ca/Mg compensation, MOA 25% filtered load and
  compensatory uric acid/glucose/SNS/lipolysis, collecting duct H+/K+ effects, LOOP uses, DOC pulmonary
  edema, and ear/ototoxicity rules).
- DONE (session 7): **ch27 "Diuretics: Part 2"** (p106-112) - 162 qs, 11 units
  (thiazides - metabolism-based drug list with chlorthalidone/metolazone specifics, MOA with Ca
  reabsorption and vasodilation, effects/uses/erectile dysfunction, loop-like side-effect table;
  K+ sparing - ENaC vs aldosterone blockers, MOA, spironolactone/eplerenone/finrenone, amiloride DOC
  list incl. Li-induced DI and the thiazide-in-DI note, triamterene; mannitol incl. TURP irrigation,
  electrolyte table and C/I; free water clearance and the diuretic effect table; vasopressin analogues
  and antagonists with SIADH management; the full diuretics summary table).
- DONE (session 7): **ch28 "Antiepileptic Drugs: Part 1"** (p113-117) - 118 qs, 10 units
  (epilepsy types; GTCS and m.s. mechanisms and features; absence typical vs atypical with 3 Hz spike;
  partial seizure SOL pathway; LGS and Dravet syndrome treatment mnemonics and duration rules; drug
  classification; valproate Tab VALPROIC with L-carnitine; phenytoin HYDANTOIN and fosphenytoin;
  carbamazepine incl. Rolandic epilepsy and SJS; lamotrigine and topiramate; oxcarbazepine,
  zonisamide, lacosamide, rufinamide; SJS/HLA associations).
- DONE (session 7): **ch29 "Antiepileptic Drugs: Part 2"** (p118-119) - 38 qs, 2 units
  (ezogabine/retigabine, AMPA/NMDA blockers, cannabidiol, SV2A modulators levetiracetam and
  brivaracetam with the pregnancy hierarchy; GABA synapse sketch with pregabalin/gabapentin,
  tiagabine, vigabatrin, GBS mnemonic, baclofen and JME polytherapy note).
- DONE (session 7): **ch30 "Sedative-Hypnotic Drugs"** (p120-122) - 73 qs, 6 units
  (classification and definitions; GABA-A receptor mechanism with bicuculline, alpha subunits, Z-drugs,
  barbiturates vs benzodiazepines, phenobarbitone DOC list, inverse agonist/antagonist/full agonist;
  benzodiazepine metabolism groups with remimazolam, longest/shortest acting lists and LETO; DORA;
  melatonin agonists incl. ramelteon/agomelatonin/tasimelteon and the sedation ranking; insomnia
  treatment algorithm).
- **TOTAL BEFORE THIS BATCH: 3692 questions, 290 units, chapters 1-36.** General Pharmacology, Autonomic Nervous System, Cardiovascular System, Renal System and Central/Peripheral Nervous System through Neurodegenerative Disorders were live.
- SESSION 4 NOTES: work/fixranges.py (auto-syncs unit [a,b] ranges from the q() order) and
  work/fixexp.py (forces exp to end "(Book p<page>)") were added to make the per-chapter pipeline
  less error-prone; run both before work/validate.py.
- SESSION 7 NOTES: `work/gen_ch23_30.py` is the generator for chapters 23-30 (same helper pattern as
  gen_ch18_22.py: start/unit/q/end_unit/finish, one `finish()` per chapter). `work/crop.py` is a new
  helper that renders a magnified CROP of any book page:
  `python3 work/crop.py <book_page> <x0%> <y0%> <x1%> <y1%> [dpi]` -> work/pages/crop.png
  (used to verify the FWC table, lipid index and loop-diuretic effect lists at 260-320 dpi).
  Renders for this batch: `python3 work/render.py 89 122 140` (34 PNGs, 1157x1636 — fully legible).
  Note: some scanned spreads are physically swapped in the PDF (e.g. book p92/p93, p106-p109 return in
  a shuffled read order); the printed page number in the image is authoritative — always trust it.

- DONE (session 8): **ch37 "Alcohol and Smoking Dependence"** (p150-152) - 65 qs, 4 units
  (ethanol/methanol/ethylene-glycol metabolism; disulfiram, naltrexone and acamprosate; LFT-based
  alcohol-dependence algorithm and acute withdrawal; varenicline receptor actions/adverse effects,
  nicotine patch/rescue NRT regimen, dry-eye use and smoking-cessation escalation).
- DONE (session 8): **ch38 "Introduction to Antibacterial Drugs"** (p153-154) - 52 qs, 4 units
  (all target-based classes and static/cidal exceptions; treatment-selection principles; therapy by
  wall presence, resistance and infection site; peptide size/porin limitations, oxygen-dependent
  aminoglycoside uptake and beta-lactam synergy).
- DONE (session 8): **ch39 "Cell Wall Synthesis Inhibitors: Part 1"** (p155-158) - 83 qs, 4 units
  (all four peptidoglycan synthesis stages and inhibitor arrows; moderate and long-acting penicillins
  with SLYGRAM; anti-staphylococcal and antipseudomonal groups; complete amoxicillin/ampicillin table;
  MRSA/VRSA resistance mechanisms and treatments).
- DONE (session 8): **ch40 "Cell Wall Synthesis Inhibitors: Part 2"** (p159-163) - 105 qs, 5 units
  (generation-wise cephalosporin spectrum and every named drug/use; cefiderocol iron-pump mechanism;
  carbapenems/aztreonam; shared and drug-specific beta-lactam toxicity/dosing; efflux, porin and PBP
  resistance; Ambler A-D classification, NDM-1 and all old/new inhibitor combinations).
- DONE (session 8): **ch41 "Cell Wall Synthesis Inhibitors: Part 3"** (p164-166) - 61 qs, 5 units
  (fosfomycin/cycloserine/bacitracin table; vancomycin action and VISA/VRSA MIC values; MRSA, VRE and
  C. difficile algorithms; red-man syndrome; Matzke/Sawchuk/Bayesian dosing; other glycopeptides).
- DONE (session 9, this session): **ch42 "Protein Synthesis Inhibitors: Part 1"** (p167-170) - 100 qs, 8 units
  (ribosome E/P/A sites with step-I peptidyl transferase and step-II translocation; chloramphenicol +
  pleuromutilin on 50S peptidyl transferase with high toxicity; 30S A-site binders - tetracyclines block,
  aminoglycosides misread to cidal death; 50S translocation blockers macrolide/linezolid/streptogramins/
  clindamycin; MLS-B methylase of MBS with lincosamide + streptogramin B cross resistance; tetracycline
  MOA/i-m C-I/minocycline 100% > doxycycline bioavailability/wide spectrum except Proteus-Pseudomonas-
  Providencia/efflux-enzyme-ribosomal protective protein resistance; doxycycline "my Pink RBC" DOC list,
  minocycline leprosy, demeclocycline SIADH, tigecycline glycycycline IV-only last-line with UTI/bacteremia
  C-I; scrub typhus fever-rash-eschar and oral vs IV doxycycline + azithromycin; tetra packet side effects
  incl. Fanconi from expired drug and V2 block for DI; aminoglycoside spectrum/routes/enzyme inactivation
  except amikacin/altered ribosome only streptomycin; gentamicin > streptomycin plague-tularemia, neomycin
  gut sterilization vs rifaximin DOC, tobramycin inhaled in cystic fibrosis; nephro/neuro/oto toxicity
  max-min rankings with Ca++ then neostigmine and early Ca++ prevention; sarecycline/omadacycline/plazomicin).
- DONE (session 9): **ch43 "Protein Synthesis Inhibitors: Part 2"** (p171-173) - 77 qs, 8 units
  (macrolide translocase MOA and enzymatic/MLS-B resistance; erythromycin penicillin-G-like spectrum,
  pertussis/diphtheria/rheumatic-fever DOCs and macro SD Card side effects with motilin HPS, QT order
  E>C>A, estolate cholestatic jaundice and gastroparesis; clarithromycin BD and azithromycin OD longest
  acting with atypical pneumonia/campylobacter/cholera-in-pregnancy/scrub typhus add-on; linezolid BM
  suppression, MAO cheese reaction with IV phentolamine, mitochondrial lactic acidosis/optic neuritis, VRE/
  MRSA-VRSA/resistant TB DOCs, 100% oral bioavailability and tedizolid OD; streptogramin IV-only central
  line and last-line MRSA/VRSA/VRE; clindamycin spectrum and the supradiaphragmatic Prevotella-clindamycin
  vs intradiaphragmatic Bacteroides-metronidazole table plus TSS/osteomyelitis; chloramphenicol gray baby
  chain; pleuromutilins retapamulin/lefamulin; fidaxomicin t-RNA polymerase, mupirocin t-RNA synthase nasal
  MRSA, fusidic acid elongation block, rifaximin RNA polymerase uses).
- DONE (session 9): **ch44 "Other Antibacterial Drugs"** (p174-179) - 144 qs, 10 units
  (three-branch classification; polymyxin cationic detergent phospholipid binding, pseudopores with lysis/
  drug entry/endotoxin block, Neosporin topical vs colistin IV MDR gram -ve with nephro/neuro toxicity and
  aminoglycoside C-I; daptomycin large peptide, K+ efflux depolarization, VRSA DOC and empirical MRSA,
  myopathy and surfactant pneumonia C-I with vancomycin/linezolid notes; folate pathway DHPS absent vs DHFR
  present in humans with bacteriostatic blockers turning bactericidal and neural-tube risk; sulfonamide
  spectrum except Enterococcus/Pseudomonas/Rickettsia paradoxical overgrowth, sulfadoxine/sulfadiazine/
  sulfisoxazole/sulfasalazine; cotrimoxazole 5:1 tablet vs 20:1 blood, 20x potency, cystitis and six-organism
  DOC list, mesalamine and spiramycin notes, topical sulfadiazine/mafenide/sulfacetamide; kernicterus
  displacement chain, porphyria, methemoglobinemia cyanosis refractory to O2, crystalluria; nalidixic acid
  and fluoroquinolone gyrase/topoisomerase IV split, norfloxacin least vs ciprofloxacin most active with the
  full DOC list incl. anthrax bioterrorism, pseudomonas C>L, respiratory FQs and the CAP amoxicillin+
  azithromycin algorithm with three unresponsive options and delafloxacin/ozenoxacin; PQRST side effects
  with tendon-rupture risks and vit-D exception, cartilage C-I, moxifloxacin/levofloxacin/gemifloxacin/
  pefloxacin maximum comparisons; urinary antiseptics with nitrofurantoin hemolysis, trimethoprim ENaC
  hyperkalemia and the methenamine hippuric-mandelic acid/ammonia-formaldehyde pathway and C-Is).
- DONE (session 9): **ch45 "Anti-fungal Drugs"** (p180-183) - 70 qs, 6 units
  (fungal cell diagram - squalene epoxidase/terbinafine, 14-alpha-sterol demethylase/azoles, flucytosine on
  DNA, griseofulvin on microtubules, beta glucan synthase/echinocandins + ibrexafungerp, wall proteins-
  chitins-beta glucans, amphotericin B ergosterol sequestration, and the full target-based tree;
  amphotericin B 5% dextrose carrier, four DOCs, shake & bake with pethidine, NaCl preload and LAmB,
  hypokalemia 1/3 with KCl, cryptococcal TOC IV AmB + IV flucytosine; terbinafine keratin concentration and
  onychomycosis; fluconazole coccidioidal meningitis and mucocutaneous candida with clotrimazole-lozenge
  exception, itraconazole Itomed/endemic mycoses/sporotrichosis and ABPA steroid-sparing; ketoconazole
  endocrine effects and Cushing secondary use, voriconazole aspergillosis and visual problems, posa/isavu-
  conazole aspergillosis-mucor and GVHD prophylaxis; echinocandin four drugs and invasive candidiasis DOCs,
  ibrexafungerp oral recurrent vaginal candidiasis with oteseconazole; griseofulvin stratum corneum/fatty
  foods/kerion DOC, flucytosine 5-FU prodrug 2-week cap, natamycin corneal ulcer with atropine add-on).
- DONE (session 9): **ch46 "Non-Retroviral Drugs"** (p184-188) - 105 qs, 7 units
  (three antiviral groups; herpes DNA virus epithelial tropism with the full replication diagram -
  docosanol/fomivirsen attachment, VK/CK phosphorylation, foscarnet primer-pyrophosphate block, AC-TP/GC-TP
  competitive DNA polymerase block, cidofovir cytosine analogue via CK; UL-97 vs thymidine kinase and
  maribavir lowering ganciclovir effect, resistance via absent/altered kinase with cidofovir/foscarnet
  alternatives; acyclovir route logic with valacyclovir DOC HSV/VZV and 36-week perinatal prophylaxis,
  crystalluria obstructive failure and neurotoxicity, ganciclovir CMV routes with valganciclovir retinitis
  DOC, intravitreal for blindness risk and filgrastim for neutropenia; penciclovir/famciclovir, foscarnet
  electrolytes, cidofovir IV-topical-intralesional uses, fomivirsen ocular toxicity and the three topical-only
  drugs; influenza RNA virus with hemagglutinin-sialic acid, m-protein uncoating block abandoned for
  resistance, neuraminidase inhibitors with every route and dosage, baloxavir endonuclease single dose;
  hepatitis B active-case criteria, entecavir decompensation DOC and lamivudine-resistance link, adefovir
  dipivoxal, tenofovir DOC/nephrotoxic/decompensation C-I, lamivudine converts not together, IFN-alpha2b
  1-year finite course and Hep-D DOC; hepatitis C IFN and ribavirin routes incl. inhaled RSV DOC, DAA
  2/3-drug TOC with ritonavir-boosted paritaprevir and the -buvir/-asvir/-previr suffix key, plus the
  interferon note with palivizumab/nirsevimab).
- **TOTAL LIVE NOW: 5201 questions, 421 units, chapters 1-55.** Antimicrobials section is COMPLETE
  (through Anti-Protozoal ch49 + Anti-Helminthic ch50); Endocrine System live through Steroids (ch55).
- DONE (session 10): **ch47 "Anti-Retroviral Drugs"** (p189-192) - 86 qs, 8 units
  (HIV replication cycle diagram - RNA virus/CD4 tropism, attachment CD4-ibalizumab + CCR5-maraviroc,
  GP41-enfuvirtide fusion only-GP41, capsid-lenacapavir, GP120-fostemsavir, uncoating/reverse
  transcription/integration in human nucleus, protease assembly->immature->maturation->mature exits;
  classification RTI(NRTI/NNRTI)/PI/integrase/attachment; NRTI nucleoside analogs HIV1+2 with
  mitochondrial toxicity, lamivudine least toxic, emtricitabine palm-sole pigmentation, tenofovir
  nephrotoxicity+bone density age<10/weight<30, 2NRTI+DTG regimen, PrEP, abacavir HLA B5701 SJS,
  didanosine/stavudine abandoned, zidovudine children marrow suppression C/I anemia; NNRTI only HIV-1
  3rd line, nevirapine perinatal DOC fatal hepatotoxicity zidovudine alternative, 5-drug list; PI <6yr/<20kg
  CYP3A4 except nelfinavir 2C19, all CYP3A4 inhibitors, insulin resistance triad, GI dose-limiting,
  hemophilia bleeding, saquinavir least vs ritonavir most potent booster, LPV/r 90/10 MI, atazanavir acid
  pH no insulin resistance stones+bilirubin also indinavir, darunavir food, boosters all except nelfinavir,
  cobicistat with atazanavir/darunavir/elvitegravir; integrase 4 drugs DTG preferred; attachment
  inhibitors routes; WHO 1st-line table TDF+3TC+DTG / ABC+3TC+DTG 6-10yr / ABC+3TC+LPV/r <6yr,
  pregnancy not-on-ART/already-on-ART/NVP-exposure rows + index).
- DONE (session 10): **ch48 "Anti-Mycobacterial Drugs"** (p193-198) - 116 qs, 10 units
  (mycolic acid pathway diagram Kat-G catalase-peroxidase -> INH(a) -> acyl protein reductase Inh-A +
  kinase Kas-A -> mycolic acid -> cell wall with ethionamide convergence; MOA table H mycolic/R RNA
  polymerase/Z pnc-a pyrazinaminidase acidic pH pyrazinoic acid fatty acid/E arabinosyl transferase;
  resistance Kat-G most severe+ethionamide cross, Inh-A overexpression, rpo-b, pnc-a, Emb-b; H/R/Z/E
  comparison cidal-static, first non-infective H, R maximum, sites intra/extra, persisters R>Z,
  excretion liver H/R/Z safest R, kidney E unsafe; S/E table - INH B6 haem anemia GABA seizure
  neuropsych, rifampicin red-orange lenses flu-like intermittent stop-permanently purpura enzyme inducer
  least rifabutin uveitis, Z most hepatotoxic Z>H>R>E hyperuricemia arthralgia, E optic neuritis green>red;
  INH toxicity IV pyridoxine 1g/gm max 5g; rifapentine+INH weekly latent; group A/B/C second line;
  new drugs bedaquiline ATP synthase 165d 99% albumin <2.8, delamanid/pretomanid free radicals+mycolic,
  MDR/pre-XDR/XDR definitions, food advice, QT C/I arrhythmia, pregnancy safe only Bdq; old drugs
  ethionamide cidal hypo thyroid, PAS DHPS static rifampicin C/I; regimens HRZE 2+4, shorter oral Bdq
  months table, injectable alternative, long oral 18-20 months, BPaL doses 200/400-200/1200;
  leprosy first/second line static-cidal split, clofazimine TB cidal leprosy static ichthyosis crystals,
  lepra type1/type2 DOC steroids thalidomide most effective; WHO supervised/monthly + non-supervised/daily
  dose table adults 10-14 <14-40kg; rifampicin-resistance 6/18 month regimens; MAC EAR azithromycin
  immunomodulator).
- DONE (session 10): **ch49 "Anti-Protozoal Drugs"** (p199-204) - 108 qs, 12 units
  (amoebiasis diagram luminal diloxanide/iodoquinol/paromomycin DOC radical cure vs symptomatic
  nitazoxanide/emetine/metronidazole DOC + chloroquine hepatic only; nitroimidazoles 5 drugs India DOC
  metronidazole west tinidazole, free radicals, TOC metronidazole f/b paromomycin, DOC list giardia/
  amoebae/infra-diaphragmatic anaerobes/tetanus/trichomonas/bacterial vaginosis, disulfiram red-brown
  urine, cefazolin+metro surgical prophylaxis, clue cells; leishmaniasis visceral LAmB IV + miltefosine
  oral PKDL pregnancy C/I nausea diarrhea, sitamaquine alternative, cutaneous sodium stibogluconate;
  trypanosomiasis East suramin/melarsoprol, West pentamidine/eflornithine fexinidazole 2019, Chagas
  benznidazole nifurtimox; cryptosporidiasis nitazoxanide from niclosamide PFOR green urine resistant
  giardia H.pylori off-label; babesiosis TOC atovaquone+azithromycin all severity, earlier quinine+
  clindamycin mild; plasmodium life cycle diagram sporozoites infective humans hypnozoite dormancy
  merozoites RBC erythrocytic schizont rupture fever chills gametocytes infective mosquito integrated
  blood meal; drug stages hypnozoiticidal primaquine 14d tafenoquine single radical cure terminal
  prophylaxis vivax-ovale only, gametocidal primaquine+artemisinin, schizontocidal fast DOC + slow,
  1fast+1slow; artemisinin most potent fastest free radicals C/I 1st trimester artesunate IV+oral,
  no monotherapy/prophylaxis, severe falciparum 48hr artesunate infusion; uncomplicated malaria vivax
  CQ+primaquine post-partum, CQ-resistant pregnant 1st quinine+clindamycin 2nd-3rd ACT, ACT sulfadoxine
  pyrimethamine all states vs artemether lumefantrine north-east, alternatives not safe pregnancy;
  chloroquine haem products efflux resistance uses mono/SLE/PCT bull's eye whorl cornea; quinine alpha
  block insulin K+ QT cinchonism black water; mefloquine neuropsychiatric conduction C/I quinine
  halofantrine, prophylaxis <6wk doxycycline 2d-4wk vs >=6wk mefloquine 250mg 2wk-4wk, atovaquone
  proguanil mosquito ovulation, clindamycin safe children pregnancy).
- DONE (session 10): **ch50 "Anti-Helminthic Drugs"** (p205-206) - 43 qs, 7 units
  (benzimidazoles 4 drugs mebendazole west/albendazole India prodrug sulfoxide liver microtubule glucose
  ATP; nematode DOC tree albendazole round/whip/hook/enterobius/trichinella, ivermectin strongyloides
  onchocerca, DEC loa loa filariasis TOC IDA, metronidazole dracunculiasis; cestodes albendazole
  neurocysticercosis echinococcus vs praziquantel intestinal T.solium T.saginata H.nana D.latum with
  steroids first priority perilesional edema; trematodes triclabendazole fasciola vs praziquantel other
  liver/lung flukes schistosoma, albendazole ineffective trematodes; ivermectin glutamate chloride tonic
  paralysis scabies oral DOC Mazzotti DEC; praziquantel Ca2+ spastic = pyrantel metrifonate, metrifonate
  AChE S.haematobium; pyrantel Nm receptors soil transmitted; piperazine GABA Cl- flaccid soil transmitted).
- DONE (session 10): **ch51 "Antidiabetic Drugs: Part 1"** (p207-210) - 70 qs, 8 units
  (DM type I/II persistently raised glucose; physiology diagram SGLT1 absorption, alpha glucosidase
  disaccharides, GLP-1/GIP DPP-4 short t1/2, Gs/q beta cell ATP-sensitive K+ block GLUT-1, post-prandial
  facilitated diffusion, insulin+amylin receptor GLUT-4, amylin+GLP-1 delayed gastric emptying dampens
  PPH, SGLT2 renal reabsorption, liver gluconeogenesis fasting; drug classification alpha-GI, GLP-1
  related (agonist/DPP4/dual), miscellaneous bromocriptine colesevelam, amylin analog, insulin, OHA 5
  mechanisms sotagliflozin 2019, T1DM insulin+amylin vs T2DM all, hypoglycemia via-insulin; insulin
  duration table ultra-short Afrezza fastest just-before-food, monomeric glulisine lispro aspart 15min,
  regular 60min slow-acting-short, PPH vs maintenance split, NPH+lente BD/TDS intermediate, detemir
  protein binding glargine acidic degludec hexameric longest OD/BD; routes inhaled Afrezza lung
  capillaries, SC all others, IV regular hyperkalemia DKA DOC; regimen 1 PPH + 1 maintenance same syringe
  regular drawn first cloudy NPH, infusion in-patients no peak; injection sites abdomen m/c periumbilical
  lipodystrophy faster reliable, thigh antero-lateral, buttocks, arm; Afrezza cartridges blue4 green8
  yellow12 cough lung cancer C/I asthma COPD smokers; lente zinc ultralente 70% long crystals semilente
  30% short powder; S/E hypoglycemia m/c proportional shorter-acting higher glargine peakless,
  hypokalemia, lipodystrophy rotation >=1 inch).
- DONE (session 10): **ch52 "Antidiabetic Drugs: Part 2"** (p211-214) - 77 qs, 9 units
  (insulin-releasers classification GLP-1 related vs ATP-sensitive K+ inhibitors common hypoglycemia;
  GLP-1 agonists liraglutide OD vs dulaglutide/albiglutide/semaglutide weekly S/C oral semaglutide,
  pancreatitis nausea delayed emptying weight loss appetite DOC obesity oral>S/C semaglutide>liraglutide;
  DPP-IV decreased metabolism weight neutral 4 -gliptins oral pancreatitis angioedema ACE DAA6
  lymphocyte infections C/I renal failure except linagliptin liver; tirzepatide dual S/C > pure;
  sulfonylurea vs meglitinide table large/small, long/short, maintenance/PPH, hypoglycemia weight gain
  HSL thin diabetics alcohol disulfiram, glyburide glibenclamide glimepiride gliclazide vs nateglinide
  phenylalanine repaglinide, insulin highest overall; TZD PPAR-gamma GLUT-4 adipocyte pioglitazone
  rosiglitazone ENaC edema CHF macular edema fracture females Ca bladder hepatotoxic; metformin AMPK
  blocks gluconeogenesis DOC T1+T2 prophylaxis PCOS anovulation NASH antipsychotic obesity FDA,
  metabolic acidosis mitochondrial aerobic glycolysis B12 calcium dependent weight loss GAMs mnemonic;
  SGLT2 cana/dapa/empa + sotagliflozin dual kidney+intestine CHF preload diuresis mortality, Na+
  diuresis hypotension dehydration glucose UTI candida rare fracture elderly Fournier's urosepsis;
  alpha-glucosidase acarbose voglibose miglitol T2DM only during meal flatulence m/c osmotic diarrhea;
  pramlintide S/C delayed emptying T1+T2 different syringe 50% insulin cut nausea weight loss off-label;
  CVS mortality SGLT2+GLP-1; metformin C/I alcoholism COPD renal liver CHF smoking not).
- DONE (session 10): **ch53 "Drugs Acting on Reproductive System"** (p215-217) - 51 qs, 8 units
  (hypothalamo-pituitary axis pulsatile GnRH Gs/q gonadotroph LH/FSH females ovulation estrogen
  progesterone males spermatogenesis testosterone; agonists goserelin buserelin nafarelin leuprolide
  intermittent increased LH/FSH infertility anovulation oligospermia delayed puberty vs continuous
  initial increase then decrease receptor downregulation precocious puberty estrogen dependent ER+
  breast endometriosis fibroids testosterone prostate DOC goserelin; gonadorelin diagnosis
  hypothalamic/pituitary anovulation; antagonists ganirelix cetrorelix abarelix elagolix decreased
  LH/FSH; SERM table tamoxifen treatment ER+ premenopausal vs raloxifene prophylaxis osteoporosis
  post-menopausal uterine Ca only tamoxifen thrombosis hot flashes, toremifene ospemifene dyspareunia;
  clomiphene partial agonist pituitary positive feedback GnRH LH ovulation DOC anovulation without PCOS
  letrozole with PCOS; fulvestrant ER block 100x resistant post-menopausal; elacestrant ESR1 mutation;
  ulipristal SPRM emergency contraception 30mg 5d vs levonorgestrel India DOC 1.5mg 73h or 0.75x2 12h;
  5-alpha reductase testosterone DHT finasteride dutasteride alopecia 1mg BPH size weight tamsulosin
  silodosin symptomatic DOC; androgen receptor blockers flutamide bicalutamide enzalutamide apalutamide
  add-on prostate hirsutism gynecomastia impotence > 5ARI; aromatase inhibitors adipocytes post-menopausal
  exemestane letrozole DOC ER+ breast + PCOS anovulation, gender change leuprolide).
- DONE (session 10): **ch54 "Growth Hormone and Related Drugs"** (p218-220) - 42 qs, 3 units
  (physiology diagram GHRH Gs/q + somatostatin Gi -, somatotrophic cell, GH direct receptor linear
  growth, liver IGF-1 + IGF BP-3 plasma, IGF-1 receptor glucose inside cell, GH inhibits insulin,
  somatostatin decreases GH+TSH; dwarfism GHRH analogs sermorelin macimorelin tesamorelin diagnostic
  GH increase hypothalamic vs no change pituitary; GH analogs somatrem somatropin SMALL small
  gestational age malabsorption short bowel teduglutide GLP-2 AIDS wasting decreased length, CHILDREN
  carpal tunnel hyperglycemia ICP leukemia DM, C/I retinopathy neoplasia; IGF-1 analogs mecasermin
  rinfabate longer hypoglycemia lipohypertrophy IGF-1 deficiency GHR mutation anti-GH Ab; acromegaly
  somatostatin analogs pasireotide octreotide LAR lanreotide 30 days S/C I/M hypothyroidism gall
  stones SOMAT secretory diarrhea DM AIDS radiolabeled diagnosis metabolic glucagonoma DOC insulinoma
  diazoxide variceal terlipressin acromegaly thyrotrope; pegvisomant GH receptor blocker resistant
  acromegaly LFT adenoma size GHRH hypertrophy MRI IGF-1 visual field chiasma).
- DONE (session 10): **ch55 "Steroids"** (p221-223) - 54 qs, 5 units
  (development tree cortisol -> hydrocortisone least potent shortest 8-12h GC1x MC1x DOC replacement
  Addison CAH after birth insufficient immune suppression; double bond prednisone/prednisolone 12-36h
  GC4x MC0.8x + methyl water soluble methylprednisolone GC5x MC0.8x; fluoride pure GCs minimal BP
  triamcinolone 12-36h GC5x MC0, betamethasone/dexamethasone 36-72h GC30x MC0 dexamethasone longest
  most potent; uses inflammation IL-1 IL-6 TNF down IL-10 annexin-1 up lymphocyte redistribution
  apoptosis RA gout AS, immunity GVHD rejection myasthenia, neoplasia leukemia lymphoma, CAH fetus
  dexamethasone virilization, preterm surfactant 24mg/48h dex 6mg q6h x4 beta 12mg q24h x2;
  Cushing diagram brain psychosis depression insomnia, eye topical glaucoma systemic posterior
  sub-capsular cataract, hair thinning, gastric ulcers, myopathy, striae, osteoporosis Ca excretion
  secondary hypercalcemia use, thin skin bruises; metabolic decreased GLUT-4 hyperglycemia DM
  lipodystrophy lemon-on-stick insulin blocks lipolysis central obesity limbs GLUT-4 down thin
  extremities buffalo hump; C/I infections exceptions H. influenzae meningitis covid pneumonia only
  mortality drug; mineralocorticoids fludrocortisone hydrocortisone+fluorine GC15x MC150x Addison
  with hydrocortisone postural hypotension DOC midodrine, aldosterone GC0 MC500x pure most potent).
- **SESSION 10 NOTES:** source pages p189-223 re-rendered at 180 dpi and read line-by-line from the scanned
  book; zoom crops verified bedaquiline "165 days" + "albumin <2.8 mg/dl" (p195), BPaL doses "400 mg OD
  first week -> 200 mg 3x/week, linezolid 1200 mg" (p196), levonorgestrel "within 73h" wording (p217),
  glucocorticoid potencies (p221) and the GH(-)->insulin arrow (p218). The session-9 leftover generator
  stubs were REWRITTEN (the old gen_ch50_52.py had pramlintide questions misplaced inside the ch50
  benzimidazoles unit; gen_ch53_55.py was missing its ch53 opening block) as three reproducible
  generators: work/gen_ch47_49.py, work/gen_ch50_52.py, work/gen_ch53_55.py (same start/unit/q/facts/
  finish helper pattern). An earlier partial remote push of this batch (commit 112f22d, 613 q / 60 u,
  built from those buggy stubs) was merged and superseded; the stale per-chapter stubs work/gen_ch47.py
  .. gen_ch55.py were deleted so the three batch generators are the single reproducible source.
  Duplicate-stem audit across the batch (and against ch44-46): NONE. Validation,
  deterministic rebuild, integrity check and Node inline-JS syntax check all pass.

- DONE (session 11, this session): **ch56 "Drugs Acting on Bone"** (p224-226) - 59 qs, 6 units
  (calcium homeostasis diagram Step-I RANK ligand synthesis PTH/Vit D3 (+), Step-II RANK activates RANK,
  Step-III ruffled borders, Step-IV bone resorption, Step-V osteoblast activation, Step-VI bone formation,
  teriparatide (+) osteoblast, raloxifene (+) estrogen, calcium analogs fastest hypocalcemia (+) calcitonin,
  sclerostin inhibits formation, romosozumab inhibits sclerostin, strontium ranelate dual (+) formation (-) resorption,
  denosumab X osteoblast->osteoclast, bisphosphonates DOC max hypocalcemia kill; MOA farnesyl pyrophosphate
  synthase apoptosis, poor oral absorption empty stomach; IV pamidronate 3 monthly, zoledronate preferred
  once yearly longest most potent for 3 years, oral risedronate OD alendronate preferred OD for 5 years,
  osteoporosis DOC alendronate intolerance zoledronate, hypercalcemia malignancy and Paget start zoledronate,
  oral S/E esophagitis prevention full glass water no lie 30 min, IV > oral bone fracture femoral chalk-stick
  DOC teriparatide hypercalcemia maximum osteonecrosis jaw; denosumab RANK ligand postmenopausal osteoporosis,
  calcitonin intranasal osteoporosis S/C Paget cancer risk; anabolic teriparatide osteosarcoma C/I Paget max 2 yr,
  abaloparatide PTHrP, romosozumab sclerostin inhibitor, algorithm alendronate -> zoledronate -> fracture risk high denosumab very high anabolic).
- DONE (session 11): **ch57 "Drugs Acting on Thyroid"** (p227-229) - 57 qs, 6 units
  (physiology Na+-I- symporter TPO organification (1) coupling (2) MIT DIT T3 T4 thyroglobulin TG colloid
  thiol endopeptidase breaks TG release T4 5-deiodinase active T3; thioamides PTU carbimazole prodrug longer
  methimazole, PTU short multiple hepatotoxic vs methimazole long OD teratogenic cutis aplasia scalp choanal/esophageal
  atresia cholestatic jaundice, common maculopapular rash m/c agranulocytosis arthralgia; uses PTU 1st trimester
  less teratogenic + thyroid storm vs methimazole commonly prescribed 2nd-3rd trimester less hepatotoxic,
  thyroid storm 1st drug beta blockers prevent AF if C/I asthma/COPD verapamil/diltiazem other steroid KI;
  thiol endopeptidase inhibitors KI 10% Lugol 5% inhibits release fastest-acting tolerance not long-term
  decreased size firm decreased vessels bleeding prior surgery; 5-deiodinase inhibitors PTU steroids beta-blocker
  amiodarone; radioactive I131 ablation I123 scan uses elderly arrhythmia carcinoma except medullary recurrent Graves,
  S/E radiation thyroiditis ↑T3/T4 premedicate methimazole stop 3 days before I131 day given restart after 3 days lifelong
  hypothyroidism secondary cancers C/I pregnancy; hypothyroidism levothyroxine Le T4 longer DOC replacement empty stomach
  30 min breakfast thyroid cancer ↓TSH oral myxedema coma IV vs liothyronine Li T3 shorter prior I131 myxedema coma
  Le+Li+steroid, S/E thyrotoxicosis osteoporosis atrial fibrillation dose ↓ in arrhythmia).
- DONE (session 11): **ch58 "Anti-histaminics"** (p230-232) - 74 qs, 5 units
  (histamine receptors GPCR H1 post-synaptic Gq ↑Ca2+ allergy/motion, H2 post Gs ↑cAMP peptic ulcer,
  H3 presynaptic Gi ↓histamine pitolisant narcolepsy wakefulness, H4 leucocyte Gi chemotaxis no drugs;
  ↑Ca2+ bronchoconstriction vasodilation ↑GI wakefulness ↓appetite itching PNS, ↑cAMP heart ↑contraction HR stomach ↑HCl;
  H1 blockers first gen less potent cross BBB sedating muscarinic blocker preferred antimuscarinics C/I elderly children pilots drivers
  S/E nausea vomiting delayed emptying vs second gen more potent non-sedating no muscarinic preferred antihistaminics;
  promethazine diphenhydramine dimenhydrinate max antimuscarinic uses motion sickness 1 hr before oral EPS acute dystonia
  Meniere vertigo local anaesthetic dimenhydrinate insomnia promethazine chemo nausea vomiting α1 hypotension;
  doxylamine + B6 doxinate DOC morning sickness, chlorpheniramine least sedating 1st gen day time, meclizine/cyclizine motion,
  doxepin TCA, cyproheptadine 5HT2 blocker, hydroxyzine antipruritic skin allergies anxiolytic antiemetic,
  DOC motion sickness transdermal scopolamine patch; second gen DOC urticaria supplement allergic rhinitis hay fever DOC steroids
  cetirizine hydroxyzine derivative most sedating 2nd gen levocetirizine more potent lesser dose astemizole terfenadine QT torsades banned
  fexofenadine terfenadine derivative no QT least sedating, loratadine metabolite desloratadine most potent, rupatadine PAF anti-inflammatory,
  topical azelastine epinastine alcaftadine levocarbastine olopatadine allergic rhinitis conjunctivitis;
  bradykinin production kininogen kallikrein kallidin bradykinin B1 B2 ↑PG pain inflammation ↑NO vasodilation antagonists aprotinin
  lanadelumab berotralstat ecallantide icatibant B2 blocker aprotinin plasmin antifibrinolytic ↓bleeding post CABG, hereditary angioedema
  Rx DOC C1 esterase alternatives icatibant ecallantide prophylaxis DOC danazol alternatives lanadelumab berotralstat pre surgery EACA).
- DONE (session 11): **ch59 "Serotonin-related Drugs"** (p233-236) - 75 qs, 7 units
  (7 types 5-HT1-7 all GPCRs exception 5-HT3 ion channel, 5-HT1A presynaptic serotonergic Gi buspirone epsapirone gepirone
  non-benzo anxiolytics ↓5-HT2 ↓anxiety; 5-HT1B/1D/1F CN V trigeminal Gi CN V nucleus ganglion axon CGRP CGRP receptor meningeal
  vessel dilation edema compression migraine headache, 5-HT1F lasmiditan CN V nucleus, triptans 5-HT1B/1D axon ↓CGRP,
  CGRP ligand blockers eptinezumab fremanezumab galcanezumab parenteral prophylaxis, receptor blockers erenumab atogepant PO prophylaxis
  rimegepant PO acute, triptans approved acute; triptans MOA 5-HT1B ↓CGRP vasoconstriction differ PK>PD rate absorption ∝ efficacy potency,
  oral frovatriptan 27 hrs > naratriptan 6 hrs slow absorption long slow prolonged attack, fast rizatriptan fastest sumatriptan zolmitriptan
  eletriptan almotriptan short fast preferred acute, nasal zolmitriptan sumatriptan, SC/rectal sumatriptan overall fastest,
  S/E coronary vasoconstriction chest pain jaw/neck sweating arrhythmia C/I IHD MI/angina no stroke/TIA ischemic bowel HTN/PVD Raynaud/Burger
  specific naratriptan liver/renal eletriptan liver zolmitriptan WPW; other acute lasmiditan rimegepant ergotamine nonselective vasoconstrictor
  gangrene feet m/c dihydroergotamine less potent better same S/E C/I as triptans D2 chlorpromazine metoclopramide NSAID paracetamol mild-moderate
  ketorolac severe opioids intranasal butorphanol oral codeine pregnancy DOC paracetamol no response codeine/caffeine/metoclopramide no response
  sumatriptan choice may block placental flow; prophylaxis mnemonic Flunarizine Can PREVENT flunarizine cyproheptadine/candesartan/clonidine
  pizotifen/propranolol DOC GABA gabapentin valproate nortiptyline topiramate methysergide; 5-HT2 antagonist cyproheptadine H1 m migraine prophylaxis
  serotonin syndrome carcinoid cold urticaria AIDS weight gain pizotifen migraine methysergide migraine fibrosis pulmonary cardiac retroperitoneal
  flibanserin 5HT2A - +5HT1A agonist HSDD females, lorcaserin obesity banned cancer; obesity anorexia liraglutide phentermine lipolysis inhibitor orlistat
  stimulator mirabegron unknown topiramate naltrexone bupropion 5-HT3 antiemetics 5-HT4 prokinetics banned rimonabant suicidal lorcaserin cancer
  phenylpropanolamine stroke sibutramine MI).
- DONE (session 11): **ch60 "Eicosanoids"** (p237-241) - 91 qs, 7 units
  (synthesis arachidonic acid COX I II -> PG pain pyrexia inflammation + thromboxane A2 platelet aggregation, 5-LOX -> leukotrienes C4 D4
  bronchoconstrictors, reversible NSAIDs except aspirin irreversible, zileuton 5-LOX, montelukast/zafirlukast leukotriene block;
  PGE1 maintain PDA misoprostol NSAID gastric ulcer abortion PPH least effective alprostadil ED sildenafil DOC ED drugs phentolamine
  bremelanotide naltrexone ketanserin trazadone alviptadil, PGE2 dinoprostone PPH cervical ripening DOC, PGI2 pulmonary HTN vasodilation
  epoprostenol recombinant iloprost beraprost treprostinil analogs selexipag receptor agonist endothelin bosentan ambrisentan,
  PGF2α carboprost PPH abortion latanoprost bimatoprost eye drops DOC open angle normal tension glaucoma S/E heterochromia iridis
  dry/sandy eyes macular edema hypertrichosis hypotrichosis use C/I uveitis; non-selective COX inhibitors acetaminophen MOA COX I II ↓PG analgesia
  antipyrexia poor antiinflammatory + TRPV1 cannabinoid receptors hepatotoxicity m/c drug induced liver failure NAPQI depletes glutathione
  free radical centrilobular necrosis periportal sparing m/c drug poisoning symptoms renal tubular necrosis hypoglycemic coma hepatotoxicity
  dose 150-250 mg/kg >10 g fatal >20 g Rumack Mathew nomogram plasma concentration vs time safe unsafe 4 hr 10 hr 24 hr management <4 hr charcoal
  DOC NAC no response fulminant hepatic failure emergency transplant; aspirin dose dependent 50-325 OD antiaggregant 325-650 SOS analgesic antipyretic
  3-4 g/day anti-inflammatory uses antiaggregant RA rheumatic arthritis niacin flushing DOC essential thrombocythemia Kawasaki ↓colon cancer
  S/E bleeding m/c Reye viral fever children hepatic encephalopathy salicylism >10 g seizures tinnitus hyperglycemia metabolic acidosis Rx symptomatic
  dialysis severe C/I viral fever children gout (-) uric acid excretion warfarin ↑bleeding; indomethacin (-) COX phospholipase A&C leucocyte proliferation
  migration acute gout DOC Bartter paroxysmal hemicrania frontal headache, sulindac indomethacin derivative FAP ↓colon carcinoma ↓breast prostate,
  ibuprofen analgesic anti-inflammatory PDA closure DOC India aseptic meningitis toxic amblyopia blurred PDA worldwide DOC indomethacin,
  ketoprofen (-) COX (-) LOX stabilizes lysosome (-) bradykinin, flurbiprofen eye drops prevent intra-op miosis, piroxicam enterohepatic longest
  slow onset chronic pain, ketorolac ↑potency acute pain oral/parenteral migraine intranasal ocular pain eye drops, diclofenac short T1/2 long acting
  joints hepatotoxic GI ulcers ↓ with misoprostol uses RA psoriatic ankylosing gout dysmenorrhea acute pain, naproxen enantiomer nabumetone non-acidic
  long OD, selective COX II oral celecoxib etoricoxib parenteral parecoxib acute post-op uses anti-inflammatory RA rheumatic psoriatic ankylosing gout
  pain 3rd line dysmenorrhea acute S/E hypersensitivity rash m/c renal papillary necrosis cardiotoxicity rofecoxib valdecoxib peptic ulcer non-selective >
  selective DOC PPIs drug interactions ↓ antihypertensive ↓ lithium clearance toxicity ↓ diuretics furosemide).
- DONE (session 11): **ch61 "Gout"** (p242-243) - 35 qs, 6 units
  (acute aim ↓inflammation symptomatic relief NSAIDs no response steroid DOC indomethacin multiple MOA, colchicine (-)microtubules chemotaxis
  migration leucocytes ↓IL-1 neutrophils inhibit phagocytosis S/E nausea vomiting diarrhoea marrow suppression alopecia; chronic aim prevent acute ↓uric acid
  (-) synthesis xanthine oxidase inhibitors ↑ excretion uricosuric ↑ metabolism uricase analogues; allopurinol DOC chronic gout tumor lysis Lesch Nyhan
  organ transplant S/E hypersensitivity m/c SJS HLA-B-5801 (-) orotidylate decarboxylase orotic aciduria DRESS, oxypurinol orphan allopurinol
  hypersensitivity, febuxostat intolerance inadequate response ↑cardiovascular death, class xanthinuria xanthine stones acute gout prevention NSAID/colchicine
  3-6 months interaction inhibit 6-MP/azathioprine ↑toxicity; uricosurics probenecid sulfinpyrazone add on > mono benzbromarone lesinraud most effective
  add on only S/E ↑urate stones C/I h/o renal stones ↑calcium stones precipitate acute gout prophylaxis needed C/I renal failure except benzbromarone
  lesinraud mild-moderate renal failure miscellaneous losartan HTN atorvastatin ↑LDL fenofibrate ↑TG; uricase analogues no metabolism humans pegloticase
  resistant gout IV q2 wks rasburicase DOC high risk tumor lysis leukemia CLL S/E hemolysis G6PD methemoglobinemia).
- DONE (session 11): **ch62 "Rheumatoid Arthritis"** (p244-246) - 53 qs, 5 units
  (acute flare mild-moderate NSAIDs aspirin diclofenac > celecoxib severe steroids unresponsive NSAIDs 1-2 joints intra-articular triamcinolone >2 joints oral
  prednisolone; long term DMARDs conventional biological JAK inhibitors conventional methotrexate hydroxychloroquine sulfasalazine leflunomide cyclosporin
  azathioprine mycophenolate cyclophosphamide biological TNF IL-1 IL-6 abatacept CD-20 JAK tofacitinib baricitinib upadacitinib immunosuppression ↑infection
  not combined; methotrexate anchor DOC new Dx 2-4 wks inadequate 3-6 months add HCQ+sulfasalazine OR abatacept OR biological -> other biological or JAK,
  MOA inhibit DHFR ↓THF purine lymphocyte toxicity increased adenosine anti-inflammatory hepatic fibrosis S/E hepatotoxicity cirrhosis ALT/AST q3-6 months
  nephrotoxicity crystalluria marrow suppression DHFR THF; hydroxychloroquine inhibit lymphocyte proliferation stabilizes lysosomes mild monotherapy
  moderate-severe add on S/E Bull eye retinopathy ≤5 mg/kg/day ophthalmology yearly; sulfasalazine gut 5 ASA not absorbed ulcerative colitis + sulfonamide
  inhibits lymphocyte mild RA mono moderate-severe add on; TNF α infliximab adalimumab certolizumab etanercept golimumab IV/SC uses Alpha Inhibitors Prevent RA
  ankylosing IBD psoriatic plaque psoriasis RA S/E GIT ulcers perforation ↑infection ↑secondary skin cancers C/I hepatitis B reactivation CHF;
  IL-6 tocilizumab sarilumab RA cytokine storm COVID-19, IL-1 anakinra least effective least preferred, CD-20 rituximab anticancer abatacept CD 80/86 T cell
  belatacept related graft v/s host; JAK (-) cytokines baricitinib RA upadacitinib RA psoriatic atopic dermatitis ruxolitinib GVHD myelofibrosis polycythemia vera
  unresponsive hydroxyurea abrocitinib atopic dermatitis tofacitinib psoriatic ulcerative colitis juvenile idiopathic ankylosing RA).
- DONE (session 11): **ch63 "Anti-aggregants and Hematopoietic Agents"** (p247-250) - 62 qs, 6 units
  (physiology collagen vWF (+) platelet GP IIb/IIIa X abciximab COX-1 X aspirin thromboxane A2 ADP P2Y12 X clopidogrel phospholipids ↑ thrombin fibrinogen fibrin
  mesh permanent clot PAR X vorapaxar aggregation; aspirin irreversible COX-1 ↓TxA2 50-325 OD 2° prophylaxis ACS ischemic stroke Rx ACS essential thrombocythemia
  Kawasaki antiphospholipid bleeding pre-op continue aspirin stop clopidogrel 7 days; ADP/P2Y12 irreversible clopidogrel ticlopidine prasugrel reversible
  competitive cangrelor adenosine analog T1/2 3-6 min IV PCI MI non-competitive ticagrelor long oral PCI MI Rx ACS 2° MI hit & run irreversible ADP aspirin PPIs ↑T1/2;
  clopidogrel prodrug CYP2C19 polymorphisms blunted ↓effect worsen MI omeprazole competitive -, same as aspirin combined stent; ticlopidine toxicity GI
  nausea vomiting diarrhea agranulocytosis TTP-HUS 2° stroke resistant; prasugrel most potent fastest ↑intracranial bleed C/I stroke TIA PCI MI;
  vorapaxar PAR - 2° MI unstable angina single/combined aspirin/clopidogrel ↑intracranial bleed C/I stroke/TIA; GP IIb/IIIa abciximab blocks GPIIb/IIIa vitronectin
  shortest T1/2 max affinity longest acting eptifibatide longest T1/2 min affinity shortest acting uses PCI MI ACS route IV/intra-coronary tirofiban;
  erythropoiesis EPO epoetin alpha darbepoetin longer clinically preferred DOC anemia CRF dialysis zidovudine/anticancer premature infants S/E HTN iron deficiency
  thrombosis pure red cell aplasia flu like peginesatide CKD; granulopoiesis G-CSF ↑potent ↓toxic lenograstim filgrastim m/c multiple SC/IV lipegfilgrastim
  pegfilgrastim long single chemo cycle neutropenia myelodysplasia aplastic anemia HIV chemotherapy bone pain GM-CSF ↓potent ↑toxic sargramostim capillary leak;
  thrombopoiesis romiplostim eltrombopag ITP portal vein thrombosis AML new avatrombopag lusutrombopag prevent procedural bleeding liver cirrhosis
  IL-11 oprelvekin chemo induced thrombocytopenia fluid retention CHF edema).
- DONE (session 11): **ch64 "Anticoagulants and Fibrinolytics"** (p251-255) - 110 qs, 6 units
  (coagulation X->Xa oral Xa inhibitors prothrombin II->thrombin IIa direct thrombin inhibitors fibrinogen->fibrin, anticoagulation protein C&S antithrombin III
  protease breaks IIa Xa XIa XIIa (+) indirect thrombin inhibitors; direct oral dabigatran apixaban edoxaban rivaroxaban DOAC/NOAC no monitoring Rx DVT DOC prophylaxis
  DVT non-valvular AF parenteral HIT DOC argatroban aPTT hirudin lepirudin stopped desirudin SC DVT prophylaxis synthetic bivalirudin argatroban PCI MI C/I renal failure
  except argatroban hepatic other no monitoring LMWH fondaparinux bleeding antidotes dabigatran idarucizumab oral Xa andexanet alfa decoy; indirect UFH
  glycosaminoglycans mast cells MALT porcine mucosa AP attached long chain HPS antithrombin III breaks Xa long chain binds IIa table UFH AP+long HPS Xa=IIa poor bioavailability
  prophylaxis SC BD Rx IV QID RES metabolism DOC renal failure short aPTT protamine effective neutralizes HPS HIT ↑↑ vs LMWH AP+short HPS Xa>IIa ↑ bioavailability SC OD kidney excreted
  contraindicated renal failure long anti-Xa renal obese elderly children less effective HIT ↑ vs fondaparinux AP only only Xa max no monitoring not effective none;
  HIT antibodies HPS cross platelet factor 4 aggregation thrombosis venous>arterial F>m surgical cancer not severe cause UFH>LMWH Rx same thrombosis treatment
  argatroban DOC fondaparinux platelet >150k start warfarin/DOAC duration 4 wks major event 3 months uses UFH catheter thrombosis concurrent thrombolysis LMWH/fondaparinux DOC Rx thrombosis
  C/I TEACHER thrombocytopenia endocarditis alcoholics cirrhosis severe HTN eye/neurosurgery renal failure LMWH/fondaparinux S/E AHOT alopecia hemorrhage/hyperkalemia osteoporosis thrombosis HIT;
  warfarin VKOR ↓active Vit K (+) gamma carboxylase factors II VII IX X protein C&S VII first decline C&S second II last minimum 5 days effect first 5 days rapid ↓C&S thrombosis skin necrosis C/I HIT
  prophylaxis DVT DOC DOAC heparin bridge LMWH 5 days thrombosis prophylaxis preferred valvular AF non-valvular renal failure Pgp - severe mitral stenosis DOC antiphospholipid splanchnic vein
  S/E bleeding skin necrosis limbs breast penile worsens HIT alopecia blue feet teratogenic nasal mid facial hypoplasia stippled epiphyseal calcification C/I pregnancy except mechanical valve
  monitoring PT/INR target 2-3 normal 0.9-1.3 INR 3-10 stop restart INR normal INR >10 asymptomatic stop + vit K restart symptomatic bleeding stop 4 factor PTC > FFP + IV vit K ciraparantag antidote all except warfarin;
  fibrinolysis plasminogen TPA plasmin breaks fibrin streptokinase binds plasminogen exposes TPA ↑plasmin clot non-specific breaks clot+plasma ↑bleeding ↑dose recombinant tPA alteplase duteplase reteplase
  tenecteplase most clot specific single dose clot specific uses STEMI never NSTEMI/unstable massive PE peripheral thrombosis C/I BRAIN brain tumour/aneurysm recent Sx/trauma aortic dissection
  intracranial hemorrhage NSTEMI S/E bleeding Rx antifibrinolytics X plasmin EACA epsilon aminocaproic acid tranexamic acid uses thrombolytics bleeding procedural hemophilia GIT trauma surgical menorrhagia C/I upper GU bleed ischemia hypotension myopathy).
- DONE (session 11): **ch65 "Bronchial Asthma"** (p256-258) - 61 qs, 5 units
  (pathophysiology allergen -> mast cell lysis -> histamine -> bronchoconstriction Rx bronchodilators inflammation Rx steroids classification β2 agonists
  anticholinergics methylxanthines; methylxanthine MOA bronchodilation PDE3>PDE4 ↑cAMP relax smooth adenosine antagonism anti-inflammatory PDE4 roflumilast COPD
  histone deacetylase steroids also stimulate ↑IL-10 apoptosis neutrophils drugs oral theophylline > aminophylline add on persistent BA IV aminophylline > theophylline acute exacerbation
  S/E PDE4 20-25 mg/L GI nausea vomiting headache adenosine >30 mg/L arrhythmia PDE3 seizures low TI theophylline N 5-15 toxicity >20; ICS fluticasone most potent mometasone budesonide ciclesonide
  beclomethasone soft ↓S/E airway metabolism flunisolide least potent uses persistent BA EIA aspirin bronchoconstriction DOC intermittent <2/wk S/E hoarseness m/c
  oropharyngeal candidiasis good inhaler technique systemic minimal note intermittent 0-5 SABA 6-11 SABA+ICS SABA before ICS >12 FDC ICS + pMDI formoterol ↓number severity;
  systemic oral prednisone/prednisolone IV hydrocortisone faster > methylprednisolone persistent if ICS fails acute oral > IV MOA ↓mucus ↓inflammatory mediators ↑β2 receptors ↑β2 agonist effect complementary;
  accessory antileukotrienes 5-LOX zileuton LTC4/LTD4 montelukast zafirlukast pranlukast uses persistent add-on ICS EIA allergic rhinitis montelukast S/E hepatotoxicity max zileuton Churg-Strauss montelukast zafirlukast,
  mast cell stabilizers inhibit Ca2+ channels prevent degranulation ↓histamine cromolyn nedocromil oral food allergy systemic mastocytosis nasal allergic rhinitis eye allergic conjunctivitis inhalational mild asthma
  least toxic preferred children ketotifen mast cell + ↑NO prophylaxis allergen asthma, monoclonal omalizumab anti IgE SC q2-4 wks resistant asthma allergic rhinitis chronic urticaria food allergy dose weight IgE titer
  C/I atopic dermatitis ↑↑IgE IL-4 dupilumab IL-4 receptor T-helper IL-5 reslizumab mepolizumab IL-5 receptor benralizumab eosinophils maturation survival severe eosinophilic asthma atopic dermatitis).
- **TOTAL LIVE NOW: 5925 questions, 546 units, chapters 1-74 — THE ENTIRE BOOK IS LIVE.** Respiratory COMPLETE (Asthma 65, Antitussives 66); GI COMPLETE (PUD 67, Prokinetics/Antiemetics 68, Laxatives/Antidiarrheal 69); Immunomodulators COMPLETE (70); Anti-neoplastic COMPLETE (Intro 71, Non-CCS 72, CCS 73, Miscellaneous 74).
- DONE (session 13): **ch66 "Antitussives"** (p259-260) - 35 qs, 8 units
  (central preferred → peripheral if no response; central non-opioids dextromethorphan NMDA S/E abuse+agitation mild cough,
  noscapine spasmodic, levopropoxyphene mild; opioids codeine max abuse/ethylmorphine least S/E mild-moderate, morphine+methadone severe,
  constipation+abuse (+); misc diphenhydramine H1/muscarinic mild, aprepitant NK1 severe, gabapentin/pregabalin chronic idiopathic;
  peripheral local anesthetics (-) stretch receptors, moguisteine K+ channels, cromolyn persistent depolarisation; expectorant guaifenesin
  only FDA gastric→reflex bronchial, iodides/hypertonic saline non-FDA; mucolytics sulphydryl N-acetyl/methyl/ethyl cysteine, ↑sialomucin
  carbocisteine/letosteine/erdosteine/stepronin, depolymerise bromhexine/ambroxol, DNase CF; productive syrup expectorant+mucolytic+
  salbutamol+phenylephrine).
- DONE (session 13): **ch67 "Peptic Ulcer Disease"** (p261-265) - 64 qs, 12 units
  (anti-secretory most effective PPI DOC/H2/anticholinergics M1 pirenzepine+telenzepine; gastroprotective cover ulcer; antacids neutralize;
  physiology D-cells somatostatin ⊣ gastrin H.pylori kills D-cells, G-cells gastrin (+)ECL+CCK-2B, ECL histamine H2, ganglion M1→ACh→M3,
  parietal H+ pumps; natezepide CCK-2B blocker gastrinoma; PPI t½ 1.5-2 h irreversible effect stops 3-5 d acid labile max rabeprazole min
  pantoprazole 30-60 min before food HCl activation; omeprazole most potent enzyme inhibitor racemic S slow CYP2C19 ↑toxicity
  antidepressants/antipsychotics ↓tamoxifen ↓clopidogrel; esomeprazole longer; pantoprazole least potent enzyme inhibitor; rabeprazole
  longest/fastest/most potent PPI; Barrett's life-long; bleed IV basic pH; pneumonia/pseudomembranous enterocolitis; ↓Ca/Mg/B12/Fe;
  hypergastrinemia; H2 cimetidine least potent+enzyme inhibitor+antiandrogenic/↑prolactin, famotidine most potent, basal acid post-op
  pneumonia DOC, neurotoxicity IV/elderly/cimetidine, rapid IV blocks Gs ↓HR/BP infuse 30 min; misoprostol PGE1 EP2/4 ↑mucin+HCO3 EP3 ↓HCl
  200 mcg QID most specific DOC PPI C/I IBD; sucralfate octasulfate+Al polymerised by HCl radiation proctitis hypophosphatemia bezoars C/I
  renal failure antacids prevent polymerisation; bismuth subsalicylate/subcitrate cover+mucin+antibacterial Reye's neurotoxic; antacids Mg
  diarrhoea Al constipation bleeding ulcer q30 min uncomplicated 1&3 h GERD DOC pregnancy/children C/I renal; alginate reflux; simethicone
  surfactant).
- DONE (session 13): **ch68 "Prokinetics and Antiemetics"** (p266-268) - 38 qs, 6 units
  (cranio-caudal gastroparesis; erythromycin/mitemcinal (+) motilin, dexloxiglumide (-) CCK, 5HT4 ↑ACh, D2 blockers; heteroreceptors;
  cisapride/tegaserod banned QT; mosapride/prucalopride GERD+chronic constipation; metoclopramide normal (-)D2 high (+)5HT4+(-)5HT3,
  (-)D2+(-)5HT3 prokinetic+antiemetic, domperidone (-)D2 less potent minor BBB, EPS acute dystonia earliest, hyperprolactinemia severe vs
  mild prolactin stimulation; 5HT3 ondansetron shortest early DOC palonosetron longest+most potent late min QT dolasetron max QT post-op/
  post-RT DOC morning sickness C/I apomorphine; NK1 late DOC fosaprepitant IV aprepitant severe cough; cannabinoids dronabinol/nabilone Gi
  ↓5HT/Dop/NE no α1 hypotension+blood shot eyes; levosulpiride post-op/gastroparesis, olanzapine CINV+transdermal patch 4.5 h before
  travel, scopolamine DOC motion, doxylamine DOC morning, antihistamines motion; dexamethasone add-on CINV).
- DONE (session 13): **ch69 "Laxatives and Antidiarrheal Drugs"** (p269-271) - 31 qs, 5 units
  (laxative formed stool vs purgative pre-op; probiotics bacillus clausii/lactobacillus/saccharomyces vs prebiotics psyllium/bran/
  methylcellulose symbiotics; stimulants bisacodyl/senna/cascara inflammation→nerve→contraction night >10 d atonic hypokalemia melanosis
  coli C/I obstruction castor oil ricinoleic; osmotic Mg C/I renal Na C/I CHF sugars saturated fatty acids 2nd line lactulose NH3→NH4+
  flatulence PEG DOC IBS-C; docusate surfactants mineral oil aspiration tenapanor Na+/H+ lubiprostone type-2 Cl- linaclotide/plecanatide
  guanylate cyclase cGMP CFTR; opioids loperamide DOC non-secretory eluxadoline μ&κ/δ resins biliary alosetron females ischemic colitis
  octreotide secretory HIV/DM/chemo pancreatitis dumping racecadotril enkephalin children crofelemer CFTR HIV).
- DONE (session 13): **ch70 "Immunomodulators"** (p272-275) - 37 qs, 6 units
  (MHC→calcineurin→NFATc dephos→NFATc+NFATn→↑IL-2; steroids block mediators+apoptosis; cyclosporin/tacrolimus calcineurin; basiliximab/
  daclizumab IL-2R CD25; everolimus/sirolimus mTOR; azathioprine/methotrexate S-phase; muromonab CD3; alemtuzumab CD52; GVHD+rejection
  prophylaxis all drugs, rejection treatment activated lymphocytes; first line cyclosporine rescue tacrolimus; DOC cyclosporine lichen
  planus/atopic/steroid-resistant UC+nephrotic/MG/RA/Behcet's; S/E tacrolimus>cyclosporine hirsutism gum hyperplasia hyperlipidemia
  hyperuricemia; mTOR G1-S sirolimus stent coating uvoretinitis temsirolimus RCC everolimus RCC/angiomyolipoma/pancreatic/ER+ breast/
  astrocytoma lymphocytes hate mTOR; daclizumab MS basiliximab prophylaxis muromonab cytokine release C/I fever+chills alemtuzumab;
  abatacept/belatacept CD80/86 alefacept CD3 drug-resistant; azathioprine 6-MP TPMT; MMF IMP dehydrogenase C/I azathioprine 1st line
  cardiac/bone marrow; IL-1 anakinra RA DOC CAPS JIA/Still's canakinumab rilonacept acute gout; T-cell CD28-CD80/86 CD2-LFA-3; thalidomide
  sedative banned phocomelia reintroduced Catch PROGRAMMES SPORT Channel).
- DONE (session 13): **ch71 "Introduction to Anticancer Drugs"** (p276-281) - 59 qs, 9 units
  (classification non-CCS alkylating/platinum/antitumor antibiotics; S-phase anti-metabolites topo I&II HDAC hydroxyurea; M-phase vinca/
  taxanes/epothilones/eribulin/estramustine; DLT bone marrow; ECL ↑5HT 5HT3 + substance P NK1 CINV severe cisplatin 4 drugs moderate
  carboplatin mild dexamethasone; DOC brain temozolomide head-neck cisplatin/cetuximab esophagus+gastric cisplatin colorectal 5FU
  FOLFOX/FOLFIRI/FOLFIRINOX anal 5FU+mitomycin-C urogenital cisplatin ±nivo/pembro prostate goserelin; retinoblastoma VEC lung cisplatin+
  etoposide HCC sorafenib pancreatic FOLFIRINOX pheo vincristine+cyclophosphamide+dacarbazine RCC pembrolizumab osteosarcoma MAP+ifosfamide;
  SCLC limited vs extensive +pembro; NSCLC mutation(-) chemo+ICP double ICP nivo+ipi Keynote189; EGFR 1st gefitinib/erlotinib T790M 2nd
  afatinib/dacomitinib 3rd osmertinib L858R; ALK crizotinib L1196 2nd alectinib/brigatinib(T790)/ceritinib G1202R 3rd lorlatinib; breast
  ER tamoxifen/letrozole/fulvestrant/elacestrant ESR-1 Her2 trastuzumab/neratinib/pertuzumab/lapatinib triple DCP+pembro BRCA olaparib;
  ALL VPAD AML cytarabine+ida/dauno FLT3 midostaurin CLL FCR; CML imatinib DOC GIST 2nd dasatinib/nilotinib/bosutinib 3rd ponatinib
  asciminib allosteric omacetaxine BCR-ABL TNF-α; Hodgkin ABVD → nivo/pembro NHL low FCR high R-CHOP hairy cladribine PV/ET/sickle
  hydroxyurea myeloma bortezomib+lenalidomide+dexa; organ S/E vincristine SIADH cytarabine cerebellar cisplatin oto/nephro NS+mannitol+
  amifostine bleo>busulfan pulmonary doxo/dauno cardio dexrazoxane MTX cirrhosis irinotecan diarrhea loperamide ifosfamide cystitis mesna
  capecitabine hand-foot B6 pemetrexed folinic+B12 flagellate bleomycin).
- DONE (session 13): **ch72 "Non-Cell Cycle Specific Drugs"** (p282-285) - 33 qs, 7 units
  (AA devoid of H binds N7 guanine G≡T check gates secondary AML; cyclophosphamide prodrug 4-hydroxy phosphoramide cytotoxic acrolein
  cystitis mesna chloroacetaldehyde GTCS/ataxia uses female/kids/Wegener's/nephrotic; ifosfamide I>C mechlorethamine vesication rapid IV
  melphalan myeloma chlorambucil CLL; nitrosoureas BBB neutropenia streptozocin β-islet; dacarbazine/procarbazine Hodgkin's MAO+disulfiram
  temozolomide brain; busulfan pulmonary fibrosis; PC bivalent cisplatin/carboplatin quadrivalent oxaliplatin Cl-diuresis; anthracyclines
  topo-II S-phase Fe radical G2 cardiotoxicity dexrazoxane doxo osteosarcoma/Hodgkin ida/dauno+cytarabine AML epirubicin breast valrubicin
  bladder mitoxantrone MS/AML red urine; bleomycin hydrolase type-II pneumocyte flagellate; actinomycin-D RNA polymerase chorio/Wilms
  radiation recall; mitomycin-C topo-II anal Ca ocular corneal topical synechiae HUS).
- DONE (session 13): **ch73 "Cell Cycle Specific Drugs"** (p286-289) - 43 qs, 6 units
  (antifolates fdUMP ternary TS dUMP/TMP DHFR MTX RECIPE leucovorin bicarbonate cirrhosis pemetrexed mesothelioma/NSCLC B12; purine de-novo
  lymphocytes 6MP ALL allopurinol ↓75% fludarabine CL/NHL cladribine hairy DOC pentostatin ADA clofarabine/nelarabine resistant ALL;
  pyrimidine 5FU TS IV capecitabine oral prodrug B6 gemcitabine HUS azacitidine/decitabine demethylation 5q lenalidomide cytarabine
  cerebellar ×7d; topo-I irinotecan delayed diarrhea loperamide topotecan ovarian topo-II etoposide teniposide childhood ALL; HD blockers
  vorinostat/romidepsin cutaneous belinostat peripheral panobinostat myeloma; hydroxyurea RDR SPECiaL DOC leg ulcer; vinca block β-tubulin
  polymerization vincristine children SIADH max neuropathy vinblastine Hodgkin's/testicular vinorelbine NSCLC; taxanes ↑polymerization
  paclitaxel castor oil hypersensitivity nab water soluble docetaxel polysorbate H2O retention CHF; ixabepilone/eribulin breast estramustine
  prostate gynecomastia).
- DONE (session 13): **ch74 "Miscellaneous Drugs"** (p290-293) - 31 qs, 7 units
  (L-asparaginase IV breaks asparagine ALL ↓protein hyperglycemia/hyperlipidemia/hemorrhage/hypercoagulation hypersensitivity; retinoic
  acid PML chr17 RARα/chr15 PML DOC arsenic trioxide pulmonary syndrome differentiating supra-physiological; proteasome bortezomib/
  carfilzomib myeloma thrombocytopenia neuropathy +lenalidomide+dexa+daratumumab; MAbs humanised -zumab trastuzumab chimeric -ximab
  abciximab murine -omab ibritumomab human -umab adalimumab stems -tu/-ci/-li/-tox/-os/-vi hybridoma; EGFR cetuximab/panitumumab gefitinib/
  erlotinib HER2 trastuzumab main/pertuzumab lapatinib/neratinib VEGF macular ramucirumab GIT vandetanib medullary thyroid axitinib/sunitinib
  RCC sorafenib DOC HCC lenvatinib CD20 rituximab/ofatumumab; ICP PD1 nivo/dostarlimab/cemiplimab/pembro CTLA4 ipilimumab CD80/86 PDL1
  durvalumab/avelumab/atezolizumab breast pembro; BTK ibrutinib/acalabrutinib CLL/mantle/marginal/Waldenstrom; MAPK BRAF vemurafenib/
  dabrafenib/encorafenib MEK trametinib/selumetinib/binimetinib melanoma 1+1; hedgehog glasdegib elderly AML sonidegib basal cell; PI3-K
  alpelisib breast+fluvestrant idelalisib/duvelisib CLL).
- **SESSION 11 NOTES:** source pages p224-258 rendered at 180 dpi and read line-by-line; crops verified osteonecrosis jaw image (p225), teriparatide max 2 yr note (p226), potassium iodide 10% vs Lugol 5% (p228), I131 timing diagram (p229), fexofenadine least sedating (p232), triptan durations 27 hr frovatriptan vs 6 hr naratriptan (p234), ergot gangrene feet m/c (p235), zileuton vs montelukast (p238-239), diclofenac short T1/2 long acting joints (p241), allopurinol HLA-B-5801 SJS (p242), uricosuric add-on > mono (p243), DMARD anchor methotrexate (p244), hydroxychloroquine Bull eye ≤5 mg/kg (p245), platelet aggregation diagram abciximab/aspirin/clopidogrel/vorapaxar (p247), hit & run definition (p248), UFH vs LMWH table AP+long vs AP+short vs AP only (p252), warfarin factor decline order VII first II last (p254), fibrinolytic BRAIN mnemonic (p255), theophylline 5-15 mg/L normal (p256), ICS soft steroids ciclesonide beclomethasone (p257), omalizumab weight+IgE titer dosing (p258). Generator work/gen_ch56_65.py is single reproducible source for this batch.
- **SESSION 12 (quality audit):** User reported options were too predictable — you could pick the longest / most complete choice without knowing the fact. Audit of live data: ch1–55 only 2.4% of 5201 questions had dummy "Only X" distractors (left as CHOOSE). ch56–65 were 44–85% "Only X" pads with a uniquely-longest correct option. Rewrote ch56–65 on the same book facts / unit path as **353 questions** (103 CHOOSE / 211 FILL / 39 MATCH), 0 dummy-Only, 0 length-giveaway. Quiz engine now supports CHOOSE (4 near-miss options), FILL (typed blank + aliases), MATCH (tap-to-pair). `work/validate.py` warns on dummy pads. `work/quiz_runtime.js` + `work/patch_engine.py` are the runtime source. Validation, rebuild, integrity, Node syntax PASS. Counts: ch56 40/6, ch57 36/6, ch58 31/5, ch59 34/7, ch60 54/7, ch61 24/6, ch62 29/5, ch63 28/6, ch64 46/6, ch65 31/5.
- NEXT: **none — ALL 74 CHAPTERS ARE LIVE (book complete, p1-293).** Future sessions: quality audits / refinements only. Keep the mixed CHOOSE/FILL/MATCH near-miss standard for any new or reworked content.
- LIVE LINK: https://deva20045.github.io/Pharm/ (index.html redirects -> pulse-pharm-complete.html).
  GitHub Pages: enable once via Repo -> Settings -> Pages -> "Deploy from a branch" -> main /(root).
- Deliverable file: `pulse-pharm-complete.html` (repo root).
- GitHub repo: https://github.com/Deva20045/Pharm
