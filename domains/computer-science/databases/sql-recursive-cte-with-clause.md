---
id: sql-recursive-cte-with-clause
title: Recursive Common Table Expressions and Hierarchical Queries
domain: computer-science
course: databases
prerequisites:
- id: sql-subquery-fundamentals
  type: hard
builds-toward:
- query-optimization
- query-execution-plan-analysis-explain
tags:
- CTE
- WITH
- recursive
- hierarchy
- traversal
stage: formal-systems
status: draft
---

# Recursive Common Table Expressions and Hierarchical Queries

## Core Idea
Common Table Expressions defined with WITH clauses create temporary named result sets improving readability. Recursive CTEs include an anchor query producing base rows and a recursive query that repeatedly appends new rows, enabling queries on hierarchical data like organizational trees or bill-of-materials. The recursion terminates when no new rows are returned, making CTEs ideal for variable-depth hierarchies.
