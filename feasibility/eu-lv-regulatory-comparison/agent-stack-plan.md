# Plan: running the rule-comparison agents on a server, with a mix of AI models

*13 October 2026. Planning only: nothing has been set up, bought or run.*

> **Superseded by [`agent-setup-v2.md`](agent-setup-v2.md)**, which has fewer free-roaming agents and more fixed steps, more model options for each step, official law sources for each country, and the concrete n8n server setup. This file is kept for the history of the decision.

This follows the owner's description of the system:
- Reader agents, one per language, file the EU rules and the same rules in about 10 countries into a topic-sorted database.
- A supervisor keeps the readers on task.
- A comparer works out the differences and their real-world effects.
- A verifier checks the comparer.
- A final check confirms facts and links, then outputs a PDF with **one rule per page**.

The owner has no legal training, cannot run this on their own PC, and wants to pick a cheaper or stronger model for each job. Costs come from [`stack_costs.py`](stack_costs.py) → [`stack_costs_results.md`](stack_costs_results.md).

---

## 1. Short answers

| Question | Answer |
|---|---|
| **Where does it run?** | On a **rented server**, not your PC. The AI models run at the model companies, so the server needs **no graphics card (GPU)**. It only runs the workflow, stores the notes and makes the PDF. Your PC just opens a web page. |
| **What are Qwen and DeepSeek?** | Two Chinese AI model families. They are much cheaper than Claude or GPT, and good enough for some jobs. See §3. |
| **Can I choose a model per agent?** | Yes. **OpenRouter** gives one account and one bill for models from many companies, including Claude, GPT, Gemini, Qwen, DeepSeek and Mistral. **n8n** is a visual workflow builder in which each agent can use a different model. See §4. |
| **What does the AI cost?** | About **€630 for one full run** of 100 rules × 10 jurisdictions with a sensible mix of models (range €190–€2,100) [Calculation]. |
| **Total cash for the first 3 months** | About **€1,500** in the base case (range €350–€4,900). That covers AI, server and an optional lawyer spot-check [Calculation, §6]. |
| **Your time** | About **3 months part-time** (10–15 hours a week; range 2–5 months). Most of it goes on setup and on reading test results, not on waiting for agents (§7). |

---

## 2. What it would look like

```
                ┌───────── rented server (EU), runs 24/7 ─────────┐
 list of 100    │                                                   │
 rules + 10  ──►│ 1 READERS (one per language)                      │
 countries      │   find official text → quote → translate → note   │
                │   model: cheap/mid (e.g. Qwen Plus)               │
                │        │                                          │
                │ 2 SUPERVISOR checks every note                    │
                │   code: quote really on the linked page? link OK? │
                │   model: very cheap (e.g. DeepSeek Flash)         │
                │        ▼                                          │
                │   NOTES DATABASE (one note per rule per country,  │
                │   linked by topic → opens in Obsidian as a map)   │
                │        │                                          │
                │ 3 COMPARER: same / different / real-world effect  │
                │   model: best (e.g. Claude Opus)                  │
                │ 4 VERIFIER: a model from a DIFFERENT company       │
                │   (e.g. GPT) tries to prove the comparer wrong     │
                │ 5 FINAL CHECK: code checks links and quotes;       │
                │   a model re-reads each page against the sources  │
                │        ▼                                          │
                │   PDF: one rule per page + links                  │
                └───────────────────────────────────────────────────┘
                     ▲ you: browser only. You read results and fix the rule list
```

**Why the verifier comes from a different company.** Two models from the same family tend to make the same mistakes. A checker from another company catches more (Interpretation). This is the main reason to mix models, besides price.

---

## 3. The model families in plain words

