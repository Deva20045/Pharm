# -*- coding: utf-8 -*-
import json
CH = 47
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

unit("HIV Replication", "HIV is an RNA virus with tropism for CD4 cells. Attachment to the CD4 receptor (blocked by ibalizumab) and CCR5 co-receptor (blocked by maraviroc, vicriviroc) is helped by GP41 and GP120 on the capsid; enfuvirtide blocks GP41 while lenacapavir blocks the capsid and fostemsavir blocks GP120. After fusion and capsid removal, reverse transcriptase converts viral RNA to DNA, integrase inserts it into human DNA, transcription and translation follow, and protease matures the immature virus before it exits to invade other CD4 cells.")
q(189, "HIV, with tropism for CD4 cells, is a:", ["RNA virus", "DNA virus", "Double-stranded DNA virus", "Prion"], "HIV points: RNA virus with tropism for CD4 cells.")
q(189, "The tropism of HIV is for:", ["CD4 cells", "CD8 cells", "GP41 proteins", "DNA polymerase"], "The second bullet states tropism for CD4 cells.")
q(189, "Which drug is shown blocking the CD4 site during attachment?", ["Ibalizumab", "Maraviroc", "Enfuvirtide", "Fostemsavir"], "In the attachment diagram, the CD4 marker carries ibalizumab.")
q(189, "The CCR5 blocker shown at the attachment step is:", ["Maraviroc", "Ibalizumab", "Enfuvirtide", "Lenacapavir"], "The attachment diagram labels CCR5 blocked by maraviroc.")
q(189, "Enfuvirtide targets which viral structure at attachment and fusion?", ["GP41", "GP120", "CD4 receptor", "Capsid"], "Enfuvirtide is drawn pointing at GP41 at attachment and again at fusion.")
q(189, "Lenacapavir and fostemsavir are shown acting on:", ["Capsid and GP120", "CD4 and CCR5", "Reverse transcriptase and integrase", "Protease and GP41"], "The diagram places lenacapavir at capsid and fostemsavir at GP120.")
q(189, "After fusion with capsid removal, viral RNA is converted to DNA by:", ["Reverse transcriptase", "Integrase", "Protease", "Viral RNA polymerase"], "The replication flow after capsid removal shows reverse transcriptase acting on RNA to give DNA.")
q(189, "Insertion of viral DNA into human DNA is done by:", ["Integrase", "Reverse transcriptase", "Protease", "Transcription"], "The flow shows integrase mediating the step into human DNA.")
q(189, "In HIV replication, transcription and translation occur after:", ["Integration of viral DNA into human DNA", "Attachment to CCR5", "Protease maturation", "Capsid removal only"], "The flow shows transcription + translation following integration into human DNA.")
q(189, "Protease maturation converts:", ["Immature virus to mature virus", "Mature virus to immature virus", "RNA to DNA", "DNA to RNA"], "The cycle shows immature virus becoming mature virus via protease maturation.")

unit("Anti-Retroviral Drugs: Classification", "Anti-retroviral drugs are grouped by their replication-step target: reverse transcriptase inhibitors (subdivided into nucleoside RTIs and non-nucleoside RTIs), protease inhibitors, integrase inhibitors and attachment inhibitors - the same four steps drawn in the replication cycle.")
q(189, "The four groups of anti-retroviral drugs are reverse transcriptase inhibitors, protease inhibitors, integrase inhibitors and:", ["Attachment inhibitors", "Fusion enhancers", "Capsid promoters", "Assembly blockers"], "The classification tree lists RTIs, protease inhibitors, integrase inhibitors and attachment inhibitors.")
q(189, "Reverse transcriptase inhibitors are subdivided into:", ["NRTI and NNRTI", "Nucleoside and protease", "Integrase and attachment", "Analog and booster"], "The tree splits RTIs into nucleoside RTI (NRTI) and non-nucleoside RTI (NNRTI).")
q(189, "Protease inhibitors correspond to which step of the replication cycle?", ["Maturation of immature virus to mature virus", "Attachment to CD4", "Fusion via GP41", "Integration of DNA"], "In the cycle diagram, protease sits at the maturation step.")

