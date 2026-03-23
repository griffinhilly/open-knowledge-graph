---
id: lp-completeness
title: Completeness of Lᵖ (Riesz-Fischer Theorem)
domain: mathematics
course: measure-theory-and-functional-analysis
prerequisites:
- id: holder-inequality
  type: hard
- id: completeness-metric-spaces
  type: hard
builds-toward:
- banach-spaces
tags:
- lp-spaces
- completeness
stage: expert
status: validated
---

# Completeness of Lᵖ (Riesz-Fischer Theorem)

## Core Idea
Lᵖ(μ) is a complete normed space (Banach space) for 1 ≤ p ≤ ∞. Riesz-Fischer states that any Cauchy sequence in Lᵖ converges to a function in Lᵖ, making it a natural setting for limiting processes.

## Questions

```yaml
- question: "A Cauchy sequence in Lᵖ converges to a function whose pointwise values may be highly irregular (e.g., undefined at individual points). Which feature of Lᵖ makes this acceptable?"
  type: multiple-choice
  options:
    - "Lᵖ norm controls pointwise values at all points, so irregular functions cannot belong to it"
    - "Functions in Lᵖ are identified up to sets of measure zero, so pointwise irregularity on a null set is irrelevant"
    - "The Hölder inequality prevents irregular limit functions from forming"
    - "Only smooth functions can be Cauchy sequences in Lᵖ"
  answer: 1
  explanation: "Lᵖ spaces consist of equivalence classes of functions that agree almost everywhere — two functions differing only on a set of measure zero are identified as equal. This coarser notion of equality rescues completeness: the limit of a Cauchy sequence in Lᵖ norm may be pointwise irregular or undefined at individual points, but as long as it belongs to the equivalence class of an Lᵖ function (finite Lᵖ norm almost everywhere), it belongs to the space."

- question: "The Riesz-Fischer theorem establishes that Lᵖ is complete. A student claims that L¹([0,1]) equipped with the L∞ norm is also complete. Which response is correct?"
  type: multiple-choice
  options:
    - "The student is correct; any norm on Lᵖ makes it complete"
    - "The student is incorrect; the L∞ norm is not even defined on all L¹ functions, so the claim is ill-formed, and L¹ with its natural norm is complete while L∞ is a different space"
    - "The student is incorrect; Banach spaces only apply to finite-dimensional spaces"
    - "The student is correct if we restrict to continuous functions"
  answer: 1
  explanation: "Completeness is norm-dependent. L¹([0,1]) with its natural L¹ norm is complete by Riesz-Fischer. But equipping L¹ with the L∞ norm is ill-formed: most L¹ functions are not essentially bounded, so the L∞ norm is undefined on most of L¹. The key point is that Riesz-Fischer establishes completeness for Lᵖ with respect to its natural Lᵖ norm; switching norms changes the topology and the function class entirely."

- question: "If a metric space is not complete, its Cauchy sequences still converge to limits that are in the space."
  type: true-false
  answer: false
  explanation: "This is exactly the negation of completeness. A metric space is complete if and only if every Cauchy sequence converges to a limit *within* the space. If the space is not complete, there exist Cauchy sequences whose limit points lie outside it — the space has 'gaps.' The rational numbers ℚ are a classic example: the sequence 3, 3.1, 3.14, 3.141, ... is Cauchy in ℚ but converges to π, which is irrational."

- question: "The completeness of Lᵖ guarantees that every Cauchy sequence in Lᵖ converges pointwise almost everywhere."
  type: true-false
  answer: false
  explanation: "Completeness guarantees convergence in the Lᵖ *norm* — ‖fₙ − f‖ₚ → 0 — not pointwise convergence. Norm convergence is strictly weaker: a Cauchy sequence in Lᵖ may fail to converge pointwise at individual points or even diverge almost everywhere, as long as the Lᵖ norm of the difference goes to zero. This separation between norm convergence and pointwise convergence is one of the key subtleties of Lᵖ theory."

- question: "Why does the standard proof of the Riesz-Fischer theorem extract a rapidly convergent subsequence rather than working directly with the Cauchy sequence? What does this strategy accomplish?"
  type: short-answer
  answer: "A general Cauchy sequence may converge arbitrarily slowly, making it hard to dominate all partial sums. By extracting a subsequence where ‖f_{n_{k+1}} − f_{n_k}‖ₚ < 2^{−k}, one can form an absolutely convergent series ∑|f_{n_{k+1}} − f_{n_k}|, then invoke the dominated convergence theorem to pass the limit inside the integral and verify the limit function has finite Lᵖ norm. Convergence of the original Cauchy sequence follows because any Cauchy sequence with a convergent subsequence converges to the same limit."
  explanation: "The subsequence strategy unlocks the dominated convergence theorem: if the dominating function (the L¹-summable bound on partial sums) is in Lᵖ, then the interchange of limit and integral is justified. For a rapidly convergent subsequence this bound is finite; for a slowly convergent sequence it need not be. Once the subsequence limit is established as an Lᵖ function, the Cauchy property forces the full sequence to converge to it."
```

## Explainer

Completeness is the property that guarantees no sequences "fall through the cracks." A metric space is complete if every Cauchy sequence converges to a limit *inside the space* — there are no missing limit points. You have already worked with this in metric spaces generally. The **Riesz-Fischer theorem** establishes that Lᵖ spaces have this property: if f₁, f₂, f₃, ... is a sequence of Lᵖ functions where ‖fₙ - fₘ‖ₚ → 0 as n, m → ∞ (a Cauchy sequence in Lᵖ norm), then there exists f ∈ Lᵖ such that ‖fₙ - f‖ₚ → 0.

Why might completeness fail without careful construction? Consider approximating a jump-discontinuous function by smooth ones: you can build a Cauchy sequence in Lᵖ whose pointwise limit is discontinuous or even unbounded at individual points. The key is that Lᵖ doesn't care about individual pointwise values — functions that agree almost everywhere are identified as equal. This coarser notion of equality is precisely what rescues completeness: the limit function exists in Lᵖ even when its pointwise behavior is irregular.

The proof strategy for Riesz-Fischer is instructive in its own right. Rather than working directly with a general Cauchy sequence, you extract a subsequence that converges quickly enough to form an absolutely convergent series. The **Hölder inequality** (your prerequisite) controls how Lᵖ norms interact, ensuring that convergence in norm is powerful enough to dominate term-by-term estimates. The dominated convergence theorem then allows you to pass the limit inside the integral, verifying that the limit function has finite Lᵖ norm and therefore belongs to the space.

Without completeness, the standard theorems of functional analysis collapse. The **Banach space** structure of Lᵖ — completeness together with the norm — enables the Hahn-Banach theorem, the open mapping theorem, and the uniform boundedness principle. L² in particular becomes a Hilbert space, where orthogonal projections and spectral decompositions live. Completeness is the structural guarantee that analysis in Lᵖ is safe: limits of approximating sequences always land back in the space you started from.
