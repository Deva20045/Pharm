# -*- coding: utf-8 -*-
import json
Q = []
def q(sec, page, text, opts, ans, exp):
    Q.append((sec, page, text, opts, ans, exp))

S1 = "Introduction to ANS: Components and Anatomy"
q(S1, 37, "The two components of the autonomic nervous system are:",
  ["Parasympathetic and sympathetic", "Somatic and autonomic",
   "Cranial and spinal", "Sympathetic and enteric"], 0,
  "The components chart divides the ANS into parasympathetic and sympathetic. (Book p37)")
q(S1, 37, "The ANS is located in the:",
  ["Neuraxis (brain + spinal cord)", "Peripheral nerves only", "Adrenal medulla only",
   "Enteric plexuses"], 0,
  "Under anatomy, the location is given as 'Neuraxis (Brain + spinal cord)'. (Book p37)")
q(S1, 37, "The cranial part of the parasympathetic outflow consists of which cranial nerves?",
  ["III, VII, IX and X", "III, V, VII and IX", "I, II, VIII and X", "V, VII, IX and XII"], 0,
  "The diagram labels the cranial part with nerves III, VII, IX and X arising from the brain stem. (Book p37)")
q(S1, 37, "The parasympathetic system is also called the:",
  ["Cranio-sacral part", "Thoraco-lumbar part", "Cervical part", "Lumbo-sacral plexus"], 0,
  "The label on the left of the diagram reads 'Cranio-sacral part of Parasympathetic System'. (Book p37)")
q(S1, 37, "The sympathetic system corresponds to the:",
  ["Thoraco-lumbar part", "Cranio-sacral part", "Cervical part only", "Sacral part only"], 0,
  "The bracket in the middle of the cord is labelled 'Thoraco-lumbar part of Sympathetic System'. (Book p37)")
q(S1, 37, "A ganglion is defined in the diagram as a:",
  ["Collection of neuronal bodies", "Bundle of axons", "Synapse between two muscles",
   "Collection of glial cells"], 0,
  "The diagram labels the ganglion as '(Collection of neuronal body)'. (Book p37)")
q(S1, 37, "In the two-neuron ANS pathway shown, the impulse passes:",
  ["From the 1st neuron to the ganglion and then the 2nd neuron to the organ",
   "Directly from the CNS to the organ", "From the organ to the CNS",
   "From the ganglion back to the CNS"], 0,
  "The diagram traces action potential → 1st neuron → ganglion → 2nd neuron → pupil/CVS. (Book p37)")
q(S1, 37, "Which organs are shown being supplied by the sympathetic second neuron?",
  ["Blood vessels and heart (CVS)", "Pupil only", "Salivary glands", "Bronchi"], 0,
  "The lower limb of the diagram ends at 'CVS → Blood vessel, Heart'. (Book p37)")

S2 = "Physiology of Action Potential: Propagation Across a Neuronal Synapse"
q(S2, 38, "The action potential depolarises the presynaptic neuron, which opens:",
  ["Voltage gated Ca2+ channels", "Voltage gated Na+ channels",
   "Ligand gated K+ channels", "Chloride channels"], 0,
  "The synapse diagram labels 'Opening of voltage gated Ca2+ channel' at the presynaptic terminal. (Book p38)")
q(S2, 38, "Ca2+ influx into the presynaptic neuron causes:",
  ["Fusion of vesicular membrane and presynaptic membrane with exocytosis of NT",
   "Opening of Na+ channels directly", "Reuptake of neurotransmitter",
   "Blockade of the receptor"], 0,
  "The second half of the figure is labelled 'Fusion of vesicular membrane and presynaptic membrane' with 'Exocytosis of NT + Bind to Receptor'. (Book p38)")
q(S2, 38, "The neurotransmitter released at the ganglion binds to:",
  ["The receptor on the post synaptic neuron", "The vesicle", "Ca2+ channels",
   "The presynaptic membrane"], 0,
  "The diagram shows exocytosis of NT and its binding to the 'Receptor' on the post-synaptic (ganglion) cell. (Book p38)")
q(S2, 38, "Binding of the neurotransmitter opens which channel on the post synaptic neuron?",
  ["Na+ channel", "K+ channel", "Cl- channel", "Ca2+ channel"], 0,
  "The figure is labelled 'Opening of Na+ channel + Influx'. (Book p38)")
q(S2, 38, "Influx of Na+ into the post synaptic neuron produces:",
  ["Depolarisation of the post synaptic neuron (action potential)",
   "Hyperpolarisation of the post synaptic neuron", "Release of more vesicles",
   "Blockade of the receptor"], 0,
  "The last step of the figure reads 'Depolarisation of post synaptic neuron (Action potential)'. (Book p38)")
