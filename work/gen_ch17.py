# -*- coding: utf-8 -*-
import json
CH = 17
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

unit("β3 Agonists for Overactive Bladder", "β3 agonists relax the urinary bladder and are the DOC drug class for overactive bladder or urge incontinence. The listed drugs are mirabegron and vibegron, with vibegron preferred. Mirabegron has more side effects than vibegron, including vascular headache, UTI from urine retention in a relaxed bladder, hypertension and nasopharyngitis; anticholinergic alternatives are darifenacin, solifenacin and trospium.")
q(58, "β3 receptors in this chapter are located mainly on the:", ["Urinary bladder", "SA node", "Prostatic urethra", "Adrenal medulla"], "The β3 agonist section says β3 receptors are in the urinary bladder.")
q(58, "β3 receptor stimulation in the urinary bladder causes:", ["Relaxation", "Contraction", "Miosis", "Increased renin"], "The note says β3 receptors in the urinary bladder cause relaxation.")
q(58, "The β3 agonists listed are:", ["Mirabegron and vibegron", "Formoterol and salmeterol", "Terbutaline and salbutamol", "Olodaterol and vilanterol"], "The β3 agonist drug list includes mirabegron and vibegron.")
q(58, "Among the listed β3 agonists, the preferred drug is:", ["Vibegron", "Mirabegron", "Salbutamol", "Terbutaline"], "Vibegron is marked as preferred.")
q(58, "β3 agonists are DOC for:", ["Overactive bladder or urge incontinence", "Intermittent bronchial asthma", "Hypertensive crisis", "Brittle asthma"], "The use line says DOC for overactive bladder (urge incontinence).")
q(58, "Which β3 agonist has more side effects according to the page?", ["Mirabegron", "Vibegron", "Formoterol", "Salmeterol"], "The side-effect line states mirabegron > vibegron.")
q(58, "A vascular side effect of mirabegron/vibegron listed is:", ["Headache", "Cataract", "Retinal detachment", "Miosis"], "The first listed side effect is vascular headache.")
q(58, "UTI with β3 agonists is attributed to urine retention in a:", ["Relaxed bladder", "Contracted bladder", "Fibrosed urethra", "Dilated pupil"], "The UTI side-effect note says it occurs due to urine retention in relaxed bladder.")
q(58, "Which cardiovascular side effect is listed for β3 agonists?", ["Hypertension", "Severe bradycardia", "AV block only", "Diastolic collapse only"], "Hypertension is side effect number 3 in the β3 list.")
q(58, "Which upper-airway side effect is listed for β3 agonists?", ["Nasopharyngitis", "Laryngospasm", "Epistaxis only", "Bronchial asthma"], "Nasopharyngitis is side effect number 4.")
q(58, "Anticholinergics listed as alternatives in urge incontinence are:", ["Darifenacin, solifenacin and trospium", "Mirabegron, vibegron and ritodrine", "Formoterol, salmeterol and vilanterol", "Epinephrine, norepinephrine and dopamine"], "The note names darifenacin, solifenacin and trospium as anticholinergics used in urge incontinence.")
q(58, "The key therapeutic action of mirabegron/vibegron is best described as:", ["Bladder relaxation for urge incontinence", "Bladder contraction for overflow incontinence", "Bronchial relaxation for COPD only", "α1 vasoconstriction for spinal hypotension"], "The β3 section links urinary bladder relaxation with use as DOC in overactive bladder.")

