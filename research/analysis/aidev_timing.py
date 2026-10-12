"""Timing analysis of agent-authored GitHub pull requests (AIDev dataset, CC-BY-4.0,
hao-li/AIDev on Hugging Face, arXiv 2602.09185). Reads only the columns needed
(created_at, agent) from the public parquet via HTTP range requests.
Run: <venv-with-pyarrow+fsspec>/python research/analysis/aidev_timing.py
Outputs research/analysis/aidev_timing_results.md and .csv.
Caveats: timestamps are UTC PR-creation times; they mark when an agent opened a PR,
not when it was 'active' or when a human triggered it. Author time zones unknown."""
import pathlib, fsspec, pyarrow.parquet as pq, pandas as pd
URL = "https://huggingface.co/datasets/hao-li/AIDev/resolve/main/all_pull_request.parquet"
OUT = pathlib.Path(__file__).resolve().parent
import os
CACHE = pathlib.Path(os.environ.get("AIDEV_CACHE", "/tmp/aidev_cols.parquet"))
if CACHE.exists():
    df = pd.read_parquet(CACHE)
else:
    with fsspec.open(URL, "rb", block_size=8 * 2**20) as f:
        t = pq.read_table(f, columns=["created_at", "agent"])
    df = t.to_pandas(); df.to_parquet(CACHE)
df["ts"] = pd.to_datetime(df["created_at"], utc=True, errors="coerce")
df = df.dropna(subset=["ts"])
df["hour"] = df.ts.dt.hour
df["dow"] = df.ts.dt.dayofweek  # 0=Mon
lines = ["# Agent-authored PR timing (AIDev, UTC)\n",
         f"Rows: {len(df):,}; period {df.ts.min():%Y-%m-%d} to {df.ts.max():%Y-%m-%d}; agents: "
         + ", ".join(f"{a} {n:,}" for a, n in df.agent.value_counts().items()) + "\n"]
rows = []
for agent, g in [("ALL", df)] + list(df.groupby("agent")):
    n = len(g)
    wk = (g.dow >= 5).mean()
    hours = g.hour.value_counts(normalize=True).sort_index()
    peak_h = int(hours.idxmax()); trough_h = int(hours.idxmin())
    night = g.hour.isin([0, 1, 2, 3, 4, 5]).mean()
    rows.append(dict(agent=agent, n=n, weekend_share=round(wk, 4), expected_weekend_if_uniform=round(2/7, 4),
                     peak_hour_utc=peak_h, peak_share=round(hours.max(), 4), trough_hour_utc=trough_h,
                     trough_share=round(hours.min(), 4), share_00_06_utc=round(night, 4),
                     peak_to_trough=round(hours.max() / hours.min(), 2)))
res = pd.DataFrame(rows)
res.to_csv(OUT / "aidev_timing_results.csv", index=False)
hdr = "| " + " | ".join(res.columns) + " |\n|" + "---|" * len(res.columns)
lines.append(hdr + "\n" + "\n".join("| " + " | ".join(str(v) for v in r) + " |" for r in res.itertuples(index=False)))
hourly = df.groupby(["hour"]).size().div(len(df)).round(4)
lines.append("\n\nAll agents, share of PRs by UTC hour:\n\n" + " ".join(f"{h:02d}:{v:.3f}" for h, v in hourly.items()))
dow = df.groupby("dow").size().div(len(df)).round(4)
lines.append("\n\nAll agents, share by weekday (0=Mon):\n\n" + " ".join(f"{d}:{v:.3f}" for d, v in dow.items()))
(OUT / "aidev_timing_results.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
