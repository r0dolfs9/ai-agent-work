#!/usr/bin/env python3
"""How long to cover the WHOLE farming sector, Latvia vs EU, with the v2 pipeline? (2026-10-13)

Two directions are needed to find every place where Latvia differs or is stricter:
  A. EU -> LV: each EU farm obligation or option -> the Latvian rule that applies it -> same / stricter / different / missing.
  B. LV -> EU: each Latvian farming rule -> its EU basis, if any -> stricter than EU / purely national.

Evidence for the size (Calculation from sources):
  - 4,630 base Cabinet regulations and 1,783 base laws in force [S203].
  - Ministry of Agriculture (ZM) = 605 of 4,161 Cabinet regulations adopted Sept 2021 - Sept 2026 (14.5%); 137 of 1,075 new
    (non-amending) ones (12.7%); 92-166 per year by submission year [S206; data/results/10_*].
  - 54 core EU acts verified in force (pilot-scope-agriculture.md); EU agriculture chapter holds about 8,300 acts, mostly
    market and trade measures [S142].
Everything below the evidence is an ASSUMPTION; the proof of concept would measure it. "High" is a plausible bad case,
not every pessimistic value stacked at once.
Run: python3 feasibility/eu-lv-regulatory-comparison/sector_scope.py -> sector_scope_results.md
"""
import pathlib

OUT = pathlib.Path(__file__).resolve().parent
USD_PER_EUR, FEE = 1.1206, 0.055
PRICE = {"Gemini 3 Flash": (0.50, 3.00), "Claude Sonnet 5.5": (2.00, 10.00), "Claude Haiku 5.5": (0.10, 0.50),
         "GPT-5.5": (5.00, 30.00), "Claude Opus 5.5": (4.00, 20.00)}  # [S044][S045][S046]
CASES = ["low", "base", "high"]
A = {  # ASSUMPTIONS, low / base / high
    "eu_acts": [100, 150, 250],            # 54 core acts + delegated/implementing acts that set farm-level duties
    "eu_units_per_act": [15, 24, 32],      # articles that need a national comparison
    "lv_acts": [350, 500, 700],            # ZM share of 4,630 base regs (12.7-14.5% = 590-670), minus forestry/fisheries,
                                           # plus farm rules from other ministries (environment, labour, health) and laws
    "lv_units_per_act": [6, 10, 14],       # rule units (chapters / groups of points) per Latvian act
    "token_scale": [0.5, 1.0, 1.5],        # multiplier on the per-unit token budget below
    "reruns": [1.5, 2.0, 2.5],
    "flag_share": [0.10, 0.15, 0.20],      # units the checks or the verifier send to you
    "min_per_flag": [3, 5, 7],             # you: re-run, accept as "unsure", or fix the source
    "finding_share": [0.08, 0.12, 0.18],   # units that end up as a reported difference
    "min_per_finding": [2, 3, 4],          # you: read the one-page result before it goes into the PDF
    "audit_items": [200, 300, 400], "min_per_audit": [3, 4, 6],   # random sample re-checked (quotes, links, sense)
    "build_hours": [120, 160, 240],        # setup, both directions, model test (v2 weeks 1-8)
    "monitor_h_per_run_week": [5, 8, 12],  # watching runs, fixing country/source problems
    "units_per_hour": [100, 60, 40],       # machine throughput with 2 n8n workers and API rate limits
}
# Per unit (one EU article or one Latvian rule unit), base token budget (input, output) and model
STEPS = [("find", "Gemini 3 Flash", 80_000, 2_000, 1.0),
         ("compare", "Claude Sonnet 5.5", 30_000, 5_000, 1.0),
         ("check", "Claude Haiku 5.5", 10_000, 1_000, 1.0),
         ("verify flagged", "GPT-5.5", 30_000, 4_000, None),      # only the flag share
         ("final page", "Claude Opus 5.5", 20_000, 3_000, None)]  # only the finding share


