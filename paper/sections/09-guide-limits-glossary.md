## 13. Practical starting guide

### 13.1 If you want to *use* agents (individual or small team)

1. **Pick one recurring, checkable task.** Examples: summarising the inbox into a to-do list, drafting replies, researching suppliers, writing code with tests.
2. **Start with an official product** (vendor app, scheduled tasks) or **your own API key**. Don't route a consumer subscription login through third-party agent software [S016][S075].
3. **Begin at autonomy level 3–4.** The agent proposes and you approve sending, paying and deleting [S002].
4. **Break the trifecta.** An agent that reads the open web shouldn't also hold your mailbox *and* be able to send [S011].
5. **Set a monthly spend cap** and check cost per *useful* result after two weeks (§6.4).
6. **Review the logs** of anything that acted on your behalf. Assume it can be fooled [S118][S069].

### 13.2 If you want to *build* agents

1. **Write down the task, success criterion and cost of an error** before choosing an agent design. Prefer a workflow if the steps are known [S001].
2. **Build an evaluation set first.** Use 30–100 real cases with human-judged expected outcomes, and calibrate any LLM grader against humans [S037].
3. **Use MCP for tools and keep tools narrow:** read and write split, idempotent, scoped credentials. Track the 2026-07-28 spec changes [S032].
4. **Put limits in code:** step caps, spend caps, approval thresholds, allow-lists [S080].
5. **Make prompts cache-friendly** and measure cost per completed task (§6.3).
6. **Red-team before launch** against OWASP ASI01–ASI10 [S010]. Repeat after every model or tool change.
7. **Design the human escalation path.** It is usually your biggest cost and your safety net (§6.6).
8. **Disclose AI interaction** to people where required, for example in the EU since 2 Aug 2026 [S074].
9. **Keep provider portability:** maintain a second model tested, and keep your own logs and data.

### 13.3 If you want to build a *business* in this market

1. **Choose a buyer you can reach** (§12.3) and a pain you can evidence: security, measurement, evaluation, readiness.
2. **Run the register's validation experiment** before building anything, once the owner approves contact or spend. Pre-commit to the go/no-go threshold.
3. **Price on outcomes the buyer already measures,** such as hours saved, incidents avoided, or resolution verified. Avoid pricing on activity counts.
4. **Watch platform risk.** Avoid businesses that need terms-of-service grey zones such as credential capture or undeclared bots [S063][S016].
5. **If operating from Latvia or the EU, know your client mix before the first invoice.**
   - Buying foreign APIs does not force VAT registration: the special s.139² registration covers it [S122].
   - Selling to an EU VAT-registered business does force full registration [S122].
   - Confirm the regime choice with an adviser before invoicing (§15.9 question 1). This does not block testing demand.
7. **Use the decision package.** `package/00-START-HERE.md` turns this paper into a route comparison, economics and prepared validation plans.
6. **Re-check this paper's dated facts quarterly.** Protocols, prices and policies moved materially within the six months before this paper.

## 14. Limitations (revised in v1.1 and v1.2)

The full claim-by-claim account is in `research/limitations-resolution.md`. Summary of the five limitations reported in v1.0 and what happened to each:

