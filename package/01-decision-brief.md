# Owner decision brief: is there an opportunity worth testing, and which first?

*Version 1.2 · 12 October 2026 · about 3,100 words of text plus tables · 18 minutes to read · revised after independent factual and commercial review*

This brief answers one question. **Is there a credible business opportunity in AI agents for you to explore? If so, which route should get your attention first, and what would it take to test it without committing to a business?**

Your technical skill, budget, available time and customer contacts are not known to me. I have not guessed them. Where the answer depends on them, the recommendation branches (§7).

How to read the labels:
- **Fact**: a claim checked against a source; the source ID is in brackets, e.g. [S127], and is listed in `research/sources.csv`.
- **Calculation**: something we computed.
- **Assumption**: our input to a model.
- **Interpretation**: our judgement.

No customer has been contacted. No price has been tested, no money spent and nothing published. Every demand statement about *your* offer is therefore a hypothesis.

---

## 1. The short answer

- **Yes, there is a credible opportunity to *explore*.** "Explore" here means a capped, reversible test, not starting a company. The opportunity is in **services sold to the people and companies who run agents**, not in products that agents buy for themselves.
- **Recommended first route (conditional).**
  - **If you can write and review code professionally:** explore **R2, coding-agent enablement with a measured pilot** for small software teams.
  - **If you cannot:** either use **R4, small AI workflow automations** sold through a freelance marketplace, *as paid practice*, or **learn first**. R4 has the clearest evidence that people pay, but also the lowest prices and the most competition.
  - **If you have a security background:** the limited **agent risk review (R1)** becomes a strong alternative.
- **What decides the money is your access to buyers, more than the route.**
  - **As a newcomer without warm contacts:** our base case is a **first year paying roughly €3–11 per hour after tax** (Calculation). That is around an ordinary Latvian professional's net pay of about €8.7 per hour, and below it for two of the four routes.
  - **With a network or strong public proof:** the same routes pay roughly **€23–36 per hour** in the first year.
  - **Your real benchmark** is your own employment or contracting rate (unknown to me). If you are a developer, contracting will probably pay more in year one than any of these routes (Interpretation).
  - The reason to test anyway is **option value**: a cheap way to learn whether buyers will pay you, before committing.
- **What testing costs (proposed caps).** About **50–60 hours over 8–10 weeks** and **under €150 of cash**. Nothing is registered until someone pays.
  - Several steps need your explicit approval because they involve contacting people or opening accounts (`05-validation-plans.md`).
  - **Do not send unsolicited sales emails to German businesses** (and check other EU countries first). Germany requires prior consent for advertising email, B2B included [S139].
- **What would reverse it.** Stop and choose "learn first" or "defer" if either happens:
  - warm or referred conversations produce **no paid commitment** (a signed order with a deposit, or a paid scoping session);
  - you cannot get even 3 conversations, in which case the *channel* failed and demand stays untested.

  That commitment is the decisive evidence we lack, and only a test can produce it.

---

## 2. What the agent market actually consists of today

An **AI agent** is software in which a language model decides, step by step, which tools to use until a goal is met. A **workflow** is different: a programmer fixes the steps in advance, possibly with an AI step inside. Most commercial "agents" sit between the two (paper §1).

What people and companies actually spend money on today, from firmest to weakest evidence:

1. **Model providers and coding agents.** This is where the money demonstrably is.
   - Anthropic said its run-rate revenue "crossed $47 billion" in May 2026 (Fact, company statement, re-read on 12 Oct [S088]). Run-rate is a revenue pace, not audited revenue.
   - Claude Code alone passed a $2.5bn run rate in February 2026 [S141].
   - Among developers who use AI, 66% use coding agents [S062].
2. **Enterprise suites adding agents.** For example, Salesforce reported Agentforce above $1.5bn of annual recurring revenue, under a broadened definition [S055].
3. **Services that fill the skills gap.** On Upwork, gross services volume (GSV, the total value of work bought through the platform) for AI-related work rose more than 22% year on year in Q2 2026, while total GSV fell 4%. "AI strategy and consulting" grew over 50% (Fact, SEC filing [S127]). The investor presentation puts AI-related work at about $330M a year; that figure was read only as a search extract.
4. **Analyst forecasts.** These are weak evidence, because definitions differ about thirtyfold.
   - Gartner puts 2026 spending on "AI agents and assistants" at $29.2bn [S082][S136].
   - Gartner's "agentic AI software spend" reaches $985bn by 2030, a far broader category [S083].
   - Both figures are real, but neither tells you what a small operator can sell.
