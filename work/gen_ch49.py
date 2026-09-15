# -*- coding: utf-8 -*-
import json
CH = 49
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

unit("Amoebiasis", "Amoebiasis is split into intestinal and extra-intestinal (hepatic) disease. Asymptomatic intestinal carriers get luminal amoebicidal drugs that act within the lumen - diloxanide furoate, iodoquinol and paromomycin (DOC) - with the aim of radical cure. Symptomatic disease uses nitazoxanide, emetine and metronidazole (DOC), while hepatic amoebiasis can additionally be treated with chloroquine, which is only used for hepatic disease.")
q(199, "Asymptomatic intestinal amoebiasis is treated with:", ["Luminal amoebicidal drugs (act within lumen)", "Only metronidazole", "Chloroquine", "Emetine"], "The intestinal-asymptomatic branch: drugs luminal amoebicidal drugs (act within lumen).")
q(199, "Which is NOT listed as a luminal amoebicidal drug?", ["Metronidazole", "Diloxanide furoate", "Iodoquinol", "Paromomycin"], "The luminal list: diloxanide furoate, iodoquinol, paromomycin.")
q(199, "The DOC among luminal amoebicidal drugs is:", ["Paromomycin", "Diloxanide furoate", "Iodoquinol", "Emetine"], "The list marks paromomycin (DOC).")
q(199, "The aim of treating asymptomatic luminal amoebiasis is:", ["Radical cure", "Symptom relief only", "Suppression of cysts for life", "Prevention of hepatic spread only"], "Below the luminal drugs: aim - radical cure.")
q(199, "Drugs listed for symptomatic intestinal amoebiasis include:", ["Nitazoxanide, emetine, metronidazole (DOC)", "Diloxanide furoate, iodoquinol, paromomycin", "Chloroquine only", "Sodium stibogluconate"], "The symptomatic branch lists nitazoxanide, emetine, metronidazole (DOC).")
q(199, "Chloroquine in amoebiasis is used only for:", ["Hepatic (extra-intestinal) amoebiasis", "Luminal intestinal amoebiasis", "Asymptomatic cyst passers", "Amoebic colitis"], "The extra-intestinal branch: chloroquine (only for hepatic).")

unit("Nitroimidazoles", "The nitroimidazoles are tinidazole (DOC in western countries), satranidazole, secnidazole, benznidazole and metronidazole (DOC in India). They act by free radical production; the treatment of cure for amoebiasis is metronidazole followed by paromomycin. Side effects are a disulfiram-like reaction (contraindicated with alcohol) and red-brown urine. Uses of metronidazole (DOC): giardiasis, amoebiasis, infra-diaphragmatic anaerobes, tetanus, trichomoniasis and bacterial vaginosis. Cefazolin plus metronidazole is surgical prophylaxis for infra-diaphragmatic surgery, and bacterial vaginosis shows clue cells in foul-smelling dirty white discharge.")
q(199, "The nitroimidazole that is DOC in India is:", ["Metronidazole", "Tinidazole", "Secnidazole", "Satranidazole"], "The drug list marks metronidazole (DOC in India).")
q(199, "Tinidazole is DOC in:", ["Western countries", "India", "North-eastern states only", "Africa"], "The list marks tinidazole (DOC in western countries).")
q(199, "Which drug listed under nitroimidazoles is used in American trypanosomiasis?", ["Benznidazole", "Secnidazole", "Metronidazole", "Tinidazole"], "Benznidazole appears in the nitroimidazole list; it is the Chagas DOC on p200.")
q(199, "The MOA of nitroimidazoles is:", ["Free radical production", "Blocking microtubules", "Inhibiting PFOR enzyme", "Inhibiting DNA gyrase"], "The MOA line: free radical production.")
q(199, "TOC for amoebiasis is:", ["Metronidazole followed by paromomycin", "Paromomycin followed by metronidazole", "Metronidazole followed by chloroquine", "Tinidazole followed by emetine"], "The line: TOC for amoebiasis - metronidazole f/b paromomycin.")
q(199, "A nitroimidazole side effect requiring alcohol abstinence is:", ["Disulfiram-like reaction", "Green urine", "Bull's eye retinopathy", "Hemolysis"], "The side-effect line: disulfiram-like reaction (C/I with alcohol).")
q(199, "The urine color change with nitroimidazoles is:", ["Red-brown urine", "Green urine", "Orange-red urine", "Black urine"], "The second side effect: red-brown urine.")
q(199, "Metronidazole covers anaerobes located:", ["Infra-diaphragmatic", "Supra-diaphragmatic", "Only intra-abdominal", "Only pelvic"], "The uses list: anaerobes (infra diaphragmatic).")
q(199, "Metronidazole is the DOC in all EXCEPT:", ["Amoebic liver abscess", "Trichomoniasis", "Bacterial vaginosis", "Ascariasis"], "Uses listed: giardiasis, amoebiasis, anaerobes, tetanus, trichomoniasis, bacterial vaginosis.")
q(199, "The surgical prophylaxis combination for infra-diaphragmatic surgery is:", ["Cefazolin + metronidazole", "Ceftriaxone + metronidazole", "Ampicillin + gentamicin", "Clindamycin + gentamicin"], "The note: cefazolin + metronidazole - surgical prophylaxis (infra diaphragm).")
q(199, "Bacterial vaginosis shows:", ["Clue cells in foul-smelling, dirty white discharge", "Strawberry cervix", "Bull's eye rash", "Green urine"], "The note: bacterial vaginosis - clue cells in foul-smelling, dirty white discharge.")

