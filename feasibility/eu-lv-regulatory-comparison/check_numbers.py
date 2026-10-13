#!/usr/bin/env python3
"""Check that the figures quoted in README.md match the model output and the query results.
Run: python3 -I feasibility/eu-lv-regulatory-comparison/check_numbers.py   (after cost_model.py and build_scope.py)
"""
import csv, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
readme = (HERE / "README.md").read_text(encoding="utf-8")
m = {r["metric"]: r for r in csv.DictReader(open(HERE / "cost_model_results.csv"))}
fails = 0


def expect(text: str, why: str) -> None:
    global fails
    ok = text in readme
    fails += not ok
    print(("OK  " if ok else "FAIL"), why, "->", repr(text))


def eur(x: str) -> str:
    return f"{float(x):,.0f}"


for case in ("low", "base", "high"):
    expect(eur(m["total"][case]), f"pilot total {case}")
    expect(eur(m["poc"][case]), f"proof of concept {case}")
    expect(eur(m["next_ind"][case]), f"second industry {case}")
    expect(eur(m["upkeep"][case]), f"upkeep {case}")
    expect(eur(m["cost_eur:LLM API"][case]), f"LLM {case}")
    expect(eur(m["legal_hours"][case]), f"legal hours {case}")
expect(f"€{float(m['total']['base'])/1000:,.0f},000 in the base case", "headline base total")
expect(f"about €{float(m['poc']['base'])/1000:,.0f},000 (€{float(m['poc']['low'])/1000:,.0f},000–€{float(m['poc']['high'])/1000:,.0f},000)", "headline PoC")
expect(f"€{float(m['manual_eur']['base'])/1000:,.0f},000 in the base case", "manual benchmark")
expect(f"{float(m['saving']['low']):.0%}–{float(m['saving']['high']):.0%} cheaper".replace("%–", "–"), "saving range")
expect(f"about {float(m['flags']['base']):,.0f} flagged findings", "flags base")
for case in ("low", "base", "high"):
    expect(f"**{eur(m['per_country'][case])}**", f"cost per added country {case}")
expect(f"about **€{round(float(m['per_country']['base']), -2):,.0f} per country** in the base case", "headline per country (rounded)")
expect(f"about €{round(3 * float(m['per_country']['base']), -2):,.0f} for 3 countries", "decision 3: three countries (rounded)")

# query results
dirs = list(csv.DictReader(open(HERE / "data/results/03_agri_directives_lv_nim_counts.csv", encoding="utf-8")))
with_lv = sum(1 for r in dirs if r["lv"] != "0")
expect(f"{with_lv} of {len(dirs)}", "directives with Latvian records")
expect(f"{sum(int(r['lv']) for r in dirs)} records in total", "total LV records")
expect(f"{len(dirs) - with_lv} of the {len(dirs)}", "directives without records")
by_type = list(csv.DictReader(open(HERE / "data/results/01_agri_chapter03_in_force_by_type.csv", encoding="utf-8")))
expect(f"({sum(int(r['n']) for r in by_type):,})".replace(",", ","), "chapter 03 total")
nitr = (HERE / "data/results/04_nitrates_directive_lv_nim.csv").read_text(encoding="utf-8")
expect(f"**{nitr.count('Likums Par piesārņojumu')} directives**", "one law against N directives")
pilot = list(csv.DictReader(open(HERE / "data/results/05_pilot_candidates.csv", encoding="utf-8")))
assert all(r["inforce"] == "1" for r in pilot)
expect(f"{len(pilot)} acts, all in force", "pilot candidates")
n_reg = sum(1 for r in pilot if r["celex"][5] == "R")
expect(f"The {n_reg} regulations in the core list", "regulations in core list")

# agent-stack plan figures == stack_costs_results.md
import re
plan = (HERE / "agent-stack-plan.md").read_text(encoding="utf-8")
res = (HERE / "stack_costs_results.md").read_text(encoding="utf-8")
res = res.split("## Where the money goes")[0] + res.split("## Cash budget")[1]  # skip the USD breakdown table
for line in res.splitlines():
    if line.startswith("| A.") or line.startswith("| B.") or line.startswith("| C.") or line.startswith("| D.") or line.startswith("| **Total**"):
        nums = re.findall(r"\*{0,2}([\d,]{3,})\*{0,2} \|", line)[-3:]
        for n in nums:
            ok = n in plan
            fails += not ok
            print(("OK  " if ok else "FAIL"), "plan figure", line.split("|")[1].strip()[:30], "->", n)
print("\nfailures:", fails)
sys.exit(1 if fails else 0)
