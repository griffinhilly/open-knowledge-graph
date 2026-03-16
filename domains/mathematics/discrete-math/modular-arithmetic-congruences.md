---
id: modular-arithmetic-congruences
title: Modular Arithmetic and Congruences
domain: mathematics
course: discrete-math
prerequisites: []
builds-toward:
- euclidean-algorithm-gcd
- chinese-remainder-theorem
tags:
- modular-arithmetic
- number-theory
stage: formal-systems
status: draft
---

# Modular Arithmetic and Congruences

## Core Idea
a ≡ b (mod n) if and only if n divides a - b. Modular arithmetic obeys addition, subtraction, and multiplication rules like standard arithmetic. Congruences partition the integers into residue classes, and arithmetic can be performed within these classes.

## Explainer

Think of a clock. After 12 hours, the clock resets — 13 o'clock is the same position as 1 o'clock. This is modular arithmetic in action: 13 ≡ 1 (mod 12) because 12 divides 13 − 1 = 12. The notation a ≡ b (mod n) simply means that a and b leave the same remainder when divided by n, or equivalently that n divides a − b. Every integer belongs to exactly one **residue class** modulo n, represented by its remainder: 0, 1, 2, ..., n − 1. Instead of working with all integers, you work with these n classes.

The power of modular arithmetic comes from its **closure under operations**. If a ≡ b (mod n) and c ≡ d (mod n), then a + c ≡ b + d (mod n) and a × c ≡ b × d (mod n). This means you can reduce numbers before performing operations and still get the right answer modulo n. For example, to compute 99 × 101 (mod 10), note that 99 ≡ 9 and 101 ≡ 1 (mod 10), so the product is ≡ 9 × 1 = 9 (mod 10). The actual product 9,999 also ends in 9 — confirming the calculation. This reduction trick makes modular arithmetic essential in cryptography and computer science, where numbers can be astronomically large.

Division works differently in modular arithmetic. You cannot always divide — you need a **modular inverse**. The inverse of a modulo n exists if and only if gcd(a, n) = 1; when it exists, a⁻¹ is the unique x with ax ≡ 1 (mod n). For example, 3 × 5 = 15 ≡ 1 (mod 7), so 3⁻¹ ≡ 5 (mod 7). When n is prime, every nonzero element has an inverse, making the residue classes modulo a prime into a complete arithmetic system (a field). This is why prime moduli appear everywhere in cryptographic protocols.

A powerful shortcut for large powers is **modular exponentiation**. To compute 2¹⁰⁰ (mod 13), you don't multiply 100 times. Instead, repeatedly square and reduce: 2² = 4, 2⁴ ≡ 3, 2⁸ ≡ 9, 2¹⁶ ≡ 3 (mod 13), and so on, then combine. This connects to Fermat's Little Theorem: if p is prime and p does not divide a, then aᵖ⁻¹ ≡ 1 (mod p). So 2¹² ≡ 1 (mod 13), meaning powers of 2 cycle with period dividing 12 modulo 13. Modular arithmetic transforms intractable arithmetic on huge numbers into manageable computation on small residues.
