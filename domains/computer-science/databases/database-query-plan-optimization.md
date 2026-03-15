---
id: database-query-plan-optimization
title: 'Query Plan Optimization: Choosing Execution Strategies'
domain: computer-science
course: databases
prerequisites:
- id: query-execution-plans
  type: hard
- id: optimization-multivariable-basics
  type: soft
tags:
- query-optimization
- performance
- cost-based-optimization
stage: formal-systems
status: draft
---

# Query Plan Optimization: Choosing Execution Strategies

## Core Idea
Query optimizers choose among multiple execution plans based on cost estimates (I/O, CPU, memory). The optimizer uses table statistics and heuristics to minimize estimated cost.

## How It's Best Learned
Use EXPLAIN ANALYZE to view actual plans, modify indexes, and re-run EXPLAIN to see how costs and row counts change.

## Common Misconceptions
The optimizer's choice is based on estimated costs, which can be inaccurate if statistics are stale. Cost-based optimization is not guaranteed to find the global optimum.
