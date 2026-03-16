---
id: properties-riemann-integral
title: Properties of the Riemann Integral
domain: mathematics
course: real-analysis
prerequisites:
- id: riemann-integrability-criteria
  type: hard
builds-toward:
- fundamental-theorem-calculus-rigorous
- improper-integrals-rigorous
tags:
- riemann-integral
- properties
- linearity
stage: advanced
status: draft
---

# Properties of the Riemann Integral

## Core Idea
The Riemann integral satisfies linearity (∫(af+bg) = a∫f + b∫g), order properties (if f ≤ g then ∫f ≤ ∫g), additivity over intervals (∫[a,c] = ∫[a,b] + ∫[b,c]), and bounds (|∫f| ≤ ∫|f|). These properties make the integral a powerful tool for analysis and follow naturally from the definition via Darboux sums.

## Explainer

From your study of Riemann integrability criteria, you know that a bounded function f on [a, b] is Riemann integrable when the gap between its upper and lower Darboux sums can be made arbitrarily small. That definition gives you the integral's existence conditions. What you build on top of it are the **properties** — algebraic and order-theoretic rules that let you compute and bound integrals without returning to the Darboux sum definition every time.

**Linearity** is the most frequently used property: ∫(af + bg) = a∫f + b∫g for real constants a, b and integrable functions f, g. This mirrors the linearity of summation — the integral is essentially a limit of sums, so it inherits sum's additive and scalar behavior. The proof follows by controlling the Darboux sums for af + bg in terms of those for f and g separately. Linearity is what allows you to integrate polynomial terms one at a time, or to split an integral of a sum into a sum of integrals.

**Monotonicity** says: if f(x) ≤ g(x) for all x in [a, b], then ∫f ≤ ∫g. Geometrically, if one function lies below another, its area is smaller. The proof is immediate: the lower Darboux sums for f are bounded above by those for g on any partition. A closely related result is the **triangle inequality for integrals**: |∫f| ≤ ∫|f|. This is the continuous analogue of |Σaᵢ| ≤ Σ|aᵢ|. It is used throughout analysis to bound error terms — you replace an absolute value of an integral with an integral of an absolute value, which is easier to estimate.

**Additivity over subintervals** states that if c ∈ [a, b], then ∫[a,b] f = ∫[a,c] f + ∫[b,c] f. This lets you split a complicated domain into manageable pieces, handle discontinuities by isolating them in a small sub-interval, and build up results about improper integrals by passing to limits. Combined with linearity, these properties form the algebraic backbone that makes the Fundamental Theorem of Calculus both meaningful and provable: when you differentiate ∫[a,x] f(t) dt with respect to x, it is the additivity property that allows you to isolate the increment [x, x+h] and let h → 0.
