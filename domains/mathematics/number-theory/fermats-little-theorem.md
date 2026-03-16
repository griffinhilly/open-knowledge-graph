---
id: fermats-little-theorem
title: Fermat's Little Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: congruence-properties
  type: hard
- id: group-definition-and-examples
  type: soft
builds-toward:
- eulers-theorem
- cryptographic-applications-rsa
tags:
- fermats-little-theorem
- prime-powers
- modular-exponentiation
stage: advanced
status: draft
---

# Fermat's Little Theorem

## Core Idea
If p is prime and gcd(a,p) = 1, then a^(p-1) ≡ 1 (mod p). This cornerstone result characterizes the exponent structure of multiplicative groups mod p and enables fast modular exponentiation in cryptography.

## Explainer

You already know from congruence properties that modular arithmetic is self-consistent: if a ≡ b (mod p), then a^k ≡ b^k (mod p). Fermat's Little Theorem takes this arithmetic into the multiplicative structure: if p is prime and a is not divisible by p, then a^(p-1) ≡ 1 (mod p). The key intuition comes from examining the set of multiples {a, 2a, 3a, ..., (p-1)a} reduced mod p. Because p is prime and gcd(a, p) = 1, these p-1 values are all distinct and nonzero — they produce the set {1, 2, ..., p-1} in some scrambled order. So their product equals the product of all nonzero residues: a · 2a · 3a · ... · (p-1)a ≡ 1 · 2 · 3 · ... · (p-1) (mod p). Factoring out a^(p-1) from the left yields a^(p-1) · (p-1)! ≡ (p-1)! (mod p). Since (p-1)! is nonzero mod p, cancel it to get a^(p-1) ≡ 1 (mod p).

The theorem has a tidy corollary: for any integer a (not just those coprime to p), a^p ≡ a (mod p). This form is often more convenient because no divisibility check is needed. Both forms appear throughout number theory and in computing.

The practical power is enormous. **Modular exponentiation** — the engine of RSA encryption — relies on reducing large exponents mod (p-1). For example, to compute 7^100 mod 13: since 13 is prime, 7^12 ≡ 1 (mod 13). Write 100 = 8·12 + 4, so 7^100 = (7^12)^8 · 7^4 ≡ 1^8 · 7^4 ≡ 7^4 ≡ 2401 ≡ 9 (mod 13). Without Fermat's Little Theorem, this computation over cryptographic-scale numbers — hundreds of digits long — would be infeasible.

If you have encountered group theory, the result has a clean restatement: the nonzero residues mod p form a **multiplicative group** of order p-1. By Lagrange's theorem, every element's order divides the group order, so a^(p-1) = 1 for all elements a. Fermat's Little Theorem is Lagrange's theorem specialized to the group (Z/pZ)*. This group-theoretic view also explains why the exponent is p-1 specifically: it equals the size of the group, not an arbitrary bound.
