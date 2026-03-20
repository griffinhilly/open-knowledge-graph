---
id: radical-functions-and-graphs
title: Radical Functions and Graphs
domain: mathematics
course: algebra-2
prerequisites:
  - id: square-roots-intro
    type: hard
  - id: inverse-functions
    type: soft
builds-toward:
  - solving-radical-equations
  - rational-exponents
tags: [radicals, functions, graphing, domain, square-root]
stage: formal-systems
status: validated
---

# Radical Functions and Graphs

## Core Idea
A radical function involves a variable under a radical sign, such as f(x) = sqrt(x), cbrt(x), or sqrt(ax + b). The square root function has domain [0, infinity) and range [0, infinity), producing a half-parabola shape. Transformations (shifts, stretches, reflections) apply as usual. The cube root function has domain and range both all reals. Radical functions are inverses of power functions (restricted to appropriate domains).

## How It's Best Learned
Graph the parent functions y = sqrt(x) and y = cbrt(x). Apply transformations systematically: y = a*sqrt(x - h) + k. Discuss domain restrictions (radicand must be non-negative for even roots). Connect to inverse functions: y = sqrt(x) is the inverse of y = x^2 for x >= 0.

## Common Misconceptions
- Thinking sqrt(x) is defined for negative x (it is not, in the reals).
- Confusing domain restrictions for even and odd roots (even roots require non-negative radicand; odd roots accept all reals).
- Forgetting that y = sqrt(x) gives only the positive root, not both.

## Explainer

You already understand square roots as numbers: √9 = 3 because 3² = 9. A **radical function** makes the input itself a variable: f(x) = √x. This seemingly small change — replacing a number under the radical with x — creates a function with a shape you have not seen before, and its shape is directly explained by your prerequisite knowledge about inverse functions.

Think of it this way: the function g(x) = x² takes any non-negative number and squares it. The square root function f(x) = √x undoes that squaring — it is the inverse of g, but only on the restricted domain x ≥ 0. (You need the restriction because squaring loses sign information: both 3 and −3 square to 9, so the full squaring function cannot be inverted without a restriction.) The graph of f(x) = √x is the graph of g(x) = x² reflected across the line y = x, which explains its curved shape — it starts at the origin and bends upward more and more slowly as x increases. The **domain** is [0, ∞) and the **range** is [0, ∞).

The cube root function f(x) = ∛x behaves differently because cubing never loses sign information: (−2)³ = −8 and 2³ = 8 are distinct, so the full cubic is invertible on all of ℝ. This is why ∛x has domain and range both equal to all real numbers, and its graph passes through the origin with an S-shape. More generally, **even-index radicals** (√, ⁴√, etc.) require a non-negative radicand and produce non-negative outputs; **odd-index radicals** (∛, ⁵√, etc.) accept any real number and can produce negative outputs.

Transformations apply to radical functions exactly as they do to any function. For f(x) = a·√(x − h) + k: shifting by h moves the starting point horizontally (h > 0 shifts right), shifting by k moves it vertically, and a stretches or compresses it vertically — a negative a reflects the curve below the x-axis. The **domain** shifts with h: f(x) = √(x − 3) is only defined for x ≥ 3. Identifying the domain from the formula means setting the radicand ≥ 0 (for even roots) and solving for x.
