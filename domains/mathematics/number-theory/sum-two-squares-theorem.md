---
id: sum-two-squares-theorem
title: Sum of Two Squares Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: fundamental-theorem-arithmetic-rigorous
  type: hard
tags:
- sum-of-squares
- diophantine
- representation
stage: advanced
status: draft
---

# Sum of Two Squares Theorem

## Core Idea
An integer n is representable as n = a^2 + b^2 iff in its prime factorization, every prime p ≡ 3 (mod 4) appears to an even power. This theorem connects number theory and geometry; Gaussian integers provide an elegant proof.

## Explainer

You already know from the fundamental theorem of arithmetic that every positive integer has a unique factorization into primes. The sum of two squares theorem gives a precise answer to the question: which integers live on the integer lattice of a circle? That is, for which n does the equation n = a² + b² have an integer solution? The answer depends entirely on the prime factorization of n, and specifically on how primes behave modulo 4.

Start with primes. The prime 2 = 1² + 1² works. For odd primes, there are only two residues mod 4: either p ≡ 1 (mod 4) or p ≡ 3 (mod 4). It turns out that every prime p ≡ 1 (mod 4) is representable as a sum of two squares — for example, 5 = 1² + 2², 13 = 2² + 3², 17 = 1² + 4² — while no prime p ≡ 3 (mod 4) is representable. You can verify the latter: modulo 4, squares are always 0 or 1, so a² + b² is congruent to 0, 1, or 2 (mod 4) — never 3. This means primes like 3, 7, 11, 19 can never be written as a sum of two squares.

The elegant proof uses the **Gaussian integers** ℤ[i] = {a + bi : a, b ∈ ℤ}. The key insight is that a² + b² = (a + bi)(a − bi) = |a + bi|². So asking whether n is a sum of two squares is the same as asking whether n is the norm of a Gaussian integer. Primes p ≡ 3 (mod 4) remain **inert** (prime) in ℤ[i] — they don't factor further. Primes p ≡ 1 (mod 4) **split**: p = π · π̄ for a Gaussian prime π = a + bi with |π|² = p. This is why such primes are sums of two squares. The prime 2 **ramifies**: 2 = −i(1+i)².

To handle composite n, you need a multiplicative identity: if m and n are both sums of two squares, so is mn. This follows from the Gaussian integer norm being multiplicative: N(αβ) = N(α)N(β). It means you can assemble the representation of n from those of its prime factors. The constraint "every prime p ≡ 3 (mod 4) appears to an even power" comes from the fact that such primes must pair up — each contributes a factor of p to the norm, and two inert primes p · p = p² = (p + 0i)(p − 0i) is representable. The theorem is one of the cleanest examples of how algebraic structure in an extended ring (ℤ[i]) illuminates purely arithmetic questions about ℤ.
