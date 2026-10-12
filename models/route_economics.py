#!/usr/bin/env python3
"""Route economics for the v1.2 decision package (2026-10-12).

Compares four entry routes for a solo operator based in Latvia, plus 'defer':
  R1 Agent risk review (limited assessment, NOT a pentest/certification)
  R2 Coding-agent enablement with measured pilot
  R3 Support-agent evaluation & outcome audit (first audit + monthly retainer)
  R4 Simpler adjacent: small AI workflow automations via freelance marketplace
  R5 Defer / build capability (cost only)

Every number is a dated source or an explicit ASSUMPTION. Prices are hypotheses
anchored to published comparables; NO customer has been asked.
Units: EUR per month unless stated. Revenue is shown NET of VAT. Latvian VAT on
Latvian clients is a pass-through and shown separately; EU B2B clients are
reverse-charged; non-EU clients are outside Latvian VAT (S122 s.19(1)).

Run: python3 models/route_economics.py -> models/route_economics_results.md / .csv
"""
from __future__ import annotations
import csv, pathlib
from dataclasses import dataclass, replace

OUT = pathlib.Path(__file__).resolve().parent

# ----------------------------------------------------------------- tax and benchmarks
VAT_LV = 0.21                 # S100 / S122
SE_SOCIAL_FULL, SE_BASE, SE_PENSION_EXCESS = 0.3107, 780.0, 0.10   # S125 (2026)
PIT_LOW = 0.255               # S125 / S100 (to €105,300/yr)
PIT_HIGH, PIT_BAND_PM = 0.33, 105_300 / 12   # S100: 33% above €105,300/yr
NONTAX_MIN = 550.0            # S125 (€6,600/yr)
CIT = 0.20                    # S100 (of gross distribution)
MUN = 0.25                    # S123 s.6 (on turnover; eligibility limits apply)
MUN_TURNOVER_CAP_YR = 50_000  # S124
BENCH_LV_PROF = 13.04         # S126 mean gross hourly earnings, professionals, LV, 2022
BENCH_EU_PROF = 24.40         # S126 EU27
EMP_SOCIAL = 0.105            # S100 employee social contribution 2026
# CALCULATION: approximate NET hourly equivalent of the LV professional mean (employee contributions + 25.5% PIT; ignores non-taxable minimum)
BENCH_LV_PROF_NET = round(BENCH_LV_PROF * (1 - EMP_SOCIAL) * (1 - PIT_LOW), 2)
FOREIGN_COST_SHARE = 0.6    # ASSUMPTION: share of cash costs bought from non-LV suppliers (APIs, SaaS)
STRIPE_EEA = (0.015, 0.25)    # S104 (used only where card payment assumed)


@dataclass(frozen=True)
class Route:
    key: str
    name: str
    price: float            # net revenue per engagement (EUR, ex-VAT)  ASSUMPTION anchored to comparables
    retainer: float         # monthly recurring revenue per retained client (0 if none)
    retain_share: float     # share of won clients who take the retainer
    retainer_months: float  # average months a retainer lasts
    deliver_h: float        # owner hours to deliver one engagement
    retainer_h: float       # owner hours per retained client per month
    rework: float           # extra delivery hours as share (rework, revisions)
    acquire_h: float        # owner hours of sales/outreach per WON engagement
    wins_pm: float          # engagements won per month at steady state
    ramp_months: int        # months before first win
    var_cash: float         # variable cash cost per engagement (APIs, tools, travel)
    platform_fee: float     # marketplace fee share of price (R4)
    card_paid: bool         # paid by card (Stripe) vs bank transfer
    fixed_pm: float         # fixed monthly cash (tools, insurance/12, bookkeeping, bank)
    setup_cash: float       # one-time cash
    setup_h: float          # one-time owner hours (materials, templates, learning)
    lv_client_share: float  # share of revenue from Latvian clients (VAT pass-through)
    eu_b2b_share: float     # share from VAT-registered clients in other EU states (forces full VAT registration; kills MUN)
    bad_debt: float         # share of revenue not collected / refunded


ADMIN_H = 6.0   # ASSUMPTION owner hours/month on bookkeeping, VAT/MUN filings, email, tools

