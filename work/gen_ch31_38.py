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

# ---------------------------------------------------------------------------
# Chapter 33: Affect Disorders: Part 1 (p131-133)
# ---------------------------------------------------------------------------
start(33)
unit("BDNF Hypothesis and the Management of Mania",
     "Part 1 of the affect-disorders chapters opens with the BDNF hypothesis: brain derived neurotrophic factor, when increased, produces mania, when decreased produces depression, and when it fluctuates produces bipolar disorder - rapid cycling meaning more than four episodes a year. Management of mania is then taken up drug by drug, beginning with lithium.")
q(131, "The hypothesis with which 'Affect Disorders: Part 1' begins is the:",
  ["BDNF hypothesis", "Monoamine hypothesis only", "Dopamine hypothesis", "GABA hypothesis"],
  "The first heading on the page is the BDNF hypothesis.")
q(131, "BDNF stands for:",
  ["Brain derived neurotrophic factor", "Brain derived nerve factor",
   "Bipolar disorder nerve factor", "Beta derived neurotrophic factor"],
  "BDNF is expanded as brain derived neurotrophic factor.")
q(131, "According to the BDNF hypothesis, an increase in BDNF produces:",
  ["Mania", "Depression", "Bipolar disorder", "Schizophrenia"],
  "The schema shows increased BDNF leading to mania.")
q(131, "According to the BDNF hypothesis, a decrease in BDNF produces:",
  ["Depression", "Mania", "Bipolar disorder", "Anxiety"],
  "Decreased BDNF is linked to depression in the schema.")
q(131, "Fluctuating BDNF levels are said to produce:",
  ["Bipolar disorder", "Unipolar depression", "Schizoaffective disorder", "Generalised anxiety disorder"],
  "Fluctuating BDNF is linked to bipolar disorder.")
q(131, "Rapid cycling in bipolar disorder is defined on the page as more than how many episodes per year?",
  ["4", "2", "6", "12"],
  "The page defines rapid cycles as more than 4 times per year.")
q(131, "The drug with which the management of mania begins is:",
  ["Lithium", "Valproate", "Carbamazepine", "Haloperidol"],
  "Under 'management of mania' the first drug discussed is lithium.")
q(131, "A patient with four mood swings in a year, swinging between elation and depression, is described as:",
  ["A rapid cycler with fluctuating BDNF", "A unipolar depressive",
   "A case of schizoaffective disorder", "Having treatment-resistant depression"],
  "Fluctuating BDNF produces bipolar disorder, and more than four cycles a year is rapid cycling.")

unit("Lithium: Mechanism of Action",
     "Lithium's mechanism is explained through two pathways that change BDNF synthesis. One runs from activation of the Frizzled (Fz) receptor through GSK-3 (glycogen synthase kinase-3), which breaks beta-catenin, with reduced nuclear uptake and reduced neuroplasticity. The other runs from activation of the Gq subtype of GPCR at the membrane through PIP2 (phospho inositol bisphosphates) to IP3, inositol recycling and inositol monophosphatase, giving IP (inositol monophosphate) and changes in BDNF with neuroplasticity and neuroprotection. Lithium acts according to the prevailing BDNF concentration, takes weeks to act, is therefore not effective in acute mania, controls mania and is a mood stabiliser.")
q(131, "The two pathways described for lithium's mechanism of action are headed as:",
  ["A pathway to decreased BDNF synthesis and a pathway to increased BDNF synthesis",
   "A dopaminergic and a serotonergic pathway",
   "A renin and an aldosterone pathway",
   "A hepatic and a renal pathway"],
  "The mechanism section splits into pathway a for decreased BDNF synthesis and pathway b for increased BDNF synthesis.")
q(131, "The receptor whose activation begins the Frizzled pathway is:",
  ["Frizzled (Fz) receptor", "Gq subtype of GPCR", "NMDA receptor", "Tyrosine kinase receptor"],
  "The first step of pathway a is activation of the Frizzled (Fz) receptor.")
q(131, "The receptor whose activation begins the second pathway is:",
  ["Gq subtype of GPCR", "Frizzled receptor", "Gs subtype of GPCR", "Gi subtype of GPCR"],
  "Pathway b begins with activation of the Gq subtype of GPCR.")
q(131, "GSK-3 in lithium's mechanism stands for:",
  ["Glycogen synthase kinase-3", "Guanylate synthase kinase-3",
   "Glutamate synthase kinase-3", "G-protein coupled serine kinase-3"],
  "GSK-3 is expanded as glycogen synthase kinase-3.")
q(131, "In the Frizzled pathway, GSK-3 is described as acting on:",
  ["Beta-catenin, which it breaks", "Glycogen, which it synthesises",
   "IP3, which it recycles", "BDNF, which it phosphorylates"],
  "The pathway shows GSK-3 breaking beta-catenin.")
q(131, "PIP2 in the Gq pathway is expanded as:",
  ["Phospho inositol bisphosphates", "Phospho inositol triphosphate",
   "Phosphatidyl inositol kinase", "Phosphorylated inositol monophosphate"],
  "PIP2 is written as phospho inositol bisphosphates.")
q(131, "PIP2 is cleaved to give:",
  ["IP3", "cAMP", "DAG only", "Inositol monophosphatase"],
  "The Gq pathway runs from PIP2 to IP3.")
q(131, "The enzyme of the inositol cycle named in the pathway is:",
  ["Inositol monophosphatase", "Inositol cyclase", "Phospholipase A2", "Adenylate cyclase"],
  "The pathway names inositol monophosphatase, which lithium inhibits.")
q(131, "IP in the lithium pathway stands for:",
  ["Inositol monophosphate", "Inositol triphosphate", "Inositol bisphosphate", "Inositol kinase"],
  "IP is expanded on the page as inositol monophosphate.")
q(131, "The two beneficial consequences written at the end of the pathways are:",
  ["Neuroplasticity and neuroprotection", "Sedation and hypnosis",
   "Analgesia and anaesthesia", "Diuresis and natriuresis"],
  "The pathway ends with neuroplasticity and neuroprotection.")
q(131, "The statement 'lithium acts based on BDNF concentration' means that lithium:",
  ["Normalises BDNF, lowering it when high and raising it when low",
   "Always increases BDNF", "Always decreases BDNF", "Has no effect on BDNF"],
  "The note says lithium acts based on the prevailing BDNF concentration, which is why it works in both mania and depression.")
q(131, "Lithium is not effective in acute mania because:",
  ["It takes weeks to act", "It is only a prophylactic drug",
   "It is not absorbed orally", "It is rapidly excreted"],
  "The page notes that lithium needs weeks to act and is therefore not effective in acute mania.")
q(131, "Lithium's role in mania is best described as that of a:",
  ["Mood stabiliser used to control mania", "Rapidly acting sedative",
   "Antipsychotic", "Antidepressant"],
  "Lithium controls mania and is labelled a mood stabiliser.")

unit("Lithium: Uses",
     "Lithium is the drug of choice for prophylaxis of mania and for bipolar disorder, and is also used for hypnic headache and for mania in the second and third trimesters of pregnancy. Its other uses are unipolar depression that has not responded to SSRI/SNRI and, as an atypical use, neutropenia or leukopenia.")
q(131, "Lithium is the drug of choice for:",
  ["Prophylaxis of mania", "Acute mania", "Acute depression", "Status epilepticus"],
  "The uses column names prophylaxis of mania under DOC.")
q(131, "The second drug-of-choice indication listed for lithium is:",
  ["Bipolar disorder", "Unipolar depression", "Migraine", "Neuropathic pain"],
  "Bipolar disorder is listed under the DOC indications for lithium.")
q(131, "The headache listed as an indication for lithium is:",
  ["Hypnic headache", "Migraine", "Cluster headache", "Tension headache"],
  "Hypnic headache, described as sleep related, is listed as a use of lithium.")
q(131, "In pregnancy, lithium may be used for mania during:",
  ["The second and third trimesters", "The first trimester only",
   "The entire pregnancy", "No trimester at all"],
  "Lithium is listed for mania in the second and third trimesters, avoiding the first trimester because of Ebstein's anomaly.")
q(131, "Among the other uses of lithium is unipolar depression that:",
  ["Has not responded to SSRI/SNRI", "Is newly diagnosed",
   "Occurs with psychosis", "Occurs in children"],
  "Unipolar depression is listed as another use when there is no response to SSRI/SNRI.")
q(131, "The atypical use of lithium listed on the page is:",
  ["Neutropenia or leukopenia", "Hypertension", "Epilepsy", "Migraine prophylaxis"],
  "Neutropenia and leukopenia are labelled an atypical use of lithium.")
q(131, "A patient with bipolar disorder who needs long term prophylaxis should receive:",
  ["Lithium", "A benzodiazepine", "An atypical antipsychotic only during attacks", "Carbamazepine as first choice"],
  "Lithium is the DOC for prophylaxis of mania and for bipolar disorder.")

unit("Lithium: Side Effects",
     "Lithium causes hypothyroidism by blocking TSH receptors (a Gq-like receptor), obesity, tremors (fine tremors at normal plasma concentration and coarse tremors as a sign of toxicity), hypercalcaemia from raised PTH, acne and nephrogenic diabetes insipidus by blocking the vasopressin-2 receptor - for which amiloride is the drug of choice, better than thiazides. Ebstein's anomaly, with a hypoplastic right ventricle and atrialisation of the ventricle, makes lithium contraindicated in the first trimester; in that situation mania is treated with an atypical antipsychotic such as aripiprazole.")
q(132, "Hypothyroidism caused by lithium is attributed to block of:",
  ["TSH receptors", "Thyroid peroxidase", "Sodium iodide symporter", "Thyroxine binding globulin"],
  "The side effect list attributes hypothyroidism to block of TSH receptors.")
q(132, "The TSH receptor is described on the page as similar to which G protein subtype?",
  ["Gq", "Gs", "Gi", "G12/13"],
  "The note says TSH receptors are similar to Gq.")
q(132, "Which endocrine effect is listed as a lithium side effect?",
  ["Hypothyroidism", "Hyperthyroidism", "Diabetes mellitus", "Addison's disease"],
  "Hypothyroidism, from TSH receptor block, is the endocrine side effect listed.")
q(132, "Lithium tremors are graded by:",
  ["Plasma concentration - fine tremors normally, coarse tremors in toxicity",
   "Duration of therapy only", "Age of the patient only", "Renal function only"],
  "The page links tremors to plasma concentration, with fine tremors at normal levels and coarse tremors in toxicity.")
q(132, "Fine tremors with lithium indicate:",
  ["A normal plasma concentration", "Toxicity", "Permanent cerebellar damage", "Thyroid dysfunction"],
  "Normal plasma concentration gives fine tremors.")
q(132, "Coarse tremors with lithium indicate:",
  ["Toxicity", "A normal plasma concentration", "Hypothyroidism", "Hypercalcaemia"],
  "Coarse tremors are listed under toxicity.")
q(132, "Hypercalcaemia with lithium is attributed to:",
  ["Increased PTH", "Increased vitamin D", "Bone metastasis", "Increased calcitonin"],
  "The list attributes hypercalcaemia to raised PTH.")
q(132, "Ebstein's anomaly due to lithium is described as:",
  ["Hypoplastic right ventricle with atrialisation of the ventricle",
   "Hypoplastic left ventricle", "Atrial septal defect", "Coarctation of the aorta"],
  "The page describes Ebstein's anomaly as a hypoplastic right ventricle with atrialisation of the ventricle.")
q(132, "Because of Ebstein's anomaly, lithium is contraindicated in:",
  ["The first trimester of pregnancy", "The second trimester", "The third trimester", "Lactation only"],
  "Ebstein's anomaly makes lithium contraindicated in the first trimester.")
q(132, "The recommended treatment of mania in the first trimester of pregnancy is:",
  ["Atypical antipsychotics such as aripiprazole", "Lithium", "Valproate", "Carbamazepine"],
  "The note states that mania in the first trimester of pregnancy is treated with atypical antipsychotics such as aripiprazole.")
q(132, "Diabetes insipidus caused by lithium is due to block of the:",
  ["Vasopressin-2 (V2) receptor", "Vasopressin-1 receptor", "Aldosterone receptor", "ENaC channel"],
  "The list attributes diabetes insipidus to block of the vasopressin-2 receptor.")
q(132, "The drug of choice for lithium-induced diabetes insipidus is:",
  ["Amiloride", "Thiazide", "Furosemide", "Desmopressin"],
  "The page gives DOC for treatment as amiloride, superior to thiazide.")
q(132, "In lithium-induced diabetes insipidus, amiloride is preferred over thiazide because it:",
  ["Directly blocks lithium entry into the collecting duct principal cells",
   "Is a stronger diuretic",
   "Corrects the hypercalcaemia",
   "Replaces vasopressin"],
  "The page ranks amiloride above thiazide as the DOC for this indication.")
q(132, "Which of the following is NOT listed as a side effect of lithium?",
  ["Hypoglycaemia", "Acne", "Obesity", "Diabetes insipidus"],
  "Acne, obesity and diabetes insipidus are listed; hypoglycaemia is not.")
q(132, "A patient on lithium develops polyuria and polydipsia. The mechanism is:",
  ["Block of vasopressin-2 receptors in the collecting duct",
   "Block of TSH receptors", "Raised PTH", "Block of ENaC"],
  "Nephrogenic diabetes insipidus from lithium is due to block of the vasopressin-2 receptor.")

unit("Lithium: Toxicity and Therapeutic Drug Monitoring",
     "Lithium toxicity runs a spectrum from the mildest features - nausea, vomiting and profuse diarrhoea needing no intervention - through ataxia, dysarthria and coarse tremors with cerebellar signs, to arrhythmia, seizures, coma and death. Because lithium has a low therapeutic index it needs therapeutic drug monitoring: blood is sampled days after starting (half-life permitting steady state) and hours after the last dose. Plasma concentrations are expressed in meq/L, with a normal or prophylactic range up to 1.0, an acute treatment range up to 1.5, toxicity beyond that and dialysis indicated at 4.0.")
q(132, "The mildest features of lithium toxicity listed are:",
  ["Nausea, vomiting and profuse diarrhoea", "Ataxia and dysarthria", "Arrhythmia and seizures", "Coma"],
  "Nausea, vomiting and profuse diarrhoea head the toxicity spectrum as the mildest features.")
q(132, "The intervention required for the mildest grade of lithium toxicity is:",
  ["No intervention", "Immediate dialysis", "Gastric lavage", "Intravenous calcium"],
  "The mildest column is marked 'no intervention'.")
q(132, "Features of the middle grade of lithium toxicity include:",
  ["Ataxia, dysarthria and coarse tremors with cerebellar signs",
   "Nausea and vomiting only",
   "Coma and death",
   "Arrhythmia and seizures"],
  "Ataxia, dysarthria and coarse tremors or cerebellar symptoms form the middle grade.")
q(132, "The severest grade of lithium toxicity comprises:",
  ["Arrhythmia, seizures, coma and death", "Nausea and vomiting",
   "Fine tremors", "Acne"],
  "Arrhythmia, seizures, coma and death are the features of severe toxicity.")
q(132, "Therapeutic drug monitoring of lithium is done because of its:",
  ["Low therapeutic index", "Long half-life only", "High cost", "Poor absorption"],
  "The page states monitoring is done because of the low therapeutic index.")
q(132, "The blood sample for lithium monitoring is taken:",
  ["Days after starting lithium and hours after the last dose",
   "Immediately after the first dose",
   "Once a year", "Only when toxicity is suspected"],
  "The page says the sample is taken days after starting, to achieve steady state, and hours after the last dose.")
q(132, "Steady state plasma concentration of lithium is achieved after starting therapy because of its:",
  ["Half-life of several hours", "Very short half-life of minutes",
   "Zero order kinetics", "Enterohepatic circulation"],
  "The note quotes a half-life in hours and advises sampling days after starting to reach steady state.")
q(132, "Plasma lithium concentration is expressed in:",
  ["meq/L", "mg/dL", "mmol/kg", "ng/mL"],
  "The scale on the page is labelled meq/L.")
q(132, "The normal or prophylactic range of plasma lithium is up to:",
  ["1.0 meq/L", "1.5 meq/L", "4.0 meq/L", "0.1 meq/L"],
  "The normal or prophylactic range on the scale runs up to 1.0 meq/L.")
q(132, "The plasma concentration aimed at during acute treatment with lithium is up to:",
  ["1.5 meq/L", "1.0 meq/L", "4.0 meq/L", "0.5 meq/L"],
  "The acute treatment range is given as up to 1.5 meq/L.")
q(132, "The plasma lithium concentration at which dialysis is advised for treatment is:",
  ["4.0 meq/L", "1.5 meq/L", "1.0 meq/L", "2.0 meq/L"],
  "Dialysis for treatment is advised at 4.0 meq/L.")
q(132, "A patient on lithium is found to have a plasma level of 1.8 meq/L with coarse tremors and dysarthria. This level lies in the:",
  ["Toxic range, above the acute treatment target of 1.5 meq/L",
   "Normal prophylactic range",
   "Range requiring dialysis",
   "Sub-therapeutic range"],
  "Toxicity begins above the acute treatment range of 1.5 meq/L, and coarse tremors with dysarthria are toxic features.")

unit("Lithium: Drug Interactions",
     "Lithium interacts through its structural similarity to sodium: any state of sodium deficiency makes the tubule reabsorb lithium compensatorily and precipitates toxicity. The causes of sodium deficiency listed are diuretics (thiazides more than potassium-sparing diuretics more than loop diuretics), vomiting and diarrhoea, and fasting. Drugs that reduce lithium excretion and cause toxicity are ACE inhibitors and ARBs (through the filtration fraction) and NSAIDs (through prostaglandin blockade constricting the afferent arteriole). Non-depolarising muscle relaxants have their effect augmented by lithium, so lithium is stopped one to two days before surgery.")
q(132, "The basis of most lithium drug interactions is the structural similarity between lithium and:",
  ["Sodium", "Potassium", "Calcium", "Magnesium"],
  "The drug interaction section begins with the structural similarity of sodium with lithium.")
q(132, "Sodium deficiency causes lithium toxicity by:",
  ["Compensatory tubular reabsorption of lithium",
   "Increased absorption of lithium from the gut",
   "Displacement of lithium from plasma proteins",
   "Inhibition of lithium metabolism in the liver"],
  "Deficiency of sodium leads to compensatory tubular reabsorption of lithium and therefore toxicity.")
q(133, "Among diuretics, the risk of lithium toxicity is greatest with:",
  ["Thiazides", "Loop diuretics", " Potassium-sparing diuretics", "Carbonic anhydrase inhibitors"],
  "The order given is thiazides greater than potassium-sparing diuretics greater than loop diuretics.")
