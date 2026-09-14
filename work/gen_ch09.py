# -*- coding: utf-8 -*-
import json
Q = []
def q(sec, page, text, opts, ans, exp):
    Q.append((sec, page, text, opts, ans, exp))

S1 = "Drug Schedules in India"
q(S1, 25, "The label warning 'Caution: It is dangerous to take this preparation except under medical supervision' is displayed for:",
  ["Schedule G", "Schedule H", "Schedule H1", "Schedule X"], 0,
  "The Schedule G row of the drug schedule table carries exactly this caution statement in the label display column. (Book p25)")
q(S1, 25, "Which drugs are listed under Schedule G?",
  ["Majority drugs such as antihypertensives and antidiabetics", "Narcotic drugs only",
   "Antibiotics only", "Drugs marketed under generic names only"], 0,
  "The drug details column for schedule G reads 'majority drugs (Antihypertensive, Antidiabetics, etc.)'. (Book p25)")
q(S1, 25, "The warning 'To be sold by retail on the prescription of a registered medical practitioner only' applies to:",
  ["Schedule H", "Schedule G", "Schedule P", "Schedule Y"], 0,
  "This warning is written in the label display cell of schedule H. (Book p25)")
q(S1, 25, "A Schedule H drug with Rx written in black:",
  ["Can be reissued with the same prescription", "Can be sold without prescription",
   "Needs a fresh prescription every time", "Requires a special licence for sale"], 0,
  "The table states for Rx (in black): 'drugs can be reissued with same prescription'. (Book p25)")
q(S1, 25, "A Schedule H drug with NRx written in red:",
  ["Is issued only once with a recent prescription", "Can be reissued with the same prescription",
   "Requires no prescription", "Is a schedule Y drug"], 0,
  "The NRx (in red) row states 'issue drug only once with recent prescription (to avoid abuse potential)'. (Book p25)")
q(S1, 25, "Which of these are examples of Schedule H NRx (red) drugs?",
  ["Codeine and benzodiazepines", "Amphetamine and ketamine",
   "Antihypertensives and antidiabetics", "Thalidomide only"], 0,
  "The drug details for NRx (in red) list narcotic drugs, e.g. codeine, benzodiazepines. (Book p25)")
q(S1, 25, "Why is an NRx (red) schedule H drug issued only once against a recent prescription?",
  ["To avoid abuse potential", "To prevent resistance", "To reduce cost", "To avoid expiry"], 0,
  "The parenthetical note in the NRx row reads '(To avoid abuse potential)'. (Book p25)")
q(S1, 25, "Antibiotics are placed in which schedule to prevent resistance?",
  ["Schedule H1", "Schedule H", "Schedule G", "Schedule X"], 0,
  "The schedule H1 row reads 'Antibiotics to prevent resistance d/t unauthorized sale'. (Book p25)")
q(S1, 25, "Schedule H1 was introduced in the year:",
  ["2013", "2003", "1993", "2020"], 0,
  "The schedule H1 cell notes '(introduced in 2013)'. (Book p25)")
q(S1, 25, "Schedule H1 drugs must display:",
  ["Rx (in red)", "NRx (in red)", "XRx (in red)", "No special label"], 0,
  "The label display for schedule H1 is Rx (in red). (Book p25)")
q(S1, 25, "Narcotic and psychotropic drugs such as amphetamine, methylphenidate, ketamine and pentobarbital belong to:",
  ["Schedule X", "Schedule H1", "Schedule G", "Schedule P"], 0,
  "The schedule X drug details list narcotic and psychotropic drugs with exactly these examples. (Book p25)")
q(S1, 25, "Which label is displayed for Schedule X drugs?",
  ["XRx (in red)", "Rx (in red)", "NRx (in red)", "A caution statement"], 0,
  "The schedule X label display column shows XRx (in red). (Book p25)")
q(S1, 25, "Schedule X drugs require special licence because:",
  ["The sale and manufacture is for drugs with high abuse potential",
   "They are very expensive", "They are antibiotics", "They expire quickly"], 0,
  "The bullet under schedule X reads 'Require special license for manufacture and sale d/t high abuse potential'. (Book p25)")
