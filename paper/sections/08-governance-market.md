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
| **EU** | AI Act high-risk rules (Annex III, e.g., hiring, credit) | Risk management, documentation, human oversight | **Deferred to 2 Dec 2027** by the Digital Omnibus; product-embedded systems to 2 Aug 2028 | [S049] |
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

### 11.4 Regional differences at a glance

| Region | Regulatory posture toward agents | Commerce and payments evidence | Notes |
|---|---|---|---|
| **United States** | Voluntary standards (NIST CAISI) [S050]; joint security guidance [S051]; access disputes run through courts. Anti-hacking law (CFAA) was held a weak tool against user-directed agents in the Ninth Circuit [S015] | Most pilots and launches: ACP, UCP checkout, Visa/Mastercard pilots [S023][S025][S021][S022] | Largest share of developer AI usage by billing (47% on OpenRouter) [S043] |
| **European Union** | AI Act Art. 50 disclosure in force since 2 Aug 2026; high-risk rules deferred to Dec 2027 [S074][S049] | Little public agent-commerce evidence. UCP expansion plans name Canada, Australia and the UK, not the EU (secondary) [S023] | Germany ~7.5% of OpenRouter tokens [S043]; GDPR applies to agent logs and transcripts |
| **United Kingdom** | Co-author of the Five Eyes guidance [S051]; 2026 payments consultation reopening consent and liability [S066] | Limited | — |
| **Singapore / ASEAN** | First dedicated agentic-AI governance framework (voluntary) [S052] | Mastercard live agentic transactions in Singapore and Malaysia [S022] | Singapore ~9% of OpenRouter tokens, likely regional billing hubs [S043] |
| **China** | Administrative restrictions on running OpenClaw in state bodies [S013] | Not examined (evidence gap) | Chinese open-weight models significant on OpenRouter [S043] |
| **Latin America, Korea, Australia, Hong Kong** | Not examined | Mastercard "first live agentic transactions" announced [S022] | Pilots, not volumes |

**UNKNOWN:** Baltic or Latvia-specific adoption, pricing or enforcement data. None was found in public sources.

## 12. Market and business implications

### 12.1 How big is it? Weigh the evidence types

| Evidence type | Example | Strength | Caveat |
|---|---|---|---|
| Audited / filed company results | Salesforce Agentforce ARR >$1.5bn (+240% YoY), broadened definition [S055] | **Strong** for that company | Definition change inflates growth |
| Company statements via press | Anthropic run-rate ~$65bn (Jul 2026), Claude Code >$2.5bn (Feb 2026) [S053]; Cursor $1bn disclosed, ~$4bn press-reported [S054] | Medium | Run-rate ≠ revenue; most of it is model usage, not "agent products" alone |
| Executive surveys | Gartner 17% deployed [S005]; McKinsey 22–40% scaling [S004] | Medium | Self-report; definitions differ |
| Analyst forecasts | "AI agents market" ~$48–53bn in 2030 [S056]; Gartner agentic AI spending ~$202bn in 2026 [S058]; 40% of enterprise apps to embed task-specific agents by end-2026, up from <5% in 2025 [S007] | **Weak** (feature counts and spend definitions, not usage) | Paywalled methods; 2025 base estimates differ >2× (conflict C013) |
| Scenarios | McKinsey: up to $1trn US / $3–5trn global agent-orchestrated goods commerce by 2030 [S057] | Weak–medium | Includes AI-influenced purchases; "up to" |
| On-chain / usage data | x402 ~$19M adjusted volume [S028] | Medium | Narrow slice |

**INTERPRETATION.**
- Spending is real and large, but it is concentrated in model providers, coding agents and enterprise suites.
- Converging analyst forecasts are not corroboration. The 2030 numbers agree while the starting points disagree, which suggests anchoring.
- Agentic *commerce* is mostly an influence channel today.

### 12.2 Where value is accruing (INTERPRETATION)

1. **Model providers** capture the largest share of spend, because every agent step is billable inference [S053].
2. **Owners of distribution and data** (CRM/ERP suites, marketplaces, payment networks) set terms of access and capture agent features as upsells [S055][S063][S022].
3. **Coding agents** are the first breakout application category [S062][S054].
4. **Infrastructure for trust**, meaning identity, evaluation, observability, security and insurance, is attracting investment because enterprises cannot deploy without it [S060][S073][S061].
5. **Services** fill the capability gap. Small and mid-sized organisations lack the skills to deploy agents safely, and most failures are organisational (§4.4, §5.3).

