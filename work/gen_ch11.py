# -*- coding: utf-8 -*-
import json
Q = []
def q(sec, page, text, opts, ans, exp):
    Q.append((sec, page, text, opts, ans, exp))

S1 = "Definitions"
q(S1, 33, "Pharmacology is best defined as the study of:",
  ["Structure, effect (MOA), side effects and contraindications of drugs",
   "Drugs derived from plants", "Compounding and dispensing of drugs",
   "Use of drugs in cancer and infection"], 0,
  "The definition on the page: 'Pharmacology : Study of structure, effect (MOA), side effects, contraindication of drugs'. (Book p33)")
q(S1, 33, "Pharmacotherapeutics is the study of:",
  ["A drug in service of disease (dose, route and response)",
   "Drugs derived from plants", "The structure of a drug molecule",
   "Compounding and dispensing of drugs"], 0,
  "The page defines pharmacotherapeutics as 'Study of a drug in service of disease (dose, route & response)'. (Book p33)")
q(S1, 33, "Pharmacognosy is the study of:",
  ["Drugs derived from plants", "Drugs derived from animals",
   "Synthetic drug design", "Drug dispensing"], 0,
  "The definition reads 'Pharmacognosy : Study of drugs derived from plants'. (Book p33)")
q(S1, 33, "Chemotherapy is the use of drugs in the treatment of:",
  ["Cancer and infection", "Hypertension and diabetes", "Pain and inflammation",
   "Psychiatric disorders"], 0,
  "The page writes 'Chemotherapy : use of drugs in treatment of cancer and infection'. (Book p33)")
q(S1, 33, "Pharmacy is the branch that deals with:",
  ["Compounding and dispensing of drugs", "The study of plant drugs",
   "The mechanism of action of drugs", "Drug regulatory affairs"], 0,
  "Pharmacy is defined as the branch dealing with compounding and dispensing of drugs. (Book p33)")
q(S1, 33, "The term 'compounding' in pharmacy is bracketed on the page with:",
  ["Mixing of drugs (obsolete)", "Dispensing of drugs", "Storage of drugs", "Barcoding"], 0,
  "A bracket under 'compounding' explains it as 'mixing of drugs (obsolete)'. (Book p33)")
q(S1, 33, "Barcoding in pharmacy is described as:",
  ["Technology for dispensing the right drug to avoid errors", "A method of mixing drugs",
   "A technique of drug storage", "A method of drug pricing"], 0,
  "The page notes 'Barcoding - Technology for dispensing right drug to avoid errors'. (Book p33)")
q(S1, 33, "A drug is defined as a chemical with:",
  ["A known structure that alters the pathophysiology for therapeutic gain",
   "An unknown structure that alters physiology", "Any natural product used in disease",
   "A chemical that only prevents disease"], 0,
  "The definition reads 'Drug : Chemical with a known structure that alters the pathophysiology for therapeutic gain'. (Book p33)")

S2 = "Drug Sources"
q(S2, 33, "The four sources of drugs listed are:",
  ["Natural, semisynthetic, synthetic and genetic engineering", "Plant, animal, mineral and marine",
   "Natural, herbal, chemical and biological", "Plant, microbial, synthetic and recombinant"], 0,
  "The drug sources flow chart branches into natural, semisynthetic (modified natural chemical), synthetic (rational drug designing) and genetic engineering. (Book p33)")
q(S2, 33, "Which plant sources of drugs are listed?",
  ["Quinine, digoxin and morphine (poppy plant)", "Quinine, insulin and heparin",
   "Digoxin, atropine and reserpine", "Morphine, codeine and papaverine"], 0,
  "The plants branch lists quinine, digoxin and morphine (poppy plant). (Book p33)")
q(S2, 33, "Which animal peptides are given as drug sources?",
  ["Insulin and heparin (porcine mucosa)", "Insulin and glucagon",
   "Heparin and streptokinase", "Vasopressin and oxytocin"], 0,
  "The animal peptides listed are insulin and heparin (porcine mucosa). (Book p33)")
q(S2, 33, "Antibiotics are obtained from:",
  ["Microorganisms", "Plants", "Animals", "Genetic engineering"], 0,
  "Under natural sources the third branch is 'microorganisms : Antibiotics'. (Book p33)")
