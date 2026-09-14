# -*- coding: utf-8 -*-
"""Generate chapters 42-46 from Marrow Pharmacology E8, book pp167-188."""
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

# CHAPTER 42 -----------------------------------------------------------------
start(42)
unit('Bacterial Protein Synthesis: Ribosomal Sites and Drug Targets',
 'The bacterial ribosome diagram shows three m-RNA sites - E (ejection), P (peptidyl, old t-RNA) and A (acceptor, new t-RNA). Step I is peptidyl transferase moving the peptide onto the new A-site t-RNA and is blocked by chloramphenicol and pleuromutilin on the 50S subunit with high toxicity; A-site binding is 30S-specific (tetracyclines block it, aminoglycosides misread m-RNA). Step II translocation is blocked by macrolides, linezolid, streptogramins and lincosamide (clindamycin) on the 50S subunit.')
facts(167,[
('The three ribosomal sites labelled on the m-RNA in step I are:','E-site, P-site and A-site',['Only P-site and A-site','E-site, P-site and T-site','P-site, A-site and R-site'],'The diagram labels E-site (ejection), P-site (peptidyl) and A-site (acceptor).'),
('In the step I diagram the E-site is the site of:','Ejection',['Peptidyl transfer','Acceptor binding','Translocation'],'E-site is annotated "(Ejection)" in the diagram.'),
('The P-site in step I carries the:','Old t-RNA (peptidyl)',['New t-RNA with amino acids','Ejected t-RNA','m-RNA itself'],'The P-site (peptidyl) holds the old t-RNA.'),
('The A-site is also called the:','Acceptor site',['Ejection site','Peptidyl site','Primer site'],'A-site is annotated "(Acceptor)".'),
('In step I the peptide chain is transferred to the new t-RNA by:','Peptidyl transferase',['Translocase','RNA polymerase','Aminoacyl t-RNA synthetase'],'The curved arrow of step I is labelled peptidyl transferase.'),
('The new t-RNA arriving at the A-site in step I carries:','Amino acids (AA)',['A DNA primer','Pyrophosphate','Ribosomal proteins'],'The new t-RNA is drawn with (AA); AA = amino acids.'),
('The two drugs shown inhibiting peptidyl transferase are:','Chloramphenicol and pleuromutilin',['Tetracyclines and aminoglycosides','Macrolides and linezolid','Clindamycin and streptogramins'],'A (-) bracket from peptidyl transferase points to chloramphenicol and pleuromutilin.'),
('The two peptidyl-transferase inhibitors share which two page features?','High toxicity and 50S subunit action',['Low toxicity and 30S subunit action','Bactericidal action and 30S subunit','Cell-wall action and high toxicity'],'The bracket beside them lists "High toxicity" and "50S subunit".'),
('Binding to the A-site is specific for which ribosomal subunit?','30S subunit',['50S subunit','40S subunit','60S subunit'],'The A-site branch is labelled "30S subunit specific".'),
('The two drug groups shown binding the A-site are:','Tetracyclines and aminoglycosides',['Macrolides and lincosamides','Chloramphenicol and pleuromutilin','Linezolid and streptogramins'],'The 30S A-site branch splits into tetracyclines and aminoglycosides.'),
('Tetracyclines act on the ribosome by:','Blocking the A-site',['Misreading of m-RNA','Blocking translocation','Inhibiting peptidyl transferase'],'Tetracyclines: blocks A-site.'),
('Aminoglycosides act on the ribosome by causing:','Misreading of m-RNA',['Blocking the A-site','Blocking translocation','Inhibiting peptidyl transferase'],'Aminoglycosides: misreading of m-RNA.'),
('Misreading of m-RNA by aminoglycosides finally leads to:','Abnormal protein formation and bacterial death',['Blocked translocation only','Intact but inactive ribosomes','Cell-wall lysis'],'Misreading -> abnormal protein formation -> bacterial death.'),
('In step II the t-RNA sitting in the E-site is:','Ejected',['Translocated to the P-site','Recharged with amino acids','Bound to the A-site'],'Step II shows an "Ejected" arrow leaving the E-site.'),
('The step II movement of the peptidyl t-RNA from A-site towards P-site is called:','Translocation',['Peptidyl transfer','Ejection','Uncoating'],'The step II arrow between A-site and P-site is labelled translocation.'),
('The drugs listed as acting on the 50S subunit to block step II are:','Macrolide, linezolid, streptogramins and lincosamide (clindamycin)',['Tetracyclines and aminoglycosides','Chloramphenicol and pleuromutilin','Polymyxins and daptomycin'],'The four-drug list acts on the 50S subunit with a (-) on translocation.'),
('The lincosamide named inside the 50S translocation-block list is:','Clindamycin',['Clarithromycin','Clavulanic acid','Colistin'],'The list reads "Lincosamide (Clindamycin)".'),
('In the step II diagram the incoming new t-RNA first occupies the:','A-site',['P-site','E-site','5-prime end of m-RNA'],'The new t-RNA arrow points into the A-site (acceptor).'),
('The abbreviation AA in the protein-synthesis diagram stands for:','Amino acids',['Antibiotic activity','Acetyl groups','Adenosine'],'The legend at right reads "AA : Amino Acids".'),
])
unit('MLS-B Resistance and the Macrolide Binding Site',
 'MLS-B resistance means the bacteria produce a methylase that methylates the MBS (macrolide binding site), giving macrolide resistance. Lincosamide and streptogramin B share that same MBS, so one methylation event produces cross resistance across the whole group.')
facts(167,[
('In MLS-B resistance the bacteria produce:','Methylase',['Beta-lactamase','An efflux pump','Acetyltransferase'],'MLS-B resistance: bacteria produce methylase.'),
('The methylase of MLS-B resistance acts by:','Methylation of the MBS (macrolide binding site)',['Hydrolysing the drug','Phosphorylating the ribosome','Altering DNA gyrase'],'The flow is methylase -> methylation of MBS (macrolide binding site).'),
('Methylation of the MBS finally produces:','Macrolide resistance',['Aminoglycoside resistance','Vancomycin resistance','Tetracycline resistance'],'Methylation of MBS -> macrolide resistance.'),
])
facts(168,[
('The MBS is the same binding site for:','Lincosamide and streptogramin B',['Streptogramin A and tetracycline','Linezolid and oxazolidinones','Chloramphenicol and pleuromutilin'],'MBS: same binding site for lincosamide and streptogramin B.'),
('Because the MBS is shared by macrolides, lincosamide and streptogramin B, methylation leads to:','Development of cross resistance',['Selective macrolide resistance only','Increased drug uptake into the ribosome','Loss of efflux pumps'],'Shared MBS explains the development of cross resistance.'),
])
unit('Tetracyclines: MOA, Routes, Spectrum and Resistance',
 'Tetracyclines block the 30S A-site; the IM route is contraindicated because of pain and inflammation, while IV and oral are used with minocycline (100%) better absorbed than doxycycline. The spectrum is wide (gram +ve and gram -ve) except Proteus, Pseudomonas and Providencia, and resistance comes through drug efflux, enzyme inactivation and ribosomal protective protein.')
facts(168,[
('The mechanism of action of tetracyclines is:','Blocks the A-site',['Blocks the P-site','Blocks translocation','Inhibits peptidyl transferase'],'Tetracyclines MOA: blocks A-site.'),
('The intramuscular route of tetracyclines is contraindicated because of:','Pain and inflammation',['Necrosis of muscle','Poor absorption only','Nerve injury'],'Note: i/m is C/I due to pain & inflammation.'),
('The routes available for tetracyclines on the page are:','IV and oral',['IM and oral','Topical and IV','Oral only'],'Route: I/v and oral (bio-availability).'),
('The oral bio-availability ranking given for tetracyclines is:','Minocycline (100%) > doxycycline',['Doxycycline (100%) > minocycline','Tetracycline > minocycline','Demeclocycline > doxycycline'],'Oral bio-availability: minocycline (100%) > doxycycline.'),
('The tetracycline spectrum is described as:','Wide, covering gram +ve and gram -ve',['Narrow gram +ve only','Narrow gram -ve only','Only atypical organisms'],'Spectrum: wide - gram +ve and gram -ve.'),
('The organisms excepted from the tetracycline spectrum are:','Proteus, Pseudomonas and Providencia',['Staphylococcus, Streptococcus and Enterococcus','E. coli, Klebsiella and Salmonella','Mycoplasma, Chlamydia and Rickettsia'],'Except: Proteus, Pseudomonas, Providencia, etc.'),
('The tetracycline mechanisms of resistance listed are:','Drug efflux, enzyme inactivation and ribosomal protective protein',['Target methylation, efflux and beta-lactamase','Altered ribosome, porin loss and PBP change','Efflux, PBP change and topoisomerase mutation'],'MOR: drug efflux, enzyme inactivation, ribosomal protective protein.'),
('Which single resistance mechanism of the page belongs to tetracyclines?','Ribosomal protective protein',['Methylation of the macrolide binding site','Altered ribosome seen only with streptomycin','Beta-lactamase production'],'Ribosomal protective protein is one of the three tetracycline MOR mechanisms.'),
])
unit('Tetracycline Drugs and Their DOC Uses',
 'Doxycycline is the workhorse - DOC for mycoplasma (STD), plague prophylaxis, rickettsial disease (scrub typhus), Borrelia, Brucella, chlamydia (STD) and cholera ("my Pink RBC"). Minocycline is DOC for leprosy and demeclocycline is used in SIADH. Tigecycline, a glycycycline derived from minocycline, is IV-only, covers MRSA/VRSA and gram -ve aerobes/anaerobes, but raises mortality in severe infections so it stays a last-line drug for intraabdominal infection and CAP, and is contraindicated in UTI and bacteremia.')
facts(168,[
('The tetracycline whose DOC list is summarised by the mnemonic "my Pink RBC" is:','Doxycycline',['Minocycline','Demeclocycline','Tigecycline'],'DOC: my Pink RBC is written under doxycycline.'),
('Doxycycline is DOC for which sexually transmitted infection caused by mycoplasma?','Mycoplasma (STD)',['Chlamydia only','Gonorrhoea','Syphilis'],'The doxycycline DOC list starts with mycoplasma (STD).'),
('Plague prophylaxis is a DOC use of:','Doxycycline',['Minocycline','Tigecycline','Sarecycline'],'Plague prophylaxis appears in the doxycycline DOC list.'),
('Rickettsial disease including scrub typhus is treated with:','Doxycycline',['Azithromycin only','Chloramphenicol only','Ciprofloxacin'],'Rickettsial disease (scrub typhus) is in the doxycycline DOC list.'),
('Borrelia and Brucella infections are DOC uses of:','Doxycycline',['Minocycline','Demeclocycline','Omadacycline'],'Borrelia and Brucella are listed under doxycycline.'),
('Chlamydia (STD) and cholera are DOC uses of:','Doxycycline',['Azithromycin in all patients','Tigecycline','Sulfisoxazole'],'Chlamydia (STD) and cholera complete the doxycycline DOC list.'),
('The tetracycline that is DOC for leprosy is:','Minocycline',['Doxycycline','Demeclocycline','Tigecycline'],'Minocycline use: leprosy (DOC).'),
('Demeclocycline is used for:','SIADH',['Diabetes insipidus','Hypertension','Hypercalcaemia'],'Demeclocycline use: SIADH.'),
('Tigecycline belongs to which subclass?','Glycycycline',['Aminocycline','Fluorocycline','Cephalosporin'],'Tigecycline (Glycycycline).'),
('Tigecycline is derived from:','Minocycline',['Doxycycline','Demeclocycline','Tetracycline base'],'Tigecycline is derived from minocycline.'),
('The MOA and resistance of tigecycline are:','Same as tetracycline',['Different - it blocks translocation','Same as aminoglycosides','Same as macrolides'],'MOA/MOR: same as tetracycline.'),
('The route of tigecycline is:','IV only',['Oral only','Oral and IV','Topical'],'Route: IV only.'),
('The gram +ve spectrum of tigecycline covers:','MRSA and VRSA',['Only penicillin-sensitive streptococci','Enterococcus only','No gram +ve cover'],'Spectrum gram +ve: MRSA, VRSA.'),
('The gram -ve spectrum of tigecycline covers:','Aerobes and anaerobes',['Only aerobes','Only anaerobes','Neither'],'Spectrum gram -ve: aerobes, anerobes.'),
('Tigecycline increases mortality in severe infections compared with other drugs and is therefore kept as a:','Last line drug',['First line drug','Prophylactic drug','Monotherapy drug'],'Increased mortality in severe infections -> last line drug.'),
('The listed uses of tigecycline are:','Intraabdominal infection and community acquired pneumonia (CAP)',['UTI and bacteremia','Meningitis and endocarditis','Skin infection only'],'Use: intraabdominal infection and CAP.'),
('Tigecycline is contraindicated in UTI and bacteremia because it:','Is not concentrated well in blood and urine',['Is rapidly metabolised by the liver','Binds plasma proteins completely','Is inactivated by surfactant'],'C/I UTI and bacteremia: not concentrated well in blood & urine.'),
])
unit('Scrub Typhus Note and the Tetracycline Side-effect Packet',
 'Scrub typhus presents with fever, rash and an eschar with central necrosis; mild/moderate disease takes oral doxycycline while severe meningitis or pneumonia needs IV doxycycline plus azithromycin. The tetracycline "tetra packet" of side effects covers photosensitivity, pseudotumor cerebri, acute renal failure (except doxycycline), calcium binding with inhibited bone growth, kidney V2 receptor blockade (diabetes insipidus, maximal with demeclocycline), esophagitis, Fanconi syndrome from expired drug (citrates) and yellow teeth in kids.')
facts(169,[
('The symptoms of scrub typhus listed in the note are:','Fever, rash and eschar with central necrosis',['Fever, cough and pleuritic pain','Rash, arthritis and urethritis','Fever, jaundice and bleeding'],'Note: scrub typhus symptoms - fever, rash, eschar central necrosis.'),
('Mild or moderate scrub typhus is treated with:','Oral doxycycline',['IV doxycycline alone','Oral azithromycin alone','IV chloramphenicol'],'Treatment mild/moderate: oral doxycycline.'),
('Severe scrub typhus with meningitis or pneumonia is treated with:','IV doxycycline + azithromycin',['Oral doxycycline alone','IV ceftriaxone','Oral chloramphenicol'],'Severe (meningitis/pneumonia): IV doxycycline + azithromycin.'),
('The tetracycline side-effect mnemonic written on the page is:','Tetra packet',['Tetra block','TETRA Toxicity','Four-Fold'],'The side-effect heading reads "Tetra packet".'),
('The skin-related tetracycline side effect is:','Photosensitivity',['Pigmentation only','Acne','Urticaria only'],'First packet item: photosensitivity.'),
('The CNS side effect of tetracyclines in the packet is:','Pseudotumor cerebri',['Meningitis','Encephalitis','Peripheral neuropathy'],'Second packet item: pseudotumor cerebri.'),
('Acute renal failure from tetracyclines occurs with all except:','Doxycycline',['Minocycline','Demeclocycline','Tetracycline base'],'Acute renal failure (except doxycycline).'),
('Tetracyclines inhibit bone growth by:','Increased Ca++ binding',['Blocking vitamin D','Chelating magnesium','Inhibiting collagen cross-linking'],'Increased Ca++ binding: inhibits bone growth.'),
('The tetracycline effect that is used therapeutically in diabetes insipidus is:','Kidney V2 receptor blockade',['ADH stimulation','Aquaporin upregulation','Sodium retention'],'Kidney V2 receptor blocker: used in diabetes insipidus.'),
('The maximum V2-blocking effect for diabetes insipidus is seen with:','Demeclocycline',['Doxycycline','Minocycline','Tigecycline'],'Diabetes insipidus effect is max with demeclocycline.'),
('The gastrointestinal side effect of tetracyclines in the packet is:','Esophagitis',['Gastric ulcer','Colitis','Pancreatitis'],'Packet item: esophagitis.'),
('Expired tetracycline causes:','Fanconi syndrome (citrates)',['Gray baby syndrome','Stevens-Johnson syndrome','Nephrotic syndrome'],'Expired drug: Fanconi syndrome (citrates).'),
('Tetracyclines given to kids discolour teeth to:','Yellow',['Brown-black','Grey','Green'],'Teeth -> yellow (kids).'),
])
unit('Tetracycline Contraindications and Aminoglycoside MOA and Uses',
 'Tetracyclines are contraindicated in pregnancy and children because of bone growth abnormality, and should not be taken with milk and antacids. Aminoglycosides cause misreading of mRNA producing abnormal protein - a cidal effect - and are used as monotherapy in gram -ve aerobes (except typhoid), as add-on drugs in Pseudomonas infection, and with ampicillin or vancomycin for gram +ve Staphylococcus and Enterococcus.')
