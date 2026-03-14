---
id: convergence-iterative-linear-solvers
title: Convergence of Iterative Methods
domain: mathematics
course: numerical-analysis
prerequisites:
- id: successive-over-relaxation-sor
  type: soft
- id: eigenvalues-and-eigenvectors
  type: hard
tags:
- convergence-analysis
- spectral-radius
- iteration-matrix
stage: advanced
status: draft
---

# Convergence of Iterative Methods

## Core Idea
Iterative methods for linear systems converge if and only if the spectral radius ρ(G) of the iteration matrix G is less than 1. The convergence rate depends on ρ(G); smaller spectral radius means faster convergence. Different splittings (Jacobi, Gauss-Seidel, SOR) produce different iteration matrices with different spectral radii, explaining their varying convergence speeds.
