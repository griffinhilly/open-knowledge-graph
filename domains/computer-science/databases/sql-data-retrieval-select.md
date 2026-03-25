---
id: sql-data-retrieval-select
title: 'SQL: SELECT Statement and Basic Queries'
domain: computer-science
course: databases
prerequisites:
- id: relational-data-model
  type: hard
- id: relational-algebra
  type: soft
builds-toward:
- sql-filtering-conditions
- sql-sorting-limiting-results
- sql-joins
tags:
- SQL
- SELECT
- query
- retrieval
stage: formal-systems
status: validated
---

# SQL: SELECT Statement and Basic Queries

## Core Idea
The SELECT statement is the primary SQL command for retrieving data from one or more tables. It specifies which columns to retrieve (projection) and which rows satisfy conditions (selection). SELECT statements form the basis of all data queries and reporting.

## Questions

```yaml
- question: "A table 'employees' has columns: id, name, salary, department. Which query returns only the name and salary columns for every row?"
  type: multiple-choice
  options: ["SELECT * FROM employees", "SELECT name, salary FROM employees", "SELECT employees WHERE columns = name, salary", "GET name, salary FROM employees"]
  answer: 1
  explanation: "SELECT name, salary FROM employees performs projection — it restricts which columns are returned while keeping all rows. SELECT * returns all columns. The other two options are not valid SQL syntax."

- question: "Without an ORDER BY clause, a SQL SELECT query guarantees that results are returned in the order the rows were inserted into the table."
  type: true-false
  answer: false
  explanation: "SQL makes no guarantee about row order unless ORDER BY is specified. A database engine is free to return rows in any order that is efficient (e.g., based on index scans or storage layout). Relying on insertion order without ORDER BY is a common mistake that produces unreliable results."

- question: "In relational algebra terms, what two operations does a basic SELECT ... FROM ... query perform, and how do they map to parts of the SQL syntax?"
  type: short-answer
  answer: "Projection (restricting columns) maps to the column list after SELECT; selection (restricting rows) maps to conditions in the WHERE clause. A query with no WHERE clause performs only projection."
  explanation: "This distinction comes directly from relational algebra: projection keeps certain attributes (columns) while selection keeps certain tuples (rows) matching a predicate. Understanding this mapping makes it easier to reason about what a query will return."
```

## Explainer

If you have studied the relational data model, you know that a database organizes data into tables — rows of records, each with named columns. The SELECT statement is how you ask a relational database to give you back some or all of that data. Every SQL query you will ever write starts here.

The minimal form of a SELECT is: `SELECT column1, column2 FROM table_name;`. The keyword SELECT is followed by a comma-separated list of column names you want to retrieve — this is *projection*, restricting the result to only the columns you care about. If you want every column, you can write `SELECT *`, but this is generally avoided in production code because it returns more data than needed and breaks if columns are added or reordered later. After FROM, you name the table to query. The semicolon ends the statement.

Think of the columns after SELECT as deciding *what shape* your result has (which attributes), and the rest of the query as deciding *which rows* to include. A query like `SELECT name, salary FROM employees` will return one row per employee — just those two columns — in an unspecified order. The database does not sort rows or filter them unless you add ORDER BY or WHERE clauses (topics you will study next).

One detail that surprises many beginners: SQL is declarative, not procedural. You describe *what data you want*, not *how to find it*. The database engine decides the physical execution plan — whether to scan the whole table, use an index, or fetch pages in parallel. This is what makes SQL so powerful: you express the intent, and the engine optimizes the execution.

A crucial point from the relational model: the result of a SELECT is itself a table — a new set of rows and columns produced by the query. This is called a *derived relation*, and it means you can use query results as inputs to other queries (subqueries), or reason about them with the same relational algebra tools you used to understand tables in the first place.