| Family | Company (country) | Example models and price per 1M tokens (input / output) | Good for | Watch out |
|---|---|---|---|---|
| **Claude** | Anthropic (US) | Opus 5.5 $4 / $20; Sonnet 5.5 $2 / $10; Haiku 5.5 $0.10 / $0.50 [S044] | Careful reasoning; comparing and checking | Most expensive at the top end |
| **GPT** | OpenAI (US) | GPT-5.5 $5 / $30; GPT-5.4-mini $0.75 / $4.50 [S045] | A strong second opinion (verifier) | Expensive output |
| **Gemini** | Google (US) | 3.1 Pro $2 / $12 [S046] | A mid-price alternative | — |
| **Qwen** | Alibaba (China) | 3.8 Max $2 / $6; 3.7 Plus $0.40 / $1.60; 3.8 Flash $0.15 / $0.47 [S174] | Cheap reading and translating at volume; Alibaba also has a Frankfurt (EU) region for some models [S174] | Quality in small languages (Latvian, Estonian) must be tested |
| **DeepSeek** | DeepSeek (China) | V4 Pro $1.32 / $3.96; Flash $0.30 / $1.20, **half price off-peak** [S173] | Very cheap simple jobs (the supervisor) | EU privacy regulators have acted against DeepSeek's app (Italy blocked it; Berlin asked app stores to remove it; Dutch investigation) [S175]. Fine for **public** law texts; never send personal or client data. Peak hours (06:00–10:00 UTC on weekdays) fall on Latvian mornings |
| **Mistral** | Mistral AI (France) | Large $0.50 / $1.50 [S181] | A cheap **European** option, worth testing as a reader for EU languages | — |

**To keep data in the EU**, some EU companies host open models (Scaleway in Paris, OVHcloud in France, Nebius in the Netherlands) [S180]. Which Qwen or DeepSeek versions they carry needs checking.

