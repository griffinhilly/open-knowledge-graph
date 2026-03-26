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
- condition-number-of-a-matrix
tags:
- gaussian-elimination
- pivoting
- linear-systems
stage: formal-systems
status: validated
---

# Gaussian Elimination with Pivoting

## Core Idea
Gaussian elimination with partial (row) or complete (row and column) pivoting reorders equations to avoid dividing by small numbers, which amplifies rounding errors. Pivoting maintains multipliers |m_ij| ≤ 1, keeping roundoff errors bounded. While Gaussian elimination without pivoting can fail catastrophically on well-conditioned systems, pivoting recovers numerical stability without significantly increasing computation.

## Questions

```yaml
- question: "Without pivoting, Gaussian elimination is applied to a system where one step produces a very small pivot ε ≈ 0.0001. The multiplier for the next row is approximately 10,000. What is the danger?"
  type: multiple-choice
  options:
    - "The algorithm will fail to find a solution because the system is ill-conditioned"
    - "Floating-point rounding errors in that row are amplified by 10,000 before being subtracted, potentially ruining the result"
    - "The pivot ε causes division by zero, halting the computation"
    - "The multiplier exceeds 1, violating Gaussian elimination's convergence criterion"
  answer: 1
  explanation: "Small pivots don't cause division by zero — they produce huge multipliers. When that large multiplier (10,000) is applied to a row with even tiny floating-point errors, those errors are scaled up by a factor of 10,000. The cumulative effect can render the numerical answer completely wrong even for a well-conditioned system. Option A is wrong because the system's condition number is a property of the matrix, independent of pivot order — a well-conditioned system can still be destroyed by poor pivot choice."

- question: "Partial pivoting guarantees that all multipliers |mᵢₖ| satisfy what condition, and why does this matter?"
  type: multiple-choice
  options:
    - "|mᵢₖ| ≤ 1, which ensures rounding errors are not amplified as they propagate through subsequent row operations"
    - "|mᵢₖ| ≥ 1, which ensures the pivot rows dominate and the algorithm converges"
    - "|mᵢₖ| = 1 exactly, which balances all rows and eliminates rounding error"
    - "|mᵢₖ| < n, where n is the matrix size — keeping multipliers below the matrix dimension"
  answer: 0
  explanation: "Partial pivoting selects the row with the largest absolute value in the current column as the pivot. By placing the maximum value in the denominator of each multiplier mᵢₖ = aᵢₖ / aₖₖ, it guarantees |mᵢₖ| ≤ 1 for all entries below the pivot. When multipliers are at most 1, rounding errors are not amplified — they can only stay the same or shrink as they propagate. This is the mechanism by which partial pivoting achieves numerical stability."

- question: "A system of linear equations is well-conditioned (small condition number), but Gaussian elimination without pivoting produces a wildly inaccurate answer. This can happen."
  type: true-false
  answer: true
  explanation: "This is the crucial point of the topic. The condition number measures sensitivity of the solution to perturbations in the data — a well-conditioned system has a unique, stable solution. But Gaussian elimination without pivoting can still fail numerically by encountering a small pivot, amplifying floating-point rounding errors catastrophically even though the mathematical problem is perfectly well-posed. Condition number and pivot behavior are separate issues. Pivoting addresses the numerical algorithm's stability, not the problem's inherent sensitivity."

- question: "Complete pivoting is always preferred over partial pivoting in practice because it provides a stronger stability guarantee."
  type: true-false
  answer: false
  explanation: "Despite its stronger theoretical guarantee, complete pivoting is rarely used in practice. It requires searching the entire remaining submatrix (O(n²) entries per step) rather than just one column (O(n) entries), and it also permutes column order, complicating the recovery of the solution. For virtually all problems in scientific computing, partial pivoting provides sufficient stability at much lower overhead. The better guarantee of complete pivoting does not justify its cost in practice — partial pivoting is the standard choice."

- question: "Why does reordering the rows of a linear system (as partial pivoting does) produce the same mathematical solution but better numerical results?"
  type: short-answer
  answer: "Row swapping is a valid elementary row operation that doesn't change the solution set of the system — the equations are the same, just reordered. Numerically, however, order determines which value becomes the pivot at each step. By choosing the largest available entry as the pivot, partial pivoting ensures multipliers stay ≤ 1, preventing rounding errors from being amplified. The mathematics is unchanged; only the numerical behavior improves."
  explanation: "The key insight is that pivoting is a strategy for the algorithm's numerical behavior, not a change to the mathematical problem. Swapping row 3 and row 7 doesn't alter the set of equations or their solution — it merely changes the sequence of operations. Since floating-point arithmetic is the source of error, and since the magnitude of multipliers determines how errors propagate, choosing large pivots controls error growth without touching the underlying mathematics."
```

## Explainer

From basic Gaussian elimination, you know the algorithm: eliminate variables one column at a time by subtracting multiples of the pivot row from rows below. The multiplier for row i (when eliminating column k) is mᵢₖ = aᵢₖ / aₖₖ. This works perfectly in exact arithmetic. The problem — which your prerequisite in numerical stability prepared you for — is that computers work with floating-point numbers, and dividing by a very small pivot aₖₖ can blow up errors dramatically.

Here's the disaster scenario. Suppose your pivot is 0.0001 and the entry below it is 1. The multiplier is 1/0.0001 = 10,000. Now every rounding error in that row gets amplified by 10,000 before being subtracted. Even a tiny floating-point imprecision in the original data becomes a massive error in the result. The system might be perfectly well-conditioned (have a unique, stable solution) and still produce a garbage numerical answer — purely because of the order in which you encountered a small number.

**Partial pivoting** fixes this by a simple rule: before eliminating column k, scan down column k from row k to n, find the entry with the largest absolute value, and swap that row up to become the pivot row. This guarantees the pivot is at least as large as all entries below it in that column, so all multipliers satisfy |mᵢₖ| ≤ 1. Small multipliers mean errors don't get amplified — they stay bounded. In practice, partial pivoting makes Gaussian elimination reliable for virtually all problems that arise in scientific computing. You're not changing the mathematical problem; you're just reordering the equations, which doesn't change the solution.

**Complete pivoting** additionally searches for the largest entry in the entire remaining submatrix, swapping both rows and columns. This provides the strongest stability guarantee, but requires more searching and also permutes the variable order, complicating bookkeeping. For most applications, partial pivoting is sufficient. The computational overhead of either strategy is small relative to the O(n³) cost of elimination itself — just O(n²) comparisons for partial pivoting. Pivoting is why Gaussian elimination is a practical algorithm, not just a theoretical one: it's the difference between a method that works on paper and one that you can trust on a computer.
