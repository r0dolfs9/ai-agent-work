## 7. Sites, services and access: what agents can reach and what they may do

### 7.1 Four different questions

For any service an agent might use, ask four separate questions. The answers often differ.

1. **Technically reachable**: can the agent get there at all (an API, or a browser driving the website)?
2. **Officially supported**: does the service provide an agent-facing interface such as an API, MCP server, protocol or checkout kit?
3. **Permitted by terms**: do the terms of service allow this use by this kind of client?
4. **Observed in use**: is there public evidence that agents actually do it?

| Service / context | Reachable | Officially supported for agents | Permitted by terms | Observed | Notes |
|---|---|---|---|---|---|
| **Amazon.com shopping** | Yes (browser agents) | No general agent interface found | Conditions of Use require agents to identify themselves and forbid concealing automation [S064]. Access by "unauthorized AI agent" is treated as a violation [S063] | Yes: Perplexity Comet [S015]; Meta Muse was blocked 2026-09-20 [S063] | A US appeals court found the *user* accessed Amazon in the Comet case (anti-hacking claims unlikely), but contract claims remain open [S015] |
| **Shopify storefronts** | Yes | Yes: Checkout Kit, agentic storefronts, UCP [S065][S023] | Default robots.txt says "Checkouts are for humans"; end-to-end payment without a final review step is not permitted [S065] | Discovery and checkout handoff via AI apps [S025] | robots.txt signals policy but is not itself legally binding [S065] |
| **Retailers in ChatGPT / Google** | Yes | Yes: ACP feeds and apps (OpenAI); UCP checkout with Google Pay (Google) [S025][S023] | Yes, for participating merchants | Discovery yes. In-chat checkout scaled back by OpenAI in Mar 2026 [S025] | See §9 |
| **AI model subscriptions (Claude, Gemini consumer plans)** | Yes (OAuth tokens can be reused) | Only in the vendor's own apps. Third parties must use API keys [S016] | Anthropic: no routing of Free/Pro/Max credentials through third-party products; enforcement "without prior notice" [S016]. Consumer terms also bar access "through automated or non-human means" except via API key or explicit permission [S018]. Google: users report 403 "ToS violation" suspensions [S075] | Yes; enforcement observed [S017][S075] | Big practical risk for personal-agent users |
| **LinkedIn** | Yes | Official APIs for approved partners only | User Agreement prohibits bots or unauthorized automation to message, connect, post, like or scrape [S076] | Widespread automation tools; restriction anecdotes [S076] | Restriction-rate statistics are unverified vendor claims |
| **Sites behind Cloudflare (new domains, from 15 Sep 2026)** | Often blocked by default on ad-supported pages | Signed agents / Web Bot Auth; pay-per-crawl options | Site owner's choice | Default: "Agent" and "Training" bots blocked on pages with ads [S019] | "Agent" means automated activity acting in real time for a person, such as chat fetchers and browser agents [S019] |
| **GitHub, Google Workspace, Microsoft 365, Salesforce** | Yes | Yes: official APIs, OAuth scopes; vendor agents and MCP connectors widely available (INTERPRETATION from vendor docs) | Generally yes within API terms and rate limits | Yes: coding agents' core workflow [S062] | API terms, scopes and rate limits apply |

**INTERPRETATION.** The open web is splitting into three zones:

- an **API/protocol zone**, where agents are welcome under contract (developer APIs, MCP servers, UCP/ACP merchants);
- a **human zone**, where agents are discouraged or blocked (consumer marketplaces, social networks);
- a **paid zone**, where agents may enter for a fee or with a verified identity (pay-per-crawl, signed agents).

Agents that pretend to be humans are increasingly being blocked: Amazon's complaint centred on an agent that did not identify itself [S015][S063].

### 7.2 APIs versus websites

- **APIs and MCP tools** are faster, cheaper (no screenshots, fewer tokens), more reliable, and come with explicit permissions and rate limits.
- **Browser and computer use** reaches long-tail sites without APIs. The costs are higher token use (~4,500–6,600 extra tokens of tool definitions per request [S044]), fragility, prompt-injection exposure [S068][S069], and terms-of-service conflicts [S063].
- **Authenticated vs public:** acting inside a logged-in account carries the user's authority. That is where both the value and the liability are. Platforms object most strongly when credentials are captured by a third party [S063].

### 7.3 Platform dependence and switching costs

Risks we observed, with evidence:
1. **Policy changes without notice.** Anthropic's credential policy reserves enforcement "without prior notice" [S016]. Google users lost access to prepaid credits after automated suspensions [S075].
2. **Product pivots.** OpenAI's Instant Checkout moved from launch (Sep 2025) to scaled-back (Mar 2026) within six months [S026][S025].
3. **Protocol churn.** MCP's 2026-07-28 revision removed sessions and the handshake and deprecated features. A 12-month deprecation window softens this [S032].
4. **Gatekeeper defaults.** One infrastructure provider's default setting (Cloudflare) changes which sites agents can reach [S019].

