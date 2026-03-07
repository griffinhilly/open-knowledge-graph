#!/usr/bin/env python3
"""Visualize the Open Knowledge Graph.

Renders the prerequisite graph as an interactive HTML file or static PNG.

Usage:
    python tools/visualize.py                    # all domains
    python tools/visualize.py --domain math      # single domain
    python tools/visualize.py --course algebra-1  # single course
    python tools/visualize.py --format png       # static image
"""

import sys
import re
import argparse
from pathlib import Path
from collections import defaultdict

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install with: pip install pyyaml")
    sys.exit(1)

try:
    import networkx as nx
except ImportError:
    print("ERROR: networkx required. Install with: pip install networkx")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_DIR = ROOT / "domains"
OUTPUT_DIR = ROOT / "output"


# Color palette for courses (matches Math Academy style)
COURSE_COLORS = {
    "4th-grade": "#FFE0B2",
    "5th-grade": "#FFCC80",
    "prealgebra": "#FFB74D",
    "algebra-1": "#90CAF9",
    "geometry": "#A5D6A7",
    "algebra-2": "#80CBC4",
    "precalculus": "#CE93D8",
    "calculus-1": "#F48FB1",
    "calculus-2": "#EF9A9A",
    "linear-algebra": "#81D4FA",
    "multivariable-calculus": "#B39DDB",
    "methods-of-proof": "#A1887F",
    "probability-and-statistics": "#90A4AE",
    "discrete-math": "#C5E1A5",
}
DEFAULT_COLOR = "#E0E0E0"


def parse_frontmatter(filepath):
    """Extract YAML frontmatter from a Markdown file."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


def load_graph(domain_filter=None, course_filter=None):
    """Load all topics into a NetworkX DiGraph."""
    G = nx.DiGraph()

    for filepath in sorted(DOMAINS_DIR.rglob("*.md")):
        data = parse_frontmatter(filepath)
        if data is None:
            continue

        topic_id = data.get("id")
        domain = data.get("domain", "")
        course = data.get("course", "")

        if domain_filter and domain != domain_filter:
            continue
        if course_filter and course != course_filter:
            continue
        if not topic_id:
            continue

        G.add_node(topic_id, **{
            "title": data.get("title", topic_id),
            "course": course,
            "domain": domain,
            "stage": data.get("stage", ""),
            "status": data.get("status", "draft"),
        })

        for prereq in data.get("prerequisites", []):
            if isinstance(prereq, dict) and "id" in prereq:
                prereq_id = prereq["id"]
                edge_type = prereq.get("type", "hard")
                # Add edge from prerequisite -> this topic (direction of learning flow)
                G.add_edge(prereq_id, topic_id, type=edge_type)

    return G


def render_png(G, output_path):
    """Render graph as static PNG using matplotlib."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
    except ImportError:
        print("ERROR: matplotlib required for PNG. Install with: pip install matplotlib")
        sys.exit(1)

    if len(G.nodes) == 0:
        print("No topics to visualize.")
        return

    # Layout
    try:
        pos = nx.nx_agraph.graphviz_layout(G, prog="dot")
    except Exception:
        # Fallback if graphviz not installed
        pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

    # Node colors by course
    node_colors = []
    for node in G.nodes:
        course = G.nodes[node].get("course", "")
        node_colors.append(COURSE_COLORS.get(course, DEFAULT_COLOR))

    # Draw
    fig, ax = plt.subplots(1, 1, figsize=(20, 16))

    # Separate hard and soft edges
    hard_edges = [(u, v) for u, v, d in G.edges(data=True) if d.get("type") == "hard"]
    soft_edges = [(u, v) for u, v, d in G.edges(data=True) if d.get("type") == "soft"]

    nx.draw_networkx_edges(G, pos, edgelist=hard_edges, alpha=0.4,
                           arrows=True, arrowsize=8, edge_color="#666666", ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=soft_edges, alpha=0.2,
                           arrows=True, arrowsize=8, edge_color="#AAAAAA",
                           style="dashed", ax=ax)
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=60, ax=ax)

    # Labels only if graph is small enough
    if len(G.nodes) <= 80:
        labels = {n: G.nodes[n].get("title", n)[:25] for n in G.nodes}
        nx.draw_networkx_labels(G, pos, labels, font_size=5, ax=ax)

    # Legend
    legend_patches = []
    courses_present = set(G.nodes[n].get("course", "") for n in G.nodes)
    for course in sorted(courses_present):
        if course:
            color = COURSE_COLORS.get(course, DEFAULT_COLOR)
            legend_patches.append(mpatches.Patch(color=color, label=course))
    if legend_patches:
        ax.legend(handles=legend_patches, loc="lower left", fontsize=7)

    ax.set_title(f"Open Knowledge Graph ({len(G.nodes)} topics, {len(G.edges)} edges)")
    ax.axis("off")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {output_path}")


def render_html(G, output_path):
    """Render graph as interactive HTML using D3.js-style force layout via pyvis."""
    try:
        from pyvis.network import Network
    except ImportError:
        print("pyvis not installed. Falling back to PNG.")
        print("Install with: pip install pyvis")
        render_png(G, output_path.with_suffix(".png"))
        return

    net = Network(height="900px", width="100%", directed=True, bgcolor="#ffffff")
    net.barnes_hut(gravity=-3000, central_gravity=0.3, spring_length=100)

    for node in G.nodes:
        data = G.nodes[node]
        course = data.get("course", "")
        color = COURSE_COLORS.get(course, DEFAULT_COLOR)
        title_text = data.get("title", node)
        hover = f"{title_text}\nCourse: {course}\nStage: {data.get('stage', 'N/A')}"
        net.add_node(node, label=title_text, color=color, title=hover, size=12)

    for u, v, d in G.edges(data=True):
        edge_type = d.get("type", "hard")
        if u in G.nodes and v in G.nodes:
            dashes = edge_type == "soft"
            color = "#666666" if edge_type == "hard" else "#CCCCCC"
            net.add_edge(u, v, color=color, dashes=dashes)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    net.save_graph(str(output_path))
    print(f"Saved: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Visualize the Open Knowledge Graph")
    parser.add_argument("--domain", help="Filter by domain (e.g., mathematics)")
    parser.add_argument("--course", help="Filter by course (e.g., algebra-1)")
    parser.add_argument("--format", choices=["html", "png"], default="html",
                        help="Output format (default: html)")
    parser.add_argument("--output", help="Output file path")
    args = parser.parse_args()

    G = load_graph(domain_filter=args.domain, course_filter=args.course)
    print(f"Loaded {len(G.nodes)} topics, {len(G.edges)} edges")

    if len(G.nodes) == 0:
        print("No topics found. Nothing to visualize.")
        return

    if args.output:
        out = Path(args.output)
    else:
        suffix = ".html" if args.format == "html" else ".png"
        name = args.course or args.domain or "full-graph"
        out = OUTPUT_DIR / f"{name}{suffix}"

    if args.format == "png":
        render_png(G, out)
    else:
        render_html(G, out)


if __name__ == "__main__":
    main()
