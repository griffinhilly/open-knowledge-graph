---
id: query-optimization
title: Query Optimization
domain: computer-science
course: databases
prerequisites:
- id: relational-algebra
  type: soft
- id: btree-indexes
  type: soft
- id: hash-indexes
  type: soft
- id: sql-joins
  type: soft
- id: sql-views
  type: soft
tags:
- query optimization
- cost-based optimization
- rule-based optimization
- join ordering
- statistics
stage: formal-systems
status: validated
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

## Questions

```yaml
- question: "After a bulk load of 50 million new rows into a table, queries that previously ran in 2 seconds now take 8 minutes. No schema or index changes were made. What is the most likely cause and the correct first step to fix it?"
  type: multiple-choice
  options:
    - "The indexes have become corrupted and must be dropped and rebuilt from scratch"
    - "The table statistics are stale — the optimizer is estimating row counts based on old data and choosing a bad plan; run ANALYZE to refresh them"
    - "The query must be manually rewritten with SQL hints to force the original execution plan"
    - "The database server ran out of memory and needs to be restarted"
  answer: 1
  explanation: "Stale statistics are the leading cause of sudden plan degradation after bulk loads. The optimizer chose the original plan based on estimated row counts, histograms, and selectivity — all of which are now wildly inaccurate after 50M new rows. Running ANALYZE refreshes these statistics, allowing the optimizer to reassess and typically choose a much better plan. SQL hints (Option C) are a last resort, not a first response — and bypassing the optimizer rather than fixing the underlying statistics problem tends to create maintenance nightmares. Dropping indexes (Option A) would make things worse, not better."

- question: "Why is join ordering considered the hardest sub-problem in query optimization for a query joining many tables?"
  type: multiple-choice
  options:
    - "Joins can only be performed in the order the tables appear in the FROM clause"
    - "The number of possible join orderings grows factorially — for n tables, there are n!/2 orderings — making exhaustive search impractical for large n"
    - "Joins always produce more output rows than input rows, so order doesn't matter for cost"
    - "The database must read all tables into memory before it can join any of them"
  answer: 1
  explanation: "For 5 tables: 5!/2 = 60 orderings. For 10 tables: 10!/2 = 1,814,400. The search space explodes factorially, making it computationally infeasible to evaluate every possible plan. Optimizers use dynamic programming (for small n) and greedy heuristics (for large n) to search this space efficiently. The insight that drives the optimization is that cheapest plans generally minimize intermediate result sizes — joining the most selective tables first keeps the data flowing through later joins as small as possible."

- question: "A cost-based query optimizer typically finds the globally optimal execution plan for a given query."
  type: true-false
  answer: false
  explanation: "Query optimizers use approximations — dynamic programming for manageable join counts, greedy heuristics for larger ones, and statistical estimates that can be imprecise (especially for multi-column correlations). The optimizer finds the best plan it can evaluate within practical time constraints, not a guaranteed global optimum. This is explicitly acknowledged in the misconceptions section: the optimizer sacrifices optimality for tractability. In practice, the plan is usually good, but edge cases (correlated columns, unusual data distributions, very large join counts) can produce poor plans even with accurate statistics."

- question: "Predicate pushdown — applying WHERE filters before joins rather than after — is beneficial because it reduces the number of rows flowing into join operations."
  type: true-false
  answer: true
  explanation: "This is one of the few rule-based optimizations that is almost always beneficial. If a table has 10 million rows but a filter reduces it to 50,000 matching rows, performing the filter first means the subsequent join operates on 50,000 rows rather than 10 million. Intermediate result sizes drive I/O and memory costs — the join algorithm (nested loop, hash join, merge join) all scale with input size. Predicate pushdown is derived from relational algebra equivalences: since filtering and joining are algebraically equivalent in either order when the filter only references one table, the optimizer freely chooses the cheaper order."

- question: "Why does the query optimizer need table statistics like row counts, histograms, and distinct value counts, and what happens to query performance when those statistics become stale?"
  type: short-answer
  answer: "The optimizer uses statistics to estimate how many rows each operation will produce — its 'cardinality estimates.' These estimates drive every cost calculation: whether an index scan beats a sequential scan depends on estimated selectivity; which join order is cheapest depends on estimated intermediate result sizes. When statistics are stale (after bulk inserts, large deletes, or significant updates), the optimizer's estimates diverge from reality. It may choose a nested-loop join expecting 100 matching rows when the table actually has 10 million, or bypass an index expecting low selectivity when the actual filter is highly selective. The result is plans that can be orders of magnitude slower than optimal."
  explanation: "Running ANALYZE (or its equivalent) refreshes the statistics the optimizer relies on. This is why ANALYZE is the first fix to try after bulk data changes — it costs relatively little and can dramatically improve plan quality by giving the optimizer accurate information to reason with."
```

## Explainer

When you write a SQL query, you describe *what* data you want — not *how* to retrieve it. The database's **query optimizer** bridges that gap. From your prerequisite work with query execution plans, you know that a single SQL statement can be executed in many different ways: scanning a full table, using an index, joining tables in different orders, or applying filters at different stages. The optimizer's job is to evaluate these alternatives and pick the one with the lowest estimated cost.

There are two broad optimization strategies. **Rule-based optimization** applies algebraic transformations that are almost always beneficial. For example, pushing a WHERE filter down so it runs before a join reduces the number of rows flowing into the join — a technique called **predicate pushdown**. Similarly, projecting away columns you don't need means less data to shuffle between operations. These rules come from the relational algebra equivalences you've studied: since the algebra defines when two expressions produce the same result, the optimizer can freely substitute one form for another. Rule-based rewrites are cheap to apply and form the first pass of most optimizers.

**Cost-based optimization** goes further by estimating the actual resource cost of candidate plans. The optimizer maintains **table statistics** — row counts, histograms of column value distributions, and distinct value counts — and uses these to estimate how many rows each operation will produce. For instance, if a table has 10 million rows and a histogram shows that 2% match the filter `status = 'active'`, the optimizer estimates 200,000 rows after filtering and can decide whether an index scan or a sequential scan is cheaper. This is where your knowledge of B-tree and hash indexes matters: the optimizer chooses an index scan only when selectivity is high enough that reading index pages plus random table lookups costs less than a single sequential pass.

The hardest sub-problem is **join ordering**. If your query joins five tables, there are 5!/2 = 60 possible orderings, each producing different intermediate result sizes. For ten tables, the number explodes to over 1.8 million. Optimizers use **dynamic programming** to find optimal orderings for small join counts and fall back to greedy heuristics for larger queries. The key insight is that the cheapest overall plan usually minimizes intermediate result sizes — joining the most selective tables first keeps the data flowing through subsequent joins as small as possible. When the optimizer chooses poorly (often due to stale statistics after a bulk load), running ANALYZE to refresh statistics is usually the first and most effective fix.