# v1.2 after independent commercial review: BASE = newcomer without track record or network (cold-ish channels);
# HIGH = owner with a network or strong public proof (this was v1.2-draft's base); LOW = adverse.
# Field order: key,name,price,retainer,retain_share,retainer_months,deliver_h,retainer_h,rework,acquire_h,wins_pm,ramp_months,
#              var_cash,platform_fee,card_paid,fixed_pm,setup_cash,setup_h,lv_client_share,eu_b2b_share,bad_debt
R = {
 "R1": {
  "low":  Route("R1", "Agent risk review (limited assessment)", 1_500, 0, 0.0, 0, 30, 0, 0.30, 60, 0.25, 9, 60, 0.0, False, 220, 900, 80, 0.3, 0.3, 0.05),
  "base": Route("R1", "Agent risk review (limited assessment)", 2_500, 300, 0.25, 6, 20, 3, 0.20, 45, 0.5, 6, 60, 0.0, False, 260, 900, 60, 0.2, 0.4, 0.03),
  "high": Route("R1", "Agent risk review (limited assessment)", 4_000, 500, 0.35, 9, 16, 3, 0.10, 25, 1.0, 4, 80, 0.0, False, 320, 900, 50, 0.1, 0.4, 0.02),
 },
 "R2": {
  "low":  Route("R2", "Coding-agent enablement + measured pilot", 1_500, 0, 0.0, 0, 30, 0, 0.30, 60, 0.25, 9, 80, 0.0, False, 160, 400, 80, 0.3, 0.3, 0.05),
  "base": Route("R2", "Coding-agent enablement + measured pilot", 3_000, 0, 0.0, 0, 26, 0, 0.20, 40, 0.5, 6, 120, 0.0, False, 180, 400, 60, 0.2, 0.4, 0.03),
  "high": Route("R2", "Coding-agent enablement + measured pilot", 4_000, 0, 0.0, 0, 26, 0, 0.20, 25, 1.0, 4, 120, 0.0, False, 220, 400, 50, 0.1, 0.4, 0.02),
 },
 "R3": {
  "low":  Route("R3", "Support-agent evaluation & outcome audit", 2_000, 800, 0.30, 6, 40, 14, 0.30, 80, 0.15, 10, 100, 0.0, False, 240, 900, 100, 0.2, 0.4, 0.05),
  "base": Route("R3", "Support-agent evaluation & outcome audit", 3_500, 1_200, 0.40, 8, 30, 12, 0.20, 60, 0.33, 8, 120, 0.0, False, 280, 900, 80, 0.1, 0.5, 0.03),
  "high": Route("R3", "Support-agent evaluation & outcome audit", 5_000, 1_800, 0.50, 10, 26, 10, 0.10, 45, 0.5, 6, 150, 0.0, False, 340, 900, 60, 0.1, 0.5, 0.02),
 },
 "R4": {
  "low":  Route("R4", "Small AI workflow automations (marketplace)", 400, 100, 0.20, 6, 14, 1.5, 0.40, 12, 0.5, 4, 15, 0.15, False, 90, 150, 40, 0.0, 0.2, 0.05),
  "base": Route("R4", "Small AI workflow automations (marketplace)", 600, 100, 0.25, 6, 10, 1.5, 0.30, 10, 1.0, 3, 20, 0.10, False, 110, 150, 30, 0.0, 0.2, 0.03),
  "high": Route("R4", "Small AI workflow automations (marketplace)", 1_000, 150, 0.30, 8, 12, 1.5, 0.30, 6, 2.5, 2, 20, 0.10, False, 140, 150, 25, 0.0, 0.2, 0.02),
 },
}
SETUP_NOTES = {  # ASSUMPTION: what the one-time setup cash and monthly fixed cash cover
 "R1": "setup €900 = professional-indemnity insurance first instalment/quote deposit (~€500, UNKNOWN price), report template and test environment (€150), domain/email/site (€100), contract template review (€150); fixed = insurance/12, bookkeeping, tools, model API",
 "R2": "setup €400 = coding-agent subscriptions for the proof case (€150), domain/email/site (€100), metrics tooling (€150); fixed = bookkeeping, tool subscriptions, model API",
 "R3": "setup €900 = evaluation harness and LLM-judge API credits (€300), DPA/contract template review (€300), domain/site (€100), insurance quote (€200); fixed = bookkeeping, eval tooling, API",
 "R4": "setup €150 = automation-platform month and API credits for demos; fixed = automation platform, API, bookkeeping",
}
DEFER = {"low": (300, 120, 20), "base": (600, 200, 40), "high": (1_200, 300, 80)}  # (setup cash, setup hours, monthly tool cash) over 3 months


