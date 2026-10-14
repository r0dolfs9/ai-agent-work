"""Cost and time model for the agri-rules comparison system (deliverable H).

Run:  python3 agri-rules/models/cost_model.py
Writes agri-rules/models/cost_model_results.md

Labels used below:
  VERIFIED  = read on the provider's official page on 2026-10-14 (ledger IDs in brackets)
  ASSUMPTION = our input; the pilot must replace it with a measurement
  UNVERIFIED = third-party figure, kept only as a placeholder
All token counts are ASSUMPTIONS. Nothing here has been measured yet.
"""
import sys
from pathlib import Path

USD_PER_EUR = 1.1188          # VERIFIED: ECB reference rate 2026-10-13 [E-P10]
VAT = 0.21                    # VERIFIED: Latvian standard rate (repo claims-ledger L50); applies only if not reverse-charged
OPENROUTER_FEE = 0.055        # VERIFIED: 5.5% on credit purchases, Standard plan [E-P05]

# USD per 1M tokens (input, output). VERIFIED 2026-10-14 [E-P01..E-P04]
PRICES = {
    "haiku-5.5":            (0.10, 0.50),   # <=100K-token prompts; >100K = 0.50/2.50
    "sonnet-5.5":           (2.00, 10.00),
    "opus-5.5":             (4.00, 20.00),
    "gpt-5.4-mini":         (0.75, 4.50),
    "gpt-6-astra":          (10.00, 50.00),
    "gemini-3.8-flash":     (0.75, 3.75),
    "gemini-3.5-flash-lite":(0.30, 2.50),
    "gemini-3.1-pro":       (2.00, 12.00),  # <=200K-token prompts
}
BRAVE_USD_PER_1K = 5.0        # VERIFIED [E-P07]
DEEPL_EUR_PER_M_CHARS = 20.0  # UNVERIFIED third-party figure; official page did not render [U-07]
SERVER_EUR_MONTH = 36.0       # UNVERIFIED (the proposal's figure; official Hetzner prices did not render) [U-08]

# Pipeline stages: (name, unit, input_tokens, output_tokens, role). ASSUMPTION.
# unit "cell" = one rule x one jurisdiction layer; unit "rule" = once per rule.
STAGES = [
    ("locate provision",        "cell", 15000, 1000, "primary"),
    ("extract + translate",     "cell",  8000, 2500, "primary"),
    ("self-check vs source",    "cell", 10000, 1500, "primary"),
    ("practical context",       "cell",  4000, 1000, "primary"),
    ("challenge review",        "cell", 12000, 1500, "challenger"),
    ("cross-jurisdiction compare", "rule", 25000, 3000, "primary"),
    ("page draft",              "rule", 15000, 3000, "primary"),
    ("page challenge",          "rule", 15000, 1500, "challenger"),
]

SCENARIOS = {
    #        primary, challenger, token multiplier, retry factor, batch discount, search queries/cell
    "low":  dict(primary="haiku-5.5", challenger="gemini-3.5-flash-lite", tok=0.6, retry=1.15, batch=0.5, queries=3,
                 gold_h=0.5, review_h=0.25, lawyer_eur_h=100, deepl=False),
    "base": dict(primary="sonnet-5.5", challenger="gemini-3.1-pro", tok=1.0, retry=1.35, batch=1.0, queries=5,
                 gold_h=0.9, review_h=0.5, lawyer_eur_h=175, deepl=True),
    "high": dict(primary="opus-5.5", challenger="gpt-6-astra", tok=2.0, retry=1.6, batch=1.0, queries=10,
                 gold_h=1.5, review_h=1.0, lawyer_eur_h=250, deepl=True),
}
EXCERPT_CHARS_PER_CELL = 3000  # ASSUMPTION: original-language excerpt sent to DeepL cross-check


def ai_cost_usd(rules: int, layers: int, sc: dict) -> tuple[float, float, float]:
    """Returns (USD, input MTok, output MTok) for one full AI pass.
    cost = Σ_stage units × tok_in × mult × retry × price_in/1e6 + same for output, × batch factor."""
    cells = rules * layers
    usd = mtok_in = mtok_out = 0.0
    for _, unit, tin, tout, role in STAGES:
        n = cells if unit == "cell" else rules
        model = sc["primary"] if role == "primary" else sc["challenger"]
        pin, pout = PRICES[model]
        i = n * tin * sc["tok"] * sc["retry"] / 1e6
        o = n * tout * sc["tok"] * sc["retry"] / 1e6
        mtok_in += i
        mtok_out += o
        usd += (i * pin + o * pout) * sc["batch"]
    return usd, mtok_in, mtok_out


