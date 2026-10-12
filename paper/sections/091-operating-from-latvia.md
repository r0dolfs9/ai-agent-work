## 15. Operating a global agent business from Latvia and the EU

> **Status of this section (revised v1.2).** It summarises published rules as of 12 October 2026 so you can make better decisions and ask better questions. It is **not tax or legal advice**. Points that depend on facts only an accountant or lawyer can assess are flagged ⚖.
>
> **v1.2 correction.** v1.1 relied on an English translation of the VAT Law that was marked outdated [S099]. On that basis it said buying foreign APIs forces VAT registration and makes the micro-enterprise tax unavailable. **That was wrong for the law in force since 1 July 2025.** v1.2 rests on:
> - the current consolidated **Latvian** text of the VAT Law (s.59 and s.139²) [S122];
> - the Micro-enterprise Tax Law [S123];
> - the State Revenue Service (VID) guidance updated 27 June 2025 [S124].

### 15.1 The hypothesis and the short answer

**Hypothesis tested:** *an operator based in Latvia can serve customers internationally through agents.*

**Short answer (INTERPRETATION):** **yes for most B2B agent services and software, with conditions.** It is **not** unrestricted global trading. What actually limits feasibility is, in order:
1. **product type**, such as handling customers' money or high-risk AI uses;
2. **customer location**, which sets the VAT, consumer-law and sanctions rules;
3. **provider and payment availability** where the *customer* is;
4. the operator's own **administrative capacity**.

Being in Latvia rather than elsewhere in the EU changes mostly tax mechanics and costs, not market access.

| Factor | Does Latvian location materially matter? | Evidence |
|---|---|---|
| Access to model APIs | **No** for Latvia itself. Latvia is a supported country for Claude API, Claude.ai and the OpenAI API | [S106] |
| Customers in unsupported or sanctioned places | **Yes**, through EU law: EU sanctions bar IT consultancy, enterprise-management software and other services to Russia-established entities (FIU authorisation needed even for subsidiaries of EU groups since 1 Oct 2024) | [S112] |
| Payment acceptance | Little. Stripe publishes Latvian pricing (EEA cards 1.5% + €0.25); merchants of record (Paddle 5% + $0.50) can take over global tax collection | [S104][S105] |
| VAT | **Yes.** EU-harmonised place-of-supply rules plus Latvian specifics (registration triggers, 21% rate) | [S099][S100][S103] |
| Company income tax | **Yes.** Latvia taxes company profit only when distributed (20% of the gross distribution) | [S100] |
| Data protection | EU-wide: GDPR applies to EU operators regardless of customer location | [S109][S110] |
| AI regulation | EU-wide: the AI Act applies by role and use case | [S107][S108] |
| Consumer law | Depends on the *customer's* country. EU consumers have a 14-day withdrawal right with exceptions | [S113] |
| Invoicing | Latvian specifics: B2B structured e-invoicing becomes mandatory on 1 Jan 2028; B2G already mandatory | [S101] |

### 15.2 Establishment options

| Form | Registration | Liability | Main tax on profit | Notes |
|---|---|---|---|---|
| **Self-employed person** (registered with VID as performing economic activity) | With the State Revenue Service | Unlimited (personal) | Progressive PIT 25.5% up to €105,300, 33% above, +3% above €200,000 [S100]. 2026 social contributions: 31.07% on income of at least €780 per month, and 10% pension contribution on income above that base or below it [S125] | Simplest. Personal liability for an agent's mistakes is a real exposure |
| **Micro-enterprise taxpayer** (natural persons registered with VID, individual merchants, individual enterprises) [S123] | Opt-in | Unlimited | **25% of turnover**, with no deduction for expenses; 80% counts as social contributions and 20% as PIT [S123][S124] | **Available alongside buying foreign APIs** via the s.139² special VAT registration (since 1 Jul 2025). **Lost** if you supply B2B services to a VAT-registered business in another EU state, or if turnover exceeds €50,000 [S124]. Taxing turnover penalises routes with high costs |
| **Individual merchant (IK)** | Enterprise Register, state fee €30 [S102] | Owner liable with own property [S102] | As self-employed | Rarely better than an SIA for liability-heavy agent work (INTERPRETATION) |
| **SIA (limited liability company)** | Enterprise Register, state fee €75, electronic filing; share capital ≥ €2,800, or reduced-equity SIA below that [S102] | Limited to the company | **CIT 20% of gross distributed profit** (0.2/0.8 of the net dividend). Retained profit untaxed. Dividends to individuals 0% PIT when CIT has been paid. Optional regime for individual-owned companies: 15% CIT + 6% PIT [S100] | Standard vehicle for selling internationally and limiting liability |

