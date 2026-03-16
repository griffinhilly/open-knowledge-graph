---
id: sql-data-insertion-modification
title: 'SQL: INSERT, UPDATE, and DELETE (DML)'
domain: computer-science
course: databases
prerequisites:
- id: sql-table-creation-definition
  type: hard
builds-toward:
- transaction-properties-acid
tags:
- SQL
- DML
- INSERT
- UPDATE
- DELETE
- modification
stage: formal-systems
status: draft
---

# SQL: INSERT, UPDATE, and DELETE (DML)

## Core Idea
Data Manipulation Language (DML) modifies table contents. INSERT adds new rows, UPDATE changes existing row values, and DELETE removes rows. DML operations must respect constraints and are typically wrapped in transactions for consistency.

## How It's Best Learned
Practice INSERT with explicit column lists, multi-row inserts, and INSERT...SELECT. Practice UPDATE with WHERE conditions affecting multiple rows. Understand the importance of WHERE clauses to avoid accidental data loss.

## Explainer

Once you have created tables with DDL (CREATE TABLE), those tables are empty structures — a schema with no data. **Data Manipulation Language (DML)** is how you populate and maintain the contents of those structures. The three core DML statements are INSERT, UPDATE, and DELETE, and each interacts directly with the constraints and data types you defined when creating the table.

**INSERT** adds new rows. The simplest form specifies the table, the columns, and the values: `INSERT INTO employees (name, department, salary) VALUES ('Alice', 'Engineering', 95000)`. Always list columns explicitly rather than relying on column order — this protects you if the table structure changes later and makes your intent clear to anyone reading the query. You can insert multiple rows in a single statement by listing several value tuples separated by commas, which is significantly faster than running separate INSERT statements. A powerful variant, **INSERT...SELECT**, lets you populate a table from the results of a query — for example, copying all active users from one table into an archive table.

**UPDATE** modifies existing rows and almost always requires a **WHERE clause** to target specific rows. Writing `UPDATE employees SET salary = 100000` without a WHERE clause sets *every* employee's salary to 100,000 — a mistake that is easy to make and painful to fix. The WHERE clause works just like in SELECT: `UPDATE employees SET salary = 100000 WHERE id = 42` targets exactly one row. You can update multiple columns simultaneously and use expressions that reference current values: `SET salary = salary * 1.10` gives everyone a 10% raise.

**DELETE** removes rows and carries the same WHERE clause imperative as UPDATE. `DELETE FROM orders WHERE status = 'cancelled'` removes only cancelled orders; `DELETE FROM orders` with no WHERE clause empties the entire table. Because UPDATE and DELETE are destructive — there is no built-in "undo" — these operations are exactly why transactions matter. Wrapping DML in a transaction (BEGIN...COMMIT) lets you verify results before making changes permanent, and ROLLBACK gives you an escape hatch if something goes wrong. Every constraint you defined during table creation — NOT NULL, UNIQUE, FOREIGN KEY, CHECK — is enforced during DML operations, so an INSERT that violates a constraint will fail rather than corrupt your data.
