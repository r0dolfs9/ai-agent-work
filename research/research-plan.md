# Research plan and research questions

Research order, from the assignment §7: definitions → architecture → costs → commerce & behaviour → standards → audits & enforcement → commercial implications. The paper is drafted as evidence accumulates.

Freshness rule: today is 2026-10-12. Product, pricing, protocol and policy facts must come from sources retrieved this session. Training-era knowledge is used only to generate leads. Wherever a claim relies on a source older than 6 months, the paper says so.

## Research questions (RQ)

| ID | Area | Research question | Preferred evidence |
|---|---|---|---|
| RQ1 | Definitions | How do leading builders and standards bodies distinguish an "agent" from a chatbot, a workflow, an automation and conventional software? | Vendor engineering guides; academic taxonomies; NIST/OECD/EU definitions |
| RQ2 | Definitions | What autonomy-level frameworks exist, and what is the human role at each level? | Academic papers (e.g. levels-of-autonomy); SAE-style analogies |
| RQ3 | Landscape | What are the main categories (coding, enterprise, personal, commerce, browser/computer-use, autonomous services), and who are the major providers, frameworks and platforms? | Official product docs; AI Agent Index |
| RQ4 | Landscape | What is in real operational use, as opposed to demos, roadmaps or marketing? | Surveys with methodology (McKinsey, Gartner, Stack Overflow, Anthropic Economic Index); benchmarks; incident data |
| RQ5 | Architecture | What are the components (model, loop, tools, memory, state, orchestration, multi-agent), and what reference architectures exist? | Vendor docs; framework docs; papers |
| RQ6 | Architecture | How do agents get identity, authentication, permissions, secrets, sandboxing and human approval? | OAuth/MCP auth spec; vendor security docs; IETF drafts |
| RQ7 | Failure modes | What failure modes are documented (hallucination, prompt injection, tool compromise, runaway loops, unauthorized actions), with attributable incidents? | OWASP; NIST; CVEs; incident reports; security research |
| RQ8 | Reliability | How reliable are agents on realistic tasks, and how is that changing? | Benchmarks (SWE-bench, OSWorld, τ-bench, TheAgentCompany); METR time-horizon |
| RQ9 | Costs | What does it cost to run agents (tokens, caching, tools, hosting, observability, human review)? What are the cost per success and the sensitivities? | Dated official pricing pages; own calculations |
| RQ10 | Access | Which services do agents use and through what interfaces? Where do "reachable", "supported", "permitted" and "observed" diverge? | API docs; ToS; Cloudflare/robots data; litigation |
| RQ11 | Standards | What is the status of MCP, A2A, AGENTS.md, ACP, AP2, UCP, x402, Web Bot Auth, Visa TAP, Mastercard Agent Pay and similar (proposed / experimental / implemented / broadly adopted)? | Spec sites; governance announcements; adoption evidence |
| RQ12 | Commerce | Who is the economic buyer? What have agents demonstrably bought, how is payment done, and where is approval required? | Payment network docs; protocol specs; retailer data; Adobe/Salesforce traffic data |
| RQ13 | Commerce behaviour | Is there evidence for agent vendor-selection, negotiation, refusal, or a stable "buying preference"? | Academic experiments (e.g. agent shopping studies); A/B studies |
| RQ14 | Activity/timing | What evidence exists about agent activity by time, geography, use case and deployment type? | Anthropic Economic Index; OpenAI usage paper; OpenRouter; Cloudflare Radar |
| RQ15 | Governance | How are agents evaluated, audited and monitored, by whom, and against which frameworks (EU AI Act, NIST AI RMF, ISO 42001, Singapore framework)? | Regulation text; framework docs |
| RQ16 | Enforcement | What platform rules restrict or ban agents? What enforcement and incidents are on record, and what appeal routes exist? | ToS; court filings; platform announcements |
| RQ17 | Market | What market-size and adoption claims exist, by what method, and with what uncertainty? | Analyst press releases; surveys; company disclosures |
| RQ18 | Business | Where is evidence of unmet pain plus willingness to pay? What are the trade-offs of selling to operators vs being selected by agents? | Revenue disclosures; funding; pricing pages; surveys |

## Milestones

1. M1 — Workspace, plan, coverage matrix skeleton *(this commit)*
2. M2 — Definitions, landscape, adoption and reliability evidence
3. M3 — Architecture, security, failure modes
4. M4 — Standards, commerce, payments, access, enforcement
5. M5 — Costs (pricing capture plus model)
6. M6 — Market, opportunities, governance and regulation
7. M7 — Paper drafting, then adversarial review, revision and handoff
