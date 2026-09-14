# -*- coding: utf-8 -*-
"""Generate chapters 37-41 from Marrow Pharmacology E8, book pp150-166."""
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

# CHAPTER 37 -----------------------------------------------------------------
start(37)
unit('Alcohol Metabolism and Toxic Alcohols','Ethanol is oxidised by alcohol dehydrogenase to acetaldehyde and then by aldehyde dehydrogenase to harmless acetic acid. Methanol and ethylene glycol traverse analogous pathways to lethal acids; ethanol and fomepizole competitively inhibit ADH, with fomepizole preferred.')
facts(150,[
('Ethanol is first converted by alcohol dehydrogenase into:','Acetaldehyde',['Acetic acid','Formaldehyde','Formic acid'],'Alcohol dehydrogenase converts alcohol to acetaldehyde.'),
('Acetaldehyde is converted to non-toxic acetic acid by:','Aldehyde dehydrogenase',['Alcohol dehydrogenase','Formaldehyde dehydrogenase','Glycolaldehyde dehydrogenase']),
('The final non-toxic product of ethanol metabolism shown is:','Acetic acid',['Acetaldehyde','Formic acid','Glycolic acid']),
('Acetic acid formed from ethanol is ultimately:','Excreted in urine',['Converted to methanol','Stored in adipose tissue','Exhaled unchanged']),
('Disulfiram produces alcohol aversion by blocking:','Aldehyde dehydrogenase',['Alcohol dehydrogenase','Monoamine oxidase','CYP2E1']),
('Methanol is converted by ADH into:','Formaldehyde',['Acetaldehyde','Glycolaldehyde','Acetic acid']),
('Formaldehyde is converted by formaldehyde dehydrogenase into toxic:','Formic acid',['Acetic acid','Lactic acid','Oxalic acid']),
('The toxic metabolite responsible for death after methanol ingestion is:','Formic acid',['Acetic acid','Acetaldehyde','Glycoaldehyde']),
('Ethylene glycol (antifreeze) is initially converted into:','Glycoaldehyde',['Formaldehyde','Acetaldehyde','Acetic acid']),
('Glycoaldehyde is further metabolised by GDH to:','Multiple toxic acids',['Non-toxic acetic acid','Only formic acid','Ethanol']),
('The drug of choice for methanol or ethylene-glycol toxicity is:','Fomepizole',['Disulfiram','Naltrexone','Acamprosate']),
('Ethanol and fomepizole treat toxic-alcohol poisoning by:','Competitive inhibition of alcohol dehydrogenase',['Activating aldehyde dehydrogenase','Chelating formic acid','Increasing renal acid reabsorption']),
('A patient who drank antifreeze should receive fomepizole to prevent formation of:','Multiple toxic acids from ethylene glycol',['Acetic acid from ethanol','Acetaldehyde from ethanol','Dopamine metabolites']),
])
unit('FDA-approved Drugs for Alcohol Dependence','The FDA-approved choices are disulfiram, naltrexone and acamprosate. Disulfiram creates aversion through acetaldehyde; naltrexone blocks the opioid reward pathway and can be oral, monthly IM or implanted; acamprosate inhibits glutamate and is taken orally three times daily.')
facts(150,[
('The FDA-approved alcohol-dependence drugs on the page are:','Disulfiram, naltrexone and acamprosate',['Diazepam, clonidine and baclofen','Topiramate, gabapentin and baclofen','Varenicline, bupropion and nicotine']),
('Accumulation of acetaldehyde during disulfiram therapy causes:','Palpitations, tremor, sweating and chest pain',['Miosis, constipation and sedation','Bradycardia and dry skin','Ataxia without autonomic symptoms']),
('Disulfiram is administered at what time of day?','In the morning',['At bedtime','Only with alcohol','Once monthly']),
('Disulfiram is reserved for:','A motivated patient',['Every patient in acute withdrawal','A patient who refuses abstinence','A patient with severe hepatic failure']),
('Minimum abstinence before starting disulfiram is:','12 hours',['No abstinence','1 hour','7 days']),
('The sleep-related adverse effect of disulfiram is:','Alteration of REM/NREM status',['Only vivid dreams','Somnambulism','Complete insomnia']),
('Monitoring recommended during disulfiram therapy is:','Liver function every 6 months',['Creatinine every day','ECG monthly','Audiometry yearly']),
('Naltrexone reduces alcohol reward as a:','Central opioid antagonist',['Glutamate agonist','Aldehyde-dehydrogenase inhibitor','Nicotinic agonist']),
('The drug of choice oral regimen for alcohol dependence is:','Naltrexone once daily',['Acamprosate once daily','Disulfiram three times daily','Fomepizole once monthly']),
('Abstinence before oral naltrexone for alcohol dependence is:','Not required',['12 hours required','One month required','Seven days required']),
('Long-acting naltrexone can be given as:','A monthly intramuscular dose',['A daily IV infusion','A weekly patch','An inhaled dose']),
('An additional long-duration naltrexone formulation mentioned is:','An implant',['A nasal spray','A suppository','An eye drop']),
('Naltrexone may worsen depression by causing:','Dysphoria',['Euphoria','Mania','Amnesia']),
('Naltrexone is contraindicated when LFT values are:','At least 3 times normal',['Below normal','Less than twice normal','Exactly normal']),
('Acamprosate acts by:','Inhibiting glutamate effects',['Blocking aldehyde dehydrogenase','Blocking opioid receptors','Stimulating nicotinic receptors']),
('The dosing schedule of acamprosate is:','Oral three times daily',['Oral once daily','Monthly intramuscular','Transdermal daily']),
])
unit('Non-FDA Drugs, Acute Withdrawal and Alcohol Treatment Algorithm','Non-approved options include benzodiazepines, clonidine, gabapentin, baclofen, topiramate and varenicline. A benzodiazepine is the drug of choice for acute withdrawal; for maintenance, LFT determines acamprosate versus naltrexone, then topiramate and finally disulfiram when topiramate is contraindicated.')
facts(151,[
('Which is a non-FDA-approved option for alcohol dependence?','Topiramate',['Disulfiram','Naltrexone','Acamprosate']),
('The six non-FDA-approved options listed include benzodiazepines, clonidine, gabapentin, baclofen, topiramate and:','Varenicline',['Fomepizole','Methadone','Naloxone']),
('The drug of choice for acute alcohol withdrawal is:','A benzodiazepine',['Naltrexone','Acamprosate','Varenicline']),
('Among non-approved maintenance agents, the preferred drug is:','Topiramate',['Clonidine','Gabapentin','Baclofen']),
('The initial investigation in a new alcohol-dependence case is:','Liver function testing',['Renal biopsy','Audiometry','Spirometry']),
('If LFT is at least three times normal, first treatment is:','Acamprosate',['Naltrexone','Topiramate','Disulfiram']),
('If LFT is less than three times normal, first treatment is:','Naltrexone',['Acamprosate','Disulfiram','Fomepizole']),
('After inadequate response to acamprosate, the next drug is:','Naltrexone',['Disulfiram','Clonidine','Fomepizole']),
('After inadequate response to naltrexone, the next drug is:','Topiramate',['Acamprosate','Diazepam','Fomepizole']),
('Topiramate is contraindicated in:','Renal stones and glaucoma',['Depression and insomnia','Asthma and COPD','Anaemia and neutropenia']),
('If topiramate is contraindicated, the algorithm proceeds to:','Disulfiram',['Fomepizole','Clonidine','Bupropion']),
])
unit('Smoking Dependence: First- and Second-line Therapy','First-line therapies are bupropion, oral varenicline and nicotine replacement. Varenicline is the most effective and the drug of choice; NRT combines a long-acting patch with a short-acting rescue form. Cytisine, nortriptyline and clonidine are second line.')
facts(151,[
('First-line smoking-cessation options are:','Bupropion, varenicline and nicotine replacement therapy',['Cytisine, nortriptyline and clonidine','Diazepam, baclofen and topiramate','Disulfiram, naltrexone and acamprosate']),
('The drug of choice and most effective drug for smoking dependence is:','Varenicline',['Bupropion','Cytisine','Nortriptyline']),
('Varenicline is a synthetic drug derived from:','Cytisine',['Nicotine','Clonidine','Nortriptyline']),
('The route used for varenicline in smoking dependence is:','Oral',['Intranasal','Transdermal','Intramuscular']),
('Varenicline acts as a nicotinic receptor:','Agonist',['Antagonist','Inverse agonist','Channel blocker']),
('At the alpha4-beta2 nicotinic receptor, varenicline is a:','Partial agonist',['Full agonist','Antagonist','Inverse agonist']),
('At the alpha7 nicotinic receptor, varenicline is a:','Full agonist',['Partial agonist','Antagonist','Allosteric inhibitor']),
('The mnemonic VA recalls varenicline adverse effects as:','Vomiting/nausea and abnormal sleep',['Vertigo and anaemia','Visual loss and anorexia','Vomiting and agranulocytosis']),
('Abnormal sleep with varenicline may manifest as:','Somnambulism',['Narcolepsy','Sleep paralysis only','Night blindness']),
('An atypical intranasal use of varenicline is:','Dry-eye disease',['Glaucoma','Allergic rhinitis','Epistaxis']),
('Intranasal varenicline increases lacrimation through the:','Trigeminal nerve and nasolacrimal reflex',['Optic nerve','Facial motor nucleus only','Vagus nerve']),
('Long-acting nicotine replacement is provided by a:','Patch lasting 16-24 hours',['Nasal spray','Gum','Lozenge']),
('The nicotine patch should be applied:','Once daily to a hairless area',['Hourly to the scalp','Weekly to broken skin','Only when craving occurs']),
('Short-acting NRT is used for:','Breakthrough craving',['Maintenance only','Alcohol withdrawal','Sleep induction']),
('The most effective short-acting NRT route is:','Nasal spray',['Gum','Lozenge','Patch']),
('Nicotine gum and lozenges are available as:','Over-the-counter drugs',['Schedule X drugs','Narcotic drugs','Hospital-only drugs']),
('Nicotine nasal spray is classified as a:','Schedule H drug',['OTC drug','Schedule X drug','Schedule G drug']),
('The recommended NRT regimen combines:','Patch plus gum, lozenge or nasal spray',['Two patches only','Gum plus alcohol','Varenicline plus disulfiram']),
('A new smoking-dependence case may start with:','Oral varenicline or NRT',['Cytisine only','Clonidine only','Nortriptyline only']),
('If a single first-line option gives inadequate response, the next step is:','Combine oral varenicline and NRT',['Stop all treatment','Use disulfiram','Switch to diazepam']),
])
facts(152,[
('The second-line therapies for smoking dependence are:','Cytisine, nortriptyline and clonidine',['Varenicline, bupropion and NRT','Disulfiram, naltrexone and acamprosate','Gabapentin, baclofen and diazepam']),
('Cytisine is a:','Plant derivative',['Synthetic opioid','Tricyclic antidepressant','Alpha-2 agonist']),
('The mechanism of cytisine is:','The same as varenicline',['Aldehyde-dehydrogenase inhibition','Opioid antagonism','Glutamate inhibition']),
('The tricyclic antidepressant used second-line for smoking cessation is:','Nortriptyline',['Amitriptyline','Imipramine','Clomipramine']),
('Withdrawal symptoms with cytisine, nortriptyline and clonidine are described as:','Minimal',['Severe','Unchanged','Fatal']),
])
finish()

