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

## Explainer

From your work with subqueries, you know how to nest one query inside another. But subqueries can become deeply nested and hard to follow — imagine a query where the same subquery appears three times, or where you need to reference an intermediate result in multiple places. A **Common Table Expression** (CTE), introduced by the `WITH` keyword, solves this by letting you name a subquery and reference it like a table throughout the rest of your query. Think of it as declaring a temporary, named result set that exists only for the duration of the statement.

A basic non-recursive CTE looks like this: `WITH active_customers AS (SELECT * FROM customers WHERE status = 'active') SELECT * FROM active_customers WHERE region = 'West'`. The `active_customers` CTE is computed once and then referenced by name. You can chain multiple CTEs by separating them with commas. This dramatically improves readability for complex queries because each CTE isolates one logical step — you can read and debug them independently, rather than untangling nested subqueries from the inside out.

**Recursive CTEs** are where the real power lies. They solve a problem that ordinary SQL cannot: traversing hierarchical or graph-structured data of unknown depth. Consider an employee table where each row has a `manager_id` pointing to another employee. To find all employees under a given VP — including their direct reports, their reports' reports, and so on — you cannot write a fixed number of joins because you do not know how deep the hierarchy goes. A recursive CTE handles this with two parts: an **anchor member** that selects the starting rows (the VP), and a **recursive member** that joins the CTE with itself to find the next level down. The database executes the anchor first, then repeatedly executes the recursive member using the previous iteration's results, appending new rows each time, until no new rows are produced.

The structure always follows the same pattern: `WITH RECURSIVE org_tree AS (SELECT id, name, manager_id, 1 AS depth FROM employees WHERE id = 42 UNION ALL SELECT e.id, e.name, e.manager_id, t.depth + 1 FROM employees e JOIN org_tree t ON e.manager_id = t.id) SELECT * FROM org_tree`. The anchor selects employee 42; the recursive member finds everyone whose manager is already in the result set, incrementing the depth counter each level. Most databases impose a recursion limit (often 100 or 1000 iterations) as a safety net against infinite loops — which can occur if your data contains cycles. Always ensure your hierarchy is acyclic, or add a termination condition like a maximum depth check in the WHERE clause of the recursive member.
