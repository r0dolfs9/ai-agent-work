# Prepared validation plans (not executed)

*Version 1.2 · 12 October 2026 · 20 minutes to read; the draft materials are for editing, not reading straight through.*

**Status:** these are **prepared plans**. Nothing has been sent, posted, opened or bought.

Each plan has two phases:
- **Phase A** is private preparation that needs no approval.
- **Phase B** involves contacting people, opening accounts or spending money, and **requires your explicit approval of each listed action.**

## Rules common to all plans

- **Honesty.**
  - Always say who you are and that you are exploring a service.
  - Never pose as a customer, never claim clients or results you don't have, and never imply partnership with a vendor.
- **Contact data.**
  - Contact people only at work addresses, or through a platform's messaging, in their professional role.
  - Keep a simple list: name, company, date, response.
  - Include a one-line opt-out, honour it, and delete the list when the test ends.
- **Unsolicited sales email is restricted. This is a blocking rule.**
  - **Germany:** advertising email without prior, provable consent counts as unreasonable nuisance under UWG §7(2), and that applies to businesses too [S139].
  - **Other EU countries:** they implement the ePrivacy rules differently.
  - **Therefore:**
    - send **no** unsolicited sales email to German recipients;
    - for any other country, send none until its rule is checked;
    - use warm introductions, referrals, replies to people who asked publicly, community posts, marketplace proposals (the buyer invited them), and personal one-to-one messages on professional networks within that platform's rules.
  - **Exact adviser question:** *"Is a one-to-one, personalised B2B email from a Latvian sender to a business in [country] lawful under that country's ePrivacy implementation and Latvian rules?"* It **blocks cold email to that country**; it does not block the other channels.
- **Money.** The listed caps are maxima. A cap is not a budget to be spent.
- **Stop rule.** Stop when either the time cap or the calendar cap is hit, even if results are inconclusive.
- **Recording.** Log every contact and outcome in `validation-log.csv`: date, plan, contact type, response, stated price or objection. That log is the evidence. Opinions without commitments count as *inconclusive*.
- **What counts as a commitment (strong signals only):**
  - (a) a paid engagement;
  - (b) a signed order with a start date and a 20–30% deposit;
  - (c) a **paid** scoping session (€300–500).

  A letter of intent is usually non-binding, so record it as *interest*, not a commitment. "Sounds interesting" is not a commitment.

---

## V2: Coding-agent enablement with measured pilot (recommended first if you code)

| Item | Plan |
|---|---|
| **Hypothesis** | Engineering leads at 5–30-developer companies will commit ≥€1,500 to a fixed-scope "safe setup + workshop" from an individual with one public measured case. **Sub-hypothesis:** a meaningful share will pay extra for the measured pilot |
| **Target customer** | CTO, head of engineering or founder at software agencies and product start-ups with 5–30 developers, in high-wage markets (DE, Nordics, NL, UK, US) or anywhere in your network. Signals: job ads or blog posts mentioning coding agents |
| **Offer tested** | Two priced options, always quoted together: **A** setup + 2-day workshop at €2,000–2,500; **B** A + 4-week measured pilot at €3,000 (first 2 clients may get B at the A price in exchange for an anonymised case study). Record which option each buyer picks |
| **Evidence to collect** | Contacts made, **by channel**; response rate; qualified calls; stated current practice; top objection; A vs B choice; price reaction; commitments; your own hours |
| **Time cap** | 60 owner-hours over **10 weeks**. Phase A ≤35 h, including a proof pilot of about 5 weeks that mostly runs in the background; Phase B ≤25 h, starting in about week 3 once the baseline and the first 2 weeks are written up |
| **Spend cap** | €150: a coding-agent subscription for one month if you don't have one, plus a domain and email if you want a professional address |
| **Success** | ≥2 commitments (strong signals, as defined above) at ≥€1,500, **or** ≥1 at ≥€2,500 plus ≥3 qualified "call me when you have a slot" |
| **Failure (demand)** | 0 commitments after ≥8 qualified conversations |
| **Failure (channel), demand untested** | <3 qualified conversations from 25 contacts. Then the channel failed, not necessarily the offer. Decide whether you have any warm route; if not, R2 is not feasible for you now |
| **Inconclusive** | Interest but no commitment; or 3–7 conversations by the time cap |
| **After success** | Register as self-employed or as an individual merchant (IK) before invoicing. If any client is an EU VAT-registered business, do full VAT registration first (s.59(8)) [S122]. Deliver; measure your own hours against the model; update `route_economics.py` |
| **After failure** | Record the top 3 objections. If buyers choose only option A at mentor prices, measurement is not the product; consider contracting with "coding-agent setup" as a skill. If "not now", defer and re-check in 6 months |
| **After inconclusive** | One extension of 3 weeks or 15 contacts, at most, then decide |

