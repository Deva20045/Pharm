# -*- coding: utf-8 -*-
import json, os, io, sys

Q = []   # (sec, page, q, [4 opts], ans, exp)
def q(sec, page, text, opts, ans, exp):
    Q.append((sec, page, text, opts, ans, exp))

S1 = "Types of Antagonism"
q(S1, 20, "Physical antagonism produces its effect by:",
  ["Physical binding to the substance", "Binding and neutralising the substance",
   "Acting on a receptor opposite to the agonist", "Inhibiting the metabolising enzyme"], 0,
  "The page defines physical antagonism as an effect produced by physical binding to the substance, without any chemical reaction or receptor involvement. (Book p20)")
q(S1, 20, "Charcoal given in alcohol toxicity is an example of:",
  ["Physical antagonism", "Chemical antagonism", "Physiological antagonism",
   "Non-competitive antagonism"], 0,
  "The book's example under physical antagonism is charcoal in alcohol toxicity, where charcoal simply binds (adsorbs) alcohol. (Book p20)")
q(S1, 20, "How does charcoal act in alcohol toxicity?",
  ["It adsorbs alcohol from the intestine", "It neutralises alcohol chemically in the stomach",
   "It blocks alcohol receptors in the brain", "It increases alcohol metabolism in the liver"], 0,
  "The bracket after the example reads 'charcoal adsorbs alcohol from intestine' - a purely physical, adsorptive binding. (Book p20)")
q(S1, 20, "Chemical antagonism means the antagonist:",
  ["Binds and neutralises the substance", "Binds the substance physically without reaction",
   "Acts through a receptor of opposite type", "Displaces the agonist from its receptor"], 0,
  "The heading 'Chemical Antagonism' is explained as 'Effect by binding & neutralizing the substance'. (Book p20)")
q(S1, 20, "Heparin is neutralised by:",
  ["Protamine sulphate", "Charcoal", "Salbutamol", "Calcium gluconate"], 0,
  "The diagram shows heparin (acid, -ve) being neutralised by protamine sulphate (base, +ve) - the classic chemical antagonism. (Book p20)")
q(S1, 20, "In the heparin-protamine pair, heparin is ____ and protamine sulphate is ____:",
  ["Acid (-ve); base (+ve)", "Base (+ve); acid (-ve)", "Acid (+ve); base (-ve)",
   "Neutral; charged"], 0,
  "The page marks heparin as 'Acid : -ve' and protamine sulphate as 'Base : +ve', which is why the two combine chemically. (Book p20)")
q(S1, 20, "Which cells are noted to contain heparin?",
  ["Mast cells", "Hepatocytes", "Platelets only", "Plasma cells"], 0,
  "The note under chemical antagonism states 'mast cells contain heparin'. (Book p20)")
q(S1, 20, "Which of the following is the example of a chelating agent for iron?",
  ["Deferiprone", "Protamine sulphate", "Charcoal", "Ipratropium"], 0,
  "Under 'Chelating agents' the book lists Fe : Dexrazoxane, Deferiprone - both are iron chelators. (Book p20)")
q(S1, 20, "Copper is removed using:",
  ["Copper chelating agents", "Protamine sulphate", "Charcoal adsorption", "β2 agonists"], 0,
  "The chelating agent list on the page gives 'Copper : Copper chelating agents'. (Book p20)")
q(S1, 20, "Physiological antagonism is defined as:",
  ["Opposite effect produced by acting on different receptors",
   "Binding of the drug to a physiological salt", "Neutralisation of the drug by a chemical",
   "Irreversible binding to the same receptor"], 0,
  "The page defines physiological antagonism as 'Opposite effect by acting on the different receptors'. (Book p20)")
q(S1, 20, "Histamine acting on H1 receptors causes:",
  ["Bronchoconstriction", "Bronchodilation", "Vasodilation of bronchial vessels",
   "Uterine relaxation"], 0,
  "In the physiological antagonism example, 'Histamine -(+)→ H1 causes → Bronchoconstriction'. (Book p20)")
q(S1, 20, "Which pair is used as the example of physiological antagonism of histamine?",
  ["Adrenaline and salbutamol acting on β2", "Heparin and protamine sulphate",
   "Charcoal and alcohol", "M1 and M2 receptors"], 0,
  "Both adrenaline and salbutamol are shown acting on β2 receptors to cause bronchodilation, opposing the H1-mediated bronchoconstriction. (Book p20)")
q(S1, 20, "In the page's flow, histamine causes bronchoconstriction while adrenaline and salbutamol cause:",
  ["Bronchodilation via β2", "Bronchoconstriction via β2", "Bronchodilation via H1",
   "Mucus secretion via M3"], 0,
  "The two arms of the example meet at the airway: H1 → bronchoconstriction, β2 → bronchodilation. (Book p20)")
q(S1, 20, "Which drug does the page call the best bronchodilator in asthma?",
  ["Salbutamol", "Ipratropium", "Tiotropium", "Theophylline"], 0,
  "An arrow from the salbutamol/adrenaline line carries the note 'Best bronchodilator in Asthma'. (Book p20)")
q(S1, 20, "Why is salbutamol NOT the best bronchodilator in COPD?",
  ["Because of cholinergic effects", "Because it is a β2 blocker",
   "Because it has no bronchodilator action in COPD", "Because it causes bronchoconstriction"], 0,
  "The note says 'Salbutamol not the best bronchodilator in COPD due to cholinergic effects'. (Book p20)")
q(S1, 20, "Instead of salbutamol, which drug class is preferred for bronchodilation in COPD?",
  ["Parasympathetic blockers such as ipratropium/tiotropium", "β2 agonists such as ritodrine",
   "Phosphodiesterase 3 inhibitors such as milrinone", "Iron chelators"], 0,
  "The note advises 'use Ipratropium/Tiotropium instead (Parasympathetic blocker)'. (Book p20)")
q(S1, 20, "Which of the following is a physical antagonist?",
  ["Charcoal", "Protamine sulphate", "Ipratropium", "Fasudil"], 0,
  "Only charcoal acts by physical binding/adsorption; protamine is a chemical antagonist and ipratropium/fasudil act through receptors/enzymes. (Book p20)")

S2 = "Competitive Reversible vs Irreversible/Non-competitive Antagonism"
q(S2, 20, "In the antagonism table, row (a) depicts:",
  ["Normal effect with drug (A)", "Addition of antagonist drug (B)",
   "Effect on (A) of increasing drug (A)", "Effect of enzyme inhibition"], 0,
  "Row 'a' of the two-column table is headed 'Normal effect with drug (A)', showing the baseline response. (Book p20)")