unit("β2 Agonists: Duration, Asthma/COPD Use and Side Effects", "β2 agonists are grouped by duration: SABA lasts about 4 hours, LABA about 12 hours, and VLABA about 24 hours. Terbutaline is the only adrenergic given subcutaneously, salbutamol can be nebulised for asthma/COPD, formoterol and salmeterol are pMDI twice-daily LABAs used as add-ons with ICS, and olodaterol/vilanterol are once-daily COPD-only VLABAs. Fast-acting β agonists are relievers in intermittent asthma, with formoterol plus ICS as DOC and salbutamol followed by ICS if unaffordable; tremor is the most common side effect, with hypokalemia, hyperglycemia and palpitations also listed.")
q(58, "Short-acting β agonists (SABA) last approximately:", ["4 hours", "12 hours", "24 hours", "2-3 days"], "The SABA branch is labelled about 4 h.")
q(58, "The SABA that is the only adrenergic given by subcutaneous route is:", ["Terbutaline", "Salbutamol", "Formoterol", "Vilanterol"], "Under SABA, terbutaline is noted as the only adrenergic given by SC route.")
q(58, "Salbutamol can be administered via nebulisers for:", ["Bronchial asthma and COPD", "Overactive bladder and BPH", "Narcolepsy and ADHD", "Pheochromocytoma and cheese reaction"], "The salbutamol note says it can be taken via nebulisers for bronchial asthma and COPD.")
q(58, "Long-acting β agonists (LABA) last approximately:", ["12 hours", "4 hours", "24 hours", "One week"], "The LABA branch is labelled about 12 h.")
q(58, "The LABAs listed are:", ["Formoterol and salmeterol", "Terbutaline and salbutamol", "Olodaterol and vilanterol", "Mirabegron and vibegron"], "Under LABA, the two drugs listed are formoterol and salmeterol.")
q(58, "LABAs are given by pMDI at what schedule in the page?", ["BD", "OD", "QID", "Every 5 minutes"], "The LABA use block says used in pMDI BD.")
q(58, "Persistent bronchial asthma in this page is defined by:", ["At least 2 episodes per week", "Less than 2 episodes per week", "One episode per month", "Only nocturnal cough"], "The persistent BA line says ≥2 episodes/week.")
q(58, "For persistent bronchial asthma, the DOC controller drug listed is:", ["Inhaled corticosteroids (ICS)", "LABA monotherapy", "VLABA alone", "Mirabegron"], "The persistent BA line marks ICS as DOC, with LABA as add-on drug.")
q(58, "In persistent bronchial asthma, LABAs are used as:", ["Add-on drugs", "The only DOC monotherapy", "Contraindicated agents", "AChE reactivators"], "A bracket beside persistent BA/COPD marks the β agonists as add-on drugs.")
q(58, "Very-long-acting β agonists (VLABA) last approximately:", ["24 hours", "4 hours", "12 hours", "3-5 minutes"], "The VLABA branch is labelled about 24 h.")
q(58, "The VLABAs listed are:", ["Olodaterol and vilanterol", "Formoterol and salmeterol", "Terbutaline and salbutamol", "Mirabegron and vibegron"], "The VLABA branch lists olodaterol and vilanterol.")
q(58, "VLABAs are used only in:", ["COPD", "Intermittent asthma", "Overactive bladder", "Narcolepsy"], "The VLABA branch says used only in COPD.")
q(58, "The dosing schedule for VLABA pMDI is:", ["OD", "BD", "QID", "Every 5 minutes"], "The VLABA use says pMDI OD.")
q(58, "Fast-acting β agonists are used as relievers in:", ["Intermittent bronchial asthma", "Permanent COPD only", "Hypertensive emergency", "Urge incontinence"], "The box says fast-acting β agonists are used as reliever in intermittent bronchial asthma.")
q(58, "Intermittent bronchial asthma is described here as:", ["Less than 2 episodes per week", "At least 2 episodes per week", "Daily symptoms", "Only nocturnal symptoms"], "The reliever box defines intermittent BA as <2 episodes/week.")
q(58, "The DOC for intermittent bronchial asthma is:", ["Formoterol plus inhaled corticosteroids", "Salbutamol alone always", "Olodaterol alone", "Mirabegron plus vibegron"], "The box says DOC for intermittent BA: formoterol + ICS.")
q(58, "The formoterol plus ICS regimen is delivered by:", ["Pressurised metered-dose inhaler (pMDI)", "Intravenous infusion", "Subcutaneous injection", "Transdermal patch"], "The reliever box writes pMDI beneath formoterol + ICS.")
q(58, "If formoterol plus ICS is unaffordable, the page advises:", ["1 pMDI salbutamol, wait 5 minutes, then 1 pMDI ICS", "Terbutaline IV every 5 minutes", "Olodaterol pMDI QID", "Mirabegron plus vibegron"], "The affordability branch shows 1 pMDI salbutamol → 5 minutes → 1 pMDI ICS.")
q(58, "The interval between salbutamol and ICS in the fallback intermittent asthma regimen is:", ["5 minutes", "30 seconds", "12 hours", "24 hours"], "The arrow between salbutamol and ICS is labelled 5 minutes.")
q(59, "The most common side effect of β2 agonists is:", ["Tremor", "Cataract", "Dementia", "Miosis"], "The side-effect list marks tremor as most common.")
q(59, "Salbutamol is useful in hyperkalemia because β2 agonists can cause:", ["Hypokalemia", "Hyperkalemia", "Hyponatremia", "Hypercalcemia"], "The side-effect list says hypokalemia and notes salbutamol is used for hyperkalemia treatment.")
q(59, "β2 agonists can cause which glucose side effect?", ["Hyperglycemia", "Hypoglycemia", "No glucose change", "Ketonuria only"], "Hyperglycemia is listed as a β agonist side effect.")
q(59, "Which cardiac symptom is listed as a β agonist side effect?", ["Palpitations", "Complete heart block", "Asystole only", "No cardiac symptom"], "Palpitations appear as side effect number 4.")
q(59, "Which side-effect cluster best matches β2 agonists in the notes?", ["Tremor, hypokalemia, hyperglycemia and palpitations", "Miosis, lacrimation, defecation and urination", "Dry mouth, constipation, dementia and urinary retention", "Cataract, iris cyst, glaucoma and brow ache"], "The side-effect list contains tremor, hypokalemia, hyperglycemia and palpitations.")