q(S2, 33, "Apomorphine, a dopamine agonist used in Parkinson's disease, is an example of a:",
  ["Semisynthetic (modified natural chemical)", "Synthetic drug", "Natural plant drug",
   "Genetically engineered product"], 0,
  "Apomorphine (Da agonist used in parkinsonism) is the example under semisynthetic - a modified natural chemical. (Book p33)")
q(S2, 33, "Synthetic drugs are designed by:",
  ["Rational drug designing", "Random screening of plants", "Gene transfer",
   "Fermentation of microbes"], 0,
  "The synthetic branch reads 'Rational drug designing'. (Book p33)")
q(S2, 33, "In rational drug designing, the drug is designed:",
  ["Complementary to a receptor, binding and inhibiting, resulting in modification of the disease",
   "To mimic a plant alkaloid exactly", "By introducing a gene into a cell line",
   "By extracting the active principle from animal tissue"], 0,
  "The page describes the synthetic group as designed complementary to a receptor, binding and inhibiting, resulting in modification of the disease. (Book p33)")
q(S2, 33, "Genetic engineering is defined in the drug sources chart as:",
  ["The process of introducing a gene in a cell line to obtain a product",
   "The process of modifying a natural chemical", "The process of chemical synthesis",
   "Extraction of drugs from plants"], 0,
  "The chart reads 'Genetic Engineering : process of introducing a gene in a cell line in outcome of a product'. (Book p33)")
q(S2, 33, "The example given for a genetically engineered drug product is:",
  ["Human insulin (gene) giving regular insulin (peptide)", "Porcine insulin",
   "Apomorphine", "Heparin from porcine mucosa"], 0,
  "The chart gives human insulin (gene) → regular insulin (peptide). (Book p33)")

S3 = "Drug Nomenclature"
q(S3, 34, "The three types of drug nomenclature are:",
  ["Chemical, generic/non proprietary and branded/proprietary",
   "Chemical, biological and trade", "Official, generic and patented",
   "Code, generic and brand"], 0,
  "The nomenclature flow chart branches into chemical, generic/non proprietary and branded/proprietary names. (Book p34)")
q(S3, 34, "A chemical name of a drug is:",
  ["A long name based on structure", "An abbreviated name", "The manufacturer's name",
   "The name in the pharmacopoeia"], 0,
  "The chemical branch reads 'Long names based on structure'. (Book p34)")
q(S3, 34, "Generic/non proprietary names are:",
  ["Abbreviated names, e.g. propranolol", "Long names based on structure",
   "Names given by the manufacturer", "Trade names"], 0,
  "The generic/non proprietary branch lists abbreviated names with propranolol as the example. (Book p34)")
q(S3, 34, "The suffix '-lol' indicates:",
  ["β blockers", "ACE inhibitors", "Proton pump inhibitors", "Calcium channel blockers"], 0,
  "The suffix list reads 'lol → β blockers'. (Book p34)")
q(S3, 34, "The suffix '-pril' indicates:",
  ["ACE inhibitors", "β blockers", "Proton pump inhibitors", "Statins"], 0,
  "The suffix list reads 'Pril → ACE inhibitor'. (Book p34)")
q(S3, 34, "The suffix '-prazole' indicates:",
  ["Proton pump inhibitors", "ACE inhibitors", "β blockers", "Antifungals"], 0,
  "The suffix list reads 'Prazole → PPI'. (Book p34)")
q(S3, 34, "Branded/proprietary names are:",
  ["Drug names given by the manufacturer", "Abbreviated generic names",
   "Names based on chemical structure", "Official pharmacopoeial names"], 0,
  "The branded/proprietary branch reads 'Drug names by the manufacturer'. (Book p34)")
q(S3, 34, "A drug compendium is:",
  ["A book containing comprehensive and organised information about drugs",
   "A list of drug prices", "A formulary of hospital drugs only",
   "A catalogue of clinical trials"], 0,
  "The definition given is 'Book containing comprehensive and organised information about drugs'. (Book p34)")
