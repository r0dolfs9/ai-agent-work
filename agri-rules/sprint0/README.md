# Sprint 0 (AI version): 3 rules × 10 jurisdictions

*14 October 2026. Every answer here is an **AI draft (Claude Opus 5.5)**, not a human-checked gold standard. Reference date: 14 Oct 2026. No money spent, no accounts, no bulk downloads: each source was fetched once and logged in `fetch-log.csv` with a SHA-256 hash. The raw source copies are kept privately and not committed, because some reuse terms are unknown.*

## Result in one line

**28 of 30 answers carry a quote that a script confirmed is word-for-word in the official source. The 2 Italian cells failed** because Italy's official sites load their law text with JavaScript.

**What a "PASS" proves:** the quoted sentence really exists in that source. It does **not** prove the AI read it correctly, chose the right law or caught every exception. That is what your 5-cell check below measures.

## The 30 cells

| Cell | Answer (short) | Source | Quote check | Confidence |
|---|---|---|---|---|
| EMP-01 EU | 48 h avg incl. overtime; agriculture may stretch the averaging period to 6 (12) months | Dir 2003/88 Art 6(b) | PASS | H |
| EMP-01 LV | 40 h normal + overtime ≤ avg 8 h/7 days → ≈48 h | Darba likums 131., 136.(5) | PASS | H |
| EMP-01 DE | 8 h/working day, 10 h if 6-month avg ≤8 h → ≈48 h/week | ArbZG § 3 | PASS | M |
| EMP-01 NL | 60 h/week max; avg 48 h over 16 weeks | Arbeidstijdenwet 5:7 | PASS | H |
| EMP-01 FR | 48 h in any week; avg 44 h over 12 weeks (**general code, not the farm rules**) | Code du travail L3121-20/22 | PASS | M |
| EMP-01 ES | 40 h avg over the year; overtime ≤80 h/year | Estatuto Art 34–35 | PASS | M |
| EMP-01 SE | 48 h avg over ≤4 months; overtime ≤200 h/year | Arbetstidslag 10 b § | PASS | H |
| EMP-01 EE | 48 h avg over ≤4 months; **farm workers: 12 months by collective agreement** | Töölepingu seadus § 46 | PASS | H |
| EMP-01 PL | 48 h avg incl. overtime | Kodeks pracy Art 131 | PASS | H |
| EMP-01 IT | 48 h avg incl. overtime, ≤4 months | D.Lgs 66/2003 Art 4 | PASS | H |
| NIT-01 EU | 170 kg N/ha/year | Dir 91/676 Annex III | PASS | H |
| NIT-01 LV | 170 kg N/ha (manure + digestate) = 1.7 livestock units | MK 834, 3.3.2 | PASS | H |
| NIT-01 DE | 170 kg N/ha farm average | DüV § 6(4) | PASS | H |
| NIT-01 NL | 170 kg N/ha; no derogation from 2026 | Meststoffenwet Art 9 | PASS | H |
| NIT-01 FR | 170 kg N/ha of farmland (**from a 2012 MP question, not the law**) | Assemblée nationale | PASS | **L** |
| NIT-01 ES | 170 kg N/ha (210 in first programme for new zones) | RD 47/2022 Annex 3 | PASS | H |
| NIT-01 SE | 170 kg N/ha **only in "sensitive areas"** | SJVFS 2004:62, 19 a § | PASS | M |
| NIT-01 EE | 170 kg N/ha incl. grazing | Veeseadus § 161 | PASS | H |
| NIT-01 PL | 170 kg N/ha | Program działań, Dz.U. 2023/244 | PASS | H |
| NIT-01 IT | 170 kg in vulnerable zones (secondary sources only) | — | **NO SOURCE** | **L** |
| AW-01 EU | No EU ban; Commission follow-up was due March 2026, outcome unknown | ECI page | PASS | M |
| AW-01 LV | **Banned from 1 Jan 2028** | Amendment, Art 13.1 | PASS | H |
| AW-01 DE | No explicit ban found; the fur section of the ordinance is "weggefallen" | TierSchNutztV | PASS | **L** |
| AW-01 NL | Banned | Wet verbod pelsdierhouderij Art 2 | PASS | H |
| AW-01 FR | Banned for mink and non-domestic species (ministry page, not the law) | ecologie.gouv.fr | PASS | M |
| AW-01 ES | No national ban found (animal-welfare law excludes farm animals) | Ley 7/2023 Art 1 | PASS | **L** |
| AW-01 SE | Not banned; fur breeding needs a permit | Djurskyddslag 4 § | PASS | M |
| AW-01 EE | **Banned from 1 Jan 2026** | Loomakaitseseadus § 4¹ | PASS | H |
| AW-01 PL | Banned except rabbits (2025 act); phase-out date not confirmed | Dz.U. 2025/1696 | PASS | M |
| AW-01 IT | Banned from 2022 (secondary sources only) | — | **NO SOURCE** | **L** |

