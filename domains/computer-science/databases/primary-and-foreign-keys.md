---
id: primary-and-foreign-keys
title: Primary Keys and Foreign Keys
domain: computer-science
course: databases
prerequisites:
- id: relational-model-basics
  type: hard
- id: entity-relationship-diagrams
  type: soft
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
status: validated
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

## Explainer

You already know that relations are tables with rows and columns, and that each row represents a distinct entity or fact. But a table full of rows is only useful if you can reliably tell them apart and connect them to rows in other tables. That is what keys do. A **primary key** is one or more columns whose values uniquely identify every row in a table — no two rows can share the same primary key value, and no part of it can be NULL. Think of it like a social security number for a row: it is the permanent, unambiguous address you use to find exactly one record.

Primary keys come in two flavors. A **natural key** uses data that already has meaning in the real world — an ISBN for a book, or an email address for a user. A **surrogate key** is an arbitrary value the database generates, typically an auto-incrementing integer or UUID, with no meaning outside the database. Surrogate keys are more common in practice because natural keys can change (people change emails), can be composite (making joins verbose), and sometimes do not exist at all. When a primary key spans multiple columns — say, a combination of student_id and course_id in an enrollment table — it is called a **composite key**, and the pair together must be unique even though individual columns need not be.

A **foreign key** is a column (or set of columns) in one table that stores values matching the primary key of another table. It is the mechanism that turns isolated tables into a connected data model. In an Orders table, a customer_id column that references the Customers table's primary key is a foreign key. This creates a formal link: every order must belong to an existing customer. The database enforces this through **referential integrity** — it will reject an INSERT into Orders if the customer_id does not match any row in Customers, and it will reject a DELETE from Customers if that customer still has orders, unless you have configured cascading behavior.

The practical consequence is that keys let you push data integrity enforcement down into the database itself rather than relying on application code. Without a primary key, duplicate rows could silently accumulate. Without foreign keys, you could delete a customer and leave behind orphaned orders that reference a customer who no longer exists. These constraints are not optional decorations — they are the structural backbone that makes the relational model trustworthy. When you design a schema, choosing your keys is one of the first and most consequential decisions: it determines how tables connect, how queries join, and how the database guards your data against corruption.
