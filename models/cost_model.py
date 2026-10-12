#!/usr/bin/env python3
"""Transparent cost model for three AI-agent deployment scenarios.

Every input is either a dated price (with a source ID from research/sources.csv)
or an explicit ASSUMPTION. Run:  python3 models/cost_model.py
Writes models/cost_model_results.md and models/cost_model_results.csv.

Currency: USD, excluding sales tax / VAT. Prices retrieved 2026-10-12.
"""
from __future__ import annotations
import csv, pathlib
from dataclasses import dataclass, replace

OUT = pathlib.Path(__file__).resolve().parent

# ---------------------------------------------------------------- prices
# USD per 1M tokens: (input, cache_write_5m, cache_read, output)
# Anthropic [S044]; OpenAI [S045] (no separate cache-write charge: write = input);
# Google [S046] (cache storage per hour ignored here — assumption, small at these volumes).
PRICES = {
    "claude-haiku-5.5":  (0.10, 0.125, 0.01, 0.50),   # prompts <=100k tokens
    "claude-sonnet-5.5": (2.00, 2.50, 0.10, 10.00),
    "claude-opus-5.5":   (4.00, 5.00, 0.20, 20.00),
    "claude-fable-5.1":  (10.00, 12.50, 0.25, 50.00),
    "gpt-5.4-mini":      (0.75, 0.75, 0.075, 4.50),
    "gpt-5.5":           (5.00, 5.00, 0.50, 30.00),
    "gemini-3.1-pro":    (2.00, 2.00, 0.20, 12.00),   # <=200k prompt
}
WEB_SEARCH_PER_CALL = 10 / 1000          # $10 per 1,000 searches [S044][S045]
FIN_PER_OUTCOME = 0.99                    # Intercom Fin [S071]
CSR_WAGE = 21.53                          # BLS May 2025 median [S077]
DEV_SALARY = 135_980                      # BLS May 2025 median [S078]
LOADED = 1.4                              # ASSUMPTION: wages ≈ 70% of total employment cost
CSR_RATE = CSR_WAGE * LOADED              # $/hour loaded
DEV_MONTH = DEV_SALARY * LOADED / 12      # $/month loaded per FTE
CONTRACTOR_RATE = 90.0                    # ASSUMPTION: freelance automation builder $/hour


@dataclass(frozen=True)
class Loop:
    """Token shape of one agent task (one attempt)."""
    model: str
    steps: int            # model calls per task (agent loop iterations)
    base_ctx: int         # system prompt + tool definitions + memory/retrieval at step 1
    delta: int            # tokens appended per step (tool results + previous output)
    out: int              # output tokens per step, incl. thinking
    cache_hit: float      # share of the reusable prefix actually read from cache
    searches: float = 0   # web searches per task


def task_cost(l: Loop) -> float:
    """$ for one attempt of one task. Context grows linearly; the prefix from the
    previous step can be served from cache (cache_hit share); everything else is
    written to the 5-minute cache (or billed at input price for providers without
    a write premium)."""
    p_in, p_w, p_r, p_out = (x / 1e6 for x in PRICES[l.model])
    cost = 0.0
    for k in range(l.steps):
        ctx = l.base_ctx + k * l.delta
        prefix = 0 if k == 0 else l.base_ctx + (k - 1) * l.delta
        cached = l.cache_hit * prefix
        fresh = ctx - cached
        cost += cached * p_r + fresh * p_w + l.out * p_out
    return cost + l.searches * WEB_SEARCH_PER_CALL


def tokens_per_task(l: Loop) -> int:
    return sum(l.base_ctx + k * l.delta + l.out for k in range(l.steps))


# ---------------------------------------------------------------- scenario 1
@dataclass(frozen=True)
class Personal:
    loop: Loop
    tasks_per_day: float
    success: float        # first-attempt success; failures retried once by the user
    hosting: float        # $/month (VPS or 0 on own laptop)
    oversight_min: float  # minutes of the owner's attention per task


def personal(s: Personal) -> dict:
    tasks = s.tasks_per_day * 30
    attempts = tasks * (1 + (1 - s.success))          # one retry for failures
    successes = tasks * (s.success + (1 - s.success) * s.success)
    api = attempts * task_cost(s.loop)
    total = api + s.hosting
    return dict(tasks=tasks, api=api, total=total, per_success=total / successes,
                success_share=successes / tasks,
                owner_hours=tasks * s.oversight_min / 60,
                tokens_m=attempts * tokens_per_task(s.loop) / 1e6)


