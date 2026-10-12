## 9. Purchasing, payments, negotiation and refusal

### 9.1 Who is the buyer?

| Situation | Economic buyer (whose money) | Decision-maker | Evidence |
|---|---|---|---|
| Consumer shopping assistant | The consumer | Mostly the human. The agent compares and recommends, the human clicks "buy" | OpenAI's pivot to discovery [S025]; Adobe referral data [S116] |
| Delegated consumer purchase with mandate | The consumer | The agent, within pre-signed limits | AP2 "intent mandates" design; pilots only [S035] |
| Employee using an agent at work | Employer | Employee, under procurement policy | Organizations set usage limits (38%) and review spend (28%) [S062] |
| Developer agent buying API calls/compute | Developer or company | Agent, within a programmatic budget | MPP/x402 [S024][S091]; managed-agent budgets [S080] |
| Agent buying from agent | The owners behind each agent | Agents, within budgets | Experiments only [S029][S040] |

**INTERPRETATION.** Today the economic buyer is almost always a **human or an organization**, and agents are mostly **influencers and executors**. Fully delegated purchasing exists in pilots, in machine-to-machine micro-payments, and in experiments.

### 9.2 What agents have demonstrably bought

**First, define autonomy.** Purchase figures are only comparable at the same level of autonomy.

| Level | Description | Who presses "pay"? |
|---|---|---|
| P1 | Agent recommends; human purchases separately | Human |
| P2 | Agent prepares the cart or checkout; human approves in the flow | Human, inside the AI surface |
| P3 | Agent executes under limits the human delegated earlier (mandate, scoped token, budget) | Agent, within pre-set limits |
| P4 | Agent transacts with no human approval at the time of purchase and no purchase-specific mandate | Agent |

**Bounded, attributable evidence** (no figure below can be added to another: they use different units, periods and populations):

| Evidence | Level | Unit | Period / population | Value | Source |
|---|---|---|---|---|---|
| AI-referred visits to US retail sites | P1 | Traffic and conversion, not purchases by agents | May 2026 vs May 2025; >1trn visits in Adobe Analytics | +138% YoY; converts 54% better than non-AI traffic; "AI-referred" undefined | [S116] |
| Google UCP checkout in AI surfaces | P2 | Availability | US, 2026 | Live with named retailers; volumes not disclosed | [S023] |
| ChatGPT Instant Checkout | P2 | Availability | Sep 2025 to Mar 2026 | Scaled back in Mar 2026; volumes not disclosed | [S026][S025] |
| Visa controlled agent transactions | P2–P3 | Count | To Dec 2025, partners | "Hundreds" | [S021] |
| Mastercard "first live agentic transactions" | P2–P3 | Announcements | 2025–2026, several countries | No volumes | [S022] |
| x402 payments (Visa/Artemis), adjusted | P3–P4 (agent, script or human cannot be distinguished) | Payment volume | May 2025 to 21 Apr 2026, onchain | **$15.0M across 109.6M transactions** after removing identified wash and test activity | [S091] |
| x402 payments (TRM Labs), screened | P3–P4 | Payment volume | May 2025 to mid-2026 | $52.7M raw; **$25.62M** "screened commerce"; only **0.6%–7.5%** looks agentic; agents moved "roughly $5,000–11,000 a month" | [S090] |
| MPP (Stripe/Tempo) | P3–P4 | Transactions | Since Mar 2026 | ~20,000 transactions/day, per a Visa executive's social-media post (no volume, no agent share) | [S028] (low confidence) |
| Anthropic Project Deal | P4 within an experiment | Gross value | One week, Dec 2025, 69 employees | 186 deals, just over $4,000 | [S040] |

**CALCULATION.** Applying TRM's agentic share to its screened total gives a cumulative upper bound of about $0.15M–$1.9M (0.6%–7.5% × $25.62M) of x402 commerce that looks agent-driven, over roughly a year. That is the largest *independently analysed*, plausibly autonomous (P3–P4) purchase stream found in this study. TRM notes that "a scheduled script and an agent look identical onchain" [S090].