facts(169,[
('Tetracyclines are contraindicated in pregnancy and children because of:','Bone growth abnormality',['Hepatotoxicity','Nephrotoxicity','Ototoxicity'],'Pregnancy and children are bracketed to bone growth abnormality.'),
('Tetracyclines should not be co-administered with:','Milk and antacids',['Fruit juice','Coffee','Plain water'],'Contraindication: with milk and antacids.'),
('The one-line mechanism of aminoglycosides on the page is:','Misreading of mRNA -> abnormal protein -> cidal effect',['Blocking A-site -> static effect','Blocking translocation -> cidal effect','Depolarising membrane -> cidal effect'],'MOA: misreading of mRNA -> abnormal protein -> cidal effect.'),
('The killing nature of aminoglycosides is described as:','Cidal effect',['Static effect','Bacteriostatic at all doses','Only synergistic'],'The chain ends in "Cidal effect".'),
('Aminoglycosides can be used as monotherapy in:','Gram -ve aerobes except typhoid',['All gram -ve organisms including typhoid','Gram +ve anaerobes','Atypical organisms'],'Monotherapy in gram -ve aerobs (except typhoid).'),
('Aminoglycosides are add-on drugs for which infection?','Pseudomonas infection',['Meningococcal meningitis','Syphilis','Tetanus'],'Add on drugs: Pseudomonas infection.'),
('Combined with ampicillin or vancomycin, aminoglycosides cover which gram +ve organisms?','Staphylococcus and Enterococcus',['Streptococcus pneumoniae and Listeria','Bacillus and Corynebacterium','Nocardia and Actinomyces'],'With ampicillin/vancomycin for gram +ve: Staphylococcus, Enterococcus.'),
])
unit('Aminoglycoside Spectrum, Routes, Resistance and Individual Drugs',
 'Aminoglycosides cover gram -ve aerobes but not anaerobes or gram +ve organisms, and are given IV or IM because oral absorption is poor. Resistance is by enzyme inactivation (except amikacin) and, only for streptomycin, an altered ribosome. Gentamicin outranks streptomycin and both are DOC for plague and tularemia; neomycin is given orally for gut sterilization in hepatic encephalopathy (now rifaximin is DOC) and tobramycin is inhaled for pseudomonas pneumonia in cystic fibrosis.')
facts(169,[
('The aminoglycoside spectrum covers:','Gram -ve aerobes',['Gram -ve anaerobes','Gram +ve aerobes','All bacteria'],'Spectrum: gram -ve aerobes.'),
('Aminoglycosides are not active against:','Anaerobes and gram +ve organisms',['Gram -ve aerobes','Mycobacteria only','Pseudomonas'],'Not active against anaerobes and gram +ve.'),
('The aminoglycoside routes listed are:','IV, IM and oral with poor absorption',['Oral with good absorption','Topical and oral','IV only'],'Routes: I/v, I/m, oral poor absorption.'),
('Oral aminoglycosides are characterised by:','Poor absorption',['Complete absorption','Enteric coating','First-pass metabolism'],'Oral: poor absorption.'),
('The common aminoglycoside resistance mechanism is:','Enzyme inactivation',['Target methylation','Efflux pumps','Porin loss'],'MOR: enzyme inactivation (except amikacin).'),
('The aminoglycoside excepted from enzyme-inactivation resistance is:','Amikacin',['Gentamicin','Tobramycin','Netilmicin'],'Enzyme inactivation (except amikacin).'),
('Altered-ribosome resistance is seen only with:','Streptomycin',['Amikacin','Neomycin','Gentamicin'],'Altered ribosome: only in streptomycin.'),
('The potency relation written between the first two aminoglycosides is:','Gentamicin > streptomycin',['Streptomycin > gentamicin','Gentamicin = streptomycin','Tobramycin > gentamicin'],'Drugs: a. gentamicin > streptomycin.'),
('Gentamicin/streptomycin are DOC for:','Plague and tularemia',['Brucellosis and Q fever','Tuberculosis and leprosy','Typhoid and paratyphoid'],'DOC: plague, tularemia.'),
('Neomycin is used orally for:','Gut sterilization in hepatic encephalopathy',['Whole-body gram -ve sepsis','UTI monotherapy','Bacterial meningitis'],'Neomycin use: orally for gut sterilization in hepatic encephalopathy.'),
('The current drug of choice for gut sterilization in hepatic encephalopathy is:','Rifaximin',['Neomycin','Metronidazole','Vancomycin'],'The Rx arrow under neomycin points to rifaximin (DOC).'),
('Tobramycin is given by which route?','Inhalational route',['Intravenous only','Oral','Intramuscular'],'Tobramycin: inhalational route.'),
('Tobramycin is used for pseudomonas pneumonia in:','Cystic fibrosis',['Bronchiectasis only','COPD','Lung abscess'],'Use: pseudomonas pneumonia in cystic fibrosis.'),
])
unit('Aminoglycoside Side Effects, Contraindication and Newer Drugs',
 'Aminoglycoside nephrotoxicity is reversible - maximal with neomycin and minimal with streptomycin. Neuromuscular toxicity (decreased ACh) comes from pre-synaptic voltage-gated Ca++ channel blockage, is maximal with neomycin and minimal with tobramycin, and is treated with calcium then neostigmine. Ototoxicity damages outer hair cells causing irreversible hearing loss that early Ca++ supplementation can prevent - auditory maximal with amikacin, vestibular maximal with streptomycin (also minocycline) and overall minimal with netilmicin; pregnancy is contraindicated because the drugs cross the placenta.')
facts(170,[
('Aminoglycoside nephrotoxicity is:','Reversible',['Irreversible','Only pre-renal','Absent with all drugs'],'Nephrotoxic: reversible.'),
('Maximum nephrotoxicity among aminoglycosides is with:','Neomycin',['Streptomycin','Tobramycin','Netilmicin'],'Nephrotoxic max: neomycin.'),
('Minimum nephrotoxicity among aminoglycosides is with:','Streptomycin',['Neomycin','Amikacin','Gentamicin'],'Nephrotoxic min: streptomycin.'),
('Aminoglycoside neuromuscular toxicity is associated with decreased:','ACh',['Dopamine','GABA','Serotonin'],'Neuromuscular toxicity (down Ach).'),
('The site of aminoglycoside neuromuscular block is the:','Pre-synaptic voltage gated Ca++ channel',['Post-synaptic ACh receptor','Motor neuron nucleus','Muscle membrane Na+ channel'],'Pre-synaptic voltage gated Ca++ channel blockage.'),
('Maximum neuromuscular toxicity is with:','Neomycin',['Tobramycin','Streptomycin','Amikacin'],'Neuromuscular max: neomycin.'),
('Minimum neuromuscular toxicity is with:','Tobramycin',['Neomycin','Gentamicin','Streptomycin'],'Neuromuscular min: tobramycin.'),
('The treatment of aminoglycoside neuromuscular toxicity is:','Ca++ then neostigmine',['Neostigmine before calcium','Atropine','Dantrolene only'],'Treatment: Ca++ > neostigmine.'),
('Aminoglycoside ototoxicity damages which structure?','Outer hair cells (neuronal damage)',['Inner hair cells only','Tympanic membrane','Auditory cortex'],'Ototoxicity: outer hair cell damage (neuronal damage).'),
('Aminoglycoside hearing loss is irreversible but can be prevented by:','Early Ca++ supplementation',['Early steroid therapy','Dose escalation','Alkalinising urine'],'Irreversible hearing loss can be prevented with early Ca++ supplementation.'),
('Maximum auditory toxicity is with:','Amikacin',['Streptomycin','Neomycin','Tobramycin'],'Max auditory toxicity: amikacin.'),
('Maximum vestibular toxicity is with:','Streptomycin',['Amikacin','Netilmicin','Gentamicin'],'Max vestibular toxicity: streptomycin.'),
('Vestibular toxicity is also noted with which non-aminoglycoside?','Minocycline',['Doxycycline','Tigecycline','Omadacycline'],'The bracket adds "(Also in minocycline)".'),
('Minimum ototoxicity is with:','Netilmicin',['Amikacin','Streptomycin','Kanamycin'],'Min ototoxicity: netilmicin.'),
('Aminoglycosides are contraindicated in pregnancy because they:','Can cross the placenta',['Cause uterine contraction','Are teratogenic by folate block','Increase maternal BP'],'Contraindication: pregnancy (can cross placenta).'),
('The newer tetracycline used for acne is:','Sarecycline',['Omadacycline','Eravacycline','Plazomicin'],'Newer tetracycline: sarecycline - acne.'),
('The newer tetracycline used for pneumonia (CAP) is:','Omadacycline',['Sarecycline','Tigecycline','Doxycycline'],'Newer tetracycline: omadacycline - pneumonia (CAP).'),
('The newer aminoglycoside used for UTI is:','Plazomicin',['Sarecycline','Omadacycline','Netilmicin'],'Newer aminoglycoside: plazomicin - UTI.'),
])
finish()

# CHAPTER 43 -----------------------------------------------------------------
start(43)
unit('Macrolides: 50S MOA, Resistance and Erythromycin Basics',
 'Macrolides are 50S-subunit drugs whose MOA is translocase inhibition; resistance is enzymatic inactivation or MLS-B type. Erythromycin is given orally or IV, mirrors penicillin G on gram +ve organisms with the same action on gram -ve, and is DOC for pertussis, diphtheria and rheumatic fever prophylaxis in penicillin allergy.')
facts(171,[
('The chapter heading places macrolides among drugs acting on which ribosomal subunit?','50S subunit',['30S subunit','40S subunit','70S initiation complex'],'Heading: drugs acting on 50s subunit.'),
('The mechanism of action of macrolides is:','Translocase inhibitor',['Peptidyl transferase inhibitor','A-site blocker','Misreading of mRNA'],'Macrolides MOA: translocase inhibitor.'),
('The macrolide mechanisms of resistance listed are:','Enzymatic inactivation and MLS-B type resistance',['Efflux only','Ribosomal protective protein','Beta-lactamase'],'MOR: enzymatic inactivation; MLS-B type resistance.'),
('The routes of erythromycin are:','Oral / IV',['IM only','Topical only','Oral only'],'Erythromycin route: oral / IV.'),
('The gram +ve spectrum of erythromycin is similar to:','Penicillin G',['Penicillin V','Flucloxacillin','Ampicillin'],'Gram +ve (similar to penicillin G).'),
('The gram -ve action of erythromycin is described as:','Same action as on gram +ve',['No gram -ve action','Only antipseudomonal','Only anti-H. pylori'],'Gram -ve (same action).'),
('Erythromycin is DOC in:','Pertussis',['Tetanus','Botulism','Gas gangrene'],'DOC in: pertussis.'),
('Erythromycin is DOC in which toxin-mediated airway disease?','Diphtheria',['Pertussis only','Epiglottitis','Ludwig angina'],'DOC in: diphtheria.'),
('Rheumatic fever prophylaxis in a penicillin-allergic patient uses:','Erythromycin',['Clindamycin','Azithromycin always','Cephalexin'],'Rheumatic fever prophylaxis (in penicillin allergy).'),
])
unit('Erythromycin Side Effects and Secondary Use',
 'The erythromycin side-effect mnemonic "macro SD Card" covers motilin-receptor agonism causing hypertrophic pyloric stenosis, skeletal muscle weakness, diarrhea and cardiac effects - QT prolongation in the order erythromycin > clarithromycin > azithromycin with risk of torsade de pointes - plus cholestatic jaundice only with the estolate salt. Its prokinetic property gives the secondary use in gastroparesis.')
facts(171,[
('The erythromycin side-effect mnemonic on the page is:','macro SD Card',['macro QT','macro SE','macro ABC'],'S/E mnemonic: macro SD Card.'),
('Erythromycin causes hypertrophic pyloric stenosis (HPS) by acting as a:','Motilin receptor agonist',['Gastrin antagonist','Serotonin antagonist','Histamine agonist'],'Motilin receptor agonist: hypertrophic pyloric stenosis (HPS).'),
('The muscle side effect of erythromycin listed is:','Skeletal muscle weakness',['Myopathy with raised CK','Rhabdomyolysis','Myasthenia gravis'],'Skeletal muscle weakness.'),
('The GIT side effect of erythromycin in the mnemonic list is:','Diarrhea',['Constipation','Colitis','Vomiting only'],'Diarrhea.'),
('The QT prolongation order among macrolides is:','Erythromycin > clarithromycin > azithromycin',['Azithromycin > clarithromycin > erythromycin','Clarithromycin > erythromycin > azithromycin','All three equal'],'Cardiac S/E: QT prolongation (erythromycin > clarithromycin > azithromycin).'),
('The cardiac risk that follows macrolide QT prolongation is:','Risk of torsade de pointes',['Atrial fibrillation','Bradycardia','Heart block'],'Risk of torsade de pointes.'),
('Cholestatic jaundice occurs only with which erythromycin salt?','Erythromycin estolate salt',['Erythromycin base','Erythromycin ethylsuccinate','Erythromycin stearate'],'Cholestatic jaundice (only with erythromycin estolate salt).'),
('The secondary (prokinetic) use of erythromycin is:','Gastroparesis',['GERD','Peptic ulcer','Ileus prevention post-op'],'Secondary use: gastroparesis.'),
])
unit('Clarithromycin and Azithromycin',
 'Clarithromycin is oral with BD dosing and is used for mycobacterium and H. pylori. Azithromycin, oral or IV, is the longest-acting macrolide with OD dosing and is DOC for atypical pneumonia (chlamydia, mycoplasma, legionella), campylobacter, chlamydia (STD) and cholera in pregnancy or children, and is the add-on drug in scrub typhus.')
facts(171,[
('The route and dosing of clarithromycin are:','Oral (BD dosing)',['IV only','Oral OD dosing','IM BD dosing'],'Clarithromycin route: oral (BD dosing).'),
('The uses of clarithromycin listed are:','Mycobacterium and H. pylori',['Legionella and chlamydia','Pertussis and diphtheria','Gastroparesis and GERD'],'Clarithromycin use: mycobacterium; H. pylori.'),
('The routes of azithromycin are:','Oral/IV',['Oral only','IV only','Topical'],'Azithromycin route: oral/IV.'),
('The longest-acting macrolide with OD dosing is:','Azithromycin',['Clarithromycin','Erythromycin','Roxithromycin'],'Azithromycin: longest acting (OD dosing).'),
('Azithromycin is DOC for atypical pneumonia caused by:','Chlamydia, mycoplasma and legionella',['Streptococcus pneumoniae','Klebsiella','Pseudomonas'],'DOC atypical pneumonia: chlamydia, mycoplasma, legionella.'),
('Azithromycin is DOC for which curved gram -ve organism?','Campylobacter',['Helicobacter','Vibrio','Spirochaete'],'DOC: campylobacter.'),
('Azithromycin is DOC for which sexually transmitted infection?','Chlamydia (STD)',['Gonorrhoea','Syphilis','Trichomonas'],'DOC: chlamydia (STD).'),
('Cholera in pregnancy or children is treated with:','Azithromycin',['Doxycycline','Tetracycline','Ciprofloxacin'],'Cholera in pregnancy/children.'),
('The add-on drug in scrub typhus (with IV doxycycline in severe disease) is:','Azithromycin',['Clarithromycin','Erythromycin','Spiramycin'],'Add on drug in scrub typhus.'),
])
unit('Oxazolidinones: Linezolid and Tedizolid',
 'Linezolid causes bone marrow suppression, is an MAO inhibitor (cheese reaction with HTN crisis treated by IV phentolamine) and produces mitochondrial toxicity with lactic acidosis and optic neuritis. It is a last-line gram +ve drug and DOC for VRE, MRSA/VRSA and resistant TB, with IV and oral BD dosing at 100% oral bioavailability. Tedizolid causes less marrow suppression and its longer half-life permits OD dosing.')
