"""Consistency check for the agri-rules package (no network).

1. Every [S##] cited in a .md file exists in evidence/sources.csv.
2. Every relative Markdown link points to an existing file.
3. Key figures quoted in the documents equal the model outputs.
4. rules/rule-list.csv has 100 unique IDs, ranks 1..100 and 20 pilot rows.
Exit code 1 on any failure.
"""
import csv
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "models"))
import cost_model  # noqa: E402
import country_score  # noqa: E402

fail = []
md = {p: p.read_text(encoding="utf-8") for p in ROOT.rglob("*.md")}

# 1. source IDs
ids = {r["id"] for r in csv.DictReader(open(ROOT / "evidence/sources.csv", encoding="utf-8"))}
for p, t in md.items():
    for m in re.finditer(r"S(\d{2})(?:[–-]S?(\d{2}))?", t):
        lo = int(m.group(1))
        hi = int(m.group(2)) if m.group(2) else lo
        if not re.search(r"\[[^\]]*" + re.escape(m.group(0)), t[max(0, m.start() - 40):m.end() + 1]):
            continue  # only bracketed citations
        for n in range(lo, hi + 1):
            if f"S{n:02d}" not in ids:
                fail.append(f"{p.name}: unknown source S{n:02d}")

# 2. relative links
for p, t in md.items():
    for m in re.finditer(r"\]\(([^)#]+?)(?:#[^)]*)?\)", t):
        target = m.group(1)
        if target.startswith(("http", "mailto")):
            continue
        if not (p.parent / target).exists():
            fail.append(f"{p.name}: broken link {target}")

# 3. figures
full = {k: round(cost_model.run_cost_eur(100, 10, sc)["eur_ex_vat"]) for k, sc in cost_model.SCENARIOS.items()}
pilot = {k: round(cost_model.run_cost_eur(20, 10, sc)["eur_ex_vat"] * 3) for k, sc in cost_model.SCENARIOS.items()}
expect = {
    "07-cost-timeline.md": [f"€{full['low']:,}", f"€{full['base']:,}", f"€{full['high']:,}",
                            f"€{pilot['low']:,}", f"€{pilot['base']:,}", f"€{pilot['high']:,}"],
    "00-START-HERE.md": [f"**€{full['base']:,}**", "79.0", "78.0"],
    "03-source-matrix.md": [f"{country_score.total('Italy'):.1f}", f"{country_score.total('Denmark'):.1f}"],
}
for name, needles in expect.items():
    t = (ROOT / name).read_text(encoding="utf-8")
    for n in needles:
        if n not in t:
            fail.append(f"{name}: expected figure {n!r} not found")

# 4. rule list
rows = list(csv.DictReader(open(ROOT / "rules/rule-list.csv", encoding="utf-8")))
if len(rows) != 100 or len({r["rule_id"] for r in rows}) != 100:
    fail.append("rule-list: not 100 unique rules")
if sorted(int(r["rank"]) for r in rows) != list(range(1, 101)):
    fail.append("rule-list: ranks are not 1..100")
if sum(r["pilot"] == "Y" for r in rows) != 20:
    fail.append("rule-list: pilot count != 20")

print(f"Checked {len(md)} Markdown files, {len(ids)} sources, {len(rows)} rules.")
print(f"Model figures: full pass {full}, pilot (3 pipelines) {pilot}")
if fail:
    print("FAILURES:\n- " + "\n- ".join(fail))
    sys.exit(1)
print("All checks passed.")
