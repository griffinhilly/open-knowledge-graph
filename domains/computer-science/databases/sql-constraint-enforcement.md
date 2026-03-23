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
status: validated
---

# SQL: Constraints (PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK, DEFAULT)

## Core Idea
Constraints enforce data integrity rules at the database level. PRIMARY KEY uniquely identifies rows. FOREIGN KEY enforces relationships between tables. UNIQUE prevents duplicate values. CHECK enforces domain constraints. DEFAULT assigns automatic values. Constraints prevent invalid data at the point of entry.

## How It's Best Learned
Design schemas with appropriate constraints, understand how constraints prevent invalid operations, and practice handling constraint violations in INSERT/UPDATE statements.

## Questions

```yaml
- question: "A web application validates that a user's age is ≥ 18 in its Python code before inserting into the database, but no CHECK constraint exists on the column. A data analyst runs a direct SQL INSERT through a terminal session. What happens?"
  type: multiple-choice
  options:
    - "The Python validation runs automatically for all database connections, including direct SQL sessions"
    - "The INTEGER column type rejects negative or out-of-range ages automatically"
    - "The analyst can insert any age value, including negative numbers, because no database constraint prevents it"
    - "The FOREIGN KEY constraint on a related table prevents the invalid age from being inserted"
  answer: 2
  explanation: "Application-level validation only runs when code passes through the application layer. A direct SQL session, a migration script, a bug in a different application, or any other client bypasses the Python code entirely. The database will happily accept whatever value is sent. Only a CHECK constraint enforced by the database itself is unconditional — it applies to every INSERT, UPDATE, and DELETE from every client. This is the core reason to move business rules into the schema: constraints cannot be bypassed."

- question: "Which statement best describes the difference between UNIQUE and PRIMARY KEY constraints?"
  type: multiple-choice
  options:
    - "PRIMARY KEY allows NULLs to accommodate missing identifiers; UNIQUE does not"
    - "UNIQUE ensures no two rows share the same value but permits NULLs; PRIMARY KEY requires NOT NULL and uniquely identifies every row"
    - "They are functionally identical — PRIMARY KEY is simply a conventional label for the main UNIQUE constraint"
    - "PRIMARY KEY only applies to single-column constraints; UNIQUE is used for multi-column uniqueness"
  answer: 1
  explanation: "PRIMARY KEY combines two requirements: uniqueness and NOT NULL. Every row must have a non-null, unique identifier. UNIQUE enforces uniqueness without requiring NOT NULL — a column like email can be UNIQUE while still allowing rows where the email is not yet known (NULL). Most databases also allow multiple NULLs under a UNIQUE constraint because NULL represents 'unknown' and two unknowns are not considered equal. Options A and C are both incorrect about the NULL behavior of PRIMARY KEY."

- question: "A FOREIGN KEY constraint prevents inserting a row whose foreign key value has no matching primary key in the referenced table."
  type: true-false
  answer: true
  explanation: "This is the definition of referential integrity as enforced by FOREIGN KEY. If a table orders has a FOREIGN KEY (customer_id) REFERENCES customers(id), the database rejects any INSERT or UPDATE that would create an orders row with a customer_id that doesn't exist in the customers table. This prevents 'orphaned' records — data that references something that doesn't exist. The constraint is checked at the time of every modification, by every client, unconditionally."

- question: "A CHECK constraint defined in the database schema is redundant if the application layer already validates the same rule, because the data will be validated before it reaches the database."
  type: true-false
  answer: false
  explanation: "Application-layer validation can be bypassed — by a different application accessing the same database, by a direct SQL session from an analyst or DBA, by a migration script, or by a bug that lets invalid data slip through. Database constraints are enforced unconditionally on every statement from every client. The schema is a contract that the database upholds regardless of how data arrives. The correct conclusion is the opposite: if a rule is important enough to enforce in the application, it is important enough to enforce in the schema as well."

- question: "Why is it better to enforce business rules like 'age must be positive' and 'email must be unique' as database constraints rather than relying solely on application code?"
  type: short-answer
  answer: "Database constraints are enforced unconditionally on every INSERT, UPDATE, and DELETE from every client — including direct SQL sessions, multiple applications, migration scripts, and future code that doesn't know the rule exists. Application code can be bypassed, updated incorrectly, or forgotten. By encoding business rules as constraints, the schema becomes a self-enforcing contract: invalid data cannot enter the database regardless of how it is submitted. This makes the data trustworthy by construction rather than by hope."
  explanation: "The deeper point is that data outlives applications. A business might replace its web app, hire a new analyst, or run automated jobs — all of which interact with the same database. If the rules live only in one application, every new access point must independently re-implement them correctly. Constraints in the schema need to be written once and are then permanent. This is why the topic describes the schema as 'a contract the database enforces.'"
```

## Explainer

When you created tables with CREATE TABLE, you defined column names and data types — but data types alone cannot express the rules your data must follow. A column declared as INTEGER will reject the string "hello," but it will happily accept -5 for an age or NULL for a required field. **Constraints** are the mechanism for encoding business rules directly into the schema so the database itself rejects invalid data, regardless of which application or user attempts the insertion.

The most fundamental constraint is **PRIMARY KEY**, which you already understand conceptually: it guarantees that every row has a unique, non-NULL identifier. In SQL, declaring `PRIMARY KEY (id)` on a table automatically enforces both uniqueness and the NOT NULL requirement on that column. **FOREIGN KEY** enforces referential integrity — it declares that values in one column must match existing values in another table's primary key. If you add `FOREIGN KEY (customer_id) REFERENCES customers(id)`, the database will reject any insert or update that would create an orphaned reference. You can also specify what happens when the referenced row is deleted: `ON DELETE CASCADE` removes the child rows automatically, while `ON DELETE SET NULL` nullifies the reference.

**UNIQUE** is like a primary key without the NOT NULL requirement — it ensures no two rows share the same value in that column, but allows NULLs (and in most databases, multiple NULLs). This is useful for columns like email addresses that should be distinct but might not serve as the primary key. **CHECK** constraints enforce arbitrary boolean conditions: `CHECK (age >= 0)` prevents negative ages, `CHECK (status IN ('active', 'inactive'))` restricts a column to an enumerated set of values. **DEFAULT** is not a validation constraint in the same sense — it provides a fallback value when an INSERT omits the column, such as `DEFAULT CURRENT_TIMESTAMP` for a created_at column.

The critical insight is that constraints move data validation from application code into the database engine. Application-level validation can be bypassed — by a different application, a manual SQL session, or a bug. Constraints cannot. They are enforced on every INSERT, UPDATE, and DELETE, by every client, unconditionally. When a constraint is violated, the database rejects the entire statement and returns an error. This means you should design your constraints to match your actual business rules as closely as possible: if an order quantity must be positive, say so with CHECK. If an email must be unique, say so with UNIQUE. The schema becomes a contract that the database enforces, making your data trustworthy by construction rather than by hope.
