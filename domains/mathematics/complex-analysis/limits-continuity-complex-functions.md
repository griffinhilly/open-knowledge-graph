---
id: limits-continuity-complex-functions
title: Limits and Continuity of Complex Functions
domain: mathematics
course: complex-analysis
prerequisites:
- id: convergence-complex-sequences
  type: hard
- id: complex-functions-mappings
  type: hard
builds-toward:
- complex-differentiability
- holomorphic-functions
tags:
- limits
- continuity
- topology
stage: advanced
status: validated
---

# Limits and Continuity of Complex Functions

## Core Idea
A function f has limit L at z₀ if lim(z→z₀) f(z) = L means for every ε > 0 there exists δ > 0 such that |z - z₀| < δ implies |f(z) - L| < ε. A function is continuous at z₀ if lim(z→z₀) f(z) = f(z₀). Continuity is equivalent to each real part u and imaginary part v being continuous as functions from ℝ² to ℝ.

## Questions

```yaml
- question: "Consider f(z) = Re(z)/|z| for z ≠ 0 and f(0) = 0. What happens as z → 0?"
  type: multiple-choice
  options:
    - "The limit is 0, because both the numerator and denominator approach 0"
    - "The limit is 1, because Re(z) ≈ |z| for real z"
    - "The limit does not exist, because the value along the real axis differs from the value along the imaginary axis"
    - "The limit exists and equals 1/2 by averaging the real and imaginary approach directions"
  answer: 2
  explanation: "Along the positive real axis z = x > 0: Re(z)/|z| = x/x = 1. Along the positive imaginary axis z = iy, y > 0: Re(z)/|z| = 0/y = 0. The limit along two different paths gives different values (1 and 0), so the limit does not exist at 0. In the complex plane, a limit must agree along every possible path — not just two directions as in real analysis. This is the key difference from real analysis and exactly the kind of reasoning required for complex limits."

- question: "Which statement correctly describes the component criterion for limits of complex functions?"
  type: multiple-choice
  options:
    - "lim_{z→z₀} f(z) = L if and only if |f(z) - L| < ε whenever z is within δ of z₀, for the single approach along the real axis"
    - "lim_{z→z₀} f(z) = L if and only if lim_{(x,y)→(x₀,y₀)} u(x,y) = Re(L) and lim_{(x,y)→(x₀,y₀)} v(x,y) = Im(L) as real multivariable limits"
    - "lim_{z→z₀} f(z) = L if and only if the real and imaginary parts of f are bounded near z₀"
    - "lim_{z→z₀} f(z) = L if and only if f has no poles in a neighborhood of z₀"
  answer: 1
  explanation: "The component criterion reduces a complex limit to two real multivariable limits: the real part u(x,y) and imaginary part v(x,y) must each converge to the corresponding real/imaginary parts of L as (x,y) → (x₀,y₀) in ℝ². This is both necessary and sufficient. The power of this criterion is that it leverages your existing knowledge of real multivariable limits — no new conceptual apparatus is needed beyond the requirement that both components converge simultaneously."

- question: "If lim_{z→z₀} f(z) = L along the real axis and lim_{z→z₀} f(z) = L along the imaginary axis (both giving the same value L), then lim_{z→z₀} f(z) = L."
  type: true-false
  answer: false
  explanation: "Agreement along two paths is not sufficient for a complex limit to exist. In the complex plane, z can approach z₀ along infinitely many paths — rays, spirals, curves — and the limit must agree along all of them. A function can give the same value along the real and imaginary axes yet different values along paths like z = te^{iπ/4} (at a 45-degree angle). For a real function f: ℝ → ℝ, agreement of one-sided limits is sufficient because there are only two approach directions; in ℂ, infinitely many directions must all agree."

- question: "A complex function f(z) = u(x,y) + iv(x,y) is continuous at z₀ = x₀ + iy₀ if and only if both u and v are continuous as real functions from ℝ² to ℝ at (x₀, y₀)."
  type: true-false
  answer: true
  explanation: "This is the component criterion for continuity, and it is an exact equivalence. Continuity of f at z₀ means lim_{z→z₀} f(z) = f(z₀), which by the component criterion is equivalent to lim_{(x,y)→(x₀,y₀)} u(x,y) = u(x₀,y₀) and lim_{(x,y)→(x₀,y₀)} v(x,y) = v(x₀,y₀) — precisely continuity of u and v as real functions. There is no additional 'complex' condition beyond these two real conditions. This makes checking continuity of complex functions reducible to real analysis."

- question: "Why is approaching a point z₀ in the complex plane fundamentally more restrictive than approaching x₀ on the real line, and what does this foreshadow about complex differentiability?"
  type: short-answer
  answer: "On the real line, x can approach x₀ from only two directions (left or right), so a limit exists if those two one-sided limits agree. In the complex plane, z can approach z₀ along infinitely many paths — every possible curve leading to z₀. The ε-δ condition |z - z₀| < δ controls all directions simultaneously, so the limit must be consistent across all approach paths. This is a much stricter condition. For differentiability, this strictness becomes even more powerful: a complex function that is differentiable at z₀ must have a single derivative value regardless of the direction of approach, forcing the Cauchy-Riemann equations and ultimately implying that complex-differentiable (holomorphic) functions are infinitely differentiable and equal their Taylor series."
  explanation: "The direction-independence requirement for complex limits is the seed of everything powerful in complex analysis. Real functions can be once-differentiable without being twice-differentiable; complex functions cannot. Real analytic functions are a very special subclass; all holomorphic functions are automatically analytic. This rigidity comes from the constraint that limits must agree along every path, which propagates through differentiation to give holomorphic functions extraordinary global properties like the maximum modulus principle and Liouville's theorem."
```

## Explainer

You already know how complex sequences converge: a sequence {zₙ} converges to L if |zₙ - L| → 0, meaning the distance in the complex plane shrinks to zero. You also know that a complex function f(z) maps points in the complex plane to other points in the complex plane, and you can write f(z) = u(x,y) + iv(x,y) where z = x + iy. Limits and continuity of complex functions combine both of these ideas using the same ε-δ framework from real analysis — but the geometry is fundamentally two-dimensional, which changes what "approaching z₀" means.

In real analysis, x can approach x₀ from only two directions: the left or the right. For a limit to exist, both one-sided limits must agree. In the complex plane, z can approach z₀ from **infinitely many directions** — along any ray, spiral, or curve leading to z₀. The definition |z - z₀| < δ means "within a disk of radius δ centered at z₀," so the limit condition must hold no matter which path z takes through that disk. This makes complex limits stricter than real limits: a function with different values along different approach paths has no limit at that point.

A powerful consequence is the **component criterion**: f(z) = u(x,y) + iv(x,y) has limit L = a + ib at z₀ = x₀ + iy₀ if and only if u(x,y) → a and v(x,y) → b as (x,y) → (x₀,y₀) in ℝ². This reduces a complex limit to two real multivariable limits. Similarly, f is continuous at z₀ if and only if u and v are both continuous as real functions at (x₀,y₀). Continuity of the component functions is both necessary and sufficient — there is no extra "complex" condition beyond this pair of real conditions.

The stricter path-independence requirement becomes essential in the next step of complex analysis: complex differentiability. A real function can have a derivative even if it approaches from only two directions; a complex function must behave consistently along every possible path to z₀ before it can be differentiated. This extra constraint turns out to force remarkably strong structure — functions that are differentiable in the complex sense (holomorphic functions) are infinitely differentiable and equal their Taylor series everywhere they are defined. The strictness you see here in limits and continuity is the first sign that complex analysis will be far more rigid and powerful than real analysis.
