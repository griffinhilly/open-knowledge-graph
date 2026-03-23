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
status: validated
---

# SQL: Subqueries (Scalar, Row, Table)

## Core Idea
A subquery (inner query) is a SELECT statement nested within another SQL statement. Scalar subqueries return one value, row subqueries return multiple columns, and table subqueries return multiple rows. Subqueries enable modular query construction and complex filtering.

## Questions

```yaml
- question: "You want to retrieve all products whose price exceeds the average price in the table. Which query correctly accomplishes this?"
  type: multiple-choice
  options:
    - "SELECT * FROM products WHERE price > AVG(price)"
    - "SELECT * FROM products WHERE price > (SELECT AVG(price) FROM products)"
    - "SELECT *, AVG(price) FROM products WHERE price > AVG(price)"
    - "SELECT * FROM products HAVING price > AVG(price)"
  answer: 1
  explanation: "Option B is correct. The WHERE clause filters individual rows before aggregation, so aggregate functions like AVG() cannot be used directly in WHERE — the database doesn't know what AVG means in that context. A scalar subquery solves this: the inner query executes first, computes a single average value, and the outer query uses that number for comparison. Option C also fails for the same reason (aggregate in WHERE). Option D misuses HAVING — that clause applies after GROUP BY, not to ungrouped row comparisons."

- question: "In the query SELECT * FROM products WHERE price > (SELECT AVG(price) FROM products), how many times does the inner query execute?"
  type: multiple-choice
  options:
    - "Once for every row in the products table — it recalculates the average for each row being evaluated"
    - "Once — it is an uncorrelated subquery and the database executes it once, reusing the result for all row comparisons"
    - "Once for every distinct price value in the table"
    - "It depends on how many rows actually exceed the average"
  answer: 1
  explanation: "This is an uncorrelated subquery: the inner SELECT references no columns from the outer query, so it is completely self-contained. The database optimizer recognizes this and executes it once, caches the result (a single average price), then uses that cached value to evaluate every row in the outer query. This is one of the key efficiency properties of uncorrelated subqueries. A correlated subquery (which would reference the outer query's current row) would need to re-execute for each outer row — a very different and typically more expensive operation."

- question: "If a scalar subquery returns more than one row, the database will silently use only the first row and discard the rest."
  type: true-false
  answer: false
  explanation: "False — this is an important safety property of SQL. A scalar subquery must return exactly one row and one column; if it returns multiple rows, the database raises a runtime error rather than silently picking one. This strict enforcement exists because the outer query semantics depend on having a single value: 'price > (scalar value)' is well-defined, but 'price > (multiple values)' is ambiguous. To compare against multiple values, you must use a different operator (IN, ANY, ALL) with a table subquery. The error behavior protects you from silently wrong results."

- question: "A table subquery in the FROM clause (a derived table) behaves like a temporary table — the outer query can filter, join, or aggregate its results exactly as if it were a regular named table."
  type: true-false
  answer: true
  explanation: "True. When a SELECT statement appears in the FROM clause, the database evaluates it first and treats its result set as a temporary, anonymous table for the duration of the outer query. You can give it an alias and reference it like any other table. This is powerful for multi-step analysis: you can compute an intermediate aggregation in the subquery, then filter or join that result in the outer query. For example, computing average salaries per department in the inner query, then selecting only departments with above-average pay in the outer query — a two-step operation that would be awkward in a single flat query."

- question: "Explain the difference between using a scalar subquery in a WHERE clause and using an aggregate function like AVG() directly in a WHERE clause — why does one work and the other fail?"
  type: short-answer
  answer: "WHERE clauses are evaluated row by row, before any aggregation occurs. An aggregate function like AVG() requires scanning all the rows it operates on to compute its result — it is inherently a set-level operation. Placing AVG() in a WHERE clause is a logical contradiction: the database would need to know the average to filter rows, but it needs to filter rows to compute the average. A scalar subquery resolves this by computing the aggregate first, in a separate inner query that runs against the full table, then producing a single concrete number that the outer WHERE clause can use for row-by-row comparison. The inner query completes its set-level computation before the outer query begins its row-level filtering."
  explanation: "This is also why HAVING exists: HAVING filters after GROUP BY aggregation, making it the correct place for aggregate conditions on grouped results. WHERE filters before aggregation. Understanding this distinction — and using subqueries when you need an aggregate for row-level filtering — is a foundational SQL skill."
```

## Explainer

You already know how to write SELECT statements to retrieve and filter data from tables. A **subquery** takes that same SELECT and nests it inside another SQL statement — in a WHERE clause, a FROM clause, or even a SELECT list. The inner query runs first and produces a result that the outer query then uses. This lets you break complex questions into logical steps rather than trying to express everything in a single flat query.

The simplest form is a **scalar subquery**, which returns exactly one value — one row, one column. For example, to find all products priced above the average: `SELECT * FROM products WHERE price > (SELECT AVG(price) FROM products)`. The inner query computes a single number (the average price), and the outer query uses it as a comparison value. If a scalar subquery accidentally returns more than one row, the database raises an error, so you need to be sure the inner query is guaranteed to produce a single value (aggregation functions are a safe bet).

A **table subquery** returns multiple rows and is used with operators like `IN`, `ANY`, `ALL`, or `EXISTS`. To find customers who have placed orders, you could write `SELECT * FROM customers WHERE id IN (SELECT customer_id FROM orders)`. The inner query produces a list of customer IDs, and the outer query checks membership against that list. Table subqueries in the FROM clause act as temporary tables (sometimes called **derived tables**): `SELECT dept, avg_sal FROM (SELECT department AS dept, AVG(salary) AS avg_sal FROM employees GROUP BY department) AS dept_averages WHERE avg_sal > 50000`. The subquery computes a result set that the outer query then filters, exactly as if it were a regular table.

The key distinction to internalize is between **uncorrelated** and correlated subqueries (the correlated case is covered in a subsequent topic). An uncorrelated subquery is self-contained — it does not reference any columns from the outer query, so the database can execute it once and reuse the result. All the examples above are uncorrelated. This independence means the optimizer can evaluate the subquery first, cache its result, and then process the outer query efficiently. When you find yourself writing a subquery that needs to "see" the current row of the outer query, you have crossed into correlated territory, which has different performance characteristics and evaluation semantics.
