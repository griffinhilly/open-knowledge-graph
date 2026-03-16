---
id: iterated-integrals-fubini
title: Iterated Integrals and Fubini's Theorem
domain: mathematics
course: multivariable-calculus
prerequisites:
- id: double-integrals
  type: hard
builds-toward:
- double-integrals-rectangular-regions
- double-integrals-general-regions
tags:
- iterated-integrals
- fubini-theorem
- order-of-integration
stage: formal-systems
status: draft
---

# Iterated Integrals and Fubini's Theorem

## Core Idea
Fubini's theorem states that for continuous f on a rectangular region, ∬_R f(x, y) dA = ∫∫ f(x, y) dy dx (inner integral with respect to y, outer with respect to x). The two orders of integration give the same answer, providing flexibility in computation.

## Explainer

From double integrals, you know that ∬_R f(x, y) dA represents a signed volume under the surface z = f(x, y) over a region R in the xy-plane. The abstract definition approximates this with Riemann sums over small rectangles, but actually computing that limit directly is unwieldy. **Iterated integrals** give you a concrete computational algorithm: integrate one variable at a time, treating the other as a constant during each step.

The intuition is a slicing argument. Fix a value x₀ and look at the "slice" of the region at that x-value: you get a one-dimensional cross-section, and ∫f(x₀, y) dy is the area under that slice (a signed area, counted by the function values). Now imagine sliding x₀ from left to right — you're sweeping out the entire region slice by slice. Integrating those slice areas ∫(∫f(x, y) dy) dx accumulates the total signed volume. **Fubini's theorem** makes this rigorous: for a continuous function on a rectangle [a, b] × [c, d], the double integral equals the iterated integral in either order:

∬_R f(x, y) dA = ∫_a^b (∫_c^d f(x, y) dy) dx = ∫_c^d (∫_a^b f(x, y) dx) dy.

The inner integral is evaluated first (treating the outer variable as a constant), then the result — a function of the remaining variable — is integrated by the outer integral.

The power of having two available orders becomes apparent when one order is computationally easier than the other. Consider integrating f(x, y) = e^(y²) over a triangular region where y ranges from x to 1 with x from 0 to 1. In the natural order (integrate y first), the inner integral is ∫_x^1 e^(y²) dy — a function with no closed form. Switching to integrate x first: for a fixed y, x runs from 0 to y, so the inner integral is ∫_0^y e^(y²) dx = y·e^(y²), which is easy. The outer integral ∫_0^1 y·e^(y²) dy evaluates to (e − 1)/2 by substitution. **Switching the order of integration** — by re-drawing the region and re-reading the bounds — is one of the most practically useful skills in multivariable calculus and appears constantly in probability, physics, and engineering applications.
