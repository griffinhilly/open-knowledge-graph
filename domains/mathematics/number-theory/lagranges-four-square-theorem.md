---
id: lagranges-four-square-theorem
title: Lagrange's Four-Square Theorem
domain: mathematics
course: number-theory
prerequisites:
- id: fundamental-theorem-arithmetic-rigorous
  type: hard
tags:
- four-squares
- representation
- diophantine
stage: advanced
status: draft
---

# Lagrange's Four-Square Theorem

## Core Idea
Every non-negative integer is the sum of four perfect squares. Unlike the two-square case, this holds universally with a clean statement, proven via quaternion algebras or generating functions.

## Explainer

Start with a simple empirical observation: 1 = 1², 2 = 1² + 1², 3 = 1² + 1² + 1², 4 = 2², 5 = 2² + 1², 6 = 2² + 1² + 1², 7 = 2² + 1² + 1² + 1². Notice that 7 requires all four squares — no way to write it as the sum of three or fewer squares of integers. Lagrange's Four-Square Theorem, proved in 1770, asserts that this never gets worse: four squares always suffice for every non-negative integer.

To understand why four is special, contrast with two. From the **Fundamental Theorem of Arithmetic** you know that every integer factors uniquely into primes. The **sum-of-two-squares theorem** (a consequence of Fermat) says a positive integer is a sum of two squares if and only if in its prime factorization, every prime of the form 4k + 3 appears to an even power. So 3 (a 4k+3 prime to the first power) fails: 3 cannot be written as a² + b² for integers a, b. The two-square representation is selective. The **three-square theorem** (Legendre) says all integers are sums of three squares except those of the form 4^a(8b + 7). So 7 itself is excluded from three squares. But no such exceptions survive with four squares.

The classical proof uses **quaternion algebras** — a number system generalizing complex numbers to four dimensions, of the form a + bi + cj + dk. Crucially, quaternion norms multiply: N(qr) = N(q)N(r), where N(a + bi + cj + dk) = a² + b² + c² + d². This gives an **identity of four squares**: if m and n are each sums of four squares, then mn is also a sum of four squares. This multiplicativity means it suffices to prove the theorem for primes — the general case follows automatically from the prime factorization. For any prime p, one can show that among the p + 1 values 0², 1², …, ((p−1)/2)² and −1 − 0², −1 − 1², …, the pigeonhole principle guarantees a solution to a² + b² ≡ −1 (mod p), which bootstraps into representing p as a sum of four integer squares.

The theorem is tight in a precise sense: **Legendre's three-square theorem** shows that exactly the integers 4^a(8b + 7) require four squares and cannot be done with three. So Lagrange's result answers the question definitively — four squares are necessary in the worst case, and always sufficient. This makes the theorem a satisfying capstone: a clean, universal statement that falls out of the deep multiplicative structure of integers and the arithmetic of primes.
