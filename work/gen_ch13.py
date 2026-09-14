# -*- coding: utf-8 -*-
import json
CH = 13
Q = []
UNITS = []
cur = None

def unit(title, guide):
    global cur
    if cur:
        end()
    cur = {"title": title, "start": len(Q) + 1, "guide": guide}

def q(page, text, opts, exp):
    assert cur is not None
    assert len(opts) == 4
    suffix = f"(Book p{page})"
    exp = exp.rstrip()
    if not exp.endswith(suffix):
        exp = f"{exp} {suffix}"
    Q.append({"id": "", "sec": cur["title"], "page": page, "q": text, "opts": opts, "ans": 0, "exp": exp})

def end():
    global cur
    if cur is None:
        return
    cur["end"] = len(Q)
    UNITS.append(cur)
    cur = None

unit("Cholinergic Drugs: Classification", "Cholinergic drugs are parasympathomimetics. Direct drugs stimulate muscarinic or nicotinic receptors themselves, while indirect drugs block acetylcholinesterase, raise acetylcholine and then stimulate m/n receptors. Direct agents are organised by structure into amides and choline esters; indirect agents are split into irreversible organophosphates and reversible tertiary or quaternary amines.")
q(42, "Cholinergic drugs are also described as:", ["Parasympathomimetics", "Parasympatholytics", "Sympathomimetics", "Ganglion blockers"], "The flowchart places cholinergic drugs under the heading parasympathomimetics.")
q(42, "Direct-acting cholinergic drugs act by:", ["Stimulating muscarinic or nicotinic receptors", "Blocking acetylcholinesterase only", "Depleting norepinephrine vesicles", "Blocking muscarinic receptors"], "Direct acting drugs are labelled as stimulating muscarinic/nicotinic receptors.")
q(42, "Direct cholinergic drugs are classified in the chart based on:", ["Structure", "Duration of action only", "Route of administration", "Renal clearance"], "The direct-acting branch says 'Based on structure'.")
q(42, "The amide direct cholinergic drugs listed are:", ["Pilocarpine and cevimeline", "Bethanechol and carbachol", "Edrophonium and neostigmine", "Tacrine and donepezil"], "Under amides, the chart lists pilocarpine and cevimeline.")
q(42, "The natural choline ester in the direct cholinergic classification is:", ["Acetylcholine", "Physostigmine", "Pilocarpine", "Pralidoxime"], "The choline ester branch lists natural acetylcholine.")
q(42, "Which set contains the derivatives of acetylcholine shown in the chart?", ["Methacholine, bethanechol and carbachol", "Pilocarpine, cevimeline and physostigmine", "Sarin, tabun and soman", "Donepezil, rivastigmine and galantamine"], "The derivatives of ACh listed are methacholine, bethanechol and carbachol.")
q(42, "Methacholine is specifically noted as:", ["Methylated", "A quaternary oxime", "A natural tertiary amine", "An organophosphate"], "The methacholine bullet carries the parenthetical note 'methylated'.")
q(42, "Indirect-acting cholinergic drugs primarily:", ["Block acetylcholinesterase", "Block muscarinic receptors", "Activate β2 receptors", "Inhibit VMAT2"], "The indirect-acting branch reads 'Blocks acetylcholine esterase (AChE)'.")
q(42, "Blocking AChE increases which transmitter in the synapse?", ["Acetylcholine", "Norepinephrine", "Dopamine", "Serotonin"], "The indirect branch shows ↑ acetylcholine after acetylcholinesterase blockade.")
q(42, "Increased acetylcholine from AChE blockade stimulates:", ["Muscarinic and nicotinic receptors", "Only α1 receptors", "Only β1 receptors", "Only dopamine receptors"], "The chart writes that ↑ ACh stimulates m/N receptors.")
q(42, "The irreversible indirect cholinergic blockers are:", ["Organophosphates", "Carbamates", "Tertiary amines", "Quaternary amines"], "The irreversible limb is labelled organophosphates.")
q(42, "Reversible AChE blockers are grouped as:", ["Carbamates/non-carbamates", "Organophosphates only", "Catecholamines", "α agonists"], "The reversible limb is labelled carbamates/non-carbamates.")
q(42, "Reversible tertiary amines include which natural drug?", ["Physostigmine", "Edrophonium", "Neostigmine", "Pyridostigmine"], "Under tertiary amines, the natural drug is physostigmine.")
q(42, "Which group is listed as synthetic tertiary amines?", ["Tacrine, donepezil, rivastigmine and galantamine", "Edrophonium, neostigmine and pyridostigmine", "Sarin, VX, tabun and soman", "Pilocarpine, cevimeline, bethanechol and carbachol"], "The synthetic tertiary amine branch contains tacrine, donepezil, rivastigmine and galantamine.")
q(42, "Which reversible AChE blockers are quaternary amines?", ["Edrophonium, neostigmine and pyridostigmine", "Physostigmine and tacrine", "Pilocarpine and cevimeline", "Sarin and soman"], "The quaternary amine list shows edrophonium, neostigmine and pyridostigmine.")