**Why no global total can be built.**
- The figures above mix different units: traffic, availability, counts and payment volume.
- They mix different autonomy levels.
- Card networks publish no agent-transaction volumes. Visa's July 2026 earnings call gave none, according to secondary transcripts [S121].
- Payment volume is not gross purchase value, and it is not provider revenue.
- Gross onchain counts include wash, test and script activity. For x402, Coinbase's gross "160M+ agentic payments" against Visa's adjusted $15.0M shows the gap (conflict C006).

**UNKNOWN.** The global value of P3–P4 purchases is not established in any public source found in this study. The defensible statement is narrower: *verified autonomous agent purchasing is, as of October 2026, small, concentrated in machine-to-machine micro-payments and experiments, and dwarfed by human purchasing that agents influence.*

**What changed since v1.0.** The v1.0 x402 figure ($19M across ~134M transactions; top 1% of buyers ≈90% of volume) came from a social-media post reported by a crypto news site. It is replaced by Visa's published report ($15.0M / 109.6M) and TRM's independent analysis. The concentration statistic is dropped because it does not appear in the Visa report as read.

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

Stated attitudes vary with wording (conflict C009). Accenture surveyed 25,590 consumers in 16 countries, including France, Germany, Italy, Spain, Sweden and the UK, online on 7–22 January 2026 [S115]:
- 74% said they would trust a personal agent more than their best friend to make a purchase.
- 32% would let an agent decide within set boundaries, with the consumer still validating before paying.
- Only **9%** were open to an agent initiating *and completing* purchases autonomously. Elsewhere the same publication says 12%, an internal inconsistency we note rather than resolve.

A separate US/UK survey by Riskified found 55% not comfortable with agents buying for them (reported via secondary coverage; see caveat on [S067]).

**INTERPRETATION:** delegated *selection* (P2) is accepted far more readily than delegated *payment* (P3–P4), and this holds across the 16 countries surveyed. In Anthropic's experiment, 46% of participants *said* they would pay for a negotiating agent [S040]. That is a stated intention, not demonstrated willingness to pay.

## 10. Activity and timing: when do agents work?

### 10.1 What "active" means

Six different things get called agent "activity". No public source reports more than two of them for the same population:
1. **Model requests** (API calls or tokens).
2. **Execution runs** (a session or task from start to finish).
3. **Background or scheduled tasks** started without a human.
4. **Tool calls** (including web fetches).
5. **Completed workflows or outputs** (for example, a pull request opened).
6. **Transactions** (payments).

Each must also be split by trigger: human-triggered, scheduled, event-driven, continuously operating, or research and synthetic workloads.

### 10.2 What the evidence shows

