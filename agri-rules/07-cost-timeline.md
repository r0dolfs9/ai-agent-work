# H. Cost and timeline model

*14 October 2026. All money is in EUR excluding VAT unless stated. FX: 1 EUR = 1.1188 USD (ECB, 13 Oct 2026) [S47]. Prices are official and verified [S34–S43], **except** the server (€36/month) and DeepL, which are UNVERIFIED. Token counts, hours and rates are ASSUMPTIONS until the pilot measures them. Regenerate the money figures with `python3 agri-rules/models/cost_model.py` (output: [`models/cost_model_results.md`](models/cost_model_results.md)).*

## H.1 Formulas

- **Cells** = questions × layers. Full build = 100 × 10 = 1,000.
- **AI € per pass** = Σ over stages [units × (tokens_in × price_in + tokens_out × price_out) ÷ 10⁶ × token multiplier × retry factor × batch factor] × (1 + 5.5 % OpenRouter fee) ÷ 1.1188.
  - units = cells for the 5 per-cell stages, questions for the 3 per-question stages.
- **Search €** = cells × queries per cell × $5 ÷ 1,000 ÷ 1.1188.
- **DeepL €** (optional; UNVERIFIED price) = cells × 3,000 characters ÷ 10⁶ × €20.
- **Hours** = gold cells × gold h/cell + reviewed cells × review h/cell + fixed build/analysis hours (H.3).
- **Lawyer €** = lawyer-reviewed cells × 0.75 h × rate. Rates of €100 / €175 / €250 per hour are an ASSUMPTION; no quote was requested, because contacting suppliers is out of scope.
- **VAT:** Latvian 21 % applies if the buyer is not VAT-registered; a registered business self-assesses foreign B2B services under reverse charge (repo claims-ledger L50). Shown separately.

## H.2 Scenario inputs

| Input | Low | Base | High |
|---|---|---|---|
| Primary / challenger model | haiku-5.5 / gemini-3.5-flash-lite | sonnet-5.5 / gemini-3.1-pro | opus-5.5 / gpt-6-astra |
| Token multiplier on stage defaults (≈55k in / 8k out per cell, incl. a 1/10 share of the per-question stages) | 0.6 | 1.0 | 2.0 |
| Retry factor | 1.15 | 1.35 | 1.6 |
| Batch discount | 50 % | none | none |
| Search queries per cell | 3 | 5 | 10 |
| Gold-standard hours per cell | 0.5 | 0.9 | 1.5 |
| Review hours per cell | 0.25 | 0.5 | 1.0 |
| Lawyer rate €/h | 100 | 175 | 250 |

## H.3 Results by phase

AI figures come from the model; hours combine the model with fixed-task ASSUMPTIONS listed in the "fixed hours" column.

| Phase | Money low / base / high (€ ex VAT) | Hours low / base / high | Fixed hours included | Weeks at 12.5 h/week (low / base / high) |
|---|---|---|---|---|
| **0. Source-feasibility sprint**: 3 questions × 10 layers by hand (EMP-01, NIT-01, AW-01), access terms, authority map | **€0** / €0 / €0 | 23 / 39 / 63 | 8 / 12 / 18 (terms, authorities, write-up) | 2 / 3 / 5 |
| **1. 20-question pilot**: 100 gold cells, AI on 200 cells × 3 candidate pipelines, review, PDF prototype | AI **€11 / €198 / €993**; + optional lawyer spot-check of 20 cells €1,500 / €2,625 / €3,750 | 138 / 265 / 490 | build 20/40/80; scoring 10/20/30; PDF 8/15/30 | 11 / 21 / 39 |
| **2. First 100-question build** (1,000 cells) | AI **€18 / €330 / €1,654**; lawyer on 100 cells €7,500 / €13,125 / €18,750 | 300 / 600 / 1,190 | hardening 40/80/150; coordination 10/20/40 | 24 / 48 / 95 |
| **3. One complete refresh** (30 % of cells changed) | AI €6 / €99 / €496; lawyer €2,250 / €3,938 / €5,625 | 75 / 150 / 300 (review only) | — | 6 / 12 / 24 |
| **4. Monthly maintenance** (10 / 30 / 80 changed cells per month) | AI €0.2 / €9.9 / €132 per month | 2 / 15 / 80 h per month | — | — |

**Reading the table:**
1. **Model spend is not the main cost; human time is.** In the base case, AI (€330 per full pass) is under 3 % of the 600 review hours valued at even €20/h (€12,000). In the high case it is ~7 % (€1,654 vs 1,190 h × €20).
2. The proposal's **€590 per run** sits between our base (€330) and high (€1,654) and cannot be confirmed or rejected until tokens are measured.
3. The proposal's **pilot of 13 weeks at 10–15 h/week (130–195 h)** matches only our *low* case. A base estimate is ~265 h (~21 weeks at 12.5 h/week), because gold-standard creation and double rating are not optional if the benchmark is to mean anything.
4. The proposal's **first three months ≈ €1,700 (€320–€5,100)** is plausible as money (pilot AI + an optional lawyer spot-check ≈ €2,800 base), but not as calendar time.
5. **Full coverage, 24 weeks (11–68):** our range is 24–95 weeks at 12.5 h/week. Review time per cell is the single most influential unknown.

## H.4 Infrastructure (pilot vs later)

| Item | Pilot (Option 3) | Full build / internal | Client-facing product |
|---|---|---|---|
| Server | €0 (local PC) | €0–€36/month (UNVERIFIED) only if scheduled monitoring is wanted | Required, plus hardening hours |
| Storage and backups | git remote (private) + one local/offline copy of snapshots | Same + scheduled backup | Off-site encrypted backups + restore tests |
| Domain | none | none | UNKNOWN price (not checked) |
| Monitoring | run logs | change-feed polling script | uptime + alerting |
| Legal review | optional spot-check | sample (08 §I.4) | **Every released cell for sold jurisdictions** (08) |
| Insurance (professional liability) | — | — | UNKNOWN; needs a broker quote (owner action, later) |

## H.5 Internal vs client-facing costs that only the client product incurs

- Lawyer review of every released cell (≈ €13k base for 1,000 cells at the assumed rate)
- Liability insurance (UNKNOWN)
- Terms of use and disclaimer drafting (UNKNOWN)
- GDPR documentation if any client or user data is held
- Commercial n8n licence, if n8n were used [S44]
- Uptime and security hardening hours
- Accessibility testing of the PDF
- Faster refresh service levels (e.g. update within X days of a gazette change), which roughly doubles maintenance review hours (ASSUMPTION)

## H.6 What the pilot must measure before any full-run forecast is reliable

1. Tokens in/out per stage (median, p90) for each candidate.
2. Retry and failure rates per stage.
3. **Gold minutes per cell by layer**: expect IT/ES/FR (regional or collective-agreement layers) to be slower.
4. **Review minutes per cell by stage verdict.** This decides whether PASS stages can drop to sample review.
5. Critical-failure rate of the chosen pipeline, which sets the size of the production review sample.
6. Share of cells whose answer is "depends on collective agreement / region". These cells need variant rows, so 1,000 cells may really be ~1,300 answer rows.
7. Change rate per month from the official change feeds (ES/EE/PL/DK APIs), which sets maintenance cost.
