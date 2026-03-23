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
status: validated
---

# Iterated Integrals and Fubini's Theorem

## Core Idea
Fubini's theorem states that for continuous f on a rectangular region, ∬_R f(x, y) dA = ∫∫ f(x, y) dy dx (inner integral with respect to y, outer with respect to x). The two orders of integration give the same answer, providing flexibility in computation.

## Questions

```yaml
- question: "Consider ∫₀¹ ∫ₓ¹ e^(y²) dy dx. Why is switching the order of integration beneficial here?"
  type: multiple-choice
  options:
    - "The region is more naturally expressed in polar coordinates after switching"
    - "e^(y²) has no elementary antiderivative, so integrating y first is impossible; integrating x first gives a tractable inner integral"
    - "The outer integral must always correspond to the variable with the simpler bounds"
    - "Switching order changes the value of the integral, producing a simpler number"
  answer: 1
  explanation: "This is the canonical example of why switching order matters: ∫ₓ¹ e^(y²) dy has no closed form because e^(y²) has no elementary antiderivative. Reversing the order — for fixed y, x runs from 0 to y, then y from 0 to 1 — gives inner integral ∫₀^y e^(y²) dx = y·e^(y²), which is trivially evaluated, and the outer integral ∫₀¹ y·e^(y²) dy = (e−1)/2 by substitution. Fubini's theorem guarantees the value is unchanged; only the computability changes."

- question: "Fubini's theorem guarantees that the two orders of integration give the same value as the double integral. For which of the following is this guarantee strongest?"
  type: multiple-choice
  options:
    - "Any integrable function on any bounded region"
    - "Any continuous function on a closed bounded rectangular region"
    - "Any function where both iterated integrals exist and are finite"
    - "Any function where the outer integral converges absolutely"
  answer: 1
  explanation: "Fubini's theorem in its basic form applies to continuous functions on closed bounded rectangles — this gives the cleanest guarantee with no additional conditions. The theorem extends to larger classes (bounded measurable functions, absolutely integrable functions) under stronger hypotheses, but those require Lebesgue integration theory. The key failure mode: a bounded discontinuous function can have iterated integrals that both exist but give different values, which is why 'any bounded function' is too broad without further conditions."

- question: "When switching the order of integration in a double integral over a non-rectangular region, the limits of integration must be recomputed by re-describing the same geometric region with the variables in the reversed order."
  type: true-false
  answer: true
  explanation: "Switching order is not as simple as swapping limit symbols — you must re-read the region's boundary curves with the roles of x and y exchanged. For a triangular region described as 'x from 0 to 1, y from x to 1,' the reversed description is 'y from 0 to 1, x from 0 to y.' Failing to redraw and re-derive the limits is the most common error in switching integration order, and it produces incorrect integrals even when the theorem applies."

- question: "For any bounded function defined on a closed rectangular region, the two orders of integration always produce the same value."
  type: true-false
  answer: false
  explanation: "This is false. Fubini's theorem requires more than boundedness. A classic counterexample involves functions that are discontinuous in a way that affects the iterated integrals differently: ∫₀¹ (∫₀¹ f(x,y) dx) dy ≠ ∫₀¹ (∫₀¹ f(x,y) dy) dx for certain pathological bounded functions. Continuity (or absolute integrability in the Lebesgue sense) is the operative condition. Assuming the theorem applies without checking conditions is a common error in advanced applications."

- question: "Explain why switching the order of integration is a practically important skill, and give an example of when it converts an impossible computation into a tractable one."
  type: short-answer
  answer: "Switching order matters because one order may yield an inner integral with no closed-form antiderivative while the other is easily computable. Example: ∫₀¹ ∫ₓ¹ e^(y²) dy dx cannot be evaluated with y as the inner variable since e^(y²) has no elementary antiderivative. Rewriting the triangular region as 'x from 0 to y, y from 0 to 1' gives inner integral y·e^(y²), and the outer integral equals (e−1)/2 by substitution."
  explanation: "The geometric key is that both orders describe the same region — one with horizontal slices, one with vertical slices. The analytic key is that the integrand may factor or simplify in one orientation. Recognizing 'switch order' as a solution strategy comes from understanding that the order of integration is flexible (when Fubini applies), not fixed by convention."
```

## Explainer

From double integrals, you know that ∬_R f(x, y) dA represents a signed volume under the surface z = f(x, y) over a region R in the xy-plane. The abstract definition approximates this with Riemann sums over small rectangles, but actually computing that limit directly is unwieldy. **Iterated integrals** give you a concrete computational algorithm: integrate one variable at a time, treating the other as a constant during each step.

The intuition is a slicing argument. Fix a value x₀ and look at the "slice" of the region at that x-value: you get a one-dimensional cross-section, and ∫f(x₀, y) dy is the area under that slice (a signed area, counted by the function values). Now imagine sliding x₀ from left to right — you're sweeping out the entire region slice by slice. Integrating those slice areas ∫(∫f(x, y) dy) dx accumulates the total signed volume. **Fubini's theorem** makes this rigorous: for a continuous function on a rectangle [a, b] × [c, d], the double integral equals the iterated integral in either order:

∬_R f(x, y) dA = ∫_a^b (∫_c^d f(x, y) dy) dx = ∫_c^d (∫_a^b f(x, y) dx) dy.

The inner integral is evaluated first (treating the outer variable as a constant), then the result — a function of the remaining variable — is integrated by the outer integral.

The power of having two available orders becomes apparent when one order is computationally easier than the other. Consider integrating f(x, y) = e^(y²) over a triangular region where y ranges from x to 1 with x from 0 to 1. In the natural order (integrate y first), the inner integral is ∫_x^1 e^(y²) dy — a function with no closed form. Switching to integrate x first: for a fixed y, x runs from 0 to y, so the inner integral is ∫_0^y e^(y²) dx = y·e^(y²), which is easy. The outer integral ∫_0^1 y·e^(y²) dy evaluates to (e − 1)/2 by substitution. **Switching the order of integration** — by re-drawing the region and re-reading the bounds — is one of the most practically useful skills in multivariable calculus and appears constantly in probability, physics, and engineering applications.
