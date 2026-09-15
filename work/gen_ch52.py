# -*- coding: utf-8 -*-
import json
CH = 52
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

unit("GLP-1 Agonists", "GLP-1 related drugs and ATP-sensitive K+ channel inhibitors both increase insulin release, with hypoglycemia as the common side effect. GLP-1 agonists: liraglutide is once daily; dulaglutide, albiglutide and semaglutide are once a week; the route is subcutaneous except oral semaglutide (OD). Side effects are pancreatitis, nausea and vomiting from delayed gastric emptying, and weight loss from decreased appetite - making them DOC for obesity, ranked oral semaglutide > subcutaneous semaglutide > subcutaneous liraglutide.")
q(211, "The common side effect of drugs that increase release of insulin is:", ["Hypoglycemia", "Weight gain", "Pancreatitis", "Lactic acidosis"], "Below the classification: common side effect - hypoglycemia.")
q(211, "The GLP-1 agonist with OD (once daily) dosage is:", ["Liraglutide", "Dulaglutide", "Albiglutide", "Semaglutide"], "The drug list: liraglutide - OD dosage.")
q(211, "The GLP-1 agonists given once a week are:", ["Dulaglutide, albiglutide, semaglutide", "Liraglutide, dulaglutide, albiglutide", "Semaglutide, liraglutide, exenatide", "Albiglutide only"], "The bracket groups dulaglutide, albiglutide, semaglutide as once a week dosage.")
q(211, "The usual route of GLP-1 agonists is:", ["S/C (oral only for oral semaglutide)", "Oral", "IV", "IM"], "The route line: S/C, with oral semaglutide (OD dosage) written below.")
q(211, "A class side effect of GLP-1 agonists is:", ["Pancreatitis", "Angioedema", "Bone fracture", "Lactic acidosis"], "The side-effect list starts with pancreatitis.")
q(211, "Nausea and vomiting with GLP-1 agonists occur due to:", ["Delayed gastric emptying", "Increased gastric motility", "Gastroparesis cure", "Vagal stimulation"], "The bullet: nausea & vomiting (D/t delayed gastric emptying).")
q(211, "Weight loss with GLP-1 agonists is due to:", ["Decreased appetite", "Malabsorption", "Increased metabolism", "Gut fluid loss"], "The bullet: weight loss (D/t decreased appetite).")
q(211, "Because of weight loss, GLP-1 agonists are:", ["DOC for obesity", "Contraindicated in obesity", "Only for thin diabetics", "Used in cachexia"], "The note: DOC for obesity.")
q(211, "The written efficacy order for obesity is:", ["Oral semaglutide > s/c semaglutide > s/c liraglutide", "S/c liraglutide > s/c semaglutide > oral semaglutide", "S/c semaglutide > oral semaglutide > s/c liraglutide", "Dulaglutide > albiglutide > liraglutide"], "The ranking: oral semaglutide > s/c semaglutide > s/c liraglutide.")