facts(172,[
('The marrow side effect of linezolid is:','Bone marrow suppression',['Aplastic anaemia only','Haemolysis','Eosinophilia'],'Linezolid S/E: bone marrow suppression.'),
('Linezolid causes the cheese reaction because it is a:','MAO inhibitor',['COMT inhibitor','Tyramine agonist','Histamine releaser'],'MAO inhibitor -> cheese reaction.'),
('The cheese reaction of linezolid presents as:','HTN crisis',['Hypotensive shock','Bronchospasm','Flush without BP change'],'Cheese reaction: HTN crisis.'),
('The treatment of linezolid cheese-reaction HTN crisis is:','I/V phentolamine',['Oral amlodipine','IV labetalol always','Nitroprusside'],'Rx: I/V phentolamine.'),
('Mitochondrial toxicity of linezolid causes:','Lactic acidosis and optic neuritis',['Peripheral neuropathy only','Hepatic failure','Cardiomyopathy'],'Mitochondrial toxicity -> lactic acidosis, optic neuritis.'),
('Linezolid is used as a last-line drug against:','Gram +ve organisms',['Gram -ve organisms','Anaerobes','Fungi'],'Use: last line against gram +ve.'),
('Linezolid is DOC in:','Vancomycin resistant enterococcus (VRE)',['MRSA only','Resistant TB only','All of the above separately listed'],'DOC in: VRE, MRSA/VRSA, resistant TB - VRE is listed first.'),
('Linezolid is DOC in which resistant staphylococcal forms?','MRSA/VRSA',['VRE only','ORSAs','Beta-lactamase producers'],'DOC in: MRSA/VRSA.'),
('Linezolid is DOC in which mycobacterial situation?','Resistant TB',['Newly diagnosed TB','Latent TB','Atypical mycobacteria only'],'DOC in: resistant TB.'),
('The routes and dosing of linezolid are:','IV and oral, BD dosing',['IV only','Oral OD dosing','IM BD dosing'],'Route: I/v and oral - BD dosing.'),
('The oral bioavailability of linezolid is:','100%',['50%','70%','90%'],'Bioavailability: 100%.'),
('Tedizolid is less toxic than linezolid because it causes:','Less bone marrow suppression',['Less optic neuritis','Less lactic acidosis','Less neuropathy'],'Tedizolid: less toxic - less BM suppression.'),
('The increased half-life of tedizolid allows:','OD dosing',['BD dosing','TDS dosing','Weekly dosing'],'Increased T1/2 life: OD dosing.'),
])
unit('Streptogramins',
 'Streptogramins are IV-only because infusion-site pain, inflammation and edema force the use of a central line. Their spectrum is gram +ve plus atypical organisms and they serve as last-line drugs in MRSA, VRSA and VRE.')
facts(172,[
('The route of streptogramins is:','IV only',['Oral','IM','Topical'],'Streptogramins route: IV only.'),
('The infusion-site problems of streptogramins are:','Pain, inflammation and edema',['Necrosis and gangrene','Phlebitis only','Urticaria'],'Pain, inflammation, edema at site of infusion.'),
('Because of infusion-site reactions streptogramins require:','A central line',['A large peripheral cannula','An arterial line','A subcutaneous port'],'Site of infusion problems -> need of central line.'),
('The streptogramin spectrum covers:','Gram +ve and atypical organisms',['Gram -ve aerobes','Anaerobes only','Only gram -ve atypicals'],'Spectrum: gram +ve; atypical organisms.'),
('Streptogramins are used as last-line drugs in:','MRSA, VRSA and VRE',['Only MRSA','Only VRE','ESBL producers'],'Use as last line drug in MRSA, VRSA, VRE.'),
])
unit('Lincosamides (Clindamycin): Spectrum and Anaerobic Uses',
 'Clindamycin covers gram +ve aerobes (staph) and anaerobes, is not effective against gram -ve aerobes, and covers gram -ve anaerobes such as Bacteroides and Prevotella. In anaerobic infection the site decides the drug: supradiaphragmatic (oral Prevotella) takes clindamycin while intradiaphragmatic (colorectal Bacteroides) takes metronidazole.')
facts(172,[
('The gram +ve spectrum of clindamycin includes:','Aerobes (staph) and anaerobes',['Only aerobes','Only anaerobes','Neither'],'Gram +ve: aerobes (staph), anaerobes.'),
('Against gram -ve aerobes clindamycin is:','Not effective',['Highly effective','Moderately effective','Effective only in urine'],'Gram -ve aerobes: not effective.'),
('The gram -ve anaerobes covered by clindamycin are:','Bacteroides and Prevotella',['Fusobacterium only','Clostridium only','Peptostreptococcus only'],'Gram -ve anaerobes: Bacteroides/Prevotella.'),
('Supradiaphragmatic anaerobic infection is typically caused by:','Prevotella (oral)',['Bacteroides (colorectal)','Clostridium perfringens','Actinomyces'],'Table: supradiaphragmatic - Prevotella (oral).'),
('The drug chosen for supradiaphragmatic anaerobic infection is:','Clindamycin',['Metronidazole','Vancomycin','Cefoxitin'],'Table: supradiaphragmatic -> clindamycin.'),
('Intradiaphragmatic (colorectal) anaerobic infection is caused by:','Bacteroides',['Prevotella (oral)','Streptococcus anginosus','E. coli'],'Table: intradiaphragmatic - Bacteroides (colorectal).'),
('The drug chosen for intradiaphragmatic (colorectal) anaerobic infection is:','Metronidazole',['Clindamycin','Linezolid','Tigecycline'],'Table: intradiaphragmatic -> metronidazole.'),
])
unit('Clindamycin in Staphylococci and Chloramphenicol',
 'In staphylococcal disease clindamycin is DOC for toxic shock syndrome and is valued in osteomyelitis for good bone penetration. Chloramphenicol is a wide-spectrum drug formerly used for typhoid; its dangers are bone-marrow suppression and the gray baby syndrome - cardiotoxicity, decreased oxygenation of tissues and an ash/grey colour of tissues.')
facts(172,[
('In Staphylococcus infections clindamycin is DOC for:','Toxic shock syndrome',['Osteomyelitis','Endocarditis','Abscesses'],'In staphylococcus: toxic shock syndrome (DOC).'),
('Clindamycin is useful in osteomyelitis because of:','Good bone penetration',['Bactericidal action','Low protein binding','Renal excretion'],'Osteomyelitis (good bone penetration).'),
])
facts(173,[
('Chloramphenicol is described as a:','Wide spectrum drug',['Narrow spectrum drug','Gram +ve only drug','Antifungal'],'Chloramphenicol: wide spectrum drug.'),
('Chloramphenicol was used earlier in the treatment of:','Typhoid',['Meningococcal meningitis','Plague','Brucellosis'],'Use: in typhoid treatment (earlier).'),
('The marrow side effect of chloramphenicol is:','BM suppression',['Haemolysis','Leucocytosis','Thrombocytosis'],'S/E: BM suppression.'),
('Gray baby syndrome begins with:','Cardiotoxicity',['Hepatotoxicity','Nephrotoxicity','Neurotoxicity'],'Gray baby syndrome: cardiotoxicity first.'),
('In gray baby syndrome the oxygenation of tissues is:','Decreased',['Increased','Unchanged','First increased then normal'],'Cardiotoxicity -> decreased oxygenation of tissues.'),
('The colour of tissues in gray baby syndrome is:','Ash/grey',['Bright red','Blue-black','Yellow'],'Decreased oxygenation -> ash/grey colour of tissues.'),
])
unit('Pleuromutilins, Fidaxomicin, Mupirocin, Fusidic Acid and Rifaximin',
 'The pleuromutilins are topical retapamulin for skin infection and lefamulin - gram +ve, gram -ve and atypical coverage, last-line CAP, with QT prolongation and hepatotoxicity. Fidaxomicin (t-RNA polymerase inhibitor as written) is oral for pseudomembranous enterocolitis; mupirocin (t-RNA synthase inhibitor) is nasal for the MRSA carrier; fusidic acid inhibits peptide chain elongation topically for skin infection; rifaximin, an RNA polymerase inhibitor, sterilizes the gut in hepatic encephalopathy, treats travelers diarrhea and is off-label in pseudomembranous enterocolitis.')
facts(173,[
('The pleuromutilins named on the page are:','Retapamulin and lefamulin',['Fidaxomicin and mupirocin','Fusidic acid and rifaximin','Bacitracin and tyrothricin'],'Pleuromutilins branch into retapamulin and lefamulin.'),
('The route of retapamulin is:','Topical',['Oral','IV','Nasal'],'Retapamulin route: topical.'),
('The use of retapamulin is:','Skin infection',['CAP','UTI','Gut sterilization'],'Retapamulin use: skin infection.'),
('The spectrum of lefamulin covers:','Gram +ve, gram -ve and atypical bacteria',['Only gram +ve','Only atypicals','Only anaerobes'],'Lefamulin spectrum: gram +ve, gram -ve, atypical bacteria.'),
('Lefamulin is used for:','CAP (last line)',['Skin infection','Meningitis','Endocarditis'],'Lefamulin use: CAP (last line).'),
('The side effects of lefamulin are:','QT prolongation and hepatotoxicity',['Nephrotoxicity and ototoxicity','BM suppression and colitis','Photosensitivity and rash'],'Lefamulin S/E: QT prolongation, hepatotoxic.'),
('The mechanism of fidaxomicin as written on the page is:','t-RNA polymerase inhibitor',['RNA polymerase inhibitor','DNA gyrase inhibitor','Cell wall inhibitor'],'The page lists fidaxomicin MOA as t-RNA polymerase inhibitor.'),
('The use of fidaxomicin is:','Pseudomembranous enterocolitis',['Travelers diarrhea','UTI','CAP'],'Fidaxomicin use: pseudomembranous enterocolitis.'),
('The route of fidaxomicin is:','Oral',['IV','Topical','Rectal'],'Fidaxomicin route: oral.'),
('The mechanism of mupirocin is:','t-RNA synthase inhibitor',['t-RNA polymerase inhibitor','RNA polymerase inhibitor','Peptide elongation block'],'Mupirocin MOA: t-RNA synthase inhibitor.'),
('Mupirocin is used for:','MRSA nasal carrier',['MRSA pneumonia','Skin abscess','UTI'],'Mupirocin use: MRSA nasal carrier.'),
('The route of mupirocin is:','Nasal',['Oral','Topical skin','IV'],'Mupirocin route: nasal.'),
('The mechanism of fusidic acid is:','Inhibit peptide chain elongation',['Inhibit t-RNA synthase','Inhibit RNA polymerase','Inhibit cell wall'],'Fusidic acid MOA: inhibit peptide chain elongation.'),
('The route and use of fusidic acid are:','Topical for skin infection',['Oral for osteomyelitis','IV for sepsis','Nasal for carriage'],'Fusidic acid route topical, use skin infection.'),
('The mechanism of rifaximin is:','RNA polymerase inhibitor',['t-RNA synthase inhibitor','DNA gyrase inhibitor','Folate inhibitor'],'Rifaximin MOA: RNA polymerase inhibitor.'),
('Rifaximin is used for gut sterilization in:','Hepatic encephalopathy',['Renal failure','Hepatitis A','Cirrhosis without encephalopathy'],'Use: gut sterilization in hepatic encephalopathy.'),
('Rifaximin is used for which diarrhoeal illness?','Travelers diarrhea',['Cholera','Dysentery','C. difficile always'],'Use: travelers diarrhea.'),
('The off-label use of rifaximin is:','Pseudomembranous enterocolitis',['Typhoid','Giardiasis','Amoebiasis'],'Use: pseudomembranous enterocolitis (off label).'),
])
finish()

# CHAPTER 44 -----------------------------------------------------------------
start(44)
unit('Other Antibacterial Drugs: Classification and Polymyxins',
 'Other antibacterial drugs split into cell-membrane agents, anti-folate drugs and DNA gyrase inhibitors. Membrane agents are bactericidal but toxic to all cells, hence last-line; polymyxins are cationic detergents that bind membrane phospholipid and form pseudopores through which water and solutes enter (lysis), other drugs enter better, and endotoxins are bound and blocked. Polymyxin-B (Neosporin) is topical for skin infection while colistin (polymyxin E) is IV for MDR gram -ve sepsis but is potently nephrotoxic and neuromuscularly toxic.')
facts(174,[
('The three branches of "other antibacterial drugs" are:','Drugs acting on cell membrane, anti-folate drugs and DNA gyrase inhibitors',['Cell wall, folate and ribosomal drugs','Membrane, ribosomal and gyrase drugs','Folate, gyrase and cell wall drugs'],'The flowchart splits into cell membrane, anti-folate and DNA gyrase inhibitors.'),
('Drugs acting on the cell membrane are:','Bactericidal drugs',['Bacteriostatic drugs','Fungicidal drugs','Virostatic drugs'],'Cell membrane drugs: bactericidal drugs.'),
('Membrane-active drugs are kept as last-line drugs because:','They are toxic due to effect on all cells',['They are poorly absorbed','They are rapidly metabolised','They cause allergy'],'Toxic d/t effect on all cells: last-line drugs.'),
('Polymyxins are chemically:','Cationic detergents',['Anionic detergents','Sterols','Polyenes'],'Polymyxins (cationic detergents).'),
('Polymyxins bind to which membrane component?','Phospholipid in cell membrane',['Ergosterol','Peptidoglycan','Lipoteichoic acid'],'Binds to phospholipid in cell membrane.'),
('After binding membrane phospholipid, polymyxins form:','Pseudopores',['True protein channels','Ion pumps','Vesicles'],'Forms pseudopores.'),
('Through pseudopores water and solutes enter the cell causing:','Lysis',['Stasis','Sporulation','Encystation'],'Water & solutes can enter cell -> lyses.'),
('Pseudopores additionally increase:','Entry of other drugs',['Efflux of other drugs','Protein synthesis','Cell-wall thickness'],'Pseudopores increase entry of other drugs.'),
('Polymyxins also bind and block:','Endotoxins',['Exotoxins','Teichoic acids','Porins'],'Bind & block endotoxins.'),
('The polymyxin spectrum is mostly:','Gram -ve',['Gram +ve','Anaerobic','Fungal'],'Spectrum: mostly gram -ve.'),
('Polymyxin-B is also known as:','Neosporin',['Colistin','Bacitracin','Gramicidin'],'Polymyxin-B (Neosporin).'),
('The use of polymyxin-B is:','Topical treatment for skin infection',['IV for MDR sepsis','Oral for gut sterilization','Intrathecal meningitis'],'Polymyxin-B use: topical treatment for skin infection.'),
('Polymyxin E is also called:','Colistin',['Neosporin','Polymyxin M','Aerosporin'],'Polymyxin E (colistin).'),
('IV colistin is reserved for:','Multi-drug resistant gram -ve infections',['Simple UTI','Skin infection only','Gram +ve sepsis'],'I/V: multi-drug resistant gram -ve infections.'),
('Examples of MDR gram -ve organisms treated with colistin include:','Pseudomonas, Enterobacter, E. coli and Klebsiella',['Proteus and Providencia only','Acinetobacter only','Stenotrophomonas only'],'Eg: Pseudomonas, Enterobacter, E. coli, Klebsiella etc.'),
('The two side effects of colistin listed are:','Potent nephrotoxicity and neuromuscular toxicity',['Hepatotoxicity and ototoxicity','Cardiotoxicity and rash','BM suppression and colitis'],'Side effects: potent nephrotoxic drug; neuromuscular toxicity.'),
('Colistin neuromuscular toxicity is a contraindication to concurrent use of:','Aminoglycosides (shared side effects)',['Beta-lactams','Macrolides','Tetracyclines'],'Neuromuscular toxicity C/I: aminoglycoside use (shared side effects).'),
])
unit('Lipopeptides: Daptomycin',
 'Lipopeptides are large peptide molecules with poor oral adsorption and a gram +ve-only spectrum (Staphylococcus, Enterococcus). Daptomycin is IV, depolarises the cell membrane causing K+ efflux, and is DOC for VRSA and for empirical MRSA cover when vancomycin sensitivity is unknown; myopathy limits it and surfactant inactivation contraindicates it in pneumonia - vancomycin remains DOC in MRSA and linezolid in VRSA pneumonia.')
