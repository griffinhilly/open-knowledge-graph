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
