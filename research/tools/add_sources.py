"""Append source rows to research/sources.csv safely (proper CSV quoting).
Usage: python3 -I add_sources.py <json-file>   (JSON = list of objects with the 12 column keys)
"""
import csv, json, sys, pathlib
COLS = ["id","title","publisher","url","pub_date","retrieved","source_type","access","topics",
        "key_extract_and_location","caveats","confidence"]
path = pathlib.Path(__file__).resolve().parents[1] / "sources.csv"
existing = {r["id"] for r in csv.DictReader(open(path))}
rows = json.load(open(sys.argv[1]))
with open(path, "a", newline="") as f:
    w = csv.DictWriter(f, fieldnames=COLS)
    for r in rows:
        if r["id"] in existing:
            sys.exit(f"duplicate id {r['id']}")
        r.setdefault("retrieved", "2026-10-12")
        w.writerow({k: r.get(k, "") for k in COLS})
print("added", len(rows))
