---
id: power-rule
title: Power Rule
domain: mathematics
course: calculus-1
prerequisites:
  - id: limit-definition-of-derivative
    type: hard
builds-toward:
  - constant-multiple-and-sum-rules
  - antiderivatives
tags: [derivatives, rules, power-rule]
stage: formal-systems
status: validated
---

# Power Rule

## Core Idea
The power rule states that if f(x) = x^n, then f'(x) = n*x^(n-1). It works for any real exponent n: positive integers, negative integers, and fractions. This is the first and most frequently used derivative shortcut. Combined with the constant multiple and sum rules, it handles all polynomial derivatives instantly.

## How It's Best Learned
Derive the power rule from the limit definition for n = 2 and n = 3 to see the pattern, then state the general rule. Practice with positive integer exponents, then extend to negative exponents (f(x) = 1/x^n = x^(-n)) and fractional exponents (f(x) = sqrt(x) = x^(1/2)). Emphasize rewriting roots and reciprocals as powers before differentiating.

## Common Misconceptions
- Forgetting to subtract 1 from the exponent.
- Not rewriting roots and fractions as powers: d/dx[sqrt(x)] requires writing it as x^(1/2) first.
- Applying the power rule to exponential functions like 2^x (the variable is in the exponent, not the base).
