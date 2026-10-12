## 11. Audits, governance and enforcement

### 11.1 What "auditing an agent" means in practice

| Activity | What is inspected | Who does it | Cadence | How findings are resolved |
|---|---|---|---|---|
| **Pre-launch evaluation** | Task success on a test set; failure categories; cost per task | Builders; increasingly specialist eval tools (e.g., Braintrust, LangSmith, Langfuse [S073][S048]) | Before each release, model change or tool change | Fix prompts and tools; gate the release |
| **Trace inspection** | Step-by-step logs of reasoning summaries, tool calls, inputs and outputs | Engineers, QA, auditors | Continuous sampling | Bug fixes; policy updates |
| **Human-calibrated quality review** | A sample of outcomes judged by people against a rubric. Automated judges can over-rate by 2–3× [S037] | QA teams, independent reviewers | Weekly or monthly | Retraining instructions; changes to escalation rules |
| **Permission review** | Which credentials, scopes and tools each agent holds | Security/IAM | Quarterly, and on change | Revoke; re-scope; rotate |
| **Spend reconciliation** | Model bills, tool fees, agent purchases versus budgets and receipts | Finance | Monthly | Adjust caps; investigate anomalies |
| **Security testing** | Prompt-injection and goal-hijack red-teaming; supply-chain review | Internal red team or external firm | Pre-launch plus periodic | Mitigations; containment |
| **Compliance review** | Disclosure (EU Art. 50), records, data protection, sector rules | Legal/compliance | On launch and when law changes | Process and UI changes |
| **Incident response** | What happened, blast radius, root cause | Security plus owners | On incident | Kill switch, rotation, notification, post-mortem |
| **Third-party certification and insurance** | Controls against a standard (e.g., AIUC-1, reported at 51 requirements) | Accredited auditors; insurers | Annual | Premium/coverage tied to audit results [S061] |

**INTERPRETATION.** Evaluation is turning into a market. Eval and observability vendors are well funded [S073], and insurance linked to agent audits has appeared, with the first live policy reported in February 2026 [S061]. Carriers and policy terms remain undisclosed, so treat this as early.

### 11.2 Regulation and public frameworks (as of 12 Oct 2026)

| Jurisdiction | Instrument | What it requires of agents | Status / date | Source |
|---|---|---|---|---|
| **EU** | AI Act Art. 50 | Providers of AI systems interacting directly with people (including AI agents) must disclose that it is AI unless obvious; content-marking duties | Applies from **2 Aug 2026** (marking for existing systems: 2 Dec 2026); fines up to €15m or 3% of turnover | [S074] |
| **EU** | AI Act high-risk rules (Annex III, e.g., hiring, credit) | Risk management, documentation, human oversight | **Deferred to 2 Dec 2027** by the AI Omnibus (in force 27 Jul 2026); product-embedded systems to 2 Aug 2028 | [S107] |
| **US** | NIST CAISI AI Agent Standards Initiative; NCCoE agent identity concept paper | Voluntary standards on security, identity and authorization, interoperability | Initiative launched Feb 2026; no final standard | [S050] |
| **US/UK/CA/AU/NZ** | Joint guidance "Careful adoption of agentic AI services" | Layered defence, strict access control; secure design and operation | Published ~1 May 2026 | [S051] |
| **Singapore** | Model AI Governance Framework for Agentic AI | Bound risks up front; keep humans meaningfully accountable; technical controls; end-user responsibility. Organisations remain legally accountable | Launched 22 Jan 2026 (voluntary) | [S052] |
| **China** | Administrative restriction (example) | State agencies, SOEs and banks restricted from running OpenClaw on office computers | Mar 2026 | [S013] |

Not legal advice. **UNKNOWN:** how national regulators (for example in Latvia or other EU member states) will prioritise Art. 50 enforcement.

### 11.3 Platform enforcement: policy versus observed action versus inference

