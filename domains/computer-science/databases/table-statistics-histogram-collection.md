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
