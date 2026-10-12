# AI agent ecosystem research project

This is an evidence-based research paper on AI agents and the market forming around them. It comes with a source register, cost model and business-opportunity register.

**Status: v1.0 COMPLETE (local research deliverables), 2026-10-12.** Nothing has been published externally, and no one has been contacted.

## Start here

| File | What it is |
|---|---|
| [`paper/paper.md`](paper/paper.md) | **The paper** (~14k words + appendices + references). Generated from `paper/sections/` by `paper/build_paper.py` |
| [`opportunities/opportunity-register.md`](opportunities/opportunity-register.md) | Ranked business opportunities, with evidence and validation plans (CSV: `opportunity-register.csv`) |
| [`research/sources.csv`](research/sources.csv) | Source and bookmark register (81 sources, searchable). Browser import: [`research/bookmarks.html`](research/bookmarks.html) |
| [`research/claims-ledger.md`](research/claims-ledger.md) | Load-bearing claims, conflicts (C001–C014), unknowns (U01–U07) |
| [`research/coverage-matrix.md`](research/coverage-matrix.md) | Topic → research question → sources → strength → section → gaps |
| [`models/`](models/) | Cost model (`cost_model.py`), assumptions (`README.md`), outputs (`cost_model_results.md/.csv`) |
| [`verification/verification-report.md`](verification/verification-report.md) | Checks performed, adversarial self-review, what could invalidate conclusions |
| [`project/brief.md`](project/brief.md) | Brief, assumptions, acceptance criteria, open questions |
| [`project/capabilities.md`](project/capabilities.md) | Tool/capability record |
| [`project/HANDOFF.md`](project/HANDOFF.md) | Progress log and handoff |

## Rebuild and verify

```bash
python3 models/cost_model.py                 # regenerate cost tables
python3 opportunities/build_register.py      # regenerate ranked register
python3 paper/build_paper.py                 # assemble paper + references, fail on unresolved citations
python3 -I verification/check_numbers.py     # paper figures == model output
python3 -I verification/check_links.py       # read-only link check (network)
python3 -I research/tools/make_bookmarks.py  # regenerate bookmarks.html
```

To produce PDF or DOCX, pandoc is available locally: `pandoc paper/paper.md -o paper.docx`.
