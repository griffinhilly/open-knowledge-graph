---
id: sql-filtering-conditions
title: 'SQL: WHERE Clause and Filtering'
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
builds-toward:
- sql-sorting-limiting-results
- sql-subquery-fundamentals
tags:
- SQL
- WHERE
- filtering
- conditions
stage: formal-systems
status: draft
---

# SQL: WHERE Clause and Filtering

## Core Idea
The WHERE clause filters rows based on conditions using comparison operators (=, <, >, <=, >=, !=), logical operators (AND, OR, NOT), and range operators (BETWEEN, IN). Complex filtering is essential for extracting relevant data from large tables.

## How It's Best Learned
Practice writing WHERE clauses with progressively complex conditions—single conditions, AND/OR combinations, range filtering, string pattern matching using LIKE, and NULL checks.

## Explainer

You already know how to retrieve data with SELECT — but without filtering, every query returns every row in the table. The **WHERE clause** is how you tell the database which rows you actually want. It appears after the FROM clause and contains a condition that each row must satisfy to be included in the result. Rows where the condition evaluates to true are kept; rows where it evaluates to false or NULL are discarded.

The simplest filters use **comparison operators**: `=`, `<`, `>`, `<=`, `>=`, and `!=` (or `<>`). These work on numbers, strings, and dates as you would expect. For example, `WHERE salary > 50000` keeps only rows where the salary column exceeds 50,000. You can combine multiple conditions with **logical operators**: `AND` requires both conditions to be true, `OR` requires at least one, and `NOT` inverts a condition. Operator precedence matters here — AND binds tighter than OR, so `WHERE a = 1 OR b = 2 AND c = 3` means `a = 1 OR (b = 2 AND c = 3)`. Use parentheses to make your intent explicit and avoid subtle bugs.

Beyond simple comparisons, SQL provides specialized filtering operators that make common patterns concise. **BETWEEN** tests whether a value falls within a range (inclusive on both ends): `WHERE price BETWEEN 10 AND 50`. **IN** checks membership in a list: `WHERE status IN ('active', 'pending', 'review')` — cleaner than chaining multiple OR conditions. **LIKE** enables pattern matching on strings using `%` (any sequence of characters) and `_` (exactly one character): `WHERE name LIKE 'J%'` finds names starting with J. And critically, **IS NULL** and **IS NOT NULL** are the only correct ways to test for missing values — `WHERE email = NULL` does not work because nothing equals NULL, not even NULL itself.

As your filters grow more complex, readability becomes the main challenge. A WHERE clause with five ANDs, two ORs, and a NOT can be correct but incomprehensible. The habit of using parentheses to group related conditions, placing each major condition on its own line, and using IN or BETWEEN instead of long OR chains will serve you well. Remember that the database evaluates the WHERE clause for every row in the table (or after joins, for every row in the combined result), so understanding what your filter actually specifies — and testing it with small datasets first — prevents the common mistake of returning far too many or far too few rows.
