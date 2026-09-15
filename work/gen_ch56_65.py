# -*- coding: utf-8 -*-
"""Generate chapters 56-65 from Marrow Pharmacology E8, book pp224-258.

Mixed types: mcq (CHOOSE), fill (FILL IN THE BLANK), match (MATCH).
Distractors are near-misses of similar length — never dummy 'Only X' pads.
"""
import json, re
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

def _exp(p, exp, fallback):
    e=(exp or fallback).rstrip('.')
    return e + f' (Book p{p})'

def mcq(p, text, answer, wrong, exp=None):
    assert CUR and len(wrong)==3 and answer not in wrong
    assert len(set([answer]+wrong))==4
    # reject dummy pads
    dummy=sum(1 for w in wrong if re.match(r'(?i)^(only |neither|none of)', w.strip()))
    assert dummy < 2, f'dummy distractors: {text}'
    Q.append({'id':'','sec':CUR['title'],'page':p,'type':'mcq','q':text,
              'opts':[answer]+wrong,'ans':0,'exp':_exp(p,exp,answer)})

def fill(p, text, blank, exp=None, aliases=None):
    assert CUR and '____' in text and str(blank).strip()
    extra=list(aliases or [])
    b=blank.strip()
    extra += [b.lower(), b.replace('-',' to '), b.replace(' to ','-'),
              b.replace('α','alpha'), b.replace('β','beta'),
              b.replace('↑','increase'), b.replace('↓','decrease')]
    seen=set(); al=[]
    for a in extra:
        k=a.strip()
        if k and k.lower()!=b.lower() and k.lower() not in seen:
            seen.add(k.lower()); al.append(k)
    Q.append({'id':'','sec':CUR['title'],'page':p,'type':'fill','q':text,
              'blank':b,'aliases':al,'exp':_exp(p,exp,b)})

def match(p, text, pairs, exp=None):
    assert CUR and 3<=len(pairs)<=4
    left=[a for a,_ in pairs]; right=[b for _,b in pairs]
    assert len(set(left))==len(left) and len(set(right))==len(right)
    exp_fb='; '.join(f'{a} → {b}' for a,b in pairs)
    Q.append({'id':'','sec':CUR['title'],'page':p,'type':'match','q':text,
              'left':left,'right':right,'ans':list(range(len(pairs))),
              'exp':_exp(p,exp,exp_fb)})

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
    n_mcq=sum(1 for x in Q if x.get('type','mcq')=='mcq')
    n_fill=sum(1 for x in Q if x.get('type')=='fill')
    n_match=sum(1 for x in Q if x.get('type')=='match')
    print(f'ch{CH}: {len(Q)} questions ({n_mcq} mcq / {n_fill} fill / {n_match} match), {len(units)} units')

# CHAPTER 56 - DRUGS ACTING ON BONE (p224-226) -------------------------------
start(56)
unit('Calcium Homeostasis: RANK-RANKL Physiology and Steps of Bone Remodeling',
 'PTH and vitamin D3 stimulate osteoblasts to synthesize RANK ligand (Step-I). RANK ligand activates RANK receptor on osteoclast precursors (Step-II), causing ruffled borders (Step-III) and bone resorption (Step-IV). Resorption then activates osteoblasts (Step-V) and new bone forms at the injury site (Step-VI). Strontium ranelate uniquely increases formation and decreases resorption.')
match(224, 'Match each remodeling step with what happens.', [
    ('Step-I', 'PTH / Vit D3 induce RANK-ligand synthesis'),
    ('Step-II', 'RANK ligand activates RANK on osteoclasts'),
    ('Step-III', 'Osteoclasts form ruffled borders'),
    ('Step-IV', 'Osteoclasts resorb (damage) bone'),
])
match(224, 'Match the later remodeling events.', [
    ('Step-V', 'Activation of osteoblast'),
    ('Step-VI', 'Bone formation at the injury site'),
    ('RANK ligand source', 'Osteoblast'),
    ('RANK receptor site', 'Osteoclast'),
])
fill(224, 'RANK ligand is produced by the ____.', 'osteoblast')
fill(224, 'The RANK receptor sits on the ____.', 'osteoclast')
mcq(224, 'Teriparatide’s place in the remodeling diagram is:',
    'PTH analog that stimulates osteoblasts (Step-V)',
    ['RANK-ligand antibody that blocks osteoclast activation',
     'Sclerostin antibody that increases bone formation',
     'Calcitonin analog that most rapidly lowers calcium'])
mcq(224, 'Raloxifene reduces bone resorption because it:',
    'Acts as an estrogen agonist on bone (SERM)',
    ['Inhibits sclerostin on osteocytes',
     'Inhibits farnesyl pyrophosphate synthase',
     'Directly stimulates PTH receptors on osteoblasts'])
fill(224, 'Sclerostin inhibits bone ____.', 'formation')
fill(224, 'Romosozumab inhibits ____.', 'sclerostin')
mcq(224, 'Strontium ranelate is unique because it:',
    'Increases formation AND decreases resorption',
    ['Decreases formation AND increases resorption',
     'Increases formation without changing resorption',
     'Decreases resorption without changing formation'])
mcq(224, 'Denosumab in the remodeling diagram blocks:',
    'The osteoblast → osteoclast RANK-ligand signal',
    ['Sclerostin on osteocytes',
     'Farnesyl pyrophosphate synthase inside osteoclasts',
     'PTH receptors on osteoblasts'])
mcq(224, 'Bisphosphonates vs calcium analogs (calcitonin) for hypocalcemia:',
    'Bisphosphonates = DOC for MAXIMUM hypocalcemia; calcitonin = FASTEST',
    ['Calcitonin = DOC for MAXIMUM hypocalcemia; bisphosphonates = FASTEST',
     'Both equally fast and equally maximum',
     'Denosumab is both fastest and maximum'])

unit('Bisphosphonates: MOA and Pharmacology',
 'Bisphosphonates inhibit farnesyl pyrophosphate synthase in osteoclasts, causing osteoclast apoptosis. They are the DOC when maximum hypocalcemia is needed. Oral absorption is poor, so they must be taken on an empty stomach.')
fill(224, 'Bisphosphonates inhibit ____ synthase in osteoclasts, causing apoptosis.', 'farnesyl pyrophosphate',
     aliases=['FPP synthase','farnesyl pyrophosphate synthase','FPPS'])
mcq(224, 'Because oral absorption of bisphosphonates is poor, they should be taken:',
    'On an empty stomach',
    ['With milk to protect the esophagus',
     'With a calcium tablet to aid uptake',
     'After a fatty meal to increase bile'])
fill(224, 'The fastest hypocalcemia is produced by ____ analogs (calcitonin).', 'calcium')
fill(224, 'Bisphosphonates are the DOC when ____ hypocalcemia is required.', 'maximum',
     aliases=['max'])

unit('Bisphosphonates: Route, Dosing and Clinical Uses',
 'IV pamidronate every 3 months and zoledronate (preferred, once yearly, longest, most potent) are given for 3 years. Oral risedronate OD and alendronate (preferred OD) are given for 5 years. Osteoporosis DOC is alendronate; if intolerant switch to zoledronate. Hypercalcemia of malignancy and Paget start with zoledronate.')
match(225, 'Match the bisphosphonate with its usual route / interval.', [
    ('Pamidronate', 'IV every 3 months'),
    ('Zoledronate', 'IV once yearly'),
    ('Risedronate', 'Oral once daily'),
    ('Alendronate', 'Preferred oral, once daily'),
])
fill(225, 'IV bisphosphonates are typically given for ____ years.', '3')
fill(225, 'Oral bisphosphonates are typically given for ____ years.', '5')
fill(225, 'The DOC for osteoporosis is ____.', 'alendronate')
fill(225, 'If the patient is intolerant to alendronate, switch to ____.', 'zoledronate',
     aliases=['zolendronate','zoledronic acid'])
mcq(225, 'Hypercalcemia of malignancy and Paget disease of bone are started with:',
    'Zoledronate directly',
    ['Alendronate for 5 years first',
     'Risedronate oral OD first',
     'Calcitonin nasal spray as DOC'])
mcq(225, 'Which IV bisphosphonate is preferred, longest-acting and more potent?',
    'Zoledronate',
    ['Pamidronate','Alendronate','Risedronate'])

unit('Bisphosphonates: Side Effects and Prevention',
 'Oral bisphosphonates cause esophagitis — take with a full glass of water and do not lie down for 30 minutes. IV > oral: bone fracture (femoral chalk-stick; DOC teriparatide), maximum hypercalcemia as a paradox, and osteonecrosis of the jaw.')
fill(225, 'The characteristic oral-route side effect of bisphosphonates is ____.', 'esophagitis')
mcq(225, 'To prevent bisphosphonate esophagitis the patient should:',
    'Take it with a full glass of water and remain upright 30 min',
    ['Take it with milk and lie on the left side',
     'Take it at bedtime with an antacid',
     'Crush the tablet and take it with calcium'])
fill(225, 'Do not lie down for ____ minutes after an oral bisphosphonate.', '30',
     aliases=['30 min','30 minutes'])
fill(225, 'The characteristic bisphosphonate fracture is a femoral ____ fracture.', 'chalk-stick',
     aliases=['chalk stick','chalkstick'])
fill(225, 'DOC for a bisphosphonate-induced femoral chalk-stick fracture is ____.', 'teriparatide')
fill(225, 'IV > oral bisphosphonates can cause osteonecrosis of the ____.', 'jaw')
mcq(225, 'Paradoxical mineral side effect that is MAXIMUM with IV bisphosphonates:',
    'Hypercalcemia',
    ['Hyponatremia','Hypokalemia','Hyperphosphatemia'])

unit('Denosumab, Raloxifene and Calcitonin Analog',
 'Denosumab is a monoclonal antibody against RANK ligand used in postmenopausal osteoporosis. Calcitonin analog is used intranasally for osteoporosis and S/C for Paget, but increases cancer risk. Raloxifene is a SERM / estrogen agonist on bone.')
fill(225, 'Denosumab inhibits ____.', 'RANK ligand', aliases=['RANKL','rank-l'])
fill(225, 'Denosumab is used in ____ osteoporosis.', 'postmenopausal',
     aliases=['post-menopausal','post menopausal'])
fill(225, 'Raloxifene is a ____ that is an estrogen agonist on bone.', 'SERM',
     aliases=['selective estrogen receptor modulator'])
match(225, 'Match calcitonin analog route with indication.', [
    ('Intranasal calcitonin', 'Osteoporosis'),
    ('S/C calcitonin', 'Paget disease'),
    ('Calcitonin safety note', 'Increased risk of cancer'),
])

unit('Anabolic Drugs and Postmenopausal Osteoporosis Algorithm',
 'Teriparatide (PTH analog) can cause osteosarcoma, is C/I in Paget, and is limited to 2 years. Abaloparatide is a PTHrP analog. Romosozumab inhibits sclerostin. Algorithm: alendronate DOC → intolerance zoledronate → check fracture risk → high: denosumab; very high: anabolic (teriparatide / romosozumab).')
fill(226, 'The PTH analog used as an anabolic bone drug is ____.', 'teriparatide')
fill(226, 'The feared side effect of teriparatide is ____.', 'osteosarcoma')
fill(226, 'Teriparatide is contraindicated in ____ disease of bone.', 'Paget', aliases=["Paget's",'Pagets'])
fill(226, 'Maximum duration of teriparatide is ____ years.', '2')
fill(226, 'The PTHrP analog is ____.', 'abaloparatide')
fill(226, 'Romosozumab inhibits ____.', 'sclerostin')
match(226, 'Match the postmenopausal osteoporosis algorithm step.', [
    ('First-line DOC', 'Alendronate'),
    ('If alendronate intolerant', 'Zoledronate'),
    ('High fracture risk after IV intolerance', 'Denosumab'),
    ('Very high fracture risk', 'Teriparatide or romosozumab'),
])
finish()

