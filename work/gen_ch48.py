# -*- coding: utf-8 -*-
import json
CH = 48
Q = []
UNITS = []
cur = None

def unit(title, guide):
    global cur
    if cur:
        end()
    cur = {"title": title, "start": len(Q) + 1, "guide": guide}

def q(page, text, opts, exp):
    assert cur is not None and len(opts) == 4
    suffix = f"(Book p{page})"
    exp = exp.rstrip()
    if not exp.endswith(suffix):
        exp = f"{exp} {suffix}"
    Q.append({"id":"", "sec":cur["title"], "page":page, "q":text, "opts":opts, "ans":0, "exp":exp})

def end():
    global cur
    if cur is None:
        return
    cur["end"] = len(Q)
    UNITS.append(cur)
    cur = None

unit("First-Line Anti-TB Drugs: Mycolic Acid Pathway", "Isoniazid is a pro-drug: the kat-G gene makes catalase peroxidase, which converts Inh into activated Inh(a). Inh(a) hits the acyl protein reductase step, the same step targeted by ethionamide; the kas-A gene controls the acyl protein kinase step. Both steps feed mycolic acid synthesis, which builds the mycobacterial cell wall - the shared target of the first-line drugs.")
q(193, "First-line anti-TB drugs ultimately act on the mycobacterial:", ["Cell wall via mycolic acid synthesis", "Ribosome", "DNA gyrase", "ATP synthase only"], "The diagram funnels acyl protein reductase and kinase into mycolic acid synthesis, which forms the cell wall.")
q(193, "The gene whose product activates isoniazid is:", ["Kat-G gene", "Kas-A gene", "Inh-A gene", "rpo-B gene"], "The diagram shows kat-G gene feeding catalase peroxidase, which activates Inh to Inh(a).")
q(193, "The enzyme that converts isoniazid (Inh) to activated Inh(a) is:", ["Catalase peroxidase", "Pyrazinamidase", "Arabinosyl transferase", "RNA polymerase"], "The flow: Inh - via catalase peroxidase - becomes Inh(a).")
q(193, "Activated isoniazid Inh(a) acts on which enzyme step?", ["Acyl protein reductase", "Acyl protein kinase", "RNA polymerase", "Dihydropteroate synthase"], "Inh(a) in the diagram points to the acyl protein reductase step.")
q(193, "Ethionamide in the pathway diagram targets:", ["Acyl protein reductase", "Catalase peroxidase", "Myobacterial ATP synthase", "Arabinosyl transferase"], "Ethionamide is drawn pointing at acyl protein reductase.")
q(193, "The gene controlling the acyl protein kinase step is:", ["Kas-A gene", "Kat-G gene", "pnc-A gene", "emb-B gene"], "The diagram labels kas-A gene at acyl protein kinase.")
q(193, "The Inh-A gene in the pathway diagram is linked to:", ["Acyl protein reductase", "Acyl protein kinase", "Catalase peroxidase", "Pyrazinamidase"], "The third label (Inh-A gene) points to acyl protein reductase.")

unit("First-Line Anti-TB Drugs: MOA and Resistance", "Each first-line drug has a signature mechanism and a signature resistance mutation: H inhibits mycolic acid synthesis (kat-G mutation is most severe; inh-A overexpression causes cross-resistance to ethionamide), R inhibits RNA polymerase (rpo-B mutation), Z is activated by pyrazinamidase (pnc-A gene) to pyrazinoic acid, which inhibits fatty acid synthesis in acidic pH (pnc-A mutation confers resistance), and E inhibits arabinosyl transferase (emb-B mutation).")
q(193, "The MOA of isoniazid is:", ["Inhibits mycolic acid synthesis, inhibiting cell wall", "Inhibits RNA polymerase", "Inhibits arabinosyl transferase", "Inhibits folate synthesis"], "The H column: inhibits mycolic acid synthesis leading to inhibited cell wall.")
q(193, "Rifampicin acts by inhibiting:", ["RNA polymerase", "DNA polymerase", "Mycolic acid synthesis", "Fatty acid synthesis"], "The R column states inhibits RNA polymerase.")
q(193, "Pyrazinamide is converted to its active form by:", ["Pyrazinamidase (pnc-A gene)", "Catalase peroxidase", "Albumin", "Xanthine oxidase"], "The Z column flow: pyrazinamide - pyrazinamidase (pnc-A gene) - pyrazinoic acid.")
q(193, "Pyrazinoic acid acts best in which pH and by what action?", ["Acidic pH; inhibits fatty acid synthesis", "Alkaline pH; inhibits RNA polymerase", "Neutral pH; inhibits DHPS", "Acidic pH; inhibits ATP synthase"], "The Z flow shows acidic pH, then pyrazinoic acid inhibiting fatty acid synthesis.")
q(193, "Ethambutol inhibits:", ["Arabinosyl transferase", "RNA polymerase", "Pyrazinamidase", "Mycobacterial ATP synthase"], "The E column: inhibits arabinosyl transferase.")
q(193, "The MOST severe resistance mutation among first-line drugs is:", ["Kat-G gene mutation", "rpo-B gene mutation", "pnc-A gene mutation", "emb-B gene mutation"], "The resistance row: kat-G gene mutation - most severe.")
q(193, "Isoniazid resistance by inh-A gene overexpression causes cross-resistance to:", ["Ethionamide", "Rifampicin", "Pyrazinamide", "Streptomycin"], "The H column: inh-A gene overexpression leads to cross resistance to ethionamide.")
q(193, "Rifampicin resistance is due to mutation of the:", ["rpo-B gene", "kat-G gene", "inh-A gene", "kas-A gene"], "The R resistance cell: rpo-B gene mutation.")
q(193, "Pyrazinamide resistance occurs via mutation of:", ["pnc-A gene", "emb-B gene", "rpo-B gene", "kat-G gene"], "The Z resistance cell: pnc-A gene mutation.")
q(193, "Ethambutol resistance is due to:", ["emb-B gene mutation", "pnc-A gene mutation", "kat-G gene mutation", "rpo-B gene mutation"], "The E resistance cell: emb-B gene mutation.")