unit("DPP-IV Inhibitors and Dual GLP-1 & GIP Agonist", "DPP-IV inhibitors work by decreasing metabolism of GLP-1 - sitagliptin, saxagliptin, alogliptin and linagliptin, all oral. Side effects: pancreatitis, angioedema (risk rises with ACE inhibitors) and increased infections by blocking CD46 on lymphocytes. They are weight-neutral because only endogenous GLP-1 action rises; all cause renal-failure contraindication except linagliptin, which is excreted by liver. The dual GLP-1 & GIP agonist is tirzepatide, subcutaneous, more efficient than a pure GLP-1 agonist.")
q(211, "The MOA of DPP-IV inhibitors is:", ["Decreases metabolism of GLP-1", "Stimulates GLP-1 release", "Blocks GLP-1 receptor", "Increases GIP degradation"], "The block: MOA - decreased metabolism of GLP-1.")
q(211, "Which is NOT a listed DPP-IV inhibitor?", ["Exenatide", "Sitagliptin", "Saxagliptin", "Linagliptin"], "The list: sitagliptin, saxagliptin, alogliptin, linagliptin.")
q(211, "The route of DPP-IV inhibitors is:", ["Oral", "Subcutaneous", "Intravenous", "Inhalational"], "The route line: oral.")
q(211, "Angioedema with DPP-IV inhibitors has increased risk with:", ["ACE inhibitors", "ARBs", "Beta blockers", "CCBs"], "The bullet: angioedema (increased risk with ACE inhibitors).")
q(211, "DPP-IV inhibitors increase risk of infections by:", ["Blocking CD46 in lymphocytes", "Blocking CD4 receptors", "Neutropenia", "Blocking complement C5"], "The bullet: increased risk of infections by blocking CD46 in lymphocytes.")
q(211, "DPP-IV inhibitors are weight-neutral because:", ["Only endogenous GLP-1 action increases", "They block appetite centers", "They cause malabsorption", "They increase GLP-1 and GIP both"], "The note: weight-neutral drugs as only endogenous GLP-1 action increased.")
q(211, "DPP-IV inhibitors are contraindicated in renal failure EXCEPT:", ["Linagliptin (D/t excretion by liver)", "Sitagliptin", "Saxagliptin", "Alogliptin"], "The C/I line: renal failure (except linagliptin D/t excretion by liver).")
q(211, "The dual GLP-1 & GIP agonist is:", ["Tirzepatide", "Semaglutide", "Dulaglutide", "Sitagliptin"], "The block: drug - tirzepatide.")
q(211, "The efficiency of tirzepatide compared with a pure GLP-1 agonist is:", ["Greater", "Equal", "Lesser", "Half"], "The line: efficiency > pure GLP-1 agonist.")

unit("Sulfonylureas and Meglitinides", "Both inhibit ATP-sensitive K+ channels: sulfonylureas release a large amount of insulin, are long acting and used for maintenance of blood glucose; meglitinides release small amounts, are short acting and manage post-prandial hyperglycemia. Shared side effects (sulfonylureas more): hypoglycemia and weight gain from blocking hormone-sensitive lipase - hence use in thin diabetics. Sulfonylureas are contraindicated with alcohol (disulfiram-like effect). Drugs: glyburide (aka glibenclamide), glimepiride, gliclazide; nateglinide (phenylalanine derivative) and repaglinide. Risk of hypoglycemia: insulin highest overall, then sulfonylureas.")
q(212, "Regarding insulin release, sulfonylureas release:", ["Large amount", "Small amount", "No insulin", "Insulin only with glucose"], "The table row: sulfonylureas - large amount.")
q(212, "Meglitinides compared with sulfonylureas have:", ["Small insulin release, short acting", "Large insulin release, long acting", "Small release, long acting", "Large release, short acting"], "The table: meglitinides - small amount, short acting.")
q(212, "The use of sulfonylureas is:", ["Maintenance of blood glucose", "Management of post-prandial hyperglycemia", "Treatment of DKA", "Weight loss"], "The use row: sulfonylureas - maintenance of blood glucose.")
q(212, "Meglitinides are used for:", ["Management of post-prandial hyperglycemia", "Maintenance of blood glucose", "Prophylaxis of DM", "Treating obesity"], "The use row: meglitinides - management of post-prandial hyperglycemia.")
q(212, "Weight gain with sulfonylureas is due to:", ["Block of hormone sensitive lipase", "Increased appetite centers", "Fluid retention", "Fat necrosis"], "The side-effect row: weight gain (D/t block of hormone sensitive lipase).")
q(212, "Because of weight gain, these drugs are used in:", ["Thin diabetics", "Obese diabetics only", "All diabetics", "Underweight children"], "The note: used in thin diabetics.")
q(212, "Sulfonylureas are contraindicated with alcohol because:", ["It causes disulfiram-like effect", "It causes lactic acidosis", "It causes hypokalemia", "It blocks insulin release"], "The C/I row: alcohol consumption - causes disulfiram-like effect.")
q(212, "Which drug is ALSO called glibenclamide?", ["Glyburide", "Glimepiride", "Gliclazide", "Repaglinide"], "The drug list: glyburide (aka glibenclamide).")
q(212, "The sulfonylureas listed are:", ["Glyburide, glimepiride, gliclazide", "Nateglinide, repaglinide", "Pioglitazone, rosiglitazone", "Sitagliptin, linagliptin"], "The drugs cell lists glyburide, glimepiride, gliclazide.")
q(212, "Nateglinide is a:", ["Phenylalanine derivative", "Sulfonylurea", "Biguanide", "Thiazolidinedione"], "The meglitinides cell: nateglinide (phenylalanine derivative).")
q(212, "The meglitinides listed are:", ["Nateglinide and repaglinide", "Gliclazide and glimepiride", "Repaglinide and glimepiride", "Acarbose and miglitol"], "The drugs cell: nateglinide, repaglinide.")
q(212, "The overall highest hypoglycemia risk is with:", ["Insulin > sulfonylureas", "Sulfonylureas > insulin", "Meglitinides > insulin", "Metformin > insulin"], "The note: risk of hypoglycemia - insulin (highest overall) > sulfonylureas.")

