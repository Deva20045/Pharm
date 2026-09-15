# -*- coding: utf-8 -*-
import json
CH = 54
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

unit("Growth Hormone Physiology and Actions", "Hypothalamic GHRH stimulates (+, Gs/Gq receptor) while somatostatin inhibits (-, Gi receptor) the pituitary somatotrophic cell. GH acts (+) on the liver to raise IGF-1, which circulates bound to IGF BP-3 and promotes linear growth; GH also acts (+) directly on cells for linear growth, moving glucose inside the cell via the IGF-1 receptor. GH inhibits (-) insulin. Mnemonic: GHRH raises GH; somatostatin lowers GH and TSH.")
q(218, "The hypothalamic hormone that stimulates GH release (+) is:", ["GHRH", "Somatostatin", "Insulin", "IGF-1"], "The diagram: hypothalamus gives GHRH (+) to the pituitary somatotrophic cell.")
q(218, "Somatostatin from the hypothalamus acts on the pituitary via:", ["Gi receptor (-)", "Gs/Gq receptor (+)", "IGF-1 receptor", "GH receptor"], "The legend: somatostatin uses Gi receptor with (-) effect.")
q(218, "GHRH acts on the somatotrophic cell through:", ["Gs/Gq receptor", "Gi receptor", "Nuclear receptor", "Tyrosine kinase receptor only"], "The legend: GHRH uses Gs/Gq receptor.")
q(218, "GH acts on the liver to:", ["Increase IGF-1", "Decrease IGF-1", "Release insulin", "Release glucagon"], "The diagram: GH (+) liver leads to increased IGF-1.")
q(218, "IGF-1 travels in plasma bound to:", ["IGF BP-3", "Albumin only", "GH binding protein", "Corticosteroid binding globulin"], "The plasma box: IGF-1 + IGF BP-3.")
q(218, "The effect of GH on insulin is:", ["Inhibition (-)", "Stimulation (+)", "No effect", "Conversion to IGF-1"], "The diagram arrow: GH (-) insulin.")
q(218, "Direct GH action on the cell increases:", ["Linear growth and glucose inside cell", "Glycogen storage only", "Insulin secretion", "IGF BP-3 synthesis"], "The cell circle: linear growth and increased glucose inside cell.")
q(218, "The IGF-1 receptor mediates:", ["Increased glucose which helps in linear growth", "Decreased glucose uptake", "Insulin release", "TSH release"], "The legend: IGF-1 receptor - increased glucose which helps in linear growth.")
q(218, "Besides lowering GH, somatostatin also lowers:", ["TSH", "ACTH", "LH", "Prolactin"], "The mnemonic line: somatostatin - decreased GH, decreased TSH.")

unit("Dwarfism: GHRH Analogs", "For diagnostic workup of dwarfism, GHRH analogs - sermorelin, macimorelin and tesamorelin - are given: a rise in GH indicates a hypothalamic cause, while no GH change indicates a pituitary cause.")
q(219, "The GHRH analogs listed are:", ["Sermorelin, macimorelin, tesamorelin", "Somatrem, somatropin, mecasermin", "Pasireotide, octreotide, lanreotide", "Pegvisomant, diazoxide"], "The drugs list: sermorelin, macimorelin, tesamorelin.")
q(219, "GHRH analogs in dwarfism are used for:", ["Diagnostic dwarfism", "Routine growth promotion", "Acromegaly treatment", "Weight loss"], "The use line: diagnostic dwarfism.")
q(219, "After the GHRH analog is given, a rise in GH indicates:", ["Hypothalamic cause", "Pituitary cause", "Receptor resistance", "Ectopic GH source"], "The flow: increased GH - hypothalamic cause.")
q(219, "No change in GH after the GHRH analog indicates:", ["Pituitary cause", "Hypothalamic cause", "Drug resistance", "Laboratory error"], "The flow: GH no change - pituitary cause.")

