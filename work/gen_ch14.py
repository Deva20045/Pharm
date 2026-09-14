# -*- coding: utf-8 -*-
import json
CH = 14
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

unit("Anticholinergic Drugs: Classification and Nicotinic Blockers", "Anticholinergic drugs are parasympatholytics and are direct acting. They include muscarinic blockers and nicotinic blockers; nicotinic blockers are further separated into Nm muscular blockers and Nn neuronal or ganglionic blockers. Nm blockers relax skeletal muscle at the NMJ, whereas ganglionic blockers reduce sympathetic post-ganglionic norepinephrine release, producing vasodilation, antihypertensive action and postural hypotension.")
q(48, "Anticholinergic drugs are also called:", ["Parasympatholytics", "Parasympathomimetics", "Sympathomimetics", "Cholinesterase reactivators"], "The chapter classification labels anticholinergic drugs as parasympatholytics.")
q(48, "The classification diagram describes parasympatholytics as:", ["Direct acting", "Indirect acting only", "AChE blockers", "Norepinephrine displacers"], "The heading under parasympatholytics explicitly says direct acting.")
q(48, "The two major branches of direct anticholinergic drugs are:", ["Muscarinic blockers and nicotinic blockers", "α blockers and β blockers", "Amides and choline esters", "SABAs and LABAs"], "The diagram splits parasympatholytics into muscarinic blockers and nicotinic blockers.")
q(48, "Nicotinic blockers are divided into:", ["Muscular Nm blockers and neuronal Nn blockers", "m1 and m3 blockers", "β1 and β2 blockers", "D1 and D2 blockers"], "The nicotinic branch splits into muscular Nm blockers and neuronal Nn blockers.")
q(48, "Neuronal nicotinic blockers are also called:", ["Ganglionic blockers", "Muscle relaxants", "Miotic agents", "Bronchodilators"], "The Nn blocker branch is labelled neuronal Nn blockers, with ganglionic blockers in parentheses.")
q(48, "Nm blockers act at the:", ["Neuromuscular junction", "Autonomic ganglion only", "Adrenal cortex", "Renal JG cell"], "The Nm blocker MOA says they block at NMJ.")
q(48, "The final effect of Nm blockers is:", ["Muscle relaxation", "Increased salivation", "Bronchoconstriction", "Hypertension"], "The Nm blocker line states blockade at NMJ relaxes muscles.")
q(48, "The Nm-blocking drugs listed here are:", ["Non-depolarising muscle relaxants", "Depolarising muscle relaxants", "β3 agonists", "AChE inhibitors"], "The drug line under Nm blockers reads non-depolarising muscle relaxants (NDMR).")
q(48, "Which NDMR is listed under Nm blockers?", ["Atracurium", "Atropine", "Mecamylamine", "Trimethaphan"], "Atracurium is one of the listed Nm-blocking NDMRs.")
q(48, "Which second NDMR is listed under Nm blockers?", ["Mivacurium", "Pilocarpine", "Physostigmine", "Droxidopa"], "Mivacurium is the other NDMR listed under Nm blockers.")
q(48, "Ganglionic blockers reduce release of which sympathetic post-ganglionic transmitter?", ["Norepinephrine", "Acetylcholine at NMJ", "Dopamine in the corpus striatum", "Histamine"], "The Nn/ganglionic blocker MOA says sympathetic post-ganglionic norepinephrine release decreases.")
q(48, "The fall in norepinephrine after ganglionic blockade produces:", ["Vasodilation", "Vasoconstriction", "Miosis", "Hyperglycemia"], "The pathway shows decreased norepinephrine release leading to vasodilation.")
q(48, "Ganglionic blockers are described as which-line treatment for hypertension?", ["Second-line", "First-line", "Contraindicated in all cases", "Only emergency first-line oral"], "The MOA line says vasodilation and second-line treatment of hypertension.")
q(48, "The characteristic side effect of ganglionic blockers listed is:", ["Postural hypotension", "Retinal detachment", "Cataract", "UTI"], "The side-effect line for Nn/ganglionic blockers states postural hypotension.")
q(48, "Mecamylamine is administered by which route?", ["Oral", "Intravenous only", "Transdermal only", "Intrathecal"], "The table lists oral as the route of administration for mecamylamine.")
q(48, "Mecamylamine is used as second-line treatment for:", ["Mild/moderate hypertension", "Acute CHF", "Brittle asthma", "Angle closure glaucoma"], "The mecamylamine use list includes mild/moderate hypertension as second-line Rx.")
q(48, "Which neuropsychiatric condition is listed as a use of mecamylamine?", ["Tourette syndrome", "Narcolepsy", "Myasthenia gravis", "Alzheimer's disease"], "Tourette syndrome is included in the mecamylamine uses.")
q(48, "With nicotine, mecamylamine can be used to prevent:", ["Peripheral side effects in smoking dependence", "Central abstinence symptoms only", "Acute angle closure glaucoma", "Cataract"], "The mecamylamine use states prevention of peripheral side effects in smoking dependence along with nicotine.")
q(48, "Trimethaphan is administered:", ["Intravenously", "Orally", "By pMDI", "Subcutaneously"], "The route column for trimethaphan shows IV.")
q(48, "Trimethaphan is used in:", ["Hypertensive emergency", "Motion sickness", "Urge incontinence", "Narcolepsy"], "The trimethaphan row gives hypertensive emergency as the use.")
q(48, "Tetraethylammonium is noted as a:", ["K+ channel blocker in animal experiments", "DOC for hypertension", "Preferred antiglaucoma drug", "Transdermal antiemetic"], "The tetraethylammonium row says K+ channel blocker in animal experiments.")

