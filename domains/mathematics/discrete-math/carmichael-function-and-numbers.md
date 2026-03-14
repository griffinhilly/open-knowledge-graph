---
id: carmichael-function-and-numbers
title: Carmichael Function and Carmichael Numbers
domain: mathematics
course: discrete-math
prerequisites:
- id: euler-totient-function
  type: hard
- id: fermat-little-theorem
  type: soft
tags:
- number-theory
- carmichael
- prime-testing
stage: formal-systems
status: draft
---

# Carmichael Function and Carmichael Numbers

## Core Idea
The Carmichael function λ(n) is the exponent of the multiplicative group modulo n. Carmichael numbers are composite numbers n where aⁿ⁻¹ ≡ 1 (mod n) for all a coprime to n, making them pseudoprimes to all bases. Understanding them is essential for probabilistic primality testing.