def run_cost_eur(rules: int, layers: int, sc: dict, via_openrouter: bool = True) -> dict:
    usd, mi, mo = ai_cost_usd(rules, layers, sc)
    usd_total = usd * (1 + OPENROUTER_FEE if via_openrouter else 1)
    search_usd = rules * layers * sc["queries"] * BRAVE_USD_PER_1K / 1000
    deepl_eur = (rules * layers * EXCERPT_CHARS_PER_CELL / 1e6 * DEEPL_EUR_PER_M_CHARS) if sc["deepl"] else 0.0
    eur = (usd_total + search_usd) / USD_PER_EUR + deepl_eur
    return dict(ai_usd=usd, mtok_in=mi, mtok_out=mo, search_usd=search_usd, deepl_eur=deepl_eur,
                eur_ex_vat=eur, eur_inc_vat=eur * (1 + VAT))


# Phases: (name, rules, layers, gold cells, reviewed cells, lawyer-reviewed cells, AI passes, months of server)
PHASES = [
    ("0 Source-feasibility sprint (3 questions x 10 layers, gold by hand, no AI)", 3, 10, 30, 0, 0, 0, 0),
    ("1 20-rule pilot (gold on 20 x 5 layers; AI on 20 x 10; 3 candidate pairs)", 20, 10, 100, 200, 20, 3, 0),
    ("2 First 100-rule build (1,000 cells)", 100, 10, 0, 1000, 100, 1, 0),
    ("3 One complete refresh (re-run 30% changed cells, re-review them)", 30, 10, 0, 300, 30, 1, 0),
]


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    L = ["# Cost and time model results (generated by cost_model.py)", "",
         f"FX: 1 EUR = {USD_PER_EUR} USD (ECB 2026-10-13). VAT {VAT:.0%} shown separately. "
         f"OpenRouter fee {OPENROUTER_FEE:.1%} included in AI totals. All token figures are ASSUMPTIONS.", "",
         "## 1. AI cost of one complete 100-rule x 10-layer pass (1,000 cells)", "",
         "| Scenario | Primary / challenger | Input MTok | Output MTok | AI USD (pre-fee) | Search USD | DeepL € (unverified) | **€ ex VAT** | € inc 21% VAT |",
         "|---|---|---|---|---|---|---|---|---|"]
    for k, sc in SCENARIOS.items():
        r = run_cost_eur(100, 10, sc)
        L.append(f"| {k} | {sc['primary']} / {sc['challenger']} | {r['mtok_in']:.1f} | {r['mtok_out']:.1f} | "
                 f"{r['ai_usd']:,.0f} | {r['search_usd']:.0f} | {r['deepl_eur']:.0f} | **{r['eur_ex_vat']:,.0f}** | {r['eur_inc_vat']:,.0f} |")
    L += ["", "Formula per stage: units × tokens × multiplier × retry ÷ 10⁶ × price per MTok × batch factor. "
          "Units = 1,000 cells for cell stages, 100 rules for rule stages. Low scenario assumes the 50% batch discount.", "",
          "Compare: the proposal's €590 per run (range €170–€2,000) is a HYPOTHESIS; this model's spread is wider because "
          "model choice alone moves cost by two orders of magnitude.", "",
          "## 2. Phases: money and hours", "",
          "| Phase | Scenario | AI + search + DeepL € ex VAT | Gold-standard h | Review h | Lawyer € (ASSUMPTION rate) | Server € |",
          "|---|---|---|---|---|---|---|"]
    for name, rules, layers, gold, rev, law, passes, months in PHASES:
        for k, sc in SCENARIOS.items():
            run = run_cost_eur(rules, layers, sc)["eur_ex_vat"] * passes
            lawyer = law * 0.75 * sc["lawyer_eur_h"]   # ASSUMPTION: 45 min lawyer time per cell
            L.append(f"| {name} | {k} | {run:,.0f} | {gold * sc['gold_h']:.0f} | {rev * sc['review_h']:.0f} | "
                     f"{lawyer:,.0f} | {months * SERVER_EUR_MONTH:.0f} |")
    L += ["", "Operator hours for building, scoring and writing are in 07-cost-timeline.md (not modelled per token).", "",
          "## 3. Monthly maintenance (after the first build)", "",
          "Formula: monitoring is free (official feeds/APIs); cost = changed cells per month × (AI pass per cell + review hours).", "",
          "| Scenario | Changed cells / month (ASSUMPTION) | AI € / month | Review h / month | Server € / month if used |",
          "|---|---|---|---|---|"]
    for k, sc, changed in (("low", SCENARIOS["low"], 10), ("base", SCENARIOS["base"], 30), ("high", SCENARIOS["high"], 80)):
        per_cell = run_cost_eur(100, 10, sc)["eur_ex_vat"] / 1000
        L.append(f"| {k} | {changed} | {changed * per_cell:,.1f} | {changed * sc['review_h']:.0f} | {SERVER_EUR_MONTH:.0f} (unverified) |")
    out = Path(__file__).with_name("cost_model_results.md")
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("\n".join(L))


if __name__ == "__main__":
    main()