q(S2, 38, "Neurotransmitter in the presynaptic neuron is stored in:",
  ["Vesicles", "The nucleus", "Mitochondria", "The synaptic cleft"], 0,
  "The presynaptic terminal is drawn with a 'Vesicle' containing neurotransmitter (NT). (Book p38)")

S3 = "Parasympathetic vs Sympathetic Innervation"
q(S3, 38, "The location of the parasympathetic outflow is:",
  ["Cranio-sacral", "Thoraco-lumbar", "Cervical only", "Sacral only"], 0,
  "The location row gives cranio-sacral for parasympathetic and thoraco-lumbar for sympathetic. (Book p38)")
q(S3, 38, "The sympathetic ganglia are located:",
  ["Away from the site of action (pre/para vertebral)", "Near the site of action",
   "Inside the target organ", "In the brain stem"], 0,
  "The ganglion row gives parasympathetic = near site of action and sympathetic = away from site of action (pre/para vertebral). (Book p38)")
q(S3, 38, "Parasympathetic ganglia are located:",
  ["Near the site of action", "Away from the site of action", "In the spinal cord",
   "In the adrenal medulla"], 0,
  "The ganglion row for parasympathetic reads 'Near site of action'. (Book p38)")
q(S3, 38, "The ganglionic receptor of both divisions is:",
  ["Nicotinic (Nn) - a sodium ion channel", "Muscarinic - a GPCR",
   "α/β adrenergic", "Nicotinic muscular (Nm)"], 0,
  "The ganglionic receptor row spans both columns and reads 'Nicotinic (Nn) : Sodium ion channel'. (Book p38)")
q(S3, 38, "The post-ganglionic receptor of the parasympathetic system is:",
  ["Muscarinic / Nicotinic", "α/β", "Nn only", "Nm only"], 0,
  "The post ganglionic receptor row gives muscarinic/nicotinic for parasympathetic and α/β for sympathetic. (Book p38)")
q(S3, 38, "The post-ganglionic receptor of the sympathetic system is:",
  ["α/β", "Muscarinic", "Nicotinic (Nn)", "Nm"], 0,
  "The sympathetic post ganglionic receptor is α/β. (Book p38)")
q(S3, 38, "The neurotransmitter of the entire parasympathetic system is:",
  ["Acetyl choline (Ach)", "Norepinephrine (NE)", "Dopamine", "Epinephrine"], 0,
  "The neurotransmitter row gives 'Acetyl choline (Ach)' for the parasympathetic column. (Book p38)")
q(S3, 38, "The pre-ganglionic neurotransmitter of the sympathetic system is:",
  ["Acetylcholine (Ach)", "Norepinephrine (NE)", "Dopamine", "Epinephrine"], 0,
  "Under sympathetic neurotransmitter the pre-ganglionic label reads 'Acetylcholine (Ach)'. (Book p38)")
q(S3, 38, "The post-ganglionic neurotransmitter of the sympathetic system is:",
  ["Norepinephrine (NE)", "Acetylcholine (Ach) only", "Dopamine only", "Serotonin"], 0,
  "The sympathetic post ganglionic list begins with Norepinephrine (NE). (Book p38)")
q(S3, 38, "Dopamine acting on renal blood vessels causes:",
  ["Vasodilatation leading to diuresis", "Vasoconstriction leading to oliguria",
   "No change in renal blood flow", "Bronchoconstriction"], 0,
  "The list reads 'Dopamine : Renal Blood vessels (D1 → Vasodilatation → Diuresis)'. (Book p38)")
q(S3, 38, "Which receptors receive acetylcholine as the post-ganglionic transmitter in the sympathetic system?",
  ["Adrenals and sweat glands", "Renal blood vessels", "The heart", "The bronchi"], 0,
  "The last sympathetic transmitter bullet reads 'Ach : Adrenals, sweat glands'. (Book p38)")
q(S3, 38, "Parasympatholytics such as atropine and datura block which receptors on sweat glands?",
  ["m3", "m1", "m2", "Nicotinic Nn"], 0,
  "The note reads 'Parasympatholytics (Atropine, Datura) : m3 blockade → Absent sweating'. (Book p38)")
q(S3, 38, "Absent sweating after m3 blockade leads to:",
  ["Hyperthermia", "Hypothermia", "Bradycardia", "Diarrhoea"], 0,
  "An arrow from 'absent sweating' leads to 'Hyperthermia'. (Book p38)")
q(S3, 38, "Sympatholytics have which effect on sweat glands?",
  ["No action", "Increased sweating", "Absent sweating", "Excessive salivation"], 0,
  "The note states 'Sympatholytics : No action' on sweat glands. (Book p38)")
