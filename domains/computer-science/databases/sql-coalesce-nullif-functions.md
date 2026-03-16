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

## Explainer

From your work with SELECT basics, you know that NULL represents missing or unknown data — and that NULL behaves strangely in comparisons (NULL = NULL is not true, it is NULL). In real-world databases, NULL values appear constantly: a customer has no middle name, an order has no shipping date yet, a sensor reading was not recorded. **COALESCE** and **NULLIF** are the two essential functions for handling these gaps cleanly in your queries.

**COALESCE** takes a list of expressions and returns the first one that is not NULL. Think of it as a fallback chain. For example, `COALESCE(mobile_phone, home_phone, work_phone, 'No phone on file')` walks through each column in order and returns the first actual value it finds. If all phone columns are NULL, it falls back to the literal string. This is enormously useful for providing default values in reports, merging columns with overlapping data, and preventing NULL from propagating through calculations. Without COALESCE, you would need nested CASE WHEN expressions to achieve the same result — far more verbose and harder to read.

**NULLIF** does the reverse job: it *creates* NULL values where you want them. `NULLIF(a, b)` returns NULL if a equals b, and returns a otherwise. The classic use case is preventing division-by-zero errors: `revenue / NULLIF(units_sold, 0)` converts a zero denominator to NULL, which makes the division result NULL rather than crashing the query. NULLIF is also useful for cleaning data — converting placeholder values like empty strings or sentinel values (like -1 or 9999) into proper NULLs so that aggregate functions like AVG and COUNT handle them correctly, since aggregates automatically skip NULL values.

The two functions complement each other in a natural workflow: use NULLIF to normalize messy data into proper NULLs, then use COALESCE to substitute meaningful defaults when presenting results. For example, `COALESCE(NULLIF(middle_name, ''), 'N/A')` first converts empty strings to NULL, then replaces NULL with 'N/A'. Mastering this pair gives you precise control over missing data without resorting to verbose conditional logic.
