## 3. How agents work

### 3.1 The loop, in plain language

Every agent, however it is marketed, runs some version of this loop:

```
goal + instructions + tool list  ──►  MODEL decides: answer, or call tool X with inputs Y
         ▲                                              │
         │                                              ▼
   result appended to the                      HARNESS runs the tool
   conversation ("context")  ◄──────────────  (search, API, browser, code, payment)
```

The **model** only produces text. That text includes structured "tool calls". The surrounding software, usually called the **harness** or runtime, actually executes them, enforces limits, and feeds results back. Everything that makes an agent safe or unsafe happens in that harness: what tools exist, what credentials they carry, what needs approval, and when to stop.

### 3.2 The components

| Component | What it is | Design questions |
|---|---|---|
| **Model** | The LLM choosing actions (frontier models for hard reasoning; small models for routing/grading) | Capability vs price (a 100× spread across one vendor's line-up [S044]); refusal and fallback behaviour |
| **Instructions** | System prompt, policies, examples; repository files such as `AGENTS.md` (adopted by >60,000 open-source projects [S034]) | Keep stable for caching; separate operator policy from untrusted content |
| **Tools** | Functions the model can call: APIs, databases, code execution, web search/fetch, browser or desktop control | Least privilege; read vs write tools; idempotency; per-tool approval |
| **Context & memory** | What the model sees each step: conversation, tool results, retrieved documents, long-term notes | Context grows each step and drives cost (§6); stale or poisoned memory is an attack vector (OWASP ASI06 [S010]) |
| **State** | Task progress outside the model: files, tickets, databases, checkpoints | Make state explicit and resumable; MCP's 2026 spec moved to *stateless* requests with explicit handles [S032] |
| **Orchestration** | The loop logic: step limits, retries, budgets, timeouts, hand-offs | Hard caps on steps and spend; per-run budgets exist on managed platforms [S080] |
| **Multi-agent** | Agents delegating to agents (coordinator/workers), possibly across organizations via A2A [S036] | Each hop adds cost and failure modes (OWASP ASI07, ASI08 [S010]) |
| **Interfaces** | How tools are exposed: native APIs, **MCP** servers, browser/computer use | APIs are cheaper and more reliable than screen control; computer-use tool definitions alone add ~4,500 input tokens per request [S044] |
| **Triggers** | Human, event, schedule, continuous (§1.3) | Who is accountable when no human started the run? |
| **Identity & secrets** | Credentials the agent uses: user's OAuth tokens, service accounts, API keys, payment tokens | Short-lived, scoped, per-agent identity (§3.4) |
| **Observability** | Traces of every step, tool call, cost; evaluations | Needed for debugging, audit and billing disputes (§11) |

### 3.3 Three reference architectures (worked examples)

**A. Personal research-and-email agent (single user).**
*Trigger:* human request, or a scheduled morning run. *Model:* mid-tier. *Tools:* web search, read-only mailbox and calendar, a "draft email" tool (not "send"). *Controls:* runs in a sandbox, uses the owner's own API key, has a monthly spend cap, and the human sends drafts. *Why:* this avoids the "lethal trifecta" [S011]. The agent reads untrusted web pages and private mail, but it cannot send anything out without a human.

**B. Small-business ticket triage and drafting (workflow plus agentic step).**
*Trigger:* new helpdesk ticket (webhook). *Steps:*
1. Classify the ticket. A small model is fine here.
2. Retrieve the customer's order through a read-only API.
3. The agent drafts a reply and proposes an action, such as a refund under a threshold.
4. A human approves.
5. A tool executes the approved action.

*Controls:* refund tool limited by amount, every action logged, weekly sample review. *Economics:* modelled in §6, Scenario 2.

**C. Production customer-service agent (50,000 conversations/month).**
*Components:*
- An agent loop with tools: order lookup, policy retrieval, ticket updates, and capped refunds.
- An escalation path to humans that carries the transcript.
- An evaluation pipeline: an automated LLM grader on a sample, plus human QA.
- Observability, plus incident runbooks.
- Per-conversation limits on steps and spend.
- AI-interaction disclosure to the customer, which is required in the EU since August 2026 [S074].

*Economics:* §6, Scenario 3. *Governance:* §11.

### 3.4 Identity, permissions, secrets, sandboxing and approval

- **Identity.** Today most agents act with the *user's* credentials (OAuth tokens, browser sessions) or a shared service account. Standards bodies are moving toward giving each agent its own identity. NIST's 2026 concept paper proposes applying OAuth 2.0, OpenID Connect and SPIFFE/SPIRE to agents as distinct non-human identities [S050]. Microsoft made "Entra Agent ID" generally available in 2026 [S060]. Card networks issue agent-specific payment tokens [S022].
- **Authorization.** MCP's 2026-07-28 revision tightened OAuth handling: issuer validation, credentials bound to the issuing server, and Client ID Metadata Documents replacing dynamic registration [S032]. **RECOMMENDATION:** give each agent short-lived, task-scoped credentials, never a human's master password or session cookie. Amazon cited an agent that "appears to capture and store customer credentials" as a reason to block it [S063].
- **Secrets.** Keep secrets out of the model's context. Managed platforms now inject secrets at the network boundary so they never enter the sandbox (Anthropic "vaults" [S080]).
- **Sandboxing.** Run code and browsing in isolated containers with restricted network egress. The most common real-world failures came from agents running on hosts with broad access [S013][S014].
- **Human approval.** Approval gates belong on irreversible or outbound actions: sending, paying, deleting, publishing. Experiments show a supervising "CEO" agent shares the same blind spots as the agent it supervises [S039]. Approvals should come from humans or deterministic rules, not only from another model.

### 3.5 Failure modes (summary; details in §5)

| Failure mode | What happens | Typical control |
|---|---|---|
| Hallucination / confabulation | Agent states or acts on false facts; even negotiation agents invented details [S040] | Grounding, citations, verification steps, human review |
| Prompt injection / goal hijack | Hidden instructions in a web page, email or document take over (OWASP ASI01) [S010] | Separate untrusted content; restrict outbound actions; confirmations |
| Compromised tools / supply chain | Malicious MCP servers or "skills" exfiltrate data [S014][S010] | Allow-lists, code review, pinned versions |
| Runaway loops / cost blow-ups | Agent repeats steps, context balloons | Step and budget caps [S080]; monitoring |
| Stale context | Acts on outdated memory or cache | Expiry, freshness checks |
| Unauthorized or destructive actions | Deletes data, violates instructions [S012] | Least privilege, dev/prod separation, backups, approvals |
| Over-compliance ("eagerness to please") | Talked into discounts or unlawful deals [S039] | Hard policy limits in code, not just in prompts |
