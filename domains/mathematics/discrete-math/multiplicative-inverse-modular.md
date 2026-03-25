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
- id: divisors-and-divisor-sums
  type: soft
builds-toward:
- cryptographic-applications-rsa
tags:
- number-theory
- modular-arithmetic
- inverses
stage: formal-systems
status: validated
---
# Multiplicative Inverses in Modular Arithmetic

## Core Idea
An integer a has a multiplicative inverse modulo n (written a⁻¹) if aa⁻¹ ≡ 1 (mod n). This exists if and only if gcd(a,n)=1. The extended Euclidean algorithm efficiently computes multiplicative inverses and is crucial for solving congruences and RSA cryptography.

## Questions

```yaml
- question: "Does 4 have a multiplicative inverse modulo 6?"
  type: multiple-choice
  options:
    - "Yes — it is 2, since 4 · 2 = 8 ≡ 2 (mod 6)"
    - "Yes — it is 4, since 4 · 4 = 16 ≡ 4 (mod 6)"
    - "No — because gcd(4, 6) = 2 ≠ 1, so no inverse exists"
    - "Yes — every nonzero residue has an inverse in any modular system"
  answer: 2
  explanation: "A multiplicative inverse of a mod n exists if and only if gcd(a, n) = 1. Here gcd(4, 6) = 2, so no integer b can satisfy 4b ≡ 1 (mod 6). The intuition: 4b is always even, and 1 is odd, so 4b − 1 is always odd and can never be divisible by 6. Option D is the classic misconception — it confuses modular arithmetic with fields like the real numbers where every nonzero element has an inverse."

- question: "The extended Euclidean algorithm yields 3 · 5 + 7 · (−2) = 1. Using this, what is the solution to 3x ≡ 5 (mod 7)?"
  type: multiple-choice
  options:
    - "x ≡ 2 (mod 7)"
    - "x ≡ 4 (mod 7)"
    - "x ≡ 5 (mod 7)"
    - "x ≡ 6 (mod 7)"
  answer: 1
  explanation: "From the equation 3 · 5 + 7 · (−2) = 1, taking both sides mod 7 gives 3 · 5 ≡ 1 (mod 7), so 3⁻¹ ≡ 5 (mod 7). To solve 3x ≡ 5 (mod 7), multiply both sides by 3⁻¹ = 5: x ≡ 5 · 5 = 25 ≡ 4 (mod 7). Verification: 3 · 4 = 12 = 7 + 5 ≡ 5 (mod 7). ✓ A common error is to use s and t from Bézout's identity without carefully identifying which coefficient goes with which modulus."

- question: "Every nonzero integer has a multiplicative inverse modulo any positive integer n."
  type: true-false
  answer: false
  explanation: "This is false. The inverse of a mod n exists if and only if gcd(a, n) = 1. For example, 6 has no inverse mod 9, because gcd(6, 9) = 3 ≠ 1. An inverse exists for every nonzero element only when n is prime — then gcd(a, n) = 1 for all 1 ≤ a < n, giving every nonzero residue an inverse. This is one of the properties that makes prime moduli special in cryptography."

- question: "If gcd(a, n) = 1, the extended Euclidean algorithm guarantees that integers s and t exist with as + nt = 1, and s is the multiplicative inverse of a modulo n."
  type: true-false
  answer: true
  explanation: "This is Bézout's identity: whenever gcd(a, n) = 1, the extended Euclidean algorithm finds s and t satisfying as + nt = 1. Taking this equation mod n eliminates the nt term (since nt ≡ 0 mod n), leaving as ≡ 1 (mod n). So s is exactly the multiplicative inverse of a modulo n. The extended Euclidean algorithm is both the existence proof and the computation method."

- question: "Explain why gcd(a, n) = 1 is necessary for a multiplicative inverse of a to exist modulo n."
  type: short-answer
  answer: "If gcd(a, n) = d > 1, then d divides both a and n. For any integer b, d also divides a · b (since d | a). But d does not divide 1. So a · b ≡ 1 (mod n) would require d | (a · b − 1), meaning d divides 1, a contradiction. Therefore no b can satisfy a · b ≡ 1 (mod n) when d > 1. When gcd(a, n) = 1, Bézout's identity guarantees the existence of such a b."
  explanation: "The core issue is divisibility: if a and n share a common factor d > 1, then every multiple of a shares that factor, and so a · b − 1 can never be divisible by d (let alone by n). The condition gcd = 1 eliminates this obstruction, and Bézout's identity then constructively provides the inverse."
```

## Explainer

In ordinary arithmetic, every nonzero number has a multiplicative inverse: 3 × (1/3) = 1, 7 × (1/7) = 1. But in modular arithmetic, there are no fractions. So what replaces 1/a? A **multiplicative inverse mod n** is an integer b such that a·b ≡ 1 (mod n) — meaning a·b leaves remainder 1 when divided by n. For example, the inverse of 3 mod 7 is 5, because 3·5 = 15 = 2·7 + 1 ≡ 1 (mod 7). Once you have this, you can "divide by 3" in mod 7 arithmetic by multiplying by 5 instead.

The key question is: when does this inverse exist? Your prerequisite on modular arithmetic introduced the idea that working mod n partitions integers into residue classes. The inverse of a mod n exists if and only if gcd(a, n) = 1 — that is, a and n share no common factor. Intuitively: if gcd(a,n) = d > 1, then a·b is always divisible by d for any b, so a·b can never leave remainder 1 (which isn't divisible by d). But if gcd(a,n) = 1, then a and n are "independent" enough that some combination a·b hits exactly 1 mod n.

To actually find the inverse, you use the **extended Euclidean algorithm**, which you already know computes gcd(a,n). Recall that the extended version doesn't just compute gcd(a,n) = 1 — it also finds integers s and t such that as + nt = 1 (Bézout's identity). Taking this equation mod n: as + nt ≡ as ≡ 1 (mod n), since nt ≡ 0. So s is the inverse of a mod n. For example, to invert 3 mod 7: the extended Euclidean algorithm finds 3·5 + 7·(−2) = 15 − 14 = 1, giving s = 5. The inverse is 5.

This tool is essential for solving **linear congruences** of the form ax ≡ b (mod n). When gcd(a,n)=1, the unique solution is x ≡ a⁻¹·b (mod n) — you just multiply both sides by the inverse. When gcd(a,n) > 1, solutions exist only if gcd(a,n) divides b, and there are multiple solutions. Multiplicative inverses also sit at the heart of RSA encryption: the decryption exponent d is the modular inverse of the encryption exponent e modulo φ(n), computed via the extended Euclidean algorithm on numbers with hundreds of digits.
