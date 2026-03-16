---
id: rolles-theorem
title: "Rolle's Theorem"
domain: mathematics
course: calculus-1
prerequisites:
  - id: continuity-definition
    type: hard
  - id: derivative-as-slope-of-tangent
    type: hard
builds-toward:
  - mean-value-theorem
tags: [theorems, Rolle, existence-theorems]
stage: formal-systems
status: validated
---

# Rolle's Theorem

## Core Idea
Rolle's Theorem is a special case of the Mean Value Theorem: if f is continuous on [a, b], differentiable on (a, b), and f(a) = f(b), then there exists at least one c in (a, b) where f'(c) = 0. Geometrically, if a smooth curve starts and ends at the same height, it must have at least one horizontal tangent in between. Rolle's Theorem is the stepping stone to proving the full MVT.

## How It's Best Learned
Visualize: draw curves that start and end at the same height and find where the tangent is horizontal. Verify with specific polynomial examples. Emphasize the three hypotheses and what can go wrong if any is violated.

## Common Misconceptions
- Applying Rolle's Theorem when f(a) does not equal f(b).
- Forgetting to check differentiability (|x| satisfies continuity and f(-1) = f(1) but has no horizontal tangent).
- Assuming the c given by Rolle's Theorem must be unique.

## Explainer

You know that a function's derivative describes its slope, and that the slope is zero wherever the function has a local maximum or minimum. Rolle's Theorem turns that observation into a formal guarantee: if a smooth curve begins and ends at the *same height*, something must have caused it to turn around in between, and that turning point is where the slope is exactly zero.

The three hypotheses are each essential. **Continuity on [a, b]** rules out jumps — a function that teleports can go from height h back to height h without ever having a horizontal tangent. **Differentiability on (a, b)** rules out corners — the absolute value function |x| satisfies f(-1) = f(1) = 1 and is continuous everywhere, but at x = 0 the derivative is undefined and f'(x) = ±1 everywhere it exists (never zero). **Equal endpoint values f(a) = f(b)** is the third condition; dropping it kills the conclusion immediately: f(x) = x is smooth on [0, 1] with f'(x) = 1 everywhere.

Think of a race: a runner starts and finishes at the same point on a circular track, and their position as a function of time is continuous and smooth. At some moment during the race, they must have been momentarily moving directly away from the finish at zero net progress — equivalently, velocity is zero at some turning point. That's exactly what Rolle's Theorem says. Concretely: f(x) = x³ - x on [-1, 1] has f(-1) = 0 = f(1), so the theorem applies. f'(x) = 3x² - 1 = 0 gives x = ±1/√3 ≈ ±0.577, both inside (-1, 1). The theorem guarantees at least one such c — here there are two.

Rolle's Theorem matters primarily as the foundation for the **Mean Value Theorem**, your next topic. The MVT generalizes it to the case where f(a) ≠ f(b): instead of a horizontal tangent, you get a tangent parallel to the secant line. The proof of the MVT constructs a new function h(x) = f(x) - [line from (a, f(a)) to (b, f(b))], which *does* satisfy h(a) = h(b) = 0, then applies Rolle's. Understanding Rolle's Theorem deeply — especially which hypotheses are doing the work and what fails when they're violated — gives you immediate leverage on the MVT and the many results that flow from it.
