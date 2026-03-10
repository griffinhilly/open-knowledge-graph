---
id: primary-and-foreign-keys
title: Primary Keys and Foreign Keys
domain: computer-science
course: databases
prerequisites:
- id: relational-model-basics
  type: hard
builds-toward:
- sql-select-basics
- sql-joins
- functional-dependencies
tags:
- primary key
- foreign key
- referential integrity
- constraints
- superkey
stage: formal-systems
status: draft
---

# Primary Keys and Foreign Keys

## Core Idea
A primary key is a minimal set of attributes that uniquely identifies each tuple in a relation; no two rows may share the same primary key value, and it cannot be NULL. A foreign key is an attribute (or set of attributes) in one table that references the primary key of another, establishing a link between tables and enforcing referential integrity. Together, these constraints maintain the consistency of the relational model by preventing orphaned references and duplicate identities.

## How It's Best Learned
Create two related tables (e.g., Orders and Customers) and attempt to insert data that violates referential integrity to observe the errors. Understand the difference between natural keys (meaningful domain data) and surrogate keys (auto-generated IDs).

## Common Misconceptions
- A primary key can consist of multiple columns (composite key), not just a single column.
- A foreign key doesn't have to match the column name in the referenced table, only the data type and value domain.
- Deleting a parent row with referencing children causes a constraint violation unless ON DELETE CASCADE or SET NULL is configured.
