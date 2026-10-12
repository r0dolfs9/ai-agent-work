# Appendices

## Appendix A — Technical deep dive

### A.1 Why agent cost grows faster than the number of steps

Let a task run *n* model calls. Call *k* (k = 0…n−1) sees a context of size C_k = B + k·Δ, where B is the starting context and Δ the tokens added per step (tool results plus the previous output). Without caching, input tokens per task are:

  Σ C_k = n·B + Δ·n(n−1)/2

so the cost grows roughly **quadratically** in *n* when Δ is large relative to B. With prefix caching at hit rate *h*, the reused prefix C_{k−1} is billed at the cache-read price r instead of the input/write price w. That replaces most of the quadratic term at a 10–40× lower rate [S044]. Output adds n·O·p_out regardless of caching. `models/cost_model.py::task_cost` implements exactly this.

**Practical implications.**
1. Long-running agents should **summarise or compact** context periodically.
2. Tool results should be **trimmed** before they are fed back to the model.
3. Stable content (system prompt, tool definitions) must come **first** so caching works.
4. MCP servers **SHOULD** return tools in a deterministic order "to enable client-side caching and improve LLM prompt cache hit rates" (MCP 2026-07-28, minor change 3 [S032]).

### A.2 MCP 2026-07-28 in one page (for builders)

From the official changelog [S032]:
- **Stateless core.** No `initialize` handshake. Every request carries the protocol version and client capabilities in `_meta`. The `Mcp-Session-Id` header and protocol-level sessions are gone. Servers needing cross-call state mint explicit handles passed as tool arguments.
- **`server/discover`.** Mandatory RPC advertising versions, capabilities and identity.
- **`subscriptions/listen`.** Replaces the GET endpoint and resource subscribe and unsubscribe.
- **Multi Round-Trip Requests.** A server needing user input or sampling returns `resultType: "input_required"` and the client retries with `inputResponses`. This replaces server-initiated requests.
- **Tasks moved to an official extension** (`io.modelcontextprotocol/tasks`) with polling.
- **Caching hints.** `ttlMs` and `cacheScope` are required on list and read results.
- **Auth hardening.** `iss` validation (RFC 9207). Credentials are bound to their issuer. Client ID Metadata Documents replace Dynamic Client Registration, which is now deprecated.
- **Deprecated:** Roots, Sampling, Logging, and the HTTP+SSE transport. There is a minimum 12-month deprecation window under the new lifecycle policy.

**RECOMMENDATION for builders:** new servers should target the stateless model directly. Existing servers should plan migration within the deprecation window. Treat each MCP server as privileged code (supply-chain risk, OWASP ASI04 [S010]).

### A.3 A2A essentials

A2A v1.0 defines Tasks (the "fundamental unit of work", stateful with a lifecycle), Messages, Artifacts (outputs) and Parts. It also defines **Agent Cards**, JSON documents describing identity, skills, endpoint and authentication, which v1.0 allows to be **signed** (§8.4 of the spec). Bindings exist for JSON-RPC, gRPC and HTTP+JSON/REST [S036]. **INTERPRETATION:** A2A matters when you must coordinate with agents *you don't control*, such as a supplier's agent. Inside one system, ordinary function calls or MCP are simpler.

### A.4 Minimal safe agent loop (pseudocode)

```
budget = Budget(max_steps=12, max_usd=0.50)
while not done:
    action = model.next_action(context)            # tool call or final answer
    if action.is_final: break
    policy.check(action)                           # allow-list, scopes, thresholds (code, not prompt)
    if action.irreversible or action.amount > LIMIT:
        require_human_approval(action)             # L4 "approver"
    result = sandbox.run(action, creds=scoped_short_lived_token(action))
    log.trace(action, result, cost)                # observability + audit
    context.append(trim(result))                   # keep context small
    budget.charge(cost); budget.enforce()          # hard stop on steps/spend
```

## Appendix B — Agent security checklist (mapped to OWASP ASI)

