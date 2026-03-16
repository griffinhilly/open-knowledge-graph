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

## Explainer

You already know how GROUP BY with aggregate functions (SUM, COUNT, AVG) collapses rows into summary groups. If you group sales by region, you get one row per region with the total for that region — but you lose the individual sale rows. **Window functions** solve the problem of wanting both: the detail of every individual row and the context of an aggregate calculated across related rows.

The key syntax is the **OVER clause**. Instead of `SELECT region, SUM(amount) FROM sales GROUP BY region`, you write `SELECT region, amount, SUM(amount) OVER (PARTITION BY region) AS region_total FROM sales`. Every row in the result keeps its original `amount`, and a new column `region_total` appears alongside it, showing the sum for that row's region. No rows are collapsed. The **PARTITION BY** clause inside OVER defines the "window" — the group of rows the function operates on. It works like GROUP BY conceptually, but without reducing the result set.

Adding **ORDER BY** inside the OVER clause changes the behavior from "compute across the whole partition" to "compute a running calculation." `SUM(amount) OVER (PARTITION BY region ORDER BY sale_date)` gives a running total that accumulates as you move through each region's sales in date order. This is because ORDER BY in a window function defines a **frame** — by default, all rows from the start of the partition up to and including the current row. The simplest window function to start with is `ROW_NUMBER() OVER (ORDER BY sale_date)`, which assigns sequential numbers 1, 2, 3... to rows in date order. Combined with PARTITION BY, `ROW_NUMBER() OVER (PARTITION BY region ORDER BY amount DESC)` numbers each region's sales from highest to lowest — making it trivial to find the top 3 sales per region by wrapping the query and filtering where `row_num <= 3`.

Window functions are evaluated after WHERE, GROUP BY, and HAVING, but before the final ORDER BY and LIMIT. This means you cannot use a window function in a WHERE clause directly — if you need to filter on a window function result (like "only rows where rank = 1"), you must wrap the query in a subquery or CTE and filter in the outer query. This evaluation order is the most common point of confusion, but once you internalize it, window functions become one of the most powerful analytical tools in SQL — enabling rankings, running totals, moving averages, and row comparisons that would otherwise require convoluted self-joins or application-level code.