unit("First-Line Anti-TB Drugs: Cidal/Static, Site, Spectrum, Excretion", "H is cidal and the first drug to make patients non-infective; R is cidal with maximum activity; Z is cidal; E is static. H and R act both intracellular and extracellular, Z is only intracellular, E only extracellular. H, Z and E act on replicating bacteria while R also kills non-replicating persisters (R greater than Z). All except E are excreted via liver; R has maximum hepatic excretion and is safest in renal failure, whereas E is renal and most unsafe in renal failure.")
q(194, "The first drug to make TB patients non-infective is:", ["Isoniazid", "Rifampicin", "Pyrazinamide", "Ethambutol"], "The H cidal cell: cidal, 1st drug to make patients non infective.")
q(194, "Which first-line anti-TB drug is cidal with MAXIMUM effect?", ["Rifampicin", "Isoniazid", "Pyrazinamide", "Ethambutol"], "The R cell: cidal (maximum).")
q(194, "The bacteriostatic first-line anti-TB drug is:", ["Ethambutol", "Isoniazid", "Rifampicin", "Pyrazinamide"], "The E cell reads static while H, R and Z read cidal.")
q(194, "Which first-line anti-TB drug acts ONLY intracellularly?", ["Pyrazinamide", "Isoniazid", "Rifampicin", "Ethambutol"], "The site-of-action row marks Z intracellular alone.")
q(194, "The first-line anti-TB drug acting only extracellularly is:", ["Ethambutol", "Pyrazinamide", "Isoniazid", "Rifampicin"], "The E site-of-action cell is extracellular.")
q(194, "Which pair acts both intracellular and extracellular?", ["Isoniazid and rifampicin", "Pyrazinamide and ethambutol", "Isoniazid and ethambutol", "Rifampicin and ethambutol"], "The site row: H and R are intracellular + extracellular.")
q(194, "Rifampicin acts on replicating bacteria plus:", ["Non-replicating bacteria (persisters), R > Z", "Only dormant spores", "Only intracellular macrophage forms", "Biofilm forms only"], "The R spectrum cell: replicating bacteria + non-replicating bacteria (persisters) R>Z.")
q(194, "Regarding persister (non-replicating) bacteria, the comparison written is:", ["R > Z", "Z > R", "H > R", "E > Z"], "The note in the R spectrum cell writes R>Z.")
q(194, "Ethambutol is active against:", ["Replicating bacteria", "Non-replicating persisters", "Both replicating and non-replicating", "Spores only"], "The E spectrum cell: replicating bacteria.")
q(194, "The organ of excretion of isoniazid and pyrazinamide is:", ["Liver", "Kidney", "Lung", "Bile only"], "The excretion row: H liver, Z liver.")
q(194, "The first-line anti-TB drug with MAXIMUM hepatic excretion and safest profile in renal failure is:", ["Rifampicin", "Ethambutol", "Pyrazinamide", "Isoniazid"], "The R excretion cell: liver, maximum excretion, safest in renal failure.")
q(194, "The first-line anti-TB drug MOST unsafe in renal failure is:", ["Ethambutol", "Rifampicin", "Isoniazid", "Pyrazinamide"], "The E excretion cell: kidney (most unsafe in renal failure).")