| Trigger / unit | Evidence | Observation period, time zone, population | Finding | Strength |
|---|---|---|---|---|
| Human-triggered **chat and Cowork conversations** | Anthropic Economic Index "Cadences" [S041] | 10 Apr–10 Jun 2026; local time from IP; consumer accounts | Personal share ~35% on weekdays, just under 50% at weekends. News peaks ~7 a.m., business correspondence 10–11 a.m., recipes 2.3× average at 6 p.m. | High for that population; not autonomous agents |
| Human-triggered **agent web fetches** (fetching pages on a person's behalf) | Cloudflare network telemetry [S092] | Year to Sep 2026; global Cloudflare network | Daily agent requests grew >1,700%. Agent traffic "follows human routines, with a weekly rhythm and a dip over the summer holidays". No figures published | Medium (qualitative) |
| Human- or event-triggered **coding-agent outputs** (pull requests opened by agents) | **Our analysis** of the public AIDev dataset [S093] (`research/analysis/aidev_timing.py`) | 2,743,854 agent-authored PRs on public GitHub, 24 Dec 2024–24 Oct 2025, UTC | See below | High for public GitHub PR creation; not general agent activity |
| **Model requests** on a developer marketplace | OpenRouter study [S043] | Weekly, UTC, to late 2025 | No time-of-day analysis. Shows growth of agentic token use | Medium |
| **API traffic mix** | Anthropic Economic Index [S042] | Jan–Mar 2026 | API traffic 64% directive, ~75% automation. No timing published for API or Claude Code | Medium |
| **Scheduled tasks** | Platform documentation [S079][S080] | Current | Schedulers deliberately add jitter (Anthropic: up to 15% of the interval, max 9 minutes). ChatGPT tasks run at most hourly | Mechanism only; no usage data |
| **Continuously operating** agents | — | — | **No representative public dataset was found within the documented search scope** | Gap |
| **Purchases** by agents | §9.2 [S090][S091] | Onchain | Monthly totals only; TRM reports agent transaction counts rose to a mid-2026 peak and then fell | Low for timing |

**Coding-agent pull requests (CALCULATION, our analysis of AIDev [S093]):**
- **Weekends:** 25.8% of agent-authored PRs, against 28.6% if activity were spread evenly across the week. Weekday shares range from 14.3% (Monday) to 15.4% (Wednesday). Saturday is 12.7% and Sunday 13.1%.
- **Hours:** the busiest UTC hours are 14:00–17:00 (~5.0–5.1% each) and the quietest 00:00–05:00 (~3.2–3.4% each). The peak-to-trough ratio is only **1.57**. 20% of PRs are opened between 00:00 and 06:00 UTC.
- **By agent:** the pattern holds for every agent. Weekend share runs from 21.4% (Devin) to 28.0% (Google Jules), and peak-to-trough from 1.53 to 1.77. OpenAI Codex, 75% of the sample, peaks at 20:00 UTC.

**INTERPRETATION.**
- Coding-agent output is *much flatter* across the day than a single-time-zone office pattern would be. That is consistent with a globally distributed user base and some agents running unattended.
- There is still a measurable weekday/working-hours lean, so human triggering still shapes activity.
- This dataset does **not** tell us when agents *ran* (a pull request is the end of a run). It does not tell us user time zones, or how much of the activity was scheduled versus human-started. There is also no human baseline in the dataset to compare against.

### 10.3 Conclusion and what remains unknown

- **Supported:** human-triggered agent use (chat, web fetches) follows human weekly and daily rhythms [S041][S092]. Coding-agent output on public GitHub runs around the clock, with only a mild working-hours peak [S093].
- **Not supported:** any universal "peak hour" or "purchase window" for agents. No representative public dataset was found within the documented search scope for:
  - hour-of-day activity of *scheduled* or *continuously operating* agents;
  - agent *purchases* by time;
  - activity by deployment type across providers.
- **What would resolve it:** provider telemetry split by trigger type (scheduled vs human vs event), or merchant logs of signed-agent requests [S020][S059].

### 10.4 Proposed measurement method for a future authorised deployment (PROPOSED METHOD, not observed behaviour)

**Events to log** (one row each, UTC timestamp plus the requester's IANA time zone where known):
- `run_started` and `run_ended`, with the trigger type (human, schedule, webhook or event, continuous loop) and outcome (completed, failed, escalated, budget-stopped);
- `model_call`, with tokens and cost;
- `tool_call`, with tool name and read/write class;
- `approval_requested` and `approval_decided`, with latency;
- `payment_attempted` and `payment_settled`, with amount, currency, mandate ID and autonomy level P1–P4;
- `external_block`, with HTTP status, site and reason (to feed §11.3).

**Privacy controls:**
- Pseudonymous user IDs, with no prompt or response content in timing tables.
- Coarsen location to country and time zone.
- Aggregate to at least hourly bins with a minimum cell size (for example ≥10 users) before analysis.
- Retention: 90 days for raw events, then aggregates only.
- Document the legal basis under the GDPR (legitimate interest assessment, or consent for consumer products) and list the logging in the privacy notice.

**Observation period:** at least 8 full weeks, including one public-holiday period, to separate weekly from seasonal effects.

**Metrics:**
- Share of runs by trigger type.
- Hour-of-week distribution per trigger type in *local* time and in UTC.
- Peak-to-trough ratio.
- Weekend share against 2/7.
- Concurrency (95th-percentile simultaneous runs) for capacity planning.
- Median approval latency by hour.
- Payment attempts by autonomy level and hour.
- Block events per 1,000 external requests by site.
