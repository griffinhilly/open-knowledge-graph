---
id: sql-joins
title: SQL Joins
domain: computer-science
course: databases
prerequisites:
- id: sql-select-basics
  type: hard
- id: primary-and-foreign-keys
  type: hard
builds-toward:
- sql-subqueries
- query-execution-plans
- query-optimization
tags:
- SQL
- JOIN
- INNER JOIN
- LEFT JOIN
- OUTER JOIN
- self-join
stage: formal-systems
status: draft
---

# SQL Joins

## Core Idea
Joins combine rows from two or more tables based on a related column condition, enabling the reconstruction of related data stored in separate tables. INNER JOIN returns only rows with matching values in both tables; LEFT OUTER JOIN includes all rows from the left table with NULLs for unmatched right-side rows; FULL OUTER JOIN includes all rows from both sides. Self-joins allow a table to be joined with itself, useful for hierarchical or recursive data. The join condition typically matches a foreign key to the referenced primary key.

## How It's Best Learned
Draw Venn diagrams for each join type, then run queries to verify behavior. Work through examples where rows don't match to understand when and where NULLs appear in outer joins. Rewrite a LEFT JOIN as a RIGHT JOIN by swapping table order.

## Common Misconceptions
- A CROSS JOIN (Cartesian product) produces n×m rows with no filter — this is almost always unintentional if written by accident.
- LEFT JOIN and RIGHT JOIN are symmetric; you can always rewrite one as the other by swapping table positions.
- INNER JOIN is not always more efficient than OUTER JOIN; the query planner decides execution strategy based on statistics.
