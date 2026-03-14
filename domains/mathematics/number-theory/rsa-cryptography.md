---
id: rsa-cryptography
title: 'Cryptographic Applications: RSA'
domain: mathematics
course: number-theory
prerequisites:
- id: euler-theorem
  type: hard
- id: euler-totient-function
  type: soft
tags:
- rsa
- cryptography
- applications
- public-key
stage: advanced
status: draft
---

# Cryptographic Applications: RSA

## Core Idea
RSA encryption relies on the difficulty of factoring large numbers and the ease of computing modular exponentiation. Using Euler's theorem, encryption and decryption are inverse operations: (m^e)^d ≡ m (mod n) when ed ≡ 1 (mod φ(n)). Security depends on the computational hardness of factorization.
