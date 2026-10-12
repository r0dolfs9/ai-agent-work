# Review, adversarial challenges and open questions

*Version 1.2 · 12 October 2026 · 10 minutes to read*

## 1. How this package was checked

| Check | Method | Result |
|---|---|---|
| Latvian VAT and micro-enterprise rules | Current consolidated **Latvian** texts on likumi.lv [S122][S123] and the State Revenue Service guidance [S124], read in this session. Re-read independently by the factual reviewer | v1.1's registration "trap" was **wrong** and has been corrected. The reviewer confirmed s.59(1), (4), (8), (9) and s.139²(4), (7), (9), (10), (11) |
| High-impact market claims | Re-read at source on 12 Oct: Anthropic $47bn run-rate [S088] and ban figures [S094]; Visa x402 [S091]; TRM [S090]; Atlas shutdown [S138]; Gartner table via an independent republication [S136] | All confirmed. The $202bn Gartner figure remains unlocated and is not used |
| Publisher alternative hosts | DNS and canonical-tag provenance check [S137] | Ownership established. The Gartner origin-host path was **discontinued** because it could sidestep bot controls |
| Independent factual review | A separate AI agent with no authorship and read-only access checked about 30 claims against sources and the tax arithmetic | 0 critical, 3 major and 8 minor findings. All fixed (§3) |
| Independent commercial review | A separate AI agent challenged the recommendation, demand assumptions, economics and plans | 2 critical, 7 major and 3 minor findings. All addressed (§3) |
| Figures vs models | `verification/check_numbers_v12.py` compares every quoted route figure with the model; plus the v1.0 and v1.1 check scripts | All pass at the time of writing (see the verification report) |
| Citations | `paper/build_paper.py` fails on any unresolved [S###]; the v1.2 check also covers package files | All resolve |
| Rendered edition | Headless Chromium at desktop (1280 px) and phone (390 px) widths: navigation, anchors, tables, horizontal overflow | Fixed: phone overflow from wide tables and long URLs. No broken in-page links |

**Limits of these checks.** The reviewers are AI model instances, not human tax advisers, lawyers or industry experts. No customer, adviser or vendor was contacted.

## 2. Adversarial challenges

**1. The strongest market claim: "customers demonstrably pay for coding agents and AI services".**
- **Challenge:** company run-rates are not audited revenue, and the Upwork growth is self-declared "AI-related" work on one marketplace.
- **Answer:** both are firm *for the category*:
  - a company statement re-read at source [S088][S141];
  - an SEC filing [S127].
- Neither shows demand for *your* offer. The brief says so explicitly and makes that the thing to test.

**2. The leading recommendation (R2 first if you code).**
- **Challenge (from the commercial reviewer):**
  - R2 depends on access to engineering leads, which a newcomer probably lacks;
  - its differentiator (measurement) is unproven;
  - a developer can likely earn more by contracting.
- **Response:**
  - the recommendation now branches on access;
  - the plan quotes two priced options, to learn whether measurement is valued;
  - "measurement" is reframed as adoption and cost telemetry, not a productivity verdict;
  - employment or contracting is named as the real benchmark.
- **Still stands:** R2 has the best newcomer first year (€11.2/h) and the best price evidence among routes open to non-credentialed developers.

**3. The weakest demand assumption.**
- **The assumption:** small teams will pay an *unknown individual*.
- **How the plans now test it:**
  - commitments must be strong signals (a paid engagement, an order with a deposit, or a paid scoping session);
  - a separate "channel failed" outcome stops a lack of conversations being misread as a lack of demand.

**4. Economics under an adverse scenario.**
- **The original adverse case was not adverse enough.** It was steady-state only and reached about €10–16/h.
- **The revised case** adds a 3-month-longer ramp and higher marketplace fees, and reports the first year. Under it, **every route loses money in year one**: −€1.3 to −€9.6 per owner hour.
- **The base case was also lowered** to a realistic newcomer: half the previous win rate, more selling hours per sale and longer ramps.
- **Conclusion:** for a newcomer, these are tests with option value, not income plans.

**5. Feasibility without credentials or customer access.**
- **R1** is explicitly gated on security credentials.
- **R3** is deferred unless you have support-industry contacts.
- **R2** needs professional coding skill, and its value depends on warm access.
- **R4** needs no credentials but pays little.
- **Without either skill or access**, the honest answer is option 3 (learn first) or option 4 (defer).

**6. Is the actual work explained concretely?**
- Each dossier has:
  - a week-by-week (R2) or step-by-step (R1, R3, R4) delivery plan with hours;
  - the skills and tools needed;
  - a self-check;
  - an illustrative engagement.
- The validation plans contain drafted messages, call scripts and checklists.

## 3. Independent review findings and what changed

| # | Reviewer | Finding (abridged) | Severity | Resolution |
|---|---|---|---|---|
| F1 | Commercial | V2 relied on cold email to Germany, where B2B advertising email needs prior consent (UWG §7(2)) | Critical | Verified via German chamber-of-commerce guidance [S139]. Cold email to German recipients removed and made a blocking rule for other countries until checked; channel list changed |
| F2 | Commercial | Benchmark compared gross wages with net take-home; employment or contracting not offered | Critical | Net benchmark ≈ €8.69/h added (CALCULATION with [S100]); own contracting rate named as the real comparator in the brief, economics and menu |
| F3, F9, C1–C2 | Commercial | Base inputs optimistic for a newcomer; adverse case steady-state only | Major | Base revised (e.g., R2 €3,000, 0.5 wins/month, 40 selling hours, first win in month 6; R4 €600, 1 win/month). Old base became "with network". Adverse adds ramp and fee; first-year figures shown |
| F4 | Commercial | Plan cannot tell whether measurement is valued | Major | Two priced options; telemetry framing |
| F5 | Commercial | 25 cold contacts cannot yield 10 conversations | Major | Separate "channel failed" outcome; demand failure needs ≥8 conversations |
| F6 | Commercial | 6-week timeline inconsistent with the proof pilot | Major | 10-week cap; baseline taken from history |
| F7 | Commercial | A letter of intent is a weak signal | Major | Commitment = paid work, an order with a deposit, or a paid scoping session |
| F8 | Commercial | Upwork fee is variable, 0–15% | Major | Cited [S140]; 15% in low and adverse cases |
| F10, F12 | Commercial | Partner channels missing; R4 lacks a self-check | Minor | Added |
| F11 | Commercial | R5 hours inconsistent; empty review file | Minor | Fixed; this document |
| 1 | Factual | Model charged 31.07% contributions below €780/month; S125 says 10% pension only | Major | Verified against our own S125 record; formula fixed; all figures regenerated |
| 2 | Factual | Micro-enterprise comparison used client mixes that make it ineligible | Major | Reworded as a hypothetical same-revenue, non-EU client mix |
| 3 | Factual | Brief applied TRM's 0.6–7.5% to Visa's $15.0M | Major | Corrected denominator ($25.6M screened, TRM) |
| 4–11 | Factual | Dates, the Claude Code citation (now [S141]), audit price bands, R4 unpaid hours, MUN loss "from the next tax year", monthly notice only for months with purchases, SIA comparison wording, MentorCruise description | Minor | All corrected |

**Did corrections change the recommendation?**
- **The ordering survived:** R2 for coders, R4 or learn-first for non-coders, R1 gated, R3 deferred, agent-bought products rejected.
- **The framing changed materially:** access to buyers, and your own alternative income, now matter more than the route.
- **The economics are much less attractive** for a newcomer than the first draft showed.

## 4. Open questions, and exactly what each blocks

**Blocking questions for you (at most two):**
1. **Which option do you choose (1–4 in the brief's decision menu)?** If 1 or 2, may the drafted outreach be sent as written, edited, or not at all? *Blocks every Phase B step.*
2. **Do you have warm access to buyers?** For R2 that means about 10 engineering leads you could reach through people who know you. For R1 or R3, security or support contacts. *Does not block Phase A. Decides whether Phase B tests demand or only tests a channel.*

**Questions for an adviser, and when they matter:**

| Question (exact wording) | Matters when | Blocks |
|---|---|---|
| "Given clients in [countries], which is cheaper and simpler for me: self-employed general regime, micro-enterprise tax with s.139² registration, or full VAT registration? At what client mix does it change?" | Before the first invoice | First sale (not the test) |
| "For marketplace X's invoicing model, who is my customer for VAT purposes, and must I register before the first job?" | Before the first marketplace job (R4) | First paid job |
| "Is a one-to-one personalised B2B email from a Latvian sender to a business in [country] lawful?" | Before any cold email to that country | Cold email only; other channels unaffected |
| "Does my limited-review contract effectively cap liability, and what professional-indemnity cover is proportionate?" | Before the first R1 sale | R1 first sale |
| "Is my DPA template adequate for processing support transcripts with a US model sub-processor?" | Before the first R3 sale | R3 first sale |
| "Should I form an SIA for liability, given my route and revenue?" | Before scaling (any route), or before the first R1 sale | Scaling |

**Unknowns that only the test can resolve:**
- win rates;
- selling hours per sale;
- accepted prices;
- whether buyers value measurement;
- your delivery speed.

These are the inputs the model is most sensitive to.

## 5. What could invalidate the conclusions

- **Evidence of demand for products that agents buy themselves.** Card networks publishing real agent-initiated volumes, or x402 agentic commerce growing by orders of magnitude, would reopen products sold to agents.
- **Vendors making the service unnecessary.** For example, free team analytics and guided setup for coding agents (against R2), or built-in independent resolution auditing (against R3).
- **SME adoption much slower than the large-firm surveys imply.** Eurostat: only 20% of EU enterprises used any AI in 2025 [S096].
- **A change in Latvian tax rules.** The 2026 contribution changes reported in secondary sources are not verified [S125].
- **Your own circumstances.** A high contracting rate makes every route a worse use of time in year one.
