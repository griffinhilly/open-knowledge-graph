---
id: sql-joins
title: SQL Joins
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
- id: primary-and-foreign-keys
  type: hard
builds-toward:
- sql-subqueries
- query-optimization
tags:
- SQL
- JOIN
- INNER JOIN
- LEFT JOIN
- OUTER JOIN
- self-join
stage: formal-systems
status: validated
---

# SQL Joins

## Core Idea
Joins combine rows from two or more tables based on a related column condition, enabling the reconstruction of related data stored in separate tables. INNER JOIN returns only rows with matching values in both tables; LEFT OUTER JOIN includes all rows from the left table with NULLs for unmatched right-side rows; FULL OUTER JOIN includes all rows from both sides. Self-joins allow a table to be joined with itself, useful for hierarchical or recursive data. The join condition typically matches a foreign key to the referenced primary key.

## How It's Best Learned
Draw Venn diagrams for each join type, then run queries to verify behavior. Work through examples where rows don't match to understand when and where NULLs appear in outer joins. Rewrite a LEFT JOIN as a RIGHT JOIN by swapping table order.

## Common Misconceptions
- A CROSS JOIN (Cartesian product) produces n×m rows with no filter — this is almost always unintentional if written by accident.
- LEFT JOIN and RIGHT JOIN are symmetric; you can always rewrite one as the other by swapping table positions.
- INNER JOIN is not always more efficient than OUTER JOIN; the query planner decides execution strategy based on statistics.

## Questions

```yaml
- question: "You want to find all customers who have never placed an order. You have a `customers` table and an `orders` table joined by `customer_id`. Which query correctly solves this?"
  type: multiple-choice
  options:
    - "SELECT c.name FROM customers c INNER JOIN orders o ON c.id = o.customer_id WHERE o.id IS NULL"
    - "SELECT c.name FROM customers c LEFT JOIN orders o ON c.id = o.customer_id WHERE o.id IS NULL"
    - "SELECT c.name FROM customers c RIGHT JOIN orders o ON c.id = o.customer_id WHERE o.id IS NULL"
    - "SELECT c.name FROM customers c INNER JOIN orders o ON c.id = o.customer_id WHERE o.customer_id IS NULL"
  answer: 1
  explanation: "LEFT JOIN keeps every customer row, filling order columns with NULL where no match exists. Then WHERE o.id IS NULL isolates the customers with no matching orders. Option A (INNER JOIN) is the classic mistake: INNER JOIN only returns rows that match on both sides, so customers with no orders are excluded before the WHERE clause even runs — the result would always be empty. RIGHT JOIN (option C) would keep all orders, not all customers, which is the opposite of what we want."

- question: "You add a filter condition `AND o.status = 'shipped'` to a LEFT JOIN query. Where you place this condition — in the ON clause versus the WHERE clause — produces different results. Which statement correctly explains why?"
  type: multiple-choice
  options:
    - "ON and WHERE are aliases in SQL; the query planner treats them identically for LEFT JOINs"
    - "A condition in ON filters before rows are returned, while WHERE filters after, but the final row count is the same because SQL optimizes both paths"
    - "A condition in ON filters during the join, so unmatched rows still appear with NULLs; a condition in WHERE filters after the join, removing those NULL rows and converting the LEFT JOIN to an INNER JOIN"
    - "Conditions belong in WHERE for correctness; ON should only contain the primary key match"
  answer: 2
  explanation: "This is the most important subtlety of outer joins. In `LEFT JOIN orders o ON c.id = o.customer_id AND o.status = 'shipped'`, customers with no shipped orders still appear in the result — their order columns are NULL. But in `LEFT JOIN orders o ON c.id = o.customer_id WHERE o.status = 'shipped'`, the WHERE clause runs after the join and eliminates all rows where o.status is NULL (including unmatched customers), effectively making it an INNER JOIN. Getting this wrong silently produces incorrect results with no error message."

- question: "A LEFT JOIN query that returns no rows from the left table proves that no rows in the left table matched the join condition."
  type: true-false
  answer: false
  explanation: "LEFT JOIN guarantees that every row from the left table appears in the result, with NULL values for the right-side columns when there is no match. If a LEFT JOIN returns no rows at all, the problem is not the join — it must be a WHERE clause (or other filter) eliminating the unmatched rows after the join. A common bug is adding a WHERE condition on a right-side column without checking for NULL, which turns the LEFT JOIN into an effective INNER JOIN and silently discards unmatched rows."

- question: "LEFT JOIN and RIGHT JOIN are functionally identical; you can always rewrite one as the other by swapping the order of the two tables."
  type: true-false
  answer: true
  explanation: "This is a genuine symmetry: `A LEFT JOIN B ON condition` returns the same data as `B RIGHT JOIN A ON condition` — the table that 'keeps all rows' is just written on a different side. In practice, most SQL developers use LEFT JOIN consistently and swap table positions rather than mixing LEFT and RIGHT joins in the same query, because it makes query logic easier to follow."

- question: "Explain the critical difference between placing a filter condition in the ON clause versus the WHERE clause of an outer (LEFT/RIGHT) JOIN query, and give an example of where getting this wrong would produce a silently incorrect result."
  type: short-answer
  answer: "A condition in ON is evaluated during the join: rows that don't satisfy it are treated as non-matching, so the left-side row still appears with NULLs for right-side columns. A condition in WHERE is evaluated after the join: it eliminates rows from the already-joined result, including rows where right-side columns are NULL (i.e., unmatched rows). Moving a filter from ON to WHERE on a LEFT JOIN silently converts it into an INNER JOIN. Example: finding customers with no 'shipped' orders — ON gets unmatched customers with NULLs; WHERE o.status = 'shipped' then drops them, returning zero results instead of the intended list."
  explanation: "The practical consequence is that SQL returns no error — wrong ON/WHERE placement produces results that look plausible but count the wrong thing. A query meant to list customers without shipped orders instead lists only customers WITH shipped orders, with no warning. This is one of the most common subtle bugs in SQL queries involving outer joins."
```

