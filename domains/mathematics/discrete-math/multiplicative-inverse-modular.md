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
