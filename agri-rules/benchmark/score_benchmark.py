"""Score a completed benchmark run (deliverable G).

Usage:
  python3 agri-rules/benchmark/score_benchmark.py <scores.csv> [<verifier_pairs.csv>]

<scores.csv> has one row per (item, candidate, rater); columns are defined in
benchmark/scores_template.csv and explained in 06-benchmark-protocol.md §6.
<verifier_pairs.csv> (optional) has columns: item_id, primary, verifier, verifier_flagged (0/1).

Outputs per candidate: critical-failure rate, mean points, verdict (PASS /
CONDITIONAL / FAIL), cost and latency; inter-rater agreement (Cohen's kappa) on
the critical-failure judgement; and the correlated-error check between a primary
model and its verifier.

The sample file benchmark/sample_scores_SYNTHETIC.csv exists only to prove the
script runs. Its numbers are invented and are NOT results.
"""
import csv
import sys
from collections import defaultdict

BINARY = ["retrieval_ok", "provision_ok", "scope_ok", "threshold_ok", "exception_ok",
          "date_ok", "citation_ok", "schema_valid"]
GRADED = ["translation_0_3", "comparison_0_3"]          # 0..3 each
MAX_POINTS = len(BINARY) + 3 * len(GRADED)                # 14
CRITICAL = {"wrong_jurisdiction", "outdated_law", "missing_material_exception", "false_citation",
            "reversed_obligation", "wrong_threshold", "unjustified_certainty"}

# Thresholds (06-benchmark-protocol.md §7). Pre-registered: do not change after seeing results.
PASS = dict(max_critical_rate=0.02, min_points=0.85, max_halluc_per_item=0.05)
CONDITIONAL = dict(max_critical_rate=0.05, min_points=0.75, max_halluc_per_item=0.15)


def kappa(a: list[int], b: list[int]) -> float:
    n = len(a)
    if n == 0:
        return float("nan")
    po = sum(x == y for x, y in zip(a, b)) / n
    pa, pb = sum(a) / n, sum(b) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def main(path: str, pairs_path: str | None = None) -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    by_cand = defaultdict(list)
    for r in rows:
        flags = {f for f in r["critical_flags"].split(";") if f}
        unknown = flags - CRITICAL
        if unknown:
            sys.exit(f"Unknown critical flag(s) {unknown} in row {r['item_id']}/{r['candidate']}")
        r["_crit"] = 1 if flags else 0
        r["_pts"] = (sum(int(r[c]) for c in BINARY) + sum(int(r[c]) for c in GRADED)) / MAX_POINTS
        by_cand[r["candidate"]].append(r)

    print("## Per-candidate results\n")
    print("| Candidate | Items×raters | Critical-failure rate | Mean points | Halluc./item | Unsupported/item | "
          "Schema valid | Mean latency s | Cost USD | Verdict |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for cand, rs in sorted(by_cand.items()):
        n = len(rs)
        crit = sum(r["_crit"] for r in rs) / n
        pts = sum(r["_pts"] for r in rs) / n
        hal = sum(int(r["hallucinations"]) for r in rs) / n
        uns = sum(int(r["unsupported_claims"]) for r in rs) / n
        sch = sum(int(r["schema_valid"]) for r in rs) / n
        lat = sum(float(r["latency_s"]) for r in rs) / n
        cost = sum(float(r["cost_usd"]) for r in rs) / max(1, len({r["rater"] for r in rs}))
        if crit <= PASS["max_critical_rate"] and pts >= PASS["min_points"] and hal <= PASS["max_halluc_per_item"]:
            v = "PASS"
        elif crit <= CONDITIONAL["max_critical_rate"] and pts >= CONDITIONAL["min_points"] and hal <= CONDITIONAL["max_halluc_per_item"]:
            v = "CONDITIONAL"
        else:
            v = "FAIL"
        print(f"| {cand} | {n} | {crit:.1%} | {pts:.1%} | {hal:.2f} | {uns:.2f} | {sch:.0%} | {lat:.1f} | {cost:.2f} | {v} |")

    # Inter-rater agreement on the critical-failure judgement
    print("\n## Inter-rater agreement (critical failure yes/no)\n")
    key = defaultdict(dict)
    for r in rows:
        key[(r["item_id"], r["candidate"])][r["rater"]] = r["_crit"]
    raters = sorted({r["rater"] for r in rows})
    if len(raters) >= 2:
        a, b = raters[0], raters[1]
        pairs = [(v[a], v[b]) for v in key.values() if a in v and b in v]
        k = kappa([p[0] for p in pairs], [p[1] for p in pairs])
        disagree = [kk for kk, v in key.items() if a in v and b in v and v[a] != v[b]]
        print(f"Raters {a} vs {b}: n = {len(pairs)}, Cohen's kappa = {k:.2f}. "
              f"Disagreements to adjudicate: {len(disagree)} -> {disagree[:10]}")
        print("Rule: kappa < 0.6 means the rubric is ambiguous; fix the rubric and re-score before trusting any verdict.")
    else:
        print("Only one rater: agreement cannot be measured. Results are provisional.")

    # Correlated errors between primary and verifier
    if pairs_path:
        print("\n## Correlated errors (primary vs verifier)\n")
        sig = {(r["item_id"], r["candidate"]): (r["_crit"], r["error_signature"]) for r in rows}
        pr = list(csv.DictReader(open(pairs_path, encoding="utf-8")))
        stats = defaultdict(lambda: dict(p_err=0, caught=0, same_err=0, n=0))
        for p in pr:
            s = stats[(p["primary"], p["verifier"])]
            s["n"] += 1
            pe = sig.get((p["item_id"], p["primary"]))
            ve = sig.get((p["item_id"], p["verifier"]))
            if pe and pe[0]:
                s["p_err"] += 1
                s["caught"] += int(p["verifier_flagged"])
                if ve and ve[0] and ve[1] and ve[1] == pe[1]:
                    s["same_err"] += 1
        print("| Primary | Verifier | Items | Primary critical errors | Caught by verifier | Same error made by verifier |")
        print("|---|---|---|---|---|---|")
        for (p, v), s in stats.items():
            catch = s["caught"] / s["p_err"] if s["p_err"] else float("nan")
            print(f"| {p} | {v} | {s['n']} | {s['p_err']} | {s['caught']} ({catch:.0%}) | {s['same_err']} |")
        print("\nA verifier that shares the primary's error signature is not independent for that error class; "
              "those classes need deterministic checks or human review.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
