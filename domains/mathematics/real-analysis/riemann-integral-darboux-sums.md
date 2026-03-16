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
status: draft
---

# Riemann Integral via Darboux Sums

## Core Idea
The Riemann integral is defined via Darboux sums: partition [a,b] into subintervals, compute upper (U) and lower (L) sums using suprema and infima of f on each subinterval. The integral exists if inf U = sup L. This definition is equivalent to Riemann sums and clarifies when functions are integrable: discontinuities on a set of measure zero are allowed.

## Explainer

You already have two powerful tools: the rigorous derivative (which taught you that calculus concepts require careful ε-δ formulation) and suprema and infima (which give you a precise way to talk about the least upper bound and greatest lower bound of a set of values). The **Riemann integral** via Darboux sums puts these tools together to define what "area under a curve" actually means — rigorously, without hand-waving.

The construction begins with a **partition** P = {a = x₀ < x₁ < … < xₙ = b} of the interval [a,b] into n subintervals. On each subinterval [xᵢ₋₁, xᵢ], the function f takes some set of values. Using the supremum, you can define Mᵢ = sup{f(x) : x ∈ [xᵢ₋₁, xᵢ]}, and using the infimum, mᵢ = inf{f(x) : x ∈ [xᵢ₋₁, xᵢ]}. The **upper Darboux sum** U(f, P) = Σ Mᵢ(xᵢ − xᵢ₋₁) overestimates the area by using the tallest rectangle on each subinterval; the **lower Darboux sum** L(f, P) = Σ mᵢ(xᵢ − xᵢ₋₁) underestimates by using the shortest. The true "area" — if it exists — must lie between them.

The key insight: as you refine partitions (add more points), upper sums can only decrease and lower sums can only increase. So the infimum of all upper sums and the supremum of all lower sums are well-defined quantities — call them U*(f) and L*(f). The function f is **Riemann integrable** on [a,b] if and only if U*(f) = L*(f), and this common value is ∫ₐᵇ f(x) dx. The condition U* = L* means the upper and lower approximations squeeze together, leaving no room for ambiguity about the area. This is the same "squeeze" logic you saw in limit proofs, now applied to the integral.

Why is this definition preferable to simply taking Riemann sums with sample points? Because Darboux sums avoid the arbitrary choice of where to sample — they use the most extreme values (sup and inf) on each subinterval, giving a partition-only criterion for integrability. This makes it straightforward to prove that continuous functions are integrable (they are uniformly continuous on closed intervals, so M_i − m_i can be made uniformly small), and to characterize exactly which discontinuous functions are integrable (those whose discontinuities form a set of measure zero). The Darboux approach is the cleanest path to the **Riemann-Lebesgue integrability criterion** and connects naturally to the Lebesgue integral you may encounter later.
