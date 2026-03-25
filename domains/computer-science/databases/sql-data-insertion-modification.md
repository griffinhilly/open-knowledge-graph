---
id: sql-data-insertion-modification
title: 'SQL: INSERT, UPDATE, and DELETE (DML)'
domain: computer-science
course: databases
prerequisites:
- id: sql-table-creation-definition
  type: hard
builds-toward:
- acid-properties
tags:
- SQL
- DML
- INSERT
- UPDATE
- DELETE
- modification
stage: formal-systems
status: validated
---

# SQL: INSERT, UPDATE, and DELETE (DML)

## Core Idea
Data Manipulation Language (DML) modifies table contents. INSERT adds new rows, UPDATE changes existing row values, and DELETE removes rows. DML operations must respect constraints and are typically wrapped in transactions for consistency.

## How It's Best Learned
Practice INSERT with explicit column lists, multi-row inserts, and INSERT...SELECT. Practice UPDATE with WHERE conditions affecting multiple rows. Understand the importance of WHERE clauses to avoid accidental data loss.

## Questions

```yaml
- question: "A developer runs: UPDATE employees SET salary = 75000; What happens?"
  type: multiple-choice
  options:
    - "Only employees with NULL salaries are updated, since those are the unset rows"
    - "The statement fails with an error because a WHERE clause is required for UPDATE"
    - "Every row in the employees table has its salary set to 75000"
    - "Only the most recently inserted employee row is updated"
  answer: 2
  explanation: "Without a WHERE clause, UPDATE applies to every row in the table. SQL does not require a WHERE clause or warn you — it happily updates all rows. This is one of the most dangerous mistakes in SQL and a major reason to write the WHERE clause before the SET clause as a habit."

- question: "Why should INSERT statements always list column names explicitly rather than relying on positional order?"
  type: multiple-choice
  options:
    - "Listing column names is required by the SQL standard; positional inserts are not valid syntax"
    - "Positional inserts are significantly slower because the database must scan the full schema"
    - "If the table is later altered — columns added, reordered, or removed — positional inserts may silently insert values into the wrong columns"
    - "Column name lists enable constraint checking; positional inserts bypass NOT NULL validation"
  answer: 2
  explanation: "Positional inserts assume a specific column order. If the table schema changes — a column added in the middle, or the order revised — the values shift to the wrong columns without any error. Explicit column names make the mapping unambiguous and protect against schema drift. Constraints apply equally regardless, and performance is not materially affected."

- question: "A DELETE statement without a WHERE clause will fail with an error, because SQL requires you to specify which rows to delete."
  type: true-false
  answer: false
  explanation: "SQL does not require a WHERE clause on DELETE. A bare DELETE FROM tablename; is perfectly valid syntax and will delete every row in the table, leaving it empty — with no confirmation prompt. This is why wrapping destructive DML in a transaction (so you can ROLLBACK) and always including WHERE clauses are essential practices."

- question: "If you attempt to INSERT a row that violates a NOT NULL or FOREIGN KEY constraint, the database will reject the insert rather than storing invalid data."
  type: true-false
  answer: true
  explanation: "Constraints are enforced at the moment of DML execution. An INSERT violating NOT NULL, FOREIGN KEY, UNIQUE, or CHECK is rejected with an error and no row is stored. This is a core benefit of defining constraints at table creation: the database guarantees data integrity automatically, so application code doesn't need to duplicate that validation."

- question: "What is the purpose of wrapping UPDATE or DELETE statements in a transaction, and when would you use ROLLBACK?"
  type: short-answer
  answer: "A transaction lets you verify the effect of a destructive statement before making it permanent. After executing the UPDATE or DELETE, you SELECT to check affected rows. If correct, COMMIT makes the change permanent. If something is wrong, ROLLBACK undoes the entire operation as if it never happened."
  explanation: "UPDATE and DELETE have no built-in undo outside a transaction. Wrapping in BEGIN...COMMIT creates a checkpoint: the changes are visible within your session but not yet to others. Only on COMMIT do they become permanent. If the WHERE clause matched more rows than expected — a common mistake — ROLLBACK lets you escape without data loss."
```

## Explainer

Once you have created tables with DDL (CREATE TABLE), those tables are empty structures — a schema with no data. **Data Manipulation Language (DML)** is how you populate and maintain the contents of those structures. The three core DML statements are INSERT, UPDATE, and DELETE, and each interacts directly with the constraints and data types you defined when creating the table.

**INSERT** adds new rows. The simplest form specifies the table, the columns, and the values: `INSERT INTO employees (name, department, salary) VALUES ('Alice', 'Engineering', 95000)`. Always list columns explicitly rather than relying on column order — this protects you if the table structure changes later and makes your intent clear to anyone reading the query. You can insert multiple rows in a single statement by listing several value tuples separated by commas, which is significantly faster than running separate INSERT statements. A powerful variant, **INSERT...SELECT**, lets you populate a table from the results of a query — for example, copying all active users from one table into an archive table.

**UPDATE** modifies existing rows and almost always requires a **WHERE clause** to target specific rows. Writing `UPDATE employees SET salary = 100000` without a WHERE clause sets *every* employee's salary to 100,000 — a mistake that is easy to make and painful to fix. The WHERE clause works just like in SELECT: `UPDATE employees SET salary = 100000 WHERE id = 42` targets exactly one row. You can update multiple columns simultaneously and use expressions that reference current values: `SET salary = salary * 1.10` gives everyone a 10% raise.

**DELETE** removes rows and carries the same WHERE clause imperative as UPDATE. `DELETE FROM orders WHERE status = 'cancelled'` removes only cancelled orders; `DELETE FROM orders` with no WHERE clause empties the entire table. Because UPDATE and DELETE are destructive — there is no built-in "undo" — these operations are exactly why transactions matter. Wrapping DML in a transaction (BEGIN...COMMIT) lets you verify results before making changes permanent, and ROLLBACK gives you an escape hatch if something goes wrong. Every constraint you defined during table creation — NOT NULL, UNIQUE, FOREIGN KEY, CHECK — is enforced during DML operations, so an INSERT that violates a constraint will fail rather than corrupt your data.