### Phase A: no approval needed (≤35 h)

1. **Self-check** (≤4 h). Set up a coding agent with restricted permissions on a repository you control. Complete three real changes. Write down where it failed.
2. **Proof pilot** (≤20 h across about 5 weeks).
   - Choose your own active project, or an open-source repository you contribute to.
   - Take the 4-week baseline **from existing history** (no waiting needed), then run 4–5 weeks with the agent: changes merged, cycle time, reverted changes, cost.
   - Outreach may start once the baseline and the first 2 weeks are written up.
   - Write a 2–3 page method-and-results note. **Report whatever you find, including "no difference".**
3. **Materials** (≤8 h). Adapt the one-pager, the outreach message, the call script and the safe-configuration checklist below.
4. **Target list** (≤3 h). 25 named organisations, chosen from public signals. Note the public source used for each.

### Phase B: needs approval (≤25 h)

| # | Action | Approval needed because |
|---|---|---|
| B1 | Publish the proof note (personal site, LinkedIn or a developer forum) | Publishing |
| B2 | Send the outreach message to up to 25 contacts, in 3 batches of about 8, a week apart. **Only through warm introductions, referrals, community replies or personal network messages; no unsolicited email to German recipients** [S139] | Contacting people |
| B3 | Hold 30-minute calls with those who reply | Contacting people |
| B4 | Send a written two-option proposal and an order form with deposit terms to interested leads | Commercial commitment |
| B5 | Spend up to €150 on subscriptions or a domain | Spending money / opening accounts |

### Draft materials (V2)

**Outreach message (≈120 words; for warm or referred contacts and personal network messages, not bulk cold email; edit before use):**

> Subject: Is your coding agent actually paying off?
>
> Hi [Name],
>
> I'm [Your name], a software developer based in Riga. I help small engineering teams set up coding agents safely and measure whether they actually help.
>
> I recently ran a 4-week measured pilot on [project] ([link to note]). The result: [one honest sentence].
>
> Teams I talk to often pay for the tool but can't say whether cycle time or defect rates changed. I'm testing a fixed-scope offer: safe configuration and a 2-day workshop on your own codebase, optionally followed by 4 weeks of adoption and cost tracking. Metrics are team-level only, and no code leaves your systems.
>
> Would a 30-minute call to sketch what a pilot would measure for [Company] be useful? If not, just say so and I won't follow up.
>
> [Signature, contact]

**Call script (30 minutes):**
1. *(3 min)* Who I am; this is exploratory; I'm not selling today.
2. *(10 min)* How do you use coding agents now? Who uses them, and for what? What does it cost you per month? What went wrong?
3. *(5 min)* How would you know whether it's working? Have you measured anything?
4. *(5 min)* Walk through the pilot outline. What's missing? What would block it (security, data, time)?
5. *(5 min)* "Option A, setup and workshop, is €2,000–2,500. Option B adds the 4-week measured pilot for €3,000. Would either work this quarter? Which one, and who else would need to agree?"
6. *(2 min)* Next step: an order with a deposit, a paid scoping session, a follow-up date, or a "no, thanks". Record the exact words used.

