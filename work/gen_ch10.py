# -*- coding: utf-8 -*-
import json
Q = []
def q(sec, page, text, opts, ans, exp):
    Q.append((sec, page, text, opts, ans, exp))

S1 = "Adverse Drug Reaction (ADR)"
q(S1, 29, "An adverse drug reaction (ADR) is defined in the book as:",
  ["An appreciably harmful reaction to a drug that is used for treatment or prophylaxis",
   "Any unwanted effect of a drug taken in overdose",
   "A harmful effect seen only with newer drugs",
   "An allergic reaction to any drug"], 0,
  "The definition reads 'ADR is an appreciably harmful reaction to a drug that is used for treatment or prophylaxis'. (Book p29)")
q(S1, 29, "The management of an ADR consists of:",
  ["Treatment for reaction and prevention of future exposure", "Only stopping the drug",
   "Only reporting to CDSCO", "Increasing the dose to tolerance"], 0,
  "The 'mx of ADR' (management) lists treatment for reaction and prevention of future exposure. (Book p29)")
q(S1, 29, "An idiosyncratic ADR is one that occurs due to:",
  ["Genetic cause", "Dose escalation", "Long duration of therapy",
   "Withdrawal of the drug"], 0,
  "The page states 'Idiosyncratic ADR : D/t genetic cause'. (Book p29)")
q(S1, 29, "The mnemonic for the types of ADR is:",
  ["ABCDEFG", "ABCHIPS", "BADDOC", "ORCHAD"], 0,
  "The types of ADR are remembered by the mnemonic ABCDEFG. (Book p29)")
q(S1, 29, "An 'Augmented' ADR is:",
  ["Dose-dependent (e.g. increased dose of captopril causing hypotension)",
   "Dose-independent (e.g. hypersensitivity)", "Seen after cessation of the drug",
   "Due to therapeutic failure"], 0,
  "Type 1, augmented, is dose-dependent, with the example of increased dose of captopril causing hypotension. (Book p29)")
q(S1, 29, "A 'Bizarre' ADR is:",
  ["Dose-independent (e.g. hypersensitivity to drug)", "Dose-dependent",
   "Dose and duration dependent", "Seen only on withdrawal"], 0,
  "Type 2, bizarre, is dose-independent, the example being hypersensitivity to a drug. (Book p29)")
q(S1, 29, "A 'Chronic' ADR is:",
  ["Dose and duration dependent (e.g. suppression of the hypothalamo-pituitary axis by chronic steroid)",
   "Dose-independent", "Present only after stopping the drug", "A therapeutic failure"], 0,
  "Type 3, chronic, is dose and duration dependent, with suppression of the hypothalamo-pituitary axis by chronic steroid as the example. (Book p29)")
q(S1, 29, "A 'Delayed' ADR is one that:",
  ["Is seen after cessation (e.g. teratogenicity)", "Appears within minutes of the dose",
   "Occurs only on withdrawal of opioids", "Is always dose-dependent"], 0,
  "Type 4, delayed, is an adverse reaction seen after cessation, the example being teratogenicity. (Book p29)")
q(S1, 29, "Withdrawal symptoms on stopping a drug (e.g. opioid or clonidine withdrawal) represent which type of ADR?",
  ["End of use", "Delayed", "Chronic", "Augmented"], 0,
  "Type 5, 'End of use', is described as withdrawal symptoms with the examples of opioid and clonidine withdrawal. (Book p29)")
q(S1, 29, "Use of rifampicin leading to OCP failure is an example of which type of ADR?",
  ["Failure", "Augmented", "Bizarre", "End of use"], 0,
  "Type 6, 'Failure', is illustrated by rifampicin causing OCP failure. (Book p29)")
q(S1, 29, "Which ADR type is illustrated by teratogenicity?",
  ["Delayed", "Chronic", "Bizarre", "Failure"], 0,
  "Teratogenicity is the example given for the delayed type (type 4) of ADR. (Book p29)")
q(S1, 29, "Which ADR type is best described as dose-independent?",
  ["Bizarre", "Augmented", "Chronic", "End of use"], 0,
  "Only the bizarre type is labelled dose-independent; augmented is dose-dependent and chronic is dose and duration dependent. (Book p29)")

S2 = "Drug-Induced Hypersensitivity"
q(S2, 29, "Type I hypersensitivity reaction to a drug manifests as:",
  ["Anaphylaxis", "Hemolysis", "Systemic lupus erythematosus", "Steven-Johnson syndrome"], 0,
  "Under 'Drug-induced hypersensitivity' the type I column reads 'Anaphylaxis'. (Book p29)")
