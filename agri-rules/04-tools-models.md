# E. Tool, service and model decision matrix

*Prices were read on the official provider pages on 14 October 2026 [S34–S43]. **No model was tested in this session.** Every quality statement below is a hypothesis for the benchmark (06), labelled UNVERIFIED. Context limits, structured-output support and language quality were **not verified** for any model, so they are UNKNOWN and become benchmark checks, not facts.*

## E.1 Principle: the model is never the source

The deterministic stages (fetch, parse, segment, cite, check, render) do the work that must be exactly right. Models are used only for **judgement** tasks:
- finding the relevant provision
- extracting a value into a schema
- translating
- comparing
- challenging

Every model output must point to a locator in an immutable source snapshot, or it is rejected (see 05 §F.4).

## E.2 Task-by-task matrix

| Task | Recommended approach | Candidates to benchmark (2–3) | Evidence | Status | Cheaper fallback | Disqualifier |
|---|---|---|---|---|---|---|
| Source discovery | Official APIs and indexes first (03 §D.1); web search only to discover guidance and agency pages | Brave Search API; Tavily; manual | Brave $5 per 1,000 requests, $5 free monthly credit; **storing results needs a plan with storage rights** [S42]. Tavily 1,000 free credits/month, $0.008/credit, basic search 1 credit [S43] | RECOMMEND manual + official in Sprint 0; Brave for the pilot | Manual browser search | Licence forbids storing what we must snapshot (Brave: keep only URLs, re-fetch from the official site) |
| Fetch and snapshot | Plain HTTP client, polite rate, store raw bytes + SHA-256 | — (deterministic) | Probes worked for 9/10 layers [log] | KEEP | — | — |
| HTML/XML parsing and segmentation | Parser per source format (GII DTD, LegalDocML/Akoma Ntoso, BOE blocks, SRU/BWB XML, Riigi Teataja XML, Cellar XHTML) | — (deterministic) | Formats observed in probes | KEEP | — | Never let an LLM re-type statute text |
| PDF text extraction | Text-layer extraction (e.g. pdfplumber); OCR only for scans | — | Not tested | UNKNOWN — TEST | Manual copy | — |
| OCR (scanned gazettes only) | Run only where no text layer exists | Tesseract (local, free); Mistral OCR (price per 1,000 pages **not shown** [S37]) | Not tested | DEFER until a scanned source is actually needed | Manual transcription with double-check | Any OCR text used without human verification of the quoted excerpt |
| Table extraction | Parser + human check of every number | — | — | Human-checked | — | — |
| Relevant-provision retrieval | Deterministic narrowing (act → chapter via structure + keyword list in the source language), then the LLM ranks ≤20 candidate sections | Sonnet 5.5 ($2/$10); Gemini 3.8 Flash ($0.75/$3.75); gpt-5.4-mini ($0.75/$4.50) [S34–S36] | Prices verified; quality UNVERIFIED | UNKNOWN — TEST | Haiku 5.5 ($0.10/$0.50 ≤100K) | Retrieval recall < 95 % on gold |
| Structured extraction (values, thresholds, exceptions, dates) | JSON-schema output validated by code | Same three as above | Structured-output support UNKNOWN per model → schema-validity metric | UNKNOWN — TEST | Haiku 5.5 / Gemini 3.5 Flash-Lite ($0.30/$2.50) | Schema validity < 99 % after one retry, or any invented value |
| Translation (evidence excerpts) | Model translation shown **next to** the original; a bilingual reviewer checks the gold set | One LLM from above vs DeepL API | DeepL API price **not readable on the official page**; third-party figures conflict [S56] | UNKNOWN — TEST | LLM only | Fidelity score < 2.5/3 on any language |
| Cross-language comparison | Stronger model over already-extracted structured records (not raw text) | Opus 5.5 ($4/$20); Gemini 3.1 Pro preview ($2/$12 ≤200k); gpt-6-astra ($10/$50) | Prices verified | UNKNOWN — TEST | Sonnet 5.5 | Any reversed obligation |
| Exception detection | Two nets: (1) source-language keyword list ("izņemot", "ausgenommen", "sauf", "salvo", "utom", "välja arvatud", "z wyjątkiem", "behalve", "eccetto" …) flags sections; (2) model extraction | Same as extraction | — | UNKNOWN — TEST | Keyword net + human | Missing material exception = critical |
| Citation checking | **Deterministic:** the quoted excerpt must be an exact substring of the snapshot at the stated locator; the URL must resolve | — | — | KEEP (code) | — | — |
| Date/version checking | Deterministic: compare in-force dates in API metadata with the reference date; flag any amendment after the snapshot | — | ES/EE/PL/DE-NeuRIS metadata expose dates (probes) | KEEP (code) | Manual | — |
| Contradiction detection / challenge review | A model from a **different provider** than the primary, given the same source snapshot and asked to find errors, not to re-answer | Gemini 3.1 Pro if primary is Claude; Sonnet/Opus if primary is Gemini | — | UNKNOWN — TEST (see E.4) | Human reviewer | Shares the primary's error signature on more than 30 % of the primary's critical errors (benchmark §8) |
| Plain-language explanation | Mid-tier model from the structured record only | Sonnet 5.5; Gemini 3.8 Flash | — | UNKNOWN — TEST | Haiku 5.5 | Adds facts not in the record |
| Practical farm example | Mid-tier model, labelled INTERPRETATION, reviewed by a person with farm knowledge | Same | — | UNKNOWN — TEST | Human-written | Unsupported practical claims > 0.1 per page |
| Page generation | **Template rendering (deterministic)**: models never write the page layout or the footnotes | — | — | KEEP (code) | — | — |

