#!/bin/bash
# Re-run the scope queries against the EU Publications Office SPARQL endpoint (public, no key).
# Usage: bash feasibility/eu-lv-regulatory-comparison/data/run_queries.sh
# Writes one CSV per query into data/results/. Each query can take up to ~2 minutes.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$HERE/results"
for q in "$HERE"/queries/*.rq; do
  name="$(basename "$q" .rq)"
  echo "running $name"
  curl -sS -m 180 -G 'https://publications.europa.eu/webapi/rdf/sparql' \
    --data-urlencode "query@$q" -H 'Accept: text/csv' > "$HERE/results/$name.csv"
done
date -u +"retrieved %Y-%m-%dT%H:%MZ" > "$HERE/results/RETRIEVED.txt"