q(S2, 29, "Type II hypersensitivity to a drug manifests as:",
  ["Hemolysis", "Anaphylaxis", "SLE", "Toxic epidermal necrolysis"], 0,
  "The type II column reads 'Hemolysis'. (Book p29)")
q(S2, 29, "Type III hypersensitivity to a drug causes:",
  ["Drug-induced systemic lupus erythematosus (SLE)", "Anaphylaxis",
   "Hemolysis", "Steven-Johnson syndrome"], 0,
  "The type III column reads 'Drug-induced systemic lupus erythematosus (SLE)'. (Book p29)")
q(S2, 29, "Drug-induced SLE is caused by drugs metabolised by:",
  ["Acetylation (e.g. isoniazid, procainamide)", "Glucuronidation (e.g. paracetamol)",
   "Sulphation (e.g. steroids)", "Oxidation by CYP3A4 only"], 0,
  "The example under type III reads 'D/t drugs metabolised by acetylation (isoniazid, Procainamide etc)'. (Book p29)")
q(S2, 29, "Type IV hypersensitivity to a drug manifests as:",
  ["Steven-Johnson syndrome", "Anaphylaxis", "Hemolysis", "SLE"], 0,
  "The type IV column reads 'Steven-Johnson Syndrome'. (Book p29)")
q(S2, 29, "Steven-Johnson syndrome is caused by drugs such as:",
  ["Carbamazepine and lamotrigine", "Isoniazid and procainamide",
   "Penicillin and cephalosporin only", "Digoxin and lithium"], 0,
  "Examples given for the type IV reaction are carbamazepine and lamotrigine. (Book p29)")
q(S2, 29, "Which hypersensitivity type is matched with the correct example?",
  ["Type III - isoniazid-induced SLE", "Type I - hemolysis",
   "Type II - anaphylaxis", "Type IV - hemolysis"], 0,
  "Type I is anaphylaxis, type II hemolysis, type III drug-induced SLE (isoniazid, procainamide) and type IV Steven-Johnson syndrome. (Book p29)")
q(S2, 29, "According to the note on the page, lepra reaction type 1 is a:",
  ["Type IV hypersensitivity", "Type III hypersensitivity",
   "Type II hypersensitivity", "Type I hypersensitivity"], 0,
  "The note maps 'Type 1 : Type IV hypersensitivity' for lepra reactions. (Book p29)")
q(S2, 29, "According to the note, lepra reaction type 2 is a:",
  ["Type III hypersensitivity", "Type IV hypersensitivity",
   "Type I hypersensitivity", "Type II hypersensitivity"], 0,
  "The note maps 'Type 2 : Type III hypersensitivity' for lepra reactions. (Book p29)")

S3 = "Pharmacovigilance"
q(S3, 30, "The aim of pharmacovigilance is:",
  ["To maintain drug safety", "To increase drug sales", "To reduce drug cost",
   "To determine the dose of a drug"], 0,
  "The aim is stated as 'To maintain drug safety'. (Book p30)")
q(S3, 30, "Pharmacovigilance in India is carried out under the:",
  ["Pharmacovigilance Program of India (PvPI)", "Program of Drug Safety of India",
   "Central Drug Testing Programme", "National ADR Registry"], 0,
  "The page states it works 'Under Pharmacovigilance Program of India (PvPI)'. (Book p30)")
q(S3, 30, "The National Co-ordinating Centre (NCC) for pharmacovigilance in India is at:",
  ["Indian Pharmacopoeia Commission, Ghaziabad (UP)", "ICMR, New Delhi",
   "AIIMS, Delhi", "CDSCO, Mumbai"], 0,
  "The NCC is the Indian Pharmacopoeia Commission (Ghaziabad, UP). (Book p30)")
q(S3, 30, "Pharmacovigilance is similar to:",
  ["Phase 4 clinical trials (by pharmaceutical companies)", "Phase 1 trials",
   "Preclinical trials", "Phase 0 microdosing"], 0,
  "The page notes it is 'Similar to Phase 4 clinical trials (by pharmaceutical companies)'. (Book p30)")
q(S3, 30, "VigiFlow is:",
  ["Software for reporting ADR", "A database of pharmacovigilance",
   "A guideline for clinical trials", "An ADR reporting form for patients only"], 0,
  "VigiFlow is described as 'Software for reporting of ADR'. (Book p30)")
q(S3, 30, "VigiFlow is available at:",
  ["Hospitals and medical colleges across the country", "Only at CDSCO",
   "Only at the WHO centre", "Only in private clinics"], 0,
  "It is 'Available at hospitals & medical colleges across country'. (Book p30)")
