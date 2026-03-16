---
id: rational-expressions-intro
title: Introduction to Rational Expressions
domain: mathematics
course: algebra-1
prerequisites:
- id: factoring-completely
  type: hard
- id: multiplying-fractions
  type: hard
- id: negative-exponents
  type: soft
builds-toward:
- solving-rational-equations
- rational-functions-and-asymptotes
tags:
- rational-expressions
- fractions
- simplifying
- domain
stage: abstract-reasoning
status: validated
---
# Introduction to Rational Expressions

## Core Idea
A rational expression is a fraction where the numerator and/or denominator are polynomials, such as (x² − 4)/(x + 2). Simplifying a rational expression means factoring the numerator and denominator and canceling common factors: (x² − 4)/(x + 2) = (x + 2)(x − 2)/(x + 2) = x − 2, with the restriction that x cannot equal −2 (because the original expression is undefined there). The domain of a rational expression excludes all values that make the denominator zero. Rational expressions extend fraction skills to algebra and appear in rate problems, probability, and calculus.

## How It's Best Learned
Review fraction simplification with numerical examples, then extend to polynomial fractions. Emphasize that you can only cancel factors, not terms — you cannot cancel the 2 in (x + 2)/(x + 4). Always factor before canceling. Practice finding excluded values (domain restrictions). Include multiplying and dividing rational expressions as extensions.

## Common Misconceptions
- Canceling terms instead of factors: writing (x + 2)/(x + 4) = 2/4 = 1/2 by "canceling" x.
- Forgetting domain restrictions — the simplified form has the same domain restrictions as the original.
- Not factoring completely before trying to cancel.

## Explainer

You've already mastered two prerequisites that unlock rational expressions: factoring polynomials and simplifying numerical fractions. A **rational expression** is simply a fraction whose numerator and/or denominator are polynomials instead of plain numbers. The same logic that simplifies 6/8 to 3/4 — factor, cancel common factors — applies here, just with polynomials in place of integers.

Work through a concrete example: (x² − 4)/(x + 2). Factor the numerator using the difference of squares: x² − 4 = (x + 2)(x − 2). The expression becomes (x + 2)(x − 2)/(x + 2). Now the factor (x + 2) appears in both numerator and denominator — cancel it to get x − 2. Simple. But here is the critical subtlety: the original expression was undefined when x = −2 (division by zero), so even though the simplified form x − 2 looks perfectly happy at x = −2, you must carry forward the restriction x ≠ −2. The **domain** of the simplified expression is not larger than the original's domain.

The most dangerous misconception is canceling *terms* rather than *factors*. You can only cancel something that is multiplied across the entire numerator and the entire denominator. In (x + 2)/(x + 4), the x's and the 2 and 4 are *added*, not multiplied — there is nothing to cancel. Writing (x + 2)/(x + 4) = 2/4 = 1/2 by "crossing out the x" is wrong for the same reason that 5/7 ≠ /7. Only factors — things that multiply the whole expression — can be canceled. This is why the rule is: **factor completely first, then cancel**.

Multiplying and dividing rational expressions extend the same logic. To multiply, factor all numerators and denominators, cancel any common factors across the numerators and denominators, then multiply what remains. To divide, multiply by the reciprocal of the divisor. These operations build directly on your fraction skills and prepare you for rational equations (where you solve for x in expressions like this) and, much later, for computing limits in calculus where expressions simplify after cancellation of the problematic factor.