# CHAPTER 38 -----------------------------------------------------------------
start(38)
unit('Antibacterial Classes and Core Properties','Antibacterials are organised by target: cell-wall synthesis, protein synthesis, folate, DNA gyrase or the membrane. Cell-wall drugs and gyrase inhibitors are bactericidal; most protein and folate inhibitors are bacteriostatic, with aminoglycosides and cotrimoxazole as bactericidal exceptions.')
facts(153,[
('Cell-wall synthesis inhibitors are most effective against:','Replicating bacteria',['Dormant spores only','Viruses','Human cells']),
('Cell-wall inhibitors kill bacteria because loss of the wall allows:','Water and solutes to enter, causing lysis',['DNA repair to stop','Ribosomes to dissociate','Folate to accumulate']),
('The least toxic cell-wall inhibitors are:','Beta-lactams',['Glycopeptides','Bacitracin','Cycloserine']),
('The beta-lactam nucleus is shown as a beta-lactam ring plus a:','Thiazoline ring',['Pyridine ring','Imidazole ring','Benzene ring']),
('Penicillins principally cover:','Gram-positive organisms',['Only Gram-negative organisms','Only anaerobes','Mycoplasma']),
('Cephalosporins principally extend coverage toward:','Gram-negative organisms',['Viruses','Fungi','Protozoa']),
('Carbapenems cover:','Both Gram-positive and Gram-negative organisms',['Only Gram-positive organisms','Only atypical bacteria','Only mycobacteria']),
('Monobactams principally cover:','Gram-negative organisms',['Gram-positive organisms','Anaerobes only','Mycoplasma']),
('The glycopeptide listed for resistant Gram-positive infection is:','Vancomycin',['Aztreonam','Fosfomycin','Bacitracin']),
('Other cell-wall inhibitors listed are:','Cycloserine, bacitracin and fosfomycin',['Tetracycline, macrolide and linezolid','Sulfonamide, trimethoprim and quinolone','Polymyxin, daptomycin and colistin']),
('Most protein-synthesis inhibitors are:','Bacteriostatic',['Bactericidal','Virucidal','Fungicidal']),
('The bactericidal exception among protein-synthesis inhibitors is:','Aminoglycosides',['Tetracyclines','Macrolides','Clindamycin']),
('Protein-synthesis inhibitors listed include tetracyclines, macrolides, clindamycin, linezolid, streptogramins and:','Aminoglycosides',['Penicillins','Sulfonamides','Polymyxins']),
('Most antifolate antibacterial action is:','Bacteriostatic',['Bactericidal','Sporicidal','Virucidal']),
('The bactericidal antifolate combination is:','Cotrimoxazole',['A sulfonamide alone','Folic acid','Methotrexate']),
('DNA-gyrase inhibitors are:','Bactericidal',['Bacteriostatic','Only fungistatic','Only virustatic']),
('The DNA-gyrase inhibitor class listed is:','Fluoroquinolones',['Macrolides','Glycopeptides','Polymyxins']),
('Drugs acting on the cell membrane include:','Polymyxins and daptomycin',['Penicillins and cephalosporins','Tetracyclines and macrolides','Sulfonamides and cotrimoxazole']),
('Daptomycin is classified as a:','Lipopeptide',['Glycopeptide','Beta-lactam','Aminoglycoside']),
('Cell-membrane-active antibacterial drugs are generally:','Bactericidal',['Bacteriostatic','Antifolate','DNA synthesis promoters']),
])
unit('Pharmacotherapy Decision Making','The hierarchy favours bactericidal and less toxic agents, but treatment always rests on benefit exceeding risk. A bacteriostatic drug may reduce a cell-wall inhibitor’s effect because the latter needs bacterial replication.')
facts(153,[
('When otherwise appropriate, pharmacotherapy favours:','Bactericidal over bacteriostatic drugs',['Bacteriostatic over bactericidal drugs','Most toxic over least toxic drugs','Combination therapy in every case']),
('The toxicity preference is:','Less toxic beta-lactams over more toxic agents',['Polymyxins over beta-lactams','Aminoglycosides over penicillins','The most toxic agent available']),
('The basic condition for using an antibacterial is:','Benefit must exceed risk',['Risk must exceed benefit','It must always be bacteriostatic','It must be orally absorbed']),
('Combining a bacteriostatic drug with a cell-wall inhibitor can:','Reduce the cell-wall inhibitor effect',['Always produce synergy','Prevent resistance completely','Increase bacterial replication']),
('Why may a bacteriostatic drug antagonise a beta-lactam?','Beta-lactams work best on actively replicating bacteria',['Beta-lactams need folate','Bacteriostatic drugs destroy beta-lactam rings','Both compete for renal excretion']),
])
unit('Therapy by Cell Wall, Site and Resistance','With a cell wall, beta-lactams are first line and aminoglycosides are added in severe disease. Without a wall, protein-synthesis inhibitors are required. Site matters: urinary and stool concentration guide UTI and GIT therapy; polymyxins and daptomycin are toxic last-line choices for resistant organisms.')
facts(154,[
('For a Gram-positive organism with a cell wall, first-line treatment is usually:','A penicillin',['A polymyxin','A tetracycline in every case','A fluoroquinolone only']),
('For a Gram-negative organism with a cell wall, first-line choices include:','Cephalosporin, penicillin or carbapenem',['Vancomycin only','Daptomycin only','Macrolide only']),
('A resistant Gram-positive cell-wall infection is treated with:','Vancomycin',['Aztreonam','Fosfomycin only','Cytisine']),
('In a severe cell-wall infection, an add-on drug is:','An aminoglycoside such as gentamicin',['A bacteriostatic tetracycline','Disulfiram','Acamprosate']),
('Gentamicin added to a beta-lactam broadens coverage to:','Gram-positive and Gram-negative bacteria',['Only anaerobes','Only atypical bacteria','Only fungi']),
('Organisms without a cell wall include:','Mycoplasma and Legionella',['Staphylococcus and Streptococcus','E. coli and Klebsiella','Enterococcus and Pneumococcus']),
('First-line choices for wall-less bacteria are:','Tetracyclines, macrolides or clindamycin',['Penicillin G only','Vancomycin only','Bacitracin only']),
('Linezolid and streptomycin in the wall-less algorithm are:','More toxic later-line options',['First-line least-toxic options','Antifolates','Cell-wall inhibitors']),
('For a UTI, a useful drug must achieve high concentration in:','Urine',['Stool','CSF only','Bile only']),
('First-line but toxic urinary antibacterial agents are:','Fluoroquinolones',['Macrolides','Glycopeptides','Lipopeptides']),
('Sulfonamides are particularly useful against:','Protozoa',['Viruses','Fungi only','Helminths']),
('Cotrimoxazole is reserved in the UTI box for:','Rare bacteria',['All uncomplicated UTIs','Fungal UTI','Viral cystitis']),
('Aminoglycosides require caution in urinary infection because they are:','Nephrotoxic',['Hepatotoxic','Myelotoxic','Only ototoxic without renal toxicity']),
('For gastrointestinal infection, a first-line drug with high stool concentration is:','A fluoroquinolone',['Vancomycin IV only','Penicillin V','Gentamicin IV']),
('Polymyxins are last-line drugs for resistant:','Gram-negative bacteria',['Gram-positive bacteria','Mycoplasma','Fungi']),
('Daptomycin is a last-line drug for resistant:','Gram-positive bacteria',['Gram-negative bacteria','Protozoa','Viruses']),
])
unit('Peptides and Aminoglycoside Synergy','Glycopeptides and lipopeptides are large proteins, explaining poor oral absorption and failure to traverse Gram-negative porins; their spectrum is Gram positive. Aminoglycosides also absorb poorly and need an oxygen-dependent membrane potential to enter; beta-lactam wall disruption permits synergistic entry.')
facts(154,[
('Glycopeptides and lipopeptides are:','Large protein molecules',['Small lipid-soluble bases','Beta-lactam sugars','Folate analogues']),
('Their large molecular size causes:','Poor oral absorption',['Complete oral absorption','Rapid BBB entry','Exclusive hepatic excretion']),
('Peptide antibiotics cannot enter Gram-negative bacteria through:','Porins',['Ribosomes','DNA gyrase','Folate pumps']),
('The spectrum of glycopeptides/lipopeptides is mainly:','Gram-positive Staphylococcus and Enterococcus',['Gram-negative aerobes','Atypical organisms only','Protozoa']),
('Aminoglycosides have:','Poor oral absorption',['Complete oral bioavailability','No renal toxicity','No need for bacterial uptake']),
('Aminoglycoside entry depends on bacterial generation of a:','Transmembrane potential',['Folate gradient','Chloride gradient only','Nuclear potential']),
('The bacterial transmembrane potential for aminoglycoside entry requires:','ATP and oxygen',['Folate and CO2','Only glucose','Only sodium']),
('Aminoglycoside monotherapy primarily covers:','Gram-negative aerobes',['Gram-positive anaerobes','Mycoplasma only','Viruses']),
('In polytherapy, aminoglycoside coverage can extend to:','Gram-positive and Gram-negative bacteria',['Only protozoa','Only fungi','Only wall-less bacteria']),
('Beta-lactam plus aminoglycoside synergy occurs because the beta-lactam:','Inhibits the wall and facilitates aminoglycoside entry',['Blocks aminoglycoside excretion','Activates bacterial folate','Prevents oxygen use']),
('The resulting beta-lactam–aminoglycoside combination effect is:','Bactericidal',['Bacteriostatic','Antiviral','Fungistatic']),
])
finish()