| # | Control | Mitigates | Done? |
|---|---|---|---|
| 1 | Inventory every agent, tool, MCP server, plugin or skill, and credential, including staff's personal agents | ASI04, ASI10 | ☐ |
| 2 | For each agent, remove at least one leg of the lethal trifecta [S011] | ASI01, ASI02 | ☐ |
| 3 | Separate read tools from write tools; require approval for write, delete, send, pay and publish | ASI02, ASI09 | ☐ |
| 4 | Per-agent identity; short-lived, task-scoped tokens; no shared human credentials [S050] | ASI03 | ☐ |
| 5 | Secrets injected outside the model context (vaults) [S080] | ASI03 | ☐ |
| 6 | Sandbox code execution and browsing; restrict network egress; never expose admin ports publicly [S014] | ASI05 | ☐ |
| 7 | Pin and review tools, skills and MCP servers; prefer registries that scan their contents; monitor for updates that change behaviour [S081] | ASI04 | ☐ |
| 8 | Treat retrieved content and memory as untrusted; validate and expire long-term memory | ASI06 | ☐ |
| 9 | Authenticate inter-agent messages (signed Agent Cards, mTLS) [S036] | ASI07 | ☐ |
| 10 | Circuit breakers: step, spend and rate caps; kill switch; idempotent tools | ASI08 | ☐ |
| 11 | Humans see what the agent is about to do in plain language before approving; no rubber-stamp UI | ASI09 | ☐ |
| 12 | Full traces retained; anomaly alerts on cost, tool use and data volume | ASI10 | ☐ |
| 13 | Prompt-injection red-team before launch and after each model or tool change [S068] | ASI01 | ☐ |
| 14 | Dev/prod separation and tested backups [S012] | ASI08 | ☐ |
| 15 | Incident runbook: revoke, rotate, notify, post-mortem | all | ☐ |

## Appendix C — EU-oriented governance starter checklist (not legal advice)

1. **Disclosure (AI Act Art. 50, from 2 Aug 2026).** Does any agent interact directly with people (chat, voice, email)? Is it obvious that it's AI? If not, disclose at first interaction [S074].
2. **Content marking.** Do you generate synthetic audio, image, video or text published to others? Check marking obligations; existing systems have until 2 Dec 2026 [S074].
3. **High-risk screen.** Is the agent used in hiring, credit, education, essential services or other Annex III areas? If so, plan for obligations applying from 2 Dec 2027 [S107].
4. **Accountability.** Name a responsible human per agent, and document its purpose, tools, permissions and limits (Singapore MGF dimension 2 [S052]).
5. **Risk bounding.** Write down what the agent may never do (amount limits, data classes, external parties) (MGF dimension 1 [S052]).
6. **Controls.** Apply Appendix B.
7. **Records.** Keep logs sufficient to reconstruct decisions; align retention with GDPR.
8. **End users.** Tell users how to reach a human and how to contest an agent's action (MGF dimension 4 [S052]).

## Appendix D — Methodology

- **Process.** Inspect → baseline → plan → research → reconcile → draft → verify → revise (see `research/research-plan.md`).
- **Search and retrieval.** Web search plus direct page retrieval, 12 October 2026. Where direct retrieval failed (HTTP 403/503), we used search-engine extracts quoting the primary and marked the access method in the register.
- **Source hierarchy.** Specifications, official docs, pricing pages, terms, court decisions, filings, then independent research, then reputable news, then vendor blogs and aggregators. Vendor claims are labelled as claims.
- **Registers.** Sources (`research/sources.csv`, 121 entries after v1.1, superseded entries kept and annotated); claims and conflicts (`research/claims-ledger.md`); limitations resolution (`research/limitations-resolution.md`); coverage (`research/coverage-matrix.md`); opportunities (`opportunities/`); cost models (`models/cost_model.py`, `models/operator_economics.py`); public-data analysis (`research/analysis/aidev_timing.py`).
- **v1.1 access paths.** Publisher-hosted alternative domains served the same public documents (gcom.pdo.aws.gartner.com for Gartner; karriere.mckinsey.de for McKinsey). Official APIs were used for Eurostat and ECB data. A public CC-BY dataset was downloaded column-by-column from Hugging Face. The tool used here could not reach web.archive.org, so no archived copies were used. No paywall, login or anti-bot protection was bypassed.
- **Verification.** See `verification/verification-report.md`, which covers the citation-resolution check, number reconciliation between prose and model outputs, and the adversarial self-review.
