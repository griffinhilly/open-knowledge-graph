---
id: quotient-rule
title: Quotient Rule
domain: mathematics
course: calculus-1
prerequisites:
  - id: product-rule
    type: hard
builds-toward:
  - implicit-differentiation
tags: [derivatives, rules, quotient-rule]
stage: formal-systems
status: validated
---

# Quotient Rule

## Core Idea
The quotient rule states that d/dx[f(x)/g(x)] = (f'(x)*g(x) - f(x)*g'(x)) / [g(x)]^2. It handles derivatives of fractions where both numerator and denominator are functions of x. The mnemonic "lo d-hi minus hi d-lo over lo-lo" helps with the formula. Alternatively, the quotient rule can be derived from the product rule with g^(-1), but the formula is used directly in practice.

## How It's Best Learned
Derive from the product rule applied to f * g^(-1). Practice with simple rational functions first, then with trig functions (this is how you derive d/dx[tan(x)] = sec^2(x)). Emphasize keeping the denominator squared and the minus sign in the correct position.

## Common Misconceptions
- Swapping the order in the numerator: it is f'g - fg', not fg' - f'g.
- Forgetting to square the denominator.
- Using the quotient rule when simpler alternatives exist (e.g., rewrite 1/x^3 as x^(-3) and use power rule).
