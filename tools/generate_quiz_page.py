#!/usr/bin/env python3
"""Generate the interactive quiz page for the OKG learning platform.

Reads assessment-questions.json and lib/fluency.js, then generates
output/quiz.html — a self-contained adaptive quiz that feeds answers
into the fluency model.

Phase 1 (Warm-Up): Cross-domain MC/TF rotation, pre-formal to concrete.
Phase 2 (Exploration): Per-domain adaptive questioning, all stages.
Results: Fluency summary with links to the knowledge graph.

Usage:
    python tools/generate_quiz_page.py
"""

import json
import math
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"
LIB_DIR = ROOT / "lib"
DOMAINS_DIR = ROOT / "domains"

# Import radial layout constants
sys.path.insert(0, str(ROOT / "tools"))
from visualize_radial import DOMAIN_ORDER, DOMAIN_HUES, STAGE_BANDS

DEFAULT_STAGE = "abstract-reasoning"


def _parse_frontmatter(filepath):
    """Parse YAML frontmatter from a markdown file."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


def _load_domain_configs():
    """Load all _domain.yml files."""
    configs = {}
    for domain_dir in sorted(DOMAINS_DIR.iterdir()):
        if domain_dir.is_dir() and (domain_dir / "_domain.yml").exists():
            data = yaml.safe_load(
                (domain_dir / "_domain.yml").read_text(encoding="utf-8")
            )
            courses = data.get("courses", [])
            course_list = []
            for c in courses:
                if isinstance(c, dict) and "id" in c:
                    course_list.append({
                        "id": c["id"],
                        "title": c.get("title", c["id"]),
                        "stage": c.get("stage", DEFAULT_STAGE),
                    })
            configs[domain_dir.name] = {
                "title": data.get("title", domain_dir.name),
                "courses": course_list,
            }
    return configs


def _compute_radial_courses(configs):
    """Pre-compute radial positions for all courses.

    Returns a list of {courseId, courseTitle, domain, domainHue, angle, radius, stage}.
    Uses DOMAIN_ORDER for sector assignment, STAGE_BANDS for radial position.
    """
    n_domains = len(DOMAIN_ORDER)
    sector_width = 2 * math.pi / n_domains
    courses = []

    for di, domain in enumerate(DOMAIN_ORDER):
        if domain not in configs:
            continue
        sector_start = di * sector_width
        domain_courses = configs[domain]["courses"]
        n_courses = len(domain_courses)
        if n_courses == 0:
            continue

        hue = DOMAIN_HUES.get(domain, 0)

        for ci, c in enumerate(domain_courses):
            angle = sector_start + sector_width * ((ci + 0.5) / n_courses)
            stage = c.get("stage", DEFAULT_STAGE)
            band = STAGE_BANDS.get(stage, STAGE_BANDS[DEFAULT_STAGE])
            radius = (band[0] + band[1]) / 2

            courses.append({
                "courseId": c["id"],
                "courseTitle": c["title"],
                "domain": domain,
                "domainHue": hue,
                "angle": round(angle, 4),
                "radius": round(radius, 4),
                "stage": stage,
            })

    return courses


def _build_lightweight_graph():
    """Build a lightweight prerequisite graph for frontier detection.

    Returns {topicId: {prereqs: [...], successors: [...], domain, course, title}}.
    Only includes hard prerequisites.
    """
    all_data = {}
    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        if filepath.name.startswith("_"):
            continue
        data = _parse_frontmatter(filepath)
        if data and "id" in data:
            all_data[data["id"]] = data

    graph = {}
    for tid, data in all_data.items():
        prereqs = []
        for p in data.get("prerequisites", []):
            if isinstance(p, dict) and "id" in p:
                ptype = p.get("type", "hard")
                if ptype == "hard" and p["id"] in all_data:
                    prereqs.append(p["id"])
        graph[tid] = {
            "prereqs": prereqs,
            "successors": [],
            "domain": data.get("domain", ""),
            "course": data.get("course", ""),
            "title": data.get("title", tid),
        }

    # Build successor lists
    for tid, node in graph.items():
        for pid in node["prereqs"]:
            if pid in graph:
                graph[pid]["successors"].append(tid)

    return graph


def _build_course_topics_map():
    """Build {courseId: [topicId, ...]} mapping."""
    course_topics = {}
    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        if filepath.name.startswith("_"):
            continue
        data = _parse_frontmatter(filepath)
        if data and "id" in data:
            course = data.get("course", "")
            if course:
                if course not in course_topics:
                    course_topics[course] = []
                course_topics[course].append(data["id"])
    return course_topics


def generate_quiz_html() -> str:
    """Generate the complete quiz HTML page with embedded data and fluency engine."""
    # Load question data
    data_path = OUTPUT_DIR / "assessment-questions.json"
    if data_path.exists():
        embedded_data = data_path.read_text(encoding="utf-8")
    else:
        embedded_data = "null"
        print("WARNING: assessment-questions.json not found, embedding null")

    # Load fluency engine
    fluency_path = LIB_DIR / "fluency.js"
    if fluency_path.exists():
        fluency_js = fluency_path.read_text(encoding="utf-8")
    else:
        fluency_js = "const OKGFluency = null;"
        print("WARNING: fluency.js not found, fluency tracking disabled")

    # Compute radial course data
    configs = _load_domain_configs()
    radial_courses = _compute_radial_courses(configs)
    radial_courses_json = json.dumps(radial_courses, separators=(",", ":"))

    # Build lightweight prerequisite graph
    graph = _build_lightweight_graph()
    graph_json = json.dumps(graph, separators=(",", ":"))

    # Build course -> topics map
    course_topics = _build_course_topics_map()
    course_topics_json = json.dumps(course_topics, separators=(",", ":"))

    # Domain hues for JS
    domain_hues_json = json.dumps(DOMAIN_HUES, separators=(",", ":"))

    print(f"  Radial courses: {len(radial_courses)}")
    print(f"  Graph nodes: {len(graph)}")
    print(f"  Courses with topics: {len(course_topics)}")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Knowledge Trivia — Open Knowledge Graph</title>
<style>
{_css()}
</style>
</head>
<body>

<div id="app"></div>

<script>
// --- Fluency Engine (embedded) ---
{fluency_js}
</script>

<script>
// --- Quiz Data (embedded) ---
const DATA = {embedded_data};

// --- Results Screen Data (embedded) ---
const RADIAL_COURSES = {radial_courses_json};
const PREREQ_GRAPH = {graph_json};
const COURSE_TOPICS = {course_topics_json};
const DOMAIN_HUES = {domain_hues_json};

// --- Quiz Application ---
{_js()}
</script>

</body>
</html>"""


