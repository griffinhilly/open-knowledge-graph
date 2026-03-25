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
- rigorous-series-convergence
tags:
- convergence
- monotone
- supremum
- bounded
stage: advanced
status: validated
---

# Monotone Convergence Theorem

## Core Idea
If a sequence is monotone increasing and bounded above, it converges to its supremum; if monotone decreasing and bounded below, it converges to its infimum. This theorem directly applies completeness to guarantee convergence without computing limits explicitly. It is one of the most practical convergence tools.

## Questions

```yaml
- question: "A sequence is defined by a₁ = 2, aₙ₊₁ = √(aₙ + 6). A student wants to prove it converges but cannot find a closed form. How does the Monotone Convergence Theorem help?"
  type: multiple-choice
  options:
    - "MCT directly computes the limit by taking both sides to the limit and solving algebraically"
    - "MCT requires the limit to be known in advance, so the student must first solve L = √(L + 6)"
    - "By verifying that the sequence is monotone and bounded, MCT guarantees convergence to some limit L; the student can then solve for L using L = √(L + 6)"
    - "MCT applies only to decreasing sequences, so the student must first show the sequence eventually decreases"
  answer: 2
  explanation: "This is the key application pattern of MCT: verify monotonicity and boundedness first, conclude convergence exists (without knowing the limit), then find the limit by taking limits of both sides of the recursion. Option A is wrong — MCT guarantees existence, not a formula. Option B reverses the logical order: MCT lets you avoid computing L first. Option D is wrong — MCT applies to both increasing (bounded above) and decreasing (bounded below) sequences. The power is that existence precedes identification."

- question: "Which pair of conditions is sufficient for the Monotone Convergence Theorem to guarantee a sequence converges?"
  type: multiple-choice
  options:
    - "Bounded above and eventually positive"
    - "Monotone (increasing or decreasing) and bounded in the appropriate direction"
    - "Monotone or bounded — either condition alone is sufficient"
    - "Monotone, bounded, and with a known supremum that can be computed explicitly"
  answer: 1
  explanation: "MCT requires BOTH conditions together. A bounded sequence that is not monotone can oscillate and fail to converge (e.g., aₙ = (−1)ⁿ is bounded but diverges). A monotone sequence that is not bounded diverges to ±∞ (e.g., aₙ = n is increasing but unbounded and diverges). Option C is the most common misconception. Option D is wrong — the whole point of MCT is that you do not need to know the supremum explicitly in advance."

- question: "The Monotone Convergence Theorem can be used to prove that the sequence aₙ = sin(nπ/4) converges, because it is bounded between −1 and 1."
  type: true-false
  answer: false
  explanation: "Boundedness alone is not sufficient for MCT. The sequence sin(nπ/4) oscillates through values 0, √2/2, 1, √2/2, 0, −√2/2, −1, ... and is definitely not monotone. MCT requires both monotonicity and boundedness (in the appropriate direction). A bounded non-monotone sequence may or may not converge, but MCT cannot be invoked to decide. For this particular sequence, it fails to converge because it oscillates indefinitely."

- question: "The Monotone Convergence Theorem and the Least Upper Bound property (completeness of ℝ) are logically equivalent: each can be proved from the other."
  type: true-false
  answer: true
  explanation: "MCT is essentially the completeness axiom applied to sequences. The proof of MCT uses LUB directly: the range of a bounded increasing sequence is non-empty and bounded above, so by LUB it has a supremum, which the sequence converges to. Conversely, given MCT, you can recover LUB: for any non-empty set S bounded above, pick an increasing sequence of elements approaching sup S (possible by definition of supremum), apply MCT to get convergence, and the limit is sup S. The two are equivalent characterizations of ℝ's completeness. Neither holds in ℚ, where both break down."

- question: "Explain why the Monotone Convergence Theorem allows you to prove a sequence converges without first knowing what the limit is, and why this argument would fail if you were working in ℚ instead of ℝ."
  type: short-answer
  answer: "MCT guarantees convergence using only two properties — monotonicity and boundedness — that can be verified without knowing the limit. The argument: the range of a bounded increasing sequence is a non-empty set bounded above, so by the Least Upper Bound property of ℝ it has a supremum L in ℝ. An epsilon argument then shows the sequence converges to L. The limit is not assumed; it is produced by completeness. In ℚ, the LUB property fails: bounded sets can have no rational supremum. For example, the sequence of rational approximations to √2 (1, 1.4, 1.41, 1.414, ...) is increasing and bounded above by 2 in ℚ, but its supremum √2 is irrational — not in ℚ. So the sequence has no limit in ℚ, and MCT fails to apply there."
```

## Explainer

From your work with the **completeness axiom** (the Least Upper Bound property), you know that ℝ has no gaps: any non-empty set bounded above has a supremum in ℝ. The **Monotone Convergence Theorem** (MCT) is essentially the completeness axiom put to work on sequences. The idea is elegant — a sequence that only increases and never exceeds a ceiling must eventually settle somewhere, and that somewhere is the supremum of its range.

Here's the argument in plain terms. Suppose (aₙ) is increasing (aₙ ≤ aₙ₊₁ for all n) and bounded above by some M. The set {aₙ : n ∈ ℕ} is non-empty and bounded above, so by the LUB property it has a supremum L = sup{aₙ}. Claim: aₙ → L. Given any ε > 0, L − ε is not an upper bound (since L is the least upper bound), so there exists some term a_N > L − ε. Since the sequence is increasing, all subsequent terms satisfy a_N ≤ aₙ ≤ L for n ≥ N, giving |aₙ − L| = L − aₙ < ε. That's precisely the **epsilon-N definition of convergence** you already know. The two prerequisites — completeness and epsilon-N convergence — are both essential ingredients.

The power of the MCT is that it guarantees convergence *without computing the limit first*. In many applications you can verify monotonicity and boundedness directly, even when finding the limit explicitly is hard. A classic example: define a₁ = 1 and aₙ₊₁ = √(2 + aₙ). Checking that this sequence is increasing (by induction) and bounded above by 2 is elementary, so MCT guarantees convergence to some limit L. You can then *solve for L* by taking the limit of both sides: L = √(2 + L), giving L² − L − 2 = 0, so L = 2. The MCT does the hard work of existence; algebra does the rest.

The theorem pairs naturally with the Nested Interval Property and Bolzano-Weierstrass theorem as one of the fundamental tools that make completeness operational. Together they show that ℝ's completeness isn't just a philosophical claim about the number line having no gaps — it's a working engine for proving that sequences converge. When you later study series, the MCT will appear again: a series with non-negative terms has partial sums that form a monotone increasing sequence, so it converges if and only if its partial sums are bounded above. That bridge from sequences to series flows directly from this theorem.
