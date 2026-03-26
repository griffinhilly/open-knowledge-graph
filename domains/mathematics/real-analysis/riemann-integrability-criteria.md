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
status: validated
---

# Criteria for Riemann Integrability

## Core Idea
A function f on [a,b] is Riemann integrable if and only if its set of discontinuities has measure zero. This criterion clarifies which functions are integrable: all continuous functions, all monotone functions, and many others. Functions discontinuous on a dense set (like Dirichlet's function) are not Riemann integrable, motivating the Lebesgue integral.

## Questions

```yaml
- question: "A function f on [0,1] is discontinuous at every rational number (a dense set), but continuous at every irrational number. Is f Riemann integrable on [0,1]?"
  type: multiple-choice
  options:
    - "No — a dense set of discontinuities guarantees the upper and lower Darboux sums can never agree"
    - "Yes — the rationals in [0,1] form a countable set, which has measure zero, so f satisfies Lebesgue's criterion"
    - "Only if f is also bounded, in which case the dense discontinuities do not matter at all"
    - "It depends on whether f is monotone; monotonicity is the deciding factor, not the discontinuity set"
  answer: 1
  explanation: "Lebesgue's criterion states that f is Riemann integrable if and only if its discontinuity set has measure zero. The rationals in [0,1] are countable, and every countable set has measure zero (they can be covered by intervals of arbitrarily small total length). So a dense discontinuity set is not automatically fatal — what matters is the measure of that set, not its density or cardinality. Option A reflects the common confusion between 'dense' and 'large in the sense of measure.'"

- question: "Why is the Dirichlet function (f = 1 on rationals, f = 0 on irrationals) not Riemann integrable on [0,1]?"
  type: multiple-choice
  options:
    - "Because it is not monotone on [0,1]"
    - "Because it has infinitely many discontinuities, and Riemann integrability requires only finitely many"
    - "Because its discontinuity set is all of [0,1], which has positive measure, so the upper and lower Darboux sums cannot be made to agree"
    - "Because it is not bounded — it oscillates between 0 and 1 without settling"
  answer: 2
  explanation: "The Dirichlet function is discontinuous at every point of [0,1]: its discontinuity set has measure 1 (positive), so Lebesgue's criterion fails. On any subinterval of [0,1], the supremum of f is 1 (a rational is always nearby) and the infimum is 0 (an irrational is always nearby). So the upper sum is always 1 and the lower sum is always 0, regardless of how fine the partition is. Option B is the common but wrong answer — infinitely many discontinuities are not inherently fatal; only a positive-measure set of them is."

- question: "A function with a countably infinite set of discontinuities on [a,b] can rarely be Riemann integrable."
  type: true-false
  answer: false
  explanation: "Countably infinite sets have measure zero — they can be covered by open intervals with total length less than any ε > 0. Therefore a function with only countably many discontinuities satisfies Lebesgue's criterion and is Riemann integrable (provided it is bounded). Monotone functions, for instance, can have countably many jump discontinuities and are always Riemann integrable. The criterion is measure zero, not finiteness."

- question: "Every monotone bounded function on [a,b] is Riemann integrable."
  type: true-false
  answer: true
  explanation: "A monotone function on a bounded interval can have at most countably many discontinuities (each discontinuity corresponds to a jump, and the jumps must sum to a finite total variation, so there can only be countably many). A countable set has measure zero, so Lebesgue's criterion is satisfied. This is one of the important corollaries of the measure-zero condition: monotone functions — even highly irregular step-like ones — are always integrable."

- question: "Why is 'the discontinuity set has measure zero' the right criterion for Riemann integrability, rather than 'the function has only finitely many discontinuities'?"
  type: short-answer
  answer: "Measure zero is the precise condition under which discontinuities can be 'hidden' by partitions — their total contribution to the gap between upper and lower Darboux sums can be made arbitrarily small. Finite is sufficient but not necessary: a function with countably or even uncountably many discontinuities (as long as they form a measure-zero set) is still integrable, because those discontinuities occupy negligible total length and don't prevent the upper and lower sums from converging. 'Finitely many' is too restrictive a sufficient condition, and it misses the deeper reason why integrability works."
  explanation: "The Darboux sum gap over a subinterval is bounded by the oscillation of f times the subinterval's length. If the discontinuities are confined to a measure-zero set, we can cover them with intervals of total tiny length. On those tiny intervals, the gap can be large, but the total contribution (oscillation × tiny length) is negligible. On the remaining intervals, f is continuous and we can make the oscillation small. The measure-zero condition is exactly the one that makes this argument go through — and it's why Lebesgue's criterion is the right statement, not the ad hoc 'finitely many' version."
```

## Explainer

Recall how the Riemann integral is built via Darboux sums. You partition [a, b] into subintervals and record the supremum (upper sum) and infimum (lower sum) of f on each. The function is integrable when you can make these upper and lower sums agree to any desired precision by refining the partition. What ruins this convergence? Discontinuities — specifically, jumps in the function's value. Where f jumps, the upper and lower sums over that subinterval differ by approximately the size of the jump times the width of the interval. If the jumps cluster badly enough, no refinement eliminates the gap.

**Lebesgue's criterion** pins this down precisely. A set has **measure zero** if it can be covered by a collection of intervals whose total length is less than any ε > 0 — intuitively, it is a "negligibly thin" set. Individual points and finite sets are measure zero. Even countably infinite sets (like the rationals in [0,1]) are measure zero. The criterion says: f is Riemann integrable on [a, b] if and only if its discontinuity set has measure zero. All continuous functions pass trivially (empty discontinuity set). Monotone functions pass because they can only have countably many jumps (a countable set has measure zero). The **Dirichlet function** — defined as 1 on rationals, 0 on irrationals — is discontinuous everywhere, so its discontinuity set is all of [a, b], which has positive measure, and it fails.

The measure-zero condition captures why "most" discontinuities are harmless. A function can have infinitely many discontinuities and still be Riemann integrable, as long as those discontinuities don't fill up any positive-length portion of the domain. Imagine painting only the rationals red on [0, 1]. They form a dense set — every interval contains infinitely many — yet they are still negligibly thin in total. A function that only misbehaves on such a set can still be integrated: the good behavior on the irrationals overwhelms the bad.

This criterion makes the Lebesgue integral's appeal concrete. The Lebesgue integral extends to functions that are "almost everywhere" well-behaved in a much richer sense. It can integrate the Dirichlet function (the answer is zero, since the rationals where f = 1 are negligible). More importantly, Lebesgue's framework handles limiting operations — the integral of a pointwise limit of integrable functions — in ways the Riemann integral cannot. Understanding Lebesgue's criterion on Riemann integrability is the moment you see precisely where the Riemann integral runs out of steam and why a more powerful theory is needed.
