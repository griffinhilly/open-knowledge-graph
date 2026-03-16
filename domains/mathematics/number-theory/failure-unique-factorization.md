---
id: failure-unique-factorization
title: Failure of Unique Factorization
domain: mathematics
course: number-theory
prerequisites:
- id: norm-algebraic-number-fields
  type: hard
builds-toward:
- introduction-ideal-class-group
tags:
- unique-factorization-failure
- algebraic-number-theory
stage: advanced
status: draft
---

# Failure of Unique Factorization

## Core Idea
Unlike ℤ and Gaussian integers, most rings of algebraic integers lack unique factorization. In ℤ[√(-5)], we have 6 = 2·3 = (1+√(-5))(1-√(-5)), two distinct factorizations. This motivates ideals, where factorization recovers uniqueness.

## Explainer

The unique factorization theorem — the fundamental theorem of arithmetic — guarantees that every integer greater than 1 factors into primes in exactly one way. This feels inevitable until you extend arithmetic to larger number systems and watch it break down. The norm of an algebraic integer, which you studied as a prerequisite, is the key tool for detecting irreducibility in these rings.

In the ring ℤ[√(-5)], consider the number 6. On one hand, 6 = 2 × 3. On the other hand, 6 = (1 + √(-5))(1 - √(-5)). Both are factorizations into elements that cannot be factored further — they are **irreducible** in ℤ[√(-5)]. To verify irreducibility, use norms: N(2) = 4, and there is no element in ℤ[√(-5)] with norm 2, since a² + 5b² = 2 has no integer solutions. So 2 cannot split. Similarly for 3, (1 + √(-5)), and (1 - √(-5)). We have four distinct irreducibles appearing in two different products equaling 6.

The failure is subtle: these irreducibles are not **prime** in the ring-theoretic sense. A prime p satisfies: if p divides ab, then p divides a or p divides b. In ℤ, every irreducible is prime — the two concepts coincide. In ℤ[√(-5)], they diverge. For example, 2 divides (1 + √(-5))(1 - √(-5)) = 6, but 2 does not divide either factor individually in this ring. This divergence between irreducible and prime is precisely what produces the two factorizations of 6. Unique factorization holds if and only if every irreducible is prime — equivalently, if and only if the ring is a **unique factorization domain (UFD)**.

The cure is the theory of **ideals**. Rather than factoring elements, we factor ideals, and ideal factorization is always unique in rings of algebraic integers. The ideal (2) in ℤ[√(-5)] factors as a product of two prime ideals, and the ideals (1 ± √(-5)) each factor further. When you recombine these ideal factorizations, the two seemingly different element-level factorizations emerge from the same underlying unique ideal factorization. This is why Dedekind invented ideals: they restore the uniqueness that element arithmetic alone cannot guarantee, and the **ideal class group** — measuring how far a ring is from being a UFD — becomes the central object for quantifying the failure.
