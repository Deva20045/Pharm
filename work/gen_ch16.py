# -*- coding: utf-8 -*-
import json
CH = 16
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

unit("Adrenergic Drugs: Classification", "Adrenergic drugs are sympathomimetics. They can act directly on α and β receptors or indirectly by increasing norepinephrine, which then stimulates α and β receptors. Direct agents are divided into catecholamines and non-catecholamines; catecholamines may be endogenous or exogenous, while non-catecholamines include α-agonists and β-agonists.")
q(56, "Adrenergic drugs are also called:", ["Sympathomimetics", "Parasympathomimetics", "Parasympatholytics", "Cholinesterase inhibitors"], "The classification heading writes adrenergics with sympathomimetics in parentheses.")
q(56, "Direct adrenergic drugs act on:", ["α and β receptors", "m and N receptors", "AChE", "VMAT2 only"], "The direct branch states act on α and β receptors.")
q(56, "Indirect adrenergic drugs increase which neurotransmitter?", ["Norepinephrine", "Acetylcholine", "Histamine", "GABA"], "The indirect branch says ↑ norepinephrine leading to α and β receptor stimulation.")
q(56, "Direct adrenergic drugs are divided into:", ["Catecholamines and non-catecholamines", "Amides and choline esters", "SAMA and LAMA", "Tertiary and quaternary amines"], "The direct branch of the diagram splits into catecholamines and non-catecholamines.")
q(56, "Catecholamines in this classification are subdivided into:", ["Endogenous and exogenous", "α1 and α2", "β1 and β2", "Short and long acting only"], "The catecholamine branch divides into endogenous and exogenous.")
q(56, "Non-catecholamine direct adrenergic drugs include:", ["α-agonists and β-agonists", "Only dopamine agonists", "Only AChE blockers", "Organophosphates and oximes"], "The non-catecholamine branch splits into α-agonist and β-agonist.")

unit("Endogenous Catecholamines: Epinephrine", "Epinephrine is the endogenous catecholamine that acts on α, β1 and β2 receptors and is a stronger cardiac stimulant than norepinephrine. It is DOC in cardiac arrest, anaphylactic shock and brittle asthma, with different dilutions/routes for cardiac arrest versus anaphylaxis. Other uses are prolonging local anaesthesia through vasoconstriction and glaucoma therapy with dipivefrine preferred; conjunctival pigmentation is linked to tyrosine, the common melanin precursor.")
q(56, "Epinephrine acts on:", ["α, β1 and β2 receptors", "Only α1 receptors", "Only β1 receptors", "Only D1 receptors"], "Under epinephrine, the page lists action on α, β1 and β2.")
q(56, "Compared with norepinephrine, epinephrine is a more potent:", ["Cardiac stimulator", "Vasoconstrictor only", "Miotic agent", "VMAT2 inhibitor"], "The epinephrine column states it is a more potent cardiac stimulator than NE.")
q(56, "Epinephrine is DOC in cardiac arrest with:", ["Non-shockable rhythm", "Mild hypertension", "Urge incontinence", "Benign prostatic hyperplasia"], "The first DOC use under epinephrine is cardiac arrest with non-shockable rhythm.")
q(56, "The route/dilution of epinephrine for cardiac arrest shown is:", ["IV, 1:10,000", "IM, 1:1000", "Oral, 1:100,000", "Topical, 1:200,000"], "The cardiac arrest line states IV with 1:10,000.")
q(56, "Epinephrine is DOC in anaphylactic shock by which route/dilution?", ["IM, 1:1000", "IV, 1:10,000", "Oral, 1:1000", "Nebulised, 1:100,000"], "The anaphylactic shock line says IM with 1:1000.")
q(56, "The adult epinephrine dose for anaphylactic shock shown is:", ["0.5 mg", "0.05 mg", "5 mg", "50 micrograms"], "The dose note gives 0.3 mg pediatric to 0.5 mg adult.")
q(56, "The pediatric epinephrine dose shown for anaphylactic shock is:", ["0.3 mg", "0.03 mg", "3 mg", "30 micrograms"], "The same dose note gives 0.3 mg for pediatric patients.")
q(56, "Epinephrine is also DOC in:", ["Brittle asthma", "Postural hypotension", "Huntington chorea", "Anticholinergic poisoning"], "The third DOC use listed for epinephrine is brittle asthma.")
q(56, "Adding epinephrine to local anaesthetic produces vasoconstriction that:", ["Increases duration and decreases toxicity", "Decreases duration and increases toxicity", "Causes immediate bronchodilation only", "Blocks AChE"], "The other-use note shows vasoconstriction causing increased duration and decreased toxicity.")
q(56, "For glaucoma, the epinephrine-related drug preferred is:", ["Dipivefrine", "Droxidopa", "Dopexamine", "Dobutamine"], "Under glaucoma, the page notes dipivefrine is preferred.")
q(56, "The ocular side effect of epinephrine/dipivefrine listed is:", ["Conjunctival pigmentation", "Retinal detachment", "Cataract", "Iris cyst"], "The epinephrine side-effect line says conjunctival pigmentation.")
q(56, "The common precursor for melanin mentioned under epinephrine is:", ["Tyrosine", "DOPA only", "Tryptophan", "Choline"], "The side-effect note says the common precursor as melanin is tyrosine.")
q(56, "Which property explains why epinephrine is chosen in anaphylaxis rather than norepinephrine?", ["It also has β2 bronchodilator action", "It cannot stimulate the heart", "It only lowers blood pressure", "It blocks α receptors"], "Epinephrine acts on α, β1 and β2, and the chapter later notes anaphylactic shock DOC is epinephrine because of added β2 bronchodilation.")

