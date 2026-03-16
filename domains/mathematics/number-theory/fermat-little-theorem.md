---
id: fermat-little-theorem
title: Fermat's Little Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: modular-arithmetic
  type: hard
- id: group-definition-and-examples
  type: soft
builds-toward:
- euler-theorem
- rsa-cryptography
tags:
- modular-arithmetic
- group-theory
- primes
- fermat
stage: advanced
status: draft
---

# Fermat's Little Theorem

## Core Idea
If p is prime and gcd(a, p) = 1, then a^(p−1) ≡ 1 (mod p). This theorem follows from Lagrange's theorem applied to the multiplicative group (ℤ/pℤ)* and forms the basis for Fermat primality tests and many cryptographic algorithms.

## How It's Best Learned
Derive it from group theory using the multiplicative group mod p. Verify with numerical examples (e.g., 2^4 ≡ 1 (mod 5)). Apply it to compute large powers modulo p efficiently.

## Common Misconceptions
The converse is false: a^(n−1) ≡ 1 (mod n) does not imply n is prime (Carmichael numbers counterexample: 561 = 3·11·17). The condition gcd(a, p) = 1 is essential; the theorem fails when a is divisible by p.

## Explainer

From your work with modular arithmetic, you know that integers mod p form a system where addition and multiplication wrap around. When p is prime, something special happens: every nonzero element has a multiplicative inverse mod p. This means the nonzero residues {1, 2, ..., p−1} form a **multiplicative group** under multiplication mod p, denoted (ℤ/pℤ)*. Its size — the **order** of the group — is p−1.

Fermat's Little Theorem follows almost immediately from one key fact about groups: for any element a in a finite group of order n, raising a to the power n gives the identity. In (ℤ/pℤ)*, the identity is 1 and the group has order p−1, so a^(p−1) ≡ 1 (mod p) for any a not divisible by p. If you haven't seen the group-theoretic proof yet, there's a more elementary argument: list the p−1 nonzero residues, then consider the list multiplied by a (mod p). Because a is coprime to p, the new list is a permutation of the old one. So the product of both lists must be equal mod p — the a^(p−1) factor cancels against the same product, leaving a^(p−1) ≡ 1.

A useful corollary restates the theorem as a^p ≡ a (mod p) for *all* integers a (including multiples of p, where both sides are 0). This version is often more convenient in proofs. The practical power of the theorem is **modular exponentiation**: to compute 7^1000 (mod 13), note that 13 is prime and 7 is coprime to 13, so 7^12 ≡ 1 (mod 13). Write 1000 = 83 × 12 + 4, so 7^1000 = (7^12)^83 · 7^4 ≡ 1^83 · 7^4 ≡ 2401 ≡ 9 (mod 13). A computation that seemed impossible becomes routine.

The one trap to watch: the converse fails. If a^(n−1) ≡ 1 (mod n), you cannot conclude n is prime. **Carmichael numbers** like 561 = 3 · 11 · 17 satisfy this equation for all a coprime to n, even though they are composite. This is why Fermat's test is only a *probable* primality check — it identifies non-primes efficiently (if the equation fails, n is definitely composite), but passing the test is not a guarantee of primality. This gap is closed by more sophisticated tests like Miller–Rabin, which also underpins the RSA cryptographic system you will encounter next.