5. **Agents buying things on their own.** This is very small.
   - On the main machine-payment rail (x402), Visa counts about **$15.0M in total from May 2025 to April 2026** after removing test and wash activity [S091].
   - An independent analysis of a related measure (TRM's $25.6M of screened x402 commerce) finds only **0.6–7.5%** looks like real agent commerce, about **$5,000–11,000 a month worldwide** [S090].
   - OpenAI scaled back in-chat checkout in March 2026 [S025] and shut down its Atlas browser on 9 August 2026 [S138][S135].

**What is operationally real (Interpretation).**
- Coding agents.
- Customer-support agents with human escalation.
- Narrow internal automations.
- The plumbing that connects them: MCP for tools, A2A for agent-to-agent communication.

**What is still speculative.**
- Agents shopping and paying at scale.
- "Optimising your products so agents pick them".
- A trillion-dollar agentic market by 2030.

The binding constraints are **reliability and security**, not capability demos:
- The best agent matched a professional on real freelance projects only 15.8% of the time [S037].
- Prompt injection, meaning hostile instructions hidden in content an agent reads, is described by OpenAI as unlikely ever to be fully solved [S118].
- In KPMG's survey of large US companies, 80% named cybersecurity as the top obstacle to their AI goals [S131].

## 3. Where customers demonstrably pay, and where evidence is weak

| Claim | Evidence | Strength |
|---|---|---|
| Companies pay for coding agents | Company revenue disclosures [S088]; usage surveys [S062] | **Strong** |
| Small businesses pay freelancers for AI work | Upwork SEC filing: AI-related work +22% YoY [S127] | **Strong for the category**; says nothing about *your* offer |
| Teams pay for coding-agent training | Published prices: a 2-day Claude Code course at €890 per person from an Anthropic partner [S128]; mentor workshops from $250–900 [S129] | **Moderate** (list prices, not volumes) |
| Companies pay for AI/LLM security assessments | Published price guide: $6k–45k+; specialists $16k–50k; 5–25 days [S130] | **Moderate** (a vendor with a selling interest) |
| Service leaders are under pressure to deploy AI | Gartner: 91% of 321 leaders [S133] | Pressure, **not** spending on independent evaluation |
| Companies pay independent firms to evaluate support agents | Not found. Substitutes exist: Zendesk QA at about $35 per agent per month [S134], plus vendor dashboards | **Weak** |
| Agents buy products autonomously at meaningful scale | About $5–11k a month of agentic x402 commerce [S090] | **Very weak** |

**The weakest assumption in this whole package** is that *a newcomer without a track record* can win these customers. Category demand is real. Nothing yet shows that buyers will choose an unknown individual over:
- the vendor's own free material;
- a partner consultancy;
- a cheaper freelancer.

That is exactly what the first test must measure.

## 4. The routes compared

We rebuilt the shortlist from scratch instead of keeping the earlier ranking (v1.1 had security reviews first).

**The scoring rubric.** Each route gets a judgement of 1–5 on eight criteria:
- evidence (20%);
- pain (15%);
- willingness to pay (15%);
- buyer access (10%);
- feasibility (10%);
- cost (10%);
- competition (10%);
- risk (10%).

The weighted score is out of 100. **Treat these scores as ordinal. Differences under about 5 points mean nothing.**

In v1.2 the decision instead uses an **entry gate**. It adds what a scoring sheet hides: the credentials and customer access a newcomer needs, the liability, and the time to first revenue.

| | **R1 Agent risk review** (limited assessment) | **R2 Coding-agent enablement + measured pilot** | **R3 Support-agent evaluation** | **R4 Small AI workflow automations** (simpler adjacent) | **R5 Defer / learn first** |
|---|---|---|---|---|---|
| Who pays / decides | CTO or founder of a small company deploying agents | Engineering manager or CTO of a 5–30 person software team | Head of customer support; CFO signs off | Small business owner posting a job | — |
| Problem they have | "Is our agent safe to connect to email, data and tools?" | "We pay for coding agents; are we using them well, and is it working?" | "Is the bot really resolving tickets? Should we pay per resolution?" | "Automate this repetitive task for me" | — |
| Their current workaround | Free checklists (OWASP); a full pentest firm; doing nothing | Vendor docs; self-teaching; partner courses | Vendor dashboards; QA tools at ~$35/agent/month | Doing it by hand; Zapier/Make templates | — |
| Paid-demand evidence | Moderate (audit market exists [S130]) | Moderate (training prices [S128][S129]) | Weak | **Strong** for the category [S127] | — |
| Price per engagement (Assumption, newcomer base) | €2,500 | €3,000 | €3,500 + €1,200/month retainer | €600 | €0 income |
| Credentials needed | **Security competence**; insurance advisable | Professional coding experience | Data/analytics plus support-operations knowledge | Practical automation skill | — |
| Liability | **High** | Low–medium | Medium (you process customer personal data under GDPR) | Low–medium | None |
| Months to first sale (Assumption, newcomer base) | 6 | 6 | 8 | 3 | — |
| Take-home once sales are steady, newcomer base (Calculation) | €783/month for ~43 h | €832/month for ~42 h | €1,379/month for ~50 h | €470/month for ~31 h | €360–1,440 cash spent over 3 months; no income |
| **First-year take-home per owner hour: newcomer / with network** (Calculation) | **€7.2 / €36.3** | **€11.2 / €27.6** | **€3.2 / €23.4** | **€9.9 / €23.2** | — |
| First year, adverse case, newcomer (Calculation) | loss (−€6.4/h) | loss (−€2.8/h) | loss (−€9.6/h) | loss (−€1.3/h) | — |
| Entry gate (Interpretation) | **Shortlist only if you have security background** | **Shortlist, recommended first if you code** | **Defer** | **Shortlist as paid practice if you don't code (or learn first)** | Valid choice |

*How to read the money rows.* They come from `models/route_economics.py`.
- **Take-home** means after costs, Latvian self-employed social contributions and income tax, under simplified 2026 rules. It is not revenue minus fees.
- **"First year"** includes setup and the months with no sales.
- **The two cases:**
  - *newcomer* means no track record and no warm contacts;
  - *with network* means you can reach buyers through people who know you, or you have strong public proof.
- **Adverse** combines six shocks at once: half the sales, prices 30% lower, double rework, double selling effort, a 3-month-longer ramp and +5 points of marketplace fee.
- **Benchmark:** Latvian professionals averaged €13.04 per hour gross in 2022 [S126], about **€8.7 per hour net** after employee contributions and income tax [S100] (Calculation).
- **Reading.** For a newcomer, the first year pays around that net benchmark at best (R2, R4) and below it for R1 and R3. The adverse first year is a loss of time and some cash. With warm access, every route clearly beats it. Full tables are in `04-economics.md`.

**Rejected for now.**
- **Products bought autonomously by agents** (pay-per-call APIs, "agent-optimised" catalogues). Measured agent spending is tiny [S090].
- **Holding or forwarding clients' money for agent purchases.** It is a regulated payment service [S114].

## 5. Why R2 leads, and why the others do not (yet)

**R2, coding-agent enablement with measurement (Interpretation).** This is the only route where all four of these hold at once:
- buyers already spend on the tool category [S088][S062];
- paid training already has public prices [S128][S129];
- the outcome is genuinely uncertain, so measuring it is valuable: controlled studies of developer speed-ups are inconclusive, and developers over-estimate their gains [S070];
- liability is modest.

The offer is a short, practical engagement:
1. Set up the coding agent safely on the team's real repository: permissions, sandboxing, secrets, review rules.
2. Run a 2-day hands-on workshop.
3. Measure a 4-week pilot against a baseline: cycle time, review load, defect escapes, cost per merged change.
4. Hand over a written report.

**The main refusal reason** is "the vendor and its partners already teach this, and our developers can learn it themselves". Two more weaknesses:
- *measurement* is the least proven part. On a 5–12-developer team over 4 weeks it gives adoption and cost telemetry, not a statistically solid productivity verdict;
- buyer access is what a newcomer most likely lacks.

So the test quotes **two priced options**, setup + workshop alone and with measurement, and records which one buyers choose. It should also run mainly through warm and referred contacts.

**R4, small workflow automations.** This is the most reliable way to earn *something* quickly. A marketplace supplies buyers, and the evidence that people pay is the strongest we found [S127]. The drawbacks:
- the price is low;
- global competition is intense;
- the marketplace controls your ranking and your account.

It has the shortest path to a first payment: about 3 months to a first win in the base case. However, at newcomer prices (€600 a job) it pays **about €15 per hour once steady and about €10 per hour in the first year**. Treat it as **paid practice that produces client stories**, not as a business. If you are not a developer, it competes closely with option 3, learning first. Before choosing it, pass the self-check in plan V4: three working demos in 20 hours.

**R1, limited agent risk review.** Demand logic is strong: security is the top adoption barrier [S131]. However:
- **A limited assessment is not a professional audit.** A limited assessment is a structured review of how an agent is configured: its permissions, the "lethal trifecta" (private data + untrusted input + a way to send data out) [S011], approval steps and logging, mapped to public checklists. It ends in a written findings list.
- A **professional security audit or penetration test** involves authorised technical testing, specialist competence and usually insurance, and costs $16k–50k from specialists [S130].
- A **certification** (e.g., ISO/IEC 42001 or SOC 2) can only be issued by accredited bodies.

Without security credentials, a newcomer's review is easy to refuse and carries real liability if something is missed. **Pursue R1 only if you already have security experience**, and always with contract language limiting scope and liability.

**R3, independent support-agent evaluation, is deferred.** It has the highest value per client in our model, because a retainer can follow the audit. But it has:
- the longest sale: 6 months to a first win in the base case;
- the hardest access: you need the client's conversation data, which makes you a GDPR processor [S110];
- cheap substitutes [S134].

It suits someone who already has support-operations clients. Revisit it once R2 or R4 has produced relationships.

## 6. What it would actually involve: one illustrative engagement per route

These are **illustrative**: no real customer, sale or interview exists.

- **R2.** A 12-developer software agency in Germany already pays for a coding agent but sees uneven use.
  - Week 1: a 1-hour call; you read their contribution data and set a baseline; you write a safe-configuration policy.
  - Week 2: a 2-day remote workshop on their own codebase.
  - Weeks 3–6: they work as usual while you collect the agreed metrics weekly.
  - Week 7: a 10-page report and a 1-hour readout.
  - Price €3,000 (newcomer) to €4,000 (with a track record), invoiced as a B2B service under reverse charge. About 31 hours of your time, plus selling time.
- **R4.** A non-EU accounting firm posts a job: "auto-file client emails and draft replies".
  - You build a flow: classify the email, extract fields, draft a reply, and wait for human approval before sending. You document running costs and hand it over in two weeks.
  - €600–1,000, minus a marketplace fee (Upwork's is variable, 0–15%, plus paid bid credits [S140]). About 13–16 hours including revisions.
- **R1.** A 20-person startup is connecting an agent to its inbox and CRM.
  - You review its configuration and data flows against the OWASP Agentic Top 10 and the trifecta rule, and interview the developer.
  - You deliver 12 prioritised findings, explicitly *not* a penetration test.
  - €2,500. About 24 hours.

Full versions are in the dossiers (`03-dossiers/`).

## 7. The recommended first move, by your situation

| If your situation is… | First move | Why |
|---|---|---|
| You code professionally **and** know 10+ software team leads you could approach | **Explore R2** (validation plan V2) | Strongest fit between real spending, price evidence and your access. First-year pay with warm access ≈ €28/h (Calculation) |
| You code professionally, no network | Explore R2 *alongside* a check of your contracting rate: build the **public proof** first, then use community, referral and marketplace channels, not cold email | Without access, R2's first year (≈ €11/h) probably pays less than contracting. Test it for option value, and keep contracting as the benchmark |
| You do not code, but can use automation tools | **R4 as paid practice** (plan V4), **or learn first** (option 3) | Marketplace supplies buyers, but newcomer pay is low (≈ €10/h in the first year) |
| You have security experience (e.g., appsec, pentesting) | Explore **R1** (plan V1) alongside R2 | Credentials remove the main objection |
| You run or know support operations | Keep R3 as the **second** test (plan V3) | Access is the bottleneck you'd already have solved |
| Under 5 hours a week, or no appetite for selling | **Learn first (R5)** or **defer** | Every route needs 40+ hours of selling before revenue |

**Time and money you would need to commit to the test (Assumption).**
- **Time:** 50–60 owner-hours across 8–10 weeks. The proof case alone needs a 4-week baseline plus 4 weeks of use.
- **Cash:** up to €150, for a domain and email, small API credits and an automation-tool month.
- **Registration:** none until a client agrees to pay.
- **Before the first invoice:** register with the State Revenue Service as self-employed, or open an individual merchant (IK), €30 [S102]. Then choose a tax regime (§8).

## 8. The Latvian operating facts that matter for this decision

Corrected in v1.2 from the **current Latvian legal text** and the tax authority's guidance.
- **Buying foreign AI tools does not force VAT registration.**
  - Since 1 July 2025, a small operator can use a **special VAT registration** just for buying foreign services (VAT Law s.139²) and stay under the €50,000 threshold [S122].
  - The cost is that 21% VAT on those purchases cannot be reclaimed. At €150 a month of tools that is about €32 a month (Calculation).
  - A notice is due by the 20th of the following month for each month with foreign purchases, and payment within 23 days.
  - The earlier v1.1 statement that this blocked the micro-enterprise tax was **wrong** and has been withdrawn.
- **Selling to a VAT-registered business in another EU country does force full VAT registration, from the first such sale** (s.59(8)) [S122]. You then invoice under reverse charge (no Latvian VAT) and file EU sales statements. It also ends eligibility for the **micro-enterprise tax**, from the next tax year [S124].
  - **Practical effect:** if your first clients are outside the EU, admin stays minimal.
  - If your first client is, say, a German company, register first.
- **Micro-enterprise tax** is 25% of *turnover*, with no deduction for costs [S123]. Self-employed social contributions are 31.07% on income from €780 a month, and personal income tax is 25.5% [S125].
  - **Comparison with the self-employed regime (Calculation).** The modelled client mixes include EU business clients, which rules the micro-enterprise tax out.
    - If the same revenue came only from non-EU or Latvian clients, it would give about the same or *less* take-home: from €161 a month less (R4) to €5 a month more (R3). This counts the non-reclaimable VAT on foreign tools.
    - It is simpler to administer, but at low incomes the self-employed regime is cheaper. Below €780 a month, self-employed people pay only a 10% pension contribution [S125].
    - It is available only while you have no EU VAT-registered clients and stay under €50,000 a year. Once that condition is broken, it is lost from the next tax year [S124].
  - A **limited company (SIA)** costs €75 to register [S102] and pays 20% company tax only when profits are distributed [S100]. It limits liability, which matters most for R1.
- **Questions that remain for an adviser, and when they matter:**
  - (a) Which regime to use for your actual client mix. *Blocks the first invoice, not the test.*
  - (b) Whether an SIA is needed for liability. *Matters before any R1 sale; does not block R2 or R4 testing.*
  - (c) Contract liability caps and insurance. *Before scaling R1.*

## 9. What could reverse this recommendation

- **Against R2:**
  - Engineering leads say coding-agent enablement is "solved" by the vendor, with fewer than 2 of 10 interested in paying for measurement.
  - Or vendors launch free, built-in team analytics that answer "is it working?"
  - Then switch to R4 or defer.
- **Against the whole services thesis:** our sources over-represent large US companies (KPMG n=130 [S131]; Gartner and McKinsey executive panels). Smaller and European firms may adopt far more slowly. Eurostat found only 20% of EU enterprises used *any* AI in 2025, and 12.2% in Latvia [S096].
- **For a product (later):** published evidence that agents are buying services at scale, for example card networks reporting real agent-initiated volumes. Then reconsider products sold to agents.
- **Economics:** if you cannot reach buyers warmly, the newcomer case applies. A first year near or below ordinary net pay means the route is worse than a job, unless the test shows prices or win rates above the newcomer assumptions.
- **Your alternative:** if your own contracting or employment rate is well above about €25 per hour net, none of these routes beats it in year one, even with a network (Interpretation from the model). Then explore only part-time, or not at all.

## 10. Decision menu

| Choice | What you'd do next (all steps needing approval are listed in `05-validation-plans.md`) | Commits you to | Implications |
|---|---|---|---|
| **1. Explore the recommended route (R2)** | Approve plan V2: build the public proof case on your own repository (no approval needed). Then approve contact with up to 25 engineering leads, through warm introductions, referrals and personal messages on professional networks. No unsolicited bulk email | ~60 hours over 8–10 weeks; ≤€150; no registration until a client pays | Fastest route to *decisive* evidence on the most promising route. Requires professional coding skill. Contacting people is visible, and reversible only socially |
| **2. Explore an alternative (R4, or R1 if you have security experience)** | Approve plan V4 (open a marketplace account, send up to 25 proposals) or V1 | ~50–60 hours; ≤€150. R4 means accepting the marketplace's terms, its variable fee and its control over your account | R4 gives earlier money and client stories at low pay. R1 pays better per engagement but carries high liability without credentials |
| **3. Learn or build capability first (R5)** | 3 months of structured practice: build and measure agents on your own data; publish nothing until you choose to | 120–300 hours; €360–1,440 cash (Assumption) | No market evidence gained. Re-take this decision with a portfolio. Choose this if the self-check in V2/V4 fails |
| **4. Defer entry** | Re-check the triggers in §9 quarterly (a calendar reminder at most) | Nothing | Zero cost. You lose ~6 months of learning in a fast market; the evidence above may be stale by then |

Not on the menu, but your real benchmark: **employment or contracting**, possibly with "coding-agent setup" as a selling point. If your best available rate is high, choosing 3 or 4 here and contracting instead is a rational answer.

**The single decision needed from you:** choose 1, 2, 3 or 4. If you choose 1 or 2, also say whether the drafted outreach (V2 or V4) may be sent as written, edited, or not at all. Nothing will be sent, bought or opened without that answer.