q(S3, 38, "Directly acting ANS drugs:",
  ["Bind to the receptor", "Act on the neurotransmitter", "Block the synapse only",
   "Act on the vesicle"], 0,
  "Under 'Drugs in ANS' the page writes 'Direct acting : Binds to Receptor'. (Book p38)")
q(S3, 38, "Indirectly acting ANS drugs:",
  ["Act on the neurotransmitter (NT)", "Bind to the receptor",
   "Cross the blood-brain barrier", "Act only on the ganglion"], 0,
  "The page writes 'Indirect acting : Act on NT'. (Book p38)")

S4 = "Parasympathetic Nervous System: Acetylcholine Mechanism"
q(S4, 39, "Acetylcholine is synthesised from acetyl Co-A and choline by:",
  ["Choline acetyl transferase", "Acetylcholinesterase", "Choline reuptake transporter",
   "Catechol-O-methyl transferase"], 0,
  "The synthesis pathway in the diagram pairs acetyl Co-A with choline via 'Acetyl Transferase' to form ACh. (Book p39)")
q(S4, 39, "The rate limiting step in the acetylcholine cycle is:",
  ["Reuptake of choline", "Synthesis by acetyl transferase", "Entry of ACh into the vesicle",
   "Ca2+ influx"], 0,
  "The reuptake arrow is labelled 'Reuptake : Rate limiting step'. (Book p39)")
q(S4, 39, "Besides the presynaptic neuron, choline is also supplied from:",
  ["Food (minor source)", "The liver", "Muscle stores", "The adrenal gland"], 0,
  "The diagram shows 'minor Source : Food' feeding into the choline box. (Book p39)")
q(S4, 39, "ACh is stored in the presynaptic neuron by entering the:",
  ["Vesicle", "Nucleus", "Mitochondria", "Sarcoplasmic reticulum"], 0,
  "The step reads 'Enters vesicle' before the ACh is shown stored. (Book p39)")
q(S4, 39, "β-bungarotoxin acts by:",
  ["Blocking ACh entry into the vesicle", "Blocking the ACh receptor",
   "Inhibiting acetylcholinesterase", "Blocking Ca2+ influx"], 0,
  "The β-bungarotoxin pill carries a block mark on the step where ACh enters the vesicle. (Book p39)")
q(S4, 39, "Botulinum toxin prevents release of ACh by:",
  ["Blocking the vesicle release step", "Blocking the nicotinic receptor",
   "Destroying acetylcholinesterase", "Blocking choline reuptake"], 0,
  "The botulinum toxin block is drawn at the vesicle release point in the ACh mechanism diagram. (Book p39)")
q(S4, 39, "Aminoglycosides are shown blocking:",
  ["Ca2+ influx", "ACh synthesis", "Choline reuptake", "The muscarinic receptor"], 0,
  "The aminoglycoside pill sits on the Ca2+ influx arrow. (Book p39)")
q(S4, 39, "ACh is metabolised rapidly by:",
  ["Acetylcholine esterase (AChE)", "Choline acetyl transferase",
   "Monoamine oxidase", "Catechol-O-methyl transferase"], 0,
  "The diagram reads 'metabolised rapidly By Acetylcholine esterase (AChE)'. (Book p39)")
q(S4, 39, "AChE splits ACh into:",
  ["Acetate and choline", "Acetyl Co-A and choline", "Choline and water",
   "Acetate and acetyl Co-A"], 0,
  "The products shown in the diagram are acetate and choline. (Book p39)")
q(S4, 39, "The two sites on the AChE molecule are:",
  ["Esteratic site (breaks ester bonds) and anionic site (-vely charged)",
   "Active site and allosteric site", "Cationic site and hydrophobic site",
   "Estrogenic and anionic site"], 0,
  "The AChE drawing is labelled 'Esteratic site (breaks ester bonds)' and '-vely charged Anionic site'. (Book p39)")
q(S4, 39, "The choline produced by AChE breakdown is:",
  ["Positively charged and taken back up", "Negatively charged and excreted",
   "Neutral and fat soluble", "Converted to acetate"], 0,
  "The diagram labels the choline as '(+vely charged)' as it is reuptaken. (Book p39)")
q(S4, 39, "ACh released at the post-ganglionic junction acts on which receptors?",
  ["Muscarinic and nicotinic", "α and β", "Only nicotinic Nn", "Only β1"], 0,
  "The post-synaptic cell in the diagram carries both 'muscarinic' and 'Nicotinic' receptors. (Book p39)")

S5 = "Clinical Significance: Nm Receptor Action and Uses of Botulinum"
q(S5, 39, "Aminoglycosides cause muscular contraction to fall by:",
  ["Decreasing ACh (↓ Ach)", "Increasing ACh release", "Blocking the ACh receptor directly",
   "Inhibiting AChE"], 0,
  "The flow starts 'Aminoglycosides : muscular contraction (↓ Ach)'. (Book p39)")