unit("Endogenous Catecholamines: Norepinephrine and Dopamine", "Norepinephrine acts on α1 and β1 and is a stronger vasoconstrictor than epinephrine because it lacks β2 vasodilation. It is given only IV for vasodilatory, cardiogenic and neurogenic shock, while IM use is contraindicated because of muscle necrosis. Dopamine is dose-dependent: low doses act on D1 for diuresis, intermediate doses on β1 for contractility, and high doses on α1 for vasoconstriction, but shock use raises mortality because of pro-arrhythmia.")
q(56, "Norepinephrine acts mainly on:", ["α1 and β1 receptors", "α1, β1 and β2 receptors", "β1 and β2 only", "D1 receptors only"], "The norepinephrine column says it acts on α1 and β1.")
q(56, "Norepinephrine is a more potent vasoconstrictor than epinephrine because it lacks:", ["β2 vasodilation", "α1 action", "β1 action", "Metabolism by MAO"], "The page says NE is a more potent vasoconstrictor than epinephrine with no β2 vasodilation.")
q(56, "Norepinephrine is DOC in vasodilatory shock due to:", ["Sepsis", "Anaphylaxis only", "Brittle asthma", "Glaucoma"], "The first norepinephrine DOC use is vasodilatory shock, with sepsis in parentheses.")
q(56, "Norepinephrine is also DOC in:", ["Cardiogenic shock", "Motion sickness", "Overactive bladder", "Myasthenia gravis"], "Cardiogenic shock is listed as the second DOC use of norepinephrine.")
q(56, "In neurogenic shock, norepinephrine is used when paraplegia is associated with:", ["Increased heart rate", "Decreased heart rate", "Absent sweating only", "Miosis"], "The neurogenic shock note writes ↑ HR if paraplegia.")
q(56, "In neurogenic shock with quadriplegia, the heart rate pattern shown is:", ["Decreased heart rate", "Increased heart rate", "No heart rate effect", "Only palpitations"], "The neurogenic shock note writes ↓ HR if quadriplegia.")
q(56, "The route of norepinephrine is:", ["Only IV", "Only IM", "Only oral", "Only transdermal"], "The norepinephrine route line says only IV.")
q(56, "Intramuscular norepinephrine is contraindicated because it can cause:", ["Muscle necrosis", "Nasal congestion", "Urine retention", "Dementia"], "The route note states IM is contraindicated due to muscle necrosis.")
q(56, "Dopamine is administered as:", ["Continuous IV infusion", "Only transdermal patch", "Eye ointment", "Oral tablet"], "The dopamine heading says dose-dependent action with continuous IV infusion.")
q(56, "Dopamine dosing is expressed in:", ["mcg/kg/min", "mg/kg/day", "mEq/L", "percentage AUC"], "The dose-dependent action line gives mcg/kg/min.")
q(56, "At 0-2 mcg/kg/min, dopamine acts on:", ["D1 receptors", "β1 receptors", "α1 receptors", "m3 receptors"], "The dopamine dose table says 0 to 2 acts on D1.")
q(56, "The low-dose D1 action of dopamine causes:", ["Diuresis", "Vasoconstriction", "Miosis", "Myocardial depression"], "The low-dose dopamine line ends with diuresis.")
q(56, "At 2-10 mcg/kg/min, dopamine acts on:", ["β1 receptors", "D1 receptors", "α1 receptors", "β3 receptors"], "The dopamine middle-dose line says 2 to 10 acts on β1.")
q(56, "Intermediate-dose dopamine produces:", ["Increased heart contraction", "Decreased heart contraction", "Pure diuresis only", "Bronchospasm"], "The β1 dose range points to increased heart contraction.")
q(56, "At doses greater than 10 mcg/kg/min, dopamine acts on:", ["α1 receptors", "D1 receptors", "β3 receptors", "m1 receptors"], "The high-dose dopamine line says >10 acts on α1.")
q(56, "High-dose dopamine causes:", ["Vasoconstriction", "Diuresis", "Bronchodilation", "AChE inhibition"], "The α1 dose range leads to vasoconstriction.")
q(56, "Using dopamine in shock can increase mortality because of:", ["Pro-arrhythmic effect", "AChE ageing", "Retinal detachment", "Acute glaucoma"], "The dopamine note says mortality rate increases if used in shock due to pro-arrhythmic effect.")
q(56, "IV epinephrine carries increased risk of:", ["Ventricular fibrillation and cardiac arrest", "Only cataract", "Only BPH", "Only diabetes remission"], "The note says IV epinephrine increases risk of V-fib and cardiac arrest.")
q(56, "The note links local anaesthesia toxicity with:", ["Neurogenic shock", "Anaphylactic shock", "Urge incontinence", "Sicca syndrome"], "One boxed note reads local anaesthesia toxicity → neurogenic shock.")
q(56, "For severe bradycardia in shock, the preferred sequence shown begins with:", ["Atropine plus norepinephrine", "Dopamine alone", "Norepinephrine alone", "Epinephrine plus atropine"], "The note ranks atropine + norepinephrine ahead of dopamine and norepinephrine alone.")

