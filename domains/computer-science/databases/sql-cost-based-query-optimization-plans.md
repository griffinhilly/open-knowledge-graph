---
id: sql-cost-based-query-optimization-plans
title: Cost-Based Query Optimization and Execution Plan Selection
domain: computer-science
course: databases
prerequisites:
- id: query-optimization
  type: hard
- id: query-cardinality-selectivity-estimation
  type: hard
- id: query-execution-plans
  type: hard
builds-toward:
- query-execution-plan-analysis-explain
tags:
- optimization
- cost-model
- plan-selection
stage: formal-systems
status: draft
---

# Cost-Based Query Optimization and Execution Plan Selection

## Core Idea
Query optimizers estimate CPU and I/O costs for different execution plans using cardinality estimates and cost functions, then select the lowest-cost plan. Cost functions account for sequential scans, index lookups, join algorithms, and sorting. The optimizer explores alternative join orders and strategies, applying heuristics to prune the search space. Modern optimizers use dynamic programming or genetic algorithms for large search spaces.
