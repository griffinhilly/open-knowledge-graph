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
stage: formal-systems
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

## Questions

```yaml
- question: "The sequence 1, 1.4, 1.41, 1.414, 1.4142, … (rational approximations to √2) is considered in the metric space (ℚ, d) where d is the usual absolute value. Which statement is correct?"
  type: multiple-choice
  options:
    - "It converges in ℚ because the terms get arbitrarily close to each other"
    - "It is Cauchy in ℚ but does not converge in ℚ, because √2 is irrational and not in ℚ"
    - "It is not Cauchy in ℚ because it has no limit in ℚ"
    - "It converges in ℚ to the rational number closest to √2"
  answer: 1
  explanation: "The sequence is Cauchy because its terms get arbitrarily close to one another — the Cauchy property is intrinsic to the sequence and does not require a limit. But √2 ∉ ℚ, so the sequence has no limit in ℚ. This is the canonical example showing that Cauchy ≠ convergent in incomplete spaces. Option C is the key misconception: the absence of a limit does not make the sequence non-Cauchy."

- question: "In which of the following spaces does every Cauchy sequence converge?"
  type: multiple-choice
  options:
    - "ℚ with the usual metric"
    - "The open interval (0, 1) with the usual metric"
    - "ℝ with the usual metric"
    - "Any metric space that contains a dense subset of ℝ"
  answer: 2
  explanation: "ℝ is complete: every Cauchy sequence of real numbers converges to a real number. ℚ is incomplete (the √2 example). The open interval (0, 1) is incomplete because the sequence 1/2, 1/3, 1/4, … is Cauchy in (0, 1) but converges to 0, which is not in the space. Option D is false — density doesn't guarantee completeness."

- question: "Every Cauchy sequence in a metric space is bounded."
  type: true-false
  answer: true
  explanation: "If (xₙ) is Cauchy, then for ε = 1 there exists N such that d(xₙ, xₘ) < 1 for all n, m > N. In particular, all terms beyond index N lie within distance 1 of x_{N+1}. The finitely many terms up to index N are also at finite distance from x_{N+1}. Taking the maximum of these finitely many distances plus 1 gives a global bound. So boundedness is a consequence of the Cauchy property, not an independent assumption."

- question: "If a sequence converges in a metric space, the space must be complete."
  type: true-false
  answer: false
  explanation: "Convergence of some sequences does not imply completeness. A space is complete only if every Cauchy sequence converges. ℚ contains many convergent sequences (e.g., 1, 1, 1, … converges to 1 ∈ ℚ), yet ℚ is not complete because the sequence of rational approximations to √2 is Cauchy but does not converge in ℚ. Completeness is a global property of the space, not a statement about individual sequences."

- question: "What does it mean for a metric space to be 'complete,' and why can the same sequence be Cauchy in one space but fail to converge in another?"
  type: short-answer
  answer: "A metric space is complete if every Cauchy sequence in it converges to a point within the space. The same sequence can be Cauchy in multiple spaces (since the Cauchy property depends only on mutual distances between terms), but convergence requires the limit point to exist in the space. If the limit point is 'missing' — as √2 is missing from ℚ — the sequence is Cauchy but non-convergent, revealing a 'hole' in the space."
  explanation: "This is the heart of the topic: Cauchy sequences detect clustering behavior without naming a limit, while convergence requires the limit to actually exist in the space. The same sequence of rational approximations to √2 is Cauchy in both ℚ and ℝ, but it only converges in ℝ (where √2 lives). Completeness is the property that rules out such holes, and it is the key hypothesis in many major theorems of analysis."
```

## Explainer

You already understand Cauchy sequences in ℝ: a sequence (xₙ) is Cauchy if its terms eventually get arbitrarily close to *each other*, regardless of whether you can name a limit. The key insight is that the Cauchy property is *intrinsic* to the sequence — it doesn't depend on any proposed limit point. This makes it possible to ask whether a sequence is "trying to converge" even in a space where the limit might not exist.

In a **metric space** (X, d), the same definition applies word-for-word: (xₙ) is **Cauchy** if for every ε > 0 there exists N such that d(xₙ, xₘ) < ε for all n, m > N. The metric d(xₙ, xₘ) measures the distance between two terms of the sequence using whatever distance function defines your space. In ℝ, d is the usual absolute value, so this recovers the standard definition. But now consider ℚ with the same distance. The sequence 3, 3.1, 3.14, 3.141, 3.1415, … of rational approximations to π is Cauchy in ℚ — the terms get arbitrarily close together — but it does *not* converge in ℚ, because π is not a rational number. The sequence is clustering, but it's clustering around a point that doesn't exist in the space.

This gap between "Cauchy" and "convergent" is the key concept. In ℝ, every Cauchy sequence converges — this is the **completeness** of the real numbers, and it's essentially the defining property that distinguishes ℝ from ℚ. A metric space is called **complete** if every Cauchy sequence in it converges to a point within it. Complete spaces have no "holes" where sequences could try to converge but fail. ℝⁿ is complete, as are closed subsets of complete metric spaces. ℚ is not complete; neither is the open interval (0, 1) under the usual metric (the sequence 1/n is Cauchy but converges to 0, which isn't in the space).

The practical importance is that completeness licenses many of the most powerful theorems in analysis and functional analysis — the Banach fixed-point theorem, the open mapping theorem, Baire category theorem — all require complete metric spaces. When you work with function spaces or sequence spaces, checking completeness is often the first step before applying these tools. The Cauchy criterion provides a way to establish convergence without knowing the limit in advance: if you can show a sequence is Cauchy and your space is complete, convergence is guaranteed. This will become essential when you study completeness of metric spaces formally.