q(S5, 39, "The neuromuscular toxicity caused by aminoglycosides is treated with:",
  ["DOC : Ca2+", "DOC : Atropine", "DOC : Physostigmine", "DOC : Neostigmine"], 0,
  "An arrow from neuromuscular toxicity leads to 'DOC : Ca2+' as the treatment. (Book p39)")
q(S5, 39, "Krait bite causes respiratory failure through:",
  ["β-bungarotoxin", "Cobra toxin", "Botulinum toxin", "Organophosphates"], 0,
  "The flow reads 'Krait bite : β-bungarotoxin → Respiratory failure'. (Book p39)")
q(S5, 39, "Cobra toxin causes:",
  ["Respiratory failure", "Floppy infant syndrome", "Tardive dyskinesia",
   "Angle closure glaucoma"], 0,
  "Cobra toxin is one of the arrows converging on respiratory failure. (Book p39)")
q(S5, 39, "Myasthenia crisis leads to:",
  ["Respiratory failure", "Hyperthermia", "Diuresis", "Hypertension"], 0,
  "Myasthenia crisis is connected by an arrow to respiratory failure. (Book p39)")
q(S5, 39, "Food poisoning with botulism leads to respiratory failure and also to:",
  ["Floppy infant syndrome", "Tardive dyskinesia", "Achalasia", "Migraine"], 0,
  "The flow reads 'Food Poisoning : Botulism → Respiratory failure' and continues down to 'Floppy Infant Syndrome'. (Book p39)")
q(S5, 39, "The management of respiratory failure in all these conditions is:",
  ["Ventilation", "Atropine", "Physostigmine", "Calcium gluconate"], 0,
  "Below respiratory failure the flow states 'mx : ventilation'. (Book p39)")
q(S5, 39, "Botulinum toxin is used in tardive dyskinesia (torticollis/cervical dystonia) by injection into the:",
  ["Sternocleidomastoid (SCM)", "Trapezius", "Deltoid", "Masseter"], 0,
  "The first use listed is 'Tardive dyskinesia (Torticollis/Cervical dystonia) : Injected into SCM'. (Book p39)")
q(S5, 39, "Botulinum toxin is used in which bladder condition?",
  ["Urge incontinence/overactive bladder", "Neurogenic bladder with retention",
   "Bladder cancer", "Interstitial cystitis"], 0,
  "The second use listed is 'urge Incontinence/Overactive bladder'. (Book p39)")
q(S5, 39, "Botulinum toxin is used cosmetically to remove:",
  ["Glabellar lines", "Wrinkles on the hands", "Acne scars", "Melasma"], 0,
  "The cosmetic use given is 'To remove glabellar lines'. (Book p39)")
q(S5, 39, "Botulinum toxin relieves achalasia by relaxing the:",
  ["Lower esophageal sphincter", "Upper esophageal sphincter", "Pylorus",
   "Cardia fundus only"], 0,
  "The use reads 'unrelaxed Lower esophageal sphincter → Achalasia'. (Book p39)")
q(S5, 39, "Botulinum toxin is useful in migraine prophylaxis because it reduces release of:",
  ["CGRP (calcitonin gene-related peptide)", "Substance P", "Nitric oxide",
   "Vasoactive intestinal peptide"], 0,
  "The last use reads 'migraine prophylaxis : D/t ↓ CGRP (Calcitonin gene-related peptide) release'. (Book p39)")
q(S5, 39, "In the respiratory failure flow, myasthenia crisis, cobra toxin and botulism all share which final mechanism?",
  ["Failure of neuromuscular transmission leading to respiratory failure",
   "Direct central nervous system depression", "Airway obstruction",
   "Pulmonary embolism"], 0,
  "All three arrows converge on respiratory failure, with the management being ventilation. (Book p39)")

S6 = "Receptors: Nicotinic Receptors"
q(S6, 40, "The two types of cholinergic receptors are:",
  ["Muscarinic (m) - GPCRs and nicotinic (N) - Na+ ion channels",
   "α and β", "m1 and m2 only", "Nn and Nm only"], 0,
  "The receptor types chart splits into 'muscarinic (m) : G-protein coupled receptors (GPCR)' and 'Nicotinic (N) : Na+ ion channels'. (Book p40)")
q(S6, 40, "Muscarinic receptors are:",
  ["G-protein coupled receptors", "Na+ ion channels", "Nuclear receptors",
   "Tyrosine kinase receptors"], 0,
  "The muscarinic branch is labelled G-protein coupled receptors (GPCR). (Book p40)")
q(S6, 40, "Nicotinic receptors are:",
  ["Na+ ion channels", "GPCRs", "K+ channels", "Cl- channels"], 0,
  "The nicotinic branch is labelled 'Na+ ion channels'. (Book p40)")
