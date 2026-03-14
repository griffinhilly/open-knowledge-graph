---
id: product-rule
title: Product Rule
domain: mathematics
course: calculus-1
prerequisites:
  - id: constant-multiple-and-sum-rules
    type: hard
builds-toward:
  - quotient-rule
  - integration-by-parts
tags: [derivatives, rules, product-rule]
stage: formal-systems
status: validated
---

# Product Rule

## Core Idea
The product rule states that d/dx[f(x)*g(x)] = f'(x)*g(x) + f(x)*g'(x). The derivative of a product is NOT the product of the derivatives. Instead, you differentiate each factor while keeping the other unchanged, then add the results. This rule is necessary whenever two non-constant functions are multiplied together.

## How It's Best Learned
Derive from the limit definition by adding and subtracting f(x+h)*g(x). Practice with products of polynomials (verifiable by expanding first), then with products involving trig and exponential functions. Use the mnemonic "first times derivative of second plus second times derivative of first."

## Common Misconceptions
- Believing (fg)' = f'g': this is the single most common calculus error.
- Forgetting one of the two terms in the product rule.
- Not recognizing when the product rule is needed vs. when the constant multiple rule suffices (if one factor is a constant, use the simpler rule).