**Costs (CALCULATION, `models/operator_economics_results.md`).**
- **One-off:** €75 SIA state fee. Share capital is equity, not a cost.
- **Recurring admin** (bookkeeping incl. VAT/OSS returns, bank, tools): roughly **€1,700–6,400 a year** (ASSUMPTION: no official price list exists; get quotes).
- **Profit distribution:** on €50,000 of distributed profit, the owner receives €40,000 under the standard regime and €39,950 under the alternative regime. The two are almost identical as described [S100]. Ask an accountant what the alternative regime changes in practice ⚖.

### 15.3 VAT: who charges what, and when you must register

**Selling** (the place of supply decides which country's VAT applies) [S099][S103]:

| You sell… | To… | VAT treatment (simplified) | Registration consequence |
|---|---|---|---|
| Agent services or software subscription | Latvian business or consumer | Latvian VAT 21% | Register once taxable supplies exceed €50,000 [S100][S099] (s.59(1)) |
| B2B services (consulting, managed agents, SaaS) | Business in another EU state (with VAT ID) | Taxed where the customer is established (s.19(1)); customer self-accounts under reverse charge; you invoice without VAT | **Threshold does not apply**: s.59(8) removes the €50,000 exemption for anyone supplying s.19(1) services to a taxable person of another Member State, so register **before the first such sale**. Also file EU sales (recapitulative) statements [S122]. A micro-enterprise taxpayer loses that regime [S124] |
| **Electronically supplied** services (automated SaaS, an agent product with minimal human involvement) | Consumers in other EU states | Customer's country VAT (s.27), unless your total cross-border B2C electronic sales and distance sales stay ≤ €10,000 in the current and previous year, in which case Latvian VAT applies; declared through the **Union OSS**, filed quarterly [S103][S099] | OSS registration in Latvia |
| Human-delivered services (e.g., consulting performed by you, set-up work) | Consumers in other EU states | General B2C rule: supplier's place (s.19(2)), i.e. Latvian VAT 21% [S099] | Classifying a service as "electronically supplied" or not is a fact-specific judgement ⚖ |
| Any services | Businesses outside the EU | Outside Latvian VAT (place of supply = customer's country) [S099] (s.19(1)) | Check the customer country's rules (some apply reverse charge or require foreign-supplier registration) ⚖ |
| Electronically supplied services | Consumers outside the EU | Outside EU VAT, but many countries tax foreign digital suppliers (e.g., the UK, and US state sales taxes). Not researched in depth here (UNKNOWN) | A **merchant of record** takes on these registrations [S105][S104] |

**Buying foreign APIs, cloud and SaaS** (corrected in v1.2):
- These are B2B services with their place of supply in Latvia. The Latvian buyer self-assesses 21% VAT under reverse charge (s.88 for EU suppliers, s.89 for non-EU) [S099][S122].
- **Since 1 July 2025, buying them does *not* by itself force full VAT registration.** A taxable person who receives such services may keep the €50,000 small-business exemption (s.59(9)) by registering under the **special procedure of s.139²** [S122]:
  - the VAT number is used only for those purchases;
  - there is no obligation to issue VAT invoices;
  - VAT is due only on those purchases, and there is **no right to deduct it** (s.139²(9));
  - a notice is due by the 20th of the following month for each month with such purchases, with payment within 23 days of the month's end.
  - Before 1 July 2025 this option did not exist (transitional provision 47).
- **Cost of the special route (CALCULATION):** 21% of foreign purchases becomes a real cost. On €150 a month of model and tool subscriptions that is **€31.50 a month (€378 a year)**. Fully registered businesses instead self-assess and deduct the same VAT in one return, so for them it is cash-neutral.
- **Micro-enterprise tax:** it can be combined with the special registration. The VID guidance confirms this as long as the taxpayer does not supply s.19(1) services to VAT-registered businesses in other Member States and turnover stays at or below €50,000 [S124][S123].
- **Practical consequence (INTERPRETATION):** client mix, not supplier mix, drives the VAT burden.

| Client mix | Registration | Admin burden (INTERPRETATION) |
|---|---|---|
| Non-EU businesses only, plus Latvian clients under €50k | s.139² special registration if buying foreign tools; micro-enterprise tax possible | **Lowest** |
| Any VAT-registered business in another EU state | Full VAT registration from the first such sale, plus EU sales statements | Medium |
| EU consumers buying an electronically supplied product | OSS above €10k, or a merchant of record | Medium–high |

- **v1.1's "trap" statement is withdrawn.** v1.1 cited s.59(6) of the outdated translation and said a micro-enterprise could not buy foreign APIs. The claim ledger (L51/L52 → L65/L66) records the correction.
- Some providers bill EU customers with VAT unless a valid VAT ID is supplied. Third-party guides report that Anthropic invoices EU customers through a non-resident VAT scheme and switches to reverse charge when a business VAT ID is added. That is unverified, and a job posting names Ireland as the EU billing entity, which conflicts with it [S120]. Check the invoice seller block.

### 15.4 Payments, invoicing, currencies, refunds and disputes

- **Processing costs** (CALCULATION from [S104][S105]). On a €49 net subscription, the seller keeps:
  - **Stripe direct:** €46.2–48.0, but files VAT and OSS itself.
  - **Paddle (merchant of record):** €45.6–46.1.
  - **Stripe Managed Payments:** €44.5–46.3. Eligibility for Latvian sellers is not confirmed.
  - The MoR premium is €0.1–2.3 per sale. In exchange, the MoR becomes the legal seller, handles foreign indirect taxes and runs disputes. **RECOMMENDATION:** use a MoR for self-serve consumer and global SaaS. Invoice directly for B2B services.
- **Disputes:** Stripe charges €20 per dispute [S104]. For agent-initiated purchases, liability rules are still unsettled (§9.4).
- **Consumer refunds (EU):** 14-day withdrawal right for online services from the contract date. It is lost only if the consumer expressly agreed to immediate performance and the service was fully performed. For digital content, it is lost once streaming or download starts with express consent [S113]. Build these consents into checkout.
- **E-invoicing:** structured B2B e-invoices become mandatory in Latvia on **1 Jan 2028** (moved from 2026). Invoices to Latvian public bodies have been mandatory since 1 Jan 2025. Peppol BIS 3.0 / EN 16931 formats apply [S101]. Choose invoicing software that already supports Peppol.
- **Currencies:** pricing in USD for global customers is commercially normal. Payment processors add about 2% when they convert [S104]. How foreign-currency invoices must show VAT amounts in Latvia was not researched (⚖).

### 15.5 Data protection (GDPR) and international transfers

| Operating role | Typical GDPR role (INTERPRETATION ⚖) | Practical requirement |
|---|---|---|
| You run agents on a client's data (B2B service) | **Processor** for the client | Art. 28 data processing agreement with the client. Flow your model provider down as a **sub-processor**. Document transfers |
| You sell a SaaS agent to users | **Controller** for account and usage data; often processor for customer content | Privacy notice, legal basis, retention schedule, DPAs with providers |
| You use agents internally | **Controller** | Minimise personal data sent to models; check the providers' DPAs |

- **Transfers to US providers:** Anthropic's DPA incorporates the EU Standard Contractual Clauses (Modules 2 and 3) [S110]. The EU–US Data Privacy Framework was upheld by the General Court on 3 Sep 2025, but an appeal to the Court of Justice (C-703/25 P) is pending [S109]. **RECOMMENDATION:** rely on SCCs plus a transfer impact assessment, not on the DPF alone, and use EU data-residency options where providers offer them.
- **Retention and security:** agent logs and traces contain personal data (§10.4). Set retention limits and access controls. Joint government guidance recommends strict access control for agentic systems [S051].

### 15.6 EU AI Act: roles, use cases and dates

- **Dates** [S107]:
  - in force 1 Aug 2024;
  - prohibited practices and **AI literacy** duties from 2 Feb 2025;
  - general-purpose model (GPAI) obligations from 2 Aug 2025;
  - **transparency (Art. 50)** from 2 Aug 2026;
  - high-risk Annex III uses from **2 Dec 2027**; Annex I product-embedded uses from 2 Aug 2028.
- **Roles** [S108]:
  - A **provider** develops an AI system (or has it developed) and places it on the market under its own name. A Latvian company selling its *own* agent product is a provider of that AI system, even if it uses a third-party model.
  - A **deployer** uses an AI system under its authority, for example an internal procurement agent or a client running your tool.
  - GPAI-model obligations fall on the model developers (Anthropic, OpenAI and similar), not on companies calling their APIs (INTERPRETATION ⚖).
- **What applies to most small agent businesses:**
  - Art. 50 disclosure when an agent interacts with people. Fines are up to €15m or 3% of turnover [S074].
  - AI literacy for staff [S107].
  - High-risk obligations from Dec 2027 **if** the use case falls in Annex III, such as hiring, credit or education. Avoid those uses unless you are ready for the conformity work.

### 15.7 Liability, delegated authority, regulated activities and sanctions

- **Product liability:** the revised Product Liability Directive brings software, including AI systems, under strict liability for products placed on the market after **9 Dec 2026**. National transposition is uneven [S111]. The proposed AI Liability Directive was withdrawn [S111]. **RECOMMENDATION:** contractual liability caps, professional indemnity insurance (pricing UNKNOWN), and logs that let you reconstruct what an agent did.
- **Authority delegated to an agent:** when your agent signs up for services, accepts terms or pays, the legal question is whether the company is bound as if an employee had acted. EU law did not provide an agent-specific answer in the sources reviewed (UNKNOWN ⚖). Practical controls are:
  - spend caps and allow-lists;
  - human approval for new contracts;
  - an agent identity distinct from staff credentials (§3.4).
- **Handling customers' money is a regulated activity.** Receiving and forwarding funds is a payment service under PSD2, possibly money remittance. The commercial-agent exclusion is narrow and is being narrowed further by the Payment Services Regulation [S114]. **INTERPRETATION ⚖:** an agent business that pays suppliers *on behalf of clients* from its own account likely needs a licence or a licensed partner. That is why opportunity O08 stays low-ranked.
- **Sanctions and export:**
  - EU Russia sanctions prohibit IT consultancy, enterprise-management software and other services to Russia-established entities [S112].
  - Model providers do not support several countries; Russia, Belarus, China and Iran are not on Anthropic's list [S106].
  - **RECOMMENDATION:** screen customers by country and ownership at onboarding.

### 15.8 Three operating models compared

| | **1. Agent services to businesses** (build, harden or audit agents; managed agent operations) | **2. Agent software subscription** (self-serve SaaS) | **3. Internal agent procuring business services** |
|---|---|---|---|
| Typical customer | EU and non-EU companies | Global SMBs and consumers | Your own company |
| VAT on sales | EU B2B: reverse charge, register before first sale (s.59(8)) [S122]. Non-EU B2B: outside scope. Latvia: 21% | EU consumers: OSS at customer-country rates (above €10k). EU B2B: reverse charge. Non-EU consumers: foreign digital-services taxes, so a MoR is advisable | n/a |
| VAT on purchases | Reverse charge on foreign APIs and cloud. If not fully registered, use the s.139² special registration (21% becomes a non-deductible cost) [S122] | Same | Same |
| GDPR role | Processor (client data) | Controller + processor | Controller |
| AI Act role | Deployer, or provider if you deliver your own branded system | **Provider** of the AI system. Art. 50 disclosure if it interacts with people | Deployer; AI literacy |
| Consumer law | Usually none (B2B) | 14-day withdrawal unless properly waived for immediate performance [S113] | n/a |
| Payments | Bank transfer / Stripe invoices; e-invoicing from 2028 | MoR or Stripe + OSS | Company card or per-agent cards with limits |
| Main risks | Professional liability; sanctions screening | Global indirect tax; chargebacks; product liability from Dec 2026 | Unauthorised commitments; spend leakage |
| Administrative burden (INTERPRETATION) | **Low** if clients are non-EU (or Latvian, below €50k). **Medium** once any EU VAT-registered client is served | **Medium–high** (lower with MoR) | Low |
| Fit with shortlisted routes (v1.2) | R2 (O07), R4 (O13), R1 (O03); R3 (O02) deferred | O05 (kit), O06 (care plan) | All (cost base) |

### 15.9 Questions to take to an accountant or lawyer (⚖)

1. *(Answered from primary sources in v1.2; confirm before the first invoice.)* Given my expected client mix, should I use the s.139² special registration plus micro-enterprise tax, the self-employed general regime, or a full registration? At what client mix does full registration become cheaper? (**Blocks:** the first invoice. **Does not block:** investigating, or unpaid validation.)
2. Is my agent product an "electronically supplied service" (OSS, customer-country VAT) or a professional service (Latvian VAT for consumers)?
3. Which non-EU countries require registration for my digital sales, and is a merchant of record cheaper than registering myself?
4. Standard vs alternative CIT regime: what actually differs for my ownership structure?
5. For my contracts: liability caps, the product-liability exposure after 9 Dec 2026, and insurance.
6. Does any planned feature involve holding or forwarding client funds (PSD2/PSR licensing)?
7. Sanctions screening procedure, and whether any target customer group touches restricted jurisdictions.
8. GDPR: processor vs controller allocation, transfer impact assessment for US model providers, and retention policy for agent logs.

### 15.10 Verdict on the operating hypothesis

- **Supported (with conditions):** a Latvia-based SIA can sell agent services to businesses across the EU and in most non-EU countries, buy the necessary model and cloud services, and get paid through mainstream processors. EU VAT and GDPR frameworks are harmonised and workable for small operators.
- **Narrowed:** consumer-facing global SaaS is feasible but administratively heavier, and is usually best run through a merchant of record. Handling customers' funds, high-risk AI uses and sanctioned markets are **not** freely available.
- **Not shown:** that demand exists in any particular country. Worldwide reach is theoretical until validated (see the opportunity register).
