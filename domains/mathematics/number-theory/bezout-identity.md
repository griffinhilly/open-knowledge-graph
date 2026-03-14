---
id: bezout-identity
title: Bézout's Identity
domain: mathematics
course: number-theory
prerequisites:
- id: divisibility-theory-formal
  type: hard
- id: euclidean-algorithm
  type: hard
builds-toward:
- linear-diophantine-equations
- chinese-remainder-theorem
tags:
- bezout
- gcd
- linear-combinations
stage: advanced
status: draft
---

# Bézout's Identity

## Core Idea
Bézout's identity states that for any integers a and b, there exist integers x and y such that ax + by = gcd(a,b). This fundamental result expresses the gcd as a linear combination of a and b, directly connecting divisibility to linear Diophantine equations.

## How It's Best Learned
Use the extended Euclidean algorithm to compute gcd(a,b) and simultaneously find the Bézout coefficients x and y. Verify with examples like gcd(35,15) step-by-step.

## Common Misconceptions
Thinking the coefficients x and y are unique (infinitely many solutions exist). Assuming x and y must be positive.
