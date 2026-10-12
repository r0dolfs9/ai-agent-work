#!/usr/bin/env python3
"""Assemble the v1.2 reading package.

1. package/04-economics.md  = 04-economics-intro.md + generated models/route_economics_results.md
2. package/reading-edition.html = one self-contained HTML file with a table of contents:
   START HERE -> decision brief -> dossiers -> economics -> validation plans -> review -> full paper
3. paper/paper.html = the paper alone

Run after: python3 models/route_economics.py && python3 paper/build_paper.py
Requires pandoc (3.x).
"""
import pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PKG = ROOT / "package"

CSS = """
:root{--bg:#fdfdfb;--fg:#1d1d1f;--muted:#5f6368;--accent:#0b57d0;--rule:#d9d9d6;--th:#f1f1ee;--code:#f4f4f1}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#17181a;--fg:#e8e8e6;--muted:#a5a7ab;--accent:#8ab4f8;--rule:#3a3b3e;--th:#232427;--code:#232427}}
html{font-size:17px}
body{background:var(--bg);color:var(--fg);font-family:Georgia,'Iowan Old Style','Palatino Linotype',serif;line-height:1.6;margin:0;padding:0 16px}
main{max-width:52rem;margin:0 auto;padding:1.5rem 0 4rem}
h1,h2,h3,h4{font-family:system-ui,-apple-system,'Segoe UI',sans-serif;line-height:1.25;margin-top:2.2em}
h1{font-size:1.9rem;border-bottom:2px solid var(--rule);padding-bottom:.3em}
h2{font-size:1.45rem}h3{font-size:1.15rem}
a{color:var(--accent);overflow-wrap:anywhere}
p,li,td{overflow-wrap:break-word}
main,body{max-width:100%}
.table-wrap{overflow-x:auto;margin:1em 0}
table{border-collapse:collapse;font-family:system-ui,sans-serif;font-size:.82rem;line-height:1.4;width:100%}
th,td{border:1px solid var(--rule);padding:.35em .5em;vertical-align:top;text-align:left}
th{background:var(--th)}
blockquote{border-left:4px solid var(--rule);margin:1em 0;padding:.2em 1em;color:var(--muted)}
code{background:var(--code);padding:.05em .3em;border-radius:3px;font-size:.88em}
pre{background:var(--code);padding:.8em;overflow-x:auto;max-width:100%;box-sizing:border-box}
div.sourceCode{overflow-x:auto;max-width:100%}
#TOC{font-family:system-ui,sans-serif;font-size:.9rem;background:var(--th);border:1px solid var(--rule);padding:.6em 1.2em;margin:1.5em 0}
#TOC ul{padding-left:1.1em}#TOC>ul>li{margin:.25em 0}
#TOC li li li{display:none}
.part{page-break-before:always}
.topbar{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--rule);font-family:system-ui,sans-serif;font-size:.85rem;padding:.4em 0;z-index:2;overflow-x:auto;white-space:nowrap}
.topbar a{margin-right:.9em;white-space:nowrap}
@media print{.topbar{display:none}body{font-size:11pt}}
"""

PARTS = [
    ("start", "Start here", "00-START-HERE.md"),
    ("brief", "Decision brief", "01-decision-brief.md"),
    ("r2", "Dossier R2: coding-agent enablement", "03-dossiers/R2-coding-agent-enablement.md"),
    ("r4", "Dossier R4: workflow automations", "03-dossiers/R4-workflow-automations.md"),
    ("r1", "Dossier R1: agent risk review", "03-dossiers/R1-agent-risk-review.md"),
    ("r3", "Dossier R3: support-agent evaluation", "03-dossiers/R3-support-agent-evaluation.md"),
    ("econ", "Economics", "04-economics.md"),
    ("valid", "Validation plans", "05-validation-plans.md"),
    ("review", "Review and open questions", "06-review-and-open-questions.md"),
]


DOSSIERS = {"R1": "03-dossiers/R1-agent-risk-review.md", "R2": "03-dossiers/R2-coding-agent-enablement.md",
            "R3": "03-dossiers/R3-support-agent-evaluation.md", "R4": "03-dossiers/R4-workflow-automations.md"}