q(133, "The diuretics that increase lithium clearance and so can lower lithium levels are:",
  ["Mannitol and carbonic anhydrase inhibitors", "Thiazides and amiloride",
   "Loop diuretics and spironolactone", "Osmotic diuretics only"],
  "The note lists mannitol and carbonic anhydrase inhibitors as increasing lithium clearance through increased diuresis.")
q(133, "A patient on lithium presents with vomiting and features of lithium toxicity. The first investigation advised is:",
  ["Serum lithium measurement", "Serum electrolytes", "Thyroid function tests", "Renal biopsy"],
  "The page advises measuring serum lithium first when a patient presents with features of lithium toxicity.")
q(133, "The differential diagnosis to be excluded in that setting, by measuring serum electrolytes, is:",
  ["Dyselectrolytaemia", "Hypothyroidism", "Addison's disease", "Meningitis"],
  "Dyselectrolytaemia is the differential, excluded by measuring serum electrolytes.")
q(133, "Fasting in a patient on lithium causes toxicity because it:",
  ["Reduces sodium intake", "Increases lithium absorption", "Induces CYP enzymes", "Alkalinises the urine"],
  "Fasting is listed as causing lithium toxicity through reduced sodium intake.")
q(133, "ACE inhibitors and ARBs cause lithium toxicity by altering the:",
  ["Filtration fraction", "Tubular secretion of potassium", "Glomerular basement membrane", "Renal blood flow only in the medulla"],
  "The mechanism given for ACE inhibitors and ARBs is a change in filtration fraction.")
q(133, "NSAIDs precipitate lithium toxicity by:",
  ["Blocking prostaglandin synthesis and constricting the afferent arteriole",
   "Inducing CYP3A4", "Displacing lithium from albumin",
   "Increasing sodium excretion"],
  "NSAIDs block prostaglandin synthesis, which constricts the afferent arteriole and reduces lithium excretion.")
q(133, "Non-depolarising muscle relaxants interact with lithium in that their effect is:",
  ["Augmented by lithium", "Abolished by lithium", "Unchanged by lithium", "Shortened by lithium"],
  "The page states the effect of non-depolarising muscle relaxants is augmented by lithium.")
q(133, "Before elective surgery, lithium should be stopped:",
  ["24 to 48 hours prior to surgery", "One week prior to surgery",
   "On the morning of surgery only", "Not at all"],
  "Lithium is stopped 24 to 48 hours before surgery because it augments non-depolarising muscle relaxants.")

unit("Other Drugs Used in Mania",
     "Acute mania is treated with valproate (the drug of choice in rapid cyclers), oxcarbazepine or carbamazepine, lamotrigine, topiramate, gabapentin and the atypical antipsychotics such as aripiprazole, which are the drug of choice for acute mania because they act fastest. The drug of choice for acute mania overall is an atypical antipsychotic; lithium is started prophylactically and benzodiazepines are used as add-on drugs.")
q(133, "In acute mania, the drug of choice is:",
  ["An atypical antipsychotic", "Lithium", "Valproate", "Gabapentin"],
  "The right-hand column names an atypical antipsychotic as the treatment of choice in acute mania.")
q(133, "The reason atypical antipsychotics are the drug of choice in acute mania is:",
  ["They have the fastest action", "They are the cheapest",
   "They are the safest in pregnancy", "They need no monitoring"],
  "Atypical antipsychotics such as aripiprazole are the DOC in acute mania because their action is fastest.")
q(133, "The drug of choice among the anticonvulsants for rapid cyclers is:",
  ["Valproate", "Carbamazepine", "Lamotrigine", "Gabapentin"],
  "Valproate is labelled the DOC in rapid cyclers.")
q(133, "Which of the following is listed for the treatment of acute mania?",
  ["Oxcarbazepine or carbamazepine", "Gabapentin only", "Levetiracetam", "Phenobarbitone"],
  "The list for acute mania includes valproate, oxcarbazepine or carbamazepine, lamotrigine, topiramate, gabapentin and atypical antipsychotics.")
q(133, "Also listed among the drugs used in acute mania are:",
  ["Lamotrigine and topiramate", "Haloperidol and chlorpromazine",
   "Phenytoin and fosphenytoin", "Levetiracetam and brivaracetam"],
  "Lamotrigine, topiramate and gabapentin appear in the acute mania list.")
q(133, "Lithium in the management of mania is:",
  ["Started prophylactically rather than for the acute attack",
   "The fastest acting drug", "Used only in rapid cyclers", "Given only with benzodiazepines"],
  "Lithium is noted as being started prophylactically.")
q(133, "Benzodiazepines are used in mania as:",
  ["Add-on drugs", "The drug of choice", "Prophylaxis", "The only treatment"],
  "Benzodiazepines are listed as add-on drugs.")
q(133, "A patient with bipolar disorder who is a rapid cycler and needs prophylaxis should receive:",
  ["Valproate", "Lithium", "Gabapentin", "Topiramate"],
  "Valproate is the DOC in rapid cyclers, while lithium is used for prophylaxis of mania generally.")

# ---------------------------------------------------------------------------
# Chapter 34: Affect Disorders: Part 2 (p134-140)
# ---------------------------------------------------------------------------
start(34)
unit("Management of Depression and the Monoamine Hypothesis",
     "Part 2 opens with the management of depression and the monoamine hypothesis. In the brain synapse the key amines are 5HT or serotonin - described as the most important neurotransmitter - and norepinephrine, both removed by reuptake and both metabolised by monoamine oxidase (MAO), with BDNF also shown. Antidepressants need two to three weeks to work. Drugs are divided into the typical antidepressants, which raise amines by blocking reuptake or MAO, and the atypical antidepressants, which block 5HT2 receptors or act on dopamine, so that the 5HT2-mediated erectile dysfunction of the typical drugs is absent.")
q(134, "The management section that opens 'Affect Disorders: Part 2' deals with:",
  ["Management of depression", "Management of mania", "Management of schizophrenia", "Management of anxiety only"],
  "The heading on the page is management of depression.")
q(134, "The hypothesis used to explain drug action in depression on this page is the:",
  ["Monoamine hypothesis", "BDNF hypothesis", "GABA hypothesis", "Cholinergic hypothesis"],
  "The page is headed monoamine hypothesis.")
q(134, "The neurotransmitter described as the most important in this synapse is:",
  ["5HT (serotonin)", "Dopamine", "GABA", "Acetylcholine"],
  "5HT or serotonin is labelled the most important neurotransmitter.")
q(134, "NE in the synapse diagram stands for:",
  ["Norepinephrine", "Norethindrone", "Neurotensin", "Neuropeptide Y"],
  "NE is expanded as norepinephrine.")
q(134, "MAO in the synapse stands for:",
  ["Monoamine oxidase", "Monoamine oxygenase", "Monoacetyl oxidase", "Microsomal amine oxidase"],
  "MAO is expanded as monoamine oxidase.")
q(134, "The two ways the synapse disposes of the amines are reuptake and:",
  ["Metabolism by MAO", "Excretion unchanged", "Binding to BDNF", "Diffusion into fat"],
  "The diagram shows reuptake and MAO-mediated metabolism as the two disposal routes.")
q(134, "The growth factor also shown in the depression synapse is:",
  ["BDNF", "NGF", "VEGF", "EPO"],
  "BDNF appears in the synapse diagram alongside the amines.")
q(134, "Antidepressants are said to need how long before their effect appears?",
  ["Two to three weeks", "Two to three days", "Two to three months", "A single dose"],
  "The page notes that two to three weeks are needed to treat depression.")
q(134, "The typical antidepressants listed are TCA, SNRI, SSRI and:",
  ["MAO inhibitors", "Atypical antipsychotics", "Benzodiazepines", "Lithium"],
  "The typical group lists TCA, SNRI, SSRI and MAO-I.")
q(134, "Tricyclic antidepressants are described as:",
  ["Non-selective, inhibiting reuptake of both 5HT and NE",
   "Selective for 5HT reuptake", "Selective for NE reuptake", "MAO-A selective"],
  "TCA are labelled non-selective because they inhibit reuptake of both 5HT and NE.")
q(134, "The receptor non-specificity of TCA includes blockade of H1, muscarinic, 5HT receptors and:",
  ["Na+ channels", "Calcium channels", "Potassium channels", "Chloride channels"],
  "The list of blocked targets includes H1, muscarinic, 5HT receptors and Na+ channels.")
q(134, "The cardiac toxicity quoted for TCA is:",
  ["Cardiac arrhythmias", "Cardiomyopathy", "Pericarditis", "Aortic dissection"],
  "Toxicity of TCA is given as cardiac arrhythmias.")
q(134, "MAO inhibitors are said to be limited by:",
  ["High drug interaction and fatal side effects", "Very low efficacy",
   "Need for intravenous use", "Severe nephrotoxicity"],
  "The page lists high drug interaction and fatal side effects against MAO inhibitors.")
q(134, "SNRI are described as retaining the effect of TCA but:",
  ["Without the side effects seen with TCA", "With more antimuscarinic effect",
   "With more sedation", "With more arrhythmia"],
  "SNRI are said to retain the effect without the side effects of TCA.")
q(134, "SSRI are described as:",
  ["The drug of choice and first line treatment for depression",
   "Second line only", "Used only in mania", "Used only in OCD"],
  "SSRI are labelled the DOC for depression and first line treatment.")
q(134, "Erectile dysfunction with typical antidepressants is attributed to stimulation of which receptor in the spinal cord?",
  ["5HT2", "5HT3", "Alpha-1", "Muscarinic M3"],
  "The comparison table attributes erectile dysfunction to stimulation of 5HT2 receptors in the spinal cord.")
q(134, "The atypical antidepressants listed at the top of the page act by blocking 5HT2 receptors and by acting on:",
  ["Dopamine", "GABA", "Histamine", "Acetylcholine"],
  "The atypical branch shows 5HT2 blockers such as mirtazapine and dopamine acting drugs such as bupropion.")
q(134, "Compared with typical antidepressants, atypical agents cause erectile dysfunction:",
  ["Rarely or not at all", "More often", "Just as often", "Only in the elderly"],
  "The table marks erectile dysfunction as present with typical and absent with atypical antidepressants.")
q(134, "The selective norepinephrine reuptake inhibitors noted at the foot of the page are used to treat:",
  ["ADHD", "Parkinson's disease", "Schizophrenia", "Insomnia"],
  "The note says selective norepinephrine reuptake inhibitors are used to treat ADHD.")
q(134, "The two selective norepinephrine reuptake inhibitors named are:",
  ["Atomoxetine and viloxazine", "Methylphenidate and dexmethylphenidate",
   "Modafinil and armodafinil", "Clonidine and guanfacine"],
  "The drugs named are atomoxetine and viloxazine.")

unit("Classification of Antidepressants",
     "Antidepressants are classified into typical and atypical. The typical group contains the non-selective tricyclics (clomipramine, imipramine, desipramine, amitriptyline, nortriptyline, doxepin, amoxapine and loxapine), the selective serotonin-norepinephrine reuptake inhibitors (duloxetine, desvenlafaxine, venlafaxine, milnacipran and levomilnacipran), the selective serotonin reuptake inhibitors (sertraline, paroxetine, escitalopram, citalopram, fluvoxamine and fluoxetine) and the MAO inhibitors (non-selective tranylcypromine, isocarboxazide and phenelzine; selective moclobemide and eprobemide). The atypical group contains the 5HT2 blockers, bupropion and the miscellaneous newer agents.")
q(135, "Antidepressants are first divided into:",
  ["Typical and atypical", "Selective and non-selective", "Short and long acting", "Oral and parenteral"],
  "The classification splits antidepressants into typical and atypical.")
q(135, "The typical antidepressant groups listed are TCA, SNRI, SSRI and:",
  ["MAO inhibitors", "5HT2 blockers", "GABA modulators", "Bupropion"],
  "MAO inhibitors complete the typical group.")
q(135, "Which of the following is a tricyclic antidepressant listed on the page?",
  ["Clomipramine", "Duloxetine", "Sertraline", "Moclobemide"],
  "Clomipramine heads the TCA column.")
q(135, "Tricyclic antidepressants listed include all of the following EXCEPT:",
  ["Venlafaxine", "Amitriptyline", "Nortriptyline", "Doxepin"],
  "Venlafaxine is an SNRI; amitriptyline, nortriptyline and doxepin are tricyclics.")
q(135, "Which of the following is an SNRI named on the page?",
  ["Duloxetine", "Imipramine", "Fluoxetine", "Phenelzine"],
  "Duloxetine heads the SNRI column.")
q(135, "Levomilnacipran belongs to which group?",
  ["SNRI", "SSRI", "TCA", "MAO inhibitor"],
  "Levomilnacipran is listed in the SNRI column.")
q(135, "Which of the following is an SSRI named on the page?",
  ["Escitalopram", "Desipramine", "Milnacipran", "Tranylcypromine"],
  "Escitalopram is listed in the SSRI column.")
q(135, "Fluvoxamine belongs to which group?",
  ["SSRI", "SNRI", "TCA", "MAO inhibitor"],
  "Fluvoxamine is listed among the SSRI.")
q(135, "The tricyclic listed alongside amoxapine at the foot of the TCA column is:",
  ["Loxapine", "Maprotiline", "Protriptyline", "Trimipramine"],
  "Amoxapine and loxapine are the last two drugs in the TCA column.")
q(135, "The atypical antidepressant groups listed are 5HT2 blockers, bupropion and:",
  ["Miscellaneous newer drugs", "Benzodiazepines", "Lithium", "Antipsychotics"],
  "The atypical branch lists 5HT2 blockers, bupropion and a miscellaneous group.")
q(135, "Older 5HT2 blockers named on the page include:",
  ["Trazodone and nefazodone", "Mirtazapine and mianserin", "Vilazodone and vortioxetine", "Bupropion and gepirone"],
  "Trazodone and nefazodone are listed as the older 5HT2 blockers.")
q(135, "Newer 5HT2 blockers named on the page include:",
  ["Mirtazapine and mianserin", "Trazodone and nefazodone", "Brexanolone and zuranolone", "Esketamine and gepirone"],
  "Mirtazapine and mianserin are listed as the newer 5HT2 blockers.")
q(135, "The miscellaneous atypical group contains GABA modulators and:",
  ["Novel antidepressants", "Tricyclics", "MAO inhibitors", "Benzodiazepines"],
  "The miscellaneous branch contains GABA modulators and novel antidepressants.")
q(135, "The GABA modulators named are:",
  ["Brexanolone and zuranolone", "Esketamine and gepirone", "Vilazodone and vortioxetine", "Trazodone and nefazodone"],
  "Brexanolone and zuranolone are the GABA modulators.")
q(135, "The novel antidepressants named are:",
  ["Vilazodone, vortioxetine, esketamine and gepirone",
   "Brexanolone and zuranolone", "Mirtazapine and mianserin", "Bupropion and atomoxetine"],
  "The novel group lists vilazodone, vortioxetine, esketamine and gepirone.")
q(135, "Bupropion is classified as:",
  ["An atypical antidepressant", "A typical antidepressant", "An antipsychotic", "A mood stabiliser"],
  "Bupropion appears in the atypical antidepressant branch.")
q(135, "Which of the following pairs is correctly matched?",
  ["Sertraline - SSRI", "Duloxetine - TCA", "Amitriptyline - SNRI", "Tranylcypromine - SSRI"],
  "Sertraline is an SSRI; duloxetine is an SNRI, amitriptyline a TCA and tranylcypromine an MAO inhibitor.")
q(135, "Which of the following is NOT a typical antidepressant?",
  ["Mirtazapine", "Fluoxetine", "Venlafaxine", "Imipramine"],
  "Mirtazapine is an atypical antidepressant (a 5HT2 blocker).")

unit("MAO Inhibitors: Types, Reversibility and Uses",
     "MAO inhibitors are divided by selectivity into selective drugs that block MAO-A and non-selective drugs that block both MAO-A and MAO-B, and by reversibility into reversible and irreversible agents. The irreversible drugs are hit-and-run drugs: their action outlasts their presence in plasma because the binding is permanent, as with proton pump inhibitors and clopidogrel. Their main use listed is as first line treatment of atypical depression, in which mood is elevated on selective occasions.")
q(135, "MAO inhibitors are classified by:",
  ["Selectivity and reversibility", "Route and cost", "Half-life only", "Potency only"],
  "The two headings are types (selectivity) and reversibility.")
q(135, "Selective MAO inhibitors block:",
  ["MAO-A", "MAO-B only", "Both MAO-A and MAO-B", "Monoamine transporter"],
  "Selective agents block MAO-A.")
q(135, "Non-selective MAO inhibitors block:",
  ["Both MAO-A and MAO-B", "MAO-A only", "MAO-B only", "Catechol-O-methyltransferase"],
  "Non-selective agents block MAO-A and MAO-B.")
q(135, "The selective, reversible MAO-A inhibitors named are:",
  ["Moclobemide and eprobemide", "Tranylcypromine and phenelzine",
   "Isocarboxazide and selegiline", "Rasagiline and safinamide"],
  "Moclobemide and eprobemide are the selective reversible MAO-A inhibitors listed.")
q(135, "The non-selective irreversible MAO inhibitors named are:",
  ["Tranylcypromine, isocarboxazide and phenelzine",
   "Moclobemide and eprobemide", "Selegiline and rasagiline", "Safinamide and linezolid"],
  "Tranylcypromine, isocarboxazide and phenelzine are the non-selective irreversible agents.")
q(135, "Irreversible MAO inhibitors are also called:",
  ["Hit and run drugs", "Prodrugs", "Designer drugs", "Orphan drugs"],
  "The irreversible group is labelled hit and run drugs.")
q(135, "A hit and run drug is one where the duration of action persists because:",
  ["The drug is permanently bound although it is absent from plasma",
   "The drug is stored in fat",
   "The drug has an active metabolite",
   "The drug is given as a depot injection"],
  "The note explains that despite the drug being absent from plasma, its action lasts because binding is permanent.")
q(135, "The examples given of hit and run drugs from other classes are:",
  ["Proton pump inhibitors and clopidogrel", "Beta blockers and ACE inhibitors",
   "Statins and fibrates", "Penicillins and cephalosporins"],
  "Proton pump inhibitors and clopidogrel are quoted as examples.")
q(136, "The use listed for MAO inhibitors is first line treatment of:",
  ["Atypical depression", "Typical depression", "Bipolar depression", "Psychotic depression"],
  "MAO inhibitors are listed as first line for atypical depression.")
q(136, "Atypical depression is characterised on the page by:",
  ["Elevated mood on selective occasions", "Loss of mood reactivity",
   "Melancholic features", "Catatonia"],
  "Atypical depression is described as elevated mood in selective occasions.")
q(136, "Which MAO inhibitor would be chosen when reversibility is desirable?",
  ["Moclobemide", "Phenelzine", "Tranylcypromine", "Isocarboxazide"],
  "Moclobemide is a reversible selective MAO-A inhibitor, so its effect can be reversed.")

