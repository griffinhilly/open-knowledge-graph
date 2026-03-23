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
status: validated
---

# COALESCE and NULLIF: NULL Handling Functions

## Core Idea
COALESCE returns the first non-NULL value from a list of arguments, while NULLIF returns NULL if two expressions are equal and otherwise returns the first expression. Both are essential for robust NULL handling in queries.

## How It's Best Learned
Practice COALESCE with multiple columns to provide default values, and use NULLIF to convert specific values to NULL for analysis.

## Common Misconceptions
COALESCE is not the same as ISNULL/IFNULL—it evaluates multiple columns sequentially. NULLIF only compares two values; use CASE for complex NULL logic.

## Questions

```yaml
- question: "A query calculates revenue per unit with the expression `revenue / units_sold`. When units_sold is 0, the query crashes. Which expression fixes this while preserving NULL to signal the undefined result?"
  type: multiple-choice
  options:
    - "CASE WHEN units_sold = 0 THEN 0 ELSE revenue / units_sold END"
    - "revenue / NULLIF(units_sold, 0)"
    - "COALESCE(revenue / units_sold, 0)"
    - "ISNULL(units_sold, 1)"
  answer: 1
  explanation: "NULLIF(units_sold, 0) converts zero to NULL, making the division result NULL rather than causing a divide-by-zero error. This is the idiomatic use case for NULLIF. Option A uses 0 as the fallback, which is semantically wrong — dividing by zero is undefined, not zero. Option C uses COALESCE around the division, but the division still crashes before COALESCE can catch anything. Option D uses ISNULL which is database-specific and only handles NULL, not zero."

- question: "A customer table has three phone columns: mobile_phone, home_phone, work_phone. Many customers have only one or two. You want a single 'best contact number' column returning whichever is available, or 'No contact' if all are NULL. Which expression is correct?"
  type: multiple-choice
  options:
    - "ISNULL(mobile_phone, home_phone)"
    - "COALESCE(mobile_phone, home_phone, work_phone, 'No contact')"
    - "NULLIF(mobile_phone, home_phone)"
    - "CASE WHEN mobile_phone IS NOT NULL THEN mobile_phone WHEN home_phone IS NOT NULL THEN home_phone ELSE work_phone END"
  answer: 1
  explanation: "COALESCE accepts any number of arguments and returns the first non-NULL value. Option B elegantly handles all three columns plus a literal fallback in one expression. Option A only checks two columns. Option C uses NULLIF, which does something entirely different (returning NULL when two values are equal). Option D is a valid CASE statement but verbose, and it drops work_phone in the final ELSE — illustrating why COALESCE is cleaner for fallback chains."

- question: "COALESCE(a, b) and NULLIF(a, b) are inverses: COALESCE handles the case where a IS NULL, and NULLIF handles the case where a IS NOT NULL."
  type: true-false
  answer: false
  explanation: "This is a seductive framing, but the functions are not inverses and don't work symmetrically. COALESCE(a, b) returns b when a is NULL and a otherwise — it handles a missing-value fallback. NULLIF(a, b) returns NULL when a EQUALS b (not when a is NULL) and returns a otherwise — it converts a specific value to NULL. The natural pairing is: use NULLIF to normalize bad data into proper NULLs, then use COALESCE to substitute defaults where NULLs appear. They complement each other in a pipeline, not as strict inverses."

- question: "COALESCE can accept more than two arguments and evaluates them in order, returning the first non-NULL value found."
  type: true-false
  answer: true
  explanation: "Unlike ISNULL or NVL (which are database-specific and accept exactly two arguments), COALESCE is SQL-standard and accepts an arbitrary number of arguments. It evaluates each in sequence and returns the first non-NULL. This makes it more versatile: COALESCE(col1, col2, col3, 'default') handles a multi-column fallback chain without nested function calls. The sequential evaluation also means you can combine columns and literals in any order."

- question: "Explain how COALESCE and NULLIF work together in data cleaning pipelines, giving a concrete example."
  type: short-answer
  answer: "NULLIF normalizes sentinel or placeholder values into proper NULLs; COALESCE then substitutes meaningful defaults where NULLs appear. For example: COALESCE(NULLIF(middle_name, ''), 'N/A') first converts empty strings to NULL (because some systems store missing names as '' rather than NULL), then replaces the NULL with 'N/A' for display. Without NULLIF, an empty string would satisfy COALESCE and appear as '' in results. Without COALESCE, the NULL from NULLIF would propagate. Together they give precise control over missing data."
  explanation: "The workflow is: (1) use NULLIF to convert dirty or sentinel values into proper NULLs so aggregate functions and comparisons handle them consistently; (2) use COALESCE at the output stage to substitute user-facing defaults. This separates concerns cleanly: normalization happens internally, presentation happens externally. The alternative — nested CASE WHEN expressions — achieves the same result but is far more verbose and harder to read at a glance."
```

## Explainer

From your work with SELECT basics, you know that NULL represents missing or unknown data — and that NULL behaves strangely in comparisons (NULL = NULL is not true, it is NULL). In real-world databases, NULL values appear constantly: a customer has no middle name, an order has no shipping date yet, a sensor reading was not recorded. **COALESCE** and **NULLIF** are the two essential functions for handling these gaps cleanly in your queries.

**COALESCE** takes a list of expressions and returns the first one that is not NULL. Think of it as a fallback chain. For example, `COALESCE(mobile_phone, home_phone, work_phone, 'No phone on file')` walks through each column in order and returns the first actual value it finds. If all phone columns are NULL, it falls back to the literal string. This is enormously useful for providing default values in reports, merging columns with overlapping data, and preventing NULL from propagating through calculations. Without COALESCE, you would need nested CASE WHEN expressions to achieve the same result — far more verbose and harder to read.

**NULLIF** does the reverse job: it *creates* NULL values where you want them. `NULLIF(a, b)` returns NULL if a equals b, and returns a otherwise. The classic use case is preventing division-by-zero errors: `revenue / NULLIF(units_sold, 0)` converts a zero denominator to NULL, which makes the division result NULL rather than crashing the query. NULLIF is also useful for cleaning data — converting placeholder values like empty strings or sentinel values (like -1 or 9999) into proper NULLs so that aggregate functions like AVG and COUNT handle them correctly, since aggregates automatically skip NULL values.

The two functions complement each other in a natural workflow: use NULLIF to normalize messy data into proper NULLs, then use COALESCE to substitute meaningful defaults when presenting results. For example, `COALESCE(NULLIF(middle_name, ''), 'N/A')` first converts empty strings to NULL, then replaces NULL with 'N/A'. Mastering this pair gives you precise control over missing data without resorting to verbose conditional logic.