q(S3, 34, "The Indian Pharmacopoeia is prepared by:",
  ["Pharmacists", "Doctors", "Nurses", "Drug manufacturers"], 0,
  "The 'made by' row of the Indian compendia table gives pharmacists for IP and doctors for the drug formulary. (Book p34)")
q(S3, 34, "The drug formulary is made by:",
  ["Doctors", "Pharmacists", "Regulatory authorities", "Manufacturers"], 0,
  "The 'made by' row for drug formulary is doctors, in contrast to pharmacists for the Indian Pharmacopoeia. (Book p34)")
q(S3, 34, "The Indian Pharmacopoeia gives information about:",
  ["Structure, storage and purity of drugs", "Usage, mechanism of action, side-effects and contraindications",
   "Only the cost of drugs", "Only drug interactions"], 0,
  "The IP column of the information row lists structure, storage and purity. (Book p34)")
q(S3, 34, "The drug formulary gives information about:",
  ["Usage, mechanism of action, side-effects and contraindications",
   "Structure, storage and purity", "Bioavailability and half-life",
   "The manufacturing process"], 0,
  "The drug formulary column lists usage, mechanism of action, side effects and contraindications. (Book p34)")
q(S3, 34, "The Indian Pharmacopoeia is used by:",
  ["Drug manufacturers and drug regulatory authorities", "Doctors for prescribing drugs",
   "Patients only", "Nurses only"], 0,
  "The 'used by' row of the IP column gives drug manufacturers and drug regulatory authorities. (Book p34)")
q(S3, 34, "The drug formulary is used by:",
  ["Doctors, for prescribing drugs", "Drug manufacturers", "Regulatory authorities",
   "Pharmacists for compounding"], 0,
  "The 'used by' row for the drug formulary reads 'Doctors : For prescribing drugs'. (Book p34)")
q(S3, 34, "The note at the end of the drug compendia section says:",
  ["A prescription must contain generic names", "A prescription must contain brand names",
   "A prescription must contain chemical names", "Only doctors may read the formulary"], 0,
  "The note reads 'Prescription must contain generic names'. (Book p34)")

S4 = "Routes of Drug Administration: Local Drugs"
q(S4, 34, "Local drugs act:",
  ["At the site of application", "Only after reaching the systemic circulation",
   "Only after hepatic metabolism", "Only on the central nervous system"], 0,
  "The first bullet under local drugs says 'Drugs act at the site of application'. (Book p34)")
q(S4, 34, "Which of these is an advantage of local drug administration?",
  ["It increases the effect of drugs and decreases systemic side effects",
   "It increases systemic side effects", "It increases first pass metabolism",
   "It never works at the site of application"], 0,
  "The bullets state local drugs increase the effect of drugs and decrease the systemic side effects. (Book p34)")
q(S4, 34, "Topical drugs applied on the skin include:",
  ["Steroid antibiotics", "Bladder cancer drugs", "Antiglaucoma drugs", "Nitroglycerin"], 0,
  "The topical flow reads 'Site → Skin (Steroid Antibiotics)'. (Book p34)")
q(S4, 34, "Bladder cancer drugs are given topically on the:",
  ["Mucous membrane", "Skin", "Eye", "Nasal mucosa"], 0,
  "The topical branch reads 'mucous membrane (bladder cancer drugs)'. (Book p34)")
q(S4, 34, "Which class of drugs is applied topically to the eye?",
  ["Drugs used in cases of glaucoma", "Steroid antibiotics", "Bladder cancer drugs",
   "Tocolytic drugs"], 0,
  "The topical branch reads 'eye (drugs used in cases of glaucoma)'. (Book p34)")

S5 = "Intrathecal, Intra-articular and Intra-arterial Routes"
q(S5, 35, "Intrathecal injection means injection:",
  ["Into CSF via the subarachnoid space by lumbar puncture", "Into a joint cavity",
   "Directly into an artery", "Into the skin"], 0,
  "The site of the intrathecal route is 'into CSF by injection into subarachnoid space by means of lumbar puncture'. (Book p35)")
q(S5, 35, "The main purpose of the intrathecal route is to:",
  ["Bypass the blood-brain barrier", "Avoid first pass metabolism",
   "Give a large volume of drug", "Produce a local effect on skin"], 0,
  "The first use given is 'Bypass blood-brain barrier (Aminoglycosides in case of meningitis)'. (Book p35)")
