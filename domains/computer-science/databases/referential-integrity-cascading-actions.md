---
id: referential-integrity-cascading-actions
title: Referential Integrity and Cascading Delete/Update Actions
domain: computer-science
course: databases
prerequisites:
- id: primary-key-foreign-key-constraints
  type: hard
- id: sql-constraint-types-domain-check
  type: hard
builds-toward:
- database-schema-design
- sql-constraint-enforcement
tags:
- referential-integrity
- foreign-keys
- cascading
- actions
stage: formal-systems
status: draft
---

# Referential Integrity and Cascading Delete/Update Actions

## Core Idea
Referential integrity ensures that foreign key values correspond to existing primary key values in referenced tables. Cascading actions define what happens when referenced rows are modified: CASCADE automatically updates/deletes dependent rows, SET NULL sets foreign keys to null, SET DEFAULT uses default values, and RESTRICT prevents the operation if dependent rows exist. Choosing the right action prevents orphaned records and maintains consistency.

## Explainer

You already know that foreign keys link rows in one table to rows in another, creating relationships that mirror real-world connections — an order belongs to a customer, a comment belongs to a post. **Referential integrity** is the guarantee that these links never point to nothing. If a foreign key in the `orders` table references `customer_id = 42`, then a row with `id = 42` must actually exist in the `customers` table. The database enforces this on every INSERT and UPDATE that touches a foreign key column, rejecting any operation that would create a dangling reference.

The interesting question is what happens when you go the other direction: what if you try to DELETE customer 42, who has 15 orders? Or UPDATE their primary key? This is where **cascading actions** come in. When you define a foreign key constraint, you specify an `ON DELETE` and `ON UPDATE` action that tells the database how to handle modifications to the referenced row. The options form a spectrum from most automatic to most restrictive.

**CASCADE** is the most aggressive option: deleting customer 42 automatically deletes all 15 of their orders. Updating the customer's primary key automatically updates the foreign key in every related order. This is convenient but dangerous — a single DELETE can ripple through many tables, removing far more data than you might expect. **SET NULL** takes a gentler approach: instead of deleting the orders, it sets their `customer_id` to NULL, effectively orphaning them in a controlled way. This works well when the child rows have independent value — you might want to keep order records even after removing a customer. **SET DEFAULT** works similarly but uses a predefined default value instead of NULL. **RESTRICT** (and its close cousin NO ACTION) is the safest choice: it simply blocks the DELETE or UPDATE if any dependent rows exist, forcing you to deal with the children first.

Choosing the right action depends on the relationship's semantics. For composition relationships where children have no meaning without their parent (like line items on an order), CASCADE makes sense — delete the order, delete its items. For association relationships where both sides have independent existence (like students enrolled in courses), RESTRICT or SET NULL is usually safer. A common mistake is applying CASCADE everywhere for convenience, then discovering that deleting one row triggers a chain reaction across half the database. The safest practice is to default to RESTRICT, switching to CASCADE only when you can articulate why automatic deletion is the correct business behavior.
