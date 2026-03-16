---
id: iterated-integrals
title: Iterated Integrals and Fubini's Theorem
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: antiderivatives
  type: hard
builds-toward:
- double-integrals-cartesian
- triple-integrals
tags:
- integrals
- fubini
stage: formal-systems
status: draft
---

# Iterated Integrals and Fubini's Theorem

## Core Idea
A double integral ∬ f(x,y) dA can be computed as an iterated integral ∫∫ f(x,y) dy dx. By Fubini's theorem, the order can be swapped if f is continuous; rewriting bounds requires understanding the region carefully.

## Explainer

You know from antiderivatives that a single integral ∫ₐᵇ f(x) dx computes the signed area under a curve on an interval. Now extend the question: what is the signed volume under a surface z = f(x, y) over a 2D region R in the xy-plane? The double integral ∬_R f(x, y) dA answers this, but computing it directly requires a strategy. The **iterated integral** reduces the 2D problem to two sequential 1D integrations, each of which you already know how to perform.

The idea is to slice the volume into thin cross-sections. Fix a value of x and integrate f(x, y) over y — this gives A(x), the area of the cross-sectional slice at that x. Then integrate A(x) over x to accumulate all slices into a total volume. Written explicitly: ∫ₐᵇ ( ∫_c^d f(x,y) dy ) dx. The inner integral treats x as a constant and integrates in y; the outer integral then integrates the result in x. The parentheses are usually omitted, and you simply evaluate the innermost integral first, working outward.

**Fubini's theorem** guarantees that when f is continuous on a rectangle [a,b] × [c,d], the order of integration can be reversed without changing the answer:

  ∫ₐᵇ ∫_c^d f(x,y) dy dx  =  ∫_c^d ∫ₐᵇ f(x,y) dx dy

This is powerful because one order may be algebraically much simpler than the other. If ∫ f(x,y) dy is hard to compute, try reversing the order and integrating in x first. The theorem guarantees you get the same answer, so algebraic convenience guides the choice.

For **non-rectangular regions**, the bounds of the inner integral become functions of the outer variable. Integrating over the triangular region where 0 ≤ x ≤ 1 and 0 ≤ y ≤ x gives ∫₀¹ ∫₀ˣ f(x,y) dy dx — y runs from 0 to x, a bound that depends on the current value of x. To reverse the order, you must re-describe the same region from y's perspective: y ranges from 0 to 1, and for each y, x ranges from y to 1. The reversed integral is ∫₀¹ ∫_y^1 f(x,y) dx dy. Always sketch the region first, label the corners and curves, and read the bounds directly from the sketch — this is the single most reliable technique for setting up iterated integrals correctly.
