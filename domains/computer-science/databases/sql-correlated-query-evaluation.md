---
id: sql-correlated-query-evaluation
title: 'SQL: Correlated Subqueries'
domain: computer-science
course: databases
prerequisites:
- id: sql-subquery-fundamentals
  type: hard
builds-toward:
- sql-group-aggregate-functions
tags:
- SQL
- correlated subquery
- row-by-row
- dependent subquery
stage: formal-systems
status: draft
---

# SQL: Correlated Subqueries

## Core Idea
A correlated subquery references columns from the outer query and executes once per outer row. Correlated subqueries are more efficient than JOIN for some queries but can be slower if not optimized. Understanding when to use correlated subqueries vs. joins is crucial for performance.

## Explainer

You already know that a subquery is a SELECT nested inside another SQL statement, and that uncorrelated subqueries run once and produce a fixed result. A **correlated subquery** is fundamentally different: it references a column from the outer query, which means it cannot run independently. Conceptually, the database re-executes the inner query once for every row the outer query processes, substituting in the current outer row's values each time.

Consider finding employees who earn more than the average salary in their own department. An uncorrelated subquery could compute a single global average, but here the average depends on which department the current employee belongs to — so the inner query must reference the outer row's department. The query looks like: `SELECT * FROM employees e1 WHERE e1.salary > (SELECT AVG(salary) FROM employees e2 WHERE e2.department = e1.department)`. The `e1.department` reference inside the subquery is what makes it correlated. For each row in the outer `employees` scan, the database evaluates the subquery with that row's department value plugged in.

Correlated subqueries are especially natural with `EXISTS` and `NOT EXISTS`. To find customers who have placed at least one order, you can write `SELECT * FROM customers c WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id)`. The EXISTS check short-circuits — it stops as soon as it finds one matching row, which can be more efficient than a JOIN that might produce duplicate customer rows when a customer has multiple orders. This is the classic case where a correlated subquery is actually the cleaner and sometimes faster approach.

The performance concern with correlated subqueries is the "once per outer row" execution model. If the outer query returns 100,000 rows and the inner query scans a table each time, you effectively run 100,000 separate queries. In practice, modern optimizers often transform correlated subqueries into equivalent joins or semi-joins internally, eliminating the row-by-row overhead. But this transformation is not always possible — particularly with complex conditions or when the subquery uses aggregation. When performance matters, check the execution plan. If the optimizer cannot decorrelate the subquery, rewriting it as an explicit JOIN with a grouped subquery in the FROM clause is a reliable fallback.