**RECOMMENDATION.**
- Use official interfaces.
- Keep a second model provider tested.
- Abstract tool access behind MCP or your own layer.
- Store your own logs and data outside any single vendor.
- Read the "automated access" clause of every service your agent touches.

## 8. Standards and protocols

### 8.1 Status table

Status categories (our classification): **Proposed** (draft or announcement), **Experimental** (pilots, beta), **Implemented** (live in at least one major product), **Broadly adopted** (multiple independent major implementations plus large ecosystems).

| Layer | Standard | Steward | Status (Oct 2026) | Evidence |
|---|---|---|---|---|
| Agent ↔ tools | **Model Context Protocol (MCP)** | Agentic AI Foundation (Linux Foundation) | **Broadly adopted.** Spec 2026-07-28 (stateless) | >10,000 published servers [S034]; Tier-1 SDKs ~0.5bn downloads/month [S033]; breaking changes [S032] |
| Agent instructions in repos | **AGENTS.md** | AAIF | **Broadly adopted** (convention) | >60,000 projects [S034] |
| Agent ↔ agent | **A2A** v1.0 | Linux Foundation | **Implemented** (adoption claimed, few named deployments) | >150 supporting orgs; in Azure AI Foundry, Bedrock AgentCore; signed Agent Cards [S035][S036] |
| Commerce: catalog & checkout | **Agentic Commerce Protocol (ACP)** | OpenAI & Stripe | **Implemented**, scope narrowed to discovery plus apps | Launched Sep 2025 [S026]; checkout scaled back Mar 2026 [S025] |
| Commerce: catalog to post-purchase | **Universal Commerce Protocol (UCP)** | Google & Shopify (+ retailers) | **Implemented** (US checkout live; expanding) | Launched 2026-01-11 [S023] |
| Payment authorization | **AP2** (Agent Payments Protocol; mandates as verifiable credentials) | Google (A2A extension) | **Experimental/Implemented** in pilots | 60+ supporting orgs [S035] |
| Agent payments (HTTP-native) | **MPP** (Machine Payments Protocol) | Stripe & Tempo | **Implemented** (since 2026-03-18) | Stripe launch [S024]; ~20,000 tx/day reported [S028] |
| Agent payments (HTTP 402, stablecoins) | **x402** | x402 Foundation (Coinbase, Cloudflare; Linux Foundation) | **Implemented**, small real volume | ~$19M adjusted volume [S028] |
| Agent identification to merchants | **Visa Trusted Agent Protocol (TAP)** | Visa (with Cloudflare) | **Implemented** in pilots | HTTP Message Signatures [S020]; "hundreds" of controlled transactions [S021] |
| Agent payment tokens | **Mastercard Agent Pay** (+ Verifiable Intent with Google) | Mastercard | **Implemented** (live transactions in several markets) | [S022] |
| Bot/agent authentication | **Web Bot Auth** (HTTP Message Signatures) | IETF WG (drafts) | **Proposed** standard; **implemented** by CDNs | No adopted WG drafts as of Aug 2026 [S059] |
| Agent identity & authorization | OAuth 2.0/OIDC profiles, SPIFFE; Client ID Metadata Documents in MCP | NIST NCCoE, IETF, vendors | **Proposed** (NIST); vendor products GA | [S050][S032][S060] |
| Evaluation & governance | OWASP Agentic Top 10; AIUC-1; Singapore MGF | OWASP; AIUC; IMDA | **Published** guidance; not certifying law | [S010][S061][S052] |

### 8.2 Compatibility and competition

- **Complementary layers.** MCP (tools) + A2A (other agents) + UCP/ACP (commerce) + AP2/TAP/Agent Pay/MPP/x402 (payment and trust) are designed to stack. Visa's acceptance product, for example, takes payments initiated via TAP, MPP, ACP and UCP [S021].
- **Competing within a layer.** Two checkout protocols exist (ACP vs UCP), as do two HTTP-native payment schemes (MPP vs x402) and several agent-identity approaches (TAP signatures, Web Bot Auth, network tokens, Entra Agent ID). **INTERPRETATION:** expect consolidation. Merchants and builders should integrate through intermediaries such as PSPs, Shopify and CDNs that abstract the choice, rather than hand-building every protocol.
- **Published standard vs vendor convention.** Only MCP and A2A sit under neutral foundations with formal change processes [S032][S035]. ACP, UCP, TAP and Agent Pay are vendor-led even where open-licensed. Web Bot Auth is still an individual draft at the IETF [S059].
- **Version skew.** SDKs and servers lag specifications. MCP's stateless redesign requires existing servers to be rewritten, which is softened by the 12-month deprecation window [S032]. **RECOMMENDATION:** check which spec version each SDK actually implements before you build on it.