facts(174,[
('Lipopeptides are peptide drugs characterised by:','Large molecule size',['Small molecule size','Lipid solubility','Cyclic sterol core'],'Lipopeptides: peptide drugs with large molecule size.'),
('The large molecule size of lipopeptides causes:','Poor oral adsorption',['Poor IV efficacy','Rapid renal excretion','High protein binding'],'Large molecule size -> poor oral adsorption.'),
('The lipopeptide spectrum is:','Only gram +ve',['Only gram -ve','Broad including anaerobes','Only atypicals'],'Spectrum: only gram +ve.'),
('The gram +ve examples given for lipopeptides are:','Staphylococcus and Enterococcus',['Streptococcus and Listeria','Bacillus and Clostridium','Nocardia and Actinomyces'],'E.g: Staphylococcus, Enterococcus.'),
('The lipopeptide drug named on the page is:','Daptomycin',['Polymyxin B','Bacitracin','Telavancin'],'Drugs: daptomycin.'),
('The route of daptomycin is:','I/v',['Oral','Topical','IM'],'Daptomycin route: I/v.'),
])
facts(175,[
('The mechanism of daptomycin is:','Depolarization of cell membrane -> K+ efflux',['Hyperpolarization -> Na+ influx','Pore formation with Ca+ influx','Membrane sterol binding'],'MOA: depolarization of cell membrane -> K+ efflux.'),
('Daptomycin is DOC for:','VRSA',['MRSA always','VRE','VISA'],'Daptomycin DOC: VRSA.'),
('Daptomycin is used for empirical treatment of MRSA when:','Vancomycin sensitivity is unknown',['Vancomycin has failed','The patient is allergic to vancomycin','The infection is pulmonary'],'Empirical treatment of MRSA (unknown vancomycin sensitivity).'),
('The side effect of daptomycin is:','Myopathy',['Neuropathy','Nephropathy','Retinopathy'],'Side effect: myopathy.'),
('Daptomycin is contraindicated in pneumonia because:','Surfactant inactivates daptomycin',['It cannot cross the alveolar membrane','It causes bronchospasm','It is excreted in breath'],'C/I pneumonia (d/t inactivation of daptomycin by surfactant).'),
('Per the note, the DOC in MRSA is:','Vancomycin',['Daptomycin','Linezolid','Ceftaroline'],'Note: DOC in MRSA is vancomycin.'),
('Per the note, the DOC in VRSA pneumonia is:','Linezolid',['Daptomycin','Vancomycin','Tigecycline'],'Note: DOC in VRSA pneumonia: linezolid.'),
])
unit('Anti-folate Drugs: Folic Acid Synthesis and Its Blockers',
 'Bacteria build folate from pteridine + PABA via dihydro-pteroid synthase (DHPS, absent in humans) to DHPA, add glutamate to make DHFA (the human consumption form), then reduce it by DHFR (present in humans) to active tetra hydrofolate. DHPS blockers (dapsone, PAS, sulfonamides) and DHFR blockers (pyrimethamine, proguanil, methotrexate, trimethoprim) are each bacteriostatic - DHFR blockers unsafe in pregnancy for neural tube defects - but together become bactericidal.')
facts(175,[
('Bacterial folic acid synthesis starts from:','Pteridine + para-amino-benzoic acid (PABA)',['Glutamate + DHFA','THF + PABA','DHPA + pteridine'],'Pteridine + para-amino-benzoic acid (PABA).'),
('Pteridine + PABA are condensed by:','Dihydro-pteroid synthase (DHPS)',['Dihydro-folic acid reductase','Thymidylate synthase','Folylpolyglutamate synthase'],'The first enzyme is dihydro-pteroid synthase (DHPS).'),
('DHPS is notable for being:','Absent in humans',['Present in humans','Present only in gut flora of children','A human liver enzyme'],'DHPS is absent in humans.'),
('The product of the DHPS step is:','Dihydro-pteroic acid (DHPA)',['Dihydrofolic acid','Tetra hydrofolate','Para-amino benzoic acid'],'DHPS yields dihydro-pteroic acid (DHPA).'),
('DHPA combines with glutamate to form:','Dihydrofolic acid (DHFA)',['Tetra hydrofolate','Folinic acid','Methyl THF'],'DHPA + glutamate -> dihydrofolic acid (DHFA).'),
('DHFA is which form of folate for humans?','Consumption form',['Active form','Storage form','Transport form'],'DHFA: consumption form for humans.'),
('DHFA is reduced to THF by:','Dihydro-folic acid reductase (DHFR)',['DHPS','Thymidylate synthase','Methionine synthase'],'The second enzyme is dihydro-folic acid reductase (DHFR).'),
('DHFR is notable for being:','Present in humans',['Absent in humans','Bacterial only','Viral only'],'DHFR is present in humans.'),
('The active form of folate is:','Tetra hydrofolate (THF)',['DHFA','DHPA','PABA'],'Tetra hydrofolate (THF): active form.'),
('The DHPS blockers (bacteriostatic) listed are:','Dapsone, para-amino salicylic acid and sulfonamides',['Pyrimethamine and proguanil','Methotrexate and trimethoprim','Sulfonamides and trimethoprim'],'(a) DHPS blocker: dapsone, P.A.S, sulfonamides.'),
('The DHFR blockers (bacteriostatic) listed are:','Pyrimethamine, proguanil, methotrexate and trimethoprim',['Dapsone and PAS','Sulfonamides and dapsone','Trimethoprim and sulfadiazine'],'(b) DHFR blocker: pyrimethamine, proguanil, methotrexate, trimethoprim.'),
('DHFR blockers are unsafe in pregnancy because they:','Increase the risk of neural tube defects',['Cause kernicterus','Cause grey baby syndrome','Cause crystalluria'],'Unsafe in pregnancy (increased risk of neural tube defects).'),
('Combining a DHPS blocker with a DHFR blocker produces a:','Bactericidal effect',['Bacteriostatic effect','Fungicidal effect','No added effect'],'(a) + (b) -> bactericidal.'),
])
unit('Sulfonamides: Spectrum and Individual Drugs',
 'Sulfonamides are aerobic-spectrum drugs: gram +ve except Enterococcus and gram -ve except Pseudomonas and Rickettsia, which even show paradoxical overgrowth. Sulfadoxine is longest acting (malaria), sulfadiazine is TOC for toxoplasma with pyrimethamine, sulfisoxazole is the most water soluble with least crystalluria risk (otitis, UTI), and sulfasalazine - sulfonamide group plus 5-ASA - modifies rheumatoid arthritis and treats ulcerative colitis because 5-ASA stays unabsorbed in the gut.')
facts(175,[
('The sulfonamide spectrum on gram +ve organisms excludes:','Enterococcus',['Staphylococcus','Streptococcus','Listeria'],'Spectrum aerobic: gram +ve except Enterococcus.'),
('The sulfonamide gram -ve coverage excludes:','Pseudomonas and Rickettsia',['E. coli and Klebsiella','Proteus and Providencia','Salmonella and Shigella'],'Gram -ve except Pseudomonas & Rickettsia.'),
('Pseudomonas and Rickettsia exposed to sulfonamides show:','Paradoxical overgrowth',['Paradoxical killing','No change','Resistance by efflux'],'They cause paradoxical overgrowth.'),
('The longest acting sulfonamide is:','Sulfadoxine',['Sulfadiazine','Sulfisoxazole','Sulfasalazine'],'Sulfadoxine (longest acting).'),
('The use of sulfadoxine is:','Malaria',['UTI','Otitis','Toxoplasma'],'Sulfadoxine use: malaria.'),
('The treatment of choice for toxoplasma (with pyrimethamine) is:','Sulfadiazine',['Sulfadoxine','Sulfisoxazole','Sulfacetamide'],'Sulfadiazine use: TOC for toxoplasma (with pyrimethamine).'),
('The most water soluble sulfonamide is:','Sulfisoxazole',['Sulfadiazine','Sulfadoxine','Sulfasalazine'],'Sulfisoxazole (most water soluble).'),
('Sulfisoxazole carries the least risk of:','Crystalluria',['Hemolysis','Kernicterus','Porphyria'],'Least risk for crystalluria.'),
('Sulfisoxazole is used in otitis and UTI because of:','Increased concentration in urine',['Increased biliary excretion','High plasma protein binding','Long half-life'],'Uses: otitis; UTI (d/t increased concentration in urine).'),
])
facts(176,[
('Sulfasalazine is made of:','Sulfonamide group and 5-amino salicylic acid (5-ASA)',['Sulfonamide group and methotrexate','5-ASA and mesalamine','Sulfapyridine and PABA'],'Made of: sulfonamide group; 5-amino salicylic acid (5-ASA).'),
('Sulfasalazine helps rheumatoid arthritis through the:','Disease modifying effect of sulfonamides',['Analgesic effect of 5-ASA','Antibacterial effect in gut','Steroid-like effect'],'Rheumatoid arthritis (disease modifying effect of sulfonamides).'),
('Sulfasalazine works in ulcerative colitis because:','5-ASA remains unabsorbed in intestine',['The sulfonamide kills gut flora','It blocks TNF','It coats the mucosa'],'Ulcerative colitis (5-ASA remains unabsorbed in intestine).'),
])
unit('Cotrimoxazole, Anti-folate Notes and Topical Anti-folates',
 'Cotrimoxazole pairs sulfamethoxazole with trimethoprim (bactericidal): tablet ratio 5:1 but blood ratio 20:1 because trimethoprim has a larger volume of distribution, and trimethoprim is 20x more potent. It is DOC in cystitis and for cyclospora, Burkholderia cepacia, pneumocystis, isospora, nocardia and sarcocyst. Mesalamine is DOC for ulcerative colitis and spiramycin for toxoplasma in pregnancy; topically, sulfadiazine ointment (burns, fungal keratomycosis), mafenide (burns, painful, metabolic acidosis via carbonic anhydrase block) and sulfacetamide drops (trachoma, conjunctivitis) are used.')
facts(176,[
('Cotrimoxazole combines:','Sulfamethoxazole + trimethoprim',['Sulfadiazine + trimethoprim','Sulfamethoxazole + pyrimethamine','Sulfadoxine + pyrimethamine'],'Cotrimoxazole: sulfamethoxazole + trimethoprim.'),
('The cotrimoxazole combination is:','Bactericidal',['Bacteriostatic','Fungistatic','Inactive'],'Sulfamethoxazole + trimethoprim: bactericidal.'),
('The sulfamethoxazole:trimethoprim ratio in the tablet is:','5 : 1',['1 : 5','20 : 1','1 : 20'],'Ratio in tablet: 5:1.'),
('The ratio in blood becomes 20:1 because:','Trimethoprim has an increased volume of distribution',['Sulfamethoxazole is protein bound','Trimethoprim is renally excreted','Sulfamethoxazole is metabolised faster'],'In blood 20:1 (trimethoprim has increased volume of distribution).'),
('The potency of trimethoprim relative to sulfamethoxazole is:','20x',['5x','10x','50x'],'Potency of trimethoprim: 20x potency of sulfamethoxazole.'),
('Cotrimoxazole is DOC in:','Cystitis',['Pyelonephritis','Prostatitis','Urethral stricture infection'],'Uses: DOC in cystitis.'),
('Cotrimoxazole is DOC for infections by cyclospora, Burkholderia cepacia and:','Pneumocystis, isospora, nocardia and sarcocyst',['Toxoplasma and cryptosporidium','Listeria and nocardia','Histoplasma and coccidioides'],'Infection by: cyclospora, Burkholderia cepacia, pneumocystis, isospora, nocardia, sarcocyst.'),
('Per the note, the DOC for ulcerative colitis is:','Mesalamine',['Sulfasalazine','Balsalazide','Olsalazine'],'Note: mesalamine - DOC for ulcerative colitis.'),
('Per the note, the DOC for toxoplasma in pregnancy is:','Spiramycin',['Sulfadiazine + pyrimethamine','Clindamycin','Atovaquone'],'Spiramycin, DOC for toxoplasma: in pregnancy.'),
('Sulfadiazine ointment is DOC in:','Burn patients',['Diabetic foot','Pressure sores','Eczema'],'Sulfadiazine ointment: DOC in burn patients.'),
('Sulfadiazine ointment is also used for:','Fungal keratomycosis',['Bacterial conjunctivitis','Trachoma','Viral keratitis'],'Sulfadiazine ointment: fungal keratomycosis.'),
('Mafenide is used in:','Burn patients',['Eye infections','UTI','Otitis'],'Mafenide uses: burn patients.'),
('The side effects of mafenide are:','Severe pain on application and increased risk of metabolic acidosis',['Crystalluria and hematuria','Kernicterus','Hypersensitivity rash'],'Mafenide: severe pain on application; increased risk of metabolic acidosis.'),
('Mafenide causes metabolic acidosis by:','Carbonic anhydrase block',['Renal tubular damage','Diarrhoea','Hypoventilation'],'Metabolic acidosis (d/t carbonic anhydrase block).'),
('Sulfacetamide eye drops are used for:','Trachoma and conjunctivitis',['Keratomycosis','Glaucoma','Dry eye'],'Sulfacetamide eye drops: trachoma; conjunctivitis.'),
])
unit('Sulfonamide Side Effects',
 'Sulfonamides given near delivery displace bilirubin from albumin (increased plasma protein binding of the sulfonamide), raising blood bilirubin that crosses the blood-brain barrier and causes kernicterus after birth. They also precipitate acute intermittent porphyria, methemoglobinemia with cyanosis refractory to O2, hypersensitivity rash and bone-marrow suppression across the whole sulfonamide group, and crystalluria with renal stones unless water intake is raised.')
facts(176,[
('Kernicterus after birth occurs if sulfonamides are given to:','The pregnant mother',['The neonate directly','The breastfeeding father','A child with G6PD only'],'Kernicterus after birth (if given to pregnant mother).'),
('The first step in sulfonamide kernicterus pathology is:','Increased plasma protein binding of sulfonamides displacing bilirubin from albumin',['Direct bilirubin overproduction','Hepatic conjugation failure','Biliary obstruction'],'Pathology: increased plasma protein binding of sulfonamides -> displacement of bilirubin from albumin.'),
('Displaced bilirubin then causes:','Increased bilirubin in blood that crosses the blood-brain barrier',['Increased urinary bilirubin','Jaundice-free encephalopathy','Conjugated hyperbilirubinemia'],'Displacement -> increased bilirubin in blood -> crosses blood-brain barrier.'),
('Sulfonamides can precipitate which porphyria?','Acute intermittent porphyria',['Porphyria cutanea tarda','Variegate porphyria','Erythropoietic porphyria'],'Side effect: acute intermittent porphyria.'),
])
facts(177,[
('Sulfonamide-induced methemoglobinemia presents as:','Cyanosis refractory to O2 inhalation',['Cyanosis responsive to O2','Pallor with tachypnoea','Clubbing'],'Methemoglobinemia: cyanosis refractory to O2 inhalation.'),
('Rash and bone marrow suppression with sulfonamides represent:','Hypersensitivity seen in all sulfonamide group-containing drugs',['Dose-dependent toxicity','Idiosyncrasy only in children','A G6PD-related effect'],'Hypersensitivity (seen in all sulfonamide group-containing drugs).'),
('Sulfonamide crystalluria can cause:','Renal stones (increased water intake advised)',['Uric acid stones','Calcium stones regardless of intake','Bladder cancer'],'Crystalluria: can cause renal stones (increased water intake advised).'),
])
unit('DNA Gyrase Inhibitors: Quinolones and Fluoroquinolone MOA',
 'DNA gyrase inhibitors are bactericidal. Nalidixic acid blocks DNA gyrase of gram -ve organisms and, concentrating in urine and stool, treats UTI and traveller\'s diarrhea. Adding fluorine gives fluoroquinolones: DNA gyrase inhibition supplies gram -ve coverage and topoisomerase IV inhibition adds gram +ve coverage. Norfloxacin is least active with poor tissue concentration (same uses as nalidixic acid) while ciprofloxacin is most active and concentrates in urine and stool.')
