---
id: eulers-theorem
title: Euler's Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: fermats-little-theorem
  type: soft
- id: eulers-totient-function
  type: hard
builds-toward:
- cryptographic-applications-rsa
tags:
- euler-theorem
- totient
- modular-exponentiation
stage: advanced
status: draft
---

# Euler's Theorem

## Core Idea
If gcd(a,n) = 1, then a^φ(n) ≡ 1 (mod n). This generalizes Fermat's Little Theorem to any modulus and is fundamental to RSA encryption, where φ(pq) = (p-1)(q-1) plays a central role.

## How It's Best Learned
Prove via group theory: (Z/nZ)* has order φ(n). Verify with examples like a=3, n=7, computing φ(7)=6 and checking 3^6 ≡ 1 (mod 7).

## Common Misconceptions
Forgetting the gcd(a,n) = 1 requirement. Confusing φ(n) with p-1 in the general case.

## Explainer

Euler's theorem sits at the heart of modern cryptography, but its logic flows naturally from your prerequisite: Euler's totient function φ(n), which counts how many integers from 1 to n share no common factor with n. Those integers form a group under multiplication modulo n — call it (ℤ/nℤ)*. This group has exactly φ(n) elements, and that group structure is the key to everything.

Here's the argument in plain language. Pick any element a in (ℤ/nℤ)* — that is, any integer coprime to n. Multiplying a by itself repeatedly (mod n) cycles through a sequence: a, a², a³, ... This sequence must eventually repeat, because there are only finitely many residues. When it repeats, you've found a subgroup, and by Lagrange's theorem, the order of any subgroup divides the order of the whole group. Since the whole group has order φ(n), the sequence must satisfy a^φ(n) ≡ 1 (mod n).

The theorem generalizes Fermat's Little Theorem, which is the special case where n = p is prime. When n = p, φ(p) = p − 1, so a^(p−1) ≡ 1 (mod p). Euler's theorem works for any modulus. For example, φ(10) = 4 (the coprimes to 10 are 1, 3, 7, 9), so 3^4 = 81 ≡ 1 (mod 10). Check: 81 = 8×10 + 1. ✓

The gcd(a, n) = 1 condition is not optional. If a shares a factor with n, then a is not in the group (ℤ/nℤ)* at all — the argument collapses. For instance, gcd(2, 10) = 2, and 2^4 = 16 ≡ 6 (mod 10), not 1. The coprimality condition defines exactly the elements for which the theorem holds. In RSA encryption, this is precisely why n = pq is chosen with φ(pq) = (p−1)(q−1): it guarantees that encryption and decryption are inverses modulo φ(n), making the entire scheme work.
