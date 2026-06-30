# Commit plan — origin-layer floor + Discernment + capacity-spine (Jun 30, 2026)

**Purpose:** Vetted `git add` allowlist for the uncommitted Jun-30 origin-layer work. The working tree has 2 unrelated dirty scratch files + ~420 untracked scratch files; a careless `git add -A`/`git add .` would sweep them in (and the pre-push/pre-commit hooks block those two forms anyway). Execute this exact list instead of re-deciding. Verified against `git status` on 2026-06-30.

## SAFE TO STAGE (run these exact commands)

```bash
# 1. All wired pre-formal topic files + the capacity rename (delete old slug + add new).
#    Only untracked file under domains/ is the renamed discernment node — safe to add the whole dir.
git add domains/

# 2. The four tool files (EXPLICIT — do NOT `git add tools/`, it would sweep tools/overnight/ scratch).
git add tools/wire_capacities.py tools/validate.py tools/visualize_radial.py tools/visualize_origin_layer.py

# 3. COMP files.
git add CLAUDE.md MEMORY.md ORIENT.md PLAN.md

# 4. Plan/spec docs (EXPLICIT — do NOT `git add plans/`, it would sweep plans/corpus-debt-triage.md
#    which is from Jun 19 and unrelated).
git add plans/origin-layer-spec.md plans/origin-layer-wiring-review.md \
        plans/capacity-spine-ideate-2026-06-30.md plans/capacity-spine-synthesis-2026-06-30.md \
        plans/commit-plan-origin-layer.md

# 5. Verify ONLY origin-layer files are staged before committing:
git status --short
```

## MUST NOT STAGE (leave dirty/untracked)
- `tools/overnight/progress.json`, `tools/overnight/run.log` — tracked-but-dirty scratch from overnight runs, NOT this session.
- `plans/corpus-debt-triage.md` — untracked, dated Jun 19, unrelated prior work.
- everything else under `tools/overnight/` (~400 untracked shards/checkpoints/logs) and any other untracked scratch.
- the parallel RL-learning session's changes, if any remain (that session was read-only on files, but double-check the staged list).

## Rename note
`discrimination-same-different.md` shows as `D` (deleted) and `discernment-same-different.md` as `??` (untracked). `git add domains/` stages both halves so the rename lands as one logical change. Don't `git mv` after the fact — the files are already in their final state.

## Suggested commit message
```
Finish origin-layer floor (307/314) + rename Discernment + capacity-spine direction

- A' wiring: 307/314 pre-formal topics floored (title+tags regex + COURSE_DEFAULTS
  + homonym guards + reconcile); anti-collapse + connectivity gates pass
- validate.py: connectivity invariant (every pre-formal topic reaches a capacity)
- rename capacity "Discrimination" -> "Discernment" (slug + node + code labels only)
- private viz: visualize_origin_layer.py + visualize_radial.py --with-origins
- capacity-spine ideate dialectic -> truth-first synthesis (plans/)

dialectic-reviewed: capacity-spine ideate 5-2-3 (2026-06-30)
```
(The pre-push hook requires a `dialectic-reviewed:`/`dialectic-skipped:` trailer on commits ≥5 non-md files or ≥200 non-md LoC — this commit qualifies.)

## Pre-commit checklist
- [ ] Render + eyeball `output/origin-layer-map.html` and `output/radial-with-origins.html` (browser was offline at build → structural-only verification). The "nodes should appear slightly differently" tweak is still unspecified.
- [x] **DONE Jun 30:** sibling-node prose changed "discrimination" → "discernment" in `classification-sorting.md`, `grade-seriation.md`, `naming-symbol-reference.md`; added an `## On the Name` section to the Discernment node explaining it's standardly called "discrimination" in perceptual psychology but we use "discernment" to avoid the loaded social connotation. (These 4 files are already covered by `git add domains/` above.) `validate.py --quick` PASS.
