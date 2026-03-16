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

## Explainer

Vandermonde's identity answers a natural question: if you have two separate groups — say m red balls and n blue balls — and you want to choose r balls total, how many ways are there? You already know from your work with combinations that choosing r items from a combined pool of m+n gives C(m+n, r). Vandermonde's identity says you can also count by considering every possible split: take k from the red group (C(m,k) ways) and r−k from the blue group (C(n,r−k) ways), then sum over all valid values of k. Both methods count the same selections, so they must be equal: C(m+n, r) = Σₖ C(m,k) · C(n,r−k).

The range of k in the summation is limited by what makes sense: k can't exceed m (you can't take more red balls than exist) and r−k can't exceed n. But you don't need to track these bounds carefully in practice, because C(m,k) = 0 whenever k > m or k < 0, and similarly C(n,r−k) = 0 whenever r−k > n. So you can let k run from 0 to r and the out-of-range terms simply contribute 0.

A useful special case is C(2n, n) = Σₖ C(n,k)². This follows by setting m = n and r = n in Vandermonde's identity, then noting that C(n, n−k) = C(n,k). It tells you that the number of ways to choose n items from 2n equals the sum of squares of the binomial coefficients in the nth row of Pascal's triangle. For instance, C(6,3) = 20 and 1² + 3² + 3² + 1² = 1 + 9 + 9 + 1 = 20. This is a striking identity that is difficult to prove algebraically but nearly obvious from the two-group counting argument.

Vandermonde's identity is also the combinatorial heart of the generating function proof you may encounter later. The generating function (1+x)^m has C(m,k) as the coefficient of xᵏ; similarly (1+x)^n has C(n,j) as the coefficient of xʲ. Multiplying these two power series and collecting the coefficient of xʳ on both sides — from (1+x)^{m+n} = C(m+n,r) and from the product as Σ C(m,k)·C(n,r−k) — gives Vandermonde's identity directly. The combinatorial proof builds intuition; the algebraic proof via generating functions connects it to a broader toolset.
