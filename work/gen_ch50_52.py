# -*- coding: utf-8 -*-
"""Generate chapters 50-52 from Marrow Pharmacology E8, book pp205-214.

ch50 Anti-Helminthic Drugs (p205-206)
ch51 Antidiabetic Drugs: Part 1 (p207-210)
ch52 Antidiabetic Drugs: Part 2 (p211-214)
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

# CHAPTER 50 - ANTI-HELMENTHIC DRUGS (p205-206) --------------------------------
start(50)
unit('Benzimidazoles',
 'The benzimidazoles are mebendazole (m/c in western countries), triclabendazole, thiabendazole and albendazole - a prodrug (m/c in India) activated in the liver to albendazole sulfoxide. MOA: blocks microtubules in the intestinal cells of helminths, decreasing glucose absorption (decreased ATP).')
facts(205,[
('The benzimidazole group includes all EXCEPT:','Praziquantel',['Mebendazole','Albendazole','Thiabendazole'],'Benzimidazoles: mebendazole, triclabendazole, thiabendazole, albendazole.'),
('The most common benzimidazole in western countries is:','Mebendazole',['Albendazole','Thiabendazole','Triclabendazole'],'Mebendazole: m/c in western countries.'),
('The benzimidazole most commonly used in India is:','Albendazole',['Mebendazole','Thiabendazole','Triclabendazole'],'Albendazole: m/c in India.'),
('Albendazole is a:','Prodrug',['Active parent drug','Drug inactivated by liver metabolism','Topical agent only'],'Albendazole: prodrug.'),
('The active metabolite of albendazole formed in the liver is:','Albendazole sulfoxide',['Albendazole sulfone','Albendazole N-oxide','Albendazole glucuronide'],'Active drug: albendazole sulfoxide (in liver).'),
('The MOA of albendazole is:','Blocks microtubules in intestinal cells of helminths -> decreased glucose absorption (decreased ATP)',['Stimulates glutamate-sensitive chloride channels','Blocks Ca2+ channels causing spastic paralysis','Blocks folate synthesis'],'MOA: blocks microtubules in intestinal cells of helminths -> decreased glucose absorption (decreased ATP).'),
('The benzimidazole that is also the DOC for Fasciola hepatica is:','Triclabendazole',['Mebendazole','Thiabendazole','Albendazole'],'Benzimidazole list includes triclabendazole (DOC Fasciola hepatica).'),
])
unit('Nematodes and Drugs of Choice',
 'Albendazole is the DOC for round worm, whip worm, hook worm, Enterobius vermicularis and Trichinella spiralis. Ivermectin is the DOC for Strongyloides and Onchocerca volvulus (river blindness). Diethylcarbamazine (DEC) is the DOC for Loa loa and filariasis where TOC is IDA (ivermectin, DEC, albendazole). Metronidazole is the DOC for dracunculiasis.')
facts(205,[
('The DOC for round worm, whip worm and hook worm is:','Albendazole',['Ivermectin','DEC','Praziquantel'],'Nematodes DOC - albendazole: round worm, whip worm, hook worm.'),
('Albendazole is the DOC for all EXCEPT:','Strongyloides',['Enterobius vermicularis','Trichinella spiralis','Hook worm'],'Albendazole: round worm, whip worm, hook worm, Enterobius vermicularis, Trichinella spiralis; Strongyloides is ivermectin.'),
('The DOC for Strongyloides is:','Ivermectin',['Albendazole','DEC','Metronidazole'],'Ivermectin: Strongyloides.'),
('The DOC for Onchocerca volvulus (river blindness) is:','Ivermectin',['DEC','Albendazole','Praziquantel'],'Ivermectin: Onchocerca volvulus (river blindness).'),
('The DOC for Loa loa is:','Diethylcarbamazine (DEC)',['Ivermectin','Albendazole','Metronidazole'],'DEC: Loa loa.'),
('The DOC for filariasis is:','Diethylcarbamazine (DEC)',['Ivermectin alone','Albendazole alone','Doxycycline'],'DEC: filariasis.'),
('The TOC for filariasis is:','IDA (ivermectin, DEC, albendazole)',['DEC monotherapy','Ivermectin + albendazole only','DEC + steroids only'],'Filariasis TOC: IDA (ivermectin, DEC, albendazole).'),
('The DOC for dracunculiasis is:','Metronidazole',['Ivermectin','Praziquantel','Albendazole'],'Metronidazole: dracunculiasis.'),
('The DOC for Trichinella spiralis is:','Albendazole',['Ivermectin','DEC','Praziquantel'],'Albendazole: Trichinella spiralis.'),
])
unit('Cestodes and Drugs of Choice',
 'Albendazole is the DOC for neurocysticercosis (T. solium) and Echinococcus. Praziquantel is the DOC for intestinal T. solium, T. saginata, H. nana and D. latum. Note: the first priority of treatment of neurocysticercosis is steroids (to decrease perilesional edema).')
facts(205,[
('The DOC for neurocysticercosis (T. solium) is:','Albendazole',['Praziquantel','Ivermectin','DEC'],'Cestodes DOC - albendazole: neurocysticercosis (T. solium).'),
('The DOC for Echinococcus is:','Albendazole',['Praziquantel','Niclosamide','Mebendazole'],'Albendazole: Echinococcus.'),
('The DOC for intestinal T. solium is:','Praziquantel',['Albendazole','Niclosamide','Ivermectin'],'Praziquantel: intestinal T. solium.'),
('Praziquantel is the DOC for all tapeworm infections EXCEPT:','Neurocysticercosis',['T. saginata','H. nana','D. latum'],'Praziquantel: intestinal T. solium, T. saginata, H. nana, D. latum; neurocysticercosis is albendazole.'),
('The cestodes treated with praziquantel as DOC are:','Intestinal T. solium, T. saginata, H. nana and D. latum',['Neurocysticercosis and Echinococcus','Fasciola and Schistosoma','Loa loa and filariasis'],'Praziquantel: intestinal T. solium, T. saginata, H. nana, D. latum.'),
('The first priority of treatment of neurocysticercosis is:','Steroids (to decrease perilesional edema)',['Albendazole immediately','Praziquantel immediately','Surgery first'],'Note: first priority of treatment of neurocysticercosis is steroids (to decrease perilesional edema).'),
])
unit('Trematodes and Drugs of Choice',
 'Triclabendazole is the DOC for Fasciola hepatica. Praziquantel is the DOC for other liver flukes, all lung flukes and Schistosoma. Note: albendazole is ineffective against trematodes.')
facts(206,[
('The DOC for Fasciola hepatica is:','Triclabendazole',['Praziquantel','Albendazole','Mebendazole'],'Trematodes DOC - triclabendazole: Fasciola hepatica.'),
('Praziquantel is the DOC for all trematode infections EXCEPT:','Fasciola hepatica',['Other liver flukes','All lung flukes','Schistosoma'],'Praziquantel: other liver flukes, all lung flukes, Schistosoma; Fasciola is triclabendazole.'),
('The DOC for Schistosoma is:','Praziquantel',['Triclabendazole','Albendazole','DEC'],'Praziquantel: Schistosoma.'),
('The DOC for all lung flukes is:','Praziquantel',['Triclabendazole','Albendazole','Ivermectin'],'Praziquantel: all lung flukes.'),
('Albendazole is ineffective against:','Trematodes',['Cestodes','Nematodes','Echinococcus'],'Note: albendazole ineffective against trematodes.'),
])
unit('Ivermectin',
 'Ivermectin MOA: stimulates glutamate-sensitive chloride channels producing tonic paralysis. Other use: oral DOC in scabies. Side effect: Mazzotti-like reaction (due to dying parasite) with rash and lymphadenopathy; it is also seen with DEC.')
facts(206,[
('The MOA of ivermectin is:','Stimulates glutamate-sensitive chloride channels -> tonic paralysis',['Stimulates Ca2+ channels -> spastic paralysis','Stimulates GABA-sensitive chloride channels -> flaccid paralysis','Inhibits ACh esterase'],'Ivermectin MOA: stimulates glutamate sensitive chloride channels -> tonic paralysis.'),
('The type of paralysis produced by ivermectin is:','Tonic paralysis',['Spastic paralysis','Flaccid paralysis','No paralysis - it only sterilizes'],'Ivermectin: glutamate-gated chloride channels -> tonic paralysis.'),
('The oral DOC in scabies is:','Ivermectin',['Permethrin','Albendazole','DEC'],'Other uses: oral DOC in scabies - ivermectin.'),
('The side effect of ivermectin is:','Mazzotti-like reaction (due to dying parasite)',['Jarisch-Herxheimer reaction','Gray baby syndrome','Serotonin syndrome'],'S/E: Mazzotti-like reaction (D/t dying parasite).'),
('The features of Mazzotti-like reaction are:','Rash and lymphadenopathy',['Fever and jaundice','Urticaria and bronchospasm only','Nephrotoxicity'],'Mazzotti-like reaction: rash, lymphadenopathy.'),
('Mazzotti-like reaction is also seen with:','DEC',['Albendazole','Praziquantel','Niclosamide'],'Mazzotti-like reaction: also seen in DEC.'),
])
unit('Praziquantel and Metrifonate',
 'Praziquantel MOA: stimulates Ca2+ channels producing spastic paralysis; the same spastic paralysis is also caused by pyrantel pamoate and metrifonate. Metrifonate MOA: inhibits ACh esterase increasing ACh; use - Schistosoma haematobium.')
facts(206,[
('The MOA of praziquantel is:','Stimulates Ca2+ channels -> spastic paralysis',['Stimulates glutamate chloride channels -> tonic paralysis','Stimulates GABA chloride channels -> flaccid paralysis','Inhibits microtubules'],'Praziquantel MOA: stimulates Ca2+ channels -> spastic paralysis.'),
('Spastic paralysis is also caused by:','Pyrantel pamoate and metrifonate',['Ivermectin and piperazine','Albendazole and mebendazole','Niclosamide and DEC'],'Spastic paralysis also caused by pyrantel pamoate, metrifonate.'),
('The MOA of metrifonate is:','Inhibits ACh esterase -> increased ACh',['Stimulates nicotinic receptors directly','Blocks ACh release','Stimulates Ca2+ channels'],'Metrifonate MOA: inhibits ACh esterase -> increased ACh.'),
('The use of metrifonate is:','Schistosoma haematobium',['All Schistosoma species','Fasciola hepatica','Tapeworms'],'Metrifonate use: Schistosoma haematobium.'),
('The channel stimulated by praziquantel in helminths is:','Ca2+ channels',['Na+ channels','K+ channels','Cl- channels'],'Praziquantel: stimulates Ca2+ channels -> spastic paralysis.'),
])
unit('Pyrantel Pamoate and Piperazine',
 'Pyrantel pamoate MOA: stimulates Nm (nicotinic muscle) receptors producing spastic paralysis; earlier used for soil-transmitted helminths. Piperazine MOA: stimulates GABA-sensitive Cl- channels producing flaccid paralysis; use - soil-transmitted helminths.')
facts(206,[
('The MOA of pyrantel pamoate is:','Stimulates Nm receptors -> spastic paralysis',['Stimulates GABA Cl- channels -> flaccid paralysis','Stimulates glutamate Cl- channels','Inhibits ACh esterase'],'Pyrantel pamoate MOA: stimulates Nm receptors -> spastic paralysis.'),
('Pyrantel pamoate was earlier used for:','Soil transmitted helminths',['Filariasis','Schistosomiasis','Hydatid disease'],'Pyrantel pamoate use: earlier used for soil transmitted helminths.'),
('The MOA of piperazine is:','Stimulates GABA-sensitive Cl- channels -> flaccid paralysis',['Stimulates Nm receptors -> spastic paralysis','Stimulates glutamate Cl- channels -> tonic paralysis','Blocks Ca2+ channels'],'Piperazine MOA: stimulates GABA sensitive Cl- channels -> flaccid paralysis.'),
('The use of piperazine is:','Soil transmitted helminths',['River blindness','Dracunculiasis','Schistosomiasis'],'Piperazine use: soil transmitted helminths.'),
('The drug producing flaccid paralysis via GABA-sensitive chloride channels is:','Piperazine',['Praziquantel','Ivermectin','Pyrantel pamoate'],'Piperazine: GABA sensitive Cl- channels -> flaccid paralysis.'),
])
finish()

# CHAPTER 51 - ANTIDIABETIC DRUGS: PART 1 (p207-210) ---------------------------
start(51)
unit('Diabetes Mellitus and Physiology of Glucose Metabolism',
 'Diabetes mellitus is type I or type II with persistently increased blood glucose levels. Physiology: food is absorbed via SGLT1 (glucose); alpha glucosidase digests disaccharides and starch to glucose; increased glucose raises GLP-1 and GIP; GLP-1 acts on Gs/q receptor on beta cells (blocks ATP-sensitive K+ channels, ATP formation, insulin release via GLUT-1). Post-prandial surge gives concentration-dependent uptake of glucose (facilitated diffusion); insulin (+ amylin) acts on the insulin receptor, GLUT-4 becomes extracellular and glucose uptake occurs into cells. Amylin + GLP-1 also delay gastric emptying (dampens post-prandial hyperglycemia); glucose is reabsorbed from urine by SGLT2 (active transport) in the kidney, and the liver does gluconeogenesis during fasting. Note: GIP & GLP-1 are metabolized in plasma by DPP-4 enzyme giving a short half-life.')
facts(207,[
('Diabetes mellitus type I and type II both show:','Persistently increased blood glucose levels',['Decreased blood glucose levels','Normal HbA1c always','Episodic hypoglycemia'],'DM type I and II: persistently increased blood glucose levels.'),
('Glucose absorption in the small intestine occurs through:','SGLT1',['SGLT2','GLUT-4','GLUT-1'],'Small intestine: glucose absorbed via SGLT1.'),
('Disaccharides and starch are digested to glucose by:','Alpha glucosidase',['Amylase in stomach','SGLT1','DPP-4'],'Alpha glucosidase: disaccharides/starch -> glucose.'),
('GIP and GLP-1 are metabolized in plasma by:','DPP-4 enzyme giving short half-life',['Insulin degrading enzyme','ACE','Neutral endopeptidase'],'Note: GIP & GLP-1 metabolized in plasma by DPP-4 enzyme -> short half-life.'),
('GLP-1 acts on beta cells through:','Gs/q receptor',['Gi receptor','Tyrosine kinase receptor','Nuclear receptor'],'Diagram: Gs/q receptor on beta cells for GLP-1.'),
('GLP-1 increases insulin release by:','Blocking ATP-sensitive K+ channels',['Opening ATP-sensitive K+ channels','Blocking GLUT-1','Stimulating glucagon release'],'Beta cell: block of ATP-sensitive K+ channel -> ATP formation -> insulin release.'),
('The post-prandial surge produces glucose uptake which is:','Concentration dependent (facilitated diffusion)',['Insulin dependent only','Active transport','SGLT2 mediated'],'Diagram: after post-prandial surge - concentration dependent uptake of glucose (facilitated diffusion).'),
('Insulin acts on target cells through:','Insulin receptor with GLUT-4 becoming extracellular',['GLUT-1 translocation','Gs/q receptor','SGLT2 activation'],'Diagram: insulin -> insulin receptor -> GLUT-4 becomes extracellular -> glucose uptake.'),
('Amylin along with GLP-1 produces:','Delayed gastric emptying (dampens post-prandial hyperglycemia)',['Increased gastric emptying','Increased glucagon release','Glycosuria'],'Diagram: delayed gastric emptying (dampens post-prandial hyperglycemia) by amylin + GLP-1.'),
('Glucose is reabsorbed from urine in the kidney by:','SGLT2 (active transport)',['SGLT1','GLUT-4','Passive diffusion'],'Kidney: reabsorbed from urine via SGLT2 (active transport).'),
('During fasting, the liver maintains glucose by:','Gluconeogenesis',['Glycogenolysis only shown','Glycosuria','Ketogenesis'],'Diagram: gluconeogenesis by liver during fasting.'),
('Glucose enters the beta cell through:','GLUT-1',['GLUT-4','SGLT1','SGLT2'],'Diagram: beta cell GLUT-1 for glucose entry.'),
])
unit('Drugs Used in Diabetes Mellitus: Classification',
 'The drug groups: alpha-glucosidase inhibitors; GLP-1 related drugs (GLP-1 agonists that increase insulin release, DPP-4 inhibitors, dual GLP-1 & GIP agonist); miscellaneous - bromocriptine and colesevelam; amylin analog (delays gastric emptying); insulin; and oral hypoglycemic agents (OHA): 1. increased insulin release (block ATP-sensitive K+ channels), 2. decreased insulin resistance (e.g. pioglitazone), 3. inhibit gluconeogenesis (e.g. metformin), 4. block SGLT2 (block reabsorption by kidneys), 5. block SGLT1 & SGLT2 - sotagliflozin (approved in 2019). Note: drugs used in T1DM are insulin & amylin analogue; T2DM - all anti-diabetic drugs. Side effect of drugs that act via insulin: hypoglycemia.')
facts(208,[
('The miscellaneous anti-diabetic drugs are:','Bromocriptine and colesevelam',['Metformin and pioglitazone','Sitagliptin and liraglutide','Pramlintide and insulin'],'Miscellaneous: bromocriptine, colesevelam.'),
('The dual GLP-1 and GIP agonist group belongs to:','GLP-1 related drugs',['OHA group 2','Amylin analogs','Miscellaneous drugs'],'GLP-1 related drugs: GLP-1 agonists, DPP-4 inhibitors, dual GLP-1 & GIP agonist.'),
('The OHA that blocks SGLT1 and SGLT2 (approved in 2019) is:','Sotagliflozin',['Dapagliflozin','Canagliflozin','Empagliflozin'],'OHA 5: block SGLT1 & SGLT2 - sotagliflozin: approved in 2019.'),
('The OHA acting by decreasing insulin resistance is:','Pioglitazone',['Metformin','Glimepiride','Sitagliptin'],'OHA 2: decreased insulin resistance e.g. pioglitazone.'),
('The OHA acting by inhibiting gluconeogenesis is:','Metformin',['Pioglitazone','Glimepiride','Acarbose'],'OHA 3: inhibit gluconeogenesis e.g. metformin.'),
('Drugs used in T1DM are:','Insulin & amylin analogue',['All anti-diabetic drugs','Metformin + insulin','Only OHA'],'Note: drugs used in T1DM - insulin & amylin analogue.'),
('Drugs used in T2DM are:','All anti-diabetic drugs',['Only insulin','Only OHA except insulin','Insulin + amylin only'],'Note: drugs used in T2DM - all anti-diabetic drugs.'),
('The common side effect of drugs that act via insulin is:','Hypoglycemia',['Lactic acidosis','Weight gain always','Ketonuria'],'Note: side effect of drugs that act via insulin - hypoglycemia.'),
('The OHA that increases insulin release acts by:','Blocking ATP-sensitive K+ channels',['Opening K+ channels','Blocking Ca2+ channels','Inhibiting DPP-4'],'OHA 1: increased insulin release (block ATP-sensitive K+ channels).'),
('The amylin analog acts by:','Delaying gastric emptying',['Increasing insulin release','Blocking SGLT2','Decreasing insulin resistance'],'Amylin analog: delays gastric emptying.'),
])
unit('Insulin: Duration of Action Classification',
 'Ultra-short acting (just before food B/F): Afrezza (fastest acting). Short acting: fast-acting AKA monomeric insulin - glulisine, lispro, aspart (15 min B/F) and slow acting regular insulin (60 min B/F); both manage post-prandial hyperglycemia. Intermediate acting (BD/TDS dosing): neutral protamine Hagedorn (NPH) and lente. Long acting (OD/BD dosing): detemir (increased plasma protein binding), glargine (acidic pH), degludec (hexameric) - longest acting; these maintain blood glucose.')
facts(208,[
('The fastest acting insulin is:','Afrezza',['Lispro','Glulisine','Regular insulin'],'Ultra-short acting: just before food (B/F) - Afrezza (fastest acting).'),
('Ultra-short acting insulin is taken:','Just before food (B/F)',['60 min before food','30 min after food','At bedtime only'],'Ultra-short acting: just before food (B/F).'),
('The monomeric insulins (fast acting, 15 min B/F) are:','Glulisine, lispro and aspart',['Regular insulin and NPH','Detemir and glargine','Insulin zinc and protamine'],'Fast acting AKA monomeric insulin: glulisine, lispro, aspart - 15 min B/F.'),
('Regular insulin is a:','Slow acting short acting insulin taken 60 min B/F',['Fast acting insulin at 15 min B/F','Intermediate acting insulin','Long acting insulin'],'Short acting: slow acting - regular insulin 60 min B/F.'),
('The insulins used for management of postprandial hyperglycemia are:','Fast acting and regular insulin',['NPH and lente','Detemir and glargine','Degludec only'],'Short acting group: for management of postprandial hyperglycemia.'),
('The intermediate acting insulins are:','Neutral protamine Hagedorn (NPH) and lente',['Glargine and detemir','Regular and aspart','Degludec and detemir'],'Intermediate acting: dosing BD/TDS - NPH, lente.'),
('The dosing of intermediate acting insulins is:','BD / TDS',['OD only','Once weekly','Continuous infusion only'],'Intermediate acting: dosing BD/TDS.'),
('The long acting insulins are:','Detemir, glargine and degludec',['NPH and lente','Regular and lispro','Afrezza and aspart'],'Long acting: detemir, glargine, degludec.'),
('The long acting insulin with increased plasma protein binding is:','Detemir',['Glargine','Degludec','NPH'],'Detemir: increased plasma protein binding.'),
('The long acting insulin prepared at acidic pH is:','Glargine',['Detemir','Degludec','Lente'],'Glargine: acidic pH.'),
('The hexameric long acting insulin is:','Degludec',['Glargine','Detemir','Lente'],'Degludec: hexameric.'),
('The longest acting insulin is:','Degludec',['Glargine','Detemir','NPH'],'Long acting: degludec - longest acting.'),
('The dosing of long acting insulins is:','OD / BD',['BD / TDS','Before each meal','Once weekly'],'Long acting: dosing OD/BD.'),
('The insulins used for maintenance of blood glucose are:','Intermediate and long acting',['Fast acting and regular','Only ultra-short acting','Only monomeric insulins'],'Intermediate + long acting: for maintenance of blood glucose.'),
])
unit('Routes of Insulin Administration',
 'Inhalational insulin is Afrezza (absorbed through lung capillaries - fastest action); subcutaneous route is used for all other insulins; IV regular insulin is used in hyperkalemia and is the DOC in diabetic ketoacidosis.')
facts(208,[
('The inhalational insulin is:','Afrezza',['Lispro','Regular insulin','NPH'],'Route: inhalational - Afrezza (absorbed through lung capillaries - fastest action).'),
('Afrezza produces the fastest action because it is:','Absorbed through lung capillaries',['Given intravenously','A monomeric analog','Not protein bound'],'Afrezza: absorbed through lung capillaries - fastest action.'),
('The route for all other insulins (except Afrezza and IV regular) is:','Subcutaneous',['Oral','Intramuscular','Rectal'],'Route: subcutaneous - all other insulins.'),
('IV regular insulin is used in:','Hyperkalemia and diabetic ketoacidosis (DOC)',['Hypercalcemia','Diabetic gastroparesis','Insulinoma diagnosis'],'I/V route: regular insulin used in hyperkalemia, diabetic ketoacidosis (DOC).'),
('The DOC for diabetic ketoacidosis is:','IV regular insulin',['SC lispro','Inhaled Afrezza','NPH infusion'],'I/V regular insulin: diabetic ketoacidosis (DOC).'),
])
unit('Insulin Regimen and Mixing Rules',
 'Regimen: 1 insulin for management of PPH (post-prandial hyperglycemia) + 1 insulin for maintenance of blood glucose. If both by S/C route: inject both in the same syringe - NPH + regular insulin with regular drawn first to prevent contamination of the vial with cloudy NPH, or inject in different syringes. Continuous infusion is preferred in in-patient cases using regular insulin with decreased risk of hypoglycemia (no peak in plasma concentration).')
facts(209,[
('The standard insulin regimen consists of:','1 insulin for management of PPH + 1 insulin for maintenance of blood glucose',['2 maintenance insulins only','Only pre-mixed insulin','3 insulins always'],'Regimen: 1 insulin for management of PPH + 1 insulin for maintenance of blood glucose.'),
('When NPH and regular insulin are mixed in the same syringe:','Regular insulin is drawn first to prevent contamination of the vial with cloudy NPH',['NPH is drawn first','They can never be mixed','Insulin diluent is drawn first'],'If both S/C: inject both in same syringe - NPH + regular; regular drawn first to prevent contamination of vial with cloudy NPH.'),
('Which insulin is drawn first in a mixed syringe?','Regular insulin',['NPH','Lente','Detemir'],'Regular drawn first (to prevent contamination of the vial with cloudy NPH).'),
('The insulin preferred for continuous infusion is:','Regular insulin',['NPH','Lispro','Glargine'],'Continuous infusion: regular insulin used.'),
('Continuous insulin infusion is preferred in:','In-patient cases',['All out-patients','Once weekly home therapy','Pregnancy only'],'Continuous infusion: preferred in in-patient cases.'),
('Continuous infusion of regular insulin decreases the risk of hypoglycemia because:','There is no peak in plasma concentration',['The dose is halved','Absorption is slower','Antibodies form'],'Continuous infusion: decreased risk of hypoglycemia (no peak in plasma concentration).'),
])
unit('Sites of Subcutaneous Insulin Injection',
 'Sites: abdomen (m/c, except periumbilical site due to increased risk of lipodystrophy; advantages - faster and most reliable absorption), upper arm, antero-lateral aspect of thigh and upper area of buttocks.')
facts(209,[
('The most common site of subcutaneous insulin injection is:','Abdomen',['Thigh','Upper arm','Buttocks'],'Sites: abdomen - m/c.'),
('The part of the abdomen avoided for insulin injection is:','Periumbilical site',['Lower abdomen','Flanks','Upper abdomen'],'Abdomen: except periumbilical site (D/t increased risk of lipodystrophy).'),
('The periumbilical site is avoided because of:','Increased risk of lipodystrophy',['Poor absorption','Pain','Infection risk only'],'Abdomen: except periumbilical site (D/t increased risk of lipodystrophy).'),
('The advantages of abdominal insulin injection are:','Faster and most reliable absorption',['Slowest absorption','Least pain','No lipodystrophy risk'],'Abdomen advantages: faster & most reliable absorption.'),
('Which of the following is a correct insulin injection site?','Antero-lateral aspect of thigh',['Medial thigh','Over bony prominences','Periumbilical area'],'Sites: abdomen, upper arm, antero-lateral aspect of thigh, upper area of buttocks.'),
])
unit('Afrezza and Lente Insulin',
 'Afrezza is available as powder in color-coded cartridges: blue - 4U, green - 8U, yellow - 12U. Side effects: cough and increased risk of lung cancer; C/I: bronchial asthma/COPD and smokers. Lente: insulin + zinc precipitates into ultralente (long acting white crystals, 70%) and semilente (short acting white powder, 30%); the combination lente is intermediate acting.')
facts(209,[
('Afrezza is available as:','Powder in color-coded cartridges',['Liquid pen injectors','Intravenous vials','Transdermal patches'],'Afrezza: available as powder in color-coded cartridges.'),
('The blue Afrezza cartridge contains:','4U',['8U','12U','2U'],'Afrezza cartridges: blue - 4U.'),
('The green Afrezza cartridge contains:','8U',['4U','12U','16U'],'Afrezza cartridges: green - 8U.'),
('The yellow Afrezza cartridge contains:','12U',['4U','8U','20U'],'Afrezza cartridges: yellow - 12U.'),
('The side effects of Afrezza are:','Cough and increased risk of lung cancer',['Weight gain and edema','Lipodystrophy and hypoglycemia only','Hepatotoxicity'],'Afrezza S/E: cough; increased risk of lung cancer.'),
('Afrezza is contraindicated in:','Bronchial asthma/COPD and smokers',['Hypertension','Renal failure','Elderly'],'Afrezza C/I: bronchial asthma/COPD; smokers.'),
('Lente insulin is prepared by adding:','Zinc to insulin',['Protamine to insulin','Zinc and protamine','Sulfate groups'],'Lente: insulin + zinc precipitates into ultralente and semilente.'),
('Ultralente is:','Long acting white crystals (70%)',['Short acting white powder (70%)','Intermediate acting','Rapid acting'],'Ultralente: long acting white crystals - 70%.'),
('Semilente is:','Short acting white powder (30%)',['Long acting white crystals (30%)','Intermediate acting','A protamine complex'],'Semilente: short acting white powder - 30%.'),
('The combination of ultralente (70%) and semilente (30%) is called:','Lente (intermediate acting)',['Ultralente','Semilente','NPH'],'70% ultralente + 30% semilente = lente: intermediate acting.'),
])
unit('Side Effects of Insulins',
 'Hypoglycemia is the most common side effect; plasma concentration is proportional to the risk of hypoglycemia - shorter acting insulins carry higher risk, and glargine (long-acting) gives a smooth peakless graph. Other side effects: hypokalemia and lipodystrophy (lipo-hypertrophy and lipo-atrophy) prevented by rotation of injection site with at least 1 inch between each site.')
facts(210,[
('The most common side effect of insulin is:','Hypoglycemia',['Lipodystrophy','Hypokalemia','Weight gain'],'S/E of insulins 1: hypoglycemia (m/c).'),
('The risk of hypoglycemia with insulin is proportional to:','Plasma concentration of insulin',['Duration of diabetes','Body weight','HbA1c level'],'S/E: plasma concentration is proportional to risk of hypoglycemia.'),
('Which insulin has the highest risk of hypoglycemia?','Shorter acting insulins',['Long acting insulins','Peakless analogs','Intermediate acting only'],'Shorter acting -> increased risk of hypoglycemia.'),
('The insulin with a smooth peakless plasma concentration graph is:','Glargine (long acting)',['Regular insulin','Lispro','Afrezza'],'Smooth peakless graph: glargine (long acting).'),
('In the insulin concentration-time graph, the curves in decreasing peak order are:','Afrezza, fast acting, regular, intermediate, long acting',['Regular, Afrezza, fast acting...','Long acting has the highest peak','All peaks are equal'],'Graph: A (Afrezza) highest peak, then FA, R, IA, LA flat.'),
('The electrolyte side effect of insulin is:','Hypokalemia',['Hyperkalemia','Hypocalcemia','Hyponatremia'],'S/E of insulins 2: hypokalemia.'),
('The injection site side effect of insulin is:','Lipodystrophy (lipo-hypertrophy and lipo-atrophy)',['Necrosis Ulcerans','Granuloma annulare','Pyoderma'],'S/E 3: lipodystrophy - lipo-hypertrophy, lipo-atrophy.'),
('Lipodystrophy from insulin is prevented by:','Rotation of site of injection with at least 1 inch between each site',['Using longer needles','Only using the abdomen','Mixing insulins'],'Prevention: rotation of site of injection with >=1 inch between each site.'),
])
finish()

# CHAPTER 52 - ANTIDIABETIC DRUGS: PART 2 (p211-214) ---------------------------
start(52)
unit('Drugs That Increase Release of Insulin: Classification',
 'Two groups: GLP-1 related drugs (GLP-1 agonists, DPP-IV inhibitors, dual GLP-1 & GIP agonist) and inhibitors of ATP-sensitive K+ channels (sulfonylureas and meglitinides). The common side effect of all is hypoglycemia.')
facts(211,[
('The drugs that increase release of insulin are grouped into:','GLP-1 related drugs and inhibitors of ATP-sensitive K+ channels',['Biguanides and thiazolidinediones','SGLT blockers and alpha-glucosidase inhibitors','Amylin analogs and insulin'],'Classification: GLP-1 related drugs + inhibitors of ATP-sensitive K+ channels.'),
('The GLP-1 related drug groups are:','GLP-1 agonists, DPP-IV inhibitors and dual GLP-1 & GIP agonist',['Sulfonylureas and meglitinides','Biguanides and glitazones','Insulin and amylin analogs'],'GLP-1 related: GLP-1 agonist, DPP-IV inhibitors, dual GLP-1 & GIP agonist.'),
('The inhibitors of ATP-sensitive K+ channels are:','Sulfonylureas and meglitinides',['DPP-4 inhibitors and GLP-1 agonists','Metformin and acarbose','Pioglitazone and rosiglitazone'],'Inhibitors of ATP sensitive K+ channels: sulfonylureas, meglitinides.'),
('The common side effect of insulin-releasing drugs is:','Hypoglycemia',['Pancreatitis','Lactic acidosis','Weight loss always'],'Common S/E: hypoglycemia.'),
])
unit('GLP-1 Agonists',
 'Drugs: liraglutide (OD dosage) and dulaglutide, albiglutide, semaglutide (once a week dosage); route S/C except oral semaglutide (OD dosage). Side effects: pancreatitis, nausea & vomiting (due to delayed gastric emptying) and weight loss (due to decreased appetite) - DOC for obesity with oral semaglutide > S/C semaglutide > S/C liraglutide.')
facts(211,[
('The GLP-1 agonist with OD (once daily) dosage is:','Liraglutide',['Dulaglutide','Albiglutide','Semaglutide S/C'],'GLP-1 agonists: liraglutide - OD dosage.'),
('The GLP-1 agonists given once a week are:','Dulaglutide, albiglutide and semaglutide',['Liraglutide and exenatide','Only albiglutide','Lixisenatide and liraglutide'],'Once a week dosage: dulaglutide, albiglutide, semaglutide.'),
('The route of GLP-1 agonists is:','S/C (except oral semaglutide)',['Oral only','I/M weekly','Intranasal'],'Route: S/C; oral semaglutide (OD dosage).'),
('The side effects of GLP-1 agonists include all EXCEPT:','Weight gain',['Pancreatitis','Nausea & vomiting','Weight loss'],'S/E: pancreatitis; nausea & vomiting (D/t delayed gastric emptying); weight loss (D/t decreased appetite).'),
('Nausea and vomiting with GLP-1 agonists occur due to:','Delayed gastric emptying',['Increased gastric motility','Vagal stimulation','Direct chemoreceptor trigger zone toxicity'],'S/E: nausea & vomiting (D/t delayed gastric emptying).'),
('Weight loss with GLP-1 agonists occurs due to:','Decreased appetite',['Malabsorption','Increased metabolism','Nausea only'],'Weight loss (D/t decreased appetite).'),
('The DOC for obesity among GLP-1 agonists is:','Semaglutide',['Liraglutide','Dulaglutide','Albiglutide'],'Weight loss - DOC for obesity.'),
('The correct efficacy order for weight loss (obesity) is:','Oral semaglutide > S/C semaglutide > S/C liraglutide',['S/C liraglutide > oral semaglutide','Dulaglutide > semaglutide','All are equal'],'Oral semaglutide > S/C semaglutide > S/C liraglutide.'),
])
unit('DPP-IV Inhibitors',
 'MOA: decreased metabolism of GLP-1 (weight-neutral drugs as only endogenous GLP-1 action increases). Drugs: sitagliptin, saxagliptin, alogliptin, linagliptin. Route: oral. Side effects: pancreatitis, angioedema (increased risk with ACE inhibitors) and increased risk of infections by blocking DAA6 in lymphocytes. C/I: renal failure except linagliptin (excretion by liver).')
facts(211,[
('The MOA of DPP-IV inhibitors is:','Decreased metabolism of GLP-1',['Stimulation of GLP-1 secretion','Direct insulin release','GLP-1 receptor antagonism'],'DPP-IV inhibitors MOA: decreased metabolism of GLP-1.'),
('DPP-IV inhibitors are weight-neutral because:','Only endogenous GLP-1 action is increased',['They block appetite centers','They increase GLP-1 supraphysiologically','They cause nausea reducing intake'],'Note: DPP-IV inhibitors are weight-neutral drugs as only endogenous GLP-1 action increases.'),
('The DPP-IV inhibitors are:','Sitagliptin, saxagliptin, alogliptin and linagliptin',['Liraglutide and semaglutide','Repaglinide and nateglinide','Cana and empagliflozin'],'DPP-IV inhibitors: sitagliptin, saxagliptin, alogliptin, linagliptin.'),
('The route of DPP-IV inhibitors is:','Oral',['Subcutaneous','Intravenous','Inhalational'],'DPP-IV inhibitors route: oral.'),
('The side effects of DPP-IV inhibitors include all EXCEPT:','Hypoglycemia (weight-neutral)',['Pancreatitis','Angioedema','Increased infections'],'S/E: pancreatitis; angioedema; increased risk of infections.'),
('Angioedema with DPP-IV inhibitors has increased risk with:','ACE inhibitors',['ARBs','Beta blockers','Calcium channel blockers'],'S/E: angioedema (increased risk with ACE inhibitors).'),
('DPP-IV inhibitors increase risk of infections by:','Blocking DAA6 in lymphocytes',['Suppressing neutrophils','Blocking complement','Inhibiting immunoglobulin synthesis'],'S/E: increased risk of infections - by blocking DAA6 in lymphocytes.'),
('DPP-IV inhibitors are contraindicated in renal failure EXCEPT:','Linagliptin (excretion by liver)',['Sitagliptin','Saxagliptin','Alogliptin'],'C/I: renal failure (except linagliptin D/t excretion by liver).'),
])
unit('Dual GLP-1 and GIP Agonist',
 'Drug: tirzepatide. Route: S/C. Efficiency: greater than pure GLP-1 agonists.')
facts(211,[
('The dual GLP-1 & GIP agonist is:','Tirzepatide',['Semaglutide','Liraglutide','Exenatide'],'Dual GLP-1 & GIP agonist drug: tirzepatide.'),
('The route of tirzepatide is:','S/C',['Oral','I/V','Transdermal'],'Tirzepatide route: S/C.'),
('The efficiency of tirzepatide compared to pure GLP-1 agonists is:','Greater',['Lesser','Equal','Unknown'],'Efficiency: > pure GLP-1 agonist.'),
])
unit('Inhibitors of ATP-Sensitive K+ Channels: Sulfonylureas vs Meglitinides',
 'Sulfonylureas release large amounts of insulin, are long acting and used for maintenance of blood glucose; meglitinides release small amounts, are short acting and manage post-prandial hyperglycemia. Side effects (sulfonylureas > meglitinides): hypoglycemia and weight gain (due to block of hormone sensitive lipase) used in thin diabetics. Sulfonylurea C/I: alcohol consumption causing disulfiram-like effect. Drugs: glyburide (AKA glibenclamide), glimepiride, gliclazide; nateglinide (phenylalanine derivative) and repaglinide. Note: risk of hypoglycemia - insulin (highest overall) > sulfonylureas.')
facts(212,[
('Insulin release with sulfonylureas is:','Large amount',['Small amount','Glucose dependent only','Basal only'],'Table: insulin release - sulfonylureas large amount; meglitinides small amount.'),
('Meglitinides release insulin in:','Small amount',['Large amount','Bolus bursts','No amount'],'Meglitinides: small amount of insulin release.'),
('The duration of action of sulfonylureas is:','Long acting',['Short acting','Ultra-short','Intermediate only'],'T 1/2: sulfonylureas long acting; meglitinides short acting.'),
('The use of meglitinides is:','Management of post-prandial hyperglycemia',['Maintenance of blood glucose','DKA treatment','Prophylaxis of DM'],'Meglitinides use: management of post-prandial hyperglycemia.'),
('The use of sulfonylureas is:','Maintenance of blood glucose',['Only post-prandial control','DKA','GDM first choice'],'Sulfonylureas use: maintenance of blood glucose.'),
('The side effects of sulfonylureas are:','Hypoglycemia and weight gain (S/E sulfonylureas > meglitinides)',['Weight loss and lactic acidosis','Pancreatitis and angioedema','Edema and fractures'],'S/E: hypoglycemia; weight gain (S/E sulfonylureas > meglitinides).'),
('Weight gain with sulfonylureas occurs due to:','Block of hormone sensitive lipase',['Increased appetite center stimulation','Insulin edema','Decreased metabolism'],'Weight gain (D/t block of hormone sensitive lipase).'),
('Weight gain with sulfonylureas is beneficially used in:','Thin diabetics',['Obese diabetics','All T1DM','Gestational diabetes'],'Weight gain: used in thin diabetics.'),
('Sulfonylureas are contraindicated with alcohol because of:','Disulfiram-like effect',['Severe hypoglycemia only','Lactic acidosis','Hepatotoxicity'],'C/I: alcohol consumption - causes disulfiram-like effect.'),
('The sulfonylurea drugs are:','Glyburide (AKA glibenclamide), glimepiride and gliclazide',['Nateglinide and repaglinide','Sitagliptin and vildagliptin','Pioglitazone and rosiglitazone'],'Sulfonylurea drugs: glyburide (AKA glibenclamide), glimepiride, gliclazide.'),
('Nateglinide is a:','Phenylalanine derivative (meglitinide)',['Sulfonylurea','Biguanide','DPP-IV inhibitor'],'Meglitinide drugs: nateglinide (phenylalanine derivative), repaglinide.'),
('The highest overall risk of hypoglycemia is with:','Insulin, then sulfonylureas',['Meglitinides','DPP-IV inhibitors','Metformin'],'Note: risk of hypoglycemia - insulin (highest overall) > sulfonylureas.'),
])
unit('Thiazolidinediones',
 'Oral hypoglycemic agents which decrease insulin resistance. Drugs: pioglitazone and rosiglitazone. MOA: stimulate PPAR-gamma -> increased GLUT-4 production (decreasing insulin resistance) and adipocyte proliferation. Side effects: retention of Na+ & water (due to block of ENaC) causing edema & congestive heart failure; macular edema (must be differentiated from diabetic etiology); bone fracture in females; increased risk for Ca bladder; hepatotoxic.')
facts(212,[
('Thiazolidinediones are OHAs which:','Decrease insulin resistance',['Increase insulin release','Block SGLT2','Inhibit gluconeogenesis'],'Thiazolidinediones: oral hypoglycemic agents which decrease insulin resistance.'),
('The thiazolidinedione drugs are:','Pioglitazone and rosiglitazone',['Metformin and phenformin','Glimepiride and gliclazide','Canagliflozin and dapagliflozin'],'TZD drugs: pioglitazone, rosiglitazone.'),
('The MOA of thiazolidinediones is:','Stimulate PPAR-gamma -> increased GLUT-4 production and adipocyte proliferation',['Block ATP-sensitive K+ channels','Stimulate AMP kinase','Inhibit DPP-4'],'MOA: stimulate PPAR-gamma -> increased GLUT-4 production (decreased insulin resistance) + adipocyte proliferation.'),
('Edema with thiazolidinediones occurs due to:','Retention of Na+ & water (block of ENaC)',['Heart failure only','Hypoalbuminemia','Increased ADH'],'S/E: retention of Na+ & water (D/t block of ENaC) -> edema & CHF.'),
('The serious cardiac side effect of thiazolidinediones is:','Congestive heart failure (edema)',['MI always','Arrhythmia','Pericarditis'],'S/E: edema & congestive heart failure (CHF).'),
('The eye side effect of thiazolidinediones is:','Macular edema (must be differentiated from diabetic etiology)',['Papilledema','Optic neuritis','Cataract'],'S/E: macular edema - must be differentiated from diabetic etiology.'),
('Thiazolidinediones increase the risk of:','Bone fracture in females and Ca bladder',['Fracture in males only','Prostate cancer','Pancreatic cancer'],'S/E: bone fracture in females; increased risk for Ca bladder.'),
('The hepatic side effect of thiazolidinediones is:','Hepatotoxic',['Hepato-protective effect','No liver effect','Chronic hepatitis C cure'],'S/E: hepatotoxic.'),
])
unit('Biguanides: Metformin',
 'OHA causing decreased hepatic glucose production. MOA: stimulates AMPK (adenosine monophosphate kinase) which blocks gluconeogenesis. Use: DOC for treatment & prophylaxis of both T1 & T2 DM; PCOS (treatment of anovulation due to decreased insulin resistance); non-alcoholic steatohepatitis (NASH); antipsychotic induced obesity - only FDA-approved drug. Side effects: metabolic acidosis (inhibition of mitochondrial aerobic glycolysis), decreased absorption of vit B12 (prevented by Ca2+ supplements - Ca2+ dependent absorption) and weight loss. Note: drugs causing weight loss - mnemonic GAMs: GLP-1 agonist, Amylin analogue, Metformin, SGLT-2 blockers.')
facts(212,[
('The biguanide drug is:','Metformin',['Phenformin (currently used)','Pioglitazone','Acarbose'],'Biguanide drug: metformin.'),
('Biguanides act by causing:','Decreased hepatic glucose production',['Increased insulin release','Increased GLUT-4 only','Block of SGLT2'],'Biguanides: OHA causing decreased hepatic glucose production.'),
('The MOA of metformin is:','Stimulates AMPK which blocks gluconeogenesis',['Blocks ATP-sensitive K+ channels','Stimulates PPAR-gamma','Inhibits SGLT2'],'MOA: stimulates AMPK (adenosine monophosphate kinase) -> blocks gluconeogenesis.'),
('Metformin is the DOC for:','Treatment & prophylaxis of both T1 & T2 DM',['Only T2DM treatment','Only prediabetes','GDM first trimester'],'Use: DOC for treatment & prophylaxis of both T1 & T2 DM.'),
('Metformin is used in PCOS for:','Treatment of anovulation (due to decreased insulin resistance)',['Ovulation induction via FSH','Hyperandrogenism block directly','Contraception'],'Use: PCOS - treatment of anovulation (D/t decreased insulin resistance).'),
('Metformin is used in:','Non-alcoholic steatohepatitis (NASH)',['Alcoholic cirrhosis','Acute hepatitis A','Hepatocellular carcinoma'],'Use: non-alcoholic steatohepatitis (NASH).'),
('The only FDA-approved drug for antipsychotic induced obesity is:','Metformin',['Orlistat','Semaglutide','Topiramate'],'Use: antipsychotic induced obesity - only FDA-approved drug.'),
('Metabolic acidosis with metformin occurs due to:','Inhibition of mitochondrial aerobic glycolysis',['Renal bicarbonate loss','Lactate overproduction in muscles only','Ketoacid formation'],'S/E: metabolic acidosis - inhibition of mitochondrial aerobic glycolysis.'),
('Metformin decreases absorption of:','Vitamin B12',['Vitamin D','Iron','Folate'],'S/E: decreased absorption of vit B12.'),
('Vitamin B12 malabsorption with metformin is prevented by:','Ca2+ supplements (Ca2+ dependent absorption)',['B12 injections always','Folate supplements','Stopping metformin'],'S/E: decreased vit B12 absorption - prevented by Ca2+ supplements (D/t Ca2+ dependent absorption).'),
('The weight effect of metformin is:','Weight loss',['Weight gain','Weight neutral always','Initial gain then loss'],'S/E: weight loss.'),
('The mnemonic for drugs causing weight loss is:','GAMs (GLP-1 agonist, Amylin analogue, Metformin, SGLT-2 blockers)',['GAMS - Gliclazide, Acarbose...','WEIGHT loss mnemonic','SLIM mnemonic'],'Note: drugs causing weight loss - mnemonic GAMs: GLP-1 agonist, Amylin analogue, metformin, SGLT-2 blockers.'),
])
unit('SGLT Blockers',
 'Drugs: canagliflozin, dapagliflozin and empagliflozin (SGLT-2 blockers) and sotagliflozin (SGLT-1 & 2 blocker). MOA: decreased glucose reabsorption in kidney (SGLT-2) and small intestine (SGLT-1). Use: DM and chronic CHF (to decrease mortality by decreasing preload due to diuresis). Common side effects: due to increased Na+ in urine - diuresis, hypotension, dehydration; due to glucose in urine - increased risk of UTI and vaginal infections (e.g. Candida). Rare: bone fracture (incidence increased in elderly, male & female), Fournier\'s gangrene and urosepsis.')
facts(213,[
('The SGLT-2 blocker drugs are:','Canagliflozin, dapagliflozin and empagliflozin',['Sotagliflozin only','Metformin and acarbose','Sitagliptin and linagliptin'],'Drugs: canagliflozin, dapagliflozin, empagliflozin - SGLT-2 blocker.'),
('The dual SGLT-1 & 2 blocker is:','Sotagliflozin',['Empagliflozin','Canagliflozin','Dapagliflozin'],'Sotagliflozin: SGLT-1 & 2 blocker.'),
('The MOA of SGLT blockers is:','Decreased glucose reabsorption in kidney (SGLT-2) and small intestine (SGLT-1)',['Increased renal glucose reabsorption','Blocking GLUT-4','Inhibiting gluconeogenesis'],'MOA: decreased glucose reabsorption in kidney (SGLT-2) and small intestine (SGLT-1).'),
('SGLT blockers decrease mortality in chronic CHF by:','Decreasing preload due to diuresis',['Improving contractility','Reducing afterload','Blocking renin'],'Use: chronic CHF (to decrease mortality) - decreased preload D/t diuresis.'),
('The common side effects due to increased Na+ in urine with SGLT blockers are:','Diuresis, hypotension and dehydration',['Hyperkalemia','Edema','Hypertension'],'S/E common: D/t increased Na+ in urine - diuresis, hypotension, dehydration.'),
('The common side effects due to glucose in urine with SGLT blockers are:','Increased risk of UTI and vaginal infections (e.g. Candida)',['Renal stones','Crystalluria with hematuria','Neurogenic bladder'],'S/E: D/t glucose in urine - increased risk of UTI; increased risk of vaginal infections (e.g. Candida).'),
('The rare side effects of SGLT blockers are:','Bone fracture, Fournier\'s gangrene and urosepsis',['Pancreatitis and angioedema','Lactic acidosis','Optic neuritis'],'Rare: bone fracture; Fournier\'s gangrene; urosepsis.'),
('Bone fracture incidence with SGLT blockers is increased in:','Elderly, both male & female',['Only young males','Only premenopausal females','Children'],'Rare: bone fracture - incidence increased in elderly, male & female.'),
])
unit('Alpha-Glucosidase Inhibitors and Amylin Analog',
 'Alpha-glucosidase inhibitors: acarbose, voglibose and miglitol; use - post-prandial hyperglycemia in T2DM only; dosage - during meal (after few bites); side effects - flatulence (m/c, due to intestinal flora acting on undigested starch & disaccharides) and osmotic diarrhea. Amylin analog: pramlintide - S/C, delays gastric emptying, decreases post-prandial hyperglycemia in both T1 & T2 DM; if used with insulin use a different syringe and decrease insulin dose by 50%; side effects nausea & vomiting and weight loss (off-label use in obesity). Note: decreased CVS mortality seen with SGLT2 blockers and GLP-1 agonists. C/I of metformin (increased lactic acidosis): chronic alcoholism, severe lung disease (COPD), renal failure, liver failure and CHF; smoking does not increase lactic acidosis - not a C/I in metformin use.')
facts(214,[
('The alpha-glucosidase inhibitors are:','Acarbose, voglibose and miglitol',['Metformin and buformin','Sitagliptin and saxagliptin','Pramlintide and liraglutide'],'Alpha-glucosidase inhibitors: acarbose, voglibose, miglitol.'),
('Alpha-glucosidase inhibitors are used for post-prandial hyperglycemia in:','T2DM only',['T1DM only','Both T1 and T2DM','GDM only'],'Use: post-prandial hyperglycemia in T2DM only.'),
('Alpha-glucosidase inhibitors are taken:','During meal (after few bites)',['60 min before meal','2 hours after meal','At bedtime'],'Dosage: during meal (after few bites).'),
('The most common side effect of alpha-glucosidase inhibitors is:','Flatulence (intestinal flora acting on undigested starch & disaccharides)',['Osmotic diarrhea','Hypoglycemia','Lactic acidosis'],'S/E: flatulence (m/c) - D/t intestinal flora acting on undigested starch & disaccharides.'),
('The other side effect of alpha-glucosidase inhibitors is:','Osmotic diarrhea',['Constipation','Steatorrhea with fat','Melena'],'S/E: osmotic diarrhea.'),
('The amylin analog drug is:','Pramlintide',['Exenatide','Lixisenatide','Dulaglutide'],'Amylin analog: pramlintide.'),
('The route of pramlintide is:','Subcutaneous',['Oral','Intravenous','Intranasal'],'Pramlintide route: S/C.'),
('The MOA of pramlintide is:','Delays gastric emptying',['Blocks glucagon receptor','Stimulates insulin release','Blocks SGLT1'],'Pramlintide MOA: delays gastric emptying.'),
('Pramlintide decreases post-prandial hyperglycemia in:','Both T1 & T2 DM',['T1DM only','T2DM only','GDM only'],'Use: decreased post-prandial hyperglycemia in both T1 & T2 DM.'),
('When pramlintide is used with insulin:','Use a different syringe and decrease insulin dose by 50%',['Mix in the same syringe','Increase insulin dose by 50%','Stop insulin'],'If used with insulin: use different syringe; decrease insulin dose by 50%.'),
('The side effects of pramlintide are:','Nausea & vomiting and weight loss (off-label use in obesity)',['Weight gain and edema','Hypokalemia','Pancreatitis only'],'S/E: nausea & vomiting; weight loss - off-label use in obesity.'),
('Decreased CVS mortality is seen with:','SGLT2 blockers and GLP-1 agonists',['Sulfonylureas and meglitinides','Acarbose and miglitol','Insulin and pramlintide'],'Note: decreased CVS mortality seen in SGLT2 blocker and GLP-1 agonist.'),
('The contraindications of metformin (increased lactic acidosis) are:','Chronic alcoholism, severe lung disease (COPD), renal failure, liver failure and CHF',['Smoking','Obesity','Hypertension'],'C/I of metformin: increased lactic acidosis - chronic alcoholism, severe lung disease (COPD), renal failure, liver failure, CHF.'),
('Which of the following is NOT a contraindication to metformin?','Smoking (does not increase lactic acidosis)',['Chronic alcoholism','Severe COPD','Heart failure'],'Smoking does not increase lactic acidosis: not C/I in metformin use.'),
])
finish()
