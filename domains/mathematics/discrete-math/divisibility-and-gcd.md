---
id: divisibility-and-gcd
title: Divisibility and Greatest Common Divisor
domain: mathematics
course: discrete-math
prerequisites:
- id: prime-and-composite-numbers
  type: hard
- id: mathematical-induction
  type: soft
builds-toward:
- euclidean-algorithm
- modular-arithmetic
- fundamental-theorem-of-arithmetic
tags:
- divisibility
- gcd
- lcm
- number-theory
- bezout
stage: formal-systems
status: draft
---

# Divisibility and Greatest Common Divisor

## Core Idea
An integer a divides b (a | b) if there exists an integer k such that b = ak. The greatest common divisor gcd(a,b) is the largest positive integer dividing both a and b. Bezout's identity guarantees integers x, y such that ax + by = gcd(a,b). The least common multiple satisfies lcm(a,b) = |ab|/gcd(a,b). These concepts are the algebraic foundation of number theory and underlie primality testing, modular arithmetic, and public-key cryptography.

## How It's Best Learned
Compute GCDs first by prime factorization to build intuition, then learn the Euclidean algorithm for efficiency. Prove Bezout's identity constructively. Connect GCD to familiar applications: simplifying fractions, finding when two periodic events coincide.

## Common Misconceptions
- Confusing GCD (largest common divisor) with LCM (smallest common multiple).
- Assuming gcd(a,b) must be prime — it can be any positive integer.
- Not knowing that Bezout coefficients x, y may be negative integers.
