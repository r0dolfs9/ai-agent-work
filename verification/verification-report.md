# Verification report

Date: 2026-10-12. Reviewer: the same AI system that wrote the paper (**self-review**). No independent human or second-model review took place, because the session had no explicit authorization to spawn reviewers. The owner should arrange an independent review before any publication.

## 1. Automated checks (reproducible)

| Check | Command | Result |
|---|---|---|
| Every `[S###]` in the paper resolves to the source register | `python3 paper/build_paper.py` | **Pass.** 81 of 81 registered sources cited, 0 unresolved |
| Paper cost figures equal model output | `python3 -I verification/check_numbers.py` | **Pass.** 44/44 figures match `models/cost_model_results.md` |
| Cost model reproduces | `python3 models/cost_model.py` | **Pass.** Deterministic output |
| Opportunity ranking reproduces and matches the paper's §12.4 table | `python3 opportunities/build_register.py` | **Pass.** Scores 71/70/69/66/64 (top 5), 44 and 36 (lowest) match the paper |
| Source register is well-formed CSV (12 columns) | `research/tools/add_sources.py` validation + csv parse | **Pass** |
| Link destinations (read-only GET) | `python3 -I verification/check_links.py` → `verification/link-check.csv` | 65 OK. 12 blocked to automated clients (403/503: Gartner, OpenAI, CNBC, White & Case and similar). 4 connection errors: 3 McKinsey URLs refuse this environment's connection (HTTP/2 stream errors; search engines index them), and LessWrong resolved on HTTP/1.1 retry. **0 confirmed dead links** |
| Unlabelled numeric claims scan | ad-hoc regex scan (see session log) | 24 hits. All are inside §6 tables that are introduced as CALCULATIONS, or restate cited figures. No unsourced factual numbers remain |

## 2. Manual checks

- **Dates.** Every product, price and policy date was re-read against the source register entry. Where sources conflicted (C003–C013), the paper states the conflict or uses the most primary source.
- **Pricing.**
  - Anthropic prices come from the official pricing page (full markdown retrieved). OpenAI and Google prices come from their official pricing pages, retrieved the same day.
  - The cached-input price on OpenAI and Google is used as the "cache read" price. Their cache-write premium is assumed to be zero, which is a simplification stated in the script.
- **Scope.** All nine research areas from the assignment are covered in the paper, or have an explicit gap entry (`research/coverage-matrix.md`).
- **Readability.** Jargon is defined at first use or in the glossary. Technical material is moved to appendices. The executive summary is readable without the body.

## 3. Adversarial review: challenges raised and how they were resolved

| # | Challenge | Finding | Action |
|---|---|---|---|
| R1 | "People, not tokens, are the biggest cost" may be an artefact of assumptions | True only where humans review or escalate. The heavy personal case is token-dominated ($4,600/month API) | Exec summary point 4 narrowed to "in business deployments" and the exception stated |
| R2 | Is "agentic commerce is mostly discovery" contradicted by live checkout in AI surfaces? | Google UCP checkout is reported live in the US, but the shopper still confirms. Network pilots are real but small | Added the UCP checkout bullet to §9.2. Claim kept, with the wording "autonomous buying" |
| R3 | Cloudflare default stated as fact although implementation was not confirmed | Correct concern | Exec summary changed to "announced that from 15 September 2026…". §11.3 notes it was not independently confirmed |
| R4 | Ninth Circuit summary overstated ("did not hack") | The holding is about likelihood of success on CFAA/CDAFA claims at preliminary-injunction stage | Reworded in the exec summary, with contract claims flagged as open |
| R5 | "No stable buying preference" could be an over-generalisation from 2025 models | The evidence covers specific models and mock markets. Future convergence is possible | Stated as "no evidence supports one", with the confidence explained. Kept the distinction between bias and preference |
| R6 | Top opportunity (security services) might be invalidated by vendor bundling (Entra Agent ID, guardrail products) and by agencies advising SMEs to keep agents to low-risk tasks, which reduces demand | Plausible counter-evidence | Recorded in the register's competitors/failure fields. Ranking margin over #2–#3 is ≤2 points, so not meaningfully different |
| R7 | Rubric bias toward services | The zero-budget assumption favours low-capital ideas | Disclosed in §12.4 and in the register header |
| R8 | Market numbers in the exec summary (Anthropic $65bn) are run-rates via press | Correct | Labelled "reported" and "not GAAP" |
| R9 | METR doubling time quoted precisely by secondary sources | Conflicting figures | The paper avoids a precise doubling figure (C003) |
| R10 | Survey adoption figures conflated | Different questions and populations | §2.2 table separates them (C001) |
| R11 | Incident list includes CVEs not verified against NVD | Correct | Marked low confidence, sourced to the aggregator S081 |
| R12 | Claims of Five-Eyes recommendations beyond the summary page | Detailed recommendations came from secondary CSA notes | The paper limits itself to "layered defence and strict access controls", quoted from the agency page |
| R13 | Coding-agent revenue implies productivity | Revenue ≠ productivity. RCTs are inconclusive | §4.3 and §12.5 make the distinction |
| R14 | Theoretical vs demonstrated vs production | Checked each capability claim | Protocol "status" uses explicit categories (§8.1). Commerce claims distinguish pilots from volume |
| R15 | Cost model holds success constant across models | Unrealistic | Flagged next to the table and in `models/README.md` |

**No critical unsupported claim remains** to the best of this self-review. Residual weaknesses are listed below.

## 4. What remains unknown or weak

See `research/claims-ledger.md` §C (U01–U07) and the coverage-matrix gaps. Most important:
1. Independent production resolution rates (drives every business case).
2. Value of agent-completed purchases.
3. Timing patterns of autonomous agents.
4. Ban frequencies and appeal outcomes.
5. Liability rules for agent payments.
6. EU/Baltic-specific market data.

## 5. What could invalidate the conclusions

- A major vendor publishes audited production resolution or reliability data far above (or below) our assumptions. That would move every cost scenario.
- Card networks publish agentic transaction volumes showing material autonomous purchasing. That would upgrade the commerce opportunities (O08, O09, O12) and weaken the "discovery, not buying" finding.
- A breakthrough defence against prompt injection, demonstrated by independent red-teams. That would relax the security constraint and lower the value of opportunity O03.
- Platforms open sanctioned agent access widely (e.g., Amazon agent APIs). That would reduce platform risk.
- Courts or regulators assign liability for agent purchases. That would shape the payments opportunities.
- Analyst methodology for market sizing becomes public and robust. That would raise confidence in §12.1.

## 6. Access limitations encountered

- Gartner, OpenAI, CNBC and White & Case pages: HTTP 403 to automated retrieval.
- McKinsey: connection errors from this environment.
- These were handled with search-engine extracts of the primary, marked as `search-extract` in the register.
