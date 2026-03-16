---
id: sum-of-two-squares-theorem
title: Sum of Two Squares Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: quadratic-residues-and-legendre-symbol
  type: soft
- id: fundamental-theorem-of-arithmetic-rigorous
  type: soft
builds-toward:
- pythagorean-triples-parametrization
tags:
- representations
- quadratic-forms
- diophantine
stage: advanced
status: draft
---

# Sum of Two Squares Theorem

## Core Idea
A positive integer n can be expressed as a sum of two squares if and only if in the prime factorization of n, every prime of the form 4k+3 appears to an even power. This classical result elegantly connects arithmetic structure to geometric representations and is proved using Gaussian integers.

## Explainer

The question "which integers are sums of two squares?" sounds simple but has a surprisingly structured answer. Start by testing small cases: 1 = 1² + 0², 2 = 1² + 1², 4 = 2² + 0², 5 = 2² + 1², 9 = 3² + 0², 10 = 3² + 1². But 3, 6, 7, and 11 cannot be written this way no matter how you try. The pattern is not obvious from the examples alone, but it becomes crisp once you classify the primes.

Primes split into three types for this problem: 2 = 1² + 1² (works), primes p ≡ 1 (mod 4) like 5, 13, 17, 29 (always expressible as sums of two squares), and primes p ≡ 3 (mod 4) like 3, 7, 11, 19 (never expressible). The modular condition connects to your background in **quadratic residues**: −1 is a quadratic residue mod p exactly when p ≡ 1 (mod 4), and this is precisely the condition that makes p expressible as a² + b². The connection between "−1 has a square root mod p" and "p is a sum of two squares" is the heart of the theorem.

The cleanest proof uses **Gaussian integers**, the ring ℤ[i] = {a + bi : a, b ∈ ℤ}. In this ring, a² + b² = (a + bi)(a − bi) = |a + bi|². So asking whether p = a² + b² is the same as asking whether p factors nontrivially in ℤ[i]. Using the **fundamental theorem of arithmetic** for ℤ[i] (which is a Euclidean domain and hence a UFD), one can show: a prime p ≡ 1 (mod 4) factors as p = π · π̄ where π = a + bi is a Gaussian prime; a prime p ≡ 3 (mod 4) remains prime (inert) in ℤ[i] and cannot be written as a product of conjugates. This is why primes of the form 4k+3 are the obstruction.

For composite n, the full theorem follows from **Brahmagupta's identity**: (a² + b²)(c² + d²) = (ac − bd)² + (ad + bc)² = (ac + bd)² + (ad − bc)². This identity says the product of two sums of squares is again a sum of squares. So to check whether n is representable, you only need to check its prime factors: each prime p ≡ 1 (mod 4) contributes, 2 contributes, and a prime p ≡ 3 (mod 4) to an even power can be absorbed (since p² = p² + 0²), but a prime p ≡ 3 (mod 4) to an odd power blocks representation entirely. The theorem gives a complete, efficient criterion: factor n, check the exponents of the 4k+3 primes, and you immediately know whether n lands on the integer lattice as the squared distance from the origin.
