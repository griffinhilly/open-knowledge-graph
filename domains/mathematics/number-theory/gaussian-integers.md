---
id: gaussian-integers
title: Gaussian Integers
domain: mathematics
course: number-theory
prerequisites:
- id: algebraic-integers
  type: hard
builds-toward:
- norm-algebraic-number-fields
tags:
- gaussian-integers
- complex-integers
- unique-factorization
stage: advanced
status: draft
---

# Gaussian Integers

## Core Idea
The Gaussian integers ℤ[i] = {a + bi : a,b ∈ ℤ} form a unique factorization domain with norm N(a+bi) = a^2 + b^2. Gaussian primes include rational primes p ≡ 3 (mod 4) and factors a±bi of primes p ≡ 1 (mod 4), elegantly explaining two-square representations.

## Explainer

From algebraic integers, you know that ℤ[i] is the ring of integers of ℚ(i) — the "integral" elements of the field of Gaussian rationals. The Gaussian integers look like the ordinary integers ℤ but spread out over the complex plane on a square grid. The unit circle in ℤ[i] contains only four elements — 1, −1, i, −i — corresponding to the four units. Just as in ℤ, units are the invertible elements, and factorization is only unique "up to units."

The key to factorization in ℤ[i] is the **norm**: N(a + bi) = a² + b² = (a + bi)(a − bi). The crucial property is multiplicativity — N(αβ) = N(α)N(β). This turns the problem of factorization in ℤ[i] into a problem about ordinary integers, because if α factors as βγ then N(α) = N(β)N(γ) in ℤ. In particular, an element with prime norm must be a **Gaussian prime** (irreducible in ℤ[i]). For example, 2 + i has norm 5, which is a rational prime, so 2 + i is a Gaussian prime.

The fate of rational primes in ℤ[i] falls into three cases that depend on their residue mod 4. A prime **p ≡ 3 (mod 4)** remains prime — it is still irreducible in ℤ[i]. Geometrically, there is no way to write p = a² + b² as a sum of two squares when p ≡ 3 (mod 4). A prime **p ≡ 1 (mod 4)** splits: it factors as p = (a + bi)(a − bi) where a² + b² = p — and Fermat's theorem on sums of squares guarantees this factorization exists. The prime **p = 2** is special: 2 = −i(1 + i)², so 2 ramifies (its Gaussian factor repeats). This tripartite classification is the prototype for how primes "split, remain inert, or ramify" in general number fields.

The payoff of all this machinery is **Fermat's two-square theorem**: a positive integer n is expressible as a sum of two squares n = a² + b² if and only if every prime factor of n of the form 4k + 3 appears to an even power. The proof flows directly from unique factorization in ℤ[i]. Writing n as a norm N(a + bi) = a² + b² is exactly asking for n to factor in ℤ[i], and unique factorization tells you exactly when that is possible. A 2,000-year-old theorem about sums of squares becomes a routine consequence of the algebraic structure.

The reason ℤ[i] is particularly tractable is that it is a **Euclidean domain**: you can perform division with remainder using the norm as the "size" function. Specifically, given α, β ∈ ℤ[i] with β ≠ 0, you can always find γ, ρ ∈ ℤ[i] with α = βγ + ρ and N(ρ) < N(β). This geometric fact — that every complex number lies within distance 1/√2 < 1 of some Gaussian integer — is the reason Euclid's algorithm works in ℤ[i], and it is what ultimately guarantees unique factorization. Not every ring of algebraic integers enjoys this property, making ℤ[i] an especially clean model to master before tackling more complex number fields.
