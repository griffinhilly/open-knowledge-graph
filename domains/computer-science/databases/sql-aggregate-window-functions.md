---
id: sql-aggregate-window-functions
title: 'Aggregate Window Functions: SUM, AVG, MIN, MAX OVER'
domain: computer-science
course: databases
prerequisites:
- id: sql-window-functions-introduction
  type: hard
builds-toward:
- sql-lag-lead-offset-functions
tags:
- sql
- aggregation
- window-functions
stage: formal-systems
status: validated
---

# Aggregate Window Functions: SUM, AVG, MIN, MAX OVER

## Core Idea
Aggregate functions (SUM, AVG, MIN, MAX) can operate as window functions, computing aggregates over a window of rows without collapsing the result set. Frame clauses control which rows are included in each window.

## How It's Best Learned
Practice with running totals and moving averages, varying the frame specification to understand cumulative vs. sliding windows.

## Common Misconceptions
Window aggregates do not reduce rows—every input row appears in output. The frame (ROWS BETWEEN) is relative to the current row and ordered by the ORDER BY clause.

## Questions

```yaml
- question: "You want each row in a sales table to show the salesperson's amount AND their region's total for that month, without losing any rows. Which query structure achieves this?"
  type: multiple-choice
  options:
    - "SELECT salesperson, month, amount, SUM(amount) OVER (PARTITION BY region, month) AS region_total FROM sales"
    - "SELECT salesperson, month, amount, SUM(amount) FROM sales GROUP BY region, month"
    - "SELECT salesperson, month, SUM(amount) OVER (ORDER BY month) AS region_total FROM sales"
    - "SELECT salesperson, month, amount FROM sales JOIN (SELECT region, month, SUM(amount) AS region_total FROM sales GROUP BY region, month) t USING (region, month)"
  answer: 0
  explanation: "A window function with PARTITION BY region, month computes the regional monthly total and attaches it to every row without collapsing anything. Option B uses GROUP BY, which collapses the result to one row per (region, month) — the individual salesperson rows are gone. Option C omits PARTITION BY region, so it would compute a cumulative sum across all regions. Option D works but is unnecessarily complex compared to the clean window function approach. The key insight is that window functions annotate rows; GROUP BY replaces them."

- question: "You write SUM(amount) OVER (ORDER BY sale_date) to compute a running total. A colleague warns you that two rows with the same sale_date will produce unexpected results. Why might they be right?"
  type: multiple-choice
  options:
    - "ORDER BY in a window function is not allowed without PARTITION BY"
    - "When ORDER BY is specified, the default frame is RANGE-based, meaning rows tied on sale_date all receive the same cumulative value — the sum up to and including all rows with that date"
    - "Window functions process rows in random order when there are ties, so results are non-deterministic"
    - "The default frame excludes the current row, so tied dates are double-counted"
  answer: 1
  explanation: "The default frame when ORDER BY is specified uses RANGE semantics: RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW. With RANGE, 'current row' means all rows with the same ORDER BY value — so all rows sharing the same sale_date are treated as peers and all receive the cumulative sum that includes every row up to that date. If you want each physical row to have its own incremental value regardless of ties, specify ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW explicitly."

- question: "SUM(amount) OVER () with no ORDER BY and no frame clause returns the grand total for every row in the result set."
  type: true-false
  answer: true
  explanation: "With no PARTITION BY and no ORDER BY, the window covers the entire result set for every row. This means SUM(amount) OVER () attaches the grand total to each row. This is useful for computing percentages: amount / SUM(amount) OVER () gives each row's share of the total without a self-join or subquery."

- question: "ROWS BETWEEN 3 PRECEDING AND CURRENT ROW and ROWS BETWEEN 3 PRECEDING AND 3 FOLLOWING both compute a 7-row moving average."
  type: true-false
  answer: false
  explanation: "ROWS BETWEEN 3 PRECEDING AND CURRENT ROW includes 4 rows (3 before + current), not 7. ROWS BETWEEN 3 PRECEDING AND 3 FOLLOWING includes 7 rows (3 before + current + 3 after). For a 7-row moving average centered on the current row, use ROWS BETWEEN 3 PRECEDING AND 3 FOLLOWING. For a 7-row trailing average (current row plus 6 previous), use ROWS BETWEEN 6 PRECEDING AND CURRENT ROW."

- question: "Explain what the frame clause ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING does in a window function, and describe one real-world analytic use case where this frame specification would be appropriate."
  type: short-answer
  answer: "The frame includes the 2 rows before, the current row, and the 2 rows after — a 5-row centered window. Each row's aggregate is computed over this symmetric neighborhood."
  explanation: "A centered moving window smooths out short-term spikes while preserving the trend. A use case: computing a 5-day centered moving average of daily stock prices to reduce noise while keeping the trend aligned in time (not lagged). Another use: anomaly detection — if a row's value deviates greatly from the 5-row centered average, it may be an outlier. The contrast with a trailing window (PRECEDING AND CURRENT ROW) is that a centered window doesn't introduce lag, making it better for visualization but unavailable in real-time streaming contexts where future rows don't exist yet."
```

## Explainer

You already know that window functions compute values across a set of rows related to the current row, and that the OVER clause defines the window. Aggregate window functions take the familiar aggregate functions you've used with GROUP BY — SUM, AVG, MIN, MAX, COUNT — and run them as window functions instead. The critical difference: GROUP BY collapses many rows into one summary row, while an aggregate window function keeps every row and attaches the computed value alongside it. Think of it as annotating each row with a summary of its neighborhood rather than replacing the neighborhood with a single number.

The simplest and most common use is a **running total**. Imagine a table of daily sales with columns `sale_date` and `amount`. Writing `SUM(amount) OVER (ORDER BY sale_date)` produces a cumulative sum: each row shows its own amount plus the sum of all preceding rows. The default frame when ORDER BY is specified is `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`, which is exactly what makes it cumulative. If you instead write `SUM(amount) OVER ()` with no ORDER BY and no frame, every row gets the grand total — useful when you want to compute each row's percentage of the whole, like `amount / SUM(amount) OVER ()`.

The **frame clause** is what gives aggregate window functions their real power. A **sliding window** — `ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING` — computes a 5-row moving average centered on the current row. A frame of `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` gives you a 7-day moving average over daily data. You can combine PARTITION BY with frames: `AVG(amount) OVER (PARTITION BY region ORDER BY sale_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)` computes a separate 7-day moving average for each region. The partition resets the window; the frame controls how much of the partition each row can see.

One subtlety worth internalizing: `ROWS` and `RANGE` frames behave differently with ties. `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` includes exactly the rows up to and including the current physical row. `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` includes all rows with ORDER BY values less than or equal to the current row's value — so if two rows share the same date, both see the same cumulative sum. For most analytic work, ROWS gives you the behavior you expect. Use RANGE when you specifically want ties to be treated as peers.
