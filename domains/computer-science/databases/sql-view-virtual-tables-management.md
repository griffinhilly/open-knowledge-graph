---
id: sql-view-virtual-tables-management
title: 'SQL: Views and Virtual Tables'
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
builds-toward:
- denormalization-strategy
tags:
- SQL
- view
- virtual table
- materialized view
stage: formal-systems
status: draft
---

# SQL: Views and Virtual Tables

## Core Idea
A view is a virtual table defined by a SELECT query stored in the database. Views simplify complex queries, provide security by limiting column access, and enable logical data independence. Materialized views store query results physically for performance.

## Explainer

You already know how to write SELECT queries that join tables, filter rows, and compute results. Now imagine you have a complex query — say, a six-table join with aggregations — that multiple reports and applications need to run regularly. Copying and pasting that query everywhere creates a maintenance nightmare. A **view** solves this by saving the query definition in the database and giving it a name. Once created with `CREATE VIEW monthly_sales AS SELECT ...`, you can query `monthly_sales` exactly like a regular table: `SELECT * FROM monthly_sales WHERE region = 'East'`. The database expands the view definition behind the scenes and executes the underlying query.

Views serve three practical purposes. First, **simplification**: complex joins and calculations are written once and hidden behind a clean name. Analysts can query `customer_lifetime_value` without knowing it involves four joins and a window function. Second, **security**: you can grant a user access to a view that shows only certain columns or filtered rows, without granting access to the underlying tables. A view showing `employee_name` and `department` but not `salary` lets HR share org data without exposing compensation. Third, **logical data independence**: if the underlying table structure changes — say a column is renamed or a table is split — you can update the view definition without changing every query that depends on it.

A standard view is not materialized — it stores no data. Every time you query the view, the database re-executes the underlying SELECT. This means views always reflect current data, but complex views on large tables can be slow. **Materialized views** address this by physically storing the query results, like a cached snapshot. They are fast to query but must be refreshed (manually or on a schedule) to pick up changes in the underlying data. The tradeoff is freshness versus performance: use a regular view when you need up-to-the-moment accuracy, and a materialized view when you need speed and can tolerate slightly stale data.

One common point of confusion is whether you can INSERT, UPDATE, or DELETE through a view. Simple views — based on a single table with no aggregations, DISTINCT, or GROUP BY — are generally **updatable**, meaning modifications pass through to the underlying table. Complex views involving joins or aggregations are typically read-only. Most databases will tell you at creation time or at the point of attempted modification. When in doubt, treat views as read-only query simplifiers and perform writes against the base tables directly.