unit("First-Line Anti-TB Drugs: Side Effects", "H lowers pyridoxine: hemolytic anemia, low GABA with seizures, plus neuropathies, hallucination, memory loss and euphoria; seizure toxicity is treated with IV pyridoxine 1 g per gram of isoniazid (maximum 5 g). R gives red-orange discoloration of urine and secretions (contact lens staining), flu-like respiratory symptoms with intermittent dosing, pulmonary syndrome and purpura (both must be stopped permanently), and induces enzymes - least with rifabutin, which causes uveitis. Z is the most hepatotoxic (Z > H > R > E) and causes hyperuricemia, arthralgia and peripheral neuropathy. E causes optic neuritis with red-green color blindness, green affected more than red. Rifapentine plus isoniazid is a once-weekly prophylaxis for latent TB.")
q(194, "Isoniazid-induced neuropathy and seizures are due to deficiency of:", ["Vitamin B6 (pyridoxine)", "Vitamin B1", "Vitamin B12", "Folic acid"], "The H side-effect block starts with down arrow Vit B6 (pyridoxine).")
q(194, "Isoniazid lowers hemoglobin causing anemia, and lowers GABA causing:", ["Seizure", "Optic neuritis", "Hyperuricemia", "Flu-like syndrome"], "The H block: down haem leads to anemia; down GABA leads to seizure.")
q(194, "Neuropathies, hallucination, memory loss and euphoria are side effects of:", ["Isoniazid", "Ethambutol", "Rifampicin", "Pyrazinamide"], "These are listed in the isoniazid side-effect column.")
q(194, "Treatment of isoniazid toxicity (seizure) is:", ["IV pyridoxine 1 g for each gram of isoniazid", "IM thiamine 100 mg", "Oral folic acid 5 mg", "Naloxone IV"], "The other-features cell: IV pyridoxine 1 g for each gm of Inh.")
q(194, "The maximum dose of IV pyridoxine written for isoniazid toxicity is:", ["5 g", "1 g", "10 g", "500 mg"], "The note: max dose of IV pyridoxine 5 g.")
q(194, "Contact lens staining with an anti-TB drug is due to:", ["Red/orange secretion with rifampicin", "Crystals in GIT mucosa", "Ichthyosis", "Optic neuritis"], "The R block: red/orange - urine, secretion (contact lens staining).")
q(194, "Flu-like respiratory symptoms with intermittent dosing are seen with:", ["Rifampicin", "Isoniazid", "Ethambutol", "Clofazimine"], "The R block item 2: respiratory symptoms, flu like (intermittent dosing).")
q(194, "Rifampicin side effects that require STOPPING the drug PERMANENTLY are:", ["Pulmonary syndrome and purpura", "Red urine and flu-like symptoms", "Uveitis only", "Hyperuricemia"], "Items 3 and 4 in the R block are marked stop permanently: pulmonary syndrome and purpura.")
q(194, "Rifampicin purpura occurs due to:", ["Decreased platelets", "Hemolysis", "Optic nerve damage", "Gout"], "The R block: purpura (down platelets).")
q(194, "Rifampicin reduces effects of other drugs because it is an enzyme inducer; this is LEAST with:", ["Rifabutin", "Rifapentine", "Isoniazid", "Ethionamide"], "Item 5: enzyme inducer, least with rifabutin (S/E: uveitis).")
q(194, "The side effect specific to rifabutin written is:", ["Uveitis", "Optic neuritis", "Red man syndrome", "Ichthyosis"], "The parenthetical: rifabutin (S/E: uveitis).")
q(194, "The correct hepatotoxicity ranking among first-line anti-TB drugs is:", ["Z > H > R > E", "H > Z > R > E", "R > Z > H > E", "E > R > H > Z"], "The Z column: most hepatotoxic: Z > H > R > E.")
q(194, "Hyperuricemia and arthralgia are side effects of:", ["Pyrazinamide", "Ethambutol", "Rifampicin", "Isoniazid"], "The Z column lists hyperuricemia and arthralgia.")
q(194, "Peripheral neuropathy as a direct listed side effect (not via B6 deficiency) is seen with:", ["Pyrazinamide", "Rifampicin", "Ethambutol", "Rifabutin"], "The Z column item 4: peripheral neuropathy.")
q(194, "Ethambutol eye toxicity includes:", ["Optic neuritis and red-green color blindness (green > red)", "Only pupillary constriction", "Cataract and retinal detachment", "Uveitis and keratitis"], "The E column: optic neuritis, red green colour blindness (green > red).")
q(194, "In ethambutol color blindness, the color pair affected with the more affected color is:", ["Red-green, green more than red", "Blue-yellow, blue more", "Red-green, red more than green", "Only blue is affected"], "The E note writes red green colour blindness (green > red).")
q(194, "Rifapentine with isoniazid is used for:", ["Prophylaxis/latent TB, once weekly", "MDR-TB, thrice daily", "XDR-TB, once monthly", "MAC infection, daily"], "The other-features cell: rifapentin with Inh - prophylaxis/latent TB, once weekly.")

