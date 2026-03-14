---
id: sql-outer-joins-comprehensive
title: 'SQL: OUTER JOINs (LEFT, RIGHT, FULL)'
domain: computer-science
course: databases
prerequisites:
- id: sql-inner-join-combining-tables
  type: hard
builds-toward:
- sql-complex-join-types
tags:
- SQL
- LEFT JOIN
- RIGHT JOIN
- FULL OUTER JOIN
stage: formal-systems
status: draft
---

# SQL: OUTER JOINs (LEFT, RIGHT, FULL)

## Core Idea
LEFT OUTER JOIN includes all rows from the left table and matching rows from the right table (nulls for non-matches). RIGHT OUTER JOIN is the opposite. FULL OUTER JOIN includes all rows from both tables. Outer joins are essential when relationships are optional.

## How It's Best Learned
Compare results of INNER vs LEFT JOIN on the same query to understand what rows are included/excluded. Practice scenarios where entities have optional relationships (e.g., employees who may not have assigned projects).