q(S6, 40, "Nicotinic muscular (Nm) receptors are found at the:",
  ["Neuromuscular junction (NMJ)", "Adrenal glands", "Ganglia", "CNS"], 0,
  "The table site column for nicotinic muscular (Nm) is the neuromuscular junction (NMJ). (Book p40)")
q(S6, 40, "Stimulation of nicotinic muscular (Nm) receptors produces:",
  ["Muscle contraction", "Stimulation of the CNS", "Release of epinephrine",
   "Action potential generation in ganglia"], 0,
  "The action column for Nm reads 'muscle contraction'. (Book p40)")
q(S6, 40, "Nicotinic neuronal (Nn) receptors at the adrenal glands cause:",
  ["↑ Norepinephrine in medulla → cortisol from cortex → epinephrine released into plasma",
   "Muscle contraction", "Bronchoconstriction", "Miosis"], 0,
  "The action cell for the adrenal glands reads '↑ Norepinephrine in medulla → Cortisol (From cortex) → Epinephrine (Released into plasma)'. (Book p40)")
q(S6, 40, "At ganglia, nicotinic neuronal (Nn) receptors:",
  ["Generate action potential", "Cause muscle contraction", "Stimulate the CNS only",
   "Release cortisol"], 0,
  "The ganglia row action is 'Generate Action Potential'. (Book p40)")
q(S6, 40, "In the CNS, nicotinic neuronal receptors cause:",
  ["Stimulation", "Inhibition", "Muscle contraction", "Vasodilation"], 0,
  "The CNS row of the nicotinic receptor table reads 'Stimulation'. (Book p40)")
q(S6, 40, "In myasthenia gravis, anti-ACh antibodies:",
  ["Block Nm receptors, decreasing muscle contraction", "Block Nn receptors at ganglia",
   "Destroy acetylcholinesterase", "Block muscarinic receptors"], 0,
  "The clinical significance reads 'Anti-Ach Antibodies → Block Nm → ↓ Muscle contraction'. (Book p40)")
q(S6, 40, "The symptoms of myasthenia gravis listed are:",
  ["Fatigue, ptosis and respiratory failure (crisis)", "Diarrhoea, miosis and lacrimation",
   "Dry mouth, mydriasis and constipation", "Fever and rash"], 0,
  "The symptoms listed are fatigue, ptosis and respiratory failure (crisis). (Book p40)")

S7 = "Muscarinic Receptors"
q(S7, 40, "Which muscarinic receptors act through Gq and increased Ca2+?",
  ["m1 and m3", "m2 and m4", "m5 only", "m2 only"], 0,
  "The bracket beside m1 and m3 is labelled 'Gq → ↑ Ca2+'. (Book p40)")
q(S7, 40, "m1 receptors in the CNS cause:",
  ["↑ Cognition", "↑ HCl secretion", "Miosis", "Bronchoconstriction"], 0,
  "The m1 CNS row reads '↑ Cognition'. (Book p40)")
q(S7, 40, "m1 receptors in the GIT cause:",
  ["↑ HCl secretion", "↑ Contraction", "Detrusor contraction", "Salivation"], 0,
  "The m1 GIT row reads '↑ HCl Secretion'. (Book p40)")
q(S7, 40, "Stimulation of m3 receptors in the GIT produces:",
  ["↑ Contraction", "↑ HCl secretion only", "Relaxation", "No effect"], 0,
  "The m3 GIT row reads '↑ Contraction'. (Book p40)")
q(S7, 40, "m3 receptors in the bladder cause the detrusor to:",
  ["Increase contraction", "Relax", "Have no effect", "Secrete mucus"], 0,
  "The m3 bladder row reads 'Detrusor → ↑ Contraction'. (Book p40)")
q(S7, 40, "m3 receptors in the bronchi cause:",
  ["Bronchoconstriction", "Bronchodilation", "Mucus secretion only", "No effect"], 0,
  "The m3 bronchi row reads 'Bronchoconstriction'. (Book p40)")
q(S7, 40, "m3 receptors on salivary glands cause:",
  ["↑ Salivation", "Dry mouth", "Miosis", "Vasodilation"], 0,
  "The m3 salivary glands row reads '↑ Salivation'. (Book p40)")
q(S7, 40, "m3 receptors on the circular muscle of the iris cause:",
  ["Miosis (pupil contraction)", "Mydriasis", "Accommodation spasm", "Ptosis"], 0,
  "The m3 circular muscle of iris row reads 'miosis (Pupil Contraction)'. (Book p40)")
q(S7, 40, "m3 receptors on the ciliary muscle cause:",
  ["Accommodation spasm", "Miosis", "Mydriasis", "Lacrimation"], 0,
  "The m3 ciliary muscle row reads 'Accommodation spasm'. (Book p40)")
