# Setup v2: the n8n pipeline, which model for which step, and what to install

*13 October 2026. Planning only: nothing has been installed, bought or run.*

This builds on [`agent-stack-plan.md`](agent-stack-plan.md), with n8n kept as the base. The owner asked two things:
- What are better model options for each job?
- Would more or fewer agents work better?

Costs come from [`stack_costs_v2.py`](stack_costs_v2.py) → [`stack_costs_v2_results.md`](stack_costs_v2_results.md).

---

## 1. Short answers

| Question | Answer |
|---|---|
| **More or fewer agents?** | **Fewer free-roaming agents, more fixed steps.** That means 6 focused AI steps, several plain-code steps, and you at 3 checkpoints. It does not mean 10+ agents talking to each other. See the reasons below. |
| **Which models?** | One model per step, chosen by a **small test** on 20 rules with known answers. A shortlist for each step is in §3. The suggested starting mix is Opus for the rule list, Gemini Flash to find, Qwen Plus to extract, Haiku to check, Sonnet for real-world context, Opus to compare and GPT to verify. |
| **AI cost** | About **€590 for one full run** of 100 rules × 10 jurisdictions (range €170–€2,000) [Calculation]. The cheapest sensible mix costs about €330; the premium mix about €1,300. |
| **Cash for the first 3 months** | About **€1,700** in the base case (range €320–€5,100). That includes the server, an optional DeepL translation cross-check and an optional lawyer spot-check [Calculation]. |
| **Server** | One EU server with 4 CPU cores and 8 GB RAM runs everything (about €36/month) [S178]. No graphics card is needed. |
| **Time** | About **13 weeks part-time** at 10–15 hours a week (§7). |

**Why fewer agents** (Interpretation, based on the evidence):
- **Simplest working option first.** Anthropic's own guidance is to "find the simplest solution possible" [S001].
- **Agents that talk to each other are expensive.** Anthropic measured multi-agent systems using about **15× the tokens of a chat**. They fit broad research that splits into parallel strands, and are a poor fit where agents must share the same context [S183].
- **Most failures come from the design, not the model.** A study of over 1,600 multi-agent runs found most failures came from system design and from agents misunderstanding each other [S184].

Your work splits cleanly into rule × country jobs. A **fixed pipeline** running those jobs in parallel gives the benefit of many agents without agents talking to each other.

---

## 2. The process, v2

| # | Step | What it does | Who does it | Runs |
|---|---|---|---|---:|
| 0 | **Rule list** (EU first) | Reads the EU acts and proposes ~100 rules. For each: an ID, a plain-language description, and search words in every language. **You approve the list** | AI (strongest) + you | 100 |
| 1 | **Fetch** | Downloads the official text for each country from that country's official source (§5) | **Code** | 1,000 |
| 2 | **Find** | Locates the article(s) about rule X in the fetched law. If nothing is found, does a web search | AI (cheap, handles long texts) | 1,000 |
| 3 | **Extract + translate** | Writes the note: original quote, translation, article number, link, key values (e.g. "overtime = 2.0x"), date in force | AI (mid) | 1,000 |
| 4 | **Check** (the "supervisor") | **Code checks:** is the quote really on the linked page, does the link open, are all fields filled, is the value plausible? Then a small AI sanity check. On failure, retry once with a stronger model, otherwise **flag it to you** | Code + small AI | 1,000 |
| 5 | **Real-world context** | Looks for official evidence of how the rule works in practice: collective agreements, agency guidance, enforcement. It must cite a source, otherwise it writes "not found" | AI with web search | 100 |
| 6 | **Compare** | Takes all 10 notes and the context, and writes what is the same, what differs and what it affects | AI (strongest) | 100 |
| 7 | **Verify** | A model **from another company** first answers the key questions on its own, without seeing the comparer's answer. Any disagreement is flagged to you | AI (strong, different company) | 100 |
| 8 | **Page + QA + PDF** | Fills the one-page template. Code checks every link and quote; a small AI re-reads the page; the PDF is generated | Code + small AI | 100 |

