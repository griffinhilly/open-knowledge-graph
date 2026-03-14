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
