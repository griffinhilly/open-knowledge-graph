---
id: sql-inner-join-combining-tables
title: 'SQL: INNER JOIN and Basic Joins'
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
- id: relational-algebra-fundamentals
  type: soft
builds-toward:
- sql-outer-joins-comprehensive
- sql-complex-join-types
- sql-inner-join-combining-tables
tags:
- SQL
- JOIN
- INNER JOIN
- combining tables
stage: formal-systems
status: draft
---

# SQL: INNER JOIN and Basic Joins

## Core Idea
INNER JOIN combines rows from two tables where the join condition is true. The join condition typically matches foreign keys to primary keys. INNER JOIN returns only rows with matches in both tables, implementing the relational algebra join operation.

## How It's Best Learned
Start with simple INNER JOINs on primary key–foreign key relationships, then practice joins on non-key columns and multiple join conditions. Visualize which rows are included and excluded.