unit("MAO Inhibitor Adverse Effects: Cheese Reaction and Serotonin Syndrome",
     "The two important adverse effects of MAO inhibitors are the cheese reaction and serotonin syndrome. The cheese reaction, from tyramine in tyramine-rich food, is treated with intravenous phentolamine. Serotonin syndrome follows an excess of 5HT and presents with sympathetic activation with raised blood pressure and heart rate, sweating, mydriasis, rigid muscles, ocular clonus and raised temperature. It is diagnosed by Hunter's criteria and treated with sympatholytic treatment plus a benzodiazepine; if there is no response, the drug of choice is cyproheptadine, which blocks 5HT2 receptors.")
q(136, "The first adverse effect listed for MAO inhibitors is:",
  ["Cheese reaction", "Serotonin syndrome", "Hepatotoxicity", "Agranulocytosis"],
  "The side effect list begins with the cheese reaction.")
q(136, "The drug of choice for the cheese reaction is:",
  ["Intravenous phentolamine", "Oral nifedipine", "Intravenous nitroprusside", "Oral prazosin"],
  "IV phentolamine is given as the DOC for the cheese reaction.")
q(136, "Phentolamine is used in the cheese reaction because it blocks:",
  ["Alpha receptors", "Beta receptors", "Muscarinic receptors", "Dopamine receptors"],
  "Phentolamine is an alpha blocker, appropriate for the pressor effect of tyramine.")
q(136, "Serotonin syndrome with MAO inhibitors is due to:",
  ["Excess 5HT", "Excess dopamine", "Excess GABA", "Excess norepinephrine only"],
  "The page attributes serotonin syndrome to increased 5HT.")
q(136, "The ocular signs listed in serotonin syndrome are:",
  ["Mydriasis and ocular clonus", "Miosis and ptosis", "Nystagmus and diplopia", "Cataract and glaucoma"],
  "Mydriasis and ocular clonus are both listed.")
q(136, "The neuromuscular feature listed in serotonin syndrome is:",
  ["Rigid muscles", "Flaccid paralysis", "Fasciculations only", "Myasthenic weakness"],
  "Rigid muscles are listed among the clinical features.")
q(136, "Autonomic features listed in serotonin syndrome include sympathetic activation with raised blood pressure, raised heart rate and:",
  ["Sweating", "Dry skin", "Bradycardia", "Hypothermia"],
  "Sympathetic activation with sweating is listed.")
q(136, "The temperature change in serotonin syndrome is:",
  ["Raised temperature", "Lowered temperature", "No change", "Alternating fever"],
  "Raised temperature is listed as a feature.")
q(136, "The diagnostic criteria used for serotonin syndrome are:",
  ["Hunter's criteria", "Jones criteria", "Duke criteria", "Revised Jones criteria"],
  "Diagnosis is by Hunter's criteria.")
q(136, "The first line treatment of serotonin syndrome is:",
  ["Sympatholytic treatment plus a benzodiazepine", "Cyproheptadine alone",
   "Dantrolene", "Bromocriptine"],
  "Treatment is sympatholytic treatment plus a benzodiazepine.")
q(136, "If there is no response to first line treatment of serotonin syndrome, the drug of choice is:",
  ["Cyproheptadine", "Dantrolene", "Bromocriptine", "Propranolol"],
  "Cyproheptadine is the DOC when there is no response.")
q(136, "Cyproheptadine works in serotonin syndrome by blocking:",
  ["5HT2 receptors", "Dopamine D2 receptors", "Muscarinic receptors", "NMDA receptors"],
  "Cyproheptadine is described as a 5HT2 blocker.")
q(136, "A patient on an MAO inhibitor eats a tyramine rich meal and develops severe hypertension. The drug of choice is:",
  ["Intravenous phentolamine", "Oral captopril", "Intravenous labetalol", "Sublingual nifedipine"],
  "The cheese reaction of MAO inhibitors is treated with IV phentolamine.")

unit("Tricyclic Antidepressants: Uses",
     "Tricyclics are used in typical depression and, individually, for a range of other indications: clomipramine, which inhibits 5HT reuptake most, is the tricyclic of choice in obsessive-compulsive disorder (though the drug of choice overall is an SSRI); imipramine is used in nocturnal enuresis (where the drug of choice is desmopressin) and in cocaine dependence; desipramine inhibits dopamine and norepinephrine reuptake most; amitriptyline is the most commonly used tricyclic, the most common cause of death by suicide among them, the tricyclic of choice for neuropathy and has the greatest antimuscarinic effect; nortriptyline is a second line drug for smoking dependence; doxepin, an H1 blocker, is used for insomnia and anxiety; and amoxapine, which blocks D2 receptors, is used in psychotic depression.")
q(136, "The main indication for tricyclic antidepressants is:",
  ["Typical depression", "Atypical depression", "Bipolar depression", "Mania"],
  "Tricyclics are listed for typical depression.")
q(136, "The tricyclic with maximum inhibition of 5HT reuptake is:",
  ["Clomipramine", "Desipramine", "Amitriptyline", "Nortriptyline"],
  "Clomipramine is credited with maximum inhibition of 5HT reuptake.")
q(136, "The tricyclic of choice in obsessive-compulsive disorder is:",
  ["Clomipramine", "Imipramine", "Amitriptyline", "Doxepin"],
  "Clomipramine is the TCA of choice in OCD, although the DOC overall is an SSRI.")
q(136, "Overall, the drug of choice for obsessive-compulsive disorder is:",
  ["An SSRI", "Clomipramine", "A tricyclic", "A benzodiazepine"],
  "The page notes that the DOC in OCD is an SSRI.")
q(136, "Imipramine is used in nocturnal enuresis, where the drug of choice is actually:",
  ["Desmopressin", "Imipramine", "Oxybutynin", "Furosemide"],
  "The note states that the DOC for nocturnal enuresis is desmopressin.")
q(136, "The other use listed for imipramine is:",
  ["Cocaine dependence", "Heroin dependence", "Alcohol dependence", "Nicotine dependence"],
  "Cocaine dependence is listed as the other use of imipramine.")
q(136, "The tricyclic with maximum inhibition of dopamine and norepinephrine reuptake is:",
  ["Desipramine", "Clomipramine", "Doxepin", "Amoxapine"],
  "Desipramine is credited with maximum inhibition of dopamine and norepinephrine reuptake.")
q(136, "The most commonly used tricyclic, and the most common cause of death by suicide among them, is:",
  ["Amitriptyline", "Nortriptyline", "Imipramine", "Clomipramine"],
  "Amitriptyline is labelled the most commonly used TCA and the most common cause of death by suicide.")
q(136, "The tricyclic of choice for neuropathy is:",
  ["Amitriptyline", "Nortriptyline", "Desipramine", "Clomipramine"],
  "Amitriptyline is the TCA of choice for neuropathy.")
q(136, "The tricyclic with the maximum antimuscarinic effect is:",
  ["Amitriptyline", "Desipramine", "Nortriptyline", "Amoxapine"],
  "Amitriptyline has the maximum antimuscarinic effect.")
q(136, "Nortriptyline is used as a second line drug for:",
  ["Smoking dependence", "Alcohol dependence", "Opioid dependence", "Cocaine dependence"],
  "Smoking dependence is listed as a second line indication for nortriptyline.")
q(136, "Doxepin is described as an H1 blocker used as a tricyclic for insomnia and:",
  ["Anxiety", "Psychosis", "Mania", "Enuresis"],
  "Doxepin is used for insomnia and anxiety.")
q(136, "The tricyclic that blocks D2 receptors and has antipsychotic effect is:",
  ["Amoxapine", "Amitriptyline", "Doxepin", "Clomipramine"],
  "Amoxapine blocks D2 receptors and has antipsychotic effect.")
q(136, "The tricyclic used in psychotic depression is:",
  ["Amoxapine", "Doxepin", "Imipramine", "Nortriptyline"],
  "Psychotic depression is the indication listed for amoxapine.")
q(136, "Loxapine is noted as:",
  ["An antipsychotic derivative of the tricyclic amoxapine", "A mood stabiliser",
   "A selective serotonin reuptake inhibitor", "A benzodiazepine"],
  "The note states loxapine is an antipsychotic derivative of the TCA amoxapine.")

unit("Tricyclic Antidepressants: Side Effects, Contraindications and Toxicity",
     "The receptor blockade profile of tricyclics explains their adverse effects: muscarinic block gives mydriasis, urinary retention and dry mouth; H1 block gives sedation, for which night-time dosing is used, and obesity through increased appetite; alpha-1 block gives postural hypotension. These effects are shared with typical and atypical antipsychotics, and they make tricyclics contraindicated in glaucoma and benign prostatic hyperplasia. Overdose is lethal even with five to ten tablets, producing metabolic acidosis and arrhythmia; the ionised form of the tricyclic blocks sodium channels and causes death, and the drug of choice is sodium bicarbonate, while the unionised form does not block sodium channels.")
q(137, "Dry mouth, urinary retention and mydriasis with tricyclics result from blockade of:",
  ["Muscarinic receptors", "H1 receptors", "Alpha-1 receptors", "Dopamine D2 receptors"],
  "Muscarinic blockade produces mydriasis, urinary retention and dry mouth.")
q(137, "Sedation with tricyclics is due to blockade of:",
  ["H1 receptors", "Muscarinic receptors", "Alpha-1 receptors", "5HT2 receptors"],
  "H1 blockade causes sedation, which is why night-time dosing is advised.")
q(137, "Obesity with tricyclics is attributed to increased appetite from blockade of:",
  ["H1 receptors", "Muscarinic receptors", "Alpha-1 receptors", "Dopamine receptors"],
  "The page links obesity to increased appetite from H1 blockade.")
q(137, "Postural hypotension with tricyclics is due to blockade of:",
  ["Alpha-1 receptors", "Beta-1 receptors", "Muscarinic receptors", "H1 receptors"],
  "Alpha-1 blockade is listed as the cause of postural hypotension.")
q(137, "Because of their antimuscarinic action, tricyclics are contraindicated in:",
  ["Glaucoma and benign prostatic hyperplasia", "Peptic ulcer and gastritis",
   "Asthma and COPD", "Epilepsy and migraine"],
  "The contraindications listed are glaucoma and BPH.")
q(137, "The receptor-blockade adverse effects of tricyclics are noted to be shared with:",
  ["Both typical and atypical antipsychotics", "Selective serotonin reuptake inhibitors",
   "Monoamine oxidase inhibitors", "Benzodiazepines"],
  "The page notes these effects are also seen with both typical and atypical antipsychotics.")
q(137, "Tricyclic overdose is described as lethal even with:",
  ["Five to ten tablets", "Fifty tablets", "A hundred tablets", "A full bottle"],
  "The page warns of a lethal effect even with five to ten tablets.")
q(137, "The metabolic derangement listed in tricyclic toxicity is:",
  ["Metabolic acidosis", "Metabolic alkalosis", "Respiratory acidosis", "Hyperchloraemic alkalosis"],
  "Metabolic acidosis is listed in the clinical presentation of toxicity.")
q(137, "The cardiac manifestation listed in tricyclic toxicity is:",
  ["Arrhythmia", "Pericardial effusion", "Myocarditis", "Aortic dissection"],
  "Arrhythmia is the cardiac feature of tricyclic toxicity.")
q(137, "Death in tricyclic toxicity is attributed to the ionised form of the drug blocking:",
  ["Na+ channels", "Calcium channels", "Potassium channels", "Chloride channels"],
  "The ionised form of TCA blocks Na+ channels, which causes death.")
q(137, "The drug of choice in tricyclic toxicity is:",
  ["Sodium bicarbonate", "Sodium chloride", "Calcium gluconate", "Magnesium sulfate"],
  "Sodium bicarbonate is the DOC in tricyclic poisoning.")
q(137, "The unionised form of a tricyclic is noted to:",
  ["Not block Na+ channels", "Block Na+ channels more strongly",
   "Block calcium channels", "Cause metabolic acidosis"],
  "The page contrasts the ionised form, which blocks Na+ channels, with the unionised form, which does not.")
q(137, "A patient who has taken an overdose of amitriptyline develops a wide-complex arrhythmia. The specific antidotal treatment is:",
  ["Sodium bicarbonate", "Intravenous calcium", "Intravenous lidocaine", "Activated charcoal only"],
  "Sodium bicarbonate is the DOC for the Na+ channel blocking arrhythmia of tricyclic overdose.")

unit("Serotonin Norepinephrine Reuptake Inhibitors",
     "SNRI action is dose dependent: at low dose they predominantly inhibit 5HT reuptake and at high dose they predominantly inhibit norepinephrine reuptake. They are used in typical depression and in depression with postural hypotension or postural tachycardia syndrome, and have miscellaneous uses including stress urinary incontinence, the neuroses (PTSD, OCD, anorexia nervosa, phobia and bulimia), recurrent pain syndromes such as fibromyalgia, premenstrual syndrome with irritability and hot flashes after the menopause. Their side effect is hypertension; venlafaxine, being short acting, carries the greatest risk of withdrawal symptoms while milnacipran carries the least or none.")
q(137, "The action of SNRI is described as depending on:",
  ["Dose", "Age", "Route", "Renal function only"],
  "The mechanism is headed 'based on dose'.")
q(137, "At low dose, SNRI predominantly inhibit reuptake of:",
  ["5HT", "Norepinephrine", "Dopamine", "GABA"],
  "Low dose gives predominant inhibition of 5HT reuptake.")
q(137, "At high dose, SNRI predominantly inhibit reuptake of:",
  ["Norepinephrine", "5HT", "Dopamine", "Histamine"],
  "High dose gives predominant inhibition of norepinephrine reuptake.")
q(137, "SNRI are used in typical depression and in depression with:",
  ["Postural hypotension or postural tachycardia syndrome", "Glaucoma", "BPH", "Epilepsy"],
  "Depression with postural hypotension or POTS is a listed indication.")
q(137, "The genitourinary use listed for SNRI is:",
  ["Stress urinary incontinence", "Urge incontinence", "Nocturnal enuresis", "Overactive bladder from BPH"],
  "Stress urine incontinence is listed among the miscellaneous uses.")
q(137, "The neuroses listed as SNRI indications include all of the following EXCEPT:",
  ["Schizophrenia", "PTSD", "OCD", "Bulimia"],
  "The neurosis list is PTSD, OCD, anorexia nervosa, phobia and bulimia; schizophrenia is not included.")
q(137, "The recurrent pain syndrome named as an SNRI indication is:",
  ["Fibromyalgia", "Trigeminal neuralgia", "Cluster headache", "Complex regional pain syndrome"],
  "Fibromyalgia is the recurrent pain syndrome listed.")
q(137, "Premenstrual syndrome is listed with the specific symptom of:",
  ["Irritability", "Headache", "Breast tenderness", "Fluid retention"],
  "Irritability in PMS is the indication listed.")
q(137, "Hot flashes after the menopause are treated with SNRI, but the drug of choice is:",
  ["Hormone replacement therapy", "Clonidine", "Gabapentin", "Black cohosh"],
  "The note says HRT is the DOC for hot flashes, with SSRI or SNRI preferred if HRT is contraindicated.")
q(137, "SSRI or SNRI are preferred over hormone replacement therapy for hot flashes when there is a risk of:",
  ["Thrombosis, breast cancer or uterine cancer", "Osteoporosis", "Diabetes", "Cataract"],
  "The note lists thrombosis, breast cancer and uterine cancer as reasons to prefer SSRI or SNRI.")
q(137, "The side effect listed for SNRI is:",
  ["Hypertension", "Hypotension", "Bradycardia", "Hypoglycaemia"],
  "Hypertension is the side effect listed for SNRI.")
q(137, "Among SNRI, the drug with the maximum risk of withdrawal symptoms is:",
  ["Venlafaxine", "Milnacipran", "Duloxetine", "Levomilnacipran"],
  "Venlafaxine, being short acting, carries the maximum risk of withdrawal symptoms.")
q(137, "The SNRI with minimum or no withdrawal symptoms is:",
  ["Milnacipran", "Venlafaxine", "Duloxetine", "Desvenlafaxine"],
  "Milnacipran is noted to have minimum or no withdrawal symptoms.")
q(137, "The short acting nature of venlafaxine explains its:",
  ["High risk of withdrawal symptoms", "Lack of efficacy", "Hepatotoxicity", "Antimuscarinic effects"],
  "The page links short action with the maximum risk of withdrawal symptoms.")

unit("Selective Serotonin Reuptake Inhibitors: Uses and Individual Drugs",
     "SSRI are the drug of choice for typical and atypical depression and are also used in neurosis and for irritability in PMS, with other uses in fibromyalgia and hot flashes. Fluoxetine is the longest acting, with a half-life of about 50 hours and an active metabolite norfluoxetine whose half-life is about 200 hours, so it causes no withdrawal symptoms. Paroxetine has no active metabolite, is short acting and carries the maximum withdrawal symptoms, the maximum erectile dysfunction, the most teratogenic risk and the maximum enzyme inhibition, blocking CYP2D6 and preventing activation of tamoxifen to endoxifen; it also blocks H1, so it sedates and is given at night. Dapoxetine is used for premature ejaculation, often fixed-dose combined with sildenafil. Escitalopram is the most specific SSRI, and all SSRI are teratogenic.")
q(138, "SSRI are the drug of choice for:",
  ["Typical and atypical depression", "Mania", "Psychotic depression", "Bipolar depression"],
  "The DOC list for SSRI names typical and atypical depression.")
q(138, "Among the other uses of SSRI, the pain condition listed is:",
  ["Fibromyalgia", "Trigeminal neuralgia", "Post-herpetic neuralgia", "Migraine"],
  "Fibromyalgia appears among the other uses of SSRI.")
q(138, "The other uses of SSRI also include:",
  ["Hot flashes", "Hypertension", "Heart failure", "Epilepsy"],
  "Hot flashes are listed among the other uses.")
q(138, "Neurosis and irritability in PMS are listed under:",
  ["The drug of choice uses of SSRI", "The other uses of SSRI",
   "The contraindications to SSRI", "The side effects of SSRI"],
  "Neurosis and irritability in PMS are listed as DOC indications for SSRI.")
q(138, "The longest acting SSRI is:",
  ["Fluoxetine", "Paroxetine", "Escitalopram", "Sertraline"],
  "Fluoxetine is described as the longest acting SSRI.")
q(138, "The half-life quoted for fluoxetine is about:",
  ["50 hours", "5 hours", "500 hours", "15 hours"],
  "Fluoxetine's half-life is given as about 50 hours.")
q(138, "The active metabolite of fluoxetine is:",
  ["Norfluoxetine", "Desmethylfluoxetine", "Paroxetine", "Fluvoxamine"],
  "The active metabolite is norfluoxetine, with a half-life quoted in hundreds of hours.")