q(S2, 20, "On the receptor drawing, drug (A) normally binds to the:",
  ["Enzymatic part", "Allosteric part", "Lipid bilayer", "G-protein subunit"], 0,
  "In row (a) the labelled arrow from (A) points to the 'Enzymatic part' of the receptor, while the lower site is marked 'Allosteric part'. (Book p20)")
q(S2, 20, "In competitive reversible antagonism, the antagonist (B) binds at the:",
  ["Same site as the agonist (A)", "Allosteric site only", "Second messenger",
   "GTP binding site"], 0,
  "Row (b) shows (A) and (B) competing for the same binding site of the receptor. (Book p20)")
q(S2, 20, "In non-competitive (and competitive irreversible) antagonism, the antagonist (B) binds at the:",
  ["Allosteric part", "Enzymatic part", "Same site as (A)", "Receptor's lipid tail"], 0,
  "Row (b) of the non-competitive column shows (A) at the enzymatic part and (B) binding the allosteric part. (Book p20)")
q(S2, 20, "Row (c) of the table studies:",
  ["Effect on (A) of increasing the dose of drug (A)", "Effect of adding a second antagonist",
   "Effect of removing drug (A)", "Effect of adding an enzyme inducer"], 0,
  "Row 'c' is headed 'Effect on A of ↑ drug (A)' - i.e. what happens when the agonist concentration is raised. (Book p20)")
q(S2, 20, "On increasing drug (A) in reversible competitive antagonism, the response:",
  ["Returns, because the antagonism is surmountable", "Remains fully blocked",
   "Is permanently abolished", "Becomes toxic"], 0,
  "Row (c) of the reversible column shows more (A) molecules out-competing (B), so the effect can be restored by raising the agonist dose. (Book p20)")
q(S2, 20, "On increasing drug (A) in competitive irreversible/non-competitive antagonism, the result written is:",
  ["'B - No change'", "'Full reversal of blockade'", "'Increased efficacy'", "'Decreased Km'"], 0,
  "The bottom cell of the non-competitive column carries the note '(B) No change' - raising (A) cannot overcome the block. (Book p20)")
q(S2, 21, "In the continued table, the 'net effect of drug (A)' in reversible competitive antagonism shows:",
  ["An upward arrow (effect restored)", "No change", "A downward arrow",
   "A biphasic response"], 0,
  "The 'Net effect of drug (A)' row has an up arrow under reversible competitive antagonism and 'No change' under the other column. (Book p21)")
q(S2, 21, "In the continued table, the 'net effect of drug (A)' with irreversible/non-competitive antagonism shows:",
  ["No change", "Increase", "Decrease to zero only", "Reversal of antagonism"], 0,
  "The row 'Net effect of drug (A)' reads 'No change' in the irreversible/non-competitive column. (Book p21)")
q(S2, 21, "The dose-response curves drawn for reversible competitive antagonism shift:",
  ["To the right, with the maximum preserved", "To the left, with a higher maximum",
   "Downwards only", "Do not shift at all"], 0,
  "Curves a, b and c are shown moving progressively right with the same height, i.e. a parallel rightward shift of the DRC. (Book p21)")
q(S2, 21, "The dose-response curves for competitive irreversible/non-competitive antagonism are labelled:",
  ["'No reversal of antagonism'", "'Reversible shift'", "'Increase in efficacy'", "'Km unchanged'"], 0,
  "The right-hand panel writes 'No reversal of antagonism' next to the family of curves a, b, c. (Book p21)")
q(S2, 21, "In reversible competitive antagonism, Vmax (α efficacy) shows:",
  ["No change", "A fall", "A rise", "A fall then rise"], 0,
  "The Vmax row is 'No change' for competitive reversible antagonism - efficacy is preserved. (Book p21)")
q(S2, 21, "In competitive irreversible/non-competitive antagonism, Vmax (α efficacy):",
  ["Falls", "Rises", "Is unchanged", "Doubles"], 0,
  "The Vmax row carries a downward arrow in the irreversible/non-competitive column, i.e. efficacy is reduced. (Book p21)")
q(S2, 21, "In reversible competitive antagonism, Km (α 1/Potency):",
  ["Increases", "Decreases", "Is unchanged", "Becomes zero"], 0,
  "The Km row has an upward arrow for reversible competitive antagonism, while it stays 'No change' for the other column. (Book p21)")
q(S2, 21, "In competitive irreversible/non-competitive antagonism, Km (α 1/Potency):",
  ["Shows no change", "Increases", "Decreases", "Becomes infinite"], 0,
  "The Km row is 'No change' in the irreversible/non-competitive column; only Vmax falls. (Book p21)")
q(S2, 21, "Potency in reversible competitive antagonism:",
  ["Decreases", "Increases", "Is unchanged", "Becomes zero"], 0,
  "The final row of the table shows a downward arrow for potency in reversible competitive antagonism (Km ↑ so potency ↓). (Book p21)")
q(S2, 21, "Potency in competitive irreversible/non-competitive antagonism:",
  ["Shows no change", "Falls", "Rises", "Rises then falls"], 0,
  "The potency row reads 'No change' for the irreversible/non-competitive column. (Book p21)")
q(S2, 21, "Which single statement correctly contrasts the two antagonism columns?",
  ["Reversible competitive lowers potency; irreversible/non-competitive lowers efficacy",
   "Reversible competitive lowers efficacy; irreversible/non-competitive lowers potency",
   "Both lower efficacy only", "Both lower potency only"], 0,
  "Reading the whole table: reversible competitive antagonist → Km ↑, potency ↓, Vmax unchanged; irreversible/non-competitive → Vmax ↓ (efficacy ↓), Km and potency unchanged. (Book p21)")
q(S2, 21, "A competitive antagonist shifts the dose-response curve to the right. This means the agonist:",
  ["Needs a higher dose for the same effect", "Can never produce its maximal effect",
   "Becomes more potent", "Has increased efficacy"], 0,
  "A parallel rightward shift means lower potency (higher dose required) while the maximum (efficacy) is still achievable. (Book p21)")
q(S2, 21, "Which type of antagonism can be surmounted by increasing the agonist dose?",
  ["Competitive reversible", "Competitive irreversible", "Non-competitive",
   "Neither can be surmounted"], 0,
  "Only in the reversible competitive column does raising drug (A) restore the response; irreversible and non-competitive blockade stays. (Book p20-21)")

