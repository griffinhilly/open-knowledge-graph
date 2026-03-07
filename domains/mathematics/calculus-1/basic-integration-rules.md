---
id: basic-integration-rules
title: Basic Integration Rules
domain: mathematics
course: calculus-1
prerequisites:
  - id: indefinite-integrals
    type: hard
  - id: constant-multiple-and-sum-rules
    type: hard
builds-toward:
  - u-substitution
  - riemann-sums
tags: [integration, rules, power-rule-integration]
stage: formal-systems
status: draft
---

# Basic Integration Rules

## Core Idea
The basic integration rules are the reverses of the basic derivative rules: the integral of x^n dx = x^(n+1)/(n+1) + C (for n not equal to -1), the integral of 1/x dx = ln|x| + C, the integral of e^x dx = e^x + C, the integral of sin(x) dx = -cos(x) + C, the integral of cos(x) dx = sin(x) + C, and so on. The constant multiple and sum rules apply to integrals just as they do to derivatives: integration is linear.

## How It's Best Learned
Build a reference table of basic integrals alongside the corresponding derivative rules. Practice until the correspondence is automatic. Emphasize the special case n = -1 (integral of 1/x is ln|x|, not the power rule). Verify every integral by differentiating.

## Common Misconceptions
- Applying the power rule for integration when n = -1 (division by zero).
- Forgetting sign changes: the integral of sin(x) is -cos(x), not +cos(x).
- Assuming there is a product rule or quotient rule for integration (there is not directly).
