# Dossier R4: Small AI workflow automations for small businesses (simpler adjacent service)

*First route **if you are not a professional developer**, or a paid warm-up before R2/R1. Register ID O13 (new in v1.2). Version 1.2, 12 October 2026. About 8 minutes to read.*

## 1. In one paragraph

You build small, fixed-scope automations with one AI step inside, such as triaging email and drafting replies, extracting invoice data, summarising calls into a CRM, or producing weekly reports. You sell them through a freelance marketplace where buyers already post such jobs.

It is "simpler" for three reasons:
- it is a **workflow**, with steps fixed in advance, not an autonomous agent;
- a human approves anything that leaves the business;
- the marketplace supplies the buyers.

It is the route with the **strongest evidence that people pay**. It is also the most crowded and the lowest-priced.

## 2. Who pays and who decides

The owner or operations lead of a small business, or a solo professional, posting a job. The person who pays also decides. Buyer type: **human**.

## 3. The problem and today's workaround

**The problem.** Repetitive admin consumes owner time. Off-the-shelf "AI features" don't fit the specific tools the business uses.

**Workarounds:**
- doing the work by hand;
- DIY with no-code templates (Zapier, Make, n8n);
- a generalist virtual assistant;
- built-in AI features of email and CRM vendors.

## 4. Evidence versus hypotheses

| Statement | Status |
|---|---|
| Buyers pay for AI-related freelance work, and the category is growing | **Fact.** Upwork Q2 2026: AI-related gross services volume +22% YoY while total GSV fell 4%; AI strategy and consulting +50% (SEC filing [S127]) |
| Size of that demand | About $330M a year of AI-related GSV on Upwork (investor presentation, read via search extract [S127]); **medium confidence** |
| A newcomer wins jobs at €500–2,000 | **Hypothesis**: cold start without reviews is the main risk |
| Fixed-scope automations stay within your delivery estimate | **Hypothesis**: scope creep is common (Interpretation) |

## 5. What you would sell and deliver

**Offer: "One automation, done properly".** Assumed €600 net as a newcomer, €1,000 with reviews. Marketplace fee assumed 10%; Upwork's actual fee is variable, 0–15%, plus bid credits [S140].
1. A 30-minute scoping call. Write down the inputs, outputs, error cases and the human-approval point.
2. Build the automation on the client's own accounts, with **least-privilege access**. The client grants it and can revoke it.
3. Test on 20 real examples. Report the error rate and the cost per run (model cost is usually cents; see paper §6.4).
4. Hand over a one-page runbook, a 30-day fix window and an optional care plan (€100–150/month, assumed).

**Hours, base case:** 12 hours of delivery + 30% rework ≈ 16 hours, plus about 6 hours of proposals per won job.

**Do not sell:**
- fully autonomous sending or paying;
- access to anything you cannot revoke;
- automations that move money: that is regulated, see paper §15.7.

## 6. Skills, credibility, tools and access

- **Skills:** comfort with one automation platform and with API keys; prompt design with test cases; clear written communication. Coding helps but isn't required.
- **Credibility:** 2–3 public demo automations, with a short video or write-up each. Then marketplace reviews, which are the real currency.
- **Tools:** an automation platform (a free tier or ~€20–50/month), model API credits (a few euros for demos) and a marketplace account. **Opening the account needs your approval.**
- **Self-check before choosing this route (no approval needed).** Build the 3 demo automations in **20 hours or less**, each with an error rate of **10% or less** on 20 test items. "Not a coder" still means handling API keys, OAuth logins and JSON. If you cannot pass, choose option 3 (learn first).
- **Other channels:** the automation platforms' own expert and partner directories (Zapier, Make, n8n). Their listing requirements are not checked here.
- **Access:** the marketplace supplies buyers. Your profile ranking depends on the platform's algorithm (platform risk).

## 7. Setup, workload and unit economics (Calculation, `models/route_economics.py`)

<!-- econ:start -->
*Cases: **low** = adverse inputs; **base** = a newcomer without track record or warm contacts; **high** = with a network or strong public proof. Benchmark: about €8.69/h net for an average Latvian professional [S126][S100]; your own contracting rate is the real comparator.*

