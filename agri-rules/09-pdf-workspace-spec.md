# J. PDF and research-workspace specification

*14 October 2026. Specification only. No PDF has been produced.*

## J.1 Can one page hold a rule for all ten layers?

**CALCULATION.** A complete cell needs, as minimums:
- original excerpt ~60 words
- translation ~60 words
- value and exceptions ~40 words
- citation ~15 words

That is **~175 words per layer × 10 = ~1,750 words** before the comparison summary and practical example. One A4 page holds ~500–700 words legibly.

**Finding:** one honest page cannot hold all ten layers with evidence.

**Recommendation:** a **two-tier unit**:
- **Overview page (1 page per question).** The question, the EU baseline, a 10-row comparison table (value / key exception / effective date / verification badge per layer), a "material differences and risks" box, and a practical-effect box.
- **Jurisdiction annex (½–1 page per layer, only where needed).** Original-language excerpt, translation, definitions, exceptions, regional/agreement variants and full source footnotes.

Harmonised questions (e.g. VET-03) can carry all evidence on the overview page; complex ones (EMP-04, NIT-02) get full annexes.

## J.2 Overview page hierarchy

1. **Header:** question ID and wording, reference date ("Law as in force on 2026-11-02"), page version (`EMP-04@a1b2c3d`), domain.
2. **EU baseline box:** instrument and article, or "No EU baseline: national competence", with the official link.
3. **Comparison table:** one row per layer. Columns: value (with unit), scope note, key exception (≤12 words), effective date, source type icon (law / agreement / regional / court / guidance), verification badge, footnote number.
4. **Material differences and interpretation risks** (≤5 bullets), each labelled INTERPRETATION.
5. **Practical effect on a farm or employer:** one worked example, labelled INTERPRETATION, with the scope stated.
6. **Uncertainty box:** UNKNOWN cells, open conflicts, pending changes (e.g. "EU follow-up to Fur Free Europe pending").
7. **Footer:** footnotes (official URLs, preserved as live links), last-checked date per layer, "Research summary, not legal advice".

**Verification badges:**

| Badge | Meaning |
|---|---|
| ● Released (lawyer-reviewed) | `expert-reviewed` |
| ◐ Researcher-reviewed | `human-reviewed` |
| ○ Unreviewed | Below `human-reviewed`; visibly marked, never released externally |
| ⚠ Stale / conflict | Source changed, or an unresolved material conflict |

Badges use text labels, not colour alone.

## J.3 Annex page

The annex shows the original excerpt and the translation **side by side**, so a reader can compare clause by clause. It records the translation method ("LLM: model-id; checked by researcher" or "human"), and then lists:
- definitions
- exceptions and derogations
- regional/agreement variants as sub-rows
- enforcement authority and sanction context
- superseded-version note
- full citation: publisher, title, article, consolidation status and whether the text is official

## J.4 Accessibility and overflow

- **Tagged PDF** (PDF/UA target): reading order, table headers, language tags per excerpt (`lang="lv"` etc.) so screen readers switch language.
- Minimum 9 pt in tables, 10.5 pt body; contrast ≥ 4.5:1.
- **Overflow:** text is never truncated or shrunk below the minimum. If a table row exceeds 3 lines, the overview shows "see annex" and the full text moves there. The renderer fails the build if any text box overflows.
- **Links:** every footnote URL is a live link, and the printed URL is also shown, so the page survives print.

## J.5 Index and cross-references

- Front matter: question index by domain, jurisdiction index, legend of badges and source types, and the methodology and limitations page.
- Cross-references such as "see also EMP-02" are generated from the rule list, never typed by hand.

## J.6 Research workspace: files, IDs, git

```
agri-rules/
  rules/rule-list.csv                    # approved questions (single source of truth)
  schema/cell-record.schema.json
  sources/registry.csv                   # one row per SourceSnapshot (no raw text)
  sources/snapshots/                     # raw bytes, named {sha256}.{ext}; NOT in git if licence unknown
  cells/{RULE-ID}/{LAYER}.md             # human-readable cell, YAML front matter = CellAnswer
  reviews/{RULE-ID}/{LAYER}/{date}-{reviewer}.md
  evidence/ledger.csv                    # claim-level evidence ledger
  runs/{run_id}.jsonl                    # every model call: model, provider, tokens, cost, latency, prompt_hash
  build/pages/{RULE-ID}.html  → build/pdf/agri-rules-{version}.pdf
```

- **IDs:** `RULE-ID` = `EMP-04`; layer = `EU`, `LV`, `DE` … or `ES-CT` for a region; cell ID = `EMP-04:LV:2026-11-02`; snapshot ID = SHA-256.
- **Cell file:** YAML front matter carries the structured record. The body carries the excerpt, translation and notes with `[[EMP-02]]`-style links, so Obsidian (optional) shows the network without being required.
- **Git workflow:**
  - one branch per batch (`batch/pilot-emp`)
  - every commit message names the cells and the run ID
  - review happens as a pull-request diff of `cells/` and `reviews/`
  - `main` holds only `human-reviewed` or better
  - releases are git tags (`v0.1-pilot`)
- **Evidence ledger:** one row per material claim on a page (claim ID, cell ID, provision ID, label, reviewer).

## J.7 Update and supersession

1. Poll official change feeds (EU SPARQL; ES, EE, PL and DK APIs) or re-fetch monthly where no feed exists (LV, NL, SE, FR bulk diff, DE GII toc date).
2. A changed hash for a cited provision marks dependent cells `stale` and their pages ⚠.
3. Re-run extraction for stale cells only, then re-review, then supersede.
4. The new PDF version lists changes since the previous version.

## J.8 PDF validation checklist (every build)

- [ ] All cells on released pages are ≥ `human-reviewed` (or visibly badged).
- [ ] V1–V3 checks green; zero release-blocking errors.
- [ ] Every footnote link returns HTTP 200 (or is logged as an expected bot-block with a manual check, e.g. Légifrance 403 [S23]).
- [ ] No overflow warnings from the renderer.
- [ ] Page count = overview pages + annex pages expected from the rule list.
- [ ] Visual diff against the previous build: render each page to PNG and review the pixel diff of changed pages.
- [ ] Accessibility check (tags, language attributes, reading order) on a sample of 5 pages.
- [ ] Version ID and build date on every page; the build hash is recorded in `PageBuild`.