unit("Nitazoxanide", "Nitazoxanide has a four-way spectrum: anti-protozoal, anti-helminthic, anti-bacterial and anti-viral. Its side effect is green urine, it is the DOC in resistant giardiasis, and it has an off-label use in H. pylori infection because of macrolide resistance. In cryptosporidiasis nitazoxanide is the DOC; the drug was sourced from niclosamide (an anti-helminthic), and its MOA is inhibition of the PFOR enzyme, blocking electron transport.")
q(200, "The spectrum of nitazoxanide includes all EXCEPT:", ["Anti-fungal", "Anti-protozoal", "Anti-helminthic", "Anti-viral"], "The spectrum bracket: anti-protozoal, anti-helminthic, anti-bacterial, anti-viral.")
q(200, "The side effect of nitazoxanide is:", ["Green urine", "Red-brown urine", "Red-orange urine", "Blue urine"], "The line: side effect green urine.")
q(200, "The DOC in resistant giardiasis is:", ["Nitazoxanide", "Metronidazole", "Tinidazole", "Paromomycin"], "Other uses: DOC in resistant giardiasis.")
q(200, "The off-label use of nitazoxanide is:", ["H. pylori infection (D/t resistance to macrolides)", "Amoebic hepatitis", "Malaria prophylaxis", "Chagas disease"], "The note: off label use H. pylori infection (D/t resistance to macrolides).")
q(200, "The DOC of cryptosporidiasis is:", ["Nitazoxanide", "Metronidazole", "Paromomycin", "Albendazole"], "The cryptosporidiasis block: nitazoxanide (DOC).")
q(200, "Nitazoxanide was sourced from:", ["Niclosamide (anti-helminthic drug)", "Metronidazole", "Chloroquine", "Emetine"], "The source line: niclosamide (anti-helminthic drug).")
q(200, "The MOA of nitazoxanide is:", ["Inhibits PFOR enzyme, blocking electron transport", "Free radical production only", "Inhibits ATP synthase", "Binds haemoglobin"], "The MOA line: inhibits PFOR enzyme - blocks electron transport.")

