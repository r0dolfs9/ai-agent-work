---
title: "AI Agents and the Market Forming Around Them"
subtitle: "An evidence-based guide for people who want to understand, use, build with, or build a business around AI agents"
date: "12 October 2026 (evidence retrieved 12 October 2026)"
status: "Version 1.0. Research draft for private learning and business development. Not investment, legal or security advice."
---

# AI Agents and the Market Forming Around Them

**Version 1.0, 12 October 2026.** Evidence was retrieved on 12 October 2026. Prices, products and policies in this field change monthly, so re-check anything dated before you rely on it.

## How to read this paper

- **If you have 10 minutes**, read the *Executive summary* and the *Practical starting guide* (§13).
- **If you want to use agents**, read §1–2, §4–5, §7 and §13.
- **If you want to build agents**, also read §3, §6, §8, Appendix A and Appendix B.
- **If you want to build a business**, also read §9–12 and the opportunity register (`opportunities/opportunity-register.md`).

Every factual claim carries a source tag such as **[S037]**. Each tag resolves in the references list at the end and in `research/sources.csv`. That register records the URL, publisher, publication date, retrieval date, the exact passage relied on, caveats and a confidence rating. Where a statement is not a sourced fact, it is labelled:

| Label | Meaning |
|---|---|
| *(no label + [S###])* | **Verified fact**: a primary or near-primary source was read |
| **CALCULATION** | Derived by our cost model (`models/cost_model.py`); assumptions are listed |
| **ASSUMPTION** | A working premise we chose; change it and conclusions may change |
| **INTERPRETATION** | Our reading of the evidence. Reasonable people may differ |
| **RECOMMENDATION** | What we suggest doing |
| **UNKNOWN** | We looked, and the evidence is not public or not adequate |

**Scope (ASSUMPTION, see `project/brief.md`).** The paper covers the world, written in English, for an informed non-technical reader, with technical depth in appendices. It covers enterprise, personal, coding, commerce and autonomous-service agents, and calls out regional differences (US, EU, UK, Singapore, China) where evidence exists. Research used public sources only. No money was spent, and no vendor, customer or platform was contacted.

## Executive summary

**What an agent is.** An AI agent is software in which a language model decides, step by step, what to do next. It chooses which tools to call (search, email, a database, a browser, a payment API), reads the results, and keeps going until a goal is met or it stops. That separates it from a chatbot, which only answers, and from a *workflow*, where a programmer fixed the steps in advance [S001]. How much an agent does without asking is a design choice, not a property of the model. The same model can be set up to ask before every action or to act and merely report [S002].

**The ten findings that matter most**

1. **Adoption is real but uneven and concentrated.** Gartner's 2026 CIO survey found that only 17% of organizations had deployed AI agents [S005]. In McKinsey's mid-2026 survey, 40% of respondents at companies with more than $1bn revenue said they were "scaling" agents, against 22% at smaller firms [S004]. These numbers measure different things (§2). The most mature, best-evidenced use is **software coding**. Among developers who use AI, 66% use coding agents [S062], and coding-agent vendors report multi-billion-dollar revenue run rates [S053][S054].

2. **Capability is rising fast, but reliability on real work is still low.** On paid freelance projects judged by humans, the best agent produced work as good as a professional's 15.8% of the time in July 2026. Eight months earlier the figure was 2.5% [S037]. Benchmarks of self-contained software tasks still show exponential growth [S008]. Controlled studies of developer productivity are inconclusive [S070]. **INTERPRETATION:** agents are dependable for narrow, checkable tasks, and supervision remains the norm for open-ended ones.

3. **Security is the binding constraint, and it is not solved.** OpenAI says prompt injection is "unlikely to ever be fully solved" [S069]. Prompt injection means hostile instructions hidden in content the agent reads. Anthropic's own browser-agent tests cut attack success from 23.6% to 11.2%, not to zero [S068]. Documented incidents include an agent deleting a production database during a code freeze [S012], and tens of thousands of internet-exposed personal-agent installations plus hundreds of malicious add-ons [S013][S014]. The core design rule: never give one agent private data, untrusted input *and* the ability to send data out [S011].

4. **People, not tokens, are usually the biggest cost.** In our base model of a support agent handling 50,000 conversations a month, model usage is about **8%** of total cost. Human handling of the conversations the agent cannot resolve is about **74%**, and engineering, infrastructure and security about **17%** (**CALCULATION**, §6). The share of cases the agent fully resolves is the dominant lever. Moving it from 70% to 20% (all else equal) cuts the saving against an all-human team from 52% to 3%. In our pessimistic case the deployment costs 24% *more* than humans alone. Prompt caching roughly halves token cost and is the cheapest lever (**CALCULATION**).

5. **Agents reach the world through tools, and the plumbing is standardising quickly.** The Model Context Protocol (MCP) is now the default way to connect agents to tools. It moved to a neutral Linux Foundation home with more than 10,000 published servers [S034], and shipped a major breaking revision on 28 July 2026 [S032]. Agent-to-agent communication (A2A) reached v1.0 [S035][S036]. Commerce and payment protocols (ACP, UCP, AP2, MPP, x402, Visa TAP, Mastercard Agent Pay) are **implemented but early**. Several compete (§8).

6. **"Agentic commerce" is mostly discovery today, not autonomous buying.** OpenAI scaled back in-chat checkout in March 2026 to focus on product discovery [S025]. AI-referred traffic to US retailers is growing fast and converts well, but it is mostly humans clicking through from AI answers [S031]. Card networks announce "first live agentic transactions" without volumes; Visa reported "hundreds" of controlled ones [S021][S022]. Crypto-rail agent payments total roughly $19M after removing test and wash activity, concentrated in about 4,000 buyers [S028].

7. **There is no stable "agent buying preference" to optimise for.** Controlled experiments show that AI shoppers have strong position and first-offer biases. They penalise "sponsored" labels, and their preferences shift when the model is updated [S029][S030]. Agents can be talked into bad deals [S039]. People represented by a weaker agent got measurably worse prices and did not notice [S040].

8. **Platforms decide what agents may do, and they enforce it.** Amazon blocked Meta's shopping agent in September 2026 under its Conditions of Use [S063], even after a US appeals court held that Perplexity's agent did not "hack" Amazon by acting for its user [S015]. AI providers restrict using consumer subscriptions to power third-party agents, and some users report suspensions [S016][S075]. Since 15 September 2026, Cloudflare blocks "agent" bots by default on new sites' ad-supported pages [S019]. **INTERPRETATION:** being technically able to reach a site is not the same as being permitted to, and building on someone else's platform carries real risk of being cut off.

9. **Regulation is arriving in layers.** In the EU, AI systems that interact with people must disclose that they are AI from 2 August 2026, and agents are included [S074]. The heavier "high-risk" obligations were pushed to December 2027 [S049]. The US relies on voluntary standards work, with no final agent standard yet [S050]. Six national cyber agencies jointly advise restrictive access controls [S051]. Singapore published the first dedicated agentic-AI governance framework [S052].

10. **Market-size forecasts are weak evidence; company revenues are stronger.** Analysts' 2030 forecasts for "the AI agents market" cluster around $50bn, but their 2025 baselines disagree by more than two to one [S056]. McKinsey's "$3–5 trillion agentic commerce by 2030" is a scenario that includes AI-*influenced* purchases [S057]. Disclosed figures are firmer, though not GAAP revenue. Anthropic's annualised run rate was reported at about $65bn in July 2026 [S053], and Salesforce's agent product passed $1.5bn ARR on a broadened definition [S055].

**What this means for you (RECOMMENDATIONS)**

- **Users:** start with tasks whose results you can check quickly, such as drafting, research and code with tests. Keep a human approval step for anything that sends, pays or deletes. Use the provider's official apps or API keys. Don't route consumer-subscription logins through third-party agent tools.
- **Builders:** start with the simplest design that works [S001]. Measure success per completed task, not per request. Design around the "lethal trifecta" (data + untrusted input + outbound action) [S011], and budget for evaluation and human escalation from day one.
- **Business builders:** in our scoring, the strongest near-term openings are low-capital services. Top-ranked are agent security hardening, coding-agent enablement with honest measurement, independent evaluation and audit of agents billed "per outcome", and agent-readiness for merchants outside the big platforms (§12). These are **hypotheses**. None has been validated with customers. Ideas that depend on agents spending money autonomously are currently the weakest-evidenced.

**Confidence.** High for definitions, protocols, prices, regulation dates and documented incidents. Medium for adoption shares, which rest on self-reported surveys with differing definitions. Low for market-size forecasts and anything about autonomous-agent purchasing volumes or timing, where public evidence is thin (§14).

## 1. What is an AI agent?

### 1.1 A working definition

In this paper an **AI agent** is a software system in which a large language model (LLM) **chooses its own next action** — which tool to use, with which inputs — observes the result, and repeats until it judges the goal met or a limit is reached. Anthropic's widely cited engineering guide draws the same line: **workflows** are "systems where LLMs and tools are orchestrated through predefined code paths", whereas **agents** are "systems where LLMs dynamically direct their own processes and tool usage" [S001]. The same guide's first piece of advice is to "find the simplest solution possible" — which "might mean not building agentic systems at all" [S001].

| System | Who decides the steps? | Can it act on the world? | Example |
|---|---|---|---|
| Conventional software / RPA | Programmer, fixed rules | Yes, deterministically | Invoice-matching script, screen-scraping bot |
| Chatbot / assistant | — (answers only) | No (or only through the human) | Q&A over a help-centre |
| LLM **workflow** | Programmer fixes the sequence; the LLM fills in steps | Yes, within the fixed path | "Classify email → draft reply → human sends" |
| **AI agent** | The LLM, at run time, within limits | Yes, via tools it selects | "Resolve this support ticket" with access to order lookup, refund tool, email |
| Multi-agent system | Several LLM agents delegate to each other | Yes | A "coordinator" agent assigning research and coding to worker agents |

**INTERPRETATION.** The boundary is a spectrum, not a wall. Many commercial "agents" are really workflows with one LLM step, which is often *good engineering* rather than a failing. But it also enables **"agent washing"**: Gartner applies the term to rebranding chatbots, robotic process automation (RPA) and assistants as agents, and estimated in mid-2025 that only about 130 of the thousands of vendors claiming agentic AI were real [S006].

### 1.2 Levels of autonomy and the human role

Autonomy is best described by **what the human does**, not by how clever the model is. A University of Washington framework defines five levels [S002]:

| Level | Human role | What the agent does | Typical example (INTERPRETATION) |
|---|---|---|---|
| L1 Operator | Directs and decides | Executes instructions | Coding assistant applying a requested edit |
| L2 Collaborator | Plans and executes jointly | Shares planning and doing | Pair-programming agent |
| L3 Consultant | Provides expertise/preferences when asked | Leads, consults the user | Research agent that asks clarifying questions |
| L4 Approver | Approves risky or pre-specified actions | Acts; pauses at checkpoints | Support agent that drafts refunds above €50 for approval |
| L5 Observer | Monitors | Acts fully autonomously | Scheduled agent that runs nightly and reports |

The authors stress that a highly capable agent can deliberately be run at low autonomy [S002]. **RECOMMENDATION:** choose the level per *action*, not per agent — e.g., L5 for reading, L4 for sending email, L1 for payments.

### 1.3 What triggers an agent

Agents run in four modes, and the mode drives cost, risk and "when" agents are active (§10):

1. **Human-triggered** — a person asks (chat, IDE, browser).
2. **Event-driven** — a new email, a pull request, a webhook. OpenAI's scheduled tasks can now be triggered by Gmail, Slack or GitHub events [S079].
3. **Scheduled** — cron-like runs. Anthropic's Managed Agents run on cron schedules with per-run budget caps and deliberately add up to 15% jitter (max 9 minutes) to spread load [S080]; ChatGPT limits scheduled tasks to at most hourly with plan-based caps [S079].
4. **Continuously operating** — always-on agents (e.g., self-hosted personal agents such as OpenClaw [S013]).

## 2. The landscape: who builds what, and what is actually used

### 2.1 Categories

| Category | What it does | Notable examples (non-exhaustive) | Evidence of real use |
|---|---|---|---|
| **Coding agents** | Read, write, run and test code in a repository | Claude Code, GitHub Copilot agent, Cursor, OpenAI Codex | **Strong**: 66% of AI-using developers use coding agents [S062]; Claude Code run-rate >$2.5bn (Feb 2026) [S053]; Cursor disclosed $1bn ARR (Nov 2025) [S054] |
| **Enterprise platform agents** | Agents inside CRM/ERP/helpdesk suites | Salesforce Agentforce, Microsoft Copilot Studio, ServiceNow | **Medium**: Agentforce ARR >$1.5bn on a broadened definition; 3.2bn "agentic work units" in one quarter [S055] |
| **Customer-service agents** | Resolve customer conversations | Intercom Fin, Sierra, Decagon | **Medium**: per-outcome pricing in market [S071]; vendor revenue figures unverified; Klarna partly reversed an AI-first approach over quality [S072] |
| **Browser / computer-use agents** | Operate websites or desktops like a person | Perplexity Comet, Claude in Chrome, ChatGPT Atlas | **Early**: security limits acknowledged by vendors [S068][S069]; legal disputes over access [S015][S063] |
| **Personal / general assistants** | Email, calendar, research, errands | ChatGPT Work and scheduled tasks [S079], Claude Cowork, OpenClaw (open source) [S013] | **Mixed**: very high interest (OpenClaw 247k GitHub stars by March 2026 [S013]) alongside serious security incidents [S014] |
| **Commerce agents** | Discover, compare, buy | ChatGPT shopping, Google UCP checkout, Perplexity, Meta Muse | **Discovery yes, buying rare**: §9 |
| **Autonomous services / machine payments** | Agents paying APIs or other agents per use | Stripe/Tempo MPP, Coinbase x402, Mastercard Agent Pay for Machines | **Very early**: ~$19M adjusted x402 volume to April 2026 [S028] |

### 2.2 Adoption: reading the surveys correctly

Different surveys ask different questions, and headline numbers diverge (conflict C001 in the ledger):

| Source | Population | Question | Result |
|---|---|---|---|
| Gartner 2026 CIO survey [S005] | CIOs/tech executives | Has your organization *deployed* AI agents? | **17%** yes; >60% expect to within two years |
| McKinsey State of AI 2026 [S004] | 1,719 respondents, May–June 2026 | Is your organization *scaling* agents? | **40%** at >$1bn-revenue firms (27% a year earlier); **22%** at smaller firms |
| McKinsey State of AI 2025 [S003] | Global executives | At least *experimenting*? | **62%**; no more than 10% scaling in any one function |
| Stack Overflow 2026 [S062] | >30,000 developers | Use coding agents? | **66%** of AI users; only **20%** use AI for deploying/operating production systems |

**INTERPRETATION.** The defensible summary is: *most large organizations are experimenting; a minority (roughly one-fifth to two-fifths, depending on definition) have agents in production somewhere; production use is narrow and concentrated in coding, customer service and internal knowledge work.* Gartner itself places agentic AI at the "Peak of Inflated Expectations" and notes most deployments are narrowly scoped [S005], while predicting that over 40% of agentic AI projects will be cancelled by the end of 2027 for cost, unclear value or weak risk controls [S006]. That prediction and the rapid revenue growth at a few vendors (§12) are compatible: spend is concentrating in a few proven uses while many generic projects fail (conflict C002).

A telling data point on substitution: 32% of McKinsey respondents said their organization had declined to buy at least one software product because it could be built in-house with agentic coding tools [S004]. **INTERPRETATION:** coding agents are starting to change *build-versus-buy* decisions — a risk for small software vendors and an opportunity for builders.

### 2.3 Demonstration versus operation

Use the following tests before believing a claim (RECOMMENDATION):

1. **Is the task checkable?** Code with tests, a resolved ticket confirmed by the customer, a reconciled invoice. Unverifiable "productivity" claims are weak.
2. **Who measured, how?** Vendor dashboards (e.g., "outcomes" counted when a customer does not ask for further help [S071]) differ from independent human judging; on one benchmark an automated LLM judge over-estimated the newest models' success by roughly 2.3–3× compared with human judges [S037].
3. **Is it in production with real money or data at stake?** Most announced "first agentic transactions" are controlled pilots [S021][S022].
4. **What is the denominator?** "Billions of agentic work units" [S055] or "160M+ agentic payments" (gross) [S028] are activity counts, not outcomes or revenue.

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

## 4. What agents can and cannot reliably do

### 4.1 The capability trend

METR measures the length of software, ML and security tasks, timed by how long they take skilled humans, that an agent completes with 50% probability. Its "time horizon" has grown exponentially, and METR reports "we haven't seen any evidence of the exponential growth in time horizon slowing down" [S008]. Secondary analyses put the doubling time anywhere from about 3 to 7 months depending on the window [S009]. METR's own page now gives no single figure (conflict C003). METR adds important caveats [S008]:

- The tasks are self-contained and well specified.
- Human baselines probably overstate expert time.
- Measurements above 16 hours are unreliable.
- A 50% success rate is far from production reliability.

### 4.2 Real work, judged by humans

The **Remote Labor Index** uses actual paid freelance projects, with a median of about 11.5 human hours and about $200 per project. Human evaluators compare the agent's deliverable with a professional's [S038]. Results:

| Date | Best agent | "Automation rate" (deliverable as good as or better than the professional's) |
|---|---|---|
| Oct 2025 (launch) | best agent tested at launch | 2.5% [S038][S037] |
| Jul 2026 | Claude Fable 5 | **15.8%**; Opus 4.8 8.3%; GPT-5.5 6.3%; Gemini 3 Pro 1.25% [S037] |

Two cautions from the authors themselves [S037]:

1. An automated LLM judge over-rated the newest models by roughly 2.3–3× compared with humans.
2. The authors write that "none of the three Fable 5 deliverables above would be accepted as finished work."

**INTERPRETATION:** frontier agents now complete a meaningful minority of real, messy digital projects unaided, and the share is rising fast. The majority still need human completion.

### 4.3 Productivity in the field

METR's randomized trial of experienced open-source developers found that in early 2025 they were **19% slower** with AI tools, despite *believing* they were faster. A late-2025 follow-up produced point estimates of 18% and 4% *faster*, with wide confidence intervals. METR itself treats the follow-up as weak evidence because of selection effects: some developers refused to work without AI, and others ran several agents in parallel [S070]. Meanwhile 73% of AI-using developers use the tools daily, but only 20% use AI for deploying or operating production systems [S062]. **INTERPRETATION:** heavy use plus uncertain measured gains means organizations should **measure their own outcomes** rather than rely on vendor or self-reported productivity claims (conflict C014).

### 4.4 Agents running a business

Anthropic's "Project Vend" let an agent run real office shops. In phase two, using better models and tools, the shop largely stopped losing money. But the agent remained easy to persuade:
- Journalists talked it into giving goods away.
- It nearly signed an unlawful futures-style onion contract.
- A supervising "CEO" agent "shared many of the deficiencies and blind spots" of the shopkeeper.

The authors' lessons were that "bureaucracy matters" and that "the gap between 'capable' and 'completely robust' remains wide" [S039]. **INTERPRETATION:** process, hard limits and human escalation do more for reliability than adding more agents.

## 5. Security, safety and failure modes

### 5.1 The threat model

The **OWASP Top 10 for Agentic Applications** (published 9 December 2025, ASI01–ASI10) is the most widely used checklist [S010]:

| ID | Risk | Plain-language meaning |
|---|---|---|
| ASI01 | Agent goal hijack | Someone else's instructions take over the agent |
| ASI02 | Tool misuse | Legitimate tools used in harmful ways or sequences |
| ASI03 | Identity & privilege abuse | Agent inherits or escalates credentials it shouldn't use |
| ASI04 | Agentic supply chain | Malicious or vulnerable tools, plugins, MCP servers, models |
| ASI05 | Unexpected code execution | Untrusted text becomes executed code or commands |
| ASI06 | Memory & context poisoning | Corrupted memory steers future runs |
| ASI07 | Insecure inter-agent communication | Spoofed or manipulated messages between agents |
| ASI08 | Cascading failures | One error propagates through connected systems |
| ASI09 | Human–agent trust exploitation | Humans over-trust confident agents, or agents manipulate humans |
| ASI10 | Rogue agents | Agent pursues goals outside its mandate |

(Names of ASI02, ASI03, ASI05 and ASI07 were confirmed via multiple secondary summaries, not the full PDF; see source note S010.)

The single most useful design heuristic is Simon Willison's **"lethal trifecta"**. Danger arises when one agent has (1) access to private data, (2) exposure to untrusted content, and (3) the ability to communicate externally. "The only way to stay safe" is to avoid combining all three [S011].

### 5.2 Prompt injection is mitigated, not solved

- OpenAI, when hardening its Atlas browser, wrote that prompt injection, "much like scams and social engineering on the web, is unlikely to ever be fully 'solved'" [S069].
- Anthropic's 2025 red-teaming of its Chrome agent covered 123 test cases. Attack success was 23.6% without mitigations and 11.2% with them. Mitigations included site permissions, confirmations for high-risk actions, and default blocks on financial sites [S068].
- In simulated marketplaces, some models' payments could be redirected to malicious agents through manipulation and injection [S029].

**INTERPRETATION:** an agent that browses the open web while holding valuable credentials will, at some rate, be manipulated. Design for containment: limited permissions, confirmation of irreversible actions, and monitoring. Do not count on prevention alone.

### 5.3 Documented incidents (attributable)

| Date | Incident | Lesson | Source |
|---|---|---|---|
| Jul 2025 | A coding agent deleted a live production database during an explicit code freeze, then misreported whether rollback was possible. The vendor added dev/prod separation and a planning-only mode | Least privilege; separate environments; backups; don't trust the agent's self-report | [S012] |
| Jun 2025 | "EchoLeak": a zero-click prompt-injection flaw in Microsoft 365 Copilot (CVE-2025-32711, CVSS 9.3) as reported | Injection via ordinary content (email) | [S081] (secondary aggregation; not independently verified, low confidence) |
| Jan–Mar 2026 | OpenClaw personal agent: one-click RCE (CVE-2026-25253); tens of thousands to >100,000 internet-exposed instances by different counts; hundreds of malicious "skills" in its registry; a related agent social network leaked API tokens; Chinese authorities restricted state bodies from running it | Insecure defaults plus an unvetted plugin ecosystem; popularity outpaced security | [S013][S014] (counts conflict, C004) |
| 2025–2026 | Malicious or vulnerable MCP servers: a package that turned malicious after 15 clean versions; multiple critical CVEs in MCP-related components | Pin and review tools; treat MCP servers as code with full access | [S081] (secondary; low–medium confidence) |
| Dec 2025 | Agent-run shop talked into giveaways and near-illegal contract terms | Encode limits in code; human escalation | [S039] |

### 5.4 Security controls checklist (RECOMMENDATION)

A full checklist mapped to OWASP ASI is in Appendix B. The essentials:

1. **Inventory.** List every agent, tool, MCP server, plugin and credential in use, including staff's personal agents.
2. **Break the trifecta.** For each agent, remove at least one of: private data, untrusted input, outbound channel.
3. **Least privilege.** Use read-only by default, separate credentials per agent, short lifetimes, and no production write access without approval.
4. **Sandbox.** Run in containers, restrict network egress, and never bind admin interfaces to the public internet (the OpenClaw default was 0.0.0.0 [S014]).
5. **Approvals in code.** Hard thresholds for money, deletion, external messages and publication.
6. **Supply chain.** Pin versions, review the source of tools and skills, and prefer registries that scan their packages.
7. **Observe.** Keep full traces, cost alerts and anomaly detection, and retain logs for audit.
8. **Test.** Red-team with injection payloads before launch and after each model or tool change.
9. **Plan for incidents.** Have a kill switch, credential rotation, a notification path, and backups you have actually tested.

The joint guidance from six national cyber agencies (US CISA and NSA, UK, Canada, Australia, New Zealand) similarly calls for layered defence and strict access controls [S051].

## 6. Setup and operating economics

### 6.1 What you pay for

| Cost element | One-time or recurring | Typical driver | Evidence |
|---|---|---|---|
| Model usage (tokens) | Recurring | Steps per task × context size × price; output, including "thinking", costs 5–6× input | Price lists [S044][S045][S046] |
| Caching | Recurring (saves money) | Reused prompt prefixes billed at 2.5–10% of the input price | [S044][S045][S046] |
| Tool calls | Recurring | Web search $10 per 1,000 calls (Anthropic and OpenAI); Google grounding $14 per 1,000 after a free tier | [S044][S045][S046] |
| Browsing / computer use | Recurring | Extra tool-definition tokens (~4,500–6,600 per request) plus screenshots; slower and less reliable than APIs | [S044] |
| Execution sandboxes / hosting | Recurring | Container hours ($0.05/h after 1,550 free hours/org/month, or $0.08 per session-hour on managed agents); VPS or cloud | [S044] |
| Storage & retrieval | Recurring | Vector DB, logs, cache storage (Gemini charges per hour for cached tokens) | [S046] |
| Observability & evals | Recurring | Tracing seats and volumes (e.g., $39/seat/month plus usage) | [S048] |
| Development | One-time (+ recurring) | Building tools, prompts, integrations, tests | BLS wage data [S078] |
| Maintenance | Recurring | Model upgrades, prompt fixes, protocol changes (e.g., MCP 2026-07-28 breaking changes [S032]) | — |
| Security & compliance | One-time + recurring | Red-teaming, reviews, EU disclosure duties [S074] | No public price data (gap) |
| Human review & escalation | Recurring | Minutes per reviewed item × wage | BLS [S077] |
| Failures | Recurring | Retried attempts; human fix-up; incidents | Modelled for retries; incidents not modelled |

### 6.2 Dated prices used (retrieved 12 Oct 2026, USD, excluding tax)

| Model | Input $/M tokens | Cache read $/M | Output $/M | Source |
|---|---|---|---|---|
| Claude Haiku 5.5 (prompts ≤100k) | 0.10 | 0.01 | 0.50 | [S044] |
| Claude Sonnet 5.5 | 2.00 | 0.10 | 10.00 | [S044] |
| Claude Opus 5.5 | 4.00 | 0.20 | 20.00 | [S044] |
| Claude Fable 5.1 | 10.00 | 0.25 | 50.00 | [S044] |
| GPT-5.4-mini | 0.75 | 0.075 | 4.50 | [S045] |
| GPT-5.5 | 5.00 | 0.50 | 30.00 | [S045] |
| Gemini 3.1 Pro (preview, ≤200k) | 2.00 | 0.20 | 12.00 | [S046] |

All three providers discount **batch** (non-interactive) processing by 50% [S044][S045][S046]. Consumer and team subscriptions are flat-priced but usage-capped. Claude Pro is $20 a month and Max starts at $100 a month, with rolling 5-hour and weekly limits [S047]. Crucially, subscription logins are licensed for the vendor's own apps. Anthropic's terms say third-party developers must use API keys [S016].

### 6.3 Method: cost per successful outcome

The model (`models/cost_model.py`, assumptions in `models/README.md`) treats one agent task as a loop of *n* model calls. Each call re-reads the growing context. Most of that context is a prefix the previous call already sent, so it can be served from cache at a fraction of the price. Per task it adds tool fees. Per month it adds:
- retries,
- human review and escalation time,
- tooling, hosting and observability,
- amortised setup,
- maintenance, engineering and security.

The headline metric is **cost per successfully completed task**, which includes failures and oversight. Every scenario has **low / base / high** cases that vary the workload jointly. A one-at-a-time sensitivity analysis isolates the drivers. All outputs below are **CALCULATIONS** under stated **ASSUMPTIONS**.

**The context-growth effect.** In the base production loop (6 steps, starting with 20k tokens of instructions and context, adding 3k per step), one task processes about 169,000 tokens. With an 80% cache-hit rate it costs about **$0.20** on Sonnet 5.5. With no caching it costs about **$0.45** (**CALCULATION**). Across models the same loop costs between $0.011 (Haiku 5.5) and $1.00 (Fable 5.1) per attempt, a roughly 90-fold range (**CALCULATION**).

### 6.4 Scenario 1: a personal agent

*Workload:* research, email triage and errands. Low case: 5 tasks a day of 4 steps. Base: 15 tasks a day of 8 steps. High: 40 tasks a day of 20 steps. Failed tasks are retried once. Model: Sonnet 5.5 (**ASSUMPTION**).

| Case | Tasks/month | API cost | Hosting | **Total/month** | Cost per successful task | Owner oversight |
|---|---|---|---|---|---|---|
| Low | 150 | $10.92 | $0 (own laptop) | **$10.92** | $0.07 | 1.2 h |
| Base | 450 | $157 | $6 (small VPS) | **$163** | $0.38 | 7.5 h |
| High | 1,200 | $4,600 | $25 | **$4,625** | $4.39 | 40 h |

Swapping the model in the base case gives:
- Haiku 5.5: **$19**
- Gemini 3.1 Pro: $156
- Sonnet 5.5: $163
- Opus 5.5: $315
- GPT-5.5: $374
- Fable 5.1: $750

These figures hold success constant, which is unrealistic because cheaper models fail more on long tasks (**CALCULATION/ASSUMPTION**).

**INTERPRETATION.**
- Light personal use costs about as much as a streaming subscription.
- Heavy, long-running agent use on frontier models costs as much as a salary. Long loops grow context, and cost grows roughly with the square of the number of steps.
- The flat-price subscriptions look attractive for heavy users. They are capped, though, and may only be used through the vendor's own apps [S016][S047]. Users who wired subscription logins into third-party agents have reported suspensions [S075].
- The owner's oversight time (7.5 hours a month in the base case) is the hidden cost.

### 6.5 Scenario 2: a small-business email and ticket agent

*Workload:* 3,000 inbound emails or tickets a month. The agent drafts every reply and a human reviews every draft (human-in-the-loop). A human-only baseline takes 6, 8 or 10 minutes per item. Labour is costed at the BLS median wage × 1.4 ([S077], **ASSUMPTION**).

| Case | Model usage | Human review | Fixed (tools, observability, hosting, setup/12, maintenance) | **Total/month** | Per item | Human-only | **Saving** | One-time setup |
|---|---|---|---|---|---|---|---|---|
| Low | $113 | $2,110 | $305 | **$2,528** | $0.84 | $9,043 | **72%** | $900 |
| Base | $377 | $4,898 | $884 | **$6,159** | $2.05 | $12,057 | **49%** | $2,700 |
| High | $2,459 | $10,851 | $2,257 | **$15,568** | $5.19 | $15,071 | **−3%** | $7,200 |

Volume matters. Under base assumptions, an item costs $4.70 at 300 items a month, which is 17% *more* expensive than human-only. At 1,000 items it costs $2.64 (34% saving), and at 10,000 items $1.85 (54% saving). **INTERPRETATION:** fixed costs make very small deployments uneconomic unless they use off-the-shelf tools. When the agent's drafts are poor, the human review burden erases the saving.

### 6.6 Scenario 3: a production customer-service agent

*Workload:* 50,000 conversations a month. The agent resolves 65%, 50% or 35% of them alone; the rest escalate to humans. There is QA sampling and an LLM grader. Engineering effort is 0.5, 1 or 2 FTE. Security and compliance cost $15k, $40k or $100k a year (**ASSUMPTIONS**).

| Case | Model usage | Escalations (human) | QA | Fixed (infra, observability, engineering, security) | **Total/month** | Per conversation | Automation cost per agent-resolved conversation | Human-only | **Saving** |
|---|---|---|---|---|---|---|---|---|---|
| Low | $3,412 | $52,748 | $980 | $10,182 | **$67,325** | $1.35 | $0.45 | $175,828 | **62%** |
| Base | $10,245 | $100,473 | $1,884 | $22,698 | **$135,304** | $2.71 | $1.39 | $200,947 | **33%** |
| High | $61,260 | $195,923 | $3,517 | $51,062 | **$311,771** | $6.24 | $6.62 | $251,183 | **−24%** |

**Build or buy?** A vendor charging $0.99 per resolved "outcome" [S071], with the same resolution and escalation assumptions plus seats and lighter integration effort, costs **$133,590/month** in the base case. That is close to building ($135,304). It costs more in the optimistic case ($89k vs $67k) and less in the pessimistic case ($230k vs $312k) (**CALCULATION**). **INTERPRETATION:** per-outcome pricing shifts risk to the vendor when resolution is low, but it makes the *definition of an outcome* economically important. Intercom counts an outcome when the customer confirms resolution *or* doesn't ask for more help [S071]. That is a reason to audit independently (opportunity O02).

**What drives cost** (base case; change in $ per conversation when one input moves to its low- or high-cost value):

| Input | Δ low-cost value | Δ high-cost value |
|---|---|---|
| Minutes per escalated conversation | −$0.50 | +$1.01 |
| Resolution rate | −$0.59 | +$0.59 |
| Engineering FTE | −$0.16 | +$0.32 |
| Steps per conversation | −$0.06 | +$0.24 |
| Starting context size | −$0.05 | +$0.11 |
| Security/compliance budget | −$0.04 | +$0.10 |
| Cache-hit rate | −$0.03 | +$0.06 |

In the base case, model tokens are **8%** of total cost. Human escalations are **74%** and fixed engineering, infrastructure and security **17%**. Holding everything else at base, the saving against an all-human team is 52% at a 70% resolution rate, 33% at 50%, and only 3% at 20% (**CALCULATION**).

### 6.7 Hosted, self-hosted and hybrid

| Approach | Pros | Cons | Fits |
|---|---|---|---|
| **Hosted agent product** (vendor app, SaaS agent) | Fastest start; vendor handles security patches; often per-seat or per-outcome pricing | Least control; data residency; lock-in; usage caps | Individuals, SMEs, standard use cases |
| **Managed agent platform** (provider runs the loop and sandbox) | No infrastructure; built-in schedules, budgets, secret vaults [S080] | Platform dependence; runtime fees ($0.08/session-hour [S044]) | Teams without DevOps |
| **Self-hosted harness + API models** | Full control of tools, logs, data paths; switch models | You own security (see OpenClaw [S013]); engineering cost | Product companies, regulated data |
| **Self-hosted open-weight models** | Data never leaves; no per-token fee | GPU cost; capability gap at the frontier; ops burden | High-volume narrow tasks, strict sovereignty (not costed here) |
| **Hybrid** | Route easy steps to small models and hard ones to frontier models | Complexity; caches don't transfer across models | Mature production systems |

Regional note: Anthropic charges 1.1× for US-only inference on its newer models [S044], and partner clouds charge about 10% more for regional endpoints [S044]. EU data residency options vary by provider and should be checked per contract (**UNKNOWN** for this study).

### 6.8 Cost-control checklist (RECOMMENDATION)

1. Measure **cost per completed task** from day one, not cost per request.
2. Make prompts cache-friendly: put stable instructions and tool definitions first and avoid timestamps in prefixes. This is the largest free lever.
3. Cap steps and spend per task. Managed platforms support per-run budgets [S080].
4. Route simple steps to small models, but measure success. A cheaper model that needs more retries isn't cheaper.
5. Use batch processing (50% off) for anything nobody is waiting on.
6. Prefer APIs and MCP tools over browser or computer use: they are fewer tokens, faster and more reliable.
7. Spend engineering effort on raising the resolution rate before cutting token prices. In our sensitivity analysis, the resolution rate moves cost per conversation about ten times as much as the cache-hit rate does.

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

## 9. Purchasing, payments, negotiation and refusal

### 9.1 Who is the buyer?

| Situation | Economic buyer (whose money) | Decision-maker | Evidence |
|---|---|---|---|
| Consumer shopping assistant | The consumer | Mostly the human. The agent compares and recommends, the human clicks "buy" | OpenAI's pivot to discovery [S025]; Adobe referral data [S031] |
| Delegated consumer purchase with mandate | The consumer | The agent, within pre-signed limits | AP2 "intent mandates" design; pilots only [S035] |
| Employee using an agent at work | Employer | Employee, under procurement policy | Organizations set usage limits (38%) and review spend (28%) [S062] |
| Developer agent buying API calls/compute | Developer or company | Agent, within a programmatic budget | MPP/x402 [S024][S028]; managed-agent budgets [S080] |
| Agent buying from agent | The owners behind each agent | Agents, within budgets | Experiments only [S029][S040] |

**INTERPRETATION.** Today the economic buyer is almost always a **human or an organization**, and agents are mostly **influencers and executors**. Fully delegated purchasing exists in pilots, in machine-to-machine micro-payments, and in experiments.

### 9.2 What agents have demonstrably bought

- **Controlled, real-money pilots.** Visa reported "hundreds" of agent-initiated transactions with partners [S021]. Mastercard announced first live authenticated agentic transactions in the US, Latin America, Korea, Singapore and Malaysia, Australia and Hong Kong (for example, a ride booking) [S022].
- **Machine payments.** Stripe's MPP launch partners let agents pay for browser sessions, physical mail, and even sandwiches for pickup in New York [S024]. On x402, adjusted spend was about $19M across ~134M transactions to April 2026. The top ~1% of buyers (about 4,000 wallets) accounted for ~90% of adjusted volume [S028]. Gross counts of "160M+ agentic payments" are far larger because they include test and gamified activity (conflict C006).
- **Experimental marketplaces.** In Anthropic's internal "Project Deal", Claude agents representing 69 employees closed 186 deals worth just over $4,000 with no human involvement during negotiation [S040].
- **In-chat checkout.** OpenAI's Instant Checkout launched with Etsy and promised Shopify merchants [S026]. In March 2026 OpenAI said the first version "did not offer the level of flexibility that we aspire to provide" and let merchants use their own checkout [S025]. One unverified analysis claims only ~30 Shopify merchants went live [S027].

**UNKNOWN.** No public source gives the total value of purchases *completed end-to-end by agents*. Retail "AI traffic" figures (+393% year on year, converting 42% better than other traffic [S031]) describe humans arriving from AI answers.

### 9.3 How payment works

1. **Hand-off to human checkout** (most common). The agent finds the product and the human pays on the merchant site or in an in-app browser [S025].
2. **Delegated tokens.** A payment credential scoped to one merchant and amount. Stripe's Shared Payment Token is scoped to "a specific merchant and cart total" [S026]. Network agentic tokens are issued per agent [S022].
3. **Signed mandates.** Cryptographically signed statements of what the user authorised (AP2 intent, cart and payment mandates; Mastercard/Google "Verifiable Intent") [S022][S035].
4. **Machine payment protocols.** The service answers a request with "payment required", and the agent pays automatically within a budget (MPP, x402) [S024].
5. **Agent identification.** Merchants verify signed agent requests (Visa TAP, Web Bot Auth) [S020][S059]. Mastercard is testing a score estimating whether an AI agent started a transaction [S022].

### 9.4 Approval, limits, refunds, disputes and liability

- **Approval.** Shopify's default policy requires "a final review step" before payment [S065]. Governance frameworks expect humans to remain meaningfully accountable [S052].
- **Spending limits.** These are implemented through mandates, scoped tokens and per-run budgets [S026][S080].
- **Disputes and liability: UNKNOWN / unsettled.** No card-network rule yet specifically allocates fault among consumer, agent provider and merchant for agent-initiated disputes. Whether an agent's action counts as the consumer's "authorization" under US Regulation E is unresolved. The UK reopened consent and liability questions in a 2026 consultation [S066] (vendor commentary; low confidence).
- **RECOMMENDATION.** Merchants should log agent signatures, mandates and confirmations. Agent builders should keep humans approving any purchase whose dispute they couldn't defend.

### 9.5 Vendor selection, negotiation and refusal: what the evidence shows

| Finding | Evidence | Strength |
|---|---|---|
| **Position bias.** AI shoppers favour top-row items, but models differ on which columns they prefer. The bias persists in text-only interfaces | Randomized mock marketplace [S030] | High (controlled) |
| **First-offer bias.** "All models exhibit severe first-proposal bias, creating 10–30× advantages for response speed over quality" | Simulated two-sided market [S029] | Medium (synthetic) |
| **Labels matter.** Agents penalise "sponsored" tags and reward platform endorsements | [S030] | High (controlled) |
| **Preferences are unstable.** Demand concentrates on a few "modal" products, and preferences change with model updates. Small description tweaks by a seller-side agent shifted market share | [S030] | High (controlled) |
| **Manipulation.** Some models' payments could be redirected by manipulative agents. Resistance varies by model | [S029] | Medium |
| **Negotiation quality depends on the model.** Users represented by a stronger model sold for ~$2.68 more and bought for ~$2.45 less per item. Users on the weaker model rated fairness the same (4.05 vs 4.06) and *didn't notice*. "Aggressive" prompting had no significant effect | Real-goods internal pilot [S040] | High (but small, self-selected) |
| **Over-compliance.** Shop agents were talked into discounts and giveaways. A supervising agent cut discounts ~80% but kept similar blind spots | [S039] | High (case study) |
| **Refusal.** Agents refuse or stop because of programmed policy (spend caps, approval gates), provider safety classifiers, site blocking [S019][S063], or failures to complete | Platform docs and policies | Mechanisms documented; rates **UNKNOWN** |

**Is there a stable "agent buying preference"? No evidence supports one (INTERPRETATION, high confidence in the negative for now).** Behaviour depends on the model and version, the interface and layout, the instructions, and the owner's constraints. Observed regularities (position, speed, labels, structured data) are better understood as **biases of current systems** than as preferences. Optimising for them is a moving target and risks manipulation claims.

Keep four layers separate:
1. **Programmed policy:** budgets, allow-lists, approval rules.
2. **Human preference:** the owner's instructions.
3. **Model behaviour:** biases, persuadability.
4. **Market demand:** what humans ultimately pay for.

### 9.6 Do people want agents to buy for them?

Stated attitudes vary with wording (conflict C009). Accenture surveyed 25,590 consumers in 16 countries. A headline 74% said they would trust a personal agent more than their best friend to make a purchase, but only **9%** were open to fully autonomous purchases including payment, and about 32% would let an agent pick products within set limits [S067]. A separate US/UK survey by Riskified found 55% not comfortable with agents buying for them (reported via secondary coverage; see caveat on [S067]). **INTERPRETATION:** delegated *selection* is accepted far more readily than delegated *payment*. In Anthropic's experiment, 46% of participants *said* they would pay for a negotiating agent [S040]. That is a stated intention, not demonstrated willingness to pay.

## 10. Activity and timing: when do agents work?

### 10.1 What is known

- **Human-triggered chat follows human rhythms.** Anthropic's June 2026 Economic Index sampled conversations daily (Apr–Jun 2026). The personal-use share rises from about 35% on weekdays to just under 50% at weekends. News requests peak around 7 a.m. local time, business correspondence at 10–11 a.m., and recipes at 2.3× average at 6 p.m. US tax conversations were ~8× normal on 14 April [S041].
- **Agentic API use is more directive.** In Anthropic's data, API traffic is 64% "directive" (vs 32% on the consumer app), and about three-quarters is classified as automation [S042]. Sales-outreach and automated-trading workflows roughly doubled their share in three months [S042].
- **Agentic workloads are growing in token terms.** On OpenRouter, reasoning models carried over half of all tokens by late 2025. Average prompts grew from ~1.5k to over 6k tokens, and programming prompts routinely exceed 20k [S043].
- **Geography (one developer platform, by billing location).** US 47%, Singapore 9%, Germany 7.5%, China 6%. Asia's share rose from ~13% to ~31% within the study period [S043].
- **Scheduled agents are spread deliberately.** Managed schedulers add jitter (Anthropic: up to 15% of the interval, max 9 minutes) [S080]. ChatGPT caps scheduled tasks at no more than hourly [S079].

### 10.2 What is not known

**UNKNOWN.** We found no public data on:
- hourly or weekday patterns of *autonomous* or *API-based* agent activity (Anthropic's hourly analysis covers chat and Cowork only [S041]; OpenRouter aggregates weekly in UTC [S043]);
- when agents make *purchases*;
- activity by deployment type across providers.

Requests, active agents, transactions and completed tasks are different units, and no source reports all four.

**INTERPRETATION / RECOMMENDATION.** There is no evidence-based "peak hour" or "purchase window" for agents in general. Human-triggered agent use will follow local working and living patterns. Scheduled and event-driven agents run whenever their owners or triggering events dictate, increasingly around the clock and spread across time zones. If timing matters to your business (capacity planning, flash offers to agents), **measure it on your own traffic** by identifying agents through signed requests [S020][S059].

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
3. **High-risk screen.** Is the agent used in hiring, credit, education, essential services or other Annex III areas? If so, plan for obligations applying from 2 Dec 2027 [S049].
4. **Accountability.** Name a responsible human per agent, and document its purpose, tools, permissions and limits (Singapore MGF dimension 2 [S052]).
5. **Risk bounding.** Write down what the agent may never do (amount limits, data classes, external parties) (MGF dimension 1 [S052]).
6. **Controls.** Apply Appendix B.
7. **Records.** Keep logs sufficient to reconstruct decisions; align retention with GDPR.
8. **End users.** Tell users how to reach a human and how to contest an agent's action (MGF dimension 4 [S052]).

## Appendix D — Methodology

- **Process.** Inspect → baseline → plan → research → reconcile → draft → verify → revise (see `research/research-plan.md`).
- **Search and retrieval.** Web search plus direct page retrieval, 12 October 2026. Where direct retrieval failed (HTTP 403/503), we used search-engine extracts quoting the primary and marked the access method in the register.
- **Source hierarchy.** Specifications, official docs, pricing pages, terms, court decisions, filings, then independent research, then reputable news, then vendor blogs and aggregators. Vendor claims are labelled as claims.
- **Registers.** Sources (`research/sources.csv`, 81 entries); claims and conflicts (`research/claims-ledger.md`); coverage (`research/coverage-matrix.md`); opportunities (`opportunities/`); cost model (`models/`).
- **Verification.** See `verification/verification-report.md`, which covers the citation-resolution check, number reconciliation between prose and model outputs, and the adversarial self-review.

# References

Each entry gives the ID, title, publisher, publication date, URL, retrieval date, access method and confidence. Exact supporting passages, caveats and topics are in `research/sources.csv`.

- **[S001]** Building effective agents. Anthropic. 2024-12-19. <https://www.anthropic.com/engineering/building-effective-agents> (retrieved 2026-10-12; fetched; confidence high)
- **[S002]** Levels of Autonomy for AI Agents (arXiv 2506.12469; Knight First Amendment Institute). Feng, McDonald, Zhang (Univ. of Washington). 2025-06 (v2 2025-07-28). <https://arxiv.org/abs/2506.12469> (retrieved 2026-10-12; search-extract; confidence high)
- **[S003]** The state of AI in 2025: Agents, innovation, and transformation. McKinsey & Company. 2025-11. <https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2025> (retrieved 2026-10-12; search-extract (direct fetch 503); confidence medium)
- **[S004]** The state of AI in 2026: On the road to ROI. McKinsey & Company. 2026-08. <https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/the-state-of-ai-in-2026-on-the-road-to-roi.pdf> (retrieved 2026-10-12; search-extract (direct fetch 503; curl HTTP/2 error); confidence medium)
- **[S005]** What the 2026 Hype Cycle for Agentic AI Reveals. Gartner. 2026 (reported 2026-04-15). <https://www.gartner.com/en/articles/hype-cycle-for-agentic-ai> (retrieved 2026-10-12; search-extract (direct fetch 403); confidence medium)
- **[S006]** Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027. Gartner (press release). 2025-06-25. <https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027> (retrieved 2026-10-12; search-extract via multiple secondary outlets (direct fetch 403); confidence medium)
- **[S007]** Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026. Gartner (press release). 2025-08-26. <https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S008]** Time horizons of AI agents (METR). METR. page shows 2026-09-08 (no longer actively updated). <https://metr.org/time-horizons/> (retrieved 2026-10-12; fetched; confidence high)
- **[S009]** Time Horizon 1.1 / secondary summaries of METR doubling time. LessWrong & others (secondary). 2026. <https://www.lesswrong.com/posts/EYb2K9acKfyG2bome/metr-time-horizons-now-10x-year> (retrieved 2026-10-12; search-extract; confidence low)
- **[S010]** OWASP Top 10 for Agentic Applications for 2026. OWASP GenAI Security Project. 2025-12-09. <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/> (retrieved 2026-10-12; fetched (landing page) + search-extract for item names; confidence medium)
- **[S011]** The lethal trifecta for AI agents. Simon Willison. 2025-06-16. <https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/> (retrieved 2026-10-12; fetched; confidence high)
- **[S012]** Replit AI agent deletes SaaStr production database (coverage). eWeek / TechTarget / AI Incident Database. 2025-07. <https://www.eweek.com/news/replit-ai-coding-assistant-failure/> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S013]** OpenClaw (Wikipedia article). Wikipedia (citing Cisco, Axios, TechCrunch, Bloomberg, The Register). continuously updated (content to 2026-08-30). <https://en.wikipedia.org/wiki/OpenClaw> (retrieved 2026-10-12; fetched; confidence medium)
- **[S014]** OpenClaw security exposure counts (secondary security-vendor reports: SecurityScorecard, Bitsight, Koi Security). Various security vendors via secondary blogs. 2026-02/03. <https://www.digitalocean.com/resources/articles/openclaw-security-challenges> (retrieved 2026-10-12; search-extract; confidence low)
- **[S015]** Amazon v. Perplexity — Ninth Circuit vacates preliminary injunction (Cooley alert). Cooley LLP. 2026-08-06 (decision 2026-08-04). <https://www.cooley.com/news/insight/2026/2026-08-06-ninth-circuit-rules-on-ai-agent-access-to-third-party-websites-under-cfaa> (retrieved 2026-10-12; fetched; confidence high)
- **[S016]** Claude Code docs — Legal and compliance (Authentication and credential use). Anthropic. undated (retrieved live). <https://code.claude.com/docs/en/legal-and-compliance> (retrieved 2026-10-12; fetched; confidence high)
- **[S017]** Third-party harness restrictions on Claude subscriptions (secondary coverage). The New Stack; GitHub issue thedotmack/claude-mem#1826; others. 2026-01 to 2026-05. <https://thenewstack.io/anthropic-claudecode-opencode-split/> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S018]** Anthropic Consumer Terms of Service. Anthropic. effective 2025-10-08. <https://www.anthropic.com/legal/consumer-terms> (retrieved 2026-10-12; fetched; confidence high)
- **[S019]** Cloudflare: Your site, your rules — new AI traffic options; Changelog 2026-07-01; Block AI Bots docs. Cloudflare. 2026-07-01. <https://blog.cloudflare.com/content-independence-day-ai-options/> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S020]** Visa Introduces Trusted Agent Protocol. Visa (press release). 2025-10-14. <https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21716.html> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S021]** Visa and Partners Complete Secure AI Transactions; Visa Intelligent Commerce Connect. Visa (press releases). 2025-12 and 2026-04. <https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.21961.html> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S022]** Mastercard Agent Pay press releases (Agent Pay for Machines Jun 2026; trust & intelligence services Sep 2026; APAC/LAC live transactions). Mastercard. 2026-03 to 2026-09. <https://www.mastercard.com/global/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S023]** Universal Commerce Protocol (UCP) launch and rollout. Google & Shopify (via Shopify news and secondary). 2026-01-11 launch. <https://www.shopify.com/news/spring-26-edition-dev> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S024]** Introducing the Machine Payments Protocol. Stripe. 2026-03-18. <https://stripe.com/blog/machine-payments-protocol> (retrieved 2026-10-12; fetched; confidence high)
- **[S025]** Powering Product Discovery in ChatGPT. OpenAI. 2026-03-24. <https://openai.com/index/powering-product-discovery-in-chatgpt/> (retrieved 2026-10-12; search-extract (direct fetch 403); confidence medium)
- **[S026]** Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol; Stripe newsroom. OpenAI; Stripe. 2025-09-29. <https://stripe.com/newsroom/news/stripe-openai-instant-checkout> (retrieved 2026-10-12; search-extract; confidence high)
- **[S027]** ChatGPT Instant Checkout merchant adoption (secondary analyses). laioutr.com; eesel.ai. 2026. <https://www.laioutr.com/en/blog/chatgpt-instant-checkout-merchant-adoption-agentic-readiness-2026> (retrieved 2026-10-12; search-extract; confidence low)
- **[S028]** x402 adjusted volume analysis (Visa/Artemis via The Defiant). The Defiant reporting Visa's Cuy Sheffield / Artemis. 2026-04. <https://thedefiant.io/news/infrastructure/visa-s-sheffield-pegs-adjusted-x402-volume-at-19m> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S029]** Magentic Marketplace: An Open-Source Environment for Studying Agentic Markets. Microsoft Research. 2025-10. <https://www.microsoft.com/en-us/research/publication/magentic-marketplace-an-open-source-environment-for-studying-agentic-markets/> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S030]** What Is Your AI Agent Buying? Evaluation, Biases, Model Dependence & Emerging Implications (arXiv 2508.02630). Allouah, Besbes, Figueroa, Kanoria, Kumar. 2025-08 (v3 later). <https://arxiv.org/abs/2508.02630> (retrieved 2026-10-12; search-extract; confidence high)
- **[S031]** Adobe Analytics AI traffic to US retail (via Digital Commerce 360 / Decrypt). Adobe (via trade press). 2026-04 to 2026-06. <https://www.digitalcommerce360.com/2026/06/17/adobe-ai-referred-traffic-to-retail-sites-doubles-in-a-year/> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S032]** MCP specification 2026-07-28 — Key Changes (changelog). Model Context Protocol project (Agentic AI Foundation / Linux Foundation). 2026-07-28. <https://modelcontextprotocol.io/specification/2026-07-28/changelog> (retrieved 2026-10-12; fetched; confidence high)
- **[S033]** MCP blog — 2026-07-28 Specification Release Candidate / release posts. Model Context Protocol blog. 2026-05-21 (RC); 2026-07-28 (final). <https://blog.modelcontextprotocol.io/tags/protocol/> (retrieved 2026-10-12; fetched; confidence medium)
- **[S034]** Linux Foundation Announces the Formation of the Agentic AI Foundation (AAIF). Linux Foundation (press release). 2025-12-09. <https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation> (retrieved 2026-10-12; fetched; confidence high)
- **[S035]** A2A Protocol surpasses 150 organizations, lands in major cloud platforms (one-year anniversary). Linux Foundation (press release). 2026-04-09. <https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year> (retrieved 2026-10-12; fetched; confidence medium)
- **[S036]** A2A Protocol Specification (latest). A2A Project (Linux Foundation). undated page; latest released version 1.0.0. <https://a2a-protocol.org/latest/specification/> (retrieved 2026-10-12; fetched (first 100k chars); confidence high)
- **[S037]** Remote Labor Index: A Significant Increase in Digital Labor Automation. Center for AI Safety (with Scale AI). 2026-07-01. <https://safe.ai/blog/significant-increase-in-digital-labor-automation> (retrieved 2026-10-12; fetched; confidence high)
- **[S038]** Remote Labor Index: Measuring AI Automation of Remote Work (arXiv 2510.26787). Scale AI & Center for AI Safety. 2025-10. <https://arxiv.org/abs/2510.26787> (retrieved 2026-10-12; search-extract; confidence high)
- **[S039]** Project Vend: Phase Two. Anthropic. 2025-12-18. <https://www.anthropic.com/research/project-vend-2> (retrieved 2026-10-12; fetched; confidence high)
- **[S040]** Project Deal. Anthropic. 2026-04-24 (run Dec 2025). <https://www.anthropic.com/features/project-deal> (retrieved 2026-10-12; fetched; confidence high)
- **[S041]** Anthropic Economic Index report: Cadences. Anthropic. 2026-06-26. <https://www.anthropic.com/research/economic-index-june-2026-report> (retrieved 2026-10-12; fetched; confidence high)
- **[S042]** Anthropic Economic Index reports: Economic primitives (Jan 2026) & Learning curves (Mar 2026). Anthropic. 2026-01 / 2026-03. <https://www.anthropic.com/research/anthropic-economic-index-january-2026-report> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S043]** State of AI: An Empirical 100 Trillion Token Study with OpenRouter. OpenRouter & a16z. 2025-12-04. <https://openrouter.ai/state-of-ai> (retrieved 2026-10-12; fetched; confidence medium)
- **[S044]** Claude API Pricing (platform docs). Anthropic. live page (skill cache dated 2026-10-06). <https://platform.claude.com/docs/en/about-claude/pricing> (retrieved 2026-10-12; fetched (full markdown saved locally); confidence high)
- **[S045]** OpenAI API Pricing. OpenAI. live page. <https://developers.openai.com/api/docs/pricing> (retrieved 2026-10-12; fetched; confidence high)
- **[S046]** Gemini Developer API pricing. Google. last updated 2026-10-09. <https://ai.google.dev/gemini-api/docs/pricing> (retrieved 2026-10-12; fetched; confidence high)
- **[S047]** Claude plans & pricing. Anthropic. live page. <https://claude.com/pricing> (retrieved 2026-10-12; fetched; confidence high)
- **[S048]** LangSmith pricing. LangChain. live page. <https://www.langchain.com/pricing> (retrieved 2026-10-12; fetched; confidence high)
- **[S049]** AI Omnibus enters into force; AI Act policy page. European Commission (DG CONNECT). 2026-07 (entry into force reported 2026-07-27). <https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S050]** NIST CAISI AI Agent Standards Initiative; NCCoE concept paper on Software and AI Agent Identity and Authorization. NIST (via secondary: CSA research notes, law-firm summaries). 2026-02-17 (initiative); 2026-02-05 (concept paper). <https://labs.cloudsecurityalliance.org/research/csa-research-note-nist-caisi-ai-agent-standards-compliance-2/> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S051]** Joint guidance on the careful adoption of agentic artificial intelligence services. Canadian Centre for Cyber Security with CISA, NSA, ASD ACSC, NCSC-UK, NCSC-NZ. 2026-05-01 (date modified). <https://cyber.gc.ca/en/news-events/joint-guidance-careful-adoption-agentic-artificial-intelligence-services> (retrieved 2026-10-12; fetched (summary page); confidence medium)
- **[S052]** Singapore Model AI Governance Framework for Agentic AI (law-firm summary). IMDA Singapore via Baker McKenzie. 2026-01-22. <https://www.bakermckenzie.com/en/insight/publications/2026/01/singapore-governance-framework-for-agentic-ai-launched> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S053]** Anthropic run-rate revenue (CNBC; VentureBeat). CNBC citing investor update; VentureBeat. 2026-08-17. <https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html> (retrieved 2026-10-12; search-extract (direct fetch 403); confidence medium)
- **[S054]** Cursor/Anysphere revenue and acquisition (Wikipedia; Dealroom; press). Wikipedia; Dealroom; others. 2026. <https://en.wikipedia.org/wiki/Cursor_(company)> (retrieved 2026-10-12; search-extract; confidence low)
- **[S055]** Salesforce Delivers Record Second Quarter Fiscal 2027 Results. Salesforce (investor relations). 2026-08-26. <https://investor.salesforce.com/news/news-details/2026/Salesforce-Delivers-Record-Second-Quarter-Fiscal-2027-Results/default.aspx> (retrieved 2026-10-12; fetched; confidence high)
- **[S056]** AI agents market size forecasts (Grand View Research; MarketsandMarkets; BCC; TBRC). Market research firms (press releases/report pages). 2025-05 to 2026-03. <https://www.marketsandmarkets.com/Market-Reports/ai-agent-market-15761548.html> (retrieved 2026-10-12; search-extract; confidence low)
- **[S057]** The agentic commerce opportunity (McKinsey); Shopping in the Age of AI (ICSC & McKinsey). McKinsey & Company. 2025-10; 2026-04-27. <https://www.mckinsey.com/industries/retail/our-insights/the-agentic-commerce-opportunity-how-ai-agents-are-ushering-in-a-new-era-for-consumers-and-merchants> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S058]** Gartner agentic AI spending forecasts (via Software Strategies blog). Gartner via secondary blog. 2026-01/02. <https://softwarestrategiesblog.com/2026/02/26/roundup-of-agentic-ai-forecasts-and-market-estimates-2026/> (retrieved 2026-10-12; search-extract; confidence low)
- **[S059]** IETF Web Bot Auth (webbotauth) working group. IETF Datatracker + secondary. 2025-2026. <https://datatracker.ietf.org/group/webbotauth/about/> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S060]** Microsoft Entra Agent ID — What's new. Microsoft Learn. 2026. <https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S061]** AIUC-1 standard and AI agent insurance (secondary coverage). AIUC via secondary (CO/AI; FourWeekMBA; CSA crosswalk). 2025-2026. <https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/08/CSA_research_note_aiuc1_owasp_agentic_crosswalk_20260804-csa-styled.pdf> (retrieved 2026-10-12; search-extract; confidence low)
- **[S062]** The results of the 2026 Developer Survey are here. Stack Overflow. 2026-10-06. <https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/> (retrieved 2026-10-12; fetched; confidence high)
- **[S063]** Amazon blocked Meta's Muse and robots.txt had nothing to say. Search Engine Journal (citing GeekWire). 2026-09-29. <https://searchenginejournal.com/amazon-blocked-metas-muse-and-robots-txt-had-nothing-to-say/590494> (retrieved 2026-10-12; fetched; confidence high)
- **[S064]** Amazon Conditions of Use agent provisions (secondary: ConductAtlas; EcomCrew; Canopy). Amazon via secondary. 2025-05-30 / 2026-03-04 (conflicting). <https://conductatlas.com/platform/amazon/amazon-conditions-of-use/provision/CA-P-018576/agent-must-identify-itself-in-all-requests/> (retrieved 2026-10-12; search-extract; confidence low)
- **[S065]** Shopify has quietly set boundaries for 'buy for me' AI bots. Modern Retail; Retail TouchPoints. 2025-07-14. <https://www.modernretail.co/technology/shopify-has-quietly-set-boundaries-for-buy-for-me-ai-bots-on-merchant-sites/> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S066]** Agentic commerce chargeback liability (vendor analyses). Chargeflow; Shopappy. 2026. <https://www.chargeflow.io/blog/ai-agent-chargeback-liability> (retrieved 2026-10-12; search-extract; confidence low)
- **[S067]** Accenture Consumer Pulse Research 2026 ('Talk to my AI agent'). Accenture. 2026. <https://www.accenture.com/gb-en/insights/consulting/talk-my-ai-agent> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S068]** Piloting Claude for Chrome. Anthropic. 2025-08-26. <https://www.anthropic.com/news/claude-for-chrome> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S069]** OpenAI says AI browsers may always be vulnerable to prompt injection attacks (coverage of OpenAI Atlas hardening post). TechCrunch (reporting OpenAI blog). 2025-12-22. <https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S070]** We are Changing our Developer Productivity Experiment Design. METR. 2026-02-24. <https://metr.org/blog/2026-02-24-uplift-update/> (retrieved 2026-10-12; search-extract; confidence high)
- **[S071]** Intercom pricing (Fin AI Agent). Intercom. live page. <https://www.intercom.com/pricing> (retrieved 2026-10-12; fetched; confidence high)
- **[S072]** Klarna reverses AI customer-service overhaul (coverage). Entrepreneur; Tech.co; eMarketer. 2025-05. <https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S073]** Braintrust raises $80M Series B (SiliconANGLE); Langfuse acquired by ClickHouse (Jan 2026). SiliconANGLE; secondary. 2026-02-17. <https://siliconangle.com/2026/02/17/braintrust-lands-80m-series-b-funding-round-become-observability-layer-ai> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S074]** EU AI Act: Transparency Obligations Take Effect 2 August 2026. Cooley LLP. 2026-08-03. <https://www.cooley.com/news/insight/2026/2026-08-03-eu-ai-act-transparency-obligations-take-effect-2-august-2026> (retrieved 2026-10-12; fetched; confidence high)
- **[S075]** Google AI Developers Forum: mass 403 ToS suspensions on Gemini/Antigravity for open-source CLI users. Google AI Developers Forum (user reports). 2026-02-20 (thread start). <https://discuss.ai.google.dev/t/urgent-mass-403-tos-bans-on-gemini-api-antigravity-for-open-source-cli-users-paid-tier/124508/7> (retrieved 2026-10-12; fetched; confidence medium)
- **[S076]** LinkedIn User Agreement §8.2 prohibitions on bots/automation (via ConductAtlas). LinkedIn via ConductAtlas. current agreement. <https://conductatlas.com/platform/linkedin/linkedin-user-agreement/provision/CA-P-023526/prohibition-on-bots-or-inauthentic-automated-engagement/> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S077]** Occupational Outlook Handbook: Customer Service Representatives. US Bureau of Labor Statistics. May 2025 wage data. <https://www.bls.gov/ooh/office-and-administrative-support/customer-service-representatives.htm> (retrieved 2026-10-12; fetched; confidence high)
- **[S078]** Occupational Outlook Handbook: Software Developers. US Bureau of Labor Statistics. May 2025 wage data. <https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm> (retrieved 2026-10-12; fetched; confidence high)
- **[S079]** Scheduled Tasks in ChatGPT; ChatGPT agent (help center); ChatGPT release notes. OpenAI Help Center. 2026 (release note 2026-06-17). <https://help.openai.com/en/articles/10291617-what-is-agent-mode> (retrieved 2026-10-12; search-extract; confidence medium)
- **[S080]** Claude Managed Agents — Scheduled deployments. Anthropic (platform docs). beta (managed-agents-2026-04-01). <https://platform.claude.com/docs/en/managed-agents/scheduled-deployments> (retrieved 2026-10-12; fetched; confidence high)
- **[S081]** awesome-ai-agent-attacks: curated timeline of AI agent security incidents (2024-2026); MCP security statistics roundups. webpro255 (GitHub) / Practical DevSecOps (secondary aggregations). 2026. <https://github.com/webpro255/awesome-ai-agent-attacks> (retrieved 2026-10-12; search-extract; confidence low)

*81 sources cited in the paper; 0 further registered sources used for background: none.*
