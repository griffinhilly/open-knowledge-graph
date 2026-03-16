---
id: systems-first-order-linear-odes
title: Systems of First-Order Linear Differential Equations
domain: mathematics
course: differential-equations
prerequisites:
- id: first-order-linear-odes
  type: hard
- id: matrix-operations
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
builds-toward:
- matrix-exponential-method
- phase-portraits-linear-systems
tags:
- systems
- matrix-form
- fundamental
stage: formal-systems
status: draft
---

# Systems of First-Order Linear Differential Equations

## Core Idea
A system dx/dt = Ax + f(t) in matrix form unifies high-order and coupled equations. The homogeneous solution x_h uses eigenvalues λ and eigenvectors v of A: x_h = Σ cᵢe^(λᵢt)vᵢ. Complex eigenvalues give oscillatory components; repeated eigenvalues require generalized eigenvectors. Systems are more general than high-order equations but reveal structure through linear algebra.

## Explainer

You already know how to solve a single first-order linear ODE like dx/dt = ax: the solution is x(t) = Ce^(at). A system of first-order linear ODEs is a collection of such equations that are coupled — the rate of change of each variable depends on the current values of all variables. The matrix form dx/dt = Ax compresses this coupling into a single equation that looks exactly like the scalar case, and the solution strategy follows the same pattern, powered by the eigenvalue theory you know from linear algebra.

Consider two coupled equations: dx₁/dt = 2x₁ + x₂ and dx₂/dt = x₁ + 2x₂. Written as a system, this is ẋ = Ax where A = [[2,1],[1,2]]. The **eigenvalues** of A are the values λ for which Av = λv has a nonzero solution v. They govern the long-term behavior: eigenvalue 3 gives a solution that grows like e^(3t), eigenvalue 1 gives e^(t). For each eigenvalue λᵢ with eigenvector vᵢ, the vector function x(t) = e^(λᵢt)vᵢ is a solution to the homogeneous system. This is the matrix analogue of Ce^(at) — instead of a scalar constant C, the direction is fixed by the eigenvector. The general homogeneous solution combines all such solutions: x_h = c₁e^(λ₁t)v₁ + c₂e^(λ₂t)v₂ + ···, with constants determined by initial conditions.

**Complex eigenvalues** arise when the matrix has no real eigenvectors — the system is naturally oscillatory. A pair α ± βi gives complex exponential solutions e^((α+βi)t)v, which you unpack using Euler's formula into real-valued solutions involving e^(αt)cos(βt) and e^(αt)sin(βt). This is exactly what you saw in second-order ODEs with complex characteristic roots — the system form reveals the same phenomenon through the matrix's eigenvalues.

The connection to higher-order equations is direct and important. Any nth-order ODE y^(n) = f(y, y', ..., y^(n-1)) can be rewritten as a first-order system by introducing variables x₁ = y, x₂ = y', ..., xₙ = y^(n-1). The system matrix A has a specific "companion matrix" structure whose characteristic polynomial matches the original ODE's characteristic equation exactly. This means the eigenvalue approach and the characteristic equation approach are not two separate methods — they are the same method, with the system view exposing the underlying linear algebra more explicitly. The eigendecomposition of A also leads directly to the **matrix exponential** e^(At), which gives the solution x(t) = e^(At)x₀ in a form that unifies all cases and connects deeply to the structure of the coefficient matrix.