facts(177,[
('DNA gyrase inhibitors are:','Bactericidal drugs',['Bacteriostatic drugs','Fungicidal drugs','Virostatic drugs'],'DNA gyrase inhibitors: bactericidal drugs.'),
('The quinolone drug named on the page is:','Nalidixic acid',['Ciprofloxacin','Moxifloxacin','Levofloxacin'],'Quinolones drug: nalidixic acid.'),
('The MOA of nalidixic acid is:','Blocks DNA gyrase',['Blocks topoisomerase IV','Blocks RNA polymerase','Blocks folate synthesis'],'MOA: blocks DNA gyrase.'),
('The spectrum of nalidixic acid is:','Gram -ve organisms',['Gram +ve organisms','Anaerobes','Atypicals'],'Spectrum: gram -ve organisms.'),
('Nalidixic acid is useful because of increased concentration of drug in:','Urine and stool',['Sputum and CSF','Bile and saliva','Bone and prostate'],'Use: d/t increased concentration of drug in urine & stool.'),
('The uses of nalidixic acid are:','UTI and traveller\'s diarrhea',['Meningitis and endocarditis','Pneumonia and otitis','Skin and bone infection'],'Uses: UTI; traveller\'s diarrhea.'),
('Fluoroquinolones are chemically:','Fluorine + quinolone',['Chlorine + quinolone','Fluorine + coumarin','Sulfur + quinolone'],'Fluoroquinolones: fluorine + quinolone.'),
('The gram -ve coverage of fluoroquinolones comes from inhibition of:','DNA gyrase',['Topoisomerase IV','RNA polymerase','Helicase'],'Inhibit DNA gyrase: gram -ve coverage.'),
('The gram +ve coverage of fluoroquinolones comes from inhibition of:','Topoisomerase IV',['DNA gyrase','Primase','Ligase'],'Inhibit topoisomerase IV: some gram +ve coverage.'),
('The least active fluoroquinolone is:','Norfloxacin',['Ciprofloxacin','Levofloxacin','Moxifloxacin'],'Norfloxacin (least active).'),
('Norfloxacin is limited by:','Poor tissue concentration',['Poor urine concentration','Rapid hepatic metabolism','High protein binding'],'Norfloxacin: poor tissue concentration.'),
('The use of norfloxacin is:','Same as nalidixic acid',['Same as moxifloxacin','Systemic sepsis','CAP'],'Norfloxacin use: same as nalidixic acid.'),
('The most active fluoroquinolone is:','Ciprofloxacin',['Norfloxacin','Levofloxacin','Pefloxacin'],'Ciprofloxacin (most active).'),
('Ciprofloxacin shows increased concentration in:','Urine and stool',['CSF and vitreous','Bile only','Bone only'],'Ciprofloxacin: increased concentration in urine & stool.'),
])
unit('Ciprofloxacin DOC List, Organism-specific Fluoroquinolones and CAP Treatment',
 'Ciprofloxacin is DOC for pyelonephritis, traveller\'s diarrhoea, typhoid carrier, shigella and contacts of meningococcal meningitis, and for penicillin-G-resistant anthrax in bioterrorism. Pseudomonas prefers ciprofloxacin over levofloxacin, some fluoroquinolones cover mycobacterium, and the respiratory fluoroquinolones (moxifloxacin, gemifloxacin, levofloxacin) treat CAP. First-line CAP is amoxicillin (ceftriaxone alternative) plus azithromycin for atypicals; if unresponsive choose a respiratory fluoroquinolone (cheaper), omadacycline (expensive) or lefamulin; delafloxacin and ozenoxacin are newer skin-infection fluoroquinolones.')
facts(177,[
('Ciprofloxacin is DOC in which upper urinary infection?','Pyelonephritis',['Cystitis','Prostatitis','Perinephric abscess'],'Ciprofloxacin DOC in pyelonephritis.'),
('Ciprofloxacin is DOC for which travellers\' illness?','Traveller\'s diarrhoea',['Traveller\'s malaria','Typhoid fever treatment','Hepatitis A'],'DOC in traveller\'s diarrhoea.'),
('The typhoid carrier state is treated with DOC:','Ciprofloxacin',['Azithromycin','Ceftriaxone','Chloramphenicol'],'DOC in typhoid carrier.'),
('Ciprofloxacin is DOC for which invasive diarrhoeal organism?','Shigella',['Salmonella enteritidis','Campylobacter','Vibrio'],'DOC in shigella.'),
('Contacts of meningococcal meningitis are protected with DOC:','Ciprofloxacin',['Rifampicin always','Ceftriaxone always','Azithromycin'],'DOC in contacts of meningococcal meningitis.'),
('Ciprofloxacin is used in anthrax when:','Penicillin G is resistant (bioterrorism)',['Penicillin G is sensitive','The patient is a child','Doxycycline fails'],'Anthrax (if penicillin G resistant): bioterrorism.'),
('For pseudomonas the fluoroquinolone order given is:','Ciprofloxacin > levofloxacin',['Levofloxacin > ciprofloxacin','Moxifloxacin > ciprofloxacin','Norfloxacin > ciprofloxacin'],'Pseudomonas: ciprofloxacin > levofloxacin.'),
('Mycobacterium is covered by:','Some fluoroquinolones',['No fluoroquinolone','All quinolones including nalidixic acid','Only norfloxacin'],'Mycobacterium: some fluoroquinolones.'),
('The respiratory fluoroquinolones listed are:','Moxifloxacin, gemifloxacin and levofloxacin',['Ciprofloxacin and norfloxacin','Pefloxacin and ofloxacin','Delafloxacin and ozenoxacin'],'Respiratory fluoroquinolones: moxifloxacin, gemifloxacin, levofloxacin.'),
('Respiratory fluoroquinolones are used for:','Community acquired pneumonia (CAP)',['Hospital-acquired pneumonia','Aspiration pneumonia','Lung abscess'],'Use: community acquired pneumonia (CAP).'),
])
facts(178,[
('First-line CAP treatment combines amoxicillin with:','Azithromycin',['Clarithromycin','Doxycycline','Cotrimoxazole'],'Treatment of CAP: amoxicillin + azithromycin.'),
('The alternative to amoxicillin in first-line CAP is:','Ceftriaxone',['Cefixime','Cephalexin','Cefepime'],'Alternative: ceftriaxone.'),
('Azithromycin in the CAP regimen provides:','Atypical bacteria coverage',['Gram -ve coverage','Anaerobic coverage','Antiviral coverage'],'Azithromycin (atypical bacteria coverage).'),
('If first-line CAP therapy is unresponsive, the cheaper option is:','A respiratory fluoroquinolone',['Omadacycline','Lefamulin','Cotrimoxazole'],'If unresponsive: respiratory fluoroquinolone (cheaper option).'),
('The expensive option for unresponsive CAP is:','Omadacycline',['Respiratory fluoroquinolone','Lefamulin','Doxycycline'],'Option 2: omadacycline (expensive).'),
('The pleuromutilin option for unresponsive CAP is:','Lefamulin',['Retapamulin','Omadacycline','Moxifloxacin'],'Option 3: lefamulin (pleuromutilin).'),
('The newer fluoroquinolones used for skin infections are:','Delafloxacin and ozenoxacin',['Moxifloxacin and gemifloxacin','Levofloxacin and pefloxacin','Ciprofloxacin and norfloxacin'],'Newer fluoroquinolones: delafloxacin, ozenoxacin - skin infections.'),
])
unit('Fluoroquinolone Side Effects, Contraindications and Activity Comparisons',
 'The PQRST mnemonic lists peripheral neuropathy, QT prolongation/torsades, rash (photosensitivity), seizure (GABA antagonism) and tendinitis - most often Achilles, with rupture risk in transplant patients, the elderly, steroid users and renal failure but not in vitamin D deficiency. Fluoroquinolones are contraindicated in pregnancy and children (cartilage growth blockage), with other QT-prolonging drugs such as macrolides, and with GABA inhibitors or epilepsy. Moxifloxacin has the maximum half-life, seizure risk, QT prolongation, dysglycemia and anti-mycobacterial activity but hepatic excretion (unsafe in liver failure, useless in UTI); levofloxacin has maximum oral bioavailability, gemifloxacin maximum protein binding and pefloxacin maximum photosensitivity.')
facts(178,[
('The fluoroquinolone side-effect mnemonic is:','PQRST',['QRST','ABCDE','SNAP'],'Mnemonic: PQRST.'),
('In PQRST the P stands for:','Peripheral neuropathy',['Photosensitivity','Pancreatitis','Pseudomembranous colitis'],'P: peripheral neuropathy.'),
('In PQRST the Q stands for:','QT prolongation / torsades de pointes',['Quinolone allergy','Quadriceps weakness','Quiet thyroid'],'Q: QT prolongation / torsades de pointes.'),
('In PQRST the R stands for:','Rash (photosensitivity)',['Renal failure','Retinopathy','Rhabdomyolysis'],'R: rash (photo sensitivity).'),
('In PQRST the S stands for:','Seizure (GABA antagonism)',['Stevens-Johnson syndrome','Syncope','Serotonin syndrome'],'S: seizure (GABA antagonism).'),
('In PQRST the T stands for:','Tendinitis (m/c Achilles tendon)',['Tinnitus','Thyroiditis','Tetany'],'T: tendinitis (m/c Achilles tendon).'),
('The risk factors for fluoroquinolone tendon rupture listed are:','Transplant patient, elderly, steroid use and renal failure',['Diabetes and hypertension','Hypothyroidism','Vitamin D deficiency'],'Increased risk of tendon rupture in transplant patient, elderly, steroid use, renal failure.'),
('Which deficiency does NOT increase fluoroquinolone tendon rupture risk?','Vitamin D deficiency',['None - all deficiencies increase risk','Calcium deficiency','Magnesium deficiency'],'Vit D deficiency does not increase risk of tendon rupture.'),
('Fluoroquinolones are contraindicated in pregnancy and children due to:','Blockage of cartilage growth',['Kernicterus','Neural tube defects','Teeth discolouration'],'Pregnancy and children: d/t blockage of cartilage growth.'),
('Fluoroquinolones should not be combined with:','Other drugs causing QT prolongation, e.g. macrolides',['Beta-lactams','Aminoglycosides in all cases','Penicillins'],'C/I with other drugs causing QT prolongation, e.g. macrolides.'),
('Fluoroquinolones are contraindicated with GABA inhibitors or epilepsy because of:','Increased risk of seizure',['Decreased absorption','QT shortening','Tendon protection'],'With GABA inhibitors / epilepsy (increased risk of seizure).'),
('Moxifloxacin has the maximum:','Half-life among current fluoroquinolones',['Oral bioavailability','Plasma protein binding','Photosensitivity'],'Moxifloxacin maximum T1/2 among current fluoroquinolones.'),
('Moxifloxacin carries maximum risk of:','Seizure, QT prolongation and dysglycemia',['Tendon rupture only','Crystalluria','Hemolysis'],'Moxifloxacin maximum: risk of seizure, QT prolongation, dysglycemia.'),
('Moxifloxacin has maximum activity against:','Mycobacteria',['Pseudomonas','Enterococcus','Anaerobes in gut'],'Moxifloxacin maximum activity against mycobacteria.'),
('Moxifloxacin is excreted:','Hepatically (safe in renal failure / unsafe in liver failure)',['Renally (safe in liver failure)','Equally by both routes','In bile only without metabolism'],'Hepatic excretion (safe in renal failure/unsafe in liver failure).'),
('Moxifloxacin must not be used in UTI because:','The drug is not present in urine',['It is inactivated by urine pH','It crystallises in urine','It causes hemorrhagic cystitis'],'Not to be used in UTI (drug not present in urine).'),
('Maximum oral bioavailability among fluoroquinolones is with:','Levofloxacin',['Moxifloxacin','Gemifloxacin','Pefloxacin'],'Levofloxacin: maximum oral bioavailability.'),
('Maximum plasma protein binding among fluoroquinolones is with:','Gemifloxacin',['Levofloxacin','Moxifloxacin','Pefloxacin'],'Gemifloxacin: maximum plasma protein binding.'),
('Maximum photosensitivity among fluoroquinolones is with:','Pefloxacin',['Levofloxacin','Gemifloxacin','Moxifloxacin'],'Pefloxacin: maximum photosensitivity.'),
])
unit('Urinary Antiseptic Agents',
 'Urinary antiseptics are drugs that concentrate in urine: fosfomycin/fosfidomycin, nalidixic acid, norfloxacin, nitrofurantoin, trimethoprim and methenamine. Nitrofurantoin (free-radical production) is a first-line UTI treatment but hemolyses in G-6-PD deficiency; trimethoprim (DHFR inhibitor, bacteriostatic) treats UTI, blocks ENaC causing hyperkalemia and is contraindicated in pregnancy. Methenamine, formulated with hippuric and mandelic acids excreted unchanged, needs acidic urine - helped by vitamin C or ammonium chloride - to release ammonia and antibacterial formaldehyde, so it only prophylaxes UTI and is contraindicated in liver failure (encephalopathy) and renal failure (acid toxicity).')