q(138, "Because of its long half-life and active metabolite, fluoxetine causes:",
  ["No withdrawal symptoms", "Maximum withdrawal symptoms",
   "Maximum teratogenicity", "Maximum enzyme inhibition"],
  "The long acting fluoxetine is noted to produce no withdrawal symptoms.")
q(138, "The SSRI with no active metabolite and a short action is:",
  ["Paroxetine", "Fluoxetine", "Citalopram", "Sertraline"],
  "Paroxetine is described as having no active metabolite and being short acting.")
q(138, "Paroxetine is noted for the maximum risk of all of the following EXCEPT:",
  ["Weight loss", "Withdrawal symptoms", "Erectile dysfunction", "Teratogenicity"],
  "Paroxetine carries maximum withdrawal symptoms, maximum erectile dysfunction and maximum teratogenicity; weight loss is not attributed to it.")
q(138, "Paroxetine blocks which enzyme, preventing activation of tamoxifen to endoxifen?",
  ["CYP2D6", "CYP3A4", "CYP2C19", "CYP1A2"],
  "Paroxetine is described as blocking CYP2D6, which converts tamoxifen to endoxifen in breast cancer.")
q(138, "The clinical consequence of paroxetine's CYP2D6 inhibition in a patient on tamoxifen is:",
  ["Reduced activation of tamoxifen to endoxifen", "Increased risk of bleeding",
   "Serotonin syndrome", "Excessive sedation"],
  "Blocking CYP2D6 prevents the conversion of tamoxifen to its active form endoxifen.")
q(138, "Paroxetine is given at night time because it blocks:",
  ["H1 receptors", "Muscarinic receptors", "Dopamine receptors", "Alpha-1 receptors"],
  "H1 blockade by paroxetine causes sedation, so it suits depression with insomnia and night dosing.")
q(138, "The SSRI used to treat premature ejaculation is:",
  ["Dapoxetine", "Fluoxetine", "Escitalopram", "Fluvoxamine"],
  "Dapoxetine is listed for premature ejaculation.")
q(138, "Dapoxetine is prescribed as a fixed dose combination with:",
  ["Sildenafil", "Tadalafil", "Apomorphine", "Yohimbine"],
  "Dapoxetine is prescribed as a fixed dose combination with sildenafil, the DOC for erectile dysfunction.")
q(138, "The most specific SSRI is:",
  ["Escitalopram", "Citalopram", "Sertraline", "Paroxetine"],
  "Escitalopram is labelled the most specific SSRI.")
q(138, "The note at the foot of the SSRI page states that:",
  ["All SSRI are teratogenic", "SSRI are safe in pregnancy",
   "Only paroxetine is teratogenic", "SSRI are contraindicated in the elderly"],
  "The note states that all SSRI are teratogenic.")

unit("Selective Serotonin Reuptake Inhibitors: Side Effects",
     "Raised 5HT stimulates receptors to produce the shared SSRI and SNRI effects: transient anxiety, insomnia (so the dose is given in the morning) and vivid dreams, with 5HT2 stimulation in the spinal cord causing erectile dysfunction - the commonest delayed side effect - anorgasmia and delayed ejaculation, and 5HT3 stimulation causing nausea and vomiting, the commonest effect, and loose stools. Other effects are akathisia, bleeding risk and osteoporosis. With continued treatment, prolonged stimulation of 5HT2 receptors leads to their downregulation over a few weeks and anxiolysis; a benzodiazepine is added for a month to cover the initial anxiety.")
q(138, "The side effects described as seen with both SSRI and SNRI follow from:",
  ["Increased 5HT stimulating its receptors", "Blockade of muscarinic receptors",
   "Blockade of histamine receptors", "Blockade of alpha-1 receptors"],
  "The section is headed with the rise in 5HT stimulating receptors.")
q(138, "Transient anxiety, insomnia and vivid dreams with SSRI lead to which practical advice?",
  ["Administer the dose in the morning", "Administer the dose at night",
   "Split the dose three times a day", "Give the drug only on alternate days"],
  "Because of insomnia, the morning dose is advised.")
q(138, "The commonest side effect overall with SSRI is:",
  ["Nausea and vomiting", "Erectile dysfunction", "Anorgasmia", "Akathisia"],
  "Nausea and vomiting are marked as the commonest effect.")
q(138, "Nausea, vomiting and loose stools with SSRI are mediated through:",
  ["5HT3 receptors", "5HT2 receptors", "Muscarinic receptors", "Dopamine receptors"],
  "The 5HT3 receptor is linked to these gastrointestinal effects.")
q(138, "Sexual dysfunction with SSRI - erectile dysfunction, anorgasmia and delayed ejaculation - is mediated through:",
  ["5HT2 receptors in the spinal cord", "5HT3 receptors in the gut",
   "Alpha-1 receptors", "Dopamine receptors"],
  "5HT2 receptors in the spinal cord are shown as the mediators of sexual dysfunction.")
q(138, "Erectile dysfunction with SSRI is described as:",
  ["The commonest delayed side effect", "The commonest immediate side effect",
   "A rare idiosyncratic reaction", "A sign of toxicity"],
  "Erectile dysfunction is labelled the commonest delayed side effect.")
q(139, "Akathisia as an SSRI side effect means:",
  ["Restlessness", "Muscle rigidity", "Tremor", "Dystonia"],
  "Akathisia is glossed as restlessness.")
q(139, "Other side effects listed for SSRI include akathisia, risk of bleeding and:",
  ["Risk of osteoporosis", "Risk of glaucoma", "Risk of hepatitis", "Risk of seizures"],
  "Osteoporosis risk is the third of the other side effects.")
q(139, "With continued SSRI treatment, prolonged stimulation of 5HT2 receptors leads to their:",
  ["Downregulation, producing anxiolysis", "Upregulation, producing anxiety",
   "Desensitisation in the gut only", "Conversion to 5HT3 receptors"],
  "Prolonged stimulation causes downregulation, which produces anxiolysis.")
q(139, "Because SSRI cause anxiety during the first few weeks, the page advises adding:",
  ["A benzodiazepine for one month", "An antipsychotic for a year",
   "A beta blocker indefinitely", "Lithium for six months"],
  "A benzodiazepine is added for one month to cover the initial anxiety.")
q(139, "The anxiolytic effect of SSRI appears only after:",
  ["A few weeks of continued treatment", "The first dose", "Twenty-four hours", "Six months"],
  "Downregulation of 5HT2 receptors, and hence anxiolysis, takes a few weeks.")

unit("Atypical Antidepressants: 5HT2 Blockers",
     "The older 5HT2 blockers are mild inhibitors of 5HT reuptake: trazodone is used for depression with insomnia but causes sedation through H1 block and erectile dysfunction, while nefazodone is obsolete because it is hepatotoxic. The newer drugs are mianserin and mirtazapine; mirtazapine blocks 5HT2 and also 5HT3, giving an antiemetic effect, causes sedation suited to night-time dosing and increases both 5HT and norepinephrine, which is why it is called a noradrenergic and specific serotonergic antidepressant (NaSSA). It does not cause erectile dysfunction and is the drug of choice for depression with insomnia.")
q(139, "The older 5HT2 blockers are described as:",
  ["Mild inhibitors of 5HT reuptake", "Potent inhibitors of 5HT reuptake",
   "MAO inhibitors", "Selective norepinephrine reuptake inhibitors"],
  "The older drugs are described as mild inhibitors of 5HT reuptake.")
q(139, "Trazodone is used for depression associated with:",
  ["Insomnia", "Psychosis", "Parkinsonism", "Enuresis"],
  "Trazodone is listed for depression with insomnia.")
q(139, "Sedation with trazodone is attributed to blockade of:",
  ["H1 receptors", "Muscarinic receptors", "Alpha-1 receptors", "Dopamine receptors"],
  "The sedation of trazodone is attributed to H1 blockade.")
q(139, "The adverse effect that limits the use of trazodone is:",
  ["Erectile dysfunction", "Hepatotoxicity", "Agranulocytosis", "Pulmonary fibrosis"],
  "Erectile dysfunction is listed as a side effect of trazodone.")
q(139, "Nefazodone is described as:",
  ["Obsolete because of hepatotoxicity", "The drug of choice in depression with insomnia",
   "A novel antidepressant", "A GABA modulator"],
  "Nefazodone is labelled obsolete, with hepatotoxicity as its side effect.")
q(139, "The newer 5HT2 blockers named are:",
  ["Mianserin and mirtazapine", "Trazodone and nefazodone",
   "Vilazodone and vortioxetine", "Brexanolone and zuranolone"],
  "Mianserin and mirtazapine are the newer 5HT2 blockers.")
q(139, "Mirtazapine, besides blocking 5HT2, also blocks 5HT3, giving it an:",
  ["Antiemetic effect", "Antipsychotic effect", "Antihypertensive effect", "Analgesic effect"],
  "5HT3 blockade gives mirtazapine an antiemetic action.")
q(139, "Sedation with mirtazapine is handled by:",
  ["Night-time dosing", "Morning dosing", "Split dosing", "Stopping the drug"],
  "Sedation is exploited by giving the drug at night.")
q(139, "Mirtazapine increases the synaptic availability of:",
  ["Both 5HT and norepinephrine", "Dopamine only", "GABA only", "Acetylcholine only"],
  "Mirtazapine increases both 5HT and norepinephrine.")
q(139, "NaSSA, the class name for mirtazapine, expands to:",
  ["Noradrenergic and specific serotonergic antidepressant",
   "Norepinephrine and serotonin selective antagonist",
   "Noradrenergic selective serotonin agonist",
   "Non-selective serotonin and noradrenaline antagonist"],
  "NaSSA stands for noradrenergic and specific serotonergic antidepressant.")
q(139, "The drug of choice for depression with insomnia is:",
  ["Mirtazapine", "Trazodone", "Fluoxetine", "Bupropion"],
  "Mirtazapine is the DOC for depression with insomnia.")
q(139, "Unlike SSRI, mirtazapine is free of which troublesome effect?",
  ["Erectile dysfunction", "Sedation", "Weight gain", "Antiemetic effect"],
  "The page notes the absence of erectile dysfunction with mirtazapine, unlike the typical antidepressants.")

unit("Bupropion",
     "Bupropion is similar to amphetamine and acts on dopamine and norepinephrine. It is used in smoking dependence, ADHD and, combined with naltrexone, in obesity. Its adverse effects are seizures and anxiety - the greatest among the antidepressants - together with weight loss. Its advantage is that it does not cause erectile dysfunction.")
q(140, "Bupropion is described as similar to:",
  ["Amphetamine", "Benzodiazepines", "Lithium", "Ketamine"],
  "The page opens the bupropion section by saying it is similar to amphetamine.")
q(140, "The neurotransmitter principally acted on by bupropion is:",
  ["Dopamine", "Serotonin", "GABA", "Histamine"],
  "Dopamine is the amine named in the mechanism of bupropion.")
q(140, "The amine reuptake inhibited along with dopamine by bupropion is:",
  ["Norepinephrine", "Serotonin", "GABA", "Glycine"],
  "Bupropion inhibits reuptake of dopamine and norepinephrine.")
q(140, "Bupropion is used in:",
  ["Smoking dependence", "Opioid dependence", "Alcohol dependence", "Benzodiazepine dependence"],
  "Smoking dependence is the first use listed.")
q(140, "The second use listed for bupropion is:",
  ["ADHD", "Narcolepsy", "Parkinson's disease", "Migraine"],
  "ADHD is the second use listed.")
q(140, "For obesity, bupropion is combined with:",
  ["Naltrexone", "Orlistat", "Liraglutide", "Phentermine"],
  "Obesity with naltrexone is listed as a use of bupropion.")
q(140, "The adverse effect of bupropion that limits its use is:",
  ["Seizures", "Hepatotoxicity", "Agranulocytosis", "Pulmonary hypertension"],
  "Seizures are listed as an adverse effect of bupropion.")
q(140, "Bupropion causes anxiety to a degree described as:",
  ["Maximum among antidepressants", "Minimum among antidepressants",
   "Equal to that of SSRI", "Absent"],
  "Anxiety with bupropion is described as the maximum among antidepressants.")
q(140, "The weight change expected with bupropion is:",
  ["Weight loss", "Weight gain", "No change", "Initial gain then loss"],
  "Weight loss is listed as an effect of bupropion, and it is used with naltrexone for obesity.")
q(140, "The advantage of bupropion over SSRI is that it does not cause:",
  ["Erectile dysfunction", "Seizures", "Anxiety", "Weight loss"],
  "The advantage quoted is the absence of erectile dysfunction.")

unit("GABA Modulators and Novel Antidepressants",
     "The miscellaneous atypical group contains the GABA modulators brexanolone, given as a continuous intravenous infusion, and zuranolone, given orally once daily, both for severe postpartum depression; mild to moderate postpartum depression is treated with SSRI or SNRI, with mirtazapine if insomnia is present. The novel antidepressants are used for resistant depression: vilazodone combines SSRI action with 5HT1A agonism, vortioxetine is a multimodal serotonin agonist-antagonist, esketamine is a ketamine derivative given as a nasal spray, and gepirone is a 5HT1A agonist approved by the FDA for depression, whereas the older 5HT1A agonists buspirone and ipsapirone are not FDA approved for it.")
q(140, "Brexanolone and zuranolone are classified as:",
  ["GABA modulators", "Novel antidepressants", "5HT2 blockers", "MAO inhibitors"],
  "The two drugs are grouped as GABA modulators.")
q(140, "Brexanolone is given:",
  ["As a continuous intravenous infusion", "Orally once daily", "As a nasal spray", "Intramuscularly"],
  "Brexanolone is given IV as a continuous infusion.")
q(140, "Zuranolone is given:",
  ["Orally once daily", "As a continuous infusion", "As a nasal spray", "By depot injection"],
  "Zuranolone is given by the oral route once daily.")
q(140, "The indication for brexanolone and zuranolone is:",
  ["Severe postpartum depression", "Resistant depression", "Bipolar depression", "Premenstrual syndrome"],
  "Both are used for severe postpartum depression.")
q(140, "Mild to moderate postpartum depression is treated with:",
  ["SSRI or SNRI", "Brexanolone", "Esketamine", "Lithium"],
  "The note says SSRI or SNRI are used for mild to moderate postpartum depression.")
q(140, "If a patient with mild postpartum depression also has insomnia, the drug named is:",
  ["Mirtazapine", "Bupropion", "Vilazodone", "Gepirone"],
  "Mirtazapine is named for postpartum depression with insomnia.")
q(140, "The novel antidepressants are used to treat:",
  ["Resistant depression", "Bipolar depression", "Postpartum depression", "Seasonal affective disorder"],
  "The novel group is introduced as treatment for resistant depression.")
q(140, "Vilazodone combines SSRI action with:",
  ["5HT1A agonism", "5HT2 blockade", "Dopamine reuptake inhibition", "GABA modulation"],
  "Vilazodone is described as an SSRI plus a 5HT1A agonist.")
q(140, "Vortioxetine is described as a:",
  ["Multimodal serotonin agonist antagonist", "Selective serotonin reuptake inhibitor only",
   "Serotonin antagonist only", "GABA modulator"],
  "Vortioxetine is labelled an mSAA drug, a multimodal serotonin agonist antagonist.")
q(140, "Besides SSRI action and 5HT1A/1B agonism, vortioxetine antagonises:",
  ["5HT1D, 5HT3 and 5HT7 receptors", "5HT2 and 5HT4 receptors",
   "Dopamine and histamine receptors", "Muscarinic receptors"],
  "Vortioxetine is described as a 5HT1A and 5HT1B agonist and a 5HT1D, 5HT3 and 5HT7 antagonist.")
q(140, "Esketamine is a derivative of:",
  ["Ketamine", "Amphetamine", "Benzodiazepine", "Lithium"],
  "Esketamine is described as a derivative of ketamine.")
q(140, "Esketamine is given for resistant depression as a:",
  ["Nasal spray", "Continuous infusion", "Weekly injection", "Transdermal patch"],
  "Esketamine is given as a nasal spray.")
q(140, "Gepirone acts as a:",
  ["5HT1A agonist", "5HT2 blocker", "GABA modulator", "Dopamine agonist"],
  "Gepirone is described as a 5HT1A agonist.")
q(140, "Which 5HT1A agonist is FDA approved for depression?",
  ["Gepirone", "Buspirone", "Ipsapirone", "Vilazodone"],
  "Gepirone is FDA approved to treat depression, whereas buspirone and ipsapirone are not.")
q(140, "The older 5HT1A agonists noted as NOT FDA approved for depression are:",
  ["Buspirone and ipsapirone", "Gepirone and vilazodone", "Vortioxetine and esketamine", "Trazodone and nefazodone"],
  "The note lists buspirone and ipsapirone as 5HT1A agonists that are not FDA approved for depression.")

# ---------------------------------------------------------------------------
# Chapter 35: Antipsychotic Drugs (p141-144)
# ---------------------------------------------------------------------------
start(35)
unit("Dopamine Hypothesis of Psychosis",
     "The antipsychotic chapter opens with the dopamine hypothesis of psychosis: dopamine acting in the limbic system on D2 receptors, which are Gi-coupled G protein coupled receptors, produces the disordered thoughts and flattened or inappropriate affect of psychosis. Blocking these receptors is the basis of antipsychotic action.")
q(141, "The hypothesis with which the antipsychotic chapter begins is the:",
  ["Dopamine hypothesis of psychosis", "Serotonin hypothesis of psychosis",
   "GABA hypothesis of psychosis", "Glutamate hypothesis of psychosis"],
  "The first heading is the dopamine hypothesis of psychosis.")
q(141, "The dopamine said to be abnormal in psychosis is that in the:",
  ["Limbic system", "Basal ganglia only", "Cerebellum", "Spinal cord"],
  "The schema specifies dopamine levels in the limbic system.")
q(141, "The dopamine receptor subtype implicated is:",
  ["D2", "D1", "D3 only", "D5"],
  "The schema shows dopamine acting on D2 receptors.")
q(141, "The D2 receptor belongs to which G protein subtype?",
  ["Gi", "Gs", "Gq", "G12/13"],
  "The page notes D2 receptors are of the Gi subtype of GPCR.")
q(141, "The two mental functions said to be affected by the dopamine excess are thoughts and:",
  ["Affect", "Memory", "Orientation", "Sleep"],
  "The schema ends with effects on thoughts and affect.")
q(141, "A drug that relieves hallucinations and disordered thinking by blocking D2 receptors in the limbic system is acting on the:",
  ["Dopamine hypothesis of psychosis", "Monoamine hypothesis of depression",
   "Cholinergic hypothesis of dementia", "GABA hypothesis of anxiety"],
  "Blocking limbic D2 receptors to improve thoughts and affect is the dopamine hypothesis applied to treatment.")