# CHAPTER 39 -----------------------------------------------------------------
start(39)
unit('Four Steps of Cell-wall Synthesis','Peptidoglycan assembly begins in cytoplasm with NAG, NAM and a D-Ala-containing pentapeptide, crosses the membrane on bactoprenol, polymerises by transglycosylation, and finally cross-links through PBP/transpeptidase. Each stage has a characteristic inhibitor.')
facts(155,[
('The first step of peptidoglycan synthesis occurs in the:','Cytoplasm',['Cell membrane exterior','Nucleus','Periplasm only']),
('NAG stands for:','N-acetylglucosamine',['N-acetylgalactosamine','N-amino glucose','N-acetylglycine']),
('NAM stands for:','N-acetylmuramic acid',['N-acetylmalonic acid','N-amino muramic acid','N-acetylmethionine']),
('PEP stands for:','Phosphoenolpyruvate',['Phosphoenolpyruvate transferase','Peptidoglycan endopeptidase','Penicillin efflux protein']),
('EPT is:','Enolpyruvate transferase',['Endopeptide transferase','Efflux pump transporter','Extracellular peptidase']),
('A PEP analogue inhibits EPT by:','Competitive inhibition',['Irreversible receptor activation','Allosteric induction','Increasing transcription']),
('L-alanine is converted to D-alanine by:','Alanine racemase',['Alanine ligase','Transpeptidase','Transglycosylase']),
('The terminal amino acids in the cell-wall pentapeptide are:','D-Ala-D-Ala',['L-Ala-L-Ala','D-Lys-D-Lys','Gly-Gly']),
('The enzyme attaching alanine into the peptide is:','Alanine ligase',['Alanine racemase','Bactoprenol phosphatase','PBP']),
('The glycine chain and other peptides are part of the:','Pentapeptide side chain',['NAG sugar alone','Bactoprenol carrier','Cell membrane lipid']),
('NAG is joined to NAM to form:','One unit of cell wall',['A ribosome','A porin','A DNA gyrase complex']),
('During membrane transport, the carrier is:','Bactoprenol phosphate',['P-glycoprotein','VMAT-2','Transferrin']),
('While transferring its cargo, bactoprenol phosphate becomes:','Bactoprenol diphosphate',['NAG','NAM','D-Ala']),
('Bacitracin blocks:','Bactoprenol-mediated transport',['Alanine racemase','Transglycosylation','PBP directly']),
('Step 3 of wall synthesis is:','Transglycosylation or polymerisation',['Cross-linking','D-alanine formation','Drug efflux']),
('The enzyme catalysing polymerisation is:','Peptidoglycan glycosyl transferase',['Alanine racemase','Dihydropeptidase','Beta-lactamase']),
('Vancomycin inhibits:','Transglycosylation/polymerisation',['Bactoprenol transport','Folate synthesis','DNA gyrase']),
])
facts(156,[
('Step 4 of cell-wall synthesis is:','Cross-linking',['Transportation','PEP formation','Folate reduction']),
('Cross-linking occurs between the fourth-position D-Ala and a:','Neighbouring peptide chain',['NAG molecule only','Bactoprenol carrier','Porin']),
('The cross-linking enzyme is:','Transpeptidase, also called PBP',['Alanine racemase','EPT','COMT']),
('PBP stands for:','Penicillin-binding protein',['Peptide-binding porin','Phosphate-binding protein','Penicillin-breaking protease']),
('Beta-lactams inhibit:','PBP/transpeptidase',['Alanine racemase','Bactoprenol','Transglycosylase only']),
('PEP-analogue drugs are:','Fosfomycin and fosmidomycin',['Cycloserine and bacitracin','Vancomycin and teicoplanin','Penicillin and aztreonam']),
('The D-Ala analogue is:','Cycloserine',['Fosfomycin','Bacitracin','Vancomycin']),
('Cycloserine inhibits:','Alanine racemase and alanine ligase',['PBP and beta-lactamase','Porins and efflux pumps','Transglycosylase only']),
('The transport inhibitor is:','Bacitracin',['Cycloserine','Fosfomycin','Penicillin V']),
('Beta-lactam subclasses are:','Penicillins, cephalosporins, carbapenems and monobactams',['Glycopeptides, macrolides, tetracyclines and quinolones','Sulfonamides, aminoglycosides, polymyxins and lipopeptides','Rifamycins, oxazolidinones, streptogramins and ketolides']),
])
unit('Moderate-spectrum and Long-acting Penicillins','Moderate-spectrum penicillins mainly cover Gram positive organisms. Penicillin G is aqueous IV and treats neurosyphilis; penicillin V is oral. Probenecid, procaine and benzathine prolong penicillin action, with benzathine lasting 28 days and supporting monthly rheumatic-fever prophylaxis.')
facts(156,[
('Moderate-spectrum penicillins act mainly against:','Gram-positive organisms',['Gram-negative organisms only','Atypical bacteria','Fungi']),
('Their Gram-negative action is limited because of:','Lower water solubility',['Excess porin production','High protein synthesis','Lack of a beta-lactam ring']),
('Aqueous penicillin G is given by the:','Intravenous route',['Oral route','Transdermal route','Inhalational route']),
('Penicillin G is the drug of choice for:','Neurosyphilis',['MRSA','VRE','Pseudomonas']),
('Penicillin V is administered:','Orally',['Only intravenously','Only intrathecally','Only topically']),
('The clinical uses of penicillin V are:','Similar to penicillin G',['Restricted to MRSA','Restricted to Pseudomonas','Only UTI']),
('Long-acting penicillins are administered by the:','Intramuscular route',['Intravenous route','Oral route','Intranasal route']),
])
facts(157,[
('The three long-acting penicillin approaches listed are:','Probenecid-PG, procaine-PG and benzathine-PG',['Clavulanate-PG, sulbactam-PG and tazobactam-PG','Cefazolin, cefuroxime and ceftriaxone','Oxacillin, nafcillin and methicillin']),
('The longest-acting penicillin preparation is:','Benzathine penicillin G',['Procaine penicillin G','Aqueous penicillin G','Penicillin V']),
('Benzathine penicillin G acts for approximately:','28 days',['28 hours','7 days','6 months']),
('Monthly rheumatic-fever prophylaxis uses:','Benzathine penicillin G',['Aqueous penicillin G daily','Penicillin V once yearly','Vancomycin monthly']),
('The S in SLYGRAM includes Streptococcus and:','Syphilis',['Staphylococcus only','Serratia','Shigella']),
('Resistance to penicillin in syphilis is described as:','Zero',['Universal','Rapidly increasing','Due to mecA']),
('The L in SLYGRAM is:','Leptospirosis',['Listeriosis','Legionellosis','Leprosy']),
('The Y in SLYGRAM is:','Yaws',['Yellow fever','Yersiniosis','Yeast infection']),
('The G in SLYGRAM is:','Gas gangrene',['Gonorrhoea','Giardiasis','Gastritis']),
('The R in SLYGRAM is:','Rat-bite fever',['Rheumatic fever only','Rocky Mountain fever','Relapsing fever']),
('The A in SLYGRAM is:','Actinomycosis',['Anthrax','Amoebiasis','Aspergillosis']),
('The M in SLYGRAM is:','Sensitive meningococcal infection',['MRSA','Mycoplasma','Malaria']),
])
unit('Penicillinase-resistant and Antipseudomonal Penicillins','Anti-staphylococcal penicillins resist penicillinase and cover Gram-positive Staphylococcus. Oral agents serve mild disease, IV agents severe disease. Wider penicillins add charge and water solubility: carboxypenicillins and ureidopenicillins cover Pseudomonas; aminopenicillins include amoxicillin and ampicillin.')
facts(157,[
('Narrow anti-staphylococcal penicillins are designed to resist:','Penicillinase',['Altered folate','DNA gyrase','Aminoglycoside-modifying enzymes']),
('Their principal activity is against Gram-positive:','Staphylococcus',['Pseudomonas','E. coli','Bacteroides']),
('Oral anti-staphylococcal penicillins include:','Oxacillin, cloxacillin and dicloxacillin',['Nafcillin, methicillin and vancomycin','Ampicillin, amoxicillin and piperacillin','Penicillin G, aztreonam and imipenem']),
('Oral anti-staphylococcal penicillins are used for:','Mild to moderate cellulitis and mastitis',['Meningitis','Pseudomonal sepsis','VRE']),
('IV anti-staphylococcal drugs include:','Oxacillin, nafcillin and methicillin',['Cloxacillin only','Penicillin V and amoxicillin','Aztreonam and cefixime']),
('Methicillin is limited by:','Nephrotoxicity',['Hepatotoxicity','Ototoxicity','Retinopathy']),
('IV anti-staphylococcal penicillins are used in:','Severe infection and endocarditis',['Only mild acne','Only viral infection','Only uncomplicated cystitis']),
('Staphylococci resist penicillin by synthesising:','Beta-lactamase (penicillinase)',['Aminoglycoside','Folate','D-Ala-D-Lac']),
('Penicillinase resistance arises when the drug has:','A modified beta-lactam region that penicillinase cannot attack',['No beta-lactam ring','No PBP affinity','A folate group']),
('MRSA resistance is mediated by:','Altered PBP encoded by mecA',['Only drug efflux','Loss of folate synthesis','D-Ala to D-Lac conversion']),
('The drug of choice for MRSA on this page is:','Vancomycin',['Methicillin','Penicillin V','Ampicillin']),
('Vancomycin resistance develops through conversion of:','D-Ala to D-lactate',['L-Ala to D-Ala','NAG to NAM','PEP to pyruvate']),
('The drug of choice for VRSA is:','Daptomycin',['Vancomycin','Methicillin','Penicillin G']),
('Alternatives for resistant staphylococcal infection include:','Linezolid, streptogramins and tigecycline',['Disulfiram, naltrexone and topiramate','Cefazolin only','Fosfomycin only']),
])
facts(158,[
('Carboxypenicillins carry a carboxyl group that adds:','Positive charge and water solubility',['Negative charge only','Lipid solubility','Protein binding']),
('The carboxypenicillins listed are:','Carbenicillin and ticarcillin',['Piperacillin and mezlocillin','Amoxicillin and ampicillin','Oxacillin and cloxacillin']),
('Ureidopenicillins carry both positive and negative charge, giving:','Maximum water solubility',['Minimum water solubility','No Gram-negative activity','Only oral absorption']),
('The penicillins described as most effective against Gram-negative organisms are:','Ureidopenicillins',['Penicillin V','Benzathine penicillin','Anti-staphylococcal penicillins']),
('Ureidopenicillins listed are:','Azlocillin, mezlocillin and piperacillin',['Carbenicillin, ticarcillin and ampicillin','Oxacillin, nafcillin and methicillin','Penicillin G, V and benzathine']),
('Aminopenicillins are:','Negatively charged',['Positively charged only','Uncharged','Lipid soluble steroids']),
('The aminopenicillins compared are:','Amoxicillin and ampicillin',['Oxacillin and cloxacillin','Piperacillin and ticarcillin','Penicillin G and V']),
])
unit('Amoxicillin versus Ampicillin and Resistance','Amoxicillin absorbs better, needs TDS dosing and causes less diarrhoea; ampicillin is less absorbed, needs QID dosing and is used IV for severe infection. IV ampicillin plus gentamicin is preferred for Listeria meningitis and E. faecalis endocarditis.')
facts(158,[
('Compared with ampicillin, oral absorption of amoxicillin is:','Greater',['Lower','Equal to zero','Only possible IV']),
('Amoxicillin is dosed:','Three times daily (TDS)',['Four times daily','Once monthly','Only once']),
('Ampicillin is dosed:','Four times daily (QID)',['Three times daily','Once daily','Once monthly']),
('Diarrhoea is more frequent with:','Ampicillin',['Amoxicillin','Penicillin G','Benzathine penicillin']),
('Amoxicillin may be given by:','Oral or IV route',['IV route only','IM route only','Intrathecal route only']),
('Ampicillin in the comparison table is given by:','IV route',['Oral route only','Transdermal route','Intranasal route']),
('Amoxicillin covers infection of:','Mild, moderate or severe intensity',['Severe intensity only','Mild intensity only','No respiratory infection']),
('Ampicillin is chiefly assigned to:','Severe infection',['Only mild infection','Dry-eye disease','Smoking dependence']),
('Amoxicillin uses include respiratory infection such as:','Otitis and pneumonia',['Only meningitis','Only endocarditis','Only skin infection']),
('Amoxicillin is used for UTI and is:','Safe in pregnancy',['Absolutely contraindicated in pregnancy','Nephrotoxic in every dose','Used only in men']),
('The preferred regimen for Listeria meningitis is:','IV ampicillin plus gentamicin',['Oral amoxicillin alone','Vancomycin alone','Piperacillin alone']),
('The preferred regimen for E. faecalis endocarditis is:','IV ampicillin plus gentamicin',['Cefixime alone','Penicillin V alone','Bacitracin']),
('If E. faecalis endocarditis fails ampicillin, the page recommends:','Vancomycin plus gentamicin',['Amoxicillin alone','Cloxacillin alone','Aztreonam']),
('Penicillinase causes resistance by:','Cutting the beta-lactam ring at its base',['Changing D-Ala to D-Lac','Blocking folate','Increasing PBP affinity']),
('PBP alteration through mecA produces:','MRSA',['VRSA','VRE','ESBL E. coli only']),
('Change of D-Ala to D-lactate produces:','Vancomycin-resistant S. aureus',['MRSA','Penicillin-sensitive Streptococcus','Meningococcus']),
])
finish()