S3 = "Michaelis-Menten Note: Vmax and Km"
q(S3, 21, "The note relates the Michaelis-Menten equation to:",
  ["Vmax = maximum effect = efficacy", "Vmax = potency", "Km = efficacy",
   "Km = clearance"], 0,
  "The note reads 'Michaelis-Menten equation → Vmax α maximum effect → Efficacy'. (Book p21)")
q(S3, 21, "Vmax is defined as the:",
  ["Maximum velocity of reaction between enzyme and drug (substrate)",
   "Concentration of drug giving half of maximum velocity",
   "Dose of drug producing 50% mortality", "Rate of drug elimination"], 0,
  "The bullet defines Vmax as 'maximum velocity of reaction between enzyme & drug (substrate)'. (Book p21)")
q(S3, 21, "Km is defined as the:",
  ["Concentration of drug at which the speed of reaction is half of its Vmax",
   "Maximum velocity of the enzyme reaction",
   "Dose producing the maximum effect", "Concentration of antagonist needed to double the dose ratio"], 0,
  "The bullet defines Km as 'conc of drug at which speed of reaction (v) is half of its Vmax'. (Book p21)")
q(S3, 21, "In the table, Km is written as being proportional to:",
  ["1/Potency", "Efficacy", "Vmax", "Affinity constant"], 0,
  "The row label reads 'Km (α 1/Potency)', linking a higher Km to lower potency. (Book p21)")
q(S3, 21, "The relationship Vmax α maximum effect implies that Vmax reflects the drug's:",
  ["Efficacy", "Potency", "Bioavailability", "Half-life"], 0,
  "Since maximum effect is efficacy (from the earlier chapter), Vmax is used here as the efficacy marker. (Book p21)")
q(S3, 21, "If a drug's Km rises while Vmax stays the same, the drug's potency:",
  ["Falls", "Rises", "Is unchanged", "Becomes zero"], 0,
  "Km is inversely proportional to potency, so a rise in Km with unchanged Vmax means reduced potency - the signature of competitive antagonism in the table. (Book p21)")

S4 = "Receptors: Ligand Gated Ion Channel Receptors"
q(S4, 21, "Which receptors are described as the fastest acting receptors?",
  ["Ligand gated ion channel receptors", "G protein coupled receptors",
   "Nuclear receptors", "Enzymatic receptors"], 0,
  "The first point under LGIC receptors states 'Fastest acting receptors'. (Book p21)")
q(S4, 21, "The substrate for the GABA-A receptor in the table is:",
  ["Chloride ion channel", "Sodium channel", "Potassium channel", "Calcium channel"], 0,
  "The examples table lists GABA-A with substrate 'Chloride ion channel'. (Book p21)")
q(S4, 21, "Which of these are listed as glutamate receptor subtypes?",
  ["NMDA, AMPA and kainate", "M1, M2 and M3", "α1, α2 and β", "H1, H2 and H3"], 0,
  "Under the Glu receptor the table lists NMDA, AMPA and kainate. (Book p21)")
q(S4, 21, "Nicotinic receptor and 5-HT3 receptor, in the substrate column, are shown as:",
  ["Dash (-), i.e. no separate substrate named", "Chloride ion channel",
   "NMDA", "Guanylate cyclase"], 0,
  "For both 'Nicotinic receptor' and '5-HT3' the substrate column simply carries a dash. (Book p21)")
q(S4, 21, "GABA-B receptor is a:",
  ["GPCR receptor", "Ligand gated ion channel", "Nuclear receptor", "Tyrosine kinase receptor"], 0,
  "The note beside the table clarifies 'GABA-B : GPCR receptor', in contrast to the ionotropic GABA-A. (Book p21)")
q(S4, 21, "Which of the following is NOT a ligand gated ion channel receptor?",
  ["GABA-B", "GABA-A", "5-HT3", "Nicotinic receptor"], 0,
  "GABA-B is a GPCR; GABA-A, 5-HT3 and the nicotinic receptor are all ligand gated ion channels. (Book p21)")
q(S4, 21, "The fastest acting receptors are also, by structure, ion channels opened by:",
  ["Ligand binding", "Gene transcription", "Tyrosine phosphorylation", "cGMP production"], 0,
  "Being ligand gated, the channel opens directly on ligand binding - the reason they act fastest. (Book p21)")

S5 = "Nicotinic Receptor Structure"
q(S5, 21, "In the nicotinic receptor diagram, the ion that passes through the lumen is:",
  ["Na+", "Cl-", "Ca2+", "K+"], 0,
  "Both the resting and the open receptor are drawn with Na+ moving through the lumen of the channel. (Book p21)")
q(S5, 21, "Acetylcholine opens the nicotinic receptor channel by acting on the:",
  ["α subunit", "β subunit", "δ subunit", "ε subunit"], 0,
  "The diagram is labelled 'Ach on α subunit → opening', with ACh molecules bound at the α subunits. (Book p21)")
q(S5, 21, "The five subunits drawn in the nicotinic receptor are:",
  ["α, α, β, δ and ε", "α, β, γ and δ only", "α, α, β and γ", "β, β, δ and ε"], 0,
  "The labelled receptor ring in the figure carries α, α, β, δ and ε subunits around the central pore. (Book p21)")
q(S5, 21, "Stimulation of the nicotinic receptor on muscle produces:",
  ["Contraction", "Depolarisation only", "Relaxation", "Secretion"], 0,
  "The site note reads 'On muscle → Contraction'. (Book p21)")
q(S5, 21, "Stimulation of the nicotinic receptor on a ganglion produces:",
  ["Depolarisation", "Contraction", "Relaxation", "Hyperpolarisation"], 0,
  "The site note reads 'On ganglion → Depolarisation'. (Book p21)")
q(S5, 21, "Within a receptor, which subunit is marked most important?",
  ["α subunit", "β subunit", "δ subunit", "ε subunit"], 0,
  "The note at the foot of the figure states 'in a receptor, α subunit → most important'. (Book p21)")
q(S5, 21, "The direction of Na+ movement through the open nicotinic channel is:",
  ["Into the cell (inward)", "Out of the cell (outward)", "Bidirectionally equal",
   "Along the membrane surface"], 0,
  "Arrows show Na+ entering through the lumen on the extracellular side and continuing into the cell. (Book p21)")

S6 = "Enzymatic Receptor"
q(S6, 22, "In an enzymatic receptor, the ligand binds to the:",
  ["Enzymatic (intracellular) part of the receptor", "Nuclear DNA directly",
   "G-protein α subunit", "Chloride channel pore"], 0,
  "The diagram shows a ligand binding the receptor on the cell surface, whose intracellular domain is the 'enzymatic' part. (Book p22)")
