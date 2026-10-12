# Dossier R1: Limited agent risk review (not an audit or certification)

*Shortlisted **only if you have security experience** (application security, penetration testing, security engineering). Register ID O03. Version 1.2, 12 October 2026. About 9 minutes to read.*

## 1. In one paragraph

Companies connecting agents to email, files, CRMs and code worry about security. In KPMG's survey of large US companies, 80% named cybersecurity as their top obstacle [S131]. You would sell a short, **document-and-configuration review** of one agent deployment:
- what data it can see;
- what untrusted content it reads;
- what it can do or send out;
- who approves what;
- what is logged.

The result is a prioritised list of findings mapped to public frameworks. **It is not a penetration test, a security audit or a certification.** That distinction is the core of the offer and its main risk.

## 2. Limited assessment versus professional audit or certification

| | **Limited risk review (this route)** | **Professional security audit / penetration test** | **Certification** (e.g., ISO/IEC 42001, ISO 27001, SOC 2 report) |
|---|---|---|---|
| What it is | Structured review of architecture, configuration, permissions and process against public checklists (OWASP Agentic Top 10, the "lethal trifecta" rule [S011], joint government guidance [S051]) | Authorised technical testing: attempts prompt injection, data exfiltration and privilege escalation against the live or staging system | Formal conformity assessment of a management system or controls |
| Who may do it | Anyone competent, but credibility needs security background | Specialists with testing methodology, written authorisation, usually insurance | **Only accredited certification bodies or licensed auditors** |
| Typical price | Assumed €1,500–4,000 | $6k–45k+; specialists $16k–50k; 5–25 days [S130] | Varies widely; not researched |
| Output | Findings list plus recommendations; explicit scope and exclusions | Test report with reproduced vulnerabilities | Certificate or attestation report |
| Liability exposure | Moderate, if scope is clear and liability capped | High | — |

**Rule for this route:** never use the words "audit", "certified", "compliant" or "penetration test" in marketing or reports. State the exclusions in the contract and in the report. Running any active test of a client system requires **written authorisation from the system owner**. Testing third-party systems is out of scope altogether.

## 3. Who pays and who decides

- **Who pays and decides:** the CTO or founder of a 10–100-person company deploying its first agents, or a product team shipping an agent feature.
- **Who sends them to you:** an investor's or customer's security questionnaire often triggers the need.
- **Who blocks it:** a security lead who prefers an established firm.

## 4. The problem and today's workaround

**The problem.**
- Agents combine private data, untrusted input and outbound actions: the "lethal trifecta" [S011].
- Prompt injection is mitigated, not solved [S068][S118].
- Documented incidents include tens of thousands of internet-exposed personal-agent installations and malicious add-ons [S013][S014].

**Workarounds:**
- free checklists, which require expertise to apply;
- vendor security defaults;
- a full pentest firm, which is expensive and slow;
- doing nothing.

## 5. Evidence versus hypotheses

| Statement | Status |
|---|---|
| Security is the leading adoption barrier for large firms | **Fact** for large US firms: 80% (KPMG Q4 2025, n=130) [S131]. 52% in a Dynatrace survey (secondary) [S132] |
| Companies pay for LLM/agent security assessments | **Fact (price guides)** [S130]: a vendor-published price guide, so biased |
| Small companies will pay €1,500–4,000 for a *limited* review from an individual | **Hypothesis** |
| The limited review reduces real risk | **Interpretation.** Configuration errors are a documented cause of incidents [S013] |

## 6. What you would sell and deliver (base: €2,500, about 24 hours)

1. Scoping and a written authorisation covering what you may read; no active testing. (2 h)
2. Architecture walkthrough with the developer: data sources, tools, outbound channels, credentials, approval points, logging. (4 h)
3. Configuration and document review against a fixed checklist (paper Appendix B, mapped to OWASP ASI). (8 h)
4. Findings report: severity, evidence, fix, owner; explicit "not tested" list. (6 h)
5. Readout; one re-check of fixes within 30 days. (4 h, which includes the 20% rework allowance)

**Optional retainer** (base assumption: €300/month, 25% of clients): re-review on each major agent change.

## 7. Skills, credibility, tools and access

- **Skills (required):** security engineering fundamentals, threat modelling, secrets and identity management, an understanding of LLM-specific attacks.
- **Credibility:** prior security role, certifications held personally (e.g., OSCP or CISSP; *not* required by law, but buyers look for them), or published research. **Without these, this route is not recommended.**
- **Tools:** a report template; a checklist; a test environment for reproducing configurations.
- **Insurance:** professional indemnity. Price UNKNOWN; a quote request needs approval.
- **Contracts:** a liability cap, a scope-and-exclusions clause and confidentiality. Have the template reviewed once, before the first sale.

## 8. Setup, workload and unit economics (Calculation, `models/route_economics.py`)