q(S7, 40, "The effect of m3 on blood vessels is:",
  ["Vasodilation > vasoconstriction, by activating eNOS in the endothelium",
   "Vasoconstriction > vasodilation by smooth muscle", "Pure vasoconstriction",
   "No effect on blood vessels"], 0,
  "The m3 blood vessels row reads 'vasodilation > vasoconstriction (Endothelium : Activates eNOS) (Smooth muscle)'. (Book p40)")
q(S7, 40, "eNOS stands for:",
  ["Endothelial Nitric Oxide Synthase", "Endothelial Nitric Oxide System",
   "Endogenous Nitric Oxide Synthase", "Endothelial Nicotinamide Oxidase Synthase"], 0,
  "The footnote at the bottom of the table expands eNOS as 'Endothelial Nitric Oxide Synthase'. (Book p40)")
q(S7, 40, "The effects of m5 and m4 receptors (CNS) are shown as:",
  ["A dash, i.e. not specified", "↑ Cognition", "Stimulation", "Relaxation"], 0,
  "Both the m5 and m4 rows (CNS) carry only a dash in the action column. (Book p40)")
q(S7, 40, "m2 receptors act through which G protein?",
  ["Gi/o, producing relaxation", "Gq, producing ↑ Ca2+", "Gs, producing ↑ cAMP",
   "G12/13"], 0,
  "The bracket beside m2/m4 is labelled 'Gi/o → Relaxation'. (Book p40)")
q(S7, 40, "Blockade of m3 receptors in the heart produces:",
  ["SA node : ↓ heart rate and AV node : ↓ conduction", "↑ heart rate and ↑ conduction",
   "No change in heart rate", "Increased contractility"], 0,
  "The m2 heart row shows 'Block → SA node : ↓ Heart rate; AV node : ↓ Conduction'. (Book p40)")

S8 = "Clinical Significance: Alzheimer's Disease"
q(S8, 41, "In Alzheimer's disease, the neurotransmitter change is:",
  ["↓ ACh → ↓ m1 stimulation → ↓ Cognition", "↑ ACh → ↑ m1 stimulation → ↑ Cognition",
   "↓ Dopamine → ↓ cognition", "↑ NE → ↑ cognition"], 0,
  "The clinical significance reads '↓ ACh → ↓ m1 stimulation → ↓ cognition'. (Book p41)")
q(S8, 41, "The drug used in Alzheimer's disease as an m1 agonist is:",
  ["Tacilifensin", "Physostigmine", "Atropine", "Donepezil"], 0,
  "The prescription line reads 'Rx : Tacilifensin (m1 Agonist)'. (Book p41)")
q(S8, 41, "Tacilifensin acts as an:",
  ["m1 agonist", "m1 antagonist", "m2 agonist", "Nm blocker"], 0,
  "The page specifies tacilifensin as an m1 agonist for Alzheimer's disease. (Book p41)")

S9 = "Cholinergic and Anticholinergic Poisoning"
q(S9, 41, "Cholinergic poisoning is caused by:",
  ["Organophosphates/carbamates", "Atropine and datura", "Tacilifensin",
   "Botulinum toxin"], 0,
  "The drugs row for cholinergic poisoning reads 'Organophosphates/Carbamates'. (Book p41)")
q(S9, 41, "The drugs causing anticholinergic poisoning are:",
  ["Atropine and datura", "Organophosphates", "Carbamates", "Physostigmine"], 0,
  "The drugs row for anticholinergic poisoning reads 'Atropine, Datura'. (Book p41)")
q(S9, 41, "In cholinergic poisoning the eyes show:",
  ["Miosis (pinpoint pupil) and lacrimation", "Mydriasis", "Dry eyes",
   "Ptosis only"], 0,
  "The eyes row for cholinergic reads 'miosis (Pinpoint pupil), Lacrimation'. (Book p41)")
q(S9, 41, "In anticholinergic poisoning the eyes show:",
  ["Mydriasis", "Miosis", "Lacrimation", "No change"], 0,
  "The eyes row for anticholinergic reads 'mydriasis'. (Book p41)")
q(S9, 41, "Cholinergic poisoning affects the salivary glands as:",
  ["↑ Salivation", "Dry mouth", "↑ HCl secretion", "No effect"], 0,
  "The salivary gland row for cholinergic reads '↑ Salivation'. (Book p41)")
q(S9, 41, "Anticholinergic poisoning causes which salivary change?",
  ["Dry mouth", "↑ salivation", "Bloody saliva", "Foaming at the mouth"], 0,
  "The salivary gland row for anticholinergic reads 'Dry mouth'. (Book p41)")