def steady_month(r: Route) -> dict:
    """Steady-state month after ramp. Retainer revenue = wins * share * months * fee (stock of active retainers)."""
    active_ret = r.wins_pm * r.retain_share * r.retainer_months
    rev_proj = r.wins_pm * r.price
    rev_ret = active_ret * r.retainer
    revenue = rev_proj + rev_ret                       # net of VAT
    fees = revenue * r.platform_fee
    if r.card_paid:
        fees += revenue * STRIPE_EEA[0] + r.wins_pm * STRIPE_EEA[1]
    bad = revenue * r.bad_debt
    var = r.wins_pm * r.var_cash
    cash_costs = fees + var + r.fixed_pm
    op_profit = revenue - bad - cash_costs
    hours = (r.wins_pm * (r.deliver_h * (1 + r.rework) + r.acquire_h)
             + active_ret * r.retainer_h + ADMIN_H)
    vat_passthrough = revenue * r.lv_client_share * VAT_LV
    return dict(revenue=revenue, rev_projects=rev_proj, rev_retainers=rev_ret, active_retainers=active_ret,
                bad_debt=bad, fees=fees, var=var, fixed=r.fixed_pm, cash_costs=cash_costs,
                op_profit=op_profit, hours=hours, vat_passthrough=vat_passthrough)


def take_home(profit: float, revenue: float, eu_b2b_share: float, cash_costs: float = 0.0) -> dict:
    """Monthly owner take-home under three Latvian forms (simplified; see S100, S122-S125)."""
    p = max(profit, 0.0)
    # Self-employed, general regime: contributions on profit (minimum-legal option), then PIT.
    # S125: income below €780/month -> 10% pension only on actual income; from €780 -> 31.07% on €780 + 10% on the excess
    soc = SE_PENSION_EXCESS * p if p < SE_BASE else SE_SOCIAL_FULL * SE_BASE + SE_PENSION_EXCESS * (p - SE_BASE)
    taxable = max(0.0, p - soc - NONTAX_MIN)
    pit = PIT_LOW * min(taxable, PIT_BAND_PM) + PIT_HIGH * max(0.0, taxable - PIT_BAND_PM)
    se = p - soc - pit
    # SIA, all profit distributed as dividends (no salary, so no social insurance cover).
    sia = p * (1 - CIT)
    # Micro-enterprise tax: 25% of TURNOVER; only if annual turnover <= €50k AND no EU B2B clients (S124).
    # Shown hypothetically for a client mix with NO EU-VAT-registered clients (non-EU + LV only).
    mun_ok = revenue * 12 <= MUN_TURNOVER_CAP_YR
    # Not fully VAT-registered -> s.139² special registration: 21% on foreign purchases is a non-deductible cost [S122].
    mun = (profit - MUN * revenue - VAT_LV * FOREIGN_COST_SHARE * cash_costs) if mun_ok else None
    return dict(self_employed=se, sia_dividend=sia, mun=mun, mun_eligible=mun_ok, se_social=soc, se_pit=pit)