# CHAPTER 57 - DRUGS ACTING ON THYROID (p227-229) ----------------------------
start(57)
unit('Thyroid Physiology and Sites of Drug Action',
 'TSH on TSH-receptor increases production via Na+/I- symporter, TPO and thiol endopeptidase. TPO does organification (1) and coupling (2) to make MIT/DIT then T3/T4 stored as thyroglobulin in colloid. Thiol endopeptidase releases T3/T4; peripheral 5-deiodinase converts T4 to active T3.')
match(227, 'Match the thyroid enzyme / transporter with its job.', [
    ('Na+-I- symporter', 'Iodide uptake into the follicle'),
    ('TPO', 'Organification (1) and coupling (2)'),
    ('Thiol endopeptidase', 'Breaks thyroglobulin to release T3/T4'),
    ('5-deiodinase', 'Peripheral T4 → active T3'),
])
fill(227, 'T3 and T4 are stored in colloid as ____.', 'thyroglobulin', aliases=['TG'])
fill(227, 'The active thyroid hormone is ____.', 'T3', aliases=['triiodothyronine'])
mcq(227, 'Organification and coupling are both:',
    'TPO steps inhibited by thioamides',
    ['Release steps inhibited by iodide',
     'Peripheral conversion steps inhibited by amiodarone',
     'Uptake steps inhibited by perchlorate only'])
fill(227, 'Release of T3/T4 is inhibited by excess ____.', 'iodide', aliases=['iodine','iodide excess'])

unit('Thioamide Drugs: Propylthiouracil and Methimazole',
 'Thioamides: PTU and carbimazole (prodrug → methimazole, longer acting). PTU: short T1/2, multiple dosing, hepatotoxic. Methimazole: long T1/2, OD, teratogenic (cutis aplasia / scalp defect, choanal/esophageal atresia) and cholestatic jaundice. Common: maculopapular rash (m/c), agranulocytosis, arthralgia.')
fill(227, 'Carbimazole is a prodrug converted to ____.', 'methimazole', aliases=['thiamazole'])
match(227, 'Match the thioamide with its kinetic / toxicity profile.', [
    ('PTU', 'Short T1/2, multiple dosing, hepatotoxic'),
    ('Methimazole', 'Long T1/2, once daily, teratogenic + cholestatic jaundice'),
    ('Carbimazole', 'Prodrug of methimazole, longer acting'),
])
fill(227, 'The most common shared thioamide side effect is ____ rash.', 'maculopapular')
mcq(227, 'Methimazole teratogenicity includes:',
    'Cutis aplasia (scalp defect) and choanal / esophageal atresia',
    ['Neural-tube defects and Ebstein anomaly',
     'Phocomelia and hearing loss',
     'Cleft lip without scalp defects'])
mcq(227, 'Shared serious thioamide toxicities (besides rash) include:',
    'Agranulocytosis and arthralgia',
    ['Pulmonary fibrosis and blue-grey skin',
     'Cinchonism and hypoglycemia',
     'Osteonecrosis of the jaw and chalk-stick fracture'])

unit('Thioamide Uses and Thyroid Storm Management',
 'PTU is preferred in 1st trimester (less teratogenic) and in thyroid storm. Methimazole is commonly prescribed and preferred in 2nd–3rd trimester (less hepatotoxic). Thyroid storm 1st drug: beta blockers to prevent AF; if C/I (asthma/COPD) use verapamil/diltiazem; also steroid and KI.')
fill(228, 'Preferred thioamide in the 1st trimester of pregnancy is ____.', 'PTU',
     aliases=['propylthiouracil'])
fill(228, 'Preferred thioamide in the 2nd and 3rd trimester is ____.', 'methimazole')
fill(228, 'The first drug in thyroid storm is a ____ blocker (to prevent AF).', 'beta',
     aliases=['β','beta-blocker','beta blocker'])
mcq(228, 'If beta blockers are contraindicated in thyroid storm because of asthma/COPD, use:',
    'Verapamil or diltiazem',
    ['Adenosine or digoxin',
     'Amiodarone or sotalol',
     'Nifedipine or amlodipine'])
mcq(228, 'Other drugs used in thyroid storm (besides the rate-control agent) include:',
    'A steroid and potassium iodide',
    ['Levothyroxine and liothyronine',
     'Radioactive I131 on day 0',
     'Carbimazole as the sole drug'])

unit('Thiol Endopeptidase Inhibitors: Iodides',
 'KI 10% and Lugol iodine 5% inhibit T3/T4 release — fastest-acting antithyroid drugs — but tolerance develops so they are not long-term therapy. They shrink and firm the gland and reduce vascularity/bleeding, so they are used prior to surgery.')
fill(228, 'Potassium iodide is ____%; Lugol iodine is 5%.', '10', aliases=['10%'])
fill(228, 'Lugol iodine is ____%; potassium iodide is 10%.', '5', aliases=['5%'])
fill(228, 'Iodides inhibit ____ of T3/T4 and are the fastest-acting antithyroid drugs.', 'release')
mcq(228, 'Iodides are NOT used as long-term antithyroid therapy because they:',
    'Develop tolerance',
    ['Cause agranulocytosis in weeks',
     'Are too hepatotoxic',
     'Block 5-deiodinase permanently'])
mcq(228, 'Pre-operative extra benefits of iodides include:',
    'Smaller, firmer gland with fewer vessels (less bleeding)',
    ['Larger, softer gland that is easier to dissect',
     'Increased vascularity so the surgeon can see planes',
     'Ablation of remnant tissue like I131'])

unit('Peripheral Conversion Inhibitors and Radioactive Iodine',
 '5-deiodinase / T4→T3 blockers: PTU, steroids, beta blockers, amiodarone. I131 = ablation; I123 = scan. I131 uses: elderly hyperthyroid, arrhythmia, thyroid ca except medullary, recurrent Graves. Radiation thyroiditis: premedicate with methimazole, stop 3 days before I131, restart 3 days after. Lifelong hypothyroidism, secondary cancers; C/I pregnancy.')
match(229, 'Match the 5-deiodinase (T4→T3) inhibitor class.', [
    ('PTU', 'Thioamide that also blocks peripheral conversion'),
    ('Steroids', 'Used in storm; block T4→T3'),
    ('Beta blocker', 'Rate-control PLUS conversion block'),
    ('Amiodarone', 'Antiarrhythmic that blocks 5-deiodinase'),
])
fill(229, 'I____ is used for thyroid ablation.', '131', aliases=['I131','I-131'])
fill(229, 'I____ is used for thyroid scan.', '123', aliases=['I123','I-123'])
mcq(229, 'Radioactive iodine is used in thyroid carcinoma EXCEPT:',
    'Medullary carcinoma',
    ['Papillary carcinoma','Follicular carcinoma','Anaplastic carcinoma'])
mcq(229, 'Preferred setting for I131 in hyperthyroidism:',
    'Elderly patient or patient with arrhythmia',
    ['First trimester pregnancy',
     'Young child with a hot nodule',
     'Medullary thyroid cancer'])
match(229, 'Match methimazole timing around I131.', [
    ('Stop methimazole', '3 days BEFORE I131'),
    ('Give I131', 'On the treatment day'),
    ('Restart methimazole', '3 days AFTER I131'),
])
fill(229, 'Radioactive iodine is contraindicated in ____.', 'pregnancy')
mcq(229, 'Long-term consequences of I131 include:',
    'Lifelong hypothyroidism and secondary cancers',
    ['Lifelong hyperthyroidism and osteosarcoma',
     'Transient thyroiditis without any hormone change',
     'Cutis aplasia in the treated adult'])

unit('Treatment of Hypothyroidism',
 'Levothyroxine (T4, longer acting) is DOC for replacement — empty stomach 30 min before breakfast; also oral to suppress TSH in thyroid cancer and IV in myxedema coma. Liothyronine (T3, shorter) is used prior to I131 and in myxedema coma as Le+Li+steroid. Levothyroxine S/E: thyrotoxicosis, osteoporosis, AF — decrease dose if arrhythmia.')
fill(229, 'Levothyroxine is the ____ salt and is longer acting.', 'T4')
fill(229, 'Liothyronine is the ____ salt and is shorter acting.', 'T3')
fill(229, 'DOC for replacement in hypothyroidism is ____.', 'levothyroxine', aliases=['LT4','L-thyroxine'])
mcq(229, 'Oral levothyroxine should be taken:',
    'Empty stomach, 30 min before breakfast',
    ['With calcium and breakfast',
     'At bedtime with milk',
     'With an antacid to protect the gut'])
fill(229, 'In thyroid cancer, levothyroxine is used orally to decrease ____.', 'TSH')
fill(229, 'Myxedema coma: levothyroxine is given by the ____ route.', 'IV', aliases=['intravenous'])
mcq(229, 'IV treatment of myxedema coma is:',
    'Levothyroxine + liothyronine + a steroid',
    ['Methimazole + KI + a beta blocker',
     'I131 ablation on day 0',
     'Liothyronine oral only'])
mcq(229, 'If a patient on levothyroxine develops atrial fibrillation:',
    'Decrease the dose',
    ['Increase the dose to suppress TSH harder',
     'Switch to I131',
     'Add amiodarone and continue the same dose'])
finish()

# CHAPTER 58 - ANTI-HISTAMINICS (p230-232) ----------------------------------
start(58)
unit('Histamine Receptors and Effects',
 'Histamine receptors are GPCRs. H1 post-synaptic Gq ↑Ca2+ (allergy/motion); H2 post-synaptic Gs ↑cAMP (peptic ulcer); H3 presynaptic Gi ↓histamine (pitolisant in narcolepsy); H4 leucocyte Gi chemotaxis (no drugs). ↑Ca2+: bronchoconstriction, vasodilation, ↑GI, wakefulness, ↓appetite, itching. ↑cAMP: ↑cardiac contraction/HR and ↑gastric HCl.')
match(230, 'Match each histamine receptor.', [
    ('H1', 'Post-synaptic Gq, ↑Ca2+, allergy / motion sickness'),
    ('H2', 'Post-synaptic Gs, ↑cAMP, peptic ulcer'),
    ('H3', 'Presynaptic Gi, ↓synaptic histamine, narcolepsy (pitolisant)'),
    ('H4', 'Leucocyte Gi, chemotaxis, no drugs yet'),
])
fill(230, 'Histamine receptors are ____ (G protein coupled receptors).', 'GPCRs', aliases=['GPCR'])
fill(230, 'The H3 agonist/inverse-agonist used in narcolepsy to increase wakefulness is ____.', 'pitolisant')
mcq(230, 'Increased Ca2+ (H1) produces all of the following EXCEPT:',
    'Increased gastric HCl secretion',
    ['Bronchoconstriction','Vasodilation','Itching via PNS'])
mcq(230, 'Increased cAMP (H2) in the stomach causes:',
    'Increased HCl release',
    ['Decreased HCl release',
     'PNS-mediated itching',
     'Bronchoconstriction'])

unit('H1 Blockers: Classification',
 '1st gen: less potent, cross BBB (sedating), block muscarinic receptors (preferred as antimuscarinics), C/I elderly/children/pilots/drivers, nausea/vomiting from delayed gastric emptying. 2nd gen: more potent, do not cross BBB (non-sedating), no muscarinic block, preferred as antihistaminics.')
match(230, 'Match 1st vs 2nd generation H1 blockers.', [
    ('1st generation potency / BBB', 'Less potent, cross BBB → sedating'),
    ('2nd generation potency / BBB', 'More potent, do not cross BBB → non-sedating'),
    ('1st generation muscarinic', 'Block muscarinic; preferred as antimuscarinics'),
    ('2nd generation muscarinic', 'Do not block muscarinic; preferred as antihistaminics'),
])
mcq(230, 'First-generation H1 blockers are contraindicated in:',
    'Elderly, children, pilots and drivers',
    ['Patients with peptic ulcer disease',
     'Patients with chronic urticaria',
     'Patients taking a PPI'])
