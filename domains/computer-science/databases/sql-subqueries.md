---
id: sql-subqueries
title: SQL Subqueries and CTEs
domain: computer-science
course: databases
prerequisites:
- id: sql-select-basics
  type: hard
- id: sql-joins
  type: soft
- id: sql-aggregation
  type: soft
builds-toward:
- query-execution-plans
tags:
- SQL
- subqueries
- CTE
- WITH
- correlated subquery
- nested queries
stage: formal-systems
status: validated
---

# SQL Subqueries and CTEs

## Core Idea
Subqueries are SELECT statements nested inside another query, used in WHERE, FROM, or SELECT clauses to compute intermediate results. Correlated subqueries reference columns from the outer query and re-execute for each outer row, enabling row-by-row comparisons against aggregated or filtered data. Common Table Expressions (CTEs) using the WITH clause improve readability by naming intermediate results and support recursive queries for hierarchical data. Subqueries and CTEs are often interchangeable with joins, with different performance and readability implications.

## How It's Best Learned
Convert a JOIN-based query to an equivalent subquery and back — this builds intuition for when each form is clearer. Practice correlated subqueries for patterns like 'find all employees earning above their department's average salary.'

## Common Misconceptions
- Correlated subqueries can have O(n) execution cost per outer row if not optimized — the optimizer often converts them to joins automatically.
- A subquery in the FROM clause (derived table) must be aliased.
- NOT IN with a subquery behaves unexpectedly when the subquery returns any NULLs — use NOT EXISTS instead.
