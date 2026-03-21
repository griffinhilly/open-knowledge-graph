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

## Questions

```yaml
- question: "You want to compute month-over-month revenue change for each row in a sales table ordered by month. Which approach is correct?"
  type: multiple-choice
  options:
    - "SELECT month, revenue - LAG(revenue, 1) OVER (ORDER BY month) AS mom_change FROM sales"
    - "SELECT month, revenue - LAG(revenue, 1) FROM sales ORDER BY month"
    - "SELECT s1.month, s1.revenue - s2.revenue AS mom_change FROM sales s1 JOIN sales s2 ON s1.month = s2.month + 1"
    - "SELECT month, revenue - FIRST_VALUE(revenue) OVER (ORDER BY month) AS mom_change FROM sales"
  answer: 0
  explanation: "LAG(revenue, 1) OVER (ORDER BY month) returns the revenue from the preceding row in the ordered window, so subtracting it gives the month-over-month change in a single, readable expression. Option B omits the OVER clause, which makes LAG syntactically invalid — LAG is a window function and requires OVER. Option C is the old self-join pattern that LAG replaces; it is more verbose and harder to read. Option D subtracts the very first row's revenue, giving change from the start rather than from the prior month."

- question: "A query uses LAST_VALUE(price) OVER (PARTITION BY product ORDER BY sale_date). What does this return on each row with the default window frame?"
  type: multiple-choice
  options:
    - "The price from the very last sale of that product"
    - "The price from the very first sale of that product"
    - "The price from the current row itself"
    - "NULL, because LAST_VALUE requires an explicit frame"
  answer: 2
  explanation: "This is the most common LAST_VALUE gotcha. The default window frame is ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW — it only includes rows from the start of the partition up to the current row. So LAST_VALUE of that frame is always the current row's own value. To get the actual last row of the partition, you must explicitly extend the frame: ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING. This is why FIRST_VALUE works intuitively with the default frame (the first row in the partition is always in the frame) but LAST_VALUE does not."

- question: "When a partition boundary is crossed, LAG returns NULL (or the specified default) rather than looking into the previous partition."
  type: true-false
  answer: true
  explanation: "PARTITION BY resets the window for each group. LAG navigating backward stops at the partition boundary — there is no 'previous row' for the first row of each partition, so LAG returns NULL (or the default value if you specify one as the third argument). This is by design: comparing January's revenue to December's makes sense within a single product or region, but mixing data across partitions would produce nonsensical results. The partition acts as a logical fence that confines row navigation."

- question: "LEAD and LAG are equivalent to window-aggregate functions like SUM OVER — they compute a value derived from all rows in the window frame."
  type: true-false
  answer: false
  explanation: "LAG and LEAD are offset functions, not aggregate functions. They access a specific row at a fixed offset from the current row (the previous row, the next row, or the nth row back/forward), returning that row's column value directly. Aggregate window functions like SUM, AVG, and COUNT compute a summary statistic across all rows in the window frame. The distinction matters: LAG returns a raw value from a specific row, while SUM returns a computed value derived from many rows. Offset functions do not respect window frame specifications the same way aggregates do."

- question: "Why did SQL need LAG and LEAD at all? What was the alternative before window functions, and what problem does the new approach solve?"
  type: short-answer
  answer: "Before LAG and LEAD, comparing a row to its neighbor required a self-join — joining the table to itself on an offset key (e.g., ON s1.month = s2.month - 1). LAG and LEAD replace this with a single expression inside a window function, eliminating the join, improving readability, and handling edge cases like missing rows or partition boundaries more cleanly."
  explanation: "The self-join approach requires knowing the key offset explicitly, fails gracefully only with careful NULL handling, and becomes difficult to read when multiple offsets are needed. LAG(revenue, 1, 0) in a single SELECT line communicates the intent directly: 'the previous row's revenue, defaulting to 0 if there is no previous row.' For sequential analysis — trends, differences, growth rates — offset functions turn a two-table join problem into a one-pass windowed scan."
```

## Explainer

From your introduction to window functions, you know that OVER defines a window of related rows and that window functions compute values across that window without collapsing the result set. LAG, LEAD, and related offset functions solve a specific problem that is awkward without them: accessing a value from a different row in the same result set. Before window functions existed, computing "this month's revenue minus last month's revenue" required a self-join — joining the table to itself on an offset date. LAG and LEAD replace that pattern with a single, readable expression.

**LAG(column, offset, default)** looks backward. Given rows ordered by some column, `LAG(revenue, 1)` on each row returns the revenue from the previous row. The offset defaults to 1 but can be any positive integer — `LAG(revenue, 3)` looks three rows back. The optional third argument provides a default when there is no previous row (the first row in the window has nothing to look back at, so without a default you get NULL). **LEAD** is the mirror: `LEAD(revenue, 1)` looks one row forward. Together they let you compute differences, growth rates, and trends in a single pass: `revenue - LAG(revenue, 1) OVER (ORDER BY month)` gives you month-over-month change on every row.

**FIRST_VALUE** and **LAST_VALUE** access the first or last row within the current window frame rather than at a fixed offset. `FIRST_VALUE(price) OVER (PARTITION BY product ORDER BY sale_date)` gives you the earliest recorded price for each product, repeated on every row — useful for computing how far the current price has moved from its starting point. LAST_VALUE requires care: the default frame is `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`, so LAST_VALUE just returns the current row's value. To get the actual last row in the partition, you need to extend the frame: `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`. **NTH_VALUE(column, n)** generalizes this further, returning the value from the nth row in the frame.

The key mental model is that these functions turn a tabular result into something you can navigate positionally — forward, backward, or to specific landmarks — without restructuring the query. PARTITION BY resets the navigation for each group (so LAG across a partition boundary returns NULL or the default, not a value from a different group), and ORDER BY determines which direction "previous" and "next" mean. Any time you find yourself writing a self-join to compare a row with its neighbor, LAG or LEAD is almost certainly the cleaner solution.
