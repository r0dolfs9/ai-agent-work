# G. Benchmark protocol (20 questions)

*Version 0.1, 14 October 2026. **Status: ready to run, NOT run.** No model has been called and no score exists. The only data in `benchmark/` that looks like results, `sample_*_SYNTHETIC.csv`, is invented test data proving that the scorer works.*

This protocol is written so that a researcher who has not seen this conversation can execute it.

## 1. Purpose

Choose, **per pipeline stage**, a primary model and a challenger model. Measure:
- each one's error profile
- how often the challenger catches the primary's errors
- what full runs will really cost in tokens and time

Public leaderboards are not used to decide anything.

## 2. Scope

- **Questions:** the 20 pilot questions in [`rules/rule-list.csv`](rules/rule-list.csv) (`pilot = Y`).
- **Gold layers (human answers):** EU, LV, DE, FR, EE. That is 5 layers × 20 = **100 gold cells**, with languages en, lv, de, fr, et.
  - These five are chosen for language spread and because they include one official consolidated source (EE), one non-official (DE GII), one informative (LV), and one bulk-data route (FR).
  - The remaining 5 layers run through the pipeline without gold. Their outputs are reviewed by sample (§9), so the benchmark measures accuracy on 100 cells and cost/latency on 200.
- **Reference date:** one fixed date for every cell, e.g. `2026-11-02`, recorded in `benchmark/config.yaml` before any model runs.

## 3. Gold standard

Made **before** any model output is seen, by a researcher who reads the official source.

For each gold cell the researcher fills one `CellAnswer` record (schema: `schema/cell-record.schema.json`) plus:

| Field | Rule |
|---|---|
| `value`, `unit`, `scope` | From binding text; record the exact `locator` and a verbatim `exact_excerpt` |
| `exceptions[]` | Every exception that would change the answer for a typical farm, marked `material: true` |
| `effective_from` and any `future_change` | From the source's in-force metadata or the amending act |
| `source_type` | One of the six types; "no binding rule" is a valid answer and needs its own evidence (search log of the official portal) |
| `acceptable_variants` | Alternative phrasings or units that count as correct (e.g. "4 weeks" = "20 working days on a 5-day week") |
| `gold_time_minutes` | **Measured** time to produce the cell (feeds the cost model) |
| `gold_confidence` | H/M/L; L cells go to a second researcher before the benchmark starts |

**Second-researcher check:** 20 % of gold cells (all `L` + a random fill) are independently re-done by a second person. Disagreements are adjudicated against the source, and the adjudication is logged. Gold cells with an unresolved dispute are **excluded** from scoring, not guessed.

## 4. Candidates

For each stage, 2–3 candidates (from 04 §E.2):

| Stage | Candidates (initial) | Challenger rule |
|---|---|---|
| Locate + extract + translate | `sonnet-5.5`, `gemini-3.8-flash`, `gpt-5.4-mini` | — |
| Cross-layer comparison | `opus-5.5`, `gemini-3.1-pro-preview`, `sonnet-5.5` | — |
| Challenge review | Must be from a **different provider** than the primary being challenged | Each primary × each other-provider challenger |
| Cheap baseline (controls whether expensive models earn their price) | `haiku-5.5`, `gemini-3.5-flash-lite` | — |

All calls go through one access layer with pinned settings:
- explicit model ID
- fixed provider
- `allow_fallbacks:false`
- `temperature` 0 (or the provider minimum)
- `zdr:true`
- `data_collection:"deny"`

Record the response's `model`, provider, token counts and latency for every call.

## 5. Running

1. **Identical inputs.** Each candidate receives the same prompt template, the same source excerpt bundle (the deterministic-retrieval output, saved with a hash), the same JSON schema and the same reference date. Prompts are versioned and hashed (`prompt_hash`).
2. **Order randomisation.** Run order across candidates is shuffled per item with a seed stored in config, to avoid time-of-day or rate-limit bias.
3. **Blinding.** A script replaces candidate names with random codes (`cand-A`, `cand-B` …) before outputs reach raters. The key stays sealed in `benchmark/blinding_key.json`, which raters must not open until scoring is final.
4. **Repeats.** Run every (item, candidate) twice. If the two outputs differ in `value`, record `nondeterministic = 1`. This is itself a metric.
5. **Failures.** Timeouts and errors are retried once and logged. A second failure scores as a retrieval failure; it is not dropped.

## 6. Scoring rubric

Columns of [`benchmark/scores_template.csv`](benchmark/scores_template.csv):

