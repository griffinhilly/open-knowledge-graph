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
