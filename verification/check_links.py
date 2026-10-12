"""Read-only link check of every URL in research/sources.csv (GET, 20s timeout, browser UA).
Writes verification/link-check.csv. Many publishers block automated clients (403) — a 403 is
recorded as 'blocked-to-bots', not as a dead link."""
import csv, pathlib, subprocess, concurrent.futures as cf
root = pathlib.Path(__file__).resolve().parents[1]
rows = list(csv.DictReader(open(root / "research" / "sources.csv")))
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
def check(r):
    try:
        out = subprocess.run(["curl", "-s", "-o", "/dev/null", "-L", "--max-time", "20", "-A", UA,
                              "-w", "%{http_code} %{url_effective}", r["url"]], capture_output=True, text=True, timeout=30).stdout
        code, final = (out.split(" ", 1) + [""])[:2]
    except Exception as e:
        code, final = "ERR", str(e)
    status = ("ok" if code.startswith(("2", "3")) else "blocked-to-bots" if code in ("401", "403", "429", "503")
              else "not-found" if code in ("404", "410") else "error")
    return [r["id"], r["url"], code, status, final if final != r["url"] else ""]
with cf.ThreadPoolExecutor(8) as ex:
    res = list(ex.map(check, rows))
with open(root / "verification" / "link-check.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["id", "url", "http_code", "status", "final_url_if_redirected"]); w.writerows(res)
from collections import Counter
print(Counter(r[3] for r in res)); [print(r) for r in res if r[3] in ("not-found", "error")]