q(S9, 41, "In cholinergic poisoning the bronchi show:",
  ["Bronchoconstriction : dyspnea", "Bronchodilation", "Cough only", "No change"], 0,
  "The bronchi row for cholinergic reads 'Bronchoconstriction : Dyspnea'. (Book p41)")
q(S9, 41, "In anticholinergic poisoning the bronchi show:",
  ["Bronchodilation", "Bronchoconstriction", "Dyspnea", "Wheeze"], 0,
  "The bronchi row for anticholinergic reads 'Bronchodilation'. (Book p41)")
q(S9, 41, "Cholinergic poisoning produces which gastrointestinal effect?",
  ["Involuntary defecation", "Constipation", "Ileus", "Bloody diarrhoea"], 0,
  "The GIT row for cholinergic reads 'Involuntary Defecation'. (Book p41)")
q(S9, 41, "Anticholinergic poisoning produces which gastrointestinal effect?",
  ["Constipation", "Involuntary defecation", "Diarrhoea", "Vomiting"], 0,
  "The GIT row for anticholinergic reads 'Constipation'. (Book p41)")
q(S9, 41, "In cholinergic poisoning the bladder shows:",
  ["Involuntary urination", "Urine retention", "Hematuria", "No effect"], 0,
  "The bladder row for cholinergic reads 'Involuntary urination'. (Book p41)")
q(S9, 41, "In anticholinergic poisoning the bladder shows:",
  ["Urine retention", "Involuntary urination", "Polyuria", "Dysuria only"], 0,
  "The bladder row for anticholinergic reads 'urine Retention'. (Book p41)")
q(S9, 41, "Sweating in cholinergic poisoning is:",
  ["Increased (↑ Sweating)", "Decreased", "Absent", "Unchanged"], 0,
  "The sweat glands row for cholinergic reads '↑ Sweating'. (Book p41)")
q(S9, 41, "Sweating in anticholinergic poisoning is:",
  ["Decreased (↓ Sweating)", "Increased", "Normal", "Excessive"], 0,
  "The sweat glands row for anticholinergic reads '↓ Sweating'. (Book p41)")
q(S9, 41, "The drug of choice for cholinergic poisoning is:",
  ["Atropine", "Physostigmine", "Tacilifensin", "Pralidoxime"], 0,
  "The DOC row for cholinergic poisoning reads 'Atropine'. (Book p41)")
q(S9, 41, "The drug of choice for anticholinergic poisoning is:",
  ["Physostigmine", "Atropine", "Datura", "Neostigmine"], 0,
  "The DOC row for anticholinergic poisoning reads 'Physostigmine'. (Book p41)")
q(S9, 41, "Which single feature best distinguishes cholinergic from anticholinergic poisoning at the bedside?",
  ["Pinpoint pupil with sweating versus mydriasis with dry skin",
   "Fever in both, differing only in severity", "Both cause urine retention",
   "Both cause constipation"], 0,
  "Cholinergic poisoning gives miosis, lacrimation, ↑ sweating and involuntary urination/defecation; anticholinergic gives mydriasis, dry mouth, ↓ sweating, urine retention and constipation. (Book p41)")