q(S3, 30, "The information collected in VigiFlow is processed at the:",
  ["NCC, giving a conclusive ADR report", "Uppsala Monitoring Centre directly",
   "WHO head office", "Pharmacy council"], 0,
  "The page notes 'Information processed at NCC → Conclusive ADR report'. (Book p30)")
q(S3, 30, "The conclusive ADR report from the NCC is sent to:",
  ["Central Drugs Standard Control Organisation (CDSCO)", "The WHO directly",
   "Uppsala Monitoring Centre", "IPC Sweden"], 0,
  "The flow shows the conclusive ADR report sent to CDSCO. (Book p30)")
q(S3, 30, "After receiving the report, CDSCO:",
  ["Bans the drug and informs doctors and patients", "Only publishes the data",
   "Informs only the pharmaceutical company", "Files the report without action"], 0,
  "One limb of the CDSCO flow reads 'Bans drug & informs doctors & patients'. (Book p30)")
q(S3, 30, "The international centre for pharmacovigilance is located at:",
  ["Uppsala, Sweden", "Geneva, Switzerland", "New Delhi, India", "Maryland, USA"], 0,
  "CDSCO informs the international pharmacovigilance centre (IPVC)/Uppsala Monitoring Centre (UMC) in Uppsala, Sweden. (Book p30)")
q(S3, 30, "The largest database of pharmacovigilance is:",
  ["Vigibase", "VigiFlow", "VigiAccess", "MedWatch"], 0,
  "The page writes 'Has largest database of pharmacovigilance : Vigibase'. (Book p30)")
q(S3, 30, "Vigibase is used to:",
  ["Inform countries worldwide", "Report ADRs from Indian hospitals",
   "Process data at the NCC", "Ban drugs directly"], 0,
  "An arrow from Vigibase reads 'Informs countries worldwide'. (Book p30)")

S4 = "Therapeutic Drug Monitoring (TDM)"
q(S4, 30, "The principle of therapeutic drug monitoring is that:",
  ["Plasma concentration of the drug correlates well with effect and side-effects",
   "Dose of the drug correlates with effect", "Urinary concentration reflects toxicity",
   "Tissue concentration always equals plasma concentration"], 0,
  "The principle reads 'The plasma concentration of drug has good correlation to effect & side-effects'. (Book p30)")
q(S4, 30, "The first indication for TDM is:",
  ["Clinical effect of the drug is not quantifiable", "Drug has a low therapeutic index",
   "Drugs with variable metabolism", "To check compliance"], 0,
  "Indication 1 is 'Clinical effect of the drug is not quantifiable'. (Book p30)")
q(S4, 30, "Which drugs have quantifiable effects and therefore do not need TDM on that count?",
  ["Oral hypoglycemic drugs and β blockers", "Aminoglycosides and digoxin",
   "Lithium and theophylline", "Anti-epileptics and tacrolimus"], 0,
  "The note under indication 1 reads 'Drug with quantifiable effects : Oral hypoglycemic drugs, β blockers etc'. (Book p30)")
q(S4, 30, "The second indication for TDM is:",
  ["A drug with a low therapeutic index", "A drug whose effect is quantifiable",
   "A drug with no metabolism", "A drug given as a single dose"], 0,
  "Indication 2 is 'Drug with low therapeutic index'. (Book p30)")
q(S4, 30, "Which of the following is listed as a drug with a low therapeutic index requiring TDM?",
  ["Aminoglycosides", "Oral hypoglycemics", "β blockers", "Aspirin"], 0,
  "The list of low therapeutic index drugs includes aminoglycosides, anti-epileptics, tacrolimus, digoxin, anti-psychotics, lithium and theophylline. (Book p30)")
q(S4, 30, "Which two anti-psychotics/anti-epileptics appear in the low therapeutic index list?",
  ["Anti-epileptics and anti-psychotics", "Anti-malarials and anti-gout drugs",
   "Antivirals and antifungals", "Anti-TB drugs and antibiotics"], 0,
  "Both anti-epileptics and anti-psychotics are bulleted in the low therapeutic index list. (Book p30)")
q(S4, 30, "Which immunosuppressant is listed among the drugs needing TDM?",
  ["Tacrolimus", "Cyclosporine only", "Azathioprine", "Methotrexate"], 0,
  "Tacrolimus is listed in the low therapeutic index group for TDM. (Book p30)")
q(S4, 30, "Lithium, digoxin and theophylline are monitored because they:",
  ["Have a low therapeutic index", "Have no measurable plasma level",
   "Are highly protein bound", "Are given intravenously"], 0,
  "All three appear in the low therapeutic index bullet list of indication 2. (Book p30)")
