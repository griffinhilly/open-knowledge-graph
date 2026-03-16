---
id: execution-plan-query-optimization
title: Query Optimization and Execution Plans
domain: computer-science
course: databases
prerequisites:
- id: index-selection-optimization
  type: soft
- id: sql-inner-join-combining-tables
  type: soft
builds-toward:
- concurrency-isolation-control
tags:
- query optimization
- execution plan
- cost estimation
- performance
stage: formal-systems
status: draft
---

# Query Optimization and Execution Plans

## Core Idea
A query optimizer transforms SQL into an efficient execution plan by estimating costs of alternative plans and choosing the cheapest. The execution plan specifies which indexes to use, join order, and join algorithms. Understanding how to read execution plans and identify bottlenecks is essential for performance tuning.

## How It's Best Learned
Examine EXPLAIN output for various queries, understand sequential scan vs. index scan decisions, analyze join orders and algorithms, and practice rewriting queries to match optimizer hints.

## Explainer

When you write a SQL query, you are describing *what* data you want, not *how* to get it. The **query optimizer** is the component of the database engine responsible for figuring out the how. It takes your declarative SQL statement and produces an **execution plan** — a step-by-step recipe of physical operations (scans, joins, sorts, filters) that retrieves the result. There are often hundreds or thousands of ways to execute a single query, and the optimizer's job is to find one that is fast enough, ideally the fastest.

Consider a simple query joining two tables with a WHERE clause. The optimizer must decide: should it scan the entire first table or use an index? Which table should be the outer loop and which the inner in a nested-loop join? Would a hash join or merge join be faster? Should the filter be applied before or after the join? Each combination of these choices is a different plan, and the optimizer estimates the **cost** of each one using statistics about the data — table sizes, index selectivity, data distribution histograms, and disk I/O estimates. It then picks the plan with the lowest estimated cost. This is why keeping table statistics up to date (via ANALYZE in PostgreSQL, for example) matters so much: stale statistics lead to bad cost estimates and therefore bad plans.

Reading an execution plan is the most practical skill for database performance tuning. Most databases expose plans through an EXPLAIN command. The plan is typically a tree of operations: leaf nodes are table access methods (**sequential scan** reads every row; **index scan** uses a B-tree to jump directly to matching rows), and internal nodes are operations like joins, sorts, and aggregations. Each node shows an estimated cost and row count. The most common performance problem is a sequential scan on a large table where an index scan would be orders of magnitude faster — this usually means either the right index doesn't exist or the optimizer's statistics are outdated. The second most common problem is a bad join order: joining a million-row table with a thousand-row table in the wrong direction can be catastrophic.

The optimizer is not infallible. It works with estimates, not certainties, and sometimes picks a suboptimal plan. When this happens, you have several levers: create or drop indexes to change what plans are available, rewrite the query to guide the optimizer (breaking a complex query into simpler steps, for instance), update statistics, or in some databases use optimizer hints to force a particular strategy. The key mindset is that query tuning is a conversation between you and the optimizer — you provide the structure (indexes, statistics, well-written SQL) and the optimizer does its best with what you give it.
