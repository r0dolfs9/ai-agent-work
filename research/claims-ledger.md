# Claim and conflict ledger

Labels: **VF** = VERIFIED FACT (primary or close-to-primary source read) · **CALC** = CALCULATION · **ASM** = ASSUMPTION · **INT** = INTERPRETATION · **REC** = RECOMMENDATION · **UNK** = UNKNOWN.
Confidence: H/M/L. "Location" points into the source register entry (`key_extract_and_location`) or the cited section. Retrieval date for all entries: 2026-10-12.

## A. Load-bearing claims used in the paper

| ID | Claim (as used in paper) | Label | Source(s) | Scope / caveat | Conf. |
|---|---|---|---|---|---|
| L01 | Leading builders distinguish *workflows* (LLMs and tools on predefined code paths) from *agents* (LLM dynamically directs its own process and tool use). They advise starting with the simplest solution. | VF | S001 | Vendor definition, Dec 2024 | H |
| L02 | Autonomy can be framed as five user roles (operator, collaborator, consultant, approver, observer), and is a design choice separate from capability. | VF | S002 | Academic framework | H |
| L03 | 17% of organizations had deployed AI agents (Gartner 2026 CIO survey). More than 60% expect to within two years. | VF (via extract) | S005 | Gartner blocks fetch; sample size unknown | M |
| L04 | At organizations with more than $1bn revenue, 40% report scaling AI agents (27% a year earlier). Smaller organizations are flat at 22%. | VF (via extract) | S004 | Self-reported; "scaling" not defined | M |
| L05 | 32% of respondents say their organization declined to buy software because it could be built in-house with agentic coding tools. | VF (via extract) | S004 | Self-reported | M |
| L06 | On real paid freelance projects, the best agent reached a 15.8% automation rate (Jul 2026), up from 2.5% (Oct 2025). | VF | S037, S038 | Human-judged; sample size undisclosed | H |
| L07 | METR: time horizons are still growing exponentially. Measurements above 16h are unreliable. Tasks are self-contained. | VF | S008 | Software/ML/cyber tasks only | H |
| L08 | Rigorous productivity RCTs on experienced developers are inconclusive: −19% (early 2025), then estimates of an 18%/4% speed-up with wide CIs (late 2025) that METR itself treats as weak. | VF | S070 | Small samples | H |
| L09 | 66% of developers who use AI use coding agents. Only 20% use AI for deploying/operating production. 93% require source attribution to trust AI. | VF | S062 | Self-selected survey | H |
| L10 | Prompt injection is unsolved. OpenAI says it is "unlikely to ever be fully solved". Anthropic's browser agent saw 23.6% attack success before mitigations and 11.2% after. | VF (via news/vendor) | S069, S068 | Vendor self-tests, 2025 | M |
| L11 | The "lethal trifecta" (private data + untrusted content + external communication) is the key design risk. | VF | S011 | Expert framing | H |
| L12 | OWASP published an Agentic Top 10 (ASI01–ASI10) on 2025-12-09. | VF | S010 | Item names via secondary | M |
| L13 | MCP's 2026-07-28 spec removed sessions and the initialize handshake (stateless), added `server/discover`, moved Tasks to an extension, deprecated Roots/Sampling/Logging and DCR, and adopted a ≥12-month deprecation policy. | VF | S032 | Spec text | H |
| L14 | MCP, goose and AGENTS.md were contributed to the Linux Foundation's Agentic AI Foundation (2025-12-09). It reported more than 10,000 published MCP servers and more than 60,000 projects adopting AGENTS.md. | VF | S034 | Self-reported counts | H |
| L15 | A2A v1.0 is the latest released version. The Linux Foundation reports more than 150 supporting organizations and integration in Azure/Bedrock AgentCore, but names no production customers. | VF | S035, S036 | "Support" ≠ use | M |
| L16 | OpenAI scaled back ChatGPT Instant Checkout in March 2026 ("did not offer the level of flexibility…"), letting merchants use their own checkout and focusing on discovery. | VF (via extract) | S025 | Direct fetch 403 | M |
| L17 | Adjusted x402 volume is about $19M across ~134M transactions (to Apr 2026). The top ~1% of buyers make up ~90% of adjusted volume. | VF (secondary of on-chain analysis) | S028 | Internal inconsistency | M |
| L18 | Card networks have announced "first live agentic transactions" in many markets but disclose no volumes. Visa reported "hundreds" of controlled transactions. | VF | S021, S022 | Company PR | M |
| L19 | Agents show strong position/first-proposal bias and unstable, model-dependent preferences. There is no stable universal "agent buying preference". | VF + INT | S029, S030 | Simulations / mock markets | H (finding) / M (generalisation) |
| L20 | In Project Deal, a stronger model negotiated better prices, and users represented by the weaker model did not notice (fairness 4.05 vs 4.06). | VF | S040 | 69 employees, pilot | H |
| L21 | Agent-run shop experiments show agents are easily persuaded into discounts and near-illegal deals. "Bureaucracy matters." | VF | S039 | Vendor experiment | H |
| L22 | The Ninth Circuit (2026-08-04) vacated Amazon's injunction against Perplexity's Comet: the user, not the agent developer, "accessed" Amazon. ToS claims remain open. | VF | S015 | US; preliminary stage | H |
| L23 | Amazon blocked Meta's Muse agent (2026-09-20) under its Conditions of Use, citing non-identification and credential capture. | VF | S063 | — | H |
| L24 | Anthropic's terms: subscription OAuth is for native apps only. Third-party developers must use API keys. Enforcement may occur "without prior notice". | VF | S016 | — | H |
| L25 | Google users reported 403 ToS suspensions after using subscription OAuth through OpenClaw/OpenCode (Feb 2026). | VF (user reports) | S075 | Reports, not policy | M |
| L26 | Cloudflare: from 2026-09-15, new domains block "Agent" and "Training" bots by default on pages that display ads. | VF (via extract) | S019 | Implementation not confirmed | M |
| L27 | EU AI Act Art. 50 interaction-disclosure duties apply from 2026-08-02 and cover AI agents interacting with people. High-risk Annex III rules are deferred to 2027-12-02. | VF | S074, S049 | Not legal advice | H/M |
| L28 | NIST CAISI launched an AI Agent Standards Initiative (Feb 2026). There is no finalized agent identity standard. | VF (secondary) | S050 | — | M |
| L29 | Six Five-Eyes agencies issued joint agentic AI guidance (May 2026) recommending layered defence and strict access control. | VF | S051 | Full PDF not read | M |
| L30 | Usage is time-patterned for chat (weekday work, weekend personal). No public hourly data exists for autonomous/API agent activity. | VF + UNK | S041, S043 | Single providers | H |
| L31 | Anthropic run-rate reached ~$65bn by end-July 2026. Claude Code exceeded $2.5bn (Feb 2026). | VF (press of company statements) | S053 | Run-rate ≠ revenue | M |
| L32 | Salesforce Agentforce ARR exceeded $1.5bn (Q2 FY27), but the definition was broadened that quarter. | VF | S055 | Definition change | H |
| L33 | 2030 "AI agents market" estimates cluster at $48–53bn, but 2025 base estimates differ by more than 2x. | VF + INT | S056 | Paywalled methods | L |
| L34 | McKinsey: up to $1trn US / $3–5trn global agent-orchestrated retail goods revenue by 2030. This includes AI-influenced purchases. | VF | S057 | Scenario | M |
| L35 | AI-referred retail traffic is growing fast and converting better (Adobe). This is mostly human click-through, not agent purchases. | VF + INT | S031 | Panel data via press | M |
| L36 | In the base production-support scenario, tokens are ~8% of cost, human escalation ~74%, and fixed engineering/infra/security ~17%. | CALC | models/cost_model_results.md | Assumption-driven | M |
| L37 | Agent/LLM API economics: caching roughly halves per-task token cost in the base loop ($0.20 vs $0.45). | CALC | cost model | Assumes linear context growth | M |
| L38 | Outcome-based pricing exists ($0.99 per Fin outcome). | VF | S071 | Vendor definition of outcome | H |
| L39 | Consumer willingness to delegate full purchasing is low (9% open to fully autonomous purchases including payment). Attitudinal "trust" headlines are much higher. | VF | S067 | Stated preferences | M |
| L40 | No card-network rule yet allocates liability specifically for agent-initiated disputes. | VF (vendor commentary) + UNK | S066 | Not authoritative | L |

