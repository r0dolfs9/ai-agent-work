# Project brief — The AI Agent Ecosystem and Its Emerging Market

Created: 2026-10-12 · Owner: repository owner (r0dolfs9/ai-agent-work) · Lead executor: Claude Code (cloud session)

## 1. Objective

Produce a comprehensive, accessible, evidence-based research paper that explains the AI agent ecosystem to someone who wants to (a) understand it, (b) start using agents, (c) build with them, or (d) build a business serving this market. Alongside it, maintain a searchable, evidence-linked business-opportunity register.

## 2. Intake status

The repository `r0dolfs9/ai-agent-work` was supplied and is checked out on branch `claude/amazing-archimedes-w4pw0c`. At intake it was **empty** (no commits, no files, no CLAUDE.md or other instructions). There was no existing project material to preserve.

None of the intake questions had been answered at kickoff. None of them blocks research, so work went ahead on the labelled assumptions below. The open questions are in the [question backlog](#6-question-backlog).

| Intake item | Status | Working assumption (ASSUMPTION) |
|---|---|---|
| Audience and technical level | Not specified | Informed nontechnical reader (manager, founder, analyst). Technical depth goes in appendices. |
| Geography / jurisdictions | Not specified | Global. Regional differences are called out explicitly for the US, EU, UK and China where evidence exists. |
| Focus segments | Not specified | All: enterprise agents, personal assistants, coding agents, commerce agents, autonomous services. |
| Length / language / format | Not specified | English Markdown. Main paper about 15–25k words plus appendices. Converts to PDF/DOCX with pandoc on request. |
| Deadline | Not specified | No hard deadline. Work in checkpointed milestones. |
| Research budget | Not specified | Zero spend. Public web sources only. No paid databases, subscriptions or purchases. |
| Purpose | Not specified | Private learning plus business development. **Not** an investment recommendation. |
| Available data / existing research | None found in repo | Public sources only. |
| Authorized tools | Session tools | Web search, web fetch, local files, git push to the designated branch (see `project/capabilities.md`). |

## 2a. Intake answers confirmed by the owner (v1.1, 2026-10-12)

| Item | Confirmed answer |
|---|---|
| Purpose | Private learning and business development. Not for publication or investors. Rigorous evidence standards retained |
| Market scope | Global |
| EU / Latvia | Deeper treatment only where location materially affects operating a global agent business: establishment, costs, taxes, invoicing, payments, legal obligations, privacy, access restrictions, cross-border operations. Latvian demand and market size are **not** prioritised |
| Working hypothesis to test | "An operator based in Latvia can serve customers internationally through agents." Not to be read as unrestricted global trading |

The assumptions in §2 for audience, format, language and budget remain in force.

## 3. Scope

**Included:** definitions; architecture; operation; security; costs; access to sites and services; standards and protocols; purchasing and payments; activity and timing; audits, governance and enforcement; market sizing claims; business opportunities.

**Excluded:**
- Purchasing services, opening accounts or trials, and contacting vendors or people.
- Running live agents against third-party sites to "test" them.
- Security testing of any third-party system.
- Any evasion of platform enforcement.
- Legal advice. Regulatory content is descriptive only.

**Blocked or limited:**
- Paywalled analyst reports (Gartner, Forrester, IDC full text). Only their public press releases and summaries are used.
- Private telemetry from vendors.
- Customer interviews, which need the owner's approval to contact people.

## 4. Authorization boundaries (from the assignment)

- Authorized: read-only investigation, analysis, drafting, reversible local artifacts, and commits and pushes to the designated branch.
- Requires explicit approval: spending money, subscriptions, credential or account changes, destructive operations, contacting real people, publishing (including creating a public artifact or a PR), deployment.
- Pushing to the designated branch of the supplied repository is the assignment's specified delivery mechanism. It is **not** treated as publication. The repository's visibility is UNKNOWN, so the owner should check it before sharing.

## 5. Acceptance criteria (measurable)

| # | Criterion | Measure |
|---|---|---|
| AC1 | Topic coverage | All 9 research areas in §5 of the assignment have a paper section, or an explicit gap entry in the coverage matrix. |
| AC2 | Traceability | Every material quantitative or factual claim in the paper carries a source ID `[S###]` that resolves in `research/sources.csv`, which records URL, publisher, publication date where known and retrieval date. |
| AC3 | Evidence labels | Load-bearing claims in the claim ledger are tagged VERIFIED FACT / CALCULATION / ASSUMPTION / INTERPRETATION / RECOMMENDATION / UNKNOWN. The paper marks interpretation and recommendation explicitly. |
| AC4 | Cost models | Three scenarios (personal, small business, production), each with low/base/high cases. Inputs are dated prices, every assumption is explicit, the model reproduces from `models/cost_model.py`, and it includes cost per successful outcome and a sensitivity analysis. |
| AC5 | Opportunity register | At least 10 opportunities with every field required by assignment §6, scored on a consistent rubric with evidence visible, and no fabricated demand. |
| AC6 | Conflicts | Contradictory evidence is recorded in the claim ledger for every material conflict found. |
| AC7 | Adversarial review | A documented skeptical self-review pass is in `verification/verification-report.md`, and critical findings are fixed. |
| AC8 | Readability | Executive summary, glossary and plain-language explanations. Jargon is defined at first use. |
| AC9 | Handoff | HANDOFF block present. Everything is committed and pushed to the designated branch. |

## 6. Question backlog

Ask a maximum of two at a time. Ranked by impact.

1. **Purpose and audience:** Is the paper for private learning and business development (assumed), or for publication or investors? This changes the tone, the citation format and the legal review.
2. **Geography:** Should any jurisdiction (for example EU/Latvia, US) get deeper treatment? The owner's context suggests Baltic/EU relevance (UNKNOWN). This affects VAT, regulatory and payments sections.
3. Target length and format (Markdown vs DOCX/PDF vs web page).
4. Does the owner have a preferred business direction (services vs software vs content) or budget for validation experiments?
5. May validation experiments in the opportunity register be run later? Many need spending or contact with people, so each would need approval.
6. Is there access to any paid data source (Gartner, CB Insights, Similarweb) or to the owner's own agent usage logs?
