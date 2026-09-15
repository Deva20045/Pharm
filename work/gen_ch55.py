# -*- coding: utf-8 -*-
import json
CH = 55
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

unit("Development of Glucocorticoids", "Endogenous cortisol replicated ex-vivo gives hydrocortisone - least potent, shortest acting (t½ 8-12 h), glucocorticoid 1x and mineralocorticoid 1x; it is DOC for replacement in Addison's disease and CAH after birth, but gives insufficient immune suppression. Adding a double bond gives prednisone/prednisolone (t½ 12-36 h; glucocorticoid 4x, mineralocorticoid 0.8x); adding a methyl group (water soluble) gives methylprednisolone (glucocorticoid 5x, mineralocorticoid 0.8x). Adding fluoride gives triamcinolone (pure glucocorticoid 5x, mineralocorticoid 0, minimal BP effect) and betamethasone/dexamethasone (t½ 36-72 h, glucocorticoid 30x, mineralocorticoid 0) - dexamethasone being longest acting and most potent.")
q(221, "The endogenous glucocorticoid replicated ex-vivo is:", ["Cortisol", "Aldosterone", "Corticosterone", "DHEA"], "The flowchart starts with endogenous glucocorticoid (cortisol) replicated ex-vivo.")
q(221, "Hydrocortisone is characterized as:", ["Least potent, shortest acting (t½ 8-12 hrs)", "Most potent, longest acting", "Pure glucocorticoid", "Water-soluble methyl derivative"], "The flowchart: hydrocortisone (least potent, shortest acting) t½ 8-12 hrs.")
q(221, "The glucocorticoid : mineralocorticoid potency of hydrocortisone is:", ["1x and 1x", "4x and 0.8x", "5x and 0", "30x and 0"], "The effect block: glucocorticoid 1x > mineralocorticoid 1x.")
q(221, "Hydrocortisone is DOC for replacement in:", ["Addison's disease and CAH after birth", "CAH fetus", "Preterm labour", "Postural hypotension"], "The use block: DOC for replacement - Addison's disease; congenital adrenal hyperplasia (CAH) after birth.")
q(221, "The disadvantage of hydrocortisone is:", ["Insufficient immune suppression", "Excessive immune suppression", "No mineralocorticoid effect", "Poor oral absorption"], "The flowchart: disadvantages - insufficient immune suppression.")
q(221, "Adding a double bond to hydrocortisone produces:", ["Prednisone/prednisolone", "Methylprednisolone directly", "Triamcinolone", "Fludrocortisone"], "The arrow: addition of double bond leads to prednisone/prednisolone.")
q(221, "The half-life of prednisone/prednisolone is:", ["12-36 hrs", "8-12 hrs", "36-72 hrs", "1-2 hrs"], "The block: prednisone/prednisolone t½ 12-36 hrs.")
q(221, "The effect of prednisone/prednisolone is:", ["Glucocorticoid 4x, mineralocorticoid 0.8x", "Glucocorticoid 1x, mineralocorticoid 1x", "Glucocorticoid 5x, mineralocorticoid 0", "Glucocorticoid 30x, mineralocorticoid 0"], "The effect block: glucocorticoid 4x, mineralocorticoid 0.8x.")
q(221, "Adding a methyl group to prednisolone makes it:", ["Water soluble as methylprednisolone", "Lipid soluble", "Longer acting 36-72 h", "Pure mineralocorticoid"], "The arrow: + methyl group (water soluble) leads to methylprednisolone.")
q(221, "The effect of methylprednisolone is:", ["Glucocorticoid 5x, mineralocorticoid 0.8x", "Glucocorticoid 4x, mineralocorticoid 0.8x", "Glucocorticoid 15x, mineralocorticoid 150x", "Glucocorticoid 30x, mineralocorticoid 0"], "The methylprednisolone block: glucocorticoid 5x, mineralocorticoid 0.8x.")
q(221, "Adding fluoride produces the drugs:", ["Triamcinolone and betamethasone/dexamethasone", "Prednisone and methylprednisolone", "Fludrocortisone only", "Cortisone and hydrocortisone"], "The + fluoride branch leads to triamcinolone and betamethasone/dexamethasone.")
q(221, "Triamcinolone is described as:", ["Pure glucocorticoid (minimal effect on BP), glucocorticoid 5x, mineralocorticoid 0", "Mixed glucocorticoid-mineralocorticoid", "Most potent glucocorticoid 30x", "Mineralocorticoid 150x"], "The triamcinolone block: pure glucocorticoids (minimal effect on BP), glucocorticoid 5x, mineralocorticoid 0.")
q(221, "The half-life of betamethasone/dexamethasone is:", ["36-72 hrs", "12-36 hrs", "8-12 hrs", "2-4 hrs"], "The block: betamethasone/dexamethasone t½ 36-72 hrs.")
q(221, "The glucocorticoid potency of betamethasone/dexamethasone is:", ["30x with mineralocorticoid 0", "5x with mineralocorticoid 0", "15x with mineralocorticoid 150x", "4x with mineralocorticoid 0.8x"], "The effect block: glucocorticoid 30x, mineralocorticoid 0.")
q(221, "The glucocorticoid with longest action and most potency is:", ["Dexamethasone", "Hydrocortisone", "Prednisolone", "Triamcinolone"], "The red note: dexamethasone - longest acting, most potent.")
q(221, "Which pair shares pure glucocorticoid action (mineralocorticoid 0)?", ["Triamcinolone and dexamethasone", "Prednisolone and methylprednisolone", "Hydrocortisone and cortisone", "Fludrocortisone and aldosterone"], "Both triamcinolone and betamethasone/dexamethasone blocks show mineralocorticoid 0.")