unit("GH and IGF-1 Analogs", "GH analogs somatrem and somatropin have uses mnemonic SMALL: small for gestational age baby, malabsorption with short bowel syndrome (the other drug is teduglutide, a GLP-2 agonist), AIDS related wasting, and decreased length. Side effects mnemonic CHILDREN: carpal tunnel syndrome, hyperglycemia, intracranial pressure rise, leukemia, diabetes mellitus; contraindications are retinopathy and neoplasia. IGF-1 analogs are mecasermin and mecasermin rinfabate (longer acting); side effects hypoglycemia and lipo-hypertrophy; used in dwarfism due to IGF-1 deficiency, GHR mutation and anti-GH antibodies.")
q(219, "The GH analogs listed are:", ["Somatrem and somatropin", "Mecasermin and rinfabate", "Sermorelin and tesamorelin", "Octreotide and lanreotide"], "The drugs list: somatrem, somatropin.")
q(219, "The mnemonic for uses of GH analogs is:", ["SMALL", "CHILDREN", "SOMAT", "GAMS"], "The use block: use SMALL.")
q(219, "In the SMALL mnemonic, 'S' stands for:", ["Small for gestational age baby", "Short bowel syndrome", "Somatotrophin deficiency", "Septo-optic dysplasia"], "The list: small for gestational age baby.")
q(219, "Malabsorption with short bowel syndrome is treated with GH analogs plus:", ["Teduglutide (GLP-2 agonist)", "Liraglutide (GLP-1 agonist)", "Tirzepatide", "Diazoxide"], "The note: other drug teduglutide - GLP-2 agonist.")
q(219, "The wasting condition in SMALL mnemonic is:", ["AIDS related wasting", "Cancer cachexia", "TB wasting", "Anorexia nervosa"], "The list: AIDS related wasting.")
q(219, "The mnemonic for side effects of GH analogs is:", ["CHILDREN", "SMALL", "SOMAT", "EAR"], "The S/E block: S/E CHILDREN.")
q(219, "In CHILDREN, the C and H stand for:", ["Carpal tunnel syndrome, Hyperglycemia", "Cardiomyopathy, Hypoglycemia", "Cataract, Hypertension", "Craniopathy, Hirsutism"], "The list: carpal tunnel syndrome, hyperglycemia.")
q(219, "The CHILDREN mnemonic includes leukemia and:", ["Diabetes mellitus", "Thyrotoxicosis", "Addison disease", "Osteoporosis"], "The list ends: leukemia, diabetes mellitus (with intracranial pressure rise).")
q(219, "Contraindications of GH analogs are:", ["Retinopathy and neoplasia", "Anemia and gout", "Asthma and smoking", "Renal and liver failure"], "The C/I list: retinopathy, neoplasia.")
q(219, "The IGF-1 analogs listed are:", ["Mecasermin and mecasermin rinfabate", "Somatropin and somatrem", "Sermorelin and macimorelin", "Pegvisomant and pasireotide"], "The drugs list: mecasermin; mecasermin rinfabate (longer acting).")
q(219, "Side effects of IGF-1 analogs are:", ["Hypoglycemia and lipo-hypertrophy", "Hyperglycemia and lipo-atrophy", "Gall stones and hypothyroidism", "Carpal tunnel syndrome"], "The S/E list: hypoglycemia, lipo-hypertrophy.")
q(219, "IGF-1 analogs are used in dwarfism due to:", ["IGF-1 deficiency, GHR mutation, anti-GH antibodies", "Only hypothalamic GHRH deficiency", "Pituitary adenoma", "Somatostatinoma"], "The use list: IGF-1 deficiency, GHR mutation, anti-GH Ab.")
q(219, "IGF-1 analogs bypass which level of defect?", ["Both GHR mutation and anti-GH antibodies", "Only liver failure", "Only nutritional deficiency", "Pituitary tumor mass effect"], "The uses (GHR mutation, anti-GH Ab) show action beyond GH itself.")

