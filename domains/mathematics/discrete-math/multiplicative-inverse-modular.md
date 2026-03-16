---
id: multiplicative-inverse-modular
title: Multiplicative Inverses in Modular Arithmetic
domain: mathematics
course: discrete-math
prerequisites:
- id: modular-arithmetic
  type: hard
- id: euclidean-algorithm
  type: hard
builds-toward:
- cryptographic-applications-rsa
tags:
- number-theory
- modular-arithmetic
- inverses
stage: formal-systems
status: draft
---

# Multiplicative Inverses in Modular Arithmetic

## Core Idea
An integer a has a multiplicative inverse modulo n (written a⁻¹) if aa⁻¹ ≡ 1 (mod n). This exists if and only if gcd(a,n)=1. The extended Euclidean algorithm efficiently computes multiplicative inverses and is crucial for solving congruences and RSA cryptography.

## Explainer

In ordinary arithmetic, every nonzero number has a multiplicative inverse: 3 × (1/3) = 1, 7 × (1/7) = 1. But in modular arithmetic, there are no fractions. So what replaces 1/a? A **multiplicative inverse mod n** is an integer b such that a·b ≡ 1 (mod n) — meaning a·b leaves remainder 1 when divided by n. For example, the inverse of 3 mod 7 is 5, because 3·5 = 15 = 2·7 + 1 ≡ 1 (mod 7). Once you have this, you can "divide by 3" in mod 7 arithmetic by multiplying by 5 instead.

The key question is: when does this inverse exist? Your prerequisite on modular arithmetic introduced the idea that working mod n partitions integers into residue classes. The inverse of a mod n exists if and only if gcd(a, n) = 1 — that is, a and n share no common factor. Intuitively: if gcd(a,n) = d > 1, then a·b is always divisible by d for any b, so a·b can never leave remainder 1 (which isn't divisible by d). But if gcd(a,n) = 1, then a and n are "independent" enough that some combination a·b hits exactly 1 mod n.

To actually find the inverse, you use the **extended Euclidean algorithm**, which you already know computes gcd(a,n). Recall that the extended version doesn't just compute gcd(a,n) = 1 — it also finds integers s and t such that as + nt = 1 (Bézout's identity). Taking this equation mod n: as + nt ≡ as ≡ 1 (mod n), since nt ≡ 0. So s is the inverse of a mod n. For example, to invert 3 mod 7: the extended Euclidean algorithm finds 3·5 + 7·(−2) = 15 − 14 = 1, giving s = 5. The inverse is 5.

This tool is essential for solving **linear congruences** of the form ax ≡ b (mod n). When gcd(a,n)=1, the unique solution is x ≡ a⁻¹·b (mod n) — you just multiply both sides by the inverse. When gcd(a,n) > 1, solutions exist only if gcd(a,n) divides b, and there are multiple solutions. Multiplicative inverses also sit at the heart of RSA encryption: the decryption exponent d is the modular inverse of the encryption exponent e modulo φ(n), computed via the extended Euclidean algorithm on numbers with hundreds of digits.
