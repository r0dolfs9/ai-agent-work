# Dossier R2: Coding-agent enablement with a measured pilot

*Recommended first route, **if you can write and review code professionally**. Register ID O07. Version 1.2, 12 October 2026. About 10 minutes to read.*

## 1. In one paragraph

Small software teams already pay for coding agents (Claude Code, Cursor, Copilot and similar). Most adopt them unevenly and cannot tell whether they help. You would sell a fixed-scope engagement in four parts:
1. Configure the agent safely on the team's real codebase.
2. Train the team in a 2-day hands-on workshop.
3. Measure a 4-week pilot against a baseline.
4. Deliver a written verdict: what works, what doesn't, what it costs per merged change, and which rules to keep.

The differentiator is **measurement and safe setup**, not tutorials. Tutorials are free.

## 2. Who pays and who decides

| Role | Who | What they care about |
|---|---|---|
| Economic buyer | CTO, head of engineering, or the founder in a 5–30-developer company or agency | Is the tool spend justified? Are we shipping faster without more defects? |
| User | Developers | Not being slowed down; not being judged by crude metrics |
| Blocker | Security or compliance lead, or a client contract forbidding code upload | Code and secret exposure; licence and IP questions |

Buyer type: **human organisation**. This is a service for human operators of agents, not a product bought by agents.

## 3. The problem and today's workaround

**The problem.**
- Coding agents are the most widely used agents. Among developers using AI, 66% use coding agents [S062], and Claude Code alone passed a $2.5bn run rate in February 2026 [S141].
- But controlled studies of productivity are inconclusive, and developers *over-estimate* their own speed-up [S070].
- Agents also cause real incidents. One agent deleted a production database during a code freeze [S012].
- So teams pay for tools without knowing the return, and without guard-rails.

**Workarounds.**
- Vendor documentation and best-practice guides (free).
- Developers teaching each other.
- Partner courses: valantic, an Anthropic partner, sells a 2-day Claude Code course at **€890 per person** [S128].
- Marketplace team workshops, from $250 (2 hours) to $900 (a full day) [S129].
- Doing nothing.

## 4. Evidence versus hypotheses

| Statement | Status |
|---|---|
| Teams use and pay for coding agents | **Fact** [S062][S088] |
| Paid training for coding agents exists, at €890 per person for 2 days, and mentor workshops from $900 | **Fact (list prices)** [S128][S129]. Volumes unknown |
| Productivity gains are uncertain | **Fact** [S070] |
| Buyers will pay a newcomer **€1,500–7,000** for setup, training and a measured pilot | **Hypothesis**: untested |
| Measurement is valued more than training alone | **Hypothesis**: the key one to test |
| Small teams (5–30 devs) are reachable without a network | **Hypothesis**: likely slow; see §8 |

## 5. What you would sell and deliver

**Offer, quoted as two priced options** so the test reveals whether measurement is valued:
- **A. Safe setup + 2-day workshop.** Assumed €2,000–2,500.
- **B. A plus a 4-week measured pilot and report.** Assumed €3,000 as a newcomer, €4,000 with a track record.

**What "measured" can honestly mean.** On a 5–12-developer team over 4 weeks, measurement produces *adoption and cost telemetry*: who uses the agent and for what, cycle time on comparable changes, review load, incidents and cost per merged change. It does **not** produce a statistically solid productivity verdict, and the report must say so.

The table shows option B.

| Week | Activity | Your hours (base) |
|---|---|---|
| 0 | 45-minute scoping call; data-access agreement (read-only repository metrics; no code leaves the client); agree 4 metrics | 2 |
| 1 | Baseline: pull 8–12 weeks of history (pull-request cycle time, review time, change size, reverted changes or bug tickets). Write a **safe-configuration policy** covering agent permissions, sandbox, secrets handling, which actions need approval, and the "never all three" rule (private data + untrusted input + outbound send) [S011] | 6 |
| 2 | **2-day workshop on their own codebase**: task decomposition, context files, test-first prompting, review discipline, cost control (caching, model choice; see paper §6) | 14 |
| 3–6 | Pilot: weekly 30-minute check-in; collect metrics; log incidents and cost | 5 |
| 7 | Report (8–12 pages): before/after telemetry with explicit statistical caveats, cost per merged change, recommended rules, what to stop doing; 1-hour readout | 4 |
| — | Rework and revisions (20% assumed) | 5 |
| | **Total delivery** | **≈31 h** (model: 26 h + 20%) |