### 12.3 Selling to humans who run agents versus being selected by agents

| | Sell to agent operators (humans/organizations) | Be selected by agents (agent as chooser) |
|---|---|---|
| Who decides | A person with a budget | A model within its owner's instructions |
| How you are found | Sales, content, partners, marketplaces | Structured data, MCP/registry listings, protocol feeds, price and position in agent results |
| Evidence that it works | Established B2B motions; vendor revenues [S055][S053] | Agents' choices are biased and unstable across models [S029][S030]; volume of agent-made purchases unknown |
| Advantages | Relationships, contracts, higher price points, lower churn | Potentially low acquisition cost; 24/7 demand; machine-readable comparison may favour good value |
| Disadvantages | Slower sales cycles; must prove ROI | Platform and model dependence; "optimising for the model" is a moving target; commoditisation on price; manipulation and regulatory risk |
| Payment | Contracts, cards, invoices | Scoped tokens, mandates, MPP/x402 micro-payments [S024][S028] |

**RECOMMENDATION.** For the next 12–24 months, build businesses that **sell to the humans responsible for agents**. Treat being selected by agents as a secondary channel. Make your offer machine-readable (structured data, an MCP server, honest labels) because it is cheap to do, but don't depend on it.

### 12.4 Opportunity summary

The full register (`opportunities/opportunity-register.md` and `.csv`) has 12 opportunities, each with customer, buyer, evidence, pricing hypothesis, competitors, invalidation criteria and a validation experiment, all scored on the same weighted rubric. The top five:

| Rank | Opportunity | Score /100 | Why it ranks high | Main risk |
|---|---|---|---|---|
| 1 | Agent security hardening and "lethal trifecta" review for SMEs | 71 | Well-documented incidents and government guidance [S014][S051]; low capital | Competition from security firms; advice liability |
| 2 | Coding-agent enablement **with measurement** for small dev teams | 70 | Widest real adoption [S062]; productivity unclear [S070] | Vendors provide free enablement |
| 3 | Independent evaluation and outcome-audit of support agents | 69 | Per-outcome billing [S071]; automated judges over-rate [S037]; resolution rate dominates cost (§6) | Data-sharing friction |
| 4 | Agent-readiness service for non-Shopify merchants | 66 | Fast-growing AI referrals [S031]; protocols live [S023] | Platform churn [S025]; small current revenue share |
| 5 | MCP connector build and migration for vertical SaaS | 64 | MCP broadly adopted; breaking 2026 spec [S032][S034] | Commoditised by code generation |

Lowest-ranked: spend-control fintech for agent purchases (36) and dispute-evidence tooling (44). Both depend on agent purchasing volumes that are not yet evidenced [S028] and on regulated infrastructure.

**Important caveats.**
- These are hypotheses. No customer was contacted, so no willingness to pay has been observed.
- The rubric favours low-capital services because the project assumed a zero budget.
- Score differences under ~5 points are not meaningful.
- The register separates revenue, cost reduction and learning value, and lists the cheapest validation experiment for each. Every such experiment needs the owner's approval before anyone is contacted or money is spent.

### 12.5 Common claims, checked

| Claim you will hear | What the evidence says |
|---|---|
| "Agents will do most knowledge work soon" | On real freelance projects the best agent matched professionals 15.8% of the time (Jul 2026), up fast from 2.5% [S037]. The trend is steep, but most work still needs humans today |
| "Agents make developers 10× faster" | Controlled studies are inconclusive. Developers overestimate their own speed-up [S070] |
| "Agentic commerce is a $5 trillion market" | That is a 2030 *scenario* that counts AI-influenced purchases [S057]. Measured agent-made payments are tiny [S028] |
| "Optimise your products for what AI agents prefer" | Agent choices show biases that change with model versions. There is no stable preference [S030] |
| "Agents are safe if you tell them the rules" | Prompts are not controls. Agents get persuaded and injected [S039][S068]. Put limits in code |
| "It's fine to plug my subscription into any agent tool" | Not under major providers' terms; suspensions have been reported [S016][S075] |
| "Model price is the main cost" | Only for heavy, unsupervised use. In supervised business deployments, human review and escalation dominate (§6) |
