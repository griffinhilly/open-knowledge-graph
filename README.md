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

| Domain | Topics | Courses | Status |
|--------|--------|---------|--------|
| Mathematics | *in progress* | 14 (4th grade through Discrete Math) | Building |

## Quick Start

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/open-knowledge-graph.git
cd open-knowledge-graph

# Validate the graph (requires Python 3.10+, PyYAML)
pip install pyyaml
python tools/validate.py

# Visualize (requires networkx, matplotlib)
pip install networkx matplotlib
python tools/visualize.py
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add topics, fix errors, or start a new domain.

**The easiest way to contribute:** pick a course you know well, find a topic that's missing, and add it. Even a stub (frontmatter + one-sentence core idea) is valuable.

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
    mathematics/
      4th-grade/          # topics grouped by course
      5th-grade/
      ...
      calculus-2/
  tools/
    validate.py           # schema + graph validation
    visualize.py          # graph rendering
    stats.py              # coverage statistics
  meta/
    schema.md             # formal schema definition
    developmental-stages.md
    course-list.md
  CONTRIBUTING.md
  LICENSE
```

## License

Content is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Code (tools/) is licensed under MIT. See [LICENSE](LICENSE).

## Vision

Mathematics is the starting point. The same schema and tooling can map any domain: physics, chemistry, biology, computer science, language, history, music -- any field where concepts build on each other. The prerequisite graph is the skeleton; the community fills in the body.

The long-term goal is a complete, open, machine-readable map of formalized human knowledge that anyone can use to build curriculum, adaptive learning tools, placement assessments, or just answer the question: "what should I learn next?"