fill(230, 'First-generation H1 blockers cause nausea/vomiting due to delayed ____ emptying.', 'gastric')

unit('First Generation H1 Blockers: Specific Drugs and Uses',
 'Promethazine, diphenhydramine, dimenhydrinate: max antimuscarinic — motion sickness 1 hr before travel, acute dystonia, Meniere vertigo; promethazine/diphenhydramine local anaesthetic; dimenhydrinate insomnia; promethazine chemo NV with α1 hypotension. Doxylamine+B6 (doxinate) DOC morning sickness. Chlorpheniramine least sedating 1st gen (daytime). DOC motion sickness: transdermal scopolamine.')
fill(231, 'General use of 1st-generation H1 blockers is ____ rhinitis (not allergic).', 'non-allergic',
     aliases=['nonallergic','non allergic'])
mcq(231, 'Maximum antimuscarinic 1st-generation drugs are:',
    'Promethazine, diphenhydramine and dimenhydrinate',
    ['Cetirizine, loratadine and fexofenadine',
     'Azelastine, olopatadine and epinastine',
     'Chlorpheniramine, loratadine and desloratadine'])
fill(231, 'For motion sickness, take oral 1st-gen drugs ____ hour before travel.', '1', aliases=['one'])
fill(231, 'DOC for morning sickness is doxylamine + vitamin B6 (____).', 'doxinate')
fill(231, 'The least sedating 1st-generation H1 blocker (preferred daytime) is ____.', 'chlorpheniramine')
fill(231, 'DOC for motion sickness is transdermal ____ patch.', 'scopolamine', aliases=['hyoscine'])
match(231, 'Match the 1st-generation drug with a distinctive use.', [
    ('Dimenhydrinate', 'Insomnia'),
    ('Promethazine', 'Chemotherapy nausea / vomiting (α1 → hypotension)'),
    ('Hydroxyzine', 'Antipruritic, anxiolytic, antiemetic'),
    ('Cyproheptadine', '5-HT2 blocker'),
])
mcq(231, 'Promethazine / diphenhydramine can also be used as a:',
    'Local anaesthetic',
    ['Proton-pump inhibitor','Loop diuretic','MAO inhibitor'])
fill(231, 'Doxepin, used for its H1 block, is a ____ antidepressant.', 'tricyclic', aliases=['TCA'])

unit('Second Generation H1 Blockers and Topical Agents',
 '2nd gen: DOC urticaria; add-on for allergic rhinitis (hay fever DOC = steroids). Cetirizine = hydroxyzine derivative, most sedating 2nd gen; levocetirizine more potent / lower dose. Astemizole & terfenadine: QT / torsades → banned. Fexofenadine (terfenadine derivative): no QT, least sedating. Desloratadine (loratadine metabolite): most potent. Rupatadine blocks PAF. Topical: azelastine, epinastine, alcaftadine, levocarbastine, olopatadine.')
fill(231, 'DOC for urticaria is a ____-generation H1 blocker.', 'second', aliases=['2nd','2nd generation'])
mcq(231, 'Hay fever (allergic rhinitis) disease-modifying DOC is:',
    'A steroid (2nd-gen H1 blockers are only supplements)',
    ['A 1st-generation H1 blocker as monotherapy',
     'A 2nd-generation H1 blocker as monotherapy',
     'Scopolamine patch'])
fill(231, 'Cetirizine is a ____ derivative and the most sedating 2nd-gen drug.', 'hydroxyzine')
fill(231, 'The least sedating antihistaminic is ____.', 'fexofenadine')
fill(231, 'The most potent antihistaminic (loratadine metabolite) is ____.', 'desloratadine',
     aliases=['desloratidine'])
mcq(231, 'Astemizole and terfenadine were banned because they:',
    'Prolong QT and cause torsades',
    ['Cause agranulocytosis',
     'Cause interstitial nephritis',
     'Are too sedating'])
fill(231, 'Fexofenadine is a ____ derivative with no QT prolongation.', 'terfenadine')
fill(231, 'Rupatadine also blocks platelet-activating factor, adding an ____ effect.', 'anti-inflammatory',
     aliases=['antiinflammatory'])
mcq(231, 'Topical antihistaminics (azelastine, olopatadine, etc.) are used for:',
    'Allergic rhinitis and allergic conjunctivitis',
    ['Peptic ulcer and motion sickness',
     'Urticaria as first-line oral DOC',
     'Narcolepsy'])

unit('Bradykinin and Hereditary Angioedema',
 'Kininogen —kallikrein→ kallidin / bradykinin → B1/B2 → ↑PG (pain, inflammation) and ↑NO (vasodilation). Kallikrein antagonists: aprotinin, lanadelumab, berotralstat, ecallantide. Icatibant blocks B2. Aprotinin also blocks plasmin (antifibrinolytic) after CABG. HAE Rx DOC: C1 esterase; alts icatibant & ecallantide. Prophylaxis DOC danazol; alts lanadelumab & berotralstat; pre-surgery EACA.')
match(232, 'Match the bradykinin pathway piece.', [
    ('Kallikrein', 'Converts kininogen → kallidin / bradykinin'),
    ('Bradykinin B1/B2', '↑ prostaglandins and nitric oxide'),
    ('Prostaglandins', 'Pain and inflammation'),
    ('Nitric oxide', 'Vasodilation'),
])
fill(232, 'Icatibant blocks the bradykinin ____ receptor.', 'B2', aliases=['bradykinin 2','BK2'])
fill(232, 'Aprotinin inhibits plasmin, giving an ____ effect useful after CABG.', 'antifibrinolytic')
fill(232, 'Hereditary angioedema treatment DOC is ____ inhibitor replacement.', 'C1 esterase',
     aliases=['C1-INH','C1 esterase inhibitor','C1 INH'])
match(232, 'Match hereditary angioedema strategy with the drug.', [
    ('Acute Rx alternatives', 'Icatibant and ecallantide'),
    ('Prophylaxis DOC', 'Danazol'),
    ('Prophylaxis alternatives', 'Lanadelumab and berotralstat'),
    ('Pre-surgery', 'EACA (epsilon-aminocaproic acid)'),
])
finish()

# CHAPTER 59 - SEROTONIN-RELATED DRUGS (p233-236) ---------------------------
start(59)
unit('Serotonin Receptors and 5-HT1A Agonists',
 'Seven 5-HT types; all GPCRs except 5-HT3 (ion channel). 5-HT1A: presynaptic serotonergic, Gi — buspirone, epsapirone, gepirone — non-benzo anxiolytics that decrease 5-HT2 activity.')
fill(233, 'There are ____ types of serotonin receptor (5-HT1 to 5-HT7).', '7', aliases=['seven'])
fill(233, 'All 5-HT receptors are GPCRs except 5-HT____, which is an ion channel.', '3')
fill(233, '5-HT1A agonists used as non-benzodiazepine anxiolytics include ____, epsapirone and gepirone.', 'buspirone')
mcq(233, '5-HT1A agonists reduce anxiety by decreasing central:',
    '5-HT2 activity',
    ['5-HT3 ion current only',
     'Dopamine D2 occupancy only',
     'GABA-A chloride current'])

unit('5-HT1B/1D/1F, CGRP Pathway and Migraine Biology',
 '5-HT1B/1D/1F sit on CN V (Gi). Migraine: trigeminal axon releases CGRP → meningeal vessel dilation, edema, compression, headache. Lasmiditan = 5-HT1F at the nucleus; triptans = 5-HT1B/1D on the axon (↓CGRP). CGRP ligand mAbs (parenteral prophylaxis); CGRP receptor blockers (erenumab/atogepant PO prophylaxis; rimegepant PO acute).')
match(233, 'Match the migraine target.', [
    ('Triptans', '5-HT1B/1D on the axon → ↓ CGRP release'),
    ('Lasmiditan', '5-HT1F agonist at CN V nucleus'),
    ('Eptinezumab / fremanezumab / galcanezumab', 'CGRP ligand blockers, parenteral prophylaxis'),
    ('Rimegepant', 'CGRP receptor blocker, oral acute attack'),
])
fill(233, 'CGRP acts on meningeal blood vessels causing dilation, edema and ____.', 'headache',
     aliases=['migraine','migraine headache'])
mcq(233, 'Erenumab and atogepant are taken:',
    'Orally for migraine prophylaxis',
    ['Parenterally for prophylaxis',
     'Orally only for acute attack',
     'As triptan substitutes in IHD'])
fill(233, 'Triptans are approved for ____ treatment of migraine (not prophylaxis).', 'acute')

unit('Triptans for Acute Migraine: Pharmacokinetics and Drugs',
 'Triptans stimulate 5-HT1B → ↓CGRP + vasoconstriction. They differ in PK more than PD; absorption rate ∝ efficacy/potency. Frovatriptan 27 h, naratriptan 6 h — slow oral, long/slow, prolonged attack. Fast oral: rizatriptan (fastest oral), sumatriptan, zolmitriptan, eletriptan, almotriptan — preferred for acute attack. Nasal: zolmitriptan, sumatriptan. Overall fastest: S/C or rectal sumatriptan.')
fill(234, 'Triptans differ more in pharmacokinetics than in ____.', 'pharmacodynamics', aliases=['PD'])
fill(234, 'Rate of absorption of a triptan is proportional to its ____ and potency.', 'efficacy')
fill(234, 'Frovatriptan acts for ____ hours.', '27', aliases=['27 hrs','27 h'])
fill(234, 'Naratriptan acts for ____ hours.', '6', aliases=['6 hrs','6 h'])
mcq(234, 'Frovatriptan and naratriptan are preferred for:',
    'A prolonged attack (slow oral absorption, long acting)',
    ['The fastest possible abortive effect',
     'Patients with IHD because they do not vasoconstrict',
     'Migraine prophylaxis instead of propranolol'])
fill(234, 'The fastest-acting ORAL triptan is ____.', 'rizatriptan')
fill(234, 'Overall fastest triptan is subcutaneous / rectal ____.', 'sumatriptan')
mcq(234, 'Nasal-spray triptans are:',
    'Zolmitriptan and sumatriptan',
    ['Frovatriptan and naratriptan',
     'Eletriptan and almotriptan',
     'Rizatriptan nasal spray alone'])

unit('Triptans: Side Effects and Contraindications',
 'Coronary vasoconstriction → chest pain, jaw/neck pain, sweating, arrhythmia. C/I: IHD (MI/angina), stroke/TIA, ischemic bowel, HTN/PVD (Raynaud/Buerger). Naratriptan: liver/renal failure. Eletriptan: liver failure. Zolmitriptan: WPW.')
mcq(234, 'The chest pain of triptans is due to:',
    'Coronary vasoconstriction',
    ['Coronary vasodilation',
     'CGRP-mediated meningeal edema',
     '5-HT3-mediated vagal surge'])
match(234, 'Match the triptan-specific contraindication.', [
    ('Naratriptan', 'Liver or renal failure'),
    ('Eletriptan', 'Liver failure'),
    ('Zolmitriptan', 'WPW syndrome'),
    ('All triptans', 'IHD, stroke/TIA, ischemic bowel, HTN/PVD'),
])

unit('Other Acute Migraine Drugs and Pregnancy Management',
 'Acute: lasmiditan, rimegepant, ergotamine (nonselective, gangrene of end-arteries — feet m/c), DHE (less potent, better tolerated, same C/I), D2 blockers, paracetamol (mild-moderate), ketorolac (severe), butorphanol/codeine. Pregnancy: paracetamol → codeine/caffeine/metoclopramide → sumatriptan (triptan of choice); triptans may block placental flow.')
