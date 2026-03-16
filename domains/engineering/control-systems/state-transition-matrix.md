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
- id: diagonalization
  type: soft
builds-toward:
- controllability-and-observability
tags:
- matrix-exponential
- state-transition
- free-response
- variation-of-parameters
stage: advanced
status: validated
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

## Explainer

In state-space form, the homogeneous equation ẋ = Ax describes how a system's state evolves freely from any initial condition. You already know from your prerequisite on state-space representation that x is a vector and A is a matrix encoding the dynamics. The challenge is solving this differential equation in the matrix setting. In scalar form, the equation ẋ = ax has the solution x(t) = e^{at}x(0) — exponential growth or decay. The **state transition matrix** Φ(t) = e^{At} is the exact matrix generalization: it "transitions" the initial state x(0) to the state at any future time t, giving x(t) = e^{At}x(0).

The key insight is that e^{At} is not computed by exponentiating each element of A. Instead, it is defined through the matrix Taylor series: e^{At} = I + At + (At)²/2! + (At)³/3! + … This infinite series always converges and has properties directly analogous to the scalar exponential — in particular, Φ(0) = I (the identity, because doing nothing means staying put), and Φ(t₁+t₂) = Φ(t₁)Φ(t₂) (transitions compose). For practical computation, the cleanest method uses your prerequisite on eigenvalues and diagonalization. If A = PΛP⁻¹ where Λ is diagonal, then e^{At} = Pe^{Λt}P⁻¹, and e^{Λt} is simply the diagonal matrix of scalar exponentials e^{λᵢt}. The eigenvalues of A directly control the natural response modes: negative real parts give decay, positive real parts give growth, imaginary parts give oscillation.

When inputs are present, the complete solution requires summing the free response and the forced response. The **variation of parameters** formula does this: x(t) = e^{At}x(0) + ∫₀ᵗ e^{A(t−τ)}Bu(τ)dτ. The second term is a convolution — at each past moment τ, the input Bu(τ) drives the state, and that contribution is then propagated forward by the state transition matrix for the remaining time (t−τ). This is the matrix analog of the scalar convolution integral you used for scalar LTI systems, with e^{At} playing the role of the impulse response.

An alternative computation route uses the Laplace transform, which converts the state equation into the algebraic problem (sI−A)X(s) = x(0) + BU(s). Solving gives X(s) = (sI−A)⁻¹x(0) + (sI−A)⁻¹BU(s), so the Laplace transform of the state transition matrix is Φ(s) = (sI−A)⁻¹. Inverting this back to time domain via partial fractions gives e^{At} explicitly — the poles of (sI−A)⁻¹ are exactly the eigenvalues of A, connecting the frequency-domain and time-domain pictures. When A is defective (repeated eigenvalues with insufficient eigenvectors), the Jordan form introduces polynomial-times-exponential terms like t·e^{λt}, which appear as poles of higher multiplicity in the Laplace domain.
