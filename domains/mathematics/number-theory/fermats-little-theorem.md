---
id: fermats-little-theorem
title: Fermat's Little Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: congruence-properties
  type: hard
- id: group-definition-and-examples
  type: soft
builds-toward:
- eulers-theorem
- cryptographic-applications-rsa
tags:
- fermats-little-theorem
- prime-powers
- modular-exponentiation
stage: advanced
status: draft
---

# Fermat's Little Theorem

## Core Idea
If p is prime and gcd(a,p) = 1, then a^(p-1) ≡ 1 (mod p). This cornerstone result characterizes the exponent structure of multiplicative groups mod p and enables fast modular exponentiation in cryptography.
