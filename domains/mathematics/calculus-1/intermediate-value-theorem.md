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

## Explainer

The **Intermediate Value Theorem** formalizes something visually obvious: if you draw a continuous curve from one height to another without lifting your pen, you must pass through every height in between. Drive from sea level to a mountain summit and you must pass through every altitude along the way — there are no teleportations on a continuous path. The IVT makes this precise: if f is **continuous** on [a, b] (your prerequisite concept), and N is any value between f(a) and f(b), then there exists at least one c in (a, b) where f(c) = N.

The most powerful application is proving that equations have solutions. To show that f(x) = x³ − x − 1 = 0 has a solution, compute f(1) = 1 − 1 − 1 = −1 (negative) and f(2) = 8 − 2 − 1 = 5 (positive). Since f is continuous (it's a polynomial) and changes sign on [1, 2], the IVT guarantees some c in (1, 2) where f(c) = 0. You've proven the equation has a solution without finding it. This is the typical pattern: evaluate at two points with opposite signs, invoke continuity, conclude existence.

The crucial philosophical point: IVT is an **existence theorem**, not a construction. It guarantees c exists but gives no formula for c, no method to find c, and no information about how many such c exist — there could be one or several. This is a new kind of mathematical reasoning: trapping a solution between two known values proves its existence without locating it. Numerical methods like the bisection algorithm can narrow down c's location, but the IVT alone only promises it's there.

**Continuity is not optional** — the theorem fails without it. The function f(x) = −1 for x < 0 and f(x) = 1 for x ≥ 0 takes both negative and positive values on [−1, 1] but never equals 0, because it jumps at x = 0. Always verify continuity on the entire closed interval before applying IVT. For polynomials, rational functions away from their singularities, and compositions of standard functions, continuity is automatic; for piecewise functions, check at every break point carefully.