| Platform | Documented policy | Observed enforcement | Appeal / recovery route | Our inference |
|---|---|---|---|---|
| Amazon | Conditions of Use require agents to identify themselves; no concealment [S064] | Lawsuit and injunction against Perplexity Comet (vacated on appeal) [S015]; block of Meta Muse with a block page [S063] | Commercial negotiation; litigation | Amazon will allow agents on its own terms. Unidentified agents and agents that capture credentials are the red lines |
| Anthropic | Subscription OAuth only for native apps; third parties use API keys; enforcement "without prior notice" [S016] | Server-side blocking of third-party harnesses (Jan–Apr 2026); some erroneous bans acknowledged by staff [S017] | Support; move to API-key billing | Treat subscription credentials as non-transferable |
| Google (Gemini/Antigravity) | Third-party tools using consumer plan access violate the ToS (as quoted by users) | Users report 403 "ToS violation" suspensions, including paid tiers, Feb 2026 [S075]; reports of a later automated unban are unverified | Forum appeals | Same pattern as Anthropic |
| LinkedIn | Bans bots and unauthorized automation for messaging, connecting, engagement and scraping [S076] | Restriction anecdotes; statistics unverified | Identity verification; appeal | High risk for outreach agents |
| Shopify | robots.txt: checkouts are for humans; use Checkout Kit [S065] | No enforcement cases found | n/a | Steers agents to sanctioned channels |
| Cloudflare-protected sites | Owner-chosen; default blocks Agent/Training bots on ad pages for new domains [S019] | Default in place from 15 Sep 2026 (implementation not independently confirmed) | Contact the site; become a signed/verified agent | Agent identity will become a ticket for entry |

**Lawful prevention and recovery (RECOMMENDATION).** This paper does not describe evasion techniques.
- **Identify honestly:** use declared user agents and signed requests (Web Bot Auth, TAP) [S059][S020].
- **Use official channels:** APIs, MCP servers, UCP/ACP, Checkout Kit.
- **Use the right credentials:** API keys, not subscription logins, for third-party tools [S016]. Never capture or store end-users' passwords for other sites [S063].
- **Respect rate limits and robots policies,** and keep logs that show you did.
- **If suspended:** stop the triggering automation, use the platform's appeal route, move to sanctioned access, and keep a second provider ready (§7.3).

#### 11.3.1 How often are agents banned? Separating rules, incidents and rates

A ban *rate* needs:
- a numerator (agent-related enforcement actions of one type);
- a denominator (agents or agent-using accounts exposed);
- the same defined period for both.

No platform publishes all three. What exists:

| Evidence type | Example | What it can support | What it cannot support |
|---|---|---|---|
| **Published rules** | Anthropic credential policy [S016]; Amazon Conditions of Use [S064]; LinkedIn User Agreement §8.2 [S076]; Shopify robots policy [S065] | Which agent behaviours are prohibited | How often enforcement happens |
| **Aggregate enforcement statistics (all causes)** | Anthropic, Jan–Jun 2026: **11.4M accounts banned; 398k appeals; 42k overturned** [S094] (Jul–Dec 2025: 1.45M banned, per earlier hub version). OpenAI publishes EU-only Digital Services Act data, not read because of a 403 [S095] | Scale of enforcement overall. Appeal overturn rate (42k/398k ≈ **10.6%** of appeals, ≈0.37% of bans; CALCULATION) | Agent-specific bans; a rate per active account (no denominator published); causes |
| **Individual incidents** | Third-party harness blocks (Jan–Apr 2026) [S017]; Google 403 suspensions (Feb 2026) [S075]; Amazon's block of Meta Muse (Sep 2026) [S063]; Perplexity litigation [S015] | That enforcement happens, its triggers and appeal paths | Frequency |
| **Site-level blocking shares** | Cloudflare: <1% of sites block search crawlers, 17% block training crawlers (2026) [S092]; default blocking of "Agent" bots on new domains' ad pages [S019] | Prevalence of *crawler* blocking among Cloudflare sites | Blocking of user-directed agents specifically (not published) |

