#!/usr/bin/env python3
"""Assemble paper/paper.md from paper/sections/*.md and append a reference list generated
from research/sources.csv (only sources actually cited). Also checks that every [S###]
tag resolves. Usage: python3 paper/build_paper.py"""
import csv, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sections = sorted((ROOT / "paper" / "sections").glob("*.md"))
body = "\n\n".join(p.read_text().rstrip() for p in sections)
src = {r["id"]: r for r in csv.DictReader(open(ROOT / "research" / "sources.csv"))}
cited = sorted(set(re.findall(r"\[(S\d{3})\]", body)))
missing = [c for c in cited if c not in src]
if missing:
    sys.exit(f"Unresolved citations: {missing}")
refs = ["\n\n# References\n",
        "Each entry gives the ID, title, publisher, publication date, URL, retrieval date, access method and confidence. "
        "Exact supporting passages, caveats and topics are in `research/sources.csv`.\n"]
for c in cited:
    r = src[c]
    refs.append(f"- **[{c}]** {r['title']}. {r['publisher']}. {r['pub_date']}. <{r['url']}> "
                f"(retrieved {r['retrieved']}; {r['access']}; confidence {r['confidence']})")
uncited = sorted(set(src) - set(cited))
refs.append(f"\n*{len(cited)} sources cited in the paper; {len(uncited)} further registered sources used for background: "
            f"{', '.join(uncited) if uncited else 'none'}.*")
out = body + "\n".join(refs) + "\n"
(ROOT / "paper" / "paper.md").write_text(out)
words = len(re.findall(r"\w+", body))
print(f"paper.md written: {words:,} words in body, {len(cited)} cited sources, uncited: {uncited}")
