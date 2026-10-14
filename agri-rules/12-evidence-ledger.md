# M. Evidence ledger and sources

*Research date for every row: 14 October 2026. Source IDs → [`evidence/sources.csv`](evidence/sources.csv) (57 sources with publisher, title, URL, jurisdiction, language, dates, locator, consolidation status, licence, access method). Probe log → [`evidence/probe-log.txt`](evidence/probe-log.txt); response hashes → [`evidence/snapshot-hashes.csv`](evidence/snapshot-hashes.csv); robots.txt copies → [`evidence/robots/`](evidence/robots/).*

**Categories:**
- **VF** = VERIFIED FACT (read in the official source this session)
- **VF-s** = verified only through a search-tool extract of an official page (re-read directly before reliance)
- **CALC** = calculation
- **ASSUMP** = assumption
- **INTERP** = interpretation
- **REC** = recommendation
- **UNK** = unknown

## M.1 Legal-source and access claims

| ID | Claim | Cat. | Source | Date of fact | Exact supporting location | Conflict / caveat | Conf. | Disconfirming evidence sought | Remaining unknown |
|---|---|---|---|---|---|---|---|---|---|
| E-L01 | Working Time Directive limits average weekly working time to 48 h | VF | S01 | OJ L 299, 18.11.2003 | Art 6(b) | Original act, not consolidated | H | Searched text for agriculture-specific exemption from Art 6: none found (derogations in Art 17(3) cover rest/reference periods) | — |
| E-L02 | Agriculture is named in Art 17(3)(c)(vii) and (d)(i); reference periods derogated under Art 17(3) may not exceed 6 months (12 by collective agreement) | VF | S01 | 2003 | Art 17(3), Art 19 | — | H | — | National transpositions |
| E-L03 | Nitrates Directive caps livestock manure at 170 kg N/ha/year (with derogation mechanism) | VF | S02 | 1991 | Annex III(2) | Derogations by separate Commission decisions | H | — | Current derogation list (IE etc.) |
| E-L04 | Seasonal Workers Directive: member states set a max stay of 5–9 months in any 12 | VF | S03 | 2014 | Art 14(1) | — | H | — | National choices |
| E-L05 | Cellar CELEX 32021R2115 returns the original CAP Strategic Plans Regulation, not the consolidated version | VF | S05 | 2021 original | Fetched text: GAEC annex as originally adopted | Consolidated texts use CELEX 0…-date | H | — | Exact consolidated CELEX for 2026 |
| E-L06 | EUR-Lex consolidated texts have no legal effect; the electronic OJ is authentic since 1 Jul 2013 | VF-s | S06 | — | EUR-Lex help (search extract) | EUR-Lex HTML blocked to scripts | M | — | Read the page in a browser |
| E-L07 | CAP simplification (2025/0236(COD)) passed Parliament 16.12.2025; Council final approval reported Dec 2025 | VF-s (EP) / secondary (Council) | S54 | Dec 2025 | EP position C/2026/2168 | Regulation number and OJ reference not found | M | Searched EUR-Lex-style titles; none returned | **UNK:** final act number and GAEC changes |
| E-L08 | gesetze-im-internet.de offers XML + daily TOC; texts are non-official consolidations; deep links allowed | VF | S08, S09 | — | Hinweise page | No explicit reuse licence | H | — | Reuse licence |
| E-L09 | NeuRIS API is a trial service with an incomplete dataset; bulk XML planned | VF | S11, S12 | — | docs.rechtsinformationen.bund.de | Answered keyless on probe | H | — | Rate limits; GA date |
| E-L10 | Riigi Teataja exposes a keyless JSON search API (164,539 acts on probe) | VF (probe) | S13 | 2026-10-14 | `/api/oigusakt_otsing/1/otsi` | Undocumented publicly | H (exists) | Searched for docs/terms: none found | **UNK:** permission and stability |
| E-L11 | Estonian consolidated texts in Riigi Teataja are official and have legal force | VF-s | S14 | from 1.6.2002 | RTS § 3(1); N-Lex description | — | M | — | Read RTS § 3 directly |
| E-L12 | likumi.lv content is informative; the official publication prevails | VF-s | S16 | — | likumi.lv "par mums" (search extract) | — | M | — | — |
| E-L13 | Latvian Labour Law: overtime supplement ≥100 %; a general agreement may set ≥50 % under a wage condition; overtime ≤ avg 8 h per 7 days over ≤4 months | VF | S15 | consolidated version on 2026-10-14 | Darba likums 68. p. (1),(3); 136. p. (5) | likumi.lv is informative (E-L12) | H | — | Whether an agricultural general agreement exists |
| E-L14 | ArbZG § 3: 8 h/working day, up to 10 h if 6-month/24-week average ≤ 8 h | VF | S10 | consolidated (non-official) | § 3 | — | H | — | — |
| E-L15 | Riksdagen open data is free to use without fees or licences, with attribution; SFS search works keyless | VF | S17 | — | Open-data page; probe | Legal status of the consolidated SFS not confirmed | H | — | Consolidated SFS status |
| E-L16 | Since 1 Apr 2018 Swedish laws are promulgated by electronic publication on svenskforfattningssamling.se | VF-s | S18 | 2018 | SFS 2018:159 | — | M | — | — |
| E-L17 | Polish Sejm ELI API answers keyless (Dz.U. 2023: 2,824 items) | VF (probe) | S19 | 2026-10-14 | `/eli/acts/DU/2023` | No terms found | H | — | Terms |
| E-L18 | ISAP unified texts are informational; official consolidation = tekst jednolity by obwieszczenie | VF-s / secondary | S20 | — | — | Training slide + university course | M | — | — |
| E-L19 | Légifrance API: free after PISTE registration; Licence Ouverte 2.0 + CGU; quotas per token | VF | S21 | — | data.gouv.fr dataservice page | CGU PDF dated 2020 may be outdated | H | — | Current quotas |
| E-L20 | DILA LEGI and KALI bulk directories are reachable without an account | VF (probe) | S22 | 2026-10-14 | Directory listings HTTP 200 | — | H | — | — |
| E-L21 | legifrance.gouv.fr, e-TAR and EUR-Lex HTML block scripted requests (403/202) | VF (probe) | S23, S52, log | 2026-10-14 | HTTP status in log | Could differ for browsers | H | — | — |
| E-L22 | BOE consolidated texts are "sin valor oficial"; cover state and autonomous-community laws; reuse must say so | VF | S24, S25 | — | FAQ consolidada | — | H | — | Rate limits |
| E-L23 | wetten.overheid.nl robots.txt explicitly disallows AI/LLM crawlers (GPTBot, ClaudeBot, CCBot …) | VF | S26 | 2026-10-14 | robots.txt lines 77–120 | Applies to the website, not necessarily to KOOP SRU open data | H | — | — |
| E-L24 | KOOP SRU returns BWB records (but with HTTP 406) | VF (probe) | S27 | 2026-10-14 | Probe | Status anomaly | M | — | **UNK:** why 406 |
| E-L25 | Netherlands has no nitrates derogation from 2026; 170 kg N/ha applies | VF-s | S28 | 2026 | RVO derogatie page (checked 10 Mar 2026) | Pre-2026 sources say otherwise (superseded) | M-H | Searched for a 2026 Commission reversal: none found | Outcome of the Feb 2026 new request |
| E-L26 | Latvia bans fur farming from 1 Jan 2028; Constitutional Court upheld it (2024) | VF-s | S30 | adopted 22.9.2022 | Dzīvnieku aizsardzības likums Art 13.1 + transitional provisions | — | M-H | — | — |
| E-L27 | Estonia bans fur farming from 1 Jan 2026 | Secondary | S31 | adopted 2021 | Loomakaitseseadus § 41; § 81¹(12) | Not read in Riigi Teataja | M | — | Read RT |
| E-L28 | Poland: fur-animal farming ban (rabbit excepted), existing farms to 31 Dec 2033 | Secondary | S29 | Dz.U. 2025 poz. 1696 | Art 12 ust. 4c–4d | Other sources say 2034 | M | Conflict noted (2033 vs 2034) | Read Dz.U. via Sejm API |
| E-L29 | The Commission's follow-up to "Fur Free Europe" was due by March 2026 | VF-s | S32 | 2025-08-01 | ECI news item | Advocacy sources say it was delayed again | M | Searched for an adopted communication: none found | **UNK:** outcome |
| E-L30 | Official APIs answered for DK, FI, AT; Normattiva portal answered but `api.normattiva.it` did not; Romanian portal timed out | VF (probe) | S48–S51, S57 | 2026-10-14 | Log | Single probe each | M | — | Italy API; Romania |