q(S4, 30, "The third indication for TDM is:",
  ["Drugs with variable metabolism (e.g. drugs metabolised by acetylation)",
   "Drugs with zero-order kinetics only", "Drugs given topically", "Drugs with a wide therapeutic index"], 0,
  "Indication 3 reads 'Drugs with variable metabolism (eg: drugs metabolised by acetylation)'. (Book p30)")
q(S4, 30, "TDM is done to check compliance to therapy for which drugs?",
  ["Anti-psychotic drugs", "β blockers", "Oral hypoglycemics", "Antacids"], 0,
  "Indication 4 reads 'To check compliance to therapy (eg: Anti-psychotic drugs)'. (Book p30)")
q(S4, 30, "The fifth indication for TDM is:",
  ["To prevent/limit damage to organ/fetus", "To reduce the cost of therapy",
   "To shorten the duration of therapy", "To determine the route of administration"], 0,
  "Indication 5 is 'To prevent/limit damage to organ/fetus'. (Book p30)")
q(S4, 30, "An aminoglycoside is monitored in a patient with pseudomonas infection and renal failure in order to:",
  ["Prevent/limit damage to the organ", "Check compliance",
   "Determine the loading dose", "Quantify a non-quantifiable effect"], 0,
  "This is the example given under indication 5 - preventing organ damage (nephrotoxicity). (Book p30)")
q(S4, 31, "In a pregnant woman on valproate, folic acid is added in a dose of 400 mcg/day when:",
  ["There is no history of neural tube defect", "There is a history of neural tube defect",
   "The patient is in the third trimester only", "Valproate is stopped"], 0,
  "The flow gives 'without H/o NTD : 400 mcg/d' and 'with H/o NTD : 4000 mcg/d'. (Book p31)")
q(S4, 31, "In a pregnant woman on valproate with a history of neural tube defect, folic acid is given in a dose of:",
  ["4000 mcg/day", "400 mcg/day", "1000 mcg/day", "5 mg/week"], 0,
  "The page writes 'with H/o NTD : 4000 mcg/d'. (Book p31)")
q(S4, 31, "TDM must be determined only after:",
  ["Reaching steady state concentration", "The first dose", "The peak of the first dose",
   "The drug is stopped"], 0,
  "The note states 'TDM must be determined only after reaching steady state concentration'. (Book p31)")
q(S4, 31, "Why is a trough level taken at steady state for TDM?",
  ["Because plasma concentration then correlates reliably with effect and side-effects",
   "Because the drug is fully absorbed only by then", "Because the drug is not bound to protein before that",
   "Because the liver enzymes are fully induced"], 0,
  "TDM rests on the principle that plasma concentration correlates with effect and side-effects, which is meaningful only at steady state. (Book p30-31)")

S5 = "Pharmacogenetics and Pharmacogenomics"
q(S5, 31, "Pharmacogenetics/pharmacogenomics is the study of:",
  ["The effect of genetics or genome on the action of drugs", "The effect of drugs on the genome only",
   "The effect of diet on drug action", "The effect of age on drug action"], 0,
  "The definition on the page is 'The effect of genetics or genome on action of drugs'. (Book p31)")
q(S5, 31, "'Genetics', in this context, is based on:",
  ["DNA polymorphism", "Chromosomal changes", "Protein structure only", "Enzyme induction"], 0,
  "The page writes '\"Genetics\" : Based on DNA polymorphism'. (Book p31)")
q(S5, 31, "'Genomics' is based on:",
  ["Chromosomal changes", "DNA polymorphism", "Single nucleotide changes only",
   "Plasma protein binding"], 0,
  "The page writes '\"Genomics\" : Based on chromosomal changes'. (Book p31)")
q(S5, 31, "Genes code for which two things that determine drug action?",
  ["Enzymes and receptors", "Albumin and globulin", "Ion channels and transporters only",
   "Hormones and vitamins"], 0,
  "The flow chart shows 'genes code for Enzymes / Receptors'. (Book p31)")
q(S5, 31, "According to the flow chart, the response to a drug depends on:",
  ["The strength of the genes", "The route of administration", "The cost of the drug",
   "The patient's weight alone"], 0,
  "From genes coding enzymes/receptors the flow proceeds 'based on strength of genes'. (Book p31)")
q(S5, 31, "Which of these is the extreme end of the spectrum of genetic drug response?",
  ["Toxicity", "Strong response to drug", "Normal response to drug",
   "Weak response to drug"], 0,
  "The spectrum listed is toxicity, strong response, normal response, weak response and failure of drug, with toxicity at the extreme. (Book p31)")