unit("Direct Cholinergic Drugs: Amides, Pilocarpine and Cevimeline", "Amides are lipid soluble, cross the BBB and therefore have central as well as peripheral effects, while choline esters are insoluble, do not cross the BBB and act peripherally on bladder, GIT and muscle. Pilocarpine and cevimeline are the amides, both useful for xerostomia; pilocarpine also contracts the pupil to increase trabecular outflow in glaucoma. The same contraction of accommodation muscles explains brow ache, accommodation spasm and tractional retinal detachment.")
q(42, "Compared with choline esters, amides are:", ["Lipid soluble", "Lipid insoluble", "Unable to cross the BBB", "Purely peripheral"], "In the direct cholinergic table, amides are marked lipid soluble.")
q(42, "Choline esters are described in the table as:", ["Lipid insoluble", "Lipid soluble", "BBB-penetrant", "Central acting"], "The lipid solubility row says choline esters are insoluble.")
q(42, "Which direct cholinergic class crosses the blood-brain barrier?", ["Amides", "Choline esters", "Organophosphates only", "Quaternary amines"], "The BBB row says amides cross the BBB, whereas choline esters do not.")
q(42, "The site of action of amide cholinergic drugs is:", ["Central/peripheral", "Only bladder", "Only GIT", "Only skeletal muscle"], "The site-of-action row for amides reads central/peripheral.")
q(42, "The site of action of choline esters is mainly:", ["Peripheral: bladder, GIT and muscle", "Central nervous system only", "Postganglionic sympathetic nerve terminals", "Renal tubules only"], "The table says choline esters are peripheral, specifically bladder, GIT and muscle.")
q(42, "Central side effects are present with:", ["Amides", "Choline esters", "Quaternary amines", "Methacholine only"], "The central side-effect row says present for amides and absent for choline esters.")
q(42, "Pilocarpine is used for xerostomia because dry mouth is due to:", ["Decreased salivary secretions", "Excess salivary secretion", "Increased bronchial secretions", "Reduced tear drainage"], "The pilocarpine use reads xerostomia, dry mouth due to decreased salivary secretions.")
q(42, "Which two syndromes are listed as xerostomia settings for pilocarpine?", ["Sjogren's syndrome and sicca syndrome", "Tourette syndrome and ADHD", "Myasthenia gravis and Lambert-Eaton syndrome", "Huntington disease and tardive dyskinesia"], "The xerostomia bullet lists Sjogren's syndrome and sicca syndrome.")
q(43, "In closed-angle glaucoma, pilocarpine is DOC only after:", ["Normalisation of IOP with mannitol", "Starting atropine", "Giving β3 agonists", "Completing cataract surgery"], "The closed-angle glaucoma line says pilocarpine is DOC after normalisation of IOP with mannitol.")
q(43, "In open-angle glaucoma, pilocarpine is used as:", ["Second-line treatment", "First-line treatment", "Contraindicated treatment", "Only a diagnostic test"], "The open-angle glaucoma bullet says '2nd line Rx'.")
q(43, "Pilocarpine lowers IOP in glaucoma by causing:", ["Miosis with pupil contraction and increased trabecular outflow", "Mydriasis with decreased trabecular outflow", "Cycloplegia with aqueous retention", "α1-mediated radial muscle contraction"], "The MOA line says miosis contracts the pupil and increases trabecular outflow.")
q(43, "The side effects of pilocarpine in the eye occur due to contraction of:", ["Muscles of accommodation", "Radial muscle of iris only", "Eyelid levator muscle", "Orbicularis oculi"], "The side-effect box attributes them to contraction of muscles of accommodation.")
q(43, "Brow ache after pilocarpine is described as:", ["Referred pain", "Allergic conjunctivitis", "Corneal ulceration", "Increased melanin deposition"], "The brow ache bullet explicitly calls it referred pain.")
q(43, "Which ocular side effect of pilocarpine reflects tractional pull?", ["Retinal detachment", "Cataract only", "Iris cyst", "Conjunctival pigmentation"], "The side-effect list states retinal detachment due to tractional pull.")
q(43, "Obsolete miotic agents listed with cataract as a side effect include:", ["Physostigmine, echothiophate and fluostigmine", "Pilocarpine, cevimeline and bethanechol", "Atropine, tropicamide and homatropine", "Timolol, latanoprost and brimonidine"], "The note groups physostigmine, echothiophate and fluostigmine as obsolete miotic agents and brackets cataract as their side effect.")
q(43, "Which anti-glaucoma drug increases trabecular outflow by Rho-kinase inhibition?", ["Netarsudil", "Cevimeline", "Carbachol", "Pralidoxime"], "The note says anti-glaucoma drugs increasing trabecular outflow include netarsudil, a Rho kinase inhibitor.")
q(43, "Cevimeline is used for:", ["Xerostomia, more effectively", "Acute angle closure glaucoma as DOC", "Bronchial challenge testing", "Organophosphate poisoning"], "The cevimeline line states its use is xerostomia and that it is more effective.")

