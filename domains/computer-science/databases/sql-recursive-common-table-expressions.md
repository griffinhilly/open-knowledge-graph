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
status: validated
---

# Recursive CTEs: Hierarchical and Graph Queries

## Core Idea
Recursive CTEs reference themselves to iteratively build results, enabling traversal of hierarchies (trees, organizational charts) and graphs without explicit stored procedures.

## How It's Best Learned
Start with an organizational hierarchy or parent-child table, write a base case, then add the recursive case to traverse levels.

## Common Misconceptions
Recursive CTEs must have a base case and a recursive case separated by UNION. The recursion terminates when no new rows are produced; infinite recursion is prevented by MAX_RECURSION_DEPTH limits.

## Questions

```yaml
- question: "You write a recursive CTE to traverse a social network where friendships are bidirectional. After running it, the query times out. What is the most likely cause?"
  type: multiple-choice
  options:
    - "Recursive CTEs cannot traverse undirected graphs — they only work on trees"
    - "The recursive member is cycling: A finds B, B finds A, A finds B again — the bidirectional edges create an infinite loop"
    - "UNION ALL should be replaced with UNION to prevent duplicate rows"
    - "The anchor member selected too many starting nodes"
  answer: 1
  explanation: "In a bidirectional graph, friendship between A and B means A appears in B's friend list and B in A's. The recursive member will follow A→B, then B→A, then A→B again — infinite loop. Option A is wrong; recursive CTEs can traverse undirected graphs with proper cycle detection. Option C misunderstands the problem — UNION deduplicates within a step but doesn't prevent cycles across iterations. The reliable solution is tracking visited nodes explicitly (e.g., maintaining a path array), not choosing UNION vs UNION ALL."

- question: "In a recursive CTE, the recursive member executes on iteration 3. What rows does it see?"
  type: multiple-choice
  options:
    - "All rows accumulated from iterations 0, 1, and 2 combined"
    - "Only the rows produced by iteration 2"
    - "Only the rows from the anchor member (iteration 0)"
    - "All rows in the original table, filtered by the WHERE clause"
  answer: 1
  explanation: "On each iteration, the recursive member sees only the rows produced by the immediately preceding iteration — not the full accumulated result. The database treats the CTE name inside the recursive member as a reference to 'last round's output.' This is what makes depth tracking work naturally: each row knows it came from the previous level. It also explains why cycles cause infinite loops — rows from two steps back are not visible to prevent revisiting."

- question: "Adding a depth counter column (anchor sets depth = 0, recursive member sets depth = parent.depth + 1) works correctly because each iteration only sees rows from the previous step."
  type: true-false
  answer: true
  explanation: "Exactly correct. Since each iteration receives only the prior step's rows, 'parent.depth' reliably refers to the depth of the row that generated the current row. Iteration 1 receives depth-0 rows and produces depth-1 rows. Iteration 2 receives depth-1 rows and produces depth-2 rows. The counter increments correctly at every level because the lineage is clean — each row has exactly one parent in scope."

- question: "Using UNION instead of UNION ALL in a recursive CTE is always safer because it eliminates duplicate rows and prevents infinite recursion."
  type: true-false
  answer: false
  explanation: "UNION vs UNION ALL is about deduplication within each step's output, not about preventing cycles across iterations. If node A was visited two iterations ago, using UNION in the current step doesn't help — that prior visit is no longer in scope. For legitimate graph traversal where the same node appears in multiple valid paths, UNION would incorrectly suppress valid rows. The correct protection against cycles is tracking visited nodes explicitly or setting a depth limit — not choosing UNION."

- question: "Why does a recursive CTE terminate naturally when traversing a tree, but may not terminate when traversing a graph?"
  type: short-answer
  answer: "A tree has no cycles: every recursive step reaches a node that hasn't been visited before, and the tree is finite, so eventually the recursive member produces no new rows and iteration stops. A graph may have cycles: a node already visited can be reached again via a different path, so the recursive member keeps producing rows — the 'no new rows' termination condition is never reached."
  explanation: "Termination requires the recursive member to eventually return empty. In a tree, every path ends at a leaf node with no children — at some depth, every branch exhausts. In a graph with cycles, the same nodes reappear via different routes, and the recursive member never goes empty. This is why cycle detection (path tracking, node-visit checking, or MAX_RECURSION limits) is mandatory for graph traversal but often unnecessary for pure tree traversal."
```

## Explainer

You already know how regular CTEs work — a `WITH` clause that names a temporary result set so you can reference it later in the query. A **recursive CTE** extends this by allowing the CTE to reference itself, enabling the kind of iterative traversal that would otherwise require procedural code or multiple queries. The classic use case is hierarchical data: org charts, category trees, bill-of-materials structures, or any table where rows point to other rows in the same table via a parent ID.

The structure has two parts connected by `UNION ALL`. The **anchor member** (base case) selects the starting rows — typically the root of the hierarchy. The **recursive member** joins the CTE back to itself to find the next level. For example, to find all employees under a given manager: the anchor selects the manager, and the recursive member joins employees to the CTE on `employee.manager_id = cte.employee_id`. On each iteration, the database takes the rows produced in the previous step, applies the recursive query to find new rows, and appends them. When no new rows are produced, recursion stops.

Think of it like a breadth-first search. Iteration 0 produces the root nodes. Iteration 1 finds their children. Iteration 2 finds the grandchildren. Each iteration sees only the rows from the previous iteration, not the entire accumulated result. This is why adding a `depth` counter works naturally: the anchor sets `depth = 0`, and the recursive member sets `depth = parent.depth + 1`. You can use this depth to limit traversal (`WHERE depth < 5`) or to indent an org chart display.

The most common pitfall is **infinite recursion** caused by cycles in the data. If employee A reports to B who reports to A, the recursive CTE will loop forever — or until the database hits its `MAXRECURSION` limit and throws an error. Guard against this by tracking visited nodes (adding a path column and checking for repeated IDs) or by setting an explicit depth limit. Also note the difference between `UNION ALL` and `UNION`: most recursive CTEs use `UNION ALL` because deduplication at each step (`UNION`) can mask legitimate repeated visits in graph traversal and adds unnecessary overhead when the data is naturally tree-shaped.