q(S6, 22, "The classic example of an enzymatic receptor given in the page is:",
  ["Tyrosine kinase", "Guanylate cyclase only", "Janus kinase only", "Phospholipase C"], 0,
  "The flow reads 'Eg : Tyrosine Kinase → Phosphorylation → Tyrosine → Cell Proliferation'. (Book p22)")
q(S6, 22, "Tyrosine kinase receptor activation ultimately leads to:",
  ["Cell proliferation", "Vasodilation", "Vasoconstriction", "Glycogenolysis"], 0,
  "The end of the cascade in the page is 'Cell Proliferation'. (Book p22)")
q(S6, 22, "Which of the following is listed as a tyrosine kinase receptor?",
  ["EGFR", "Leptin receptor", "TGFR", "ANP receptor"], 0,
  "The tyrosine kinase receptor column gives EGFR, VEGF-R, Her-2/neu R and insulin/IGF R. (Book p22)")
q(S6, 22, "VEGF-R and Her-2/neu R belong to which receptor type?",
  ["Tyrosine kinase receptors", "JAK receptors", "STKR", "Guanylate cyclase receptors"], 0,
  "Both are listed in the tyrosine kinase receptor examples column. (Book p22)")
q(S6, 22, "Insulin/IGF receptor is an example of a:",
  ["Tyrosine kinase receptor", "JAK receptor", "Nuclear receptor", "Ion channel receptor"], 0,
  "Insulin/IGF R appears in the tyrosine kinase receptor list. (Book p22)")
q(S6, 22, "Leptin (cytokine), prolactin and growth hormone act through:",
  ["Janus kinase (JAK) receptors", "Tyrosine kinase receptors", "STKR", "Guanylate cyclase receptors"], 0,
  "The JAK receptor column lists leptin (cytokine), prolactin and growth hormone. (Book p22)")
q(S6, 22, "TGFR is an example of:",
  ["STKR (serine-threonine kinase receptor)", "Tyrosine kinase receptor", "JAK receptor",
   "Guanylate cyclase receptor"], 0,
  "The STKR column contains TGFR. (Book p22)")
q(S6, 22, "ANP and BNP act on which receptor?",
  ["Guanylate cyclase receptor", "Tyrosine kinase receptor", "JAK receptor", "STKR"], 0,
  "The last column, 'Guanylate cyclase receptor', lists ANP and BNP. (Book p22)")
q(S6, 22, "Activation of the guanylate cyclase receptor by ANP/BNP causes:",
  ["↑ cGMP → vasodilation", "↓ cGMP → vasoconstriction", "↑ cAMP → bronchodilation",
   "↑ IP3 → smooth muscle contraction"], 0,
  "The cell in the table reads 'ANP, BNP → ↑ cGMP → vasodilation'. (Book p22)")
q(S6, 22, "Which second messenger is increased by the guanylate cyclase receptor?",
  ["cGMP", "cAMP", "IP3", "DAG"], 0,
  "Guanylate cyclase generates cGMP, which the page links to vasodilation. (Book p22)")

S7 = "Nuclear Receptor (NRT)"
q(S7, 22, "Which receptors are described as the slowest acting receptors?",
  ["Nuclear receptors", "Ligand gated ion channels", "GPCRs", "Enzymatic receptors"], 0,
  "The nuclear receptor (NRT) heading carries the note 'Slowest acting receptors'. (Book p22)")
q(S7, 22, "Nuclear receptors are so called because they act:",
  ["On gene transcription in the nucleus", "On ion channels in the membrane",
   "On G proteins in the cytoplasm", "On enzymes in the cytosol only"], 0,
  "Being the slowest acting, their site of action is the nucleus where they alter gene transcription. (Book p22)")
q(S7, 22, "Which receptors are listed under the 'Nucleus' site column?",
  ["Estrogen, progesterone, vitamin A, T3/T4 and PPAR", "Androgen, mineralocorticoid, glucocorticoid and vitamin D",
   "EGFR, VEGF-R and Her-2/neu", "M2, α2, H3 and 5HT1"], 0,
  "The nuclear-site column lists estrogen receptor, progesterone receptor, vitamin A receptor, T3/T4 receptor and PPAR (α, δ, γ). (Book p22)")
q(S7, 22, "PPAR receptors are listed in the page as PPAR:",
  ["α, δ and γ", "α, β and γ only", "1, 2 and 3", "A and B"], 0,
  "The nuclear-site column writes 'PPAR (α, δ, γ)'. (Book p22)")
q(S7, 22, "Which receptors sit in the cytoplasm and translocate to the nucleus upon binding ligand?",
  ["Androgen, mineralocorticoid, glucocorticoid and vitamin D receptors",
   "Estrogen, progesterone and vitamin A receptors", "T3/T4 and PPAR receptors",
   "GABA-A and nicotinic receptors"], 0,
  "The third column is headed 'Cytoplasm (Translocation to nucleus upon binding to ligand)' and lists androgen, mineralocorticoid, glucocorticoid and vitamin D receptors. (Book p22)")
q(S7, 22, "The glucocorticoid receptor in this scheme is located in the:",
  ["Cytoplasm", "Nucleus", "Cell membrane", "Mitochondria"], 0,
  "Glucocorticoid receptors are grouped in the cytoplasm column, moving to the nucleus after ligand binding. (Book p22)")
q(S7, 22, "Vitamin D receptor belongs to which location group?",
  ["Cytoplasm (translocates to nucleus)", "Nucleus only", "Cell membrane", "Endoplasmic reticulum"], 0,
  "Vitamin D receptor appears in the cytoplasm/translocation column of the NRT table. (Book p22)")
q(S7, 22, "Which of the following pairs is correctly matched?",
  ["Vitamin A receptor - nucleus; vitamin D receptor - cytoplasm",
   "Vitamin A receptor - cytoplasm; vitamin D receptor - nucleus",
   "Both are nuclear only", "Both are cytoplasmic only"], 0,
  "The table puts the vitamin A receptor in the nucleus column and the vitamin D receptor in the cytoplasm (translocation) column. (Book p22)")
q(S7, 22, "Which statement best explains why nuclear receptor effects are slow?",
  ["They require gene transcription and protein synthesis", "They open ion channels slowly",
   "They need GTP hydrolysis", "They act through second messengers only"], 0,
  "Acting on the nucleus and altering transcription, nuclear receptors take the longest to produce their effects. (Book p22)")

S8 = "G Protein Coupled Receptor (GPCR)"
q(S8, 22, "Which receptor family is described as the most common target for drugs?",
  ["G protein coupled receptors", "Nuclear receptors", "Ligand gated ion channels",
   "Tyrosine kinase receptors"], 0,
  "Right under the GPCR heading the page notes 'most common target for drugs'. (Book p22)")
