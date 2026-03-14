---
id: query-cardinality-selectivity-estimation
title: Query Cardinality and Selectivity Estimation
domain: computer-science
course: databases
prerequisites:
- id: query-optimization
  type: hard
- id: sql-filtering-conditions
  type: hard
builds-toward:
- sql-cost-based-query-optimization
- table-statistics-histogram
tags:
- cardinality
- selectivity
- estimation
- cost-model
stage: formal-systems
status: draft
---

# Query Cardinality and Selectivity Estimation

## Core Idea
Cardinality estimation predicts how many rows result from query operations to guide optimizer decisions. Selectivity is the fraction of rows passing a condition (e.g., age > 18 might have selectivity 0.3). The optimizer combines estimates from individual operations and uses data distribution statistics. Accurate estimates are critical for good plan selection; errors of 2-3x are common but errors of 100x+ cause terrible plans.