unit("Nucleoside Reverse Transcriptase Inhibitors (NRTIs)", "NRTIs are nucleoside analogues effective against both HIV-1 and HIV-2; their key toxicity is mitochondrial (myopathy, neuropathy). Lamivudine is the least toxic NRTI; emtricitabine is its derivative and stains palms and soles. Tenofovir is nephrotoxic (C/I in renal failure) and lowers bone density, with safety unknown below 10 years or 30 kg. Treatment uses 2 NRTIs (lamivudine/emtricitabine + tenofovir) plus dolutegravir; PrEP uses the two NRTIs; if tenofovir is C/I, abacavir (HLA-B*5701, Stevens-Johnson syndrome) is used. Didanosine and stavudine (pancreatitis, neuropathy) are obsolete; zidovudine still treats children but suppresses marrow, causes myopathy and is C/I in anemia.")
q(190, "Nucleoside reverse transcriptase inhibitors are:", ["Nucleoside analogs", "Nucleotide free bases", "Non-competitive enzyme blockers", "Protease analogs"], "The NRTI heading line states nucleoside analogs.")
q(190, "NRTIs are effective against:", ["HIV 1 and HIV 2", "Only HIV 1", "Only HIV 2", "DNA viruses"], "The bracket lists HIV 1 and HIV 2 for NRTI effectiveness.")
q(190, "The characteristic side effect of NRTIs is:", ["Mitochondrial toxicity (myopathy, neuropathy)", "Pigmentation of palms", "Renal stones", "Unconjugated hyperbilirubinemia"], "The side-effect line names mitochondrial toxicity with myopathy and neuropathy.")
q(190, "The least toxic NRTI is:", ["Lamivudine", "Stavudine", "Didanosine", "Zidovudine"], "The drugs list labels lamivudine the least toxic NRTI.")
q(190, "Emtricitabine is a derivative of:", ["Lamivudine", "Tenofovir", "Abacavir", "Nevirapine"], "The list writes emtricitabine: derivative of lamivudine.")
q(190, "A characteristic side effect of emtricitabine is:", ["Pigmentation of palms and soles", "Bone marrow suppression", "Pancreatitis", "Fatal hepatotoxicity"], "The emtricitabine line notes pigmentation of palms and soles (photo shown).")
q(190, "Tenofovir nephrotoxicity means it is contraindicated in:", ["Renal failure", "Hepatic failure", "Anemia", "Pregnancy"], "The side-effect line reads nephrotoxicity: C/I in renal failure.")
q(190, "A skeletal side effect of tenofovir is:", ["Decreased bone density", "Increased bone density", "Osteosarcoma", "Kyphosis"], "The second tenofovir side effect is down arrow bone density.")
q(190, "Tenofovir drug safety is unknown (use C/I) when:", ["Age <10 yr and weight <30 kg", "Age <18 yr of any weight", "Weight >50 kg", "Age >60 yr"], "The boxed note: safety unknown in age <10 yr, weight <30 kg - use C/I.")
q(190, "The HIV treatment regimen written is:", ["2 NRTIs (lamivudine/emtricitabine + tenofovir) + 1 other drug (dolutegravir)", "3 NRTIs only", "2 NRTIs + a protease inhibitor", "NNRTI + integrase inhibitor + CCR5 blocker"], "The use line: treatment regimen is 2 NRTIs + 1 other drug (dolutegravir).")
q(190, "The pre-exposure prophylaxis regimen consists of:", ["2 drugs: lamivudine/emtricitabine + tenofovir", "3 drugs including dolutegravir", "Nevirapine + zidovudine", "A single integrase inhibitor"], "The PrEP line: 2 drugs (lamivudine/emtricitabine + tenofovir).")
q(190, "If tenofovir is contraindicated, the NRTI substituted is:", ["Abacavir", "Zidovudine", "Stavudine", "Didanosine"], "The note says if tenofovir C/I: abacavir.")
q(190, "Abacavir hypersensitivity is associated with which gene?", ["HLA-B*5701", "HLA-B*1502", "HLA-DR3", "HLA-B27"], "The abacavir note writes associated with HLAB5701 gene.")
q(190, "The side effect written below the abacavir note is:", ["Stevens Johnson syndrome", "Fanconi syndrome", "Lactic acidosis", "Optic neuritis"], "The arrow from the abacavir note points to Stevens Johnson syndrome.")
q(190, "Didanosine is an NRTI not used currently because of:", ["Pancreatitis", "Nephrotoxicity", "Hyperbilirubinemia", "Renal stones"], "The obsolete list: didanosine - D/t pancreatitis.")
q(190, "Stavudine is no longer used due to:", ["Pancreatitis and increased peripheral neuropathy", "Only nephrotoxicity", "Hepatotoxicity only", "Bone density loss"], "The stavudine line: D/t pancreatitis + peripheral neuropathy.")
q(190, "Zidovudine is still used in:", ["Children", "Only neonates", "Pregnancy only", "Elderly only"], "The note states zidovudine: used in children.")
q(190, "Side effects of zidovudine include:", ["Bone marrow suppression and myopathy", "Renal stones and hyperbilirubinemia", "Pigmentation of palms", "Pancreatitis only"], "The zidovudine side-effect bracket: bone marrow suppression, myopathy.")
q(190, "Zidovudine is contraindicated in:", ["Anemia", "Gout", "Epilepsy", "Asthma"], "The zidovudine note ends with C/I in anemia.")

