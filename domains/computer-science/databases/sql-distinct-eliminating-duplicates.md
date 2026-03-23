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
status: validated
---

# DISTINCT: Eliminating Duplicate Rows

## Core Idea
The DISTINCT keyword removes duplicate rows from query results, keeping only unique combinations of the selected columns. It is useful for exploratory analysis to understand the range of values in a dataset.

## How It's Best Learned
Start with simple single-column DISTINCT queries, then apply it to multi-column selects to understand how uniqueness is determined.

## Common Misconceptions
DISTINCT does not affect the underlying data—it only filters the result set. Using DISTINCT with ORDER BY requires the ordering columns to be in the SELECT list (in some databases).

## Questions

```yaml
- question: "A table has columns: first_name, last_name, department. Compared to SELECT DISTINCT first_name FROM employees, how will SELECT DISTINCT first_name, department FROM employees affect the row count?"
  type: multiple-choice
  options:
    - "It will decrease, since more filtering criteria are applied"
    - "It will stay the same, since first_name already determines uniqueness"
    - "It will increase or stay the same, since more column combinations can be unique"
    - "It will always exactly double, since department doubles the grouping dimensions"
  answer: 2
  explanation: "DISTINCT applies to the entire combination of selected columns, not a single column. Adding 'department' means two rows with the same first_name but different departments are now distinct — so the query can only return more rows, never fewer. The intuition that 'more conditions = fewer results' is backwards here: DISTINCT is about uniqueness of the whole row, not filtering down a column."

- question: "A JOIN between orders and customers is returning unexpected duplicate rows. A developer adds DISTINCT to the SELECT to fix it. What is the most likely underlying problem?"
  type: multiple-choice
  options:
    - "The orders table has corrupted data entries that need to be cleaned"
    - "A missing or incorrect join condition is causing unintended many-to-many matches"
    - "DISTINCT is being applied before the WHERE clause, producing wrong results"
    - "The database engine is not correctly processing the specified join type"
  answer: 1
  explanation: "When a JOIN produces unexpected duplicates, the root cause is almost always a query logic error: a missing join condition, joining on a non-unique column, or an unintended many-to-many relationship. Adding DISTINCT hides the symptom without fixing the cause. The correct response is to diagnose why duplicates appear and fix the join logic — otherwise the band-aid may mask a deeper data integrity issue."

- question: "SELECT DISTINCT city, state FROM customers can return more rows than SELECT DISTINCT city FROM the same table."
  type: true-false
  answer: true
  explanation: "DISTINCT deduplicates based on the entire selected row. Two rows with the same city but different states (Portland, OR and Portland, ME) are distinct when both columns are selected, but collapse to one row when only city is selected. Adding columns to a DISTINCT query generally increases the number of distinct combinations, because there are more ways for rows to differ."

- question: "The DISTINCT keyword modifies the underlying table data by permanently removing duplicate rows."
  type: true-false
  answer: false
  explanation: "DISTINCT only affects the query result set — it has zero effect on stored data. The underlying table is completely unchanged. DISTINCT is a presentation filter applied when producing output. To permanently remove duplicates from a table, you would need DELETE statements with deduplication logic, not a SELECT DISTINCT."

- question: "When should you be suspicious that DISTINCT is hiding a bug rather than solving a legitimate problem?"
  type: short-answer
  answer: "When duplicates appear after a JOIN and you're adding DISTINCT to make them go away. Legitimate DISTINCT uses are exploratory (what unique values exist in this column?) or when the query design inherently produces one value per combination. But JOIN-produced duplicates should trigger the question: why are these duplicates appearing? A missing join condition or unintended many-to-many relationship is the usual culprit, and fixing the JOIN logic is the correct solution."
  explanation: "DISTINCT is a tool for asking 'what unique values exist?', not a general-purpose deduplication patch. Using it to suppress JOIN duplicates is an antipattern: it hides a query logic error, masks potential data integrity problems, and adds unnecessary performance cost (the database must hash or sort the entire result set to identify duplicates)."
```

## Explainer

When you run a SELECT query, the result set can contain duplicate rows — especially after joins or when selecting a subset of columns. If you select just the `city` column from a million-row customer table, you might get the same city name thousands of times. **DISTINCT** tells the database to collapse these duplicates, returning only one row for each unique combination of values in your selected columns.

The key insight is that DISTINCT operates on the **entire row** of your result set, not on a single column. If you write `SELECT DISTINCT city, state FROM customers`, a row is considered a duplicate only if both the city and state match. Portland, Oregon and Portland, Maine are distinct rows even though the city name is the same. This means adding more columns to a DISTINCT query generally produces more rows, not fewer, because there are more ways for combinations to be unique.

DISTINCT is most valuable during **exploratory analysis** — when you want to understand what values exist in a column before writing more complex queries. "What departments do we have?" (`SELECT DISTINCT department FROM employees`) or "Which product-category combinations exist?" are natural DISTINCT questions. It is also useful for quick sanity checks: if `SELECT COUNT(*)` returns 10,000 rows but `SELECT COUNT(DISTINCT customer_id)` returns only 8,500, you know some customers appear multiple times.

A common antipattern is using DISTINCT as a band-aid to hide a query bug. If a JOIN produces unexpected duplicates, slapping DISTINCT on the SELECT hides the symptom without fixing the cause — usually a missing join condition or an unintended many-to-many relationship. When you find yourself reaching for DISTINCT to "fix" duplicate rows, pause and ask whether the duplicates indicate a problem in your query logic rather than a legitimate need for deduplication. Also be aware that DISTINCT has a performance cost: the database must sort or hash the entire result set to identify duplicates, which can be expensive on large datasets.
