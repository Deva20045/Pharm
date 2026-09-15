# -*- coding: utf-8 -*-
import json
CH = 51
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

unit("Physiology of Glucose Metabolism", "Diabetes mellitus, type 1 or type 2, means persistently raised blood glucose. Food is broken down in the small intestine where disaccharides are split by alpha-glucosidase and glucose is absorbed via SGLT1, raising GLP-1 and glucose in systemic circulation; GLP and GLP-1 are metabolized in plasma by the DPP-4 enzyme, giving them a short half-life. After the post-prandial surge, concentration-dependent glucose uptake occurs by facilitated diffusion. In beta cells, glucose acting through the SUR receptor blocks ATP-sensitive potassium channels, ATP formation rises and insulin is released; insulin plus amylin act on the insulin receptor, GLUT-4 becomes extracellular and glucose uptake follows. Three dampening/disposal points are marked D: alpha-glucosidase, renal SGLT2 reabsorption and delayed gastric emptying, which dampens post-prandial hyperglycemia; the liver drives gluconeogenesis during fasting.")
q(207, "Diabetes mellitus type 1 and type 2 are characterized by:", ["Persistently increased blood glucose levels", "Episodic hypoglycemia", "Low HbA1c", "Post-prandial hypoglycemia"], "The opening note: DM type 1/type 2 - persistently increased blood glucose levels.")
q(207, "In the small intestine, disaccharides are broken down by:", ["alpha-glucosidase", "SGLT2", "DPP-4", "Amylase only"], "The diagram shows disaccharides acted on by alpha-glucosidase.")
q(207, "Glucose absorption from the small intestine occurs via:", ["SGLT1", "SGLT2", "GLUT-4", "DPP-4"], "The small-intestine absorptive arrow is labelled SGLT1.")
q(207, "GLP and GLP-1 are metabolized in plasma by:", ["DPP-4 enzyme giving short half-life", "CYP3A4 giving long half-life", "Renal peptidases only", "Alpha-glucosidase"], "The note: GLP & GLP-1 metabolised in plasma by DPP4 enzyme, leading to short half-life.")
q(207, "Insulin release from beta cells is triggered by:", ["Block of ATP-sensitive K+ channels via SUR receptor", "Opening of ATP-sensitive K+ channels", "Block of GLUT-1", "Activation of alpha-glucosidase"], "The beta-cell flow: SUR receptor blocks the ATP-sensitive K+ channel, then ATP formation and insulin release.")
q(207, "The sequence inside beta cells after SUR receptor stimulation is:", ["ATP-sensitive K+ channel block, then ATP formation, then release", "ATP formation, then K+ channel opening, then release", "GLUT-1 block, then release", "cAMP fall, then release"], "The diagram numbers: block of ATP-sensitive K+ channel, then ATP formation, then release.")
q(207, "Insulin acts with which co-secreted peptide on the insulin receptor?", ["Amylin", "GLP-1", "GIP", "Somatostatin"], "The diagram shows insulin + amylin acting on the insulin receptor.")
q(207, "After insulin receptor activation, glucose entry into cells occurs via:", ["GLUT-4 becoming extracellular", "GLUT-1 becoming extracellular", "SGLT2 insertion", "SUR receptor internalization"], "The flow: insulin receptor acts on GLUT-4, which becomes extracellular, then glucose uptake.")
q(207, "Uptake of glucose after the post-prandial surge occurs by:", ["Facilitated diffusion (concentration dependent)", "Active transport via SGLT2", "Simple diffusion only", "Pinocytosis"], "The note: after post-prandial surge, concentration dependent uptake of glucose (facilitated diffusion).")
q(207, "The D-marked mechanism that dampens post-prandial hyperglycemia is:", ["Delayed gastric emptying", "Renal gluconeogenesis", "Hepatic glycogenolysis", "Insulin degradation"], "The D note: delayed gastric emptying (dampens post-prandial hyper glycemia).")
q(207, "Kidneys reabsorb glucose from urine via:", ["SGLT2 (active transport)", "SGLT1 (passive)", "GLUT-2", "DPP-4"], "The kidney box: reabsorbed from urine via SGLT2 (active transport).")
q(207, "Gluconeogenesis shown in the diagram occurs during:", ["Fasting", "Post-prandial state", "Insulin excess", "Exercise only"], "The liver/lower diagram notes gluconeogenesis during fasting.")