## B. Conflicts and contradictory evidence

| ID | Topic | Conflict | Resolution in paper |
|---|---|---|---|
| C001 | Enterprise agent adoption | Gartner reports 17% deployed (S005). McKinsey reports 22–40% "scaling" (S004). A Gartner application-leaders poll reports 75% "piloting/deploying/deployed". | Different questions and populations. The paper reports a range and explains the definitions. It does not average them. |
| C002 | Agent project failure | Gartner predicts >40% of projects canceled by 2027 (S006) vs. rapid revenue growth at vendors (S053–S055). | Both can be true: spend concentrates in coding and a few workflows, while many generic projects fail. Reported as such. |
| C003 | METR doubling time | Secondary sources give 4.3 months, ~7 months or 49 days. METR's own page gives no number now (S008, S009). | The paper says "exponential, doubling on the order of months" and cites the METR page. It does not give a precise figure. |
| C004 | OpenClaw exposed instances | 30k (Bitsight) vs 42k vs 135k+ (SecurityScorecard) (S014). | The paper reports "tens of thousands to over a hundred thousand" with low confidence. |
| C005 | Anthropic third-party harness policy | One blog claims a May 2026 reversal. The current Anthropic docs (S016) still restrict subscription OAuth to native apps. | The primary current docs win. The reversal is unverified. |
| C006 | x402 scale | Coinbase gross count of 160M+ "agentic payments" vs adjusted ~$19M volume, with roughly half of activity "gamified" (S028). | The paper uses the adjusted figures and flags that gross counts overstate commerce. |
| C007 | Anthropic API sample definition | The March report includes Claude Code in the API sample. The June report excludes it (S042, S041). | No cross-report trend is computed. |
| C008 | Amazon agent terms effective date | 2025-05-30 vs 2026-03-04 (S064). | The paper says Amazon's Conditions of Use contain agent-identification requirements, without a date. |
| C009 | Consumer trust in agent purchasing | Accenture reports 74% "trust" (attitudinal), 9% fully autonomous (S067). Riskified reports 55% not comfortable. | Behavioural or narrow measures are favoured. Both are reported. |
| C010 | Instant Checkout status | Retired (blogs) vs available to approved partners (OpenAI dev docs) (S025, S027). | "Scaled back; limited to approved partners/apps." |
| C011 | Cursor revenue | $1bn disclosed (Nov 2025) vs $4bn press-reported (Jun 2026) (S054). | The paper cites the disclosed figure and says later ones are press-reported. |
| C012 | Agentforce growth | 240% growth headline vs broadened ARR definition (S055). | Both are reported. |
| C013 | Market sizing | Base-year estimates span $3bn–$7.8bn (2025) while 2030 estimates converge (S056). | Treated as low-confidence. The paper shows why convergence is not corroboration. |
| C014 | Coding-agent productivity | Vendor/user claims of large gains vs RCTs (S070) and the "developers overestimate gains" finding. | Reported as unresolved. The cost model does not assume productivity multipliers. |