unit("Uses of Glucocorticoids", "Glucocorticoids decrease inflammation by reducing production of inflammatory mediators (IL-1, IL-6, TNF-alpha), raising anti-inflammatory mediators (IL-10, Annexin 1) and causing lymphocyte redistribution and apoptosis - e.g. rheumatoid arthritis, gout, ankylosing spondylitis. They decrease immunity - e.g. graft vs host disease, graft rejection, myasthenia gravis - and treat neoplasia such as leukemia and lymphoma. Dexamethasone is given in CAH fetus to prevent virilization; in preterm labour steroids mature surfactant, dosed 24 mg over 48 hours - dexamethasone 4 times (6 mg q6h) or betamethasone 2 times (12 mg q24h).")
q(222, "Inflammatory mediators whose production is DECREASED by glucocorticoids are:", ["IL-1, IL-6, TNF-alpha", "IL-10 and Annexin 1", "IL-2 and interferon-gamma only", "Bradykinin and serotonin"], "The MOA bullet: decreased production of inflammatory mediators (IL-1, IL-6, TNF-alpha).")
q(222, "Anti-inflammatory mediators INCREASED by glucocorticoids are:", ["IL-10 and Annexin 1", "IL-1 and IL-6", "TNF-alpha and IL-8", "Histamine and bradykinin"], "The bullet: increased anti-inflammatory mediators (IL-10, Annexin 1).")
q(222, "The cellular immune effects of glucocorticoids written are:", ["Lymphocyte redistribution & apoptosis", "Lymphocyte proliferation", "Neutrophil apoptosis", "Macrophage activation"], "The bullet: lymphocyte redistribution & apoptosis.")
q(222, "Examples of inflammatory conditions treated with glucocorticoids are:", ["Rheumatoid arthritis, gout, ankylosing spondylitis", "Gout, gouty nephropathy, urolithiasis", "RA, SLE only", "OA and fibromyalgia"], "The example line: rheumatoid arthritis, gout, ankylosing spondylitis etc.")
q(222, "Examples where glucocorticoids DECREASE immunity include:", ["Graft vs host disease, graft rejection, myasthenia gravis", "AIDS and tuberculosis", "Leukemia and lymphoma", "CAH and preterm labour"], "The use-2 line: graft vs host disease, graft rejection, myasthenia gravis.")
q(222, "The neoplasia uses of glucocorticoids are:", ["Leukemia and lymphoma", "Solid breast tumors", "Melanoma", "Glioblastoma only"], "The use-3 line: neoplasia - e.g. leukemia, lymphoma.")
q(222, "In CAH fetus, dexamethasone is used to:", ["Prevent virilization", "Mature surfactant", "Induce labour", "Treat hypercalcemia"], "The use-4 line: CAH fetus - dexamethasone used to prevent virilization.")
q(222, "Steroids in preterm labour act by:", ["Surfactant maturation", "Uterine relaxation only", "Cervical ripening", "Antibiotic synergy"], "The use-5 line: preterm labour - surfactant maturation.")
q(222, "The total steroid dose written for preterm labour is:", ["24 mg in 48 hrs", "12 mg in 24 hrs", "6 mg in 48 hrs", "36 mg in 72 hrs"], "The dose line: 24 mg in 48 hrs.")
q(222, "The dexamethasone regimen for preterm labour is:", ["4 times (6 mg q6h)", "2 times (12 mg q24h)", "4 times (12 mg q6h)", "Single 24 mg dose"], "The dose block: dexamethasone 4 times (6 mg q6h).")
q(222, "The betamethasone regimen for preterm labour is:", ["2 times (12 mg q24h)", "4 times (6 mg q6h)", "2 times (6 mg q12h)", "3 times (8 mg q8h)"], "The dose block: betamethasone 2 times (12 mg q24h).")

