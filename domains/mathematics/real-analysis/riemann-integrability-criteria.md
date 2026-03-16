---
id: riemann-integrability-criteria
title: Criteria for Riemann Integrability
domain: mathematics
course: real-analysis
prerequisites:
- id: riemann-integral-darboux-sums
  type: hard
- id: connected-sets
  type: soft
builds-toward:
- riemann-integral-properties
- fundamental-theorem-calculus-rigorous
tags:
- integrability
- criteria
- discontinuities
stage: advanced
status: draft
---

# Criteria for Riemann Integrability

## Core Idea
A function f on [a,b] is Riemann integrable if and only if its set of discontinuities has measure zero. This criterion clarifies which functions are integrable: all continuous functions, all monotone functions, and many others. Functions discontinuous on a dense set (like Dirichlet's function) are not Riemann integrable, motivating the Lebesgue integral.

## Explainer

Recall how the Riemann integral is built via Darboux sums. You partition [a, b] into subintervals and record the supremum (upper sum) and infimum (lower sum) of f on each. The function is integrable when you can make these upper and lower sums agree to any desired precision by refining the partition. What ruins this convergence? Discontinuities — specifically, jumps in the function's value. Where f jumps, the upper and lower sums over that subinterval differ by approximately the size of the jump times the width of the interval. If the jumps cluster badly enough, no refinement eliminates the gap.

**Lebesgue's criterion** pins this down precisely. A set has **measure zero** if it can be covered by a collection of intervals whose total length is less than any ε > 0 — intuitively, it is a "negligibly thin" set. Individual points and finite sets are measure zero. Even countably infinite sets (like the rationals in [0,1]) are measure zero. The criterion says: f is Riemann integrable on [a, b] if and only if its discontinuity set has measure zero. All continuous functions pass trivially (empty discontinuity set). Monotone functions pass because they can only have countably many jumps (a countable set has measure zero). The **Dirichlet function** — defined as 1 on rationals, 0 on irrationals — is discontinuous everywhere, so its discontinuity set is all of [a, b], which has positive measure, and it fails.

The measure-zero condition captures why "most" discontinuities are harmless. A function can have infinitely many discontinuities and still be Riemann integrable, as long as those discontinuities don't fill up any positive-length portion of the domain. Imagine painting only the rationals red on [0, 1]. They form a dense set — every interval contains infinitely many — yet they are still negligibly thin in total. A function that only misbehaves on such a set can still be integrated: the good behavior on the irrationals overwhelms the bad.

This criterion makes the Lebesgue integral's appeal concrete. The Lebesgue integral extends to functions that are "almost everywhere" well-behaved in a much richer sense. It can integrate the Dirichlet function (the answer is zero, since the rationals where f = 1 are negligible). More importantly, Lebesgue's framework handles limiting operations — the integral of a pointwise limit of integrable functions — in ways the Riemann integral cannot. Understanding Lebesgue's criterion on Riemann integrability is the moment you see precisely where the Riemann integral runs out of steam and why a more powerful theory is needed.
