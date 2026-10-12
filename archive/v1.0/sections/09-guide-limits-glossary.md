## 13. Practical starting guide

### 13.1 If you want to *use* agents (individual or small team)

1. **Pick one recurring, checkable task.** Examples: summarising the inbox into a to-do list, drafting replies, researching suppliers, writing code with tests.
2. **Start with an official product** (vendor app, scheduled tasks) or **your own API key**. Don't route a consumer subscription login through third-party agent software [S016][S075].
3. **Begin at autonomy level 3–4.** The agent proposes and you approve sending, paying and deleting [S002].
4. **Break the trifecta.** An agent that reads the open web shouldn't also hold your mailbox *and* be able to send [S011].
5. **Set a monthly spend cap** and check cost per *useful* result after two weeks (§6.4).
6. **Review the logs** of anything that acted on your behalf. Assume it can be fooled [S069].

### 13.2 If you want to *build* agents

1. **Write down the task, success criterion and cost of an error** before choosing an agent design. Prefer a workflow if the steps are known [S001].
2. **Build an evaluation set first.** Use 30–100 real cases with human-judged expected outcomes, and calibrate any LLM grader against humans [S037].
3. **Use MCP for tools and keep tools narrow:** read and write split, idempotent, scoped credentials. Track the 2026-07-28 spec changes [S032].
4. **Put limits in code:** step caps, spend caps, approval thresholds, allow-lists [S080].
5. **Make prompts cache-friendly** and measure cost per completed task (§6.3).
6. **Red-team before launch** against OWASP ASI01–ASI10 [S010]. Repeat after every model or tool change.
7. **Design the human escalation path.** It is usually your biggest cost and your safety net (§6.6).
8. **Disclose AI interaction** to people where required, for example in the EU since 2 Aug 2026 [S074].
9. **Keep provider portability:** maintain a second model tested, and keep your own logs and data.

### 13.3 If you want to build a *business* in this market

1. **Choose a buyer you can reach** (§12.3) and a pain you can evidence: security, measurement, evaluation, readiness.
2. **Run the register's validation experiment** before building anything, once the owner approves contact or spend. Pre-commit to the go/no-go threshold.
3. **Price on outcomes the buyer already measures,** such as hours saved, incidents avoided, or resolution verified. Avoid pricing on activity counts.
4. **Watch platform risk.** Avoid businesses that need terms-of-service grey zones such as credential capture or undeclared bots [S063][S016].
5. **Re-check this paper's dated facts quarterly.** Protocols, prices and policies moved materially within the six months before this paper.

## 14. Limitations

- **Freshness.** Evidence was retrieved on 12 October 2026. Several facts changed within weeks of each other: Amazon's agent block, Cloudflare's defaults, and the MCP spec.
- **Access limits.** Several primary sources blocked automated retrieval: Gartner, McKinsey, CNBC, OpenAI's site, White & Case. For those, we relied on search-engine extracts of the primary text or reputable secondary reporting, and marked confidence "medium". No paywalled analyst reports were read.
- **Vendor-sourced evidence.** Much evidence on adoption, transactions and security comes from vendors with an interest in the result (e.g., [S021][S022][S053][S068]). Vendor statements establish what vendors claim, not independent proof.
- **Survey limits.** Adoption surveys are self-reported and use incompatible definitions (C001).
- **Experimental limits.** Agent-behaviour findings come from simulations, mock marketplaces and small internal pilots [S029][S030][S039][S040]. Generalising to open markets is uncertain.
- **Cost model.** The scenarios rest on explicit assumptions, not observed deployments. The resolution rates, engineering effort and security budgets most need local validation (gaps G-COST-1 to -3). Incident costs, taxes and currency effects are excluded.
- **Geography.** Evidence is US-heavy. EU coverage is mainly regulatory. Asian evidence is limited to payments pilots, OpenRouter geography and Singapore's framework. No Baltic-specific market data was found.
- **No primary research.** No interviews, surveys or experiments with real customers were conducted, because they need approval. The opportunity register is therefore hypothesis-only.
- **Self-review.** The adversarial review (see `verification/verification-report.md`) was carried out by the same AI system that wrote the paper. No independent human review has taken place.

## Glossary

- **A2A (Agent2Agent):** open protocol for agents to discover and message other agents. Uses "Agent Cards" describing an agent's skills and endpoint [S036].
- **ACP (Agentic Commerce Protocol):** OpenAI/Stripe protocol for merchants to expose products and checkout to AI assistants [S026].
- **Agent:** an LLM-driven system that chooses its own actions and tools at run time (§1).
- **Agent washing:** marketing a non-agentic product as an agent [S006].
- **AGENTS.md:** a plain-text file in a code repository that tells coding agents how to work on it [S034].
- **AP2 (Agent Payments Protocol):** Google-led protocol using signed "mandates" to prove what a user authorised [S035].
- **ARR / run-rate:** annualised recurring revenue, or current revenue extrapolated to a year. Not the same as annual revenue.
- **Cache (prompt caching):** the provider stores a repeated prompt prefix and bills re-reads at a fraction of the price [S044].
- **Computer use / browser use:** the agent controls a screen or browser by "seeing" screenshots and clicking.
- **Context window:** the text the model can consider at once. Agent loops fill it as they go.
- **Escalation:** handing a case from the agent to a human.
- **Harness:** the software around the model that runs tools, enforces limits and records traces.
- **Human-in-the-loop:** a person approves or edits before an action takes effect.
- **Lethal trifecta:** private data + untrusted content + outbound communication in one agent [S011].
- **LLM:** large language model.
- **Mandate:** a signed statement of what an agent is authorised to buy [S035].
- **MCP (Model Context Protocol):** open standard for connecting agents to tools and data [S032].
- **MPP (Machine Payments Protocol):** Stripe/Tempo protocol letting agents pay for services programmatically [S024].
- **Prompt injection:** hidden instructions in content the agent reads that hijack its behaviour [S069].
- **Resolution rate:** the share of cases an agent completes without a human.
- **Sandbox:** isolated environment limiting what an agent's actions can affect.
- **Signed agent / Web Bot Auth:** an agent that cryptographically signs its web requests so sites can verify who it is [S059].
- **Time horizon (METR):** the length of tasks (in human time) that an agent completes 50% of the time [S008].
- **Token:** a chunk of text (~¾ of an English word) used for model billing.
- **TAP (Trusted Agent Protocol):** Visa's protocol for merchants to recognise legitimate shopping agents [S020].
- **UCP (Universal Commerce Protocol):** Google/Shopify-led open protocol for agentic shopping from catalog to post-purchase [S023].
- **x402:** protocol using the HTTP "402 Payment Required" status to let agents pay per request, typically in stablecoins [S028].
