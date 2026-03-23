---
id: sql-insert-select-statement
title: 'INSERT...SELECT: Populating Tables from Queries'
domain: computer-science
course: databases
prerequisites:
- id: sql-table-creation-definition
  type: hard
- id: sql-data-retrieval-select
  type: hard
builds-toward:
- sql-bulk-insert-operations
tags:
- sql
- dml
- data-loading
stage: formal-systems
status: validated
---

# INSERT...SELECT: Populating Tables from Queries

## Core Idea
INSERT...SELECT allows inserting rows derived from a SELECT query directly into a table, avoiding manual INSERT statements and enabling bulk data migration and transformation.

## How It's Best Learned
Practice inserting filtered or aggregated data from one table to another, then use with JOINs to combine data from multiple sources.

## Questions

```yaml
- question: "You want to populate a monthly_revenue table with one row per month containing the total order amount for that month, using data from an orders table. Which SQL approach correctly does this in a single statement?"
  type: multiple-choice
  options:
    - "INSERT INTO monthly_revenue VALUES (SELECT month, SUM(amount) FROM orders GROUP BY month)"
    - "INSERT INTO monthly_revenue (month, total) SELECT DATE_TRUNC('month', order_date), SUM(amount) FROM orders GROUP BY DATE_TRUNC('month', order_date)"
    - "INSERT INTO monthly_revenue (month, total) VALUES (month, SUM(amount)) FROM orders GROUP BY month"
    - "SELECT month, SUM(amount) INTO monthly_revenue FROM orders GROUP BY month"
  answer: 1
  explanation: "INSERT...SELECT replaces the VALUES clause entirely with a SELECT statement. The SELECT can include aggregation (SUM), grouping (GROUP BY), date functions, and anything else a standalone SELECT supports. Option A incorrectly places SELECT inside VALUES. Option C wrongly mixes VALUES syntax with FROM. Option D uses SELECT INTO syntax (a different operation that creates a new table). The columns returned by the SELECT must match the columns listed in the INSERT clause in number and type."

- question: "In an INSERT...SELECT statement, what replaces the VALUES keyword?"
  type: multiple-choice
  options:
    - "A FROM clause that specifies the source table"
    - "A SELECT statement that returns the rows to be inserted"
    - "A RETURNING clause that redirects query output to the target table"
    - "Both VALUES and SELECT are required — VALUES for schema and SELECT for data"
  answer: 1
  explanation: "In INSERT...SELECT, the SELECT statement completely replaces the VALUES clause. The syntax is: INSERT INTO target (col1, col2) SELECT expr1, expr2 FROM source WHERE ..., with no VALUES keyword at all. The SELECT query can be arbitrarily complex — it can join tables, filter rows, aggregate data, and use subqueries. Every row the SELECT returns becomes a new row in the target table. No other clause mediates between the SELECT and the INSERT."

- question: "In an INSERT...SELECT statement, the SELECT query can include GROUP BY clauses, JOIN operations, and aggregate functions like SUM or COUNT."
  type: true-false
  answer: true
  explanation: "The SELECT in INSERT...SELECT is a full SQL SELECT statement with no restrictions on its complexity. You can aggregate data (GROUP BY + SUM/COUNT/AVG), join multiple source tables, filter with WHERE or HAVING, use subqueries, apply window functions, and more. The only constraint is structural: the SELECT's output columns must match the INSERT's target columns in number and data type. This flexibility is exactly why INSERT...SELECT is powerful — it can transform and combine data in one pass."

- question: "An INSERT...SELECT statement requires both a VALUES clause (to specify column types) and a SELECT clause (to provide the actual data)."
  type: true-false
  answer: false
  explanation: "INSERT...SELECT uses NO VALUES clause — the SELECT completely replaces it. This is a fundamental distinction from regular INSERT...VALUES statements. Mixing both syntaxes is a SQL error. The SELECT alone determines both the structure (number and types of returned columns) and the data (the actual rows) that get inserted. Trying to combine them would be like writing INSERT INTO t (a, b) VALUES SELECT a, b FROM s — which is invalid syntax."

- question: "Why is INSERT...SELECT preferred over writing individual INSERT statements when migrating or transforming data between tables?"
  type: short-answer
  answer: "INSERT...SELECT performs the entire operation as a single database statement, letting the query engine optimize the batch operation as a whole. Individual INSERT statements require a round-trip per row — thousands of rows mean thousands of statements, which is slow due to parsing overhead, transaction cost per statement, and network latency in client-server setups. INSERT...SELECT also allows complex transformations (joins, aggregations) to happen in the database layer rather than in application code, reducing data transfer and exploiting the database's optimized execution plans."
  explanation: "This is the core ETL (extract-transform-load) pattern in SQL. Consider archiving a million old orders: with individual INSERTs you'd write a million statements; with INSERT...SELECT you write one. The performance difference is often orders of magnitude. The database can also apply set-based optimizations — parallel execution, bulk loading paths, buffer management — that aren't available for row-by-row inserts. For data migration, reporting tables, and aggregated summaries, INSERT...SELECT is the idiomatic SQL approach."
```

## Explainer

You already know how INSERT works for adding individual rows — `INSERT INTO orders (customer_id, amount) VALUES (42, 99.99)` — and you know how SELECT retrieves data from existing tables. **INSERT...SELECT** combines these two operations: instead of providing literal VALUES, you supply a SELECT query, and every row the query returns gets inserted into the target table. The syntax is straightforward: `INSERT INTO target_table (col1, col2) SELECT colA, colB FROM source_table WHERE condition`. There is no VALUES keyword — the SELECT replaces it entirely.

This matters because real database work constantly involves moving and transforming data between tables. Suppose you need to archive all orders older than a year into an orders_archive table, or populate a summary table with aggregated monthly totals, or create a denormalized reporting table by joining several normalized tables together. Doing this row-by-row with individual INSERT statements would be painfully slow and verbose. INSERT...SELECT handles it in a single statement, and the database engine can optimize the entire operation as one batch rather than thousands of individual inserts.

The SELECT query in an INSERT...SELECT can be as complex as any standalone query. You can filter with WHERE, aggregate with GROUP BY, join multiple tables, and even use subqueries. The only hard requirement is that the columns returned by the SELECT must match the columns listed in the INSERT clause — same number, compatible data types, correct order. For example, `INSERT INTO monthly_revenue (month, total) SELECT DATE_TRUNC('month', order_date), SUM(amount) FROM orders GROUP BY DATE_TRUNC('month', order_date)` creates summary rows from detailed transaction data in one pass. This pattern is the backbone of ETL (extract, transform, load) workflows, data migrations, and materialized reporting tables throughout production database systems.
