---
id: sql-views
title: SQL Views and Materialized Views
domain: computer-science
course: databases
prerequisites:
- id: sql-select-basics
  type: hard
- id: sql-joins
  type: soft
builds-toward:
- database-security
- query-optimization
tags:
- SQL
- views
- materialized views
- virtual tables
- abstraction
stage: formal-systems
status: validated
---

# SQL Views and Materialized Views

## Core Idea
A view is a named, stored SQL query that appears to users as a virtual table — querying a view executes the underlying SELECT each time without storing data. Views simplify complex queries, enforce security by exposing only certain columns or rows, and provide a stable interface when the underlying schema changes. Materialized views physically store the query result and must be refreshed periodically; they trade freshness for dramatically faster reads on expensive aggregations or joins.

## How It's Best Learned
Create a view over a multi-table join, then query it as if it were a plain table. Experiment with updatable vs. non-updatable views. Compare query execution time between a complex query run directly vs. through a materialized view with pre-computed aggregates.

## Common Misconceptions
- Regular views don't store data — they are saved queries. Only materialized views physically persist results.
- Views are not always updatable; views with GROUP BY, DISTINCT, or multi-table joins may be read-only.
- Views do not automatically improve query performance; the query still executes on each access unless materialized.
