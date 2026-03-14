---
id: sql-coalesce-nullif-functions
title: 'COALESCE and NULLIF: NULL Handling Functions'
domain: computer-science
course: databases
prerequisites:
- id: sql-select-basics
  type: hard
builds-toward:
- sql-case-when-expressions
tags:
- sql
- null-handling
- functions
stage: formal-systems
status: draft
---

# COALESCE and NULLIF: NULL Handling Functions

## Core Idea
COALESCE returns the first non-NULL value from a list of arguments, while NULLIF returns NULL if two expressions are equal and otherwise returns the first expression. Both are essential for robust NULL handling in queries.

## How It's Best Learned
Practice COALESCE with multiple columns to provide default values, and use NULLIF to convert specific values to NULL for analysis.

## Common Misconceptions
COALESCE is not the same as ISNULL/IFNULL—it evaluates multiple columns sequentially. NULLIF only compares two values; use CASE for complex NULL logic.
