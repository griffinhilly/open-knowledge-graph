---
id: fundamental-theorem-of-arithmetic-rigorous
title: Fundamental Theorem of Arithmetic (Rigorous)
domain: mathematics
course: number-theory
prerequisites:
- id: fundamental-theorem-of-arithmetic
  type: hard
- id: euclidean-algorithm
  type: soft
builds-toward:
- arithmetic-functions-and-multiplicativity
- failure-of-unique-factorization
tags:
- unique-factorization
- prime-factorization
- integers
stage: advanced
status: draft
---

# Fundamental Theorem of Arithmetic (Rigorous)

## Core Idea
Every integer greater than 1 either is prime or is uniquely expressible as a product of primes, up to order. This rigorous treatment proves both existence (by strong induction) and uniqueness (via Euclid's lemma) and explores why it holds in ℤ but fails in other number systems.

## How It's Best Learned
Prove existence and uniqueness separately using strong induction and Euclid's lemma. Compare with domains where unique factorization fails, such as ℤ[√5] where 6 = 2·3 = (1+√5)(1−√5).

## Common Misconceptions
Unique factorization is not universal across all algebraic structures; it requires special conditions. The unit 1 is not prime and must be handled separately in the uniqueness statement.

## Explainer

You already know from the introductory treatment that every integer greater than 1 can be broken into prime factors, and that 60 = 2² · 3 · 5 regardless of how you start factoring it. The rigorous version asks: *why* is this true? The proof has two completely separate jobs — proving a prime factorization **exists** and proving it is **unique** — and each requires a distinct technique.

**Existence** is proved by **strong induction**. The base case is 2, which is already prime. For the inductive step, assume every integer from 2 to n−1 is either prime or has a prime factorization. Now consider n: if n is prime, we are done. If n is composite, then n = a · b with 2 ≤ a, b < n. By the inductive hypothesis, both a and b have prime factorizations. Multiplying those factorizations together gives a prime factorization of n. Notice that strong induction — where you assume the result holds for *all* smaller values, not just the immediate predecessor — is what makes this work. The Euclidean algorithm from your prerequisites isn't needed for existence, but it is the key to uniqueness.

**Uniqueness** rests on **Euclid's Lemma**: if a prime p divides a product ab, then p | a or p | b (or both). This lemma is provable using the Euclidean algorithm through Bézout's identity. Here is where it matters: if two different prime factorizations of n existed, say p₁p₂···pₖ = q₁q₂···qₘ, then p₁ divides the right side. By repeated application of Euclid's Lemma, p₁ must equal some qⱼ. Cancel both and repeat — the two factorizations must be identical up to order.

The theorem's limitations are equally important to understand. Consider the ring ℤ[√−5], which consists of numbers of the form a + b√−5. In this ring, 6 = 2 · 3 = (1 + √−5)(1 − √−5), and one can verify that 2, 3, 1+√−5, and 1−√−5 are all **irreducible** (cannot be factored further in the ring) yet 2 does not divide either factor on the right — Euclid's Lemma fails. The reason is that irreducible does not imply prime in this ring. The Fundamental Theorem holds in ℤ precisely because every irreducible integer *is* prime, which is itself a consequence of the Euclidean algorithm. Rings where unique factorization holds are called **unique factorization domains (UFDs)**; the existence of ℤ[√−5] shows that not every ring deserves this title.
