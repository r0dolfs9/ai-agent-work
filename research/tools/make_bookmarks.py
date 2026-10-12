"""Export research/sources.csv to a browser-importable bookmarks file (Netscape format),
grouped by first topic. Local file only — does not touch any browser profile.
Usage: python3 -I make_bookmarks.py"""
import csv, html, pathlib, collections
root = pathlib.Path(__file__).resolve().parents[1]
rows = list(csv.DictReader(open(root / "sources.csv")))
groups = collections.defaultdict(list)
for r in rows:
    groups[r["topics"].split(";")[0]].append(r)
out = ["<!DOCTYPE NETSCAPE-Bookmark-file-1>", '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">',
       "<TITLE>AI agent ecosystem research sources</TITLE>", "<H1>AI agent ecosystem research sources</H1>", "<DL><p>"]
for g in sorted(groups):
    out.append(f"<DT><H3>{html.escape(g)}</H3>\n<DL><p>")
    for r in groups[g]:
        out.append(f'<DT><A HREF="{html.escape(r["url"])}">[{r["id"]}] {html.escape(r["title"])}</A>')
        out.append(f'<DD>{html.escape(r["publisher"])} · {html.escape(r["pub_date"])} · conf {r["confidence"]}')
    out.append("</DL><p>")
out.append("</DL><p>")
(root / "bookmarks.html").write_text("\n".join(out) + "\n")
print(len(rows), "bookmarks in", len(groups), "folders")
