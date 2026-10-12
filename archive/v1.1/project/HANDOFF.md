# Progress log and handoff

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
GOAL: Reduce the reported v1.0 limitations as far as public evidence allows. Answer the scope questions (private learning/business development; global; EU/Latvia only where location affects operations). Integrate the stronger findings into the paper, source register, claim ledger, cost models and opportunity register. Add a Latvia/EU operating section and test the hypothesis that a Latvia-based operator can serve international customers through agents.
STATE: v1.1 COMPLETE as local research deliverables on branch `claude/amazing-archimedes-w4pw0c` (see `git log` for the v1.1 commit). Limitation outcomes:
- A (Gartner/McKinsey/OpenAI extracts): PARTIALLY RESOLVED. 11 of 14 claims resolved, 2 partial, 1 removed.
- B (activity timing): PARTIALLY RESOLVED.
- C (ban frequency): UNRESOLVED AFTER DOCUMENTED SEARCH for a rate; context improved.
- D (autonomous purchase value): PARTIALLY RESOLVED, bounded examples only.
- E (US-heavy evidence): PARTIALLY RESOLVED.
- F (Latvia/EU operations): new §15, PARTIALLY RESOLVED pending professional confirmation.
Nothing published, no accounts opened, no contact made, no money spent.
VERIFIED:
- `python3 paper/build_paper.py`: 111 cited sources resolve; 121 registered.
- `python3 -I verification/check_numbers.py`: 44/44.
- `python3 -I verification/check_numbers_v11.py`: 32/32.
- Models and register regenerate deterministically.
- Link check: 98 OK, 20 blocked to bots, 3 McKinsey .com connection errors (content read on the McKinsey-hosted mirror).
- Read directly this session: Gartner releases and article (via gcom.pdo.aws.gartner.com); McKinsey 2025/2026 surveys and commerce report (via karriere.mckinsey.de); Anthropic Series G/H posts and transparency hub; Visa onchain report; TRM Labs analysis; Cloudflare blog; Eurostat and ECB APIs; Latvian VAT Law translation; KPMG 2026 tax card; Enterprise Register; EC OSS and AI Act pages; FIU sanctions notice; Stripe and Paddle pricing; Anthropic supported countries; Accenture survey; Stripe ACP newsroom.
UNVERIFIED:
- OpenAI March-2026 checkout post and Atlas security post (openai.com 403; quotes via search extract plus independent coverage).
- Atlas deprecation (help center 403).
- Anthropic $65bn run-rate (single anonymous source).
- Current consolidated Latvian VAT Law text (translation read is marked outdated, valid 2024).
- Latvian e-invoicing 2028 date (secondary sources).
- Product Liability Directive dates (secondary sources).
- Anthropic EU billing entity (conflicting secondaries).
- Self-employed social contribution rates.
- Bookkeeping costs (assumption).
- Stripe Managed Payments eligibility for Latvia.
- All opportunity demand and willingness to pay.
- Review was self-review only.
BLOCKERS: None for v1.1. Owner decisions needed:
- (1) Accept or reject the use of publisher-hosted alternative domains for Gartner/McKinsey (verification report V1). If rejected, revert S082–S087 and S098 to search-extract status.
- (2) Any validation experiment, accountant/lawyer consultation or outreach needs explicit approval.
NEXT:
- (1) Take the §15.9 questions to a Latvian accountant and lawyer. Priority: does s.59(6) of the current VAT Law force VAT registration when buying foreign APIs, and which tax regime fits.
- (2) If approved, run the cheapest validation tests for O03, O07, O02.
- (3) Re-check quarterly: Gartner/McKinsey updates, card-network agent volumes, Anthropic transparency hub, the MCP spec, AI Act guidance.
- (4) Optional: query the EU DSA Transparency Database for automation-related enforcement; extend the AIDev analysis with a human-PR baseline.
FILES:
- New: `research/limitations-resolution.md`; `research/analysis/aidev_timing.py`; `research/analysis/aidev_timing_results.md` and `.csv`; `models/operator_economics.py`; `models/operator_economics_results.md`; `paper/sections/091-operating-from-latvia.md`; `paper/sections/095-glossary.md`; `verification/check_numbers_v11.py`; `archive/v1.0/*`.
- Updated: `paper/paper.md` and `sections/*`; `research/sources.csv`; `research/bookmarks.html`; `research/claims-ledger.md`; `research/coverage-matrix.md`; `models/cost_model.py`; `models/cost_model_results.*`; `models/README.md`; `opportunities/*`; `verification/verification-report.md`; `verification/link-check.csv`; `project/brief.md`; `project/capabilities.md`; `README.md`; this file.
EVIDENCE: Sources S082–S121 (retrieved 2026-10-12, access path recorded per entry). AIDev dataset hao-li/AIDev (CC-BY-4.0). ECB FX 1.1206 USD/EUR (2026-10-09). Eurostat isoc_eb_ai and lc_lci_lev queries.
DO NOT REPEAT:
- Do not recreate the `v1.0` tag or overwrite `archive/v1.0/`.
- Do not re-add sources S082–S121 (next ID is S122; `add_sources.py` rejects duplicates).
- Do not delete superseded source entries (they are annotated for traceability).
- Do not re-download the 1.5 GB AIDev parquet unnecessarily (column cache in the scratchpad is session-local).
- Do not contact anyone, spend money, publish, or open a PR without approval.
- Do not bypass openai.com/cnbc.com 403s.
