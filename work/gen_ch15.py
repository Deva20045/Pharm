# -*- coding: utf-8 -*-
import json
CH = 15
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

unit("Physiology of Norepinephrine: Synthesis, Storage, Release and Metabolism", "Norepinephrine synthesis begins with tyrosine and the rate-limiting enzyme tyrosine hydroxylase, then proceeds through DOPA and dopamine before dopamine enters the vesicle through VMAT2 and is converted to norepinephrine by dopamine-β-hydroxylase. Released norepinephrine acts on α and β receptors, is metabolised by MAO and COMT, and is cleared by reuptake. Several drugs map exactly onto this diagram: metyrosine blocks tyrosine hydroxylase, reserpine/tetrabenazine derivatives block VMAT2, and cocaine, TCAs and SNRIs block reuptake.")
q(52, "Norepinephrine synthesis begins with:", ["Tyrosine", "Dopamine", "Acetylcholine", "Epinephrine"], "The pathway in the presynaptic neuron starts with tyrosine.")
q(52, "Tyrosine is converted to DOPA by:", ["Tyrosine hydroxylase", "Dopa decarboxylase", "Dopamine-β-hydroxylase", "Monoamine oxidase"], "The synthesis diagram labels tyrosine hydroxylase between tyrosine and DOPA.")
q(52, "The rate-limiting enzyme in norepinephrine synthesis is:", ["Tyrosine hydroxylase", "Dopa decarboxylase", "VMAT2", "COMT"], "Tyrosine hydroxylase is marked as the rate-limiting enzyme and rate-limiting step.")
q(52, "Which drug inhibits the rate-limiting step of norepinephrine synthesis?", ["Metyrosine", "Reserpine", "Tetrabenazine", "Cocaine"], "Metyrosine is drawn at tyrosine hydroxylase.")
q(52, "DOPA is converted to dopamine by:", ["Dopa decarboxylase", "Tyrosine hydroxylase", "Dopamine-β-hydroxylase", "VMAT2"], "The arrow from DOPA to dopamine is labelled dopa decarboxylase.")
q(52, "Dopamine enters the storage vesicle through:", ["VMAT2", "NET", "SERT", "AChE"], "The diagram shows dopamine entering the vesicle through VMAT2.")
q(52, "VMAT2 stands for:", ["Vesicle monoamine transporter 2", "Vascular monoamine transferase 2", "Vagal muscarinic activating transporter 2", "Vesicular myosin ATPase 2"], "The legend expands VMAT2 as vesicle monoamine transporter 2.")
q(52, "Inside the vesicle, dopamine is converted to norepinephrine by:", ["Dopamine-β-hydroxylase", "Dopa decarboxylase", "Tyrosine hydroxylase", "MAO"], "The vesicle step is labelled dopamine-β-hydroxylase.")
q(52, "Released norepinephrine acts on which postsynaptic receptors in the diagram?", ["α and β receptors", "m and N receptors", "D1 only", "H1 only"], "The synapse diagram shows NE acting on α and β receptors.")
q(52, "Norepinephrine metabolism in the diagram is by:", ["MAO and COMT", "AChE and pseudocholinesterase", "CYP3A4 and CYP2D6", "Renin and ACE"], "The metabolism branch lists MAO and COMT.")
q(52, "MAO stands for:", ["Monoamine oxidase", "Muscarinic activating oxidase", "Methyl amine oxygenase", "Myocardial adrenergic oxidase"], "The abbreviation list expands MAO as monoamine oxidase.")
q(52, "COMT stands for:", ["Catechol-O-methyl transferase", "Choline-O-methyl transferase", "Cortisol monoamine transporter", "Calcium oxidative methyl transferase"], "The legend expands COMT as catechol-O-methyl transferase.")
q(52, "DA in the diagram stands for:", ["Dopamine", "Dopa decarboxylase", "Dale's agonist", "Direct adrenergic"], "The legend defines DA as dopamine.")
q(52, "NE in the diagram stands for:", ["Norepinephrine", "Neostigmine", "Neuroepinephrine enzyme", "Nicotinic excitation"], "The legend defines NE as norepinephrine.")
q(52, "Which drugs are marked as VMAT2 inhibitors?", ["Reserpine, tetrabenazine, deutetrabenazine and valbenazine", "Cocaine, TCAs and SNRIs", "Metyrosine and phenylephrine", "Pilocarpine and cevimeline"], "The VMAT2 inhibitor bracket lists reserpine, tetrabenazine, deutetrabenazine and valbenazine.")
q(52, "Cocaine is shown inhibiting:", ["Reuptake", "Tyrosine hydroxylase", "VMAT2", "Dopamine-β-hydroxylase"], "The cocaine label is placed on the reuptake pathway.")
q(52, "Tricyclic antidepressants in the diagram inhibit:", ["Reuptake of catecholamines", "AChE", "VMAT2", "Dopa decarboxylase"], "The TCA label is also on the reuptake limb.")
q(52, "Serotonin-norepinephrine reuptake inhibitors act at which step shown?", ["Reuptake", "Vesicular conversion of dopamine to NE", "Tyrosine hydroxylation", "MAO metabolism"], "SNRIs are drawn on the reuptake pathway in the synapse.")