## E.3 Shortlisted models: verified facts only

| Model / service | Provider | Price USD per 1M input / output (verified 14 Oct 2026) | Batch | Data handling (verified) | Known risk |
|---|---|---|---|---|---|
| Haiku 5.5 | Anthropic | $0.10 / $0.50 (≤100K tokens); $0.50 / $2.50 above [S34] | −50 % | API inputs/outputs deleted within 30 days by default; ZDR by agreement [S45] | Long-context price step at 100K |
| Sonnet 5.5 | Anthropic | $2 / $10 [S34] | −50 % | as above | — |
| Opus 5.5 | Anthropic | $4 / $20 [S34] | −50 % | as above | — |
| gpt-5.4-mini / gpt-5.4-nano | OpenAI | $0.75 / $4.50; $0.20 / $1.25 [S35] | −50 % | Abuse logs up to 30 days; no training by default; ZDR needs approval; EU residency +10 % on models released after 5 Mar 2026 [S46] | Older generation: deprecation risk UNKNOWN |
| gpt-6-astra | OpenAI | $10 / $50 [S35] | −50 % | as above | Most expensive |
| Gemini 3.8 Flash / 3.5 Flash-Lite | Google | $0.75 / $3.75; $0.30 / $2.50 [S36] | −50 % | Paid tier: "Content not used to improve our products" [S36] | **Price increases scheduled** around end-2026 / Jan 2027 [S36] |
| Gemini 3.1 Pro (preview) | Google | $2 / $12 (≤200k); $4 / $18 above [S36] | −50 % | as above | **"preview" status**: version stability UNKNOWN |
| Mistral Large | Mistral (EU) | $0.50 / $1.50 [S37] | −50 % | Not checked | EU provider option; quality UNVERIFIED |

Context windows, structured-output modes and per-language quality: **UNKNOWN**. They go into benchmark checks B-2 and B-7 rather than into this table from memory.

## E.4 OpenRouter as the access layer

| Question | Finding | Label |
|---|---|---|
| Cost | 5.5 % fee on credit purchases (Standard), 8 % Business; inference at provider list price; BYOK free up to $25k/month then 5 % [S38] | VERIFIED FACT |
| Reproducibility | Default routing **load-balances across providers** and falls back automatically. Open-weight models can be served at different quantizations. Pinning needs `order`/`only` + `allow_fallbacks:false` (+ `quantizations`) [S39] | VERIFIED FACT |
| Version pinning | Use explicit model IDs, never `~…-latest` aliases. Log the `model` returned in each response, since billing and output follow the model actually used (per OpenRouter fallback docs, via search) | VERIFIED (docs) / RECOMMENDATION |
| Logging/privacy | OpenRouter stores no prompts or responses unless opted in; metadata is stored [S40]. `data_collection:"deny"` and `zdr:true` exist per request [S39]. Provider retention still applies, and OpenRouter does not route on retention policies [S41] | VERIFIED FACT |
| Outage/deprecation | No OpenRouter deprecation policy was found this session | UNKNOWN |
| Spending cap | The brief's "account spending limit" requires an account, which was **not created** | Not done (approval gate) |
| Independence of "different companies" | Routing through one intermediary adds a shared failure point, but that is not the main issue. **Independence is about the models**: different training data and methods. A Claude primary checked by a Gemini challenger is more independent than two Claude sizes. Even so, all large models share public web training data and can share the same misreading of a legal text, so independence must be **measured** (benchmark §8), not assumed | INTERPRETATION |

**Verdict: KEEP for the benchmark** (one integration, many models), configured with:
- `allow_fallbacks:false`
- pinned provider
- `zdr:true`
- `data_collection:"deny"`
- explicit model IDs

**Revisit for production.** Direct provider APIs remove the 5.5 % fee and one dependency, at the cost of 2–3 integrations. Decide on measured volume.

## E.5 Search APIs

| Candidate | Price (verified) | Strength | Weakness | Status |
|---|---|---|---|---|
| Brave Search API | $5/1,000 requests, $5 monthly free credit [S42] | Independent index; simple | Storage rights only on specific plans [S42]; snippets must never be cited | RECOMMEND for discovery only |
| Tavily | 1,000 credits/month free; $0.008/credit; advanced search 2 credits [S43] | Returns extracted page content | Content is Tavily's extraction, not the official source; same citation risk | ALTERNATIVE |
| Official portal search + APIs | Free | Authoritative | Uneven (no LV API) | **PRIMARY** |

## E.6 Translation services

DeepL's API price could not be read on its official page (JavaScript-rendered), and third-party reports conflict (€4.99 + €20/M characters vs a "Growth" plan) [S56], so it is **UNVERIFIED**. DeepL states that Pro texts are stored only as technically needed and never used for training [S56]. **Recommendation:** benchmark LLM translation first. Add DeepL only if LLM fidelity fails for a language, after reading the API terms on the official developer site.

## E.7 n8n (licence finding relevant to a client product)

n8n is released under the **Sustainable Use License**: "use or modify the software only for your own internal business purposes or for non-commercial or personal use" [S44]. Running it internally to produce your own deliverables appears to fit "internal business purposes", but that is an **INTERPRETATION, not legal advice**. Offering an n8n-based service to clients needs a lawyer's reading or an n8n commercial licence. This is one more reason not to build the pilot on n8n.
