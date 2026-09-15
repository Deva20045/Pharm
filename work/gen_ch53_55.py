# -*- coding: utf-8 -*-
"""Generate chapters 53-55 from Marrow Pharmacology E8, book pp215-223.

ch53 Drugs Acting on Reproductive System (p215-217)
ch54 Growth Hormone and Related Drugs (p218-220)
ch55 Steroids (p221-223)
"""
import json
from pathlib import Path
Q=[]; U=[]; CH=0; CUR=None

def start(ch):
    global Q,U,CH,CUR; Q=[];U=[];CH=ch;CUR=None

def unit(title,guide):
    global CUR
    if CUR: close()
    CUR={'title':title,'start':len(Q),'guide':guide}

def close():
    global CUR
    if CUR is not None: CUR['end']=len(Q);U.append(CUR);CUR=None

def q(p,text,answer,wrong,exp=None):
    assert CUR and len(wrong)==3 and answer not in wrong
    assert len(set([answer]+wrong))==4, f'duplicate options: {text}'
    Q.append({'id':'','sec':CUR['title'],'page':p,'q':text,'opts':[answer]+wrong,'ans':0,
              'exp':(exp or answer.rstrip('.'))+f' (Book p{p})'})

def facts(p, rows):
    for row in rows:
        q(p,*row)

