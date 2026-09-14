#!/usr/bin/env python3
"""Patch a gen_chNN.py unit-range table: recompute [a,b] from the q() call order."""
import re, sys
p = sys.argv[1]
src = open(p).read()
lines = [l for l in src.split("\n") if l.startswith("q(")]
rng, secs = {}, []
for i, l in enumerate(lines, 1):
    s = re.match(r'q\((\w+),', l).group(1)
    if s not in rng:
        secs.append(s); rng[s] = [i, i]
    rng[s][1] = i
# find the UNITS block and rewrite each tuple's range
start = src.index("UNITS = [")
def fix(m):
    n = int(m.group(1))
    s = secs[n-1]
    return f" ({n}, {m.group(2)}, [{rng[s][0]},{rng[s][1]}]"
src = src[:start] + re.sub(r' \((\d+), ("(?:[^"\\]|\\.)*"), \[[0-9]+, ?[0-9]+\]', fix, src[start:])
open(p, "w").write(src)
print({k: v for k, v in rng.items()}, "sections:", len(secs))
