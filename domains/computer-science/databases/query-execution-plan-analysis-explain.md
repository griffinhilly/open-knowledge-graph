---
id: query-execution-plan-analysis-explain
title: Query Execution Plans and EXPLAIN Analysis
domain: computer-science
course: databases
prerequisites:
- id: query-execution-plans
  type: hard
- id: sql-cost-based-query-optimization-plans
  type: hard
tags:
- EXPLAIN
- execution-plan
- analysis
- optimization
stage: formal-systems
status: draft
---

# Query Execution Plans and EXPLAIN Analysis

## Core Idea
The EXPLAIN statement displays the optimizer's chosen execution plan, showing operations (Seq Scan, Index Scan, Join) with estimated row counts, costs, and timing. Analyzing EXPLAIN output reveals whether the optimizer made good decisions and identifies bottlenecks like full table scans or inefficient joins. Discrepancies between estimated and actual row counts indicate poor statistics. Understanding plan interpretation is essential for query tuning.