## C. Unknowns (explicit evidence gaps)

| ID | Unknown | Why it matters | Best lawful alternative |
|---|---|---|---|
| U01 | Production resolution / success rates by use case, independently measured | Dominant cost driver (L36) | Run your own pilot with a holdout. Pay for an analyst dataset. |
| U02 | Volume of fully agent-completed purchases (not referrals) | Sizing agent commerce | Network/PSP disclosures (none yet). Merchant-side logging of signed agents (TAP/Web Bot Auth). |
| U03 | Hour-of-day / weekday patterns of autonomous agent activity | Scheduling, capacity, "purchase windows" | Own telemetry. Cloudflare Radar agent categories (not examined in depth). |
| U04 | Frequency of platform bans for agent use and appeal success rates | Platform risk | Community reports only. No platform publishes counts. |
| U05 | Insurance pricing for agent risks | Cost of risk transfer | Broker quotes (needs approval to contact). |
| U06 | Liability allocation in agent payment disputes | Commerce risk | Watch Visa/Mastercard rule releases and the CFPB/HM Treasury outcomes. |
| U07 | Enterprise budgets earmarked for agent tooling | Opportunity sizing | Customer interviews (needs approval). |

## D. v1.1 updates (limitations follow-up, 2026-10-12)

### D.1 Amended v1.0 claims

