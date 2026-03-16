---
id: euler-totient-function
title: Euler's Totient Function
domain: mathematics
course: number-theory
prerequisites:
- id: modular-arithmetic
  type: hard
- id: arithmetic-functions-and-multiplicativity
  type: soft
builds-toward:
- euler-theorem
- rsa-cryptography
tags:
- euler-phi
- coprime-integers
- multiplicative-function
stage: advanced
status: draft
---

# Euler's Totient Function

## Core Idea
Euler's totient function φ(n) counts the positive integers up to n that are coprime to n. This function is multiplicative with a closed form φ(n) = n∏_{p|n}(1−1/p), making it central to many number-theoretic algorithms, cryptographic systems, and applications of Fermat's Little Theorem.

## Explainer

You already know modular arithmetic: working with remainders, and the idea that two numbers are **coprime** when they share no common factor other than 1. Euler's totient function φ(n) puts a precise count on how many integers from 1 to n are coprime to n. For example, φ(9) asks: how many of 1, 2, 3, 4, 5, 6, 7, 8 share no factor with 9? Since 9 = 3², the only multiples of 3 in range are 3 and 6. That leaves 6 integers, so φ(9) = 6. For a prime p, every number from 1 to p−1 is coprime to p, giving φ(p) = p − 1 — a clean formula with major downstream consequences.

The deeper power of φ comes from its **multiplicative** structure: if gcd(m, n) = 1, then φ(mn) = φ(m)φ(n). This means you never have to count coprime integers directly for large numbers. Instead, factor n into prime powers, compute φ for each piece, and multiply. The **product formula** φ(n) = n∏_{p|n}(1 − 1/p) makes this mechanical. For n = 12 = 2² · 3: φ(12) = 12 · (1 − 1/2) · (1 − 1/3) = 12 · 1/2 · 2/3 = 4. Indeed, only 1, 5, 7, 11 are coprime to 12 — exactly four values.

The reason φ appears everywhere is **Euler's theorem**: if gcd(a, n) = 1, then a^φ(n) ≡ 1 (mod n). This generalizes Fermat's Little Theorem, which is the special case where n is prime. Euler's theorem says that when you repeatedly multiply a by itself in modular arithmetic, you return to 1 after exactly φ(n) steps. This periodicity is the mathematical engine behind RSA cryptography: encoding and decoding messages amounts to raising numbers to carefully chosen exponents modulo n, and φ(n) controls the cycle length that makes decryption work.

Think of φ(n) as measuring how "rich" the multiplicative structure of ℤ/nℤ is. The integers from 1 to n that are coprime to n are exactly the **units** of ℤ/nℤ — the elements with multiplicative inverses mod n. φ(n) is the size of this group of units. When n is prime, every nonzero element has an inverse, giving the fullest possible structure. Understanding φ(n) is therefore understanding the symmetry of modular arithmetic, and it sits at the intersection of elementary number theory, abstract algebra, and cryptography.