unit("Muscarinic Blockers: CNS, Eyes and Oropharynx", "Muscarinic blockade in the CNS decreases cognition; scopolamine is remembered as a truth serum, an alternate narcoanalysis drug and the DOC for motion sickness as a transdermal patch. In the eye, muscarinic blockers cause passive mydriasis and cycloplegia; short-acting drops are used in adults, whereas potent atropine ointment is used in children and for uveitis-related indications. Glycopyrrolate decreases oropharyngeal secretions as a quaternary amine that does not cross the BBB, making it useful before anaesthesia to prevent aspiration.")
q(49, "The CNS effect of muscarinic receptor blockers is:", ["Decreased cognition", "Increased cognition", "Muscle relaxation only", "Increased salivation"], "In the CNS row, the effect column reads decreased cognition.")
q(49, "The muscarinic blocker labelled as truth serum is:", ["Scopolamine", "Atropine", "Tropicamide", "Glycopyrrolate"], "The CNS drug cell lists scopolamine and notes truth serum.")
q(49, "At high doses, scopolamine is an alternate drug for:", ["Narcoanalysis", "Bronchial challenge testing", "Tensilon testing", "Dale's phenomenon"], "The use cell says alternate drug for narcoanalysis at increased doses.")
q(49, "The DOC for narcoanalysis, preferred for better safety and efficacy, is:", ["Thiopentone", "Scopolamine", "Atropine", "Hyoscine patch"], "The narcoanalysis note says DOC: thiopentone, with better safety and efficacy.")
q(49, "Scopolamine is DOC for motion sickness when given as a:", ["Transdermal patch", "Intravenous bolus", "Eye drop", "Nebulised solution"], "The CNS use cell lists motion sickness (DOC): transdermal patch.")
q(49, "The eye effects of muscarinic blockers include:", ["Passive mydriasis and cycloplegia", "Miosis and accommodation spasm", "Retinal detachment and cataract only", "Bronchoconstriction and lacrimation"], "The eye effect column lists passive mydriasis and cycloplegia.")
q(49, "Cycloplegia means:", ["Paralysis of accommodation", "Pupil contraction", "Increased lacrimation", "Eyelid retraction"], "The table defines cycloplegia in parentheses as paralysis of accommodation.")
q(49, "The shortest-acting ocular antimuscarinic drop is:", ["Tropicamide", "Atropine", "Homatropine", "Cyclopentolate"], "The eye-drop list marks tropicamide as shortest acting.")
q(49, "Tropicamide is used especially in:", ["Adults", "Children", "Neonates only", "Pregnancy-induced hypertension"], "The note beside tropicamide says it is used in adults.")
q(49, "Which other ocular antimuscarinic drops are listed with tropicamide?", ["Cyclopentolate and homatropine", "Pilocarpine and carbachol", "Darifenacin and solifenacin", "Ipratropium and tiotropium"], "The eye-drop list includes cyclopentolate and homatropine.")
q(49, "Eye-drop muscarinic blockers are used for:", ["Ocular fundus examination and refraction testing", "Bronchial asthma and COPD", "Peptic ulcer disease and dysmenorrhoea", "Hypertensive emergency and Tourette syndrome"], "The uses column for eye drops lists ocular fundus examination and refraction testing.")
q(49, "A major ocular side effect of antimuscarinic mydriasis is:", ["Acute angle closure glaucoma", "Miosis", "Increased trabecular outflow", "Pinpoint pupils"], "The side-effect column lists acute angle closure glaucoma.")
q(49, "Muscarinic eye blockers are contraindicated in:", ["Glaucoma", "Myasthenia gravis", "Narcolepsy", "Obesity"], "The eye side-effect column writes C/I in glaucoma.")
q(49, "The 1% ointment antimuscarinic used in children is:", ["Atropine", "Tropicamide", "Cyclopentolate", "Homatropine"], "The lower eye drug cell says 1% ointment: atropine, most potent and used in children.")
q(49, "Atropine eye ointment is described as the:", ["Most potent", "Shortest acting", "Least potent", "Only β3 agonist"], "Atropine ointment is labelled most potent.")
q(49, "Atropine ointment is used in corneal ulcer or uveitis to prevent:", ["Synechiae formation", "Bronchoconstriction", "Urine retention", "NE release"], "The use cell says corneal ulcer/uveitis: prevent synechiae formation.")
q(49, "In iridocyclitis, atropine helps by:", ["Decreasing pain", "Increasing salivation", "Inducing bronchospasm", "Treating tics"], "The lower eye use cell includes iridocyclitis: decreased pain.")
q(49, "The oropharyngeal effect of muscarinic blockers is:", ["Decreased secretions", "Increased secretions", "Bronchoconstriction", "Miosis"], "The oropharynx row effect column reads decreased secretions.")
q(49, "The oropharyngeal antimuscarinic drug listed is:", ["Glycopyrrolate", "Scopolamine", "Tropicamide", "Pirenzepine"], "The oropharynx row drug cell lists glycopyrrolate.")
q(49, "Glycopyrrolate is a quaternary amine, so it:", ["Does not cross the BBB", "Readily crosses the BBB", "Is a catecholamine", "Is an AChE reactivator"], "The glycopyrrolate note says quaternary amine and does not cross BBB.")
q(49, "The pre-anaesthetic use of glycopyrrolate is to prevent:", ["Aspiration", "Retinal detachment", "Tardive dyskinesia", "Hyperkalemia"], "The oropharynx use cell states preanaesthetic medication to prevent aspiration.")
q(49, "Which glaucoma-contraindicated drug class is specifically listed in the note?", ["Tricyclic antidepressants such as amitriptyline", "β3 agonists such as vibegron", "Oximes such as pralidoxime", "AChE inhibitors such as neostigmine"], "The note lists tricyclic antidepressants, with amitriptyline in parentheses.")
q(49, "Which antipsychotic group is listed among drugs contraindicated in glaucoma?", ["Typical and atypical antipsychotics", "Only phenothiazines", "Only atypicals", "None of the antipsychotics"], "The glaucoma note lists typical/atypical antipsychotics.")
q(49, "Which antiparkinsonian drug is listed as contraindicated in glaucoma due to mydriasis?", ["Levodopa", "Bromocriptine", "Selegiline", "Amantadine"], "The glaucoma note also lists levodopa.")