fill(235, 'Ergotamine is a non-selective 5-HT agonist and a very potent ____.', 'vasoconstrictor')
fill(235, 'Ergotamine gangrene of end-arteries is most common in the ____.', 'feet', aliases=['foot'])
fill(235, 'Pregnancy DOC for migraine is ____.', 'paracetamol', aliases=['acetaminophen'])
fill(235, 'Triptan of choice in pregnancy (if needed) is ____.', 'sumatriptan')
mcq(235, 'If paracetamol fails in pregnancy migraine, next is:',
    'Codeine / caffeine / metoclopramide',
    ['Ergotamine immediately',
     'Frovatriptan for a prolonged attack',
     'Methysergide prophylaxis'])
mcq(235, 'Dihydroergotamine compared with ergotamine is:',
    'Less potent, better tolerated, same S/E and C/I as triptans',
    ['More potent, poorly tolerated, and safe to use in IHD',
     'A selective 5-HT1F agonist used like lasmiditan',
     'Reserved for migraine prophylaxis rather than acute attacks'])
fill(235, 'NSAID for a severe migraine attack is ____.', 'ketorolac')

unit('Migraine Prophylaxis and 5-HT2 Drugs',
 'Mnemonic Flunarizine Can PREVENT. DOC: pizotifen/propranolol. Cyproheptadine: H1 + muscarinic block — migraine prophylaxis, serotonin syndrome, carcinoid, cold urticaria, AIDS weight gain. Methysergide: fibrosis (pulmonary, cardiac, retroperitoneal). Flibanserin: 5-HT2A antagonist + 5-HT1A agonist for HSDD. Lorcaserin (obesity) banned for cancer.')
fill(235, 'Migraine-prophylaxis mnemonic: Flunarizine Can ____ migraine.', 'PREVENT')
fill(235, 'DOC for migraine prophylaxis is pizotifen / ____.', 'propranolol')
mcq(235, 'Cyproheptadine uses include all EXCEPT:',
    'Acute abortive treatment of migraine',
    ['Migraine prophylaxis',
     'Serotonin syndrome and carcinoid',
     'Cold urticaria and AIDS weight gain'])
fill(235, 'Methysergide causes ____ (pulmonary, cardiac, retroperitoneal).', 'fibrosis')
fill(235, 'Flibanserin (5-HT2A antagonist + 5-HT1A agonist) treats ____ in females.', 'HSDD',
     aliases=['hypoactive sexual desire disorder'])
fill(235, 'Lorcaserin (obesity) was banned because of increased ____ risk.', 'cancer')

unit('Obesity Treatment and Banned Drugs',
 'Anorexia: liraglutide, phentermine. Lipolysis inhibitor: orlistat. Lipolysis stimulator: mirabegron. Unknown: topiramate, naltrexone, bupropion. 5-HT3 antagonists = antiemetics; 5-HT4 agonists = prokinetics. Banned: rimonabant (suicide), lorcaserin (cancer), phenylpropanolamine (stroke), sibutramine (MI).')
match(236, 'Match the anti-obesity mechanism.', [
    ('Liraglutide / phentermine', 'Cause anorexia'),
    ('Orlistat', 'Inhibits lipolysis (fat absorption)'),
    ('Mirabegron', 'Stimulates lipolysis'),
    ('Topiramate / naltrexone / bupropion', 'Unknown / mixed mechanisms'),
])
match(236, 'Match the banned weight-loss drug with why it was withdrawn.', [
    ('Rimonabant', 'Increased suicidal tendency'),
    ('Lorcaserin', 'Cancer'),
    ('Phenylpropanolamine', 'Stroke'),
    ('Sibutramine', 'Myocardial infarction'),
])
fill(236, '5-HT3 antagonists are ____; 5-HT4 agonists are prokinetics.', 'antiemetics')
finish()

# CHAPTER 60 - EICOSANOIDS (p237-241) ----------------------------------------
start(60)
unit('Eicosanoid Synthesis and Inhibitors',
 'Arachidonic acid —COX I/II→ PG (pain, pyrexia, inflammation) and TXA2 (platelet aggregation); —5-LOX→ LTC4/D4 (bronchoconstrictors). NSAIDs reversible except aspirin (irreversible). Zileuton blocks 5-LOX; montelukast/zafirlukast block LT receptors.')
match(237, 'Match the arachidonic-acid product.', [
    ('Prostaglandins', 'Pain, pyrexia, inflammation'),
    ('Thromboxane A2', 'Platelet aggregation'),
    ('LTC4 / LTD4', 'Bronchoconstriction'),
    ('COX vs LOX', 'Cyclooxygenase vs lipoxygenase'),
])
fill(237, 'NSAIDs inhibit COX reversibly except ____, which is irreversible.', 'aspirin')
fill(237, 'Zileuton inhibits ____.', '5-LOX', aliases=['5-lipoxygenase','5 lipoxygenase','five-LOX'])
mcq(237, 'Montelukast / zafirlukast block:',
    'Leukotriene C4/D4 receptors',
    ['COX-1 irreversibly',
     '5-LOX enzyme itself',
     'Thromboxane synthase'])

unit('Prostaglandin E1 and E2 Analogs',
 'PGE1 keeps the ductus arteriosus patent. Misoprostol: NSAID gastric ulcer, abortion, PPH (least effective). Alprostadil: ED. Sildenafil is DOC for ED. PGE2 dinoprostone: PPH and cervical ripening DOC.')
fill(237, 'A common use of prostaglandin E1 is to maintain patency of the ____.', 'ductus arteriosus',
     aliases=['PDA','patent ductus arteriosus'])
fill(237, 'The least effective drug for PPH among PG analogs is ____.', 'misoprostol')
fill(237, 'Alprostadil is a PGE1 analog used for ____.', 'erectile dysfunction', aliases=['ED'])
fill(237, 'DOC for erectile dysfunction is ____.', 'sildenafil')
fill(237, 'Dinoprostone is prostaglandin ____.', 'E2', aliases=['PGE2'])
fill(237, 'DOC for cervical ripening is ____.', 'dinoprostone')
mcq(237, 'Misoprostol uses include:',
    'NSAID gastric ulcer, abortion, and PPH (least effective)',
    ['Open-angle glaucoma as eye drops',
     'Pulmonary hypertension as an infusion',
     'PDA closure in a neonate'])

unit('Prostaglandin I2, F2α and Other PHTN Drugs',
 'PGI2: pulmonary HTN (vasodilation) — epoprostenol (recombinant), iloprost/beraprost/treprostinil (analogs), selexipag (receptor agonist). Endothelin antagonists: bosentan, ambrisentan. PGF2α: carboprost (PPH, abortion); latanoprost/bimatoprost eye drops DOC open-angle / normal-tension glaucoma. S/E: heterochromia, sandy eyes, macular edema, hypertrichosis (used for hypotrichosis). C/I uveitis.')
fill(237, 'Epoprostenol is recombinant prostaglandin ____.', 'I2', aliases=['PGI2','prostacyclin'])
fill(237, 'Selexipag is a PGI2 ____ agonist.', 'receptor')
mcq(237, 'Endothelin antagonists used in pulmonary HTN are:',
    'Bosentan and ambrisentan',
    ['Sildenafil and tadalafil only',
     'Latanoprost and bimatoprost',
     'Misoprostol and dinoprostone'])
fill(237, 'Carboprost (PGF2α) is used for PPH and ____.', 'abortion')
fill(237, 'Latanoprost / bimatoprost are DOC for ____-angle and normal-tension glaucoma.', 'open')
mcq(237, 'PGF2α eye-drop side effects include all EXCEPT:',
    'Uveitis as a desired therapeutic effect',
    ['Heterochromia iridis',
     'Dry / sandy eyes and macular edema',
     'Hypertrichosis (exploited in hypotrichosis)'])
fill(237, 'PGF2α eye drops are contraindicated in ____.', 'uveitis')

unit('Non-Selective COX Inhibitors: Paracetamol',
 'Paracetamol: COX I/II ↓PG (analgesia, antipyrexia, poor anti-inflammatory) + TRPV1 and cannabinoid receptors. M/c drug-induced liver failure via NAPQI depleting glutathione → centrilobular necrosis + periportal sparing. M/c drug poisoning. Toxic 150–250 mg/kg or >10 g; fatal >20 g. Rumack-Matthew nomogram. <4 h charcoal; DOC NAC; failure → transplant.')
mcq(238, 'Paracetamol anti-inflammatory effect is:',
    'Poor, despite COX I/II inhibition',
    ['Equal to high-dose aspirin',
     'Stronger than indomethacin',
     'Absent because it only blocks LOX'])
fill(238, 'The hepatotoxic paracetamol metabolite is ____.', 'NAPQI')
fill(238, 'NAPQI depletes ____, the free-radical scavenger.', 'glutathione', aliases=['GSH'])
mcq(238, 'Paracetamol liver histology is:',
    'Centrilobular necrosis with periportal sparing',
    ['Periportal necrosis with centrilobular sparing',
     'Panlobular caseating granulomas',
     'Macrovesicular steatosis only'])
fill(238, 'Paracetamol is the most common cause of drug ____ and of drug-induced liver failure.', 'poisoning')
fill(238, 'Toxic paracetamol dose is 150–250 mg/kg or > ____ g.', '10')
fill(238, 'Fatal paracetamol dose is > ____ g.', '20')
fill(238, 'Hepatotoxicity is predicted with the ____ Mathew nomogram.', 'Rumack', aliases=['Rumack-Matthew','Rumack Matthew'])
fill(238, 'Within 4 hours of paracetamol ingestion give ____.', 'charcoal', aliases=['activated charcoal'])
fill(238, 'DOC for paracetamol poisoning is ____.', 'N-acetyl cysteine',
     aliases=['NAC','N acetylcysteine','n-acetylcysteine'])
mcq(238, 'If NAC fails and fulminant hepatic failure develops:',
    'Emergency liver transplant',
    ['Repeat charcoal every hour',
     'Hemodialysis as first-line antidote',
     'Switch to fomepizole'])

unit('Aspirin: Dose Dependent Effects and Uses',
 '50–325 mg OD antiaggregant; 325–650 mg SOS analgesic/antipyretic; 3–4 g/day anti-inflammatory. Uses include RA, rheumatic fever, niacin flushing DOC, essential thrombocythemia, Kawasaki, ↓ colon cancer. S/E: bleeding m/c; Reye; salicylism >10 g (seizures, tinnitus, hyperglycemia, metabolic acidosis) — symptomatic ± dialysis. C/I: viral fever in children, gout, warfarin.')
match(239, 'Match the aspirin dose with the effect.', [
    ('50–325 mg OD', 'Antiaggregant'),
    ('325–650 mg SOS (max 4/day)', 'Analgesic and antipyretic'),
    ('3–4 g/day divided', 'Anti-inflammatory'),
])
fill(239, 'DOC for niacin-induced flushing is ____.', 'aspirin')
fill(239, 'Most common side effect of aspirin is ____.', 'bleeding')
mcq(239, 'Reye syndrome is:',
    'Viral fever in a child + aspirin → hepatic encephalopathy',
    ['Gout flare from decreased urate excretion',
     'Tinnitus and metabolic acidosis after 10 g',
     'Colon-cancer chemoprevention'])
fill(239, 'Salicylism occurs at doses > ____ g.', '10')
mcq(239, 'Clinical features of salicylism include:',
    'Seizures, tinnitus, hyperglycemia and metabolic acidosis',
    ['Bradycardia, hypothermia and metabolic alkalosis',
     'Cinchonism without acid-base change',
     'Isolated bleeding with a normal anion gap'])