unit("Side Effects: Cushing's Syndrome", "Cushing's syndrome effects by organ: eye - topical steroids cause glaucoma while systemic use causes posterior sub-capsular cataract; brain (long term use) - psychosis, depression, insomnia; thinning of hair; GIT - gastric ulcers; muscle - myopathy; abdominal striae; bone - osteoporosis from increased Ca++ excretion (hypercalcemia being a secondary use of steroids); skin - thin skin and multiple bruises.")
q(222, "Topical steroid use in the eye causes:", ["Glaucoma", "Posterior sub-capsular cataract", "Optic neuritis", "Papilledema"], "The eye block: topical - glaucoma.")
q(222, "Systemic steroid eye side effect is:", ["Cataract (posterior sub-capsular)", "Open angle glaucoma", "Retinopathy", "Uveitis"], "The eye block: systemic - cataract (posterior sub-capsular).")
q(222, "Long term steroid brain effects are:", ["Psychosis, depression, insomnia", "Seizures and tremor", "Parkinsonism", "Memory improvement"], "The brain block: psychosis, depression, insomnia.")
q(222, "The GIT side effect of steroids is:", ["Gastric ulcers", "Osmotic diarrhea", "Pancreatitis", "Esophageal varices"], "The GIT label: gastric ulcers.")
q(222, "The muscle side effect of steroids is:", ["Myopathy", "Rhabdomyolysis", "Myotonia", "Malignant hyperthermia"], "The muscle label: myopathy.")
q(222, "Steroid osteoporosis occurs due to:", ["Increased Ca++ excretion", "Decreased Ca++ excretion", "Increased Ca++ absorption", "Vitamin D excess"], "The bone label: osteoporosis (D/t increased Ca++ excretion).")
q(222, "Hypercalcemia is a secondary use of steroids because they:", ["Increase Ca++ excretion", "Increase Ca++ absorption", "Stimulate osteoblasts", "Increase vitamin D"], "The bone note: secondary use of steroids - hypercalcemia.")
q(222, "Skin effects of steroids include:", ["Thin skin and multiple bruises", "Hyperpigmentation and thick skin", "Alopecia with scarring", "Ichthyosis"], "The skin block: thin skin, multiple bruises.")
q(222, "Which Cushing feature relates to hair?", ["Thinning of hair", "Hypertrichosis", "Curly regrowth", "Early greying"], "The label at the head: thinning of hair.")
q(222, "Abdominal striae in Cushing's syndrome are:", ["Purple-red stretch marks from skin thinning", "Surgical scars", "Bruises over the abdomen only", "Linear rashes from allergy"], "The figure labels abdominal striae as a body wall feature of Cushing's syndrome.")

