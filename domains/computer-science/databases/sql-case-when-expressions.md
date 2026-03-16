---
id: sql-case-when-expressions
title: 'CASE WHEN: Conditional Expressions in SQL'
domain: computer-science
course: databases
prerequisites:
- id: sql-select-basics
  type: hard
builds-toward:
- sql-update-with-joins
- sql-aggregate-window-functions
tags:
- sql
- conditional-logic
- data-transformation
stage: formal-systems
status: draft
---

# CASE WHEN: Conditional Expressions in SQL

## Core Idea
CASE WHEN allows conditional branching in SELECT, UPDATE, and other SQL statements, returning different values based on evaluated conditions. It provides SQL the ability to perform if-then-else logic.

## How It's Best Learned
Begin with simple two-branch CASE expressions, then progress to multi-condition CASE with ELSE clauses and nested CASE statements.

## Common Misconceptions
CASE evaluates conditions sequentially and stops at the first match—later conditions are not evaluated. The ELSE clause is optional and defaults to NULL if no condition matches.

## Explainer

You already know how to select and filter data with SELECT and WHERE. But sometimes you need to transform values conditionally — not just retrieve them, but reclassify, bucket, or label them based on rules. **CASE WHEN** gives SQL the equivalent of if-then-else logic, letting you produce new computed values inline within a query.

The basic structure reads almost like English: `CASE WHEN condition THEN result WHEN condition THEN result ELSE default END`. For example, if you have a table of exam scores and want to assign letter grades, you would write `CASE WHEN score >= 90 THEN 'A' WHEN score >= 80 THEN 'B' WHEN score >= 70 THEN 'C' ELSE 'F' END AS grade`. The database evaluates conditions top to bottom and returns the result for the **first** match. This sequential evaluation matters — if you accidentally put `score >= 70` before `score >= 90`, every score above 70 would get a 'C' because the engine stops at the first true condition.

CASE expressions are not limited to SELECT lists. You can use them inside ORDER BY to create custom sort orders (sort active users before inactive ones), inside GROUP BY to bucket rows into categories before aggregating, and inside UPDATE statements to conditionally change values. A particularly powerful pattern is combining CASE with aggregate functions: `SUM(CASE WHEN status = 'paid' THEN amount ELSE 0 END)` gives you a conditional sum, effectively pivoting rows into columns without restructuring your query.

One subtlety to watch: if no condition matches and you omit the ELSE clause, the result is NULL — not an error, not zero, just NULL. This silent default catches people off guard when they use CASE inside arithmetic expressions, since any operation involving NULL produces NULL. Adding an explicit ELSE clause, even when you think every case is covered, is a defensive habit that prevents unexpected NULLs from propagating through your results.
