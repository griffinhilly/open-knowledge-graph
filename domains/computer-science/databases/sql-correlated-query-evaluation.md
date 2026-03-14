---
id: sql-correlated-query-evaluation
title: 'SQL: Correlated Subqueries'
domain: computer-science
course: databases
prerequisites:
- id: sql-subquery-fundamentals
  type: hard
builds-toward:
- sql-group-aggregate-functions
tags:
- SQL
- correlated subquery
- row-by-row
- dependent subquery
stage: formal-systems
status: draft
---

# SQL: Correlated Subqueries

## Core Idea
A correlated subquery references columns from the outer query and executes once per outer row. Correlated subqueries are more efficient than JOIN for some queries but can be slower if not optimized. Understanding when to use correlated subqueries vs. joins is crucial for performance.
