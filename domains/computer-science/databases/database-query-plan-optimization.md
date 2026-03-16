---
id: database-query-plan-optimization
title: 'Query Plan Optimization: Choosing Execution Strategies'
domain: computer-science
course: databases
prerequisites:
- id: query-execution-plans
  type: hard
- id: optimization-multivariable-basics
  type: soft
tags:
- query-optimization
- performance
- cost-based-optimization
stage: formal-systems
status: draft
---

# Query Plan Optimization: Choosing Execution Strategies

## Core Idea
Query optimizers choose among multiple execution plans based on cost estimates (I/O, CPU, memory). The optimizer uses table statistics and heuristics to minimize estimated cost.

## How It's Best Learned
Use EXPLAIN ANALYZE to view actual plans, modify indexes, and re-run EXPLAIN to see how costs and row counts change.

## Common Misconceptions
The optimizer's choice is based on estimated costs, which can be inaccurate if statistics are stale. Cost-based optimization is not guaranteed to find the global optimum.

## Explainer

When you write a SQL query, you specify *what* data you want — not *how* to retrieve it. The **query optimizer** is the component that decides the how. For even a moderately complex query joining three or four tables, there may be dozens or hundreds of possible execution strategies: which table to scan first, whether to use an index or a full table scan, which join algorithm to use (nested loop, hash join, merge join), and in what order to join the tables. The optimizer's job is to evaluate these alternatives and choose the plan with the lowest estimated cost.

**Cost-based optimization** works by assigning a numeric cost estimate to each candidate plan, then selecting the cheapest one. These cost estimates combine several factors: the number of **disk I/O operations** (typically the dominant cost), CPU time for comparisons and hashing, and memory usage for intermediate results. To estimate these, the optimizer relies on **table statistics** — metadata about the data, including table sizes (number of rows), the number of distinct values in each column, value distributions (histograms), and index availability. For example, if the optimizer knows a table has 10 million rows but an index on the filtered column has high selectivity (the WHERE clause matches only 0.1% of rows), it will choose an index scan. If the filter matches 80% of rows, a sequential scan is cheaper because it avoids the overhead of random index lookups.

**Join ordering** is where optimization gets combinatorially challenging. For a query joining n tables, there are roughly n! possible orderings, each with multiple join algorithm choices. Optimizers use **dynamic programming** for small numbers of tables (typically up to 10–12), evaluating all orderings and pruning suboptimal partial plans. For larger queries, they switch to heuristics and greedy algorithms that sacrifice optimality for speed. The optimizer also applies **logical transformations** — pushing filter predicates down to reduce intermediate result sizes early, reordering operations based on algebraic equivalences, and eliminating redundant joins — before costing physical plans.

The optimizer's choices are only as good as its statistics. When table data changes significantly (after large inserts, updates, or deletes) but statistics have not been refreshed, the optimizer may choose a plan based on outdated assumptions — selecting a nested loop join when a hash join would be far faster, or using a full table scan when an index scan would suffice. This is why databases provide commands like `ANALYZE` (PostgreSQL) or `UPDATE STATISTICS` (SQL Server) to refresh this metadata. Running `EXPLAIN ANALYZE` on a query shows both the optimizer's estimated costs and the actual execution metrics, making it the primary tool for diagnosing when the optimizer has made a poor choice and understanding why.
