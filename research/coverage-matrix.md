# Coverage matrix

Each research area from the assignment is mapped to its research questions, key sources, evidence strength, paper sections and unresolved gaps. Strength ratings:
- **Strong:** primary, multiple, or independent sources.
- **Moderate:** primary but vendor-sourced, or a single independent source.
- **Weak:** secondary only, or conflicting sources.
- **Gap:** no adequate public evidence.

| Area / topic | RQ | Key sources | Evidence strength | Paper section | Unresolved gaps |
|---|---|---|---|---|---|
| Agent vs chatbot/workflow/automation/software | RQ1 | S001, S006 | Strong (definitions are conventions) | §1.1 | No regulator-adopted definition used. EU AI Act "AI system" definition not analysed |
| Autonomy levels & human role | RQ2 | S002, S080, S079 | Strong | §1.2–1.3 | No empirical distribution of deployments by level |
| Categories, providers, platforms, marketplaces, infrastructure | RQ3 | S013, S053–S055, S062, S071, S023–S026, S024, S028 | Moderate | §2.1 | No systematic vendor census (e.g., AI Agent Index not reviewed) |
| Operational use vs demos/marketing | RQ4 | S003–S006, S062, S037, S021–S022 | Moderate (surveys disagree, C001) | §2.2–2.3 | Independent production resolution rates (U01) |
| Models, loop, tools, memory, state, orchestration, multi-agent | RQ5 | S001, S032, S036, S044, S080 | Strong | §3.1–3.3, App. A | — |
| APIs, browser/computer control, connectors, triggers, scheduling | RQ5, RQ10 | S044, S068, S079, S080, S032 | Strong | §1.3, §3.2, §7.2 | Reliability of computer use vs APIs not quantified |
| Identity, auth, permissions, secrets, sandboxing, approval | RQ6 | S050, S060, S032, S016, S080, S063 | Moderate (standards immature) | §3.4, App. B | Final NIST/IETF standards pending |
| Failure modes & incidents | RQ7 | S010–S014, S039, S068, S069, S081, S072 | Strong for existence; weak for frequencies | §3.5, §5 | Incident base rates. CVEs not verified against NVD |
| Reliability/capability | RQ8 | S008, S009, S037, S038, S070 | Strong | §4 | Domain-specific reliability outside software/freelance |
| Hosted/self-hosted/hybrid; cost components | RQ9 | S044–S048, S077, S078 | Strong (prices); moderate (labour) | §6.1–6.2, §6.7 | Open-weight self-hosting not costed |
| Cost models (personal, SMB, production), sensitivity, cost per success | RQ9 | models/*, S044–S047, S071, S077, S078 | CALCULATION on stated assumptions | §6.3–6.6 | G-COST-1/2/3: engineering effort, security budgets, resolution rates |
| Which services agents use; reachable/supported/permitted/observed | RQ10 | S015–S019, S023, S025, S063–S065, S075, S076 | Moderate | §7 | Systematic ToS survey across top 100 sites not done |
| Platform dependence, switching costs | RQ10 | S016, S025, S032, S019, S075 | Moderate | §7.3 | — |
| Standards status & compatibility | RQ11 | S020–S026, S028, S032–S036, S059, S060 | Strong (spec texts) / moderate (adoption) | §8, App. A | AP2 spec not read directly. ACP/UCP spec texts not read in full |
| Economic buyer, what agents bought, payment mechanics, approvals | RQ12 | S021–S028, S035, S040, S065, S080 | Moderate | §9.1–9.4 | U02: total agent-completed purchase value |
| Spending limits, subscriptions, refunds, disputes, liability | RQ12 | S026, S066, S080 | Weak (liability) | §9.4 | U06: network dispute rules |
| Vendor selection, negotiation, acceptance, refusal; stable preference? | RQ13 | S029, S030, S039, S040 | Strong (controlled) / moderate (generalisation) | §9.5 | Refusal rates in live deployments |
| Consumer willingness to delegate purchases | RQ13 | S067 | Weak–moderate (stated preferences; C009) | §9.6 | Revealed-preference data |
| Activity by time, geography, use case, deployment type | RQ14 | S041–S043, S079, S080 | Moderate for chat; gap for autonomous agents | §10 | U03: hourly/weekday patterns of autonomous agents and purchases |
| Evaluation, trace inspection, permission review, reconciliation, security testing, compliance, incident response | RQ15 | S037, S048, S051, S061, S073 | Moderate | §11.1 | Who audits in practice (no survey found) |
| Regulation & frameworks | RQ15 | S049–S052, S074, S013 | Strong (EU), moderate (others) | §11.2, §11.4, App. C | National enforcement priorities |
| Platform suspension/ban rules, incidents, appeals, prevention | RQ16 | S015–S019, S063–S065, S075, S076 | Moderate (policy) / weak (frequency) | §11.3 | U04: ban counts and appeal success rates |
| Buyers, budgets, distribution, procurement barriers, competition | RQ17–18 | S004–S007, S053–S058, S062 | Moderate | §12 | U07: budgets earmarked for agent tooling |
| Market size & growth claims, with methodology | RQ17 | S056–S058, S007 | Weak (forecasts) / moderate (company data) | §12.1 | Paywalled methods |
| Opportunities (infra, integrations, monitoring, eval, security, identity, payments, data, services) | RQ18 | opportunities/* (all cite S-IDs) | Hypotheses | §12.4, register | No customer validation (requires approval) |
| Selling to operators vs being selected by agents | RQ18 | S029, S030, S024, S028, S055 | Moderate | §12.3 | — |
| **Added during research:** platform credential policies for AI subscriptions | RQ16 | S016, S017, S075 | Moderate | §7.1, §11.3 | Added because it is a top practical risk for personal-agent users and builders |
| **Added:** agent insurance and certification | RQ15 | S061 | Weak | §11.1 | Added because risk transfer is an emerging cost and opportunity |
| **Added:** regional differences | RQ15 | S013, S022, S043, S049–S052 | Moderate | §11.4 | Baltic/EU commerce data gap |

## v1.1 additions (2026-10-12)

| Area / topic | Key sources | Evidence strength | Paper section | Remaining gaps |
|---|---|---|---|---|
| Adoption, EU official statistics and international qualitative | S096, S097, S084, S085, S098, S087 | Strong (EU stats), medium (surveys) | §2.2 | Agent-specific official statistics |
| Activity definitions and timing by trigger | S041, S092, S093 (own analysis), S043, S079, S080 | Medium (narrow populations) | §10 | Scheduled/continuous agent timing; purchase timing |
| Enforcement frequency (policy vs incidents vs rates) | S094, S095, S092, incident sources | Strong (policy/incidents), gap (rates) | §11.3.1 | Agent-specific numerator + denominator |
| Autonomous purchase value by autonomy level | S090, S091, S116, S115, S021, S022, S121 | Medium–strong (bounded examples) | §9.2 | Card-network agent volumes; global total |
| Transferability of conclusions by geography/provider | All | Interpretation | §11.4 | — |
| Latvia/EU establishment, tax, VAT, invoicing | S099, S100, S101, S102, S103 | Medium–high (statute translation outdated) | §15.2–15.4 | Current VAT Law text; accountant costs |
| Payments, MoR, currencies, refunds | S104, S105, S113, ECB FX | High (prices) | §15.4 | MoR seller eligibility for Latvia |
| Provider availability, sanctions | S106, S112 | High | §15.1, §15.7 | Provider terms on serving unsupported regions |
| GDPR roles and transfers | S109, S110 | Medium | §15.5 | DPF appeal outcome (C-703/25 P) |
| AI Act roles and dates | S107, S108, S074 | High | §15.6 | National enforcement priorities |
| Liability, delegated authority, payment licensing | S111, S114 | Medium | §15.7 | Agent-authority law (UNKNOWN) |
| Operator economics model | models/operator_economics.py | CALCULATION | §6.9, §15 | Non-EU taxes not modelled |
| Labour-cost jurisdiction sensitivity | S119 | CALCULATION on official stats | §6.9 | Occupation-specific EU wages |
