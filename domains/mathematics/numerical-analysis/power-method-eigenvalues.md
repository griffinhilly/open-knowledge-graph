---
id: power-method-eigenvalues
title: Power Method for Eigenvalues
domain: mathematics
course: numerical-analysis
prerequisites:
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- qr-algorithm
tags:
- power-method
- eigenvalues
- iteration
stage: abstract-reasoning
status: draft
---

# Power Method for Eigenvalues

## Core Idea
The power method finds the largest (in absolute value) eigenvalue and its eigenvector by repeatedly multiplying a random vector by the matrix: v^{(k+1)} = Av^{(k)} / ‖Av^{(k)}‖. Convergence is geometric with rate determined by the ratio of the two largest eigenvalues. Simple to implement, the power method is practical for large sparse matrices but slow when eigenvalues are close.
