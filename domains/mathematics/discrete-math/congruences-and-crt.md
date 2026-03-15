---
id: congruences-and-crt
title: Linear Congruences and the Chinese Remainder Theorem
domain: mathematics
course: discrete-math
prerequisites:
- id: modular-arithmetic-discrete
  type: hard
- id: chinese-remainder-theorem
  type: hard
tags:
- linear-congruences
- CRT
- simultaneous-congruences
- solution-existence
stage: formal-systems
status: draft
---

# Linear Congruences and the Chinese Remainder Theorem

## Core Idea
A linear congruence ax ≡ b (mod n) has solutions iff gcd(a, n) divides b. If a solution exists, there are gcd(a, n) distinct solutions mod n. The Chinese Remainder Theorem: if n₁, n₂, ..., nₖ are pairwise coprime, the system x ≡ aᵢ (mod nᵢ) has a unique solution mod (n₁n₂...nₖ).

## How It's Best Learned
Solve ax ≡ b (mod n) by finding a multiplicative inverse (if it exists) via extended Euclidean algorithm. Apply CRT to solve systems of congruences. Use CRT for applications: secret sharing, garbled circuits.

## Common Misconceptions
Linear congruences don't always have solutions; check gcd(a, n) | b first. CRT requires pairwise coprimality, not just mutual primality. Solutions are unique mod the product, not individually.
