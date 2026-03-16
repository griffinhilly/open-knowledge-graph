---
id: sql-cost-based-query-optimization-plans
title: Cost-Based Query Optimization and Execution Plan Selection
domain: computer-science
course: databases
prerequisites:
- id: query-optimization
  type: hard
- id: query-cardinality-selectivity-estimation
  type: hard
- id: query-execution-plans
  type: hard
builds-toward:
- query-execution-plan-analysis-explain
tags:
- optimization
- cost-model
- plan-selection
stage: formal-systems
status: draft
---

# Cost-Based Query Optimization and Execution Plan Selection

## Core Idea
Query optimizers estimate CPU and I/O costs for different execution plans using cardinality estimates and cost functions, then select the lowest-cost plan. Cost functions account for sequential scans, index lookups, join algorithms, and sorting. The optimizer explores alternative join orders and strategies, applying heuristics to prune the search space. Modern optimizers use dynamic programming or genetic algorithms for large search spaces.

## Explainer

From your work on query optimization and cardinality estimation, you know that the database doesn't just run your SQL literally — it considers many possible ways to execute it and picks one. Cost-based optimization is the mechanism for that choice. The optimizer assigns a numerical **cost** to each candidate plan, measured in abstract units that approximate the real work the database would have to do, and then selects the plan with the lowest estimated cost.

The cost model typically breaks work into two components: **I/O cost** (reading pages from disk) and **CPU cost** (processing rows in memory). A sequential scan of a 10,000-page table has an I/O cost proportional to 10,000 page reads. An index scan that matches 50 rows might read 50 index pages plus 50 data pages — far cheaper if the table is large, but possibly more expensive if the table fits in a few pages (since random I/O from index lookups can cost more per page than sequential reads). The optimizer uses these cost functions together with **cardinality estimates** — how many rows each operation will produce — to estimate the total cost of a complete plan from scan to final result.

Join ordering is where cost-based optimization gets combinatorially hard. Joining three tables A, B, C can be done as (A⋈B)⋈C, (A⋈C)⋈B, or (B⋈C)⋈A, and each ordering can use different join algorithms — Nested Loop, Hash Join, or Merge Join. For n tables, the number of possible join orders grows factorially, and each can be combined with multiple access methods and join strategies. With 5 tables, the search space is manageable; with 15, it is astronomically large. Optimizers use **dynamic programming** for moderate numbers of tables, building optimal sub-plans bottom-up: first find the best way to access each single table, then the best way to join each pair, then each triple, reusing previously computed sub-plans. For very large joins (10+ tables), some databases switch to **genetic algorithms** or randomized search that samples the space rather than exhaustively exploring it.

The quality of a cost-based optimizer is bounded by the accuracy of its cardinality estimates. If the optimizer thinks a filter will match 100 rows but it actually matches 1,000,000, the cost calculation is wrong and the chosen plan may be terrible — for instance, choosing a Nested Loop join when a Hash Join would be orders of magnitude faster. This is why keeping table statistics current (via ANALYZE in PostgreSQL or equivalent commands) directly affects query performance. The optimizer is only as smart as the data it has about your data.