PERSONAL = {
    "low":  Personal(Loop("claude-sonnet-5.5", 4, 8_000, 2_000, 400, 0.9, 0.5), 5, 0.90, 0, 0.5),
    "base": Personal(Loop("claude-sonnet-5.5", 8, 15_000, 4_000, 800, 0.8, 1.0), 15, 0.80, 6, 1.0),
    "high": Personal(Loop("claude-sonnet-5.5", 20, 30_000, 8_000, 1_500, 0.6, 3.0), 40, 0.65, 25, 2.0),
}

# ---------------------------------------------------------------- scenario 2
@dataclass(frozen=True)
class SmallBiz:
    loop: Loop
    volume: int            # inbound emails / tickets per month
    accept: float          # share of drafts approved with no edit
    review_min: float      # human minutes to review every draft (human-in-the-loop)
    fix_min: float         # extra minutes to fix a rejected draft
    tools: float           # $/month helpdesk/automation platform add-on
    observability: float   # $/month tracing/eval
    hosting: float         # $/month
    setup_hours: float     # one-time build hours (amortised over 12 months)
    maint_hours: float     # hours/month maintenance, prompt fixes, evals
    human_only_min: float  # baseline minutes per email without the agent


def smallbiz(s: SmallBiz) -> dict:
    llm = s.volume * task_cost(s.loop)
    human = s.volume * (s.review_min + (1 - s.accept) * s.fix_min) / 60 * CSR_RATE
    setup_m = s.setup_hours * CONTRACTOR_RATE / 12
    maint = s.maint_hours * CONTRACTOR_RATE
    fixed = s.tools + s.observability + s.hosting + setup_m + maint
    total = llm + human + fixed
    baseline = s.volume * s.human_only_min / 60 * CSR_RATE
    return dict(llm=llm, human=human, fixed=fixed, total=total,
                per_item=total / s.volume, baseline=baseline,
                saving=baseline - total, saving_pct=(baseline - total) / baseline,
                setup_once=s.setup_hours * CONTRACTOR_RATE)


SMALLBIZ = {
    "low":  SmallBiz(Loop("claude-sonnet-5.5", 3, 6_000, 1_500, 300, 0.85), 3_000, 0.70, 0.5, 3, 50, 0, 0, 10, 2, 6),
    "base": SmallBiz(Loop("claude-sonnet-5.5", 5, 10_000, 3_000, 600, 0.75), 3_000, 0.55, 1.0, 5, 150, 39, 20, 30, 5, 8),
    "high": SmallBiz(Loop("claude-sonnet-5.5", 10, 20_000, 6_000, 1_200, 0.50), 3_000, 0.35, 2.0, 8, 400, 117, 60, 80, 12, 10),
}

# ---------------------------------------------------------------- scenario 3
@dataclass(frozen=True)
class Prod:
    loop: Loop
    volume: int            # conversations / month
    resolve: float         # share fully resolved by the agent (no human)
    escalate_min: float    # human minutes per escalated conversation (incl. context reading)
    qa_share: float        # share of agent-resolved conversations human-QA sampled
    qa_min: float
    judge_share: float     # share auto-graded by an LLM judge (Haiku-class)
    infra: float           # $/month hosting, vector DB, queues, logging
    obs: float             # $/month observability / eval platform
    eng_fte: float         # engineering FTE for build-maintain-evaluate
    sec_annual: float      # $/year security testing, compliance review, red-teaming
    human_only_min: float  # baseline handling minutes per conversation


JUDGE = Loop("claude-haiku-5.5", 1, 6_000, 0, 300, 0.0)


