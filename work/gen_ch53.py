# -*- coding: utf-8 -*-
import json
CH = 53
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

unit("GnRH and GnRH-Related Drugs", "Hypothalamic GnRH is released in pulsatile fashion, acting on Gs/Gq receptors of pituitary gonadotroph cells to raise LH/FSH: in females this drives ovulation (LH surge) and synthesis of estrogen and progesterone; in males, spermatogenesis and testosterone. GnRH agonists - goserelin, buserelin, nafarelin, leuprolide - given intermittently raise LH/FSH and treat infertility due to anovulation or oligospermia plus delayed puberty; continuous dosing first raises then lowers LH/FSH by receptor downregulation, treating precocious puberty, estrogen-dependent conditions (ER-positive breast cancer, endometriosis, fibroids) and testosterone-dependent prostate cancer (DOC goserelin). GnRH antagonists - ganirelix, cetrorelix, abarelix, elagolix - directly lower LH/FSH. Gonadorelin, the GnRH analog, diagnoses the cause of hypogonadism (hypothalamic vs pituitary) and treats anovulation.")
q(215, "GnRH is released from the hypothalamus in which pattern?", ["Pulsatile release", "Continuous release", "Only nocturnal release", "Random tonic release"], "The axis diagram labels GnRH (pulsatile release).")
q(215, "GnRH acts on which receptor of pituitary gonadotroph cells?", ["Gs/Gq receptor", "Gi receptor", "Nuclear receptor", "Ligand-gated chloride channel"], "The note: Gs/Gq receptor on pituitary gonadotroph cells.")
q(215, "GnRH increases pituitary release of:", ["LH/FSH", "ACTH", "GH", "TSH"], "The flow: pituitary gland then increased LH/FSH.")
q(215, "In females, the LH surge produces:", ["Ovulation", "Spermatogenesis", "Testosterone synthesis", "Luteolysis"], "The female branch: ovulation (LH surge).")
q(215, "LH/FSH in females stimulates synthesis of:", ["Estrogen and progesterone", "Testosterone and DHT", "Inhibin only", "Relaxin only"], "The female branch: synthesis of estrogen, progesterone.")
q(215, "In males, LH/FSH effects written are:", ["Spermatogenesis and testosterone", "Ovulation and estrogen", "Milk ejection", "Sperm capacitation only"], "The male branch: spermatogenesis, testosterone.")
q(215, "The GnRH agonists listed are:", ["Goserelin, buserelin, nafarelin, leuprolide", "Ganirelix, cetrorelix, abarelix, elagolix", "Gonadorelin, clomiphene, letrozole", "Flutamide, bicalutamide, enzalutamide"], "The agonist branch lists goserelin, buserelin, nafarelin, leuprolide.")
q(215, "GnRH antagonists produce which hormonal change?", ["Decreased LH/FSH", "Increased LH/FSH", "Initial increase then decrease", "No hormonal change"], "The antagonist branch: decreased LH/FSH.")
q(215, "The GnRH antagonists listed are:", ["Ganirelix, cetrorelix, abarelix, elagolix", "Goserelin, buserelin, nafarelin, leuprolide", "Finasteride, dutasteride", "Tamoxifen, raloxifene"], "The antagonist list: ganirelix, cetrorelix, abarelix, elagolix.")
q(215, "Intermittent dosing of GnRH agonists produces:", ["Increased LH/FSH", "Decreased LH/FSH", "Biphasic LH/FSH", "No change"], "The agonist split: intermittent dosing - increased LH/FSH.")
q(215, "Intermittent GnRH agonist dosing is used in infertility due to:", ["Anovulation and oligospermia", "Fibroids and endometriosis", "Precocious puberty", "Prostate cancer"], "The use block: infertility d/t anovulation, oligospermia.")
q(215, "Intermittent GnRH agonist dosing is also used in:", ["Delayed puberty", "Precocious puberty", "Fibroids", "ER positive breast cancer"], "The second use: delayed puberty.")
q(215, "Continuous dosing of GnRH agonists causes LH/FSH to:", ["Initially increase, then decrease due to receptor downregulation", "Steadily increase", "Immediately decrease", "Remain unchanged"], "The continuous-dosing note: LH/FSH initial increased, then decreased (D/t receptor downregulation).")
q(215, "Continuous GnRH agonist dosing is used in:", ["Precocious puberty", "Delayed puberty", "Anovulatory infertility", "Oligospermia"], "The continuous-dosing use: precocious puberty.")
q(215, "Estrogen dependent conditions treated with continuous GnRH agonists are:", ["ER positive breast cancer, endometriosis, fibroids", "Prostate and testicular cancer", "Precocious puberty", "Hirsutism"], "The estrogen dependent conditions branch lists ER positive breast cancer, endometriosis, fibroids.")
q(215, "The DOC among GnRH agonists for prostate cancer is:", ["Goserelin", "Nafarelin", "Buserelin", "Leuprolide"], "The note: testosterone dependent cancers - prostate cancer (DOC goserelin).")
q(215, "The GnRH analog used to diagnose the cause of hypogonadism is:", ["Gonadorelin", "Leuprolide", "Elagolix", "Cetrorelix"], "The block: GnRH analog - gonadorelin.")
q(215, "Gonadorelin distinguishes hypogonadism due to:", ["Hypothalamic vs pituitary cause", "Ovarian vs testicular cause", "Primary vs tertiary cause", "Acquired vs congenital cause"], "The use line: diagnosis of cause of hypogonadism (hypothalamic/pituitary).")
q(215, "The second listed use of gonadorelin is:", ["Anovulation", "Fibroids", "Hirsutism", "Alopecia"], "The use list: anovulation.")