q(S5, 35, "Which drug is given intrathecally in meningitis?",
  ["Aminoglycosides", "Baclofen", "Methotrexate", "Lidocaine"], 0,
  "The example for bypassing the blood-brain barrier is aminoglycosides in case of meningitis. (Book p35)")
q(S5, 35, "Lidocaine and bupivacaine given intrathecally are used for:",
  ["Lumbosacral anesthesia", "CNS leukemia", "Amyotrophic lateral sclerosis",
   "Meningitis"], 0,
  "The bullet reads 'Lidocaine, Bupivacaine (Lumbosacral anesthesia)'. (Book p35)")
q(S5, 35, "Methotrexate is given by the intrathecal route in:",
  ["CNS leukemia", "Lumbosacral anesthesia", "Meningitis", "Rheumatoid arthritis"], 0,
  "The page lists 'methotrexate in CNS leukemia' under intrathecal use. (Book p35)")
q(S5, 35, "Baclofen is given intrathecally in amyotrophic lateral sclerosis because:",
  ["Being planted in the subarachnoid space it releases muscle relaxant periodically",
   "It bypasses the blood-brain barrier only once", "It is too irritant for oral use",
   "It has no oral absorption at all"], 0,
  "The page explains that baclofen in ALS is planted in the subarachnoid space and releases muscle relaxant periodically. (Book p35)")
q(S5, 35, "Steroids injected into a joint in rheumatoid arthritis represent which route?",
  ["Intraarticular", "Intrathecal", "Intraarterial", "Subcutaneous"], 0,
  "The line 'Intraarticular : Eg → Steroids in rheumatoid arthritis' defines this route. (Book p35)")
q(S5, 35, "The intraarterial route means injecting:",
  ["Directly into the artery supplying the organ, avoiding systemic circulation",
   "Into the subarachnoid space", "Into a joint space", "Into the subcutaneous fat"], 0,
  "The definition given is 'Directly into the artery supplying organ (Avoids system circulation)'. (Book p35)")
q(S5, 35, "Which cancers are treated by the intraarterial route?",
  ["Head & neck cancer and hepatocellular cancer", "CNS leukemia and bladder cancer",
   "Lung cancer and breast cancer", "Melanoma and sarcoma"], 0,
  "The uses listed for the intraarterial route are head & neck cancer and hepatocellular cancer. (Book p35)")

S6 = "Enteral Routes: Oral, Rectal and Sublingual"
q(S6, 35, "The most common route of drug administration is:",
  ["Oral", "Rectal", "Sublingual", "Intravenous"], 0,
  "The oral row of the enteral table begins 'm/c route'. (Book p35)")
q(S6, 35, "The advantages of the oral route include:",
  ["Cost effective, convenient and safest", "Fastest onset with 100% bioavailability",
   "No first pass metabolism", "Useful in unconscious patients"], 0,
  "The oral advantages are cost effective, convenient and safest. (Book p35)")
q(S6, 35, "The oral route has maximum first pass metabolism because:",
  ["100% of the drug reaches the portal vein", "50% reaches the portal vein",
   "It is absorbed into the inferior vena cava", "It is absorbed from the rectum"], 0,
  "The disadvantage reads 'maximum first pass metabolism (100% → Portal vein)'. (Book p35)")
q(S6, 35, "Absorption after oral administration is described as the most variable because of:",
  ["Differences in lipid solubility, food intake and HCl", "Differences in renal function only",
   "Differences in plasma protein binding", "Differences in cardiac output"], 0,
  "The second oral disadvantage is most variable absorption due to difference in lipid solubility, food, intake and HCl. (Book p35)")
q(S6, 35, "Large molecular drugs like proteins have:",
  ["Poor oral absorption", "Excellent oral absorption", "No first pass metabolism",
   "100% oral bioavailability"], 0,
  "The oral disadvantage notes 'Large molecular drugs have poor oral absorption (like proteins)'. (Book p35)")