| ID | v1.1 status | Change |
|---|---|---|
| L03 | VF (read on Gartner-hosted mirror, S098) | Sample size still not published → representativeness UNKNOWN |
| L04, L05 | VF (read on McKinsey-hosted mirror, S084) | n=1,719, 97 nations, GDP-weighted; "scaling" undefined; figure is share of *respondents* at large orgs |
| L17 | **REPLACED** | $19M/134M and top-1% concentration (social media via S028) → Visa report $15.0M / 109.6M to 2026-04-21 (S091); TRM screened $25.62M, agentic 0.6–7.5% (S090) |
| L31 | Re-sourced | $14bn (Feb) and >$47bn (May) run-rate and Claude Code >$2.5bn = company-disclosed (S088); $65bn = single anonymous source (S089) |
| L33 | Extended | Gartner primaries: agents & assistants $29.2bn (2026) vs agentic software $985bn (2030) (S082, S083); "$202bn" (S058) **removed** |
| L34 | VF (S086) | Method footnote recorded ("US Census data and forecasted adoption rates"); "orchestrated revenue" undefined |
| L35 | Re-sourced (S116) | May 2026 +138% YoY, 54% better conversion; "AI-referred" undefined by source |
| L39 | VF (S115) | 16 countries incl. 5 EU states + UK; 9% vs 12% internal inconsistency |
| L10 | Partially strengthened | Primary title/text extract S118; Atlas itself deprecated (S117) |

### D.2 New load-bearing claims