unit("Pulmonary Antimuscarinics, Inhalation Devices and Paradoxical Bronchoconstriction", "Antimuscarinics in the lung cause bronchodilation and are classified by duration into SAMA, IAMA and LAMA. Ipratropium is the short-acting QID drug, tiotropium is DOC in COPD, and long-acting agents are add-on drugs in asthma or COPD. They are delivered by inhalation through pMDI or nebuliser, but paradoxical bronchoconstriction can occur from hypotonic solution, bromide or presynaptic m2 blockade that increases ACh and stimulates postsynaptic m3.")
q(49, "The pulmonary effect of muscarinic receptor blockers is:", ["Bronchodilation", "Bronchoconstriction", "Miosis", "Gastric acid secretion"], "The lung row effect column reads bronchodilation.")
q(49, "SAMA stands for:", ["Short-acting muscarinic antagonist", "Selective adrenal medullary agonist", "Slow acting muscarinic agonist", "Short-acting methylxanthine antagonist"], "The drug column expands SAMA as short acting muscarinic antagonist.")
q(49, "The SAMA listed is:", ["Ipratropium", "Tiotropium", "Oxitropium", "Aclidinium"], "The SAMA line says QID: ipratropium.")
q(49, "Ipratropium is dosed in the table as:", ["QID", "BD", "OD", "Single annual dose"], "The ipratropium line is marked QID.")
q(49, "IAMA stands for:", ["Intermediate-acting muscarinic antagonist", "Inhaled adrenergic muscarinic agonist", "Irreversible antimuscarinic antagonist", "Intravenous anti-migraine agent"], "The table expands IAMA as intermediate acting muscarinic antagonist.")
q(49, "Which drugs are listed as IAMA agents?", ["Oxitropium and aclidinium", "Tiotropium and umeclidinium", "Ipratropium and revefenacin", "Darifenacin and solifenacin"], "The IAMA line lists oxitropium and aclidinium.")
q(49, "IAMA agents are dosed:", ["BD", "QID", "OD", "Every 2 to 3 days"], "The IAMA line is labelled BD.")
q(49, "LAMA stands for:", ["Long-acting muscarinic antagonist", "Local anaesthetic muscarinic antagonist", "Long-acting methylxanthine antagonist", "Low-affinity muscarinic agonist"], "The table expands LAMA as long acting muscarinic antagonist.")
q(49, "The DOC antimuscarinic for COPD is:", ["Tiotropium", "Ipratropium", "Oxitropium", "Tropicamide"], "The COPD use cell says DOC: tiotropium.")
q(49, "Long-acting muscarinic antagonists are dosed:", ["OD", "QID", "BD", "Every 5 minutes"], "The LAMA line marks OD dosing.")
q(49, "Which newer/latest LAMA drugs are listed?", ["Umeclidinium and revefenacin", "Cyclopentolate and homatropine", "Mecamylamine and trimethaphan", "Pirenzepine and telenzepine"], "The LAMA list includes umeclidinium and revefenacin as latest drugs.")
q(49, "In bronchial asthma, inhaled antimuscarinics are used as:", ["Add-on drugs", "The only DOC reliever", "Contraindicated drugs", "Anticholinesterase antidotes"], "The lung use cell says bronchial asthma: add-on drugs.")
q(49, "In COPD, antimuscarinics treat bronchoconstriction due to:", ["Parasympathetic overactivity", "Dopamine depletion", "β2 overactivity", "m3 blockade"], "The COPD use explains treatment of bronchoconstriction due to parasympathetic overactivity.")
q(49, "The reversible component of COPD bronchoconstriction is contrasted with which irreversible component?", ["Fibrosis/sclerosis", "Miosis", "Dementia", "Cataract"], "The COPD note contrasts reversible parasympathetic overactivity with irreversible fibrosis/sclerosis.")
q(49, "A common local side effect of pMDI antimuscarinic bronchodilators is:", ["Dry mouth", "Involuntary salivation", "Miosis", "Hypoglycemia"], "The lung side-effect column lists dry mouth with pMDI.")
q(49, "Inhaled antimuscarinics can worsen:", ["BPH", "Myasthenic crisis", "Tardive dyskinesia", "Acute CHF"], "The lung side-effect column also states worsen BPH.")
q(50, "The route of administration for bronchodilation shown is:", ["Inhalation", "Intrathecal", "Oral only", "Intra-articular"], "The line at the top of the page states route for bronchodilation: inhalation.")
q(50, "A pressurised metered dose inhaler contains a canister with:", ["Drug plus gas (HFA)", "Only dry powder", "Only oxygen", "AChE reactivator solution"], "The pMDI diagram labels the canister as drug plus gas, HFA.")
q(50, "Correct pMDI technique requires release of drug to coincide with:", ["Inspiration", "Expiration", "Swallowing", "Coughing after exhalation"], "The diagram shows release of drug should coincide with inspiration.")
q(50, "The nebuliser image is labelled for which drug?", ["Ipratropium", "Tropicamide", "Pirenzepine", "Atropine ointment"], "The nebuliser is labelled 'Nebulizer: Ipratropium'.")
q(50, "Inhalable mist is shown as useful in acute exacerbation of:", ["Asthma/COPD", "Glaucoma", "Peptic ulcer disease", "Tourette syndrome"], "The nebuliser diagram labels inhalable mist in acute exacerbation of asthma/COPD.")
q(50, "The paradoxical airway side effect of inhaled antimuscarinics is:", ["Paradoxical bronchoconstriction", "Paradoxical miosis", "Paradoxical urination", "Paradoxical hypoglycemia"], "The side-effect bullet states paradoxical bronchoconstriction.")
q(50, "Paradoxical bronchoconstriction from solution tonicity is avoided by using:", ["Isotonic solution", "Hypotonic solution", "Hypertonic saline only", "Distilled water"], "The cause list says hypotonic solution is avoided with isotonic solution.")
q(50, "Bromide is listed as a cause of:", ["Paradoxical bronchoconstriction", "Mydriasis without cycloplegia", "Cholinergic crisis", "Acute CHF"], "Bromide appears under the causes of paradoxical bronchoconstriction.")
q(50, "Presynaptic m2 autoreceptor blockade increases ACh, which then stimulates postsynaptic:", ["m3 receptors", "β3 receptors", "D1 receptors", "Nm receptors"], "The mechanism says blocking presynaptic m2 increases ACh and stimulates postsynaptic m3.")

