---
id: sql-subquery-fundamentals
title: 'SQL: Subqueries (Scalar, Row, Table)'
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
builds-toward:
- sql-correlated-query-evaluation
- sql-group-aggregate-functions
tags:
- SQL
- subquery
- nested query
- inner query
stage: formal-systems
status: draft
---

# SQL: Subqueries (Scalar, Row, Table)

## Core Idea
A subquery (inner query) is a SELECT statement nested within another SQL statement. Scalar subqueries return one value, row subqueries return multiple columns, and table subqueries return multiple rows. Subqueries enable modular query construction and complex filtering.

## Explainer

You already know how to write SELECT statements to retrieve and filter data from tables. A **subquery** takes that same SELECT and nests it inside another SQL statement — in a WHERE clause, a FROM clause, or even a SELECT list. The inner query runs first and produces a result that the outer query then uses. This lets you break complex questions into logical steps rather than trying to express everything in a single flat query.

The simplest form is a **scalar subquery**, which returns exactly one value — one row, one column. For example, to find all products priced above the average: `SELECT * FROM products WHERE price > (SELECT AVG(price) FROM products)`. The inner query computes a single number (the average price), and the outer query uses it as a comparison value. If a scalar subquery accidentally returns more than one row, the database raises an error, so you need to be sure the inner query is guaranteed to produce a single value (aggregation functions are a safe bet).

A **table subquery** returns multiple rows and is used with operators like `IN`, `ANY`, `ALL`, or `EXISTS`. To find customers who have placed orders, you could write `SELECT * FROM customers WHERE id IN (SELECT customer_id FROM orders)`. The inner query produces a list of customer IDs, and the outer query checks membership against that list. Table subqueries in the FROM clause act as temporary tables (sometimes called **derived tables**): `SELECT dept, avg_sal FROM (SELECT department AS dept, AVG(salary) AS avg_sal FROM employees GROUP BY department) AS dept_averages WHERE avg_sal > 50000`. The subquery computes a result set that the outer query then filters, exactly as if it were a regular table.

The key distinction to internalize is between **uncorrelated** and correlated subqueries (the correlated case is covered in a subsequent topic). An uncorrelated subquery is self-contained — it does not reference any columns from the outer query, so the database can execute it once and reuse the result. All the examples above are uncorrelated. This independence means the optimizer can evaluate the subquery first, cache its result, and then process the outer query efficiently. When you find yourself writing a subquery that needs to "see" the current row of the outer query, you have crossed into correlated territory, which has different performance characteristics and evaluation semantics.