def _css() -> str:
    return """\
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  background: #1a1a2e; color: #ccc;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  min-height: 100vh;
}

.container {
  max-width: 720px; margin: 0 auto; padding: 40px 20px;
}

h1 { color: #eee; font-size: 28px; margin-bottom: 6px; }
h2 { color: #ddd; font-size: 22px; margin-bottom: 12px; }
.subtitle { color: #777; font-size: 14px; margin-bottom: 32px; }

/* --- Progress bar --- */
.progress-wrap {
  background: rgba(40,40,70,0.6); border-radius: 8px;
  height: 8px; margin-bottom: 24px; overflow: hidden;
}
.progress-bar {
  height: 100%; border-radius: 8px;
  background: linear-gradient(90deg, #4a9eff, #7c4dff);
  transition: width 0.4s ease;
}

/* --- Phase label --- */
.phase-label {
  display: inline-block; padding: 4px 12px; border-radius: 12px;
  font-size: 11px; font-weight: 600; letter-spacing: 0.5px; text-transform: uppercase;
  margin-bottom: 16px;
}
.phase-label.warmup { background: rgba(74,158,255,0.15); color: #4a9eff; }
.phase-label.explore { background: rgba(124,77,255,0.15); color: #7c4dff; }
.phase-label.deep-dive { background: rgba(255,152,0,0.15); color: #FF9800; }

/* --- Domain tag --- */
.domain-tag {
  display: inline-block; padding: 3px 10px; border-radius: 10px;
  font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px;
  margin-bottom: 14px; background: rgba(255,255,255,0.08); color: #999;
}

/* --- Question card --- */
.question-card {
  background: rgba(40,40,70,0.6); border: 1px solid #333;
  border-radius: 12px; padding: 28px 24px; margin-bottom: 20px;
  animation: fadeIn 0.3s ease;
  transition: border-color 0.3s;
}
.question-card.correct { border-color: #4CAF50; }
.question-card.wrong { border-color: #F44336; }

@keyframes fadeIn { from { opacity:0; transform:translateY(8px); } to { opacity:1; transform:translateY(0); } }

.question-text {
  color: #eee; font-size: 17px; line-height: 1.6; margin-bottom: 20px;
}

/* --- Answer buttons --- */
.answers { display: flex; flex-direction: column; gap: 10px; }

.answer-btn {
  background: rgba(50,50,85,0.7); border: 1px solid #444; border-radius: 8px;
  padding: 14px 18px; color: #ccc; font-size: 15px; cursor: pointer;
  transition: all 0.2s ease; text-align: left; position: relative;
}
.answer-btn:hover:not(.disabled) { border-color: #888; background: rgba(60,60,100,0.8); color: #eee; }
.answer-btn.disabled { cursor: default; opacity: 0.7; }
.answer-btn.selected { border-color: #7c4dff; background: rgba(124,77,255,0.15); }
.answer-btn.correct-answer { border-color: #4CAF50; background: rgba(76,175,80,0.15); color: #eee; }
.answer-btn.wrong-answer { border-color: #F44336; background: rgba(244,67,54,0.12); }

.answer-letter {
  display: inline-block; width: 28px; height: 28px; line-height: 28px;
  text-align: center; border-radius: 50%; margin-right: 12px;
  background: rgba(255,255,255,0.08); color: #888; font-weight: 600; font-size: 13px;
}
.answer-btn.correct-answer .answer-letter { background: rgba(76,175,80,0.3); color: #4CAF50; }
.answer-btn.wrong-answer .answer-letter { background: rgba(244,67,54,0.3); color: #F44336; }

/* --- TF buttons --- */
.tf-buttons { display: flex; gap: 12px; }
.tf-btn {
  flex: 1; padding: 16px; border-radius: 8px; font-size: 16px; font-weight: 600;
  cursor: pointer; transition: all 0.2s; text-align: center;
  background: rgba(50,50,85,0.7); border: 1px solid #444; color: #ccc;
}
.tf-btn:hover:not(.disabled) { border-color: #888; }
.tf-btn.disabled { cursor: default; opacity: 0.7; }
.tf-btn.selected { border-color: #7c4dff; background: rgba(124,77,255,0.15); }
.tf-btn.correct-answer { border-color: #4CAF50; background: rgba(76,175,80,0.15); color: #4CAF50; }
.tf-btn.wrong-answer { border-color: #F44336; background: rgba(244,67,54,0.12); color: #F44336; }

/* --- Feedback --- */
.feedback {
  margin-top: 16px; padding: 14px 16px; border-radius: 8px;
  font-size: 13px; line-height: 1.6;
  animation: fadeIn 0.2s ease;
}
.feedback.correct { background: rgba(76,175,80,0.1); border: 1px solid rgba(76,175,80,0.3); color: #a5d6a7; }
.feedback.wrong { background: rgba(244,67,54,0.08); border: 1px solid rgba(244,67,54,0.25); color: #ef9a9a; }
.feedback-icon { font-size: 16px; margin-right: 6px; }

/* --- Next button --- */
.next-btn {
  display: inline-block; margin-top: 16px; padding: 10px 24px; border-radius: 8px;
  background: #3a3a7a; border: 1px solid #555; color: #eee;
  font-size: 14px; cursor: pointer; transition: all 0.2s;
}
.next-btn:hover { background: #4a4a8a; border-color: #777; }

/* --- Action buttons row --- */
.action-row {
  display: flex; gap: 10px; flex-wrap: wrap; margin-top: 12px;
}
.action-btn {
  padding: 8px 16px; border-radius: 6px; font-size: 13px;
  cursor: pointer; transition: all 0.2s; border: 1px solid #444;
  background: rgba(50,50,85,0.5); color: #999;
}
.action-btn:hover { border-color: #777; color: #ccc; }
.action-btn.primary {
  background: #3a3a7a; border-color: #555; color: #eee;
}
.action-btn.primary:hover { background: #4a4a8a; }

/* --- Score display --- */
.score-display {
  display: inline-block; padding: 3px 10px; border-radius: 10px;
  font-size: 12px; font-weight: 600; margin-left: 8px;
  background: rgba(255,255,255,0.06); color: #888;
}

/* --- Intro card --- */
.intro-card {
  background: rgba(40,40,70,0.6); border: 1px solid #333;
  border-radius: 12px; padding: 32px 28px; margin-bottom: 20px;
}
.intro-features { list-style: none; margin: 20px 0 24px; }
.intro-features li {
  color: #aaa; font-size: 14px; line-height: 2;
  padding-left: 24px; position: relative;
}
.intro-features li::before {
  content: attr(data-icon); position: absolute; left: 0;
}

/* --- Domain picker grid --- */
.domain-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 12px; margin-bottom: 24px;
}
.domain-card {
  background: rgba(40,40,70,0.6); border: 1px solid #333;
  border-radius: 10px; padding: 16px 18px; cursor: pointer;
  transition: all 0.2s;
}
.domain-card:hover { border-color: #666; background: rgba(50,50,90,0.6); }
.domain-card.strong { border-left: 4px solid #4CAF50; }
.domain-card.familiar { border-left: 4px solid #FFC107; }
.domain-card.weak { border-left: 4px solid #555; }
.domain-card.explored { opacity: 0.5; }
.domain-card .name { color: #ddd; font-weight: 600; font-size: 14px; margin-bottom: 4px; }
.domain-card .info { color: #777; font-size: 12px; }
.domain-card .bar { height: 3px; border-radius: 2px; margin-top: 8px; background: rgba(255,255,255,0.06); overflow: hidden; }
.domain-card .bar-fill { height: 100%; border-radius: 2px; transition: width 0.3s; }

/* --- Results --- */
.results-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 12px; margin-bottom: 24px;
}
.result-card {
  background: rgba(40,40,70,0.6); border: 1px solid #333;
  border-radius: 10px; padding: 16px 18px;
}
.result-card .domain-name { color: #ddd; font-size: 14px; font-weight: 600; margin-bottom: 4px; }
.result-card .score { font-size: 24px; font-weight: 700; margin-bottom: 2px; }
.result-card .detail { color: #777; font-size: 12px; }

.stat-bar {
  display: flex; align-items: center; gap: 12px; margin-bottom: 10px;
}
.stat-bar .label { color: #999; font-size: 13px; min-width: 100px; }
.stat-bar .bar { flex: 1; height: 8px; border-radius: 4px; background: rgba(255,255,255,0.06); overflow: hidden; }
.stat-bar .bar-fill { height: 100%; border-radius: 4px; }
.stat-bar .value { color: #ccc; font-size: 13px; font-weight: 600; min-width: 40px; text-align: right; }

/* --- Summary card --- */
.summary-card {
  background: rgba(40,40,70,0.6); border: 1px solid #333;
  border-radius: 12px; padding: 28px 24px; margin-bottom: 20px;
}

/* --- Links --- */
.link-row { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 24px; }
.link-btn {
  display: inline-block; padding: 10px 20px;
  background: #2a2a5a; border: 1px solid #555; border-radius: 6px;
  color: #ccc; text-decoration: none; font-size: 14px;
  transition: all 0.2s; cursor: pointer;
}
.link-btn:hover { background: #3a3a6a; border-color: #777; color: #eee; }

/* --- Deep dive --- */
.model-answer-box {
  margin-top: 16px; padding: 18px 20px; border-radius: 8px;
  background: rgba(76,175,80,0.1); border: 1px solid rgba(76,175,80,0.3);
  color: #a5d6a7; font-size: 14px; line-height: 1.7;
  animation: fadeIn 0.3s ease;
}
.model-answer-box .label {
  font-size: 11px; font-weight: 600; text-transform: uppercase;
  letter-spacing: 0.5px; color: #4CAF50; margin-bottom: 8px;
}

.self-grade-row {
  display: flex; gap: 10px; margin-top: 16px; animation: fadeIn 0.3s ease;
}
.grade-btn {
  flex: 1; padding: 14px 12px; border-radius: 8px; font-size: 14px;
  font-weight: 600; cursor: pointer; transition: all 0.2s;
  text-align: center; border: 1px solid;
}
.grade-btn.got-it {
  background: rgba(76,175,80,0.12); border-color: rgba(76,175,80,0.4); color: #4CAF50;
}
.grade-btn.got-it:hover { background: rgba(76,175,80,0.25); }
.grade-btn.partial {
  background: rgba(255,152,0,0.12); border-color: rgba(255,152,0,0.4); color: #FF9800;
}
.grade-btn.partial:hover { background: rgba(255,152,0,0.25); }
.grade-btn.missed {
  background: rgba(244,67,54,0.1); border-color: rgba(244,67,54,0.3); color: #F44336;
}
.grade-btn.missed:hover { background: rgba(244,67,54,0.2); }
.grade-btn.selected { opacity: 1; transform: scale(1.03); }
.grade-btn:not(.selected).faded { opacity: 0.4; cursor: default; }

.reveal-btn {
  display: block; width: 100%; margin-top: 16px; padding: 16px;
  border-radius: 8px; font-size: 15px; font-weight: 600;
  cursor: pointer; transition: all 0.2s; text-align: center;
  background: rgba(255,152,0,0.15); border: 1px solid rgba(255,152,0,0.4);
  color: #FF9800;
}
.reveal-btn:hover { background: rgba(255,152,0,0.3); }

.think-prompt {
  color: #666; font-size: 13px; font-style: italic;
  margin-top: 12px; text-align: center;
}

.deep-answer-input {
  display: block; width: 100%; margin-top: 14px; padding: 12px 14px;
  border-radius: 8px; border: 1px solid #444; resize: vertical;
  background: rgba(50,50,85,0.7); color: #ccc; font-size: 14px;
  font-family: inherit; line-height: 1.6; outline: none;
  transition: border-color 0.2s;
}
.deep-answer-input:focus { border-color: #FF9800; }
.deep-answer-input:read-only { opacity: 0.7; cursor: default; }

.user-answer-box {
  margin-top: 16px; padding: 14px 16px; border-radius: 8px;
  background: rgba(124,77,255,0.08); border: 1px solid rgba(124,77,255,0.25);
  color: #b39ddb; font-size: 14px; line-height: 1.6;
}
.user-answer-box .label {
  font-size: 11px; font-weight: 600; text-transform: uppercase;
  letter-spacing: 0.5px; color: #7c4dff; margin-bottom: 6px;
}
.user-answer-box .text { white-space: pre-wrap; }

/* --- Mini radial canvas --- */
.radial-wrap {
  display: flex; justify-content: center; margin-bottom: 28px;
}
.radial-canvas-container {
  position: relative; width: 580px; height: 580px;
}
.radial-canvas-container canvas {
  display: block; width: 100%; height: 100%;
}

/* --- Domain summary cards --- */
.domain-summary-card {
  background: rgba(40,40,70,0.6); border: 1px solid #333;
  border-radius: 10px; margin-bottom: 12px; overflow: hidden;
}
.domain-summary-header {
  display: flex; justify-content: space-between; align-items: center;
  padding: 14px 18px; cursor: pointer; transition: background 0.2s;
}
.domain-summary-header:hover { background: rgba(50,50,90,0.4); }
.domain-summary-header .name { color: #ddd; font-weight: 600; font-size: 14px; }
.domain-summary-header .stats { display: flex; align-items: center; gap: 12px; }
.domain-summary-header .fluency-bar {
  width: 80px; height: 6px; border-radius: 3px;
  background: rgba(255,255,255,0.06); overflow: hidden;
}
.domain-summary-header .fluency-fill { height: 100%; border-radius: 3px; }
.domain-summary-header .pct { color: #aaa; font-size: 12px; font-weight: 600; min-width: 32px; text-align: right; }
.domain-summary-header .arrow { color: #555; font-size: 12px; transition: transform 0.2s; }
.domain-summary-header.open .arrow { transform: rotate(90deg); }
.domain-summary-body {
  display: none; padding: 0 18px 16px;
}
.domain-summary-body.open { display: block; }
.course-bar-row {
  display: flex; align-items: center; gap: 10px; margin-bottom: 6px;
}
.course-bar-row .course-name { color: #999; font-size: 12px; min-width: 140px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.course-bar-row .bar { flex: 1; height: 6px; border-radius: 3px; background: rgba(255,255,255,0.06); overflow: hidden; }
.course-bar-row .bar-fill { height: 100%; border-radius: 3px; }
.course-bar-row .val { color: #888; font-size: 11px; min-width: 32px; text-align: right; }
.domain-tier { color: #777; font-size: 11px; margin-top: 8px; font-style: italic; }

/* --- Frontier panel --- */
.frontier-panel {
  background: rgba(40,40,70,0.6); border: 1px solid #333;
  border-radius: 12px; padding: 24px; margin-bottom: 20px;
}
.frontier-panel h2 { margin-bottom: 6px; }
.frontier-desc { color: #777; font-size: 13px; margin-bottom: 16px; }
.frontier-list { display: flex; flex-direction: column; gap: 8px; }
.frontier-item {
  display: flex; align-items: center; gap: 12px;
  padding: 10px 14px; border-radius: 8px;
  background: rgba(50,50,85,0.5); border: 1px solid #333;
  transition: border-color 0.2s;
}
.frontier-item:hover { border-color: #555; }
.frontier-item .f-title { flex: 1; color: #ccc; font-size: 13px; }
.frontier-item .f-title a { color: #ccc; text-decoration: none; }
.frontier-item .f-title a:hover { color: #eee; text-decoration: underline; }
.frontier-item .f-badge {
  display: inline-block; padding: 2px 8px; border-radius: 8px;
  font-size: 10px; font-weight: 600; text-transform: uppercase;
  background: rgba(255,255,255,0.06); color: #888; white-space: nowrap;
}
.frontier-item .f-readiness {
  width: 60px; height: 5px; border-radius: 3px;
  background: rgba(255,255,255,0.06); overflow: hidden;
}
.frontier-item .f-readiness-fill { height: 100%; border-radius: 3px; background: #4a9eff; }

/* --- Adjustment sliders --- */
.adjustments-section {
  background: rgba(40,40,70,0.6); border: 1px solid #333;
  border-radius: 12px; margin-bottom: 20px; overflow: hidden;
}
.adjustments-toggle {
  display: flex; justify-content: space-between; align-items: center;
  padding: 14px 20px; cursor: pointer; transition: background 0.2s;
}
.adjustments-toggle:hover { background: rgba(50,50,90,0.4); }
.adjustments-toggle .label { color: #999; font-size: 13px; }
.adjustments-toggle .arrow { color: #555; font-size: 12px; transition: transform 0.2s; }
.adjustments-toggle.open .arrow { transform: rotate(90deg); }
.adjustments-body {
  display: none; padding: 0 20px 20px;
}
.adjustments-body.open { display: block; }
.adj-domain-group { margin-bottom: 16px; }
.adj-domain-group .adj-domain-name { color: #bbb; font-size: 13px; font-weight: 600; margin-bottom: 8px; }
.adj-slider-row {
  display: flex; align-items: center; gap: 10px; margin-bottom: 6px;
}
.adj-slider-row .slider-label { color: #888; font-size: 12px; min-width: 140px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.adj-slider-row input[type=range] {
  flex: 1; height: 4px; -webkit-appearance: none; appearance: none;
  background: rgba(255,255,255,0.1); border-radius: 2px; outline: none;
  cursor: pointer;
}
.adj-slider-row input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none; appearance: none;
  width: 14px; height: 14px; border-radius: 50%;
  background: #7c4dff; cursor: pointer;
}
.adj-slider-row input[type=range]::-moz-range-thumb {
  width: 14px; height: 14px; border-radius: 50%;
  background: #7c4dff; cursor: pointer; border: none;
}
.adj-slider-row .slider-val { color: #aaa; font-size: 11px; min-width: 32px; text-align: right; font-weight: 600; }

/* --- Mobile --- */
@media (max-width: 600px) {
  .container { padding: 24px 14px; }
  h1 { font-size: 22px; }
  .question-card { padding: 20px 16px; }
  .question-text { font-size: 15px; }
  .results-grid { grid-template-columns: 1fr; }
  .domain-grid { grid-template-columns: 1fr 1fr; }
  .tf-buttons { flex-direction: column; }
  .self-grade-row { flex-direction: column; }
  .radial-canvas-container { width: 370px; height: 370px; }
  .course-bar-row .course-name { min-width: 100px; }
  .adj-slider-row .slider-label { min-width: 100px; }
}
"""


