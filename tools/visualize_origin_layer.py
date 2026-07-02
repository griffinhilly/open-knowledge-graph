#!/usr/bin/env python3
"""Private origin-layer map — the 10 kind:capacity nodes + their edges down to the floored pre-formal
topics. A LOCAL sanity-check surface (NOT published; capacities are excluded from every public surface
per plans/origin-layer-spec.md sec 0.1). Lets Griffin eyeball the funnel/mesh structure before deciding
whether to surface capacities on the public radial.

purpose : render the origin layer (capacity<->capacity build-up + topic->capacity floor edges) as an
          interactive D3 force graph; capacity hubs sized by how many topics depend on them.
inputs  : domains/developmental-origins/precursor-capacities/*.md (the 10 capacities) +
          every pre-formal kind:topic with >=1 capacity prerequisite.
outputs : output/origin-layer-map.html (gitignored; open locally).
last_run: 2026-06-29
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"
OUTPUT_DIR = ROOT / "output"
sys.path.insert(0, str(ROOT / "tools"))
from parse_topic import parse_topic as _parse

CAP_IDS = {"core-objects", "core-agents", "core-number", "core-space", "core-social",
           "discernment-same-different", "grade-seriation", "naming-symbol-reference",
           "classification-sorting", "symbolic-function"}

CAP_SHORT = {
    "core-objects": "Objects", "core-agents": "Agents", "core-number": "Number",
    "core-space": "Space", "core-social": "Social",
    "discernment-same-different": "Discernment", "grade-seriation": "Ordering",
    "naming-symbol-reference": "Naming", "classification-sorting": "Classification",
    "symbolic-function": "Symbolic Thinking",
}

# Build-up tier (for a gentle vertical layout hint): foundations at the bottom, gateway at the top.
CAP_TIER = {
    "core-objects": 0, "core-agents": 0, "core-number": 0, "core-space": 0, "core-social": 0,
    "discernment-same-different": 1, "grade-seriation": 2, "naming-symbol-reference": 3,
    "classification-sorting": 3, "symbolic-function": 4,
}

DOMAIN_HUES = {
    "mathematics": 5, "formal-sciences-and-logic": 157, "philosophy": 309, "computer-science": 100,
    "engineering": 252, "physics": 43, "earth-and-space-sciences": 195, "chemistry": 347,
    "biology": 138, "health-and-human-development": 290, "psychology": 81, "social-sciences": 233,
    "economics": 24, "practical-life-skills": 176, "history": 328, "language-and-communication": 119,
    "literature": 271, "arts-and-aesthetics": 62, "music": 214,
}


def build_graph():
    caps = {}      # id -> dict
    topics = []    # floored pre-formal topics
    for fp in sorted(DOMAINS_DIR.rglob("*.md")):
        if fp.name.startswith("_"):
            continue
        data, _ = _parse(fp)
        if not data:
            continue
        tid = data.get("id")
        if data.get("kind") == "capacity":
            cap_prereqs = [(p.get("id"), p.get("type", "hard")) for p in (data.get("prerequisites") or [])
                           if isinstance(p, dict) and p.get("id") in CAP_IDS]
            caps[tid] = {"id": tid, "title": data.get("title", tid), "prereqs": cap_prereqs}
            continue
        if data.get("stage") != "pre-formal":
            continue
        cap_edges = [(p.get("id"), p.get("type", "hard")) for p in (data.get("prerequisites") or [])
                     if isinstance(p, dict) and p.get("id") in CAP_IDS]
        if cap_edges:
            topics.append({"id": tid, "title": data.get("title", tid),
                           "domain": data.get("domain", "?"), "course": data.get("course", "?"),
                           "caps": cap_edges})

    indeg = {cid: 0 for cid in caps}
    for t in topics:
        for cid, _ in t["caps"]:
            if cid in indeg:
                indeg[cid] += 1

    nodes, links = [], []
    for cid, c in caps.items():
        nodes.append({"id": cid, "label": CAP_SHORT.get(cid, cid), "title": c["title"],
                      "kind": "capacity", "tier": CAP_TIER.get(cid, 0), "indeg": indeg.get(cid, 0)})
    for cid, c in caps.items():
        for pid, ptype in c["prereqs"]:
            links.append({"source": cid, "target": pid, "etype": ptype, "lkind": "cap"})
    for t in topics:
        nodes.append({"id": t["id"], "label": t["title"], "title": t["title"], "kind": "topic",
                      "domain": t["domain"], "course": t["course"],
                      "hue": DOMAIN_HUES.get(t["domain"], 0)})
        for cid, ptype in t["caps"]:
            links.append({"source": t["id"], "target": cid, "etype": ptype, "lkind": "floor"})

    by_domain = {}
    for t in topics:
        by_domain[t["domain"]] = by_domain.get(t["domain"], 0) + 1

    return {"nodes": nodes, "links": links,
            "stats": {"caps": len(caps), "topics": len(topics), "edges": len(links),
                      "by_domain": sorted(by_domain.items(), key=lambda x: -x[1]),
                      "indeg": sorted(indeg.items(), key=lambda x: -x[1])},
            "hues": DOMAIN_HUES}


HTML = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Origin Layer Map (private)</title>
<script src="https://d3js.org/d3.v7.min.js"></script>
<style>
  html,body{margin:0;height:100%;overflow:hidden;background:#08080f;
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;color:#ccc;}
  svg{width:100vw;height:100vh;display:block;cursor:grab;}
  svg:active{cursor:grabbing;}
  .floor-link{stroke:#2a3146;stroke-width:.5;}
  .floor-link.soft{stroke:#222838;stroke-dasharray:2 3;}
  .cap-link{stroke:#caa24a;stroke-width:1.6;stroke-opacity:.55;}
  .cap-link.soft{stroke:#7a6a3a;stroke-dasharray:4 3;stroke-width:1.2;}
  .topic{stroke:#08080f;stroke-width:.4;}
  .cap{stroke:#1a1408;stroke-width:1.5;fill:#f3d27a;}
  .cap-label{fill:#fbe9b8;font-size:12px;font-weight:600;pointer-events:none;
    text-shadow:0 0 5px #000,0 0 8px #000;}
  .cap-sub{fill:#9a8a5a;font-size:9px;pointer-events:none;text-shadow:0 0 4px #000;}
  #hud{position:fixed;top:14px;left:14px;max-width:300px;background:rgba(10,12,22,.82);
    border:1px solid #222838;border-radius:8px;padding:13px 15px;font-size:11px;line-height:1.55;}
  #hud h1{font-size:14px;margin:0 0 4px;color:#f3d27a;font-weight:600;}
  #hud .sub{color:#667;margin-bottom:9px;}
  #hud .row{display:flex;justify-content:space-between;color:#aab;}
  #hud .sec{margin-top:9px;padding-top:8px;border-top:1px solid #1c2230;color:#778;
    text-transform:uppercase;letter-spacing:.5px;font-size:9px;}
  #legend{position:fixed;bottom:12px;left:14px;max-width:46vw;display:flex;flex-wrap:wrap;gap:3px 11px;
    font-size:10px;color:#99a;}
  #legend span{display:flex;align-items:center;gap:4px;}
  #legend i{width:8px;height:8px;border-radius:50%;display:inline-block;}
  #tip{position:fixed;pointer-events:none;background:rgba(8,10,18,.96);border:1px solid #2a3346;
    border-radius:6px;padding:7px 10px;font-size:11px;color:#dde;max-width:260px;display:none;z-index:9;}
  #tip h4{margin:0 0 2px;font-size:12px;color:#fff;} #tip .m{color:#88a;font-size:10px;}
  #tip .b{display:inline-block;margin-top:4px;padding:1px 5px;border-radius:3px;font-size:9px;}
  #tip .b.hard{background:rgba(220,80,80,.16);color:#d77;} #tip .b.soft{background:rgba(80,160,220,.16);color:#7ac;}
  #hint{position:fixed;top:14px;right:16px;font-size:10px;color:#556;text-align:right;line-height:1.5;}
</style></head><body>
<svg></svg>
<div id="hud"></div><div id="legend"></div><div id="tip"></div>
<div id="hint">drag nodes &middot; scroll to zoom &middot; hover a hub to isolate<br>gold = capacity (origin layer) &middot; dots = floored topics</div>
<script>
const DATA = __DATA__;
const W = window.innerWidth, H = window.innerHeight;
const svg = d3.select("svg").attr("viewBox",[0,0,W,H]);
const g = svg.append("g");
svg.call(d3.zoom().scaleExtent([0.2,4]).on("zoom",e=>g.attr("transform",e.transform)));

const capById = {}; DATA.nodes.forEach(n=>{ if(n.kind==="capacity") capById[n.id]=n; });
const maxIndeg = d3.max(DATA.nodes.filter(n=>n.kind==="capacity"),d=>d.indeg)||1;
const capR = d3.scaleSqrt().domain([0,maxIndeg]).range([10,34]);

// gentle vertical hint: foundations low, gateway high (topics float above the floor)
const tierY = t => H*0.86 - t*(H*0.13);

const link = g.append("g").selectAll("line").data(DATA.links).join("line")
  .attr("class",d=> (d.lkind==="cap"?"cap-link":"floor-link") + (d.etype==="soft"?" soft":""));

const node = g.append("g").selectAll("circle").data(DATA.nodes).join("circle")
  .attr("class",d=>d.kind==="capacity"?"cap":"topic")
  .attr("r",d=>d.kind==="capacity"?capR(d.indeg):3.2)
  .attr("fill",d=>d.kind==="capacity"?"#f3d27a":`hsl(${d.hue},58%,55%)`)
  .call(d3.drag().on("start",dragS).on("drag",dragM).on("end",dragE))
  .on("mouseover",hoverIn).on("mouseout",hoverOut);

const labels = g.append("g").selectAll("g").data(DATA.nodes.filter(n=>n.kind==="capacity")).join("g");
labels.append("text").attr("class","cap-label").attr("text-anchor","middle").text(d=>d.label);
labels.append("text").attr("class","cap-sub").attr("text-anchor","middle").attr("dy",13)
  .text(d=>d.indeg+" topics");

const sim = d3.forceSimulation(DATA.nodes)
  .force("link",d3.forceLink(DATA.links).id(d=>d.id)
     .distance(d=>d.lkind==="cap"?70:48).strength(d=>d.lkind==="cap"?0.5:0.12))
  .force("charge",d3.forceManyBody().strength(d=>d.kind==="capacity"?-680:-26))
  .force("x",d3.forceX(W/2).strength(0.04))
  .force("y",d3.forceY(d=>d.kind==="capacity"?tierY(d.tier):H*0.42).strength(d=>d.kind==="capacity"?0.5:0.06))
  .force("collide",d3.forceCollide(d=>d.kind==="capacity"?capR(d.indeg)+6:4.5))
  .on("tick",tick);

function tick(){
  link.attr("x1",d=>d.source.x).attr("y1",d=>d.source.y).attr("x2",d=>d.target.x).attr("y2",d=>d.target.y);
  node.attr("cx",d=>d.x).attr("cy",d=>d.y);
  labels.attr("transform",d=>`translate(${d.x},${d.y-capR(d.indeg)-7})`);
}
function dragS(e,d){ if(!e.active) sim.alphaTarget(0.25).restart(); d.fx=d.x; d.fy=d.y; }
function dragM(e,d){ d.fx=e.x; d.fy=e.y; }
function dragE(e,d){ if(!e.active) sim.alphaTarget(0); if(d.kind!=="capacity"){d.fx=null;d.fy=null;} }

const tip = d3.select("#tip");
const neighborCaps = new Map();   // topicId -> Set(capId)
DATA.links.forEach(l=>{ if(l.lkind==="floor"){ const s=(l.source.id||l.source),t=(l.target.id||l.target);
  if(!neighborCaps.has(s)) neighborCaps.set(s,new Set()); neighborCaps.get(s).add(t); }});

function hoverIn(e,d){
  let html;
  if(d.kind==="capacity"){
    html = `<h4>${d.label}</h4><div class="m">${d.title}</div><div class="m">${d.indeg} topics depend on this</div>`;
    // isolate: dim everything not connected to this capacity
    node.attr("opacity",n=> n===d ? 1 : (n.kind==="topic" && neighborCaps.get(n.id)?.has(d.id) ? 0.95 : (n.kind==="capacity"?0.5:0.06)));
    link.attr("opacity",l=> (l.source===d||l.target===d)?0.9:0.04);
  } else {
    const caps = (d.caps||[]).map(c=>`<span class="b ${c[1]}">${(capById[c[0]]||{}).label||c[0]}</span>`).join(" ");
    html = `<h4>${d.title}</h4><div class="m">${d.domain} &middot; ${d.course}</div>${caps}`;
    node.attr("opacity",n=> n===d?1:(n.kind==="capacity"&&neighborCaps.get(d.id)?.has(n.id)?1:0.12));
    link.attr("opacity",l=> (l.source===d)?0.9:0.04);
  }
  tip.style("display","block").html(html);
}
function hoverOut(){ tip.style("display","none"); node.attr("opacity",1); link.attr("opacity",null); }
svg.on("mousemove",e=>tip.style("left",(e.clientX+14)+"px").style("top",(e.clientY+14)+"px"));

// HUD
const s = DATA.stats;
let hud = `<h1>Origin Layer Map</h1><div class="sub">private &middot; not published</div>`;
hud += `<div class="row"><span>Capacities</span><b>${s.caps}</b></div>`;
hud += `<div class="row"><span>Floored topics</span><b>${s.topics}</b></div>`;
hud += `<div class="row"><span>Edges</span><b>${s.edges}</b></div>`;
hud += `<div class="sec">Load (topics per capacity)</div>`;
const capLbl = {}; DATA.nodes.forEach(n=>{if(n.kind==="capacity")capLbl[n.id]=n.label;});
s.indeg.forEach(([cid,n])=>{ hud += `<div class="row"><span>${capLbl[cid]||cid}</span><b>${n}</b></div>`; });
document.getElementById("hud").innerHTML = hud;

// legend
const leg = d3.select("#legend");
s.by_domain.forEach(([dom,cnt])=>{ leg.append("span").html(
  `<i style="background:hsl(${DATA.hues[dom]||0},58%,55%)"></i>${dom.replace(/-/g," ")} (${cnt})`); });
</script></body></html>"""


def main():
    graph = build_graph()
    OUTPUT_DIR.mkdir(exist_ok=True)
    out = OUTPUT_DIR / "origin-layer-map.html"
    html = HTML.replace("__DATA__", json.dumps(graph))
    out.write_text(html, encoding="utf-8")
    s = graph["stats"]
    print(f"Wrote {out}")
    print(f"  {s['caps']} capacities, {s['topics']} floored topics, {s['edges']} edges")
    print("  Load (topics per capacity):")
    for cid, n in s["indeg"]:
        print(f"    {n:3d}  {CAP_SHORT.get(cid, cid)}")


if __name__ == "__main__":
    main()
