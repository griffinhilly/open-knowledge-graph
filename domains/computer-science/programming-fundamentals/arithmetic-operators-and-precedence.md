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

## Explainer

You've already seen that expressions combine values and operators to produce results, and you know how integers and floats behave as data types. Arithmetic operators are the specific symbols that perform mathematical computations: **addition** (`+`), **subtraction** (`-`), **multiplication** (`*`), **division** (`/`), and **modulo** (`%`, which gives the remainder after division). Most languages also include **integer division** (`//` in Python, or implicit when dividing two integers in C/Java) and **exponentiation** (`**` in Python, `Math.pow()` in many others). These operators work on numbers the way you'd expect from math class — with one crucial addition: the rules for which operation happens first.

**Operator precedence** determines the order in which operations are evaluated when an expression contains multiple operators. Just like in algebra, multiplication and division happen before addition and subtraction. The expression `2 + 3 * 4` evaluates to 14, not 20, because `3 * 4` is computed first. The full precedence hierarchy, from highest to lowest, is typically: parentheses, exponentiation, unary negation, multiplication/division/modulo, then addition/subtraction. When operators share the same precedence level, **associativity** determines the order: most arithmetic operators are **left-associative**, meaning they evaluate left-to-right (`10 - 3 - 2` is `(10 - 3) - 2 = 5`, not `10 - (3 - 2) = 9`). The important exception is exponentiation, which is **right-associative**: `2 ** 3 ** 2` evaluates as `2 ** (3 ** 2) = 2 ** 9 = 512`, not `(2 ** 3) ** 2 = 64`.

**Parentheses** override all precedence and associativity rules. When you write `(2 + 3) * 4`, the addition happens first regardless of precedence, giving 20. Even when parentheses aren't strictly necessary, adding them makes your intent explicit and your code easier to read. The expression `a + b * c / d` is technically unambiguous, but `a + ((b * c) / d)` communicates the same computation with zero chance of misreading. Experienced programmers use parentheses as a communication tool, not just a computation tool.

One operator worth special attention is **modulo** (`%`). It returns the remainder of integer division: `17 % 5` is 2, because 17 divided by 5 is 3 with remainder 2. Modulo is surprisingly useful in practice — you can test whether a number is even (`n % 2 == 0`), wrap values around a range (clock arithmetic: `hour % 12`), or cycle through a sequence of indices. Also watch out for division behavior with integers: in Python 3, `/` always returns a float (`7 / 2` gives `3.5`), while `//` performs floor division (`7 // 2` gives `3`). In languages like C and Java, dividing two integers automatically truncates the decimal, which can cause unexpected results if you're not paying attention.