**Optional add-ons (hypotheses):**
- a quarterly re-measurement (€800);
- a configuration review for new repositories.

**Never promised:** a productivity percentage. The report states what was measured and how reliable it is.

## 6. Skills, credibility, tools and access

- **Skills (required):**
  - professional software development, including reading unfamiliar codebases and judging code review quality;
  - hands-on, daily use of at least one coding agent;
  - basic data analysis (pulling repository metrics; simple before/after comparisons with honest caveats).
- **Credibility:** a public, measured case study. The cheapest is your own or an open-source repository: "I ran a 4-week measured pilot on X; here is the method and the data".
  - Without it, cold outreach is unlikely to work (Interpretation).
  - A vendor partner status (not required) would add credibility later.
- **Tools:** a coding-agent subscription (≈€20–200/month, depending on vendor and plan; check current pricing before buying); a repository-analytics script (you can write it); a slide/report template.
- **Access:** to engineering leads. Your network matters most. Otherwise use public proof plus community channels: meetups, developer forums, LinkedIn posts. Each requires your approval before anything is posted.

**Self-check before choosing this route (no approval needed).** Could you, in one weekend:
1. set up a coding agent with restricted permissions on a real repository;
2. complete three non-trivial changes with it;
3. explain where it failed?

If not, choose R4 or "learn first".

## 7. Setup, workload and unit economics (Calculation, `models/route_economics.py`)

<!-- econ:start -->
*Cases: **low** = adverse inputs; **base** = a newcomer without track record or warm contacts; **high** = with a network or strong public proof. Benchmark: about €8.69/h net for an average Latvian professional [S126][S100]; your own contracting rate is the real comparator.*

| | Low | Base (newcomer) | High (with network) |
|---|---|---|---|
| Price per engagement (net of VAT) — assumption | €1,500 | €3,000 | €4,000 |
| Engagements won per month once steady | 0.25 | 0.5 | 1 |
| Months before first sale | 9 | 6 | 4 |
| Selling hours per *won* engagement | 60 h | 40 h | 25 h |
| Delivery hours per engagement incl. rework | 39 h | 31 h | 31 h |
| One-time setup: cash / owner hours | €400 / 80 h | €400 / 60 h | €400 / 50 h |
| Monthly fixed cash costs | €160 | €180 | €220 |
| Revenue per month once steady (net of VAT) | €375 | €1,500 | €4,000 |
| Operating profit per month once steady | €176 | €1,215 | €3,580 |
| Owner hours per month once steady | 31 h | 42 h | 62 h |
| **Self-employed take-home per month once steady** | €159 | €832 | €2,418 |
| Take-home per owner hour once steady | €5.2 | €20.0 | €38.9 |
| First 12 months: operating cash before income tax | −€1,311 | €5,810 | €27,360 |
| First 12 months: owner hours | 361 h | 466 h | 672 h |
| **First 12 months: take-home per owner hour** | −€3.6 (loss) | €11.2 | €27.6 |
| First 12 months under the combined adverse case | −€7.0 (loss) | −€2.8 (loss) | €6.2 |

Setup and fixed-cost contents (assumption): setup €400 = coding-agent subscriptions for the proof case (€150), domain/email/site (€100), metrics tooling (€150); fixed = bookkeeping, tool subscriptions, model API.
<!-- econ:end -->

## 8. Competition, substitutes and why customers may refuse

| Competitor or substitute | Why a buyer might choose it |
|---|---|
| Vendor docs, webinars and built-in onboarding | Free; "good enough" |
| Vendor partners (e.g. valantic [S128]) | Brand, official status, invoices a large company accepts |
| Mentors and marketplaces [S129] | Cheaper, per session |
| Internal champion developer | No procurement needed |
| Engineering-analytics SaaS | Ongoing dashboards instead of a one-off pilot |

**Likely refusal reasons:**
- "We already use it; developers figure it out."
- "We can't let an outsider see our repository."
- "Metrics feel like surveillance."
- "No budget until next quarter."

The offer answers these by:
- using read-only metrics only, with no code upload;
- reporting at team level, not per person;
- fixing the price below a partner course.

