---
id: matrix-exponential
title: Matrix Exponential and Differential Equations
domain: mathematics
course: linear-algebra
prerequisites:
- id: diagonalization-similar-matrices
  type: hard
builds-toward:
- applications-linear-algebra-modeling
tags:
- matrix-exponential
- odes
- systems
stage: formal-systems
status: draft
---

# Matrix Exponential and Differential Equations

## Core Idea
The matrix exponential eᴬ = Σ Aⁿ/n! solves the matrix ODE dX/dt = AX with initial condition X(0) = I, giving X(t) = eᴬᵗ. If A is diagonalizable, eᴬ = PeᴰPP⁻¹ where e^D is diagonal. Solutions to dx/dt = Ax are x(t) = eᴬᵗx₀. Jordan normal form provides formulas for eᴬᵗ in the non-diagonalizable case.