q(S1, 25, "For Schedule X drugs, the retailer should maintain the register and prescription copy for a minimum of:",
  ["2 years", "6 months", "5 years", "10 years"], 0,
  "The schedule X bullet states the retailer should maintain register and prescription copy for a minimum 2 years. (Book p25)")
q(S1, 25, "Schedule P deals with:",
  ["The expiry period of the drug", "Clinical trials and import of new drugs",
   "Drugs marketed under generic names only", "Antibiotics"], 0,
  "The schedule P row reads 'About expiry period of drug'. (Book p25)")
q(S1, 25, "Drugs marketed under generic names only fall under:",
  ["Schedule W", "Schedule P", "Schedule Y", "Schedule H1"], 0,
  "The schedule W row states 'Drugs marketed under generic names only'. (Book p25)")
q(S1, 25, "Guidelines on clinical trials, import and manufacture of new drugs are given in:",
  ["Schedule Y", "Schedule X", "Schedule G", "Schedule P"], 0,
  "The schedule Y row reads 'Guideline on clinical trials, import and manufacture of new drugs'. (Book p25)")
q(S1, 25, "For which three schedules is the label display column left blank (a dash)?",
  ["Schedule P, W and Y", "Schedule G, H and X", "Schedule H1, X and Y",
   "Schedule G, P and Y"], 0,
  "In the table the label display cells of schedule P, W and Y each carry only a dash. (Book p25)")

S2 = "Pregnancy Drug Categories"
q(S2, 25, "The pregnancy drug categories are based on:",
  ["Safety : A > B > C", "Efficacy : A > B > C", "Cost : A > B > C", "Half-life : A > B > C"], 0,
  "Under 'Pregnancy Drug Categories' the note reads 'Based on Safety : A > B > C'. (Book p25)")
q(S2, 25, "In an animal study, absence of risk plus maximum safety in humans corresponds to category:",
  ["A", "B", "C", "D"], 0,
  "Category A has 'Absent to fetus' in human studies with maximum safety in the significance column. (Book p25)")
q(S2, 25, "Human studies are lacking but animal studies show the drug is safe (absent risk) in category:",
  ["B", "A", "C", "D"], 0,
  "Category B : human study lacking, animal studies absent (of risk) - 'safely prescribed'. (Book p25)")
q(S2, 25, "Positive teratogenic effect in animals with human data not available corresponds to category:",
  ["C", "B", "D", "X"], 0,
  "Category C shows 'Not available' for human studies and 'Positive Teratogenic' for animal studies. (Book p25)")
q(S2, 25, "Which categories show positive teratogenicity in human studies?",
  ["D and X", "A and B", "B and C", "C only"], 0,
  "The human studies column reads 'Positive Teratogenic' for both category D and category X. (Book p25)")
q(S2, 25, "Category D drugs are used when:",
  ["The benefit is greater than the risk (e.g. valproate in JME)",
   "There is maximum safety (e.g. vitamins)", "They can never be used in pregnancy",
   "Animal studies are absent"], 0,
  "The significance column for D reads 'used if benefit > Risk (e.g. valproate in JME)'. (Book p25)")
q(S2, 25, "Category X drugs are:",
  ["Absolutely contraindicated (e.g. thalidomide)", "Used if benefit exceeds risk",
   "Safely prescribed in pregnancy", "Reserved for labour"], 0,
  "The significance column for X reads 'Absolute C/I (e.g. Thalidomide)'. (Book p25)")
q(S2, 25, "Which drug is the example given for category X?",
  ["Thalidomide", "Valproate", "Phenytoin", "Warfarin"], 0,
  "Thalidomide is the example quoted for absolute contraindication in category X. (Book p25)")
q(S2, 25, "Valproate used in juvenile myoclonic epilepsy is quoted as an example for category:",
  ["D", "C", "X", "B"], 0,
  "Category D's example of benefit exceeding risk is valproate in JME. (Book p25)")

S3 = "Types of Drugs"
q(S3, 26, "A prescription/legend drug is:",
  ["A Schedule H drug", "A drug other than schedule G, H and X",
   "A drug for rare diseases", "A drug with a false label"], 0,
  "Type 1 in the list reads 'Prescription/Legend drug : schedule H drug'. (Book p26)")