unit("Selective Estrogen Receptor Modulators (SERMs)", "Tamoxifen treats ER-positive breast cancer in premenopausal females; raloxifene provides prophylaxis of ER-positive breast cancer and treats post-menopausal osteoporosis in females at high risk for ER-positive breast cancer, used in post-menopausal females. Shared side effects are thrombosis and hot flashes, while uterine carcinoma occurs only with tamoxifen. Other SERMs: toremifene treats ER-positive breast cancer and ospemifene treats post-menopausal dyspareunia.")
q(216, "The use of tamoxifen written is:", ["Treatment of ER (+) breast cancer", "Prophylaxis of ER (+) breast cancer", "Post-menopausal osteoporosis", "Dyspareunia"], "The SERM table: tamoxifen use - treatment of ER(+) breast cancer.")
q(216, "Tamoxifen is used in which age group?", ["Premenopausal females", "Post-menopausal females", "Only males", "Children"], "The age-group row: tamoxifen - premenopausal females.")
q(216, "Raloxifene uses are:", ["Prophylaxis of ER (+) breast cancer and post-menopausal osteoporosis in high-risk females", "Treatment of ER (+) breast cancer only", "Dyspareunia only", "Anovulation"], "The raloxifene column: prophylaxis of ER(+) breast cancer; post-menopausal osteoporosis in females with high risk for ER(+) Ca breast.")
q(216, "Raloxifene is used in which age group?", ["Post-menopausal females", "Premenopausal females", "Adolescents", "Elderly males"], "The age-group row: raloxifene - post-menopausal females.")
q(216, "Uterine carcinoma as a SERM side effect is seen with:", ["Only tamoxifen", "Only raloxifene", "Both equally", "Neither"], "The side-effect row: uterine carcinoma (only tamoxifen).")
q(216, "Shared SERM side effects listed besides uterine carcinoma are:", ["Thrombosis and hot flashes", "Gynecomastia and impotence", "Bone fracture and edema", "Pancreatitis and angioedema"], "The side-effect list: thrombosis, hot flashes.")
q(216, "The other SERM used for treatment of ER(+) breast cancer is:", ["Toremifene", "Ospemifene", "Fulvestrant", "Letrozole"], "The other SERMs: toremifene - treatment of ER(+) breast cancer.")
q(216, "Ospemifene is used for:", ["Post-menopausal dyspareunia", "Osteoporosis", "ER(+) breast cancer prophylaxis", "Anovulation"], "The line: ospemifene - post menopausal dyspareunia.")

