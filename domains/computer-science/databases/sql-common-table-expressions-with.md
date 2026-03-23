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
status: validated
---

# Common Table Expressions (CTEs): WITH Clause

## Core Idea
CTEs, defined with the WITH clause, create named intermediate result sets that can be referenced in the main query. They improve readability and allow multiple references to the same temporary result.

## How It's Best Learned
Refactor a complex nested subquery into a CTE, then add a second CTE to build a more sophisticated query.

## Common Misconceptions
CTEs are not materialized by default—they are expanded at query time. Multiple references to the same CTE are re-executed unless the database optimizes them away.

## Questions

```yaml
- question: "A developer writes a CTE that performs an expensive aggregation across millions of rows. They reference this CTE three times in the main query, expecting it to execute only once and cache its results. This expectation is:"
  type: multiple-choice
  options:
    - "Correct — CTEs are always materialized and their results cached for reuse within the query"
    - "Incorrect — CTEs are typically not materialized; each reference may re-execute the underlying query"
    - "Correct, but only in PostgreSQL databases where CTEs are optimized automatically"
    - "Incorrect — CTEs always execute more times than subqueries due to parsing overhead"
  answer: 1
  explanation: "CTEs are primarily a readability and maintainability tool, not a performance optimization. Most databases treat a CTE like an inline view — substituting its definition wherever it is referenced and optimizing the combined query. Referencing a CTE three times may cause the underlying query to execute three times. For true materialization (compute once, reuse result), you need an explicit MATERIALIZED hint (PostgreSQL 12+), a temporary table, or a materialized view. The common misconception — that CTEs automatically cache results — can lead to serious performance problems on expensive computations."

- question: "What is the primary advantage of using a CTE over an equivalent nested subquery?"
  type: multiple-choice
  options:
    - "CTEs always execute faster because the database can optimize them separately from the main query"
    - "CTEs eliminate the need to create indexes on intermediate result sets"
    - "CTEs let the query logic read top-to-bottom with named steps, rather than inside-out through nested parentheses"
    - "CTEs permanently store intermediate results for use in future queries"
  answer: 2
  explanation: "The core benefit of CTEs is structural clarity. A nested subquery forces readers to parse inside-out — the innermost SELECT must be understood before the outer query makes sense. A CTE externalizes each step, names it, and lets the reader follow the logic sequentially: 'first compute X, then Y, then filter using both.' This is especially valuable for complex multi-step queries. Options A and D are wrong: CTEs have no guaranteed performance advantage over subqueries, and they do not persist between queries."

- question: "In a SQL WITH clause containing multiple CTEs, each CTE can reference CTEs that were defined earlier in the same WITH clause."
  type: true-false
  answer: true
  explanation: "This is one of the most powerful features of CTEs: they can be chained. The syntax is WITH step1 AS (...), step2 AS (SELECT ... FROM step1), step3 AS (SELECT ... FROM step2) SELECT ... FROM step3. Each CTE in the list can reference any previously defined CTE, building a pipeline of transformations. This allows complex multi-stage data transformations to be expressed as a clean sequence of named steps rather than a deeply nested single query."

- question: "Using a CTE is always preferable to creating a temporary table when an intermediate result needs to be referenced multiple times in a query."
  type: true-false
  answer: false
  explanation: "For performance-critical work involving large intermediate results referenced multiple times, a temporary table is often better because it is explicitly materialized — computed once and stored. Since CTEs are typically re-executed on each reference, a CTE referenced three times over a large dataset may be three times more expensive than a temporary table. CTEs win on simplicity and readability for moderately complex queries; temporary tables win when materialization matters for performance or when intermediate results must be indexed."

- question: "Explain the difference between a CTE and a subquery. In what scenario would you prefer a CTE even if their performance is identical?"
  type: short-answer
  answer: "A subquery is a SELECT statement nested inside another query, read inside-out. A CTE is a named temporary result set defined before the main query with the WITH keyword, read top-to-bottom. Their logical results are equivalent — they can often be rewritten as each other — but CTEs are preferable when: (1) the same intermediate result is referenced multiple times, avoiding duplication; (2) the query has multiple logical stages that benefit from named intermediate steps; (3) readability and maintainability matter, since CTEs make query intent explicit."
  explanation: "The key is that CTEs are a communication tool as much as a technical one — they document the intent behind each step of a complex query. A deeply nested subquery may be logically correct but opaque; a chain of well-named CTEs reads like a description of the transformation pipeline. In production environments where queries are maintained over time, this clarity has real value even when performance is equivalent."
```

## Explainer

You already know how to use subqueries — nested SELECT statements embedded within a larger query. Subqueries work, but they can become deeply nested and hard to read. A **Common Table Expression** (CTE) solves this by letting you define a named temporary result set *before* the main query, using the WITH clause. Instead of burying logic three levels deep inside parentheses, you pull each logical step out, give it a name, and then reference that name in your main query as if it were a table.

Here is the structural pattern. You write `WITH cte_name AS (SELECT ...)` followed by your main query that references `cte_name`. For example, suppose you want to find departments where average salary exceeds $100,000. With a subquery, you would nest the aggregation inside the WHERE clause. With a CTE, you write: `WITH dept_avg AS (SELECT department_id, AVG(salary) AS avg_sal FROM employees GROUP BY department_id) SELECT * FROM dept_avg WHERE avg_sal > 100000`. The logic reads top-to-bottom — first compute averages, then filter — rather than inside-out.

CTEs become especially valuable when you need to reference the same intermediate result multiple times. A subquery forces you to duplicate the entire nested SELECT in each location, creating maintenance headaches and potential inconsistencies. A CTE lets you define the computation once and use its name wherever needed. You can also chain multiple CTEs by separating them with commas: `WITH step1 AS (...), step2 AS (SELECT ... FROM step1), step3 AS (SELECT ... FROM step2) SELECT ... FROM step3`. Each step can reference any previously defined CTE, building a pipeline of transformations.

One important caveat: CTEs are typically *not* materialized. The database treats a CTE like an inline view — it substitutes the CTE's definition wherever it is referenced and optimizes the combined query. This means referencing a CTE three times may execute its underlying query three times, not once. Some databases (like PostgreSQL 12+) let you control this with `MATERIALIZED` and `NOT MATERIALIZED` hints, but the default behavior varies. CTEs are primarily a readability and maintainability tool rather than a performance optimization. For the performance dimension, materialized views or temporary tables are more explicit choices.