unit("Second-Line Anti-TB Drugs: Groups A, B, C", "Second-line drugs treat resistant TB. Group A includes all three: levofloxacin or moxifloxacin, bedaquiline and linezolid. Group B includes one or both: clofazimine, and cycloserine or terizidone. Group C is used when A or B cannot be added: ethambutol, delamanid, pyrazinamide, imipenem-cilastatin or meropenem, amikacin or streptomycin, ethionamide or prothionamide, and PAS.")
q(195, "Second-line anti-TB drugs are used in:", ["Resistant TB", "All new TB cases", "Latent TB only", "TB with pregnancy"], "The use line: resistant TB.")
q(195, "Which of the following belongs to Group A of second-line drugs?", ["Linezolid", "Clofazimine", "Ethambutol", "Cycloserine"], "Group A: levofloxacin/moxifloxacin, bedaquiline, linezolid.")
q(195, "The fluoroquinolones in Group A are:", ["Levofloxacin or moxifloxacin", "Ofloxacin or ciprofloxacin", "Norfloxacin or gatifloxacin", "Ciprofloxacin or sparfloxacin"], "Group A lists levofloxacin (Lfx) or moxifloxacin (Mfx).")
q(195, "Group B second-line drugs include:", ["Clofazimine and cycloserine or terizidone", "Bedaquiline and linezolid", "Delamanid and PAS", "Amikacin and ethambutol"], "Group B: include 1 or both drugs - clofazimine, cycloserine or terizidone.")
q(195, "Group C second-line drugs are used when:", ["Group A or B cannot be added", "Patient is pregnant", "TB is drug-sensitive", "Hepatitis develops"], "The Group C header: used when group A or B cannot be added.")
q(195, "Which carbapenems are listed in Group C?", ["Imipenem-cilastatin or meropenem", "Ertapenem or doripenem", "Faropenem only", "No carbapenem is listed"], "Group C: imipenem-cilastatin (Ipm-cln) or meropenem (mpm).")
q(195, "The aminoglycosides listed in Group C are:", ["Amikacin or streptomycin", "Gentamicin or tobramycin", "Neomycin or kanamycin only", "No aminoglycoside is listed"], "Group C: amikacin (Am) or streptomycin (S).")
q(195, "The thioamides in Group C are:", ["Ethionamide or prothionamide", "Isoniazid or ethambutol", "Cycloserine or terizidone", "PAS or delamanid"], "Group C: ethionamide (Eto) or prothionamide (Pto).")

