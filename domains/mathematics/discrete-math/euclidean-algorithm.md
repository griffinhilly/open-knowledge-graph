---
id: euclidean-algorithm
title: The Euclidean Algorithm
domain: mathematics
course: discrete-math
prerequisites:
- id: divisibility-and-gcd
  type: hard
- id: mathematical-induction
  type: soft
builds-toward:
- modular-arithmetic
- chinese-remainder-theorem
tags:
- euclidean-algorithm
- gcd
- extended-euclidean
- bezout
- modular-inverse
stage: formal-systems
status: validated
---

# The Euclidean Algorithm

## Core Idea
The Euclidean algorithm computes gcd(a,b) by repeated application of the division algorithm: gcd(a,b) = gcd(b, a mod b), stopping when the remainder is 0. The algorithm runs in O(log(min(a,b))) steps — far faster than factoring. The extended Euclidean algorithm additionally computes integers x, y satisfying ax + by = gcd(a,b) by back-substituting through the remainder table. This is the standard method for computing modular inverses, essential in RSA and other cryptographic algorithms.

## How It's Best Learned
Trace the algorithm step-by-step for several pairs, recording the remainder at each step. Practice back-substitution to find Bezout coefficients. Implement in pseudocode to appreciate the algorithm's efficiency versus exhaustive search.

## Common Misconceptions
- Stopping too early — the algorithm terminates only when the remainder reaches exactly 0.
- Making sign errors during the back-substitution step of the extended algorithm.
- Thinking GCD computation requires factoring — the Euclidean algorithm avoids factoring entirely.