# CHAPTER 40 -----------------------------------------------------------------
start(40)
unit('Cephalosporin Generations and Spectrum','Across older generations, Gram-positive activity generally falls while Gram-negative activity rises. Fourth generation extends third-generation Gram-negative coverage; fifth generation restores strong Gram-positive activity including MRSA; cefiderocol is a sixth-generation siderophore cephalosporin.')
facts(159,[
('The example given for a third-generation cephalosporin is:','Ceftriaxone',['Cefazolin','Cefuroxime','Cefiderocol']),
('From first to third generation, Gram-positive activity generally:','Decreases',['Increases','Remains absent','Becomes antifungal']),
('From first to third generation, Gram-negative activity generally:','Increases',['Decreases','Remains absent','Becomes antiviral']),
('First-generation cephalosporins mainly cover Gram-positive:','Aerobes',['Anaerobes only','Atypical organisms','Protozoa']),
('Second-generation activity includes:','Aerobes and anaerobes',['Only viruses','Only fungi','Only mycobacteria']),
('Third-generation Gram-positive emphasis includes:','Pneumococcus',['MRSA only','Enterococcus only','Mycoplasma']),
('Fourth-generation Gram-positive spectrum is:','Similar to third generation',['Absent','Only MRSA','Only enterococci']),
('Fourth-generation Gram-negative spectrum is:','Greater than third generation',['Less than first generation','Absent','Only anaerobes']),
('Fourth-generation added Gram-negative targets include:','Pseudomonas, Enterobacter, ESBL, Serratia and Proteus',['MRSA, VRE and pneumococcus only','Mycoplasma and Legionella','Protozoa and fungi']),
('Fifth-generation Gram-positive activity is:','Greater than third generation',['Absent','Less than first generation','Restricted to anaerobes']),
('Fifth-generation coverage includes:','Staphylococcus, Streptococcus and MRSA',['Only Pseudomonas','Only atypical bacteria','Only fungi']),
('Fifth-generation Gram-negative activity is:','Similar to third generation',['Absent','Greater than sixth in every case','Only anaerobic']),
('The sixth-generation example is:','Cefiderocol',['Ceftriaxone','Ceftaroline','Cefepime']),
('Cefiderocol is a:','Siderophore cephalosporin carrying an iron molecule',['Glycopeptide','Monobactam','Carbapenem']),
('Reduced porin production causes cephalosporin:','Resistance',['Synergy','Hypersensitivity','Oral absorption']),
('Cefiderocol bypasses porin-related resistance by entering via:','An iron pump',['A folate transporter','VMAT-2','The sodium channel']),
('Cefiderocol acts mainly against:','Gram-negative organisms',['Gram-positive organisms only','Protozoa','Fungi']),
('Cefiderocol is used for resistant:','UTI and ventilator-associated pneumonia',['Otitis and mastitis','Syphilis and yaws','Alcohol withdrawal']),
])
unit('Individual Cephalosporins','Cefazolin is the surgical-prophylaxis standard; cefuroxime treats respiratory disease; cefotetan and cefoxitin are anaerobe-active cephamycins. Ceftriaxone has broad third-generation indications, while ceftazidime is the best antipseudomonal cephalosporin and later generations cover resistant pathogens.')
facts(160,[
('Cefazolin belongs to the:','First generation',['Second generation','Third generation','Fifth generation']),
('The route of cefazolin is:','Intravenous',['Oral','Intranasal','Transdermal']),
('Cefazolin is the drug of choice for:','Surgical prophylaxis',['MRSA bacteraemia','VRE','Pseudomonal meningitis']),
('For surgical prophylaxis cefazolin is given:','60 minutes before surgery',['After wound closure','24 hours after surgery','One month before surgery']),
('Cefazolin has maximal effect against:','Staphylococci and streptococci',['Pseudomonas and Acinetobacter','Mycoplasma and Legionella','Bacteroides only']),
('Cefuroxime belongs to the:','Second generation',['First generation','Fourth generation','Sixth generation']),
('Cefuroxime covers Gram-positive and Gram-negative:','Aerobes',['Only anaerobes','Only atypical organisms','Only fungi']),
('Cefuroxime is used for:','Respiratory infection such as pneumonia or otitis',['MRSA endocarditis','VRE','Neurosyphilis']),
('Cefuroxime is commonly used in children because it is:','Cheaper',['The only oral cephalosporin','Free of allergy','Active against all bacteria']),
('The cephamycins are:','Cefotetan and cefoxitin',['Cefazolin and cefuroxime','Ceftriaxone and cefixime','Cefepime and cefpirome']),
('Cephamycins cover:','Gram-positive, Gram-negative and anaerobic organisms',['Only Gram-positive aerobes','Only Gram-negative aerobes','Only atypical bacteria']),
('Cephamycins are used for:','Abdominal and pelvic infections',['Smoking cessation','Neurosyphilis','Dry eye']),
('Ceftriaxone is given by:','IV or IM route',['Oral route only','Transdermal route','Intranasal route']),
('Ceftriaxone is a drug of choice for infections due to:','E. coli, Klebsiella and Providencia',['MRSA and VRE','Mycoplasma and Legionella','Fungi']),
('Ceftriaxone is also a drug of choice for:','Typhoid and gonorrhoea',['Tuberculosis and leprosy','Malaria and amoebiasis','Influenza and COVID-19']),
('Gonorrhoea can be treated with ceftriaxone as:','Monotherapy',['Mandatory triple therapy','Topical therapy','Prophylaxis only']),
('The empirical drug of choice for meningitis listed is:','Ceftriaxone',['Cefazolin','Cefiderocol','Cefoxitin']),
('A shorter-acting alternative to ceftriaxone in meningitis is:','Cefotaxime',['Cefixime','Cefoperazone','Ceftaroline']),
('The oral drug of choice for typhoid is:','Cefixime',['Ceftriaxone','Cefepime','Cefazolin']),
('The antipseudomonal third-generation drugs listed are:','Ceftolozane, cefoperazone and ceftazidime',['Cefazolin, cefuroxime and cefotetan','Ceftaroline, ceftobiprole and cefiderocol','Cefixime, cefotaxime and ceftriaxone']),
('The best antipseudomonal cephalosporin on the page is:','Ceftazidime',['Cefazolin','Cefuroxime','Ceftaroline']),
('Fourth-generation cephalosporins are given by the:','IV route',['Oral route','Intranasal route','Topical route']),
('Fourth-generation examples are:','Cefepime and cefpirome',['Ceftriaxone and cefixime','Ceftaroline and ceftobiprole','Cefotetan and cefoxitin']),
('Fourth-generation drugs add coverage of Pseudomonas, Proteus, Enterobacter, Acinetobacter, Serratia and:','ESBL organisms',['MRSA only','VRE only','Mycoplasma']),
('Fifth-generation examples are:','Ceftobiprole and ceftaroline',['Cefepime and cefpirome','Cefotetan and cefoxitin','Ceftriaxone and cefixime']),
('Fifth-generation cephalosporins are useful against:','MRSA and streptococci/staphylococci',['Only Pseudomonas','Only anaerobes','Only atypicals']),
('Cefiderocol is administered:','Intravenously',['Orally','Intranasally','Topically']),
])
unit('Carbapenems and Monobactams','Carbapenems are wide-spectrum drugs for serious resistant infections. Imipenem needs cilastatin; doripenem/meropenem favour Gram negative disease and meningitis; ertapenem is longest acting but lacks strong Gram-negative and antipseudomonal reach. Aztreonam provides Gram-negative coverage when penicillin allergy prevents other beta-lactams.')
facts(161,[
('Carbapenems cover:','Gram-positive and Gram-negative aerobes and anaerobes',['Only Gram-positive aerobes','Only Gram-negative anaerobes','Only atypical organisms']),
('Carbapenems are drugs of choice for:','ESBL, Serratia, Enterobacter and Acinetobacter',['MRSA only','VRE only','Mycoplasma']),
('Most carbapenems have:','Antipseudomonal activity',['No Gram-negative action','Only oral action','Only antifolate action']),
('Imipenem is very short acting because it is metabolised by:','Renal dihydropeptidase',['Hepatic CYP3A4','Plasma cholinesterase','MAO-B']),
('Imipenem is combined with:','Cilastatin',['Clavulanate','Tazobactam','Avibactam']),
('Cilastatin acts by inhibiting:','Renal dihydropeptidase',['Beta-lactamase','PBP','DNA gyrase']),
('Imipenem activity favours:','Gram-positive over Gram-negative organisms',['Gram-negative over Gram-positive organisms','Only anaerobes','Only atypicals']),
('Doripenem and meropenem activity favours:','Gram-negative over Gram-positive organisms',['Gram-positive over Gram-negative organisms','Only enterococci','Only fungi']),
('The carbapenem of choice for meningitis is:','Meropenem',['Imipenem','Ertapenem','Aztreonam']),
('The longest-acting carbapenem with once-daily dosing is:','Ertapenem',['Imipenem','Meropenem','Doripenem']),
('Ertapenem spectrum is chiefly:','Anaerobes with low Gram-negative activity',['Only MRSA','Only Pseudomonas','Only atypical bacteria']),
('Ertapenem is useful in:','Pelvic and abdominal infections',['Neurosyphilis','Alcohol withdrawal','Dry eye']),
('The monobactam discussed is:','Aztreonam',['Imipenem','Cefiderocol','Vancomycin']),
('Aztreonam covers:','Only Gram-negative organisms',['Only Gram-positive organisms','Only anaerobes','Only fungi']),
('Aztreonam has no cross-sensitivity with other beta-lactams except:','Ceftazidime',['Cefazolin','Cefuroxime','Ceftriaxone']),
('Aztreonam is used for Gram-negative infection in a patient with:','Penicillin allergy',['Vancomycin allergy only','Renal stones','Glaucoma']),
])
unit('Beta-lactam Adverse Effects and Dosing','Shared harms are hypersensitivity and pseudomembranous enterocolitis; individual drugs cause MTT-related bleeding, ceftriaxone biliary effects, seizures, hepatitis or neutropenia. Most doses require renal adjustment, except liver-excreted cefpiramide and cefoperazone.')
facts(161,[
('Type I beta-lactam hypersensitivity presents with:','Rash and anaphylaxis',['Hemolytic anaemia','Neutropenia','Pseudolithiasis']),
('Type II beta-lactam hypersensitivity presents with:','Hemolytic anaemia',['Anaphylaxis','Red-man syndrome','Kernicterus']),
('Pseudomembranous enterocolitis follows beta-lactam suppression of:','Normal gut flora',['Renal flora','Skin keratin','Hepatic enzymes']),
('Loss of normal flora promotes infection with:','Clostridium difficile',['Mycoplasma','Treponema','Legionella']),
('The greatest beta-lactam risk of pseudomembranous enterocolitis is with:','Third-generation cephalosporins',['Penicillin V','Aztreonam','Benzathine penicillin']),
('The risk order shown after third-generation cephalosporins is:','Aminopenicillins, fluoroquinolones, then clindamycin',['Clindamycin, penicillin V, then vancomycin','Carbapenems, polymyxins, then macrolides','Sulfonamides, tetracyclines, then bacitracin']),
])
facts(162,[
('MTT-containing cephalosporins can cause a:','Disulfiram-like reaction with alcohol',['Serotonin syndrome','Red-man syndrome','Cheese reaction']),
('MTT cephalosporins can produce bleeding through:','Hypoprothrombinaemia',['Thrombocytosis','Polycythaemia','Factor VIII excess']),
('Drugs associated with MTT-related hypoprothrombinaemia include:','Moxalactam, cefoperazone, cefamandole and cefotetan',['Cefazolin, cefuroxime, cefixime and cefiderocol','Imipenem, meropenem, aztreonam and vancomycin','Penicillin G, V, amoxicillin and ampicillin']),
('Ceftriaxone specifically causes:','Pseudolithiasis and kernicterus',['Red-man syndrome and deafness','Neutropenia only','Psychosis and seizures']),
('Beta-lactams avoided in meningitis because of seizure risk include:','Imipenem and rapidly pushed IV ampicillin',['Meropenem and ceftriaxone','Aztreonam and cefixime','Penicillin V and cefuroxime']),
('The anti-staphylococcal penicillin associated with hepatotoxicity is:','Oxacillin',['Nafcillin','Methicillin','Cloxacillin']),
('The anti-staphylococcal penicillin associated with neutropenia is:','Nafcillin',['Oxacillin','Methicillin','Dicloxacillin']),
('In renal failure, beta-lactam doses generally should be:','Adjusted',['Doubled routinely','Left unchanged in all cases','Stopped permanently']),
('Renal-dose-adjustment exceptions are:','Cefpiramide and cefoperazone',['Cefazolin and cefuroxime','Ceftriaxone and cefixime','Cefepime and cefpirome']),
('Cefpiramide and cefoperazone are excreted:','Completely by the liver',['Completely by the kidney','Through the lungs','In sweat']),
('Liver-excreted cefpiramide and cefoperazone should not be used for:','UTI',['Pneumonia','Pelvic infection','Endocarditis']),
('Another antibacterial noted as unsuitable for UTI is:','Moxifloxacin',['Ciprofloxacin','Cotrimoxazole','Fosfomycin']),
])
unit('Mechanisms of Beta-lactam Resistance','Gram-negative organisms resist by active MDR-1 efflux and reduced porins. Both Gram-positive and Gram-negative bacteria can alter PBP or produce beta-lactamases. Ambler classes A-D and old versus new inhibitors determine which combination can restore beta-lactam activity.')
facts(162,[
('The Gram-negative active drug-efflux pump shown is:','MDR-1',['P-glycoprotein in human gut only','VMAT-2','Bactoprenol']),
('An efflux pump moves drug:','Against its concentration gradient',['Only down its gradient','Into the bacterium','Into the nucleus']),
('Examples using active efflux include:','Pseudomonas, E. coli and gonococci',['Only streptococci','Only enterococci','Only clostridia']),
('Reduced porin production causes resistance by:','Preventing penicillin from crossing the outer wall',['Increasing drug entry','Increasing PBP affinity','Blocking renal excretion']),
('An organism exemplifying reduced porins is:','Pseudomonas',['Streptococcus','Enterococcus','Treponema']),
])
facts(163,[
('A resistance mechanism shared by Gram-positive and Gram-negative organisms is:','Alteration of penicillin-binding protein',['Only MDR-1 efflux','Only reduced porins','Only loss of a cell wall']),
('MRSA has altered PBP through the:','mecA gene',['vanA gene','SOD1 gene','rpoB gene']),
('Ampicillin resistance in H. influenzae may result from:','Altered PBP',['D-Ala to D-Lac only','No cell wall','Loss of ADH']),
('Ambler type A beta-lactamases are:','ESBLs including penicillinase, cephalosporinase and monobactamase',['Metalloenzymes except monobactamase','Only cephalosporinase','Only cloxacillinase']),
('Ambler type B includes:','All major beta-lactamase activity except monobactamase',['Only ESBL penicillinase','Only cephalosporinase','Only cloxacillinase']),
('Ambler type C is:','Cephalosporinase',['Cloxacillinase','Penicillinase only','Monobactamase only']),
('Ambler type D is:','Cloxacillinase',['Cephalosporinase','Metallo-beta-lactamase','Penicillinase only']),
('NDM-1 beta-lactamase:','Breaks most beta-lactam drugs',['Only breaks monobactams','Increases porins','Blocks efflux']),
('Treatment options listed for NDM-1 producers are:','Tigecycline and colistin',['Penicillin G and V','Cefazolin and cefuroxime','Amoxicillin and ampicillin']),
('Old beta-lactamase inhibitors are described as:','Suicidal inhibitors',['Reversible agonists','Non-suicidal inhibitors','PBP activators']),
('Clavulanic acid is paired with:','Amoxicillin',['Ampicillin','Piperacillin','Ceftazidime']),
('Sulbactam is paired with:','Ampicillin',['Amoxicillin','Meropenem','Imipenem']),
('Sulbactam alone has activity against:','Acinetobacter',['MRSA','VRE','Treponema']),
('Tazobactam is paired with:','Piperacillin',['Penicillin V','Cefazolin','Aztreonam']),
('Avibactam is paired with:','Ceftazidime',['Amoxicillin','Ampicillin','Meropenem']),
('Vaborbactam is paired with:','Meropenem',['Piperacillin','Imipenem','Cefazolin']),
('Relebactam is paired with:','Imipenem plus cilastatin',['Amoxicillin alone','Ceftazidime alone','Piperacillin alone']),
('Most Gram-negative beta-lactamases are coded by:','Plasmids',['Mitochondria','Ribosomes','Human chromosomes']),
('Chromosomal beta-lactamases are:','Inducible by beta-lactams',['Never inducible','Found only in Gram-positive bacteria','Always inhibited by clavulanate']),
('Chromosomal inducible beta-lactamases occur in:','Pseudomonas, Enterobacter and Acinetobacter',['Streptococcus, Treponema and Mycoplasma','Only Staphylococcus','Only Enterococcus']),
('Against chromosomal inducible beta-lactamases, effective inhibitors are:','New non-suicidal inhibitors',['Only clavulanate','Only sulbactam','No inhibitors']),
])
finish()

