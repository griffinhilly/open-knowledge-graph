---
id: sql-common-table-expressions-with
title: 'Common Table Expressions (CTEs): WITH Clause'
domain: computer-science
course: databases
prerequisites:
- id: sql-subqueries
  type: hard
builds-toward:
- sql-recursive-common-table-expressions
tags:
- sql
- subqueries
- readability
- composition
stage: formal-systems
status: draft
---

# Common Table Expressions (CTEs): WITH Clause

## Core Idea
CTEs, defined with the WITH clause, create named intermediate result sets that can be referenced in the main query. They improve readability and allow multiple references to the same temporary result.

## How It's Best Learned
Refactor a complex nested subquery into a CTE, then add a second CTE to build a more sophisticated query.

## Common Misconceptions
CTEs are not materialized by default—they are expanded at query time. Multiple references to the same CTE are re-executed unless the database optimizes them away.

## Explainer

You already know how to use subqueries — nested SELECT statements embedded within a larger query. Subqueries work, but they can become deeply nested and hard to read. A **Common Table Expression** (CTE) solves this by letting you define a named temporary result set *before* the main query, using the WITH clause. Instead of burying logic three levels deep inside parentheses, you pull each logical step out, give it a name, and then reference that name in your main query as if it were a table.

Here is the structural pattern. You write `WITH cte_name AS (SELECT ...)` followed by your main query that references `cte_name`. For example, suppose you want to find departments where average salary exceeds $100,000. With a subquery, you would nest the aggregation inside the WHERE clause. With a CTE, you write: `WITH dept_avg AS (SELECT department_id, AVG(salary) AS avg_sal FROM employees GROUP BY department_id) SELECT * FROM dept_avg WHERE avg_sal > 100000`. The logic reads top-to-bottom — first compute averages, then filter — rather than inside-out.

CTEs become especially valuable when you need to reference the same intermediate result multiple times. A subquery forces you to duplicate the entire nested SELECT in each location, creating maintenance headaches and potential inconsistencies. A CTE lets you define the computation once and use its name wherever needed. You can also chain multiple CTEs by separating them with commas: `WITH step1 AS (...), step2 AS (SELECT ... FROM step1), step3 AS (SELECT ... FROM step2) SELECT ... FROM step3`. Each step can reference any previously defined CTE, building a pipeline of transformations.

One important caveat: CTEs are typically *not* materialized. The database treats a CTE like an inline view — it substitutes the CTE's definition wherever it is referenced and optimizes the combined query. This means referencing a CTE three times may execute its underlying query three times, not once. Some databases (like PostgreSQL 12+) let you control this with `MATERIALIZED` and `NOT MATERIALIZED` hints, but the default behavior varies. CTEs are primarily a readability and maintainability tool rather than a performance optimization. For the performance dimension, materialized views or temporary tables are more explicit choices.