unit("Exogenous Catecholamines", "Exogenous catecholamines are receptor-selective clinical tools. Dobutamine acts on myocardial β receptors, increases contraction without SA-node effect and is DOC in acute CHF; isoprenaline is a pure β1/β2 agonist with no α action. Fenoldopam and dopexamine combine D1 with α1 or β1 effects to lower BP, while droxidopa is a norepinephrine prodrug for neurogenic orthostatic hypotension from diabetic neuropathy.")
q(57, "Dobutamine acts on β receptors primarily at the:", ["Myocardium", "Bladder", "Prostatic urethra", "Iris only"], "The dobutamine box says it acts on β at myocardium.")
q(57, "Dobutamine has no effect on the:", ["SA node", "Myocardial contractile cells", "β receptors", "Heart as an organ"], "The dobutamine note states no effect on SA node.")
q(57, "The action of dobutamine is to increase myocardial contraction while:", ["Heart rate is maintained", "Heart rate is always decreased", "Blood pressure is always zero", "ACh release is blocked"], "The dobutamine action line says ↑ myocardial contraction with HR maintained.")
q(57, "Dobutamine is DOC in:", ["Acute CHF", "Hypertensive emergency", "Postural hypotension", "Brittle asthma"], "Dobutamine is labelled DOC: acute CHF.")
q(57, "Another use of dobutamine is:", ["Stress echocardiography", "Ocular fundus examination", "Tensilon test", "Motion sickness"], "The dobutamine box lists stress ECHO cardiography as another use.")
q(57, "Isoprenaline acts on:", ["β1 and β2 receptors", "α1 and β1 receptors", "D1 and α1 receptors", "Only D1 receptors"], "The isoprenaline box says acts on β1 and β2.")
q(57, "Isoprenaline has:", ["No α stimulation", "Only α stimulation", "Only D1 stimulation", "Muscarinic blockade"], "The isoprenaline box explicitly notes no α stimulation.")
q(57, "Fenoldopam acts on:", ["D1 and α1, decreasing BP", "β1 only, increasing HR", "α2 only, causing sedation", "m3 only, causing bronchospasm"], "The fenoldopam box says acts on D1, α1 with decreased BP.")
q(57, "Fenoldopam is used for:", ["Hypertensive emergency by IV route", "Acute CHF by oral route", "Overactive bladder", "Narcolepsy"], "The fenoldopam use states hypertensive emergency, IV route.")
q(57, "Dopexamine acts on:", ["D1 and β1, decreasing BP", "α1 only", "β3 only", "m1 only"], "The dopexamine box says acts on D1, β1 and decreases BP.")
q(57, "Dopexamine is used in:", ["Acute CHF", "BPH", "Glaucoma", "Cheese reaction"], "The dopexamine box lists acute CHF.")
q(57, "Droxidopa is a prodrug of:", ["Norepinephrine", "Dopamine", "Epinephrine", "Acetylcholine"], "The droxidopa box calls it a prodrug of NE.")
q(57, "Droxidopa is used for:", ["Neurogenic hypotension", "Hypertensive emergency", "Anaphylactic shock", "Glaucoma"], "The droxidopa use is neurogenic hypotension.")
q(57, "The neurogenic hypotension example for droxidopa is postural hypotension in:", ["Diabetes mellitus", "Asthma", "Glaucoma", "Huntington disease"], "The droxidopa use specifies postural hypotension in diabetes mellitus.")
q(57, "In diabetic neurogenic postural hypotension, neuropathic damage to ganglia causes decreased:", ["NE, preload and cardiac output", "AChE and IOP", "Insulin and potassium only", "Dopamine and cortisol only"], "The droxidopa mechanism states ganglionic neuropathic damage lowers NE, preload and cardiac output.")

