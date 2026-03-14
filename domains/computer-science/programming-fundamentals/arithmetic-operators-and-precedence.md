---
id: arithmetic-operators-and-precedence
title: Arithmetic Operators and Operator Precedence
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: operators-and-expressions
  type: hard
- id: working-with-numbers-integers-floats
  type: soft
builds-toward:
- expressions-and-evaluation
- type-conversion-intro
tags:
- operators
- precedence
- expressions
stage: abstract-reasoning
status: draft
---

# Arithmetic Operators and Operator Precedence

## Core Idea
Operators (+, −, *, /, %) follow precedence rules: multiplication before addition, and parentheses override. Expression evaluation order affects results. Understanding precedence prevents logic errors and makes code more maintainable.

## How It's Best Learned
Evaluate expressions on paper with explicit rules, then verify with code; use parentheses liberally even when not required to clarify intent.

## Common Misconceptions
That operators always associate left-to-right (exponentiation is right-associative); that 2 + 3 * 4 equals 20 (it's 14); that % is only for percentages (it's modulo/remainder).