q(S6, 35, "Which drugs are listed as used by the oral route?",
  ["Lipid soluble drugs and small molecule drugs", "Peptides and proteins",
   "Nitroglycerin and ergotamine", "Aminoglycosides and baclofen"], 0,
  "The oral 'drugs used' cell gives lipid soluble drugs and small molecule drugs. (Book p35)")
q(S6, 35, "The advantage of the rectal route over oral is:",
  ["Faster effect with 50% less first pass metabolism", "100% bioavailability",
   "No first pass metabolism at all", "It is the safest route"], 0,
  "The rectal advantages are a faster effect and 50% less first pass metabolism than the oral route. (Book p35)")
q(S6, 35, "In the rectal route, the drug absorbed enters:",
  ["50% portal vein and 50% IVC (systemic circulation)", "100% portal vein",
   "100% inferior vena cava", "Lymphatics only"], 0,
  "The bracket reads '(50% : Portal vein) (50% : IVC Systemic circulation)'. (Book p35)")
q(S6, 35, "The disadvantage of the rectal route is that it is:",
  ["Inconvenient", "Costly", "Unsafe", "Slow in onset"], 0,
  "The only disadvantage listed for the rectal route is 'Inconvenient'. (Book p35)")
q(S6, 35, "Diazepam by the rectal route is used in children for:",
  ["Febrile seizures", "Meningitis", "Glaucoma", "Status asthmaticus"], 0,
  "The rectal drugs cell gives 'Diazepam in children for febrile seizures'. (Book p35)")
q(S6, 35, "In febrile seizures of children, which drug is preferred over diazepam rectally?",
  ["Midazolam", "Lorazepam", "Phenobarbitone", "Nitroglycerin"], 0,
  "The parenthesis reads '(midazolam preferred)'. (Book p35)")
q(S6, 35, "In the sublingual route, the drug is absorbed into the:",
  ["SVC and then the heart", "Portal vein and then the liver",
   "IVC directly", "Lymphatics"], 0,
  "The sublingual flow chart reads 'under the tongue → SVC → Heart'. (Book p35)")
q(S6, 35, "The sublingual route has:",
  ["No first pass metabolism and fast cardiac effects", "Maximum first pass metabolism",
   "Slow onset of action", "Poor bioavailability"], 0,
  "The sublingual advantages are no first pass metabolism and fast cardiac effects. (Book p35)")
q(S6, 35, "Nitroglycerin (NTG) is spat out after the desired result because:",
  ["Absorption of NTG after the desired effect causes postural hypotension",
   "It stains the teeth", "It causes tachycardia", "It is bitter in taste"], 0,
  "The sublingual advantage cell explains that NTG is spat out after the desired result since further absorption causes postural hypotension. (Book p35)")
q(S6, 35, "The disadvantages of the sublingual route are:",
  ["Cardiac side effects and teeth discolouration", "Inconvenience and cost",
   "Postural hypotension only", "Infection and pain"], 0,
  "The sublingual disadvantages listed are cardiac side effects and teeth discolouration. (Book p35)")
q(S6, 35, "Which drugs are listed as used by the sublingual route?",
  ["Nitroglycerin, ergotamine, nifedipine and buprenorphine",
   "Lipid soluble and small molecule drugs", "Insulin and peptides",
   "Salbutamol and ipratropium"], 0,
  "The sublingual drug list is nitroglycerin (angina/MI), ergotamine, nifedipine and buprenorphine. (Book p35)")
q(S6, 35, "Sublingual nifedipine is used because it:",
  ["Rapidly lowers BP compared to oral", "Has no cardiac side effects",
   "Avoids teeth discolouration", "Has a long duration of action"], 0,
  "The sublingual drug cell notes 'Nifedipine : Rapidly ↓ BP compared to oral'. (Book p35)")
q(S6, 35, "Drugs ending with 'tide', 'mab' or 'ase' are identified as:",
  ["Proteins", "Lipid soluble drugs", "Small molecule drugs", "Prodrugs"], 0,
  "The note reads 'Identification of proteins → Drugs ending with tide, mab, ase'. (Book p35)")