def finish():
    close()
    for i,x in enumerate(Q,1): x['id']=f'PHARM-C{CH}-{i:03d}'
    units=[]
    for n,u in enumerate(U,1):
        ids=[x['id'] for x in Q[u['start']:u['end']]]
        units.append({'id':f'PHARM-U{CH}-{n}','ch':CH,'n':n,'title':u['title'],
                      'sec':f"{u['title']} · p{Q[u['start']]['page']}",'qs':ids,'guide':u['guide']})
    Path('data').mkdir(exist_ok=True)
    json.dump({'questions':Q,'units':units},open(f'data/ch{CH:02d}.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
    print(f'ch{CH}: {len(Q)} questions, {len(units)} units')

# CHAPTER 53 - DRUGS ACTING ON REPRODUCTIVE SYSTEM (p215-217) ------------------
start(53)
unit('GnRH and the Hypothalamo-Pituitary Axis',
 'The hypothalamus releases GnRH (pulsatile release) which acts on the Gs/q receptor on pituitary gonadotroph cells, increasing LH/FSH. In females: ovulation (LH surge) and synthesis of estrogen and progesterone; in males: spermatogenesis and testosterone.')
facts(215,[
('The release of GnRH from the hypothalamus is:','Pulsatile',['Continuous','Tonic only','Circadian fixed'],'Diagram: GnRH (pulsatile release).'),
('GnRH acts on the pituitary through:','Gs/q receptor on gonadotroph cells',['Gi receptor','Tyrosine kinase receptor','Intracellular steroid receptor'],'Diagram: Gs/q receptor on pituitary gonadotroph cells.'),
('GnRH increases the release of:','LH/FSH',['ACTH and TSH','GH and prolactin','Oxytocin and ADH'],'GnRH -> pituitary -> increased LH/FSH.'),
('LH surge in females produces:','Ovulation',['Spermatogenesis','Menstruation','Implantation'],'Females: ovulation (LH surge).'),
('LH/FSH in females also increases the synthesis of:','Estrogen and progesterone',['Testosterone only','Oxytocin','Relaxin only'],'Females: synthesis of estrogen and progesterone.'),
('LH/FSH in males produces:','Spermatogenesis and testosterone',['Ovulation','Milk ejection','Prostate involution'],'Males: spermatogenesis, testosterone.'),
])
unit('GnRH Agonists and Their Dosing Logic',
 'GnRH agonists: goserelin, buserelin, nafarelin and leuprolide. Intermittent dosing increases LH/FSH - used in infertility due to anovulation/oligospermia and delayed puberty. Continuous dosing gives initial increase then decrease of LH/FSH (due to receptor downregulation) - used in precocious puberty, estrogen dependent conditions (ER positive breast cancer, endometriosis, fibroids) and testosterone dependent cancers (prostate cancer, DOC goserelin). GnRH analog: gonadorelin - used for diagnosis of cause of hypogonadism (hypothalamic/pituitary) and anovulation.')
facts(215,[
('The GnRH agonists are:','Goserelin, buserelin, nafarelin and leuprolide',['Cetrorelix and ganirelix','Gonadorelin only','Elagolix and abarelix'],'GnRH agonists: goserelin, buserelin, nafarelin, leuprolide.'),
('Intermittent dosing of GnRH agonists produces:','Increased LH/FSH',['Decreased LH/FSH','Initial increase then decrease','No change'],'GnRH agonists: intermittent dosing - increased LH/FSH.'),
('Continuous dosing of GnRH agonists produces:','LH/FSH initial increase then decrease (receptor downregulation)',['Sustained increase of LH/FSH','Immediate fall of LH/FSH','No effect on LH/FSH'],'Continuous dosing: LH/FSH initial increase then decrease (D/t receptor downregulation).'),
('Intermittent GnRH agonist dosing is used in:','Infertility due to anovulation/oligospermia and delayed puberty',['Precocious puberty','Prostate cancer','Endometriosis'],'Intermittent use: infertility D/t anovulation, oligospermia; delayed puberty.'),
('Continuous GnRH agonist dosing is used in:','Precocious puberty',['Delayed puberty','Anovulatory infertility','Oligospermia'],'Continuous use: precocious puberty.'),
('Estrogen dependent conditions treated with continuous GnRH agonists include:','ER positive breast cancer, endometriosis and fibroids',['ER negative breast cancer','PCOS','Prostatic hypertrophy only'],'Continuous use: estrogen dependent conditions - ER positive breast cancer, endometriosis, fibroids.'),
('The DOC for prostate cancer among GnRH agonists is:','Goserelin',['Leuprolide','Nafarelin','Buserelin'],'Testosterone dependent cancers - prostate cancer (DOC: goserelin).'),
('The GnRH analog used for diagnosis of the cause of hypogonadism is:','Gonadorelin',['Goserelin','Leuprolide','Nafarelin'],'GnRH analog: gonadorelin - diagnosis of cause of hypogonadism (hypothalamic/pituitary).'),
('Gonadorelin is also used in:','Anovulation',['Precocious puberty','Fibroids','Hirsutism'],'Gonadorelin use: anovulation.'),
])
unit('GnRH Antagonists',
 'GnRH antagonists decrease LH/FSH: ganirelix, cetrorelix, abarelix and elagolix.')
facts(215,[
('The GnRH antagonists are:','Ganirelix, cetrorelix, abarelix and elagolix',['Goserelin and leuprolide','Buserelin and nafarelin','Gonadorelin'],'GnRH antagonists: ganirelix, cetrorelix, abarelix, elagolix.'),
('GnRH antagonists produce:','Decreased LH/FSH',['Increased LH/FSH','Initial flare then block','Pulsatile LH release'],'GnRH antagonists: decreased LH/FSH.'),
('Elagolix is a:','GnRH antagonist',['GnRH agonist','GnRH analog','Estrogen agonist'],'GnRH antagonist list: ganirelix, cetrorelix, abarelix, elagolix.'),
])
unit('Selective Estrogen Receptor Modulators (SERM)',
 'Tamoxifen: treatment of ER(+) breast cancer in premenopausal females. Raloxifene: prophylaxis of ER(+) breast cancer and post-menopausal osteoporosis in females with high risk for ER(+) Ca breast, used in post-menopausal females. Common side effects: uterine carcinoma (only tamoxifen), thrombosis and hot flashes. Other SERMs: toremifene (treatment of ER(+) breast cancer) and ospemifene (post-menopausal dyspareunia).')
facts(216,[
('The SERM used for treatment of ER(+) breast cancer is:','Tamoxifen',['Raloxifene','Clomiphene','Fulvestrant'],'Tamoxifen use: treatment of ER(+) breast cancer.'),
('Raloxifene is used for:','Prophylaxis of ER(+) breast cancer and post-menopausal osteoporosis (high risk for ER+ Ca breast)',['Treatment of ER+ breast cancer only','Ovarian cancer','Endometriosis'],'Raloxifene use: prophylaxis of ER(+) breast cancer; post-menopausal osteoporosis in females with high risk for ER(+) Ca breast.'),
('Tamoxifen is used in which age group?','Premenopausal females',['Post-menopausal females only','Only children','Only males'],'Age group: tamoxifen - premenopausal females; raloxifene - post-menopausal females.'),
('Raloxifene is used in which age group?','Post-menopausal females',['Premenopausal females','Adolescents','Any age'],'Raloxifene: post-menopausal females.'),
('The SERM side effect limited to tamoxifen is:','Uterine carcinoma',['Thrombosis','Hot flashes','Osteoporosis'],'S/E: uterine carcinoma (only tamoxifen).'),
('The common SERM side effects are:','Thrombosis and hot flashes',['Deafness and neuropathy','Nephrotoxicity','Hepatotoxicity only'],'SERM S/E: thrombosis; hot flashes.'),
('The other SERM used for treatment of ER(+) breast cancer is:','Toremifene',['Ospemifene','Clomiphene','Elacestrant'],'Other SERMs: toremifene - treatment of ER(+) breast cancer.'),
('Ospemifene is used for:','Post-menopausal dyspareunia',['Breast cancer','Osteoporosis','Infertility'],'Other SERMs: ospemifene - post-menopausal dyspareunia.'),
])
unit('Selective Estrogen Receptor Downregulator (SERD): Clomiphene, Fulvestrant and Elacestrant',
 'Clomiphene citrate: partial agonist at pituitary estrogen receptor -> positive feedback to hypothalamus -> increased GnRH -> increased LH -> ovulation; use: DOC for anovulation without PCOS. Note: DOC for anovulation with PCOS is letrozole. Fulvestrant: blocks ER at breast, potency 100x tamoxifen, used in resistant post-menopausal breast cancer. Elacestrant: ER+ve breast cancer with ESR1 mutation (estrogen receptor 1).')
facts(216,[
('The MOA of clomiphene citrate is:','Partial agonist at pituitary estrogen receptor',['Complete antagonist at ovarian receptors','Aromatase inhibition','ER destruction at breast'],'Clomiphene MOA: partial agonist at pituitary estrogen receptor.'),
('Clomiphene increases LH by:','Positive feedback to hypothalamus -> increased GnRH -> increased LH',['Direct pituitary stimulation of LH genes','Blocking dopamine','Increasing FSH only'],'Chain: positive feedback to hypothalamus -> increased GnRH -> increased LH -> ovulation.'),
('The use of clomiphene citrate is:','DOC for anovulation without PCOS',['DOC for anovulation with PCOS','Breast cancer treatment','Post-menopausal osteoporosis'],'Clomiphene use: DOC for anovulation without PCOS.'),
('The DOC for anovulation with PCOS is:','Letrozole',['Clomiphene citrate','Tamoxifen','HMG'],'Note: DOC for anovulation with PCOS is letrozole.'),
('The MOA of fulvestrant is:','Blocks ER at breast',['Partial agonist at pituitary','Blocks ER at uterus','Aromatase inhibition'],'Fulvestrant MOA: blocks ER at breast.'),
('The potency of fulvestrant compared to tamoxifen is:','100x',['10x','2x','500x'],'Fulvestrant potency: 100x tamoxifen.'),
('Fulvestrant is used in:','Resistant post-menopausal breast cancer',['Premenopausal breast cancer','Anovulation','Male infertility'],'Fulvestrant use: resistant post-menopausal breast cancer.'),
('Elacestrant is used in:','ER+ve breast cancer with ESR1 mutation (estrogen receptor 1)',['ER-negative breast cancer','Anovulation with PCOS','Prostate cancer'],'Elacestrant use: ER+ve breast cancer with ESR1 mutation (estrogen receptor 1).'),
])
unit('Selective Progesterone Receptor Modulator (SPRM) and Emergency Contraception',
 'Ulipristal: use - emergency contraception; dose 30 mg single dose within 5d of unprotected intercourse. Note: DOC for emergency contraception in India is levonorgestrel - 1.5 mg single dose within 72h of unprotected intercourse (or) 0.75 mg two doses 12h apart within 72h of unprotected intercourse.')
facts(217,[
('The SPRM (selective progesterone receptor modulator) is:','Ulipristal',['Mifepristone only','Raloxifene','Clomiphene'],'SPRM: ulipristal.'),
('The use of ulipristal is:','Emergency contraception',['Induction of labour','Fibroid surgery only','IVF stimulation'],'Ulipristal use: emergency contraception.'),
('The dose of ulipristal for emergency contraception is:','30 mg single dose within 5d of unprotected intercourse',['1.5 mg single dose within 72h','0.75 mg two doses 12h apart','150 mg IM injection'],'Ulipristal dose: 30 mg single dose within 5d of unprotected intercourse.'),
('The DOC for emergency contraception in India is:','Levonorgestrel',['Ulipristal','Mifepristone','Ethinyl estradiol'],'Note: DOC for emergency contraception in India - levonorgestrel.'),
('The dose of levonorgestrel for emergency contraception is:','1.5 mg single dose within 73h (or) 0.75 mg two doses 12h apart within 73h',['30 mg single dose within 5 days','0.15 mg daily for 21 days','75 mg weekly'],'Levonorgestrel dose: 1.5 mg single dose within 73h of unprotected intercourse (or) 0.75 mg two doses 12h apart within 73h.'),
])
unit('5-alpha Reductase Inhibitors',
 'MOA: block conversion of testosterone to dihydrotestosterone (DHT). Drugs: finasteride and dutasteride. Use: DOC for androgenic alopecia (dose 1 mg) and benign prostatic hyperplasia (BPH) - reduces size & weight of prostate improving outcome. Note: DOC for BPH (symptomatic relief) is tamsulosin/silodosin.')
facts(217,[
('5-alpha reductase inhibitors block the conversion of:','Testosterone -> dihydrotestosterone (DHT)',['Testosterone -> estrogen','DHT -> testosterone','Androstenedione -> testosterone'],'MOA: testosterone -> (X) -> dihydrotestosterone (DHT).'),
('The 5-alpha reductase inhibitors are:','Finasteride and dutasteride',['Flutamide and bicalutamide','Leuprolide and goserelin','Tamsulosin and silodosin'],'Drugs: finasteride / dutasteride.'),
('The DOC for androgenic alopecia is:','Finasteride (dose 1 mg)',['Dutasteride 5 mg','Minoxidil oral','Testosterone gel'],'Use: DOC for androgenic alopecia (dose 1 mg).'),
('5-alpha reductase inhibitors in BPH act by:','Reducing size & weight of prostate -> improves outcome',['Relaxing prostatic smooth muscle','Blocking prostatic receptors acutely','Dissolving prostatic calculi'],'Use: BPH - reduces size & weight of prostate -> improves outcome.'),
('The DOC for BPH (symptomatic) is:','Tamsulosin / silodosin',['Finasteride','Dutasteride','Flutamide'],'Note: DOC for BPH - tamsulosin / silodosin.'),
])
unit('Androgen Receptor Blockers and Aromatase Inhibitors',
 'Androgen receptor blockers: flutamide, bicalutamide, enzalutamide and apalutamide; use: add-on drug for prostate cancer and hirsutism. Side effects are seen more with androgen receptor blockers than 5-alpha reductase inhibitors: gynecomastia and impotence. Aromatase inhibitors (MOA in adipocytes of post-menopausal females - block testosterone to estrogen): exemestane and letrozole; use: DOC for post-menopausal ER(+) Ca breast and anovulation due to PCOS. Note: DOC in gender change surgeries is leuprolide.')
facts(217,[
('The androgen receptor blockers are:','Flutamide, bicalutamide, enzalutamide and apalutamide',['Finasteride and dutasteride','Tamsulosin and silodosin','Goserelin and leuprolide'],'Androgen receptor blockers: flutamide, bicalutamide, enzalutamide, apalutamide.'),
('The uses of androgen receptor blockers are:','Add-on drug for prostate cancer and hirsutism',['DOC for BPH monotherapy','Androgenic alopecia','Precocious puberty'],'Use: add-on drug for prostate cancer; hirsutism.'),
('Side effects (gynecomastia and impotence) are seen more with:','Androgen receptor blockers > 5-alpha reductase inhibitors',['5-alpha reductase inhibitors > AR blockers','Only with GnRH agonists','Equally with both'],'S/E seen in androgen receptor blockers > 5-alpha reductase inhibitors: gynecomastia, impotence.'),
('The aromatase inhibitors are:','Exemestane and letrozole',['Anastrozole and tamoxifen','Finasteride and dutasteride','Flutamide and bicalutamide'],'Aromatase inhibitors drugs: exemestane, letrozole.'),
('The MOA site of aromatase inhibitors is:','Adipocytes of post-menopausal females (block testosterone -> estrogen)',['Ovaries of premenopausal females','Pituitary','Adrenal cortex'],'MOA: in adipocytes of post-menopausal females - testosterone (X aromatase) -> estrogen.'),
('Aromatase inhibitors are DOC for:','Post-menopausal ER(+) Ca breast and anovulation due to PCOS',['Premenopausal ER+ breast cancer','Anovulation without PCOS','Prostate cancer'],'Use DOC: post-menopausal ER(+) Ca breast; anovulation D/t PCOS.'),
('The DOC in gender change surgeries is:','Leuprolide',['Letrozole','Goserelin','Flutamide'],'Note: DOC in gender change surgeries -> leuprolide.'),
])
finish()

# CHAPTER 54 - GROWTH HORMONE AND RELATED DRUGS (p218-220) ---------------------
start(54)
unit('Growth Hormone Physiology and Actions',
 'Hypothalamus releases GHRH (+, Gs/q receptor) and somatostatin (-, Gi receptor) acting on the pituitary somatotrophic cell to regulate GH. GH acts on the GH receptor (increased linear growth), on liver to increase IGF-1 (+, via IGF-1 receptor increasing glucose inside cell which helps linear growth), and inhibits (-) insulin. IGF-1 travels in plasma bound to IGF BP-3. Note: GHRH -> increased GH; somatostatin -> decreased GH and decreased TSH.')
facts(218,[
('GH secretion is increased by:','GHRH (+)',['Somatostatin (-)','Insulin (-)','IGF BP-3'],'Diagram: GHRH (+) -> GH.'),
('Somatostatin acts on the somatotrophic cell through:','Gi receptor (-)',['Gs/q receptor (+)','Tyrosine kinase receptor','Nuclear receptor'],'Somatostatin: Gi receptor (-).'),
('GHRH acts on the somatotrophic cell through:','Gs/q receptor',['Gi receptor','GH receptor','IGF-1 receptor'],'GHRH: Gs/q receptor (+).'),
('GH is released from:','Somatotrophic cells of pituitary',['Beta cells','Gonadotrophs','Thyrotrophs'],'Diagram: somatotrophic cell -> GH.'),
('GH produces linear growth by acting on:','GH receptor directly',['Only through IGF-1','GH receptor on liver only','IGF BP-3 receptor'],'GH receptor: increased linear growth (direct effect).'),
('GH increases IGF-1 from the:','Liver',['Kidney','Pituitary','Adipose tissue'],'Diagram: GH (+) -> liver -> increased IGF-1.'),
('IGF-1 travels in plasma bound to:','IGF BP-3',['Albumin','IGF BP-1 only','GH binding protein'],'Diagram: IGF-1 + IGF BP-3 in plasma.'),
('The IGF-1 receptor in the cell increases:','Glucose inside cell which helps in linear growth',['Glycogen breakdown','Lipolysis only','Protein catabolism'],'IGF-1 receptor: increased glucose which helps in linear growth.'),
('GH has what effect on insulin?','Inhibits (-) insulin',['Stimulates insulin','No interaction','Degrades insulin'],'Diagram: GH (-) -> insulin.'),
('Somatostatin decreases:','GH and TSH',['Only GH','GH and ACTH','TSH and LH'],'Note: somatostatin -> decreased GH, decreased TSH.'),
])
unit('Dwarfism (GH Decrease): GHRH Analogs, GH Analogs and IGF-1 Analogs',
 'GHRH analogs: sermorelin, macimorelin and tesamorelin - used for diagnostic dwarfism: if GH increases the cause is hypothalamic, if GH shows no change the cause is pituitary. GH analogs: somatrem and somatropin - use SMALL (small for gestational age baby, malabsorption with short bowel syndrome - other drug teduglutide a GLP-2 agonist, AIDS related wasting, decreased length); S/E CHILDREN (carpal tunnel syndrome, hyperglycemia, intracranial pressure increase, leukemia, diabetes mellitus); C/I retinopathy and neoplasia. IGF-1 analogs: mecasermin and mecasermin rinfabate (longer acting); S/E hypoglycemia and lipohypertrophy; use - dwarfism due to IGF-1 deficiency, GHR mutation and anti-GH antibodies.')
facts(219,[
('The GHRH analogs are:','Sermorelin, macimorelin and tesamorelin',['Somatrem and somatropin','Mecasermin and rinfabate','Octreotide and lanreotide'],'GHRH analogs: sermorelin, macimorelin, tesamorelin.'),
('GHRH analogs are used in:','Diagnostic dwarfism',['Treatment of acromegaly','GH replacement in adults','Weight loss'],'GHRH analogs use: diagnostic dwarfism.'),
('In diagnostic dwarfism, GH increases after drug given - the cause is:','Hypothalamic',['Pituitary','Ectopic GH','Receptor resistance'],'Drug given -> increased GH: hypothalamic cause; GH no change: pituitary cause.'),
('In diagnostic dwarfism, no change in GH after drug given - the cause is:','Pituitary',['Hypothalamic','Hypothalamic and pituitary combined','Drug failure'],'Drug given -> GH no change: pituitary cause.'),
('The GH analogs are:','Somatrem and somatropin',['Sermorelin and macimorelin','Mecasermin and mecasermin rinfabate','Pasireotide and lanreotide'],'GH analogs: somatrem, somatropin.'),
('The mnemonic for uses of GH analogs is:','SMALL',['CHILDREN','SOMAT','GAMES'],'GH analogs use: SMALL.'),
('In the SMALL mnemonic, SM stands for:','Small for gestational age baby and malabsorption with short bowel syndrome',['Somatotroph stimulation','Secretory myopathy','Sella mass'],'SMALL: small for gestational age baby; malabsorption with short bowel syndrome.'),
('The other drug for malabsorption with short bowel syndrome is:','Teduglutide (GLP-2 agonist)',['Tesamorelin','Mecasermin','Pegvisomant'],'Short bowel syndrome: other drug teduglutide - GLP-2 agonist.'),
('The AL of SMALL stands for:','AIDS related wasting and decreased length',['Acromegaly and lipodystrophy','Adenoma and leukemia','Amenorrhea and lactation'],'SMALL: AIDS related wasting; decreased length.'),
('The mnemonic for side effects of GH analogs is:','CHILDREN',['SMALL','SOMAT','SHORT'],'GH analog S/E: CHILDREN.'),
('In the CHILDREN mnemonic, CHI stands for:','Carpal tunnel syndrome, hyperglycemia and intracranial pressure increase',['Cretinism','Cholestasis','Cardiac hypertrophy'],'CHILDREN: carpal tunnel syndrome; hyperglycemia; intracranial pressure increase.'),
('In the CHILDREN mnemonic, LDREN stands for:','Leukemia, diabetes mellitus (and retinopathy/neoplasia as C/I)',['Lipodystrophy','Renal failure','Deafness'],'CHILDREN: leukemia; diabetes mellitus.'),
('GH analogs are contraindicated in:','Retinopathy and neoplasia',['Pregnancy only','Hypertension','Asthma'],'C/I: retinopathy; neoplasia.'),
('The IGF-1 analogs are:','Mecasermin and mecasermin rinfabate (longer acting)',['Somatrem and somatropin','Sermorelin and tesamorelin','Octreotide and pasireotide'],'IGF-1 analogs: mecasermin; mecasermin rinfabate (longer acting).'),
('The side effects of IGF-1 analogs are:','Hypoglycemia and lipohypertrophy',['Hyperglycemia and carpal tunnel','Leukemia','Intracranial hypertension'],'IGF-1 analog S/E: hypoglycemia; lipohypertrophy.'),
('IGF-1 analogs are used in dwarfism due to:','IGF-1 deficiency, GHR mutation and anti-GH antibodies',['Hypothalamic GHRH deficiency','Pituitary agenesis only','Malnutrition only'],'IGF-1 analog use: dwarfism due to IGF-1 deficiency; GHR mutation; anti-GH Ab.'),
])
unit('Acromegaly (GH Increase): Somatostatin Analogs and Pegvisomant',
 'Somatostatin analogs: pasireotide, octreotide LAR depot and lanreotide (long acting 30 days); route S/C and I/M; S/E hypothyroidism and gall stones. Uses (SOMAT): secretory diarrhea (also in diarrhea with DM & AIDS), octreotide (radiolabeled) for diagnosis of pituitary adenoma, metabolic tumors (glucagonoma DOC; insulinoma DOC diazoxide), acute variceal bleed (DOC terlipressin), acromegaly and thyrotrope adenoma. Pegvisomant: MOA GH receptor blocker; use resistant acromegaly; S/E hepatotoxicity (monitor LFT) and increased adenoma size (increased GHRH -> somatotrophin cell hypertrophy) - monitor size (MRI), IGF-1 levels and visual field (adenoma near optic chiasma).')
facts(220,[
('The somatostatin analogs are:','Pasireotide, octreotide LAR depot and lanreotide',['Sermorelin and tesamorelin','Pegvisomant only','Octreotide IV only'],'Somatostatin analogs: pasireotide, octreotide LAR depot, lanreotide.'),
('The long acting (30 days) somatostatin analogs are:','Octreotide LAR depot and lanreotide',['Pasireotide daily','Octreotide S/C TDS','All are short acting'],'Long acting (30 days): octreotide LAR depot, lanreotide.'),
('The routes of somatostatin analogs are:','S/C and I/M',['Oral','Inhalational','Rectal'],'Route: S/C; I/M.'),
('The side effects of somatostatin analogs are:','Hypothyroidism and gall stones',['Hyperthyroidism','Nephrolithiasis','Pancreatitis'],'S/E: hypothyroidism; gall stones.'),
('The mnemonic for uses of somatostatin analogs is:','SOMAT',['SMALL','CHILDREN','EAR'],'Somatostatin analogs use: SOMAT.'),
('In SOMAT, S stands for:','Secretory diarrhea (also in diarrhea with DM & AIDS)',['Sellar tumors','Spasm of sphincter of Oddi only','Steatorrhea'],'SOMAT: secretory diarrhea - also in diarrhea a/w DM & AIDS.'),
('Radiolabeled octreotide is used for:','Diagnosis of pituitary adenoma',['Treatment of dwarfism','GH stimulation test','Insulinoma treatment'],'SOMAT: O - octreotide (radiolabeled) for diagnosis of pituitary adenoma.'),
('The metabolic tumor treated by octreotide as DOC is:','Glucagonoma',['Insulinoma','Gastrinoma','VIPoma only'],'SOMAT: M - metabolic tumors - glucagonoma (DOC).'),
('The DOC for insulinoma is:','Diazoxide',['Octreotide','Pasireotide','Diazepam'],'Metabolic tumors: insulinoma (DOC diazoxide).'),
('The DOC for acute variceal bleed is:','Terlipressin',['Octreotide','Somatostatin','Vasopressin'],'SOMAT: A - acute variceal bleed (DOC terlipressin).'),
('The uses of somatostatin analogs in SOMAT also include:','Acromegaly and thyrotrope adenoma',['Dwarfism and gigantism','Prolactinoma','Cushing disease only'],'SOMAT: A - acromegaly; T - thyrotrope adenoma.'),
('The MOA of pegvisomant is:','GH receptor blocker',['Somatostatin analog','GH antibody induction','Dopamine agonist'],'Pegvisomant MOA: GH receptor blocker.'),
('Pegvisomant is used in:','Resistant acromegaly',['Acromegaly first line','Dwarfism','Pituitary cachexia'],'Pegvisomant use: resistant acromegaly.'),
('The side effects of pegvisomant are:','Hepatotoxicity (monitor LFT) and increased adenoma size',['Hypothyroidism and gall stones','Hypoglycemia','Nephrotoxicity'],'Pegvisomant S/E: hepatotoxicity (monitor LFT); increased adenoma size.'),
('Increased adenoma size with pegvisomant occurs due to:','Increased GHRH -> somatotrophin cell hypertrophy',['Direct tumor growth stimulation','Receptor agonist activity','Malignant transformation'],'Increased adenoma size: increased GHRH (+) -> somatotrophin cell hypertrophy.'),
('Adenoma monitoring with pegvisomant includes:','Size by MRI, IGF-1 levels and visual field (adenoma near optic chiasma)',['Only LFT monthly','Serum GH hourly','Biopsy yearly'],'Monitor: size - MRI; monitor IGF-1 levels; monitor visual field - adenoma near optic chiasma.'),
])
finish()

# CHAPTER 55 - STEROIDS (p221-223) ---------------------------------------------
start(55)
unit('Development of Glucocorticoids: Hydrocortisone to Prednisolone',
 'The endogenous glucocorticoid cortisol is replicated ex-vivo as hydrocortisone - least potent, shortest acting (t 1/2 8-12 hrs), effect glucocorticoid 1x > mineralocorticoid 1x; use: DOC for replacement in Addison\'s disease and congenital adrenal hyperplasia (CAH) after birth; disadvantage: insufficient immune suppression. Addition of a double bond gives prednisone/prednisolone (t 1/2 12-36 hrs) with glucocorticoid 4x and mineralocorticoid 0.8x; adding a methyl group (water soluble) gives methylprednisolone (t 1/2 12-36 hrs) with glucocorticoid 5x and mineralocorticoid 0.8x.')
facts(221,[
('The endogenous glucocorticoid replicated ex-vivo is:','Hydrocortisone (cortisol)',['Prednisolone','Dexamethasone','Methylprednisolone'],'Development: endogenous glucocorticoid (cortisol) replicated ex-vivo -> hydrocortisone.'),
('The least potent and shortest acting glucocorticoid is:','Hydrocortisone',['Prednisolone','Triamcinolone','Dexamethasone'],'Hydrocortisone: least potent, shortest acting.'),
('The half life of hydrocortisone is:','8-12 hrs',['12-36 hrs','36-72 hrs','2-4 hrs'],'Hydrocortisone t 1/2 = 8-12 hrs.'),
('The potency of hydrocortisone is:','Glucocorticoid 1x, mineralocorticoid 1x',['GC 4x, MC 0.8x','GC 5x, MC 0.8x','GC 30x, MC 0'],'Effect: glucocorticoid 1x > mineralocorticoid 1x.'),
('Hydrocortisone is the DOC for replacement in:','Addison\'s disease and CAH after birth',['Congenital adrenal hyperplasia in fetus only','SIADH','Addisonian crisis prevention in athletes'],'Use: DOC for replacement - Addison\'s disease; congenital adrenal hyperplasia (CAH) after birth.'),
('The disadvantage of hydrocortisone for immune diseases is:','Insufficient immune suppression',['Too much immune suppression','Severe mineralocorticoid excess','Poor oral absorption'],'Disadvantage: insufficient immune suppression.'),
('Prednisone and prednisolone are formed from hydrocortisone by:','Addition of a double bond',['Addition of fluorine','Addition of a methyl group only','Hydroxylation'],'Step: addition of double bond -> prednisone/prednisolone.'),
('The half life of prednisone/prednisolone is:','12-36 hrs',['8-12 hrs','36-72 hrs','1-2 hrs'],'Prednisone + prednisolone: t 1/2 = 12-36 hrs.'),
('The potency of prednisone/prednisolone is:','Glucocorticoid 4x, mineralocorticoid 0.8x',['GC 5x, MC 0.8x','GC 1x, MC 1x','GC 15x, MC 150x'],'Effect: glucocorticoid 4x, mineralocorticoid 0.8x.'),
('Methylprednisolone is formed from prednisolone by adding:','Methyl group (water soluble)',['Fluoride','Double bond','Hydroxyl group'],'+ methyl group (water soluble) -> methylprednisolone.'),
('The potency of methylprednisolone is:','Glucocorticoid 5x, mineralocorticoid 0.8x',['GC 4x, MC 0.8x','GC 30x, MC 0','GC 5x, MC 5x'],'Methylprednisolone: t 1/2 = 12-36 hrs; glucocorticoid 5x, mineralocorticoid 0.8x.'),
])
unit('Pure Glucocorticoids: Triamcinolone, Betamethasone and Dexamethasone',
 'Addition of fluoride gives the pure glucocorticoids (minimal effect on BP). Triamcinolone (t 1/2 12-36h): glucocorticoid 5x, mineralocorticoid 0. Betamethasone and dexamethasone (t 1/2 36-72 hrs): glucocorticoid 30x, mineralocorticoid 0. Dexamethasone is the longest acting and most potent.')
facts(221,[
('Pure glucocorticoids are formed by addition of:','Fluoride',['Methyl group','Double bond','Hydroxyl group'],'+ fluoride -> pure glucocorticoids.'),
('Pure glucocorticoids have minimal effect on:','BP (no mineralocorticoid effect)',['Immunity','Blood glucose','Bone density'],'Pure glucocorticoids: minimal effect on BP.'),
('The half life of triamcinolone is:','12-36 hrs',['8-12 hrs','36-72 hrs','2-4 hrs'],'Triamcinolone: t 1/2 = 12-36 h.'),
('The potency of triamcinolone is:','Glucocorticoid 5x, mineralocorticoid 0',['GC 5x, MC 0.8x','GC 30x, MC 0','GC 1x, MC 1x'],'Triamcinolone effect: glucocorticoid 5x, mineralocorticoid 0.'),
('The half life of betamethasone and dexamethasone is:','36-72 hrs',['12-36 hrs','8-12 hrs','1-2 hrs'],'Betamethasone + dexamethasone: t 1/2 = 36-72 hrs.'),
('The potency of betamethasone/dexamethasone is:','Glucocorticoid 30x, mineralocorticoid 0',['GC 5x, MC 0','GC 15x, MC 150x','GC 4x, MC 0.8x'],'Effect: glucocorticoid 30x, mineralocorticoid 0.'),
('The longest acting and most potent glucocorticoid is:','Dexamethasone',['Triamcinolone','Prednisolone','Hydrocortisone'],'Dexamethasone: longest acting, most potent.'),
('Which glucocorticoid has zero mineralocorticoid activity?','Triamcinolone, betamethasone and dexamethasone',['Prednisolone and methylprednisolone','Hydrocortisone','All glucocorticoids'],'Triamcinolone MC 0; betamethasone/dexamethasone MC 0; prednisolone/methylprednisolone MC 0.8x.'),
])
unit('Uses of Glucocorticoids',
 '1. To decrease inflammation - MOA: decreased production of inflammatory mediators (IL-1, IL-6, TNF-alpha), increased anti-inflammatory mediators (IL-10, annexin 1), lymphocyte redistribution & apoptosis; e.g. rheumatoid arthritis, gout, ankylosing spondylitis. 2. To decrease immunity - e.g. graft vs host disease, graft rejection, myasthenia gravis. 3. Neoplasia - e.g. leukemia, lymphoma. 4. CAH fetus: dexamethasone used to prevent virilization. 5. Preterm labour (surfactant maturation) - dose 24 mg in 48 hrs: dexamethasone 4 times (6 mg q6h) or betamethasone 2 times (12 mg q24h).')
facts(222,[
('Glucocorticoids decrease inflammation by:','Decreasing inflammatory mediators (IL-1, IL-6, TNF-alpha) and increasing anti-inflammatory mediators (IL-10, annexin 1)',['Increasing prostaglandins','Blocking histamine receptors only','Inhibiting complement cascade only'],'MOA: decreased IL-1, IL-6, TNF-alpha; increased IL-10, annexin 1.'),
('Glucocorticoids cause lymphocyte:','Redistribution & apoptosis',['Proliferation','Activation','Anergy only'],'MOA: lymphocyte redistribution & apoptosis.'),
('Glucocorticoids are used to decrease immunity in:','Graft vs host disease, graft rejection and myasthenia gravis',['Rheumatoid arthritis only','Gout','Ankylosing spondylitis only'],'Use 2: decrease immunity - GVHD, graft rejection, myasthenia gravis.'),
('Glucocorticoids are used in neoplasia such as:','Leukemia and lymphoma',['Solid breast tumors only','Melanoma','Prostate cancer'],'Use 3: neoplasia - leukemia, lymphoma.'),
('The drug used in CAH fetus to prevent virilization is:','Dexamethasone',['Hydrocortisone','Prednisolone','Betamethasone only'],'Use 4: CAH fetus - dexamethasone used to prevent virilization.'),
('Steroids are used in preterm labour for:','Surfactant maturation',['Tocolysis','Cervical ripening','Fetal growth acceleration'],'Use 5: preterm labour - surfactant maturation.'),
('The total steroid dose for surfactant maturation is:','24 mg in 48 hrs',['12 mg in 24 hrs','48 mg in 24 hrs','6 mg single dose'],'Dose: 24 mg in 48 hrs.'),
('Dexamethasone for surfactant maturation is given as:','4 times (6 mg q6h)',['2 times (12 mg q12h)','4 times (12 mg q6h)','8 times (3 mg q3h)'],'Dexamethasone: 4 times (6 mg q6h).'),
('Betamethasone for surfactant maturation is given as:','2 times (12 mg q24h)',['4 times (6 mg q6h)','2 times (6 mg q12h)','Single 24 mg dose'],'Betamethasone: 2 times (12 mg q24h).'),
])
unit('Side Effects of Glucocorticoids: Cushing\'s Syndrome',
 'The Cushing\'s syndrome diagram: brain (long term use) - psychosis, depression, insomnia; eye - topical causes glaucoma, systemic causes cataract (posterior sub-capsular); thinning of hair; GIT - gastric ulcers; muscle - myopathy; abdominal striae; bone - osteoporosis (due to increased Ca2+ excretion) with secondary use of steroids in hypercalcemia; skin - thin skin and multiple bruises.')
facts(222,[
('The brain side effects of long term steroids are:','Psychosis, depression and insomnia',['Migraine','Seizures','Optic neuritis'],'Brain (long term use): psychosis, depression, insomnia.'),
('Topical steroids cause which eye side effect?','Glaucoma',['Cataract','Papilledema','Optic atrophy'],'Eye: topical - glaucoma; systemic - cataract.'),
('Systemic steroids cause:','Posterior sub-capsular cataract',['Open angle glaucoma','Keratitis','Retinal detachment'],'Eye: systemic - cataract (posterior sub-capsular).'),
('The GIT side effect of steroids is:','Gastric ulcers',['Diarrhea','Pancreatitis always','Esophageal varices'],'GIT: gastric ulcers.'),
('The muscle side effect of steroids is:','Myopathy',['Myotonia','Rhabdomyolysis acutely','Muscle hypertrophy'],'Muscle: myopathy.'),
('The bone side effect of steroids is:','Osteoporosis (due to increased Ca2+ excretion)',['Osteopetrosis','Osteomalacia from vit D excess','Paget disease'],'Bone: osteoporosis (D/t increased Ca2+ excretion).'),
('The secondary use of steroids based on calcium effect is:','Hypercalcemia',['Hypocalcemia','Osteoporosis treatment in elderly','Rickets'],'Bone note: secondary use of steroids - hypercalcemia.'),
('The skin side effects of steroids are:','Thin skin and multiple bruises',['Thick hyperkeratotic skin','Hyperpigmentation','Hirsutism only'],'Skin: thin skin; multiple bruises.'),
('Steroid abdominal change seen is:','Abdominal striae',['Nothing typical','Rectus diastasis','Caput medusae'],'Diagram: abdominal striae.'),
('Steroid hair change is:','Thinning of hair',['Hypertrichosis','Alopecia totalis','Hirsutism'],'Diagram: thinning of hair.'),
])
unit('Metabolic Side Effects, Contraindications and Mineralocorticoids',
 'Metabolic side effects: decreased GLUT 4 production -> hyperglycemia -> diabetes mellitus, and lipodystrophy (lemon on stick appearance): increased insulin blocks lipolysis -> central obesity; decreased GLUT 4 in limbs (glucose unavailable) -> lipolysis -> thin extremities; buffalo hump. C/I: infections; exceptions - H. influenzae meningitis and covid pneumonia (only drug that decreases mortality). Mineralocorticoids: fludrocortisone (exogenous, hydrocortisone + fluorine; glucocorticoid 15x, mineralocorticoid 150x) used in adrenal insufficiency (Addison\'s disease - hydrocortisone + fludrocortisone) and postural hypotension (DOC midodrine); aldosterone (endogenous; glucocorticoid 0, mineralocorticoid 500x) - the pure & most potent mineralocorticoid.')
facts(223,[
('Metabolic side effects of steroids begin with:','Decreased GLUT 4 production',['Increased GLUT 4 production','Insulin hypersensitivity','Beta cell destruction'],'Flow: decreased GLUT 4 production -> hyperglycemia + lipodystrophy.'),
('Steroid-induced hyperglycemia progresses to:','Diabetes mellitus',['Diabetes insipidus','Insulinoma','Metabolic syndrome reversal'],'Flow: decreased GLUT 4 -> hyperglycemia -> diabetes mellitus.'),
('The appearance of steroid lipodystrophy is described as:','Lemon on stick appearance',['Apple on stick appearance','Moon on stick','Cushing helmet only'],'Lipodystrophy: (lemon on stick appearance).'),
('Central obesity in steroid excess occurs because:','Increased insulin blocks lipolysis centrally',['Fat redistribution from limbs','Increased appetite only','Decreased basal metabolic rate only'],'Lipodystrophy 1: increased insulin - blocks -> lipolysis -> central obesity.'),
('Thin extremities in steroid excess occur because:','Decreased GLUT 4 in limbs (glucose unavailable) -> lipolysis',['Increased muscle catabolism only','Peripheral vascular disease','Lipase hyperactivity in limbs'],'Lipodystrophy 2: decreased GLUT 4 in limbs (glucose unavailable) -> lipolysis -> thin extremities.'),
('The third feature of steroid lipodystrophy is:','Buffalo hump',['Moon face only','Truncal obesity','Nuchal rigidity'],'Lipodystrophy 3: buffalo hump.'),
('Steroids are contraindicated in:','Infections',['All pregnancies','Hypertension','Diabetes'],'C/I: infections.'),
('The exceptions where steroids are used despite infection are:','H. influenzae meningitis and covid pneumonia (only drug that decreases mortality)',['All bacterial meningitis','Fungal sepsis','Malaria'],'Exception: H. influenzae meningitis; covid pneumonia - only drug that decreases mortality.'),
('The exogenous mineralocorticoid is:','Fludrocortisone',['Aldosterone','Cortisol','Prednisolone'],'Mineralocorticoids 1: fludrocortisone (exogenous).'),
('Fludrocortisone is chemically:','Hydrocortisone + fluorine',['Cortisone + methyl group','Prednisolone + double bond','Dexamethasone + chloride'],'Fludrocortisone (exogenous): hydrocortisone + fluorine.'),
('The potencies of fludrocortisone are:','Glucocorticoid 15x, mineralocorticoid 150x',['GC 150x, MC 15x','GC 1x, MC 500x','GC 30x, MC 0'],'Effect: glucocorticoid 15x, mineralocorticoid 150x.'),
('Adrenal insufficiency (Addison\'s disease) is treated with:','Hydrocortisone + fludrocortisone',['Dexamethasone alone','Aldosterone orally','Methylprednisolone + midodrine'],'Use: adrenal insufficiency (Addison\'s disease) - hydrocortisone + fludrocortisone.'),
('The DOC for postural hypotension is:','Midodrine',['Fludrocortisone','Phenylephrine','Droxidopa'],'Use: postural hypotension (DOC midodrine).'),
('The endogenous mineralocorticoid is:','Aldosterone',['Fludrocortisone','Cortisol','Deoxycorticosterone'],'Mineralocorticoids 2: aldosterone (endogenous).'),
('The potencies of aldosterone are:','Glucocorticoid 0, mineralocorticoid 500x',['GC 15x, MC 150x','GC 1x, MC 1x','GC 0, MC 50x'],'Aldosterone effect: glucocorticoid 0; mineralocorticoid 500x.'),
('The pure and most potent mineralocorticoid is:','Aldosterone',['Fludrocortisone','Desoxycorticosterone','9-alpha-fluorohydrocortisone'],'Aldosterone: MC 500x (pure & most potent mineralocorticoid).'),
])
finish()