facts(179,[
('Urinary antiseptic agents are defined as drugs with:','Increased concentration in urine',['Increased concentration in blood','Increased biliary excretion','Increased tissue penetration'],'Drugs with increased concentration in urine.'),
('The urinary antiseptic list begins with:','Fosfomycin / fosfidomycin, nalidixic acid and norfloxacin',['Nitrofurantoin, trimethoprim and methenamine','Cotrimoxazole and ciprofloxacin','Methenamine and hippuric acid'],'List: fosfomycin/fosfidomycin, nalidixic acid, norfloxacin, then others.'),
('The MOA of nitrofurantoin is:','Free radical production',['DHFR inhibition','DNA gyrase inhibition','Cell wall inhibition'],'Nitrofurantoin MOA: free radical production.'),
('Nitrofurantoin is used as:','Treatment of UTI (first line drug)',['Prophylaxis of UTI only','Treatment of pyelonephritis','Treatment of prostatitis'],'Use: treatment of UTI (first line drug).'),
('The side effect of nitrofurantoin in G-6-PD deficiency is:','Hemolysis',['Methemoglobinemia','Crystalluria','Peripheral neuropathy'],'Side effects: hemolysis in G-6-PD deficiency.'),
('The MOA of trimethoprim is:','DHFR inhibitor (bacteriostatic)',['DHPS inhibitor','ENaC activator','Folate conjugase inhibitor'],'Trimethoprim MOA: DHFR inhibitor (bacteriostatic).'),
('Trimethoprim is used for:','Treatment of UTI',['Prophylaxis of UTI only','Pneumocystis pneumonia only','Typhoid'],'Trimethoprim use: treatment of UTI.'),
('Trimethoprim causes hyperkalemia by:','Inhibiting ENaC (epithelial sodium channels)',['Blocking aldosterone synthesis','Damaging glomeruli','Causing acidosis'],'Side effect: inhibits ENaC -> hyperkalemia.'),
('Trimethoprim is contraindicated in pregnancy because of:','Neural tube defects in the fetus',['Kernicterus','Cardiac defects','Limb defects'],'C/I pregnancy (d/t neural tube defects in fetus).'),
('Methenamine is formulated with:','Hippuric and mandelic acid',['Ascorbic and citric acid','Benzoic and salicylic acid','Acetic and lactic acid'],'Formulated with hippuric & mandelic acid.'),
('The hippuric and mandelic acids of methenamine are excreted in urine:','Unchanged',['As conjugates','After hepatic metabolism','As ammonia only'],'Excreted in urine unchanged.'),
('Methenamine requires which urine pH to work?','Acidic pH',['Alkaline pH','Neutral pH','Any pH'],'Acidic pH of urine is required.'),
('The urine acidifying agents listed to lower pH further are:','Vitamin C and ammonium chloride',['Sodium bicarbonate','Acetazolamide','Potassium citrate'],'To decrease pH more: urine acidifying agents - vit. C, ammonium chloride.'),
('In acidic urine methenamine releases:','Ammonia and formaldehyde (antibacterial)',['Ammonia only','Formaldehyde and acetaldehyde','Nitrite and ammonia'],'Methenamine -> ammonia + formaldehyde (antibacterial).'),
('The use of methenamine is:','Prophylaxis of UTI (not used for treatment)',['Treatment of acute UTI','Treatment of pyelonephritis','Gut sterilization'],'Use: prophylaxis of UTI (not used for treatment).'),
('Methenamine is contraindicated in liver failure because of:','Increased risk of encephalopathy',['Increased ammonia excretion','Hepatorenal syndrome','Coagulopathy'],'C/I liver failure (increased risk of encephalopathy).'),
('Methenamine is contraindicated in renal failure because of:','Hippuric and mandelic acid toxicity',['Formaldehyde nephrotoxicity','Crystalluria','Hyperkalemia'],'C/I renal failure (hippuric & mandelic acid toxicity).'),
])
finish()

# CHAPTER 45 -----------------------------------------------------------------
start(45)
unit('Fungal Microbiology and Target-based Classification',
 'The fungal cell diagram runs squalene (cytoplasm) -> squalene epoxidase (terbinafine block) -> squalene epoxide -> lanosterol -> 14-alpha-sterol demethylase (azole block) -> ergosterol, with flucytosine on nuclear DNA and griseofulvin on microtubules. The wall - proteins, chitins and beta glucans - needs beta glucan synthase, blocked by echinocandins and ibrexafungerp, while amphotericin B sequesters ergosterol from the cell membrane. Target-wise: sequestration (amphotericin B), synthesis block (terbinafine, azoles), wall beta-glucan synthase block (echinocandins, ibrexafungerp), microtubules (griseofulvin) and DNA (flucytosine).')
facts(180,[
('In the fungal cell diagram squalene sits in the:','Cytoplasm',['Cell wall','Cell membrane','Nucleus'],'Squalene (in cytoplasm).'),
('Squalene is converted to squalene epoxide by:','Squalene epoxidase',['Squalene synthase','Lanosterol synthase','14-alpha-sterol demethylase'],'Squalene -> squalene epoxidase -> squalene epoxide.'),
('Squalene epoxidase is blocked by:','Terbinafine',['Azoles','Amphotericin B','Echinocandins'],'Terbinafine blocks squalene epoxidase.'),
('Lanosterol is converted towards ergosterol by:','14-alpha-sterol demethylase',['Squalene epoxidase','Ergosterol synthase','Chitin synthase'],'Lanosterol -> 14-alpha-sterol demethylase -> ergosterol.'),
('14-alpha-sterol demethylase is blocked by:','Azoles',['Terbinafine','Griseofulvin','Flucytosine'],'Azoles block 14-alpha-sterol demethylase.'),
('The drug shown blocking fungal nuclear DNA is:','Flucytosine',['Griseofulvin','Azoles','Echinocandins'],'Flucytosine blocks DNA in the nucleus.'),
('The drug shown targeting fungal microtubules is:','Griseofulvin',['Flucytosine','Terbinafine','Amphotericin B'],'Griseofulvin blocks microtubules.'),
('Beta glucan synthase is required for synthesis of:','Beta glucans',['Chitins','Proteins','Ergosterol'],'Beta glucan synthase is for synthesis of beta glucans.'),
('Beta glucan synthase is blocked by:','Echinocandins class and ibrexafungerp',['Azoles','Polyenes','Allylamines'],'Echinocandins class and ibrexafungerp block beta glucan synthase.'),
('The fungal cell wall is made of:','Proteins, chitins and beta glucans',['Ergosterol and chitin only','Cellulose and pectin','Peptidoglycan and teichoic acid'],'Cell wall made of: proteins, chitins, beta glucans.'),
('Amphotericin B acts on the:','Cell membrane',['Cell wall','Microtubules','Nucleus'],'Cell membrane: acts on - amphotericin B.'),
('The MOA of amphotericin B is:','Sequestration of ergosterol from the cell membrane',['Blocking ergosterol synthesis','Blocking beta glucan synthase','Binding chitin'],'MOA: sequestration of ergosterol from CM.'),
('In the target-based classification, ergosterol sequestration is done by:','Amphotericin B',['Terbinafine','Azoles','Echinocandins'],'Ergosterol: sequestration - amphotericin B.'),
('Ergosterol synthesis is blocked by:','Terbinafine and azoles',['Amphotericin B','Echinocandins','Griseofulvin'],'Ergosterol: block synthesis - terbinafine, azoles.'),
('Cell-wall beta-glucan synthase is blocked by:','Echinocandins and ibrexafungerp',['Amphotericin B','Azoles','Flucytosine'],'Cell wall: block beta-glucan synthase - echinocandins, ibrexafungerp.'),
('In the target-based tree, microtubules are targeted by:','Griseofulvin',['Flucytosine','Terbinafine','Ibrexafungerp'],'Microtubules: griseofulvin.'),
('In the target-based tree, fungal DNA is targeted by:','Flucytosine',['Griseofulvin','Azoles','Polyenes'],'DNA: flucytosine.'),
])
unit('Amphotericin B',
 'Amphotericin B is given IV with a 5% dextrose carrier and is DOC for systemic fungal infections, kala azar, mucormycosis and cryptococcal meningitis. Its infusion reaction - the "shake & bake" of fever and chills - is treated with pethidine; nephrotoxicity is prevented by preloading 1-2 L of NaCl or by liposomal Am-B (LAmB); hypokalemia (~1/3 of patients, treated with KCl), hypomagnesemia and hypotension complete the picture. The TOC for cryptococcal meningitis is IV amphotericin B plus IV flucytosine, with fluconazole as alternative.')
facts(181,[
('The route of amphotericin B is:','IV with carrier (5% dextrose)',['Oral','IM','IV in normal saline only'],'Route: IV with carrier (5% dextrose).'),
('Amphotericin B is DOC in which broad category?','Systemic fungal infections',['Superficial dermatophytosis','Oral candidiasis only','Fungal keratitis'],'Uses: DOC in systemic fungal infections.'),
('Among fungal-parasitic overlaps, amphotericin B is DOC in:','Kala azar',['Mucormycosis','Sporotrichosis','Histoplasmosis'],'DOC in kala azar.'),
('Amphotericin B is DOC in which zygomycete (mucor) infection?','Mucormycosis',['Aspergillosis','Candidiasis','Blastomycosis'],'DOC in mucormycosis.'),
('Amphotericin B is DOC in which fungal meningitis?','Cryptococcal meningitis',['Coccidioidal meningitis','Bacterial meningitis','TB meningitis'],'DOC in cryptococcal meningitis.'),
('The amphotericin B infusion reaction is nicknamed:','Shake & bake reaction',['Red-man syndrome','Cheese reaction','Flushing syndrome'],'Infusion reaction: shake & bake reaction.'),
('The shake & bake infusion reaction consists of:','Fever + chills',['Rigors with hypotension only','Rash and wheeze','Headache and vomiting'],'Fever + chills.'),
('The infusion reaction of amphotericin B is treated with:','Pethidine',['Paracetamol always','Hydrocortisone','Adrenaline'],'Treated with pethidine.'),
('Nephrotoxicity of amphotericin B is prevented by preloading with:','1-2 L of NaCl (nephroprotective)',['1-2 L of dextrose','Mannitol','Furosemide'],'Preload 1-2 L of NaCl (nephroprotective).'),
('The formulation that reduces amphotericin B nephrotoxicity is:','Liposomal Am-B (LAmB)',['Lipid emulsion','Albumin-bound form','Nebulised form'],'Combine with liposomes -> liposomal Am-B (LAmB).'),
('The incidence of amphotericin B hypokalemia is about:','1/3rd of patients',['1/10th of patients','Half of patients','Nearly all patients'],'Hypokalemia incidence: ~1/3rd patients.'),
('Amphotericin B hypokalemia is treated with:','KCl',['NaCl','Calcium gluconate','Magnesium only'],'Treatment: KCl.'),
('The other electrolyte and vascular side effects of amphotericin B are:','Hypomagnesemia and hypotension',['Hyperkalemia and hypertension','Hyponatremia and bradycardia','Hypercalcemia and tachycardia'],'Hypomagnesemia; hypotension.'),
('The TOC of cryptococcal meningitis is:','IV amphotericin B + IV flucytosine',['IV fluconazole alone','Oral itraconazole','IV voriconazole'],'TOC of cryptococcal meningitis: IV amphotericin B + IV flucytosine.'),
('The alternative drug for cryptococcal meningitis is:','Fluconazole',['Itraconazole','Voriconazole','Posaconazole'],'Alternative: fluconazole.'),
])
unit('Terbinafine and Azoles: Fluconazole and Itraconazole',
 'Terbinafine (topical or oral) concentrates in hair, skin and nails, treating dermatophytes and standing as DOC for onychomycosis. Fluconazole is DOC for coccidioidal meningitis and for mucocutaneous Candida albicans (vaginal, esophagitis) but not oral candidiasis, where clotrimazole lozenges win. Itraconazole, a ketoconazole derivative, is DOC for dermatophytes (the Itomed ointment pairs terbinafine with itraconazole), endemic mycoses and sporotrichosis, and serves in ABPA as a steroid-sparing agent.')
facts(181,[
('The routes of terbinafine are:','Topical and oral',['IV only','Topical only','Oral only'],'Terbinafine route: topical, oral.'),
('Terbinafine works well on dermatophytes because of:','Good concentration in hair, skin and nails',['Good CSF penetration','Renal excretion','Biliary concentration'],'Dermatophytes (d/t good concentration in hair, skin, nails etc).'),
('Terbinafine is DOC for:','Onychomycosis',['Tinea versicolor','Oral candidiasis','Fungal keratitis'],'DOC for onychomycosis.'),
('Fluconazole is DOC in which meningitis?','Coccidioidal meningitis',['Cryptococcal meningitis','Bacterial meningitis','TB meningitis'],'Fluconazole DOC in coccidioidal meningitis.'),
('Fluconazole is DOC for Candida albicans limited to:','Mucocutaneous sites (e.g. vaginal, esophagitis)',['Systemic candidiasis','Candida endocarditis','Candida meningitis'],'Candida albicans (only mucocutaneous, e.g. vaginal, esophagitis).'),
('The exception where fluconazole is NOT DOC for candidiasis is oral candidiasis, whose DOC is:','Clotrimazole lozenges',['Nystatin swish','Oral fluconazole','IV echinocandin'],'Exception: oral candidiasis (DOC: clotrimazole lozenges).'),
('Itraconazole is a derivative of:','Ketoconazole',['Fluconazole','Voriconazole','Posaconazole'],'Itraconazole (derivative of ketoconazole).'),
('Itraconazole is DOC in dermatophytes; the TOC branded ointment combines:','Topical terbinafine + itraconazole (Itomed)',['Topical clotrimazole + ketoconazole','Oral griseofulvin alone','Topical nystatin'],'Dermatophytes (TOC: Itomed -> topical ointment of terbinafine + itraconazole).'),
('Itraconazole is DOC in which deep mycoses group?','Endemic mycoses',['Mucormycosis','Candidiasis','Cryptococcosis'],'DOC in endemic mycoses.'),
('Itraconazole is DOC in which lymphocutaneous mycosis?','Sporotrichosis',['Chromoblastomycosis','Mycetoma','Paracoccidioidomycosis'],'DOC in sporotrichosis.'),
])
facts(182,[
('In allergic bronchopulmonary aspergillosis (ABPA) the DOC is steroids, and itraconazole is added as a:','Steroid-sparing agent (lower steroid dose required)',['Primary therapy','Rescue therapy','Prophylaxis'],'ABPA (DOC: steroids) - as a steroid-sparing agent (decreased dose of steroid required).'),
])
unit('Ketoconazole, Voriconazole, Posaconazole and Isavuconazole',
 'Ketoconazole use has fallen in preference to itraconazole; it causes gynecomastia and impotence in males, menstrual irregularities in females and blocks steroid synthesis - hence the secondary use in Cushing syndrome. Voriconazole is DOC in invasive aspergillosis but disturbs vision. Posaconazole and isavuconazole share invasive aspergillosis (when voriconazole is contraindicated) and mucormycosis, and specifically prevent fungal infection in graft vs host disease.')
facts(182,[
('Ketoconazole use has decreased in preference to:','Itraconazole',['Fluconazole','Voriconazole','Posaconazole'],'Ketoconazole: use of drug decreased in preference to itraconazole.'),
('The side effects of ketoconazole in males are:','Gynecomastia and impotence',['Galactorrhoea only','Hirsutism','Precocious puberty'],'In males: gynecomastia, impotence.'),
('The side effect of ketoconazole in females is:','Menstrual irregularities',['Amenorrhoea only','Hirsutism','Infertility only'],'In females: menstrual irregularities.'),
('Ketoconazole blocks steroid synthesis, giving the secondary use in:','Cushing syndrome',['Addison disease','Congenital adrenal hyperplasia','Pheochromocytoma'],'Block steroid synthesis (secondary use: Cushing syndrome).'),
('Voriconazole is DOC in:','Invasive aspergillosis',['Mucormycosis','Candidiasis','Cryptococcosis'],'Voriconazole: DOC in invasive aspergillosis.'),
('The side effect of voriconazole is:','Visual problems',['Hearing loss','Taste disturbance','Photosensitivity only'],'Side effects: visual problems.'),
('Posaconazole and isavuconazole share the common uses of:','Invasive aspergillosis (if voriconazole C/I) and mucormycosis',['Candidiasis and cryptococcosis','Dermatophytosis and onychomycosis','ABPA and asthma'],'Common uses: invasive aspergillosis (if voriconazole C/I); mucormycosis.'),
('The specific use of posaconazole/isavuconazole is to prevent fungal infection in:','Graft vs host disease (GVHD) in immunosuppressed patients',['HIV patients','Neutropenic induction','Transplant rejection treatment'],'Specific use: graft vs host disease (GVHD) - to prevent fungal infection in immunosuppressed patients.'),
])
unit('Cell Wall Targeting Drugs: Echinocandins and Ibrexafungerp',
 'Echinocandins treat invasive aspergillosis and candida - DOC both for species other than Candida albicans and for invasive candidiasis - and the group is caspofungin, micafungin, anidulafungin and rezafungin. Ibrexafungerp is the oral beta-glucan synthase blocker used for recurrent vaginal candidiasis, with oral oteseconazole as alternative.')
