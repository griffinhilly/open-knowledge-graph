---
id: harmonic-conjugates
title: Harmonic Conjugates
domain: mathematics
course: complex-analysis
prerequisites:
- id: harmonic-functions-complex-analysis
  type: hard
tags:
- harmonic
- conjugate-pairs
- reconstruction
stage: advanced
status: validated
---

# Harmonic Conjugates

## Core Idea
If u is a harmonic function on a simply connected domain D, a harmonic conjugate v is a harmonic function such that f = u + iv is holomorphic on D. The Cauchy-Riemann equations tell us how to find v from u: v is obtained by integration using ∂v/∂x = -∂u/∂y and ∂v/∂y = ∂u/∂x. Every harmonic function has a unique harmonic conjugate up to an additive constant.

## Questions

```yaml
- question: "A student wants to find the harmonic conjugate of u = (1/2)ln(x² + y²) on the punctured plane ℝ² \\ {0}. They integrate the Cauchy-Riemann equations and obtain v = arctan(y/x), concluding this is the harmonic conjugate. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The Cauchy-Riemann equations only apply to analytic functions, not to arbitrary harmonic functions"
    - "The integration is incorrect — the harmonic conjugate of (1/2)ln(x² + y²) is |z|, not arctan(y/x)"
    - "The punctured plane is not simply connected, so the integral is path-dependent and arctan(y/x) is multivalued — its value changes by 2π when looping around the origin"
    - "The function u = (1/2)ln(x² + y²) is not harmonic on the punctured plane"
  answer: 2
  explanation: "The Cauchy-Riemann integration is formally correct — it yields arctan(y/x) as the 'natural' candidate. But the punctured plane ℝ² \\ {0} is not simply connected: it has a hole at the origin. When you traverse a closed loop around the origin, arctan(y/x) increases by 2π rather than returning to its starting value. This multivaluedness disqualifies arctan(y/x) as a harmonic conjugate, which must be a single-valued function. On a simply connected domain that excludes the origin (like the right half-plane), the conjugate does exist — but no simply connected domain can cover the full punctured plane."

- question: "To find the harmonic conjugate of u = x³ − 3xy², what is the correct procedure?"
  type: multiple-choice
  options:
    - "Set v = −(y³ − 3x²y) and verify the Cauchy-Riemann equations hold"
    - "Integrate ∂v/∂y = ∂u/∂x = 3x² − 3y² with respect to y, obtaining v = 3x²y − y³ + g(x), then use ∂v/∂x = −∂u/∂y to determine g(x)"
    - "Take the imaginary part of eᶻ where the real part equals u"
    - "Differentiate u twice and solve Laplace's equation directly for v"
  answer: 1
  explanation: "The standard construction: since ∂v/∂y = ∂u/∂x = 3x² − 3y², integrate with respect to y to get v = 3x²y − y³ + g(x), where g(x) is an unknown function of x alone. Then apply the second Cauchy-Riemann equation: ∂v/∂x = 6xy + g'(x) must equal −∂u/∂y = −(−6xy) = 6xy. So g'(x) = 0, meaning g is a constant. The harmonic conjugate is v = 3x²y − y³ + C, and the corresponding holomorphic function is f = (x³ − 3xy²) + i(3x²y − y³) = z³."

- question: "Nearly every harmonic function defined on any open connected domain in ℝ² has a harmonic conjugate."
  type: true-false
  answer: false
  explanation: "This is only true on simply connected domains — domains with no holes. On domains that are not simply connected (like the punctured plane, or an annulus), a harmonic function may not have a single-valued harmonic conjugate because the line integral used to construct it can be path-dependent. The canonical counterexample is u = (1/2)ln(x² + y²) on ℝ² \\ {0}: it is harmonic there, but its 'natural' conjugate arctan(y/x) is multivalued. On any simply connected domain, the Cauchy-Riemann equations can always be integrated to produce a single-valued harmonic conjugate."

- question: "If v is the harmonic conjugate of u on a simply connected domain, then u is also the harmonic conjugate of v, and both u and v individually satisfy Laplace's equation."
  type: true-false
  answer: true
  explanation: "Both claims follow from the structure of holomorphic functions. If f = u + iv is holomorphic, then if = −v + iu is also holomorphic (multiplication by i rotates the function). This shows that u is the real part of a holomorphic function whose imaginary part is −v, confirming the symmetric relationship: u and v are each other's harmonic conjugates (up to sign). Additionally, both u and v are the real and imaginary parts of a holomorphic function, and all such parts satisfy Laplace's equation — this is a direct consequence of the Cauchy-Riemann equations."

- question: "Why does the harmonic conjugate of u = (1/2)ln(x² + y²) fail to exist on the punctured plane ℝ² \\ {0}, even though u is harmonic there?"
  type: short-answer
  answer: "The punctured plane is not simply connected — it has a hole at the origin. The 'natural' conjugate arctan(y/x) is multivalued: traveling along a closed loop around the origin returns to the same point but shifts arctan's value by 2π. A harmonic conjugate must be single-valued, so no harmonic conjugate exists on the full punctured plane."
  explanation: "On a simply connected domain, any closed path can be continuously contracted to a point without crossing the boundary, which guarantees that line integrals are path-independent and the Cauchy-Riemann construction produces a single-valued function. On the punctured plane, paths that wind around the origin cannot be contracted — they are topologically distinct, and the integral accumulates an extra 2π per winding. This is not a failure of the Cauchy-Riemann equations but a topological obstruction. The remedy is to restrict to a simply connected subset: on the right half-plane (x > 0), for example, the branch of arctan that maps into (−π/2, π/2) is a valid single-valued harmonic conjugate."
```

