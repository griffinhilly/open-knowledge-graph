---
id: sql-joins
title: SQL Joins
domain: computer-science
course: databases
prerequisites:
- id: sql-select-basics
  type: hard
- id: primary-and-foreign-keys
  type: hard
builds-toward:
- sql-subqueries
- query-execution-plans
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

## Explainer

You know how to retrieve data from a single table with SELECT and how primary keys uniquely identify rows while foreign keys reference rows in other tables. **Joins** are the mechanism that puts these pieces together — they let you combine rows from two or more tables based on a matching condition, reconstructing the relationships that normalization split apart.

The most common join is the **INNER JOIN**. It returns only the rows where the join condition finds a match in both tables. If you join `orders` to `customers` on `orders.customer_id = customers.id`, you get one result row for each order paired with its customer data. Orders with no matching customer (orphaned foreign keys) and customers with no orders are both excluded. Think of it as the intersection: only rows with a partner on both sides survive.

**LEFT OUTER JOIN** (usually written just `LEFT JOIN`) keeps every row from the left table, whether or not it has a match on the right. When there is no match, the right-side columns are filled with NULL. This is essential when you want to find things that *don't* have a relationship — `SELECT customers.name FROM customers LEFT JOIN orders ON customers.id = orders.customer_id WHERE orders.id IS NULL` finds customers who have never placed an order. RIGHT JOIN is the mirror image, and FULL OUTER JOIN keeps unmatched rows from both sides.

A **self-join** joins a table to itself, which is useful whenever rows in the same table have relationships to each other. An `employees` table where each row has a `manager_id` pointing to another employee's `id` is the classic case: `SELECT e.name, m.name AS manager FROM employees e LEFT JOIN employees m ON e.manager_id = m.id`. You alias the table twice (here `e` and `m`) so the database can distinguish which "copy" you mean. Without self-joins, querying hierarchical or graph-structured data stored in a single table would require multiple round-trips or procedural code.

One critical detail: the join condition determines which rows pair up, but it does not filter the final result in the same way a WHERE clause does. For inner joins, putting a condition in ON versus WHERE produces the same result. But for outer joins, it matters. A condition in the ON clause filters during the join (unmatched rows still appear with NULLs), while a condition in the WHERE clause filters after the join (removing those NULL rows entirely, effectively converting the outer join back to an inner join). Getting this distinction right is essential for writing correct outer join queries.
