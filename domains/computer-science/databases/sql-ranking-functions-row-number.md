---
id: sql-ranking-functions-row-number
title: 'Ranking Functions: ROW_NUMBER, RANK, DENSE_RANK'
domain: computer-science
course: databases
prerequisites:
- id: sql-window-functions-introduction
  type: hard
builds-toward:
- sql-lag-lead-offset-functions
tags:
- sql
- ranking
- window-functions
stage: formal-systems
status: draft
---

# Ranking Functions: ROW_NUMBER, RANK, DENSE_RANK

## Core Idea
ROW_NUMBER assigns unique sequential integers regardless of ties, RANK assigns the same number to tied rows and skips ranks, and DENSE_RANK also handles ties but does not skip ranks. Each serves different ranking semantics.

## How It's Best Learned
Create a query with tied values and apply each function to observe the differences, especially in the handling of gaps.

## Common Misconceptions
ROW_NUMBER always produces unique values even for ties; use RANK or DENSE_RANK to handle ties correctly. The ORDER BY in the OVER clause determines rank order.
