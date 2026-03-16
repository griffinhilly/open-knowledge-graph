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
status: draft
---

# Best Rational Approximations

## Core Idea
The convergents p_n/q_n of a continued fraction are the best rational approximations to a real number α: no fraction with smaller denominator approximates α as well. This optimality underpins Diophantine approximation and factorization algorithms.

## Explainer

From your work with continued fractions, you know that every real number α has a representation [a₀; a₁, a₂, …], and that cutting this expansion off at each stage yields the **convergents** p₀/q₀, p₁/q₁, p₂/q₂, … — rational numbers that approach α. What you may not have appreciated is just how special these convergents are: they are not merely convenient stopping points, they are the *optimal* rational approximations in a precise sense.

The formal claim is this: if p/q is any fraction with 0 < q ≤ qₙ, then |α − pₙ/qₙ| ≤ |α − p/q|. In words, no fraction with denominator as small as qₙ approximates α better than the nth convergent does. To feel why this is remarkable, consider approximating π. The fractions 3/1, 22/7, 333/106, 355/113 are successive convergents of π. Try as you might, you cannot find a fraction with denominator ≤ 113 that matches π better than 355/113 does — and 355/113 is accurate to six decimal places. The continued fraction algorithm is not just producing *good* approximations; it is producing the *best possible* approximations for each denominator budget.

The proof of this optimality leans on the **mediants** and interlacing structure you encountered in continued fractions. The key algebraic identity is pₙqₙ₋₁ − pₙ₋₁qₙ = (−1)ⁿ, which tells you consecutive convergents straddle α from opposite sides and cannot be bettered without increasing the denominator. If some fraction p/q with q < qₙ₊₁ were a better approximation than pₙ/qₙ, you could show that it would have to be pₙ/qₙ itself — a contradiction.

This optimality has practical consequences that reach well beyond pure mathematics. The **Stern-Brocot tree** organizes all fractions by denominator in a way that mirrors convergent structure. In signal processing and gear design, you often need to approximate an irrational ratio (like a target frequency ratio) using integers — the convergents give you the best ratio for any given constraint on the size of the numerator or denominator. In the **Lenstra–Lenstra–Lovász (LLL) algorithm** for lattice basis reduction, the same idea of "best approximation for bounded denominator" underlies efficient factorization and cryptanalysis. The humble convergent, it turns out, is one of the most useful computational primitives in algorithmic number theory.