<!-- econ:start -->
*Cases: **low** = adverse inputs; **base** = a newcomer without track record or warm contacts; **high** = with a network or strong public proof. Benchmark: about €8.69/h net for an average Latvian professional [S126][S100]; your own contracting rate is the real comparator.*

| | Low | Base (newcomer) | High (with network) |
|---|---|---|---|
| Price per engagement (net of VAT) — assumption | €1,500 | €2,500 + €300/month retainer (25% of clients) | €4,000 + €500/month retainer (35% of clients) |
| Engagements won per month once steady | 0.25 | 0.5 | 1 |
| Months before first sale | 9 | 6 | 4 |
| Selling hours per *won* engagement | 60 h | 45 h | 25 h |
| Delivery hours per engagement incl. rework | 39 h | 24 h | 18 h |
| One-time setup: cash / owner hours | €900 / 80 h | €900 / 60 h | €900 / 50 h |
| Monthly fixed cash costs | €220 | €260 | €320 |
| Revenue per month once steady (net of VAT) | €375 | €1,475 | €5,575 |
| Operating profit per month once steady | €121 | €1,141 | €5,064 |
| Owner hours per month once steady | 31 h | 43 h | 58 h |
| **Self-employed take-home per month once steady** | €109 | €783 | €3,413 |
| Take-home per owner hour once steady | €3.5 | €18.3 | €58.8 |
| First 12 months: operating cash before income tax | −€2,516 | €3,839 | €32,154 |
| First 12 months: owner hours | 361 h | 482 h | 601 h |
| **First 12 months: take-home per owner hour** | −€7.0 (loss) | €7.2 | €36.3 |
| First 12 months under the combined adverse case | −€10.7 (loss) | −€6.4 (loss) | €5.3 |

Setup and fixed-cost contents (assumption): setup €900 = professional-indemnity insurance first instalment/quote deposit (~€500, UNKNOWN price), report template and test environment (€150), domain/email/site (€100), contract template review (€150); fixed = insurance/12, bookkeeping, tools, model API.
<!-- econ:end -->

## 9. Competition, substitutes and refusal reasons

- **Competition:**
  - security boutiques adding "AI security" ($15k–40k [S130]);
  - AI-security start-ups with automated scanners;
  - large consultancies;
  - model vendors' own security guidance.
- **Why a buyer refuses:**
  - "We need a recognised firm for our customer's questionnaire";
  - "A scanner does this";
  - "What happens if you miss something?";
  - "We haven't deployed yet."

## 10. Global distribution and acquisition barriers

- Trust-based selling is slow without a reputation. Referral partners (development agencies, fractional CTOs) are the realistic channel.
- Cold outreach on security topics is easily mistaken for spam or scare-selling. Messages must be factual.

## 11. EU and Latvian operating implications

- **Liability:** this is the route where an **SIA** (limited liability; €75 registration [S102]) plus insurance matters before the first sale. **Exact adviser question:** "Does my contract template effectively cap liability for a limited configuration review under Latvian/EU law, and what professional-indemnity cover is proportionate?" It **blocks the first sale; it does not block the test.**
- **VAT:** the same client-mix rule as other routes (s.59(8)) [S122].
- **GDPR:** reviewing configurations may expose personal data. Use a processor clause and minimise what you copy [S110].
- **AI Act:** none applies directly to the reviewer. Clients may need Art. 50 disclosure from August 2026 [S074], which is a useful finding category.

## 12. What would invalidate this route

- You lack security credentials. This is decisive.
- In the test, buyers say they would only accept an established firm, or price expectations sit below €1,000.
- Insurance quotes exceed about 20% of expected revenue.

## 13. Cheapest credible first test

See **plan V1**.
- **Phase A (no approval needed):** write a public, anonymised "agent risk review checklist and sample report" based on your own agent setup.
- **Phase B (needs approval):** offer 3 free or discounted reviews to companies reached through referral partners, in exchange for permission to use an anonymised case. Then 15 conversations at the full price.
- **Caps:** ≤60 hours and ≤€150, excluding insurance.

## 14. Illustrative engagement (not a real customer)

> **Illustrative.** A 20-person B2B start-up in the Netherlands is connecting an agent to its support inbox and CRM, with permission to email customers.
>
> - **Review.** You review the setup and find:
>   - the agent reads inbound email (untrusted), sees the full CRM (private) and can send email (outbound): the trifecta;
>   - API keys sit in a shared environment file;
>   - no log ties a sent email to the input that caused it.
> - **Report.** 12 findings, each with a fix: split read and send roles; require human approval for first-contact emails; move secrets to a vault; add trace logging. It also lists what was **not tested**, such as resistance to live prompt injection.
> - **Commercials.** €2,500. The client is a Dutch company with a VAT ID, so the invoice is reverse charge and full Latvian VAT registration is required before invoicing. An SIA plus insurance is recommended.
