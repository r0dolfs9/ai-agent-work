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

**INTERPRETATION.** The boundary is a spectrum, not a wall. Many commercial "agents" are really workflows with one LLM step, which is often *good engineering* rather than a failing. But it also enables **"agent washing"**: Gartner applies the term to rebranding chatbots, robotic process automation (RPA) and assistants as agents, and estimated in mid-2025 that only about 130 of the thousands of vendors claiming agentic AI were real [S087].

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
| **Coding agents** | Read, write, run and test code in a repository | Claude Code, GitHub Copilot agent, Cursor, OpenAI Codex | **Strong**: 66% of AI-using developers use coding agents [S062]; Claude Code run-rate >$2.5bn (Feb 2026) [S088]; Cursor disclosed $1bn ARR (Nov 2025) [S054] |
| **Enterprise platform agents** | Agents inside CRM/ERP/helpdesk suites | Salesforce Agentforce, Microsoft Copilot Studio, ServiceNow | **Medium**: Agentforce ARR >$1.5bn on a broadened definition; 3.2bn "agentic work units" in one quarter [S055] |
| **Customer-service agents** | Resolve customer conversations | Intercom Fin, Sierra, Decagon | **Medium**: per-outcome pricing in market [S071]; vendor revenue figures unverified; Klarna partly reversed an AI-first approach over quality [S072] |
| **Browser / computer-use agents** | Operate websites or desktops like a person | Perplexity Comet, Claude in Chrome; OpenAI moved browser agents into ChatGPT and a Chrome extension after deprecating its Atlas browser (Aug 2026) [S117] | **Early and unstable**: security limits acknowledged by vendors [S068][S118]; legal disputes over access [S015][S063]; a flagship product discontinued within a year [S117] |
| **Personal / general assistants** | Email, calendar, research, errands | ChatGPT Work and scheduled tasks [S079], Claude Cowork, OpenClaw (open source) [S013] | **Mixed**: very high interest (OpenClaw 247k GitHub stars by March 2026 [S013]) alongside serious security incidents [S014] |
| **Commerce agents** | Discover, compare, buy | ChatGPT shopping, Google UCP checkout, Perplexity, Meta Muse | **Discovery yes, buying rare**: §9 |
| **Autonomous services / machine payments** | Agents paying APIs or other agents per use | Stripe/Tempo MPP, Coinbase x402, Mastercard Agent Pay for Machines | **Very early**: ~$15.0M adjusted x402 volume May 2025–Apr 2026 [S091], of which only 0.6%–7.5% of screened commerce looks agent-driven [S090] |

### 2.2 Adoption: reading the surveys correctly

Different surveys ask different questions, and headline numbers diverge (conflict C001 in the ledger):

| Source | Population | Question | Result |
|---|---|---|---|
| Gartner 2026 CIO and Technology Executive Survey [S098] | CIOs/tech executives; sample size and geography not published on the article | Has your organization *deployed* AI agents? | **17%** yes; >60% expect to within two years |
| McKinsey State of AI 2026 [S084] | 1,719 respondents in 97 nations, online, 4 May–8 Jun 2026, weighted by national GDP share; 36% at >$1bn firms | Is your organization *scaling* agents? ("scaling" not defined) | **40%** of respondents at >$1bn-revenue firms (27% a year earlier); **22%** at smaller firms |
| McKinsey State of AI 2025 [S085] | 1,993 respondents in 105 nations, 25 Jun–29 Jul 2025 | At least *experimenting*? | **62%** (23% scaling somewhere + 39% experimenting); no more than 10% scaling in any one function |
| Gartner poll, Jan 2025 [S087] | 3,412 **webinar attendees** (self-selected) | Investment in agentic AI | 19% significant, 42% conservative, 8% none, 31% waiting/unsure |
| Eurostat ICT usage in enterprises 2025 [S096] | Official EU survey, enterprises with 10+ employees | Use of *any* AI technology (not agents specifically) | **EU 20.0%** (2024: 13.5%); Latvia 12.2%, Estonia 23.4%, Lithuania 21.3%; range 5.2% (Romania) to 42.0% (Denmark) |
| OECD practitioner interviews, Sep 2026 [S097] | 25 organisations (74 contacted) in 11 countries across Americas, Europe, Asia, Africa | How are agents deployed and governed? | Qualitative: moving into workflows; safeguards = incremental autonomy and human checkpoints for high-stakes actions; "illustrative rather than representative" |
| Stack Overflow 2026 [S062] | >30,000 developers | Use coding agents? | **66%** of AI users; only **20%** use AI for deploying/operating production systems |

**Geographic note.** The McKinsey and Gartner figures are global or unspecified and weighted toward large organizations. The official EU statistic is lower and broader: 20% of EU enterprises use *any* AI, and Latvia is below the EU average at 12.2% [S096]. These sources do not justify stating a single "agent adoption rate" for any one country.

**INTERPRETATION.** The defensible summary is: *most large organizations are experimenting; a minority (roughly one-fifth to two-fifths, depending on definition) have agents in production somewhere; production use is narrow and concentrated in coding, customer service and internal knowledge work.* Gartner itself places agentic AI at the "Peak of Inflated Expectations" and notes most deployments are narrowly scoped [S098], while predicting that over 40% of agentic AI projects will be cancelled by the end of 2027 for cost, unclear value or weak risk controls [S087]. That prediction and the rapid revenue growth at a few vendors (§12) are compatible: spend is concentrating in a few proven uses while many generic projects fail (conflict C002).

A telling data point on substitution: 32% of McKinsey respondents said their organization had decided against buying at least one software product or feature because it could be built in-house with agentic coding tools [S084]. **INTERPRETATION:** coding agents are starting to change *build-versus-buy* decisions — a risk for small software vendors and an opportunity for builders.

### 2.3 Demonstration versus operation

Use the following tests before believing a claim (RECOMMENDATION):

1. **Is the task checkable?** Code with tests, a resolved ticket confirmed by the customer, a reconciled invoice. Unverifiable "productivity" claims are weak.
2. **Who measured, how?** Vendor dashboards (e.g., "outcomes" counted when a customer does not ask for further help [S071]) differ from independent human judging; on one benchmark an automated LLM judge over-estimated the newest models' success by roughly 2.3–3× compared with human judges [S037].
3. **Is it in production with real money or data at stake?** Most announced "first agentic transactions" are controlled pilots [S021][S022].
4. **What is the denominator?** "Billions of agentic work units" [S055] or "160M+ agentic payments" (gross) [S028] are activity counts, not outcomes or revenue.