q(S3, 26, "Over the counter (OTC) drugs are defined as:",
  ["Drugs other than Schedule G, H and X", "Only schedule H drugs",
   "Drugs for rare diseases", "Drugs of abuse"], 0,
  "Type 2 defines OTC drugs as drugs other than schedule G, H, X. (Book p26)")
q(S3, 26, "Orphan drugs are:",
  ["Drugs for rare diseases with low availability", "Drugs of abuse",
   "Drugs manufactured under another drug's name", "Drugs with unwanted substances"], 0,
  "Type 3 defines orphan drugs as drugs for rare diseases, with a downward arrow for availability. (Book p26)")
q(S3, 26, "Cocaine, heroin and methamphetamine are examples of:",
  ["Street/illicit drugs of abuse", "Orphan drugs", "Spurious drugs", "Prototype drugs"], 0,
  "Type 4, 'Street/illicit drug', gives cocaine, heroin and methamphetamine as drugs of abuse. (Book p26)")
q(S3, 26, "A spurious drug is one which is:",
  ["Manufactured under a name belonging to another drug (imitation), or does not solve the intended purpose",
   "Sold only on prescription", "Given a false label while containing the correct drug",
   "Marketed under a generic name"], 0,
  "The two bullets under spurious drug describe an imitation of another drug's name and a product that does not solve the intended purpose (e.g. wrong dosage). (Book p26)")
q(S3, 26, "A drug carrying false information on its label is a:",
  ["Misbranded drug", "Spurious drug", "Adulterated drug", "Prototype drug"], 0,
  "Type 6 defines a misbranded drug as a drug with false information on the label. (Book p26)")
q(S3, 26, "An adulterated drug is one that:",
  ["Contains an unwanted substance", "Has false label information",
   "Is imported illegally", "Is used for rare diseases"], 0,
  "Type 7 defines an adulterated drug as a drug with an unwanted substance in it. (Book p26)")
q(S3, 26, "The prototype drug of the opioids is:",
  ["Morphine", "Codeine", "Pethidine", "Fentanyl"], 0,
  "Type 8 defines a prototype drug as the parental/most commonly used drug of a group, and gives morphine for all opioids as the example. (Book p26)")
q(S3, 26, "A prototype drug is defined as:",
  ["The parental/most commonly used drug of a group", "The newest drug of a group",
   "The cheapest drug of a group", "A drug with no known receptor"], 0,
  "The definition reads 'Parental / most common used drug of a group'. (Book p26)")
q(S3, 26, "A P (Personal) drug is developed for a disease based on:",
  ["STEP criteria", "GCP guidelines", "CPCSEA guidelines", "AND gate criteria"], 0,
  "Type 9 states 'P (Personal) drug : Developed for a disease based on STEP criteria'. (Book p26)")
q(S3, 26, "The STEP criteria for a personal drug include:",
  ["Safety, tolerability, efficacy and price", "Safety, toxicity and efficacy only",
   "Speed, toxicity, efficacy and price", "Safety, tolerability, expiry and potency"], 0,
  "The four bullets under STEP are safety, tolerability, efficacy and price. (Book p26)")
q(S3, 26, "An orphan receptor is:",
  ["A receptor without a known ligand", "A receptor for an orphan drug",
   "A receptor with two ligands", "A nuclear receptor"], 0,
  "The note box beside the drug types states 'Orphan receptor : Receptor without a known ligand'. (Book p26)")

S4 = "Drug Development and Preclinical Trials"
q(S4, 26, "Before any clinical trial, a new drug must first undergo:",
  ["Preclinical trials", "Phase I trial", "Phase II trial", "Phase IV surveillance"], 0,
  "The drug development flow begins with the preclinical trials (in animals) oval before clinical trials (in humans). (Book p26)")
q(S4, 26, "Preclinical trials are known as:",
  ["Non-mandatory trials conducted in animals", "Mandatory trials in humans",
   "Postmarketing surveillance", "Phase 0 microdosing studies"], 0,
  "In the flow chart the preclinical trials are marked 'non mandatory' and '(in animals)', while phases I-IV are labelled mandatory. (Book p26)")
q(S4, 26, "In the drug development flow chart, phases I, II, III and IV are labelled:",
  ["Mandatory", "Non-mandatory", "Optional", "Ethical committee phases"], 0,
  "The bracket spanning phases I to IV in the flow chart is labelled 'mandatory'. (Book p26)")
