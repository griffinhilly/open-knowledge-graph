---
id: power-method-eigenvalues
title: Power Method for Eigenvalues
domain: mathematics
course: numerical-analysis
prerequisites:
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- qr-algorithm-eigenvalues
tags:
- power-method
- eigenvalue-computation
- dominant-eigenvalue
stage: advanced
status: draft
---

# Power Method for Eigenvalues

## Core Idea
The power method finds the dominant eigenvalue (largest in magnitude) and corresponding eigenvector by iterating x^{(k+1)} = Ax^{(k)} / ||Ax^{(k)}||. The method converges linearly with rate |λ₂/λ₁| when |λ₁| > |λ₂|. It is simple and efficient for sparse matrices but finds only the dominant eigenvalue.
