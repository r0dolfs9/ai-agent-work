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
