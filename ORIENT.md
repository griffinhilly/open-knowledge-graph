# Open Knowledge Graph — Orientation

An open-source, machine-readable prerequisite map across all domains of human knowledge. 13,925 topics across 19 domains, 163 courses, and 6 developmental stages (preschool through graduate research). Each topic is a Markdown file with YAML frontmatter encoding prerequisites (typed hard/soft), builds-toward links, domain, course, and stage. The Markdown body has a Core Idea, explainer, questions, and pedagogical notes. Content is CC BY-SA 4.0; tools are MIT. Live at `griffinhilly.github.io/open-knowledge-graph/`.

## Codebase Shape

- `domains/` — 19 subdirectories, each with `_domain.yml` + course folders containing topic `.md` files
- `tools/` — Python tooling: validation, visualization (hierarchy + radial), topic page generation, assessment/quiz generation, QA analysis, reconciliation, overnight batch orchestrator
- `meta/` — Schema spec, developmental stage definitions, course listing
- `lib/` — `fluency.js` (Bayesian fluency engine for the learning platform), autocomplete lib, vis.js bundle
- `output/` — Generated HTML (gitignored): index page, 19 hierarchy views, radial graph, 13,925 topic pages, quiz, tag pages

## Common Operations

```bash
python tools/validate.py                          # validate schema + graph integrity
python tools/stats.py                             # coverage statistics
python tools/visualize_hierarchy.py --all         # regenerate all 19 domain hierarchies + index
python tools/visualize_radial.py                  # regenerate cross-domain radial view
python tools/generate_topic_pages.py              # regenerate all topic detail pages
python tools/generate_quiz_page.py                # regenerate the quiz
```

GitHub Actions runs validation + deploys visualizations on every push.

## Known Weirdness

- 2,325 edges (8%) violate radial ordering (prereq staged more advanced than successor) — known data debt
- `deploy-pages.yml` does NOT include quiz generation — quiz won't appear on Pages until CI is updated
- `visualize_domain_map.py` exists as a prototype but layout needs v2 (course clustering is broken for large domains)
- Python f-string `\'` doesn't produce `\'` in JS template output — use `"'" +` concatenation
- Inline JSON >700KB in `<script>` tags causes blank pages — use `indent=1` or external `.js` file
- UMAP is broken system-wide (numba/numpy incompatibility), irrelevant here but noted if you try force-directed layouts

## Key Links

- GitHub: `github.com/griffinhilly/open-knowledge-graph`
- Pages: `griffinhilly.github.io/open-knowledge-graph/`
- Schema: `meta/schema.md`
- Contributing: `CONTRIBUTING.md`
- Tools reference: `guides/tools-reference.md`
- Visualization guide: `guides/visualization.md`
- Predecessor project: `~/Projects/griffin/knowledge-architecture/`