unit("Choline Esters and Derivatives of ACh", "Acetylcholine is destroyed in plasma by plasma, pseudo or butyryl cholinesterase, so it is systemically very short acting and is mainly remembered as a topical miotic in ocular surgery. Bethanechol, carbachol and methacholine differ by esterase resistance, receptor affinity, nicotinic side effects and uses. Bethanechol treats bladder and GIT atony, carbachol is topical because systemic use is limited by side effects, and methacholine provokes m3 bronchospasm in bronchial challenge testing.")
q(43, "Acetylcholine is metabolised in plasma by:", ["Plasma/pseudo/butyryl cholinesterase", "Monoamine oxidase", "Catechol-O-methyl transferase", "Tyrosine hydroxylase"], "The ACh metabolism line says it is metabolised in plasma by plasma, pseudo or butyryl choline esterase.")
q(43, "Because acetylcholine is metabolised in plasma, it is systemically:", ["Very short acting", "Very long acting", "Irreversible", "Only central acting"], "The arrow below plasma cholinesterase reads systemically very short acting.")
q(43, "Topical acetylcholine is used as a:", ["Miotic agent", "Mydriatic agent", "β2 bronchodilator", "Ganglion blocker"], "The ACh use is written as miotic agent by topical route.")
q(43, "During ocular surgery, corneal damage releases prostaglandins that may cause:", ["Mydriasis with acute block of trabecular outflow", "Miosis with increased trabecular outflow", "Only lacrimation", "Retinal vasodilation without IOP change"], "The flow says corneal damage releases prostaglandins, causing mydriasis and acute block of trabecular outflow.")
q(43, "Acute block of trabecular outflow during ocular surgery can lead to:", ["Increased IOP and acute angle closure glaucoma", "Decreased IOP and open-angle glaucoma", "Dry mouth", "Urine retention"], "The flow continues to increased IOP and acute angle closure glaucoma.")
q(43, "The shortest-acting cholinergic drug listed among plasma-metabolised drugs is:", ["Acetylcholine", "Bethanechol", "Carbachol", "Methacholine"], "The 'shortest acting in each class' note lists cholinergic: ACh.")
q(43, "Which muscle relaxant is listed as shortest acting due to plasma metabolism?", ["Succinylcholine", "Atracurium", "Rocuronium", "Baclofen"], "The shortest-acting list names succinylcholine for muscle relaxants.")
q(43, "Which β-blocker is listed as shortest acting due to plasma metabolism?", ["Esmolol", "Propranolol", "Atenolol", "Carvedilol"], "The shortest-acting list names esmolol among β-blockers.")
q(43, "Which opioid is listed as shortest acting due to plasma metabolism?", ["Remifentanil", "Morphine", "Fentanyl", "Methadone"], "The shortest-acting list names remifentanil among opioids.")
q(43, "Which calcium-channel blocker is listed as shortest acting due to plasma metabolism?", ["Clevidipine", "Verapamil", "Amlodipine", "Diltiazem"], "The shortest-acting list names clevidipine among calcium-channel blockers.")
q(43, "Which benzodiazepine is listed as shortest acting due to plasma metabolism?", ["Remimazolam", "Diazepam", "Lorazepam", "Midazolam"], "The shortest-acting list names remimazolam among benzodiazepines.")
q(44, "Bethanechol and carbachol are resistant to:", ["True and pseudo cholinesterase", "Only pseudo cholinesterase", "Only monoamine oxidase", "Only catechol-O-methyl transferase"], "In the derivatives table, bethanechol and carbachol share resistance to true plus pseudo choline esterase.")
q(44, "Methacholine is resistant to:", ["Pseudo cholinesterase", "True and pseudo cholinesterase", "Acetylcholinesterase irreversibly", "No esterase"], "The enzyme-resistance row lists pseudo choline esterase for methacholine.")
q(44, "Bethanechol and carbachol are described as:", ["Long acting", "Short acting like ACh", "Ultra-short acting", "Irreversible"], "The T1/2 row shows long acting across bethanechol and carbachol.")
q(44, "Methacholine is:", ["Short acting but longer than ACh", "Long acting like bethanechol", "Irreversible", "Unable to act on muscarinic receptors"], "The T1/2 row says methacholine is short acting, longer than ACh.")
q(44, "The muscarinic affinity of bethanechol and carbachol is:", ["m1 = m3 > m2", "m2 > m1 = m3", "m3 only", "m2 only"], "The muscarinic affinity row under bethanechol/carbachol reads m1 = m3 > m2.")
q(44, "Methacholine has highest affinity for:", ["m2 over m1 and m3", "m3 over all receptors", "Nn receptors only", "Nm receptors only"], "The methacholine affinity row reads m2 > m1 = m3.")
q(44, "Which ACh derivative has no nicotinic side effect in the table?", ["Bethanechol", "Carbachol", "Methacholine", "Acetylcholine"], "The nicotinic side-effect row says no action under bethanechol.")
q(44, "Which ACh derivative has maximum nicotinic side effects?", ["Carbachol", "Bethanechol", "Methacholine", "Cevimeline"], "The nicotinic side-effect row says maximum under carbachol.")
q(44, "Which ACh derivative has moderate nicotinic side effects?", ["Methacholine", "Bethanechol", "Pilocarpine", "Cevimeline"], "The nicotinic side-effect row says moderate under methacholine.")
q(44, "Bethanechol is used for bladder atony presenting as:", ["Overflow incontinence", "Urge incontinence", "Stress incontinence", "Hematuria"], "Under bethanechol uses, bladder atony leads to overflow incontinence.")
q(44, "A post-operative patient with urinary retention may be treated with:", ["Bethanechol", "Tropicamide", "Apraclonidine", "Bromocriptine"], "Post-operative urine retention is listed under bethanechol bladder uses.")
q(44, "Bethanechol is used in the GIT for:", ["Gastroparesis and paralytic ileus", "Peptic ulcer disease and reflux", "Infectious diarrhoea and dysmenorrhoea", "Motion sickness"], "The bethanechol GIT uses are gastroparesis and paralytic ileus.")
q(44, "Carbachol is used topically as:", ["A miotic agent for ocular surgery", "A systemic bronchodilator", "A bladder antispasmodic", "A β3 agonist"], "The carbachol use is topical: miotic agent for ocular surgery.")
q(44, "Systemic carbachol is not used because of:", ["Side effects", "Lack of any receptor activity", "Poor topical action", "Irreversible ageing"], "The carbachol systemic use cell says not used due to side effects.")
q(44, "Methacholine is used in the:", ["Bronchial challenge test", "Tensilon test", "Dale phenomenon", "Narcoanalysis test"], "The methacholine use is bronchial challenge test.")
q(44, "In bronchial challenge testing, methacholine is given:", ["In incremental doses", "Only as a single massive bolus", "Only after atropine", "Only by intravenous infusion"], "The methacholine column says it is given in incremental doses.")
q(44, "Methacholine produces bronchospasm through action on:", ["m3 receptors", "β2 receptors", "α2 receptors", "D1 receptors"], "The bronchial challenge line says bronchospasm occurs due to action on m3.")
q(44, "The parameter measured in the methacholine bronchial challenge test is:", ["FEV", "IOP", "GFR", "AUC"], "The note in the methacholine column says measure FEV.")
q(44, "The most widely distributed muscarinic receptor in the human body is:", ["m3", "m1", "m2", "m5"], "The note below the table states m3 is the most widely distributed muscarinic receptor.")
q(44, "The bronchial challenge test can also be performed with mannitol because it increases resistance due to:", ["Edema", "Esterase inhibition", "Ciliary muscle paralysis", "Dopamine release"], "The note says bronchial challenge can also be performed with mannitol, causing increased resistance due to edema.")

