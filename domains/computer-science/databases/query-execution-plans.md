---
id: query-execution-plans
title: Query Execution Plans
domain: computer-science
course: databases
prerequisites:
- id: sql-select-basics
  type: hard
- id: relational-algebra
  type: soft
- id: indexing-concepts
  type: soft
builds-toward:
- query-optimization
tags:
- query plan
- EXPLAIN
- execution plan
- operator tree
- join algorithms
- seq scan
stage: formal-systems
status: draft
---

# Query Execution Plans

## Core Idea
A query execution plan is the step-by-step strategy a database engine uses to retrieve data, represented as a tree of physical operators such as sequential scan, index scan, hash join, nested loop join, merge join, and sort. The query planner generates this plan using statistics about table sizes, column cardinalities, and available indexes, choosing the estimated lowest-cost option. Reading execution plans via EXPLAIN (estimated) and EXPLAIN ANALYZE (actual) reveals bottlenecks such as missing indexes, bad cardinality estimates, or expensive sorts.

## How It's Best Learned
Run EXPLAIN ANALYZE on real queries and learn to read the operator tree top-down. Identify the most expensive node and hypothesize whether an index, a rewrite, or updated statistics could eliminate it.

## Common Misconceptions
- EXPLAIN without ANALYZE shows only the estimated plan; actual row counts and times may differ substantially.
- A sequential scan is not always bad — for small tables or queries returning most rows, it outperforms an index scan.
- The database cannot always use an index even if one exists; function wrappers on indexed columns (e.g., LOWER(name) = 'foo') disable index use.