*If "Quay bots" meant Poe bots (Quora's app):* Poe is a chat app for making simple bots on many models. It is good for trying models by hand, but not built to run an automated pipeline like this one (Interpretation).

---

## 4. Tools that let you pick a model for each agent

| Tool | What it is | Fit for you | Cost |
|---|---|---|---|
| **OpenRouter** | One account, one API key, models from many companies at the providers' own prices. Falls back to another provider automatically if one fails [S176] | **Yes.** It is the "switchboard" for choosing models | No markup on model prices; **5.5% fee** when you buy credits by card [S176] |
| **n8n** | Visual workflow builder (boxes and arrows). The **AI Agent** box can use a different model each time, including through OpenRouter [S177] | **Yes, if you prefer not to code.** It runs on your server | Self-hosted: **free**. Cloud: €20 or €50 per month [S177] |
| **Dify** | An open-source visual builder for agents and workflows, supporting 100+ model providers [S179] | An alternative to n8n | Self-hosted free; cloud about $59/month [S179] |
| **Claude Managed Agents** | Anthropic hosts the agents and their workspace; no server of your own [S182] | Simplest to operate, but **Claude models only** (you can still mix Haiku, Sonnet and Opus) | Tokens + $0.08 per hour of running time [S182] |
| **Python code with an AI coding assistant** | The most flexible option; Claude Code can write it, and Claude Code on the web runs in the cloud, not on your PC | Only if you are comfortable reading some code | Free tools; your time |

**Suggested setup** (Recommendation):
- **n8n**, self-hosted on a small EU server.
- **OpenRouter** for all models.
- The notes database as a **folder of Markdown files**, backed up to GitHub. Obsidian opens it as a linked mind map.
- **Pandoc** on the server to make the PDF.

Everything except the AI usage is free or a few euros a month.

---

## 5. Which model for which agent

| Agent | Runs | Needs | Suggested model (mix B) | Why |
|---|---:|---|---|---|
| Reader / translator | 1,000 (100 rules × 10) | Good reading in 9 languages; exact quotes | **Qwen 3.7 Plus**; test against Mistral Large and Claude Sonnet first | It runs most often, so the price matters most here |
| Supervisor | 1,000 | Simple yes/no checks; most checks are done by code | **DeepSeek Flash** | Simple job, very cheap |
| Comparer | 100 | Best reasoning; real-world effects | **Claude Opus 5.5** | Only 100 runs, so the best model costs little |
| Verifier | 100 | Independent, strong | **GPT-5.5** | A different company from the comparer |
| Final check | 100 | Careful re-reading | **Claude Sonnet 5.5** | Mid price, careful |

**What each mix costs for one full run** (EUR; low / **base** / high; [`stack_costs_results.md`](stack_costs_results.md)):

| Mix | Low | Base | High |
|---|---:|---:|---:|
| A. All Claude | 371 | **1,321** | 4,936 |
| **B. Mixed (suggested)** | 189 | **634** | 2,112 |
| C. Chinese models only | 224 | **818** | 3,098 |
| D. Premium (best everywhere) | 719 | **2,561** | 9,622 |

Mixing companies is the cheapest option and also the safest, because the verifier is independent. "Chinese only" is not the cheapest: DeepSeek V4 Pro costs more than Qwen Plus for the reading job, unless you run it off-peak. In every mix, the readers are most of the bill.

---

## 6. Cash budget, first 3 months (EUR; Calculation)

| Item | Low | Base | High |
|---|---:|---:|---:|
| AI usage: one full run (mix B) + 50% for test runs | 283 | 951 | 3,168 |
| Server, 3 months (about €20–36 a month) [S178] | 62 | 110 | 110 |
| n8n (self-hosted free; cloud €50/month in the high case) [S177] | 0 | 0 | 150 |
| Optional lawyer spot-check of final pages | 0 | 450 | 1,500 |
| **Total** | **345** | **1,511** | **4,927** |

Not included: your own time, and the AI subscriptions you already have.

**Server prices.** Hetzner (Germany/Finland) raised prices sharply in 2026. A 4-core, 8 GB server is reported at about €35–36 a month [S178]. Any EU server with 4–8 GB of RAM is enough.

**Spending limit.** Set one in OpenRouter so a stuck agent cannot run up a bill.

---

## 7. Realistic timeline (part-time, 10–15 h a week)

| Weeks | What you do | Result |
|---|---|---|
| 1–2 | Write the list of ~100 rules and the 10 countries. Find each country's official law website. Rent the server; set up n8n and OpenRouter | Setup done; rule list |
| 3–5 | Build the pipeline. Run **1 rule × 10 countries** (overtime pay). Read the result and fix it | First working pages |
| 6–7 | Run **10 rules**. Check about 20 answers you can verify yourself. Pick the reader model that gets them right | Model choice; trust check |
| 8–10 | **Full run** of 100 rules. The supervisor flags problems; you re-run failures | Filled notes database (mind map) |
| 11–12 | Comparer, verifier and final check. Fix broken pages. Make the PDF. Optional lawyer spot-check | **Final PDF** |

**About 12 weeks part-time.** Full-time, it would be about 5–7 weeks. It takes longer (up to about 5 months) if country websites block automated reading, or if the reader models struggle with some languages.

---

## 8. The main risks for this setup, and the simple fix for each

| Risk | Simple fix |
|---|---|
| Agents agree on something wrong | The verifier comes from another company. Code checks that every quote is really on the linked official page. "Unsure" is allowed |
| Readers misread small languages | Test 2–3 reader models on 20 rules you can check, before the full run |
| Country websites block bots (EUR-Lex and the Estonian site did during our research) | Use official open-data downloads where they exist; download by hand where needed |
| "Real-world effect" is guessed | Only report effects backed by an official source (collective agreements, guidance); otherwise write "not found" |
| Runaway costs | Spending limit in OpenRouter; test small before the full run |
| Privacy (DeepSeek) | Send only public law texts, never personal or client data; or use EU-hosted models |

---

## 9. Decisions before building

1. **The list of rules** (about 100 for agriculture) and the **10 jurisdictions**: EU, Latvia, Germany, Netherlands, France, Spain, Sweden, Estonia, Poland, plus one more?
2. **No-code (n8n) or code** (Python written with an AI coding assistant)?
3. **Budget cap** for the first 3 months (base case about €1,500).
