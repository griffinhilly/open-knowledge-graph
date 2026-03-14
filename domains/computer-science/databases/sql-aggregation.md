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
