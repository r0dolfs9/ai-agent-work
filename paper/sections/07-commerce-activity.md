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
- **Checkout inside AI surfaces, with human confirmation.** Google's UCP-powered checkout with Google Pay is reported live in the US with major retailers and Shopify merchants. The shopper still confirms the purchase [S023].
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
