---
id: query-optimization
title: Query Optimization
domain: computer-science
course: databases
prerequisites:
- id: query-execution-plans
  type: hard
- id: relational-algebra
  type: soft
- id: btree-indexes
  type: soft
tags:
- query optimization
- cost-based optimization
- rule-based optimization
- join ordering
- statistics
stage: formal-systems
status: draft
---

# Query Optimization

## Core Idea
Query optimization is the process of automatically selecting the most efficient execution plan for a SQL query. Rule-based optimization applies algebraic equivalences (push selections early, project away unused columns) to reduce intermediate result sizes. Cost-based optimization estimates the I/O and CPU cost of candidate plans using table statistics (histograms, row counts, distinct value counts) and selects the minimum-cost plan. Join order selection is especially important — there are n!/2 distinct join orders for n tables, so optimizers use dynamic programming or greedy heuristics to search this space efficiently.

## How It's Best Learned
Experiment with manual query rewrites and compare EXPLAIN outputs: move filters earlier, avoid function calls on indexed columns, rewrite NOT IN as NOT EXISTS. Run ANALYZE to refresh statistics and see how plans change.

## Common Misconceptions
- The optimizer does not always find the globally optimal plan — it uses approximations to avoid exponential search time.
- SQL hints that force a specific plan are a last resort, not a routine practice.
- Outdated statistics (after large bulk loads) are a leading cause of bad plan selection — running ANALYZE fixes this.
