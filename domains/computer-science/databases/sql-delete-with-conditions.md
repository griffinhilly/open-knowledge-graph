---
id: sql-delete-with-conditions
title: 'DELETE Statements: Removing Rows with Conditions'
domain: computer-science
course: databases
prerequisites:
- id: sql-data-insertion-modification
  type: hard
- id: sql-filtering-conditions
  type: hard
tags:
- sql
- dml
- data-integrity
stage: formal-systems
status: draft
---

# DELETE Statements: Removing Rows with Conditions

## Core Idea
DELETE removes rows from a table based on WHERE conditions. Cascading deletes via foreign key constraints enforce referential integrity but require careful planning.

## Explainer

From your work with INSERT and UPDATE, you know that SQL's data manipulation language (DML) modifies table contents. DELETE is the third major DML operation — it removes rows from a table. The basic syntax is straightforward: `DELETE FROM customers WHERE status = 'inactive'` removes every row matching the condition. The WHERE clause works exactly as it does in SELECT — you can use comparisons, logical operators, subqueries, and even joins to identify which rows to remove. This is where your understanding of filtering conditions becomes essential, because the WHERE clause is the only thing standing between a targeted cleanup and accidentally emptying an entire table.

A DELETE without a WHERE clause — `DELETE FROM customers` — removes **every row** in the table. This is almost never what you want, and it's one of the most dangerous statements in SQL. In practice, you should always write and test your WHERE clause as a SELECT first: run `SELECT * FROM customers WHERE status = 'inactive'` to see exactly which rows will be affected, verify the count and contents, and only then change SELECT to DELETE. This habit prevents catastrophic data loss.

The complexity of DELETE increases when tables have **foreign key relationships**. If you try to delete a customer who has orders in another table, the database faces a referential integrity conflict — those orders reference a customer that would no longer exist. The foreign key constraint's **ON DELETE** action determines what happens: `RESTRICT` (the default in most databases) blocks the delete entirely, `CASCADE` automatically deletes the dependent rows too, `SET NULL` sets the foreign key column to NULL, and `SET DEFAULT` resets it to its default value. Cascading deletes are powerful but dangerous — deleting one parent row might cascade through multiple levels of related tables, removing far more data than you intended. Always trace the cascade path before relying on it.

For large-scale deletions, performance matters. Deleting millions of rows in a single transaction locks the table, fills the transaction log, and can block other operations for extended periods. A common technique is **batched deletion**: delete in chunks of 1,000 or 10,000 rows at a time using a loop with `DELETE FROM table WHERE condition LIMIT 10000`, committing between batches. This keeps lock durations short and allows other transactions to interleave. Some databases also offer `TRUNCATE TABLE` as a faster alternative when you want to remove all rows — it deallocates entire data pages rather than logging individual row deletions, but it cannot be filtered with a WHERE clause and may not fire triggers.
