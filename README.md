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

**13,489 topics across 19 domains, 148 courses, 29,596 prerequisite edges.**

| Domain | Topics | Courses |
|--------|--------|---------|
| Mathematics | 1,920 | 28 (Kindergarten through Topology) |
| Computer Science | 1,059 | 11 |
| Biology | 924 | 9 |
| Physics | 856 | 8 |
| Engineering | 722 | 7 |
| Economics | 721 | 7 |
| Philosophy | 706 | 8 |
| Psychology | 679 | 8 |
| Earth & Space Sciences | 640 | 7 |
| Music | 607 | 6 |
| History | 605 | 6 |
| Social Sciences | 577 | 7 |
| Language & Communication | 537 | 6 |
| Health & Human Development | 530 | 6 |
| Chemistry | 527 | 4 |
| Literature | 495 | 6 |
| Practical Life Skills | 482 | 4 |
| Formal Sciences & Logic | 458 | 5 |
| Arts & Aesthetics | 444 | 5 |

## Quick Start

```bash
# Clone the repo
git clone https://github.com/griffinhilly/open-knowledge-graph.git
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

# Generate individual topic detail pages
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
    mathematics/        # 1,920 topics, 28 courses (K through Topology)
    physics/            # 856 topics, 8 courses
    computer-science/   # 1,059 topics, 11 courses
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
    diagnose_positioning.py  # angular displacement analysis
    diagnose_radial_order.py # radial ordering violation finder
    trace_topic.py           # per-topic positioning debugger
    overnight/               # autonomous generation orchestrator
  meta/
    schema.md                # formal schema definition
    developmental-stages.md
    course-list.md
  output/                    # generated HTML (gitignored)
    index.html               # domain card grid
    radial-graph.html        # full cross-domain radial view
    *-hierarchy.html         # per-domain hierarchy views
    topics/                  # 13,489 individual topic pages
  CONTRIBUTING.md
  LICENSE
```

## License

Content is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Code (tools/) is licensed under MIT. See [LICENSE](LICENSE).

## Vision

The prerequisite graph is the skeleton of human knowledge. This project provides a foundation that anyone can build on — curriculum designers, adaptive learning platforms, tutors, or self-directed learners who just want to know: "what should I learn next?"
