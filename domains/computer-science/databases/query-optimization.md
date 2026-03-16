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

## Explainer

When you write a SQL query, you describe *what* data you want — not *how* to retrieve it. The database's **query optimizer** bridges that gap. From your prerequisite work with query execution plans, you know that a single SQL statement can be executed in many different ways: scanning a full table, using an index, joining tables in different orders, or applying filters at different stages. The optimizer's job is to evaluate these alternatives and pick the one with the lowest estimated cost.

There are two broad optimization strategies. **Rule-based optimization** applies algebraic transformations that are almost always beneficial. For example, pushing a WHERE filter down so it runs before a join reduces the number of rows flowing into the join — a technique called **predicate pushdown**. Similarly, projecting away columns you don't need means less data to shuffle between operations. These rules come from the relational algebra equivalences you've studied: since the algebra defines when two expressions produce the same result, the optimizer can freely substitute one form for another. Rule-based rewrites are cheap to apply and form the first pass of most optimizers.

**Cost-based optimization** goes further by estimating the actual resource cost of candidate plans. The optimizer maintains **table statistics** — row counts, histograms of column value distributions, and distinct value counts — and uses these to estimate how many rows each operation will produce. For instance, if a table has 10 million rows and a histogram shows that 2% match the filter `status = 'active'`, the optimizer estimates 200,000 rows after filtering and can decide whether an index scan or a sequential scan is cheaper. This is where your knowledge of B-tree and hash indexes matters: the optimizer chooses an index scan only when selectivity is high enough that reading index pages plus random table lookups costs less than a single sequential pass.

The hardest sub-problem is **join ordering**. If your query joins five tables, there are 5!/2 = 60 possible orderings, each producing different intermediate result sizes. For ten tables, the number explodes to over 1.8 million. Optimizers use **dynamic programming** to find optimal orderings for small join counts and fall back to greedy heuristics for larger queries. The key insight is that the cheapest overall plan usually minimizes intermediate result sizes — joining the most selective tables first keeps the data flowing through subsequent joins as small as possible. When the optimizer chooses poorly (often due to stale statistics after a bulk load), running ANALYZE to refresh statistics is usually the first and most effective fix.
