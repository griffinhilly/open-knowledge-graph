---
id: monotone-convergence-theorem
title: Monotone Convergence Theorem
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
- id: completeness-axiom-lub
  type: hard
builds-toward:
- series-convergence-rigorous
tags:
- convergence
- monotone
- supremum
- bounded
stage: advanced
status: draft
---

# Monotone Convergence Theorem

## Core Idea
If a sequence is monotone increasing and bounded above, it converges to its supremum; if monotone decreasing and bounded below, it converges to its infimum. This theorem directly applies completeness to guarantee convergence without computing limits explicitly. It is one of the most practical convergence tools.

## Explainer

From your work with the **completeness axiom** (the Least Upper Bound property), you know that ℝ has no gaps: any non-empty set bounded above has a supremum in ℝ. The **Monotone Convergence Theorem** (MCT) is essentially the completeness axiom put to work on sequences. The idea is elegant — a sequence that only increases and never exceeds a ceiling must eventually settle somewhere, and that somewhere is the supremum of its range.

Here's the argument in plain terms. Suppose (aₙ) is increasing (aₙ ≤ aₙ₊₁ for all n) and bounded above by some M. The set {aₙ : n ∈ ℕ} is non-empty and bounded above, so by the LUB property it has a supremum L = sup{aₙ}. Claim: aₙ → L. Given any ε > 0, L − ε is not an upper bound (since L is the least upper bound), so there exists some term a_N > L − ε. Since the sequence is increasing, all subsequent terms satisfy a_N ≤ aₙ ≤ L for n ≥ N, giving |aₙ − L| = L − aₙ < ε. That's precisely the **epsilon-N definition of convergence** you already know. The two prerequisites — completeness and epsilon-N convergence — are both essential ingredients.

The power of the MCT is that it guarantees convergence *without computing the limit first*. In many applications you can verify monotonicity and boundedness directly, even when finding the limit explicitly is hard. A classic example: define a₁ = 1 and aₙ₊₁ = √(2 + aₙ). Checking that this sequence is increasing (by induction) and bounded above by 2 is elementary, so MCT guarantees convergence to some limit L. You can then *solve for L* by taking the limit of both sides: L = √(2 + L), giving L² − L − 2 = 0, so L = 2. The MCT does the hard work of existence; algebra does the rest.

The theorem pairs naturally with the Nested Interval Property and Bolzano-Weierstrass theorem as one of the fundamental tools that make completeness operational. Together they show that ℝ's completeness isn't just a philosophical claim about the number line having no gaps — it's a working engine for proving that sequences converge. When you later study series, the MCT will appear again: a series with non-negative terms has partial sums that form a monotone increasing sequence, so it converges if and only if its partial sums are bounded above. That bridge from sequences to series flows directly from this theorem.