## Explainer

You know how to retrieve data from a single table with SELECT and how primary keys uniquely identify rows while foreign keys reference rows in other tables. **Joins** are the mechanism that puts these pieces together — they let you combine rows from two or more tables based on a matching condition, reconstructing the relationships that normalization split apart.

The most common join is the **INNER JOIN**. It returns only the rows where the join condition finds a match in both tables. If you join `orders` to `customers` on `orders.customer_id = customers.id`, you get one result row for each order paired with its customer data. Orders with no matching customer (orphaned foreign keys) and customers with no orders are both excluded. Think of it as the intersection: only rows with a partner on both sides survive.

**LEFT OUTER JOIN** (usually written just `LEFT JOIN`) keeps every row from the left table, whether or not it has a match on the right. When there is no match, the right-side columns are filled with NULL. This is essential when you want to find things that *don't* have a relationship — `SELECT customers.name FROM customers LEFT JOIN orders ON customers.id = orders.customer_id WHERE orders.id IS NULL` finds customers who have never placed an order. RIGHT JOIN is the mirror image, and FULL OUTER JOIN keeps unmatched rows from both sides.

A **self-join** joins a table to itself, which is useful whenever rows in the same table have relationships to each other. An `employees` table where each row has a `manager_id` pointing to another employee's `id` is the classic case: `SELECT e.name, m.name AS manager FROM employees e LEFT JOIN employees m ON e.manager_id = m.id`. You alias the table twice (here `e` and `m`) so the database can distinguish which "copy" you mean. Without self-joins, querying hierarchical or graph-structured data stored in a single table would require multiple round-trips or procedural code.

One critical detail: the join condition determines which rows pair up, but it does not filter the final result in the same way a WHERE clause does. For inner joins, putting a condition in ON versus WHERE produces the same result. But for outer joins, it matters. A condition in the ON clause filters during the join (unmatched rows still appear with NULLs), while a condition in the WHERE clause filters after the join (removing those NULL rows entirely, effectively converting the outer join back to an inner join). Getting this distinction right is essential for writing correct outer join queries.
