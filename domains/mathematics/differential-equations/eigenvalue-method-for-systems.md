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
stage: formal-systems
status: draft
---

# Eigenvalue Method for Systems of ODEs

## Core Idea
To solve y' = Ay, find eigenvalues λ and eigenvectors v of A. Each eigenvalue-eigenvector pair gives a solution y = e^{λt}v. For complex eigenvalues, extract real and imaginary parts to form real-valued oscillating solutions.

## How It's Best Learned
Work through 2×2 systems step-by-step: compute det(A - λI) = 0, find λ, solve (A - λI)v = 0 for v. Construct the general solution and verify by substitution.

## Common Misconceptions
- Forgetting that real eigenvector entries are required for real-valued solutions; complex eigenvalues give oscillations. - Not recognizing that repeated eigenvalues may not have enough linearly independent eigenvectors (generalized eigenvectors needed). - Confusing eigenvectors of A with solutions to the ODE system.

## Explainer

To solve a single first-order linear ODE y' = ay, you know the answer is y = Ce^{at} — an exponential, where a is the coefficient. The eigenvalue method generalizes this to a system of n coupled equations written as y' = Ay, where y is a vector of n unknown functions and A is an n×n matrix. The key insight is the same: look for solutions of the form y = e^{λt}v, where λ is a scalar and v is a constant vector. Substituting y = e^{λt}v into y' = Ay gives λe^{λt}v = Ae^{λt}v, and dividing by the nonzero scalar e^{λt} gives Av = λv. This is exactly the **eigenvalue equation** from linear algebra: v must be an eigenvector of A with eigenvalue λ.

So the method is: find the eigenvalues and eigenvectors of the matrix A, then construct solutions. For a 2×2 system, you compute det(A − λI) = 0 to find two eigenvalues λ₁ and λ₂. For each eigenvalue λᵢ, you solve (A − λᵢI)v = 0 to find the corresponding eigenvector vᵢ. Each pair gives an independent solution y = e^{λᵢt}vᵢ. The general solution is their linear combination: y = c₁e^{λ₁t}v₁ + c₂e^{λ₂t}v₂. You determine the constants c₁ and c₂ from initial conditions.

When the eigenvalues are complex — which happens when the characteristic polynomial has no real roots — the solutions still work, but you must extract real-valued solutions. If λ = α + βi is a complex eigenvalue with eigenvector v = p + qi (where p and q are real vectors), then the complex solution e^{λt}v expands using Euler's formula: e^{(α+βi)t}(p + qi) = e^{αt}[(cos βt)p − (sin βt)q] + ie^{αt}[(sin βt)p + (cos βt)q]. The real and imaginary parts are each real-valued solutions, and together they replace the pair of complex solutions. This is why complex eigenvalues produce oscillatory behavior in the system — the sin and cos terms encode rotations in the solution space.

The eigenvalue method works because the exponential structure e^{λt}v perfectly matches the structure of the system y' = Ay — the derivative of an exponential is proportional to itself, and a matrix-vector product with an eigenvector is proportional to the same vector. When A has n linearly independent eigenvectors (which is guaranteed if all eigenvalues are distinct, and is the usual case), the n independent solutions span the full solution space, and every solution is a linear combination of them. This is the **diagonalization** of the system: in the eigenvector basis, A acts by simply scaling each component, so the coupled system decouples into n independent scalar equations, each solved by an exponential.