q(S5, 31, "The five outcomes of genetic variation in drug response listed are:",
  ["Toxicity, strong response, normal response, weak response and failure of drug",
   "Toxicity, allergy, tolerance, resistance and failure",
   "Strong, weak, absent, delayed and idiosyncratic response",
   "Toxicity, tachyphylaxis, tolerance, dependence and withdrawal"], 0,
  "The bracket in the flow chart lists exactly these five outcomes. (Book p31)")
q(S5, 31, "Fast acetylators are individuals with the:",
  ["NAT1 gene", "NAT2 gene", "CYP2D6 gene", "VKORC1 gene"], 0,
  "The page states 'NAT1 gene : Fast acetylators'. (Book p31)")
q(S5, 31, "Slow acetylators are individuals with the:",
  ["NAT2 gene", "NAT1 gene", "NAT3 gene", "TPMT gene"], 0,
  "The page states 'NAT2 gene : Slow acetylators'. (Book p31)")
q(S5, 31, "Isoniazid (INH) is converted by acetylation to:",
  ["INHA", "Acetyl-INH hydrazine only", "INH-N oxide", "Rifampicin"], 0,
  "The diagram shows 'Isoniazid (INH) --Acetylation--> INHA'. (Book p31)")
q(S5, 31, "According to the diagram, high levels of INH in slow acetylators cause:",
  ["Hepatotoxicity", "Neuropathy", "Nephrotoxicity", "Ototoxicity"], 0,
  "The left limb reads INH → high levels → hepatotoxicity (slow acetylators). (Book p31)")
q(S5, 31, "According to the diagram, high levels of INHA in fast acetylators cause:",
  ["Neuropathy", "Hepatotoxicity", "Haemolysis", "Agranulocytosis"], 0,
  "The right limb reads INHA → high levels → neuropathy (fast acetylators). (Book p31)")
q(S5, 31, "Which pairing of acetylator status and isoniazid toxicity is given on the page?",
  ["Slow acetylators - hepatotoxicity; fast acetylators - neuropathy",
   "Slow acetylators - neuropathy; fast acetylators - hepatotoxicity",
   "Both groups get hepatotoxicity", "Both groups get neuropathy"], 0,
  "The page links high INH (slow acetylators) to hepatotoxicity and high INHA (fast acetylators) to neuropathy. (Book p31)")

S6 = "Malignant Hyperthermia"
q(S6, 31, "Malignant hyperthermia occurs due to polymorphism of the:",
  ["RyR (ryanodine receptor) gene", "NAT2 gene", "CYP2D6 gene", "TPMT gene"], 0,
  "The page states 'malignant hyperthermia : D/t RyR (Ryanodine receptor) gene polymorphism'. (Book p31)")
q(S6, 31, "Which drugs are listed as triggering malignant hyperthermia?",
  ["Succinylcholine, lidocaine and halothane", "Isoniazid, rifampicin and pyrazinamide",
   "Clopidogrel, warfarin and tamoxifen", "Digoxin, lithium and theophylline"], 0,
  "The boxed list of triggering agents contains succinylcholine (SCh), lidocaine and halothane. (Book p31)")
q(S6, 31, "The drug used for treatment of malignant hyperthermia is:",
  ["Dantrolene", "Succinylcholine", "Halothane", "Lidocaine"], 0,
  "The diagram shows dantrolene (used for treatment) blocking the step where these drugs act. (Book p31)")
q(S6, 31, "In malignant hyperthermia, the gene polymorphism causes:",
  ["Increased RyR stimulation due to increased expression of the gene",
   "Decreased RyR expression", "Blockade of the ryanodine receptor",
   "Loss of the sarcoplasmic reticulum"], 0,
  "The step reads '↑ RyR stimulation (d/t ↑ expression of gene)'. (Book p31)")
q(S6, 31, "The rise in intracellular calcium in malignant hyperthermia comes from:",
  ["Release from the sarcoplasmic reticulum", "Influx through L-type calcium channels only",
   "The mitochondria", "Extracellular calcium binding to troponin"], 0,
  "The cascade reads '↑ Ca2+ release from sarcoplasmic reticulum'. (Book p31)")
q(S6, 31, "The sequence after the calcium release in malignant hyperthermia is:",
  ["↑ ATP used for Ca2+ reuptake → ↑ heat release", "↓ ATP use → hypothermia",
   "↑ cAMP → vasodilation", "↓ Ca2+ reuptake → hypocalcaemia"], 0,
  "The final two steps are '↑ ATP used for Ca2+ reuptake' and then '↑ Heat release'. (Book p31)")
q(S6, 31, "Excess heat in malignant hyperthermia is generated because:",
  ["ATP is consumed for calcium reuptake", "Mitochondria are destroyed",
   "The hypothalamic set point rises", "Shivering is induced by halothane"], 0,
  "The book explains the heat release as a consequence of ATP used for Ca2+ reuptake. (Book p31)")

