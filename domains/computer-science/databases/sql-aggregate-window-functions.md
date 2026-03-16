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
status: draft
---

# Aggregate Window Functions: SUM, AVG, MIN, MAX OVER

## Core Idea
Aggregate functions (SUM, AVG, MIN, MAX) can operate as window functions, computing aggregates over a window of rows without collapsing the result set. Frame clauses control which rows are included in each window.

## How It's Best Learned
Practice with running totals and moving averages, varying the frame specification to understand cumulative vs. sliding windows.

## Common Misconceptions
Window aggregates do not reduce rows—every input row appears in output. The frame (ROWS BETWEEN) is relative to the current row and ordered by the ORDER BY clause.

## Explainer

You already know that window functions compute values across a set of rows related to the current row, and that the OVER clause defines the window. Aggregate window functions take the familiar aggregate functions you've used with GROUP BY — SUM, AVG, MIN, MAX, COUNT — and run them as window functions instead. The critical difference: GROUP BY collapses many rows into one summary row, while an aggregate window function keeps every row and attaches the computed value alongside it. Think of it as annotating each row with a summary of its neighborhood rather than replacing the neighborhood with a single number.

The simplest and most common use is a **running total**. Imagine a table of daily sales with columns `sale_date` and `amount`. Writing `SUM(amount) OVER (ORDER BY sale_date)` produces a cumulative sum: each row shows its own amount plus the sum of all preceding rows. The default frame when ORDER BY is specified is `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`, which is exactly what makes it cumulative. If you instead write `SUM(amount) OVER ()` with no ORDER BY and no frame, every row gets the grand total — useful when you want to compute each row's percentage of the whole, like `amount / SUM(amount) OVER ()`.

The **frame clause** is what gives aggregate window functions their real power. A **sliding window** — `ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING` — computes a 5-row moving average centered on the current row. A frame of `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` gives you a 7-day moving average over daily data. You can combine PARTITION BY with frames: `AVG(amount) OVER (PARTITION BY region ORDER BY sale_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)` computes a separate 7-day moving average for each region. The partition resets the window; the frame controls how much of the partition each row can see.

One subtlety worth internalizing: `ROWS` and `RANGE` frames behave differently with ties. `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` includes exactly the rows up to and including the current physical row. `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` includes all rows with ORDER BY values less than or equal to the current row's value — so if two rows share the same date, both see the same cumulative sum. For most analytic work, ROWS gives you the behavior you expect. Use RANGE when you specifically want ties to be treated as peers.