facts(182,[
('Echinocandins are used in:','Invasive aspergillosis',['Mucormycosis','Dermatophytosis','Fungal keratitis'],'Echinocandins uses: invasive aspergillosis.'),
('In candida, echinocandins are DOC for:','Species other than Candida albicans',['Candida albicans only','All species equally','Only C. krusei'],'DOC for species other than Candida albicans.'),
('Echinocandins are DOC for:','Invasive candidiasis',['Mucocutaneous candidiasis','Oral thrush','Vaginal candidiasis'],'DOC for invasive candidiasis.'),
('The echinocandin drugs listed are:','Caspofungin, micafungin, anidulafungin and rezafungin',['Fluconazole and itraconazole','Amphotericin and nystatin','Terbinafine and griseofulvin'],'Drugs: caspofungin, micafungin, anidulafungin, rezafungin.'),
('The route of ibrexafungerp is:','Oral',['IV','Topical','Nasal'],'Ibrexafungerp route: oral.'),
('Ibrexafungerp is used for:','Recurrent vaginal candidiasis',['Invasive candidiasis','Oral thrush','Onychomycosis'],'Uses: recurrent vaginal candidiasis.'),
('The alternative to ibrexafungerp in recurrent vaginal candidiasis is:','Oral oteseconazole',['Oral fluconazole','IV micafungin','Topical clotrimazole'],'Alternative: oral oteseconazole.'),
])
unit('Organelle Targeting Drugs: Griseofulvin, Flucytosine and Natamycin',
 'Griseofulvin is a static microtubule drug given orally, concentrated in stratum corneum and taken with fatty foods for absorption; it covers dermatophytes (now with rising resistance) and is DOC for tinea capitis (kerion) in children. Flucytosine, a prodrug of 5-fluoro-uracil, inhibits DNA synthesis and treats cryptococcal meningitis IV for a maximum of 2 weeks before bone-marrow suppression and colitis dominate. Natamycin is DOC for fungal corneal ulcer, with atropine added to prevent synechiae between iris and lens.')
facts(183,[
('Griseofulvin is a:','Static drug targeting microtubules',['Cidal drug targeting ergosterol','Static drug targeting DNA','Cidal drug targeting cell wall'],'Static drug -> targets microtubules.'),
('The route of griseofulvin is:','Oral (concentrated in stratum corneum)',['Topical','IV','Nasal'],'Route: oral (concentrated in stratum corneum).'),
('Griseofulvin should be taken with fatty foods to:','Increase absorption',['Decrease gastric irritation','Delay excretion','Prefer hepatic uptake'],'To be taken with fatty foods (for increased absorption).'),
('Griseofulvin is used for:','Dermatophytes (now with increased resistance)',['Candidiasis','Cryptococcosis','Mucormycosis'],'Use: dermatophytes (now increased resistance).'),
('Griseofulvin is DOC for which paediatric condition?','Tinea capitis (kerion) in children',['Tinea corporis in adults','Onychomycosis','Tinea versicolor'],'DOC for tinea capitis (kerion) in children.'),
('Flucytosine is a prodrug of:','5-Fluoro-uracil',['5-Fluoro-cytosine','Cytarabine','Uracil'],'Prodrug of 5-fluoro-uracil.'),
('Flucytosine ultimately inhibits:','DNA synthesis',['RNA polymerase','Protein synthesis','Ergosterol synthesis'],'Inhibits DNA synthesis.'),
('Flucytosine is used for:','Cryptococcal meningitis (IV route)',['Candidiasis (oral)','Aspergillosis','Dermatophytosis'],'Uses: cryptococcal meningitis (IV route).'),
('The side effects of flucytosine are:','Bone marrow suppression and colitis',['Hepatotoxicity and rash','Nephrotoxicity and ototoxicity','QT prolongation'],'Side effects: bone marrow suppression; colitis.'),
('The maximum duration of flucytosine use is:','2 weeks',['1 week','4 weeks','6 weeks'],'Maximum duration of use: 2 weeks.'),
('Natamycin is DOC for:','Fungal corneal ulcer',['Fungal keratitis','Endophthalmitis','Orbital cellulitis'],'Natamycin: DOC for fungal corneal ulcer.'),
('The add-on drug with natamycin in fungal corneal ulcer is:','Atropine (to prevent synechiae between iris and lens)',['Pilocarpine','Timolol','Phenylephrine'],'Add-on drug: atropine (to prevent synechiae formation b/w iris & lens).'),
])
finish()

# CHAPTER 46 -----------------------------------------------------------------
start(46)
unit('Anti-Herpes Drugs: Replication Cycle and Drug Targets',
 'Non-retroviral antivirals divide into anti-herpes, anti-influenza and anti-hepatitis groups. Herpes is a DNA virus tropic for epithelial cells: docosanol and fomivirsen block attachment, viral RNA polymerase makes RNA that is translated into viral kinase, cytoplasmic kinase converts nucleoside to nucleotide, and DNA polymerase - blocked by acyclovir and ganciclovir - elongates the chain while foscarnet blocks the DNA primer pyrophosphate site. Acyclovir and ganciclovir need VK/CK to reach triphosphates (AC-TP, GC-TP) that competitively inhibit DNA polymerase; cidofovir, a cytosine analogue, needs only CK to reach diphosphates with the same end effect.')
facts(184,[
('The three groups of non-retroviral antivirals are:','Antiherpes, anti-influenza and anti-hepatitis',['Anti-herpes, anti-fungal and anti-hepatitis','Anti-influenza, anti-RSV and anti-HIV','Anti-hepatitis, anti-HIV and anti-herpes'],'Non-retroviral antivirals: antiherpes, anti-influenza, anti-hepatitis.'),
('Herpes virus is a:','DNA virus',['RNA virus','Retrovirus','Prion'],'Herpes virus replication: DNA virus.'),
('Herpes virus shows tropism for:','Epithelial cells',['Neurones only','Lymphocytes','Hepatocytes'],'Tropism for epithelial cells.'),
('The replication step blocked by docosanol and fomivirsen is:','Attachment of virus to cell',['Uncoating','Translation','Chain elongation'],'Docosanol and fomivirsen inhibit attachment of virus to cell.'),
('In the herpes cycle, viral RNA polymerase produces:','RNA',['DNA primer','Nucleotide','Protein directly'],'RNA polymerase -> RNA.'),
('Translation of viral RNA produces:','Viral kinase (VK)',['Cytoplasmic kinase','DNA polymerase','Neuraminidase'],'Translation -> viral kinase (VK).'),
('A nucleoside is converted to a nucleotide by:','Cytoplasmic kinase (CK)',['Viral kinase','DNA polymerase','Thymidine kinase only'],'Nucleoside -> cytoplasmic kinase (CK) -> nucleotide.'),
('Foscarnet blocks which part of the herpes cycle?','The DNA primer (pyrophosphate) site',['Viral kinase','Attachment','Translation'],'Foscarnet blocks the DNA primer (X-P-P-P) step.'),
('Acyclovir and ganciclovir block:','DNA polymerase',['RNA polymerase','Viral kinase','Attachment'],'Acyclovir and ganciclovir block DNA polymerase.'),
('During chain elongation DNA polymerase releases:','P-P (pyrophosphate)',['ATP','A water molecule only','Inorganic phosphate single unit'],'DNA polymerase adds -P-nucleotide and releases P-P (pyrophosphate).'),
('Acyclovir and ganciclovir are activated to triphosphates (AC-TP, GC-TP) by:','VK and CK',['CK only','VK only','Host thymidylate synthase'],'Acyclovir/ganciclovir -> VK/CK -> AC-TP/GC-TP (triphosphates).'),
('AC-TP and GC-TP act by:','Competitively inhibiting DNA polymerase and blocking viral DNA chain elongation',['Inhibiting RNA polymerase','Blocking attachment','Inhibiting cytoplasmic kinase'],'They competitively inhibit DNA polymerase and block viral DNA chain elongation.'),
('Cidofovir belongs to which analogue class?','Cytosine analogue',['Guanosine analogue','Adenosine analogue','Thymidine analogue'],'Cytosine analogue: cidofovir.'),
('Cidofovir is phosphorylated to diphosphates by:','CK',['VK','DNA polymerase','Host dihydrofolate reductase'],'Cidofovir -> CK -> diphosphates.'),
('Cidofovir diphosphates act by:','Competitively inhibiting DNA polymerase and blocking viral DNA chain elongation',['Inhibiting pyrophosphate binding','Blocking uncoating','Inhibiting neuraminidase'],'Same end effect: competitively inhibits DNA polymerase, blocks chain elongation.'),
])
unit('Foscarnet Site, Viral Kinases, Maribavir and Resistance',
 'Foscarnet inhibits the pyrophosphate binding site and needs no kinase activation. The viral kinase is thymidine kinase in HSV/VZV but UL-97 in CMV - the kinase maribavir inhibits, thereby reducing ganciclovir effect. Resistance to acyclovir/ganciclovir is most commonly an absent or altered viral kinase, then DNA polymerase mutation; the alternatives are cidofovir and foscarnet, foscarnet being DOC in resistance because of lower toxicity.')
facts(185,[
('Foscarnet inhibits which site?','Pyrophosphate binding site',['Nucleoside binding site','Triphosphate site','Primer site'],'Foscarnet: inhibits pyrophosphate binding site.'),
('The viral kinase in HSV/VZV is:','Thymidine kinase',['UL-97','Protein kinase R','Cytoplasmic kinase'],'Viral kinase in HSV/VZV: thymidine kinase.'),
('The viral kinase in CMV is:','UL-97',['Thymidine kinase','DNA polymerase','Integrase'],'Viral kinase in CMV: UL-97.'),
('Maribavir inhibits:','UL-97',['Thymidine kinase','DNA polymerase','Neuraminidase'],'Maribavir inhibits UL-97.'),
('By inhibiting UL-97, maribavir causes:','Decreased ganciclovir effect',['Increased ganciclovir effect','Increased acyclovir effect','No effect on ganciclovir'],'Maribavir inhibits UL-97 -> decreased ganciclovir effect.'),
('The most common mechanism of acyclovir/ganciclovir resistance is:','Absent/altered viral kinase',['DNA polymerase mutation','Efflux pumps','Thymidylate synthase upregulation'],'Resistance: absent/altered viral kinase (m/c).'),
('The second resistance mechanism to acyclovir/ganciclovir is:','DNA polymerase mutation',['Altered attachment protein','Cytoplasmic kinase loss','Membrane change'],'DNA polymerase mutation.'),
('The alternative drugs in acyclovir/ganciclovir resistance are:','Cidofovir and foscarnet',['Valacyclovir and valganciclovir','Famciclovir and penciclovir','Docosanol and fomivirsen'],'Alternative drugs: cidofovir; foscarnet.'),
('The DOC in resistance due to lower toxicity is:','Foscarnet',['Cidofovir','Ganciclovir','Acyclovir high dose'],'Foscarnet: DOC in resistance d/t decreased toxicity.'),
])
unit('Acyclovir and Ganciclovir: Routes, Uses and Toxicity',
 'Acyclovir, the most important anti-herpes drug, is poorly absorbed topically and orally: IV is DOC for severe disease (herpes encephalitis, neonatal HSV, HSV in immunocompromised patients) and the oral prodrug valacyclovir is DOC for HSV/VZV and for preventing perinatal HSV transmission when started at 36 weeks of gestation. IV high doses crystallise into renal stones with obstructive renal failure and also cause neurotoxicity, while oral therapy upsets the gut. Ganciclovir is IV for systemic CMV (lungs, brain, GIT), oral valganciclovir is DOC for CMV retinitis and intravitreal injection or implant is used when blindness risk is high; bone-marrow suppression is managed by continuing treatment plus filgrastim.')
facts(185,[
('The most important anti-herpes drug on the page is:','Acyclovir',['Ganciclovir','Foscarnet','Cidofovir'],'Acyclovir (most important).'),
('Topical acyclovir is not preferred because of:','Low absorption',['Local irritation','Rapid inactivation','Poor patient compliance'],'Topical: not preferred (d/t low absorption).'),
('IV acyclovir is DOC for severe infections including:','Herpes encephalitis, neonatal HSV and HSV in immunocompromised patients',['Genital herpes first episode','Cold sores','Herpes keratitis'],'IV DOC for severe infections: herpes encephalitis, neonatal HSV, HSV in immunocompromised patients.'),
('Oral acyclovir is not preferred because of:','Poor oral absorption',['First-pass metabolism','Food interactions','Gastric degradation'],'Oral: not preferred (d/t poor oral absorption).'),
('The preferred oral prodrug of acyclovir, DOC for HSV/VZV, is:','Valacyclovir',['Famciclovir','Penciclovir','Ganciclovir'],'Pro-drug valacyclovir preferred: DOC for HSV/VZV.'),
('Prevention of perinatal HSV transmission uses valacyclovir started at:','36 weeks of gestation',['28 weeks of gestation','32 weeks of gestation','Term only'],'DOC for prevention of perinatal HSV transmission: started at 36 weeks of gestation.'),
('The common side effect of oral acyclovir is:','GI upsets',['Rash','Headache only','Hepatotoxicity'],'Side effects: GI upsets.'),
('High-dose IV acyclovir causes nephrotoxicity through:','Crystalluria -> renal stones -> obstructive renal failure',['Direct tubular necrosis','Interstitial nephritis','Glomerulonephritis'],'If IV route (high doses): nephrotoxicity d/t crystalluria -> renal stones -> obstructive renal failure.'),
('High-dose IV acyclovir also causes:','Neurotoxicity',['Ototoxicity','Cardiotoxicity','Ocular toxicity'],'IV high doses also cause neurotoxicity.'),
('IV ganciclovir is used for:','Systemic CMV infections (e.g. lungs, brain, GIT)',['HSV encephalitis','VZV disseminated disease','EBV mononucleosis'],'IV: used for systemic CMV infections (e.g. lungs, brain, GIT etc).'),
('The oral prodrug preferred for CMV, DOC for CMV retinitis, is:','Valganciclovir',['Valacyclovir','Famciclovir','Cidofovir'],'Oral: pro-drug valganciclovir preferred d/t increased oral absorption (DOC for CMV retinitis).'),
('Intravitreal injection or implant of ganciclovir is used when:','There is increased risk of blindness in CMV retinitis (increased local effect)',['Systemic disease is present','The patient is pregnant','Oral therapy fails only'],'Intravitreal injection/implant: if increased risk of blindness in CMV retinitis (d/t increased local effect).'),
('The major side effect of ganciclovir is:','Bone marrow suppression',['Nephrotoxicity','Hepatotoxicity','Pancreatitis'],'Side effects: bone marrow suppression.'),
('If neutropenia develops on ganciclovir, the page advises:','Continue treatment + filgrastim to treat neutropenia',['Stop ganciclovir immediately','Switch to acyclovir','Add steroids'],'If neutropenia: continue treatment + filgrastim to treat neutropenia.'),
])
unit('Penciclovir, Foscarnet, Famciclovir, Cidofovir, Fomivirsen and Topical-only Drugs',
 'Penciclovir is given IV or topically for HSV/VZV because oral absorption is poor; its oral prodrug is famciclovir. Foscarnet is IV and DOC for resistant herpes but is nephrotoxic and disturbs calcium, phosphate, magnesium and potassium. Cidofovir is IV for acyclovir/ganciclovir-resistant herpes, BK virus in transplant patients and adenovirus, topical for ano-genital warts and CIN, and intralesional DOC for recurrent laryngeal papillomatosis. Fomivirsen is intraocular for ganciclovir-resistant CMV retinitis with ocular inflammation; docosanol, idoxuridine and trifluridine are topical-only drugs.')