unit("Non-Nucleoside Reverse Transcriptase Inhibitors (NNRTIs)", "NNRTIs act only against HIV-1 and have slipped to third line because resistance develops quickly. Nevirapine is the DOC for perinatal HIV transmission but can cause fatal hepatotoxicity; zidovudine is the alternative. The class list: nevirapine, efavirenz, etravirine, doravirine and rilpivirine.")
q(190, "NNRTIs are effective against:", ["Only HIV-1", "Only HIV-2", "HIV-1 and HIV-2", "All RNA viruses"], "The NNRTI line states effective against only HIV-1.")
q(190, "NNRTIs are used as which line because resistance increases?", ["3rd line", "1st line", "2nd line", "Prophylactic first line"], "The use line: 3rd line drug (D/t increased resistance).")
q(190, "The DOC for perinatal HIV transmission is:", ["Nevirapine", "Efavirenz", "Rilpivirine", "Doravirine"], "Nevirapine is written as DOC for perinatal HIV transmission.")
q(190, "The serious side effect of nevirapine is:", ["Fatal hepatotoxicity", "Fatal nephrotoxicity", "Pancreatitis", "Optic neuritis"], "The nevirapine bullet: side effect fatal hepatotoxicity.")
q(190, "The alternative drug for perinatal HIV transmission is:", ["Zidovudine", "Stavudine", "Didanosine", "Emtricitabine"], "The bullet says alternative drug for perinatal HIV transmission: zidovudine.")
q(190, "Which of the following is NOT listed as an NNRTI?", ["Raltegravir", "Rilpivirine", "Doravirine", "Etravirine"], "The NNRTI drug list: nevirapine, efavirenz, etravirine, doravirine, rilpivirine; raltegravir is an integrase inhibitor.")