unit("Drugs Used: Classification", "Anti-diabetic drugs fall into alpha-glucosidase inhibitors, GLP-1 related drugs (GLP-1 agonists that raise insulin release, DPP-4 inhibitors and dual GLP-1 & GIP agonists - class side effect pancreatitis), amylin analogs that delay gastric emptying, miscellaneous agents bromocriptine and colesevelam, insulin, and oral hypoglycemic agents with five mechanisms: raise insulin release by blocking ATP-sensitive K+ channels, lower insulin resistance (pioglitazone), inhibit gluconeogenesis (metformin), block SGLT1, or block both SGLT1 and SGLT2 (sotagliflozin, approved 2019). T1DM uses insulin and amylin analog; T2DM can use all anti-diabetic drugs; any drug acting via insulin causes hypoglycemia.")
q(208, "The side effect of GLP-1 related drugs is:", ["Pancreatitis", "Lipodystrophy", "Lactic acidosis", "Hypokalemia"], "The GLP1-related branch: side effect pancreatitis.")
q(208, "GLP-1 agonists act by:", ["Increasing insulin release", "Blocking insulin release", "Increasing glucagon", "Blocking gastric emptying only"], "The branch: GLP1 agonists (increased insulin release).")
q(208, "Which GLP-1 related subgroup is a dual agonist?", ["Dual GLP1 & GIP agonist", "DPP-4 inhibitor", "Amylin analog", "SGLT2 blocker"], "The branch lists dual GLP1 & GIP agonist.")
q(208, "The amylin analog acts by:", ["Delaying gastric emptying", "Blocking SGLT2", "Blocking ATP-sensitive K+ channels", "Inhibiting gluconeogenesis"], "The amylin analog branch: delays gastric emptying.")
q(208, "The miscellaneous anti-diabetic drugs listed are:", ["Bromocriptine and colesevelam", "Metformin and pioglitazone", "Sotagliflozin and dapagliflozin", "NPH and lente"], "The miscellaneous branch: bromocriptine, colesevelam.")
q(208, "OHA mechanism 1, raising insulin release, works by:", ["Blocking ATP-sensitive K+ channels", "Opening ATP-sensitive K+ channels", "Blocking SUR receptor antagonism", "Stimulating alpha-glucosidase"], "The OHA list: 1. increased insulin release (block ATP-sensitive K+ channels).")
q(208, "The OHA example given for decreasing insulin resistance is:", ["Pioglitazone", "Metformin", "Sitagliptin", "Glipizide"], "The list: decreased insulin resistance e.g. pioglitazone.")
q(208, "The OHA example for inhibition of gluconeogenesis is:", ["Metformin", "Pioglitazone", "Colesevelam", "Liraglutide"], "The list: inhibit gluconeogenesis e.g. metformin.")
q(208, "Blocking SGLT1 alone treats diabetes by:", ["Blocking reabsorption by kidneys", "Blocking gastric emptying", "Raising insulin release", "Reducing insulin resistance"], "The OHA list item 4: block SGLT1 (block reabsorption by kidneys).")
q(208, "The drug that blocks BOTH SGLT1 and SGLT2, approved in 2019, is:", ["Sotagliflozin", "Dapagliflozin", "Empagliflozin", "Canagliflozin"], "The list: block SGLT1 & SGLT2 - sotagliflozin: approved in 2019.")
q(208, "Drugs used in T1DM are:", ["Insulin & amylin analogue", "All anti-diabetic drugs", "Only OHA", "Only alpha-glucosidase inhibitors"], "The note: T1DM - insulin & amylin analogue.")
q(208, "Drugs used in T2DM are:", ["All anti-diabetic drugs", "Only insulin", "Insulin & amylin analog only", "Only sulfonylureas"], "The note: T2DM - all anti-diabetic drugs.")
q(208, "The side effect of drugs that act via insulin is:", ["Hypoglycemia", "Hyperglycemia", "Pancreatitis", "Lactic acidosis"], "The note: side effect of drugs that act via insulin - hypoglycemia.")