unit("Leishmaniasis", "Visceral leishmaniasis (kala azar) DOC is IV liposomal amphotericin B, which has decreased nephrotoxicity; oral miltefosine - also the DOC for post-kala azar dermal leishmaniasis - causes nausea, vomiting and diarrhea and is contraindicated in pregnancy due to teratogenicity. Visceral alternatives are paromomycin, pentamidine and sitamaquine. Cutaneous leishmaniasis DOC is sodium stibogluconate, with LAmB, paromomycin and pentamidine as alternatives.")
q(200, "The DOC of visceral leishmaniasis (kala azar) is:", ["IV liposomal amphotericin B (LAmB)", "Oral miltefosine", "Sodium stibogluconate", "Pentamidine"], "The visceral DOC: IV liposomal amphotericin B (LAmB).")
q(200, "Liposomal amphotericin B is preferred over conventional formulations because of:", ["Decreased nephrotoxicity", "Decreased hepatotoxicity", "Better oral absorption", "Lower cost"], "The parenthetical under LAmB: decreased nephrotoxicity.")
q(200, "The oral drug for visceral leishmaniasis is:", ["Miltefosine", "Sitamaquine", "Paromomycin", "Sodium stibogluconate"], "The visceral block: oral - miltefosine.")
q(200, "The DOC for post-kala azar dermal leishmaniasis is:", ["Miltefosine", "LAmB", "Sodium stibogluconate", "Pentamidine"], "The note: miltefosine - also DOC for post-kala azar dermal leishmaniasis.")
q(200, "Side effects of miltefosine include:", ["Nausea, vomiting and diarrhea", "Hemolysis and methemoglobinemia", "Bull's eye retinopathy", "QT prolongation"], "The side-effect bracket: nausea & vomiting, diarrhea.")
q(200, "Miltefosine is contraindicated in pregnancy because it is:", ["Teratogenic", "Abortifacient only", "Nephrotoxic", "Hepatotoxic"], "The C/I line: pregnancy (D/t teratogenic effect).")
q(200, "Which is an alternative drug for visceral leishmaniasis?", ["Sitamaquine", "Sodium stibogluconate", "Fexinidazole", "Suramin"], "The alternatives list: paromomycin, pentamidine, sitamaquine.")
q(200, "The DOC of cutaneous leishmaniasis is:", ["Sodium stibogluconate", "Miltefosine", "LAmB", "Sitamaquine"], "The cutaneous branch: DOC sodium stibogluconate.")
q(200, "Which is an alternative drug for cutaneous leishmaniasis?", ["Pentamidine", "Miltefosine", "Suramin", "Eflornithine"], "Cutaneous alternatives: LAmB, paromomycin, pentamidine.")

unit("Trypanosomiasis", "African sleeping sickness is staged by species: East African - early IV suramin, late IV melarsoprol; West African - early IV pentamidine, late IV eflornithine; oral fexinidazole (approved 2018) is the cheaper, easier alternative. American Chagas disease DOC is benznidazole with nifurtimox as alternative.")
q(200, "Early East African sleeping sickness is treated with:", ["IV suramin", "IV pentamidine", "IV melarsoprol", "IV eflornithine"], "The East African early branch: IV suramin.")
q(200, "Late East African trypanosomiasis is treated with:", ["IV melarsoprol", "IV suramin", "IV pentamidine", "Oral fexinidazole only"], "The East African late branch: IV melarsoprol.")
q(200, "Early West African sleeping sickness is treated with:", ["IV pentamidine", "IV suramin", "IV eflornithine", "IV melarsoprol"], "The West African early branch: IV pentamidine.")
q(200, "Late West African trypanosomiasis is treated with:", ["IV eflornithine", "IV pentamidine", "IV suramin", "Benznidazole"], "The West African late branch: IV eflornithine.")
q(200, "The oral alternative (approved 2018) for trypanosomiasis described as cheaper and easier is:", ["Fexinidazole", "Nifurtimox", "Miltefosine", "Benznidazole"], "The note: oral fexinidazole (approved 2018) - cheaper, easier alternative.")
q(200, "African sleeping sickness is also called:", ["Sleeping sickness", "Chagas disease", "Kala azar", "Guinea worm disease"], "The branch heading: African (sleeping sickness).")
q(200, "The DOC of American trypanosomiasis (Chagas disease) is:", ["Benznidazole", "Nifurtimox", "Suramin", "Miltefosine"], "The American branch: DOC benznidazole.")
q(200, "The alternative drug for Chagas disease is:", ["Nifurtimox", "Fexinidazole", "Eflornithine", "Melarsoprol"], "The American branch: alternative nifurtimox.")

unit("Babesiosis", "The treatment of choice for babesiosis - mild, moderate or severe - is atovaquone plus azithromycin. Earlier TOC split by severity: quinine plus clindamycin for mild-to-moderate disease and atovaquone-azithromycin for severe disease.")
q(201, "The current TOC for babesiosis (mild, moderate & severe) is:", ["Atovaquone + azithromycin", "Quinine + clindamycin", "Chloroquine + primaquine", "Artesunate + clindamycin"], "The TOC line: atovaquone + azithromycin (for mild, moderate & severe).")
q(201, "In the earlier TOC, mild-to-moderate babesiosis was treated with:", ["Quinine + clindamycin", "Atovaquone + azithromycin", "Suramin", "Pentamidine"], "The note: earlier TOC - mild to moderate: quinine + clindamycin.")
q(201, "In the earlier TOC, severe babesiosis was treated with:", ["Atovaquone + azithromycin", "Quinine + clindamycin", "Mefloquine", "Artesunate"], "The note: severe - atovaquone + azithromycin.")

