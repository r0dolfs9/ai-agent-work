# I. Legal-quality, risk, security and product plan

*14 October 2026. This plan supports research. **Nothing produced by the system is legal advice**, and nothing in this document is legal advice either.*

## I.1 Kinds of authority: never merge them

| Type | What it is | How the system treats it |
|---|---|---|
| **Binding legislation** | EU regulations/directives (via national transposition); national acts and regulations as published in the official journal | The only basis for a "the law says" answer. Cite the official publication; a consolidated text is a convenience copy unless it is itself official (Estonia [S14]) |
| **Regional rules** | Acts of regions/Länder/autonomous communities (ES, DE, IT) | A separate `territorial_level=regional` row; never averaged into the national answer |
| **Collective agreements** | Sector agreements; binding on all employers only if extended (erga omnes) | Separate field `collective_agreement_note`; the page says whether it is generally binding (e.g. LV Art 68(3) general agreements [S15]; FR KALI [S22]) |
| **Court decisions** | CJEU and national supreme-court interpretations | An interpretation layer with case reference; can change the reading of a statute (EMP-17) |
| **Official guidance** | Ministry and agency guidance, FAQs | Labelled "guidance, not binding"; used for practical context and to resolve ambiguity, never as the answer to "what is the law" |
| **Administrative practice** | How inspectorates actually enforce | Only from official reports; labelled; low weight |
| **AI interpretation** | Model-generated reading, translation or comparison | Always labelled; never the sole basis of a released statement |
| **Practical examples** | Worked farm scenarios | Labelled INTERPRETATION; reviewed by a person with farm knowledge |

## I.2 Layered verification

| Layer | Check | Automated? | Blocks release? |
|---|---|---|---|
| V1 Schema | Record validates against `cell-record.schema.json` | Yes | Yes |
| V2 Source-to-claim | Each `exact_excerpt` is a byte-exact substring of the cited snapshot; each locator resolves; each URL returns 200 at build time | Yes | Yes |
| V3 Date and amendment | `effective_from` ≤ reference date < `effective_to`; no amending act in the change feed after the snapshot; snapshot age ≤ 30 days at release (or change feed confirmed silent) | Yes where a feed exists (ES, EE, PL, DK, EU SPARQL); manual otherwise | Yes |
| V4 Challenger model | A model from another provider tries to refute each cell; disagreement → escalation | Yes | Disagreement blocks until resolved |
| V5 Researcher review | A person reads the source for every cell before `human-reviewed` | No | Yes (internal release) |
| V6 Subject expert | Farm/labour/vet expert checks practical examples and plausibility | No | Practical section only |
| V7 Qualified lawyer | Jurisdiction-qualified lawyer reviews the sample or the full set (I.4) | No | Yes for the client product |
| V8 Conflict escalation | Any source conflict, e.g. secondary vs official, or two official versions, is logged in `open_issues` and shown on the page until resolved | Partly | Unresolved material conflict blocks a definitive answer; the page shows "conflict" instead |

**Release-blocking errors** (any one stops a page):
- any critical flag (wrong jurisdiction, outdated law, missing material exception, false citation, reversed obligation, wrong threshold, unjustified certainty)
- V1–V3 failure
- missing effective date
- a cell below `human-reviewed`
- an unresolved challenger disagreement
- a secondary source cited as the authority

## I.3 Correction and version history

- Pages carry a version ID (`page_id@build_hash`) and "last checked" date per cell.
- A correction creates a new `CellAnswer` that supersedes the old one, never edits it. The page's change log lists the superseded value, the date and the reason.
- Released PDFs are immutable. Corrections produce a new PDF version, and a public product keeps a corrections list.

## I.4 How much lawyer review, and what it proves

**Statistics (CALCULATION, rule of three).** If n independently sampled cells contain 0 critical errors, the 95 % upper confidence bound on the critical-error rate is ≈ 3/n:

