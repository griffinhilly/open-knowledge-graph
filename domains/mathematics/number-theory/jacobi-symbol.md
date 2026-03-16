---
id: jacobi-symbol
title: The Jacobi Symbol
domain: mathematics
course: number-theory
prerequisites:
- id: law-quadratic-reciprocity
  type: hard
tags:
- jacobi-symbol
- quadratic-reciprocity
- composite-moduli
stage: advanced
status: draft
---

# The Jacobi Symbol

## Core Idea
The Jacobi symbol (a/n) extends the Legendre symbol to composite odd n via the Chinese Remainder Theorem: (a/n) = ∏(a/p_i)^(e_i) for n = ∏p_i^(e_i). While not a direct residuosity test, it satisfies quadratic reciprocity and is efficient to compute.

## Explainer

Recall that the **Legendre symbol** (a/p) for an odd prime p answers a yes/no question: is a a quadratic residue mod p? It equals 1 if a ≡ x² (mod p) has a solution, −1 if not, and 0 if p|a. The trouble is that many algorithms want to reason about quadratic residuosity modulo a large number n that may not be prime — and factoring n just to evaluate a Legendre symbol at each prime factor is expensive. The **Jacobi symbol** solves the computational bottleneck by generalizing the definition multiplicatively.

If n = p₁^e₁ · p₂^e₂ · · · pₖ^eₖ is the prime factorization of any positive odd integer, the Jacobi symbol is defined as the product (a/n) = (a/p₁)^e₁ · (a/p₂)^e₂ · · · (a/pₖ)^eₖ, where each factor is a Legendre symbol. The key insight is that this product can be computed very efficiently — using an analogue of the Euclidean algorithm — without ever finding the prime factors of n. The computation looks like repeated application of the **quadratic reciprocity law** and a few supplementary rules, reducing (a/n) to smaller and smaller Jacobi symbols until you reach a base case.

The critical warning is that the Jacobi symbol is **not** a quadratic residuosity test for composite moduli. When n is prime, (a/n) = 1 means a is a quadratic residue, and (a/n) = −1 means it is not. But when n is composite, (a/n) = 1 does not guarantee that a is a quadratic residue mod n — the Legendre symbols at different prime factors could each be −1, and their product would still be 1. For example, if (a/p) = −1 and (a/q) = −1, then (a/pq) = (−1)(−1) = 1, yet a might not be a square mod pq. The implication runs only one way: if (a/n) = −1, then a is definitely not a quadratic residue mod n.

Despite this limitation, the Jacobi symbol is enormously useful. It is the key ingredient in **Solovay–Strassen primality testing**, where checking (a/n) ≡ a^((n−1)/2) (mod n) for random a quickly certifies compositeness when they disagree. It also enables efficient algorithms for computing square roots mod n in cryptographic contexts. Think of the Jacobi symbol as a fast-to-compute proxy for quadratic reciprocity: it preserves the algebraic laws of the Legendre symbol (multiplicativity, reciprocity) while discarding the exact residuosity meaning — a trade that is computationally cheap and theoretically indispensable.