unit("Insulin: Duration of Action", "By duration: ultra-short acting insulins are given just before food, fastest being inhaled Afrezza; short acting splits into fast-acting rDNA monomeric insulins - glulisine, lispro, aspart, 15 minutes before food - and slow-acting regular insulin 60 minutes before food; these manage post-prandial hyperglycemia. Intermediate acting: NPH (neutral protamine Hagedorn) and Lente, dosed BD/TDS. Long acting: detemir (increased plasma protein binding), glargine (acidic pH) and degludec (hexameric), the longest acting, dosed OD/BD for maintenance of blood glucose. Routes: inhaled Afrezza is absorbed through lung capillaries (fastest), all others subcutaneous, and IV regular insulin is used in hyperkalemia and is DOC in diabetic ketoacidosis.")
q(208, "Ultra-short acting insulin is taken:", ["Just before food (B/F)", "60 min before food", "Once daily at night", "Only during fasting"], "The ultra-short acting branch: just before food/B/F.")
q(208, "The fastest acting insulin is:", ["Afrezza", "Lispro", "Glulisine", "Regular insulin"], "The branch labels Afrezza (fastest acting).")
q(208, "Fast-acting rDNA monomeric insulins include:", ["Glulisine, lispro, aspart", "NPH, lente, detemir", "Glargine, degludec, detemir", "Regular, NPH, lente"], "The fast-acting list: glulisine, lispro, aspart.")
q(208, "Fast-acting rDNA monomeric insulins are given:", ["15 min before food", "60 min before food", "With food only", "After food"], "The bracket: 15 min B/F.")
q(208, "Regular insulin is taken:", ["60 min before food", "15 min before food", "Just before food", "At bedtime"], "The slow-acting line: regular insulin 60 min B/F.")
q(208, "Ultra-short and short acting insulins are used for:", ["Management of post-prandial hyperglycemia", "Maintenance of blood glucose", "Treatment of DKA only", "Treatment of hyperkalemia"], "The bracket under short acting: for management of post-prandial hyperglycemia.")
q(208, "The intermediate acting insulins are:", ["NPH and Lente", "Detemir and glargine", "Lispro and aspart", "Regular and degludec"], "The intermediate branch: neutral protamine Hagedorn (NPH), Lente.")
q(208, "The dosing of intermediate acting insulins is:", ["BD / TDS", "OD / BD", "Once weekly", "Only TDS"], "The intermediate branch: dosing BD/TDS.")
q(208, "The long acting insulin with increased plasma protein binding is:", ["Detemir", "Glargine", "Degludec", "NPH"], "The long acting list: detemir (increased plasma protein binding).")
q(208, "Glargine is characterized by:", ["Acidic pH", "Hexameric structure", "Protamine content", "Zinc crystals only"], "The list: glargine (acidic pH).")
q(208, "The hexameric, longest acting insulin is:", ["Degludec", "Glargine", "Detemir", "Lente"], "The list: degludec (hexameric), marked longest acting.")
q(208, "The dosing of long acting insulins is:", ["OD / BD", "BD / TDS", "Thrice weekly", "Once weekly"], "The long acting branch: dosing OD/BD.")
q(208, "Long acting insulins are used for:", ["Maintenance of blood glucose", "Post-prandial hyperglycemia", "Emergency hyperkalemia", "Gestational diabetes screening"], "The bracket under long acting: for maintenance of blood glucose.")
q(208, "The inhaled insulin absorbed through lung capillaries is:", ["Afrezza", "NPH", "Insulin glargine", "Regular insulin"], "The route block: inhalational - Afrezza (absorbed through lung capillaries: fastest action).")
q(208, "The route for all insulins other than Afrezza is:", ["Subcutaneous", "Inhalational", "Intravenous", "Intramuscular"], "The route block: subcutaneous - all other insulins.")
q(208, "IV regular insulin is used in:", ["Hyperkalemia and diabetic ketoacidosis (DOC)", "Hypokalemia only", "Chronic maintenance therapy", "Hypoglycemia"], "The I/V block: regular insulin used in hyperkalemia and DKA (DOC).")