**One-pager outline:** problem (2 lines with sources [S062][S070]); the offer in four steps; what you need from them (CSV export, 2 workshop days); what they get (policy, workshop, report); price; what is *not* promised (a productivity figure); about you, with a link to the proof note.

**Safe-configuration checklist (deliverable seed):**
- [ ] The agent runs in a sandbox or container with no production credentials.
- [ ] Secrets are excluded from context; secret scanning is on.
- [ ] Shell commands that touch deployment, databases or package publishing need human approval.
- [ ] No single session has private data + untrusted input + outbound send [S011].
- [ ] Agent changes go through normal code review; size limits per change.
- [ ] Cost limits per user per month; prompt caching enabled.
- [ ] Logs retained, with a retention period agreed for traces.

---

## V4: Small AI workflow automations via a marketplace (first move if you don't code)

| Item | Plan |
|---|---|
| **Hypothesis** | A newcomer with 3 public demos can win ≥2 fixed-price automation jobs at ≥€500 within 6 weeks, and deliver them at ≥€20 per owner hour |
| **Target customer** | Small businesses posting automation or AI-integration jobs on a freelance marketplace, preferably non-EU at first, which keeps VAT simple |
| **Offer tested** | "One automation, done properly": fixed price €500–1,500, a human-approval step, a runbook and 30-day fixes |
| **Evidence to collect** | Proposals sent; replies; interviews; wins; price; delivered hours (timed); rework; client rating |
| **Time cap** | 50 owner-hours over 6 weeks, excluding delivery of won jobs, which is paid |
| **Spend cap** | €100: an automation-platform month plus API credits. Marketplace bid credits (Upwork "Connects" are $0.15 each, often 10+ per proposal [S140]) **count toward this cap** |
| **Success** | ≥2 paid jobs **and** effective pay ≥€20 per owner hour on delivered work, proposal time included |
| **Failure** | 0 paid jobs after 25 proposals, **or** effective pay <€13 per hour on delivered jobs |
| **Inconclusive** | 1 job, or effective pay of €13–20 per hour |
| **After success** | Continue, raising the price after 3 good reviews. Consider a niche (e.g., accounting firms). Use the client stories to approach R2-type work if you learn to code |
| **After failure** | Choose "learn first" or "defer". The marketplace evidence is then against you personally, not against the category |
| **After inconclusive** | Narrow to one niche and retry with 15 more proposals |

### Phase A: no approval needed (≤20 h)

**Self-check (gate):** if the 3 demos below are not working within 20 hours, with an error rate of 10% or less on 20 test items, stop and choose option 3 (learn first).

- Build 3 demo automations on your own data or synthetic data, for example:
  - email triage with drafted replies;
  - invoice PDF extraction into a spreadsheet;
  - meeting notes into a task list.
- Time yourself, and write a 1-page case for each: problem, flow, error rate on 20 test items, cost per run.
- Draft the profile and 3 proposal templates (below).

### Phase B: needs approval

| # | Action | Approval needed because |
|---|---|---|
| B1 | Open a freelance-marketplace account and accept its terms and fees (check the current fee schedule first) | Opening an account; contractual terms |
| B2 | Publish the profile and demo cases | Publishing |
| B3 | Send up to 25 proposals | Contacting people; spending bid credits |
| B4 | Accept contracts and connect to client systems with client-granted, revocable access | Commercial commitment; credentials |
| B5 | Register as self-employed or IK before the first payment | Registration with authorities |

### Draft materials (V4)

**Profile headline:** "AI workflow automations with a human in the loop: email, documents, CRM. Fixed price, tested on your real examples."

**Proposal template (≈100 words):**

> Hi, I read your post about [task]. Here's how I'd approach it:
> (1) [trigger] → (2) AI step that [classifies/extracts/drafts] → (3) [you approve] → (4) [result lands in tool].
>
> I'll test it on 20 of your real examples and tell you the error rate and running cost before you accept it. You get a one-page runbook and 30 days of fixes.
>
> Fixed price: €[X]. A similar demo: [link].
>
> One question to scope it: [specific question about volume or exceptions].

