---
id: primary-key-foreign-key-constraints
title: Primary Keys and Foreign Key Relationships
domain: computer-science
course: databases
prerequisites:
- id: sql-constraint-enforcement
  type: hard
- id: entity-relationship-conceptual-design
  type: soft
builds-toward:
- functional-dependency-schema
tags:
- primary key
- foreign key
- referential integrity
- relationships
stage: formal-systems
status: draft
---

# Primary Keys and Foreign Key Relationships

## Core Idea
A primary key uniquely identifies each row in a table and cannot contain NULL values. A foreign key in one table references the primary key in another table, establishing relationships and enforcing referential integrity. Together they implement database relationships and prevent orphaned records.

## How It's Best Learned
Design multi-table schemas with primary and foreign keys, understand ON DELETE/UPDATE actions (CASCADE, SET NULL, RESTRICT), and practice enforcing referential integrity constraints.

## Explainer

From your work with constraint enforcement, you know that a database can reject invalid data automatically. Primary keys and foreign keys are the most important specific constraints for structuring multi-table databases. A **primary key** is a column (or combination of columns) that uniquely identifies every row in a table — no two rows can share the same primary key value, and the value can never be NULL. Think of it like a social security number for each row: every row gets exactly one, and no duplicates are allowed. When you declare a primary key, the database creates a unique index behind the scenes and enforces uniqueness on every INSERT and UPDATE.

A **foreign key** is where things get relational. A foreign key in one table holds values that must match a primary key in another table, creating a link between the two. For example, an `orders` table might have a `customer_id` foreign key that references the `id` primary key in a `customers` table. This means you cannot insert an order for a customer that does not exist — the database enforces **referential integrity** by checking that every foreign key value has a corresponding primary key in the referenced table. Without this constraint, you could end up with orphaned records: orders pointing to customers who were never created or were deleted.

The power of foreign keys becomes clearer when you consider what happens during deletions and updates. If you delete a customer, what should happen to their orders? The **ON DELETE** action controls this: `RESTRICT` prevents the deletion entirely (the default, and safest), `CASCADE` automatically deletes all related orders, and `SET NULL` sets the foreign key column to NULL, breaking the link but keeping the order record. The same options exist for `ON UPDATE` when a primary key value changes. Choosing the right action depends on your domain — cascading deletes make sense for a blog post and its comments, but restricting deletes makes sense for a customer with outstanding invoices.

In practice, every table should have a primary key, and every relationship between tables should be enforced with a foreign key. When you design schemas from entity-relationship diagrams, each relationship line in the diagram becomes a foreign key in the physical schema. The discipline of declaring these constraints up front means the database catches integrity violations at write time rather than letting corrupted data silently accumulate until a query returns nonsensical results.