def calc(i: int) -> dict:
    eu_units = A["eu_acts"][i] * A["eu_units_per_act"][i]
    lv_units = A["lv_acts"][i] * A["lv_units_per_act"][i]
    units = eu_units + lv_units
    usd = 0.0
    for name, model, tin, tout, share in STEPS:
        share = share if share is not None else (A["flag_share"][i] if name.startswith("verify") else A["finding_share"][i])
        p_in, p_out = PRICE[model]
        usd += units * share * (tin * p_in + tout * p_out) * A["token_scale"][i] / 1e6
    eur = usd * A["reruns"][i] * (1 + FEE) / USD_PER_EUR
    run_hours = units * A["reruns"][i] / A["units_per_hour"][i]
    run_weeks = run_hours / (24 * 5)                     # machine runs on weekdays, round the clock
    h = {
        "build and test": A["build_hours"][i],
        "handle flagged items": units * A["flag_share"][i] * A["min_per_flag"][i] / 60,
        "read findings": units * A["finding_share"][i] * A["min_per_finding"][i] / 60,
        "audit sample": A["audit_items"][i] * A["min_per_audit"][i] / 60,
        "watch runs, fix sources": max(run_weeks, 2) * A["monitor_h_per_run_week"][i],
    }
    hours = sum(h.values())
    return dict(eu_units=eu_units, lv_units=lv_units, units=units, eur=eur, run_hours=run_hours, h=h, hours=hours,
                wk_part=hours / 15, wk_full=hours / 35, findings=units * A["finding_share"][i], flags=units * A["flag_share"][i])


def main() -> None:
    R = [calc(i) for i in range(3)]
    L = ["# Whole farming sector, Latvia vs EU: size, time and AI cost\n",
         "Generated by `sector_scope.py` (2026-10-13). Evidence and assumptions are listed in the script.\n",
         "| | Low | Base | High |", "|---|---:|---:|---:|"]
    rows = [("EU acts in scope (ASSUMPTION)", lambda r, i: f"{A['eu_acts'][i]:,}"),
            ("Latvian acts in scope (estimate)", lambda r, i: f"{A['lv_acts'][i]:,}"),
            ("Units to check, EU to LV", lambda r, i: f"{r['eu_units']:,}"),
            ("Units to check, LV to EU", lambda r, i: f"{r['lv_units']:,}"),
            ("**Units total**", lambda r, i: f"**{r['units']:,}**"),
            ("Machine run time (hours, all passes)", lambda r, i: f"{r['run_hours']:,.0f}"),
            ("Items flagged to you", lambda r, i: f"{r['flags']:,.0f}"),
            ("Differences reported (estimate)", lambda r, i: f"{r['findings']:,.0f}"),
            ("AI usage, EUR", lambda r, i: f"{r['eur']:,.0f}")]
    for name, f in rows:
        L.append(f"| {name} | " + " | ".join(f(R[i], i) for i in range(3)) + " |")
    L.append("\n**Your hours**\n")
    L.append("| Task | Low | Base | High |\n|---|---:|---:|---:|")
    for k in R[0]["h"]:
        L.append(f"| {k} | " + " | ".join(f"{R[i]['h'][k]:,.0f}" for i in range(3)) + " |")
    L.append("| **Total hours** | " + " | ".join(f"**{R[i]['hours']:,.0f}**" for i in range(3)) + " |")
    L.append("| Weeks at 15 h/week (part-time) | " + " | ".join(f"{R[i]['wk_part']:,.0f}" for i in range(3)) + " |")
    L.append("| Weeks at 35 h/week (full-time) | " + " | ".join(f"{R[i]['wk_full']:,.0f}" for i in range(3)) + " |")
    (OUT / "sector_scope_results.md").write_text("\n".join(L) + "\n")
    for i, c in enumerate(CASES):
        r = R[i]
        print(c, "units", r["units"], "eur", round(r["eur"]), "hours", round(r["hours"]), "weeks part", round(r["wk_part"]),
              "full", round(r["wk_full"]), "run_h", round(r["run_hours"]), "findings", round(r["findings"]))


if __name__ == "__main__":
    main()
