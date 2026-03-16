---
id: sql-distinct-eliminating-duplicates
title: 'DISTINCT: Eliminating Duplicate Rows'
domain: computer-science
course: databases
prerequisites:
- id: sql-select-basics
  type: hard
builds-toward:
- sql-group-aggregate-functions
tags:
- sql
- queries
- result-filtering
stage: formal-systems
status: draft
---

# DISTINCT: Eliminating Duplicate Rows

## Core Idea
The DISTINCT keyword removes duplicate rows from query results, keeping only unique combinations of the selected columns. It is useful for exploratory analysis to understand the range of values in a dataset.

## How It's Best Learned
Start with simple single-column DISTINCT queries, then apply it to multi-column selects to understand how uniqueness is determined.

## Common Misconceptions
DISTINCT does not affect the underlying data—it only filters the result set. Using DISTINCT with ORDER BY requires the ordering columns to be in the SELECT list (in some databases).

## Explainer

When you run a SELECT query, the result set can contain duplicate rows — especially after joins or when selecting a subset of columns. If you select just the `city` column from a million-row customer table, you might get the same city name thousands of times. **DISTINCT** tells the database to collapse these duplicates, returning only one row for each unique combination of values in your selected columns.

The key insight is that DISTINCT operates on the **entire row** of your result set, not on a single column. If you write `SELECT DISTINCT city, state FROM customers`, a row is considered a duplicate only if both the city and state match. Portland, Oregon and Portland, Maine are distinct rows even though the city name is the same. This means adding more columns to a DISTINCT query generally produces more rows, not fewer, because there are more ways for combinations to be unique.

DISTINCT is most valuable during **exploratory analysis** — when you want to understand what values exist in a column before writing more complex queries. "What departments do we have?" (`SELECT DISTINCT department FROM employees`) or "Which product-category combinations exist?" are natural DISTINCT questions. It is also useful for quick sanity checks: if `SELECT COUNT(*)` returns 10,000 rows but `SELECT COUNT(DISTINCT customer_id)` returns only 8,500, you know some customers appear multiple times.

A common antipattern is using DISTINCT as a band-aid to hide a query bug. If a JOIN produces unexpected duplicates, slapping DISTINCT on the SELECT hides the symptom without fixing the cause — usually a missing join condition or an unintended many-to-many relationship. When you find yourself reaching for DISTINCT to "fix" duplicate rows, pause and ask whether the duplicates indicate a problem in your query logic rather than a legitimate need for deduplication. Also be aware that DISTINCT has a performance cost: the database must sort or hash the entire result set to identify duplicates, which can be expensive on large datasets.