**What changed from your version:**
- **"One agent per language"** becomes **one reader template** run for each country with that country's language settings. The steps are identical, so one design is easier to fix. You can still give one language a different model if the test shows it reads that language better.
- **The supervisor is mostly code.** Each step is short and fixed, so nothing has time to "wander off". Code catches broken links and invented quotes for certain. The AI part only checks sense. You get a message when something fails.
- **Added:**
  - the rule-list step, so you approve what gets searched;
  - a separate fetch step from official sources, so readers never guess where the law is;
  - a separate real-world context step, so "in practice" claims need a source;
  - an **independent** verifier, which answers first and compares afterwards, instead of just "checking" the comparer.
- **Your 3 checkpoints:**
  - approve the rule list;
  - handle flagged items;
  - spot-check about 10% of the final pages.

---

## 3. Model options for each step

Prices are USD per million tokens (input / output). "Suggested" is where to start; the final pick comes from the test in §8.

| Step | Suggested | Also worth testing | Why |
|---|---|---|---|
| 0 Rule list | **Claude Opus 5.5** $4 / $20 [S044] | GPT-5.5 $5 / $30 [S045]; Gemini 3.1 Pro $2 / $12 [S046] | Runs once per rule, so the best model is cheap here |
| 2 Find | **Gemini 3 Flash** $0.50 / $3 [S046] | DeepSeek Flash $0.30 / $1.20 (half off-peak) [S173]; Mistral Large $0.50 / $1.50 [S181] | Reads long laws 1,000 times, so it must be cheap |
| 3 Extract + translate | **Qwen 3.7 Plus** $0.40 / $1.60 [S174] | Mistral Large (French company); Claude Sonnet 5.5 $2 / $10 | Quality in each language is what matters, so test it per language |
| 4 Check (AI part) | **Claude Haiku 5.5** $0.10 / $0.50 [S044] | Qwen 3.8 Flash $0.15 / $0.47 [S174]; GLM 5.3 Flash about $0.15 / $0.50 (unverified price) [S201] | Small yes/no job |
| 5 Real-world context | **Claude Sonnet 5.5** + Brave Search ($5 per 1,000 searches) [S200] | Gemini with Google Search grounding (5,000 free a month, then $14 per 1,000) [S046] | Needs careful searching and citing |
| 6 Compare | **Claude Opus 5.5** | GPT-5.5; Gemini 3.1 Pro; Qwen 3.8 Max $2 / $6 [S174] | The hardest reasoning; only 100 runs |
| 7 Verify | **GPT-5.5** | Gemini 3.1 Pro | **Must be from a different company** than the comparer |
| 8 Page QA | **Claude Haiku 5.5** | Qwen 3.8 Flash | Simple re-read |

**Specialist tools, not general chat models:**
- **DeepL API (translation).** A European company. It supports Latvian, Estonian, Lithuanian, Polish, Swedish, Dutch, Spanish, French and German, **with glossaries** so legal terms are translated the same way every time [S185]. Pro texts are deleted after translation [S186]. It costs about €22–28 per million characters; prices are third-party and conflicting [S186]. Translating every extracted rule once is about €250 in the base case. Best used as a **second translation** to catch AI translation drift.
- **TildeOpen (Latvia).** An open model for 34 European languages, with a strong focus on Latvian. The released model is a raw base model, not yet tuned to follow instructions, so it is not ready to be an agent [S187]. Tilde's translation platform built on it could be a Baltic-language translation check.
- **Search and extraction APIs** for the find and context steps, when official sources fail:
  - Brave Search API: $5 per 1,000 searches, with a $5 free monthly credit.
  - Tavily: 1,000 free credits a month, then $0.008 per credit.
  - Firecrawl: turns web pages into clean text; about $99 a month for 100,000 credits [S200].