unit("Irreversible AChE Blockers and Organophosphate Poisoning", "Organophosphates bind AChE and first produce a reversible phase with raised ACh, but ageing replaces phosphate bonds with stronger bonds and makes inhibition irreversible. Oximes can break the organophosphate-AChE link before ageing but become ineffective after ageing. Organophosphate poisoning is a cholinergic syndrome; atropine treats muscarinic features, while oximes reactivate AChE for nicotinic toxicity.")
q(44, "Irreversible indirect cholinergic blockers act by binding AChE with:", ["Organophosphate", "Atropine", "Bromocriptine", "Dopamine"], "The irreversible blocker mechanism diagram labels organophosphate binding to AChE.")
q(44, "During the reversible phase of organophosphate binding, ACh levels:", ["Increase", "Decrease", "Become zero", "Are unchanged"], "The reversible phase bracket in the diagram is marked ↑ ACh levels.")
q(44, "Oximes are useful early in organophosphate poisoning because they:", ["Break the organophosphate-AChE bond", "Block muscarinic receptors", "Prevent ACh synthesis", "Act as β2 agonists"], "The diagram shows oximes breaking the organophosphate attachment before ageing.")
q(44, "Ageing of organophosphate-bound AChE means:", ["Replacement of phosphate bonds with stronger bonds", "Spontaneous recovery of AChE", "Conversion to a quaternary amine", "Direct β2 stimulation"], "The lower part of the diagram says replacement of PO4 bonds with stronger bonds leads to ageing.")
q(44, "Once ageing has occurred, oximes are:", ["Ineffective", "More effective", "The only antimuscarinic treatment", "Used as local anaesthetics"], "The diagram notes oximes are ineffective if ageing has occurred.")
q(44, "Chemical warfare organophosphates listed are:", ["Sarin, tabun, VX and soman", "Tacrine, donepezil, rivastigmine and galantamine", "Edrophonium, neostigmine and pyridostigmine", "Pilocarpine, cevimeline, bethanechol and carbachol"], "The agents table lists sarin, tabun, VX and soman under chemical warfare agents.")
q(44, "Which obsolete miotic organophosphates are listed?", ["Echothiophate and fluostigmine", "Sarin and VX", "Pralidoxime and obidoxime", "Methacholine and carbachol"], "The miotic-agent row lists echothiophate and fluostigmine as obsolete miotic agents.")
q(44, "The side effects of obsolete miotic organophosphates include:", ["Cataract and iris cysts", "Dementia and BPH", "Tremor and hypokalemia", "Mydriasis and dry mouth"], "The side-effect column for obsolete miotic agents lists cataract and iris cysts.")
q(44, "Insecticides and pesticides acting as organophosphates cause:", ["Cholinergic symptoms", "Pure anticholinergic symptoms", "Only hyperkalemia", "Only dopamine depletion"], "The insecticide/pesticide row lists cholinergic symptoms as side effects.")
q(45, "The clinical presentation of organophosphate poisoning is:", ["Cholinergic symptoms", "Anticholinergic symptoms", "Dopamine withdrawal", "β-blockade"], "The organophosphate poisoning section starts with clinical presentation: cholinergic symptoms.")
q(45, "Which eye finding is listed in organophosphate poisoning?", ["Miosis", "Mydriasis", "Cycloplegia only", "Passive mydriasis"], "Miosis is the first clinical-presentation bullet.")
q(45, "Organophosphate poisoning increases:", ["Salivation and lacrimation", "Only dry mouth", "Only blood pressure", "Only dopamine release"], "The symptoms include increased salivation/lacrimation.")
q(45, "Which skin-gland feature is listed in organophosphate poisoning?", ["Increased sweating", "Absent sweating", "Dry skin only", "Conjunctival pigmentation"], "The clinical presentation includes ↑ sweating.")
q(45, "The respiratory symptom listed in organophosphate poisoning is:", ["Dyspnea", "Apnea only in neonates", "Bronchodilation without dyspnea", "Hiccup"], "Dyspnea is listed among the cholinergic symptoms.")
q(45, "Organophosphate poisoning causes which bowel and bladder effects?", ["Involuntary defecation and involuntary urination", "Constipation and urine retention", "Gastroparesis and overflow incontinence", "Peptic ulcer and dysmenorrhoea"], "The presentation list includes involuntary defecation and involuntary urination.")
q(45, "The DOC antimuscarinic for organophosphate poisoning is:", ["Atropine", "Physostigmine", "Methacholine", "Tacrine"], "The treatment section says antimuscarinic: atropine (DOC).")
q(45, "The most common marker used for adequate atropinisation is:", ["Pupil size", "Serum potassium", "FEV", "Plasma dopamine"], "Under marker of adequate atropinisation, the m/c marker is pupil size.")
q(45, "The most specific marker of adequate atropinisation is:", ["Normalisation of respiratory secretions", "Complete mydriasis", "Increase in sweating", "Fall in glucose"], "The note says the most specific marker is normalisation of respiratory secretions.")
q(45, "The antinicotinic treatment in organophosphate poisoning is:", ["AChE reactivators", "Muscarinic antagonists only", "β3 agonists", "VMAT2 inhibitors"], "The treatment section labels antinicotinic therapy as AChE reactivators.")
q(45, "The most specific AChE reactivators are:", ["Oximes", "Amides", "Choline esters", "Ganglion blockers"], "The AChE reactivator section states oximes are most specific.")
q(45, "Which oxime is most commonly used in India?", ["Pralidoxime (PAM)", "Obidoxime", "Diacetyl monoxime", "Physostigmine"], "The oxime list marks pralidoxime (PAM) as most commonly used in India.")
q(45, "Besides pralidoxime, the oximes listed are:", ["Obidoxime and diacetyl monoxime", "Tacrine and galantamine", "Edrophonium and pyridostigmine", "Pilocarpine and cevimeline"], "The oxime list includes obidoxime and diacetyl monoxime.")