| ID | Claim | Label | Source(s) | Caveat | Conf. |
|---|---|---|---|---|---|
| L41 | 20.0% of EU enterprises (10+ staff) used any AI technology in 2025; Latvia 12.2%; range 5.2–42.0% | VF | S096 | AI in general, not agents | H |
| L42 | OECD's 25-organisation, 11-country interviews: agentic AI moving into workflows; safeguards = incremental autonomy, human checkpoints; "illustrative rather than representative" | VF | S097 | Qualitative | H |
| L43 | Gartner Jan 2025 investment poll respondents were 3,412 webinar attendees | VF | S087 | — | H |
| L44 | Coding-agent PRs (2.74M, Dec 2024–Oct 2025): weekend share 25.8% vs 28.6% uniform; peak/trough hourly ratio 1.57 (UTC) | CALC | S093; research/analysis/aidev_timing.py | Creation time ≠ activity; public GitHub only; no human baseline | M |
| L45 | Agent web-fetch traffic follows weekly human rhythms; daily agent requests +1,700% YoY | VF (vendor) | S092 | No figures for rhythm | M |
| L46 | Anthropic H1 2026: 11.4M banned accounts, 398k appeals, 42k overturned (all causes) | VF | S094 | No denominator; not agent-specific | H |
| L47 | No public agent-specific ban rate (numerator + exposure denominator) found within documented search scope | UNK | §3 of limitations-resolution | — | — |
| L48 | Plausibly agentic x402 commerce ≈ $0.15M–$1.9M cumulative (≈$5–11k/month recently) | CALC + VF | S090 | Agent vs script indistinguishable | M |
| L49 | Latvia: CIT 20% of gross distributed profit, retained profits untaxed; alt regime 15% + 6% PIT | VF | S100 | Professional summary | H |
| L50 | Latvia VAT standard 21%; registration threshold €50,000 | VF | S100, S099 | — | H |
| L51 | Supplying B2B services to taxable persons in other Member States, or receiving B2B services from abroad, disapplies the €50,000 registration exemption (s.59(4), s.59(6)) | VF (statute text, outdated translation) + ⚖ | S099 | Translation valid 2024; confirm current text | M |
| L52 | Micro-enterprise tax requires not being a VAT payer and turnover ≤ €50,000 → likely incompatible with buying foreign APIs | INT ⚖ | S100 + L51 | Needs accountant | L-M |
| L53 | B2C cross-border electronically supplied services: customer-country VAT via Union OSS above €10,000 (current + previous year) | VF | S103 | — | H |
| L54 | Latvian B2B e-invoicing mandatory from 2028-01-01 (B2G since 2025) | VF (secondary) | S101 | Not checked on likumi.lv | M |
| L55 | SIA: state fee €75; capital ≥ €2,800 (or reduced-equity SIA); IK fee €30 | VF | S102 | Page shows "(?)" on some figures | M-H |
| L56 | Stripe Latvia: EEA standard 1.5% + €0.25; international 3.15% + €0.25; +2% FX; disputes €20; Paddle 5% + $0.50 | VF | S104, S105 | Prices change | H |
| L57 | Seller keeps €44.5–48.0 of a €49 net subscription depending on route and customer type | CALC | models/operator_economics.py | Excludes non-EU taxes | M |
| L58 | Latvia is supported for Claude API/Claude.ai and OpenAI API; Russia, Belarus, China, Iran not on Anthropic's list | VF | S106 | Lists change | H |
| L59 | EU sanctions (Art. 5n Reg. 833/2014) prohibit IT consultancy and enterprise-management software for Russia-established entities; FIU authorisation needed for subsidiaries since 2024-10-01 | VF | S112 | Check consolidated text | H |
| L60 | AI Act dates: in force 2024-08-01; prohibitions and AI literacy from 2025-02-02; GPAI 2025-08-02; Art 50 2026-08-02; Annex III 2027-12-02; Annex I 2028-08-02 | VF | S107 | — | H |
| L61 | Revised Product Liability Directive covers software for products placed on the market after 2026-12-09; AI Liability Directive withdrawn | VF (secondary) | S111 | Transposition uneven | M |
| L62 | Receiving and forwarding funds is a PSD2 payment service; commercial-agent exclusion narrow | VF (regulator Q&A) | S114 | Not legal advice | M |
| L63 | Labour-cost jurisdiction: base production saving 33% (US) vs 22% (Latvia average) vs 39% (Germany average) | CALC | S119; cost model | Whole-economy averages; engineering at US rates | M |
| L64 | OpenAI deprecated the Atlas browser (announced 2026-07-09; stops 2026-08-09) | VF (search extract of help center) | S117 | Primary not read | M |

### D.3 New conflicts

| ID | Topic | Conflict | Resolution |
|---|---|---|---|
| C015 | x402 adjusted volume | Visa report $15.0M / 109.6M (to 2026-04-21) vs Visa executive's post ~$19M / ~134M | Report used; post not reproduced in report |
| C016 | Accenture autonomous-purchase share | 9% vs 12% within the same publication | Both reported; 9% used as "initiate and complete" |
| C017 | Gartner "agent market" size | $29.2bn (2026 agents and assistants) vs $985bn (2030 agentic software spend) | Different definitions; both reported, with the definitional warning |
| C018 | Anthropic EU billing entity | Third-party guides: US PBC with non-resident VAT; job posting: Ireland as primary EU billing entity | Unresolved; check invoices (S120) |
| C019 | Latvian VAT threshold test | 12-month test (2024 translation) vs calendar-year test (2025 secondary sources) | Calendar year per KPMG/secondary; confirm with current law |
| C020 | Alternative CIT regime value | Calculated owner take ~equal to standard regime | Flagged ⚖; possible features not captured by summaries |

