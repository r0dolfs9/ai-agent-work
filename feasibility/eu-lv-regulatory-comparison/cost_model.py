#!/usr/bin/env python3
"""Cost, effort and certainty model: AI-assisted EU-vs-Latvia rule comparison, pilot industry = agriculture (2026-10-13).

What it models (low / base / high):
  1. Setup and pilot cost: engineering build, legal-expert work (taxonomy, gold set, review of findings,
     recall audit, sweep for purely national rules), project management, hosting, and LLM API spend.
  2. A fully manual comparison of the same scope, as a benchmark.
  3. Monthly upkeep after the pilot (re-checking provisions that changed).
  4. Optional: comparing Latvia with other EU countries on rules the EU leaves to each country (parameter matrix).
  5. How sure we can be: the statistical bounds that review samples of a given size support.

Every number is a dated source [S###] or an explicit ASSUMPTION. Nothing here has been measured on this task;
the pilot's proof-of-concept phase exists to replace these assumptions with observed figures.

Run: python3 feasibility/eu-lv-regulatory-comparison/cost_model.py  -> cost_model_results.md / .csv (same folder)
"""
from __future__ import annotations
import csv, math, pathlib
from dataclasses import dataclass

OUT = pathlib.Path(__file__).resolve().parent
USD_PER_EUR = 1.1206   # ECB reference rate 2026-10-09, as used in models/operator_economics.py
BATCH_DISCOUNT = 0.50  # S044: Message Batches API bills at 50%
POC_ACTS = 10          # ASSUMPTION: proof of concept on 3 sub-domains (nutrients, plant protection, farm-animal welfare), ~10 EU acts

# ---------------------------------------------------------------- dated prices, USD per million tokens [S044]
PRICE = {
    #              input  cache_read  output
    "opus-5.5":   (4.00,  0.20,       20.00),
    "sonnet-5.5": (2.00,  0.10,       10.00),
    "haiku-5.5":  (0.10,  0.01,        0.50),   # prompts <=100k tokens
}


@dataclass(frozen=True)
class Case:
    # --- scope (ASSUMPTION; 49 candidate core acts were verified in force on 2026-10-13, see data/results/05_*)
    eu_acts: int              # base EU acts in the pilot slice
    arts_per_act: float       # average articles per act (annexes counted as articles)
    relevant_share: float     # share of articles that need a national comparison (rest: Commission powers, comitology, recitals-like)
    # --- tokens per step (ASSUMPTION; measure in proof of concept with response.usage)
    triage_in: float; triage_out: float          # haiku: is this article relevant to national law?
    options_in: float; options_out: float        # sonnet: extract "Member States may/shall" options from regulations
    compare_in: float; compare_out: float        # opus: EU article (LV-language version) + candidate LV provisions -> finding
    cached_share: float                          # share of compare/verify input that is a stable cached prefix (instructions, taxonomy)
    verify_in: float; verify_out: float          # opus, independent adversarial pass
    synth_in: float; synth_out: float            # opus, per act: cluster findings, build the "connections" list
    gold_items: int           # gold-standard EU provisions annotated by the expert
    gold_runs: int            # prompt/pipeline iterations scored against the gold set
    full_runs: float          # complete passes over the scope (first run + reruns after fixes)
    use_batch: bool           # run full passes through the Batch API
    # --- people (ASSUMPTION: rates are Latvian contractor-market guesses; see README section 5 for the evidence)
    dev_days: float; dev_rate: float             # engineering build, EUR/hour
    legal_rate: float                            # EUR/hour for the Latvian agri / EU-law reviewer
    taxonomy_days: float                         # scope sign-off, difference taxonomy, review guide
    gold_h_per_item: float
    flag_share: float                            # share of relevant provisions the pipeline flags as a difference or "unsure"
    review_h_per_flag: float
    audit_items: int                             # random sample of "no difference" results re-checked by the expert
    audit_h_per_item: float
    national_sweep_days: float                   # finding purely national rules with no EU counterpart (D9)
    pm_share: float                              # project management / QA, as share of all human hours
    pm_rate: float
    hosting_pm: float; months: float             # storage, search index, review UI hosting (EUR / month), pilot months
    # --- manual benchmark (ASSUMPTION)
    manual_h_per_relevant: float                 # find LV counterpart + compare + write up, per relevant EU provision
    # --- upkeep after the pilot (ASSUMPTION)
    changed_per_month: float                     # EU or LV provisions in scope changed per month
    upkeep_dev_days_pm: float


