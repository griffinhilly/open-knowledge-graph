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

## Explainer

You already know how regular CTEs work — a `WITH` clause that names a temporary result set so you can reference it later in the query. A **recursive CTE** extends this by allowing the CTE to reference itself, enabling the kind of iterative traversal that would otherwise require procedural code or multiple queries. The classic use case is hierarchical data: org charts, category trees, bill-of-materials structures, or any table where rows point to other rows in the same table via a parent ID.

The structure has two parts connected by `UNION ALL`. The **anchor member** (base case) selects the starting rows — typically the root of the hierarchy. The **recursive member** joins the CTE back to itself to find the next level. For example, to find all employees under a given manager: the anchor selects the manager, and the recursive member joins employees to the CTE on `employee.manager_id = cte.employee_id`. On each iteration, the database takes the rows produced in the previous step, applies the recursive query to find new rows, and appends them. When no new rows are produced, recursion stops.

Think of it like a breadth-first search. Iteration 0 produces the root nodes. Iteration 1 finds their children. Iteration 2 finds the grandchildren. Each iteration sees only the rows from the previous iteration, not the entire accumulated result. This is why adding a `depth` counter works naturally: the anchor sets `depth = 0`, and the recursive member sets `depth = parent.depth + 1`. You can use this depth to limit traversal (`WHERE depth < 5`) or to indent an org chart display.

The most common pitfall is **infinite recursion** caused by cycles in the data. If employee A reports to B who reports to A, the recursive CTE will loop forever — or until the database hits its `MAXRECURSION` limit and throws an error. Guard against this by tracking visited nodes (adding a path column and checking for repeated IDs) or by setting an explicit depth limit. Also note the difference between `UNION ALL` and `UNION`: most recursive CTEs use `UNION ALL` because deduplication at each step (`UNION`) can mask legitimate repeated visits in graph traversal and adds unnecessary overhead when the data is naturally tree-shaped.