unit("Plasmodium Life Cycle", "The mosquito bite injects sporozoites, the infective form for humans, which travel via the bloodstream and enter the liver. In hepatic schizonts some parasites stay dormant as hypnozoites while others replicate; rupture releases merozoites that infect RBCs, forming erythrocytic schizonts whose rupture causes fever and chills. Some merozoites form gametocytes - the infective form for the mosquito, taken up with a blood meal.")
q(201, "The infective form of Plasmodium for humans injected by the mosquito is:", ["Sporozoites", "Merozoites", "Gametocytes", "Hypnozoites"], "The diagram: sporozoites (infective form for humans) from the mosquito bite.")
q(201, "Sporozoites first travel to and enter:", ["Liver", "RBCs", "Spleen", "Bone marrow"], "The cycle: travels via blood stream, enters hepatic schizont in liver.")
q(201, "The dormant form within the hepatic schizont is the:", ["Hypnozoite", "Gametocyte", "Trophozoite", "Sporozoite"], "The liver diagram shows dormancy leading to hypnozoite.")
q(201, "Rupture of erythrocytic schizonts within RBCs causes:", ["Fever and chills", "Relapse", "Transmission to mosquito", "Hepatomegaly"], "The cycle: rupture leads to symptoms - increased fever, chills.")
q(201, "The infective form of Plasmodium for the mosquito is:", ["Gametocytes", "Sporozoites", "Merozoites", "Hypnozoites"], "The diagram: gametocytes (infective form for mosquito).")
q(201, "Gametocytes are taken up by the mosquito:", ["Ingested with blood meal", "Through fecal contamination", "Via salivary glands directly", "Through skin penetration"], "The cycle: gametocytes ingested with blood meal by mosquito.")
q(201, "Merozoites released from the liver infect:", ["RBCs", "Liver cells again only", "WBCs", "Platelets"], "The cycle: liver rupture releases merozoites which infect RBC.")