q(S4, 26, "Phase I clinical trials are conducted in:",
  ["Normal healthy individuals", "Patients only", "Pregnant women", "Children"], 0,
  "The flow chart marks phase I with 'normal healthy individuals'. (Book p26)")
q(S4, 26, "Clinical trials as a whole are conducted in:",
  ["Humans", "Animals", "Tissue culture only", "Computer models"], 0,
  "The central oval of the flow chart reads 'Clinical Trials (In Humans)'. (Book p26)")
q(S4, 26, "Which phases involve patients in the flow chart?",
  ["Phase II onwards", "Phase I onwards", "Only phase IV", "Only phase 0"], 0,
  "The flow chart labels the later phases 'Patients' after the healthy individuals of phase I. (Book p26)")
q(S4, 26, "The first step of preclinical trials is to:",
  ["Draft a protocol (expectation of drug / information of animals)",
   "Submit to the human ethical committee", "Obtain CDSCO approval",
   "Submit a new drug application"], 0,
  "Step 1 of the PCT sequence is 'Draft a Protocol (Expectation of drug / information of animals)'. (Book p26)")
q(S4, 26, "The protocol of a preclinical trial is submitted to the:",
  ["Animal Ethical Committee (AEC)", "Human Ethical Committee", "CDSCO in New Delhi",
   "Pharmacy Council"], 0,
  "Step 2 of preclinical trials is 'Submit to Animal Ethical Committee (AEC)'. (Book p26)")
q(S4, 26, "Preclinical trials are conducted under:",
  ["CPCSEA guidelines", "GCP guidelines", "ICH guidelines", "Schedule Y only"], 0,
  "The last step of the PCT flow reads 'Conduct PCT under CPCSEA guidelines'. (Book p26)")
q(S4, 26, "In the preclinical trial sequence, what follows the approval of permission?",
  ["Conducting the PCT under CPCSEA guidelines", "Filing the NDA",
   "Phase 0 microdosing", "Phase I enrolment"], 0,
  "The sequence is draft protocol → submit to AEC → permission approved → conduct PCT under CPCSEA guidelines. (Book p26)")

S5 = "Clinical Trials: Prerequisite and Phase 0"
q(S5, 27, "The first step in the prerequisite for a clinical trial is:",
  ["Draft a protocol", "Submit to the human ethical committee",
   "Permission approved", "Conduct CT under GCP"], 0,
  "The clinical trial prerequisite list begins 'Draft a Protocol'. (Book p27)")
q(S5, 27, "The clinical trial protocol is submitted to the:",
  ["Human Ethical Committee", "Animal Ethical Committee", "CDSCO", "Institutional pharmacy"], 0,
  "Step 2 of the prerequisite reads 'Submit to Human Ethical Committee'. (Book p27)")
q(S5, 27, "Clinical trials are conducted under:",
  ["GCP (Good Clinical Practice) guidelines", "CPCSEA guidelines",
   "Schedule P", "Schedule W"], 0,
  "The final prerequisite step states 'Conduct CT under GCP guidelines (Good Clinical Practice)'. (Book p27)")
q(S5, 27, "Phase 0 of a clinical trial involves:",
  ["Microdosing with 100 mcg or 1/100th of the normal dose", "Therapeutic doses in patients",
   "Postmarketing surveillance", "Confirmation of efficacy in thousands"], 0,
  "Phase 0 is defined on the page as microdosing : dose of 100 mcg or 1/100th of normal dose. (Book p27)")
q(S5, 27, "Phase 0 is carried out in:",
  ["Normal healthy volunteers", "Patients", "Pregnant women", "Elderly patients only"], 0,
  "After microdosing the flow specifies 'in normal healthy volunteers'. (Book p27)")
q(S5, 27, "In phase 0, the drug given is:",
  ["Radioligand bound drug", "A supratherapeutic dose", "An intravenous bolus of the full dose",
   "A depot preparation"], 0,
  "The phase 0 flow reads 'Radioligand bound drug'. (Book p27)")
q(S5, 27, "The purpose of phase 0 is to determine:",
  ["Pharmacokinetics and pharmacodynamics", "Long term adverse drug reactions",
   "Confirmatory efficacy", "Cost effectiveness"], 0,
  "The phase 0 flow states 'Determine pharmacokinetics and pharmacodynamics'. (Book p27)")
