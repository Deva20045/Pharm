# -*- coding: utf-8 -*-
"""Generate chapters 47-49 from Marrow Pharmacology E8, book pp189-204.

ch47 Anti-Retroviral Drugs  (p189-192)
ch48 Anti-Mycobacterial Drugs (p193-198)
ch49 Anti-Protozoal Drugs (p199-204)
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

# CHAPTER 47 - ANTI-RETROVIRAL DRUGS (p189-192) --------------------------------
start(47)
unit('HIV Replication Cycle and Drug Targets',
 'HIV is an RNA virus with tropism for CD4 cells. The replication diagram shows attachment at CD4 and CCR5, fusion through GP41 (only GP41), uncoating with capsid removal, reverse transcription of RNA to DNA, integration of viral DNA into human DNA inside the human nucleus, transcription and translation, protease assembly into immature virus and protease maturation into mature virus which exits and invades other CD4 cells. Drugs drawn on the cycle: GP41 - enfuvirtide, CD4 - ibalizumab, CCR5 - maraviroc, GP120 - fostemsavir and capsid - lenacapavir.')
facts(189,[
('HIV is a:','RNA virus',['DNA virus','Double-stranded DNA virus','Prion'],'Human immunodeficiency virus: RNA virus.'),
('The tropism of HIV is for:','CD4 cells',['CD8 cells','B cells','Platelets'],'HIV: tropism for CD4 cells.'),
('The drug shown acting at GP41 on the replication cycle is:','Enfuvirtide',['Maraviroc','Ibalizumab','Fostemsavir'],'GP41 - enfuvirtide.'),
('Ibalizumab acts at:','CD4',['CCR5','GP41','GP120'],'Attachment: CD4 - ibalizumab.'),
('Maraviroc acts at:','CCR5',['CD4','GP120','GP41'],'Attachment: CCR5 - maraviroc.'),
('The drug acting at GP120 is:','Fostemsavir',['Enfuvirtide','Maraviroc','Lenacapavir'],'GP120 - fostemsavir.'),
('The drug acting on the capsid is:','Lenacapavir',['Fostemsavir','Ibalizumab','Enfuvirtide'],'Capsid - lenacapavir.'),
('Fusion of HIV with the host cell membrane occurs through:','GP41 only',['GP120 only','GP41 and GP120 together','CD4 and CCR5 together'],'Fusion (only GP41) is labelled on the diagram.'),
('The first event after fusion inside the host cell is:','Removal of capsid',['Reverse transcription','Integration','Budding'],'Fusion -> capsid removed -> RNA exposed.'),
('Viral RNA is converted into DNA by:','Reverse transcriptase',['Integrase','Protease','RNA polymerase'],'RNA --(reverse transcriptase)--> DNA.'),
('Viral DNA is integrated into human DNA by:','Integrase',['Reverse transcriptase','Protease','Ligase'],'DNA --(integrase)--> integration into human DNA.'),
('Integration of viral DNA takes place in the:','Human nucleus',['Cytoplasm','Viral capsid','Golgi apparatus'],'Integration is drawn inside the human nucleus.'),
('After integration, transcription and translation occur in the:','Human nucleus',['Cytoplasm','Viral capsid','Free ribosomes of blood'],'Transcription + translation are drawn in the human nucleus.'),
('Protease assembly directly produces:','Immature virus',['Mature virus','Proviral DNA','Empty capsids'],'Protease assembly -> immature virus.'),
('The step converting immature virus into mature virus is:','Protease maturation',['Integrase action','Reverse transcription','Uncoating'],'Immature virus --(protease maturation)--> mature virus.'),
('The mature virus finally:','Exits the cell and invades other CD4 cells',['Remains dormant in the nucleus','Is destroyed inside the cell','Infects CD8 cells'],'Mature virus exits cells and invades other CD4 cells.'),
])
unit('Classification of Anti-Retroviral Drugs',
 'Anti-retroviral drugs are divided into four groups: reverse transcriptase inhibitors (RTIs), protease inhibitors, integrase inhibitors and attachment inhibitors. RTIs are further divided into nucleoside RTIs (NRTI) and non-nucleoside RTIs (NNRTI).')
facts(189,[
('The four groups of anti-retroviral drugs are:','Reverse transcriptase inhibitors, protease inhibitors, integrase inhibitors and attachment inhibitors',['NRTIs, NNRTIs, exit and release inhibitors','Antiherpes, anti-HIV, anti-HBV and anti-HCV','Attachment, uncoating, assembly and release inhibitors'],'Classification: RTIs, protease inhibitors, integrase inhibitors, attachment inhibitors.'),
('Reverse transcriptase inhibitors are divided into:','Nucleoside RTI (NRTI) and non-nucleoside RTI (NNRTI)',['Nucleotide and nucleoside analogs only','Competitive and non-competitive inhibitors','Purine and pyrimidine analogs'],'RTIs: NRTI and NNRTI.'),
('Enfuvirtide, ibalizumab, maraviroc, fostemsavir and lenacapavir all belong to:','Attachment inhibitors',['Protease inhibitors','Integrase inhibitors','Reverse transcriptase inhibitors'],'Drugs acting at GP41/CD4/CCR5/GP120/capsid = attachment inhibitors.'),
('Dolutegravir belongs to:','Integrase inhibitors',['Protease inhibitors','NRTIs','NNRTIs'],'Dolutegravir: integrase inhibitor.'),
('Ritonavir belongs to:','Protease inhibitors',['Integrase inhibitors','NRTIs','Attachment inhibitors'],'Ritonavir: protease inhibitor (booster).'),
])
unit('Nucleoside Reverse Transcriptase Inhibitors (NRTI)',
 'NRTIs are nucleoside analogs effective against HIV 1 and HIV 2 with the class side effect of mitochondrial toxicity (myopathy, neuropathy). Lamivudine is the least toxic NRTI; emtricitabine (lamivudine derivative) causes pigmentation of palms and soles; tenofovir causes nephrotoxicity (C/I renal failure) and decreased bone density with safety unknown below age 10 yr or 30 kg. Treatment: 2 NRTIs (lamivudine/emtricitabine + tenofovir) + 1 other drug (dolutegravir); PrEP uses the same 2 NRTIs; if tenofovir is C/I use abacavir (HLA B5701 gene, Steven Johnson syndrome). Didanosine (pancreatitis) and stavudine (peripheral neuropathy) are abandoned; zidovudine is still used in children causing bone marrow suppression and myopathy, C/I in anemia.')
facts(190,[
('Nucleoside reverse transcriptase inhibitors are:','Nucleoside analogs',['Nucleotide analogs only','Non-competitive enzyme blockers','Protease analogs'],'NRTI: nucleoside analogs.'),
('NRTIs are effective against:','HIV 1 and HIV 2',['Only HIV 1','Only HIV 2','HIV and influenza'],'NRTI effective against HIV 1 + HIV 2 (contrast NNRTI: only HIV-1).'),
('The class side effect of NRTIs is:','Mitochondrial toxicity (myopathy, neuropathy)',['Nephrotoxicity','Pulmonary fibrosis','Optic neuritis'],'NRTI S/E: mitochondrial toxicity -> myopathy, neuropathy.'),
('The least toxic NRTI is:','Lamivudine',['Stavudine','Zidovudine','Didanosine'],'Drugs: least toxic NRTI - lamivudine.'),
('Emtricitabine is a derivative of:','Lamivudine',['Tenofovir','Abacavir','Zidovudine'],'Emtricitabine: derivative of lamivudine.'),
('The side effect of emtricitabine is:','Pigmentation of palms and soles',['Pancreatitis','Lactic acidosis','Renal stones'],'Emtricitabine S/E: pigmentation of palms and soles (photo shown).'),
('The side effects of tenofovir are:','Nephrotoxicity and decreased bone density',['Hepatotoxicity and pancreatitis','Myopathy and cardiomyopathy','Pigmentation and rash'],'Tenofovir S/E: nephrotoxicity (C/I in renal failure) + decreased bone density.'),
('In HIV treatment, tenofovir is contraindicated in:','Renal failure',['Liver failure','Heart failure','Asthma'],'Tenofovir nephrotoxicity: C/I in renal failure.'),
('Safety of tenofovir is unknown (use as C/I) in:','Age <10 yr and weight <30 kg',['Age <18 yr of any weight','Pregnancy only','Elderly above 65 yr'],'Drug safety unknown in age <10 yr, weight <30 kg - use C/I.'),
('The HIV treatment regimen is:','2 NRTIs (lamivudine/emtricitabine + tenofovir) + 1 other drug (dolutegravir)',['3 NRTIs together','1 NRTI + 1 NNRTI only','Tenofovir monotherapy'],'Use: 2 NRTIs (Lamivudine/Emtricitabine + Tenofovir) + 1 other drug (Dolutegravir).'),
('The pre-exposure prophylaxis (PrEP) regimen is:','2 drugs (lamivudine/emtricitabine + tenofovir)',['Tenofovir alone','Zidovudine + lamivudine','2 NRTIs + dolutegravir'],'PrEP regimen: 2 drugs (lamivudine/emtricitabine + tenofovir).'),
('If tenofovir is contraindicated, the NRTI used is:','Abacavir',['Didanosine','Stavudine','Zalcitabine'],'If tenofovir C/I: abacavir.'),
('Abacavir is associated with:','HLA B5701 gene',['HLA B1502 gene','HLA DR4','HLA B27'],'Abacavir: associated with HLA B5701 gene.'),
('The side effect of abacavir is:','Steven Johnson syndrome',['Fatal hepatotoxicity','Bone marrow suppression','Nephrotoxicity'],'Abacavir S/E: Steven Johnson syndrome.'),
('Didanosine is not used currently due to:','Pancreatitis',['Peripheral neuropathy','Nephrotoxicity','Renal stones'],'Didanosine not used: D/t pancreatitis.'),
('Stavudine is not used currently due to:','Increased peripheral neuropathy',['Pancreatitis','Renal stones','Anemia'],'Stavudine not used: D/t increased peripheral neuropathy.'),
('Zidovudine is currently used in:','Children',['Only adults','Only pregnant women','No group - it is withdrawn'],'NRTIs not used currently note: zidovudine used in children.'),
('The side effects of zidovudine are:','Bone marrow suppression and myopathy',['Nephrotoxicity and stones','Pigmentation and SJS','Hepatotoxicity and gynecomastia'],'Zidovudine S/E: bone marrow suppression, myopathy.'),
('Zidovudine is contraindicated in:','Anemia',['Hypertension','Diabetes','Gout'],'Zidovudine: C/I in anemia.'),
])
unit('Non-Nucleoside Reverse Transcriptase Inhibitors (NNRTI)',
 'NNRTIs are effective against only HIV-1 and are third line drugs because of increased resistance. Nevirapine is the DOC for perinatal HIV transmission but causes fatal hepatotoxicity; the alternative for perinatal transmission is zidovudine. The other NNRTIs are efavirenz, etravirine, doravirine and rilpivirine.')
facts(190,[
('NNRTIs are effective against:','Only HIV-1',['HIV-1 and HIV-2','HIV-2 only','All retroviruses'],'NNRTI effective against: only HIV-1.'),
('NNRTIs are used as:','3rd line drugs (due to increased resistance)',['1st line drugs','Only in PrEP','Only in children'],'NNRTI use: 3rd line drug (D/t increased resistance).'),
('The DOC for perinatal HIV transmission is:','Nevirapine',['Efavirenz','Rilpivirine','Doravirine'],'Nevirapine: DOC for perinatal HIV transmission.'),
('The side effect of nevirapine is:','Fatal hepatotoxicity',['Nephrotoxicity','Renal stones','Optic neuritis'],'Nevirapine S/E: fatal hepatotoxicity.'),
('The alternative drug for perinatal HIV transmission is:','Zidovudine',['Abacavir','Etravirine','Delavirdine'],'Alternative for perinatal HIV transmission: zidovudine.'),
('All of the following are NNRTIs EXCEPT:','Raltegravir',['Efavirenz','Etravirine','Doravirine'],'NNRTI drugs: nevirapine, efavirenz, etravirine, doravirine, rilpivirine; raltegravir is an integrase inhibitor.'),
('Rilpivirine belongs to:','NNRTIs',['NRTIs','Integrase inhibitors','Attachment inhibitors'],'NNRTI drugs 4-5: doravirine, rilpivirine.'),
])
unit('Protease Inhibitors',
 'Protease inhibitors are used in children below 6 yr or below 20 kg for increased benefit, are metabolized by CYP3A4 (except nelfinavir: CYP2C19) and all of them inhibit CYP3A4. Side effects: hepatotoxicity, insulin resistance (hyperglycemia, hyperlipidemia, lipodystrophy), GI upset as the dose-limiting effect and increased bleeding in hemophiliacs. Saquinavir is the least potent enzyme inhibitor, ritonavir the most potent and is used as a booster (raises t 1/2); lopinavir (MI, LPV/r 90%/10%) is formulated with ritonavir; atazanavir needs acidic pH (antacid C/I), has no insulin resistance and causes renal stones with unconjugated hyperbilirubinemia (also indinavir); darunavir is taken with food. All PIs can be boosters except nelfinavir; cobicistat (CYP3A4 inhibitor) replaces ritonavir and is available with atazanavir, darunavir and elvitegravir.')
facts(191,[
('Protease inhibitors are used due to increased benefit in:','Age <6 yr and weight <20 kg',['Age >18 yr adults','Only adolescents','Elderly above 60 yr'],'PI use D/t increased benefit: age <6 yr, weight <20 kg.'),
('Protease inhibitors are metabolized by:','CYP3A4 (except nelfinavir: CYP2C19)',['CYP2D6 only','CYP2C9','Flavin monooxygenases'],'Metabolized by CYP3A4 except nelfinavir: CYP2C19.'),
('All protease inhibitors are:','CYP3A4 enzyme inhibitors',['CYP3A4 enzyme inducers','CYP2C19 inhibitors','Enzyme inducers of metabolism'],'All PIs are CYP3A4 enzyme inhibitors.'),
('The side effect of protease inhibitors producing hyperglycemia, hyperlipidemia and lipodystrophy is:','Insulin resistance',['Insulin hypersensitivity','Beta cell destruction','Thyroid dysfunction'],'PI S/E: insulin resistance -> hyperglycemia, hyperlipidemia, lipodystrophy.'),
('The dose limiting side effect of protease inhibitors is:','GI upset',['Hepatotoxicity','Nephrotoxicity','Rash'],'PI S/E: GI upset - dose limiting side effect.'),
('Protease inhibitors increase the risk of bleeding in:','Hemophiliacs',['Von Willebrand disease','Thrombocytopenia','Vitamin K deficiency'],'PI S/E: increased risk of bleeding in hemophiliacs.'),
('The least potent enzyme inhibitor among protease inhibitors is:','Saquinavir',['Ritonavir','Darunavir','Atazanavir'],'Saquinavir: least potent enzyme inhibitor.'),
('The side effect of lopinavir is:','MI (myocardial infarction)',['Renal stones','Unconjugated hyperbilirubinemia','Optic neuritis'],'Lopinavir S/E: MI.'),
('Lopinavir is formulated with ritonavir in the ratio:','90%/10% (LPV/r)',['50%/50%','10%/90%','80%/20%'],'Lopinavir formulated with ritonavir (LPV/r: 90%/10%).'),
('The most potent enzyme inhibitor among protease inhibitors is:','Ritonavir',['Saquinavir','Lopinavir','Nelfinavir'],'Ritonavir: most potent enzyme inhibitor.'),
('Ritonavir is used as a:','Booster - inhibits metabolism and increases t 1/2',['Primary antiretroviral monotherapy','Integrase inhibitor','Nucleoside analog'],'Ritonavir use: booster - inhibits metabolism (increases t 1/2).'),
('Atazanavir requires which condition for absorption?','Acidic pH (antacids are C/I)',['Alkaline pH','Neutral pH with food only','Bile salts'],'Atazanavir: requires acidic pH for absorption (antacid C/I).'),
('The protease inhibitor with no insulin resistance is:','Atazanavir',['Ritonavir','Lopinavir','Saquinavir'],'Atazanavir: no insulin resistance.'),
('The side effects of atazanavir are:','Renal stones and unconjugated hyperbilirubinemia',['Pancreatitis and neuropathy','MI and myopathy','Hepatotoxicity and rash'],'Atazanavir S/E: renal stones + unconjugated hyperbilirubinemia.'),
('Renal stones and unconjugated hyperbilirubinemia are also seen with:','Indinavir',['Darunavir','Nelfinavir','Saquinavir'],'Atazanavir S/E note: also seen with indinavir.'),
('Darunavir should be taken:','With food (increased absorption)',['Empty stomach','With antacids','With milk only'],'Darunavir: taken with food (increased absorption).'),
('All protease inhibitors can be used as boosters EXCEPT:','Nelfinavir',['Ritonavir','Darunavir','Atazanavir'],'Note: all protease inhibitors can be boosters except nelfinavir.'),
('Cobicistat is:','A CYP3A4 inhibitor used to replace ritonavir',['An integrase inhibitor','An NRTI prodrug','A CYP3A4 inducer'],'Note: cobicistat (CYP3A4 inhibitor) - to replace ritonavir.'),
('Cobicistat is available with:','Atazanavir, darunavir and elvitegravir',['Zidovudine and lamivudine','Nevirapine and efavirenz','Tenofovir alone'],'Cobicistat available with: atazanavir - darunavir - elvitegravir.'),
])
unit('Integrase Inhibitors',
 'The integrase inhibitors are raltegravir, elvitegravir, bictegravir and dolutegravir, of which dolutegravir is the preferred agent and the "1 other drug" added to two NRTIs in the standard treatment regimen.')
facts(191,[
('The integrase inhibitors are:','Raltegravir, elvitegravir, bictegravir and dolutegravir (preferred)',['Ritonavir and cobicistat','Efavirenz and nevirapine','Enfuvirtide and maraviroc'],'Integrase inhibitors: raltegravir, elvitegravir, bictegravir, dolutegravir (preferred).'),
('The preferred integrase inhibitor is:','Dolutegravir',['Raltegravir','Elvitegravir','Bictegravir'],'Integrase inhibitors: dolutegravir (preferred).'),
('Dolutegravir serves as:','The 1 other drug added to 2 NRTIs in the treatment regimen',['An NNRTI used in PrEP alone','A protease booster','An attachment inhibitor'],'Treatment regimen: 2 NRTIs + 1 other drug = dolutegravir (integrase inhibitor).'),
('Bictegravir belongs to:','Integrase inhibitors',['NRTIs','Attachment inhibitors','Protease inhibitors'],'Integrase inhibitor list: raltegravir, elvitegravir, bictegravir, dolutegravir.'),
])
unit('Attachment Inhibitors',
 'Attachment inhibitors are used in resistant HIV and act at every entry structure: GP41 - enfuvirtide (fusion blocker, S/C route), CD4 - ibalizumab (I/V route), GP120 - fostemsavir, CCR5 - maraviroc and vicriviroc, and capsid - lenacapavir.')
facts(192,[
('The use of attachment inhibitors is:','Resistant HIV',['First line treatment alone','PrEP in healthy adults','Perinatal prophylaxis'],'Attachment inhibitors use: resistant HIV.'),
('The GP41 inhibitor (fusion blocker) is:','Enfuvirtide',['Ibalizumab','Fostemsavir','Vicriviroc'],'GP41 inhibitor (fusion blocker): enfuvirtide.'),
('The route of enfuvirtide is:','S/C',['Oral','I/V','Inhalational'],'Enfuvirtide route: S/C.'),
('The CD4 blocker is:','Ibalizumab',['Maraviroc','Lenacapavir','Fostemsavir'],'CD4 blocker: ibalizumab.'),
('The route of ibalizumab is:','I/V',['Oral','S/C','Topical'],'Ibalizumab route: I/V.'),
('The GP120 blocker is:','Fostemsavir',['Enfuvirtide','Maraviroc','Raltegravir'],'GP120 blocker: fostemsavir.'),
('The CCR5 blockers are:','Maraviroc and vicriviroc',['Fostemsavir and lenacapavir','Enfuvirtide and ibalizumab','Raltegravir and dolutegravir'],'CCR5 blocker: maraviroc, vicriviroc.'),
('The capsid blocker is:','Lenacapavir',['Maraviroc','Ibalizumab','Fostemsavir'],'Capsid blocker: lenacapavir.'),
])
unit('HIV Treatment Guidelines (Preferred 1st Line Regimens)',
 'Adults and children with age >10 yrs and weight >30 kg get TDF + 3TC + DTG; children 6-10 yrs (weight 20-30 kg) get ABC + 3TC + DTG; age <6 years (weight <20 kg) gets ABC + 3TC + LPV/r. In pregnancy/lactation: not on any ART - TDF + 3TC + DTG; already on ART - continue same ART; exposure to NVP in previous pregnancy - TDF + 3TC + DTG. Index: TDF tenofovir, 3TC lamivudine, DTG dolutegravir, ABC abacavir, LPV/r lopinavir/ritonavir.')
facts(192,[
('The preferred 1st line regimen for adults and children with age >10 yrs and weight >30 kg is:','TDF + 3TC + DTG',['ABC + 3TC + DTG','ABC + 3TC + LPV/r','TDF + 3TC + NVP'],'Age >10 yrs & weight >30 kg: TDF + 3TC + DTG.'),
('The preferred 1st line regimen for children 6-10 yrs (weight 20-30 kg) is:','ABC + 3TC + DTG',['TDF + 3TC + DTG','ABC + 3TC + LPV/r','TDF + 3TC + LPV/r'],'Children 6-10 yrs, weight 20-30 kg: ABC + 3TC + DTG.'),
('The preferred 1st line regimen for age <6 years (weight <20 kg) is:','ABC + 3TC + LPV/r',['TDF + 3TC + DTG','ABC + 3TC + DTG','TDF + 3TC + NVP'],'Age <6 years, weight <20 kg: ABC + 3TC + LPV/r.'),
('In pregnancy/lactation not on any ART, the preferred regimen is:','TDF + 3TC + DTG',['Continue same ART','ABC + 3TC + LPV/r','NVP monotherapy'],'Pregnancy not on any ART: TDF + 3TC + DTG.'),
('In pregnancy/lactation already on ART:','Continue same ART',['Switch to TDF + 3TC + DTG','Stop ART till delivery','Switch to ABC + 3TC + DTG'],'Pregnancy already on ART: continue same ART.'),
('In pregnancy with exposure to NVP in previous pregnancy:','TDF + 3TC + DTG',['Continue NVP alone','ABC + 3TC + LPV/r','Avoid all ART'],'Pregnancy with NVP exposure in previous pregnancy: TDF + 3TC + DTG.'),
('In the regimen index, 3TC stands for:','Lamivudine',['Emtricitabine','Abacavir','Dolutegravir'],'Index: 3TC - lamivudine.'),
('In the regimen index, ABC and LPV/r stand for:','Abacavir and lopinavir/ritonavir',['Adefovir and lopinavir/rifampicin','Abacavir and lamivudine/ritonavir','Amikacin and lopinavir/ritonavir'],'Index: ABC - abacavir; LPV/r - lopinavir/ritonavir.'),
])
finish()

# CHAPTER 48 - ANTI-MYCOBACTERIAL DRUGS (p193-198) -----------------------------
start(48)
unit('First Line Anti-TB Drugs: Mycolic Acid Pathway, MOA and Resistance',
 'The diagram shows isoniazid entering the bacterium and being activated by catalase peroxidase (Kat-G gene) to INH(a); ethionamide also acts here. INH(a) works on acyl protein reductase (Inh A gene) and acyl protein kinase (Kas-A gene), both driving mycolic acid synthesis for the cell wall. MOA: H inhibits mycolic acid synthesis (cell wall), R inhibits RNA polymerase, Z is activated by pyrazinaminidase (pnc-a gene) in acidic pH to pyrazinoic acid which inhibits fatty acid synthesis, and E inhibits arabinosyl transferase. Resistance: Kat-G mutation most severe with cross resistance to ethionamide, Inh A overexpression, rpo-b (R), pnc-a (Z), Emb-b (E).')
facts(193,[
('The gene producing catalase peroxidase that activates isoniazid is:','Kat-G gene',['Inh A gene','Kas-A gene','rpo-b gene'],'Diagram 1: Kat-G gene -> catalase peroxidase.'),
('Intracellular isoniazid is activated to:','INH(a) by catalase peroxidase',['INH(b) by pyrazinaminidase','Pyrazinoic acid by catalase','Acyl protein by kinase'],'Inh --(catalase peroxidase)--> INH(a).'),
('The gene for acyl protein kinase is:','Kas-A gene',['Kat-G gene','pnc-a gene','Emb-b gene'],'Diagram 2: Kas-A gene -> acyl protein kinase.'),
('The gene controlling acyl protein reductase is:','Inh A gene',['Kat-G gene','Kas-A gene','rpo-b gene'],'Diagram 3: Inh A gene -> acyl protein reductase.'),
('Acyl protein reductase and acyl protein kinase act on:','Mycolic acid synthesis',['Peptidoglycan cross linking','RNA synthesis','Folate synthesis'],'Both enzymes -> mycolic acid synthesis -> cell wall.'),
('Mycolic acid synthesis is required for the:','Cell wall',['Ribosome','Nucleus','Capsule only'],'Mycolic acid synthesis -> cell wall.'),
('The drug acting along with isoniazid on acyl protein reductase is:','Ethionamide',['Ethambutol','Pyrazinamide','PAS'],'Ethionamide points to acyl protein reductase in the diagram.'),
('The MOA of isoniazid is:','Inhibits mycolic acid synthesis, inhibiting cell wall',['Inhibits RNA polymerase','Inhibits arabinosyl transferase','Inhibits folate synthesis'],'MOA: H inhibits mycolic acid synthesis -> inhibits cell wall.'),
('The MOA of rifampicin is:','Inhibits RNA polymerase',['Inhibits mycolic acid synthesis','Inhibits arabinosyl transferase','Inhibits fatty acid synthesis'],'MOA: R inhibits RNA polymerase.'),
('Pyrazinamide is converted to pyrazinoic acid by:','Pyrazinaminidase (pnc-a gene) in acidic pH',['Catalase peroxidase in neutral pH','Arylsulfatase in alkaline pH','Beta lactamase at any pH'],'Pyrazinamide --(pyrazinaminidase, pnc-a gene) + acidic pH--> pyrazinoic acid.'),
('Pyrazinoic acid acts by:','Inhibiting fatty acid synthesis',['Inhibiting RNA polymerase','Blocking arabinosyl transferase','Inhibiting DHPS'],'Pyrazinoic acid -> inhibits fatty acid synthesis.'),
('The MOA of ethambutol is:','Inhibits arabinosyl transferase',['Inhibits mycolic acid synthesis','Inhibits RNA polymerase','Inhibits fatty acid synthesis'],'MOA: E inhibits arabinosyl transferase.'),
('The most severe mechanism of INH resistance is:','Kat-G gene mutation',['Inh A gene overexpression','rpo-b mutation','Emb-b mutation'],'Kat-G gene mutation: most severe.'),
('Inh A gene overexpression causes:','Cross resistance to ethionamide',['Cross resistance to rifampicin','Cross resistance to pyrazinamide','No cross resistance'],'Inh A gene overexpression -> cross resistance to ethionamide.'),
('The mechanism of rifampicin resistance is:','rpo-b gene mutation',['Kat-G mutation','pnc-a mutation','Emb-b mutation'],'R resistance: rpo-b gene mutation.'),
('The mechanism of pyrazinamide resistance is:','pnc-a gene mutation',['rpo-b mutation','Kas-A mutation','Inh A overexpression'],'Z resistance: pnc-a gene mutation.'),
('The mechanism of ethambutol resistance is:','Emb-b gene mutation',['pnc-a mutation','Kat-G mutation','rpo-b mutation'],'E resistance: Emb-b gene mutation.'),
])
unit('First Line Anti-TB Drugs: Comparison of Nature, Site, Activity and Excretion',
 'Isoniazid is cidal and the first drug to make patients non-infective; rifampicin is cidal with maximum action; pyrazinamide is cidal; ethambutol is static. Site of action: H and R intracellular + extracellular, Z only intracellular, E only extracellular. Activity: H and E on replicating bacteria only; R and Z also on non-replicating persisters (R > Z). Excretion: H, R and Z by liver (R gives maximum excretion and is safest in renal failure); E by kidney and is the most unsafe in renal failure.')
facts(194,[
('The first drug to make TB patients non-infective is:','Isoniazid (cidal)',['Ethambutol (static)','Pyrazinamide','Rifampicin'],'H: cidal, 1st drug to make patients non-infective.'),
('Bactericidal action is maximum with:','Rifampicin',['Isoniazid','Pyrazinamide','Ethambutol'],'R: cidal (maximum).'),
('The bacteriostatic first-line anti-TB drug is:','Ethambutol',['Rifampicin','Pyrazinamide','Isoniazid'],'E: static.'),
('The drugs acting at both intracellular and extracellular sites are:','Isoniazid and rifampicin',['Pyrazinamide and ethambutol','Pyrazinamide only','Ethambutol only'],'Site of action: H, R - intracellular + extracellular.'),
('The first-line anti-TB drug acting only intracellularly is:','Pyrazinamide',['Ethambutol','Isoniazid','Rifampicin'],'Site: Z - intracellular.'),
('The first-line anti-TB drug acting only extracellularly is:','Ethambutol',['Pyrazinamide','Rifampicin','Isoniazid'],'Site: E - extracellular.'),
('Rifampicin is active against replicating bacteria and:','Non-replicating bacteria (persisters) - R > Z',['Only replicating bacteria','Only dormant spores','Persisters only, not replicating'],'Active agonist: replicating + non-replicating bacteria (persisters) R > Z.'),
('Pyrazinamide is active against non-replicating persisters; isoniazid and ethambutol act on:','Replicating bacteria only',['Persisters only','Both equally','Dormant spores'],'H: replicating bacteria; E: replicating bacteria.'),
('The organ of excretion of isoniazid and pyrazinamide is:','Liver',['Kidney','Lung','Milk'],'Excretion: H - liver; Z - liver.'),
('Rifampicin is the safest anti-TB drug in renal failure because:','Maximum excretion is by liver',['It is not metabolized at all','It is completely dialyzed','It acts only in the kidney'],'R: liver - maximum excretion, safest in renal failure.'),
('The most unsafe first-line anti-TB drug in renal failure is:','Ethambutol',['Rifampicin','Isoniazid','Pyrazinamide'],'E: kidney (most unsafe in renal failure).'),
])
unit('Side Effects of First Line Anti-TB Drugs and INH Toxicity Treatment',
 'Isoniazid decreases vitamin B6 (pyridoxine) causing decreased haem (anemia) and decreased GABA (seizure), neuropathies, hallucination, memory loss and euphoria. Rifampicin gives red/orange urine and secretions (contact lens staining), flu-like respiratory symptoms with intermittent dosing, pulmonary syndrome and purpura (stop permanently), and is an enzyme inducer - least with rifabutin (S/E uveitis). Pyrazinamide is the most hepatotoxic (Z > H > R > E) and causes hyperuricemia, arthralgia and peripheral neuropathy. Ethambutol causes optic neuritis with red-green colour blindness (green > red). INH toxicity is treated with IV pyridoxine 1 g per gram of INH (max 5 g). Rifapentine with INH is used once weekly for prophylaxis/latent TB.')
facts(194,[
('The side effects of isoniazid are due to:','Decreased vitamin B6 (pyridoxine)',['Vitamin B6 excess','Zinc deficiency','Pyridoxine independent action'],'H S/E: decreased vit B6 (pyridoxine).'),
('Decreased haem due to isoniazid causes:','Anemia',['Polycythemia','Methemoglobinemia','Hemochromatosis'],'INH: decreased haem -> anemia.'),
('Decreased GABA due to isoniazid causes:','Seizure',['Migraine','Parkinsonism','Myopathy'],'INH: decreased GABA -> seizure.'),
('The neuropsychiatric side effects of isoniazid are:','Neuropathies, hallucination, memory loss and euphoria',['Optic neuritis and red-green blindness','Renal stones and hyperuricemia','Deafness and vertigo'],'INH: neuropathies, hallucination, memory loss, euphoria.'),
('The side effect of rifampicin in urine and secretions is:','Red/orange discoloration',['Blue-green discoloration','Black discoloration','No discoloration'],'R S/E 1: red/orange - urine, secretions.'),
('Rifampicin red/orange secretions cause staining of:','Contact lenses',['Spectacles','Dentures','Wound drains'],'Rifampicin: secretion (contact lens staining).'),
('Flu-like respiratory symptoms with rifampicin are seen with:','Intermittent dosing',['Daily dosing','Food intake','Overdose only'],'R S/E 2: respiratory symptoms, flu-like (intermittent dosing).'),
('Rifampicin pulmonary syndrome and purpura require:','Stopping the drug permanently',['Reducing the dose','Continuing with antihistamines','Weekly monitoring only'],'R S/E 3-4: pulmonary syndrome + purpura -> stop permanently.'),
('Purpura with rifampicin is due to:','Decreased platelets',['Increased platelets','Vessel wall defect','Factor VIII antibodies'],'R S/E: purpura (decreased platelets).'),
('Rifampicin is an enzyme inducer reducing the effects of other drugs; the induction is least with:','Rifabutin',['Rifampicin itself','Rifapentine','Rifaximin'],'R: enzyme inducer (reduces effects of other drugs) - least with rifabutin.'),
('The side effect of rifabutin is:','Uveitis',['Optic neuritis','Keratitis','Retinopathy'],'Rifabutin S/E: uveitis.'),
('The most hepatotoxic anti-TB drug is:','Pyrazinamide',['Isoniazid','Rifampicin','Ethambutol'],'Z: most hepatotoxic.'),
('The order of hepatotoxicity of anti-TB drugs is:','Z > H > R > E',['H > R > Z > E','R > Z > H > E','E > Z > R > H'],'Most hepatotoxic: Z > H > R > E.'),
('The metabolic side effects of pyrazinamide are:','Hyperuricemia and arthralgia',['Hypouricemia','Hypokalemia','Hypercalcemia'],'Z S/E: hyperuricemia; arthralgia.'),
('The eye toxicity of ethambutol is:','Optic neuritis with red-green colour blindness (green > red)',['Cataract with night blindness','Retinal detachment','Painless ptosis'],'E S/E: eye toxicity - optic neuritis; red green colour blindness (green > red).'),
('In ethambutol colour blindness, the affected order is:','Green more than red',['Red more than green','Blue more than green','Equal for all colours'],'Ethambutol: red green colour blindness (green > red).'),
('The treatment of INH toxicity (seizure) is:','IV pyridoxine 1 g for each gram of INH',['IV pyridoxine 5 g fixed dose','Oral vitamin B6 100 mg','Naloxone infusion'],'Toxicity: seizure - treatment IV pyridoxine 1 g for each gm of INH.'),
('The maximum dose of IV pyridoxine in INH toxicity is:','5 g',['1 g','10 g','15 g'],'Max dose of IV pyridoxine: 5 g.'),
('Rifapentine with INH is used for:','Prophylaxis/latent TB, once weekly',['Daily treatment of MDR TB','XDR TB salvage','Only extrapulmonary TB'],'Other features: rifapentine with INH - use prophylaxis/latent TB; once weekly.'),
])
unit('Second Line Anti-TB Drugs: Groups A, B and C',
 'Second line drugs are used for resistant TB. Group A includes all 3 drugs: levofloxacin or moxifloxacin, bedaquiline and linezolid. Group B includes 1 or both: clofazimine and cycloserine or terizidone. Group C is used when group A or B cannot be added: ethambutol, delamanid, pyrazinamide, imipenem-cilastatin or meropenem, amikacin or streptomycin, ethionamide or prothionamide and PAS.')
facts(195,[
('The use of second-line anti-TB drugs is:','Resistant TB',['New sputum positive TB','Latent TB prophylaxis','Only pediatric TB'],'Second line anti TB drugs: use resistant TB.'),
('Group A of second-line anti-TB drugs includes:','All 3 drugs - levofloxacin or moxifloxacin, bedaquiline and linezolid',['Only the fluoroquinolones','Clofazimine and cycloserine','Ethambutol and delamanid'],'Group A: include all 3 drugs - Lfx or Mfx, Bdq, Lzd.'),
('Group B of second-line anti-TB drugs includes:','1 or both - clofazimine and cycloserine or terizidone',['Bedaquiline and linezolid','Delamanid and PAS','Amikacin and ethionamide'],'Group B: include 1 or both - Clofazimine (Cfz), Cycloserine (Cs) or Terizidone (Trd).'),
('Group C drugs are used when:','Group A or B cannot be added',['Always added first','Only in pregnancy','Only in children under 6 yr'],'Group C: used when group A or B cannot be added.'),
('All of the following are Group C drugs EXCEPT:','Levofloxacin',['Ethambutol','Delamanid','Imipenem-cilastatin'],'Group C: ethambutol, delamanid, pyrazinamide, imipenem-cilastatin or meropenem, amikacin or streptomycin, ethionamide or prothionamide, PAS; levofloxacin is group A.'),
('The injectable antibiotics of Group C are:','Amikacin or streptomycin',['Gentamicin or tobramycin','Vancomycin or teicoplanin','Ceftriaxone or cefixime'],'Group C: amikacin (Am) or streptomycin (S).'),
('Ethionamide or prothionamide and PAS belong to:','Group C',['Group A','Group B','First line drugs'],'Group C: ethionamide (Eto) or prothionamide (Pto); P aminosalicylic acid (PAS).'),
])
unit('New Anti-TB Drugs: Bedaquiline and Nitroimidazoles (Delamanid, Pretomanid)',
 'Bedaquiline inhibits mycobacterial ATP synthase. Nitroimidazoles: delamanid and pretomanid produce free radicals killing non-replicating bacteria and inhibit mycolic acid synthesis killing replicating bacteria. Use: MDR TB (resistance to H + R), pre-XDR (H + R + FQ or any group A) and XDR (H + R + FQ + any group A); drugs should be taken with food for increased absorption. Bedaquiline is sequestered in tissue with long t 1/2 (165 days) allowing intermittent dosing 3 times/weekly, is 99% protein bound metabolized by albumin (C/I if albumin <2.8 mg/dl), metabolized in liver and excreted by kidney. Side effects: QT prolongation with C/I in arrhythmia for bedaquiline and delamanid; bedaquiline is safe in pregnancy while delamanid and pretomanid are not safe.')
facts(195,[
('The new anti-TB drugs are:','Bedaquiline and nitroimidazoles (delamanid, pretomanid)',['Cycloserine and PAS','Ethionamide and prothionamide','Amikacin and capreomycin'],'New drugs table: bedaquiline + nitroimidazoles (delamanid, pretomanid).'),
('The MOA of bedaquiline is:','Inhibits mycobacterial ATP synthase',['Inhibits RNA polymerase','Produces free radicals','Inhibits arabinosyl transferase'],'Bedaquiline MOA: inhibits mycobacterial ATP synthase.'),
('Delamanid kills non-replicating bacteria by:','Producing free radicals',['Inhibiting ATP synthase','Blocking RNA polymerase','Inhibiting folate'],'Nitroimidazoles: produces free radicals - kills non-replicating bacteria.'),
('Delamanid kills replicating bacteria by:','Inhibiting mycolic acid synthesis',['Producing free radicals','ATP synthase block','DNA gyrase block'],'Nitroimidazoles: inhibits mycolic acid synthesis - kills replicating bacteria.'),
('MDR TB is defined as:','Resistance to H + R',['Resistance to H only','Resistance to any 3 drugs','Resistance to FQ + group A'],'Use: MDR TB - resistance to H + R.'),
('Pre-XDR TB is:','Resistance to H + R + FQ or any group A drug',['Resistance to H + R only','H + R + FQ + any group A','Single drug resistance'],'Pre-XDR: resistance to H + R + FQ or any group A.'),
('XDR TB is:','H + R + FQ + any group A drug resistance',['H + R + FQ only','H + R only','MDR + streptomycin'],'XDR: H + R + FQ + any group A.'),
('Bedaquiline, delamanid and pretomanid should be taken:','With food (increased absorption)',['Empty stomach','With milk only','With antacids'],'Advice: drug should be taken with food (increased absorption).'),
('Bedaquiline is sequestered in tissue with a long half life of:','165 days allowing intermittent dosing 3 times/weekly',['24 hours with daily dosing','5 days with weekly dosing','30 days with monthly dosing'],'PK: sequestered in tissue - long t 1/2 (165 days); intermittent dosing 3 times/weekly.'),
('Bedaquiline is 99% bound to plasma proteins and metabolized by albumin; it is contraindicated if albumin is:','<2.8 mg/dl',['<3.5 g/dl','<1.8 g/dl','<5 g/dl'],'PK: plasma protein binding 99% (high), metabolized by albumin -> C/I if albumin <2.8 mg/dl.'),
('The metabolism and excretion of bedaquiline are:','Metabolism liver, excretion kidney',['Both renal','Both biliary','Pulmonary excretion'],'PK: metabolism - liver; excreted - kidney.'),
('The side effects of bedaquiline and delamanid are:','QT prolongation (C/I in arrhythmia)',['Hepatotoxicity only','Nephrotoxicity','Optic neuritis'],'S/E: bedaquiline and delamanid - QT prolongation; C/I in arrhythmia.'),
('Safety of the new anti-TB drugs in pregnancy:','Bedaquiline safe; delamanid and pretomanid not safe',['All three are safe','All three are unsafe','Only pretomanid is safe'],'Pregnancy: bedaquiline safe in pregnancy; delamanid not safe; pretomanid not safe.'),
('The nitroimidazole NOT associated with QT prolongation in the table is:','Pretomanid',['Delamanid','Bedaquiline','None - all three prolong QT'],'S/E row: pretomanid column shows "-"; QT prolongation listed for bedaquiline and delamanid.'),
])
unit('Old Anti-TB Drugs: Ethionamide and PAS',
 'Ethionamide inhibits mycolic acid synthesis (cidal) with side effect of hypothyroidism. Para amino salicylic acid inhibits DHPS (static) and is contraindicated with rifampicin due to decreased absorption.')
facts(196,[
('The old anti-TB drugs are:','Ethionamide and para amino salicylic acid',['Cycloserine and terizidone','Amikacin and capreomycin','Rifabutin and rifapentine'],'Old drugs: ethionamide; para amino salicylic acid.'),
('The MOA of ethionamide is:','Inhibits mycolic acid synthesis (cidal)',['Inhibits DHPS (static)','Inhibits RNA polymerase','Inhibits arabinosyl transferase'],'Ethionamide MOA: inhibits mycolic acid synthesis (cidal).'),
('The side effect of ethionamide is:','Hypothyroidism',['Hyperthyroidism','Optic neuritis','Nephrotoxicity'],'Ethionamide S/E: hypothyroidism.'),
('The MOA of para amino salicylic acid is:','Inhibits DHPS (static)',['Inhibits mycolic acid synthesis (cidal)','Inhibits RNA polymerase','Inhibits pyrazinamidase'],'PAS MOA: inhibits DHPS (static).'),
('PAS is contraindicated with rifampicin because of:','Decreased absorption',['Increased hepatotoxicity','Antagonism at DHPS','Enzyme induction'],'PAS C/I: with rifampicin (decreased absorption).'),
])
unit('Drug Regimens for TB',
 'New/previously treated case: HRZE 2 months intensive + HRE 4 months continuous. Rifampicin resistant or MDR TB: shorter oral bedaquiline-containing regimen - Bdq 6 months with Lfx, Cfz, Z, E, H, Eto for 4-6 months, then Lfx, Cfz, Z, E for 5 months (months 4 and 5-6 add Bdq with high dose H and Eto; months 7-9 Lfx, Cfz, Z, E). Alternative shorter injectable regimen: Mfx, Km/Am, Eto, Cfz, Z, H, E (4-6 months) then Mfx, Cfz, Z, E (5 months). Long oral MDR/XDR regimen: Bdq 6 months + Lfx, Lzd, Cfz, Cs for 18-20 months. BPaL (pilot) for MDR TB with FQ resistance: pretomanid 200 mg OD daily x 26 weeks; bedaquiline 400 mg OD for first week then 200 mg three times a week for 24 weeks; linezolid 1200 mg once daily for 24 weeks.')
facts(196,[
('The regimen for a new/previously treated TB case is:','HRZE 2 months (intensive) + HRE 4 months (continuous)',['HRE 6 months total','HRZE 6 months continuous','HZ 4 months + HRE 2 months'],'New/previously treated case: intensive HRZE 2 months; continuous HRE 4 months.'),
('The intensive phase for a new TB case is:','HRZE for 2 months',['HRE for 2 months','HRZE for 4 months','HZE for 6 months'],'Intensive phase: HRZE (2 months).'),
('The continuous phase for a new TB case is:','HRE for 4 months',['HRZE for 4 months','HRE for 2 months','HRZ for 6 months'],'Continuous phase: HRE (4 months).'),
('The shorter oral bedaquiline-containing regimen is used for:','Rifampicin resistant or MDR TB',['New pulmonary TB','Latent TB','XDR TB only'],'Shorter oral bedaquiline containing regimen: rifampicin resistant or MDR TB.'),
('The intensive phase of the shorter oral bedaquiline regimen is:','Bdq (6 months) + Lfx, Cfz, Z, E, H, Eto (4-6 months)',['Bdq 2 months alone','Injection for 6 months','Lfx alone 6 months'],'Intensive: Bdq (6 months); Lfx, Cfz, Z, E, H, Eto (4-6 months).'),
('The continuous phase of the shorter oral bedaquiline regimen is:','Lfx, Cfz, Z, E (5 months)',['HRE 4 months','Bdq 5 months','Eto 5 months'],'Continuous phase: Lfx, Cfz, Z, E (5 months).'),
('In the shorter oral bedaquiline regimen, till 4 months and months 5-6 the drugs are:','Lfx, Cfz, Z, E, Bdq with high doses H, Eto; then months 5-6 Lfx, Cfz, Z, E, Bdq',['Bdq alone till 6 months','Injections till 6 months','High dose H alone'],'Till 4 months: Lfx, Cfz, Z, E, Bdq + high doses H, Eto; 5th & 6th months: Lfx, Cfz, Z, E, Bdq.'),
('In the shorter oral bedaquiline regimen, months 7 to 9 include:','Lfx, Cfz, Z, E',['Bdq continues till 9 months','High dose H and Eto','Km/Am injections'],'7th till 9th months: Lfx, Cfz, Z, E.'),
('The alternative shorter injectable containing regimen includes:','Mfx, Km/Am, Eto, Cfz, Z, H, E (4-6 months) then Mfx, Cfz, Z, E (5 months)',['Bdq 6 months + 5 months','PAS + Cs for 9 months','Lzd 6 months only'],'Shorter injectable containing regimen (alternative): intensive Mfx, Km/Am, Eto, Cfz, Z, H, E (4-6 month); continuous Mfx, Cfz, Z, E (5 months).'),
('The long oral MDR/XDR regimen is:','Bdq (6 months) + Lfx, Lzd, Cfz, Cs (18-20 months)',['9 months HRZE','6 months Bdq alone','24-30 months injections'],'Long oral MDR/XDR regimen: Bdq (6 months) + Lfx, Lzd, Cfz, Cs (18-20 months).'),
('The BPaL regimen (pilot) is used for:','MDR TB with FQ resistance',['New TB cases','Latent TB','XDR TB only'],'BPaL regimen (pilot): MDR TB with FQ resistance.'),
('In BPaL, the dose of pretomanid is:','200 mg OD daily for 26 weeks',['400 mg daily for 24 weeks','200 mg three times a week','600 mg weekly'],'BPaL: pretomanid 200 mg OD daily for 26 weeks.'),
('In BPaL, the dose of bedaquiline is:','400 mg OD daily for the first week, then 200 mg three times a week for 24 weeks',['400 mg throughout 26 weeks','200 mg daily for 26 weeks','200 mg weekly for 24 weeks'],'BPaL: bedaquiline 400 mg OD daily for the first week of treatment; 200 mg three times a week for 24 weeks.'),
('In BPaL, the dose of linezolid is:','1200 mg once daily for 24 weeks',['600 mg once daily for 26 weeks','1200 mg weekly','300 mg daily for 6 months'],'BPaL: linezolid 1200 mg once daily for 24 weeks.'),
])
unit('Anti-Leprosy Drugs: First Line, Second Line and Lepra Reaction',
 'First line: rifampicin (most cidal), dapsone (DHPS inhibitor, static, S/E hemolysis in G6PD deficiency - most common) and clofazimine (free radical production; cidal in TB but static in leprosy; S/E ichthyosis and crystal deposition in GIT mucosa). Second line: clarithromycin and minocycline (static); fluoroquinolones ofloxacin and moxifloxacin (cidal). Lepra reaction type 1: DOC steroids; type 2: DOC steroids with alternatives clofazimine and thalidomide (most effective).')
facts(197,[
('The first line anti-leprosy drugs are:','Rifampicin, dapsone and clofazimine',['Clarithromycin, minocycline and ofloxacin','Thalidomide and steroids','Ethionamide and PAS'],'First line: 1. rifampicin, 2. dapsone, 3. clofazimine.'),
('The most cidal anti-leprosy drug is:','Rifampicin',['Dapsone','Clofazimine','Minocycline'],'First line: rifampicin - most cidal.'),
('Dapsone is a:','DHPS inhibitor and static drug',['RNA polymerase inhibitor, cidal','Free radical producer','ATP synthase inhibitor'],'Dapsone: DHPS inhibitor; static drug.'),
('The most common side effect of dapsone is:','Hemolysis in G6PD deficiency',['Methemoglobinemia only','Optic neuritis','Gray baby syndrome'],'Dapsone S/E: hemolysis in G6PD deficiency (m/c).'),
('The MOA of clofazimine is:','Free radical production',['DHPS inhibition','RNA polymerase inhibition','ATP synthase inhibition'],'Clofazimine MOA: free radical production.'),
('Clofazimine in TB is:','Cidal',['Static','Inactive','Bacteriolytic only'],'Clofazimine: in TB - cidal effect.'),
('Clofazimine in leprosy is:','Static',['Cidal','Sterilizing','Fungicidal'],'Clofazimine: in leprosy - static effect.'),
('The side effects of clofazimine are:','Ichthyosis and deposition of crystals in GIT mucosa',['Hemolysis and methemoglobinemia','Gray baby syndrome','Optic neuritis'],'Clofazimine S/E: ichthyosis; deposition of crystals in GIT mucosa.'),
('The second line static anti-leprosy drugs are:','Clarithromycin and minocycline',['Ofloxacin and moxifloxacin','Dapsone and clofazimine','Rifampicin and ethambutol'],'Second line: clarithromycin, minocycline - static.'),
('The cidal fluoroquinolones used in leprosy are:','Ofloxacin and moxifloxacin',['Ciprofloxacin and norfloxacin','Levofloxacin and gemifloxacin','Pefloxacin only'],'Second line 3. FQ: ofloxacin, moxifloxacin - cidal.'),
('The DOC for type 1 lepra reaction is:','Steroids',['Thalidomide','Clofazimine','NSAIDs'],'Lepra reaction type 1: DOC steroids.'),
('The DOC for type 2 lepra reaction is:','Steroids',['Thalidomide','Dapsone','Antihistamines'],'Lepra reaction type 2: DOC steroids.'),
('The alternative drugs for type 2 lepra reaction are:','Clofazimine and thalidomide (most effective)',['Steroids alone','Minocycline and ofloxacin','Rifampicin rechallenge'],'Type 2 alternative drugs: clofazimine; thalidomide (most effective).'),
('The most effective drug for type 2 lepra reaction is:','Thalidomide',['Clofazimine','Steroids','Dapsone'],'Alternative drugs for type 2: thalidomide (most effective).'),
])
unit('WHO Guidelines for Leprosy Treatment and Drug Resistance',
 'Supervised doses (once a month): adults rifampicin 600 mg + clofazimine 300 mg; children 10-14 years rifampicin 450 mg + clofazimine 150 mg; children <14 years or <40 kg rifampicin 10 mg/kg + clofazimine 6 mg/kg. Non-supervised (once a day): adults dapsone 100 mg + clofazimine 50 mg; children 10-14 years dapsone 50 mg + clofazimine 50 mg alternate day; small children dapsone 2 mg/kg + clofazimine 1 mg/kg. Rifampicin resistance regimens (daily): first 6 months ofloxacin 400 mg + minocycline 100 mg + clofazimine 50 mg (or with clarithromycin 500 mg); next 18 months ofloxacin 400 mg or minocycline 100 mg + clofazimine 50 mg. Rifampicin + ofloxacin resistance: clarithromycin 500 mg + minocycline 100 mg + clofazimine 50 mg.')
facts(197,[
('In WHO leprosy guidelines, supervised doses are given:','Once a month',['Once a day','Once a week','Twice a week'],'WHO guidelines: supervised (once a month).'),
('Non-supervised leprosy doses are given:','Once a day',['Once a month','Once a week','Alternate weeks'],'WHO guidelines: non-supervised (once a day).'),
('The supervised adult leprosy doses are:','Rifampicin 600 mg + clofazimine 300 mg',['Rifampicin 450 mg + clofazimine 150 mg','Dapsone 100 mg + clofazimine 50 mg','Rifampicin 10 mg/kg + clofazimine 6 mg/kg'],'Supervised adults: rifampicin 600 mg, clofazimine 300 mg.'),
('The supervised doses for children 10-14 years are:','Rifampicin 450 mg + clofazimine 150 mg',['Rifampicin 600 mg + clofazimine 300 mg','Rifampicin 10 mg/kg + clofazimine 6 mg/kg','Dapsone 100 mg + clofazimine 50 mg'],'Children 10-14 years: rifampicin 450 mg, clofazimine 150 mg.'),
('The supervised doses for children <14 years or <40 kg are:','Rifampicin 10 mg/kg + clofazimine 6 mg/kg',['Rifampicin 450 mg fixed dose','Dapsone 100 mg + clofazimine 50 mg','Rifampicin 600 mg + clofazimine 300 mg'],'Children <14 years or <40 kg: rifampicin 10 mg/kg, clofazimine 6 mg/kg.'),
('The non-supervised adult leprosy doses are:','Dapsone 100 mg + clofazimine 50 mg',['Rifampicin 600 mg daily','Dapsone 50 mg alone','Clofazimine 300 mg daily'],'Non-supervised adults: dapsone 100 mg, clofazimine 50 mg.'),
('The non-supervised doses for children 10-14 years are:','Dapsone 50 mg + clofazimine 50 mg (alternate day)',['Dapsone 100 mg daily','Clofazimine 150 mg daily','Rifampicin 450 mg monthly'],'Children 10-14 years: dapsone 50 mg + clofazimine 50 mg (alternate day).'),
('The non-supervised doses for children <14 years or <40 kg are:','Dapsone 2 mg/kg + clofazimine 1 mg/kg',['Dapsone 50 mg fixed','Clofazimine 6 mg/kg','Rifampicin 10 mg/kg daily'],'Children <14 yr or <40 kg: dapsone 2 mg/kg, clofazimine 1 mg/kg.'),
('In rifampicin-resistant leprosy, the first 6 months daily regimen is:','Ofloxacin 400 mg + minocycline 100 mg + clofazimine 50 mg (or ofloxacin 400 mg + clarithromycin 500 mg + clofazimine 50 mg)',['Dapsone + rifampicin daily','Thalidomide + steroids','Ofloxacin alone'],'Rifampicin resistance, first 6 months (daily): ofloxacin 400 mg + minocycline 100 mg + clofazimine 50 mg / ofloxacin 400 mg + clarithromycin 500 mg + clofazimine 50 mg.'),
('In rifampicin-resistant leprosy, the next 18 months daily regimen is:','Ofloxacin 400 mg or minocycline 100 mg + clofazimine 50 mg (or ofloxacin 400 mg + clofazimine 50 mg)',['All three drugs continue unchanged','Rifampicin is rechallenged','Dapsone monotherapy'],'Next 18 months (daily): ofloxacin 400 mg or minocycline 100 mg + clofazimine 50 mg / ofloxacin 400 mg + clofazimine 50 mg.'),
('In rifampicin and ofloxacin resistant leprosy, the regimen is:','Clarithromycin 500 mg + minocycline 100 mg + clofazimine 50 mg (daily), then clarithromycin 500 mg or minocycline 100 mg + clofazimine 50 mg',['Ofloxacin is continued','Rifampicin is rechallenged','Dapsone + clofazimine'],'Rifampicin and ofloxacin resistance: first 6 months clarithromycin 500 mg + minocycline 100 mg + clofazimine 50 mg; next 18 months clarithromycin 500 mg or minocycline 100 mg + clofazimine 50 mg.'),
])
unit('Drugs for Mycobacterium Avium Complex',
 'The MAC regimen uses the mnemonic EAR: ethambutol, azithromycin and rifampicin. Azithromycin can be used even in macrolide resistance because of its immunomodulator effect.')
facts(198,[
('The regimen for Mycobacterium avium complex uses the mnemonic:','EAR',['MAC','EARS','ERA'],'Regimen mnemonic: EAR.'),
('The drugs in the MAC regimen are:','Ethambutol, azithromycin and rifampicin',['Clarithromycin, amikacin and ethambutol','Isoniazid, pyrazinamide and ethambutol','Dapsone, clofazimine and minocycline'],'EAR: ethambutol, azithromycin, rifampicin.'),
('Azithromycin can be used in macrolide resistance due to:','Immunomodulator effect',['Higher ribosomal affinity','Renal excretion','Dose escalation'],'Azithromycin: can be used in macrolide resistance - immunomodulator effect.'),
('The drug NOT part of the EAR regimen for MAC is:','Clarithromycin',['Ethambutol','Azithromycin','Rifampicin'],'MAC mnemonic EAR: ethambutol, azithromycin, rifampicin - no clarithromycin.'),
])
finish()

# CHAPTER 49 - ANTI-PROTOZOAL DRUGS (p199-204) ---------------------------------
start(49)
unit('Amoebiasis: Classification and Drug Choice',
 'Amoebiasis is divided into intestinal (asymptomatic and symptomatic) and extra-intestinal (hepatic). Asymptomatic disease is treated with luminal amoebicidal drugs acting within the lumen - diloxanide furoate, iodoquinol and paromomycin (DOC) - with the aim of radical cure. Symptomatic and extra-intestinal disease uses nitazoxanide, emetine and metronidazole (DOC); chloroquine is used only for hepatic amoebiasis.')
facts(199,[
('Amoebiasis is classified into:','Intestinal and extra-intestinal (hepatic)',['Acute and chronic only','Luminal and blood forms only','Cyst passers and carriers only'],'Diagram: intestinal (asymptomatic, symptomatic) and extra-intestinal (hepatic).'),
('Intestinal amoebiasis is of two types:','Asymptomatic and symptomatic',['Hepatic and pulmonary','Fulminant and chronic','Invasive and non-invasive'],'Intestinal: asymptomatic, symptomatic.'),
('Asymptomatic intestinal amoebiasis is treated with:','Luminal amoebicidal drugs (act within lumen)',['Tissue amoebicides only','Chloroquine','Emetine'],'Asymptomatic: drugs - luminal amoebicidal drugs (act within lumen).'),
('The DOC for asymptomatic (luminal) amoebiasis is:','Paromomycin',['Diloxanide furoate','Iodoquinol','Metronidazole'],'Luminal drugs: diloxanide furoate, iodoquinol, paromomycin (DOC).'),
('The luminal amoebicidal drugs are:','Diloxanide furoate, iodoquinol and paromomycin',['Metronidazole, emetine and nitazoxanide','Chloroquine and emetine','Tinidazole and secnidazole'],'Luminal amoebicidal drugs: diloxanide furoate, iodoquinol, paromomycin (DOC).'),
('The aim of luminal amoebicidal drugs is:','Radical cure',['Symptom relief only','Suppression of cysts during flare','Prophylaxis in contacts'],'Aim: radical cure.'),
('The drugs for symptomatic intestinal and extra-intestinal amoebiasis are:','Nitazoxanide, emetine and metronidazole (DOC)',['Diloxanide furoate and iodoquinol','Chloroquine and paromomycin','Paromomycin and iodoquinol'],'Symptomatic + extra-intestinal drugs: nitazoxanide, emetine, metronidazole (DOC).'),
('The DOC for symptomatic amoebiasis is:','Metronidazole',['Emetine','Nitazoxanide','Tinidazole'],'Symptomatic drugs: metronidazole (DOC).'),
('Chloroquine in amoebiasis is used only for:','Hepatic (extra-intestinal) amoebiasis',['Intestinal amoebiasis','Luminal cyst carriage','All forms of amoebiasis'],'Extra-intestinal: chloroquine (only for hepatic).'),
])
unit('Nitroimidazoles',
 'Nitroimidazoles are tinidazole (DOC in western countries), satranidazole, secnidazole, benznidazole and metronidazole (DOC in India). MOA is free radical production; TOC for amoebiasis is metronidazole followed by (f/b) paromomycin. They are DOC in giardiasis, amoebiasis, anaerobes (infra diaphragmatic), tetanus, trichomoniasis and bacterial vaginosis. Side effects: disulfiram-like reaction (C/I with alcohol) and red-brown urine. Note: cefazolin + metronidazole is the surgical prophylaxis for infra-diaphragmatic surgery; bacterial vaginosis shows clue cells in foul-smelling, dirty white discharge.')
facts(199,[
('The nitroimidazole drugs are:','Tinidazole, satranidazole, secnidazole, benznidazole and metronidazole',['Metronidazole and nimorazole only','Tinidazole and ornidazole only','Diloxanide and iodoquinol'],'Nitroimidazole drugs: tinidazole, satranidazole, secnidazole, benznidazole, metronidazole.'),
('The DOC for amoebiasis in western countries is:','Tinidazole',['Metronidazole','Secnidazole','Satranidazole'],'Tinidazole: DOC in western countries.'),
('The DOC for amoebiasis in India is:','Metronidazole',['Tinidazole','Benznidazole','Satranidazole'],'Metronidazole: DOC in India.'),
('The MOA of nitroimidazoles is:','Free radical production',['Folate synthesis block','Direct membrane pore formation','RNA polymerase inhibition'],'Nitroimidazole MOA: free radical production.'),
('The TOC (treatment of choice) course for amoebiasis with nitroimidazoles is:','Metronidazole followed by (f/b) paromomycin',['Metronidazole alone','Paromomycin followed by metronidazole','Tinidazole then chloroquine'],'TOC for amoebiasis: metronidazole f/b paromomycin.'),
('Nitroimidazoles are the DOC in all EXCEPT:','Ascariasis',['Trichomoniasis','Giardiasis','Bacterial vaginosis'],'Uses (DOC in): giardiasis, amoebiasis, anaerobes, tetanus, trichomoniasis, bacterial vaginosis.'),
('Nitroimidazoles are DOC for anaerobes which are:','Infra diaphragmatic',['Supra diaphragmatic','Both supra and infra','Only in blood'],'Uses: anaerobes (infra diaphragmatic).'),
('Nitroimidazoles are also DOC in:','Tetanus',['Tetany','Botulism','Diphtheria'],'Uses: DOC in tetanus.'),
('The side effects of nitroimidazoles are:','Disulfiram-like reaction (C/I with alcohol) and red-brown urine',['Green urine and neuropathy','Gray baby syndrome','Optic neuritis'],'S/E: disulfiram-like reaction (C/I with alcohol); red-brown urine.'),
('The prophylaxis for infra-diaphragmatic surgery is:','Cefazolin + metronidazole',['Cefazolin alone','Metronidazole alone','Vancomycin + metronidazole'],'Note: cefazolin + metronidazole - surgical prophylaxis (infra diaphragm).'),
('Bacterial vaginosis shows clue cells in:','Foul-smelling, dirty white discharge',['Curdy white discharge','Green frothy discharge','Clear mucoid discharge'],'Note: bacterial vaginosis - clue cells in foul-smelling, dirty white discharge.'),
('A patient on metronidazole must avoid:','Alcohol',['Milk','Antacids','Green leafy vegetables'],'Nitroimidazole S/E: disulfiram-like reaction - C/I with alcohol.'),
])
unit('Leishmaniasis',
 'Visceral leishmaniasis (kala azar): IV DOC is liposomal amphotericin B (LAmB, decreased nephrotoxicity); oral DOC is miltefosine which is also the DOC for post-kala azar dermal leishmaniasis; its side effects are nausea, vomiting and diarrhea and it is contraindicated in pregnancy (teratogenic). Alternatives: paromomycin, pentamidine and sitamaquine. Cutaneous leishmaniasis DOC: sodium stibogluconate with alternatives LAmB, paromomycin and pentamidine.')
facts(200,[
('Leishmaniasis is classified into:','Visceral (kala azar) and cutaneous',['Mucocutaneous and visceral only','Cutaneous and diffuse cutaneous only','Oriental sore and dumb forms only'],'Diagram: visceral (kala azar) and cutaneous.'),
('The IV DOC for visceral leishmaniasis (kala azar) is:','Liposomal amphotericin B (LAmB)',['Conventional amphotericin B','Miltefosine','Sodium stibogluconate'],'Kala azar IV DOC: liposomal amphotericin B (decreased nephrotoxicity).'),
('The oral DOC for visceral leishmaniasis is:','Miltefosine',['Paromomycin','Sitamaquine','Pentamidine'],'Kala azar oral DOC: miltefosine.'),
('Miltefosine is also the DOC for:','Post-kala azar dermal leishmaniasis',['Cutaneous leishmaniasis','Mucocutaneous leishmaniasis only','African trypanosomiasis'],'Miltefosine: also DOC for post-kala azar dermal leishmaniasis.'),
('The side effects of miltefosine are:','Nausea & vomiting and diarrhea',['Nephrotoxicity and hypokalemia','Cardiotoxicity and flushing','Hepatotoxicity only'],'Miltefosine S/E: nausea & vomiting; diarrhea.'),
('Miltefosine is contraindicated in:','Pregnancy (teratogenic effect)',['Lactation only','Children only','Elderly only'],'Miltefosine C/I: pregnancy (D/t teratogenic effect).'),
('The DOC for cutaneous leishmaniasis is:','Sodium stibogluconate',['Liposomal amphotericin B','Miltefosine','Pentamidine'],'Cutaneous leishmaniasis DOC: sodium stibogluconate.'),
('The alternatives for cutaneous leishmaniasis are:','LAmB, paromomycin and pentamidine',['Sodium stibogluconate and miltefosine only','Chloroquine and emetine','Sitamaquine only'],'Cutaneous alternatives: LAmB, paromomycin, pentamidine.'),
('The alternative drugs for visceral leishmaniasis are:','Paromomycin, pentamidine and sitamaquine',['Sodium stibogluconate and miltefosine','Chloroquine and emetine','Amphotericin B deoxycholate only'],'Kala azar alternatives: paromomycin, pentamidine, sitamaquine.'),
])
unit('Trypanosomiasis',
 'African trypanosomiasis (sleeping sickness): East African early - IV suramin, late - IV melarsoprol; West African early - IV pentamidine, late - IV eflornithine, with oral fexinidazole (approved 2019) as the cheaper, easier alternative. American trypanosomiasis (Chagas disease): DOC benznidazole, alternative nifurtimox.')
facts(200,[
('African trypanosomiasis is also called:','Sleeping sickness',['Chagas disease','Kala azar','River blindness'],'African trypanosomiasis = sleeping sickness.'),
('American trypanosomiasis is:','Chagas disease',['Sleeping sickness','Leishmaniasis','Babesiosis'],'American trypanosomiasis = Chagas disease.'),
('The DOC for American trypanosomiasis (Chagas disease) is:','Benznidazole',['Nifurtimox','Suramin','Pentamidine'],'Chagas DOC: benznidazole.'),
('The alternative drug for Chagas disease is:','Nifurtimox',['Suramin','Melarsoprol','Eflornithine'],'Chagas alternative: nifurtimox.'),
('Early East African sleeping sickness is treated with:','IV suramin',['IV melarsoprol','IV pentamidine','IV eflornithine'],'East African early: I/V suramin.'),
('Late East African sleeping sickness is treated with:','IV melarsoprol',['IV suramin','IV eflornithine','Oral fexinidazole'],'East African late: I/V melarsoprol.'),
('Early West African sleeping sickness is treated with:','IV pentamidine',['IV suramin','IV melarsoprol','Oral benznidazole'],'West African early: I/V pentamidine.'),
('Late West African sleeping sickness is treated with:','IV eflornithine',['IV pentamidine','IV suramin','IV melarsoprol'],'West African late: I/V eflornithine.'),
('The approved oral alternative for West African trypanosomiasis is:','Fexinidazole (approved 2019) - cheaper, easier',['Nifurtimox','Benznidazole','Suramin'],'West African: oral fexinidazole (approved 2019) - cheaper, easier alternative.'),
('Melarsoprol is used in:','Late East African sleeping sickness',['Early West African disease','Chagas disease','Visceral leishmaniasis'],'East African late: I/V melarsoprol (arsenical used in late stage).'),
])
unit('Cryptosporidiasis, Nitazoxanide Spectrum and Babesiosis',
 'Cryptosporidiasis DOC is nitazoxanide, derived from niclosamide (an anti-helminthic); MOA is inhibition of PFOR enzyme blocking electron transport. Nitazoxanide spectrum covers anti-protozoal, anti-helminthic, anti-bacterial and anti-viral; side effect green urine; other uses - DOC in resistant giardiasis and off-label in H. pylori infection (due to resistance to macrolides). Babesiosis TOC for mild, moderate and severe: atovaquone + azithromycin; the earlier TOC was quinine + clindamycin for mild-moderate and atovaquone + azithromycin for severe.')
facts(200,[
('The DOC for cryptosporidiasis is:','Nitazoxanide',['Metronidazole','Paromomycin','Albendazole'],'Cryptosporidiasis: nitazoxanide (DOC).'),
('Nitazoxanide is derived from:','Niclosamide (anti-helminthic drug)',['Metronidazole','Chloramphenicol','Furazolidone'],'Nitazoxanide source: niclosamide (anti-helminthic drug).'),
('The MOA of nitazoxanide is:','Inhibits PFOR enzyme -> blocks electron transport',['Produces free radicals','Inhibits DHFR','Blocks microtubules'],'MOA: inhibits PFOR enzyme -> blocks electron transport.'),
('The spectrum of nitazoxanide is:','Anti-protozoal, anti-helminthic, anti-bacterial and anti-viral',['Only anti-protozoal','Only anti-bacterial','Anti-fungal and anti-viral only'],'Spectrum: anti-protozoal, anti-helminthic, anti-bacterial, anti-viral.'),
('The side effect of nitazoxanide is:','Green urine',['Red urine','Red-brown urine','Blue-green urine'],'Nitazoxanide S/E: green urine.'),
('Nitazoxanide is the DOC in resistant:','Giardiasis',['Trichomoniasis','Amoebiasis','Cryptosporidiasis alone'],'Other uses: DOC in resistant giardiasis.'),
('The off-label use of nitazoxanide is:','H. pylori infection (due to resistance to macrolides)',['Tuberculosis','Kala azar','Chagas disease'],'Off label use: H. pylori infection (D/t resistance to macrolides).'),
('The TOC for babesiosis for mild, moderate and severe disease is:','Atovaquone + azithromycin',['Quinine + clindamycin','Artemether + lumefantrine','Chloroquine + primaquine'],'Babesiosis TOC: atovaquone + azithromycin (for mild, moderate & severe).'),
('The earlier TOC for mild to moderate babesiosis was:','Quinine + clindamycin',['Atovaquone + azithromycin','Doxycycline + quinine','Pentamidine'],'Earlier TOC: mild to moderate - quinine + clindamycin.'),
('The earlier TOC for severe babesiosis was:','Atovaquone + azithromycin',['Quinine + clindamycin','Melarsoprol','Suramin'],'Earlier TOC: severe - atovaquone + azithromycin.'),
])
unit('Life Cycle of Plasmodium within the Human Body',
 'Mosquito bites inject sporozoites (the infective form for humans) which travel via the blood stream and enter the liver. The hepatic schizont can remain dormant (hypnozoite) or replicate and rupture to release merozoites; merozoites infect RBCs where erythrocytic schizonts replicate, rupture and produce symptoms (increased fever, chills). Merozoites also form gametocytes (the infective form for mosquito) which are taken up by the mosquito during an integrated blood meal.')
facts(201,[
('The infective form of plasmodium for humans is:','Sporozoites',['Merozoites','Gametocytes','Hypnozoites'],'Diagram: sporozoites (infective form for humans).'),
('Sporozoites reach the liver:','Via the blood stream',['Through lymphatics','Across the gastric mucosa directly','Via the CSF'],'Diagram: travels via blood stream -> enters liver.'),
('The hepatic schizont in vivax and ovale can:','Remain dormant as hypnozoite (replicates later)',['Rupture immediately always','Form gametocytes in liver','Be killed by chloroquine'],'Diagram: hepatic schizont - dormancy (hypnozoite) and replicates.'),
('The dormant hepatic stage of plasmodium is called:','Hypnozoite',['Merozoite','Oocyst','Sporoblast'],'Diagram label: hypnozoite (dormant in liver).'),
('Rupture of the liver schizont releases:','Merozoites',['Sporozoites','Gametocytes','Hypnozoites'],'Diagram: liver (ruptures) -> merozoites.'),
('Merozoites infect:','RBCs',['Liver cells','WBCs','Endothelial cells'],'Diagram: merozoites infect RBC.'),
('Rupture of erythrocytic schizonts produces:','Symptoms with increased fever and chills',['Gametocytes only','Hypnozoites','Cure of infection'],'Diagram: erythrocytic schizont rupture -> symptoms (increased fever, chills).'),
('The infective form of plasmodium for the mosquito is:','Gametocytes',['Sporozoites','Merozoites','Hypnozoites'],'Diagram: gametocytes (infective form for mosquito).'),
('Gametocytes are taken up by the mosquito during:','Integrated blood meal',['Salivary contact only','Water contact','A second bite after maturation'],'Diagram: gametocytes -> integrated blood meal -> mosquito.'),
])
unit('Stages of Drug Action in Malaria',
 'Hypnozoiticidal drugs (primaquine x 14 days, tafenoquine single dose) prevent relapse; with treatment they give radical cure and act as terminal prophylaxis; hypnozoites are seen only in vivax and ovale. Gametocidal drugs block transmission of malaria - primaquine and the artemisinin group. Erythrocytic schizontocidal drugs are fast acting (DOC) and slow acting; the treatment regimen is 1 fast acting + 1 slow acting drug.')
facts(202,[
('Hypnozoiticidal drugs prevent:','Relapse',['Transmission','Recrudescence','Initial infection'],'Hypnozoiticidal drugs: prevents relapse.'),
('The hypnozoiticidal regimens are:','Primaquine x 14 days or tafenoquine single dose',['Chloroquine x 3 days','Mefloquine weekly x 4 weeks','Quinine x 7 days'],'Hypnozoiticidal: primaquine x 14 days; tafenoquine: single dose.'),
('Hypnozoiticidal drugs along with treatment produce:','Radical cure and terminal prophylaxis',['Only suppression of symptoms','Transmission block only','Causal prophylaxis only'],'Along with treatment: radical cure; terminal prophylaxis.'),
('Hypnozoites are seen only in:','Vivax and ovale',['Falciparum and malariae','All species','Falciparum only'],'Hypnozoite seen only in: vivax, ovale.'),
('Gametocidal drugs block:','Transmission of malaria',['Relapse of malaria','Hepatic schizogony','Sporozoite inoculation'],'Gametocidal drugs: blocks transmission of malaria.'),
('The gametocidal drugs are:','Primaquine and artemisinin group of drugs',['Chloroquine and quinine','Mefloquine and lumefantrine','Sulfadoxine and pyrimethamine'],'Gametocidal: primaquine; artemisinin group of drugs.'),
('Erythrocytic schizontocidal drugs are divided into:','Fast acting (DOC) and slow acting',['Cidal and static','Hepatic and erythrocytic','Monotherapy and combination only'],'Erythrocytic schizontocidal: fast acting (DOC) and slow acting.'),
('The regimen for treatment of malaria is:','1 fast acting + 1 slow acting drug',['2 fast acting drugs','Slow acting drug alone','Fast acting drug alone always'],'Regimen for treatment of malaria: 1 fast acting + 1 slow acting.'),
])
unit('Artemisinin Group',
 'Artemisinins are the most potent and fastest acting schizontocidal drugs with MOA of free radical production; they are contraindicated in the first trimester of pregnancy. Artesunate is IV and oral; artemether and dihydroartemisinin are only oral. Because they are short acting they cannot be used as monotherapy or for prophylaxis. Uses: severe falciparum malaria (DOC - continuous IV infusion artesunate for 48 hr followed by treatment regimen) and uncomplicated malaria.')
facts(202,[
('The most potent and fastest acting schizontocidal drugs are:','Artemisinin group',['Chloroquine','Quinine','Mefloquine'],'Artemisinin group: most potent and fastest acting schizontocidal drugs.'),
('The MOA of artemisinins is:','Free radical production',['Folate pathway block','Haem polymerization inhibition only','Electron transport block in liver'],'MOA: free radical production (C/I in 1st trimester of pregnancy).'),
('Artemisinins are contraindicated in:','1st trimester of pregnancy',['2nd trimester','Lactation','Children above 5 yr'],'MOA note: free radical production (C/I in 1st trimester of pregnancy).'),
('The routes of artesunate are:','I/V and oral',['Only oral','Only I/M','Only rectal'],'Artesunate: I/V & oral.'),
('The artemisinins that are only oral are:','Artemether and dihydroartemisinin',['Artesunate only','All three are oral','None - all are parenteral'],'Artemether, dihydroartemisinin: only oral.'),
('The disadvantage of the artemisinin group is:','Short acting - cannot be used as monotherapy and cannot be used for prophylaxis',['Cannot be given by any route in children','Cannot be combined with any drug','Cannot be used in vivax'],'Disadvantage (D/t short acting): cannot be used as monotherapy; cannot be used for prophylaxis.'),
('The DOC for severe falciparum malaria is:','Continuous IV infusion artesunate for 48 hr followed by treatment regimen',['IV quinine for 48 hours','IM artemether single dose','Oral artemether-lumefantrine'],'Severe falciparum malaria: DOC - continuous I/V infusion artesunate for 48 hr (followed by treatment regimen).'),
('The uses of the artemisinin group are:','Severe falciparum malaria and uncomplicated malaria',['Only severe malaria','Prophylaxis of malaria','Radical cure of vivax'],'Uses: severe falciparum malaria; uncomplicated malaria.'),
])
unit('Treatment of Uncomplicated Malaria',
 'Vivax malaria TOC: chloroquine (DOC) x 3 days + primaquine x 14 days / tafenoquine single dose; primaquine/tafenoquine in pregnancy are given post-partum (not safe in pregnancy). Chloroquine resistant vivax: pregnant female 1st trimester - quinine (DOC) + clindamycin, 2nd and 3rd trimester - ACT; normal population - ACT or quinine + one of tetracycline/doxycycline (not safe in pregnancy) or clindamycin. ACT options: oral artesunate + sulfadoxine + pyrimethamine (all Indian states) or oral artemether + lumefantrine (north-eastern states). Falciparum malaria TOC: ACT.')
facts(203,[
('The TOC for vivax malaria is:','Chloroquine (DOC) x 3 days + primaquine x 14 days / tafenoquine single dose',['ACT alone for 3 days','Quinine + doxycycline','Chloroquine alone for 14 days'],'Vivax TOC: chloroquine (DOC) x 3 d + primaquine x 14 d / tafenoquine single dose.'),
('Primaquine/tafenoquine in a pregnant woman with vivax malaria:','Given post-partum (not safe in pregnancy)',['Given in the first trimester only','Given with folic acid throughout','Safe at all gestations'],'Pregnant: given post-partum (not safe).'),
('In chloroquine resistant vivax malaria, a pregnant female in the 1st trimester is treated with:','Quinine (DOC) + clindamycin',['ACT','Mefloquine + tetracycline','Primaquine'],'Pregnant female 1st trimester: quinine (DOC) + clindamycin.'),
('In chloroquine resistant vivax malaria, 2nd and 3rd trimester pregnancy is treated with:','ACT',['Quinine + clindamycin','Tetracycline + quinine','Primaquine'],'2nd & 3rd trimester: ACT.'),
('The ACT used in all Indian states is:','Oral artesunate + sulfadoxine + pyrimethamine',['Oral artemether + lumefantrine','Artesunate + doxycycline','Artesunate + mefloquine'],'ACT 1: oral artesunate + sulfadoxine + pyrimethamine - all Indian states.'),
('The ACT used in north-eastern states is:','Oral artemether + lumefantrine',['Oral artesunate + sulfadoxine + pyrimethamine','Artesunate + clindamycin','Artemether + primaquine'],'ACT 2: oral artemether + lumefantrine - north-eastern states.'),
('In normal population with chloroquine resistant vivax malaria, alternatives to ACT are:','Quinine + one of tetracycline/doxycycline (not safe in pregnancy) or clindamycin',['Chloroquine rechallenge','Primaquine alone','Mefloquine monotherapy'],'Normal population: ACT; alternatives quinine + one of tetracycline/doxycycline (not safe in pregnancy), clindamycin.'),
('The TOC for falciparum malaria is:','ACT',['Chloroquine x 3 days','Quinine + clindamycin 14 days','Chloroquine + primaquine'],'Falciparum malaria TOC: ACT (arm of the diagram).'),
])
unit('Chloroquine',
 'Chloroquine MOA: binds to haemoglobin producing toxic haem products; mechanism of resistance is drug efflux from the vacuole of cells. Uses: infectious - malaria, hepatic amoebiasis and infectious mononucleosis; non-infectious - rheumatoid arthritis, SLE, discoid LE and porphyria cutanea tarda. Side effect: bull\'s eye retinopathy with multiple concentric circles plus whorl-like corneal deposits.')
facts(203,[
('The MOA of chloroquine is:','Binds to haemoglobin -> toxic haem products',['Produces free radicals','Blocks DHPS','Blocks electron transport'],'Chloroquine MOA: binds to haemoglobin -> toxic haem products.'),
('The mechanism of chloroquine resistance is:','Drug efflux from vacuole of cells',['Target enzyme mutation','Drug degradation by parasite','Loss of drug uptake receptor only'],'Mechanism of resistance: drug efflux from vacuole of cells.'),
('The infectious uses of chloroquine are:','Malaria, hepatic amoebiasis and infectious mononucleosis',['Giardiasis and trichomoniasis','Kala azar and Chagas disease','Cryptosporidiasis and babesiosis'],'Uses infectious: malaria, hepatic amoebiasis, infectious mononucleosis.'),
('The non-infectious uses of chloroquine are:','Rheumatoid arthritis, SLE, discoid LE and porphyria cutanea tarda',['Gout and osteoarthritis','Ankylosing spondylitis and psoriasis','Pemphigus and dermatitis herpetiformis'],'Uses non-infectious: RA, SLE, discoid LE, porphyria cutanea tarda.'),
('The eye side effect of chloroquine is:','Bull\'s eye retinopathy (multiple concentric circles) + whorl-like corneal deposits',['Optic neuritis with colour blindness','Cataract with glaucoma','Ptosis and nystagmus'],'Chloroquine S/E: bull\'s eye retinopathy - multiple concentric circles + whorl-like corneal deposits.'),
('Bull\'s eye retinopathy of chloroquine shows:','Multiple concentric circles',['Whorl-like lens opacity','Papilledema','Dot-blot hemorrhages'],'Bull\'s eye retinopathy: multiple concentric circles + whorl-like corneal deposits.'),
('Chloroquine is the DOC for:','Sensitive (chloroquine responsive) vivax malaria',['Falciparum malaria in India','Chloroquine resistant vivax','Severe falciparum malaria'],'Vivax TOC: chloroquine (DOC) x 3 days.'),
('Chloroquine is used only for hepatic amoebiasis because:','It reaches high liver tissue concentrations (extra-intestinal action)',['It kills cysts in the lumen','It is a luminal amoebicide','It acts on intestinal flora'],'Extra-intestinal (hepatic): chloroquine (only for hepatic).'),
])
unit('Quinine',
 'Quinine is used in resistant malaria. Side effects: alpha blocker causing hypotension, increased insulin release causing hypoglycemia and blockade of K+ channels causing QT prolongation. Cinchonism (derived from the Cinchona plant) presents with tinnitus and vertigo; inadequate doses cause black water fever.')
facts(203,[
('The use of quinine is:','Resistant malaria',['First-line vivax malaria','Malaria prophylaxis','Hepatic amoebiasis'],'Quinine use: resistant malaria.'),
('Quinine causes hypotension by:','Alpha blockade',['Beta blockade','Ganglionic stimulation','Muscarinic blockade'],'Quinine: alpha blocker -> hypotension.'),
('Quinine causes hypoglycemia by:','Increasing insulin release',['Blocking insulin release','Increasing gluconeogenesis','Decreasing renal insulin clearance'],'Quinine: increased insulin release -> hypoglycemia.'),
('Quinine causes QT prolongation by:','Blocking K+ channels',['Blocking Na+ channels','Blocking Ca2+ channels','Blocking beta receptors'],'Quinine: blocks K+ channels -> QT prolongation.'),
('Cinchonism is derived from:','Cinchona plant',['A synthetic impurity','An insect toxin','A fungal contaminant'],'Cinchonism (derived from Cinchona plant).'),
('The symptoms of cinchonism are:','Tinnitus and vertigo',['Blindness and deafness','Constipation and retention','Rash and arthritis'],'Cinchonism symptoms: tinnitus, vertigo.'),
('Inadequate doses of quinine cause:','Black water fever',['Cinchonism','G6PD hemolysis only','Agranulocytosis'],'If inadequate doses: black water fever.'),
])
unit('Mefloquine, Malaria Prophylaxis, Atovaquone-Proguanil and Antibiotics',
 'Mefloquine is used for resistant malaria and prophylaxis for travel of 6 weeks or more; side effects are neuropsychiatric effects and conduction block (C/I with quinine and halofantrine). Prophylaxis note: travel <6 weeks - doxycycline 100 mg OD, start 2 days before travel, stop 4 weeks after; travel >=6 weeks - mefloquine 250 mg/week, start 2 weeks before travel, stop 4 weeks after. Atovaquone + proguanil is used in resistant malaria with the MOA note - proguanil inhibits ovulation in the mosquito. Tetracycline, doxycycline and clindamycin are also used in resistant malaria; clindamycin is safe for use in children and pregnancy.')
facts(204,[
('The uses of mefloquine are:','Resistant malaria and prophylaxis of malaria for travel >=6 weeks',['Sensitive vivax malaria','Prophylaxis only for travel <6 weeks','Hepatic amoebiasis'],'Mefloquine use: resistant malaria; prophylaxis of malaria for travel >=6 wks.'),
('The side effects of mefloquine are:','Neuropsychiatric effects and conduction block (C/I with quinine & halofantrine)',['Hypoglycemia and hypotension','Black water fever','Optic neuritis'],'Mefloquine S/E: neuropsychiatric effects; conduction block (C/I with quinine & halofantrine).'),
('Malaria prophylaxis for travel <6 weeks is:','Doxycycline 100 mg OD',['Mefloquine 250 mg/week','Atovaquone + proguanil OD','Chloroquine 600 mg weekly'],'Travel <6 weeks: doxycycline 100 mg OD.'),
('Doxycycline malaria prophylaxis is started and stopped:','Start 2 days before travel, stop 4 weeks after travel',['Start 2 weeks before, stop 4 weeks after','Start on arrival, stop on leaving','Start 4 weeks before, stop 2 days after'],'<6 weeks: start 2 days before travel; stop 4 weeks after travel.'),
('Malaria prophylaxis for travel of 6 weeks or more is:','Mefloquine 250 mg/week',['Doxycycline 100 mg OD','Primaquine daily','Chloroquine 300 mg weekly'],'Travel >=6 weeks: mefloquine 250 mg/week.'),
('Mefloquine prophylaxis is started and stopped:','Start 2 weeks before travel, stop 4 weeks after travel',['Start 2 days before, stop 4 weeks after','Start on arrival, stop on return','Start 4 weeks before, stop 2 weeks after'],'>=6 weeks: start 2 weeks before travel; stop 4 weeks after travel.'),
('The use of atovaquone + proguanil is:','Resistant malaria',['Sensitive malaria','Babesiosis only','Pneumocystis prophylaxis'],'Atovaquone + proguanil use: resistant malaria.'),
('The MOA note for atovaquone + proguanil is:','Proguanil inhibits ovulation in mosquito',['Proguanil blocks electron transport in the parasite','Atovaquone inhibits DHFR','Proguanil blocks gametocyte formation in humans'],'MOA: proguanil inhibits ovulation in mosquito.'),
('The antibiotics used in resistant malaria are:','Tetracycline, doxycycline and clindamycin',['Azithromycin and clarithromycin','Amoxicillin and ceftriaxone','Gentamicin and ciprofloxacin'],'Tetracycline / doxycycline / clindamycin: use resistant malaria.'),
('The antibiotic safe for use in children and pregnancy (for malaria) is:','Clindamycin',['Doxycycline','Tetracycline','Mefloquine'],'Clindamycin is safe for use in children & pregnancy.'),
])
finish()