| | Low | Base (newcomer) | High (with network) |
|---|---|---|---|
| Price per engagement (net of VAT) — assumption | €400 + €100/month retainer (20% of clients) | €600 + €100/month retainer (25% of clients) | €1,000 + €150/month retainer (30% of clients) |
| Engagements won per month once steady | 0.5 | 1 | 2.5 |
| Months before first sale | 4 | 3 | 2 |
| Selling hours per *won* engagement | 12 h | 10 h | 6 h |
| Delivery hours per engagement incl. rework | 20 h | 13 h | 16 h |
| One-time setup: cash / owner hours | €150 / 40 h | €150 / 30 h | €150 / 25 h |
| Monthly fixed cash costs | €90 | €110 | €140 |
| Revenue per month once steady (net of VAT) | €260 | €750 | €3,400 |
| Operating profit per month once steady | €110 | €522 | €2,802 |
| Owner hours per month once steady | 23 h | 31 h | 69 h |
| **Self-employed take-home per month once steady** | €99 | €470 | €1,897 |
| Take-home per owner hour once steady | €4.4 | €15.0 | €27.5 |
| First 12 months: operating cash before income tax | €254 | €3,896 | €24,818 |
| First 12 months: owner hours | 267 h | 354 h | 726 h |
| **First 12 months: take-home per owner hour** | €0.9 | €9.9 | €23.2 |
| First 12 months under the combined adverse case | −€4.4 (loss) | −€1.3 (loss) | €7.8 |

Setup and fixed-cost contents (assumption): setup €150 = automation-platform month and API credits for demos; fixed = automation platform, API, bookkeeping.
<!-- econ:end -->

## 8. Competition, substitutes and refusal reasons

- **Competition:** a very large global freelancer pool, much of it in lower-cost countries, so prices are under pressure. Agencies run productised packages.
- **Substitutes:** no-code templates; vendors' built-in AI (e.g., email clients drafting replies).
- **Why a buyer refuses:** no reviews yet; a cheaper bid; worries about access to their accounts; the job turns out simpler than expected and they do it themselves.

## 9. Global distribution and acquisition barriers

- The marketplace solves *finding* buyers but controls ranking, fees and account standing (platform risk).
- Time zones matter little for asynchronous work.
- Language: English is fine for most jobs. Latvian or Russian may be a niche advantage locally, but the brief deprioritises Latvian demand.

## 10. EU and Latvian operating implications

**Client mix is decisive for VAT** [S122][S124]:

| Clients | Consequence |
|---|---|
| Non-EU only (plus Latvian clients under €50k a year) | Outside Latvian VAT for non-EU clients. Micro-enterprise tax possible. The s.139² special registration covers buying foreign tools: 21% non-reclaimable |
| Any VAT-registered business in another EU country | Full VAT registration before that sale; reverse-charge invoice; EU sales statement; micro-enterprise tax lost |

**Marketplace invoices.** How the marketplace documents the supply (whether you invoice the client or the platform) affects VAT. **Exact question for an adviser:** "for marketplace X's invoicing model, who is my customer for VAT purposes?" It **blocks the first paid job, not the test.**

**Other obligations:**
- **GDPR:** automations touching customer emails make you a processor during the build. Use a short data-processing clause and do not keep the data [S110].
- **AI Act:** if the automation sends AI-drafted text directly to the public, disclosure rules may apply from 2 August 2026 [S074]. Keep a human approval step.

## 11. What would invalidate this route

- After 25 tailored proposals over 6 weeks, fewer than 2 paid jobs.
- Effective pay on delivered jobs under about €13 per hour, the Latvian professional average.
- The platform's terms or fees change so that the economics fail. Check the current fee before relying on the 10% assumption.

## 12. Cheapest credible first test

See **plan V4** in `05-validation-plans.md`.
- **Phase A (no approval needed):** build 3 demo automations on your own data.
- **Phase B (needs approval):** open a marketplace profile and send up to 25 proposals.
- **Caps:** ≤50 hours and ≤€100.

## 13. Illustrative engagement (not a real customer)

> **Illustrative.** A 6-person accounting firm in Canada posts: "We get ~80 client emails a day; sort them and draft replies."
>
> - **Build.** You build:
>   - a classifier into 6 categories;
>   - field extraction (client name, deadline, document type);
>   - a drafted reply for 3 routine categories, placed in a "drafts" folder for a human to send.
> - **Test and hand over.** You test on 20 past emails, report the misclassification rate, and estimate the model cost per email.
> - **Commercials.** €600 fixed (newcomer price). Two revision rounds. A €150/month care plan offered. The client is outside the EU, so the supply is outside Latvian VAT, and with no EU business clients the micro-enterprise tax remains possible.
>
> *No error rate or cost figure is shown because none has been measured.*
