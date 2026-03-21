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

## Questions

```yaml
- question: "You compute the Jacobi symbol (a/n) = 1, where n = pq is a product of two distinct odd primes. What can you conclude about a?"
  type: multiple-choice
  options:
    - "a is definitely a quadratic residue mod n"
    - "a is definitely not a quadratic residue mod n"
    - "a may or may not be a quadratic residue mod n — Jacobi = 1 gives no guarantee when n is composite"
    - "The computation is invalid because n is not prime"
  answer: 2
  explanation: "This is the central warning about the Jacobi symbol. When n is composite, (a/n) = 1 does not imply that a is a quadratic residue mod n. It's possible that (a/p) = −1 and (a/q) = −1 at each prime factor, so the product (−1)(−1) = 1, even though a is not a square mod pq. The implication runs only one way: (a/n) = −1 guarantees non-residuosity, but (a/n) = 1 is inconclusive. Option A is the classic error."

- question: "What is the primary computational advantage of the Jacobi symbol over directly evaluating Legendre symbols at each prime factor of n?"
  type: multiple-choice
  options:
    - "It produces a more accurate residuosity test than any individual Legendre symbol"
    - "It can be computed via a Euclidean-algorithm-like procedure without factoring n"
    - "It avoids the need for quadratic reciprocity in calculations"
    - "It works for even moduli, unlike the Legendre symbol"
  answer: 1
  explanation: "The whole point of the Jacobi symbol is efficiency: you can evaluate (a/n) using repeated application of quadratic reciprocity and supplementary rules — reducing to smaller symbols until a base case — without ever finding the prime factors of n. Factoring a large n is expensive (computationally hard); computing the Jacobi symbol is fast. This is why it appears in the Solovay–Strassen primality test."

- question: "For composite n, the Jacobi symbol (a/n) = 1 guarantees that a is a quadratic residue modulo n."
  type: true-false
  answer: false
  explanation: "This is false and is the central misconception to avoid. When n is prime, (a/n) = 1 does imply a is a QR. But when n is composite, (a/n) is defined as the product of Legendre symbols at each prime power factor. Those Legendre symbols could each be −1, and their product would still be 1, even though a is not a quadratic residue mod n. The Jacobi symbol can only certify non-residuosity: (a/n) = −1 is a conclusive negative."

- question: "If the Jacobi symbol (a/n) = −1, then a is not a quadratic residue modulo n."
  type: true-false
  answer: true
  explanation: "This is the one-directional guarantee the Jacobi symbol provides. If a were a quadratic residue mod n, then a would be a QR at every prime power factor of n, so each Legendre symbol would equal 1, and their product would be 1. A product of values in {1, −1} equals −1 only if an odd number of factors equal −1 — which cannot happen if all factors are 1. Therefore (a/n) = −1 conclusively rules out quadratic residuosity."

- question: "Explain why the Jacobi symbol cannot serve as a direct quadratic residuosity test for composite moduli, even though it satisfies quadratic reciprocity."
  type: short-answer
  answer: "The Jacobi symbol (a/n) is defined multiplicatively as the product of Legendre symbols at each prime factor of n. When (a/p) = −1 for two different prime factors p and q, the product (a/p)(a/q) = (−1)(−1) = 1, so (a/pq) = 1 — but a is not a square mod pq. The Jacobi symbol 'loses information' about individual prime factors by multiplying their values, so a result of 1 is consistent with both residuosity and non-residuosity."
  explanation: "This asymmetry is inherent to the multiplicative definition. The Legendre symbol at a prime directly encodes residuosity; the Jacobi symbol at a composite aggregates multiple Legendre symbols and the signs can cancel. The Solovay–Strassen test exploits this: when (a/n) disagrees with a^((n−1)/2) mod n, n must be composite — the Jacobi symbol's failure to certify residuosity becomes a compositeness certificate."
```

## Explainer

Recall that the **Legendre symbol** (a/p) for an odd prime p answers a yes/no question: is a a quadratic residue mod p? It equals 1 if a ≡ x² (mod p) has a solution, −1 if not, and 0 if p|a. The trouble is that many algorithms want to reason about quadratic residuosity modulo a large number n that may not be prime — and factoring n just to evaluate a Legendre symbol at each prime factor is expensive. The **Jacobi symbol** solves the computational bottleneck by generalizing the definition multiplicatively.

If n = p₁^e₁ · p₂^e₂ · · · pₖ^eₖ is the prime factorization of any positive odd integer, the Jacobi symbol is defined as the product (a/n) = (a/p₁)^e₁ · (a/p₂)^e₂ · · · (a/pₖ)^eₖ, where each factor is a Legendre symbol. The key insight is that this product can be computed very efficiently — using an analogue of the Euclidean algorithm — without ever finding the prime factors of n. The computation looks like repeated application of the **quadratic reciprocity law** and a few supplementary rules, reducing (a/n) to smaller and smaller Jacobi symbols until you reach a base case.

The critical warning is that the Jacobi symbol is **not** a quadratic residuosity test for composite moduli. When n is prime, (a/n) = 1 means a is a quadratic residue, and (a/n) = −1 means it is not. But when n is composite, (a/n) = 1 does not guarantee that a is a quadratic residue mod n — the Legendre symbols at different prime factors could each be −1, and their product would still be 1. For example, if (a/p) = −1 and (a/q) = −1, then (a/pq) = (−1)(−1) = 1, yet a might not be a square mod pq. The implication runs only one way: if (a/n) = −1, then a is definitely not a quadratic residue mod n.

Despite this limitation, the Jacobi symbol is enormously useful. It is the key ingredient in **Solovay–Strassen primality testing**, where checking (a/n) ≡ a^((n−1)/2) (mod n) for random a quickly certifies compositeness when they disagree. It also enables efficient algorithms for computing square roots mod n in cryptographic contexts. Think of the Jacobi symbol as a fast-to-compute proxy for quadratic reciprocity: it preserves the algebraic laws of the Legendre symbol (multiplicativity, reciprocity) while discarding the exact residuosity meaning — a trade that is computationally cheap and theoretically indispensable.
