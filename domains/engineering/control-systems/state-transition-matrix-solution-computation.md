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
stage: expert
status: validated
---

# State Transition Matrix and Solution Computation

## Core Idea
The state transition matrix Φ(t) = eAt solves the homogeneous state equation ẋ = Ax without Laplace transforms. The complete solution is x(t) = Φ(t)x(0) + ∫₀ᵗ Φ(t−τ)Bu(τ)dτ. Computation of eAt can be done via Laplace transform inversion or diagonalization.

## Questions

```yaml
- question: "A linear system has state matrix A with eigenvalues {-2, -3+4j, -3-4j}. What can you conclude about the state transition matrix Φ(t) = eAt as t → ∞?"
  type: multiple-choice
  options:
    - "Φ(t) grows without bound because complex eigenvalues produce oscillation that amplifies over time"
    - "Φ(t) → 0 because all eigenvalues have strictly negative real parts, so every mode decays"
    - "Φ(t) oscillates permanently at finite amplitude because of the complex eigenvalue pair"
    - "Nothing can be concluded without explicitly computing eAt from the matrix series"
  answer: 1
  explanation: "The eigenvalues of A determine the character of Φ(t) directly: each eigenvalue λ = σ + jω contributes a mode of the form eσt(cos ωt + ...). The real part σ determines growth or decay. Here all eigenvalues have σ < 0 (−2, −3, −3), so all modes decay exponentially. The complex pair produces oscillation, but a decaying oscillation — eAt → 0 as t → ∞. Stability is determined entirely by the real parts of eigenvalues; complex parts add oscillation but not growth."

- question: "In the complete solution x(t) = Φ(t)x(0) + ∫₀ᵗ Φ(t−τ)Bu(τ)dτ, what does the factor Φ(t−τ) inside the integral represent?"
  type: multiple-choice
  options:
    - "The input applied at time τ, scaled by the system's DC gain"
    - "The inverse of the transition matrix, used to back-propagate the current state"
    - "The evolution of an impulse input applied at time τ through the remaining t−τ seconds of system dynamics"
    - "A weighting function that normalizes the input magnitude across the integration interval"
  answer: 2
  explanation: "The convolution integral accumulates the effect of all inputs over time. At each instant τ, the input Bu(τ) enters the system as an effective impulse. That impulse then evolves through the system dynamics for the remaining t−τ seconds before the observation time t — and Φ(t−τ) is exactly the transition matrix that describes how a state vector is propagated forward by t−τ seconds. Summing (integrating) these 'aged' input contributions from τ = 0 to τ = t gives the total zero-state response. Older inputs (small τ, large t−τ) have been propagated longer and carry the imprint of the system's dynamics more heavily."

- question: "The eigenvalues of the state matrix A completely determine whether the zero-input response of a linear system is stable, oscillatory, or divergent — without requiring explicit computation of eAt."
  type: true-false
  answer: true
  explanation: "Each eigenvalue λᵢ of A contributes a mode eλᵢt to Φ(t). Real negative eigenvalues → exponential decay. Real positive eigenvalues → exponential growth (unstable). Complex pairs σ ± jω → oscillation at frequency ω with growth/decay rate σ. Purely imaginary pairs → undamped oscillation. So reading the eigenvalues directly tells you the qualitative behavior of all modes without computing the full matrix exponential. This is why stability analysis focuses on eigenvalue locations in the complex plane."

- question: "A linear system whose state transition matrix Φ(t) does not decay to zero is typically unstable and will produce unbounded output for any input."
  type: true-false
  answer: false
  explanation: "A system with purely imaginary eigenvalues (e.g., λ = ±jω) has a transition matrix that oscillates at constant amplitude — Φ(t) does not decay to zero, but the system is marginally stable, not unstable. For bounded inputs, outputs remain bounded (BIBO stable in some formulations). Only when eigenvalues have strictly positive real parts does Φ(t) grow without bound and produce unbounded outputs. The distinction between asymptotic stability (all eigenvalues strictly in left half-plane), marginal stability (eigenvalues on imaginary axis), and instability (any eigenvalue in right half-plane) is critical for control design."

- question: "Why does computing eAt by diagonalization require A to have distinct eigenvalues, and what method must be used when eigenvalues repeat?"
  type: short-answer
  answer: "Diagonalization requires that A = PΛP⁻¹, where P is the matrix of eigenvectors and Λ is diagonal. This is only possible when A has n linearly independent eigenvectors — which is guaranteed when eigenvalues are distinct but not when they repeat. For a repeated eigenvalue, the eigenvector set may be deficient (fewer independent eigenvectors than the eigenvalue's algebraic multiplicity). In this case, A must be reduced to Jordan canonical form J = P⁻¹AP, where J has the eigenvalues on the diagonal and 1s on the superdiagonal of each Jordan block. The matrix exponential then involves terms of the form t^k e^λt corresponding to the Jordan block structure."
  explanation: "The physical meaning: a Jordan block of size 2 for eigenvalue λ produces modes eλt and t·eλt. The polynomial factor t multiplying the exponential is the hallmark of a defective matrix. For stable systems (Re(λ) < 0), these modes still decay to zero (exponential beats polynomial), but they can cause large transient responses before doing so."
```

## Explainer

The **state transition matrix** eAt is the matrix analog of the scalar exponential eat that solves scalar first-order ODEs. Recall from state-space representation that a linear system evolves as ẋ = Ax + Bu. The homogeneous solution (no input) starting from initial condition x(0) is simply x(t) = eAt x(0) — the matrix exponential propagates the initial state vector forward in time, stretching and rotating it through state space according to the dynamics encoded in A.

Computing eAt by hand uses two main strategies. The first is via the Laplace transform: eAt = L⁻¹{(sI − A)⁻¹}. Since you already compute (sI − A) in state-space analysis, inverting it and taking the inverse Laplace transform yields Φ(t) directly. The second strategy is **diagonalization**: if A = PΛP⁻¹ where Λ is the diagonal matrix of eigenvalues, then eAt = PeΛtP⁻¹, and eΛt is trivial — a diagonal matrix of scalar exponentials eλᵢt. Diagonalization works whenever A has distinct eigenvalues; repeated eigenvalues require the Jordan form.

The complete state response with inputs uses the **convolution integral**: x(t) = Φ(t)x(0) + ∫₀ᵗ Φ(t−τ)Bu(τ)dτ. The first term is the zero-input response — initial conditions propagated forward by Φ(t). The second term is the zero-state response — inputs accumulated over time, with each input Bu(τ) applied at time τ propagated forward for t−τ seconds before being added together. Think of Φ(t−τ) as the "aging" of each input: an impulse delivered at time τ has had t−τ seconds to evolve through the system dynamics by observation time t.

The eigenvalues of A directly determine the character of Φ(t). Negative real eigenvalues produce decaying modes; positive real eigenvalues produce exponentially growing (unstable) modes. Complex-conjugate eigenvalue pairs λ = σ ± jω produce oscillatory modes of the form eσt cos(ωt + φ). If all eigenvalues have strictly negative real parts, all modes decay and the system is asymptotically stable — Φ(t) → 0 as t → ∞. This is why eigenvalue analysis of A, which you encountered in state-space representation, gives you the complete qualitative picture of the transition matrix even before you compute it explicitly.