S7 = "G-6-PD Deficiency and Haemolysis"
q(S7, 32, "G-6-PD deficiency leads to:",
  ["Hemolysis via the HMP shunt", "Hepatotoxicity via CYP2E1",
   "Neuropathy via INHA", "Agranulocytosis via myeloperoxidase"], 0,
  "The heading reads 'G-6-PD deficiency : Leads to hemolysis (via HMP shunt)'. (Book p32)")
q(S7, 32, "Which antimalarial drugs can cause haemolysis in G-6-PD deficiency?",
  ["Primaquine (and tafenoquine)", "Chloroquine", "Artemether", "Sulfadoxine only"], 0,
  "Primaquine is braced as an anti-malarial in the haemolysis list, and tafenoquine is also listed. (Book p32)")
q(S7, 32, "Which oral antidiabetic drugs are listed as causing haemolysis in G-6-PD deficiency?",
  ["Glyburide and glibenclamide", "Metformin and sitagliptin", "Insulin and glargine",
   "Pioglitazone and rosiglitazone"], 0,
  "Glyburide and glibenclamide head the list of drugs causing haemolysis in G-6-PD deficiency. (Book p32)")
q(S7, 32, "Dapsone and dabrafenib are listed under:",
  ["Drugs causing haemolysis in G-6-PD deficiency", "Drugs causing drug-induced SLE",
   "Drugs causing Steven-Johnson syndrome", "Drugs needing TDM"], 0,
  "Both are in the bullet list of agents precipitating haemolysis in G-6-PD deficiency. (Book p32)")
q(S7, 32, "Menadione (vitamin K) and methylene blue can precipitate haemolysis in:",
  ["G-6-PD deficiency", "Slow acetylators", "CYP2D6 poor metabolisers",
   "Thiopurine methyltransferase deficiency"], 0,
  "Both menadione (vit K) and methylene blue appear in the G-6-PD haemolysis list. (Book p32)")
q(S7, 32, "Which anti-gout medications are named as causing haemolysis in G-6-PD deficiency?",
  ["Pegloticase and rasburicase", "Allopurinol and febuxostat",
   "Colchicine and probenecid", "Benzbromarone and sulfinpyrazone"], 0,
  "The list gives 'Anti-gout medication (eg : Pegloticase, Rasburicase)'. (Book p32)")
q(S7, 32, "Nalidixic acid and nitrofurantoin are listed because they:",
  ["Cause haemolysis in G-6-PD deficiency", "Cause tardive dyskinesia",
   "Cause pulmonary fibrosis", "Need TDM"], 0,
  "Both appear in the third column of drugs causing haemolysis in G-6-PD deficiency. (Book p32)")
q(S7, 32, "Sulfonamides appear in which list on this page?",
  ["Drugs causing haemolysis in G-6-PD deficiency", "Drugs causing SLE",
   "Drugs causing malignant hyperthermia", "Drugs metabolised by acetylation"], 0,
  "Sulfonamides are bulleted in the G-6-PD haemolysis list. (Book p32)")

S8 = "CYP450 Enzyme Polymorphism"
q(S8, 32, "Low action of CYP2C19 leads to:",
  ["↓ Activation of clopidogrel and development of MI despite medication",
   "↑ Activation of clopidogrel and bleeding", "Variable effect of warfarin",
   "Prolonged apnoea with succinylcholine"], 0,
  "The page writes 'Low action of CYP2C19 → ↓ Activation of Clopidogrel → Development of MI despite medication'. (Book p32)")
q(S8, 32, "Polymorphism of which two genes leads to a variable effect of warfarin?",
  ["CYP2C9 and VKORC1", "CYP2D6 and TPMT", "CYP2C19 and NAT2", "CYP3A4 and MDR1"], 0,
  "The page states 'Polymorphism of CYP2C9 + VKORC1 → variable effect of warfarin'. (Book p32)")
q(S8, 32, "Polymorphism of CYP2D6 causes:",
  ["↓ Effect of the drug", "↑ effect of the drug", "No change in effect",
   "Increased renal excretion"], 0,
  "The page writes 'Polymorphism of CYP2D6 → ↓ Effect'. (Book p32)")
q(S8, 32, "With CYP2D6 polymorphism, reduced metabolism of psychiatric drugs leads to:",
  ["Toxicity", "Therapeutic failure", "Haemolysis", "Prolonged apnoea"], 0,
  "The left limb reads '↓ metabolism of psychiatric drugs → Toxicity'. (Book p32)")
