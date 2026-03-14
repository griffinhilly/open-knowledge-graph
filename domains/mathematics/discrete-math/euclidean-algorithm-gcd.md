---
id: euclidean-algorithm-gcd
title: The Euclidean Algorithm and Greatest Common Divisor
domain: mathematics
course: discrete-math
prerequisites:
- id: modular-arithmetic-congruences
  type: hard
builds-toward:
- chinese-remainder-theorem
tags:
- number-theory
- gcd
- algorithm
stage: formal-systems
status: draft
---

# The Euclidean Algorithm and Greatest Common Divisor

## Core Idea
The Euclidean algorithm efficiently computes gcd(a,b) using repeated division: gcd(a,b) = gcd(b, a mod b), stopping when the remainder is 0. Time complexity is O(log(min(a,b))). The extended Euclidean algorithm finds integers x, y such that ax + by = gcd(a,b).