unit("Drugs Modifying NE/DA and Cocaine Dependence", "Metyrosine lowers catecholamines by competitively inhibiting tyrosine hydroxylase and is used in malignant pheochromocytoma. VMAT2 blockers lower norepinephrine and dopamine: reserpine is now uncommon, tetrabenazine is DOC for Huntington chorea and Tourette-associated tics, and deutetrabenazine/valbenazine are long-acting derivatives used for tardive dyskinesia. Cocaine blocks NA and DA reuptake, raising DA and addiction potential; dependence is managed by keeping dopamine receptors engaged with bromocriptine and tapering.")
q(52, "Metyrosine is a tyrosine analogue that acts as a:", ["Competitive inhibitor of tyrosine hydroxylase", "VMAT2 inhibitor", "Reuptake inhibitor", "D2 receptor agonist"], "The metyrosine MOA cell says tyrosine analogue and competitive inhibitor of tyrosine hydroxylase.")
q(52, "The effect of metyrosine on norepinephrine is:", ["Decreased NE", "Increased NE", "No effect", "Only increased dopamine"], "The metyrosine MOA ends with ↓ NE.")
q(52, "Metyrosine is used in malignant pheochromocytoma to:", ["Block raised catecholamines and lower BP", "Increase catecholamines", "Treat ADHD", "Treat bronchospasm"], "The use cell says malignant pheochromocytoma: block raised catecholamines and decrease blood pressure.")
q(52, "Reserpine decreases:", ["NE and DA", "Only ACh", "Only histamine", "Only insulin"], "The reserpine MOA row shows ↓ NE and ↓ DA.")
q(52, "Current listed uses of reserpine are uncommon but include:", ["Mild/moderate hypertension and agitated psychotic state", "Acute CHF and stress echo", "Glaucoma and xerostomia", "Organophosphate poisoning"], "The reserpine use row lists mild/moderate hypertension and agitated psychotic state with an 'uncommon' bracket.")
q(52, "Tetrabenazine blocks:", ["VMAT2", "Tyrosine hydroxylase", "NET only", "AChE"], "The tetrabenazine row has the MOA 'Block VMAT2'.")
q(52, "Tetrabenazine lowers:", ["NE and DA", "Only acetylcholine", "Only glucose", "Only cortisol"], "The tetrabenazine MOA cell shows ↓ NE and ↓ DA.")
q(52, "Tetrabenazine is DOC for treatment of:", ["Huntington's chorea", "Acute CHF", "Brittle asthma", "Angle closure glaucoma"], "The use cell lists DOC: Rx of Huntington's chorea.")
q(52, "Tetrabenazine is also used for tics associated with:", ["Tourette syndrome", "Parkinson disease", "Myasthenia gravis", "Sicca syndrome"], "The same use cell includes tics associated with Tourette syndrome.")
q(52, "The table notes tetrabenazine is preferred over antipsychotics because of antipsychotic:", ["Extrapyramidal side effects", "Bronchodilation", "Aqueous outflow increase", "Renin release"], "The note says tetrabenazine is preferred over antipsychotics due to extrapyramidal side effects.")
q(52, "Deutetrabenazine and valbenazine are:", ["Long-acting derivatives of tetrabenazine", "Short-acting β2 agonists", "AChE reactivators", "Muscarinic blockers"], "Their row says derivatives of tetrabenazine, long acting.")
q(52, "Deutetrabenazine and valbenazine are DOC for:", ["Tardive dyskinesia", "Huntington chorea only", "Pheochromocytoma", "Bronchial asthma"], "The use cell for these derivatives says DOC: tardive dyskinesia.")
q(53, "Cocaine inhibits reuptake of:", ["NA and DA", "ACh and serotonin only", "Insulin and glucose", "Renin and angiotensin"], "The cocaine MOA lists inhibition of reuptake of NA and DA.")
q(53, "Cocaine's addictive potential is due to increased:", ["Dopamine acting on DA receptors", "Acetylcholine acting on m3", "Norepinephrine acting on α1 only", "Histamine acting on H1"], "The cocaine MOA says ↑ DA acts on DA receptors, producing addictive potential.")
q(53, "The DOC for cocaine dependence shown is:", ["Bromocriptine", "Atropine", "Pralidoxime", "Metyrosine"], "The dependence section says DOC: bromocriptine.")
q(53, "Bromocriptine treats dependence by acting as a:", ["D2 agonist", "D2 antagonist", "VMAT2 inhibitor", "AChE inhibitor"], "Bromocriptine is labelled D2 agonist.")
q(53, "Bromocriptine prevents withdrawal symptoms by:", ["Keeping receptors engaged", "Blocking all dopamine receptors", "Rapidly stopping all therapy", "Raising acetylcholine"], "The flow below dependence says keeps receptors engaged → no withdrawal symptoms.")
q(53, "After starting bromocriptine for dependence, the dose should be:", ["Gradually tapered", "Stopped abruptly", "Doubled every hour", "Given only once"], "The dependence flow ends with gradually taper dose.")
q(53, "Side effects due to decreased norepinephrine include:", ["Depression and hypotension", "Parkinsonism only", "Hyperglycemia and tremor", "Mydriasis and cycloplegia"], "The side-effects section says due to ↓ NE: depression and hypotension.")
q(53, "A side effect due to decreased dopamine is:", ["Parkinsonism", "Hypertensive crisis", "Bronchodilation", "Tachycardia only"], "The side-effects section says due to ↓ dopamine: Parkinsonism.")
q(53, "Stopping a dependence-producing drug causes withdrawal because plasma concentration:", ["Decreases", "Increases", "Becomes therapeutic indefinitely", "Converts to norepinephrine"], "The dependence note shows stop drug → decreased plasma concentration → withdrawal.")
q(53, "The deaddiction principle shown is to start a similar drug and then:", ["Gradually taper it", "Never taper it", "Add atropine", "Block VMAT2"], "The deaddiction arm says start similar drug → gradual taper → mild withdrawal.")
q(53, "Compared with abrupt stopping, deaddiction with a similar drug produces:", ["Mild withdrawal", "No receptor engagement and severe withdrawal", "Immediate hypertensive crisis", "Acute glaucoma"], "The note ends the deaddiction path with mild withdrawal.")

