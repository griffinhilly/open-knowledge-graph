---
id: table-statistics-histogram-collection
title: Table Statistics, Histograms, and Column Statistics
domain: computer-science
course: databases
prerequisites:
- id: query-cardinality-selectivity-estimation
  type: hard
builds-toward:
- sql-cost-based-query-optimization-plans
tags:
- statistics
- histogram
- sampling
- column-stats
- MFV
stage: formal-systems
status: draft
---

# Table Statistics, Histograms, and Column Statistics

## Core Idea
Database systems maintain statistics on column distributions: histograms partition values into buckets to represent skewed distributions, most-frequent-value (MFV) lists track high-cardinality values, and sampling estimates statistics without scanning entire tables. The optimizer uses these statistics to estimate selectivity more accurately than uniform distribution assumptions. Regular statistic maintenance is essential as data changes.

## Explainer

From your study of cardinality and selectivity estimation, you know the query optimizer needs to predict how many rows a filter or join will produce in order to choose the best execution plan. But where does the optimizer get those predictions? It cannot scan the entire table for every query — that would defeat the purpose of optimization. Instead, the database pre-computes and stores **table statistics**: compact summaries of column distributions that the optimizer consults during planning.

The simplest statistics are per-column summaries: the number of distinct values, the fraction of NULLs, the minimum and maximum values, and the total row count. These let the optimizer make basic estimates — if a column has 100 distinct values in a 10,000-row table, a filter on a specific value is estimated to return about 100 rows, assuming uniform distribution. But real data is rarely uniform. A `city` column might have 40% of rows in "New York" and 0.1% in "Boise." Assuming uniformity would wildly misestimate both queries.

**Histograms** solve this by partitioning the column's value range into buckets, each recording a count or frequency. An **equi-width histogram** divides the range into equal intervals, while an **equi-depth (equi-height) histogram** adjusts bucket boundaries so each bucket contains roughly the same number of rows — better for skewed data because popular ranges get narrower buckets with more precise estimates. **Most-frequent-value (MFV) lists** complement histograms by tracking the exact frequencies of the top N most common values. Together, the MFV list handles the peaks and the histogram covers the rest of the distribution.

Because collecting exact statistics requires a full table scan, databases typically use **sampling**: reading a random subset of pages or rows and extrapolating. PostgreSQL's `ANALYZE` command, for example, samples a configurable number of rows per column to build histograms and MFV lists. This is fast enough to run regularly but introduces sampling error. The critical operational point is that statistics go stale as data is inserted, updated, and deleted. If your table has grown 10x since the last ANALYZE, the optimizer is planning queries against an outdated picture of the data. Most databases offer auto-analyze features, but high-churn tables may need manual intervention. When a query plan suddenly degrades, stale statistics are one of the first things to check.
