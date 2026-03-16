---
id: state-transition-matrix-solution-computation
title: State Transition Matrix and Solution Computation
domain: engineering
course: control-systems
prerequisites:
- id: state-transition-matrix
  type: hard
- id: state-space-representation-control
  type: hard
builds-toward:
- state-observer-full-and-partial-observation
tags:
- state-space
- exponential-matrix
- time-domain-solution
- discretization
stage: abstract-reasoning
status: draft
---

# State Transition Matrix and Solution Computation

## Core Idea
The state transition matrix Φ(t) = eAt solves the homogeneous state equation ẋ = Ax without Laplace transforms. The complete solution is x(t) = Φ(t)x(0) + ∫₀ᵗ Φ(t−τ)Bu(τ)dτ. Computation of eAt can be done via Laplace transform inversion or diagonalization.

## Explainer

The **state transition matrix** eAt is the matrix analog of the scalar exponential eat that solves scalar first-order ODEs. Recall from state-space representation that a linear system evolves as ẋ = Ax + Bu. The homogeneous solution (no input) starting from initial condition x(0) is simply x(t) = eAt x(0) — the matrix exponential propagates the initial state vector forward in time, stretching and rotating it through state space according to the dynamics encoded in A.

Computing eAt by hand uses two main strategies. The first is via the Laplace transform: eAt = L⁻¹{(sI − A)⁻¹}. Since you already compute (sI − A) in state-space analysis, inverting it and taking the inverse Laplace transform yields Φ(t) directly. The second strategy is **diagonalization**: if A = PΛP⁻¹ where Λ is the diagonal matrix of eigenvalues, then eAt = PeΛtP⁻¹, and eΛt is trivial — a diagonal matrix of scalar exponentials eλᵢt. Diagonalization works whenever A has distinct eigenvalues; repeated eigenvalues require the Jordan form.

The complete state response with inputs uses the **convolution integral**: x(t) = Φ(t)x(0) + ∫₀ᵗ Φ(t−τ)Bu(τ)dτ. The first term is the zero-input response — initial conditions propagated forward by Φ(t). The second term is the zero-state response — inputs accumulated over time, with each input Bu(τ) applied at time τ propagated forward for t−τ seconds before being added together. Think of Φ(t−τ) as the "aging" of each input: an impulse delivered at time τ has had t−τ seconds to evolve through the system dynamics by observation time t.

The eigenvalues of A directly determine the character of Φ(t). Negative real eigenvalues produce decaying modes; positive real eigenvalues produce exponentially growing (unstable) modes. Complex-conjugate eigenvalue pairs λ = σ ± jω produce oscillatory modes of the form eσt cos(ωt + φ). If all eigenvalues have strictly negative real parts, all modes decay and the system is asymptotically stable — Φ(t) → 0 as t → ∞. This is why eigenvalue analysis of A, which you encountered in state-space representation, gives you the complete qualitative picture of the transition matrix even before you compute it explicitly.
