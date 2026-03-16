---
id: operator-precedence-and-evaluation
title: Operator Precedence and Order of Evaluation
domain: computer-science
course: programming-fundamentals
prerequisites:
- id: arithmetic-operators-intro
  type: hard
- id: comparison-operators-and-relations
  type: hard
- id: logical-operators-and-gates
  type: hard
builds-toward:
- conditional-statements
tags:
- operators
- precedence
- evaluation
stage: abstract-reasoning
status: draft
---

# Operator Precedence and Order of Evaluation

## Core Idea
Operator precedence determines the order in which operators are applied in complex expressions. Parentheses override precedence. Understanding evaluation order is essential for writing correct expressions and debugging subtle bugs.

## How It's Best Learned
Evaluate complex expressions with mixed operators. Use parentheses to override precedence and compare results.

## Common Misconceptions
- Operators are always evaluated left to right (precedence and associativity matter; some languages have special rules).
- Parentheses are always necessary for clarity (they're helpful but the precedence rules still apply).

## Explainer

From arithmetic operators, comparison operators, and logical operators, you know three families of operators that each produce results — numbers, booleans from comparisons, and booleans from logical combinations. When these operators appear together in a single expression like `x + 3 > 10 and y * 2 < 20`, the computer needs a set of rules to determine which operations happen first. **Operator precedence** is that set of rules — it defines a hierarchy that determines the order in which operators are applied, exactly as the mathematical convention "multiplication before addition" determines that `2 + 3 × 4` equals 14, not 20.

The general precedence hierarchy across most languages, from highest (evaluated first) to lowest, is: **parentheses** → **unary operators** (NOT, negation) → **arithmetic** (first multiplication/division/modulus, then addition/subtraction) → **comparison** (>, <, ==, !=) → **logical AND** → **logical OR**. So the expression `x + 3 > 10 and y * 2 < 20` is evaluated as `((x + 3) > 10) and ((y * 2) < 20)` — arithmetic first, then comparisons, then the logical AND combines the two boolean results. You never need to memorize the entire precedence table; knowing the broad categories (arithmetic beats comparison beats logic) and using parentheses for anything non-obvious is the practical approach.

When two operators have the **same precedence**, **associativity** determines the order. Most binary operators are **left-associative**: `a - b - c` is evaluated as `(a - b) - c`, left to right. The notable exception is exponentiation in languages that have it (`**` in Python): `2 ** 3 ** 2` evaluates as `2 ** (3 ** 2)` = `2 ** 9` = 512, not `(2 ** 3) ** 2` = 64, because exponentiation is **right-associative**. Assignment is another right-associative operator: `a = b = 5` assigns 5 to b first, then assigns the result to a.

**Parentheses always override precedence**, and this is the most important practical rule. If you are unsure whether `a + b * c` means what you intend, add parentheses: `a + (b * c)` or `(a + b) * c`. Parentheses make your intent explicit to both the compiler and to anyone reading your code. The common mistake is not that programmers fail to memorize precedence tables — it is that they *assume* left-to-right evaluation when precedence or associativity dictates otherwise. When debugging an expression that produces an unexpected result, add parentheses to match what you *think* the evaluation order is, then compare with what the language actually does. The discrepancy, when it exists, is almost always a precedence or associativity issue.