| v1.0 limitation | Outcome | What changed |
|---|---|---|
| Gartner, McKinsey and OpenAI figures supported only by search extracts | **PARTIALLY RESOLVED** | Gartner and McKinsey releases were read directly on publisher-hosted pages. Populations, samples and dates were added [S084][S085][S086][S087][S098][S082][S083]. One Gartner figure (~$202bn) was **removed** because no primary contained it. Anthropic revenue now rests on company posts, with $65bn kept as a single-source press report [S088][S089]. The OpenAI March 2026 checkout quote and Atlas security quote still rely on search extracts of the primary, corroborated by independent coverage [S025][S118] |
| When autonomous agents are active | **PARTIALLY RESOLVED** | "Active" defined in six units (§10.1). New evidence: Cloudflare (agent fetches follow weekly human rhythms) [S092] and our analysis of 2.74M agent-authored pull requests (flat daily profile, mild weekday lean) [S093]. No representative dataset found for scheduled or continuous agents or for purchase timing. Measurement plan in §10.4 |
| How often platforms ban agents | **UNRESOLVED AFTER DOCUMENTED SEARCH** (rate); partially improved (context) | Policy, incident and frequency evidence separated (§11.3.1). Anthropic's all-cause enforcement totals added (11.4M bans, 10.6% of appeals overturned, H1 2026) [S094]. No agent-specific numerator or exposure denominator is published, so no rate is given |
| Value of purchases completed autonomously | **PARTIALLY RESOLVED** (bounded) | Autonomy levels P1–P4 defined. The social-media x402 figure was replaced by Visa's report ($15.0M adjusted) [S091] and TRM's analysis (0.6%–7.5% looks agentic; ~$5–11k a month) [S090]. A global total remains unknown, and we explain why one cannot be built (§9.2) |
| US-heavy evidence | **PARTIALLY RESOLVED** | Added Eurostat (EU and Latvia AI use) [S096], OECD 11-country interviews [S097], an Accenture 16-country survey read directly [S115], Eurostat labour costs [S119], EU legal sources [S107][S103][S113][S114], and Latvian tax and registry sources [S099][S100][S102]. Added a transferability classification for each conclusion (§11.4). Commerce and enforcement evidence remains US-centred because that is where the activity and litigation are |

**Limitations that remain:**
- **Freshness.** Evidence was retrieved on 12 October 2026. Several facts changed within weeks of each other: Amazon's agent block, Cloudflare's defaults, the MCP spec, and the discontinuation of OpenAI's Atlas browser.
- **Access.** Some primaries still block automated retrieval (openai.com, cnbc.com, OpenAI's DSA data pages). We did not bypass these.
  - In v1.1, Gartner's and McKinsey's alternative hosts were used. In v1.2, their provenance was checked [S137]: DNS records place the Gartner host inside Gartner's own infrastructure, and the pages declare canonical gartner.com or mckinsey.com URLs.
  - Reading Gartner through its origin host could, however, sidestep the bot controls on www.gartner.com. **That access path was discontinued in v1.2.** The key Gartner table was corroborated through an independent republication [S136].
  - No paywalled analyst reports were read.
- **Vendor-sourced evidence.** Much evidence on adoption, transactions and security comes from vendors with an interest in the result (e.g., [S021][S022][S088][S068]). Vendor statements establish what vendors claim, not independent proof.
- **Survey limits.** Adoption surveys are self-reported and use incompatible definitions (C001). The Gartner 2025 poll was of webinar attendees [S087].
- **Experimental limits.** Agent-behaviour findings come from simulations, mock marketplaces and small internal pilots [S029][S030][S039][S040].
- **Cost models.** The scenarios rest on explicit assumptions, not observed deployments. Resolution rates, engineering effort, security budgets and Latvian administrative costs need local quotes or pilots. Incident costs and non-EU indirect taxes are excluded.
- **Tax and legal (§15).** v1.1 relied on an outdated English translation of the VAT Law and reached a wrong conclusion about registration and the micro-enterprise tax.
  - v1.2 re-read the current consolidated Latvian text [S122][S123] and the tax authority's guidance [S124], and corrected it.
  - Consolidated texts are informative; the official publication prevails.
  - Remaining questions depend on the owner's circumstances and are stated precisely in `package/01-decision-brief.md` §8, with what each blocks.
- **Commercial evidence (v1.2).** Route prices come from published list prices and a vendor price guide [S128][S129][S130], not transaction data. Win rates and selling hours are assumptions. Large-company surveys dominate the demand evidence [S131][S133].
- **Reviews.** v1.2 used two independent AI reviewers (factual and commercial; see `verification/verification-report.md`). They are separate model instances, not human experts.
- **Timing and enforcement data.** These are narrow: coding agents on public GitHub, chat usage at one provider, and all-cause bans at one provider.
- **No primary research.** No interviews, surveys or experiments with real customers were conducted, because they need approval. The opportunity register remains hypothesis-only.
- **No human review.** No independent human expert has reviewed the paper.