unit("New TB Drugs: Bedaquiline, Delamanid, Pretomanid", "Bedaquiline inhibits mycobacterial ATP synthase; the nitroimidazoles delamanid and pretomanid produce free radicals that kill non-replicating bacteria and inhibit mycolic acid synthesis killing replicating bacteria. All are used for MDR-TB (resistance to H+R), pre-XDR (H+R+FQ or any group A drug) and XDR-TB (H+R+FQ plus any group A drug), and should be taken with food for better absorption. Bedaquiline sequesters in tissue with a long half-life of about 65 days allowing thrice-weekly intermittent dosing; delamanid is 99% protein bound and metabolized by albumin so is C/I if albumin is below 2.8 mg/dl; pretomanid is liver-metabolized and kidney-excreted. Bedaquiline and delamanid prolong QT (C/I in arrhythmia); bedaquiline is safe in pregnancy while the nitroimidazoles are not.")
q(195, "The MOA of bedaquiline is:", ["Inhibits mycobacterial ATP synthase", "Inhibits RNA polymerase", "Produces free radicals only", "Inhibits DHPS"], "The new-drugs table: bedaquiline inhibits mycobacterial ATP synthase.")
q(195, "Delamanid and pretomanid belong to which class?", ["Nitroimidazoles", "Thioamides", "Aminoglycosides", "Oxazolidinones"], "The table groups delamanid and pretomanid under nitroimidazoles.")
q(195, "Nitroimidazoles kill non-replicating bacteria by:", ["Producing free radicals", "Inhibiting ATP synthase", "Inhibiting RNA polymerase", "Blocking arabinosyl transferase"], "The nitroimidazole block: produces free radicals - kills non-replicating bacteria.")
q(195, "Nitroimidazoles kill replicating bacteria by:", ["Inhibiting mycolic acid synthesis", "Producing free radicals", "Inhibiting ATP synthase", "Inhibiting DHPS"], "The second nitroimidazole line: inhibits mycolic acid synthesis - kills replicating bacteria.")
q(195, "MDR-TB is defined as resistance to:", ["H + R", "H + R + FQ", "H + R + FQ + any group A", "Any three group C drugs"], "The use block: MDR TB - resistance to H + R.")
q(195, "Pre-XDR-TB is resistance to:", ["H + R + FQ or any group A drug", "H + R only", "H + R + FQ + any group A", "All first-line drugs"], "The use block: pre-XDR - resistance to H + R + FQ or any group A.")
q(195, "XDR-TB is defined as resistance to:", ["H + R + FQ + any group A drug", "H + R only", "H + R + FQ or any group A", "Z + E + S"], "The use block: XDR - H + R + FQ + any group A.")
q(195, "The common advice for bedaquiline, delamanid and pretomanid is:", ["Take with food (increased absorption)", "Take on empty stomach", "Avoid milk", "Take only at bedtime"], "The advice row: drug should be taken with food (increased absorption).")
q(195, "Bedaquiline has a long half-life of about 65 days because it is:", ["Sequestered in tissue", "Excreted unchanged", "Bound to RBCs", "Resistant to metabolism"], "The PK cell: sequestered in tissue, long t-half (~65 days).")
q(195, "The intermittent dosing schedule of bedaquiline written is:", ["3 times/weekly", "Once weekly", "Once monthly", "Twice daily"], "The PK cell: intermittent dosing 3 times/weekly.")
q(195, "Delamanid plasma protein binding is:", ["99% (high)", "50%", "10%", "25%"], "The delamanid PK cell: plasma protein binding 99% (high).")
q(195, "Delamanid is contraindicated if albumin is:", ["<2.8 mg/dl", "<5 mg/dl", ">3.5 mg/dl", "<1 mg/dl"], "The PK cell: metabolized by albumin - C/I if albumin <2.8 mg/dl.")
q(195, "Pretomanid pharmacokinetics are:", ["Metabolism: liver; excreted: kidney", "Metabolism: kidney; excreted: liver", "Metabolism: lung; excreted: bile", "Not metabolized"], "The pretomanid PK cell: metabolism liver, excreted kidney.")
q(195, "The shared side effect of bedaquiline and delamanid is:", ["QT prolongation (C/I in arrhythmia)", "Hepatotoxicity", "Optic neuritis", "Hypothyroidism"], "The S/E row: both entries list QT prolongation, C/I in arrhythmia.")
q(195, "Which new TB drug is safe in pregnancy?", ["Bedaquiline", "Delamanid", "Pretomanid", "All three"], "The last row: bedaquiline safe in pregnancy; delamanid and pretomanid not safe.")

