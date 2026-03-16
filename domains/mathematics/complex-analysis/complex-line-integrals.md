---
id: complex-line-integrals
title: Complex Line Integrals
domain: mathematics
course: complex-analysis
prerequisites:
- id: holomorphic-functions
  type: hard
- id: line-integrals-scalar
  type: hard
builds-toward:
- contour-integration
- cauchys-theorem
tags:
- line-integrals
- contour-integrals
- path-dependence
stage: advanced
status: draft
---

# Complex Line Integrals

## Core Idea
The integral of f(z) along a path γ from a to b is ∫_γ f(z) dz = ∫_a^b f(γ(t)) γ'(t) dt. For a general continuous f, this integral depends on the path. But for holomorphic f on simply connected domains, the integral is path-independent and depends only on the endpoints, a fact made rigorous by Cauchy's theorem.

## How It's Best Learned
Compute ∫_γ z dz along two different paths from 0 to 1+i; verify that they give the same result. Then try f(z) = 1/z along paths that wind around the origin; observe the path-dependence.

## Common Misconceptions
Assuming all line integrals are path-independent; this is true only for holomorphic functions on simply connected domains. Forgetting to parametrize the contour when computing the integral.

## Explainer

From your work with scalar line integrals in real analysis, you know how to integrate a function along a curve in the plane by parametrizing the curve and reducing to a single-variable integral. The complex line integral does something analogous but richer: it integrates a complex-valued function f(z) along a directed path γ in the complex plane. The definition ∫_γ f(z) dz = ∫_a^b f(γ(t)) γ'(t) dt is the direct translation — parametrize the path, substitute, and integrate. The factor γ'(t) accounts for both the speed and direction of travel along the path, just as arc-length differentials do in real line integrals.

The key new ingredient is **holomorphicity**. For real line integrals, path-independence required the integrand to be a gradient (a conservative field). For complex line integrals, holomorphicity plays the analogous role — but it is a much stronger condition. A holomorphic function satisfies the Cauchy-Riemann equations, which impose tight coupling between its real and imaginary parts. Because of this coupling, holomorphic functions on simply connected domains are automatically path-independent: ∫_γ f(z) dz depends only on the endpoints of γ, not on the specific path taken.

Path-dependence arises precisely when holomorphicity fails. The canonical example is f(z) = 1/z, which has a singularity at z = 0. If you integrate 1/z along a small circle centered at the origin, you get 2πi regardless of the radius; if you integrate along a path that doesn't wind around the origin, you get 0. The **winding number** of the path around the singularity determines the answer. This is the first glimpse of why complex analysis connects integration to topology — the value of an integral can depend on how the path encircles singularities, not just where it starts and ends.

Computing a complex line integral in practice means choosing a parametrization γ(t) for a ≤ t ≤ b, then evaluating ∫_a^b f(γ(t)) γ'(t) dt as an ordinary real integral of a complex-valued function (integrate real and imaginary parts separately). For the upper half of the unit circle from 1 to −1, set γ(t) = e^(it) for 0 ≤ t ≤ π; then γ'(t) = ie^(it) dt, and you substitute f(γ(t)) accordingly. This parametrization technique is the computational foundation for everything in contour integration and Cauchy's theorem that follows.