S7 = "Parenteral Routes"
q(S7, 36, "The advantage of the intravenous route is that it is:",
  ["Fastest, used in emergency, allows large volume and gives 100% bioavailability",
   "Self injectable", "Long acting", "Free of all toxicity"], 0,
  "The IV advantages are fastest (used in emergency), large volume can be given and 100% bioavailability. (Book p36)")
q(S7, 36, "A drug in an oily medium given intravenously can cause:",
  ["Hemolysis", "Skin necrosis", "Cough", "Infection"], 0,
  "The IV disadvantage reads 'Drug in oily medium : Hemolysis'. (Book p36)")
q(S7, 36, "Epinephrine given intramuscularly is preferred over the intravenous route because IV use causes:",
  ["Ventricular tachycardia and cardiac arrest", "Severe hemolysis",
   "Skin necrosis", "Bronchospasm"], 0,
  "The example in the IV disadvantage cell is 'Epinephrine i/m > i/v (i/v causes ventricular tachycardia and cardiac arrest)'. (Book p36)")
q(S7, 36, "Which drug is given intravenously in hypertensive emergency?",
  ["Nicardipine", "Furosemide", "Sumatriptan", "Salbutamol"], 0,
  "The IV drugs cell lists nicardipine for hypertensive emergency. (Book p36)")
q(S7, 36, "Furosemide is given by which route in pulmonary edema?",
  ["Intravenous", "Subcutaneous", "Intranasal", "Inhalational"], 0,
  "The IV drugs cell lists 'Furosemide in Pulmonary edema'. (Book p36)")
q(S7, 36, "Peptides are listed as drugs used by which parenteral routes?",
  ["Intravenous, intramuscular and subcutaneous", "Only intravenous",
   "Only intranasal", "Only subcutaneous"], 0,
  "Peptides appear in the drugs-used cells of IV, IM and SC routes. (Book p36)")
q(S7, 36, "The advantage of the intramuscular route is that it is:",
  ["Self injectable, with right expertise", "The fastest route",
   "Free of infection risk", "Gives 100% bioavailability"], 0,
  "The IM advantage reads 'Self injectable, (with right expertise)'. (Book p36)")
q(S7, 36, "Infections with the intramuscular route occur due to:",
  ["Unsanitary or faulty techniques", "Oily vehicles", "Large volume injection",
   "Rapid absorption"], 0,
  "The IM disadvantage reads 'Infections - D/t unsanitary / faulty techniques'. (Book p36)")
q(S7, 36, "Which drugs are given intramuscularly and can cause pain as a side effect?",
  ["Drugs in oily medium", "Nitroglycerin", "Insulin", "Sumatriptan"], 0,
  "The IM drugs cell lists peptides, irritants and drugs in oily medium - S/E pain. (Book p36)")
q(S7, 36, "The subcutaneous route gives a long duration of action because:",
  ["Of slow absorbing from S.C. fat", "The drug is given in a large volume",
   "It bypasses the liver", "The drug is highly protein bound"], 0,
  "The SC advantage is long duration of action due to slow absorbing from S.C. fat. (Book p36)")
q(S7, 36, "The subcutaneous route is contraindicated with irritants because it causes:",
  ["Skin necrosis", "Abscess formation only", "Hemolysis", "Cough"], 0,
  "The SC disadvantage reads 'Skin necrosis with irritants (C/I)'. (Book p36)")
q(S7, 36, "Long acting insulin is given by which route?",
  ["Subcutaneous", "Intravenous", "Intranasal", "Inhalational"], 0,
  "The SC drugs cell lists long acting insulin under peptides. (Book p36)")
q(S7, 36, "The intranasal (spray) route has the advantages of:",
  ["Rapid effect and bypassing the blood-brain barrier", "100% bioavailability only",
   "No limit on the dose", "Use in emergency only"], 0,
  "The intranasal advantages are rapid effect and bypassing the BBB. (Book p36)")
q(S7, 36, "For the intranasal route:",
  ["Only a limited dose can be given and only potent drugs are used",
   "Large volumes can be given", "Only lipid soluble drugs are used",
   "It is unsuitable for peptides"], 0,
  "The intranasal disadvantages are that a limited dose can be administered and only potent drugs are used. (Book p36)")
