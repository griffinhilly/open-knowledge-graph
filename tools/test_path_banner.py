"""Purpose: regression test for the radial path banner (path engine, PLAN item 3).
Checks, in headless Chrome against the built page:
  1. No banner state clips its text (the no-path fallback's payload — the shared
     foundation's name — must be readable at every desktop and mobile width).
  2. A deep link (?path= / ?ancestry= / ?focus=) naming an unknown topic shows an
     explicit banner instead of failing silently.
Inputs: output/radial-graph.html + output/js/graph.js (build with
  `python tools/visualize_hierarchy.py --index-only && python tools/visualize_radial.py`).
Outputs: none (exit 0 = pass, 1 = fail).
last_run: 2026-11-06
Usage: python tools/test_path_banner.py
"""
import functools, http.server, pathlib, socketserver, sys, threading
from playwright.sync_api import sync_playwright

OUT = pathlib.Path(__file__).resolve().parent.parent / "output"
WIDTHS = [(1024, 768), (1280, 800), (1400, 900), (1920, 1080), (390, 844)]
PAIRS = {
    "fork": "?path=linear-regression-ml,sonata-form-advanced",
    "disjoint": "?path=dislocation-motion-and-slip,switching-basics",
    "bridge": "?path=biosignatures-exoplanet-atmospheres,sound-intensity-and-decibels",
    "ancestry": "?ancestry=linear-regression-ml",
}
MISSING = {
    "path_unknown": ("?path=linear-regression-ml,not-a-real-topic", "not-a-real-topic"),
    "path_one_id": ("?path=linear-regression-ml", None),
    "ancestry_unknown": ("?ancestry=no-such-topic-xyz", "no-such-topic-xyz"),
    "focus_unknown": ("?focus=no-such-topic-xyz", "no-such-topic-xyz"),
}
BANNER_JS = """() => { const b = document.getElementById('pathBanner');
  const s = b && b.querySelector('span');
  return { shown: !!b && b.style.display === 'flex', text: b ? b.innerText : '',
           clipped: !!s && (s.scrollWidth > s.clientWidth + 1 || s.scrollHeight > s.clientHeight + 1),
           offscreen: !!b && (b.getBoundingClientRect().left < 0 || b.getBoundingClientRect().right > innerWidth) }; }"""


def serve():
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    handler = functools.partial(Quiet, directory=str(OUT))
    srv = socketserver.TCPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def load(page, url, need_banner=True):
    page.goto(url)
    page.wait_for_function("() => typeof nodeMap !== 'undefined' && Object.keys(nodeMap).length > 1000", timeout=60000)
    if need_banner:
        try:
            page.wait_for_function("() => document.getElementById('pathBanner').style.display === 'flex'", timeout=20000)
        except Exception:
            pass
    page.wait_for_timeout(300)


def main():
    if not (OUT / "radial-graph.html").exists():
        print("FAIL: output/radial-graph.html missing — build it first"); return 1
    srv = serve()
    base = f"http://127.0.0.1:{srv.server_address[1]}/radial-graph.html"
    fails = []
    with sync_playwright() as p:
        br = p.chromium.launch()
        for w, h in WIDTHS:
            page = br.new_context(viewport={"width": w, "height": h}).new_page()
            for name, q in PAIRS.items():
                load(page, base + q)
                r = page.evaluate(BANNER_JS)
                if not r["shown"]:
                    fails.append(f"{w}px {name}: banner not shown")
                elif r["clipped"] or r["offscreen"]:
                    fails.append(f"{w}px {name}: banner text clipped/offscreen: {r['text'][:90]!r}")
            page.context.close()
        page = br.new_context(viewport={"width": 1400, "height": 900}).new_page()
        for name, (q, must_name) in MISSING.items():
            load(page, base + q)
            r = page.evaluate(BANNER_JS)
            if not r["shown"]:
                fails.append(f"{name}: no banner for a broken deep link ({q})")
            elif must_name and must_name not in r["text"]:
                fails.append(f"{name}: banner does not name the missing id: {r['text'][:90]!r}")
        br.close()
    srv.shutdown()
    for f in fails:
        print("FAIL:", f)
    print("ALL PASS" if not fails else f"{len(fails)} failure(s)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
