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
31: 123-126 | 32: 127-130 | 33: 131-133 |
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

## Status  (last updated: 2026-09-14, session 6)
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
- **TOTAL LIVE NOW: 2952 questions, 227 units, chapters 1-30.** General Pharmacology, Autonomic Nervous System, Cardiovascular System and Renal System are COMPLETE; Central/Peripheral Nervous System chapters 28-30 are live.
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
- NEXT: **ch31 "Opioids: Part 1"** (book p123-126 = pdf p128-131), then ch32 Opioids: Part 2 (127-130),
  ch33 (131-133) ... (Continue Central and Peripheral Nervous System).

- LIVE LINK: https://deva20045.github.io/Pharm/ (index.html redirects -> pulse-pharm-complete.html).
  GitHub Pages: enable once via Repo -> Settings -> Pages -> "Deploy from a branch" -> main /(root).
- Deliverable file: `pulse-pharm-complete.html` (repo root).
- GitHub repo: https://github.com/Deva20045/Pharm