q(S7, 36, "Which drugs are given by the intranasal spray?",
  ["GnRH agonist, sumatriptan and nicotine", "Salbutamol, ipratropium and tobramycin",
   "Insulin and heparin", "Nicardipine and furosemide"], 0,
  "The intranasal drugs cell lists peptides like GnRH agonist, sumatriptan and nicotine (in case of headache). (Book p36)")
q(S7, 36, "The inhalational route has the fastest effect because the lung is:",
  ["A highly vascularized organ", "A large organ", "A peripheral organ",
   "Protected by surfactant"], 0,
  "The inhalational advantage reads 'Fastest effect - Lung : Highly vascularized organ'. (Book p36)")
q(S7, 36, "The disadvantage of the inhalational route is:",
  ["Irritants cause cough", "Skin necrosis", "Hemolysis", "Limited dose only"], 0,
  "The inhalational disadvantage reads 'Irritants → Cough'. (Book p36)")
q(S7, 36, "Afrezza is:",
  ["The fastest and shortest acting insulin", "A long acting insulin",
   "An inhaled anticholinergic", "An inhaled antibiotic"], 0,
  "The note at the foot of the page reads 'Afrezza → Fastest and Shortest acting insulin'. (Book p36)")
q(S7, 36, "Afrezza is given by which route?",
  ["Inhalational (systemic)", "Subcutaneous", "Intravenous", "Intranasal"], 0,
  "Afrezza (insulin) is listed under the systemic drugs of the inhalational route. (Book p36)")
q(S7, 36, "Inhaled gases are grouped under the inhalational route with:",
  ["100% bioavailability", "50% bioavailability", "No systemic absorption",
   "First pass metabolism"], 0,
  "The inhalational systemic drug list writes 'Inhalational gases (100% bio availability)'. (Book p36)")
q(S7, 36, "Which drugs are given by the inhalational route for a local effect?",
  ["Salbutamol, ipratropium and tobramycin", "Afrezza and inhaled gases",
   "Sumatriptan and nicotine", "Nicardipine and furosemide"], 0,
  "The local inhalational list is salbutamol, ipratropium and tobramycin (pseudomonas pneumonia). (Book p36)")
q(S7, 36, "Tobramycin by inhalation is used for:",
  ["Pseudomonas pneumonia", "Asthma", "Pulmonary edema", "Tuberculosis"], 0,
  "The inhalational local drug list gives 'Tobramycin (Pseudomonas pneumonia)'. (Book p36)")

