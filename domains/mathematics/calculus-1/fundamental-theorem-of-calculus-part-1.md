---
id: fundamental-theorem-of-calculus-part-1
title: Fundamental Theorem of Calculus Part 1
domain: mathematics
course: calculus-1
prerequisites:
- id: definite-integral-definition
  type: hard
- id: continuity-definition
  type: hard
- id: antiderivatives
  type: soft
builds-toward:
- fundamental-theorem-of-calculus-part-2
tags:
- integration
- FTC
- fundamental-theorem
stage: formal-systems
status: validated
---
# Fundamental Theorem of Calculus Part 1

## Core Idea
FTC Part 1 states that if f is continuous on [a, b], then the function g(x) = integral from a to x of f(t) dt is an antiderivative of f: g'(x) = f(x). In other words, differentiation undoes integration. This theorem guarantees that every continuous function has an antiderivative and connects the two branches of calculus (differential and integral). With the chain rule, d/dx[integral from a to h(x) of f(t) dt] = f(h(x)) * h'(x).

## How It's Best Learned
Start with concrete examples: if g(x) = integral from 0 to x of t^2 dt, compute g(x) as x^3/3 and verify g'(x) = x^2. Then apply to functions defined by integrals whose antiderivatives are not elementary. Practice the chain rule extension. Emphasize the deep meaning: integration and differentiation are inverse processes.

## Common Misconceptions
- Confusing FTC Part 1 (derivative of an integral) with FTC Part 2 (evaluating a definite integral).
- Forgetting the chain rule when the upper limit is not simply x.
- Not recognizing that the variable of integration (t) is a dummy variable, distinct from x.
