---
id: cauchy-sequences-metric-spaces
title: Cauchy Sequences in Metric Spaces
domain: mathematics
course: topology
prerequisites:
- id: metric-topology-from-metric
  type: hard
- id: cauchy-sequences-and-completeness
  type: soft
builds-toward:
- completeness-metric-spaces-definition
tags:
- cauchy-sequences
- convergence
stage: abstract-reasoning
status: draft
---

# Cauchy Sequences in Metric Spaces

## Core Idea
A sequence (xₙ) is Cauchy if for every ε > 0 there exists N such that d(xₙ, xₘ) < ε for all n,m > N. In ℝ every Cauchy sequence converges (completeness). In ℚ or incomplete spaces, Cauchy sequences may fail to converge. Cauchy sequences measure whether terms 'cluster' without requiring a limit point.

## How It's Best Learned
Construct Cauchy sequences in ℚ that converge to irrational limits (e.g., rational approximations to √2). Show that in complete spaces every Cauchy sequence converges, and identify counterexamples in incomplete spaces.

## Common Misconceptions
- Assuming every Cauchy sequence must converge; this only holds in complete spaces.
- Confusing the Cauchy criterion with bounded sequences; Cauchy implies bounded, but not vice versa.
- Thinking the metric must come from a norm; Cauchy sequences are defined for any metric space.

## Explainer

You already understand Cauchy sequences in ℝ: a sequence (xₙ) is Cauchy if its terms eventually get arbitrarily close to *each other*, regardless of whether you can name a limit. The key insight is that the Cauchy property is *intrinsic* to the sequence — it doesn't depend on any proposed limit point. This makes it possible to ask whether a sequence is "trying to converge" even in a space where the limit might not exist.

In a **metric space** (X, d), the same definition applies word-for-word: (xₙ) is **Cauchy** if for every ε > 0 there exists N such that d(xₙ, xₘ) < ε for all n, m > N. The metric d(xₙ, xₘ) measures the distance between two terms of the sequence using whatever distance function defines your space. In ℝ, d is the usual absolute value, so this recovers the standard definition. But now consider ℚ with the same distance. The sequence 3, 3.1, 3.14, 3.141, 3.1415, … of rational approximations to π is Cauchy in ℚ — the terms get arbitrarily close together — but it does *not* converge in ℚ, because π is not a rational number. The sequence is clustering, but it's clustering around a point that doesn't exist in the space.

This gap between "Cauchy" and "convergent" is the key concept. In ℝ, every Cauchy sequence converges — this is the **completeness** of the real numbers, and it's essentially the defining property that distinguishes ℝ from ℚ. A metric space is called **complete** if every Cauchy sequence in it converges to a point within it. Complete spaces have no "holes" where sequences could try to converge but fail. ℝⁿ is complete, as are closed subsets of complete metric spaces. ℚ is not complete; neither is the open interval (0, 1) under the usual metric (the sequence 1/n is Cauchy but converges to 0, which isn't in the space).

The practical importance is that completeness licenses many of the most powerful theorems in analysis and functional analysis — the Banach fixed-point theorem, the open mapping theorem, Baire category theorem — all require complete metric spaces. When you work with function spaces or sequence spaces, checking completeness is often the first step before applying these tools. The Cauchy criterion provides a way to establish convergence without knowing the limit in advance: if you can show a sequence is Cauchy and your space is complete, convergence is guaranteed. This will become essential when you study completeness of metric spaces formally.

