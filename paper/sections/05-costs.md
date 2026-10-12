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
