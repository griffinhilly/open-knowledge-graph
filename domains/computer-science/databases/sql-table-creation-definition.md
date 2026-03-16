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

## Explainer

From your work with the relational data model, you understand that a database organizes data into relations (tables) with defined attributes (columns) and domains (data types). **Data Definition Language (DDL)** is how you translate that conceptual model into a physical structure the database can enforce and operate on. The three core DDL commands are CREATE TABLE, ALTER TABLE, and DROP TABLE — they define, modify, and remove the containers that hold your data.

**CREATE TABLE** is where schema design becomes concrete. You specify the table name, then for each column you declare a name and a data type: `CREATE TABLE employees (id INT, name VARCHAR(100), hire_date DATE, salary NUMERIC(10,2))`. Choosing the right data type matters — VARCHAR for variable-length text, INT or BIGINT for whole numbers, NUMERIC for exact decimal values (like money), DATE or TIMESTAMP for time data. Each data type determines what values the column can store, how much space it uses, and what operations are valid on it. Storing a price as VARCHAR instead of NUMERIC means you lose the ability to do arithmetic directly and invite data quality issues.

Beyond data types, CREATE TABLE lets you declare **constraints** that the database enforces automatically. NOT NULL means a column cannot be left empty. UNIQUE ensures no two rows share the same value in that column. DEFAULT provides a fallback value when an INSERT omits the column. PRIMARY KEY combines NOT NULL and UNIQUE to uniquely identify each row. FOREIGN KEY links a column to a primary key in another table, enforcing referential integrity — you cannot insert an order referencing a customer that does not exist. CHECK constraints enforce arbitrary conditions like `CHECK (salary > 0)`. These constraints turn your table from a passive container into an active guardian of data quality.

**ALTER TABLE** modifies an existing table's structure: adding columns (`ALTER TABLE employees ADD COLUMN department VARCHAR(50)`), dropping columns, renaming columns, or changing constraints. This is how schemas evolve as requirements change — you rarely get the design perfectly right on the first try. **DROP TABLE** removes a table and all its data permanently, which is why it should be used with extreme caution. Understanding DDL is foundational because every SELECT, INSERT, UPDATE, and DELETE you will write depends on the structure these commands define. A well-designed schema with appropriate types and constraints prevents entire categories of bugs before any application code runs.