## Explainer

From your study of harmonic functions, you know that u(x, y) is harmonic if it satisfies Laplace's equation ∂²u/∂x² + ∂²u/∂y² = 0. You also know the Cauchy-Riemann equations: if f = u + iv is holomorphic, then ∂u/∂x = ∂v/∂y and ∂u/∂y = −∂v/∂x. A **harmonic conjugate** of u is a function v satisfying exactly these two equations — it is the imaginary part of a holomorphic function whose real part is u. The relationship is symmetric: u and v are each other's harmonic conjugates, and both are individually harmonic.

The construction of v from u is concrete and computational. Since ∂v/∂y = ∂u/∂x, integrate with respect to y to obtain v up to an unknown function of x alone. Then use the second Cauchy-Riemann equation ∂v/∂x = −∂u/∂y to determine that function. For example, if u = x² − y², then ∂u/∂x = 2x and ∂u/∂y = −2y. Integrating ∂v/∂y = 2x with respect to y gives v = 2xy + g(x). Then ∂v/∂x = 2y + g'(x) must equal −∂u/∂y = 2y, so g'(x) = 0 and g is a constant. The harmonic conjugate is v = 2xy + C, and the corresponding holomorphic function is f = (x² − y²) + i(2xy) = (x + iy)² = z².

The requirement that the domain be **simply connected** is essential. On a domain with holes, a line integral used to construct v may give different values along paths that wind around the hole — the function would be multivalued. The canonical example is u = (1/2) ln(x² + y²) on ℝ² \ {0}, which is harmonic on the punctured plane but has no harmonic conjugate there. The "natural" conjugate would be arctan(y/x), which is multivalued — its value changes by 2π when you loop around the origin. On a simply connected domain, every harmonic function has a harmonic conjugate, unique up to an additive constant.

Harmonic conjugates connect the real and complex worlds cleanly: every harmonic function on a simply connected domain is the real part of some holomorphic function, and finding the conjugate reconstructs that holomorphic function. This is why harmonic functions in complex analysis are far more constrained than harmonic functions in purely real analysis — they come in conjugate pairs, bound together by the Cauchy-Riemann equations and the rigid structure of holomorphic functions.