unit("Typical versus Atypical Antipsychotics",
     "Typical antipsychotics block the D2 receptor, produce marked extrapyramidal side effects and act only on positive symptoms; they are second line drugs, preferred for agitation (haloperidol) and carry a risk of QT prolongation (haloperidol, chlorpromazine). Atypical antipsychotics act mainly on central 5HT receptors with minor D2 blockade, produce far fewer extrapyramidal effects, act on both positive and negative symptoms and are first line drugs (apart from clozapine and olanzapine); olanzapine is also used for agitation, quetiapine for insomnia and as an add-on (or even monotherapy) when antidepressants fail, and quetiapine and ziprasidone prolong the QT interval. For sedation in agitation, sublingual dexmedetomidine, an alpha-2 agonist, and lorazepam are noted.")
q(141, "The two types of antipsychotics compared on this page are:",
  ["Typical and atypical", "First and second generation only",
   "Selective and non-selective", "Reversible and irreversible"],
  "Types of antipsychotics are given as typical and atypical.")
q(141, "Typical antipsychotics mainly block the:",
  ["D2 receptor", "Central 5HT receptor", "D4 receptor", "NMDA receptor"],
  "The receptor blocked by typical agents is the D2 receptor.")
q(141, "Atypical antipsychotics act mainly on:",
  ["Central 5HT receptors, with D2 blockade a minor component",
   "D2 receptors only", "Dopamine transporters only", "GABA-A receptors"],
  "The atypical column lists central 5HT blockade as major and D2 blockade as minor.")
q(141, "Extrapyramidal side effects with typical antipsychotics are graded as:",
  ["Marked (+++)", "Minimal (+)", "Absent", "Identical to atypical agents"],
  "Typical agents are graded +++ for extrapyramidal side effects.")
q(141, "The milder extrapyramidal profile of atypical agents is attributed to:",
  ["Less D2 stimulation blockade", "Greater D2 blockade",
   "Antimuscarinic potency", "Faster metabolism"],
  "The page attributes the lower extrapyramidal effect to less D2 blockade.")
q(141, "In psychosis or schizophrenia, the preferred first line drugs are:",
  ["Atypical antipsychotics, apart from clozapine and olanzapine",
   "Typical antipsychotics", "Benzodiazepines", "Lithium"],
  "Atypical agents are first line, but clozapine and olanzapine are excepted from routine first line use.")
q(141, "Typical antipsychotics are described as:",
  ["Second line drugs", "First line drugs", "Drugs of choice in resistant disease", "Not used in psychosis"],
  "Typical agents are labelled second line drugs.")
q(141, "The drugs preferred for agitation are:",
  ["Haloperidol and olanzapine", "Clozapine and quetiapine",
   "Risperidone and aripiprazole", "Chlorpromazine and thioridazine"],
  "Haloperidol and olanzapine are the drugs preferred for agitation.")
q(141, "Typical antipsychotics act on which symptoms?",
  ["Only positive symptoms", "Only negative symptoms",
   "Both positive and negative symptoms", "Only cognitive symptoms"],
  "Typical agents are said to act only on positive symptoms.")
q(141, "Atypical antipsychotics act on:",
  ["Both positive and negative symptoms", "Only positive symptoms",
   "Only negative symptoms", "Neither"],
  "Atypical agents act on positive and negative symptoms.")
q(141, "The drugs described as best for negative symptoms, in order, are:",
  ["Cariprazine, then risperidone", "Risperidone, then cariprazine",
   "Haloperidol, then chlorpromazine", "Quetiapine, then olanzapine"],
  "The note reads cariprazine greater than risperidone for negative symptoms.")
q(141, "The antipsychotic used in insomnia disorder is:",
  ["Quetiapine", "Haloperidol", "Risperidone", "Aripiprazole"],
  "Quetiapine is named as the drug used in insomnia disorder.")
q(141, "When antidepressants are ineffective, the antipsychotic used as an add-on is:",
  ["Quetiapine", "Haloperidol", "Chlorpromazine", "Fluphenazine"],
  "Quetiapine is listed for add-on use when antidepressants are ineffective, and it can even be used as monotherapy.")
q(141, "Typical antipsychotics in that add-on situation are:",
  ["Not used", "The drugs of choice", "Used only with lithium", "Used only in the elderly"],
  "Typical agents are marked as not used for add-on treatment of depression.")
q(141, "The QT prolonging drugs listed are:",
  ["Haloperidol, chlorpromazine, quetiapine and ziprasidone",
   "Haloperidol and clozapine only",
   "Aripiprazole and brexpiprazole only", "Lurasidone and cariprazine only"],
  "Haloperidol, chlorpromazine, quetiapine and ziprasidone are the drugs listed with increased QT prolongation risk.")
q(141, "For sedation in agitation, the note mentions sublingual dexmedetomidine, which is:",
  ["An alpha-2 agonist", "A benzodiazepine", "A dopamine antagonist", "An anticholinergic"],
  "Dexmedetomidine is noted as an alpha-2 agonist given sublingually.")
q(141, "The other drug noted for sedation in agitation is:",
  ["Lorazepam", "Diazepam", "Promethazine", "Zolpidem"],
  "Lorazepam is the second drug noted for sedation in agitation.")

unit("Classification of Antipsychotics",
     "Typical antipsychotics are divided by potency: the low potency phenothiazines chlorpromazine and thioridazine, and the high potency phenothiazines fluphenazine, trifluoperazine and perphenazine together with the butyrophenones haloperidol and droperidol; molindone is listed separately. Colour vision disturbances are a recall point: brown vision with thioridazine, blue vision with sildenafil and yellow vision with digoxin.")
q(142, "Typical antipsychotics are subdivided by:",
  ["Potency", "Route", "Half-life", "Cost"],
  "The typical branch divides into low potency and high potency drugs.")
q(142, "Low potency typical antipsychotics named are:",
  ["Chlorpromazine and thioridazine", "Haloperidol and droperidol",
   "Fluphenazine and perphenazine", "Trifluoperazine and molindone"],
  "Chlorpromazine and thioridazine are the low potency agents.")
q(142, "High potency typical antipsychotics named include:",
  ["Fluphenazine, trifluoperazine and perphenazine",
   "Chlorpromazine and thioridazine", "Clozapine and olanzapine", "Quetiapine and ziprasidone"],
  "Fluphenazine, trifluoperazine and perphenazine are the high potency phenothiazines.")
q(142, "The butyrophenones named are:",
  ["Haloperidol and droperidol", "Chlorpromazine and thioridazine",
   "Risperidone and paliperidone", "Aripiprazole and brexpiprazole"],
  "Haloperidol and droperidol are the butyrophenones.")
q(142, "Chlorpromazine and thioridazine belong to which chemical group?",
  ["Phenothiazines", "Butyrophenones", "Thioxanthenes", "Dibenzodiazepines"],
  "The phenothiazine group is labelled against chlorpromazine and thioridazine.")
q(142, "The drug listed outside the phenothiazine and butyrophenone groups is:",
  ["Molindone", "Haloperidol", "Perphenazine", "Trifluoperazine"],
  "Molindone is listed separately in the typical group.")
q(142, "Brown vision is a characteristic adverse effect of:",
  ["Thioridazine", "Sildenafil", "Digoxin", "Chlorpromazine"],
  "The colour vision note pairs brown vision with thioridazine.")
q(142, "Blue vision is associated with:",
  ["Sildenafil", "Thioridazine", "Digoxin", "Haloperidol"],
  "Blue vision is listed for sildenafil.")
q(142, "Yellow vision is classically associated with:",
  ["Digoxin", "Thioridazine", "Sildenafil", "Clozapine"],
  "Yellow vision is listed for digoxin.")
q(142, "A patient on a low potency phenothiazine complains that everything looks brown. The drug is:",
  ["Thioridazine", "Chlorpromazine", "Haloperidol", "Fluphenazine"],
  "Thioridazine, a low potency phenothiazine, is the drug that causes brown vision.")

unit("Clozapine",
     "Clozapine has the least D2 receptor blockade of the antipsychotics, is the most effective because it blocks D4 receptors and is also the most toxic. Its adverse effects are remembered by the mnemonic SAMOSA: sedation, agranulocytosis (which does not correlate with plasma concentration, so therapeutic drug monitoring is impossible), myocarditis, obesity, sialorrhoea (the wet pillow syndrome) and angle closure glaucoma; it is also used to treat suicidal tendencies. Its indications are resistant schizophrenia, where it is the drug of choice, with lithium and electroconvulsive therapy as other options.")
q(142, "Clozapine is described as having the:",
  ["Minimum D2 receptor blockade", "Maximum D2 receptor blockade",
   "No dopamine blockade at all", "Selective D1 blockade"],
  "Clozapine is credited with the minimum D2 receptor block.")
q(142, "Clozapine is the most effective antipsychotic because it blocks:",
  ["D4 receptors", "D1 receptors", "5HT3 receptors", "NMDA receptors"],
  "Its superior efficacy is attributed to D4 receptor block.")
q(142, "Clozapine is also described as the:",
  ["Most toxic antipsychotic", "Safest antipsychotic", "Least effective antipsychotic", "Cheapest antipsychotic"],
  "The page labels clozapine the most toxic antipsychotic.")
q(142, "The mnemonic given for clozapine's side effects is:",
  ["SAMOSA", "MUSCARINE", "ORCHAD", "HIPS Dance"],
  "The mnemonic is SAMOSA.")
q(142, "In the SAMOSA mnemonic, the first S stands for:",
  ["Sedation", "Sialorrhoea", "Seizures", "Sweating"],
  "The first S is sedation.")
q(142, "The A of SAMOSA stands for:",
  ["Agranulocytosis", "Akathisia", "Anorexia", "Alopecia"],
  "A stands for agranulocytosis.")
q(142, "Why is therapeutic drug monitoring not possible for clozapine's agranulocytosis?",
  ["There is no correlation with plasma concentration",
   "The drug cannot be measured in plasma",
   "The reaction is immediate", "The reaction is dose independent in everyone"],
  "The page states agranulocytosis has no correlation to plasma concentration, so monitoring cannot predict it.")
q(142, "The M of SAMOSA stands for:",
  ["Myocarditis", "Mydriasis", "Miosis", "Metabolic acidosis"],
  "M stands for myocarditis.")
q(142, "The O of SAMOSA stands for:",
  ["Obesity", "Osteoporosis", "Ocular clonus", "Oliguria"],
  "O stands for obesity.")
q(142, "The second S of SAMOSA stands for sialorrhoea, also called:",
  ["Wet pillow syndrome", "Dry mouth syndrome", "Cotton wool syndrome", "Restless leg syndrome"],
  "Sialorrhoea with clozapine is described as the wet pillow syndrome.")
q(142, "The final A of SAMOSA stands for:",
  ["Angle closure glaucoma", "Agranulocytosis", "Akathisia", "Anaemia"],
  "The final A is angle closure glaucoma.")
q(142, "Another use of clozapine noted on the page is treatment of:",
  ["Suicidal tendencies", "Insomnia", "Obsessive-compulsive disorder", "Tourette syndrome"],
  "The note mentions treatment of suicidal tendencies.")
q(142, "Clozapine is the drug of choice in:",
  ["Resistant schizophrenia", "First episode psychosis", "Postpartum psychosis", "Drug induced psychosis"],
  "Clozapine is the DOC in resistant schizophrenia.")
q(142, "Other options noted for resistant schizophrenia besides clozapine are lithium and:",
  ["Electroconvulsive therapy", "Deep brain stimulation", "Psychosurgery", "Vagus nerve stimulation"],
  "Lithium and electroconvulsive therapy are the other options listed, ECT being described as the best method.")
q(142, "A patient on clozapine reports drooling onto the pillow at night. This is:",
  ["Sialorrhoea - the wet pillow syndrome", "Sedation", "Obesity related reflux", "A sign of myocarditis"],
  "Sialorrhoea, the wet pillow syndrome, is one of the SAMOSA effects of clozapine.")

unit("Other Atypical Antipsychotics",
     "Risperidone and paliperidone have the greatest D2 blockade among the atypical agents and quetiapine causes cataract. Pimavanserin is a pure 5HT blocker with no D2 blockade and is the drug of choice for levodopa-induced psychosis. Aripiprazole, brexpiprazole and cariprazine are 5HT blockers that are also partial agonists at D2 receptors; because they do not block muscarinic or histamine receptors they can be used in BPH and glaucoma. Ziprasidone is a 5HT blocker that is weight neutral and lurasidone is a 5HT agonist.")
q(143, "The atypical antipsychotics with maximum D2 blockade are:",
  ["Risperidone and paliperidone", "Clozapine and quetiapine",
   "Aripiprazole and brexpiprazole", "Pimavanserin and lurasidone"],
  "Risperidone and paliperidone are credited with maximum D2 blockade.")
q(143, "The ocular adverse effect specifically attributed to quetiapine is:",
  ["Cataract", "Glaucoma", "Retinal detachment", "Optic neuritis"],
  "Cataract is listed as a side effect of quetiapine.")
q(143, "Pimavanserin is described as:",
  ["A 5HT blocker with no D2 blockade", "A D2 blocker with no 5HT effect",
   "A dopamine partial agonist", "A GABA modulator"],
  "Pimavanserin is a 5HT blocker only, with no D2 blockade.")
q(143, "Pimavanserin is the drug of choice for:",
  ["Levodopa-induced psychosis", "Resistant schizophrenia", "Tourette syndrome", "Delirium tremens"],
  "Pimavanserin is the DOC for levodopa-induced psychosis.")
q(143, "Aripiprazole, brexpiprazole and cariprazine are 5HT blockers that are additionally:",
  ["Partial agonists at D2 receptors", "Full antagonists at D2 receptors",
   "Dopamine reuptake inhibitors", "MAO inhibitors"],
  "These three are described as 5HT blockers plus partial agonists at D2 receptors.")
q(143, "Because aripiprazole, brexpiprazole and cariprazine do not block muscarinic or histamine receptors, they can be used in:",
  ["BPH and glaucoma", "Asthma and COPD", "Peptic ulcer", "Myasthenia gravis"],
  "The note says they can be used in BPH and glaucoma because other receptors are spared.")
q(143, "Ziprasidone is distinguished by being:",
  ["Weight neutral", "The most sedating", "The most antimuscarinic", "The most hepatotoxic"],
  "Ziprasidone is noted as weight neutral.")
q(143, "Lurasidone is described as a:",
  ["5HT agonist", "Selective D2 antagonist", "GABA agonist", "Dopamine agonist"],
  "Lurasidone is described as a 5HT agonist.")
q(143, "Which atypical agent is safest in a patient with glaucoma and prostatic hypertrophy?",
  ["Aripiprazole", "Clozapine", "Olanzapine", "Quetiapine"],
  "Aripiprazole does not block muscarinic or histamine receptors, so it is suitable in BPH and glaucoma.")
q(143, "A patient with Parkinson's disease on levodopa develops visual hallucinations. The drug of choice is:",
  ["Pimavanserin", "Haloperidol", "Risperidone", "Clozapine"],
  "Pimavanserin, a pure 5HT blocker without D2 blockade, is the DOC for levodopa-induced psychosis.")

unit("Adverse Effects According to Receptor Blocked",
     "D2 blockade produces extrapyramidal side effects and hyperprolactinaemia - most severe with risperidone, least severe with clozapine and absent with pimavanserin and the partial agonists. Blockade of other receptors produces obesity, urinary retention, sedation, dyslipidaemia and hyperglycaemia from insulin resistance, in the order clozapine greater than olanzapine greater than risperidone greater than ziprasidone, with cariprazine and lurasidone the mildest.")
q(143, "Extrapyramidal side effects and hyperprolactinaemia are due to blockade of:",
  ["D2 receptors", "5HT2 receptors", "Histamine H1 receptors", "Muscarinic receptors"],
  "The page attributes extrapyramidal effects and hyperprolactinaemia to D2 blockade.")
q(143, "Among atypical agents, D2-related effects are most severe with:",
  ["Risperidone", "Clozapine", "Pimavanserin", "Aripiprazole"],
  "Risperidone is listed in the most severe column.")
q(143, "The atypical agent with the least D2 related effects is:",
  ["Clozapine", "Risperidone", "Paliperidone", "Haloperidol"],
  "Clozapine appears in the least severe column.")
q(143, "In which drug are D2 related effects absent?",
  ["Pimavanserin", "Risperidone", "Clozapine", "Olanzapine"],
  "Pimavanserin is placed in the absent column because it has no D2 blockade.")
q(143, "Metabolic and sedative effects such as obesity, urinary retention and sedation are due to blockade of:",
  ["Receptors other than D2", "D2 receptors only", "Dopamine transporters", "GABA receptors"],
  "These effects are grouped under blockade of other receptors.")
q(143, "Hyperglycaemia with atypical antipsychotics is attributed to:",
  ["Insulin resistance", "Beta cell destruction", "Increased glucagon", "Renal glycosuria"],
  "The page attributes hyperglycaemia to insulin resistance.")
q(143, "The drug with the greatest metabolic and sedative burden is:",
  ["Clozapine", "Lurasidone", "Cariprazine", "Ziprasidone"],
  "The order begins with clozapine as the most severe.")
q(143, "The drug with the least metabolic burden among those listed is:",
  ["Lurasidone", "Clozapine", "Olanzapine", "Risperidone"],
  "Lurasidone is at the mildest end of the list.")
q(143, "Which of the following is NOT listed among the non-D2 receptor mediated effects?",
  ["Extrapyramidal symptoms", "Obesity", "Dyslipidaemia", "Urinary retention"],
  "Extrapyramidal symptoms are D2 mediated; obesity, dyslipidaemia and urinary retention belong to the other receptor group.")

unit("Extrapyramidal Side Effects: Akathisia, Acute Dystonia and Parkinsonism",
     "Akathisia is the commonest extrapyramidal effect and presents as restlessness with pacing around and shifting or crossing of the legs; propranolol is the drug of choice and a benzodiazepine is used if there is no response. Acute dystonia, commoner in young patients, produces abnormal posturing and facial grimacing from muscle contraction and is treated with an anticholinergic, benzhexol (trihexyphenidyl) being preferred, or with the H1 blocker promethazine. Parkinsonism from D2 blockade produces tremors and bradykinesia.")
q(143, "The commonest extrapyramidal side effect of antipsychotics is:",
  ["Akathisia", "Acute dystonia", "Parkinsonism", "Tardive dyskinesia"],
  "Akathisia is marked as the commonest.")
q(143, "Akathisia means:",
  ["Restlessness", "Muscle rigidity", "Tremor at rest", "Involuntary facial movement"],
  "Akathisia is glossed as restlessness.")