unit("Reversible AChE Blockers: Mechanism and Tertiary Amines", "Carbamates and non-carbamates are called pseudo-irreversible because they are long acting, yet they bind AChE with weak ionic bonds rather than aged organophosphate bonds. Edrophonium is the short-acting exception that only binds the anionic site, and oximes are not used for carbamate/non-carbamate poisoning. Tertiary amines cross the BBB, so physostigmine treats anticholinergic poisoning and synthetic agents are used for Alzheimer's disease.")
q(45, "Reversible AChE blockers are also called pseudo-irreversible because they are:", ["Long acting", "Organophosphates", "Unable to bind AChE", "β2 agonists"], "The reversible blockers mechanism notes carbamates/non-carbamates are aka pseudo irreversible due to long-acting nature.")
q(45, "Carbamates/non-carbamates bind AChE mainly by:", ["Weak ionic bonds", "Strong aged phosphate bonds", "Covalent DNA bonds", "Hydrogen cyanide release"], "The mechanism diagram labels weak ionic bonds as the basis of short action.")
q(45, "Edrophonium is unique because it only binds the:", ["Anionic site", "Esteratic site", "β2 receptor", "D1 receptor"], "The diagram notes edrophonium only binds to the anionic site.")
q(45, "Oximes cannot be used to treat poisoning with:", ["Carbamates/non-carbamates", "Organophosphates before ageing", "Sarin exposure before ageing", "Tabun exposure before ageing"], "A note beside the reversible-blocker diagram states oximes cannot be used to Rx carbamate/non-carbamates.")
q(45, "Tertiary amine AChE inhibitors cross the BBB and therefore have:", ["Central action", "Only peripheral action", "Only ocular action", "No cholinergic action"], "The tertiary amine section says crosses blood-brain barrier → central action.")
q(45, "The natural tertiary amine AChE inhibitor is:", ["Physostigmine", "Neostigmine", "Pyridostigmine", "Edrophonium"], "The tertiary amine table lists physostigmine under natural drugs.")
q(45, "The synthetic tertiary amines listed are:", ["Tacrine, donepezil, rivastigmine and galantamine", "Edrophonium, neostigmine and pyridostigmine", "Sarin, tabun, VX and soman", "Bethanechol, carbachol and methacholine"], "The synthetic column lists tacrine, donepezil, rivastigmine and galantamine.")
q(45, "Physostigmine is DOC for poisoning due to:", ["Atropine or scopolamine", "Organophosphates after ageing", "β2 agonists", "Norepinephrine"], "The physostigmine use says anticholinergic poisoning (atropine/scopolamine): DOC.")
q(45, "Besides anticholinergic poisoning, physostigmine is also listed as a:", ["Miotic agent", "Nasal decongestant", "Uterine relaxant", "β3 agonist"], "The second physostigmine use in the table is miotic agent.")
q(45, "Synthetic tertiary AChE inhibitors are used in:", ["Alzheimer's disease", "Hypertensive emergency", "Acute CHF", "Anaphylactic shock"], "The synthetic tertiary amine column gives Alzheimer's disease as the use.")
q(45, "The natural source of physostigmine shown is:", ["Calabar beans from Physostigma venenosum", "Datura thorny fruit", "Rauwolfia root", "Ephedra plant"], "The figure labels Calabar beans and Physostigma venenosum as the natural source of physostigmine.")