q(S5, 27, "In phase 0, if the results are abnormal (toxicity/efficacy), the action is to:",
  ["Abort the trial", "Proceed to phase I", "Repeat the microdose", "Proceed directly to phase III"], 0,
  "The branching in phase 0 reads 'If normal → Phase I' and 'If abnormal (Toxicity/efficacy) → Abort trial'. (Book p27)")
q(S5, 27, "In phase 0, a normal result leads to:",
  ["Phase I", "Abort trial", "Phase IV", "New drug application"], 0,
  "The 'if normal' limb of the phase 0 flow leads to phase I. (Book p27)")

S6 = "Mandatory Phases of Clinical Trials"
q(S6, 27, "Phase I is described as:",
  ["Human pharmacology and toxicity study", "Therapeutic exploratory trial",
   "Therapeutic confirmatory trial", "Postmarketing surveillance"], 0,
  "The table's heading for phase I reads 'Human Pharmacology and Toxicity Study'. (Book p27)")
q(S6, 27, "Phase II is described as:",
  ["Therapeutic exploratory trial", "Human pharmacology and toxicity study",
   "Therapeutic confirmatory trial", "Postmarketing surveillance"], 0,
  "The heading over the phase II column is 'Therapeutic Exploratory Trial'. (Book p27)")
q(S6, 27, "Phase III is described as:",
  ["Therapeutic confirmatory trial", "Therapeutic exploratory trial",
   "Human pharmacology and toxicity study", "Postmarketing surveillance"], 0,
  "The heading over the phase III column is 'Therapeutic Confirmatory Trial'. (Book p27)")
q(S6, 27, "Phase IV is described as:",
  ["Postmarketing surveillance", "Therapeutic confirmatory trial",
   "Therapeutic exploratory trial", "Human pharmacology and toxicity study"], 0,
  "The heading over the phase IV column is 'Post marketing surveillance'. (Book p27)")
q(S6, 27, "The aim of phase I is to determine:",
  ["Toxicity, maximum tolerable dose, pharmacokinetics and pharmacodynamics",
   "Efficacy only", "Long term adverse drug reactions", "Efficacy confirmation"], 0,
  "The aim cell of phase I lists toxicity, maximum tolerable dose, pharmacokinetics and pharmacodynamics. (Book p27)")
q(S6, 27, "Maximum tolerable dose is determined in:",
  ["Phase I", "Phase II", "Phase III", "Phase IV"], 0,
  "Maximum tolerable dose appears in the aim list of phase I. (Book p27)")
q(S6, 27, "The aim of phase II is to:",
  ["Determine efficacy", "Confirm efficacy", "Detect rare ADRs", "Study toxicity in animals"], 0,
  "The aim cell for phase II reads 'To determine efficacy'. (Book p27)")
q(S6, 27, "The aim of phase III is to:",
  ["Confirm efficacy", "Determine efficacy", "Detect long term ADRs", "Fix the dose for animals"], 0,
  "The aim cell for phase III reads 'To confirm efficacy'. (Book p27)")
q(S6, 27, "The aim of phase IV is to determine:",
  ["Long term/rare adverse drug reactions (ADR)", "Efficacy in a few patients",
   "Maximum tolerable dose", "Pharmacokinetics in volunteers"], 0,
  "The phase IV aim cell reads 'To determine long term/rare Adverse Drug Reactions (ADR)'. (Book p27)")
q(S6, 27, "Phase I subjects are:",
  ["Normal healthy volunteers", "Patients only", "Pregnant women", "Both patients and healthy volunteers equally"], 0,
  "The subjects row of phase I lists 'Normal Healthy volunteers'. (Book p27)")
q(S6, 27, "The subjects in phases II, III and IV are:",
  ["Patients", "Normal healthy volunteers", "Animals", "Healthy volunteers in phase II and patients later"], 0,
  "The subjects row reads 'Patients' for phase II, III and IV. (Book p27)")
q(S6, 27, "For toxic drugs such as anti-HIV and anticancer agents:",
  ["Phases I and II are done simultaneously in patients", "Phase I is skipped entirely",
   "Only phase IV is done", "Phase I is done in animals"], 0,
  "The subjects cell notes 'Patients : For toxic drugs (Eg : Anti-HIV, Anticancer) → Phase I and II simultaneously done'. (Book p27)")
