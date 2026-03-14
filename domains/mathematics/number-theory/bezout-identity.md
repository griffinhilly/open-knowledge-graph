---
id: bezout-identity
title: Bézout's Identity
domain: mathematics
course: number-theory
prerequisites:
- id: euclidean-algorithm
  type: hard
builds-toward:
- linear-diophantine-equations
tags:
- gcd
- linear-combinations
- bézout
stage: advanced
status: draft
---

# Bézout's Identity

## Core Idea
Bézout's identity states that for any integers a and b with gcd(a,b) = d, there exist integers x and y such that ax + by = d. This fundamental result connects the greatest common divisor to linear combinations and enables solving linear Diophantine equations. The extended Euclidean algorithm provides a constructive proof.

## How It's Best Learned
First apply the Euclidean algorithm to find gcd(a,b), then work backward to express the gcd as a linear combination. Practice with several examples where the linear combination is non-obvious.

## Common Misconceptions
The coefficients x and y are not unique; any solution plus a multiple of (b/d, −a/d) gives another solution. Not all linear combinations of a and b equal the gcd—only the minimum positive linear combination does.
