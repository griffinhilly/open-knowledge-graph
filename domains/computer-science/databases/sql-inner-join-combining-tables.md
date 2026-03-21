---
id: sql-inner-join-combining-tables
title: 'SQL: INNER JOIN and Basic Joins'
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
- id: relational-algebra-fundamentals
  type: soft
builds-toward:
  - sql-outer-joins-comprehensive
  - sql-complex-join-types
tags:
- SQL
- JOIN
- INNER JOIN
- combining tables
stage: formal-systems
status: draft
---
# SQL: INNER JOIN and Basic Joins

## Core Idea
INNER JOIN combines rows from two tables where the join condition is true. The join condition typically matches foreign keys to primary keys. INNER JOIN returns only rows with matches in both tables, implementing the relational algebra join operation.

## How It's Best Learned
Start with simple INNER JOINs on primary key–foreign key relationships, then practice joins on non-key columns and multiple join conditions. Visualize which rows are included and excluded.

## Questions

```yaml
- question: "A database has a 'customers' table with 200 customers and an 'orders' table with 350 orders. After running SELECT * FROM customers INNER JOIN orders ON customers.id = orders.customer_id, the result contains 310 rows. What is the most likely explanation?"
  type: multiple-choice
  options:
    - "INNER JOIN randomly excludes rows to improve query performance"
    - "Some customers placed multiple orders, and 40 customers have no orders at all — both effects reduce or multiply row counts"
    - "The orders table is corrupted and missing 40 rows"
    - "INNER JOIN combines the row counts of both tables and then removes duplicates"
  answer: 1
  explanation: "INNER JOIN returns one row for each matching pair. A customer with 3 orders contributes 3 rows; a customer with 0 orders contributes 0 rows. The result row count is determined entirely by how many rows in each table match the join condition — it can be more than either table (due to one-to-many relationships) or fewer (due to unmatched rows)."

- question: "You write: SELECT e.name, d.dept_name FROM employees e JOIN departments d ON e.dept_id = d.id. Which employees will appear in the results?"
  type: multiple-choice
  options:
    - "All employees, with NULL in dept_name for those without a matching department"
    - "Only employees whose dept_id matches an existing id in the departments table"
    - "Only departments that have at least one employee assigned"
    - "Every combination of every employee with every department"
  answer: 1
  explanation: "INNER JOIN is strict: only rows where the join condition is satisfied appear in the results. An employee with a dept_id that doesn't match any department id is silently excluded — no NULL, no row at all. If you need to keep all employees regardless of whether they have a department, you would use a LEFT JOIN instead."

- question: "If a 'products' table has 50 products and an 'order_items' table records which products appear in which orders, an INNER JOIN between them could return more than 50 rows."
  type: true-false
  answer: true
  explanation: "One product can appear in many orders, so it generates multiple rows in order_items. When joined, each order_items row for that product produces a separate result row. A popular product appearing in 20 orders contributes 20 rows to the join result, not 1."

- question: "An INNER JOIN between tables A and B always returns the same number of rows as the smaller of the two tables."
  type: true-false
  answer: false
  explanation: "The result size depends entirely on how many rows match the join condition, not on the size of either table. If many rows on one side match a single row on the other, the result can be larger than both individual tables. If many rows have no match, the result can be smaller than either. Size of either table is not a reliable predictor."

- question: "Explain why an INNER JOIN is described as 'strict' and what this means for rows that appear in one table but not the other."
  type: short-answer
  answer: "INNER JOIN only returns rows where the join condition is satisfied on both sides. If a row in table A has no matching row in table B (or vice versa), it is completely excluded from the result — it does not appear with NULLs, it simply does not appear. This 'strictness' is what distinguishes INNER JOIN from outer joins, which can preserve unmatched rows."
  explanation: "This is the defining behavior of INNER JOIN and the most common source of unexpected missing data in query results. When a query returns fewer rows than expected, the first thing to check is whether an INNER JOIN is silently excluding unmatched rows — a LEFT or RIGHT JOIN may be more appropriate for the use case."
```

## Explainer

From your work with SELECT statements, you can retrieve and filter data from a single table. But real databases spread related data across multiple tables — customers in one, orders in another, products in a third. This **normalization** eliminates redundancy, but it means answering questions like "what did each customer order?" requires combining data from several tables. That is exactly what **INNER JOIN** does.

The basic syntax is `SELECT columns FROM table_a JOIN table_b ON table_a.key = table_b.key`. The ON clause specifies the **join condition** — typically matching a **foreign key** in one table to the **primary key** in another. For example, if an `orders` table has a `customer_id` column that references the `id` column in a `customers` table, you write: `SELECT customers.name, orders.total FROM customers JOIN orders ON customers.id = orders.customer_id`. The database examines every combination of rows from both tables and keeps only those where the condition is true.

The defining behavior of INNER JOIN is that it returns only **matching rows**. If a customer has no orders, that customer does not appear in the result. If an order somehow references a customer ID that does not exist, that order is excluded too. Both sides must satisfy the join condition. This is the key distinction you will encounter when you learn about outer joins later — outer joins can preserve unmatched rows from one or both sides, but INNER JOIN is strict: no match, no row.

You can join on multiple conditions (`ON a.x = b.x AND a.y = b.y`), join more than two tables by chaining JOIN clauses, and join on columns that are not primary or foreign keys (though key-based joins are the most common and usually the most efficient). When joining multiple tables, read the query as a pipeline: start with one table, join the second to get an intermediate result, then join the third to that intermediate result. Each JOIN narrows or expands the result set based on how many rows match. Building a mental picture of which rows survive each join is the most important skill — sketch a few sample rows from each table, walk through the matching by hand, and verify which combinations appear in the output.
