"""fetch.py NAME URL [Accept] -> saves snap/NAME.raw + snap/NAME.txt, logs to fetch-log.csv (one request)."""
import sys, hashlib, html, re, urllib.request, datetime, pathlib, io
W = pathlib.Path(__file__).parent
name, url = sys.argv[1], sys.argv[2]
acc = sys.argv[3] if len(sys.argv) > 3 else "*/*"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research; single request)", "Accept": acc, "Accept-Language": "eng"})
ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
try:
    r = urllib.request.urlopen(req, timeout=60); raw = r.read(); code = r.status; ctype = r.headers.get("Content-Type", "")
except Exception as e:
    code = getattr(e, "code", 0); raw = getattr(e, "read", lambda: b"")() if hasattr(e, "read") else b""; ctype = str(e)[:80]
(W / "snap" / f"{name}.raw").write_bytes(raw)
h = hashlib.sha256(raw).hexdigest()
if b"%PDF" == raw[:4]:
    try:
        from pypdf import PdfReader
        txt = "\n".join(p.extract_text() or "" for p in PdfReader(io.BytesIO(raw)).pages)
    except Exception as e:
        txt = f"[pdf text extraction failed: {e}]"
else:
    t = raw.decode("utf-8", errors="ignore")
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
    txt = html.unescape(re.sub(r"<[^>]+>", " ", t))
txt = re.sub(r"\s+", " ", txt)
(W / "snap" / f"{name}.txt").write_text(txt, encoding="utf-8")
with open(W / "fetch-log.csv", "a", encoding="utf-8") as f:
    f.write(f"{ts},{name},{code},{len(raw)},{h},\"{ctype}\",{url}\n")
print(code, len(raw), len(txt), h[:12], name)
