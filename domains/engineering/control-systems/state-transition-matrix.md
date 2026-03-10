---
id: state-transition-matrix
title: State Transition Matrix
domain: engineering
course: control-systems
prerequisites:
- id: state-space-representation-control
  type: hard
- id: eigenvalues-and-eigenvectors
  type: hard
- id: matrix-operations
  type: hard
builds-toward:
- controllability-and-observability
tags:
- matrix-exponential
- state-transition
- free-response
- variation-of-parameters
stage: advanced
status: draft
---

# State Transition Matrix

## Core Idea
The state transition matrix Φ(t) = e^{At} is the matrix exponential of At and solves the homogeneous state equation ẋ = Ax, giving x(t) = e^{At}x(0) for any initial condition. The complete state response including an input is x(t) = e^{At}x(0) + ∫₀ᵗ e^{A(t−τ)}Bu(τ)dτ (variation of parameters / convolution integral). The matrix exponential can be computed via eigendecomposition when A is diagonalizable, using Cayley-Hamilton reduction, or via the Laplace transform as Φ(s) = (sI−A)⁻¹. Key properties include Φ(0) = I, Φ(t₁+t₂) = Φ(t₁)Φ(t₂), and dΦ/dt = AΦ.

## How It's Best Learned
Compute e^{At} for 2×2 systems using both eigendecomposition and Laplace inversion to verify they agree. Start with diagonal A matrices (giving scalar exponentials on the diagonal) before tackling non-diagonal cases requiring Jordan form.

## Common Misconceptions
- e^{At} is NOT computed element-by-element — the matrix exponential is a fundamentally different operation from applying the scalar exponential to each matrix entry.
- For non-diagonalizable (defective) matrices, the Jordan form must be used, introducing polynomial-times-exponential terms (t·e^{λt}, t²·e^{λt}, etc.).
- The property dΦ/dt = AΦ holds; the reversed order dΦ/dt = ΦA does not in general because matrix multiplication is not commutative.