unit("Quaternary AChE Inhibitors and Myasthenia Gravis", "Quaternary amines do not cross the BBB, so their action is peripheral. Edrophonium is a short-acting diagnostic drug for myasthenia gravis and separates myasthenic from cholinergic crisis by improvement versus worsening. Neostigmine is long acting for Nm and peripheral bladder/GIT uses, while pyridostigmine is the DOC for chronic myasthenia gravis; severe myasthenic crisis uses IVIG and newer chronic therapies lower antibodies.")
q(46, "Quaternary amine AChE inhibitors do not cross the BBB, so their action is:", ["Peripheral", "Central", "Only cortical", "Only ocular"], "The quaternary amine heading says they do not cross the BBB and have peripheral action.")
q(46, "Edrophonium is described as:", ["Short acting", "Long acting", "Irreversible", "A tertiary amine"], "The duration column for edrophonium reads short acting.")
q(46, "Edrophonium is DOC for diagnosing myasthenia gravis in the:", ["Tensilon test", "Bronchial challenge test", "Dale test", "Schirmer test"], "The edrophonium use states DOC for diagnosis of MG: Tensilon test.")
q(46, "In differentiating myasthenic crisis from cholinergic crisis, edrophonium worsening of symptoms indicates:", ["Cholinergic crisis", "Myasthenic crisis", "Neurogenic shock", "Tardive dyskinesia"], "The edrophonium flow says symptoms worsen → cholinergic crisis.")
q(46, "In the same edrophonium test, improvement of symptoms indicates:", ["Myasthenic crisis", "Cholinergic crisis", "Atropine poisoning", "Organophosphate ageing"], "The edrophonium flow says symptoms improve → myasthenic crisis.")
q(46, "Neostigmine is:", ["Long acting", "Short acting", "Only central acting", "An organophosphate"], "The duration column for neostigmine reads long acting.")
q(46, "Neostigmine's muscle action is on:", ["Nm only", "m3 only", "α1 only", "β3 only"], "The neostigmine muscle use says action on Nm only.")
q(46, "Neostigmine is used with atropine to prevent:", ["Muscarinic side effects", "Nicotinic Nm action", "AChE reactivation", "VMAT2 blockade"], "The neostigmine muscle note says it is used with atropine to prevent muscarinic side effects.")
q(46, "In cobra bite, neostigmine is useful because cobra toxin competitively inhibits ACh at:", ["Nicotinic Nm receptors", "β2 receptors", "D1 receptors", "m1 receptors"], "The cobra-bite line notes cobra toxin is a competitive inhibitor of ACh at the nicotinic receptor at the muscle end plate.")
q(46, "Neostigmine reverses:", ["Non-depolarising muscle relaxants", "Depolarising succinylcholine block", "β-blockers", "MAO inhibitors"], "One neostigmine muscle use is NDMR reversal.")
q(46, "Neostigmine is used for the treatment/diagnosis of:", ["Myasthenia gravis", "Pheochromocytoma", "Motion sickness", "ADHD"], "The neostigmine muscle use list includes Rx/Dx of MG.")
q(46, "Neostigmine treats bladder atony presenting as:", ["Overflow incontinence", "Urge incontinence", "Stress incontinence", "Polyuria"], "Under bladder uses, neostigmine is listed for bladder atony → overflow incontinence.")
q(46, "Which postoperative bladder problem is listed for neostigmine?", ["Post-operative urine retention", "Post-operative hematuria", "Post-operative incontinence from detrusor overactivity", "Post-operative anuria from renal failure"], "The bladder section includes post-operative urine retention.")
q(46, "Neostigmine is used in the GIT for:", ["Gastroparesis and paralytic ileus", "Peptic ulcer disease", "Infectious diarrhoea pain only", "Motion sickness"], "The GIT uses listed for neostigmine are gastroparesis and paralytic ileus.")
q(46, "Pyridostigmine is:", ["Long acting", "Short acting", "Only central", "A miotic organophosphate"], "The table lists pyridostigmine as long acting.")
q(46, "The DOC for treatment of myasthenia gravis is:", ["Pyridostigmine", "Edrophonium", "Tacrine", "Pilocarpine"], "The pyridostigmine row says Rx of MG: DOC.")
q(46, "The DOC for myasthenic crisis is:", ["IVIG", "Pyridostigmine", "Pilocarpine", "Atropine only"], "The myasthenia gravis note says DOC for myasthenic crisis: IVIG.")
q(46, "New chronic myasthenia gravis drugs aim at:", ["Immunosuppression with decreased antibodies", "Increasing salivary secretion only", "Blocking β2 receptors", "Raising norepinephrine levels"], "The note says new drugs for chronic MG act by immunosuppression/decreasing antibodies.")
q(46, "Complement-5 inhibitors for myasthenia gravis listed are:", ["Ravulizumab and zilucoplan", "Rozanolixizumab and tacrine", "Edrophonium and neostigmine", "Mirabegron and vibegron"], "The complement-5 inhibitor list contains ravulizumab and zilucoplan.")
q(46, "The neonatal Fc fragment inhibitor listed for myasthenia gravis is:", ["Rozanolixizumab", "Ravulizumab", "Zilucoplan", "Pyridostigmine"], "The neonatal Fc fragment inhibitor bullet names rozanolixizumab.")
q(46, "Datura poisoning is associated with a thorny fruit containing:", ["Atropine-like compounds", "Physostigmine", "Pralidoxime", "Acetylcholine"], "The figure labels Datura thorny fruit and notes Datura poisoning due to atropine-like compound.")

