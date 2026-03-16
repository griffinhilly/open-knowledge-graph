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
status: draft
---

# Constraint Types: Domain, Check, Unique, and Key Constraints

## Core Idea
Databases support multiple constraint types to maintain data integrity: domain constraints restrict column values to appropriate types and ranges, check constraints enforce logical conditions on column values, unique constraints prevent duplicate non-null values, and key constraints uniquely identify rows. The DBMS automatically enforces these constraints, rejecting invalid data before it enters the database.

## Explainer

When you created tables with `CREATE TABLE`, you chose data types for each column — `INTEGER`, `VARCHAR(100)`, `DATE`, and so on. Data types are the first layer of constraint: they guarantee a column holds the right kind of value. But types alone are not enough. A column declared as `INTEGER` will happily accept -999 for an age or 0 for a quantity that should always be positive. Constraints let you tighten the rules beyond what the type system provides, pushing data validation into the database itself rather than relying on application code to always get it right.

**Domain constraints** restrict a column to a named set of legal values or a specific subtype. In SQL, you can define a domain with `CREATE DOMAIN` — for example, `CREATE DOMAIN positive_int AS INTEGER CHECK (VALUE > 0)` — and then use that domain as a column type. This is especially useful when multiple tables share the same validation rule. **Check constraints** are more flexible: they attach a boolean expression directly to a column or table, and the database rejects any row where the expression evaluates to false. For example, `CHECK (end_date > start_date)` on a table ensures temporal consistency, while `CHECK (status IN ('active', 'inactive', 'suspended'))` limits a column to an enumerated set of values.

**Unique constraints** ensure that no two rows share the same value in a column (or combination of columns), but unlike primary keys, they allow NULL values — and multiple NULLs at that, since NULL is not equal to anything, including itself. A common use case is an `email` column that must be unique across all users but is optional. **Key constraints** are the strongest form: a primary key is a unique constraint plus a NOT NULL constraint, guaranteeing that every row has a distinct, non-missing identifier.

The important insight is that constraints move validation logic from your application into the database engine, where it is enforced universally. No matter how data enters the table — through your web application, a bulk import script, a manual SQL session, or a future application you have not written yet — the constraints hold. This is declarative integrity: you state the rules once, and the DBMS enforces them on every INSERT and UPDATE. The cost is that constraint violations produce errors your application must handle, but the benefit is that your data is always in a valid state, which makes every query and every downstream system more trustworthy.