| Cells reviewed per layer | Bound if 0 errors found |
|---|---|
| 10 | ≈ 30 % |
| 30 | ≈ 10 % |
| 60 | ≈ 5 % |
| 100 (whole layer) | ≈ 3 % (and the unchecked remainder is 0) |

**Spot-checking does not validate the unchecked pages.** At realistic volumes (~100 cells per layer) it can only show whether errors are rare or common, and it bounds that rate loosely. A clean spot-check of 10 cells is consistent with 1 in 4 pages being wrong.

**Recommendations:**

| Stage | Lawyer review | Purpose |
|---|---|---|
| Pilot | 2 cells per layer = **20 cells**, chosen from trap cases (T1–T8) | Find *systematic* misreadings (wrong source type, ignored agreements, outdated texts). Not a quality certificate |
| Internal 100-question build | **10 random cells per layer (100)** + every cell the challenger or researcher flagged | Bound the overall rate (0 errors in 100 → ≤ ~3 % pooled, but only ~30 % per layer) |
| Client-facing product | **Every released cell** in each jurisdiction sold, by a lawyer qualified there, or the product is explicitly sold as an unreviewed research summary with that label on every page | Liability; a client will act on the page |

## I.5 Security and privacy controls

| Control | Private research | Internal company tool | Client-facing research product | Publicly distributed PDF |
|---|---|---|---|---|
| Secrets (API keys) in an OS keychain / `.env` outside git, git-secrets scan | **Required now** | Required | Secret manager | Required |
| Spending caps on every model account | **Required at the first account** | Required | Required | Required |
| Least privilege (separate keys per stage; read-only tokens for fetchers) | Later | Required | Required | — |
| Server hardening (SSH keys only, firewall, auto-updates) | n/a (no server) | If a server exists | Required | — |
| Encryption at rest | Disk encryption on the PC | Required | Required + backups encrypted | — |
| Backups | git remote + one offline copy | Scheduled | Scheduled + **restore test quarterly** | Archive each release |
| Dependency updates | Monthly `pip` check | Automated alerts | Automated + review | — |
| Monitoring / audit log | Run log (model, provider, tokens, cost) | + access log | + audit log of every review decision (already in the `Review` records) | — |
| Incident response | Note what to do if a key leaks: revoke, rotate, check spend | Written 1-page runbook | Runbook + client notification duty | Correction notice |
| GDPR | Reviewer names are personal data; keep them in the review log, not in a public PDF | Internal privacy notice | Data-protection terms with clients; processor terms with model providers (OpenAI ZDR requires approval [S46]; Anthropic 30-day default [S45]) | Avoid personal data in examples |
| Copyright / database rights on sources | Store snapshots privately; cite and link | Same | **Check reuse terms per source** before republishing excerpts: BOE requires an "informative" label [S24]; FR Licence Ouverte 2.0 [S21]; SE free with attribution [S17]; NL CC0 for KOOP datasets [S27]; **EE, LV, PL terms not found = UNKNOWN** | Same, stricter: excerpts only, attributed |
| Client confidentiality | n/a | n/a | No client data in prompts unless the provider route is ZDR | n/a |
| AI crawling restrictions | Respect robots.txt: **never crawl wetten.overheid.nl with an AI agent** [S26]; use official APIs | Same | Same | — |

**Can wait until after the pilot:** least-privilege key separation, server hardening, scheduled backups, client terms, insurance, accessibility audit.

**Required from day one of any model use:**
- secrets out of git
- spending caps
- run logging
- ZDR/no-training routing
- no personal or client data in prompts
- private storage of snapshots
- respecting robots and terms

## I.6 Client-product caveats (must appear on every page of a sold product)

1. "Research summary. Not legal advice. Check the official source before acting."
2. Verification badge and last-checked date per jurisdiction.
3. Reviewer type: researcher, subject expert or lawyer (with jurisdiction).
4. Collective-agreement and regional caveats wherever they apply.
5. A link to the official publication, not only to a consolidated convenience copy.
