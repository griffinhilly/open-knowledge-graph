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

## Questions

```yaml
- question: "What is φ(12)?"
  type: multiple-choice
  options:
    - "2"
    - "4"
    - "6"
    - "10"
  answer: 1
  explanation: "Using the product formula: 12 = 2² · 3, so φ(12) = 12 · (1 − 1/2) · (1 − 1/3) = 12 · 1/2 · 2/3 = 4. You can verify by listing: of the integers 1–11, only 1, 5, 7, and 11 share no factor with 12. A common error is φ(12) = 6 (confusing with φ(9) or forgetting that multiples of both 2 and 3 are excluded), but the product formula handles this systematically."

- question: "For a prime p, what is φ(p²)?"
  type: multiple-choice
  options:
    - "p − 1"
    - "p² − 1"
    - "p(p − 1)"
    - "p²"
  answer: 2
  explanation: "Using the product formula: φ(p²) = p² · (1 − 1/p) = p² − p = p(p − 1). Alternatively, the integers from 1 to p² that are NOT coprime to p² are exactly the multiples of p: p, 2p, 3p, …, p·p — there are p of them, leaving p² − p. Option A, p − 1, is φ(p), not φ(p²); a common confusion between the prime and its square. The multiplicativity formula φ(p^k) = p^k − p^(k−1) generalizes this."

- question: "The formula φ(mn) = φ(m) · φ(n) holds for all positive integers m and n."
  type: true-false
  answer: false
  explanation: "The multiplicativity formula φ(mn) = φ(m)φ(n) only holds when gcd(m, n) = 1. For example, φ(4) = 2 and φ(2) = 1, but 4 = 2 · 2 and gcd(2,2) = 2 ≠ 1, so φ(4) ≠ φ(2)φ(2) = 1. Correctly, φ(4) = 2. This condition is essential: φ is a multiplicative function in the number-theoretic sense, meaning multiplicativity holds only for coprime inputs."

- question: "The integers from 1 to n that are coprime to n are exactly the invertible elements (units) of the ring ℤ/nℤ."
  type: true-false
  answer: true
  explanation: "An integer a has a multiplicative inverse mod n — i.e., there exists b with ab ≡ 1 (mod n) — if and only if gcd(a, n) = 1. So the coprime residues are precisely the units of ℤ/nℤ, and φ(n) is the size of the multiplicative group (ℤ/nℤ)×. This is why φ(n) appears in Euler's theorem: a^φ(n) ≡ 1 (mod n) for gcd(a,n) = 1 is simply the statement that every unit has order dividing the group size."

- question: "Why does Euler's theorem require gcd(a, n) = 1? What goes wrong — concretely — if a and n share a common factor?"
  type: short-answer
  answer: "If gcd(a, n) = d > 1, then a is not a unit in ℤ/nℤ — it has no multiplicative inverse. Powers of a mod n cannot cycle back to 1 because a unit multiplied by a non-unit never yields a unit. For example, a = 2, n = 4: powers of 2 mod 4 are 2, 0, 0, 0, … — they never reach 1. The group structure underlying Euler's theorem applies only to the units (ℤ/nℤ)×, and a ∉ (ℤ/nℤ)× when gcd(a,n) > 1."
  explanation: "This condition is not just a technical nicety — it is the heart of why RSA works. In RSA, messages are encoded as integers a with gcd(a, n) = 1 (guaranteed by choosing large prime factors). Encryption raises a to an exponent e, and decryption uses Euler's theorem to find the inverse exponent d such that ed ≡ 1 (mod φ(n)), recovering a. If a shared a factor with n, the cycle structure breaks and decryption fails — which is also why RSA keys use large primes, making such collisions astronomically unlikely."
```

## Explainer

You already know modular arithmetic: working with remainders, and the idea that two numbers are **coprime** when they share no common factor other than 1. Euler's totient function φ(n) puts a precise count on how many integers from 1 to n are coprime to n. For example, φ(9) asks: how many of 1, 2, 3, 4, 5, 6, 7, 8 share no factor with 9? Since 9 = 3², the only multiples of 3 in range are 3 and 6. That leaves 6 integers, so φ(9) = 6. For a prime p, every number from 1 to p−1 is coprime to p, giving φ(p) = p − 1 — a clean formula with major downstream consequences.

The deeper power of φ comes from its **multiplicative** structure: if gcd(m, n) = 1, then φ(mn) = φ(m)φ(n). This means you never have to count coprime integers directly for large numbers. Instead, factor n into prime powers, compute φ for each piece, and multiply. The **product formula** φ(n) = n∏_{p|n}(1 − 1/p) makes this mechanical. For n = 12 = 2² · 3: φ(12) = 12 · (1 − 1/2) · (1 − 1/3) = 12 · 1/2 · 2/3 = 4. Indeed, only 1, 5, 7, 11 are coprime to 12 — exactly four values.

The reason φ appears everywhere is **Euler's theorem**: if gcd(a, n) = 1, then a^φ(n) ≡ 1 (mod n). This generalizes Fermat's Little Theorem, which is the special case where n is prime. Euler's theorem says that when you repeatedly multiply a by itself in modular arithmetic, you return to 1 after exactly φ(n) steps. This periodicity is the mathematical engine behind RSA cryptography: encoding and decoding messages amounts to raising numbers to carefully chosen exponents modulo n, and φ(n) controls the cycle length that makes decryption work.

Think of φ(n) as measuring how "rich" the multiplicative structure of ℤ/nℤ is. The integers from 1 to n that are coprime to n are exactly the **units** of ℤ/nℤ — the elements with multiplicative inverses mod n. φ(n) is the size of this group of units. When n is prime, every nonzero element has an inverse, giving the fullest possible structure. Understanding φ(n) is therefore understanding the symmetry of modular arithmetic, and it sits at the intersection of elementary number theory, abstract algebra, and cryptography.
