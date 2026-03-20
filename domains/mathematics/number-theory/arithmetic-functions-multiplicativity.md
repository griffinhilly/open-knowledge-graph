---
id: arithmetic-functions-multiplicativity
title: Arithmetic Functions and Multiplicativity
domain: mathematics
course: number-theory
prerequisites:
- id: fundamental-theorem-arithmetic-rigorous
  type: hard
builds-toward:
- eulers-totient-function
- mobius-function-inversion
tags:
- arithmetic-functions
- multiplicative
stage: advanced
status: draft
---

# Arithmetic Functions and Multiplicativity

## Core Idea
An arithmetic function maps positive integers to complex numbers. A function f is multiplicative if f(mn) = f(m)f(n) whenever gcd(m, n) = 1, and completely multiplicative if this holds for all m and n regardless of their gcd. Because every positive integer factors uniquely into prime powers, a multiplicative function is entirely determined by its values on prime powers. Key examples include Euler's totient φ(n), the divisor function σ(n), and the Möbius function μ(n). Multiplicativity enables efficient computation and is the foundation for techniques like Möbius inversion and Dirichlet series manipulation.

## How It's Best Learned
Verify multiplicativity by hand for small examples: compute φ(12) via φ(4)·φ(3) and confirm it matches the direct count. Then see how knowing φ(pᵏ) = pᵏ − pᵏ⁻¹ lets you compute φ for any n from its prime factorization.

## Common Misconceptions
Multiplicative does not mean f(mn) = f(m)f(n) for all m, n—that is completely multiplicative. The coprimality condition is essential. Also, f(1) = 1 is a consequence of multiplicativity, not an extra assumption.