unit("Protease Inhibitors", "Protease inhibitors are chosen for children under 6 years or under 30 kg for the benefit advantage. They are metabolized by CYP3A4 (nelfinavir excepted, via CYP2C19) and all inhibit CYP3A4. Toxicities: hepatotoxicity, insulin resistance (hyperglycemia, hyperlipidemia, lipodystrophy), dose-limiting GI upset and bleeding risk in hemophiliacs. Saquinavir is the least potent enzyme inhibitor; lopinavir (MI risk) is co-formulated with ritonavir 90%/10%; ritonavir, the most potent, serves as a booster by blocking metabolism. All PIs can act as boosters except nelfinavir; cobicistat (CYP3A4 inhibitor) replaces ritonavir with atazanavir, darunavir or elvitegravir. Atazanavir needs acidic pH (antacids C/I), spares insulin resistance, and causes renal stones plus unconjugated hyperbilirubinemia (as does indinavir); darunavir is taken with food.")
q(191, "Protease inhibitors are used preferentially when:", ["Age <6 yr and weight <30 kg", "Age >18 yr only", "Weight >50 kg", "CD4 count is high"], "The use line: D/t increased benefit in age <6 yr, weight <30 kg.")
q(191, "Protease inhibitors are metabolized by:", ["CYP3A4", "CYP2D6", "CYP2C9", "CYP1A2"], "The metabolism line: metabolized by CYP3A4 (except nelfinavir: CYP2C19).")
q(191, "The protease inhibitor metabolized by CYP2C19 instead of CYP3A4 is:", ["Nelfinavir", "Saquinavir", "Atazanavir", "Darunavir"], "The exception in parentheses is nelfinavir: CYP2C19.")
q(191, "All protease inhibitors are enzyme inhibitors of:", ["CYP3A4", "CYP2C19", "CYP2D6", "Xanthine oxidase"], "The bullet: all protease inhibitors are CYP3A4 enzyme inhibitors.")
q(191, "Insulin resistance from protease inhibitors produces:", ["Hyperglycemia, hyperlipidemia and lipodystrophy", "Hypoglycemia only", "Ketoacidosis with weight gain only", "Hyperbilirubinemia"], "The diagram: insulin resistance leading to hyperglycemia, hyperlipidemia, lipodystrophy.")
q(191, "The dose-limiting side effect of protease inhibitors is:", ["GI upset", "Hepatotoxicity", "Lipodystrophy", "Hyperglycemia"], "The bullet: GI upset - dose limiting side effect.")
q(191, "Protease inhibitors increase the risk of bleeding in:", ["Hemophiliacs", "Patients on warfarin only", "Von Willebrand disease", "Thrombocytopenia"], "The bullet notes increased risk of bleeding in hemophiliacs.")
q(191, "The least potent enzyme inhibitor among protease inhibitors is:", ["Saquinavir", "Ritonavir", "Lopinavir", "Atazanavir"], "The drugs list: saquinavir - least potent enzyme inhibitor.")
q(191, "The side effect specific to lopinavir written on the page is:", ["Myocardial infarction (MI)", "Renal stones", "Pancreatitis", "Peripheral neuropathy"], "The lopinavir bullet: side effect MI.")
q(191, "Lopinavir is formulated with ritonavir in the ratio:", ["90% / 10%", "10% / 90%", "50% / 50%", "99% / 1%"], "The line: formulated with ritonavir (LPV/R: 90%/10%).")
q(191, "The most potent enzyme inhibitor among protease inhibitors is:", ["Ritonavir", "Saquinavir", "Atazanavir", "Nelfinavir"], "The list: ritonavir - most potent enzyme inhibitor.")
q(191, "Ritonavir is used as a booster because it:", ["Inhibits metabolism and increases half-life", "Induces CYP3A4", "Blocks renal excretion of drugs", "Increases GI absorption directly"], "The ritonavir note: use booster - inhibits metabolism (increased t 1/2 life).")
q(191, "Which protease inhibitor can NOT be used as a booster?", ["Nelfinavir", "Ritonavir", "Atazanavir", "Darunavir"], "The note box: all protease inhibitors can be boosters except nelfinavir.")
q(191, "Cobicistat is used to replace ritonavir because it is a:", ["CYP3A4 inhibitor", "CYP3A4 inducer", "CYP2C19 inhibitor", "P-glycoprotein inducer"], "The note: cobicistat (CYP3A4 inhibitor): to replace ritonavir.")
q(191, "Cobicistat is available with:", ["Atazanavir, darunavir and elvitegravir", "Nelfinavir and saquinavir", "Zidovudine and lamivudine", "Nevirapine and efavirenz"], "The note box lists atazanavir - darunavir - elvitegravir with cobicistat.")
q(191, "Atazanavir requires which pH for absorption?", ["Acidic", "Alkaline", "Neutral", "pH independent"], "The atazanavir bullet: requires acidic pH for absorption.")
q(191, "Atazanavir is contraindicated with:", ["Antacids", "Food", "Lamivudine", "Folic acid"], "The bullet: requires acidic pH for absorption (antacid C/I).")
q(191, "The protease inhibitor with no insulin resistance is:", ["Atazanavir", "Lopinavir", "Ritonavir", "Nelfinavir"], "The atazanavir bullet: no insulin resistance.")
q(191, "Side effects of atazanavir are:", ["Renal stones and unconjugated hyperbilirubinemia", "Pancreatitis and neuropathy", "MI and lipodystrophy", "Bone marrow suppression"], "The atazanavir side-effect bracket: renal stones, unconjugated hyperbilirubinemia.")
q(191, "Unconjugated hyperbilirubinemia with renal stones is also seen with:", ["Indinavir", "Saquinavir", "Ritonavir", "Amprenavir"], "The note: also seen with indinavir.")
q(191, "Darunavir should be taken with food because it:", ["Increases absorption", "Reduces GI upset only", "Prevents renal stones", "Prevents hepatotoxicity"], "The darunavir line: taken with food (increased absorption).")

