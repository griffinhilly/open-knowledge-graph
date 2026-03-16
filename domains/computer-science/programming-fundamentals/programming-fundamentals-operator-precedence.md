---
id: programming-fundamentals-operator-precedence
title: Operator Precedence and Evaluation Order
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: programming-fundamentals-logical-operators
  type: hard
builds-toward:
- programming-fundamentals-nested-conditions
tags:
- operators
- precedence
- evaluation
stage: abstract-reasoning
status: draft
---

# Operator Precedence and Evaluation Order

## Core Idea
Operator precedence determines the order in which operations are evaluated in an expression without parentheses. Multiplication and division are evaluated before addition and subtraction. Understanding precedence prevents subtle bugs.

## Explainer

You already know how logical operators like AND, OR, and NOT combine boolean values. But when you write an expression that mixes arithmetic, comparison, and logical operators — like `x + 3 > 10 and y * 2 < 5` — the computer needs a set of rules to decide which operation happens first. These rules are called **operator precedence**, and they work much like the order of operations you learned in arithmetic (PEMDAS/BODMAS), but extended to cover every operator a programming language supports.

The basic hierarchy goes like this: arithmetic operators are evaluated first (multiplication and division before addition and subtraction), then comparison operators (`>`, `<`, `==`, `!=`), and finally logical operators (NOT before AND, AND before OR). So in the expression `3 + 4 * 2 > 10 or False`, the computer first computes `4 * 2` to get `8`, then `3 + 8` to get `11`, then `11 > 10` to get `True`, and finally `True or False` to get `True`. If you assumed left-to-right evaluation instead, you might expect `3 + 4` first, giving a completely different result. This is where precedence bugs hide — the code runs without errors but produces the wrong answer.

**Associativity** determines the tiebreaker when operators have equal precedence. Most arithmetic operators are left-associative, meaning `8 - 3 - 2` evaluates as `(8 - 3) - 2 = 3`, not `8 - (3 - 2) = 7`. Exponentiation is typically right-associative: `2 ** 3 ** 2` evaluates as `2 ** (3 ** 2) = 2 ** 9 = 512`. Knowing associativity matters most for subtraction, division, and exponentiation, where grouping changes the result.

The practical takeaway is simple: **when in doubt, use parentheses**. Parentheses override all precedence rules and make your intent explicit. Writing `(x + 3) > 10` instead of `x + 3 > 10` costs nothing in performance and makes the code self-documenting. Experienced programmers use parentheses liberally not because they have forgotten precedence rules, but because clear code is more valuable than clever code. Precedence knowledge helps you *read* code that lacks parentheses and *debug* expressions that behave unexpectedly — but when you *write* code, explicit grouping is almost always the better choice.