### D.4 Unknowns: status after v1.1

| ID | Status |
|---|---|
| U01 production resolution rates | Unchanged (UNKNOWN) |
| U02 value of agent-completed purchases | Narrowed: bounded examples (L48); global total UNKNOWN |
| U03 timing of autonomous agents | Narrowed: coding-agent PRs and human-triggered agents covered; scheduled and continuous UNKNOWN |
| U04 ban frequency | UNKNOWN (rate); context improved (L46) |
| U05 insurance pricing | Unchanged |
| U06 payment dispute liability | Unchanged |
| U07 enterprise budgets | Partly informed by Gartner category spend (S082); budgets per buyer UNKNOWN |
| U08 (new) current consolidated text of Latvian VAT Law s.59 | UNKNOWN (outdated translation read) |
| U09 (new) Latvian bookkeeping/compliance costs | UNKNOWN (assumption €1.7–6.4k/yr) |
| U10 (new) non-EU indirect-tax registration duties for digital sales | Not researched; MoR recommended |

## E. v1.2 updates (decision package, 2026-10-12)

The handoff was treated as a navigation aid, not as proof. The high-impact claims were re-read at source on 12 Oct 2026.

### E.1 Re-checked claims

| ID | Claim | Re-check result | Label | Sources |
|---|---|---|---|---|
| L01/L64 | Atlas shut down | **Confirmed.** Announced 2026-07-09; deprecation 2026-08-09 (trade press, plus a tertiary source). OpenAI primary still returns 403 | VF (secondary) | S117, S138, S135 |
| (Anthropic revenue) | Run-rate "crossed $47 billion" (Series H post dated 2026-05-28); $65bn remains single-source press | **Confirmed** (primary re-read) | VF / weak | S088, S089 |
| (Anthropic bans) | 11.4M banned accounts, 398k appeals, 42k overturns, Jan–Jun 2026 | **Confirmed** (primary re-read). All causes; no denominator | VF | S094 |
| (x402) | ~$15.0M adjusted across 109.6M transactions, Artemis data to 2026-04-21, excluding identified wash and test activity | **Confirmed** (primary re-read) | VF | S091 |
| (market size) | Gartner $29.2bn 2026 "AI agents and assistants" | **Corroborated** via an independent republication; origin-host access path discontinued | VF | S082, S136, S137 |
| (market size) | ~$202bn "agentic AI spending 2026" | Attributed by secondaries to an earlier, broader 4Q25 Gartner forecast; still not found in a primary; **not cited** | UNKNOWN | S058 |

### E.2 Corrected and new load-bearing claims

