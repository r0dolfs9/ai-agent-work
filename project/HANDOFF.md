# Progress log and handoff

## Feasibility study: EU vs Latvian rules by industry with AI agents (2026-10-13)

The owner asked whether AI agents could compare EU rules with Latvian law for an industry, starting with agriculture. They wanted to know the setup costs, time, result quality, certainty, negatives and how to prevent them, plus a provisional timeframe.

| Stage | Inputs | Verification | Output |
|---|---|---|---|
| Evidence | EU Publications Office SPARQL (Cellar); likumi.lv; TAP open data (data.gov.lv CKAN); studies on legal-AI accuracy; Latvian regulators and Saeima | Queries saved and re-run; counts re-derived from saved CSVs; one near-miss (single-property NIM query) caught and corrected | Sources S142–S164 |
| Model | Anthropic prices [S044]; ECB rate 1.1206 | `check_numbers.py`: every README figure equals model or query output (0 failures) | `cost_model.py` → results .md/.csv |
| Scope | 49 candidate core EU acts | All confirmed in force via SPARQL | `pilot-scope-agriculture.md` (generated) |
| Writing | — | All 24 cited source IDs resolve; all new IDs cited | `feasibility/eu-lv-regulatory-comparison/README.md` |

HANDOFF (feasibility study)
GOAL: Answer the owner's feasibility question for an AI-agent system comparing EU rules with Latvian law by industry, with agriculture as the pilot.
STATE: Complete as a research and planning document. Nothing built, bought or sent.
- Base pilot: about €63k (range €19k–€275k), about 98% of it people.
- Proof of concept: about €28k (range €10k–€96k).
- AI usage: about €1k.
- Time: about 17 weeks (range 11–25).
VERIFIED:
- **EUR-Lex counts:** 8,293 in-force acts in chapter 03. 208 of 270 agriculture directives have Latvian NIM records, 428 records in total.
- **MK No. 834:** in force, amended 5 times. MK No. 33: repealed 2015-01-08.
- **TAP annotations:** CC0 open data, Sep 2021–Sep 2026. Section 5.4 conformity table confirmed in a real agriculture annotation.
- **Copyright:** Art. 6 of the Copyright Law excludes official texts.
- **Latvian deviations, all read at source:**
  - UTP law scope [S155][S164];
  - fur-farming ban from 2028 [S157];
  - MON 810 exclusion [S158].