unit("Thiazolidinediones", "Pioglitazone and rosiglitazone are oral hypoglycemic agents that decrease insulin resistance by stimulating PPAR-gamma, which raises GLUT-4 production and causes adipocyte proliferation. Side effects: sodium and water retention from eNaC block leading to edema and congestive heart failure, macular edema (must be differentiated from diabetic etiology), bone fractures in females, increased risk of bladder cancer and hepatotoxicity.")
q(212, "Thiazolidinediones are OHAs which:", ["Decrease insulin resistance", "Increase insulin release", "Inhibit glucagon", "Block SGLT2"], "The heading line: OHAs which decreased insulin resistance.")
q(212, "The thiazolidinedione drugs listed are:", ["Pioglitazone and rosiglitazone", "Metformin and phenformin", "Glyburide and glimepiride", "Canagliflozin and dapagliflozin"], "The drug list: pioglitazone, rosiglitazone.")
q(212, "The MOA of thiazolidinediones is:", ["Stimulate PPAR-gamma, increasing GLUT-4 production and decreasing insulin resistance", "Block ATP-sensitive K+ channels", "Stimulate AMPK", "Inhibit alpha-glucosidase"], "The MOA flow: stimulate PPAR-gamma, then increased GLUT-4 production, then decreased insulin resistance.")
q(212, "PPAR-gamma stimulation also causes:", ["Adipocyte proliferation", "Adipocyte apoptosis", "Hepatic lipolysis", "Muscle hypertrophy"], "The second branch of the MOA: adipocyte proliferation.")
q(212, "TZD sodium-water retention occurs due to:", ["Block of eNaC", "Activation of eNaC", "Increased aldosterone only", "Renal failure"], "The side-effect bullet: retention of Na+ & water (D/t block of eNaC).")
q(212, "Na+/water retention with TZDs leads to:", ["Edema & congestive heart failure", "Hypertensive crisis only", "Nephrotic syndrome", "Cirrhosis"], "The arrow: edema & congestive heart failure.")
q(212, "The TZD side effect that must be differentiated from diabetic etiology is:", ["Macular edema", "Peripheral edema", "Bone fracture", "Hepatotoxicity"], "The bullet: macular edema - must be differentiated from diabetic etiology.")
q(212, "Bone fractures with TZDs occur in:", ["Females", "Males", "Children", "Elderly males only"], "The bullet: bone fracture in females.")
q(212, "The cancer risk increased by TZDs is:", ["Ca bladder", "Ca lung", "Ca breast", "Lymphoma"], "The bullet: increased risk for Ca bladder.")
q(212, "The hepatotoxic OHA class here is:", ["Thiazolidinediones", "Meglitinides", "DPP-IV inhibitors", "Alpha-glucosidase inhibitors"], "The last TZD bullet: hepatotoxic.")