unit("α1 and Mixed α Non-catecholamine Agonists", "α1 non-catecholamines produce vasoconstriction and are used for the mnemonic-like cluster PHEN: priapism, hypotension from spinal anaesthesia, mydriasis without cycloplegia and nasal decongestion. Midodrine is DOC for postural hypotension, while mephentermine, metaraminol and methoxamine treat hypotension. Apraclonidine has α1/α2 action, can cause mydriasis and lid retraction through raised calcium, and is used as an antiglaucoma drug in open-angle glaucoma.")
q(57, "The α1 agonist action highlighted is:", ["Vasoconstriction", "Vasodilation", "Bronchodilation only", "AChE inhibition"], "The α1 agonist branch is labelled vasoconstriction.")
q(57, "Phenylephrine is DOC for priapism such as after:", ["Sildenafil abuse", "Organophosphate poisoning", "Atropine overdose", "β-blocker toxicity"], "The phenylephrine use list says priapism, e.g. sildenafil abuse, DOC.")
q(57, "In hypotension due to spinal anaesthesia, the α1 agonist with best fetal outcome is:", ["Phenylephrine", "Dopamine", "Isoprenaline", "Droxidopa"], "The phenylephrine use list says hypotension by spinal anaesthesia: DOC with best fetal outcome.")
q(57, "Phenylephrine causes mydriasis:", ["Without cycloplegia", "With mandatory cycloplegia", "By m3 stimulation", "By β3 action"], "The phenylephrine use list states mydriasis without cycloplegia.")
q(57, "A nasal decongestant α1 agonist listed as phenylephrine's use is:", ["Phenylephrine", "Bromocriptine", "Droxidopa", "Pyridostigmine"], "The phenylephrine use list includes nasal decongestant.")
q(57, "Xylometazoline and oxymetazoline are used as:", ["Nasal decongestants", "Cardiac stimulants", "Miotic agents", "AChE reactivators"], "The second α1 list line says xylometazoline and oxymetazoline are nasal decongestants.")
q(57, "Midodrine is DOC for:", ["Postural hypotension", "Hypertensive emergency", "Acute CHF", "Anaphylactic shock"], "The midodrine line says DOC for postural hypotension.")
q(57, "Mephentermine, metaraminol and methoxamine are used for:", ["Hypotension", "Hyperthyroidism", "Motion sickness", "Overactive bladder"], "These three are bracketed with use: hypotension.")
q(57, "Apraclonidine is an agonist at:", ["α1 and α2 receptors", "β1 and β2 receptors", "D1 and D2 receptors", "m1 and m3 receptors"], "Apraclonidine is placed under the α1 and α2 agonist branch.")
q(57, "Apraclonidine's side effects are mediated by increased:", ["Ca2+", "cAMP only", "AChE", "VMAT2"], "The apraclonidine note says S/E: ↑ Ca2+.")
q(57, "Apraclonidine may cause:", ["Mydriasis and lid retraction", "Miosis and accommodation spasm", "Bronchoconstriction and dyspnea", "Cholinergic crisis"], "The apraclonidine side-effect branches show mydriasis and lid retraction.")
q(57, "Apraclonidine is used as an anti-glaucoma drug in:", ["Open-angle glaucoma", "Closed-angle glaucoma before mannitol", "Only cataract", "Only uveitis"], "The apraclonidine branch says used as anti-glaucoma drugs in open-angle glaucoma.")
q(57, "The DOC for pregnancy-induced hypertension noted on this page is:", ["Oral labetalol", "Phenylephrine", "Dopamine", "Clonidine"], "The boxed note says DOC in PIH: oral labetalol.")

