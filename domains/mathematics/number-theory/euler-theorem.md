---
id: euler-theorem
title: Euler's Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: fermat-little-theorem
  type: soft
- id: euler-totient-function
  type: hard
builds-toward:
- rsa-cryptography
tags:
- modular-arithmetic
- euler-phi
- group-theory
stage: advanced
status: draft
---

# Euler's Theorem

## Core Idea
If gcd(a, n) = 1, then a^φ(n) ≡ 1 (mod n), where φ is Euler's totient function. This generalizes Fermat's Little Theorem (where n = p gives φ(p) = p−1) and is essential for understanding RSA cryptography and computing modular exponentiation.

## Explainer

You already know from the totient function that φ(n) counts how many integers from 1 to n share no common factor with n — the **units modulo n**. Euler's theorem makes a powerful claim about what happens when you raise any such unit to the φ(n) power: you always land on 1. Think of this as a "reset" — repeated multiplication eventually cycles back to the identity.

To build intuition, consider n = 10 and a = 3. We have φ(10) = 4 (the units are 1, 3, 7, 9). Compute: 3¹ = 3, 3² = 9, 3³ = 27 ≡ 7 (mod 10), 3⁴ = 81 ≡ 1 (mod 10). The power cycle resets after exactly 4 steps. Euler's theorem guarantees this will happen for any a coprime to n — it might reset earlier (when the order divides φ(n)), but it always resets by step φ(n).

You may recognize a special case: if n = p is prime, then φ(p) = p − 1, and the theorem says a^(p−1) ≡ 1 (mod p) for any a not divisible by p. This is exactly **Fermat's Little Theorem**. Euler's theorem is the generalization that works for composite moduli too, which is why it has broader applications. The proof strategy is elegant: the set {a·1, a·3, a·7, a·9} (multiplying all units by a) is just a rearrangement of {1, 3, 7, 9} modulo n. Multiplying all elements on both sides yields a^φ(n) times the product of units ≡ that same product — cancel, and you get a^φ(n) ≡ 1.

The main application you'll encounter is **modular exponentiation for large numbers**. If you need to compute a^k mod n, you can reduce the exponent: a^k ≡ a^(k mod φ(n)) (mod n) when gcd(a, n) = 1. This is the mathematical engine behind RSA encryption, where message decryption requires computing m^d mod n for astronomically large numbers. Euler's theorem is what makes that computation tractable — without it, you could never decrypt quickly.
