---
id: sql-distinct-eliminating-duplicates
title: 'DISTINCT: Eliminating Duplicate Rows'
domain: computer-science
course: databases
prerequisites:
- id: sql-select-basics
  type: hard
builds-toward:
- sql-group-aggregate-functions
tags:
- sql
- queries
- result-filtering
stage: formal-systems
status: draft
---

# DISTINCT: Eliminating Duplicate Rows

## Core Idea
The DISTINCT keyword removes duplicate rows from query results, keeping only unique combinations of the selected columns. It is useful for exploratory analysis to understand the range of values in a dataset.

## How It's Best Learned
Start with simple single-column DISTINCT queries, then apply it to multi-column selects to understand how uniqueness is determined.

## Common Misconceptions
DISTINCT does not affect the underlying data—it only filters the result set. Using DISTINCT with ORDER BY requires the ordering columns to be in the SELECT list (in some databases).
