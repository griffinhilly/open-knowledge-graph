---
id: primary-and-foreign-keys
title: Primary Keys and Foreign Keys
domain: computer-science
course: databases
prerequisites:
- id: relational-data-model
  type: hard
- id: entity-relationship-diagrams
  type: soft
builds-toward:
- sql-data-retrieval-select
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

## Questions

```yaml
- question: "A developer deletes a row from the Customers table for a customer who has 5 active orders in the Orders table. The Orders.customer_id column is a foreign key referencing Customers.id, with no cascade behavior configured. What happens?"
  type: multiple-choice
  options:
    - "The customer is deleted and the 5 orders are automatically deleted as well"
    - "The customer is deleted and the orders' customer_id values are set to NULL"
    - "The database rejects the deletion with a constraint violation"
    - "The customer row is marked as deleted but retained until the orders are removed"
  answer: 2
  explanation: "Without ON DELETE CASCADE or ON DELETE SET NULL, referential integrity prevents deleting a parent row that has referencing children. The database enforces this actively: the deletion is rejected with a foreign key constraint violation. This is the whole point of foreign keys — preventing orphaned records where orders reference a customer who no longer exists. The developer must either delete or reassign the orders first, or configure cascade behavior explicitly if automatic deletion is desired."

- question: "A developer proposes using users' email addresses as the primary key in the Users table since emails are unique per user. What is the primary risk of this design?"
  type: multiple-choice
  options:
    - "Email addresses are too long to be indexed efficiently by most databases"
    - "Primary keys must be integers; string values are not permitted"
    - "Email addresses can change, which would require updating every foreign key reference across all dependent tables"
    - "Email uniqueness cannot be guaranteed at the database level"
  answer: 2
  explanation: "This is the core argument for surrogate keys over natural keys: natural keys can change in the real world. When a user changes their email, every Orders.user_email, Messages.sender_email, and other foreign key column referencing that value must also be updated — or the references break. A surrogate key (auto-incrementing integer or UUID) never changes, so updating a user's email is a single-row change with no cascade of foreign key updates. The email can still be enforced as UNIQUE for lookup purposes without serving as the primary key."

- question: "A primary key should typically consist of a single column."
  type: true-false
  answer: false
  explanation: "A primary key can span multiple columns — this is called a composite key. For example, an Enrollments table relating students to courses might use a composite primary key of (student_id, course_id), where neither column is unique alone but the combination is. The requirement is that the primary key uniquely identifies each row and contains no NULLs; the number of columns is unrestricted."

- question: "A foreign key column in one table should have the same name as the primary key column it references in another table."
  type: true-false
  answer: false
  explanation: "Foreign keys only need to match the data type and value domain of the referenced primary key — the column names can be entirely different. For example, Orders.buyer_id might reference Users.id. The foreign key constraint specifies the relationship explicitly: FOREIGN KEY (buyer_id) REFERENCES Users(id). Requiring matching names would make schemas less readable and more rigid without any technical benefit."

- question: "Why is enforcing referential integrity through database constraints preferable to relying on application code to check validity?"
  type: short-answer
  answer: "Application code can be bypassed — data can be inserted or deleted through multiple interfaces (direct database access, scripts, different application versions, batch imports) that may not all run the same validation logic. Database constraints are enforced unconditionally, regardless of how data arrives. They also eliminate race conditions where two concurrent transactions might each check validity, both pass, and then both insert, leaving an inconsistent state. Constraints push correctness down to the data layer where it is universal and atomic."
  explanation: "The principle is that data integrity should be guaranteed by the layer closest to the data, not by layers above it. Application code is fragile: it can have bugs, be bypassed by maintenance scripts, or be inconsistently updated across code versions. A NOT NULL constraint, UNIQUE constraint, or foreign key constraint fires for every transaction, from every source, in every scenario — including edge cases that application developers forgot to handle. This is why database constraints are not optional decorations but structural backbone."
```

## Explainer

You already know that relations are tables with rows and columns, and that each row represents a distinct entity or fact. But a table full of rows is only useful if you can reliably tell them apart and connect them to rows in other tables. That is what keys do. A **primary key** is one or more columns whose values uniquely identify every row in a table — no two rows can share the same primary key value, and no part of it can be NULL. Think of it like a social security number for a row: it is the permanent, unambiguous address you use to find exactly one record.

Primary keys come in two flavors. A **natural key** uses data that already has meaning in the real world — an ISBN for a book, or an email address for a user. A **surrogate key** is an arbitrary value the database generates, typically an auto-incrementing integer or UUID, with no meaning outside the database. Surrogate keys are more common in practice because natural keys can change (people change emails), can be composite (making joins verbose), and sometimes do not exist at all. When a primary key spans multiple columns — say, a combination of student_id and course_id in an enrollment table — it is called a **composite key**, and the pair together must be unique even though individual columns need not be.

A **foreign key** is a column (or set of columns) in one table that stores values matching the primary key of another table. It is the mechanism that turns isolated tables into a connected data model. In an Orders table, a customer_id column that references the Customers table's primary key is a foreign key. This creates a formal link: every order must belong to an existing customer. The database enforces this through **referential integrity** — it will reject an INSERT into Orders if the customer_id does not match any row in Customers, and it will reject a DELETE from Customers if that customer still has orders, unless you have configured cascading behavior.

The practical consequence is that keys let you push data integrity enforcement down into the database itself rather than relying on application code. Without a primary key, duplicate rows could silently accumulate. Without foreign keys, you could delete a customer and leave behind orphaned orders that reference a customer who no longer exists. These constraints are not optional decorations — they are the structural backbone that makes the relational model trustworthy. When you design a schema, choosing your keys is one of the first and most consequential decisions: it determines how tables connect, how queries join, and how the database guards your data against corruption.
