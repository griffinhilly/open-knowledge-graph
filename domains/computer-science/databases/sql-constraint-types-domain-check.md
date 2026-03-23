---
id: sql-constraint-types-domain-check
title: 'Constraint Types: Domain, Check, Unique, and Key Constraints'
domain: computer-science
course: databases
prerequisites:
- id: sql-table-creation-definition
  type: hard
builds-toward:
- referential-integrity-cascading-actions
- sql-constraint-enforcement
tags:
- constraints
- integrity
- domain
- check
- unique
stage: formal-systems
status: validated
---

# Constraint Types: Domain, Check, Unique, and Key Constraints

## Core Idea
Databases support multiple constraint types to maintain data integrity: domain constraints restrict column values to appropriate types and ranges, check constraints enforce logical conditions on column values, unique constraints prevent duplicate non-null values, and key constraints uniquely identify rows. The DBMS automatically enforces these constraints, rejecting invalid data before it enters the database.

## Questions

```yaml
- question: "A web application validates all user input before inserting it into the database, enforcing rules like 'age must be positive' in application code. A data engineer then runs a bulk CSV import directly against the database, bypassing the application. What happens to data integrity?"
  type: multiple-choice
  options:
    - "The database enforces the same rules because it inherits application logic"
    - "Application-level validation is sufficient; any data already in the database was clean when inserted"
    - "Invalid data can enter the database because application code is bypassed; only database constraints would catch this"
    - "The database automatically rejects any INSERT that does not go through the application layer"
  answer: 2
  explanation: "Application-level validation only runs when data enters through that specific application. Any other access path — bulk import, manual SQL session, a future API — bypasses it entirely. Database constraints (CHECK, UNIQUE, NOT NULL, etc.) are enforced by the DBMS on every INSERT and UPDATE, regardless of how the data arrives. This is the central argument for declarative integrity: state the rules in the schema once, and they hold universally."

- question: "A users table needs an email column that must be unique when present, but is allowed to be absent (NULL) for some users. Which constraint is appropriate?"
  type: multiple-choice
  options:
    - "PRIMARY KEY — ensures uniqueness and non-null presence"
    - "UNIQUE — prevents duplicate non-null values but permits multiple NULLs"
    - "CHECK (email IS UNIQUE) — enforces uniqueness as a boolean condition"
    - "NOT NULL plus CHECK — the only combination that allows uniqueness with optional values"
  answer: 1
  explanation: "A UNIQUE constraint prevents two rows from sharing the same non-null value, but it allows multiple rows to have NULL in that column (since NULL is not equal to anything, including another NULL). A PRIMARY KEY would also enforce uniqueness but additionally requires NOT NULL — disqualifying it here since the column is optional. Option C is invalid SQL syntax. Option D contradicts the requirement since NOT NULL would prevent the column from being absent."

- question: "A UNIQUE constraint and a PRIMARY KEY constraint both prevent duplicate values AND both prevent NULL values in the constrained column."
  type: true-false
  answer: false
  explanation: "A PRIMARY KEY is a UNIQUE constraint plus NOT NULL — it prevents both duplicates and nulls. A UNIQUE constraint prevents duplicate non-null values but explicitly allows NULLs, and multiple NULLs are permitted since NULL ≠ NULL in SQL. This distinction matters in practice: columns like 'email' or 'phone_number' that should be unique when present but optional make natural UNIQUE (not PRIMARY KEY) candidates."

- question: "A CHECK constraint can reference and compare multiple columns within the same row, not just the value of a single column."
  type: true-false
  answer: true
  explanation: "CHECK constraints accept any boolean SQL expression, which can span multiple columns. Classic examples include CHECK(end_date > start_date), CHECK(min_salary <= max_salary), or CHECK(discount < price). This makes CHECK constraints more powerful than simple domain restrictions — they can enforce cross-column logical relationships that are impossible to express as a single-column type constraint."

- question: "Why is enforcing data integrity through database constraints preferable to enforcing it exclusively through application code?"
  type: short-answer
  answer: "Application code only runs when data enters through that specific application. Any other access path — a different application, a bulk import script, a direct SQL session, a future service — bypasses it. Database constraints are enforced by the DBMS engine on every INSERT and UPDATE, regardless of origin. This is declarative integrity: rules are stated once in the schema and hold universally. It also means downstream queries and systems can trust the data without re-validating it."
  explanation: "A common counter-argument is that handling constraint violations at the database layer produces errors that applications must catch. This is true, but the benefit — guaranteed data validity — outweighs the cost. The alternative, relying solely on application code, creates a fragile system where the database's correctness depends on every access path implementing the same rules correctly. Schemas outlive individual applications; constraints protect the data's integrity across the full lifetime of the system."
```

## Explainer

When you created tables with `CREATE TABLE`, you chose data types for each column — `INTEGER`, `VARCHAR(100)`, `DATE`, and so on. Data types are the first layer of constraint: they guarantee a column holds the right kind of value. But types alone are not enough. A column declared as `INTEGER` will happily accept -999 for an age or 0 for a quantity that should always be positive. Constraints let you tighten the rules beyond what the type system provides, pushing data validation into the database itself rather than relying on application code to always get it right.

**Domain constraints** restrict a column to a named set of legal values or a specific subtype. In SQL, you can define a domain with `CREATE DOMAIN` — for example, `CREATE DOMAIN positive_int AS INTEGER CHECK (VALUE > 0)` — and then use that domain as a column type. This is especially useful when multiple tables share the same validation rule. **Check constraints** are more flexible: they attach a boolean expression directly to a column or table, and the database rejects any row where the expression evaluates to false. For example, `CHECK (end_date > start_date)` on a table ensures temporal consistency, while `CHECK (status IN ('active', 'inactive', 'suspended'))` limits a column to an enumerated set of values.

**Unique constraints** ensure that no two rows share the same value in a column (or combination of columns), but unlike primary keys, they allow NULL values — and multiple NULLs at that, since NULL is not equal to anything, including itself. A common use case is an `email` column that must be unique across all users but is optional. **Key constraints** are the strongest form: a primary key is a unique constraint plus a NOT NULL constraint, guaranteeing that every row has a distinct, non-missing identifier.

The important insight is that constraints move validation logic from your application into the database engine, where it is enforced universally. No matter how data enters the table — through your web application, a bulk import script, a manual SQL session, or a future application you have not written yet — the constraints hold. This is declarative integrity: you state the rules once, and the DBMS enforces them on every INSERT and UPDATE. The cost is that constraint violations produce errors your application must handle, but the benefit is that your data is always in a valid state, which makes every query and every downstream system more trustworthy.