q(S8, 32, "With CYP2D6 polymorphism, reduced activation of tamoxifen leads to:",
  ["↓ Levels of endoxifen and failure of the drug", "Toxicity from endoxifen excess",
   "Increased endoxifen and bleeding", "Reduced hepatotoxicity"], 0,
  "The right limb reads '↓ Activation of tamoxifen → ↓ Levels of endoxifen → Failure of drug'. (Book p32)")
q(S8, 32, "Tamoxifen requires CYP2D6 to be converted to:",
  ["Endoxifen", "INHA", "4-hydroxycyclophosphamide", "Norethisterone"], 0,
  "The flow shows activation of tamoxifen producing endoxifen. (Book p32)")
q(S8, 32, "Which polymorphism explains development of MI despite clopidogrel therapy?",
  ["CYP2C19", "CYP2D6", "CYP2C9", "VKORC1"], 0,
  "Low action of CYP2C19 reduces clopidogrel activation, so MI can develop despite medication. (Book p32)")
q(S8, 32, "CYP2D6 polymorphism causing reduced metabolism of psychiatric drugs results in toxicity because:",
  ["The drug accumulates", "The active metabolite is not formed",
   "The drug is excreted too fast", "The receptor is upregulated"], 0,
  "Reduced metabolism means accumulation of the psychiatric drug, hence toxicity. (Book p32)")
q(S8, 32, "In CYP2D6 poor metabolisers, tamoxifen therapy is likely to fail because:",
  ["The prodrug is not activated to endoxifen", "The drug is not absorbed",
   "The drug is over-activated", "The receptor is mutated"], 0,
  "The book's flow shows that reduced activation lowers endoxifen levels and leads to failure of the drug. (Book p32)")

S9 = "Other Pharmacogenetic Examples"
q(S9, 32, "Succinylcholine with atypical pseudocholinesterase causes:",
  ["Prolonged apnoea", "Malignant hyperthermia", "Haemolysis", "Toxicity from 6-mercaptopurine"], 0,
  "The line reads 'Succinylcholine --Atypical pseudocholinesterase--> Prolonged apnea'. (Book p32)")
q(S9, 32, "The enzyme abnormality responsible for prolonged apnoea with succinylcholine is:",
  ["Atypical pseudocholinesterase", "Thiopurine methyltransferase",
   "CYP2D6", "N-acetyltransferase"], 0,
  "The arrow between succinylcholine and prolonged apnoea is labelled 'Atypical pseudocholinesterase'. (Book p32)")
q(S9, 32, "A reduced effect of thiopurine methyl-transferase causes decreased metabolism of:",
  ["6-mercaptopurine and azathioprine", "Isoniazid and procainamide",
   "Tamoxifen and clopidogrel", "Warfarin and phenytoin"], 0,
  "The boxed substrates of thiopurine methyltransferase are 6-mercaptopurine and azathioprine. (Book p32)")
q(S9, 32, "Deficiency of thiopurine methyl-transferase results in:",
  ["↑ Toxicity of 6-mercaptopurine and azathioprine", "Treatment failure of azathioprine",
   "Prolonged apnoea", "Warfarin resistance"], 0,
  "The flow ends '↑ Toxicity' after the reduced metabolism of 6-mercaptopurine and azathioprine. (Book p32)")
q(S9, 32, "Which of the following is an example of a pharmacogenetic cause of drug toxicity from a parent drug rather than a metabolite?",
  ["Reduced metabolism of 6-mercaptopurine by TPMT", "High INHA in fast acetylators",
   "High endoxifen levels with CYP2D6", "Reduced RyR expression"], 0,
  "Reduced TPMT activity lets the parent thiopurines accumulate and cause toxicity. (Book p32)")

