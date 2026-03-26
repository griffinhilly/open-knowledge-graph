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
status: validated
---

# Power Series in the Complex Plane

## Core Idea
A power series Σ aₙ(z - z₀)^n converges on a disk |z - z₀| < R (the radius of convergence) to a holomorphic function, and diverges outside. On any compact subset of the disk, convergence is uniform. The function can be differentiated and integrated term-by-term inside the radius of convergence.

## Questions

```yaml
- question: "The function f(x) = 1/(1 + x²) is smooth and well-defined for all real x. Yet its Taylor series centered at 0 converges only for |x| < 1. What is the correct explanation?"
  type: multiple-choice
  options:
    - "The Taylor series is computed incorrectly; 1/(1+x²) should have an infinite radius of convergence since it has no real singularities"
    - "The series converges only where the function is analytic, and 1/(1+x²) has a singularity at x = 1"
    - "The complex extension 1/(1+z²) has poles at z = ±i, which are distance 1 from the origin, limiting the radius of convergence"
    - "Convergence is limited to |x| < 1 because the function oscillates rapidly near x = ±1"
  answer: 2
  explanation: "The radius of convergence equals the distance from the center of expansion to the nearest singularity in the *complex* plane. The complex extension f(z) = 1/(1+z²) has poles at z = i and z = −i, both distance 1 from the origin. Even though these poles are purely imaginary and the real function is smooth everywhere on ℝ, the power series 'sees' them. The key insight is that power series convergence is determined by singularities that may be invisible when you look only at the real line."

- question: "Inside the radius of convergence, a complex power series converges to a function that is..."
  type: multiple-choice
  options:
    - "Continuous but not necessarily differentiable"
    - "Infinitely differentiable in the real sense, but not complex-differentiable"
    - "Holomorphic — complex-differentiable at every point inside the disk — and therefore infinitely differentiable"
    - "Holomorphic only at the center z₀, with decreasing differentiability toward the boundary"
  answer: 2
  explanation: "A fundamental theorem of complex analysis states that the sum of a convergent power series is holomorphic throughout its disk of convergence. Holomorphic means complex-differentiable — and complex differentiability is much stronger than real differentiability. Holomorphic functions are automatically infinitely differentiable (differentiating the power series term-by-term any number of times yields a series with the same radius of convergence). There is no real analogue: real-smooth functions need not be real-analytic."

- question: "The power series for 1/(1+x²) centered at x = 0 converges for most real x because the function is smooth on most of ℝ."
  type: true-false
  answer: false
  explanation: "This is the key misconception this topic corrects. Smoothness on ℝ does not guarantee convergence everywhere on ℝ. The radius of convergence is determined by singularities in the *complex* plane, which may lie off the real axis entirely. For 1/(1+z²), the complex poles at z = ±i are distance 1 from the origin, so the power series converges only for |z| < 1. The series diverges for |x| > 1 even though the real function is perfectly smooth there."

- question: "On any compact subset of the disk of convergence, a complex power series converges uniformly, which justifies term-by-term differentiation and integration."
  type: true-false
  answer: true
  explanation: "Uniform convergence on compact subsets (closed disks |z − z₀| ≤ r for r < R) is what permits swapping the limit with differentiation and integration. On such subsets the partial sums converge uniformly, and uniform convergence interchanges with integrals and derivatives. This is why the derivative of a power series is computed by differentiating term-by-term, and the resulting series converges on the same open disk with the same radius of convergence R."

- question: "Explain why the radius of convergence of a complex power series is determined by the nearest singularity in the complex plane, and use this to explain why the power series for 1/(1+x²) centered at 0 does not converge for all real x despite the function being smooth on ℝ."
  type: short-answer
  answer: "A power series represents a holomorphic function inside its disk of convergence. Holomorphic functions cannot be continued through singularities — at a singularity the function ceases to be defined or differentiable. The disk of convergence is the largest disk centered at z₀ in which the represented function is holomorphic, which means it extends up to (but not past) the nearest singularity. For 1/(1+z²), the singularities are poles at z = ±i, distance 1 from the origin. Even though these poles lie off the real axis, the power series along the real line still 'feels' their presence, and convergence stops at radius 1."
  explanation: "This example shows why complex analysis and real analysis cannot be fully separated: to understand real power series, you must look in the complex plane. The function 1/(1+x²) looks innocent on ℝ but harbors invisible obstacles just off-axis that limit where its Taylor series converges."
```

## Explainer

You've already worked with complex Taylor series, so you know how to represent holomorphic functions as power series. Now the goal is to understand the geometry of convergence in the complex plane and why it differs sharply from the real case.

Over the real line, a power series Σ aₙxⁿ converges on a symmetric interval (−R, R) — a one-dimensional segment. The complex plane has two dimensions, and the natural generalization of an interval centered at a point is a **disk**. The series Σ aₙ(z − z₀)ⁿ converges for all z satisfying |z − z₀| < R, the open disk of radius R centered at z₀. Outside this disk (|z − z₀| > R), the series diverges. On the boundary circle |z − z₀| = R, convergence must be checked individually at each point. The **radius of convergence** R is computed by the Cauchy-Hadamard formula: 1/R = lim sup |aₙ|^{1/n}, or equivalently by the ratio test when the limit exists: 1/R = lim |aₙ₊₁/aₙ|.

The key theorem is that the convergence region is not just an analytic accident — it has deep geometric meaning. The function represented by the power series is **holomorphic** (complex-differentiable) everywhere inside the disk, and conversely, every holomorphic function defined on a disk can be expressed as a power series centered at the center of that disk. Holomorphicity and power-series representability are the same thing in complex analysis, a much stronger equivalence than anything true over the reals (real-smooth functions need not be real-analytic).

Inside the disk, you can differentiate and integrate term-by-term with no concerns about swapping limit and integral — this is justified by **uniform convergence** on compact subsets. Concretely: on any closed disk |z − z₀| ≤ r with r < R, the partial sums converge uniformly. Differentiating the series gives d/dz Σ aₙ(z − z₀)ⁿ = Σ naₙ(z − z₀)ⁿ⁻¹, which has the same radius of convergence R. The derived series represents f′(z), and you can differentiate again to get f″, and so on infinitely. This is why holomorphic functions are automatically infinitely differentiable — a fact with no real analogue.

The boundary circle |z − z₀| = R is where the series cannot converge absolutely, and the function typically has a singularity somewhere on it. This singularity is the reason the radius of convergence stops where it does: the power series "sees" the nearest singularity in the complex plane, even if you started with a real function on the real line. For example, the real function f(x) = 1/(1 + x²) seems well-behaved everywhere on ℝ, but its power series centered at 0 converges only for |x| < 1 — because the complex extension has poles at z = ±i, which are distance 1 from the origin.