unit("SERDs: Clomiphene, Fulvestrant, Elacestrant", "Clomiphene citrate is a partial agonist at pituitary estrogen receptors: the positive feedback to the hypothalamus raises GnRH, raising LH and triggering ovulation; it is DOC for anovulation WITHOUT PCOS, while letrozole is DOC when PCOS is present. Fulvestrant blocks ER at breast, is 100 times more potent than tamoxifen and treats resistant post-menopausal breast cancer. Elacestrant is used for ER-positive breast cancer with ESR1 (estrogen receptor 1) mutation.")
q(216, "Clomiphene citrate acts as:", ["Partial agonist at pituitary estrogen receptor", "Full agonist at ovarian ER", "ER blocker at breast", "Aromatase inhibitor"], "The MOA line: partial agonist at pituitary estrogen receptor.")
q(216, "The ovulation cascade after clomiphene is:", ["Positive feedback to hypothalamus, increased GnRH, increased LH, ovulation", "Increased FSH only, ovulation", "Decreased GnRH, decreased LH, ovulation", "Direct ovarian stimulation"], "The flow: positive feedback to hypothalamus, then GnRH up, then LH up, then ovulation.")
q(216, "Clomiphene is DOC for anovulation:", ["Without PCOS", "With PCOS", "In post-menopausal women", "With fibroids"], "The use line: DOC for anovulation without PCOS.")
q(216, "DOC for anovulation WITH PCOS is:", ["Letrozole", "Clomiphene", "Tamoxifen", "Gonadorelin"], "The note: DOC for anovulation with PCOS is letrozole.")
q(216, "The MOA of fulvestrant is:", ["Blocks ER at breast", "Partial agonist at pituitary ER", "Blocks aromatase", "Degrades GnRH receptor"], "The fulvestrant block: MOA blocks ER at breast.")
q(216, "Fulvestrant potency compared with tamoxifen is:", ["100x tamoxifen", "10x tamoxifen", "Equal", "1/100th"], "The line: potency 100x tamoxifen.")
q(216, "Fulvestrant is used in:", ["Resistant post-menopausal breast cancer", "Premenopausal breast cancer first line", "Osteoporosis", "Dyspareunia"], "The use line: resistant post-menopausal breast cancer.")
q(216, "Elacestrant is used for ER-positive breast cancer with:", ["ESR1 mutation (estrogen receptor 1)", "BRCA1 mutation", "HER2 amplification", "P53 mutation"], "The line: ER +ve breast cancer with ESR1 mutation (estrogen receptor 1).")

unit("Selective Progesterone Receptor Modulator (SPRM)", "Ulipristal is the SPRM used for emergency contraception - 30 mg single dose within 5 days of unprotected intercourse. The DOC for emergency contraception in India is levonorgestrel: 1.5 mg single dose within 72 hours, or 0.75 mg two doses 12 hours apart within 72 hours of unprotected intercourse.")
q(217, "The SPRM listed is:", ["Ulipristal", "Ospemifene", "Raloxifene", "Pramlintide"], "The SPRM block: ulipristal.")
q(217, "The use of ulipristal written is:", ["Emergency contraception", "Treatment of fibroids only", "Habitual abortion", "Endometriosis"], "The use line: emergency contraception.")
q(217, "The ulipristal dose for emergency contraception is:", ["30 mg single dose within 5 days of unprotected intercourse", "1.5 mg single dose within 72 hours", "0.75 mg two doses 12 hours apart", "30 mg weekly"], "The dose line: 30 mg single dose within 5d of unprotected intercourse.")
q(217, "DOC for emergency contraception in India is:", ["Levonorgestrel", "Ulipristal", "Mifepristone", "Ethinyl estradiol"], "The note: DOC for emergency contraception in India - levonorgestrel.")
q(217, "The levonorgestrel emergency contraception regimen is:", ["1.5 mg single dose within 72 h, or 0.75 mg two doses 12 h apart within 72 h", "30 mg single dose within 5 days", "1.5 mg daily for 5 days", "0.75 mg single dose within 120 h"], "The note: 1.5 mg single dose within 72h (or) 0.75 mg two doses 12h apart within 72h of unprotected intercourse.")

