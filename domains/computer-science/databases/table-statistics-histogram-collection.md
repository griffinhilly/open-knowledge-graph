---
id: table-statistics-histogram-collection
title: Table Statistics, Histograms, and Column Statistics
domain: computer-science
course: databases
prerequisites:
- id: query-cardinality-selectivity-estimation
  type: hard
builds-toward:
- query-optimization
tags:
- statistics
- histogram
- sampling
- column-stats
- MFV
stage: formal-systems
status: validated
---

# Table Statistics, Histograms, and Column Statistics

## Core Idea
Database systems maintain statistics on column distributions: histograms partition values into buckets to represent skewed distributions, most-frequent-value (MFV) lists track high-cardinality values, and sampling estimates statistics without scanning entire tables. The optimizer uses these statistics to estimate selectivity more accurately than uniform distribution assumptions. Regular statistic maintenance is essential as data changes.

## Questions

```yaml
- question: "A 'city' column in a 1,000,000-row table has 500 distinct values and contains 'New York' for 40% of rows. The optimizer assumes uniform distribution. How will it estimate the row count for WHERE city = 'New York'?"
  type: multiple-choice
  options:
    - "400,000 rows — it recognizes 'New York' as the dominant value"
    - "2,000 rows — dividing total rows by the number of distinct values"
    - "1,000,000 rows — it defaults to full table scan estimates"
    - "0 rows — no statistics are available without an explicit ANALYZE"
  answer: 1
  explanation: "With uniform distribution assumed and 500 distinct values, the optimizer estimates 1/500 × 1,000,000 = 2,000 rows for any specific city. The true count is 400,000 — two orders of magnitude off. This misestimate has real consequences: the optimizer would likely choose an index scan (efficient for 2,000 rows) when a sequential scan would be far faster for 400,000 rows. This is exactly why histograms and MFV lists exist — to capture the actual distribution instead of assuming uniformity."

- question: "For a highly skewed column where a few values account for most rows, an equi-depth histogram provides better selectivity estimates than an equi-width histogram. Why?"
  type: multiple-choice
  options:
    - "Equi-depth uses less memory, leaving room for more precise per-value statistics"
    - "Equi-depth adjusts bucket boundaries so popular ranges get narrower buckets with more precise estimates, concentrating precision where data is dense"
    - "Equi-depth captures the exact frequencies of the most common values, eliminating estimation error for those values"
    - "Equi-depth requires no maintenance after data changes, while equi-width must be rebuilt after every insert"
  answer: 1
  explanation: "Equi-depth (equi-height) histograms place bucket boundaries so each bucket contains roughly the same number of rows. In a skewed distribution, the dense ranges get many narrow buckets — high resolution where it matters most. Equi-width divides the value range into equal intervals, so a skewed distribution packs most rows into a few wide buckets, yielding crude estimates for the popular ranges. Note that MFV (most-frequent-value) lists, not equi-depth histograms, capture exact counts for top values."

- question: "When a query plan suddenly degrades after a large bulk insert, stale statistics are one of the first things worth checking."
  type: true-false
  answer: true
  explanation: "Statistics describe the data distribution at the time they were collected. After a large bulk insert, row counts, value distributions, and selectivities may have changed dramatically. If the optimizer is still consulting pre-insert statistics, it may choose a plan that was optimal for the old data but performs poorly on the new data — for example, using an index that is no longer selective, or choosing a nested-loop join when a hash join would be faster. Running ANALYZE (or equivalent) after bulk operations is a standard DBA practice."

- question: "Collecting exact column statistics in a database requires only a brief metadata lookup — the system tracks distributions automatically without scanning the table."
  type: true-false
  answer: false
  explanation: "Exact statistics require reading and analyzing the actual data values, which means a full table scan. For large tables, this is expensive. That is why databases use sampling — reading a random subset of pages or rows and extrapolating. PostgreSQL's ANALYZE, for example, samples a configurable number of rows per column. Sampling is fast enough to run regularly but introduces sampling error. The tradeoff is speed of collection versus precision of estimates."

- question: "Why do databases use sampling rather than full-table scans to build statistics, and what is the key operational risk of this approach?"
  type: short-answer
  answer: "Sampling reads only a fraction of the table (e.g., a few thousand rows) and extrapolates column distributions from that subset. This makes statistics collection fast enough to run regularly without heavily impacting the system. The key operational risk is that statistics become stale as data changes: inserts, deletes, and updates shift the actual distribution away from what the statistics describe, causing the optimizer to make poor plan choices based on an outdated picture of the data."
  explanation: "The staleness risk is the core operational concern. High-churn tables — those with frequent inserts or deletes — may need frequent ANALYZE runs, and most databases offer auto-analyze features. But in practice, unexpected query regressions after bulk operations or schema migrations often trace back to stale statistics. A DBA's first question when a previously fast query becomes slow is often: 'When were statistics last collected?'"
```

## Explainer

From your study of cardinality and selectivity estimation, you know the query optimizer needs to predict how many rows a filter or join will produce in order to choose the best execution plan. But where does the optimizer get those predictions? It cannot scan the entire table for every query — that would defeat the purpose of optimization. Instead, the database pre-computes and stores **table statistics**: compact summaries of column distributions that the optimizer consults during planning.

The simplest statistics are per-column summaries: the number of distinct values, the fraction of NULLs, the minimum and maximum values, and the total row count. These let the optimizer make basic estimates — if a column has 100 distinct values in a 10,000-row table, a filter on a specific value is estimated to return about 100 rows, assuming uniform distribution. But real data is rarely uniform. A `city` column might have 40% of rows in "New York" and 0.1% in "Boise." Assuming uniformity would wildly misestimate both queries.

**Histograms** solve this by partitioning the column's value range into buckets, each recording a count or frequency. An **equi-width histogram** divides the range into equal intervals, while an **equi-depth (equi-height) histogram** adjusts bucket boundaries so each bucket contains roughly the same number of rows — better for skewed data because popular ranges get narrower buckets with more precise estimates. **Most-frequent-value (MFV) lists** complement histograms by tracking the exact frequencies of the top N most common values. Together, the MFV list handles the peaks and the histogram covers the rest of the distribution.

Because collecting exact statistics requires a full table scan, databases typically use **sampling**: reading a random subset of pages or rows and extrapolating. PostgreSQL's `ANALYZE` command, for example, samples a configurable number of rows per column to build histograms and MFV lists. This is fast enough to run regularly but introduces sampling error. The critical operational point is that statistics go stale as data is inserted, updated, and deleted. If your table has grown 10x since the last ANALYZE, the optimizer is planning queries against an outdated picture of the data. Most databases offer auto-analyze features, but high-churn tables may need manual intervention. When a query plan suddenly degrades, stale statistics are one of the first things to check.