UNVERIFIED:
- **Model inputs:** all model inputs except prices are assumptions, including reviewer rates, minutes per finding, tokens per step and manual hours.
- **Legal-AI evidence:** S153, S154 and S160 were read via search extracts.
- **Latvian datasets:** the Ministry of Justice transposition dataset (S149) was unreachable.
- **IED 2024/1785:** whether Latvia has transposed it (no NIM record on 2026-10-13) is unknown.
BLOCKERS: Owner decisions:
- (1) Does "European standard rules" mean EU legislation (assumed), technical standards, or both?
- (2) Is the register for internal research or a client product? This sets reviewer level and cost case.
NEXT: If approved:
- Engage a reviewer.
- Run the proof of concept: nutrients, plant protection, farm-animal welfare; 10 acts; gold set of about 200 provisions.
- Apply the Gate 1 thresholds in README §6.
- Replace the model assumptions with measured figures.
FILES:
- **New:** `feasibility/eu-lv-regulatory-comparison/` (README, cost_model.py + results, build_scope.py, pilot-scope-agriculture.md, check_numbers.py, data/queries, data/results, data/run_queries.sh).
- **Updated:** `research/sources.csv` (S142–S164), `research/bookmarks.html`, `README.md`, `paper/build_paper.py` (S142+ excluded from the paper's background-source line; paper.md unchanged).
DO NOT REPEAT:
- The next source ID is S165.
- Query NIM links on BOTH `measure_national_implementing_implements_resource_legal` and `..._implements_directive`.
- Do not treat EUR-Lex NIM lists as current law; check status on likumi.lv.

## v1.2: reading and decision package (2026-10-12)

| Stage | Inputs | Verification | Output |
|---|---|---|---|
| Inspect | v1.1 paper, register, models, ledger, verification report | Read directly. The handoff was treated as navigation only | v1.1 preserved in `archive/v1.1/` + local tag `v1.1` |
| Evidence | Current Latvian VAT and micro-enterprise law, VID guidance, 2026 contributions, Eurostat SES, SEC 8-K, price sources, re-reads of Anthropic, Visa, TRM and Atlas | Read at source; provenance check of alternative hosts | S122–S141; v1.1 VAT claim corrected; origin-host path discontinued |
| Analysis | Register rescored, with an entry gate; new `models/route_economics.py`; occupation-adjusted labour | Deterministic models; `check_numbers_v12.py` | O13 added; R1–R5 economics |
| Writing | — | Two independent AI reviews (factual and commercial); findings verified and applied | `package/` (START HERE, brief, 4 dossiers, economics, validation plans, review), paper v1.2 |
| Rendering | pandoc; Chromium | Screenshots at 1280/390 px; anchor and overflow checks | `package/reading-edition.html`, `paper/paper.html` |
| Delivery | — | All check scripts pass | **Local commit only; not pushed** (owner instruction) |


## v1.1: limitations follow-up (2026-10-12)

| Step | Outcome |
|---|---|
| Inspect | v1.0 artifacts read. Prior version preserved in `archive/v1.0/` and annotated git tag `v1.0` → commit 783cee5 (tag local unless pushed) |
| List affected claims | Claim-level list in `research/limitations-resolution.md` §2 (14 claims) |
| Research | 37 new sources plus 3 low-confidence secondaries (S082–S121). Superseded entries annotated, not deleted |
| Original analysis | `research/analysis/aidev_timing.py`: timing of 2,743,854 agent-authored PRs (public CC-BY dataset) |
| Models | Labour-cost jurisdiction sensitivity added to `models/cost_model.py`. New `models/operator_economics.py` |
| Paper | v1.1. Exec summary rewritten (11 findings). §2.2, §9.2, §9.6, §10, §11.3.1, §11.4, §12, §14 revised. §6.9 and §15 added. Glossary split into its own file |
| Registers | Claims ledger D.1–D.4. Coverage matrix v1.1 rows. Opportunity register v1.1 fields and score changes (O02, O06, O08, O09) |
| Verify | Citations 111/111 resolve; 44/44 v1.0 + 32/32 v1.1 figure checks; link check 98 OK / 20 bot-blocked / 3 McKinsey connection errors; self-review V1–V14 |

## Earlier history
- v1.0 completed the same day (commits 50c66ab → 783cee5). See `archive/v1.0/` and the v1.0 section of `verification/verification-report.md`.


---

HANDOFF
GOAL: Deliver a finished reading and decision package. It must answer whether there is a credible AI-agent opportunity for the owner to explore, which route to try first, and how to test it without committing to a business. Fix weak v1.1 claims, above all Latvian VAT and the tax regimes. Rebuild the commercial shortlist around realistic entry. Provide the decision brief, the full integrated paper, route dossiers, economics and prepared validation plans, plus Markdown originals and a combined HTML edition.
STATE: v1.2 COMPLETE as a local reading and decision package, committed locally on branch `claude/amazing-archimedes-w4pw0c`. **Not pushed** (owner instruction). Nothing was published, sent, bought or opened; no one was contacted.
- **Recommendation (conditional):**
  - explore R2 (coding-agent enablement with measurement) if the owner codes professionally, ideally with warm access to engineering leads;
  - otherwise R4 (small AI workflow automations) as paid practice, or learn first;
  - R1 (limited agent risk review; not an audit or certification) only with security credentials;
  - R3 deferred;
  - products bought by agents rejected for now.
- **Economics (newcomer):** about €3–11 per owner-hour in the first year after tax, against about €23–36 with a network. The adverse first year is a loss on every route. Access to buyers matters more than the route.
VERIFIED:
- **Citations and checks:**
  - `python3 paper/build_paper.py`: 127 cited sources resolve (141 registered).
  - `check_numbers.py` 44/44; `check_numbers_v11.py` 32/32 (against the archived v1.1 snapshot); `check_numbers_v12.py` 185/185.
- **Latvian law** read in the current consolidated Latvian text (VAT Law s.59(1)/(4)/(8)/(9), s.139²; Micro-enterprise Tax Law s.4, s.6) and the VID guidance of 27 Jun 2025. Independently re-read by the factual reviewer.
- **Re-read at source on 12 Oct:** Anthropic $47bn run-rate (28 May 2026) and Claude Code $2.5bn (Series G); Anthropic bans (11.4M / 398k / 42k, H1 2026); Visa x402 ($15.0M / 109.6M transactions to 21 Apr 2026); TRM (0.6–7.5%, $5–11k/month); Atlas shutdown (9 Aug 2026, trade press); Upwork 8-K; KPMG 80%; Eurostat SES; KPMG tax card (employee contributions 10.5%).
- **Two independent AI reviews** completed (factual: 0 critical / 3 major / 8 minor; commercial: 2 critical / 7 major / 3 minor). One material claim from each was verified by us before acting: the S125 contribution rule, and the German UWG email-consent rule [S139]. All findings were addressed.
- **Rendered HTML** checked in headless Chromium at 1280 and 390 px: no broken anchors and no page overflow.
UNVERIFIED:
- **Route inputs:** all prices, win rates, selling and delivery hours, and months to first sale are assumptions. No customer has been asked.
- **Single-source or blocked figures:**
  - Upwork "~$330M AI-related GSV" (search extract);
  - Gartner primary page (403; corroborated via republication);
  - UWG statute text (gesetze-im-internet.de 503; chamber guidance used);
  - Upwork fee page (403; competitor blog used).
- **Latvian rules:** reported 2026 changes to minimum contributions; whether contributions are deductible before PIT (model uses general practice); marketplace VAT treatment.
- **Unpriced items:** professional-indemnity insurance price; bookkeeping costs.
- **Review coverage:** no human expert review.
- **Link check:** not re-run in v1.2 (the new sources were fetched individually in this session).
BLOCKERS: None for the package. Owner decisions needed (at most two):
- (1) Choose option 1–4 in the decision menu (`package/01-decision-brief.md` §10). If 1 or 2, approve, edit or reject the drafted outreach.
- (2) State whether you have warm access to buyers (about 10 engineering leads, or security/support contacts).
NEXT:
- (1) The owner reads `package/00-START-HERE.md` and makes the decision above.
- (2) If approved, run Phase A of V2 or V4. It needs no approval: self-check, proof pilot or demos.
- (3) Phase B only after explicit approval of each listed action. No cold email to German recipients.
- (4) Before the first invoice, ask an adviser the regime question in the review document §4.
- (5) After a test, replace the model assumptions with observed figures and rerun `models/route_economics.py` and `package/build_package.py`.
- (6) Push or publish only if the owner asks.
FILES:
- **New:**
  - `package/00-START-HERE.md`, `01-decision-brief.md`, `03-dossiers/R1-agent-risk-review.md`, `R2-coding-agent-enablement.md`, `R3-support-agent-evaluation.md`, `R4-workflow-automations.md`, `04-economics-intro.md`, `04-economics.md` (generated), `05-validation-plans.md`, `06-review-and-open-questions.md`, `reading-edition.html`, `build_package.py`;
  - `models/route_economics.py` and `route_economics_results.md`/`.csv`;
  - `paper/paper.html`; `verification/check_numbers_v12.py`; `archive/v1.1/*`.
- **Updated:** `paper/sections/*` (front, exec summary, §2, §5, §6.9, §12.4, §13.3, §14, §15) and `paper/paper.md`; `research/sources.csv` (S122–S141 plus annotations); `research/bookmarks.html`; `research/claims-ledger.md` (section E); `research/coverage-matrix.md`; `research/limitations-resolution.md` (§5); `models/cost_model.py` and results; `models/operator_economics.py` and results; `models/README.md`; `opportunities/*` (O13, v1.2 gate); `verification/verification-report.md`; `verification/check_numbers_v11.py`; `project/capabilities.md`; `README.md`; this file.
EVIDENCE: Sources S122–S141 (retrieved 2026-10-12, access path recorded per entry). Model outputs: `models/route_economics_results.md`, `models/cost_model_results.md` (v1.2 labour section). Review reports summarised in `package/06-review-and-open-questions.md` §3.
DO NOT REPEAT:
- Do not re-add S001–S141 (the next ID is S142).
- Do not overwrite `archive/v1.0/` or `archive/v1.1/`, or recreate tags `v1.0`/`v1.1`.
- Do not use the Gartner origin host (gcom.pdo.aws.gartner.com).
- Do not re-derive Latvian VAT from the outdated English translation (S099).
- Do not hand-edit the dossier economics tables (they are generated) or `04-economics.md` (generated from the intro plus the model).
- Do not send cold email to German recipients.
- Do not contact anyone, spend money, open accounts, publish or push without explicit approval of that exact action.
