---
id: gaussian-elimination-pivoting
title: Gaussian Elimination with Partial Pivoting
domain: mathematics
course: linear-algebra
prerequisites:
- id: gaussian-elimination
  type: hard
builds-toward:
- lu-decomposition
- matrix-norms-conditioning
tags:
- numerical-stability
- pivoting
- gaussian-elimination
stage: formal-systems
status: validated
---

# Gaussian Elimination with Partial Pivoting

## Core Idea
Partial pivoting swaps rows to place the largest entry in the pivot position before elimination, reducing rounding errors in floating-point arithmetic. Without pivoting, small pivots can amplify errors in subsequent operations. Pivoting is essential for numerical stability and is standard in computational practice.

## Questions

```yaml
- question: "A student argues: 'Gaussian elimination finds the correct solution by construction, so pivoting is only needed when a diagonal entry is literally zero — otherwise it's just extra bookkeeping.' What is the critical flaw in this reasoning?"
  type: multiple-choice
  options:
    - "Gaussian elimination does not always find the correct solution even with exact arithmetic"
    - "A very small but nonzero pivot creates a huge multiplier that amplifies floating-point rounding errors, potentially making the computed answer completely wrong even when the exact solution exists and is unique"
    - "Pivoting is needed to reduce the number of row operations and improve speed, not for accuracy"
    - "The student is correct — pivoting is only logically required when the pivot is exactly zero"
  answer: 1
  explanation: "With exact arithmetic, the student would be right. The problem is floating-point arithmetic, where every stored number carries a tiny rounding error. If the pivot is 0.0001 and another entry in the column is 500, the elimination multiplier is 5,000,000. Any rounding error in the pivot row is multiplied by this factor before being subtracted from the other row. The resulting error can overwhelm the true solution. A near-zero pivot is as dangerous as a zero pivot in floating-point computation."

- question: "Before using entry (k, k) as the current pivot, partial pivoting scans column k below that row and swaps the row with the largest absolute value into position k. What is the key numerical consequence?"
  type: multiple-choice
  options:
    - "It guarantees the system has a unique solution by ensuring all pivots are nonzero"
    - "It ensures all elimination multipliers in this step have absolute value ≤ 1, so rounding errors in the pivot row cannot be amplified beyond their original magnitude"
    - "It reduces the total number of arithmetic operations needed for the elimination"
    - "It produces a symmetric factorization that is cheaper to back-substitute"
  answer: 1
  explanation: "By placing the largest entry in the pivot position, every multiplier m_{ij} = a_{ij}/pivot satisfies |m_{ij}| ≤ 1. When you subtract m_{ij} times the pivot row from row j, any rounding errors are scaled by a factor ≤ 1 — they shrink or stay the same, never grow. Without pivoting, multipliers can be arbitrarily large (0.0001 pivot against a 500 entry gives multiplier 5,000,000), turning microscopic floating-point errors into catastrophic ones through n steps of elimination."

- question: "Even when a linear system Ax = b has a unique exact solution, Gaussian elimination without pivoting can produce a completely wrong numerical answer due to floating-point error amplification."
  type: true-false
  answer: true
  explanation: "This is the core motivation for partial pivoting. The existence and uniqueness of the mathematical solution is not the issue; the question is whether the numerical algorithm finds it accurately. A near-zero pivot creates a large multiplier that amplifies rounding errors. Across multiple elimination steps, these errors compound, potentially making the computed result far from the true solution. Partial pivoting keeps all multipliers ≤ 1, preventing this amplification regardless of the system's condition."

- question: "Using partial pivoting changes the mathematical solution that Gaussian elimination computes, and should primarily be applied when numerical accuracy matters more than finding the true exact solution."
  type: true-false
  answer: false
  explanation: "Partial pivoting does not change the solution being computed — it finds the same solution more accurately. Row swaps are valid elementary row operations that preserve the solution set of Ax = b. The row swaps are tracked via a permutation matrix P, so the resulting factorization is PA = LU instead of A = LU, but this represents the same system. The mathematical answer is unchanged; only the numerical accuracy of computing it improves. All major numerical libraries apply pivoting by default for this reason."

- question: "Explain in your own words why a very small pivot entry is dangerous in floating-point Gaussian elimination, and how partial pivoting addresses the problem."
  type: short-answer
  answer: "A small pivot creates a large elimination multiplier (the ratio by which the pivot row is scaled before subtracting from another row). Every floating-point number carries a tiny rounding error — roughly 10^{-16} for double precision. Multiply that error by a factor of 5,000,000 and it becomes 10^{-9}, which can be large relative to the true answer. Partial pivoting puts the largest available entry in the pivot position, ensuring all multipliers have absolute value at most 1, so rounding errors cannot grow during elimination."
  explanation: "The relationship is direct: multiplier = (entry to eliminate) / (pivot). Small pivot + large entry = huge multiplier = large error amplification. Partial pivoting inverts this: by making the pivot the largest entry, every other entry divided by it gives a multiplier ≤ 1. This bounds error growth throughout the n steps of elimination. The technique has zero cost in terms of the final mathematical answer — only bookkeeping (tracking row swaps in a permutation matrix) is added."
```

## Explainer

You know Gaussian elimination: systematically use row operations to reduce a matrix to upper triangular form, then back-substitute to find the solution. On paper with exact arithmetic, it works perfectly. But computers store numbers in **floating-point** format with finite precision — every number is rounded to about 15-16 significant digits. This rounding is usually harmless, but Gaussian elimination without care can turn tiny rounding errors into massive ones. The fix is **partial pivoting**.

Here's the problem. Suppose your current pivot — the leading entry you're eliminating with — is 0.0001, and another entry in the same column is 500. To eliminate the 500, you multiply the pivot row by 500/0.0001 = 5,000,000 and subtract. You've just amplified any rounding error in the pivot row by a factor of 5 million. The result can have errors so large that your "solution" is completely wrong. The size of this amplification is related to the **multiplier**: if the multiplier is large, errors grow; if it's small (≤ 1), errors stay controlled.

**Partial pivoting** prevents this by swapping rows before each elimination step. Before using entry (k, k) as the pivot, scan all the entries below it in column k and find the largest one in absolute value. Swap that row up to position k. Now the pivot is the largest available entry in its column, so every multiplier in this step has absolute value ≤ 1. Errors don't get amplified — they stay bounded. The only cost is bookkeeping: you record the row swaps in a permutation matrix P so you can reconstruct that you solved PA = LU rather than A = LU directly.

A small example shows the difference clearly. Solving the system [0.001, 1; 1, 1] × [x; y] = [1; 2] without pivoting: divide row 2 by 0.001 to eliminate, producing a multiplier of 1000 that amplifies floating-point noise. With pivoting: swap rows first so the pivot is 1 (the larger entry), multiplier becomes 0.001, and the elimination is numerically clean. The final answers match analytically but diverge significantly in floating-point.

Every serious numerical linear algebra library — LAPACK, NumPy, MATLAB — applies partial pivoting by default when solving Ax = b. It's not optional engineering caution; it's the reason direct solvers work reliably in practice. Understanding pivoting also prepares you for **LU decomposition with permutation matrices** (PA = LU), where the same row-swapping logic is formalized into a factorization that can be reused to solve systems with multiple right-hand sides efficiently.
