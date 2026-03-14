---
id: qr-algorithm
title: QR Algorithm
domain: mathematics
course: numerical-analysis
prerequisites:
- id: power-method-eigenvalues
  type: hard
tags:
- qr-algorithm
- eigenvalues
- qr-decomposition
stage: abstract-reasoning
status: draft
---

# QR Algorithm

## Core Idea
The QR algorithm iteratively computes QR decomposition A_k = Q_k R_k and sets A_{k+1} = R_k Q_k, creating a sequence similar to A_k. This sequence converges to a Schur form (upper triangular for real matrices), revealing all eigenvalues on the diagonal. The QR algorithm is highly efficient, stable, and the foundation of modern eigenvalue solvers.
