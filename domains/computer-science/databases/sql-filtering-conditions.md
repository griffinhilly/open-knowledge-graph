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
- sql-subqueries
tags:
- SQL
- WHERE
- filtering
- conditions
stage: formal-systems
status: validated
---

# SQL: WHERE Clause and Filtering

## Core Idea
The WHERE clause filters rows based on conditions using comparison operators (=, <, >, <=, >=, !=), logical operators (AND, OR, NOT), and range operators (BETWEEN, IN). Complex filtering is essential for extracting relevant data from large tables.

## How It's Best Learned
Practice writing WHERE clauses with progressively complex conditions—single conditions, AND/OR combinations, range filtering, string pattern matching using LIKE, and NULL checks.

## Questions

```yaml
- question: "You run SELECT * FROM users WHERE email = NULL expecting to retrieve all users without an email address. The query returns zero rows despite NULL values existing in the table. Why?"
  type: multiple-choice
  options:
    - "NULL is stored as an empty string, so you need WHERE email = '' instead"
    - "Nothing equals NULL — not even NULL itself — so = NULL never evaluates to true; you must use IS NULL"
    - "The = operator does not work on string columns; use LIKE instead"
    - "NULL values are filtered out before the WHERE clause is evaluated"
  answer: 1
  explanation: "In SQL's three-valued logic, any comparison involving NULL yields NULL (not true, not false). This means email = NULL evaluates to NULL for every row — including rows where email actually is NULL — so no rows pass the filter. IS NULL is the only correct test for missing values: it is explicitly designed to check for the absence of a value, not to compare values."

- question: "Given the condition WHERE a = 1 OR b = 2 AND c = 3, which rows does SQL return?"
  type: multiple-choice
  options:
    - "Rows where (a = 1 OR b = 2) AND c = 3"
    - "Rows where a = 1, OR rows where both b = 2 AND c = 3"
    - "Rows where all three conditions are true simultaneously"
    - "Rows where any one of a = 1, b = 2, or c = 3 is true"
  answer: 1
  explanation: "AND binds tighter than OR — the same precedence rule as multiplication over addition in arithmetic. So this parses as a = 1 OR (b = 2 AND c = 3). A row is returned if a = 1 regardless of b and c, OR if both b = 2 and c = 3 regardless of a. This precedence rule is a common source of subtle bugs; using explicit parentheses makes your intent clear and prevents misreads."

- question: "WHERE price BETWEEN 10 AND 50 includes rows where price equals exactly 10 or exactly 50."
  type: true-false
  answer: true
  explanation: "BETWEEN is inclusive on both endpoints. It is equivalent to WHERE price >= 10 AND price <= 50. This is worth memorizing because it is easy to assume BETWEEN is exclusive. When you need to exclude an endpoint, use explicit comparison operators instead."

- question: "WHERE status = NULL is equivalent to WHERE status IS NULL and both will correctly return rows where status has no value."
  type: true-false
  answer: false
  explanation: "WHERE status = NULL never returns any rows because = NULL always evaluates to NULL (unknown), not true. IS NULL is the only correct way to test for missing values in SQL. These two expressions look similar but behave completely differently, making NULL handling one of the most common sources of SQL bugs for new practitioners."

- question: "Why does WHERE column = NULL never return any rows, even when NULL values exist in that column?"
  type: short-answer
  answer: "SQL uses three-valued logic: expressions evaluate to true, false, or NULL. Any comparison with NULL — including NULL = NULL — evaluates to NULL, not true. The WHERE clause only keeps rows where the condition is true; a NULL result is treated the same as false and the row is discarded. Since email = NULL evaluates to NULL for every row (including those where email is NULL), no rows pass the filter. IS NULL is a special predicate that tests for the absence of a value rather than comparing it."
  explanation: "This is one of the most important SQL behaviors to internalize. NULL means 'unknown' — you can't know if an unknown value equals another value, including another unknown. The practical rule: always use IS NULL or IS NOT NULL when testing for missing data, never = NULL or != NULL."
```

## Explainer

You already know how to retrieve data with SELECT — but without filtering, every query returns every row in the table. The **WHERE clause** is how you tell the database which rows you actually want. It appears after the FROM clause and contains a condition that each row must satisfy to be included in the result. Rows where the condition evaluates to true are kept; rows where it evaluates to false or NULL are discarded.

The simplest filters use **comparison operators**: `=`, `<`, `>`, `<=`, `>=`, and `!=` (or `<>`). These work on numbers, strings, and dates as you would expect. For example, `WHERE salary > 50000` keeps only rows where the salary column exceeds 50,000. You can combine multiple conditions with **logical operators**: `AND` requires both conditions to be true, `OR` requires at least one, and `NOT` inverts a condition. Operator precedence matters here — AND binds tighter than OR, so `WHERE a = 1 OR b = 2 AND c = 3` means `a = 1 OR (b = 2 AND c = 3)`. Use parentheses to make your intent explicit and avoid subtle bugs.

Beyond simple comparisons, SQL provides specialized filtering operators that make common patterns concise. **BETWEEN** tests whether a value falls within a range (inclusive on both ends): `WHERE price BETWEEN 10 AND 50`. **IN** checks membership in a list: `WHERE status IN ('active', 'pending', 'review')` — cleaner than chaining multiple OR conditions. **LIKE** enables pattern matching on strings using `%` (any sequence of characters) and `_` (exactly one character): `WHERE name LIKE 'J%'` finds names starting with J. And critically, **IS NULL** and **IS NOT NULL** are the only correct ways to test for missing values — `WHERE email = NULL` does not work because nothing equals NULL, not even NULL itself.

As your filters grow more complex, readability becomes the main challenge. A WHERE clause with five ANDs, two ORs, and a NOT can be correct but incomprehensible. The habit of using parentheses to group related conditions, placing each major condition on its own line, and using IN or BETWEEN instead of long OR chains will serve you well. Remember that the database evaluates the WHERE clause for every row in the table (or after joins, for every row in the combined result), so understanding what your filter actually specifies — and testing it with small datasets first — prevents the common mistake of returning far too many or far too few rows.
