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
status: validated
---

# Cost-Based Query Optimization and Execution Plan Selection

## Core Idea
Query optimizers estimate CPU and I/O costs for different execution plans using cardinality estimates and cost functions, then select the lowest-cost plan. Cost functions account for sequential scans, index lookups, join algorithms, and sorting. The optimizer explores alternative join orders and strategies, applying heuristics to prune the search space. Modern optimizers use dynamic programming or genetic algorithms for large search spaces.

## Questions

```yaml
- question: "A query joining two tables runs slowly. After running ANALYZE (which updates table statistics), the database switches from a Nested Loop join to a Hash Join and performance improves dramatically. What most likely happened?"
  type: multiple-choice
  options:
    - "The filter on the inner table actually matched far more rows than the optimizer estimated, making Hash Join much cheaper at the true cardinality"
    - "ANALYZE discovered a new index that Hash Join requires but Nested Loop does not"
    - "Nested Loop join had a bug in the old query plan that ANALYZE fixed"
    - "Hash Join is always faster than Nested Loop; ANALYZE simply enabled the optimizer to recognize this"
  answer: 0
  explanation: "Stale statistics caused the optimizer to underestimate the number of rows returned by the filter. With low estimated cardinality, Nested Loop join looked cheap (it is efficient for small inner tables). With accurate statistics revealing the true (large) cardinality, the optimizer correctly identifies that Hash Join is far cheaper — it scans both inputs once and uses a hash table, scaling much better for large row counts. This illustrates the core principle: the optimizer is only as smart as its cardinality estimates. ANALYZE refreshes those estimates; it does not create indexes or fix bugs."

- question: "A database must join 10 tables. How does a cost-based optimizer avoid evaluating all possible join orderings?"
  type: multiple-choice
  options:
    - "It randomly samples a subset of orderings and picks the cheapest one found"
    - "It uses dynamic programming: first find the best single-table access plan, then the best two-table join, building up optimal sub-plans and reusing them"
    - "It evaluates all 10! = 3,628,800 orderings and picks the minimum cost"
    - "It always joins tables in the order they appear in the FROM clause"
  answer: 1
  explanation: "Dynamic programming exploits the principle of optimal substructure: if the best 5-table join plan includes a particular 3-table sub-plan, that 3-table sub-plan must also be optimal for those 3 tables alone. The optimizer builds solutions bottom-up — optimal single-table scans, then optimal 2-table joins using those results, then 3-table joins, etc. — reusing previously computed results rather than starting from scratch. This reduces the search from factorial to roughly exponential, making even 15-table queries tractable. For very large numbers of tables (15+), some optimizers switch to genetic algorithms or other heuristic searches."

- question: "If table statistics are stale (outdated), the query optimizer may select an execution plan that is orders of magnitude slower than the optimal plan."
  type: true-false
  answer: true
  explanation: "The optimizer's cost estimates depend entirely on statistics — row counts, value distributions, null fractions, and histograms. If these statistics don't reflect current data (e.g., after a large data load), the optimizer may severely underestimate or overestimate cardinalities. A factor-of-1000 error in cardinality estimation can easily cause the optimizer to choose Nested Loop over Hash Join, or to use an index scan on a nearly full table instead of a sequential scan — either of which can make a query orders of magnitude slower."

- question: "A cost-based optimizer determines the best execution plan by actually running each candidate plan on a sample of data and measuring the real execution time."
  type: true-false
  answer: false
  explanation: "The optimizer uses a cost model — mathematical formulas that estimate I/O page reads and CPU operations for each operation type (scan, index lookup, hash join, etc.) — combined with statistics about the data. It never actually executes plans to compare them; that would be prohibitively expensive (you'd have to run the query multiple times just to optimize it). The tradeoff is that the cost model can be wrong when statistics are stale or when the data distribution is skewed in ways the model doesn't capture."

- question: "Why does the accuracy of cardinality estimation matter so much for query optimization? Give an example of how a bad estimate leads to a bad plan choice."
  type: short-answer
  answer: "Cardinality estimation tells the optimizer how many rows each operation will produce. This number directly determines which join algorithm and access method appear cheapest in the cost model. For example: if a filter on a 10-million-row table is estimated to return 50 rows, the optimizer chooses Nested Loop join (cheap for tiny inner tables: 50 lookups × small cost each). If the filter actually returns 500,000 rows, the Nested Loop must do 500,000 lookups — potentially catastrophically slow — while a Hash Join would have scanned each table once and finished far faster. The cost model was applied correctly; it just had wrong inputs."
  explanation: "The fundamental asymmetry is that the optimizer optimizes based on estimates, but query execution happens against actual data. Any gap between estimated and actual cardinality propagates through the entire plan: wrong cardinality at one join node produces wrong estimates for every subsequent node. This is why keeping statistics current with regular ANALYZE (PostgreSQL) or UPDATE STATISTICS (SQL Server) is a core database maintenance task."
```

## Explainer

From your work on query optimization and cardinality estimation, you know that the database doesn't just run your SQL literally — it considers many possible ways to execute it and picks one. Cost-based optimization is the mechanism for that choice. The optimizer assigns a numerical **cost** to each candidate plan, measured in abstract units that approximate the real work the database would have to do, and then selects the plan with the lowest estimated cost.

The cost model typically breaks work into two components: **I/O cost** (reading pages from disk) and **CPU cost** (processing rows in memory). A sequential scan of a 10,000-page table has an I/O cost proportional to 10,000 page reads. An index scan that matches 50 rows might read 50 index pages plus 50 data pages — far cheaper if the table is large, but possibly more expensive if the table fits in a few pages (since random I/O from index lookups can cost more per page than sequential reads). The optimizer uses these cost functions together with **cardinality estimates** — how many rows each operation will produce — to estimate the total cost of a complete plan from scan to final result.

Join ordering is where cost-based optimization gets combinatorially hard. Joining three tables A, B, C can be done as (A⋈B)⋈C, (A⋈C)⋈B, or (B⋈C)⋈A, and each ordering can use different join algorithms — Nested Loop, Hash Join, or Merge Join. For n tables, the number of possible join orders grows factorially, and each can be combined with multiple access methods and join strategies. With 5 tables, the search space is manageable; with 15, it is astronomically large. Optimizers use **dynamic programming** for moderate numbers of tables, building optimal sub-plans bottom-up: first find the best way to access each single table, then the best way to join each pair, then each triple, reusing previously computed sub-plans. For very large joins (10+ tables), some databases switch to **genetic algorithms** or randomized search that samples the space rather than exhaustively exploring it.

The quality of a cost-based optimizer is bounded by the accuracy of its cardinality estimates. If the optimizer thinks a filter will match 100 rows but it actually matches 1,000,000, the cost calculation is wrong and the chosen plan may be terrible — for instance, choosing a Nested Loop join when a Hash Join would be orders of magnitude faster. This is why keeping table statistics current (via ANALYZE in PostgreSQL or equivalent commands) directly affects query performance. The optimizer is only as smart as the data it has about your data.