unit("Old TB Drugs and Drug Regimens", "Ethionamide inhibits mycolic acid synthesis (cidal) with hypothyroidism as its side effect; PAS inhibits DHPS (static) and is C/I with rifampicin because absorption falls. New/previously treated TB gets 2 months HRZE intensive then 4 months HRE continuous. The shorter oral bedaquiline regimen (9 months) uses Bdq for 6 months with Lfx, Cfz, Z, E plus high-dose H and Eto till 4 months, drops H/Eto in months 5-6, then continues Lfx, Cfz, Z, E months 7-9; the injectable alternative uses Mfx, Km/Am, Eto, Cfz, Z, H, E then Mfx, Cfz, Z, E. The long oral RR/XDR regimen is Bdq 6 months + Lfx, Lzd, Cfz, Cs for 18-20 months. BPaL (pilot) for MDR-TB with FQ resistance: pretomanid 200 mg OD 26 weeks, bedaquiline 400 mg OD week 1 then 200 mg thrice weekly for 24 weeks, linezolid 1200 mg OD for 24 weeks.")
q(196, "The MOA of ethionamide is:", ["Inhibits mycolic acid synthesis (cidal)", "Inhibits DHPS (static)", "Inhibits ATP synthase", "Inhibits RNA polymerase"], "The old-drugs block: ethionamide MOA inhibits mycolic acid synthesis (cidal).")
q(196, "The side effect of ethionamide is:", ["Hypothyroidism", "Hyperthyroidism", "Optic neuritis", "Hemolysis"], "The ethionamide bullet: S/E hypothyroidism.")
q(196, "PAS acts by:", ["Inhibiting DHPS (static)", "Inhibiting mycolic acid synthesis (cidal)", "Inhibiting arabinosyl transferase", "Producing free radicals"], "The PAS bullet: MOA inhibits DHPS (static).")
q(196, "PAS is contraindicated with rifampicin because it:", ["Decreases rifampicin absorption", "Increases rifampicin toxicity", "Causes disulfiram reaction", "Induces hepatic enzymes"], "The PAS bullet: C/I with rifampicin (decreased absorption).")
q(196, "The intensive phase for a new/previously treated TB case is:", ["HRZE (2 months)", "HRE (4 months)", "HRZE (4 months)", "HRE (2 months)"], "The regimen table: new/previously treated case gets HRZE 2 months intensive.")
q(196, "The continuous phase of the standard TB regimen is:", ["HRE (4 months)", "HRZE (2 months)", "HRZE (6 months)", "HRE (6 months)"], "The regimen table: continuous phase HRE 4 months.")
q(196, "In the shorter oral bedaquiline-containing regimen, bedaquiline is given for:", ["6 months", "4 months", "9 months", "2 months"], "The regimen cell: Bdq (6 months).")
q(196, "In the shorter oral Bdq regimen, the intensive-phase companions (Lfx, Cfz, Z, E, H, Eto) run for:", ["4-6 months", "9 months", "2 months", "18-20 months"], "The cell: Lfx, Cfz, Z, E, H, Eto (4-6 months).")
q(196, "In months 7 till 9 of the shorter oral Bdq regimen, the drugs used are:", ["Lfx, Cfz, Z, E", "Lfx, Cfz, Z, E, Bdq", "High-dose H and Eto only", "Bdq alone"], "The timeline row: 7th till 9th months - Lfx, Cfz, Z, E.")
q(196, "During the 5th and 6th months of the shorter oral Bdq regimen, the drugs are:", ["Lfx, Cfz, Z, E, Bdq", "Lfx, Cfz, Z, E + high dose H, Eto", "Mfx, Km/Am, Eto", "Bdq + Lzd"], "The middle timeline cell: 5th and 6th months - Lfx, Cfz, Z, E, Bdq.")
q(196, "Till the 4th month of the shorter oral Bdq regimen, the regimen includes high doses of:", ["H and Eto", "Z and E", "Lfx and Cfz", "Rifampicin and PAS"], "The first timeline cell: Lfx, Cfz, Z, E, Bdq, high doses H, Eto.")
q(196, "The shorter INJECTABLE containing (alternative) regimen intensive phase is:", ["Mfx, Km/Am, Eto, Cfz, Z, H, E (4-6 months)", "Mfx, Cfz, Z, E (5 months)", "Bdq, Lfx, Lzd, Cfz, Cs", "HRZE (2 months)"], "The alternative regimen cell lists Mfx, Km/Am, Eto, Cfz, Z, H, E for 4-6 months.")
q(196, "The long oral RR-/XDR regimen consists of:", ["Bdq (6 months) + Lfx, Lzd, Cfz, Cs (18-20 months)", "Bdq + Lfx, Cfz, Z, E for 9 months", "Mfx + Km/Am for 6 months", "Pretomanid + linezolid for 26 weeks"], "The long oral regimen cell: Bdq (6 months), Lfx, Lzd, Cfz, Cs (18-20 months).")
q(196, "The BPaL regimen (pilot) is indicated for:", ["MDR TB with FQ resistance", "New drug-sensitive TB", "Latent TB", "Leprosy reactions"], "The BPaL row: MDR TB with FQ resistance.")
q(196, "In BPaL, pretomanid is given as:", ["200 mg OD daily for 26 weeks", "400 mg OD for 26 weeks", "1200 mg once daily for 24 weeks", "200 mg thrice weekly for 24 weeks"], "The BPaL bullet: pretomanid 200 mg OD daily for 26 weeks.")
q(196, "In BPaL, the bedaquiline dosing written is:", ["400 mg OD for first week, then 200 mg three times a week for 24 weeks", "200 mg OD for 26 weeks", "400 mg thrice weekly throughout", "600 mg OD for 6 months"], "The BPaL bullet details 400 mg OD daily for the first week, then 200 mg three times a week for 24 weeks.")
q(196, "In BPaL, linezolid is given as:", ["1200 mg once daily for 24 weeks", "600 mg once daily for 6 weeks", "1200 mg thrice weekly for 12 weeks", "300 mg OD for 26 weeks"], "The BPaL bullet: linezolid 1200 mg once daily for 24 weeks.")

