# B. Verdict on the current proposal

*14 October 2026. Classes: KEEP · CHANGE · REMOVE FOR PILOT · DEFER · UNKNOWN — TEST REQUIRED.*

## B.1 Components

| Component | Verdict | Why (short) |
|---|---|---|
| Rented EU server, 4 CPU / 8 GB, ~€36/month | **REMOVE FOR PILOT** | Nothing in a 200-cell pilot runs continuously. The price is UNVERIFIED (Hetzner renders prices by JavaScript [S55]). Revisit at S10 if scheduled monitoring is wanted |
| n8n (self-hosted) | **REMOVE FOR PILOT** | Weak reproducibility of flows; an extra web UI to secure; the Sustainable Use License limits use to internal business or non-commercial purposes [S44], an open question for a client product |
| Postgres | **DEFER** | SQLite/files suffice for ≤1,000 cells; adopt Postgres when there are concurrent users or a client UI |
| Redis | **REMOVE FOR PILOT** | No queue or cache need at this volume |
| Gotenberg | **REMOVE FOR PILOT** | Local HTML→PDF is enough; reconsider only if PDF generation becomes a shared service |
| Caddy | **REMOVE FOR PILOT** | No public endpoint in the pilot |
| OpenRouter with spending limit | **CHANGE** | Useful for the benchmark (one integration, many providers, 5.5 % fee [S38]), but only with pinned provider, `allow_fallbacks:false`, `zdr:true`, `data_collection:"deny"` and explicit model IDs [S39]. Default load-balancing breaks reproducibility. Re-decide direct-vs-OpenRouter for production on measured volume. The account and spending cap are 🔒 owner actions |
| Markdown research files in a private GitHub repo | **KEEP (with a change)** | Right tool for versioning and review diffs. Change: keep raw source snapshots **out of git** where reuse terms are unknown (EE, LV, PL); commit hashes + locators |
| Obsidian | **DEFER** | Optional viewer; Markdown with `[[links]]` works without it |
| 1. Approve rule list | **CHANGE** | Approve *comparison questions* with fixed scope, answer type and reference date, not "rules" (02 §C.1) |
| 2. Fetch sources | **CHANGE** | Fetch only from the official route per layer (03); snapshot immutably with SHA-256; never crawl wetten.overheid.nl with an AI agent [S26]; no scraping of Légifrance/e-TAR (bot-blocked [S23, S52]) |
| 3. Find relevant provisions | **CHANGE** | Deterministic narrowing by legal structure first, then the model ranks a short candidate list |
| 4. Extract and translate | **UNKNOWN — TEST REQUIRED** | Model quality per language and task is unmeasured; benchmark (06) |
| 5. Check extracted facts | **CHANGE** | Make the core of checking deterministic: quote-in-snapshot, locator, dates, schema (08 §I.2 V1–V3). Model self-checking is not verification |
| 6. Add real-world context | **KEEP (labelled)** | Always labelled INTERPRETATION; reviewed by a person with farm knowledge |
| 7. Compare jurisdictions | **CHANGE** | Compare structured records, not raw texts; show collective-agreement and regional variants as separate rows |
| 8. Cross-check with an AI from another company | **UNKNOWN — TEST REQUIRED** | Not automatically independent; adopt only if catch rate ≥ 70 % and shared errors < 30 % (06 §8) |
| 9. One-page summaries and PDF | **CHANGE** | One overview page + jurisdiction annexes; one page cannot honestly hold 10 layers with evidence (09 §J.1) |
| DeepL cross-check (optional) | **DEFER / UNKNOWN** | Official API price unreadable; third-party prices conflict [S56]; test LLM translation first |
| Lawyer spot-check (optional) | **CHANGE: not optional for any client use** | Spot checks find systematic errors but do not validate unchecked pages (08 §I.4) |

## B.2 Estimates in the proposal

| Estimate | Verdict | Evidence |
|---|---|---|
| AI €590 per complete run (€170–€2,000) | **UNKNOWN — TEST REQUIRED.** Plausible: inside our modelled range €18–€1,654 (base €330) | Verified list prices [S34–S36]; token use unmeasured (07) |
| First three months ~€1,700 (€320–€5,100) | **Plausible as money**, if it includes a lawyer spot-check (~€2,800 base with lawyer, ~€200 without) | 07 §H.3 |
| Pilot 13 weeks × 10–15 h/week | **Optimistic.** Matches only our low case; base is ~265 h ≈ 21 weeks at 12.5 h/week | 07 §H.3: gold standard and double rating dominate |
| Full coverage 24 weeks (11–68) | **Optimistic.** Base ~48 weeks, range 24–95, driven by review hours per cell | 07 §H.3 |
| €36/month server | **UNVERIFIED** and unnecessary for the pilot | [S55] |

## B.3 The known concerns

| Concern | Verdict | Evidence |
|---|---|---|
| Germany's official API may be beta | **Confirmed**, but not a blocker: use gesetze-im-internet.de XML (non-official consolidation) | [S08, S11] |
| Estonia may lack an API | **Not confirmed.** A keyless JSON API answered; terms unknown | [S13, S14] |
| Unofficial connectors (DE, SE, PL) | **Confirmed unofficial, and unnecessary**: official APIs answered | [S12, S17, S19] |
| Model quality by language untested | **Still true**: benchmark | 06 |
| Token use and run cost unmeasured | **Still true**: benchmark measures it | 06 §10 |
| DeepL and server prices from third parties | **Still true**: official pages did not render prices | [S55, S56] |
| Additional country, budget cap, audience undecided | Country: **Italy (runner-up Denmark)**. Budget cap and audience can wait until S8 | 03 §D.3 |
