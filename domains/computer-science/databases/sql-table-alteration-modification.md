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
status: draft
---

# SQL: ALTER TABLE and Schema Modification

## Core Idea
ALTER TABLE modifies table structure after creation—adding columns, dropping columns, renaming columns, changing data types, and adding/dropping constraints. Schema modifications must consider existing data and running applications that depend on the table structure.

## Explainer

You know how to create tables with CREATE TABLE, defining columns, data types, and constraints up front. ALTER TABLE is what you use when the design needs to change after the table already exists and contains data. Real schemas evolve constantly — new features require new columns, old columns become obsolete, constraints need tightening or relaxing, and data types occasionally need correction. ALTER TABLE handles all of these without requiring you to drop and recreate the table from scratch.

The most common operations are **adding columns**, **dropping columns**, **renaming columns**, and **modifying data types**. `ALTER TABLE orders ADD COLUMN tracking_number VARCHAR(50)` adds a new nullable column — existing rows get NULL in that column. `ALTER TABLE orders DROP COLUMN legacy_code` removes a column and all its data irreversibly. `ALTER TABLE orders RENAME COLUMN ship_date TO shipped_at` changes a column name without touching the data. `ALTER TABLE orders ALTER COLUMN status TYPE VARCHAR(100)` widens a data type. Each of these can succeed or fail depending on existing data: narrowing a VARCHAR from 100 to 50 will fail if any row contains a value longer than 50 characters, and changing a text column to an integer will fail if any values aren't valid numbers.

**Constraint modification** is equally important. You can add constraints after the fact: `ALTER TABLE orders ADD CONSTRAINT orders_customer_fk FOREIGN KEY (customer_id) REFERENCES customers(id)` adds a foreign key to an existing table, but only succeeds if every current customer_id actually exists in the customers table. `ALTER TABLE orders ALTER COLUMN email SET NOT NULL` enforces non-null going forward, but fails if any existing rows have NULL in that column. To drop a constraint, you reference it by name: `ALTER TABLE orders DROP CONSTRAINT orders_customer_fk`. This is why naming your constraints explicitly at creation time matters — auto-generated names are harder to reference later.

The practical concern with ALTER TABLE is that some operations **lock the table** for the duration. Adding a nullable column with no default is usually instant (the database just updates the catalog). But adding a column with a DEFAULT value on a large table may rewrite every row, locking the table for minutes or hours. Similarly, adding a NOT NULL constraint requires scanning every row to verify compliance. In production systems, these locking behaviors determine whether a schema change can happen during normal operations or requires a maintenance window. Understanding which ALTER operations are fast metadata changes and which require full table rewrites is essential for working with databases that serve live traffic.
