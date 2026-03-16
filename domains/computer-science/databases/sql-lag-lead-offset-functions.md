---
id: sql-lag-lead-offset-functions
title: 'LAG, LEAD, and OFFSET: Accessing Rows in Windows'
domain: computer-science
course: databases
prerequisites:
- id: sql-window-functions-introduction
  type: hard
tags:
- sql
- window-functions
- row-access
- analytics
stage: formal-systems
status: draft
---

# LAG, LEAD, and OFFSET: Accessing Rows in Windows

## Core Idea
LAG accesses a previous row in the window, LEAD accesses a following row, and FIRST_VALUE/LAST_VALUE access specific rows within a frame. These enable row-to-row comparisons and sequential analysis.

## Explainer

From your introduction to window functions, you know that OVER defines a window of related rows and that window functions compute values across that window without collapsing the result set. LAG, LEAD, and related offset functions solve a specific problem that is awkward without them: accessing a value from a different row in the same result set. Before window functions existed, computing "this month's revenue minus last month's revenue" required a self-join — joining the table to itself on an offset date. LAG and LEAD replace that pattern with a single, readable expression.

**LAG(column, offset, default)** looks backward. Given rows ordered by some column, `LAG(revenue, 1)` on each row returns the revenue from the previous row. The offset defaults to 1 but can be any positive integer — `LAG(revenue, 3)` looks three rows back. The optional third argument provides a default when there is no previous row (the first row in the window has nothing to look back at, so without a default you get NULL). **LEAD** is the mirror: `LEAD(revenue, 1)` looks one row forward. Together they let you compute differences, growth rates, and trends in a single pass: `revenue - LAG(revenue, 1) OVER (ORDER BY month)` gives you month-over-month change on every row.

**FIRST_VALUE** and **LAST_VALUE** access the first or last row within the current window frame rather than at a fixed offset. `FIRST_VALUE(price) OVER (PARTITION BY product ORDER BY sale_date)` gives you the earliest recorded price for each product, repeated on every row — useful for computing how far the current price has moved from its starting point. LAST_VALUE requires care: the default frame is `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`, so LAST_VALUE just returns the current row's value. To get the actual last row in the partition, you need to extend the frame: `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`. **NTH_VALUE(column, n)** generalizes this further, returning the value from the nth row in the frame.

The key mental model is that these functions turn a tabular result into something you can navigate positionally — forward, backward, or to specific landmarks — without restructuring the query. PARTITION BY resets the navigation for each group (so LAG across a partition boundary returns NULL or the default, not a value from a different group), and ORDER BY determines which direction "previous" and "next" mean. Any time you find yourself writing a self-join to compare a row with its neighbor, LAG or LEAD is almost certainly the cleaner solution.
