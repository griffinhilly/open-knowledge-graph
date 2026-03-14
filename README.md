# Open Knowledge Graph

An open-source, machine-readable map of prerequisite relationships between topics across every domain of human knowledge. Think Wikipedia, but for the *structure* of what you need to learn and in what order.

## Why This Exists

Knowing what to learn next is one of the hardest problems in education. Paid platforms like Math Academy have built sophisticated knowledge graphs that power adaptive learning -- but their graphs are proprietary. Meanwhile, free resources like Khan Academy and Wikipedia organize content by subject but don't expose the fine-grained prerequisite structure that makes personalized learning paths possible.

This project aims to build that prerequisite map in the open, so anyone can use it, contribute to it, and build tools on top of it.

## What's in the Graph

Each **topic** is a Markdown file with YAML frontmatter that encodes:
- **What it is** (title, core idea)
- **What you need to know first** (prerequisite links, typed as hard or soft)
- **What it unlocks** (builds-toward links)
- **Where it fits** (domain, course, developmental stage, tags)

The Markdown body contains a human-readable explanation, pedagogical notes, and common misconceptions.

## Current Coverage

**2,628 topics across 19 domains, 101 courses, 7,563+ prerequisite edges.** All topics at `status: validated`.

| Domain | Topics | Courses |
|--------|--------|---------|
| Mathematics | 661 | 18 (Kindergarten through Discrete Math) |
| Computer Science | 170 | 6 |
| Physics | 163 | 5 |
| Biology | 134 | 5 |
| History | 127 | 5 |
| Philosophy | 124 | 6 |
| Economics | 120 | 4 |
| Engineering | 115 | 5 |
| Chemistry | 112 | 4 |
| Psychology | 111 | 5 |
| Literature | 105 | 5 |
| Music | 102 | 5 |
| Earth & Space Sciences | 89 | 4 |
| Language & Communication | 89 | 4 |
| Health & Human Development | 85 | 4 |
| Formal Sciences & Logic | 81 | 4 |
| Social Sciences | 80 | 4 |
| Arts & Aesthetics | 80 | 4 |
| Practical Life Skills | 80 | 4 |

## Quick Start

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/open-knowledge-graph.git
cd open-knowledge-graph

# Validate the graph (requires Python 3.10+, PyYAML)
pip install pyyaml
python tools/validate.py

# View coverage stats
python tools/stats.py

# Generate all visualizations (19 domain hierarchies + index page)
python tools/visualize_hierarchy.py --all

# Generate radial cross-domain visualization
python tools/visualize_radial.py

# Generate individual topic detail pages (2,628 pages)
python tools/generate_topic_pages.py

# Or visualize a single domain
python tools/visualize_hierarchy.py --domain mathematics
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add topics, fix errors, or start a new domain.

**The easiest way to contribute:** pick a course you know well, find a topic that's missing or incomplete, and improve it. Expert review and corrections are among the highest-impact contributions.

## Schema

Every topic file follows the schema defined in [meta/schema.md](meta/schema.md). The key ideas:

- One `.md` file per topic
- YAML frontmatter for machine-readable fields
- Markdown body for human-readable content
- Prerequisites are typed (`hard` or `soft`) and link by topic ID
- File name = topic ID

## Project Structure

```
open-knowledge-graph/
  domains/
    mathematics/        # 661 topics, 18 courses (K through Discrete Math)
    physics/            # 163 topics, 5 courses
    computer-science/   # 170 topics, 6 courses
    ... (19 domains total)
  tools/
    validate.py              # schema + graph validation
    visualize_hierarchy.py   # per-domain hierarchical canvas graphs
    visualize_radial.py      # radial cross-domain torus visualization
    generate_topic_pages.py  # individual topic detail page generator
    visualize.py             # alternative force-directed rendering
    stats.py                 # coverage statistics
    qa_analyze.py            # structural QA analysis
    reconcile.py             # builds-toward reconciliation
    reconcile_analyze.py     # mismatch analysis
    overnight/               # autonomous generation orchestrator
  meta/
    schema.md                # formal schema definition
    developmental-stages.md
    course-list.md
  output/                    # generated HTML (gitignored)
    index.html               # domain card grid
    radial-graph.html        # full cross-domain radial view
    *-hierarchy.html         # per-domain hierarchy views
    topics/                  # 2,628 individual topic pages
  CONTRIBUTING.md
  LICENSE
```

## License

Content is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Code (tools/) is licensed under MIT. See [LICENSE](LICENSE).

## Vision

The prerequisite graph is the skeleton of human knowledge. This project provides a foundation that anyone can build on — curriculum designers, adaptive learning platforms, tutors, or self-directed learners who just want to know: "what should I learn next?"
