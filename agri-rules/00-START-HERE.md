# START HERE: EU agricultural-rules comparison, decision package

*14 October 2026 · Research and planning only. Nothing was bought, no account was opened, no key requested, nothing deployed, published or sent. Each live check was a single request, logged in `evidence/probe-log.txt`.*

## The answer in one paragraph

The project is **feasible to test** and no load-bearing premise has failed:
- Every comparison layer except Italy has a working official route, and Italy's portal exists but its API is unconfirmed.
- None of the four "known concerns" blocks the work.

But the proposal is aimed at the wrong risk:
- **The expensive, uncertain part is human verification, not AI or servers.** A full AI pass over 1,000 cells costs roughly **€18–€1,650** at today's official prices (base **€330**). Checking those cells takes **hundreds of hours**.
- So the first step is to **measure how long a defensible answer takes by hand**, with no server, no n8n and no spend.

## Recommendations

| Topic | Recommendation |
|---|---|
| **Scope** | Redefine "100 rules" as **100 comparison questions**, each with a fixed scope, answer type and reference date. 100 questions × 10 layers = 1,000 cells. Exclude tax and payment rates, forestry and fisheries. Show collective agreements, regional rules and court decisions as separate, labelled layers (02) |
| **Additional country** | **Italy** (79.0/100; third-largest EU farm output, €70.2bn [S33]), **runner-up Denmark** (78.0; best official API). The margin is small: Denmark wins if Italy's API or terms fail in Sprint 0, or if the project stays internal and cheap (03 §D.3). "10th" = the 10th comparison layer, so EU + 9 countries |
| **Pilot architecture** | **Local, code-first, no server**: Python + git + SQLite/files + immutable source snapshots + template HTML→PDF. Remove the server, n8n, Redis, Gotenberg and Caddy for the pilot; defer Postgres and Obsidian (05) |
| **Research and model testing** | Official sources only (Cellar, GII XML, KOOP SRU, DILA LEGI/KALI, BOE API, Riksdagen API, Riigi Teataja API, Sejm ELI API, likumi.lv). Deterministic citation and date checks. A pre-registered **20-question benchmark** against human gold answers, with blind scoring and a **measured** primary/challenger correlation check (06) |
| **Pilot cost and time** | **Sprint 0: €0, ~40 h (23–63).** Full 20-question pilot: AI **~€200** (€11–€990) + optional lawyer spot-check ~€2,600 (assumed rates), **~265 h** (138–490), so ~21 weeks at 12.5 h/week. The proposal's 13 weeks matches only our low case (07) |

## Five largest risks

1. **Human review time per cell** is unknown and drives cost: 0.25–1.0 h/cell means 250–1,000 h for the full build.
2. **Collective agreements and regional rules** make many "national answers" misleading (e.g. Latvia's overtime premium is ≥100 % by statute but may be ≥50 % under a general agreement [S15]).
3. **Outdated or unconsolidated text.** EU Cellar returns original acts unless you ask for the consolidated version [S05]. Several national consolidations are non-official (DE, ES, LV, PL). Rules change mid-project (NL derogation ended 2026; CAP simplification; pending EU fur decision).
4. **Correlated AI errors.** A second model from another company may share the primary's misreading; independence must be measured.
5. **Reuse permission is unknown for some sources** (Estonia's API, Latvia, Poland), and the Dutch law site bans AI crawlers [S26]. That is fine for private research, but a blocker for a client product until resolved.

## Immediate next action

**Sprint 0 (no approval needed, €0):**
- By hand, answer 3 questions (EMP-01 weekly hours, NIT-01 manure nitrogen, AW-01 fur ban) for all 10 layers from official sources.
- Time each cell.
- Record reuse terms for every source.
- Check Italy's and Denmark's access.

Details: 10 §K.1 S0 and §K.4.

## Decisions that can safely wait

- the audience (internal vs client)
- the budget cap
- Italy vs Denmark (Sprint 0 tests both)
- the model choice (the benchmark decides)
- OpenRouter vs direct APIs
- DeepL
- Obsidian
- any hosting
- lawyer engagement (after the pilot PDF)

## Approval gates ahead (🔒)

1. API account + spending cap (benchmark, ~€200).
2. Contacting and paying lawyers.
3. Any server or domain purchase.
4. Any publication or client distribution.

## Reading order

| # | File | Deliverable |
|---|---|---|
| 1 | This page | A. START HERE |
| 2 | [01-verdict-on-proposal.md](01-verdict-on-proposal.md) | B. Verdict on each component and estimate |
| 3 | [02-rule-taxonomy.md](02-rule-taxonomy.md) + [rules/rule-list.csv](rules/rule-list.csv) | C. Taxonomy, 100 questions, 20-question pilot, trap cases |
| 4 | [03-source-matrix.md](03-source-matrix.md) | D. Official-source matrix, concern checks, country selection |
| 5 | [04-tools-models.md](04-tools-models.md) | E. Tool, service and model matrix; OpenRouter; search |
| 6 | [05-architecture.md](05-architecture.md) + [schema/](schema/cell-record.schema.json) | F. Architecture options, data flow, data model |
| 7 | [06-benchmark-protocol.md](06-benchmark-protocol.md) + [benchmark/](benchmark/) | G. Executable benchmark protocol + scorer |
| 8 | [07-cost-timeline.md](07-cost-timeline.md) + [models/](models/) | H. Cost and time model with formulas |
| 9 | [08-legal-quality-plan.md](08-legal-quality-plan.md) | I. Legal quality, sampling, security, client caveats |
| 10 | [09-pdf-workspace-spec.md](09-pdf-workspace-spec.md) | J. PDF and workspace specification |
| 11 | [10-plan-30-60-90.md](10-plan-30-60-90.md) | K. Staged plan, gates, 30/60/90 days, continue/stop rules |
| 12 | [11-decision-menu.md](11-decision-menu.md) | L. Decision menu |
| 13 | [12-evidence-ledger.md](12-evidence-ledger.md) + [evidence/](evidence/) | M. Evidence ledger, sources, probe log |

## Labels

**VERIFIED FACT** (read in the official source today, [S##]) · **CALCULATION** (script in `models/`, rerunnable) · **ASSUMPTION** (our input; the pilot must measure it) · **INTERPRETATION** (judgement) · **RECOMMENDATION** · **UNKNOWN** (looked for; not found). Nothing here is legal advice.
