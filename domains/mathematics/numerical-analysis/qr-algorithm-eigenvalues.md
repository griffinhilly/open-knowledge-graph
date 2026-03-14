---
id: qr-algorithm-eigenvalues
title: QR Algorithm for Eigenvalues
domain: mathematics
course: numerical-analysis
prerequisites:
- id: power-method-eigenvalues
  type: soft
tags:
- qr-algorithm
- eigenvalue-algorithm
- convergence
stage: advanced
status: draft
---

# QR Algorithm for Eigenvalues

## Core Idea
The QR algorithm repeatedly factors A_k = Q_k R_k and sets A_{k+1} = R_k Q_k, preserving eigenvalues while converging to upper triangular form with eigenvalues on the diagonal. This method is more robust than power method, converging to all eigenvalues simultaneously. Shifted and Hessenberg variants improve efficiency.