unit("Anti-Leprosy Drugs: First and Second Line", "First-line leprosy drugs: rifampicin is the most cidal; dapsone is a DHPS inhibitor and static, most commonly causing hemolysis in G6PD deficiency; clofazimine works by free radical production - cidal in TB but static in leprosy - and treats lepra reactions: type 1 and type 2 are both managed with steroids as DOC, with clofazimine and thalidomide (most effective) as alternatives; its side effects are ichthyosis and crystal deposition in GIT mucosa. Second line: clarithromycin and minocycline are static; ofloxacin and moxifloxacin are cidal.")
q(197, "The MOST cidal first-line antileprosy drug is:", ["Rifampicin", "Dapsone", "Clofazimine", "Minocycline"], "The first-line list: rifampicin - most cidal.")
q(197, "Dapsone acts by inhibiting:", ["DHPS", "RNA polymerase", "Mycolic acid synthesis", "ATP synthase"], "The dapsone bullet: DHPS inhibitor.")
q(197, "Dapsone is a:", ["Static drug", "Cidal drug", "Steroid", "Immunomodulator only"], "The dapsone bullet: static drug.")
q(197, "The MOST COMMON side effect of dapsone in G6PD deficiency is:", ["Hemolysis", "Ichthyosis", "Optic neuritis", "Hypothyroidism"], "The dapsone S/E: hemolysis in G6PD deficiency (M/C).")
q(197, "The MOA of clofazimine is:", ["Free radical production", "DHPS inhibition", "ATP synthase inhibition", "RNA polymerase inhibition"], "The clofazimine bullet: MOA free radical production.")
q(197, "Clofazimine in TB is:", ["Cidal", "Static", "Inactive", "Steroid-sparing only"], "The clofazimine bullet: in TB cidal effect.")
q(197, "Clofazimine in leprosy is:", ["Static", "Cidal", "Most cidal", "Contraindicated"], "The clofazimine bullet: in leprosy static effect.")
q(197, "The DOC for both type 1 and type 2 lepra reaction is:", ["Steroids", "Thalidomide", "Clofazimine", "Dapsone"], "Both lepra reaction branches mark DOC: steroids.")
q(197, "The MOST EFFECTIVE alternative drug for type 2 lepra reaction is:", ["Thalidomide", "Clofazimine", "Ofloxacin", "Minocycline"], "The type 2 branch: alternative drugs clofazimine, thalidomide (most effective).")
q(197, "Side effects of clofazimine are:", ["Ichthyosis and crystal deposition in GIT mucosa", "Hemolysis and methemoglobinemia", "Optic neuritis and arthralgia", "QT prolongation"], "The clofazimine S/E list: ichthyosis, deposition of crystals in GIT mucosa.")
q(197, "The STATIC second-line antileprosy drugs are:", ["Clarithromycin and minocycline", "Ofloxacin and moxifloxacin", "Rifampicin and dapsone", "Thalidomide and steroids"], "The second-line block: clarithromycin, minocycline bracketed static.")
q(197, "The CIDAL second-line antileprosy drugs are the fluoroquinolones:", ["Ofloxacin and moxifloxacin", "Levofloxacin and ciprofloxacin", "Clarithromycin and minocycline", "Norfloxacin and gatifloxacin"], "The FQ branch: ofloxacin, moxifloxacin bracketed cidal.")