q(S8, 22, "GPCRs are alternately named:",
  ["Serpentine / 7 transmembrane / heptahelical receptor",
   "3 transmembrane / coiled receptor", "Single transmembrane kinase receptor",
   "Pentameric ion channel"], 0,
  "The page gives three synonyms: Serpentine receptor, 7 transmembrane receptor and heptahelical receptor. (Book p22)")
q(S8, 22, "The GPCR consists of how many transmembrane helices?",
  ["Seven", "Three", "Five", "Twelve"], 0,
  "Being a heptahelical/7 transmembrane receptor, the drawing shows seven membrane-spanning segments. (Book p22)")
q(S8, 22, "In the GPCR, which subunit is described as most important?",
  ["α subunit", "β subunit", "γ subunit", "δ subunit"], 0,
  "The page states 'α subunit : most important' beside the GPCR diagram. (Book p22)")
q(S8, 22, "Which subunit of the G protein possesses intrinsic GTPase activity?",
  ["α subunit", "β subunit", "γ subunit", "All three equally"], 0,
  "The label at the bottom of the GPCR figure reads 'Intrinsic GTPase activity of (α)'. (Book p22)")
q(S8, 22, "Activation of the G protein involves exchange of:",
  ["GDP for GTP on the α subunit", "GTP for GDP on the α subunit",
   "ATP for ADP on the β subunit", "cAMP for cGMP"], 0,
  "The figure shows the inactive state with GDP and, on activation, GTP bound to the α subunit. (Book p22)")
q(S8, 22, "Termination of the G protein signal occurs by:",
  ["Hydrolysis of GTP by the intrinsic GTPase of α",
   "Dephosphorylation of the receptor by a kinase", "Reuptake into the nucleus",
   "Degradation of cAMP by adenylate cyclase"], 0,
  "The curved arrow labelled 'Intrinsic GTPase activity of (α)' shows GTP hydrolysis turning the G protein off. (Book p22)")
q(S8, 22, "GPCRs are classified based on:",
  ["Their α subunits (subtypes)", "The number of transmembrane domains",
   "The type of ion conducted", "The nuclear site of action"], 0,
  "The note states 'GPCRs are classified based on subtypes' and the accompanying table maps α subtypes to GPCR types. (Book p22)")
q(S8, 22, "The α subtype 's' corresponds to which GPCR type?",
  ["Gs", "Gq", "Gi", "G12/13"], 0,
  "The table pairs the α subtypes column (s, q, i) with GPCR types Gs, Gq and Gi respectively. (Book p22)")
q(S8, 22, "The α subtype 'q' corresponds to which GPCR type?",
  ["Gq", "Gs", "Gi", "Go"], 0,
  "The α subtype table maps q → Gq. (Book p22)")
q(S8, 22, "The α subtype 'i' corresponds to which GPCR type?",
  ["Gi", "Gs", "Gq", "G12/13"], 0,
  "The α subtype table maps i → Gi. (Book p22)")

S9 = "Gs Subtype"
q(S9, 23, "Stimulation of Gs leads to activation of:",
  ["Adenylate cyclase", "Phospholipase C", "Rho-kinase", "Guanylate cyclase"], 0,
  "The Gs cascade runs Gs → αs-GTP → (+) Adenylate cyclase. (Book p23)")
q(S9, 23, "In the Gs pathway, the immediate effect of adenylate cyclase is:",
  ["↑ Cyclic AMP", "↓ Cyclic AMP", "↑ IP3", "↓ Ca2+"], 0,
  "The next step of the cascade is written as '↑ Cyclic AMP'. (Book p23)")
q(S9, 23, "Cyclic AMP produced by the Gs pathway is metabolised by:",
  ["Phosphodiesterase", "Adenylate cyclase", "Phospholipase C", "Protein kinase A"], 0,
  "An arrow from 'Cyclic AMP' is labelled 'metabolised by' pointing to phosphodiesterase. (Book p23)")
q(S9, 23, "In cardiac and skeletal muscle, the cAMP rise causes:",
  ["Contraction due to calcium channel phosphorylation",
   "Relaxation due to myosin light chain kinase activation", "Vasodilation only",
   "Glycogen synthesis only"], 0,
  "The bracket from cardiac and skeletal muscle into cAMP reads 'Contraction (d/t calcium channel phosphorylation)'. (Book p23)")
q(S9, 23, "In smooth muscle, the effect of the Gs-cAMP pathway is:",
  ["Relaxation", "Contraction", "No effect", "Spasm"], 0,
  "Smooth muscle is labelled 'Relaxation (d/t myosin light chain phosphorylase activation and myosin light chain kinase inhibition)'. (Book p23)")
q(S9, 23, "The smooth muscle relaxation produced by cAMP is attributed to:",
  ["Myosin light chain phosphorylase activation and myosin light chain kinase inhibition",
   "Calcium channel phosphorylation", "Rho-kinase activation",
   "Phospholipase C activation"], 0,
  "The page gives exactly this mechanism - MLC phosphorylase activation plus MLC kinase inhibition. (Book p23)")
q(S9, 23, "Which of these are effects of Gs-mediated smooth muscle relaxation listed on the page?",
  ["Bronchodilation, vasodilation and uterine relaxing",
   "Bronchoconstriction and vasoconstriction", "Trabecular meshwork contraction",
   "Increased heart rate and tremors"], 0,
  "The bullet list under smooth muscle reads bronchodilation, vasodilation and uterine relaxing. (Book p23)")
q(S9, 23, "Ritodrine is described as a:",
  ["Tocolytic used in labor", "Drug used in CHF", "Bronchodilator used in asthma",
   "Phosphodiesterase inhibitor"], 0,
  "The pill icon for ritodrine is labelled 'Tocolytic used in labor'. (Book p23)")
q(S9, 23, "Ritodrine produces its tocolytic effect by acting through:",
  ["Gs (β receptors) on uterine smooth muscle", "Gi receptors in the heart",
   "Gq receptors on the uterus", "Phosphodiesterase 3 inhibition"], 0,
  "Ritodrine is shown on the Gs cascade, whose uterine effect is 'uterine relaxing'. (Book p23)")
q(S9, 23, "Dobutamine is used in:",
  ["CHF", "Asthma", "Labor tocolysis", "Open-angle glaucoma"], 0,
  "The label beside dobutamine reads 'used in CHF'. (Book p23)")