unit("α2 Agonists", "α2 agonists reduce norepinephrine release to produce central sympatholysis and lower BP; if they cross the BBB they also cause sedation. Clonidine is the prototype and is used for Tourette-associated ADHD, withdrawal syndromes, postmenopausal hot flashes, hypertension and pre-anaesthetic medication, with rebound hypertension on withdrawal due to α2 down-regulation. Lofexidine treats opioid withdrawal, tizanidine is a muscle relaxant, α-methyldopa forms α-methyl-NE and is used in PIH, while guanfacine/guanabenz and brimonidine complete the list.")
q(57, "The primary action of α2 agonists is to:", ["Decrease NE release", "Increase NE release", "Block AChE", "Open nicotinic channels"], "The α2 agonist action box begins with ↓ NE release.")
q(57, "Decreased NE release from α2 agonists produces:", ["Central sympatholysis", "Peripheral sympathetic stimulation", "Direct β2 bronchodilation", "ACh accumulation"], "The action flow says ↓ NE release → central sympatholysis.")
q(57, "Central sympatholysis caused by α2 agonists lowers:", ["Blood pressure", "IOP only", "AChE activity", "Dopamine only"], "The α2 flow continues central sympatholysis → ↓ BP.")
q(57, "If an α2 agonist crosses the BBB it can cause:", ["Sedation", "Miosis only", "Cataract", "Iris cyst"], "The action box also says cause sedation if it crosses BBB.")
q(57, "The prototype α2 agonist is:", ["Clonidine", "Lofexidine", "Tizanidine", "Brimonidine"], "Clonidine is labelled as the prototype drug.")
q(57, "Clonidine is DOC for ADHD associated with:", ["Tourette's syndrome", "Narcolepsy", "Huntington disease", "Myasthenia gravis"], "The clonidine use list states ADHD associated with Tourette's syndrome (DOC).")
q(57, "Clonidine is used for withdrawal from:", ["Opioids, alcohol and nicotine", "Only benzodiazepines", "Only insulin", "Only corticosteroids"], "The clonidine use list includes opioid/alcohol/nicotine withdrawal.")
q(57, "Clonidine can be used for:", ["Post-menopausal hot flashes", "BPH only", "Acute angle closure glaucoma", "Organophosphate ageing"], "Post-menopausal hot flashes are listed as a clonidine use.")
q(57, "Clonidine is also used in:", ["Hypertension and pre-anaesthetic medication", "Acute CHF and stress echo only", "Anticholinergic poisoning", "Urge incontinence"], "The clonidine use list includes hypertension and pre-anaesthetic medication.")
q(57, "Clonidine withdrawal can cause rebound hypertension due to:", ["α2 down-regulation", "β3 up-regulation", "AChE ageing", "Tyrosine depletion"], "The side-effect note says withdrawal/rebound hypertension due to α2 down-regulation.")
q(57, "Lofexidine is used for:", ["Opioid withdrawal symptoms", "Brittle asthma", "Cardiac arrest", "Glaucoma"], "The lofexidine line says for opioid withdrawal symptoms.")
q(57, "Tizanidine is a:", ["Muscle relaxant", "β3 agonist", "Miotic agent", "AChE reactivator"], "The tizanidine line identifies it as a muscle relaxant.")
q(57, "α-methyldopa is a prodrug converted to:", ["α-methyl-NE", "Droxidopa", "Metyrosine", "Acetylcholine"], "The α-methyl-dopa line says prodrug → α methyl-NE.")
q(57, "α-methyldopa decreases NE release and:", ["Depletes NE in vesicles", "Increases NE storage", "Blocks β3 receptors", "Inhibits AChE"], "The action lines under α-methyldopa say ↓ NE release and depletes NE in vesicle.")
q(57, "α-methyldopa is used in:", ["Pregnancy-induced hypertension", "Priapism", "Narcolepsy", "Acute CHF"], "The use line says pregnancy induced hypertension.")
q(57, "A side effect of α-methyldopa listed is:", ["Hemolysis", "Cataract", "Iris cyst", "Retinal detachment"], "The side-effect line for α-methyl-dopa says hemolysis.")
q(57, "Guanfacine and guanabenz can be used in:", ["ADHD", "Acute CHF", "Anaphylactic shock", "Organophosphate poisoning"], "The guanfacine/guanabenz line says can be used in ADHD.")
q(57, "Brimonidine can cross the:", ["Blood-brain barrier", "Placenta only", "Blood-testis barrier only", "Synovial membrane only"], "The brimonidine line says it can cross the blood-brain barrier.")
q(57, "Neonatal side effects of brimonidine include:", ["Drowsiness and apnea", "Tremor and hyperglycemia", "Miosis and lacrimation", "Cataract and iris cysts"], "The brimonidine side-effect line lists drowsiness and apnea in neonates.")

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