unit("WHO Leprosy Guidelines, Resistant Leprosy and MAC", "WHO multidrug therapy: supervised once monthly - adults rifampicin 600 mg + clofazimine 300 mg, children 10-14 years rifampicin 450 mg + clofazimine 150 mg, children below 14 years or 40 kg rifampicin 10 mg/kg + clofazimine 6 mg/kg; non-supervised once daily - adults dapsone 100 mg + clofazimine 50 mg, children 10-14 years dapsone 50 mg + clofazimine 50 mg alternate days, small children dapsone 2 mg/kg + clofazimine 1 mg/kg. Rifampicin-resistant leprosy: ofloxacin 400 mg + minocycline 100 mg (or clarithromycin 500 mg) + clofazimine 50 mg for 6 months daily, then 18 months with ofloxacin or minocycline + clofazimine. Rifampicin+ofloxacin resistance: clarithromycin 500 mg + minocycline 100 mg + clofazimine. MAC regimen mnemonic EAR: ethambutol, azithromycin (usable in macrolide resistance - immunomodulator effect), rifampicin.")
q(197, "In WHO supervised (once a month) therapy, the adult doses are:", ["Rifampicin 600 mg + clofazimine 300 mg", "Rifampicin 450 mg + clofazimine 150 mg", "Dapsone 100 mg + clofazimine 50 mg", "Rifampicin 10 mg/kg + clofazimine 6 mg/kg"], "The WHO table adult supervised cell: rifampicin 600 mg, clofazimine 300 mg.")
q(197, "Supervised monthly doses for children 10-14 years are:", ["Rifampicin 450 mg + clofazimine 150 mg", "Rifampicin 600 mg + clofazimine 300 mg", "Dapsone 50 mg + clofazimine 50 mg", "Rifampicin 10 mg/kg + clofazimine 6 mg/kg"], "The children 10-14 years supervised cell: rifampicin 450 mg, clofazimine 150 mg.")
q(197, "For children <14 years or <40 kg, supervised doses are:", ["Rifampicin 10 mg/kg + clofazimine 6 mg/kg", "Rifampicin 450 mg + clofazimine 150 mg", "Dapsone 2 mg/kg + clofazimine 1 mg/kg", "Rifampicin 600 mg + clofazimine 300 mg"], "The third supervised column: rifampicin 10 mg/kg, clofazimine 6 mg/kg.")
q(197, "Non-supervised (once a day) adult therapy is:", ["Dapsone 100 mg + clofazimine 50 mg", "Dapsone 50 mg + clofazimine 50 mg", "Rifampicin 600 mg + clofazimine 300 mg", "Dapsone 2 mg/kg + clofazimine 1 mg/kg"], "The adult non-supervised cell: dapsone 100 mg, clofazimine 50 mg.")
q(197, "Non-supervised therapy for children 10-14 years is:", ["Dapsone 50 mg + clofazimine 50 mg (alternate day)", "Dapsone 100 mg daily + clofazimine 50 mg", "Dapsone 2 mg/kg + clofazimine 1 mg/kg", "Rifampicin 450 mg monthly"], "The children 10-14 non-supervised cell: dapsone 50 mg, clofazimine 50 mg alternate day.")
q(197, "Non-supervised doses for children <14 years or <40 kg are:", ["Dapsone 2 mg/kg + clofazimine 1 mg/kg", "Dapsone 50 mg + clofazimine 50 mg", "Dapsone 100 mg + clofazimine 50 mg", "Rifampicin 10 mg/kg + clofazimine 6 mg/kg"], "The last non-supervised cell: dapsone 2 mg/kg, clofazimine 1 mg/kg.")
q(198, "In rifampicin-resistant leprosy, the FIRST 6 months daily regimen (option 1) is:", ["Ofloxacin 400 mg + minocycline 100 mg + clofazimine 50 mg", "Clarithromycin 500 mg + minocycline 100 mg + clofazimine 50 mg", "Ofloxacin 400 mg + clofazimine 50 mg only", "Dapsone 100 mg + ofloxacin 400 mg"], "The table: rifampicin resistance first 6 months - ofloxacin 400 + minocycline 100 + clofazimine 50.")
q(198, "In rifampicin resistance, the alternative first-6-months combination replaces minocycline with:", ["Clarithromycin 500 mg", "Moxifloxacin 400 mg", "Thalidomide 100 mg", "Amikacin"], "The second rifampicin-resistance row uses ofloxacin 400 + clarithromycin 500 + clofazimine 50.")
q(198, "In rifampicin resistance, the next 18 months daily therapy can be:", ["Ofloxacin 400 mg or minocycline 100 mg + clofazimine 50 mg", "Ofloxacin + minocycline + clofazimine all three", "Clarithromycin + ofloxacin only", "Dapsone monotherapy"], "The next-18-months cell: ofloxacin 400 mg or minocycline 100 mg + clofazimine 50 mg.")
q(198, "In rifampicin AND ofloxacin resistant leprosy, the first 6 months daily regimen is:", ["Clarithromycin 500 mg + minocycline 100 mg + clofazimine 50 mg", "Ofloxacin 400 mg + clofazimine 50 mg", "Dapsone + clarithromycin", "Minocycline monotherapy"], "The table: clarithromycin 500 + minocycline 100 + clofazimine 50.")
q(198, "For rifampicin and ofloxacin resistance, the next 18 months uses:", ["Clarithromycin 500 mg or minocycline 100 mg + clofazimine 50 mg", "Clarithromycin + minocycline + clofazimine all three daily", "Ofloxacin + clofazimine", "Thalidomide + dapsone"], "The final cell: clarithromycin 500 or minocycline 100 + clofazimine 50.")
q(198, "The regimen mnemonic for Mycobacterium Avium Complex is:", ["EAR", "REH", "CAZ", "ZEUS"], "The MAC section: mnemonic EAR.")
q(198, "The MAC regimen drugs are ethambutol, rifampicin and:", ["Azithromycin", "Amikacin", "Arabinosyl transferase inhibitor only", "Albendazole"], "The EAR list: ethambutol, azithromycin, rifampicin.")
q(198, "The macrolide in the MAC regimen that can be used in macrolide resistance due to immunomodulator effect is:", ["Azithromycin", "Clarithromycin", "Erythromycin", "Roxithromycin"], "The azithromycin bullet: can be used in macrolid resistance - immunomodulator effect.")

end()
for i, item in enumerate(Q, 1):
    item["id"] = f"PHARM-C{CH}-{i:03d}"
units = []
for n, u in enumerate(UNITS, 1):
    a, b = u["start"], u["end"]
    units.append({"id": f"PHARM-U{CH}-{n}", "ch": CH, "n": n, "title": u["title"],
                  "sec": f"{u['title']} · p{Q[a-1]['page']}",
                  "qs": [f"PHARM-C{CH}-{i:03d}" for i in range(a, b+1)],
                  "guide": u["guide"]})
json.dump({"questions": Q, "units": units}, open(f"data/ch{CH:02d}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"ch{CH}: {len(Q)} questions, {len(units)} units")
for u in units:
    print(u["id"], len(u["qs"]), u["sec"])
