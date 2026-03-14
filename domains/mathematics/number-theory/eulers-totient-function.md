---
id: eulers-totient-function
title: Euler's Totient Function
domain: mathematics
course: number-theory
prerequisites:
- id: arithmetic-functions-multiplicativity
  type: hard
- id: modular-arithmetic
  type: hard
builds-toward:
- eulers-theorem
- primitive-roots-cyclic-groups-mod-p
- cryptographic-applications-rsa
tags:
- totient
- euler-phi
- coprime
stage: advanced
status: draft
---

# Euler's Totient Function

## Core Idea
Euler's totient function φ(n) counts the positive integers up to n that are coprime to n. For a prime power p^k, φ(p^k) = p^(k-1)(p-1). Since φ is multiplicative, φ(n) = n∏(1 - 1/p) over primes dividing n.

## How It's Best Learned
Compute φ(n) for small values and verify the formula. Recognize the multiplicative structure and its connection to cyclic groups.

## Common Misconceptions
Thinking φ(n) requires checking all n integers (use the formula instead). Confusing φ with other arithmetic functions like σ or τ.