**Types of enforcement are different events.** Count them separately:
- account suspensions or bans;
- API-key revocations;
- rate limits;
- automated-access blocks (HTTP 403 or block pages);
- payment restrictions;
- marketplace or registry removals (for example, malicious skills removed from ClawHub [S014]).

The Anthropic figure is account bans for all Usage Policy reasons. It is **not** an agent ban count.

**Conclusion (UNKNOWN, narrowed).** No defensible public estimate of how often platforms ban agents or agent operators was found within the documented search scope. The evidence supports three narrower statements:
1. Major AI providers ban accounts at large scale for all reasons, and roughly 1 in 10 appeals succeed at Anthropic [S094].
2. Agent-specific enforcement clusters around a few triggers: reusing subscription credentials in third-party tools, unidentified browsing agents, credential capture, and automated outreach on social networks [S016][S063][S075][S076].
3. Blocking of *crawlers* by websites is common for training (17%) and rare for search (<1%) [S092].

**What would resolve it:** platform transparency reports that break out automation-related enforcement, with active-account denominators, or an operator's own block logs (§10.4 `external_block`).

### 11.4 Regional differences at a glance

| Region | Regulatory posture toward agents | Commerce and payments evidence | Notes |
|---|---|---|---|
| **United States** | Voluntary standards (NIST CAISI) [S050]; joint security guidance [S051]; access disputes run through courts. Anti-hacking law (CFAA) was held a weak tool against user-directed agents in the Ninth Circuit [S015] | Most pilots and launches: ACP, UCP checkout, Visa/Mastercard pilots [S023][S025][S021][S022] | Largest share of developer AI usage by billing (47% on OpenRouter) [S043] |
| **European Union** | AI Act: prohibited practices and AI literacy from 2 Feb 2025; GPAI obligations from 2 Aug 2025; Art. 50 disclosure from 2 Aug 2026; high-risk Annex III deferred to 2 Dec 2027 [S107][S074]. DSA transparency reporting covers some AI services [S095]. Product liability extends to software for products placed on the market after 9 Dec 2026 [S111] | Little public agent-commerce evidence. UCP expansion plans name Canada, Australia and the UK, not the EU (secondary) [S023]. Stripe/Paddle/MoR infrastructure available [S104][S105] | **Official statistic:** 20.0% of enterprises (10+ staff) used any AI in 2025; range 5.2%–42.0% by country [S096]. Germany ~7.5% of OpenRouter tokens [S043]. GDPR applies to agent logs and transcripts |
| **United Kingdom** | Co-author of the Five Eyes guidance [S051]; 2026 payments consultation reopening consent and liability [S066] | Limited | — |
| **Singapore / ASEAN** | First dedicated agentic-AI governance framework (voluntary) [S052] | Mastercard live agentic transactions in Singapore and Malaysia [S022] | Singapore ~9% of OpenRouter tokens, likely regional billing hubs [S043] |
| **China** | Administrative restrictions on running OpenClaw in state bodies [S013] | Not examined (evidence gap) | Chinese open-weight models significant on OpenRouter [S043] |
| **Latin America, Korea, Australia, Hong Kong** | Not examined | Mastercard "first live agentic transactions" announced [S022] | Pilots, not volumes |

**Baltics (operator-relevant facts only).** Latvia 12.2%, Estonia 23.4% and Lithuania 21.3% of enterprises used AI in 2025 [S096]. Latvia is a supported country for the main model APIs [S106]. Latvian tax and legal operating conditions are in §15. Latvian customer demand is deliberately not analysed (scope decision).

**Transferability of the paper's main conclusions (INTERPRETATION).**

