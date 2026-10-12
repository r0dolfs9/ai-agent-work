# Dossier R3: Independent evaluation and outcome audit of customer-support agents

*Status: **defer**. It is the second test once you have support-operations contacts. Register ID O02. Version 1.2, 12 October 2026. About 8 minutes to read.*

## 1. In one paragraph

Companies deploying AI support agents often pay per "resolution" (for example, Intercom's per-outcome pricing [S071]). They rely on the vendor's own count of what was resolved. You would sell an independent check:
1. sample the conversations;
2. label them against a clear definition of "resolved";
3. find where the bot fails or hands off badly;
4. estimate what that costs.

A monthly retainer would follow. It has the highest value per client of the four routes and the hardest entry.

## 2. Who pays and who decides

- **Who pays and decides:** the head of customer support or CX operations, with finance signing off when per-resolution bills are large.
- **Who blocks it:** the vendor's account team (they own the dashboard); IT and privacy (data export).
- Buyer type: **human organisation**.

## 3. The problem and today's workaround

**The problem.**
- In our cost model, the share of conversations the agent truly resolves is the biggest lever on total cost. Moving it from 70% to 20% cuts the saving against an all-human team from 52% to 3% (Calculation, paper §6).
- Automated judges over-rate quality [S037].
- Vendors billed per resolution have an incentive to count generously (Interpretation).

**Workarounds:**
- vendor dashboards;
- internal QA teams sampling tickets;
- QA software, e.g. Zendesk QA at about $35 per agent per month (secondary, low confidence [S134]).

## 4. Evidence versus hypotheses

| Statement | Status |
|---|---|
| Service leaders are under pressure to deploy AI | **Fact.** Gartner: 91% of 321 leaders (search extract [S133]) |
| Per-outcome pricing exists | **Fact** [S071] |
| Buyers pay *independent* firms to verify resolution claims | **Not found.** Hypothesis |
| QA tools are a cheaper substitute | **Fact (secondary prices)** [S134] |

## 5. What you would sell and deliver

**Audit: base €3,500, about 36 hours including rework.**
- An export of 500–2,000 conversations, pseudonymised by the client.
- A labelling rubric.
- A double-labelled sample.
- Failure taxonomy and cost estimate.
- Readout.

**Retainer: base €1,200/month, about 12 hours a month.** Monthly sample, trend and vendor-claim reconciliation.

## 6. Skills, credibility, tools and access

- **Skills:** support operations, sampling and statistics, evaluation design, LLM-assisted labelling with human checks.
- **Credibility:** a support-operations background matters more than AI skill.
- **Access:** you need the client's conversation data, which makes you a **GDPR processor**. Required: an Article 28 data-processing agreement, a transfer assessment if a US model is used, and a retention limit [S110][S109].
- **Tools:** an evaluation harness, LLM-judge API credits and a secure storage practice.

## 7. Setup, workload and unit economics (Calculation, `models/route_economics.py`)

<!-- econ:start -->
*Cases: **low** = adverse inputs; **base** = a newcomer without track record or warm contacts; **high** = with a network or strong public proof. Benchmark: about €8.69/h net for an average Latvian professional [S126][S100]; your own contracting rate is the real comparator.*

| | Low | Base (newcomer) | High (with network) |
|---|---|---|---|
| Price per engagement (net of VAT) — assumption | €2,000 + €800/month retainer (30% of clients) | €3,500 + €1,200/month retainer (40% of clients) | €5,000 + €1,800/month retainer (50% of clients) |
| Engagements won per month once steady | 0.15 | 0.33 | 0.5 |
| Months before first sale | 10 | 8 | 6 |
| Selling hours per *won* engagement | 80 h | 60 h | 45 h |
| Delivery hours per engagement incl. rework | 52 h | 36 h | 29 h |
| One-time setup: cash / owner hours | €900 / 100 h | €900 / 80 h | €900 / 60 h |
| Monthly fixed cash costs | €240 | €280 | €340 |
| Revenue per month once steady (net of VAT) | €516 | €2,422 | €7,000 |
| Operating profit per month once steady | €235 | €2,030 | €6,445 |
| Owner hours per month once steady | 30 h | 50 h | 68 h |
| **Self-employed take-home per month once steady** | €212 | €1,379 | €4,339 |
| Take-home per owner hour once steady | €7.2 | €27.4 | €64.0 |
| First 12 months: operating cash before income tax | −€3,137 | €1,599 | €18,531 |
| First 12 months: owner hours | 333 h | 453 h | 540 h |
| **First 12 months: take-home per owner hour** | −€9.4 (loss) | €3.2 | €23.4 |
| First 12 months under the combined adverse case | −€12.0 (loss) | −€9.6 (loss) | −€3.7 (loss) |

Setup and fixed-cost contents (assumption): setup €900 = evaluation harness and LLM-judge API credits (€300), DPA/contract template review (€300), domain/site (€100), insurance quote (€200); fixed = bookkeeping, eval tooling, API.
<!-- econ:end -->

## 8. Competition, substitutes and refusal reasons

- **Competition and substitutes:** vendor analytics; QA platforms; CX consultancies.
- **Why a buyer refuses:**
  - "Our vendor already reports this";
  - "We can't export customer conversations";
  - "Our QA team does sampling".

## 9. Global distribution and acquisition barriers

- **Strongest market:** high-wage countries with large support teams, where each percentage point of true resolution is worth the most [S119].
- **Barriers:** procurement; the data-protection review; long sales cycles.

## 10. EU and Latvian implications

- **Processor duties:** these make this the most legally demanding route. Adviser question: *"Is my DPA template adequate for processing support transcripts, including a US model sub-processor?"* It **blocks the first sale.**
- **VAT:** the same client-mix rule as other routes (s.59(8)) [S122].
- **AI Act:** none for the evaluator directly.

## 11. What would invalidate this route

- Buyers consistently refuse to export conversations.
- Vendors add independent-grade verification.
- Fewer than 2 of 10 support leaders agree that per-resolution billing needs independent checking.

## 12. Cheapest credible first test

See **plan V3**.
- **Phase A (no approval needed):** build an evaluation method on a public customer-support dataset and publish nothing until approved.
- **Phase B (needs approval):** 10 interviews with support leaders.
- **Caps:** ≤50 hours and ≤€100.

## 13. Illustrative engagement (not a real customer)

> **Illustrative.** A UK software company with 25 support staff pays its bot vendor per resolution and receives a monthly bill it cannot verify.
>
> - **Audit.** You audit a pseudonymised sample of 1,000 conversations against a definition of "resolved", agreed with the client in writing. Example: no repeat contact within 7 days, and the customer's question was answered.
> - **Report.** It shows the gap between the vendor's count and the audited count, the main failure types, and the cost implication.
> - **Commercials.** €3,500, then a €1,200/month retainer. The client is in the UK (non-EU), so the supply is outside Latvian VAT. The UK's own rules apply to the customer.
>
> *No gap figure is shown because none has been observed.*
