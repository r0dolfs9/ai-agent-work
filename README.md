# AI agent ecosystem research project

This is an evidence-based research paper on AI agents and the market forming around them. It comes with a source register, cost model and business-opportunity register.

**Status: v1.2 (reading and decision package), 2026-10-12.** Committed locally at the time; now on the remote branch.

**New, 2026-10-13: [feasibility study](feasibility/eu-lv-regulatory-comparison/README.md)** on using AI agents to compare EU rules with Latvian law, industry by industry, with agriculture as the pilot. It covers costs, timeline, expected quality and certainty, risks and how to prevent them. **Simpler follow-up plan:** [`agent-stack-plan.md`](feasibility/eu-lv-regulatory-comparison/agent-stack-plan.md) (server, model mix including Qwen and DeepSeek, budget, timeline).

The rest of this README describes v1.2. v1.1 is preserved in `archive/v1.1/` and local tag `v1.1`; v1.0 in `archive/v1.0/` and tag `v1.0`. Nothing has been published externally, no one has been contacted, and no money has been spent.

**Start with [`package/00-START-HERE.md`](package/00-START-HERE.md)**, or open the single-file reading edition [`package/reading-edition.html`](package/reading-edition.html).

## Start here

| File | What it is |
|---|---|
| [`feasibility/eu-lv-regulatory-comparison/`](feasibility/eu-lv-regulatory-comparison/) | **Feasibility study (2026-10-13):** AI-agent comparison of EU rules with Latvian law by industry (pilot: agriculture). Costs (`cost_model.py`), verified pilot scope of 49 EU acts, EUR-Lex SPARQL queries and results, risks, timeline |
| [`package/`](package/) | **v1.2 decision package:** START HERE, decision brief, route dossiers (R1–R4), economics, validation plans with draft materials, review and open questions, and a combined HTML reading edition |
| [`models/route_economics.py`](models/route_economics.py) | Route economics: setup, costs, selling time, VAT, Latvian taxes, take-home per hour, adverse cases (v1.2) |
| [`paper/paper.md`](paper/paper.md) / [`paper/paper.html`](paper/paper.html) | **The paper** v1.2 (~22k words incl. appendices, + references), generated from `paper/sections/` by `paper/build_paper.py`. §15 corrected from current Latvian law |
| [`research/limitations-resolution.md`](research/limitations-resolution.md) | **Limitations-resolution matrix** and claim-level audit (v1.1) |
| [`research/analysis/`](research/analysis/) | Our analysis of 2.74M agent-authored pull requests (timing) |
| [`opportunities/opportunity-register.md`](opportunities/opportunity-register.md) | Ranked business opportunities, with evidence and validation plans (CSV: `opportunity-register.csv`) |
| [`research/sources.csv`](research/sources.csv) | Source and bookmark register (141 sources; superseded entries kept and annotated). Browser import: [`research/bookmarks.html`](research/bookmarks.html) |
| [`research/claims-ledger.md`](research/claims-ledger.md) | Load-bearing claims (L01–L76), conflicts (C001–C025), unknowns; v1.2 section E |
| [`research/coverage-matrix.md`](research/coverage-matrix.md) | Topic → research question → sources → strength → section → gaps |
| [`models/`](models/) | Agent cost model (`cost_model.py`, incl. labour-cost jurisdiction sensitivity), operator economics for a Latvia-based seller (`operator_economics.py`), assumptions (`README.md`), outputs (`*_results.md`) |
| [`verification/verification-report.md`](verification/verification-report.md) | Checks performed, adversarial self-review, what could invalidate conclusions |
| [`project/brief.md`](project/brief.md) | Brief, assumptions, acceptance criteria, open questions |
| [`project/capabilities.md`](project/capabilities.md) | Tool/capability record |
| [`project/HANDOFF.md`](project/HANDOFF.md) | Progress log and handoff |

## Rebuild and verify

```bash
python3 models/cost_model.py                 # regenerate cost tables
python3 opportunities/build_register.py      # regenerate ranked register
python3 paper/build_paper.py                 # assemble paper + references, fail on unresolved citations
python3 models/operator_economics.py         # regenerate operator economics (v1.1)
python3 -I verification/check_numbers.py     # paper figures == model output
python3 -I verification/check_numbers_v11.py # v1.1 figures (checks the archived v1.1 snapshot)
python3 models/route_economics.py           # route economics (v1.2)
python3 package/build_package.py            # regenerate dossier tables, economics doc, HTML editions
python3 -I verification/check_numbers_v12.py # v1.2 package figures vs model
python3 -I verification/check_links.py       # read-only link check (network)
python3 -I research/tools/make_bookmarks.py  # regenerate bookmarks.html
bash feasibility/eu-lv-regulatory-comparison/data/run_queries.sh      # re-run EUR-Lex scope queries (network)
python3 feasibility/eu-lv-regulatory-comparison/build_scope.py        # regenerate pilot-scope-agriculture.md
python3 feasibility/eu-lv-regulatory-comparison/cost_model.py         # feasibility cost/effort/certainty tables
python3 feasibility/eu-lv-regulatory-comparison/stack_costs.py        # model-mix and 3-month budget for the agent plan
python3 -I feasibility/eu-lv-regulatory-comparison/check_numbers.py   # study figures == model and query output
```

To produce PDF or DOCX, pandoc is available locally: `pandoc paper/paper.md -o paper.docx`.
