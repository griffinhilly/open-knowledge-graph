---
id: gaussian-elimination-with-pivoting
title: Gaussian Elimination with Pivoting
domain: mathematics
course: numerical-analysis
prerequisites:
- id: gaussian-elimination
  type: hard
- id: numerical-stability
  type: hard
builds-toward:
- lu-decomposition
- condition-number-of-matrix
tags:
- gaussian-elimination
- pivoting
- linear-systems
stage: formal-systems
status: draft
---

# Gaussian Elimination with Pivoting

## Core Idea
Gaussian elimination with partial (row) or complete (row and column) pivoting reorders equations to avoid dividing by small numbers, which amplifies rounding errors. Pivoting maintains multipliers |m_ij| ≤ 1, keeping roundoff errors bounded. While Gaussian elimination without pivoting can fail catastrophically on well-conditioned systems, pivoting recovers numerical stability without significantly increasing computation.

## Explainer

From basic Gaussian elimination, you know the algorithm: eliminate variables one column at a time by subtracting multiples of the pivot row from rows below. The multiplier for row i (when eliminating column k) is mᵢₖ = aᵢₖ / aₖₖ. This works perfectly in exact arithmetic. The problem — which your prerequisite in numerical stability prepared you for — is that computers work with floating-point numbers, and dividing by a very small pivot aₖₖ can blow up errors dramatically.

Here's the disaster scenario. Suppose your pivot is 0.0001 and the entry below it is 1. The multiplier is 1/0.0001 = 10,000. Now every rounding error in that row gets amplified by 10,000 before being subtracted. Even a tiny floating-point imprecision in the original data becomes a massive error in the result. The system might be perfectly well-conditioned (have a unique, stable solution) and still produce a garbage numerical answer — purely because of the order in which you encountered a small number.

**Partial pivoting** fixes this by a simple rule: before eliminating column k, scan down column k from row k to n, find the entry with the largest absolute value, and swap that row up to become the pivot row. This guarantees the pivot is at least as large as all entries below it in that column, so all multipliers satisfy |mᵢₖ| ≤ 1. Small multipliers mean errors don't get amplified — they stay bounded. In practice, partial pivoting makes Gaussian elimination reliable for virtually all problems that arise in scientific computing. You're not changing the mathematical problem; you're just reordering the equations, which doesn't change the solution.

**Complete pivoting** additionally searches for the largest entry in the entire remaining submatrix, swapping both rows and columns. This provides the strongest stability guarantee, but requires more searching and also permutes the variable order, complicating bookkeeping. For most applications, partial pivoting is sufficient. The computational overhead of either strategy is small relative to the O(n³) cost of elimination itself — just O(n²) comparisons for partial pivoting. Pivoting is why Gaussian elimination is a practical algorithm, not just a theoretical one: it's the difference between a method that works on paper and one that you can trust on a computer.
