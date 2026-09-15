# -*- coding: utf-8 -*-
import json
CH = 50
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

unit("Benzimidazoles", "The benzimidazoles are mebendazole (most common in western countries), triclabendazole, thiabendazole and albendazole - a prodrug, most common in India, activated in the liver to albendazole sulfoxide. Its MOA is blocking microtubules in the intestinal cells of helminths, reducing glucose absorption and thus ATP.")
q(205, "The benzimidazole most common in WESTERN countries is:", ["Mebendazole", "Albendazole", "Thiabendazole", "Triclabendazole"], "The drug list: mebendazole - m/c in western countries.")
q(205, "The benzimidazole most common in INDIA is:", ["Albendazole", "Mebendazole", "Triclabendazole", "Thiabendazole"], "Albendazole is marked m/c in India.")
q(205, "Which is NOT a benzimidazole listed?", ["Praziquantel", "Mebendazole", "Triclabendazole", "Thiabendazole"], "The list: mebendazole, triclabendazole, thiabendazole, albendazole.")
q(205, "Albendazole is a:", ["Prodrug", "Active drug directly", "Metabolite", "Enzyme inducer"], "The albendazole line: prodrug.")
q(205, "The active drug of albendazole formed in the liver is:", ["Albendazole sulfoxide", "Albendazole sulfone", "Albendazole N-oxide", "Fenbendazole"], "The line: active drug - albendazole sulfoxide (in liver).")
q(205, "The MOA of albendazole is:", ["Blocks microtubules in intestinal cells of helminths, decreasing glucose absorption (decreased ATP)", "Stimulates glutamate-gated chloride channels", "Stimulates Ca2+ channels", "Inhibits ACh esterase"], "The MOA line: blocks microtubules in intestinal cells of helminths, leading to down glucose absorption (down ATP).")

unit("Common Helminths and Drugs: Nematodes", "Nematode DOCs: albendazole covers round worm, whip worm, hook worm, Enterobius vermicularis and Trichinella spiralis; ivermectin covers Strongyloides and Onchocerca volvulus (river blindness); diethylcarbamazine covers Loa loa and filariasis, whose TOC is IDA (ivermectin, DEC, albendazole); metronidazole covers dracunculiasis.")
q(205, "The DOC column for round worm, whip worm, hook worm, Enterobius vermicularis and Trichinella spiralis is:", ["Albendazole", "Ivermectin", "DEC", "Metronidazole"], "The nematode DOC tree lists these under albendazole.")
q(205, "Ivermectin is the DOC for:", ["Strongyloides and Onchocerca volvulus", "Round worm and whip worm", "Loa loa and filariasis", "Dracunculiasis"], "The ivermectin branch: strongyloides, onchocerca volvulus.")
q(205, "Onchocerca volvulus causes:", ["River blindness", "Dracunculiasis", "Filariasis", "Neurocysticercosis"], "The branch writes onchocerca volvulus (river blindness).")
q(205, "The DOC for Loa loa is:", ["Diethylcarbamazine (DEC)", "Ivermectin", "Albendazole", "Praziquantel"], "The DEC branch lists Loa loa.")
q(205, "The TOC for filariasis is:", ["IDA (ivermectin, DEC, albendazole)", "DEC monotherapy", "Ivermectin monotherapy", "Praziquantel + albendazole"], "The filariasis note: TOC IDA (ivermedtin, DEC, albendazole).")
q(205, "The drug listed as DOC for dracunculiasis is:", ["Metronidazole", "DEC", "Ivermectin", "Thiabendazole"], "The metronidazole branch: dracunculiasis.")
q(205, "Which nematode infection is treated with metronidazole as DOC?", ["Dracunculiasis", "Strongyloidiasis", "Onchocerciasis", "Trichinellosis"], "Only dracunculiasis sits under metronidazole in the DOC tree.")

unit("Cestodes and Trematodes", "Cestode DOCs: albendazole for neurocysticercosis (T. solium) and echinococcus; praziquantel for intestinal T. solium, T. saginata, H. nana and D. latum. First priority in neurocysticercosis treatment is steroids to reduce perilesional edema. Trematode DOCs: triclabendazole for Fasciola hepatica; praziquantel for other liver flukes, all lung flukes and schistosoma; albendazole is ineffective against trematodes.")
q(205, "The DOC for neurocysticercosis (T. solium) is:", ["Albendazole", "Praziquantel", "Mebendazole", "DEC"], "The cestode DOC tree lists neurocysticercosis under albendazole.")
q(205, "The FIRST PRIORITY of treatment of neurocysticercosis is:", ["Steroids (to decrease perilesional edema)", "Albendazole immediately", "Praziquantel immediately", "Surgery"], "The note: first priority of treatment of neurocysticercosis is steroids (to down perilesional edema).")
q(205, "The DOC for echinococcus is:", ["Albendazole", "Praziquantel", "Mebendazole", "Niclosamide"], "The cestode DOC tree lists echinococcus under albendazole.")
q(205, "Praziquantel as cestode DOC covers:", ["Intestinal T. solium, T. saginata, H. nana, D. latum", "Neurocysticercosis and echinococcus", "Fasciola hepatica", "Schistosoma only"], "The praziquantel branch lists intestinal T. solium, T. saginata, H. nana, D. latum.")
q(205, "The DOC for Fasciola hepatica is:", ["Triclabendazole", "Praziquantel", "Albendazole", "Mebendazole"], "The trematode DOC tree: triclabendazole - fasciola hepatica.")
q(205, "Under praziquantel, the trematodes covered are:", ["Other liver flukes, all lung flukes, schistosoma", "Only Fasciola hepatica", "Only schistosoma", "Cestodes only"], "The praziquantel trematode branch lists other liver flukes, all lung flukes, schistosoma.")
q(205, "The note about albendazole and flukes states albendazole is:", ["Ineffective against trematodes", "DOC for trematodes", "DOC for lung flukes", "Effective against all flukes"], "The note: albendazole ineffective against trematodes.")
q(206, "Schistosoma DOC among the trematode drugs is:", ["Praziquantel", "Triclabendazole", "Albendazole", "Metrifonate only"], "Schistosoma is listed in the praziquantel branch of the trematode DOC tree.")

