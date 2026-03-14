---
id: chinese-remainder-theorem
title: The Chinese Remainder Theorem and Its Applications
domain: mathematics
course: discrete-math
prerequisites:
- id: euclidean-algorithm-gcd
  type: hard
tags:
- number-theory
- crt
stage: formal-systems
status: draft
---

# The Chinese Remainder Theorem and Its Applications

## Core Idea
If n₁, n₂, …, nₖ are pairwise coprime, the system x ≡ a₁ (mod n₁), x ≡ a₂ (mod n₂), … has a unique solution modulo n₁n₂⋯nₖ. The CRT enables efficient computation by reducing large moduli to smaller ones and has applications in cryptography and parallel computation.