unit("Biguanides: Metformin", "Metformin, the biguanide, lowers hepatic glucose production by stimulating AMPK (adenosine monophosphate kinase), which blocks gluconeogenesis. Uses: DOC for treatment and prophylaxis of both T1 and T2 DM; PCOS - treating anovulation via decreased insulin resistance; non-alcoholic steatohepatitis; and antipsychotic-induced obesity, where it is the only FDA-approved drug. Side effects: metabolic acidosis from inhibition of mitochondrial aerobic glycolysis, decreased vitamin B12 absorption prevented by calcium supplements (calcium-dependent absorption), and weight loss. Weight-losing drugs: mnemonic GAMS - GLP-1 agonist, Amylin analogue, Metformin, SGLT-2 blockers. Metformin is contraindicated where lactic acidosis risk rises: chronic alcoholism, severe lung disease (COPD), renal failure, liver failure and CHF; smoking does NOT increase lactic acidosis and is not a contraindication.")
q(212, "The biguanide OHA acts by:", ["Decreasing hepatic glucose production", "Increasing insulin release", "Decreasing renal glucose loss", "Slowing gastric emptying"], "The biguanide heading: OHA causing decreased hepatic glucose production; drug metformin.")
q(212, "The MOA of metformin is:", ["Stimulates AMPK which blocks gluconeogenesis", "Stimulates PPAR-gamma", "Blocks ATP-sensitive K+ channels", "Blocks eNaC"], "The MOA line: stimulates AMPK (adenosine monophosphate kinase) blocking gluconeogenesis.")
q(213, "Metformin is DOC for treatment and prophylaxis of:", ["Both T1 & T2 DM", "Only T2 DM", "Only T1 DM", "Gestational DM only"], "The use line: DOC for treatment & prophylaxis of both T1 & T2 DM.")
q(213, "In PCOS, metformin treats anovulation by:", ["Decreasing insulin resistance", "Increasing FSH", "Blocking androgens directly", "Inducing ovulation reflexly"], "The use line: PCOS - treatment of anovulation (D/t decreased insulin resistance).")
q(213, "Metformin is used in non-alcoholic steatohepatitis, abbreviated:", ["NASH", "NAFLD only", "PSC", "T2DM"], "The use line: non-alcoholic steatohepatitis (NASH).")
q(213, "For antipsychotic induced obesity, metformin is:", ["The only FDA-approved drug", "Contraindicated", "Second line to orlistat", "Off-label only"], "The use line: antipsychotic induced obesity - only FDA-approved drug.")
q(213, "Metformin causes metabolic acidosis by:", ["Inhibition of mitochondrial aerobic glycolysis", "Increased renal bicarbonate loss", "Lactate transporter activation", "Ketoacid production"], "The side-effect bullet: metabolic acidosis - inhibition of mitochondrial aerobic glycolysis.")
q(213, "Metformin decreases vitamin B12 absorption; prevention is with:", ["Calcium supplements (D/t Ca++ dependent absorption)", "Vitamin C supplements", "Zinc supplements", "Intrinsic factor"], "The bullet: decreased absorption of Vit B12, prevented by Ca++ supplements (D/t Ca++ dependent absorption).")
q(213, "The mnemonic for weight-losing anti-diabetic drugs is:", ["GAMS", "GASM", "MAGS", "SAGM"], "The note box: drugs causing weight loss - mnemonic GAMS.")
q(213, "In the weight-loss mnemonic GAMS, the letters stand for:", ["GLP-1 agonist, Amylin analogue, Metformin, SGLT-2 blockers", "Glimepiride, Acarbose, Metformin, Sitagliptin", "GLP-1 agonist, Amylin, Miglitol, Sulfonylurea", "Gliclazide, Actos, Metformin, Semaglutide"], "The note box maps GAMS to GLP-1 agonist, amylin analogue, metformin, SGLT-2 blockers.")
q(214, "Metformin is contraindicated in all of these EXCEPT:", ["Smoking", "Chronic alcoholism", "Severe lung disease (COPD)", "Renal failure"], "The C/I list: chronic alcoholism, severe lung disease (COPD), renal failure, liver failure, CHF; smoking is explicitly not a C/I.")
q(214, "The common mechanism of metformin contraindications is:", ["Increased lactic acidosis", "Increased hypoglycemia", "Hepatic necrosis", "Renal stones"], "The C/I header: increased lactic acidosis.")
q(214, "The note about smoking and metformin states:", ["Smoking does not increase lactic acidosis; not a C/I", "Smoking doubles lactic acidosis risk", "Smoking is absolute C/I", "Smoking causes B12 loss only"], "The line: smoking does not increase lactic acidosis - not C/I in metformin use.")

