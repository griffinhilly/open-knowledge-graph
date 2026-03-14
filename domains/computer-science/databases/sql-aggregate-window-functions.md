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