mcq(239, 'Aspirin is contraindicated in all EXCEPT:',
    'Kawasaki disease',
    ['Viral fever in children',
     'Gout (decreases uric acid excretion)',
     'Combination with warfarin (↑ bleeding)'])

unit('Other Non-Selective NSAIDs: Indomethacin to Ketorolac',
 'Indomethacin: COX + PLA/C + leucocyte migration; DOC acute gout, Bartter, paroxysmal hemicrania; frontal headache. Sulindac: FAP / colon, breast, prostate cancer risk ↓. Ibuprofen: PDA closure DOC in India (worldwide DOC indomethacin); aseptic meningitis, toxic amblyopia. Ketoprofen also blocks LOX. Flurbiprofen eye drops prevent intra-op miosis. Piroxicam enterohepatic, longest, slow, chronic pain. Ketorolac high potency — acute pain, nasal migraine, ocular drops.')
mcq(240, 'Indomethacin is DOC for acute gout partly because it also:',
    'Inhibits phospholipase A & C and leucocyte migration',
    ['Irreversibly acetylates COX-1 only',
     'Inhibits xanthine oxidase',
     'Blocks IL-1 release via microtubules'])
fill(240, 'A distinctive indomethacin side effect is ____ headache.', 'frontal')
fill(240, 'Sulindac reduces risk of colon carcinoma in ____ (familial adenomatous polyposis).', 'FAP')
fill(240, 'DOC for PDA closure in India is ____; worldwide DOC is indomethacin.', 'ibuprofen')
fill(240, 'Ibuprofen is the most common drug causing aseptic ____.', 'meningitis')
mcq(240, 'Piroxicam is longest-acting among these NSAIDs because of:',
    'Enterohepatic circulation (slow onset → chronic pain)',
    ['Irreversible COX acetylation',
     'Concentration inside joints despite a short T1/2',
     'Renal tubular secretion that saturates'])
fill(240, 'Flurbiprofen eye drops are used to prevent intra-operative ____.', 'miosis')
mcq(240, 'Ketorolac is used as:',
    'Oral/parenteral acute pain, intranasal migraine, ocular drops',
    ['Once-daily chronic-pain NSAID like piroxicam',
     'DOC for PDA closure worldwide',
     'First-line disease-modifying drug in RA'])

unit('Diclofenac, Naproxen and Selective COX II Inhibitors',
 'Diclofenac: short T1/2 but long acting (joints); hepatotoxic, GI ulcers ↓ by misoprostol combo. Nabumetone: non-acidic, long, OD. COX-2: celecoxib, etoricoxib oral; parecoxib IV post-op. 3rd-line for pain. S/E: hypersensitivity rash m/c, renal papillary necrosis, cardiotoxicity (rofecoxib, valdecoxib). Ulcer: non-selective > selective; DOC PPIs. Interactions: ↓ antihypertensives, ↓ lithium clearance, ↓ furosemide.')
fill(241, 'Diclofenac has a short T1/2 but is long-acting because it concentrates in ____.', 'joints')
fill(241, 'GI ulcers from diclofenac are reduced by combining it with ____.', 'misoprostol')
fill(241, 'Nabumetone is a non-acidic, long-acting naproxen derivative given ____.', 'OD',
     aliases=['once daily','once a day'])
fill(241, 'Parenteral selective COX-2 inhibitor for post-op pain is ____.', 'parecoxib')
mcq(241, 'Cardiotoxic COX-2 inhibitors that were withdrawn include:',
    'Rofecoxib and valdecoxib',
    ['Celecoxib and parecoxib',
     'Etoricoxib and nabumetone',
     'Indomethacin and sulindac'])
fill(241, 'Most common side effect of selective COX-2 inhibitors is hypersensitivity ____.', 'rash')
fill(241, 'Nephrotoxicity of COX-2 inhibitors is renal ____ necrosis.', 'papillary')
mcq(241, 'Peptic-ulcer risk is:',
    'Higher with non-selective NSAIDs than with COX-2 inhibitors',
    ['Higher with COX-2 inhibitors than with non-selective NSAIDs',
     'Equal for both classes',
     'Absent if a PPI is not co-prescribed'])
fill(241, 'DOC for NSAID-induced peptic ulcer is a ____.', 'PPI', aliases=['PPIs','proton pump inhibitor'])
mcq(241, 'Selective COX-2 inhibitors can cause lithium toxicity because they:',
    'Decrease lithium clearance',
    ['Induce CYP3A4',
     'Increase lithium absorption via P-gp block',
     'Displace lithium from albumin'])
finish()
# CHAPTER 61 - GOUT (p242-243) -----------------------------------------------
start(61)
unit('Acute Gout: Aim and Drugs',
 'Acute gout aims to decrease inflammation and give symptomatic relief — not to lower uric acid yet. NSAIDs first; if no response, a steroid. DOC is indomethacin (multiple MOAs). Colchicine inhibits microtubules → chemotaxis/migration of leucocytes, ↓IL-1 from neutrophils, and phagocytosis. S/E: nausea, vomiting, diarrhoea, marrow suppression, alopecia.')
mcq(242, 'The aim of ACUTE gout treatment is:',
    'Decrease inflammation and give symptomatic relief',
    ['Lower uric acid with a xanthine-oxidase inhibitor on day 1',
     'Increase uric acid excretion with a uricosuric on day 1',
     'Give pegloticase as first-line'])
fill(242, 'DOC for acute gout is ____ (multiple mechanisms of action).', 'indomethacin')
mcq(242, 'If NSAIDs fail in an acute flare, next is a:',
    'Steroid',
    ['Xanthine oxidase inhibitor','Uricosuric','Uricase analog'])
fill(242, 'Colchicine inhibits ____, thereby blocking leucocyte chemotaxis and migration.', 'microtubules')
mcq(242, 'Colchicine also:',
    'Decreases IL-1 release from neutrophils and inhibits phagocytosis',
    ['Inhibits xanthine oxidase',
     'Blocks URAT1 in the proximal tubule',
     'Converts uric acid to allantoin'])
mcq(242, 'Colchicine side effects include:',
    'Nausea, vomiting, diarrhoea, marrow suppression and alopecia',
    ['SJS with HLA-B*5801 and orotic aciduria',
     'Xanthine stones and cardiovascular death',
     'Hemolysis in G6PD deficiency and methemoglobinemia'])

unit('Chronic Gout: Aim and Classification',
 'Chronic gout aims to prevent acute attacks by lowering uric acid: inhibit synthesis (XO inhibitors), increase excretion (uricosurics), or increase metabolism (uricase analogs).')
match(242, 'Match the chronic-gout strategy.', [
    ('Xanthine oxidase inhibitors', 'Decrease uric acid synthesis'),
    ('Uricosuric drugs', 'Increase uric acid excretion'),
    ('Uricase analogs', 'Increase uric acid metabolism'),
])

unit('Xanthine Oxidase Inhibitors: Allopurinol',
 'Allopurinol is DOC for chronic gout, tumor lysis, Lesch-Nyhan and organ transplant. Hypersensitivity m/c = SJS (HLA-B*5801); also orotidylate decarboxylase block → orotic aciduria, and DRESS. Class: xanthinuria → xanthine stones; acute gout flare prevented with NSAID/colchicine 3–6 months. Interaction: ↑ 6-MP / azathioprine toxicity.')
fill(242, 'DOC for chronic gout, tumor lysis, Lesch-Nyhan and organ transplant is ____.', 'allopurinol')
fill(242, 'Allopurinol SJS is associated with HLA-B*____.', '5801', aliases=['HLA-B-5801','HLA-B5801'])
fill(242, 'Allopurinol inhibits orotidylate decarboxylase causing ____ aciduria.', 'orotic')
fill(242, 'Allopurinol can cause ____ syndrome (drug rash with eosinophilia).', 'DRESS')
mcq(242, 'Xanthine oxidase inhibitors can cause stones of:',
    'Xanthine',
    ['Urate only','Cystine','Calcium oxalate only'])
fill(242, 'Prevent the early acute-gout flare on XO inhibitors with NSAID/colchicine for ____ months.', '3-6',
     aliases=['3–6','3 to 6'])
mcq(242, 'Allopurinol increases toxicity of:',
    '6-mercaptopurine / azathioprine',
    ['Methotrexate / pemetrexed',
     'Cyclophosphamide / ifosfamide',
     'Probenecid / sulfinpyrazone'])

unit('Xanthine Oxidase Inhibitors: Oxypurinol and Febuxostat',
 'Oxypurinol is an orphan drug for allopurinol hypersensitivity. Febuxostat is for intolerance or inadequate response; S/E increased cardiovascular death.')
fill(243, 'The orphan drug used in allopurinol hypersensitivity is ____.', 'oxypurinol')
fill(243, 'Febuxostat is used when allopurinol is not tolerated or the response is ____.', 'inadequate',
     aliases=['inadequate response'])
fill(243, 'Febuxostat increases the risk of ____ death.', 'cardiovascular', aliases=['CV','cardiac'])

unit('Uricosuric Drugs',
 'Probenecid and sulfinpyrazone: add-on > monotherapy. Benzbromarone and lesinurad: most effective, add-on only, usable in mild–moderate renal failure. S/E: urate stones (C/I previous stones), calcium stones, precipitate acute gout. Comorbid add-ons: losartan (HTN), atorvastatin (↑LDL), fenofibrate (↑TG).')
match(243, 'Match the uricosuric with how it is used.', [
    ('Probenecid / sulfinpyrazone', 'Add-on therapy better than monotherapy'),
    ('Benzbromarone / lesinurad', 'Most effective; add-on only; OK in mild–moderate CKD'),
    ('History of renal stones', 'Contraindication (urate + calcium stones)'),
])
mcq(243, 'Uricosurics may precipitate acute gout, so:',
    'Preventive prophylaxis is needed',
    ['They are therefore first-line in acute gout',
     'They should be combined with pegloticase on day 1',
     'No NSAID cover is required'])
match(243, 'Match the comorbid chronic-gout add-on.', [
    ('Losartan', 'When the patient also has hypertension'),
    ('Atorvastatin', 'When LDL / cholesterol is high'),
    ('Fenofibrate', 'When triglycerides are high'),
])

unit('Uricase Analogues',
 'Humans have no uricase. Pegloticase: resistant gout, IV every 2 weeks. Rasburicase: DOC high-risk tumor lysis (leukemia, especially CLL). S/E: hemolysis in G6PD deficiency and methemoglobinemia.')
fill(243, 'Humans have ____ uric acid metabolism via uricase.', 'no', aliases=['no uricase','absent'])
fill(243, 'Resistant gout can be treated with IV ____ every 2 weeks.', 'pegloticase')
fill(243, 'DOC for high-risk tumor lysis (e.g. CLL) is ____.', 'rasburicase')
mcq(243, 'Uricase analog side effects include:',
    'Hemolysis in G6PD deficiency and methemoglobinemia',
    ['SJS with HLA-B*5801 and orotic aciduria',
     'Xanthine stones and cardiovascular death',
     'Bull’s-eye maculopathy'])
finish()

# CHAPTER 62 - RHEUMATOID ARTHRITIS (p244-246) -------------------------------
start(62)
unit('Acute Flare and Long Term Management Principles',
 'Mild–moderate flare: NSAIDs (aspirin, diclofenac > celecoxib). Severe / NSAID-unresponsive: steroids — 1–2 joints intra-articular triamcinolone; >2 joints oral prednisolone. Long-term DMARDs: conventional, biological, JAK inhibitors. All immunosuppress; do not combine.')
mcq(244, 'Mild–moderate acute RA flare is treated with:',
    'NSAIDs (aspirin, diclofenac > celecoxib)',
    ['Immediate JAK inhibitor monotherapy',
     'Intra-articular triamcinolone as first step',
     'TNF inhibitor plus methotrexate on day 1'])
