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

## Explainer

From your work with SELECT statements, you can retrieve and filter data from a single table. But real databases spread related data across multiple tables — customers in one, orders in another, products in a third. This **normalization** eliminates redundancy, but it means answering questions like "what did each customer order?" requires combining data from several tables. That is exactly what **INNER JOIN** does.

The basic syntax is `SELECT columns FROM table_a JOIN table_b ON table_a.key = table_b.key`. The ON clause specifies the **join condition** — typically matching a **foreign key** in one table to the **primary key** in another. For example, if an `orders` table has a `customer_id` column that references the `id` column in a `customers` table, you write: `SELECT customers.name, orders.total FROM customers JOIN orders ON customers.id = orders.customer_id`. The database examines every combination of rows from both tables and keeps only those where the condition is true.

The defining behavior of INNER JOIN is that it returns only **matching rows**. If a customer has no orders, that customer does not appear in the result. If an order somehow references a customer ID that does not exist, that order is excluded too. Both sides must satisfy the join condition. This is the key distinction you will encounter when you learn about outer joins later — outer joins can preserve unmatched rows from one or both sides, but INNER JOIN is strict: no match, no row.

You can join on multiple conditions (`ON a.x = b.x AND a.y = b.y`), join more than two tables by chaining JOIN clauses, and join on columns that are not primary or foreign keys (though key-based joins are the most common and usually the most efficient). When joining multiple tables, read the query as a pipeline: start with one table, join the second to get an intermediate result, then join the third to that intermediate result. Each JOIN narrows or expands the result set based on how many rows match. Building a mental picture of which rows survive each join is the most important skill — sketch a few sample rows from each table, walk through the matching by hand, and verify which combinations appear in the output.