unit("Stages of Drug Action and Artemisinins", "Hypnozoiticidal drugs prevent relapse - primaquine for 14 days or single-dose tafenoquine - given along with treatment for radical cure or as terminal prophylaxis; hypnozoites are seen only in vivax and ovale. Gametocidal drugs (primaquine, artemisinin group) block transmission. Erythrocytic schizontocidals are fast acting (DOC) or slow acting, and the treatment regimen combines 1 fast acting + 1 slow acting drug. Artemisinins are the most potent and fastest acting schizontocidals, acting by free radical production and contraindicated in the first trimester; artesunate is IV and oral while artemether and dihydroartemisinin are only oral. Because they are short acting they cannot be monotherapy or prophylaxis. Severe falciparum malaria DOC is continuous IV artesunate infusion for 48 hours followed by a treatment regimen; uncomplicated malaria is another use.")
q(202, "Hypnozoiticidal drugs:", ["Prevent relapse", "Block transmission", "Treat acute RBC infection only", "Prevent infection"], "The hypnozoiticidal block: prevents relapse.")
q(202, "Hypnozoite-eradicating schedules written are:", ["Primaquine x 14 days or tafenoquine single dose", "Chloroquine x 3 days", "Artesunate x 7 days", "Mefloquine weekly x 4"], "The block: primaquine x 14 days; tafenoquine single dose.")
q(202, "Primaquine/tafenoquine given along with treatment achieves:", ["Radical cure", "Terminal prophylaxis only", "Blood schizontocidal cure", "Transmission block only"], "The bracket: along with treatment - radical cure.")
q(202, "The alternative purpose of the primaquine/tafenoquine course named is:", ["Terminal prophylaxis", "Causal prophylaxis", "Suppressive therapy", "Pre-erythrocytic vaccine effect"], "The bracket lists radical cure and terminal prophylaxis.")
q(202, "Hypnozoites are seen ONLY in:", ["Vivax and ovale", "Falciparum and vivax", "Malariae and ovale", "All species"], "The block: hypnozoite seen only in vivax, ovale.")
q(202, "Gametocidal drugs act by:", ["Blocking transmission of malaria", "Preventing relapse", "Curing acute infection", "Blocking liver entry"], "The block: gametocidal drugs - blocks transmission of malaria.")
q(202, "Drugs listed as gametocidal are:", ["Primaquine and artemisinin group", "Chloroquine and quinine", "Mefloquine and doxycycline", "Sulfadoxine-pyrimethamine only"], "The block: primaquine, artemisinin group of drugs.")
q(202, "The regimen for treatment of malaria is:", ["1 fast acting + 1 slow acting", "2 fast acting drugs", "Only slow acting drugs", "3 fast acting drugs"], "The line: 1 fast acting + 1 slow acting.")
q(202, "The most potent and fastest acting schizontocidal drugs are:", ["Artemisinin group", "Chloroquine", "Quinine", "Mefloquine"], "The artemisinin block: most potent and fastest acting schizontocidal drugs.")
q(202, "The MOA of artemisinins is:", ["Free radical production (C/I in 1st trimester of pregnancy)", "Heme polymerase inhibition", "DHFR inhibition", "Block of K+ channels"], "The MOA line: free radical production, C/I in 1st trimester of pregnancy.")
q(202, "Which artemisinin is available both IV and oral?", ["Artesunate", "Artemether", "Dihydroartemisinin", "Arteether"], "The drug list: artesunate IV & oral; artemether and DHA only oral.")
q(202, "The artemisinins that are ONLY oral are:", ["Artemether and dihydroartemisinin", "Artesunate only", "Artesunate and artemether", "DHA and artesunate"], "The bracket groups artemether and dihydroartemisinin as only oral.")
q(202, "The disadvantage of artemisinins due to short action:", ["Cannot be used as monotherapy or prophylaxis", "Cannot be combined with other drugs", "Cannot be given IV", "Cannot be used in children"], "The disadvantage block: can't be used as monotherapy; can't be used for prophylaxis.")
q(202, "The DOC for severe falciparum malaria is:", ["Continuous IV infusion artesunate for 48 hr (followed by treatment regimen)", "IM artemether for 3 days", "Oral quinine for 7 days", "IV chloroquine infusion"], "The uses block: severe falciparum malaria DOC - continuous IV artesunate 48 hr followed by treatment regimen.")
q(202, "Besides severe falciparum malaria, artemisinins are used in:", ["Uncomplicated malaria", "Vivax relapse only", "Malaria prophylaxis", "Babesiosis prophylaxis"], "The second use: uncomplicated malaria.")

unit("Treatment of Uncomplicated Malaria", "Vivax malaria: TOC chloroquine (DOC) for 3 days plus primaquine x 14 days or single-dose tafenoquine; in pregnancy the primaquine/tafenoquine part is given post-partum because it is not safe. Chloroquine-resistant falciparum malaria: pregnant first trimester gets quinine (DOC) + clindamycin, second and third trimesters get ACT; the normal population gets ACT, or quinine + one of tetracycline, doxycycline (both not safe in pregnancy) or clindamycin. ACT options: oral artesunate + sulfadoxine + pyrimethamine for all Indian states, or oral artemether + lumefantrine for north-eastern states.")
q(203, "TOC of vivax malaria is:", ["Chloroquine (DOC) x 3 d + primaquine x 14 d/tafenoquine single dose", "ACT for 3 days", "Quinine + clindamycin", "Artesunate IV x 7 days"], "The vivax branch: chloroquine (DOC) x 3 d + primaquine x 14 d/tafenoquine single dose.")
q(203, "In pregnant vivax malaria, primaquine/tafenoquine is:", ["Given post-partum (not safe)", "Given in reduced dose", "Given in first trimester only", "Replaced by chloroquine"], "The vivax branch: pregnant - given post-partum (not safe).")
q(203, "In chloroquine-resistant falciparum malaria, the first-trimester pregnant woman gets:", ["Quinine (DOC) + clindamycin", "ACT", "Quinine + doxycycline", "Sulfadoxine-pyrimethamine"], "The pregnant female branch: 1st trimester quinine (DOC) + clindamycin.")
q(203, "A second/third trimester pregnant woman with falciparum malaria gets:", ["ACT", "Quinine (DOC) + clindamycin", "Quinine + tetracycline", "Chloroquine"], "The pregnant branch: 2nd & 3rd trimester - ACT.")
q(203, "The ACT combination for ALL Indian states is:", ["Oral artesunate + sulfadoxine + pyrimethamine", "Oral artemether + lumefantrine", "Artesunate + clindamycin", "Artemether + primaquine"], "ACT list item 1: artesunate + SP - all Indian states.")
q(203, "The ACT combination reserved for NORTH-EASTERN states is:", ["Oral artemether + lumefantrine", "Oral artesunate + sulfadoxine + pyrimethamine", "Artemether + doxycycline", "Artesunate + mefloquine"], "ACT list item 2: artemether + lumefantrine - north-eastern states.")
q(203, "In the normal population with falciparum malaria, alternatives to ACT include:", ["Quinine + one of tetracycline/doxycycline/clindamycin", "Chloroquine + primaquine", "Artemether + SP", "Mefloquine monotherapy"], "The normal population branch: ACT, alternatives quinine + one of tetracycline, doxycycline, clindamycin.")
q(203, "Among the quinine-combination alternatives for falciparum malaria, the drugs NOT safe in pregnancy are:", ["Tetracycline and doxycycline", "Clindamycin and quinine", "Tetracycline and clindamycin", "All three alternatives"], "The bracket marks tetracycline/doxycycline not safe in pregnancy.")