fill(244, 'For 1–2 joints in a severe flare use intra-articular ____.', 'triamcinolone')
fill(244, 'For >2 joints in a severe flare use oral ____.', 'prednisolone')
match(244, 'Match the DMARD class with examples.', [
    ('Conventional', 'Methotrexate, HCQ, sulfasalazine, leflunomide…'),
    ('Biological', 'TNF / IL-1 / IL-6 / CD20 / abatacept'),
    ('JAK inhibitors', 'Tofacitinib, baricitinib, upadacitinib'),
])
mcq(244, 'DMARDs should not be combined because they all:',
    'Immunosuppress and raise infection risk',
    ['Share identical hepatotoxicity that is always additive',
     'Antagonize methotrexate intracellularly',
     'Are pregnancy category X together'])

unit('Methotrexate and Treatment Algorithm',
 'Methotrexate is the anchor / DOC for new RA; anti-inflammatory effect in 2–4 weeks. Inadequate at 3–6 months: add HCQ+sulfasalazine OR abatacept OR a biologic; if biologic fails → another biologic or JAK. MTX inhibits DHFR → ↓THF → ↓purine → lymphocyte toxicity; ↑adenosine (anti-inflammatory) but also hepatic fibrosis. Monitor ALT/AST q3–6 months. Also crystalluria and marrow suppression.')
fill(244, 'The anchor drug and DOC for newly diagnosed RA is ____.', 'methotrexate')
fill(244, 'Anti-inflammatory effect of methotrexate appears in ____ weeks.', '2-4', aliases=['2–4','2 to 4'])
mcq(244, 'If methotrexate is inadequate after 3–6 months, add:',
    'HCQ + sulfasalazine, OR abatacept, OR a biological DMARD',
    ['A higher NSAID dose alone',
     'Lifelong intra-articular triamcinolone',
     'Pegloticase'])
fill(244, 'Methotrexate inhibits ____, lowering THF and purine synthesis.', 'DHFR',
     aliases=['dihydrofolate reductase'])
fill(244, 'Increased ____ from methotrexate contributes to the anti-inflammatory effect.', 'adenosine')
fill(244, 'Monitor ALT/AST every ____ months on methotrexate.', '3-6', aliases=['3–6','3 to 6'])
mcq(244, 'Methotrexate nephrotoxicity presents as:',
    'Crystalluria',
    ['Minimal-change nephropathy',
     'Papillary necrosis',
     'ATN from myoglobin'])
fill(244, 'THF stands for ____.', 'tetrahydrofolate')

unit('Conventional DMARDs: Hydroxychloroquine and Sulfasalazine',
 'HCQ: inhibits lymphocyte proliferation, stabilizes lysosomes; mild = monotherapy, moderate–severe = add-on. S/E bull’s-eye retinopathy; max ≤5 mg/kg/day; yearly ophthalmology. Sulfasalazine → 5-ASA (not absorbed, UC) + sulfonamide (lymphocyte inhibition; mild RA mono, moderate–severe add-on).')
fill(245, 'Hydroxychloroquine retinopathy is a ____-eye maculopathy.', "bull's-eye",
     aliases=['bull eye','bulleye','bulls-eye','bull’s eye'])
fill(245, 'Keep hydroxychloroquine ≤ ____ mg/kg/day and see ophthalmology yearly.', '5')
match(245, 'Match hydroxychloroquine use by RA severity.', [
    ('Mild RA', 'Hydroxychloroquine monotherapy'),
    ('Moderate–severe RA', 'Hydroxychloroquine as add-on'),
    ('Ophthalmology', 'Once yearly'),
])
fill(245, 'Sulfasalazine splits in the gut into 5-ASA (not absorbed) and a ____.', 'sulfonamide')
fill(245, 'Unabsorbed 5-ASA is used for ____ colitis.', 'ulcerative')
mcq(245, 'The sulfonamide moiety of sulfasalazine in RA:',
    'Inhibits lymphocyte proliferation (mono in mild, add-on in moderate–severe)',
    ['Is the piece used for ulcerative colitis',
     'Is a JAK inhibitor',
     'Depletes B cells via CD20'])

unit('Biological DMARDs and Side Effects',
 'TNF-α: infliximab, adalimumab, certolizumab, etanercept, golimumab (IV/SC). Mnemonic Alpha Inhibitors Prevent RA — AS, IBD, psoriatic arthritis, plaque psoriasis, RA. S/E: GI ulcers/perforation, infection, secondary skin cancers. C/I: hepatitis B reactivation, CHF. IL-6: tocilizumab, sarilumab (RA, COVID cytokine storm). Anakinra (IL-1) least effective. Rituximab CD20; abatacept CD80/86; belatacept GVHD.')
mcq(245, 'TNF-α inhibitors (infliximab, adalimumab, certolizumab, etanercept, golimumab) are given:',
    'IV or subcutaneous',
    ['Orally as a once-daily tablet','Intramuscular depot monthly','As eye drops for uveitis'])
fill(245, 'TNF-inhibitor mnemonic: Alpha Inhibitors Prevent ____.', 'RA')
mcq(245, 'TNF-α inhibitor contraindications include:',
    'Hepatitis B (reactivation) and congestive heart failure',
    ['Mild RA as the only approved use',
     'Ulcerative colitis',
     'Ankylosing spondylitis'])
fill(245, 'IL-6 inhibitors tocilizumab and sarilumab are also used for cytokine storm in ____.', 'COVID-19',
     aliases=['COVID','covid19'])
fill(245, 'The least effective / least preferred biological is the IL-1 blocker ____.', 'anakinra')
fill(245, 'Abatacept inhibits CD80/86 and therefore ____-cell activation.', 'T')
fill(245, 'Belatacept (related to abatacept) is used for ____ versus host disease.', 'graft',
     aliases=['GVHD','graft vs host','graft-versus-host'])

unit('JAK Inhibitors',
 'JAK inhibitors block cytokine function. Baricitinib: RA. Upadacitinib: RA, PsA, atopic dermatitis. Ruxolitinib: GVHD, myelofibrosis, PV unresponsive to hydroxyurea. Abrocitinib: atopic dermatitis. Tofacitinib: PsA, UC, JIA, AS, RA.')
fill(246, 'JAK inhibitors work by blocking the function of ____.', 'cytokines')
match(246, 'Match the JAK inhibitor with a headline use.', [
    ('Baricitinib', 'Rheumatoid arthritis'),
    ('Ruxolitinib', 'GVHD, myelofibrosis, PV failing hydroxyurea'),
    ('Abrocitinib', 'Atopic dermatitis'),
    ('Tofacitinib', 'PsA, UC, JIA, ankylosing spondylitis, RA'),
])
fill(246, 'Upadacitinib is used for RA, psoriatic arthritis and ____ dermatitis.', 'atopic')
finish()

# CHAPTER 63 - ANTI-AGGREGANTS AND HEMATOPOIETIC AGENTS (p247-250) ------------
start(63)
unit('Physiology of Platelet Aggregation and Aspirin',
 'Injury → collagen + vWF activate platelets. GP IIb/IIIa ← abciximab; COX-1 ← aspirin (↓TXA2); ADP/P2Y12 ← clopidogrel; PAR ← vorapaxar. Aspirin irreversible COX-1, 50–325 mg OD. Uses: 2° ACS/stroke prophylaxis, ACS Rx, essential thrombocythemia, Kawasaki, APS. Pre-op: continue aspirin, stop clopidogrel 7 days.')
match(247, 'Match the antiplatelet target.', [
    ('Aspirin', 'Irreversible COX-1 → ↓ thromboxane A2'),
    ('Clopidogrel', 'P2Y12 (ADP) receptor'),
    ('Abciximab', 'GP IIb/IIIa'),
    ('Vorapaxar', 'PAR (protease-activated receptor)'),
])
fill(247, 'Antiplatelet aspirin dose is ____ mg once daily.', '50-325', aliases=['50–325','50 to 325'])
mcq(247, 'Before surgery in a patient on dual antiplatelets:',
    'Continue aspirin; stop clopidogrel 7 days pre-op',
    ['Stop both agents 7 days pre-op',
     'Continue both through surgery',
     'Stop aspirin and continue clopidogrel'])
mcq(247, 'Aspirin antiplatelet uses include all EXCEPT:',
    'Primary prophylaxis of a first DVT in a healthy adult',
    ['Secondary prophylaxis of ACS and ischemic stroke',
     'Essential thrombocythemia and Kawasaki disease',
     'Antiphospholipid antibody syndrome'])

unit('ADP/P2Y12 Inhibitors: Classification and Hit and Run Concept',
 'Irreversible: clopidogrel, ticlopidine, prasugrel. Reversible competitive: cangrelor (adenosine analog, T1/2 3–6 min, IV, PCI in MI). Reversible non-competitive: ticagrelor (long, oral; PCI, ACS, 2° MI). Hit-and-run: irreversible P2Y12 blockers, aspirin, PPIs — irreversible binding prolongs T1/2 effect.')
match(248, 'Match the P2Y12 blocker class.', [
    ('Clopidogrel / ticlopidine / prasugrel', 'Irreversible'),
    ('Cangrelor', 'Reversible competitive; IV; T1/2 3–6 min; PCI in MI'),
    ('Ticagrelor', 'Reversible non-competitive; long oral; PCI, ACS, 2° MI'),
])
fill(248, 'Cangrelor is an ____ analog with a 3–6 minute half-life.', 'adenosine')
mcq(248, '“Hit and run” drugs (irreversible target binding → longer effect) include:',
    'Irreversible P2Y12 blockers, aspirin and PPIs',
    ['Cangrelor and ticagrelor only',
     'Heparin and warfarin',
     'Abciximab and eptifibatide only'])

unit('Clopidogrel, Ticlopidine and Prasugrel',
 'Clopidogrel: prodrug via CYP2C19; polymorphisms blunt effect and worsen MI; omeprazole competitively inhibits. Use like aspirin; combine with aspirin on a stent. Ticlopidine: GI toxicity, agranulocytosis, TTP-HUS; 2° stroke if resistant. Prasugrel: most potent/fastest, ↑ intracranial bleed, C/I prior stroke/TIA, PCI in MI.')
fill(248, 'Clopidogrel is a prodrug activated by CYP____.', '2C19')
mcq(248, 'Omeprazole reduces clopidogrel effect because CYP2C19:',
    'Metabolizes omeprazole → competitive inhibition of clopidogrel activation',
    ['Induces P-gp and pumps clopidogrel out',
     'Acetylates COX-1 irreversibly',
     'Converts clopidogrel to an inactive sulfate'])
fill(248, 'Ticlopidine unique toxicities include agranulocytosis and ____-HUS.', 'TTP')
fill(248, 'The most potent and fastest oral P2Y12 inhibitor is ____.', 'prasugrel')
mcq(248, 'Prasugrel is contraindicated if there is a history of:',
    'Stroke or TIA (↑ intracranial bleed)',
    ['PCI in MI (its only approved use is banned)',
     'Stent placement (must never combine with aspirin)',
     'CYP2C19 poor-metabolizer status'])

unit('Vorapaxar and GP IIb/IIIa Inhibitors',
 'Vorapaxar: PAR blocker; 2° MI / unstable angina ± aspirin/clopidogrel; ↑ intracranial bleed, C/I stroke/TIA. Abciximab: GP IIb/IIIa + vitronectin; shortest T1/2 but max affinity → longest acting. Eptifibatide: longest T1/2, min affinity → shortest acting. Uses PCI/ACS; IV or intracoronary. Also tirofiban.')
fill(249, 'Vorapaxar blocks the ____ receptor.', 'PAR', aliases=['protease activated receptor','protease-activated receptor'])
mcq(249, 'Vorapaxar, like prasugrel, raises intracranial bleed risk and is C/I in:',
    'Prior stroke / TIA',
    ['PCI in MI','Unstable angina','Aspirin co-therapy'])