q(143, "The presentation of akathisia includes pacing around and:",
  ["Shifting or crossing of the legs", "Facial grimacing", "Lip smacking", "Tongue protrusion"],
  "Shifting and crossing of the legs are listed with pacing around.")
q(143, "The drug of choice for akathisia is:",
  ["Propranolol", "Trihexyphenidyl", "Promethazine", "Bromocriptine"],
  "Propranolol is the DOC for akathisia.")
q(143, "If akathisia does not respond to the drug of choice, the next option is:",
  ["A benzodiazepine", "Levodopa", "An anticholinergic", "Dantrolene"],
  "A benzodiazepine is advised when there is no response.")
q(143, "Acute dystonia is said to occur with increased incidence in:",
  ["Young patients", "Elderly patients", "Women only", "Patients with renal failure"],
  "The page notes the increased incidence in young patients.")
q(143, "The manifestations of acute dystonia listed are abnormal posturing and:",
  ["Facial grimacing", "Lip smacking", "Waving of the hand", "Tongue protrusion"],
  "Facial grimacing and abnormal posturing are listed for acute dystonia.")
q(143, "The drug of choice for acute dystonia is an anticholinergic, specifically:",
  ["Benzhexol (trihexyphenidyl)", "Propranolol", "Promethazine", "Biperiden only"],
  "Anticholinergics are the DOC, with benzhexol or trihexyphenidyl preferred.")
q(143, "The antihistamine used alternatively in acute dystonia is:",
  ["Promethazine", "Cetirizine", "Fexofenadine", "Ranitidine"],
  "Promethazine, an H1 blocker, is named as the alternative.")
q(143, "Drug induced parkinsonism from D2 blockade presents with tremors and:",
  ["Bradykinesia", "Chorea", "Myoclonus", "Ataxia"],
  "Tremors and bradykinesia are listed under parkinsonism.")
q(143, "A young man started on haloperidol develops painful neck muscle spasm and facial grimacing. The diagnosis and treatment are:",
  ["Acute dystonia treated with an anticholinergic such as trihexyphenidyl",
   "Akathisia treated with propranolol",
   "Parkinsonism treated with levodopa",
   "Tardive dyskinesia treated with a VMAT blocker"],
  "Acute dystonia is commoner in the young, presents with abnormal posturing and grimacing, and is treated with anticholinergics.")
q(143, "A patient on an antipsychotic cannot sit still and constantly crosses and uncrosses the legs. The drug of choice is:",
  ["Propranolol", "Trihexyphenidyl", "Dantrolene", "Bromocriptine"],
  "This is akathisia, for which propranolol is the DOC.")

unit("Tardive Dyskinesia and Neuroleptic Malignant Syndrome",
     "Tardive dyskinesia is a late onset movement disorder from upregulation of D2 receptors, producing facial dyskinesia with lip smacking and tongue protrusion and limb dyskinesia with waving of the hand; the drugs of choice are the VMAT blockers tetrabenazine, deutetrabenazine and valbenazine, which prevent dopamine entering the vesicle. Neuroleptic malignant syndrome follows severe D2 blockade and causes severe muscle rigidity, hyperthermia, autonomic instability with sweating and reduced respiratory rate; dantrolene, which inhibits the ryanodine receptor, is the drug of choice, while bromocriptine, a D2 agonist, is the most specific drug. Metoclopramide, a D2 blocking antiemetic, also causes acute dystonia and parkinsonism.")
q(144, "Tardive dyskinesia is described as:",
  ["Late onset", "Immediate onset", "Occurring only with clozapine", "Reversible within hours"],
  "Tardive dyskinesia is labelled late onset.")
q(144, "The mechanism of tardive dyskinesia is:",
  ["Upregulation of D2 receptors", "Downregulation of D2 receptors",
   "Dopamine depletion", "GABA receptor loss"],
  "The aetiology given is upregulation of D2 receptors.")
q(144, "Facial dyskinesia in tardive dyskinesia comprises:",
  ["Lip smacking and tongue protrusion", "Facial grimacing only",
   "Ptosis and diplopia", "Trismus only"],
  "Lip smacking and tongue protrusion are the facial features.")
q(144, "The limb manifestation of tardive dyskinesia described is:",
  ["Waving of the hand", "Foot drop", "Winging of the scapula", "Intention tremor"],
  "Limb dyskinesia is described as waving of the hand.")
q(144, "The drugs of choice for tardive dyskinesia are the:",
  ["VMAT blockers", "Anticholinergics", "Beta blockers", "Benzodiazepines"],
  "VMAT blockers are the DOC for tardive dyskinesia.")
q(144, "The VMAT blockers named are tetrabenazine, deutetrabenazine and:",
  ["Valbenazine", "Reserpine", "Haloperidol", "Bromocriptine"],
  "Valbenazine is the third VMAT blocker named.")
q(144, "VMAT blockers work by:",
  ["Preventing dopamine entry into the vesicle", "Blocking dopamine receptors",
   "Stimulating dopamine release", "Inhibiting monoamine oxidase"],
  "Their mechanism is prevention of dopamine entry into the vesicle.")
q(144, "Neuroleptic malignant syndrome is attributed to:",
  ["Severe D2 receptor blockade", "Anticholinergic excess", "Serotonin excess", "GABA depletion"],
  "The aetiology given is severe D2 block.")
q(144, "Features of neuroleptic malignant syndrome listed include severe muscle rigidity, hyperthermia, sweating, autonomic instability and:",
  ["Reduced respiratory rate", "Bradycardia", "Hypothermia", "Polyuria"],
  "Reduced respiratory rate is listed among the features.")
q(144, "The drug of choice for neuroleptic malignant syndrome is:",
  ["Dantrolene", "Bromocriptine", "Diazepam", "Propranolol"],
  "Dantrolene is the DOC in neuroleptic malignant syndrome.")
q(144, "Dantrolene acts by inhibiting the:",
  ["Ryanodine receptor", "D2 receptor", "Sodium channel", "Calcium channel only in the heart"],
  "Dantrolene's mechanism is inhibition of the ryanodine receptor.")
q(144, "The most specific drug for neuroleptic malignant syndrome is:",
  ["Bromocriptine", "Dantrolene", "Diazepam", "Amantadine"],
  "Bromocriptine is described as the most specific drug.")
q(144, "Bromocriptine is used in neuroleptic malignant syndrome because it is a:",
  ["D2 agonist", "D2 antagonist", "Muscle relaxant", "Antipyretic"],
  "Bromocriptine is a D2 agonist, reversing the blockade that caused the syndrome.")
q(144, "The antiemetic named as also causing acute dystonia and parkinsonism is:",
  ["Metoclopramide", "Ondansetron", "Domperidone only", "Prochlorperazine only"],
  "Metoclopramide, a D2 blocker antiemetic, is noted to cause acute dystonia and parkinsonism.")
q(144, "Dantrolene is also the drug of choice for:",
  ["Malignant hyperthermia", "Tardive dyskinesia", "Serotonin syndrome", "Acute dystonia"],
  "The note states dantrolene is the DOC for malignant hyperthermia.")

unit("Therapeutic Decision Making",
     "In psychosis, treatment starts with an atypical antipsychotic other than clozapine or olanzapine; if the response is inadequate another atypical antipsychotic is added, and if that fails the patient is switched to a typical antipsychotic such as haloperidol or fluphenazine, with electroconvulsive therapy reserved for those still unresponsive. Postpartum psychosis is treated with an antipsychotic plus lithium because of its association with bipolar disorder.")
q(144, "The first step in treating psychosis is to start:",
  ["An atypical antipsychotic other than clozapine or olanzapine",
   "A typical antipsychotic", "Lithium alone", "A benzodiazepine alone"],
  "The algorithm starts with atypical antipsychotics, excluding clozapine and olanzapine.")
q(144, "Clozapine and olanzapine are excluded from the starting regimen because of their:",
  ["Toxicity", "Lack of efficacy", "Cost", "Need for injection"],
  "The two most toxic or metabolically burdened agents are held back rather than used first line.")
q(144, "If the first atypical antipsychotic produces an inadequate response, the next step is to:",
  ["Add another atypical antipsychotic", "Switch immediately to clozapine",
   "Stop all antipsychotics", "Add lithium"],
  "The second step is to add another atypical antipsychotic.")
q(144, "If the response is still inadequate, the next step is to switch to:",
  ["A typical antipsychotic such as haloperidol or fluphenazine",
   "Clozapine", "A benzodiazepine", "An antidepressant"],
  "The third step is a switch to a typical antipsychotic such as haloperidol or fluphenazine.")
q(144, "The option reserved for patients unresponsive to the earlier steps is:",
  ["Electroconvulsive therapy", "Psychosurgery", "Insulin coma therapy", "Long term benzodiazepines"],
  "Electroconvulsive therapy is the last option named in the algorithm.")
q(144, "Postpartum psychosis is treated with an antipsychotic plus:",
  ["Lithium", "Valproate", "Carbamazepine", "An antidepressant alone"],
  "Lithium is added in postpartum psychosis.")
q(144, "The reason lithium is added in postpartum psychosis is its association with:",
  ["Bipolar disorder", "Schizophrenia", "Obsessive-compulsive disorder", "Epilepsy"],
  "The page notes the association of postpartum psychosis with bipolar disorder, hence lithium.")
q(144, "A patient with schizophrenia fails two atypical antipsychotics. According to the algorithm the next step is:",
  ["Switch to a typical antipsychotic such as haloperidol", "Start clozapine immediately",
   "Add a benzodiazepine", "Stop treatment and observe"],
  "After an inadequate response to atypical agents including an add-on, the algorithm switches to a typical antipsychotic.")
q(144, "Which statement about antipsychotic choice is correct?",
  ["Atypical agents are first line, typical agents are second line, and ECT is reserved for the unresponsive",
   "Typical agents are first line and atypical agents second line",
   "Clozapine is the first line drug of choice in every patient",
   "Lithium alone is the treatment of choice in schizophrenia"],
  "The algorithm and comparison table put atypical agents first, typical agents second and ECT last.")
q(144, "Haloperidol and fluphenazine appear in the algorithm as:",
  ["Typical antipsychotics used after atypical agents fail",
   "First line drugs", "Drugs used only in postpartum psychosis", "Drugs used only for insomnia"],
  "They are the typical antipsychotics named for the switch step of the algorithm.")

# ---------------------------------------------------------------------------
# Chapter 36: Neurodegenerative Disorders (p145-149)
# ---------------------------------------------------------------------------
start(36)
unit("Neurodegenerative Disorders: Overview",
     "The neurodegenerative chapter opens with the common cause of these disorders: free radical damage to cells, which is increased by excitatory neurotransmitters. Three diseases are then set out side by side. Alzheimer's disease is a state of reduced acetylcholine and presents with memory loss. Amyotrophic lateral sclerosis is death of motor neurons and presents with muscle spasticity. Parkinson's disease is death of dopaminergic neurons in the corpus striatum with a fall in dopamine levels, presenting with tremors and bradykinesia.")
q(145, "The cause common to neurodegenerative disorders given at the top of the chapter is:",
  ["Free radical damage to cells", "Autoantibody mediated demyelination",
   "Prion protein deposition", "Mitochondrial DNA deletion"],
  "The page opens with the cause: free radical damage to cells.")
q(145, "The free radical damage of neurodegeneration is said to be increased by:",
  ["Excitatory neurotransmitters", "Inhibitory neurotransmitters",
   "Acetylcholinesterase", "Dopamine reuptake"],
  "The parenthesis after the cause reads that it is increased by excitatory neurotransmitters.")
q(145, "The three neurodegenerative disorders listed are Alzheimer's disease, amyotrophic lateral sclerosis and:",
  ["Parkinson's disease", "Huntington's chorea",
   "Multiple sclerosis", "Creutzfeldt-Jakob disease"],
  "The three headings are Alzheimer's disease, ALS and Parkinson's disease.")
q(145, "The neurotransmitter described as deficient in Alzheimer's disease is:",
  ["Acetylcholine", "Dopamine", "GABA", "Serotonin"],
  "Alzheimer's disease is listed with a decrease of acetylcholine.")
q(145, "The clinical feature linked to the acetylcholine deficit in Alzheimer's disease is:",
  ["Memory loss", "Tremors", "Muscle spasticity", "Bradykinesia"],
  "Memory loss is the feature noted under Alzheimer's disease.")
q(145, "The pathological basis of amyotrophic lateral sclerosis is death of:",
  ["Motor neurons", "Dopaminergic neurons", "Cholinergic neurons", "Purkinje cells"],
  "ALS is described as motor neuron death.")
q(145, "The manifestation of motor neuron death in ALS noted here is:",
  ["Muscle spasticity", "Memory loss", "Bradykinesia", "Tremors"],
  "Muscle spasticity is the feature listed under ALS.")
q(145, "In Parkinson's disease the neurons that die are the:",
  ["Dopaminergic neurons of the corpus striatum", "Cholinergic neurons of the nucleus basalis",
   "Motor neurons of the anterior horn", "GABAergic neurons of the striatum"],
  "Parkinson's disease is described as death of dopaminergic neurons in the corpus striatum.")
q(145, "The two clinical features listed for Parkinson's disease are tremors and:",
  ["Bradykinesia", "Memory loss", "Spasticity", "Ataxia"],
  "The page lists tremors and bradykinesia under Parkinson's disease.")
q(145, "A 70 year old with memory loss and a 60 year old with tremor and bradykinesia illustrate the two ends of this page, the neurotransmitter deficits being respectively:",
  ["Low acetylcholine and low dopamine", "Low dopamine and low acetylcholine",
   "Low GABA in both", "Low serotonin in both"],
  "Alzheimer's disease is the low acetylcholine memory loss state and Parkinson's disease is the low dopamine tremor bradykinesia state.")

unit("Drugs for Alzheimer's Disease: Cholinergics",
     "Cholinergics are the most preferred drugs for Alzheimer's disease. They act by blocking acetylcholinesterase so that acetylcholine levels rise. Four drugs are named in order. Tacrine is not preferred because of hepatotoxicity. Rivastigmine is used in mild to moderate disease. Galantamine is listed third. Donepezil is the drug of choice and can be used in mild, moderate or severe disease.")
q(145, "The heading under which the Alzheimer's drugs are grouped first is:",
  ["Cholinergics", "Anti-beta amyloid monoclonal antibodies",
   "Nootropic drugs", "NMDA blockers"],
  "The first group listed under drugs for Alzheimer's disease is cholinergics.")
q(145, "Cholinergics are described as:",
  ["Most preferred drugs", "Least preferred drugs",
   "Not preferred", "Add-on drugs only"],
  "The word most preferred is written against cholinergics.")
q(145, "The mechanism of action of the cholinergics in Alzheimer's disease is:",
  ["Block acetylcholinesterase so that acetylcholine increases",
   "Block NMDA receptors",
   "Stimulate nicotinic receptors directly",
   "Increase acetylcholine release from vesicles"],
  "The mechanism given is block of acetylcholinesterase leading to raised acetylcholine.")
q(145, "Which cholinesterase inhibitor is described as not preferred?",
  ["Tacrine", "Donepezil", "Rivastigmine", "Galantamine"],
  "Tacrine is the drug labelled not preferred.")
q(145, "The side effect that makes tacrine an unfavoured drug is:",
  ["Hepatotoxicity", "Nephrotoxicity", "Ototoxicity", "Pulmonary fibrosis"],
  "Hepatotoxicity is the side effect listed for tacrine.")
q(145, "The cholinesterase inhibitor indicated for mild to moderate disease is:",
  ["Rivastigmine", "Donepezil", "Tacrine", "Galantamine"],
  "Rivastigmine carries the indication mild to moderate disease.")
q(145, "The drug of choice among the cholinergics for Alzheimer's disease is:",
  ["Donepezil", "Tacrine", "Rivastigmine", "Galantamine"],
  "Donepezil is marked as the drug of choice.")
q(145, "Donepezil can be used in which stages of Alzheimer's disease?",
  ["Mild, moderate and severe disease", "Mild disease only",
   "Severe disease only", "Moderate disease only"],
  "Donepezil is stated to be useful in mild, moderate and severe disease.")
q(145, "Which cholinesterase inhibitor is listed without any restriction of stage or preference?",
  ["Galantamine", "Tacrine", "Rivastigmine", "Donepezil"],
  "Galantamine is listed third, with no stage restriction or preference note attached.")
q(145, "A patient with severe Alzheimer's disease should receive:",
  ["Donepezil", "Rivastigmine", "Tacrine", "No cholinesterase inhibitor"],
  "Only donepezil is documented for use in severe disease; rivastigmine is restricted to mild to moderate disease.")
q(145, "A patient on tacrine is found to have rising transaminases. The most appropriate change is to:",
  ["Stop tacrine and use another cholinergic such as donepezil",
   "Continue tacrine and add a hepatoprotective", "Increase the dose of tacrine",
   "Switch to an anti-beta amyloid antibody"],
  "Tacrine is not preferred because of hepatotoxicity, so another cholinergic, preferably donepezil, replaces it.")
q(145, "The biochemical aim shared by all four drugs in this group is to:",
  ["Raise central acetylcholine", "Lower central glutamate",
   "Raise central dopamine", "Raise central GABA"],
  "All act by blocking acetylcholinesterase and raising acetylcholine.")
q(145, "Which statement about cholinergics in Alzheimer's disease is correct?",
  ["They are most preferred and act by blocking acetylcholinesterase",
   "They are add-on drugs that block NMDA receptors",
   "They are not FDA approved for Alzheimer's disease",
   "Their mechanism of action is well established as free radical scavenging"],
  "Cholinergics are the most preferred group and block acetylcholinesterase; it is the nootropics that are not FDA approved with unknown mechanism.")

unit("Memantine",
     "Memantine appears after the cholinergics as the option when there is no response. It is an add-on drug whose mechanism is blockade of NMDA receptors, so it complements rather than replaces the cholinergic approach.")
q(145, "Memantine is listed in the Alzheimer's section as:",
  ["An add-on drug", "The most preferred drug",
   "A drug not preferred", "A drug for muscle spasticity"],
  "Memantine is described as an add-on drug.")
q(145, "The mechanism of action of memantine is:",
  ["Blocks NMDA receptors", "Blocks acetylcholinesterase",
   "Blocks beta amyloid fibrils", "Blocks histone deacetylase"],
  "The mechanism given is blockade of NMDA receptors.")
q(145, "Memantine is reached in the Alzheimer's algorithm after:",
  ["No response to cholinergics", "A hepatotoxic reaction to tacrine",
   "MRI confirmation of beta amyloid deposition", "Development of muscle spasticity"],
  "The note no response appears just before memantine in the sequence.")
q(145, "Unlike the cholinergics, memantine acts on the:",
  ["Glutamate system", "Cholinergic system", "Dopaminergic system", "GABA system"],
  "NMDA receptor blockade places memantine in the glutamate system rather than the cholinergic system.")
