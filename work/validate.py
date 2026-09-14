#!/usr/bin/env python3
"""Validator for PULSE Pharm chapter data files.

Schema (must match exactly):
- Question: {id:"PHARM-C{ch}-{nnn}" sequential per chapter from 001, sec, page(book),
             q, opts[4], ans(idx 0-3), exp ends "(Book pX)"}
- Unit: {id:"PHARM-U{ch}-{n}" sequential per chapter from 1, ch, n, title,
         sec:"<Heading> · p<page>", qs:[ids contiguous & ordered],
         guide: vivid 2-3 sentence prose}
- Units must cover every question exactly once, in order.

Usage: python3 work/validate.py data/chNN.json [more.json ...]
"""
import json, re, sys

PAGE_MAP = {  # book start-end pages per chapter (from TOC; ch end = next ch start - 1)
     1: (1, 1),    2: (2, 4),    3: (5, 8),    4: (9, 10),   5: (11, 14),
     6: (15, 17),  7: (18, 19),  8: (20, 24),  9: (25, 28), 10: (29, 32),
    11: (33, 36), 12: (37, 41), 13: (42, 47), 14: (48, 51), 15: (52, 55),
    16: (56, 57), 17: (58, 62), 18: (63, 68), 19: (69, 73), 20: (74, 76),
    21: (77, 82), 22: (83, 88), 23: (89, 90), 24: (91, 93), 25: (94, 100),
    26: (101, 105), 27: (106, 112), 28: (113, 117), 29: (118, 119), 30: (120, 122),
    31: (123, 126), 32: (127, 130), 33: (131, 133), 34: (134, 140), 35: (141, 144),
    36: (145, 149), 37: (150, 152), 38: (153, 154), 39: (155, 158), 40: (159, 163),
    41: (164, 166), 42: (167, 170), 43: (171, 173), 44: (174, 179), 45: (180, 183),
    46: (184, 188), 47: (189, 192), 48: (193, 198), 49: (199, 204), 50: (205, 206),
    51: (207, 210), 52: (211, 214), 53: (215, 217), 54: (218, 220), 55: (221, 223),
    56: (224, 226), 57: (227, 229), 58: (230, 232), 59: (233, 236), 60: (237, 241),
    61: (242, 243), 62: (244, 246), 63: (247, 250), 64: (251, 255), 65: (256, 258),
    66: (259, 260), 67: (261, 265), 68: (266, 268), 69: (269, 271), 70: (272, 275),
    71: (276, 281), 72: (282, 285), 73: (286, 289), 74: (290, 293),
}

def fail(msg):
    print("  FAIL:", msg)
    sys.exit(1)

def validate(path):
    print(f"== {path}")
    d = json.load(open(path, encoding="utf-8"))
    qs, units = d["questions"], d["units"]
    if not qs:
        fail("no questions")
    m = re.match(r"PHARM-C(\d+)-(\d+)", qs[0]["id"])
    ch = int(m.group(1))
    lo, hi = PAGE_MAP.get(ch, (1, 293))

    # ---- questions ----
    for i, q in enumerate(qs, 1):
        if q["id"] != f"PHARM-C{ch}-{i:03d}":
            fail(f"question order/id: got {q['id']} expected PHARM-C{ch}-{i:03d}")
        if len(q["opts"]) != 4:
            fail(f"{q['id']}: opts != 4")
        if not (isinstance(q["ans"], int) and 0 <= q["ans"] <= 3):
            fail(f"{q['id']}: bad ans")
        if not (lo <= q["page"] <= hi):
            fail(f"{q['id']}: page {q['page']} outside chapter range {lo}-{hi}")
        if not q["exp"].rstrip().endswith(f"(Book p{q['page']})"):
            fail(f"{q['id']}: exp must end '(Book p{q['page']})' -> ...{q['exp'][-20:]}")
        if not q["q"].strip() or any(not str(o).strip() for o in q["opts"]):
            fail(f"{q['id']}: empty text")
        if len(set(q["opts"])) != 4:
            fail(f"{q['id']}: duplicate options")
        if not q["sec"].strip():
            fail(f"{q['id']}: empty sec")
    print(f"  questions OK: {len(qs)} (C{ch}-001 .. C{ch}-{len(qs):03d})")

    # ---- units ----
    covered = []
    for i, u in enumerate(units, 1):
        if u["id"] != f"PHARM-U{ch}-{i}":
            fail(f"unit order/id: got {u['id']} expected PHARM-U{ch}-{i}")
        if u["ch"] != ch or u["n"] != i:
            fail(f"{u['id']}: ch/n mismatch")
        if not re.match(r".+ · p\d+$", u["sec"]):
            fail(f"{u['id']}: sec format '{u['sec']}'")
        if not u["qs"] or not u["guide"].strip():
            fail(f"{u['id']}: empty qs/guide")
        covered += u["qs"]
    # units cover every question exactly once, in order
    if covered != [q["id"] for q in qs]:
        want, got = set(q["id"] for q in qs), set(covered)
        missing = [x for x in (q["id"] for q in qs) if x not in got]
        dupes = [x for x in covered if covered.count(x) > 1]
        extra = [x for x in covered if x not in want]
        fail(f"coverage mismatch. missing={missing[:5]} dupes={sorted(set(dupes))[:5]} extra={extra[:5]}")
    print(f"  units OK: {len(units)} cover all {len(qs)} questions in order")
    print(f"  PASS ✓  ({path})")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    for p in sys.argv[1:]:
        validate(p)