unit("Indirect Adrenergics, Cheese Reaction and Stimulants", "Indirect adrenergics are norepinephrine displacers: a drug similar to NE enters the neuron, displaces NE from vesicles into the synapse, and produces α/β sympathomimetic stimulation. Intermittent dosing works, but continuous dosing depletes NE and turns into drug failure with sympatholysis. The cheese reaction is tyramine plus MAO-inhibitor physiology, and stimulant examples include methylphenidate, amphetamine and methamphetamine.")
q(59, "Indirect adrenergics are also known as:", ["Norepinephrine displacers", "AChE inhibitors", "Muscarinic blockers", "β3 antagonists"], "The section begins by saying indirect adrenergics are aka norepinephrine displacers.")
q(59, "In the mechanism of indirect adrenergics, the drug is similar to:", ["Norepinephrine", "Acetylcholine", "Histamine", "GABA"], "The mechanism line says drug similar to NE enters the neuron.")
q(59, "After an indirect adrenergic enters the neuron, norepinephrine is displaced from the:", ["Vesicle", "Nucleus", "Postsynaptic receptor", "AChE molecule"], "The mechanism says NE molecule is displaced from vesicle.")
q(59, "Displaced NE enters the:", ["Synaptic space", "Urine", "Aqueous humour", "CSF only"], "The flow sends displaced NE to synaptic space.")
q(59, "The synaptic NE produced by indirect adrenergics stimulates:", ["α and β receptors", "m and N receptors", "Only D2 receptors", "Only H3 receptors"], "The mechanism flow has α, β stimulation after synaptic NE release.")
q(59, "The final pharmacologic effect of indirect adrenergics is:", ["Sympathomimetic effect", "Parasympatholytic effect", "AChE reactivation", "Muscle paralysis"], "The mechanism ends with sympathomimetic effect.")
q(59, "With intermittent dosing of an indirect adrenergic, NE acts on:", ["α and β receptors", "Only m3 receptors", "Only NMJ nicotinic receptors", "Only renal D1 receptors"], "The dosing branch says intermittent dosing → NE acts on α and β receptors.")
q(59, "Intermittent dosing of indirect adrenergics produces:", ["Sympathomimetic effects", "Sympatholysis", "ACh depletion", "Only cholinergic crisis"], "The intermittent dosing branch ends with sympathomimetic effects.")
q(59, "Continuous dosing of indirect adrenergics leads to:", ["Depletion of NE", "Accumulation of ACh", "Increased vesicular NE forever", "Only D1 diuresis"], "The continuous dosing branch says depletion of NE.")
q(59, "NE depletion during continuous dosing causes:", ["Failure of drug and sympatholysis", "Greater sympathomimetic action indefinitely", "Miosis", "AChE ageing"], "The continuous branch ends with failure of drug and sympatholysis.")
q(59, "Norepinephrine is metabolised by:", ["Monoamine oxidase", "Acetylcholinesterase", "Pseudocholinesterase", "Tyrosine hydroxylase"], "The note beneath dosing says NE is metabolised by monoamine oxidase.")
q(59, "Cheese reaction involves food containing:", ["Tyramine", "Histamine", "Pilocarpine", "Atropine"], "The boxed note says tyramine-containing food such as cheese and wine.")
q(59, "Examples of tyramine-containing food in the note are:", ["Cheese and wine", "Milk and rice", "Meat and eggs", "Coffee and tea"], "The note includes cheese and wine as examples.")
q(59, "Tyramine causes cheese reaction by:", ["Displacing NE", "Blocking β receptors", "Activating AChE", "Increasing insulin directly"], "The tyramine branch leads to displacement of NE.")
q(59, "MAO inhibitors in the cheese reaction are identified as:", ["Antidepressants", "Antihistamines", "Anticholinergics", "Antibiotics"], "The patient branch lists MAO inhibitors with antidepressants in parentheses.")
q(59, "When MAO is inhibited, NE is:", ["Not metabolised", "Rapidly destroyed", "Converted to ACh", "Stored only in urine"], "The MAO-inhibitor branch says NE is not metabolised.")
q(59, "Accumulation of NE in cheese reaction produces:", ["Hypertensive crisis", "Hypotensive syncope", "Miosis", "Bronchial relaxation only"], "The final outcome of the cheese reaction flow is hypertensive crisis.")
q(59, "Methylphenidate is DOC for:", ["ADHD", "Obesity", "Brittle asthma", "Overactive bladder"], "The stimulant list states methylphenidate is DOC for ADHD.")
q(59, "Another listed use of methylphenidate is:", ["Narcolepsy", "Anaphylaxis", "Pheochromocytoma", "Glaucoma"], "Under methylphenidate, other use is narcolepsy.")
q(59, "Methylphenidate can worsen:", ["Tics", "Cataract", "BPH", "Diuresis"], "The side effects under methylphenidate include worsens tics.")
q(59, "A second methylphenidate adverse issue listed is:", ["Abuse potential", "Retinal detachment", "Organophosphate ageing", "Urine retention only"], "Abuse potential is listed as a side effect of methylphenidate.")
q(59, "Amphetamine is used in:", ["ADHD, narcolepsy and obesity", "Glaucoma, uveitis and cataract", "PUD, diarrhoea and dysmenorrhoea", "BPH and postural hypotension only"], "The amphetamine use list contains ADHD, narcolepsy and obesity.")
q(59, "Methamphetamine is described as a:", ["Designer drug and drug of abuse", "DOC for ADHD", "β3 agonist", "AChE reactivator"], "The methamphetamine list says designer drug and drug of abuse.")
q(59, "Methamphetamine is also known as:", ["Crystal meth", "Truth serum", "Calabar bean", "Datura"], "The page writes methamphetamine is aka crystal meth.")

