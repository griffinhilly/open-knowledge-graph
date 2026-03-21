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

## Questions

```yaml
- question: "In a programming language that uses integer division (like C or Java), what is the value of the expression 9 / 4?"
  type: multiple-choice
  options:
    - "2.25, because 9 divided by 4 is 2.25"
    - "2, because integer division discards the fractional part"
    - "3, because integer division rounds to the nearest whole number"
    - "An error, because 9 is not evenly divisible by 4"
  answer: 1
  explanation: "Integer division truncates — it discards the fractional part rather than rounding. 9 / 4 = 2.25 in real arithmetic, but with integer operands, only the 2 is kept. The 0.25 is simply thrown away, not rounded. This surprises many beginners who expect rounding: 2.25 is closer to 2 than to 3, but even 3.9 / 4 would give 0 (not 1) in integer division — the fractional part is always discarded, not rounded. To get the decimal result, at least one operand must be a float: 9.0 / 4 gives 2.25."

- question: "What is the value of 17 % 5?"
  type: multiple-choice
  options:
    - "3, because 17 = 3 × 5 + 2, so the remainder is 2. Wait — 3 × 5 = 15, remainder = 2"
    - "2, because 17 = 3 × 5 + 2"
    - "3, because 17 divided by 5 gives quotient 3"
    - "0.4, because the fractional part of 17/5 is 0.4"
  answer: 1
  explanation: "The modulo operator returns the remainder after integer division. 17 ÷ 5 = 3 remainder 2, because 3 × 5 = 15 and 17 − 15 = 2. So 17 % 5 = 2. Option C confuses the quotient with the remainder: the quotient is 3, but modulo gives the remainder, which is 2. Option D confuses modulo with fractional parts of real division — they are different concepts. The modulo result is always a non-negative integer less than the divisor (when both operands are positive)."

- question: "In most programming languages, the expression 7 % 2 evaluates to 1."
  type: true-false
  answer: true
  explanation: "7 divided by 2 gives quotient 3 and remainder 1 (since 3 × 2 = 6, and 7 − 6 = 1). Modulo returns the remainder, so 7 % 2 = 1. This is consistent across essentially all mainstream programming languages. Modulo is commonly used to check divisibility: if n % 2 == 0, the number is even; if n % 2 == 1, it is odd. It is also used for clock arithmetic (wrapping values around a range), cycling through array indices, and extracting digits from numbers."

- question: "Integer division rounds the result to the nearest whole number, so 7 / 2 evaluates to 4 in a language with integer division."
  type: true-false
  answer: false
  explanation: "Integer division truncates — it discards the fractional part, always moving toward zero. 7 / 2 = 3.5 in real arithmetic, and integer division gives 3, not 4. Even if the decimal part were 0.9 (e.g., 9 / 10 = 0.9), integer division would give 0, not 1. Rounding and truncation are different operations: rounding moves to the nearest integer, truncation always moves toward zero. This distinction matters whenever you mix integer arithmetic with expected decimal results, which is a common source of bugs for new programmers."

- question: "Explain why 7 / 2 gives 3 (not 3.5 or 4) in a language that performs integer division, and what you must do to get the decimal result."
  type: short-answer
  answer: "When both operands are integers, the hardware performs integer division, which computes the quotient and discards the remainder. 7 ÷ 2 = 3 remainder 1, so the result is 3. The fractional part (0.5) is truncated, not rounded. To get the decimal result 3.5, at least one operand must be a float: 7.0 / 2 or 7 / 2.0 will trigger floating-point division and return 3.5."
  explanation: "The root cause is that integers and floating-point numbers are stored and processed differently at the hardware level. Integer division is exact quotient arithmetic — the same operation you learned as 'long division' in grade school, where you keep the remainder. Floating-point division approximates real number division. Programming languages must distinguish these because choosing the wrong one causes subtle bugs: a temperature sensor reading of 7 / 2 that returns 3 instead of 3.5 could cause real errors in a control system. Knowing your language's division rules — and when to cast to float — is a fundamental programming skill."
```

## Explainer

Now that you understand the difference between integers and floating-point numbers, you can see why arithmetic in programming is not quite the same as arithmetic in math class. The five basic **arithmetic operators** — addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), and modulo (`%`) — work on numeric values, but their behavior depends on the types of the operands. Addition, subtraction, and multiplication work as you would expect for both integers and floats. Division and modulo are where things get interesting.

When you divide two integers, most languages perform **integer division** (sometimes called floor division): the result is an integer with the fractional part discarded. So `7 / 2` gives `3`, not `3.5`. This is not rounding — it is truncation. If you want the decimal result, at least one operand must be a float: `7.0 / 2` gives `3.5`. This distinction trips up beginners constantly because math does not distinguish between "integer 7 divided by 2" and "real number 7 divided by 2" — but programming must, because the types determine how the hardware performs the operation. Python 3 made a deliberate design choice here: `/` always returns a float, and `//` performs integer division. Other languages like C, Java, and JavaScript each handle this differently, so knowing your language's rules is essential.

The **modulo operator** (`%`) returns the remainder after integer division. If `7 / 2` is `3`, then `7 % 2` is `1` — because 3 times 2 is 6, and 7 minus 6 is 1. Modulo is more useful than it first appears: it is the standard way to check if a number is even (`n % 2 == 0`), to wrap values around a range (clock arithmetic, array index cycling), and to extract digits from numbers. Together, integer division and modulo give you both the quotient and the remainder — the two pieces of information that division naturally produces.

One more subtlety worth noting: when you mix types in an expression, like `3 + 2.5`, the language performs **type promotion** — it converts the integer to a float before doing the operation, so the result is `5.5` (a float). This automatic conversion is usually what you want, but it means that the type of an arithmetic expression depends not just on the operator but on the types of its inputs. As you start writing more complex expressions, keeping track of types through each operation will help you predict results correctly and avoid subtle bugs.