def _js() -> str:
    return r"""
'use strict';

// ============================================================
// Constants
// ============================================================
const EXPLORE_PER_DOMAIN = 7;     // questions per domain visit
const TIER_QUESTIONS = 3;         // questions per stage tier before escalation check
const TIER_PROMOTE = 0.6;         // 60%+ correct at a tier → escalate
// No auto-advance — user clicks "Next" manually to avoid misclicks

const STAGES_ORDERED = [
  'pre-formal', 'concrete-operations', 'abstract-reasoning',
  'formal-systems', 'advanced', 'expert'
];
const STAGE_LABELS = {
  'pre-formal':          'Pre-Formal',
  'concrete-operations': 'Concrete Operations',
  'abstract-reasoning':  'Abstract Reasoning',
  'formal-systems':      'Formal Systems',
  'advanced':            'Advanced',
  'expert':              'Expert'
};

const DOMAIN_ORDER = [
  'mathematics', 'formal-sciences-and-logic', 'philosophy', 'computer-science',
  'engineering', 'physics', 'earth-and-space-sciences', 'chemistry', 'biology',
  'health-and-human-development', 'psychology', 'social-sciences',
  'economics', 'history', 'language-and-communication', 'literature',
  'arts-and-aesthetics', 'music'
];

// Median response times (ms) for evidence weighting
const MEDIAN_MC = 12000;
const MEDIAN_TF = 8000;
const MEDIAN_SA = 20000;

// Deep dive
const DEEP_PER_DOMAIN = 7;
const DEEP_STAGE_DIFFICULTY = {
  'formal-systems': 0.6,
  'advanced': 0.8,
  'expert': 0.95
};

// ============================================================
// State
// ============================================================
let S = {
  phase: 'loading',
  // Warmup (adaptive tier escalation)
  warmupPools: {},      // stage -> [questions]
  warmupTier: 0,        // current stage index (0=pre-formal ... 4=advanced)
  warmupTierIndex: 0,   // questions asked at current tier
  warmupTierCorrect: 0, // correct at current tier
  warmupAnswers: [],     // {topicId, domain, correct, responseTimeMs, stage}
  warmupDone: false,
  questionStart: null,
  showingFeedback: false,
  feedbackTimer: null,
  // Exploration
  exploreDomain: null,
  exploreQueue: [],
  exploreIndex: 0,
  exploreAnswers: [],
  exploredDomains: {},  // domain -> {correct, total}
  skippedDomains: {},
  // Deep dive
  deepDomain: null,
  deepQueue: [],
  deepIndex: 0,
  deepAnswers: [],     // {topicId, domain, selfGrade, responseTimeMs, stage}
  deepRevealed: false,
  deepRevealTime: null,
  // Tracking
  usedQuestionKeys: {},  // "topicId::question" -> true
};

// ============================================================
// Rendering helpers
// ============================================================
const app = () => document.getElementById('app');

function h(tag, attrs, ...children) {
  const el = document.createElement(tag);
  if (attrs) {
    for (const [k, v] of Object.entries(attrs)) {
      if (k === 'className') el.className = v;
      else if (k.startsWith('on') && typeof v === 'function') el.addEventListener(k.slice(2).toLowerCase(), v);
      else if (k === 'style' && typeof v === 'object') Object.assign(el.style, v);
      else if (k === 'innerHTML') el.innerHTML = v;
      else el.setAttribute(k, v);
    }
  }
  for (const c of children.flat()) {
    if (c == null || c === false) continue;
    if (typeof c === 'string' || typeof c === 'number') el.appendChild(document.createTextNode(c));
    else if (c instanceof Node) el.appendChild(c);
  }
  return el;
}

function setContent(el) {
  app().innerHTML = '';
  app().appendChild(el);
}

function formatDomain(slug) {
  return slug.replace(/-/g, ' ').replace(/\band\b/g, '&')
    .replace(/\b\w/g, c => c.toUpperCase());
}

function qKey(q) { return q.topicId + '::' + q.question.slice(0, 60); }

// ============================================================
// Shuffle
// ============================================================
function shuffle(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

// ============================================================
// Build warmup pools: one shuffled pool per stage tier
// ============================================================
function buildWarmupPools() {
  const pools = {};
  for (const q of DATA.warmup) {
    if (!pools[q.stage]) pools[q.stage] = [];
    pools[q.stage].push(q);
  }
  // Also pull exploration questions into pools as overflow
  for (const domain in DATA.exploration) {
    for (const q of DATA.exploration[domain]) {
      if (!pools[q.stage]) pools[q.stage] = [];
      pools[q.stage].push(q);
    }
  }
  // Shuffle each pool, rotating domains for variety
  for (const stage in pools) {
    // Sort by domain first, then interleave
    const byDomain = {};
    for (const q of pools[stage]) {
      if (!byDomain[q.domain]) byDomain[q.domain] = [];
      byDomain[q.domain].push(q);
    }
    for (const d in byDomain) shuffle(byDomain[d]);
    const domains = shuffle(Object.keys(byDomain));
    const interleaved = [];
    let round = 0;
    let added = true;
    while (added) {
      added = false;
      for (const d of domains) {
        if (round < byDomain[d].length) {
          interleaved.push(byDomain[d][round]);
          added = true;
        }
      }
      round++;
    }
    pools[stage] = interleaved;
  }
  return pools;
}

// ============================================================
// Build exploration queue for a domain
// ============================================================
function buildExploreQueue(domain) {
  const questions = DATA.exploration[domain];
  if (!questions) return [];

  // Determine the user's floor tier from warmup performance.
  // The highest stage where they got >= 50% correct becomes the floor;
  // skip all stages below it so exploration starts near demonstrated level.
  let floorIndex = 0;
  if (S.warmupAnswers.length > 0) {
    const byStage = {};
    for (const a of S.warmupAnswers) {
      if (!byStage[a.stage]) byStage[a.stage] = {correct: 0, total: 0};
      byStage[a.stage].total++;
      if (a.correct) byStage[a.stage].correct++;
    }
    for (let i = 0; i < STAGES_ORDERED.length; i++) {
      const sp = byStage[STAGES_ORDERED[i]];
      if (sp && sp.total > 0 && sp.correct / sp.total >= 0.5) {
        floorIndex = i;
      }
    }
  }

  // Sort by stage order, then shuffle within stage, skipping below floor
  const stageGroups = {};
  for (const q of questions) {
    if (S.usedQuestionKeys[qKey(q)]) continue;
    if (!stageGroups[q.stage]) stageGroups[q.stage] = [];
    stageGroups[q.stage].push(q);
  }

  const queue = [];
  for (let i = 0; i < STAGES_ORDERED.length; i++) {
    if (i < floorIndex) continue;  // skip stages below demonstrated floor
    const stage = STAGES_ORDERED[i];
    if (stageGroups[stage]) {
      shuffle(stageGroups[stage]);
      queue.push(...stageGroups[stage]);
    }
  }
  return queue;
}

// ============================================================
// Build deep dive queue for a domain
// ============================================================
function buildDeepDiveQueue(domain) {
  if (!DATA.deepDive || !DATA.deepDive[domain]) return [];

  const questions = DATA.deepDive[domain];
  // Sort by stage order (formal-systems -> advanced -> expert), shuffle within
  const byStage = {};
  for (const q of questions) {
    if (S.usedQuestionKeys[qKey(q)]) continue;
    if (!byStage[q.stage]) byStage[q.stage] = [];
    byStage[q.stage].push(q);
  }

  const stageOrder = ['formal-systems', 'advanced', 'expert'];
  const queue = [];
  for (const stage of stageOrder) {
    if (byStage[stage]) {
      shuffle(byStage[stage]);
      queue.push(...byStage[stage]);
    }
  }
  return queue;
}

// ============================================================
// Fluency integration
// ============================================================
function recordAnswer(question, correct, responseTimeMs) {
  if (typeof OKGFluency !== 'undefined' && OKGFluency) {
    OKGFluency.updateTopic(question.topicId, correct, {
      difficulty: question.difficulty || 0.5,
      responseTimeMs: responseTimeMs,
      medianTimeMs: question.type === 'true-false' ? MEDIAN_TF : MEDIAN_MC
    });
  }
  S.usedQuestionKeys[qKey(question)] = true;
}

// ============================================================
// Domain performance analysis
// ============================================================
function domainPerformance() {
  const perf = {};
  const all = [...S.warmupAnswers, ...S.exploreAnswers];
  for (const a of all) {
    if (!perf[a.domain]) perf[a.domain] = {correct: 0, total: 0};
    perf[a.domain].total++;
    if (a.correct) perf[a.domain].correct++;
  }
  // Merge explored domains
  for (const d in S.exploredDomains) {
    if (!perf[d]) perf[d] = {correct: 0, total: 0};
  }
  // Merge deep dive self-grades (selfGrade >= 0.5 counts as correct)
  for (const a of S.deepAnswers) {
    if (!perf[a.domain]) perf[a.domain] = {correct: 0, total: 0};
    perf[a.domain].total++;
    if (a.selfGrade >= 0.5) perf[a.domain].correct++;
  }
  return perf;
}

function domainStrength(perf, domain) {
  const p = perf[domain];
  if (!p || p.total === 0) return 'weak';
  const pct = p.correct / p.total;
  if (pct >= 0.6) return 'strong';
  if (pct >= 0.3) return 'familiar';
  return 'weak';
}

// ============================================================
// Phase: Welcome
// ============================================================
function renderWelcome() {
  const totalQ = DATA.stats.topics_with_questions;

  setContent(h('div', {className: 'container'},
    h('h1', null, 'Knowledge Trivia'),
    h('p', {className: 'subtitle'}, 'A fun way to map what you know'),
    h('div', {className: 'intro-card'},
      h('p', {style: {color: '#bbb', fontSize: '15px', lineHeight: '1.7', marginBottom: '20px'}},
        'This isn\'t a test \u2014 it\'s a trivia game that helps personalize your knowledge map. ' +
        'Answer what you can, skip what you can\'t. Every answer teaches us something about where you are.'
      ),
      h('ul', {className: 'intro-features'},
        h('li', {'data-icon': '\uD83C\uDFAF'}, 'Quick-fire questions across ' + Object.keys(DATA.exploration).length + ' domains'),
        h('li', {'data-icon': '\uD83E\uDDE0'}, 'Your answers color your personal knowledge graph'),
        h('li', {'data-icon': '\u23F1\uFE0F'}, 'Takes about 5\u201310 minutes \u2014 stop anytime'),
        h('li', {'data-icon': '\uD83D\uDD13'}, 'No grades, no pressure, just discovery')
      ),
      h('button', {className: 'next-btn', style: {fontSize: '16px', padding: '14px 32px'}, onClick: startWarmup},
        'Let\'s Play')
    ),
    h('div', {className: 'action-row'},
      h('a', {href: 'assessment.html', className: 'action-btn'}, 'Self-Assessment Instead'),
      h('a', {href: 'index.html', className: 'action-btn'}, 'Browse Graph')
    )
  ));
}

// ============================================================
// Phase: Warmup (adaptive tier escalation)
// ============================================================
// Asks TIER_QUESTIONS per stage tier, then escalates if doing well.
// A college-educated user should breeze through easy tiers in ~6 questions
// and hit their ceiling within ~15 total.

const TIER_LABELS_SHORT = {
  'pre-formal': 'Basics',
  'concrete-operations': 'Elementary',
  'abstract-reasoning': 'Intermediate',
  'formal-systems': 'Advanced',
  'advanced': 'Graduate',
  'expert': 'Expert'
};

function startWarmup() {
  S.phase = 'warmup';
  S.warmupPools = buildWarmupPools();
  S.warmupTier = 0;
  S.warmupTierIndex = 0;
  S.warmupTierCorrect = 0;
  S.warmupAnswers = [];
  S.warmupDone = false;
  S.showingFeedback = false;
  // Skip to lowest tier that has questions
  while (S.warmupTier < STAGES_ORDERED.length &&
         (!S.warmupPools[STAGES_ORDERED[S.warmupTier]] ||
          S.warmupPools[STAGES_ORDERED[S.warmupTier]].length === 0)) {
    S.warmupTier++;
  }
  render();
}

function getWarmupQuestion() {
  // Get next question from current tier's pool
  const stage = STAGES_ORDERED[S.warmupTier];
  const pool = S.warmupPools[stage];
  if (!pool) return null;
  // Find next unused question
  for (let i = 0; i < pool.length; i++) {
    if (!S.usedQuestionKeys[qKey(pool[i])]) return pool[i];
  }
  return null;
}

function advanceTier() {
  // Always advance to the next tier — don't stop on easy misses.
  // Domain-specific questions at lower tiers aren't good indicators
  // of general academic level. The inference uses the HIGHEST tier
  // where the user demonstrated competence across multiple domains,
  // so missing "are ribosomes organelles?" doesn't matter if you
  // later ace formal-systems math.
  S.warmupTier++;
  S.warmupTierIndex = 0;
  S.warmupTierCorrect = 0;
  // Skip tiers with no questions
  while (S.warmupTier < STAGES_ORDERED.length &&
         !getWarmupQuestion()) {
    S.warmupTier++;
  }
}

function renderWarmup() {
  if (S.warmupDone || S.warmupTier >= STAGES_ORDERED.length) {
    showWarmupResults();
    return;
  }

  const q = getWarmupQuestion();
  if (!q) {
    // No more questions at this tier, try next
    S.warmupTier++;
    if (S.warmupTier >= STAGES_ORDERED.length) {
      showWarmupResults();
      return;
    }
    S.warmupTierIndex = 0;
    S.warmupTierCorrect = 0;
    render();
    return;
  }

  const tierLabel = TIER_LABELS_SHORT[STAGES_ORDERED[S.warmupTier]] || '';
  const totalAnswered = S.warmupAnswers.length;
  const totalCorrect = S.warmupAnswers.filter(a => a.correct).length;
  const scoreText = totalAnswered > 0 ? totalCorrect + '/' + totalAnswered : '';

  // Progress: show tier progression (5 tiers)
  const tierProgress = ((S.warmupTier + S.warmupTierIndex / TIER_QUESTIONS) / STAGES_ORDERED.length) * 100;

  setContent(h('div', {className: 'container'},
    h('div', {style: {display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px'}},
      h('h1', {style: {margin: 0}}, 'Knowledge Trivia'),
      scoreText ? h('span', {className: 'score-display'}, scoreText) : null
    ),
    h('p', {className: 'subtitle'},
      tierLabel + ' \u2014 Question ' + (S.warmupTierIndex + 1) + ' of ' + TIER_QUESTIONS +
      ' (Tier ' + (S.warmupTier + 1) + ' of ' + STAGES_ORDERED.length + ')'
    ),
    h('div', {className: 'progress-wrap'},
      h('div', {className: 'progress-bar', style: {width: tierProgress + '%'}})
    ),
    h('span', {className: 'phase-label warmup'}, tierLabel),
    renderQuestionCard(q, 'warmup'),
    h('div', {className: 'action-row'},
      h('button', {className: 'action-btn', onClick: skipWarmupQuestion}, 'Skip'),
      h('button', {className: 'action-btn', onClick: () => { showWarmupResults(); }}, 'I\'m Done')
    )
  ));
  S.questionStart = performance.now();
}

function answerWarmup(q, selectedAnswer) {
  if (S.showingFeedback) return;
  S.showingFeedback = true;

  const responseTimeMs = Math.round(performance.now() - S.questionStart);
  const correct = selectedAnswer === q.answer;

  recordAnswer(q, correct, responseTimeMs);
  S.warmupAnswers.push({
    topicId: q.topicId, domain: q.domain, correct, responseTimeMs,
    stage: q.stage
  });

  S.warmupTierIndex++;
  S.warmupTierCorrect += correct ? 1 : 0;

  showFeedback(q, selectedAnswer, correct, () => {
    S.showingFeedback = false;
    // Check tier escalation after TIER_QUESTIONS at this tier
    if (S.warmupTierIndex >= TIER_QUESTIONS) {
      advanceTier();
    }
    render();
  });
}

function skipWarmupQuestion() {
  if (S.showingFeedback) return;
  const q = getWarmupQuestion();
  if (q) S.usedQuestionKeys[qKey(q)] = true;
  S.warmupTierIndex++;
  if (S.warmupTierIndex >= TIER_QUESTIONS) {
    advanceTier();
  }
  render();
}

function showWarmupResults() {
  S.phase = 'warmup-results';
  render();
}

function renderWarmupResults() {
  const perf = domainPerformance();
  const totalCorrect = S.warmupAnswers.filter(a => a.correct).length;
  const totalAnswered = S.warmupAnswers.length;
  const pct = totalAnswered > 0 ? Math.round(totalCorrect / totalAnswered * 100) : 0;

  // Build domain results sorted by performance
  const domainResults = [];
  for (const d of DOMAIN_ORDER) {
    if (perf[d] && perf[d].total > 0) {
      const p = perf[d];
      domainResults.push({domain: d, correct: p.correct, total: p.total, pct: Math.round(p.correct / p.total * 100)});
    }
  }
  domainResults.sort((a, b) => b.pct - a.pct);

  const hasExploreQuestions = Object.keys(DATA.exploration).length > 0;

  setContent(h('div', {className: 'container'},
    h('h1', null, 'Warm-Up Complete!'),
    h('p', {className: 'subtitle'}, 'You got ' + totalCorrect + ' out of ' + totalAnswered + ' right (' + pct + '%)'),
    h('div', {className: 'summary-card'},
      h('h2', null, 'Domain Breakdown'),
      ...domainResults.map(dr =>
        h('div', {className: 'stat-bar'},
          h('span', {className: 'label'}, formatDomain(dr.domain)),
          h('div', {className: 'bar'},
            h('div', {className: 'bar-fill', style: {
              width: dr.pct + '%',
              background: dr.pct >= 60 ? '#4CAF50' : dr.pct >= 30 ? '#FFC107' : '#666'
            }})
          ),
          h('span', {className: 'value'}, dr.correct + '/' + dr.total)
        )
      )
    ),
    hasExploreQuestions ? h('div', {className: 'intro-card'},
      h('h2', null, 'Ready to Explore Deeper?'),
      h('p', {style: {color: '#999', fontSize: '14px', marginBottom: '16px'}},
        'Pick a domain to dive into harder questions. You can explore as many or as few as you like.'
      ),
      h('button', {className: 'next-btn', style: {fontSize: '16px', padding: '14px 32px'}, onClick: startExplore},
        'Explore Domains')
    ) : null,
    h('div', {className: 'link-row'},
      h('button', {className: 'link-btn', onClick: showResults}, 'See Final Results'),
      h('a', {href: 'radial-graph.html', className: 'link-btn'}, 'View Knowledge Graph')
    )
  ));
}

// ============================================================
// Phase: Exploration
// ============================================================
function startExplore() {
  S.phase = 'explore-pick';
  render();
}

function renderExplorePick() {
  const perf = domainPerformance();

  // Build domain cards
  const strong = [], familiar = [], weak = [];
  for (const d of DOMAIN_ORDER) {
    if (!DATA.exploration[d]) continue;
    if (S.skippedDomains[d]) continue;

    const remaining = DATA.exploration[d].filter(q => !S.usedQuestionKeys[qKey(q)]).length;
    if (remaining === 0) continue;

    const strength = domainStrength(perf, d);
    const explored = S.exploredDomains[d] || null;
    const card = {domain: d, strength, remaining, explored};

    if (strength === 'strong') strong.push(card);
    else if (strength === 'familiar') familiar.push(card);
    else weak.push(card);
  }

  const allCards = [...strong, ...familiar, ...weak];

  if (allCards.length === 0) {
    showResults();
    return;
  }

  function makeCard(c) {
    const p = perf[c.domain];
    const pStr = p && p.total > 0 ? p.correct + '/' + p.total + ' correct' : c.remaining + ' questions';
    const cls = 'domain-card ' + c.strength + (c.explored ? ' explored' : '');
    return h('div', {className: cls, onClick: () => startDomainExplore(c.domain)},
      h('div', {className: 'name'}, formatDomain(c.domain)),
      h('div', {className: 'info'}, pStr + (c.explored ? ' \u2014 explored' : ''))
    );
  }

  setContent(h('div', {className: 'container'},
    h('h1', null, 'Choose a Domain'),
    h('p', {className: 'subtitle'}, 'Pick a domain to explore with harder questions'),
    h('div', {className: 'domain-grid'},
      ...allCards.map(makeCard)
    ),
    h('div', {className: 'link-row'},
      hasDeepDive() ? h('button', {className: 'link-btn', style: {background: 'rgba(255,152,0,0.1)', borderColor: '#FF9800', color: '#FF9800'}, onClick: startDeepPick},
        'Deep Dive \u2192') : null,
      h('button', {className: 'link-btn', onClick: showResults}, 'See Final Results'),
      h('a', {href: 'radial-graph.html', className: 'link-btn'}, 'View Knowledge Graph')
    )
  ));
}

function startDomainExplore(domain) {
  S.phase = 'explore';
  S.exploreDomain = domain;
  S.exploreQueue = buildExploreQueue(domain);
  S.exploreIndex = 0;
  S.showingFeedback = false;
  if (S.exploreQueue.length === 0) {
    S.phase = 'explore-pick';
    render();
    return;
  }
  render();
}

function renderExplore() {
  if (S.exploreIndex >= S.exploreQueue.length || S.exploreIndex >= EXPLORE_PER_DOMAIN) {
    finishDomainExplore();
    return;
  }

  const q = S.exploreQueue[S.exploreIndex];
  const progress = (S.exploreIndex / Math.min(EXPLORE_PER_DOMAIN, S.exploreQueue.length)) * 100;

  // Domain explore score
  const domainAnswers = S.exploreAnswers.filter(a => a.domain === S.exploreDomain);
  const correct = domainAnswers.filter(a => a.correct).length;
  const total = domainAnswers.length;
  const scoreText = total > 0 ? correct + '/' + total : '';

  setContent(h('div', {className: 'container'},
    h('div', {style: {display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px'}},
      h('h1', {style: {margin: 0}}, formatDomain(S.exploreDomain)),
      scoreText ? h('span', {className: 'score-display'}, scoreText) : null
    ),
    h('p', {className: 'subtitle'},
      'Question ' + (S.exploreIndex + 1) + ' of ' + Math.min(EXPLORE_PER_DOMAIN, S.exploreQueue.length) +
      ' \u2014 ' + STAGE_LABELS[q.stage]
    ),
    h('div', {className: 'progress-wrap'},
      h('div', {className: 'progress-bar', style: {width: progress + '%'}})
    ),
    h('span', {className: 'phase-label explore'}, 'Exploration'),
    renderQuestionCard(q, 'explore'),
    h('div', {className: 'action-row'},
      h('button', {className: 'action-btn', onClick: skipExploreQuestion}, 'Skip'),
      h('button', {className: 'action-btn', onClick: () => { S.phase = 'explore-pick'; render(); }}, 'Something Different'),
      h('button', {className: 'action-btn', onClick: () => { S.skippedDomains[S.exploreDomain] = true; S.phase = 'explore-pick'; render(); }}, 'Skip Domain'),
      h('button', {className: 'action-btn', onClick: showResults}, 'I\'m Done')
    )
  ));
  S.questionStart = performance.now();
}

function answerExplore(q, selectedAnswer) {
  if (S.showingFeedback) return;
  S.showingFeedback = true;

  const responseTimeMs = Math.round(performance.now() - S.questionStart);
  const correct = q.type === 'multiple-choice'
    ? selectedAnswer === q.answer
    : selectedAnswer === q.answer;

  recordAnswer(q, correct, responseTimeMs);
  S.exploreAnswers.push({topicId: q.topicId, domain: q.domain, correct, responseTimeMs});

  showFeedback(q, selectedAnswer, correct, () => {
    S.showingFeedback = false;
    S.exploreIndex++;
    render();
  });
}

function skipExploreQuestion() {
  if (S.showingFeedback) return;
  S.usedQuestionKeys[qKey(S.exploreQueue[S.exploreIndex])] = true;
  S.exploreIndex++;
  render();
}

function finishDomainExplore() {
  const domainAnswers = S.exploreAnswers.filter(a => a.domain === S.exploreDomain);
  S.exploredDomains[S.exploreDomain] = {
    correct: domainAnswers.filter(a => a.correct).length,
    total: domainAnswers.length
  };
  S.phase = 'explore-pick';
  render();
}

// ============================================================
// Phase: Deep Dive (self-graded short-answer)
// ============================================================
function hasDeepDive() {
  return DATA.deepDive && Object.keys(DATA.deepDive).length > 0;
}

function startDeepPick() {
  S.phase = 'deep-pick';
  render();
}

function renderDeepPick() {
  const perf = domainPerformance();

  // Build domain cards — show all domains with deep dive questions
  const cards = [];
  for (const d of DOMAIN_ORDER) {
    if (!DATA.deepDive || !DATA.deepDive[d]) continue;

    const remaining = DATA.deepDive[d].filter(q => !S.usedQuestionKeys[qKey(q)]).length;
    if (remaining === 0) continue;

    const strength = domainStrength(perf, d);
    const stages = [...new Set(DATA.deepDive[d].map(q => q.stage))];
    cards.push({domain: d, strength, remaining, stages});
  }

  if (cards.length === 0) {
    showResults();
    return;
  }

  function makeCard(c) {
    const stageStr = c.stages.map(s => STAGE_LABELS[s] || s).join(', ');
    const cls = 'domain-card ' + c.strength;
    return h('div', {className: cls, onClick: () => startDomainDeepDive(c.domain)},
      h('div', {className: 'name'}, formatDomain(c.domain)),
      h('div', {className: 'info'}, c.remaining + ' short-answer questions'),
      h('div', {className: 'info', style: {color: '#666', fontSize: '11px'}}, stageStr)
    );
  }

  setContent(h('div', {className: 'container'},
    h('h1', null, 'Deep Dive'),
    h('p', {className: 'subtitle'}, 'Short-answer questions \u2014 think, reveal, self-grade'),
    h('div', {className: 'intro-card', style: {marginBottom: '20px'}},
      h('p', {style: {color: '#999', fontSize: '14px', lineHeight: '1.7'}},
        'These are open-ended questions from advanced stages. Read each question, think about your answer, ' +
        'then reveal the model answer and grade yourself honestly. This gives much more precise fluency readings ' +
        'than multiple choice.'
      )
    ),
    h('div', {className: 'domain-grid'},
      ...cards.map(makeCard)
    ),
    h('div', {className: 'link-row'},
      h('button', {className: 'link-btn', onClick: showResults}, 'See Final Results'),
      h('a', {href: 'radial-graph.html', className: 'link-btn'}, 'View Knowledge Graph')
    )
  ));
}

function startDomainDeepDive(domain) {
  S.phase = 'deep-dive';
  S.deepDomain = domain;
  S.deepQueue = buildDeepDiveQueue(domain);
  S.deepIndex = 0;
  S.deepRevealed = false;
  S.deepRevealTime = null;
  if (S.deepQueue.length === 0) {
    S.phase = 'deep-pick';
    render();
    return;
  }
  render();
}

function renderDeepDive() {
  if (S.deepIndex >= S.deepQueue.length || S.deepIndex >= DEEP_PER_DOMAIN) {
    S.phase = 'deep-pick';
    render();
    return;
  }

  const q = S.deepQueue[S.deepIndex];
  const progress = (S.deepIndex / Math.min(DEEP_PER_DOMAIN, S.deepQueue.length)) * 100;

  // Score display
  const domainDeep = S.deepAnswers.filter(a => a.domain === S.deepDomain);
  const gotCount = domainDeep.filter(a => a.selfGrade === 1.0).length;
  const totalDone = domainDeep.length;
  const scoreText = totalDone > 0 ? gotCount + '/' + totalDone : '';

  const textarea = document.createElement('textarea');
  textarea.className = 'deep-answer-input';
  textarea.id = 'deep-answer-input';
  textarea.placeholder = 'Write your answer here before revealing — it helps you learn more than just thinking about it...';
  textarea.rows = 4;

  const card = h('div', {className: 'question-card', id: 'qcard'},
    h('span', {className: 'domain-tag'}, formatDomain(q.domain)),
    h('div', {className: 'question-text'}, q.question),
    textarea,
    h('p', {className: 'think-prompt'}, 'Write your answer above, then reveal to compare'),
    h('button', {className: 'reveal-btn', id: 'reveal-btn', onClick: () => revealDeepAnswer(q)},
      'Reveal Answer')
  );

  setContent(h('div', {className: 'container'},
    h('div', {style: {display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px'}},
      h('h1', {style: {margin: 0}}, formatDomain(S.deepDomain)),
      scoreText ? h('span', {className: 'score-display'}, scoreText) : null
    ),
    h('p', {className: 'subtitle'},
      'Question ' + (S.deepIndex + 1) + ' of ' + Math.min(DEEP_PER_DOMAIN, S.deepQueue.length) +
      ' \u2014 ' + STAGE_LABELS[q.stage]
    ),
    h('div', {className: 'progress-wrap'},
      h('div', {className: 'progress-bar', style: {width: progress + '%'}})
    ),
    h('span', {className: 'phase-label deep-dive'}, 'Deep Dive'),
    card,
    h('div', {className: 'action-row'},
      h('button', {className: 'action-btn', onClick: skipDeepQuestion}, 'Skip'),
      h('button', {className: 'action-btn', onClick: () => { S.phase = 'deep-pick'; render(); }}, 'Different Domain'),
      h('button', {className: 'action-btn', onClick: showResults}, 'I\'m Done')
    )
  ));
  S.questionStart = performance.now();
  S.deepRevealed = false;
  S.deepRevealTime = null;
}

function revealDeepAnswer(q) {
  if (S.deepRevealed) return;
  S.deepRevealed = true;
  S.deepRevealTime = performance.now();

  const card = document.getElementById('qcard');
  if (!card) return;

  // Make textarea readonly for comparison
  const inputEl = document.getElementById('deep-answer-input');
  const userText = inputEl ? inputEl.value.trim() : '';
  if (inputEl) inputEl.readOnly = true;

  // Remove think prompt and reveal button
  const prompt = card.querySelector('.think-prompt');
  if (prompt) prompt.remove();
  const revealBtn = document.getElementById('reveal-btn');
  if (revealBtn) revealBtn.remove();

  // Show user's answer (if they typed anything) above model answer
  if (userText) {
    // Remove the textarea and replace with a styled box
    if (inputEl) inputEl.remove();
    const userBox = h('div', {className: 'user-answer-box'},
      h('div', {className: 'label'}, 'Your Answer'),
      h('div', {className: 'text'}, userText)
    );
    card.appendChild(userBox);
  } else if (inputEl) {
    inputEl.remove();
  }

  // Show model answer
  const answerBox = h('div', {className: 'model-answer-box'},
    h('div', {className: 'label'}, 'Model Answer'),
    h('div', null, q.model_answer)
  );
  card.appendChild(answerBox);

  // Show self-grade buttons
  const gradeRow = h('div', {className: 'self-grade-row', id: 'grade-row'},
    h('button', {className: 'grade-btn got-it', onClick: () => gradeDeep(q, 1.0)},
      'Got it \u2713'),
    h('button', {className: 'grade-btn partial', onClick: () => gradeDeep(q, 0.5)},
      'Partially \u223C'),
    h('button', {className: 'grade-btn missed', onClick: () => gradeDeep(q, 0.0)},
      'Missed it \u2717')
  );
  card.appendChild(gradeRow);
}

function gradeDeep(q, selfGrade) {
  // Prevent double-grading
  const gradeRow = document.getElementById('grade-row');
  if (!gradeRow) return;
  const buttons = gradeRow.querySelectorAll('.grade-btn');
  let selectedClass = selfGrade === 1.0 ? 'got-it' : selfGrade === 0.5 ? 'partial' : 'missed';
  buttons.forEach(btn => {
    if (btn.classList.contains(selectedClass)) {
      btn.classList.add('selected');
    } else {
      btn.classList.add('faded');
    }
  });

  const responseTimeMs = Math.round(S.deepRevealTime - S.questionStart);
  const stageDiff = DEEP_STAGE_DIFFICULTY[q.stage] || 0.7;

  // Update fluency based on self-grade
  if (typeof OKGFluency !== 'undefined' && OKGFluency) {
    if (selfGrade === 1.0) {
      OKGFluency.updateTopic(q.topicId, true, {
        difficulty: stageDiff,
        responseTimeMs: responseTimeMs,
        medianTimeMs: MEDIAN_SA
      });
    } else if (selfGrade === 0.5) {
      // Partially correct: true with reduced difficulty (lower evidence)
      OKGFluency.updateTopic(q.topicId, true, {
        difficulty: 0.8,
        responseTimeMs: responseTimeMs,
        medianTimeMs: MEDIAN_SA
      });
    } else {
      OKGFluency.updateTopic(q.topicId, false, {
        difficulty: stageDiff,
        responseTimeMs: responseTimeMs,
        medianTimeMs: MEDIAN_SA
      });
    }
  }

  S.usedQuestionKeys[qKey(q)] = true;
  S.deepAnswers.push({
    topicId: q.topicId,
    domain: q.domain,
    selfGrade: selfGrade,
    responseTimeMs: responseTimeMs,
    stage: q.stage
  });

  // Brief pause, then next question
  setTimeout(() => {
    S.deepIndex++;
    S.deepRevealed = false;
    S.deepRevealTime = null;
    render();
  }, 600);
}

function skipDeepQuestion() {
  if (S.deepRevealed) return;
  S.usedQuestionKeys[qKey(S.deepQueue[S.deepIndex])] = true;
  S.deepIndex++;
  S.deepRevealed = false;
  S.deepRevealTime = null;
  render();
}

// ============================================================
// Question card rendering (shared)
// ============================================================
function renderQuestionCard(q, phase) {
  const answerHandler = phase === 'warmup'
    ? (ans) => answerWarmup(q, ans)
    : (ans) => answerExplore(q, ans);

  const card = h('div', {className: 'question-card', id: 'qcard'},
    h('span', {className: 'domain-tag'}, formatDomain(q.domain)),
    h('div', {className: 'question-text'}, q.question)
  );

  if (q.type === 'multiple-choice' && q.options) {
    const letters = ['A', 'B', 'C', 'D', 'E', 'F'];
    const answersDiv = h('div', {className: 'answers'});
    q.options.forEach((opt, i) => {
      const btn = h('button', {
        className: 'answer-btn',
        id: 'opt-' + i,
        onClick: () => answerHandler(i)
      },
        h('span', {className: 'answer-letter'}, letters[i]),
        String(opt)
      );
      answersDiv.appendChild(btn);
    });
    card.appendChild(answersDiv);
  } else if (q.type === 'true-false') {
    const tfDiv = h('div', {className: 'tf-buttons'},
      h('button', {className: 'tf-btn', id: 'tf-true', onClick: () => answerHandler(true)}, 'True'),
      h('button', {className: 'tf-btn', id: 'tf-false', onClick: () => answerHandler(false)}, 'False')
    );
    card.appendChild(tfDiv);
  }

  return card;
}

// ============================================================
// Feedback display
// ============================================================
function showFeedback(q, selectedAnswer, correct, onDone) {
  const card = document.getElementById('qcard');
  if (!card) { onDone(); return; }

  // Guard against double-fire (timer + click)
  let fired = false;
  function advance() {
    if (fired) return;
    fired = true;
    clearTimeout(S.feedbackTimer);
    onDone();
  }

  card.classList.add(correct ? 'correct' : 'wrong');

  // Highlight answers
  if (q.type === 'multiple-choice') {
    const buttons = card.querySelectorAll('.answer-btn');
    buttons.forEach((btn, i) => {
      btn.classList.add('disabled');
      if (i === q.answer) btn.classList.add('correct-answer');
      if (i === selectedAnswer && !correct) btn.classList.add('wrong-answer');
      if (i === selectedAnswer) btn.classList.add('selected');
    });
  } else {
    const trueBtn = document.getElementById('tf-true');
    const falseBtn = document.getElementById('tf-false');
    if (trueBtn && falseBtn) {
      trueBtn.classList.add('disabled');
      falseBtn.classList.add('disabled');
      if (q.answer === true) trueBtn.classList.add('correct-answer');
      else falseBtn.classList.add('correct-answer');
      if (selectedAnswer === true && !correct) trueBtn.classList.add('wrong-answer');
      if (selectedAnswer === false && !correct) falseBtn.classList.add('wrong-answer');
      if (selectedAnswer === true) trueBtn.classList.add('selected');
      if (selectedAnswer === false) falseBtn.classList.add('selected');
    }
  }

  // Show explanation
  const feedbackDiv = h('div', {className: 'feedback ' + (correct ? 'correct' : 'wrong')},
    h('span', {className: 'feedback-icon'}, correct ? '\u2705' : '\u274C'),
    correct ? 'Correct!' : 'Not quite.',
    q.explanation ? h('span', {style: {display: 'block', marginTop: '6px', fontSize: '12px', color: '#999'}}, q.explanation) : null
  );
  card.appendChild(feedbackDiv);

  // Next button (manual only — no auto-advance to prevent misclicks)
  const nextBtn = h('button', {className: 'next-btn', onClick: advance}, 'Next \u2192');
  card.appendChild(nextBtn);
  nextBtn.focus();
}

// ============================================================
// Phase: Results
// ============================================================
function showResults() {
  S.phase = 'results';

  // Run post-assessment inference before rendering results
  if (typeof OKGFluency !== 'undefined' && OKGFluency && DATA.topicIndex) {
    S.inferenceResult = runInference();
  }

  render();
}

/**
 * Build domain-stage performance map and run inference.
 */
function runInference() {
  const allAnswers = [...S.warmupAnswers, ...S.exploreAnswers];

  // Build domainPerformance: {domain: {stage: {correct, total}}}
  // We need to map answers back to their stage via the question data
  const stagePerf = {};
  for (const a of allAnswers) {
    // Find the question to get its stage
    const q = findQuestionByTopic(a.topicId);
    const stage = q ? q.stage : null;
    if (!stage) continue;

    if (!stagePerf[a.domain]) stagePerf[a.domain] = {};
    if (!stagePerf[a.domain][stage]) stagePerf[a.domain][stage] = {correct: 0, total: 0};
    stagePerf[a.domain][stage].total++;
    if (a.correct) stagePerf[a.domain][stage].correct++;
  }

  // Include deep dive self-grades (selfGrade >= 0.5 counts as correct)
  for (const a of S.deepAnswers) {
    const stage = a.stage;
    if (!stage) continue;
    if (!stagePerf[a.domain]) stagePerf[a.domain] = {};
    if (!stagePerf[a.domain][stage]) stagePerf[a.domain][stage] = {correct: 0, total: 0};
    stagePerf[a.domain][stage].total++;
    if (a.selfGrade >= 0.5) stagePerf[a.domain][stage].correct++;
  }

  return OKGFluency.postAssessmentInference(stagePerf, DATA.topicIndex);
}

function findQuestionByTopic(topicId) {
  // Search warmup, exploration, and deep dive pools
  for (const q of DATA.warmup) {
    if (q.topicId === topicId) return q;
  }
  for (const domain in DATA.exploration) {
    for (const q of DATA.exploration[domain]) {
      if (q.topicId === topicId) return q;
    }
  }
  if (DATA.deepDive) {
    for (const domain in DATA.deepDive) {
      for (const q of DATA.deepDive[domain]) {
        if (q.topicId === topicId) return q;
      }
    }
  }
  return null;
}

// ============================================================
// Component 1: Mini Radial Canvas
// ============================================================
function renderMiniRadial(container) {
  if (typeof RADIAL_COURSES === 'undefined' || !RADIAL_COURSES || !RADIAL_COURSES.length) return;
  if (typeof OKGFluency === 'undefined' || !OKGFluency) return;

  const scores = OKGFluency.loadScores();
  const courseAvg = {};
  for (const rc of RADIAL_COURSES) {
    const topics = COURSE_TOPICS[rc.courseId] || [];
    if (topics.length === 0) { courseAvg[rc.courseId] = 0; continue; }
    let sum = 0;
    for (const tid of topics) sum += (scores[tid] || 0);
    courseAvg[rc.courseId] = sum / topics.length;
  }

  const wrap = h('div', {className: 'radial-wrap'});
  const canvasContainer = h('div', {className: 'radial-canvas-container'});
  const canvas = document.createElement('canvas');
  canvas.width = 580; canvas.height = 580;
  canvasContainer.appendChild(canvas);
  wrap.appendChild(canvasContainer);
  container.appendChild(wrap);

  const ctx = canvas.getContext('2d');
  const cx = 290, cy = 290, maxR = 210;
  ctx.fillStyle = '#1a1a2e';
  ctx.fillRect(0, 0, 580, 580);

  // Faint ring guides
  ctx.strokeStyle = 'rgba(255,255,255,0.04)';
  ctx.lineWidth = 1;
  for (let r = 0.2; r <= 1.0; r += 0.2) {
    ctx.beginPath();
    ctx.arc(cx, cy, r * maxR, 0, Math.PI * 2);
    ctx.stroke();
  }

  // Course dots
  for (const rc of RADIAL_COURSES) {
    const avg = courseAvg[rc.courseId] || 0;
    const x = cx + Math.cos(rc.angle - Math.PI / 2) * rc.radius * maxR;
    const y = cy + Math.sin(rc.angle - Math.PI / 2) * rc.radius * maxR;
    ctx.beginPath();
    ctx.arc(x, y, avg > 0 ? 4 : 2.5, 0, Math.PI * 2);
    ctx.fillStyle = OKGFluency.fluencyColor(rc.domainHue, avg);
    ctx.fill();
  }

  // Domain labels
  const DOMAIN_ABBREVS = {
    'earth-and-space-sciences': 'Earth & Space',
    'formal-sciences-and-logic': 'Formal Sci & Logic',
    'health-and-human-development': 'Health & Human Dev',
    'language-and-communication': 'Language & Comm',
    'arts-and-aesthetics': 'Arts & Aesthetics',
    'practical-life-skills': 'Practical Life',
    'social-sciences': 'Social Sciences',
    'computer-science': 'Computer Science'
  };
  const domainSeen = {};
  ctx.font = '10px -apple-system, BlinkMacSystemFont, sans-serif';
  ctx.textAlign = 'center';
  ctx.textBaseline = 'middle';
  for (const rc of RADIAL_COURSES) {
    if (domainSeen[rc.domain]) continue;
    domainSeen[rc.domain] = true;
    const domCourses = RADIAL_COURSES.filter(c => c.domain === rc.domain);
    let sumAngle = 0;
    for (const dc of domCourses) sumAngle += dc.angle;
    const midAngle = sumAngle / domCourses.length;
    const labelR = maxR + 28;
    const lx = cx + Math.cos(midAngle - Math.PI / 2) * labelR;
    const ly = cy + Math.sin(midAngle - Math.PI / 2) * labelR;
    ctx.save();
    ctx.translate(lx, ly);
    let rot = midAngle - Math.PI / 2;
    if (rot > Math.PI / 2 && rot < Math.PI * 1.5) rot += Math.PI;
    ctx.rotate(rot);
    ctx.fillStyle = 'hsl(' + rc.domainHue + ', 50%, 55%)';
    const label = DOMAIN_ABBREVS[rc.domain] || formatDomain(rc.domain);
    ctx.fillText(label.length > 18 ? label.slice(0, 16) + '..' : label, 0, 0);
    ctx.restore();
  }
}

// ============================================================
// Component 2: Domain Summary Cards
// ============================================================
function renderDomainCards(container, domainPerf, effectiveScores) {
  if (!effectiveScores || typeof COURSE_TOPICS === 'undefined') return;
  const cardsWrap = h('div', null);

  for (const d of DOMAIN_ORDER) {
    const p = domainPerf[d];
    if (!p || p.total === 0) continue;
    let domainSum = 0, domainCount = 0;
    const domainCourses = RADIAL_COURSES.filter(rc => rc.domain === d);
    const courseData = [];
    for (const rc of domainCourses) {
      const topics = COURSE_TOPICS[rc.courseId] || [];
      if (topics.length === 0) continue;
      let cSum = 0;
      for (const tid of topics) { cSum += (effectiveScores[tid] || 0); domainSum += (effectiveScores[tid] || 0); }
      domainCount += topics.length;
      courseData.push({courseId: rc.courseId, title: rc.courseTitle, avg: Math.round(cSum / topics.length), stage: rc.stage});
    }
    const domainAvg = domainCount > 0 ? Math.round(domainSum / domainCount) : 0;
    const accuracy = Math.round(p.correct / p.total * 100);

    // Estimate tier
    const stageOrd = ['pre-formal', 'concrete-operations', 'abstract-reasoning', 'formal-systems', 'advanced', 'expert'];
    let estimatedTier = '';
    for (const stage of stageOrd) {
      const sc = courseData.filter(c => c.stage === stage);
      if (sc.length > 0 && sc.reduce((s, c) => s + c.avg, 0) / sc.length > 50) estimatedTier = STAGE_LABELS[stage] || stage;
    }

    const card = h('div', {className: 'domain-summary-card'});
    const header = h('div', {className: 'domain-summary-header'});
    header.appendChild(h('span', {className: 'name'}, formatDomain(d)));
    const statsDiv = h('div', {className: 'stats'});
    statsDiv.appendChild(h('span', {style: {color: '#777', fontSize: '11px'}}, accuracy + '% acc'));
    const barDiv = h('div', {className: 'fluency-bar'});
    barDiv.appendChild(h('div', {className: 'fluency-fill', style: {width: domainAvg + '%', background: OKGFluency.masteryColor(domainAvg)}}));
    statsDiv.appendChild(barDiv);
    statsDiv.appendChild(h('span', {className: 'pct'}, domainAvg + '%'));
    statsDiv.appendChild(h('span', {className: 'arrow'}, '\u25B6'));
    header.appendChild(statsDiv);

    const body = h('div', {className: 'domain-summary-body'});
    for (const cd of courseData) {
      const row = h('div', {className: 'course-bar-row'});
      row.appendChild(h('span', {className: 'course-name', title: cd.title}, cd.title));
      const bar = h('div', {className: 'bar'});
      bar.appendChild(h('div', {className: 'bar-fill', style: {width: cd.avg + '%', background: OKGFluency.masteryColor(cd.avg)}}));
      row.appendChild(bar);
      row.appendChild(h('span', {className: 'val'}, cd.avg + '%'));
      body.appendChild(row);
    }
    if (estimatedTier) body.appendChild(h('div', {className: 'domain-tier'}, 'Estimated tier: ' + estimatedTier));

    header.addEventListener('click', function() { header.classList.toggle('open'); body.classList.toggle('open'); });
    card.appendChild(header);
    card.appendChild(body);
    cardsWrap.appendChild(card);
  }

  if (cardsWrap.children.length > 0) {
    container.appendChild(h('h2', {style: {marginBottom: '12px'}}, 'Domain Fluency'));
    container.appendChild(cardsWrap);
  }
}

// ============================================================
// Component 3: Manual Adjustment Sliders
// ============================================================
function renderAdjustments(container, domainPerf) {
  if (typeof OKGFluency === 'undefined' || !OKGFluency) return;
  const scores = OKGFluency.loadScores();
  const currentAdj = OKGFluency.loadAdjustments();
  const allAns = [...S.warmupAnswers, ...S.exploreAnswers];
  const answeredTopics = new Set(allAns.map(a => a.topicId));

  const domainGroups = {};
  for (const d of DOMAIN_ORDER) {
    if (!domainPerf[d] || domainPerf[d].total === 0) continue;
    const coursesWithEvidence = [];
    for (const rc of RADIAL_COURSES.filter(rc => rc.domain === d)) {
      const topics = COURSE_TOPICS[rc.courseId] || [];
      if (topics.some(tid => answeredTopics.has(tid) || (scores[tid] && scores[tid] > 0)))
        coursesWithEvidence.push({courseId: rc.courseId, title: rc.courseTitle});
    }
    if (coursesWithEvidence.length > 0) domainGroups[d] = coursesWithEvidence;
  }
  if (Object.keys(domainGroups).length === 0) return;

  const section = h('div', {className: 'adjustments-section'});
  const toggle = h('div', {className: 'adjustments-toggle'});
  toggle.appendChild(h('span', {className: 'label'}, 'This doesn\'t look right? Adjust your estimates'));
  toggle.appendChild(h('span', {className: 'arrow'}, '\u25B6'));

  const body = h('div', {className: 'adjustments-body'});
  body.appendChild(h('p', {style: {color: '#666', fontSize: '12px', marginBottom: '14px'}},
    'Slide to adjust fluency estimates per course. Changes apply immediately and update the results above.'));

  for (const d in domainGroups) {
    const group = h('div', {className: 'adj-domain-group'});
    group.appendChild(h('div', {className: 'adj-domain-name'}, formatDomain(d)));
    for (const c of domainGroups[d]) {
      const row = h('div', {className: 'adj-slider-row'});
      row.appendChild(h('span', {className: 'slider-label', title: c.title}, c.title));
      const curVal = currentAdj[c.courseId] || 0;
      const valSpan = h('span', {className: 'slider-val'}, (curVal >= 0 ? '+' : '') + curVal);
      const slider = document.createElement('input');
      slider.type = 'range'; slider.min = '-30'; slider.max = '30'; slider.value = String(curVal);
      slider.addEventListener('input', function() {
        const v = parseInt(this.value);
        valSpan.textContent = (v >= 0 ? '+' : '') + v;
        const adj = OKGFluency.loadAdjustments();
        if (v === 0) delete adj[c.courseId]; else adj[c.courseId] = v;
        OKGFluency.saveAdjustments(adj);
        reRenderResults();
      });
      row.appendChild(slider);
      row.appendChild(valSpan);
      group.appendChild(row);
    }
    body.appendChild(group);
  }

  toggle.addEventListener('click', function() { toggle.classList.toggle('open'); body.classList.toggle('open'); });
  section.appendChild(toggle);
  section.appendChild(body);
  container.appendChild(section);
}

// ============================================================
// Component 4: Frontier Panel
// ============================================================
function renderFrontier(container, graph, effectiveScores) {
  if (typeof OKGFluency === 'undefined' || !OKGFluency) return;
  if (!graph || Object.keys(graph).length === 0) return;
  // Weight frontier by domains the user explored/deep-dived
  const domainWeights = {};
  const perf = domainPerformance();
  for (const d in perf) {
    if (perf[d].total > 0) domainWeights[d] = 1.5;  // explored
  }
  for (const a of S.deepAnswers) {
    domainWeights[a.domain] = 2.0;  // deep-dived gets stronger boost
  }
  const frontierIds = OKGFluency.findFrontier(graph, effectiveScores, {preferredDomains: domainWeights});
  if (!frontierIds || frontierIds.length === 0) return;

  const top20 = frontierIds.slice(0, 20);
  const panel = h('div', {className: 'frontier-panel'});
  panel.appendChild(h('h2', null, 'Ready to Learn Next'));
  panel.appendChild(h('p', {className: 'frontier-desc'},
    'Topics where you have strong prerequisites but haven\'t learned the topic itself yet.'));
  const list = h('div', {className: 'frontier-list'});

  for (const tid of top20) {
    const node = graph[tid];
    if (!node) continue;
    const prereqs = node.prereqs || [];
    let avgPrereq = 100;
    if (prereqs.length > 0) {
      let sum = 0;
      for (const pid of prereqs) sum += (effectiveScores[pid] || 0);
      avgPrereq = Math.round(sum / prereqs.length);
    }
    const readiness = Math.min(100, Math.max(0, avgPrereq - (effectiveScores[tid] || 0)));
    const item = h('div', {className: 'frontier-item'});
    const hue = DOMAIN_HUES[node.domain] || 0;
    item.appendChild(h('span', {className: 'f-badge', style: {
      background: 'hsla(' + hue + ',40%,40%,0.3)', color: 'hsl(' + hue + ',50%,65%)'
    }}, formatDomain(node.domain)));
    item.appendChild(h('span', {className: 'f-title'},
      h('a', {href: 'topics/' + tid + '.html'}, node.title || tid)));
    const rBar = h('div', {className: 'f-readiness'});
    rBar.appendChild(h('div', {className: 'f-readiness-fill', style: {width: readiness + '%'}}));
    item.appendChild(rBar);
    list.appendChild(item);
  }
  panel.appendChild(list);
  container.appendChild(panel);
}

// ============================================================
// Debounced re-render for adjustment sliders
// ============================================================
let _reRenderTimer = null;
function reRenderResults() {
  if (_reRenderTimer) clearTimeout(_reRenderTimer);
  _reRenderTimer = setTimeout(function() { _reRenderTimer = null; renderResults(); }, 200);
}

// ============================================================
// Results: orchestrate all components
// ============================================================
function renderResults() {
  const mcAnswers = [...S.warmupAnswers, ...S.exploreAnswers];
  const deepCount = S.deepAnswers ? S.deepAnswers.length : 0;
  const allAnswers = deepCount > 0
    ? [...mcAnswers, ...S.deepAnswers.map(a => ({...a, correct: a.selfGrade >= 0.5}))]
    : mcAnswers;
  const totalCorrect = allAnswers.filter(a => a.correct).length;
  const totalAnswered = allAnswers.length;
  const pct = totalAnswered > 0 ? Math.round(totalCorrect / totalAnswered * 100) : 0;

  const perf = domainPerformance();
  const domainResults = [];
  for (const d of DOMAIN_ORDER) {
    const p = perf[d];
    if (!p || p.total === 0) continue;
    domainResults.push({domain: d, correct: p.correct, total: p.total, pct: Math.round(p.correct / p.total * 100)});
  }
  domainResults.sort((a, b) => b.pct - a.pct);

  let fluencySummary = null;
  if (typeof OKGFluency !== 'undefined' && OKGFluency) fluencySummary = OKGFluency.summary();

  const uniqueTopics = new Set(allAnswers.map(a => a.topicId)).size;
  const inf = S.inferenceResult || {topicsInferred: 0, domainsProcessed: 0, crossDomainApplied: false, overallTier: null};

  const TIER_LABELS_R = {
    'pre-formal': 'Early Learner', 'concrete-operations': 'Elementary',
    'abstract-reasoning': 'High School', 'formal-systems': 'College', 'advanced': 'Graduate'
  };

  // Propagate to get effective scores (includes adjustments)
  let effectiveScores = {};
  if (typeof OKGFluency !== 'undefined' && OKGFluency && typeof PREREQ_GRAPH !== 'undefined' && PREREQ_GRAPH) {
    effectiveScores = OKGFluency.propagate(PREREQ_GRAPH);
  }

  const root = h('div', {className: 'container'});

  // --- 1. Summary stats ---
  root.appendChild(h('h1', null, 'Your Results'));
  root.appendChild(h('p', {className: 'subtitle'},
    totalCorrect + ' of ' + totalAnswered + ' correct (' + pct + '%) across ' + uniqueTopics + ' topics'));

  const summaryCard = h('div', {className: 'summary-card'});
  const statsRow = h('div', {style: {display: 'flex', gap: '24px', flexWrap: 'wrap', marginBottom: '16px'}});
  statsRow.appendChild(h('div', null,
    h('div', {style: {fontSize: '32px', fontWeight: '700', color: '#eee'}}, pct + '%'),
    h('div', {style: {color: '#777', fontSize: '12px'}}, 'Accuracy')));
  statsRow.appendChild(h('div', null,
    h('div', {style: {fontSize: '32px', fontWeight: '700', color: '#eee'}}, String(uniqueTopics)),
    h('div', {style: {color: '#777', fontSize: '12px'}}, 'Directly Tested')));
  if (inf.topicsInferred > 0) {
    statsRow.appendChild(h('div', null,
      h('div', {style: {fontSize: '32px', fontWeight: '700', color: '#b39ddb'}}, String(inf.topicsInferred)),
      h('div', {style: {color: '#777', fontSize: '12px'}}, 'Inferred')));
  }
  if (deepCount > 0) {
    statsRow.appendChild(h('div', null,
      h('div', {style: {fontSize: '32px', fontWeight: '700', color: '#FF9800'}}, String(deepCount)),
      h('div', {style: {color: '#777', fontSize: '12px'}}, 'Deep Dive')));
  }
  statsRow.appendChild(h('div', null,
    h('div', {style: {fontSize: '32px', fontWeight: '700', color: '#eee'}}, String(domainResults.length)),
    h('div', {style: {color: '#777', fontSize: '12px'}}, 'Domains Covered')));
  summaryCard.appendChild(statsRow);

  if (inf.overallTier) {
    summaryCard.appendChild(h('p', {style: {color: '#b39ddb', fontSize: '14px', fontWeight: '600', marginBottom: '8px'}},
      'Estimated level: ' + (TIER_LABELS_R[inf.overallTier] || inf.overallTier)));
  }
  if (inf.topicsInferred > 0) {
    summaryCard.appendChild(h('p', {style: {color: '#999', fontSize: '13px', marginBottom: '8px'}},
      'Inferred knowledge for ' + inf.topicsInferred.toLocaleString() +
      ' additional topics across ' + inf.domainsProcessed + ' domains' +
      (inf.crossDomainApplied ? ' (general-education baseline applied).' : '.')));
  }
  if (fluencySummary && fluencySummary.totalTracked > 0) {
    summaryCard.appendChild(h('p', {style: {color: '#999', fontSize: '13px'}},
      fluencySummary.totalTracked.toLocaleString() + ' topics now have fluency scores.'));
  }
  summaryCard.appendChild(h('p', {style: {color: '#666', fontSize: '11px', fontStyle: 'italic', marginTop: '8px'}},
    'Directly tested topics have high confidence. Inferred topics have lower confidence ' +
    'and may not reflect specialized knowledge gaps.' +
    (deepCount > 0 ? ' Deep dive short-answer questions provide the most precise readings.' :
     ' Try the Deep Dive for more precise short-answer readings.')));
  root.appendChild(summaryCard);

  // --- 2. Mini Radial Canvas ---
  renderMiniRadial(root);

  // --- 3. Domain Summary Cards ---
  renderDomainCards(root, perf, effectiveScores);

  // --- 4. Frontier Panel ---
  if (typeof PREREQ_GRAPH !== 'undefined' && PREREQ_GRAPH) {
    renderFrontier(root, PREREQ_GRAPH, effectiveScores);
  }

  // --- 5. Adjustment Sliders ---
  renderAdjustments(root, perf);

  // --- 6. Action Buttons ---
  root.appendChild(h('div', {className: 'link-row'},
    h('button', {className: 'link-btn', onClick: startExplore}, 'Explore More Domains'),
    hasDeepDive() ? h('button', {className: 'link-btn', style: {background: 'rgba(255,152,0,0.1)', borderColor: '#FF9800', color: '#FF9800'}, onClick: startDeepPick},
      'Try Deep Dive') : null,
    h('a', {href: 'radial-graph.html', className: 'link-btn', style: {background: '#2a4a2a', borderColor: '#4CAF50'}},
      'View Full Radial'),
    h('button', {className: 'link-btn', onClick: resetQuiz,
      style: {background: 'rgba(244,67,54,0.1)', borderColor: '#F44336', color: '#F44336'}},
      'Play Again')
  ));

  setContent(root);
}

function resetQuiz() {
  S = {
    phase: 'welcome',
    warmupPools: {},
    warmupTier: 0,
    warmupTierIndex: 0,
    warmupTierCorrect: 0,
    warmupAnswers: [],
    warmupDone: false,
    questionStart: null,
    showingFeedback: false,
    feedbackTimer: null,
    exploreDomain: null,
    exploreQueue: [],
    exploreIndex: 0,
    exploreAnswers: [],
    exploredDomains: {},
    skippedDomains: {},
    deepDomain: null,
    deepQueue: [],
    deepIndex: 0,
    deepAnswers: [],
    deepRevealed: false,
    deepRevealTime: null,
    usedQuestionKeys: {},
  };
  render();
}

// ============================================================
// Main render dispatcher
// ============================================================
function render() {
  switch (S.phase) {
    case 'loading':
      setContent(h('div', {className: 'container'},
        h('div', {style: {textAlign: 'center', padding: '60px 0'}},
          h('div', {style: {
            width: '36px', height: '36px', border: '3px solid #333',
            borderTopColor: '#7c4dff', borderRadius: '50%',
            animation: 'spin 0.8s linear infinite', margin: '0 auto 16px'
          }}),
          h('p', null, 'Loading quiz data...')
        )
      ));
      break;
    case 'welcome':       renderWelcome(); break;
    case 'warmup':        renderWarmup(); break;
    case 'warmup-results': renderWarmupResults(); break;
    case 'explore-pick':  renderExplorePick(); break;
    case 'explore':       renderExplore(); break;
    case 'deep-pick':     renderDeepPick(); break;
    case 'deep-dive':     renderDeepDive(); break;
    case 'results':       renderResults(); break;
    default:
      setContent(h('div', {className: 'container'},
        h('p', {style: {color: '#F44336'}}, 'Unknown phase: ' + S.phase)
      ));
  }
}

// ============================================================
// Boot
// ============================================================
function boot() {
  if (!DATA) {
    setContent(h('div', {className: 'container'},
      h('h1', null, 'Knowledge Trivia'),
      h('p', {style: {color: '#F44336'}},
        'Quiz data not found. Run generate_assessment_questions.py first.')
    ));
    return;
  }
  S.phase = 'welcome';
  render();
}

// Add spin animation
const style = document.createElement('style');
style.textContent = '@keyframes spin { to { transform: rotate(360deg); } }';
document.head.appendChild(style);

render();
boot();
"""


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    html = generate_quiz_html()
    out_path = OUTPUT_DIR / "quiz.html"
    out_path.write_text(html, encoding="utf-8")
    size_kb = len(html.encode("utf-8")) / 1024
    print(f"Generated {out_path} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