- **Embeddings** (optional) help find the right article inside a long law by meaning. They are cheap: OpenAI's small model costs $0.02 per million tokens, Cohere's multilingual v4 about $0.12 [S202].
- **How to choose for each language.** EuroEval publishes model leaderboards for 30+ European languages [S188]. Use it to pick candidates, then confirm with your own test.

**Cost of the main mixes for one full run** (EUR; low / **base** / high; Calculation):

| Mix | Find / Extract | Compare / Verify | Low | Base | High |
|---|---|---|---:|---:|---:|
| **Suggested** | Gemini 3 Flash / Qwen 3.7 Plus | Opus / GPT-5.5 | 170 | **594** | 1,998 |
| EU-leaning | Mistral Large / Mistral Large | Opus / Gemini 3.1 Pro | 147 | **517** | 1,757 |
| Cheapest sensible | DeepSeek Flash / Qwen 3.7 Plus | Qwen 3.8 Max / Gemini 3.1 Pro | 91 | **326** | 1,097 |
| Premium | Sonnet / Sonnet | Opus / GPT-5.5 | 361 | **1,297** | 4,549 |

All of these are small next to the value of your time. So pick by **quality in the test**, not by price.

---

## 4. Cash budget, first 3 months (EUR; Calculation)

| Item | Low | Base | High |
|---|---:|---:|---:|
| AI usage: one full run (suggested mix) + 50% for tests and the model test | 256 | 891 | 2,996 |
| Server (4 vCPU / 8 GB, about €36/month) [S178] | 62 | 110 | 110 |
| Domain name for the server (HTTPS address) | 0 | 15 | 15 |
| Optional DeepL translation cross-check [S186] | 0 | 250 | 500 |
| Optional lawyer spot-check | 0 | 450 | 1,500 |
| **Total** | **317** | **1,715** | **5,121** |

n8n is free when self-hosted [S177]. Set a **spending limit in OpenRouter** [S176].

---

## 5. Where the law texts come from

| Jurisdiction | Official source | Machine access | Confidence |
|---|---|---|---|
| EU | EUR-Lex / Cellar | Public SPARQL and REST interfaces; **we used both this week** [S142] | High |
| Latvia | likumi.lv; TAP explanatory notes | Website (gentle, rate-limited); TAP notes as CC0 open data [S146][S150] | High |
| Poland | ISAP / Sejm ELI API | Official API with OpenAPI docs [S192] | Medium-high |
| Sweden | Riksdagen open data (SFS) | Free documents API [S193] | Medium |
| Netherlands | wetten.overheid.nl (BWB) | CC-0 open data plus the SRU search service [S194] | Medium |
| Spain | BOE | Open-data API [S197] | Medium |
| France | Légifrance | Free reuse; the API needs a free **PISTE** key [S196] | Medium |
| Germany | NeuRIS (rechtsinformationen.bund.de) | Official but **beta and incomplete** [S195]; gesetze-im-internet.de was unreachable once (HTTP 503) | Low-medium |
| Estonia | Riigi Teataja | Official and free, but **no API found**, so website or manual download [S198] | Medium |
| All countries | **N-Lex** (EU gateway to national law databases, with automatic translation) | Search one or several countries at once; useful for lookups [S199] | Medium-high |

Community-built connectors (MCP servers) for German, Swedish and Polish law also exist [S192][S193][S195]; n8n would call them as tools. They are not official, so test them before relying on them.

---

## 6. The n8n setup: what to install and build

### 6.1 One server, run with Docker Compose

| Part | Job |
|---|---|
| **n8n main** | The editor you open in your browser; starts workflows |
| **n8n workers** (2) | Run the jobs in parallel ("queue mode") [S190] |
| **PostgreSQL** | The database: rules, notes, findings, checks. n8n 2.0 recommends Postgres; queue mode requires it [S189][S190] |
| **Redis** | The job queue used by queue mode [S190] |
| **Gotenberg** (or pandoc) | Turns the HTML pages into the PDF, called over HTTP |
| **Caddy** | Gives the server an HTTPS address so you can log in safely |
| Optional: Qdrant or pgvector | Storage for embeddings, if used |

