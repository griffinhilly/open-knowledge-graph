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

## Questions

```yaml
- question: "You want to compute ∫_γ z dz from 0 to 1+i. You try two paths: a straight line, and an L-shaped path via the point 1. What result should you expect?"
  type: multiple-choice
  options:
    - "Different values, because the two paths trace different curves through the complex plane"
    - "The same value, because f(z) = z is holomorphic and the domain ℂ is simply connected"
    - "The same value only if both paths have the same arc length"
    - "Different values, depending on the winding number of each path around the origin"
  answer: 1
  explanation: "f(z) = z is holomorphic everywhere (it's entire), and ℂ is simply connected, so by path-independence for holomorphic functions, the integral depends only on the endpoints. Winding number and arc length are irrelevant for holomorphic integrands on simply connected domains — they matter only when there are singularities. The key distinction: path-independence is a consequence of holomorphicity, not of the path's geometry."

- question: "A student computes ∮ (1/z) dz along the unit circle (traversed once counterclockwise) and gets 2πi. Her classmate argues she must have made an error: 'The path is closed, so it returns to the starting point — the integral must be 0.' Who is correct?"
  type: multiple-choice
  options:
    - "The classmate — by Cauchy's theorem, any integral along a closed path is 0"
    - "The student — 1/z has a singularity at z = 0 inside the unit circle, so Cauchy's theorem does not apply, and the integral equals 2πi"
    - "Neither — the integral of 1/z around a closed path is always πi regardless of the contour"
    - "The classmate — the integral is 0 because 1/z is holomorphic on the punctured plane ℂ\\{0}"
  answer: 1
  explanation: "Cauchy's theorem requires the function to be holomorphic on a *simply connected* domain containing the path. The unit circle encloses z = 0, where 1/z has a singularity — the domain ℂ\\{0} is not simply connected (there's a hole at the origin). The integral ∮ (1/z) dz = 2πi is one of the foundational results of complex analysis; its value reflects the path winding once around the singularity. Option D confuses 'holomorphic on a punctured plane' with 'holomorphic on a simply connected domain.'"

- question: "Since a complex line integral along a closed path always returns to the starting point in the complex plane, it always evaluates to 0."
  type: true-false
  answer: false
  explanation: "Returning to the starting point does not make the integral zero — this confuses the path being closed geometrically with the integral being zero analytically. The integral is 0 for closed paths only when the integrand is holomorphic on a simply connected region containing the path. For f(z) = 1/z integrated around the origin, the path is closed but the integral is 2πi. The value depends on whether (and how) the path encircles singularities."

- question: "When integrating a holomorphic function f over a simply connected domain, the value of ∫_γ f(z) dz depends only on the endpoints of γ, not on the specific path taken between them."
  type: true-false
  answer: true
  explanation: "Path-independence is exactly what holomorphicity buys you on simply connected domains. This is the complex analogue of gradient vector fields in real calculus: just as integrating a conservative field depends only on endpoints, integrating a holomorphic function on a simply connected domain depends only on where you start and end. The simply connected condition is essential — if the domain has holes (like ℂ\\{0}), path-independence can fail because different paths may wind differently around the holes."

- question: "Why does ∫_γ (1/z) dz around a circle enclosing the origin equal 2πi rather than 0, and what concept connects the integral's value to the geometry of the path?"
  type: short-answer
  answer: "The function 1/z is not holomorphic at z = 0, and the circle encloses that singularity. The value 2πi comes from the winding number of the path around the singularity: a path that winds once counterclockwise around the origin gives 2πi · 1 = 2πi; a path winding twice would give 4πi; a path not enclosing the origin gives 0. The winding number connects the integral's value to the topological relationship between the path and the singularity — this is the first glimpse of why complex integration connects analysis to topology."
  explanation: "Computing the integral explicitly confirms this: parametrize γ(t) = e^{it} for 0 ≤ t ≤ 2π, so dz = ie^{it} dt and 1/z = e^{-it}. Then ∫ e^{-it} · ie^{it} dt = ∫ i dt = 2πi. The 'i times 1' factor comes directly from the winding — the path going all the way around."
```

## Explainer

From your work with scalar line integrals in real analysis, you know how to integrate a function along a curve in the plane by parametrizing the curve and reducing to a single-variable integral. The complex line integral does something analogous but richer: it integrates a complex-valued function f(z) along a directed path γ in the complex plane. The definition ∫_γ f(z) dz = ∫_a^b f(γ(t)) γ'(t) dt is the direct translation — parametrize the path, substitute, and integrate. The factor γ'(t) accounts for both the speed and direction of travel along the path, just as arc-length differentials do in real line integrals.

The key new ingredient is **holomorphicity**. For real line integrals, path-independence required the integrand to be a gradient (a conservative field). For complex line integrals, holomorphicity plays the analogous role — but it is a much stronger condition. A holomorphic function satisfies the Cauchy-Riemann equations, which impose tight coupling between its real and imaginary parts. Because of this coupling, holomorphic functions on simply connected domains are automatically path-independent: ∫_γ f(z) dz depends only on the endpoints of γ, not on the specific path taken.

Path-dependence arises precisely when holomorphicity fails. The canonical example is f(z) = 1/z, which has a singularity at z = 0. If you integrate 1/z along a small circle centered at the origin, you get 2πi regardless of the radius; if you integrate along a path that doesn't wind around the origin, you get 0. The **winding number** of the path around the singularity determines the answer. This is the first glimpse of why complex analysis connects integration to topology — the value of an integral can depend on how the path encircles singularities, not just where it starts and ends.

Computing a complex line integral in practice means choosing a parametrization γ(t) for a ≤ t ≤ b, then evaluating ∫_a^b f(γ(t)) γ'(t) dt as an ordinary real integral of a complex-valued function (integrate real and imaginary parts separately). For the upper half of the unit circle from 1 to −1, set γ(t) = e^(it) for 0 ≤ t ≤ π; then γ'(t) = ie^(it) dt, and you substitute f(γ(t)) accordingly. This parametrization technique is the computational foundation for everything in contour integration and Cauchy's theorem that follows.