UNITS = [
 (1, "Definitions", [1,8],
  "The chapter opens with definitions. Pharmacology is the study of structure, effect (MOA), side effects and contraindications of drugs; pharmacotherapeutics is the study of a drug in service of disease (dose, route and response); pharmacognosy is the study of drugs derived from plants; chemotherapy is the use of drugs in cancer and infection; and pharmacy deals with compounding - mixing of drugs, now obsolete - and dispensing of drugs, with barcoding used to dispense the right drug and avoid errors. A drug is a chemical with a known structure that alters the pathophysiology for therapeutic gain."),
 (2, "Drug Sources", [9,17],
  "Drugs come from four sources: natural (plants - quinine, digoxin, morphine from the poppy plant; animal peptides - insulin and heparin from porcine mucosa; microorganisms - antibiotics), semisynthetic or modified natural chemicals (apomorphine, a dopamine agonist used in parkinsonism), synthetic drugs made by rational drug designing - designed complementary to a receptor, binding and inhibiting, resulting in modification of the disease - and genetic engineering, the process of introducing a gene in a cell line to obtain a product, e.g. human insulin (gene) giving regular insulin (peptide)."),
 (3, "Drug Nomenclature and Compendia", [18,32],
  "Drugs carry a chemical name (long, based on structure), a generic/non proprietary name (abbreviated, e.g. propranolol, with tell-tale suffixes: -lol for β blockers, -pril for ACE inhibitors, -prazole for PPIs) and a branded/proprietary name given by the manufacturer. A compendium is a book of comprehensive organised drug information: the Indian Pharmacopoeia is made by pharmacists, covers structure, storage and purity, and is used by drug manufacturers and regulatory authorities, whereas the drug formulary is made by doctors, covers usage, mechanism of action, side effects and contraindications, and is used by doctors for prescribing. The note to remember is that a prescription must contain generic names."),
 (4, "Routes of Drug Administration: Local Drugs", [33,37],
  "Local drugs act at the site of application, increasing the effect of the drug while decreasing systemic side effects. Topically they are applied to skin (steroid antibiotics), mucous membrane (bladder cancer drugs) and eye (drugs used in glaucoma)."),
 (5, "Intrathecal, Intra-articular and Intra-arterial Routes", [38,46],
  "Intrathecal injection puts the drug into CSF by injection into the subarachnoid space by lumbar puncture; its uses are to bypass the blood-brain barrier (aminoglycosides in meningitis), and to give a local effect on brain/spinal cord with lidocaine and bupivacaine for lumbosacral anesthesia, methotrexate in CNS leukemia, and baclofen in amyotrophic lateral sclerosis - planted in the subarachnoid space, it releases muscle relaxant periodically. Intraarticular injection is exemplified by steroids in rheumatoid arthritis, while the intraarterial route goes directly into the artery supplying the organ, avoiding systemic circulation, and is used for head & neck cancer and hepatocellular cancer."),
 (6, "Enteral Routes: Oral, Rectal and Sublingual", [47,64],
  "Among enteral routes the oral route is the most common, being cost effective, convenient and safest, but it has maximum first pass metabolism (100% to the portal vein), the most variable absorption (difference in lipid solubility, food, intake, HCl) and poor absorption of large molecules like proteins; lipid soluble and small molecule drugs are used orally. The rectal route acts faster with 50% less first pass metabolism (50% portal vein, 50% IVC) but is inconvenient - diazepam is given rectally in children for febrile seizures, with midazolam preferred. Sublingual drugs are absorbed under the tongue into the SVC and then the heart, giving no first pass metabolism and fast cardiac effects (NTG is spat out after the desired result, since further absorption causes postural hypotension); disadvantages are cardiac side effects and teeth discolouration, and the drugs used are nitroglycerin, ergotamine, nifedipine (rapidly lowers BP compared with oral) and buprenorphine. Proteins are recognised by names ending in 'tide', 'mab' or 'ase'."),
 (7, "Parenteral Routes", [65,86],
  "Parenteral routes: intravenous is the fastest, used in emergency, allows large volume and gives 100% bioavailability, but oily medium causes hemolysis and epinephrine is better intramuscular (IV causes ventricular tachycardia and cardiac arrest) - nicardipine is used in hypertensive emergency and furosemide in pulmonary edema. Intramuscular is self injectable with right expertise, risks infection through unsanitary or faulty techniques, and suits peptides, irritants and oily drugs (pain). Subcutaneous gives long duration of action from slow absorption from S.C. fat and is self injectable, but irritants cause skin necrosis; long acting insulin is given this way. Intranasal spray gives rapid effect and bypasses the BBB but only a limited dose of potent drugs can be given (GnRH agonist, sumatriptan, nicotine). The inhalational route has the fastest effect because the lung is highly vascularized; irritants cause cough. Afrezza is the fastest and shortest acting insulin, and inhalational gases have 100% bioavailability, while salbutamol, ipratropium and tobramycin (pseudomonas pneumonia) are given for a local effect."),
]

byid = {}
for i, (sec, page, text, opts, ans, exp) in enumerate(Q, 1):
    byid[i] = {"id": f"PHARM-C11-{i:03d}", "sec": sec, "page": page, "q": text,
               "opts": opts, "ans": ans, "exp": exp}
questions = [byid[i] for i in sorted(byid)]
units = []
for n, title, (a, b), guide in UNITS:
    for i in range(a, b + 1):
        byid[i]["sec"] = title
    units.append({"id": f"PHARM-U11-{n}", "ch": 11, "n": n, "title": title,
                  "sec": f"{title} · p{byid[a]['page']}",
                  "qs": [f"PHARM-C11-{i:03d}" for i in range(a, b + 1)],
                  "guide": guide})
json.dump({"questions": questions, "units": units},
          open("data/ch11.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("questions:", len(questions), "units:", len(units))
for u in units:
    print(" ", u["id"], u["title"], len(u["qs"]), u["sec"])