unit("ADHD/Narcolepsy Notes and Mixed-Acting Sympathomimetics", "The chapter adds that guanfacine and guanabenz can lower BP through sympatholysis but are contraindicated in pheochromocytoma. For ADHD with a family history of drug abuse, the preferred DOC group is selective NE reuptake inhibitors such as atomoxetine and viloxazine. Narcolepsy drugs include solriamfetol, pitolisant, amphetamine, methylphenidate and modafinil; mixed-acting sympathomimetics stimulate α/β receptors directly and also raise NE levels, with ephedrine, pseudoephedrine and banned norephedrine as the examples.")
q(60, "Guanfacine and guanabenz can treat hypertension by:", ["Sympatholysis", "Direct α1 vasoconstriction", "AChE reactivation", "β3 bladder relaxation"], "The page says guanfacine and guanabenz can be used to treat HTN by sympatholysis.")
q(60, "Guanfacine and guanabenz are contraindicated in:", ["Pheochromocytoma", "Bronchial asthma", "Glaucoma", "Sicca syndrome"], "The line under guanfacine and guanabenz says C/I in pheochromocytoma.")
q(60, "The DOC for ADHD with family history of drug abuse is:", ["Selective NE reuptake inhibitors", "Methylphenidate", "Methamphetamine", "Epinephrine"], "The note states DOC for ADHD with family history of drug abuse: selective NE reuptake inhibitors.")
q(60, "Selective NE reuptake inhibitors listed for ADHD are:", ["Atomoxetine and viloxazine", "Solriamfetol and modafinil", "Guanfacine and guanabenz", "Amphetamine and methamphetamine"], "Atomoxetine and viloxazine are written in parentheses after selective NE reuptake inhibitors.")
q(60, "Solriamfetol is a:", ["Dopamine-NE reuptake inhibitor", "H3 receptor antagonist only", "β3 agonist", "AChE inhibitor"], "The narcolepsy drug list describes solriamfetol as a dopamine-NE reuptake inhibitor.")
q(60, "Pitolisant is described as a receptor antagonist/inverse agonist at:", ["H3 receptors", "β1 receptors", "m3 receptors", "D1 receptors"], "The narcolepsy list identifies pitolisant as an H3 receptor antagonist/inverse agonist.")
q(60, "Which two stimulant drugs are listed among narcolepsy drugs?", ["Amphetamine and methylphenidate", "Epinephrine and norepinephrine", "Mirabegron and vibegron", "Olodaterol and vilanterol"], "The narcolepsy list includes amphetamine and methylphenidate.")
q(60, "Modafinil acts by greatly increasing:", ["Dopamine", "Acetylcholine", "GABA", "Histamine only"], "The modafinil line says ↑↑ dopamine.")
q(60, "Modafinil is DOC for narcolepsy and also for:", ["Obstructive sleep apnea and shift worker disease", "BPH and glaucoma", "Pheochromocytoma and shock", "Tardive dyskinesia and Huntington chorea"], "The arrows from modafinil DOC point to narcolepsy, obstructive sleep apnea and shift worker disease.")
q(60, "Mixed-acting sympathomimetics stimulate:", ["α and β receptors as well as increasing NE levels", "Only m3 receptors", "Only AChE", "Only β3 bladder receptors"], "The mixed-acting section states they stimulate α and β receptors as well as ↑ NE levels.")
q(60, "Ephedrine is described as similar to:", ["Phenylephrine", "Physostigmine", "Mirabegron", "Tetrabenazine"], "The ephedrine line says similar to phenylephrine.")
q(60, "Ephedrine is used for hypotension due to spinal anaesthesia when associated with:", ["Bradycardia", "Tachyarrhythmia only", "Miosis", "Urge incontinence"], "The ephedrine use says hypotension due to spinal anaesthesia with bradycardia.")
q(60, "Ephedrine can produce mydriasis:", ["Without cycloplegia", "With obligatory cycloplegia", "Only after atropine", "By m3 stimulation"], "The ephedrine use list includes mydriasis without cycloplegia.")
q(60, "Ephedrine is also used as a:", ["Nasal decongestant", "β3 agonist", "AChE reactivator", "Miotic agent"], "The ephedrine use list includes nasal decongestant.")
q(60, "Pseudoephedrine is used as an oral:", ["Nasal decongestant", "Bronchodilator for severe asthma", "Antiglaucoma miotic", "Anticholinergic antidote"], "The pseudoephedrine line says nasal decongestant (PO).")
q(60, "Norephedrine is also known as:", ["Phenylpropanolamine", "Dipivefrine", "Droxidopa", "Isoprenaline"], "The norephedrine line gives aka phenylpropanolamine.")
q(60, "Norephedrine was formerly used for obesity but was banned because of increased incidence of:", ["Stroke", "Cataract", "Iris cysts", "Dementia"], "The norephedrine note says it was banned due to increased incidence of stroke.")