## M.2 Market, price and service claims

| ID | Claim | Cat. | Source | Date | Location | Caveat | Conf. | Remaining unknown |
|---|---|---|---|---|---|---|---|---|
| E-P01 | Anthropic: Opus 5.5 $4/$20, Sonnet 5.5 $2/$10, Haiku 5.5 $0.10/$0.50 (≤100K), Fable 5.1 $10/$50; batch −50 % | VF | S34 | 2026-10-14 | claude.com/pricing | USD | H | — |
| E-P02 | OpenAI: gpt-6-astra $10/$50; gpt-5.4-mini $0.75/$4.50; nano $0.20/$1.25; batch −50 % | VF | S35 | 2026-10-14 | developers.openai.com pricing | — | H | — |
| E-P03 | Google: Gemini 3.1 Pro preview $2/$12 (≤200k); 3.8 Flash $0.75/$3.75; 3.5 Flash-Lite $0.30/$2.50; paid tier not used to improve products | VF | S36 | 2026-10-14 | ai.google.dev pricing | Scheduled increases end-2026/2027 | H | Exact new prices |
| E-P04 | Mistral Large $0.50/$1.50 | VF | S37 | 2026-10-14 | mistral.ai/pricing | Other Mistral prices not shown | M | OCR price |
| E-P05 | OpenRouter: 5.5 % fee on credits (Standard), no per-request fee; ZDR routing on all plans | VF | S38 | 2026-10-14 | openrouter.ai/pricing | — | H | — |
| E-P06 | OpenRouter load-balances by default; pinning needs `order`/`only` + `allow_fallbacks:false` | VF | S39 | 2026-10-14 | Provider routing docs | — | H | Deprecation policy |
| E-P07 | Brave Search API $5/1,000 requests; storage needs a plan with storage rights | VF | S42 | 2026-10-14 | brave.com/search/api | — | H | Which plans include storage |
| E-P08 | Tavily $0.008/credit; 1,000 free/month; basic search 1 credit | VF | S43 | 2026-10-14 | Pricing + credits doc | — | H | — |
| E-P09 | n8n Sustainable Use License limits use to internal business or non-commercial purposes | VF | S44 | current | LICENSE.md "Limitations" | Applicability to a client product = legal question | H | Lawyer reading |
| E-P10 | ECB: 1 EUR = 1.1188 USD on 2026-10-13 | VF | S47 | 2026-10-13 | ECB EXR | — | H | — |
| E-P11 | Anthropic deletes API inputs/outputs within 30 days by default | VF | S45 | — | privacy.claude.com | — | H | Training statement |
| E-P12 | OpenAI: no training on API data by default; abuse logs ≤30 days; ZDR needs approval | VF | S46 | — | your-data guide | — | H | — |
| E-C01 | 2024 agricultural-industry output: FR €88.3bn, DE €75.5bn, IT €70.2bn, ES €68.7bn, NL €41.3bn, PL €39.5bn, RO €20.2bn, DK €12.6bn, IE €12.5bn, AT €9.9bn, SE €7.5bn, FI €5.5bn, LT €4.4bn, LV €1.9bn, EE €1.3bn | VF | S33 | dataset updated 2026-05-13 | aact_eaa01, AM180000, PRD_BP, MIO_EUR, 2024 | Basic prices | H | — |
| U-07 | DeepL API price | UNK | S56 | — | Official page did not render API prices | Third-party figures conflict | — | Read developers.deepl.com in a browser |
| U-08 | Server ~€36/month for 4 vCPU/8 GB | UNK | S55 | — | Prices JS-rendered | Spec CPX32 = 4 vCPU/8 GB confirmed | — | Read in a browser if ever needed |

