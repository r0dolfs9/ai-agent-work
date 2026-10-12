# Cost model — assumptions register

Reproduce with `python3 models/cost_model.py`. The script writes `cost_model_results.md` (tables) and `cost_model_results.csv` (machine-readable). Every number in the paper's cost section comes from these files.

## Dated prices (VERIFIED FACT, retrieved 2026-10-12, USD, excl. tax)

| Item | Value | Source |
|---|---|---|
| Claude Haiku 5.5 in / 5m-cache write / cache read / out per MTok (prompts ≤100k) | 0.10 / 0.125 / 0.01 / 0.50 | S044 |
| Claude Sonnet 5.5 | 2.00 / 2.50 / 0.10 / 10.00 | S044 |
| Claude Opus 5.5 | 4.00 / 5.00 / 0.20 / 20.00 | S044 |
| Claude Fable 5.1 | 10.00 / 12.50 / 0.25 / 50.00 | S044 |
| GPT-5.5 in / cached in / out (≤272K) | 5.00 / 0.50 / 30.00 | S045 |
| GPT-5.4-mini | 0.75 / 0.075 / 4.50 | S045 |
| Gemini 3.1 Pro Preview in / cache / out (≤200k) | 2.00 / 0.20 / 12.00 (+$4.50/h cache storage, ignored) | S046 |
| Web search tool | $10 per 1,000 searches (Anthropic, OpenAI) | S044, S045 |
| Batch API discount | 50% (all three providers). **Not applied** in the scenarios, which are interactive. | S044–S046 |
| Claude Pro / Max subscriptions | $20 / from $100 per month | S047 |
| Intercom Fin | $0.99 per outcome; seats $29/$85/$132 | S071 |
| LangSmith Plus | $39/seat/month | S048 |
| US median customer-service wage | $21.53/h (May 2025) | S077 |
| US median software developer salary | $135,980/yr (May 2025) | S078 |

## Modelling assumptions (ASSUMPTION — change them in the script)

| Assumption | Value | Rationale / how to falsify |
|---|---|---|
| Context growth | Linear: each loop step appends `delta` tokens (tool results plus prior output) | Typical ReAct-style loop. Measure from your own traces (`usage` fields). |
| Caching | The previous step's prefix is read from cache at rate `cache_hit`. New tokens are billed at the 5-minute cache-write price (OpenAI/Google: input price). | Provider caching is prefix-based (S044 docs). Real hit rates depend on prompt stability. |
| Thinking tokens | Included in `out` per step | Reasoning models bill thinking as output. |
| Loaded labour multiplier | 1.4 × wage | Wages are commonly ~70% of total employer cost. Not sourced. Replace with your own payroll data. |
| Contractor rate | $90/h | Placeholder for a freelance automation builder. Highly variable by region. |
| Personal agent retries | A failed task is retried once | A simplification. Real users may abandon or fix by hand. |
| Small business | A human reviews **every** draft (human-in-the-loop). Rejected drafts need extra fix time. | Matches governance guidance to keep humans approving outbound communications (S051, S052). |
| Production escalation | Escalated conversations take as long as or longer than human-only handling | Escalations skew to harder cases and require reading the agent transcript. |
| Engineering FTE | 0.5 / 1 / 2 FTE to build, evaluate and maintain at 50k conversations/month | No public benchmark found (gap G-COST-1). |
| Security/compliance | $15k / $40k / $100k per year | Placeholder for a red-team engagement plus compliance review. No public price list (gap G-COST-2). |
| Resolution rate | 65% / 50% / 35% | Vendor claims vary widely, and no independent benchmark of production resolution rates was found (gap G-COST-3). Klarna's partial reversal (S072) and RLI (S037) caution against high values. |
| Model swap holds success constant | Yes, in the model-choice table only | This is unrealistic, and the paper says so. |

## What the model does not include

- VAT or sales tax.
- Currency conversion.
- Payment processing fees.
- Legal review of terms.
- Insurance premiums (AIUC-type cover pricing is undisclosed, S061).
- Opportunity cost of the owner's time in the personal case. Hours are reported, not priced.
- Cost of incidents (data leak, wrong refund).
- Vendor price changes over the year.
- Volume discounts or committed-use contracts.
- Cache-storage fees on Gemini.

The incidents line is potentially the largest omitted cost. Treat it qualitatively using the failure-mode section of the paper.