CASES = {
    "low":  Case(40, 50, 0.40, 2_000, 200, 3_000, 500, 15_000, 3_000, 0.30, 15_000, 2_000, 60_000, 6_000,
                 150, 8, 1.5, True,
                 20, 45, 60, 3, 0.33, 0.25, 0.25, 150, 0.15, 3, 0.10, 45, 20, 3.0,
                 0.75, 30, 1),
    "base": Case(50, 60, 0.50, 2_000, 200, 3_000, 500, 20_000, 5_000, 0.25, 20_000, 3_000, 80_000, 8_000,
                 200, 12, 2.0, True,
                 35, 60, 90, 5, 0.50, 0.35, 0.40, 200, 0.20, 5, 0.15, 60, 50, 4.0,
                 1.00, 60, 2),
    "high": Case(70, 75, 0.60, 3_000, 300, 4_000, 800, 30_000, 8_000, 0.20, 30_000, 5_000, 120_000, 12_000,
                 300, 20, 3.0, False,
                 60, 85, 150, 8, 0.75, 0.45, 0.60, 300, 0.30, 10, 0.20, 85, 150, 6.0,
                 1.50, 120, 4),
}


# ---------------------------------------------------------------- optional: Latvia vs other Member States (ASSUMPTION)
# Not EU-vs-LV but LV-vs-country X, for rules the EU leaves to each country (e.g. overtime pay rates [S165]-[S172]).
# Designed as a "parameter matrix": a fixed list of key rules/numbers for the industry, one cell per country.
#   params: rules in the matrix; h_per_cell: reviewer time to check one AI-extracted cell against that country's
#   official text; dev_days: adding one country's legal portal; tokens per cell: search + extraction (Opus 5.5).
COMPARE = {
    "low":  dict(params=40,  h_per_cell=10 / 60, dev_days=1, cell_in=20_000, cell_out=2_000, runs=1.5),
    "base": dict(params=80,  h_per_cell=15 / 60, dev_days=2, cell_in=30_000, cell_out=3_000, runs=2.0),
    "high": dict(params=150, h_per_cell=25 / 60, dev_days=4, cell_in=50_000, cell_out=5_000, runs=3.0),
}


def per_country(k: str) -> dict:
    c, x = CASES[k], COMPARE[k]
    review_h = x["params"] * x["h_per_cell"]
    dev_h = x["dev_days"] * 8
    llm = x["params"] * usd("opus-5.5", x["cell_in"], x["cell_out"]) * x["runs"] / USD_PER_EUR
    eur = review_h * c.legal_rate + dev_h * c.dev_rate + (review_h + dev_h) * c.pm_share * c.pm_rate + llm
    return dict(review_h=review_h, dev_h=dev_h, llm=llm, eur=eur)


def usd(model: str, tin: float, tout: float, cached: float = 0.0) -> float:
    p_in, p_cache, p_out = PRICE[model]
    return ((tin * (1 - cached)) * p_in + tin * cached * p_cache + tout * p_out) / 1e6


