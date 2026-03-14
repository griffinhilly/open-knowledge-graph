---
id: sql-set-operations-combining-results
title: 'SQL: Set Operations (UNION, INTERSECT, EXCEPT)'
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
tags:
- SQL
- UNION
- INTERSECT
- EXCEPT
- set operations
stage: formal-systems
status: draft
---

# SQL: Set Operations (UNION, INTERSECT, EXCEPT)

## Core Idea
Set operations combine results from multiple SELECT statements. UNION concatenates unique rows from both queries. INTERSECT returns only rows appearing in both queries. EXCEPT returns rows in the first query but not the second. These operations implement relational set algebra.

## How It's Best Learned
Practice combining results from different tables and queries with different set operations. Understand the difference between UNION (unique rows) and UNION ALL (all rows including duplicates).