unit("Insulin Regimen and Injection Sites", "The standard regimen is 1 insulin for post-prandial hyperglycemia management plus 1 insulin for maintenance of blood glucose. If both are subcutaneous they can go in the same syringe as NPH + regular, drawing regular first to prevent contaminating the vial with cloudy NPH, or in different syringes. Continuous infusion with regular insulin is preferred in in-patients because there is no plasma peak, lowering hypoglycemia risk. Injection sites: abdomen is most common - except periumbilical skin (increased lipodystrophy risk) - with faster, most reliable absorption; alternatives are upper arm, antero-lateral thigh and upper buttock area. Afrezza comes as powder in color-coded cartridges: blue 4U, green 8U, yellow 12U; side effects are cough and increased lung cancer risk; it is contraindicated in bronchial asthma/COPD and smokers. Lente is insulin + zinc precipitated into long-acting white crystals (ultralente) and short-acting white powder (semilente), mixed 70%/30% as intermediate-acting Lente.")
q(209, "The standard insulin regimen consists of:", ["1 insulin for PPH management + 1 insulin for maintenance of blood glucose", "2 insulins for maintenance only", "Only regular insulin TDS", "3 insulins of different durations"], "The regimen line: 1 insulin for management of PPH + 1 insulin for maintenance of blood glucose.")
q(209, "When mixing in one syringe, the combination and order are:", ["NPH + regular, regular drawn first", "Regular + NPH, NPH drawn first", "Glargine + lispro, lispro first", "Degludec + aspart, degludec first"], "The regimen: NPH + regular insulin in same syringe, regular drawn first.")
q(209, "Regular insulin is drawn first to prevent:", ["Contamination of vial with cloudy NPH", "Loss of potency of NPH", "Air embolism", "Adsorption to syringe"], "The note: regular drawn first to prevent contamination of vial with cloudy NPH.")
q(209, "Continuous insulin infusion is preferred in:", ["In-patient cases", "All outpatients", "Children only", "Pregnancy only"], "The block: continuous infusion - preferred in in-patient cases.")
q(209, "Continuous infusion lowers hypoglycemia risk because:", ["There is no peak in plasma concentration", "The dose is smaller", "Absorption is slower", "It avoids the kidney"], "The note: decreased risk of hypoglycemia (no peak in plasma concentration).")
q(209, "The most common site of s/c insulin injection is:", ["Abdomen", "Upper arm", "Thigh", "Buttocks"], "The sites figure: abdomen m/c.")
q(209, "The abdominal site to EXCLUDE is:", ["Periumbical site (increased risk of lipodystrophy)", "Upper abdomen", "Flanks", "Lower abdomen entirely"], "The abdomen note: except periumbical site (d/t increased risk of lipodystrophy).")
q(209, "Advantages of the abdomen as injection site:", ["Faster & most reliable absorption", "Painless injection", "No infection risk", "Longest duration of action"], "The abdomen bullet: advantages - faster & most reliable absorption.")
q(209, "Other s/c injection sites listed are:", ["Upper arm, antero-lateral thigh, upper area of buttocks", "Anterior thigh and flank", "Deltoid only", "Lumbar region and calf"], "The figure labels: upper arm, antero-lateral aspect of thigh, upper area of buttocks.")
q(209, "Afrezza cartridges are color-coded as:", ["Blue 4U, green 8U, yellow 12U", "Blue 12U, green 8U, yellow 4U", "Red 4U, blue 8U, green 12U", "Blue 2U, green 4U, yellow 8U"], "The Afrezza block: blue 4U, green 8U, yellow 12U.")
q(209, "Side effects of inhaled Afrezza are:", ["Cough and increased risk of lung cancer", "Lipodystrophy and hypokalemia", "Pancreatitis", "Lactic acidosis"], "The side-effect list: cough, increased risk of lung cancer.")
q(209, "Afrezza is contraindicated in:", ["Bronchial asthma/COPD and smokers", "Diabetics with nephropathy", "Elderly only", "Pregnant women only"], "The C/I list: bronchial asthma/COPD, smokers.")
q(209, "Lente insulin is formed by precipitating:", ["Insulin + zinc", "Insulin + protamine", "Insulin + phenol", "Insulin + albumin"], "The lente block: insulin + zinc precipitates into.")
q(209, "Ultralente and semilente are respectively:", ["Long acting white crystals and short acting white powder", "Short acting crystals and long acting powder", "Both intermediate acting", "Both long acting liquids"], "The block: ultralente long acting white crystals, semilente short acting white powder.")
q(209, "The 70%/30% mix under lente refers to:", ["Ultralente 70% + semilente 30% = intermediate acting Lente", "Regular 70% + NPH 30%", "Lispro 70% + glargine 30%", "Detemir 70% + degludec 30%"], "The 70%/30% bracket ends in Lente intermediate acting.")