UNITS = [
 (1, "Adverse Drug Reaction (ADR)", [1,12],
  "An ADR is an appreciably harmful reaction to a drug used for treatment or prophylaxis; management is treatment of the reaction plus prevention of future exposure, and an idiosyncratic ADR is genetic in origin. The types are remembered by ABCDEFG - Augmented (dose-dependent, e.g. captopril hypotension), Bizarre (dose-independent, e.g. hypersensitivity), Chronic (dose and duration dependent, e.g. steroid-induced hypothalamo-pituitary suppression), Delayed (seen after cessation, e.g. teratogenicity), End of use (withdrawal, e.g. opioid/clonidine) and Failure (e.g. rifampicin causing OCP failure)."),
 (2, "Drug-Induced Hypersensitivity", [13,21],
  "Four hypersensitivity types are shown: type I anaphylaxis, type II hemolysis, type III drug-induced SLE (from drugs metabolised by acetylation such as isoniazid and procainamide) and type IV Steven-Johnson syndrome (carbamazepine, lamotrigine). The closing note maps lepra reactions: type 1 lepra reaction is type IV and type 2 is type III hypersensitivity."),
 (3, "Pharmacovigilance", [22,33],
  "Pharmacovigilance aims to maintain drug safety and runs under the Pharmacovigilance Program of India (PvPI), co-ordinated by the NCC at the Indian Pharmacopoeia Commission, Ghaziabad (UP); it is similar to phase 4 clinical trials by pharmaceutical companies. VigiFlow is the software used at hospitals and medical colleges to report ADRs; the NCC processes them into a conclusive ADR report, sent to CDSCO, which may ban the drug and inform doctors and patients and also informs the international pharmacovigilance centre - the Uppsala Monitoring Centre (UMC) in Uppsala, Sweden - whose Vigibase, the largest pharmacovigilance database, informs countries worldwide."),
 (4, "Therapeutic Drug Monitoring (TDM)", [34,49],
  "TDM rests on the principle that plasma concentration of a drug correlates well with its effect and side-effects. Indications are: non-quantifiable clinical effect (drugs with quantifiable effects like oral hypoglycemics and β blockers are excluded), low therapeutic index (aminoglycosides, anti-epileptics, tacrolimus, digoxin, anti-psychotics, lithium, theophylline), variable metabolism such as acetylation, checking compliance (anti-psychotics) and preventing damage to organ or fetus - e.g. an aminoglycoside for pseudomonas in renal failure, or valproate in pregnancy with folic acid 400 mcg/day without a history of NTD and 4000 mcg/day with it. TDM is determined only after steady state concentration is reached."),
 (5, "Pharmacogenetics and Pharmacogenomics", [50,62],
  "Pharmacogenetics/pharmacogenomics studies the effect of genetics or genome on drug action - genetics being based on DNA polymorphism and genomics on chromosomal changes. Genes code for enzymes and receptors, and the strength of these genes decides whether the response is toxic, strong, normal, weak or a failure. The acetylation example shows NAT1 individuals are fast acetylators and NAT2 individuals slow acetylators: high INH in slow acetylators causes hepatotoxicity while high INHA in fast acetylators causes neuropathy."),
 (6, "Malignant Hyperthermia", [63,69],
  "Malignant hyperthermia is due to RyR (ryanodine receptor) gene polymorphism and is triggered by succinylcholine, lidocaine and halothane, with dantrolene used for treatment. Increased expression of the gene raises RyR stimulation, releasing Ca2+ from the sarcoplasmic reticulum; ATP is then used for calcium reuptake and heat is released - the hyperthermia."),
 (7, "G-6-PD Deficiency and Haemolysis", [70,77],
  "G-6-PD deficiency leads to hemolysis through the HMP shunt. The drugs to remember are glyburide, glibenclamide, sulfonamides, primaquine and tafenoquine (anti-malarials), dapsone, dabrafenib, menadione (vitamin K), methylene blue, anti-gout medication (pegloticase, rasburicase), nalidixic acid and nitrofurantoin."),
 (8, "CYP450 Enzyme Polymorphism", [78,86],
  "CYP polymorphism explains several therapeutic failures: low action of CYP2C19 reduces activation of clopidogrel so MI develops despite medication; CYP2C9 with VKORC1 polymorphism gives a variable warfarin effect; and CYP2D6 polymorphism reduces drug effect - the reduced metabolism of psychiatric drugs causes toxicity, while reduced activation of tamoxifen lowers endoxifen levels and the drug fails."),
 (9, "Other Pharmacogenetic Examples", [87,91],
  "Two further examples complete the page. Succinylcholine given with atypical pseudocholinesterase causes prolonged apnoea. A reduced effect of thiopurine methyl-transferase decreases metabolism of 6-mercaptopurine and azathioprine, leading to increased toxicity."),
]

byid = {}
for i, (sec, page, text, opts, ans, exp) in enumerate(Q, 1):
    byid[i] = {"id": f"PHARM-C10-{i:03d}", "sec": sec, "page": page, "q": text,
               "opts": opts, "ans": ans, "exp": exp}
questions = [byid[i] for i in sorted(byid)]
units = []
for n, title, (a, b), guide in UNITS:
    for i in range(a, b + 1):
        byid[i]["sec"] = title
    units.append({"id": f"PHARM-U10-{n}", "ch": 10, "n": n, "title": title,
                  "sec": f"{title} · p{byid[a]['page']}",
                  "qs": [f"PHARM-C10-{i:03d}" for i in range(a, b + 1)],
                  "guide": guide})
json.dump({"questions": questions, "units": units},
          open("data/ch10.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("questions:", len(questions), "units:", len(units))
for u in units:
    print(" ", u["id"], u["title"], len(u["qs"]), u["sec"])