**Scoping checklist:** input source and volume; output destination; the approval point; error handling; who owns the API keys (the client); data that must never be sent to a model; acceptance test (20 examples).

---

## V1: Limited agent risk review (only with security background)

| Item | Plan |
|---|---|
| **Hypothesis** | Small companies deploying agents will pay ≥€1,500 for a limited, clearly scoped review from a credentialed individual |
| **Target customer** | 10–100-person companies shipping agent features. Reached via referral partners (development agencies, fractional CTOs) rather than cold outreach |
| **Offer tested** | Limited agent risk review at €2,500 (first 3 as discounted or free case studies, with permission to publish anonymised findings) |
| **Evidence to collect** | Partner willingness to refer; buyer objections ("need a recognised firm"?); price acceptance; insurance quote |
| **Time cap** | 60 hours over 8 weeks |
| **Spend cap** | €150, excluding insurance (insurance is a separate approval once a sale is likely) |
| **Success** | ≥1 paid review at ≥€1,500 **and** ≥2 partners willing to refer |
| **Failure** | Partners decline to refer, **or** ≥5 buyers say only an established firm is acceptable |
| **Inconclusive** | Free case-study demand only |
| **After success** | Consider an SIA, insurance and an adviser-reviewed contract template **before** the first paid sale |
| **After failure** | Fold security content into R2 (the safe-configuration checklist) instead |

**Phase A (no approval):**
- Write the review checklist and an anonymised sample report from your *own* agent setup.
- Draft the contract scope and exclusions.

**Phase B (approval):**

| # | Action |
|---|---|
| B1 | Contact up to 10 potential referral partners |
| B2 | Offer 3 case-study reviews |
| B3 | Request insurance quotes |
| B4 | Ask an adviser to review the contract template, at a cost |

**Partner message draft:**

> Hi [Name], I'm [Your name], a security engineer focused on AI agents. Clients of agencies like yours are connecting agents to email, CRMs and code. I do a short, clearly scoped configuration review (not a pentest) that finds the common "private data + untrusted input + outbound action" mistakes. Could I show you a sample report? If it's useful for your clients, I'd like to discuss referrals.

**Scope statement (must appear in the contract and report):**

> This is a limited review of documented architecture and configuration as provided by the client. It is not a penetration test, security audit, certification or guarantee. No active testing was performed unless separately authorised in writing.

---

## V3: Support-agent evaluation (second test, later)

| Item | Plan |
|---|---|
| **Hypothesis** | Support leaders paying per resolution will commit ≥€2,000 to an independent outcome audit |
| **Target** | Heads of support at 10–100-agent support teams using an AI agent billed per outcome |
| **Evidence** | Whether they distrust the vendor count; data-export feasibility; price reaction |
| **Time / spend cap** | 50 h over 8 weeks / €100 |
| **Success** | ≥1 commitment at ≥€2,000 and ≥3 confirmations that data export is feasible |
| **Failure** | Most say export is impossible or vendor reports suffice |
| **Inconclusive** | Interest without data access |
| **Phase A (no approval)** | Build the labelling rubric and evaluation method on a public customer-support dataset; write a sample report |
| **Phase B (approval)** | Up to 10 interviews (contacting people); any data processing requires a signed DPA (contractual commitment) |

**Interview opener:**

> "How do you check the resolution numbers your AI vendor reports? What would it be worth to know the true figure?"

---

## Decision timeline if you approve V2 or V4

| Week | V2 | V4 |
|---|---|---|
| 1–5 | Phase A: self-check, proof pilot (baseline from history), materials | 1–3: Phase A: demos, profile |
| 3–10 | Phase B contacts and calls (after approval) | 3–6: Phase B proposals (after approval) |
| 10 | Score against thresholds; decide | 6: score; decide |

**Total commitment if both phases run:**
- **V2:** ≤60 hours, ≤€150, 10 calendar weeks.
- **V4:** ≤50 hours, ≤€100, 6 weeks.
- No registration until someone pays.