def econ_block(k):
    """Generated dossier economics tables (kept in sync with models/route_economics.py)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("route_economics", ROOT / "models/route_economics.py")
    m = importlib.util.module_from_spec(spec); sys.modules["route_economics"] = m; spec.loader.exec_module(m)
    cs = ("low", "base", "high")
    r = {c: m.R[k][c] for c in cs}
    st = {c: m.steady_month(r[c]) for c in cs}
    th = {c: m.take_home(st[c]["op_profit"], st[c]["revenue"], r[c].eu_b2b_share, st[c]["cash_costs"]) for c in cs}
    tw = {c: m.twelve_months(r[c]) for c in cs}
    e = lambda x: f"€{x:,.0f}" if x >= 0 else f"−€{abs(x):,.0f}"
    rows = [
        ("Price per engagement (net of VAT) — assumption", lambda c: e(r[c].price) + (f" + {e(r[c].retainer)}/month retainer ({r[c].retain_share:.0%} of clients)" if r[c].retainer else "")),
        ("Engagements won per month once steady", lambda c: f"{r[c].wins_pm:g}"),
        ("Months before first sale", lambda c: f"{r[c].ramp_months}"),
        ("Selling hours per *won* engagement", lambda c: f"{r[c].acquire_h:.0f} h"),
        ("Delivery hours per engagement incl. rework", lambda c: f"{r[c].deliver_h * (1 + r[c].rework):.0f} h"),
        ("One-time setup: cash / owner hours", lambda c: f"{e(r[c].setup_cash)} / {r[c].setup_h:.0f} h"),
        ("Monthly fixed cash costs", lambda c: e(r[c].fixed_pm)),
        ("Revenue per month once steady (net of VAT)", lambda c: e(st[c]["revenue"])),
        ("Operating profit per month once steady", lambda c: e(st[c]["op_profit"])),
        ("Owner hours per month once steady", lambda c: f"{st[c]['hours']:.0f} h"),
        ("**Self-employed take-home per month once steady**", lambda c: e(th[c]["self_employed"])),
        ("Take-home per owner hour once steady", lambda c: f"€{th[c]['self_employed'] / st[c]['hours']:.1f}"),
        ("First 12 months: operating cash before income tax", lambda c: e(tw[c]["cum_cash"])),
        ("First 12 months: owner hours", lambda c: f"{tw[c]['cum_hours']:,.0f} h"),
        ("**First 12 months: take-home per owner hour**", lambda c: m.eph(m.first_year_rates(r[c])[1])),
        ("First 12 months under the combined adverse case", lambda c: m.eph(m.first_year_rates(m.adverse(r[c]))[1])),
    ]
    out = ["*Cases: **low** = adverse inputs; **base** = a newcomer without track record or warm contacts; **high** = with a network or strong public proof. "
           f"Benchmark: about €{m.BENCH_LV_PROF_NET}/h net for an average Latvian professional [S126][S100]; your own contracting rate is the real comparator.*", "",
           "| | Low | Base (newcomer) | High (with network) |", "|---|---|---|---|"]
    out += [f"| {lab} | " + " | ".join(f(c) for c in cs) + " |" for lab, f in rows]
    out.append("")
    out.append(f"Setup and fixed-cost contents (assumption): {m.SETUP_NOTES[k]}.")
    return "\n".join(out)


def fill_dossiers():
    for k, rel in DOSSIERS.items():
        p = PKG / rel
        s = p.read_text()
        s = re.sub(r"<!-- econ:start -->.*?<!-- econ:end -->", lambda _: "<!-- econ:start -->\n" + econ_block(k) + "\n<!-- econ:end -->", s, flags=re.S)
        p.write_text(s)


def build_economics():
    intro = (PKG / "04-economics-intro.md").read_text()
    gen = (ROOT / "models/route_economics_results.md").read_text()
    gen = re.sub(r"^# .*\n", "", gen, count=1)                        # drop generated H1
    gen = re.sub(r"^## ", "### ", gen, flags=re.M)                     # demote
    out = intro + "\n## Detailed tables by route (generated)\n\n" + gen
    out += ("\n## How to change an assumption\n\nEdit the `Route(...)` lines in `models/route_economics.py` "
            "(price, retainer, wins per month, hours, months to first win, costs, client mix) and run "
            "`python3 models/route_economics.py && python3 package/build_package.py`.\n")
    (PKG / "04-economics.md").write_text(out)


def shift_headings(md: str, by: int) -> str:
    """Demote every ATX heading by `by` levels (so each part nests under its own H1)."""
    def rep(m):
        level = min(len(m.group(1)) + by, 6)
        return "#" * level + m.group(2)
    lines, out, fence = md.splitlines(), [], False
    for ln in lines:
        if ln.startswith("```"):
            fence = not fence
        out.append(ln if fence else re.sub(r"^(#{1,6})(\s.*)$", rep, ln))
    return "\n".join(out)


def rewrite_links(md: str) -> str:
    """Point intra-package Markdown links at in-page anchors of the combined edition."""
    targets = {p[2].split("/")[-1]: p[0] for p in PARTS}
    targets["paper.md"] = "paper"
    def rep(m):
        text, href = m.group(1), m.group(2)
        name = href.split("#")[0].split("/")[-1]
        if href.startswith("http"):
            return m.group(0)
        if name in targets:
            return f"[{text}](#{targets[name]})"
        return m.group(0)
    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", rep, md)


def build_html():
    chunks = []
    for anchor, title, rel in PARTS:
        md = (PKG / rel).read_text()
        md = re.sub(r"^# (.*)$", "", md, count=1, flags=re.M)        # replace own H1 with a part heading
        chunks.append(f'\n\n# {title} {{#{anchor} .part}}\n\n' + shift_headings(rewrite_links(md), 1))
    paper = (ROOT / "paper/paper.md").read_text()
    paper = re.sub(r"^---\n.*?\n---\n", "", paper, count=1, flags=re.S)  # strip YAML
    paper = re.sub(r"^# AI Agents and the Market Forming Around Them\s*$", "", paper, count=1, flags=re.M)
    # Paper uses '# Appendices'/'# References' as H1 and '##' for sections -> demote by 1 so all sit under the part H1
    chunks.append('\n\n# Full research paper (v1.2) {#paper .part}\n\n' + shift_headings(paper, 1))
    combined = "\n".join(chunks)
    src = PKG / ".reading-edition.md"
    src.write_text(combined)
    css = PKG / ".reading.css"
    css.write_text(CSS)
    topbar = ('<nav class="topbar">' + "".join(f'<a href="#{a}">{t.split(":")[0]}</a>' for a, t, _ in PARTS[:2])
              + '<a href="#r2">Dossiers</a><a href="#econ">Economics</a><a href="#valid">Validation</a>'
              '<a href="#review">Review</a><a href="#paper">Paper</a><a href="#TOC">Contents</a></nav>')
    hdr = PKG / ".header.html"
    hdr.write_text(topbar)
    cmd = ["pandoc", str(src), "-f", "markdown+pipe_tables+header_attributes+lists_without_preceding_blankline-implicit_figures", "-t", "html5",
           "--standalone", "--embed-resources", "--toc", "--toc-depth=3", "--section-divs",
           "--metadata", "title=AI agents: reading and decision package (v1.2)",
           "--metadata", "lang=en", "--css", str(css), "--include-before-body", str(hdr),
           "-o", str(PKG / "reading-edition.html")]
    subprocess.run(cmd, check=True)
    subprocess.run(["pandoc", str(ROOT / "paper/paper.md"), "-f", "markdown+lists_without_preceding_blankline", "-t", "html5", "--standalone", "--embed-resources",
                    "--toc", "--toc-depth=2", "--css", str(css), "-o", str(ROOT / "paper/paper.html")], check=True)
    for f in (src, css, hdr):
        f.unlink()
    # wrap tables for horizontal scroll on phones
    for path in (PKG / "reading-edition.html", ROOT / "paper/paper.html"):
        h = path.read_text()
        h = re.sub(r"(<table[^>]*>)", r'<div class="table-wrap">\1', h).replace("</table>", "</table></div>")
        path.write_text(h)


if __name__ == "__main__":
    fill_dossiers()
    build_economics()
    if "--md-only" not in sys.argv:
        build_html()
    print("built:", PKG / "04-economics.md", PKG / "reading-edition.html", ROOT / "paper/paper.html")
