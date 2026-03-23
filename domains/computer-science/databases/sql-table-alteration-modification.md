---
id: sql-table-alteration-modification
title: 'SQL: ALTER TABLE and Schema Modification'
domain: computer-science
course: databases
prerequisites:
- id: sql-table-creation-definition
  type: hard
tags:
- SQL
- ALTER TABLE
- DDL
- schema modification
stage: formal-systems
status: validated
---

# SQL: ALTER TABLE and Schema Modification

## Core Idea
ALTER TABLE modifies table structure after creation—adding columns, dropping columns, renaming columns, changing data types, and adding/dropping constraints. Schema modifications must consider existing data and running applications that depend on the table structure.

## Questions

```yaml
- question: "Your team wants to add a NOT NULL column with a DEFAULT value to a 50-million-row orders table during peak business hours. Which outcome should you expect?"
  type: multiple-choice
  options:
    - "The operation completes instantly because adding a default is a metadata-only change"
    - "The operation rewrites every row to store the default value, locking the table for potentially minutes and blocking all reads and writes"
    - "The operation fails immediately because NOT NULL columns cannot have defaults"
    - "The operation succeeds but existing rows get NULL instead of the default value"
  answer: 1
  explanation: "Adding a column with a DEFAULT value on many older or certain database configurations requires rewriting every existing row to store the default, taking an exclusive lock for the duration. On a 50-million-row table this can block all queries for minutes. Modern PostgreSQL (v11+) handles this specific case more efficiently for volatile defaults, but behavior varies by engine and version. The practical lesson is: always test ALTER TABLE operations on production-sized data, and plan schema changes for maintenance windows when they involve full rewrites."

- question: "An ALTER TABLE command attempts to change a column from VARCHAR(100) to VARCHAR(50). Under what condition will this operation fail?"
  type: multiple-choice
  options:
    - "Always — data type changes require dropping and recreating the table"
    - "Never — the database silently truncates values that exceed the new length"
    - "Only if the column has a foreign key referencing another table"
    - "If any existing row contains a value longer than 50 characters in that column"
  answer: 3
  explanation: "Narrowing a data type is a constraint tightening: the database must verify that all existing data fits the new type. If even one row has a 51-character value, the ALTER TABLE will fail with a constraint violation — it does not silently truncate. This is the general principle: any ALTER TABLE that imposes a new constraint (NOT NULL, shorter length, type change, foreign key) will fail if current data violates that constraint. The fix is either to clean the data first or to widen rather than narrow."

- question: "An ALTER TABLE operation that adds a nullable column with no default value is always a fast, metadata-only change regardless of table size."
  type: true-false
  answer: true
  explanation: "Adding a nullable column with no default does not need to touch existing rows — the database records the new column in the catalog and uses NULL as the implicit value for existing rows without actually rewriting storage. This is one of the few ALTER TABLE operations that is genuinely instant even on billion-row tables. The contrast with adding a NOT NULL column with a default (which may require rewriting rows) is an important practical distinction for production deployments."

- question: "Dropping a column with ALTER TABLE DROP COLUMN is a reversible operation because the data remains in the table's storage pages until the next VACUUM."
  type: true-false
  answer: false
  explanation: "From the application and SQL perspective, DROP COLUMN is irreversible. While some databases mark the column as invisible rather than immediately reclaiming storage space, the column is logically deleted and cannot be accessed or recovered through SQL. You cannot un-drop a column — once committed, the schema change and the data are gone (short of restoring from a backup). This makes dropping columns among the more dangerous ALTER TABLE operations, and naming your backup state before running it is essential practice."

- question: "Why do some ALTER TABLE operations lock the table for seconds or minutes on large tables, while others complete almost instantly? What determines which category an operation falls into?"
  type: short-answer
  answer: "The key distinction is whether the operation requires reading and rewriting existing rows (a table rewrite) or only updating the database catalog metadata. Operations like adding a nullable column with no default, renaming a column, or dropping a constraint are metadata-only — the database records the change in system tables and returns immediately. Operations like adding a NOT NULL constraint, adding a column with a default, changing a data type, or adding an index that must be built require scanning and sometimes rewriting every row, holding an exclusive lock for the duration."
  explanation: "Understanding this distinction is critical for production database management. The rule of thumb: anything that validates or transforms existing data requires a scan; anything that only changes how future writes are interpreted is metadata-only. Many production teams use tools like pg_repack or online schema change utilities precisely to avoid the table lock during large rewrites."
```

## Explainer

You know how to create tables with CREATE TABLE, defining columns, data types, and constraints up front. ALTER TABLE is what you use when the design needs to change after the table already exists and contains data. Real schemas evolve constantly — new features require new columns, old columns become obsolete, constraints need tightening or relaxing, and data types occasionally need correction. ALTER TABLE handles all of these without requiring you to drop and recreate the table from scratch.

The most common operations are **adding columns**, **dropping columns**, **renaming columns**, and **modifying data types**. `ALTER TABLE orders ADD COLUMN tracking_number VARCHAR(50)` adds a new nullable column — existing rows get NULL in that column. `ALTER TABLE orders DROP COLUMN legacy_code` removes a column and all its data irreversibly. `ALTER TABLE orders RENAME COLUMN ship_date TO shipped_at` changes a column name without touching the data. `ALTER TABLE orders ALTER COLUMN status TYPE VARCHAR(100)` widens a data type. Each of these can succeed or fail depending on existing data: narrowing a VARCHAR from 100 to 50 will fail if any row contains a value longer than 50 characters, and changing a text column to an integer will fail if any values aren't valid numbers.

**Constraint modification** is equally important. You can add constraints after the fact: `ALTER TABLE orders ADD CONSTRAINT orders_customer_fk FOREIGN KEY (customer_id) REFERENCES customers(id)` adds a foreign key to an existing table, but only succeeds if every current customer_id actually exists in the customers table. `ALTER TABLE orders ALTER COLUMN email SET NOT NULL` enforces non-null going forward, but fails if any existing rows have NULL in that column. To drop a constraint, you reference it by name: `ALTER TABLE orders DROP CONSTRAINT orders_customer_fk`. This is why naming your constraints explicitly at creation time matters — auto-generated names are harder to reference later.

The practical concern with ALTER TABLE is that some operations **lock the table** for the duration. Adding a nullable column with no default is usually instant (the database just updates the catalog). But adding a column with a DEFAULT value on a large table may rewrite every row, locking the table for minutes or hours. Similarly, adding a NOT NULL constraint requires scanning every row to verify compliance. In production systems, these locking behaviors determine whether a schema change can happen during normal operations or requires a maintenance window. Understanding which ALTER operations are fast metadata changes and which require full table rewrites is essential for working with databases that serve live traffic.
