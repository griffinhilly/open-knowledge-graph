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
status: validated
---

# Bolzano-Weierstrass Theorem

## Core Idea
Every bounded sequence in ℝ has a convergent subsequence. This theorem bridges sequential behavior and compactness: a bounded sequence must 'accumulate' somewhere due to completeness. It is equivalent to the Heine-Borel Theorem in ℝ and is the gateway to compact sets.

## Questions

```yaml
- question: "The sequence a_n = sin(n) is bounded (|sin(n)| ≤ 1 for all n) but does not converge. What does the Bolzano-Weierstrass theorem guarantee about this sequence?"
  type: multiple-choice
  options:
    - "The sequence must eventually converge since it is bounded"
    - "The sequence must become monotone at some point, after which it converges"
    - "The sequence has a convergent subsequence, even though the full sequence diverges"
    - "The sequence has at most one accumulation point in [−1, 1]"
  answer: 2
  explanation: "Bolzano-Weierstrass guarantees that every bounded sequence has a *convergent subsequence*, not that the sequence itself converges. sin(n) is bounded and nowhere near convergent — it oscillates without settling — but there exist infinite subsequences of its values that do converge. This distinction between 'the sequence converges' and 'a subsequence converges' is the essential content of the theorem."

- question: "The proof of Bolzano-Weierstrass by repeated interval bisection uses which fundamental property of ℝ at its crucial step?"
  type: multiple-choice
  options:
    - "The archimedean property — for any real number, there exists a larger integer"
    - "The density of ℚ — between any two reals there is a rational number"
    - "Completeness — the nested interval property guarantees that the intersection of nested closed intervals contains a point of ℝ"
    - "The uncountability of ℝ — the sequence cannot exhaust all real numbers"
  answer: 2
  explanation: "The bisection produces nested closed intervals [a_n, b_n] with lengths shrinking to zero. The nested interval property — a consequence of completeness — guarantees their intersection contains exactly one real point L. This is where completeness is used: in ℚ, the same bisection might produce intervals whose intersection is irrational, so no rational limit point exists. Bolzano-Weierstrass is a theorem about ℝ precisely because ℝ is complete."

- question: "The Bolzano-Weierstrass theorem holds in the rational numbers ℚ: every bounded sequence of rationals has a convergent subsequence converging to a rational limit."
  type: true-false
  answer: false
  explanation: "This fails because ℚ is not complete — it has 'holes.' A sequence of rationals can converge to an irrational number (e.g., the decimal approximations 1, 1.4, 1.41, 1.414, ... converge to √2). Any subsequence of this rational sequence also converges to √2, which is not in ℚ. The theorem holds in ℝ because ℝ has no such holes — every Cauchy sequence (and hence every limit point produced by the bisection argument) corresponds to an actual real number."

- question: "Bolzano-Weierstrass implies that every bounded sequence in ℝ converges."
  type: true-false
  answer: false
  explanation: "A bounded sequence need not converge — it need only have a convergent subsequence. sin(n) is a standard counterexample: bounded but not convergent. The theorem guarantees accumulation points, not convergence of the whole sequence. A bounded sequence converges if and only if it has exactly one accumulation point (equivalently, all its convergent subsequences share the same limit). Bolzano-Weierstrass guarantees at least one accumulation point; convergence requires at most one."

- question: "Why does the Bolzano-Weierstrass theorem fail in ℚ but hold in ℝ, and what does this reveal about the role of completeness in the theorem?"
  type: short-answer
  answer: "The bisection proof produces a limit point L as the intersection of nested intervals. In ℝ, completeness guarantees L exists as a real number, so every subsequence selected from those intervals converges to L within ℝ. In ℚ, L might be irrational — a 'hole' that ℚ does not contain — and the constructed subsequence converges to something outside the space. Bolzano-Weierstrass is therefore not a theorem about sequences per se; it is a theorem about the completeness of ℝ expressed in sequential language. The theorem fails in any incomplete metric space where limit points can fall outside the space."
  explanation: "This connection explains why Bolzano-Weierstrass is equivalent to the Heine-Borel theorem in ℝ: both are ways of asserting that closed bounded subsets of ℝ are 'compact' — they retain all their limit points. Completeness is the structural property that makes this possible."
```

## Explainer

Start with intuition. You have a sequence of points all trapped inside, say, the interval [−10, 10]. There are infinitely many of them, but they are confined to a finite cage. They cannot spread out forever. So they must pile up somewhere — there must be some value that the sequence visits arbitrarily often, or at least gets arbitrarily close to infinitely many times. The **Bolzano-Weierstrass Theorem** makes this intuition rigorous: every bounded sequence in ℝ contains a **convergent subsequence**.

The standard proof uses repeated bisection — a technique you've likely encountered in root-finding. Take the interval [a, b] containing all terms of the sequence. Cut it in half. At least one half must contain infinitely many terms of the sequence (since the sequence is infinite and both halves together contain all terms). Choose that half, call it [a₁, b₁], and note that it contains infinitely many terms. Now bisect again. Repeat indefinitely. Each nested interval [aₙ, bₙ] has length (b−a)/2ⁿ → 0, so by the nested interval property (which follows from completeness of ℝ), there is a single point L in their intersection. At each stage, pick a term of the sequence from [aₙ, bₙ] whose index is larger than the previous pick. This constructs a subsequence converging to L.

The theorem reveals why **completeness** is so essential. In the rationals ℚ, the same bisection argument would run, but the limit point L might be irrational — a hole in ℚ — and the subsequence would fail to converge within ℚ. Bolzano-Weierstrass is a theorem about ℝ specifically because ℝ has no holes. This connects to your study of subsequences: a subsequence is just an infinite thinning of the original sequence, preserving the same terms in the same order. The theorem guarantees that even if the original sequence behaves wildly, some infinite thinning must settle down.

The relationship to **compactness** is deep. A set K ⊆ ℝ is sequentially compact if every sequence in K has a subsequence converging to a point in K. Bolzano-Weierstrass proves that every closed bounded interval [a, b] is sequentially compact. In metric spaces, sequential compactness and compactness (every open cover has a finite subcover) are equivalent. So this theorem is not merely a fact about sequences — it is the sequential face of compactness, one of the most important structures in analysis and topology. Every convergence argument in real analysis that assumes bounded sequences — in optimization, in series, in function approximation — implicitly relies on Bolzano-Weierstrass lurking in the background.
