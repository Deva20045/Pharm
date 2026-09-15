# -*- coding: utf-8 -*-
"""Generate chapters 56-65 from Marrow Pharmacology E8, book pp224-258.

ch56 Drugs Acting on Bone (p224-226)
ch57 Drugs Acting on Thyroid (p227-229)
ch58 Anti-histaminics (p230-232)
ch59 Serotonin-related Drugs (p233-236)
ch60 Eicosanoids (p237-241)
ch61 Gout (p242-243)
ch62 Rheumatoid Arthritis (p244-246)
ch63 Anti-aggregants and Hematopoietic Agents (p247-250)
ch64 Anticoagulants and Fibrinolytics (p251-255)
ch65 Bronchial Asthma (p256-258)
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
    assert len(set([answer]+wrong))==4, f'duplicate options: {text} | {answer} | {wrong}'
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

# CHAPTER 56 - DRUGS ACTING ON BONE (p224-226) -------------------------------
start(56)
unit('Calcium Homeostasis: RANK-RANKL Physiology and Steps of Bone Remodeling',
 'PTH and vitamin D3 stimulate osteoblasts to synthesize RANK ligand (Step-I). RANK ligand activates RANK receptor on osteoclast precursors (Step-II), causing structural change with ruffled borders (Step-III) and bone resorption (Step-IV). The resorption triggers osteoblast activation (Step-V) and new bone formation at the injury site (Step-VI). Strontium ranelate is unique with dual action — it increases bone formation and decreases bone resorption.')
facts(224,[
('PTH and vitamin D3 act in bone remodeling by:','Inducing synthesis of RANK ligand (Step-I)',['Directly killing osteoclasts','Inhibiting sclerostin','Activating calcitonin'],'Step-I: Induce Synthesis of RANK ligand - PTH/Vit D3 (+).'),
('Step-II of bone remodeling is:','RANK ligand activates RANK receptor',['Change in structure of osteoclast','Osteoclast damages bone','Activation of osteoblast'],'Step-II: RANK ligand activates RANK receptor.'),
('Step-III of bone remodeling is:','Change in structure of osteoclast with ruffled borders',['Osteoclast damages bone','Activation of osteoblast','Bone formation at site of injury'],'Step-III: Change in structure of Osteoclast, Ruffled borders.'),
('Step-IV of bone remodeling is:','Osteoclast damages bone (Bone resorption)',['Activation of osteoblast','Bone formation at site of injury','Synthesis of RANK ligand'],'Step-IV: Osteoclast damages bone (Bone resorption).'),
('Step-V of bone remodeling is:','Activation of osteoblast',['Bone resorption','Change in osteoclast structure','RANK ligand synthesis'],'Step-V: Activation of Osteoblast.'),
('Step-VI of bone remodeling is:','Bone formation at site of injury',['Bone resorption','RANK ligand synthesis','Ruffled border formation'],'Step-VI: Bone formation at site of injury.'),
('RANK ligand is produced by:','Osteoblast',['Osteoclast','Osteocyte only','Chondrocyte'],'Diagram: Osteoblast -> RANK ligand.'),
('RANK receptor is present on:','Osteoclast',['Osteoblast','Osteocyte','Fibroblast'],'Rank receptor on osteoclast.'),
('PTH analog teriparatide acts in bone remodeling by:','(+) Stimulating osteoblast leading to Step-V activation',['Killing osteoclast directly','Inhibiting RANK ligand','Blocking sclerostin only'],'PTH analog (Teriparatide) (+) Osteoblast -> Step V.'),
('Raloxifene acts on bone by:','(+) Estrogen -> inhibits bone resorption',['Inhibiting sclerostin','Directly killing osteoclast','Stimulating osteoblast only'],'Raloxifene -> (+) Estrogen -> X Bone resorption.'),
('Calcium analogs act by:','Fastest hypocalcemia via (+) Calcitonin -> inhibits bone resorption',['Inhibiting RANK ligand','Stimulating sclerostin','Blocking PTH'],'Calcium Analogs (Fastest Hypocalcemia) -> (+) Calcitonin.'),
('Sclerostin inhibits:','Bone formation',['Bone resorption','RANK ligand','Calcitonin'],'Diagram: Sclerostin X Bone formation.'),
('Romosozumab acts by:','Inhibiting sclerostin (X Sclerostin)',['Inhibiting RANK ligand','Stimulating estrogen','Blocking calcitonin'],'Romosozumab X Sclerostin.'),
('Strontium ranelate action is:','(+) Bone formation + (-) Bone reabsorption',['Only inhibits resorption','Only stimulates formation','Inhibits both formation and resorption'],'Note: Strontium Ranolate Action (+) Bone formation + (-) Bone Reabsorption.'),
('Denosumab acts in the remodeling diagram by:','Blocking osteoblast to osteoclast signal (X)',['Killing mature osteoclasts','Inhibiting sclerostin','Stimulating estrogen'],'Denosumab X between Osteoblast and Osteoclast.'),
('Bisphosphonates in the remodeling diagram are:','DOC for max hypocalcemia, Kill osteoclast',['Fastest hypocalcemia','Only inhibit sclerostin','Only act on osteoblast'],'Bisphosphonates (DOC) (max Hypocalcemia) Kill osteoclast.'),
])
unit('Bisphosphonates: MOA and Pharmacology',
 'Bisphosphonates inhibit farnesyl pyrophosphate synthase in osteoclasts, leading to apoptosis of osteoclasts. They are the DOC when maximum hypocalcemia is needed. Their oral absorption is poor, so they must be taken on an empty stomach for adequate bioavailability.')
facts(224,[
('The MOA of bisphosphonates is:','Inhibits Farnesyl Pyrophosphate Synthase in Osteoclasts -> Apoptosis of Osteoclasts',['Inhibits RANK ligand','Inhibits sclerostin','Stimulates osteoblast GLP-2 receptors'],'MOA: Inhibits Farnesyl Pyrophosphate Synthase in Osteoclasts -> Apoptosis of Osteoclasts.'),
('Bisphosphonates are DOC for:','Maximum hypocalcemia',['Fastest hypocalcemia','Hypercalcemia with fastest action','Only Paget disease'],'Bisphosphonates (DOC) (max Hypocalcemia).'),
('The fastest hypocalcemia is produced by:','Calcium analogs (calcitonin)',['Bisphosphonates','Denosumab','Raloxifene'],'Calcium Analogs (Fastest Hypocalcemia).'),
('The pharmacokinetics of bisphosphonates is:','Poor oral absorption',['High oral absorption','Complete IV absorption only','Lipid soluble high absorption'],'Pharmacokinetics: Poor oral absorption.'),
('Due to poor oral absorption, bisphosphonates should be:','Taken on empty stomach',['Taken with milk','Taken with calcium','Taken with food'],'Poor oral absorption -> Taken on empty stomach.'),
])
unit('Bisphosphonates: Route, Dosing and Clinical Uses',
 'Intravenous bisphosphonates — pamidronate every 3 months and zoledronate preferred, once yearly, longest acting and more potent — are used for 3 years. Oral bisphosphonates — risedronate once daily and alendronate preferred once daily — are used for 5 years. For osteoporosis the DOC is alendronate, and if intolerant switch to zoledronate; for hypercalcemia of malignancy and Paget disease start with zoledronate directly.')
facts(225,[
('IV bisphosphonates are:','Pamidronate and zoledronate',['Risedronate and alendronate','Ibandronate only','Etidronate only'],'Drugs and Route: IV: Pamidronate, Zoledronate.'),
('Pamidronate dosing is:','3 monthly',['Once yearly','Once daily','Once weekly'],'Pamidronate: 3 monthly.'),
('Zoledronate dosing and properties are:','Preferred, once yearly, longest acting, more potent',['Least potent, daily','Only for Paget','Only oral'],'Zoledronate: Preferred, Once yearly, Longest acting, more potent.'),
('IV bisphosphonates are given for:','3 years',['5 years','1 year','10 years'],'IV: for 3 years.'),
('Oral bisphosphonates are:','Risedronate and alendronate',['Pamidronate and zoledronate','Etidronate only','Clodronate only'],'Oral: Risedronate, Alendronate.'),
('Risedronate dosing is:','OD (once daily)',['3 monthly','Once yearly','BD'],'Risedronate: OD.'),
('Alendronate is:','Preferred oral bisphosphonate, OD',['IV only','Weekly only','Not preferred'],'Alendronate Preferred OD.'),
('Oral bisphosphonates are given for:','5 years',['3 years','1 year','2 years'],'Oral for 5 years.'),
('The DOC for osteoporosis is:','Alendronate',['Zoledronate','Pamidronate','Risedronate'],'Use: DOC: Osteoporosis: Alendronate.'),
('If intolerance to alendronate in osteoporosis:','Zoledronate',['Pamidronate','Risedronate','Stop therapy'],'Alendronate Intolerance -> Zoledronate.'),
('For hypercalcemia of malignancy:','Start zoledronate',['Start alendronate','Start pamidronate only','Start risedronate'],'Hypercalcemia of malignancy -> Start zoledronate.'),
('For Paget disease of bone:','Start zoledronate',['Start alendronate first','Start risedronate only','Start calcitonin first'],'Paget disease -> Start zoledronate.'),
])
unit('Bisphosphonates: Side Effects and Prevention',
 'Oral bisphosphonates cause esophagitis, prevented by taking the drug with a full glass of water and not lying down for 30 minutes. IV bisphosphonates more commonly cause bone fractures including the characteristic femoral chalk-stick fracture whose DOC is teriparatide, maximum hypercalcemia as a paradox, and osteonecrosis of the jaw shown in the clinical photograph.')
facts(225,[
('The side effect of oral bisphosphonates is:','Esophagitis',['Gastritis with bleeding','Osteosarcoma','Hypercalcemia'],'Side effect: Oral route: Esophagitis.'),
('Prevention of bisphosphonate esophagitis includes:','Take drug with full glass of water',['Take with milk','Take at bedtime','Take with antacids'],'Prevention: i. Take drug with full glass of water.'),
('Second prevention of esophagitis is:','Do not lie down for 30 min',['Lie down immediately','Take with calcium','Take on empty bladder'],'ii. Do not lie down for 30 min.'),
('IV > Oral route side effects include:','Bone fracture, hypercalcemia (maximum), osteonecrosis of jaw',['Only esophagitis','Only renal stones','Only alopecia'],'IV > Oral Route: Bone fracture, Hypercalcemia (maximum), Osteonecrosis of jaw.'),
('The characteristic fracture with bisphosphonates is:','Femoral chalk-stick fracture',['Colles fracture','Vertebral compression only','Scaphoid fracture'],'Bone fracture: Femoral chalk-stick fracture (Characteristic fracture).'),
('The DOC for bisphosphonate-induced femoral chalk-stick fracture is:','Teriparatide',['Zoledronate','Alendronate','Denosumab'],'DOC: Teriparatide.'),
('Osteonecrosis of jaw is a side effect of:','Bisphosphonates (IV > Oral)',['Only calcitonin','Only teriparatide','Only raloxifene'],'Osteonecrosis of jaw side effect.'),
('The IV bisphosphonate side effect of hypercalcemia is:','Maximum hypercalcemia',['No hypercalcemia','Only hypocalcemia','Mild hypercalcemia only'],'Hypercalcemia (maximum).'),
])
unit('Denosumab, Raloxifene and Calcitonin Analog',
 'Denosumab is a monoclonal antibody that inhibits RANK ligand and is used in postmenopausal osteoporosis. Calcitonin analog is used intranasally for osteoporosis and subcutaneously for Paget disease, but increases the risk of cancer. Raloxifene is a SERM that mimics estrogen action on bone to inhibit resorption.')
facts(225,[
('The MOA of denosumab is:','Inhibits RANK ligand',['Inhibits sclerostin','Inhibits farnesyl pyrophosphate synthase','Stimulates PTH receptor'],'Denosumab MOA: Inhibits RANK ligand.'),
('Denosumab is used in:','Post menopausal Osteoporosis',['Hypercalcemia of malignancy only','Paget disease DOC','Only in men'],'Use: Post menopausal Osteoporosis.'),
('Raloxifene is a:','SERM that increases estrogen effect on bone',['Bisphosphonate','Calcitonin analog','PTH analog'],'Raloxifene is SERM, Estrogen agonist on bone.'),
('Calcitonin analog uses are:','Osteoporosis -> Intranasal Route, Paget disease -> S/C Route',['Only IV for osteoporosis','Only oral for Paget','Only for hypercalcemia'],'Use: Osteoporosis -> Intranasal Route, Paget disease -> S/C Route.'),
('The side effect of calcitonin analog is:','Increased risk of cancer',['Osteonecrosis of jaw','Chalk-stick fracture','Esophagitis'],'S/E: ↑ Risk of cancer.'),
('Intranasal route is used for calcitonin in:','Osteoporosis',['Paget disease','Hypercalcemia of malignancy','Only in children'],'Osteoporosis -> Intranasal Route.'),
('S/C route for calcitonin is used in:','Paget disease',['Osteoporosis','Hypercalcemia only','Only for nasal polyps'],'Paget disease -> S/C Route.'),
])
unit('Anabolic Drugs and Postmenopausal Osteoporosis Algorithm',
 'Anabolic drugs build bone: teriparatide is a PTH analog with side effect osteosarcoma, contraindicated in Paget disease and limited to maximum 2 years; abaloparatide is a PTH-related peptide analog; romosozumab inhibits sclerostin. The treatment algorithm for postmenopausal osteoporosis starts with alendronate DOC, if intolerant switch to zoledronate, if still intolerant check fracture risk — high risk gets denosumab and very high risk gets anabolic drugs teriparatide or romosozumab.')
facts(226,[
('The PTH analog used as anabolic drug is:','Teriparatide',['Abaloparatide','Romosozumab','Denosumab'],'PTH Analog: Teriparatide.'),
('The side effect of teriparatide is:','Osteosarcoma',['Osteonecrosis of jaw','Esophagitis','Chalk-stick fracture'],'S/E: Osteosarcoma.'),
('Teriparatide is contraindicated in:','Paget disease',['Osteoporosis','Hypercalcemia of malignancy','Postmenopausal osteoporosis'],'C/I: Paget disease.'),
('Maximum duration of teriparatide use is:','2 years',['3 years','5 years','Lifelong'],'Use: maximum use for 2 years.'),
('PTHrP analog is:','Abaloparatide',['Teriparatide','Romosozumab','Calcitonin'],'PTHrP Analog: Abaloparatide.'),
('Romosozumab MOA is:','Inhibits Sclerostin',['Inhibits RANK ligand','Inhibits farnesyl pyrophosphate synthase','Stimulates RANK ligand'],'Romosozumab MOA: Inhibits Sclerostin.'),
('Postmenopausal osteoporosis first line DOC is:','Alendronate (DOC)',['Zoledronate','Denosumab','Teriparatide'],'Note: Post menopausal Osteoporosis: Start: Alendronate (DOC).'),
('After alendronate intolerance, next drug is:','Zoledronate',['Denosumab','Teriparatide','Raloxifene'],'Intolerance -> Zolendronate.'),
('After zoledronate intolerance, next step is:','Check for Risk of fracture',['Stop treatment','Start calcium only','Start estrogen only'],'Zolendronate Intolerance -> Check for Risk of fracture.'),
('High fracture risk after bisphosphonate intolerance gets:','Denosumab',['Teriparatide','Romosozumab','Alendronate again'],'High: Denosumab.'),
('Very high fracture risk gets:','Anabolic drugs: Teriparatide, Romosozumab',['Only calcium','Only bisphosphonates','Only denosumab'],'Very high: Anabolic Drugs: Teriparatide, Romosozumab.'),
])
finish()

# CHAPTER 57 - DRUGS ACTING ON THYROID (p227-229) ----------------------------
start(57)
unit('Thyroid Physiology and Sites of Drug Action',
 'TSH acting on TSH-receptor increases production via Na+/I- symporter, thyroid peroxidase (TPO) and thiol endopeptidase. Iodide enters via Na+-I- symporter, undergoes organification (1) and coupling (2) by TPO to form MIT/DIT and then T3/T4 stored in colloid as thyroglobulin (TG). Thiol endopeptidase breaks TG to release T3/T4; T4 is peripherally converted by 5-deiodinase to active T3.')
facts(227,[
('TSH acts on:','TSH-Receptor to increase production',['Na+-I- symporter only','Thyroglobulin receptor only','TPO directly'],'(T) TSH-Receptor Production ↑.'),
('Na+-I- symporter transports:','I-',['Na+ only','T3/T4','Thyroglobulin'],'Na+-I- Symporter I-.'),
('Thyroid peroxidase (TPO) mediates:','Organification (1) and Coupling (2)',['Only organification','Only coupling','Thiol endopeptidase action'],'TPO (1) Organification (2) Coupling.'),
('Organification is:','(1) step inhibited by thioamides',['Release step','Deiodination','TG breakdown'],'(1): Organification.'),
('Coupling is:','(2) step inhibited by thioamides',['Organification','Release','Deiodination'],'(2): Coupling.'),
('MIT and DIT form:','T3 and T4',['Only T3','Only T4','Reverse T3 only'],'MIT TPO DIT -> T3 T4.'),
('T3 and T4 are stored as:','Thyroglobulin (TG) in colloid (Storage)',['Free hormones in blood','Only in follicular cells','In parafollicular cells'],'Thyroglobulin (TG) Colloid (Storage) T3 T4.'),
('Thiol endopeptidase:','Breaks TG to release T3/T4',['Synthesizes TG','Organifies iodide','Converts T4 to T3'],'Thiol endopeptidase: Breaks TG.'),
('Release of T3/T4 is:','Inhibited by iodide excess',['Stimulated by iodide','Not regulated','Only via TPO'],'Release (-) with iodide.'),
('Peripheral conversion T4 to T3 is by:','5-deiodinase',['TPO','Thiol endopeptidase','Na+-I- symporter'],'T4 5-deiodinase (-) -> T3.'),
('T3 is:','Active hormone',['Inactive','Storage form','Prodrug only'],'T3 (active).'),
('Thyroglobulin receptor is indicated by:','Uptake arrow for TG',['TSH receptor','Na+ symporter','TPO enzyme'],'Diagram: Thyroglobulin Receptor.'),
('Drugs inhibiting Na+-I- symporter would:','Decrease iodide uptake',['Increase T3 release','Increase coupling','Block deiodinase only'],'Na+-I- Symporter (-) reduces I-.'),
])
unit('Thioamide Drugs: Propylthiouracil and Methimazole',
 'Thioamide drugs for hyperthyroidism are propylthiouracil (PTU) and carbimazole which is a prodrug converted to methimazole and is longer acting. PTU has short half life requiring multiple dosing and is hepatotoxic; methimazole has long half life with once daily dosing but is teratogenic causing cutis aplasia with scalp defect and choanal/esophageal atresia plus cholestatic jaundice. Common side effects for both are maculopapular rash most common, agranulocytosis and arthralgia.')
facts(227,[
('Thioamide drugs are:','Propylthiouracil (PTU) and carbimazole (prodrug) -> methimazole',['Potassium iodide and Lugol iodine','Radioactive iodine','Levothyroxine and liothyronine'],'Thioamide drugs: Propylthiouracil (PTU), Carbimazole (Prodrug).'),
('Carbimazole is:','Prodrug converted to methimazole, longer acting',['Active drug itself','Short acting only','Not a thioamide'],'Carbimazole (Prodrug): Longer acting -> methimazole.'),
('PTU T1/2 is:','Short: multiple dosing',['Long: once daily dosing','Very long weekly','Intermediate BD'],'PTU T1/2 Short: multiple dosing.'),
('Methimazole T1/2 is:','Long: once daily dosing',['Short: multiple dosing','Ultra-short','Only IV'],'Methimazole long: Once daily dosing.'),
('PTU side effect is:','Hepatotoxic',['Teratogenic cutis aplasia','Cholestatic jaundice','Scalp defect'],'S/E Hepatotoxic for PTU.'),
('Methimazole teratogenic effects are:','Cutis Aplasia: scalp defect, choanal/esophageal atresia',['Hepatotoxicity only','Rash only','Agranulocytosis only'],'1. Teratogenic -> Cutis Aplasia: Scalp defect choanal/esophageal Atresia.'),
('Methimazole also causes:','Cholestatic jaundice',['Hepatocellular necrosis only','No liver effect','Pancreatitis'],'2. Cholestatic Jaundice.'),
('Common side effects of thioamides are:','Maculopapular rash (m/c), agranulocytosis, arthralgia',['Only hepatotoxicity','Only rash','Only agranulocytosis'],'Common S/E: maculopapular Rash (m/c), Agranulocytosis, Arthralgia.'),
('Most common side effect of thioamides is:','Maculopapular rash',['Agranulocytosis','Arthralgia','Hepatotoxicity'],'Maculopapular Rash (m/c).'),
])
unit('Thioamide Uses and Thyroid Storm Management',
 'PTU is preferred in first trimester of pregnancy because it is less teratogenic and is also used in thyroid storm; methimazole is commonly prescribed and is preferred in second and third trimester because it is less hepatotoxic. In thyroid storm the first drug is beta blockers to prevent atrial fibrillation, if contraindicated due to asthma/COPD use verapamil/diltiazem, plus other drugs steroid and potassium iodide.')
facts(228,[
('PTU is preferred in:','1st trimester pregnancy (less teratogenic) and thyroid storm',['2nd and 3rd trimester','Only in elderly','Only prior to surgery'],'Use: In pregnancy: 1st trimester (Less Teratogenic) Thyroid storm.'),
('Methimazole is:','Commonly prescribed',['Rarely used','Only for thyroid storm','Only IV'],'Commonly Prescribed.'),
('Methimazole in pregnancy is used in:','2nd and 3rd trimester (less hepatotoxic)',['1st trimester','Only 1st trimester','Never in pregnancy'],'In pregnancy: 2nd and 3rd trimester (less Hepatotoxic).'),
('Thyroid storm first drug is:','Beta blockers to prevent atrial fibrillation',['PTU','Methimazole','Potassium iodide'],'Note: management of thyroid storm 1st drug -> Beta Blockers: To prevent Atrial fibrillation.'),
('If beta blockers contraindicated in thyroid storm due to asthma/COPD:','Verapamil/Diltiazem',['Continue beta blockers','Stop all treatment','Use only KI'],'If C/I: Asthma/COPD Verapamil/Diltiazem.'),
('Other drugs in thyroid storm are:','Steroid, KI',['Only beta blockers','Only PTU','Only methimazole'],'Other drugs: Steroid, KI.'),
])
unit('Thiol Endopeptidase Inhibitors: Iodides',
 'Potassium iodide 10% and Lugol iodine 5% inhibit release of T3/T4 and are the fastest-acting antithyroid drugs, but they develop tolerance and cannot be used as long-term therapy. Extra benefits are decreased size of thyroid making it firm and decreased blood vessels in gland reducing bleeding, so they are used prior to surgery.')
facts(228,[
('Thioendopeptidase inhibitors are:','Potassium iodide (10%) and Lugol iodine (5%)',['PTU and methimazole','Steroids and beta blockers','Radioactive iodine'],'Drugs: Potassium iodide (10%) Lugol iodine (5%).'),
('MOA of iodides is:','Inhibits Release of T3/T4',['Inhibits organification only','Stimulates release','Blocks 5-deiodinase'],'MOA: Inhibits Release of T3/T4.'),
('Iodides are:','Fastest-acting antithyroid drugs',['Slowest acting','No effect on release','Only for hypothyroidism'],'Fastest-acting Antithyroid drugs.'),
('Iodides develop:','Tolerance: cannot be used as long-term therapy',['No tolerance','Dependence','Only short tolerance of 1 day'],'Develop tolerance: Cannot be used as long-term therapy.'),
('Extra benefits of iodides are:','Decreased size of thyroid (makes it firm) and decreased blood vessels in gland (decreased bleeding)',['Increased size only','Increased vascularity','No surgical benefit'],'Extra benefits: ↓ Size of thyroid: makes it firm ↓ Blood vessels in gland: ↓ Bleeding.'),
('Iodides are used:','Prior to surgery',['As long-term monotherapy','In pregnancy alone','Only in thyroid storm'],'Used Prior to Surgery.'),
('Lugol iodine concentration is:','5%',['10%','1%','0.5%'],'Lugol iodine (5%).'),
('Potassium iodide concentration is:','10%',['5%','1%','20%'],'Potassium iodide (10%).'),
])
unit('Peripheral Conversion Inhibitors and Radioactive Iodine',
 '5-deiodinase inhibitors blocking peripheral conversion of T4 to T3 are PTU, steroids, beta blockers and amiodarone. Radioactive iodine I131 is used for thyroid ablation and I123 for thyroid scan. Uses of I131 are hyperthyroidism in elderly, patient with arrhythmia, thyroid carcinoma except medullary carcinoma, and recurrent Graves disease. Side effects include radiation thyroiditis with increased T3/T4 treated by premedicating with methimazole stopping 3 days before I131, giving I131 on the day, restarting after 3 days, plus lifelong hypothyroidism and secondary cancers; it is contraindicated in pregnancy.')
facts(229,[
('5-deiodinase inhibitors / peripheral conversion (T4-T3) inhibitors are:','PTU, steroids, beta-blocker, amiodarone',['Only PTU','Only amiodarone','Potassium iodide and Lugol iodine'],'5-Deiodinase inhibitors: PTU Steroids Beta-blocker Amiodarone.'),
('I131 is used for:','Thyroid ablation',['Thyroid scan','Only hypothyroidism treatment','Only for medullary ca'],'I131: Thyroid Ablation.'),
('I123 is used for:','Thyroid scan',['Thyroid ablation','Only for Graves','Only for hypothyroidism'],'I123: Thyroid Scan.'),
('Radioactive iodine for hyperthyroidism is preferred in:','Elderly and patient with arrhythmia',['Children and pregnant women','Only in young adults','Only first trimester'],'Hyperthyroidism -> In Elderly, Patient with Arrhythmia.'),
('Radioactive iodine is used in thyroid carcinoma except:','Medullary carcinoma',['Papillary carcinoma','Follicular carcinoma','Anaplastic carcinoma'],'Thyroid Carcinoma (Except: medullary ca).'),
('Recurrent Graves disease is treated with:','Radioactive iodine',['Only surgery','Only thioamides lifelong','Only beta blockers'],'Recurrent Graves disease.'),
('Side effect of I131 is:','Radiation thyroiditis -> increased T3/T4',['Decreased T3/T4 immediately','No thyroiditis','Only hypothyroidism without rise'],'S/E: Radiation Thyroiditis -> ↑ T3/T4.'),
('Management to prevent radiation thyroiditis includes:','Premedicate patient with methimazole',['Premedicate with PTU only','No premedication needed','Give KI only'],'Rx: Premedicate patient with methimazole.'),
('Methimazole timing around I131 therapy is:','Start methimazole, stop before 3 days I131 therapy, Day I131 given, restart after 3 days',['Continue methimazole during I131','Stop 10 days before','Never restart after'],'Start methimazole Stop before 3 days I131 therapy Day I131 given Restart After 3 days.'),
('Long term side effects of I131 are:','Life long hypothyroidism and secondary cancers',['Only transient hyperthyroidism','Only alopecia','Only GI upset'],'Life long Hypothyroidism, Secondary cancers.'),
('Radioactive iodine is contraindicated in:','Pregnancy',['Elderly','Patient with arrhythmia','Recurrent Graves'],'C/I: Pregnancy.'),
])
unit('Treatment of Hypothyroidism',
 'Levothyroxine (Le) T4 salt is longer acting and is DOC for replacement in hypothyroidism given orally on empty stomach 30 min before breakfast; it is also used for thyroid cancer to suppress TSH orally and for myxedema coma IV. Liothyronine (Li) T3 salt is shorter acting, used prior to I131 therapy and for myxedema coma IV as Le + Li + steroid. Side effects of levothyroxine are thyrotoxicosis, osteoporosis and atrial fibrillation requiring dose reduction in patients with arrhythmia.')
facts(229,[
('Levothyroxine (Le) is:','T4 salt, longer acting',['T3 salt, shorter acting','T3 salt longer acting','T4 salt shorter acting'],'Levothyroxine (Le) [T4 salt] Longer Acting.'),
('Liothyronine (Li) is:','T3 salt, shorter acting',['T4 salt longer acting','T4 salt shorter','Only IV'],'Liothyronine (Li) [T3 salt] Shorter Acting.'),
('Levothyroxine is DOC for:','Replacement in hypothyroidism (DOC)',['Thyroid storm','Hyperthyroidism','Thyroid scan'],'Replacement in Hypothyroidism (DOC).'),
('Levothyroxine oral administration is:','Empty stomach 30 min before breakfast',['With food','With calcium','At bedtime with milk'],'Empty Stomach 30 min before breakfast.'),
('Levothyroxine for thyroid cancer is used to:','Decrease TSH, oral route',['Increase TSH','Only IV','Only for medullary ca'],'Thyroid cancer (↓ TSH): Oral Route.'),
('Levothyroxine for myxedema coma is given:','IV route',['Oral only','IM only','Not used'],'Myxedema coma: IV Route.'),
('Liothyronine prior to I131 therapy is:','Used prior to I131 therapy',['Not used','Only for hypothyroidism replacement','Only for hyperthyroidism'],'Prior to I131 Therapy.'),
('Myxedema coma IV treatment is:','Le + Li + steroid',['Only Le','Only Li','Only steroid'],'Myxedema coma: IV Route Rx: Le + Li + steroid.'),
('Side effects of levothyroxine are:','Thyrotoxicosis, osteoporosis, atrial fibrillation',['Only weight gain','Only bradycardia','Only rash'],'S/E: Thyrotoxicosis Osteoporosis Atrial fibrillation.'),
('In patient with arrhythmia on levothyroxine:','Decrease dose',['Increase dose','Stop permanently','Add beta blocker only'],'Atrial fibrillation: ↓ Dose in Patient of arrhythmia.'),
])
finish()

# CHAPTER 58 - ANTI-HISTAMINICS (p230-232) ----------------------------------
start(58)
unit('Histamine Receptors and Effects',
 'Histamine effects are due to its receptors which are GPCRs. H1 is post-synaptic Gq increasing Ca2+ used for allergy/motion sickness; H2 is post-synaptic Gs increasing cAMP used for peptic ulcer; H3 is presynaptic Gi decreasing histamine in synapse used for wakefulness via pitolisant in narcolepsy; H4 is on leucocytes Gi mediating chemotaxis with no drugs currently. Increased Ca2+ causes bronchoconstriction, vasodilatation, increased GI contractions, wakefulness, decreased appetite and itching via PNS; increased cAMP increases heart contraction and HR and stomach HCl release.')
facts(230,[
('Histamine effects are due to:','Its receptors',['Only H1','Only H2','Only H3'],'Effects are d/t its receptors.'),
('Histamine receptors are:','GPCR (G protein coupled receptors)',['Ion channel receptors','Nuclear receptors','Tyrosine kinase receptors'],'Receptors: GPCR.'),
('H1 receptor location and subtype are:','Post-synaptic, Gq',['Presynaptic Gi','Leucocyte Gi','Post-synaptic Gs'],'H1 Post-synaptic Gq.'),
('H1 function and use are:','Increased Ca2+, Allergy/motion sickness',['Increased cAMP, Peptic ulcer','Decreased histamine, narcolepsy','Mediates chemotaxis'],'H1 ↑Ca2+ Allergy/motion sickness.'),
('H2 receptor location and subtype are:','Post-synaptic, Gs',['Presynaptic Gi','Leucocyte Gi','Post-synaptic Gq'],'H2 Post-synaptic Gs.'),
('H2 function and use are:','Increased cAMP, Peptic ulcer disease',['Increased Ca2+, allergy','Decreased histamine, narcolepsy','Mediates chemotaxis'],'H2 ↑cAMP Peptic ulcer disease.'),
('H3 receptor location and subtype are:','Presynaptic, Gi',['Post-synaptic Gq','Leucocyte Gi','Post-synaptic Gs'],'H3 Presynaptic Gi.'),
('H3 function is:','Decreases histamine in synapse (-) H1 H2',['Increases Ca2+','Increases cAMP','Mediates chemotaxis'],'↓ Histamine in synapse (-) H1 H2.'),
('H3 use is:','Pitolisant: In narcolepsy -> increased wakefulness',['Allergy/motion sickness','Peptic ulcer','No drugs currently'],'Pitolisant: In narcolepsy ↑wakefulness.'),
('H4 receptor location and function are:','Leucocyte, mediates chemotaxis',['Post-synaptic, increases Ca2+','Presynaptic, decreases histamine','Post-synaptic, increases cAMP'],'H4 Leucocyte mediates chemotaxis.'),
('H4 drugs currently:','No drugs currently',['Pitolisant','Cetirizine','Famotidine'],'No drugs currently.'),
('Effects of increased Ca2+ include:','Bronchoconstriction',['Increased HCl release only','Increased HR only','Decreased GI contractions'],'Effects of ↑Ca2+: Bronchoconstriction.'),
('Vasodilatation is due to:','Increased Ca2+',['Increased cAMP only','Gi activation only','Decreased Ca2+'],'Vasodilatation effect of ↑Ca2+.'),
('Increased GI contractions are due to:','Increased Ca2+',['Increased cAMP','Gi','No receptor'],'↑ GI contractions.'),
('Wakefulness and decreased appetite are due to:','Increased Ca2+',['Increased cAMP','Gi only','No effect'],'Wakefulness, ↓ Appetite.'),
('Itching (PNS mediated) is due to:','Increased Ca2+',['Increased cAMP','Gi','No receptor'],'Itching (PNS mediated).'),
('Effects of increased cAMP in heart are:','Increased contraction and HR',['Decreased contraction','No effect','Only vasodilation'],'Heart: ↑ Contraction & HR.'),
('Effect of increased cAMP in stomach is:','Increased HCl release',['Decreased HCl','No effect','Increased pepsin only'],'Stomach: ↑HCl release.'),
])
unit('H1 Blockers: Classification',
 'First generation H1 blockers are less potent, cross blood-brain barrier causing sedation, block muscarinic receptors so preferred as antimuscarinics, contraindicated in elderly, children, pilots and drivers, and cause nausea and vomiting due to delayed gastric emptying. Second generation are more potent, do not cross BBB so non-sedating, do not block muscarinic receptors and are preferred as antihistaminics.')
facts(230,[
('First generation H1 blockers are:','Less potent',['More potent','Equally potent','Most potent antihistaminic'],'First Generation Less potent.'),
('First generation BBB crossing is:','Cross Blood-Brain Barrier -> Sedating',['Does not cross BBB -> Non-sedating','No sedation','Only peripheral'],'Cross Blood-Brain Barrier -> Sedating.'),
('First generation muscarinic effect is:','Muscarinic receptors blocker',['Do not block muscarinic','Only H2 block','Only H3 block'],'Muscarinic receptors blocker.'),
('First generation are preferred as:','Antimuscarinics',['Antihistaminics','Prokinetics','Antiemetics only'],'Preferred antimuscarinics.'),
('First generation C/I are:','Elderly, children, pilots, drivers',['Only elderly','Only children','Only hypertensives'],'C/I: Elderly, children, pilots, drivers.'),
('First generation S/E is:','Nausea & vomiting d/t delayed gastric emptying',['Only sedation','Only dry mouth','Only urinary retention'],'S/E: Nausea & vomiting d/t delayed gastric emptying.'),
('Second generation potency is:','More potent',['Less potent','Equal','No potency'],'Second Generation more potent.'),
('Second generation BBB is:','Does not cross BBB -> Non-sedating',['Crosses BBB -> Sedating','Crosses partially','No effect'],'Does not cross BBB -> Non-sedating.'),
('Second generation muscarinic blocking:','Do not block muscarinic receptors',['Block muscarinic','Block nicotinic','Block adrenergic'],'Do not block muscarinic receptors.'),
('Second generation preferred as:','Antihistaminics',['Antimuscarinics','Prokinetics','Sedatives'],'Preferred antihistaminics.'),
])
unit('First Generation H1 Blockers: Specific Drugs and Uses',
 'Promethazine, diphenhydramine and dimenhydrinate have maximum antimuscarinic effect and are used for motion sickness taken 1 hr before travel orally, for acute dystonia in EPS, for vertigo in Meniere disease, promethazine and diphenhydramine also as local anaesthetic, dimenhydrinate for insomnia, promethazine for chemotherapy induced nausea vomiting with side effect alpha1 blockade causing hypotension. Doxylamine with vitamin B6 as doxinate is DOC for morning sickness. Chlorpheniramine is least sedating first gen and preferred for daytime use; meclizine/cyclizine for motion sickness; doxepin is a tricyclic antidepressant; cyproheptadine is a 5HT2 blocker; hydroxyzine has antipruritic effect for skin allergies, anxiolytic and antiemetic. DOC for motion sickness is transdermal scopolamine patch.')
facts(231,[
('General use of 1st generation H1 blockers is:','Non-allergic rhinitis',['Allergic rhinitis only','Urticaria only','Peptic ulcer'],'General use: Non-allergic rhinitis.'),
('Drugs with maximum antimuscarinic effect are:','Promethazine, Diphenhydramine, Dimenhydrinate',['Cetirizine and loratadine','Fexofenadine only','Azelastine only'],'Promethazine, Diphenhydramine, Dimenhydrinate: maximum antimuscarinic effect.'),
('Promethazine/diphenhydramine/dimenhydrinate for motion sickness:','Taken 1 hr before travel (Oral)',['Taken after travel','IV only','Topical only'],'Motion sickness: Taken 1 hr before travel (Oral).'),
('Promethazine etc for EPS:','Acute dystonia',['Tardive dyskinesia only','Akathisia only','Only parkinsonism'],'EPS (Extra Pyramidal symptoms): Acute dystonia.'),
('Meniere disease treated with promethazine group for:','Vertigo',['Hearing loss only','Tinnitus only','Allergy only'],'Meniere disease: vertigo.'),
('Promethazine, Diphenhydramine as:','Local anaesthetic',['Only antihistaminic','Only antiemetic','Only sedative'],'Promethazine, Diphenhydramine: Local anaesthetic.'),
('Dimenhydrinate used for:','Insomnia',['Only motion sickness','Only allergy','Only vertigo'],'Dimenhydrinate: Insomnia.'),
('Promethazine for chemotherapy induced:','Nausea & vomiting',['Only allergy','Only insomnia','Only motion sickness'],'Chemotherapy induced nausea & vomiting.'),
('Promethazine S/E alpha1 blockade causes:','Hypotension',['Hypertension','Tachycardia only','No effect'],'S/E: α1 blockade -> Hypotension.'),
('Doxinate is:','Doxylamine + Vitamin B6',['Doxylamine + Vitamin C','Chlorpheniramine + B6','Promethazine + B6'],'Doxinate: Doxylamine + Vitamin B6.'),
('DOC for morning sickness is:','Doxylamine (Doxinate)',['Promethazine','Chlorpheniramine','Cetirizine'],'DOC: morning sickness.'),
('Least sedating 1st gen drug is:','Chlorpheniramine',['Promethazine','Diphenhydramine','Dimenhydrinate'],'Chlorpheniramine: Least sedating 1st gen drug.'),
('Chlorpheniramine preferred for:','Day time use',['Night time use','Only in elderly','Only in children'],'Preferred: Day time use.'),
('Meclizine/cyclizine used for:','Motion sickness',['Urticaria only','Allergic rhinitis only','Peptic ulcer'],'Meclizine/cyclizine: motion sickness.'),
('Doxepin is:','Tricyclic Antidepressants',['Only antihistaminic','Only antimuscarinic','Only topical'],'Doxepin: Tricyclic Antidepressants.'),
('Cyproheptadine is:','5HT2 blocker',['H1 blocker only','H2 blocker','H3 blocker'],'Cyproheptadine: 5HT2 blocker.'),
('Hydroxyzine anti pruritic effect -> Rx of:','Skin allergies',['Peptic ulcer','Motion sickness only','Asthma'],'Anti pruritic effect -> Rx of skin allergies.'),
('Hydroxyzine other effects are:','Anxiolytic and antiemetic',['Only antipruritic','Only sedative','Only local anaesthetic'],'Anxiolytic, Antiemetic.'),
('DOC for motion sickness is:','Transdermal scopolamine patch',['Promethazine','Chlorpheniramine','Cetirizine'],'DOC for motion sickness: Transdermal scopolamine patch.'),
])
unit('Second Generation H1 Blockers and Topical Agents',
 'Second generation uses are urticaria DOC and as supplements for allergic rhinitis where hay fever DOC is steroids. Cetirizine is a hydroxyzine derivative and most sedating second gen; levocetirizine is its more potent isomer requiring lesser dose; astemizole and terfenadine increase QT prolongation causing torsades hence banned; fexofenadine is a terfenadine derivative with no QT prolongation and least sedating; loratadine metabolite desloratadine is most potent antihistaminic; rupatadine blocks platelet activating factor giving anti-inflammatory effect. Topical drugs azelastine, epinastine, alcaftadine, levocarbastine and olopatadine are used for allergic rhinitis and allergic conjunctivitis.')
facts(231,[
('DOC for urticaria is:','Second generation H1 blockers',['First generation','Steroids','No drug'],'DOC: urticaria.'),
('As supplements for allergic rhinitis (Hay fever DOC Steroids):','Second generation H1 blockers',['First generation only','No role','Only topical'],'As supplements: Allergic rhinitis (Hay fever->DOC: Steroids).'),
('Cetirizine is:','Hydroxyzine derivative',['Promethazine derivative','Loratadine derivative','Terfenadine derivative'],'Cetirizine: Hydroxyzine derivative.'),
('Most sedating 2nd gen drug is:','Cetirizine',['Fexofenadine','Loratadine','Desloratadine'],'Most sedating 2nd gen drug.'),
('Levocetirizine is:','More potent isomer of cetirizine, lesser dose requirement',['Less potent isomer','Same potency','Prodrug of cetirizine'],'More potent isomer of cetirizine, Lesser dose requirement.'),
('Astemizole & Terfenadine risk is:','QT prolongation -> Torsades (Hence banned)',['No QT risk','Only sedation','Only antimuscarinic'],'↑ Risk of QT prolongation -> Torsades (Hence banned).'),
('Fexofenadine is:','Terfenadine derivative: No QT prolongation',['Astemizole derivative with QT prolongation','Cetirizine derivative','Loratadine derivative'],'Fexofenadine: Terfenadine derivative: No QT prolongation.'),
('Least sedating antihistaminic is:','Fexofenadine',['Cetirizine','Chlorpheniramine','Promethazine'],'Least sedating antihistaminic.'),
('Loratadine metabolite is:','Desloratidine, most potent antihistaminic',['Fexofenadine, least sedating','Cetirizine, most sedating','Azelastine, topical only'],'Loratidine metabolite -> Desloratidine: most potent antihistaminic.'),
('Most potent antihistaminic is:','Desloratidine',['Cetirizine','Fexofenadine','Chlorpheniramine'],'Most potent antihistaminic.'),
('Rupatadine:','(-)Platelet activating factor -> Anti-inflammatory',['Only H1 blocker','Only antimuscarinic','Only sedative'],'(-)Platelet activating factor -> Anti-inflammatory.'),
('Topical antihistaminic drugs are:','Azelastine, Epinastine, Alcaftadine, Levocarbastine, Olopatadine',['Cetirizine and loratadine','Promethazine only','Chlorpheniramine only'],'Topical Drugs: Azelastine, Epinastine, Alcaftadine, Levocarbastine, Olopatadine.'),
('Topical antihistaminics uses are:','Allergic rhinitis, Allergic conjunctivitis',['Only urticaria','Only motion sickness','Only peptic ulcer'],'Uses: Allergic rhinitis, Allergic conjunctivitis.'),
])
unit('Bradykinin and Hereditary Angioedema',
 'Kininogen via kallikrein forms kallidin and bradykinin which stimulate bradykinin 1 and 2 receptors increasing prostaglandins causing pain and inflammation and nitric oxide causing vasodilation. Kallikrein antagonists are aprotinin, lanadelumab, berotralstat and ecallantide; icatibant blocks bradykinin 2 receptor. Aprotinin also inhibits plasmin giving antifibrinolytic effect used to decrease bleeding post CABG. Hereditary angioedema treatment DOC is C1 esterase inhibitor deficiency replacement, alternatives icatibant and ecallantide; prophylaxis DOC danazol, alternatives lanadelumab and berotralstat, pre-surgery epsilon-aminocaproic acid EACA.')
facts(232,[
('Kininogen via kallikrein forms:','Kallidin and bradykinin',['Only bradykinin 1','Only kallidin','Only histamine'],'Kininogen Kallidrein -> Kallidin Bradykinin.'),
('Bradykinin stimulates:','Bradykinin 1 and Bradykinin 2',['Only B1','Only B2','Only H1'],'Bradykinin 1 Bradykinin 2.'),
('Bradykinin 1/2 activation increases:','Prostaglandins and Nitric Oxide',['Only prostaglandins','Only NO','Only histamine'],'↑Prostaglandins ↑Nitric Oxide.'),
('Prostaglandins cause:','Pain and inflammation',['Vasodilation only','Only itching','Only fever'],'Pain Inflammation.'),
('Nitric oxide causes:','Vasodilation',['Pain','Inflammation','Bronchoconstriction'],'Nitric Oxide Vasodilation.'),
('Kallikrein antagonists are:','Aprotinin, Lanadelumab, Berotralstat, Ecallantide',['Icatibant only','Danazol only','Only aprotinin'],'Antagonists: Aprotinin Lanadelumab Berotralstat Ecallantide.'),
('Icatibant blocks:','Bradykinin 2 receptor',['Kallikrein','Bradykinin 1 only','Histamine H1'],'Icatibant (-) Bradykinin 2.'),
('Aprotinin MOA is:','Plasmin (-) : Antifibrinolytic',['Kallikrein (+)','Bradykinin (+)','Histamine (-)'],'Plasmin (-): Antifibrinolytic.'),
('Aprotinin use is:','Decreased risk of bleeding post CABG (Coronary Artery Bypass Grafting)',['Increased bleeding','Only angioedema','Only prophylaxis'],'Uses: ↓ Risk of bleeding post CABG.'),
('Hereditary angioedema Rx DOC is:','C1 Esterase inhibitor (C1 Esterase -)',['Icatibant','Ecallantide','Danazol'],'DOC: C1 Esterase (-).'),
('Alternatives for hereditary angioedema Rx are:','Icatibant & Ecallantide',['Lanadelumab & Berotralstat','Danazol only','Aprotinin only'],'Alternatives: Icatibant & Ecallantide.'),
('Prophylaxis of hereditary angioedema DOC is:','Danazol',['C1 esterase','Icatibant','EACA only'],'Prophylaxis DOC: Danazol.'),
('Alternatives for prophylaxis are:','Lanadelumab & Berotralstat',['Icatibant & Ecallantide','Aprotinin only','C1 esterase only'],'Alternatives: Lanadelumab & Berotralstat.'),
('Pre surgery prophylaxis for hereditary angioedema is:','Epsilon-AminoCaproic Acid (EACA)',['Danazol','Icatibant','C1 esterase'],'Pre surgery: Epsilon-AminoCaproic Acid (EACA).'),
])
finish()

# CHAPTER 59 - SEROTONIN-RELATED DRUGS (p233-236) ---------------------------
start(59)
unit('Serotonin Receptors and 5-HT1A Agonists',
 'Serotonin has 7 receptor types 5-HT1 to 5-HT7, all are GPCRs except 5-HT3 which is an ion channel receptor. 5-HT1A agonists act presynaptically on serotonergic neurons, subtype Gi, and include buspirone, epsapirone and gepirone; they inhibit 5-HT1A autoreceptor leading to decreased 5-HT2 activity in brain reducing anxiety, used as non-benzodiazepine anxiolytics.')
facts(233,[
('Serotonin receptor types are:','7 types: 5-HT1 to 5-HT7',['3 types only','5 types only','10 types'],'7 types: 5-HT1 to 5-HT7.'),
('All serotonin receptors are:','GPCRs (G protein coupled receptors) except 5-HT3',['All ion channels','All nuclear','All tyrosine kinase'],'All are GPCRs.'),
('Exception to GPCR among 5-HT receptors is:','5-HT3 (Ion channel receptors)',['5-HT1A','5-HT2','5-HT7'],'Exception: 5-HT3 (Ion channel receptors).'),
('5-HT1A agonists location is:','Pre-synaptic serotonergic neurons',['Post-synaptic only','CN V trigeminal','Leucocyte'],'Location: Pre-synaptic serotonergic neurons.'),
('5-HT1A subtype is:','Gi',['Gq','Gs','Ion channel'],'Subtype: Gi.'),
('5-HT1A agonists are:','Buspirone, Epsapirone, Gepirone',['Lasmiditan and triptans','Ergotamine only','Chlorpromazine'],'Buspirone Epsapirone Gepirone.'),
('5-HT1A agonists used as:','Non-benzodiazepine anxiolytics',['Antidepressants only','Antiemetics','Prokinetics'],'Used as Non-benzodiazepine anxiolytics.'),
('5-HT1A agonists effect on anxiety is:','Decreased anxiety',['Increased anxiety','No effect','Only sedation'],'↓ Anxiety Brain.'),
('5-HT1A agonists mechanism decreases:','5-HT2 activity',['5-HT3 only','5-HT4 only','Dopamine only'],'↓ 5-HT2 Brain.'),
])
unit('5-HT1B/1D/1F, CGRP Pathway and Migraine Biology',
 '5-HT1B/1D and 5-HT1F receptors are located on trigeminal nerve CN V, subtype Gi. In migraine, trigeminal ganglion nucleus releases CGRP via axon acting on CGRP receptor on meningeal blood vessels causing dilation, meningeal edema and compression leading to headache. 5-HT1F agonist lasmiditan acts at CN V nucleus, triptans act at 5-HT1B/1D on axon inhibiting CGRP release; CGRP ligand blockers eptinezumab, fremanezumab, galcanezumab are parenteral for prophylaxis, CGRP receptor blockers erenumab and atogepant are oral for prophylaxis, rimegepant is oral for acute attack.')
facts(233,[
('5-HT1B/1D and 5HT1F location is:','CN V (Trigeminal)',['Pre-synaptic serotonergic neurons','Leucocyte','Post-synaptic GI'],'Location: CN V (Trigeminal).'),
('5-HT1B/1D subtype is:','Gi',['Gq','Gs','Ion channel'],'Subtype: Gi.'),
('In migraine, CGRP is released from:','Axon of trigeminal nerve',['Pre-synaptic serotonergic neuron','Leucocyte','Only blood vessel'],'Axon CGRP.'),
('CGRP acts on:','CGRP Receptor on meningeal blood vessel',['5-HT1A receptor','H1 receptor','Dopamine receptor'],'CGRP Receptor meningeal Blood vessel.'),
('CGRP receptor activation causes:','Dilation -> meningeal edema & compression -> headache: migraine',['Constriction only','No edema','Only nausea'],'↓ Dilation ↓ meningeal Edema & Compression ↓ Headache: migraine.'),
('5-HT1F agonist is:','Lasmiditan',['Sumatriptan','Buspirone','Ergotamine'],'Lasmiditan.'),
('Triptans act on:','5-HT1B/1D (Gi) to inhibit CGRP release',['5-HT1A only','5-HT2 only','5-HT3 only'],'5-HT1B/1D (Gi) Triptans.'),
('CGRP Ligand blockers are:','Eptinezumab, Fremanezumab, Galcanezumab',['Erenumab and atogepant','Rimegepant only','Lasmiditan only'],'CGRP Ligand blockers Eptinezumab Fremanezumab Galcanezumab.'),
('CGRP Ligand blockers route and use are:','Parenterally for prophylaxis of migraine',['Oral for acute attack','Only IV for acute','Only for cluster'],'Parenterally for prophylaxis of migraine.'),
('CGRP Receptor blockers are:','Erenumab, Atogepant, Rimegepant',['Eptinezumab and fremanezumab','Only lasmiditan','Only triptans'],'CGRP Receptor blockers Erenumab Atogepant Rimegepant.'),
('Erenumab and atogepant are:','PO for prophylaxis',['Parenteral for prophylaxis','Only for acute attack','Only IV'],'PO for prophylaxis.'),
('Rimegepant is:','PO for Rx of acute attack',['Parenteral for prophylaxis','Only for prophylaxis','Only IV'],'Rimegepant: PO for Rx of acute attack.'),
('Triptans are approved for:','Acute Rx of migraine',['Prophylaxis only','Only chronic tension headache','Only cluster prophylaxis'],'Triptans: Approved for acute Rx of migraine.'),
])
unit('Triptans for Acute Migraine: Pharmacokinetics and Drugs',
 'Triptans stimulate 5-HT1B decreasing CGRP release and cause vasoconstriction; they differ in pharmacokinetics more than pharmacodynamics with rate of absorption proportional to efficacy and potency. Oral frovatriptan acts for 27 hours and naratriptan for 6 hours with slow oral absorption making them long acting and slow acting used in prolonged attack; fast oral absorption drugs rizatriptan fastest acting, sumatriptan, zolmitriptan, eletriptan and almotriptan are short and fast acting preferred for acute attack; nasal spray zolmitriptan and sumatriptan; subcutaneous/rectal sumatriptan is overall fastest acting.')
facts(234,[
('Triptans mechanism of action is:','Stimulate 5-HT1B -> decreased CGRP Release and vasoconstriction',['Only vasodilation','Only CGRP increase','Block 5-HT3'],'Stimulate 5-HT1B -> ↓ CGRP Release, Vasoconstriction.'),
('Triptans differ in:','Pharmacokinetics > Pharmacodynamics',['Pharmacodynamics only','No difference','Only in toxicity'],'Differ in Pharmacokinetics > Pharmacodynamics.'),
('Rate of absorption of triptans is:','Proportional to efficacy & potency',['Inversely proportional','No relation','Only affects toxicity'],'Rate of absorption ∝ Efficacy & potency.'),
('Frovatriptan acts for:','27 hrs',['6 hrs','1 hr','12 hrs'],'Frovatriptan (Acts for: 27 hrs).'),
('Naratriptan acts for:','6 hrs',['27 hrs','1 hr','24 hrs'],'Naratriptan (6 hrs).'),
('Frovatriptan and naratriptan absorption is:','Slow oral absorption -> Long acting + Slow acting',['Fast oral absorption -> Short & fast acting','No absorption','Only IV'],'Slow oral absorption -> Long acting + Slow acting.'),
('Frovatriptan and naratriptan used in:','Prolonged attack',['Acute attack preferred','Only in pregnancy','Only prophylaxis'],'Used in: Prolonged attack.'),
('Fastest acting oral triptan is:','Rizatriptan',['Frovatriptan','Naratriptan','Almotriptan'],'Rizatriptan (Fastest acting).'),
('Fast oral absorption triptans are:','Rizatriptan, Sumatriptan, Zolmitriptan, Eletriptan, Almotriptan',['Frovatriptan and naratriptan','Only sumatriptan','Only zolmitriptan'],'Fast oral absorption -> Short & fast acting.'),
('Fast oral absorption triptans are preferred for:','Acute attack',['Prolonged attack','Prophylaxis','Only in pregnancy'],'Preferred Acute attack.'),
('Nasal spray triptans are:','Zolmitriptan and Sumatriptan',['Only frovatriptan','Only naratriptan','Only eletriptan'],'Nasal Spray: Zolmitriptan, Sumatriptan.'),
('Overall fastest acting triptan route is:','Subcutaneous/Rectal Sumatriptan',['Oral frovatriptan','Nasal zolmitriptan','Oral rizatriptan'],'Sumatriptan: Overall fastest acting.'),
])
unit('Triptans: Side Effects and Contraindications',
 'Coronary vasoconstriction from triptans causes acute chest pain, pain in jaw/neck, sweating and arrhythmia. Contraindications are ischemic heart disease with MI/angina, no stroke/TIA, ischemic bowel disease, hypertension/PVD with Raynaud/Burger disease. Specific contraindications: naratriptan in liver/renal failure, eletriptan in liver failure, zolmitriptan in Wolf-Parkinson-White WPW syndrome.')
facts(234,[
('Triptans side effect coronary vasoconstriction causes:','Acute chest pain',['Only headache','Only nausea','Only dizziness'],'Acute chest pain.'),
('Coronary vasoconstriction also causes:','Pain in Jaw/neck, sweating, arrhythmia',['Only chest pain','Only GI upset','Only visual changes'],'Pain in Jaw/neck, Sweating, Arrhythmia.'),
('Triptans contraindicated in:','Ischemic Heart Disease (IHD): MI/Angina',['Only in pregnancy','Only in children','Only in elderly'],'Ischemic Heart Disease (IHD): MI/Angina.'),
('Triptans C/I also include:','No stroke/TIA, Ischemic Bowel Disease, HTN/PVD (Raynaud/Burger)',['Only IHD','Only pregnancy','Only liver failure'],'No stroke/TIA, Ischemic Bowel Disease, HTN/PVD (Raynaud/Burger).'),
('Naratriptan specific C/I is:','Liver /Renal failure',['Only cardiac','Only WPW','Only liver failure alone'],'Naratriptan: Liver /Renal failure.'),
('Eletriptan specific C/I is:','Liver failure',['Renal failure','WPW syndrome','Only IHD'],'Eletriptan: Liver failure.'),
('Zolmitriptan specific C/I is:','Wolf-Parkinson-White (WPW) Syndrome',['Liver failure','Renal failure','Only IHD'],'Zolmitriptan: Wolf-Parkinson-White (WPW) Syndrome.'),
])
unit('Other Acute Migraine Drugs and Pregnancy Management',
 'Other acute drugs: 5HT-1F agonist lasmiditan, CGRP receptor blocker rimegepant, ergot alkaloids ergotamine non-selective agonist very potent vasoconstrictor with side effect gangrene of organs with end arteries feet most common and dihydroergotamine less potent better tolerated with same S/E and C/I as triptans, D2 blockers chlorpromazine and metoclopramide, NSAIDs paracetamol for mild-moderate and ketorolac for severe attack, opioids intranasal butorphanol and oral codeine. In pregnancy DOC is paracetamol, if no response codeine/caffeine/metoclopramide, if no response sumatriptan is triptan of choice; triptans may block placental blood flow.')
facts(235,[
('5HT-1F Agonist for migraine is:','Lasmiditan',['Triptan','Ergotamine','Rimegepant'],'2. 5HT-1F Agonists: Lasmiditan.'),
('CGRP Receptor Blocker for acute attack is:','Rimegepant',['Eptinezumab','Fremanezumab','Galcanezumab'],'3. CGRP Receptor Blockers: Rimegepant.'),
('Ergotamine mechanism is:','5-HT e/o Non selective agonist -> potent vasoconstrictor',['Selective 5-HT1B only','Only CGRP blocker','Only D2 blocker'],'S-HT e/o: Non selective agonist -> ↑↑Potent vasoconstrictor.'),
('Ergotamine side effect is:','Gangrene of organs with end arteries: Feet (m/c)',['Only headache','Only nausea','Only chest pain'],'Gangrene of organs with end arteries: Feet (m/c).'),
('Dihydroergotamine is:','Less potent -> Better tolerated, S/E & C/I same as triptans',['More potent than ergotamine','Not related to ergot','Only for prophylaxis'],'Less potent -> Better tolerated, S/E & C/I: Same as triptans.'),
('D2 blockers for migraine are:','Chlorpromazine and metoclopramide',['Only chlorpromazine','Only metoclopramide','Only domperidone'],'5. D2 Blockers: Chlorpromazine, metoclopramide.'),
('NSAIDs for migraine mild-moderate attack:','Paracetamol',['Ketorolac','Only triptans','Only ergotamine'],'Paracetamol: mild - moderate attack.'),
('NSAID for severe migraine attack:','Ketorolac',['Paracetamol','Ibuprofen only','Aspirin only'],'Ketorolac: Severe attack.'),
('Opioids for migraine are:','Intranasal butorphanol and oral codeine',['Only morphine','Only tramadol','Only fentanyl'],'Intranasal butorphanol, Oral codeine.'),
('In pregnancy DOC for migraine is:','Paracetamol',['Sumatriptan','Ergotamine','Naratriptan'],'DOC: Paracetamol.'),
('If no response to paracetamol in pregnancy:','Codeine/Caffeine/metoclopramide',['Triptans directly','Ergotamine','Stop treatment'],'No response Codeine/Caffeine/metoclopramide.'),
('If no response to codeine/caffeine/metoclopramide in pregnancy:','Triptan: Sumatriptan (Triptan of choice in pregnancy)',['Ergotamine','Frovatriptan','Naratriptan'],'No response Triptan: Sumatriptan (Triptan of choice in pregnancy).'),
('Triptans in pregnancy may:','Block placental blood flow',['Increase fetal growth','No effect on placenta','Only cause teratogenicity'],'Triptans: may block placental blood flow.'),
])
unit('Migraine Prophylaxis and 5-HT2 Drugs',
 'Prophylaxis mnemonic Flunarizine Can PREVENT migraine includes flunarizine, cyproheptadine/candesartan/clonidine, pizotifen/propranolol DOC, release GABA gabapentin, valproate, nortiptyline, topiramate and methysergide. 5-HT2 antagonist cyproheptadine blocks H1 and muscarinic, used for migraine prophylaxis, serotonin syndrome, carcinoid syndrome, cold urticaria and AIDS weight gain; pizotifen for migraine prophylaxis; methysergide for migraine prophylaxis with fibrosis side effect pulmonary, cardiac and retroperitoneal; flibanserin is 5HT2A antagonist plus 5HT1A agonist for hypoactive sexual desire disorder HSDD in females. 5-HT2 agonist lorcaserin was used for obesity but banned due to increased cancer risk; 5-HT3 antagonists are antiemetics and 5-HT4 agonists are prokinetics.')
facts(235,[
('Migraine prophylaxis mnemonic is:','Flunarizine Can PREVENT migraine',['Only propranolol','Only valproate','Only flunarizine'],'Mnemonic: Flunarizine Can PREVENT migraine.'),
('DOC for migraine prophylaxis is:','Pizotifen/Propranolol',['Flunarizine only','Valproate only','Topiramate only'],'Pizotifen/Propranolol: DOC.'),
('Drugs for migraine prophylaxis include:','Flunarizine, Cyproheptadine/Candesartan/Clonidine, Pizotifen/Propranolol, Gabapentin, Valproate, Nortiptyline, Topiramate, Methysergide',['Only triptans','Only ergotamine','Only NSAIDs'],'List: Flunarizine, Cyproheptadine/Candesartan/Clonidine, Pizotifen/Propranolol, Release GABA: Gabapentin, Valproate, Nortiptyline, Topiramate, methysergide.'),
('Release GABA drug for migraine prophylaxis is:','Gabapentin',['Valproate','Topiramate','Propranolol'],'Release GABA: Gabapentin.'),
('5-HT2 antagonist cyproheptadine blocks:','H1 and muscarinic',['Only 5-HT2','Only H2','Only D2'],'Cyproheptadine (-) H1 m.'),
('Cyproheptadine uses are:','Migraine prophylaxis, serotonin syndrome, carcinoid syndrome, cold urticaria, AIDS weight gain',['Only migraine prophylaxis','Only serotonin syndrome','Only cold urticaria'],'Uses: migraine prophylaxis, Serotonin syndrome, Carcinoid syndrome, Cold urticaria, AIDS weight gain.'),
('Pizotifen used for:','Migraine prophylaxis',['Serotonin syndrome','Carcinoid','Only AIDS weight gain'],'Pizotifen: migraine prophylaxis.'),
('Methysergide used for:','Migraine prophylaxis',['Only serotonin syndrome','Only carcinoid','Only obesity'],'Methysergide: migraine prophylaxis.'),
('Methysergide S/E is:','Fibrosis: Pulmonary, Cardiac, Retroperitoneal',['Only hepatotoxicity','Only nephrotoxicity','Only QT prolongation'],'S/E: Fibrosis -> Pulmonary, Cardiac, Retroperitoneal.'),
('Flibanserin is:','5HT2A (-) + 5HT1A agonist, Rx: Hypoactive Sexual Desire Disorder (HSDD) in females',['Only 5HT2 antagonist','Only for migraine','Only for obesity'],'5HT2A (-) + 5HT1 agonist Rx: HSDD in females.'),
('Lorcaserin use and ban reason:','Use: Rx of obesity, Banned: increased risk of cancer',['Use: migraine, banned for fibrosis','Use: anxiety, banned for liver failure','Use: depression, banned for stroke'],'Use: Rx of obesity, Banned: ↑ Risk of cancer.'),
])
unit('Obesity Treatment and Banned Drugs',
 'Drugs causing anorexia for obesity are liraglutide and phentermine; inhibitor of lipolysis is orlistat; stimulator of lipolysis is mirabegron; unknown mechanisms are topiramate, naltrexone and bupropion. Note: 5-HT3 antagonists are antiemetics and 5-HT4 agonists are prokinetics. Banned drugs: rimonabant increased suicidal tendency, lorcaserin cancer, phenylpropanolamine norephedrine stroke, sibutramine myocardial infarction.')
facts(236,[
('Drugs causing anorexia for obesity are:','Liraglutide and phentermine',['Orlistat only','Mirabegron only','Topiramate only'],'Drugs Causing Anorexia: Liraglutide, Phentermine.'),
('Inhibitor of lipolysis for obesity is:','Orlistat',['Mirabegron','Liraglutide','Phentermine'],'Inhibitors of Lipolysis: Orlistat.'),
('Stimulator of lipolysis is:','Mirabegron',['Orlistat','Liraglutide','Topiramate'],'Stimulators of lipolysis: mirabegron.'),
('Unknown mechanism obesity drugs are:','Topiramate, Naltrexone, Bupropion',['Liraglutide and phentermine','Orlistat only','Mirabegron only'],'Unknown mechanism: Topiramate, Naltrexone, Bupropion.'),
('5-HT3 (-) are:','Antiemetics',['Prokinetics','Anxiolytics','Antidepressants'],'5-HT3 (-): Antiemetics.'),
('5-HT4 (+) are:','Prokinetics',['Antiemetics','Anxiolytics','Antipsychotics'],'5-HT4 (+): Prokinetics.'),
('Rimonabant banned due to:','Increased suicidal tendency',['Cancer','Stroke','MI'],'Rimonabant ↑ suicidal tendency.'),
('Lorcaserin banned due to:','Cancer',['Suicidal tendency','Stroke','MI'],'Lorcaserin Cancer.'),
('Phenylpropanolamine (Norephedrine) banned due to:','Stroke',['Cancer','MI','Suicidal tendency'],'Phenylpropanolamine (Norephedrine) Stroke.'),
('Sibutramine banned due to:','Myocardial infarction',['Stroke','Cancer','Suicidal tendency'],'Sibutramine myocardial infarction.'),
])
finish()

# CHAPTER 60 - EICOSANOIDS (p237-241) ----------------------------------------
start(60)
unit('Eicosanoid Synthesis and Inhibitors',
 'Arachidonic acid via COX I and II forms prostaglandins mediating pain, pyrexia and inflammation and thromboxane A2 causing platelet aggregation; via 5-LOX forms leukotrienes C4 and D4 which are bronchoconstrictors. NSAIDs inhibit COX I and II reversibly except aspirin which is irreversible; zileuton inhibits 5-LOX; montelukast/zafrlukast block leukotriene receptors. COX is cyclooxygenase and LOX is lipooxygenase.')
facts(237,[
('Arachidonic acid via COX forms:','Prostaglandins and Thromboxane A2',['Only leukotrienes','Only prostaglandins','Only thromboxane'],'COX -> Prostaglandins Thromboxane A2.'),
('Prostaglandins mediate:','Pain, Pyrexia, Inflammation',['Only platelet aggregation','Only bronchoconstriction','Only chemotaxis'],'Prostaglandins mediate Pain Pyrexia Inflammation.'),
('Thromboxane A2 causes:','Platelet aggregation',['Bronchoconstriction only','Vasodilation only','Only pain'],'Thromboxane A2 Platelet aggregation.'),
('Arachidonic acid via 5-LOX forms:','Leukotrienes C4 and D4 (Broncho constrictors)',['Prostaglandins','Thromboxane','Only PG I2'],'Leukotrienes C4 D4 (Broncho constrictors).'),
('NSAIDs inhibit COX:','Reversibly except aspirin which is irreversible',['All irreversibly','All reversibly including aspirin','Only COX II'],'All are reversible NSAIDs except aspirin Irreversible (Aspirin).'),
('Zileuton inhibits:','5-LOX',['COX I','COX II','Only COX I and II'],'5-LOX X Zileuton.'),
('Montelukast/zafrleukast block:','Leukotriene C4/D4 receptors',['COX I','5-LOX','Thromboxane receptor'],'Montelukast/zafrleukast X Leukotrienes.'),
('COX stands for:','CycloOxygenase',['LipoOxygenase','Cyclic Oxygenase','Carbon Oxygenase'],'COX: CycloOxygenase.'),
('LOX stands for:','LipoOxygenase',['CycloOxygenase','Lipid Oxygenase','LipoXxygenase'],'LOX: LipoOxygenase.'),
])
unit('Prostaglandin E1 and E2 Analogs',
 'Prostaglandin E1 common use is maintaining patency of ductus arteriosus. Misoprostol is used for NSAID induced gastric ulcer, abortion and post partum hemorrhage least effective; alprostadil is used for erectile dysfunction ED. Drugs used in ED include phentolamine, bremelanotide, naltrexone, ketanserin, sildenafil DOC, alprostadil, trazadone and alviptadil. Prostaglandin E2 dinoprostone is used for PPH and cervical ripening DOC.')
facts(237,[
('Prostaglandin E1 common use is:','Maintain patency of Ductus arteriosus',['Close PDA','Only for PPH','Only for glaucoma'],'Common use: maintain patency of Ductus arteriosus.'),
('Misoprostol uses are:','NSAID induced gastric ulcer, Abortion, Post Partum Hemorrhage (Least effective)',['Only PPH','Only abortion','Only gastric ulcer'],'Misoprostol: NSAID induced gastric ulcer, Abortion, Post Partum Hemorrhage (Least effective).'),
('Least effective drug for PPH is:','Misoprostol',['Dinoprostone','Carboprost','Oxytocin'],'Post Partum Hemorrhage (Least effective).'),
('Alprostadil is used for:','Erectile dysfunction (ED)',['PDA maintenance','PPH','Cervical ripening'],'Alprostadil use Erectile dysfunction (ED).'),
('DOC for erectile dysfunction is:','Sildenafil',['Alprostadil','Phentolamine','Trazadone'],'Sildenafil: DOC.'),
('Drugs used in ED include:','Phentolamine, Bremelanotide, Naltrexone, Ketanserin, Sildenafil DOC, Alprostadil, Trazadone, Alviptadil',['Only sildenafil','Only alprostadil','Only phentolamine'],'Drugs used in ED: Phentolamine, Bremelanotide, Naltrexone, Ketanserin, Sildenafil DOC, Alprostadil, Trazadone, Alviptadil.'),
('Dinoprostone is:','Prostaglandin E2',['Prostaglandin E1','Prostaglandin F2α','Prostaglandin I2'],'Prostaglandin E2: Dinoprostone.'),
('Dinoprostone uses are:','PPH and Cervical ripening DOC',['Only PPH','Only glaucoma','Only ED'],'Use PPH Cervical ripening: DOC.'),
('Cervical ripening DOC is:','Dinoprostone',['Misoprostol','Carboprost','Oxytocin'],'Cervical ripening: DOC.'),
])
unit('Prostaglandin I2, F2α and Other PHTN Drugs',
 'Prostaglandin I2 use is pulmonary hypertension due to vasodilation; drugs are epoprostenol recombinant PGI2, iloprost, beraprost and treprostinil as PGI2 analogs and selexipag as PGI2 receptor agonist; other PHTN drugs are endothelin antagonists bosentan and ambrisentan. Prostaglandin F2α drugs carboprost for PPH and abortion and latanoprost and bimatoprost eye drops DOC for open angle glaucoma and normal tension glaucoma with side effects heterochromia iridis, dry/sandy eyes, macular edema and hypertrichosis used for hypotrichosis, contraindicated in uveitis.')
facts(237,[
('Prostaglandin I2a use is:','Pulmonary HTN (D/t vasodilation)',['Maintain PDA','Cervical ripening','Glaucoma'],'Use: Pulmonary HTN (D/t vasodilation).'),
('Epoprostenol is:','Recombinant PGI2',['PGE1','PGF2α','PGD2'],'Epoprostenol: Recombinant PGI2.'),
('PGI2 analogs are:','Iloprost, Beraprost, Treprostinil',['Misoprostol and alprostadil','Latanoprost and bimatoprost','Only selexipag'],'Iloprost, Beraprost, Treprostinil PGI2 analogs.'),
('Selexipag is:','PGI2 receptor agonist',['PGE1 analog','PGF2α analog','PGI2 analog itself'],'Selexipag: PGI2 receptor agonist.'),
('Other drugs used in PHTN are:','Endothelin antagonists Bosentan, Ambrisentan',['Only sildenafil','Only alprostadil','Only calcium channel blockers'],'Other Drugs used in PHTN: Endothelin antagonists Bosentan Ambrisentan.'),
('Prostaglandin F2α drugs are:','Carboprost and Latanoprost & Bimatoprost',['Misoprostol and alprostadil','Epoprostenol only','Only dinoprostone'],'Prostaglandin F2α: Drugs.'),
('Carboprost uses are:','PPH & Abortion',['Only glaucoma','Only ED','Only cervical ripening'],'Carboprost: PPH & Abortion.'),
('Latanoprost & Bimatoprost eye drops DOC for:','Open angle glaucoma and Normal Tension glaucoma',['Only closed angle glaucoma','Only PPH','Only ED'],'DOC Open angle glaucoma (N) Tension glaucoma.'),
('PGF2α side effects are:','Heterochromia iridis, Dry/Sandy eyes, Macular edema, Hypertrichosis',['Only cataract','Only glaucoma','Only blindness'],'S/E: Heterochromia iridis, Dry/Sandy eyes, macular edema, Hypertrichosis.'),
('Hypertrichosis as side effect is used for:','Rx of Hypotrichosis',['Only cosmetic','Only for alopecia areata','Only for glaucoma'],'Hypertrichosis (Use: Rx of Hypotrichosis).'),
('PGF2α C/I is:','Uveitis',['Cataract','Only glaucoma','Only PPH'],'C/I: uveitis.'),
])
unit('Non-Selective COX Inhibitors: Paracetamol',
 'Non-selective COX inhibitors inhibit both COX I and COX II. Acetaminophen paracetamol mechanism is inhibition of COX I and II decreasing PG synthesis giving analgesia, antipyrexia and poor anti-inflammatory effect, plus activation of TRPV1 receptors and cannabinoid receptors. It is most common cause of drug induced liver failure via NAPQI metabolite depleting glutathione free radical scavenger causing free radical damage showing centrilobular necrosis with periportal sparing on HPE. It is also most common cause of drug poisoning with symptoms renal tubular necrosis, hypoglycemic coma and hepatotoxicity; dose 150-250 mg/kg or >10 g, fatal >20 g, prediction by Rumack Mathew Nomogram with plasma concentration vs time graph safe zone below and unsafe zone above at 4 hr and 10 hr cutoffs up to 24 hr; management <4 hr charcoal, DOC N-acetyl cysteine, if no response fulminant hepatic failure needs emergency liver transplant.')
facts(238,[
('Non selective COX inhibitors inhibit:','Both COX I & COX II',['Only COX I','Only COX II','Only LOX'],'(-) both COX I & COX II.'),
('Acetaminophen (Paracetamol) mechanism includes:','(-) COX I & II -> ↓ PG synthesis and (+) TRPV1 and Cannabinoid receptors',['Only COX II inhibition','Only LOX inhibition','Only TRPV1 inhibition'],'Mechanism: (-) COX I & II (+) TRPV1 Cannabinoid receptors.'),
('Paracetamol PG synthesis effects are:','Analgesia, Antipyrexia, Antiinflammatory (Poor effect)',['Only analgesia','Only antipyrexia','Only anti-inflammatory strong'],'↓ PG synthesis: Analgesia, Antipyrexia, Antiinflammatory (Poor effect).'),
('Paracetamol hepatotoxicity is:','Most common cause of drug induced liver failure',['Rare cause','Only with alcohol','Only in children'],'M/C cause of drug induced liver failure.'),
('Paracetamol hepatotoxic metabolite is:','NAPQI (Paracetamol metabolite)',['Glutathione itself','Only sulfate conjugate','Only glucuronide'],'NAPQI (Paracetamol metabolite).'),
('NAPQI depletes:','Glutathione (Free radical scavenger)',['Only albumin','Only bilirubin','Only glucose'],'Depletes Glutathione (Free radical scavenger).'),
('Free radical damage to liver on HPE shows:','Centrilobular necrosis + Periportal sparing',['Only periportal necrosis','Only centrilobular sparing','Panlobular necrosis'],'On HPE Centrilobular necrosis + Periportal sparing.'),
('Most common cause of drug poisoning is:','Paracetamol',['Aspirin','Ibuprofen','Warfarin'],'M/C cause of drug poisoning: Paracetamol.'),
('Paracetamol poisoning symptoms include:','Renal tubular necrosis, Hypoglycemic coma, Hepatotoxicity',['Only hepatotoxicity','Only renal failure','Only coma'],'Symptoms: Renal tubular necrosis, Hypoglycemic coma, Hepatotoxicity.'),
('Paracetamol toxic dose is:','150-250 mg/kg or >10 g',['50-100 mg/kg','<5 g','Only >20 g'],'Dose: 150-250 mg/kg or >10 g.'),
('Fatal dose of paracetamol is:','>20 g',['>10 g','>5 g','>30 g'],'Fatal: >20 g.'),
('Prediction of hepatotoxicity uses:','Rumack Mathew Nomogram',['Only clinical features','Only LFT','Only INR'],'Prediction of hepatotoxicity: Rumack Mathew Nomogram.'),
('Rumack Mathew graph axes are:','Plasma concentration vs Time',['Dose vs weight','Only concentration','Only time'],'Graph Plasma concentration vs Time.'),
('Graph zones are:','Safe zone and unsafe zone',['Only safe zone','Only unsafe zone','No zones'],'Safe zone Unsafe zone.'),
('Cutoffs on nomogram are:','4 hr and 10 hr up to 24 hr',['Only 4 hr','Only 10 hr','Only 24 hr'],'4 hr 10 hr 24 hr.'),
('Management <4 hr of consumption:','Charcoal',['NAC only','Liver transplant','Only observation'],'<4 hr of consumption: Charcoal.'),
('DOC for paracetamol poisoning is:','N-acetyl cysteine',['Charcoal only','Liver transplant directly','Only dialysis'],'DOC: N-acetyl cysteine.'),
('If no response to NAC:','Fulminant hepatic failure -> Emergency liver transplant',['Only charcoal again','Only observation','Only dialysis'],'No response Fulminant hepatic failure Emergency liver transplant.'),
])
unit('Aspirin: Dose Dependent Effects and Uses',
 'Aspirin dose dependent effect: 50-325 mg OD antiaggregant, 325-650 mg SOS max 4 doses/day analgesic antipyretic, 3-4 g/day divided doses anti-inflammatory. Uses: antiaggregant, rheumatoid arthritis, rheumatic arthritis, niacin induced flushing DOC, essential thrombocythemia, Kawasaki disease, decreased risk of colon cancer. Side effects: bleeding most common, Reye syndrome viral fever in children aspirin leads to hepatic encephalopathy, salicylism toxicity dose >10 g with clinical features seizures, tinnitus, hyperglycemia, metabolic acidosis treated symptomatically and dialysis in severe toxicity. Contraindications: viral fever in children, gout decreased uric acid excretion, with warfarin increased bleeding risk.')
facts(239,[
('Aspirin 50-325 mg OD is:','Antiaggregant',['Analgesic antipyretic','Anti-inflammatory','Only antipyretic'],'50-325 mg OD: Antiaggregant.'),
('Aspirin 325-650 mg SOS (max 4 doses/day) is:','Analgesic, Antipyretic',['Antiaggregant only','Anti-inflammatory only','Only antiaggregant'],'325-650 mg SOS (max 4doses/day): Analgesic, Antipyretic.'),
('Aspirin 3-4 g/day (Divided doses) is:','Anti-inflammatory',['Only antiaggregant','Only analgesic','Only antipyretic'],'3-4 g/day (Divided doses): Anti-inflammatory.'),
('Aspirin uses include:','Antiaggregant, Rheumatoid arthritis, Rheumatic arthritis, Essential thrombocythemia, Kawasaki disease, ↓ Risk of colon cancer',['Only antiaggregant','Only analgesic','Only PPH'],'Uses list.'),
('DOC for niacin induced flushing is:','Aspirin',['Only laropiprant','Only clopidogrel','Only paracetamol'],'Niacin induced flushing: DOC.'),
('Most common S/E of aspirin is:','Bleeding',['Reye syndrome','Salicylism','Tinnitus only'],'Bleeding: m/c.'),
('Reye Syndrome is:','Viral fever in children + Aspirin -> Hepatic Encephalopathy',['Only hepatic failure','Only encephalopathy','Only with paracetamol'],'Reye Syndrome: Viral fever in children Aspirin -> Hepatic Encephalopathy.'),
('Salicylism (Toxicity) dose is:','>10 g',['>20 g','>5 g','>15 g'],'Dose >10g.'),
('Clinical features of salicylism include:','Seizures, Tinnitus, Hyperglycemia, Metabolic acidosis',['Only seizures','Only tinnitus','Only metabolic alkalosis'],'Clinical features: Seizures, Tinnitus, Hyperglycemia, Metabolic acidosis.'),
('Rx of aspirin toxicity is:','Symptomatic and Dialysis in severe toxicity',['Only charcoal','Only NAC','Only liver transplant'],'Rx of toxicity: Symptomatic, Dialysis: Severe toxicity.'),
('Aspirin C/I include:','Viral fever in children, Gout: (-) uric acid excretion, With warfarin: ↑ Risk of bleeding',['Only viral fever','Only gout','Only warfarin'],'C/I: Viral fever in children, Gout, With warfarin.'),
('Aspirin in gout:','Decreases uric acid excretion',['Increases excretion','No effect','Only increases metabolism'],'Gout: (-) uric acid excretion.'),
('Aspirin with warfarin:','Increases risk of bleeding',['Decreases bleeding','No interaction','Only decreases warfarin effect'],'With warfarin: ↑ Risk of bleeding.'),
])
unit('Other Non-Selective NSAIDs: Indomethacin to Ketorolac',
 'Indomethacin inhibits COX, phospholipase A and C, and leucocyte proliferation and migration; uses acute gout DOC, Bartter syndrome and paroxysmal hemicrania; side effect frontal headache. Sulindac is indomethacin derivative with similar uses, blocks FAP familial adenomatous polyposis decreasing colon carcinoma risk and decreasing breast and prostate cancer risk. Ibuprofen uses analgesic anti-inflammatory and PDA closure DOC for closure in India with side effects aseptic meningitis most common drug inducing and toxic amblyopia/blurred vision; note PDA worldwide DOC is indomethacin. Ketoprofen inhibits COX, LOX, stabilizes lysosome and inhibits bradykinin; flurbiprofen eye drops prevent intra-operative miosis; piroxicam has enterohepatic circulation longest acting with slow onset for chronic pain; ketorolac has increased potency used for acute pain oral/parenteral, migraine intranasal spray and ocular pain/inflammation eye drops.')
facts(240,[
('Indomethacin mechanism is:','(-) COX, (-) Phospholipase A & C, (-) Leucocyte Proliferation & migration',['Only COX inhibition','Only LOX inhibition','Only phospholipase A'],'Mechanism: (-) COX (-) Phospholipase A & C (-) Leucocyte Proliferation migration.'),
('Indomethacin use acute gout is:','DOC',['Second line','Not used','Only prophylaxis'],'Acute gout: DOC.'),
('Indomethacin uses also include:','Bartter syndrome and Paroxysmal hemicrania',['Only gout','Only PDA','Only pain'],'Bartter syndrome, Paroxysmal hemicrania.'),
('Indomethacin S/E is:','Frontal headache',['Occipital headache','Only GI ulcer','Only renal failure'],'Frontal headache.'),
('Sulindac is:','Indomethacin derivative: Similar uses',['Ibuprofen derivative','Aspirin derivative','Paracetamol derivative'],'Indomethacin derivative: Similar uses.'),
('Sulindac blocks:','FAP (Familial Adenomatous Polyposis): ↓ Risk of colon carcinoma',['Only pain','Only gout','Only PDA'],'Blocks FAP (Familial Adenomatous Polyposis): ↓ Risk of colon carcinoma.'),
('Sulindac also decreases risk of:','Breast & prostate cancer',['Only colon','Only lung','Only skin'],'↓ Risk of Breast & prostate cancer.'),
('Ibuprofen uses are:','Analgesic & Anti-inflammatory and Patent ductus arteriosus: DOC for closure (India)',['Only analgesic','Only PDA worldwide','Only gout'],'Analgesic & Anti-inflammatory, Patent ductus arteriosus: DOC for closure (India).'),
('Ibuprofen S/E is:','Most common drug inducing Aseptic meningitis and Toxic amblyopia/Blurred vision',['Only GI ulcer','Only renal failure','Only hepatotoxicity'],'M/C drug inducing Aseptic meningitis, Toxic amblyopia/Blurred vision.'),
('PDA worldwide DOC is:','Indomethacin',['Ibuprofen','Paracetamol','Aspirin'],'Note: PDA world wide DOC is Indomethacin.'),
('Ketoprofen mechanism includes:','(-) COX, (-) LOX, Stabilizes lysosome, (-) Bradykinin',['Only COX','Only LOX','Only bradykinin'],'Mechanism: (-) COX (-) LOX Stabilizes lysosome (-) Bradykinin.'),
('Flurbiprofen use is:','Eye drops Prevent Intra-operative miosis',['Only oral for pain','Only for gout','Only for PDA'],'Use: Eye drops Prevent Intra-operative miosis.'),
('Piroxicam property is:','Enterohepatic circulation: Longest acting, Slow onset of action: Analgesic in chronic pain',['Shortest acting','No enterohepatic','Fast onset for acute pain'],'Enterohepatic circulation: Longest acting, Slow onset of action: Analgesic in chronic pain.'),
('Ketorolac potency is:','Increased potency',['Decreased potency','Same as ibuprofen','Only weak'],'↑ Potency.'),
('Ketorolac uses are:','Acute pain: Oral/Parenteral, Migraine: Intranasal spray, Ocular pain/Inflammation: Eye drops',['Only acute pain oral','Only migraine','Only ocular'],'Uses: Acute pain: Oral/Parenteral, Migraine: Intranasal spray, Ocular pain/Inflammation: Eye drops.'),
])
unit('Diclofenac, Naproxen and Selective COX II Inhibitors',
 'Diclofenac has short half life but long acting due to concentration in joints with side effects hepatotoxic and GI ulcers decreased by formulation with misoprostol; uses rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis, gout, dysmenorrhea and acute pain. Naproxen is an enantiomer; nabumetone is naproxen derivative non-acidic long acting OD. Selective COX II inhibitors classification oral celecoxib and etoricoxib, parenteral IV parecoxib for acute post-op pain; uses anti-inflammatory rheumatoid, rheumatic, psoriatic, ankylosing, gout and pain third line dysmenorrhea acute pain; side effects most common hypersensitivity rash, nephrotoxicity renal papillary necrosis, cardiotoxicity rofecoxib and valdecoxib, peptic ulcer non-selective greater than selective, DOC PPIs; drug interactions decrease effect of antihypertensives, decrease lithium clearance leading to toxicity and decrease effect of diuretics furosemide.')
facts(241,[
('Diclofenac T1/2 is:','Short T1/2 but Long acting d/t concentration in joints',['Long T1/2 and long acting','Short T1/2 short acting','Long T1/2 short acting'],'Short T1/2, Long acting d/t concentration in joints.'),
('Diclofenac S/E are:','Hepatotoxic and GI ulcers',['Only GI ulcers','Only hepatotoxic','Only renal failure'],'Hepatotoxic, GI ulcers.'),
('GI ulcers with diclofenac decreased by:','Formulation with misoprostol',['Formulation with paracetamol','Only dose reduction','Only food intake'],'↓ By formulation with misoprostol.'),
('Diclofenac uses include:','Rheumatoid arthritis, Psoriatic arthritis, Ankylosing spondylitis, Gout, Dysmenorrhea, Acute pain',['Only rheumatoid','Only gout','Only dysmenorrhea'],'Uses: Rheumatoid arthritis, Psoriatic arthritis, Ankylosing spondylitis, Gout, Dysmenorrhea, Acute pain.'),
('Naproxen is:','Enantiomer',['Only racemate','Only prodrug','Only active metabolite'],'Enantiomer.'),
('Nabumetone (Naproxen derivative) is:','Non-acidic, Long acting (OD)',['Acidic short acting','Only IV','Only topical'],'Non-acidic, Long acting (OD).'),
('Selective COX II inhibitors oral are:','Celecoxib and Etoricoxib',['Only celecoxib','Only rofecoxib','Only valdecoxib'],'Oral Celecoxib, Enterocoxib.'),
('Selective COX II parenteral IV is:','Parecoxib: Use: Acute pain (Post-op)',['Celecoxib IV','Etoricoxib IV','Rofecoxib IV'],'Parenteral (IV) Parecoxib: Use: Acute pain (Post-op).'),
('Selective COX II anti-inflammatory uses are:','Rheumatoid arthritis, Rheumatic arthritis, Psoriatic arthritis, Ankylosing spondylitis, Gout',['Only rheumatoid','Only gout','Only dysmenorrhea'],'Anti-inflammatory: Rheumatoid, Rheumatic, Psoriatic, Ankylosing, Gout.'),
('Selective COX II pain uses are:','3rd line drugs for Dysmenorrhea and Acute pain',['1st line for all pain','Only for chronic pain','Only for post-op'],'Pain: 3rd line drugs, Dysmenorrhea, Acute pain.'),
('Selective COX II most common S/E is:','Hypersensitivity rash',['GI ulcer only','Cardiotoxicity only','Nephrotoxicity only'],'M/C: Hypersensitivity rash.'),
('Selective COX II nephrotoxicity is:','Renal papillary necrosis',['Only ATN','Only glomerulonephritis','Only nephrotic'],'Nephrotoxicity: Renal papillary necrosis.'),
('Cardiotoxic selective COX II are:','Refecoxib & Valdecoxib',['Celecoxib only','Parecoxib only','All selective'],'Cardiotoxicity: Refecoxib & Valdecoxib.'),
('Peptic ulcer risk:','Non-selective > Selective COX II (-)',['Selective > Non-selective','Equal','No ulcer with either'],'Non-selective > Selective COX II (-).'),
('DOC for NSAID induced peptic ulcer is:','PPIs',['H2 blockers','Misoprostol only','Antacids only'],'DOC: PPIs.'),
('Selective COX II drug interactions decrease:','Effect of antihypertensive drugs, Lithium clearance -> Toxicity, Effect of diuretics (Furosemide)',['Only antihypertensives','Only lithium','Only diuretics'],'↓ Effect of antihypertensive, ↓ Lithium clearance -> Toxicity, ↓ Effect of diuretics (Furosemide).'),
])
finish()

# CHAPTER 61 - GOUT (p242-243) -----------------------------------------------
start(61)
unit('Acute Gout: Aim and Drugs',
 'Aim of acute gout treatment is to decrease inflammation and symptomatic relief. First line is NSAIDs with no response leading to steroid; DOC is indomethacin due to multiple mechanisms of action. Second drug is colchicine which inhibits microtubules decreasing chemotaxis and migration of leucocytes, decreases IL-1 release from neutrophils and inhibits phagocytosis; side effects are nausea, vomiting, diarrhoea, bone marrow suppression and alopecia.')
facts(242,[
('Aim of acute gout Rx is:','Decrease inflammation + Symptomatic relief',['Only decrease uric acid','Only increase excretion','Only increase metabolism'],'Aim of Rx: ↓ Inflammation + Symptomatic relief.'),
('Acute gout drugs: NSAIDs no response leads to:','Steroid',['Colchicine directly','Allopurinol','Febuxostat'],'No response Steroid.'),
('DOC for acute gout is:','Indomethacin (multiple mechanisms of action)',['Colchicine','Allopurinol','Probenecid'],'DOC: Indomethacin (multiple mechanisms of action).'),
('Colchicine mechanism is:','(-)microtubules -> (-)Chemotaxis -> (-) migration of leucocytes',['Only increases uric acid excretion','Only inhibits xanthine oxidase','Only increases metabolism'],'(-)microtubules (-) Chemotaxis (-) migration of leucocytes.'),
('Colchicine also:','Decreases IL-1 release from neutrophils and inhibits phagocytosis',['Increases IL-1','Stimulates phagocytosis','Only blocks COX'],'↓IL-1 release from neutrophils, Inhibit phagocytosis.'),
('Side effects of colchicine are:','Nausea, Vomiting, Diarrhoea, Bone marrow suppression, Alopecia',['Only GI upset','Only alopecia','Only marrow suppression'],'Side effects: Nausea, Vomiting, Diarrhoea, Bone marrow suppression, Alopecia.'),
])
unit('Chronic Gout: Aim and Classification',
 'Aim of chronic gout is to prevent acute gout by decreasing uric acid via inhibiting synthesis with xanthine oxidase inhibitors, increasing excretion with uricosuric drugs and increasing metabolism with uricase analogues.')
facts(242,[
('Aim of chronic gout is:','To prevent acute gout by decreasing uric acid',['Only symptomatic relief','Only increase inflammation','Only increase uric acid'],'Aim: To prevent acute gout ↓uric acid.'),
('Chronic gout can be managed by:','(-) Synthesis (Xanthine Oxidase inhibitors), ↑ Excretion (Uricosuric Drugs), ↑ Metabolism (Uricase Analogues)',['Only synthesis inhibition','Only excretion increase','Only metabolism increase'],'(-) Synthesis Xanthine Oxidase inhibitors ↑Excretion Uricosuric Drugs ↑Metabolism Uricase Analogues.'),
])
unit('Xanthine Oxidase Inhibitors: Allopurinol',
 'Allopurinol is DOC for chronic gout, tumor lysis syndrome, Lesch Nyhan syndrome and organ transplant. Side effects are hypersensitivity most common Steven Johnson Syndrome associated with HLA-B-5801, inhibition of orotidylate decarboxylase causing orotic aciduria and DRESS syndrome. Side effects of class are xanthinuria leading to xanthine stones and acute gout precipitation prevented by NSAID/colchicine for 3-6 months. Drug interaction inhibits 6-mercaptopurine/azathioprine increasing toxicity.')
facts(242,[
('Xanthine oxidase inhibitors are used for:','Chronic gout',['Acute gout DOC','Only tumor lysis','Only Lesch Nyhan'],'Chronic gout.'),
('Allopurinol DOC includes:','Chronic gout, Tumor Lysis Syndrome, Lesch Nyhan Syndrome, Organ transplant',['Only chronic gout','Only tumor lysis','Only organ transplant'],'DOC Chronic gout, Tumor Lysis Syndrome, Lesch Nyhan, Organ transplant.'),
('Most common S/E of allopurinol is:','Hypersensitivity: Steven Johnson Syndrome (A/w: HLA-B-5801)',['Only DRESS','Only orotic aciduria','Only xanthinuria'],'Hypersensitivity (m/c): Steven Johnson Syndrome (A/w: HLA-B-5801).'),
('Allopurinol inhibits:','Orotidylate decarboxylase -> Orotic aciduria',['Only xanthine oxidase','Only HPRT','Only purine nucleoside phosphorylase'],'(-) Orotidylate decarboxylase -> Orotic aciduria.'),
('Allopurinol also causes:','DRESS Syndrome',['Only SJS','Only orotic aciduria','Only xanthinuria'],'DRESS Syndrome.'),
('Xanthine oxidase inhibitor class S/E:','Xanthinuria -> Xanthine stones',['Only urate stones','Only calcium stones','Only cysteine stones'],'Xanthinuria -> Xanthine stones.'),
('Acute gout with xanthine oxidase inhibitors prevented by:','NSAID/Colchicine x 3-6 months',['No prevention needed','Only allopurinol dose increase','Only stop drug'],'Acute gout Prevention -> NSAID/Colchicine x 3-6 months.'),
('Allopurinol drug interaction:','Inhibit 6-mercaptopurine/ Azathioprine -> ↑ Toxicity',['Decreases toxicity','No interaction','Only increases excretion'],'Inhibit 6-mercaptopurine/ Azathioprine -> ↑ Toxicity.'),
])
unit('Xanthine Oxidase Inhibitors: Oxypurinol and Febuxostat',
 'Oxypurinol is an orphan drug used for allopurinol hypersensitivity. Febuxostat is used for allopurinol intolerance and inadequate response to allopurinol with side effect increased risk of cardiovascular death.')
facts(243,[
('Oxypurinol is:','Orphan drug',['First line DOC','Only for tumor lysis','Only for Lesch Nyhan'],'Orphan drug.'),
('Oxypurinol use is:','Allopurinol hypersensitivity',['Allopurinol intolerance only','Inadequate response only','Only gout prophylaxis'],'Use: Allopurinol hypersensitivity.'),
('Febuxostat use is:','Allopurinol intolerance and Inadequate response to allopurinol',['Only hypersensitivity','Only first line DOC','Only tumor lysis'],'Use: Allopurinol intolerance, Inadequate response to allopurinol.'),
('Febuxostat S/E is:','Increased risk of cardiovascular death',['Only SJS','Only DRESS','Only xanthinuria'],'S/E: ↑ Risk of cardiovascular death.'),
])
unit('Uricosuric Drugs',
 'Uricosuric drugs are probenecid, sulfinpyrazone which are better as add on therapy than monotherapy, and benzbromarone and lesinraud which are most effective and used as add on therapy only. Side effects are increased urate stone formation contraindicated in history of renal stones, increased risk of calcium stones and precipitation of acute gout needing preventive prophylaxis. Contraindications renal failure except benzbromarone and lesinraud which can be used in mild-moderate renal failure. Miscellaneous drugs for chronic gout with comorbidities: losartan for hypertension, atorvastatin for increased LDL/cholesterol and fenofibrate for increased triglycerides.')
facts(243,[
('Uricosuric drugs are:','Probenecid, Sulfinpyrazone, Benzbromarone, Lesinraud',['Only probenecid','Only allopurinol','Only febuxostat'],'Drugs: Probenecid, Sulfinpyrazone, Benzbromarone, Lesinraud.'),
('Probenecid and sulfinpyrazone:','Add on therapy > monotherapy',['Monotherapy > add on','Only monotherapy','Only prophylaxis'],'Add on therapy > monotherapy.'),
('Most effective uricosurics are:','Benzbromarone and Lesinraud (Add on therapy only)',['Probenecid only','Sulfinpyrazone only','Only allopurinol'],'Most effective, Add on therapy only.'),
('Uricosuric S/E:','Increased urate stone formation: C/I in h/o renal stones',['No stone risk','Only calcium stones','Only xanthine stones'],'↑Urate stone formation: C/I in h/o renal stones.'),
('Uricosuric also increases risk of:','Calcium stones',['Xanthine stones only','No stone','Only urate'],'↑ Risk of calcium stones.'),
('Uricosuric may:','Precipitate acute gout (Preventive prophylaxis needed)',['Prevent acute gout','No effect on acute gout','Only treat acute gout'],'Precipitate acute gout (Preventive prophylaxis).'),
('Uricosuric contraindication:','Renal failure except Benzbromarone and Lesinraud',['No contraindication','Only liver failure','Only in gout'],'Contraindications: Renal failure except Benzbromarone, Lesinraud.'),
('Benzbromarone and lesinraud can be used in:','Mild-moderate renal failure',['Severe renal failure','No renal failure','Only normal renal function'],'Use: mild-moderate renal failure.'),
('Losartan in chronic gout is used when a/w:','HTN',['Increased LDL','Increased triglycerides','Only renal failure'],'Losartan HTN.'),
('Atorvastatin in chronic gout a/w:','Increased LDL/ Cholesterol',['HTN','Increased triglycerides','Only renal stones'],'Atorvastatin ↑LDL/ Cholesterol.'),
('Fenofibrate in chronic gout a/w:','Increased Triglycerides',['HTN','Increased LDL','Only urate stones'],'Fenofibrate ↑Triglycerides.'),
])
unit('Uricase Analogues',
 'No uric acid metabolism in humans. Pegloticase is used for resistant gout IV once every 2 weeks; rasburicase is DOC for high risk of tumor lysis syndrome in leukemia especially CLL. Side effects are hemolysis in G-6-PD deficiency and methemoglobinemia.')
facts(243,[
('Uric acid metabolism in humans is:','No uric acid metabolism in humans',['Present as uricase','Only in liver','Only in kidney'],'No uric acid metabolism in humans.'),
('Pegloticase is:','Rx of resistant gout: I/V x once every 2 wks',['DOC for tumor lysis high risk','Only oral','Only for chronic gout first line'],'Rx of resistant gout: I/V x once every 2 wks.'),
('Rasburicase is DOC for:','High risk of Tumor Lysis Syndrome (Leukemia: CLL)',['Resistant gout','Chronic gout','Only acute gout'],'DOC High risk of Tumor Lysis Syndrome (Leukemia: CLL).'),
('Uricase analogues S/E are:','Hemolysis in G-6-PD deficiency and methemoglobinemia',['Only hepatotoxicity','Only nephrotoxicity','Only rash'],'Hemolysis in G-6-PD deficiency, methemoglobinemia.'),
])
finish()

# CHAPTER 62 - RHEUMATOID ARTHRITIS (p244-246) -------------------------------
start(62)
unit('Acute Flare and Long Term Management Principles',
 'Mild to moderate acute flare of rheumatoid arthritis uses NSAIDs aspirin, diclofenac greater than celecoxib; severe flare uses steroids also if unresponsive to NSAIDs with involvement 1-2 joints intra-articular triamcinolone and more than 2 joints oral prednisolone. Long term management uses disease modifying anti rheumatoid drugs DMARDs divided into conventional DMARDs, biological DMARDs and JAK inhibitors; conventional includes methotrexate, hydroxychloroquine, sulfasalazine, leflunomide, cyclosporin, azathioprine, mycophenolate mofetil and cyclophosphamide; biological includes TNF alpha inhibitors, IL-1 inhibitors, IL-6 inhibitors, abatacept and CD-20 inhibitors; JAK inhibitors include tofacitinib, baricitinib and upadacitinib; all cause immunosuppression increasing infection risk and should not be combined.')
facts(244,[
('Mild-moderate acute flare of RA uses:','NSAIDs: Aspirin, Diclofenac > Celecoxib',['Only steroids','Only methotrexate','Only biologics'],'Mild - moderate: NSAIDs: Aspirin, Diclofenac > Celecoxib.'),
('Severe acute flare of RA uses:','Steroids: Also if unresponsive to NSAIDs',['Only NSAIDs','Only methotrexate','Only biologics'],'Severe: Steroids: Also if unresponsive to NSAIDS.'),
('If 1-2 joints involved in severe flare:','Intra-articular triamcinolone',['Oral prednisolone','Only NSAIDs','Only methotrexate'],'1-2 Joints: Intra-articular triamcinolone.'),
('If >2 joints involved:','Oral prednisolone',['Intra-articular triamcinolone','Only NSAIDs','Only methotrexate'],'>2 joints: Oral prednisolone.'),
('Disease modifying anti rheumatoid drugs (DMARDs) are:','Conventional DMARDs, Biological DMARDs, JAK inhibitors',['Only conventional','Only biological','Only JAK inhibitors'],'DMARDs: Conventional, Biological, JAK inhibitors.'),
('Conventional DMARDs include:','Methotrexate, Hydroxychloroquine, Sulfasalazine, Leflunomide, Cyclosporin, Azathioprine, Mycophenolate mofetil, Cyclophosphamide',['Only methotrexate','Only biologics','Only JAK inhibitors'],'Conventional DMARDs list.'),
('Biological DMARDs include:','TNF α inhibitors, IL-1 inhibitors, IL-6 inhibitors, Abatacept, CD-20 inhibitors',['Only TNF inhibitors','Only JAK inhibitors','Only conventional'],'Biological DMARDs TNF α, IL-1, IL-6, Abatacept, CD-20.'),
('JAK inhibitors include:','Tofacitinib, Baricitinib, Upadacitinib',['Only tofacitinib','Only methotrexate','Only rituximab'],'JAK inhibitors Tofacitinib Baricitinib Upadacitinib.'),
('DMARDs cause:','Immunosuppression -> ↑ Risk of infection -> Not to be combined',['No immunosuppression','Only hepatotoxicity','Only nephrotoxicity'],'Immunosuppression ↑ Risk of infection Not to be combined.'),
])
unit('Methotrexate and Treatment Algorithm',
 'Methotrexate is anchor drug and DOC for new diagnosis of RA with anti-inflammatory effect in 2-4 weeks. If inadequate response after 3-6 months add hydroxychloroquine plus sulfasalazine or abatacept or biological DMARDs; if inadequate response to biological DMARDs add other biological DMARDs or JAK inhibitors. Methotrexate inhibits DHFR decreasing THF decreasing purine synthesis causing lymphocyte toxicity and increases adenosine giving anti-inflammatory response but also hepatic fibrosis; side effects hepatotoxicity plus liver cirrhosis monitor ALT/AST every 3-6 months, nephrotoxicity causing crystalluria and bone marrow suppression; DHFR is dihydrofolate reductase and THF is tetrahydrofolate.')
facts(244,[
('Anchor drug for RA is:','Methotrexate',['Hydroxychloroquine','Sulfasalazine','Tofacitinib'],'Methotrexate (Anchor drug).'),
('DOC for new diagnosis of RA is:','Methotrexate',['Hydroxychloroquine','Sulfasalazine','Leflunomide'],'DOC for new Dx.'),
('Methotrexate anti-inflammatory effect in:','2-4 wks',['1-2 days','6-12 months','Only after 1 year'],'Anti-inflammatory effect: 2-4 wks.'),
('If inadequate response after 3-6 months to methotrexate:','Add Hydroxychloroquine + Sulfasalazine OR Abatacept OR Biological DMARDs',['Stop methotrexate','Only increase dose','Only add steroids'],'Inadequate response after 3-6 months: Add.'),
('If inadequate response to biological DMARDs:','Other biological DMARDs or JAK inhibitors',['Only stop biologics','Only add steroids','Only NSAIDs'],'Inadequate response Other biological DMARDs JAK inhibitors.'),
('Methotrexate inhibits:','DHFR: ↓ THF -> Purine synthesis -> Lymphocyte toxicity',['Only THF increase','Only purine increase','Only adenosine decrease'],'Inhibit DHFR: ↓ THF Purine synthesis Lymphocyte toxicity.'),
('Methotrexate increased adenosine causes:','Anti-inflammatory response',['Pro-inflammatory','No effect','Only fibrosis'],'Increased Adenosine: Anti-inflammatory response.'),
('Methotrexate also causes:','Hepatic fibrosis',['Only renal fibrosis','Only pulmonary fibrosis','Only cardiac fibrosis'],'Hepatic fibrosis.'),
('Methotrexate hepatotoxicity + liver cirrhosis monitor:','ALT/AST every 3-6 months',['Only ALT once','Only AST once','No monitoring needed'],'Monitor: ALT/AST every 3-6 months.'),
('Methotrexate nephrotoxicity causes:','Crystalluria',['Only hematuria','Only proteinuria','Only stones'],'Nephrotoxicity -> Crystalluria.'),
('Methotrexate also causes:','Bone marrow suppression',['Only hepatotoxicity','Only nephrotoxicity','Only rash'],'Bone marrow suppression.'),
('DHFR stands for:','Dihydrofolate reductase',['Dihydrofolate receptor','Dehydrofolate reductase','Dihydrofolate resistant'],'DHFR: Dihydrofolate reductase.'),
('THF stands for:','Tetrahydrofolate',['Trihydrofolate','Tetrahydrofolic acid receptor','Thymidine hydrofolate'],'THF: Tetrahydrofolate.'),
])
unit('Conventional DMARDs: Hydroxychloroquine and Sulfasalazine',
 'Hydroxychloroquine inhibits lymphocyte proliferation and stabilizes lysosomes; use mild monotherapy and moderate-severe as add on; side effect Bull eye retinopathy/maculopathy with max dose ≤5 mg/kg/day requiring ophthalmological exam once yearly. Sulfasalazine in gut metabolized to 5 aminosalicylic acid which is not absorbed used for ulcerative colitis and sulfonamide which inhibits lymphocyte proliferation used as monotherapy for mild RA and add on for moderate-severe RA.')
facts(245,[
('Hydroxychloroquine MOA is:','Inhibit lymphocyte proliferation and stabilizes lysosomes',['Only DHFR inhibition','Only adenosine increase','Only purine synthesis'],'Inhibit lymphocyte proliferation, Stabilizes lysosomes.'),
('Hydroxychloroquine use mild:','Monotherapy',['Only add on','Only with biologics','Only with JAK inhibitors'],'Mild: monotherapy.'),
('Hydroxychloroquine moderate-severe:','Add on',['Monotherapy','No use','Only biologics'],'Moderate - Severe: Add on.'),
('Hydroxychloroquine S/E is:','Bull eye retinopathy/maculopathy',['Only hepatotoxicity','Only nephrotoxicity','Only bone marrow suppression'],'Bull eye retinopathy/maculopathy.'),
('Max dose of hydroxychloroquine to avoid retinopathy:','≤5 mg/kg/day',['≤10 mg/kg/day','≤2 mg/kg/day','≤15 mg/kg/day'],'Max dose: ≤5 mg/kg/day.'),
('Ophthalmological exam for hydroxychloroquine:','Once yearly',['Every 3-6 months','Only at start','Never needed'],'Ophthalmological exam once yearly.'),
('Sulfasalazine metabolism in gut:','5 Aminosalicylic acid and Sulfonamide',['Only 5 ASA','Only sulfonamide','Only sulfapyridine'],'In gut 5 Aminosalicylic acid Sulfonamide.'),
('5 Aminosalicylic acid is:','Not absorbed',['Absorbed fully','Only renal excretion','Only hepatic'],'Not absorbed.'),
('5 ASA use is:','Ulcerative colitis',['Only RA','Only Crohn only','Only for fever'],'Ulcerative colitis.'),
('Sulfonamide MOA is:','Inhibits lymphocyte proliferation',['Not absorbed only','Only 5 ASA effect','Only antibacterial'],'Inhibits lymphocyte proliferation.'),
('Sulfonamide monotherapy for:','Mild RA',['Moderate-severe only','Only ulcerative colitis','Only as add on'],'Monotherapy: mild RA.'),
('Sulfonamide add on for:','Moderate - Severe RA',['Mild only','Only ulcerative colitis','No use in RA'],'Add on: moderate - Severe RA.'),
])
unit('Biological DMARDs and Side Effects',
 'TNF alpha inhibitors are infliximab, adalimumab, certolizumab, etanercept and golimumab given IV or SC with uses mnemonic Alpha Inhibitors Prevent RA including ankylosing spondylitis, inflammatory bowel disease, psoriatic arthritis, plaque psoriasis and rheumatoid arthritis. Side effects are GIT ulcers leading to perforation, increased risk of infection and increased risk of secondary skin cancers; contraindicated in hepatitis B reactivation risk and congestive heart failure. IL-6 inhibitors tocilizumab and sarilumab used for RA and cytokine storm in COVID-19; IL-1 inhibitor anakinra is least effective and least preferred biological; CD-20 inhibitors rituximab anticancer drug, abatacept inhibits CD 80/86 inhibiting T cell activation and belatacept related to abatacept used for graft versus host disease.')
facts(245,[
('TNF α inhibitors are:','Infliximab, Adalimumab, Certolizumab, Etanercept, Golimumab',['Only infliximab','Only etanercept','Only adalimumab'],'Drugs: Infliximab, Adalimumab, Certolizumab, Etanercept, Golimumab.'),
('TNF α inhibitors route is:','I/V and S/C',['Only oral','Only IV','Only SC'],'I/V S/C.'),
('TNF α inhibitors uses mnemonic:','Alpha Inhibitors Prevent RA',['Only RA','Only IBD','Only psoriasis'],'Mnemonic: Alpha Inhibitors Prevent RA.'),
('TNF α inhibitors uses include:','Ankylosing spondylitis, Inflammatory bowel disease, Psoriatic arthritis, Plaque psoriasis, Rheumatoid Arthritis',['Only RA','Only ankylosing','Only IBD'],'Ankylosing spondylitis, Inflammatory bowel disease, Psoriatic arthritis, Plaque psoriasis, Rheumatoid Arthritis.'),
('TNF α inhibitors S/E include:','GIT ulcers -> Perforation, ↑ Risk of infection, ↑ Risk of secondary skin cancers',['Only GIT ulcers','Only infection','Only skin cancers'],'S/E: GIT ulcers -> Perforation, ↑ Risk of infection, ↑ Risk of secondary skin cancers.'),
('TNF α inhibitors C/I include:','Hepatitis B: Reactivation risk and Congestive heart failure',['Only hepatitis B','Only CHF','Only renal failure'],'C/I: Hepatitis B: Reactivation risk, Congestive heart failure.'),
('IL-6 inhibitors are:','Tocilizumab & Sarilumab',['Anakinra only','Rituximab only','Abatacept only'],'Tocilizumab & Sarilumab.'),
('IL-6 inhibitors uses are:','RA and Cytokine storm in COVID-19',['Only RA','Only COVID cytokine storm','Only IBD'],'Uses: RA, Cytokine storm in COVID-19.'),
('IL-1 inhibitor is:','Anakinra: Least effective & Least preferred biological',['Tocilizumab','Rituximab','Abatacept'],'Anakinra: Least effective & Least preferred biological.'),
('CD-20 inhibitors include:','Rituximab, Abatacept, Belatacept',['Only rituximab','Only abatacept','Only belatacept'],'CD-20 inhibitors: Rituximab, Abatacept, Belatacept.'),
('Rituximab is:','Anticancer drug',['Only for RA','Only for GVHD','Only for IBD'],'Rituximab: Anticancer drug.'),
('Abatacept MOA is:','Inhibit CD 80/86 -> Inhibit T cell activation',['Only B cell depletion','Only IL-6 inhibition','Only TNF inhibition'],'Inhibit CD 80/86 -> Inhibit T cell activation.'),
('Belatacept is:','Related to Abatacept, Use: Graft v/s host disease',['Only for RA','Only anticancer','Only for IBD'],'Related to Abatacept, Use: Graft v/s host disease.'),
])
unit('JAK Inhibitors',
 'Janus kinase JAK inhibitors mechanism is inhibition of cytokine function. Drugs: baricitinib for RA, upadacitinib for RA, psoriatic arthritis and atopic dermatitis, ruxolitinib for GVHD, myelofibrosis and polycythemia vera unresponsive to hydroxyurea, abrocitinib for atopic dermatitis and tofacitinib for psoriatic arthritis, ulcerative colitis, juvenile idiopathic arthritis, ankylosing spondylitis and rheumatoid arthritis.')
facts(246,[
('JAK inhibitors MOA is:','(-) Function of cytokines',['(+) Cytokines','Only IL-6','Only TNF'],'MOA: (-) function of cytokines.'),
('Baricitinib used for:','RA',['Atopic dermatitis only','Psoriatic arthritis only','Only GVHD'],'Baricitinib: RA.'),
('Upadacitinib used for:','RA, Psoriatic arthritis, Atopic dermatitis',['Only RA','Only atopic','Only GVHD'],'Upadacitinib: RA, Psoriatic arthritis, Atopic dermatitis.'),
('Ruxolitinib used for:','GVHD, Myelofibrosis, Polycythemia vera (unresponsive to hydroxyurea)',['Only RA','Only atopic dermatitis','Only psoriatic arthritis'],'Ruxolitinib: GVHD, Myelofibrosis, Polycythemia vera (unresponsive to hydroxyurea).'),
('Abrocitinib used for:','Atopic dermatitis',['Only RA','Only GVHD','Only myelofibrosis'],'Abrocitinib: Atopic dermatitis.'),
('Tofacitinib used for:','Psoriatic arthritis, Ulcerative colitis, Juvenile idiopathic arthritis, Ankylosing spondylitis, Rheumatoid arthritis',['Only RA','Only atopic dermatitis','Only GVHD'],'Tofacitinib: Psoriatic arthritis, Ulcerative colitis, Juvenile idiopathic arthritis, Ankylosing spondylitis, Rheumatoid arthritis.'),
])
finish()

# CHAPTER 63 - ANTI-AGGREGANTS AND HEMATOPOIETIC AGENTS (p247-250) ------------
start(63)
unit('Physiology of Platelet Aggregation and Aspirin',
 'Blood vessel injury releases collagen and vWF activating platelets. Platelet activation pathways: GP IIb/IIIa blocked by abciximab, COX-1 blocked by aspirin producing thromboxane A2 leading to aggregation, ADP acting on P2Y12 blocked by clopidogrel, increased phospholipids increasing thrombin production forming fibrin from fibrinogen forming mesh and permanent clot, and protease activated receptor PAR blocked by vorapaxar. Aspirin irreversibly inhibits COX-1 decreasing thromboxane A2 at 50-325 mg OD used for secondary prophylaxis of acute coronary syndrome and ischemic stroke, treatment of ACS, essential thrombocythemia, Kawasaki disease and antiphospholipid antibody syndrome; side effect bleeding with pre-op continue aspirin and stop clopidogrel 7 days pre-op.')
facts(247,[
('Blood vessel injury releases:','Collagen, vWF (+) Platelet',['Only collagen','Only vWF','Only thrombin'],'Blood vessel injury Release Collagen, vWF (+) Platelet.'),
('GP IIb/IIIa is blocked by:','Abciximab',['Aspirin','Clopidogrel','Vorapaxar'],'(+) X Abciximab GP IIb/IIIa.'),
('COX-1 is blocked by:','Aspirin',['Abciximab','Clopidogrel','Vorapaxar'],'(+) X Aspirin COX-1.'),
('COX-1 produces:','Thromboxane A2 -> Platelet Aggregation',['Only ADP','Only phospholipids','Only fibrin'],'COX-1 (+) Thromboxane A2.'),
('ADP acts on:','P2Y12 receptor blocked by Clopidogrel',['GP IIb/IIIa','COX-1','PAR'],'ADP (+) P2Y12 X Clopidogrel.'),
('Increased phospholipids increase:','Thrombin production -> Fibrinogen -> Fibrin mesh -> Permanent clot',['Only collagen','Only vWF','Only ADP'],'↑ Phospholipids ↑ Production Thrombin Fibrinogen -> Fibrin mesh formation Permanent clot.'),
('PAR is blocked by:','Vorapaxar',['Aspirin','Clopidogrel','Abciximab'],'Vorapaxar X PAR Platelet Aggregation.'),
('Aspirin mechanism is:','Irreversible (-) COX-1 -> ↓ Thromboxane A2',['Reversible COX-1','Only COX-2','Only LOX'],'Aspirin Irreversible (-) COX-1 -> ↓ Thromboxane A2.'),
('Aspirin dose for antiplatelet is:','50-325 mg OD',['325-650 mg SOS','3-4 g/day','>10 g'],'50-325 mg OD.'),
('Aspirin use 2° prophylaxis:','Acute coronary syndrome (ACS) and Ischemic stroke',['Only ACS','Only stroke','Only Kawasaki'],'2° prophylaxis Acute coronary syndrome (ACS), Ischemic stroke.'),
('Aspirin Rx of ACS:','Used for Rx of ACS',['Only prophylaxis','Not used','Only for Kawasaki'],'Rx of ACS.'),
('Aspirin other uses:','Essential Thrombocythemia, Kawasaki disease, Antiphospholipid antibody syndrome',['Only essential thrombocythemia','Only Kawasaki','Only antiphospholipid'],'Essential Thrombocythemia, Kawasaki disease, Antiphospholipid antibody syndrome.'),
('Aspirin S/E is:','Bleeding',['Only thrombosis','Only hypertension','Only rash'],'Bleeding.'),
('Pre-op with aspirin and clopidogrel:','Continue aspirin, Stop clopidogrel x 7 days pre-op',['Stop both','Continue both','Stop aspirin only'],'Pre-op: Continue aspirin, Stop clopidogrel x 7 days pre-op.'),
])
unit('ADP/P2Y12 Inhibitors: Classification and Hit and Run Concept',
 'ADP/P2Y12 inhibitors classification: irreversible clopidogrel, ticlopidine and prasugrel; reversible competitive cangrelor adenosine analog short acting T1/2 3-6 min IV used for PCI in MI; non-competitive ticagrelor long acting oral used for PCI in MI, Rx of ACS and secondary prophylaxis of MI. Note hit and run drugs irreversible ADP/P2Y12 inhibitors, aspirin and PPIs bind irreversibly to target increasing T1/2 period.')
facts(248,[
('Irreversible ADP/P2Y12 inhibitors are:','Clopidogrel, Ticlopidine, Prasugrel',['Cangrelor and ticagrelor','Only clopidogrel','Only prasugrel'],'Irreversible Clopidogrel Ticlopidine Prasugrel.'),
('Reversible competitive ADP inhibitor is:','Cangrelor',['Ticagrelor','Clopidogrel','Prasugrel'],'Competitive Cangrelor.'),
('Cangrelor is:','Adenosine analog, T1/2 3-6 min (Short acting), Route I/V, Use PCI in MI',['Long acting oral','Only for stroke','Only for ACS'],'Adenosine analog T1/2 3-6 min (Short acting) Route I/V Use PCI in MI.'),
('Reversible non-competitive ADP inhibitor is:','Ticagrelor',['Cangrelor','Clopidogrel','Ticlopidine'],'Non-competitive Ticagrelor.'),
('Ticagrelor is:','Long acting, Route Oral, Use PCI in MI, Rx of ACS, 2° prophylaxis of MI',['Short acting IV only','Only for stroke prophylaxis','Only for PCI in MI only'],'Long acting Route Oral Use PCI in MI Rx of ACS 2° prophylaxis of MI.'),
('Hit & run drugs are:','Irreversible ADP(-)/P2Y12 (-), Aspirin, PPIs: Bind irreversibly to target -> ↑ T1/2 period',['Only reversible drugs','Only aspirin','Only PPIs'],'Hit & run drugs: Irreversible ADP(-)/P2Y12 (-), Aspirin, PPIs Bind irreversibly to target -> ↑ T1/2 period.'),
])
unit('Clopidogrel, Ticlopidine and Prasugrel',
 'Clopidogrel is prodrug activated by CYP2C19; CYP2C19 polymorphisms blunt clopidogrel decreasing effect worsening MI and it metabolizes omeprazole causing competitive inhibition of clopidogrel; use same as aspirin and combined with aspirin for patient on stent. Ticlopidine has increased toxicity GI nausea/vomiting/diarrhea, agranulocytosis and TTP-HUS complex; use secondary stroke prophylaxis in resistant cases. Prasugrel is most potent and fastest acting with increased risk of intracranial bleed contraindicated in history of stroke/TIA, used for PCI in MI.')
facts(248,[
('Clopidogrel is:','Prodrug CYP2C19 Activated',['Active drug itself','Only CYP3A4 activated','Only renal excretion'],'Prodrug CYP2C19 Activated.'),
('CYP2C19 polymorphisms cause:','Blunted clopidogrel -> ↓Effect -> Worsen MI',['Increased effect','No effect','Only increased bleeding'],'Polymorphisms -> Blunted clopidogrel -> ↓Effect -> Worsen MI.'),
('Omeprazole interaction with clopidogrel:','Competitive (-) of clopidogrel because CYP2C19 metabolizes omeprazole',['Increases clopidogrel effect','No interaction','Only decreases omeprazole effect'],'Metabolizes Omeprazole -> Competitive (-) of clopidogrel.'),
('Clopidogrel use is:','Same as aspirin and combined with aspirin for patient on stent',['Only same as aspirin','Only for stent','Only for stroke'],'Same as aspirin, Combined with aspirin for patient on stent.'),
('Ticlopidine toxicity includes:','GI: Nausea/Vomiting/Diarrhea, Agranulocytosis, TTP-HUS complex',['Only GI','Only agranulocytosis','Only TTP-HUS'],'↑↑ Toxicity GI Nausea/Vomiting/Diarrhea Agranulocytosis TTP-HUS complex.'),
('Ticlopidine use is:','2° stroke prophylaxis in resistant cases',['Only PCI in MI','Only ACS','Only first line stroke'],'2° stroke prophylaxis in resistant cases.'),
('Prasugrel is:','Most potent + Fastest acting',['Least potent','Slowest acting','Only moderate potency'],'Most potent + Fastest acting.'),
('Prasugrel risk is:','↑ Risk of Intracranial bleed',['Only GI bleed','Only rash','Only thrombosis'],'↑ Risk of Intracranial bleed.'),
('Prasugrel C/I is:','H/o stroke, TIA',['Only renal failure','Only liver failure','Only age >65'],'C/I: h/o stroke, TIA.'),
('Prasugrel use is:','PCI in MI',['Only stroke prophylaxis','Only ACS','Only stable angina'],'Use: PCI in MI.'),
])
unit('Vorapaxar and GP IIb/IIIa Inhibitors',
 'Vorapaxar mechanism is PAR negative; use secondary prophylaxis MI and unstable angina as single agent or combined with aspirin/clopidogrel; side effect increased risk of intracranial bleed contraindicated in stroke/TIA. Glycoprotein IIb/IIIa inhibitor mechanism abciximab blocks GPIIb/IIIa and vitronectin with shortest T1/2 maximum affinity longest acting and eptifibatide longest T1/2 minimum affinity shortest acting; uses PCI in MI and ACS; route IV/intra-coronary; other drug tirofiban.')
facts(249,[
('Vorapaxar mechanism is:','PAR (-)',['COX-1 (-)','P2Y12 (-)','GP IIb/IIIa (-)'],'PAR (-).'),
('Vorapaxar use is:','2° prophylaxis MI and Unstable angina',['Only MI','Only unstable angina','Only stroke'],'2° prophylaxis MI, Unstable angina.'),
('Vorapaxar can be:','Single agent/Combined: Aspirin/Clopidogrel',['Only single agent','Only with heparin','Only with warfarin'],'Single agent/Combined: Aspirin/Clopidogrel.'),
('Vorapaxar S/E is:','Increased risk of intracranial bleed -> C/I in Stroke/TIA',['Only GI bleed','Only rash','Only thrombocytopenia'],'↑ Risk of intracranial bleed -> C/I in Stroke/TIA.'),
('Glycoprotein IIb/IIIa inhibitor abciximab:','Blocks GPIIb/IIIa and vitronectin',['Only blocks GPIIb/IIIa','Only blocks vitronectin','Only blocks COX-1'],'Abciximab Blocks GPIIb/IIIa Vitronectin.'),
('Abciximab pharmacokinetics:','Shortest T1/2, maximum affinity -> Longest acting',['Longest T1/2 minimum affinity -> Shortest acting','Only short acting','Only long acting'],'Shortest T1/2, maximum affinity -> Longest acting.'),
('Eptifibatide pharmacokinetics:','Longest T1/2 + minimum affinity -> Shortest acting',['Shortest T1/2 max affinity -> Longest acting','Only long acting','Only intermediate'],'Longest T1/2 + minimum affinity -> Shortest acting.'),
('GP IIb/IIIa inhibitors uses are:','PCI in MI and ACS',['Only PCI in MI','Only ACS','Only stroke'],'Uses: PCI in MI, ACS.'),
('GP IIb/IIIa inhibitors route is:','IV/Intra-coronary',['Only oral','Only SC','Only IM'],'Route: IV/Intra-coronary.'),
('Other GP IIb/IIIa drug is:','Tirofiban',['Only abciximab','Only eptifibatide','Only vorapaxar'],'Other Drugs: Tirofiban.'),
])
unit('Hematopoietic Agents: Erythropoiesis and Granulopoiesis',
 'Drugs acting on erythropoiesis are erythropoietin EPO analogs epoetin alpha and darbepoetin longer acting clinically preferred used DOC for anemia due to CRF, dialysis, zidovudine/anticancer drugs and premature infants with side effects HTN, iron deficiency, thrombosis, pure red cell aplasia and flu like symptoms; EPO receptor agonist peginesatide for anemia of CKD CRF. Drugs acting on granulopoiesis G-CSF analog granulocyte colony stimulating factor more potent less toxic lenograstim and filgrastim most commonly used multiple dose SC or IV with derivatives lipegfilgrastin and pegfilgrastim long acting single dose in a chemotherapy cycle; uses neutropenia due to myelodysplasia, aplastic anemia, HIV and chemotherapy with side effect bone pain; GM-CSF analog granulocyte macrophage CSF less potent more toxic sargramostim with side effect capillary leak syndrome.')
facts(249,[
('EPO analogs are:','Epoetin alpha and Darbepoetin',['Only epoetin alpha','Only darbepoetin','Only peginesatide'],'Erythropoietin (EPO) analogs Epoetin alpha Darbepoetin.'),
('Darbepoetin is:','Longer acting (Clinically preferred)',['Shorter acting','Same as epoetin','Only for dialysis'],'Longer acting (Clinically preferred).'),
('EPO analogs DOC for anemia due to:','CRF, Dialysis, Zidovudine/Anticancer drugs, Premature infants',['Only CRF','Only dialysis','Only zidovudine'],'DOC: Anemia d/t CRF, Dialysis, Zidovudine/Anticancer drugs, Premature infants.'),
('EPO analogs S/E are:','HTN, Iron deficiency, Thrombosis, Pure red cell aplasia, Flu like symptoms',['Only HTN','Only thrombosis','Only flu like symptoms'],'S/E: HTN, Iron deficiency, Thrombosis, Pure red cell aplasia, Flu like symptoms.'),
('EPO Receptor Agonist is:','Peginesatide: Anemia of CKD (CRF)',['Epoetin alpha','Darbepoetin','Only filgrastim'],'EPO Receptor Agonists Peginesatide: Anemia of CKD (CRF).'),
('G-CSF analog is:','Granulocyte Colony Stimulating Factor, ↑ Potent, ↓ Toxic',['GM-CSF','Only toxic','Only less potent'],'G-CSF analog (Granulocyte Colony Stimulating Factor) ↑ Potent, ↓ Toxic.'),
('G-CSF analog drugs are:','Lenograstim and Filgrastim (m/c used)',['Only lenograstim','Only filgrastim','Only sargramostim'],'Drugs: Lenograstim, Filgrastim: m/c used.'),
('G-CSF route is:','Multiple dose s/c or I/V',['Only oral','Only IV single dose','Only SC single dose'],'Route: multiple dose s/c or I/V.'),
('G-CSF derivatives are:','Lipegfilgrastin and Pegfilgrastim',['Only lipegfilgrastin','Only pegfilgrastim','Only filgrastim'],'Derivatives Lipegfilgrastin Pegfilgrastim.'),
('G-CSF derivatives property is:','Long acting, Single dose in a chemotherapy cycle',['Short acting multiple dose','Only for HIV','Only for aplastic anemia'],'Long acting, Single dose in a chemotherapy cycle.'),
('G-CSF uses neutropenia d/t:','Myelodysplasia, Aplastic anemia, HIV, Chemotherapy',['Only chemotherapy','Only HIV','Only aplastic anemia'],'Neutropenia d/t myelodysplasia, Aplastic anemia, HIV, Chemotherapy.'),
('G-CSF S/E is:','Bone pain',['Capillary leak','Only fever','Only rash'],'Bone pain.'),
('GM-CSF analog is:','G macrophage-CSF, ↓ Potent, ↑ Toxic, Sargramostim',['G-CSF','Only more potent','Only less toxic'],'GM-CSF Analog (G macrophage -CSF) ↓ Potent, ↑ Toxic.'),
('Sargramostim S/E is:','Capillary leak syndrome',['Bone pain','Only fever','Only rash'],'S/E: Capillary leak syndrome.'),
])
unit('Drugs Acting on Thrombopoiesis',
 'Thrombopoietin agonists are romiplostim and eltrombopag used for ITP immune thrombocytopenic purpura with side effects portal vein thrombosis and acute myeloid leukemia; new drugs avatrombopag and lusutrombopag prevent procedural bleeding in liver cirrhosis. IL-11 analog oprelvekin used for chemotherapy induced thrombocytopenia with side effect fluid retention causing congestive heart failure and edema.')
facts(250,[
('Thrombopoietin agonist drugs are:','Romiplostim and Eltrombopag',['Only romiplostim','Only eltrombopag','Only oprelvekin'],'Drugs Romiplostim, Eltrombopag.'),
('Thrombopoietin agonist use is:','ITP (Immune Thrombocytopenic Purpura)',['Only chemotherapy thrombocytopenia','Only aplastic anemia','Only HIV'],'Use: ITP (Immune Thrombocytopenic Purpura).'),
('Thrombopoietin agonist S/E are:','Portal vein thrombosis and Acute myeloid leukemia',['Only portal vein thrombosis','Only AML','Only bleeding'],'S/E Portal vein thrombosis, Acute myeloid leukemia.'),
('New thrombopoietin drugs are:','Avatrombopag and Lusutrombopag',['Only avatrombopag','Only lusutrombopag','Only romiplostim'],'New drugs Avatrombopag, Lusutrombopag.'),
('Avatrombopag/lusutrombopag use is:','Prevent procedural bleeding in liver cirrhosis',['Only ITP','Only chemotherapy','Only aplastic anemia'],'Prevent procedural bleeding in liver cirrhosis.'),
('IL-11 analog is:','Oprelvekin',['Romiplostim','Eltrombopag','Filgrastim'],'IL-11 analog: Oprelvekin.'),
('Oprelvekin use is:','Chemotherapy induced thrombocytopenia',['Only ITP','Only aplastic anemia','Only HIV'],'Use: Chemotherapy induced thrombocytopenia.'),
('Oprelvekin S/E is:','Fluid retention -> Congestive Heart and Edema',['Only bone pain','Only capillary leak','Only fever'],'S/E: Fluid retention -> Congestive Heart, Edema.'),
])
finish()

# CHAPTER 64 - ANTICOAGULANTS AND FIBRINOLYTICS (p251-255) -------------------
start(64)
unit('Physiology of Coagulation and Anticoagulation',
 'Coagulation: X to Xa blocked by oral Xa inhibitors, prothrombin II to thrombin IIa blocked by direct thrombin inhibitors, fibrinogen to fibrin. Anticoagulation: protein C and S and antithrombin III protease which breaks down IIa, Xa, XIa and XIIa and is stimulated by indirect thrombin inhibitors heparins.')
facts(251,[
('Oral Xa Inhibitors block:','Xa',['IIa only','Fibrinogen only','Only XIa'],'X -> Xa X Oral Xa Inhibitors.'),
('Direct Thrombin Inhibitors block:','Thrombin (IIa)',['Xa only','Fibrinogen only','Only XIa'],'Thrombin (IIa) X Direct Thrombin Inhibitors.'),
('Prothrombin is:','II',['IIa','Xa','Fibrinogen'],'Prothrombin (II).'),
('Thrombin is:','IIa',['II','Xa','XIIa'],'Thrombin (IIa).'),
('Fibrinogen converts to:','Fibrin',['Thrombin','Prothrombin','Xa'],'Fibrinogen -> Fibrin.'),
('Anticoagulation proteins are:','Protein C & S and Antithrombin III (Protease)',['Only protein C','Only protein S','Only antithrombin III'],'Protein C & S Antithrombin III (Protease).'),
('Antithrombin III breaks down:','IIa, Xa, XIa, XIIa',['Only IIa','Only Xa','Only IIa and Xa'],'Breaks down IIa Xa XIa XIIa.'),
('Indirect Thrombin Inhibitors stimulate:','Antithrombin III (+)',['Protein C','Protein S only','Only factor X'],'(+) Indirect Thrombin Inhibitors.'),
])
unit('Direct Acting Anticoagulants: DOAC/NOAC',
 'Direct thrombin inhibitor oral is dabigatran; oral Xa inhibitors are apixaban, edoxaban and rivaroxaban; together they are DOAC/Novel OAC direct acting oral anticoagulants which do not require coagulation monitoring and are used for treatment of DVT and DOC for prophylaxis of DVT and prophylaxis of thrombosis in non-valvular atrial fibrillation AF. Parenteral direct thrombin inhibitors uses heparin induced thrombocytopenia with DOC argatroban requiring aPTT monitoring and hirudin derivatives semisynthetic lepirudin production stopped and desirudin SC in DVT prophylaxis pre-op and synthetic bivalirudin and argatroban used for PCI in MI contraindicated in renal failure except argatroban due to hepatic excretion; other drugs not requiring monitoring are LMWH and fondaparinux. Side effect bleeding with antidotes dabigatran idarucizumab and oral Xa inhibitors andexanet alfa decoy.')
facts(251,[
('Oral direct thrombin inhibitor is:','Dabigatran',['Apixaban','Rivaroxaban','Edoxaban'],'Oral: Dabigatran.'),
('Oral Xa inhibitors are:','Apixaban, Edoxaban, Rivaroxaban',['Only apixaban','Only rivaroxaban','Only dabigatran'],'Oral Xa inhibitors: Apixaban Edoxaban Rivaroxaban.'),
('DOAC / NOAC stands for:','Direct acting oral anticoagulants/Novel OAC',['Only direct oral','Only novel oral','Only direct acting'],'DOAC / NOAC Direct acting oral anticoagulants/Novel OAC.'),
('DOACs require coagulation monitoring:','Do not require coagulation monitoring',['Require aPTT','Require PT/INR','Require anti-Xa always'],'Do not require coagulation monitoring.'),
('DOAC uses include:','Rx of DVT and Prophylaxis of DVT and Prophylaxis of thrombosis in non-valvular atrial fibrillation (AF)',['Only DVT treatment','Only AF prophylaxis','Only valvular AF'],'Rx of DVT, DOC: Prophylaxis of DVT and Prophylaxis of thrombosis in non-valvular AF.'),
('DOC for prophylaxis of DVT and thrombosis in non-valvular AF is:','DOAC',['Warfarin','Heparin','Aspirin'],'DOC: Prophylaxis of DVT and Prophylaxis of thrombosis in non-valvular AF.'),
('Parenteral direct thrombin inhibitors uses:','Heparin induced thrombocytopenia, DOC: Argatroban',['Only DVT prophylaxis','Only PCI in MI','Only valvular AF'],'Uses: Heparin induced thrombocytopenia DOC: Argatroban.'),
('Argatroban monitoring is:','aPTT monitoring required',['PT/INR','No monitoring','Only anti-Xa'],'aPTT monitoring required.'),
('Hirudin derivatives semisynthetic drugs are:','Lepirudin: Production stopped, Desirudin: S/c in DVT prophylaxis pre-op',['Only lepirudin','Only desirudin','Only bivalirudin'],'Semisynthetic: Lepirudin: Production stopped, Desirudin: S/c in DVT prophylaxis pre-op.'),
('Synthetic hirudin derivatives are:','Bivalirudin and Argatroban',['Only bivalirudin','Only argatroban','Only lepirudin'],'Synthetic: Bivalirudin, Argatroban.'),
('Argatroban used for:','PCI in MI',['Only HIT','Only DVT prophylaxis','Only valvular AF'],'Used for PCI in MI.'),
('Direct thrombin inhibitors C/I in:','Renal failure except Argatroban (D/t hepatic excretion)',['No C/I','Only liver failure','Only renal failure for all'],'C/I: Renal failure Exception: Argatroban (D/t hepatic excretion).'),
('Other drugs not requiring monitoring are:','LMWH and Fondaparinux',['Only LMWH','Only fondaparinux','Only UFH'],'Other drugs not requiring monitoring LMWH Fondaparinux.'),
('Side effect of direct acting anticoagulants is:','Bleeding',['Thrombosis only','Only rash','Only fever'],'Side effects: Bleeding.'),
('Antidote for dabigatran is:','Idarucizumab',['Andexanet alfa','Protamine sulfate','Vitamin K'],'Dabigatran: Idarucizumab.'),
('Antidote for oral Xa inhibitors is:','Andexanet alfa (Decoy)',['Idarucizumab','Protamine','Vitamin K'],'Oral Xa inhibitors: Andexanet alfa (Decoy).'),
])
unit('Indirect Thrombin Inhibitors: UFH, LMWH and Fondaparinux Structure',
 'Unfractionated heparin UFH is glycosaminoglycans from mast cells sourced from MALT of porcine intestinal mucosa. Structure and mechanism: active pentasaccharide AP attached to long chain heteropolysaccharide binds antithrombin III breaking down Xa and long chain HPS binds IIa breaking down IIa. Comparison table: UFH structure AP plus long chain HPS activity against Xa equal IIa bioavailability poor route prophylaxis SC BD and treatment IV QID metabolism reticuloendothelial system in renal failure DOC short acting monitoring aPTT antidote protamine sulfate effective neutralizes HPS risk of HIT double up arrow; LMWH enoxaparin/tinzaparin structure AP plus short chain HPS activity against Xa greater than IIa bioavailability increased route prophylaxis and treatment SC OD metabolism excreted unchanged by kidneys contraindicated in renal failure long acting monitoring only in renal failure obese elderly children by anti-Xa assay antidote less effective risk of HIT single up arrow; fondaparinux structure AP only activity only against Xa bioavailability maximum monitoring not required antidote not effective risk of HIT none.')
facts(252,[
('UFH is:','Glycosaminoglycans: mast cells',['Only protein C','Only protein S','Only Xa inhibitor'],'Glycosaminoglycans: mast cells.'),
('Source of UFH is:','MALT of porcine intestinal mucosa',['Bovine lung only','Human plasma','Synthetic only'],'Source: MALT of porcine intestinal mucosa.'),
('Active pentasaccharide (AP) attached to:','Long chain heteropolysaccharide',['Short chain only','Only AP','No chain'],'Active pentasaccharide (AP) Attached to Long chain heteropolysaccharide.'),
('AP binds to:','Antithrombin III -> Breaks down Xa',['Only IIa','Only fibrinogen','Only protein C'],'Binds to Antithrombin III Breaks down Xa.'),
('Long chain HPS binds to:','IIa -> IIa broken down',['Only Xa','Only XIa','Only fibrinogen'],'Binds to IIa II a broken down.'),
('UFH structure is:','AP + Long chain HPS',['AP + Short chain HPS','AP only','Only long chain HPS'],'UFH Structure AP + Long chain HPS.'),
('LMWH structure is:','AP + Short chain HPS',['AP + Long chain HPS','AP only','Only short chain'],'LMWH AP + Short chain HPS.'),
('Fondaparinux structure is:','AP only',['AP + Long chain HPS','AP + Short chain HPS','Only HPS'],'Fondaparinux AP only.'),
('UFH activity is:','Against Xa = IIa',['Against Xa > IIa','Only against Xa','Only against IIa'],'Against Xa = IIa.'),
('LMWH activity is:','Against Xa > IIa',['Against Xa = IIa','Only against Xa','Only against IIa'],'Against Xa > IIa.'),
('Fondaparinux activity is:','Only against Xa',['Against Xa = IIa','Against Xa > IIa','Only against IIa'],'Only against Xa.'),
('UFH bioavailability is:','Poor',['Maximum','Increased','Moderate'],'Bioavailability Poor.'),
('LMWH bioavailability is:','Increased',['Poor','Maximum','Same as UFH'],'Bioavailability ↑.'),
('Fondaparinux bioavailability is:','Maximum',['Poor','Increased','Low'],'Maximum.'),
('UFH route and dose:','Prophylaxis: S/C; BD and Rx: I/V; QID',['Only SC OD','Only IV OD','Only SC BD'],'Prophylaxis: S/C; BD Rx: I/V; QID.'),
('LMWH route and dose:','Prophylaxis and Rx S/C; OD',['Prophylaxis S/C BD','Only IV QID','Only oral'],'Prophylaxis Rx S/C; OD.'),
('UFH metabolism is:','Reticuloendothelial system',['Excreted unchanged by kidneys','Only hepatic','Only renal'],'Reticuloendothelial system.'),
('LMWH/Fondaparinux metabolism is:','Excreted unchanged by Kidneys',['Reticuloendothelial','Only hepatic','Only biliary'],'Excreted unchanged by Kidneys.'),
('In renal failure DOC is:','UFH',['LMWH','Fondaparinux','All are safe'],'In renal failure DOC.'),
('LMWH/Fondaparinux in renal failure:','Contraindicated',['DOC','Safe','No contraindication'],'Contraindicated.'),
('UFH duration is:','Short acting',['Long acting','Intermediate','Very long'],'Short acting.'),
('LMWH duration is:','Long acting',['Short acting','Intermediate','Very short'],'Long acting.'),
('UFH monitoring is:','aPTT',['PT/INR','Anti Xa assay only','Not required'],'Monitoring aPTT.'),
('LMWH monitoring:','Only in: Renal failure, obese, elderly, children By: Anti Xa assay',['Always aPTT','No monitoring ever','Only PT/INR'],'Only in: Renal failure, obese, elderly, children By: Anti Xa assay.'),
('Fondaparinux monitoring:','Not required',['aPTT','PT/INR','Anti Xa always'],'Not required.'),
('UFH antidote protamine sulfate:','Effective: Neutralizes HPS',['Not effective','Less effective','No antidote'],'Effective: Neutralizes HPS.'),
('LMWH antidote protamine:','Less effective',['Effective neutralizes HPS','Not effective','No effect'],'Less effective.'),
('Fondaparinux antidote protamine:','Not effective',['Effective','Less effective','Partially effective'],'Not effective.'),
('Risk of HIT with UFH is:','↑↑ (highest)',['↑','None','Same as LMWH'],'Risk of HIT ↑↑.'),
('Risk of HIT with LMWH is:','↑',['↑↑','None','Zero'],'Risk ↑.'),
('Risk of HIT with fondaparinux is:','None',['↑↑','↑','Moderate'],'None.'),
])
unit('Heparin Induced Thrombocytopenia and Heparin Uses',
 'Antibodies produced against HPS cross react with platelet factor 4 causing platelet aggregation leading to thrombosis incidence venous greater than arterial, female greater than male, surgical and cancer patients leading to heparin induced thrombocytopenia HIT not severe with cause UFH greater than LMWH and treatment same as thrombosis. Treatment of thrombosis is parenteral direct thrombin inhibitor argatroban DOC and fondaparinux; if platelet count greater than 1,50,000 start warfarin/DOAC with duration minimum 4 weeks and with history of major thromboembolic event 3 months. Uses UFH catheter induced thrombosis and anticoagulant with concurrent thrombolysis; LMWH/fondaparinux DOC for treatment of thrombosis. Heparin contraindications mnemonic TEACHER thrombocytopenia, endocarditis, alcoholics, cirrhosis, severe hypertension, eye/neurosurgery and renal failure for LMWH/fondaparinux; side effects mnemonic AHOT alopecia, hemorrhage/hyperkalemia, osteoporosis and thrombosis HIT.')
facts(253,[
('Antibodies in HIT are produced against:','HPS: Cross react with platelet factor 4',['Only platelet factor 4 alone','Only HPS alone','Only fibrinogen'],'Antibodies produced against HPS: Cross react with platelet factor 4.'),
('Antibodies cause:','Platelet aggregation',['Only bleeding','Only hemolysis','Only leukopenia'],'Platelet aggregation.'),
('Thrombosis in HIT incidence:','Venous > Arterial',['Arterial > Venous','Equal','Only arterial'],'Venous > Arterial.'),
('Gender incidence in HIT:','F > M',['M > F','Equal','Only in females'],'F > M.'),
('Patient groups at risk for HIT:','Surgical and cancer patients',['Only medical patients','Only healthy','Only children'],'Surgical and cancer patients.'),
('Heparin induced thrombocytopenia is:','Not severe',['Severe always','Fatal always','Only mild bleeding'],'Not severe.'),
('Cause of HIT more with:','UFH > LMWH',['LMWH > UFH','Fondaparinux > UFH','Equal for all'],'Cause: UFH > LMWH.'),
('Rx of HIT thrombosis is:','Same as thrombosis',['Only heparin','Only warfarin alone','Only stop heparin'],'Rx: Same as thrombosis.'),
('Treatment of thrombosis in HIT is:','Parenteral direct thrombin inhibitor: Argatroban(DOC) and Fondaparinux',['Only UFH','Only LMWH','Only warfarin'],'Parenteral direct thrombin inhibitor: Argatroban(DOC), Fondaparinux.'),
('If platelet count >1,50,000 in HIT:','Start Warfarin / DOAC',['Continue heparin','Stop all anticoagulants','Only aspirin'],'If platelet count >1,50,000 Start Warfarin / DOAC.'),
('Duration of treatment for HIT thrombosis:','Minimum 4 wks, With h/o major thromboembolic event: 3 months',['Only 1 week','Only 2 weeks','Lifelong always'],'Minimum 4 wks, With h/o major thromboembolic event: 3 months.'),
('UFH uses are:','Catheter induced thrombosis and Anticoagulant with concurrent thrombolysis',['Only catheter thrombosis','Only thrombolysis','Only DVT prophylaxis'],'Catheter induced thrombosis, Anticoagulant with concurrent thrombolysis.'),
('LMWH/Fondaparinux DOC for:','Rx of thrombosis',['Only catheter thrombosis','Only prophylaxis','Only HIT'],'DOC: Rx of thrombosis.'),
('Heparin C/I mnemonic is:','TEACHER',['AHOT','BRAIN','Only TEACHER'],'Mnemonic: TEACHER.'),
('TEACHER stands for:','Thrombocytopenia, Endocarditis, Alcoholics, Cirrhosis, Hypertension (Severe), Eye/Neurosurgery, Renal failure (LMWH/Fondaparinux)',['Only thrombocytopenia','Only endocarditis','Only renal failure'],'Thrombocytopenia, Endocarditis, Alcoholics, Cirrhosis, Hypertension (Severe), Eye/Neurosurgery, Renal failure (LMWH/Fondaparinux).'),
('Heparin S/E mnemonic is:','AHOT',['TEACHER','BRAIN','Only AHOT'],'Mnemonic: AHOT.'),
('AHOT stands for:','Alopecia, Hemorrhage/Hyperkalemia, Osteoporosis, Thrombosis: HIT',['Only alopecia','Only hemorrhage','Only thrombosis'],'Alopecia, Hemorrhage/Hyperkalemia, Osteoporosis, Thrombosis: HIT.'),
])
unit('Warfarin: MOA, Uses and Monitoring',
 'Warfarin inhibits vitamin K oxidoreductase VKOR decreasing active vitamin K which stimulates gamma carboxylase needed for factors II, VII, IX, X and protein C and S; factor VII first to decline, protein C and S second to decline and factor II last to decline; minimum 5 days to produce anticoagulant effect and first 5 days rapid decrease in protein C and S causes thrombosis leading to skin necrosis contraindicated in HIT. Uses prophylaxis of DVT DOC DOAC with heparin bridge LMWH for first 5 days until warfarin effective; thrombosis prophylaxis preferred over DOAC in valvular AF and non-valvular AF with renal failure, Pgp pump negative and severe mitral stenosis; DOC for thrombosis in antiphospholipid antibody syndrome and splanchnic vein thrombosis. Side effects bleeding, skin necrosis limbs breast penile area, worsens HIT, alopecia, blue feet and teratogenicity nasal mid facial hypoplasia and stippled epiphyseal calcification; contraindicated in pregnancy except if patient has mechanical valve. Monitoring PT/INR target 2-3 normal 0.9-1.3; INR 3-10 stop warfarin restart when INR normalizes; INR >10 asymptomatic stop warfarin plus vitamin K restart when INR normalizes; symptomatic bleeding stop warfarin start 4 factor prothrombin complex PTC greater than FFP plus IV vitamin K; note ciraparantag antidote for all anticoagulants except warfarin.')
facts(254,[
('Warfarin inhibits:','Vitamin K oxidoreductase (VKOR)',['Gamma carboxylase directly','Only protein C','Only factor X'],'Vitamin K Vit K oxidoreductase (VKOR).'),
('VKOR produces:','Active Vit K',['Inactive Vit K','Only protein C','Only factor II'],'VKOR -> ↓ Active Vit K.'),
('Active Vit K stimulates:','Gamma carboxylase',['Only VKOR','Only factor II','Only protein C'],'Active Vit K (+) γ carboxylase.'),
('Gamma carboxylase activates:','Factors II, VII, IX, X and Protein C & S',['Only factors II and VII','Only protein C & S','Only factor X'],'Factors: II, VII, IX, X Protein C & S.'),
('First factor to decline with warfarin is:','VII',['II','Protein C','Protein S'],'First to decline.'),
('Second to decline is:','Protein C & S',['Factor II','Factor VII','Factor IX'],'Second to decline.'),
('Last to decline is:','Factor II',['Factor VII','Protein C','Protein S'],'Last to decline.'),
('Minimum days for warfarin to produce anticoagulant effect:','5 days',['1 day','2 days','10 days'],'Minimum 5 days to produce anticoagulant effect.'),
('First 5 days rapid decrease in protein C & S causes:','Thrombosis -> Skin necrosis (C/I in HIT)',['Only bleeding','Only alopecia','Only blue feet'],'First 5 days: Rapid ↓ in protein C & S -> Thrombosis -> Skin necrosis (C/I in HIT).'),
('Prophylaxis of DVT DOC is:','DOAC',['Warfarin','Heparin','Aspirin'],'Prophylaxis of DVT (DOC: DOAC).'),
('Heparin bridge is:','LMWH for first 5 days until warfarin is effective',['Only warfarin alone','Only DOAC','No bridge needed'],'Heparin bridge: LMWH for first 5 days until warfarin is effective.'),
('Warfarin preferred over DOAC in:','Valvular AF and Non valvular AF with Renal failure, Pgp pump (-), Severe mitral stenosis',['Only non-valvular AF','Only valvular AF','No preference'],'Thrombosis prophylaxis (Preferred over DOAC) Valvular AF, Non valvular AF: Renal failure, Pgp pump (-), Severe mitral stenosis.'),
('Warfarin DOC for thrombosis in:','Antiphospholipid antibody syndrome and Splanchnic vein thrombosis',['Only antiphospholipid','Only splanchnic vein','Only DVT'],'DOC Thrombosis: Antiphospholipid antibody syndrome, Splanchnic vein thrombosis.'),
('Warfarin side effects include:','Bleeding, Skin necrosis (Limbs, breast, penile area), Worsens HIT, Alopecia, Blue feet',['Only bleeding','Only skin necrosis','Only alopecia'],'Bleeding, Skin necrosis, Worsens HIT, Alopecia, Blue feet.'),
('Skin necrosis sites with warfarin are:','Limbs, breast, penile area',['Only limbs','Only breast','Only penile'],'Limbs, breast, penile area.'),
('Warfarin teratogenicity:','Nasal (mid facial) hypoplasia and Stippled epiphyseal calcification',['Only nasal hypoplasia','Only stippled calcification','Only limb defects'],'Nasal (mid facial) hypoplasia, Stippled epiphyseal calcification.'),
('Warfarin C/I in pregnancy:','Pregnancy except if patient has mechanical valve',['Always contraindicated','Never contraindicated','Only first trimester'],'Pregnancy: Except if patient has mechanical valve.'),
('PT/INR target for warfarin is:','2-3 (Normal: 0.9-1.3)',['1-2','3-4','0.9-1.3 only'],'Target: 2-3 (Normal: 0.9-1.3).'),
('INR >3-10 management:','Stop warfarin -> Restart when INR normalizes',['Continue warfarin','Add vitamin K immediately','Start FFP'],'INR >3-10: Stop warfarin -> Restart when INR normalizes.'),
('INR >10 asymptomatic management:','Stop warfarin + Start vit K -> Restart when INR normalizes',['Only stop warfarin','Only vitamin K','Start FFP only'],'INR >10 & Asymptomatic: Stop warfarin + Start vit K -> Restart when INR normalizes.'),
('Symptomatic bleeding with warfarin:','Stop warfarin -> Start 4 factor prothrombin complex (PTC) > FFP + I/V Vit K',['Only vitamin K','Only FFP','Only stop warfarin'],'Symptomatic (Bleeding): Stop warfarin -> Start 4 factor prothrombin complex (PTC) > FFP + I/V Vit K.'),
('Ciraparantag is:','Antidote for all anticoagulants except warfarin',['Antidote for warfarin only','Only for heparin','Only for DOACs'],'Antidote for all anticoagulants except warfarin.'),
])
unit('Fibrinolytics and Antifibrinolytics',
 'Physiology of fibrinolysis plasminogen via tissue plasminogen activator TPA to plasmin which breaks fibrin. Streptokinase binds to plasminogen exposing TPA binding site increasing plasmin, clot non-specific breaking fibrin in both clot and plasma increasing bleeding risk and increased dose requirement. Recombinant tPA alteplase, duteplase, reteplase and tenecteplase most clot specific with single dose administration are clot specific. Uses STEMI never in NSTEMI/unstable angina, massive pulmonary embolism and peripheral thrombosis; contraindications mnemonic BRAIN brain tumour/aneurysm, recent surgery/trauma, aortic dissection, intracranial hemorrhage and NSTEMI. Side effect bleeding treated with antifibrinolytics inhibiting plasmin EACA epsilon aminocaproic acid and tranexamic acid used for thrombolytics induced bleeding, procedural bleed in hemophilia, GIT bleeding, trauma/surgical bleed and menorrhagia with contraindications upper genitourinary bleed risk of ischemia, hypotension and myopathy.')
facts(255,[
('Physiology of fibrinolysis:','Plasminogen Tissue Plasminogen Activator (TPA) -> Plasmin -> Breaks fibrin',['Only plasminogen -> fibrin','Only TPA -> fibrinogen','Only plasmin -> thrombin'],'Plasminogen TPA -> Plasmin -> Breaks fibrin.'),
('Streptokinase MOA:','Binds to plasminogen Exposes TPA binding site -> ↑ Plasmin',['Only inhibits plasmin','Only blocks TPA','Only degrades fibrinogen directly'],'Binds to plasminogen Exposes TPA binding site -> ↑ Plasmin.'),
('Streptokinase clot specificity:','Clot non specific: Breaks fibrin in both clot and plasma -> ↑ Risk of bleeding',['Clot specific','Only breaks clot fibrin','No bleeding risk'],'Clot non specific: Breaks fibrin in both clot and plasma -> ↑ Risk of bleeding.'),
('Streptokinase dose requirement is:','Increased dose requirement',['Decreased dose','No dose change','Only single dose'],'↑Dose requirement.'),
('Recombinant tPA drugs are:','Alteplase, Duteplase, Reteplase, Tenecteplase',['Only alteplase','Only streptokinase','Only tenecteplase'],'Alteplase, Duteplase, Reteplase, Tenecteplase.'),
('Recombinant tPA clot specificity is:','Clot specific',['Clot non specific','No specificity','Only non specific for alteplase'],'Clot specific.'),
('Most clot specific + single dose is:','Tenecteplase',['Alteplase','Reteplase','Streptokinase'],'Most clot specific + Single dose administration.'),
('Fibrinolytics use is:','STEMI (Never in: NSTEMI/Unstable angina), Massive pulmonary embolism, Peripheral thrombosis',['Only STEMI','Only NSTEMI','Only unstable angina'],'STEMI (Never in: NSTEMI/Unstable angina), Massive pulmonary embolism, Peripheral thrombosis.'),
('Fibrinolytics never in:','NSTEMI/Unstable angina',['STEMI','Massive PE','Peripheral thrombosis'],'Never in: NSTEMI/Unstable angina.'),
('Fibrinolytics C/I mnemonic is:','BRAIN',['TEACHER','AHOT','Only BRAIN'],'Mnemonic: BRAIN.'),
('BRAIN stands for:','Brain tumour/Aneurysm, Recent Sx/Trauma, Aortic dissection, Intracranial hemorrhage, NSTEMI',['Only brain tumour','Only recent surgery','Only aortic dissection'],'Brain tumour/Aneurysm, Recent Sx/Trauma, Aortic dissection, Intracranial hemorrhage, NSTEMI.'),
('Bleeding due to fibrinolytics Rx is:','Antifibrinolytics -> X -> Plasmin',['Only continue fibrinolytics','Only vitamin K','Only FFP'],'Antifibrinolytics X Plasmin.'),
('Antifibrinolytics are:','EACA (Epsilon aminocaproic acid) and Tranexamic acid',['Only EACA','Only tranexamic acid','Only aprotinin'],'EACA Tranexamic acid.'),
('Antifibrinolytics uses include:','Thrombolytics induced bleeding, Procedural bleed in hemophilia, GIT bleeding, Trauma/Surgical bleed, Menorrhagia',['Only thrombolytics bleeding','Only menorrhagia','Only GIT bleeding'],'Uses: Thrombolytics induced bleeding, Procedural bleed in hemophilia, GIT bleeding, Trauma/Surgical bleed, Menorrhagia.'),
('Antifibrinolytics C/I include:','Upper Genitourinary bleed: Risk of Ischemia, Hypotension, Myopathy',['Only upper GU bleed','Only hypotension','Only myopathy'],'C/I: Upper Genitourinary bleed: Risk of Ischemia, Hypotension, Myopathy.'),
('Upper genitourinary bleed with antifibrinolytics risk is:','Ischemia',['Only bleeding','Only thrombosis','Only infection'],'Risk of Ischemia.'),
])
finish()

# CHAPTER 65 - BRONCHIAL ASTHMA (p256-258) -----------------------------------
start(65)
unit('Pathophysiology and Bronchodilator Classification',
 'Bronchial asthma pathophysiology: allergen exposure leads to mast cell lysis releasing histamine causing bronchoconstriction and inflammation treated with bronchodilators and steroids respectively. Bronchodilators classification includes beta2 agonists, anticholinergics and methylxanthines.')
facts(256,[
('Pathophysiology of bronchial asthma:','Allergen exposure -> mast cell lysis -> Histamine Release -> Bronchoconstriction & Inflammation',['Only bronchoconstriction','Only inflammation','Only mast cell lysis'],'Allergen exposure -> mast cell lysis -> Histamine Release -> Bronchoconstriction & Inflammation.'),
('Bronchoconstriction in asthma Rx is:','Bronchodilators',['Steroids','Only antihistaminics','Only antibiotics'],'Bronchoconstriction Rx Bronchodilators.'),
('Inflammation in asthma Rx is:','Steroids',['Bronchodilators','Only antihistaminics','Only antibiotics'],'Inflammation Rx Steroids.'),
('Bronchodilators classification includes:','Beta2 agonists, Anticholinergics, Methylxanthines',['Only beta agonists','Only anticholinergics','Only methylxanthines'],'Classification: Beta2 agonists, Anticholinergics, Methylxanthines.'),
])
unit('Methylxanthines: MOA and Drugs',
 'Methylxanthine MOA bronchodilation via inhibition of phosphodiesterase 3 PDE3 greater than PDE4 increasing cAMP relaxing smooth muscles plus adenosine receptor antagonism; anti-inflammatory via PDE4 inhibition roflumilast for COPD, stimulation of histone deacetylase which steroids also stimulate, increased IL-10 and apoptosis of neutrophils. Drugs oral theophylline greater than aminophylline add on treatment of persistent BA and IV aminophylline greater than theophylline for acute exacerbation of BA.')
facts(256,[
('Methylxanthine bronchodilation MOA is:','(-) Phosphodiesterase 3 (PDE3 > PDE4) -> ↑ cAMP -> Relax smooth muscles and Adenosine Receptor antagonism',['Only PDE4 inhibition','Only adenosine antagonism','Only PDE3 inhibition only'],'(-) Phosphodiesterase 3 (PDE3 > PDE4) -> ↑ cAMP Relax smooth muscles Adenosine Receptor antagonism.'),
('Methylxanthine anti-inflammatory MOA includes:','PDE 4 (-): Roflumilast -> Rx of COPD, (+) Histone deacetylase, ↑ IL-10, Apoptosis of neutrophils',['Only PDE3 inhibition','Only adenosine antagonism','Only cAMP increase'],'PDE 4 (-): Roflumilast -> Rx of COPD, (+) Histone deacetylase, ↑ IL-10, Apoptosis of neutrophils.'),
('Roflumilast is:','PDE4 inhibitor used for COPD',['PDE3 inhibitor','Only for asthma','Only bronchodilator'],'PDE 4 (-): Roflumilast -> Rx of COPD.'),
('Histone deacetylase is stimulated by:','Methylxanthines and steroids',['Only methylxanthines','Only steroids','Neither'],'(+) Histone deacetylase (Steroids also stimulate it).'),
('Methylxanthine increases:','IL-10',['IL-1','Only TNF','Only IL-6'],'↑ IL-10.'),
('Methylxanthine causes apoptosis of:','Neutrophils',['Only eosinophils','Only lymphocytes','Only macrophages'],'Apoptosis of neutrophils.'),
('Oral methylxanthine drug is:','Theophylline > Aminophylline',['Aminophylline > Theophylline','Only theophylline','Only aminophylline'],'Oral Theophylline > Aminophylline.'),
('Oral theophylline use is:','Add on Rx of persistent BA',['Acute exacerbation of BA','Only COPD','Only intermittent asthma'],'Add on Rx of persistent BA.'),
('IV methylxanthine drug is:','Aminophylline > Theophylline',['Theophylline > Aminophylline','Only theophylline','Only aminophylline'],'IV Aminophylline > Theophylline.'),
('IV aminophylline use is:','Acute exacerbation of BA',['Add on persistent BA','Only COPD','Only intermittent'],'Acute exacerbation of BA.'),
])
unit('Methylxanthines: Side Effects and Therapeutic Index',
 'Side effects due to PDE4 inhibition at levels around 20-25 mg/L cause GI upset nausea vomiting and headache; due to adenosine receptor antagonism at greater than 30 mg/L cause arrhythmia also due to PDE3 inhibition and seizures. Low therapeutic index with theophylline normal range 5-15 mg/L and toxicity greater than 20 mg/L.')
facts(256,[
('Methylxanthine S/E D/t PDE4 (-) occurs at:','At levels ~20-25 mg/L',['At >30 mg/L','At 5-15 mg/L','At <5 mg/L'],'At levels ~20-25 mg/L.'),
('PDE4 inhibition S/E includes:','GI upset: Nausea, vomiting and Headache',['Only arrhythmia','Only seizures','Only GI upset only'],'GI upset: Nausea, vomiting, Headache.'),
('Methylxanthine S/E D/t Adenosine Receptor (-) occurs at:','At >30 mg/L',['At 20-25 mg/L','At 5-15 mg/L','At <5 mg/L'],'At >30 mg/L.'),
('Adenosine receptor antagonism S/E includes:','Arrhythmia (Also d/t PDE 3(-)) and Seizures',['Only GI upset','Only headache','Only nausea'],'Arrhythmia (Also d/t PDE 3(-)), Seizures.'),
('Theophylline normal therapeutic range is:','5-15 mg/L',['20-25 mg/L','>30 mg/L','0-5 mg/L'],'Theophylline (N) range: 5-15 mg/L.'),
('Theophylline toxicity level is:','>20 mg/L',['5-15 mg/L','20-25 mg/L','>30 mg/L only'],'Toxicity: >20 mg/L.'),
('Theophylline has:','Low therapeutic index',['High therapeutic index','No therapeutic index','Only wide index'],'Low Therapeutic index.'),
])
unit('Inhalational and Systemic Steroids in Asthma',
 'Inhalational corticosteroids ICS drugs fluticasone most potent, mometasone, budesonide, ciclesonide and beclomethasone soft steroids with decreased side effects due to metabolism in airway and flunisolide least potent; uses persistent BA, exercise induced asthma EIA, aspirin induced bronchoconstriction DOC and intermittent BA less than 2 attacks/week; side effects hoarseness of voice most common, oropharyngeal candidiasis prevented by good inhaler technique and systemic side effects minimal. Note intermittent asthma treatment 0-5 years SABA short acting beta agonist, 6-11 years SABA plus ICS SABA before ICS, greater than 12 years FDC ICS plus pMDI formoterol decreasing number and severity of attack. Systemic steroids oral prednisone/prednisolone and IV hydrocortisone faster acting greater than methylprednisolone used for persistent asthma if ICS fails and acute exacerbation oral greater than IV steroids; MOA in acute exacerbation decreases mucus secretion, decreases inflammatory mediators and increases beta2 receptors increasing effect of beta2 agonist increasing steroid effect complementary.')
facts(257,[
('Most potent ICS is:','Fluticasone',['Mometasone','Budesonide','Flunisolide'],'Fluticasone: most potent.'),
('Least potent ICS is:','Flunisolide',['Fluticasone','Mometasone','Budesonide'],'Flunisolide: Least potent.'),
('Soft steroids are:','Ciclesonide and Beclomethasone: ↓ S/E d/t metabolism in airway',['Fluticasone and mometasone','Budesonide only','Flunisolide only'],'Soft steroids: ↓ S/E d/t metabolism in airway.'),
('ICS drugs include:','Fluticasone, Mometasone, Budesonide, Ciclesonide, Beclomethasone, Flunisolide',['Only fluticasone','Only budesonide','Only beclomethasone'],'Drugs list.'),
('ICS uses include:','Persistent BA, Exercise Induced Asthma (EIA), Aspirin Induced Bronchoconstriction, Intermittent BA (<2 attacks/wk)',['Only persistent BA','Only EIA','Only intermittent BA'],'Persistent BA, Exercise Induced Asthma (EIA), Aspirin Induced Bronchoconstriction, Intermittent BA (<2 attacks/wk).'),
('DOC for aspirin induced bronchoconstriction is:','ICS',['Only SABA','Only systemic steroids','Only leukotriene blockers'],'Aspirin Induced Bronchoconstriction DOC.'),
('ICS side effect most common is:','Hoarseness of voice',['Oropharyngeal candidiasis','Systemic effects','Only hoarseness only'],'Hoarseness of voice: m/c.'),
('Oropharyngeal candidiasis with ICS prevented by:','Good inhaler technique',['Only dose reduction','Only stopping ICS','Only adding antifungal prophylaxis'],'Prevented by good inhaler technique.'),
('Systemic S/E with ICS is:','Minimal',['Maximum','Moderate','Severe always'],'Systemic S/E: minimal.'),
('Intermittent asthma 0-5 years Rx:','SABA (Short acting β Agonist)',['SABA + ICS','FDC ICS + Formoterol','Only ICS'],'0-5 years: SABA (Short acting β Agonist).'),
('Intermittent asthma 6-11 years Rx:','SABA + ICS (SABA before ICS)',['Only SABA','FDC ICS + Formoterol','Only ICS'],'6-11 years: SABA + ICS (SABA before ICS).'),
('Intermittent asthma >12 years Rx:','FDC ICS + pMDI Formoterol -> ↓Number & Severity of attack',['Only SABA','SABA + ICS only','Only systemic steroids'],'>12 years: FDC ICS + pMDI Formoterol -> ↓Number & Severity of attack.'),
('Systemic steroids oral is:','Prednisone/Prednisolone',['Hydrocortisone only','Methylprednisolone only','Only dexamethasone'],'Oral: Prednisone/Prednisolone.'),
('Systemic steroids I/V is:','Hydrocortisone (Faster acting) > Methylprednisolone',['Only methylprednisolone','Only prednisone','Only dexamethasone'],'I/V drug: Hydrocortisone (Faster acting) > methylprednisolone.'),
('Systemic steroids for persistent asthma:','Oral steroids if ICS fails',['Only IV steroids','Only ICS','No steroids needed'],'Persistent asthma: Oral steroids if ICS fails.'),
('Acute exacerbation steroids:','Oral > I/V steroids',['I/V > Oral','Only IV','Only oral'],'Acute Exacerbation: Oral > I/V steroids.'),
('Steroids MOA in acute exacerbation decreases:','Mucus secretion and Inflammatory mediators',['Only mucus','Only inflammatory mediators','Only beta receptors'],'↓ Mucus secretion, ↓ Inflammatory mediators.'),
('Steroids increase in acute exacerbation:','β2 receptors -> ↑ Effect of β2 Agonist -> ↑ Steroid Effect (Complementary)',['Only beta1','Only alpha','Only muscarinic'],'↑ β2 receptors -> ↑ Effect of β2 Agonist -> ↑ Steroid Effect (Complementary).'),
])
unit('Accessory Drugs: Antileukotrienes, Mast Cell Stabilizers and Monoclonal Antibodies',
 'Antileukotrienes are 5-LOX lipoxygenase inhibitors zileuton and LTC4/LTD4 inhibitors montelukast, zafirlukast and pranlukast used for persistent BA add-on to ICS, EIA and allergic rhinitis with montelukast and side effects hepatotoxicity maximum with zileuton and Churg-Strauss syndrome with montelukast and zafirlukast. Mast cell stabilizers inhibit Ca2+ channels in mast cells preventing degranulation decreasing histamine release; drugs cromolyn sodium and nedocromil uses oral food allergy systemic mastocytosis, nasal spray allergic rhinitis, eye drops allergic conjunctivitis and inhalational mild asthma least toxic preferred in children; ketotifen MOA mast cell stabilization plus increased NO release used for prophylaxis of allergen induced asthma. Monoclonal antibodies omalizumab anti IgE monoclonal antibody SC every 2-4 weeks used for resistant asthma, allergic rhinitis, chronic urticaria and food allergy dosed based on weight and IgE titer contraindicated in atopic dermatitis due to very high IgE; IL-4 and IL-5 related dupilumab blocks IL-4 receptor on T-helper cells, reslizumab and mepolizumab block IL-5 and benralizumab blocks IL-5 receptor on eosinophils decreasing maturation and survival used for severe eosinophilic asthma and atopic dermatitis.')
facts(258,[
('5-LOX (Lipoxygenase) Inhibitor is:','Zileuton',['Montelukast','Zafirlukast','Pranlukast'],'5-LOX Inhibitors: Zileuton.'),
('LTC4/LTD4 Inhibitors are:','Montelukast, Zafirlukast, Pranlukast',['Only montelukast','Only zileuton','Only pranlukast'],'LTC4/LTD4 Inhibitor: montelukast, Zafirlukast, Pranlukast.'),
('Antileukotrienes uses include:','Persistent BA: Add-on to ICS, EIA, Allergic rhinitis: montelukast',['Only persistent BA','Only EIA','Only allergic rhinitis'],'Uses: Persistent BA: Add-on to ICS, EIA, Allergic rhinitis: montelukast.'),
('Antileukotriene S/E hepatotoxicity max with:','Zileuton',['Montelukast','Zafirlukast','Pranlukast'],'Hepatotoxicity: max with zileuton.'),
('Churg-Strauss syndrome S/E with:','Montelukast & Zafirlukast',['Only zileuton','Only pranlukast','Only montelukast alone'],'Churg-Strauss syndrome: montelukast & Zafirlukast.'),
('Mast cell stabilizers MOA:','Inhibit Ca2+ channels in mast cells Prevent Degranulation ↓ Release Histamine',['Only increase histamine','Only block H1','Only block leukotrienes'],'Inhibit Ca2+ channels in mast cells Prevent Degranulation ↓ Release Histamine.'),
('Cromolyn sodium, Nedocromil oral use:','Food allergy, systemic mastocytosis',['Only asthma','Only rhinitis','Only conjunctivitis'],'Oral: Food allergy, systemic mastocytosis.'),
('Cromolyn nasal spray use:','Allergic rhinitis',['Food allergy','Only asthma','Only conjunctivitis'],'Nasal spray: Allergic rhinitis.'),
('Cromolyn eye drops use:','Allergic conjunctivitis',['Only rhinitis','Only asthma','Only food allergy'],'Eye drops: Allergic conjunctivitis.'),
('Cromolyn inhalational use:','Mild asthma (Least toxic -> Preferred in children)',['Severe asthma','Only COPD','Only EIA'],'Inhalational: mild asthma (Least toxic -> Preferred in children).'),
('Ketotifen MOA is:','Mast cell stabilization + ↑ NO release',['Only mast cell stabilization','Only NO release','Only H1 blockade'],'Mast cell stabilization + ↑ NO release.'),
('Ketotifen use is:','Prophylaxis of allergen induced asthma',['Only food allergy','Only rhinitis','Only conjunctivitis'],'Prophylaxis of allergen induced asthma.'),
('Omalizumab is:','Anti IgE monoclonal antibody',['Anti IL-5','Anti IL-4','Anti IL-4 receptor'],'Anti IgE monoclonal antibody.'),
('Omalizumab route is:','S/C x every 2-4 wks',['IV only','Oral only','IM only'],'Route: S/C x every 2-4 wks.'),
('Omalizumab uses include:','Resistant asthma, Allergic rhinitis, Chronic urticaria, Food allergy',['Only resistant asthma','Only allergic rhinitis','Only chronic urticaria'],'Resistant asthma, Allergic rhinitis, Chronic urticaria, Food allergy.'),
('Omalizumab dose based on:','Weight of pt and IgE titer',['Only weight','Only IgE titer','Only age'],'Based on weight of pt, IgE titer.'),
('Omalizumab C/I is:','Atopic dermatitis (D/t: ↑↑ IgE)',['Only asthma','Only rhinitis','Only urticaria'],'C/I: Atopic dermatitis (D/t: ↑↑ IgE).'),
('Dupilumab blocks:','IL-4 Receptor on T-helper cells',['IL-5','IL-5 receptor','IgE'],'Dupilumab X IL-4 Receptor on T-helper cells.'),
('Reslizumab and mepolizumab block:','IL-5',['IL-4','IL-5 receptor','IgE'],'Reslizumab Mepolizumab X IL-5.'),
('Benralizumab blocks:','IL-5 Receptor on eosinophils',['IL-4 receptor','IL-5 itself','IgE'],'Benralizumab X IL-5 Receptor on eosinophils.'),
('IL-5 receptor activation causes:','Maturation & survival of eosinophils',['Only maturation','Only survival','Only apoptosis'],'Maturation & survival.'),
('IL-4 & IL-5 monoclonal antibodies uses:','Severe Eosinophilic asthma and Atopic Dermatitis',['Only severe eosinophilic asthma','Only atopic dermatitis','Only food allergy'],'Severe Eosinophilic asthma, Atopic Dermatitis: Atopic dermatitis.'),
])
finish()