facts(186,[
('The routes of penciclovir for HSV/VZV are:','IV and topical',['Oral and IV','Topical only','IM'],'Penciclovir route: I/v and topical for HSV/VZV.'),
('Oral penciclovir is limited by:','Poor oral absorption',['Rapid metabolism','Food effects','Gastric acid degradation'],'Oral: poor oral absorption.'),
('Foscarnet is given IV as DOC for:','Resistant herpes',['Sensitive HSV','CMV retinitis','VZV keratitis'],'Foscarnet route: IV - DOC for resistant herpes.'),
('The side effects of foscarnet are:','Nephrotoxicity and electrolyte imbalance',['Hepatotoxicity and rash','BM suppression','Neurotoxicity only'],'Side effects: nephrotoxicity; electrolyte imbalance.'),
('The electrolyte disturbances of foscarnet include:','Increase/decrease of Ca++ and PO4 3-, and decrease of Mg++ and K+',['Only hypokalemia','Only hypercalcemia','Only hyponatremia'],'Electrolyte imbalance: up/down of Ca++, PO4 3-; down of Mg++, K+.'),
('Famciclovir is the:','Oral prodrug of penciclovir',['Oral prodrug of ganciclovir','Topical form of acyclovir','IV form of cidofovir'],'Famciclovir: oral prodrug of penciclovir.'),
('IV cidofovir treats:','AC/GC resistant herpes, BK virus (transplant patients) and adenovirus',['Sensitive HSV only','CMV retinitis only','Influenza'],'IV: to treat AC/GC resistant herpes, BK virus (in transplant patients), adenovirus.'),
('Topical cidofovir treats:','Ano-genital warts and cervical intraepithelial neoplasia (CIN)',['Recurrent laryngeal papillomatosis','CMV retinitis','HSV keratitis'],'Topical: to treat ano genital warts, cervical intraepithelial neoplasia (CIN).'),
('Intralesional cidofovir is DOC for:','Recurrent laryngeal papillomatosis',['Ano-genital warts','CIN','Adenovirus pneumonia'],'Intralesional: DOC for recurrent laryngeal papillomatosis.'),
('Fomivirsen is given intraocularly for:','CMV retinitis resistant to ganciclovir',['HSV keratitis','VZV retinitis','Sensitive CMV retinitis'],'Route: intraocular for CMV retinitis resistant to ganciclovir.'),
('The side effects of fomivirsen are:','Ocular (iritis, uveitis, cataract, macular edema)',['Systemic nephrotoxicity','BM suppression','Hepatotoxicity'],'Side effects: ocular (e.g. iritis, uveitis, cataract, macular edema).'),
('Docosanol is a topical-only drug used for:','Orolabial herpes',['Genital herpes','HSV keratitis','CMV retinitis'],'Docosanol: orolabial herpes (topical-only group).'),
('Idoxuridine is a topical-only drug used for:','Orolabial and genital herpes',['HSV keratitis','Orolabial herpes only','CMV retinitis'],'Idoxuridine: orolabial & genital herpes (topical-only group).'),
('Trifluridine is a topical-only drug used for:','HSV keratitis',['Orolabial herpes','Genital herpes','CMV retinitis'],'Trifluridine: HSV keratitis (topical-only group).'),
])
unit('Anti-influenza Drugs: Replication, M-protein and Neuraminidase Inhibitors',
 'Influenza is an RNA virus tropic for respiratory epithelial cells; hemagglutinin binds the sialic acid receptor, the m-protein proton pump drives uncoating (blocked by amantadine and rimantadine, now abandoned for high resistance), and release needs neuraminidase (oseltamivir, zanamivir). Oseltamivir is the oral DOC for influenza A, B and bird flu at 75 mg BD x5d for treatment and 75 mg OD x7d for prophylaxis; zanamivir (inhalational > IV) is DOC for oseltamivir-resistant influenza at 10 mg BD x5d / 10 mg OD x7d; peramivir is IV 600 mg once for sensitive cases and laninamivir inhaled 40 mg once for resistant cases.')
facts(186,[
('Influenza virus is a:','RNA virus',['DNA virus','Retrovirus','Defective virus'],'Influenza virus replication: RNA virus.'),
('Influenza shows tropism for:','Respiratory epithelial cells',['Gut epithelial cells','Hepatocytes','Neurones'],'Tropism for respiratory epithelial cells.'),
('The influenza surface protein that binds the host sialic acid receptor is:','Hemagglutinin',['Neuraminidase','m-protein','RNA polymerase'],'Hemagglutinin binds to sialic acid receptor.'),
('The m-protein of influenza acts as a:','Proton pump',['Ion channel for K+','Fusion protein','Capsid protein'],'m-protein (proton pump).'),
('Uncoating of influenza is blocked by:','Amantadine and rimantadine',['Oseltamivir and zanamivir','Baloxavir','Peramivir'],'Uncoating step is blocked by amantadine/rimantadine.'),
('Baloxavir blocks which influenza enzyme activity?','Endonuclease activity of RNA polymerase',['Neuraminidase','m-protein pump','Hemagglutinin'],'Baloxavir blocks endonuclease activity.'),
('Oseltamivir and zanamivir block the influenza step of:','Neuraminidase-mediated release (break down/assembly)',['Attachment','Uncoating','Translation'],'Oseltamivir (DOC)/zanamivir act at the neuraminidase break-down step.'),
])
facts(187,[
('The MOA of m-protein inhibitors is:','Block uncoating',['Block attachment','Block neuraminidase','Block endonuclease'],'m-protein inhibitors MOA: block uncoating.'),
('Amantadine and rimantadine are not used because of:','Increased level of resistance',['High toxicity','Poor absorption','Narrow spectrum'],'Not used d/t increased level of resistance.'),
('The route of oseltamivir and its DOC status cover:','Oral route; DOC for influenza A, influenza B and bird flu',['IV route; DOC for resistant flu','Inhalational; DOC for bird flu only','Oral; DOC only for influenza A'],'Oseltamivir: oral route - DOC for influenza A, influenza B, bird flu.'),
('The treatment dosage of oseltamivir is:','75 mg BID x5d',['75 mg OD x7d','150 mg BID x5d','30 mg BID x5d'],'Treatment: 75 mg BID x5d.'),
('The prophylaxis dosage of oseltamivir is:','75 mg OD x7d',['75 mg BID x5d','150 mg OD x7d','40 mg once'],'Prophylaxis: 75 mg OD x7d.'),
('The route preference for zanamivir is:','Inhalational > IV',['Oral > IV','IV > inhalational','Oral only'],'Zanamivir route: inhalational > I/v.'),
('Zanamivir is DOC for:','Oseltamivir resistant influenza',['Sensitive influenza A','Bird flu first line','Influenza B only'],'DOC: oseltamivir resistant influenza.'),
('The treatment dosage of zanamivir is:','10 mg BID x 5d',['10 mg OD x 7d','40 mg once','600 mg once'],'Zanamivir treatment: 10 mg BID x 5d.'),
('The prophylaxis dosage of zanamivir is:','10 mg OD x 7d',['10 mg BID x 5d','75 mg OD x7d','40 mg once'],'Zanamivir prophylaxis: 10 mg OD x 7d.'),
('Peramivir is given:','IV, 600 mg once, for oseltamivir sensitive cases',['Inhaled 40 mg once for resistant cases','Orally 75 mg BID','IV for resistant cases'],'Peramivir: route I/v, dosage 600 mg once, use oseltamivir sensitive cases.'),
('Laninamivir is given:','Inhalational, 40 mg once, for oseltamivir resistant cases',['IV 600 mg once for sensitive cases','Orally 10 mg BID','Inhaled 10 mg OD x7d'],'Laninamivir: route inhalational, dosage 40 mg once, use oseltamivir resistant cases.'),
])
unit('Baloxavir and Anti-Hepatitis B Drugs',
 'Baloxavir, an oral single dose of 40-80 mg, blocks endonuclease and covers resistant influenza A, B and bird flu. In hepatitis B only chronic active cases (raised ALT/AST with histological inflammation) are treated: specific DNA-polymerase blockers with no finite duration include first-line entecavir (DOC when hepatic decompensation, but lamivudine resistance breeds entecavir resistance) and poorly absorbed adefovir (given as adefovir dipivoxal); non-specific anti-HIV reverse-transcriptase blockers include tenofovir (DOC for Hep-B, nephrotoxic, contraindicated in hepatic decompensation) plus lamivudine and its converts emtricitabine, clavudine and telbivudine, which must not be given together. IFN-alpha2b gives a finite 1-year course but suppresses marrow, is contraindicated in decompensation and is DOC when Hep D coexists.')
facts(187,[
('The MOA of the RNA polymerase inhibitor baloxavir is:','Blocks endonuclease activity',['Blocks neuraminidase','Blocks uncoating','Blocks attachment'],'RNA polymerase inhibitor MOA: blocks endonuclease activity.'),
('The route of baloxavir is:','Oral single dose',['Oral x5 days','IV single dose','Inhalational'],'Baloxavir route: oral single dose.'),
('Baloxavir is used for:','Resistant cases of influenza A, influenza B and bird flu',['Sensitive influenza only','Prophylaxis only','RSV'],'Use: resistant cases of influenza A, influenza B, bird flu.'),
('The dosage of baloxavir is:','40-80 mg single dose',['75 mg BID x5d','10 mg OD x7d','600 mg once'],'Dosage: 40-80 mg single dose.'),
])
facts(188,[
('Hepatitis B is treated only in chronic cases in active state, defined by:','Raised ALT/AST and histological signs of inflammation',['HBsAg positivity alone','Any ALT rise','Family history of HCC'],'Only treat chronic cases in active state with ALT/AST up and histological signs of inflammation.'),
('The specific hepatitis B drugs act by:','Blocking DNA polymerase, with no finite treatment duration',['Blocking reverse transcriptase with finite duration','Blocking RNA polymerase','Blocking entry'],'Specific drugs: block DNA polymerase; no finite treatment duration.'),
('Entecavir (1st line) is DOC for:','Hep-B with hepatic decompensation',['Hep-B without decompensation','Hep-B with Hep D','Hep-B in pregnancy'],'Entecavir: DOC for Hep-B with hepatic decompensation.'),
('If lamivudine resistance is present, what happens to entecavir?','Entecavir resistance develops',['Entecavir becomes more effective','No change','Entecavir is contraindicated by toxicity'],'If lamivudine resistance (+) -> entecavir resistance develops.'),
('Adefovir is limited by poor oral absorption, so the prodrug used is:','Adefovir dipivoxal',['Adefovir pivoxil free base','Tenofovir alafenamide','Entecavir'],'Pro-drug adefovir dipivoxal used instead.'),
('The non-specific hepatitis B drugs are:','Anti-HIV drugs that block reverse transcriptase',['Interferons','DNA polymerase blockers','Entry inhibitors'],'Non-specific drugs: anti-HIV drugs (block reverse transcriptase).'),
('Tenofovir is DOC for:','Hep-B',['Hep-C','Hep-D','Hep-A'],'Tenofovir: DOC for Hep-B.'),
('The side effect of tenofovir is:','Nephrotoxic',['Hepatotoxic','Pancreatitis','Lactic acidosis only'],'Side effect: nephrotoxic.'),
('Tenofovir is contraindicated in:','Hep-B with hepatic decompensation (risk of hepatic renal syndrome)',['Hep-B with normal liver','HIV coinfection','Pregnancy always'],'C/I: Hep-B with hepatic decompensation (d/t risk of hepatic renal syndrome).'),
('Lamivudine is converted into:','Emtricitabine, clavudine and telbivudine',['Tenofovir and adefovir','Entecavir','Zidovudine'],'Lamivudine converted into emtricitabine, clavudine, telbivudine.'),
('Lamivudine and its converts should not be:','Given together',['Given with tenofovir','Given with entecavir','Given in decompensation'],'They should not be given together.'),
('IFN-alpha2b therapy in hepatitis B has a finite duration of:','1 year',['6 months','2 years','Indefinite'],'Finite duration of treatment: 1 yr.'),
('Chronic interferon use causes toxicity as:','BM suppression',['Hepatotoxicity','Nephrotoxicity','Cardiotoxicity'],'Chronic use -> toxicity (BM suppression).'),
('Interferon is contraindicated in:','Hepatic decompensation',['Chronic active hepatitis','Hep D coinfection','Compensated cirrhosis'],'C/I: hepatic decompensation.'),
('Interferon is DOC in:','Hep B with Hep D',['Hep B alone','Hep C alone','Hep A'],'DOC: Hep B with Hep D.'),
])
unit('Hepatitis C Drugs, DAA Suffixes and Interferon Notes',
 'In hepatitis C, IFN alpha-2a/2b raises viral RNA degrading enzymes (marrow suppression limits it) and ribavirin blocks RNA polymerase - IV also in severe influenza and hemorrhagic fever, inhaled as DOC for RSV. Oral direct-acting antivirals are the treatment of choice as 2/3-drug regimens (sofosbuvir, velpatasvir, paritaprevir boosted with ritonavir), with suffixes decoding targets: -buvir NS5B, -asvir NS5A, -previr protease/NS3-4. Interferons elsewhere: IFN-gamma in chronic granulomatous disease, IFN-beta in multiple sclerosis, IFN-alpha 2a/2b in CML and Kaposi sarcoma, and palivizumab or nirsevimab for RSV prophylaxis.')
facts(188,[
('The MOA of IFN alpha-2a/2b in hepatitis C is:','Increased viral RNA degrading enzymes',['Blocking RNA polymerase','Blocking reverse transcriptase','Increasing NK cells only'],'MOA: increased viral RNA degrading enzymes.'),
('The side effect of interferon in HCV therapy is:','BM suppression',['Hepatotoxicity','Nephrotoxicity','Hypothyroidism only'],'Side effect: BM suppression.'),
('The MOA of ribavirin is:','Blocks RNA polymerase',['Blocks DNA polymerase','Blocks protease','Blocks entry'],'Ribavirin MOA: blocks RNA polymerase.'),
('IV ribavirin is also given in:','Severe influenza and hemorrhagic fever',['RSV only','Hepatitis B','Lassa fever only'],'I/V also given in severe influenza & hemorrhagic fever.'),
('Inhalational ribavirin is DOC in:','Respiratory syncytial virus (RSV)',['Influenza','Parainfluenza','Adenovirus'],'Inhalational: DOC in respiratory syncytial virus (RSV).'),
('The route of direct acting antivirals (DAAs) is:','Oral',['IV','Topical','IM'],'DAAs route: oral.'),
('DAAs are the treatment of choice in HCV as a:','2/3 drug regimen',['Monotherapy','4 drug regimen','Sequential monotherapy'],'Treatment of choice (2/3 drug regimen).'),
('The example DAAs listed are:','Sofosbuvir, velpatasvir and paritaprevir',['Ribavirin and interferon','Entecavir and tenofovir','Oseltamivir and zanamivir'],'Eg: sofosbuvir, velpatasvir, paritaprevir.'),
('Paritaprevir is boosted with:','Ritonavir',['Cobicistat','Itraconazole','Grapefruit juice'],'Paritaprevir: boosted with ritonavir.'),
('The DAA suffix -buvir denotes a:','NS5B blocker',['NS5A blocker','Protease blocker','Entry blocker'],'DAA suffix: bu-vir - NS5B blocker.'),
('The DAA suffix -asvir denotes a:','NS5A blocker',['NS5B blocker','Protease blocker','Polymerase II blocker'],'DAA suffix: as-vir - NS5A blocker.'),
('The DAA suffix -previr denotes a:','Protease or NS 3/4 blocker',['NS5B blocker','NS5A blocker','Integrase blocker'],'DAA suffix: pre-vir - protease or NS 3/4 blocker.'),
('IFN-gamma is used in:','Chronic granulomatous disease',['Multiple sclerosis','CML','Kaposi sarcoma'],'IFN-gamma: chronic granulomatous disease.'),
('IFN-beta is used in:','Multiple sclerosis',['Chronic granulomatous disease','CML','Hepatitis C only'],'IFN-beta: multiple sclerosis.'),
('IFN-alpha 2a/2b is used in:','Chronic myelogenous leukemia and Kaposi\'s sarcoma',['Multiple sclerosis','Chronic granulomatous disease','RSV'],'IFN-alpha 2a/2b: chronic myelogenous leukemia, Kaposi\'s sarcoma.'),
('The anti-RSV monoclonal antibodies for RSV prophylaxis are:','Palivizumab and nirsevimab',['Omalizumab and dupilumab','Rituximab and infliximab','Bevacizumab and cetuximab'],'RSV prophylaxis: palivizumab, nirsevimab (anti-RSV monoclonal antibodies).'),
])
finish()
