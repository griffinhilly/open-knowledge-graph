# Tools Reference

All tools run from the project root (`open-knowledge-graph/`). Requires Python 3.10+, pyyaml. Optional: networkx, matplotlib, pyvis.

## Validation

```
python tools/validate.py
```
Schema + graph validation. Catches broken refs, cycles, duplicates.

## Visualization

```
python tools/visualize_hierarchy.py --domain mathematics
python tools/visualize_hierarchy.py --course algebra-1
python tools/visualize_hierarchy.py --all
```
Per-domain hierarchical canvas layout (course-band Y-axis, top-to-bottom). `--all` batch-generates all 19 domains + index page.

```
python tools/visualize_radial.py
```
Radial torus visualization. Developmental-stage radial bands, curated domain ordering, polar force simulation. Generates `output/radial-graph.html`.

```
python tools/visualize.py
```
Force-directed graph rendering (pyvis HTML or matplotlib PNG).

```
python tools/generate_topic_pages.py
```
Generates individual topic detail pages in `output/topics/`.

## Assessment & Quiz

```
python tools/generate_assessment.py
```
Selects calibration probes, domain probes, and frontier chains from the topic graph. Outputs `output/assessment-data.json`.

```
python tools/generate_assessment_page.py
```
Generates `output/assessment.html` — self-report placement assessment (3-round adaptive, "I know this" style).

```
python tools/generate_assessment_questions.py
```
Extracts questions from topic markdown files, selects warmup + exploration pools (MC/TF only). Outputs `output/assessment-questions.json`.

```
python tools/generate_quiz_page.py
```
Generates `output/quiz.html` — interactive trivia quiz with actual questions from the question bank. Feeds answers into `lib/fluency.js` with response time tracking. Requires `assessment-questions.json`.

## Statistics & QA

```
python tools/stats.py
```
Coverage statistics.

```
python tools/qa_analyze.py
python tools/qa_analyze.py --json
python tools/qa_analyze.py --domain <name>
```
Structural QA analysis: hubs, longest chains, islands, thin courses, shallow content, bidirectional pairs.

## Reconciliation

```
python tools/reconcile.py --dry-run
python tools/reconcile.py --apply
python tools/reconcile_analyze.py
```
Builds-toward reconciliation. `--dry-run` previews changes; `--apply` executes them. `reconcile_analyze.py` analyzes mismatches for decision-making.

## Overnight Orchestrator

```
python tools/overnight/orchestrator.py
```
Autonomous bulk generation. Invokes `claude --print` per course. Used to build the initial graph. Do not run without understanding its scope — it generates many topics in parallel.