q(S6, 27, "The sample size in phase I is:",
  ["30-100", "100-500", "500-3000", "Many thousands"], 0,
  "The sample size row gives 30-100 for phase I. (Book p27)")
q(S6, 27, "The sample size in phase II is:",
  ["100-500", "30-100", "500-3000", "Many thousands"], 0,
  "The sample size row gives 100-500 for phase II. (Book p27)")
q(S6, 27, "The sample size in phase III is:",
  ["500-3000", "100-500", "30-100", "Many thousands"], 0,
  "The sample size row gives 500-3000 for phase III. (Book p27)")
q(S6, 27, "The sample size in phase IV is:",
  ["Many thousands", "500-3000", "100-500", "30-100"], 0,
  "The sample size row gives 'many thousands' for phase IV. (Book p27)")
q(S6, 27, "The duration of phase I is:",
  ["1-2 yrs", "2-3 yrs", "3-5 yrs", "Not specified"], 0,
  "The duration row gives 1-2 yrs for phase I. (Book p27)")
q(S6, 27, "The duration of phase II is:",
  ["2-3 yrs", "1-2 yrs", "3-5 yrs", "Not specified"], 0,
  "The duration row gives 2-3 yrs for phase II. (Book p27)")
q(S6, 27, "The duration of phase III is:",
  ["3-5 yrs", "2-3 yrs", "1-2 yrs", "Not specified"], 0,
  "The duration row gives 3-5 yrs for phase III. (Book p27)")
q(S6, 27, "The duration of phase IV is:",
  ["Not specified", "3-5 yrs", "5-10 yrs", "1-2 yrs"], 0,
  "In the duration row, phase IV is written as 'Not specified'. (Book p27)")
q(S6, 27, "The study design of phase I is:",
  ["Open type", "Randomized control trial", "RCT/RUCT", "Double blind"], 0,
  "The study design row gives 'Open type' for phase I. (Book p27)")
q(S6, 27, "The study design of phase IV is:",
  ["Open type", "Blinded", "RCT/RUCT", "Randomized control trial"], 0,
  "The study design row gives 'Open type' for phase IV. (Book p27)")
q(S6, 27, "The study design of phase III is:",
  ["RCT/RUCT", "Open type", "Blinded only", "Uncontrolled"], 0,
  "The study design row gives 'RCT/RUCT' for phase III. (Book p27)")
q(S6, 27, "The note on study designs of phases II and III says:",
  ["Blinded > Open", "Open > Blinded", "Only open studies are used",
   "Only blinded studies are used"], 0,
  "Above the study design cells for phases II and III the table writes 'Blinded > Open'. (Book p27)")
q(S6, 27, "Phase II study design involves:",
  ["Randomized control trial", "Open type", "RCT/RUCT", "Case control study"], 0,
  "The study design row for phase II reads 'Randomized Control Trial'. (Book p27)")
q(S6, 27, "R UCT stands for:",
  ["Random uncontrolled trial", "Randomised unique control trial",
   "Retrospective uncontrolled trial", "Rapid unblinded clinical trial"], 0,
  "The footnote below the table expands RUCT as 'Random uncontrolled Trial'. (Book p27)")
q(S6, 27, "Phase II trials are conducted at:",
  ["Unicentric centres", "Multicentric centres", "No fixed centre", "Only in New Delhi"], 0,
  "The centers row gives 'Unicentric' for phase II. (Book p27)")
q(S6, 27, "Phase III trials are conducted at:",
  ["Multicentric centres", "Unicentric centres", "A single centre only", "Only in animals"], 0,
  "The centers row gives 'multicentric' for phase III. (Book p27)")
q(S6, 27, "The centres row for phases I and IV is:",
  ["A dash (-), i.e. not specified", "Unicentric", "Multicentric", "Two centres"], 0,
  "In the centers row, both phase I and phase IV carry only a dash. (Book p27)")
q(S6, 27, "Maximum failure rate is seen in:",
  ["Phase II", "Phase I", "Phase III", "Phase IV"], 0,
  "The failure rate row writes 'maximum' under phase II and dashes elsewhere. (Book p27)")
