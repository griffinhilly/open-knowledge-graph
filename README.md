# Open Knowledge Graph

An open-source, machine-readable knowledge graph mapping prerequisite relationships between topics across every domain of human knowledge.

Live site: https://openknowledgegraph.com

## What this is

Most knowledge is taught in fixed sequences, but the actual dependency structure — what you genuinely need to understand before something else — is rarely written down in a usable form. This project maps that structure as a graph: each topic is a node, and each edge is a prerequisite relationship.

The prerequisite graph is a directed acyclic graph (DAG) and is the source of truth for sequencing. It is stored as plain Markdown with YAML frontmatter — one file per topic — so it is readable by humans, diffable in git, and parseable by tools without a database.

## The numbers

| | |
|---|---|
| Topics | ~15,285 |
| Domains | 19 |
| Courses | 261 |
| Developmental stages | 6 (pre-formal → expert) |

All topics are currently at `status: validated`. Counts change as topics are added; `PLAN.md` holds the live figure.

## Repository structure

- `domains/` — the content: 19 domains, each split into courses, each course a directory of topic `.md` files. Each domain has a `_domain.yml` with domain metadata and its course list.
- `tools/` — Python tooling: `validate.py` (schema + cycle checks), the `visualize_*.py` scripts, page/asset generators, sitemap generation, and dedup/reconciliation utilities. Shared parsing lives in `parse_topic.py`.
- `meta/` — schema definition (`schema.md`), the six developmental stages (`developmental-stages.md`), and the full course list (`course-list.md`).
- `hooks/` — git hooks. The pre-push hook runs cycle detection before each push. Enable with `git config core.hooksPath hooks`.
- `output/` — generated HTML visualizations and assets (gitignored).

## Topic schema

Each topic is a Markdown file whose name is its `id` plus `.md` (lowercase, hyphenated). IDs are globally unique across all domains.

Frontmatter — required fields:

```yaml
---
id: adding-fractions-unlike-denominators
title: Adding Fractions with Unlike Denominators
domain: mathematics
course: 5th-grade
prerequisites:
  - id: equivalent-fractions
    type: hard
  - id: least-common-multiple
    type: soft
---
```

Optional fields include `builds-toward`, `stage`, `tags`, `status`, `aliases`, and `external-refs`.

Prerequisite edges are typed:

- `hard` — cannot be meaningfully understood without it; skipping it causes failure.
- `soft` — helpful and enriching, but the topic can be attempted without it.

The Markdown body uses `## Core Idea` (required) plus optional `## How It's Best Learned`, `## Common Misconceptions`, `## Questions` (a YAML block of test questions), `## Explainer`, and `## Notes`.

See [`meta/schema.md`](meta/schema.md) for the full specification, including the questions format and validation rules.

## Using the data

The graph is just Markdown and YAML, so any YAML/Markdown parser can read it directly — no build step or database required. To work with it locally:

```bash
python tools/validate.py           # full validation (warnings + errors)
python tools/validate.py --quick   # errors only: cycles, dupes, schema (~7s)
```

The `tools/` directory also contains the visualization scripts used to render the graph (hierarchy, radial, and domain-map views). Generated output lands in `output/` (gitignored).

## Contributing

Contributions are welcome — fixing a wrong prerequisite, filling in a stub, or adding a missing topic are all useful. Even a stub (frontmatter only) has value, because the prerequisite links are the most important part. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for how to add topics, set up the git hooks, validate locally, and start a new domain.

## License

Dual-licensed:

- Content (`domains/`, `meta/`) — Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
- Code (`tools/`) — MIT

See [`LICENSE`](LICENSE) for full terms.
