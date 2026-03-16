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

## Explainer

You have learned to store values in variables and to distinguish between data types like integers, floats, and strings. **Operators** are the symbols that let you do things with those values — combine them, compare them, and build up complex calculations from simple parts. An **expression** is any combination of values, variables, and operators that the computer can evaluate to produce a single result. The expression `3 + 4` evaluates to `7`. The expression `age >= 18` evaluates to `true` or `false`. Even a lone variable like `x` is an expression — it evaluates to whatever value `x` currently holds.

**Arithmetic operators** work the way you expect from math: `+` adds, `-` subtracts, `*` multiplies, `/` divides. The one to watch carefully is division. In many languages, dividing two integers performs **integer division**, which truncates the result: `7 / 2` gives `3`, not `3.5`. If you want the decimal result, at least one operand must be a float: `7.0 / 2` gives `3.5`. The **modulo operator** `%` returns the remainder after division: `7 % 2` gives `1`, because 7 divided by 2 is 3 with a remainder of 1. Modulo is surprisingly useful — it is the standard way to check whether a number is even (`n % 2 == 0`), to cycle through a fixed range, or to wrap around indices.

**Comparison operators** produce boolean values. `==` checks equality, `!=` checks inequality, and `<`, `>`, `<=`, `>=` compare magnitude. The critical beginner trap is confusing `=` (assignment, which stores a value) with `==` (comparison, which tests equality). Writing `if (x = 5)` assigns 5 to `x` instead of checking whether `x` equals 5 — a bug that can be very difficult to spot because the program may still run without an error.

**Logical operators** — `and`, `or`, `not` (or `&&`, `||`, `!` in C-style languages) — combine boolean expressions. `and` is true only when both sides are true; `or` is true when at least one side is true; `not` inverts true to false and vice versa. A critical behavior is **short-circuit evaluation**: in `A and B`, if `A` is false, the computer skips evaluating `B` entirely because the result must be false regardless. Similarly, in `A or B`, if `A` is true, `B` is never evaluated. This is not just an optimization — it lets you write safe conditions like `if (x != 0 and 10 / x > 2)`, where the division only happens if `x` is nonzero. When multiple operators appear in one expression, **precedence rules** (which you know from order of operations in math) determine what gets evaluated first. Multiplication before addition, comparison before logic, and when in doubt, parentheses make the order explicit and the code readable.