unit("Epinephrine Dilutions and Dale's Phenomenon", "The details section turns epinephrine dilutions into route-based facts: 1:1000 for SC/IM/endotracheal, 1:10,000 for IV/intracardiac/intraosseous, 1:100,000 for local vasoconstriction and 1:100,000 or 1:200,000 with local anaesthetic. Dale's phenomenon is the biphasic BP response to epinephrine: high adrenaline reaches the higher-threshold α response to raise BP, while low adrenaline acts on lower-threshold β2 receptors to lower BP. With α blockade the pressor limb is reversed to a pure fall, and with β blockade the response is re-reversed to an unopposed α1 steep rise.")
q(60, "Epinephrine dilution 1:1000 is used by which routes?", ["Subcutaneous, intramuscular and endotracheal", "Intravenous, intracardiac and intraosseous", "Only local vasoconstriction", "Only with local anaesthetic"], "The dilution table lists 1:1000 for subcutaneous, intramuscular and endotracheal use.")
q(60, "Epinephrine dilution 1:10,000 is used by which routes?", ["Intravenous, intracardiac and intraosseous", "Subcutaneous, intramuscular and endotracheal", "Only with local anaesthetic", "Only pMDI"], "The table lists 1:10,000 for intravenous, intracardiac and intraosseous use.")
q(60, "Epinephrine dilution 1:100,000 is used for:", ["Local vasoconstriction", "Intracardiac resuscitation", "Endotracheal delivery", "Oral decongestion"], "The table says 1:100,000 is used in local vasoconstriction.")
q(60, "The purpose of local vasoconstriction with 1:100,000 epinephrine is to prevent:", ["Muscle necrosis", "Mydriasis", "Hyperglycemia", "Cataract"], "The note under 1:100,000 says local vasoconstriction to prevent muscle necrosis.")
q(60, "Epinephrine dilution 1:100,000 or 1:200,000 is used with:", ["Local anaesthetic", "MAO inhibitor", "β3 agonist", "AChE reactivator"], "The fourth dilution column says used with local anaesthetic.")
q(61, "Dale's phenomenon refers to epinephrine causing a:", ["Biphasic blood-pressure pattern", "Single fixed fall in BP", "Pure bradycardia only", "No vascular effect"], "The heading states epinephrine administration leads to a biphasic pattern of BP.")
q(61, "At high concentrations, adrenaline primarily acts on:", ["α receptors", "β2 receptors only", "D1 receptors", "m3 receptors"], "The high concentration branch says acts on α.")
q(61, "High-concentration adrenaline acts on α receptors because their threshold is:", ["Higher", "Lower", "Absent", "Unrelated to concentration"], "The high concentration branch says α acts due to higher threshold.")
q(61, "The high-concentration pressor limb reflects vasoconstriction due to α action minus:", ["β2 vasodilation", "m3 miosis", "D1 diuresis", "AChE activity"], "The high-concentration branch writes vasoconstriction (α) minus vasodilation (β2).")
q(61, "The high-concentration limb of Dale's phenomenon causes:", ["Increased BP", "Decreased BP", "No BP change", "Only urine retention"], "The high-concentration branch ends with increased BP and a curve.")
q(61, "At low concentrations, adrenaline primarily acts on:", ["β2 receptors", "α receptors", "D1 receptors", "Nm receptors"], "The low concentration branch says acts on β2.")
q(61, "Low-concentration β2 action occurs because β2 has a:", ["Lower threshold", "Higher threshold", "Nonexistent threshold", "Threshold only after atropine"], "The low concentration branch says β2 acts due to lower threshold.")
q(61, "Low-concentration adrenaline causes vasodilation and:", ["Decreased BP", "Increased BP", "No change in BP", "Only increased IOP"], "The low concentration branch says vasodilation leads to decreased BP and b curve.")
q(61, "Vasomotor reversal of Dale occurs after epinephrine plus:", ["An α blocker", "A β blocker", "Atropine", "AChE inhibitor"], "The reversal heading says administration of epinephrine plus α blocker.")
q(61, "With α blockade, epinephrine shows only:", ["β2 action with a decline in BP", "α1 action with steep rise in BP", "No receptor action", "D1 action with diuresis"], "The vasomotor reversal note says only β2 action and only decline in BP.")
q(61, "Vasomotor re-reversal of Dale occurs after epinephrine plus:", ["A β-blocker", "An α-blocker", "Pralidoxime", "Mannitol"], "The re-reversal heading says administration of epinephrine plus β-blocker.")
q(61, "With β blockade, epinephrine produces:", ["Unopposed α1 action with a steep rise in BP", "Only β2 vasodilation", "Only no change in BP", "Only diuresis"], "The re-reversal note says unopposed α1 action causes a steep rise in BP.")
q(61, "Systolic BP is directly proportional to cardiac contractility and:", ["Preload", "AChE activity", "Aqueous humour", "miosis"], "The factors section says systolic BP is proportional to cardiac contractility and to preload.")
q(61, "Preload is increased by:", ["Vasoconstriction", "Bronchodilation", "Miosis", "AChE blockade"], "The factors section notes preload is increased by vasoconstriction.")
q(61, "Diastolic BP is proportional to:", ["Tone of peripheral blood vessels", "ACh concentration", "Bladder contraction", "Ciliary accommodation"], "The factors list says diastolic BP is proportional to the tone of peripheral blood vessels.")