unit("Muscarinic Blockers: Heart and GIT", "Atropine increases heart rate and AV conduction and is the DOC for conduction blocks such as digoxin toxicity and for bradycardia when the dose is at least 0.5 mg. Very low IV doses can paradoxically slow the heart through presynaptic muscarinic blockade. In the GIT, m1 blockers such as pirenzepine and telenzepine are obsolete anti-secretory drugs, while antispasmodics such as glycopyrrolate, dicyclomine and hyoscine reduce contraction and relieve abdominal pain or motion sickness.")
q(50, "The cardiac effect of atropine is:", ["Increased heart rate and increased AV conduction", "Decreased heart rate and decreased AV conduction", "Only decreased AV conduction", "No effect on heart rate"], "The heart effect column lists ↑ heart rate and ↑ AV conduction.")
q(50, "Atropine is DOC for conduction blocks such as:", ["Digoxin toxicity", "β3 agonist toxicity", "Pilocarpine toxicity only", "Cocaine dependence"], "The heart use cell says conduction blocks (DOC), e.g. digoxin toxicity.")
q(50, "The atropine dose threshold mentioned for treating bradycardia is:", ["At least 0.5 mg", "Less than 0.5 mg", "5 micrograms", "50 micrograms"], "The bradycardia use is marked ≥0.5 mg.")
q(50, "The IV atropine dose schedule shown is:", ["1 mg IV repeated in 3-5 minutes up to 3 mg", "0.1 mg IV once only", "5 mg IV every hour up to 50 mg", "1 pMDI every 5 minutes"], "The dosing cell states 1 mg IV, repeat in 3-5 minutes, up to 3 mg.")
q(50, "An IV atropine dose below 0.5 mg can cause:", ["Paradoxical bradycardia", "Paradoxical bronchoconstriction", "Acute angle closure glaucoma only", "Dementia"], "The heart side-effect cell says <0.5 mg IV dose can cause paradoxical bradycardia.")
q(50, "The mechanism of low-dose atropine paradoxical bradycardia shown is blockade of:", ["Presynaptic muscarinic autoreceptor", "β1 receptor in SA node", "Nicotinic Nm receptor", "D1 receptor"], "The side-effect mechanism labels presynaptic muscarinic blockade leading to paradoxical bradycardia.")
q(50, "Muscarinic blockers in the GIT decrease:", ["HCl secretion", "Renin release", "Norepinephrine reuptake", "Pulmonary surfactant"], "The first GIT effect row says ↓ HCl secretion.")
q(50, "The obsolete m1 blockers for peptic ulcer disease are:", ["Pirenzepine and telenzepine", "Atropine and scopolamine", "Darifenacin and solifenacin", "Ipratropium and tiotropium"], "The GIT acid row lists m1 blockers pirenzepine and telenzepine and brackets them as obsolete.")
q(50, "Pirenzepine and telenzepine were used for:", ["Peptic ulcer disease", "Motion sickness", "Urge incontinence", "Hypertensive emergency"], "The use column beside m1 blockers says peptic ulcer disease.")
q(50, "The antispasmodic effect of antimuscarinics in the GIT is:", ["Decreased contraction", "Increased contraction", "Increased HCl secretion", "Increased insulin release"], "The lower GIT effect row reads ↓ contraction.")
q(50, "Which drugs are listed as antispasmodics?", ["Glycopyrrolate, dicyclomine and scopolamine", "Pirenzepine, telenzepine and atropine ointment", "Ipratropium, oxitropium and tiotropium", "Darifenacin, solifenacin and trospium"], "The antispasmodic drug list contains glycopyrrolate, dicyclomine and scopolamine (hyoscine).")
q(50, "GIT antispasmodics are used to relieve abdominal pain in:", ["Infectious diarrhoea and dysmenorrhoea", "COPD and asthma", "Pheochromocytoma and CHF", "Tardive dyskinesia and Huntington disease"], "The use cell says to relieve abdomen pain in infectious diarrhoea and dysmenorrhea.")
q(50, "Hyoscine is another name for:", ["Scopolamine", "Atropine", "Tropicamide", "Darifenacin"], "The antispasmodic list writes scopolamine (hyoscine).")
q(50, "Hyoscine for motion sickness is given as a:", ["Transdermal patch", "Nebulised mist", "Intracardiac injection", "Eye ointment only"], "The hyoscine use cell says transdermal patch used for motion sickness.")
q(50, "Hyoscine patch absorption is:", ["Slow", "Instantaneous", "Absent through skin", "Only oral"], "The patch note says lipid soluble with slow absorption.")
q(50, "Because hyoscine absorption is slow, it should be administered:", ["4-5 hours before travel, often the night before", "Only after symptoms start", "Every 5 minutes during travel", "Only after meals"], "The table says administer before 4-5 hours, night before travel.")
q(50, "A hyoscine patch is long acting and is reapplied every:", ["2-3 days", "2-3 hours", "3-5 minutes", "Once monthly"], "The hyoscine note states long acting: reapply 2-3 days.")

