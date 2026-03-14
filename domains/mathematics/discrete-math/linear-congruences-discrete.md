---
id: linear-congruences-discrete
title: Linear Congruences and Solutions
domain: mathematics
course: discrete-math
prerequisites:
- id: modular-arithmetic
  type: hard
- id: divisibility-and-gcd
  type: hard
builds-toward:
- simultaneous-congruences-crt
- multiplicative-inverse-modular
tags:
- number-theory
- modular-arithmetic
- congruences
stage: formal-systems
status: draft
---

# Linear Congruences and Solutions

## Core Idea
A linear congruence ax ≡ b (mod n) has solutions if and only if gcd(a,n) divides b. When solutions exist, there are exactly gcd(a,n) distinct solutions modulo n. These can be found using the extended Euclidean algorithm.
