---
id: arithmetic-operators-intro
title: Arithmetic Operators and Operations
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: integer-and-floating-point-types
  type: hard
builds-toward:
- operator-precedence-and-evaluation
tags:
- operators
- arithmetic
- math
stage: abstract-reasoning
status: draft
---

# Arithmetic Operators and Operations

## Core Idea
Arithmetic operators (+, −, *, /, %) perform mathematical calculations on numbers. Each operator has well-defined semantics; integer division differs from floating-point division, and modulo returns the remainder.

## How It's Best Learned
Compute arithmetic expressions by hand, then verify with code. Test integer vs. float division to see the difference.

## Common Misconceptions
- Integer division truncates (it floors the result toward zero or negative infinity, depending on the language).
- All divisions produce the same result (integer and float division differ fundamentally).

## Explainer

Now that you understand the difference between integers and floating-point numbers, you can see why arithmetic in programming is not quite the same as arithmetic in math class. The five basic **arithmetic operators** — addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and modulo (`%`) — work on numeric values, but their behavior depends on the types of the operands. Addition, subtraction, and multiplication work as you would expect for both integers and floats. Division and modulo are where things get interesting.

When you divide two integers, most languages perform **integer division** (sometimes called floor division): the result is an integer with the fractional part discarded. So `7 / 2` gives `3`, not `3.5`. This is not rounding — it is truncation. If you want the decimal result, at least one operand must be a float: `7.0 / 2` gives `3.5`. This distinction trips up beginners constantly because math does not distinguish between "integer 7 divided by 2" and "real number 7 divided by 2" — but programming must, because the types determine how the hardware performs the operation. Python 3 made a deliberate design choice here: `/` always returns a float, and `//` performs integer division. Other languages like C, Java, and JavaScript each handle this differently, so knowing your language's rules is essential.

The **modulo operator** (`%`) returns the remainder after integer division. If `7 / 2` is `3`, then `7 % 2` is `1` — because 3 times 2 is 6, and 7 minus 6 is 1. Modulo is more useful than it first appears: it is the standard way to check if a number is even (`n % 2 == 0`), to wrap values around a range (clock arithmetic, array index cycling), and to extract digits from numbers. Together, integer division and modulo give you both the quotient and the remainder — the two pieces of information that division naturally produces.

One more subtlety worth noting: when you mix types in an expression, like `3 + 2.5`, the language performs **type promotion** — it converts the integer to a float before doing the operation, so the result is `5.5` (a float). This automatic conversion is usually what you want, but it means that the type of an arithmetic expression depends not just on the operator but on the types of its inputs. As you start writing more complex expressions, keeping track of types through each operation will help you predict results correctly and avoid subtle bugs.