def twelve_months(r: Route) -> dict:
    """Cumulative first 12 months: setup, ramp with no wins, then steady state (retainers build linearly)."""
    s = steady_month(r)
    cum_cash = -r.setup_cash
    cum_hours = r.setup_h
    cum_rev = 0.0
    for m in range(1, 13):
        if m <= r.ramp_months:
            cum_cash -= r.fixed_pm
            cum_hours += ADMIN_H + r.acquire_h * r.wins_pm      # still prospecting
            continue
        k = m - r.ramp_months
        active = min(k * r.wins_pm * r.retain_share, s["active_retainers"])
        rev = r.wins_pm * r.price + active * r.retainer
        fees = rev * r.platform_fee + (rev * STRIPE_EEA[0] + r.wins_pm * STRIPE_EEA[1] if r.card_paid else 0)
        cum_cash += rev * (1 - r.bad_debt) - fees - r.wins_pm * r.var_cash - r.fixed_pm
        cum_rev += rev
        cum_hours += r.wins_pm * (r.deliver_h * (1 + r.rework) + r.acquire_h) + active * r.retainer_h + ADMIN_H
    return dict(cum_cash=cum_cash, cum_rev=cum_rev, cum_hours=cum_hours)


def breakeven_wins(r: Route, target_hourly: float = 0.0) -> float:
    """Wins/month needed so that self-employed take-home per owner hour >= target (0 = cash break-even)."""
    for w in [x / 20 for x in range(1, 201)]:
        rr = replace(r, wins_pm=w)
        s = steady_month(rr)
        th = take_home(s["op_profit"], s["revenue"], rr.eu_b2b_share)["self_employed"] if target_hourly else s["op_profit"]
        if target_hourly:
            if s["op_profit"] > 0 and th / s["hours"] >= target_hourly:
                return w
        elif th >= 0:
            return w
    return float("nan")


def adverse(r: Route) -> Route:
    """Combined adverse case (after independent commercial review): several shocks at once."""
    return replace(r, wins_pm=r.wins_pm / 2, price=r.price * 0.7, retainer=r.retainer * 0.7,
                   rework=min(r.rework * 2, 1.0), acquire_h=r.acquire_h * 2,
                   platform_fee=(r.platform_fee + 0.05) if r.platform_fee else 0.0, ramp_months=r.ramp_months + 3)


def first_year_rates(r: Route) -> tuple[float, float]:
    """First 12 months incl. setup and ramp: (pre-tax operating cash per owner hour, approx. self-employed take-home per owner hour)."""
    t = twelve_months(r)
    if t["cum_cash"] <= 0:
        return t["cum_cash"] / t["cum_hours"], t["cum_cash"] / t["cum_hours"]   # a loss: no tax, report negative cash per hour
    th = take_home(t["cum_cash"] / 12, t["cum_rev"] / 12, r.eu_b2b_share)["self_employed"] * 12
    return t["cum_cash"] / t["cum_hours"], th / t["cum_hours"]


def sensitivity(r: Route) -> list[tuple[str, float]]:
    base = steady_month(r)
    def tk(x):
        s = steady_month(x)
        return take_home(s["op_profit"], s["revenue"], x.eu_b2b_share)["self_employed"]
    b = tk(r)
    cases = [
        ("Rework doubles", replace(r, rework=min(r.rework * 2, 1.0))),
        ("Sales halve (low utilisation)", replace(r, wins_pm=r.wins_pm / 2)),
        ("Price -30%", replace(r, price=r.price * 0.7, retainer=r.retainer * 0.7)),
        ("Bad debt/refunds 15%", replace(r, bad_debt=0.15)),
        ("Acquisition effort +100%", replace(r, acquire_h=r.acquire_h * 2)),
        ("COMBINED adverse: sales halve, price -30%, rework x2, acquisition x2, fee +5pp",
         adverse(r)),
    ]
    out = [("(base)", 0.0, 0.0, b / base["hours"])]
    for name, x in cases:
        s = steady_month(x)
        out.append((name, tk(x) - b, s["hours"] - base["hours"], tk(x) / s["hours"]))
    return out


def eph(x):
    return f"€{x:.1f}" if x >= 0 else f"−€{abs(x):.1f} (loss)"


def money(x):
    return "n/a" if x is None else f"€{x:,.0f}"


