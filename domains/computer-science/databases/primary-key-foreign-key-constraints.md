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

## Questions

```yaml
- question: "You attempt to insert a row into an `orders` table with `customer_id = 99`, but no row with `id = 99` exists in the `customers` table. A foreign key constraint is in place. What happens?"
  type: multiple-choice
  options:
    - "The insert succeeds and creates an orphaned order record"
    - "The database automatically creates a customer with id = 99 to maintain integrity"
    - "The insert is rejected because the foreign key value has no matching primary key in the referenced table"
    - "The insert succeeds but sets customer_id to NULL automatically"
  answer: 2
  explanation: "This is the core purpose of a foreign key constraint: it enforces referential integrity by rejecting any write that would create a reference to a non-existent row. Without this constraint, option A would happen — orphaned records silently accumulate. Options B and D are not default behaviors; the database does not fabricate missing parents or silently override values."

- question: "A `departments` table and an `employees` table are linked by `employees.dept_id` referencing `departments.dept_id` with `ON DELETE CASCADE`. What happens when a department row is deleted?"
  type: multiple-choice
  options:
    - "The deletion is blocked until all employees are manually reassigned to another department"
    - "All employee rows belonging to that department are also automatically deleted"
    - "All employee rows in that department have their dept_id set to NULL"
    - "The foreign key constraint is temporarily suspended during the deletion"
  answer: 1
  explanation: "CASCADE propagates the delete: removing the parent row triggers automatic deletion of all child rows referencing it. Option C describes SET NULL behavior; option A describes RESTRICT (the default). Understanding the three ON DELETE actions — RESTRICT, CASCADE, SET NULL — is essential for designing schemas that behave correctly when referenced data is modified."

- question: "A primary key column can contain NULL values as long as only one row has that NULL."
  type: true-false
  answer: false
  explanation: "Primary keys must never contain NULL, period. Uniqueness alone is not sufficient — the constraint requires both uniqueness AND non-nullability. This makes sense: a primary key must unambiguously identify a row, and NULL (meaning 'unknown') cannot serve as a unique identifier. The database enforces this automatically when you declare a PRIMARY KEY constraint."

- question: "Without a foreign key constraint, it is possible to insert rows in a child table that reference a parent row that does not exist."
  type: true-false
  answer: true
  explanation: "Foreign key constraints are precisely what prevent this. Without the constraint, the database performs no referential check on inserts or updates — you can freely insert `order.customer_id = 999` even if customer 999 does not exist. Over time this produces orphaned records: child rows pointing to missing parents, which cause confusing query results and data integrity problems."

- question: "What is referential integrity, and what would happen to a database over time if foreign key constraints were never enforced?"
  type: short-answer
  answer: "Referential integrity means that every foreign key value in a child table corresponds to an existing primary key in the referenced parent table — no row points to a non-existent row. Without enforcement, orphaned records accumulate: orders for deleted customers, line items for nonexistent orders. Queries that join across tables return incomplete or nonsensical results, and the database can no longer be trusted as a consistent representation of real-world relationships."
  explanation: "Foreign key constraints catch integrity violations at write time — the moment of the bad insert or delete — rather than letting silent corruption propagate. This is far easier to fix than discovering orphaned records months later when a query unexpectedly returns wrong counts or missing data."
```

## Explainer

From your work with constraint enforcement, you know that a database can reject invalid data automatically. Primary keys and foreign keys are the most important specific constraints for structuring multi-table databases. A **primary key** is a column (or combination of columns) that uniquely identifies every row in a table — no two rows can share the same primary key value, and the value can never be NULL. Think of it like a social security number for each row: every row gets exactly one, and no duplicates are allowed. When you declare a primary key, the database creates a unique index behind the scenes and enforces uniqueness on every INSERT and UPDATE.

A **foreign key** is where things get relational. A foreign key in one table holds values that must match a primary key in another table, creating a link between the two. For example, an `orders` table might have a `customer_id` foreign key that references the `id` primary key in a `customers` table. This means you cannot insert an order for a customer that does not exist — the database enforces **referential integrity** by checking that every foreign key value has a corresponding primary key in the referenced table. Without this constraint, you could end up with orphaned records: orders pointing to customers who were never created or were deleted.

The power of foreign keys becomes clearer when you consider what happens during deletions and updates. If you delete a customer, what should happen to their orders? The **ON DELETE** action controls this: `RESTRICT` prevents the deletion entirely (the default, and safest), `CASCADE` automatically deletes all related orders, and `SET NULL` sets the foreign key column to NULL, breaking the link but keeping the order record. The same options exist for `ON UPDATE` when a primary key value changes. Choosing the right action depends on your domain — cascading deletes make sense for a blog post and its comments, but restricting deletes makes sense for a customer with outstanding invoices.

In practice, every table should have a primary key, and every relationship between tables should be enforced with a foreign key. When you design schemas from entity-relationship diagrams, each relationship line in the diagram becomes a foreign key in the physical schema. The discipline of declaring these constraints up front means the database catches integrity violations at write time rather than letting corrupted data silently accumulate until a query returns nonsensical results.
