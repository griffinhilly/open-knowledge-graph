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
status: validated
---

# Query Optimization and Execution Plans

## Core Idea
A query optimizer transforms SQL into an efficient execution plan by estimating costs of alternative plans and choosing the cheapest. The execution plan specifies which indexes to use, join order, and join algorithms. Understanding how to read execution plans and identify bottlenecks is essential for performance tuning.

## How It's Best Learned
Examine EXPLAIN output for various queries, understand sequential scan vs. index scan decisions, analyze join orders and algorithms, and practice rewriting queries to match optimizer hints.

## Questions

```yaml
- question: "A query that ran in 50ms last month now takes 45 seconds. You run EXPLAIN and see the optimizer chose a sequential scan on a large table. The index still exists. What is the most likely cause?"
  type: multiple-choice
  options:
    - "The index was automatically deleted when the data changed"
    - "The optimizer's statistics are stale, so it underestimated the table size and chose the wrong plan"
    - "Sequential scans are always chosen for safety when queries slow down"
    - "The optimizer tried every possible plan and sequential scan was genuinely the fastest"
  answer: 1
  explanation: "When an optimizer chooses a sequential scan despite an index existing, the most common culprit is stale statistics. If the table has grown dramatically since the last ANALYZE, the optimizer may think the table is small and that a sequential scan is cheaper than an index lookup (for very small tables, this is actually true). Running ANALYZE updates the statistics and typically restores the optimizer's ability to choose correctly. Option D is wrong because the optimizer works with estimates, not certainties — it doesn't try every plan and measure."

- question: "An execution plan shows that a join between a 10-row table (users) and a 10-million-row table (events) uses a nested-loop join with users as the outer relation and events as the inner. Why is this join order important?"
  type: multiple-choice
  options:
    - "Join order only matters for hash joins, not nested-loop joins"
    - "With users as outer, the inner table (events) is probed 10 times; reversing would probe events 10 million times"
    - "The optimizer always puts the smaller table on the left regardless of cost"
    - "Nested-loop joins process both tables simultaneously, so order has no performance impact"
  answer: 1
  explanation: "In a nested-loop join, for every row in the outer relation, the database scans or probes the inner relation. With users (10 rows) as outer, the events table is probed 10 times — manageable if an index exists. If events were the outer relation, users would be probed 10 million times. The difference can be orders of magnitude in performance. This is why join order is one of the most critical decisions the optimizer makes and why bad join order (caused by stale statistics, for instance) is a frequent performance problem."

- question: "A query optimizer sometimes chooses a suboptimal execution plan even when all statistics are up to date."
  type: true-false
  answer: true
  explanation: "The optimizer works with cost estimates, not certainties. Statistics capture distributions (histograms, averages) but cannot perfectly predict every combination of filter values. For multi-table joins with complex predicates, the optimizer must make independence assumptions about correlations that may not hold in real data. The result is that the chosen plan may not be the fastest in practice. This is why query tuning levers (index creation, query rewriting, optimizer hints) exist — they let you guide the optimizer when its estimates are systematically wrong."

- question: "Adding more indexes to a database table always improves query performance."
  type: true-false
  answer: false
  explanation: "Indexes speed up reads but slow down writes. Every INSERT, UPDATE, and DELETE must also update all indexes on the affected table. A table with 20 indexes may have dramatically slower writes than one with 3 targeted indexes. Furthermore, indexes consume disk space and must be maintained by the optimizer during planning (more indexes = more plan candidates to evaluate). The right index strategy targets the specific queries that are performance-critical — indiscriminate indexing creates as many problems as it solves."

- question: "What is the purpose of running EXPLAIN (or EXPLAIN ANALYZE) on a slow query, and what key information should you look for in the output?"
  type: short-answer
  answer: "EXPLAIN shows the optimizer's chosen execution plan: the physical operations (sequential scan, index scan, hash join, etc.), the estimated cost and row count at each step, and the order in which operations are performed. EXPLAIN ANALYZE actually runs the query and shows actual row counts and times alongside the estimates. Key things to look for: large gaps between estimated and actual row counts (stale statistics), sequential scans on large tables where an index scan would be faster, and expensive operations (sorts, hash aggregates) near the root of the plan tree that process large intermediate results."
  explanation: "The execution plan is the optimizer's reasoning made visible. A sequential scan on a million-row table when a suitable index exists typically indicates either that the index doesn't exist, the statistics suggest the table is small, or the filter is not selective enough for an index to help. Estimated vs. actual row-count mismatches pinpoint where the optimizer's model diverges from reality — and those divergences are exactly where plan quality degrades. Reading plans is the most direct path to diagnosing slow queries."
```

## Explainer

When you write a SQL query, you are describing *what* data you want, not *how* to get it. The **query optimizer** is the component of the database engine responsible for figuring out the how. It takes your declarative SQL statement and produces an **execution plan** — a step-by-step recipe of physical operations (scans, joins, sorts, filters) that retrieves the result. There are often hundreds or thousands of ways to execute a single query, and the optimizer's job is to find one that is fast enough, ideally the fastest.

Consider a simple query joining two tables with a WHERE clause. The optimizer must decide: should it scan the entire first table or use an index? Which table should be the outer loop and which the inner in a nested-loop join? Would a hash join or merge join be faster? Should the filter be applied before or after the join? Each combination of these choices is a different plan, and the optimizer estimates the **cost** of each one using statistics about the data — table sizes, index selectivity, data distribution histograms, and disk I/O estimates. It then picks the plan with the lowest estimated cost. This is why keeping table statistics up to date (via ANALYZE in PostgreSQL, for example) matters so much: stale statistics lead to bad cost estimates and therefore bad plans.

Reading an execution plan is the most practical skill for database performance tuning. Most databases expose plans through an EXPLAIN command. The plan is typically a tree of operations: leaf nodes are table access methods (**sequential scan** reads every row; **index scan** uses a B-tree to jump directly to matching rows), and internal nodes are operations like joins, sorts, and aggregations. Each node shows an estimated cost and row count. The most common performance problem is a sequential scan on a large table where an index scan would be orders of magnitude faster — this usually means either the right index doesn't exist or the optimizer's statistics are outdated. The second most common problem is a bad join order: joining a million-row table with a thousand-row table in the wrong direction can be catastrophic.

The optimizer is not infallible. It works with estimates, not certainties, and sometimes picks a suboptimal plan. When this happens, you have several levers: create or drop indexes to change what plans are available, rewrite the query to guide the optimizer (breaking a complex query into simpler steps, for instance), update statistics, or in some databases use optimizer hints to force a particular strategy. The key mindset is that query tuning is a conversation between you and the optimizer — you provide the structure (indexes, statistics, well-written SQL) and the optimizer does its best with what you give it.