unit("SGLT Blockers", "Canagliflozin, dapagliflozin and empagliflozin are SGLT-2 blockers; sotagliflozin blocks both SGLT-1 and SGLT-2. They decrease glucose reabsorption in the kidney (SGLT-2) and small intestine (SGLT-1). Uses: DM and chronic CHF where mortality falls due to decreased preload from diuresis. Common side effects: from increased urine sodium - diuresis, hypotension, dehydration; from glucosuria - increased risk of UTI and vaginal infections like Candida. Rare effects: bone fracture (incidence up in elderly, both sexes), Fournier's gangrene and urosepsis.")
q(213, "The SGLT-2 blockers listed are:", ["Canagliflozin, dapagliflozin, empagliflozin", "Sotagliflozin, remogliflozin, sergliflozin", "Canagliflozin, metformin, acarbose", "Empagliflozin and linagliptin"], "The drug list brackets canagliflozin, dapagliflozin, empagliflozin as SGLT-2 blockers.")
q(213, "The drug that blocks BOTH SGLT-1 and SGLT-2 is:", ["Sotagliflozin", "Empagliflozin", "Dapagliflozin", "Canagliflozin"], "The list: sotagliflozin - SGLT-1 & 2 blocker.")
q(213, "The MOA of SGLT blockers is:", ["Decrease glucose reabsorption in kidney (SGLT-2) and small intestine (SGLT-1)", "Increase insulin release", "Block gluconeogenesis", "Delay gastric emptying"], "The MOA flow: decreased glucose reabsorption in kidney (SGLT-2) and small intestine (SGLT-1).")
q(213, "In chronic CHF, SGLT blockers decrease mortality by:", ["Decreasing preload due to diuresis", "Increasing contractility", "Reducing afterload directly", "Blocking RAAS"], "The use line: chronic CHF (to decrease mortality) - decreased preload D/t diuresis.")
q(213, "Diuresis, hypotension and dehydration with SGLT blockers are due to:", ["Increased Na+ in urine", "Glucose in urine", "Ketoacidosis", "Volume overload"], "The side-effect branch: D/t increased Na+ in urine - diuresis, hypotension, dehydration.")
q(213, "UTI and vaginal infections (e.g. Candida) with SGLT blockers occur due to:", ["Glucose in urine", "Increased Na+ in urine", "Immune suppression", "Alkaline urine"], "The second branch: D/t glucose in urine - increased risk of UTI and vaginal infections.")
q(214, "Rare side effects of SGLT blockers include:", ["Bone fracture, Fournier's gangrene, urosepsis", "Pancreatitis, angioedema, lactic acidosis", "Optic neuritis, ichthyosis, arthralgia", "Lipodystrophy only"], "The rare list: bone fracture, Fournier's gangrene, urosepsis.")
q(214, "Rare bone fracture with SGLT blockers has increased incidence in:", ["Elderly, male & female", "Only premenopausal women", "Only children", "Only athletes"], "The bone fracture bullet: incidence increased in elderly, male & female.")
q(214, "The devastating perineal infection rarely seen with SGLT blockers is:", ["Fournier's gangrene", "Necrotizing fasciitis of abdomen", "Retroperitoneal fibrosis", "Perirectal abscess only"], "The rare list names Fournier's gangrene.")
q(214, "The note listing drugs with DECREASED CVS mortality includes:", ["SGLT2 blocker and GLP-1 agonist", "Sulfonylurea and insulin", "TZD and meglitinide", "Alpha-glucosidase inhibitor and amylin analog"], "The note: decreased CVS mortality seen in SGLT2 blocker and GLP-1 agonist.")

