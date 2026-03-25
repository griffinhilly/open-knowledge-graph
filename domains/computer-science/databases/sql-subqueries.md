---
id: sql-subqueries
title: SQL Subqueries and CTEs
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
- id: sql-joins
  type: soft
- id: sql-aggregation
  type: soft
builds-toward:
- query-optimization
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

## Questions

```yaml
- question: "You run: SELECT * FROM employees WHERE id NOT IN (SELECT manager_id FROM departments). You expect some results, but get zero rows, even though many employees are not managers. What is the most likely cause?"
  type: multiple-choice
  options:
    - "NOT IN cannot be used with subqueries — you must use a JOIN instead"
    - "The departments table has at least one NULL in the manager_id column, causing NOT IN to return no rows"
    - "The subquery returns too many rows, causing a performance timeout that returns no results"
    - "NOT IN requires the subquery to be aliased with AS"
  answer: 1
  explanation: "This is the NULL trap in NOT IN. SQL uses three-valued logic: comparisons with NULL produce UNKNOWN (neither TRUE nor FALSE). When the subquery returns any NULL, the condition `id NOT IN (...)` includes a comparison `id != NULL` which evaluates to UNKNOWN. Since UNKNOWN is not TRUE, the row is excluded — effectively making NOT IN return no results when NULLs are present. The fix is NOT EXISTS: `WHERE NOT EXISTS (SELECT 1 FROM departments WHERE manager_id = e.id)`. NOT EXISTS tests set membership through a correlated subquery, which is NULL-safe."

- question: "What distinguishes a correlated subquery from a non-correlated subquery?"
  type: multiple-choice
  options:
    - "A correlated subquery appears in the FROM clause; a non-correlated subquery appears in the WHERE clause"
    - "A correlated subquery references a column from the outer query and logically re-executes for each outer row; a non-correlated subquery executes once"
    - "A correlated subquery always executes faster because the optimizer caches its result per outer row"
    - "A correlated subquery is only valid inside a CTE; non-correlated subqueries can appear anywhere"
  answer: 1
  explanation: "A correlated subquery contains a reference to a column from the outer query (e.g., `WHERE department = e.department`), making it dependent on the current outer row. Logically, it re-executes for each outer row — O(n) executions. A non-correlated subquery has no outer reference, executes once, and its result is reused. In practice, modern optimizers often rewrite correlated subqueries as joins, so actual performance may be similar — but the logical distinction governs behavior when the optimizer cannot rewrite."

- question: "A subquery used as a derived table in the FROM clause must be given an alias."
  type: true-false
  answer: true
  explanation: "In standard SQL, a subquery in the FROM clause (derived table) must be aliased so the outer query can reference it by name. For example: `SELECT * FROM (SELECT id, salary FROM employees) AS emp_data WHERE salary > 50000`. Without the alias `AS emp_data`, most databases throw a syntax error. The alias gives the temporary result set a name that can be used in the outer query's SELECT, WHERE, and JOIN clauses."

- question: "A correlated subquery always executes once per outer row, making it slower than an equivalent JOIN regardless of the database optimizer used."
  type: true-false
  answer: false
  explanation: "Modern query optimizers frequently detect correlated subqueries and rewrite them internally as joins. The *logical* execution model is once per outer row, but the *physical* execution plan often differs significantly. The SQL standard defines semantics, not execution strategy. That said, you should check execution plans when performance matters — the optimizer may not always rewrite, and a correlated subquery touching a large table without an index can genuinely perform poorly. Write for clarity first, optimize after profiling."

- question: "Why should you use NOT EXISTS rather than NOT IN when your subquery might return NULL values?"
  type: short-answer
  answer: "SQL's three-valued logic means any comparison with NULL produces UNKNOWN. In NOT IN, if the subquery returns any NULL, the expression `value NOT IN (..., NULL)` includes `value != NULL`, which is UNKNOWN — causing the entire condition to be UNKNOWN, treated as FALSE, so the row is filtered out. NOT EXISTS tests whether the correlated subquery returns any matching rows at all (a boolean existence check), which is unaffected by NULLs in the data. NOT EXISTS returns TRUE when no matching rows exist, correctly including the outer row in the result."
  explanation: "The practical impact is significant: a query using NOT IN to exclude employees who aren't managers will silently return zero results if any department has a NULL manager_id — a hard-to-debug failure. NOT EXISTS avoids this entirely. This is one of SQL's most notorious NULL-related gotchas, and understanding it requires knowing that SQL's three-value logic (TRUE/FALSE/UNKNOWN) differs from ordinary Boolean logic. When the subquery result is guaranteed to never contain NULLs (e.g., from a NOT NULL column), NOT IN is safe — but NOT EXISTS is always safe."
```

## Explainer

You already know how to SELECT, JOIN, and aggregate data. Subqueries let you compose these operations — embedding one query inside another to build complex results step by step. The simplest form is a **scalar subquery** in a WHERE clause: `SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees)`. The inner query runs first, computes a single value (the average salary), and the outer query uses that value as a filter. This is something you cannot do with a plain WHERE clause alone, because the comparison target itself requires a computation.

Subqueries become more powerful — and more subtle — when placed in the FROM clause or when they are **correlated**. A subquery in the FROM clause acts as a temporary table (called a **derived table**): `SELECT dept, avg_sal FROM (SELECT department AS dept, AVG(salary) AS avg_sal FROM employees GROUP BY department) AS dept_stats WHERE avg_sal > 80000`. The inner query creates a result set, the outer query filters it. A correlated subquery, by contrast, references a column from the outer query and re-executes for each outer row: `SELECT e.name FROM employees e WHERE e.salary > (SELECT AVG(salary) FROM employees WHERE department = e.department)`. This finds employees earning above their own department's average — something that requires the inner query to "know" which department the outer row belongs to.

**Common Table Expressions (CTEs)** offer a cleaner syntax for the same idea. Instead of nesting queries, you name intermediate results with `WITH`: `WITH dept_avg AS (SELECT department, AVG(salary) AS avg_sal FROM employees GROUP BY department) SELECT e.name, d.avg_sal FROM employees e JOIN dept_avg d ON e.department = d.department WHERE e.salary > d.avg_sal`. The logic is identical to the correlated subquery version, but the CTE makes the data flow explicit and readable. CTEs also support **recursion** — a `WITH RECURSIVE` CTE can traverse hierarchical data like organizational charts or category trees by repeatedly joining a result set with itself.

One important practical note: subqueries, CTEs, and joins are often interchangeable, and the query optimizer frequently rewrites one form into another internally. A correlated subquery that looks like it would execute once per row is often transformed into a join by the optimizer. This means you should generally write whichever form is clearest to read and maintain, then check the execution plan only if performance is a concern. The exception is the `NOT IN` versus `NOT EXISTS` distinction — when the subquery can return NULLs, `NOT IN` produces unexpected results due to SQL's three-valued logic, so `NOT EXISTS` is the safer choice.
