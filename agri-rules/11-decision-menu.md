# L. Decision menu

*14 October 2026. Money in EUR ex VAT; hours at the base assumptions (07). Pick one.*

| # | Option | What it is | Cost | Effort | Learning value | Downside |
|---|---|---|---|---|---|---|
| **1** | **Run the smallest pilot** *(recommended)* | Sprint S0 only: 3 questions × 10 layers by hand, terms and authority mapping, timing log | **€0** | ~40 h (23–63) over ~3 weeks | **Highest per hour.** Measures gold time per cell (the dominant cost driver), confirms access and permissions for every layer, and produces the first benchmark gold data | No AI is tested yet; it feels slow. Decision on the AI pipeline is postponed ~2 months |
| 2 | Run an expanded evidence pilot | S0 → S5: 20 questions, 100 gold cells, benchmark of 3 candidate pipelines, pilot PDF, optional lawyer spot-check | AI ~€200 (11–993) + lawyer ~€2,600 (optional, assumed rates) | ~265 h (138–490) over ~21 weeks | Answers the whole viability question with measured numbers | Commits 5+ months before knowing whether gold time per cell is affordable; requires an API account (🔒) and possibly lawyers (🔒) |
| 3 | Narrow the subject domain first | Restrict to one domain (e.g. **employment/working time**, 20 questions) across 10 layers, then expand | ~Option 2 cost × 0.5 | ~130 h | Fast, coherent product for one audience (farm employers); deepest test of the collective-agreement problem | Loses the cross-domain picture; employment is also the hardest domain (agreements), so it is not an "easy start" |
| 4 | Pause because a load-bearing premise failed | Stop now, keep the package | €0 | 0 h | Preserves options | **No premise has failed so far.** Access works for 9 of 10 layers, and none of the brief's concerns is a blocker. Pausing now would be premature unless the owner's audience or budget is the real constraint |

**Decisions that can safely wait** (they do not affect Option 1):
- the intended audience (internal vs client)
- the budget cap
- Italy vs Denmark (S0 includes both in the access check)
- n8n vs code (the pilot needs neither a server nor n8n)
- DeepL
- Obsidian
- the hosting provider
