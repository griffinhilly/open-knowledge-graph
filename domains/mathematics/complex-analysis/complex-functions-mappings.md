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
status: validated
---

# Complex Functions and Mappings

## Core Idea
A complex function f: D → ℂ assigns to each z in a domain D ⊆ ℂ a complex number f(z). As functions of two real variables, f(x + iy) = u(x,y) + i v(x,y), complex functions map regions of the plane to regions in the plane, creating geometric transformations that reveal deep structure through their analytic properties.

## How It's Best Learned
Visualize simple functions like f(z) = z², f(z) = 1/z, and f(z) = e^z by drawing what happens to vertical and horizontal lines. Use graphing software to see how circles and lines are transformed. Observe how angles are preserved (or not).

## Common Misconceptions
Thinking complex functions are just two independent real functions; the requirement for analyticity couples them through Cauchy-Riemann. Assuming all continuous functions are analytic; differentiability in the complex sense is much more restrictive.

## Questions

```yaml
- question: "A student defines f(z) = x² − y² + 2ixy (where z = x + iy) and g(z) = x² − y² + 2iy² as two complex-valued functions. From the perspective of complex analysis, what is the key difference?"
  type: multiple-choice
  options:
    - "f is analytic because its real and imaginary parts satisfy the Cauchy-Riemann equations, while g generally does not"
    - "g is analytic because both its components are polynomial in x and y"
    - "Both are equally valid analytic functions — complex analysis only requires the output to be a complex number"
    - "Neither is analytic because they are written in terms of x and y rather than z"
  answer: 0
  explanation: "f(z) = x² − y² + 2ixy = (x + iy)² = z², which is analytic. For g, u = x² − y² and v = 2y². Checking Cauchy-Riemann: ∂u/∂x = 2x but ∂v/∂y = 4y — these are equal only when x = 2y, not everywhere. So g is not analytic. The crucial point: writing f(z) = u(x,y) + iv(x,y) does NOT make it analytic. Analyticity imposes the Cauchy-Riemann coupling between u and v — the condition that elevates a pair of real functions into a genuinely complex-analytic function."

- question: "What does it mean geometrically for a complex function to be conformal at a point where its derivative is non-zero?"
  type: multiple-choice
  options:
    - "The function maps the neighborhood of that point to a disk"
    - "The function maps circles through that point to other circles"
    - "The function preserves angles between any two curves passing through that point"
    - "The function preserves the Euclidean distances between nearby points"
  answer: 2
  explanation: "A conformal map preserves angles and their orientation. At a point z₀ where f'(z₀) ≠ 0, any two smooth curves meeting at angle θ will map to curves meeting at the same angle θ. This is a geometric consequence of complex differentiability: the derivative acts locally like multiplication by a complex number, which rotates and scales uniformly in all directions. Conformality fails exactly where f'(z₀) = 0 (critical points), where the derivative's rotation/scaling is degenerate. This angle-preservation property is what makes conformal maps powerful tools in physics and engineering."

- question: "Writing f(z) = u(x,y) + iv(x,y) shows that any complex function is just a pair of real functions u and v, with no additional constraints between them."
  type: true-false
  answer: false
  explanation: "Any complex-valued function can be written in the form u(x,y) + iv(x,y), but the functions that matter in complex analysis — the analytic (holomorphic) ones — must have u and v satisfy the Cauchy-Riemann equations: ∂u/∂x = ∂v/∂y and ∂u/∂y = −∂v/∂x. This coupling is extremely restrictive: it forces both u and v to be harmonic (satisfying Laplace's equation) and means that specifying u almost entirely determines v (up to a constant). Far from being arbitrary, an analytic function's real and imaginary parts are deeply intertwined."

- question: "The function f(z) = 1/z maps circles that do not pass through the origin to other circles."
  type: true-false
  answer: true
  explanation: "f(z) = 1/z is a Möbius transformation, and Möbius transformations map circles and lines to circles and lines (where a 'line' is a circle of infinite radius). Specifically, circles not passing through the origin map to circles, while circles through the origin map to lines (since z = 0 maps to infinity). This circle-preserving property (with lines as degenerate circles) is fundamental to the study of Möbius transformations and conformal mapping, and it can be verified algebraically by substituting the general equation of a circle into w = 1/z and simplifying."

- question: "Why is complex differentiability a far more restrictive condition than real differentiability, even though both are defined as limits of difference quotients? What geometric consequence does this extra restrictiveness have?"
  type: short-answer
  answer: "Real differentiability requires only that the limit of [f(x+h)−f(x)]/h exists as h→0 along the real line. Complex differentiability requires the limit of [f(z+h)−f(z)]/h to exist as h→0 from ANY direction in the complex plane — horizontally, vertically, diagonally, or along any curve. This imposes the Cauchy-Riemann equations as a necessary condition, tightly coupling the real and imaginary parts. The geometric consequence is conformality: because the derivative is a single complex number (not a 2×2 matrix), it acts on directions uniformly — rotating and scaling by the same amount in every direction. This is angle preservation."
  explanation: "In real analysis, a function can be differentiable yet quite 'wild' (e.g., differentiable once but not twice). In complex analysis, once-differentiable (analytic) implies infinitely differentiable, and in fact implies the function equals its Taylor series everywhere in its domain. This extraordinary rigidity — one complex derivative implies all — is entirely due to the Cauchy-Riemann coupling. Geometrically, every analytic function with nonzero derivative is a conformal map: it looks locally like a rotation and stretching, the same in every direction, which is why complex analysis is so useful in fluid dynamics, electrostatics, and potential theory."
```

## Explainer

You are already comfortable with the complex plane as a two-dimensional space, where a point z = x + iy carries both a real part x and an imaginary part y. A complex function f: D → ℂ is a rule that moves every point z in some domain D to a new complex number f(z). Because both input and output are two-dimensional, a complex function is simultaneously a **mapping** from one region of the plane to another — and visualizing what the mapping does geometrically is one of the central skills of complex analysis.

Write f(z) = f(x + iy) = u(x, y) + i v(x, y). The two real-valued functions u and v are the **real and imaginary parts** of f. In principle, you could choose u and v to be any two real functions of x and y — but doing so would not generally give a complex function with any special structure. The functions that matter in complex analysis are the **analytic** (holomorphic) ones, where u and v are tightly coupled through the Cauchy-Riemann equations. That coupling is what makes complex differentiation far more restrictive — and far more powerful — than real differentiation.

To build geometric intuition, consider three key examples. The function f(z) = z² maps a grid of horizontal and vertical lines to a grid of parabolas that intersect at right angles. The function f(z) = 1/z turns circles through the origin into lines, and circles not through the origin into other circles — an inversion that reverses inside and outside. The function f(z) = eˣ(cos y + i sin y) maps every horizontal strip of height 2π to the entire complex plane (except zero), and maps vertical lines to circles. Each of these is a **conformal map** — it preserves angles between curves at every point where the derivative is non-zero.

Understanding mappings by their geometric action on simple sets (horizontal lines, vertical lines, circles) is the standard technique. Draw the **domain grid** and then track where the gridlines go. Where horizontal lines and vertical lines map to orthogonal curves in the image, conformality is visible. Where gridlines get crowded together, the function is compressing; where they spread apart, it is stretching. This visual vocabulary — domains mapping to other domains, angles preserved, shapes transformed — is the language you will use throughout complex analysis to understand limits, derivatives, integrals, and the behavior of analytic functions at their zeros and singularities.
