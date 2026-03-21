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

## Questions

```yaml
- question: "An analyst frequently runs a complex query joining five tables with aggregations. A developer creates a standard (non-materialized) view for her. What happens each time the analyst queries the view?"
  type: multiple-choice
  options:
    - "The database returns the cached result set stored when the view was created"
    - "The database re-executes the underlying SELECT query against the current base tables"
    - "The database locks the view to prevent concurrent modification of base tables"
    - "The view returns stale data unless manually refreshed with REFRESH VIEW"
  answer: 1
  explanation: "A standard view stores only the query definition, not any data. Every query against the view triggers re-execution of the underlying SELECT against the current state of the base tables. This means the view always returns up-to-date results, but offers no performance advantage over running the query directly. The tradeoff is simplicity and freshness at the cost of re-executing a potentially expensive query every time. Caching behavior belongs to materialized views, not standard views."

- question: "A company wants to give an external auditor access to employee names and departments without revealing salaries. Which view property makes this possible?"
  type: multiple-choice
  options:
    - "Materialization — storing only non-sensitive columns physically"
    - "Updateability — allowing writes to pass through only for approved columns"
    - "Security — granting access to the view while restricting access to underlying tables"
    - "Logical independence — renaming sensitive columns to hide their meaning"
  answer: 2
  explanation: "Views are a powerful security mechanism because you can grant a user SELECT permission on a view while denying them access to the underlying tables. The view exposes only the columns defined in its SELECT statement, effectively creating a filtered window into the data. The auditor never touches the base employee table directly. Materialization is about performance, not access control. Updateability is about write permissions. Logical independence is about schema changes, not data hiding."

- question: "A standard SQL view always reflects the most current data in the underlying tables."
  type: true-false
  answer: true
  explanation: "Because a standard view stores only the query definition and re-executes it each time, it always returns data as it exists in the base tables at query time. This is both its strength (freshness) and its limitation (no performance benefit). Contrast with a materialized view, which stores a snapshot of the results and must be explicitly or automatically refreshed to pick up changes — trading freshness for query speed."

- question: "You can always INSERT, UPDATE, or DELETE rows through any SQL view."
  type: true-false
  answer: false
  explanation: "Updateability through views is limited to simple cases: a view over a single table with no aggregations, DISTINCT, GROUP BY, or joins may support write operations that pass through to the base table. Complex views — especially those involving joins, aggregations, or computed columns — are typically read-only. Most databases will reject write operations on such views. The safe rule: treat views as read-only query simplifiers and write directly to base tables."

- question: "Explain the key tradeoff between a standard view and a materialized view, and describe when you would choose each."
  type: short-answer
  answer: "A standard view stores only the query definition and re-executes it every time, so it always returns current data but offers no performance benefit for expensive queries. A materialized view physically stores the query results, making reads very fast, but it must be refreshed to stay current and can return stale data between refreshes. Choose a standard view when data freshness is critical or the query is fast. Choose a materialized view when the query is expensive, reads are frequent, and slightly stale data is acceptable."
  explanation: "The core tension is freshness vs. performance. Real-time financial dashboards need standard views; daily summary reports accessed thousands of times per day benefit from materialization. Many databases (PostgreSQL, Oracle) support automatic refresh intervals to narrow the staleness window for materialized views."
```

## Explainer

You already know how to write SELECT queries that join tables, filter rows, and compute results. Now imagine you have a complex query — say, a six-table join with aggregations — that multiple reports and applications need to run regularly. Copying and pasting that query everywhere creates a maintenance nightmare. A **view** solves this by saving the query definition in the database and giving it a name. Once created with `CREATE VIEW monthly_sales AS SELECT ...`, you can query `monthly_sales` exactly like a regular table: `SELECT * FROM monthly_sales WHERE region = 'East'`. The database expands the view definition behind the scenes and executes the underlying query.

Views serve three practical purposes. First, **simplification**: complex joins and calculations are written once and hidden behind a clean name. Analysts can query `customer_lifetime_value` without knowing it involves four joins and a window function. Second, **security**: you can grant a user access to a view that shows only certain columns or filtered rows, without granting access to the underlying tables. A view showing `employee_name` and `department` but not `salary` lets HR share org data without exposing compensation. Third, **logical data independence**: if the underlying table structure changes — say a column is renamed or a table is split — you can update the view definition without changing every query that depends on it.

A standard view is not materialized — it stores no data. Every time you query the view, the database re-executes the underlying SELECT. This means views always reflect current data, but complex views on large tables can be slow. **Materialized views** address this by physically storing the query results, like a cached snapshot. They are fast to query but must be refreshed (manually or on a schedule) to pick up changes in the underlying data. The tradeoff is freshness versus performance: use a regular view when you need up-to-the-moment accuracy, and a materialized view when you need speed and can tolerate slightly stale data.

One common point of confusion is whether you can INSERT, UPDATE, or DELETE through a view. Simple views — based on a single table with no aggregations, DISTINCT, or GROUP BY — are generally **updatable**, meaning modifications pass through to the underlying table. Complex views involving joins or aggregations are typically read-only. Most databases will tell you at creation time or at the point of attempted modification. When in doubt, treat views as read-only query simplifiers and perform writes against the base tables directly.