| Metric | Column | Scale | Definition |
|---|---|---|---|
| Retrieval success | `retrieval_ok` | 0/1 | The provision cited contains the answer |
| Correct legal provision | `provision_ok` | 0/1 | Same provision as gold (or an equivalent listed in `acceptable_variants`) |
| Correct scope | `scope_ok` | 0/1 | Applies to the scope the question defines |
| Threshold and unit | `threshold_ok` | 0/1 | Value and unit match gold exactly (after variant normalisation) |
| Exception detection | `exception_ok` | 0/1 | All `material: true` exceptions present |
| Date/version | `date_ok` | 0/1 | In force on the reference date; future change mentioned if gold has one |
| Citation precision | `citation_ok` | 0/1 | Excerpt is verbatim (checked by script) and the locator is right |
| Structured output | `schema_valid` | 0/1 | Validates against the schema on the first try |
| Translation fidelity | `translation_0_3` | 0–3 | 3 = meaning and legal force preserved; 2 = minor wording loss; 1 = a qualifier lost; 0 = meaning changed |
| Comparison quality | `comparison_0_3` | 0–3 | Rule-level only: correct similarities and differences, no false equivalence |
| Hallucinations | `hallucinations` | count | Statements of law with no support in the supplied sources |
| Unsupported practical claims | `unsupported_claims` | count | Practical-effect statements that do not follow from the record |
| Latency, tokens, cost | `latency_s`, `tokens_in`, `tokens_out`, `cost_usd` | measured | From the run log |
| Critical failures | `critical_flags` | list | See §7 |
| Error signature | `error_signature` | text | Short normalised description of a wrong answer, e.g. `threshold:48h->60h`; used for the correlation check |

Points = (sum of the 8 binary metrics + the two 0–3 scores) ÷ 14.

## 7. Critical failures and verdict thresholds

**Critical failures** are scored separately from points, and any one makes the cell wrong regardless of points:
- `wrong_jurisdiction`
- `outdated_law`
- `missing_material_exception`
- `false_citation`
- `reversed_obligation`
- `wrong_threshold`
- `unjustified_certainty` (states a definite answer where gold says "depends" or "unknown")

**Pre-registered thresholds.** They are fixed now; changing them after seeing results invalidates the run.

| Verdict | Critical-failure rate | Mean points | Hallucinations per item |
|---|---|---|---|
| PASS | ≤ 2 % | ≥ 85 % | ≤ 0.05 |
| CONDITIONAL (usable only with 100 % human review of that stage) | ≤ 5 % | ≥ 75 % | ≤ 0.15 |
| FAIL | otherwise | | |

**Interpreting a small sample.** 100 gold cells cannot prove a 2 % error rate. With 0 critical failures in 100 cells, the 95 % upper bound is still about 3 % (rule of three: 3/n). These thresholds therefore select candidates; they do **not** certify accuracy. Production accuracy claims need the sampling in 08 §I.4.

## 8. Correlated errors between primary and challenger

For every primary-model critical error, record in `pairs.csv` whether the challenger flagged it (`verifier_flagged`). Then compute, with `score_benchmark.py`:
- **catch rate** = flagged ÷ primary critical errors
- **shared-error count** = items where the challenger made the *same* error signature

**Decision rule:**
- A challenger is accepted for a stage only if its catch rate is ≥ 70 % **and** it shares the error signature on < 30 % of the primary's critical errors.
- Error classes where both models fail together, e.g. a missed exception hidden in a cross-reference, are routed to deterministic checks or mandatory human review. A second model is not added for them.

## 9. Human review instructions

- **Raters:** two per item for the 100 gold cells. One must read the source language; a qualified lawyer is not required at this stage.
- Raters score from the **gold record and the source snapshot**, never from memory or web search.
- Each rater works alone, then the scorer computes Cohen's kappa on the critical-failure judgement.
  - **κ < 0.6:** the rubric is ambiguous. Fix the wording, re-score, and do not trust any verdict until then.
  - **κ ≥ 0.6:** disagreements are adjudicated by a third person against the source, and the adjudicated row is kept as rater `ADJ`.
- Time each rater's scoring. Review minutes per cell is the key input for the production cost model.
- **Non-gold layers** (NL, ES, SE, PL, IT/DK): one reviewer checks a random 20 % of cells against the source and records the same critical flags. These are reported separately and labelled "sample review".

## 10. What the benchmark must output (measurements for the cost model)

| Measurement | Replaces assumption in `cost_model.py` |
|---|---|
| Tokens in/out per stage per cell, median and p90 | `STAGES` token figures |
| Retry and failure rate per stage | `retry` |
| Gold minutes per cell, by layer | `gold_h` |
| Review minutes per cell, by layer | `review_h` |
| Critical-failure rate per stage | Release-gate sampling size (08) |
| Catch rate and shared errors per primary/challenger pair | Whether a challenger stage is worth its cost |
| Cost per cell per candidate | Model routing for the full build |

## 11. Files

| File | Purpose |
|---|---|
| `benchmark/scores_template.csv` | Empty scoring sheet with the exact columns |
| `benchmark/score_benchmark.py` | Scorer: verdicts, kappa, correlated errors |
| `benchmark/sample_scores_SYNTHETIC.csv`, `sample_pairs_SYNTHETIC.csv` | **Invented** data to test the scorer only |
| `benchmark/config.yaml` | To create at run time: reference date, seeds, model IDs, provider pins, prompt hashes |

Run the scorer: `python3 agri-rules/benchmark/score_benchmark.py scores.csv pairs.csv`.

## 12. Budget gate

The benchmark costs money only at step 5. Cost at verified list prices (base assumptions, 20 questions × 10 layers × 3 candidate pipelines) is estimated at **~€200 ex VAT** (low ~€11, high ~€990; `cost_model_results.md` §2). It **requires owner approval of an API account and a spending cap** before any call is made. Steps 1–3 and the gold standard cost only time.