q(S6, 27, "The failure rate in phases I, III and IV is:",
  ["Shown as a dash (-)", "Maximum", "Minimum", "50%"], 0,
  "The failure rate row shows a dash for phases I, III and IV, with 'maximum' only in phase II. (Book p27)")
q(S6, 27, "Irrespective of population size, all multicentric studies belong to:",
  ["Phase III", "Phase II", "Phase I", "Phase IV"], 0,
  "The note below the table states 'irrespective of population size, all multicentric studies → Phase III'. (Book p27)")

S7 = "Approval in Phase III and Phase V"
q(S7, 28, "IND stands for:",
  ["Investigational New Drug", "Indian New Drug", "Investigational Narcotic Drug",
   "Initial New Dose"], 0,
  "The approval flow begins with 'IND (Investigational New Drug)'. (Book p28)")
q(S7, 28, "Before submitting a new drug application, one must:",
  ["Confirm efficacy and safety for use", "Obtain a schedule X licence",
   "Complete phase V", "Publish results in a journal"], 0,
  "The second step of the approval flow is 'Confirm efficacy and safety for use'. (Book p28)")
q(S7, 28, "The New Drug Application (NDA) in India is submitted to:",
  ["CDSCO in New Delhi", "WHO", "FDA", "ICMR in Mumbai"], 0,
  "The flow states 'Submit New Drug Application (NDA) to CDSCO in New Delhi'. (Book p28)")
q(S7, 28, "CDSCO stands for:",
  ["Central Drugs Standard Control Organisation", "Central Drug Safety Control Office",
   "Clinical Drugs Standards Committee Organisation", "Central Directorate of Schedule Control Organisation"], 0,
  "The bracket after CDSCO expands it as 'Central Drugs Standard Control Organisation'. (Book p28)")
q(S7, 28, "The step immediately after submitting the NDA to CDSCO is:",
  ["Approval of drug", "Phase V study", "Phase I trial", "Microdosing"], 0,
  "The last step of the approval flow is 'Approval of Drug'. (Book p28)")
q(S7, 28, "Phase V is also called:",
  ["Pharmaco epidemiology", "Postmarketing surveillance", "Therapeutic confirmatory trial",
   "Human pharmacology study"], 0,
  "The phase V heading reads 'Phase V : Pharmaco epidemiology'. (Book p28)")
q(S7, 28, "The aim of phase V is:",
  ["To validate the toxicity claimed in phase IV", "To determine efficacy",
   "To confirm efficacy", "To fix the maximum tolerable dose"], 0,
  "Phase V's aim is stated as 'To validate toxicity claimed in Phase IV'. (Book p28)")
q(S7, 28, "The types of epidemiological studies used in phase V are:",
  ["Case control / cohort study", "Randomized control trial", "Open label study",
   "Microdosing study"], 0,
  "The second bullet of phase V reads 'Epidemiological studies : Case Control / Cohort Study'. (Book p28)")
q(S7, 28, "Which of these correctly orders the phases?",
  ["Phase 0 → I → II → III → IV → V", "Phase I → 0 → II → III → IV → V",
   "Phase 0 → I → III → II → IV → V", "Phase I → II → III → V → IV"], 0,
  "The book presents phase 0 (microdosing) first, then the mandatory phases I-IV, and finally phase V pharmacoepidemiology. (Book p26-28)")

