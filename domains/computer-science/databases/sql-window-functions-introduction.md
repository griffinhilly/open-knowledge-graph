---
id: sql-window-functions-introduction
title: 'Window Functions: Analytical Queries'
domain: computer-science
course: databases
prerequisites:
- id: sql-group-aggregate-functions
  type: hard
builds-toward:
- sql-ranking-functions-row-number
- sql-aggregate-window-functions
- sql-lag-lead-offset-functions
tags:
- sql
- analytics
- window-functions
- advanced-queries
stage: formal-systems
status: draft
---

# Window Functions: Analytical Queries

## Core Idea
Window functions perform calculations across a set of rows defined by an OVER clause, without collapsing rows as GROUP BY does. They enable row-by-row analysis while maintaining detail rows in the result set.

## How It's Best Learned
Start with simple window functions like ROW_NUMBER(), then understand the PARTITION BY and ORDER BY clauses, and finally explore frame specifications (ROWS, RANGE).

## Common Misconceptions
Window functions do not reduce rows like GROUP BY—each input row produces an output row. The window frame is separate from the query's WHERE clause filtering.

## Questions

```yaml
- question: "You want a result set showing each employee's name, salary, and their department's average salary — all in one row per employee. Why does GROUP BY fail here?"
  type: multiple-choice
  options:
    - "GROUP BY doesn't support AVG for salary columns"
    - "GROUP BY collapses rows — you'd get one row per department, losing the individual employee rows"
    - "You'd need to join the table to itself, which GROUP BY prohibits"
    - "GROUP BY only works with COUNT, not AVG"
  answer: 1
  explanation: "GROUP BY aggregates rows into groups, producing one output row per group. If you GROUP BY department, you get one row per department with the average salary — the individual employee records disappear. Window functions solve exactly this problem: `AVG(salary) OVER (PARTITION BY department)` computes the department average while preserving every employee's individual row in the output. Options A, C, and D are simply false about how GROUP BY and AVG work."

- question: "What effect does adding ORDER BY inside an OVER clause have on a window function like SUM()?"
  type: multiple-choice
  options:
    - "It changes which rows are included in the result set"
    - "It sorts the final output just like ORDER BY at the end of the query"
    - "It changes the calculation from a total across the full partition to a running cumulative total"
    - "It has no effect — ORDER BY only matters outside the OVER clause"
  answer: 2
  explanation: "ORDER BY inside OVER defines a frame within the partition — by default, all rows from the start of the partition up to and including the current row. This turns SUM(amount) into a running total that accumulates as you move through the ordered rows. Without ORDER BY, the full partition is the frame and every row gets the same total. The ORDER BY here is conceptually distinct from the query-level ORDER BY, which controls output sorting, not calculation frames."

- question: "You can use a window function result directly in a WHERE clause to filter rows — for example, WHERE ROW_NUMBER() OVER (ORDER BY salary DESC) = 1."
  type: true-false
  answer: false
  explanation: "Window functions are evaluated after WHERE, GROUP BY, and HAVING — so the window function result doesn't exist yet when the WHERE clause is processed. Filtering on a window function result requires wrapping the query in a subquery or CTE, then filtering in the outer query: `SELECT * FROM (SELECT *, ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn FROM employees) t WHERE rn = 1`. This evaluation order is one of the most common points of confusion with window functions."

- question: "PARTITION BY inside an OVER clause groups rows for the window calculation in a conceptually similar way to GROUP BY, but without collapsing those rows into a single output row."
  type: true-false
  answer: true
  explanation: "This is exactly right. PARTITION BY divides the rows into groups (partitions) and the window function operates independently within each partition — exactly like GROUP BY defines groups for aggregation. The crucial difference is that GROUP BY reduces the result set to one row per group, while PARTITION BY keeps all input rows, each receiving a value computed from its partition. A window function with no PARTITION BY treats the entire table as one partition."

- question: "Why can't you filter on a window function result in a WHERE clause, and what is the correct way to do it?"
  type: short-answer
  answer: "Window functions are evaluated late in query processing — after WHERE, GROUP BY, and HAVING — so a window function result does not yet exist when the WHERE clause runs. To filter on a window function result, wrap the query in a subquery or CTE that computes the window function, then apply the filter in the outer query's WHERE clause. For example: SELECT * FROM (SELECT *, RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS rnk FROM employees) t WHERE rnk <= 3."
  explanation: "SQL has a defined logical evaluation order: FROM → WHERE → GROUP BY → HAVING → SELECT (including window functions) → ORDER BY → LIMIT. The WHERE clause runs before window functions are computed, so they cannot appear in WHERE. This is a fundamental architectural fact about SQL, not a bug — it means filters on window results always require a wrapping subquery or CTE."
```

## Explainer

You already know how GROUP BY with aggregate functions (SUM, COUNT, AVG) collapses rows into summary groups. If you group sales by region, you get one row per region with the total for that region — but you lose the individual sale rows. **Window functions** solve the problem of wanting both: the detail of every individual row and the context of an aggregate calculated across related rows.

The key syntax is the **OVER clause**. Instead of `SELECT region, SUM(amount) FROM sales GROUP BY region`, you write `SELECT region, amount, SUM(amount) OVER (PARTITION BY region) AS region_total FROM sales`. Every row in the result keeps its original `amount`, and a new column `region_total` appears alongside it, showing the sum for that row's region. No rows are collapsed. The **PARTITION BY** clause inside OVER defines the "window" — the group of rows the function operates on. It works like GROUP BY conceptually, but without reducing the result set.

Adding **ORDER BY** inside the OVER clause changes the behavior from "compute across the whole partition" to "compute a running calculation." `SUM(amount) OVER (PARTITION BY region ORDER BY sale_date)` gives a running total that accumulates as you move through each region's sales in date order. This is because ORDER BY in a window function defines a **frame** — by default, all rows from the start of the partition up to and including the current row. The simplest window function to start with is `ROW_NUMBER() OVER (ORDER BY sale_date)`, which assigns sequential numbers 1, 2, 3... to rows in date order. Combined with PARTITION BY, `ROW_NUMBER() OVER (PARTITION BY region ORDER BY amount DESC)` numbers each region's sales from highest to lowest — making it trivial to find the top 3 sales per region by wrapping the query and filtering where `row_num <= 3`.

Window functions are evaluated after WHERE, GROUP BY, and HAVING, but before the final ORDER BY and LIMIT. This means you cannot use a window function in a WHERE clause directly — if you need to filter on a window function result (like "only rows where rank = 1"), you must wrap the query in a subquery or CTE and filter in the outer query. This evaluation order is the most common point of confusion, but once you internalize it, window functions become one of the most powerful analytical tools in SQL — enabling rankings, running totals, moving averages, and row comparisons that would otherwise require convoluted self-joins or application-level code.
