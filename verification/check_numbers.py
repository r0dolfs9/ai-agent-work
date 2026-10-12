"""Reconcile cost figures quoted in the paper with the generated model output.
Each check: (string that must appear in paper.md, string that must appear in cost_model_results.md)."""
import pathlib, sys
root = pathlib.Path(__file__).resolve().parents[1]
paper = (root / "paper" / "paper.md").read_text()
model = (root / "models" / "cost_model_results.md").read_text()
checks = [
 ("$10.92", "$10.92"), ("$163", "| base | 450 | $157 | $6.00 | $163"), ("$4,625", "$4,625"), ("$4.39", "$4.39"),
 ("Haiku 5.5: **$19**", "| claude-haiku-5.5 | $19.40 |"), ("Opus 5.5: $315", "| claude-opus-5.5 | $315 |"),
 ("GPT-5.5: $374", "| gpt-5.5 | $374 |"), ("Fable 5.1: $750", "| claude-fable-5.1 | $750 |"), ("Gemini 3.1 Pro: $156", "| gemini-3.1-pro | $156 |"),
 ("**$2,528**", "$2,528"), ("**$6,159**", "$6,159"), ("**$15,568**", "$15,568"), ("**49%**", "| 49% |"), ("**72%**", "| 72% |"), ("**−3%**", "| -3% |"),
 ("$4.70", "| 300 | $4.70 | -17% |"), ("$2.64", "| 1,000 | $2.64 | 34% |"), ("$1.85", "| 10,000 | $1.85 | 54% |"),
 ("**$67,325**", "$67,325"), ("**$135,304**", "$135,304"), ("**$311,771**", "$311,771"), ("**62%**", "| 62% |"), ("**33%**", "| 33% |"), ("**−24%**", "| -24% |"),
 ("**$133,590/month**", "$133,590"), ("$89k", "$89,361"), ("$230k", "$229,713"),
 ("**8%**", "LLM tokens are 8%"), ("**74%**", "human escalations 74%"), ("**17%**", "fixed engineering/infra/security 17%"),
 ("52% at a 70% resolution rate", "resolve 70%: total $95,869 vs human-only $200,947 → saving 52%"),
 ("only 3% at 20%", "resolve 20%: total $194,458 vs human-only $200,947 → saving 3%"),
 ("about **$0.20**", "| claude-sonnet-5.5 | 0.2049 |"), ("about **$0.45**", "0.4545 $/task"),
 ("$0.011 (Haiku 5.5)", "| claude-haiku-5.5 | 0.0108 |"), ("$1.00 (Fable 5.1)", "| claude-fable-5.1 | 0.9985 |"),
 ("−$0.50 | +$1.01", "| escalate_min | -0.502 | +1.005 |"), ("−$0.59 | +$0.59", "| resolve | -0.592 | +0.592 |"),
 ("−$0.16 | +$0.32", "| eng_fte | -0.159 | +0.317 |"), ("−$0.06 | +$0.24", "| loop.steps | -0.064 | +0.235 |"),
 ("−$0.05 | +$0.11", "| loop.base_ctx | -0.054 | +0.108 |"), ("−$0.04 | +$0.10", "| sec_annual | -0.042 | +0.100 |"),
 ("−$0.03 | +$0.06", "| loop.cache_hit | -0.031 | +0.062 |"),
 ("about 169,000 tokens", "169,200"),
]
bad = [(p, m) for p, m in checks if p not in paper or m not in model]
for p, m in bad:
    print("MISMATCH:", repr(p), "in paper:", p in paper, "| model:", repr(m), m in model)
print(f"{len(checks)-len(bad)}/{len(checks)} figure checks passed")
sys.exit(1 if bad else 0)