q(145, "A patient with moderate Alzheimer's disease on donepezil continues to deteriorate. According to this page the next step is to:",
  ["Add memantine", "Switch to tacrine",
   "Add a nootropic drug", "Stop all drugs"],
  "Memantine is the add-on drug used when there is no response to cholinergics.")
q(145, "Which pair correctly matches drug and mechanism?",
  ["Donepezil blocks acetylcholinesterase, memantine blocks NMDA",
   "Donepezil blocks NMDA, memantine blocks acetylcholinesterase",
   "Both block acetylcholinesterase", "Both block NMDA receptors"],
  "The cholinergics block acetylcholinesterase and memantine blocks NMDA receptors.")

unit("Anti-beta Amyloid Monoclonal Antibodies",
     "The second group of Alzheimer's drugs is the anti-beta amyloid monoclonal antibodies. Their use is restricted to mild disease and to patients in whom MRI has confirmed beta amyloid deposition in the brain. Aducanumab blocks fibrils while lecanemab blocks protofibrils.")
q(145, "The second group of drugs listed for Alzheimer's disease is:",
  ["Anti-beta amyloid monoclonal antibodies", "Cholinergics",
   "Nootropic drugs", "NMDA antagonists"],
  "The second heading is anti-beta amyloid monoclonal antibodies.")
q(145, "Anti-beta amyloid monoclonal antibodies may be used only after:",
  ["MRI confirmed beta amyloid deposition in brain", "CT confirmed cerebral atrophy",
   "PET showing reduced glucose uptake", "CSF showing raised tau protein"],
  "Their use requires MRI confirmed beta amyloid deposition in the brain.")
q(145, "The stage of disease in which anti-beta amyloid antibodies are used is:",
  ["Mild disease", "Severe disease",
   "Any stage", "End stage disease only"],
  "The indication is mild disease.")
q(145, "The monoclonal antibody that blocks fibrils is:",
  ["Aducanumab", "Lecanemab", "Donepezil", "Memantine"],
  "Aducanumab blocks fibrils.")
q(145, "The monoclonal antibody that blocks protofibrils is:",
  ["Lecanemab", "Aducanumab", "Tacrine", "Rivastigmine"],
  "Lecanemab blocks protofibrils.")
q(145, "A patient with severe Alzheimer's disease asks about aducanumab. The correct response is that it is:",
  ["Not indicated, since these antibodies are used only in mild disease",
   "Indicated at any stage", "Indicated only after memantine fails",
   "Indicated as the drug of choice in severe disease"],
  "Anti-beta amyloid antibodies are restricted to mild disease.")
q(145, "Which is correctly paired?",
  ["Aducanumab fibrils, lecanemab protofibrils",
   "Aducanumab protofibrils, lecanemab fibrils",
   "Both block fibrils", "Both block protofibrils"],
  "Aducanumab blocks fibrils and lecanemab blocks protofibrils.")

unit("Nootropic Drugs",
     "The third group is the nootropic drugs, described as memory enhancers. They are not FDA approved for Alzheimer's disease and their mechanism of action is unknown. The drugs named are piribedil, piracetam, citicoline and cerebrolysin.")
q(145, "The third group of drugs for Alzheimer's disease is:",
  ["Nootropic drugs", "Anti-beta amyloid monoclonal antibodies",
   "Cholinergics", "NMDA blockers"],
  "The third heading is nootropic drugs.")
q(145, "Nootropic drugs are described as:",
  ["Memory enhancers", "Muscle relaxants",
   "Free radical scavengers", "Antipsychotics"],
  "Nootropics are labelled memory enhancers.")
q(145, "The regulatory status of nootropic drugs in Alzheimer's disease is that they:",
  ["Are not FDA approved for Alzheimer's disease",
   "Are the FDA approved drugs of choice",
   "Are approved only for severe disease",
   "Are approved only as add-on to memantine"],
  "The page states they are not FDA approved for Alzheimer's disease.")
q(145, "The mechanism of action of the nootropic drugs is stated to be:",
  ["Unknown", "Acetylcholinesterase blockade",
   "NMDA blockade", "Beta amyloid binding"],
  "The mechanism of action of nootropics is given as unknown.")
q(145, "Which of the following is named as a nootropic drug?",
  ["Citicoline", "Donepezil", "Memantine", "Aducanumab"],
  "Citicoline is one of the drugs listed under nootropics.")
q(145, "Which of the following is named as a nootropic drug?",
  ["Cerebrolysin", "Lecanemab", "Galantamine", "Tacrine"],
  "Cerebrolysin is listed among the nootropic drugs.")
q(145, "A patient with Alzheimer's disease is already on a nootropic drug alone. The most appropriate comment is that:",
  ["Nootropics are not FDA approved for Alzheimer's disease and their mechanism is unknown, so a cholinesterase inhibitor such as donepezil is preferred",
   "Nootropics are the most preferred drugs",
   "Nootropics block NMDA receptors and are curative",
   "Nootropics are the drugs of choice in mild disease with MRI confirmed amyloid"],
  "Cholinergics are the most preferred drugs, whereas nootropics are not FDA approved with unknown mechanism.")

unit("Drugs for ALS: Preventing Neurodegeneration",
     "Drugs for amyotrophic lateral sclerosis are divided into those that prevent neurodegeneration and those that treat muscle spasticity. Under prevention, riluzole is the drug of choice and blocks sodium channels to reduce glutamate. Edaravone is an add-on drug acting as a free radical scavenger. Sodium phenylbutyrate is combined with taurursodiol, which is anti-apoptotic, and inhibits histone deacetylase. Tofersen is a new antisense oligonucleotide that blocks the messenger RNA of superoxide dismutase 1 and is used in ALS with an SOD1 gene mutation.")
q(146, "The two headings under drugs for ALS are drugs to prevent neurodegeneration and drugs to treat:",
  ["Muscle spasticity", "Memory loss", "Tremors", "Sialorrhoea"],
  "The two groups are drugs to prevent neurodegeneration and drugs to treat muscle spasticity.")
q(146, "The drug of choice for amyotrophic lateral sclerosis is:",
  ["Riluzole", "Edaravone", "Tofersen", "Baclofen"],
  "Riluzole is listed first and marked DOC.")
q(146, "The mechanism of action of riluzole is to block:",
  ["Sodium channels and thereby reduce glutamate", "Calcium channels",
   "NMDA receptors directly", "Histone deacetylase"],
  "Riluzole blocks sodium channels, which reduces glutamate.")
q(146, "Edaravone is used in ALS as:",
  ["An add-on drug", "The drug of choice",
   "Rescue therapy", "A muscle relaxant"],
  "Edaravone is labelled an add-on drug.")
q(146, "The mechanism of action of edaravone is:",
  ["Free radical scavenger", "Histone deacetylase inhibitor",
   "Antisense oligonucleotide", "GABA receptor agonist"],
  "Edaravone is a free radical scavenger.")
q(146, "The free radical scavenging action of edaravone is logical in ALS because the chapter's stated cause of neurodegeneration is:",
  ["Free radical damage to cells", "Prion deposition",
   "Autoimmune demyelination", "Acetylcholine deficiency"],
  "The chapter opened with free radical damage to cells as the common cause, which is what edaravone targets.")
q(146, "Sodium phenylbutyrate is combined with:",
  ["Taurursodiol", "Edaravone", "Riluzole", "Trofinetide"],
  "Sodium phenylbutyrate is given with taurursodiol.")
q(146, "Taurursodiol is described as:",
  ["Anti-apoptotic", "A free radical scavenger",
   "A histone deacetylase inhibitor", "A GABA agonist"],
  "The bracket after taurursodiol reads anti-apoptotic.")
q(146, "The mechanism of action of sodium phenylbutyrate is:",
  ["Inhibits histone deacetylase", "Blocks sodium channels",
   "Scavenges free radicals", "Blocks mRNA of SOD1"],
  "Sodium phenylbutyrate inhibits histone deacetylase.")
q(146, "Tofersen is described as:",
  ["A new drug that is an antisense oligonucleotide",
   "A free radical scavenger", "A muscle relaxant",
   "A histone deacetylase inhibitor"],
  "Tofersen is the new drug described as an antisense oligonucleotide.")
q(146, "Tofersen blocks the messenger RNA of:",
  ["Superoxide dismutase 1", "Superoxide dismutase 2",
   "Histone deacetylase", "Glutamate transporter"],
  "The target given is the mRNA of SOD1, superoxide dismutase 1.")
q(146, "Tofersen is used specifically in:",
  ["ALS with SOD1 gene mutation", "All cases of ALS",
   "Rett syndrome", "Friedreich's ataxia"],
  "The use is ALS with SOD1 gene mutation.")
q(146, "Which drug is matched correctly with its indication?",
  ["Tofersen - ALS with SOD1 gene mutation",
   "Trofinetide - Friedreich's ataxia",
   "Omaveloxolone - Rett syndrome",
   "Edaravone - muscle spasticity"],
  "Tofersen is for ALS with SOD1 mutation; trofinetide is for Rett syndrome and omaveloxolone for Friedreich's ataxia.")
q(146, "A patient with ALS and a documented SOD1 mutation is best treated with:",
  ["Tofersen", "Riluzole only", "Baclofen", "Edaravone only"],
  "Tofersen blocks SOD1 mRNA and is used in ALS with SOD1 gene mutation.")

unit("Muscle Spasticity in ALS and Related Notes",
     "Muscle spasticity in ALS is treated with baclofen, a muscle relaxant acting as a GABA receptor agonist. Two notes close the ALS section: trofinetide is the only drug for Rett syndrome and omaveloxolone is the only drug for Friedreich's ataxia.")
q(146, "The drug used to treat muscle spasticity in ALS is:",
  ["Baclofen", "Riluzole", "Edaravone", "Tofersen"],
  "Baclofen is the drug listed to treat muscle spasticity.")
q(146, "Baclofen is described as a:",
  ["Muscle relaxant", "Free radical scavenger",
   "Antisense oligonucleotide", "Cholinesterase inhibitor"],
  "Baclofen is labelled a muscle relaxant.")
q(146, "The mechanism of action of baclofen is:",
  ["GABA receptor agonist", "NMDA receptor blocker",
   "Sodium channel blocker", "Histone deacetylase inhibitor"],
  "Baclofen acts as a GABA receptor agonist.")
q(146, "The only drug for Rett syndrome is:",
  ["Trofinetide", "Omaveloxolone", "Tofersen", "Riluzole"],
  "The note states trofinetide is the only drug for Rett syndrome.")
q(146, "The only drug for Friedreich's ataxia is:",
  ["Omaveloxolone", "Trofinetide", "Edaravone", "Baclofen"],
  "Omaveloxolone is noted as the only drug for Friedreich's ataxia.")
q(146, "Which pairing of drug and unique indication is correct?",
  ["Trofinetide Rett syndrome, omaveloxolone Friedreich's ataxia",
   "Trofinetide Friedreich's ataxia, omaveloxolone Rett syndrome",
   "Both are used for ALS", "Both are used for Alzheimer's disease"],
  "Trofinetide is for Rett syndrome and omaveloxolone for Friedreich's ataxia.")

unit("Synthesis and Metabolism of Dopamine",
     "The Parkinson's section begins with the dopamine synapse. Tyrosine is converted to dopa with vitamin B as cofactor, dopa is converted to dopamine by dopa decarboxylase, dopamine is taken into the synaptic vesicle by VMAT-2 and released to act on the post-synaptic neuron. Dopamine is then metabolised by MAO-B and COMT. MAO-B stands for monoamine oxidase B in brain and COMT for catechol-O-methyl transferase.")
q(146, "The amino acid from which dopamine synthesis begins is:",
  ["Tyrosine", "Tryptophan", "Phenylalanine only", "Glutamate"],
  "The synthesis scheme starts from tyrosine.")
q(146, "Tyrosine is converted to:",
  ["Dopa", "Dopamine directly", "Noradrenaline", "Homovanillic acid"],
  "The scheme shows tyrosine going to dopa.")
q(146, "The cofactor shown at the tyrosine to dopa step is:",
  ["Vitamin B", "Vitamin C", "Vitamin D", "Vitamin K"],
  "A vitamin B cofactor is noted at the tyrosine to dopa step.")
q(146, "Dopa is converted to dopamine by:",
  ["Dopa decarboxylase", "Tyrosine hydroxylase",
   "Monoamine oxidase B", "Catechol-O-methyl transferase"],
  "Dopa decarboxylase converts dopa to dopamine.")
q(146, "Dopamine is pumped into the synaptic vesicle by:",
  ["VMAT-2", "DAT", "MAO-B", "COMT"],
  "The vesicular transporter shown is VMAT-2.")
q(146, "After release, dopamine acts on:",
  ["The post-synaptic neuron", "The pre-synaptic neuron only",
   "The muscle end plate", "The dorsal root ganglion"],
  "The released dopamine is shown acting on the post-synaptic neuron.")
q(146, "The two enzymes shown metabolising dopamine are:",
  ["MAO-B and COMT", "MAO-A and COMT",
   "MAO-B and acetylcholinesterase", "Dopa decarboxylase and COMT"],
  "Dopamine is metabolised by MAO-B and COMT.")
q(146, "MAO-B stands for:",
  ["Monoamine oxidase B", "Monoamine oxidase brain",
   "Methyl amine oxidase B", "Monoacetyl oxidase B"],
  "The index expands MAO-B as monoamine oxidase B.")
q(146, "COMT stands for:",
  ["Catechol-O-methyl transferase", "Catechol-O-methyl transferase A",
   "Catechol monoamine transporter", "Cytochrome O methyl transferase"],
  "COMT is expanded as catechol-O-methyl transferase.")
q(146, "A drug that blocks both MAO-B and the peripheral decarboxylation of levodopa is acting on:",
  ["The metabolism and activation of dopamine", "The vesicular storage of dopamine only",
   "Dopamine receptors directly", "Acetylcholine synthesis"],
  "MAO-B metabolises dopamine and dopa decarboxylase forms it, so blocking both alters dopamine metabolism and formation.")

unit("Levodopa",
     "Levodopa is the best drug for Parkinson's disease and the drug of choice in patients above 65 years. It is the levo-isomer of dopa and a prodrug of dopamine, converted by dopa decarboxylase. Efficacy is increased by carbidopa, a lipid insoluble dopa analogue that does not cross the blood brain barrier and reduces peripheral metabolism of levodopa, and by entacapone, a COMT inhibitor that blocks first pass metabolism and raises oral bioavailability. Efficacy is reduced by vitamin B6, which increases the activity of dopa decarboxylase. Side effects are recalled by the mnemonic DOPA: dyskinesia from excess dopamine, treated with amantadine; orthostatic hypotension; psychosis from D2 stimulation, which also causes nausea and vomiting; and angle closure glaucoma from mydriasis. Psychosis is an absolute contraindication, while angle closure glaucoma, peptic ulcer disease and melanoma are relative contraindications.")
q(147, "Levodopa is described as the:",
  ["Best drug for Parkinson's disease", "Worst drug for Parkinson's disease",
   "Drug used only for tremors", "Drug used only in young patients"],
  "Levodopa is labelled the best drug for Parkinson's disease.")
q(147, "Levodopa is the drug of choice in patients with Parkinson's disease aged:",
  ["Above 65 years", "Below 65 years",
   "Below 40 years", "Between 40 and 50 years"],
  "Levodopa is the DOC in patients above 65 years.")
q(147, "Levodopa is the:",
  ["Levo-isomer of dopa and a prodrug of dopamine",
   "Dextro-isomer of dopa",
   "Active form of dopamine already",
   "Dopamine receptor agonist"],
  "It is the levo-isomer of dopa and a prodrug of dopamine.")
q(147, "Levodopa is converted to dopamine by:",
  ["Dopa decarboxylase", "Tyrosine hydroxylase",
   "Catechol-O-methyl transferase", "Monoamine oxidase B"],
  "The scheme shows levodopa becoming dopamine through dopa decarboxylase.")
q(147, "Carbidopa is an analogue of:",
  ["Dopa", "Dopamine", "Tyrosine", "Catecholamine"],
  "Carbidopa is described as an analogue of dopa.")
q(147, "Carbidopa is lipid insoluble and therefore:",
  ["Does not cross the blood brain barrier",
   "Enters the brain freely", "Is given intrathecally",
   "Is excreted unchanged by the kidney"],
  "The page notes it is lipid insoluble and does not cross the blood brain barrier.")
q(147, "The mechanism by which carbidopa improves levodopa therapy is:",
  ["It reduces levodopa metabolism in the periphery and increases availability in brain",
   "It stimulates dopamine receptors directly",
   "It blocks COMT in the brain",
   "It increases dopa decarboxylase activity"],
  "Carbidopa lowers peripheral metabolism of levodopa and raises its availability in the brain.")
q(147, "The COMT inhibitor listed among drugs that increase levodopa efficacy is:",
  ["Entacapone", "Carbidopa", "Vitamin B6", "Amantadine"],
  "Entacapone is the COMT inhibitor listed with carbidopa.")
q(147, "Entacapone increases levodopa efficacy by:",
  ["Blocking first pass metabolism and increasing oral bioavailability",
   "Blocking renal excretion", "Stimulating dopamine release",
   "Blocking dopa decarboxylase centrally"],
  "Entacapone blocks first pass metabolism of levodopa and increases oral bioavailability.")
q(147, "The agent listed under drugs that decrease levodopa efficacy is:",
  ["Vitamin B6", "Carbidopa", "Entacapone", "Amantadine"],
  "Vitamin B6 is the drug listed as decreasing efficacy.")
q(147, "Vitamin B6 reduces levodopa efficacy because it:",
  ["Increases the activity of dopa decarboxylase",
   "Blocks dopa decarboxylase", "Blocks COMT",
   "Blocks dopamine receptors"],
  "Vitamin B6 increases the activity of dopa decarboxylase, so more levodopa is converted outside the brain.")
q(147, "The mnemonic used for the side effects of levodopa is:",
  ["DOPA", "CHOP", "PADA", "MAD"],
  "The side effects are remembered with the mnemonic DOPA.")
q(147, "In the DOPA mnemonic, D stands for:",
  ["Dyskinesia", "Drowsiness", "Diarrhoea", "Depression"],
  "D stands for dyskinesia, due to increased dopamine.")
q(147, "The drug of choice for levodopa induced dyskinesia is:",
  ["Amantadine", "Baclofen", "Trihexyphenidyl", "Propranolol"],
  "Amantadine is the DOC for dyskinesia caused by levodopa.")
q(147, "In the DOPA mnemonic, O stands for:",
  ["Orthostatic hypotension", "Oedema", "Oliguria", "Osteoporosis"],
  "O stands for orthostatic hypotension.")