unit("Acromegaly: Somatostatin Analogs", "For GH excess, somatostatin analogs - pasireotide, octreotide LAR depot and lanreotide (long acting, 30 days) - are given S/C or I/M; side effects hypothyroidism and gall stones. Uses mnemonic SOMAT: secretory diarrhea (also in diarrhea with DM and AIDS), octreotide radiolabeled to diagnose pituitary adenoma, metabolic tumors (glucagonoma DOC; insulinoma DOC diazoxide), acute variceal bleed (DOC terlipressin), acromegaly and thyrotrope adenoma.")
q(220, "The somatostatin analogs listed are:", ["Pasireotide, octreotide LAR depot, lanreotide", "Sermorelin, tesamorelin, macimorelin", "Octreotide, diazoxide, terlipressin", "Pegvisomant, somatropin, somatrem"], "The drugs list: pasireotide, octreotide LAR depot, lanreotide.")
q(220, "Octreotide LAR depot and lanreotide are long acting for about:", ["30 days", "7 days", "24 hours", "6 months"], "The bracket: long acting (30 days).")
q(220, "The routes of somatostatin analogs are:", ["S/C and I/M", "Oral and S/C", "IV and oral", "Only intranasal"], "The route list: S/C, I/M.")
q(220, "Side effects of somatostatin analogs are:", ["Hypothyroidism and gall stones", "Hyperthyroidism and kidney stones", "Optic neuritis and gout", "Lipodystrophy and hypoglycemia"], "The S/E list: hypothyroidism, gall stones.")
q(220, "The mnemonic for uses of somatostatin analogs is:", ["SOMAT", "SMALL", "CHILDREN", "EAR"], "The use block: use SOMAT.")
q(220, "The 'S' in SOMAT is secretory diarrhea, also seen in diarrhea associated with:", ["DM & AIDS", "Cholera only", "IBS only", "Celiac disease"], "The line: secretory diarrhea - also in diarrhea a/w DM & AIDS.")
q(220, "Radiolabeled octreotide is used to diagnose:", ["Pituitary adenoma", "Pancreatic cyst", "Hepatoma", "Medullary carcinoma thyroid"], "The line: octreotide (radiolabeled) for diagnosis of pituitary adenoma.")
q(220, "In metabolic tumors, the DOC of glucagonoma is:", ["Octreotide (somatostatin analog)", "Diazoxide", "Terlipressin", "Pasireotide only"], "The metabolic tumors list: glucagonoma (DOC) under octreotide.")
q(220, "The DOC of insulinoma among metabolic tumors is:", ["Diazoxide", "Octreotide", "Terlipressin", "Lanreotide"], "The list: insulinoma (DOC diazoxide).")
q(220, "In acute variceal bleed, the DOC written is:", ["Terlipressin", "Diazoxide", "Octreotide", "Somatropin"], "The list: acute variceal bleed (DOC terlipressin).")
q(220, "The SOMAT mnemonic's T includes thyrotrope adenoma and:", ["Acromegaly", "TSH-secreting tumor only", "Thyroid carcinoma", "Tetany"], "The use list: acromegaly, thyrotrope adenoma.")

unit("Pegvisomant", "Pegvisomant is a GH receptor blocker used in resistant acromegaly. Its side effects are hepatotoxicity (monitor LFTs) and increased adenoma size - raised GHRH drives somatotrophin cell hypertrophy. Monitoring: MRI for size, IGF-1 levels and visual fields because the adenoma may sit near the optic chiasma.")
q(220, "The MOA of pegvisomant is:", ["GH receptor blocker", "Somatostatin analog", "GHRH antagonist", "Dopamine agonist"], "The MOA line: GH receptor blocker.")
q(220, "Pegvisomant is used in:", ["Resistant acromegaly", "First line acromegaly", "Dwarfism", "Secretory diarrhea"], "The use line: resistant acromegaly.")
q(220, "Pegvisomant hepatotoxicity requires:", ["Monitoring LFT", "Weekly CBC", "Monthly ECG", "Visual field charting only"], "The S/E line: hepatotoxicity (monitor LFT).")
q(220, "Pegvisomant can increase adenoma size because:", ["Increased GHRH leads to somatotrophin cell hypertrophy", "It stimulates GH receptors", "It converts to IGF-1", "It blocks apoptosis"], "The note: increased GHRH (+) leads to somatotrophin cell hypertrophy.")
q(220, "The three monitoring parameters written for pegvisomant are:", ["MRI size, IGF-1 levels, visual field", "LFT, CBC, ECG", "GH level, glucose, weight", "TSH, prolactin, cortisol"], "The monitor list: monitor size MRI, monitor IGF-1 levels, monitor visual field.")
q(220, "Visual field monitoring in pegvisomant is needed because:", ["Adenoma near optic chiasma", "Retinopathy risk", "Papilledema", "Cortical blindness"], "The note: monitor visual field - adenoma near optic chiasma.")

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