unit("Alpha-Glucosidase Inhibitors and Amylin Analog", "Acarbose, voglibose and miglitol treat post-prandial hyperglycemia in T2 DM only, taken during the meal after a few bites. Side effects: flatulence (most common) because intestinal flora act on undigested starch and disaccharides, and osmotic diarrhea. The amylin analog pramlintide is subcutaneous, delays gastric emptying and reduces post-prandial hyperglycemia in BOTH T1 and T2 DM; with insulin it needs a different syringe and a 50% insulin dose reduction. Side effects are nausea/vomiting and weight loss - off-label used in obesity.")
q(214, "The alpha-glucosidase inhibitors listed are:", ["Acarbose, voglibose, miglitol", "Acarbose, metformin, miglitol", "Voglibose, sitagliptin, miglitol", "Acarbose, voglibose, pramlintide"], "The drug list: acarbose, voglibose, miglitol.")
q(214, "Alpha-glucosidase inhibitors are used for post-prandial hyperglycemia in:", ["T2 DM only", "T1 DM only", "Both T1 & T2 DM", "Gestational DM"], "The use line: post-prandial hyperglycemia in T2 DM only.")
q(214, "The dosage timing of alpha-glucosidase inhibitors is:", ["During meal (after few bites)", "30 min before meal", "Immediately after meal", "Fasting state"], "The dosage line: during meal (after few bites).")
q(214, "The MOST COMMON side effect of alpha-glucosidase inhibitors is:", ["Flatulence (D/t intestinal flora acting on undigested starch & disaccharides)", "Osmotic diarrhea", "Hypoglycemia", "Weight gain"], "The side-effect list: flatulence (m/c) with the noted mechanism.")
q(214, "The second side effect of alpha-glucosidase inhibitors is:", ["Osmotic diarrhoea", "Constipation", "Steatorrhea", "Lactic acidosis"], "The list continues with osmotic diarrhoea.")
q(214, "The amylin analog is:", ["Pramlintide", "Exenatide", "Lixisenatide", "Tirzepatide"], "The block: drug - pramlintide.")
q(214, "Pramlintide reduces post-prandial hyperglycemia in:", ["Both T1 & T2 DM", "T2 DM only", "T1 DM only", "Only steroid diabetes"], "The use line: decreased post-prandial hyperglycemia in both T1 & T2 DM.")
q(214, "When pramlintide is used with insulin:", ["Use different syringe and decrease insulin dose by 50%", "Mix in the same syringe", "Double the insulin dose", "Give insulin only IV"], "The if-used-with-insulin block: use different syringe, decreased insulin dose by 50%.")
q(214, "The off-label use of pramlintide based on weight loss is:", ["Obesity", "Cachexia", "Anorexia nervosa", "Malabsorption"], "The side-effect bullet: weight loss - off-label use in obesity.")
q(214, "The MOA of pramlintide is:", ["Delays gastric emptying", "Blocks SGLT2", "Stimulates AMPK", "Blocks alpha-glucosidase"], "The MOA line: delays gastric emptying.")

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
