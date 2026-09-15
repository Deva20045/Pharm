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
51: 207-210 DONE (70 qs, 8 units) | 52: 211-214 DONE (77 qs, 9 units) | 53: 215-217 DONE (51 qs, 8 units) | 54: 218-220 DONE (42 qs, 3 units) | 55: 221-223 DONE (54 qs, 5 units) | 56: 224-226 | 57: 227-229
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
- NEXT: **ch56 (book p224-226)** and ch57 (p227-229) to finish the Endocrine System, then Autacoids.
- LIVE LINK: https://deva20045.github.io/Pharm/ (index.html redirects -> pulse-pharm-complete.html).
  GitHub Pages: enable once via Repo -> Settings -> Pages -> "Deploy from a branch" -> main /(root).
- Deliverable file: `pulse-pharm-complete.html` (repo root).
- GitHub repo: https://github.com/Deva20045/Pharm
