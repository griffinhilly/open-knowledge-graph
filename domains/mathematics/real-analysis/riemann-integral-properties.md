---
id: riemann-integral-properties
title: Properties of the Riemann Integral
domain: mathematics
course: real-analysis
prerequisites:
- id: riemann-integral-darboux-sums
  type: hard
- id: riemann-integrability-criteria
  type: hard
builds-toward:
- fundamental-theorem-calculus-rigorous
- improper-integrals-rigorous
tags:
- integral-properties
- linearity
- monotonicity
stage: advanced
status: draft
---

# Properties of the Riemann Integral

## Core Idea
The Riemann integral satisfies linearity (∫(af + bg) = a∫f + b∫g), monotonicity (f ≤ g ⟹ ∫f ≤ ∫g), and additivity over intervals. These properties follow from the definition and form the computational toolkit of integration. They extend to the Lebesgue integral.

## Explainer

You built the Riemann integral from Darboux sums: the lower sum L(f, P) and upper sum U(f, P) sandwich the integral from below and above, and f is integrable when the infimum of upper sums equals the supremum of lower sums. That construction answers "does the integral exist?" — but it is not something you want to use directly for every computation. The properties of the Riemann integral are the tools that let you work efficiently without returning to Darboux sums from scratch each time.

**Linearity** is the most-used property: ∫ₐᵇ (αf + βg) = α ∫ₐᵇ f + β ∫ₐᵇ g. This holds whenever f and g are both integrable on [a, b]. The proof is not deep — Darboux sums are already linear in the function, so the inequality squeezeback argument transfers directly — but the payoff is enormous. It means integration distributes over sums and scales with constants, which underlies every technique for computing integrals of complicated expressions by breaking them into simpler parts. Without linearity, you could not use substitution and partial fractions to split a rational function and integrate each piece.

**Monotonicity** says that if f(x) ≤ g(x) for all x in [a, b], then ∫ₐᵇ f ≤ ∫ₐᵇ g. Geometrically this is obvious: if one function lies below another everywhere, it sweeps out less area. The proof uses the fact that lower and upper Darboux sums respect pointwise inequality of functions. Monotonicity is the gateway to estimation: if you can bound a complicated integrand between two simpler ones, you immediately bound the integral. A direct consequence is the **integral mean value inequality**: if m ≤ f(x) ≤ M on [a, b], then m(b − a) ≤ ∫ₐᵇ f ≤ M(b − a). This is the weakest possible estimate (using only global bounds), but it suffices for convergence proofs and error estimates.

**Additivity over intervals** states that ∫ₐᶜ f = ∫ₐᵇ f + ∫ᵦᶜ f for any b between a and c (and by convention, extending to any b when ∫ₐᵇ f is defined with reversed orientation as −∫ᵦᵃ f). This allows you to handle functions defined piecewise, to break integrals at discontinuities or change-of-formula points, and to integrate over unions of intervals. Together, linearity, monotonicity, and additivity form a package that extends cleanly to the Lebesgue integral — and the fact that these properties are shared explains why many analytic arguments work identically in both theories, with the Lebesgue theory adding the power to handle larger classes of functions.
