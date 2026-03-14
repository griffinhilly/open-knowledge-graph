---
id: sql-recursive-common-table-expressions
title: 'Recursive CTEs: Hierarchical and Graph Queries'
domain: computer-science
course: databases
prerequisites:
- id: sql-common-table-expressions-with
  type: hard
tags:
- sql
- recursion
- hierarchies
- graphs
stage: formal-systems
status: draft
---

# Recursive CTEs: Hierarchical and Graph Queries

## Core Idea
Recursive CTEs reference themselves to iteratively build results, enabling traversal of hierarchies (trees, organizational charts) and graphs without explicit stored procedures.

## How It's Best Learned
Start with an organizational hierarchy or parent-child table, write a base case, then add the recursive case to traverse levels.

## Common Misconceptions
Recursive CTEs must have a base case and a recursive case separated by UNION. The recursion terminates when no new rows are produced; infinite recursion is prevented by MAX_RECURSION_DEPTH limits.
