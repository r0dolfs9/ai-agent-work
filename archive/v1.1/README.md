# AI agent ecosystem research project

This is an evidence-based research paper on AI agents and the market forming around them. It comes with a source register, cost model and business-opportunity register.

**Status: v1.1 (limitations follow-up) COMPLETE as local research deliverables, 2026-10-12.** v1.0 is preserved in `archive/v1.0/` and git tag `v1.0`. Nothing has been published externally, and no one has been contacted.

## Start here

| File | What it is |
|---|---|
| [`paper/paper.md`](paper/paper.md) | **The paper** v1.1 (~20.7k words incl. appendices, + references). Generated from `paper/sections/` by `paper/build_paper.py`. New §15: operating a global agent business from Latvia and the EU |
| [`research/limitations-resolution.md`](research/limitations-resolution.md) | **Limitations-resolution matrix** and claim-level audit (v1.1) |
| [`research/analysis/`](research/analysis/) | Our analysis of 2.74M agent-authored pull requests (timing) |
| [`opportunities/opportunity-register.md`](opportunities/opportunity-register.md) | Ranked business opportunities, with evidence and validation plans (CSV: `opportunity-register.csv`) |
| [`research/sources.csv`](research/sources.csv) | Source and bookmark register (121 sources; superseded entries kept and annotated). Browser import: [`research/bookmarks.html`](research/bookmarks.html) |
| [`research/claims-ledger.md`](research/claims-ledger.md) | Load-bearing claims (L01–L64), conflicts (C001–C020), unknowns (U01–U10) |
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
python3 -I verification/check_numbers_v11.py # v1.1 figures and arithmetic
python3 -I verification/check_links.py       # read-only link check (network)
python3 -I research/tools/make_bookmarks.py  # regenerate bookmarks.html
```

To produce PDF or DOCX, pandoc is available locally: `pandoc paper/paper.md -o paper.docx`.
