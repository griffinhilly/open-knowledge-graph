---
id: complex-functions-mappings
title: Complex Functions and Mappings
domain: mathematics
course: complex-analysis
prerequisites:
- id: complex-plane
  type: hard
- id: topological-spaces-complex-plane
  type: soft
builds-toward:
- limits-continuity-complex-functions
- complex-differentiability
tags:
- functions
- mappings
- domains
stage: advanced
status: draft
---

# Complex Functions and Mappings

## Core Idea
A complex function f: D → ℂ assigns to each z in a domain D ⊆ ℂ a complex number f(z). As functions of two real variables, f(x + iy) = u(x,y) + i v(x,y), complex functions map regions of the plane to regions in the plane, creating geometric transformations that reveal deep structure through their analytic properties.

## How It's Best Learned
Visualize simple functions like f(z) = z², f(z) = 1/z, and f(z) = e^z by drawing what happens to vertical and horizontal lines. Use graphing software to see how circles and lines are transformed. Observe how angles are preserved (or not).

## Common Misconceptions
Thinking complex functions are just two independent real functions; the requirement for analyticity couples them through Cauchy-Riemann. Assuming all continuous functions are analytic; differentiability in the complex sense is much more restrictive.

## Explainer

You are already comfortable with the complex plane as a two-dimensional space, where a point z = x + iy carries both a real part x and an imaginary part y. A complex function f: D → ℂ is a rule that moves every point z in some domain D to a new complex number f(z). Because both input and output are two-dimensional, a complex function is simultaneously a **mapping** from one region of the plane to another — and visualizing what the mapping does geometrically is one of the central skills of complex analysis.

Write f(z) = f(x + iy) = u(x, y) + i v(x, y). The two real-valued functions u and v are the **real and imaginary parts** of f. In principle, you could choose u and v to be any two real functions of x and y — but doing so would not generally give a complex function with any special structure. The functions that matter in complex analysis are the **analytic** (holomorphic) ones, where u and v are tightly coupled through the Cauchy-Riemann equations. That coupling is what makes complex differentiation far more restrictive — and far more powerful — than real differentiation.

To build geometric intuition, consider three key examples. The function f(z) = z² maps a grid of horizontal and vertical lines to a grid of parabolas that intersect at right angles. The function f(z) = 1/z turns circles through the origin into lines, and circles not through the origin into other circles — an inversion that reverses inside and outside. The function f(z) = eˣ(cos y + i sin y) maps every horizontal strip of height 2π to the entire complex plane (except zero), and maps vertical lines to circles. Each of these is a **conformal map** — it preserves angles between curves at every point where the derivative is non-zero.

Understanding mappings by their geometric action on simple sets (horizontal lines, vertical lines, circles) is the standard technique. Draw the **domain grid** and then track where the gridlines go. Where horizontal lines and vertical lines map to orthogonal curves in the image, conformality is visible. Where gridlines get crowded together, the function is compressing; where they spread apart, it is stretching. This visual vocabulary — domains mapping to other domains, angles preserved, shapes transformed — is the language you will use throughout complex analysis to understand limits, derivatives, integrals, and the behavior of analytic functions at their zeros and singularities.
