---
id: best-rational-approximations
title: Best Rational Approximations
domain: mathematics
course: number-theory
prerequisites:
- id: continued-fractions
  type: hard
tags:
- approximation
- convergents
- continued-fractions
stage: advanced
status: validated
---

# Best Rational Approximations

## Core Idea
The convergents p_n/q_n of a continued fraction are the best rational approximations to a real number α: no fraction with smaller denominator approximates α as well. This optimality underpins Diophantine approximation and factorization algorithms.

## Questions

```yaml
- question: "Which statement best captures what it means for a convergent pₙ/qₙ to be a 'best rational approximation' to α?"
  type: multiple-choice
  options:
    - "pₙ/qₙ is closer to α than any other fraction with denominator strictly less than or equal to qₙ"
    - "pₙ/qₙ is the fraction with the smallest absolute error among all rationals"
    - "pₙ/qₙ is closer to α than any fraction whose denominator is a multiple of qₙ"
    - "pₙ/qₙ is the fraction with the smallest numerator that falls within 1/qₙ² of α"
  answer: 0
  explanation: "The formal claim is precise: no fraction p/q with 0 < q ≤ qₙ approximates α better than the nth convergent does. This is stronger than saying convergents are 'very good' approximations — it is an optimality guarantee. Option B is wrong because the claim is not global across all rationals, just among fractions with denominator up to qₙ. Options C and D describe unrelated properties."

- question: "A gear designer needs to approximate the ratio √2 ≈ 1.41421 using integers, and the largest gear has at most 100 teeth (denominator ≤ 100). The convergents of √2 include 1/1, 3/2, 7/5, 17/12, 41/29, 99/70. Which fraction should she use, and why?"
  type: multiple-choice
  options:
    - "141/100 — closest decimal truncation within the constraint"
    - "99/70 — as the convergent with largest denominator ≤ 100, it is provably the best approximation for that budget"
    - "41/29 — smaller denominators are more mechanically reliable"
    - "Any fraction within 0.001 of √2 is equally valid for engineering purposes"
  answer: 1
  explanation: "The optimality theorem guarantees that 99/70, as a convergent, is the best rational approximation among all fractions with denominator ≤ 100 — not just the best among convergents. 141/100 seems closer as a decimal but actually has larger error (1.41 vs √2 ≈ 1.41421). Option D ignores the optimality: the continued fraction algorithm provides a provably optimal answer, making the search unnecessary."

- question: "A fraction that is not a convergent of α can never be a best rational approximation to α."
  type: true-false
  answer: true
  explanation: "By the optimality theorem, every best rational approximation to α must be a convergent. Non-convergents may approximate α tolerably well, but there always exists a convergent with a denominator no larger that does at least as well. This is why the continued fraction algorithm is not merely one method for finding good approximations — it is the algorithm that produces all best rational approximations."

- question: "It is possible to find a fraction p/q with q < qₙ that approximates α more closely than the nth convergent pₙ/qₙ."
  type: true-false
  answer: false
  explanation: "This is precisely what the best-approximation theorem rules out. No fraction with denominator smaller than qₙ can beat the nth convergent — that is the definition of 'best rational approximation.' The algebraic identity pₙqₙ₋₁ − pₙ₋₁qₙ = (−1)ⁿ, which shows consecutive convergents straddle α from opposite sides, is the key to proving this impossibility."

- question: "Why is it useful to know that convergents are the *best* rational approximations, rather than merely *good* ones?"
  type: short-answer
  answer: "The optimality guarantee means that no improvement is possible for a given denominator budget — no search is required. In applications such as gear ratios, frequency synthesis, or lattice reduction algorithms, the continued fraction algorithm hands you the provably optimal approximation at every step, making it the correct tool rather than a convenient heuristic."
  explanation: "The distinction between 'good' and 'best' is practically significant. Without optimality, you would need to exhaustively search fractions with small denominators to find the best one. With optimality, you run the continued fraction algorithm and stop — the convergent is guaranteed to be optimal. This is why continued fractions underlie efficient algorithms in signal processing, cryptanalysis (LLL), and numerical mathematics."
```

## Explainer

From your work with continued fractions, you know that every real number α has a representation [a₀; a₁, a₂, …], and that cutting this expansion off at each stage yields the **convergents** p₀/q₀, p₁/q₁, p₂/q₂, … — rational numbers that approach α. What you may not have appreciated is just how special these convergents are: they are not merely convenient stopping points, they are the *optimal* rational approximations in a precise sense.

The formal claim is this: if p/q is any fraction with 0 < q ≤ qₙ, then |α − pₙ/qₙ| ≤ |α − p/q|. In words, no fraction with denominator as small as qₙ approximates α better than the nth convergent does. To feel why this is remarkable, consider approximating π. The fractions 3/1, 22/7, 333/106, 355/113 are successive convergents of π. Try as you might, you cannot find a fraction with denominator ≤ 113 that matches π better than 355/113 does — and 355/113 is accurate to six decimal places. The continued fraction algorithm is not just producing *good* approximations; it is producing the *best possible* approximations for each denominator budget.

The proof of this optimality leans on the **mediants** and interlacing structure you encountered in continued fractions. The key algebraic identity is pₙqₙ₋₁ − pₙ₋₁qₙ = (−1)ⁿ, which tells you consecutive convergents straddle α from opposite sides and cannot be bettered without increasing the denominator. If some fraction p/q with q < qₙ₊₁ were a better approximation than pₙ/qₙ, you could show that it would have to be pₙ/qₙ itself — a contradiction.

This optimality has practical consequences that reach well beyond pure mathematics. The **Stern-Brocot tree** organizes all fractions by denominator in a way that mirrors convergent structure. In signal processing and gear design, you often need to approximate an irrational ratio (like a target frequency ratio) using integers — the convergents give you the best ratio for any given constraint on the size of the numerator or denominator. In the **Lenstra–Lenstra–Lovász (LLL) algorithm** for lattice basis reduction, the same idea of "best approximation for bounded denominator" underlies efficient factorization and cryptanalysis. The humble convergent, it turns out, is one of the most useful computational primitives in algorithmic number theory.
