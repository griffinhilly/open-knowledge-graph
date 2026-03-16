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

## Explainer

You know how to write SELECT queries and join tables together. A **view** is simply a saved SELECT query that you can reference by name as though it were a table. When you write `CREATE VIEW active_customers AS SELECT id, name, email FROM customers WHERE status = 'active'`, you are not creating a new table or copying any data. You are storing the query text under the name `active_customers`. Every time someone writes `SELECT * FROM active_customers`, the database substitutes in the underlying query and executes it fresh against the current data.

This indirection provides three practical benefits. First, **simplification**: a complex multi-table join with filters can be wrapped in a view, and downstream users query a single "table" without needing to understand the join logic. Second, **security**: by granting access to a view instead of the underlying tables, you can expose only certain columns or rows. A view on the employees table that excludes salary and SSN columns lets HR assistants look up contact information without seeing compensation data. Third, **schema stability**: if the underlying table structure changes (a column is renamed, a table is split), you can update the view definition while keeping the view's interface unchanged — queries that depend on the view continue to work.

**Materialized views** are a fundamentally different tool despite the similar name. A regular view stores a query; a materialized view stores the *result* of a query. When you create a materialized view, the database executes the query and writes the output to disk, just like a table. Subsequent reads hit this pre-computed result instead of re-executing the query. This is enormously valuable for expensive aggregations — if a dashboard query joins five tables and computes monthly revenue breakdowns, a materialized view can serve that result in milliseconds. The tradeoff is staleness: the materialized view reflects the data at the time it was last refreshed, not necessarily the current state. You must explicitly refresh it (manually or on a schedule) to pick up changes.

Not all views are updatable. If you INSERT, UPDATE, or DELETE through a view, the database must be able to map those changes back to the underlying table unambiguously. Simple views over a single table with no aggregation are typically updatable. But views involving GROUP BY, DISTINCT, joins across multiple tables, or computed columns are generally read-only — the database cannot determine which base row to modify. When designing views, decide upfront whether the view is for reading only or whether it must support writes, because this constrains how you can define it.
