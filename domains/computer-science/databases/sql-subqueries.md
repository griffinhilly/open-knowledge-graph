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

## Explainer

You already know how to SELECT, JOIN, and aggregate data. Subqueries let you compose these operations — embedding one query inside another to build complex results step by step. The simplest form is a **scalar subquery** in a WHERE clause: `SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees)`. The inner query runs first, computes a single value (the average salary), and the outer query uses that value as a filter. This is something you cannot do with a plain WHERE clause alone, because the comparison target itself requires a computation.

Subqueries become more powerful — and more subtle — when placed in the FROM clause or when they are **correlated**. A subquery in the FROM clause acts as a temporary table (called a **derived table**): `SELECT dept, avg_sal FROM (SELECT department AS dept, AVG(salary) AS avg_sal FROM employees GROUP BY department) AS dept_stats WHERE avg_sal > 80000`. The inner query creates a result set, the outer query filters it. A correlated subquery, by contrast, references a column from the outer query and re-executes for each outer row: `SELECT e.name FROM employees e WHERE e.salary > (SELECT AVG(salary) FROM employees WHERE department = e.department)`. This finds employees earning above their own department's average — something that requires the inner query to "know" which department the outer row belongs to.

**Common Table Expressions (CTEs)** offer a cleaner syntax for the same idea. Instead of nesting queries, you name intermediate results with `WITH`: `WITH dept_avg AS (SELECT department, AVG(salary) AS avg_sal FROM employees GROUP BY department) SELECT e.name, d.avg_sal FROM employees e JOIN dept_avg d ON e.department = d.department WHERE e.salary > d.avg_sal`. The logic is identical to the correlated subquery version, but the CTE makes the data flow explicit and readable. CTEs also support **recursion** — a `WITH RECURSIVE` CTE can traverse hierarchical data like organizational charts or category trees by repeatedly joining a result set with itself.

One important practical note: subqueries, CTEs, and joins are often interchangeable, and the query optimizer frequently rewrites one form into another internally. A correlated subquery that looks like it would execute once per row is often transformed into a join by the optimizer. This means you should generally write whichever form is clearest to read and maintain, then check the execution plan only if performance is a concern. The exception is the `NOT IN` versus `NOT EXISTS` distinction — when the subquery can return NULLs, `NOT IN` produces unexpected results due to SQL's three-valued logic, so `NOT EXISTS` is the safer choice.