UNITS = [
 (1, "Introduction to ANS: Components and Anatomy", [1,8],
  "The ANS has two components, parasympathetic and sympathetic, and is located in the neuraxis (brain + spinal cord). The parasympathetic is the cranio-sacral part - cranial nerves III, VII, IX and X from the brain stem plus the sacral outflow - while the sympathetic is the thoraco-lumbar part. Both use a two-neuron pathway: action potential travels along the 1st neuron to a ganglion (a collection of neuronal bodies) and then along the 2nd neuron to the organ, such as the pupil or the CVS (blood vessel, heart)."),
 (2, "Physiology of Action Potential: Propagation Across a Neuronal Synapse", [9,14],
  "An action potential depolarises the presynaptic neuron, opening voltage gated Ca2+ channels; the resulting Ca2+ influx causes fusion of the vesicular and presynaptic membranes with exocytosis of neurotransmitter, which binds the post synaptic receptor. This opens Na+ channels, Na+ influx follows, and the post synaptic neuron depolarises to generate its own action potential. Neurotransmitter is stored in vesicles in the presynaptic terminal."),
 (3, "Parasympathetic vs Sympathetic Innervation", [15,30],
  "Parasympathetic outflow is cranio-sacral with ganglia near the site of action; sympathetic outflow is thoraco-lumbar with ganglia away from the site of action (pre/para vertebral). Both use nicotinic (Nn) ganglionic receptors that are sodium ion channels. Post-ganglionic parasympathetic receptors are muscarinic/nicotinic with acetylcholine as the transmitter throughout; sympathetic post-ganglionic receptors are α/β with norepinephrine, plus dopamine on renal blood vessels (D1 → vasodilatation → diuresis) and Ach at adrenals and sweat glands. Note: parasympatholytics (atropine, datura) block m3 on sweat glands causing absent sweating and hyperthermia, whereas sympatholytics have no action there. Drugs may act directly (binding the receptor) or indirectly (acting on the neurotransmitter)."),
 (4, "Parasympathetic Nervous System: Acetylcholine Mechanism", [31,42],
  "ACh is synthesised from acetyl Co-A and choline by choline acetyl transferase, with choline reuptake as the rate limiting step and food as a minor source of choline. It enters the vesicle and is released; β-bungarotoxin blocks entry into the vesicle, botulinum toxin blocks vesicle release and aminoglycosides block Ca2+ influx. Released ACh acts on muscarinic and nicotinic receptors and is metabolised rapidly by acetylcholinesterase (AChE), which breaks ACh into acetate and choline. AChE has an esteratic site (breaks ester bonds) and a negatively charged anionic site, and the choline released is positively charged and reuptaken."),
 (5, "Clinical Significance: Nm Receptor Action and Uses of Botulinum", [43,55],
  "At the Nm receptor, aminoglycosides reduce muscular contraction by lowering ACh and cause neuromuscular toxicity treated with Ca2+ as DOC. Respiratory failure is the common end point of krait bite (β-bungarotoxin), myasthenia crisis, cobra toxin and food poisoning with botulism (which also causes floppy infant syndrome), and its management is ventilation. Botulinum toxin is used in tardive dyskinesia (torticollis/cervical dystonia, injected into the SCM), urge incontinence/overactive bladder, cosmetically for glabellar lines, for unrelaxed lower esophageal sphincter causing achalasia, and for migraine prophylaxis by reducing CGRP release."),
 (6, "Receptors: Nicotinic Receptors", [56,65],
  "Cholinergic receptors are of two types: muscarinic (m), which are GPCRs, and nicotinic (N), which are Na+ ion channels. Nicotinic muscular (Nm) receptors at the neuromuscular junction produce muscle contraction; nicotinic neuronal (Nn) receptors at adrenal glands raise medullary norepinephrine, then cortisol from the cortex and finally epinephrine released into plasma, at ganglia generate action potential, and in the CNS cause stimulation. In myasthenia gravis anti-ACh antibodies block Nm and decrease muscle contraction, giving fatigue, ptosis and respiratory failure (crisis)."),
 (7, "Muscarinic Receptors", [66,79],
  "Muscarinic receptors split by G protein: m1 and m3 work through Gq → ↑ Ca2+, while m2/m4 work through Gi/o → relaxation. m1 in the CNS raises cognition and in the GIT raises HCl secretion. m3 causes GIT contraction, detrusor contraction in the bladder, bronchoconstriction, ↑ salivation, miosis (pupil contraction) in the circular muscle of the iris, accommodation spasm in the ciliary muscle, and in blood vessels vasodilation > vasoconstriction by activating eNOS in the endothelium. m5/m4 (CNS) are shown with a dash, and m2 blockade in the heart slows the SA node (↓ heart rate) and AV node (↓ conduction)."),
 (8, "Clinical Significance: Alzheimer's Disease", [80,82],
  "In Alzheimer's disease there is ↓ ACh, so ↓ m1 stimulation and ↓ cognition. Treatment is with tacilifensin, an m1 agonist."),
 (9, "Cholinergic and Anticholinergic Poisoning", [83,99],
  "Cholinergic poisoning from organophosphates/carbamates gives miosis (pinpoint pupil) with lacrimation, ↑ salivation, bronchoconstriction with dyspnea, involuntary defecation, involuntary urination and ↑ sweating - the drug of choice being atropine. Anticholinergic poisoning from atropine and datura gives exactly the opposite picture: mydriasis, dry mouth, bronchodilation, constipation, urine retention and ↓ sweating - the drug of choice being physostigmine."),
]

byid = {}
for i, (sec, page, text, opts, ans, exp) in enumerate(Q, 1):
    byid[i] = {"id": f"PHARM-C12-{i:03d}", "sec": sec, "page": page, "q": text,
               "opts": opts, "ans": ans, "exp": exp}
questions = [byid[i] for i in sorted(byid)]
units = []
for n, title, (a, b), guide in UNITS:
    for i in range(a, b + 1):
        byid[i]["sec"] = title
    units.append({"id": f"PHARM-U12-{n}", "ch": 12, "n": n, "title": title,
                  "sec": f"{title} · p{byid[a]['page']}",
                  "qs": [f"PHARM-C12-{i:03d}" for i in range(a, b + 1)],
                  "guide": guide})
json.dump({"questions": questions, "units": units},
          open("data/ch12.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("questions:", len(questions), "units:", len(units))
for u in units:
    print(" ", u["id"], u["title"], len(u["qs"]), u["sec"])
