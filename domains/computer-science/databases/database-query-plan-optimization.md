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
stage: advanced
status: validated
---

# Query Plan Optimization: Choosing Execution Strategies

## Core Idea
Query optimizers choose among multiple execution plans based on cost estimates (I/O, CPU, memory). The optimizer uses table statistics and heuristics to minimize estimated cost.

## How It's Best Learned
Use EXPLAIN ANALYZE to view actual plans, modify indexes, and re-run EXPLAIN to see how costs and row counts change.

## Common Misconceptions
The optimizer's choice is based on estimated costs, which can be inaccurate if statistics are stale. Cost-based optimization is not guaranteed to find the global optimum.

## Questions

```yaml
- question: "A query filters a 10-million-row table on the `email` column (highly unique — 99.99% selectivity) but runs slowly. You check with EXPLAIN and find the optimizer chose a sequential scan despite an index on `email`. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "Sequential scans are always faster than index scans for large tables due to I/O prefetching"
    - "The table statistics are stale — the optimizer's estimate of selectivity is outdated and suggests the filter matches many rows, making a sequential scan appear cheaper"
    - "Index scans cannot be used with equality predicates; they require range conditions"
    - "The database lacks sufficient buffer pool memory to hold the index in RAM"
  answer: 1
  explanation: "The optimizer chooses plans based on estimated costs, not actual data. If statistics haven't been updated since a column became highly selective (e.g., after adding many unique emails), the optimizer may estimate that the filter matches 50% of rows — in which case a sequential scan is genuinely cheaper. With accurate statistics showing 0.01% selectivity, the optimizer would correctly choose the index scan. This is the canonical case where running ANALYZE (or equivalent) resolves poor performance without touching indexes, schema, or SQL."

- question: "A query joins a 50-row 'countries' table with a 5-million-row 'orders' table, filtered to orders in a specific month (matching ~10,000 rows). Which execution strategy should the optimizer prefer?"
  type: multiple-choice
  options:
    - "Scan the full 'orders' table first, then join with 'countries', because the larger table must be read into memory before joining"
    - "Apply the month filter to 'orders' first (reducing it to ~10,000 rows), then join the filtered result with 'countries', minimizing intermediate result size"
    - "Join 'countries' and 'orders' before filtering, because joins are cheaper when no filter conditions exist"
    - "The join order has no effect on performance; only the join algorithm (hash vs. nested loop) matters"
  answer: 1
  explanation: "A core optimizer strategy is pushing filter predicates down before joins to reduce intermediate result sizes as early as possible. Filtering 'orders' first produces ~10,000 rows; joining that against 50 'countries' rows is trivial. Joining unfiltered 'orders' (5 million rows) to 'countries' first produces 5 million output rows before any filtering — dramatically more work. This is why the optimizer's logical transformation step (predicate pushdown) precedes physical plan costing."

- question: "Running ANALYZE (or the equivalent statistics refresh command) on a table after a large bulk insert can improve query performance without modifying any SQL, indexes, or table schema."
  type: true-false
  answer: true
  explanation: "The optimizer's decisions are only as good as its statistics. After a bulk insert significantly changes the data distribution, the stored statistics (row counts, value histograms, selectivity estimates) no longer reflect reality. The optimizer may choose plans that were optimal for the old data but are poor for the new state. ANALYZE recomputes statistics from the current data, giving the optimizer accurate inputs — and better plan choices follow automatically, with no code or schema changes required."

- question: "Because modern query optimizers evaluate all possible execution plans for a given query, they always find the globally optimal plan."
  type: true-false
  answer: false
  explanation: "For queries joining many tables, the plan space is combinatorially explosive — there are roughly n! orderings for n tables, each with multiple join algorithm choices. Optimizers use dynamic programming for small numbers of joins (up to ~10–12 tables), but switch to heuristics and greedy algorithms for larger queries, which do not guarantee global optimality. Furthermore, even for small queries, cost estimates are based on statistics that may be approximate or stale, so the 'cheapest estimated plan' is not always the cheapest actual plan. Cost-based optimization finds the best plan given available information, not the provably optimal plan."

- question: "Why might a query optimizer choose a different execution plan for the same SQL query in January versus June, even though no indexes, schema, or application code have changed?"
  type: short-answer
  answer: "The optimizer uses table statistics — row counts, value distributions, histograms — to estimate plan costs. If statistics are periodically refreshed (e.g., automatically by the database or by scheduled ANALYZE runs), and the data has changed between January and June (different row counts, different value distributions due to seasonal data), the optimizer receives different inputs and may produce a different plan. For example, a table with 100,000 rows in January might have 10 million rows in June; an index scan that was optimal for the small table may be worse than a sequential scan for the large one. The plan is a function of the statistics, not just the SQL."
  explanation: "This illustrates why query performance monitoring is ongoing, not one-time. Data distributions drift, statistics age, and plan choices shift. EXPLAIN ANALYZE is the diagnostic tool: it shows both estimated costs (what the optimizer believed) and actual costs (what happened), making stale statistics visible as a large gap between the two."
```

## Explainer

When you write a SQL query, you specify *what* data you want — not *how* to retrieve it. The **query optimizer** is the component that decides the how. For even a moderately complex query joining three or four tables, there may be dozens or hundreds of possible execution strategies: which table to scan first, whether to use an index or a full table scan, which join algorithm to use (nested loop, hash join, merge join), and in what order to join the tables. The optimizer's job is to evaluate these alternatives and choose the plan with the lowest estimated cost.

**Cost-based optimization** works by assigning a numeric cost estimate to each candidate plan, then selecting the cheapest one. These cost estimates combine several factors: the number of **disk I/O operations** (typically the dominant cost), CPU time for comparisons and hashing, and memory usage for intermediate results. To estimate these, the optimizer relies on **table statistics** — metadata about the data, including table sizes (number of rows), the number of distinct values in each column, value distributions (histograms), and index availability. For example, if the optimizer knows a table has 10 million rows but an index on the filtered column has high selectivity (the WHERE clause matches only 0.1% of rows), it will choose an index scan. If the filter matches 80% of rows, a sequential scan is cheaper because it avoids the overhead of random index lookups.

**Join ordering** is where optimization gets combinatorially challenging. For a query joining n tables, there are roughly n! possible orderings, each with multiple join algorithm choices. Optimizers use **dynamic programming** for small numbers of tables (typically up to 10–12), evaluating all orderings and pruning suboptimal partial plans. For larger queries, they switch to heuristics and greedy algorithms that sacrifice optimality for speed. The optimizer also applies **logical transformations** — pushing filter predicates down to reduce intermediate result sizes early, reordering operations based on algebraic equivalences, and eliminating redundant joins — before costing physical plans.

The optimizer's choices are only as good as its statistics. When table data changes significantly (after large inserts, updates, or deletes) but statistics have not been refreshed, the optimizer may choose a plan based on outdated assumptions — selecting a nested loop join when a hash join would be far faster, or using a full table scan when an index scan would suffice. This is why databases provide commands like `ANALYZE` (PostgreSQL) or `UPDATE STATISTICS` (SQL Server) to refresh this metadata. Running `EXPLAIN ANALYZE` on a query shows both the optimizer's estimated costs and the actual execution metrics, making it the primary tool for diagnosing when the optimizer has made a poor choice and understanding why.
