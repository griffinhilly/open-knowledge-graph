---
id: vandermonde-identity
title: Vandermonde's Identity
domain: mathematics
course: discrete-math
prerequisites:
- id: binomial-coefficients
  type: hard
- id: combinations
  type: hard
tags:
- combinatorics
- binomial-coefficients
- identities
stage: formal-systems
status: draft
---

# Vandermonde's Identity

## Core Idea
Vandermonde's identity states that C(m+n, r) = Σ C(m, k) × C(n, r-k). It counts ways to choose r items from two groups of sizes m and n. This identity connects binomial coefficients and has applications in probability and counting problems.

## How It's Best Learned
Derive it combinatorially by thinking of choosing r items from two combined groups. Verify with small values numerically.

## Common Misconceptions
- Treating the indices incorrectly in the summation. - Forgetting that k ranges only over valid values where both C(m,k) and C(n,r-k) are non-zero.
