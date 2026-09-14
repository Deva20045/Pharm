# -*- coding: utf-8 -*-
"""Generate PULSE Pharm data for chapters 31-38 from the rendered book-page scans.

Source: uploads/Pharmacology Marrow E8 (1).pdf, book pages 123-154.
Chapters: 31 Opioids: Part 1 (123-126), 32 Opioids: Part 2 (127-130),
33 Affect Disorders: Part 1 (131-133), 34 Affect Disorders: Part 2 (134-140),
35 Antipsychotic Drugs (141-144), 36 Neurodegenerative Disorders (145-149),
37 Alcohol and Smoking Dependence (150-152),
38 Introduction to Antibacterial Drugs (153-154).
"""
import json
from pathlib import Path

Q = []
UNITS = []
CH = None
CUR = None

def start(ch):
    global CH, Q, UNITS, CUR
    CH = ch
    Q = []
    UNITS = []
    CUR = None

def unit(title, guide):
    global CUR
    if CUR:
        end_unit()
    CUR = {"title": title, "start": len(Q) + 1, "guide": guide}

def q(page, text, opts, exp):
    assert CUR is not None, "call unit() before q()"
    assert len(opts) == 4, opts
    assert len(set(opts)) == 4, opts
    suffix = f"(Book p{page})"
    exp = exp.rstrip()
    if not exp.endswith(suffix):
        exp = f"{exp} {suffix}"
    Q.append({"id": "", "sec": CUR["title"], "page": page, "q": text,
              "opts": opts, "ans": 0, "exp": exp})

def end_unit():
    global CUR
    if CUR is None:
        return
    CUR["end"] = len(Q)
    UNITS.append(CUR)
    CUR = None

