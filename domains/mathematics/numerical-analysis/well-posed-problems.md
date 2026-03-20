---
id: well-posed-problems
title: Well-Posed Problems
domain: mathematics
course: numerical-analysis
prerequisites:
- id: condition-number
  type: hard
tags:
- well-posed
- hadamard
- existence-uniqueness
stage: formal-systems
status: draft
---

# Well-Posed Problems

## Core Idea
A problem is well-posed (Hadamard) if (1) a solution exists, (2) it is unique, and (3) it depends continuously on input data. Ill-posed problems violate one or more conditions and are numerically unstable. Understanding well-posedness guides method selection; ill-posed problems may require regularization to be numerically tractable.

## Explainer

Your study of the **condition number** gave you a way to measure how sensitive a problem's output is to small perturbations in its input — a large condition number flags a problem where tiny errors get amplified. Well-posedness is the conceptual layer beneath that: before asking *how much* a solution changes, you need to ask whether the solution framework is sound at all. Hadamard's three conditions define what it means for a mathematical problem to be "solvable in a meaningful sense."

The three conditions address three distinct failure modes. **Existence**: a solution to the problem must actually exist. If you pose a linear system Ax = b but b lies outside the column space of A, there is no exact solution — numerical methods will chase a mirage. **Uniqueness**: the solution must be the only one. A linear system with infinitely many solutions (underdetermined or rank-deficient) has no well-defined answer; any numerical method will find a different solution depending on its starting point or floating-point path. **Continuous dependence**: small changes in the problem data must produce only small changes in the solution. This is the condition that connects directly to what you know about condition numbers — if a problem lacks continuous dependence, it is inherently numerically unstable regardless of the method used.

The classic ill-posed example is **numerical differentiation**. The mathematical problem — find f'(x) given f — is perfectly well-defined for smooth functions, but as a numerical problem it violates continuous dependence. Adding a small high-frequency oscillation ε·sin(ωx) to f changes the function by ε in L∞ norm, but changes its derivative by εω, which can be enormous. No matter how carefully you implement a finite difference formula, the derivative amplifies measurement noise catastrophically. The problem is ill-posed in the sense that the map from f to f' is not continuously dependent on the data.

Understanding well-posedness tells you *why* certain numerical problems are hard, not just *that* they are hard. When a problem is ill-posed, the cure is usually **regularization**: modifying the problem by adding a constraint or penalty that restores continuous dependence, at the cost of slightly biasing the solution. Examples include Tikhonov regularization for ill-conditioned linear systems, truncated SVD for rank-deficient matrices, and smoothness priors in inverse problems. Recognizing that your problem is ill-posed is the first step; regularization is the engineering response. Without this conceptual diagnosis, you might keep refining your algorithm and never understand why convergence fails.
