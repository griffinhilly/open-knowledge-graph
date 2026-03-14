---
id: sql-subquery-fundamentals
title: 'SQL: Subqueries (Scalar, Row, Table)'
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
builds-toward:
- sql-correlated-query-evaluation
- sql-group-aggregate-functions
tags:
- SQL
- subquery
- nested query
- inner query
stage: formal-systems
status: draft
---

# SQL: Subqueries (Scalar, Row, Table)

## Core Idea
A subquery (inner query) is a SELECT statement nested within another SQL statement. Scalar subqueries return one value, row subqueries return multiple columns, and table subqueries return multiple rows. Subqueries enable modular query construction and complex filtering.
