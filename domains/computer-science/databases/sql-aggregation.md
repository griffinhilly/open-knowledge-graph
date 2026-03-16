---
id: sql-aggregation
title: SQL Aggregation and GROUP BY
domain: computer-science
course: databases
prerequisites:
- id: sql-select-basics
  type: hard
builds-toward:
- sql-subqueries
- query-execution-plans
tags:
- SQL
- GROUP BY
- HAVING
- COUNT
- SUM
- AVG
- aggregate functions
stage: formal-systems
status: validated
---

# SQL Aggregation and GROUP BY

## Core Idea
Aggregate functions (COUNT, SUM, AVG, MIN, MAX) compute summary statistics over groups of rows rather than returning individual rows. GROUP BY partitions the result set into groups by one or more columns before applying aggregation, so SUM(amount) GROUP BY region yields a total per region rather than a grand total. HAVING filters groups after aggregation, analogous to how WHERE filters individual rows before aggregation; HAVING is necessary for conditions referencing aggregate results like HAVING COUNT(*) > 10.

## How It's Best Learned
Build up from COUNT(*) over all rows, then group by a categorical column, then add HAVING. Practice distinguishing whether a filter belongs in WHERE (before grouping) vs. HAVING (after grouping) by asking: 'does this condition apply to individual rows or to the group?'

## Common Misconceptions
- Every column in SELECT must either appear in GROUP BY or be wrapped in an aggregate function — omitting this causes an error or undefined behavior.
- COUNT(*) counts all rows including NULLs; COUNT(column) skips NULL values in that column.
- HAVING and WHERE are often confused: WHERE filters before grouping, HAVING filters the resulting groups.

## Explainer

You already know how SELECT retrieves individual rows from a table — filtering with WHERE, choosing columns, ordering results. Aggregation changes the question from "show me the rows" to "summarize the rows." **Aggregate functions** like COUNT, SUM, AVG, MIN, and MAX collapse many rows into a single summary value. Writing `SELECT COUNT(*) FROM orders` gives you one number: the total row count. Writing `SELECT AVG(price) FROM products` gives you one number: the average price across all products. The database reads every qualifying row but returns a single summary instead of the rows themselves.

The real power arrives with **GROUP BY**, which partitions rows into buckets before aggregating. Think of it like sorting a deck of cards by suit and then counting each pile separately. `SELECT region, SUM(amount) FROM sales GROUP BY region` first groups all rows sharing the same region value, then computes SUM(amount) independently within each group. The result has one row per group, not one row per original record. A critical rule follows from this: every column in your SELECT must either appear in the GROUP BY clause or be wrapped in an aggregate function. If you select `region` and `SUM(amount)`, you must group by `region` — otherwise the database cannot know which single region value to display alongside the sum.

The distinction between **WHERE** and **HAVING** is the most commonly confused aspect of aggregation, and it comes down to timing. WHERE filters individual rows *before* grouping happens — it decides which rows enter the groups in the first place. HAVING filters *after* grouping — it decides which completed groups appear in the final result. If you want only orders from 2024 to be included in your sums, that is a WHERE condition: `WHERE order_date >= '2024-01-01'`. If you want to see only regions whose total exceeds $10,000, that is a HAVING condition: `HAVING SUM(amount) > 10000`. The test is simple — ask whether the condition references an aggregate result. If yes, it belongs in HAVING; if it references raw column values, it belongs in WHERE.

One subtlety worth noting: `COUNT(*)` counts all rows in a group, including those with NULL values in any column. `COUNT(column_name)` counts only rows where that specific column is not NULL. This distinction matters when your data has missing values — counting customers versus counting customers who have a phone number on file can yield very different results. Understanding this behavior, combined with the WHERE/HAVING timing distinction, gives you precise control over how groups are formed and filtered.