| Conclusion | Broadly applicable technically | Provider-specific | Jurisdiction-specific | Limited sample |
|---|---|---|---|---|
| Workflows vs agents; autonomy is a design choice (§1) | ✔ | | | |
| Security: prompt injection unsolved; lethal trifecta (§5) | ✔ (vendor tests from Anthropic and OpenAI, but mechanism is model-agnostic) | partly | | |
| Reliability: RLI 15.8%, METR trends (§4) | ✔ for digital/software work | | | ✔ (task sets: freelance, software) |
| Adoption levels (§2.2) | | | ✔ (Eurostat EU differs from global executive surveys) | ✔ (executive self-report) |
| Cost structure: humans dominate supervised deployments (§6) | ✔ (structure) | prices provider-specific | labour cost **jurisdiction-specific** (US BLS wages used; Latvian/EU wages lower, which *reduces* human costs and therefore the savings) | |
| Commerce is mostly discovery; autonomous buying tiny (§9) | | ✔ (OpenAI, Visa, Mastercard, Coinbase rails) | US-heavy evidence; the 16-country Accenture survey points the same way | ✔ |
| No stable agent buying preference (§9.5) | ✔ | models tested | | ✔ (mock markets) |
| Platform enforcement patterns (§11.3) | | ✔ (Amazon, Anthropic, Google, LinkedIn) | US litigation (CFAA) is US-specific; ToS enforcement is global | ✔ (incidents) |
| Activity timing (§10) | | ✔ (Anthropic, Cloudflare) | | ✔ (public GitHub coding agents) |
| Regulation (§11.2) | | | ✔ by definition | |


## 12. Market and business implications

### 12.1 How big is it? Weigh the evidence types

| Evidence type | Example | Strength | Caveat |
|---|---|---|---|
| Audited / filed company results | Salesforce Agentforce ARR >$1.5bn (+240% YoY), broadened definition [S055] | **Strong** for that company | Definition change inflates growth |
| Company disclosures | Anthropic run-rate $14bn (Feb 2026) [S141] and >$47bn (May 2026) [S088]; Claude Code >$2.5bn (Feb 2026) [S141]. Cursor $1bn disclosed (Nov 2025) [S054] | Medium–strong | Run-rate ≠ revenue; most of it is model usage, not "agent products" alone |
| Press reports from anonymous sources | Anthropic ~$65bn run-rate by end-July 2026 (one person familiar, via Bloomberg/Reuters) [S089]; Cursor ~$4bn [S054] | Medium–weak | Not confirmed by the companies |
| Executive surveys | Gartner 17% deployed [S098]; McKinsey 22–40% of respondents report scaling [S084] | Medium | Self-report; definitions differ; samples not representative of all firms |
| Official statistics | Eurostat: 20.0% of EU enterprises used any AI in 2025 [S096] | **Strong** (for its definition) | AI in general, not agents |
| Analyst forecasts | Gartner "AI agents and assistants" spending $16.5bn (2025), **$29.2bn (2026)**, $65.5bn (2027), within total AI spending of $2.67trn in 2026 [S082]; Gartner "agentic AI software spend" $985bn by 2030 [S083]; "AI agents market" ~$48–53bn in 2030 (other firms) [S056]; 40% of enterprise apps to embed task-specific agents by end-2026 [S007] | **Weak** (definitions vary by ~30×; feature counts and spend categories, not usage) | Paywalled methods; Gartner's category definitions are in client documents; 2025 base estimates differ >2× (C013). The v1.0 figure "~$202bn agentic AI spending 2026" could not be found in any Gartner primary and was **removed** |
| Scenarios | McKinsey: up to $1trn ("$900 billion to $1 trillion") US B2C / $3–5trn global "orchestrated revenue" in goods by 2030 [S086] | Weak | "Orchestrated revenue" undefined; built from US Census data and undisclosed adoption rates; excludes services and B2B |
| On-chain / usage data | x402 $15.0M adjusted (to Apr 2026) [S091]; TRM: 0.6%–7.5% of $25.6M screened looks agentic [S090] | Medium–strong | Narrow slice; agent vs script indistinguishable |

**INTERPRETATION.**
- Spending is real and large, but it is concentrated in model providers, coding agents and enterprise suites.
- Converging analyst forecasts are not corroboration. The 2030 numbers agree while the starting points disagree, which suggests anchoring.
- Agentic *commerce* is mostly an influence channel today.

