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

## Questions

```yaml
- question: "A student interpolating 25 uniformly spaced data points finds wild oscillations near the endpoints and proposes using a degree-40 polynomial to get a better fit. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "A degree-40 polynomial cannot interpolate more than 40 points"
    - "Increasing polynomial degree worsens Runge's phenomenon — oscillations near the endpoints grow as degree increases for uniform nodes"
    - "The student should use Chebyshev nodes instead of a higher-degree polynomial, but the degree itself is not the problem"
    - "High-degree polynomials are too slow to compute for practical use"
  answer: 1
  explanation: "This is exactly Runge's phenomenon: for uniformly spaced nodes, a high-degree global polynomial interpolant oscillates increasingly near the endpoints as degree grows. The solution is NOT to add more degrees — it is to switch to a piecewise approach (like cubic splines) that keeps the polynomial degree low on each interval while enforcing smooth joins between pieces."

- question: "What makes the linear system that arises when constructing a natural cubic spline particularly efficient to solve?"
  type: multiple-choice
  options:
    - "The system is diagonal, so each unknown can be solved independently"
    - "The system is small — it always has exactly 3 unknowns regardless of n"
    - "The system is tridiagonal, symmetric, and diagonally dominant, allowing O(n) solution via the Thomas algorithm"
    - "The spline coefficients can be read directly from the data without solving any system"
  answer: 2
  explanation: "Setting up the interior second-derivative conditions produces a tridiagonal system — each equation involves only three consecutive unknowns. This sparsity, combined with diagonal dominance, makes the Thomas algorithm applicable, solving the system in O(n) time. This is one of the key practical advantages of cubic splines over direct high-degree polynomial interpolation."

- question: "A natural cubic spline is called 'natural' because it mimics the shape an elastic rod (drafting spline) takes when forced through data points — it minimizes bending energy."
  type: true-false
  answer: true
  explanation: "This is exactly right. Minimizing bending energy corresponds mathematically to minimizing ∫[S''(x)]² dx, which is precisely what the natural cubic spline achieves when the second derivatives at the endpoints are set to zero. The physical analogy is not decorative — it is the mechanical origin of the construction."

- question: "Cubic splines achieve high accuracy primarily by using higher-degree polynomials than simpler interpolants — the cubic degree is what buys smoothness."
  type: true-false
  answer: false
  explanation: "The accuracy and smoothness of cubic splines come from enforcing C² continuity (matching first and second derivatives) at interior nodes, not merely from using cubic polynomials. Each piece is still a low-degree (cubic) polynomial; what distinguishes the spline is the derivative-matching conditions across pieces. You could have piecewise cubics without these conditions and get a much rougher result."

- question: "Why do cubic splines require boundary conditions, and what are the two most common choices?"
  type: short-answer
  answer: "With n+1 nodes, a cubic spline has n cubic pieces, each with 4 coefficients — 4n parameters. The interpolation and C² interior conditions supply 4n−2 constraints, leaving 2 free. Boundary conditions close the system. The natural spline sets S''=0 at both endpoints (zero curvature, minimizing bending). The clamped spline specifies S' at the endpoints using known derivative data."
  explanation: "Without boundary conditions the system is underdetermined — infinitely many cubic splines pass through the same data. The boundary conditions make the solution unique. The natural choice is appropriate when no derivative data is available; the clamped choice is more accurate when endpoint derivative information is known (e.g., from the physical problem generating the data)."
```

## Explainer

If you've studied interpolation error analysis, you've seen one fundamental problem with high-degree polynomial interpolation: adding more data points can actually *worsen* the fit, particularly near the endpoints. This is **Runge's phenomenon** — oscillations that grow unboundedly for uniformly spaced nodes as the polynomial degree increases. The fix is not to use a single high-degree polynomial, but to break the domain into pieces, fit a low-degree polynomial on each piece, and stitch them together smoothly. This is the **spline** idea.

A **cubic spline** on n+1 nodes x₀ < x₁ < ... < xₙ is a piecewise cubic polynomial S(x) satisfying three conditions: (1) S(xᵢ) matches the data value at each node, (2) the pieces join continuously at interior nodes, and (3) the first and second derivatives also match at each interior junction. The C² smoothness condition — continuous up to the second derivative — is what makes the result look visually smooth: no kinks and no sudden changes in curvature. A physical analogy: a thin elastic rod forced through the data points naturally minimizes bending energy, which corresponds mathematically to minimizing ∫[S''(x)]² dx. The natural cubic spline achieves exactly this minimum, making it the shape a drafting spline would take.

Setting up the spline requires solving a **tridiagonal linear system** for the second derivatives at interior nodes. This system is sparse, symmetric, and diagonally dominant — properties that make it extremely fast to solve (O(n) time using the Thomas algorithm) and numerically stable. Two **boundary conditions** must be specified to close the system, since n−1 interior second derivatives give n−1 equations but you have n cubic pieces requiring 4n − 3 constraints. The most common choices are the **natural spline** (S'' = 0 at the endpoints, minimizing curvature there) or the **clamped spline** (specify S' at the endpoints when derivative data is available).

The payoff is that cubic splines achieve near-optimal interpolation accuracy — O(h⁴) error on n intervals with spacing h — without the endpoint blowup of global high-degree polynomials. This makes them the default choice in computer graphics (smooth Bézier-style curves through control points), CAD/CAM (smooth tool paths in numerical machining), and scientific computing (interpolating tabulated data like thermodynamic properties). The key insight is that smoothness and stability come not from higher-degree polynomials globally, but from enforcing derivative continuity locally across piecewise low-degree pieces. The tradeoff you paid — solving a linear system instead of evaluating a single formula — is minimal, and the gain in stability is enormous.