unit("Specifics of Drugs", "Ivermectin stimulates glutamate-sensitive chloride channels causing tonic paralysis; it is also the oral DOC in scabies, and causes a Mazzotti-like reaction (rash, lymphadenopathy) from dying parasites, also seen with DEC. Praziquantel stimulates Ca2+ channels causing spastic paralysis, as do pyrantel pamoate (Nn receptors) and metrifonate. Metrifonate inhibits ACh esterase raising ACh and is used for Schistosoma haematobium. Pyrantel pamoate was earlier used for soil-transmitted helminths. Piperazine stimulates GABA-sensitive Cl- channels causing flaccid paralysis and is used for soil-transmitted helminths.")
q(206, "The MOA of ivermectin is:", ["Stimulates glutamate sensitive chloride channels leading to tonic paralysis", "Stimulates Ca2+ channels causing spastic paralysis", "Stimulates GABA-sensitive Cl- channels", "Inhibits ACh esterase"], "The ivermectin block: stimulates glutamate sensitive chloride channels, then tonic paralysis.")
q(206, "The type of paralysis caused by ivermectin is:", ["Tonic paralysis", "Flaccid paralysis", "Spastic paralysis", "No paralysis"], "The arrow under ivermectin MOA ends in tonic paralysis.")
q(206, "The other use of ivermectin written is:", ["Oral DOC in scabies", "Oral DOC in pediculosis", "DOC in malaria", "DOC in giardiasis"], "The line: other uses - oral DOC in scabies.")
q(206, "The side effect of ivermectin is:", ["Mazzotti-like reaction (D/t dying parasite)", "Bull's eye retinopathy", "Green urine", "Disulfiram-like reaction"], "The side-effect line: mazzotti-like reaction (d/t dying parasite).")
q(206, "Features of the Mazzotti-like reaction include:", ["Rash and lymphadenopathy", "Hemolysis and methemoglobinemia", "Optic neuritis", "QT prolongation"], "The bracket under Mazzotti-like: rash, lymphadenopathy.")
q(206, "Besides ivermectin, the Mazzotti-like reaction is also seen with:", ["DEC", "Albendazole", "Praziquantel", "Piperazine"], "The note: also seen in DEC.")
q(206, "The MOA of praziquantel is:", ["Stimulates Ca2+ channels leading to spastic paralysis", "Stimulates glutamate Cl- channels", "Blocks microtubules", "Stimulates GABA Cl- channels"], "The praziquantel block: stimulates Ca2+ channels, spastic paralysis.")
q(206, "Besides praziquantel, spastic paralysis is also caused by:", ["Pyrantel pamoate and metrifonate", "Piperazine and ivermectin", "Albendazole and mebendazole", "DEC and ivermectin"], "The line: also caused by pyrantel pamoate, metrifonate.")
q(206, "The MOA of metrifonate is:", ["Inhibits ACh esterase leading to increased ACh", "Stimulates Nn receptors", "Blocks Ca2+ channels", "Stimulates GABA Cl- channels"], "The metrifonate block: MOA inhibits ACh esterase, increased ACh.")
q(206, "Metrifonate is used for:", ["Schistosoma haematobium", "Fasciola hepatica", "T. saginata", "Onchocerca volvulus"], "The metrifonate use line: schistosoma haematobium.")
q(206, "Pyrantel pamoate acts by:", ["Stimulating Nn receptors causing spastic paralysis", "Blocking Nn receptors", "Stimulating GABA Cl- channels", "Blocking microtubules"], "The pyrantel block: stimulates Nn receptors, spastic paralysis.")
q(206, "The use of pyrantel pamoate written is:", ["Earlier used for soil transmitted helminths", "DOC for filariasis", "DOC for scabies", "DOC for schistosomiasis"], "The use line: earlier used for soil transmitted helminths.")
q(206, "The MOA of piperazine is:", ["Stimulates GABA sensitive Cl- channels causing flaccid paralysis", "Stimulates glutamate Cl- channels", "Stimulates Ca2+ channels", "Inhibits AChE"], "The piperazine block: stimulates GABA sensitive Cl- channels, flaccid paralysis.")
q(206, "Flaccid paralysis of worms is produced by:", ["Piperazine", "Ivermectin", "Praziquantel", "Pyrantel pamoate"], "Only piperazine's arrow ends in flaccid paralysis.")
q(206, "Piperazine is used for:", ["Soil transmitted helminths", "Filariasis", "River blindness", "Schistosoma haematobium"], "The piperazine use line: soil transmitted helminths.")
q(206, "Which drug pair correctly matches paralysis type?", ["Ivermectin - tonic; praziquantel - spastic; piperazine - flaccid", "Ivermectin - spastic; praziquantel - tonic; piperazine - flaccid", "Ivermectin - flaccid; praziquantel - tonic; piperazine - spastic", "All three cause spastic paralysis"], "Ivermectin gives tonic, praziquantel spastic, piperazine flaccid paralysis.")

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