unit("Muscarinic Blockers Acting on Bladder", "Bladder antimuscarinics reduce detrusor contraction and treat urge incontinence. Selective m3 blockers such as darifenacin and solifenacin are contrasted with trospium, a quaternary amine useful when Alzheimer's disease is present because it does not cross the BBB. Non-selective drugs such as oxybutynin, tolterodine, flavoxate and fesoterodine can block brain m1 receptors and cause dementia on long-term use.")
q(51, "The bladder effect of muscarinic blockers is:", ["Decreased contraction", "Increased contraction", "Increased urine formation", "Increased salivation"], "The bladder table effect column says ↓ contraction.")
q(51, "Selective bladder m3 blockers have selectivity:", ["m3 > m1", "m1 > m3", "m2 only", "Nn > Nm"], "The selective m3 cell states m3 > m1.")
q(51, "Which selective m3 blockers are listed for bladder overactivity?", ["Darifenacin and solifenacin", "Trospium and flavoxate", "Oxybutynin and tolterodine", "Mirabegron and vibegron"], "The selective m3 drug list contains darifenacin and solifenacin.")
q(51, "Darifenacin and solifenacin are used for:", ["Urge incontinence or overactive bladder", "Overflow incontinence due to bladder atony", "Post-operative urine retention", "Peptic ulcer disease"], "The use column for selective m3 drugs states urge incontinence (overactive bladder).")
q(51, "The DOC drug class paired with overactive bladder in the table is:", ["β3 agonists", "β1 blockers", "AChE reactivators", "Ganglionic blockers"], "The use cell lists β3 agonists (DOC) for overactive bladder.")
q(51, "The β3 agonists listed as DOC for urge incontinence are:", ["Mirabegron and vibegron", "Darifenacin and solifenacin", "Flavoxate and tolterodine", "Pirenzepine and telenzepine"], "The table lists mirabegron/vibegron after β3 agonists (DOC).")
q(51, "Trospium is a:", ["Quaternary amine", "Tertiary amine", "Catecholamine", "Organophosphate"], "The trospium cell says quaternary amine.")
q(51, "Trospium does not cross the BBB and is useful in urge incontinence with:", ["Alzheimer's disease", "Asthma", "Glaucoma", "Pheochromocytoma"], "The trospium row notes not crossing BBB and the use is urge incontinence plus Alzheimer's.")
q(51, "Which drugs are listed as non-selective bladder antimuscarinics?", ["Flavoxate, fesoterodine, oxybutynin and tolterodine", "Darifenacin, solifenacin and trospium only", "Ipratropium, oxitropium and aclidinium", "Tropicamide, cyclopentolate and homatropine"], "The non-selective list contains flavoxate, fesoterodine, oxybutynin and tolterodine.")
q(51, "Long-term non-selective bladder antimuscarinics can cause dementia by blocking:", ["m1 receptors in the brain", "m3 receptors in bladder only", "β3 receptors in bladder", "Nn receptors in ganglia"], "The side-effect cell says m1 block in brain leads to dementia on long-term use.")
q(51, "For an elderly patient with overactive bladder and Alzheimer's disease, the table points toward:", ["Trospium", "Oxybutynin", "Tolterodine", "Flavoxate"], "Trospium is highlighted as quaternary, not crossing BBB, and useful in urge incontinence plus Alzheimer's.")
q(51, "Which statement best distinguishes the bladder drugs in this table?", ["Selective m3 blockers and trospium treat urge incontinence, while non-selective brain m1 blockade risks dementia", "All bladder drugs freely cross the BBB and are preferred in Alzheimer's", "β3 agonists cause detrusor contraction", "Darifenacin and solifenacin are non-selective m1 blockers"], "The table separates selective m3 drugs and trospium from non-selective agents whose brain m1 blockade may cause dementia.")

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