q(S9, 23, "Salbutamol is used in asthma and is shown on the:",
  ["Gs cascade (β2 → cAMP)", "Gq cascade", "Gi cascade", "G12/13 cascade"], 0,
  "Salbutamol appears among the drugs of the Gs subtype, producing bronchodilation through cAMP. (Book p23)")
q(S9, 23, "The side effects of salbutamol noted on the page are:",
  ["Palpitations and tremors", "Bradycardia and sedation", "Hypotension and diarrhoea",
   "Hyperkalaemia and rash"], 0,
  "Under salbutamol the page writes 'S/E : Palpitations & tremors'. (Book p23)")
q(S9, 23, "Theophylline is used in asthma and acts by inhibiting:",
  ["Phosphodiesterase", "Adenylate cyclase", "Phospholipase C", "Rho-kinase"], 0,
  "Theophylline is shown with a block (✳) on phosphodiesterase, i.e. PDE inhibition. (Book p23)")
q(S9, 23, "Theophylline is indicated in asthma when:",
  ["β-blockers have been used previously", "β2 agonists have failed only",
   "The patient has COPD", "The patient is in labor"], 0,
  "The bracket after theophylline reads '(if β-blocker are used previously)'. (Book p23)")
q(S9, 23, "Milrinone is used in:",
  ["Acute CHF (if β-blockers were used previously)", "Chronic stable angina",
   "Asthma in children", "Graft versus host disease"], 0,
  "The milrinone pill is labelled 'Acute CHF (if β-blocker are used previously)'. (Book p23)")
q(S9, 23, "Milrinone acts by inhibiting:",
  ["Phosphodiesterase 3", "Phosphodiesterase 3 and 4", "Adenylate cyclase", "Phospholipase A2"], 0,
  "The block for milrinone sits on the 'Phosphodiesterase 3 → in Heart' line, whereas theophylline blocks PDE 3, 4. (Book p23)")
q(S9, 23, "Phosphodiesterase 3 and 4 are located in the ____, while phosphodiesterase 3 is located in the ____:",
  ["Bronchi; heart", "Heart; bronchi", "Liver; kidney", "Brain; lung"], 0,
  "The page links 'Phosphodiesterase 3, 4 → in Bronchi' and 'Phosphodiesterase 3 → in Heart'. (Book p23)")
q(S9, 23, "Which drug is paired with the correct phosphodiesterase?",
  ["Theophylline - PDE 3, 4 in bronchi", "Milrinone - PDE 3, 4 in bronchi",
   "Theophylline - PDE 3 in heart only", "Milrinone - PDE 4 in heart"], 0,
  "Theophylline blocks PDE 3, 4 (bronchi) and milrinone blocks PDE 3 (heart). (Book p23)")
q(S9, 23, "The receptor subtypes feeding into Gs in the diagram are:",
  ["β1 and β2", "α1, M1 and M2", "M2, α2, H3 and 5HT1", "G12/13 only"], 0,
  "The small circles feeding the Gs cascade are labelled β1 and β2. (Book p23)")
q(S9, 23, "Both theophylline and milrinone are used when β-blockers have been given previously because they:",
  ["Act distal to the β receptor by raising cAMP", "Stimulate β receptors directly",
   "Block β receptors themselves", "Increase β receptor number"], 0,
  "By inhibiting phosphodiesterase they raise cAMP downstream of the blocked β receptor, which is why the page specifies this setting. (Book p23)")

S10 = "Gq Subtype"
q(S10, 23, "Stimulation of Gq activates:",
  ["Phospholipase C", "Adenylate cyclase", "Rho-kinase", "Phosphodiesterase"], 0,
  "The Gq cascade reads Gq → αq-GTP → (+) Phospholipase C. (Book p23)")
q(S10, 23, "Activation of phospholipase C raises:",
  ["PIP2 breakdown products (IP3 and DAG)", "Cyclic AMP", "Cyclic GMP", "Intracellular K+"], 0,
  "An up arrow leads from phospholipase C to PIP2, which then splits into IP3 and DAG. (Book p23)")
q(S10, 23, "IP3 is described in the page as a:",
  ["Secondary messenger", "Primary messenger", "Hormone", "Enzyme"], 0,
  "The label beside IP3 reads 'IP3 (Secondary messenger)'. (Book p23)")
q(S10, 23, "IP3 acts by binding to a receptor on the:",
  ["Sarcoplasmic reticulum", "Cell membrane", "Nucleus", "Mitochondria"], 0,
  "The cascade notes 'binds to receptor on sarcoplasmic reticulum' after IP3. (Book p23)")
q(S10, 23, "The consequence of IP3 action is:",
  ["↑ Ca2+ and smooth muscle constriction", "↓ Ca2+ and smooth muscle relaxation",
   "↑ cAMP and bronchodilation", "↑ cGMP and vasodilation"], 0,
  "The cascade ends '→ ↑ Ca2+ → Smooth muscle constriction'. (Book p23)")
q(S10, 23, "Besides IP3, the other product of PIP2 splitting is:",
  ["DAG", "cAMP", "cGMP", "GTP"], 0,
  "The PIP2 branch is shown dividing into IP3 and DAG. (Book p23)")
q(S10, 23, "Which receptors are listed as examples of Gq receptors?",
  ["Oxytocin R, angiotensin R and vasopressin 1 R", "β1, β2 and β3 receptors",
   "M2, α2, H3 and 5HT1 receptors", "EGFR and VEGF-R"], 0,
  "The list reads oxytocin R, angiotensin R and vasopressin 1 R. (Book p23)")
q(S10, 23, "Which Gq subtype receptors feed into the Gq cascade in the diagram?",
  ["α1, M1 and M2", "β1 and β2", "M2, α2, H3 and 5HT1", "Only α1"], 0,
  "The circles feeding Gq are labelled α1, M1 and M2. (Book p23)")
q(S10, 23, "Note on the Gq page: phospholipase A2 is responsible for:",
  ["Synthesis of prostaglandins", "Formation of IP3", "Hydrolysis of cAMP",
   "Opening of K+ channels"], 0,
  "The closing note states 'Phospholipase A2 synthesis of prostaglandins'. (Book p23)")
q(S10, 23, "Angiotensin receptor signalling through Gq would be expected to cause:",
  ["Smooth muscle constriction via IP3 and Ca2+", "Smooth muscle relaxation via cAMP",
   "Reduced heart rate via K+ channel opening", "Increased cGMP"], 0,
  "As a Gq receptor, angiotensin R works through phospholipase C, IP3 and a rise in Ca2+, giving constriction. (Book p23)")