unit("Side Effects of Insulins", "Hypoglycemia is the most common side effect; plasma concentration is proportional to hypoglycemia risk, so shorter acting insulins carry higher risk, while glargine's smooth peakless long-acting curve keeps risk low (the plasma concentration graph orders A, FA, R, IA and LA). Hypokalemia is second; lipodystrophy - lipo-hypertrophy and lipo-atrophy - is third, prevented by rotating injection sites at least 1 inch apart.")
q(210, "The MOST COMMON side effect of insulin is:", ["Hypoglycemia", "Lipodystrophy", "Hypokalemia", "Weight gain"], "The list: 1. hypoglycemia (m/c).")
q(210, "Risk of hypoglycemia is proportional to:", ["Plasma concentration", "Injection site", "Dose frequency only", "Insulin origin"], "The line: plasma concentration proportional to risk of hypoglycemia.")
q(210, "Which insulins carry the HIGHEST hypoglycemia risk?", ["Shorter acting insulins", "Long acting insulins", "Intermediate acting insulins", "All equally"], "The bullet: shorter acting, then increased risk.")
q(210, "The insulin with a smooth peakless graph (lowest peak-related risk) is:", ["Glargine (long-acting)", "Afrezza", "Regular insulin", "Lispro"], "The bullet: smooth peakless graph - glargine (long-acting).")
q(210, "In the plasma concentration graph, the insulin with the HIGHEST, sharpest peak is:", ["A: Afrezza", "LA: long acting", "IA: intermediate acting", "R: regular insulin"], "The graph shows A with the tallest earliest peak, followed by FA, R, IA, LA.")
q(210, "The second side effect of insulin listed is:", ["Hypokalemia", "Hypoglycemia", "Lipodystrophy", "Edema"], "The list: 2. hypokalemia.")
q(210, "Lipodystrophy from insulin includes:", ["Lipo-hypertrophy and lipo-atrophy", "Only lipo-atrophy", "Only hirsutism", "Skin necrosis only"], "The photos: lipo-hypertrophy and lipo-atrophy.")
q(210, "Prevention of insulin lipodystrophy is:", ["Rotation of injection site with >=1 inch between each site", "Use of IM route", "Zinc-free insulin", "Prophylactic antihistamines"], "The prevention line: rotation of site of injection with >=1 inch between each site.")

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
