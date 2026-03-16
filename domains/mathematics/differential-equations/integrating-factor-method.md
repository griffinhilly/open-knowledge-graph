---
id: integrating-factor-method
title: Integrating Factor Method for First-Order Linear ODEs
domain: mathematics
course: differential-equations
prerequisites:
- id: separable-differential-equations
  type: hard
builds-toward:
- exact-differential-equations
- first-order-linear-odes
tags:
- integrating-factor
- first-order
- linear
stage: formal-systems
status: draft
---

# Integrating Factor Method for First-Order Linear ODEs

## Core Idea
For a first-order linear ODE of the form dy/dx + P(x)y = Q(x), an integrating factor μ(x) = e^(∫P(x)dx) transforms the left side into the derivative of a product: d/dx[μ(x)y] = μ(x)Q(x). This makes the equation directly integrable, converting a challenging linear equation into a solvable form. The integrating factor is one of the most powerful techniques in differential equations.

## Explainer

You've already solved separable differential equations by getting all the y-terms on one side and all the x-terms on the other, then integrating both sides. That works beautifully when the equation separates — but dy/dx + P(x)y = Q(x) generally cannot be separated if Q(x) ≠ 0. A different strategy is needed: rather than rearranging the equation, multiply both sides by a carefully chosen function to create a pattern you recognize.

The goal is to turn the left side y′ + P(x)y into the derivative of a product. Recall the product rule: d/dx[μ(x)y] = μ(x)y′ + μ′(x)y. Compare this to μ(x)·(y′ + P(x)y) = μ(x)y′ + μ(x)P(x)y. For these to be equal, you need μ′(x) = μ(x)P(x). This is itself a separable ODE: dμ/μ = P(x)dx. Integrating both sides gives ln|μ| = ∫P(x)dx, so **μ(x) = e^{∫P(x)dx}**. The constant of integration is dropped because any particular μ works — the simplest one suffices.

To see the method in action, consider y′ + (2/x)y = x². Here P(x) = 2/x, so μ(x) = e^{∫2/x dx} = e^{2 ln x} = x². Multiply both sides by x²: x²y′ + 2xy = x⁴. The left side is now d/dx[x²y] by the product rule. Integrate both sides: x²y = ∫x⁴ dx = x⁵/5 + C. Divide by x²: y = x³/5 + C/x². The integrating factor converted an unseparable equation into a straightforward integration.

The algorithm in full: (1) rewrite the equation in standard form y′ + P(x)y = Q(x), identifying P and Q. (2) Compute μ(x) = e^{∫P(x)dx}. (3) Multiply both sides by μ. (4) Recognize the left side as d/dx[μy] and write it that way. (5) Integrate both sides. (6) Solve for y. Each step has a clear mechanical purpose, and the method always works for first-order linear equations — unlike separation of variables, which only applies to a restricted class.
