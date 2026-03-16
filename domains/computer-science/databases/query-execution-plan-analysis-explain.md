---
id: query-execution-plan-analysis-explain
title: Query Execution Plans and EXPLAIN Analysis
domain: computer-science
course: databases
prerequisites:
- id: query-execution-plans
  type: hard
- id: sql-cost-based-query-optimization-plans
  type: hard
tags:
- EXPLAIN
- execution-plan
- analysis
- optimization
stage: formal-systems
status: draft
---

# Query Execution Plans and EXPLAIN Analysis

## Core Idea
The EXPLAIN statement displays the optimizer's chosen execution plan, showing operations (Seq Scan, Index Scan, Join) with estimated row counts, costs, and timing. Analyzing EXPLAIN output reveals whether the optimizer made good decisions and identifies bottlenecks like full table scans or inefficient joins. Discrepancies between estimated and actual row counts indicate poor statistics. Understanding plan interpretation is essential for query tuning.

## Explainer

You already know that query optimizers consider multiple execution plans and pick the cheapest one based on cost estimates. The EXPLAIN statement lets you see the plan the optimizer actually chose — it is your window into the database engine's decision-making. In PostgreSQL, running `EXPLAIN` before a query prints a tree of operations; adding `EXPLAIN ANALYZE` actually executes the query and reports real timing alongside the estimates, so you can compare what the optimizer predicted with what actually happened.

The output is a **plan tree** read from the inside out. Each node represents an operation — a **Seq Scan** (reading every row in a table), an **Index Scan** (jumping directly to matching rows via an index), a **Nested Loop** or **Hash Join** (combining two tables), or a **Sort** (ordering results). Each node shows an estimated **cost** (in arbitrary units combining I/O and CPU), the **estimated rows** it expects to produce, and the **width** of each row in bytes. When you run EXPLAIN ANALYZE, you also see **actual time** (in milliseconds) and **actual rows**. The gap between estimated and actual rows is the single most diagnostic number in the output.

When estimated rows are close to actual rows, the optimizer is making informed decisions and the plan is likely reasonable. When they diverge sharply — the optimizer expected 10 rows but got 100,000 — the plan is almost certainly wrong. This happens because the optimizer relies on **table statistics** (histograms of column value distributions), and those statistics can go stale after bulk inserts or deletes. Running `ANALYZE` on the table refreshes them. A common pattern: a slow query shows a Nested Loop join where the optimizer expected a tiny inner table, but the actual row count is enormous. Switching to a Hash Join or Merge Join would be far better, and refreshing statistics often causes the optimizer to make that switch on its own.

Reading EXPLAIN output is a skill built through repetition. Start with simple single-table queries: is it doing a Seq Scan when an index exists? That might mean the table is small enough that a sequential scan is genuinely cheaper, or it might mean the WHERE clause doesn't match any index. Then move to joins: check the join algorithm (Nested Loop is fine for small inner tables, Hash Join for larger ones, Merge Join for pre-sorted data) and verify the join order makes sense. Finally, look for **sort operations** that spill to disk — the `Sort Method: external merge` line means the data exceeded work_mem and performance dropped significantly.

The practical workflow is: identify a slow query, run EXPLAIN ANALYZE, find the node with the highest actual time or the biggest estimated-vs-actual row mismatch, then address that node — whether by adding an index, rewriting the query, updating statistics, or increasing work_mem. EXPLAIN does not change anything; it only reveals what the database is doing. That visibility is what transforms query tuning from guesswork into engineering.
