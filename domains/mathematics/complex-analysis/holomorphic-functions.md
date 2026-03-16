---
id: holomorphic-functions
title: Holomorphic Functions
domain: mathematics
course: complex-analysis
prerequisites:
- id: complex-differentiability
  type: hard
builds-toward:
- cauchy-riemann-equations
- complex-line-integrals
- taylor-series-complex
tags:
- holomorphic
- analytic
- differentiable
stage: advanced
status: draft
---

# Holomorphic Functions

## Core Idea
A function f is holomorphic (analytic) on a domain D if it is differentiable at every point in D. Holomorphic functions are infinitely differentiable and equal their Taylor series. They are the central objects of complex analysis because they satisfy rigid properties: their real and imaginary parts satisfy the Cauchy-Riemann equations, they satisfy integral theorems, and isolated zeros force local injectivity.

## How It's Best Learned
Study the function f(z) = e^z and verify it is holomorphic everywhere; compute its derivatives and Taylor series. Compare to a merely continuous function like f(z) = |z| to see the difference in rigidity.

## Common Misconceptions
Thinking holomorphic functions form a large class; they are extremely special and rigid. Assuming holomorphic functions are only polynomials and exponentials; there are many more (trig, logarithm, etc.).

## Explainer

You already know **complex differentiability**: f is differentiable at a point z₀ if the limit (f(z₀+h) − f(z₀))/h exists as h → 0 through all paths in the complex plane. This is a much stronger demand than real differentiability, because h can approach zero from infinitely many directions, not just left and right. A function is **holomorphic** on a domain D if it is complex-differentiable at every point of D — not just at isolated points, but everywhere throughout an open set. This global condition unleashes a cascade of rigidity that has no parallel in real analysis.

The key theorem to internalize is that holomorphic implies infinitely differentiable. In real calculus, a function can be differentiable once but not twice — there is no such restriction. In complex analysis, once f is holomorphic, f', f'', f''', and all higher derivatives automatically exist and are themselves holomorphic. Furthermore, f equals its own **Taylor series** on any disk inside D: it is not merely approximated by a Taylor series, it is exactly represented by one. This is why "holomorphic" and "complex analytic" are synonyms — both names capture the same property arrived at from different directions.

The Cauchy-Riemann equations give you a practical test. If f(z) = f(x + iy) = u(x,y) + iv(x,y) where u and v are real-valued, then f is holomorphic if and only if ∂u/∂x = ∂v/∂y and ∂u/∂y = −∂v/∂x (plus appropriate continuity conditions on the partials). These two equations encode the requirement that the limit of (f(z₀+h)−f(z₀))/h is the same in every direction. Checking them is computationally efficient: rather than checking all possible limit directions, you only need two equations between partial derivatives.

The rigidity of holomorphic functions has surprising global consequences. A holomorphic function is completely determined on an entire connected domain by its values on any tiny disk — or even by its values on a sequence of points converging to a point. If two holomorphic functions agree on even a small neighborhood, they agree everywhere they can both be defined. This is the **identity theorem**, and it has no analogue for real smooth functions. Concretely: there is essentially one way to extend sin(x) from the real line to a holomorphic function on the complex plane, and it is the function sin(z) = (eⁱᶻ − e⁻ⁱᶻ)/(2i). The "smallness" of the holomorphic class is its greatest strength: it means these functions are predictable, classifiable, and tractable in ways that arbitrary smooth functions are not.
