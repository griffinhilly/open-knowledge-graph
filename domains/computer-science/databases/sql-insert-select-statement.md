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
status: draft
---

# INSERT...SELECT: Populating Tables from Queries

## Core Idea
INSERT...SELECT allows inserting rows derived from a SELECT query directly into a table, avoiding manual INSERT statements and enabling bulk data migration and transformation.

## How It's Best Learned
Practice inserting filtered or aggregated data from one table to another, then use with JOINs to combine data from multiple sources.

## Explainer

You already know how INSERT works for adding individual rows — `INSERT INTO orders (customer_id, amount) VALUES (42, 99.99)` — and you know how SELECT retrieves data from existing tables. **INSERT...SELECT** combines these two operations: instead of providing literal VALUES, you supply a SELECT query, and every row the query returns gets inserted into the target table. The syntax is straightforward: `INSERT INTO target_table (col1, col2) SELECT colA, colB FROM source_table WHERE condition`. There is no VALUES keyword — the SELECT replaces it entirely.

This matters because real database work constantly involves moving and transforming data between tables. Suppose you need to archive all orders older than a year into an orders_archive table, or populate a summary table with aggregated monthly totals, or create a denormalized reporting table by joining several normalized tables together. Doing this row-by-row with individual INSERT statements would be painfully slow and verbose. INSERT...SELECT handles it in a single statement, and the database engine can optimize the entire operation as one batch rather than thousands of individual inserts.

The SELECT query in an INSERT...SELECT can be as complex as any standalone query. You can filter with WHERE, aggregate with GROUP BY, join multiple tables, and even use subqueries. The only hard requirement is that the columns returned by the SELECT must match the columns listed in the INSERT clause — same number, compatible data types, correct order. For example, `INSERT INTO monthly_revenue (month, total) SELECT DATE_TRUNC('month', order_date), SUM(amount) FROM orders GROUP BY DATE_TRUNC('month', order_date)` creates summary rows from detailed transaction data in one pass. This pattern is the backbone of ETL (extract, transform, load) workflows, data migrations, and materialized reporting tables throughout production database systems.
