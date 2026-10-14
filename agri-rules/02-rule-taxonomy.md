# C. Rule taxonomy and proposed rule lists

*14 October 2026. Machine-readable list: [`rules/rule-list.csv`](rules/rule-list.csv) (100 rows, validated: unique IDs, ranks 1–100, 20 pilot rows).*

**Labelling of the list's `eu_baseline` column:**
- An entry with an [S##] tag was **VERIFIED** in the source this session.
- Every other EU instrument named there is an **ASSUMPTION from background knowledge**. Each one must be checked against Cellar/EUR-Lex while the gold standard is prepared, and no page may cite it until then.

## C.1 What "100 farming rules" should mean (premise audit)

**Finding (INTERPRETATION):** "100 rules" is not a well-defined unit.
- A "rule" like *agricultural overtime* fans out into several questions: the cap, the premium, consent, the reference period and record-keeping.
- Each of those answers changes with the employee category, any collective agreement, the date and sometimes the region.

Counting "rules" therefore hides the real workload.

**Recommendation:** redefine the unit as a **comparison question**: one precisely worded question with a fixed *answer type*, a fixed *scope* (who or what it applies to) and a *reference date*.
- **Layer** = one jurisdiction answering one question.
- **Cell** = one question × one layer.

100 questions × 10 layers = **1,000 cells**, which is what costs, time and review are counted in.

**Rules for writing a question:**
1. It must be answerable by a value of a stated type (hours, kg N/ha, yes/no + date, …) **or** by "no binding rule", which is a valid answer that must be evidenced.
2. It names the default scope (e.g. "adult, non-family farm employee, no collective agreement"). Deviations are recorded as variants, never merged into the default answer.
3. It carries a reference date. Answers are "as in force on YYYY-MM-DD", with future changes shown separately.

## C.2 Domain analysis

| Domain (code) | Where the rules mainly live | Meaningful comparison? | Must distinguish | Risk of comparing unlike concepts |
|---|---|---|---|---|
| Employment: working time, pay, leave, seasonal (EMP) | EU minimum directives + national law + **collective agreements** (dominant in SE, FR, IT, DK; important in DE, NL) | **Yes for statutory floors**; partial for pay | Employee vs self-employed vs family member; seasonal vs permanent; third-country seasonal; young workers; piece-rate | **High.** A "statutory 0 %" overtime premium (DE) next to "100 %" (LV) misleads unless the collective-agreement layer is shown |
| Occupational safety (OSH) | EU framework + individual directives; national enforcement | Yes for exposure limits and duties | Employee vs self-employed farmer | Medium. Many duties don't apply to the self-employed |
| CAP conditionality (CAP) | EU regulation sets the GAEC/SMR frame; national CAP Strategic Plans set the standards | Yes, if the **consolidated** EU text and the current national plan are used | Farm size (small-farmer exemption), land type | **High amendment risk:** GAEC changed in 2024 and again in the 2025–26 simplification [S05, S54] |
| Nitrates/water (NIT) | EU directive + national action programmes + derogations | Yes (170 kg N/ha is a harmonised ceiling [S02]) | Derogation farms; vulnerable zones; soil type | Medium. Derogation status changes by year (NL ended 2026 [S28]) |
| Pesticides (PPP) | EU directive and regulation + **product authorisations / labels** | Partly | Product-specific vs general rule | **High.** Buffer zones are often set per product label, not by a general rule |
| Fertiliser products (FER) | Optional EU harmonisation + national | Limited | CE-marked vs national products | Medium |
| Animal welfare (AW) | EU species directives (minimums) + stricter national rules + national bans | Yes; good for showing "gold-plating" | Species, production system, existing vs new farms (phase-outs) | Medium. Phase-out dates must be shown, not just the end state |
| Veterinary/biosecurity (VET) | Mostly EU-harmonised regulations (Animal Health Law, vet medicines) | Low added value: largely identical | Zone status (ASF) | Low; risk of 10 identical pages |
| Organic (ORG) | EU regulation, almost fully harmonised | Low added value | — | Low; candidate for exclusion |
| Land use/ownership (LAND) | National (constitutional and Treaty limits) | Yes; highly distinctive | Buyer type, area | Medium |
| Records/inspections (REC) | EU control regulations + national systems | Partly | — | Low |
| Agricultural tax and subsidy rates | National tax law; CAP payment rates in CAP Strategic Plans | Poor; changes yearly | Legal form, VAT schemes | **Very high.** **Excluded** (see C.3) |

## C.3 Inclusion and exclusion boundary

**Include** a question only if all four hold:
1. It is answerable from **binding law** (EU, national or regional), or from an **extended collective agreement** that is shown as such.
2. It affects a farm or farm employer's day-to-day operation or compliance.
3. At least 5 of the 10 layers can give a non-trivial answer.
4. The answer can be traced to an official source with a stable locator.

**Exclude:**
- tax rates and payment amounts (they change yearly and depend on the person)
- forestry, fisheries and aquaculture
- food processing beyond the farm gate
- rules that exist only as non-binding guidance (these may be *noted*, not compared)
- court decisions as the sole basis of a "rule". Case law is shown as an interpretation layer on top of a legislative question (EMP-17 is the test case).

**Optional / candidates to drop if the pilot shows low value:** ORG-01..05 and VET-01/02/07/08. They are near-identical across the EU, so 10 pages would repeat one answer. Better: one EU page with national deviations noted.

## C.4 Taxonomy (100 questions)

| Domain | Count | IDs | Notes |
|---|---|---|---|
| EMP | 20 | EMP-01..20 | Working time 10, pay 3, leave 2, seasonal and posted 4, youth 1 |
| AW | 14 | AW-01..14 | Bans, species standards, transport, slaughter |
| CAP | 12 | CAP-01..12 | GAEC 1–8, small farms, social conditionality, penalties |
| NIT | 10 | NIT-01..10 | |
| PPP | 10 | PPP-01..10 | |
| OSH | 8 | OSH-01..08 | |
| VET | 8 | VET-01..08 | |
| ORG | 5 | ORG-01..05 | |
| LAND | 5 | LAND-01..05 | |
| REC | 5 | REC-01..05 | |
| FER | 3 | FER-01..03 | |

**Ranking method (INTERPRETATION):** practical impact on a farm or employer × comparability × likelihood of real cross-country difference, ranked by judgement. Ranks 1–25 are mostly employment, nitrates and the high-salience animal-welfare questions. The full ranked list is in the CSV (`rank` column).

## C.5 Ranked 20-question pilot (balanced)

Selected for balance across domains, answer types and difficulty, not purely by rank. There are 6 employment questions, the core of the examples in the brief.

| # | ID | Question (short) | Domain | Why in the pilot |
|---|---|---|---|---|
| 1 | NIT-01 | Max manure N per ha | NIT | Harmonised EU number + derogations (trap T3) |
| 2 | EMP-01 | Max average weekly hours | EMP | Clean EU baseline (48 h) [S01] |
| 3 | EMP-11 | Minimum annual leave | EMP | Unit trap (days vs weeks) |
| 4 | EMP-04 | Statutory overtime premium | EMP | Collective-agreement trap (T1) |
| 5 | EMP-02 | Working-time reference period in agriculture | EMP | Derogation chain (T2) |
| 6 | EMP-15 | Seasonal worker max stay | EMP | EU range, national choice [S03] |
| 7 | AW-01 | Fur-farming ban and date | AW | No EU baseline; dates; phase-outs (T4) |
| 8 | PPP-01 | Pesticide user certificate | PPP | Easy control case |
| 9 | CAP-01 | GAEC 4 buffer strip | CAP | Amendment + national standard (T5) |
| 10 | NIT-02 | Closed spreading periods | NIT | Many variants per soil/crop: tests structure |
| 11 | AW-08 | Broiler stocking density | AW | Numeric, EU tiers |
| 12 | VET-03 | Prophylactic antimicrobials | VET | Harmonised control case: expect identical answers |
| 13 | EMP-17 | Working-time recording duty | EMP | Court-decision layer (T6) |
| 14 | NIT-03 | Manure storage capacity | NIT | Numeric with species/zone variants |
| 15 | PPP-04 | Pesticide buffer zones to water | PPP | Product-label layer |
| 16 | CAP-08 | Small-farm conditionality exemption | CAP | Recent amendment |
| 17 | LAND-01 | Who may buy farmland | LAND | No EU baseline; national distinctiveness |
| 18 | AW-04 | Piglet castration without anaesthesia | AW | National bans over an EU minimum |
| 19 | REC-01 | Vet-medicine record retention | REC | Harmonised numeric control case |
| 20 | OSH-03 | Heat rules for outdoor work | OSH | Binding vs guidance (T7) |

## C.6 Trap cases

These are deliberately included to test whether the system says "it depends" correctly. Facts marked [S##] were verified this session. Everything else is a **hypothesis the gold standard must confirm or refute**.

| ID | Question | Why it is a trap | What a correct answer must show |
|---|---|---|---|
| **T1** | EMP-04 overtime premium | **Latvia:** statute says ≥100 %, but a sectoral general agreement meeting a wage condition may set ≥50 % (Darba likums Art 68(1) and (3)) [S15]. **Germany:** ArbZG sets hours limits [S10]; premiums are expected to come from collective agreements (hypothesis). | Separate statutory and collective-agreement values; flag "depends on agreement" |
| **T2** | EMP-02 reference period | EU allows agriculture to derogate from the 4-month reference period (Art 17(3)(c)(vii), (d)(i)) but caps it at 6 months, or 12 by collective agreement (Art 19) [S01]. National transposition differs. | EU cap + national choice + whether a collective agreement is needed |
| **T3** | NIT-01 manure N | The 170 kg N/ha ceiling is harmonised [S02]. **Netherlands:** derogation ended; no derogation from 2026 [S28]. A pre-2026 source says otherwise. | Date-stamped answer; superseded derogation shown as history |
| **T4** | AW-01 fur ban | No EU ban: the Commission's follow-up to "Fur Free Europe" was due by March 2026 [S32]; outcome UNKNOWN. **EE:** ban from 1 Jan 2026 [S31]. **LV:** from 1 Jan 2028 [S30]. **PL:** phase-out to 31 Dec 2033, rabbits excepted (secondary source [S29]). **ES:** regional initiative in Catalonia (news). | Status *and* effective date per layer; pending EU action flagged; secondary sources replaced by the official gazette |
| **T5** | CAP-01/03/04/08 GAEC | Regulation 2021/2115 amended in 2024 and again by the 2025–26 simplification [S54]. Cellar returns the **original** text for CELEX 32021R2115 [S05]. | Consolidated version with its date; amendment chain listed |
| **T6** | EMP-17 time recording | The obligation comes from a CJEU judgment (C-55/18) more than from directive text; national follow-up varies (hypothesis). | Labelled "court decision" layer, separate from legislation |
| **T7** | OSH-03 heat | In some states this is binding regulation, elsewhere official guidance only (hypothesis). | Binding / guidance / none, never merged |
| **T8** | AW-14 / EMP-14 Sweden | Rules may sit in agency regulations or collective agreements rather than SFS acts (hypothesis). | Source type recorded; "not in statute" is not "no rule" |
