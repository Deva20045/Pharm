#!/usr/bin/env python3
"""Force every exp to end with (Book p<q.page>) - matches work/validate.py."""
import json, re, sys
for p in sys.argv[1:]:
    d = json.load(open(p, encoding="utf-8")); n = 0
    for q in d["questions"]:
        want = f"(Book p{q['page']})"
        if not q["exp"].rstrip().endswith(want):
            q["exp"] = re.sub(r"\s*\(Book p.*\)$", "", q["exp"].rstrip()) + f" {want}"; n += 1
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{p}: fixed {n}")
