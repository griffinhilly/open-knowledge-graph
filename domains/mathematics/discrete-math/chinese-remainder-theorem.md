---
id: chinese-remainder-theorem
title: The Chinese Remainder Theorem
domain: mathematics
course: discrete-math
prerequisites:
- id: modular-arithmetic
  type: hard
- id: euclidean-algorithm
  type: hard
tags:
- chinese-remainder-theorem
- CRT
- congruences
- number-theory
- cryptography
stage: formal-systems
status: draft
---

# The Chinese Remainder Theorem

## Core Idea
The Chinese Remainder Theorem (CRT) states that if n₁, n₂, …, nₖ are pairwise coprime, then for any remainders r₁, …, rₖ, there exists a unique solution mod N = n₁n₂⋯nₖ to the simultaneous congruences x ≡ rᵢ (mod nᵢ). The constructive proof builds the solution using modular inverses. The CRT has broad applications: it speeds up RSA decryption by splitting computations across small moduli, enables secret sharing schemes, and appears in polynomial interpolation and multi-precision arithmetic.

## How It's Best Learned
Solve small systems by substitution first to see a solution exists, then apply the constructive formula. Work through a numerical cryptographic example to see how CRT reduces RSA computation cost. Try a system where the coprimality condition fails to understand why it is necessary.

## Common Misconceptions
- Applying CRT when moduli are not pairwise coprime — the theorem does not guarantee existence or uniqueness in this case.
- Confusing the combined modulus N = n₁n₂⋯nₖ with the sum n₁ + n₂ + ⋯ + nₖ.
