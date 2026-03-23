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
status: validated
---

# SQL: Correlated Subqueries

## Core Idea
A correlated subquery references columns from the outer query and executes once per outer row. Correlated subqueries are more efficient than JOIN for some queries but can be slower if not optimized. Understanding when to use correlated subqueries vs. joins is crucial for performance.

## Questions

```yaml
- question: "An analyst writes: SELECT * FROM employees e1 WHERE e1.salary > (SELECT AVG(salary) FROM employees e2 WHERE e2.department = e1.department). What makes this a correlated subquery?"
  type: multiple-choice
  options:
    - "It uses an aggregate function (AVG) inside the subquery"
    - "The subquery references e1.department, a column from the outer query, so it cannot run independently"
    - "The subquery scans the same table as the outer query"
    - "The subquery returns a scalar value instead of a table"
  answer: 1
  explanation: "A subquery is correlated when it references a column from the outer query — here, e1.department. This reference creates a dependency: the inner query's result changes based on which outer row is being evaluated, so it cannot be run once and reused. The database conceptually re-executes the subquery for each outer row with that row's department value substituted in. Using AVG, scanning the same table, or returning a scalar are all possible in both correlated and uncorrelated subqueries — none of those features is what makes a subquery correlated."

- question: "You need to find all customers who have placed at least one order. Which approach is most likely to be efficient and avoid duplicate customer rows?"
  type: multiple-choice
  options:
    - "JOIN customers to orders on customer_id, since joins are always faster than correlated subqueries"
    - "Use a correlated EXISTS subquery: SELECT * FROM customers c WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id)"
    - "Use SELECT DISTINCT with a join to remove duplicates after joining"
    - "Use a GROUP BY on the join result to collapse duplicate customer rows"
  answer: 1
  explanation: "EXISTS with a correlated subquery is the natural fit for existence checks. It short-circuits — the inner query stops as soon as one matching row is found — and it returns each customer at most once, because the outer query drives iteration. A plain JOIN of customers to orders produces one row per order, so a customer with 10 orders appears 10 times; you must add DISTINCT or GROUP BY to fix it, adding overhead. The claim that joins are always faster than correlated subqueries is false: modern optimizers often convert EXISTS subqueries into semi-joins internally, and for existence tests the EXISTS pattern is often both cleaner and faster."

- question: "A correlated subquery that references the outer query is guaranteed to execute once per outer row, regardless of the database engine used."
  type: true-false
  answer: false
  explanation: "Conceptually, a correlated subquery executes once per outer row, but modern query optimizers often decorrelate subqueries — transforming them internally into equivalent joins or semi-joins that execute more efficiently. This transformation is not always possible (complex conditions or certain aggregations may block it), but when it is, the optimizer avoids the row-by-row overhead entirely. 'Guaranteed to execute once per outer row' is the naive execution model, not a guarantee about actual behavior. This is why checking the execution plan (EXPLAIN/EXPLAIN ANALYZE) is necessary when performance matters."

- question: "An uncorrelated subquery must be rewritten as a JOIN to improve performance, while a correlated subquery can be left as-is."
  type: true-false
  answer: false
  explanation: "This reverses the actual concern. Uncorrelated subqueries run once and return a fixed result — they are rarely a performance problem. Correlated subqueries are the ones that can become expensive because they re-execute per outer row when the optimizer cannot decorrelate them. The recommended performance fix for a poorly-performing correlated subquery is often to rewrite it as an explicit JOIN with a grouped subquery in the FROM clause, not the other way around. Uncorrelated subqueries typically need no rewriting."

- question: "What fundamentally distinguishes a correlated subquery from an uncorrelated subquery, and why does this distinction affect how the database executes the query?"
  type: short-answer
  answer: "A correlated subquery references a column from the outer query, creating a dependency: the inner query's result changes for each outer row, so it cannot be evaluated once and reused. An uncorrelated subquery has no such reference — it runs once, produces a fixed result, and that result is used for all outer rows. The dependency in a correlated subquery means the database must (conceptually) re-execute the inner query for each outer row, substituting the current outer row's values. This per-row execution model is what makes correlated subqueries potentially expensive on large outer result sets."
  explanation: "The key test is whether the subquery can run independently. If you can extract the subquery and execute it by itself without any input from the outer query and get a meaningful result, it is uncorrelated. If it references outer columns and would fail or be meaningless without them, it is correlated. Understanding this distinction is essential for predicting query performance and knowing when to rewrite."
```

## Explainer

You already know that a subquery is a SELECT nested inside another SQL statement, and that uncorrelated subqueries run once and produce a fixed result. A **correlated subquery** is fundamentally different: it references a column from the outer query, which means it cannot run independently. Conceptually, the database re-executes the inner query once for every row the outer query processes, substituting in the current outer row's values each time.

Consider finding employees who earn more than the average salary in their own department. An uncorrelated subquery could compute a single global average, but here the average depends on which department the current employee belongs to — so the inner query must reference the outer row's department. The query looks like: `SELECT * FROM employees e1 WHERE e1.salary > (SELECT AVG(salary) FROM employees e2 WHERE e2.department = e1.department)`. The `e1.department` reference inside the subquery is what makes it correlated. For each row in the outer `employees` scan, the database evaluates the subquery with that row's department value plugged in.

Correlated subqueries are especially natural with `EXISTS` and `NOT EXISTS`. To find customers who have placed at least one order, you can write `SELECT * FROM customers c WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id)`. The EXISTS check short-circuits — it stops as soon as it finds one matching row, which can be more efficient than a JOIN that might produce duplicate customer rows when a customer has multiple orders. This is the classic case where a correlated subquery is actually the cleaner and sometimes faster approach.

The performance concern with correlated subqueries is the "once per outer row" execution model. If the outer query returns 100,000 rows and the inner query scans a table each time, you effectively run 100,000 separate queries. In practice, modern optimizers often transform correlated subqueries into equivalent joins or semi-joins internally, eliminating the row-by-row overhead. But this transformation is not always possible — particularly with complex conditions or when the subquery uses aggregation. When performance matters, check the execution plan. If the optimizer cannot decorrelate the subquery, rewriting it as an explicit JOIN with a grouped subquery in the FROM clause is a reliable fallback.