# CHAPTER 41 -----------------------------------------------------------------
start(41)
unit('Fosfomycin, Cycloserine and Bacitracin','Fosfomycin/fosmidomycin mimic PEP and block EPT; fosfomycin concentrates in urine for single-dose pregnancy-safe UTI therapy. Cycloserine blocks alanine enzymes but causes neuropsychiatric toxicity. Bacitracin blocks bactoprenol and is restricted to topical skin use.')
facts(164,[
('Fosfomycin and fosmidomycin are analogues of:','PEP (phosphoenolpyruvate)',['D-Ala','Bactoprenol','PBP']),
('They inhibit:','EPT (enolpyruvate transferase)',['Transpeptidase','Alanine racemase','DNA gyrase']),
('The antibacterial spectrum listed for fosfomycin is:','Gram-negative',['Only Gram-positive','Only atypical','Only anaerobic']),
('Fosfomycin is useful in UTI because it:','Concentrates in urine',['Is excreted entirely in bile','Blocks renal filtration','Concentrates in CSF']),
('The UTI regimen of fosfomycin is:','A single 3-g dose',['3 mg hourly','30 g daily','A monthly implant']),
('Fosfomycin is described as:','Safe in pregnancy',['Teratogenic','Contraindicated in all women','Nephrotoxic at any dose']),
('Cycloserine is an analogue of:','D-alanine',['PEP','NAG','NAM']),
('Cycloserine inhibits:','Alanine racemase and alanine ligase',['EPT and PBP','Porins and MDR-1','Transglycosylase and beta-lactamase']),
('Cycloserine is a:','Second-line tuberculosis drug',['First-line UTI drug','Drug of choice for MRSA','Cephalosporin']),
('Cycloserine neuropsychiatric effects include:','Psychosis, neuropathy and seizures',['Red-man syndrome and deafness','Pseudolithiasis and kernicterus','Bleeding and neutropenia']),
('Bacitracin inhibits:','Bactoprenol-mediated wall-unit transport',['PBP cross-linking','Alanine racemase','DNA gyrase']),
('Bacitracin is used topically for:','Bacterial skin infection',['Systemic MRSA sepsis','Meningitis','Endocarditis']),
('Systemic bacitracin is avoided because of:','Very high toxicity',['Poor taste only','Hepatic metabolism','No antibacterial action']),
('For an MRSA nasal carrier, the drug of choice is:','Mupirocin',['Bacitracin','Vancomycin IV','Fosfomycin']),
])
unit('Glycopeptide Action and Resistance','Vancomycin binds the D-Ala terminus and prevents transglycosylation. VRSA changes D-Ala to D-lactate and has MIC at least 16 µg/mL; VISA thickens its wall by raising D-Ala density, with MIC 4-8 µg/mL. Susceptible S. aureus has MIC below 2 µg/mL.')
facts(164,[
('Glycopeptides inhibit cell-wall synthesis by binding:','D-Ala termini',['PBP directly','Porins','DNA gyrase']),
('The blocked stage is:','Transglycosylation/polymerisation',['Folate synthesis','DNA replication','Protein translation']),
('VRSA resists vancomycin by converting:','D-Ala to D-lactate',['D-Ala to L-Ala','NAG to NAM','PEP to pyruvate']),
('The vancomycin MIC defining VRSA on the page is:','At least 16 µg/mL',['Below 2 µg/mL','4-8 µg/mL','Exactly 1 µg/mL']),
('VISA resistance results from:','Increased D-Ala density and a thicker cell wall',['Complete loss of the wall','Reduced folate','Altered DNA gyrase']),
('The VISA MIC range is:','4-8 µg/mL',['Below 2 µg/mL','At least 16 µg/mL','0.1-0.5 µg/mL']),
('VISA expands to:','Vancomycin-intermediate Staphylococcus aureus',['Vancomycin-insensitive Streptococcus aeruginosa','Variable-inhibition Staphylococcus aureus','Vancomycin-induced Staphylococcus antigen']),
('VRSA expands to:','Vancomycin-resistant Staphylococcus aureus',['Vancomycin-resistant Streptococcus aeruginosa','Variable-resistant Staphylococcus antigen','Vancomycin-reactive Staphylococcus aureus']),
('MIC means:','Minimum inhibitory concentration',['Maximum inhibitory concentration','Minimum infused concentration','Mean intracellular concentration']),
('Vancomycin-susceptible S. aureus has MIC:','Below 2 µg/mL',['4-8 µg/mL','At least 16 µg/mL','Above 32 µg/mL']),
])
unit('Vancomycin Uses and Enterococcal/C. difficile Algorithms','Vancomycin is poorly absorbed and is given IV for systemic Gram-positive disease such as MRSA and enterococcal endocarditis. Its poor absorption is useful orally in C. difficile enterocolitis, though fidaxomicin is preferred for non-fulminant disease and recurrence is age-stratified.')
facts(165,[
('Vancomycin spectrum is:','Gram-positive Staphylococcus and Enterococcus',['Gram-negative aerobes','Atypical organisms only','Protozoa']),
('Oral absorption of vancomycin is:','Poor',['Complete','Greater than 90%','Enhanced by food']),
('For systemic MRSA, vancomycin is given by the:','IV route',['Oral route','Topical route only','Intranasal route']),
('Alternative MRSA drugs listed are:','Doxycycline, ceftaroline, clindamycin and cotrimoxazole',['Penicillin V, ampicillin and aztreonam','Fosfomycin only','Cefazolin and cefuroxime only']),
('E. faecalis endocarditis is initially treated with:','Ampicillin',['Vancomycin first in every case','Linezolid','Daptomycin']),
('If E. faecalis is unresponsive to ampicillin, use:','Vancomycin',['Penicillin V','Bacitracin','Fosfomycin']),
('E. faecium endocarditis is treated with:','Vancomycin',['Ampicillin in every case','Cefazolin','Aztreonam']),
('Vancomycin-unresponsive enterococcus is termed:','VRE',['VRSA','VISA','MRSA']),
('The drug of choice for VRE is:','Linezolid',['Vancomycin','Ampicillin','Penicillin G']),
('Other VRE options are:','Streptogramins and daptomycin',['Cefazolin and cefuroxime','Fosfomycin and bacitracin','Amoxicillin and cefixime']),
('Oral vancomycin is used for:','Pseudomembranous enterocolitis',['Systemic MRSA bacteraemia','Meningitis','Endocarditis']),
('For a first non-fulminant C. difficile episode, the drug of choice is:','Oral fidaxomicin',['IV vancomycin','Oral metronidazole','IV linezolid']),
('An alternative for a first non-fulminant episode is:','Oral vancomycin',['IV vancomycin','Bacitracin','Ceftriaxone']),
('For a second episode at age at least 60 years, use:','Oral fidaxomicin',['Ceftriaxone','IV metronidazole alone','Bacitracin']),
('For a second episode below age 60 years, use:','Oral fidaxomicin plus bezlotoxumab',['Oral vancomycin alone','IV cefazolin','Linezolid alone']),
('Fulminant pseudomembranous enterocolitis is treated with:','Oral vancomycin plus IV metronidazole',['Oral fidaxomicin alone','IV vancomycin alone','Ceftriaxone plus gentamicin']),
])
unit('Vancomycin Adverse Effects and Precision Dosing','Rapid infusion triggers histamine-mediated red-man syndrome, prevented by slow infusion and diphenhydramine. Ototoxicity and nephrotoxicity motivate dose individualisation by Matzke, Sawchuk or preferably Bayesian methods.')
facts(166,[
('Rapid IV vancomycin can cause:','Red-man syndrome',['Stevens-Johnson syndrome','Serotonin syndrome','Cheese reaction']),
('Red-man syndrome results from increased:','Histamine release',['Dopamine release','GABA release','Insulin release']),
('The flushing of red-man syndrome is caused by:','Vasodilation',['Vasoconstriction','Haemolysis','Thrombosis']),
('The best prevention of red-man syndrome is:','Slow IV infusion',['Rapid IV push','Oral dosing for systemic infection','Adding cilastatin']),
('Premedication for red-man syndrome uses:','Diphenhydramine, an H1 blocker',['Cyproheptadine, a 5HT2 blocker','Propranolol','Dantrolene']),
('Other major vancomycin toxicities are:','Ototoxicity and nephrotoxicity',['Hepatotoxicity and retinopathy','Agranulocytosis and myocarditis','Pseudolithiasis and kernicterus']),
('The Matzke nomogram chooses vancomycin dose based on:','Creatinine clearance',['Liver function','Age only','Body temperature']),
('The Sawchuk method is based on:','Vancomycin pharmacokinetics after a first dose',['Creatinine alone','Bayes theorem alone','Liver excretion']),
('The Sawchuk method measures:','Elimination constant and volume of distribution',['Only albumin','Only GFR','Only oral absorption']),
('Ctr denotes:','Trough concentration',['Peak concentration','Toxic concentration','Target clearance']),
('Cmax denotes:','Peak plasma concentration',['Trough concentration','Renal clearance','Volume of distribution']),
('The best vancomycin dosing approach listed is:','Bayesian software',['Matzke nomogram','Sawchuk nomogram','Fixed dose for all']),
('A disadvantage of Bayesian software is that it is:','Expensive',['Inaccurate','Based only on creatinine','Unable to predict a next dose']),
('Bayesian vancomycin dosing applies:','Bayes theorem',['Henderson-Hasselbalch equation','Fick principle','Michaelis-Menten only']),
('Bayesian software compares first-dose pharmacokinetics with:','General-population pharmacokinetics',['Only creatinine clearance','Liver enzymes','Bacterial MIC alone']),
])
unit('Other Glycopeptides','Teicoplanin, dalbavancin, telavancin and oritavancin are IV glycopeptides. Dalbavancin is longest acting; telavancin and oritavancin also depolarise the membrane. They are approved for MRSA skin and soft-tissue infection, not systemic MRSA disease.')
facts(166,[
('Other glycopeptides listed include:','Teicoplanin, dalbavancin, telavancin and oritavancin',['Cefazolin, cefuroxime, ceftriaxone and cefepime','Imipenem, meropenem, ertapenem and aztreonam','Fosfomycin, cycloserine, bacitracin and mupirocin']),
('The longest-acting glycopeptide is:','Dalbavancin',['Teicoplanin','Telavancin','Oritavancin']),
('Telavancin and oritavancin additionally:','Depolarise the cell membrane',['Block DNA gyrase','Inhibit folate','Block ribosomes']),
('The route for these other glycopeptides is:','Intravenous',['Oral','Intranasal','Transdermal']),
('Their approved MRSA uses are:','Skin and soft-tissue infections',['All systemic infections','Meningitis only','UTI only']),
('These agents are not approved for:','Systemic MRSA infection',['MRSA skin infection','MRSA soft-tissue infection','IV administration']),
])
finish()
