---
id: sql-table-creation-definition
title: 'SQL: Creating and Modifying Tables'
domain: computer-science
course: databases
prerequisites:
- id: relational-data-model
  type: hard
builds-toward:
- sql-data-retrieval-select
- sql-constraint-enforcement
- primary-key-foreign-key-constraints
tags:
- SQL
- DDL
- CREATE
- ALTER
- DROP
stage: formal-systems
status: draft
---

# SQL: Creating and Modifying Tables

## Core Idea
Data Definition Language (DDL) comprises SQL commands to create, alter, and drop tables. CREATE TABLE specifies table name, column names, data types, and constraints. ALTER TABLE modifies existing table structure. These commands define the schema that data follows.

## How It's Best Learned
Write CREATE TABLE statements for various scenarios, specifying appropriate data types (INT, VARCHAR, DATE, etc.) and constraints. Practice ALTER TABLE for adding/dropping columns and changing constraints.

## Questions

```yaml
- question: "A developer creates an `orders` table with a `price` column defined as VARCHAR(20). A query later computes AVG(price). What is the most likely problem?"
  type: multiple-choice
  options:
    - "No problem — VARCHAR can store numbers, and AVG converts them automatically"
    - "The query fails or produces incorrect results because VARCHAR columns don't support arithmetic aggregation reliably"
    - "The database automatically converts VARCHAR to NUMERIC for AVG whenever the values look like numbers"
    - "The query computes the average of the string lengths instead"
  answer: 1
  explanation: "Data types are not merely labels — they determine what operations are valid. Storing a price as VARCHAR means the database treats the values as text, not numbers. AVG on a text column will either fail, silently convert in inconsistent ways, or produce wrong results depending on the database. The right fix is declaring price as NUMERIC(10,2) at table creation. Choosing the correct data type is where schema design actively enforces correctness, not just storage."

- question: "An `orders` table needs to ensure every row references a valid customer. Which constraint enforces this?"
  type: multiple-choice
  options:
    - "UNIQUE constraint on the customer_id column in orders"
    - "CHECK constraint verifying customer_id > 0"
    - "FOREIGN KEY on customer_id referencing the primary key of the customers table"
    - "NOT NULL constraint on customer_id in orders"
  answer: 2
  explanation: "FOREIGN KEY is the constraint that links one table's column to a primary key in another table, enforcing referential integrity — the database will reject an INSERT or UPDATE that references a customer_id that doesn't exist in customers. NOT NULL only prevents the value from being absent; CHECK only validates the value against a condition; UNIQUE prevents duplicates within orders but says nothing about whether the referenced customer actually exists. Referential integrity is enforced by FOREIGN KEY, not by application code."

- question: "A PRIMARY KEY constraint on a column implies that the column is both NOT NULL and UNIQUE."
  type: true-false
  answer: true
  explanation: "PRIMARY KEY is shorthand for NOT NULL + UNIQUE, combined into a single constraint that also signals to the database that this column is the row's identifier. Databases typically create an index on the primary key automatically. This is why declaring a PRIMARY KEY is preferred over manually adding both NOT NULL and UNIQUE — it conveys intent (this is the identifier) and enables optimizations the database can leverage."

- question: "Adding a NOT NULL constraint to a column is sufficient to ensure that column's values are correct and meaningful."
  type: true-false
  answer: false
  explanation: "NOT NULL only prevents a value from being absent — it says nothing about whether the value is valid. A price column with NOT NULL can still contain -999.99 or 0, which may be nonsensical for a price. To enforce domain validity, you need additional constraints: CHECK (price > 0) to require positive prices, or a FOREIGN KEY to ensure a referenced ID actually exists. Schema design involves layering constraints — NOT NULL is a starting point, not a complete solution."

- question: "Why is it better to enforce data quality rules (e.g., non-negative prices, valid category values) as database constraints rather than only in application code?"
  type: short-answer
  answer: "Database constraints are enforced by the database engine for every operation, regardless of where data enters the system. Application code can be bypassed — through direct database access, scripts, bugs, or other applications sharing the same database. Constraints act as a last line of defense at the data layer, preventing invalid data from ever entering the store."
  explanation: "This is the key insight behind schema design: constraints are not documentation — they are active enforcers. Once a constraint like CHECK (salary > 0) or FOREIGN KEY is in place, no path into the database can violate it without an explicit error. This prevents entire categories of bugs before application code runs. Well-designed schemas with appropriate constraints and data types make systems more reliable and reduce the cost of data quality issues downstream."
```

## Explainer

From your work with the relational data model, you understand that a database organizes data into relations (tables) with defined attributes (columns) and domains (data types). **Data Definition Language (DDL)** is how you translate that conceptual model into a physical structure the database can enforce and operate on. The three core DDL commands are CREATE TABLE, ALTER TABLE, and DROP TABLE — they define, modify, and remove the containers that hold your data.

**CREATE TABLE** is where schema design becomes concrete. You specify the table name, then for each column you declare a name and a data type: `CREATE TABLE employees (id INT, name VARCHAR(100), hire_date DATE, salary NUMERIC(10,2))`. Choosing the right data type matters — VARCHAR for variable-length text, INT or BIGINT for whole numbers, NUMERIC for exact decimal values (like money), DATE or TIMESTAMP for time data. Each data type determines what values the column can store, how much space it uses, and what operations are valid on it. Storing a price as VARCHAR instead of NUMERIC means you lose the ability to do arithmetic directly and invite data quality issues.

Beyond data types, CREATE TABLE lets you declare **constraints** that the database enforces automatically. NOT NULL means a column cannot be left empty. UNIQUE ensures no two rows share the same value in that column. DEFAULT provides a fallback value when an INSERT omits the column. PRIMARY KEY combines NOT NULL and UNIQUE to uniquely identify each row. FOREIGN KEY links a column to a primary key in another table, enforcing referential integrity — you cannot insert an order referencing a customer that does not exist. CHECK constraints enforce arbitrary conditions like `CHECK (salary > 0)`. These constraints turn your table from a passive container into an active guardian of data quality.

**ALTER TABLE** modifies an existing table's structure: adding columns (`ALTER TABLE employees ADD COLUMN department VARCHAR(50)`), dropping columns, renaming columns, or changing constraints. This is how schemas evolve as requirements change — you rarely get the design perfectly right on the first try. **DROP TABLE** removes a table and all its data permanently, which is why it should be used with extreme caution. Understanding DDL is foundational because every SELECT, INSERT, UPDATE, and DELETE you will write depends on the structure these commands define. A well-designed schema with appropriate types and constraints prevents entire categories of bugs before any application code runs.