def prod_build(s: Prod) -> dict:
    llm = s.volume * task_cost(s.loop)
    judge = s.volume * s.judge_share * task_cost(JUDGE)
    resolved = s.volume * s.resolve
    esc = s.volume * (1 - s.resolve) * s.escalate_min / 60 * CSR_RATE
    qa = resolved * s.qa_share * s.qa_min / 60 * CSR_RATE
    eng = s.eng_fte * DEV_MONTH
    fixed = s.infra + s.obs + eng + s.sec_annual / 12
    total = llm + judge + esc + qa + fixed
    agent_side = llm + judge + qa + fixed       # what the automation itself costs
    baseline = s.volume * s.human_only_min / 60 * CSR_RATE
    return dict(llm=llm, judge=judge, escalation=esc, qa=qa, fixed=fixed, total=total,
                per_conv=total / s.volume, per_agent_resolution=agent_side / resolved,
                baseline=baseline, saving_pct=(baseline - total) / baseline)


def prod_buy(s: Prod, seats: int = 10, seat_price: float = 85) -> dict:
    """Vendor with per-outcome pricing (Intercom Fin $0.99/outcome [S071]); seats
    for the human team ($85 Advanced tier [S071]); same escalation and QA load;
    integration engineering assumed at 25% of the build FTE (ASSUMPTION)."""
    resolved = s.volume * s.resolve
    vendor = resolved * FIN_PER_OUTCOME + seats * seat_price
    esc = s.volume * (1 - s.resolve) * s.escalate_min / 60 * CSR_RATE
    qa = resolved * s.qa_share * s.qa_min / 60 * CSR_RATE
    eng = 0.25 * s.eng_fte * DEV_MONTH
    total = vendor + esc + qa + eng + s.sec_annual / 12 * 0.5
    return dict(vendor=vendor, escalation=esc, qa=qa, total=total, per_conv=total / s.volume)


PROD = {
    "low":  Prod(Loop("claude-sonnet-5.5", 4, 10_000, 2_000, 400, 0.90), 50_000, 0.65, 6, 0.02, 3, 0.05, 500, 500, 0.5, 15_000, 7),
    "base": Prod(Loop("claude-sonnet-5.5", 6, 20_000, 3_000, 700, 0.80), 50_000, 0.50, 8, 0.05, 3, 0.10, 1_500, 2_000, 1.0, 40_000, 8),
    "high": Prod(Loop("claude-sonnet-5.5", 12, 40_000, 6_000, 1_200, 0.60), 50_000, 0.35, 12, 0.10, 4, 0.20, 5_000, 6_000, 2.0, 100_000, 10),
}

# ---------------------------------------------------------------- sensitivity
def tornado(base: Prod, low: Prod, high: Prod) -> list[tuple[str, float, float]]:
    """One-at-a-time swing of each production input between its low and high case."""
    out = []
    b = prod_build(base)["per_conv"]
    loop_fields = ["steps", "base_ctx", "delta", "out", "cache_hit"]
    for f in loop_fields:
        lo = prod_build(replace(base, loop=replace(base.loop, **{f: getattr(low.loop, f)})))["per_conv"]
        hi = prod_build(replace(base, loop=replace(base.loop, **{f: getattr(high.loop, f)})))["per_conv"]
        out.append((f"loop.{f}", lo - b, hi - b))
    for f in ["resolve", "escalate_min", "qa_share", "infra", "obs", "eng_fte", "sec_annual"]:
        lo = prod_build(replace(base, **{f: getattr(low, f)}))["per_conv"]
        hi = prod_build(replace(base, **{f: getattr(high, f)}))["per_conv"]
        out.append((f, lo - b, hi - b))
    return sorted(out, key=lambda t: -max(abs(t[1]), abs(t[2])))


def money(x: float) -> str:
    return f"${x:,.2f}" if abs(x) < 100 else f"${x:,.0f}"


