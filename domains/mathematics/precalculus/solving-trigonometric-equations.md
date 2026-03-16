---
id: solving-trigonometric-equations
title: Solving Trigonometric Equations
domain: mathematics
course: precalculus
prerequisites:
- id: inverse-trigonometric-functions
  type: hard
- id: trigonometric-identities-pythagorean
  type: hard
- id: unit-circle
  type: hard
- id: double-angle-identities
  type: soft
- id: half-angle-identities
  type: soft
- id: sum-and-difference-identities
  type: soft
builds-toward:
- differential-equations-intro-separable
tags:
- trigonometry
- equations
- solving
stage: formal-systems
status: validated
---
# Solving Trigonometric Equations

## Core Idea
Solving trigonometric equations means finding all angles that satisfy a given equation. The process typically involves isolating the trig function using algebraic techniques and identities, finding reference angles using inverse trig functions, then accounting for periodicity to list all solutions (either in a given interval or as a general solution with + 2*pi*n). This skill ties together everything from the trig unit.

## How It's Best Learned
Start with basic equations like sin(x) = 1/2, find solutions on [0, 2*pi), then write general solutions. Progress to equations requiring identities (e.g., 2sin^2(x) - 1 = 0 using Pythagorean identity) and factoring. Emphasize the systematic approach: isolate, solve, list all solutions.

## Common Misconceptions
- Finding only one solution when there are multiple in the given interval.
- Forgetting to account for periodicity in the general solution.
- Dividing both sides by a trig function, which loses solutions where that function is zero.

## Explainer

Solving a trigonometric equation is like solving any algebraic equation, but with one critical difference: trig functions are periodic, so equations almost always have infinitely many solutions. Your three core prerequisites — the **unit circle**, **inverse trig functions**, and **Pythagorean identities** — give you exactly the tools to find and organize all of them.

The unit circle is your lookup table. You know that sin(θ) = 1/2 at θ = π/6 and θ = 5π/6 in [0, 2π), and then again every 2π beyond that. The **inverse trig function** arcsin(1/2) = π/6 gives you the reference angle — the first-quadrant solution. But inverse trig functions only return one value (their range is restricted), so you must use the unit circle to find all solutions in the target interval. For sin, a positive value appears in quadrants I and II; for cos, in quadrants I and IV; for tan, in quadrants I and III. The second solution is found by symmetry: for sin(θ) = k > 0, the two solutions in [0, 2π) are arcsin(k) and π − arcsin(k). The **general solution** packages all of them: for sin(θ) = k, write θ = arcsin(k) + 2πn and θ = (π − arcsin(k)) + 2πn for all integers n.

When the equation is more complex, you first simplify using identities before applying this procedure. The **Pythagorean identity** sin²x + cos²x = 1 lets you convert between functions to get an equation in a single trig function. For example, 2sin²x − sinx − 1 = 0 factors as (2sinx + 1)(sinx − 1) = 0, giving sinx = −1/2 or sinx = 1. Solve each case separately using the unit circle. Similarly, a double-angle identity like cos(2x) = 1 − 2sin²x can reduce a degree-2 problem to a linear one. The general strategy is always: isolate one trig function (or factor to get separate simple equations), find the reference angle, use the unit circle to list all solutions in the required interval, and state the general solution with the ± 2πn period.

One dangerous shortcut is **dividing both sides by a trig function** to simplify. For instance, given sinx · cosx = sinx, you might divide by sinx to get cosx = 1. But this discards the solutions where sinx = 0 (namely x = 0, π, 2π, …). The safe approach is to move everything to one side and factor: sinx · cosx − sinx = 0, so sinx(cosx − 1) = 0, giving sinx = 0 or cosx = 1 as two separate cases, both of which must be solved. Factoring preserves all solutions; division hides the ones that make the divisor zero.
