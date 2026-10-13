#!/bin/bash
# Count Latvian laws (Saeima, izd_id=138, veids_id=84) and Cabinet regulations (izd_id=92, veids_id=87) on likumi.lv,
# using the same endpoint the public list pages (likumi.lv/ta/veids/...) call. Six requests, 2 s apart.
# spe=1: in force; ngr=1: base acts only (amending acts hidden); no filter: every act ever published.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="$HERE/results/09_likumi_lv_counts.csv"
B='https://likumi.lv/ajax/ties_akti_pec_veida.php'
echo "act_type,filter,rows" > "$OUT"
for t in "laws:138:84" "cabinet_regulations:92:87"; do
  IFS=: read name izd veids <<< "$t"
  for q in "spe=1" "spe=1&ngr=1" "all"; do
    f="$q"; [ "$q" = "all" ] && q="spe=0"
    rows=$(curl -sS -m 40 -A 'Mozilla/5.0 (research; low-rate)' "$B?piece=0&mode=i&alpha=&izd_id=$izd&veids_id=$veids&$q&oby=0&odir=0&tstamp=0&qwstats=1" | python3 -c 'import json,sys; print(json.load(sys.stdin)["rows"])')
    echo "$name,$f,$rows" >> "$OUT"; sleep 2
  done
done
date -u +"retrieved %Y-%m-%dT%H:%MZ" >> "$OUT"
cat "$OUT"
