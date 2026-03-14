---
id: cryptographic-applications-rsa
title: Cryptographic Applications (RSA)
domain: mathematics
course: number-theory
prerequisites:
- id: eulers-theorem
  type: hard
- id: eulers-totient-function
  type: hard
- id: modular-arithmetic
  type: hard
tags:
- rsa
- cryptography
- public-key
stage: advanced
status: draft
---

# Cryptographic Applications (RSA)

## Core Idea
RSA uses Euler's theorem and the difficulty of factoring large numbers. Given n = pq (p, q distinct primes), pick e coprime to φ(n) = (p-1)(q-1), compute d ≡ e^(-1) (mod φ(n)), encrypt m as c ≡ m^e (mod n), and decrypt as m ≡ c^d (mod n). Security rests on n's factorization being hard.
