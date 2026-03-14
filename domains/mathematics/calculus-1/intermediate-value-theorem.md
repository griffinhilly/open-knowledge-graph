---
id: intermediate-value-theorem
title: Intermediate Value Theorem
domain: mathematics
course: calculus-1
prerequisites:
  - id: continuity-definition
    type: hard
builds-toward:
  - mean-value-theorem
tags: [continuity, existence-theorems, IVT]
stage: formal-systems
status: validated
---

# Intermediate Value Theorem

## Core Idea
The Intermediate Value Theorem (IVT) states that if f is continuous on [a, b] and N is any value between f(a) and f(b), then there exists at least one c in (a, b) such that f(c) = N. In plain terms: a continuous function cannot skip a value. The most common application is proving that an equation has a solution (especially finding roots): if f(a) and f(b) have opposite signs, there must be a zero between them.

## How It's Best Learned
Start with the intuitive idea: you cannot draw a continuous curve from one height to another without passing through every height in between. Apply IVT to prove existence of roots. Emphasize that IVT guarantees existence but does not find the exact value.

## Common Misconceptions
- Using IVT without verifying continuity on the interval.
- Thinking IVT gives the exact location of c (it only guarantees existence).
- Applying IVT to functions with discontinuities in the interval.