def run(c: Case) -> dict:
    arts = c.eu_acts * c.arts_per_act
    rel = arts * c.relevant_share
    # one complete pass, USD
    per_pass = {
        "triage (Haiku 5.5)": arts * usd("haiku-5.5", c.triage_in, c.triage_out),
        "options scan (Sonnet 5.5)": arts * usd("sonnet-5.5", c.options_in, c.options_out),
        "compare (Opus 5.5)": rel * usd("opus-5.5", c.compare_in, c.compare_out, c.cached_share),
        "verify (Opus 5.5)": rel * usd("opus-5.5", c.verify_in, c.verify_out, c.cached_share),
        "synthesis (Opus 5.5)": c.eu_acts * usd("opus-5.5", c.synth_in, c.synth_out),
    }
    pass_usd = sum(per_pass.values())
    full_usd = pass_usd * c.full_runs * (1 - BATCH_DISCOUNT if c.use_batch else 1)
    per_item = per_pass["compare (Opus 5.5)"] / rel + per_pass["verify (Opus 5.5)"] / rel
    gold_usd = c.gold_items * per_item * c.gold_runs           # interactive (no batch) during development
    llm_eur = (full_usd + gold_usd) / USD_PER_EUR

    flags = rel * c.flag_share
    legal_h = {
        "taxonomy, scope, review guide": c.taxonomy_days * 8,
        "gold-standard set": c.gold_items * c.gold_h_per_item,
        "review of every flagged finding": flags * c.review_h_per_flag,
        "recall audit (random no-difference sample)": c.audit_items * c.audit_h_per_item,
        "sweep for purely national rules": c.national_sweep_days * 8,
    }
    legal_hours = sum(legal_h.values())
    dev_hours = c.dev_days * 8
    pm_hours = (legal_hours + dev_hours) * c.pm_share
    cost = {
        "engineering build": dev_hours * c.dev_rate,
        "legal expert": legal_hours * c.legal_rate,
        "project management / QA": pm_hours * c.pm_rate,
        "hosting and tools": c.hosting_pm * c.months,
        "LLM API": llm_eur,
    }
    total = sum(cost.values())
    manual_h = rel * c.manual_h_per_relevant + c.taxonomy_days * 8 + c.national_sweep_days * 8
    manual_eur = manual_h * c.legal_rate * (1 + c.pm_share)

    upkeep_llm = c.changed_per_month * per_item * 3 / USD_PER_EUR      # x3: re-map neighbours of each changed provision
    # x1.5: a changed provision is more likely than average to create a difference; +4 h: monthly sign-off of the register
    upkeep_legal_h = c.changed_per_month * c.flag_share * c.review_h_per_flag * 1.5 + 4
    upkeep = upkeep_llm + upkeep_legal_h * c.legal_rate + c.upkeep_dev_days_pm * 8 * c.dev_rate + c.hosting_pm

    # proof of concept: 3 sub-domains, POC_ACTS acts; half the build; full taxonomy and gold set; review of PoC flags only
    poc_share = POC_ACTS / c.eu_acts
    poc_legal_h = legal_h["taxonomy, scope, review guide"] + legal_h["gold-standard set"] + legal_h["review of every flagged finding"] * poc_share
    poc_dev_h = dev_hours * 0.5
    poc = ((poc_dev_h * c.dev_rate) + poc_legal_h * c.legal_rate + (poc_dev_h + poc_legal_h) * c.pm_share * c.pm_rate
           + c.hosting_pm * 1.5 + gold_usd / USD_PER_EUR + full_usd * poc_share / USD_PER_EUR)
    # a second industry of similar size: 30% of the build (adapters, new sources), half the taxonomy work, everything else again
    next_ind = (0.3 * dev_hours * c.dev_rate + (legal_hours - 0.5 * legal_h["taxonomy, scope, review guide"]) * c.legal_rate
                + (0.3 * dev_hours + legal_hours) * c.pm_share * c.pm_rate + c.hosting_pm * c.months + llm_eur)
    return dict(arts=arts, rel=rel, flags=flags, poc=poc, poc_legal_h=poc_legal_h, poc_dev_h=poc_dev_h,
                per_pass=per_pass, pass_usd=pass_usd, full_usd=full_usd, gold_usd=gold_usd, llm_eur=llm_eur, legal_h=legal_h, legal_hours=legal_hours, dev_hours=dev_hours,
                pm_hours=pm_hours, cost=cost, total=total, manual_h=manual_h, manual_eur=manual_eur,
                next_ind=next_ind, upkeep=upkeep, upkeep_llm=upkeep_llm, upkeep_legal_h=upkeep_legal_h,
                human_share=(cost["engineering build"] + cost["legal expert"] + cost["project management / QA"]) / total,
                legal_share=cost["legal expert"] / total)