unit("Chloroquine and Quinine", "Chloroquine binds haemoglobin to generate toxic haem products; resistance develops by drug efflux from the vacuole of cells. Infectious uses: malaria, hepatic amoebiasis, infectious mononucleosis; non-infectious: rheumatoid arthritis, SLE, discoid LE and porphyria cutanea tarda. Its classic side effect is bull's eye retinopathy with multiple concentric circles plus whorl-like corneal deposits. Quinine is used in resistant malaria; side effects are alpha-blockade (hypotension), increased insulin release (hypoglycemia), potassium-channel block (QT prolongation), cinchonism from the cinchona plant (tinnitus, vertigo) and black water fever if doses are inadequate.")
q(203, "The MOA of chloroquine is:", ["Binds to haemoglobin leading to toxic haem products", "Free radical production", "Inhibits PFOR enzyme", "Blocks microtubules"], "The chloroquine block: MOA binds to haemoglobin - toxic haem products.")
q(203, "Mechanism of chloroquine resistance is:", ["Drug efflux from vacuole of cells", "Drug inactivation by catalase", "Target gene amplification", "Ribosomal mutation"], "The block: mechanism of resistance - drug efflux from vacuole of cells.")
q(203, "An INFECTIOUS use of chloroquine listed besides malaria is:", ["Hepatic amoebiasis", "Giardiasis", "Babesiosis", "Trypanosomiasis"], "Infectious uses: malaria, hepatic amoebiasis, infectious mononucleosis.")
q(203, "Which NON-infectious use of chloroquine is listed?", ["Rheumatoid arthritis", "Gout", "Psoriasis", "Atopic dermatitis"], "Non-infectious uses: RA, SLE, discoid LE, porphyria cutanea tarda.")
q(203, "Chloroquine is used in all of these non-infectious conditions EXCEPT:", ["Porphyria cutanea tarda", "SLE", "Discoid LE", "Lichen planus"], "The list has RA, SLE, discoid LE, porphyria cutanea tarda.")
q(203, "The characteristic ocular side effect of chloroquine is:", ["Bull's eye retinopathy", "Optic neuritis", "Red-green color blindness", "Uveitis"], "The side-effect line: bull's eye retinopathy.")
q(203, "Bull's eye retinopathy of chloroquine shows:", ["Multiple concentric circles + whorl-like corneal deposits", "Optic disc pallor only", "Retinal hemorrhages", "Cherry red spot"], "The description: multiple concentric circles + whorl-like corneal deposits.")
q(203, "Quinine is used in:", ["Resistant malaria", "Uncomplicated vivax malaria as DOC", "Malaria prophylaxis", "Babesiosis as TOC"], "The quinine block: use - resistant malaria.")
q(203, "Quinine's alpha-blocker side effect causes:", ["Hypotension", "Hypertension", "Bradycardia", "Uterine contraction"], "The side-effect list: alpha blocker - hypotension.")
q(203, "Quinine increases insulin release causing:", ["Hypoglycemia", "Hyperglycemia", "Ketoacidosis", "Insulin resistance"], "The side-effect list: increased insulin release - hypoglycemia.")
q(203, "Quinine blocks K+ channels causing:", ["QT prolongation", "QT shortening", "QRS widening only", "Sinus bradycardia"], "The side-effect list: block K+ channels - QT prolongation.")
q(203, "Cinchonism, with tinnitus and vertigo, is derived from the:", ["Cinchona plant", "Artemisia annua plant", "Poppy plant", "Rauwolfia plant"], "The note: cinchonism (derived from cinchona plant): tinnitus, vertigo.")
q(203, "Inadequate doses of quinine lead to:", ["Black water fever", "Cinchonism", "Bull's eye retinopathy", "Hemolysis in G6PD deficiency"], "The line: if inadequate doses - black water fever.")

