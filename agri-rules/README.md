# agri-rules: EU agricultural-rules comparison (planning package v0.1)

A separate project from the AI-agents paper in the rest of this repository. **Start with [00-START-HERE.md](00-START-HERE.md).**

Status: research and decision package, 14 October 2026. No purchases, accounts, credentials, deployments, bulk scraping, publication or client contact.

## Rebuild and check

```bash
python3 agri-rules/models/country_score.py        # country rubric + sensitivity -> models/country_score_results.md
python3 agri-rules/models/cost_model.py           # cost/time scenarios -> models/cost_model_results.md
python3 agri-rules/benchmark/score_benchmark.py agri-rules/benchmark/sample_scores_SYNTHETIC.csv agri-rules/benchmark/sample_pairs_SYNTHETIC.csv   # scorer self-test on INVENTED data
python3 agri-rules/check_package.py               # references, links, figures vs model outputs
```

## HANDOFF

- **GOAL:** A decision-ready plan for a system that compares ~100 farm-related rules across the EU + 9 member states and produces an evidence-grade PDF. Planning only.
- **STATE:** Package v0.1 complete (deliverables A–M). Nothing built or run beyond single-request access probes. Benchmark designed and scorer tested on synthetic data only.
- **VERIFIED:**
  - official access routes probed for EU, LV, DE, NL, FR, ES, SE, EE, PL + candidates IT, DK, AT, FI, IE, LT, RO
  - the four brief concerns checked (DE trial API confirmed; EE has a keyless API; official DE/SE/PL APIs make unofficial connectors unnecessary; PISTE useful but optional thanks to DILA bulk)
  - EU baselines for working time, nitrates and seasonal workers read in Cellar
  - LV Darba likums Art 68/136 and DE ArbZG § 3 read
  - official model, search and OpenRouter prices; OpenRouter routing and privacy controls
  - n8n licence
  - Eurostat 2024 output
  - ECB FX
- **UNVERIFIED:**
  - reuse terms for EE API, likumi.lv and the Sejm API
  - KOOP SRU HTTP 406
  - Normattiva API
  - DeepL and Hetzner prices
  - final CAP-simplification act number
  - Commission fur follow-up outcome
  - national authority names
  - model quality, context limits and structured output per model
  - all token and hour assumptions
- **BLOCKERS:** None for Sprint 0. The benchmark needs owner approval of an API account and spending cap.
- **NEXT:** Sprint 0: hand-answer EMP-01, NIT-01 and AW-01 for all 10 layers from official sources, timing each cell, and record reuse terms (10-plan §K.1 S0).
- **FILES:** `agri-rules/` (13 documents, rule list, schema, 3 scripts + generated results, benchmark templates, evidence folder).
- **EVIDENCE:** `12-evidence-ledger.md`, `evidence/sources.csv` (57), `evidence/probe-log.txt`, `evidence/snapshot-hashes.csv`, `evidence/robots/`.
- **DO NOT REPEAT:**
  - the access probes of 14 Oct 2026, unless more than a month has passed
  - the country scoring, unless weights or Sprint-0 facts change
  - the price lookups for Anthropic, OpenAI, Google, OpenRouter, Brave and Tavily (re-check only before spending)
  - the EU-text checks of Dir 2003/88, 91/676 and 2014/36
