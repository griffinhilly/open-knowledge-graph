---
id: sql-window-functions-over-partition
title: 'Window Functions: OVER Clause, PARTITION BY, and Frames'
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
- id: sql-group-aggregate-functions
  type: hard
builds-toward:
- sql-subqueries
- query-execution-plan-analysis-explain
tags:
- window-functions
- OVER
- PARTITION-BY
- ranking
- frame
stage: formal-systems
status: draft
---

# Window Functions: OVER Clause, PARTITION BY, and Frames

## Core Idea
Window functions compute aggregates or rankings over subsets (windows) of result rows without collapsing rows like GROUP BY does. The OVER clause defines the window using PARTITION BY to divide rows into groups and ORDER BY to specify row order. Frame specifications (ROWS/RANGE BETWEEN) limit which rows contribute. Common functions include ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD, and aggregate functions with OVER.

## Explainer

You already know how GROUP BY with aggregate functions like SUM and COUNT collapses rows into summary groups — one output row per group. This is powerful, but it forces a choice: either you see the detail rows or the aggregates, never both. **Window functions** eliminate this tradeoff. They compute aggregates, rankings, or positional lookups across a set of rows related to the current row, but they do not collapse anything. Every detail row stays in the result, and the window function's output appears as an additional column alongside it.

The syntax centers on the **OVER clause**, which defines the "window" — the set of rows the function looks at for each row in the result. `SUM(amount) OVER (PARTITION BY department)` computes the total amount for each department, but instead of collapsing to one row per department, it attaches that total to every row within the department. **PARTITION BY** is like GROUP BY's cousin: it divides rows into groups, but only for the purpose of the window calculation. If you omit PARTITION BY, the window is the entire result set. Adding **ORDER BY** inside the OVER clause sorts rows within each partition, which is essential for ranking functions and running totals: `SUM(amount) OVER (PARTITION BY department ORDER BY hire_date)` gives a cumulative sum that grows as you move through rows in hire-date order.

**Ranking functions** are among the most common window functions. `ROW_NUMBER()` assigns a unique sequential integer to each row within its partition. `RANK()` does the same but assigns the same number to ties, leaving gaps (1, 2, 2, 4). `DENSE_RANK()` assigns the same number to ties without gaps (1, 2, 2, 3). These are invaluable for queries like "find the top 3 salespeople per region" — something that is extremely awkward with GROUP BY alone. **LAG** and **LEAD** let you access values from previous or subsequent rows: `LAG(revenue, 1) OVER (ORDER BY month)` gives you last month's revenue on each row, making period-over-period comparisons trivial.

The **frame specification** gives you even finer control. `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` limits the window to a sliding three-row range, enabling moving averages. `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` includes all rows from the start of the partition up to the current row's value, which is the default for ordered windows and produces running totals. The frame is the most subtle part of window functions, but understanding it unlocks the difference between a running sum, a sliding average, and a full-partition total — all using the same SUM function with different frame boundaries.
