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
- arithmetic-operators
- type-conversion
- string-operations
tags:
- operators
- arithmetic
- comparison
- expressions
- precedence
stage: formal-systems
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

## Questions

```yaml
- question: "What does the expression `7 / 2` evaluate to in a language that uses integer division when both operands are integers?"
  type: multiple-choice
  options:
    - "3.5"
    - "3"
    - "4"
    - "1"
  answer: 1
  explanation: "When both operands are integers, integer division truncates (rounds toward zero), so `7 / 2` gives `3`, not `3.5`. The remainder is discarded, not rounded up. To get `3.5`, at least one operand must be a float: `7.0 / 2` or `7 / 2.0`. This surprises many beginners who expect division to behave like a calculator. Option C (4) represents rounding up, which is not how truncation works."

- question: "Consider the condition: `if (x != 0 and 10 / x > 2)`. If x equals 0, what happens?"
  type: multiple-choice
  options:
    - "A division-by-zero error occurs because both sides of `and` are always evaluated"
    - "The condition evaluates safely to false because short-circuit evaluation skips the division"
    - "The condition evaluates to true because 0 satisfies the `!=` check"
    - "The program crashes because `and` requires both operands to be computed before combining them"
  answer: 1
  explanation: "This is short-circuit evaluation in action. In `A and B`, if A is false, B is never evaluated — the result must be false regardless. When x is 0, `x != 0` is false, so the `and` short-circuits and `10 / x` is never computed. This makes the pattern a standard safe-division idiom. Options A and D reflect the misconception that logical operators always evaluate both sides."

- question: "Writing `if (x = 5)` instead of `if (x == 5)` in most C-style languages will cause an immediate syntax error that stops the program from running."
  type: true-false
  answer: false
  explanation: "This is one of the most insidious bugs precisely because it often does NOT cause an error. In many languages, `x = 5` is a valid assignment expression that evaluates to 5 (truthy), so the condition always passes — the program runs without complaint but with wrong behavior. This makes the = vs == confusion especially dangerous. Some modern linters warn about this pattern, but the language itself may not reject it."

- question: "The modulo operator `%` is primarily useful for checking whether a number is even or odd."
  type: true-false
  answer: false
  explanation: "While `n % 2 == 0` is a classic even-check, calling that its primary use understates modulo's range. Modulo is also the standard tool for cycling through a fixed range (index wrapping in circular buffers), implementing clock arithmetic, determining the day of the week from a day count, and many other cyclic computations. Even/odd checking is simply the most elementary example of a broadly useful operator."

- question: "Why does operator precedence matter in programming, and how does it relate to order of operations from math?"
  type: short-answer
  answer: "Operator precedence determines which sub-expression is evaluated first when multiple operators appear in a single expression. Programming languages inherit the mathematical convention (multiplication before addition) and extend it: comparison operators bind less tightly than arithmetic, and logical operators bind least. Without precedence rules, `3 + 4 * 2` would be ambiguous. In programming, `x + 1 > 3 and y < 5` first computes `x + 1`, then compares with `>`, then applies `and`."
  explanation: "Precedence is not arbitrary — it follows conventions inherited from mathematics and extended consistently to new operator types. Knowing the order prevents bugs where expressions evaluate in an unexpected sequence. When in doubt, parentheses make the intended order explicit and the code more readable, which is why experienced programmers use them liberally even when not strictly required."
```

## Explainer

You have learned to store values in variables and to distinguish between data types like integers, floats, and strings. **Operators** are the symbols that let you do things with those values — combine them, compare them, and build up complex calculations from simple parts. An **expression** is any combination of values, variables, and operators that the computer can evaluate to produce a single result. The expression `3 + 4` evaluates to `7`. The expression `age >= 18` evaluates to `true` or `false`. Even a lone variable like `x` is an expression — it evaluates to whatever value `x` currently holds.

**Arithmetic operators** work the way you expect from math: `+` adds, `-` subtracts, `*` multiplies, `/` divides. The one to watch carefully is division. In many languages, dividing two integers performs **integer division**, which truncates the result: `7 / 2` gives `3`, not `3.5`. If you want the decimal result, at least one operand must be a float: `7.0 / 2` gives `3.5`. The **modulo operator** `%` returns the remainder after division: `7 % 2` gives `1`, because 7 divided by 2 is 3 with a remainder of 1. Modulo is surprisingly useful — it is the standard way to check whether a number is even (`n % 2 == 0`), to cycle through a fixed range, or to wrap around indices.

**Comparison operators** produce boolean values. `==` checks equality, `!=` checks inequality, and `<`, `>`, `<=`, `>=` compare magnitude. The critical beginner trap is confusing `=` (assignment, which stores a value) with `==` (comparison, which tests equality). Writing `if (x = 5)` assigns 5 to `x` instead of checking whether `x` equals 5 — a bug that can be very difficult to spot because the program may still run without an error.

**Logical operators** — `and`, `or`, `not` (or `&&`, `||`, `!` in C-style languages) — combine boolean expressions. `and` is true only when both sides are true; `or` is true when at least one side is true; `not` inverts true to false and vice versa. A critical behavior is **short-circuit evaluation**: in `A and B`, if `A` is false, the computer skips evaluating `B` entirely because the result must be false regardless. Similarly, in `A or B`, if `A` is true, `B` is never evaluated. This is not just an optimization — it lets you write safe conditions like `if (x != 0 and 10 / x > 2)`, where the division only happens if `x` is nonzero. When multiple operators appear in one expression, **precedence rules** (which you know from order of operations in math) determine what gets evaluated first. Multiplication before addition, comparison before logic, and when in doubt, parentheses make the order explicit and the code readable.