**Totals:**

| Measure | Result |
|---|---|
| Confidence | High 17 · Medium 8 · Low 5 |
| Answers resting on binding law, as retrieved | 24 of 30 |
| Answers resting on other sources | 6: guidance 1, Commission news 1, parliamentary record 1, secondary-only 2 (Italy), plus the Swedish agency regulation, which is binding but issued by an agency |

## What the sprint taught us (feeds the plan)

1. **The AI pipeline works for 8 of 10 jurisdictions** using only official, free routes:
   - EU via Cellar
   - LV via likumi.lv
   - DE via gesetze-im-internet.de
   - NL via KOOP open data
   - ES via the BOE API
   - SE via the Riksdagen API and the agency PDF
   - EE via `public-api/api/v1/akt/{id}/xml`, newly found and undocumented
   - PL via the Sejm ELI API
2. **France is partly blocked.** Labour law came through the ministry's code.travail.gouv.fr. The nitrate and fur answers rest on non-law sources, because Légifrance blocks scripts and its API needs a PISTE account.
3. **Italy failed 2 of 3.** Normattiva and the Gazzetta load text by JavaScript. **Under the plan's own rule (03 §D.3), this tips the 10th-country choice towards Denmark**, whose API worked in the earlier probe.
4. **The traps the plan predicted showed up in real data:**
   - Estonia lets *farm workers'* hours be averaged over 12 months by collective agreement.
   - Sweden's 170 kg limit applies only in sensitive areas.
   - Latvia's fur ban is invisible in today's consolidated law (it starts in 2028).
   - France's general labour code may not be the farm rule.
   - Germany's answer depends on a repealed section.
5. **"No ban" answers are the weakest.** DE, ES and SE all need a human to confirm absence.

## Your part: check 5 answers (~1 hour)

For each one:
1. Start a timer.
2. Open the link and find the quoted sentence (Ctrl+F a few words).
3. Decide: does the source say what the "Answer" column claims? Write **OK / WRONG / UNSURE** and the minutes.

Use the browser's translate button if needed.

| # | Cell | Link | Check this claim | Verdict | Minutes |
|---|---|---|---|---|---|
| 1 | EMP-01 LV | https://likumi.lv/ta/id/26019-darba-likums (Ctrl+F "136.pants") | Overtime ≤ average 8 h per 7 days over ≤4 months, so ≈48 h total | | |
| 2 | NIT-01 LV | https://likumi.lv/ta/id/271376 (Ctrl+F "3.3.2") | Manure + digestate ≤170 kg N/ha/year, applies to all farms | | |
| 3 | AW-01 LV | https://likumi.lv/ta/id/336054 | Fur-farming ban starts 1 Jan 2028 | | |
| 4 | EMP-01 EE | https://www.riigiteataja.ee/akt/103072026035 (§ 46) | Farm workers' averaging period can be 12 months by collective agreement | | |
| 5 | AW-01 PL | https://api.sejm.gov.pl/eli/acts/DU/2025/1696/text.pdf | Commercial fur farming banned, rabbits excepted | | |

The first three are Latvian, so you can judge them without translation. Your minutes per cell become the **review-time** number that drives every cost in the plan (07 §H.6).

## Files

| File | What it is |
|---|---|
| `cells.json` | All 30 records: answer, act, locator, quote, translation, exceptions, confidence |
| `verify_quotes.py` | Re-runs the quote check against the private snapshots |
| `verify_results.json` | The check results |
| `fetch.py` | The single-request fetch helper |
| `fetch-log.csv` | Every fetch: time, HTTP status, bytes, SHA-256, URL. Includes failed attempts, e.g. Légifrance 403 and the Estonian 406s |
