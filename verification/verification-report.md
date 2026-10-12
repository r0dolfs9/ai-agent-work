# Verification report

Date: 2026-10-12. Reviewer for v1.0 and v1.1: the same AI system that wrote the paper (**self-review**). **v1.2 added two independent AI reviewers** (factual and commercial; see the v1.2 section at the end). No human expert review has taken place.

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

---

# v1.1 verification (limitations follow-up, 2026-10-12)

Reviewer: the same AI system (**self-review**). No independent reviewer was used, because the owner did not request one and none was authorised.

## A. Automated checks

| Check | Command | Result |
|---|---|---|
| Citations resolve (121 registered sources; 111 cited; 10 superseded, removed or background) | `python3 paper/build_paper.py` | **Pass** |
| v1.0 cost figures unchanged and still match | `python3 -I verification/check_numbers.py` | **Pass, 44/44** |
| v1.1 figures (labour sensitivity, operator economics, AIDev, opportunity scores) + 5 arithmetic checks | `python3 -I verification/check_numbers_v11.py` | **Pass, 32/32** |
| Models and register regenerate | `python3 models/cost_model.py`; `python3 models/operator_economics.py`; `python3 opportunities/build_register.py` | **Pass** (deterministic) |
| AIDev analysis reproducible | `research/analysis/aidev_timing.py` (needs pyarrow and fsspec; reads two columns of a public CC-BY parquet over HTTP) | **Pass**. Results in `research/analysis/aidev_timing_results.md` |
| Link check (read-only GET) | `python3 -I verification/check_links.py` | 98 OK, 20 blocked to automated clients, 3 errors (the McKinsey .com URLs, which refuse connections from this environment; their content was read on the McKinsey-hosted mirror) |

## B. Adversarial review (v1.1)

| # | Attempt to disprove | Finding | Action |
|---|---|---|---|
| V1 | *Is the use of alternative publisher hosts (gcom.pdo.aws.gartner.com, karriere.mckinsey.de) a bypass of anti-bot protection?* | These are the publishers' own domains, surfaced by ordinary search, serving the same public press pages without login, spoofing or any circumvention. www.gartner.com returns 403 to automated clients. mckinsey.com produced connection errors, not a block page | Treated as a lawful alternative access path and **disclosed** in the source register and §14. **Owner decision point:** if you consider this inappropriate, the affected citations (S082–S087, S098) revert to "search extract" status. The conclusions would not change, but their confidence would drop to medium |
| V2 | Strongest global-market claim: "AI agents market" numbers | Gartner's own figures differ ~30× by definition. Analyst 2030 figures converge from divergent bases. McKinsey's scenario method is undisclosed | Market numbers are kept in the paper only as definitional illustrations, labelled weak |
| V3 | Universal agent buying behaviour | No new evidence of a stable preference. Accenture's 16-country survey supports the gap between selecting and paying | Conclusion retained |
| V4 | Validity of the activity metric (AIDev) | (a) PR creation is the *end* of a run; (b) 75% is OpenAI Codex, so the profile is dominated by one product; (c) there is no human-PR baseline, and human GitHub activity is also globally distributed, so "flatness" cannot be attributed to autonomy; (d) agent attribution heuristics miss untagged work | All four caveats are stated in §10.2. The interpretation is limited to "consistent with a global user base and some unattended runs". No claim about autonomy share is made |
| V5 | Validity of the enforcement metric | Anthropic's ban counts are all-cause, with no denominator. The 10.6% overturn rate is appeals-based, not a ban error rate | Stated explicitly. No ban *rate* reported |
| V6 | Validity of purchase metrics | x402 volume ≠ purchases (it includes scripts). TRM's agentic share is heuristic. Visa's adjustment method is undisclosed. Units differ across rows | The table states units and autonomy levels. No summation. "Global total unknown" |
| V7 | Feasibility of the leading opportunities from Latvia | B2B services are feasible (reverse charge, no consumer-law withdrawal). O02 requires a GDPR processor role (friction) | O02 risk score lowered. Others unchanged. Demand is still unvalidated |
| V8 | Unrestricted cross-border operation | Disproved as stated: sanctions (Art. 5n), provider-unsupported countries, PSD2 licensing for client funds, non-EU indirect taxes and high-risk AI uses all restrict it | §15.1 verdict: "supported with conditions, not unrestricted" |
| V9 | Tax interpretation risk (s.59(6) → VAT registration → micro-enterprise regime unavailable) | Based on an English translation explicitly marked outdated (valid 2024). The 2025 amendments changed the threshold test. Paragraphs (4) and (6) may also have changed | Marked ⚖ everywhere, listed first in §15.9, recorded as conflict C019 and unknown U08 |
| V10 | Alternative CIT regime calculation shows no advantage, which is suspicious | Likely reflects features not captured by the summaries | Flagged ⚖ (C020). No recommendation made |
| V11 | Currency consistency | Operator economics in EUR. Cost model in USD. Conversions use the ECB rate of 1.1206 (2026-10-09), stated in both | OK |
| V12 | Effective dates | AI Act dates read from the Commission page (updated 2026-08-03). PLD 9 Dec 2026 from secondary sources. E-invoicing 2028 from secondary sources | Confidence labels set accordingly |
| V13 | Source independence | Bloomberg and Reuters ($65bn) share one anonymous source. TRM and Visa use overlapping onchain data but independent methods. Talon.One and CNBC coverage of the OpenAI quote both derive from OpenAI's post | Independence limits stated. No double counting |
| V14 | Consistency across artifacts | Opportunity scores in the paper (§12.4) match the register. Labour-sensitivity and operator figures match the model outputs (automated check) | OK |

