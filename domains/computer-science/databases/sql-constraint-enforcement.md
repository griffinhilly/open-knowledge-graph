---
id: sql-constraint-enforcement
title: 'SQL: Constraints (PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK, DEFAULT)'
domain: computer-science
course: databases
prerequisites:
- id: sql-table-creation-definition
  type: hard
builds-toward:
- primary-key-foreign-key-constraints
- functional-dependency-schema
tags:
- SQL
- constraint
- integrity
- validation
stage: formal-systems
status: draft
---

# SQL: Constraints (PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK, DEFAULT)

## Core Idea
Constraints enforce data integrity rules at the database level. PRIMARY KEY uniquely identifies rows. FOREIGN KEY enforces relationships between tables. UNIQUE prevents duplicate values. CHECK enforces domain constraints. DEFAULT assigns automatic values. Constraints prevent invalid data at the point of entry.

## How It's Best Learned
Design schemas with appropriate constraints, understand how constraints prevent invalid operations, and practice handling constraint violations in INSERT/UPDATE statements.

## Explainer

When you created tables with CREATE TABLE, you defined column names and data types — but data types alone cannot express the rules your data must follow. A column declared as INTEGER will reject the string "hello," but it will happily accept -5 for an age or NULL for a required field. **Constraints** are the mechanism for encoding business rules directly into the schema so the database itself rejects invalid data, regardless of which application or user attempts the insertion.

The most fundamental constraint is **PRIMARY KEY**, which you already understand conceptually: it guarantees that every row has a unique, non-NULL identifier. In SQL, declaring `PRIMARY KEY (id)` on a table automatically enforces both uniqueness and the NOT NULL requirement on that column. **FOREIGN KEY** enforces referential integrity — it declares that values in one column must match existing values in another table's primary key. If you add `FOREIGN KEY (customer_id) REFERENCES customers(id)`, the database will reject any insert or update that would create an orphaned reference. You can also specify what happens when the referenced row is deleted: `ON DELETE CASCADE` removes the child rows automatically, while `ON DELETE SET NULL` nullifies the reference.

**UNIQUE** is like a primary key without the NOT NULL requirement — it ensures no two rows share the same value in that column, but allows NULLs (and in most databases, multiple NULLs). This is useful for columns like email addresses that should be distinct but might not serve as the primary key. **CHECK** constraints enforce arbitrary boolean conditions: `CHECK (age >= 0)` prevents negative ages, `CHECK (status IN ('active', 'inactive'))` restricts a column to an enumerated set of values. **DEFAULT** is not a validation constraint in the same sense — it provides a fallback value when an INSERT omits the column, such as `DEFAULT CURRENT_TIMESTAMP` for a created_at column.

The critical insight is that constraints move data validation from application code into the database engine. Application-level validation can be bypassed — by a different application, a manual SQL session, or a bug. Constraints cannot. They are enforced on every INSERT, UPDATE, and DELETE, by every client, unconditionally. When a constraint is violated, the database rejects the entire statement and returns an error. This means you should design your constraints to match your actual business rules as closely as possible: if an order quantity must be positive, say so with CHECK. If an email must be unique, say so with UNIQUE. The schema becomes a contract that the database enforces, making your data trustworthy by construction rather than by hope.
