---
id: query-cardinality-selectivity-estimation
title: Query Cardinality and Selectivity Estimation
domain: computer-science
course: databases
prerequisites:
- id: query-optimization
  type: hard
- id: sql-filtering-conditions
  type: hard
builds-toward:
- sql-cost-based-query-optimization
- table-statistics-histogram
tags:
- cardinality
- selectivity
- estimation
- cost-model
stage: formal-systems
status: draft
---

# Query Cardinality and Selectivity Estimation

## Core Idea
Cardinality estimation predicts how many rows result from query operations to guide optimizer decisions. Selectivity is the fraction of rows passing a condition (e.g., age > 18 might have selectivity 0.3). The optimizer combines estimates from individual operations and uses data distribution statistics. Accurate estimates are critical for good plan selection; errors of 2-3x are common but errors of 100x+ cause terrible plans.

## Explainer

You already know that the query optimizer chooses between different execution plans — sequential scans, index lookups, various join algorithms — to find the fastest way to answer a query. But how does it decide? The answer is **cardinality estimation**: the optimizer's prediction of how many rows will flow through each step of a plan. If it expects a filter to return 10 rows, an index lookup makes sense. If it expects 10 million rows, a full table scan is cheaper. The entire cost model rests on these row-count predictions.

**Selectivity** is the fundamental unit of estimation. It represents the fraction of rows that satisfy a given condition. A filter like `status = 'active'` on a table with 1 million rows might have selectivity 0.4, meaning the optimizer estimates 400,000 rows will pass. For equality conditions on columns with uniform distribution, selectivity is simply 1/NDV (number of distinct values). For range conditions like `age > 30`, selectivity depends on knowing how values are distributed — which is why databases collect statistics like histograms, most-common-value lists, and null fractions.

The real challenge arises when the optimizer must combine selectivity estimates across multiple conditions. For `WHERE age > 30 AND city = 'Denver'`, the standard assumption is **independence**: multiply the individual selectivities together. If age > 30 has selectivity 0.6 and city = 'Denver' has selectivity 0.05, the combined estimate is 0.03 — 3% of rows. This independence assumption is often wrong (age and city may correlate), but without multi-column statistics it is the best the optimizer can do. Correlated predicates are one of the most common sources of severe estimation errors.

Estimation errors compound through the plan. A 3x overestimate at a filter feeds into the join above it, which uses that inflated number to pick a join algorithm — perhaps choosing a hash join when a nested-loop join on a small result set would have been far faster. This cascading effect explains why a single bad selectivity estimate can make a query run 100x slower than optimal. When you encounter a mysteriously slow query, examining the optimizer's cardinality estimates (via EXPLAIN ANALYZE or equivalent) and comparing them to actual row counts is often the fastest path to diagnosis. The gap between estimated and actual rows points directly to the broken assumption.
