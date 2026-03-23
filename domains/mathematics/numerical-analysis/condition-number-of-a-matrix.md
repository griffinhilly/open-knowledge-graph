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
stage: formal-systems
status: draft
---

# Condition Number of a Matrix

## Core Idea
The condition number κ(A) = ||A|| ||A⁻¹|| measures sensitivity of the linear system Ax = b to perturbations in A and b. Relative error in x is bounded by approximately κ(A) times relative error in data. Large condition numbers indicate ill-conditioned problems; small perturbations cause large solution changes regardless of algorithm choice.

## Questions

```yaml
- question: "A scientist finds that changing the last digit of one entry in b causes the solution x to change drastically. Their colleague suggests switching from Gaussian elimination to a more sophisticated iterative solver. Will this help?"
  type: multiple-choice
  options:
    - "Yes — iterative solvers are more numerically stable and will produce more accurate results"
    - "No — the sensitivity of x to perturbations in b is determined by κ(A), a property of the matrix, not the algorithm"
    - "Yes — but only if the iterative method also uses higher-precision floating point"
    - "No — the only fix is to eliminate the measurement error in b, after which any algorithm works"
  answer: 1
  explanation: "The condition number κ(A) measures how much the problem amplifies errors, not how much the algorithm does. A large κ(A) means that even tiny changes in b can produce large changes in x — this is true regardless of which algorithm is used. Switching solvers can improve stability (reduce algorithm-introduced rounding errors), but it cannot make the solution less sensitive to perturbations in the data. The problem is intrinsically ill-conditioned; no algorithm can extract information that isn't there."

- question: "A matrix A has condition number κ(A) = 10⁸. If you solve Ax = b using double-precision arithmetic (about 16 significant decimal digits), approximately how many accurate significant digits can you expect in your solution?"
  type: multiple-choice
  options:
    - "16 — double-precision always delivers 16 accurate digits regardless of the matrix"
    - "About 8 — roughly 16 − log₁₀(κ(A)) significant digits survive"
    - "0 — any condition number above 1 renders the solution meaningless"
    - "It depends on the algorithm; partial pivoting can recover all 16 digits"
  answer: 1
  explanation: "The condition number bounds relative error in x by κ(A) × (relative error in data). Double precision represents numbers to about 16 decimal digits, so floating-point round-off introduces relative errors of about 10⁻¹⁶. Multiplied by κ(A) = 10⁸, this gives up to 10⁻⁸ relative error in x — about 8 accurate digits. With κ(A) = 10¹⁶ on a 16-digit machine, the entire solution would be meaningless. This loss is intrinsic to the problem, not to the algorithm."

- question: "An orthogonal matrix Q (where Q^T Q = I) has condition number κ(Q) = 1, making it perfectly conditioned."
  type: true-false
  answer: true
  explanation: "An orthogonal matrix preserves vector lengths: ||Qx|| = ||x|| for all x. This means ||Q|| = 1 and ||Q⁻¹|| = ||Q^T|| = 1, so κ(Q) = ||Q|| · ||Q⁻¹|| = 1. Geometrically, Q only rotates and reflects the unit sphere — it maps it to itself, not to an elongated ellipsoid. A system Qx = b is maximally well-conditioned: perturbations in b produce equally-sized perturbations in x, with no amplification at all."

- question: "Gaussian elimination with partial pivoting can reduce the condition number of an ill-conditioned matrix, improving how accurately the solution reflects the true answer."
  type: true-false
  answer: false
  explanation: "Partial pivoting improves the numerical stability of the elimination algorithm — it prevents unnecessary amplification of rounding errors introduced during computation. But pivoting does not change the condition number, which is a property of the matrix A itself, not the computation. If A is ill-conditioned, the underlying problem is ill-conditioned regardless of how you solve it. Pivoting helps you reach the 'best possible' numerical answer given κ(A), but that best possible answer may still be highly inaccurate if κ(A) is large."

- question: "Explain in your own words why an ill-conditioned system cannot be 'fixed' by using a better algorithm, and what the appropriate response is when you discover that κ(A) is very large."
  type: short-answer
  answer: "An ill-conditioned system is one where the data (A and b) do not contain enough information to determine x precisely — small uncertainties or errors in the data map to large uncertainties in the solution. This is a property of the problem, not the computation. No algorithm can extract precision that isn't present in the inputs. When κ(A) is large, the right responses are: question whether the problem is well-posed, look for sources of near-linear dependence in A, or apply regularization (e.g., Tikhonov regularization) which modifies the problem to trade sensitivity for stability."
  explanation: "This reflects the core principle: numerical algorithms solve mathematical problems; they cannot improve the mathematical problem itself. The condition number is the bridge between data quality (relative error in A and b) and solution quality (relative error in x). A condition number of 10¹² on a 16-digit machine means 12 digits are consumed by error amplification, leaving at most 4 meaningful digits — and no algorithm changes that arithmetic. Understanding this shifts the practitioner's attention from 'which solver?' to 'is this a well-posed problem?'"
```

## Explainer

When you solve a linear system Ax = b using Gaussian elimination with pivoting, you obtain a numerical answer — but how much should you trust it? The answer depends not on your algorithm's quality, but on the problem itself. The **condition number** κ(A) is the quantity that tells you how sensitive the solution is to small perturbations in the data, regardless of how you solve the system.

To build intuition, think of κ(A) as an "error amplification factor." If the data in b has relative errors of size ε (due to measurement noise or floating-point representation), the computed solution x can have relative errors up to roughly κ(A) · ε. If κ(A) = 10³ and your data has 6 significant digits (ε ≈ 10⁻⁶), you might lose 3 of those digits — leaving only 3 significant digits in your solution. If κ(A) = 10¹², you lose 12 digits, and on a 16-digit double-precision machine, your "solution" may be numerically meaningless even with a perfect algorithm.

The formal definition κ(A) = ||A|| · ||A⁻¹|| measures how much the matrix can stretch vectors (||A||) and how much the inverse can then amplify perturbations (||A⁻¹||). A geometric picture: a well-conditioned matrix maps the unit sphere to a modestly elongated ellipsoid; an ill-conditioned matrix maps it to a very thin needle — and when the needle gets perturbed, recovering the preimage amplifies the perturbation enormously. An orthogonal matrix has κ = 1 (it only rotates, never stretches), so it is perfectly conditioned.

**Ill-conditioning** is a property of the problem, not the algorithm. No amount of clever pivoting or iterative refinement can rescue a truly ill-conditioned system, because the information in b simply does not determine x precisely. Common sources of ill-conditioning include nearly linearly dependent rows or columns, matrices with rows spanning widely different scales, and the **Hilbert matrix** (whose (i,j) entry is 1/(i+j−1)) — a famous example whose condition number grows exponentially with size. When you encounter κ(A) >> 1, the right response is not to seek a better algorithm but to reconsider whether the problem is well-posed, or to employ regularization techniques that trade solution sensitivity for solution stability.