**No critical unsupported claim was found to remain** after the fixes above. The highest residual risks are V1 (access-path judgement) and V9 (Latvian VAT interpretation).


## v1.2 verification (decision package, 2026-10-12)

### V12.A Automated checks

| Check | Command | Result |
|---|---|---|
| Paper citations resolve | `python3 paper/build_paper.py` | **Pass.** 127 cited sources, 0 unresolved (141 registered) |
| v1.0 cost figures | `python3 -I verification/check_numbers.py` | **Pass.** 44/44 |
| v1.1 figures (against the preserved v1.1 snapshot in `archive/v1.1/`; v1.1 wording was deliberately revised) | `python3 -I verification/check_numbers_v11.py` | **Pass.** 32/32 |
| v1.2 figures: brief, economics, dossiers and paper vs `models/route_economics.py`; tax arithmetic; register ranks; labour table; package citations | `python3 -I verification/check_numbers_v12.py` | **Pass.** See the final run in HANDOFF |
| Dossier economics tables | generated from the model by `package/build_package.py` | Regenerated on every build |
| Rendered edition | Headless Chromium at 1280 px and 390 px: anchors, horizontal overflow, table count, screenshots | No broken in-page anchors. No page-level horizontal overflow at 390 px after the fix: wide tables scroll inside their own container, and long URLs wrap |

### V12.B Independent reviews (two separate AI agents, read-only)

- **Factual reviewer.** About 30 claims re-checked at source, including the Latvian statute text, VID guidance, the SEC filing, Anthropic, Visa, TRM, Eurostat and price sources.
  - **Findings:** 0 critical, 3 major, 8 minor. All fixed.
  - **Most material:** the self-employed contribution rule below €780 per month. **Verified by us** against the S125 record before the model was changed.
- **Commercial reviewer.** Challenged the recommendation, demand assumptions, economics, plans and legality.
  - **Findings:** 2 critical, 7 major, 3 minor. All addressed.
  - **Most material:** cold B2B email to Germany. **Verified by us** via German chamber-of-commerce guidance [S139] before the plans were changed.
- **Full table:** `package/06-review-and-open-questions.md` §3.

### V12.C Adversarial review (required challenges)

Covered in `package/06-review-and-open-questions.md` §2:
- the strongest market claim;
- the leading recommendation;
- the weakest demand assumption;
- adverse-scenario economics;
- feasibility without credentials or access;
- whether the actual work is explained concretely.

### V12.D Corrections of earlier versions

- **v1.1 Latvian VAT conclusion withdrawn** (claims ledger L51 → L65, L52 → L66, C021).
- **v1.1 access path withdrawn.** Owner decision point V1 (publisher alternative hosts) is resolved: provenance established [S137], origin-host use discontinued, and the key figure corroborated through an independent republication [S136].
- **v1.2 draft economics revised after review.** The base case is now a newcomer, and the adverse case includes ramp and fee shocks.

### V12.E What could still be wrong

- **Route inputs** (prices, win rates, hours) are assumptions. They are the most decision-relevant unknowns.
- **Consolidated Latvian texts** are informative only; the official publication prevails. Reported 2026 changes to minimum contributions are unverified.
- **Commercial evidence** relies on list prices and vendor guides, not transactions.
- **The reviews** were performed by AI agents, not human professionals.