def finish():
    end_unit()
    for i, item in enumerate(Q, 1):
        item["id"] = f"PHARM-C{CH}-{i:03d}"
    units = []
    for n, u in enumerate(UNITS, 1):
        a, b = u["start"], u["end"]
        units.append({
            "id": f"PHARM-U{CH}-{n}", "ch": CH, "n": n, "title": u["title"],
            "sec": f"{u['title']} · p{Q[a-1]['page']}",
            "qs": [f"PHARM-C{CH}-{i:03d}" for i in range(a, b + 1)],
            "guide": u["guide"],
        })
    Path("data").mkdir(exist_ok=True)
    out = Path(f"data/ch{CH:02d}.json")
    json.dump({"questions": Q, "units": units}, out.open("w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"ch{CH}: {len(Q)} questions, {len(units)} units -> {out}")
    for u in units:
        print("  ", u["id"], len(u["qs"]), u["sec"])

# ---------------------------------------------------------------------------
# Chapter 31: Opioids: Part 1 (p123-126)
# ---------------------------------------------------------------------------
start(31)
unit("Opioid Receptors and the mu (mu) Receptor Effects",
     "The chapter opens with the three opioid receptors - mu, kappa and delta - and their effects. The mu effects are remembered by the mnemonic mMuSCARINE: miosis, urine retention, sedation, constipation, analgesia, respiratory depression and increased muscle rigidity (classically the wooden chest syndrome of fentanyl), followed by reduced bile flow from sphincter of Oddi contraction, contraction of circular smooth muscle and relaxation of longitudinal smooth muscle.")
q(123, "The first topic discussed in the chapter 'Opioids: Part 1' is:",
  ["Opioid receptors", "Opioid antagonists", "Opioid toxicity", "Opioid tolerance"],
  "The page starts with the heading 'Opioid receptors' before any drug is discussed.")
q(123, "The three opioid receptors named on the page are mu, kappa and:",
  ["Delta", "Sigma", "Epsilon", "Omega"],
  "The three receptor headings are mu (mu), kappa (kappa) and delta.")
q(123, "The mnemonic used for the effects of the mu receptor is:",
  ["mMuSCARINE", "MUDPILES", "SLUDGE", "ABCDEF"],
  "The page gives the mnemonic 'mMuSCARINE' against the mu receptor effects.")
q(123, "In the muSCARINE mnemonic for mu receptor effects, the letter M stands for:",
  ["Miosis", "Mydriasis", "Muscle rigidity", "Metoclopramide-like vomiting"],
  "M = miosis, the first effect listed under the mu receptor.")
q(123, "In the muSCARINE mnemonic, the letter U stands for:",
  ["Urine retention", "Ulceration", "Urea elevation", "Urticaria"],
  "U = urine retention, listed immediately after miosis.")
q(123, "In the muSCARINE mnemonic, the letter S stands for:",
  ["Sedation", "Salivation", "Sweating", "Seizure"],
  "S = sedation.")
q(123, "In the muSCARINE mnemonic, the letter C stands for:",
  ["Constipation", "Cough suppression", "Cyanosis", "Confusion"],
  "C = constipation.")
q(123, "In the muSCARINE mnemonic, the letter A stands for:",
  ["Analgesia", "Anxiolysis", "Anorexia", "Ataxia"],
  "A = analgesia.")
q(123, "In the muSCARINE mnemonic, the letter R stands for:",
  ["Respiratory depression", "Renal failure", "Rash", "Reflex tachycardia"],
  "R = respiratory depression.")
q(123, "In the muSCARINE mnemonic, the letter I stands for:",
  ["Increased muscle rigidity", "Itching", "Increased peristalsis", "Insomnia"],
  "I = increased muscle rigidity.")
q(123, "The example quoted for opioid-induced increased muscle rigidity is wooden chest syndrome with:",
  ["Fentanyl", "Morphine", "Codeine", "Loperamide"],
  "The page quotes 'wooden chest syndrome in Fentanyl' as the example of increased muscle rigidity.")
q(123, "A patient on an intravenous fentanyl infusion suddenly develops a rigid chest wall that cannot be ventilated. This is an example of:",
  ["Increased muscle rigidity - wooden chest syndrome", "Respiratory depression from medullary suppression",
   "Anaphylaxis with bronchospasm", "Malignant hyperthermia"],
  "Wooden chest syndrome due to increased muscle rigidity is the classic example given for fentanyl.")
q(123, "Pin-point pupils seen in opioid overdose reflect which mu receptor effect?",
  ["Miosis", "Sedation", "Urinary retention", "Analgesia"],
  "Miosis is the M of the muSCARINE mnemonic and produces the pin-point pupil of opioid overdose.")
q(123, "Inability to pass urine after morphine is explained by which mu effect?",
  ["Urine retention", "Constipation", "Sedation", "Miosis"],
  "Urine retention (U of the mnemonic) is a mu receptor effect.")
q(123, "The mu receptor effect on bile flow is:",
  ["Decreased bile flow", "Increased bile flow", "No change in bile flow", "Bile flow becomes cyclic"],
  "The mu list includes reduced bile flow, which follows contraction of the sphincter of Oddi.")
q(123, "The reduced bile flow produced by mu agonists is attributable to contraction of the:",
  ["Sphincter of Oddi", "Lower oesophageal sphincter", "Internal anal sphincter", "Pyloric sphincter"],
  "The side note against the mu column reads 'contraction of sphincter of Oddi', which cuts bile flow.")
q(123, "According to the mu receptor column, circular smooth muscle:",
  ["Contracts", "Relaxes", "Is unaffected", "Becomes paralysed only in overdose"],
  "The mu column ends with 'circular smooth muscles: contract'.")
q(123, "According to the mu receptor column, longitudinal smooth muscle:",
  ["Relaxes", "Contracts", "Is unaffected", "Undergoes hypertrophy"],
  "The mu column ends with 'longitudinal smooth muscles: relax'.")
q(123, "Which of the following is NOT listed as a mu receptor effect?",
  ["Psychomimetic dysphoria", "Miosis", "Respiratory depression", "Increased muscle rigidity"],
  "Psychomimetic (dysphoria) is listed under the kappa receptor, not under mu.")
q(123, "The combination of contracted circular muscle and relaxed longitudinal muscle in the gut of a patient on morphine best explains:",
  ["Constipation and spasm with reduced propulsive movement", "Profuse watery diarrhoea",
   "Rapid gastric emptying", "Loss of the gastro-colic reflex only"],
  "Circular muscle contracts while longitudinal muscle relaxes, so non-propulsive segmental tone rises - the basis of opioid constipation.")

unit("kappa and delta Receptor Effects, the Biliary Colic Note and Difelikefalin",
     "The kappa receptor adds constipation, analgesia, anti-pruritic action and psychomimetic dysphoria, whereas the delta receptor produces analgesia and modulates the release of neurotransmitters and hormones. The page carries two clinical notes: opioids are not contraindicated in biliary colic because the analgesic effect outweighs sphincter contraction, and difelikefalin, a kappa agonist, is used for pruritus in dialysis-dependent CKD patients.")
q(123, "Constipation is listed as an effect of which receptors?",
  ["Both mu and kappa", "mu only", "kappa only", "delta only"],
  "Constipation appears in the mu list (C of muSCARINE) and at the top of the kappa list.")
q(123, "Analgesia is listed as an effect of:",
  ["mu, kappa and delta", "mu only", "kappa and delta only", "mu and kappa only"],
  "Analgesia appears in all three receptor columns - mu, kappa and delta.")
q(123, "The psychomimetic (dysphoria) effect of opioids is attributed to the:",
  ["kappa receptor", "mu receptor", "delta receptor", "sigma receptor"],
  "Psychomimetic (dysphoria) is listed in the kappa column.")
q(123, "Anti-pruritic action is a listed effect of the:",
  ["kappa receptor", "mu receptor", "delta receptor", "All three receptors equally"],
  "The kappa column lists anti-pruritus.")
q(123, "Modulation of the release of neurotransmitters and hormones is listed under:",
  ["delta receptor", "mu receptor", "kappa receptor", "Both mu and kappa receptors"],
  "The delta column lists 'modulate release of: i. neurotransmitters, ii. hormones'.")
q(123, "The two categories of release said to be modulated by the delta receptor are:",
  ["Neurotransmitters and hormones", "Enzymes and bile acids", "Electrolytes and water", "Cytokines and complement"],
  "The delta column lists i. neurotransmitters and ii. hormones.")
q(123, "A patient on an opioid complains of dysphoria and strange dreams while still having good pain relief. The receptor most responsible is:",
  ["kappa", "mu", "delta", "NMDA"],
  "Psychomimetic effects such as dysphoria are kappa mediated.")
q(123, "Which receptor effect listed on the page is unique to the delta receptor?",
  ["Modulation of neurotransmitter and hormone release", "Analgesia", "Constipation", "Miosis"],
  "Only the delta column lists modulation of neurotransmitter and hormone release.")
q(123, "According to the note on the page, opioids in biliary colic are:",
  ["Not contraindicated because the analgesic effect exceeds the contraction",
   "Absolutely contraindicated because they contract the sphincter of Oddi",
   "Used only after cholecystectomy", "Replaced by papaverine in all cases"],
  "The note reads 'Opioids not c/l in biliary colic (Analgesic effect > Contraction)'.")
q(123, "The reasoning given for continuing opioids in biliary colic is that the:",
  ["Analgesic effect is greater than the sphincter contraction", "Sphincter relaxes at analgesic doses",
   "Biliary tree has no opioid receptors", "Drug is excreted entirely in bile"],
  "The note justifies opioid use by stating analgesic effect > contraction.")
q(123, "Difelikefalin is described as a:",
  ["kappa agonist", "mu agonist", "delta antagonist", "mu antagonist"],
  "The page states 'Difelikefalin: kappa agonist'.")
q(123, "Difelikefalin is used for:",
  ["Pruritus in CKD patients on dialysis", "Pain in acute pancreatitis",
   "Diarrhoea-predominant irritable bowel syndrome", "Opioid-induced constipation"],
  "Difelikefalin is used for pruritus in CKD patients on dialysis.")
q(123, "A dialysis-dependent patient with refractory uraemic pruritus is best treated, per this page, with:",
  ["Difelikefalin", "Naltrexone", "Loperamide", "Eluxadoline"],
  "Difelikefalin, a kappa agonist, is the drug named for pruritus in dialysis patients.")

unit("Endogenous Opioids",
     "The drug section begins with the endogenous opioids, which are synthesised within the body: enkephalin acting on the delta receptor, endorphin on the mu receptor and dynorphin on the kappa receptor.")
q(123, "The first group of drugs discussed under 'Drugs' is:",
  ["Endogenous opioids", "Synthetic opioids", "Opioid antagonists", "Semi-synthetic opioids"],
  "Under the heading 'Drugs' the first group is endogenous opioids.")
q(123, "Endogenous opioids are defined as those:",
  ["Synthesised within the body", "Extracted from Papaver somniferum",
   "Prepared by chemical modification of morphine", "Produced only in the pituitary"],
  "The page says endogenous opioids are synthesised within the body.")
q(123, "Enkephalin acts predominantly on the:",
  ["delta receptor", "mu receptor", "kappa receptor", "sigma receptor"],
  "The list pairs enkephalin with the delta receptor.")
q(123, "Endorphin acts predominantly on the:",
  ["mu receptor", "delta receptor", "kappa receptor", "NMDA receptor"],
  "The list pairs endorphin with the mu receptor.")
q(123, "Dynorphin acts predominantly on the:",
  ["kappa receptor", "mu receptor", "delta receptor", "GABA-B receptor"],
  "The list pairs dynorphin with the kappa receptor.")
q(123, "Correctly matched endogenous opioid and receptor is:",
  ["Enkephalin - delta, endorphin - mu, dynorphin - kappa",
   "Enkephalin - mu, endorphin - delta, dynorphin - kappa",
   "Enkephalin - kappa, endorphin - mu, dynorphin - delta",
   "Enkephalin - delta, endorphin - kappa, dynorphin - mu"],
  "The three pairings are enkephalin-delta, endorphin-mu and dynorphin-kappa.")
q(123, "Which endogenous opioid is paired with the kappa receptor?",
  ["Dynorphin", "Enkephalin", "Endorphin", "Beta-lipotropin"],
  "Dynorphin is the endogenous ligand listed against the kappa receptor.")

unit("Exogenous Opioids: Natural Opiates",
     "Exogenous opioids are first classified by source into natural opiates, semi-synthetic and synthetic drugs. Natural opiates are derived from Papaver somniferum and split into chemicals with opioid action (morphine and codeine) and chemicals without opioid action (noscapine, used as an anti-tussive for spasmodic cough; papaverine, which inhibits phosphodiesterase, raises cyclic AMP and relaxes smooth muscle in biliary and ureteric colic; and thebaine).")
q(124, "Exogenous opioids on this page are classified based on:",
  ["Source and opioid receptor interaction", "Route of administration only",
   "Duration of action only", "Chemical structure alone"],
  "Two classifications are given - 'based on source' and 'based on opioid receptor interaction'.")
q(124, "The 'based on source' classification divides exogenous opioids into:",
  ["Natural (opiates), semi-synthetic and synthetic", "Agonists and antagonists",
   "Short, intermediate and long acting", "Oral, parenteral and transdermal"],
  "The three source-based groups are natural (opiates), semi-synthetic and synthetic.")
q(124, "Natural opiates are derived from:",
  ["Papaver somniferum", "Atropa belladonna", "Digitalis lanata", "Rauwolfia serpentina"],
  "The natural opiates branch states 'derived from Papaver somniferum'.")
q(124, "Under natural opiates, the chemicals with opioid action are:",
  ["Morphine and codeine", "Noscapine and papaverine", "Thebaine and noscapine", "Papaverine and codeine"],
  "The 'chemicals with opioid action' branch lists a. morphine and b. codeine.")
q(124, "Under natural opiates, the chemicals without opioid action include:",
  ["Noscapine, papaverine and thebaine", "Morphine and codeine",
   "Heroin and pholcodine", "Fentanyl and pethidine"],
  "The 'chemicals without opioid action' branch lists a. noscapine, b. papaverine and c. thebaine.")
q(124, "Noscapine is used as:",
  ["An anti-tussive for spasmodic cough", "An analgesic for severe pain",
   "An anti-diarrhoeal agent", "A smooth muscle relaxant in biliary colic"],
  "Noscapine's use is given as anti-tussive for spasmodic cough.")
q(124, "Papaverine acts by inhibiting:",
  ["Phosphodiesterase", "Adenylate cyclase", "Monoamine oxidase", "Na+/K+ ATPase"],
  "Papaverine inhibits phosphodiesterase, which raises cyclic AMP.")
q(124, "The second messenger increased by papaverine is:",
  ["Cyclic AMP", "Cyclic GMP", "Inositol triphosphate", "Diacylglycerol"],
  "Phosphodiesterase inhibition by papaverine increases cyclic AMP.")
q(124, "Increased cyclic AMP produced by papaverine leads to:",
  ["Relaxation of smooth muscles", "Contraction of smooth muscles",
   "Increased peristalsis", "Bronchoconstriction"],
  "The page chain reads: inhibits phosphodiesterase, up cyclic AMP, relaxation of smooth muscles.")
q(124, "Papaverine is used as a smooth muscle relaxant for:",
  ["Biliary colic and ureteric colic", "Bronchial asthma", "Migraine", "Gastric ulcer"],
  "The uses listed are biliary colic and ureteric colic.")
q(124, "A patient with biliary colic is given a smooth muscle relaxant derived from opium that has no opioid (analgesic) action. The drug is:",
  ["Papaverine", "Morphine", "Codeine", "Pethidine"],
  "Papaverine is a natural opiate without opioid action used as a smooth muscle relaxant in biliary colic.")
q(124, "Which natural opiate lacking opioid action is used for cough?",
  ["Noscapine", "Thebaine", "Papaverine", "Pholcodine"],
  "Noscapine is the chemical without opioid action used as an anti-tussive.")
q(124, "Thebaine is grouped with the chemicals:",
  ["Without opioid action", "With opioid action", "That are synthetic", "That are pure antagonists"],
  "Thebaine is listed as 'c' under chemicals without opioid action.")
q(124, "Which of the following is a natural opiate WITH opioid action?",
  ["Codeine", "Noscapine", "Papaverine", "Thebaine"],
  "Only morphine and codeine are listed as chemicals with opioid action; noscapine, papaverine and thebaine lack opioid action.")

unit("Semi-synthetic and Synthetic Opioids",
     "Semi-synthetic opioids are those derived from morphine (diacetylmorphine/heroin, four times as potent as morphine and a drug of abuse; apomorphine, a dopamine agonist used in Parkinson's disease; hydromorphone, ethylmorphine and the non-opioid anti-tussive pholcodine), from codeine (hydrocodone, an analgesic) and from thebaine (buprenorphine, oxycodone and oxymorphone). The synthetic group lists fentanyl, pethidine, loperamide and methadone.")
q(124, "Diacetylmorphine (heroin) is described as having a potency of:",
  ["4 times that of morphine", "Equal to morphine", "10 times that of morphine", "One-fourth of morphine"],
  "The page states potency: 4x morphine for diacetylmorphine (heroin).")
q(124, "Diacetylmorphine (heroin) is categorised as a:",
  ["Drug of abuse", "Drug of choice in terminal cancer pain",
   "First line anti-tussive", "Pure opioid antagonist"],
  "Heroin is labelled a drug of abuse on the page.")
q(124, "Apomorphine is a:",
  ["Dopamine (D) agonist used in Parkinson's disease", "Mu antagonist used in opioid toxicity",
   "Kappa agonist used for pruritus", "Delta agonist used for analgesia"],
  "Apomorphine is listed as a D agonist with the use of Parkinson's disease.")
q(124, "The semi-synthetic opioid used in Parkinson's disease is:",
  ["Apomorphine", "Hydromorphone", "Pholcodine", "Ethylmorphine"],
  "Apomorphine, a dopamine agonist, is used in Parkinson's disease.")
q(124, "Hydromorphone is listed as a semi-synthetic opioid used as an:",
  ["Analgesic", "Anti-tussive", "Anti-diarrhoeal", "Antagonist"],
  "Hydromorphone's entry reads 'analgesic'.")
q(124, "Pholcodine is described as:",
  ["A non-opioid anti-tussive", "A strong analgesic",
   "A pure antagonist", "An anti-diarrhoeal drug"],
  "Pholcodine is labelled 'non-opioid' with the use anti-tussive.")
q(124, "Hydrocodone is derived from:",
  ["Codeine", "Morphine", "Thebaine", "Papaverine"],
  "Hydrocodone appears under the 'derived from codeine' branch as an analgesic.")
q(124, "Buprenorphine is derived from:",
  ["Thebaine", "Morphine", "Codeine", "Papaver somniferum directly"],
  "The 'derived from thebaine' branch lists buprenorphine, oxycodone and oxymorphone.")
q(124, "Oxycodone is derived from thebaine and is used as an:",
  ["Analgesic", "Anti-tussive", "Anti-diarrhoeal", "Antagonist"],
  "Oxycodone is listed under thebaine derivatives with the use 'analgesic'.")
q(124, "Oxymorphone is derived from:",
  ["Thebaine", "Morphine", "Codeine", "Noscapine"],
  "Oxymorphone is the third drug under 'derived from thebaine'.")
q(124, "Which of the following is a SYNTHETIC opioid?",
  ["Fentanyl", "Heroin", "Hydrocodone", "Oxycodone"],
  "The synthetic branch lists fentanyl, pethidine, loperamide and methadone.")
q(124, "Pethidine belongs to which source-based group?",
  ["Synthetic", "Natural opiate", "Semi-synthetic", "Endogenous"],
  "Pethidine is listed in the synthetic group.")
q(124, "Loperamide is classified, by source, as a:",
  ["Synthetic opioid", "Natural opiate", "Semi-synthetic opioid", "Endogenous opioid"],
  "Loperamide appears in the synthetic group.")
q(124, "Methadone is listed under:",
  ["Synthetic opioids", "Natural opiates", "Semi-synthetic opioids", "Pure antagonists"],
  "Methadone is the fourth drug in the synthetic group.")
q(124, "All of the following are semi-synthetic opioids EXCEPT:",
  ["Fentanyl", "Heroin", "Hydromorphone", "Oxycodone"],
  "Fentanyl is synthetic; heroin, hydromorphone and oxycodone are semi-synthetic.")
q(124, "Which semi-synthetic opioid is derived from morphine AND is a drug of abuse?",
  ["Diacetylmorphine (heroin)", "Apomorphine", "Pholcodine", "Hydrocodone"],
  "Heroin (diacetylmorphine) is derived from morphine and is labelled a drug of abuse.")

unit("Classification Based on Opioid Receptor Interaction",
     "The second classification is based on opioid receptor interaction. Agonists are either full agonists or mixed agonist-antagonists, while antagonists are pure antagonists, which are further divided into central and peripheral agents.")
q(124, "Based on opioid receptor interaction, opioids are first divided into:",
  ["Agonists and antagonists", "Natural and synthetic", "Short and long acting", "Central and peripheral"],
  "The receptor-interaction classification splits into agonist and antagonist.")
q(124, "Agonists are further divided into:",
  ["Full agonists and mixed (agonist-antagonists)", "Central and peripheral",
   "Natural and synthetic", "Reversible and irreversible"],
  "Under agonist the page lists 'full agonist' and 'mixed'.")
q(124, "Antagonists in this classification are described as:",
  ["Pure antagonists", "Partial antagonists", "Mixed antagonists", "Competitive agonists"],
  "The antagonist branch leads to 'pure antagonist'.")
q(124, "Pure antagonists are subdivided into:",
  ["Central and peripheral", "Full and partial", "Natural and synthetic", "Short and long acting"],
  "The antagonist branch further divides into central and peripheral.")
q(124, "A drug that is a mixed agonist-antagonist belongs to which limb of the receptor-interaction classification?",
  ["Agonist", "Pure antagonist", "Peripheral antagonist", "Endogenous opioid"],
  "Mixed agonist-antagonists are grouped under agonists.")
q(124, "A peripherally acting pure opioid antagonist would be placed under:",
  ["Antagonist - peripheral", "Agonist - mixed", "Agonist - full", "Endogenous opioid"],
  "Peripheral agents are a subdivision of the pure antagonists.")

unit("Pure Centrally Acting Antagonists: Naloxone",
     "Pure centrally acting antagonists can cross the blood-brain barrier and are the drugs used in opioid toxicity. Naloxone is the shortest acting, is given intravenously (and intranasally in acute toxicity), is the drug of choice in opioid toxicity, and is used off label for valproate-induced CNS depression and clonidine toxicity; its adverse effects - hypertension, arrhythmias and pulmonary edema - follow the surge of catecholamines.")
q(125, "Pure centrally acting antagonists are characterised by their ability to:",
  ["Cross the blood-brain barrier", "Act only on peripheral opioid receptors",
   "Stimulate the kappa receptor", "Release endogenous endorphins"],
  "The heading states that these drugs can cross the blood-brain barrier.")
q(125, "Pure centrally acting antagonists are the drugs used in:",
  ["Opioid toxicity", "Chronic constipation", "Cough suppression", "Parkinson's disease"],
  "The page says these are the drugs used in opioid toxicity.")
q(125, "Naloxone is described as the:",
  ["Shortest acting", "Long acting", "Longest acting", "Ultra-short acting"],
  "Naloxone is labelled 'shortest acting' among the three antagonists.")
q(125, "The route of administration given for naloxone is:",
  ["Intravenous", "Oral", "Intramuscular only", "Subcutaneous only"],
  "The route listed under naloxone is i.v.")
q(125, "In acute opioid toxicity, naloxone can also be given by the:",
  ["Intranasal route", "Oral route", "Rectal route", "Transdermal route"],
  "The page notes intranasal naloxone in acute toxicity.")
q(125, "The drug of choice in opioid toxicity is:",
  ["Naloxone", "Naltrexone", "Nalmifene", "Methylnaltrexone"],
  "Naloxone is labelled DOC in opioid toxicity.")
q(125, "An off-label use of naloxone mentioned on the page is:",
  ["Valproate-induced CNS depression", "Alcohol dependence", "Opioid dependence relapse prevention", "Irritable bowel syndrome"],
  "The off-label uses listed are valproate-induced CNS depression and clonidine toxicity.")
q(125, "The second off-label use of naloxone given on the page is:",
  ["Clonidine toxicity", "Methadone overdose", "Benzodiazepine overdose", "Hepatic encephalopathy"],
  "Clonidine toxicity is the second off-label indication listed.")
q(125, "The adverse effects of naloxone are attributed to increased:",
  ["Catecholamines", "Serotonin", "Histamine", "GABA"],
  "The page states side effects are d/t up catecholamines.")
q(125, "Which of the following is listed as a naloxone adverse effect?",
  ["Pulmonary edema", "Hepatotoxicity", "Dysphoria and depression", "Frank liver failure"],
  "Hypertension, arrhythmias and pulmonary edema are the listed naloxone effects.")
q(125, "Hypertension, arrhythmias and pulmonary edema after naloxone are explained by:",
  ["A surge of catecholamines reversing opioid effect abruptly",
   "Direct mu agonism in the myocardium",
   "Histamine release from mast cells",
   "Antagonism at peripheral delta receptors"],
  "The note attributes these effects to increased catecholamines.")
q(125, "A patient brought drowsy after taking clonidine is given naloxone. This use is:",
  ["An off-label use of naloxone", "The drug of choice indication for naltrexone",
   "Absolutely contraindicated", "A use of nalmifene"],
  "Clonidine toxicity is listed as an off-label use of naloxone.")
q(125, "Which pure centrally acting antagonist is shortest acting and therefore often needs repeated dosing?",
  ["Naloxone", "Naltrexone", "Nalmifene", "Alvimopan"],
  "Naloxone is the shortest acting of the three centrally acting antagonists.")

unit("Nalmifene and Naltrexone",
     "Nalmifene is the long-acting antagonist, while naltrexone is the longest acting and is given orally. Naltrexone is the drug of choice in alcohol dependence and is used in opioid dependence to prevent relapse; its problems are hepatotoxicity (AST/ALT rising to three times normal, or frank liver failure) and dysphoria or depression from mu antagonism, which contraindicates its use.")
q(125, "Nalmifene is described as:",
  ["Long acting", "Shortest acting", "Longest acting", "Ultra-short acting"],
  "Nalmifene's entry reads 'long acting'.")
q(125, "Naltrexone is described as the:",
  ["Longest acting", "Shortest acting", "Short acting", "Ultra-short acting"],
  "Naltrexone is labelled 'longest acting'.")
q(125, "Arranged from shortest to longest acting, the three pure centrally acting antagonists are:",
  ["Naloxone, nalmifene, naltrexone", "Naltrexone, nalmifene, naloxone",
   "Nalmifene, naloxone, naltrexone", "Naloxone, naltrexone, nalmifene"],
  "Naloxone is shortest acting, nalmifene long acting and naltrexone longest acting.")
q(125, "The route of administration given for naltrexone is:",
  ["Oral", "Intravenous", "Intranasal", "Sublingual"],
  "Naltrexone's route is given as oral.")
q(125, "Naltrexone is the drug of choice in:",
  ["Alcohol dependence", "Opioid toxicity", "Biliary colic", "Spasmodic cough"],
  "The DOC label under naltrexone is alcohol dependence.")
q(125, "In opioid dependence, naltrexone is used to:",
  ["Prevent relapse", "Treat acute withdrawal", "Reverse respiratory depression",
   "Potentiate methadone"],
  "Naltrexone is used in opioid dependence to prevent relapse.")
q(125, "The hepatotoxicity of naltrexone is described as an rise of AST/ALT to:",
  ["3 times the normal values", "10 times the normal values",
   "1.5 times the normal values", "Within twice the normal values"],
  "The page says AST/ALT up to 3x normal values.")
q(125, "The severe form of naltrexone hepatotoxicity mentioned is:",
  ["Frank liver failure", "Cirrhosis with portal hypertension",
   "Hepatic adenoma", "Sclerosing cholangitis"],
  "The page lists frank liver failure as the severe outcome.")
q(125, "Dysphoria and depression with naltrexone are attributed to:",
  ["Antagonism at the mu receptor", "Agonism at the kappa receptor",
   "Inhibition of phosphodiesterase", "Excess catecholamine release"],
  "The page explains dysphoria and depression as a consequence of antagonism at the mu receptor.")
q(125, "Because it causes dysphoria and depression, naltrexone use is:",
  ["Contraindicated in depression", "Preferred in depression",
   "Given only intravenously", "Restricted to children"],
  "The page states that because of mu antagonism-related depression, its use is contraindicated.")
q(125, "A patient with alcohol dependence and coexisting major depression is a poor candidate for:",
  ["Naltrexone", "Naloxone", "Acamprosate", "Disulfiram"],
  "Naltrexone causes dysphoria and depression by mu antagonism, so its use is contraindicated in depression.")
q(125, "Monitoring during naltrexone therapy should include:",
  ["Liver function tests (AST/ALT)", "Serum amylase", "Pulmonary function tests", "Serum potassium"],
  "Naltrexone can raise AST/ALT to three times normal and cause frank liver failure, so liver function is monitored.")
q(125, "Which antagonist is taken by mouth for relapse prevention in opioid dependence?",
  ["Naltrexone", "Naloxone", "Nalmifene", "Methylnaltrexone"],
  "Naltrexone is the orally administered, longest acting antagonist used to prevent relapse.")

unit("Mixed Agonist/Antagonists: Nalorphine, Dezocine, Pentazocine and Butorphanol",
     "The mixed agonist/antagonist table lists the drug, its receptor interaction at mu, kappa and delta, and details. Nalorphine (earlier used in opioid toxicity, with fewer side effects because of mu antagonism, but a poor analgesic) and dezocine are mu antagonists with full kappa agonism, whereas pentazocine and butorphanol are mu partial agonists with full kappa agonism. Pentazocine raises heart rate and is contraindicated in a patient with myocardial infarction.")
q(126, "The table on this page lists drug, receptor interaction and:",
  ["Details", "Dose", "Cost", "Route only"],
  "The three column headings are Drug, Receptor interaction and Details.")
q(126, "The receptor interaction columns in the table are, in order:",
  ["mu, kappa and delta", "kappa, delta and mu",
   "delta, mu and kappa", "mu, delta and sigma"],
  "The receptor interaction heading spans the mu, kappa and delta columns.")
q(126, "Nalorphine's receptor interaction is:",
  ["Antagonist at mu and full agonist at kappa", "Partial agonist at mu and antagonist at kappa",
   "Full agonist at mu and delta", "Antagonist at delta only"],
  "Nalorphine is an antagonist at mu and a full agonist at kappa.")
q(126, "The earlier use of nalorphine was:",
  ["Opioid toxicity", "Severe cancer pain", "Cough suppression", "Alcohol dependence"],
  "The details column gives nalorphine's earlier use as opioid toxicity.")
q(126, "Nalorphine is said to have fewer side effects because of antagonism at:",
  ["mu receptor", "delta receptor", "kappa receptor", "NMDA receptor"],
  "The details column reads 'down side effects d/t antagonism at mu'.")
q(126, "The analgesic efficacy of nalorphine is described as:",
  ["Poor", "Excellent", "Superior to morphine", "Equal to fentanyl"],
  "Nalorphine's use is given as analgesic (poor).")
q(126, "Dezocine's receptor interaction is:",
  ["Antagonist at mu and full agonist at kappa", "Partial agonist at mu and antagonist at kappa",
   "Full agonist at mu and kappa", "Antagonist at kappa and delta"],
  "Dezocine is listed as antagonist at mu and full agonist at kappa.")
q(126, "Pentazocine's receptor interaction is:",
  ["Partial agonist at mu and full agonist at kappa", "Antagonist at mu and full agonist at kappa",
   "Full agonist at mu, kappa and delta", "Antagonist at kappa and delta"],
  "Pentazocine is a partial agonist at mu and a full agonist at kappa.")
q(126, "Butorphanol's receptor interaction is:",
  ["Partial agonist at mu and full agonist at kappa", "Antagonist at mu and full agonist at kappa",
   "Full agonist at mu and antagonist at delta", "Partial agonist at kappa and delta"],
  "Butorphanol is a partial agonist at mu and a full agonist at kappa.")
q(126, "The cardiovascular caution listed for pentazocine is:",
  ["It raises heart rate and is contraindicated in MI patients",
   "It causes severe hypotension and is contraindicated in shock",
   "It causes bradycardia and is contraindicated in heart block",
   "It prolongs the QT interval"],
  "The details column states pentazocine increases heart rate and is contraindicated in MI patients.")
q(126, "A patient with acute myocardial infarction and severe pain should not receive:",
  ["Pentazocine", "Morphine", "Fentanyl", "Naloxone"],
  "Pentazocine raises heart rate and is contraindicated in myocardial infarction.")
q(126, "Which two drugs in the table share the interaction 'antagonist at mu plus full agonist at kappa'?",
  ["Nalorphine and dezocine", "Pentazocine and butorphanol",
   "Buprenorphine and nalorphine", "Eluxadoline and dezocine"],
  "Nalorphine and dezocine are both mu antagonists with full kappa agonism.")
q(126, "Which two drugs in the table share the interaction 'partial agonist at mu plus full agonist at kappa'?",
  ["Pentazocine and butorphanol", "Nalorphine and dezocine",
   "Buprenorphine and eluxadoline", "Nalorphine and pentazocine"],
  "Pentazocine and butorphanol are both mu partial agonists with full kappa agonism.")

unit("Eluxadoline, Buprenorphine and the Ceiling Effect",
     "Eluxadoline is a full agonist at mu and kappa and an antagonist at delta, used in irritable bowel syndrome with diarrhoea. Buprenorphine is a partial agonist at mu and an antagonist at kappa; because it binds fast and dissociates slowly (high affinity for mu) it produces no or only mild withdrawal symptoms and is used in opioid toxicity and, thanks to its ceiling effect, in mild to moderate pain. It is contraindicated in labour pain because it may cause naloxone-resistant respiratory depression in the fetus.")
q(126, "Eluxadoline's receptor interaction is:",
  ["Full agonist at mu and kappa, antagonist at delta", "Partial agonist at mu, antagonist at kappa",
   "Antagonist at mu, full agonist at kappa", "Full agonist at all three receptors"],
  "Eluxadoline is a full agonist at mu and kappa and an antagonist at delta.")
q(126, "Eluxadoline is used in:",
  ["Irritable bowel syndrome with diarrhoea", "Opioid-induced constipation",
   "Ulcerative colitis", "Chronic pancreatitis pain"],
  "The details column gives its use as irritable bowel syndrome (IBS) with diarrhoea.")
q(126, "The only drug in the table that is an antagonist at the delta receptor is:",
  ["Eluxadoline", "Buprenorphine", "Pentazocine", "Nalorphine"],
  "Eluxadoline is the delta antagonist in the table.")
q(126, "Buprenorphine's receptor interaction is:",
  ["Partial agonist at mu and antagonist at kappa", "Full agonist at mu and kappa",
   "Antagonist at mu and full agonist at kappa", "Partial agonist at kappa and delta"],
  "Buprenorphine is a partial agonist at mu and an antagonist at kappa.")
q(126, "Buprenorphine binds to the mu receptor:",
  ["Fast, with slow dissociation because of increased affinity",
   "Slowly, with fast dissociation",
   "Irreversibly", "Only at peripheral sites"],
  "The details column says fast binding with slow dissociation d/t increased affinity to mu.")
q(126, "The clinical consequence of buprenorphine's slow dissociation from mu is:",
  ["No or only mild withdrawal symptoms", "Severe withdrawal on stopping",
   "Rapid tolerance", "Marked euphoria"],
  "Fast binding and slow dissociation mean no or only mild withdrawal symptoms.")
q(126, "Buprenorphine is used in mild to moderate pain because of its:",
  ["Ceiling effect", "Very short half-life", "High potency at delta", "Peripheral selectivity"],
  "The details column attributes its use in mild to moderate pain to the ceiling effect.")
q(126, "Buprenorphine is contraindicated in:",
  ["Labour pain", "Myocardial infarction", "Renal colic", "Cough"],
  "Labour pain is listed as a contraindication.")
q(126, "The reason buprenorphine is avoided in labour pain is that it may cause:",
  ["Naloxone-resistant respiratory depression in the fetus",
   "Severe maternal hypertension",
   "Uterine inversion",
   "Postpartum haemorrhage"],
  "The page states it may cause naloxone-resistant respiratory depression in the fetus.")
q(126, "According to the note at the foot of the page, increasing the dose of a drug:",
  ["Increases the drug effect only until the peak effect dose is reached, after which a ceiling is seen",
   "Increases the drug effect indefinitely",
   "Has no relation to drug effect",
   "Produces toxicity before any analgesia"],
  "The note describes a rising effect with dose that plateaus - the ceiling effect - after the peak effect dose is reached.")
q(126, "The ceiling effect described in the note is classically a property of:",
  ["A partial agonist such as buprenorphine", "A full agonist such as morphine",
   "A pure antagonist such as naloxone", "An anti-tussive such as noscapine"],
  "A ceiling effect is the hallmark of a partial agonist, which is why buprenorphine suits mild to moderate pain.")
q(126, "Which drug in the table is useful in BOTH opioid toxicity and mild to moderate pain?",
  ["Buprenorphine", "Nalorphine", "Eluxadoline", "Pentazocine"],
  "Buprenorphine is used in opioid toxicity (fast binding, slow dissociation) and in mild to moderate pain (ceiling effect).")

# ---------------------------------------------------------------------------
# Chapter 32: Opioids: Part 2 (p127-130)
# ---------------------------------------------------------------------------
start(32)
unit("Full Agonist Opioids: Morphine - Pharmacokinetics, Uses and Contraindications",
     "Part 2 opens with the full agonist opioids, beginning with morphine. Its oral bioavailability is low because of extensive first-pass metabolism, so the oral dose exceeds the intravenous dose; it is metabolised in the liver (hence contraindicated in liver and renal failure) and eliminated by the kidney, and its duration of action is attributed to active metabolites. Morphine is the drug of choice in severe pain, but it is absolutely contraindicated in head trauma because it raises intracranial pressure and relatively contraindicated in bronchial asthma because it releases histamine.")
q(127, "The group of opioids with which 'Opioids: Part 2' begins is:",
  ["Full agonist opioids", "Mixed agonist-antagonists", "Pure antagonists", "Peripheral antagonists"],
  "The page heading is 'Full agonist opioids'.")
q(127, "The first full agonist opioid discussed is:",
  ["Morphine", "Codeine", "Pethidine", "Fentanyl"],
  "Morphine is the first drug listed under full agonist opioids.")
q(127, "The oral bioavailability of morphine is low because of:",
  ["High first pass metabolism", "Poor tablet disintegration", "P-glycoprotein efflux in the gut only", "Binding to food"],
  "The pharmacokinetics line states that oral bioavailability is low owing to high first pass metabolism.")
q(127, "Because of first pass metabolism, the oral dose of morphine compared with the intravenous dose is:",
  ["Greater", "Smaller", "Equal", "Half"],
  "The page notes 'oral dose > IV dose'.")
q(127, "Morphine is metabolised in the:",
  ["Liver", "Kidney", "Plasma", "Intestinal mucosa"],
  "The entry reads metabolism: liver.")
q(127, "Metabolism in the liver makes morphine contraindicated in:",
  ["Liver and renal failure", "Peptic ulcer disease", "Glaucoma only", "Asthma only"],
  "The note against metabolism reads 'C/I in liver and renal failure'.")
q(127, "Morphine is eliminated mainly by the:",
  ["Kidney", "Lung", "Bile", "Skin"],
  "The entry reads elimination: kidney.")
q(127, "The duration of action of morphine is attributed to its:",
  ["Active metabolites", "High plasma protein binding", "Enterohepatic circulation", "Slow absorption"],
  "The duration-of-action line is qualified by 'd/t active metabolites'.")
q(127, "Morphine is described as the drug of choice in:",
  ["Severe pain", "Mild pain", "Neuropathic pain only", "Cough"],
  "The uses section of morphine begins with 'DOC in severe pain'.")
q(127, "Which of the following pains is listed as an indication for morphine?",
  ["Pain in cancer", "Tension headache", "Dysmenorrhoea", "Post-herpetic itch"],
  "The list of pains includes labour pain, bone pain, pain in multiple myeloma, MI pain and pain in cancer.")
q(127, "Absolute contraindication to morphine listed on the page is:",
  ["Head trauma", "Bronchial asthma", "Renal colic", "Myocardial infarction"],
  "Head trauma is labelled an absolute contraindication.")
q(127, "Morphine is contraindicated in head trauma because it causes:",
  ["Increased intracranial pressure", "Decreased intracranial pressure", "Cerebral vasoconstriction", "Seizures"],
  "The reason given against head trauma is the rise in intracranial pressure.")
q(127, "Bronchial asthma is listed as what type of contraindication to morphine?",
  ["Relative", "Absolute", "No contraindication", "Only in children"],
  "Bronchial asthma is labelled a relative contraindication.")
q(127, "Morphine is relatively contraindicated in bronchial asthma because it causes increased release of:",
  ["Histamine", "Leukotrienes only", "Acetylcholine", "Serotonin"],
  "The reason given against bronchial asthma is increased release of histamine.")
q(127, "A patient with head injury and a rising intracranial pressure should not receive morphine chiefly because it:",
  ["Raises intracranial pressure further", "Causes histamine release",
   "Is eliminated by the kidney", "Has active metabolites"],
  "Head trauma is an absolute contraindication because morphine raises intracranial pressure.")

unit("Codeine",
     "Codeine is a prodrug: about a tenth of the dose is converted by CYP2D6 to morphine, so increased CYP2D6 activity gives more analgesia but also a risk of respiratory distress, while reduced activity gives poor analgesia. The bulk of the drug (about 90%) is inactivated by glucuronidation and excreted. Codeine is used as an anti-tussive and for mild to moderate pain.")
q(127, "The drug discussed immediately after morphine on this page is:",
  ["Codeine", "Pethidine", "Tramadol", "Fentanyl"],
  "Codeine follows morphine in the full agonist list.")
q(127, "The fraction of codeine that is converted to morphine is:",
  ["About 10% of the drug", "About 90% of the drug", "Half of the drug", "None of the drug"],
  "The metabolism diagram shows 10% of the drug going to morphine.")
q(127, "The enzyme that converts codeine to morphine is:",
  ["CYP2D6", "CYP3A4", "CYP2C19", "Pseudocholinesterase"],
  "The arrow from codeine to morphine is labelled CYP2D6.")
q(127, "The metabolic fate of the remaining (about 90%) fraction of codeine is:",
  ["Glucuronidation to an inactive metabolite that is excreted",
   "Oxidation to morphine",
   "Acetylation to an active metabolite",
   "Excretion unchanged in the urine"],
  "The second branch shows 90% of the drug undergoing glucuronidation to an inactive metabolite that is excreted.")
q(127, "A patient with increased CYP2D6 activity given codeine would be expected to have:",
  ["Increased analgesia with a risk of respiratory distress",
   "No analgesia at all",
   "Only anti-tussive effect",
   "Accumulation of inactive metabolite"],
  "Increased activity of CYP2D6 gives more morphine, hence increased analgesia and a risk of respiratory distress.")
q(127, "A poor metaboliser with decreased CYP2D6 activity given codeine would have:",
  ["Decreased analgesia", "Excessive analgesia", "Hepatotoxicity", "No change in effect"],
  "Decreased CYP2D6 activity means less morphine is formed, so analgesia is reduced.")
q(127, "Codeine is used as an:",
  ["Anti-tussive and for mild to moderate pain", "Anti-diarrhoeal only",
   "Drug of abuse only", "Pure antagonist"],
  "The uses listed are anti-tussive and mild to moderate pain.")
q(127, "Which statement about codeine is correct?",
  ["It is a prodrug partly converted to morphine by CYP2D6",
   "It is a pure antagonist at the mu receptor",
   "It is more potent than morphine",
   "It does not require metabolism for analgesia"],
  "Codeine's analgesia depends on CYP2D6-mediated conversion to morphine, i.e. it is a prodrug.")
q(127, "Respiratory distress as an adverse effect of codeine is explained by:",
  ["Excess formation of morphine in extensive CYP2D6 metabolisers",
   "Histamine release in the bronchi",
   "Direct depression of the cough centre",
   "Accumulation of the glucuronide metabolite"],
  "The diagram links increased CYP2D6 activity with the risk of respiratory distress through excess morphine formation.")

unit("Pethidine (Meperidine): Metabolism, Uses, Side Effects and Contraindications",
     "Pethidine may be used for only 48 hours because of toxicity. Most of the drug becomes meperidinic acid, which is excreted by the kidney, while about a tenth becomes nor-meperidine, a neurotoxic metabolite that is further converted to nor-meperidinic acid. It is a cheaper alternative for severe pain such as labour pain, is the drug of choice for post-operative and post-drug chills, and causes serotonin syndrome, neurotoxicity and hypotension; it is contraindicated in renal failure and with MAO inhibitors.")
q(127, "The maximum duration of use recommended for pethidine (meperidine) is:",
  ["48 hours", "48 days", "7 days", "2 weeks"],
  "The page states maximum duration of use: 48 hr, because of toxicity.")
q(127, "The 48-hour limit on pethidine use is imposed because of:",
  ["Toxicity", "Tolerance", "Cost", "Shortage of the drug"],
  "The limit is qualified by 'd/t toxicity'.")
q(128, "The major fraction of pethidine is metabolised to:",
  ["Meperidinic acid, which is excreted by the kidney",
   "Nor-meperidine, which is neurotoxic",
   "Morphine",
   "Nor-meperidinic acid"],
  "About 90% is metabolised to meperidinic acid, which is excreted by the kidney.")
q(128, "The minor (about 10%) metabolite of pethidine is:",
  ["Nor-meperidine", "Meperidinic acid", "Morphine-6-glucuronide", "Normorphine"],
  "About 10% is converted to nor-meperidine.")
q(128, "Nor-meperidine is important because it is:",
  ["Neurotoxic", "Analgesic", "Anti-tussive", "Hepatotoxic"],
  "Nor-meperidine is labelled neurotoxic.")
q(128, "Nor-meperidine is further metabolised to:",
  ["Nor-meperidinic acid", "Meperidinic acid", "Morphine", "Normorphine"],
  "The metabolic chain continues from nor-meperidine to nor-meperidinic acid.")
q(128, "Nor-meperidinic acid, like meperidinic acid, is:",
  ["Excreted by the kidney", "Excreted in the bile", "Neurotoxic", "Converted back to pethidine"],
  "Both acid metabolites are noted as excreted by the kidney.")
q(128, "Pethidine is described as a cheaper alternative for:",
  ["Severe pain, for example labour pain", "Mild pain", "Cough", "Diarrhoea"],
  "The page says severe pain: cheaper alternative (eg: labour pain).")
q(128, "The drug of choice for post-operative chills is:",
  ["Pethidine", "Morphine", "Tramadol", "Naloxone"],
  "Pethidine is labelled DOC for chills, covering post-operative chills.")
q(128, "Chills occurring after a drug infusion, for example with monoclonal antibodies or amphotericin B, are treated with:",
  ["Pethidine", "Paracetamol", "Naloxone", "Ondansetron"],
  "Post drug chills due to monoclonal antibodies or amphotericin B are listed under the DOC-for-chills indication.")
q(128, "Two causes of post-drug chills listed on the page are:",
  ["Monoclonal antibodies and amphotericin B", "Opioids and benzodiazepines",
   "Statins and fibrates", "Beta blockers and clonidine"],
  "The page names monoclonal antibodies and amphotericin B as causes of post drug chills.")
q(128, "The mechanism quoted for the anti-chills effect of pethidine is agonism at:",
  ["Alpha-2 receptors", "Mu opioid receptors", "Dopamine D2 receptors", "GABA-A receptors"],
  "The mechanism line reads MOA: alpha-2 receptor agonism.")
q(128, "Which of the following is listed as a side effect of pethidine?",
  ["Serotonin syndrome", "QT prolongation", "Hepatotoxicity", "Pulmonary edema"],
  "The side effects list includes serotonin syndrome, neurotoxicity and hypotension.")
q(128, "Hypotension with pethidine calls for cautious use in:",
  ["Hypovolemia and myocardial infarction", "Hepatic failure", "Asthma", "Glaucoma"],
  "The note reads hypotension with cautious use in hypovolemia and MI.")
q(128, "The first contraindication listed for pethidine is:",
  ["Renal failure with accumulation of nor-meperidine", "MAO inhibitor use", "Head trauma", "Bronchial asthma"],
  "C/I 1 is renal failure, because nor-meperidine accumulates.")
q(128, "Renal failure predisposes to pethidine toxicity through accumulation of:",
  ["Nor-meperidine", "Meperidinic acid", "Pethidine glucuronide", "Morphine"],
  "Accumulation of nor-meperidine in renal failure causes neurotoxicity.")
q(128, "The second contraindication listed for pethidine is concomitant use of:",
  ["MAO inhibitors", "Beta blockers", "Benzodiazepines", "Statins"],
  "C/I 2 is MAO inhibitor use.")
q(128, "MAO inhibitors increase the risk of serotonin syndrome with pethidine because they:",
  ["Block formation of meperidinic and nor-meperidinic acid",
   "Induce CYP2D6", "Increase renal excretion", "Release histamine"],
  "The page states that MAO inhibitors block formation of meperidinic and nor-meperidinic acid, leading to neurotoxicity and an increased risk of serotonin syndrome.")
q(128, "A patient on an MAO inhibitor who receives pethidine is at risk of:",
  ["Both neurotoxicity and serotonin syndrome", "Only respiratory depression",
   "Only histamine-mediated bronchospasm", "Only QT prolongation"],
  "The note names neurotoxicity and an increased risk of serotonin syndrome together.")
q(128, "Which opioid has a 48-hour ceiling on use, is the DOC for chills and accumulates a neurotoxic metabolite in renal failure?",
  ["Pethidine (meperidine)", "Morphine", "Codeine", "Tramadol"],
  "All three statements describe pethidine: 48-hour limit, DOC for chills and nor-meperidine accumulation.")

unit("Methadone",
     "Methadone's analgesia begins in about 10 minutes intravenously and about 1 hour orally. Besides analgesia it is used in opioid dependence because the drug is sequestered in tissues, giving sustained effects and only minimal withdrawal symptoms. Its adverse effects are QT prolongation and anti-cholinergic effects.")
q(128, "The time to onset of analgesia with intravenous methadone is:",
  ["About 10 minutes", "About 1 hour", "About 1 minute", "About 6 hours"],
  "The page gives IV route: 10 min for onset of analgesia.")
q(128, "The time to onset of analgesia with oral methadone is:",
  ["About 1 hour", "About 10 minutes", "About 6 hours", "About 30 seconds"],
  "The page gives oral route: 1 hr for onset of analgesia.")
q(128, "Which of the following is a listed side effect of methadone?",
  ["QT prolongation", "Pulmonary edema", "Hepatotoxicity", "Serotonin syndrome"],
  "The side effects listed are QT prolongation and anti-cholinergic effects.")
q(128, "The second side effect listed for methadone is:",
  ["Anti-cholinergic effects", "Neurotoxicity", "Hypotension", "Histamine release"],
  "Along with QT prolongation, anti-cholinergic effects are listed.")
q(128, "Methadone is used in opioid dependence because the drug is:",
  ["Sequestered in tissues, giving sustained effects with minimal withdrawal symptoms",
   "A pure antagonist at the mu receptor",
   "Excreted unchanged by the kidney",
   "Free of any effect on the heart"],
  "The page states the drug is sequestered in tissues, producing sustained effects and minimal withdrawal symptoms.")
q(128, "The sustained effect of methadone in opioid dependence is explained by:",
  ["Sequestration of the drug in tissues", "Enterohepatic circulation",
   "Active renal reabsorption", "Inhibition of CYP3A4"],
  "Tissue sequestration is given as the reason for the sustained effect.")
q(128, "A patient on methadone maintenance develops a prolonged QT interval. The drug-related explanation is:",
  ["Methadone causes QT prolongation", "Methadone causes hypokalaemia",
   "Methadone releases histamine", "Methadone blocks calcium channels"],
  "QT prolongation is a listed adverse effect of methadone.")
q(128, "Apart from opioid dependence, methadone is used as an:",
  ["Analgesic", "Anti-tussive", "Anti-diarrhoeal", "Antagonist"],
  "The uses listed are analgesic and opioid dependence.")

unit("Loperamide, Diphenoxylate and Difenoxin",
     "These agents are used in non-secretory diarrhoea, in irritable bowel syndrome (where loperamide is the drug of choice) and in irinotecan-induced diarrhoea. Loperamide does not cross the blood-brain barrier, so it causes no dependence; to prevent abuse of diphenoxylate and difenoxin, atropine is added to their formulations.")
q(128, "The three anti-diarrhoeal opioids grouped together on this page are:",
  ["Loperamide, diphenoxylate and difenoxin", "Loperamide, codeine and morphine",
   "Diphenoxylate, tramadol and pethidine", "Difenoxin, loperamide and eluxadoline"],
  "The heading groups loperamide, diphenoxylate and difenoxin.")
q(128, "These opioids are used in:",
  ["Non-secretory diarrhoea", "Secretory diarrhoea only", "Constipation", "Vomiting"],
  "The use listed is non-secretory diarrhoea.")
q(128, "The drug of choice in irritable bowel syndrome among these agents is:",
  ["Loperamide", "Diphenoxylate", "Difenoxin", "Codeine"],
  "The page names loperamide as the DOC in irritable bowel syndrome.")
q(128, "Chemotherapy-induced diarrhoea specifically mentioned is that caused by:",
  ["Irinotecan", "Cyclophosphamide", "Methotrexate", "5-fluorouracil only"],
  "Irinotecan-induced diarrhoea is listed as an indication.")
q(128, "Loperamide does not produce dependence because it:",
  ["Does not cross the blood-brain barrier", "Is not an opioid",
   "Is excreted unchanged", "Is a pure antagonist"],
  "The note states loperamide does not cross the blood-brain barrier, hence no dependence.")
q(128, "To prevent dependence on and abuse of diphenoxylate and difenoxin, the formulation contains:",
  ["Atropine", "Naloxone", "Naltrexone", "Hyoscine"],
  "Atropine is added to prevent dependence and abuse of diphenoxylate and difenoxin.")
q(128, "A patient with chemotherapy (irinotecan) induced diarrhoea would be treated with:",
  ["Loperamide", "Eluxadoline", "Alvimopan", "Methylnaltrexone"],
  "Irinotecan-induced diarrhoea is listed under the uses of loperamide, diphenoxylate and difenoxin.")
q(128, "Which anti-diarrhoeal opioid is safest with respect to central dependence?",
  ["Loperamide", "Diphenoxylate", "Difenoxin", "Codeine"],
  "Loperamide does not cross the blood-brain barrier, so it does not cause dependence.")

unit("Tramadol",
     "Tramadol has two components to its analgesia: an opioid component through mu receptor agonism and a non-opioid component through inhibition of serotonin and norepinephrine reuptake, a TCA/SNRI-like effect that makes it useful in neuropathic pain. It is used for mild to moderate pain and for post-operative or drug-induced chills through alpha-2 agonism.")
q(129, "The first drug discussed on this page is:",
  ["Tramadol", "Fentanyl", "Methadone", "Loperamide"],
  "Tramadol begins the page.")
q(129, "Tramadol's effects are divided into:",
  ["Opioid analgesia and non-opioid analgesia", "Central and peripheral analgesia",
   "Analgesia and anti-tussive effect", "Analgesia and anti-diarrhoeal effect"],
  "The effects column splits into opioid analgesia and non-opioid analgesia.")
q(129, "The mechanism of the opioid analgesia of tramadol is:",
  ["Mu receptor agonism", "Kappa receptor antagonism", "NMDA blockade", "GABA-A potentiation"],
  "Opioid analgesia is attributed to mu receptor agonism.")
q(129, "The mechanism of the non-opioid analgesia of tramadol is:",
  ["Inhibition of serotonin and norepinephrine reuptake",
   "Blockade of sodium channels",
   "Inhibition of cyclo-oxygenase",
   "Activation of GABA-B receptors"],
  "Non-opioid analgesia is due to inhibition of serotonin and norepinephrine reuptake.")
q(129, "The non-opioid analgesia of tramadol is described as similar to that of:",
  ["TCA/SNRI drugs", "Benzodiazepines", "Antipsychotics", "Antihistamines"],
  "The page calls the reuptake inhibition a TCA/SNRI-like effect.")
q(129, "The non-opioid component of tramadol makes it useful in:",
  ["Neuropathic pain", "Cancer pain only", "Migraine only", "Biliary colic"],
  "Neuropathic pain is listed as the use of the non-opioid (reuptake inhibiting) component.")
q(129, "Tramadol is used for:",
  ["Mild to moderate pain", "Only severe pain", "Only cough", "Only diarrhoea"],
  "The uses list gives mild to moderate pain.")
q(129, "The anti-chills effect of tramadol is attributed to:",
  ["Alpha-2 agonism", "Kappa antagonism", "NMDA antagonism", "Muscarinic blockade"],
  "Post-operative and drug-induced chills are listed with alpha-2 agonism as the mechanism.")
q(129, "Post-operative or drug-induced chills can be treated with:",
  ["Tramadol", "Naloxone", "Alvimopan", "Methylnaltrexone"],
  "Tramadol is listed for post-operative and drug induced chills.")
q(129, "A patient with neuropathic pain and moderate pain intensity is best served by which drug on this page?",
  ["Tramadol", "Morphine", "Fentanyl", "Loperamide"],
  "Tramadol combines mu agonism with serotonin and norepinephrine reuptake inhibition, suiting neuropathic pain of mild to moderate intensity.")

unit("Fentanyl, Sufentanil, Alfentanil, Remifentanil and Oliceridine",
     "Fentanyl is a common drug of abuse, is 100 times as potent as morphine and is used in anaesthesia. Sufentanil is 1000 times as potent as morphine and is the most potent opioid, has the maximum plasma protein binding and is used during bronchoscopy to inhibit the stress response. Alfentanil is 20 times as potent as morphine and is used for total intravenous anaesthesia. Remifentanil is the shortest and fastest acting, is metabolised by pseudocholinesterase and is given as a continuous intravenous infusion for daycare surgery. Oliceridine is given intravenously for severe pain.")
q(129, "Fentanyl is described on this page as a:",
  ["Common drug of abuse", "Drug of choice for chills", "Pure antagonist", "Anti-diarrhoeal"],
  "Fentanyl is labelled a common drug of abuse.")
q(129, "The potency of fentanyl relative to morphine is:",
  ["100 times", "1000 times", "20 times", "10 times"],
  "Fentanyl's potency is given as 100x morphine.")
q(129, "Fentanyl is used for:",
  ["Anaesthesia", "Cough suppression", "Diarrhoea", "Opioid de-addiction"],
  "The use listed for fentanyl is anaesthesia.")
q(129, "The opioid stated to be the most potent, at 1000 times morphine, is:",
  ["Sufentanil", "Fentanyl", "Alfentanil", "Remifentanil"],
  "Sufentanil is listed at 1000x morphine and labelled the most potent opioid.")
q(129, "The opioid with the maximum plasma protein binding is:",
  ["Sufentanil", "Fentanyl", "Remifentanil", "Alfentanil"],
  "Maximum plasma protein binding is noted for sufentanil.")
q(129, "The opioid used during bronchoscopy to inhibit the stress response is:",
  ["Sufentanil", "Fentanyl", "Remifentanil", "Oliceridine"],
  "The bronchoscopy indication, to inhibit the stress response, is listed under sufentanil.")
q(129, "Alfentanil is used for:",
  ["Anaesthesia, specifically total intravenous anaesthesia (TIVA)",
   "Daycare surgery infusion only",
   "Severe pain by the intravenous route",
   "Post-operative ileus"],
  "Alfentanil's use is given as anaesthesia (TIVA).")
q(129, "The potency of alfentanil relative to morphine is:",
  ["20 times", "100 times", "1000 times", "2 times"],
  "Alfentanil's potency is given as 20x morphine.")
q(129, "The shortest and fastest acting opioid in this group is:",
  ["Remifentanil", "Fentanyl", "Alfentanil", "Sufentanil"],
  "Remifentanil is labelled the shortest and fastest acting.")
q(129, "Remifentanil is metabolised by:",
  ["Pseudocholinesterase", "CYP3A4", "CYP2D6", "Monoamine oxidase"],
  "Metabolism by pseudocholinesterase is stated for remifentanil.")
q(129, "Because of its pharmacokinetics, remifentanil is used as:",
  ["A continuous intravenous infusion for daycare surgeries",
   "A weekly depot injection",
   "An oral maintenance analgesic",
   "A transdermal patch"],
  "The use listed is continuous IV infusion for daycare surgeries.")
q(129, "Oliceridine is given by the intravenous route for:",
  ["Severe pain", "Mild pain", "Cough", "Diarrhoea"],
  "Oliceridine's use is IV route for severe pain.")
q(129, "Arrange these opioids in increasing order of potency relative to morphine:",
  ["Alfentanil < fentanyl < sufentanil", "Fentanyl < alfentanil < sufentanil",
   "Sufentanil < fentanyl < alfentanil", "Alfentanil < sufentanil < fentanyl"],
  "Alfentanil is 20x, fentanyl 100x and sufentanil 1000x morphine.")
q(129, "Which opioid is preferred when a very short, rapidly titratable effect is needed during daycare surgery?",
  ["Remifentanil", "Methadone", "Morphine", "Codeine"],
  "Remifentanil is the shortest and fastest acting opioid and is given as a continuous IV infusion for daycare surgeries.")

unit("Peripheral Opioid Antagonists",
     "Peripheral antagonists do not cross the blood-brain barrier and are used for their action on the gut. Alvimopan is for short-term use only, is given for post-operative ileus and carries an FDA black box warning for myocardial infarction. Methylnaltrexone, naloxegol and naldemedine are used for opioid-induced constipation.")
q(129, "Peripheral opioid antagonists are characterised by their inability to:",
  ["Cross the blood-brain barrier", "Bind opioid receptors", "Be absorbed orally", "Reach the kidney"],
  "The note states that peripheral antagonists do not cross the blood-brain barrier.")
q(129, "Peripheral antagonists are used for their action on the:",
  ["Gastrointestinal tract", "Central nervous system", "Heart", "Lung"],
  "They are used for action on the GIT.")
q(129, "The restriction on alvimopan use is that it is:",
  ["For short term use only", "For lifelong use", "Restricted to children", "Given only intravenously"],
  "Alvimopan is noted as being for short term use only.")
q(129, "Alvimopan is used for:",
  ["Post-operative ileus", "Opioid-induced constipation", "Irritable bowel syndrome with diarrhoea", "Chemotherapy-induced diarrhoea"],
  "The use listed for alvimopan is post-operative ileus.")
q(129, "The serious adverse effect of alvimopan that carries an FDA black box warning is:",
  ["Myocardial infarction", "Hepatotoxicity", "Pulmonary edema", "Seizures"],
  "The side effect listed is MI, with a black box warning by the FDA.")
q(129, "Which peripheral antagonist carries an FDA black box warning?",
  ["Alvimopan", "Methylnaltrexone", "Naloxegol", "Naldemedine"],
  "Only alvimopan is listed with a black box warning.")
q(129, "The peripheral antagonists used for opioid-induced constipation include all of the following EXCEPT:",
  ["Alvimopan", "Methylnaltrexone", "Naloxegol", "Naldemedine"],
  "Methylnaltrexone, naloxegol and naldemedine are listed for opioid-induced constipation; alvimopan is for post-operative ileus.")
q(129, "A patient on long-term morphine for cancer pain develops severe constipation. The most appropriate drug class is a:",
  ["Peripheral opioid antagonist", "Centrally acting antagonist",
   "Mixed agonist-antagonist", "Full agonist"],
  "Peripheral antagonists act on the gut without entering the brain, so analgesia is preserved while constipation is relieved.")
q(129, "Why do peripheral antagonists not reverse analgesia?",
  ["They do not cross the blood-brain barrier and act only on the gut",
   "They are partial agonists",
   "They are rapidly metabolised",
   "They block only delta receptors"],
  "Because they fail to cross the blood-brain barrier, their action is confined to the gastrointestinal tract.")

unit("Opioid Dependence: Tolerance and Withdrawal",
     "Tolerance is the reduction of effect with the same dose on continuous dosing, produced by receptor desensitisation and downregulation. Tolerance develops at different rates for different effects: none or minimal for miosis, moderate for other opioid effects and fastest (tachyphylaxis) for euphoria. Withdrawal symptoms are the opposite of mu receptor agonism - for example mydriasis - and their severity is proportional to the dose and the potency of the drug.")
q(129, "Tolerance is defined on the page as:",
  ["Decreased effect with the same dose on continuous dosage",
   "Increased effect with the same dose",
   "Loss of effect after a single dose",
   "Need for a lower dose over time"],
  "The definition given is decreased effect with the same dose on continuous dosage.")
q(129, "The two receptor mechanisms said to underlie tolerance are:",
  ["Receptor desensitisation and receptor downregulation",
   "Receptor upregulation and supersensitivity",
   "Enzyme induction and enzyme inhibition",
   "Increased absorption and decreased excretion"],
  "The page lists receptor desensitisation and receptor downregulation.")
q(130, "Tolerance to miosis with opioids is:",
  ["None or minimal", "Moderate", "Fastest of all effects", "Complete within a week"],
  "The page says no or minimal tolerance develops to miosis.")
q(130, "Tolerance to the other opioid effects (apart from miosis and euphoria) is:",
  ["Moderate", "None", "Fastest", "Absent"],
  "Moderate tolerance is listed for other opioid effects.")
q(130, "The effect to which tolerance develops fastest (tachyphylaxis) is:",
  ["Euphoria", "Miosis", "Constipation", "Analgesia"],
  "Fastest tolerance, described as tachyphylaxis, is to euphoria.")
q(130, "Tachyphylaxis in opioid use refers to rapid tolerance to:",
  ["Euphoria", "Miosis", "Constipation", "Respiratory depression"],
  "Euphoria is the effect labelled with fastest tolerance or tachyphylaxis.")
q(130, "Opioid withdrawal symptoms are described as:",
  ["Effects opposite to mu receptor agonism", "Effects identical to mu receptor agonism",
   "Effects of kappa antagonism", "Effects of delta agonism"],
  "The page states withdrawal symptoms are the effect opposite to mu receptor agonism.")
q(130, "The example given of an opioid withdrawal sign is:",
  ["Mydriasis", "Miosis", "Bradycardia", "Constipation"],
  "Mydriasis is quoted as the example of an effect opposite to mu agonism.")
q(130, "The severity of opioid withdrawal is proportional to:",
  ["Both the dose and the potency of the drug", "The dose only",
   "The duration of drug use only", "The route of administration only"],
  "The page notes severity is proportional to dose and to potency.")
q(130, "A heroin user who stops the drug develops dilated pupils. This is explained by:",
  ["Withdrawal producing effects opposite to mu receptor agonism",
   "Direct kappa receptor stimulation",
   "Anticholinergic contamination of the drug",
   "Tolerance to miosis"],
  "Withdrawal effects are opposite to mu agonism, so miosis of intoxication is replaced by mydriasis.")
q(130, "Which opioid effect shows the least tolerance on continued use?",
  ["Miosis", "Euphoria", "Analgesia", "Sedation"],
  "No or minimal tolerance develops to miosis, which is why pin-point pupils persist in chronic users.")

unit("De-addiction",
     "De-addiction has two arms: reducing withdrawal symptoms and preventing relapse. Withdrawal is reduced by starting the patient on methadone or buprenorphine, which produces only mild symptoms on cessation, followed by symptomatic treatment with a beta blocker, clonidine and similar drugs. Relapse is prevented with the opioid receptor blocker oral naltrexone, which abolishes the euphoria of a dose and so reduces the desire to consume the drug.")
q(130, "De-addiction in opioid dependence has how many components?",
  ["Two - reducing withdrawal symptoms and preventing relapse",
   "One - only detoxification",
   "Three - detoxification, rehabilitation and surgery",
   "Four - including vaccination"],
  "The two headings are 1. reduce withdrawal symptoms and 2. prevent relapse.")
q(130, "The drugs named to reduce withdrawal symptoms are:",
  ["Methadone and buprenorphine", "Naltrexone and naloxone",
   "Clonidine and naltrexone", "Loperamide and diphenoxylate"],
  "The withdrawal arm names methadone and buprenorphine.")
q(130, "Buprenorphine is preferred in de-addiction because on cessation it produces:",
  ["Only mild symptoms", "No symptoms at all", "Severe symptoms", "Immediate relapse"],
  "The page notes mild symptoms on cessation with buprenorphine.")
q(130, "After the substitute opioid, withdrawal is further managed with symptomatic treatment using:",
  ["A beta blocker and clonidine", "Naloxone and naltrexone",
   "Loperamide and atropine", "Ondansetron and metoclopramide"],
  "Symptomatic treatment is listed as beta blocker, clonidine etc.")
q(130, "Clonidine is used in opioid de-addiction as:",
  ["Symptomatic treatment of withdrawal", "A substitute for the opioid",
   "A relapse-preventing blocker", "An anti-diarrhoeal"],
  "Clonidine appears under symptomatic treatment of withdrawal symptoms.")
q(130, "The drug used to prevent relapse in opioid dependence is:",
  ["Oral naltrexone", "Oral methadone", "Intravenous naloxone", "Buprenorphine"],
  "Relapse prevention is by the opioid receptor blocker oral naltrexone.")
q(130, "Naltrexone prevents relapse by:",
  ["Blocking the euphoria of a dose, thereby reducing the desire to consume the drug",
   "Substituting for the opioid",
   "Sedating the patient",
   "Stimulating the reward pathway"],
  "The page states naltrexone blocks the euphoria on intake, which lowers the desire for consumption.")
q(130, "Which statement about de-addiction is correct?",
  ["Withdrawal is reduced with methadone or buprenorphine and relapse is prevented with naltrexone",
   "Withdrawal is reduced with naltrexone and relapse is prevented with methadone",
   "Both arms use naloxone",
   "Both arms use loperamide"],
  "The page separates the two arms: methadone/buprenorphine for withdrawal and naltrexone for relapse prevention.")
q(130, "A patient who has completed withdrawal and wants to avoid going back to heroin should be offered:",
  ["Oral naltrexone", "Intravenous naloxone", "Oral methadone indefinitely", "Alvimopan"],
  "Oral naltrexone is the opioid receptor blocker used to prevent relapse.")
finish()