unit("5-Alpha Reductase Inhibitors", "Finasteride and dutasteride block conversion of testosterone to dihydrotestosterone (DHT). Uses: DOC for androgenic alopecia at 1 mg dose; in benign prostatic hyperplasia they reduce the size and weight of the prostate, improving outcome. The DOC for BPH overall, however, is tamsulosin or silodosin.")
q(217, "The MOA of 5-alpha reductase inhibitors is:", ["Blocking testosterone to dihydrotestosterone (DHT) conversion", "Blocking testosterone receptors", "Blocking aromatase", "Blocking LH release"], "The MOA line: testosterone blocked from becoming dihydrotestosterone (DHT).")
q(217, "The 5-alpha reductase inhibitors listed are:", ["Finasteride / dutasteride", "Flutamide / bicalutamide", "Exemestane / letrozole", "Tamsulosin / silodosin"], "The drugs line: finasteride / dutasteride.")
q(217, "Finasteride is DOC for androgenic alopecia at the dose of:", ["1 mg", "5 mg", "10 mg", "0.1 mg"], "The use line: DOC for androgenic alopecia (dose 1 mg).")
q(217, "In BPH, 5-alpha reductase inhibitors:", ["Reduce size & weight of prostate, improving outcome", "Only relax the prostatic smooth muscle", "Dissolve prostatic calculi", "Increase urine flow by CNS action"], "The BPH line: reduces size & weight of prostate, improving outcome.")
q(217, "The note stating the DOC for BPH names:", ["Tamsulosin / silodosin", "Finasteride / dutasteride", "Flutamide / bicalutamide", "Enzalutamide / apalutamide"], "The note: DOC for BPH - tamsulosin / silodosin.")

unit("Androgen Receptor Blockers", "Flutamide, bicalutamide, enzalutamide and apalutamide block androgen receptors. Uses: add-on drug for prostate cancer and hirsutism. Side effects are more frequent than with 5-alpha reductase inhibitors: gynecomastia and impotence.")
q(217, "The androgen receptor blockers listed are:", ["Flutamide, bicalutamide, enzalutamide, apalutamide", "Finasteride, dutasteride, minoxidil", "Letrozole, exemestane, anastrozole", "Tamsulosin, silodosin, alfuzosin"], "The drug list: flutamide, bicalutamide, enzalutamide, apalutamide.")
q(217, "Androgen receptor blockers are used as:", ["Add-on drug for prostate cancer", "First line monotherapy for BPH", "DOC for alopecia", "Emergency contraception"], "The use line: add-on drug for prostate cancer.")
q(217, "The second use of androgen receptor blockers is:", ["Hirsutism", "Alopecia", "Gynecomastia", "Infertility"], "The use list: hirsutism.")
q(217, "Side effects are more common with which drug class?", ["Androgen receptor blockers > 5-alpha reductase inhibitors", "5-alpha reductase inhibitors > androgen receptor blockers", "Aromatase inhibitors > AR blockers", "Both are equal"], "The note: seen in androgen receptor blockers > 5-alpha reductase inhibitors.")
q(217, "Side effects of androgen receptor blockers listed are:", ["Gynecomastia and impotence", "Osteoporosis and hot flashes", "Thrombosis and uterine carcinoma", "Dyspareunia and weight gain"], "The side-effect list: gynecomastia, impotence.")

unit("Aromatase Inhibitors", "In adipocytes of post-menopausal females, aromatase converts testosterone to estrogen; exemestane and letrozole block this step. Uses - DOC for post-menopausal ER-positive carcinoma breast and for anovulation due to PCOS. The DOC in gender change surgeries is leuprolide.")
q(217, "Aromatase inhibitors act in:", ["Adipocytes of post-menopausal females", "Testicular Sertoli cells", "Ovarian theca cells of premenopausal women", "Pituitary gonadotrophs"], "The MOA line: in adipocytes of post-menopausal females.")
q(217, "The reaction blocked by aromatase inhibitors is:", ["Testosterone to estrogen", "Testosterone to DHT", "Cholesterol to pregnenolone", "Estradiol to estrone"], "The flow: testosterone blocked (aromatase) from becoming estrogen.")
q(217, "The aromatase inhibitors listed are:", ["Exemestane and letrozole", "Finasteride and dutasteride", "Tamoxifen and raloxifene", "Goserelin and leuprolide"], "The drug list: exemestane, letrozole.")
q(217, "Aromatase inhibitors are DOC for:", ["Post-menopausal ER(+) Ca breast and anovulation D/t PCOS", "Premenopausal ER(+) Ca breast", "All cases of anovulation", "Prostate cancer"], "The use block: DOC for post-menopausal ER(+) Ca breast; anovulation D/t PCOS.")
q(217, "The DOC in gender change surgeries is:", ["Leuprolide", "Letrozole", "Flutamide", "Goserelin"], "The note: DOC in gender change surgeries - leuprolide.")

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
