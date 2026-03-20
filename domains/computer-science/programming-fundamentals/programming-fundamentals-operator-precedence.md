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

## Questions

```yaml
- question: "What does the expression `2 + 3 * 4 > 10 and False` evaluate to, and which evaluation order produces that result?"
  type: multiple-choice
  options:
    - "True — left-to-right evaluation gives (2+3)=5, then 5×4=20, then 20>10=True, and True overrides False"
    - "False — multiplication evaluates first (3×4=12), then addition (2+12=14), then comparison (14>10=True), then 'and' (True and False=False)"
    - "True — 'and' is evaluated before comparison operators, so 'and False' is processed before '>10'"
    - "Error — arithmetic, comparison, and boolean operators cannot be chained in a single expression"
  answer: 1
  explanation: "The precedence hierarchy: multiplication before addition (arithmetic), then comparison operators, then logical operators (NOT > AND > OR). So: 3×4=12, then 2+12=14, then 14>10=True, then True and False=False. Option A shows the classic left-to-right mistake: assuming operators execute in the order they appear on the line. Option C reverses the precedence of 'and' relative to comparison operators — 'and' is actually lower precedence. This is exactly the kind of silent bug that runs without error but produces the wrong result."

- question: "What does `8 - 3 - 2` evaluate to, and what rule determines this?"
  type: multiple-choice
  options:
    - "7 — subtraction is right-associative, so it evaluates as 8-(3-2)=7"
    - "3 — subtraction is left-associative, so it evaluates as (8-3)-2=3"
    - "It depends on the programming language — no universal associativity rule exists for subtraction"
    - "Both 3 and 7 are valid — when operators have equal precedence, the result is unspecified"
  answer: 1
  explanation: "Subtraction is left-associative in all standard programming languages, meaning equal-precedence operators group to the left: (8-3)-2 = 5-2 = 3. Option A shows the right-associative interpretation: 8-(3-2) = 8-1 = 7 — a different result. This matters whenever you have a chain of subtractions or divisions, where changing associativity changes the answer. Contrast with exponentiation, which is typically right-associative: 2**3**2 = 2**(3**2) = 512, not (2**3)**2 = 64."

- question: "In the expression `x + 1 > 5`, the comparison operator `>` is evaluated before the addition because comparisons need their operands fully resolved first."
  type: true-false
  answer: false
  explanation: "Arithmetic operators have higher precedence than comparison operators, so `x + 1` is computed first and then the result is compared to 5. The expression evaluates as `(x + 1) > 5`. The reasoning in the statement is backwards — 'needing operands resolved first' is true of all operators, but precedence rules determine which operator claims its operands first. If `>` evaluated first, you would be comparing `x` to something before the addition was complete."

- question: "Operator precedence bugs are especially dangerous because the code runs without producing any error — the expression evaluates silently to the wrong value."
  type: true-false
  answer: true
  explanation: "Unlike syntax errors or type errors, precedence mistakes are logically valid expressions. The language executes them as written and produces an incorrect result with no warning. The code 'works' from the computer's perspective; the only symptom is unexpected behavior at runtime. This is what makes them subtle. Using explicit parentheses eliminates this class of bug by making the intended grouping impossible to misread."

- question: "Why do experienced programmers use parentheses liberally even when they know the precedence rules?"
  type: short-answer
  answer: "Parentheses make intent explicit and make code easier to read, review, and maintain. Even if a programmer knows that `x + 1 > 5` parses as `(x + 1) > 5`, writing it with explicit parentheses removes any ambiguity for future readers (including themselves months later). Clear code is more valuable than clever code that relies on the reader memorizing precedence tables. Parentheses also prevent accidental bugs when expressions are modified later without full consideration of precedence interactions."
  explanation: "The practical rule is: when in doubt, parenthesize. Experienced developers go further — they parenthesize whenever there's any chance of ambiguity, not just when they're uncertain. The cost is zero (no performance impact), and the benefit is code that communicates intent unambiguously. Precedence knowledge is most valuable for reading existing code and debugging unexpected results; when writing new code, explicit grouping is almost always the better choice."
```

## Explainer

You already know how logical operators like AND, OR, and NOT combine boolean values. But when you write an expression that mixes arithmetic, comparison, and logical operators — like `x + 3 > 10 and y * 2 < 5` — the computer needs a set of rules to decide which operation happens first. These rules are called **operator precedence**, and they work much like the order of operations you learned in arithmetic (PEMDAS/BODMAS), but extended to cover every operator a programming language supports.

The basic hierarchy goes like this: arithmetic operators are evaluated first (multiplication and division before addition and subtraction), then comparison operators (`>`, `<`, `==`, `!=`), and finally logical operators (NOT before AND, AND before OR). So in the expression `3 + 4 * 2 > 10 or False`, the computer first computes `4 * 2` to get `8`, then `3 + 8` to get `11`, then `11 > 10` to get `True`, and finally `True or False` to get `True`. If you assumed left-to-right evaluation instead, you might expect `3 + 4` first, giving a completely different result. This is where precedence bugs hide — the code runs without errors but produces the wrong answer.

**Associativity** determines the tiebreaker when operators have equal precedence. Most arithmetic operators are left-associative, meaning `8 - 3 - 2` evaluates as `(8 - 3) - 2 = 3`, not `8 - (3 - 2) = 7`. Exponentiation is typically right-associative: `2 ** 3 ** 2` evaluates as `2 ** (3 ** 2) = 2 ** 9 = 512`. Knowing associativity matters most for subtraction, division, and exponentiation, where grouping changes the result.

The practical takeaway is simple: **when in doubt, use parentheses**. Parentheses override all precedence rules and make your intent explicit. Writing `(x + 3) > 10` instead of `x + 3 > 10` costs nothing in performance and makes the code self-documenting. Experienced programmers use parentheses liberally not because they have forgotten precedence rules, but because clear code is more valuable than clever code. Precedence knowledge helps you *read* code that lacks parentheses and *debug* expressions that behave unexpectedly — but when you *write* code, explicit grouping is almost always the better choice.