unit("Blood Pressure Responses to Acetylcholine", "Low-dose ACh lowers BP through m3-mediated vasodilation, and a larger dose gives a larger fall. If atropine blocks m3, ordinary ACh produces no BP effect. With high-dose ACh in the presence of atropine, ganglionic Nn stimulation releases norepinephrine, producing vasoconstriction and a pressor response.")
q(47, "Low-dose acetylcholine lowers blood pressure by causing:", ["m3-mediated vasodilation", "α1 vasoconstriction", "β1 cardiac stimulation", "D1 renal vasodilation only"], "The note says ACh causes vasodilation through m3 and decreases blood pressure.")
q(47, "Graph A represents the BP response to:", ["ACh 2 micrograms", "ACh 50 micrograms", "Atropine plus ACh", "ACh 5 mg after atropine"], "The first graph is labelled ACh 2 μg and shows a fall in BP.")
q(47, "Graph B represents the BP response to:", ["ACh 50 micrograms", "ACh 2 micrograms", "Atropine alone", "High-dose ACh 5 mg after atropine"], "The second graph is labelled ACh 50 μg and shows a larger fall in BP.")
q(47, "After atropine blocks m3 receptors, ACh 50 micrograms produces:", ["No effect on blood pressure", "A marked fall in BP", "A steep rise in BP", "Tachyphylaxis"], "The C note says ACh plus atropine, which blocks m3, has no effect on BP.")
q(47, "Graph C includes pretreatment with:", ["Atropine 2 mg before ACh 50 micrograms", "Mannitol before pilocarpine", "Pralidoxime before sarin", "Phenylephrine before ACh"], "The C graph is labelled atropine 2 mg followed by ACh 50 μg.")
q(47, "High-dose ACh in the presence of atropine stimulates:", ["Ganglionic Nn receptors", "β3 receptors in bladder", "m3 receptors in blood vessels", "D2 receptors"], "The D note says high-dose ACh plus atropine stimulates ganglionic Nn.")
q(47, "Ganglionic Nn stimulation by high-dose ACh increases:", ["Norepinephrine release", "Acetylcholine breakdown", "Insulin release only", "Aqueous outflow"], "The D pathway says stimulation of ganglionic Nn raises norepinephrine.")
q(47, "The BP response to high-dose ACh plus atropine is:", ["Vasoconstriction with increased blood pressure", "Vasodilation with decreased blood pressure", "No change in BP", "Only bradycardia without pressure change"], "The D pathway continues norepinephrine → vasoconstriction → increased blood pressure.")
q(47, "Graph D is labelled with which ACh dose?", ["ACh 5 mg", "ACh 2 micrograms", "ACh 50 micrograms", "Atropine 2 mg alone"], "The fourth graph is labelled ACh 5 mg and shows a pressor response.")

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