unit("Mefloquine, Malaria Prophylaxis and Other Drugs", "Mefloquine treats resistant malaria and provides prophylaxis for travel of 6 weeks or more; side effects are neuropsychiatric effects and conduction block (contraindicated with quinine and halofantrine). Prophylaxis by travel duration: below 6 weeks uses doxycycline 100 mg OD starting 2 days before travel and stopping 4 weeks after; 6 weeks or more uses mefloquine 250 mg/week starting 2 weeks before and stopping 4 weeks after. Atovaquone + proguanil is for resistant malaria; proguanil inhibits ovulation in the mosquito. Tetracycline, doxycycline and clindamycin are for resistant malaria, with clindamycin safe in children and pregnancy.")
q(204, "Mefloquine is used for resistant malaria and prophylaxis when travel duration is:", [">=6 weeks", "<6 weeks", "<2 days", "Any duration"], "The mefloquine use line: prophylaxis of malaria for travel >=6 wks.")
q(204, "A characteristic side effect of mefloquine is:", ["Neuropsychiatric effects", "Bull's eye retinopathy", "Green urine", "Hemolysis"], "The side-effect list: neuropsychiatric effects.")
q(204, "Mefloquine causes conduction block, so it is contraindicated with:", ["Quinine and halofantrine", "Artesunate and lumefantrine", "Chloroquine and primaquine", "Atovaquone and proguanil"], "The line: conduction block (C/I with quinine & halofantrine).")
q(204, "For travel <6 weeks, malaria prophylaxis is:", ["Doxycycline 100 mg OD", "Mefloquine 250 mg/week", "Atovaquone-proguanil daily", "Primaquine weekly"], "The prophylaxis note: <6 weeks - doxycycline 100 mg OD.")
q(204, "Doxycycline prophylaxis (<6 weeks travel) is started and stopped:", ["Start 2 days before travel, stop 4 weeks after", "Start 2 weeks before, stop 4 weeks after", "Start 1 day before, stop 1 week after", "Start on arrival, stop at departure"], "The note: start 2 days before travel, stop 4 weeks after travel.")
q(204, "Mefloquine prophylaxis (>=6 weeks travel) dosing written is:", ["250 mg/week, start 2 weeks before, stop 4 weeks after travel", "250 mg/week, start 2 days before, stop 2 days after", "100 mg OD, start 2 weeks before", "250 mg OD, start 1 week before"], "The note: mefloquine 250 mg/week, start 2 weeks before travel, stop 4 weeks after.")
q(204, "Both prophylaxis schedules share which stop rule?", ["Stop 4 weeks after travel", "Stop at return", "Stop 1 week after travel", "Stop 4 weeks before travel"], "Both columns end: stop 4 weeks after travel.")
q(204, "Atovaquone + proguanil is used for:", ["Resistant malaria", "Babesiosis TOC", "Vivax relapse prevention", "Cryptosporidiasis"], "The block: use - resistant malaria.")
q(204, "The written MOA note for atovaquone-proguanil says proguanil inhibits:", ["Ovulation in mosquito", "Liver schizogony", "RBC invasion", "Hemozoin formation"], "The MOA line: proguanil inhibits ovulation in mosquito.")
q(204, "Among tetracycline/doxycycline/clindamycin for resistant malaria, the one safe in children and pregnancy is:", ["Clindamycin", "Doxycycline", "Tetracycline", "All three"], "The block: clindamycin is safe for use children & pregnancy.")

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
