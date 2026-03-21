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

## Questions

```yaml
- question: "A query optimizer estimates that WHERE age > 30 AND city = 'Denver' will return 3,000 rows (using independence: selectivity 0.6 × 0.05 on a 100,000-row table). The actual result is 200 rows because age and city are correlated. What plan failure is most likely?"
  type: multiple-choice
  options:
    - "The optimizer will generate a syntax error because correlated columns require special syntax"
    - "The optimizer will skip the city filter entirely to reduce computation"
    - "The optimizer will choose a join algorithm and scan strategy suited for 3,000 rows — likely a hash join or full scan — when a nested-loop join on the actual 200-row result would be far faster"
    - "The optimizer will correctly detect the correlation and rewrite the query"
  answer: 2
  explanation: "A 15× overestimate (3,000 vs. 200 rows) causes the optimizer to select algorithms designed for large intermediate results. Hash joins have good throughput for large sets but high setup cost; nested-loop joins are optimal for small result sets. The optimizer, believing 3,000 rows are coming, picks the wrong algorithm. Without multi-column statistics, the optimizer cannot detect the correlation — it only has per-column selectivity estimates and assumes independence. This is a classic example of how a single estimation error cascades into a bad plan."

- question: "A column has 200 distinct values uniformly distributed across a 1,000,000-row table. What selectivity does the optimizer assign to an equality condition on this column?"
  type: multiple-choice
  options:
    - "0.5 — equality conditions match about half the rows on average"
    - "0.005 — selectivity equals 1/NDV (number of distinct values) = 1/200"
    - "1.0 — every row matches some value, so selectivity is 1"
    - "Unknown — selectivity cannot be calculated without a histogram"
  answer: 1
  explanation: "For equality conditions on uniformly distributed columns, selectivity = 1/NDV = 1/200 = 0.005. With 1,000,000 rows, the optimizer estimates 5,000 matching rows. This is the baseline formula. Non-uniform distributions require histograms or most-common-value lists to refine the estimate — if 90% of rows have one value, a uniform assumption drastically underestimates that value's selectivity and overestimates all others."

- question: "When estimating the combined selectivity of multiple filter conditions (e.g., WHERE a = 1 AND b = 2), databases multiply the individual selectivities together. This is always accurate."
  type: true-false
  answer: false
  explanation: "The independence assumption — multiply individual selectivities — is standard practice but is only accurate when the columns are truly uncorrelated. Many real-world columns correlate: age and retirement status, city and state, product category and price range. When columns correlate, the actual combined selectivity may be much higher or lower than the product predicts. Correlated predicates are one of the most common causes of severe cardinality estimation errors and the query plan failures that follow."

- question: "A single large cardinality estimation error at an early stage of a query execution plan can cause dramatically poor performance for the entire query, including join strategy and index selection decisions downstream."
  type: true-false
  answer: true
  explanation: "Cardinality estimates cascade through the plan tree. An overestimate at a filter makes the join above it receive an inflated row count, causing the optimizer to choose a join algorithm appropriate for large inputs (hash join) rather than the optimal one for a small result (nested-loop). Index-vs-full-scan decisions are similarly driven by estimated row counts. A single bad estimate propagates and amplifies — a 100× error at a filter can easily produce a query that runs 1,000× slower than the optimal plan."

- question: "When diagnosing an unexpectedly slow SQL query, why is comparing 'estimated rows' to 'actual rows' in the query execution plan often the fastest path to finding the root cause?"
  type: short-answer
  answer: "Because every plan decision — join algorithm, index vs. scan, join order — is driven by the optimizer's cardinality estimates. A large gap between estimated and actual rows at a specific plan node directly identifies which assumption was wrong and which operation is misconfigured. The location of the gap points to stale statistics, a correlated predicate being treated as independent, or a skewed distribution the optimizer didn't know about."
  explanation: "EXPLAIN ANALYZE (or equivalent) shows estimated vs. actual row counts for every node in the plan tree. A gap of 10× or more at a node is a strong signal that the statistics or selectivity model for that node is broken. Once you identify the broken node, the fix is usually specific: refresh table statistics with ANALYZE, add multi-column statistics for correlated columns, add an index hint, or rewrite the query to give the optimizer better information. Without this diagnostic, you'd be guessing which part of the query is slow."
```

## Explainer

You already know that the query optimizer chooses between different execution plans — sequential scans, index lookups, various join algorithms — to find the fastest way to answer a query. But how does it decide? The answer is **cardinality estimation**: the optimizer's prediction of how many rows will flow through each step of a plan. If it expects a filter to return 10 rows, an index lookup makes sense. If it expects 10 million rows, a full table scan is cheaper. The entire cost model rests on these row-count predictions.

**Selectivity** is the fundamental unit of estimation. It represents the fraction of rows that satisfy a given condition. A filter like `status = 'active'` on a table with 1 million rows might have selectivity 0.4, meaning the optimizer estimates 400,000 rows will pass. For equality conditions on columns with uniform distribution, selectivity is simply 1/NDV (number of distinct values). For range conditions like `age > 30`, selectivity depends on knowing how values are distributed — which is why databases collect statistics like histograms, most-common-value lists, and null fractions.

The real challenge arises when the optimizer must combine selectivity estimates across multiple conditions. For `WHERE age > 30 AND city = 'Denver'`, the standard assumption is **independence**: multiply the individual selectivities together. If age > 30 has selectivity 0.6 and city = 'Denver' has selectivity 0.05, the combined estimate is 0.03 — 3% of rows. This independence assumption is often wrong (age and city may correlate), but without multi-column statistics it is the best the optimizer can do. Correlated predicates are one of the most common sources of severe estimation errors.

Estimation errors compound through the plan. A 3x overestimate at a filter feeds into the join above it, which uses that inflated number to pick a join algorithm — perhaps choosing a hash join when a nested-loop join on a small result set would have been far faster. This cascading effect explains why a single bad selectivity estimate can make a query run 100x slower than optimal. When you encounter a mysteriously slow query, examining the optimizer's cardinality estimates (via EXPLAIN ANALYZE or equivalent) and comparing them to actual row counts is often the fastest path to diagnosis. The gap between estimated and actual rows points directly to the broken assumption.