unit("Comparing Epinephrine, Norepinephrine and Isoprenaline on BP and HR", "The final table compares α1/β1/β2 epinephrine, α1/β1 norepinephrine and β1/β2 isoprenaline. Norepinephrine gives the greatest mean BP rise but net bradycardia from reflex vagal tone, epinephrine raises mean BP with net tachycardia, and isoprenaline lowers diastolic/mean BP while driving the greatest HR rise with pro-arrhythmic action. Clinically, norepinephrine is preferred for most shock except anaphylaxis, where epinephrine is DOC because β2 bronchodilation matters; atropine blocks vagal reflex bradycardia and is paired with NE in neurogenic hypotension.")
q(62, "The receptor profile of epinephrine in the comparison table is:", ["α1, β1 and β2 stimulation", "α1 and β1 stimulation only", "β1 and β2 stimulation only", "D1 and β1 stimulation"], "The epinephrine column is headed α1, β1, β2 stimulation.")
q(62, "The receptor profile of norepinephrine in the comparison table is:", ["α1 and β1 stimulation", "α1, β1 and β2 stimulation", "β1 and β2 stimulation", "β3 stimulation only"], "The norepinephrine column is headed α1, β1 stimulation.")
q(62, "The receptor profile of isoprenaline is:", ["β1 and β2 stimulation", "α1 and β1 stimulation", "α1, β1 and β2 stimulation", "D1 stimulation only"], "The isoprenaline column is headed β1, β2 stimulation.")
q(62, "Epinephrine increases systolic BP in the table:", ["Markedly", "Not at all", "Always decreases it", "Only after α blockade"], "The systolic BP row under epinephrine has double upward arrows.")
q(62, "Norepinephrine's effect on systolic BP is:", ["Marked increase", "Marked decrease", "No change", "Only transient fall"], "The systolic BP row under norepinephrine has double upward arrows.")
q(62, "Isoprenaline's systolic BP effect is shown as:", ["No change or slight increase", "Marked fall", "Marked rise like norepinephrine", "No possible effect"], "The systolic BP row under isoprenaline is marked no change/slight increase.")
q(62, "Epinephrine's diastolic BP effect in the table is:", ["Increase", "Marked decrease", "No change", "Only biphasic with no net effect"], "The diastolic BP row under epinephrine shows an upward arrow.")
q(62, "Norepinephrine's diastolic BP effect is:", ["Marked increase", "Marked decrease", "No change", "Only a β2 fall"], "The diastolic BP row under norepinephrine has double upward arrows.")
q(62, "Isoprenaline's diastolic BP effect is:", ["Marked decrease", "Marked increase", "No change", "Same as norepinephrine"], "The diastolic BP row under isoprenaline has multiple downward arrows.")
q(62, "The greatest rise in mean BP/tissue perfusion is with:", ["Norepinephrine", "Epinephrine", "Isoprenaline", "Salbutamol"], "The mean BP row shows the largest upward effect in the norepinephrine column.")
q(62, "Isoprenaline changes mean BP by:", ["Decreasing it", "Greatly increasing it", "Leaving it unchanged", "Increasing it more than norepinephrine"], "The mean BP row under isoprenaline has downward arrows.")
q(62, "The direct β-mediated heart-rate effect of epinephrine is:", ["Increase", "Decrease", "No change", "Only reflex bradycardia"], "The HR direct row under epinephrine shows upward arrows.")
q(62, "The direct β-mediated heart-rate effect of norepinephrine is:", ["Increase", "Decrease", "No change", "Only blocked by atropine"], "The HR direct row under norepinephrine shows an upward arrow.")
q(62, "The direct β-mediated heart-rate effect of isoprenaline is:", ["Increase", "Decrease", "No change", "Only α1-mediated"], "The HR direct row under isoprenaline shows upward arrows.")
q(62, "The reflex heart-rate effect from vessel tone with norepinephrine is:", ["Decrease", "Increase", "No change", "Only β2 tachycardia"], "The HR reflex row under norepinephrine has downward arrows.")
q(62, "The net heart-rate effect of norepinephrine is:", ["Decrease", "Increase", "No change", "Massive tachycardia"], "The HR net row under norepinephrine has a downward arrow.")
q(62, "The net heart-rate effect of epinephrine is:", ["Increase", "Decrease", "No change", "Only bradycardia"], "The HR net row under epinephrine has an upward arrow.")
q(62, "The net heart-rate effect of isoprenaline is:", ["Very large increase with pro-arrhythmic action", "Decrease", "No change", "Only reflex bradycardia"], "The isoprenaline net HR cell has multiple upward arrows and notes pro-arrhythmic action.")
q(62, "In the mean BP graph, curve a represents:", ["Norepinephrine", "Epinephrine", "Isoprenaline", "Dopamine"], "The mean BP graph labels curve a as NE.")
q(62, "In the mean BP graph, curve b represents:", ["Epinephrine", "Norepinephrine", "Isoprenaline", "Dobutamine"], "The mean BP graph labels curve b as epinephrine.")
q(62, "In the mean BP graph, curve c represents:", ["Isoprenaline", "Norepinephrine", "Epinephrine", "Phenylephrine"], "The mean BP graph labels curve c as isoprenaline.")
q(62, "In the HR graph, curve a represents:", ["Isoprenaline", "Epinephrine", "Norepinephrine", "Dopamine"], "The HR graph labels curve a as isoprenaline.")
q(62, "In the HR graph, curve b represents:", ["Epinephrine", "Isoprenaline", "Norepinephrine", "Salbutamol"], "The HR graph labels curve b as epinephrine.")
q(62, "In the HR graph, curve c represents:", ["Norepinephrine", "Epinephrine", "Isoprenaline", "Droxidopa"], "The HR graph labels curve c as NE.")
q(62, "The preferred treatment for shock, except anaphylactic shock, is:", ["Norepinephrine", "Isoprenaline", "Salbutamol", "Mirabegron"], "The note says norepinephrine is preferred treatment for shock except anaphylactic shock.")
q(62, "The DOC in anaphylactic shock is:", ["Epinephrine", "Norepinephrine", "Isoprenaline", "Dobutamine"], "The note says anaphylactic shock DOC is epinephrine.")
q(62, "Epinephrine is DOC in anaphylaxis because it adds:", ["β2 bronchodilation", "β3 bladder relaxation", "Pure α2 sympatholysis", "AChE inhibition"], "The note explains epinephrine is DOC due to added bronchodilation from β2 action.")
q(62, "Epinephrine/NE can reduce HR reflexly due to:", ["Vagal stimulation", "AChE ageing", "β3 activation", "Dopamine depletion"], "The note says vagal stimulation causes reflex decrease in HR due to epinephrine/NE administration.")
q(62, "If vagal effects are blocked by atropine or the heart is transplanted, NE administration causes only:", ["Increased HR", "Decreased HR", "No HR change", "Miosis"], "The note says blockade of vagal effect due to atropine/transplanted heart leads to NE administered → only ↑ HR.")
q(62, "In neurogenic hypotension, norepinephrine is combined with atropine to counteract:", ["Bradycardia", "Bronchospasm", "Urine retention", "Hyperglycemia"], "The final note says neurogenic hypotension: NE + atropine to counteract bradycardia.")

end()
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
