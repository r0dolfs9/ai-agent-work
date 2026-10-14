# D. Jurisdiction and official-source matrix

*Research date: 14 October 2026. Every "probe" below is one HTTP request by script. Each is logged with a timestamp in [`evidence/probe-log.txt`](evidence/probe-log.txt), with response hashes in [`evidence/snapshot-hashes.csv`](evidence/snapshot-hashes.csv). The first 7 probes ran before logging was set up, so they were re-run once at 09:52Z with logging, giving the same status codes; the log says so. [S##] IDs resolve in [`evidence/sources.csv`](evidence/sources.csv). No account was created, no key requested, and nothing was bulk-downloaded.*

## D.1 The access matrix

Access classes are those set by the brief. **"Probe OK" means technically accessible on 14 Oct 2026.** It does not mean permitted for this use, tested at scale, or reliable in production. The brief's distinctions (advertised / exists / accessible / permitted / tested / production-reliable) are kept apart in the last four columns.

| Layer | Authoritative publication (binding) | Consolidated text: who, legal status | Best automated route (class) | Probe 2026-10-14 | Reuse / terms found | Stable article-level IDs | Main limitation | Lawful fallback |
|---|---|---|---|---|---|---|---|---|
| **EU** | Official Journal, electronic edition authentic since 1 Jul 2013 [S06] | EUR-Lex consolidations: **no legal effect, documentation only** [S06] | Cellar REST content negotiation by CELEX (**official structured API**) + SPARQL [S01–S05, S07] | Cellar 200 (html/xhtml/pdf); SPARQL 200; **EUR-Lex HTML 202 empty (WAF)** | Commission reuse decision (not re-read) | CELEX + ELI; article anchors in HTML | CELEX `3xxxx` returns the **original act**, not the consolidation (trap: 2021/2115) | Consolidated CELEX `0xxxx-YYYYMMDD` via Cellar; manual EUR-Lex in a browser |
| **Latvia** | *Latvijas Vēstnesis* (official publisher VSIA "Latvijas Vēstnesis") [S16] | likumi.lv systematised versions: **informative; the official publication prevails** [S16] | **Official HTML** (likumi.lv) | 200 [S15] | No explicit licence found; robots.txt disallows `/search.php`, version-date paths | `ta/id/{id}` + article anchors | No public API found; ministry guidance separate | Manual download of the current version + Latvijas Vēstnesis PDF for disputed text |
| **Germany** | *Bundesgesetzblatt*, electronic since 1 Jan 2023 [S08] | gesetze-im-internet.de: **non-official** consolidation [S08] | **Official bulk XML** (gii-toc.xml + per-law XML) [S08, S09] | 200; robots allows all | Deep links expressly allowed; no reuse licence stated | `/{abbr}/__{§}.html` | Federal law only; **Länder law is separate** (16 portals); NeuRIS API is a **"trial service", dataset "not yet complete"** [S11, S12] | Use GII XML now and treat NeuRIS as a later upgrade; Länder portals manually |
| **Netherlands** | *Staatsblad* / *Staatscourant* (officielebekendmakingen.nl) | wetten.overheid.nl (BWB) consolidated | **Official structured API** (KOOP SRU 2.0, BWB) [S27] | SRU returned records **with HTTP 406** (anomaly to resolve) | KOOP datasets listed CC0 1.0 (BWB-specific wording unconfirmed) [S27] | BWBR id + article | **wetten.overheid.nl robots.txt explicitly disallows AI/LLM crawlers** [S26], so never crawl the site with an AI agent | SRU/repository open data only; manual reading in a browser |
| **France** | *Journal officiel* (JORF) | Légifrance LEGI (DILA) | **Official bulk dataset** (DILA LEGI + **KALI collective agreements**) [S22]; PISTE Légifrance API needs registration [S21] | LEGI/KALI directories 200; **legifrance.gouv.fr 403 Cloudflare** [S23] | Licence Ouverte 2.0 + PISTE/API CGU [S21] | LEGIARTI ids | PISTE = account action (not done); quotas per token | LEGI/KALI bulk (no account); PISTE after owner approval |
| **Spain** | *Boletín Oficial del Estado* + 17 regional gazettes | BOE consolidated: **"sin valor oficial"**, informative; covers state **and autonomous-community** laws [S24] | **Official structured API** (BOE datos abiertos) [S24, S25] | 200 JSON | Reuse must state the text is informative [S24] | BOE-A-yyyy-n + block ids | Regional competence (agriculture, water, animal welfare); collective agreements provincial | Regional gazettes manually for the regions sampled |
| **Sweden** | *Svensk författningssamling*, electronic since 1 Apr 2018 [S18] | Riksdag/Regeringskansliet consolidated SFS (legal status not confirmed) | **Official structured API** (Riksdagen öppna data, doktyp=sfs) [S17] | 200 JSON | "Free to use without fees or licences; credit Sveriges riksdag" [S17] | SFS number (no native ELI) | Labour terms largely in collective agreements; agency regulations (SJVFS) are separate | svenskforfattningssamling.se PDFs + agency sites manually |
| **Estonia** | *Riigi Teataja* | Riigi Teataja consolidated texts are **official and have legal force** (from 1 Jun 2002) [S14] | **Official structured API** (`/api/oigusakt_otsing`, JSON; acts as `/akt/{id}.xml`) [S13] | **200 JSON, keyless**, 164,539 acts | **No public documentation or terms found**, so permission is UNKNOWN | globaalID / terviktekstID | Undocumented endpoint could change without notice | Ask RIK/Ministry (owner action); manual XML/PDF per act |
| **Poland** | *Dziennik Ustaw* / *Monitor Polski* | ISAP unified text = **informational**; the official consolidation is the *tekst jednolity* announced by *obwieszczenie* [S20] | **Official structured API** (Sejm ELI API, OpenAPI) [S19] | 200 JSON | No terms found | `DU/{year}/{pos}` | Unofficial connectors are unnecessary: the official API exists | eli.gov.pl / isap PDFs manually |
| **Italy** (recommended 10th) | *Gazzetta Ufficiale* | Normattiva "multivigente" (point-in-time) | **Official portal; API status UNKNOWN** (dati.normattiva.it, 2026) [S51] | Portal 200 (JS shell); `api.normattiva.it` no response | UNKNOWN | URN:NIR / ELI (announced) | 20 regions with agricultural competence; national + provincial collective agreements | Manual Normattiva + regional bulletins |
| Denmark (runner-up) | *Lovtidende* | Retsinformation consolidated (LBK) | **Official structured API** (change feed) [S48] | 200 JSON | Terms on retsinformation.dk (not read) | accession no. + ELI | 1 call / 10 s; 03:00–23:45 only (per guide, secondary) | Manual retsinformation.dk |

**Search capability:** EU (SPARQL + EUR-Lex UI), DE (NeuRIS search trial; GII none), NL (SRU), FR (PISTE search, account), ES (API filters), SE (API `sok=`), EE (API search), PL (API filters), LV (UI only; robots disallows `/search.php`). **Rate limits:** none published for any probed EU-9 route except DK (secondary). **Treat every route as "be polite": ≤1 request/second, cache everything, and do one-off fetches rather than crawls.**

**History / amendment tracking:** official point-in-time versions exist in the EU (consolidated CELEX by date), DE (NeuRIS ELI version dates; GII current only), NL (BWB date-versions), FR (LEGI versions), ES (all versions via API), EE (redaction ids), PL (status + change date), LV (versions, but robots disallows version-date paths for crawlers). **SE: UNKNOWN** for structured history.

## D.2 Verifying the four concerns in the brief

| Concern (brief) | Finding | Label |
|---|---|---|
| "Germany's official-law data interface may still be in beta" | **Confirmed.** Docs say "This is a trial service" and "The dataset is not yet complete"; bulk XML "planned" [S11]. The trial host answered keyless [S12]. The stable alternative is gesetze-im-internet.de XML, which is non-official [S08]. | VERIFIED FACT |
| "Estonia may not provide a suitable API" | **Contradicted on access, open on permission.** A keyless JSON search API responded with 164,539 acts [S13], and Estonia's consolidated texts are themselves official [S14]. No public documentation or terms were found. | VERIFIED FACT (access) / UNKNOWN (permission) |
| "Community connectors for Germany, Sweden and Poland are unofficial" | **Confirmed, and they are not needed.** Official routes exist and responded: GII XML / NeuRIS (DE), Riksdagen API (SE), Sejm ELI API (PL) [S09, S12, S17, S19]. The community MCP servers found in search are third-party wrappers of these. | VERIFIED FACT |
| "France's PISTE platform: purpose and usefulness" | PISTE is the government API gateway; the Légifrance API there is free after registration and governed by Licence Ouverte 2.0 plus CGU, with per-token quotas [S21]. **It is useful but not required**: DILA's LEGI and KALI bulk dumps are keyless [S22], and KALI matters because French farm labour terms sit in collective agreements. The Légifrance website blocks scripts [S23]. | VERIFIED FACT + RECOMMENDATION |

## D.3 Additional-country selection

**The "10th country" question.** The brief lists EU + 8 member states + "one additional country". With the additional country that makes 9 countries + the EU = **10 comparison layers**. The brief's own figure of "approximately 1,000 jurisdiction-rule comparisons" = 100 rules × 10 layers, which only works under this reading. **INTERPRETATION: "10th" means the 10th comparison layer, not a 10th country.** If the owner actually wants 10 countries, add the runner-up too; the variable cost scales linearly (+10 %).

**Rubric and arithmetic.** Generated by [`models/country_score.py`](models/country_score.py); full table in [`models/country_score_results.md`](models/country_score_results.md). The score is 100 × Σ(weight × score) / (5 × Σ weights).

| Country | Total | Why (one line per decisive score) |
|---|---|---|
| **Italy** | **79.0** | Third-largest EU farm output, €70.2bn in 2024 [S33] and not yet covered; Mediterranean, regional agricultural competence; large seasonal workforce. Minus: API UNKNOWN [S51]; 20 regions + collective agreements raise maintenance |
| **Denmark** | **78.0** | Best official access in the candidate set (keyless change-feed API [S48], official consolidated texts); intensive livestock/nitrates. Minus: adds less beyond NL + SE |
| Austria | 70.0 | Excellent RIS API [S50]; but German-language and federal structure overlap DE |
| Finland | 70.0 | Excellent Finlex API [S49]; small output, Nordic overlap with SE |
| Ireland | 69.0 | English, common law, still uses a nitrates derogation (contrast with NL) — but weak consolidation |
| Romania | 57.0 | Large output (€20.2bn); official portal did not respond to two probes [S57] |
| Lithuania | 52.0 | e-TAR blocks scripts (Cloudflare 403) [S52]; third Baltic state adds little |

**Recommendation.**
- **Primary: Italy.**
- **Runner-up: Denmark.**

The 1-point gap is within scoring judgement, so it is **not** a decisive margin. The sensitivity table shows that the winner flips with the weighting:
- A **cheap internal pilot** (access and maintenance doubled, client value zero) → **Denmark** first (81.8 vs Italy 73.6).
- A **client product** → **Italy** (80.3 vs 75.4).

**Denmark becomes preferable if any of these happens:**
1. The Normattiva API or its reuse terms fail verification in Sprint 0.
2. Gold-standard cells for Italy take more than 1.5× the median time of the other layers (regional fragmentation).
3. The audience is internal research with a tight hours budget.
4. The audience is livestock, nitrates or fur oriented, where Denmark is the more distinctive case.

## D.4 Authorities to map per country (owner of guidance distinct from binding law)

For each layer the gold-standard researcher records the ministry or agency responsible in five areas, plus whether it publishes **guidance** (not binding) separately from law:
- agriculture/CAP paying agency
- labour inspectorate
- environment/water authority
- food/veterinary authority
- OSH authority

These names were **not verified in this session**: listing ~50 bodies from memory would breach the no-fabrication rule. **UNKNOWN; resolved in Sprint 0 (10-plan-30-60-90.md, task S0-4).** Verified so far: RVO is the Dutch manure/derogation authority [S28].

## D.5 Failed or incomplete access attempts (kept visible)

| Attempt | Result | What depends on it |
|---|---|---|
| EUR-Lex HTML by script | HTTP 202, empty body (WAF challenge) | Nothing; Cellar works |
| Légifrance HTML, robots.txt | HTTP 403 Cloudflare | Nothing; DILA bulk works |
| e-TAR (Lithuania) | HTTP 403 Cloudflare | Lithuania scored low partly for this |
| legislatie.just.ro (Romania) | no response in 30–40 s, twice | Romania scored low; may be transient |
| api.normattiva.it | no response | Italy's access score (3/5) is provisional |
| KOOP SRU | records returned with status 406 | NL route works, but the status anomaly must be understood before automating |
| Riigi Teataja API terms | none found | Permission to automate in Estonia: UNKNOWN |
| Hetzner and DeepL API prices | JavaScript-rendered, not readable | €36/month and DeepL costs stay UNVERIFIED |
