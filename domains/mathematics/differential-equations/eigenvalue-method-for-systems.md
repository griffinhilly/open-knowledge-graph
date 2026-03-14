---
id: eigenvalue-method-for-systems
title: Eigenvalue Method for Systems of ODEs
domain: mathematics
course: differential-equations
prerequisites:
- id: systems-of-first-order-linear-odes
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- phase-portraits-for-linear-systems
tags:
- systems
- eigenvalue
- diagonalization
stage: advanced
status: draft
---

# Eigenvalue Method for Systems of ODEs

## Core Idea
To solve y' = Ay, find eigenvalues λ and eigenvectors v of A. Each eigenvalue-eigenvector pair gives a solution y = e^{λt}v. For complex eigenvalues, extract real and imaginary parts to form real-valued oscillating solutions.

## How It's Best Learned
Work through 2×2 systems step-by-step: compute det(A - λI) = 0, find λ, solve (A - λI)v = 0 for v. Construct the general solution and verify by substitution.

## Common Misconceptions
- Forgetting that real eigenvector entries are required for real-valued solutions; complex eigenvalues give oscillations. - Not recognizing that repeated eigenvalues may not have enough linearly independent eigenvectors (generalized eigenvectors needed). - Confusing eigenvectors of A with solutions to the ODE system.
