---
id: sql-common-table-expressions-with
title: 'Common Table Expressions (CTEs): WITH Clause'
domain: computer-science
course: databases
prerequisites:
- id: sql-subqueries
  type: hard
builds-toward:
- sql-recursive-common-table-expressions
tags:
- sql
- subqueries
- readability
- composition
stage: formal-systems
status: draft
---

# Common Table Expressions (CTEs): WITH Clause

## Core Idea
CTEs, defined with the WITH clause, create named intermediate result sets that can be referenced in the main query. They improve readability and allow multiple references to the same temporary result.

## How It's Best Learned
Refactor a complex nested subquery into a CTE, then add a second CTE to build a more sophisticated query.

## Common Misconceptions
CTEs are not materialized by default—they are expanded at query time. Multiple references to the same CTE are re-executed unless the database optimizes them away.
