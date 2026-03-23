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
status: validated
---

# Recursive Common Table Expressions and Hierarchical Queries

## Core Idea
Common Table Expressions defined with WITH clauses create temporary named result sets improving readability. Recursive CTEs include an anchor query producing base rows and a recursive query that repeatedly appends new rows, enabling queries on hierarchical data like organizational trees or bill-of-materials. The recursion terminates when no new rows are returned, making CTEs ideal for variable-depth hierarchies.

## Questions

```yaml
- question: "A recursive CTE is used to traverse an employee hierarchy. After the anchor query runs, the recursive member finds no employees whose manager_id matches any id in the current result set. What happens next?"
  type: multiple-choice
  options:
    - "The database throws an error because the recursion must complete at least two iterations"
    - "The recursion terminates and the final result is just the rows from the anchor query"
    - "The database continues running the recursive member indefinitely until the recursion limit is hit"
    - "The anchor query reruns to seed new rows"
  answer: 1
  explanation: "Recursive CTEs terminate when the recursive member returns zero new rows — this is the natural stopping condition. If the anchor selects a leaf node (an employee with no direct reports), the very first recursive iteration finds nothing, and the recursion stops immediately, returning only the anchor rows. No error is thrown; the query simply ends. This self-terminating property is what makes recursive CTEs safe for trees of any depth."

- question: "You need to query all ancestors of a given product in a bill-of-materials table (each part has a parent_part_id). Which approach correctly accomplishes this?"
  type: multiple-choice
  options:
    - "Write a subquery that performs a self-join on the table five times, covering up to five levels of ancestry"
    - "Use a recursive CTE with an anchor that selects the starting part and a recursive member that joins the CTE to the table on parent_part_id"
    - "Use a GROUP BY with a HAVING clause to filter for ancestor rows"
    - "Use a window function with ROWS BETWEEN to scan backward through the hierarchy"
  answer: 1
  explanation: "Recursive CTEs are the right tool precisely because the hierarchy depth is unknown. A fixed number of self-joins only works if you know the maximum depth in advance — and even then it's brittle. GROUP BY and window functions don't traverse parent-child relationships iteratively. The recursive CTE pattern — anchor on the starting part, recursive member following parent_part_id upward — handles any depth automatically."

- question: "A non-recursive CTE defined with WITH is computed once and its result is reused every time it is referenced in the rest of the query."
  type: true-false
  answer: true
  explanation: "This is one of the key readability and performance benefits of non-recursive CTEs — the named result set is computed once and can be referenced multiple times in the main query, just like a temporary table. This contrasts with a correlated subquery, which re-executes for each row of the outer query. (Note: some query optimizers may inline the CTE rather than materializing it, but logically the result is defined once.)"

- question: "A recursive CTE can safely traverse any table with a manager_id self-referencing column without risk of infinite loops."
  type: true-false
  answer: false
  explanation: "Recursive CTEs will loop infinitely if the data contains cycles — for example, if employee A's manager is B and B's manager is A. Most databases impose a maximum recursion depth (commonly 100 or 1000 iterations) as a safety net, but this causes an error rather than a graceful result. To safely handle potentially cyclic data, you must add a termination condition (such as a maximum depth check in the WHERE clause) or maintain a visited-node list. Assuming acyclicity without checking is a common bug."

- question: "What is the essential structural difference between a recursive CTE and a non-recursive one, and what problem does the recursive form solve that ordinary SQL cannot?"
  type: short-answer
  answer: "A recursive CTE contains two parts joined by UNION ALL: an anchor member that produces the base rows, and a recursive member that references the CTE itself to generate the next level of rows. This repeats until the recursive member returns no new rows. The problem it solves is traversal of hierarchical or graph-structured data of unknown depth — organizational trees, bill-of-materials, category hierarchies. Ordinary SQL requires you to write a fixed number of joins, which only works if you know the depth in advance; the recursive CTE handles arbitrary depth automatically."
  explanation: "The key insight is that ordinary SQL is not Turing-complete for graph traversal — you can't follow an unknown number of parent-child links without recursion. The recursive CTE adds exactly this capability by letting the query reference its own partial result at each iteration. The termination condition (no new rows) acts as the base case of the recursion, just like a recursive function that stops when its condition is met."
```

## Explainer

From your work with subqueries, you know how to nest one query inside another. But subqueries can become deeply nested and hard to follow — imagine a query where the same subquery appears three times, or where you need to reference an intermediate result in multiple places. A **Common Table Expression** (CTE), introduced by the `WITH` keyword, solves this by letting you name a subquery and reference it like a table throughout the rest of your query. Think of it as declaring a temporary, named result set that exists only for the duration of the statement.

A basic non-recursive CTE looks like this: `WITH active_customers AS (SELECT * FROM customers WHERE status = 'active') SELECT * FROM active_customers WHERE region = 'West'`. The `active_customers` CTE is computed once and then referenced by name. You can chain multiple CTEs by separating them with commas. This dramatically improves readability for complex queries because each CTE isolates one logical step — you can read and debug them independently, rather than untangling nested subqueries from the inside out.

**Recursive CTEs** are where the real power lies. They solve a problem that ordinary SQL cannot: traversing hierarchical or graph-structured data of unknown depth. Consider an employee table where each row has a `manager_id` pointing to another employee. To find all employees under a given VP — including their direct reports, their reports' reports, and so on — you cannot write a fixed number of joins because you do not know how deep the hierarchy goes. A recursive CTE handles this with two parts: an **anchor member** that selects the starting rows (the VP), and a **recursive member** that joins the CTE with itself to find the next level down. The database executes the anchor first, then repeatedly executes the recursive member using the previous iteration's results, appending new rows each time, until no new rows are produced.

The structure always follows the same pattern: `WITH RECURSIVE org_tree AS (SELECT id, name, manager_id, 1 AS depth FROM employees WHERE id = 42 UNION ALL SELECT e.id, e.name, e.manager_id, t.depth + 1 FROM employees e JOIN org_tree t ON e.manager_id = t.id) SELECT * FROM org_tree`. The anchor selects employee 42; the recursive member finds everyone whose manager is already in the result set, incrementing the depth counter each level. Most databases impose a recursion limit (often 100 or 1000 iterations) as a safety net against infinite loops — which can occur if your data contains cycles. Always ensure your hierarchy is acyclic, or add a termination condition like a maximum depth check in the WHERE clause of the recursive member.