def main() -> None:
    global CSR_RATE
    lines, rows = [], []
    w = lines.append
    w("# Cost model results (generated by `models/cost_model.py`)\n")
    w("All figures USD/month unless stated, excluding VAT/sales tax. Prices dated 2026-10-12 "
      "([S044] Anthropic, [S045] OpenAI, [S046] Google, [S071] Intercom). Labour: BLS May 2025 medians "
      f"[S077][S078] × {LOADED} loaded-cost ASSUMPTION → support ${CSR_RATE:.2f}/h, engineer "
      f"${DEV_MONTH:,.0f}/FTE-month; contractor ${CONTRACTOR_RATE:.0f}/h ASSUMPTION.\n")

    w("## Per-task model cost by model (base production loop shape)\n")
    w("| Model | $ per task attempt | Tokens processed per task |\n|---|---|---|")
    for m in PRICES:
        l = replace(PROD["base"].loop, model=m)
        w(f"| {m} | {task_cost(l):.4f} | {tokens_per_task(l):,} |")
        rows.append(["per_task", m, "base", "cost_per_task", round(task_cost(l), 5)])
    nocache = replace(PROD["base"].loop, cache_hit=0.0)
    w(f"\nSame loop on claude-sonnet-5.5 with **no cache hits**: {task_cost(nocache):.4f} $/task "
      f"(vs {task_cost(PROD['base'].loop):.4f} at 80% hit) — caching is the largest free lever.\n")

    w("## Scenario 1 — Personal agent (API pay-as-you-go vs subscription)\n")
    w("| Case | Tasks/mo | API $ | Hosting $ | Total $/mo | $ per successful task | Success after 1 retry | Owner oversight h/mo | Tokens (M) |\n|---|---|---|---|---|---|---|---|---|")
    for k, s in PERSONAL.items():
        r = personal(s)
        w(f"| {k} | {r['tasks']:.0f} | {money(r['api'])} | {money(s.hosting)} | {money(r['total'])} | "
          f"{money(r['per_success'])} | {r['success_share']:.0%} | {r['owner_hours']:.1f} | {r['tokens_m']:.1f} |")
        rows += [["personal", s.loop.model, k, key, round(v, 4)] for key, v in r.items()]
    w("\nComparison: Claude Pro $20/mo, Max from $100/mo [S047] (flat, but with rolling 5-hour and weekly usage limits; "
      "subscription credentials may **not** be used by third-party agent harnesses [S016]).\n")
    w("Model-choice sensitivity for the base personal case:\n")
    w("| Model | Total $/mo |\n|---|---|")
    for m in ["claude-haiku-5.5", "claude-sonnet-5.5", "claude-opus-5.5", "claude-fable-5.1", "gpt-5.5", "gemini-3.1-pro"]:
        s = replace(PERSONAL["base"], loop=replace(PERSONAL["base"].loop, model=m))
        w(f"| {m} | {money(personal(s)['total'])} |")
    w("\n*Model swap holds success rate constant — in reality cheaper models usually fail more on long tasks, "
      "which raises cost per success (see METR/RLI evidence in the paper).*\n")

    w("## Scenario 2 — Small-business email/ticket agent (3,000 items/month, human approves every draft)\n")
    w("| Case | LLM $ | Human review $ | Fixed $ (tools, obs, hosting, setup/12, maintenance) | Total $ | $ per item | Human-only baseline $ | Saving | One-time setup $ |\n|---|---|---|---|---|---|---|---|---|")
    for k, s in SMALLBIZ.items():
        r = smallbiz(s)
        w(f"| {k} | {money(r['llm'])} | {money(r['human'])} | {money(r['fixed'])} | {money(r['total'])} | "
          f"{money(r['per_item'])} | {money(r['baseline'])} | {r['saving_pct']:.0%} | {money(r['setup_once'])} |")
        rows += [["smallbiz", s.loop.model, k, key, round(v, 4)] for key, v in r.items()]
    w("\nVolume sensitivity (base assumptions):\n")
    w("| Items/month | $ per item | Saving vs human-only |\n|---|---|---|")
    for v in [300, 1_000, 3_000, 10_000]:
        r = smallbiz(replace(SMALLBIZ["base"], volume=v))
        w(f"| {v:,} | {money(r['per_item'])} | {r['saving_pct']:.0%} |")
    w("")

    w("## Scenario 3 — Production customer-support agent (50,000 conversations/month)\n")
    w("| Case | LLM $ | LLM-judge $ | Escalations $ | QA $ | Fixed $ (infra, obs, eng, security) | Total $ | $ per conversation | $ per agent-resolved conversation (automation cost only) | Human-only baseline $ | Saving |\n|---|---|---|---|---|---|---|---|---|---|---|")
    for k, s in PROD.items():
        r = prod_build(s)
        w(f"| {k} | {money(r['llm'])} | {money(r['judge'])} | {money(r['escalation'])} | {money(r['qa'])} | {money(r['fixed'])} | "
          f"{money(r['total'])} | {money(r['per_conv'])} | {money(r['per_agent_resolution'])} | {money(r['baseline'])} | {r['saving_pct']:.0%} |")
        rows += [["prod_build", s.loop.model, k, key, round(v, 4)] for key, v in r.items()]
    w("\nBuy instead of build (per-outcome vendor pricing, same resolution and escalation assumptions):\n")
    w("| Case | Vendor $ | Escalations $ | QA $ | Total $ | $ per conversation |\n|---|---|---|---|---|---|")
    for k, s in PROD.items():
        r = prod_buy(s)
        w(f"| {k} | {money(r['vendor'])} | {money(r['escalation'])} | {money(r['qa'])} | {money(r['total'])} | {money(r['per_conv'])} |")
        rows += [["prod_buy", "vendor", k, key, round(v, 4)] for key, v in r.items()]

    w("\n### Sensitivity (tornado): change in $ per conversation when one input moves from its base value to its value in the low-cost / high-cost case\n")
    w("| Input | Δ with low-cost-case value | Δ with high-cost-case value |\n|---|---|---|")
    for name, lo, hi in tornado(PROD["base"], PROD["low"], PROD["high"]):
        w(f"| {name} | {lo:+.3f} | {hi:+.3f} |")
    b = prod_build(PROD["base"])
    w(f"\nBase total ${b['total']:,.0f}: LLM tokens are {b['llm']/b['total']:.0%}, human escalations "
      f"{b['escalation']/b['total']:.0%}, fixed engineering/infra/security {b['fixed']/b['total']:.0%}. "
      "The resolution rate, not the token price, dominates economics.\n")

    w("### Break-even resolution rate (base build case)\n")
    for rr in [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]:
        r = prod_build(replace(PROD["base"], resolve=rr))
        w(f"- resolve {rr:.0%}: total ${r['total']:,.0f} vs human-only ${r['baseline']:,.0f} → saving {r['saving_pct']:.0%}")
    # ---- labour-cost jurisdiction sensitivity (added v1.1) ----
    w("\n## Labour-cost jurisdiction sensitivity (v1.1)\n")
    w("Eurostat hourly labour cost levels, 2025, whole economy excl. public administration, all-in employer cost "
      "(lc_lci_lev, D1_D4_MD5) [S119]: EU27 €34.9, Germany €45.0, Estonia €21.1, Latvia €16.3. Converted at 1.1206 USD/EUR (ECB, 2026-10-09). "
      "**Caveat:** whole-economy averages, not support-agent wages. The US figure is the occupation-specific BLS median × 1.4 (ASSUMPTION).\n")
    w("| Labour cost basis | $/hour | Production base: total $/month | Human-only baseline | Saving | Small-business base: total | Human-only | Saving |\n|---|---|---|---|---|---|---|---|")
    saved = CSR_RATE
    for label, eur in [("US support agent (BLS × 1.4)", None), ("EU27 average", 34.9), ("Germany average", 45.0),
                       ("Estonia average", 21.1), ("Latvia average", 16.3)]:
        CSR_RATE = saved if eur is None else eur * 1.1206
        pb = prod_build(PROD["base"]); sb = smallbiz(SMALLBIZ["base"])
        w(f"| {label} | {CSR_RATE:.2f} | {money(pb['total'])} | {money(pb['baseline'])} | {pb['saving_pct']:.0%} | "
          f"{money(sb['total'])} | {money(sb['baseline'])} | {sb['saving_pct']:.0%} |")
        rows.append(["labour_sensitivity", "claude-sonnet-5.5", label, "prod_saving_pct", round(pb["saving_pct"], 4)])
    CSR_RATE = saved
    w("\nINTERPRETATION: cheaper labour shrinks the *percentage* saving from automation, because fixed engineering, security and model costs "
      "are priced globally (in USD) while the human work replaced is cheaper. An EU/Latvia-based deployment therefore needs a higher resolution rate "
      "to beat an all-human team than a US one. Engineering FTE is held at the US BLS rate in every row; with local engineering salaries the gap narrows (not modelled).\n")
    (OUT / "cost_model_results.md").write_text("\n".join(lines) + "\n")
    with open(OUT / "cost_model_results.csv", "w", newline="") as f:
        cw = csv.writer(f)
        cw.writerow(["scenario", "model", "case", "metric", "value"])
        cw.writerows(rows)
    print("\n".join(lines))


if __name__ == "__main__":
    main()