unit("Sympathetic α Receptors", "Sympathetic receptors are GPCRs divided into α and β. α1 is mainly postsynaptic, centrally placed on the membrane and Gq-coupled; it contracts vascular, prostatic, bladder sphincter and radial iris smooth muscle but relaxes GIT through Ca2+-dependent K+ opening and hyperpolarisation. α2 is predominantly presynaptic and Gi-coupled; late stimulation reduces further NE release, causing central sympatholysis, but postsynaptic vascular α2 can vasoconstrict and pancreatic β-islet α2 reduces insulin to raise glucose.")
q(53, "Sympathetic receptors are:", ["G-protein coupled receptors", "Ligand-gated Na+ channels", "Nuclear receptors", "AChE enzymes"], "The receptors diagram says α and β sympathetic receptors are GPCRs.")
q(53, "The two α receptor types listed are:", ["α1 and α2", "α3 and α4", "β1 and β2", "m1 and m3"], "The α receptor section lists types α1 and α2.")
q(53, "The usual location of α1 receptors is:", ["Postsynaptic", "Presynaptic more than postsynaptic", "Only adrenal medulla", "Only CNS"], "The location row says α1 is postsynaptic.")
q(53, "α2 receptors are located:", ["Presynaptic more than postsynaptic", "Only postsynaptic", "Only at NMJ", "Only inside mitochondria"], "The location row for α2 says presynaptic > postsynaptic.")
q(53, "The density of α1 receptors is greatest at the:", ["Centre of the membrane", "Periphery of the membrane", "Nucleus", "Vesicle"], "The density row says α1 receptors are at the center of the membrane.")
q(53, "The density of α2 receptors is greatest at the:", ["Periphery of the membrane", "Centre of the membrane", "Nucleus", "Mitochondria"], "The density row says α2 receptors are at the periphery of the membrane.")
q(53, "α1 receptors are coupled to:", ["Gq", "Gi", "Gs", "G12/13 only"], "The subtype row for α1 reads Gq.")
q(53, "α2 receptors are coupled to:", ["Gi", "Gq", "Gs", "Tyrosine kinase"], "The subtype row for α2 reads Gi.")
q(53, "Initial presynaptic NE release stimulates α1 to increase:", ["Ca2+", "cAMP", "cGMP", "Cl- influx"], "The α1 MOA row says presynaptic release of NE initially stimulates α1 and raises Ca2+.")
q(53, "Late stimulation of presynaptic α2 causes:", ["Decreased NE release", "Increased NE release indefinitely", "AChE inhibition", "Insulin release"], "The α2 MOA row says increased synaptic NE gives late α2 stimulation and presynaptic decrease of NE release.")
q(53, "α1 stimulation contracts vascular smooth muscle to cause:", ["Vasoconstriction", "Vasodilation", "Bronchodilation", "Urine formation"], "Under α1 effects, blood vessels undergo smooth muscle contraction causing vasoconstriction.")
q(53, "α1 stimulation contracts which urinary outlet structures?", ["Prostatic urethra and bladder sphincter", "Detrusor only", "Ureter only", "Renal tubule only"], "The α1 smooth muscle list includes prostatic urethra and bladder sphincter.")
q(53, "α1 stimulation of radial muscle of iris causes:", ["Mydriasis", "Miosis", "Cycloplegia", "Lacrimation"], "The α1 effect list states radial muscle of iris: mydriasis.")
q(53, "α1 stimulation in the GIT causes relaxation because increased Ca2+ opens:", ["Ca2+-dependent K+ channels", "Voltage-gated Na+ channels", "Cl- channels", "AChE channels"], "The GIT α1 line explains ↑ Ca2+ opens Ca2+-dependent K+ channels.")
q(53, "Opening Ca2+-dependent K+ channels in the GIT produces:", ["Hyperpolarisation", "Depolarisation", "Miosis", "ACh release"], "The α1 GIT mechanism ends with hyperpolarise.")
q(53, "α1 stimulation in liver increases:", ["Gluconeogenesis", "Insulin release", "Renin degradation", "ACh metabolism"], "The α1 effect list says liver: increased gluconeogenesis.")
q(53, "α1 stimulation in skeletal muscle increases:", ["Glycogenolysis", "Insulin secretion", "Aqueous outflow", "Cortisol synthesis"], "The α1 effect list says skeletal muscle: increased glycogenolysis.")
q(53, "The glucose effect of α1 stimulation in liver/skeletal muscle is:", ["Hyperglycemia", "Hypoglycemia", "No glucose change", "Ketonuria only"], "The α1 liver and skeletal muscle effects are bracketed to hyperglycemia.")
q(53, "The presynaptic α2 effect in the brain stem is:", ["Central sympatholysis", "Central sympathetic excitation", "Peripheral neuromuscular block", "Direct bronchodilation"], "The α2 presynaptic effect cell says central sympatholysis.")
q(53, "Central sympatholysis from presynaptic α2 stimulation decreases:", ["Blood pressure", "Aqueous outflow", "Bladder capacity", "Lacrimation"], "The α2 presynaptic effect shows decreased blood pressure.")
q(53, "Postsynaptic α2 on blood vessels is a:", ["Gq subtype causing vasoconstriction", "Gi subtype causing vasodilation", "Gs subtype causing bronchodilation", "Na+ channel causing muscle contraction"], "The α2 postsynaptic blood vessel row says Gq subtype: vasoconstriction.")
q(53, "α2 on pancreatic β-islet cells is a Gi subtype that:", ["Decreases insulin release", "Increases insulin release", "Increases glucagon only", "Releases norepinephrine"], "The α2 pancreatic row says β-islet cells of pancreas, Gi subtype, decreases insulin release.")
q(53, "Reduced insulin release from α2 stimulation causes:", ["Increased glucose", "Decreased glucose", "No glucose effect", "Hypokalemia only"], "The pancreatic α2 row ends with increased glucose.")

