# Open Knowledge Graph — Orientation

An open-source, machine-readable prerequisite map across all domains of human knowledge. 15,285 topics across 19 domains, 261 courses, and 6 developmental stages (preschool through graduate research). Each topic is a Markdown file with YAML frontmatter encoding prerequisites (typed hard/soft), builds-toward links, domain, course, and stage. The Markdown body has a Core Idea, explainer, questions, and pedagogical notes. Content is CC BY-SA 4.0; tools are MIT. Live at `openknowledgegraph.com`.

## Codebase Shape

- `domains/` — 19 subdirectories, each with `_domain.yml` + course folders containing topic `.md` files. PLUS a hidden 20th meta-domain `developmental-origins/` holding the 10 `kind: capacity` origin-layer nodes (a private substrate beneath the pre-formal floor — in the prereq graph, out of every public surface). See `plans/origin-layer-spec.md`.
- `tools/` — Python tooling: validation, visualization (domain maps + radial), topic page generation, assessment/quiz generation, leaf connector, dedup, QA analysis, reconciliation, overnight batch orchestrator
- `hooks/` — Git hooks (`pre-push`: cycle detection + CI script check, ~7s). Setup: `git config core.hooksPath hooks`
- `meta/` — Schema spec, developmental stage definitions, course listing
- `lib/` — `fluency.js` (Bayesian fluency engine + learning path engine + goal system), autocomplete lib, vis.js bundle
- `output/` — Generated HTML (gitignored): index page, 19 domain maps, radial graph, 15,285 topic pages, quiz, assessment, tag pages, keystones leaderboard, `js/graph.js` (prerequisite graph for client-side path computation)
- `guides/` — tools-reference.md, visualization.md

## Common Operations

```bash
python tools/validate.py                          # full validation (schema + graph + warnings)
python tools/validate.py --quick                   # errors only: cycles, dupes, schema (~7s)
python tools/visualize_hierarchy.py --index-only   # regenerate index page only
python tools/visualize_radial.py                   # regenerate cross-domain radial view
python tools/generate_topic_pages.py               # regenerate all topic detail pages
python tools/visualize_domain_map.py --all         # regenerate all 19 domain maps
python tools/generate_quiz_page.py                 # regenerate the quiz (needs assessment-questions.json)
python tools/connect_leaves.py --min-score 0.35    # propose leaf topic connections (dry-run)
python tools/dedup_pairs.py                        # deduplicate flagged pairs (dry-run)
python tools/wire_capacities.py --report           # origin layer: anti-collapse gate + connectivity (--apply to wire)
node   tools/test_fluency_capacity.js              # origin layer: fluency assumed-known regression test
python tools/visualize_origin_layer.py             # PRIVATE origin-layer map → output/origin-layer-map.html (internal only)
python tools/visualize_radial.py --with-origins    # PRIVATE radial w/ capacities at center → output/radial-with-origins.html
```

The origin-layer floor is wired: 307/314 pre-formal topics carry a direct `kind:capacity` prereq (the other 7 reach one transitively). The two `--with-origins` / origin-layer maps are PRIVATE/internal — capacities are the central hub of the graph but get no public radial wedge and never render or index. The capacity-spine extension direction (faculty engine as a private validation-gated truth-test) is in `plans/capacity-spine-synthesis-2026-06-30.md`.

CI pipeline (`deploy-pages.yml`): validate → index → radial → topic pages → domain maps → assessment data → assessment page → quiz question bank → quiz page → deploy to Pages.

## Known Weirdness

- Domain maps are the primary navigation — hierarchy views still exist in the codebase but are not linked or generated in CI
- `visualize_radial.py` imports `COURSE_BRANCH_X` from `visualize_domain_map.py` — they share the branch axis data
- Pre-push hook runs `validate.py --quick` only when `domains/` files are in the push range
- Broad text replace during dedup can corrupt IDs if delete_id is substring of keep_id — always validate after
- 394 dangling cross-domain refs (pre-existing) — mostly course names used as prereq IDs
- Python f-string `\'` doesn't produce `\'` in JS template output — use `"'" +` concatenation
- Inline JSON >700KB in `<script>` tags causes blank pages — use `indent=1` or external `.js` file

## Key Links

- GitHub: `github.com/griffinhilly/open-knowledge-graph`
- Site: `openknowledgegraph.com` (GitHub Pages, custom domain)
- Schema: `meta/schema.md`
- Contributing: `CONTRIBUTING.md`
- Tools reference: `guides/tools-reference.md`
- Visualization guide: `guides/visualization.md`
- Predecessor project: `~/Projects/griffin/knowledge-architecture/`
