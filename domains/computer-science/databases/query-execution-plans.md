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
- id: sql-aggregation
  type: soft
- id: sql-joins
  type: soft
- id: sql-subqueries
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
status: validated
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

## Explainer

When you write a SQL query, you describe *what* data you want — but not *how* the database should retrieve it. The **query execution plan** is the database's answer to that "how" question. Think of it like a GPS route: you specify the destination, and the planner picks a route based on current conditions. The planner considers table sizes, available indexes, column statistics, and join methods to produce a tree of physical operations that it estimates will be cheapest to execute. You already know from your work with SELECT, joins, and aggregation what these queries ask for; execution plans reveal the machinery underneath.

The plan is structured as a **tree of operators**. At the leaves are data-access methods: a **sequential scan** reads every row in a table (like flipping through an entire phone book), while an **index scan** uses an index to jump directly to matching rows (like using the alphabetical tabs). Above the leaves sit join operators — **nested loop join** iterates through one table and probes the other for each row, **hash join** builds a hash table from one side and probes it with the other, and **merge join** walks two pre-sorted inputs in tandem. Sort, aggregate, and filter operators appear higher in the tree. Each node passes rows upward to its parent until the root produces the final result.

The key tool for reading plans is **EXPLAIN**, which shows the estimated plan without running the query, and **EXPLAIN ANALYZE**, which actually executes the query and reports real row counts and timings alongside the estimates. The most important numbers to compare are the estimated versus actual row counts at each node. When these diverge dramatically — say the planner expected 10 rows but got 100,000 — it means the planner chose its strategy based on bad information, and you have found your bottleneck. This commonly happens when table statistics are stale (fix with ANALYZE) or when the planner cannot estimate selectivity for complex expressions.

Reading plans is a diagnostic skill, not a memorization exercise. Start at the most expensive node — the one consuming the most time or processing the most rows — and ask: could an index eliminate this sequential scan? Could rewriting the query avoid this sort? Could updated statistics fix this cardinality misestimate? Remember that a sequential scan on a small table is perfectly fine; the goal is not to eliminate all sequential scans but to ensure the planner is making informed choices. Over time, reading execution plans becomes the primary way you bridge the gap between writing correct SQL and writing *fast* SQL.
