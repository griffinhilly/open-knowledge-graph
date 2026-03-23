---
id: riemann-integral-darboux-sums
title: Riemann Integral via Darboux Sums
domain: mathematics
course: real-analysis
prerequisites:
- id: rigorous-derivative-definition
  type: hard
- id: supremum-and-infimum
  type: hard
builds-toward:
- riemann-integrability-criteria
- riemann-integral-properties
tags:
- riemann-integral
- darboux-sums
- integrability
stage: advanced
status: validated
---

# Riemann Integral via Darboux Sums

## Core Idea
The Riemann integral is defined via Darboux sums: partition [a,b] into subintervals, compute upper (U) and lower (L) sums using suprema and infima of f on each subinterval. The integral exists if inf U = sup L. This definition is equivalent to Riemann sums and clarifies when functions are integrable: discontinuities on a set of measure zero are allowed.

## Questions

```yaml
- question: "According to the Darboux definition, a bounded function f is Riemann integrable on [a,b] when..."
  type: multiple-choice
  options:
    - "f is continuous at every point of [a,b]"
    - "There exists some partition for which the upper Darboux sum equals the lower Darboux sum"
    - "The infimum of all upper Darboux sums equals the supremum of all lower Darboux sums"
    - "The upper Darboux sum decreases to zero as the partition is refined"
  answer: 2
  explanation: "Integrability requires inf U* = sup L* — the infimum over all partitions of all upper sums equals the supremum over all partitions of all lower sums. This common value is the integral. Option B is wrong because for most integrable functions, no single partition makes U = L exactly; it is the limiting behavior over all partitions that matters. Option A is sufficient but not necessary: functions with finitely many (or even countably many) discontinuities can still be integrable."

- question: "Consider the Dirichlet function on [0,1]: f(x) = 1 if x is rational, f(x) = 0 if x is irrational. Which statement correctly applies the Darboux criterion?"
  type: multiple-choice
  options:
    - "f is integrable because it is bounded between 0 and 1"
    - "f is integrable because its integral should equal 0, since rationals form a 'small' set"
    - "f is not integrable: on every subinterval, sup f = 1 and inf f = 0, so U = 1 and L = 0 for every partition"
    - "f is integrable for sufficiently fine partitions that separate rationals from irrationals"
  answer: 2
  explanation: "Every subinterval of [0,1], no matter how small, contains both rationals and irrationals. So on every subinterval, the supremum of f is 1 and the infimum is 0. This means every upper sum U(f,P) = 1 and every lower sum L(f,P) = 0, regardless of how fine the partition is. Therefore inf U* = 1 and sup L* = 0, which are not equal — f is not Riemann integrable. This is why the Darboux criterion is powerful: it immediately identifies non-integrable functions via the gap between upper and lower sums."

- question: "Adding more points to a partition (refining it) can cause the upper Darboux sum to increase."
  type: true-false
  answer: false
  explanation: "Refinement can only decrease (or leave unchanged) the upper Darboux sum, and can only increase (or leave unchanged) the lower Darboux sum. When you add a point to a partition, each original subinterval either stays the same or splits into two. Splitting replaces the supremum over a larger interval with suprema over two smaller ones — which can only be ≤ the original. This monotone behavior is what guarantees that inf U* and sup L* are well-defined, and that the upper and lower Darboux sums squeeze toward each other as partitions are refined."

- question: "A function with exactly 5 jump discontinuities on [a,b] is Riemann integrable on [a,b]."
  type: true-false
  answer: true
  explanation: "The Riemann-Lebesgue criterion states that a bounded function is Riemann integrable if and only if its set of discontinuities has Lebesgue measure zero. A finite set of points (including 5 jump discontinuities) has measure zero. To see this directly from Darboux sums: on a subinterval containing one discontinuity, the gap Mᵢ − mᵢ may be large, but the width Δxᵢ of that subinterval can be made arbitrarily small. With careful partition refinement, the contribution of these finitely many 'bad' subintervals to U − L can be made as small as desired."

- question: "Why does the Darboux definition use suprema and infima on each subinterval, rather than arbitrary sample points as in the standard Riemann sum?"
  type: short-answer
  answer: "Using sup and inf gives the tightest possible overestimate (upper sum) and underestimate (lower sum) for each subinterval — extremes that depend only on the partition, not on how we sample. This makes integrability a property of the function and partition alone, without the arbitrary choice of sample points. If even these worst-case upper and lower sums converge to the same value, then any Riemann sum (which lies between them) must also converge to that value. Darboux sums thus provide a clean, sample-point-free criterion for integrability."
  explanation: "Arbitrary sample points can make a function look integrable or not depending on where you pick them — for example, always picking rationals in the Dirichlet function gives sum 1, always picking irrationals gives sum 0. Darboux sums avoid this arbitrariness by using the extreme values. This is why the Darboux approach is the cleanest foundation for the Riemann integral and connects most naturally to the Lebesgue theory."
```

## Explainer

You already have two powerful tools: the rigorous derivative (which taught you that calculus concepts require careful ε-δ formulation) and suprema and infima (which give you a precise way to talk about the least upper bound and greatest lower bound of a set of values). The **Riemann integral** via Darboux sums puts these tools together to define what "area under a curve" actually means — rigorously, without hand-waving.

The construction begins with a **partition** P = {a = x₀ < x₁ < … < xₙ = b} of the interval [a,b] into n subintervals. On each subinterval [xᵢ₋₁, xᵢ], the function f takes some set of values. Using the supremum, you can define Mᵢ = sup{f(x) : x ∈ [xᵢ₋₁, xᵢ]}, and using the infimum, mᵢ = inf{f(x) : x ∈ [xᵢ₋₁, xᵢ]}. The **upper Darboux sum** U(f, P) = Σ Mᵢ(xᵢ − xᵢ₋₁) overestimates the area by using the tallest rectangle on each subinterval; the **lower Darboux sum** L(f, P) = Σ mᵢ(xᵢ − xᵢ₋₁) underestimates by using the shortest. The true "area" — if it exists — must lie between them.

The key insight: as you refine partitions (add more points), upper sums can only decrease and lower sums can only increase. So the infimum of all upper sums and the supremum of all lower sums are well-defined quantities — call them U*(f) and L*(f). The function f is **Riemann integrable** on [a,b] if and only if U*(f) = L*(f), and this common value is ∫ₐᵇ f(x) dx. The condition U* = L* means the upper and lower approximations squeeze together, leaving no room for ambiguity about the area. This is the same "squeeze" logic you saw in limit proofs, now applied to the integral.

Why is this definition preferable to simply taking Riemann sums with sample points? Because Darboux sums avoid the arbitrary choice of where to sample — they use the most extreme values (sup and inf) on each subinterval, giving a partition-only criterion for integrability. This makes it straightforward to prove that continuous functions are integrable (they are uniformly continuous on closed intervals, so M_i − m_i can be made uniformly small), and to characterize exactly which discontinuous functions are integrable (those whose discontinuities form a set of measure zero). The Darboux approach is the cleanest path to the **Riemann-Lebesgue integrability criterion** and connects naturally to the Lebesgue integral you may encounter later.