q(S10, 23, "Vasopressin 1 receptor-mediated vasoconstriction is an example of:",
  ["Gq signalling", "Gs signalling", "Gi signalling", "G12/13 signalling"], 0,
  "Vasopressin 1 R is listed among the Gq receptor examples. (Book p23)")

S11 = "Gi Subtype"
q(S11, 24, "Gi is described as present in the:",
  ["Heart (↓ HR)", "Bronchi (bronchodilation)", "Uterus (relaxation)",
   "Trabecular meshwork (contraction)"], 0,
  "The Gi heading notes 'Present in the heart (↓ HR)'. (Book p24)")
q(S11, 24, "Which receptors are shown feeding into the Gi/Go pathway?",
  ["M2, α2, H3 and 5HT1", "α1, M1 and M2", "β1 and β2", "H1 and H2"], 0,
  "The four circles above Gi are labelled M2, α2, H3 and 5HT1. (Book p24)")
q(S11, 24, "The note states that M2, α2, H3 and 5HT1 receptors are:",
  ["Autoreceptors", "Heteroreceptors only", "Ion channels", "Nuclear receptors"], 0,
  "The note reads 'M2, α2, H3, 5HT1 receptors are autoreceptors'. (Book p24)")
q(S11, 24, "In the Gi pathway, αi-GTP causes:",
  ["↓ cyclic AMP", "↑ cyclic AMP", "↓ Ca2+", "↑ IP3"], 0,
  "The left branch runs αi-GTP → ↓ cyclic AMP → opens K+ channel. (Book p24)")
q(S11, 24, "In the Go branch of the same figure, β,γ subunits cause:",
  ["↓ Ca2+", "↓ cyclic AMP", "↑ IP3", "↑ cGMP"], 0,
  "The right branch runs β, γ → ↓ Ca2+ → opens K+ channel. (Book p24)")
q(S11, 24, "Both branches of the Gi/Go pathway finally:",
  ["Open K+ channels, causing relaxation", "Close K+ channels, causing contraction",
   "Open Ca2+ channels, causing contraction", "Inhibit adenylate cyclase only"], 0,
  "The two limbs converge on 'Opens K+ channel' and then 'Relaxation'. (Book p24)")
q(S11, 24, "The net effect of the Gi/Go pathway in the heart is:",
  ["Relaxation with decreased heart rate", "Contraction with increased heart rate",
   "No change in rate", "Increased contractility"], 0,
  "The Gi page states it is present in the heart with ↓ HR, converging on relaxation. (Book p24)")
q(S11, 24, "Stimulation of M2 receptors in the heart would:",
  ["Reduce cyclic AMP and open K+ channels", "Increase cyclic AMP and open Ca2+ channels",
   "Increase IP3 and intracellular Ca2+", "Activate Rho-kinase"], 0,
  "M2 feeds the Gi pathway, lowering cAMP and opening K+ channels to relax and slow the heart. (Book p24)")

S12 = "G12/13 Subtype"
q(S12, 24, "G12/13 signalling proceeds through:",
  ["Rho-GTP → (+) Rho-kinase", "αs-GTP → adenylate cyclase", "αq-GTP → phospholipase C",
   "αi-GTP → ↓ cAMP"], 0,
  "The cascade is written G12/13 → Rho-GTP → (+) Rho-kinase. (Book p24)")
q(S12, 24, "Activation of Rho-kinase produces:",
  ["Smooth muscle contraction, vasoconstriction and trabecular meshwork contraction",
   "Smooth muscle relaxation and vasodilation", "Bronchodilation and uterine relaxation",
   "Increased cGMP"], 0,
  "The three bullets under Rho-kinase read smooth muscle contraction, vasoconstriction and trabecular meshwork contraction. (Book p24)")
q(S12, 24, "Belumosudil is described as a new drug used in:",
  ["Graft versus host disease", "Acute CHF", "Open-angle glaucoma", "Angina"], 0,
  "The label beside belumosudil reads 'New drug used in Graft vs host disease'. (Book p24)")
q(S12, 24, "RHO kinase is noted to be involved in:",
  ["Leukocytosis", "Bronchoconstriction", "Platelet aggregation", "Bradycardia"], 0,
  "The bullet under belumosudil states 'RHO kinase involved in leukocytosis'. (Book p24)")
q(S12, 24, "Fasudil is used for:",
  ["Vasodilation in angina", "Tocolysis in labor", "Open-angle glaucoma",
   "Graft versus host disease"], 0,
  "The fasudil label reads 'vasodilation in Angina'. (Book p24)")
q(S12, 24, "Netarsudil increases:",
  ["Trabecular outflow", "Aqueous humour production", "Heart rate", "Uterine tone"], 0,
  "The netarsudil label reads '↑ Trabecular outflow'. (Book p24)")
q(S12, 24, "Netarsudil is used in:",
  ["Open-angle glaucoma", "Angle-closure glaucoma", "Asthma", "Angina"], 0,
  "The bullet under netarsudil states 'used in open-angle glaucoma'. (Book p24)")
q(S12, 24, "All three drugs listed - belumosudil, fasudil and netarsudil - act by inhibiting:",
  ["Rho-kinase", "Phosphodiesterase 3", "Adenylate cyclase", "Phospholipase C"], 0,
  "All three pill icons point to the Rho-kinase step with the (-) inhibition mark in the G12/13 cascade. (Book p24)")
q(S12, 24, "Which G protein pathway explains netarsudil's effect on the trabecular meshwork?",
  ["G12/13 - Rho-kinase", "Gs - cAMP", "Gq - IP3", "Gi - K+ channel"], 0,
  "Trabecular meshwork contraction is a Rho-kinase (G12/13) effect, so its inhibition by netarsudil increases trabecular outflow. (Book p24)")
q(S12, 24, "In the G12/13 cascade, the drug acts on Rho-kinase with which symbol?",
  ["(-), i.e. inhibition", "(+), i.e. activation", "No symbol", "A question mark"], 0,
  "A (-) mark is drawn where belumosudil, fasudil and netarsudil meet the Rho-kinase step, denoting inhibition. (Book p24)")