unit("Catecholamines, Blood Glucose and β Receptors", "The notes compare m3 and α/β signalling and explain why catecholamines produce hyperglycemia: α1/α2/β2 stimulation is released during hypoglycemia, and the β2 liver/skeletal-muscle rise in glucose outweighs pancreatic insulin release. β receptors are Gs-coupled: β1 acts in heart and kidney to raise contraction, rate, conduction and renin, β2 relaxes smooth muscle but also causes tremor, palpitations, hyperglycemia and hypokalemia, and β3 relaxes bladder while stimulating adipocyte lipolysis.")
q(54, "The note states that m3, although a Gq subtype, does not cause:", ["Relaxation", "Increased Ca2+", "K+ channel blockade", "Smooth muscle signalling"], "The first note says m3 (Gq subtype) does not cause relaxation.")
q(54, "ACh stimulation of m3 increases Ca2+ and blocks:", ["K+ channels", "Na+ channels", "Cl- channels", "VMAT2"], "The m3 note shows ACh stimulates m3, increases Ca2+ and blocks the K+ channel.")
q(54, "Slow infusion of clonidine produces:", ["Central sympatholysis with decreased BP", "Postsynaptic vasoconstriction with worsened hypertension", "Bronchospasm", "Dopamine release"], "The clonidine note says slow infusion → central sympatholysis → decreased BP.")
q(54, "Fast infusion of clonidine can produce:", ["Postsynaptic vasoconstriction and worsened hypertension", "Only central sympatholysis", "Miosis", "AChE ageing"], "The clonidine note says fast infusion → postsynaptic vasoconstriction → worsens hypertension/increases BP.")
q(54, "Hypoglycemia triggers catecholamine release that stimulates:", ["α1, α2 and β2 receptors", "m1, m2 and m3 receptors", "Only β3 receptors", "Only D1 receptors"], "The blood-glucose note says hypoglycemia releases catecholamines that stimulate α1, α2 and β2.")
q(54, "The net blood-glucose effect of catecholamines is:", ["Increased glucose", "Decreased glucose", "No effect", "Only decreased potassium without glucose effect"], "The flow after α1, α2, β2 stimulation ends with increased glucose.")
q(54, "β2 receptors are coupled to:", ["Gs", "Gi", "Gq", "Nicotinic ion channels"], "The β2 note labels β2 as a Gs subtype.")
q(54, "β2 stimulation in liver/skeletal muscle increases:", ["Gluconeogenesis and glycogenolysis", "Insulin release only", "Glycogen synthesis only", "ACh breakdown"], "The β2 diagram shows liver/skeletal muscle gluconeogenesis plus glycogenolysis leading to increased glucose.")
q(54, "β2 stimulation of pancreatic β-islets causes:", ["Increased insulin", "Decreased insulin", "No insulin effect", "Glucagon blockade"], "The middle branch from β-islets of pancreas says ↑ insulin.")
q(54, "The pancreatic insulin effect of β2 stimulation lowers:", ["Glucose and K+", "Only blood pressure", "Only norepinephrine", "Only aqueous humour"], "The β-islet branch shows decreased glucose and decreased K+.")
q(54, "β2-induced fall in K+ is used to treat:", ["Hyperkalemia", "Hypokalemia", "Hyponatremia", "Hypercalcemia"], "The β2 branch says ↓ K+ is used to Rx hyperkalemia.")
q(54, "Catecholamine warning symptoms of hypoglycemia include:", ["Palpitation, tremor and sweating", "Miosis, salivation and diarrhea", "Dry mouth and urine retention", "Cataract and iris cysts"], "The heart branch lists palpitation/tremor/sweating as hypoglycemia awareness due to increased catecholamines.")
q(54, "Despite insulin release, the net result of β2 effects on glucose is:", ["Hyperglycemia", "Hypoglycemia", "Euglycemia only", "No effect"], "The diagram states net result: hyperglycemia, similar to α.")
q(54, "β receptors are divided into:", ["β1, β2 and β3", "β1 and β4 only", "α1 and α2", "m1 to m5"], "The β receptor section lists β1, β2 and β3.")
q(54, "β receptors are coupled to which G protein subtype?", ["Gs", "Gi", "Gq", "G12/13"], "The bracket beside β1, β2 and β3 says Gs subtype.")
q(54, "β1 receptors in the heart increase:", ["Ca2+", "K+ efflux only", "AChE activity", "VMAT2 storage"], "The β1 heart MOA row says ↑ Ca2+.")
q(54, "Cardiac β1 stimulation increases:", ["Contraction, heart rate and conduction", "Only vasodilation", "Only bronchial relaxation", "Only GIT relaxation"], "The β1 heart effect list shows increased contraction, heart rate and conduction.")
q(54, "β1 receptors in the kidney are on JG cells and increase:", ["Renin release", "Insulin release", "ACh release", "Bile secretion"], "The β1 kidney row says JG cells: increased renin release.")
q(54, "The BP effect of β1 stimulation at the kidney is:", ["Increased blood pressure", "Decreased blood pressure", "No effect", "Only postural hypotension"], "The β1 kidney effect cell reads increased blood pressure.")
q(55, "β2 stimulation relaxes smooth muscle through increased:", ["cAMP", "cGMP only", "ACh", "COMT"], "The β2 smooth-muscle mechanism row reads relaxation (↑ cAMP).")
q(55, "β2-mediated vasodilation tends to cause:", ["Hypotension", "Severe hypertension", "Miosis", "Urine retention"], "The β2 effects column lists vasodilation with hypotension.")
q(55, "The β2 agonist use linked to asthma is:", ["Salbutamol", "Ritodrine", "Mirabegron", "Metyrosine"], "The β2 smooth-muscle use cell lists salbutamol in asthma.")
q(55, "β2 stimulation causes bronchi to undergo:", ["Bronchodilation", "Bronchoconstriction", "Fibrosis", "Mucus plugging only"], "The β2 effects row includes bronchodilation.")
q(55, "β2 stimulation relaxes the uterus; the uterine relaxant listed is:", ["Ritodrine", "Phenylephrine", "Tetrabenazine", "Droxidopa"], "The uterine relaxation row lists ritodrine as uterine relaxant.")
q(55, "β2 action on cardiac muscle causes:", ["Palpitations", "Cataract", "Miosis", "Urge incontinence"], "The cardiac muscle row under β2 gives palpitations.")
q(55, "β2 action on skeletal muscle causes:", ["Tremors", "Miosis", "Cycloplegia", "Constipation"], "The skeletal muscle row gives tremors.")
q(55, "β2 effects on glucose metabolism cause:", ["Hyperglycemia", "Hypoglycemia", "No effect", "Lactic acidosis only"], "The glucose metabolism row shows gluconeogenesis/glycogenolysis and hyperglycemia.")
q(55, "β2 causes inward K+ movement by increasing insulin and activating:", ["Na+-K+ ATPase", "AChE", "VMAT2", "MAO"], "The K+ row states ↑ insulin and ↑ cAMP activate Na+-K+ ATPase, causing inward K+ movement.")
q(55, "The potassium effect of β2 stimulation is:", ["Hypokalemia", "Hyperkalemia", "No potassium effect", "Hypercalcemia"], "The K+ row lists hypokalemia as the effect.")
q(55, "Salbutamol is used for which potassium emergency?", ["Hyperkalemia", "Hypokalemia", "Hypernatremia", "Hypocalcemia"], "The use column in the K+ row says salbutamol for hyperkalemia.")
q(55, "β3 receptors in the bladder increase cAMP to cause:", ["Relaxation", "Contraction", "Miosis", "Renin release"], "The β3 bladder row has MOA ↑ cAMP and effect relaxation.")
q(55, "The β3 bladder drugs used for urge incontinence are:", ["Mirabegron and vibegron", "Darifenacin and solifenacin", "Ipratropium and tiotropium", "Metyrosine and reserpine"], "The β3 bladder use row lists urge incontinence: mirabegron, vibegron.")
q(55, "β3 stimulation in adipocytes activates:", ["Hormone-sensitive lipase", "Tyrosine hydroxylase", "Dopa decarboxylase", "Acetylcholinesterase"], "The adipocyte row states ↑ cAMP stimulates HSL, hormone-sensitive lipase.")
q(55, "The adipocyte effect of β3 stimulation is:", ["Lipolysis", "Lipogenesis", "Miosis", "Bronchoconstriction"], "The β3 adipocyte effect column says lipolysis.")
q(55, "The β3 adipocyte use listed is:", ["Treatment of obesity", "Treatment of glaucoma", "Tensilon test", "Conduction block"], "The adipocyte use column says Rx of obesity.")

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
