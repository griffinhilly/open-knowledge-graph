---
id: matrix-exponential-method
title: Matrix Exponential Method
domain: mathematics
course: differential-equations
prerequisites:
- id: systems-first-order-linear-odes
  type: hard
- id: diagonalization
  type: hard
builds-toward:
- phase-portraits-linear-systems
tags:
- matrix-exponential
- fundamental-matrix
- solution-formula
stage: advanced
status: draft
---

# Matrix Exponential Method

## Core Idea
The solution to dx/dt = Ax, x(0) = x₀ is x(t) = e^(At)x₀, where e^(At) is the matrix exponential. If A = PDP⁻¹ (diagonalizable), then e^(At) = Pe^(Dt)P⁻¹ is easy to compute. The matrix exponential encodes all solution behavior and naturally handles initial conditions. It is the matrix analog of the scalar solution x(t) = e^(at)x₀.
