# Capability-selection record

Observed 2026-10-12. Values: yes / no / unknown / n/a / not attempted.

| Capability | Installed / file present | Exposed & invocable | Service connected | Permission & user authorization | Attempted | Succeeded | Evidence |
|---|---|---|---|---|---|---|---|
| Git repo `r0dolfs9/ai-agent-work` (local checkout) | yes | yes | yes (origin remote configured) | yes, push to designated branch only | yes | yes | `git status` shows branch `claude/amazing-archimedes-w4pw0c` with no commits |
| WebSearch | yes (deferred tool) | yes after ToolSearch load | yes | yes (read-only research) | yes | yes | Four searches returned results on 2026-10-12 |
| WebFetch | yes (deferred tool) | yes after load | yes | yes (read-only) | yes | yes; some sites block it (see source register notes) | Fetch log in `research/sources.csv` |
| python3 3.13 | yes | yes | n/a | yes (local computation) | yes | yes | `python3 --version` |
| pandoc | yes | yes | n/a | yes | not attempted | not attempted | `/usr/bin/pandoc` present |
| Sub-agents (Agent tool) | yes | yes | n/a | **no explicit user request.** The assignment says delegation is optional, and session policy says to avoid spawning without an explicit request. | no | n/a | Research done inline. No delegated results need verification. |
| GitHub MCP (PRs, comments) | yes (deferred) | not loaded | unknown | **no.** Creating a PR or comment counts as an outward action and was not requested. | no | n/a | — |
| Gmail / Google Calendar MCP | yes (deferred) | not loaded | unknown | **no.** Contacting people needs approval, and these tools are irrelevant to read-only research. | no | n/a | Deliberately not used |
| Gamma / Claude Docs / Artifact publishing | yes | yes | unknown | **no.** Publishing needs approval. | no | n/a | Local Markdown only. Publishing is offered, not done. |
| Paid data (Gartner, Statista full text, Similarweb) | no | no | no | no budget authorized | no | n/a | Fallback: public press releases and summaries, labelled as such |

Owner actions that would unlock more evidence:
1. Approve a budget or provide credentials for analyst reports.
2. Approve customer-discovery outreach.
3. Share any first-party agent usage logs.

## v1.1 capability record (2026-10-12)

| Capability | Installed/present | Exposed & invocable | Service connected | Permission & authorization | Attempted | Succeeded | Evidence |
|---|---|---|---|---|---|---|---|
| WebFetch → web.archive.org | yes | tool refuses this host | n/a | read-only research authorised | yes | **no** ("unable to fetch from web.archive.org") | Not worked around; archived copies not used |
| WebFetch → publisher-hosted alternative domains (gcom.pdo.aws.gartner.com, karriere.mckinsey.de) | yes | yes | yes | yes (public pages, no login or spoofing) | yes | yes | S082–S087, S098; disclosed as owner decision point V1 |
| WebFetch → openai.com, help.openai.com, cnbc.com, oecd.org HTML | yes | yes | yes | yes | yes | no (HTTP 403) | Not bypassed; alternatives used (PDF on oecd.org fetched; developer docs) |
| Eurostat dissemination API | n/a (public HTTP) | yes (curl) | yes | yes | yes | yes | isoc_eb_ai, lc_lci_lev queries |
| ECB Data API (FX) | n/a | yes | yes | yes | yes | yes | EXR D.USD.EUR, 2026-10-09 = 1.1206 |
| Hugging Face public dataset (AIDev, CC-BY-4.0) | n/a | yes (HTTP range reads) | no account | yes (public, licensed) | yes | yes | 2,743,854 rows, two columns read |
| Python venv with pyarrow/fsspec (scratchpad only; not a repo dependency) | created | yes | n/a | local, reversible | yes | yes | Used only for the AIDev analysis |
| pdftotext | yes | yes | n/a | yes | yes | yes | OECD, OpenAI DSA cover letter, KPMG tax card |
| GitHub/Gmail/Calendar MCP | intermittently connected | not used | — | **no** (no outward action needed) | no | n/a | — |
