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

## Questions

```yaml
- question: "What is the value of the expression `10 - 3 * 2 + 4`?"
  type: multiple-choice
  options:
    - "18 — evaluated left-to-right: 10−3=7, 7*2=14, 14+4=18"
    - "8 — multiplication first: 3*2=6, then left-to-right: 10−6+4=8"
    - "0 — subtraction and addition cancel out after multiplying"
    - "14 — the addition is evaluated before the subtraction due to left-to-right order"
  answer: 1
  explanation: "Operator precedence applies: multiplication (*) has higher precedence than subtraction (−) and addition (+), so 3*2=6 is evaluated first. Then the remaining operations are evaluated left-to-right at equal precedence: 10−6=4, 4+4=8. Option A is the classic left-to-right-ignoring-precedence error — the mistake of treating 2+3*4 as 20 instead of 14."

- question: "A student writes `2 ** 3 ** 2` expecting the result `(2**3)**2 = 64`. What does the expression actually evaluate to?"
  type: multiple-choice
  options:
    - "64 — exponentiation is left-associative, so 2**3 is computed first, giving 8, then 8**2 = 64"
    - "512 — exponentiation is right-associative, so 3**2 = 9 is computed first, then 2**9 = 512"
    - "64 — when operators are repeated, the language always picks the leftmost operation"
    - "512 — the larger base is always evaluated first in chained exponentiation"
  answer: 1
  explanation: "Exponentiation is right-associative — the rightmost operation is evaluated first. `2 ** 3 ** 2` is parsed as `2 ** (3 ** 2)` = `2 ** 9` = 512. This is the important exception to the general left-to-right associativity of arithmetic operators. The student's expectation of 64 reflects applying left-associativity where right-associativity applies. To get 64, the student should write `(2 ** 3) ** 2` explicitly."

- question: "The expression `17 % 5` evaluates to 2."
  type: true-false
  answer: true
  explanation: "The modulo operator (%) returns the remainder after integer division. 17 ÷ 5 = 3 with remainder 2, so 17 % 5 = 2. Modulo is not a percentage operator — it computes the remainder. It's useful for checking divisibility (n % 2 == 0 tests if n is even), wrapping values around a range (e.g., hour % 12 for clock arithmetic), and cycling through indices."

- question: "Adding parentheses to an expression in a way that reflects the order it would already be evaluated can change the result."
  type: true-false
  answer: false
  explanation: "Parentheses override precedence by forcing a specific evaluation order, but if the parenthesized order matches what precedence already prescribes, the result is identical. `(3 * 4) + 2` and `3 * 4 + 2` both equal 14, because multiplication already has higher precedence than addition. Parentheses that reflect the existing evaluation order are purely for readability — they communicate intent without changing computation."

- question: "Explain why operator precedence rules exist in programming languages, and what problem would arise if all operators were evaluated strictly left-to-right."
  type: short-answer
  answer: "Operator precedence ensures that mathematical expressions in code behave consistently with algebraic convention — multiplication and division bind more tightly than addition and subtraction, matching what students learn in mathematics. Without precedence rules, `2 + 3 * 4` would evaluate left-to-right as `(2 + 3) * 4 = 20` instead of the mathematically correct `2 + (3 * 4) = 14`. Programmers would then need explicit parentheses around every multiplication in a mixed expression, making arithmetic code verbose, error-prone, and inconsistent with mathematical notation. Precedence rules reduce visual noise while keeping expressions unambiguous."
  explanation: "This is an example of a language design decision that prioritizes ergonomics and mathematical consistency. The precedence hierarchy (PEMDAS/BODMAS) is essentially built into every programming language's parser. Knowing the rules lets you write `a + b * c / d` without parentheses when the default evaluation order is correct, and add parentheses only when you need to override it — which is the minimum-friction way to express arithmetic intent in code."
```

## Explainer

You've already seen that expressions combine values and operators to produce results, and you know how integers and floats behave as data types. Arithmetic operators are the specific symbols that perform mathematical computations: **addition** (`+`), **subtraction** (`-`), **multiplication** (`*`), **division** (`/`), and **modulo** (`%`, which gives the remainder after division). Most languages also include **integer division** (`//` in Python, or implicit when dividing two integers in C/Java) and **exponentiation** (`**` in Python, `Math.pow()` in many others). These operators work on numbers the way you'd expect from math class — with one crucial addition: the rules for which operation happens first.

**Operator precedence** determines the order in which operations are evaluated when an expression contains multiple operators. Just like in algebra, multiplication and division happen before addition and subtraction. The expression `2 + 3 * 4` evaluates to 14, not 20, because `3 * 4` is computed first. The full precedence hierarchy, from highest to lowest, is typically: parentheses, exponentiation, unary negation, multiplication/division/modulo, then addition/subtraction. When operators share the same precedence level, **associativity** determines the order: most arithmetic operators are **left-associative**, meaning they evaluate left-to-right (`10 - 3 - 2` is `(10 - 3) - 2 = 5`, not `10 - (3 - 2) = 9`). The important exception is exponentiation, which is **right-associative**: `2 ** 3 ** 2` evaluates as `2 ** (3 ** 2) = 2 ** 9 = 512`, not `(2 ** 3) ** 2 = 64`.

**Parentheses** override all precedence and associativity rules. When you write `(2 + 3) * 4`, the addition happens first regardless of precedence, giving 20. Even when parentheses aren't strictly necessary, adding them makes your intent explicit and your code easier to read. The expression `a + b * c / d` is technically unambiguous, but `a + ((b * c) / d)` communicates the same computation with zero chance of misreading. Experienced programmers use parentheses as a communication tool, not just a computation tool.

One operator worth special attention is **modulo** (`%`). It returns the remainder of integer division: `17 % 5` is 2, because 17 divided by 5 is 3 with remainder 2. Modulo is surprisingly useful in practice — you can test whether a number is even (`n % 2 == 0`), wrap values around a range (clock arithmetic: `hour % 12`), or cycle through a sequence of indices. Also watch out for division behavior with integers: in Python 3, `/` always returns a float (`7 / 2` gives `3.5`), while `//` performs floor division (`7 // 2` gives `3`). In languages like C and Java, dividing two integers automatically truncates the decimal, which can cause unexpected results if you're not paying attention.
