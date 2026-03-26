---
id: sql-case-when-expressions
title: 'CASE WHEN: Conditional Expressions in SQL'
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
builds-toward:
- sql-update-with-joins
- sql-window-functions-introduction
tags:
- sql
- conditional-logic
- data-transformation
stage: formal-systems
status: validated
---

# CASE WHEN: Conditional Expressions in SQL

## Core Idea
CASE WHEN allows conditional branching in SELECT, UPDATE, and other SQL statements, returning different values based on evaluated conditions. It provides SQL the ability to perform if-then-else logic.

## How It's Best Learned
Begin with simple two-branch CASE expressions, then progress to multi-condition CASE with ELSE clauses and nested CASE statements.

## Common Misconceptions
CASE evaluates conditions sequentially and stops at the first match—later conditions are not evaluated. The ELSE clause is optional and defaults to NULL if no condition matches.

## Questions

```yaml
- question: "A developer writes: CASE WHEN score >= 70 THEN 'C' WHEN score >= 80 THEN 'B' WHEN score >= 90 THEN 'A' ELSE 'F' END. A student with score 95 receives which grade?"
  type: multiple-choice
  options:
    - "'A' — the highest matching condition wins"
    - "'C' — the first true condition (95 >= 70) is returned and evaluation stops"
    - "'F' — no condition matches because evaluation happens in reverse order"
    - "NULL — multiple conditions are simultaneously true, producing a conflict"
  answer: 1
  explanation: "CASE evaluates conditions top-to-bottom and returns the result of the FIRST true condition. Since 95 >= 70 is true, it returns 'C' immediately — it never evaluates the later conditions. This is the classic ordering mistake: to work correctly, conditions must go from most specific (>= 90) to least specific (>= 70), not the other way around."

- question: "A query calculates `price * CASE WHEN discount_eligible THEN 0.9 END` with no ELSE clause. For rows where discount_eligible is false, this expression evaluates to:"
  type: multiple-choice
  options:
    - "price * 1.0 — CASE defaults to 1 when no ELSE is provided"
    - "price * 0 — CASE returns 0 when no condition matches"
    - "NULL — CASE with no matching branch returns NULL, and NULL in arithmetic produces NULL"
    - "An error — SQL raises an exception when CASE has no matching branch"
  answer: 2
  explanation: "When no WHEN condition matches and no ELSE clause is present, CASE silently returns NULL. Any arithmetic involving NULL produces NULL — so `price * NULL = NULL`, not price. This is a common bug: the developer intended non-eligible rows to keep their full price, but gets NULL instead. Adding ELSE 1.0 is the fix. SQL never raises an error for a CASE with no match — the NULL behavior is silent and easy to miss."

- question: "A CASE expression evaluates most its WHEN conditions for nearly every row, even after finding the first true condition."
  type: true-false
  answer: false
  explanation: "CASE uses short-circuit evaluation: it stops at the first true WHEN condition and returns that result without evaluating subsequent conditions. This is why condition order matters — and also means later conditions can assume earlier ones were false. For example, in a grade-assigning CASE ordered correctly (>= 90, >= 80, >= 70), the '>= 80' branch implicitly handles scores in 80-89, because any score >= 90 was already caught by the first branch."

- question: "CASE WHEN can primarily appear in the SELECT list of a query, not inside aggregate functions or ORDER BY clauses."
  type: true-false
  answer: false
  explanation: "CASE is a general expression that can appear anywhere an expression is valid in SQL: in SELECT, ORDER BY, GROUP BY, HAVING, and inside aggregate functions. A particularly powerful pattern is using CASE inside aggregates — e.g., SUM(CASE WHEN status = 'paid' THEN amount ELSE 0 END) — to produce conditional totals from a single table scan. CASE can also appear in UPDATE SET clauses to conditionally modify values."

- question: "You need a single query against an orders table that returns three counts in one row: how many orders are 'pending', how many are 'paid', and how many are 'cancelled'. How would you use CASE WHEN to accomplish this?"
  type: short-answer
  answer: "SELECT SUM(CASE WHEN status = 'pending' THEN 1 ELSE 0 END) AS pending_count, SUM(CASE WHEN status = 'paid' THEN 1 ELSE 0 END) AS paid_count, SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) AS cancelled_count FROM orders"
  explanation: "This technique — sometimes called conditional aggregation — uses CASE inside SUM (or COUNT) to count rows that meet each condition. Each CASE returns 1 when the condition is true and 0 otherwise; SUM then accumulates the count. This performs a single pass over the table rather than three separate queries, and is the standard SQL pattern for pivoting categorical data into columns."
```

## Explainer

You already know how to select and filter data with SELECT and WHERE. But sometimes you need to transform values conditionally — not just retrieve them, but reclassify, bucket, or label them based on rules. **CASE WHEN** gives SQL the equivalent of if-then-else logic, letting you produce new computed values inline within a query.

The basic structure reads almost like English: `CASE WHEN condition THEN result WHEN condition THEN result ELSE default END`. For example, if you have a table of exam scores and want to assign letter grades, you would write `CASE WHEN score >= 90 THEN 'A' WHEN score >= 80 THEN 'B' WHEN score >= 70 THEN 'C' ELSE 'F' END AS grade`. The database evaluates conditions top to bottom and returns the result for the **first** match. This sequential evaluation matters — if you accidentally put `score >= 70` before `score >= 90`, every score above 70 would get a 'C' because the engine stops at the first true condition.

CASE expressions are not limited to SELECT lists. You can use them inside ORDER BY to create custom sort orders (sort active users before inactive ones), inside GROUP BY to bucket rows into categories before aggregating, and inside UPDATE statements to conditionally change values. A particularly powerful pattern is combining CASE with aggregate functions: `SUM(CASE WHEN status = 'paid' THEN amount ELSE 0 END)` gives you a conditional sum, effectively pivoting rows into columns without restructuring your query.

One subtlety to watch: if no condition matches and you omit the ELSE clause, the result is NULL — not an error, not zero, just NULL. This silent default catches people off guard when they use CASE inside arithmetic expressions, since any operation involving NULL produces NULL. Adding an explicit ELSE clause, even when you think every case is covered, is a defensive habit that prevents unexpected NULLs from propagating through your results.