## M.3 Calculations, assumptions, interpretations

| ID | Claim | Cat. | Where |
|---|---|---|---|
| E-X01 | "10th country" = 10th comparison layer (EU + 9 countries); consistent with the brief's ~1,000 comparisons = 100 × 10 | INTERP | 03 §D.3 |
| E-X02 | Italy 79.0 vs Denmark 78.0 on the weighted rubric; the winner flips under a cheap-internal weighting | CALC (on INTERP scores) | `models/country_score_results.md` |
| E-X03 | Full AI pass €18 / €330 / €1,654 ex VAT | CALC (on ASSUMP tokens) | `models/cost_model_results.md` |
| E-X04 | Pilot ≈ 265 h base (138–490) | CALC (on ASSUMP hours) | 07 §H.3 |
| E-X05 | 0 errors in n samples → 95 % upper bound ≈ 3/n | CALC (rule of three) | 08 §I.4 |
| E-X06 | One page cannot hold 10 layers with evidence (~1,750 words) | CALC (on ASSUMP word counts) | 09 §J.1 |
| E-X07 | Human review time, not AI cost, dominates the budget | INTERP from E-X03/E-X04 | 07 |
| E-X08 | All national-authority names (agency per domain per country) | UNK, deliberately not listed from memory | 03 §D.4 |
| E-X09 | EU instruments named in `rule-list.csv` without an [S##] tag | ASSUMP (background knowledge); verify during gold preparation | 02 |

## M.4 Disconfirming searches performed

- Searched for evidence that Estonia has **no** API → found a working API instead (E-L10).
- Searched for an official German statement that NeuRIS is production-ready → found the opposite (E-L09).
- Searched for a 2026 reversal of the Dutch derogation decision → none found (E-L25).
- Searched for an adopted Commission fur-farming act → none found (E-L29).
- Searched for an official DeepL API price and Hetzner price → not readable; left UNKNOWN rather than substituting third-party figures.
- Checked whether the proposal's €590/run is outside plausible bounds → it is inside the modelled range, so not refuted (E-X03).
