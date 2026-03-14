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
