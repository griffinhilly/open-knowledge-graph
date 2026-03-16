---
id: bolzano-weierstrass-theorem
title: Bolzano-Weierstrass Theorem
domain: mathematics
course: real-analysis
prerequisites:
- id: subsequences
  type: hard
- id: compact-sets
  type: soft
builds-toward:
- compact-sets
- heine-borel-theorem
tags:
- bolzano-weierstrass
- compactness
- subsequences
stage: advanced
status: draft
---

# Bolzano-Weierstrass Theorem

## Core Idea
Every bounded sequence in ℝ has a convergent subsequence. This theorem bridges sequential behavior and compactness: a bounded sequence must 'accumulate' somewhere due to completeness. It is equivalent to the Heine-Borel Theorem in ℝ and is the gateway to compact sets.

## Explainer

Start with intuition. You have a sequence of points all trapped inside, say, the interval [−10, 10]. There are infinitely many of them, but they are confined to a finite cage. They cannot spread out forever. So they must pile up somewhere — there must be some value that the sequence visits arbitrarily often, or at least gets arbitrarily close to infinitely many times. The **Bolzano-Weierstrass Theorem** makes this intuition rigorous: every bounded sequence in ℝ contains a **convergent subsequence**.

The standard proof uses repeated bisection — a technique you've likely encountered in root-finding. Take the interval [a, b] containing all terms of the sequence. Cut it in half. At least one half must contain infinitely many terms of the sequence (since the sequence is infinite and both halves together contain all terms). Choose that half, call it [a₁, b₁], and note that it contains infinitely many terms. Now bisect again. Repeat indefinitely. Each nested interval [aₙ, bₙ] has length (b−a)/2ⁿ → 0, so by the nested interval property (which follows from completeness of ℝ), there is a single point L in their intersection. At each stage, pick a term of the sequence from [aₙ, bₙ] whose index is larger than the previous pick. This constructs a subsequence converging to L.

The theorem reveals why **completeness** is so essential. In the rationals ℚ, the same bisection argument would run, but the limit point L might be irrational — a hole in ℚ — and the subsequence would fail to converge within ℚ. Bolzano-Weierstrass is a theorem about ℝ specifically because ℝ has no holes. This connects to your study of subsequences: a subsequence is just an infinite thinning of the original sequence, preserving the same terms in the same order. The theorem guarantees that even if the original sequence behaves wildly, some infinite thinning must settle down.

The relationship to **compactness** is deep. A set K ⊆ ℝ is sequentially compact if every sequence in K has a subsequence converging to a point in K. Bolzano-Weierstrass proves that every closed bounded interval [a, b] is sequentially compact. In metric spaces, sequential compactness and compactness (every open cover has a finite subcover) are equivalent. So this theorem is not merely a fact about sequences — it is the sequential face of compactness, one of the most important structures in analysis and topology. Every convergence argument in real analysis that assumes bounded sequences — in optimization, in series, in function approximation — implicitly relies on Bolzano-Weierstrass lurking in the background.