### 12.2 Where value is accruing (INTERPRETATION)

1. **Model providers** capture the largest share of spend, because every agent step is billable inference [S088].
2. **Owners of distribution and data** (CRM/ERP suites, marketplaces, payment networks) set terms of access and capture agent features as upsells [S055][S063][S022].
3. **Coding agents** are the first breakout application category [S062][S054].
4. **Infrastructure for trust**, meaning identity, evaluation, observability, security and insurance, is attracting investment because enterprises cannot deploy without it [S060][S073][S061].
5. **Services** fill the capability gap. Small and mid-sized organisations lack the skills to deploy agents safely, and most failures are organisational (§4.4, §5.3).

### 12.3 Selling to humans who run agents versus being selected by agents

| | Sell to agent operators (humans/organizations) | Be selected by agents (agent as chooser) |
|---|---|---|
| Who decides | A person with a budget | A model within its owner's instructions |
| How you are found | Sales, content, partners, marketplaces | Structured data, MCP/registry listings, protocol feeds, price and position in agent results |
| Evidence that it works | Established B2B motions; vendor revenues [S055][S088] | Agents' choices are biased and unstable across models [S029][S030]; volume of agent-made purchases unknown |
| Advantages | Relationships, contracts, higher price points, lower churn | Potentially low acquisition cost; 24/7 demand; machine-readable comparison may favour good value |
| Disadvantages | Slower sales cycles; must prove ROI | Platform and model dependence; "optimising for the model" is a moving target; commoditisation on price; manipulation and regulatory risk |
| Payment | Contracts, cards, invoices | Scoped tokens, mandates, MPP/x402 micro-payments [S024][S090] |

**RECOMMENDATION.** For the next 12–24 months, build businesses that **sell to the humans responsible for agents**. Treat being selected by agents as a secondary channel. Make your offer machine-readable (structured data, an MCP server, honest labels) because it is cheap to do, but don't depend on it.

### 12.4 Opportunity summary (rebuilt in v1.2)

The register (`opportunities/opportunity-register.md` and `.csv`) holds 13 opportunities. Each has a customer, buyer, evidence, pricing hypothesis, competitors, invalidation criteria and a validation experiment.

**How v1.2 differs from v1.1.**
- **New entry gate.** v1.1 ranked opportunities on a weighted 1–5 rubric: evidence 20%, pain 15%, willingness to pay 15%, and 10% each for access, feasibility, cost, competition and risk. That rubric hides what matters most for a newcomer: the credentials and customer access needed, liability, and time to first revenue. v1.2 therefore adds an **entry gate** and decides on that, treating the numeric score as an ordinal summary. Differences under about 5 points are noise.
- **New evidence changed three scores:**
  - security reviews (O03): willingness to pay up on observed audit prices [S130]; access, feasibility and risk down, because credible buyers want specialists and liability is real;
  - coding-agent enablement (O07): willingness to pay up on observed training prices [S128][S129];
  - support-agent evaluation (O02): access and competition down, because of cheap QA substitutes [S134] and data-access friction.
- **New simpler adjacent service (O13):** small AI workflow automations, with the strongest observed paid demand [S127].

