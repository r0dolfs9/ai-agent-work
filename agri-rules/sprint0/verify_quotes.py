"""Deterministic check: each quote must appear verbatim (whitespace-normalised only) in its saved snapshot text."""
import json, re, sys, hashlib, csv, pathlib
sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(__file__).parent
norm = lambda s: re.sub(r"\s+", " ", s).strip()
log = {r[1]: r for r in csv.reader(open(W / "fetch-log.csv", encoding="utf-8"))}
cells = json.load(open(W / "cells.json", encoding="utf-8"))["cells"]
res = []
for c in cells:
    if not c["snapshot"]:
        res.append((c["cell"], "NO SOURCE", "")); continue
    raw = (W / "snap" / f"{c['snapshot']}.raw").read_bytes()
    h = hashlib.sha256(raw).hexdigest()
    logged = log.get(c["snapshot"], [None] * 5)[4]
    txt = norm((W / "snap" / f"{c['snapshot']}.txt").read_text(encoding="utf-8"))
    ok = norm(c["quote"]) in txt
    res.append((c["cell"], "PASS" if ok else "FAIL", ("hash ok" if h == logged else "HASH MISMATCH") + f" {h[:12]}"))
for r in res: print(" | ".join(r))
print("PASS", sum(r[1] == "PASS" for r in res), "FAIL", sum(r[1] == "FAIL" for r in res), "NO SOURCE", sum(r[1] == "NO SOURCE" for r in res))
json.dump([dict(cell=a, check=b, hash=c) for a, b, c in res], open(W / "verify_results.json", "w", encoding="utf-8"), indent=1)
