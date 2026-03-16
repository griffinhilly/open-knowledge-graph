---
id: condition-number-of-a-matrix
title: Condition Number of a Matrix
domain: mathematics
course: numerical-analysis
prerequisites:
- id: gaussian-elimination-with-pivoting
  type: hard
builds-toward:
- jacobi-iterative-method
tags:
- condition-number
- matrix-sensitivity
- ill-conditioning
stage: advanced
status: draft
---

# Condition Number of a Matrix

## Core Idea
The condition number κ(A) = ||A|| ||A⁻¹|| measures sensitivity of the linear system Ax = b to perturbations in A and b. Relative error in x is bounded by approximately κ(A) times relative error in data. Large condition numbers indicate ill-conditioned problems; small perturbations cause large solution changes regardless of algorithm choice.

## Explainer

When you solve a linear system Ax = b using Gaussian elimination with pivoting, you obtain a numerical answer — but how much should you trust it? The answer depends not on your algorithm's quality, but on the problem itself. The **condition number** κ(A) is the quantity that tells you how sensitive the solution is to small perturbations in the data, regardless of how you solve the system.

To build intuition, think of κ(A) as an "error amplification factor." If the data in b has relative errors of size ε (due to measurement noise or floating-point representation), the computed solution x can have relative errors up to roughly κ(A) · ε. If κ(A) = 10³ and your data has 6 significant digits (ε ≈ 10⁻⁶), you might lose 3 of those digits — leaving only 3 significant digits in your solution. If κ(A) = 10¹², you lose 12 digits, and on a 16-digit double-precision machine, your "solution" may be numerically meaningless even with a perfect algorithm.

The formal definition κ(A) = ||A|| · ||A⁻¹|| measures how much the matrix can stretch vectors (||A||) and how much the inverse can then amplify perturbations (||A⁻¹||). A geometric picture: a well-conditioned matrix maps the unit sphere to a modestly elongated ellipsoid; an ill-conditioned matrix maps it to a very thin needle — and when the needle gets perturbed, recovering the preimage amplifies the perturbation enormously. An orthogonal matrix has κ = 1 (it only rotates, never stretches), so it is perfectly conditioned.

**Ill-conditioning** is a property of the problem, not the algorithm. No amount of clever pivoting or iterative refinement can rescue a truly ill-conditioned system, because the information in b simply does not determine x precisely. Common sources of ill-conditioning include nearly linearly dependent rows or columns, matrices with rows spanning widely different scales, and the **Hilbert matrix** (whose (i,j) entry is 1/(i+j−1)) — a famous example whose condition number grows exponentially with size. When you encounter κ(A) >> 1, the right response is not to seek a better algorithm but to reconsider whether the problem is well-posed, or to employ regularization techniques that trade solution sensitivity for solution stability.
