---
id: comparison-operators-and-boolean-tests
title: Comparison Operators and Boolean Tests
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: operators-and-expressions
  type: hard
- id: boolean-logic-programming
  type: hard
builds-toward:
- if-else-branching-logic
- conditional-logic-chains
tags:
- comparison
- boolean
- logic
stage: abstract-reasoning
status: draft
---

# Comparison Operators and Boolean Tests

## Core Idea
Comparison operators (<, >, ==, !=, <=, >=) return boolean values (true or false). These form the basis of conditional logic. Subtle differences exist: = (assignment) vs == (comparison) is a common source of bugs.

## How It's Best Learned
Build truth tables for comparisons; test edge cases like comparing strings and numbers; deliberately write == instead of = to feel the error.

## Common Misconceptions
That = and == are interchangeable; that comparison of strings is lexicographic not alphabetic (issues with case sensitivity); that 5 == '5' is true (it's false in typed languages).