# ------------------------------------------------------------------ units
UNITS = [
 (S1, 1, "Types of Antagonism", [1,17],
  "Antagonism is classified by mechanism, not by receptor: physical antagonism binds the substance (charcoal adsorbs alcohol from the intestine), chemical antagonism binds and neutralises it (heparin, an acid/-ve, is neutralised by protamine sulphate, a base/+ve; iron is chelated by dexrazoxane or deferiprone), and physiological antagonism uses opposite receptors - histamine via H1 constricts bronchi while adrenaline/salbutamol via β2 dilate them. Salbutamol is the best bronchodilator in asthma, but in COPD ipratropium or tiotropium is preferred instead because of cholinergic effects."),
 (S2, 2, "Competitive Reversible vs Irreversible and Non-competitive Antagonism", [18,37],
  "The table follows drug (A) through three rows: its normal effect, the addition of antagonist (B), and the effect of raising (A). In competitive reversible antagonism (A) and (B) compete for the same (enzymatic) site, so raising (A) restores the effect, Km rises, potency falls and Vmax/efficacy is unchanged. In competitive irreversible and non-competitive antagonism (B) occupies the allosteric part, raising (A) gives 'no reversal of antagonism', Vmax falls while Km and potency show no change."),
 (S3, 3, "Michaelis-Menten Note: Vmax and Km", [38,43],
  "The Michaelis-Menten equation is used to read the same table numerically: Vmax is the maximum velocity of the reaction between enzyme and drug (substrate) and stands for maximum effect, i.e. efficacy; Km is the concentration of drug at which the reaction velocity is half of Vmax and is proportional to 1/potency. So a competitive antagonist raises Km (potency falls) with Vmax untouched, while a non-competitive antagonist lowers Vmax with Km unchanged."),
 (S4, 4, "Receptors: Ligand Gated Ion Channel Receptors", [44,50],
  "Receptors begin with the fastest acting type, the ligand gated ion channel receptors (LGICR). Their examples are tabulated by substrate: GABA-A conducts chloride, glutamate has the NMDA, AMPA and kainate subtypes, while the nicotinic receptor and 5-HT3 are listed with a dash. The note to remember is that GABA-B is a GPCR, not an ion channel."),
 (S5, 5, "Nicotinic Receptor Structure", [51,57],
  "The nicotinic receptor is a pentamer of α, α, β, δ and ε subunits surrounding a lumen through which Na+ enters. Acetylcholine acts on the α subunit to open the channel, which is why the α subunit is marked most important in a receptor. Functionally, the same receptor gives contraction on muscle and depolarisation on a ganglion."),
 (S6, 6, "Enzymatic Receptor", [58,68],
  "An enzymatic receptor carries an intracellular enzymatic domain; the ligand binds the receptor and the enzyme acts, the classic example being tyrosine kinase, where phosphorylation of tyrosine leads to cell proliferation. The four tabulated types are tyrosine kinase receptors (EGFR, VEGF-R, Her-2/neu R, insulin/IGF R), Janus kinase receptors (leptin/cytokine, prolactin, growth hormone), STKR (TGFR) and the guanylate cyclase receptor (ANP, BNP → ↑ cGMP → vasodilation)."),
 (S7, 7, "Nuclear Receptor (NRT)", [69,77],
  "Nuclear receptors are the slowest acting receptors because they work on gene transcription. Some already sit in the nucleus - estrogen, progesterone, vitamin A, T3/T4 and PPAR (α, δ, γ) receptors - while others (androgen, mineralocorticoid, glucocorticoid and vitamin D receptors) wait in the cytoplasm and translocate to the nucleus only upon ligand binding."),
 (S8, 8, "G Protein Coupled Receptor (GPCR)", [78,88],
  "GPCRs - also called serpentine, 7 transmembrane or heptahelical receptors - are the most common target for drugs. The α subunit is the most important and carries intrinsic GTPase activity; activation exchanges GDP for GTP and hydrolysis of GTP switches the signal off. GPCRs are classified by their α subtypes: s → Gs, q → Gq and i → Gi."),
 (S9, 9, "Gs Subtype", [89,108],
  "Gs signals through αs-GTP to activate adenylate cyclase, raising cyclic AMP, which phosphodiesterase then metabolises. In cardiac and skeletal muscle cAMP causes contraction through calcium channel phosphorylation, while in smooth muscle it causes relaxation (myosin light chain phosphorylase activation and myosin light chain kinase inhibition) giving bronchodilation, vasodilation and uterine relaxation - the basis for ritodrine in labor, dobutamine in CHF and salbutamol in asthma (palpitations and tremors). Theophylline blocks phosphodiesterase 3, 4 in bronchi and milrinone blocks phosphodiesterase 3 in the heart, both used when β-blockers have already been given."),
 (S10, 10, "Gq Subtype", [109,119],
  "Gq works through αq-GTP to activate phospholipase C, which raises PIP2 and splits it into IP3 (a secondary messenger) and DAG. IP3 binds a receptor on the sarcoplasmic reticulum, releasing Ca2+ and causing smooth muscle constriction - the pathway behind oxytocin, angiotensin and vasopressin 1 receptor effects, with α1, M1 and M2 as the feeding receptors. A separate note records that phospholipase A2 is responsible for the synthesis of prostaglandins."),
 (S11, 11, "Gi Subtype", [120,127],
  "Gi is present in the heart, where it lowers heart rate. Its receptors - M2, α2, H3 and 5HT1 - are autoreceptors. The αi-GTP limb lowers cyclic AMP while the Go limb (β, γ) lowers Ca2+; both converge on opening K+ channels and so produce relaxation."),
 (S12, 12, "G12/13 Subtype", [128,137],
  "G12/13 signals through Rho-GTP, which activates Rho-kinase and produces smooth muscle contraction, vasoconstriction and trabecular meshwork contraction. Three Rho-kinase inhibitors are shown: belumosudil, a new drug for graft versus host disease (RHO kinase is involved in leukocytosis), fasudil for vasodilation in angina, and netarsudil, which increases trabecular outflow and is used in open-angle glaucoma."),
]

byid = {}
for i, (sec, page, text, opts, ans, exp) in enumerate(Q, 1):
    byid[i] = {"id": f"PHARM-C8-{i:03d}", "sec": sec, "page": page, "q": text,
               "opts": opts, "ans": ans, "exp": exp}

# assign sec for questions pulled into a unit from a different section name
for u in UNITS:
    sec, n, title, (a, b), guide = u
    for i in range(a, b + 1):
        byid[i]["sec"] = title

questions = [byid[i] for i in sorted(byid)]
units = []
for sec, n, title, (a, b), guide in UNITS:
    units.append({"id": f"PHARM-U8-{n}", "ch": 8, "n": n, "title": title,
                  "sec": f"{title} · p{byid[a]['page']}",
                  "qs": [f"PHARM-C8-{i:03d}" for i in range(a, b + 1)],
                  "guide": guide})

out = {"questions": questions, "units": units}
json.dump(out, open("data/ch08.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("questions:", len(questions), "units:", len(units))
for u in units:
    print(" ", u["id"], u["title"], "->", len(u["qs"]), "qs  |", u["sec"])