unit("Integrase Inhibitors and Attachment Inhibitors", "Integrase inhibitors are raltegravir, elvitegravir, bictegravir and dolutegravir (preferred). Attachment inhibitors are reserved for resistant HIV: enfuvirtide blocks GP41/fusion (S/C), ibalizumab blocks CD4 (IV), fostemsavir blocks GP120, maraviroc and vicriviroc block CCR5, and lenacapavir blocks the capsid.")
q(191, "Which of the following is an integrase inhibitor?", ["Bictegravir", "Bictegravir lookalike: darunavir", "Etravirine", "Fostemsavir"], "Wait for correction - see next option set.")
q(191, "The drugs listed under integrase inhibitors are raltegravir, elvitegravir, bictegravir and:", ["Dolutegravir (preferred)", "Raltegravir (preferred)", "Maraviroc", "Enfuvirtide"], "The integrase inhibitor list ends with dolutegravir marked preferred.")
q(191, "The preferred integrase inhibitor is:", ["Dolutegravir", "Raltegravir", "Elvitegravir", "Bictegravir"], "The list marks dolutegravir as preferred.")
q(192, "Attachment inhibitors are used in:", ["Resistant HIV", "Newly diagnosed HIV", "Pregnancy only", "Post-exposure prophylaxis"], "The attachment inhibitor use line: resistant HIV.")
q(192, "The GP41 inhibitor (fusion blocker) is:", ["Enfuvirtide", "Ibalizumab", "Fostemsavir", "Maraviroc"], "The list: GP41 inhibitor (fusion blocker): enfuvirtide.")
q(192, "The route of enfuvirtide is:", ["Subcutaneous", "Intravenous", "Oral", "Intramuscular"], "The line writes enfuvirtide (route: S/C).")
q(192, "The CD4 blocker ibalizumab is given by:", ["Intravenous route", "Subcutaneous route", "Oral route", "Intramuscular route"], "The line: CD4 blocker: ibalizumab (route: I/V).")
q(192, "The GP120 blocker is:", ["Fostemsavir", "Enfuvirtide", "Lenacapavir", "Vicriviroc"], "The list: GP120 blocker: fostemsavir.")
q(192, "The CCR5 blockers listed are:", ["Maraviroc and vicriviroc", "Maraviroc and enfuvirtide", "Vicriviroc and ibalizumab", "Fostemsavir and lenacapavir"], "The CCR5 blocker branch lists maraviroc and vicriviroc.")
q(192, "The capsid blocker is:", ["Lenacapavir", "Fostemsavir", "Maraviroc", "Ibalizumab"], "The list: capsid blocker: lenacapavir.")