# ---------------------------------------------------------------- certainty: what review samples can support
def zero_miss_upper(n: int, conf: float = 0.95) -> float:
    """Exact (Clopper-Pearson) one-sided upper bound on a rate when 0 events are seen in n checks."""
    return 1 - (1 - conf) ** (1 / n)


def wilson(p: float, n: int, z: float = 1.96) -> tuple[float, float]:
    d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return centre - half, centre + half


def fmt(x: float) -> str:
    return f"{x:,.0f}"


def main() -> None:
    R = {k: run(c) for k, c in CASES.items()}
    L = []
    w = L.append
    w("# Cost, effort and certainty model: results\n")
    w("Generated by `cost_model.py` (2026-10-13). EUR unless stated; USD converted at 1.1206 USD/EUR (ECB, 2026-10-09). "
      "LLM prices [S044]. **Every input except prices is an ASSUMPTION** (see the script); nothing has been measured on this task yet.\n")
    w("## 1. Pilot (agriculture) total, low / base / high\n")
    w("| Item | Low | Base | High |\n|---|---:|---:|---:|")
    for k in ["engineering build", "legal expert", "project management / QA", "hosting and tools", "LLM API"]:
        w(f"| {k} | {fmt(R['low']['cost'][k])} | {fmt(R['base']['cost'][k])} | {fmt(R['high']['cost'][k])} |")
    w(f"| **Total pilot cost** | **{fmt(R['low']['total'])}** | **{fmt(R['base']['total'])}** | **{fmt(R['high']['total'])}** |")
    w(f"| Share spent on people (build, review, PM) | {R['low']['human_share']:.0%} | {R['base']['human_share']:.0%} | {R['high']['human_share']:.0%} |")
    w(f"| of which legal expert | {R['low']['legal_share']:.0%} | {R['base']['legal_share']:.0%} | {R['high']['legal_share']:.0%} |")
    w(f"| LLM API as share of total | {R['low']['cost']['LLM API']/R['low']['total']:.1%} | {R['base']['cost']['LLM API']/R['base']['total']:.1%} | {R['high']['cost']['LLM API']/R['high']['total']:.1%} |\n")

    w("**Proof of concept first** (3 sub-domains, about 10 EU acts; half the build, the full taxonomy and gold set, review of the PoC findings):\n")
    w("| | Low | Base | High |\n|---|---:|---:|---:|")
    w(f"| Proof-of-concept cost, EUR | {fmt(R['low']['poc'])} | {fmt(R['base']['poc'])} | {fmt(R['high']['poc'])} |")
    w(f"| of which legal-expert hours | {fmt(R['low']['poc_legal_h'])} | {fmt(R['base']['poc_legal_h'])} | {fmt(R['high']['poc_legal_h'])} |")
    w(f"| of which engineering hours | {fmt(R['low']['poc_dev_h'])} | {fmt(R['base']['poc_dev_h'])} | {fmt(R['high']['poc_dev_h'])} |")
    w(f"| Second industry of similar size (build mostly reused) | {fmt(R['low']['next_ind'])} | {fmt(R['base']['next_ind'])} | {fmt(R['high']['next_ind'])} |\n")
    w("## 2. Scope and effort\n")
    w("| Quantity | Low | Base | High |\n|---|---:|---:|---:|")
    rows = [("EU acts in pilot slice", lambda r, c: c.eu_acts), ("EU articles (incl. annexes)", lambda r, c: r["arts"]),
            ("articles needing a national comparison", lambda r, c: r["rel"]), ("findings flagged for expert review", lambda r, c: r["flags"]),
            ("engineering hours", lambda r, c: r["dev_hours"]), ("legal-expert hours", lambda r, c: r["legal_hours"]),
            ("PM / QA hours", lambda r, c: r["pm_hours"])]
    for name, f in rows:
        w(f"| {name} | {fmt(f(R['low'], CASES['low']))} | {fmt(f(R['base'], CASES['base']))} | {fmt(f(R['high'], CASES['high']))} |")
    w("")
    w("Legal-expert hours by task:\n")
    w("| Task | Low | Base | High |\n|---|---:|---:|---:|")
    for k in R["base"]["legal_h"]:
        w(f"| {k} | {fmt(R['low']['legal_h'][k])} | {fmt(R['base']['legal_h'][k])} | {fmt(R['high']['legal_h'][k])} |")
    w("")

    w("## 3. LLM API detail (USD)\n")
    w("| Step, one complete pass | Low | Base | High |\n|---|---:|---:|---:|")
    for k in R["base"]["per_pass"]:
        w(f"| {k} | {R['low']['per_pass'][k]:,.0f} | {R['base']['per_pass'][k]:,.0f} | {R['high']['per_pass'][k]:,.0f} |")
    w(f"| **One complete pass** | {R['low']['pass_usd']:,.0f} | {R['base']['pass_usd']:,.0f} | {R['high']['pass_usd']:,.0f} |")
    w(f"| All full passes (batch discount: low/base yes, high no) | {R['low']['full_usd']:,.0f} | {R['base']['full_usd']:,.0f} | {R['high']['full_usd']:,.0f} |")
    w(f"| Gold-set development runs (interactive) | {R['low']['gold_usd']:,.0f} | {R['base']['gold_usd']:,.0f} | {R['high']['gold_usd']:,.0f} |")
    w(f"| **Total LLM, EUR** | {R['low']['llm_eur']:,.0f} | {R['base']['llm_eur']:,.0f} | {R['high']['llm_eur']:,.0f} |\n")
    w("Even a 3x token overrun on the base case would add about "
      f"€{R['base']['llm_eur']*2:,.0f}, small next to the people costs.\n")

    w("## 4. Benchmark: the same scope done fully by hand\n")
    w("| | Low | Base | High |\n|---|---:|---:|---:|")
    w(f"| Manual expert hours | {fmt(R['low']['manual_h'])} | {fmt(R['base']['manual_h'])} | {fmt(R['high']['manual_h'])} |")
    w(f"| Manual cost (expert rate + PM share) | {fmt(R['low']['manual_eur'])} | {fmt(R['base']['manual_eur'])} | {fmt(R['high']['manual_eur'])} |")
    w(f"| AI-assisted pilot cost (section 1) | {fmt(R['low']['total'])} | {fmt(R['base']['total'])} | {fmt(R['high']['total'])} |")
    for k in ["low", "base", "high"]:
        R[k]["saving"] = 1 - R[k]["total"] / R[k]["manual_eur"]
    w(f"| Saving vs manual | {R['low']['saving']:.0%} | {R['base']['saving']:.0%} | {R['high']['saving']:.0%} |\n")
    w("The manual benchmark also assumes an expert, so the saving comes from less searching and drafting, not from removing review. "
      "The AI-assisted case includes one-off build costs, which a second industry would mostly reuse.\n")

    w("## 5. Monthly upkeep after the pilot\n")
    w("| | Low | Base | High |\n|---|---:|---:|---:|")
    w(f"| Changed provisions per month (ASSUMPTION) | {CASES['low'].changed_per_month:.0f} | {CASES['base'].changed_per_month:.0f} | {CASES['high'].changed_per_month:.0f} |")
    w(f"| LLM re-check, EUR | {R['low']['upkeep_llm']:,.0f} | {R['base']['upkeep_llm']:,.0f} | {R['high']['upkeep_llm']:,.0f} |")
    w(f"| Expert hours | {R['low']['upkeep_legal_h']:,.0f} | {R['base']['upkeep_legal_h']:,.0f} | {R['high']['upkeep_legal_h']:,.0f} |")
    w(f"| **Total per month, EUR** | {fmt(R['low']['upkeep'])} | {fmt(R['base']['upkeep'])} | {fmt(R['high']['upkeep'])} |\n")

    w("## 6. Optional: compare Latvia with other EU countries (parameter matrix)\n")
    w("For rules the EU leaves to each country (for example, overtime pay rates), the comparison is Latvia against other "
      "countries, not against EU law. Modelled as a fixed list of key rules per industry, one cell per country, each cell "
      "AI-extracted from that country's official text and checked by a reviewer who reads its language. ASSUMPTIONS in `COMPARE`.\n")
    w("| | Low | Base | High |\n|---|---:|---:|---:|")
    PC = {k: per_country(k) for k in CASES}
    w(f"| Rules in the matrix | {COMPARE['low']['params']} | {COMPARE['base']['params']} | {COMPARE['high']['params']} |")
    w(f"| Reviewer minutes per cell | {COMPARE['low']['h_per_cell']*60:.0f} | {COMPARE['base']['h_per_cell']*60:.0f} | {COMPARE['high']['h_per_cell']*60:.0f} |")
    w(f"| Reviewer hours per country | {PC['low']['review_h']:,.0f} | {PC['base']['review_h']:,.0f} | {PC['high']['review_h']:,.0f} |")
    w(f"| AI usage per country, EUR | {PC['low']['llm']:,.0f} | {PC['base']['llm']:,.0f} | {PC['high']['llm']:,.0f} |")
    w(f"| **Cost per added country, EUR** | **{fmt(PC['low']['eur'])}** | **{fmt(PC['base']['eur'])}** | **{fmt(PC['high']['eur'])}** |")
    for n in (3, 8, 26):
        w(f"| {n} countries | {fmt(PC['low']['eur']*n)} | {fmt(PC['base']['eur']*n)} | {fmt(PC['high']['eur']*n)} |")
    w("\nThe hard part is not money but finding a reviewer for each country's law and language. A cheaper first pass can use "
      "EU-level comparative sources, with country experts only for disputed cells. A full EU-law comparison for another country "
      "(not just a matrix) would cost about as much as a new pilot (section 1).\n")
    for k in CASES:
        R[k]["per_country"] = PC[k]["eur"]
    w("## 7. How sure can we be? What review samples support\n")
    w("**A. Missed differences.** The expert re-checks a random sample of items the system marked \"no difference\". "
      "If none turn out to be a missed difference, the true miss rate is below the bound shown, with 95% confidence "
      "(exact one-sided bound; the 'rule of three' gives about 3/n).\n")
    w("| Items re-checked, 0 misses found | 95% upper bound on miss rate |\n|---:|---:|")
    for n in (50, 100, 150, 200, 300, 500):
        w(f"| {n} | {zero_miss_upper(n):.1%} |")
    w("")
    w("**B. Recall on the gold set.** If the system finds 90% of the known differences in the gold set, the true recall lies in this "
      "95% interval (Wilson). Small gold sets give wide intervals, which is why the gold set needs enough real differences.\n")
    w("| Known differences in gold set | Observed recall | 95% interval |\n|---:|---:|---|")
    for n in (20, 40, 60, 100, 200):
        lo, hi = wilson(0.90, n)
        w(f"| {n} | 90% | {lo:.0%} – {hi:.0%} |")
    w("")
    w("**C. Reviewer agreement.** Classification (for example, is this rule *stricter*, or just *different*?) is a judgement call. "
      "A second reviewer should label a subset of about 50–100 findings blind, so that agreement can be reported (for example, Cohen's kappa).\n")
    (OUT / "cost_model_results.md").write_text("\n".join(L) + "\n")

    with open(OUT / "cost_model_results.csv", "w", newline="") as f:
        cw = csv.writer(f)
        cw.writerow(["metric", "low", "base", "high"])
        for k in ["engineering build", "legal expert", "project management / QA", "hosting and tools", "LLM API"]:
            cw.writerow([f"cost_eur:{k}"] + [round(R[c]["cost"][k], 2) for c in CASES])
        for m in ["total", "poc", "next_ind", "per_country", "manual_eur", "upkeep", "llm_eur", "legal_hours", "dev_hours", "pm_hours", "arts", "rel", "flags", "saving"]:
            cw.writerow([m] + [round(R[c][m], 4) for c in CASES])
    print("wrote", OUT / "cost_model_results.md")
    for k in CASES:
        print(k, "total", fmt(R[k]["total"]), "poc", fmt(R[k]["poc"]), "next", fmt(R[k]["next_ind"]), "manual", fmt(R[k]["manual_eur"]), "llm", fmt(R[k]["llm_eur"]),
              "legal_h", fmt(R[k]["legal_hours"]), "upkeep", fmt(R[k]["upkeep"]), "saving", f"{R[k]['saving']:.0%}")


if __name__ == "__main__":
    main()