## 9. Global distribution and acquisition barriers

- **Market reach.** Demand is global and the work can be fully remote. The strongest buyers by willingness to pay are in high-wage markets (US, DE, Nordics). There a measured 10% time saving is worth more: an all-in hourly labour cost of €45 in Germany against €16.3 in Latvia [S119].
- **Barriers:**
  - no track record;
  - cold outreach has low response rates (unknown for this offer; the test measures it);
  - time zones for US clients;
  - client contracts restricting code access.
- **Channel order (Interpretation):**
  1. your own network and warm introductions;
  2. the public proof case, shared in developer communities;
  3. referral partners: development agencies, fractional CTOs, and later the coding-agent vendors' partner programmes;
  4. a freelance-marketplace profile for "coding-agent setup";
  5. personal one-to-one messages on professional networks.
- **Not unsolicited bulk email.** In Germany, advertising email needs prior consent, B2B included [S139]. Check each target country's rules before any cold email.

## 10. EU and Latvian operating implications

- **Form:** self-employed or an individual merchant is enough to start. An SIA is optional, for liability. The risk here is low–medium if you never get write access to production.
- **VAT:**
  - non-EU clients are outside Latvian VAT;
  - **any VAT-registered client in another EU country triggers full Latvian VAT registration before the first such sale** (s.59(8)) [S122], plus reverse-charge invoicing and EU sales statements, and ends micro-enterprise eligibility [S124];
  - Latvian clients pay 21% VAT once you are registered.
- **Buying the agent subscriptions:** if you are not fully registered, use the special s.139² registration. The 21% VAT on foreign tools is then a non-reclaimable cost [S122].
- **GDPR:** repository metrics usually contain developer names, so you act as a processor. You need a short data-processing agreement and must keep metrics aggregated [S110].
- **AI Act:** you train staff and configure tools, which supports the client's AI-literacy duty [S107]. No high-risk category is involved.

## 11. What would invalidate this route

- In the test, fewer than 2 of 10 qualified conversations show willingness to pay at €1,500 or more.
- Buyers consistently say "training yes, measurement no", and only at mentor prices of a few hundred euros.
- A vendor ships free team analytics that answers "is it working?"
- Your own proof pilot shows no measurable change, so you have nothing credible to sell.

## 12. Cheapest credible first test

See **plan V2** in `05-validation-plans.md`. In outline:
- **Phase A (no approval needed):** run a measured pilot of about 5 weeks on your own or an open-source repository, taking the baseline from history, and write the case study.
- **Phase B (needs approval):** contact up to 25 engineering leads through warm introductions, referrals, communities or personal network messages. No unsolicited email to German recipients [S139]. Quote two priced options.
- **Caps:** ≤60 hours, ≤€150 and 10 weeks.
- **Success:** ≥2 strong commitments (a paid engagement, an order with a deposit, or a paid scoping session) at ≥€1,500.
- **Channel failure:** fewer than 3 conversations means the channel failed and demand is untested.

## 13. Illustrative engagement (not a real customer)

> **Illustrative.** A 12-developer software agency in Germany has used a coding agent for 4 months. Usage is uneven: three heavy users, five occasional, four none. The founder asks whether to keep paying.
>
> - **Week 0.** A call and a data agreement. Read-only access to merge-request metadata through an exported CSV. No source code leaves the agency.
> - **Week 1.** Baseline: median merge-request cycle time, review comments per change, and reverted changes per month. The safe-configuration policy: the agent runs in a sandbox, has no production credentials, needs approval before any shell command touches deployment, and keeps secrets out of context.
> - **Week 2.** A 2-day workshop on two real backlog items.
> - **Weeks 3–6.** Weekly check-ins. One incident is logged: the agent edited a migration file outside scope. It was caught in review, and the policy was updated.
> - **Week 7.** Report: "cycle time down X% for small changes, no change for large ones; review load up; cost €Y per merged change; keep for test-writing and refactoring, stop for schema changes."
> - **Commercials.** €3,000 net (newcomer price; €4,000 once there is a track record). The agency is a German business with a VAT ID, so the invoice is reverse charge and the operator must be fully VAT-registered in Latvia **before** invoicing. About 31 hours of delivery.
>
> *The X and Y values are deliberately blank: no result has been observed.*