UNITS = [
 (1, 'Drug Schedules in India', [1,18],
  "Indian drug schedules are read off the label: Schedule G carries the caution that the preparation is dangerous except under medical supervision and covers majority drugs such as antihypertensives and antidiabetics; Schedule H needs a registered practitioner's prescription, with Rx (in black) reusable on the same prescription and NRx (in red) for narcotics like codeine and benzodiazepines, issued once to avoid abuse potential; Schedule H1 (introduced in 2013) shows Rx in red and covers antibiotics against resistance; Schedule X shows XRx in red for narcotic/psychotropic drugs (amphetamine, methylphenidate, ketamine, pentobarbital) needing special licence and a register with prescription copy kept 2 years. Schedule P concerns expiry period, Schedule W generic-name marketing and Schedule Y clinical trials, import and manufacture of new drugs."),
 (2, 'Pregnancy Drug Categories', [19,27],
  "Pregnancy categories are ranked by safety A > B > C. Category A has risk absent to the fetus with maximum safety; B lacks human studies but is absent in animals and is safely prescribed; C has no human data with positive teratogenicity in animals; D and X are positive teratogenic in humans, D being used if benefit > risk (valproate in JME) and X being absolutely contraindicated (thalidomide)."),
 (3, 'Types of Drugs', [28,39],
  "Nine drug types are listed: prescription/legend (schedule H), OTC (anything other than schedule G, H, X), orphan drugs for rare diseases with low availability, street/illicit drugs of abuse (cocaine, heroin, methamphetamine), spurious drugs (imitating another drug's name or failing the intended purpose), misbranded drugs (false label information), adulterated drugs (unwanted substance), prototype drugs - the parental/most used drug of a group, e.g. morphine for opioids - and P (personal) drugs chosen on STEP criteria: safety, tolerability, efficacy and price. An orphan receptor is a receptor without a known ligand."),
 (4, 'Drug Development and Preclinical Trials', [40,49],
  "Development starts with non-mandatory preclinical trials in animals, which must be completed before the mandatory human phases I-IV. Preclinical steps are: draft a protocol describing the expectation of the drug and information on animals, submit it to the Animal Ethical Committee (AEC), get permission approved, then conduct the PCT under CPCSEA guidelines. The flow chart then enters clinical trials in humans, phase I being done in normal healthy individuals and later phases in patients."),
 (5, 'Clinical Trials: Prerequisite and Phase 0', [50,58],
  "A clinical trial opens with prerequisites: draft a protocol, submit it to the Human Ethical Committee, obtain approval, then conduct it under GCP (Good Clinical Practice) guidelines. Phase 0 is microdosing with 100 mcg or 1/100th of the normal dose as a radioligand-bound drug in normal healthy volunteers to determine pharmacokinetics and pharmacodynamics; if normal the trial moves to phase I, if abnormal (toxicity/efficacy) the trial is aborted."),
 (6, 'Mandatory Phases of Clinical Trials', [59,90],
  "The mandatory phases table compares the four phases: phase I (human pharmacology and toxicity study) determines toxicity, maximum tolerable dose, pharmacokinetics and pharmacodynamics in 30-100 normal healthy volunteers over 1-2 years in an open design; phase II (therapeutic exploratory trial) determines efficacy in 100-500 patients over 2-3 years by randomized control trial at a unicentric centre, and carries the maximum failure rate; phase III (therapeutic confirmatory trial) confirms efficacy in 500-3000 patients over 3-5 years by RCT/RUCT at multicentric centres; phase IV (postmarketing surveillance) looks for long term/rare ADRs in many thousands of patients in an open design. For toxic drugs such as anti-HIV and anticancer agents phases I and II are done simultaneously in patients, blinded designs are preferred over open in phases II-III, and all multicentric studies are phase III irrespective of population size."),
 (7, 'Approval in Phase III and Phase V', [91,99],
  "The approval pathway runs from IND (Investigational New Drug) through confirming efficacy and safety for use, to a New Drug Application (NDA) submitted to CDSCO - Central Drugs Standard Control Organisation - in New Delhi, and ends with approval of the drug. Phase V is pharmacoepidemiology: its aim is to validate the toxicity claimed in phase IV using epidemiological studies, namely case control or cohort studies."),
]

byid = {}
for i, (sec, page, text, opts, ans, exp) in enumerate(Q, 1):
    byid[i] = {"id": f"PHARM-C9-{i:03d}", "sec": sec, "page": page, "q": text,
               "opts": opts, "ans": ans, "exp": exp}

questions = [byid[i] for i in sorted(byid)]
units = []
for n, title, (a, b), guide in UNITS:
    for i in range(a, b + 1):
        byid[i]["sec"] = title
    units.append({"id": f"PHARM-U9-{n}", "ch": 9, "n": n, "title": title,
                  "sec": f"{title} · p{byid[a]['page']}",
                  "qs": [f"PHARM-C9-{i:03d}" for i in range(a, b + 1)],
                  "guide": guide})

json.dump({"questions": questions, "units": units},
          open("data/ch09.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("questions:", len(questions), "units:", len(units))
for u in units:
    print(" ", u["id"], u["title"], len(u["qs"]), u["sec"])