def main():
    L, rows = [], []
    w = L.append
    w("# Route economics (generated by `models/route_economics.py`, v1.2, 2026-10-12)\n")
    w("**Read this first.** Prices, win rates and hours are **ASSUMPTIONS** anchored to published comparables "
      "(Claude Code workshops from $900/day and €890 per person for 2 days [S129][S128]; LLM security audits $6k–$45k+, "
      "specialist floor ~$16k [S130]; Upwork AI-related work +22% YoY [S127]). No customer has been asked. "
      "Revenue is net of VAT. Latvian VAT on Latvian clients is a pass-through, not income. "
      "Take-home pay uses simplified 2026 Latvian rules [S100][S123][S124][S125] and is **not tax advice**.\n")
    w(f"Admin overhead assumed {ADMIN_H:.0f} owner-hours/month in all routes. Opportunity-cost benchmarks: mean gross hourly earnings of "
      f"professionals 2022 — Latvia €{BENCH_LV_PROF}, EU27 €{BENCH_EU_PROF} [S126]; approximate **net** Latvian equivalent "
      f"€{BENCH_LV_PROF_NET}/h after 10.5% employee contributions and 25.5% PIT [S100] (CALCULATION). Take-home figures below are net, so compare them with "
      f"€{BENCH_LV_PROF_NET}/h — and, above all, with **your own** net employment or contracting rate (UNKNOWN).\n")
    w("**Cases (revised after independent commercial review):** *base* = a newcomer without track record or warm network; "
      "*high* = an owner with a network or strong public proof; *low* = adverse. The combined adverse case also adds 3 months of ramp and +5 percentage points of marketplace fee.\n")
    for key in ["R1", "R2", "R3", "R4"]:
        name = R[key]["base"].name
        w(f"\n## {key} — {name}\n")
        w(f"Setup and fixed-cost contents (ASSUMPTION): {SETUP_NOTES[key]}\n")
        w("| | Low | Base | High |\n|---|---|---|---|")
        res = {c: steady_month(R[key][c]) for c in ("low", "base", "high")}
        th = {c: take_home(res[c]["op_profit"], res[c]["revenue"], R[key][c].eu_b2b_share, res[c]["cash_costs"]) for c in res}
        tw = {c: twelve_months(R[key][c]) for c in res}
        def row(label, f):
            w(f"| {label} | " + " | ".join(f(c) for c in ("low", "base", "high")) + " |")
        row("Price per engagement (net of VAT) — ASSUMPTION", lambda c: money(R[key][c].price))
        row("Retainer €/month × share of clients", lambda c: f"{money(R[key][c].retainer)} × {R[key][c].retain_share:.0%}" if R[key][c].retainer else "—")
        row("Engagements won per month (steady state)", lambda c: f"{R[key][c].wins_pm:g}")
        row("Months before first win", lambda c: f"{R[key][c].ramp_months}")
        row("**One-time setup cash / owner hours**", lambda c: f"{money(R[key][c].setup_cash)} / {R[key][c].setup_h:.0f} h")
        row("Monthly fixed cash costs", lambda c: money(R[key][c].fixed_pm))
        row("Variable cash per engagement (+ platform fee)", lambda c: money(R[key][c].var_cash) + (f" + {R[key][c].platform_fee:.0%}" if R[key][c].platform_fee else ""))
        row("Sales effort per won engagement (owner hours)", lambda c: f"{R[key][c].acquire_h:.0f} h")
        row("Delivery hours per engagement (incl. rework)", lambda c: f"{R[key][c].deliver_h*(1+R[key][c].rework):.0f} h")
        row("**Revenue / month (net of VAT)**", lambda c: money(res[c]["revenue"]))
        row("VAT collected on Latvian clients (pass-through, not income)", lambda c: money(res[c]["vat_passthrough"]))
        row("Cash costs / month (fixed + variable + fees)", lambda c: money(res[c]["cash_costs"]))
        row("Bad debt / refunds", lambda c: money(res[c]["bad_debt"]))
        row("**Operating profit / month**", lambda c: money(res[c]["op_profit"]))
        row("Owner hours / month", lambda c: f"{res[c]['hours']:.0f} h")
        row("**Take-home: self-employed (general regime)**", lambda c: money(th[c]["self_employed"]))
        row("Take-home: SIA, all profit as dividend (no social cover)", lambda c: money(th[c]["sia_dividend"]))
        row("Take-home: micro-enterprise tax — only if NO EU-VAT-registered clients (incl. 21% non-deductible VAT on foreign tools)", lambda c: money(th[c]["mun"]) if th[c]["mun_eligible"] else "not eligible (>€50k/yr)")
        row("**Self-employed take-home per owner hour**", lambda c: f"€{th[c]['self_employed']/res[c]['hours']:.1f}" if res[c]['hours'] else "—")
        row("First 12 months: cumulative operating cash before income tax (after setup and ramp)", lambda c: money(tw[c]["cum_cash"]))
        row("First 12 months: owner hours", lambda c: f"{tw[c]['cum_hours']:,.0f} h")
        row("**First 12 months: take-home per owner hour (approx., self-employed)**", lambda c: eph(first_year_rates(R[key][c])[1]))
        row("First 12 months under COMBINED adverse case: take-home per owner hour", lambda c: eph(first_year_rates(adverse(R[key][c]))[1]))
        row("Break-even wins/month (operating profit ≥ 0)", lambda c: f"{breakeven_wins(R[key][c]):.2f}")
        row(f"Wins/month for take-home ≥ €{BENCH_LV_PROF_NET}/h (net equivalent of LV professional mean)", lambda c: (lambda v: "not reached" if v != v else f"{v:.2f}")(breakeven_wins(R[key][c], BENCH_LV_PROF_NET)))
        w("\nSensitivity of base case (change in monthly self-employed take-home; change in owner hours):\n")
        w("| Shock | Δ take-home €/month | Δ owner hours | Take-home per owner hour |\n|---|---|---|---|")
        for name, d, dh, ph in sensitivity(R[key]["base"]):
            w(f"| {name} | {d:+,.0f} | {dh:+.0f} | €{ph:.1f} |")
        for c in ("low", "base", "high"):
            rows.append([key, c, round(res[c]["revenue"]), round(res[c]["op_profit"]), round(res[c]["hours"]),
                         round(th[c]["self_employed"]), round(th[c]["sia_dividend"]),
                         round(th[c]["mun"]) if th[c]["mun_eligible"] else "", round(tw[c]["cum_cash"])])
    w("\n## R5 — Defer and build capability (3 months)\n")
    w("| | Low | Base | High |\n|---|---|---|---|")
    w("| Cash (courses, API credits, tools) | " + " | ".join(money(DEFER[c][0] + 3 * DEFER[c][2]) for c in ("low", "base", "high")) + " |")
    w("| Owner hours | " + " | ".join(f"{DEFER[c][1]} h" for c in ("low", "base", "high")) + " |")
    w("| Revenue | €0 | €0 | €0 |")
    w("\nOutput is capability and a portfolio, not income (ASSUMPTION).\n")
    w("\n## Cross-route summary (base case = newcomer)\n")
    w("| Route | Revenue/mo | Operating profit/mo | Owner h/mo | Self-employed take-home/mo | €/owner-hour (steady) | €/owner-hour first 12 months | Adverse, first 12 months | 12-month operating cash (pre-tax) | Months to first win |")
    w("|---|---|---|---|---|---|---|---|---|---|")
    for key in ["R1", "R2", "R3", "R4"]:
        r = R[key]["base"]; s = steady_month(r); t = take_home(s["op_profit"], s["revenue"], r.eu_b2b_share); tw = twelve_months(r)
        w(f"| {key} {r.name} | {money(s['revenue'])} | {money(s['op_profit'])} | {s['hours']:.0f} | {money(t['self_employed'])} | "
          f"€{t['self_employed']/s['hours']:.1f} | {eph(first_year_rates(r)[1])} | {eph(first_year_rates(adverse(r))[1])} | {money(tw['cum_cash'])} | {r.ramp_months} |")
    (OUT / "route_economics_results.md").write_text("\n".join(L) + "\n")
    with open(OUT / "route_economics_results.csv", "w", newline="") as f:
        cw = csv.writer(f)
        cw.writerow(["route", "case", "revenue_pm", "op_profit_pm", "owner_hours_pm", "takehome_self_employed_pm",
                     "takehome_sia_dividend_pm", "takehome_mun_pm", "cum_cash_12m"])
        cw.writerows(rows)
    print("\n".join(L))


if __name__ == "__main__":
    main()
