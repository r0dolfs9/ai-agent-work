"""v1.1 reconciliation: paper figures vs generated outputs (operator economics, labour sensitivity,
AIDev timing, opportunity scores) and arithmetic checks on derived numbers."""
import pathlib, csv, sys
root = pathlib.Path(__file__).resolve().parents[1]
paper = (root / "paper" / "paper.md").read_text()
cm = (root / "models" / "cost_model_results.md").read_text()
op = (root / "models" / "operator_economics_results.md").read_text()
aid = (root / "research" / "analysis" / "aidev_timing_results.md").read_text()
reg = (root / "opportunities" / "opportunity-register.md").read_text()
checks = [
 # labour sensitivity
 ("| US support agent (BLS × 1.4) | 33% | 49% |", cm, "| US support agent (BLS × 1.4) | 30.14 | $135,304 | $200,947 | 33% | $6,159 | $12,057 | 49% |"),
 ("| EU27 average | 36% | 51% |", cm, "| EU27 average | 39.11 | $165,755 | $260,726 | 36% |"),
 ("| Germany average | 39% | 53% |", cm, "| Germany average | 50.43 | $204,189 | $336,180 | 39% |"),
 ("| Estonia average | 28% | 46% |", cm, "| Estonia average | 23.64 | $113,240 | $157,631 | 28% |"),
 ("| Latvia average | 22% | 42% |", cm, "| Latvia average | 18.27 | $94,975 | $121,772 | 22% |"),
 # operator economics
 ("€46.2–48.0", op, "€46.23"), ("€46.2–48.0", op, "€48.02"), ("€45.6–46.1", op, "€45.59"), ("€45.6–46.1", op, "€46.10"),
 ("€44.5–46.3", op, "€44.51"), ("€44.5–46.3", op, "€46.30"), ("€0.1–2.3", op, "€0.1 (US card"),
 ("the owner receives €40,000 under the standard regime and €39,950", op, "| €50,000 | €40,000 | €10,000 | €39,950 |"),
 ("about €375 VAT", op, "≈ €375"), ("about €1,700–6,400 a year", op, "€1,740"), ("about €1,700–6,400 a year", op, "€6,360"),
 # AIDev
 ("2,743,854", aid, "Rows: 2,743,854"), ("25.8% of agent-authored PRs", aid, "| ALL | 2743854 | 0.2579 |"),
 ("peak-to-trough ratio is only **1.57**", aid, "| 1.57 |"), ("20% of PRs are opened between 00:00 and 06:00 UTC", aid, "| 0.2002 |"),
 ("21.4% (Devin) to 28.0% (Google Jules)", aid, "| Devin | 43298 | 0.2137"), ("21.4% (Devin) to 28.0% (Google Jules)", aid, "| Google_Jules | 50490 | 0.28 |"),
 ("peaks at 20:00 UTC", aid, "| OpenAI_Codex | 2069595 | 0.2627 | 0.2857 | 20 |"),
 ("Saturday is 12.7% and Sunday 13.1%", aid, "5:0.127 6:0.131"),
 # opportunity scores
 ("| 67 (v1.0: 69;", reg, "| O02 | Independent evaluation"), ("(30, down from 36)", reg, "**30.0** | 36.0"), ("(43, down from 47)", reg, "**43.0** | 47.0"),
]
bad = [(p, m) for p, src, m in checks if p not in paper or m not in src]
for p, m in bad:
    print("MISMATCH:", repr(p)[:80], "| expected in source:", repr(m)[:80])
# arithmetic
arith = [("Anthropic overturn share of appeals", round(42/398*100, 1), 10.6),
         ("Anthropic overturns per ban (%)", round(42/11400*100, 2), 0.37),
         ("TRM lower bound $M", round(0.006*25.62, 2), 0.15), ("TRM upper bound $M", round(0.075*25.62, 1), 1.9),
         ("Gartner agents growth 2025-26 %", round((29219/16481-1)*100), 77)]
for name, got, want in arith:
    if abs(got - want) > 1e-9:
        bad.append((name, got)); print("ARITH MISMATCH", name, got, want)
print(f"{len(checks)+len(arith)-len(bad)}/{len(checks)+len(arith)} v1.1 checks passed")
sys.exit(1 if bad else 0)
