---
id: cubic-spline-interpolation
title: Cubic Spline Interpolation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: chebyshev-nodes
  type: soft
- id: interpolation-error-analysis
  type: hard
tags:
- splines
- cubic
- interpolation
stage: advanced
status: draft
---

# Cubic Spline Interpolation

## Core Idea
Cubic spline interpolation uses piecewise cubic polynomials with continuous first and second derivatives at the nodes. This approach avoids Runge's phenomenon and produces smooth, stable interpolants without oscillation. Cubic splines are widely used in computer graphics, CAD, and numerical analysis because they balance smoothness with computational efficiency.

## Explainer

If you've studied interpolation error analysis, you've seen one fundamental problem with high-degree polynomial interpolation: adding more data points can actually *worsen* the fit, particularly near the endpoints. This is **Runge's phenomenon** — oscillations that grow unboundedly for uniformly spaced nodes as the polynomial degree increases. The fix is not to use a single high-degree polynomial, but to break the domain into pieces, fit a low-degree polynomial on each piece, and stitch them together smoothly. This is the **spline** idea.

A **cubic spline** on n+1 nodes x₀ < x₁ < ... < xₙ is a piecewise cubic polynomial S(x) satisfying three conditions: (1) S(xᵢ) matches the data value at each node, (2) the pieces join continuously at interior nodes, and (3) the first and second derivatives also match at each interior junction. The C² smoothness condition — continuous up to the second derivative — is what makes the result look visually smooth: no kinks and no sudden changes in curvature. A physical analogy: a thin elastic rod forced through the data points naturally minimizes bending energy, which corresponds mathematically to minimizing ∫[S''(x)]² dx. The natural cubic spline achieves exactly this minimum, making it the shape a drafting spline would take.

Setting up the spline requires solving a **tridiagonal linear system** for the second derivatives at interior nodes. This system is sparse, symmetric, and diagonally dominant — properties that make it extremely fast to solve (O(n) time using the Thomas algorithm) and numerically stable. Two **boundary conditions** must be specified to close the system, since n−1 interior second derivatives give n−1 equations but you have n cubic pieces requiring 4n − 3 constraints. The most common choices are the **natural spline** (S'' = 0 at the endpoints, minimizing curvature there) or the **clamped spline** (specify S' at the endpoints when derivative data is available).

The payoff is that cubic splines achieve near-optimal interpolation accuracy — O(h⁴) error on n intervals with spacing h — without the endpoint blowup of global high-degree polynomials. This makes them the default choice in computer graphics (smooth Bézier-style curves through control points), CAD/CAM (smooth tool paths in numerical machining), and scientific computing (interpolating tabulated data like thermodynamic properties). The key insight is that smoothness and stability come not from higher-degree polynomials globally, but from enforcing derivative continuity locally across piecewise low-degree pieces. The tradeoff you paid — solving a linear system instead of evaluating a single formula — is minimal, and the gain in stability is enormous.
