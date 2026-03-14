---
id: convergence-iterative-methods
title: Convergence of Iterative Methods
domain: mathematics
course: numerical-analysis
prerequisites:
- id: successive-over-relaxation
  type: soft
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- power-method-eigenvalues
tags:
- convergence
- iterative-methods
- spectral-radius
stage: abstract-reasoning
status: draft
---

# Convergence of Iterative Methods

## Core Idea
For iterative methods like Jacobi and Gauss-Seidel, convergence occurs if and only if the spectral radius (largest absolute eigenvalue) of the iteration matrix is less than 1. The spectral radius determines the asymptotic convergence rate: smaller spectral radius means faster convergence. This theorem connects linear algebra to iterative algorithm design.

## How It's Best Learned
For simple 2×2 systems, compute the iteration matrix and its eigenvalues, predicting convergence behavior analytically and comparing to numerical results.

## Common Misconceptions
- Thinking diagonal dominance guarantees fast convergence; it only guarantees convergence, possibly slowly.
- Confusing spectral radius with condition number; they measure different aspects of matrix behavior.