match(249, 'Match the GP IIb/IIIa blocker kinetics.', [
    ('Abciximab', 'Shortest T1/2, maximum affinity → longest acting'),
    ('Eptifibatide', 'Longest T1/2, minimum affinity → shortest acting'),
    ('Route', 'IV or intra-coronary (PCI / ACS)'),
])
fill(249, 'The other GP IIb/IIIa inhibitor besides abciximab and eptifibatide is ____.', 'tirofiban')

unit('Hematopoietic Agents: Erythropoiesis and Granulopoiesis',
 'EPO: epoetin alfa; darbepoetin longer / preferred. DOC anemia of CRF, dialysis, zidovudine/chemo, prem infants. S/E HTN, iron deficiency, thrombosis, PRCA, flu-like. Peginesatide: EPO-receptor agonist, CKD. G-CSF (more potent, less toxic): filgrastim m/c, lenograstim; pegfilgrastim / lipegfilgrastim long, once per cycle. S/E bone pain. GM-CSF sargramostim: less potent, more toxic, capillary leak.')
fill(249, 'The longer-acting, clinically preferred EPO analog is ____.', 'darbepoetin')
mcq(249, 'EPO analogs are DOC for anemia due to all EXCEPT:',
    'Iron-deficiency anemia in an otherwise healthy adult',
    ['CRF / dialysis',
     'Zidovudine or anticancer drugs',
     'Premature infants'])
mcq(249, 'EPO analog side effects include:',
    'HTN, iron deficiency, thrombosis, pure red-cell aplasia, flu-like symptoms',
    ['Capillary leak as the dominant toxicity',
     'Bone pain as the dominant toxicity',
     'Agranulocytosis and TTP-HUS'])
fill(249, 'Peginesatide is an EPO-receptor agonist for anemia of ____.', 'CKD', aliases=['CRF','chronic kidney disease'])
fill(249, 'The most commonly used G-CSF analog is ____.', 'filgrastim')
fill(249, 'G-CSF side effect is ____ pain; GM-CSF (sargramostim) causes capillary leak.', 'bone')
mcq(249, 'Pegfilgrastim / lipegfilgrastim are:',
    'Long-acting G-CSF given once per chemotherapy cycle',
    ['Short-acting EPO analogs given thrice weekly',
     'IL-11 analogs for ITP',
     'GM-CSF analogs that cause PRCA'])

unit('Drugs Acting on Thrombopoiesis',
 'TPO agonists romiplostim and eltrombopag: ITP; S/E portal-vein thrombosis and AML. Newer avatrombopag / lusutrombopag prevent procedural bleeding in cirrhosis. IL-11 oprelvekin: chemo thrombocytopenia; fluid retention → CHF/edema.')
fill(250, 'Romiplostim and eltrombopag are used for ____.', 'ITP',
     aliases=['immune thrombocytopenic purpura','immune thrombocytopenia'])
mcq(250, 'TPO-agonist toxicities include:',
    'Portal-vein thrombosis and acute myeloid leukemia',
    ['Pure red-cell aplasia and hypertension',
     'Capillary leak and bone pain',
     'TTP-HUS and agranulocytosis'])
fill(250, 'Avatrombopag and lusutrombopag prevent procedural bleeding in liver ____.', 'cirrhosis')
fill(250, 'The IL-11 analog for chemotherapy-induced thrombocytopenia is ____.', 'oprelvekin')
fill(250, 'Oprelvekin causes fluid retention leading to ____ and edema.', 'CHF',
     aliases=['congestive heart failure','heart failure'])
finish()

# CHAPTER 64 - ANTICOAGULANTS AND FIBRINOLYTICS (p251-255) -------------------
start(64)
unit('Physiology of Coagulation and Anticoagulation',
 'X→Xa blocked by oral Xa inhibitors; II→IIa blocked by direct thrombin inhibitors; fibrinogen→fibrin. Anticoagulation: protein C & S and antithrombin III (breaks IIa, Xa, XIa, XIIa), stimulated by indirect thrombin inhibitors (heparins).')
match(251, 'Match the coagulation step with the drug class.', [
    ('Factor Xa', 'Blocked by oral Xa inhibitors (apixaban…)'),
    ('Thrombin (IIa)', 'Blocked by direct thrombin inhibitors'),
    ('Antithrombin III', 'Stimulated by heparins (indirect)'),
    ('Protein C & S', 'Natural anticoagulant proteins'),
])
fill(251, 'Prothrombin is factor ____; thrombin is IIa.', 'II')
mcq(251, 'Antithrombin III proteolyses:',
    'IIa, Xa, XIa and XIIa',
    ['Fibrinogen itself',
     'Protein C exclusively',
     'Tissue-factor pathway inhibitor'])

unit('Direct Acting Anticoagulants: DOAC/NOAC',
 'Oral DTI: dabigatran. Oral Xa: apixaban, edoxaban, rivaroxaban. DOACs: no routine monitoring; Rx DVT; DOC DVT prophylaxis and non-valvular AF. Parenteral DTI: HIT — argatroban DOC (aPTT); hirudins; bivalirudin/argatroban PCI. C/I renal failure except argatroban (hepatic). Antidotes: idarucizumab (dabigatran), andexanet alfa (Xa, decoy).')
fill(251, 'The oral direct thrombin inhibitor is ____.', 'dabigatran')
mcq(251, 'Oral Xa inhibitors are:',
    'Apixaban, edoxaban and rivaroxaban',
    ['Dabigatran, argatroban and bivalirudin',
     'Warfarin, acenocoumarol and phenindione',
     'Enoxaparin, tinzaparin and fondaparinux'])
fill(251, 'DOACs ____ routine coagulation monitoring.', 'do not require', aliases=["don't require",'do not need','need no'])
fill(251, 'DOC for DVT prophylaxis and thrombosis prophylaxis in non-valvular AF is a ____.', 'DOAC',
     aliases=['NOAC','direct oral anticoagulant'])
fill(251, 'DOC for HIT among parenteral DTIs is ____ (monitor aPTT).', 'argatroban')
mcq(251, 'Direct thrombin inhibitors are C/I in renal failure EXCEPT:',
    'Argatroban (hepatic excretion)',
    ['Dabigatran (also hepatic only)',
     'Lepirudin',
     'Desirudin'])
fill(251, 'Antidote for dabigatran is ____.', 'idarucizumab')
fill(251, 'Antidote for oral Xa inhibitors is ____ alfa (a decoy).', 'andexanet')

unit('Indirect Thrombin Inhibitors: UFH, LMWH and Fondaparinux Structure',
 'UFH: AP + long HPS, Xa = IIa, poor BA, SC BD prophylaxis / IV QID Rx, RES metabolism, DOC in renal failure, short, aPTT, protamine effective, HIT ↑↑. LMWH: AP + short HPS, Xa > IIa, better BA, SC OD, renal excretion, C/I in renal failure, long, anti-Xa in special groups, protamine less effective, HIT ↑. Fondaparinux: AP only, Xa only, max BA, no monitoring, protamine useless, no HIT.')
match(252, 'Match structure with anti-Xa / anti-IIa activity.', [
    ('UFH (AP + long HPS)', 'Anti-Xa = anti-IIa'),
    ('LMWH (AP + short HPS)', 'Anti-Xa > anti-IIa'),
    ('Fondaparinux (AP only)', 'Anti-Xa only'),
])
match(252, 'Match the heparin-type with monitoring / antidote / HIT.', [
    ('UFH', 'aPTT; protamine effective; HIT risk highest'),
    ('LMWH', 'Anti-Xa in CKD/obese/elderly/children; protamine less effective'),
    ('Fondaparinux', 'No monitoring; protamine ineffective; no HIT'),
])
fill(252, 'In renal failure the heparin of choice is ____.', 'UFH',
     aliases=['unfractionated heparin','unfractionated'])
fill(252, 'LMWH and fondaparinux are ____ in renal failure.', 'contraindicated')
mcq(252, 'UFH dosing is typically:',
    'Prophylaxis SC BD; treatment IV QID',
    ['Prophylaxis and treatment SC OD',
     'Oral OD',
     'Intra-arterial once weekly'])
fill(252, 'LMWH is given SC ____ for both prophylaxis and treatment.', 'OD', aliases=['once daily'])
fill(252, 'UFH is metabolized by the ____ system.', 'reticuloendothelial', aliases=['RES'])
mcq(252, 'Bioavailability ranking is:',
    'Fondaparinux (maximum) > LMWH (increased) > UFH (poor)',
    ['UFH > LMWH > fondaparinux',
     'LMWH = UFH > fondaparinux',
     'All three are complete after oral dosing'])

unit('Heparin Induced Thrombocytopenia and Heparin Uses',
 'HIT: antibodies to HPS cross-react with PF4 → aggregation → thrombosis (venous > arterial, F>M, surgical/cancer). UFH > LMWH; not severe thrombocytopenia. Rx like thrombosis: argatroban DOC, fondaparinux; platelets >150k then warfarin/DOAC; ≥4 weeks, 3 months if major event. UFH: catheter thrombosis, with thrombolysis. LMWH/fondaparinux DOC for treating thrombosis. C/I TEACHER; S/E AHOT.')
fill(253, 'HIT antibodies against heparin polysaccharides cross-react with platelet factor ____.', '4',
     aliases=['PF4'])
mcq(253, 'HIT thrombosis is:',
    'Venous > arterial, women > men, surgical and cancer patients',
    ['Arterial > venous, men > women, only medical inpatients',
     'Never thrombotic — only bleeding',
     'Seen equally with fondaparinux and UFH'])
fill(253, 'HIT is more common with UFH than with ____.', 'LMWH')
fill(253, 'Once platelets are > ____ /µL in HIT, start warfarin or a DOAC.', '150000',
     aliases=['150,000','1,50,000','150 k','150000'])
fill(253, 'Minimum duration of anticoagulation after HIT thrombosis is ____ weeks (3 months if a major event).', '4')
mcq(253, 'Heparin C/I mnemonic TEACHER includes all EXCEPT:',
    'Hyperthyroidism',
    ['Thrombocytopenia and endocarditis',
     'Alcoholics / cirrhosis and severe hypertension',
     'Eye/neurosurgery and renal failure (LMWH/fondaparinux)'])
mcq(253, 'Heparin S/E mnemonic AHOT stands for:',
    'Alopecia, hemorrhage/hyperkalemia, osteoporosis, thrombosis (HIT)',
    ['Asthma, hepatitis, ototoxicity, tremor',
     'Anemia, hiccups, osteosarcoma, tinnitus',
     'Ataxia, hyperthermia, oliguria, thrombocytosis'])
fill(253, 'UFH is preferred for catheter-induced thrombosis and when given with concurrent ____.', 'thrombolysis',
     aliases=['fibrinolysis'])

unit('Warfarin: MOA, Uses and Monitoring',
 'Warfarin inhibits VKOR → ↓ active vit K → ↓ γ-carboxylation of II, VII, IX, X, protein C & S. VII first, C&S second, II last. 5 days to anticoagulate; first 5 days thrombosis/skin necrosis (C/I HIT) — heparin-bridge with LMWH. Preferred over DOAC in valvular AF and non-valvular AF with CKD, P-gp(−), severe MS. DOC APS and splanchnic-vein thrombosis. INR 2–3. Ciraparantag reverses all but warfarin.')
fill(254, 'Warfarin inhibits vitamin K ____ (VKOR).', 'oxidoreductase', aliases=['epoxide reductase'])
match(254, 'Match the order in which warfarin-sensitive proteins fall.', [
    ('First to decline', 'Factor VII'),
    ('Second to decline', 'Protein C and S'),
    ('Last to decline', 'Factor II'),
])
fill(254, 'Warfarin needs a minimum of ____ days for an anticoagulant effect.', '5')
mcq(254, 'Skin necrosis in the first 5 days of warfarin is due to:',
    'Rapid fall in protein C & S → thrombosis (therefore C/I in HIT)',
    ['Excess factor II remaining while VII is still high',
     'Vitamin K accumulating in dermal capillaries',
     'HIT-type antibodies to platelet factor 4'])
