# Corpus Debt Triage Plan

*Date: 2026-06-19. Read-only analysis — no corpus/tooling files were modified.*
*Provenance: counts below are MODELED from validator source + reconcile_analysis.json + PLAN/MEMORY estimates, NOT observed (the validator was not run live — ~15k files, 2+ min). Run the exact-count command in the last section to replace estimates with observed numbers before citing.*

## Warning Summary Table

| Cat | Type | Est. Count | Correctness Impact | Fix Approach | Effort |
|---|---|---|---|---|---|
| A | `builds-toward X` but X doesn't back-reference this topic | ~9,100–9,331 | **Medium** — informational forward-hint field; does NOT corrupt the graph (prerequisites are authoritative) | Hybrid: **policy decision first**, then optional bulk `reconcile.py --apply` | policy 1h; apply 30min |
| B | Dangling prereq "not found" (ID resolves to no topic file) | ~500–1,100 | **Medium** — real missing edge; learning paths over-count | **Script-ready**: `tools/fix_dangling_prereqs.py` complete (138 FIXES, 120 REMOVES), unapplied | 30 min apply + verify |
| C | Duplicate prereq ID in one file (sometimes hard+soft conflict) | ~90 files (unverified) | **Low** — duplicate edge; no user-facing break unless a tool dedups badly | Scriptable (keep hard on conflict, drop dup); validator doesn't catch this yet | 1h write + apply |
| D | Course staged below median cross-course prereq | ~5–20 | **Low** — affects stage-based opacity/decay UX, not structure | Hybrid: `audit_course_stages.py` surfaces, human checks each | 1–2h |
| E | Question schema (missing fields, wrong count, MC answer OOB) | ~500–2,000 (unknown) | **Cosmetic** — supplementary content, no graph integrity impact | Script easy cases, human for content | 2–4h |

Category A alone is ~75–78% of the total. The validator emits one warning per occurrence, not per unique ID.

## Recommended Sequencing

**1. Fix first — Category B (dangling prereqs).** Apply `tools/fix_dangling_prereqs.py` — it was prepared with verified fixes/removes and has *never been run*. Clears ~500–1,100 warnings representing real missing edges. **Pre-condition:** run its `verify_targets()` first — the corpus changed since the script was written, so some FIX targets may no longer exist. Run `validate.py` after to confirm the new count.

**2. Fix second — Category C (duplicate prereq IDs).** Small dedup script: per file, scan prerequisites for repeated IDs; on hard+soft conflict keep hard, drop the dup. **Also patch the validator** to catch this going forward (add an intra-file ID-dedup check near `validate.py` lines 208–221) — this is keystone follow-up (c) from PLAN.md.

**3. Policy decision required — Category A (bidirectional mismatches).** ~9,100 warnings cannot resolve without choosing:
- **Option 1 (recommended):** Declare `builds-toward` a non-authoritative hint NOT required to be bidirectionally consistent. Demote the mismatch check to debug-only. Prerequisite graph stays the single source of truth. **Zero corpus edits.**
- **Option 2:** Systematically remove `builds-toward` entries lacking a back-reference via `reconcile.py --apply` (already built). Clears warnings but strips ~9,100 forward-edge hints the path engine's display uses. Run `reconcile_analyze.py` first for cycle-risk/already-transitive breakdown.
- **Do NOT** add missing prerequisites to resolve these — `reconcile_analysis.json` shows 13 would create cycles and 411 are already transitive (redundant).

**4. Defer — Categories D, E.** Cosmetic / supplementary. Fix on a dedicated quality pass, not before citing the validator.

## What validate.py Does NOT Currently Catch
1. **Intra-file duplicate prereq IDs** (~90 files) — prereq loop (lines 208–221) has no dedup check.
2. **builds-toward self-references** (rare) — cycle check covers prereq cycles only.
3. **Stage inversions** — 2,325 prereq edges have the prereq staged *more advanced* than its successor; a quality signal not surfaced in validation.

## "validate.py clean" Citability
| Claim | Safe? |
|---|---|
| "Zero errors, zero cycles" | YES — structurally accurate |
| "Graph is clean" (unqualified) | NO — 9,000+ bidirectional warnings unresolved |
| "validate.py clean of errors" (qualified) | YES — accurate and precise |

## Get exact observed counts (replaces the modeled estimates)
```bash
cd "C:/Users/griff/Projects/griffin/open-knowledge-graph"
C:/Python314/python.exe tools/validate.py > /tmp/okg_validate.txt 2>&1
grep -c "doesn't list" /tmp/okg_validate.txt   # Category A
grep -c "not found"     /tmp/okg_validate.txt   # Categories A(builds-toward)+B
```

## Key files
- `tools/validate.py` — warning source (A: 359–374, B: 353, D: 382–415, E: 74–174)
- `tools/fix_dangling_prereqs.py` — complete dangling-fix script, **unapplied** (FIXES/REMOVES at 20–285, `verify_targets()` at 296)
- `tools/reconcile.py` / `reconcile_analyze.py` / `reconcile_analysis.json` (stale, 2,573-topic era)