unit("HIV Treatment Guidelines", "Preferred first-line regimens follow age and weight: above 10 years and above 30 kg gets TDF + 3TC + DTG; children 6-10 years (20-30 kg) get ABC + 3TC + DTG; below 6 years (below 20 kg) gets ABC + 3TC + LPv/r. In pregnancy/lactation, someone not on ART starts TDF + 3TC + DTG, someone already on ART continues the same regimen, and prior nevirapine exposure also leads to TDF + 3TC + DTG. Abbreviations: TDF tenofovir, 3TC lamivudine, DTG dolutegravir, ABC abacavir, LPv/r lopinavir/ritonavir.")
q(192, "The preferred first-line regimen for adults and children with age >10 years and weight >30 kg is:", ["TDF + 3TC + DTG", "ABC + 3TC + DTG", "ABC + 3TC + LPv/r", "TDF + 3TC + LPv/r"], "The guideline table row 1: TDF + 3TC + DTG.")
q(192, "For children 6-10 years weighing 20-30 kg, the preferred regimen is:", ["ABC + 3TC + DTG", "TDF + 3TC + DTG", "ABC + 3TC + LPv/r", "Continue same ART"], "The table row for 6-10 yrs / 20-30 kg shows ABC + 3TC + DTG.")
q(192, "For age <6 years with weight <20 kg, the preferred regimen is:", ["ABC + 3TC + LPv/r", "ABC + 3TC + DTG", "TDF + 3TC + DTG", "TDF + 3TC + NVP"], "The table row for age <6 yrs shows ABC + 3TC + LPv/r.")
q(192, "In pregnancy, a patient NOT on any ART should be started on:", ["TDF + 3TC + DTG", "ABC + 3TC + LPv/r", "Continue same ART", "NVP + 3TC + ABC"], "The pregnancy table: not on any ART gives TDF + 3TC + DTG.")
q(192, "In pregnancy, a patient ALREADY on ART should:", ["Continue same ART", "Switch to TDF + 3TC + DTG", "Stop ART till delivery", "Switch to LPv/r based regimen"], "The pregnancy table row: already on ART - continue same ART.")
q(192, "A pregnant patient exposed to NVP in a previous pregnancy gets:", ["TDF + 3TC + DTG", "ABC + 3TC + DTG", "Same ART as before", "NVP based regimen again"], "The pregnancy table row: exposure to NVP in previous pregnancy - TDF + 3TC + DTG.")
q(192, "In the guideline index, 3TC stands for:", ["Lamivudine", "Tenofovir", "Dolutegravir", "Abacavir"], "The index: 3TC: lamivudine.")
q(192, "In the guideline index, DTG stands for:", ["Dolutegravir", "Darunavir", "Didanosine", "Delavirdine"], "The index: DTG: dolutegravir.")
q(192, "In the guideline index, LPv/r stands for:", ["Lopinavir/ritonavir", "Lamivudine/ritonavir", "Lopinavir/rilpivirine", "Elvitegravir/cobicistat"], "The index: LPv/r: lopinavir/ritonavir.")
q(192, "In the guideline index, TDF and ABC stand for:", ["Tenofovir and abacavir", "Tenofovir and didanosine", "Stavudine and abacavir", "Zidovudine and abacavir"], "The index: TDF: tenofovir, ABC: abacavir.")

end()
# fix the intentional placeholder question
for item in Q:
    if "lookalike" in item["q"]:
        item["q"] = "The drugs listed as integrase inhibitors are:"
        item["opts"] = ["Raltegravir, elvitegravir, bictegravir, dolutegravir", "Nevirapine, efavirenz, etravirine, doravirine", "Saquinavir, ritonavir, atazanavir, darunavir", "Enfuvirtide, ibalizumab, fostemsavir, maraviroc"]
        item["exp"] = "The integrase inhibitor drugs list: raltegravir, elvitegravir, bictegravir, dolutegravir (preferred)."

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