q(147, "In the DOPA mnemonic, P for psychosis is attributed to:",
  ["D2 stimulation", "D1 stimulation", "Muscarinic blockade", "NMDA blockade"],
  "Psychosis is stated to be due to D2 stimulation.")
q(147, "The nausea and vomiting of levodopa are grouped in the mnemonic under:",
  ["P for psychosis, since they also result from dopamine stimulation",
   "O for orthostatic hypotension", "A for angle closure glaucoma",
   "D for dyskinesia"],
  "The page adds that the D2 stimulation causing psychosis also causes nausea and vomiting.")
q(147, "In the DOPA mnemonic, A stands for:",
  ["Angle closure glaucoma from mydriasis",
   "Alopecia", "Agranulocytosis", "Akathisia"],
  "A stands for angle closure glaucoma, due to mydriasis.")
q(147, "The absolute contraindication to levodopa listed here is:",
  ["Psychosis", "Peptic ulcer disease", "Melanoma", "Angle closure glaucoma"],
  "Psychosis is the absolute contraindication.")
q(147, "The relative contraindications to levodopa listed here include:",
  ["Angle closure glaucoma, peptic ulcer disease and melanoma",
   "Psychosis and schizophrenia", "Renal failure and hepatic failure",
   "Myasthenia gravis and epilepsy"],
  "The relative column lists angle closure glaucoma, peptic ulcer disease and melanoma.")

unit("Dopamine Agonists",
     "The dopamine agonists are pramipexole and ropinirole, both oral, and rotigotine which is given orally or as a transdermal patch. They are the drugs of choice in patients below 65 years and are not preferred above 65 years. They are also used in restless leg syndrome. Their side effects are fatigue and compulsive behaviours such as compulsive sexual activity and gambling. Apomorphine is given subcutaneously as rescue therapy for the on-off phenomenon; it causes severe nausea and vomiting for which trimethobenzamide is the drug of choice, started three hours before apomorphine and continued for a few months, while ondansetron is contraindicated because of the risk of hypotension.")
q(147, "The group of drugs listed after levodopa is:",
  ["Dopamine agonists", "MAO-B inhibitors",
   "COMT inhibitors", "Anticholinergics"],
  "The next heading after levodopa is DA agonists.")
q(147, "The dopamine agonist given by the oral route only among the three named is/are:",
  ["Pramipexole and ropinirole", "Rotigotine only",
   "Apomorphine only", "Rotigotine and apomorphine"],
  "Pramipexole and ropinirole are both labelled oral.")
q(147, "The dopamine agonist available as a transdermal patch is:",
  ["Rotigotine", "Pramipexole", "Ropinirole", "Apomorphine"],
  "Rotigotine is available as an oral or transdermal patch formulation.")
q(147, "The dopamine agonists are the drugs of choice in patients with Parkinson's disease aged:",
  ["Below 65 years", "Above 65 years",
   "Below 40 years only", "Any age equally"],
  "They are the DOC for patients below 65 years.")
q(147, "Dopamine agonists are described as not preferred in patients aged:",
  ["Above 65 years", "Below 65 years",
   "Below 30 years", "Between 50 and 60 years"],
  "The side effect note says they are not preferred above 65 years.")
q(147, "The other use of dopamine agonists listed on this page is:",
  ["Restless leg syndrome", "Alzheimer's disease",
   "Amyotrophic lateral sclerosis", "Muscle spasticity"],
  "Restless leg syndrome is listed as another use.")
q(147, "The drugs of choice for restless leg syndrome as given here are:",
  ["Pregabalin or gabapentin", "Levodopa or carbidopa",
   "Baclofen or tizanidine", "Trihexyphenidyl or benzhexol"],
  "Pregabalin and gabapentin are named as the drugs of choice for restless leg syndrome.")
q(147, "The psychiatric side effect peculiar to dopamine agonists is:",
  ["Compulsive sexual activity and gambling", "Obsessive washing",
   "Delirium tremens", "Kleptomania only"],
  "Compulsive sexual activity and gambling are listed as side effects.")
q(147, "The non-psychiatric side effect of dopamine agonists listed here is:",
  ["Fatigue", "Ankle oedema", "Livedo reticularis", "Hepatotoxicity"],
  "Fatigue is the side effect listed for dopamine agonists.")
q(147, "Apomorphine is given by the:",
  ["Subcutaneous route", "Oral route", "Transdermal patch", "Intrathecal route"],
  "Apomorphine is noted as being given by the SC route.")
q(147, "Apomorphine is used as:",
  ["Rescue therapy for the on-off phenomenon",
   "First line therapy in young patients",
   "Treatment of restless leg syndrome",
   "Treatment of levodopa induced psychosis"],
  "Apomorphine is the rescue therapy for the on-off phenomenon.")
q(147, "The troublesome side effect of apomorphine is:",
  ["Severe nausea and vomiting", "Severe constipation",
   "Marked bradycardia", "Agranulocytosis"],
  "Severe nausea and vomiting are listed as the side effect of apomorphine.")
q(147, "The drug of choice for the nausea and vomiting of apomorphine is:",
  ["Trimethobenzamide", "Ondansetron", "Metoclopramide", "Domperidone"],
  "Trimethobenzamide is the DOC for this nausea and vomiting.")
q(147, "Trimethobenzamide is started how long before apomorphine?",
  ["Three hours before", "Three minutes before",
   "One hour after", "Immediately with the dose"],
  "It is started three hours before apomorphine.")
q(147, "Why is ondansetron contraindicated with apomorphine?",
  ["It increases the risk of hypotension",
   "It causes severe dystonia",
   "It blocks the anti-parkinsonian effect",
   "It causes agranulocytosis"],
  "Ondansetron is contraindicated because of an increased risk of hypotension.")

unit("MAO-B Inhibitors",
     "The MAO-B inhibitors are classified as irreversible and reversible. Rasagiline and selegiline are irreversible, and selegiline is additionally said to prevent neurodegeneration; selegiline is metabolised to amphetamine, which causes anxiety and insomnia. Safinamide is the reversible agent. These drugs are used for the on-off phenomenon and as initial treatment in young onset Parkinson's disease.")
q(148, "The MAO-B inhibitors are classified as:",
  ["Irreversible and reversible", "Selective and non-selective",
   "Short and long acting only", "Peripheral and central only"],
  "The classification given is irreversible and reversible.")
q(148, "The irreversible MAO-B inhibitors named are:",
  ["Rasagiline and selegiline", "Safinamide and rasagiline",
   "Selegiline and safinamide", "Entacapone and tolcapone"],
  "Rasagiline and selegiline are listed under irreversible.")
q(148, "The reversible MAO-B inhibitor is:",
  ["Safinamide", "Selegiline", "Rasagiline", "Tolcapone"],
  "Safinamide is the reversible agent.")
q(148, "The MAO-B inhibitor stated to prevent neurodegeneration is:",
  ["Selegiline", "Rasagiline", "Safinamide", "Entacapone"],
  "Selegiline carries the note that it can prevent neurodegeneration.")
q(148, "Selegiline is metabolised to:",
  ["Amphetamine", "Dopamine", "Noradrenaline", "L-dopa"],
  "The scheme notes selegiline is metabolised to amphetamine.")
q(148, "The amphetamine metabolite of selegiline produces:",
  ["Anxiety and insomnia", "Sedation and hypotension",
   "Bradykinesia", "Confusion and hallucinations only"],
  "Anxiety and insomnia are the effects noted for the amphetamine metabolite.")
q(148, "The reversible MAO-B inhibitor safinamide is used for:",
  ["On-off phenomena", "Acute dystonia",
   "Restless leg syndrome", "Muscle spasticity"],
  "Safinamide's use is given as on-off phenomena.")
q(148, "MAO-B inhibitors are used in:",
  ["Initial treatment and young onset of Parkinson's disease",
   "Only end stage disease", "Only in patients above 65 years",
   "Only as rescue therapy"],
  "The use listed is initial treatment and young onset of Parkinson's disease.")
q(148, "A young patient with newly diagnosed Parkinson's disease and mild symptoms could be started on:",
  ["Selegiline", "Apomorphine", "Levodopa", "Amantadine only as rescue therapy"],
  "MAO-B inhibitors such as selegiline are used as initial treatment in young onset disease.")
q(148, "Which statement about MAO-B inhibitors is correct?",
  ["Selegiline is irreversible, prevents neurodegeneration and is metabolised to amphetamine",
   "Selegiline is reversible and free of metabolites",
   "Safinamide is irreversible and used only in elderly patients",
   "Rasagiline is reversible and used as rescue therapy"],
  "Selegiline is grouped with the irreversible agents, can prevent neurodegeneration and is metabolised to amphetamine.")

unit("COMT Inhibitors",
     "The COMT inhibitors are reversible and are the drugs of choice for the on-off phenomenon. Entacapone and opicapone are named, and tolcapone is noted for its greater potency but is hepatotoxic.")
q(148, "COMT inhibitors are described as:",
  ["Reversible", "Irreversible",
   "Non-selective", "Peripheral only"],
  "The word reversible is written against COMT inhibitors.")
q(148, "COMT inhibitors are the drugs of choice for:",
  ["On-off phenomena", "Acute dystonia",
   "Restless leg syndrome", "Alzheimer's disease"],
  "They are the DOC for on-off phenomena.")
q(148, "The COMT inhibitor noted for increased potency is:",
  ["Tolcapone", "Entacapone", "Opicapone", "Safinamide"],
  "Tolcapone is noted for increased potency.")
q(148, "The disadvantage of tolcapone is that it is:",
  ["Hepatotoxic", "Nephrotoxic", "Ototoxic", "Cardiotoxic"],
  "Hepatotoxicity is the bracketed note against tolcapone.")
q(148, "Which of the following is a COMT inhibitor named on this page?",
  ["Opicapone", "Rasagiline", "Safinamide", "Pramipexole"],
  "Opicapone is listed among the COMT inhibitors.")
q(148, "The COMT inhibitor that also appears under drugs increasing levodopa efficacy is:",
  ["Entacapone", "Tolcapone", "Opicapone", "Rasagiline"],
  "Entacapone is listed both as a COMT inhibitor and as a drug increasing levodopa efficacy by blocking first pass metabolism.")
q(148, "Which drug class is common to both the on-off phenomenon indication and hepatotoxicity?",
  ["COMT inhibitors", "MAO-B inhibitors",
   "Dopamine agonists", "Anti-beta amyloid antibodies"],
  "COMT inhibitors are the DOC for on-off phenomena, and tolcapone among them is hepatotoxic.")
q(148, "A patient develops abnormal liver function tests on tolcapone. The best alternative COMT inhibitor is:",
  ["Entacapone or opicapone", "Selegiline", "Safinamide", "Amantadine"],
  "Entacapone and opicapone are the COMT inhibitors listed without the hepatotoxicity note.")

unit("Amantadine",
     "Amantadine has a dual mechanism: it is anticholinergic and blocks NMDA receptors, and it augments dopamine. It is the drug of choice for levodopa induced dyskinesia and can be used as initial treatment for Parkinson's disease. Its side effects are ankle oedema and livedo reticularis, a purple pigmentation. The note reminds that purple toe syndrome from warfarin involves only the foot and that amlodipine causes ankle oedema.")
q(148, "The two mechanisms of amantadine given here are anticholinergic action and:",
  ["NMDA receptor blockade", "MAO-B inhibition",
   "COMT inhibition", "Dopamine reuptake inhibition"],
  "Amantadine is described as anticholinergic and an NMDA blocker.")
q(148, "Besides blocking NMDA receptors amantadine:",
  ["Augments dopamine", "Depletes dopamine",
   "Blocks dopamine receptors", "Blocks dopa decarboxylase"],
  "The note states that amantadine augments dopamine.")
q(148, "Amantadine is the drug of choice for:",
  ["Levodopa induced dyskinesia", "On-off phenomena",
   "Restless leg syndrome", "Muscle spasticity"],
  "It is the DOC for levodopa induced dyskinesia.")
q(148, "Amantadine is also used as:",
  ["Initial treatment for Parkinson's disease",
   "Rescue therapy", "Only in end stage disease",
   "Only in patients above 65 years"],
  "The second use listed is initial treatment for Parkinson's disease.")
q(148, "The oedema producing side effect of amantadine is:",
  ["Ankle oedema", "Facial oedema", "Pulmonary oedema", "Periorbital oedema"],
  "Ankle oedema is the first side effect listed.")
q(148, "Livedo reticularis due to amantadine is described as:",
  ["Purple pigmentation", "Brown pigmentation",
   "Yellow discolouration", "Blue discolouration"],
  "Livedo reticularis is explained in brackets as purple pigmentation.")
q(148, "The note about purple toe syndrome concerns:",
  ["Warfarin, in which only the foot is involved",
   "Amantadine, in which only the foot is involved",
   "Amlodipine, which causes livedo reticularis",
   "Apomorphine, which causes purple pigmentation"],
  "The note attributes purple toe syndrome to warfarin, with only the foot involved.")
q(148, "The drug noted in the same context as causing ankle oedema is:",
  ["Amlodipine", "Warfarin", "Apomorphine", "Selegiline"],
  "Amlodipine is noted as causing ankle oedema.")
q(148, "A patient on levodopa develops dyskinesias. The drug of choice to control them is:",
  ["Amantadine", "Trihexyphenidyl", "Propranolol", "Baclofen"],
  "Amantadine is the DOC for levodopa induced dyskinesia.")
q(148, "Which statement about amantadine is correct?",
  ["It augments dopamine, blocks NMDA receptors and causes ankle oedema and livedo reticularis",
   "It blocks MAO-B and causes purple toe syndrome",
   "It is a COMT inhibitor used for on-off phenomena",
   "It is the rescue therapy given subcutaneously"],
  "The page gives its dopamine augmenting and NMDA blocking actions with ankle oedema and livedo reticularis as side effects.")

unit("On-Off Phenomena",
     "The on-off phenomenon is a complication seen with levodopa, and the page relates it to deficiency that becomes apparent as the disease progresses. It is the indication for COMT inhibitors, for the reversible MAO-B inhibitor safinamide and for apomorphine as rescue therapy.")
q(148, "The on-off phenomenon is seen with:",
  ["Levodopa", "Baclofen", "Apomorphine as initial therapy",
   "Anti-beta amyloid antibodies"],
  "The note states the on-off phenomenon is seen with levodopa.")
q(148, "The on-off phenomenon is related to deficiency developing:",
  ["As the disease progresses", "At the start of treatment",
   "Only after stopping levodopa", "Only in young patients"],
  "The note adds that deficiency appears as the disease progresses.")
q(148, "The drugs of choice for the on-off phenomenon are:",
  ["COMT inhibitors", "Dopamine agonists",
   "Anticholinergics", "Nootropics"],
  "COMT inhibitors are labelled DOC for on-off phenomena.")
q(148, "The reversible MAO-B inhibitor used for the on-off phenomenon is:",
  ["Safinamide", "Selegiline", "Rasagiline", "Tolcapone"],
  "Safinamide is the reversible MAO-B inhibitor used for on-off phenomena.")
q(148, "The rescue therapy for the on-off phenomenon is:",
  ["Apomorphine", "Amantadine", "Entacapone", "Selegiline"],
  "Apomorphine is the rescue therapy for the on-off phenomenon.")

unit("Protocol for Treatment of Parkinson's Disease",
     "The management table gives a sequence: entacapone is the drug of choice, with a dopamine agonist or an MAO-B inhibitor as alternatives when there is no response, and apomorphine as rescue therapy. The treatment protocol begins with the effect of symptoms on daily life. If the effect is minimal, no drug is prescribed unless the patient requests one, in which case an MAO-B inhibitor such as selegiline is the drug of choice and amantadine the alternative. If the effect is significant, patients below 65 years receive a dopamine agonist such as pramipexole while patients above 65 years receive levodopa.")
q(149, "The management table at the top of the page begins with the drug of choice:",
  ["Entacapone", "Selegiline", "Pramipexole", "Apomorphine"],
  "Entacapone is placed under DOC in the management row.")
q(149, "When there is no response, the drugs listed as alternatives are:",
  ["A dopamine agonist and an MAO-B inhibitor",
   "Levodopa and carbidopa", "Amantadine and apomorphine",
   "Baclofen and tizanidine"],
  "The alternatives column lists a dopamine agonist and an MAO-B inhibitor.")
q(149, "The rescue therapy in the management algorithm is:",
  ["Apomorphine", "Amantadine", "Entacapone", "Rotigotine"],
  "Apomorphine is placed under rescue therapy.")
q(149, "The treatment protocol starts by assessing:",
  ["The effect of symptoms on daily life", "The age of the patient",
   "The dopamine level in blood", "The presence of tremors"],
  "The first decision box is the effect of symptoms on daily life.")
q(149, "When the effect of symptoms on daily life is minimal, the protocol advises:",
  ["No drug is prescribed", "Immediate levodopa",
   "Immediate dopamine agonist", "Immediate apomorphine"],
  "The minimal branch leads to no drug being prescribed.")
q(149, "If a drug is to be given to a patient with minimal symptoms, it is given:",
  ["On patient request", "Compulsorily", "Only after admission",
   "Only after MRI confirmation"],
  "The bracket notes that the drug is given on patient request.")
q(149, "The drug of choice for a patient with minimal symptoms who requests treatment is:",
  ["An MAO-B inhibitor such as selegiline",
   "Levodopa", "A dopamine agonist", "Apomorphine"],
  "The DOC in this branch is an MAO-B inhibitor, selegiline.")
q(149, "The alternative to an MAO-B inhibitor in minimal disease is:",
  ["Amantadine", "Apomorphine", "Entacapone", "Ropinirole"],
  "Amantadine is listed as the alternative.")
q(149, "When the effect of symptoms on daily life is significant, the next branch is based on:",
  ["Age, below or above 65 years", "Sex of the patient",
   "Presence of tremors", "Response to apomorphine"],
  "The significant branch splits at 65 years of age.")
q(149, "A patient aged 50 years with significant limitation of daily activities should receive:",
  ["A dopamine agonist such as pramipexole", "Levodopa",
   "Apomorphine", "No drug"],
  "Below 65 years the drug listed is a dopamine agonist, pramipexole.")
q(149, "A patient aged 72 years with significant limitation of daily activities should receive:",
  ["Levodopa", "A dopamine agonist", "Selegiline", "Amantadine"],
  "Above 65 years the drug listed is levodopa.")
q(149, "Which statement summarises the protocol correctly?",
  ["Minimal effect needs no drug or an MAO-B inhibitor, significant effect needs a dopamine agonist below 65 years and levodopa above 65 years",
   "All patients should receive levodopa regardless of age",
   "All patients should receive a dopamine agonist regardless of age",
   "Apomorphine is the initial drug in every patient"],
  "The protocol branches on the effect on daily life and then on age at 65 years.")
finish()
