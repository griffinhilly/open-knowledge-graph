---
id: introduction-p-adic-numbers
title: Introduction to p-adic Numbers
domain: mathematics
course: number-theory
prerequisites:
- id: p-adic-valuation
  type: hard
- id: metric-spaces-definition
  type: soft
builds-toward:
- hensels-lemma
tags:
- p-adic-numbers
- metric-spaces
- completion
stage: advanced
status: validated
---

# Introduction to p-adic Numbers

## Core Idea
The p-adic numbers ℚ_p are the completion of ℚ under the p-adic metric d_p(x, y) = p^(-v_p(x-y)). They provide a 'p-adic topology' where convergence is based on divisibility by powers of p, enabling tools like Hensel lifting.

## Questions

```yaml
- question: "In the 7-adic metric, which of the following numbers is closest to 0?"
  type: multiple-choice
  options:
    - "3"
    - "7"
    - "49"
    - "343"
  answer: 3
  explanation: "The 7-adic absolute value is |x|₇ = 7^(−v₇(x)), where v₇(x) counts how many times 7 divides x. For 3: v₇(3) = 0, so |3|₇ = 1. For 7: v₇(7) = 1, so |7|₇ = 1/7. For 49 = 7²: v₇(49) = 2, so |49|₇ = 1/49. For 343 = 7³: v₇(343) = 3, so |343|₇ = 1/343. Numbers highly divisible by 7 are *small* in the 7-adic metric — a complete inversion of ordinary intuition about size."

- question: "A student claims that the sequence 5, 25, 125, 625, … (powers of 5) diverges to infinity in the 5-adic metric. Is this correct?"
  type: multiple-choice
  options:
    - "Yes — powers of 5 grow without bound, so they diverge in any metric"
    - "No — in the 5-adic metric, |5ⁿ|₅ = 5^(−n) → 0, so the sequence converges to 0"
    - "No — the sequence converges to −1 in ℚ₅"
    - "Yes — the 5-adic metric agrees with the ordinary absolute value for positive integers"
  answer: 1
  explanation: "In the 5-adic metric, |5ⁿ|₅ = 5^(−v₅(5ⁿ)) = 5^(−n), which tends to 0 as n → ∞. So the sequence converges to 0, not infinity. This is the core reversal: large powers of p become *small* in the p-adic world because they are highly divisible by p. This directly contradicts Archimedean intuition, where larger numbers are farther from 0."

- question: "In the 3-adic numbers ℚ₃, the infinite series 2 + 2·3 + 2·3² + 2·3³ + ··· converges, and its sum equals −1."
  type: true-false
  answer: true
  explanation: "The partial sums Sₙ = 2(1 + 3 + ··· + 3^(n−1)) = 3ⁿ − 1. In the 3-adic metric, |Sₙ − (−1)|₃ = |3ⁿ|₃ = 3^(−n) → 0. So the series converges to −1 in ℚ₃. The 3-adic representation of −1 is an infinite string of 2's in base 3 — extending infinitely to the left. This illustrates how p-adic numbers represent familiar quantities (even negative integers) through infinite expansions in powers of p, and how convergence in the p-adic metric is entirely governed by divisibility."

- question: "The p-adic numbers ℚ_p are just the rational numbers ℚ with a different notation — they introduce no new mathematical objects."
  type: true-false
  answer: false
  explanation: "ℚ_p is a proper extension of ℚ, constructed by completing ℚ under the p-adic metric. It contains elements that are not rational numbers — limits of p-adic Cauchy sequences that do not converge in ℚ. The construction is exactly analogous to how ℝ extends ℚ by adding limits of ordinary Cauchy sequences (like √2 and π). ℚ_p adds new elements like infinite p-adic expansions that represent quantities not in ℚ. By Ostrowski's theorem, ℝ and all the ℚ_p are the *only* completions of ℚ."

- question: "How does the construction of ℚ_p parallel the construction of ℝ, and what does this analogy reveal about the significance of p-adic numbers?"
  type: short-answer
  answer: "ℝ is the completion of ℚ under the ordinary absolute value — it adds all limits of rational Cauchy sequences that were missing from ℚ under the usual metric. ℚ_p is the completion of ℚ under the p-adic absolute value |x|_p = p^(−v_p(x)) — it adds all limits of rational Cauchy sequences that are Cauchy under the p-adic metric but don't converge in ℚ. The analogy reveals that ℝ and the family {ℚ_p : p prime} are all equally valid completions of the rationals, each capturing a different notion of nearness. Ostrowski's theorem shows these are the *only* completions, making them together a complete picture of the ways ℚ can be metrically extended."
  explanation: "This parallel is philosophically important: ℝ is not uniquely 'natural' as a number system containing ℚ. The p-adic completions are just as natural from a purely algebraic standpoint, and arise inevitably when studying congruences and divisibility in number theory. The p-adic absolute value is non-Archimedean (satisfying the ultrametric inequality), giving ℚ_p a radically different geometry from ℝ."
```

## Explainer

You already know the **p-adic valuation** v_p(n): it counts how many times the prime p divides an integer n. If n = 12 and p = 2, then v₂(12) = 2 because 12 = 4 × 3. The p-adic absolute value is defined as |x|_p = p^(−v_p(x)), with |0|_p = 0. This inverts our usual sense of size: numbers highly divisible by p are *small* in the p-adic world. In the 5-adic world, 125 = 5³ has absolute value 5⁻³ = 1/125 — it's tiny, not large.

The **p-adic metric** d_p(x, y) = |x − y|_p measures how close two numbers are by how divisible their difference is by p. Two integers are close if their difference is divisible by a high power of p. This is a legitimate metric, and it satisfies the much stronger **ultrametric inequality**: d_p(x, z) ≤ max(d_p(x, y), d_p(y, z)). This "non-Archimedean" property means the hypotenuse of a triangle is never longer than its longest side — a world very different from the geometry you're used to.

From your study of metric spaces, you know that every metric space can be completed by adding limits of Cauchy sequences. The reals ℝ are the completion of ℚ under the usual absolute value. **ℚ_p is the completion of ℚ under the p-adic absolute value.** Concretely, every element of ℚ_p can be written as a formal power series in p: a₀ + a₁p + a₂p² + a₃p³ + ⋯, where each coefficient aᵢ is an integer between 0 and p−1. This looks like a base-p expansion, but it extends infinitely to the left (toward higher powers of p) rather than to the right.

This representation reveals surprising facts. In ℚ₃, the number −1 equals 2 + 2·3 + 2·3² + 2·3³ + ⋯ — an infinite string of 2's in base 3. This is valid because the partial sums converge 3-adically: after n terms, the error is 3ⁿ, and |3ⁿ|₃ = 3⁻ⁿ → 0. There are infinitely many p-adic number systems, one for each prime, and **Ostrowski's theorem** says these — together with the usual absolute value — are the only ways to complete the rationals. The reals and all the p-adic fields together capture every possible notion of size on ℚ.
