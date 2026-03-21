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

## Questions

```yaml
- question: "A DBA creates a view called monthly_sales_summary that joins five large tables and computes SUM and COUNT aggregations. A dashboard queries this view every 5 minutes. What performance problem should the DBA anticipate?"
  type: multiple-choice
  options:
    - "None — views automatically cache their results, so repeated queries are fast"
    - "The view's JOIN and aggregation logic executes fresh on every query, potentially making each dashboard refresh expensive"
    - "The view will accumulate stale data over time, gradually degrading read performance"
    - "Views containing GROUP BY are invalid SQL and this definition will fail"
  answer: 1
  explanation: "A regular SQL view stores only the query definition — no data. Every time a client queries the view, the database substitutes in the underlying SELECT and executes it from scratch against the current base tables. For expensive joins and aggregations across large tables, this means each dashboard refresh triggers the full computation. The solution is a materialized view, which stores the pre-computed result and serves reads instantly — at the cost of possible staleness."

- question: "A company grants employees SELECT access to an employee_directory view (showing name, email, department) but not to the underlying employees table (which also contains salary and SSN). An employee runs SELECT * FROM employee_directory. What does the database actually do?"
  type: multiple-choice
  options:
    - "Returns a pre-stored snapshot of the permitted columns from the last time the view was refreshed"
    - "Executes the view's underlying SELECT query against the current employees table, returning only the columns the view exposes"
    - "Raises an error because employees lack direct table access, making the query impossible"
    - "Prompts the DBA to approve the access before returning results"
  answer: 1
  explanation: "The database substitutes the view's query definition and executes it. Because the view's SELECT only references name, email, and department, the employee sees only those columns — even though the underlying table contains salary and SSN. The database enforces permissions at the view boundary: the employee never directly accesses the base table. This is the security use case for views: exposing a safe, limited interface over sensitive data."

- question: "A regular SQL view improves query performance because the database pre-computes and stores the view's result on disk, making subsequent reads faster."
  type: true-false
  answer: false
  explanation: "Regular (non-materialized) views store the query definition only — zero rows of data are persisted. Each access re-executes the full underlying SELECT. There is no performance advantage from the view itself. Only materialized views physically store results on disk and serve pre-computed data. A common misconception is that creating a view is like caching a result; it is not — it is just giving a name to a query."

- question: "A SQL view can enforce security by limiting which columns or rows a user can see, even when the user has no direct access to the underlying table."
  type: true-false
  answer: true
  explanation: "Views are a standard database security mechanism. By granting SELECT on a view (not the underlying table), you control exactly what data is visible. A view over employees that excludes salary and SSN, or filters WHERE department = 'HR', lets you expose exactly the right data to the right users. When the user queries the view, the database executes the underlying query transparently — the user sees only what the view's SELECT specifies."

- question: "Explain the key difference between a regular view and a materialized view in terms of what is stored, and describe the tradeoff this creates."
  type: short-answer
  answer: "A regular view stores only the SQL query text — no data. Every query re-executes the SELECT from scratch, so results are always current but potentially slow for complex queries. A materialized view stores the query result as actual data on disk. Reads are fast because the computation is pre-done, but the data can become stale between refreshes. The tradeoff is: regular views = always fresh, potentially slow; materialized views = very fast reads, potentially out-of-date."
  explanation: "The right choice depends on your access pattern and freshness requirements. If the underlying data changes frequently and users need current results, a regular view is safer. If the query is expensive (multi-table joins, aggregations) and data can be slightly stale (e.g., nightly reports, dashboards refreshed every hour), a materialized view dramatically improves performance. Some databases support incremental refresh — updating only changed rows — to reduce the cost of keeping materialized views current."
```

## Explainer

You know how to write SELECT queries and join tables together. A **view** is simply a saved SELECT query that you can reference by name as though it were a table. When you write `CREATE VIEW active_customers AS SELECT id, name, email FROM customers WHERE status = 'active'`, you are not creating a new table or copying any data. You are storing the query text under the name `active_customers`. Every time someone writes `SELECT * FROM active_customers`, the database substitutes in the underlying query and executes it fresh against the current data.

This indirection provides three practical benefits. First, **simplification**: a complex multi-table join with filters can be wrapped in a view, and downstream users query a single "table" without needing to understand the join logic. Second, **security**: by granting access to a view instead of the underlying tables, you can expose only certain columns or rows. A view on the employees table that excludes salary and SSN columns lets HR assistants look up contact information without seeing compensation data. Third, **schema stability**: if the underlying table structure changes (a column is renamed, a table is split), you can update the view definition while keeping the view's interface unchanged — queries that depend on the view continue to work.

**Materialized views** are a fundamentally different tool despite the similar name. A regular view stores a query; a materialized view stores the *result* of a query. When you create a materialized view, the database executes the query and writes the output to disk, just like a table. Subsequent reads hit this pre-computed result instead of re-executing the query. This is enormously valuable for expensive aggregations — if a dashboard query joins five tables and computes monthly revenue breakdowns, a materialized view can serve that result in milliseconds. The tradeoff is staleness: the materialized view reflects the data at the time it was last refreshed, not necessarily the current state. You must explicitly refresh it (manually or on a schedule) to pick up changes.

Not all views are updatable. If you INSERT, UPDATE, or DELETE through a view, the database must be able to map those changes back to the underlying table unambiguously. Simple views over a single table with no aggregation are typically updatable. But views involving GROUP BY, DISTINCT, joins across multiple tables, or computed columns are generally read-only — the database cannot determine which base row to modify. When designing views, decide upfront whether the view is for reading only or whether it must support writes, because this constrains how you can define it.