unit("Metabolic Side Effects, Contraindications and Exceptions", "Steroids decrease GLUT-4 production causing hyperglycemia that progresses to diabetes mellitus, and lipodystrophy with lemon-on-stick appearance: raised insulin blocks lipolysis causing central obesity, while decreased GLUT-4 in limbs (glucose unavailable) drives lipolysis and thin extremities; buffalo hump completes the picture. Contraindication is infections, with exceptions: H. influenzae meningitis and Covid pneumonia - the only drug that decreases mortality.")
q(223, "Steroids decrease production of:", ["GLUT-4", "Insulin", "Glucagon", "SGLT-2"], "The metabolic block: decreased GLUT 4 production.")
q(223, "The hyperglycemia caused by steroids progresses to:", ["Diabetes mellitus", "Diabetic ketoacidosis only", "Hypoglycemia", "Metabolic alkalosis"], "The flow: hyperglycemia then diabetes mellitus.")
q(223, "The appearance of steroid lipodystrophy is described as:", ["Lemon on stick", "Buffalo on stick", "Apple on table", "Pear shape"], "The lipodystrophy line: lemon on stick appearances.")
q(223, "Central obesity in steroid lipodystrophy is due to:", ["Increased insulin blocking lipolysis", "Increased GLUT-4 in adipose", "Decreased cortisol receptor", "Enhanced lipolysis centrally"], "The chain: increased insulin blocks lipolysis, leading to central obesity.")
q(223, "Thin extremities develop because:", ["Decreased GLUT-4 in limbs (glucose unavailable) causes lipolysis", "Muscle hypertrophy burns fat", "Insulin acts only centrally", "Limb vessels are spared"], "The chain: decreased GLUT 4 in limbs (glucose unavailable), lipolysis, thin extremities.")
q(223, "The third feature of steroid lipodystrophy listed is:", ["Buffalo hump", "Moon face only", "Supraclavicular sparing", "Gynecomastia"], "Item 3: buffalo hump.")
q(223, "The contraindication of steroids written is:", ["Infections", "Pregnancy", "Diabetes", "Hypertension"], "The C/I line: infections.")
q(223, "Exceptions where steroids are allowed despite infection are:", ["H. influenzae meningitis and Covid pneumonia", "Pulmonary TB and fungal sepsis", "Chickenpox and herpes zoster", "All bacterial meningitis"], "The exception list: H. influenza meningitis; covid pneumonia.")
q(223, "In Covid pneumonia, steroids are notable as:", ["The only drug that decreases mortality", "The only antiviral", "Purely symptomatic agents", "Contraindicated"], "The red note: covid pneumonia - only drug that decreases mortality.")

unit("Mineralocorticoids", "Fludrocortisone is exogenous - hydrocortisone plus fluorine - with glucocorticoid 15x and mineralocorticoid 150x effects; uses: adrenal insufficiency (Addison's disease) as hydrocortisone plus fludrocortisone, and postural hypotension (whose DOC is midodrine). Aldosterone is endogenous with glucocorticoid 0 and mineralocorticoid 500x - the pure and most potent mineralocorticoid.")
q(223, "Fludrocortisone is chemically:", ["Hydrocortisone + fluorine", "Cortisol + methyl group", "Prednisolone + double bond", "Aldosterone acetate"], "The line: fludrocortisone (exogenous) - hydrocortisone + flourine.")
q(223, "The effect profile of fludrocortisone is:", ["Glucocorticoid 15x, mineralocorticoid 150x", "Glucocorticoid 150x, mineralocorticoid 15x", "Glucocorticoid 0, mineralocorticoid 500x", "Glucocorticoid 30x, mineralocorticoid 0"], "The effect block: glucocorticoid 15x, mineralocorticoid 150x.")
q(223, "In adrenal insufficiency (Addison's disease), the regimen is:", ["Hydrocortisone + fludrocortisone", "Fludrocortisone alone", "Aldosterone + hydrocortisone", "Dexamethasone + fludrocortisone"], "The use line: adrenal insufficiency (Addison's disease) - hydrocortisone + fludrocortisone.")
q(223, "In postural hypotension, fludrocortisone is used but the DOC is:", ["Midodrine", "Fludrocortisone", "Aldosterone", "Dexamethasone"], "The use line: postural hypotension (DOC midodrine).")
q(223, "The endogenous mineralocorticoid is:", ["Aldosterone", "Fludrocortisone", "Cortisol", "Desoxycorticosterone"], "The block: aldosterone (endogenous).")
q(223, "Aldosterone's effect profile is:", ["Glucocorticoid 0, mineralocorticoid 500x", "Glucocorticoid 15x, mineralocorticoid 150x", "Glucocorticoid 1x, mineralocorticoid 1x", "Glucocorticoid 0, mineralocorticoid 150x"], "The effect block: glucocorticoid 0, mineralocorticoid 500x.")
q(223, "The pure & most potent mineralocorticoid is:", ["Aldosterone", "Fludrocortisone", "Dexamethasone", "Triamcinolone"], "The note: mineralocorticoid 500x (pure & most potent mineralocorticoid).")

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