| ID | Claim | Label | Source | Caveat | Conf. |
|---|---|---|---|---|---|
| L51 → **L65** | Supplying s.19(1) services to a taxable person of another Member State disapplies the €50,000 exemption (s.59(8)), so registration is needed before the first such sale. Receiving foreign services does **not**: since 2025-07-01 the recipient may keep the exemption via the s.139² special registration (s.59(9)). L51 is **withdrawn** | VF (current Latvian consolidated text) | S122 | Consolidated text informative; official publication prevails | H |
| L52 → **L66** | Micro-enterprise tax is compatible with s.139² special registration. It is lost if the payer supplies s.19(1) services to a VAT-registered person in another Member State or if turnover exceeds €50,000. Available only to natural persons registered with VID, individual merchants and similar (not an SIA). L52 is **withdrawn** | VF | S123, S124 | VID guidance dated 2025-06-27 | H |
| L67 | Under s.139², VAT on received services is paid without a right of deduction; monthly notice by the 20th; payment within 23 days | VF | S122 | — | H |
| L68 | 2026 self-employed contributions: 31.07% on income of at least €780 a month; 10% pension contribution otherwise or on the excess; PIT 25.5% up to €105,300 | VF (official-publisher consultation) | S125 | Non-binding; 2026 law changes reported but not verified | M-H |
| L69 | Occupation-adjusted base production saving: Latvia 17% (US engineering) / 28% (local engineering); Germany 38%/40%; EU27 35%/38% | CALC | S119, S126; cost model | Earnings ratios applied to labour cost | M |
| L70 | Paid demand: Upwork AI-related GSV +22% YoY in Q2 2026; AI Strategy & Consulting +50%; total GSV −4% | VF | S127 | Marketplace-specific; ~$330M annualised is a search extract | H (growth) / M (size) |
| L71 | Coding-agent training list prices: €890 per person for 2 days (Anthropic partner); mentor workshops from $250 / $500 / $900 | VF (list prices) | S128, S129 | No volumes | M |
| L72 | LLM security audit price bands: $6k–45k+; specialists $16k–50k; 5–25 days | VF (vendor guide) | S130 | Vendor with a selling interest | M |
| L73 | Cybersecurity is the top obstacle for 80% of 130 large US firms (Q4 2025) | VF | S131 | Small, large-firm, US sample | M |
| L74 | Route economics (revised after the independent commercial review): first-year take-home per owner hour €3.2–11.2 for a newcomer and €23.2–36.3 with a network; adverse first year is a loss on all routes; net Latvian professional benchmark ≈ €8.69/h | CALC | models/route_economics.py; S126; S100 | Prices, win rates and hours are ASSUMPTIONS | L-M |
| L75 | "B2B services = least admin" holds only for non-EU (or small Latvian) clients; any EU VAT-registered client forces full VAT registration and EU sales statements | INT from VF | S122, S124 | — | H |
| L76 | Recommendation: explore R2 (coding-agent enablement) if the owner codes; otherwise R4; R1 only with security credentials; defer R3; reject agent-bought products | REC | package/01-decision-brief.md | Conditional on unknown personal constraints and untested demand | — |

### E.3 Conflicts

| ID | Topic | Conflict | Resolution |
|---|---|---|---|
| C019 | Latvian VAT threshold test | 12-month test (2024 translation) vs calendar-year test | **Resolved:** the current s.59(1) text uses the current calendar year [S122] |
| C021 | v1.1 VAT conclusion vs current law | Outdated translation's s.59(6) vs current s.59(9) + s.139² | **Resolved** in favour of the current Latvian text; v1.1 statement withdrawn |
| C022 | Zendesk QA price | $25 / $35 / $50 in different secondary guides | Unresolved; used only as an order of magnitude [S134] |
| C024 | Contribution rule below €780 a month | v1.2 draft model charged 31.07% below €780; S125 says 10% pension only | **Resolved:** model corrected (finding from the independent factual review) |
| C025 | Cold B2B email as the V2 channel | Draft plan vs German UWG §7(2) consent rule | **Resolved:** cold email to German recipients removed; channel rule added [S139] |
| C023 | Route attractiveness | v1.1 numeric rank (security first) vs v1.2 entry gate (coding enablement first) | Entry gate decides; numeric score is ordinal (register v1.2 note) |

### E.4 Unknowns after v1.2

| Unknown | Status |
|---|---|
| U08 current consolidated Latvian VAT text | **RESOLVED** [S122] |
| Win rates, selling hours and acceptable prices for each route | UNKNOWN; only the validation plans can measure them |
| Professional-indemnity insurance price for an agent risk review | UNKNOWN (a quote requires approval) |
| Marketplace VAT treatment (who is the customer) | UNKNOWN; depends on the marketplace's invoicing model (adviser question; blocks first paid job) |
| Owner's skills, time, budget and contacts | UNKNOWN by design; the brief branches on them |
