---
id: power-series-complex-plane
title: Power Series in the Complex Plane
domain: mathematics
course: complex-analysis
prerequisites:
- id: taylor-series-complex
  type: hard
- id: uniform-convergence
  type: soft
builds-toward:
- laurent-series
tags:
- power-series
- radius-of-convergence
- uniform-convergence
stage: advanced
status: draft
---

# Power Series in the Complex Plane

## Core Idea
A power series Σ aₙ(z - z₀)^n converges on a disk |z - z₀| < R (the radius of convergence) to a holomorphic function, and diverges outside. On any compact subset of the disk, convergence is uniform. The function can be differentiated and integrated term-by-term inside the radius of convergence.

## Explainer

You've already worked with complex Taylor series, so you know how to represent holomorphic functions as power series. Now the goal is to understand the geometry of convergence in the complex plane and why it differs sharply from the real case.

Over the real line, a power series Σ aₙxⁿ converges on a symmetric interval (−R, R) — a one-dimensional segment. The complex plane has two dimensions, and the natural generalization of an interval centered at a point is a **disk**. The series Σ aₙ(z − z₀)ⁿ converges for all z satisfying |z − z₀| < R, the open disk of radius R centered at z₀. Outside this disk (|z − z₀| > R), the series diverges. On the boundary circle |z − z₀| = R, convergence must be checked individually at each point. The **radius of convergence** R is computed by the Cauchy-Hadamard formula: 1/R = lim sup |aₙ|^{1/n}, or equivalently by the ratio test when the limit exists: 1/R = lim |aₙ₊₁/aₙ|.

The key theorem is that the convergence region is not just an analytic accident — it has deep geometric meaning. The function represented by the power series is **holomorphic** (complex-differentiable) everywhere inside the disk, and conversely, every holomorphic function defined on a disk can be expressed as a power series centered at the center of that disk. Holomorphicity and power-series representability are the same thing in complex analysis, a much stronger equivalence than anything true over the reals (real-smooth functions need not be real-analytic).

Inside the disk, you can differentiate and integrate term-by-term with no concerns about swapping limit and integral — this is justified by **uniform convergence** on compact subsets. Concretely: on any closed disk |z − z₀| ≤ r with r < R, the partial sums converge uniformly. Differentiating the series gives d/dz Σ aₙ(z − z₀)ⁿ = Σ naₙ(z − z₀)ⁿ⁻¹, which has the same radius of convergence R. The derived series represents f′(z), and you can differentiate again to get f″, and so on infinitely. This is why holomorphic functions are automatically infinitely differentiable — a fact with no real analogue.

The boundary circle |z − z₀| = R is where the series cannot converge absolutely, and the function typically has a singularity somewhere on it. This singularity is the reason the radius of convergence stops where it does: the power series "sees" the nearest singularity in the complex plane, even if you started with a real function on the real line. For example, the real function f(x) = 1/(1 + x²) seems well-behaved everywhere on ℝ, but its power series centered at 0 converges only for |x| < 1 — because the complex extension has poles at z = ±i, which are distance 1 from the origin.
