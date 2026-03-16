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
stage: advanced
status: draft
---

# Completeness of Lᵖ (Riesz-Fischer Theorem)

## Core Idea
Lᵖ(μ) is a complete normed space (Banach space) for 1 ≤ p ≤ ∞. Riesz-Fischer states that any Cauchy sequence in Lᵖ converges to a function in Lᵖ, making it a natural setting for limiting processes.

## Explainer

Completeness is the property that guarantees no sequences "fall through the cracks." A metric space is complete if every Cauchy sequence converges to a limit *inside the space* — there are no missing limit points. You have already worked with this in metric spaces generally. The **Riesz-Fischer theorem** establishes that Lᵖ spaces have this property: if f₁, f₂, f₃, ... is a sequence of Lᵖ functions where ‖fₙ - fₘ‖ₚ → 0 as n, m → ∞ (a Cauchy sequence in Lᵖ norm), then there exists f ∈ Lᵖ such that ‖fₙ - f‖ₚ → 0.

Why might completeness fail without careful construction? Consider approximating a jump-discontinuous function by smooth ones: you can build a Cauchy sequence in Lᵖ whose pointwise limit is discontinuous or even unbounded at individual points. The key is that Lᵖ doesn't care about individual pointwise values — functions that agree almost everywhere are identified as equal. This coarser notion of equality is precisely what rescues completeness: the limit function exists in Lᵖ even when its pointwise behavior is irregular.

The proof strategy for Riesz-Fischer is instructive in its own right. Rather than working directly with a general Cauchy sequence, you extract a subsequence that converges quickly enough to form an absolutely convergent series. The **Hölder inequality** (your prerequisite) controls how Lᵖ norms interact, ensuring that convergence in norm is powerful enough to dominate term-by-term estimates. The dominated convergence theorem then allows you to pass the limit inside the integral, verifying that the limit function has finite Lᵖ norm and therefore belongs to the space.

Without completeness, the standard theorems of functional analysis collapse. The **Banach space** structure of Lᵖ — completeness together with the norm — enables the Hahn-Banach theorem, the open mapping theorem, and the uniform boundedness principle. L² in particular becomes a Hilbert space, where orthogonal projections and spectral decompositions live. Completeness is the structural guarantee that analysis in Lᵖ is safe: limits of approximating sequences always land back in the space you started from.