**Important n8n 2.0 defaults** [S189]:
- The "Execute Command" node is **off by default**. That is why the PDF is made by a separate converter called over HTTP, not by running commands.
- Code nodes run isolated and cannot read server secrets.
- **Back up the n8n encryption key.** Losing it loses all saved credentials [S190].

### 6.2 Accounts and keys

- **OpenRouter**: one key for all models, with a spending limit [S176].
- **Search**: Brave Search API or Tavily [S200].
- **GitHub**: a private repository for the notes folder, which opens in Obsidian.
- **Alerts and approvals**: a Telegram bot or email. n8n can pause until you reply ("send and wait") [S191].
- **France**: a free PISTE key for Légifrance [S196].
- **Optional**: DeepL API [S185].

### 6.3 Workflows to build in n8n

| Workflow | Main n8n parts |
|---|---|
| W0 Rule list | Manual trigger → AI Agent (Opus) → Postgres → send-and-wait for your approval |
| W1 Dispatcher | Loops over rules × countries and starts W2 as a sub-workflow, with a limit on parallel jobs |
| W2 Reader (sub-workflow) | HTTP Request (country source) → AI (find) → AI (extract, structured output) → Code (checks) → retry or flag → Postgres + GitHub note |
| W3 Context | AI Agent with a search tool, per rule |
| W4 Compare | AI per rule, reading all 10 notes |
| W5 Verify | AI from another company → Code compares the two answers → flag disagreements |
| W6 Page + QA | Code (template, link checks) → AI re-read → GitHub |
| W7 PDF | HTTP Request to Gotenberg → PDF saved and sent to you |
| W8 Error handler | Error trigger → message to you |
| W9 **Test runner** | Runs the 20 known rules and scores them. Re-run it after every change and every model switch |

### 6.4 The notes folder (your Obsidian "mind map")

```
vault/
  rules/R017-overtime-pay.md        ← one note per rule; links to every country note
  countries/R017/EU.md, LV.md, DE.md, NL.md, ...   ← quote, translation, article, link, values, date
  findings/R017.md                  ← comparison, real-world effects, verifier result
  pdf/R017.pdf                      ← the final page
```

Opening `vault/` in Obsidian shows the rules and countries as a linked graph.

---

## 7. Timeline (part-time, 10–15 h a week)

| Weeks | Work |
|---|---|
| 1–2 | Rent the server and install the stack (§6.1); open the accounts (§6.2). Run W0 to draft the ~100-rule list, and approve it |
| 3–4 | Build W2 for the **EU + Latvia + 1 country**. Test on overtime pay |
| 5–6 | Add the fetch step for the other 7 countries, one at a time. Run 1 rule across all 10 |
| 7–8 | **Model test** (§8). Choose a model for each step and language |
| 9–11 | **Full run** of 100 rules. Handle flags |
| 12–13 | Context, compare, verify, pages, PDF. Spot-check 10% |

**About 13 weeks.** The biggest risk to the timeline is country websites without good machine access (Germany beta, Estonia without an API).

---

## 8. The model test (do this before the full run)

1. Pick **20 rules where the answer can be checked**, for example: overtime pay, the 48-hour week, annual leave, the nitrate limit, fur-farming bans.
2. For each step, run **2–3 candidate models** from §3 on the same 20 rules × 10 jurisdictions.
3. Score each one:
   - Is the quote really in the official text?
   - Is it the right article?
   - Is the key value correct?
   - Is the translation faithful? Check this against DeepL.
4. Pick the **cheapest model that passes** for each step. Use the best one for comparing and verifying.
5. Save the 20 rules as the permanent test set (W9), and re-run it whenever you change something.