| Route | Register ID | Score v1.2 (v1.1) | Entry gate (INTERPRETATION) | Strongest evidence | Main reason it could fail |
|---|---|---|---|---|---|
| **R2** Coding-agent enablement + measured pilot | O07 | 73 (70) | **Shortlist; recommended first if the owner codes (best first year with warm access to engineering leads)** | Widest real adoption [S062][S088]; paid training at €890 per person for 2 days [S128]; productivity uncertain [S070] | Vendors and partners teach it free or cheaply |
| **R4** Small AI workflow automations (simpler adjacent) | O13 | 68 (new) | **Shortlist; first if the owner does not code** | Upwork AI-related work +22% YoY [S127] | Price competition; marketplace control |
| **R1** Limited agent risk review | O03 | 68 (71) | **Shortlist only with security credentials** | Security is the top adoption barrier (80% of large US firms [S131]); audit prices $6k–50k [S130] | Buyers want credentialed firms; liability |
| **R3** Support-agent evaluation and outcome audit | O02 | 63 (67) | **Defer** | Per-outcome pricing [S071]; 91% of service leaders under AI pressure [S133] | No observed paid demand; data access; QA substitutes [S134] |
| Products bought autonomously by agents | O09 | 43 | **Reject for now** | Agentic x402 commerce about $5–11k a month [S090] | Market too small to measure |
| Spend controls for agent purchases | O08 | 30 | **Reject** | — | Regulated payment service [S114] |

**Security: what a newcomer can and cannot sell.**
- A *limited risk review* is a structured configuration and architecture review against public checklists, with stated exclusions.
- A *security audit or penetration test* involves authorised technical testing by specialists, typically $16k–50k [S130].
- A *certification* can only be issued by accredited bodies.

Marketing a limited review as either of the latter is misleading and creates liability.

**Economics (CALCULATION, `models/route_economics.py`; base revised downward after the independent commercial review).**
- **Newcomer** without track record or warm contacts: the first year yields about €3–11 per owner-hour after Latvian taxes (once steady, €15–27).
- **With a network** or strong public proof: €23–36 per hour in the first year.
- **Benchmark:** a Latvian professional's mean pay is €13.04 gross [S126], about €8.7 net (CALCULATION with [S100]).
- **Adverse case:** the first year is a loss on every route.
- **Risk:** setup cash is small (€150–900). The real risk is about 215–285 unpaid hours before the first sale on R1–R3.
- **INTERPRETATION:** the owner's access to buyers matters more than the choice of route.

**Operating from Latvia (corrected in v1.2).**
- B2B services remain the simplest model, but **client mix decides the admin load**:
  - non-EU clients, or Latvian clients under €50,000, allow the micro-enterprise tax plus the special registration for foreign tool purchases [S122][S124];
  - the first EU VAT-registered client forces full VAT registration [S122].
- v1.1 said B2B services were simplest "with reverse charge for EU clients" without noting that this requires full registration. That has been corrected.

**Important caveats.**
- These are hypotheses. No customer was contacted, so no willingness to pay has been observed.
- The decision package (`package/`) sets out conditional recommendations, route dossiers, economics and prepared validation plans.
- Every validation step that contacts people, opens accounts or spends money needs the owner's approval.

### 12.5 Common claims, checked

| Claim you will hear | What the evidence says |
|---|---|
| "Agents will do most knowledge work soon" | On real freelance projects the best agent matched professionals 15.8% of the time (Jul 2026), up fast from 2.5% [S037]. The trend is steep, but most work still needs humans today |
| "Agents make developers 10× faster" | Controlled studies are inconclusive. Developers overestimate their own speed-up [S070] |
| "Agentic commerce is a $5 trillion market" | That is a 2030 *scenario* of "orchestrated revenue" from undisclosed adoption assumptions [S086]. Measured agent-made payments are tiny: the plausibly agentic share of x402 commerce is about $5k–11k a month [S090] |
| "AI agents are a $30bn or a $1trn market" | Both are Gartner figures for different definitions: $29.2bn of 2026 spending on agents and assistants [S082] vs $985bn agentic software spend by 2030 [S083]. Always ask which definition is meant |
| "Optimise your products for what AI agents prefer" | Agent choices show biases that change with model versions. There is no stable preference [S030] |
| "Agents are safe if you tell them the rules" | Prompts are not controls. Agents get persuaded and injected [S039][S068]. Put limits in code |
| "It's fine to plug my subscription into any agent tool" | Not under major providers' terms; suspensions have been reported [S016][S075] |
| "Model price is the main cost" | Only for heavy, unsupervised use. In supervised business deployments, human review and escalation dominate (§6) |
