---
id: operators-and-expressions
title: Operators and Expressions
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: variables-and-assignment
  type: hard
- id: primitive-data-types
  type: hard
- id: order-of-operations
  type: soft
builds-toward:
- conditional-statements
- type-conversion
- string-operations
tags:
- operators
- arithmetic
- comparison
- expressions
- precedence
stage: abstract-reasoning
status: validated
---

# Operators and Expressions

## Core Idea
Operators combine values and variables into expressions that evaluate to a result. Arithmetic operators (+, -, *, /, %) perform math; comparison operators (==, !=, <, >) produce booleans; logical operators (and, or, not) combine boolean expressions. Operator precedence rules determine the order of evaluation when multiple operators appear together. Every expression has a type determined by its operands and operator.

## How It's Best Learned
Evaluate expressions by hand first, then verify in a REPL. Pay particular attention to integer vs. float division and short-circuit evaluation in logical expressions.

## Common Misconceptions
- Forgetting that == tests equality while = assigns.
- Misunderstanding integer division truncation.
- Assuming logical operators always evaluate both sides (they short-circuit).
