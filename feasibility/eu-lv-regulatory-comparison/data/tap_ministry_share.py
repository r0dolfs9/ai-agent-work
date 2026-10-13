#!/usr/bin/env python3
"""Share of adopted Cabinet regulations by responsible ministry, from TAP open data (CC0, data.gov.lv) [S146][S206].
Usage: python3 -I tap_ministry_share.py <folder>   (folder = the monthly JSON files downloaded from the dataset
'tap-publicetie-tiesibu-akti'; see the CKAN API at https://data.gov.lv/dati/api/3/action/package_show?id=tap-publicetie-tiesibu-akti)
Writes results/10_tap_cabinet_regulations_by_ministry.csv next to this script.
"""
import collections, csv, glob, json, pathlib, sys

acts, types = {}, {}
for f in sorted(glob.glob(sys.argv[1] + "/*.json")):
    d = json.load(open(f, encoding="utf-8"))
    for x in d.get("included", []):
        if x["type"] == "legal_act_types":
            types[x["id"]] = x["attributes"]["name"]
    for it in d.get("data", []):
        a, t = it["attributes"], it["relationships"]["legal_act_type"]["data"]
        acts[it["id"]] = (a["name"], a["responsible_institution_name"], a["progress_name"],
                          types.get(t["id"], "?") if t else "?", (a.get("submitted_at") or "")[:4])
regs = [v for v in acts.values() if v[3] == "Noteikumu projekts" and v[2] == "Pieņemts"]
allc = collections.Counter(v[1] for v in regs)
newc = collections.Counter(v[1] for v in regs if not v[0].startswith("Grozījum"))
out = pathlib.Path(__file__).resolve().parent / "results/10_tap_cabinet_regulations_by_ministry.csv"
with open(out, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["ministry", "adopted_regulations", "share", "new_non_amending", "share_new"])
    for m, n in allc.most_common():
        w.writerow([m, n, round(n / len(regs), 4), newc.get(m, 0), round(newc.get(m, 0) / max(1, sum(newc.values())), 4)])
    w.writerow(["TOTAL", len(regs), 1, sum(newc.values()), 1])
zm = [v for v in regs if v[1] == "Zemkopības ministrija"]
print("adopted Cabinet regulations:", len(regs), "| Zemkopības ministrija:", len(zm),
      "| by submission year:", sorted(collections.Counter(v[4] for v in zm).items()))