fill(254, 'Bridge warfarin with ____ for the first 5 days.', 'LMWH')
mcq(254, 'Warfarin is preferred over a DOAC in all EXCEPT:',
    'Uncomplicated non-valvular AF with normal kidneys',
    ['Valvular AF',
     'Non-valvular AF with renal failure, P-gp block or severe mitral stenosis',
     'Antiphospholipid syndrome and splanchnic-vein thrombosis'])
fill(254, 'Warfarin INR target is ____ (normal 0.9–1.3).', '2-3', aliases=['2–3','2 to 3'])
match(254, 'Match the high-INR scenario.', [
    ('INR 3–10, no bleed', 'Stop warfarin; restart when INR normal'),
    ('INR >10, asymptomatic', 'Stop warfarin + vitamin K; restart when INR normal'),
    ('Symptomatic bleeding', 'Stop warfarin; 4-factor PCC > FFP + IV vitamin K'),
])
fill(254, 'Warfarin teratogenicity includes nasal (mid-facial) hypoplasia and ____ epiphyseal calcification.', 'stippled')
fill(254, 'Warfarin is C/I in pregnancy except if the patient has a ____ valve.', 'mechanical')
fill(254, 'Ciraparantag is an antidote for all anticoagulants except ____.', 'warfarin')
mcq(254, 'Warfarin skin necrosis prefers:',
    'Limbs, breast and penile skin',
    ['Scalp, palms and soles',
     'The abdominal wall exclusively',
     'Oral mucosa only'])

unit('Fibrinolytics and Antifibrinolytics',
 'Plasminogen —tPA→ plasmin → fibrin. Streptokinase: clot-nonspecific, ↑ bleed, ↑ dose. Recombinant tPA (alteplase, duteplase, reteplase, tenecteplase) clot-specific; tenecteplase most specific + single dose. Uses: STEMI (never NSTEMI/UA), massive PE, peripheral thrombosis. C/I BRAIN. Bleed: EACA, tranexamic acid. TXA C/I: upper GU bleed (ischemia), hypotension, myopathy.')
fill(255, 'tPA converts plasminogen to ____, which breaks fibrin.', 'plasmin')
mcq(255, 'Streptokinase is clot-nonspecific, so it:',
    'Lyses fibrin in clot AND plasma → more bleeding and a higher dose',
    ['Is the most clot-specific agent and is given once',
     'Cannot cause bleeding',
     'Is preferred in NSTEMI'])
fill(255, 'The most clot-specific fibrinolytic, given as a single dose, is ____.', 'tenecteplase')
mcq(255, 'Fibrinolytics are used in STEMI, massive PE and peripheral thrombosis, but NEVER in:',
    'NSTEMI / unstable angina',
    ['STEMI within the window',
     'Massive pulmonary embolism',
     'Acute limb thrombosis'])
mcq(255, 'BRAIN contraindications to fibrinolysis include all EXCEPT:',
    'Uncomplicated STEMI presenting early',
    ['Brain tumour / aneurysm and intracranial hemorrhage',
     'Recent surgery / trauma and aortic dissection',
     'NSTEMI'])
fill(255, 'Antifibrinolytics that block plasmin are EACA and ____ acid.', 'tranexamic')
mcq(255, 'Tranexamic acid / EACA are C/I in upper genitourinary bleed because of the risk of:',
    'Ischemia (also hypotension and myopathy)',
    ['Massive fibrinolysis',
     'HIT',
     'Warfarin skin necrosis'])
finish()

# CHAPTER 65 - BRONCHIAL ASTHMA (p256-258) -----------------------------------
start(65)
unit('Pathophysiology and Bronchodilator Classification',
 'Allergen → mast-cell lysis → histamine → bronchoconstriction (bronchodilators) and inflammation (steroids). Bronchodilators: β2 agonists, anticholinergics, methylxanthines.')
mcq(256, 'In asthma, bronchoconstriction is treated with bronchodilators and inflammation with:',
    'Steroids',
     ['A second bronchodilator class',
     'Antibiotics',
     'Antihistaminics as disease-modifying DOC'])
match(256, 'Match the asthma path step with the treatment idea.', [
    ('Mast-cell lysis → histamine', 'Starts both constriction and inflammation'),
    ('Bronchoconstriction', 'Bronchodilators'),
    ('Inflammation', 'Steroids'),
    ('Bronchodilator classes', 'β2 agonists, anticholinergics, methylxanthines'),
])

unit('Methylxanthines: MOA and Drugs',
 'Bronchodilation: PDE3 > PDE4 → ↑cAMP → relax muscle, plus adenosine-receptor antagonism. Anti-inflammatory: PDE4 (roflumilast in COPD), histone deacetylase (also steroids), ↑IL-10, neutrophil apoptosis. Oral theophylline > aminophylline (add-on persistent BA). IV aminophylline > theophylline (acute exacerbation).')
mcq(256, 'Methylxanthine bronchodilation is mainly:',
    'PDE3 > PDE4 inhibition → ↑cAMP, plus adenosine-receptor block',
    ['PDE4-only inhibition with no adenosine effect',
     'Direct β2 agonism',
     'Muscarinic M3 blockade'])
fill(256, 'Roflumilast is a PDE____ inhibitor used for COPD.', '4')
mcq(256, 'Anti-inflammatory methylxanthine actions include all EXCEPT:',
    'Increased IL-1 and TNF',
    ['PDE4 inhibition',
     'Stimulation of histone deacetylase (steroids do this too)',
     'Increased IL-10 and neutrophil apoptosis'])
fill(256, 'Oral methylxanthine preferred for add-on persistent asthma is ____.', 'theophylline')
fill(256, 'IV methylxanthine preferred for acute exacerbation is ____.', 'aminophylline')

unit('Methylxanthines: Side Effects and Therapeutic Index',
 'PDE4 S/E at ~20–25 mg/L: GI upset, headache. Adenosine-block (± PDE3) S/E at >30 mg/L: arrhythmia, seizures. Theophylline N 5–15 mg/L; toxicity >20; low TI.')
match(256, 'Match theophylline level with the meaning.', [
    ('5–15 mg/L', 'Normal therapeutic range'),
    ('~20–25 mg/L', 'PDE4 S/E: nausea, vomiting, headache'),
    ('>30 mg/L', 'Adenosine-block S/E: arrhythmia and seizures'),
    ('>20 mg/L', 'Toxicity threshold (low therapeutic index)'),
])
fill(256, 'Theophylline has a ____ therapeutic index.', 'low')

unit('Inhalational and Systemic Steroids in Asthma',
 'ICS: fluticasone most potent; flunisolide least; ciclesonide & beclomethasone = soft (airway metabolism). Uses: persistent BA, EIA, aspirin-induced constriction (DOC), intermittent <2/week. S/E hoarseness m/c; thrush prevented by technique; systemic minimal. Intermittent: 0–5 y SABA; 6–11 SABA then ICS; >12 FDC ICS+formoterol. Oral prednisone/olone; IV hydrocortisone faster than methylpred. Acute: oral > IV. Steroids ↓ mucus/mediators and ↑ β2 receptors (complementary).')
fill(257, 'The most potent ICS is ____.', 'fluticasone')
fill(257, 'The least potent ICS is ____.', 'flunisolide')
fill(257, 'Soft ICS (airway metabolism, fewer S/E) are ciclesonide and ____.', 'beclomethasone')
fill(257, 'DOC for aspirin-induced bronchoconstriction is an ____.', 'ICS',
     aliases=['inhaled corticosteroid','inhalational steroid'])
fill(257, 'Most common ICS local side effect is ____ of voice.', 'hoarseness')
mcq(257, 'Oropharyngeal candidiasis from ICS is prevented by:',
    'Good inhaler technique',
     ['Routine oral antifungal prophylaxis in everyone',
      'Switching to oral prednisolone',
      'Stopping ICS after one attack'])
match(257, 'Match intermittent-asthma age with reliever strategy.', [
    ('0–5 years', 'SABA alone'),
    ('6–11 years', 'SABA + ICS (SABA first)'),
    ('>12 years', 'FDC ICS + formoterol pMDI'),
])
fill(257, 'Oral systemic steroid: prednisone / ____.', 'prednisolone')
fill(257, 'Faster-acting IV steroid in asthma is ____ (over methylprednisolone).', 'hydrocortisone')
mcq(257, 'For an acute asthma exacerbation, systemic steroids are given:',
    'Oral in preference to IV',
    ['IV in preference to oral',
     'Never — only ICS',
     'If theophylline has already failed'])
mcq(257, 'In an exacerbation, steroids increase β2 receptors so that:',
    'β2-agonist effect and steroid effect become complementary',
    ['β2 agonists stop working',
     'Methylxanthines become unnecessary forever',
     'Muscarinic receptors are upregulated'])

unit('Accessory Drugs: Antileukotrienes, Mast Cell Stabilizers and Monoclonal Antibodies',
 'Zileuton = 5-LOX (max hepatotoxicity). Montelukast/zafirlukast/pranlukast = LTC4/D4; Churg-Strauss with montelukast/zafirlukast. Cromolyn/nedocromil: Ca2+ channel block in mast cells. Ketotifen: mast-cell + ↑NO. Omalizumab: anti-IgE SC q2–4 wk; dose by weight + IgE; C/I atopic dermatitis (very high IgE). Dupilumab IL-4R; reslizumab/mepolizumab IL-5; benralizumab IL-5R — severe eosinophilic asthma and atopic dermatitis.')
fill(258, 'The 5-LOX inhibitor is ____.', 'zileuton')
mcq(258, 'LTC4/LTD4 receptor blockers are:',
    'Montelukast, zafirlukast and pranlukast',
    ['Zileuton only',
     'Cromolyn and nedocromil',
     'Omalizumab and dupilumab'])
fill(258, 'Hepatotoxicity of antileukotrienes is maximum with ____.', 'zileuton')
fill(258, 'Churg-Strauss is associated with montelukast and ____.', 'zafirlukast')
fill(258, 'Mast-cell stabilizers block ____ channels, preventing degranulation.', 'Ca2+',
     aliases=['calcium','Ca','Ca++'])
match(258, 'Match cromolyn / nedocromil route with use.', [
    ('Oral', 'Food allergy and systemic mastocytosis'),
    ('Nasal spray', 'Allergic rhinitis'),
    ('Eye drops', 'Allergic conjunctivitis'),
    ('Inhaled', 'Mild asthma (least toxic; preferred in children)'),
])
fill(258, 'Ketotifen stabilizes mast cells and increases ____ release.', 'NO', aliases=['nitric oxide'])
fill(258, 'Omalizumab is an anti-____ monoclonal antibody.', 'IgE')
fill(258, 'Omalizumab is given S/C every ____ weeks; dose depends on weight and IgE titer.', '2-4',
     aliases=['2–4','2 to 4'])
mcq(258, 'Omalizumab is contraindicated in atopic dermatitis because of:',
    'Very high IgE levels',
    ['Very low IgE levels',
     'IL-5 receptor saturation',
     'PDE4 inhibition'])
match(258, 'Match the monoclonal with its target.', [
    ('Dupilumab', 'IL-4 receptor on T-helper cells'),
    ('Reslizumab / mepolizumab', 'IL-5 itself'),
    ('Benralizumab', 'IL-5 receptor on eosinophils'),
    ('IL-4 / IL-5 mAbs use', 'Severe eosinophilic asthma and atopic dermatitis'),
])
finish()
